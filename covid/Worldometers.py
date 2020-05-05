'''
Created on Mar 17, 2020

@author: NOOK
'''
import requests
import urllib
import lxml.etree as etree
import lxml.html as lh
import pandas as pd
from Population import loadPopulation

class Country :
    def __init__(self):
        self.name = '';
        self.population = 0;
        self.totalCases = 0;
        self.totalDeaths = 0;
        self.totalRecovered = 0;
        self.activeCases = 0;
        self.seriousCritical = 0;
        self.casesPerMillion = 0;
        
    def toString(self):
        return '%-15s %8.0f %8.0f %8.0f %8.0f %8.0f %8.3f' % (
            self.name, self.totalCases, self.totalDeaths, self.totalRecovered,
            self.activeCases, self.seriousCritical, self.casesPerMillion);
            
    def normalized(self, population):
        if (self.casesPerMillion == 0) :
            self.casesPerMillion = self.activeCases / population
        return (self.casesPerMillion,
                self.totalDeaths/self.totalCases * self.casesPerMillion,
                self.totalRecovered/self.totalCases * self.casesPerMillion,
                self.activeCases/self.totalCases * self.casesPerMillion,
                self.seriousCritical/self.totalCases * self.casesPerMillion)
        
    def parseCountryRow( self, trs ):
        i = 0
        for tr in trs :
#             print(i,tr.text)
            if (i == 0) :
                if (len(tr) == 1) :
                    if (tr[0].text is None):
                        self.name = 'Diamond Princess'
                    else :
                        self.name = tr[0].text.strip()
                else:
                    self.name = tr.text.strip()
            else :
                if (tr.text is None) :
                    text = '0'
                else :
                    text = tr.text.strip()
                    if (text.startswith('<')) : 
                        continue
                if (len(text) == 0) :
                    text = '0'
                if (i == 1) :
                    self.totalCases = float(text.replace(',',''));
                elif (i == 3) :
                    self.totalDeaths = float(text.replace(',',''));
                elif (i == 5) :
                    self.totalRecovered = float(text.replace(',',''));
                elif (i == 6) :
                    self.activeCases = float(text.replace(',',''));
                elif (i == 7) :
    #                 print('['+text+']')
                    self.seriousCritical = float(text.replace(',',''));
                elif (i == 8) :
                    self.casesPerMillion = float(text.replace(',',''));
            i += 1

def oneFile( month, day, population):
#     url = 'https://web.archive.org/' + urllib.parse.quote('web/20200302000357/https://www.worldometers.info/coronavirus/')
#     url = 'https://web.archive.org/download/20200302000357/https://www.worldometers.info/coronavirus/'
#     page = requests.get(url)
    url = '/Users/NOOK/Documents/0Worldometer/Worldometer-%2.2d%2.2d.html' % (month, day)
    with open(url, 'r', encoding='UTF-8') as file:
        data = file.read()    
        doc = lh.fromstring(data)
#     nextButton = doc.xpath('//img[@alt="Next capture"]')
#     print(nextButton)
#     
# def main():
#     print('%-30s %9s %9s %9s %9s %5s' % ('Country', 'Cases/1M', 'Deaths/1M', 'Crit./1M', 'Pop M', 'Deaths/Cases'))
#     url = 'https://www.worldometers.info/coronavirus/#countries'
#     #Create a handle, page, to handle the contents of the website
#     page = requests.get(url)
#     #Store the contents of the website under doc
#     doc = lh.fromstring(page.content)
#     #Parse data that are stored between <tr>..</tr> of HTML
    table = doc.xpath('//table[@id="main_table_countries_today"]')
    if (len(table) == 0) :
        table = doc.xpath('//table[@id="main_table_countries"]')  # pre ? id
        
    table = table[0]
    
    tbody = table[1]
    for tr in tbody :
#         print(etree.tostring(tr, pretty_print=True))
        C = Country()
        C.parseCountryRow(tr)
#         print(C.toString())
        if (C.name == 'USA') : #  in population) :
            n = C.normalized(population[C.name]);
            print('%2.2d/%2.2d %-30s %9.3f %9.3f %9.3f %9.3f' % (month, day, C.name, n[0], n[1], n[-1], population[C.name]), end='')
            if (n[0] > 0) :
                print(' %5.1f%%' % (100*n[1]/n[0]))
            else :
                print()
#         else :
#             print('%s' % C.name)

if __name__ == '__main__':
    population = loadPopulation();
    population['USA'] = population['United States']
    population['UK'] = population['United Kingdom']
    population['S. Korea'] = population['South Korea']
    for day in range(1,31+1) :
        oneFile( 3, day, population)
    for day in range(1,12+1) :
        oneFile( 4, day, population)
    
