'''
Created on May 3, 2020

@author: NOOK
'''
import os
import copy
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
from Analysis import countries
from docutils.nodes import line

# Allocation of NYC data to counties
#  R. K. Wadhera, et al, "Variation in COVID-19 Hospitalizations and Deaths Across New York City Boroughs", April 29, 2020
#  https://jamanetwork.com/journals/jama/fullarticle/2765524
# More recent from NYC Health: https://raw.githubusercontent.com/nychealth/coronavirus-data/master/by-boro.csv
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
        
    
# def main(dataPath : str):
#     fipsTable = loadFIPSTable(dataPath)
#     countyPopulation = loadCountyPopulation(dataPath, fipsTable)
#     countyDeaths = loadCountyDeaths(dataPath, fipsTable)
#     return countyPopulation, countyDeaths, fipsTable
# #     print(countyPopulation)

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

def statisticsString(deaths, cases, population, deathRate=None, caseRate=None, sep=' '):
    dr = 'N/A' + sep
    if not deathRate is None:
        dr = '%6.3f%s' % (1e6*max(0,deathRate)/population, sep)
    cr = 'N/A' + sep
    if not caseRate is None:
        cr = '%6.3f%s' % (1e6*max(0,caseRate)/population, sep)
    return '%6s %6.3f%s %s%6s %9.3f%s %s%8s' % ('{:6,.0f}'.format(deaths)+sep, 1e6*deaths/population, sep, dr, '{:6,.0f}'.format(cases)+sep, 1e6*cases/population, sep, cr, '{:8,.0f}'.format(population)+sep)
       
class Group:
    def __init__(self):
        self.deaths = 0
        self.cases = 0
        self.population = 0
        
class State(Group):
    def __init__(self, fips : str):
        super().__init__()
        self.which = us.states.lookup(fips, field='fips');
        self.counties = []
        
    def toTableRow(self):
        return '|%s|%d counties|%s\n' % (self.which.abbr, len(self.counties), statisticsString(self.deaths, self.cases, self.population, sep='|')) 
           
    def __str__(self):
        return '%s %3d %s' % (self.which.abbr, len(self.counties), statisticsString(self.deaths, self.cases, self.population))

    def add(self, county):
        self.counties.append(county)
        self.counties.sort(key=lambda x: x.deaths, reverse=True)
        self.deaths += county.deaths
        self.cases += county.cases
        self.population += county.population
        
class County(Group):
    def __init__(self, state, fips, row):
        super().__init__()
        self.fips = fips
        self.name = row['County']
        self.state = state
        self.deaths = row['Deaths']
        self.cases = row['Cases']
        self.population = row['Population']
        self.deathRate = row['DeathRate']
        self.caseRate = row['CaseRate']
    
    def plot(self, ax1):
        ax1.plot(self.cases, self.deaths, linestyle='', markeredgecolor='none', marker='.' )
        if not self.caseRate is None:
            ax1.plot(self.caseRate, self.deathRate, linestyle='', markeredgecolor='none', marker='+' )
        
    def toTableRow(self):
        return '| |%s|%s\n' % (self.name.split(',',1)[0].split('/',1)[0], statisticsString(self.deaths, self.cases, self.population, self.deathRate, self.caseRate, sep='|')) 
           
    def __str__(self):
        return '%s %-40s %s' % (self.fips, self.name, statisticsString(self.deaths, self.cases, self.population, self.deathRate, self.caseRate))
 
class Counties(Group):
    def __init__(self):
        super().__init__()
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
                self.rfips[d[c]] = c + ', ' + two2State[s]
            
    def getTableHeader(self):
        header1 = ("|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|\n")
        header2 = ("|:--|:--|--:|--:|--:|--:|--:|--:|--:|\n")
        return [header1, header2]
        
    def update(self, countyCases, countyDeaths, deathTrend, casesTrend, include=lambda pop: True):
        self.cases = loadCountyData(countyCases, self.fipsTable, nycHospitalizations)
        self.deaths = loadCountyData(countyDeaths, self.fipsTable, nycDeaths)
        fips = list(self.deaths.keys())
        values = list(self.deaths.values())
#         out = open('counties.csv', 'w')
        self.latest = pd.DataFrame(columns=['County', 'Cases', 'Deaths', 'Population', 'PDR', 'CaseRate', 'DeathRate'])
        for i in range(0,len(fips)):
            f = fips[i]
            if f in self.countyPopulation and include(self.countyPopulation[f]) :
#                 print(fips[i],',"'+self.rfips[fips[i]]+'",',self.cases[f],',',values[i],',', self.countyPopulation[fips[i]],',',1e6 * values[i] / self.countyPopulation[fips[i]], file=out)
                row = dict();
                row['County'] = self.rfips[fips[i]]
                row['Cases'] = self.cases[f]
                row['Deaths'] = values[i]
                row['Population'] = self.countyPopulation[fips[i]]
                row['PDR'] = 1e6*values[i] / self.countyPopulation[fips[i]]
                if row['County'] in deathTrend:
                    row['CaseRate'] = (casesTrend[row['County']][-1]-casesTrend[row['County']][-2])  # delta cases/last day
                    row['DeathRate'] = (deathTrend[row['County']][-1]-deathTrend[row['County']][-2]) # delta deaths/last day
                else:
                    row['CaseRate'] = None
                    row['DeathRate'] = None
                r = pd.DataFrame(row, index=[fips[i]])
                self.latest = self.latest.append(r, sort=False)
#             else:
#                 print('?-', f, values[i], self.cases[f], self.countyPopulation[f])
#         out.close()
        self.latest.sort_values('Deaths', axis=0,ascending=False,inplace=True)
        self.latest['SumCases'] = self.latest['Cases'].cumsum()
        self.latest['SumDeaths'] = self.latest['Deaths'].cumsum()
        self.latest['SumPopulation'] = self.latest['Population'].cumsum()
        self.population = self.latest['SumPopulation'].iloc[-1]
        self.cases = self.latest['SumCases'].iloc[-1]
        self.deaths = self.latest['SumDeaths'].iloc[-1]
         
        self.i25 = (len(self.latest[self.latest['SumDeaths'].le(0.25 * self.deaths)]))
        self.i50 = (len(self.latest[self.latest['SumDeaths'].le(0.50 * self.deaths)]))
        self.i75 = (len(self.latest[self.latest['SumDeaths'].le(0.75 * self.deaths)]))
        self.len = (len(self.latest))
         
        print('%4d %s' % (self.len, statisticsString( self.deaths, self.cases, self.population)))
        
        self.subsets = []
        self.subsets.append( self.Subset( self, 0, self.i25 ) )
        self.subsets.append( self.Subset( self, self.i25, self.i50 ) )
        self.subsets.append( self.Subset( self, self.i50, self.i75 ) )
        self.subsets.append( self.Subset( self, self.i75, self.len ) )
        
#         fig, ax1 = plt.subplots()
#         ss = self.subsets[0]
#         ss.plot(ax1)
#         plt.show()
        
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
        
    def getTemplateDict(self, us : Group, sizeName : str) -> dict:
        fields = dict()
        fields.update({'gCount': '%d' % self.len} )
        fields.update({'gSize': sizeName})
        fields.update({'gPopulation': '{:,.0f}'.format(self.population)})
        fields.update({'gPctofUSPopulation': '%.2f' % (100*self.population / us.population)})
        fields.update({'gDeaths': '{:,.0f}'.format(self.deaths)})
        fields.update({'gCases': '{:,.0f}'.format(self.cases)})
        fields.update({'gPDR': '%.3f' % (1e6*self.deaths / self.population)})
        fields.update({'gPCR': '%.3f' % (1e6*self.cases / self.population)})
        fields.update({'gPctOfUSDeaths': '%.2f' % (100*self.deaths / us.deaths)})
        fields.update({'gPctOfUSCases': '%.2f' % (100*self.cases / us.cases)})
        
        for prefix, subset in zip(['g1', 'g2', 'g3', 'g4'], self.subsets):
            fields.update({prefix+'Pct': '%.2f' % (100*subset.deaths / self.deaths)})
            fields.update({prefix+'PctUSDeaths': '%.2f' % (100*subset.deaths / us.deaths)})
            fields.update({prefix+'MCounties': '{:,.0f}'.format(subset.to-subset.fr)})
            fields.update({prefix+'NStates': '%d' % len(subset.whichStates)})
            fields.update({prefix+'Population': '{:,.0f}'.format(subset.population)})
            fields.update({prefix+'PctUSPopulation': '%.2f' % (100*subset.population / us.population)})
#             fields.update({prefix+'Table': subset.tableSubset()} );
            
        return fields
    
    class Subset(Group):
        
        def __init__(self, counties, fr : int, to : int):
            super().__init__()
            print(self, fr, to, self.population )
            self.counties = counties
            self.fr = fr 
            self.to = to
            buildStates = dict() # indexed by 2-digit state FIPS code; list of State objects
            for i in range(fr, to) :
                f2 = self.counties.latest.index[i][0:2]
                s = State(f2)
                if not f2 in buildStates:
                    buildStates[f2] = s
                s = buildStates[f2]
                c = County(s, self.counties.latest.index[i], self.counties.latest.iloc[i])
                s.add(c)
            self.whichStates = list(buildStates.values())
            self.whichStates.sort(key=lambda x: x.deaths, reverse=True)
            for s in self.whichStates:
                self.deaths += s.deaths
                self.cases += s.cases
                self.population += s.population
    
        def tableSubset(self, basePath, deathRateTrend, casesRateTrend):
            lines = []
            for state in self.whichStates:
                lines.append('\n### %s ###\n' % state.which)
                
                path = '%s/%s.png' % (basePath, state.which)
                plotStateCounties(path, '%s' % state.which, deathRateTrend, casesRateTrend )
                
                for line in self.counties.getTableHeader():
                    lines.append(line)
                lines.append( state.toTableRow() )
                for county in state.counties:
                    lines.append( county.toTableRow() )
                lines.append('\n')
            txt = ''
            for line in lines:
                txt += line
            return txt
    
        def printSubsets(self):
            for state in self.whichStates:
                print(state)
                for county in state.counties:
                    print('  ', county)
        
        def plot(self, ax1):
            for state in self.whichStates:
                for county in state.counties:
                    county.plot(ax1)
 
shortNames = dict()

def plotStateCounties(path, state, deathRates, caseRates):
    data = dict()
    for c in deathRates.keys():
        if c.endswith(state):
            data[c] = (deathRates[c], caseRates[c])
    plotCountyRates( path, data )
       
def plotCountyRates(path, data, xmin=None, xmax=None, ymin=None, ymax=None ):            
    fig, ax1 = plt.subplots()
    ax1.set_title('7 Day Case Rate vs Death Rate Trajectories')
    ax1.set_xlabel("Deaths/day/1M")
    ax1.set_ylabel("Confirmed Cases/day/1M")
    for one in data.keys() :
        xy = data[one]
        color = next(ax1._get_lines.prop_cycler)['color']
        ax1.plot(xy[0],xy[1], color=color)
        ax1.scatter(xy[0][-1], xy[1][-1], color=color)
        ax1.annotate( shortNames[one], xy=(xy[0][-1], xy[1][-1]), color=color, xycoords='data',
                xytext=(5,5), textcoords='offset points')
#     ax1.set_xlim(xmin, xmax)
#     ax1.set_ylim(ymin, ymax)

    ax1.set_yscale('log')
    ax1.set_xscale('log')
    fig.tight_layout()
    plt.draw()
    fig.savefig(path)
    plt.close()      
    return [ax1.get_xlim()[1], ax1.get_ylim()[1]] 
        
def main():
    dataPath = home + '/GITHUB/COVIDtoTimeSeries/data/'    
    env = Environment(
        loader=FileSystemLoader(home + '/GITHUB/COVIDtoTimeSeries/covid/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template("COUNTIES.mdt")
    groupTemplate = env.get_template("COUNTIES_group.mdt")

    larger = Counties()
    smaller = copy.deepcopy(larger)
    all = copy.deepcopy(larger)

    
    h = pd.read_csv(dataPath + "county-deaths.csv", parse_dates=True, index_col=0)
    hc = pd.read_csv(dataPath + "county-cases.csv", parse_dates=True, index_col=0)
    
    # generate short county names
    for c in h.columns:
        name = c.split(',')[0].strip() # remove state
        name = name.split(' ')
        name = ' '.join( name[0:-1] )
        shortNames[c] = name
    print(shortNames)
    
    # reallocate NYC deaths to boroughs
    fDeath = nyc2Scale(nycDeaths)
    fCases = nyc2Scale(nycHospitalizations)
    for f in nycDeaths:
        if f != '36061':
            h[larger.rfips[f]] = fDeath[f] * h["New York County, New York"]
            hc[larger.rfips[f]] = fCases[f] * hc["New York County, New York"]
    h["New York County, New York"] = fDeath['36061'] * h["New York County, New York"]
    hc["New York County, New York"] = fCases['36061'] * hc["New York County, New York"]
    
    # LOWESS smooth death and case trends
    deathTrend = dict()
    casesTrend = dict()
    deathRateTrend = dict()
    casesRateTrend = dict()
    T = np.asarray(((h.index-h.index[0]).days)).reshape(-1, 1)
    target = 'New York County, New York' # 'Brevard County, Florida'
    for county in h.columns :
#         if county == target:
        if h[county].array[-1] >= 100:
            print('Smoothing ', county, h[county].array[-1])
            Y = np.asarray(h[county]).reshape(-1, 1)
            deathTrend[county] = smooth(Y[-22:,0], T[-22:,0])
            Y = np.asarray(h[county].diff()).reshape(-1, 1)
            S = smooth(Y[-7:,0], T[-7:,0])
            S[S < 0.1] = np.nan
            deathRateTrend[county] = S
            Y = np.asarray(hc[county]).reshape(-1, 1)
            casesTrend[county] = smooth(Y[-22:,0], T[-22:,0])
            Y = np.asarray(hc[county].diff()).reshape(-1, 1)
            S = smooth(Y[-7:,0], T[-7:,0])
            S[S < 0.1] = np.nan
            casesRateTrend[county] = S
#     print(','.join(['%.5f' % num for num in deathTrend[target]]))
#     print(','.join(['%.5f' % num for num in casesTrend[target]]))
    

    usa = Group()
    usa.population = sum(larger.countyPopulation.values())
    usa.deaths = h.iloc[-1].sum()
    usa.cases = hc.iloc[-1].sum()

    print('All Counties') 
    all.update( hc, h, deathTrend, casesTrend)
    allCounties = all.Subset( all, 0, all.len)
    
    print('Larger Counties')
    larger.update( hc, h, deathTrend, casesTrend, include=lambda pop: pop>=50000 )
    fields = ( larger.getTemplateDict(usa, 'larger'))
    largerTxt = groupTemplate.render(fields)
    print('Smaller Counties')
    smaller.update( hc, h, deathTrend, casesTrend, include=lambda pop: pop<50000 )
    fields = ( smaller.getTemplateDict(usa, 'smaller'))  
    smallerTxt = groupTemplate.render(fields)
    
    fields = dict();
    fields.update({'largerCounties': largerTxt}) 
    fields.update({'smallerCounties': smallerTxt}) 
    fields.update({'allCountiesTable': allCounties.tableSubset(home + '/GITHUB/COVIDtoTimeSeries/analysis/counties', deathRateTrend, casesRateTrend
                                                               )}) 
    fields.update({'TOC': statesTable()})
     
    out = open(home + '/GITHUB/COVIDtoTimeSeries/analysis/COUNTIES.md', 'w')
    print(template.render(fields), file=out)
    out.close()
    outPath = home + '/GITHUB/COVIDtoTimeSeries'
    os.system('git -C %s commit -a -m "daily update"' % outPath)
    os.system('git -C %s push' % outPath)
    print('========================================================')
#     counties.printSubsets()
#     print('Smaller Counties')
#     counties.update( hc, h, deathTrend, casesTrend, include=lambda pop: pop<50000 )
#     counties.printSubsets()
    
    
def statesTable():
    txt = "||||||\n|:-:|:-:|:-:|:-:|:-:|\n"
    i = 0
    
    for state in us.states.STATES:
        if not state is None:
            txt += ('|<a href="#%s">%s</a>' % (state.name.lower(), state.name))
            i += 1
            if (i >= 5):
                i = 0
                txt += ('|\n')
    return txt
    
if __name__ == '__main__':
    main()