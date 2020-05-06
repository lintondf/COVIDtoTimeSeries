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
from astropy.wcs.docstrings import row

# from adjustText import adjust_text  

register_matplotlib_converters()

Y_UPPER = 1.5 # upper y limit for DDGR charts
nD = 3 # 3DRR
home = os.path.expanduser('~')
pathToRepository = home + '/GITHUB/COVID-19'
ihme = IHME(home)

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


class Analysis():
    def __init__(self):
        self.top10StatesTable = ''
        self.top10CountriesTable = ''
        self.statesLinks = np.array([],dtype=str)
        self.countriesLinks = np.array([],dtype=str)
        

    def sigmoid(self, x, L ,x0, k, b):
        y = L / (1 + np.exp(-k*(x-x0)))+b
        return (y)
    
    def analyze(self, cases, population, which=None, verbose=False, links = None):  
        link = ("[%s](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/%s/%s.png)" %
              (cases.columns[0], which, urllib.parse.quote(cases.columns[0]) ) )
        if not verbose :
            print(cases.columns[0])
        cases['Ln'] = np.log(cases[cases.columns[0]])
        lnCases = cases[['Ln']].dropna()
        if (len(lnCases) < 10) :
            return None, None, None, None, links
        reg = linear_model.LinearRegression()
        T = np.asarray(((lnCases.index-lnCases.index[0]).days))
        T = T.reshape(-1, 1)
        Y = np.asarray(lnCases['Ln']).reshape(-1, 1)
            
        lowess = sm.nonparametric.lowess
        trend = lowess(Y[:,0], T[:,0], frac=0.5, it=10)[:,1]

#         try:
#             ydata = np.exp(trend)
#             xdata = T[:,0] - T[0,0]
#             idx = ydata > population
#             ydata = ydata[idx]
#             xdata = xdata[idx]
#             p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess
#     
#             popt, pcov = curve_fit(self.sigmoid, xdata, ydata,p0, method='dogbox', maxfev=5000)
#             print(cases.columns[0], ydata[-1], popt)
#             print(np.sqrt(np.diag(pcov)))
#             f,a  = plt.subplots()
#             a.plot(xdata, ydata, 'r.')
#             xz = np.linspace(xdata[0], 2*xdata[-1], 25)
#             z = self.sigmoid( xz, popt[0], popt[1], popt[2], popt[3] )
#             a.plot(xz,z, 'b-')
#             a.set_title(cases.columns[0])
#             plt.show()
#         except:
#             print(cases.columns[0], "?")
        Z = np.exp(Y) # very roundabout way to get non-zero values
        y3raw = (Z[nD:,0] / Z[:-nD,0])
        y3ddr = lowess(y3raw, T[nD:,0], frac=0.5, it=10)[:,1]
    #     np.savetxt('../' + cases.columns[0] + '.csv', trend, delimiter=',') 
        x3ddr = lnCases.index[-len(T[nD:,0]):] #  T[3:]
        if (len(T) < 10) :
            print(cases.columns[0], len(T), 'days of history')
            return None, None, None, None, links
        else:
            t = T[-3:] - T[-1]
            t = np.hstack([t,t**2])
            reg.fit(t, y3ddr[-3:])
            intercept = reg.intercept_
            coef = reg.coef_
            y_pred = reg.predict(t)
             
            overall = ( (trend[-1] - trend[0]) / (T[-1] - T[0]));
            direction = 'D'
            if (y3ddr[-1] > y3ddr[-5]) :
                direction = 'A'
            scaledTrend = np.exp(trend) / population
            def rpt(y3 : float) -> str:
                ddgr = y3**(1/nD)
                if ddgr <= 1.0 :
                    ddgr = 1.0
                    days = ' --'
                elif (ddgr > 1.0) :
                    ndays = int(np.log(2)/np.log(ddgr))
                    if ndays > 99:
                        days = ' **'
                    else :                                        
                        days = '%3d' % ndays
                return '%7.3f/%s' % (ddgr, days)
            row = ''
            row += ('|%-15s| %3d   ' % (link, len(T)))  
            row += ('|  %6.0f|  %10.2f' % (np.exp(trend[-1]), scaledTrend[-1]))
            row += ('| %s| %s| %s| %s |' % (rpt(y3ddr[-7]), rpt(y3ddr[-3]), rpt(y3ddr[-2]), rpt(y3ddr[-1])))
            row += ('\n')
            if verbose :
                if (which == 'states') :
                    self.top10StatesTable += row
                else:
                    self.top10CountriesTable += row
            else:
                if not links is None:
                    links = np.append( links, np.array([row], dtype=str) )
                    
        return scaledTrend, x3ddr, y3ddr, y3raw, links

    def plotOneState( self, path, state, pop, which, links, compare=False ):
        scaled, x3ddr, y3ddr, y3raw, links = self.analyze( state, pop, which=which, verbose=False, links=links ) # smoothed trend/population (M), x and y for smoothed 3-day death ratios
        if scaled is None:
            return links
        values = np.asarray(state[[state.columns[0]]].values)
        if (compare) :
#             fig, (ax1, axi) = plt.subplots(2, figsize=(8,10.5), sharex=False)
            fig = plt.figure(constrained_layout=False, figsize=(8,10.5))
            spec1 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig)
            ax1 = fig.add_subplot(spec1[0, 0]) #, sharex=False)
            spec2 = gridspec.GridSpec(ncols=1, nrows=2, figure=fig, hspace=0.30)
            axi = fig.add_subplot(spec2[1, 0]) #, sharex=False)   
            ax1.get_shared_x_axes().remove(axi)         
            axi.get_shared_x_axes().remove(ax1)         
        else:
            fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
#         fig.autofmt_xdate()
        plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')
        ax1.set_title('%s - %d Deaths' % (state.columns[0], values[-1]))
        ax1.grid(True)
        ax2.set_ylim(1, Y_UPPER)
        color = 'red'
        ax1.semilogy(state.index[:], (scaled), color=color, label='Deaths/1M (Left)') # 
        ax1.semilogy(state.index[:], (values/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
        ax1.annotate('%5.1f' % (values[-1]/pop),
                xy=(state.index[-1], values[-1]/pop), xycoords='data',
                xytext=(-10, -30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))
        ax2.plot( x3ddr, y3ddr**(1/nD), color='blue', label='DDGR (Right)')
        ax2.plot( x3ddr, y3raw**(1/nD), color='blue', linestyle='', markeredgecolor='none', marker='.' )
        ax2.annotate('%5.2f' % (y3raw[-1]**(1/nD)),
                xy=(x3ddr[-1], y3raw[-1]**(1/nD)), xycoords='data',
                xytext=(-10, 30), textcoords='offset points',
                arrowprops=dict(arrowstyle="->"))
        ax1.legend(loc='upper left')
        ax2.legend(loc='center right')
        if compare:
            ihme.plot( state.columns[0], axi)
            plt.setp(axi.get_xticklabels(), rotation=30, ha='right')
        plt.draw()
        fig.savefig(path+"/"+state.columns[0]+".png")
        plt.close()
        return links
    
    def plotCasesVsDeaths(self, deaths, cases, population, xlim, ylim, which=None):
        fig, ax1 = plt.subplots()
        texts = []
        if which is None:
            states = deaths.columns;
        else :
            states = which
        for s in states :
            if not s in cases.columns:
                continue;
            if not s in population:
                continue;
            d = deaths[s] / population[s]
            d = d[d > 50]
            if len(d) == 0:
                continue;
            c = cases[s] / population[s]
            c = c[c > 1000]
            if len(c) == 0:
                continue;
            first = c.index[0]
            if d.index[0] > first:
                first = d.index[0]
            last = c.index[-1]
            if d.index[-1] < last:
                last = d.index[-1]
            color = next(ax1._get_lines.prop_cycler)['color']
            if which is None:
                ax1.loglog( np.asarray(c[first:last].values), np.asarray(d[first:last].values), '-', color='gray')
            ax1.loglog(c[last], d[last], '.', color=color)
            text = ax1.annotate(s, color=color,
                    xy=(c[last], d[last]), xycoords='data',
                    xytext=(10, 30), textcoords='offset points',
                    arrowprops=dict(arrowstyle="->", color=color))
            if len(texts) == 0 :
                texts = [text]
            else :
                texts.append(text)
        fig.canvas.draw()            
#         print(texts, texts.get_window_extent() )
# very slow; pushes label out of frame...
#         adjust_text(texts, arrowprops=dict(arrowstyle='->', color='gray'))
        ax1.grid(True)
        ax1.set_xlabel('Cases per Million')
        ax1.set_ylabel('Deaths per Million')
#         ax1.set_xlim(50, xlim)
#         ax1.set_ylim(1000, ylim)
        plt.show();
        
    def main(self, reload, pathToRepository, outPath):
        if (reload) :
            f, g, fc, gc = updateDeaths(pathToRepository, pull=False)
            f.sort_values(f.index[-1], axis=1,ascending=False,inplace=True)
            g.sort_values(g.index[-1], axis=1,ascending=False,inplace=True)
            f.to_csv(outPath + "/data/states.csv")
            g.to_csv(outPath + "/data/countries.csv")
            fc.to_csv(outPath + "/data/states-cases.csv")
            gc.to_csv(outPath + "/data/countries-cases.csv")
        else :
            f = pd.read_csv(outPath + "/data/states.csv", parse_dates=True, index_col=0)
            g = pd.read_csv(outPath + "/data/countries.csv", parse_dates=True, index_col=0)
            fc = pd.read_csv(outPath + "/data/states-cases.csv", parse_dates=True, index_col=0)
            gc = pd.read_csv(outPath + "/data/countries-cases.csv", parse_dates=True, index_col=0)
            
        print(f.index[-1])
        
        statesPopulation = loadStatePopulations();
        countriesPopulation = loadPopulation();
        countriesPopulation['US'] = countriesPopulation['United States']
        
#         self.plotCasesVsDeaths( g, gc, countriesPopulation, 5000, 500 )
#         self.plotCasesVsDeaths( f, fc, statesPopulation, 5000, 500 )

        population = statesPopulation;
    #     print('%-15s   N  %10s  %10s  %7s %7s %7s %7s' % ('State', 'Deaths', 'Per 1M', 'DDGR[-7]', 'DDGR[-3]', 'DDGR[-2]', 'DDGR[-1]'))
        header1 = ("|State|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|\n")
        header2 = ("|:--|--:|--:|--:|--:|--:|--:|--:|\n")
        self.statesLinks = np.append( self.statesLinks, np.array([header1, header2], dtype=str) )
        self.top10StatesTable = header1
        self.top10StatesTable += header2
    #     fig, (ax1, ax2) = plt.subplots(1,2)
    #     plt.grid(True)
        fig1, ax1 = plt.subplots() # 10 states death rates
        fig2, ax2 = plt.subplots() # 10 states DDGRs
#         fig1.autofmt_xdate()
#         fig2.autofmt_xdate()
    
        ax1.set_title('Highest 10 States - Deaths/Million Population')
        ax1.grid(True)
        ax2.set_title('Highest 10 States - Lowess Smoothed DDGRs')
        ax2.grid(True)
        for i in range(0,10) :
            x = f[[f.columns[i]]]
            x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
            pop = population[x.columns[0]]
            scaled, x3ddr, y3ddr, __, __ = self.analyze( x, pop, 'states', verbose=True ) # smoothed trend/population (M), x and y for smoothed 3-day death ratios
            color = next(ax1._get_lines.prop_cycler)['color']
    #         label = '%s : %6.1f' % (f.columns[i], scaled[-1])
            label = f.columns[i]
            ax1.semilogy(x.index[:], (scaled), label=label, color=color) # 
            ax1.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
    #         label = '%s : %6.1f' % (f.columns[i], y3ddr[-1]**(1/nD))
            ax2.plot( x3ddr, y3ddr**(1/nD), color=color, label=label)
        print()
    
        # generate charts for all states    
        for name in f.columns.sort_values():
            x = f[[name]]
            x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
            if name in population:
                pop = population[x.columns[0]]
                compare = True
                if (name == 'Puerto Rico') or (name == 'Wyoming') :
                    compare = False
                self.statesLinks = self.plotOneState(outPath + "/analysis/states", x, pop, 
                                                     which='states', links=self.statesLinks, compare=compare)
    
        
    #     print('%-15s   N  %10s  %10s  %6s %6s %6s' % ('Country', 'Deaths', 'Per 1M', 'DDR[-3]', 'DDR[-2]', 'DDR[-1]'))
        header1 = ("|Country|Days|Deaths|Deaths/1M|DDGR[6:7]|DDGR[2:3]|DDGR[1:2]|DDGR[0:1]|\n")
        header2 = ("|:--|--:|--:|--:|--:|--:|--:|--:|\n")
        self.countriesLinks = np.append( self.countriesLinks, np.array([header1, header2], dtype=str) )        
        self.top10CountriesTable = header1
        self.top10CountriesTable += header2
        population = countriesPopulation;
        population['US'] = population['United States']
        
        x = g[['US']]
        x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
        pop = population[x.columns[0]]
        scaled, x3ddr, y3ddr, __, __ = self.analyze( x, pop, 'countries' ) # smoothed trend/population (M)
        color = 'Black'
        ax1.semilogy(x.index[:], (scaled), label=x.columns[0], color=color) # 
        ax1.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
        ax2.plot( x3ddr, y3ddr**(1/nD), color=color, label=x.columns[0])
        
        ax1.legend(loc='upper left')
        ax2.legend(loc='upper left')
        ax2.set_ylim(1, Y_UPPER)
        fig1.savefig(outPath+"/analysis/States10WorstDeathRates.png")
        fig2.savefig(outPath+"/analysis/States10WorstDDGR.png")
        plt.close()
        
        fig3, ax3 = plt.subplots() # 10 countries death rates
        fig4, ax4 = plt.subplots() # 10 countries DDGRs
        ax3.set_xticklabels(ax3.get_xticklabels(), rotation=90) # fig3.autofmt_xdate()
        ax4.set_xticklabels(ax4.get_xticklabels(), rotation=90) # fig4.autofmt_xdate()
        ax3.set_title('Highest 10 Countries - Deaths/Million Population')
        ax3.grid(True)
        ax4.set_title('Highest 10 Countries - Lowess Smoothed DDGRs')
        ax4.grid(True)
        
        for i in range(0,10) :
            x = g[[g.columns[i]]]
            x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
            pop = population[x.columns[0]]
            scaled, x3ddr, y3ddr, __, __ = self.analyze( x, pop, 'countries', verbose=True ) # smoothed trend/population (M)
            color = next(ax3._get_lines.prop_cycler)['color']
            ax3.semilogy(x.index[:], (scaled), label=g.columns[i], color=color) # 
            ax3.semilogy(x.index[:], (np.asarray(x[[x.columns[0]]].values)/pop), linestyle='', markeredgecolor='none', marker='.', color=color)
            ax4.plot( x3ddr, y3ddr**(1/nD), color=color, label=g.columns[i])
        ax3.legend(loc='upper left')
        ax4.legend(loc='upper left')
        ax4.set_ylim(1, Y_UPPER)
        fig3.savefig(outPath+"/analysis/Countries10WorstDeathRates.png")
        fig4.savefig(outPath+"/analysis/Countries10WorstDDGR.png")
        plt.close()
    
        # generate charts for all countries
        for name in g.columns.sort_values():
            x = g[[name]]
            x = x[(x.T != 0).any()].apply(pd.to_numeric, errors='coerce')
            if name in population:
                pop = population[x.columns[0]]
                self.countriesLinks = self.plotOneState(outPath + "/analysis/countries", x, pop, 
                                        which='countries', links=self.countriesLinks, compare=name == 'US')
    #     os.system('git -C %s commit -a -m "daily update"' % outPath)
    #     os.system('git -C %s push' % outPath)


if __name__ == '__main__':
    outPath = home + "/GITHUB/COVIDtoTimeSeries"
    env = Environment(
        loader=FileSystemLoader(outPath + '/covid/templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template("ANALYSIS.mdt")
    analysis = Analysis()    

    result = os.popen('git -C %s pull' % pathToRepository).read()

    reload = not result.startswith('Already up to date.')
    if reload:
        os.system('git -C %s pull' % outPath)

    analysis.main(reload, pathToRepository, outPath)
    
    statesContent = ''
    for state in analysis.statesLinks:
        statesContent += state
    countriesContent = ''
    for state in analysis.countriesLinks:
        countriesContent += state
    fields = dict();
    fields.update({'date': datetime.date(datetime.now())})
    fields.update({'top10StatesTable': analysis.top10StatesTable})
    fields.update({'top10CountriesTable': analysis.top10CountriesTable})
    fields.update({'statesLinks': statesContent})
    fields.update({'countriesLinks': countriesContent})    
    f = open(outPath + '/analysis/ANALYSIS.md', 'w') 
    print(template.render(fields), file=f)
    f.close()
    if reload :
        os.system('git -C %s commit -a -m "daily update"' % outPath)
        os.system('git -C %s push' % outPath)
