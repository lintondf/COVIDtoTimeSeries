'''
Created on Jun 29, 2020

@author: lintondf
'''
import os
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
from Population import loadPopulation, loadStatePopulations


def compareDeaths(path, countries, countriesPopulation):
    fig, ax1 = plt.subplots()          
    width = 0.35  # the width of the bars
    deathRates = [71.72,
        117.61,
        160.18,
        226.43,
        498.26,
        674.42,
        6553.40 ]
    labels = ['2015 Seasonal',
        '2016 Seasonal',
        '2014 Seasonal',
        '2017 Seasonal',
        '1968 H3N2',
        '1957 Asian Flu',
        '1918 Spanish Flu']
    ind = np.arange(len(deathRates))
    pop = countriesPopulation['United States']
    rates = countries[['US']]['2020-04-01':] / pop
    modY = 500
    n = np.ceil((rates.iloc[-1].array[0] + modY) / modY)
    maxY = modY * n
    ax1.set_ylim(0.0, maxY)
    ax1.bar(ind, deathRates, width, color='r', tick_label=ind)
    for i in ind:
        ax1.annotate('%.2f' % deathRates[int(i)], xy=(i - width, min(0.95 * maxY, deathRates[int(i)])))
    ax1.set_xticklabels(labels)   
    plt.setp(ax1.get_xticklabels(), rotation=30, ha='right')   
    ax2 = ax1.twiny()
    lasti = rates.index[-1]
    ax2.plot(rates, color='k', label='Sine')
    ax2.annotate('%.2f' % rates.iloc[-1], xy=(lasti, rates.iloc[-1])) 
    plt.setp(ax2.get_xticklabels(), rotation=-30, ha='right')
    ax1.set_ylabel('US Deaths per Million')
    fig.tight_layout() 
    plt.draw()
    fig.savefig(path)

    
if __name__ == '__main__':
    home = os.path.expanduser('~')
    outPath = home + "/GITHUB/COVIDtoTimeSeries"
    countries = pd.read_csv(outPath + "/data/countries.csv", parse_dates=True, index_col=0)
    countriesPopulation = loadPopulation();
    compareDeaths('', countries, countriesPopulation)
