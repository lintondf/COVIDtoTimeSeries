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

import plotly.figure_factory as ff

def main(dataPath : str):
    path = dataPath + 'US-Counties-Population.xlsx'
    counties = pd.read_excel(path, 'CO-EST2019-ANNRES', skiprows=3, index_col=0, usecols=[0, 12])
    counties = counties[1:-6]
    print(counties)
    counties.to_csv( dataPath + 'US-Counties-Population.csv')
    
if __name__ == '__main__':
    home = os.path.expanduser('~')
#     main(home + '/GITHUB/COVIDtoTimeSeries/data/')
    df_sample = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/laucnty16.csv')
    df_sample['State FIPS Code'] = df_sample['State FIPS Code'].apply(lambda x: str(x).zfill(2))
    df_sample['County FIPS Code'] = df_sample['County FIPS Code'].apply(lambda x: str(x).zfill(3))
    df_sample['FIPS'] = df_sample['State FIPS Code'] + df_sample['County FIPS Code']
    
    colorscale = ["#f7fbff", "#ebf3fb", "#deebf7", "#d2e3f3", "#c6dbef", "#b3d2e9", "#9ecae1",
        "#85bcdb", "#6baed6", "#57a0ce", "#4292c6", "#3082be", "#2171b5", "#1361a9",
        "#08519c", "#0b4083", "#08306b"
    ]
    endpts = list(np.linspace(1, 12, len(colorscale) - 1))
    fips = df_sample['FIPS'].tolist()
    values = df_sample['Unemployment Rate (%)'].tolist()
    
    
    fig = ff.create_choropleth(
        fips=fips, values=values, scope=['usa'],
        binning_endpoints=endpts, colorscale=colorscale,
        show_state_data=False,
        show_hover=True,
        asp = 2.9,
        title_text = 'USA by Unemployment %',
        legend_title = '% unemployed'
    )
    fig.layout.template = None
    fig.show()
