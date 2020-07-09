'''
Created on May 3, 2020

@author: NOOK
'''
import os
from pathlib import Path
import warnings
import io
import requests
import urllib.parse
import numpy as np
import scipy.stats as stats
from scipy.stats import norm
from seasonal import fit_seasons, adjust_seasons, fit_trend
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pandas.plotting import register_matplotlib_converters
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

from scipy.optimize.minpack import curve_fit
from scipy.integrate import trapz
from sortedcontainers import SortedSet
from Population import loadPopulation, loadStatePopulations
from Deaths import updateDeaths
from Analysis4 import smooth

# from IHME import IHME
# import plotly
# import plotly.figure_factory as ff
from matplotlib import cm
import us

# Allocation of NYC data to counties
#  R. K. Wadhera, et al, "Variation in COVID-19 Hospitalizations and Deaths Across New York City Boroughs", April 29, 2020
#  https://jamanetwork.com/journals/jama/fullarticle/2765524
nycDeaths = {
    '36047': 132, # Kings/Brooklyn
    '36005': 173, # Bronx
    '36085': 117, # Richmond/Staten Island
    '36081': 154, # Queens
    '36061':  91 # New York/Manhattan
    }
nycHospitalizations = {
    '36047': 404, # Kings/Brooklyn
    '36005': 634, # Bronx
    '36085': 373, # Richmond/Staten Island
    '36081': 568, # Queens
    '36061': 331 # New York/Manhattan
    }

two2State = {  # yes these are redundant; but one is sorted by name and the other by 2 letter
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

state2Two = {v: k for k, v in two2State.items()}

home = os.path.expanduser('~')
pathToRepository = home + '/GITHUB/COVID-19'

def once(dataPath : str):
    path = dataPath + 'US-Counties-Population.xlsx'
    counties = pd.read_excel(path, 'CO-EST2019-ANNRES', skiprows=3, index_col=0, usecols=[0, 12])
    counties = counties[1:-6]
    print(counties)
    counties.to_csv( dataPath + 'US-Counties-Population.csv')
    return counties

def loadFIPSTable(dataPath:str):
    path = dataPath + 'laucnty16.csv'
    counties = pd.read_csv(path, encoding = "ISO-8859-1")
    stateCounties = dict() # by state dict's
    for row in counties.iterrows():
        cnsa = row[1]['County Name/State Abbreviation']
        if not ',' in cnsa:
            stateCounties['DC'] = dict()
            stateCounties['DC'][cnsa] = '%2.2d%3.3d' % (row[1]['State FIPS Code'], row[1]['County FIPS Code'])
            continue
        abb = cnsa.split(',')[1].strip()
        name = cnsa.split(',')[0].strip()
        if (not isinstance(abb, str)):
            continue
        if not abb in stateCounties :
            stateCounties[abb] = dict()
        sd = stateCounties[abb]
#         print(row)
        sd[name] = '%2.2d%3.3d' % (row[1]['State FIPS Code'], row[1]['County FIPS Code'])
    return stateCounties

def handleSpecialCounties(county):
    cname = county.replace('ottineau', 'Bottineau')
    cname = cname.replace('Doña', 'Dona')
    cname = cname.replace('Anchorage Municipality', 'Anchorage Borough/municipality')
    cname = cname.replace('Juneau City and Borough', 'Juneau Borough/city')
    cname = cname.replace('Juneau City and Borough', 'Juneau Borough/city')
    cname = cname.replace('Sitka City and Borough', 'Sitka Borough/city')
    cname = cname.replace('Wrangell City and Borough', 'Wrangell Borough/city')
    cname = cname.replace('Yakutat City and Borough', 'Yakutat Borough/city')
    return cname
    
def loadCountyPopulation( dataPath : str, fipsTable : dict):
    path = dataPath + 'US-Counties-Population.csv'
    population = pd.read_csv(path, index_col=0) # pd.read_excel(path, 'US-Counties-Population')
#     print(deaths.index)
    cpop = dict()
    for where in population.index :
        fields = where.split(',')
        state = fields[1].strip()
        county = fields[0].strip()[1:]
        if len(state) > 0 and state in state2Two and state2Two[state] in fipsTable:
#             print(state2Two[state], county)
            stateCounties = fipsTable[state2Two[state]]
            cname = handleSpecialCounties(county)
#             if cname == 'Kalawao County':
#                 continue            
            if not cname in stateCounties :
                cname = county + '/city'
                if not cname in stateCounties :
                    cname = county + '/town'
                    if not cname in stateCounties :
                        print( '?~', state, county, cname)
                        continue
            cpop[stateCounties[cname]] = population.loc[where]['2019']
        else :
            print('?+', state)
    return cpop 

def loadCountyDeaths(dataPath : str, fipsTable : dict):
    path = dataPath + 'county-deaths.csv'
    deaths = pd.read_csv(path, index_col=0) 
    return loadCountyData(deaths, fipsTable, nycDeaths)

def nyc2Scale( nyc : dict):
    total = 0
    for b in nyc:
        total += nyc[b]
    for b in nyc:
        nyc[b] = nyc[b]/total
    return nyc

def loadCountyData( data, fipsTable : dict, nyc : dict):
    nyc = nyc2Scale(nyc)
    cdead = dict()
    for where in data.columns:
        fields = where.split(',')
        state = fields[1].strip()
        county = fields[0].strip()
        if len(state) > 0 and state in state2Two and state2Two[state] in fipsTable:
#             print(state2Two[state], county)
            stateCounties = fipsTable[state2Two[state]]
            cname = handleSpecialCounties(county);
#             if cname == 'Kalawao County':
#                 continue
            if not cname in stateCounties :
                cname = county + '/city'
                if not cname in stateCounties :
                    cname = county + '/town'
                    if not cname in stateCounties :
                        print( '?', state, county, cname)
                        continue
            cdead[stateCounties[cname]] = data.iloc[-1][where]
        else :
            print('?@', state)
    # spread NYC deaths across 5 boroughs per https://jamanetwork.com/journals/jama/fullarticle/2765524
    cdead['36047'] = nyc['36047'] * cdead['36061'] # Kings
    cdead['36005'] = nyc['36005'] * cdead['36061'] # Bronx
    cdead['36085'] = nyc['36085'] * cdead['36061'] # Richmond
    cdead['36081'] = nyc['36081'] * cdead['36061'] # Queens
    cdead['36061'] = nyc['36061'] * cdead['36061'] # New York
    
    return cdead 
        
    
def main(dataPath : str):
    fipsTable = loadFIPSTable(dataPath)
    countyPopulation = loadCountyPopulation(dataPath, fipsTable)
    countyDeaths = loadCountyDeaths(dataPath, fipsTable)
    return countyPopulation, countyDeaths, fipsTable
#     print(countyPopulation)

def colorTupleToString(t):
        r = min(255, int(255.0 * t[0]))
        g = min(255, int(255.0 * t[1]))
        b = min(255, int(255.0 * t[2]))
        return ( '#%2.2x%2.2x%2.2x' % (r, g, b) )
    
# def mapcolors(values, nlevels):
#     minv = np.min(values)
#     maxv = np.max(values)
#     endpts = list(np.linspace(minv, maxv, nlevels,endpoint=False))
#     cs = []
# 
#     for i in range(0, nlevels+1):
#         t = cm.jet(int(255.0*i/(nlevels+1)))
#         r = min(255, int(255.0 * t[0]))
#         g = min(255, int(255.0 * t[1]))
#         b = min(255, int(255.0 * t[2]))
#         cs.append( '#%2.2x%2.2x%2.2x' % (r, g, b) )
#     return cs, endpts

def loadLandAreas(dataPath : str):
    areas = pd.read_csv(dataPath + 'county-data.csv')
    print(areas)
    fa = dict()
    out = open('landareas.csv', 'w')
    for row in areas.iterrows() :
        fa[int(row[1]['fips'])] = row[1]['LND110210']
        print(int(row[1]['fips']), row[1]['LND110210'], file=out)
    out.close()
    return fa

class State:
    def __init__(self, fips : str):
        self.which = us.states.lookup(fips, field='fips');
        self.deaths = 0
        self.cases = 0
        self.population = 0
        self.counties = []
        
    def __str__(self):
        return '%s %3d %6.0f %6.3f %6.0f %6.3f %8.0f' % (self.which.abbr, len(self.counties), self.deaths, 1e6*self.deaths/self.population, self.cases, 1e6*self.cases/self.population, self.population)

    def add(self, county):
        self.counties.append(county)
        self.counties.sort(key=lambda x: x.deaths, reverse=True)
        self.deaths += county.deaths
        self.cases += county.cases
        self.population += county.population
        
class County:
    def __init__(self, state, fips, row):
        self.fips = fips
        self.name = row['County']
        self.state = state
        self.deaths = row['Deaths']
        self.cases = row['Cases']
        self.population = row['Population']
        
    def __str__(self):
        return '%s %-32s %6.0f %6.3f %6.0f %6.3f %8.0f' % (self.fips, self.name, self.deaths, 1e6*self.deaths/self.population, self.cases, 1e6*self.cases/self.population, self.population)
 
def statisticsString(deaths, cases, population):
    return '%6s %6.3f %6s %6.3f %8s' % ('{:6,.0f}'.format(deaths), 1e6*deaths/population, '{:6,.0f}'.format(cases), 1e6*cases/population, '{:8,.0f}'.format(population))
       
class Counties:
    def __init__(self):
        dataPath = home + '/GITHUB/COVIDtoTimeSeries/data/'
        self.fipsTable = loadFIPSTable(dataPath)
        self.countyPopulation = loadCountyPopulation(dataPath, self.fipsTable)
        if "Doña Ana County" in self.countyPopulation:
            self.countyPopulation["Dona Ana County"] = self.countyPopulation["Doña Ana County"]
            self.countyPopulation.pop("Doña Ana County")
        self.rfips = dict() # reverse fip
        for s in self.fipsTable.keys():
            d = self.fipsTable[s]
            for c in d.keys():
                self.rfips[d[c]] = c + ', ' + s
        
    def update(self, countyCases, countyDeaths, include=lambda pop: True):
        self.cases = loadCountyData(countyCases, self.fipsTable, nycHospitalizations)
        self.deaths = loadCountyData(countyDeaths, self.fipsTable, nycDeaths)
        fips = list(self.deaths.keys())
        values = list(self.deaths.values())
#         out = open('counties.csv', 'w')
        self.latest = pd.DataFrame(columns=['County', 'Cases', 'Deaths', 'Population', 'CaseRate', 'DeathRate'])
        for i in range(0,len(fips)):
            f = fips[i]
            if f in self.countyPopulation and include(self.countyPopulation[f]) :
#                 print(fips[i],',"'+self.rfips[fips[i]]+'",',self.cases[f],',',values[i],',', self.countyPopulation[fips[i]],',',1e6 * values[i] / self.countyPopulation[fips[i]], file=out)
                row = dict();
                row['County'] = self.rfips[fips[i]]
                row['Cases'] = self.cases[f]
                row['Deaths'] = values[i]
                row['Population'] = self.countyPopulation[fips[i]]
                row['CaseRate'] = 1e6 * row['Cases'] / row['Population']
                row['DeathRate'] = 1e6 * row['Deaths'] / row['Population']
                r = pd.DataFrame(row, index=[fips[i]])
                self.latest = self.latest.append(r, sort=False)
#             else:
#                 print('?-', f, values[i], self.cases[f], self.countyPopulation[f])
#         out.close()
        self.latest.sort_values('DeathRate', axis=0,ascending=False,inplace=True)
        self.latest['SumCases'] = self.latest['Cases'].cumsum()
        self.latest['SumDeaths'] = self.latest['Deaths'].cumsum()
        self.latest['SumPopulation'] = self.latest['Population'].cumsum()
        self.usPopulation = self.latest['SumPopulation'].iloc[-1]
        self.usCases = self.latest['SumCases'].iloc[-1]
        self.usDeaths = self.latest['SumDeaths'].iloc[-1]
        
        self.i25 = (len(self.latest[self.latest['SumDeaths'].le(0.25 * self.usDeaths)]))
        self.i50 = (len(self.latest[self.latest['SumDeaths'].le(0.50 * self.usDeaths)]))
        self.i75 = (len(self.latest[self.latest['SumDeaths'].le(0.75 * self.usDeaths)]))
        self.len = (len(self.latest))
        
        print('%4d %s' % (self.len, statisticsString( self.usDeaths, self.usCases, self.usPopulation)))
        
    def inventory(self):
        buildStates = dict()
        for i in range(0, self.len):
            f2 = self.latest.index[i][0:2]
            s = State(f2)
            if not f2 in buildStates:
                buildStates[f2] = s
            s = buildStates[f2]
            c = County(s, self.latest.index[i], self.latest.iloc[i])
            s.add(c)
        states = list(buildStates.values())
        states.sort(key=lambda x: x.which.abbr, reverse=False)
#         for state in states:
#             print(state)
        counties = buildStates['02'].counties
        counties.sort(key=lambda x: x.name, reverse=False)
        for c in counties:
            print(c)
        
        
    def printSubsets(self):
        def stateSubset(fr, to):
            buildStates = dict() # indexed by 2-digit state FIPS code; list of State objects
            for i in range(fr, to) :
                f2 = self.latest.index[i][0:2]
                s = State(f2)
                if not f2 in buildStates:
                    buildStates[f2] = s
                s = buildStates[f2]
                c = County(s, self.latest.index[i], self.latest.iloc[i])
                s.add(c)
            whichStates = list(buildStates.values())
            whichStates.sort(key=lambda x: x.deaths, reverse=True)
            return whichStates
        
        whichStates = stateSubset(0, self.i25)
        print(0.25, len(whichStates))
        for state in whichStates:
            print(state)
            for county in state.counties:
                print('  ', county)
                
        whichStates = stateSubset(self.i25, self.i50)
        print(0.5, len(whichStates))
        for state in whichStates:
            print(state)
            for county in state.counties:
                print('  ', county)
                
        print(0.75, self.i75-self.i50)
        print(1.00, self.len-self.i75)
        
if __name__ == '__main__':
    counties = Counties()
    dataPath = home + '/GITHUB/COVIDtoTimeSeries/data/'
    
    h = pd.read_csv(dataPath + "county-deaths.csv", parse_dates=True, index_col=0)
    hc = pd.read_csv(dataPath + "county-cases.csv", parse_dates=True, index_col=0)
    
#     fDeath = nyc2Scale(nycDeaths)
#     fCases = nyc2Scale(nycHospitalizations)
#     for f in nycDeaths:
#         h[f] = fDeath[f] * h["New York County, New York"]
#         hc[f] = fCases[f] * hc["New York County, New York"]
    #TODO add NY bourogh columns by allocation
    #TODO compute smooths /day deaths and cases for all counties
#     counties.update( hc, h )
#     counties.inventory()
    print('Larger Counties')
    counties.update( hc, h, include=lambda pop: pop>=50000 )
    rfips = dict()
    for s in counties.fipsTable.keys():
        d = counties.fipsTable[s]
        for c in d.keys():
            rfips[d[c]] = c + ', ' + two2State[s]
    for i in range(0,10) :
        print(h[[rfips[counties.latest.index[i]]]])
    counties.printSubsets()
    print('Smaller Counties')
    counties.update( hc, h, include=lambda pop: pop<50000 )
    counties.printSubsets()
    
    if False :
        outPath = home + '/GITHUB/COVIDtoTimeSeries/data/'
        countyPopulation, countyDeaths, fipsTable = main( outPath )
        rfips = dict()
        for s in fipsTable.keys():
            d = fipsTable[s]
            for c in d.keys():
                rfips[d[c]] = c + ', ' + s
        fips = list(countyDeaths.keys())
        values = list(countyDeaths.values())
        out = open('counties.csv', 'w')
        for i in range(0,len(fips)):
            def categeorize(rate):
                if rate <= 0:
                    return 0.0
                return 1e-3+np.ceil(np.log10(rate))
            
            f = fips[i]
            if f in countyPopulation :
                c = categeorize( 1e6 * values[i] / countyPopulation[fips[i]])
                print(fips[i],',"'+rfips[fips[i]]+'",',c,',',values[i],',', countyPopulation[fips[i]],',',1e6 * values[i] / countyPopulation[fips[i]], file=out)
                values[i] = c
        out.close()
#     lfips = []
#     lvalues = []
#     target = us.states.CA
#     for i in range(0,len(values)):
#         v = values[i]
#         stateFips = int(fips[i]) // 1000
#         if stateFips == int(target.fips) : # v == 0: # v >=1 and v < 4.0:
#             lfips.append(fips[i])
#             lvalues.append(int(v))
#     colorscale, endpts = mapcolors(values, 5-1) 
# #     print(colorscale)
#     colorscale = ['white', 'blue', 'yellow', 'orange', 'red']
#     colorscale = ['white', 
#                   colorTupleToString(cm.inferno(0)),
#                   colorTupleToString(cm.inferno(85)),
#                   colorTupleToString(cm.inferno(170)),
#                   colorTupleToString(cm.inferno(255)),
#                   ]
#     colorscale = np.array(colorscale)
#     order = np.unique(lvalues)
#     colorscale = colorscale[order]
#     endpts = [1,2,3,4,5,6] 
#     fig = ff.create_choropleth(
#         fips=lfips, values=lvalues, scope=[target.abbr],
# #         binning_endpoints=endpts,
#         colorscale=colorscale.tolist(), # order=order.tolist(),
#         show_state_data=True,
#         state_outline={'color': 'rgb(0,0,0)', 'width': 1.0},
#         show_hover=True,
# #         asp = 2.9,
#         title_text = 'USA County Death Rate Categories',
#         legend_title = 'Population'
#     )
#     fig.layout.template = None
#     fig.show()
#     plotly.io.orca.config.executable = '/Users/blinton/anaconda3/bin/orca'
#     fig.write_image("plotly.png")
