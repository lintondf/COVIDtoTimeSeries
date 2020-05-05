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
from astropy.wcs.docstrings import row


def main(dataPath : str):
    path = dataPath + 'US-Counties-Population.xlsx'
    counties = pd.read_excel(path, 'CO-EST2019-ANNRES', skiprows=3, index_col=0, usecols=[0, 12])
    counties = counties[1:-6]
    print(counties)
    counties.to_csv( dataPath + 'US-Counties-Population.csv')
    
if __name__ == '__main__':
    home = os.path.expanduser('~')
    main(home + '/GITHUB/COVIDtoTimeSeries/data/')