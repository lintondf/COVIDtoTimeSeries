'''
Created on Apr 9, 2020

@author: D. F. Linton, Blue Lightning Development, LLC
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
from pandas.plotting import register_matplotlib_converters
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

from scipy.optimize.minpack import curve_fit
from scipy.integrate import trapz
from sortedcontainers import SortedSet
from Population import loadPopulation, loadStatePopulations
from Deaths import updateDeaths

register_matplotlib_converters()


nD = 3 # 3DRR

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands', 'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cruise Ship', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Czechia', 'Denmark', 'Diamond Princess', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon', 'Gambia', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong', 'Hong Kong SAR', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iran (Islamic Republic of)', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South', 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'MS Zaandam', 'Macao SAR', 'Macau', 'Madagascar', 'Mainland China', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'North Ireland', 'North Macedonia', 'Norway', 'Oman', 'Others', 'Pakistan', 'Palestine', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Republic of Ireland', 'Republic of Korea', 'Republic of Moldova', 'Republic of the Congo', 'Reunion', 'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Barthelemy', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Martin', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia', 'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St. Martin', 'Sudan', 'Suriname', 'Sweden', 'Switzerland', 'Syria', 'Taipei and environs', 'Taiwan', 'Taiwan*', 'Tanzania', 'Thailand', 'The Bahamas', 'The Gambia', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'UK', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'Uruguay', 'US', 'Uzbekistan', 'Vatican City', 'Venezuela', 'Viet Nam', 'Vietnam', 'West Bank and Gaza', 'Zambia', 'Zimbabwe', 'occupied Palestinian territory']
states2 = {
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


def scan(cases, population, urlDirectory=None):  
    if not urlDirectory is None:
        marker = 'analysis/'
        i = urlDirectory.find(marker) + len(marker)
        print("![%s](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/%s/%s.png" %
              (cases.columns[0], urlDirectory[i:], urllib.parse.quote(cases.columns[0]) ) )
    cases['Ln'] = np.log(cases[cases.columns[0]])
    lnCases = cases[['Ln']].dropna()
    if (len(lnCases) < 10) :
        return None, None, None, None
    reg = linear_model.LinearRegression()
    T = np.asarray(((lnCases.index-lnCases.index[0]).days))
    T = T.reshape(-1, 1)
    Y = np.asarray(lnCases['Ln']).reshape(-1, 1)
        
    lowess = sm.nonparametric.lowess
    trend = lowess(Y[:,0], T[:,0], frac=0.5, it=10)[:,1]
    Z = np.exp(Y)
    y3raw = (Z[nD:,0] / Z[:-nD,0])
    y3ddr = lowess(y3raw, T[nD:,0], frac=0.5, it=10)[:,1]
    np.savetxt('../' + cases.columns[0] + '.csv', trend, delimiter=',') 
    x3ddr = lnCases.index[-len(T[nD:,0]):] #  T[3:]
    if (len(T) < 10) :
        print(cases.columns[0], len(T), 'days of history')
        return None, None, None, None
    else:
        t = np.hstack([T[-3:],T[-3:]**2])
        reg.fit(t, y3ddr[-3:])
        intercept = reg.intercept_
        coef = reg.coef_
        y_pred = reg.predict(t)
         
        overall = ( (trend[-1] - trend[0]) / (T[-1] - T[0]));
        direction = 'D'
        if (y3ddr[-1] > y3ddr[-5]) :
            direction = 'A'
        if urlDirectory is None :
            print('%-15s %3d   ' % (cases.columns[0], len(T)), end=' ')  
        scaledTrend = np.exp(trend) / population
        if urlDirectory is None:
            print('  %6.0f  %10.2f' % (np.exp(trend[-1]), scaledTrend[-1]), end='  ')
            print(' %7.3f %7.3f %7.3f ' % (y3ddr[-3]**(1/nD), y3ddr[-2]**(1/nD), y3ddr[-1]**(1/nD)))
    return scaledTrend, x3ddr, y3ddr, y3raw

def plotOneState( state, pop, path ):
    scaled, x3ddr, y3ddr, y3raw = scan( state, pop, path ) # smoothed trend/population (M), x and y for smoothed 3-day death ratios
    if scaled is None:
        return
    values = np.asarray(x[[x.columns[0]]].values)
    fig, ax1 = plt.subplots()
    ax2 = ax1.twinx()
    fig.autofmt_xdate()
    ax1.set_title('%s - %d Deaths' % (state.columns[0], values[-1]))
    ax1.grid(True)
    ax2.set_ylim(1, 2)
    color = 'red'
    ax1.semilogy(state.index[:], (scaled), color=color, label='Deaths/1M (Left)') # 
    ax1.semilogy(state.index[:], (values/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
    ax2.plot( x3ddr, y3ddr**(1/nD), color='blue', label='DDGR (Right)')
    ax2.plot( x3ddr, y3raw**(1/nD), color='blue', linestyle='', markeredgecolor='none', marker='.' )
    ax1.legend(loc='upper left')
    ax2.legend(loc='center right')
    plt.draw()
    fig.savefig(path+"/"+state.columns[0]+".png")
    plt.close()
    
if __name__ == '__main__':
    population = loadStatePopulations();
    home = 'C:/Users/NOOK' #TODO from sys.argv
    pathToRepository = home + '/GITHUB/COVID-19'
    outPath = home + "/GITHUB/COVIDtoTimeSeries"
    print( os.path.getmtime( pathToRepository) )
    os.system('git -C %s pull' % pathToRepository)
    if (os.path.getmtime( outPath + "/data/states.csv") < os.path.getmtime( pathToRepository)) :
        f, g = updateDeaths(pathToRepository, pull=False)
        f.sort_values(f.index[-1], axis=1,ascending=False,inplace=True)
        g.sort_values(g.index[-1], axis=1,ascending=False,inplace=True)
        f.to_csv(outPath + "/data/states.csv")
        g.to_csv(outPath + "/data/countries.csv")
    else :
        f = pd.read_csv(outPath + "/data/states.csv", parse_dates=True, index_col=0)
        g = pd.read_csv(outPath + "/data/countries.csv", parse_dates=True, index_col=0)
    
    print('%-15s   N  %10s  %10s  %7s %7s %7s' % ('State', 'Deaths', 'Per 1M', 'DDGR[-3]', 'DDGR[-2]', 'DDGR[-1]'))
#     fig, (ax1, ax2) = plt.subplots(1,2)
#     plt.grid(True)
    fig1, ax1 = plt.subplots() # 10 states death rates
    fig2, ax2 = plt.subplots() # 10 states DDGRs
    fig1.autofmt_xdate()
    fig2.autofmt_xdate()

    ax1.set_title('Highest 10 States - Deaths/Million Population')
    ax1.grid(True)
    ax2.set_title('Highest 10 States - Lowess Smoothed DDGRs')
    ax2.grid(True)
    for i in range(0,10) :
        x = f[[f.columns[i]]]
        x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
        pop = population[x.columns[0]]
        scaled, x3ddr, y3ddr, __ = scan( x, pop, 'states' ) # smoothed trend/population (M), x and y for smoothed 3-day death ratios
        color = next(ax1._get_lines.prop_cycler)['color']
        ax1.semilogy(x.index[:], (scaled), label=f.columns[i], color=color) # 
        ax1.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
        ax2.plot( x3ddr, y3ddr**(1/nD), color=color, label=f.columns[i])
    print()

    # generate charts for all states    
    for name in f.columns.sort_values():
        x = f[[name]]
        x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
        if name in population:
            pop = population[x.columns[0]]
            plotOneState(x, pop, outPath + "/analysis/states")

    
    print('%-15s   N  %10s  %10s  %6s %6s %6s' % ('Country', 'Deaths', 'Per 1M', 'DDR[-3]', 'DDR[-2]', 'DDR[-1]'))
    population = loadPopulation();
    population['US'] = population['United States']
    
    x = g[['US']]
    x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
    pop = population[x.columns[0]]
    scaled, x3ddr, y3ddr, __ = scan( x, pop, 'countries' ) # smoothed trend/population (M)
    color = 'Black'
    ax1.semilogy(x.index[:], (scaled), label=x.columns[0], color=color) # 
    ax1.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
    ax2.plot( x3ddr, y3ddr**(1/nD), color=color, label=x.columns[0])
    
    ax1.legend(loc='upper left')
    ax2.legend(loc='upper left')
    ax2.set_ylim(1, 2)
    fig1.savefig(outPath+"/analysis/States10WorstDeathRates.png")
    fig2.savefig(outPath+"/analysis/States10WorstDDGR.png")
    plt.close()
    
    fig3, ax3 = plt.subplots() # 10 countries death rates
    fig4, ax4 = plt.subplots() # 10 countries DDGRs
    fig3.autofmt_xdate()
    fig4.autofmt_xdate()
    ax3.set_title('Highest 10 Countries - Deaths/Million Population')
    ax3.grid(True)
    ax4.set_title('Highest 10 Countries - Lowess Smoothed DDGRs')
    ax4.grid(True)
    
    for i in range(0,10) :
        x = g[[g.columns[i]]]
        x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
        pop = population[x.columns[0]]
        scaled, x3ddr, y3ddr, __ = scan( x, pop ) # smoothed trend/population (M)
        color = next(ax3._get_lines.prop_cycler)['color']
        ax3.semilogy(x.index[:], (scaled), label=g.columns[i], color=color) # 
        ax3.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
        ax4.plot( x3ddr, y3ddr**(1/nD), color=color, label=g.columns[i])
    ax3.legend(loc='upper left')
    ax4.legend(loc='upper left')
    ax4.set_ylim(1, 2)
    fig3.savefig(outPath+"/analysis/Countries10WorstDeathRates.png")
    fig4.savefig(outPath+"/analysis/Countries10WorstDDGR.png")
    plt.close()

    # generate charts for all countries
    for name in g.columns.sort_values():
        x = g[[name]]
        x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
        if name in population:
            pop = population[x.columns[0]]
            plotOneState(x, pop, outPath + "/analysis/countries")
