'''
Created on Mar 18, 2020

@author: NOOK
'''
import requests
import lxml.etree as etree
import lxml.html as lh
import pandas as pd
import numpy as np
from scipy.optimize import _trustregion_ncg

def loadPopulation():
    population = dict()
    url = 'https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    table = doc.xpath('//table')
    table = table[0]
#     print(etree.tostring(table, pretty_print=True))
    tbody = table[0]
    row = 0
    for tr in tbody :
        if (row == 0) :
            row += 1
            continue
#         print(etree.tostring(tr, pretty_print=True))
        td = tr[1] # span, a
        name = (td[1].text)
        td = tr[2]
        value = (float(td.text.replace(",",'')))
        population.update({name : 1e-6*value})
        row += 1
        if (row > 100) :
            break;
    return population

def loadStatePopulations():
    states = dict();
    url = 'https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States_by_population'
    page = requests.get(url)
    doc = lh.fromstring(page.content)
    table = doc.xpath('//table')
    table = table[0]
#     print(etree.tostring(table, pretty_print=True))
    tbody = table[0]
    row = 0
    for tr in tbody :
        if (row < 2) :
            row += 1
            continue
#         print(row, etree.tostring(tr, pretty_print=True))
#         for td in tr[2]:
#             print(' ', etree.tostring(td, pretty_print=True))
        if (np.isscalar(tr[2])) :
            break
#         print(row, etree.tostring(tr[2], pretty_print=True))
        if (len(tr[2]) == 1) :
            name = tr[2][0].text
        else :
            name = tr[2][1].text
        value = (float(tr[3].text.replace(",",'')))
#         print('--', name, value)
        states.update({name : 1e-6*value})
        row += 1
    
    return states
        
if __name__ == '__main__':
    print(loadPopulation())