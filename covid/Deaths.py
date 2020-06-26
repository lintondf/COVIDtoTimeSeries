'''
Created on Apr 3, 2020

@author: D. F. Linton, Blue Lightning Development, LLC
'''

import os
import pandas as pd

pathToRepository = 'C:/Users/NOOK/GITHUB/COVID-19'  # change to where you checked out https://github.com/CSSEGISandData/COVID-19.git

countries = ['Afghanistan', 'Albania', 'Algeria', 'Andorra', 'Angola', 'Antigua and Barbuda', 'Argentina', 'Armenia',
              'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', 'Bahamas, The', 'Bahrain', 'Bangladesh',
              'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina',
              'Botswana', 'Brazil', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cabo Verde', 'Cambodia',
              'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Republic', 'Chad', 'Channel Islands',
              'Chile', 'China', 'Colombia', 'Congo (Brazzaville)', 'Congo (Kinshasa)', 'Costa Rica', "Cote d'Ivoire",
               'Croatia', 'Cruise Ship', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Czechia', 'Denmark', 'Diamond Princess',
               'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea',
                'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'Gabon',
                 'Gambia', 'Gambia, The', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe',
                  'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong',
                  'Hong Kong SAR', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iran (Islamic Republic of)', 'Iraq', 'Ireland',
                   'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Korea, South',
                    'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania',
                    'Luxembourg', 'MS Zaandam', 'Macao SAR', 'Macau', 'Madagascar', 'Mainland China', 'Malaysia', 'Maldives', 'Mali',
                     'Malta', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia',
                      'Montenegro', 'Morocco', 'Mozambique', 'Namibia', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua',
                      'Niger', 'Nigeria', 'North Ireland', 'North Macedonia', 'Norway', 'Oman', 'Others', 'Pakistan', 'Palestine',
                       'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar',
                        'Republic of Ireland', 'Republic of Korea', 'Republic of Moldova', 'Republic of the Congo', 'Reunion',
                        'Romania', 'Russia', 'Russian Federation', 'Rwanda', 'Saint Barthelemy', 'Saint Kitts and Nevis',
                        'Saint Lucia', 'Saint Martin', 'Saint Vincent and the Grenadines', 'San Marino', 'Saudi Arabia',
                        'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Somalia',
                        'South Africa', 'South Korea', 'Spain', 'Sri Lanka', 'St. Martin', 'Sudan', 'Suriname', 'Sweden',
                        'Switzerland', 'Syria', 'Taipei and environs', 'Taiwan', 'Taiwan*', 'Tanzania', 'Thailand', 'The Bahamas',
                         'The Gambia', 'Timor-Leste', 'Togo', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'UK', 'Uganda', 'Ukraine',
                          'United Arab Emirates', 'United Kingdom', 'Uruguay', 'US', 'Uzbekistan', 'Vatican City', 'Venezuela',
                           'Viet Nam', 'Vietnam', 'West Bank and Gaza', 'Zambia', 'Zimbabwe', 'occupied Palestinian territory']
states = ["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado",
      "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois",
      "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland",
      "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana",
      "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York",
      "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico",
      "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
      "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
states2 = {  # yes these are redundant; but one is sorted by name and the other by 2 letter
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


def updateDeaths(pathToRepository, pull=True, counties=None, casesColumn='Confirmed', deathsColumn='Deaths'):
    if (pull) :
        os.system('git -C %s pull' % pathToRepository)
    f = pd.DataFrame(columns=states)
    g = pd.DataFrame(columns=countries)
    fc = pd.DataFrame(columns=states)
    gc = pd.DataFrame(columns=countries)
    if not counties is None:
        h = pd.DataFrame(columns=counties.keys())
        hc = pd.DataFrame(columns=counties.keys())
        
    
    base = '%s/csse_covid_19_data/csse_covid_19_daily_reports/' % pathToRepository
    for (__, __, filenames) in os.walk(base):
        for name in filenames:
            if (name.endswith('.csv')) :
                print(name, pd.to_datetime(name[0:-4]))
                daily = pd.read_csv(base + name, encoding='utf8').fillna(0)
                countryColumn = 'Country/Region'
                stateColumn = 'Province/State'
                countyColumn = 'Admin2'
                if (not countryColumn in daily.columns) :
                    countryColumn = 'Country_Region'
                    stateColumn = 'Province_State'
                    # Confirmed
                stateDeaths = dict()
                for s in f.columns :
                    stateDeaths.update({s: 0})
                countryDeaths = dict()
                for s in g.columns :
                    countryDeaths.update({s: 0})
                stateCases = dict()
                for s in fc.columns :
                    stateCases.update({s: 0})
                countryCases = dict()
                for s in gc.columns :
                    countryCases.update({s: 0})
                    
                if not counties is None:
                    countyDeaths = dict()
                    countyCases = dict()
                    for s in counties.keys():
                        countyDeaths.update({s:0})
                        countyCases.update({s:0})
                for index, row in daily.iterrows():
                    if (row[deathsColumn] > 0) :
                        if (row[countryColumn] == 'US'):
                                s = row[stateColumn].strip().replace('D.C.', 'DC').replace('D.C.', 'DC')
                                if (',' in s) :
                                    s = states2[s[-2:]]
                                if (s in stateDeaths) :
                                    stateDeaths[s] += row[deathsColumn]
                                    if not counties is None and countyColumn in row and isinstance(row[countyColumn], str):
                                        county = row[countyColumn] + ' County, ' + s
                                        if county in counties:
                                            countyDeaths[county] += row[deathsColumn]
                                        elif s == 'Louisiana':
                                            county = row[countyColumn] + ' Parish, ' + s
                                            if county in counties:
                                                countyDeaths[county] += row[deathsColumn]
                                            else :
                                                print('Skipping ', row[countyColumn], s)
                                        elif s == 'Alaska':
                                            county = row[countyColumn] + 'Municipality, ' + s
                                            if county in counties:
                                                countyDeaths[county] += row[deathsColumn]
                                            else :
                                                print('Skipping ', row[countyColumn], s)
                                        elif s == 'District of Columbia':
                                            countyDeaths['District of Columbia, District of Columbia'] += row[deathsColumn]                                            
                                        else:
                                            if 'City' in row[countyColumn] :
                                                county = row[countyColumn].replace('City', 'County') + ', ' + s
                                            else :
                                                county = row[countyColumn] + ' city, ' + s # VA
                                            if county in counties:
                                                countyDeaths[county] += row[deathsColumn]
                                            elif row[countyColumn] != 'Unassigned' :
                                                print('Skipping ', row[countyColumn], s)
                                else :
                                    print("Skipping: ", s)
                        c = row[countryColumn]
                        if (c in countryDeaths) :
                            countryDeaths[c] += row[deathsColumn]
                        else :
                            print("Skipping: ", c)
                    if (casesColumn in row and row[casesColumn] > 0) :
                        if (row[countryColumn] == 'US'):
                                s = row[stateColumn].strip().replace('D.C.', 'DC')
                                if not 'Diamond Princess' in s:
                                    if (not ', U.S.' in s and ',' in s) :
                                        if s[-2:] == 'C.':
                                            print(s)
                                        s = states2[s[-2:]]
                                    if (s in stateCases) :
                                        stateCases[s] += row[casesColumn]
                                    else :
                                        print("Skipping: ", s)
                        c = row[countryColumn]
                        if (c in countryCases) :
                            countryCases[c] += row[casesColumn]
                        else :
                            print("Skipping: ", c)
                        
#                 for n in countyDeaths :
#                     countyCases[n] = countyCases[n] / counties[n]
#                     countyDeaths[n] = countyDeaths[n] / counties[n]
                e = pd.DataFrame(stateDeaths, index=[pd.to_datetime(name[0:-4])])
                f = f.append(e, sort=False)
                e = pd.DataFrame(countryDeaths, index=[pd.to_datetime(name[0:-4])])
                g = g.append(e, sort=False)
                e = pd.DataFrame(stateCases, index=[pd.to_datetime(name[0:-4])])
                fc = fc.append(e, sort=False)
                e = pd.DataFrame(countryCases, index=[pd.to_datetime(name[0:-4])])
                gc = gc.append(e, sort=False)
                if not counties is None:
                    e = pd.DataFrame(countyDeaths, index=[pd.to_datetime(name[0:-4])])
                    h = h.append(e, sort=False)
                    e = pd.DataFrame(countyCases, index=[pd.to_datetime(name[0:-4])])
                    hc = hc.append(e, sort=False)
    if counties is None:         
        return (f, g, fc, gc)
    else:    
        return (f, g, fc, gc, h, hc)

    
if __name__ == '__main__':
    home = os.path.expanduser('~')
    countiesData = pd.read_csv(home + '/GITHUB/COVIDtoTimeSeries/data/' + 'US-Counties-Population.csv', encoding='utf8', index_col=0).fillna(0)
    counties = dict()
    for i in range(0,len(countiesData.index)) :
        name = countiesData.index[i]
        counties[name[1:]] = countiesData[['2019']].iloc[0].values[0] * 1e-6 # convert to millions
    f, g, fc, gc, h, hc = updateDeaths(pathToRepository, counties=counties)
# uncomment to sort columns by ascending deaths                
#     f.sort_values(e.index[0], axis=1,ascending=False,inplace=True)
#     g.sort_values(e.index[0], axis=1,ascending=False,inplace=True)
    h.sort_values(h.index[-1], axis=1,ascending=False,inplace=True)
    h.to_csv("./county-deaths.csv")
    hc.sort_values(hc.index[-1], axis=1,ascending=False,inplace=True)
    hc.to_csv("./county-cases.csv")
    f.to_csv("./state-deaths.csv")    
    g.to_csv("./country-deaths.csv")
    fc.to_csv("./state-cases.csv")    
    gc.to_csv("./country-cases.csv")
