# Analysis of US By County #

Updated: at 2020-08-04

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 123,460 deaths (427.698 deaths/million) and 4,061,692 confirmed cases (14070.750 confirmed cases/million).  This group accounts for 80.68% of all US deaths and for 87.63% of all US cases.

24.08% of this group's deaths (19.42% of the total US deaths) occured in 12 counties in 9 states with a combined population of 32,573,893 (9.92% of the total US population):



The next 25.79% of this group's deaths (20.80% of the total US deaths) occured in 33 counties in 14 states with a combined population of 40,700,179 (12.40% of the total US population):



The next 25.03% of this group's deaths (20.20% of the total US deaths) occured in 84 counties in 29 states with a combined population of 66,770,111 (20.34% of the total US population)

The remaining 25.11% of this group's deaths (20.25% of the total US deaths) occured in 861 counties in 50 states with a combined population of 148,617,876 (45.28% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,140 deaths (230.940 deaths/million) and 406,341 confirmed cases (10266.979 confirmed cases/million).  This group accounts for 5.97% of all US deaths and for 8.77% of all US cases.

24.84% of this group's deaths (1.48% of the total US deaths) occured in 54 counties in 16 states with a combined population of 1,750,537 (0.53% of the total US population):



The next 25.03% of this group's deaths (1.50% of the total US deaths) occured in 106 counties in 26 states with a combined population of 3,229,880 (0.98% of the total US population):



The next 25.09% of this group's deaths (1.50% of the total US deaths) occured in 219 counties in 32 states with a combined population of 5,393,924 (1.64% of the total US population)

The remaining 25.04% of this group's deaths (1.50% of the total US deaths) occured in 1,773 counties in 47 states with a combined population of 29,203,123 (8.90% of the total US population) 

## All US Counties ##

||||||
|:-:|:-:|:-:|:-:|:-:|
|<a href="#alabama">Alabama</a>|<a href="#alaska">Alaska</a>|<a href="#arizona">Arizona</a>|<a href="#arkansas">Arkansas</a>|<a href="#california">California</a>|
|<a href="#colorado">Colorado</a>|<a href="#connecticut">Connecticut</a>|<a href="#delaware">Delaware</a>|<a href="#florida">Florida</a>|<a href="#georgia">Georgia</a>|
|<a href="#hawaii">Hawaii</a>|<a href="#idaho">Idaho</a>|<a href="#illinois">Illinois</a>|<a href="#indiana">Indiana</a>|<a href="#iowa">Iowa</a>|
|<a href="#kansas">Kansas</a>|<a href="#kentucky">Kentucky</a>|<a href="#louisiana">Louisiana</a>|<a href="#maine">Maine</a>|<a href="#maryland">Maryland</a>|
|<a href="#massachusetts">Massachusetts</a>|<a href="#michigan">Michigan</a>|<a href="#minnesota">Minnesota</a>|<a href="#mississippi">Mississippi</a>|<a href="#missouri">Missouri</a>|
|<a href="#montana">Montana</a>|<a href="#nebraska">Nebraska</a>|<a href="#nevada">Nevada</a>|<a href="#new hampshire">New Hampshire</a>|<a href="#new jersey">New Jersey</a>|
|<a href="#new mexico">New Mexico</a>|<a href="#new york">New York</a>|<a href="#north carolina">North Carolina</a>|<a href="#north dakota">North Dakota</a>|<a href="#ohio">Ohio</a>|
|<a href="#oklahoma">Oklahoma</a>|<a href="#oregon">Oregon</a>|<a href="#pennsylvania">Pennsylvania</a>|<a href="#rhode island">Rhode Island</a>|<a href="#south carolina">South Carolina</a>|
|<a href="#south dakota">South Dakota</a>|<a href="#tennessee">Tennessee</a>|<a href="#texas">Texas</a>|<a href="#utah">Utah</a>|<a href="#vermont">Vermont</a>|
|<a href="#virginia">Virginia</a>|<a href="#washington">Washington</a>|<a href="#west virginia">West Virginia</a>|<a href="#wisconsin">Wisconsin</a>|<a href="#wyoming">Wyoming</a>|


States and counties sorted by highest total number of deaths.  Counties with ten or fewer total deaths are not plotted nor are daily per capita rates compute for these counties.

The charts below are somewhat unusual.  The daily case and death rates per capita vary widely between US counties:  zero values occur frequently as do very large values.  We use log-log scales for these charts and add one (1) to the case and death rates before plotting.  Thus if a point is plotted at 1.0 the true value is zero, this difference is less and less visibile as rate values increase.  Adding 1.0 permits the use of log axis scales that best present these varying values.


### New Jersey ###

![New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Jersey.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NJ|21 counties|15,846| 1784.019| N/A|181,942| 20483.912| N/A|8,882,190|
| |Essex County| 2,104| 2633.374|  1.065|19,558| 24478.864| 31.720| 798,975|
| |Bergen County| 2,041| 2189.440|  0.444|20,552| 22046.724| 31.233| 932,202|
| |Hudson County| 1,503| 2235.307|  1.487|19,528| 29042.625| 23.852| 672,391|
| |Middlesex County| 1,403| 1700.478|  0.000|17,735| 21495.354| 25.156| 825,062|
| |Union County| 1,348| 2422.974|  0.764|16,590| 29819.841| 26.962| 556,341|
| |Passaic County| 1,242| 2474.961|  0.000|17,507| 34886.594| 71.738| 501,826|
| |Ocean County| 1,016| 1673.293|  0.000|10,469| 17241.834| 26.568| 607,186|
| |Monmouth County|   858| 1386.566|  0.000|10,137| 16381.839| 58.178| 618,795|
| |Morris County|   830| 1687.524|  2.033| 7,167| 14571.664| 22.365| 491,845|
| |Mercer County|   619| 1684.675|  4.986| 8,051| 21911.657| 30.956| 367,430|
| |Camden County|   575| 1135.307|  1.678| 8,375| 16535.991| 44.677| 506,471|
| |Somerset County|   555| 1687.269|  0.477| 5,195| 15793.442| 15.810| 328,934|
| |Burlington County|   470| 1055.352|  0.350| 5,846| 13126.784| 43.045| 445,349|
| |Atlantic County|   252| 955.740|  1.260| 3,408| 12925.247| 53.116| 263,670|
| |Gloucester County|   209| 716.647|  1.210| 3,106| 10650.263| 48.997| 291,636|
| |Sussex County|   195| 1388.019|  0.000| 1,307|  9303.286| 24.913| 140,488|
| |Warren County|   171| 1624.441|  0.000| 1,330| 12634.539|  4.364| 105,267|
| |Cumberland County|   157| 1049.978|  0.000| 3,253| 21755.268| 84.084| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,138|  9150.043| 48.243| 124,371|
| |Cape May County|    87| 945.251|  0.000|   813|  8833.212| 23.698|  92,039|
| |Salem County|    85| 1362.507| 13.336|   877| 14057.866| 64.118|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,290| 631.768| N/A|249,731| 12837.280| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,380| 31969.366| 41.559|1,356,924|
| |Suffolk County| 1,997| 1352.430|  0.000|43,395| 29388.440| 35.252|1,476,601|
| |Westchester County| 1,446| 1494.564|  0.442|36,014| 37223.542| 23.946| 967,506|
| |Queens County|   983| 436.079|  1.257| 7,804|  3462.504| 15.422|2,253,858|
| |Kings County|   929| 362.851|  1.046| 1,339|   523.199|  2.330|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,885| 42619.610|  7.764| 325,789|
| |Erie County|   669| 728.201|  0.000| 8,626|  9389.334| 45.650| 918,702|
| |Bronx County|   648| 456.897|  1.317|26,577| 18739.624| 83.467|1,418,207|
| |Orange County|   489| 1270.328|  0.000|11,096| 28825.271| 11.235| 384,940|
| |New York County|   414| 253.977|  0.732|15,328|  9411.040| 41.917|1,628,706|
| |Monroe County|   277| 373.431|  0.000| 4,790|  6457.527| 34.129| 741,770|
| |Onondaga County|   200| 434.284|  6.125| 3,490|  7578.258| 16.448| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,543| 15440.932| 63.434| 294,218|
| |Richmond County|   148| 310.395|  0.895| 7,804| 16390.016| 73.001| 476,143|
| |Albany County|   126| 412.431|  0.000| 2,531|  8284.616| 39.279| 305,506|
| |Oneida County|   112| 489.787|  0.000| 2,090|  9139.768| 24.295| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,449|  6923.705| 13.052| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,031| 11437.550| 18.497| 177,573|
| |Broome County|    64| 335.979|  0.000| 1,064|  5585.654| 45.361| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,433| 14574.858| 40.570|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   295|  7310.666|  7.775|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,483| 19660.091|  6.239|  75,432|
| |Steuben County|    42| 440.349|  0.000|   292|  3061.471|  8.339|  95,379|
| |Columbia County|    37| 622.257|  0.000|   523|  8795.681| 50.453|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,037|  6677.442| 23.266| 155,299|
| |Ontario County|    34| 309.719|  0.000|   351|  3197.391|  0.000| 109,777|
| |Warren County|    33| 516.077|  0.000|   300|  4691.605|  0.000|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   740|  4662.475| 25.763| 158,714|
| |Tioga County|    25| 518.640|  0.000|   190|  3941.663| 20.746|  48,203|
| |Fulton County|    24| 449.581|  0.000|   285|  5338.778| 44.156|  53,383|
| |Greene County|    18| 381.453|  0.000|   289|  6124.438|  0.000|  47,188|
| |Madison County|    17| 239.636|  0.000|   401|  5652.585| 14.096|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   733|  3188.856| 20.462| 229,863|
| |Washington County|    14| 228.743|  0.000|   255|  4166.394|  2.563|  61,204|
| |Chautauqua County|     9| 70.920| N/A|   234|  1843.928| N/A| 126,903|
| |Livingston County|     8| 127.158| N/A|   167|  2654.417| N/A|  62,914|
| |Yates County|     7| 280.978| N/A|    55|  2207.683| N/A|  24,913|
| |Chenango County|     6| 127.100| N/A|   211|  4469.676| N/A|  47,207|
| |Cattaraugus County|     6| 78.826| N/A|   162|  2128.302| N/A|  76,117|
| |Genesee County|     5| 87.291| N/A|   273|  4766.061| N/A|  57,280|
| |Otsego County|     5| 84.044| N/A|   114|  1916.192| N/A|  59,493|
| |Wyoming County|     5| 125.442| N/A|   113|  2834.993| N/A|  39,859|
| |Herkimer County|     4| 65.233| N/A|   246|  4011.807| N/A|  61,319|
| |St. Lawrence County|     4| 37.126| N/A|   262|  2431.780| N/A| 107,740|
| |Montgomery County|     4| 81.266| N/A|   160|  3250.645| N/A|  49,221|
| |Delaware County|     4| 90.631| N/A|   104|  2356.406| N/A|  44,135|
| |Clinton County|     4| 49.699| N/A|   127|  1577.934| N/A|  80,485|
| |Wayne County|     3| 33.364| N/A|   247|  2746.947| N/A|  89,918|
| |Oswego County|     3| 25.614| N/A|   248|  2117.414| N/A| 117,124|
| |Seneca County|     3| 88.194| N/A|    86|  2528.222| N/A|  34,016|
| |Chemung County|     3| 35.947| N/A|   163|  1953.125| N/A|  83,456|
| |Cayuga County|     2| 26.118| N/A|   148|  1932.720| N/A|  76,576|
| |Allegany County|     1| 21.696| N/A|    75|  1627.216| N/A|  46,091|
| |Franklin County|     0|  0.000| N/A|    50|   999.560| N/A|  50,022|
| |Jefferson County|     0|  0.000| N/A|   134|  1220.023| N/A| 109,834|
| |Hamilton County|     0|  0.000| N/A|     7|  1585.145| N/A|   4,416|
| |Essex County|     0|  0.000| N/A|    55|  1491.121| N/A|  36,885|
| |Cortland County|     0|  0.000| N/A|    92|  1933.545| N/A|  47,581|
| |Lewis County|     0|  0.000| N/A|    35|  1331.001| N/A|  26,296|
| |Schoharie County|     0|  0.000| N/A|    68|  2193.619| N/A|  30,999|
| |Tompkins County|     0|  0.000| N/A|   230|  2250.930| N/A| 102,180|
| |Schuyler County|     0|  0.000| N/A|    22|  1235.469| N/A|  17,807|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties| 9,441| 238.939| N/A|516,851| 13080.788| N/A|39,512,223|
| |Los Angeles County| 4,702| 468.368|  2.096|193,877| 19312.176| 169.338|10,039,107|
| |Riverside County|   695| 281.314|  0.000|37,011| 14980.899|  0.000|2,470,546|
| |Orange County|   651| 204.995|  2.174|37,813| 11907.011| 160.640|3,175,692|
| |San Diego County|   565| 169.246|  0.511|29,883|  8951.482| 125.063|3,338,330|
| |San Bernardino County|   418| 191.736|  0.241|33,432| 15335.182| 171.106|2,180,085|
| |Imperial County|   222| 1225.064| 20.963| 9,448| 52136.964| 127.862| 181,215|
| |Santa Clara County|   191| 99.074|  0.000|10,794|  5598.978| 122.675|1,927,852|
| |Alameda County|   189| 113.084|  0.657|11,524|  6895.112| 46.993|1,671,329|
| |Tulare County|   189| 405.410|  9.815| 9,745| 20903.270| 312.101| 466,195|
| |San Joaquin County|   180| 236.175|  7.389|11,885| 15594.084| 263.728| 762,148|
| |Sacramento County|   145| 93.424|  0.000|10,122|  6521.663| 82.720|1,552,058|
| |Kern County|   144| 159.964|  0.000|20,651| 22940.407| 427.126| 900,202|
| |Fresno County|   138| 138.124|  0.000|15,083| 15096.572| 262.281| 999,101|
| |Contra Costa County|   127| 110.097|  2.445| 8,033|  6963.866| 101.915|1,153,526|
| |San Mateo County|   119| 155.236|  0.000| 5,683|  7413.514| 97.838| 766,573|
| |Stanislaus County|   112| 203.392|  5.133| 9,221| 16745.360| 253.096| 550,660|
| |Ventura County|    76| 89.834|  0.000| 7,344|  8680.789|  0.000| 846,006|
| |Marin County|    70| 270.452|  0.000| 5,092| 19673.449| 161.341| 258,826|
| |San Francisco County|    61| 69.196| N/A| 6,916|  7845.281| N/A| 881,549|
| |Santa Barbara County|    60| 134.379|  0.000| 6,167| 13811.901|  0.000| 446,499|
| |Kings County|    56| 366.157|  2.763| 4,453| 29115.993| 650.269| 152,940|
| |Merced County|    50| 180.063|  0.000| 4,285| 15431.432|  0.000| 277,680|
| |Yolo County|    42| 190.476|  1.917| 1,572|  7129.252| 98.116| 220,500|
| |Sonoma County|    39| 78.894|  4.046| 3,113|  6297.336| 176.247| 494,336|
| |Solano County|    37| 82.655|  0.000| 3,611|  8066.696|  0.000| 447,643|
| |Madera County|    30| 190.686|  0.000| 1,943| 12350.073|  0.000| 157,327|
| |Monterey County|    30| 69.115|  1.446| 4,924| 11344.028| 286.780| 434,061|
| |Placer County|    16| 40.168|  1.072| 1,925|  4832.689| 28.267| 398,329|
| |San Luis Obispo County|    16| 56.515|  1.480| 1,902|  6718.213| 179.179| 283,111|
| |Shasta County|     9| 49.978| N/A|   390|  2165.704| N/A| 180,080|
| |Mendocino County|     9| 103.748| N/A|   322|  3711.858| N/A|  86,749|
| |Napa County|     8| 58.079| N/A|   888|  6446.742| N/A| 137,744|
| |Butte County|     7| 31.936| N/A|   941|  4293.157| N/A| 219,186|
| |Sutter County|     6| 61.874| N/A|   797|  8218.952| N/A|  96,971|
| |Colusa County|     4| 185.641| N/A|   331| 15361.767| N/A|  21,547|
| |Humboldt County|     4| 29.508| N/A|   233|  1718.821| N/A| 135,558|
| |San Benito County|     4| 63.686| N/A|   647| 10301.236| N/A|  62,808|
| |Santa Cruz County|     4| 14.641| N/A| 1,152|  4216.490| N/A| 273,213|
| |Yuba County|     4| 50.847| N/A|   502|  6381.248| N/A|  78,668|
| |Mariposa County|     2| 116.259| N/A|    57|  3313.376| N/A|  17,203|
| |Tuolumne County|     2| 36.712| N/A|   141|  2588.201| N/A|  54,478|
| |Tehama County|     1| 15.365| N/A|   234|  3595.354| N/A|  65,084|
| |Lake County|     1| 15.531| N/A|   208|  3230.516| N/A|  64,386|
| |Mono County|     1| 69.233| N/A|   145| 10038.770| N/A|  14,444|
| |Nevada County|     1| 10.025| N/A|   299|  2997.343| N/A|  99,755|
| |Calaveras County|     1| 21.784| N/A|   125|  2723.015| N/A|  45,905|
| |Inyo County|     1| 55.435| N/A|    61|  3381.562| N/A|  18,039|
| |El Dorado County|     1|  5.186| N/A|   637|  3303.205| N/A| 192,843|
| |Glenn County|     1| 35.220| N/A|   332| 11693.023| N/A|  28,393|
| |Amador County|     0|  0.000| N/A|   126|  3169.652| N/A|  39,752|
| |Plumas County|     0|  0.000| N/A|    33|  1754.666| N/A|  18,807|
| |Trinity County|     0|  0.000| N/A|     5|   407.000| N/A|  12,285|
| |Siskiyou County|     0|  0.000| N/A|    73|  1676.658| N/A|  43,539|
| |Sierra County|     0|  0.000| N/A|     2|   665.557| N/A|   3,005|
| |Modoc County|     0|  0.000| N/A|     2|   226.219| N/A|   8,841|
| |Lassen County|     0|  0.000| N/A|   626| 20475.583| N/A|  30,573|
| |Del Norte County|     0|  0.000| N/A|    88|  3164.102| N/A|  27,812|
| |Alpine County|     0|  0.000| N/A|     2|  1771.479| N/A|   1,129|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,641| 1253.681| N/A|118,256| 17157.192| N/A|6,892,503|
| |Middlesex County| 1,988| 1233.481|  1.803|25,932| 16089.853| 43.485|1,611,699|
| |Essex County| 1,185| 1501.836|  2.648|17,422| 22080.164| 74.141| 789,034|
| |Suffolk County| 1,059| 1317.317|  1.244|21,378| 26592.628| 62.551| 803,907|
| |Worcester County|   993| 1195.490|  1.204|13,442| 16183.053| 44.039| 830,622|
| |Norfolk County|   988| 1397.899|  2.830|10,361| 14659.545| 97.627| 706,775|
| |Plymouth County|   713| 1367.992|  1.919| 9,126| 17509.526| 22.047| 521,202|
| |Hampden County|   699| 1498.804|  2.144| 7,477| 16032.266| 48.831| 466,372|
| |Bristol County|   626| 1107.539|  2.169| 9,153| 16193.780| 57.195| 565,217|
| |Barnstable County|   157| 737.124|  0.000| 1,764|  8282.079| 25.768| 212,990|
| |Hampshire County|   127| 789.654|  0.000| 1,139|  7082.012| 24.322| 160,830|
| |Franklin County|    60| 854.944|  0.000|   405|  5770.875| 10.344|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   657|  5258.356|  8.004| 124,944|
| |Dukes County|     0|  0.000| N/A|     0|     0.000| N/A|  17,332|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,526| 593.916| N/A|183,175| 14455.302| N/A|12,671,821|
| |Cook County| 4,897| 950.831|  0.815|107,247| 20823.718| 109.537|5,150,233|
| |DuPage County|   510| 552.593|  0.000|11,558| 12523.282| 100.491| 922,921|
| |Lake County|   440| 631.698|  0.000|12,089| 17355.912| 103.562| 696,535|
| |Will County|   339| 490.776|  0.000| 8,650| 12522.747| 103.749| 690,743|
| |Kane County|   298| 559.726|  0.888| 9,239| 17353.396| 99.610| 532,403|
| |St. Clair County|   156| 600.725|  0.823| 3,655| 14074.690| 174.689| 259,686|
| |Winnebago County|   125| 442.365|  3.539| 3,688| 13051.541| 49.581| 282,572|
| |McHenry County|   114| 370.402|  1.891| 2,961|  9620.696| 93.678| 307,774|
| |Madison County|    73| 277.602|  1.624| 2,222|  8449.762| 136.900| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,686| 15346.526| 73.010| 109,862|
| |Peoria County|    35| 195.335|  0.000| 1,341|  7484.136| 170.221| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,037|  5326.909| 138.261| 194,672|
| |Rock Island County|    31| 218.496|  0.000| 1,605| 11312.456| 144.489| 141,879|
| |DeKalb County|    29| 276.462|  0.000|   850|  8103.187| 109.631| 104,897|
| |Macon County|    23| 221.135|  0.000|   489|  4701.516| 153.833| 104,009|
| |Boone County|    23| 429.553|  0.000|   735| 13727.028| 93.381|  53,544|
| |Kendall County|    23| 178.308|  0.000| 1,291| 10008.528| 116.288| 128,990|
| |Union County|    21| 1261.034|  0.000|   303| 18194.920| 210.172|  16,653|
| |LaSalle County|    20| 184.045| 18.405|   560|  5153.264| 269.093| 108,669|
| |Champaign County|    19| 90.610|  0.000| 1,547|  7377.593| 128.762| 209,689|
| |Coles County|    19| 375.338|  0.000|   401|  7921.614| 155.426|  50,621|
| |Jackson County|    19| 334.802|  0.000|   650| 11453.744| 167.401|  56,750|
| |Jefferson County|    17| 451.120|  0.000|   192|  5095.001| 123.806|  37,684|
| |Clinton County|    17| 452.585|  0.000|   349|  9291.305| 194.942|  37,562|
| |Whiteside County|    16| 289.986|  0.000|   313|  5672.859| 54.372|  55,175|
| |McDonough County|    15| 505.357|  0.000|   128|  4312.378| 51.924|  29,682|
| |McLean County|    15| 87.455|  0.000|   572|  3334.946| 93.285| 171,517|
| |Monroe County|    13| 375.321|  0.000|   278|  8026.099| 134.513|  34,637|
| |Cass County|    11| 905.573|  0.000|   202| 16629.620| 215.218|  12,147|
| |Tazewell County|     8| 60.697| N/A|   388|  2943.787| N/A| 131,803|
| |Iroquois County|     7| 258.169| N/A|   249|  9183.448| N/A|  27,114|
| |Randolph County|     7| 220.250| N/A|   435| 13686.993| N/A|  31,782|
| |Montgomery County|     7| 246.357| N/A|   147|  5173.506| N/A|  28,414|
| |Jasper County|     7| 728.408| N/A|    53|  5515.088| N/A|   9,610|
| |Stephenson County|     6| 134.838| N/A|   318|  7146.389| N/A|  44,498|
| |Grundy County|     5| 97.936| N/A|   282|  5523.563| N/A|  51,054|
| |Morgan County|     5| 148.553| N/A|   203|  6031.256| N/A|  33,658|
| |Ogle County|     5| 98.730| N/A|   377|  7444.267| N/A|  50,643|
| |Williamson County|     5| 75.078| N/A|   341|  5120.351| N/A|  66,597|
| |Adams County|     4| 61.129| N/A|   445|  6800.642| N/A|  65,435|
| |Christian County|     4| 123.824| N/A|   115|  3559.931| N/A|  32,304|
| |Macoupin County|     3| 66.776| N/A|   137|  3049.459| N/A|  44,926|
| |Woodford County|     3| 78.005| N/A|    98|  2548.168| N/A|  38,459|
| |Fayette County|     3| 140.607| N/A|    58|  2718.410| N/A|  21,336|
| |Carroll County|     3| 209.717| N/A|    46|  3215.659| N/A|  14,305|
| |Vermilion County|     2| 26.400| N/A|   215|  2837.984| N/A|  75,758|
| |Bond County|     2| 121.758| N/A|    57|  3470.108| N/A|  16,426|
| |Bureau County|     2| 61.297| N/A|   144|  4413.387| N/A|  32,628|
| |Douglas County|     2| 102.749| N/A|   102|  5240.175| N/A|  19,465|
| |Cumberland County|     2| 185.770| N/A|    47|  4365.595| N/A|  10,766|
| |Lee County|     2| 58.658| N/A|   148|  4340.685| N/A|  34,096|
| |Livingston County|     2| 56.104| N/A|    92|  2580.790| N/A|  35,648|
| |Knox County|     1| 20.121| N/A|   262|  5271.736| N/A|  49,699|
| |Jersey County|     1| 45.928| N/A|    70|  3214.991| N/A|  21,773|
| |Jo Daviess County|     1| 47.092| N/A|   113|  5321.403| N/A|  21,235|
| |Wayne County|     1| 61.671| N/A|    50|  3083.565| N/A|  16,215|
| |Henry County|     1| 20.444| N/A|   207|  4232.004| N/A|  48,913|
| |Saline County|     1| 42.569| N/A|   113|  4810.353| N/A|  23,491|
| |Perry County|     1| 47.810| N/A|   126|  6024.096| N/A|  20,916|
| |Hancock County|     1| 56.472| N/A|    34|  1920.036| N/A|  17,708|
| |Shelby County|     1| 46.224| N/A|    60|  2773.412| N/A|  21,634|
| |Effingham County|     1| 29.405| N/A|   116|  3410.962| N/A|  34,008|
| |Ford County|     1| 77.155| N/A|    41|  3163.336| N/A|  12,961|
| |Schuyler County|     0|  0.000| N/A|    17|  2511.820| N/A|   6,768|
| |Moultrie County|     0|  0.000| N/A|    55|  3792.842| N/A|  14,501|
| |Menard County|     0|  0.000| N/A|    48|  3935.717| N/A|  12,196|
| |Massac County|     0|  0.000| N/A|    34|  2468.777| N/A|  13,772|
| |Mason County|     0|  0.000| N/A|    42|  3143.948| N/A|  13,359|
| |Marshall County|     0|  0.000| N/A|    21|  1835.985| N/A|  11,438|
| |Marion County|     0|  0.000| N/A|   138|  3709.179| N/A|  37,205|
| |Washington County|     0|  0.000| N/A|    58|  4176.568| N/A|  13,887|
| |Lawrence County|     0|  0.000| N/A|    42|  2678.913| N/A|  15,678|
| |Mercer County|     0|  0.000| N/A|    70|  4534.560| N/A|  15,437|
| |Piatt County|     0|  0.000| N/A|    48|  2936.858| N/A|  16,344|
| |White County|     0|  0.000| N/A|    58|  4284.553| N/A|  13,537|
| |Pope County|     0|  0.000| N/A|     8|  1915.250| N/A|   4,177|
| |Warren County|     0|  0.000| N/A|   183| 10864.403| N/A|  16,844|
| |Wabash County|     0|  0.000| N/A|    32|  2777.778| N/A|  11,520|
| |Stark County|     0|  0.000| N/A|     7|  1310.371| N/A|   5,342|
| |Scott County|     0|  0.000| N/A|    11|  2221.773| N/A|   4,951|
| |Richland County|     0|  0.000| N/A|    13|   838.007| N/A|  15,513|
| |Putnam County|     0|  0.000| N/A|     8|  1393.971| N/A|   5,739|
| |Pulaski County|     0|  0.000| N/A|    91| 17057.170| N/A|   5,335|
| |Pike County|     0|  0.000| N/A|    13|   835.422| N/A|  15,561|
| |Logan County|     0|  0.000| N/A|    86|  3005.102| N/A|  28,618|
| |Johnson County|     0|  0.000| N/A|    57|  4590.481| N/A|  12,417|
| |Fulton County|     0|  0.000| N/A|    26|   757.135| N/A|  34,340|
| |Franklin County|     0|  0.000| N/A|   132|  3431.334| N/A|  38,469|
| |Edwards County|     0|  0.000| N/A|    13|  2032.838| N/A|   6,395|
| |Edgar County|     0|  0.000| N/A|    26|  1515.063| N/A|  17,161|
| |Crawford County|     0|  0.000| N/A|    29|  1553.544| N/A|  18,667|
| |Clay County|     0|  0.000| N/A|    14|  1061.893| N/A|  13,184|
| |Clark County|     0|  0.000| N/A|    68|  4403.860| N/A|  15,441|
| |Calhoun County|     0|  0.000| N/A|     7|  1477.105| N/A|   4,739|
| |Brown County|     0|  0.000| N/A|    13|  1976.285| N/A|   6,578|
| |Alexander County|     0|  0.000| N/A|    36|  6248.915| N/A|   5,761|
| |Gallatin County|     0|  0.000| N/A|    45|  9320.630| N/A|   4,828|
| |Greene County|     0|  0.000| N/A|    20|  1542.139| N/A|  12,969|
| |Hamilton County|     0|  0.000| N/A|    23|  2833.908| N/A|   8,116|
| |Hardin County|     0|  0.000| N/A|    17|  4449.097| N/A|   3,821|
| |Henderson County|     0|  0.000| N/A|     9|  1354.198| N/A|   6,646|
| |De Witt County|     0|  0.000| N/A|    30|  1918.404| N/A|  15,638|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,224| 564.287| N/A|118,894|  9287.151| N/A|12,801,989|
| |Philadelphia County| 1,692| 1068.139| N/A|30,665| 19358.435| N/A|1,584,064|
| |Montgomery County|   850| 1022.969|  0.000| 9,870| 11878.471| 39.524| 830,915|
| |Delaware County|   687| 1212.181|  1.034| 8,859| 15631.313| 110.333| 566,747|
| |Bucks County|   579| 921.578|  0.680| 7,020| 11173.540| 55.475| 628,270|
| |Lancaster County|   407| 745.798|  0.286| 5,682| 10411.857| 84.292| 545,724|
| |Berks County|   365| 866.646|  0.000| 5,218| 12389.473| 59.359| 421,164|
| |Chester County|   348| 662.871|  0.000| 4,965|  9457.341| 76.192| 524,989|
| |Lehigh County|   335| 907.077|  0.355| 4,853| 13140.437| 10.831| 369,318|
| |Northampton County|   290| 949.932|  0.000| 3,863| 12653.750| 35.742| 305,285|
| |Allegheny County|   234| 192.427|  0.812| 8,310|  6833.629| 61.334|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,901|  9066.456|  8.856| 209,674|
| |Luzerne County|   183| 576.529|  0.000| 3,338| 10516.135| 94.450| 317,417|
| |Dauphin County|   155| 556.955|  0.000| 2,682|  9637.117| 55.104| 278,299|
| |Monroe County|   123| 722.378|  0.000| 1,598|  9385.039| 41.111| 170,271|
| |Beaver County|    89| 542.918|  0.957| 1,237|  7545.950| 53.248| 163,929|
| |York County|    88| 195.966|  2.227| 2,350|  5233.177| 65.332| 449,058|
| |Cumberland County|    70| 276.276|  0.000| 1,230|  4854.561| 30.864| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,577| 11121.847| 37.237| 141,793|
| |Schuylkill County|    49| 346.635|  0.000|   896|  6338.472| 38.448| 141,359|
| |Westmoreland County|    46| 131.843|  0.000| 1,457|  4175.994| 50.367| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,284|  8282.428| 30.172| 155,027|
| |Columbia County|    35| 538.760|  0.000|   462|  7111.631| 15.393|  64,964|
| |Carbon County|    28| 436.259|  0.000|   360|  5609.049| 13.581|  64,182|
| |Susquehanna County|    26| 644.713|  0.000|   210|  5207.300| 10.532|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003| 14.969|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   339|  2992.083| 35.651| 113,299|
| |Adams County|    20| 194.158|  0.000|   480|  4659.787| 67.955| 103,009|
| |Erie County|    16| 59.319|  0.000|   983|  3644.412| 114.931| 269,728|
| |Butler County|    15| 79.850|  0.000|   605|  3220.603| 15.970| 187,853|
| |Lawrence County|    12| 140.331|  1.835|   349|  4081.299| 64.318|  85,512|
| |Washington County|    11| 53.175|  0.000|   764|  3693.230| 38.673| 206,865|
| |Northumberland County|    11| 121.088|  0.000|   407|  4480.257| 27.556|  90,843|
| |Centre County|    10| 61.582|  0.000|   358|  2204.637|  6.158| 162,385|
| |Mercer County|     9| 82.249| N/A|   356|  3253.400| N/A| 109,424|
| |Wyoming County|     8| 298.574| N/A|    57|  2127.342| N/A|  26,794|
| |Wayne County|     8| 155.760| N/A|   158|  3076.264| N/A|  51,361|
| |Indiana County|     6| 71.367| N/A|   275|  3270.967| N/A|  84,073|
| |Armstrong County|     6| 92.686| N/A|   188|  2904.148| N/A|  64,735|
| |Juniata County|     6| 242.297| N/A|   127|  5128.619| N/A|  24,763|
| |Perry County|     5| 108.057| N/A|   120|  2593.361| N/A|  46,272|
| |Clinton County|     5| 129.426| N/A|   115|  2976.807| N/A|  38,632|
| |Huntingdon County|     4| 88.605| N/A|   290|  6423.888| N/A|  45,144|
| |Bedford County|     4| 83.528| N/A|   130|  2714.668| N/A|  47,888|
| |Fayette County|     4| 30.942| N/A|   414|  3202.500| N/A| 129,274|
| |Blair County|     3| 24.625| N/A|   233|  1912.517| N/A| 121,829|
| |Bradford County|     3| 49.732| N/A|    82|  1359.349| N/A|  60,323|
| |Cambria County|     3| 23.043| N/A|   274|  2104.584| N/A| 130,192|
| |Montour County|     3| 164.564| N/A|    93|  5101.481| N/A|  18,230|
| |Clarion County|     2| 52.032| N/A|    76|  1977.210| N/A|  38,438|
| |Fulton County|     2| 137.646| N/A|    24|  1651.755| N/A|  14,530|
| |Elk County|     2| 66.867| N/A|    45|  1504.514| N/A|  29,910|
| |Somerset County|     2| 27.231| N/A|   125|  1701.907| N/A|  73,447|
| |Union County|     2| 44.521| N/A|   173|  3851.034| N/A|  44,923|
| |Tioga County|     2| 49.272| N/A|    35|   862.260| N/A|  40,591|
| |Snyder County|     2| 49.539| N/A|    98|  2427.425| N/A|  40,372|
| |Mifflin County|     1| 21.674| N/A|   109|  2362.478| N/A|  46,138|
| |McKean County|     1| 24.615| N/A|    33|   812.308| N/A|  40,625|
| |Warren County|     1| 25.516| N/A|    19|   484.805| N/A|  39,191|
| |Crawford County|     1| 11.816| N/A|   132|  1559.749| N/A|  84,629|
| |Jefferson County|     1| 23.028| N/A|    58|  1335.636| N/A|  43,425|
| |Greene County|     1| 27.599| N/A|   109|  3008.307| N/A|  36,233|
| |Forest County|     0|  0.000| N/A|     9|  1241.893| N/A|   7,247|
| |Venango County|     0|  0.000| N/A|    62|  1223.652| N/A|  50,668|
| |Sullivan County|     0|  0.000| N/A|    10|  1648.533| N/A|   6,066|
| |Potter County|     0|  0.000| N/A|    20|  1210.214| N/A|  16,526|
| |Clearfield County|     0|  0.000| N/A|   141|  1779.068| N/A|  79,255|
| |Cameron County|     0|  0.000| N/A|     6|  1349.224| N/A|   4,447|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 7,157| 333.229| N/A|491,253| 22872.661| N/A|21,477,737|
| |Miami-Dade County| 1,694| 623.496|  8.681|123,644| 45508.550| 564.440|2,716,940|
| |Palm Beach County|   845| 564.549|  6.844|34,550| 23083.039| 256.973|1,496,770|
| |Broward County|   748| 383.044|  3.946|58,531| 29973.197| 443.983|1,952,778|
| |Pinellas County|   442| 453.335|  2.564|16,886| 17319.045| 163.906| 974,996|
| |Hillsborough County|   348| 236.418|  2.378|30,450| 20686.591| 225.548|1,471,968|
| |Lee County|   300| 389.319|  0.000|15,799| 20502.818| 162.216| 770,577|
| |Polk County|   271| 373.908|  1.391|13,137| 18125.575| 277.327| 724,777|
| |Orange County|   239| 171.516|  4.002|29,927| 21476.879| 190.500|1,393,452|
| |Manatee County|   187| 463.729|  2.480| 8,825| 21884.524| 211.824| 403,253|
| |Duval County|   160| 167.057|  1.973|21,830| 22792.885| 271.191| 957,755|
| |St. Lucie County|   125| 380.753|  4.858| 5,256| 16009.893| 241.859| 328,297|
| |Collier County|   124| 322.160|  0.919| 9,811| 25489.605| 200.051| 384,902|
| |Sarasota County|   121| 278.968|  0.000| 5,814| 13404.282| 167.914| 433,742|
| |Brevard County|   117| 194.371|  1.661| 5,619|  9334.786| 95.736| 601,942|
| |Volusia County|   116| 209.657|  2.587| 7,194| 13002.364| 214.527| 553,284|
| |Pasco County|    99| 178.717|  2.273| 6,548| 11820.625| 144.369| 553,947|
| |Escambia County|    97| 304.729|  1.144| 8,125| 25524.950| 376.385| 318,316|
| |Charlotte County|    89| 471.124|  3.999| 2,062| 10915.251| 206.135| 188,910|
| |Seminole County|    88| 186.509|  4.263| 6,687| 14172.598| 134.608| 471,826|
| |Osceola County|    81| 215.568|  8.007| 8,894| 23669.930| 352.233| 375,751|
| |Martin County|    77| 478.261|  5.263| 3,644| 22633.540| 81.373| 161,000|
| |Marion County|    64| 175.065|  4.103| 5,286| 14459.255| 331.999| 365,579|
| |Lake County|    51| 138.920|  0.000| 4,708| 12824.215| 153.932| 367,118|
| |Indian River County|    48| 300.144|  3.238| 2,340| 14632.042| 218.855| 159,923|
| |Clay County|    48| 218.926|  0.000| 2,935| 13386.423| 190.743| 219,252|
| |Hendry County|    37| 880.491|  0.000| 1,667| 39669.697| 284.290|  42,022|
| |Suwannee County|    36| 810.500|  0.000| 1,190| 26791.544| 413.660|  44,417|
| |Sumter County|    35| 264.311| 11.908| 1,142|  8624.075| 180.624| 132,420|
| |Hernando County|    33| 170.173|  0.624| 1,766|  9106.848| 155.489| 193,920|
| |Jackson County|    33| 710.992| 12.324| 1,618| 34860.171| 310.288|  46,414|
| |Okaloosa County|    30| 142.357|  1.926| 3,031| 14382.788| 424.718| 210,738|
| |Citrus County|    30| 200.458|  4.951| 1,299|  8679.848| 153.685| 149,657|
| |St. Johns County|    29| 109.570|  2.838| 3,362| 12702.515| 181.357| 264,672|
| |Highlands County|    29| 273.016|  0.000| 1,277| 12022.105| 320.087| 106,221|
| |Santa Rosa County|    24| 130.213|  1.702| 3,484| 18902.628| 341.810| 184,313|
| |Alachua County|    23| 85.488|  0.000| 3,749| 13934.576| 286.324| 269,043|
| |Bay County|    22| 125.927|  2.367| 3,701| 21184.282| 309.560| 174,705|
| |Gadsden County|    20| 438.020| 12.829| 1,576| 34515.988| 1522.120|  45,660|
| |Putnam County|    19| 254.962| 19.301| 1,379| 18504.851| 401.836|  74,521|
| |Leon County|    15| 51.093|  0.000| 4,448| 15150.793| 281.905| 293,582|
| |DeSoto County|    15| 394.726|  0.000| 1,297| 34130.681| 228.817|  38,001|
| |Washington County|    14| 549.602|  0.000|   597| 23436.580| 765.516|  25,473|
| |Walton County|    13| 175.507|  0.000| 1,256| 16956.704| 220.359|  74,071|
| |Nassau County|    11| 124.118|  4.666| 1,121| 12648.801| 243.934|  88,625|
| |Columbia County|    11| 153.447|  5.803| 2,598| 36241.386| 448.996|  71,686|
| |Flagler County|    11| 95.585|  8.690|   945|  8211.607| 119.216| 115,081|
| |Monroe County|    11| 148.192| 13.623| 1,379| 18577.895| 360.487|  74,228|
| |Madison County|     8| 432.596| N/A|   655| 35418.807| N/A|  18,493|
| |Hardee County|     7| 259.866| N/A|   857| 31814.976| N/A|  26,937|
| |Calhoun County|     7| 496.278| N/A|   328| 23254.165| N/A|  14,105|
| |Okeechobee County|     6| 142.288| N/A|   958| 22718.649| N/A|  42,168|
| |Jefferson County|     5| 350.976| N/A|   363| 25480.837| N/A|  14,246|
| |Baker County|     4| 136.939| N/A|   403| 13796.645| N/A|  29,210|
| |Wakulla County|     4| 118.557| N/A|   612| 18139.245| N/A|  33,739|
| |Union County|     4| 262.519| N/A|   225| 14766.686| N/A|  15,237|
| |Bradford County|     4| 141.839| N/A|   340| 12056.310| N/A|  28,201|
| |Dixie County|     4| 237.727| N/A|   277| 16462.617| N/A|  16,826|
| |Taylor County|     3| 139.089| N/A|   396| 18359.683| N/A|  21,569|
| |Levy County|     3| 72.284| N/A|   618| 14890.490| N/A|  41,503|
| |Hamilton County|     3| 207.929| N/A|   586| 40615.470| N/A|  14,428|
| |Glades County|     3| 217.218| N/A|   392| 28383.173| N/A|  13,811|
| |Gilchrist County|     3| 161.447| N/A|   331| 17812.937| N/A|  18,582|
| |Holmes County|     2| 101.952| N/A|   455| 23194.168| N/A|  19,617|
| |Franklin County|     2| 164.948| N/A|   158| 13030.928| N/A|  12,125|
| |Gulf County|     2| 146.638| N/A|   390| 28594.472| N/A|  13,639|
| |Liberty County|     2| 239.406| N/A|   412| 49317.692| N/A|   8,354|
| |Lafayette County|     1| 118.737| N/A|   113| 13417.241| N/A|   8,422|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 6,884| 237.413| N/A|456,624| 15747.892| N/A|28,995,881|
| |Harris County|   767| 162.730|  2.259|78,100| 16570.043| 352.250|4,713,325|
| |Dallas County|   691| 262.188|  2.204|51,490| 19536.971| 180.875|2,635,516|
| |Hidalgo County|   656| 755.145|  5.830|17,353| 19975.665| 169.202| 868,707|
| |Bexar County|   622| 310.448| 16.471|41,138| 20532.514| 68.138|2,003,554|
| |Tarrant County|   391| 185.968|  3.611|29,054| 13818.689| 279.189|2,102,515|
| |Cameron County|   368| 869.641| 27.550|13,516| 31940.411| 2804.228| 423,163|
| |El Paso County|   251| 299.081|  3.710|14,914| 17770.883| 300.272| 839,238|
| |Travis County|   236| 185.250|  1.311|21,214| 16652.093| 219.788|1,273,954|
| |Nueces County|   195| 538.237| 26.393|12,575| 34709.380| 318.673| 362,294|
| |Fort Bend County|   146| 179.872|  2.351| 7,191|  8859.315| 67.144| 811,688|
| |Galveston County|   103| 301.047|  5.846| 8,825| 25793.610| 151.985| 342,139|
| |Williamson County|    80| 135.467|  0.000| 5,832|  9875.523| 99.060| 590,551|
| |Webb County|    77| 278.328|  2.835| 6,411| 23173.518| 567.261| 276,652|
| |Denton County|    75| 84.535|  1.458| 6,938|  7820.047| 84.547| 887,207|
| |Jefferson County|    73| 290.183|  7.950| 5,506| 21886.987| 94.964| 251,565|
| |Montgomery County|    73| 120.186|  0.951| 6,291| 10357.414| 78.203| 607,391|
| |Brazoria County|    73| 195.049|  3.207| 6,732| 17987.303| 285.505| 374,264|
| |Collin County|    72| 69.583|  0.000| 6,403|  6188.088| 48.322|1,034,730|
| |Lubbock County|    65| 209.293|  3.220| 5,593| 18008.880| 155.288| 310,569|
| |Comal County|    63| 403.306|  7.334| 1,679| 10748.420| 32.008| 156,209|
| |Starr County|    51| 789.071| 15.472| 1,894| 29303.916| 625.779|  64,633|
| |Ector County|    49| 294.785|  0.000| 3,287| 19774.640|  0.000| 166,223|
| |Val Verde County|    49| 999.490|  0.000| 1,507| 30739.419| 355.182|  49,025|
| |Guadalupe County|    44| 263.715|  5.994| 1,597|  9571.643|  3.761| 166,847|
| |Brazos County|    42| 183.237|  0.000| 3,922| 17110.872| 100.144| 229,211|
| |Midland County|    42| 237.514|  0.000| 2,179| 12322.430|  0.000| 176,832|
| |McLennan County|    39| 151.974|  0.000| 4,436| 17286.058| 219.145| 256,623|
| |Maverick County|    39| 664.146|  0.000| 1,989| 33871.462|  0.000|  58,722|
| |Potter County|    39| 332.155|  0.000| 3,505| 29851.382| 204.403| 117,415|
| |Washington County|    38| 1059.027|  0.000|   497| 13850.956| 287.363|  35,882|
| |Walker County|    38| 520.755|  0.000| 2,840| 38919.571| 197.308|  72,971|
| |Angelina County|    36| 415.153| 11.532| 1,647| 18993.254| 75.497|  86,715|
| |Nacogdoches County|    36| 552.113|  2.406| 1,035| 15873.259| 92.019|  65,204|
| |Ellis County|    34| 183.957|  0.000| 2,472| 13374.742| 16.389| 184,826|
| |Hays County|    33| 143.359|  2.498| 4,893| 21256.261|  0.000| 230,191|
| |Bell County|    32| 88.173|  1.460| 3,496|  9632.871| 10.093| 362,924|
| |Bowie County|    31| 332.458|  7.826|   708|  7592.900| 24.653|  93,245|
| |Victoria County|    29| 314.930|  4.673| 3,203| 34783.459|  0.000|  92,084|
| |Liberty County|    25| 283.386|  0.000|   851|  9646.448| 70.864|  88,219|
| |Johnson County|    25| 142.193|  3.014| 1,541|  8764.795| 45.975| 175,817|
| |Tom Green County|    24| 201.342|  0.000| 2,421| 20310.403| 327.181| 119,200|
| |Medina County|    24| 465.261|  3.041|   595| 11534.584| 116.315|  51,584|
| |Matagorda County|    23| 627.678| 22.704|   681| 18584.723| 172.156|  36,643|
| |Caldwell County|    23| 526.750|  0.000| 1,071| 24528.215|  0.000|  43,664|
| |Kaufman County|    22| 161.582| 22.034| 1,816| 13337.838| 161.497| 136,154|
| |Hale County|    22| 658.564|  0.000| 1,185| 35472.670| 58.677|  33,406|
| |Harrison County|    22| 330.564|  0.000|   624|  9375.986| 73.259|  66,553|
| |Wharton County|    21| 505.342|  3.775|   635| 15280.585| 264.703|  41,556|
| |Gregg County|    21| 169.430|  6.712| 1,313| 10593.408| 67.009| 123,945|
| |Willacy County|    20| 936.417|  0.000|   594| 27811.593| 200.845|  21,358|
| |Grimes County|    20| 692.521|  5.432|   849| 29397.507| 149.394|  28,880|
| |Hunt County|    20| 202.852|  0.000| 1,059| 10741.019| 122.792|  98,594|
| |Taylor County|    19| 137.647|  0.000| 1,092|  7911.094| 35.844| 138,034|
| |Bastrop County|    18| 202.879|  0.000| 1,296| 14607.261| 78.897|  88,723|
| |Rockwall County|    17| 162.036|  0.000|   720|  6862.698|  0.000| 104,915|
| |Deaf Smith County|    17| 916.640|  0.000|   597| 32190.230| 166.166|  18,546|
| |Randall County|    17| 123.445|  0.000| 1,586| 11516.705| 56.673| 137,713|
| |Panola County|    17| 732.948|  0.000|   270| 11640.942| 18.664|  23,194|
| |Orange County|    17| 203.847|  6.869| 1,021| 12242.793| 41.383|  83,396|
| |Smith County|    17| 73.039|  1.292| 2,309|  9920.473|  0.000| 232,751|
| |San Patricio County|    16| 239.772|  2.351|   797| 11943.654| 89.734|  66,730|
| |Wilson County|    16| 313.295|  0.000|   414|  8106.520|  0.000|  51,070|
| |Lamar County|    16| 320.905|  0.000|   625| 12535.350| 88.909|  49,859|
| |Shelby County|    16| 633.062|  0.000|   381| 15074.780| 52.393|  25,274|
| |DeWitt County|    15| 744.048|  7.781|   531| 26339.286| 23.344|  20,160|
| |Atascosa County|    15| 293.238|  0.000|   405|  7917.424|  0.000|  51,153|
| |Brown County|    14| 369.744|  0.000|   351|  9270.019|  0.000|  37,864|
| |Titus County|    14| 427.481|  0.000| 1,289| 39358.779|  0.000|  32,750|
| |Lavaca County|    14| 694.651|  0.000|   593| 29423.440|  0.000|  20,154|
| |Fayette County|    13| 512.901|  0.000|   367| 14479.602|  0.000|  25,346|
| |Parker County|    12| 83.988|  0.000| 1,070|  7488.907| 13.973| 142,878|
| |Aransas County|    12| 510.421|  0.000|   158|  6720.544| 92.752|  23,510|
| |Moore County|    12| 573.066|  0.000| 1,013| 48376.313| 37.296|  20,940|
| |San Augustine County|    11| 1335.438|  0.000|   155| 18817.531| 37.819|   8,237|
| |Grayson County|    11| 80.756|  0.000| 1,025|  7525.035| 77.807| 136,212|
| |Hardin County|    11| 190.966|  2.723|   811| 14079.372| 24.032|  57,602|
| |Red River County|    11| 914.913|  0.000|   134| 11145.305|  0.000|  12,023|
| |Wichita County|    10| 75.626|  0.000|   902|  6821.447|  0.000| 132,230|
| |Hood County|     9| 146.002| N/A|   437|  7089.207| N/A|  61,643|
| |Anderson County|     9| 155.885| N/A| 2,307| 39958.431| N/A|  57,735|
| |Henderson County|     9| 108.778| N/A|   577|  6973.905| N/A|  82,737|
| |Polk County|     9| 175.258| N/A|   659| 12832.746| N/A|  51,353|
| |Bee County|     9| 276.370| N/A|   626| 19223.092| N/A|  32,565|
| |Lee County|     8| 464.064| N/A|   153|  8875.225| N/A|  17,239|
| |Navarro County|     8| 159.639| N/A|   767| 15305.410| N/A|  50,113|
| |Jim Wells County|     8| 197.619| N/A|   630| 15562.472| N/A|  40,482|
| |San Jacinto County|     8| 277.210| N/A|   148|  5128.383| N/A|  28,859|
| |Fannin County|     8| 225.263| N/A|   214|  6025.793| N/A|  35,514|
| |Burnet County|     7| 145.364| N/A|   542| 11255.321| N/A|  48,155|
| |Gonzales County|     7| 335.941| N/A|   617| 29610.789| N/A|  20,837|
| |Lamb County|     7| 542.930| N/A|   203| 15744.978| N/A|  12,893|
| |Parmer County|     7| 728.787| N/A|   311| 32378.969| N/A|   9,605|
| |Cass County|     7| 233.131| N/A|   153|  5095.584| N/A|  30,026|
| |Marion County|     7| 710.371| N/A|   127| 12888.167| N/A|   9,854|
| |Uvalde County|     7| 261.770| N/A|   496| 18548.297| N/A|  26,741|
| |Sabine County|     6| 569.152| N/A|    44|  4173.781| N/A|  10,542|
| |Palo Pinto County|     6| 205.557| N/A|   194|  6646.339| N/A|  29,189|
| |Houston County|     6| 261.233| N/A|   249| 10841.170| N/A|  22,968|
| |Kerr County|     6| 114.068| N/A|   348|  6615.970| N/A|  52,600|
| |Andrews County|     6| 320.770| N/A|   267| 14274.258| N/A|  18,705|
| |Kleberg County|     5| 162.973| N/A|   361| 11766.623| N/A|  30,680|
| |Floyd County|     5| 875.350| N/A|    83| 14530.812| N/A|   5,712|
| |Erath County|     5| 117.102| N/A|   462| 10820.179| N/A|  42,698|
| |Wise County|     5| 71.445| N/A|   311|  4443.873| N/A|  69,984|
| |Wood County|     5| 109.796| N/A|   291|  6390.127| N/A|  45,539|
| |Coryell County|     5| 65.832| N/A|   614|  8084.160| N/A|  75,951|
| |Dallam County|     5| 686.153| N/A|   179| 24564.293| N/A|   7,287|
| |Zavala County|     5| 422.297| N/A|   175| 14780.405| N/A|  11,840|
| |Jasper County|     5| 140.730| N/A|   291|  8190.492| N/A|  35,529|
| |Frio County|     5| 246.233| N/A|   475| 23392.101| N/A|  20,306|
| |Burleson County|     5| 271.106| N/A|   231| 12525.077| N/A|  18,443|
| |Jackson County|     5| 338.753| N/A|   320| 21680.217| N/A|  14,760|
| |Hockley County|     4| 173.754| N/A|   181|  7862.387| N/A|  23,021|
| |Young County|     4| 222.099| N/A|   139|  7717.934| N/A|  18,010|
| |Karnes County|     4| 256.394| N/A|   300| 19229.537| N/A|  15,601|
| |Gillespie County|     4| 148.214| N/A|   171|  6336.149| N/A|  26,988|
| |Bailey County|     4| 571.429| N/A|   158| 22571.429| N/A|   7,000|
| |Lynn County|     4| 672.156| N/A|    65| 10922.534| N/A|   5,951|
| |Dawson County|     4| 314.268| N/A|   137| 10763.671| N/A|  12,728|
| |Blanco County|     4| 335.261| N/A|    98|  8213.897| N/A|  11,931|
| |Newton County|     4| 294.226| N/A|    86|  6325.855| N/A|  13,595|
| |Cherokee County|     4| 75.979| N/A|   783| 14872.925| N/A|  52,646|
| |Camp County|     4| 305.483| N/A|   218| 16648.847| N/A|  13,094|
| |Duval County|     3| 268.889| N/A|   152| 13623.734| N/A|  11,157|
| |Austin County|     3| 99.893| N/A|   213|  7092.435| N/A|  30,032|
| |Bandera County|     3| 129.803| N/A|    83|  3591.208| N/A|  23,112|
| |Van Zandt County|     3| 53.013| N/A|   332|  5866.761| N/A|  56,590|
| |Waller County|     3| 54.303| N/A|   408|  7385.150| N/A|  55,246|
| |Limestone County|     3| 128.003| N/A|   199|  8490.848| N/A|  23,437|
| |Crockett County|     3| 866.051| N/A|   154| 44457.275| N/A|   3,464|
| |Castro County|     3| 398.406| N/A|   170| 22576.361| N/A|   7,530|
| |Milam County|     3| 120.856| N/A|   306| 12327.277| N/A|  24,823|
| |Cooke County|     3| 72.715| N/A|   200|  4847.662| N/A|  41,257|
| |Reagan County|     3| 779.423| N/A|    58| 15068.849| N/A|   3,849|
| |Comanche County|     3| 220.022| N/A|   230| 16868.354| N/A|  13,635|
| |Goliad County|     3| 391.747| N/A|    77| 10054.845| N/A|   7,658|
| |Reeves County|     3| 187.782| N/A|   136|  8512.769| N/A|  15,976|
| |Nolan County|     3| 203.887| N/A|   131|  8903.085| N/A|  14,714|
| |Hill County|     3| 81.858| N/A|   308|  8404.049| N/A|  36,649|
| |Callahan County|     3| 215.162| N/A|    41|  2940.544| N/A|  13,943|
| |Howard County|     3| 81.824| N/A|   157|  4282.130| N/A|  36,664|
| |Calhoun County|     3| 140.911| N/A|   453| 21277.595| N/A|  21,290|
| |Martin County|     3| 519.841| N/A|    45|  7797.609| N/A|   5,771|
| |Zapata County|     2| 141.054| N/A|   157| 11072.713| N/A|  14,179|
| |Terry County|     2| 162.114| N/A|   116|  9402.610| N/A|  12,337|
| |Stephens County|     2| 213.538| N/A|    29|  3096.306| N/A|   9,366|
| |Swisher County|     2| 270.380| N/A|    75| 10139.246| N/A|   7,397|
| |Brewster County|     2| 217.320| N/A|   184| 19993.480| N/A|   9,203|
| |Rusk County|     2| 36.761| N/A|   334|  6139.029| N/A|  54,406|
| |Kendall County|     2| 42.167| N/A|   145|  3057.072| N/A|  47,431|
| |Madison County|     2| 140.017| N/A|   645| 45155.419| N/A|  14,284|
| |Ochiltree County|     2| 203.335| N/A|    84|  8540.057| N/A|   9,836|
| |Bosque County|     2| 107.038| N/A|   128|  6850.415| N/A|  18,685|
| |Trinity County|     2| 136.509| N/A|   143|  9760.426| N/A|  14,651|
| |Falls County|     2| 115.627| N/A|   110|  6359.484| N/A|  17,297|
| |Garza County|     2| 321.079| N/A|    97| 15572.323| N/A|   6,229|
| |Hartley County|     2| 358.680| N/A|    82| 14705.882| N/A|   5,576|
| |Hudspeth County|     2| 409.333| N/A|    22|  4502.661| N/A|   4,886|
| |Hansford County|     2| 370.439| N/A|    59| 10927.950| N/A|   5,399|
| |Hamilton County|     2| 236.379| N/A|    55|  6500.414| N/A|   8,461|
| |Chambers County|     2| 45.624| N/A|   894| 20393.731| N/A|  43,837|
| |Hutchinson County|     2| 95.520| N/A|   114|  5444.646| N/A|  20,938|
| |Cottle County|     2| 1430.615| N/A|    14| 10014.306| N/A|   1,398|
| |Crane County|     2| 416.927| N/A|    75| 15634.772| N/A|   4,797|
| |Tyler County|     2| 92.285| N/A|   115|  5306.386| N/A|  21,672|
| |Upshur County|     2| 47.901| N/A|   193|  4622.422| N/A|  41,753|
| |Culberson County|     2| 921.234| N/A|    15|  6909.258| N/A|   2,171|
| |Gray County|     2| 91.383| N/A|   183|  8361.510| N/A|  21,886|
| |Colorado County|     2| 93.054| N/A|   246| 11445.587| N/A|  21,493|
| |Jim Hogg County|     1| 192.308| N/A|    53| 10192.308| N/A|   5,200|
| |Hall County|     1| 337.382| N/A|     8|  2699.055| N/A|   2,964|
| |Eastland County|     1| 54.466| N/A|    51|  2777.778| N/A|  18,360|
| |Kenedy County|     1| 2475.248| N/A|     6| 14851.485| N/A|     404|
| |Hopkins County|     1| 26.966| N/A|   169|  4557.221| N/A|  37,084|
| |Fisher County|     1| 261.097| N/A|    24|  6266.319| N/A|   3,830|
| |Llano County|     1| 45.882| N/A|    86|  3945.859| N/A|  21,795|
| |Pecos County|     1| 63.199| N/A|   209| 13208.620| N/A|  15,823|
| |McCulloch County|     1| 125.251| N/A|    41|  5135.271| N/A|   7,984|
| |Dickens County|     1| 452.284| N/A|     4|  1809.136| N/A|   2,211|
| |Scurry County|     1| 59.869| N/A|   433| 25923.487| N/A|  16,703|
| |Live Oak County|     1| 81.920| N/A|   207| 16957.483| N/A|  12,207|
| |La Salle County|     1| 132.979| N/A|   357| 47473.404| N/A|   7,520|
| |Oldham County|     1| 473.485| N/A|    13|  6155.303| N/A|   2,112|
| |Morris County|     1| 80.723| N/A|    97|  7830.158| N/A|  12,388|
| |Leon County|     1| 57.458| N/A|   138|  7929.212| N/A|  17,404|
| |Montague County|     1| 50.459| N/A|    57|  2876.173| N/A|  19,818|
| |Dimmit County|     1| 98.775| N/A|   124| 12248.123| N/A|  10,124|
| |Franklin County|     1| 93.240| N/A|    84|  7832.168| N/A|  10,725|
| |Rains County|     1| 79.911| N/A|    45|  3595.973| N/A|  12,514|
| |Runnels County|     1| 97.428| N/A|   107| 10424.786| N/A|  10,264|
| |Schleicher County|     1| 358.038| N/A|    35| 12531.328| N/A|   2,793|
| |Robertson County|     1| 58.569| N/A|   216| 12650.814| N/A|  17,074|
| |Lampasas County|     1| 46.668| N/A|    84|  3920.105| N/A|  21,428|
| |Sutton County|     1| 264.831| N/A|    58| 15360.169| N/A|   3,776|
| |Coke County|     1| 295.247| N/A|    39| 11514.615| N/A|   3,387|
| |Clay County|     1| 95.502| N/A|    34|  3247.063| N/A|  10,471|
| |Crosby County|     1| 174.307| N/A|    52|  9063.971| N/A|   5,737|
| |Concho County|     1| 366.838| N/A|    26|  9537.784| N/A|   2,726|
| |Brooks County|     1| 140.984| N/A|    87| 12265.614| N/A|   7,093|
| |Briscoe County|     1| 646.831| N/A|    11|  7115.136| N/A|   1,546|
| |Yoakum County|     1| 114.771| N/A|    85|  9755.538| N/A|   8,713|
| |Winkler County|     1| 124.844| N/A|    68|  8489.388| N/A|   8,010|
| |Upton County|     1| 273.448| N/A|    16|  4375.171| N/A|   3,657|
| |Wilbarger County|     1| 78.315| N/A|    50|  3915.733| N/A|  12,769|
| |Ward County|     1| 83.347| N/A|    83|  6917.820| N/A|  11,998|
| |Haskell County|     0|  0.000| N/A|    35|  6185.931| N/A|   5,658|
| |Kimble County|     0|  0.000| N/A|    13|  2997.464| N/A|   4,337|
| |Kent County|     0|  0.000| N/A|     2|  2624.672| N/A|     762|
| |Jones County|     0|  0.000| N/A|   622| 30971.468| N/A|  20,083|
| |Jeff Davis County|     0|  0.000| N/A|     8|  3518.030| N/A|   2,274|
| |Jack County|     0|  0.000| N/A|    40|  4476.777| N/A|   8,935|
| |Irion County|     0|  0.000| N/A|     9|  5859.375| N/A|   1,536|
| |Carson County|     0|  0.000| N/A|    13|  2193.723| N/A|   5,926|
| |Cochran County|     0|  0.000| N/A|    21|  7360.673| N/A|   2,853|
| |Hemphill County|     0|  0.000| N/A|    41| 10735.795| N/A|   3,819|
| |Hardeman County|     0|  0.000| N/A|    15|  3813.883| N/A|   3,933|
| |Childress County|     0|  0.000| N/A|    34|  4653.709| N/A|   7,306|
| |Collingsworth County|     0|  0.000| N/A|     7|  2397.260| N/A|   2,920|
| |Stonewall County|     0|  0.000| N/A|     4|  2962.963| N/A|   1,350|
| |Coleman County|     0|  0.000| N/A|    11|  1345.566| N/A|   8,175|
| |Delta County|     0|  0.000| N/A|    16|  3001.313| N/A|   5,331|
| |Sterling County|     0|  0.000| N/A|     1|   774.593| N/A|   1,291|
| |Wheeler County|     0|  0.000| N/A|    31|  6131.329| N/A|   5,056|
| |Baylor County|     0|  0.000| N/A|     7|  1994.870| N/A|   3,509|
| |Throckmorton County|     0|  0.000| N/A|     4|  2664.890| N/A|   1,501|
| |Terrell County|     0|  0.000| N/A|     2|  2577.320| N/A|     776|
| |Lipscomb County|     0|  0.000| N/A|    15|  4639.654| N/A|   3,233|
| |Kinney County|     0|  0.000| N/A|    17|  4635.942| N/A|   3,667|
| |King County|     0|  0.000| N/A|     0|     0.000| N/A|     272|
| |Glasscock County|     0|  0.000| N/A|     6|  4258.339| N/A|   1,409|
| |Gaines County|     0|  0.000| N/A|   132|  6141.820| N/A|  21,492|
| |Freestone County|     0|  0.000| N/A|   139|  7049.754| N/A|  19,717|
| |Foard County|     0|  0.000| N/A|     2|  1731.602| N/A|   1,155|
| |Edwards County|     0|  0.000| N/A|    24| 12422.360| N/A|   1,932|
| |Donley County|     0|  0.000| N/A|    43| 13117.755| N/A|   3,278|
| |Armstrong County|     0|  0.000| N/A|     8|  4239.534| N/A|   1,887|
| |Motley County|     0|  0.000| N/A|     4|  3333.333| N/A|   1,200|
| |Knox County|     0|  0.000| N/A|    46| 12554.585| N/A|   3,664|
| |Shackelford County|     0|  0.000| N/A|    17|  5206.738| N/A|   3,265|
| |Borden County|     0|  0.000| N/A|     0|     0.000| N/A|     654|
| |San Saba County|     0|  0.000| N/A|    22|  3633.361| N/A|   6,055|
| |Roberts County|     0|  0.000| N/A|     7|  8196.721| N/A|     854|
| |Refugio County|     0|  0.000| N/A|   209| 30080.599| N/A|   6,948|
| |Real County|     0|  0.000| N/A|    76| 22016.222| N/A|   3,452|
| |Presidio County|     0|  0.000| N/A|    44|  6563.246| N/A|   6,704|
| |Mitchell County|     0|  0.000| N/A|    52|  6085.430| N/A|   8,545|
| |Mills County|     0|  0.000| N/A|    15|  3078.186| N/A|   4,873|
| |Menard County|     0|  0.000| N/A|    16|  7483.630| N/A|   2,138|
| |Mason County|     0|  0.000| N/A|    40|  9358.914| N/A|   4,274|
| |McMullen County|     0|  0.000| N/A|     8| 10767.160| N/A|     743|
| |Loving County|     0|  0.000| N/A|     0|     0.000| N/A|     169|
| |Sherman County|     0|  0.000| N/A|    37| 12243.547| N/A|   3,022|
| |Somervell County|     0|  0.000| N/A|    58|  6354.075| N/A|   9,128|
| |Archer County|     0|  0.000| N/A|    20|  2338.361| N/A|   8,553|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,393| 640.141| N/A|87,912|  8802.769| N/A|9,986,857|
| |Wayne County| 2,805| 1603.459|  0.565|27,377| 15649.875| 57.061|1,749,343|
| |Oakland County| 1,126| 895.368|  0.000|14,861| 11817.103| 85.084|1,257,584|
| |Macomb County|   936| 1070.973|  0.000| 9,722| 11123.926| 96.473| 873,972|
| |Genesee County|   294| 724.472|  0.000| 3,522|  8678.874| 45.191| 405,813|
| |Kent County|   154| 234.415|  0.000| 7,233| 11009.887| 94.514| 656,955|
| |Saginaw County|   129| 677.027|  0.000| 1,855|  9735.540| 53.534| 190,539|
| |Washtenaw County|   112| 304.678|  0.000| 2,414|  6566.903| 39.445| 367,601|
| |Kalamazoo County|    82| 309.357|  2.170| 1,560|  5885.327| 41.534| 265,066|
| |Berrien County|    65| 423.726|  1.023| 1,292|  8422.370| 39.394| 153,401|
| |Muskegon County|    58| 334.167|  0.904| 1,127|  6493.207| 14.563| 173,566|
| |Ottawa County|    54| 185.039|  0.000| 1,746|  5982.935| 81.461| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   778|  4889.146| 41.049| 159,128|
| |Calhoun County|    42| 313.061|  1.169|   749|  5582.928| 44.723| 134,159|
| |Ingham County|    34| 116.277| 13.680| 1,493|  5105.914| 38.626| 292,406|
| |Jackson County|    33| 208.189|  0.000|   690|  4353.038| 35.866| 158,510|
| |Lapeer County|    32| 365.268|  0.000|   421|  4805.552| 58.188|  87,607|
| |Bay County|    31| 300.603|  0.000|   550|  5333.282| 37.354| 103,126|
| |Tuscola County|    28| 535.936| 19.141|   310|  5933.582| 60.417|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   329|  4829.570| 29.359|  68,122|
| |Livingston County|    28| 145.837|  0.000|   784|  4083.440| 40.422| 191,995|
| |Hillsdale County|    25| 548.186|  0.000|   251|  5503.782| 23.589|  45,605|
| |Monroe County|    22| 146.179|  0.000|   904|  6006.645| 99.668| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   145|  3561.691| 14.086|  40,711|
| |Alpena County|    13| 457.666|  0.000|   125|  4400.634|  0.000|  28,405|
| |Clinton County|    13| 163.327|  0.000|   414|  5201.332| 31.328|  79,595|
| |Iosco County|    12| 477.574|  0.000|   129|  5133.920|  0.000|  25,127|
| |Lenawee County|    12| 121.888|  0.000|   402|  4083.250| 54.616|  98,451|
| |Van Buren County|    11| 145.355|  0.000|   414|  5470.619| 87.030|  75,677|
| |Marquette County|    11| 164.920|  0.000|   138|  2068.997| 46.292|  66,699|
| |Cass County|    10| 193.099|  3.029|   292|  5638.481| 34.158|  51,787|
| |Otsego County|    10| 405.383|  0.000|   131|  5310.524|  0.000|  24,668|
| |Midland County|    10| 120.256|  5.653|   311|  3739.959| 78.166|  83,156|
| |Isabella County|     9| 128.807| N/A|   201|  2876.689| N/A|  69,872|
| |Eaton County|     8| 72.551| N/A|   456|  4135.379| N/A| 110,268|
| |St. Joseph County|     7| 114.822| N/A|   561|  9202.152| N/A|  60,964|
| |Allegan County|     7| 59.281| N/A|   507|  4293.663| N/A| 118,081|
| |Oceana County|     6| 226.697| N/A|   467| 17644.614| N/A|  26,467|
| |Sanilac County|     6| 145.737| N/A|    97|  2356.085| N/A|  41,170|
| |Crawford County|     5| 356.405| N/A|    97|  6914.249| N/A|  14,029|
| |Grand Traverse County|     5| 53.713| N/A|   202|  2169.990| N/A|  93,088|
| |Ionia County|     5| 77.283| N/A|   266|  4111.473| N/A|  64,697|
| |Huron County|     4| 129.111| N/A|   146|  4712.566| N/A|  30,981|
| |Kalkaska County|     4| 221.754| N/A|    48|  2661.049| N/A|  18,038|
| |Wexford County|     4| 118.938| N/A|    66|  1962.475| N/A|  33,631|
| |Clare County|     3| 96.931| N/A|    61|  1970.921| N/A|  30,950|
| |Delta County|     3| 83.836| N/A|    81|  2263.581| N/A|  35,784|
| |Arenac County|     3| 201.572| N/A|    41|  2754.821| N/A|  14,883|
| |Mecosta County|     2| 46.027| N/A|    57|  1311.762| N/A|  43,453|
| |Charlevoix County|     2| 76.502| N/A|    44|  1683.051| N/A|  26,143|
| |Barry County|     2| 32.494| N/A|   172|  2794.476| N/A|  61,550|
| |Cheboygan County|     2| 79.126| N/A|    38|  1503.402| N/A|  25,276|
| |Dickinson County|     2| 79.242| N/A|    46|  1822.576| N/A|  25,239|
| |Emmet County|     2| 59.853| N/A|    58|  1735.747| N/A|  33,415|
| |Ogemaw County|     2| 95.252| N/A|    51|  2428.918| N/A|  20,997|
| |Gladwin County|     2| 78.589| N/A|    53|  2082.597| N/A|  25,449|
| |Branch County|     2| 45.959| N/A|   330|  7583.243| N/A|  43,517|
| |Iron County|     1| 90.367| N/A|    17|  1536.237| N/A|  11,066|
| |Gogebic County|     1| 71.556| N/A|    99|  7084.079| N/A|  13,975|
| |Benzie County|     1| 56.287| N/A|    28|  1576.044| N/A|  17,766|
| |Alcona County|     1| 96.108| N/A|    28|  2691.014| N/A|  10,405|
| |Missaukee County|     1| 66.146| N/A|    40|  2645.853| N/A|  15,118|
| |Montcalm County|     1| 15.652| N/A|   181|  2833.083| N/A|  63,888|
| |Presque Isle County|     1| 79.416| N/A|    17|  1350.064| N/A|  12,592|
| |Oscoda County|     1| 121.344| N/A|    24|  2912.268| N/A|   8,241|
| |Ontonagon County|     0|  0.000| N/A|     5|   874.126| N/A|   5,720|
| |Roscommon County|     0|  0.000| N/A|    48|  1998.418| N/A|  24,019|
| |Schoolcraft County|     0|  0.000| N/A|    12|  1482.580| N/A|   8,094|
| |Alger County|     0|  0.000| N/A|     9|   988.142| N/A|   9,108|
| |Newaygo County|     0|  0.000| N/A|   247|  5042.875| N/A|  48,980|
| |Lake County|     0|  0.000| N/A|    18|  1518.603| N/A|  11,853|
| |Montmorency County|     0|  0.000| N/A|     8|   857.633| N/A|   9,328|
| |Antrim County|     0|  0.000| N/A|    38|  1629.223| N/A|  23,324|
| |Menominee County|     0|  0.000| N/A|   100|  4389.816| N/A|  22,780|
| |Mason County|     0|  0.000| N/A|    97|  3328.301| N/A|  29,144|
| |Manistee County|     0|  0.000| N/A|    34|  1384.478| N/A|  24,558|
| |Mackinac County|     0|  0.000| N/A|    20|  1852.023| N/A|  10,799|
| |Luce County|     0|  0.000| N/A|     3|   481.618| N/A|   6,229|
| |Leelanau County|     0|  0.000| N/A|    66|  3032.949| N/A|  21,761|
| |Keweenaw County|     0|  0.000| N/A|     3|  1417.769| N/A|   2,116|
| |Osceola County|     0|  0.000| N/A|    70|  2983.802| N/A|  23,460|
| |Houghton County|     0|  0.000| N/A|    48|  1345.141| N/A|  35,684|
| |Chippewa County|     0|  0.000| N/A|    32|   856.783| N/A|  37,349|
| |Baraga County|     0|  0.000| N/A|     5|   609.088| N/A|   8,209|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,437| 1244.500| N/A|49,819| 13973.349| N/A|3,565,287|
| |Hartford County| 1,412| 1583.457|  0.000|12,701| 14243.260| 31.400| 891,720|
| |Fairfield County| 1,408| 1492.582|  0.878|17,870| 18943.490|  0.000| 943,332|
| |New Haven County| 1,104| 1291.595|  1.482|13,086| 15309.614| 21.960| 854,757|
| |Middlesex County|   191| 1175.848|  0.000| 1,388|  8544.904|  0.000| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,598|  8861.384|  0.000| 180,333|
| |New London County|   103| 388.377|  0.000| 1,414|  5331.704| 22.624| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,050|  6966.514|  0.000| 150,721|
| |Windham County|    15| 128.444|  0.000|   712|  6096.830|  0.000| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 3,910| 841.078| N/A|120,835| 25992.763| N/A|4,648,794|
| |Orleans Parish|   560| 1435.367|  0.000|10,426| 26723.466| 212.479| 390,144|
| |Jefferson Parish|   518| 1197.707|  0.000|14,533| 33602.856| 437.001| 432,493|
| |East Baton Rouge Parish|   328| 745.355|  1.916|11,263| 25594.295|  0.000| 440,059|
| |Caddo Parish|   281| 1169.839|  5.236| 6,299| 26223.543| 322.642| 240,204|
| |St. Tammany Parish|   203| 779.513|  3.155| 4,808| 18462.555| 233.185| 260,419|
| |Calcasieu Parish|   127| 624.275| 13.864| 6,527| 32083.800| 611.986| 203,436|
| |Rapides Parish|   106| 817.598| 12.959| 3,068| 23664.075| 308.856| 129,648|
| |Ouachita Parish|   105| 685.025|  0.000| 4,509| 29416.946| 343.190| 153,279|
| |Lafourche Parish|    96| 983.465|  0.000| 2,589| 26522.835| 288.967|  97,614|
| |St. John the Baptist Parish|    88| 2054.299|  0.000| 1,355| 31631.533| 163.410|  42,837|
| |Lafayette Parish|    87| 355.988|  5.170| 6,423| 26281.763| 533.371| 244,390|
| |Terrebonne Parish|    78| 706.132| 17.023| 2,800| 25348.313| 391.170| 110,461|
| |Acadia Parish|    77| 1241.035| 40.822| 2,403| 38729.954| 580.224|  62,045|
| |St. Landry Parish|    75| 913.253| 12.177| 2,226| 27105.353| 523.598|  82,124|
| |Bossier Parish|    73| 574.627| 16.702| 2,118| 16672.046| 251.891| 127,039|
| |Ascension Parish|    71| 560.804| 23.696| 2,643| 20876.118| 465.366| 126,604|
| |Iberia Parish|    65| 930.832| 18.037| 2,247| 32178.147| 415.294|  69,830|
| |Tangipahoa Parish|    63| 467.505|  3.153| 3,159| 23442.022| 452.663| 134,758|
| |Washington Parish|    58| 1255.574|  0.000| 1,199| 25955.752| 226.591|  46,194|
| |St. Charles Parish|    50| 941.620|  0.000| 1,375| 25894.539| 275.078|  53,100|
| |St. Mary Parish|    49| 992.948|  0.000| 1,445| 29281.835| 511.366|  49,348|
| |Livingston Parish|    49| 348.039|  3.034| 2,680| 19035.578| 267.915| 140,789|
| |Iberville Parish|    47| 1445.665|  0.000| 1,152| 35434.161| 430.623|  32,511|
| |St. Martin Parish|    42| 786.061|  0.000| 1,519| 28429.189| 477.251|  53,431|
| |West Baton Rouge Parish|    36| 1360.287|  0.000|   661| 24976.384| 571.879|  26,465|
| |East Feliciana Parish|    35| 1829.109|  0.000|   522| 27279.854| 713.371|  19,135|
| |Union Parish|    33| 1492.672| 19.322|   623| 28179.844| 519.656|  22,108|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   739| 34008.283| 598.251|  21,730|
| |St. James Parish|    31| 1469.473|  0.000|   649| 30764.126|  0.000|  21,096|
| |Bienville Parish|    30| 2265.690|  0.000|   353| 26659.618| 159.346|  13,241|
| |Avoyelles Parish|    27| 672.579| 10.543|   951| 23689.717| 357.749|  40,144|
| |Lincoln Parish|    24| 513.457|  9.054|   720| 15403.705| 226.030|  46,742|
| |De Soto Parish|    24| 873.903|  0.000|   662| 24105.160| 340.504|  27,463|
| |Jefferson Davis Parish|    24| 765.111|  0.000|   963| 30700.077| 255.525|  31,368|
| |St. Bernard Parish|    23| 486.834|  0.000| 1,037| 21949.877|  0.000|  47,244|
| |Allen Parish|    23| 897.491| 73.374| 1,156| 45108.674| 1555.909|  25,627|
| |Vernon Parish|    22| 463.851|  8.927|   704| 14843.239| 329.114|  47,429|
| |Assumption Parish|    20| 913.617|  0.000|   555| 25352.885| 297.357|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   425| 18321.335|  0.000|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   359| 22802.337| 127.033|  15,744|
| |Franklin Parish|    17| 849.363| 23.487|   839| 41918.561| 870.056|  20,015|
| |Beauregard Parish|    17| 453.370| 34.176|   789| 21041.683| 613.382|  37,497|
| |Vermilion Parish|    17| 285.661|  0.000| 1,378| 23155.383| 1269.751|  59,511|
| |Natchitoches Parish|    17| 445.516|  0.000|   691| 18108.916| 309.717|  38,158|
| |West Feliciana Parish|    16| 1027.749|  0.000|   326| 20940.391| 104.430|  15,568|
| |Webster Parish|    13| 339.071|  0.000|   826| 21544.079| 165.376|  38,340|
| |Morehouse Parish|    11| 442.229|  0.000|   443| 17809.761| 188.831|  24,874|
| |Red River Parish|    11| 1303.009| 55.684|   189| 22388.060|  0.000|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   221| 14103.382| 134.646|  15,670|
| |Sabine Parish|    10| 418.690| 41.869|   535| 22399.933| 299.392|  23,884|
| |Grant Parish|     9| 401.983| N/A|   282| 12595.471| N/A|  22,389|
| |Concordia Parish|     8| 415.390| N/A|   287| 14902.124| N/A|  19,259|
| |Winn Parish|     7| 503.452| N/A|   398| 28624.856| N/A|  13,904|
| |Madison Parish|     6| 547.895| N/A|   566| 51684.778| N/A|  10,951|
| |Richland Parish|     6| 298.181| N/A|   544| 27035.086| N/A|  20,122|
| |West Carroll Parish|     5| 461.681| N/A|   259| 23915.051| N/A|  10,830|
| |Catahoula Parish|     4| 421.319| N/A|   264| 27807.036| N/A|   9,494|
| |Caldwell Parish|     2| 201.654| N/A|   200| 20165.356| N/A|   9,918|
| |Evangeline Parish|     2| 59.889| N/A|   732| 21919.449| N/A|  33,395|
| |LaSalle Parish|     2| 134.300| N/A|   242| 16250.336| N/A|  14,892|
| |St. Helena Parish|     1| 98.697| N/A|   246| 24279.510| N/A|  10,132|
| |East Carroll Parish|     1| 145.751| N/A|   501| 73021.425| N/A|   6,861|
| |Tensas Parish|     0|  0.000| N/A|    65| 14997.693| N/A|   4,334|
| |Cameron Parish|     0|  0.000| N/A|   167| 23949.520| N/A|   6,973|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 3,778| 519.048| N/A|179,497| 24660.527| N/A|7,278,717|
| |Maricopa County| 2,108| 469.968|  1.561|120,960| 26967.410| 234.734|4,485,414|
| |Pima County|   462| 441.143|  0.454|16,741| 15985.234| 82.118|1,047,279|
| |Yuma County|   263| 1230.196| 21.049|11,203| 52402.625| 419.397| 213,787|
| |Navajo County|   188| 1694.854|  4.508| 5,284| 47636.219| 185.405| 110,924|
| |Mohave County|   153| 721.082|  2.929| 3,040| 14327.390| 156.426| 212,181|
| |Pinal County|   141| 304.674|  2.382| 8,301| 17936.900| 159.900| 462,789|
| |Apache County|   136| 1891.858|  0.000| 3,084| 42900.664| 403.233|  71,887|
| |Coconino County|   116| 808.498|  0.000| 2,997| 20888.511| 118.487| 143,476|
| |Yavapai County|    62| 263.719|  4.254| 1,858|  7903.054| 170.141| 235,099|
| |Santa Cruz County|    50| 1075.315|  0.000| 2,610| 56131.447| 36.630|  46,498|
| |Cochise County|    50| 397.071|  4.578| 1,557| 12364.797| 135.004| 125,922|
| |Gila County|    29| 536.858|  0.000|   841| 15568.884| 185.805|  54,018|
| |La Paz County|    10| 473.754|  0.000|   474| 22455.941| 62.144|  21,108|
| |Graham County|     9| 231.738| N/A|   490| 12616.834| N/A|  38,837|
| |Greenlee County|     1| 105.285| N/A|    57|  6001.263| N/A|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 3,754| 353.570| N/A|176,961| 16667.039| N/A|10,617,423|
| |Fulton County|   398| 374.082|  1.852|18,224| 17128.834| 172.003|1,063,937|
| |Cobb County|   298| 392.033|  0.204|11,844| 15581.320| 268.371| 760,141|
| |Gwinnett County|   240| 256.342|  0.335|17,927| 19147.664| 253.496| 936,250|
| |DeKalb County|   225| 296.327|  0.974|12,604| 16599.565| 229.818| 759,297|
| |Dougherty County|   169| 1921.415| 11.369| 2,621| 29798.990| 185.228|  87,956|
| |Clayton County|   101| 345.587|  3.201| 4,557| 15592.494| 152.264| 292,256|
| |Richmond County|    83| 409.840|  6.102| 3,786| 18694.635| 495.739| 202,518|
| |Muscogee County|    82| 418.861|  0.801| 4,368| 22312.011| 296.268| 195,769|
| |Hall County|    79| 386.420|  1.976| 5,547| 27132.522| 226.960| 204,441|
| |Chatham County|    67| 231.489|  0.000| 5,051| 17451.543| 261.929| 289,430|
| |Troup County|    63| 901.004| 11.133| 2,175| 31106.090| 99.963|  69,922|
| |Bibb County|    61| 398.279|  2.048| 3,214| 20984.728| 350.103| 153,159|
| |Bartow County|    60| 556.907|  9.789| 1,618| 15017.914| 193.289| 107,738|
| |Sumter County|    56| 1896.762|  0.000|   732| 24793.388| 133.457|  29,524|
| |Cherokee County|    56| 216.406|  1.518| 2,885| 11148.767| 181.626| 258,773|
| |Douglas County|    49| 334.830|  1.065| 2,331| 15928.333| 177.665| 146,343|
| |Houston County|    49| 310.396|  0.000| 1,802| 11414.961| 177.369| 157,863|
| |Habersham County|    48| 1058.948|  0.000| 1,048| 23120.367| 242.676|  45,328|
| |Carroll County|    47| 391.693|  0.000| 1,756| 14634.309| 188.969| 119,992|
| |Upson County|    46| 1747.720|  5.960|   488| 18541.033| 175.755|  26,320|
| |Henry County|    42| 179.058|  4.263| 3,019| 12870.852| 158.966| 234,561|
| |Mitchell County|    41| 1875.314|  0.000|   617| 28221.196| 191.546|  21,863|
| |Thomas County|    39| 877.371|  0.000|   999| 22474.185| 309.113|  44,451|
| |Spalding County|    39| 584.681|  0.000|   868| 13012.908| 160.202|  66,703|
| |Baldwin County|    38| 846.514|  0.000|   972| 21652.929| 362.903|  44,890|
| |Butts County|    37| 1483.799|  0.000|   466| 18687.841| 60.154|  24,936|
| |Tift County|    35| 861.136|  3.860| 1,249| 30730.243| 165.902|  40,644|
| |Newton County|    35| 313.216|  6.849| 1,618| 14479.525| 243.096| 111,744|
| |Glynn County|    34| 398.631| 26.795| 2,330| 27317.920| 299.334|  85,292|
| |Hancock County|    34| 4020.338|  0.000|   283| 33463.403| 118.245|   8,457|
| |Walton County|    34| 359.435|  0.000|   969| 10243.887| 212.259|  94,593|
| |Lowndes County|    32| 272.558|  1.377| 2,985| 25424.595| 229.971| 117,406|
| |Barrow County|    32| 384.431|  0.000| 1,127| 13539.164| 258.735|  83,240|
| |Early County|    31| 3042.198|  0.000|   346| 33954.858|  0.000|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   292| 34228.109| 86.950|   8,531|
| |Whitfield County|    27| 258.057|  0.000| 3,232| 30890.393| 463.547| 104,628|
| |Randolph County|    26| 3835.940|  0.000|   261| 38506.934| 155.699|   6,778|
| |Coffee County|    25| 577.727|  3.603| 1,347| 31127.955| 316.595|  43,273|
| |Fayette County|    25| 218.491|  1.371|   980|  8564.861| 156.938| 114,421|
| |Worth County|    23| 1135.971|  0.000|   427| 21089.544| 148.170|  20,247|
| |Ware County|    23| 643.645|  0.000| 1,083| 30307.270| 251.534|  35,734|
| |Gordon County|    23| 396.805|  0.000| 1,026| 17700.947| 215.655|  57,963|
| |Monroe County|    23| 833.998|  0.000|   428| 15519.617| 217.565|  27,578|
| |Colquitt County|    22| 482.456|  3.440| 1,481| 32478.070| 87.719|  45,600|
| |Lee County|    22| 733.529|  0.000|   520| 17337.957| 221.151|  29,992|
| |Jenkins County|    22| 2535.731|  0.000|   230| 26509.912| 111.371|   8,676|
| |Coweta County|    21| 141.406|  2.113| 1,359|  9150.961| 148.686| 148,509|
| |Forsyth County|    20| 81.883|  1.749| 1,942|  7950.805| 100.217| 244,252|
| |Paulding County|    19| 112.648|  0.000| 1,452|  8608.679| 156.572| 168,667|
| |Columbia County|    19| 121.240|  0.000| 1,969| 12564.289| 381.298| 156,714|
| |Turner County|    18| 2254.227|  0.000|   227| 28428.303| 250.470|   7,985|
| |Wilcox County|    18| 2084.540|  0.000|   167| 19339.896| 202.377|   8,635|
| |Putnam County|    17| 768.570|  0.000|   384| 17360.640| 156.883|  22,119|
| |Clarke County|    17| 132.470|  0.000| 1,741| 13566.480| 187.016| 128,331|
| |Harris County|    16| 454.081|  4.452|   624| 17709.161| 142.417|  35,236|
| |Rockdale County|    16| 176.025|  1.726| 1,176| 12937.863| 166.801|  90,896|
| |Appling County|    16| 870.227|  0.000|   602| 32742.304| 435.114|  18,386|
| |Walker County|    16| 229.355|  4.497|   556|  7970.069| 56.764|  69,761|
| |Floyd County|    15| 152.287|  0.000| 1,283| 13025.645| 233.503|  98,498|
| |Brooks County|    15| 970.434|  0.000|   374| 24196.157| 181.671|  15,457|
| |Oconee County|    15| 372.393|  0.000|   396|  9831.182| 223.436|  40,280|
| |Crisp County|    14| 625.782|  0.000|   363| 16225.639| 59.223|  22,372|
| |Dooly County|    14| 1045.556|  0.000|   242| 18073.189| 54.717|  13,390|
| |Jackson County|    13| 178.138|  0.000|   958| 13127.424| 180.633|  72,977|
| |Bulloch County|    12| 150.739|  0.000| 1,112| 13968.445| 228.922|  79,608|
| |Peach County|    12| 435.635|  0.000|   334| 12125.172| 290.423|  27,546|
| |Greene County|    11| 600.306|  0.000|   254| 13861.602| 327.439|  18,324|
| |Johnson County|    10| 1037.022|  0.000|   227| 23540.392| 311.107|   9,643|
| |Macon County|    10| 772.380|  0.000|   175| 13516.645| 69.173|  12,947|
| |Stephens County|    10| 385.728|  0.000|   561| 21639.344| 259.061|  25,925|
| |Wilkinson County|    10| 1116.819|  0.000|   185| 20661.157| 439.518|   8,954|
| |Catoosa County|     9| 133.175| N/A|   546|  8079.313| N/A|  67,580|
| |Lamar County|     9| 471.772| N/A|   237| 12423.337| N/A|  19,077|
| |Screven County|     9| 644.422| N/A|   175| 12530.431| N/A|  13,966|
| |Polk County|     9| 211.203| N/A|   682| 16004.506| N/A|  42,613|
| |McDuffie County|     9| 422.297| N/A|   296| 13888.889| N/A|  21,312|
| |Decatur County|     8| 302.984| N/A|   677| 25640.055| N/A|  26,404|
| |Burke County|     7| 312.737| N/A|   415| 18540.857| N/A|  22,383|
| |Telfair County|     7| 441.362| N/A|   254| 16015.132| N/A|  15,860|
| |Bryan County|     7| 176.647| N/A|   566| 14283.191| N/A|  39,627|
| |Oglethorpe County|     7| 458.746| N/A|   189| 12386.133| N/A|  15,259|
| |Emanuel County|     7| 309.105| N/A|   426| 18811.269| N/A|  22,646|
| |Cook County|     6| 347.423| N/A|   405| 23451.071| N/A|  17,270|
| |Lumpkin County|     6| 178.518| N/A|   302|  8985.421| N/A|  33,610|
| |Union County|     6| 244.788| N/A|   227|  9261.148| N/A|  24,511|
| |Haralson County|     6| 201.396| N/A|   196|  6578.947| N/A|  29,792|
| |Toombs County|     6| 223.630| N/A|   649| 24189.340| N/A|  26,830|
| |Bacon County|     6| 537.442| N/A|   415| 37173.056| N/A|  11,164|
| |Jeff Davis County|     6| 396.957| N/A|   404| 26728.415| N/A|  15,115|
| |Jefferson County|     6| 390.574| N/A|   449| 29227.965| N/A|  15,362|
| |Pierce County|     6| 308.246| N/A|   380| 19522.219| N/A|  19,465|
| |Calhoun County|     6| 969.462| N/A|   194| 31345.936| N/A|   6,189|
| |Pickens County|     5| 153.417| N/A|   295|  9051.579| N/A|  32,591|
| |Stewart County|     5| 755.173| N/A|   250| 37758.647| N/A|   6,621|
| |White County|     5| 162.348| N/A|   302|  9805.832| N/A|  30,798|
| |Meriwether County|     5| 236.217| N/A|   358| 16913.119| N/A|  21,167|
| |Grady County|     5| 202.980| N/A|   419| 17009.702| N/A|  24,633|
| |Madison County|     4| 133.869| N/A|   341| 11412.316| N/A|  29,880|
| |Pike County|     4| 210.948| N/A|   195| 10283.725| N/A|  18,962|
| |Lanier County|     4| 383.767| N/A|   215| 20627.459| N/A|  10,423|
| |Marion County|     4| 478.526| N/A|   145| 17346.573| N/A|   8,359|
| |Franklin County|     4| 171.314| N/A|   375| 16060.645| N/A|  23,349|
| |Lincoln County|     4| 504.987| N/A|   129| 16285.822| N/A|   7,921|
| |Wayne County|     4| 133.659| N/A|   630| 21051.225| N/A|  29,927|
| |Brantley County|     4| 209.325| N/A|   228| 11931.551| N/A|  19,109|
| |Clinch County|     4| 604.412| N/A|   176| 26594.137| N/A|   6,618|
| |Laurens County|     4| 84.129| N/A|   762| 16026.585| N/A|  47,546|
| |Candler County|     4| 370.268| N/A|   229| 21197.815| N/A|  10,803|
| |Camden County|     4| 73.172| N/A|   689| 12603.812| N/A|  54,666|
| |Dodge County|     3| 145.596| N/A|   189|  9172.531| N/A|  20,605|
| |Charlton County|     3| 224.014| N/A|   389| 29047.192| N/A|  13,392|
| |Jones County|     3| 104.402| N/A|   270|  9396.207| N/A|  28,735|
| |Gilmer County|     3| 95.636| N/A|   518| 16513.118| N/A|  31,369|
| |Bleckley County|     3| 233.046| N/A|   133| 10331.702| N/A|  12,873|
| |Ben Hill County|     3| 179.641| N/A|   351| 21017.964| N/A|  16,700|
| |Banks County|     3| 155.974| N/A|   244| 12685.869| N/A|  19,234|
| |Baker County|     3| 987.492| N/A|    58| 19091.508| N/A|   3,038|
| |Heard County|     3| 251.615| N/A|   131| 10987.168| N/A|  11,923|
| |Talbot County|     3| 484.262| N/A|   128| 20661.824| N/A|   6,195|
| |Rabun County|     3| 175.060| N/A|   193| 11262.181| N/A|  17,137|
| |Dawson County|     3| 114.907| N/A|   301| 11529.033| N/A|  26,108|
| |Twiggs County|     3| 369.458| N/A|    94| 11576.355| N/A|   8,120|
| |Treutlen County|     3| 434.720| N/A|   100| 14490.654| N/A|   6,901|
| |Wilkes County|     3| 306.843| N/A|   179| 18308.275| N/A|   9,777|
| |Echols County|     2| 499.251| N/A|   218| 54418.372| N/A|   4,006|
| |Seminole County|     2| 247.219| N/A|   145| 17923.362| N/A|   8,090|
| |Clay County|     2| 705.716| N/A|    80| 28228.652| N/A|   2,834|
| |Chattooga County|     2| 80.681| N/A|   198|  7987.414| N/A|  24,789|
| |Atkinson County|     2| 244.948| N/A|   296| 36252.296| N/A|   8,165|
| |Pulaski County|     2| 179.582| N/A|    88|  7901.589| N/A|  11,137|
| |Murray County|     2| 49.880| N/A|   538| 13417.797| N/A|  40,096|
| |McIntosh County|     2| 139.101| N/A|   157| 10919.460| N/A|  14,378|
| |Hart County|     2| 76.321| N/A|   269| 10265.217| N/A|  26,205|
| |Taylor County|     2| 249.377| N/A|    71|  8852.868| N/A|   8,020|
| |Liberty County|     2| 32.555| N/A|   624| 10157.077| N/A|  61,435|
| |Fannin County|     2| 76.371| N/A|   284| 10844.662| N/A|  26,188|
| |Webster County|     2| 767.165| N/A|    37| 14192.558| N/A|   2,607|
| |Washington County|     2| 98.164| N/A|   427| 20958.084| N/A|  20,374|
| |Towns County|     1| 83.077| N/A|   119|  9886.184| N/A|  12,037|
| |Wheeler County|     1| 127.307| N/A|    84| 10693.826| N/A|   7,855|
| |Warren County|     1| 190.331| N/A|    55| 10468.215| N/A|   5,254|
| |Schley County|     1| 190.223| N/A|    55| 10462.241| N/A|   5,257|
| |Montgomery County|     1| 109.027| N/A|   138| 15045.792| N/A|   9,172|
| |Tattnall County|     1| 39.548| N/A|   425| 16807.720| N/A|  25,286|
| |Quitman County|     1| 434.972| N/A|    29| 12614.180| N/A|   2,299|
| |Long County|     1| 51.127| N/A|   124|  6339.792| N/A|  19,559|
| |Effingham County|     1| 15.553| N/A|   651| 10125.047| N/A|  64,296|
| |Elbert County|     1| 52.100| N/A|   324| 16880.275| N/A|  19,194|
| |Evans County|     1| 93.861| N/A|   227| 21306.552| N/A|  10,654|
| |Chattahoochee County|     1| 91.684| N/A|   665| 60970.019| N/A|  10,907|
| |Dade County|     1| 62.050| N/A|   111|  6887.565| N/A|  16,116|
| |Jasper County|     1| 70.328| N/A|   126|  8861.383| N/A|  14,219|
| |Irwin County|     1| 106.202| N/A|   157| 16673.747| N/A|   9,416|
| |Miller County|     0|  0.000| N/A|   129| 22560.336| N/A|   5,718|
| |Taliaferro County|     0|  0.000| N/A|    13|  8458.035| N/A|   1,537|
| |Morgan County|     0|  0.000| N/A|   226| 11724.424| N/A|  19,276|
| |Glascock County|     0|  0.000| N/A|    23|  7741.501| N/A|   2,971|
| |Crawford County|     0|  0.000| N/A|    89|  7175.105| N/A|  12,404|
| |Berrien County|     0|  0.000| N/A|   263| 13558.798| N/A|  19,397|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,539| 302.761| N/A|93,963|  8038.515| N/A|11,689,100|
| |Franklin County|   514| 390.353|  0.560|17,254| 13103.415| 83.539|1,316,756|
| |Cuyahoga County|   477| 386.212|  1.348|12,753| 10325.714| 95.136|1,235,072|
| |Lucas County|   318| 742.387|  2.721| 4,944| 11542.017| 212.444| 428,348|
| |Mahoning County|   253| 1106.335|  3.190| 2,411| 10542.979| 59.752| 228,683|
| |Hamilton County|   248| 303.374|  1.223| 9,160| 11205.263| 71.335| 817,473|
| |Summit County|   217| 401.099|  0.000| 3,294|  6088.578| 75.784| 541,013|
| |Stark County|   132| 356.173|  0.436| 1,690|  4560.099| 40.680| 370,606|
| |Trumbull County|   103| 520.270|  0.000| 1,433|  7238.324| 75.768| 197,974|
| |Montgomery County|    78| 146.703|  3.722| 4,057|  7630.429| 81.815| 531,687|
| |Lorain County|    76| 245.293|  0.000| 1,634|  5273.809| 57.692| 309,833|
| |Portage County|    60| 369.308|  0.000|   717|  4413.231| 27.379| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,582| 15527.615| 80.178| 101,883|
| |Butler County|    59| 153.993|  0.000| 2,714|  7083.684| 86.132| 383,134|
| |Wayne County|    58| 501.253|  0.000|   499|  4312.505| 48.211| 115,710|
| |Wood County|    58| 443.367|  0.000|   924|  7063.302| 114.664| 130,817|
| |Ashtabula County|    45| 462.768|  0.000|   539|  5542.929| 13.925|  97,241|
| |Marion County|    44| 675.956|  0.000| 2,884| 44305.839| 126.755|  65,093|
| |Geauga County|    43| 459.161|  0.000|   531|  5670.109| 42.222|  93,649|
| |Licking County|    43| 243.127|  5.654| 1,125|  6360.892| 85.438| 176,862|
| |Pickaway County|    42| 718.477|  0.000| 2,357| 40320.235| 72.713|  58,457|
| |Allen County|    42| 410.353|  0.000|   654|  6389.776| 92.164| 102,351|
| |Miami County|    37| 345.836|  0.000|   769|  7187.789| 50.616| 106,987|
| |Lake County|    36| 156.420|  3.667| 1,043|  4531.847| 45.732| 230,149|
| |Warren County|    35| 149.189|  0.000| 1,634|  6964.988| 117.314| 234,602|
| |Medina County|    33| 183.592|  0.000|   835|  4645.444| 38.944| 179,746|
| |Erie County|    27| 363.558|  2.112|   524|  7055.719| 114.453|  74,266|
| |Darke County|    27| 528.241|  0.000|   321|  6280.203| 78.890|  51,113|
| |Belmont County|    26| 388.025|  0.000|   589|  8790.258|  0.000|  67,006|
| |Fairfield County|    25| 158.656|  8.133| 1,254|  7958.166| 82.501| 157,574|
| |Ottawa County|    25| 616.903|  0.000|   359|  8858.729| 154.455|  40,525|
| |Washington County|    22| 367.211|  7.130|   197|  3288.211| 21.223|  59,911|
| |Delaware County|    18| 86.052|  0.000| 1,206|  5765.452| 62.148| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    91|  6664.714| 73.239|  13,654|
| |Putnam County|    17| 502.053|  0.000|   192|  5670.240| 18.557|  33,861|
| |Sandusky County|    17| 290.509|  0.000|   332|  5673.468| 111.077|  58,518|
| |Mercer County|    13| 315.749|  0.000|   535| 12994.268| 301.602|  41,172|
| |Tuscarawas County|    13| 141.324|  0.000|   747|  8120.713| 30.649|  91,987|
| |Clark County|    13| 96.955|  0.000| 1,086|  8099.461| 70.236| 134,083|
| |Richland County|    12| 99.047|  0.000|   540|  4457.137| 37.143| 121,154|
| |Hardin County|    12| 382.592|  0.000|   150|  4782.401|  4.972|  31,365|
| |Clermont County|    11| 53.287|  4.844|   855|  4141.880| 92.042| 206,428|
| |Greene County|    11| 65.113|  0.000|   626|  3705.523| 29.035| 168,937|
| |Madison County|    10| 223.559|  0.000|   333|  7444.502| 135.143|  44,731|
| |Hocking County|     9| 318.426| N/A|   111|  3927.257| N/A|  28,264|
| |Wyandot County|     7| 321.514| N/A|   120|  5511.666| N/A|  21,772|
| |Guernsey County|     7| 180.064| N/A|   111|  2855.305| N/A|  38,875|
| |Holmes County|     6| 136.488| N/A|   322|  7324.841| N/A|  43,960|
| |Coshocton County|     6| 163.934| N/A|   186|  5081.967| N/A|  36,600|
| |Clinton County|     6| 142.966| N/A|   148|  3526.496| N/A|  41,968|
| |Crawford County|     5| 120.499| N/A|   168|  4048.778| N/A|  41,494|
| |Auglaize County|     5| 109.515| N/A|   222|  4862.450| N/A|  45,656|
| |Carroll County|     5| 185.777| N/A|   108|  4012.781| N/A|  26,914|
| |Shelby County|     4| 82.321| N/A|   160|  3292.859| N/A|  48,590|
| |Ross County|     4| 52.174| N/A|   401|  5230.480| N/A|  76,666|
| |Defiance County|     4| 105.023| N/A|   129|  3386.982| N/A|  38,087|
| |Huron County|     4| 68.651| N/A|   376|  6453.163| N/A|  58,266|
| |Seneca County|     3| 54.369| N/A|   161|  2917.830| N/A|  55,178|
| |Williams County|     3| 81.762| N/A|   124|  3379.483| N/A|  36,692|
| |Jefferson County|     3| 45.924| N/A|   206|  3153.463| N/A|  65,325|
| |Ashland County|     3| 56.092| N/A|   133|  2486.725| N/A|  53,484|
| |Vinton County|     2| 152.847| N/A|    30|  2292.702| N/A|  13,085|
| |Knox County|     2| 32.091| N/A|   169|  2711.723| N/A|  62,322|
| |Morrow County|     2| 56.612| N/A|   158|  4472.373| N/A|  35,328|
| |Adams County|     2| 72.207| N/A|    53|  1913.496| N/A|  27,698|
| |Hancock County|     2| 26.391| N/A|   320|  4222.583| N/A|  75,783|
| |Perry County|     2| 55.350| N/A|   106|  2933.525| N/A|  36,134|
| |Preble County|     2| 48.921| N/A|   166|  4060.467| N/A|  40,882|
| |Gallia County|     1| 33.447| N/A|    58|  1939.929| N/A|  29,898|
| |Muskingum County|     1| 11.599| N/A|   181|  2099.403| N/A|  86,215|
| |Fulton County|     1| 23.738| N/A|   140|  3323.363| N/A|  42,126|
| |Scioto County|     1| 13.278| N/A|   188|  2496.216| N/A|  75,314|
| |Van Wert County|     1| 35.367| N/A|    69|  2440.318| N/A|  28,275|
| |Union County|     1| 16.953| N/A|   216|  3661.762| N/A|  58,988|
| |Champaign County|     1| 25.717| N/A|   138|  3548.926| N/A|  38,885|
| |Athens County|     1| 15.308| N/A|   345|  5281.124| N/A|  65,327|
| |Brown County|     1| 23.024| N/A|   112|  2578.744| N/A|  43,432|
| |Harrison County|     1| 66.489| N/A|    20|  1329.787| N/A|  15,040|
| |Henry County|     1| 37.029| N/A|   106|  3925.054| N/A|  27,006|
| |Logan County|     1| 21.895| N/A|   123|  2693.116| N/A|  45,672|
| |Highland County|     1| 23.169| N/A|   132|  3058.317| N/A|  43,161|
| |Fayette County|     0|  0.000| N/A|    97|  3400.526| N/A|  28,525|
| |Jackson County|     0|  0.000| N/A|    67|  2067.072| N/A|  32,413|
| |Noble County|     0|  0.000| N/A|    17|  1178.591| N/A|  14,424|
| |Pike County|     0|  0.000| N/A|    66|  2376.494| N/A|  27,772|
| |Paulding County|     0|  0.000| N/A|    61|  3266.924| N/A|  18,672|
| |Morgan County|     0|  0.000| N/A|    20|  1378.550| N/A|  14,508|
| |Meigs County|     0|  0.000| N/A|    25|  1091.369| N/A|  22,907|
| |Lawrence County|     0|  0.000| N/A|   220|  3699.780| N/A|  59,463|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,504| 579.587| N/A|91,144| 15075.889| N/A|6,045,680|
| |Baltimore County|   964| 1165.138|  3.859|24,149| 29187.667| 455.111| 827,370|
| |Montgomery County|   793| 754.744|  1.592|17,842| 16981.254| 85.548|1,050,688|
| |Prince George's County|   743| 817.088|  1.653|22,880| 25161.466| 159.875| 909,327|
| |Anne Arundel County|   217| 374.633|  0.000| 7,007| 12097.011| 146.746| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,010| 11597.129| 40.774| 259,547|
| |Carroll County|   117| 694.580|  5.937| 1,491|  8851.449| 76.970| 168,447|
| |Howard County|   106| 325.463|  0.000| 3,660| 11237.680| 135.957| 325,690|
| |Charles County|    91| 557.403|  0.000| 1,909| 11693.220| 161.715| 163,257|
| |Harford County|    68| 266.206|  0.000| 1,853|  7254.121| 138.903| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   931|  8201.921| 118.932| 113,510|
| |Wicomico County|    44| 424.674|  0.000| 1,298| 12527.869| 57.012| 103,609|
| |Washington County|    30| 198.611|  0.000|   982|  6501.202| 99.306| 151,049|
| |Cecil County|    30| 291.673|  0.000|   655|  6368.188| 116.616| 102,855|
| |Calvert County|    28| 302.621|  0.000|   635|  6863.010| 169.693|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   399|  7919.652| 59.546|  50,381|
| |Kent County|    23| 1184.224|  0.000|   235| 12099.681| 38.921|  19,422|
| |Worcester County|    19| 363.456|  3.001|   611| 11687.964| 394.697|  52,276|
| |Allegany County|    18| 255.624|  0.000|   273|  3876.960| 38.307|  70,416|
| |Dorchester County|     5| 156.597| N/A|   352| 11024.461| N/A|  31,929|
| |Talbot County|     4| 107.582| N/A|   368|  9897.528| N/A|  37,181|
| |Caroline County|     3| 89.804| N/A|   438| 13111.417| N/A|  33,406|
| |Somerset County|     3| 117.114| N/A|   123|  4801.686| N/A|  25,616|
| |Baltimore city|     0|  0.000| N/A|     0|     0.000| N/A| 593,490|
| |Garrett County|     0|  0.000| N/A|    43|  1482.043| N/A|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,780| 412.940| N/A|68,433| 10164.999| N/A|6,732,219|
| |Marion County|   719| 745.401|  0.440|14,863| 15408.747| 147.732| 964,582|
| |Lake County|   271| 558.195|  2.420| 7,101| 14626.369| 111.782| 485,493|
| |Allen County|   158| 416.558|  1.110| 3,635|  9583.468| 105.836| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,652| 10444.657| 70.679| 158,167|
| |Hendricks County|   105| 616.519|  0.000| 1,750| 10275.320| 117.432| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,513|  7434.669| 99.109| 338,011|
| |St. Joseph County|    79| 290.627|  0.000| 3,154| 11603.011| 161.140| 271,826|
| |Elkhart County|    77| 373.169|  2.423| 4,597| 22278.655| 74.973| 206,341|
| |Howard County|    65| 787.459|  5.075|   810|  9812.948| 84.548|  82,544|
| |Madison County|    65| 501.663|  0.000|   847|  6537.057| 162.076| 129,569|
| |Delaware County|    52| 455.601|  0.000|   638|  5589.872| 56.178| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   743|  8868.571| 87.477|  83,779|
| |Boone County|    46| 678.036|  0.000|   635|  9359.846| 71.815|  67,843|
| |Clark County|    45| 380.382|  0.000| 1,081|  9137.631| 80.303| 118,302|
| |Floyd County|    44| 560.353|  0.000|   694|  8838.287| 184.662|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,195|  7013.364| 130.403| 170,389|
| |Hancock County|    37| 473.339|  0.000|   623|  7970.013| 103.043|  78,168|
| |Greene County|    34| 1065.096|  0.000|   239|  7487.000| 62.653|  31,922|
| |Morgan County|    32| 453.972|  0.000|   425|  6029.310| 81.625|  70,489|
| |Decatur County|    32| 1204.865|  0.000|   314| 11822.734| 124.614|  26,559|
| |Warrick County|    30| 476.206|  2.490|   516|  8190.736| 230.253|  62,998|
| |Monroe County|    30| 202.114|  0.000|   686|  4621.676| 47.773| 148,431|
| |LaPorte County|    29| 263.905|  0.000|   838|  7625.946| 103.506| 109,888|
| |Grant County|    29| 440.937|  0.000|   496|  7541.547|  8.975|  65,769|
| |Dearborn County|    28| 566.137|  0.000|   465|  9401.917| 105.612|  49,458|
| |Noble County|    28| 586.461|  0.000|   637| 13341.991| 137.651|  47,744|
| |Lawrence County|    27| 595.107|  0.000|   328|  7229.447| 76.780|  45,370|
| |Shelby County|    26| 581.278|  0.000|   511| 11424.356| 34.189|  44,729|
| |Orange County|    24| 1221.623|  0.000|   164|  8347.755| 87.420|  19,646|
| |Harrison County|    22| 543.009|  0.000|   294|  7256.572| 148.093|  40,515|
| |Marshall County|    22| 475.593|  0.000|   742| 16040.469| 51.708|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   343|  8946.737| 130.419|  38,338|
| |Daviess County|    19| 569.698|  0.000|   246|  7376.091| 98.540|  33,351|
| |Henry County|    18| 375.219|  0.000|   361|  7525.223| 41.691|  47,972|
| |Vanderburgh County|    12| 66.134|  0.000| 1,726|  9512.210| 187.656| 181,451|
| |Perry County|    12| 626.011|  0.000|   172|  8972.821| 52.168|  19,169|
| |Jennings County|    12| 432.666|  0.000|   210|  7571.660| 108.167|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   819| 10307.592| 65.476|  79,456|
| |Dubois County|    12| 280.794|  0.000|   626| 14648.072| 139.457|  42,736|
| |Tippecanoe County|    11| 56.199|  0.000| 1,103|  5635.256| 81.667| 195,732|
| |White County|    10| 414.903|  0.000|   347| 14397.145| 82.981|  24,102|
| |Vigo County|    10| 93.425|  0.000|   474|  4428.334| 126.090| 107,038|
| |Scott County|    10| 418.883|  0.000|   250| 10472.081| 114.598|  23,873|
| |LaGrange County|    10| 252.436|  0.000|   542| 13682.032| 75.731|  39,614|
| |Franklin County|    10| 439.406|  0.000|   224|  9842.693| 543.457|  22,758|
| |Newton County|    10| 715.103|  0.000|   110|  7866.133| 71.510|  13,984|
| |Wayne County|     9| 136.604| N/A|   317|  4811.487| N/A|  65,884|
| |Cass County|     9| 238.796| N/A| 1,751| 46459.179| N/A|  37,689|
| |Putnam County|     8| 212.902| N/A|   222|  5908.026| N/A|  37,576|
| |Starke County|     7| 304.414| N/A|   165|  7175.473| N/A|  22,995|
| |Ripley County|     7| 247.140| N/A|   188|  6637.481| N/A|  28,324|
| |Fayette County|     7| 303.004| N/A|   155|  6709.376| N/A|  23,102|
| |Whitley County|     6| 176.658| N/A|   148|  4357.555| N/A|  33,964|
| |Tipton County|     5| 330.077| N/A|   107|  7063.639| N/A|  15,148|
| |Clay County|     5| 190.658| N/A|    97|  3698.761| N/A|  26,225|
| |Ohio County|     4| 680.851| N/A|    51|  8680.851| N/A|   5,875|
| |Jackson County|     4| 90.434| N/A|   552| 12479.935| N/A|  44,231|
| |Rush County|     4| 241.240| N/A|    79|  4764.489| N/A|  16,581|
| |DeKalb County|     4| 92.007| N/A|   222|  5106.383| N/A|  43,475|
| |Gibson County|     4| 118.839| N/A|   200|  5941.947| N/A|  33,659|
| |Randolph County|     4| 162.173| N/A|   103|  4175.958| N/A|  24,665|
| |Clinton County|     3| 92.595| N/A|   357| 11018.859| N/A|  32,399|
| |Huntington County|     3| 82.147| N/A|   118|  3231.106| N/A|  36,520|
| |Steuben County|     3| 86.720| N/A|   200|  5781.349| N/A|  34,594|
| |Wabash County|     3| 96.787| N/A|   161|  5194.219| N/A|  30,996|
| |Spencer County|     3| 147.951| N/A|   114|  5622.133| N/A|  20,277|
| |Wells County|     2| 70.681| N/A|   134|  4735.652| N/A|  28,296|
| |Fountain County|     2| 122.354| N/A|    63|  3854.154| N/A|  16,346|
| |Fulton County|     2| 100.130| N/A|   146|  7309.502| N/A|  19,974|
| |Blackford County|     2| 170.097| N/A|    53|  4507.569| N/A|  11,758|
| |Adams County|     2| 55.902| N/A|    81|  2264.024| N/A|  35,777|
| |Carroll County|     2| 98.731| N/A|   145|  7158.019| N/A|  20,257|
| |Miami County|     2| 56.313| N/A|   258|  7264.332| N/A|  35,516|
| |Jefferson County|     2| 61.904| N/A|   149|  4611.861| N/A|  32,308|
| |Jasper County|     2| 59.591| N/A|   208|  6197.485| N/A|  33,562|
| |Owen County|     1| 48.079| N/A|    78|  3750.180| N/A|  20,799|
| |Parke County|     1| 59.042| N/A|    45|  2656.905| N/A|  16,937|
| |Warren County|     1| 120.992| N/A|    19|  2298.851| N/A|   8,265|
| |Sullivan County|     1| 48.382| N/A|    76|  3677.004| N/A|  20,669|
| |Pulaski County|     1| 80.952| N/A|    72|  5828.544| N/A|  12,353|
| |Washington County|     1| 35.668| N/A|   116|  4137.537| N/A|  28,036|
| |Brown County|     1| 66.260| N/A|    70|  4638.219| N/A|  15,092|
| |Benton County|     0|  0.000| N/A|    60|  6858.711| N/A|   8,748|
| |Crawford County|     0|  0.000| N/A|    42|  3970.880| N/A|  10,577|
| |Vermillion County|     0|  0.000| N/A|    38|  2451.929| N/A|  15,498|
| |Union County|     0|  0.000| N/A|    32|  4536.433| N/A|   7,054|
| |Switzerland County|     0|  0.000| N/A|    43|  3999.628| N/A|  10,751|
| |Posey County|     0|  0.000| N/A|   158|  6213.867| N/A|  25,427|
| |Pike County|     0|  0.000| N/A|    46|  3712.971| N/A|  12,389|
| |Martin County|     0|  0.000| N/A|    42|  4095.563| N/A|  10,255|
| |Knox County|     0|  0.000| N/A|   131|  3579.822| N/A|  36,594|
| |Jay County|     0|  0.000| N/A|    82|  4012.527| N/A|  20,436|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,218| 259.855| N/A|93,106| 10908.065| N/A|8,535,519|
| |Fairfax County|   530| 461.861|  0.646|15,989| 13933.381| 93.231|1,147,532|
| |Henrico County|   182| 550.151|  1.292| 3,654| 11045.348| 116.428| 330,818|
| |Prince William County|   173| 367.823|  1.640| 8,988| 19109.783| 103.478| 470,335|
| |Arlington County|   136| 574.222|  0.000| 2,945| 12434.450| 77.166| 236,842|
| |Loudoun County|   112| 270.834|  0.953| 5,059| 12233.459| 53.091| 413,538|
| |Chesterfield County|    75| 212.584|  2.143| 4,097| 11612.746| 168.702| 352,802|
| |Alexandria city|    59| 370.073|  0.000| 2,844| 17838.774| 103.495| 159,428|
| |Suffolk city|    49| 531.984|  0.000| 1,112| 12072.784| 285.763|  92,108|
| |Virginia Beach city|    47| 104.450|  1.294| 4,427|  9838.346| 276.683| 449,974|
| |Richmond County|    43| 4765.599|  0.000| 3,309| 366729.469| 3304.114|   9,023|
| |Shenandoah County|    42| 962.949|  0.000|   681| 15613.536| 84.415|  43,616|
| |Spotsylvania County|    34| 249.605|  0.000| 1,357|  9962.192| 134.971| 136,215|
| |Mecklenburg County|    32| 1046.196|  0.000|   309| 10102.331| 65.296|  30,587|
| |Hanover County|    31| 287.660|  0.000|   597|  5539.781| 41.757| 107,766|
| |Harrisonburg city|    29| 547.005|  0.000| 1,055| 19899.653| 94.311|  53,016|
| |Chesapeake city|    29| 118.447|  0.000| 2,617| 10688.831| 268.638| 244,835|
| |Northampton County|    28| 2391.119|  0.000|   294| 25106.746| 70.870|  11,710|
| |Norfolk city|    26| 107.110|  0.000| 3,345| 13780.063| 329.568| 242,742|
| |Page County|    24| 1004.100|  0.000|   333| 13931.889| 41.838|  23,902|
| |Portsmouth city|    24| 254.243|  3.324| 1,540| 16313.905| 263.319|  94,398|
| |Galax city|    22| 3466.205| 116.733|   338| 53253.506| 1102.883|   6,347|
| |Colonial Heights city|    21| 1208.981|  0.000|   185| 10650.547| 124.190|  17,370|
| |Manassas city|    20| 486.796|  0.000| 1,612| 39235.731| 60.849|  41,085|
| |Roanoke County|    18| 191.111|  0.000| 1,365| 14492.600| 355.679|  94,186|
| |Rockingham County|    17| 207.449|  0.000|   908| 11080.197| 74.454|  81,948|
| |James City County|    16| 209.087|  0.000|   562|  7344.197| 121.259|  76,523|
| |Newport News city|    16| 89.273|  0.000| 1,671|  9323.476| 178.547| 179,225|
| |Emporia city|    15| 2805.836|  0.000|   167| 31238.309| 215.871|   5,346|
| |Accomack County|    15| 464.166|  0.000| 1,080| 33419.978| 53.203|  32,316|
| |Carroll County|    14| 469.941|  0.000|   314| 10540.096| 90.170|  29,791|
| |Southampton County|    13| 737.338|  8.898|   240| 13612.387| 113.437|  17,631|
| |Charlottesville city|    13| 275.039|  6.638|   495| 10472.644| 231.879|  47,266|
| |Petersburg city|    13| 414.726| 10.009|   473| 15089.645| 303.069|  31,346|
| |Culpeper County|    12| 228.115|  0.000|   957| 18192.187| 99.973|  52,605|
| |Albemarle County|    12| 109.759|  0.000|   775|  7088.631| 133.681| 109,330|
| |Greensville County|    10| 882.145|  0.000|   437| 38549.753| 676.551|  11,336|
| |Prince Edward County|    10| 438.558|  6.880|   356| 15612.666| 219.279|  22,802|
| |Nottoway County|     9| 590.861| N/A|   176| 11554.622| N/A|  15,232|
| |Isle of Wight County|     9| 242.529| N/A|   353|  9512.517| N/A|  37,109|
| |Frederick County|     9| 100.769| N/A|   670|  7501.707| N/A|  89,313|
| |Sussex County|     9| 806.524| N/A|   279| 25002.240| N/A|  11,159|
| |Fluvanna County|     8| 293.363| N/A|   175|  6417.308| N/A|  27,270|
| |Fauquier County|     8| 112.325| N/A|   580|  8143.551| N/A|  71,222|
| |Danville city|     7| 174.808| N/A|   344|  8590.550| N/A|  40,044|
| |Goochland County|     7| 294.700| N/A|   151|  6357.092| N/A|  23,753|
| |Manassas Park city|     7| 400.503| N/A|   500| 28607.392| N/A|  17,478|
| |Franklin County|     7| 124.906| N/A|   308|  5495.878| N/A|  56,042|
| |Stafford County|     7| 45.787| N/A| 1,283|  8392.093| N/A| 152,882|
| |Botetourt County|     7| 209.462| N/A|   192|  5745.235| N/A|  33,419|
| |Williamsburg city|     6| 401.230| N/A|   114|  7623.378| N/A|  14,954|
| |Dinwiddie County|     6| 210.202| N/A|   209|  7322.029| N/A|  28,544|
| |Falls Church city|     6| 410.481| N/A|    59|  4036.396| N/A|  14,617|
| |Buckingham County|     6| 349.895| N/A|   596| 34756.240| N/A|  17,148|
| |Warren County|     6| 149.388| N/A|   348|  8664.476| N/A|  40,164|
| |Henry County|     6| 118.678| N/A|   511| 10107.404| N/A|  50,557|
| |Bedford County|     6| 75.952| N/A|   307|  3886.224| N/A|  78,997|
| |Charles City County|     5| 718.081| N/A|    50|  7180.813| N/A|   6,963|
| |Hampton city|     5| 37.172| N/A| 1,070|  7954.799| N/A| 134,510|
| |Hopewell city|     5| 221.936| N/A|   258| 11451.906| N/A|  22,529|
| |Grayson County|     4| 257.235| N/A|   134|  8617.363| N/A|  15,550|
| |Augusta County|     4| 52.939| N/A|   253|  3348.421| N/A|  75,558|
| |King George County|     4| 149.054| N/A|   124|  4620.659| N/A|  26,836|
| |Winchester city|     4| 142.460| N/A|   392| 13961.108| N/A|  28,078|
| |Caroline County|     4| 130.187| N/A|   191|  6216.436| N/A|  30,725|
| |Washington County|     4| 74.432| N/A|   181|  3368.068| N/A|  53,740|
| |Powhatan County|     4| 134.898| N/A|   128|  4316.741| N/A|  29,652|
| |Wise County|     3| 80.250| N/A|    94|  2514.512| N/A|  37,383|
| |Alleghany County|     3| 201.884| N/A|    56|  3768.506| N/A|  14,860|
| |Orange County|     3| 80.969| N/A|   213|  5748.833| N/A|  37,051|
| |Wythe County|     3| 104.588| N/A|   108|  3765.165| N/A|  28,684|
| |Waynesboro city|     3| 132.567| N/A|   167|  7379.585| N/A|  22,630|
| |Salem city|     3| 118.572| N/A|   139|  5493.854| N/A|  25,301|
| |Patrick County|     3| 170.377| N/A|   115|  6531.122| N/A|  17,608|
| |Montgomery County|     3| 30.446| N/A|   289|  2932.968| N/A|  98,535|
| |Scott County|     3| 139.108| N/A|    60|  2782.157| N/A|  21,566|
| |Pulaski County|     3| 88.165| N/A|    75|  2204.132| N/A|  34,027|
| |Smyth County|     3| 99.655| N/A|   123|  4085.836| N/A|  30,104|
| |York County|     3| 43.937| N/A|   318|  4657.293| N/A|  68,280|
| |Martinsville city|     3| 238.968| N/A|   171| 13621.157| N/A|  12,554|
| |Westmoreland County|     2| 111.019| N/A|   195| 10824.313| N/A|  18,015|
| |Rappahannock County|     2| 271.370| N/A|    40|  5427.408| N/A|   7,370|
| |Prince George County|     2| 52.147| N/A|   341|  8891.091| N/A|  38,353|
| |Pittsylvania County|     2| 33.138| N/A|   375|  6213.341| N/A|  60,354|
| |Greene County|     2| 100.913| N/A|   147|  7417.125| N/A|  19,819|
| |Surry County|     2| 311.429| N/A|    38|  5917.160| N/A|   6,422|
| |Louisa County|     2| 53.204| N/A|   167|  4442.553| N/A|  37,591|
| |Northumberland County|     2| 165.358| N/A|    66|  5456.800| N/A|  12,095|
| |King William County|     2| 116.632| N/A|    77|  4490.320| N/A|  17,148|
| |Gloucester County|     2| 53.550| N/A|   145|  3882.403| N/A|  37,348|
| |Fredericksburg city|     2| 68.880| N/A|   368| 12673.922| N/A|  29,036|
| |Lynchburg city|     2| 24.340| N/A|   469|  5707.818| N/A|  82,168|
| |Campbell County|     2| 36.440| N/A|   157|  2860.527| N/A|  54,885|
| |Madison County|     1| 75.409| N/A|    62|  4675.364| N/A|  13,261|
| |Lunenburg County|     1| 81.994| N/A|    55|  4509.675| N/A|  12,196|
| |Floyd County|     1| 63.496| N/A|    39|  2476.348| N/A|  15,749|
| |Halifax County|     1| 29.489| N/A|   141|  4157.943| N/A|  33,911|
| |Lee County|     1| 42.693| N/A|   100|  4269.308| N/A|  23,423|
| |King and Queen County|     1| 142.349| N/A|    36|  5124.555| N/A|   7,025|
| |Essex County|     1| 91.299| N/A|    83|  7577.833| N/A|  10,953|
| |Brunswick County|     1| 61.610| N/A|   212| 13061.426| N/A|  16,231|
| |Amelia County|     1| 76.075| N/A|    73|  5553.442| N/A|  13,145|
| |Middlesex County|     1| 94.500| N/A|    28|  2646.003| N/A|  10,582|
| |Russell County|     1| 37.614| N/A|    70|  2632.965| N/A|  26,586|
| |New Kent County|     1| 43.307| N/A|   119|  5153.523| N/A|  23,091|
| |Charlotte County|     0|  0.000| N/A|    49|  4124.579| N/A|  11,880|
| |Cumberland County|     0|  0.000| N/A|    68|  6846.557| N/A|   9,932|
| |Giles County|     0|  0.000| N/A|    23|  1375.598| N/A|  16,720|
| |Dickenson County|     0|  0.000| N/A|    29|  2025.423| N/A|  14,318|
| |Craig County|     0|  0.000| N/A|    16|  3118.301| N/A|   5,131|
| |Clarke County|     0|  0.000| N/A|    69|  4719.885| N/A|  14,619|
| |Buchanan County|     0|  0.000| N/A|    72|  3427.918| N/A|  21,004|
| |Highland County|     0|  0.000| N/A|     3|  1369.863| N/A|   2,190|
| |Bland County|     0|  0.000| N/A|     7|  1114.650| N/A|   6,280|
| |Amherst County|     0|  0.000| N/A|   118|  3733.586| N/A|  31,605|
| |Appomattox County|     0|  0.000| N/A|    71|  4462.322| N/A|  15,911|
| |Bath County|     0|  0.000| N/A|     4|   964.553| N/A|   4,147|
| |Lancaster County|     0|  0.000| N/A|    31|  2923.701| N/A|  10,603|
| |Staunton city|     0|  0.000| N/A|   143|  5735.601| N/A|  24,932|
| |Roanoke city|     0|  0.000| N/A|     0|     0.000| N/A|  99,143|
| |Richmond city|     0|  0.000| N/A|     0|     0.000| N/A| 230,436|
| |Tazewell County|     0|  0.000| N/A|    98|  2414.090| N/A|  40,595|
| |Bristol city|     0|  0.000| N/A|    65|  3877.819| N/A|  16,762|
| |Buena Vista city|     0|  0.000| N/A|    48|  7409.694| N/A|   6,478|
| |Covington city|     0|  0.000| N/A|    12|  2166.847| N/A|   5,538|
| |Fairfax city|     0|  0.000| N/A|     0|     0.000| N/A|  24,019|
| |Franklin city|     0|  0.000| N/A|     0|     0.000| N/A|   7,967|
| |Lexington city|     0|  0.000| N/A|    33|  4431.910| N/A|   7,446|
| |Rockbridge County|     0|  0.000| N/A|    67|  2968.148| N/A|  22,573|
| |Mathews County|     0|  0.000| N/A|    14|  1584.786| N/A|   8,834|
| |Nelson County|     0|  0.000| N/A|    34|  2277.294| N/A|  14,930|
| |Norton city|     0|  0.000| N/A|    13|  3265.511| N/A|   3,981|
| |Poquoson city|     0|  0.000| N/A|    39|  3178.225| N/A|  12,271|
| |Radford city|     0|  0.000| N/A|    26|  1424.736| N/A|  18,249|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,043| 194.792| N/A|127,630| 12169.048| N/A|10,488,084|
| |Mecklenburg County|   222| 199.936|  5.404|21,054| 18961.486| 168.983|1,110,356|
| |Guilford County|   147| 273.654|  3.101| 5,254|  9780.816| 90.021| 537,174|
| |Wake County|   133| 119.630|  0.955|11,305| 10168.552| 143.784|1,111,761|
| |Durham County|    79| 245.732|  2.578| 5,917| 18405.042| 159.738| 321,488|
| |Henderson County|    54| 459.899|  3.543| 1,402| 11940.349| 119.233| 117,417|
| |Robeson County|    51| 390.431|  0.000| 2,658| 20348.325| 219.992| 130,625|
| |Chatham County|    50| 671.411|  0.000| 1,245| 16718.142| 167.853|  74,470|
| |Cumberland County|    50| 149.027|  0.000| 2,817|  8396.198| 183.304| 335,509|
| |Cabarrus County|    49| 226.377|  9.992| 2,504| 11568.331| 275.323| 216,453|
| |Forsyth County|    49| 128.173|  0.000| 4,955| 12961.195| 100.118| 382,295|
| |Rowan County|    48| 337.819|  0.000| 2,032| 14300.997| 175.947| 142,088|
| |Buncombe County|    46| 176.116|  0.000| 1,715|  6566.076| 111.030| 261,191|
| |Columbus County|    46| 828.709|  0.000|   833| 15006.846| 252.216|  55,508|
| |Orange County|    45| 303.079|  0.000| 1,293|  8708.478| 55.275| 148,476|
| |Johnston County|    44| 210.185|  0.000| 3,085| 14736.862| 221.056| 209,339|
| |Duplin County|    43| 732.027|  9.021| 1,939| 33009.312| 138.400|  58,741|
| |Union County|    41| 170.934|  4.169| 2,823| 11769.415| 135.050| 239,859|
| |Alamance County|    41| 241.875|  0.000| 2,264| 13356.223| 241.875| 169,509|
| |Gaston County|    41| 182.604| 17.815| 3,035| 13517.185| 126.900| 224,529|
| |Vance County|    40| 898.170|  0.000|   738| 16571.236| 123.498|  44,535|
| |Wayne County|    37| 300.493|  0.000| 2,328| 18906.693| 117.129| 123,131|
| |Randolph County|    36| 250.579|  0.000| 2,071| 14415.280| 79.065| 143,667|
| |Harnett County|    36| 264.753|  0.000| 1,158|  8516.209| 213.273| 135,976|
| |Wilson County|    35| 427.868|  7.003| 1,436| 17554.798| 298.930|  81,801|
| |Catawba County|    29| 181.760|  0.000| 1,972| 12359.684| 278.908| 159,551|
| |Burke County|    28| 309.444| 10.928| 1,637| 18091.396| 505.537|  90,485|
| |Franklin County|    25| 358.757|  0.000|   797| 11437.182| 165.793|  69,685|
| |Granville County|    25| 413.613|  0.000| 1,185| 19605.248| 173.717|  60,443|
| |Moore County|    20| 198.255|  0.000|   909|  9010.706| 158.604| 100,880|
| |Stanly County|    20| 318.441| 143.298|   912| 14520.906| 232.535|  62,806|
| |New Hanover County|    20| 85.298|  1.784| 2,449| 10444.699| 270.820| 234,473|
| |Davidson County|    18| 107.393|  2.482| 1,653|  9862.239| 59.416| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,771|  9741.153| 242.221| 181,806|
| |Brunswick County|    17| 119.031|  2.991| 1,198|  8388.181| 80.867| 142,820|
| |Cleveland County|    17| 173.563| 30.629| 1,037| 10587.358| 223.247|  97,947|
| |Pasquotank County|    17| 426.878|  0.000|   359|  9014.665| 103.740|  39,824|
| |Northampton County|    16| 821.229|  0.000|   329| 16886.516| 1129.190|  19,483|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 996.373|  27,173|
| |Caldwell County|    14| 170.362| 10.074| 1,138| 13847.989| 212.952|  82,178|
| |Rutherford County|    14| 208.865|  0.000|   689| 10279.133| 149.189|  67,029|
| |McDowell County|    13| 284.116| 40.411|   609| 13309.730| 152.985|  45,756|
| |Sampson County|    12| 188.884|  0.000| 1,427| 22461.476| 80.996|  63,531|
| |Lenoir County|    12| 214.481|  0.000|   536|  9580.153| 64.512|  55,949|
| |Pitt County|    11| 60.860|  0.000| 1,795|  9931.283| 160.450| 180,742|
| |Hertford County|    11| 464.586|  0.000|   295| 12459.349| 380.116|  23,677|
| |Edgecombe County|    11| 213.708|  0.000|   589| 11443.115| 152.951|  51,472|
| |Nash County|    11| 116.651|  0.000| 1,063| 11272.774| 260.086|  94,298|
| |Lee County|    10| 161.867|  2.539| 1,217| 19699.251| 314.280|  61,779|
| |Wilkes County|    10| 146.173|  0.000|   736| 10758.346| 57.082|  68,412|
| |Craven County|    10| 97.906|  0.000|   673|  6589.060| 202.166| 102,139|
| |Onslow County|    10| 50.521|  0.000|   934|  4718.649| 58.403| 197,938|
| |Hoke County|     8| 144.838| N/A|   674| 12202.629| N/A|  55,234|
| |Surry County|     8| 111.447| N/A|   872| 12147.723| N/A|  71,783|
| |Richmond County|     8| 178.456| N/A|   486| 10841.197| N/A|  44,829|
| |Warren County|     7| 354.772| N/A|   243| 12315.645| N/A|  19,731|
| |Bladen County|     7| 213.923| N/A|   589| 18000.122| N/A|  32,722|
| |Rockingham County|     7| 76.915| N/A|   494|  5427.975| N/A|  91,010|
| |Yadkin County|     6| 159.291| N/A|   508| 13486.606| N/A|  37,667|
| |Halifax County|     6| 119.976| N/A|   650| 12997.401| N/A|  50,010|
| |Davie County|     6| 140.036| N/A|   386|  9009.009| N/A|  42,846|
| |Carteret County|     6| 86.364| N/A|   332|  4778.835| N/A|  69,473|
| |Haywood County|     6| 96.282| N/A|   348|  5584.351| N/A|  62,317|
| |Martin County|     6| 267.380| N/A|   244| 10873.440| N/A|  22,440|
| |Polk County|     5| 241.266| N/A|   140|  6755.453| N/A|  20,724|
| |Bertie County|     5| 263.894| N/A|   249| 13141.922| N/A|  18,947|
| |Cherokee County|     3| 104.851| N/A|   265|  9261.848| N/A|  28,612|
| |Greene County|     3| 142.389| N/A|   311| 14761.023| N/A|  21,069|
| |Pender County|     3| 47.574| N/A|   626|  9927.054| N/A|  63,060|
| |Macon County|     3| 83.663| N/A|   460| 12828.379| N/A|  35,858|
| |Jackson County|     3| 68.278| N/A|   412|  9376.849| N/A|  43,938|
| |Jones County|     3| 318.505| N/A|    78|  8281.134| N/A|   9,419|
| |Stokes County|     3| 65.802| N/A|   266|  5834.485| N/A|  45,591|
| |Lincoln County|     3| 34.839| N/A|   751|  8721.302| N/A|  86,111|
| |Washington County|     3| 259.067| N/A|   121| 10449.050| N/A|  11,580|
| |Dare County|     2| 54.041| N/A|   202|  5458.132| N/A|  37,009|
| |Perquimans County|     2| 148.555| N/A|    71|  5273.713| N/A|  13,463|
| |Person County|     2| 50.646| N/A|   201|  5089.896| N/A|  39,490|
| |Swain County|     2| 140.144| N/A|   105|  7357.578| N/A|  14,271|
| |Mitchell County|     2| 133.654| N/A|   116|  7751.938| N/A|  14,964|
| |Gates County|     2| 172.980| N/A|    45|  3892.060| N/A|  11,562|
| |Scotland County|     2| 57.433| N/A|   293|  8413.979| N/A|  34,823|
| |Anson County|     2| 81.813| N/A|   304| 12435.572| N/A|  24,446|
| |Alexander County|     2| 53.338| N/A|   295|  7867.296| N/A|  37,497|
| |Caswell County|     2| 88.480| N/A|   186|  8228.632| N/A|  22,604|
| |Camden County|     2| 184.043| N/A|    63|  5797.368| N/A|  10,867|
| |Beaufort County|     2| 42.559| N/A|   373|  7937.183| N/A|  46,994|
| |Chowan County|     1| 71.721| N/A|   144| 10327.763| N/A|  13,943|
| |Ashe County|     1| 36.761| N/A|   126|  4631.842| N/A|  27,203|
| |Transylvania County|     1| 29.082| N/A|   132|  3838.883| N/A|  34,385|
| |Pamlico County|     1| 78.579| N/A|    65|  5107.654| N/A|  12,726|
| |Tyrrell County|     1| 249.004| N/A|    92| 22908.367| N/A|   4,016|
| |Watauga County|     0|  0.000| N/A|   283|  5037.649| N/A|  56,177|
| |Yancey County|     0|  0.000| N/A|   101|  5589.684| N/A|  18,069|
| |Madison County|     0|  0.000| N/A|    40|  1838.658| N/A|  21,755|
| |Hyde County|     0|  0.000| N/A|    37|  7494.430| N/A|   4,937|
| |Graham County|     0|  0.000| N/A|    27|  3198.673| N/A|   8,441|
| |Currituck County|     0|  0.000| N/A|    70|  2521.341| N/A|  27,763|
| |Clay County|     0|  0.000| N/A|    76|  6766.984| N/A|  11,231|
| |Avery County|     0|  0.000| N/A|    99|  5638.777| N/A|  17,557|
| |Alleghany County|     0|  0.000| N/A|   165| 14815.480| N/A|  11,137|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,844| 320.209| N/A|47,950|  8326.480| N/A|5,758,736|
| |Denver County|   412| 566.548| N/A| 9,813| 13494.020| N/A| 727,211|
| |Arapahoe County|   363| 552.856|  0.239| 7,023| 10696.173| 71.286| 656,590|
| |Jefferson County|   227| 389.445|  0.000| 3,971|  6812.711| 51.511| 582,881|
| |Adams County|   171| 330.485|  0.000| 6,115| 11818.229| 93.734| 517,421|
| |Weld County|   141| 434.525|  0.000| 3,552| 10946.341| 46.082| 324,492|
| |El Paso County|   136| 188.783|  0.656| 4,625|  6420.018| 94.392| 720,403|
| |Boulder County|    75| 229.923|  0.000| 1,927|  5907.491| 56.569| 326,196|
| |Douglas County|    59| 168.017|  0.447| 1,653|  4707.336| 38.288| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   677| 23290.216| 25.488|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,417|  3970.311| 55.972| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   615|  3651.499| 24.141| 168,424|
| |Broomfield County|    32| 454.126| N/A|   417|  5917.832| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   287| 14099.037| 20.470|  20,356|
| |Montrose County|    13| 304.037|  0.000|   283|  6618.644| 67.386|  42,758|
| |Alamosa County|     9| 554.426| N/A|   224| 13799.051| N/A|  16,233|
| |Eagle County|     9| 163.259| N/A| 1,069| 19391.587| N/A|  55,127|
| |Gunnison County|     6| 343.603| N/A|   257| 14717.673| N/A|  17,462|
| |Otero County|     6| 328.263| N/A|    61|  3337.345| N/A|  18,278|
| |Routt County|     6| 234.028| N/A|   108|  4212.497| N/A|  25,638|
| |Logan County|     5| 223.125| N/A|   648| 28916.953| N/A|  22,409|
| |Summit County|     4| 128.986| N/A|   323| 10415.659| N/A|  31,011|
| |Montezuma County|     4| 152.771| N/A|   108|  4124.814| N/A|  26,183|
| |Garfield County|     4| 66.599| N/A|   721| 12004.462| N/A|  60,061|
| |Mesa County|     3| 19.454| N/A|   271|  1757.344| N/A| 154,210|
| |Kit Carson County|     3| 422.714| N/A|    43|  6058.898| N/A|   7,097|
| |Teller County|     3| 118.166| N/A|   113|  4450.922| N/A|  25,388|
| |Saguache County|     2| 293.083| N/A|   107| 15679.953| N/A|   6,824|
| |Pitkin County|     2| 112.568| N/A|   172|  9680.869| N/A|  17,767|
| |Rio Grande County|     2| 177.510| N/A|    87|  7721.665| N/A|  11,267|
| |La Plata County|     2| 35.574| N/A|   198|  3521.816| N/A|  56,221|
| |Elbert County|     2| 74.825| N/A|    87|  3254.892| N/A|  26,729|
| |Sedgwick County|     1| 444.840| N/A|    11|  4893.238| N/A|   2,248|
| |Moffat County|     1| 75.284| N/A|    25|  1882.105| N/A|  13,283|
| |Park County|     1| 53.064| N/A|    42|  2228.708| N/A|  18,845|
| |Huerfano County|     1| 144.991| N/A|     6|   869.943| N/A|   6,897|
| |Grand County|     1| 63.557| N/A|    44|  2796.492| N/A|  15,734|
| |Delta County|     1| 32.090| N/A|   110|  3529.940| N/A|  31,162|
| |Crowley County|     1| 164.989| N/A|    72| 11879.228| N/A|   6,061|
| |Ouray County|     1| 201.939| N/A|    12|  2423.263| N/A|   4,952|
| |Clear Creek County|     1| 103.093| N/A|    27|  2783.505| N/A|   9,700|
| |Conejos County|     0|  0.000| N/A|    23|  2803.169| N/A|   8,205|
| |Cheyenne County|     0|  0.000| N/A|     8|  4369.197| N/A|   1,831|
| |Bent County|     0|  0.000| N/A|     5|   896.539| N/A|   5,577|
| |Baca County|     0|  0.000| N/A|    14|  3909.522| N/A|   3,581|
| |Archuleta County|     0|  0.000| N/A|    33|  2352.270| N/A|  14,029|
| |Custer County|     0|  0.000| N/A|    10|  1973.165| N/A|   5,068|
| |Washington County|     0|  0.000| N/A|    47|  9576.202| N/A|   4,908|
| |Costilla County|     0|  0.000| N/A|    22|  5659.892| N/A|   3,887|
| |Dolores County|     0|  0.000| N/A|     1|   486.618| N/A|   2,055|
| |Prowers County|     0|  0.000| N/A|    48|  3943.477| N/A|  12,172|
| |Yuma County|     0|  0.000| N/A|    62|  6188.242| N/A|  10,019|
| |San Miguel County|     0|  0.000| N/A|    76|  9292.089| N/A|   8,179|
| |Gilpin County|     0|  0.000| N/A|    16|  2562.870| N/A|   6,243|
| |San Juan County|     0|  0.000| N/A|     2|  2747.253| N/A|     728|
| |Rio Blanco County|     0|  0.000| N/A|     8|  1265.022| N/A|   6,324|
| |Phillips County|     0|  0.000| N/A|    19|  4454.865| N/A|   4,265|
| |Fremont County|     0|  0.000| N/A|   112|  2341.186| N/A|  47,839|
| |Mineral County|     0|  0.000| N/A|    18| 23407.022| N/A|     769|
| |Lincoln County|     0|  0.000| N/A|     6|  1052.447| N/A|   5,701|
| |Las Animas County|     0|  0.000| N/A|    15|  1034.055| N/A|  14,506|
| |Lake County|     0|  0.000| N/A|    73|  8982.404| N/A|   8,127|
| |Kiowa County|     0|  0.000| N/A|     0|     0.000| N/A|   1,406|
| |Jackson County|     0|  0.000| N/A|     8|  5747.126| N/A|   1,392|
| |Hinsdale County|     0|  0.000| N/A|     3|  3658.537| N/A|     820|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 1,793| 348.242| N/A|92,951| 18053.246| N/A|5,148,714|
| |Greenville County|   189| 361.003|  1.910|10,306| 19685.145| 165.375| 523,542|
| |Charleston County|   171| 415.648|  7.292|11,714| 28473.090| 291.683| 411,406|
| |Richland County|   141| 339.139|  8.872| 8,040| 19338.126| 209.222| 415,759|
| |Horry County|   130| 367.148|  2.465| 8,174| 23085.113| 180.672| 354,081|
| |Lexington County|   104| 348.117|  6.199| 4,685| 15682.008| 174.685| 298,750|
| |Florence County|    99| 715.871| 12.588| 3,091| 22351.095| 564.228| 138,293|
| |Spartanburg County|    87| 272.058|  5.537| 3,793| 11861.094| 137.592| 319,785|
| |Berkeley County|    59| 258.878|  2.554| 3,880| 17024.488| 154.507| 227,907|
| |Orangeburg County|    58| 673.049|  6.119| 2,231| 25889.179| 446.940|  86,175|
| |Clarendon County|    50| 1481.701|  0.000|   786| 23292.340| 279.985|  33,745|
| |Beaufort County|    49| 255.046|  2.957| 3,682| 19164.906| 272.485| 192,122|
| |Anderson County|    48| 236.969|  6.687| 2,103| 10382.212| 260.478| 202,558|
| |Sumter County|    45| 421.660|  3.325| 2,316| 21701.446| 198.149| 106,721|
| |Dorchester County|    40| 245.687|  6.142| 2,839| 17437.611| 362.388| 162,809|
| |Laurens County|    34| 503.756|  0.000| 1,236| 18313.010| 227.034|  67,493|
| |Darlington County|    33| 495.362|  0.000| 1,133| 17007.415| 555.405|  66,618|
| |Colleton County|    31| 822.783|  0.000|   765| 20304.164| 345.038|  37,677|
| |Aiken County|    29| 169.718| 17.557| 1,594|  9328.620| 182.584| 170,872|
| |York County|    28| 99.652|  0.558| 3,246| 11552.465| 199.243| 280,979|
| |Williamsburg County|    27| 889.094| 15.497|   939| 30920.706| 625.659|  30,368|
| |Lee County|    27| 1604.469|  0.000|   526| 31257.428| 569.704|  16,828|
| |Cherokee County|    25| 436.300|  0.000|   561|  9790.576| 193.749|  57,300|
| |Pickens County|    23| 181.268|  0.000| 1,747| 13768.481| 153.684| 126,884|
| |Kershaw County|    23| 345.600|  2.357| 1,295| 19458.761| 193.951|  66,551|
| |Fairfield County|    23| 1029.221|  0.000|   539| 24119.569| 192.659|  22,347|
| |Dillon County|    23| 754.618|  0.000|   579| 18996.686| 430.359|  30,479|
| |Lancaster County|    21| 214.259|  0.000| 1,085| 11070.073| 231.872|  98,012|
| |Chesterfield County|    19| 416.210|  0.000|   707| 15487.404| 268.034|  45,650|
| |Georgetown County|    19| 303.127|  2.589| 1,307| 20851.946| 365.844|  62,680|
| |Bamberg County|    17| 1208.588| 29.573|   446| 31707.664| 484.384|  14,066|
| |Greenwood County|    15| 211.831|  0.000| 1,275| 18005.677| 564.884|  70,811|
| |Jasper County|    13| 432.281| 10.433|   510| 16958.734| 232.509|  30,073|
| |Chester County|    12| 372.162| 12.969|   578| 17925.816| 454.729|  32,244|
| |Marion County|    12| 391.428|  0.000|   523| 17059.725| 163.095|  30,657|
| |Calhoun County|    10| 687.144| 50.911|   337| 23156.737| 962.001|  14,553|
| |Newberry County|     9| 234.131| N/A|   782| 20343.392| N/A|  38,440|
| |Saluda County|     8| 390.759| N/A|   421| 20563.669| N/A|  20,473|
| |Hampton County|     7| 364.166| N/A|   392| 20393.299| N/A|  19,222|
| |Oconee County|     7| 87.999| N/A|   755|  9491.363| N/A|  79,546|
| |Abbeville County|     7| 285.400| N/A|   298| 12149.876| N/A|  24,527|
| |Edgefield County|     6| 220.103| N/A|   289| 10601.614| N/A|  27,260|
| |Marlboro County|     4| 153.151| N/A|   443| 16961.483| N/A|  26,118|
| |Barnwell County|     4| 191.699| N/A|   369| 17684.271| N/A|  20,866|
| |Allendale County|     3| 345.304| N/A|   193| 22214.549| N/A|   8,688|
| |Union County|     2| 73.217| N/A|   335| 12263.875| N/A|  27,316|
| |McCormick County|     2| 211.349| N/A|   106| 11201.522| N/A|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,711| 574.904| N/A|61,125| 20538.286| N/A|2,976,149|
| |Hinds County|   106| 457.212|  5.249| 5,269| 22726.881| 228.264| 231,840|
| |Lauderdale County|    88| 1187.184|  0.000| 1,329| 17929.174| 55.738|  74,125|
| |Neshoba County|    88| 3022.186| 18.199| 1,197| 41108.593| 137.372|  29,118|
| |Leflore County|    59| 2093.461|  0.000|   840| 29805.202| 266.138|  28,183|
| |Jones County|    57| 837.029|  0.000| 1,774| 26050.692| 293.760|  68,098|
| |Madison County|    56| 526.950| 16.276| 2,297| 21614.348| 124.618| 106,272|
| |Forrest County|    53| 707.638| 13.501| 1,640| 21896.738| 322.441|  74,897|
| |Monroe County|    50| 1418.359|  0.000|   702| 19913.764| 212.754|  35,252|
| |Holmes County|    47| 2763.081| 24.929|   847| 49794.239| 389.841|  17,010|
| |Lincoln County|    40| 1171.200| 16.873|   745| 21813.603| 147.075|  34,153|
| |Pearl River County|    36| 648.240|  0.000|   485|  8733.231| 162.060|  55,535|
| |Oktibbeha County|    35| 705.830|  0.000| 1,054| 21255.571| 100.833|  49,587|
| |Jackson County|    34| 236.741|  0.000| 1,994| 13884.150| 392.574| 143,617|
| |Washington County|    32| 728.780|  0.000| 1,492| 33979.366| 474.615|  43,909|
| |Bolivar County|    32| 1044.796|  0.000|   948| 30952.070| 287.220|  30,628|
| |Lowndes County|    32| 546.122| 14.580|   989| 16878.573| 268.450|  58,595|
| |Pike County|    32| 814.498|  7.986|   832| 21176.950| 183.356|  39,288|
| |Harrison County|    32| 153.787|  0.749| 2,152| 10342.176| 195.545| 208,080|
| |Lee County|    30| 351.140|  1.836| 1,239| 14502.083| 280.772|  85,436|
| |Rankin County|    28| 180.330|  0.000| 2,146| 13820.997| 112.706| 155,271|
| |Warren County|    27| 594.963| 18.579|   964| 21242.370| 94.785|  45,381|
| |Simpson County|    27| 1012.829| 37.512|   712| 26708.680| 145.933|  26,658|
| |DeSoto County|    27| 145.989|  0.848| 3,326| 17983.725| 340.106| 184,945|
| |Leake County|    25| 1097.165|  0.000|   768| 33704.907| 160.814|  22,786|
| |Adams County|    25| 814.518| 10.222|   584| 19027.140| 191.668|  30,693|
| |Clarke County|    25| 1608.648|  0.000|   300| 19303.777| 96.519|  15,541|
| |Copiah County|    24| 855.158| 15.220|   917| 32674.149| 243.695|  28,065|
| |Attala County|    24| 1320.568|  8.632|   498| 27401.783| 165.071|  18,174|
| |Tate County|    23| 812.118| 20.622|   650| 22951.167| 600.261|  28,321|
| |Sunflower County|    22| 876.145|  0.000|   908| 36160.892| 145.606|  25,110|
| |Wayne County|    21| 1040.480|  0.000|   733| 36317.693| 49.547|  20,183|
| |Grenada County|    20| 963.484|  0.000|   813| 39165.623| 228.963|  20,758|
| |Chickasaw County|    19| 1110.916|  0.000|   438| 25609.542| 337.188|  17,103|
| |Walthall County|    18| 1259.975|  0.000|   453| 31709.366| 571.259|  14,286|
| |Marion County|    18| 732.511|  0.000|   601| 24457.738| 214.955|  24,573|
| |Scott County|    17| 604.466|  0.000|   955| 33956.763| 82.486|  28,124|
| |Kemper County|    15| 1539.725|  0.000|   223| 22890.577|  0.000|   9,742|
| |Winston County|    15| 835.422|  8.737|   571| 31801.727| 139.237|  17,955|
| |Hancock County|    14| 293.920|  0.000|   336|  7054.081| 114.005|  47,632|
| |Union County|    13| 451.154|  0.000|   531| 18427.902| 318.060|  28,815|
| |Claiborne County|    13| 1446.373|  0.000|   400| 44503.783| 55.630|   8,988|
| |Clay County|    13| 673.017|  0.000|   370| 19155.105| 139.648|  19,316|
| |Smith County|    13| 816.788|  9.856|   380| 23875.346| 223.841|  15,916|
| |Wilkinson County|    12| 1390.498|  0.000|   187| 21668.598| 579.374|   8,630|
| |Webster County|    12| 1238.518|  0.000|   199| 20538.755| 206.420|   9,689|
| |Lamar County|    12| 189.445|  0.000| 1,121| 17697.299| 173.600|  63,343|
| |Tippah County|    12| 545.083|  0.000|   312| 14172.155| 408.812|  22,015|
| |Greene County|    11| 809.657|  0.000|   226| 16634.771| 36.008|  13,586|
| |Humphreys County|    11| 1364.087|  0.000|   271| 33606.151| 373.099|   8,064|
| |Carroll County|    11| 1105.861|  0.000|   245| 24630.542| 146.430|   9,947|
| |Panola County|    11| 321.713|  0.000|   912| 26672.906| 555.686|  34,192|
| |Yazoo County|    11| 370.495|  0.000|   786| 26473.560| 349.927|  29,690|
| |Newton County|    11| 523.361|  0.000|   516| 24550.385|  0.000|  21,018|
| |Lafayette County|    11| 203.632| 21.209|   881| 16309.076| 444.288|  54,019|
| |Covington County|    11| 590.255|  0.000|   588| 31551.835| 536.596|  18,636|
| |Coahoma County|    10| 451.998|  0.000|   663| 29967.456| 402.633|  22,124|
| |Yalobusha County|    10| 825.900|  0.000|   312| 25768.087| 57.300|  12,108|
| |Itawamba County|    10| 427.533|  0.000|   307| 13125.267| 87.042|  23,390|
| |Tallahatchie County|    10| 724.165|  0.000|   493| 35701.354| 1701.789|  13,809|
| |Noxubee County|    10| 959.969|  0.000|   419| 40222.713| 247.320|  10,417|
| |Marshall County|     8| 226.667| N/A|   571| 16178.387| N/A|  35,294|
| |Calhoun County|     8| 557.064| N/A|   378| 26321.287| N/A|  14,361|
| |Jasper County|     8| 488.311| N/A|   376| 22950.620| N/A|  16,383|
| |Perry County|     7| 584.649| N/A|   222| 18541.719| N/A|  11,973|
| |Pontotoc County|     7| 217.567| N/A|   737| 22906.695| N/A|  32,174|
| |Tunica County|     6| 622.924| N/A|   278| 28862.126| N/A|   9,632|
| |Jefferson County|     6| 858.369| N/A|   193| 27610.873| N/A|   6,990|
| |Jefferson Davis County|     6| 539.180| N/A|   202| 18152.408| N/A|  11,128|
| |Prentiss County|     6| 238.796| N/A|   342| 13611.399| N/A|  25,126|
| |Amite County|     5| 406.603| N/A|   210| 17077.336| N/A|  12,297|
| |George County|     5| 204.082| N/A|   547| 22326.531| N/A|  24,500|
| |Lawrence County|     5| 397.267| N/A|   313| 24868.902| N/A|  12,586|
| |Alcorn County|     4| 108.246| N/A|   357|  9660.921| N/A|  36,953|
| |Choctaw County|     4| 487.211| N/A|   127| 15468.940| N/A|   8,210|
| |Tishomingo County|     4| 206.366| N/A|   320| 16509.312| N/A|  19,383|
| |Montgomery County|     3| 306.905| N/A|   293| 29974.425| N/A|   9,775|
| |Stone County|     3| 163.613| N/A|   152|  8289.703| N/A|  18,336|
| |Franklin County|     2| 259.302| N/A|   116| 15039.544| N/A|   7,713|
| |Issaquena County|     1| 753.580| N/A|    21| 15825.170| N/A|   1,327|
| |Quitman County|     1| 147.232| N/A|   225| 33127.208| N/A|   6,792|
| |Sharkey County|     1| 231.428| N/A|   180| 41657.024| N/A|   4,321|
| |Benton County|     0|  0.000| N/A|   125| 15135.004| N/A|   8,259|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,616| 286.544| N/A|56,420| 10004.199| N/A|5,639,632|
| |Hennepin County|   819| 647.000|  0.000|18,009| 14226.883| 182.487|1,265,843|
| |Ramsey County|   261| 474.269|  0.854| 6,944| 12618.090| 160.074| 550,321|
| |Anoka County|   113| 316.597|  0.000| 3,365|  9427.857| 118.315| 356,921|
| |Dakota County|   103| 240.081|  2.331| 3,991|  9302.575| 152.140| 429,021|
| |Washington County|    43| 163.847|  0.000| 1,917|  7304.527| 125.172| 262,440|
| |Clay County|    40| 622.840|  2.443|   745| 11600.386| 23.753|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,629| 10291.043| 56.857| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,831| 17575.664| 78.739| 161,075|
| |St. Louis County|    19| 95.444|  2.361|   436|  2190.184| 77.036| 199,070|
| |Winona County|    16| 316.932|  0.000|   247|  4892.639| 42.706|  50,484|
| |Scott County|    14| 93.952|  6.711| 1,390|  9328.045| 188.855| 149,013|
| |Crow Wing County|    13| 199.831|  0.000|   213|  3274.153| 115.287|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   312|  9103.110| 133.414|  34,274|
| |Itasca County|    12| 265.899|  0.000|   132|  2924.884|  0.000|  45,130|
| |Pipestone County|     9| 986.193| N/A|   143| 15669.516| N/A|   9,126|
| |Rice County|     8| 119.453| N/A|   999| 14916.682| N/A|  66,972|
| |Goodhue County|     8| 172.637| N/A|   176|  3798.015| N/A|  46,340|
| |Sherburne County|     7| 71.988| N/A|   649|  6674.345| N/A|  97,238|
| |Nobles County|     6| 277.405| N/A| 1,746| 80724.953| N/A|  21,629|
| |Renville County|     5| 343.690| N/A|    59|  4055.540| N/A|  14,548|
| |Wright County|     5| 36.133| N/A|   813|  5875.254| N/A| 138,377|
| |Blue Earth County|     5| 73.907| N/A|   852| 12593.677| N/A|  67,653|
| |Martin County|     5| 254.026| N/A|   204| 10364.274| N/A|  19,683|
| |Wilkin County|     3| 483.325| N/A|    28|  4511.036| N/A|   6,207|
| |Benton County|     3| 73.369| N/A|   306|  7483.675| N/A|  40,889|
| |Koochiching County|     3| 245.319| N/A|    74|  6051.190| N/A|  12,229|
| |Mille Lacs County|     3| 114.168| N/A|    65|  2473.646| N/A|  26,277|
| |Otter Tail County|     3| 51.067| N/A|   176|  2995.949| N/A|  58,746|
| |Polk County|     3| 95.651| N/A|   131|  4176.763| N/A|  31,364|
| |Lyon County|     3| 117.767| N/A|   416| 16330.376| N/A|  25,474|
| |Mower County|     2| 49.923| N/A| 1,081| 26983.176| N/A|  40,062|
| |Meeker County|     2| 86.125| N/A|    83|  3574.197| N/A|  23,222|
| |Sibley County|     2| 134.544| N/A|    79|  5314.497| N/A|  14,865|
| |Todd County|     2| 81.090| N/A|   420| 17028.868| N/A|  24,664|
| |Carver County|     2| 19.031| N/A|   779|  7412.764| N/A| 105,089|
| |Brown County|     2| 79.974| N/A|    85|  3398.912| N/A|  25,008|
| |Cass County|     2| 67.161| N/A|    58|  1947.681| N/A|  29,779|
| |Swift County|     1| 107.921| N/A|    52|  5611.915| N/A|   9,266|
| |Steele County|     1| 27.286| N/A|   330|  9004.338| N/A|  36,649|
| |Freeborn County|     1| 33.024| N/A|   354| 11690.499| N/A|  30,281|
| |Grant County|     1| 167.448| N/A|    49|  8204.956| N/A|   5,972|
| |Pennington County|     1| 70.827| N/A|    72|  5099.511| N/A|  14,119|
| |Murray County|     1| 122.041| N/A|   122| 14888.943| N/A|   8,194|
| |Morrison County|     1| 29.953| N/A|    83|  2486.072| N/A|  33,386|
| |Mahnomen County|     1| 180.930| N/A|    23|  4161.390| N/A|   5,527|
| |Le Sueur County|     1| 34.618| N/A|   201|  6958.147| N/A|  28,887|
| |Kandiyohi County|     1| 23.149| N/A|   676| 15648.510| N/A|  43,199|
| |Kanabec County|     1| 61.211| N/A|    29|  1775.112| N/A|  16,337|
| |Becker County|     1| 29.050| N/A|   143|  4154.199| N/A|  34,423|
| |Chippewa County|     1| 84.746| N/A|    98|  8305.085| N/A|  11,800|
| |Chisago County|     1| 17.674| N/A|   179|  3163.718| N/A|  56,579|
| |Lake of the Woods County|     0|  0.000| N/A|     1|   267.380| N/A|   3,740|
| |McLeod County|     0|  0.000| N/A|   138|  3844.761| N/A|  35,893|
| |Marshall County|     0|  0.000| N/A|    28|  2999.143| N/A|   9,336|
| |Norman County|     0|  0.000| N/A|    34|  5333.333| N/A|   6,375|
| |Pine County|     0|  0.000| N/A|   127|  4293.587| N/A|  29,579|
| |Pope County|     0|  0.000| N/A|    43|  3822.562| N/A|  11,249|
| |Wabasha County|     0|  0.000| N/A|    81|  3745.318| N/A|  21,627|
| |Yellow Medicine County|     0|  0.000| N/A|    49|  5046.864| N/A|   9,709|
| |Watonwan County|     0|  0.000| N/A|   298| 27346.976| N/A|  10,897|
| |Waseca County|     0|  0.000| N/A|   128|  6877.283| N/A|  18,612|
| |Wadena County|     0|  0.000| N/A|    23|  1681.041| N/A|  13,682|
| |Traverse County|     0|  0.000| N/A|    10|  3068.426| N/A|   3,259|
| |Stevens County|     0|  0.000| N/A|    15|  1529.832| N/A|   9,805|
| |Roseau County|     0|  0.000| N/A|    46|  3033.300| N/A|  15,165|
| |Rock County|     0|  0.000| N/A|    74|  7944.176| N/A|   9,315|
| |Redwood County|     0|  0.000| N/A|    30|  1977.587| N/A|  15,170|
| |Red Lake County|     0|  0.000| N/A|    20|  4932.182| N/A|   4,055|
| |Lincoln County|     0|  0.000| N/A|    54|  9576.166| N/A|   5,639|
| |Faribault County|     0|  0.000| N/A|    83|  6079.250| N/A|  13,653|
| |Lake County|     0|  0.000| N/A|    18|  1691.570| N/A|  10,641|
| |Lac qui Parle County|     0|  0.000| N/A|     6|   905.934| N/A|   6,623|
| |Kittson County|     0|  0.000| N/A|     4|   930.665| N/A|   4,298|
| |Jackson County|     0|  0.000| N/A|    70|  7109.486| N/A|   9,846|
| |Isanti County|     0|  0.000| N/A|   110|  2709.627| N/A|  40,596|
| |Hubbard County|     0|  0.000| N/A|    28|  1302.871| N/A|  21,491|
| |Houston County|     0|  0.000| N/A|    39|  2096.774| N/A|  18,600|
| |Fillmore County|     0|  0.000| N/A|    61|  2895.524| N/A|  21,067|
| |Douglas County|     0|  0.000| N/A|   130|  3408.406| N/A|  38,141|
| |Dodge County|     0|  0.000| N/A|   123|  5875.609| N/A|  20,934|
| |Cottonwood County|     0|  0.000| N/A|   171| 15273.312| N/A|  11,196|
| |Cook County|     0|  0.000| N/A|     2|   366.099| N/A|   5,463|
| |Clearwater County|     0|  0.000| N/A|    15|  1701.066| N/A|   8,818|
| |Carlton County|     0|  0.000| N/A|   125|  3484.709| N/A|  35,871|
| |Big Stone County|     0|  0.000| N/A|    22|  4407.934| N/A|   4,991|
| |Beltrami County|     0|  0.000| N/A|   193|  4090.023| N/A|  47,188|
| |Aitkin County|     0|  0.000| N/A|    27|  1699.610| N/A|  15,886|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,599| 209.983| N/A|58,527|  7685.860| N/A|7,614,893|
| |King County|   658| 292.083|  0.666|15,603|  6926.103| 65.298|2,252,782|
| |Yakima County|   205| 817.147|  1.650|10,047| 40048.152| 169.391| 250,873|
| |Snohomish County|   190| 231.120|  0.841| 5,159|  6275.522| 43.791| 822,083|
| |Pierce County|   129| 142.545|  1.271| 5,216|  5763.663| 110.167| 904,980|
| |Benton County|   110| 538.187|  3.440| 3,514| 17192.622| 70.514| 204,390|
| |Spokane County|    61| 116.680|  2.472| 3,909|  7477.075| 98.508| 522,798|
| |Franklin County|    47| 493.583|  1.624| 3,325| 34918.401| 228.028|  95,222|
| |Clark County|    42| 86.023|  0.172| 1,620|  3318.034| 109.577| 488,241|
| |Whatcom County|    38| 165.760|  0.684|   936|  4082.932| 57.608| 229,247|
| |Skagit County|    21| 162.532|  1.205|   826|  6392.941| 81.497| 129,205|
| |Kittitas County|    17| 354.647|  0.000|   348|  7259.831| 77.636|  47,935|
| |Grant County|    12| 122.784|  0.000| 1,294| 13240.154| 322.307|  97,733|
| |Island County|    11| 129.197|  0.000|   239|  2807.108| 12.729|  85,141|
| |Chelan County|    10| 129.534|  2.032| 1,177| 15246.114| 465.941|  77,200|
| |Thurston County|     8| 27.535| N/A|   640|  2202.825| N/A| 290,536|
| |Douglas County|     7| 161.183| N/A|   830| 19111.654| N/A|  43,429|
| |Cowlitz County|     5| 45.211| N/A|   446|  4032.805| N/A| 110,593|
| |Adams County|     4| 200.170| N/A|   400| 20017.014| N/A|  19,983|
| |Kitsap County|     4| 14.734| N/A|   658|  2423.814| N/A| 271,473|
| |Walla Walla County|     3| 49.375| N/A|   454|  7472.021| N/A|  60,760|
| |Klickitat County|     3| 133.779| N/A|   106|  4726.867| N/A|  22,425|
| |Lewis County|     3| 37.171| N/A|   189|  2341.804| N/A|  80,707|
| |Pacific County|     2| 89.004| N/A|    40|  1780.072| N/A|  22,471|
| |Okanogan County|     2| 47.345| N/A|   771| 18251.545| N/A|  42,243|
| |Asotin County|     2| 88.566| N/A|    24|  1062.793| N/A|  22,582|
| |Stevens County|     1| 21.871| N/A|    92|  2012.116| N/A|  45,723|
| |Skamania County|     1| 82.761| N/A|    53|  4386.328| N/A|  12,083|
| |Mason County|     1| 14.977| N/A|   163|  2441.289| N/A|  66,768|
| |Columbia County|     1| 250.941| N/A|    13|  3262.233| N/A|   3,985|
| |Grays Harbor County|     1| 13.322| N/A|    99|  1318.927| N/A|  75,061|
| |Wahkiakum County|     0|  0.000| N/A|     5|  1114.082| N/A|   4,488|
| |Jefferson County|     0|  0.000| N/A|    53|  1644.890| N/A|  32,221|
| |Whitman County|     0|  0.000| N/A|    87|  1736.388| N/A|  50,104|
| |Garfield County|     0|  0.000| N/A|     2|   898.876| N/A|   2,225|
| |Lincoln County|     0|  0.000| N/A|    13|  1188.408| N/A|  10,939|
| |San Juan County|     0|  0.000| N/A|    28|  1592.538| N/A|  17,582|
| |Pend Oreille County|     0|  0.000| N/A|    36|  2623.142| N/A|  13,724|
| |Clallam County|     0|  0.000| N/A|    94|  1215.554| N/A|  77,331|
| |Ferry County|     0|  0.000| N/A|    18|  2360.037| N/A|   7,627|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,580| 322.240| N/A|89,927| 18340.528| N/A|4,903,185|
| |Jefferson County|   225| 341.648|  0.555|11,859| 18007.115| 335.659| 658,573|
| |Mobile County|   191| 462.235|  3.460| 9,086| 21988.819| 212.967| 413,210|
| |Montgomery County|   143| 631.386|  3.701| 6,249| 27591.109| 321.278| 226,486|
| |Tallapoosa County|    78| 1932.271|  0.000|   814| 20164.986| 164.457|  40,367|
| |Tuscaloosa County|    63| 300.924|  0.000| 3,974| 18982.112| 296.148| 209,355|
| |Walker County|    63| 991.798|  6.113| 1,470| 23141.953| 154.601|  63,521|
| |Lee County|    40| 243.099|  0.000| 2,505| 15224.077| 151.937| 164,542|
| |Chambers County|    38| 1142.720|  0.000|   821| 24688.759| 181.640|  33,254|
| |Elmore County|    37| 455.615|  0.000| 1,602| 19726.878| 246.278|  81,209|
| |Butler County|    35| 1799.671|  0.000|   752| 38667.215| 228.153|  19,448|
| |Shelby County|    32| 146.990|  0.000| 3,050| 14009.977| 218.102| 217,702|
| |Marshall County|    30| 310.001|  3.242| 2,966| 30648.728| 475.283|  96,774|
| |Hale County|    26| 1774.623| 68.255|   459| 31328.920| 364.994|  14,651|
| |Etowah County|    26| 254.234|  9.778| 1,930| 18871.983| 224.899| 102,268|
| |Madison County|    25| 67.040|  0.000| 5,014| 13445.640| 264.140| 372,909|
| |Marion County|    24| 807.836|  0.000|   542| 18243.630| 235.619|  29,709|
| |Lowndes County|    24| 2467.613|  0.000|   552| 56755.089| 281.531|   9,726|
| |Dallas County|    23| 618.346|  0.000| 1,288| 34627.379| 288.323|  37,196|
| |Baldwin County|    23| 103.031|  3.781| 3,210| 14379.530| 174.705| 223,234|
| |Dale County|    20| 406.736| 15.862|   785| 15964.370| 233.716|  49,172|
| |Covington County|    20| 539.826|  0.000|   709| 19136.819| 301.544|  37,049|
| |Franklin County|    20| 637.714|  0.000| 1,196| 38135.323| 382.629|  31,362|
| |Autauga County|    20| 357.980|  0.000| 1,024| 18328.590| 317.067|  55,869|
| |Sumter County|    18| 1448.459| 12.623|   361| 29049.650|  0.000|  12,427|
| |Morgan County|    15| 125.335|  3.538| 2,223| 18574.687| 271.883| 119,679|
| |Escambia County|    15| 409.467|  0.000|   979| 26724.538| 352.436|  36,633|
| |Marengo County|    14| 742.194|  0.000|   520| 27567.195| 106.028|  18,863|
| |Limestone County|    13| 131.426|  5.883| 1,196| 12091.189| 188.780|  98,915|
| |Macon County|    13| 719.504| 23.642|   309| 17102.059| 152.186|  18,068|
| |Talladega County|    13| 162.545|  1.961|   918| 11478.156| 326.661|  79,978|
| |DeKalb County|    13| 181.785|  0.000| 1,701| 23785.885| 349.288|  71,513|
| |St. Clair County|    12| 134.060|  7.751| 1,217| 13595.942| 268.120|  89,512|
| |Choctaw County|    12| 953.213|  0.000|   274| 21765.033| 100.905|  12,589|
| |Lauderdale County|    12| 129.409|  3.383| 1,071| 11549.785| 219.230|  92,729|
| |Colbert County|    12| 217.230|  0.000| 1,093| 19786.028| 386.486|  55,241|
| |Houston County|    12| 113.334|  0.000| 1,319| 12457.264| 207.778| 105,882|
| |Bullock County|    11| 1089.001|  0.000|   438| 43362.043| 176.652|  10,101|
| |Cullman County|    11| 131.315|  0.000| 1,141| 13620.953| 285.128|  83,768|
| |Washington County|    11| 673.772|  9.609|   310| 18988.117| 185.584|  16,326|
| |Winston County|    11| 465.530|  0.000|   429| 18155.656| 112.221|  23,629|
| |Greene County|    11| 1356.183|  0.000|   242| 29836.025| 155.220|   8,111|
| |Conecuh County|    10| 828.706|  0.000|   373| 30910.748| 414.353|  12,067|
| |Randolph County|    10| 440.102|  0.000|   388| 17075.962| 50.912|  22,722|
| |Calhoun County|     9| 79.222| N/A| 1,560| 13731.790| N/A| 113,605|
| |Clarke County|     9| 381.001| N/A|   486| 20574.041| N/A|  23,622|
| |Wilcox County|     9| 867.637| N/A|   405| 39043.671| N/A|  10,373|
| |Pickens County|     9| 451.581| N/A|   367| 18414.451| N/A|  19,930|
| |Pike County|     7| 211.391| N/A|   660| 19931.147| N/A|  33,114|
| |Cherokee County|     7| 267.216| N/A|   242|  9238.052| N/A|  26,196|
| |Chilton County|     6| 135.050| N/A|   710| 15980.913| N/A|  44,428|
| |Fayette County|     5| 306.711| N/A|   174| 10673.537| N/A|  16,302|
| |Barbour County|     5| 202.544| N/A|   563| 22806.449| N/A|  24,686|
| |Clay County|     5| 377.786| N/A|   217| 16395.920| N/A|  13,235|
| |Coffee County|     5| 95.526| N/A|   709| 13545.527| N/A|  52,342|
| |Perry County|     4| 448.280| N/A|   429| 48078.001| N/A|   8,923|
| |Monroe County|     4| 192.929| N/A|   391| 18858.824| N/A|  20,733|
| |Bibb County|     3| 133.964| N/A|   374| 16700.902| N/A|  22,394|
| |Blount County|     3| 51.880| N/A|   736| 12727.839| N/A|  57,826|
| |Crenshaw County|     3| 217.833| N/A|   286| 20766.773| N/A|  13,772|
| |Henry County|     3| 174.368| N/A|   245| 14240.046| N/A|  17,205|
| |Jackson County|     3| 58.110| N/A|   828| 16038.430| N/A|  51,626|
| |Lamar County|     2| 144.875| N/A|   198| 14342.629| N/A|  13,805|
| |Coosa County|     2| 187.564| N/A|    92|  8627.966| N/A|  10,663|
| |Russell County|     1| 17.253| N/A| 1,233| 21272.925| N/A|  57,961|
| |Cleburne County|     1| 67.069| N/A|   121|  8115.359| N/A|  14,910|
| |Lawrence County|     0|  0.000| N/A|   310|  9415.624| N/A|  32,924|
| |Geneva County|     0|  0.000| N/A|   232|  8831.030| N/A|  26,271|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,225| 199.595| N/A|47,187|  7688.400| N/A|6,137,428|
| |St. Louis County|   821| 825.785|  0.844|18,141| 18246.740| 257.338| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,636|  9044.281| 159.195| 402,022|
| |Jackson County|    59| 83.925|  0.502| 3,537|  5031.216| 108.106| 703,011|
| |Jasper County|    25| 206.053|  0.000| 1,659| 13673.678| 164.842| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,395|  6197.769| 148.323| 225,081|
| |Clay County|    20| 80.017|  0.628|   914|  3656.761| 36.007| 249,948|
| |Franklin County|    18| 173.132|  0.000|   542|  5213.193| 117.457| 103,967|
| |Scott County|    13| 339.603|  0.000|   352|  9195.402| 143.678|  38,280|
| |Platte County|    10| 95.769|  4.507|   318|  3045.452| 67.038| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,062| 12156.037| 68.678|  87,364|
| |Greene County|    10| 34.120|  0.000| 1,256|  4285.432| 86.586| 293,086|
| |Stoddard County|     9| 310.078| N/A|   209|  7200.689| N/A|  29,025|
| |Cass County|     9| 85.082| N/A|   654|  6182.643| N/A| 105,780|
| |Gentry County|     9| 1369.655| N/A|    82| 12479.075| N/A|   6,571|
| |Pemiscot County|     8| 506.169| N/A|   214| 13540.019| N/A|  15,805|
| |Saline County|     7| 307.544| N/A|   415| 18232.942| N/A|  22,761|
| |McDonald County|     7| 306.520| N/A|   936| 40986.119| N/A|  22,837|
| |Newton County|     6| 103.029| N/A|   807| 13857.408| N/A|  58,236|
| |Camden County|     4| 86.384| N/A|   309|  6673.145| N/A|  46,305|
| |Dunklin County|     4| 137.311| N/A|   255|  8753.561| N/A|  29,131|
| |Perry County|     4| 209.030| N/A|   208| 10869.565| N/A|  19,136|
| |Boone County|     3| 16.624| N/A| 1,236|  6849.049| N/A| 180,463|
| |Cape Girardeau County|     3| 38.037| N/A|   607|  7696.111| N/A|  78,871|
| |Henry County|     3| 137.463| N/A|    72|  3299.120| N/A|  21,824|
| |Pettis County|     3| 70.857| N/A|   435| 10274.215| N/A|  42,339|
| |Taney County|     3| 53.640| N/A|   456|  8153.340| N/A|  55,928|
| |Butler County|     2| 47.083| N/A|   247|  5814.775| N/A|  42,478|
| |St. Francois County|     2| 29.755| N/A|   307|  4567.433| N/A|  67,215|
| |Moniteau County|     2| 123.977| N/A|   123|  7624.597| N/A|  16,132|
| |Cole County|     2| 26.060| N/A|   325|  4234.804| N/A|  76,745|
| |Johnson County|     2| 36.995| N/A|   473|  8749.214| N/A|  54,062|
| |Lawrence County|     2| 52.144| N/A|   192|  5005.866| N/A|  38,355|
| |Lafayette County|     2| 61.147| N/A|   158|  4830.622| N/A|  32,708|
| |Howell County|     2| 49.854| N/A|   140|  3489.792| N/A|  40,117|
| |Douglas County|     2| 151.688| N/A|    81|  6143.345| N/A|  13,185|
| |Pulaski County|     1| 19.009| N/A|   183|  3478.625| N/A|  52,607|
| |Putnam County|     1| 212.947| N/A|    10|  2129.472| N/A|   4,696|
| |Pike County|     1| 54.639| N/A|    74|  4043.274| N/A|  18,302|
| |Randolph County|     1| 40.407| N/A|    57|  2303.216| N/A|  24,748|
| |Ste. Genevieve County|     1| 55.885| N/A|    46|  2570.694| N/A|  17,894|
| |Scotland County|     1| 203.998| N/A|    12|  2447.980| N/A|   4,902|
| |Shannon County|     1| 122.459| N/A|    43|  5265.736| N/A|   8,166|
| |Stone County|     1| 31.297| N/A|    88|  2754.131| N/A|  31,952|
| |Webster County|     1| 25.258| N/A|   118|  2980.400| N/A|  39,592|
| |Washington County|     1| 40.437| N/A|    56|  2264.456| N/A|  24,730|
| |Dallas County|     1| 59.249| N/A|    50|  2962.436| N/A|  16,878|
| |Audrain County|     1| 39.389| N/A|   194|  7641.405| N/A|  25,388|
| |Bates County|     1| 61.835| N/A|    40|  2473.411| N/A|  16,172|
| |Benton County|     1| 51.432| N/A|    75|  3857.429| N/A|  19,443|
| |Marion County|     1| 35.051| N/A|   157|  5502.979| N/A|  28,530|
| |Linn County|     1| 83.893| N/A|    31|  2600.671| N/A|  11,920|
| |Lincoln County|     1| 16.945| N/A|   314|  5320.862| N/A|  59,013|
| |Lewis County|     1| 102.291| N/A|    34|  3477.905| N/A|   9,776|
| |Laclede County|     1| 27.993| N/A|   200|  5598.634| N/A|  35,723|
| |Harrison County|     1| 119.732| N/A|    60|  7183.908| N/A|   8,352|
| |Andrew County|     1| 56.459| N/A|    84|  4742.547| N/A|  17,712|
| |Grundy County|     1| 101.523| N/A|    24|  2436.548| N/A|   9,850|
| |Christian County|     1| 11.287| N/A|   286|  3228.173| N/A|  88,595|
| |Carter County|     1| 167.168| N/A|    19|  3176.195| N/A|   5,982|
| |Callaway County|     1| 22.350| N/A|   130|  2905.482| N/A|  44,743|
| |Caldwell County|     1| 110.865| N/A|    35|  3880.266| N/A|   9,020|
| |DeKalb County|     1| 79.700| N/A|    32|  2550.410| N/A|  12,547|
| |New Madrid County|     1| 58.562| N/A|   194| 11360.974| N/A|  17,076|
| |Gasconade County|     0|  0.000| N/A|    20|  1359.989| N/A|  14,706|
| |Carroll County|     0|  0.000| N/A|    99| 11406.844| N/A|   8,679|
| |Mercer County|     0|  0.000| N/A|     9|  2488.250| N/A|   3,617|
| |Hickory County|     0|  0.000| N/A|    17|  1781.224| N/A|   9,544|
| |Maries County|     0|  0.000| N/A|    17|  1954.697| N/A|   8,697|
| |Madison County|     0|  0.000| N/A|    17|  1406.353| N/A|  12,088|
| |Macon County|     0|  0.000| N/A|    53|  3505.987| N/A|  15,117|
| |Livingston County|     0|  0.000| N/A|    53|  3480.659| N/A|  15,227|
| |Knox County|     0|  0.000| N/A|    19|  4799.192| N/A|   3,959|
| |Iron County|     0|  0.000| N/A|    17|  1679.012| N/A|  10,125|
| |Howard County|     0|  0.000| N/A|    46|  4599.540| N/A|  10,001|
| |Holt County|     0|  0.000| N/A|     6|  1362.707| N/A|   4,403|
| |Cedar County|     0|  0.000| N/A|    34|  2369.503| N/A|  14,349|
| |Dent County|     0|  0.000| N/A|     9|   577.923| N/A|  15,573|
| |Daviess County|     0|  0.000| N/A|    17|  2053.636| N/A|   8,278|
| |Dade County|     0|  0.000| N/A|    21|  2777.410| N/A|   7,561|
| |Crawford County|     0|  0.000| N/A|    57|  2382.943| N/A|  23,920|
| |Cooper County|     0|  0.000| N/A|    98|  5533.909| N/A|  17,709|
| |Clinton County|     0|  0.000| N/A|    65|  3188.306| N/A|  20,387|
| |Clark County|     0|  0.000| N/A|    14|  2059.732| N/A|   6,797|
| |Chariton County|     0|  0.000| N/A|    16|  2154.592| N/A|   7,426|
| |Barton County|     0|  0.000| N/A|    65|  5530.032| N/A|  11,754|
| |Texas County|     0|  0.000| N/A|    38|  1496.181| N/A|  25,398|
| |Reynolds County|     0|  0.000| N/A|    16|  2551.834| N/A|   6,270|
| |Warren County|     0|  0.000| N/A|   171|  4796.768| N/A|  35,649|
| |Vernon County|     0|  0.000| N/A|    46|  2237.028| N/A|  20,563|
| |Sullivan County|     0|  0.000| N/A|   136| 22335.359| N/A|   6,089|
| |Shelby County|     0|  0.000| N/A|    29|  4890.388| N/A|   5,930|
| |Monroe County|     0|  0.000| N/A|    21|  2429.431| N/A|   8,644|
| |Miller County|     0|  0.000| N/A|   104|  4059.487| N/A|  25,619|
| |Barry County|     0|  0.000| N/A|   230|  6426.556| N/A|  35,789|
| |Atchison County|     0|  0.000| N/A|    12|  2333.269| N/A|   5,143|
| |Adair County|     0|  0.000| N/A|   134|  5287.456| N/A|  25,343|
| |Bollinger County|     0|  0.000| N/A|    56|  4615.511| N/A|  12,133|
| |St. Louis city|     0|  0.000| N/A|     0|     0.000| N/A| 300,576|
| |Morgan County|     0|  0.000| N/A|    71|  3442.090| N/A|  20,627|
| |Schuyler County|     0|  0.000| N/A|     9|  1931.330| N/A|   4,660|
| |St. Clair County|     0|  0.000| N/A|    18|  1915.505| N/A|   9,397|
| |Ripley County|     0|  0.000| N/A|    45|  3386.514| N/A|  13,288|
| |Ralls County|     0|  0.000| N/A|    23|  2231.060| N/A|  10,309|
| |Worth County|     0|  0.000| N/A|     9|  4470.939| N/A|   2,013|
| |Polk County|     0|  0.000| N/A|   192|  5972.192| N/A|  32,149|
| |Phelps County|     0|  0.000| N/A|    74|  1660.198| N/A|  44,573|
| |Ozark County|     0|  0.000| N/A|     7|   763.026| N/A|   9,174|
| |Osage County|     0|  0.000| N/A|    42|  3084.833| N/A|  13,615|
| |Oregon County|     0|  0.000| N/A|    14|  1329.661| N/A|  10,529|
| |Nodaway County|     0|  0.000| N/A|   162|  7332.971| N/A|  22,092|
| |Montgomery County|     0|  0.000| N/A|    38|  3289.758| N/A|  11,551|
| |Wayne County|     0|  0.000| N/A|    37|  2874.233| N/A|  12,873|
| |Wright County|     0|  0.000| N/A|    58|  3171.305| N/A|  18,289|
| |Mississippi County|     0|  0.000| N/A|   131|  9939.302| N/A|  13,180|
| |Ray County|     0|  0.000| N/A|    96|  4170.649| N/A|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,074| 157.266| N/A|104,899| 15360.423| N/A|6,829,174|
| |Shelby County|   288| 307.309|  2.747|21,492| 22932.970| 286.181| 937,166|
| |Davidson County|   202| 291.006|  2.436|19,400| 27948.091| 180.527| 694,144|
| |Sumner County|    70| 365.950|  2.201| 3,178| 16614.127| 109.785| 191,283|
| |Rutherford County|    53| 159.502|  2.577| 6,072| 18273.470| 140.396| 332,285|
| |Hamilton County|    47| 127.785|  0.000| 5,661| 15391.350| 156.989| 367,804|
| |Knox County|    36| 76.545|  4.744| 4,032|  8573.014| 230.986| 470,313|
| |Williamson County|    22| 92.277|  0.000| 3,269| 13711.558| 255.860| 238,412|
| |Wilson County|    21| 145.171|  0.000| 2,072| 14323.538| 135.209| 144,657|
| |McMinn County|    20| 371.789|  0.000|   489|  9090.233| 185.894|  53,794|
| |Robertson County|    17| 236.726| 13.925| 1,450| 20191.330| 231.013|  71,813|
| |Madison County|    13| 132.675| 10.206|   912|  9307.642| 249.240|  97,984|
| |Hamblen County|    13| 200.203|  0.000| 1,229| 18926.910| 190.567|  64,934|
| |Putnam County|    13| 162.004|  0.000| 1,544| 19241.074| 55.853|  80,245|
| |Macon County|    13| 528.412|  0.000|   832| 33818.389| 70.269|  24,602|
| |Hardeman County|    11| 439.122|  0.000|   801| 31976.048| 410.291|  25,050|
| |Montgomery County|    11| 52.633|  0.000| 1,734|  8296.929| 136.368| 208,993|
| |Bradley County|    10| 92.498|  0.000| 1,713| 15844.973| 166.617| 108,110|
| |Bedford County|    10| 201.155|  0.000|   871| 17520.568| 268.066|  49,713|
| |Giles County|     9| 305.458| N/A|   351| 11912.843| N/A|  29,464|
| |Tipton County|     9| 146.106| N/A| 1,106| 17954.837| N/A|  61,599|
| |Monroe County|     9| 193.361| N/A|   366|  7863.358| N/A|  46,545|
| |Sullivan County|     9| 56.837| N/A|   806|  5090.055| N/A| 158,348|
| |Fayette County|     8| 194.491| N/A|   620| 15073.056| N/A|  41,133|
| |Blount County|     7| 52.597| N/A| 1,120|  8415.484| N/A| 133,088|
| |Hardin County|     7| 272.883| N/A|   401| 15632.309| N/A|  25,652|
| |Dyer County|     7| 188.380| N/A|   555| 14935.816| N/A|  37,159|
| |Trousdale County|     6| 531.726| N/A| 1,572| 139312.301| N/A|  11,284|
| |Lawrence County|     6| 135.925| N/A|   478| 10828.689| N/A|  44,142|
| |Lauderdale County|     6| 234.073| N/A|   423| 16502.165| N/A|  25,633|
| |Cumberland County|     6| 99.141| N/A|   379|  6262.393| N/A|  60,520|
| |Haywood County|     5| 288.951| N/A|   374| 21613.500| N/A|  17,304|
| |Greene County|     5| 72.391| N/A|   371|  5371.440| N/A|  69,069|
| |Maury County|     5| 51.874| N/A| 1,081| 11215.205| N/A|  96,387|
| |Sevier County|     5| 50.891| N/A| 1,713| 17435.115| N/A|  98,250|
| |McNairy County|     5| 194.598| N/A|   316| 12298.591| N/A|  25,694|
| |Carter County|     5| 88.667| N/A|   427|  7572.130| N/A|  56,391|
| |Anderson County|     5| 64.954| N/A|   607|  7885.370| N/A|  76,978|
| |Cheatham County|     5| 122.950| N/A|   548| 13475.299| N/A|  40,667|
| |Marion County|     4| 138.375| N/A|   205|  7091.708| N/A|  28,907|
| |Warren County|     4| 96.906| N/A|   403|  9763.306| N/A|  41,277|
| |Hawkins County|     4| 70.440| N/A|   362|  6374.811| N/A|  56,786|
| |Franklin County|     4| 94.769| N/A|   286|  6775.967| N/A|  42,208|
| |Obion County|     4| 133.027| N/A|   435| 14466.727| N/A|  30,069|
| |Crockett County|     3| 210.822| N/A|   226| 15881.940| N/A|  14,230|
| |Smith County|     3| 148.832| N/A|   363| 18008.632| N/A|  20,157|
| |Weakley County|     3| 90.014| N/A|   276|  8281.325| N/A|  33,328|
| |White County|     3| 109.709| N/A|   194|  7094.533| N/A|  27,345|
| |Carroll County|     3| 108.042| N/A|   228|  8211.186| N/A|  27,767|
| |Humphreys County|     3| 161.447| N/A|   105|  5650.630| N/A|  18,582|
| |Loudon County|     3| 55.486| N/A|   653| 12077.384| N/A|  54,068|
| |Washington County|     2| 15.459| N/A| 1,066|  8239.614| N/A| 129,375|
| |Roane County|     2| 37.466| N/A|   364|  6818.778| N/A|  53,382|
| |Marshall County|     2| 58.182| N/A|   265|  7709.091| N/A|  34,375|
| |Jefferson County|     2| 36.701| N/A|   496|  9101.752| N/A|  54,495|
| |Gibson County|     2| 40.706| N/A|   567| 11540.105| N/A|  49,133|
| |Coffee County|     2| 35.386| N/A|   417|  7377.919| N/A|  56,520|
| |Chester County|     2| 115.627| N/A|   193| 11158.004| N/A|  17,297|
| |Grundy County|     2| 148.954| N/A|   101|  7522.157| N/A|  13,427|
| |Decatur County|     2| 171.482| N/A|   161| 13804.339| N/A|  11,663|
| |Hancock County|     1| 151.057| N/A|    76| 11480.363| N/A|   6,620|
| |Pickett County|     1| 198.098| N/A|    22|  4358.162| N/A|   5,048|
| |Jackson County|     1| 84.846| N/A|   106|  8993.721| N/A|  11,786|
| |Polk County|     1| 59.411| N/A|   165|  9802.757| N/A|  16,832|
| |Rhea County|     1| 30.150| N/A|   502| 15135.526| N/A|  33,167|
| |Dickson County|     1| 18.536| N/A|   595| 11029.139| N/A|  53,948|
| |Overton County|     1| 44.962| N/A|   134|  6024.909| N/A|  22,241|
| |DeKalb County|     1| 48.804| N/A|   305| 14885.310| N/A|  20,490|
| |Lewis County|     1| 81.513| N/A|    56|  4564.721| N/A|  12,268|
| |Morgan County|     1| 46.722| N/A|    82|  3831.239| N/A|  21,403|
| |Lincoln County|     1| 29.099| N/A|   254|  7391.026| N/A|  34,366|
| |Campbell County|     1| 25.099| N/A|   213|  5346.117| N/A|  39,842|
| |Wayne County|     1| 59.977| N/A|   216| 12955.077| N/A|  16,673|
| |Benton County|     1| 61.881| N/A|    97|  6002.475| N/A|  16,160|
| |Bledsoe County|     1| 66.383| N/A|   672| 44609.665| N/A|  15,064|
| |Cocke County|     1| 27.775| N/A|   400| 11109.877| N/A|  36,004|
| |Perry County|     0|  0.000| N/A|    74|  9162.952| N/A|   8,076|
| |Moore County|     0|  0.000| N/A|    45|  6935.882| N/A|   6,488|
| |Cannon County|     0|  0.000| N/A|   118|  8039.242| N/A|  14,678|
| |Van Buren County|     0|  0.000| N/A|    33|  5619.891| N/A|   5,872|
| |Union County|     0|  0.000| N/A|   120|  6008.412| N/A|  19,972|
| |Unicoi County|     0|  0.000| N/A|   138|  7716.826| N/A|  17,883|
| |Scott County|     0|  0.000| N/A|   104|  4712.706| N/A|  22,068|
| |Sequatchie County|     0|  0.000| N/A|    94|  6255.823| N/A|  15,026|
| |Stewart County|     0|  0.000| N/A|    70|  5103.901| N/A|  13,715|
| |Lake County|     0|  0.000| N/A|   749| 106755.986| N/A|   7,016|
| |Henderson County|     0|  0.000| N/A|   431| 15328.805| N/A|  28,117|
| |Henry County|     0|  0.000| N/A|   216|  6678.003| N/A|  32,345|
| |Hickman County|     0|  0.000| N/A|   231|  9174.676| N/A|  25,178|
| |Houston County|     0|  0.000| N/A|    55|  6706.499| N/A|   8,201|
| |Johnson County|     0|  0.000| N/A|   172|  9669.440| N/A|  17,788|
| |Fentress County|     0|  0.000| N/A|    74|  3995.033| N/A|  18,523|
| |Clay County|     0|  0.000| N/A|    61|  8010.506| N/A|   7,615|
| |Meigs County|     0|  0.000| N/A|    98|  7889.229| N/A|  12,422|
| |Claiborne County|     0|  0.000| N/A|   221|  6915.110| N/A|  31,959|
| |Grainger County|     0|  0.000| N/A|   169|  7246.998| N/A|  23,320|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   949| 162.990| N/A|55,328|  9502.555| N/A|5,822,434|
| |Milwaukee County|   446| 471.595|  1.732|19,855| 20994.453| 194.519| 945,726|
| |Racine County|    76| 387.141|  0.000| 3,249| 16550.270| 147.725| 196,311|
| |Waukesha County|    55| 136.072|  1.445| 3,693|  9136.611| 138.187| 404,198|
| |Kenosha County|    53| 312.572|  0.000| 2,499| 14738.059| 147.440| 169,561|
| |Brown County|    51| 192.786|  0.000| 4,011| 15162.054| 104.017| 264,542|
| |Dane County|    37| 67.679|  0.000| 4,230|  7737.404| 85.034| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,371|  8392.816| 50.881| 163,354|
| |Washington County|    22| 161.724|  0.000|   880|  6468.971| 108.597| 136,034|
| |Walworth County|    21| 202.180|  0.000| 1,258| 12111.526| 161.447| 103,868|
| |Winnebago County|    18| 104.708|  2.420| 1,063|  6183.576| 80.038| 171,907|
| |Ozaukee County|    17| 190.538|  1.758|   568|  6366.214| 101.815|  89,221|
| |Waupaca County|    15| 294.175|  3.077|   379|  7432.830| 193.250|  50,990|
| |Grant County|    14| 272.167|  0.000|   329|  6395.925| 79.091|  51,439|
| |Outagamie County|    13| 69.191|  0.000| 1,113|  5923.836| 94.414| 187,885|
| |Clark County|     7| 201.300| N/A|   177|  5090.010| N/A|  34,774|
| |Fond du Lac County|     6| 58.025| N/A|   571|  5522.083| N/A| 103,403|
| |Marathon County|     6| 44.218| N/A|   580|  4274.386| N/A| 135,692|
| |Sheboygan County|     5| 43.350| N/A|   622|  5392.752| N/A| 115,340|
| |Jefferson County|     5| 58.984| N/A|   564|  6653.376| N/A|  84,769|
| |Dodge County|     5| 56.922| N/A|   705|  8026.048| N/A|  87,839|
| |Forest County|     4| 444.247| N/A|    59|  6552.643| N/A|   9,004|
| |Richland County|     4| 231.857| N/A|    32|  1854.857| N/A|  17,252|
| |Marinette County|     3| 74.349| N/A|   331|  8203.222| N/A|  40,350|
| |Eau Claire County|     3| 28.668| N/A|   507|  4844.906| N/A| 104,646|
| |Barron County|     3| 66.307| N/A|   259|  5724.516| N/A|  45,244|
| |Sauk County|     3| 46.553| N/A|   392|  6082.989| N/A|  64,442|
| |Door County|     3| 108.429| N/A|    85|  3072.141| N/A|  27,668|
| |Trempealeau County|     2| 67.456| N/A|   307| 10354.481| N/A|  29,649|
| |Calumet County|     2| 39.929| N/A|   258|  5150.832| N/A|  50,089|
| |Adams County|     2| 98.912| N/A|    73|  3610.287| N/A|  20,220|
| |St. Croix County|     2| 22.054| N/A|   452|  4984.176| N/A|  90,687|
| |Polk County|     2| 45.680| N/A|   120|  2740.790| N/A|  43,783|
| |Kewaunee County|     2| 97.876| N/A|   110|  5383.185| N/A|  20,434|
| |Buffalo County|     2| 153.480| N/A|    41|  3146.343| N/A|  13,031|
| |Monroe County|     1| 21.620| N/A|   226|  4886.170| N/A|  46,253|
| |Marquette County|     1| 64.210| N/A|    71|  4558.880| N/A|  15,574|
| |Burnett County|     1| 64.876| N/A|    18|  1167.770| N/A|  15,414|
| |Jackson County|     1| 48.443| N/A|    49|  2373.686| N/A|  20,643|
| |Bayfield County|     1| 66.507| N/A|    20|  1330.141| N/A|  15,036|
| |Juneau County|     1| 37.471| N/A|   129|  4833.814| N/A|  26,687|
| |Green County|     1| 27.056| N/A|   131|  3544.372| N/A|  36,960|
| |Iron County|     1| 175.840| N/A|    72| 12660.454| N/A|   5,687|
| |Langlade County|     1| 52.113| N/A|    49|  2553.546| N/A|  19,189|
| |La Crosse County|     1|  8.473| N/A|   825|  6990.578| N/A| 118,016|
| |Manitowoc County|     1| 12.661| N/A|   306|  3874.350| N/A|  78,981|
| |Wood County|     1| 13.699| N/A|   241|  3301.415| N/A|  72,999|
| |Rusk County|     1| 70.532| N/A|    16|  1128.509| N/A|  14,178|
| |Columbia County|     1| 17.382| N/A|   227|  3945.630| N/A|  57,532|
| |Lincoln County|     0|  0.000| N/A|    64|  2319.429| N/A|  27,593|
| |Ashland County|     0|  0.000| N/A|    20|  1285.182| N/A|  15,562|
| |Douglas County|     0|  0.000| N/A|   135|  3128.621| N/A|  43,150|
| |Dunn County|     0|  0.000| N/A|   105|  2314.407| N/A|  45,368|
| |Florence County|     0|  0.000| N/A|     7|  1629.802| N/A|   4,295|
| |Chippewa County|     0|  0.000| N/A|   210|  3247.858| N/A|  64,658|
| |Pierce County|     0|  0.000| N/A|   174|  4069.795| N/A|  42,754|
| |Washburn County|     0|  0.000| N/A|    35|  2226.463| N/A|  15,720|
| |Vilas County|     0|  0.000| N/A|    38|  1712.097| N/A|  22,195|
| |Waushara County|     0|  0.000| N/A|   107|  4377.531| N/A|  24,443|
| |Green Lake County|     0|  0.000| N/A|    52|  2749.432| N/A|  18,913|
| |Pepin County|     0|  0.000| N/A|    40|  5489.227| N/A|   7,287|
| |Crawford County|     0|  0.000| N/A|    62|  3843.531| N/A|  16,131|
| |Taylor County|     0|  0.000| N/A|    54|  2654.476| N/A|  20,343|
| |Iowa County|     0|  0.000| N/A|    65|  2745.164| N/A|  23,678|
| |Lafayette County|     0|  0.000| N/A|   110|  6600.660| N/A|  16,665|
| |Price County|     0|  0.000| N/A|    21|  1572.916| N/A|  13,351|
| |Menominee County|     0|  0.000| N/A|    20|  4389.816| N/A|   4,556|
| |Oconto County|     0|  0.000| N/A|   183|  4824.677| N/A|  37,930|
| |Oneida County|     0|  0.000| N/A|    89|  2500.351| N/A|  35,595|
| |Portage County|     0|  0.000| N/A|   355|  5016.108| N/A|  70,772|
| |Sawyer County|     0|  0.000| N/A|    40|  2415.751| N/A|  16,558|
| |Vernon County|     0|  0.000| N/A|    58|  1881.773| N/A|  30,822|
| |Shawano County|     0|  0.000| N/A|   161|  3936.527| N/A|  40,899|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   884| 280.184| N/A|45,897| 14547.062| N/A|3,155,070|
| |Polk County|   203| 414.150|  1.169| 9,723| 19836.339| 116.288| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,108|  9298.386| 128.560| 226,706|
| |Black Hawk County|    62| 472.460|  0.000| 3,003| 22883.836| 72.393| 131,228|
| |Woodbury County|    51| 494.632|  8.177| 3,651| 35409.817| 96.987| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   826| 19360.585| 138.967|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,789| 19143.313| 117.706|  93,453|
| |Wapello County|    32| 915.096| 28.597|   849| 24278.647| 199.847|  34,969|
| |Dubuque County|    29| 298.014|  1.612| 1,537| 15794.720| 174.698|  97,311|
| |Tama County|    29| 1720.660|  0.000|   537| 31861.873| 59.844|  16,854|
| |Marshall County|    24| 609.617|  0.000| 1,389| 35281.567| 137.374|  39,369|
| |Jasper County|    24| 645.422|  0.000|   455| 12236.117| 80.678|  37,185|
| |Pottawattamie County|    23| 246.765|  8.758| 1,217| 13057.099| 547.175|  93,206|
| |Mahaska County|    17| 769.405|  0.000|   136|  6155.239| 31.759|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   576| 13568.905| 93.419|  42,450|
| |Johnson County|    15| 99.246|  0.000| 1,933| 12789.467| 110.396| 151,140|
| |Louisa County|    14| 1268.691|  0.000|   379| 34345.265| 62.189|  11,035|
| |Story County|    14| 144.156|  0.000| 1,109| 11419.216| 56.007|  97,117|
| |Buena Vista County|    12| 611.621|  0.000| 1,785| 90978.593| 50.968|  19,620|
| |Scott County|    12| 69.387|  0.000| 1,593|  9211.127| 59.253| 172,943|
| |Washington County|    10| 455.270|  0.000|   287| 13066.242|  0.000|  21,965|
| |Poweshiek County|     8| 432.339| N/A|   146|  7890.186| N/A|  18,504|
| |Plymouth County|     8| 317.750| N/A|   443| 17595.424| N/A|  25,177|
| |Monroe County|     7| 908.265| N/A|    67|  8693.396| N/A|   7,707|
| |Bremer County|     7| 279.307| N/A|   187|  7461.495| N/A|  25,062|
| |Franklin County|     5| 496.524| N/A|   220| 21847.071| N/A|  10,070|
| |Guthrie County|     5| 467.771| N/A|   126| 11787.819| N/A|  10,689|
| |Webster County|     5| 139.260| N/A|   725| 20192.736| N/A|  35,904|
| |Allamakee County|     4| 292.248| N/A|   151| 11032.366| N/A|  13,687|
| |Dickinson County|     4| 231.777| N/A|   375| 21729.053| N/A|  17,258|
| |Lucas County|     4| 465.116| N/A|    45|  5232.558| N/A|   8,600|
| |Appanoose County|     3| 241.429| N/A|    42|  3380.010| N/A|  12,426|
| |Clarke County|     3| 319.319| N/A|   186| 19797.765| N/A|   9,395|
| |Lee County|     3| 89.135| N/A|    95|  2822.593| N/A|  33,657|
| |Crawford County|     3| 178.359| N/A|   719| 42746.730| N/A|  16,820|
| |Clinton County|     3| 64.615| N/A|   317|  6827.629| N/A|  46,429|
| |Montgomery County|     3| 302.511| N/A|    43|  4335.989| N/A|   9,917|
| |Clayton County|     3| 170.950| N/A|    98|  5584.364| N/A|  17,549|
| |Henry County|     3| 150.346| N/A|   113|  5663.025| N/A|  19,954|
| |Madison County|     2| 122.414| N/A|   102|  6243.114| N/A|  16,338|
| |Jones County|     2| 96.707| N/A|   124|  5995.842| N/A|  20,681|
| |Hancock County|     2| 188.147| N/A|   117| 11006.585| N/A|  10,630|
| |Floyd County|     2| 127.861| N/A|   129|  8247.027| N/A|  15,642|
| |Sioux County|     2| 57.381| N/A|   595| 17070.722| N/A|  34,855|
| |Des Moines County|     2| 51.325| N/A|   139|  3567.121| N/A|  38,967|
| |Boone County|     2| 76.237| N/A|   228|  8691.012| N/A|  26,234|
| |Calhoun County|     2| 206.868| N/A|    82|  8481.589| N/A|   9,668|
| |Butler County|     2| 138.514| N/A|   114|  7895.284| N/A|  14,439|
| |Grundy County|     1| 81.753| N/A|    74|  6049.706| N/A|  12,232|
| |Cedar County|     1| 53.686| N/A|   120|  6442.261| N/A|  18,627|
| |Emmet County|     1| 108.601| N/A|   179| 19439.618| N/A|   9,208|
| |Cass County|     1| 77.906| N/A|    48|  3739.483| N/A|  12,836|
| |Carroll County|     1| 49.591| N/A|   181|  8975.948| N/A|  20,165|
| |Buchanan County|     1| 47.226| N/A|   111|  5242.031| N/A|  21,175|
| |Benton County|     1| 38.994| N/A|   143|  5576.136| N/A|  25,645|
| |Audubon County|     1| 181.951| N/A|    28|  5094.614| N/A|   5,496|
| |Cherokee County|     1| 89.008| N/A|    97|  8633.734| N/A|  11,235|
| |Clay County|     1| 62.438| N/A|   171| 10676.823| N/A|  16,016|
| |Davis County|     1| 111.111| N/A|    48|  5333.333| N/A|   9,000|
| |Delaware County|     1| 58.785| N/A|    90|  5290.694| N/A|  17,011|
| |Iowa County|     1| 61.789| N/A|    89|  5499.259| N/A|  16,184|
| |Jackson County|     1| 51.443| N/A|   141|  7253.460| N/A|  19,439|
| |Keokuk County|     1| 97.599| N/A|    30|  2927.972| N/A|  10,246|
| |Humboldt County|     1| 104.624| N/A|    92|  9625.445| N/A|   9,558|
| |Wayne County|     1| 155.255| N/A|    16|  2484.086| N/A|   6,441|
| |O'Brien County|     1| 72.711| N/A|   131|  9525.195| N/A|  13,753|
| |Pocahontas County|     1| 151.080| N/A|   113| 17072.065| N/A|   6,619|
| |Shelby County|     1| 87.306| N/A|   161| 14056.225| N/A|  11,454|
| |Union County|     1| 81.693| N/A|    70|  5718.487| N/A|  12,241|
| |Hamilton County|     1| 67.691| N/A|   241| 16313.545| N/A|  14,773|
| |Ringgold County|     1| 204.332| N/A|    21|  4290.969| N/A|   4,894|
| |Van Buren County|     1| 141.965| N/A|    32|  4542.873| N/A|   7,044|
| |Warren County|     1| 19.430| N/A|   528| 10259.200| N/A|  51,466|
| |Winneshiek County|     1| 50.023| N/A|    85|  4251.913| N/A|  19,991|
| |Wright County|     1| 79.605| N/A|   443| 35265.085| N/A|  12,562|
| |Adams County|     0|  0.000| N/A|    16|  4441.977| N/A|   3,602|
| |Howard County|     0|  0.000| N/A|    48|  5241.319| N/A|   9,158|
| |Harrison County|     0|  0.000| N/A|    97|  6904.406| N/A|  14,049|
| |Hardin County|     0|  0.000| N/A|   165|  9794.610| N/A|  16,846|
| |Greene County|     0|  0.000| N/A|    38|  4275.428| N/A|   8,888|
| |Fremont County|     0|  0.000| N/A|    35|  5028.736| N/A|   6,960|
| |Fayette County|     0|  0.000| N/A|    81|  4122.137| N/A|  19,650|
| |Decatur County|     0|  0.000| N/A|    22|  2795.426| N/A|   7,870|
| |Chickasaw County|     0|  0.000| N/A|    51|  4273.862| N/A|  11,933|
| |Adair County|     0|  0.000| N/A|    21|  2936.242| N/A|   7,152|
| |Ida County|     0|  0.000| N/A|    29|  4227.405| N/A|   6,860|
| |Lyon County|     0|  0.000| N/A|   102|  8677.159| N/A|  11,755|
| |Kossuth County|     0|  0.000| N/A|    78|  5265.645| N/A|  14,813|
| |Jefferson County|     0|  0.000| N/A|    77|  4208.800| N/A|  18,295|
| |Worth County|     0|  0.000| N/A|    61|  8264.463| N/A|   7,381|
| |Taylor County|     0|  0.000| N/A|    93| 15193.596| N/A|   6,121|
| |Sac County|     0|  0.000| N/A|    81|  8332.476| N/A|   9,721|
| |Palo Alto County|     0|  0.000| N/A|    79|  8890.389| N/A|   8,886|
| |Page County|     0|  0.000| N/A|    76|  5030.780| N/A|  15,107|
| |Osceola County|     0|  0.000| N/A|    77| 12923.800| N/A|   5,958|
| |Monona County|     0|  0.000| N/A|    90| 10446.895| N/A|   8,615|
| |Mitchell County|     0|  0.000| N/A|    76|  7179.293| N/A|  10,586|
| |Mills County|     0|  0.000| N/A|    82|  5427.229| N/A|  15,109|
| |Marion County|     0|  0.000| N/A|   153|  4601.089| N/A|  33,253|
| |Winnebago County|     0|  0.000| N/A|    76|  7340.158| N/A|  10,354|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   840| 272.713| N/A|50,881| 16518.969| N/A|3,080,156|
| |Clark County|   702| 309.699|  3.088|44,066| 19440.468| 416.790|2,266,715|
| |Washoe County|   115| 243.893|  1.220| 5,343| 11331.463| 166.483| 471,519|
| |Nye County|     9| 193.453| N/A|   356|  7652.129| N/A|  46,523|
| |Lyon County|     5| 86.941| N/A|   206|  3581.986| N/A|  57,510|
| |Humboldt County|     4| 237.657| N/A|    96|  5703.761| N/A|  16,831|
| |Elko County|     2| 37.895| N/A|   488|  9246.277| N/A|  52,778|
| |Churchill County|     1| 40.146| N/A|    48|  1927.014| N/A|  24,909|
| |Lander County|     1| 180.766| N/A|    50|  9038.322| N/A|   5,532|
| |White Pine County|     1| 104.384| N/A|    14|  1461.378| N/A|   9,580|
| |Carson City|     0|  0.000| N/A|     0|     0.000| N/A|  55,916|
| |Eureka County|     0|  0.000| N/A|     2|   985.707| N/A|   2,029|
| |Esmeralda County|     0|  0.000| N/A|     0|     0.000| N/A|     873|
| |Douglas County|     0|  0.000| N/A|   180|  3680.605| N/A|  48,905|
| |Lincoln County|     0|  0.000| N/A|     4|   771.754| N/A|   5,183|
| |Storey County|     0|  0.000| N/A|     4|   970.167| N/A|   4,123|
| |Pershing County|     0|  0.000| N/A|    13|  1933.086| N/A|   6,725|
| |Mineral County|     0|  0.000| N/A|    11|  2441.731| N/A|   4,505|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   744| 166.530| N/A|31,508|  7052.441| N/A|4,467,673|
| |Jefferson County|   233| 303.877|  0.279| 7,206|  9398.023| 123.086| 766,757|
| |Fayette County|    46| 142.348|  0.000| 2,807|  8686.315| 164.429| 323,152|
| |Kenton County|    37| 221.560|  0.000| 1,323|  7922.251| 77.845| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   403|  9018.485| 47.533|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,021|  7643.303| 74.187| 133,581|
| |Shelby County|    22| 448.760|  0.000|   711| 14503.101| 80.909|  49,024|
| |Logan County|    22| 811.748|  0.000|   302| 11143.089| 47.800|  27,102|
| |Graves County|    22| 590.350|  0.000|   511| 13712.231| 140.145|  37,266|
| |Warren County|    22| 165.543|  0.000| 2,451| 18442.993| 240.790| 132,896|
| |Adair County|    19| 989.480|  0.000|   203| 10571.815| 44.675|  19,202|
| |Butler County|    15| 1164.687|  0.000|   295| 22905.505| 232.937|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   143| 10728.487| 95.303|  13,329|
| |Oldham County|    14| 209.584| 13.440|   575|  8607.913| 217.069|  66,799|
| |Campbell County|    13| 138.913|  0.000|   525|  5609.933| 84.415|  93,584|
| |Edmonson County|    12| 987.654|  0.000|    95|  7818.930| 164.609|  12,150|
| |Grayson County|    11| 416.241|  0.000|   181|  6849.056| 91.174|  26,427|
| |Casey County|    10| 618.850|  0.000|   154|  9530.293| 154.713|  16,159|
| |Muhlenberg County|    10| 326.563| 13.949|   612| 19985.631| 32.656|  30,622|
| |Gallatin County|     8| 902.018| N/A|    79|  8907.430| N/A|   8,869|
| |Hardin County|     8| 72.099| N/A|   522|  4704.483| N/A| 110,958|
| |Knox County|     8| 256.863| N/A|   201|  6453.684| N/A|  31,145|
| |Allen County|     8| 375.323| N/A|   217| 10180.624| N/A|  21,315|
| |Simpson County|     7| 376.911| N/A|   139|  7484.385| N/A|  18,572|
| |Daviess County|     7| 68.958| N/A|   715|  7043.572| N/A| 101,511|
| |Clark County|     7| 193.034| N/A|   156|  4301.906| N/A|  36,263|
| |Christian County|     6| 85.153| N/A|   476|  6755.510| N/A|  70,461|
| |Ohio County|     6| 250.063| N/A|   340| 14170.209| N/A|  23,994|
| |Grant County|     5| 199.450| N/A|   101|  4028.880| N/A|  25,069|
| |Clay County|     5| 251.244| N/A|   143|  7185.569| N/A|  19,901|
| |Russell County|     5| 278.971| N/A|   100|  5579.423| N/A|  17,923|
| |Franklin County|     5| 98.057| N/A|   257|  5040.105| N/A|  50,991|
| |McCracken County|     4| 61.145| N/A|   334|  5105.628| N/A|  65,418|
| |Lyon County|     4| 487.211| N/A|    30|  3654.080| N/A|   8,210|
| |Laurel County|     4| 65.775| N/A|   374|  6150.001| N/A|  60,813|
| |Bullitt County|     4| 48.974| N/A|   315|  3856.702| N/A|  81,676|
| |Henderson County|     4| 88.476| N/A|   324|  7166.556| N/A|  45,210|
| |Boyd County|     3| 64.215| N/A|   174|  3724.475| N/A|  46,718|
| |Pike County|     3| 51.835| N/A|   219|  3783.952| N/A|  57,876|
| |Perry County|     3| 116.469| N/A|   189|  7337.526| N/A|  25,758|
| |Harlan County|     3| 115.340| N/A|   207|  7958.478| N/A|  26,010|
| |Calloway County|     3| 76.921| N/A|   196|  5025.512| N/A|  39,001|
| |Taylor County|     2| 77.613| N/A|   101|  3919.438| N/A|  25,769|
| |Bell County|     2| 76.829| N/A|   281| 10794.407| N/A|  26,032|
| |Barren County|     2| 45.199| N/A|   334|  7548.193| N/A|  44,249|
| |Breckinridge County|     2| 97.671| N/A|    52|  2539.434| N/A|  20,477|
| |Metcalfe County|     2| 198.590| N/A|    51|  5064.045| N/A|  10,071|
| |Meade County|     2| 69.999| N/A|    85|  2974.941| N/A|  28,572|
| |Marshall County|     2| 64.309| N/A|   125|  4019.293| N/A|  31,100|
| |Monroe County|     2| 187.793| N/A|    88|  8262.911| N/A|  10,650|
| |Nelson County|     2| 43.259| N/A|   190|  4109.619| N/A|  46,233|
| |Pulaski County|     2| 30.779| N/A|   260|  4001.293| N/A|  64,979|
| |Carroll County|     2| 188.129| N/A|   142| 13357.163| N/A|  10,631|
| |Floyd County|     2| 56.197| N/A|    83|  2332.181| N/A|  35,589|
| |Green County|     2| 182.799| N/A|    30|  2741.980| N/A|  10,941|
| |Henry County|     2| 124.023| N/A|    94|  5829.096| N/A|  16,126|
| |Knott County|     1| 67.540| N/A|    45|  3039.308| N/A|  14,806|
| |Madison County|     1| 10.754| N/A|   396|  4258.660| N/A|  92,987|
| |Mason County|     1| 58.582| N/A|    53|  3104.862| N/A|  17,070|
| |McLean County|     1| 108.613| N/A|    38|  4127.294| N/A|   9,207|
| |Livingston County|     1| 108.767| N/A|    32|  3480.531| N/A|   9,194|
| |Lincoln County|     1| 40.735| N/A|    99|  4032.751| N/A|  24,549|
| |Larue County|     1| 69.454| N/A|    51|  3542.159| N/A|  14,398|
| |Greenup County|     1| 28.492| N/A|    89|  2535.757| N/A|  35,098|
| |Fulton County|     1| 167.532| N/A|    60| 10051.935| N/A|   5,969|
| |Webster County|     1| 77.268| N/A|    81|  6258.693| N/A|  12,942|
| |Bath County|     1| 80.000| N/A|    35|  2800.000| N/A|  12,500|
| |Anderson County|     1| 43.962| N/A|    75|  3297.138| N/A|  22,747|
| |Bourbon County|     1| 50.536| N/A|    69|  3486.962| N/A|  19,788|
| |Carlisle County|     1| 210.084| N/A|    31|  6512.605| N/A|   4,760|
| |Whitley County|     1| 27.576| N/A|   144|  3970.880| N/A|  36,264|
| |Carter County|     1| 37.318| N/A|    95|  3545.173| N/A|  26,797|
| |Crittenden County|     1| 113.559| N/A|    26|  2952.532| N/A|   8,806|
| |Trigg County|     0|  0.000| N/A|    50|  3412.736| N/A|  14,651|
| |Owsley County|     0|  0.000| N/A|    10|  2265.006| N/A|   4,415|
| |Todd County|     0|  0.000| N/A|    33|  2684.236| N/A|  12,294|
| |Spencer County|     0|  0.000| N/A|   102|  5271.045| N/A|  19,351|
| |Scott County|     0|  0.000| N/A|   330|  5789.067| N/A|  57,004|
| |Rowan County|     0|  0.000| N/A|    68|  2780.049| N/A|  24,460|
| |Rockcastle County|     0|  0.000| N/A|    61|  3653.789| N/A|  16,695|
| |Robertson County|     0|  0.000| N/A|     3|  1423.150| N/A|   2,108|
| |Powell County|     0|  0.000| N/A|    50|  4045.635| N/A|  12,359|
| |Pendleton County|     0|  0.000| N/A|    36|  2467.443| N/A|  14,590|
| |Union County|     0|  0.000| N/A|    54|  3754.954| N/A|  14,381|
| |Washington County|     0|  0.000| N/A|    64|  5291.443| N/A|  12,095|
| |Wayne County|     0|  0.000| N/A|    53|  2606.600| N/A|  20,333|
| |Jessamine County|     0|  0.000| N/A|   300|  5543.749| N/A|  54,115|
| |Menifee County|     0|  0.000| N/A|    29|  4469.102| N/A|   6,489|
| |Martin County|     0|  0.000| N/A|    30|  2679.768| N/A|  11,195|
| |Marion County|     0|  0.000| N/A|   110|  5707.466| N/A|  19,273|
| |Magoffin County|     0|  0.000| N/A|    23|  1891.292| N/A|  12,161|
| |McCreary County|     0|  0.000| N/A|    37|  2147.293| N/A|  17,231|
| |Lewis County|     0|  0.000| N/A|    36|  2711.864| N/A|  13,275|
| |Leslie County|     0|  0.000| N/A|    26|  2632.378| N/A|   9,877|
| |Nicholas County|     0|  0.000| N/A|    20|  2751.410| N/A|   7,269|
| |Lee County|     0|  0.000| N/A|     4|   540.321| N/A|   7,403|
| |Lawrence County|     0|  0.000| N/A|    33|  2154.469| N/A|  15,317|
| |Johnson County|     0|  0.000| N/A|    39|  1757.707| N/A|  22,188|
| |Hickman County|     0|  0.000| N/A|    34|  7762.557| N/A|   4,380|
| |Wolfe County|     0|  0.000| N/A|    11|  1536.957| N/A|   7,157|
| |Hart County|     0|  0.000| N/A|    80|  4202.784| N/A|  19,035|
| |Harrison County|     0|  0.000| N/A|   116|  6142.116| N/A|  18,886|
| |Hancock County|     0|  0.000| N/A|    47|  5388.672| N/A|   8,722|
| |Morgan County|     0|  0.000| N/A|    30|  2254.114| N/A|  13,309|
| |Owen County|     0|  0.000| N/A|    42|  3852.858| N/A|  10,901|
| |Trimble County|     0|  0.000| N/A|    32|  3777.594| N/A|   8,471|
| |Woodford County|     0|  0.000| N/A|   133|  4974.938| N/A|  26,734|
| |Montgomery County|     0|  0.000| N/A|   113|  4013.212| N/A|  28,157|
| |Mercer County|     0|  0.000| N/A|    74|  3373.911| N/A|  21,933|
| |Letcher County|     0|  0.000| N/A|    51|  2366.260| N/A|  21,553|
| |Cumberland County|     0|  0.000| N/A|    40|  6047.777| N/A|   6,614|
| |Clinton County|     0|  0.000| N/A|    27|  2642.396| N/A|  10,218|
| |Caldwell County|     0|  0.000| N/A|    49|  3844.042| N/A|  12,747|
| |Breathitt County|     0|  0.000| N/A|    26|  2058.591| N/A|  12,630|
| |Bracken County|     0|  0.000| N/A|    29|  3492.713| N/A|   8,303|
| |Boyle County|     0|  0.000| N/A|   137|  4557.552| N/A|  30,060|
| |Ballard County|     0|  0.000| N/A|    31|  3930.020| N/A|   7,888|
| |Garrard County|     0|  0.000| N/A|    68|  3849.202| N/A|  17,666|
| |Elliott County|     0|  0.000| N/A|     8|  1064.254| N/A|   7,517|
| |Estill County|     0|  0.000| N/A|    12|   850.702| N/A|  14,106|
| |Fleming County|     0|  0.000| N/A|    56|  3840.614| N/A|  14,581|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   655| 312.376| N/A|19,862|  9472.399| N/A|2,096,829|
| |McKinley County|   221| 3096.669|  8.158| 4,004| 56104.362| 154.133|  71,367|
| |San Juan County|   181| 1460.172|  4.034| 3,003| 24225.947| 20.177| 123,958|
| |Bernalillo County|   123| 181.116|  1.140| 4,879|  7184.287| 63.336| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,096|  7468.586| 52.788| 146,748|
| |Dona Ana County|    24| 109.993|  3.538| 2,240| 10266.046| 112.329| 218,195|
| |Cibola County|    17| 637.301|  0.000|   340| 12746.017| 149.953|  26,675|
| |Otero County|    10| 148.170|  0.000|   188|  2785.598| 33.573|  67,490|
| |Chaves County|     6| 92.858| N/A|   367|  5679.796| N/A|  64,615|
| |Socorro County|     6| 360.642| N/A|    73|  4387.810| N/A|  16,637|
| |Rio Arriba County|     5| 128.465| N/A|   296|  7605.149| N/A|  38,921|
| |Valencia County|     4| 52.159| N/A|   373|  4863.864| N/A|  76,688|
| |Lea County|     4| 56.283| N/A|   656|  9230.336| N/A|  71,070|
| |Eddy County|     4| 68.423| N/A|   258|  4413.274| N/A|  58,460|
| |Luna County|     3| 126.534| N/A|   235|  9911.848| N/A|  23,709|
| |Santa Fe County|     3| 19.952| N/A|   597|  3970.524| N/A| 150,358|
| |Grant County|     2| 74.080| N/A|    68|  2518.705| N/A|  26,998|
| |Curry County|     2| 40.855| N/A|   483|  9866.405| N/A|  48,954|
| |Roosevelt County|     1| 54.054| N/A|   142|  7675.676| N/A|  18,500|
| |Quay County|     1| 121.168| N/A|    33|  3998.546| N/A|   8,253|
| |Catron County|     1| 283.527| N/A|     4|  1134.108| N/A|   3,527|
| |Colfax County|     1| 83.745| N/A|    14|  1172.431| N/A|  11,941|
| |Torrance County|     1| 64.679| N/A|    60|  3880.732| N/A|  15,461|
| |Lincoln County|     1| 51.093| N/A|   109|  5569.180| N/A|  19,572|
| |Taos County|     1| 30.560| N/A|    99|  3025.395| N/A|  32,723|
| |Sierra County|     0|  0.000| N/A|    30|  2780.095| N/A|  10,791|
| |Union County|     0|  0.000| N/A|    27|  6651.885| N/A|   4,059|
| |San Miguel County|     0|  0.000| N/A|    42|  1539.759| N/A|  27,277|
| |Mora County|     0|  0.000| N/A|     6|  1327.140| N/A|   4,521|
| |Los Alamos County|     0|  0.000| N/A|    20|  1032.578| N/A|  19,369|
| |Hidalgo County|     0|  0.000| N/A|    88| 20962.363| N/A|   4,198|
| |Harding County|     0|  0.000| N/A|     1|  1600.000| N/A|     625|
| |Guadalupe County|     0|  0.000| N/A|    31|  7209.302| N/A|   4,300|
| |De Baca County|     0|  0.000| N/A|     0|     0.000| N/A|   1,748|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   586| 830.324| N/A|12,313| 17446.713| N/A| 705,749|
| |District of Columbia|   586| 830.324|  0.000|12,313| 17446.713|  0.000| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   585| 600.762| N/A|14,826| 15225.455| N/A| 973,764|
| |New Castle County|   287| 513.644|  0.000| 6,938| 12416.936| 87.695| 558,753|
| |Sussex County|   191| 815.455|  0.000| 5,673| 24220.301| 92.342| 234,225|
| |Kent County|   107| 591.860|  8.677| 2,215| 12252.055| 88.502| 180,786|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   551| 139.248| N/A|38,586|  9751.398| N/A|3,956,971|
| |Tulsa County|   101| 155.014|  1.160| 9,159| 14057.205| 223.108| 651,552|
| |Oklahoma County|    98| 122.894|  0.000| 9,439| 11836.716| 198.970| 797,434|
| |Cleveland County|    49| 172.527|  0.000| 2,725|  9594.597| 164.051| 284,014|
| |Washington County|    39| 756.885|  0.000|   575| 11159.198| 109.191|  51,527|
| |McCurtain County|    25| 761.452|  0.000|   829| 25249.756| 156.075|  32,832|
| |Wagoner County|    22| 270.639|  0.000|   738|  9078.719| 146.169|  81,289|
| |Delaware County|    19| 441.768|  0.000|   403|  9370.132| 72.934|  43,009|
| |Muskogee County|    16| 235.304|  0.000|   448|  6588.526| 132.443|  67,997|
| |Caddo County|    14| 486.753|  0.000|   373| 12968.500| 243.377|  28,762|
| |Rogers County|    14| 151.418|  0.000|   823|  8901.243| 243.675|  92,459|
| |Creek County|    13| 181.762|  0.000|   500|  6990.856| 122.886|  71,522|
| |Osage County|    11| 234.227|  0.000|   367|  7814.663| 93.398|  46,963|
| |Kay County|    10| 229.684|  0.000|   217|  4984.152| 58.587|  43,538|
| |Comanche County|    10| 82.816|  0.000|   778|  6443.118| 49.690| 120,749|
| |Pottawatomie County|     8| 110.205| N/A|   400|  5510.249| N/A|  72,592|
| |Greer County|     8| 1400.560| N/A|    81| 14180.672| N/A|   5,712|
| |Texas County|     7| 350.298| N/A| 1,036| 51844.067| N/A|  19,983|
| |Grady County|     6| 107.461| N/A|   412|  7379.016| N/A|  55,834|
| |Mayes County|     6| 145.985| N/A|   285|  6934.307| N/A|  41,100|
| |Canadian County|     5| 33.714| N/A| 1,089|  7342.926| N/A| 148,306|
| |Seminole County|     5| 206.118| N/A|   193|  7956.138| N/A|  24,258|
| |Adair County|     5| 225.286| N/A|   305| 13742.453| N/A|  22,194|
| |Sequoyah County|     4| 96.226| N/A|   264|  6350.886| N/A|  41,569|
| |McClain County|     4| 98.829| N/A|   397|  9808.766| N/A|  40,474|
| |Jackson County|     4| 163.066| N/A|   486| 19812.475| N/A|  24,530|
| |Garvin County|     4| 144.347| N/A|   208|  7506.045| N/A|  27,711|
| |Garfield County|     4| 65.514| N/A|   372|  6092.767| N/A|  61,056|
| |Pawnee County|     3| 183.195| N/A|   122|  7449.927| N/A|  16,376|
| |Payne County|     3| 36.682| N/A|   672|  8216.766| N/A|  81,784|
| |Pittsburg County|     3| 68.722| N/A|   201|  4604.389| N/A|  43,654|
| |Okmulgee County|     3| 77.993| N/A|   396| 10295.073| N/A|  38,465|
| |Carter County|     3| 62.356| N/A|   308|  6401.862| N/A|  48,111|
| |Lincoln County|     2| 57.344| N/A|   132|  3784.729| N/A|  34,877|
| |Noble County|     2| 179.678| N/A|    77|  6917.617| N/A|  11,131|
| |Pontotoc County|     2| 52.241| N/A|   177|  4623.341| N/A|  38,284|
| |Ottawa County|     2| 64.253| N/A|   347| 11147.878| N/A|  31,127|
| |Stephens County|     2| 46.357| N/A|   175|  4056.278| N/A|  43,143|
| |Cotton County|     2| 352.983| N/A|    17|  3000.353| N/A|   5,666|
| |Tillman County|     1| 137.931| N/A|    56|  7724.138| N/A|   7,250|
| |Nowata County|     1| 99.246| N/A|    56|  5557.761| N/A|  10,076|
| |Hughes County|     1| 75.307| N/A|   111|  8359.063| N/A|  13,279|
| |McIntosh County|     1| 51.031| N/A|   151|  7705.654| N/A|  19,596|
| |Logan County|     1| 20.829| N/A|   189|  3936.598| N/A|  48,011|
| |Le Flore County|     1| 20.059| N/A|   249|  4994.684| N/A|  49,853|
| |Latimer County|     1| 99.275| N/A|    71|  7048.546| N/A|  10,073|
| |Kiowa County|     1| 114.837| N/A|    27|  3100.597| N/A|   8,708|
| |Major County|     1| 131.079| N/A|    25|  3276.969| N/A|   7,629|
| |Beckham County|     1| 45.748| N/A|    45|  2058.649| N/A|  21,859|
| |Bryan County|     1| 20.836| N/A|   385|  8021.669| N/A|  47,995|
| |Cherokee County|     1| 20.552| N/A|   351|  7213.762| N/A|  48,657|
| |Choctaw County|     1| 68.157| N/A|   166| 11314.068| N/A|  14,672|
| |Coal County|     0|  0.000| N/A|    27|  4913.558| N/A|   5,495|
| |Cimarron County|     0|  0.000| N/A|     1|   467.946| N/A|   2,137|
| |Blaine County|     0|  0.000| N/A|    38|  4030.120| N/A|   9,429|
| |Beaver County|     0|  0.000| N/A|    36|  6778.384| N/A|   5,311|
| |Atoka County|     0|  0.000| N/A|    64|  4651.839| N/A|  13,758|
| |Alfalfa County|     0|  0.000| N/A|     3|   526.131| N/A|   5,702|
| |Craig County|     0|  0.000| N/A|    77|  5444.774| N/A|  14,142|
| |Custer County|     0|  0.000| N/A|   192|  6620.005| N/A|  29,003|
| |Dewey County|     0|  0.000| N/A|     8|  1635.657| N/A|   4,891|
| |Grant County|     0|  0.000| N/A|    12|  2769.444| N/A|   4,333|
| |Woods County|     0|  0.000| N/A|    15|  1705.902| N/A|   8,793|
| |Ellis County|     0|  0.000| N/A|     3|   777.403| N/A|   3,859|
| |Murray County|     0|  0.000| N/A|    60|  4263.483| N/A|  14,073|
| |Woodward County|     0|  0.000| N/A|    32|  1583.296| N/A|  20,211|
| |Washita County|     0|  0.000| N/A|    24|  2198.608| N/A|  10,916|
| |Harmon County|     0|  0.000| N/A|    25|  9423.294| N/A|   2,653|
| |Roger Mills County|     0|  0.000| N/A|     8|  2232.766| N/A|   3,583|
| |Pushmataha County|     0|  0.000| N/A|   100|  9012.257| N/A|  11,096|
| |Okfuskee County|     0|  0.000| N/A|    57|  4752.772| N/A|  11,993|
| |Marshall County|     0|  0.000| N/A|    97|  5729.136| N/A|  16,931|
| |Love County|     0|  0.000| N/A|    65|  6339.608| N/A|  10,253|
| |Kingfisher County|     0|  0.000| N/A|   111|  7040.913| N/A|  15,765|
| |Johnston County|     0|  0.000| N/A|    40|  3608.480| N/A|  11,085|
| |Jefferson County|     0|  0.000| N/A|    31|  5164.945| N/A|   6,002|
| |Haskell County|     0|  0.000| N/A|    43|  3405.401| N/A|  12,627|
| |Harper County|     0|  0.000| N/A|     9|  2440.347| N/A|   3,688|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   475| 157.399| N/A|42,956| 14234.191| N/A|3,017,804|
| |Pulaski County|    79| 201.576|  2.552| 4,893| 12484.977| 114.822| 391,911|
| |Washington County|    47| 196.499|  4.181| 6,072| 25385.995| 248.135| 239,187|
| |Benton County|    39| 139.714|  0.000| 4,572| 16378.819| 137.923| 279,141|
| |Jefferson County|    39| 583.623|  8.607| 1,382| 20681.192| 436.363|  66,824|
| |Crittenden County|    20| 417.058| 21.086| 1,242| 25899.281| 604.734|  47,955|
| |Union County|    16| 413.629|  0.000|   435| 11245.541| 63.856|  38,682|
| |Sebastian County|    15| 117.346|  3.342| 1,856| 14519.624| 516.323| 127,827|
| |Yell County|    14| 656.014|  0.000| 1,030| 48263.905| 419.965|  21,341|
| |Craighead County|    12| 108.763|  0.000| 1,134| 10278.070| 137.413| 110,332|
| |Lincoln County|    11| 844.595|  0.000| 1,186| 91062.654| 622.141|  13,024|
| |Mississippi County|    11| 270.596| 14.288|   797| 19605.914| 552.836|  40,651|
| |Sevier County|    10| 587.993|  0.000|   939| 55212.560| 187.576|  17,007|
| |Lawrence County|    10| 609.533| 28.653|   185| 11276.362| 105.639|  16,406|
| |Pope County|     9| 140.467| N/A| 1,216| 18978.649| N/A|  64,072|
| |Nevada County|     9| 1090.645| N/A|   133| 16117.305| N/A|   8,252|
| |Hot Spring County|     9| 266.501| N/A| 1,465| 43380.415| N/A|  33,771|
| |Garland County|     8| 80.494| N/A|   875|  8804.057| N/A|  99,386|
| |Lee County|     7| 790.335| N/A|   890| 100485.492| N/A|   8,857|
| |Columbia County|     6| 255.787| N/A|   202|  8611.502| N/A|  23,457|
| |Phillips County|     6| 337.420| N/A|   284| 15971.207| N/A|  17,782|
| |Chicot County|     6| 593.003| N/A|   536| 52974.896| N/A|  10,118|
| |Carroll County|     6| 211.416| N/A|   340| 11980.268| N/A|  28,380|
| |Faulkner County|     5| 39.680| N/A| 1,212|  9618.513| N/A| 126,007|
| |Cleburne County|     5| 200.650| N/A|   182|  7303.664| N/A|  24,919|
| |Sharp County|     5| 286.664| N/A|   106|  6077.285| N/A|  17,442|
| |Saline County|     5| 40.837| N/A|   892|  7285.379| N/A| 122,437|
| |Clay County|     4| 274.895| N/A|   109|  7490.894| N/A|  14,551|
| |Ashley County|     4| 203.490| N/A|   254| 12921.606| N/A|  19,657|
| |Miller County|     4| 92.471| N/A|   470| 10865.293| N/A|  43,257|
| |Randolph County|     3| 167.056| N/A|   175|  9744.960| N/A|  17,958|
| |Bradley County|     3| 278.733| N/A|   147| 13657.902| N/A|  10,763|
| |Poinsett County|     3| 127.508| N/A|   167|  7097.926| N/A|  23,528|
| |St. Francis County|     3| 120.029| N/A| 1,140| 45610.947| N/A|  24,994|
| |Crawford County|     3| 47.426| N/A|   554|  8757.924| N/A|  63,257|
| |Newton County|     3| 386.947| N/A|    98| 12640.268| N/A|   7,753|
| |Conway County|     3| 143.913| N/A|   137|  6572.004| N/A|  20,846|
| |Desha County|     2| 176.041| N/A|   160| 14083.267| N/A|  11,361|
| |Drew County|     2| 109.776| N/A|   166|  9111.367| N/A|  18,219|
| |Cross County|     2| 121.810| N/A|   172| 10475.668| N/A|  16,419|
| |Cleveland County|     2| 251.383| N/A|    71|  8924.082| N/A|   7,956|
| |Franklin County|     2| 112.899| N/A|   108|  6096.528| N/A|  17,715|
| |Howard County|     2| 151.492| N/A|   300| 22723.830| N/A|  13,202|
| |Hempstead County|     2| 92.885| N/A|   220| 10217.351| N/A|  21,532|
| |Lafayette County|     2| 301.932| N/A|    49|  7397.343| N/A|   6,624|
| |White County|     2| 25.396| N/A|   266|  3377.649| N/A|  78,753|
| |Van Buren County|     2| 120.882| N/A|    52|  3142.943| N/A|  16,545|
| |Lonoke County|     2| 27.282| N/A|   452|  6165.682| N/A|  73,309|
| |Stone County|     1| 79.962| N/A|    55|  4397.889| N/A|  12,506|
| |Greene County|     1| 22.063| N/A|   393|  8670.712| N/A|  45,325|
| |Logan County|     1| 46.585| N/A|   195|  9084.133| N/A|  21,466|
| |Ouachita County|     1| 42.768| N/A|    81|  3464.203| N/A|  23,382|
| |Boone County|     1| 26.715| N/A|   176|  4701.859| N/A|  37,432|
| |Polk County|     1| 50.090| N/A|   131|  6561.811| N/A|  19,964|
| |Little River County|     1| 81.573| N/A|   156| 12725.345| N/A|  12,259|
| |Madison County|     1| 60.328| N/A|   262| 15805.985| N/A|  16,576|
| |Izard County|     1| 73.373| N/A|    45|  3301.783| N/A|  13,629|
| |Jackson County|     1| 59.812| N/A|    59|  3528.919| N/A|  16,719|
| |Pike County|     1| 93.301| N/A|    81|  7557.380| N/A|  10,718|
| |Calhoun County|     0|  0.000| N/A|    13|  2505.300| N/A|   5,189|
| |Baxter County|     0|  0.000| N/A|    62|  1478.584| N/A|  41,932|
| |Dallas County|     0|  0.000| N/A|    58|  8275.075| N/A|   7,009|
| |Clark County|     0|  0.000| N/A|   159|  7123.656| N/A|  22,320|
| |Fulton County|     0|  0.000| N/A|    29|  2324.277| N/A|  12,477|
| |Grant County|     0|  0.000| N/A|   127|  6953.189| N/A|  18,265|
| |Woodruff County|     0|  0.000| N/A|    20|  3164.557| N/A|   6,320|
| |Marion County|     0|  0.000| N/A|    23|  1377.741| N/A|  16,694|
| |Arkansas County|     0|  0.000| N/A|   201| 11494.910| N/A|  17,486|
| |Johnson County|     0|  0.000| N/A|   636| 23929.566| N/A|  26,578|
| |Independence County|     0|  0.000| N/A|   398| 10522.141| N/A|  37,825|
| |Monroe County|     0|  0.000| N/A|    53|  7909.267| N/A|   6,701|
| |Perry County|     0|  0.000| N/A|    49|  4686.753| N/A|  10,455|
| |Searcy County|     0|  0.000| N/A|    27|  3425.961| N/A|   7,881|
| |Scott County|     0|  0.000| N/A|    44|  4279.739| N/A|  10,281|
| |Prairie County|     0|  0.000| N/A|    74|  9178.864| N/A|   8,062|
| |Montgomery County|     0|  0.000| N/A|    26|  2893.390| N/A|   8,986|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   417| 306.683| N/A| 6,659|  4897.364| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  1.400| 3,775|  9052.215| 23.765| 417,025|
| |Rockingham County|    95| 306.680|  0.000| 1,642|  5300.724| 20.171| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   458|  3025.279|  1.411| 151,391|
| |Strafford County|    13| 99.515|  0.000|   335|  2564.436| 26.208| 130,633|
| |Belknap County|     4| 65.250| N/A|   109|  1778.053| N/A|  61,303|
| |Cheshire County|     2| 26.286| N/A|    92|  1209.174| N/A|  76,085|
| |Sullivan County|     1| 23.177| N/A|    40|   927.085| N/A|  43,146|
| |Grafton County|     1| 11.125| N/A|   103|  1145.896| N/A|  89,886|
| |Carroll County|     1| 20.446| N/A|    89|  1819.669| N/A|  48,910|
| |Coos County|     0|  0.000| N/A|    16|   506.923| N/A|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   366| 125.630| N/A|28,432|  9759.332| N/A|2,913,314|
| |Johnson County|    98| 162.682|  0.000| 5,150|  8549.123| 217.463| 602,401|
| |Wyandotte County|    96| 580.309|  2.504| 4,535| 27413.573| 415.397| 165,429|
| |Sedgwick County|    43| 83.327|  2.542| 4,348|  8425.671| 181.752| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,434|  8107.420| 84.342| 176,875|
| |Lyon County|    13| 391.625|  0.000|   676| 20364.513| 409.665|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,740| 47714.372| 43.536|  36,467|
| |Phillips County|     8| 1528.468| N/A|    49|  9361.865| N/A|   5,234|
| |Leavenworth County|     8| 97.850| N/A| 1,425| 17429.487| N/A|  81,758|
| |Coffey County|     8| 978.115| N/A|    67|  8191.710| N/A|   8,179|
| |Ford County|     8| 237.961| N/A| 2,042| 60739.463| N/A|  33,619|
| |Saline County|     5| 92.210| N/A|   343|  6325.612| N/A|  54,224|
| |Riley County|     5| 67.356| N/A|   450|  6062.076| N/A|  74,232|
| |Montgomery County|     5| 157.089| N/A|   161|  5058.280| N/A|  31,829|
| |Douglas County|     4| 32.717| N/A|   679|  5553.783| N/A| 122,259|
| |Seward County|     4| 186.672| N/A| 1,188| 55441.478| N/A|  21,428|
| |Barton County|     3| 116.374| N/A|   116|  4499.787| N/A|  25,779|
| |Sumner County|     3| 131.372| N/A|    98|  4291.470| N/A|  22,836|
| |Geary County|     2| 63.151| N/A|   128|  4041.680| N/A|  31,670|
| |Cowley County|     2| 57.293| N/A|   158|  4526.183| N/A|  34,908|
| |Morton County|     2| 773.096| N/A|     9|  3478.933| N/A|   2,587|
| |Grant County|     2| 279.720| N/A|    97| 13566.434| N/A|   7,150|
| |Clay County|     2| 249.938| N/A|    18|  2249.438| N/A|   8,002|
| |Marion County|     1| 84.147| N/A|    44|  3702.457| N/A|  11,884|
| |Reno County|     1| 16.130| N/A|   228|  3677.538| N/A|  61,998|
| |McPherson County|     1| 35.036| N/A|   130|  4554.691| N/A|  28,542|
| |Kearny County|     1| 260.552| N/A|    57| 14851.485| N/A|   3,838|
| |Nemaha County|     1| 97.742| N/A|    48|  4691.623| N/A|  10,231|
| |Ellis County|     1| 35.023| N/A|   133|  4658.004| N/A|  28,553|
| |Franklin County|     1| 39.148| N/A|   155|  6067.961| N/A|  25,544|
| |Harvey County|     1| 29.045| N/A|   169|  4908.653| N/A|  34,429|
| |Jackson County|     1| 75.924| N/A|   144| 10933.111| N/A|  13,171|
| |Trego County|     1| 356.761| N/A|     5|  1783.803| N/A|   2,803|
| |Stanton County|     1| 498.504| N/A|    16|  7976.072| N/A|   2,006|
| |Dickinson County|     1| 54.154| N/A|    43|  2328.604| N/A|  18,466|
| |Bourbon County|     1| 68.804| N/A|    73|  5022.705| N/A|  14,534|
| |Crawford County|     1| 25.761| N/A|   377|  9711.989| N/A|  38,818|
| |Cherokee County|     1| 50.153| N/A|    78|  3911.931| N/A|  19,939|
| |Clark County|     1| 501.505| N/A|    43| 21564.694| N/A|   1,994|
| |Rooks County|     0|  0.000| N/A|    16|  3252.033| N/A|   4,920|
| |Rice County|     0|  0.000| N/A|    30|  3145.643| N/A|   9,537|
| |Republic County|     0|  0.000| N/A|    32|  6902.502| N/A|   4,636|
| |Rawlins County|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Pratt County|     0|  0.000| N/A|    33|  3601.048| N/A|   9,164|
| |Pottawatomie County|     0|  0.000| N/A|   105|  4306.279| N/A|  24,383|
| |Pawnee County|     0|  0.000| N/A|     7|  1091.363| N/A|   6,414|
| |Ottawa County|     0|  0.000| N/A|    30|  5259.467| N/A|   5,704|
| |Osborne County|     0|  0.000| N/A|     4|  1169.249| N/A|   3,421|
| |Osage County|     0|  0.000| N/A|    38|  2382.595| N/A|  15,949|
| |Norton County|     0|  0.000| N/A|    23|  4290.244| N/A|   5,361|
| |Ness County|     0|  0.000| N/A|     6|  2181.818| N/A|   2,750|
| |Neosho County|     0|  0.000| N/A|    53|  3311.051| N/A|  16,007|
| |Morris County|     0|  0.000| N/A|     9|  1601.423| N/A|   5,620|
| |Mitchell County|     0|  0.000| N/A|    27|  4515.805| N/A|   5,979|
| |Miami County|     0|  0.000| N/A|   120|  3504.980| N/A|  34,237|
| |Meade County|     0|  0.000| N/A|    40|  9918.175| N/A|   4,033|
| |Logan County|     0|  0.000| N/A|     2|   715.820| N/A|   2,794|
| |Marshall County|     0|  0.000| N/A|     9|   927.166| N/A|   9,707|
| |Rush County|     0|  0.000| N/A|     6|  1976.285| N/A|   3,036|
| |Russell County|     0|  0.000| N/A|    13|  1896.149| N/A|   6,856|
| |Greeley County|     0|  0.000| N/A|     3|  2435.065| N/A|   1,232|
| |Atchison County|     0|  0.000| N/A|    62|  3857.401| N/A|  16,073|
| |Anderson County|     0|  0.000| N/A|    29|  3690.506| N/A|   7,858|
| |Allen County|     0|  0.000| N/A|    15|  1212.709| N/A|  12,369|
| |Cheyenne County|     0|  0.000| N/A|     2|   752.729| N/A|   2,657|
| |Chautauqua County|     0|  0.000| N/A|     5|  1538.462| N/A|   3,250|
| |Cloud County|     0|  0.000| N/A|    30|  3414.523| N/A|   8,786|
| |Labette County|     0|  0.000| N/A|   110|  5607.096| N/A|  19,618|
| |Greenwood County|     0|  0.000| N/A|    19|  3176.195| N/A|   5,982|
| |Kiowa County|     0|  0.000| N/A|     6|  2424.242| N/A|   2,475|
| |Kingman County|     0|  0.000| N/A|    10|  1398.210| N/A|   7,152|
| |Jewell County|     0|  0.000| N/A|    10|  3473.428| N/A|   2,879|
| |Jefferson County|     0|  0.000| N/A|    70|  3675.891| N/A|  19,043|
| |Hodgeman County|     0|  0.000| N/A|    11|  6131.550| N/A|   1,794|
| |Haskell County|     0|  0.000| N/A|    44| 11088.710| N/A|   3,968|
| |Harper County|     0|  0.000| N/A|     9|  1655.629| N/A|   5,436|
| |Barber County|     0|  0.000| N/A|     4|   903.546| N/A|   4,427|
| |Brown County|     0|  0.000| N/A|    32|  3345.880| N/A|   9,564|
| |Butler County|     0|  0.000| N/A|   215|  3213.224| N/A|  66,911|
| |Sheridan County|     0|  0.000| N/A|     7|  2776.676| N/A|   2,521|
| |Scott County|     0|  0.000| N/A|    28|  5805.515| N/A|   4,823|
| |Wilson County|     0|  0.000| N/A|     8|   938.416| N/A|   8,525|
| |Woodson County|     0|  0.000| N/A|    11|  3505.417| N/A|   3,138|
| |Wichita County|     0|  0.000| N/A|     4|  1887.683| N/A|   2,119|
| |Washington County|     0|  0.000| N/A|     2|   369.959| N/A|   5,406|
| |Chase County|     0|  0.000| N/A|    34| 12839.879| N/A|   2,648|
| |Wallace County|     0|  0.000| N/A|     0|     0.000| N/A|   1,518|
| |Wabaunsee County|     0|  0.000| N/A|    39|  5626.894| N/A|   6,931|
| |Thomas County|     0|  0.000| N/A|    32|  4114.697| N/A|   7,777|
| |Stevens County|     0|  0.000| N/A|    44|  8021.878| N/A|   5,485|
| |Stafford County|     0|  0.000| N/A|     3|   721.848| N/A|   4,156|
| |Smith County|     0|  0.000| N/A|     3|   837.287| N/A|   3,583|
| |Sherman County|     0|  0.000| N/A|    15|  2535.068| N/A|   5,917|
| |Linn County|     0|  0.000| N/A|    35|  3607.132| N/A|   9,703|
| |Lincoln County|     0|  0.000| N/A|     6|  2025.658| N/A|   2,962|
| |Lane County|     0|  0.000| N/A|     5|  3257.329| N/A|   1,535|
| |Hamilton County|     0|  0.000| N/A|    37| 14572.666| N/A|   2,539|
| |Comanche County|     0|  0.000| N/A|     3|  1764.706| N/A|   1,700|
| |Gray County|     0|  0.000| N/A|    71| 11857.047| N/A|   5,988|
| |Graham County|     0|  0.000| N/A|    16|  6446.414| N/A|   2,482|
| |Gove County|     0|  0.000| N/A|     6|  2276.176| N/A|   2,636|
| |Ellsworth County|     0|  0.000| N/A|    18|  2949.853| N/A|   6,102|
| |Elk County|     0|  0.000| N/A|     1|   395.257| N/A|   2,530|
| |Edwards County|     0|  0.000| N/A|    10|  3573.981| N/A|   2,798|
| |Doniphan County|     0|  0.000| N/A|    46|  6052.632| N/A|   7,600|
| |Decatur County|     0|  0.000| N/A|     5|  1768.659| N/A|   2,827|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   328| 169.561| N/A|26,801| 13854.885| N/A|1,934,408|
| |Douglas County|   131| 229.291|  0.000|10,611| 18572.551| 228.450| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,717| 27985.592| 63.845|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,901| 94926.595|  0.000|  20,026|
| |Lancaster County|    15| 47.009|  0.000| 3,133|  9818.546| 125.356| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    96| 10296.010| 50.698|   9,324|
| |Adams County|    11| 350.732|  0.000|   344| 10968.338| 59.325|  31,363|
| |Dawson County|     9| 381.437| N/A|   949| 40220.386| N/A|  23,595|
| |Dodge County|     8| 218.788| N/A|   775| 21195.132| N/A|  36,565|
| |Scotts Bluff County|     6| 168.454| N/A|   289|  8113.875| N/A|  35,618|
| |Sarpy County|     6| 32.052| N/A| 2,064| 11025.877| N/A| 187,196|
| |Madison County|     5| 142.454| N/A|   420| 11966.153| N/A|  35,099|
| |Howard County|     4| 620.636| N/A|    54|  8378.588| N/A|   6,445|
| |Custer County|     4| 371.161| N/A|    43|  3989.979| N/A|  10,777|
| |Colfax County|     4| 373.518| N/A|   695| 64898.683| N/A|  10,709|
| |Gage County|     4| 185.934| N/A|    82|  3811.649| N/A|  21,513|
| |Thurston County|     4| 553.710| N/A|   202| 27962.348| N/A|   7,224|
| |Platte County|     3| 89.633| N/A|   767| 22916.044| N/A|  33,470|
| |Dixon County|     2| 354.862| N/A|    56|  9936.125| N/A|   5,636|
| |Saunders County|     2| 92.687| N/A|   139|  6441.746| N/A|  21,578|
| |Saline County|     2| 140.607| N/A|   582| 40916.760| N/A|  14,224|
| |Lincoln County|     2| 57.284| N/A|    94|  2692.330| N/A|  34,914|
| |Furnas County|     1| 213.858| N/A|    15|  3207.870| N/A|   4,676|
| |Washington County|     1| 48.242| N/A|   108|  5210.092| N/A|  20,729|
| |Seward County|     1| 57.857| N/A|   100|  5785.698| N/A|  17,284|
| |Perkins County|     1| 345.901| N/A|    17|  5880.318| N/A|   2,891|
| |Richardson County|     1| 127.146| N/A|    20|  2542.912| N/A|   7,865|
| |Buffalo County|     1| 20.137| N/A|   357|  7189.029| N/A|  49,659|
| |Antelope County|     1| 158.781| N/A|    19|  3016.831| N/A|   6,298|
| |Fillmore County|     1| 183.083| N/A|    24|  4393.995| N/A|   5,462|
| |Valley County|     0|  0.000| N/A|    10|  2405.002| N/A|   4,158|
| |Merrick County|     0|  0.000| N/A|    54|  6963.250| N/A|   7,755|
| |McPherson County|     0|  0.000| N/A|     4|  8097.166| N/A|     494|
| |Loup County|     0|  0.000| N/A|     0|     0.000| N/A|     664|
| |Logan County|     0|  0.000| N/A|     0|     0.000| N/A|     748|
| |Knox County|     0|  0.000| N/A|    32|  3840.614| N/A|   8,332|
| |Keya Paha County|     0|  0.000| N/A|     0|     0.000| N/A|     806|
| |Otoe County|     0|  0.000| N/A|    43|  2685.486| N/A|  16,012|
| |Keith County|     0|  0.000| N/A|    19|  2364.949| N/A|   8,034|
| |Kearney County|     0|  0.000| N/A|    34|  5234.796| N/A|   6,495|
| |Johnson County|     0|  0.000| N/A|    13|  2563.597| N/A|   5,071|
| |Jefferson County|     0|  0.000| N/A|    14|  1986.943| N/A|   7,046|
| |Hooker County|     0|  0.000| N/A|     4|  5865.103| N/A|     682|
| |Holt County|     0|  0.000| N/A|    11|  1092.679| N/A|  10,067|
| |Hitchcock County|     0|  0.000| N/A|     1|   362.056| N/A|   2,762|
| |Hayes County|     0|  0.000| N/A|     0|     0.000| N/A|     922|
| |Nuckolls County|     0|  0.000| N/A|     5|  1205.400| N/A|   4,148|
| |Pawnee County|     0|  0.000| N/A|     8|  3061.615| N/A|   2,613|
| |Greeley County|     0|  0.000| N/A|     8|  3395.586| N/A|   2,356|
| |Thomas County|     0|  0.000| N/A|     1|  1385.042| N/A|     722|
| |York County|     0|  0.000| N/A|    72|  5263.543| N/A|  13,679|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|     783|
| |Webster County|     0|  0.000| N/A|     9|  2581.015| N/A|   3,487|
| |Morrill County|     0|  0.000| N/A|    58| 12494.614| N/A|   4,642|
| |Nance County|     0|  0.000| N/A|     8|  2273.373| N/A|   3,519|
| |Nemaha County|     0|  0.000| N/A|    21|  3012.048| N/A|   6,972|
| |Kimball County|     0|  0.000| N/A|    15|  4129.956| N/A|   3,632|
| |Wayne County|     0|  0.000| N/A|    35|  3729.355| N/A|   9,385|
| |Thayer County|     0|  0.000| N/A|    26|  5196.882| N/A|   5,003|
| |Phelps County|     0|  0.000| N/A|    36|  3984.946| N/A|   9,034|
| |Banner County|     0|  0.000| N/A|     2|  2684.564| N/A|     745|
| |Boone County|     0|  0.000| N/A|     8|  1540.832| N/A|   5,192|
| |Gosper County|     0|  0.000| N/A|    19|  9547.739| N/A|   1,990|
| |Clay County|     0|  0.000| N/A|    48|  7738.191| N/A|   6,203|
| |Garfield County|     0|  0.000| N/A|     3|  1523.616| N/A|   1,969|
| |Garden County|     0|  0.000| N/A|     4|  2177.463| N/A|   1,837|
| |Frontier County|     0|  0.000| N/A|     3|  1141.987| N/A|   2,627|
| |Franklin County|     0|  0.000| N/A|     9|  3021.148| N/A|   2,979|
| |Dundy County|     0|  0.000| N/A|     1|   590.667| N/A|   1,693|
| |Deuel County|     0|  0.000| N/A|     1|   557.414| N/A|   1,794|
| |Dawes County|     0|  0.000| N/A|     8|   931.424| N/A|   8,589|
| |Cuming County|     0|  0.000| N/A|    59|  6669.681| N/A|   8,846|
| |Cheyenne County|     0|  0.000| N/A|    26|  2918.070| N/A|   8,910|
| |Box Butte County|     0|  0.000| N/A|    11|  1020.124| N/A|  10,783|
| |Cherry County|     0|  0.000| N/A|     4|   703.111| N/A|   5,689|
| |Chase County|     0|  0.000| N/A|     6|  1529.052| N/A|   3,924|
| |Cedar County|     0|  0.000| N/A|    21|  2499.405| N/A|   8,402|
| |Cass County|     0|  0.000| N/A|   160|  6095.703| N/A|  26,248|
| |Butler County|     0|  0.000| N/A|    56|  6986.028| N/A|   8,016|
| |Burt County|     0|  0.000| N/A|    25|  3870.568| N/A|   6,459|
| |Brown County|     0|  0.000| N/A|     0|     0.000| N/A|   2,955|
| |Boyd County|     0|  0.000| N/A|     1|   521.105| N/A|   1,919|
| |Stanton County|     0|  0.000| N/A|    28|  4729.730| N/A|   5,920|
| |Sioux County|     0|  0.000| N/A|     5|  4288.165| N/A|   1,166|
| |Sherman County|     0|  0.000| N/A|     9|  2999.000| N/A|   3,001|
| |Sheridan County|     0|  0.000| N/A|     9|  1715.593| N/A|   5,246|
| |Rock County|     0|  0.000| N/A|     2|  1473.839| N/A|   1,357|
| |Red Willow County|     0|  0.000| N/A|    16|  1491.981| N/A|  10,724|
| |Polk County|     0|  0.000| N/A|    24|  4603.875| N/A|   5,213|
| |Pierce County|     0|  0.000| N/A|    18|  2518.187| N/A|   7,148|
| |Harlan County|     0|  0.000| N/A|     1|   295.858| N/A|   3,380|
| |Grant County|     0|  0.000| N/A|     0|     0.000| N/A|     623|
| |Arthur County|     0|  0.000| N/A|     0|     0.000| N/A|     463|
| |Blaine County|     0|  0.000| N/A|     0|     0.000| N/A|     465|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   328| 77.767| N/A|19,366|  4591.562| N/A|4,217,737|
| |Multnomah County|    93| 114.412|  0.533| 4,497|  5532.352| 65.382| 812,855|
| |Marion County|    68| 195.505|  1.191| 2,692|  7739.680| 112.455| 347,818|
| |Clackamas County|    36| 86.086|  0.000| 1,421|  3398.001| 50.122| 418,187|
| |Umatilla County|    24| 307.890|  2.078| 2,060| 26427.197| 532.393|  77,950|
| |Washington County|    23| 38.232|  0.261| 2,849|  4735.768| 71.477| 601,592|
| |Polk County|    12| 139.397|  0.000|   296|  3438.462| 55.835|  86,085|
| |Yamhill County|    11| 102.708|  1.465|   386|  3604.108| 130.719| 107,100|
| |Linn County|    10| 77.072|  0.000|   254|  1957.626| 40.061| 129,749|
| |Malheur County|    10| 327.107| 13.849|   676| 22112.460| 268.968|  30,571|
| |Lincoln County|     9| 180.137| N/A|   395|  7906.009| N/A|  49,962|
| |Deschutes County|     8| 40.467| N/A|   540|  2731.522| N/A| 197,692|
| |Benton County|     6| 64.479| N/A|   157|  1687.211| N/A|  93,053|
| |Lane County|     3|  7.852| N/A|   523|  1368.870| N/A| 382,067|
| |Jefferson County|     3| 121.664| N/A|   311| 12612.540| N/A|  24,658|
| |Wasco County|     3| 112.435| N/A|   170|  6371.336| N/A|  26,682|
| |Union County|     2| 74.530| N/A|   388| 14458.729| N/A|  26,835|
| |Wallowa County|     1| 138.735| N/A|    19|  2635.960| N/A|   7,208|
| |Morrow County|     1| 86.185| N/A|   305| 26286.305| N/A|  11,603|
| |Klamath County|     1| 14.655| N/A|   196|  2872.300| N/A|  68,238|
| |Josephine County|     1| 11.430| N/A|   107|  1223.039| N/A|  87,487|
| |Jackson County|     1|  4.526| N/A|   394|  1783.257| N/A| 220,944|
| |Douglas County|     1|  9.011| N/A|   134|  1207.425| N/A| 110,980|
| |Crook County|     1| 40.977| N/A|    43|  1762.006| N/A|  24,404|
| |Gilliam County|     0|  0.000| N/A|     4|  2092.050| N/A|   1,912|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|   1,332|
| |Tillamook County|     0|  0.000| N/A|    30|  1109.632| N/A|  27,036|
| |Sherman County|     0|  0.000| N/A|    15|  8426.966| N/A|   1,780|
| |Lake County|     0|  0.000| N/A|    32|  4066.590| N/A|   7,869|
| |Hood River County|     0|  0.000| N/A|   169|  7227.782| N/A|  23,382|
| |Harney County|     0|  0.000| N/A|     8|  1082.105| N/A|   7,393|
| |Grant County|     0|  0.000| N/A|     2|   277.816| N/A|   7,199|
| |Curry County|     0|  0.000| N/A|    14|   610.687| N/A|  22,925|
| |Columbia County|     0|  0.000| N/A|    79|  1508.958| N/A|  52,354|
| |Clatsop County|     0|  0.000| N/A|    82|  2038.584| N/A|  40,224|
| |Baker County|     0|  0.000| N/A|    33|  2046.639| N/A|  16,124|
| |Coos County|     0|  0.000| N/A|    85|  1318.095| N/A|  64,487|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   257| 80.163| N/A|33,034| 10303.940| N/A|3,205,958|
| |Salt Lake County|   178| 153.390|  1.149|19,556| 16852.272| 143.293|1,160,437|
| |Utah County|    35| 55.011|  0.493| 8,047| 12647.842| 188.345| 636,235|
| |San Juan County|    24| 1567.808|  0.000|   628| 41024.301| 326.627|  15,308|
| |Davis County|    15| 42.196|  2.345| 3,026|  8512.410| 105.965| 355,481|
| |Wasatch County|     4| 117.333| N/A|   533| 15634.625| N/A|  34,091|
| |Summit County|     1| 23.728| N/A|   697| 16538.142| N/A|  42,145|
| |Grand County|     0|  0.000| N/A|     0|     0.000| N/A|   9,754|
| |Duchesne County|     0|  0.000| N/A|     0|     0.000| N/A|  19,938|
| |Garfield County|     0|  0.000| N/A|     0|     0.000| N/A|   5,051|
| |Wayne County|     0|  0.000| N/A|     0|     0.000| N/A|   2,711|
| |Kane County|     0|  0.000| N/A|     0|     0.000| N/A|   7,886|
| |Washington County|     0|  0.000| N/A|     0|     0.000| N/A| 177,556|
| |Uintah County|     0|  0.000| N/A|     0|     0.000| N/A|  35,734|
| |Tooele County|     0|  0.000| N/A|   547|  7569.991| N/A|  72,259|
| |Sevier County|     0|  0.000| N/A|     0|     0.000| N/A|  21,620|
| |Sanpete County|     0|  0.000| N/A|     0|     0.000| N/A|  30,939|
| |Rich County|     0|  0.000| N/A|     0|     0.000| N/A|   2,483|
| |Piute County|     0|  0.000| N/A|     0|     0.000| N/A|   1,479|
| |Morgan County|     0|  0.000| N/A|     0|     0.000| N/A|  12,124|
| |Millard County|     0|  0.000| N/A|     0|     0.000| N/A|  13,188|
| |Juab County|     0|  0.000| N/A|     0|     0.000| N/A|  12,017|
| |Iron County|     0|  0.000| N/A|     0|     0.000| N/A|  54,839|
| |Weber County|     0|  0.000| N/A|     0|     0.000| N/A| 260,213|
| |Beaver County|     0|  0.000| N/A|     0|     0.000| N/A|   6,710|
| |Emery County|     0|  0.000| N/A|     0|     0.000| N/A|  10,012|
| |Cache County|     0|  0.000| N/A|     0|     0.000| N/A| 128,289|
| |Carbon County|     0|  0.000| N/A|     0|     0.000| N/A|  20,463|
| |Box Elder County|     0|  0.000| N/A|     0|     0.000| N/A|  56,046|
| |Daggett County|     0|  0.000| N/A|     0|     0.000| N/A|     950|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   200| 111.915| N/A|21,670| 12126.028| N/A|1,787,065|
| |Ada County|    64| 132.894|  2.432| 8,069| 16755.020| 163.073| 481,587|
| |Canyon County|    37| 160.975|  0.000| 4,959| 21575.034| 381.783| 229,849|
| |Twin Falls County|    32| 368.333|  6.100| 1,238| 14249.868| 183.791|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   134|  3316.175| 41.177|  40,408|
| |Kootenai County|    13| 78.456|  4.734| 1,620|  9776.882| 150.817| 165,697|
| |Blaine County|     6| 260.632| N/A|   570| 24760.002| N/A|  23,021|
| |Jerome County|     6| 245.781| N/A|   433| 17737.178| N/A|  24,412|
| |Elmore County|     3| 109.047| N/A|   201|  7306.168| N/A|  27,511|
| |Bonneville County|     2| 16.798| N/A|   774|  6500.815| N/A| 119,062|
| |Payette County|     2| 83.504| N/A|   343| 14320.905| N/A|  23,951|
| |Shoshone County|     2| 155.255| N/A|    78|  6054.960| N/A|  12,882|
| |Washington County|     2| 196.194| N/A|   191| 18736.512| N/A|  10,194|
| |Minidoka County|     2| 95.062| N/A|   444| 21103.665| N/A|  21,039|
| |Bingham County|     2| 42.725| N/A|   187|  3994.788| N/A|  46,811|
| |Bannock County|     2| 22.777| N/A|   312|  3553.207| N/A|  87,808|
| |Jefferson County|     1| 33.477| N/A|   146|  4887.684| N/A|  29,871|
| |Boise County|     1| 127.698| N/A|    39|  4980.207| N/A|   7,831|
| |Valley County|     1| 87.781| N/A|    47|  4125.702| N/A|  11,392|
| |Cassia County|     1| 41.615| N/A|   483| 20099.875| N/A|  24,030|
| |Gooding County|     1| 65.880| N/A|   142|  9355.030| N/A|  15,179|
| |Owyhee County|     1| 84.581| N/A|   238| 20130.255| N/A|  11,823|
| |Madison County|     0|  0.000| N/A|   135|  3382.865| N/A|  39,907|
| |Teton County|     0|  0.000| N/A|    61|  5023.884| N/A|  12,142|
| |Power County|     0|  0.000| N/A|    43|  5598.229| N/A|   7,681|
| |Oneida County|     0|  0.000| N/A|     9|  1986.316| N/A|   4,531|
| |Lewis County|     0|  0.000| N/A|     1|   260.552| N/A|   3,838|
| |Caribou County|     0|  0.000| N/A|    23|  3214.535| N/A|   7,155|
| |Latah County|     0|  0.000| N/A|    88|  2194.076| N/A|  40,108|
| |Idaho County|     0|  0.000| N/A|    30|  1799.964| N/A|  16,667|
| |Gem County|     0|  0.000| N/A|   159|  8778.710| N/A|  18,112|
| |Fremont County|     0|  0.000| N/A|    63|  4809.527| N/A|  13,099|
| |Franklin County|     0|  0.000| N/A|    47|  3387.143| N/A|  13,876|
| |Custer County|     0|  0.000| N/A|     7|  1622.248| N/A|   4,315|
| |Clearwater County|     0|  0.000| N/A|    15|  1713.111| N/A|   8,756|
| |Clark County|     0|  0.000| N/A|     3|  3550.296| N/A|     845|
| |Camas County|     0|  0.000| N/A|     1|   904.159| N/A|   1,106|
| |Butte County|     0|  0.000| N/A|     0|     0.000| N/A|   2,597|
| |Boundary County|     0|  0.000| N/A|    34|  2776.644| N/A|  12,245|
| |Bonner County|     0|  0.000| N/A|   156|  3410.656| N/A|  45,739|
| |Benewah County|     0|  0.000| N/A|    57|  6130.351| N/A|   9,298|
| |Bear Lake County|     0|  0.000| N/A|     7|  1142.857| N/A|   6,125|
| |Adams County|     0|  0.000| N/A|    18|  4191.896| N/A|   4,294|
| |Lemhi County|     0|  0.000| N/A|    12|  1494.955| N/A|   8,027|
| |Lincoln County|     0|  0.000| N/A|    53|  9877.003| N/A|   5,366|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   135| 152.601| N/A| 9,020| 10196.019| N/A| 884,659|
| |Minnehaha County|    64| 331.376|  0.000| 4,233| 21917.425| 113.911| 193,134|
| |Pennington County|    29| 254.889|  2.758|   845|  7426.939| 61.525| 113,775|
| |Beadle County|     9| 487.726| N/A|   587| 31810.546| N/A|  18,453|
| |Todd County|     4| 393.043| N/A|    66|  6485.212| N/A|  10,177|
| |Union County|     4| 251.067| N/A|   199| 12490.585| N/A|  15,932|
| |Brown County|     3| 77.242| N/A|   410| 10556.399| N/A|  38,839|
| |Buffalo County|     3| 1529.052| N/A|   108| 55045.872| N/A|   1,962|
| |Lyman County|     2| 528.961| N/A|    88| 23274.266| N/A|   3,781|
| |Lincoln County|     2| 32.718| N/A|   579|  9471.928| N/A|  61,128|
| |Lake County|     2| 156.287| N/A|    84|  6564.038| N/A|  12,797|
| |Yankton County|     2| 87.665| N/A|   102|  4470.939| N/A|  22,814|
| |Hughes County|     2| 114.116| N/A|    84|  4792.879| N/A|  17,526|
| |Jackson County|     1| 299.043| N/A|    10|  2990.431| N/A|   3,344|
| |Jerauld County|     1| 496.771| N/A|    40| 19870.840| N/A|   2,013|
| |McCook County|     1| 179.019| N/A|    24|  4296.455| N/A|   5,586|
| |Meade County|     1| 35.296| N/A|    76|  2682.479| N/A|  28,332|
| |Oglala Lakota County|     1| 70.537| N/A|   149| 10509.981| N/A|  14,177|
| |Faulk County|     1| 434.972| N/A|    26| 11309.265| N/A|   2,299|
| |Butte County|     1| 95.886| N/A|    11|  1054.751| N/A|  10,429|
| |Roberts County|     1| 96.209| N/A|    70|  6734.655| N/A|  10,394|
| |Brookings County|     1| 28.509| N/A|   120|  3421.045| N/A|  35,077|
| |Bon Homme County|     0|  0.000| N/A|    13|  1883.785| N/A|   6,901|
| |Edmunds County|     0|  0.000| N/A|    13|  3395.142| N/A|   3,829|
| |Dewey County|     0|  0.000| N/A|    61| 10353.021| N/A|   5,892|
| |Day County|     0|  0.000| N/A|    21|  3871.681| N/A|   5,424|
| |Hanson County|     0|  0.000| N/A|    21|  6081.668| N/A|   3,453|
| |Davison County|     0|  0.000| N/A|    88|  4450.063| N/A|  19,775|
| |Custer County|     0|  0.000| N/A|    23|  2563.531| N/A|   8,972|
| |Corson County|     0|  0.000| N/A|    29|  7097.406| N/A|   4,086|
| |Codington County|     0|  0.000| N/A|   119|  4248.634| N/A|  28,009|
| |Clay County|     0|  0.000| N/A|   118|  8386.638| N/A|  14,070|
| |Clark County|     0|  0.000| N/A|    16|  4282.655| N/A|   3,736|
| |Charles Mix County|     0|  0.000| N/A|   100| 10761.946| N/A|   9,292|
| |Campbell County|     0|  0.000| N/A|     2|  1453.488| N/A|   1,376|
| |Hand County|     0|  0.000| N/A|     7|  2193.670| N/A|   3,191|
| |Harding County|     0|  0.000| N/A|     0|     0.000| N/A|   1,298|
| |Perkins County|     0|  0.000| N/A|     6|  2094.241| N/A|   2,865|
| |Walworth County|     0|  0.000| N/A|    18|  3311.868| N/A|   5,435|
| |Turner County|     0|  0.000| N/A|    44|  5248.092| N/A|   8,384|
| |Tripp County|     0|  0.000| N/A|    20|  3675.795| N/A|   5,441|
| |Sully County|     0|  0.000| N/A|     1|   718.907| N/A|   1,391|
| |Stanley County|     0|  0.000| N/A|    14|  4519.045| N/A|   3,098|
| |Spink County|     0|  0.000| N/A|    21|  3293.601| N/A|   6,376|
| |Sanborn County|     0|  0.000| N/A|    13|  5546.075| N/A|   2,344|
| |Potter County|     0|  0.000| N/A|     1|   464.468| N/A|   2,153|
| |Moody County|     0|  0.000| N/A|    30|  4562.044| N/A|   6,576|
| |Hutchinson County|     0|  0.000| N/A|    27|  3703.196| N/A|   7,291|
| |Douglas County|     0|  0.000| N/A|    16|  5477.576| N/A|   2,921|
| |Fall River County|     0|  0.000| N/A|    16|  2383.435| N/A|   6,713|
| |Grant County|     0|  0.000| N/A|    23|  3261.486| N/A|   7,052|
| |Deuel County|     0|  0.000| N/A|     8|  1838.658| N/A|   4,351|
| |Hamlin County|     0|  0.000| N/A|    14|  2271.252| N/A|   6,164|
| |Haakon County|     0|  0.000| N/A|     2|  1053.186| N/A|   1,899|
| |Gregory County|     0|  0.000| N/A|     7|  1672.640| N/A|   4,185|
| |Mellette County|     0|  0.000| N/A|    24| 11644.833| N/A|   2,061|
| |Ziebach County|     0|  0.000| N/A|     8|  2902.758| N/A|   2,756|
| |Miner County|     0|  0.000| N/A|    15|  6768.953| N/A|   2,216|
| |Marshall County|     0|  0.000| N/A|     8|  1621.074| N/A|   4,935|
| |McPherson County|     0|  0.000| N/A|     7|  2942.413| N/A|   2,379|
| |Aurora County|     0|  0.000| N/A|    38| 13813.159| N/A|   2,751|
| |Lawrence County|     0|  0.000| N/A|    32|  1238.198| N/A|  25,844|
| |Kingsbury County|     0|  0.000| N/A|    14|  2834.582| N/A|   4,939|
| |Jones County|     0|  0.000| N/A|     2|  2214.839| N/A|     903|
| |Hyde County|     0|  0.000| N/A|     3|  2305.919| N/A|   1,301|
| |Brule County|     0|  0.000| N/A|    40|  7551.444| N/A|   5,297|
| |Bennett County|     0|  0.000| N/A|     6|  1783.061| N/A|   3,365|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   124| 92.247| N/A| 3,968|  2951.915| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  3.390| 2,058|  6976.200| 27.118| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   658|  3168.931| 14.448| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   169|  1381.825| 13.940| 122,302|
| |Androscoggin County|     7| 64.649| N/A|   548|  5061.093| N/A| 108,277|
| |Penobscot County|     5| 32.863| N/A|   150|   985.882| N/A| 152,148|
| |Aroostook County|     1| 14.913| N/A|    32|   477.220| N/A|  67,055|
| |Somerset County|     1| 19.808| N/A|    34|   673.481| N/A|  50,484|
| |Lincoln County|     1| 28.873| N/A|    34|   981.694| N/A|  34,634|
| |Knox County|     1| 25.143| N/A|    26|   653.726| N/A|  39,772|
| |Hancock County|     1| 18.186| N/A|    34|   618.328| N/A|  54,987|
| |Franklin County|     1| 33.114| N/A|    45|  1490.116| N/A|  30,199|
| |Piscataquis County|     0|  0.000| N/A|     3|   178.731| N/A|  16,785|
| |Oxford County|     0|  0.000| N/A|    55|   948.685| N/A|  57,975|
| |Washington County|     0|  0.000| N/A|     9|   286.816| N/A|  31,379|
| |Sagadahoc County|     0|  0.000| N/A|    51|  1422.356| N/A|  35,856|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   117| 65.285| N/A| 6,978|  3893.654| N/A|1,792,147|
| |Kanawha County|    21| 117.895|  2.398|   851|  4777.571| 119.758| 178,124|
| |Jackson County|    19| 664.894|  0.000|   157|  5494.121|  0.000|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   657|  5513.086| 34.882| 119,171|
| |Wayne County|     9| 228.415| N/A|   185|  4695.193| N/A|  39,402|
| |Fayette County|     5| 117.908| N/A|   131|  3089.185| N/A|  42,406|
| |Monongalia County|     5| 47.343| N/A|   925|  8758.474| N/A| 105,612|
| |Mineral County|     4| 148.876| N/A|   113|  4205.747| N/A|  26,868|
| |Jefferson County|     4| 69.996| N/A|   292|  5109.719| N/A|  57,146|
| |Wood County|     4| 47.894| N/A|   236|  2825.738| N/A|  83,518|
| |Ohio County|     4| 96.593| N/A|   255|  6157.784| N/A|  41,411|
| |Greenbrier County|     3| 86.550| N/A|    87|  2509.953| N/A|  34,662|
| |Logan County|     3| 93.694| N/A|   154|  4809.644| N/A|  32,019|
| |Preston County|     3| 89.734| N/A|   124|  3709.021| N/A|  33,432|
| |Mercer County|     3| 51.057| N/A|   165|  2808.128| N/A|  58,758|
| |Cabell County|     2| 21.752| N/A|   338|  3676.111| N/A|  91,945|
| |Marion County|     2| 35.668| N/A|   179|  3192.324| N/A|  56,072|
| |Lewis County|     2| 125.731| N/A|    27|  1697.366| N/A|  15,907|
| |Mingo County|     2| 85.383| N/A|   134|  5720.628| N/A|  23,424|
| |Brooke County|     1| 45.581| N/A|    62|  2826.018| N/A|  21,939|
| |Harrison County|     1| 14.869| N/A|   198|  2943.975| N/A|  67,256|
| |Pendleton County|     1| 143.493| N/A|    38|  5452.719| N/A|   6,969|
| |Wyoming County|     1| 49.034| N/A|    23|  1127.783| N/A|  20,394|
| |Raleigh County|     1| 13.631| N/A|   196|  2671.719| N/A|  73,361|
| |Roane County|     1| 73.057| N/A|    14|  1022.794| N/A|  13,688|
| |Nicholas County|     1| 40.823| N/A|    32|  1306.336| N/A|  24,496|
| |Barbour County|     1| 60.824| N/A|    29|  1763.883| N/A|  16,441|
| |Clay County|     1| 117.536| N/A|    17|  1998.119| N/A|   8,508|
| |Hampshire County|     1| 43.150| N/A|    74|  3193.096| N/A|  23,175|
| |Mason County|     1| 37.713| N/A|    49|  1847.941| N/A|  26,516|
| |Tucker County|     0|  0.000| N/A|    11|  1608.422| N/A|   6,839|
| |Taylor County|     0|  0.000| N/A|    53|  3174.603| N/A|  16,695|
| |Summers County|     0|  0.000| N/A|     7|   556.749| N/A|  12,573|
| |Wirt County|     0|  0.000| N/A|     6|  1030.751| N/A|   5,821|
| |Wetzel County|     0|  0.000| N/A|    41|  2721.540| N/A|  15,065|
| |Tyler County|     0|  0.000| N/A|    12|  1396.811| N/A|   8,591|
| |Upshur County|     0|  0.000| N/A|    38|  1571.807| N/A|  24,176|
| |Webster County|     0|  0.000| N/A|     3|   369.731| N/A|   8,114|
| |Morgan County|     0|  0.000| N/A|    26|  1453.813| N/A|  17,884|
| |Gilmer County|     0|  0.000| N/A|    16|  2045.251| N/A|   7,823|
| |Grant County|     0|  0.000| N/A|    81|  7002.075| N/A|  11,568|
| |Hancock County|     0|  0.000| N/A|   102|  3540.437| N/A|  28,810|
| |Hardy County|     0|  0.000| N/A|    54|  3919.861| N/A|  13,776|
| |McDowell County|     0|  0.000| N/A|    44|  2496.596| N/A|  17,624|
| |Braxton County|     0|  0.000| N/A|     8|   573.189| N/A|  13,957|
| |Doddridge County|     0|  0.000| N/A|     4|   473.485| N/A|   8,448|
| |Boone County|     0|  0.000| N/A|    79|  3681.782| N/A|  21,457|
| |Randolph County|     0|  0.000| N/A|   207|  7213.800| N/A|  28,695|
| |Pleasants County|     0|  0.000| N/A|     8|  1072.386| N/A|   7,460|
| |Putnam County|     0|  0.000| N/A|   172|  3046.944| N/A|  56,450|
| |Pocahontas County|     0|  0.000| N/A|    41|  4971.505| N/A|   8,247|
| |Calhoun County|     0|  0.000| N/A|     6|   844.001| N/A|   7,109|
| |Marshall County|     0|  0.000| N/A|   127|  4159.707| N/A|  30,531|
| |Monroe County|     0|  0.000| N/A|    19|  1431.262| N/A|  13,275|
| |Lincoln County|     0|  0.000| N/A|    68|  3331.863| N/A|  20,409|
| |Ritchie County|     0|  0.000| N/A|     3|   314.005| N/A|   9,554|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   105| 137.784| N/A| 6,767|  8879.855| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 2,932| 16116.709| 63.154| 181,923|
| |Burleigh County|     5| 52.287| N/A|   979| 10237.801| N/A|  95,626|
| |Grand Forks County|     5| 71.993| N/A|   637|  9171.934| N/A|  69,451|
| |Morton County|     3| 95.651| N/A|   281|  8959.316| N/A|  31,364|
| |Stark County|     3| 95.271| N/A|   214|  6796.024| N/A|  31,489|
| |Williams County|     2| 53.207| N/A|   233|  6198.622| N/A|  37,589|
| |Stutsman County|     2| 96.600| N/A|   118|  5699.382| N/A|  20,704|
| |Ramsey County|     2| 173.626| N/A|    47|  4080.215| N/A|  11,519|
| |Emmons County|     1| 308.547| N/A|    16|  4936.748| N/A|   3,241|
| |McHenry County|     1| 174.064| N/A|    15|  2610.966| N/A|   5,745|
| |McIntosh County|     1| 400.481| N/A|    26| 10412.495| N/A|   2,497|
| |McKenzie County|     1| 66.560| N/A|    79|  5258.253| N/A|  15,024|
| |Benson County|     1| 146.370| N/A|    94| 13758.782| N/A|   6,832|
| |Ward County|     1| 14.784| N/A|   191|  2823.731| N/A|  67,641|
| |Mountrail County|     1| 94.832| N/A|   119| 11284.969| N/A|  10,545|
| |Divide County|     0|  0.000| N/A|     1|   441.696| N/A|   2,264|
| |Dunn County|     0|  0.000| N/A|    30|  6781.193| N/A|   4,424|
| |Eddy County|     0|  0.000| N/A|    13|  5684.303| N/A|   2,287|
| |Towner County|     0|  0.000| N/A|     5|  2284.148| N/A|   2,189|
| |Traill County|     0|  0.000| N/A|    46|  5724.241| N/A|   8,036|
| |Wells County|     0|  0.000| N/A|    17|  4434.011| N/A|   3,834|
| |Walsh County|     0|  0.000| N/A|    98|  9209.661| N/A|  10,641|
| |Foster County|     0|  0.000| N/A|    19|  5919.003| N/A|   3,210|
| |LaMoure County|     0|  0.000| N/A|    14|  3460.208| N/A|   4,046|
| |Logan County|     0|  0.000| N/A|     6|  3243.243| N/A|   1,850|
| |Kidder County|     0|  0.000| N/A|    11|  4435.484| N/A|   2,480|
| |Hettinger County|     0|  0.000| N/A|     6|  2400.960| N/A|   2,499|
| |Griggs County|     0|  0.000| N/A|    30| 13446.885| N/A|   2,231|
| |Grant County|     0|  0.000| N/A|     4|  1759.015| N/A|   2,274|
| |Golden Valley County|     0|  0.000| N/A|     4|  2271.437| N/A|   1,761|
| |Sheridan County|     0|  0.000| N/A|     5|  3802.281| N/A|   1,315|
| |Sioux County|     0|  0.000| N/A|    59| 13947.991| N/A|   4,230|
| |Slope County|     0|  0.000| N/A|     3|  4000.000| N/A|     750|
| |Steele County|     0|  0.000| N/A|    11|  5820.106| N/A|   1,890|
| |Dickey County|     0|  0.000| N/A|    11|  2257.800| N/A|   4,872|
| |Mercer County|     0|  0.000| N/A|    23|  2809.332| N/A|   8,187|
| |Cavalier County|     0|  0.000| N/A|    31|  8240.298| N/A|   3,762|
| |Burke County|     0|  0.000| N/A|    22| 10401.891| N/A|   2,115|
| |Bowman County|     0|  0.000| N/A|     6|  1984.127| N/A|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000| N/A|     2|  2155.172| N/A|     928|
| |Barnes County|     0|  0.000| N/A|    34|  3264.522| N/A|  10,415|
| |Adams County|     0|  0.000| N/A|     2|   902.527| N/A|   2,216|
| |McLean County|     0|  0.000| N/A|    39|  4126.984| N/A|   9,450|
| |Nelson County|     0|  0.000| N/A|    18|  6252.171| N/A|   2,879|
| |Oliver County|     0|  0.000| N/A|     7|  3573.252| N/A|   1,959|
| |Sargent County|     0|  0.000| N/A|     9|  2308.876| N/A|   3,898|
| |Rolette County|     0|  0.000| N/A|    34|  2398.420| N/A|  14,176|
| |Richland County|     0|  0.000| N/A|    93|  5748.903| N/A|  16,177|
| |Renville County|     0|  0.000| N/A|     9|  3867.641| N/A|   2,327|
| |Ransom County|     0|  0.000| N/A|    26|  4982.752| N/A|   5,218|
| |Pierce County|     0|  0.000| N/A|    11|  2767.296| N/A|   3,975|
| |Pembina County|     0|  0.000| N/A|    27|  3970.004| N/A|   6,801|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    64| 59.881| N/A| 4,233|  3960.598| N/A|1,068,778|
| |Yellowstone County|    27| 167.390|  2.595| 1,110|  6881.587| 192.188| 161,300|
| |Big Horn County|    11| 825.888| 79.573|   348| 26128.088| 884.281|  13,319|
| |Toole County|     6| 1266.892| N/A|    31|  6545.608| N/A|   4,736|
| |Gallatin County|     3| 26.216| N/A|   868|  7585.158| N/A| 114,434|
| |Lincoln County|     2| 100.100| N/A|    70|  3503.504| N/A|  19,980|
| |Flathead County|     2| 19.267| N/A|   263|  2533.572| N/A| 103,806|
| |Cascade County|     2| 24.580| N/A|   150|  1843.522| N/A|  81,366|
| |Custer County|     2| 175.408| N/A|    52|  4560.603| N/A|  11,402|
| |Richland County|     1| 92.567| N/A|    46|  4258.076| N/A|  10,803|
| |Madison County|     1| 116.279| N/A|    76|  8837.209| N/A|   8,600|
| |Missoula County|     1|  8.361| N/A|   267|  2232.441| N/A| 119,600|
| |Ravalli County|     1| 22.828| N/A|    73|  1666.438| N/A|  43,806|
| |Rosebud County|     1| 111.894| N/A|    22|  2461.676| N/A|   8,937|
| |Sweet Grass County|     1| 267.594| N/A|     4|  1070.377| N/A|   3,737|
| |Lewis and Clark County|     1| 14.403| N/A|   135|  1944.348| N/A|  69,432|
| |Glacier County|     1| 72.711| N/A|    58|  4217.262| N/A|  13,753|
| |Lake County|     1| 32.832| N/A|   164|  5384.464| N/A|  30,458|
| |Beaverhead County|     0|  0.000| N/A|    47|  4971.967| N/A|   9,453|
| |McCone County|     0|  0.000| N/A|     1|   600.962| N/A|   1,664|
| |Mineral County|     0|  0.000| N/A|     0|     0.000| N/A|   4,397|
| |Petroleum County|     0|  0.000| N/A|     0|     0.000| N/A|     487|
| |Park County|     0|  0.000| N/A|    52|  3131.398| N/A|  16,606|
| |Phillips County|     0|  0.000| N/A|     0|     0.000| N/A|   3,954|
| |Pondera County|     0|  0.000| N/A|     9|  1522.585| N/A|   5,911|
| |Powder River County|     0|  0.000| N/A|     1|   594.530| N/A|   1,682|
| |Sheridan County|     0|  0.000| N/A|     3|   906.618| N/A|   3,309|
| |Musselshell County|     0|  0.000| N/A|     2|   431.686| N/A|   4,633|
| |Powell County|     0|  0.000| N/A|     2|   290.276| N/A|   6,890|
| |Wibaux County|     0|  0.000| N/A|     3|  3095.975| N/A|     969|
| |Wheatland County|     0|  0.000| N/A|     3|  1411.101| N/A|   2,126|
| |Valley County|     0|  0.000| N/A|    13|  1757.707| N/A|   7,396|
| |Treasure County|     0|  0.000| N/A|     2|  2873.563| N/A|     696|
| |Teton County|     0|  0.000| N/A|    15|  2440.215| N/A|   6,147|
| |Stillwater County|     0|  0.000| N/A|    19|  1970.546| N/A|   9,642|
| |Silver Bow County|     0|  0.000| N/A|    66|  1890.305| N/A|  34,915|
| |Sanders County|     0|  0.000| N/A|     9|   743.003| N/A|  12,113|
| |Roosevelt County|     0|  0.000| N/A|    19|  1726.645| N/A|  11,004|
| |Prairie County|     0|  0.000| N/A|     0|     0.000| N/A|   1,077|
| |Daniels County|     0|  0.000| N/A|     2|  1183.432| N/A|   1,690|
| |Chouteau County|     0|  0.000| N/A|     7|  1242.236| N/A|   5,635|
| |Carter County|     0|  0.000| N/A|     0|     0.000| N/A|   1,252|
| |Carbon County|     0|  0.000| N/A|    58|  5407.925| N/A|  10,725|
| |Broadwater County|     0|  0.000| N/A|    11|  1763.668| N/A|   6,237|
| |Blaine County|     0|  0.000| N/A|     9|  1347.104| N/A|   6,681|
| |Meagher County|     0|  0.000| N/A|     4|  2148.228| N/A|   1,862|
| |Dawson County|     0|  0.000| N/A|    16|  1857.657| N/A|   8,613|
| |Deer Lodge County|     0|  0.000| N/A|    20|  2188.184| N/A|   9,140|
| |Fergus County|     0|  0.000| N/A|     7|   633.484| N/A|  11,050|
| |Fallon County|     0|  0.000| N/A|     2|   702.741| N/A|   2,846|
| |Liberty County|     0|  0.000| N/A|     1|   427.899| N/A|   2,337|
| |Judith Basin County|     0|  0.000| N/A|     3|  1494.768| N/A|   2,007|
| |Jefferson County|     0|  0.000| N/A|    27|  2209.312| N/A|  12,221|
| |Hill County|     0|  0.000| N/A|    40|  2426.595| N/A|  16,484|
| |Granite County|     0|  0.000| N/A|     8|  2367.564| N/A|   3,379|
| |Golden Valley County|     0|  0.000| N/A|     3|  3654.080| N/A|     821|
| |Garfield County|     0|  0.000| N/A|    12|  9538.951| N/A|   1,258|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    57| 91.348| N/A| 1,419|  2274.079| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   721|  4402.408| 12.270| 163,774|
| |Franklin County|     6| 121.453| N/A|   117|  2368.325| N/A|  49,402|
| |Windham County|     3| 71.053| N/A|   101|  2392.118| N/A|  42,222|
| |Washington County|     2| 34.241| N/A|    49|   838.912| N/A|  58,409|
| |Addison County|     2| 54.382| N/A|    72|  1957.745| N/A|  36,777|
| |Windsor County|     2| 36.323| N/A|    71|  1289.456| N/A|  55,062|
| |Rutland County|     1| 17.185| N/A|    89|  1529.446| N/A|  58,191|
| |Lamoille County|     1| 39.429| N/A|    42|  1656.021| N/A|  25,362|
| |Bennington County|     1| 28.193| N/A|    84|  2368.198| N/A|  35,470|
| |Orange County|     0|  0.000| N/A|    16|   553.787| N/A|  28,892|
| |Essex County|     0|  0.000| N/A|     4|   649.035| N/A|   6,163|
| |Orleans County|     0|  0.000| N/A|    14|   517.809| N/A|  27,037|
| |Caledonia County|     0|  0.000| N/A|    26|   866.869| N/A|  29,993|
| |Grand Isle County|     0|  0.000| N/A|    13|  1796.821| N/A|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    25| 17.657| N/A| 2,425|  1712.725| N/A|1,415,872|
| |Honolulu County|    19| 19.496| N/A| 2,083|  2137.368| N/A| 974,563|
| |Maui County|     6| 35.839| N/A|   178|  1063.213| N/A| 167,417|
| |Hawaii County|     0|  0.000| N/A|   117|   580.608| N/A| 201,513|
| |Kauai County|     0|  0.000| N/A|    47|   650.132| N/A|  72,293|
| |Kalawao County|     0|  0.000| N/A|     0|     0.000| N/A|      86|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 2,848|  4920.874| N/A| 578,759|
| |Johnson County|     1| 118.413| N/A|    22|  2605.092| N/A|   8,445|
| |Fremont County|     0|  0.000| N/A|   488| 12429.638| N/A|  39,261|
| |Crook County|     0|  0.000| N/A|     9|  1186.709| N/A|   7,584|
| |Converse County|     0|  0.000| N/A|    31|  2242.801| N/A|  13,822|
| |Carbon County|     0|  0.000| N/A|    82|  5540.541| N/A|  14,800|
| |Teton County|     0|  0.000| N/A|   358| 15257.416| N/A|  23,464|
| |Sweetwater County|     0|  0.000| N/A|   250|  5904.164| N/A|  42,343|
| |Sublette County|     0|  0.000| N/A|    37|  3763.605| N/A|   9,831|
| |Natrona County|     0|  0.000| N/A|   217|  2717.323| N/A|  79,858|
| |Sheridan County|     0|  0.000| N/A|    61|  2000.984| N/A|  30,485|
| |Platte County|     0|  0.000| N/A|     5|   595.735| N/A|   8,393|
| |Park County|     0|  0.000| N/A|   117|  4007.673| N/A|  29,194|
| |Niobrara County|     0|  0.000| N/A|     2|   848.896| N/A|   2,356|
| |Goshen County|     0|  0.000| N/A|    19|  1438.195| N/A|  13,211|
| |Hot Springs County|     0|  0.000| N/A|    18|  4078.858| N/A|   4,413|
| |Lincoln County|     0|  0.000| N/A|    92|  4639.435| N/A|  19,830|
| |Laramie County|     0|  0.000| N/A|   479|  4814.070| N/A|  99,500|
| |Campbell County|     0|  0.000| N/A|   118|  2546.341| N/A|  46,341|
| |Big Horn County|     0|  0.000| N/A|    36|  3053.435| N/A|  11,790|
| |Albany County|     0|  0.000| N/A|    88|  2263.374| N/A|  38,880|
| |Uinta County|     0|  0.000| N/A|   265| 13101.948| N/A|  20,226|
| |Washakie County|     0|  0.000| N/A|    49|  6278.027| N/A|   7,805|
| |Weston County|     0|  0.000| N/A|     5|   721.813| N/A|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Yukon-Koyukuk Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,230|
| |Northwest Arctic Borough|     0|  0.000| N/A|     0|     0.000| N/A|   7,621|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Valdez-Cordova Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   9,202|
| |Southeast Fairbanks Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   6,893|
| |Skagway Municipality|     0|  0.000| N/A|     0|     0.000| N/A|   1,183|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   6,203|
| |Petersburg Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,266|
| |Fairbanks North Star Borough|     0|  0.000| N/A|     0|     0.000| N/A|  96,849|
| |Lake and Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|   1,592|
| |Kusilvak Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   8,314|
| |Kodiak Island Borough|     0|  0.000| N/A|     0|     0.000| N/A|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000| N/A|     0|     0.000| N/A|  13,901|
| |Kenai Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|  58,708|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Hoonah-Angoon Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   2,148|
| |Haines Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Dillingham Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   4,916|
| |Nome Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  10,004|
| |Denali Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,097|
| |Bristol Bay Borough|     0|  0.000| N/A|     0|     0.000| N/A|     836|
| |Bethel Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,634|
| |Aleutians East Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,337|
| |Matanuska-Susitna Borough|     0|  0.000| N/A|     0|     0.000| N/A| 108,317|
| |North Slope Borough|     0|  0.000| N/A|     0|     0.000| N/A|   9,832|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|17,244| 16277.737| N/A|1,059,361|
| |Washington County|     0|  0.000| N/A|   590|  4698.313| N/A| 125,577|
| |Providence County|     0|  0.000| N/A|14,549| 22770.847| N/A| 638,931|
| |Newport County|     0|  0.000| N/A|   380|  4629.517| N/A|  82,082|
| |Kent County|     0|  0.000| N/A| 1,421|  8649.234| N/A| 164,292|
| |Bristol County|     0|  0.000| N/A|   304|  6270.756| N/A|  48,479|


