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
from IHME import IHME
# import plotly
# import plotly.figure_factory as ff
from matplotlib import cm
import us
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

def once(dataPath : str):
    path = dataPath + 'US-Counties-Population.xlsx'
    counties = pd.read_excel(path, 'CO-EST2019-ANNRES', skiprows=3, index_col=0, usecols=[0, 12])
    counties = counties[1:-6]
    print(counties)
    counties.to_csv( dataPath + 'US-Counties-Population.csv')

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
            cname = county #.replace(" County", '').replace(' Parish', '').replace(' Borough', '').strip()
            if not cname in stateCounties :
                cname = county + '/city'
                if not cname in stateCounties :
                    cname = county + '/town'
                    if not cname in stateCounties :
                        print( '?', state, county, cname)
                        continue
            cpop[stateCounties[cname]] = population.loc[where]['2019']
        else :
            print('??', state)
    return cpop 

def loadCountyDeaths(dataPath : str, fipsTable : dict):
    path = dataPath + 'county-deaths.csv'
    deaths = pd.read_csv(path, index_col=0)    
    cdead = dict()
    for where in deaths.columns:
        fields = where.split(',')
        state = fields[1].strip()
        county = fields[0].strip()
        if len(state) > 0 and state in state2Two and state2Two[state] in fipsTable:
#             print(state2Two[state], county)
            stateCounties = fipsTable[state2Two[state]]
            cname = county.replace('Doña', 'Dona')
            if not cname in stateCounties :
                cname = county + '/city'
                if not cname in stateCounties :
                    cname = county + '/town'
                    if not cname in stateCounties :
                        print( '?', state, county, cname)
                        continue
            cdead[stateCounties[cname]] = deaths.iloc[-1][where]
        else :
            print('??', state)
    # spread NYC deaths across 5 boroughs per https://jamanetwork.com/journals/jama/fullarticle/2765524
    cdead['36047'] = 0.198 * cdead['36061'] # Kings
    cdead['36005'] = 0.259 * cdead['36061'] # Bronx
    cdead['36085'] = 0.175 * cdead['36061'] # Richmond
    cdead['36081'] = 0.231 * cdead['36061'] # Queens
    cdead['36061'] = 0.137 * cdead['36061'] # New York
    
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
    
def mapcolors(values, nlevels):
    minv = np.min(values)
    maxv = np.max(values)
    endpts = list(np.linspace(minv, maxv, nlevels,endpoint=False))
    cs = []

    for i in range(0, nlevels+1):
        t = cm.jet(int(255.0*i/(nlevels+1)))
        r = min(255, int(255.0 * t[0]))
        g = min(255, int(255.0 * t[1]))
        b = min(255, int(255.0 * t[2]))
        cs.append( '#%2.2x%2.2x%2.2x' % (r, g, b) )
    return cs, endpts

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
    
if __name__ == '__main__':
    home = os.path.expanduser('~')
#     landareas = loadLandAreas(home + '/GITHUB/COVIDtoTimeSeries/data/')
#     print(landareas)
#     exit(0)
#     once(home + '/GITHUB/COVIDtoTimeSeries/data/')
    countyPopulation, countyDeaths, fipsTable = main( home + '/GITHUB/COVIDtoTimeSeries/data/' )
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
    lfips = []
    lvalues = []
    target = us.states.CA
    for i in range(0,len(values)):
        v = values[i]
        stateFips = int(fips[i]) // 1000
        if stateFips == int(target.fips) : # v == 0: # v >=1 and v < 4.0:
            lfips.append(fips[i])
            lvalues.append(int(v))
    colorscale, endpts = mapcolors(values, 5-1) 
#     print(colorscale)
    colorscale = ['white', 'blue', 'yellow', 'orange', 'red']
    colorscale = ['white', 
                  colorTupleToString(cm.inferno(0)),
                  colorTupleToString(cm.inferno(85)),
                  colorTupleToString(cm.inferno(170)),
                  colorTupleToString(cm.inferno(255)),
                  ]
    colorscale = np.array(colorscale)
    order = np.unique(lvalues)
    colorscale = colorscale[order]
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
