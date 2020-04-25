'''
Created on Apr 20, 2020

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
from pandas.plotting import register_matplotlib_converters
import statsmodels.api as sm
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.colors as mcolors
from datetime import datetime
from jinja2 import Environment, FileSystemLoader, select_autoescape

from scipy.optimize.minpack import curve_fit
from scipy.integrate import trapz
from sortedcontainers import SortedSet
from Population import loadPopulation, loadStatePopulations
from Deaths import updateDeaths
from Analysis import states2

register_matplotlib_converters()

class IHME():
    def __init__(self, home : str):
        outPath = home + "/GITHUB/COVIDtoTimeSeries"
        self.ihmePath = home + "/GITHUB/COVIDtoTimeSeries/data/IHME"
        self.states = pd.read_csv(outPath + "/data/states.csv", parse_dates=True, index_col=0)
        self.countries = pd.read_csv(outPath + "/data/countries.csv", parse_dates=True, index_col=0)
        
    
    def plot(self, which : str, ax1):
#         fig1, ax1 = plt.subplots()
#         fig1.autofmt_xdate()
        if which == 'US':
            which = 'United States of America'
        first = pd.Timestamp('2020-04-01')
        last = pd.Timestamp('2020-05-31')
        stat = 'totdea' # 'deaths'
        lower = stat + '_lower'
        mean = stat + '_mean'
        upper = stat + '_upper'
        if stat == 'deaths' :
            ax1.set_title("IMHE's %s Daily Deaths Estimates" % which)
        else:
            ax1.set_title("IMHE's %s Total Deaths Estimates" % which)
            
        for root, dirs, files in os.walk(self.ihmePath):
            for filename in files:
                if (filename.endswith('.csv')) :
#                     print(root,filename)    
                    estimate = pd.read_csv(root + "/" + filename, parse_dates=True, index_col=2)
    #                 print(estimate[estimate['location_name'] == 'Florida'])
    #                 estimate = estimate[estimate['location_name'] == 'US'] = 'United States of America'
                    florida = estimate[estimate['location_name'] == which]
                    florida = florida[[lower, mean, upper]]
                    florida = florida[florida[lower] > 0]
                    florida = florida[first:last]
    #                 print( estimate['location_name'].unique())
                    color = next(ax1._get_lines.prop_cycler)['color']
                    rgba = (mcolors.to_rgba(color))
    #                 print(root, rgba)
                    i = root.find('2020_')
                    label = 'As of %s' % root[i+5:i+10]
                    ax1.plot( florida.index[:], florida[mean], label=label, color=rgba ) # semilogy
                    rgba = (0.5+0.5*rgba[0], 0.5+0.5*rgba[1], 0.5+0.5*rgba[2], 1.0)
                    ax1.fill_between( florida.index[:], (florida[lower]), (florida[upper]), color=rgba)
    #                 if first is None:
    #                     first = florida.index[0]
    #                 last = florida.index[-1]
    #                 print(florida)
    #                 return
    # deaths_mean    deaths_lower    deaths_upper
        if which == 'United States of America' :
            FL = self.countries['US']
        else:
            FL = self.states[[which]]
        FL = FL[FL > 0]
        dFL = FL.dropna().diff().dropna()
        dFL = dFL[first:last]
        if stat == 'totdea' :
            dFL = dFL.cumsum()
        ax1.plot( dFL.index[:], dFL, label='Actual', color='black') # semilogy
        ax1.legend(loc='best') # 'upper left')
        plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')
        
#         plt.draw()
#         fig1.savefig(outpath + "/"+which+".png")
#         plt.close()

        

# def main():
#     home = 'C:/Users/NOOK' #TODO from sys.argv
#     pathToRepository = home + '/GITHUB/COVID-19'
#     outPath = home + "/GITHUB/COVIDtoTimeSeries"
#     ihmePath = home + "/GITHUB/COVIDtoTimeSeries/data/IHME"
#     states = pd.read_csv(outPath + "/data/states.csv", parse_dates=True, index_col=0)
#     countries = pd.read_csv(outPath + "/data/countries.csv", parse_dates=True, index_col=0)
#     fig1, ax1 = plt.subplots()
#     fig1.autofmt_xdate()
# #     plt.yscale('log')
#     which = 'United States of America' # 'Florida' #  'New York' # 
#     first = pd.Timestamp('2020-04-01')
#     last = pd.Timestamp('2020-05-31')
#     stat = 'totdea' # 'deaths'
#     lower = stat + '_lower'
#     mean = stat + '_mean'
#     upper = stat + '_upper'
#     if stat == 'deaths' :
#         ax1.set_title("IMHE's %s Daily Deaths Estimates" % which)
#     else:
#         ax1.set_title("IMHE's %s Total Deaths Estimates" % which)
#         
#     for root, dirs, files in os.walk(ihmePath):
#         for filename in files:
#             if (filename.endswith('.csv')) :
#                 print(root,filename)    
#                 estimate = pd.read_csv(root + "/" + filename, parse_dates=True, index_col=2)
# #                 print(estimate[estimate['location_name'] == 'Florida'])
# #                 estimate = estimate[estimate['location_name'] == 'US'] = 'United States of America'
#                 florida = estimate[estimate['location_name'] == which]
#                 florida = florida[[lower, mean, upper]]
#                 florida = florida[florida[lower] > 0]
#                 florida = florida[first:last]
# #                 print( estimate['location_name'].unique())
#                 color = next(ax1._get_lines.prop_cycler)['color']
#                 rgba = (mcolors.to_rgba(color))
# #                 print(root, rgba)
#                 i = root.find('2020_')
#                 label = 'As of %s' % root[i+5:i+10]
#                 ax1.plot( florida.index[:], florida[mean], label=label, color=rgba )
#                 rgba = (0.5+0.5*rgba[0], 0.5+0.5*rgba[1], 0.5+0.5*rgba[2], 1.0)
#                 ax1.fill_between( florida.index[:], florida[lower], florida[upper], color=rgba)
# #                 if first is None:
# #                     first = florida.index[0]
# #                 last = florida.index[-1]
# #                 print(florida)
# #                 return
# # deaths_mean    deaths_lower    deaths_upper
#     if which == 'United States of America' :
#         FL = countries['US']
#     else:
#         FL = states[[which]]
#     FL = FL[FL > 0]
#     dFL = FL.dropna().diff().dropna()
#     dFL = dFL[first:last]
#     if stat == 'totdea' :
#         dFL = dFL.cumsum()
#     ax1.plot( dFL.index[:], dFL, label='Actual', color='black')
#     ax1.legend(loc='upper left')
#     plt.show()
#     
# if __name__ == '__main__':
#     main()