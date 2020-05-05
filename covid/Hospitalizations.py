'''
Created on Apr 3, 2020

@author: D. F. Linton, Blue Lightning Development, LLC
'''

import os
import pandas as pd

pathToRepository = 'C:/Users/NOOK/GITHUB/COVID-19'  # change to where you checked out https://github.com/CSSEGISandData/COVID-19.git

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


def updateHospitalizations(pathToRepository, pull=True):
    if (pull) :
        os.system('git -C %s pull' % pathToRepository)
    f = pd.DataFrame(columns=states)
    
    base = '%s/csse_covid_19_data/csse_covid_19_daily_reports_us/' % pathToRepository
    for (__, __, filenames) in os.walk(base):
        for name in filenames:
            if (name.endswith('.csv')) :
                print(name, pd.to_datetime(name[0:-4]))
                daily = pd.read_csv(base + name, encoding='utf8').fillna(0)
                countryColumn = 'Country/Region'
                stateColumn = 'Province/State'
                if (not countryColumn in daily.columns) :
                    countryColumn = 'Country_Region'
                    stateColumn = 'Province_State'
                stateHospitalizations = dict()
                for s in f.columns :
                    stateHospitalizations.update({s: 0})
                for index, row in daily.iterrows():
                    if (row['People_Hospitalized'] > 0) :
                        if (row[countryColumn] == 'US'):
                                s = row[stateColumn]
                                if (',' in s) :
                                    s = states2[s[-2:]]
                                if (s in stateHospitalizations) :
                                    stateHospitalizations[s] += row['People_Hospitalized']
                                else :
                                    print("Skipping: ", s)
                e = pd.DataFrame(stateHospitalizations, index=[pd.to_datetime(name[0:-4])])
                f = f.append(e, sort=False)
    return (f)    

    
if __name__ == '__main__':
    f = updateHospitalizations(pathToRepository)
# uncomment to sort columns by ascending hospitalizations                
    f.sort_values(f.index[0], axis=1,ascending=False,inplace=True)
    f.to_csv("./state-hospitalizations.csv")    
