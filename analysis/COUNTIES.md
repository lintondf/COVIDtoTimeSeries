# Analysis of US By County #

Updated: at 2020-08-06

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 124,614 deaths (431.695 deaths/million) and 4,111,095 confirmed cases (14241.896 confirmed cases/million).  This group accounts for 80.73% of all US deaths and for 87.62% of all US cases.

23.97% of this group's deaths (19.35% of the total US deaths) occured in 12 counties in 9 states with a combined population of 32,573,893 (9.92% of the total US population):



The next 25.68% of this group's deaths (20.73% of the total US deaths) occured in 33 counties in 14 states with a combined population of 40,700,179 (12.40% of the total US population):



The next 25.21% of this group's deaths (20.35% of the total US deaths) occured in 85 counties in 30 states with a combined population of 66,010,981 (20.11% of the total US population)

The remaining 25.14% of this group's deaths (20.29% of the total US deaths) occured in 860 counties in 50 states with a combined population of 149,377,006 (45.51% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,312 deaths (235.285 deaths/million) and 413,351 confirmed cases (10444.100 confirmed cases/million).  This group accounts for 6.03% of all US deaths and for 8.81% of all US cases.

24.79% of this group's deaths (1.50% of the total US deaths) occured in 55 counties in 16 states with a combined population of 1,809,432 (0.55% of the total US population):



The next 25.16% of this group's deaths (1.52% of the total US deaths) occured in 108 counties in 26 states with a combined population of 3,254,718 (0.99% of the total US population):



The next 25.05% of this group's deaths (1.51% of the total US deaths) occured in 223 counties in 34 states with a combined population of 5,502,937 (1.68% of the total US population)

The remaining 25.00% of this group's deaths (1.51% of the total US deaths) occured in 1,766 counties in 47 states with a combined population of 29,010,377 (8.84% of the total US population) 

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
|NJ|21 counties|15,857| 1785.258| N/A|182,326| 20527.145| N/A|8,882,190|
| |Essex County| 2,106| 2635.877|  2.054|19,588| 24516.412| 36.801| 798,975|
| |Bergen County| 2,041| 2189.440|  0.454|20,609| 22107.869| 31.109| 932,202|
| |Hudson County| 1,503| 2235.307|  1.227|19,544| 29066.421| 23.967| 672,391|
| |Middlesex County| 1,403| 1700.478|  0.000|17,765| 21531.715| 31.666| 825,062|
| |Union County| 1,348| 2422.974|  0.279|16,590| 29819.841| 20.082| 556,341|
| |Passaic County| 1,243| 2476.954|  0.000|17,532| 34936.412| 42.088| 501,826|
| |Ocean County| 1,017| 1674.940|  0.943|10,501| 17294.536| 34.108| 607,186|
| |Monmouth County|   858| 1386.566|  0.000|10,170| 16435.168| 42.825| 618,795|
| |Morris County|   830| 1687.524|  0.864| 7,179| 14596.062| 24.398| 491,845|
| |Mercer County|   620| 1687.396|  5.047| 8,063| 21944.316| 32.659| 367,430|
| |Camden County|   576| 1137.281|  1.444| 8,400| 16585.352| 42.451| 506,471|
| |Somerset County|   558| 1696.389|  0.000| 5,199| 15805.602| 12.160| 328,934|
| |Burlington County|   470| 1055.352|  0.000| 5,880| 13203.128| 55.013| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,420| 12970.759| 51.200| 263,670|
| |Gloucester County|   209| 716.647|  0.000| 3,130| 10732.557| 56.577| 291,636|
| |Sussex County|   196| 1395.137|  0.000| 1,314|  9353.112| 28.793| 140,488|
| |Warren County|   171| 1624.441|  1.490| 1,331| 12644.038|  5.457| 105,267|
| |Cumberland County|   158| 1056.665|  3.544| 3,275| 21902.399| 111.306| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,139|  9158.083|  8.040| 124,371|
| |Cape May County|    87| 945.251|  0.000|   817|  8876.672| 33.950|  92,039|
| |Salem County|    85| 1362.507| 15.070|   880| 14105.955| 65.477|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,291| 631.809| N/A|250,243| 12863.614| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,436| 32010.636| 41.369|1,356,924|
| |Suffolk County| 1,997| 1352.430|  0.106|43,468| 29437.878| 39.931|1,476,601|
| |Westchester County| 1,446| 1494.564|  0.000|36,049| 37259.717| 26.042| 967,506|
| |Queens County|   983| 436.190|  0.838| 7,815|  3467.346| 16.290|2,253,858|
| |Kings County|   929| 362.943|  0.698| 1,341|   523.931|  2.462|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,893| 42644.165| 17.101| 325,789|
| |Erie County|   669| 728.201|  0.000| 8,667|  9433.962| 47.787| 918,702|
| |Bronx County|   648| 457.014|  0.878|26,614| 18765.830| 88.167|1,418,207|
| |Orange County|   489| 1270.328|  0.000|11,105| 28848.652| 12.989| 384,940|
| |New York County|   414| 254.042|  0.488|15,349|  9424.201| 44.277|1,628,706|
| |Monroe County|   277| 373.431|  0.000| 4,821|  6499.319| 35.725| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,515|  7632.544| 30.322| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,557| 15488.515| 61.574| 294,218|
| |Richmond County|   148| 310.474|  0.597| 7,815| 16412.937| 77.112| 476,143|
| |Albany County|   126| 412.431|  0.000| 2,543|  8323.895| 39.279| 305,506|
| |Oneida County|   112| 489.787|  0.000| 2,103|  9196.619| 33.342| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,458|  6966.710| 25.784| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,039| 11482.602| 30.973| 177,573|
| |Broome County|    64| 335.979|  0.000| 1,078|  5659.149| 59.164| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,437| 14615.541| 40.683|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   295|  7310.666|  0.000|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,484| 19673.348|  5.514|  75,432|
| |Steuben County|    42| 440.349|  0.000|   294|  3082.440| 20.969|  95,379|
| |Columbia County|    37| 622.257|  0.000|   529|  8896.588| 61.378|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,041|  6703.198| 19.460| 155,299|
| |Ontario County|    34| 309.719|  0.000|   352|  3206.500|  9.109| 109,777|
| |Warren County|    33| 516.077|  0.000|   302|  4722.883| 12.946|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   748|  4712.880| 33.709| 158,714|
| |Tioga County|    25| 518.640|  0.000|   191|  3962.409| 20.746|  48,203|
| |Fulton County|    24| 449.581|  0.000|   285|  5338.778| 18.942|  53,383|
| |Greene County|    18| 381.453|  0.000|   289|  6124.438|  0.000|  47,188|
| |Madison County|    17| 239.636|  0.000|   405|  5708.969| 31.945|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   739|  3214.958| 16.861| 229,863|
| |Washington County|    14| 228.743|  0.000|   255|  4166.394|  0.000|  61,204|
| |Chautauqua County|     9| 70.920| N/A|   241|  1899.088| N/A| 126,903|
| |Livingston County|     8| 127.158| N/A|   170|  2702.101| N/A|  62,914|
| |Yates County|     7| 280.978| N/A|    56|  2247.822| N/A|  24,913|
| |Cattaraugus County|     6| 78.826| N/A|   164|  2154.578| N/A|  76,117|
| |Chenango County|     6| 127.100| N/A|   212|  4490.859| N/A|  47,207|
| |Otsego County|     5| 84.044| N/A|   115|  1933.001| N/A|  59,493|
| |Wyoming County|     5| 125.442| N/A|   113|  2834.993| N/A|  39,859|
| |Genesee County|     5| 87.291| N/A|   273|  4766.061| N/A|  57,280|
| |Clinton County|     4| 49.699| N/A|   127|  1577.934| N/A|  80,485|
| |Montgomery County|     4| 81.266| N/A|   160|  3250.645| N/A|  49,221|
| |Herkimer County|     4| 65.233| N/A|   262|  4272.738| N/A|  61,319|
| |Delaware County|     4| 90.631| N/A|   104|  2356.406| N/A|  44,135|
| |St. Lawrence County|     4| 37.126| N/A|   262|  2431.780| N/A| 107,740|
| |Chemung County|     3| 35.947| N/A|   163|  1953.125| N/A|  83,456|
| |Wayne County|     3| 33.364| N/A|   248|  2758.068| N/A|  89,918|
| |Oswego County|     3| 25.614| N/A|   249|  2125.952| N/A| 117,124|
| |Seneca County|     3| 88.194| N/A|    86|  2528.222| N/A|  34,016|
| |Cayuga County|     2| 26.118| N/A|   150|  1958.838| N/A|  76,576|
| |Allegany County|     1| 21.696| N/A|    75|  1627.216| N/A|  46,091|
| |Lewis County|     0|  0.000| N/A|    37|  1407.058| N/A|  26,296|
| |Jefferson County|     0|  0.000| N/A|   139|  1265.546| N/A| 109,834|
| |Franklin County|     0|  0.000| N/A|    50|   999.560| N/A|  50,022|
| |Hamilton County|     0|  0.000| N/A|     7|  1585.145| N/A|   4,416|
| |Essex County|     0|  0.000| N/A|    55|  1491.121| N/A|  36,885|
| |Cortland County|     0|  0.000| N/A|    93|  1954.562| N/A|  47,581|
| |Schuyler County|     0|  0.000| N/A|    22|  1235.469| N/A|  17,807|
| |Schoharie County|     0|  0.000| N/A|    68|  2193.619| N/A|  30,999|
| |Tompkins County|     0|  0.000| N/A|   230|  2250.930| N/A| 102,180|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties| 9,684| 245.089| N/A|526,685| 13329.673| N/A|39,512,223|
| |Los Angeles County| 4,760| 474.146|  3.206|195,805| 19504.225| 180.693|10,039,107|
| |Riverside County|   738| 298.719|  0.000|38,487| 15578.338|  0.000|2,470,546|
| |Orange County|   653| 205.624|  0.334|38,066| 11986.679| 117.689|3,175,692|
| |San Diego County|   568| 170.145|  0.562|30,516|  9141.097| 94.808|3,338,330|
| |San Bernardino County|   477| 218.799| 11.621|34,017| 15603.520| 220.865|2,180,085|
| |Imperial County|   232| 1280.247| 33.110| 9,513| 52495.654| 251.446| 181,215|
| |Tulare County|   193| 413.990|  8.580| 9,990| 21428.801|  0.000| 466,195|
| |Alameda County|   192| 114.879|  0.907|11,909|  7125.467| 114.417|1,671,329|
| |Santa Clara County|   192| 99.593|  0.215|11,030|  5721.394| 112.964|1,927,852|
| |San Joaquin County|   180| 236.175|  6.468|11,958| 15689.866|  0.000| 762,148|
| |Kern County|   151| 167.740|  3.240|21,228| 23581.374| 736.501| 900,202|
| |Sacramento County|   148| 95.357|  2.539|10,174|  6555.167| 33.504|1,552,058|
| |Fresno County|   138| 138.124|  0.000|15,759| 15773.180| 387.695| 999,101|
| |Stanislaus County|   135| 245.160| 10.896| 9,308| 16903.352| 237.457| 550,660|
| |Contra Costa County|   131| 113.565|  2.737| 8,176|  7087.833| 99.703|1,153,526|
| |San Mateo County|   120| 156.541|  0.000| 5,744|  7493.089| 86.120| 766,573|
| |Ventura County|    77| 91.016|  0.000| 7,877|  9310.809|  0.000| 846,006|
| |Marin County|    76| 293.634|  9.786| 5,180| 20013.445| 296.835| 258,826|
| |Santa Barbara County|    63| 141.098|  6.719| 6,526| 14615.934|  0.000| 446,499|
| |San Francisco County|    61| 69.196| N/A| 6,989|  7928.090| N/A| 881,549|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993| 238.656| 152,940|
| |Merced County|    51| 183.665|  1.498| 4,583| 16504.610| 1073.178| 277,680|
| |Yolo County|    42| 190.476|  0.706| 1,614|  7319.728| 158.849| 220,500|
| |Sonoma County|    39| 78.894|  1.942| 3,113|  6297.336| 224.544| 494,336|
| |Solano County|    38| 84.889|  0.000| 3,806|  8502.311|  0.000| 447,643|
| |Monterey County|    34| 78.330|  3.890| 4,966| 11440.788| 163.149| 434,061|
| |Madera County|    32| 203.398|  0.000| 2,114| 13436.982|  0.000| 157,327|
| |Placer County|    18| 45.189|  5.021| 1,953|  4902.982| 34.490| 398,329|
| |San Luis Obispo County|    16| 56.515|  1.491| 1,926|  6802.985| 158.770| 283,111|
| |Napa County|     9| 65.339| N/A|   980|  7114.647| N/A| 137,744|
| |Shasta County|     9| 49.978| N/A|   397|  2204.576| N/A| 180,080|
| |Mendocino County|     9| 103.748| N/A|   341|  3930.881| N/A|  86,749|
| |Butte County|     8| 36.499| N/A| 1,012|  4617.083| N/A| 219,186|
| |Sutter County|     6| 61.874| N/A|   840|  8662.384| N/A|  96,971|
| |Humboldt County|     4| 29.508| N/A|   245|  1807.344| N/A| 135,558|
| |Santa Cruz County|     4| 14.641| N/A| 1,196|  4377.537| N/A| 273,213|
| |Colusa County|     4| 185.641| N/A|   357| 16568.432| N/A|  21,547|
| |San Benito County|     4| 63.686| N/A|   689| 10969.940| N/A|  62,808|
| |Yuba County|     4| 50.847| N/A|   533|  6775.309| N/A|  78,668|
| |Mariposa County|     2| 116.259| N/A|    59|  3429.634| N/A|  17,203|
| |Tuolumne County|     2| 36.712| N/A|   144|  2643.269| N/A|  54,478|
| |Calaveras County|     1| 21.784| N/A|   136|  2962.640| N/A|  45,905|
| |Glenn County|     1| 35.220| N/A|   332| 11693.023| N/A|  28,393|
| |El Dorado County|     1|  5.186| N/A|   668|  3463.958| N/A| 192,843|
| |Mono County|     1| 69.233| N/A|   145| 10038.770| N/A|  14,444|
| |Nevada County|     1| 10.025| N/A|   316|  3167.761| N/A|  99,755|
| |Tehama County|     1| 15.365| N/A|   246|  3779.731| N/A|  65,084|
| |Lake County|     1| 15.531| N/A|   211|  3277.110| N/A|  64,386|
| |Inyo County|     1| 55.435| N/A|    64|  3547.869| N/A|  18,039|
| |Siskiyou County|     0|  0.000| N/A|    88|  2021.176| N/A|  43,539|
| |Trinity County|     0|  0.000| N/A|     5|   407.000| N/A|  12,285|
| |Sierra County|     0|  0.000| N/A|     3|   998.336| N/A|   3,005|
| |Plumas County|     0|  0.000| N/A|    33|  1754.666| N/A|  18,807|
| |Modoc County|     0|  0.000| N/A|     4|   452.438| N/A|   8,841|
| |Lassen County|     0|  0.000| N/A|   632| 20671.835| N/A|  30,573|
| |Amador County|     0|  0.000| N/A|   137|  3446.367| N/A|  39,752|
| |Del Norte County|     0|  0.000| N/A|    90|  3236.013| N/A|  27,812|
| |Alpine County|     0|  0.000| N/A|     2|  1771.479| N/A|   1,129|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,650| 1254.987| N/A|118,786| 17234.088| N/A|6,892,503|
| |Middlesex County| 1,989| 1234.101|  1.242|26,027| 16148.797| 44.480|1,611,699|
| |Essex County| 1,186| 1503.104|  1.817|17,494| 22171.415| 102.657| 789,034|
| |Suffolk County| 1,062| 1321.048|  3.732|21,481| 26720.753| 80.885| 803,907|
| |Worcester County|   993| 1195.490|  0.704|13,469| 16215.559| 32.506| 830,622|
| |Norfolk County|   991| 1402.144|  2.830|10,447| 14781.225| 73.574| 706,775|
| |Plymouth County|   714| 1369.910|  1.919| 9,163| 17580.516| 41.870| 521,202|
| |Hampden County|   699| 1498.804|  0.000| 7,499| 16079.439| 47.173| 466,372|
| |Bristol County|   626| 1107.539|  1.233| 9,224| 16319.396| 63.692| 565,217|
| |Barnstable County|   157| 737.124|  0.000| 1,770|  8310.249| 28.166| 212,990|
| |Hampshire County|   127| 789.654|  0.000| 1,145|  7119.319| 27.386| 160,830|
| |Franklin County|    60| 854.944|  0.000|   406|  5785.124|  8.197|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   661|  5290.370| 17.244| 124,944|
| |Dukes County|     0|  0.000| N/A|     0|     0.000| N/A|  17,332|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,545| 595.416| N/A|184,628| 14569.966| N/A|12,671,821|
| |Cook County| 4,902| 951.802|  0.836|107,744| 20920.219| 102.166|5,150,233|
| |DuPage County|   513| 555.844|  1.372|11,689| 12665.223| 115.110| 922,921|
| |Lake County|   440| 631.698|  0.000|12,223| 17548.293| 172.999| 696,535|
| |Will County|   340| 492.224|  0.598| 8,729| 12637.117| 104.075| 690,743|
| |Kane County|   298| 559.726|  0.401| 9,336| 17535.589| 125.855| 532,403|
| |St. Clair County|   156| 600.725|  0.000| 3,696| 14232.573| 164.540| 259,686|
| |Winnebago County|   127| 449.443|  5.551| 3,704| 13108.164| 52.097| 282,572|
| |McHenry County|   114| 370.402|  0.525| 2,991|  9718.170| 84.729| 307,774|
| |Madison County|    73| 277.602|  0.597| 2,266|  8617.084| 167.322| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,698| 15455.754| 71.056| 109,862|
| |Peoria County|    35| 195.335|  0.000| 1,399|  7807.835| 245.684| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,057|  5429.646| 113.011| 194,672|
| |Rock Island County|    32| 225.544|  4.038| 1,615| 11382.939| 133.917| 141,879|
| |DeKalb County|    29| 276.462|  0.000|   871|  8303.383| 128.823| 104,897|
| |Kendall County|    23| 178.308|  0.000| 1,295| 10039.538| 42.639| 128,990|
| |Macon County|    23| 221.135|  0.000|   502|  4826.505| 152.126| 104,009|
| |Boone County|    23| 429.553|  0.000|   739| 13801.733| 74.705|  53,544|
| |Union County|    21| 1261.034|  0.000|   305| 18315.018| 115.927|  16,653|
| |LaSalle County|    20| 184.045|  7.862|   577|  5309.702| 266.677| 108,669|
| |Jackson County|    19| 334.802|  0.000|   658| 11594.714| 158.590|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,576|  7515.893| 138.300| 209,689|
| |Coles County|    19| 375.338|  0.000|   411|  8119.160| 149.452|  50,621|
| |Clinton County|    17| 452.585|  0.000|   353|  9397.796| 188.134|  37,562|
| |Jefferson County|    17| 451.120|  0.000|   191|  5068.464| 57.685|  37,684|
| |Whiteside County|    16| 289.986|  0.000|   320|  5799.728| 93.536|  55,175|
| |McDonough County|    15| 505.357|  0.000|   133|  4480.830| 86.749|  29,682|
| |McLean County|    15| 87.455|  0.000|   584|  3404.910| 63.274| 171,517|
| |Monroe County|    13| 375.321|  0.000|   284|  8199.324| 114.876|  34,637|
| |Cass County|    11| 905.573|  0.000|   203| 16711.945| 91.714|  12,147|
| |Iroquois County|     9| 331.932| N/A|   250|  9220.329| N/A|  27,114|
| |Tazewell County|     8| 60.697| N/A|   406|  3080.355| N/A| 131,803|
| |Montgomery County|     7| 246.357| N/A|   147|  5173.506| N/A|  28,414|
| |Randolph County|     7| 220.250| N/A|   435| 13686.993| N/A|  31,782|
| |Jasper County|     7| 728.408| N/A|    55|  5723.205| N/A|   9,610|
| |Morgan County|     6| 178.264| N/A|   205|  6090.677| N/A|  33,658|
| |Stephenson County|     6| 134.838| N/A|   321|  7213.807| N/A|  44,498|
| |Grundy County|     5| 97.936| N/A|   287|  5621.499| N/A|  51,054|
| |Adams County|     5| 76.412| N/A|   454|  6938.183| N/A|  65,435|
| |Williamson County|     5| 75.078| N/A|   344|  5165.398| N/A|  66,597|
| |Ogle County|     5| 98.730| N/A|   383|  7562.743| N/A|  50,643|
| |Christian County|     4| 123.824| N/A|   117|  3621.842| N/A|  32,304|
| |Carroll County|     3| 209.717| N/A|    46|  3215.659| N/A|  14,305|
| |Fayette County|     3| 140.607| N/A|    58|  2718.410| N/A|  21,336|
| |Macoupin County|     3| 66.776| N/A|   142|  3160.753| N/A|  44,926|
| |Mercer County|     3| 194.338| N/A|    73|  4728.898| N/A|  15,437|
| |Woodford County|     3| 78.005| N/A|   106|  2756.182| N/A|  38,459|
| |Douglas County|     2| 102.749| N/A|   103|  5291.549| N/A|  19,465|
| |Cumberland County|     2| 185.770| N/A|    47|  4365.595| N/A|  10,766|
| |Livingston County|     2| 56.104| N/A|    96|  2692.998| N/A|  35,648|
| |Lee County|     2| 58.658| N/A|   148|  4340.685| N/A|  34,096|
| |Vermilion County|     2| 26.400| N/A|   218|  2877.584| N/A|  75,758|
| |Bureau County|     2| 61.297| N/A|   154|  4719.873| N/A|  32,628|
| |Bond County|     2| 121.758| N/A|    57|  3470.108| N/A|  16,426|
| |Wayne County|     1| 61.671| N/A|    50|  3083.565| N/A|  16,215|
| |Shelby County|     1| 46.224| N/A|    63|  2912.083| N/A|  21,634|
| |Saline County|     1| 42.569| N/A|   115|  4895.492| N/A|  23,491|
| |Perry County|     1| 47.810| N/A|   126|  6024.096| N/A|  20,916|
| |Knox County|     1| 20.121| N/A|   265|  5332.099| N/A|  49,699|
| |Jo Daviess County|     1| 47.092| N/A|   116|  5462.680| N/A|  21,235|
| |Jersey County|     1| 45.928| N/A|    73|  3352.776| N/A|  21,773|
| |Henry County|     1| 20.444| N/A|   208|  4252.448| N/A|  48,913|
| |Hancock County|     1| 56.472| N/A|    35|  1976.508| N/A|  17,708|
| |Effingham County|     1| 29.405| N/A|   119|  3499.177| N/A|  34,008|
| |Ford County|     1| 77.155| N/A|    42|  3240.491| N/A|  12,961|
| |Stark County|     0|  0.000| N/A|     7|  1310.371| N/A|   5,342|
| |Menard County|     0|  0.000| N/A|    49|  4017.711| N/A|  12,196|
| |Massac County|     0|  0.000| N/A|    34|  2468.777| N/A|  13,772|
| |Mason County|     0|  0.000| N/A|    43|  3218.804| N/A|  13,359|
| |Marshall County|     0|  0.000| N/A|    22|  1923.413| N/A|  11,438|
| |Moultrie County|     0|  0.000| N/A|    62|  4275.567| N/A|  14,501|
| |Piatt County|     0|  0.000| N/A|    51|  3120.411| N/A|  16,344|
| |Pike County|     0|  0.000| N/A|    13|   835.422| N/A|  15,561|
| |Pope County|     0|  0.000| N/A|     8|  1915.250| N/A|   4,177|
| |Putnam County|     0|  0.000| N/A|     9|  1568.217| N/A|   5,739|
| |White County|     0|  0.000| N/A|    60|  4432.297| N/A|  13,537|
| |Washington County|     0|  0.000| N/A|    59|  4248.578| N/A|  13,887|
| |Warren County|     0|  0.000| N/A|   184| 10923.771| N/A|  16,844|
| |Wabash County|     0|  0.000| N/A|    33|  2864.583| N/A|  11,520|
| |Scott County|     0|  0.000| N/A|    11|  2221.773| N/A|   4,951|
| |Schuyler County|     0|  0.000| N/A|    17|  2511.820| N/A|   6,768|
| |Richland County|     0|  0.000| N/A|    14|   902.469| N/A|  15,513|
| |Pulaski County|     0|  0.000| N/A|    91| 17057.170| N/A|   5,335|
| |Marion County|     0|  0.000| N/A|   140|  3762.935| N/A|  37,205|
| |Logan County|     0|  0.000| N/A|    87|  3040.045| N/A|  28,618|
| |Fulton County|     0|  0.000| N/A|    28|   815.376| N/A|  34,340|
| |Franklin County|     0|  0.000| N/A|   134|  3483.324| N/A|  38,469|
| |Edwards County|     0|  0.000| N/A|    14|  2189.210| N/A|   6,395|
| |Edgar County|     0|  0.000| N/A|    26|  1515.063| N/A|  17,161|
| |De Witt County|     0|  0.000| N/A|    31|  1982.351| N/A|  15,638|
| |Crawford County|     0|  0.000| N/A|    29|  1553.544| N/A|  18,667|
| |Clay County|     0|  0.000| N/A|    15|  1137.743| N/A|  13,184|
| |Clark County|     0|  0.000| N/A|    70|  4533.385| N/A|  15,441|
| |Calhoun County|     0|  0.000| N/A|     8|  1688.120| N/A|   4,739|
| |Brown County|     0|  0.000| N/A|    13|  1976.285| N/A|   6,578|
| |Alexander County|     0|  0.000| N/A|    36|  6248.915| N/A|   5,761|
| |Greene County|     0|  0.000| N/A|    21|  1619.246| N/A|  12,969|
| |Gallatin County|     0|  0.000| N/A|    45|  9320.630| N/A|   4,828|
| |Hamilton County|     0|  0.000| N/A|    23|  2833.908| N/A|   8,116|
| |Lawrence County|     0|  0.000| N/A|    43|  2742.697| N/A|  15,678|
| |Johnson County|     0|  0.000| N/A|    59|  4751.550| N/A|  12,417|
| |Hardin County|     0|  0.000| N/A|    17|  4449.097| N/A|   3,821|
| |Henderson County|     0|  0.000| N/A|     9|  1354.198| N/A|   6,646|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 7,402| 344.636| N/A|496,692| 23125.900| N/A|21,477,737|
| |Miami-Dade County| 1,724| 634.537|  9.786|124,759| 45918.938| 382.471|2,716,940|
| |Palm Beach County|   861| 575.239|  8.323|34,929| 23336.251| 235.769|1,496,770|
| |Broward County|   765| 391.750|  5.189|58,953| 30189.300| 320.403|1,952,778|
| |Pinellas County|   460| 471.797|  9.429|17,047| 17484.174| 145.075| 974,996|
| |Hillsborough County|   369| 250.685|  6.943|30,798| 20923.009| 236.418|1,471,968|
| |Lee County|   312| 404.891|  8.252|15,874| 20600.148| 97.330| 770,577|
| |Polk County|   286| 394.604|  2.759|13,231| 18255.270| 199.746| 724,777|
| |Orange County|   241| 172.952|  2.512|30,140| 21629.737| 158.240|1,393,452|
| |Manatee County|   187| 463.729|  1.166| 8,887| 22038.274| 191.205| 403,253|
| |Duval County|   162| 169.146|  1.044|22,034| 23005.884| 244.137| 957,755|
| |St. Lucie County|   130| 395.983|  9.138| 5,329| 16232.253| 316.786| 328,297|
| |Collier County|   129| 335.150|  5.498| 9,897| 25713.039| 187.061| 384,902|
| |Sarasota County|   128| 295.106| 16.139| 5,854| 13496.503| 145.445| 433,742|
| |Brevard County|   123| 204.339|  4.727| 5,671|  9421.173| 76.099| 601,942|
| |Volusia County|   118| 213.272|  2.847| 7,288| 13172.259| 186.834| 553,284|
| |Escambia County|   101| 317.295|  5.820| 8,262| 25955.340| 389.572| 318,316|
| |Pasco County|   101| 182.328|  3.610| 6,636| 11979.485| 143.539| 553,947|
| |Seminole County|    89| 188.629|  2.784| 6,760| 14327.316| 133.264| 471,826|
| |Charlotte County|    89| 471.124|  0.000| 2,076| 10989.360| 149.316| 188,910|
| |Osceola County|    88| 234.198| 10.645| 9,018| 23999.936| 314.038| 375,751|
| |Martin County|    80| 496.894|  8.313| 3,658| 22720.497| 65.217| 161,000|
| |Marion County|    76| 207.889| 17.370| 5,434| 14864.092| 346.715| 365,579|
| |Lake County|    52| 141.644|  0.000| 4,769| 12990.374| 145.610| 367,118|
| |Indian River County|    50| 312.650|  5.300| 2,369| 14813.379| 208.120| 159,923|
| |Clay County|    49| 223.487|  4.561| 2,984| 13609.910| 186.026| 219,252|
| |Sumter County|    38| 286.966| 17.229| 1,163|  8782.661| 178.504| 132,420|
| |Bay County|    37| 211.786|  3.981| 3,921| 22443.548| 709.768| 174,705|
| |Hernando County|    37| 190.800|  8.757| 1,802|  9292.492| 149.422| 193,920|
| |Suwannee County|    37| 833.014| 54.264| 1,203| 27084.225| 360.855|  44,417|
| |Hendry County|    37| 880.491|  3.733| 1,691| 40240.826| 464.043|  42,022|
| |Okaloosa County|    34| 161.338|  7.919| 3,106| 14738.680| 415.208| 210,738|
| |Citrus County|    34| 227.186| 12.166| 1,322|  8833.533| 153.685| 149,657|
| |Jackson County|    33| 710.992|  3.470| 1,643| 35398.802| 538.631|  46,414|
| |St. Johns County|    30| 113.348|  3.778| 3,422| 12929.210| 189.397| 264,672|
| |Highlands County|    30| 282.430|  3.916| 1,296| 12200.977| 262.864| 106,221|
| |Santa Rosa County|    30| 162.767| 14.131| 3,552| 19271.565| 268.921| 184,313|
| |Alachua County|    25| 92.922|  4.258| 3,808| 14153.871| 271.144| 269,043|
| |Gadsden County|    21| 459.921| 12.631| 1,600| 35041.612| 1178.006|  45,660|
| |Putnam County|    20| 268.381| 13.419| 1,397| 18746.394| 345.528|  74,521|
| |DeSoto County|    16| 421.042| 10.946| 1,308| 34420.147| 210.521|  38,001|
| |Washington County|    15| 588.859| 39.257|   676| 26537.903| 1620.828|  25,473|
| |Leon County|    15| 51.093|  0.000| 4,489| 15290.447| 196.610| 293,582|
| |Walton County|    14| 189.008| 13.501| 1,286| 17361.721| 251.783|  74,071|
| |Monroe County|    13| 175.136| 15.435| 1,389| 18712.615| 251.902|  74,228|
| |Columbia County|    13| 181.346| 27.899| 2,637| 36785.425| 431.975|  71,686|
| |Flagler County|    13| 112.964| 17.379|   961|  8350.640| 128.572| 115,081|
| |Nassau County|    11| 124.118|  5.304| 1,138| 12840.621| 212.771|  88,625|
| |Madison County|     8| 432.596| N/A|   661| 35743.254| N/A|  18,493|
| |Hardee County|     7| 259.866| N/A|   857| 31814.976| N/A|  26,937|
| |Calhoun County|     7| 496.278| N/A|   333| 23608.649| N/A|  14,105|
| |Okeechobee County|     6| 142.288| N/A|   967| 22932.081| N/A|  42,168|
| |Jefferson County|     5| 350.976| N/A|   417| 29271.374| N/A|  14,246|
| |Levy County|     4| 96.379| N/A|   627| 15107.342| N/A|  41,503|
| |Dixie County|     4| 237.727| N/A|   284| 16878.640| N/A|  16,826|
| |Baker County|     4| 136.939| N/A|   423| 14481.342| N/A|  29,210|
| |Bradford County|     4| 141.839| N/A|   341| 12091.770| N/A|  28,201|
| |Union County|     4| 262.519| N/A|   227| 14897.946| N/A|  15,237|
| |Taylor County|     4| 185.451| N/A|   551| 25545.922| N/A|  21,569|
| |Wakulla County|     4| 118.557| N/A|   627| 18583.835| N/A|  33,739|
| |Glades County|     3| 217.218| N/A|   392| 28383.173| N/A|  13,811|
| |Hamilton County|     3| 207.929| N/A|   592| 41031.328| N/A|  14,428|
| |Gilchrist County|     3| 161.447| N/A|   334| 17974.384| N/A|  18,582|
| |Holmes County|     2| 101.952| N/A|   457| 23296.121| N/A|  19,617|
| |Franklin County|     2| 164.948| N/A|   189| 15587.629| N/A|  12,125|
| |Gulf County|     2| 146.638| N/A|   415| 30427.451| N/A|  13,639|
| |Liberty County|     2| 239.406| N/A|   418| 50035.911| N/A|   8,354|
| |Lafayette County|     1| 118.737| N/A|   113| 13417.241| N/A|   8,422|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,248| 566.162| N/A|119,724|  9351.984| N/A|12,801,989|
| |Philadelphia County| 1,695| 1070.033| N/A|30,771| 19425.352| N/A|1,584,064|
| |Montgomery County|   851| 1024.172|  0.555| 9,908| 11924.204| 41.981| 830,915|
| |Delaware County|   693| 1222.768|  4.744| 8,956| 15802.466| 134.099| 566,747|
| |Bucks County|   580| 923.170|  1.592| 7,056| 11230.840| 49.770| 628,270|
| |Lancaster County|   408| 747.631|  0.766| 5,705| 10454.002| 60.857| 545,724|
| |Berks County|   367| 871.395|  0.000| 5,248| 12460.704| 65.740| 421,164|
| |Chester County|   348| 662.871|  0.000| 5,014|  9550.676| 83.130| 524,989|
| |Lehigh County|   335| 907.077|  0.000| 4,871| 13189.176| 39.639| 369,318|
| |Northampton County|   290| 949.932|  0.000| 3,878| 12702.884| 35.732| 305,285|
| |Allegheny County|   237| 194.894|  2.467| 8,442|  6942.177| 79.505|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,903|  9075.994|  7.501| 209,674|
| |Luzerne County|   183| 576.529|  0.000| 3,352| 10560.241| 76.907| 317,417|
| |Dauphin County|   156| 560.548|  0.000| 2,702|  9708.982| 64.484| 278,299|
| |Monroe County|   124| 728.251|  0.000| 1,608|  9443.769| 45.680| 170,271|
| |York County|    89| 198.193|  2.227| 2,365|  5266.580| 50.378| 449,058|
| |Beaver County|    89| 542.918|  0.000| 1,261|  7692.355| 86.355| 163,929|
| |Cumberland County|    70| 276.276|  0.000| 1,239|  4890.082| 27.628| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,581| 11150.057| 36.164| 141,793|
| |Schuylkill County|    49| 346.635|  0.000|   900|  6366.768| 32.682| 141,359|
| |Westmoreland County|    46| 131.843|  0.000| 1,464|  4196.057| 45.859| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,294|  8346.933| 41.928| 155,027|
| |Columbia County|    35| 538.760|  0.000|   464|  7142.417| 24.321|  64,964|
| |Carbon County|    28| 436.259|  0.000|   364|  5671.372| 28.407|  64,182|
| |Susquehanna County|    27| 669.510| 24.797|   212|  5256.893| 24.615|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003| 10.384|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   342|  3018.562| 25.546| 113,299|
| |Adams County|    20| 194.158|  0.000|   481|  4669.495| 48.539| 103,009|
| |Erie County|    17| 63.026|  1.965| 1,025|  3800.125| 155.712| 269,728|
| |Butler County|    15| 79.850|  0.000|   615|  3273.836| 34.602| 187,853|
| |Lawrence County|    12| 140.331|  0.000|   353|  4128.076| 58.602|  85,512|
| |Northumberland County|    11| 121.088|  0.000|   416|  4579.329| 64.107|  90,843|
| |Washington County|    11| 53.175|  0.000|   773|  3736.737| 43.507| 206,865|
| |Centre County|    10| 61.582|  0.000|   359|  2210.795|  6.158| 162,385|
| |Mercer County|     9| 82.249| N/A|   364|  3326.510| N/A| 109,424|
| |Wayne County|     8| 155.760| N/A|   157|  3056.794| N/A|  51,361|
| |Wyoming County|     8| 298.574| N/A|    58|  2164.664| N/A|  26,794|
| |Armstrong County|     6| 92.686| N/A|   192|  2965.938| N/A|  64,735|
| |Juniata County|     6| 242.297| N/A|   128|  5169.002| N/A|  24,763|
| |Indiana County|     6| 71.367| N/A|   279|  3318.545| N/A|  84,073|
| |Perry County|     5| 108.057| N/A|   120|  2593.361| N/A|  46,272|
| |Clinton County|     5| 129.426| N/A|   115|  2976.807| N/A|  38,632|
| |Huntingdon County|     4| 88.605| N/A|   290|  6423.888| N/A|  45,144|
| |Fayette County|     4| 30.942| N/A|   423|  3272.120| N/A| 129,274|
| |Bedford County|     4| 83.528| N/A|   133|  2777.314| N/A|  47,888|
| |Blair County|     3| 24.625| N/A|   238|  1953.558| N/A| 121,829|
| |Bradford County|     3| 49.732| N/A|    84|  1392.504| N/A|  60,323|
| |Cambria County|     3| 23.043| N/A|   282|  2166.032| N/A| 130,192|
| |Montour County|     3| 164.564| N/A|    94|  5156.336| N/A|  18,230|
| |Somerset County|     3| 40.846| N/A|   128|  1742.753| N/A|  73,447|
| |Tioga County|     3| 73.908| N/A|    36|   886.896| N/A|  40,591|
| |Elk County|     2| 66.867| N/A|    46|  1537.947| N/A|  29,910|
| |Fulton County|     2| 137.646| N/A|    25|  1720.578| N/A|  14,530|
| |Clarion County|     2| 52.032| N/A|    77|  2003.226| N/A|  38,438|
| |Union County|     2| 44.521| N/A|   191|  4251.720| N/A|  44,923|
| |Snyder County|     2| 49.539| N/A|   100|  2476.964| N/A|  40,372|
| |Mifflin County|     1| 21.674| N/A|   111|  2405.826| N/A|  46,138|
| |McKean County|     1| 24.615| N/A|    33|   812.308| N/A|  40,625|
| |Crawford County|     1| 11.816| N/A|   133|  1571.565| N/A|  84,629|
| |Greene County|     1| 27.599| N/A|   110|  3035.906| N/A|  36,233|
| |Jefferson County|     1| 23.028| N/A|    60|  1381.693| N/A|  43,425|
| |Warren County|     1| 25.516| N/A|    20|   510.321| N/A|  39,191|
| |Clearfield County|     0|  0.000| N/A|   142|  1791.685| N/A|  79,255|
| |Venango County|     0|  0.000| N/A|    62|  1223.652| N/A|  50,668|
| |Sullivan County|     0|  0.000| N/A|    10|  1648.533| N/A|   6,066|
| |Potter County|     0|  0.000| N/A|    20|  1210.214| N/A|  16,526|
| |Forest County|     0|  0.000| N/A|     9|  1241.893| N/A|   7,247|
| |Cameron County|     0|  0.000| N/A|     6|  1349.224| N/A|   4,447|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 7,090| 244.517| N/A|466,032| 16072.352| N/A|28,995,881|
| |Harris County|   789| 167.398|  2.885|79,536| 16874.712| 317.899|4,713,325|
| |Dallas County|   722| 273.950|  5.778|52,131| 19780.187| 193.947|2,635,516|
| |Hidalgo County|   656| 755.145|  0.000|17,751| 20433.817| 359.236| 868,707|
| |Bexar County|   646| 322.427| 11.979|41,274| 20600.393| 61.978|2,003,554|
| |Tarrant County|   398| 189.297|  6.183|29,357| 13962.802| 306.300|2,102,515|
| |Cameron County|   383| 905.089| 35.447|14,781| 34929.802| 3812.531| 423,163|
| |El Paso County|   254| 302.656|  3.108|15,142| 18042.558| 288.371| 839,238|
| |Travis County|   240| 188.390|  2.036|21,549| 16915.053| 266.640|1,273,954|
| |Nueces County|   204| 563.079| 27.506|12,813| 35366.305| 488.553| 362,294|
| |Fort Bend County|   146| 179.872|  0.526| 7,287|  8977.587|  0.000| 811,688|
| |Galveston County|   106| 309.816|  8.768| 8,999| 26302.175|  0.000| 342,139|
| |Williamson County|    80| 135.467|  0.796| 5,930| 10041.470| 99.060| 590,551|
| |Webb County|    79| 285.557|  0.000| 6,629| 23961.511| 618.762| 276,652|
| |Brazoria County|    78| 208.409|  8.335| 6,732| 17987.303| 264.519| 374,264|
| |Denton County|    78| 87.916|  2.284| 7,032|  7925.997| 88.447| 887,207|
| |Montgomery County|    73| 120.186|  0.000| 6,397| 10531.931| 127.092| 607,391|
| |Jefferson County|    73| 290.183|  0.000| 5,609| 22296.424| 197.572| 251,565|
| |Collin County|    72| 69.583|  0.000| 6,421|  6205.484| 32.859|1,034,730|
| |Lubbock County|    66| 212.513|  3.220| 5,652| 18198.854| 186.263| 310,569|
| |Comal County|    65| 416.109| 10.678| 1,720| 11010.889|  0.000| 156,209|
| |Ector County|    52| 312.833|  7.467| 3,440| 20695.090| 378.888| 166,223|
| |Starr County|    52| 804.543| 15.472| 1,981| 30649.978| 1346.062|  64,633|
| |Val Verde County|    49| 999.490|  0.000| 1,564| 31902.091| 496.601|  49,025|
| |Maverick County|    46| 783.352|  0.000| 2,210| 37634.958|  0.000|  58,722|
| |Guadalupe County|    45| 269.708|  5.994| 1,610|  9649.559| 32.350| 166,847|
| |Brazos County|    43| 187.600|  0.000| 3,936| 17171.951| 82.842| 229,211|
| |Midland County|    42| 237.514|  0.000| 2,362| 13357.311|  0.000| 176,832|
| |McLennan County|    40| 155.871|  0.000| 4,571| 17812.121| 382.184| 256,623|
| |Potter County|    39| 332.155|  0.000| 3,546| 30200.571| 174.594| 117,415|
| |Walker County|    38| 520.755|  0.000| 2,842| 38946.979| 152.354|  72,971|
| |Washington County|    38| 1059.027|  0.000|   498| 13878.825| 231.402|  35,882|
| |Nacogdoches County|    37| 567.450|  6.379| 1,054| 16164.652| 198.080|  65,204|
| |Angelina County|    37| 426.685|  9.723| 1,745| 20123.393| 1130.139|  86,715|
| |Ellis County|    35| 189.367|  5.410| 2,545| 13769.708| 167.958| 184,826|
| |Hays County|    34| 147.703|  3.667| 4,931| 21421.341| 1178.844| 230,191|
| |Bell County|    33| 90.928|  2.323| 3,598|  9913.921| 119.358| 362,924|
| |Victoria County|    32| 347.509| 18.191| 3,331| 36173.494|  0.000|  92,084|
| |Bowie County|    31| 332.458|  0.000|   706|  7571.452|  0.000|  93,245|
| |Tom Green County|    28| 234.899| 33.557| 2,476| 20771.812| 399.578| 119,200|
| |Liberty County|    28| 317.392| 34.006|   855|  9691.790| 63.292|  88,219|
| |Johnson County|    27| 153.569| 11.375| 1,619|  9208.438| 193.464| 175,817|
| |Hale County|    24| 718.434| 59.869| 1,230| 36819.733| 673.532|  33,406|
| |Medina County|    24| 465.261|  0.000|   615| 11922.301| 214.570|  51,584|
| |Caldwell County|    24| 549.652| 22.902| 1,080| 24734.335| 114.511|  43,664|
| |Matagorda County|    23| 627.678| 23.315|   688| 18775.755| 191.032|  36,643|
| |Wharton County|    23| 553.470| 20.020|   641| 15424.969| 204.543|  41,556|
| |Kaufman County|    22| 161.582| 10.358| 1,900| 13954.786| 616.948| 136,154|
| |Harrison County|    22| 330.564|  0.000|   630|  9466.140| 75.128|  66,553|
| |Taylor County|    21| 152.136| 14.489| 1,106|  8012.519| 72.300| 138,034|
| |Gregg County|    21| 169.430|  0.000| 1,322| 10666.021| 38.069| 123,945|
| |Willacy County|    21| 983.238| 46.821|   614| 28748.010| 547.914|  21,358|
| |Hunt County|    20| 202.852|  0.000| 1,105| 11207.579| 283.993|  98,594|
| |Grimes County|    20| 692.521|  0.000|   854| 29570.637| 173.130|  28,880|
| |Smith County|    18| 77.336|  1.855| 2,369| 10178.259|  0.000| 232,751|
| |Randall County|    18| 130.707|  3.021| 1,623| 11785.380| 134.337| 137,713|
| |Bastrop County|    18| 202.879|  0.000| 1,302| 14674.887| 33.813|  88,723|
| |Deaf Smith County|    17| 916.640|  0.000|   612| 32999.029| 349.830|  18,546|
| |Panola County|    17| 732.948|  0.000|   271| 11684.056| 36.170|  23,194|
| |Orange County|    17| 203.847|  5.122| 1,250| 14988.728| 1455.108|  83,396|
| |San Patricio County|    17| 254.758|  6.234|   834| 12498.127| 277.237|  66,730|
| |Rockwall County|    17| 162.036|  0.000|   737|  7024.734| 68.714| 104,915|
| |Shelby County|    17| 672.628| 39.566|   383| 15153.913| 67.165|  25,274|
| |Lamar County|    16| 320.905|  0.000|   640| 12836.198| 171.637|  49,859|
| |Wilson County|    16| 313.295|  0.000|   422|  8263.168|  0.000|  51,070|
| |Atascosa County|    15| 293.238|  0.000|   413|  8073.818|  0.000|  51,153|
| |Parker County|    15| 104.985| 20.997| 1,123|  7859.852|  0.000| 142,878|
| |DeWitt County|    15| 744.048|  0.000|   626| 31051.587| 4712.302|  20,160|
| |Brown County|    15| 396.155| 10.986|   356|  9402.071|  0.000|  37,864|
| |Lavaca County|    14| 694.651|  0.000|   613| 30415.798| 992.359|  20,154|
| |Titus County|    14| 427.481|  0.000| 1,312| 40061.069|  0.000|  32,750|
| |Fayette County|    13| 512.901|  0.000|   372| 14676.872|  0.000|  25,346|
| |Moore County|    12| 573.066|  0.000| 1,023| 48853.868| 198.712|  20,940|
| |Aransas County|    12| 510.421|  0.000|   158|  6720.544| 84.134|  23,510|
| |Henderson County|    11| 132.951| 24.173|   604|  7300.241| 138.139|  82,737|
| |Jim Wells County|    11| 271.726| 51.930|   637| 15735.389| 568.154|  40,482|
| |Hardin County|    11| 190.966|  0.000|   859| 14912.677| 397.600|  57,602|
| |San Augustine County|    11| 1335.438|  0.000|   156| 18938.934| 121.403|   8,237|
| |Grayson County|    11| 80.756|  0.000| 1,035|  7598.449| 73.415| 136,212|
| |Polk County|    11| 214.204| 16.200|   686| 13358.518| 525.773|  51,353|
| |Red River County|    11| 914.913|  0.000|   134| 11145.305|  0.000|  12,023|
| |Wichita County|    10| 75.626|  1.709|   932|  7048.325| 93.847| 132,230|
| |Anderson County|    10| 173.205| 14.603| 2,329| 40339.482| 664.354|  57,735|
| |Bee County|     9| 276.370| N/A|   669| 20543.528| N/A|  32,565|
| |Hood County|     9| 146.002| N/A|   480|  7786.772| N/A|  61,643|
| |Lamb County|     8| 620.492| N/A|   207| 16055.224| N/A|  12,893|
| |Marion County|     8| 811.853| N/A|   127| 12888.167| N/A|   9,854|
| |Gonzales County|     8| 383.932| N/A|   631| 30282.670| N/A|  20,837|
| |San Jacinto County|     8| 277.210| N/A|   150|  5197.685| N/A|  28,859|
| |Fannin County|     8| 225.263| N/A|   219|  6166.582| N/A|  35,514|
| |Navarro County|     8| 159.639| N/A|   794| 15844.192| N/A|  50,113|
| |Lee County|     8| 464.064| N/A|   154|  8933.233| N/A|  17,239|
| |Uvalde County|     7| 261.770| N/A|   501| 18735.275| N/A|  26,741|
| |Parmer County|     7| 728.787| N/A|   315| 32795.419| N/A|   9,605|
| |Burnet County|     7| 145.364| N/A|   544| 11296.854| N/A|  48,155|
| |Cass County|     7| 233.131| N/A|   158|  5262.106| N/A|  30,026|
| |Andrews County|     6| 320.770| N/A|   268| 14327.720| N/A|  18,705|
| |Houston County|     6| 261.233| N/A|   304| 13235.806| N/A|  22,968|
| |Kleberg County|     6| 195.567| N/A|   375| 12222.947| N/A|  30,680|
| |Kerr County|     6| 114.068| N/A|   372|  7072.243| N/A|  52,600|
| |Palo Pinto County|     6| 205.557| N/A|   224|  7674.124| N/A|  29,189|
| |Sabine County|     6| 569.152| N/A|    49|  4648.074| N/A|  10,542|
| |Jackson County|     5| 338.753| N/A|   344| 23306.233| N/A|  14,760|
| |Floyd County|     5| 875.350| N/A|    85| 14880.952| N/A|   5,712|
| |Cherokee County|     5| 94.974| N/A|   807| 15328.800| N/A|  52,646|
| |Frio County|     5| 246.233| N/A|   476| 23441.347| N/A|  20,306|
| |Wise County|     5| 71.445| N/A|   329|  4701.075| N/A|  69,984|
| |Erath County|     5| 117.102| N/A|   476| 11148.063| N/A|  42,698|
| |Dallam County|     5| 686.153| N/A|   180| 24701.523| N/A|   7,287|
| |Jasper County|     5| 140.730| N/A|   301|  8471.952| N/A|  35,529|
| |Camp County|     5| 381.854| N/A|   218| 16648.847| N/A|  13,094|
| |Coryell County|     5| 65.832| N/A|   620|  8163.158| N/A|  75,951|
| |Burleson County|     5| 271.106| N/A|   232| 12579.298| N/A|  18,443|
| |Zavala County|     5| 422.297| N/A|   183| 15456.081| N/A|  11,840|
| |Blanco County|     5| 419.076| N/A|    98|  8213.897| N/A|  11,931|
| |Karnes County|     5| 320.492| N/A|   344| 22049.869| N/A|  15,601|
| |Gillespie County|     5| 185.268| N/A|   171|  6336.149| N/A|  26,988|
| |Wood County|     5| 109.796| N/A|   302|  6631.678| N/A|  45,539|
| |Calhoun County|     4| 187.882| N/A|   493| 23156.411| N/A|  21,290|
| |Kendall County|     4| 84.333| N/A|   148|  3120.322| N/A|  47,431|
| |Bailey County|     4| 571.429| N/A|   159| 22714.286| N/A|   7,000|
| |Duval County|     4| 358.519| N/A|   152| 13623.734| N/A|  11,157|
| |Newton County|     4| 294.226| N/A|    89|  6546.524| N/A|  13,595|
| |Hockley County|     4| 173.754| N/A|   189|  8209.895| N/A|  23,021|
| |Hill County|     4| 109.143| N/A|   311|  8485.907| N/A|  36,649|
| |Young County|     4| 222.099| N/A|   145|  8051.083| N/A|  18,010|
| |Castro County|     4| 531.208| N/A|   182| 24169.987| N/A|   7,530|
| |Lynn County|     4| 672.156| N/A|    66| 11090.573| N/A|   5,951|
| |Waller County|     4| 72.403| N/A|   413|  7475.654| N/A|  55,246|
| |Dawson County|     4| 314.268| N/A|   137| 10763.671| N/A|  12,728|
| |Crockett County|     3| 866.051| N/A|   156| 45034.642| N/A|   3,464|
| |Bandera County|     3| 129.803| N/A|    83|  3591.208| N/A|  23,112|
| |Howard County|     3| 81.824| N/A|   161|  4391.228| N/A|  36,664|
| |Austin County|     3| 99.893| N/A|   216|  7192.328| N/A|  30,032|
| |Limestone County|     3| 128.003| N/A|   201|  8576.183| N/A|  23,437|
| |Callahan County|     3| 215.162| N/A|    43|  3083.985| N/A|  13,943|
| |Goliad County|     3| 391.747| N/A|    77| 10054.845| N/A|   7,658|
| |Milam County|     3| 120.856| N/A|   327| 13173.267| N/A|  24,823|
| |Van Zandt County|     3| 53.013| N/A|   351|  6202.509| N/A|  56,590|
| |Nolan County|     3| 203.887| N/A|   131|  8903.085| N/A|  14,714|
| |Comanche County|     3| 220.022| N/A|   236| 17308.398| N/A|  13,635|
| |Martin County|     3| 519.841| N/A|    46|  7970.889| N/A|   5,771|
| |Cooke County|     3| 72.715| N/A|   202|  4896.139| N/A|  41,257|
| |Reagan County|     3| 779.423| N/A|    60| 15588.465| N/A|   3,849|
| |Reeves County|     3| 187.782| N/A|   141|  8825.739| N/A|  15,976|
| |Stephens County|     2| 213.538| N/A|    30|  3203.075| N/A|   9,366|
| |Swisher County|     2| 270.380| N/A|    76| 10274.436| N/A|   7,397|
| |Terry County|     2| 162.114| N/A|   121|  9807.895| N/A|  12,337|
| |Trinity County|     2| 136.509| N/A|   152| 10374.718| N/A|  14,651|
| |Tyler County|     2| 92.285| N/A|   115|  5306.386| N/A|  21,672|
| |Upshur County|     2| 47.901| N/A|   194|  4646.373| N/A|  41,753|
| |Madison County|     2| 140.017| N/A|   645| 45155.419| N/A|  14,284|
| |Rusk County|     2| 36.761| N/A|   338|  6212.550| N/A|  54,406|
| |Ochiltree County|     2| 203.335| N/A|    86|  8743.392| N/A|   9,836|
| |Live Oak County|     2| 163.840| N/A|   207| 16957.483| N/A|  12,207|
| |Robertson County|     2| 117.137| N/A|   216| 12650.814| N/A|  17,074|
| |Lampasas County|     2| 93.336| N/A|    83|  3873.437| N/A|  21,428|
| |Chambers County|     2| 45.624| N/A|   912| 20804.343| N/A|  43,837|
| |Brewster County|     2| 217.320| N/A|   186| 20210.801| N/A|   9,203|
| |Bosque County|     2| 107.038| N/A|   135|  7225.047| N/A|  18,685|
| |Culberson County|     2| 921.234| N/A|    16|  7369.876| N/A|   2,171|
| |Crane County|     2| 416.927| N/A|    75| 15634.772| N/A|   4,797|
| |Cottle County|     2| 1430.615| N/A|    14| 10014.306| N/A|   1,398|
| |Colorado County|     2| 93.054| N/A|   257| 11957.381| N/A|  21,493|
| |Hudspeth County|     2| 409.333| N/A|    22|  4502.661| N/A|   4,886|
| |Hutchinson County|     2| 95.520| N/A|   118|  5635.686| N/A|  20,938|
| |Hamilton County|     2| 236.379| N/A|    55|  6500.414| N/A|   8,461|
| |Hansford County|     2| 370.439| N/A|    58| 10742.730| N/A|   5,399|
| |Hartley County|     2| 358.680| N/A|    82| 14705.882| N/A|   5,576|
| |Yoakum County|     2| 229.542| N/A|    89| 10214.622| N/A|   8,713|
| |Zapata County|     2| 141.054| N/A|   160| 11284.294| N/A|  14,179|
| |Garza County|     2| 321.079| N/A|    97| 15572.323| N/A|   6,229|
| |Gray County|     2| 91.383| N/A|   196|  8955.497| N/A|  21,886|
| |Falls County|     2| 115.627| N/A|   112|  6475.111| N/A|  17,297|
| |Wilbarger County|     1| 78.315| N/A|    52|  4072.363| N/A|  12,769|
| |Scurry County|     1| 59.869| N/A|   454| 27180.746| N/A|  16,703|
| |Ward County|     1| 83.347| N/A|    84|  7001.167| N/A|  11,998|
| |McCulloch County|     1| 125.251| N/A|    43|  5385.772| N/A|   7,984|
| |Winkler County|     1| 124.844| N/A|    71|  8863.920| N/A|   8,010|
| |Morris County|     1| 80.723| N/A|    97|  7830.158| N/A|  12,388|
| |Hopkins County|     1| 26.966| N/A|   180|  4853.845| N/A|  37,084|
| |La Salle County|     1| 132.979| N/A|   357| 47473.404| N/A|   7,520|
| |Leon County|     1| 57.458| N/A|   138|  7929.212| N/A|  17,404|
| |Llano County|     1| 45.882| N/A|    86|  3945.859| N/A|  21,795|
| |Schleicher County|     1| 358.038| N/A|    35| 12531.328| N/A|   2,793|
| |Montague County|     1| 50.459| N/A|    60|  3027.551| N/A|  19,818|
| |Upton County|     1| 273.448| N/A|    16|  4375.171| N/A|   3,657|
| |Fisher County|     1| 261.097| N/A|    26|  6788.512| N/A|   3,830|
| |Kenedy County|     1| 2475.248| N/A|     6| 14851.485| N/A|     404|
| |Sutton County|     1| 264.831| N/A|    60| 15889.831| N/A|   3,776|
| |Franklin County|     1| 93.240| N/A|    87|  8111.888| N/A|  10,725|
| |Clay County|     1| 95.502| N/A|    35|  3342.565| N/A|  10,471|
| |Coke County|     1| 295.247| N/A|    40| 11809.861| N/A|   3,387|
| |Concho County|     1| 366.838| N/A|    26|  9537.784| N/A|   2,726|
| |Jim Hogg County|     1| 192.308| N/A|    54| 10384.615| N/A|   5,200|
| |Dimmit County|     1| 98.775| N/A|   131| 12939.550| N/A|  10,124|
| |Dickens County|     1| 452.284| N/A|     4|  1809.136| N/A|   2,211|
| |Eastland County|     1| 54.466| N/A|    58|  3159.041| N/A|  18,360|
| |Hall County|     1| 337.382| N/A|     9|  3036.437| N/A|   2,964|
| |Rains County|     1| 79.911| N/A|    45|  3595.973| N/A|  12,514|
| |Runnels County|     1| 97.428| N/A|   112| 10911.925| N/A|  10,264|
| |Crosby County|     1| 174.307| N/A|    54|  9412.585| N/A|   5,737|
| |Oldham County|     1| 473.485| N/A|    14|  6628.788| N/A|   2,112|
| |Pecos County|     1| 63.199| N/A|   222| 14030.209| N/A|  15,823|
| |Brooks County|     1| 140.984| N/A|    91| 12829.550| N/A|   7,093|
| |Briscoe County|     1| 646.831| N/A|    11|  7115.136| N/A|   1,546|
| |Freestone County|     0|  0.000| N/A|   139|  7049.754| N/A|  19,717|
| |Donley County|     0|  0.000| N/A|    44| 13422.819| N/A|   3,278|
| |Gaines County|     0|  0.000| N/A|   136|  6327.936| N/A|  21,492|
| |Stonewall County|     0|  0.000| N/A|     4|  2962.963| N/A|   1,350|
| |Sterling County|     0|  0.000| N/A|     1|   774.593| N/A|   1,291|
| |Sherman County|     0|  0.000| N/A|    37| 12243.547| N/A|   3,022|
| |Shackelford County|     0|  0.000| N/A|    17|  5206.738| N/A|   3,265|
| |Glasscock County|     0|  0.000| N/A|     6|  4258.339| N/A|   1,409|
| |San Saba County|     0|  0.000| N/A|    22|  3633.361| N/A|   6,055|
| |Edwards County|     0|  0.000| N/A|    25| 12939.959| N/A|   1,932|
| |Delta County|     0|  0.000| N/A|    16|  3001.313| N/A|   5,331|
| |Terrell County|     0|  0.000| N/A|     2|  2577.320| N/A|     776|
| |Borden County|     0|  0.000| N/A|     0|     0.000| N/A|     654|
| |Baylor County|     0|  0.000| N/A|     7|  1994.870| N/A|   3,509|
| |Throckmorton County|     0|  0.000| N/A|     4|  2664.890| N/A|   1,501|
| |Foard County|     0|  0.000| N/A|     2|  1731.602| N/A|   1,155|
| |Hemphill County|     0|  0.000| N/A|    42| 10997.643| N/A|   3,819|
| |Lipscomb County|     0|  0.000| N/A|    15|  4639.654| N/A|   3,233|
| |Knox County|     0|  0.000| N/A|    48| 13100.437| N/A|   3,664|
| |Kinney County|     0|  0.000| N/A|    17|  4635.942| N/A|   3,667|
| |King County|     0|  0.000| N/A|     0|     0.000| N/A|     272|
| |Kimble County|     0|  0.000| N/A|    13|  2997.464| N/A|   4,337|
| |Kent County|     0|  0.000| N/A|     3|  3937.008| N/A|     762|
| |Jones County|     0|  0.000| N/A|   628| 31270.229| N/A|  20,083|
| |Irion County|     0|  0.000| N/A|     9|  5859.375| N/A|   1,536|
| |Jack County|     0|  0.000| N/A|    43|  4812.535| N/A|   8,935|
| |Collingsworth County|     0|  0.000| N/A|     7|  2397.260| N/A|   2,920|
| |Coleman County|     0|  0.000| N/A|    13|  1590.214| N/A|   8,175|
| |Roberts County|     0|  0.000| N/A|     7|  8196.721| N/A|     854|
| |Refugio County|     0|  0.000| N/A|   214| 30800.230| N/A|   6,948|
| |Presidio County|     0|  0.000| N/A|    44|  6563.246| N/A|   6,704|
| |Real County|     0|  0.000| N/A|    77| 22305.910| N/A|   3,452|
| |Somervell County|     0|  0.000| N/A|    61|  6682.734| N/A|   9,128|
| |Archer County|     0|  0.000| N/A|    20|  2338.361| N/A|   8,553|
| |Loving County|     0|  0.000| N/A|     0|     0.000| N/A|     169|
| |Armstrong County|     0|  0.000| N/A|     9|  4769.475| N/A|   1,887|
| |Wheeler County|     0|  0.000| N/A|    32|  6329.114| N/A|   5,056|
| |Carson County|     0|  0.000| N/A|    14|  2362.470| N/A|   5,926|
| |Haskell County|     0|  0.000| N/A|    39|  6892.895| N/A|   5,658|
| |Jeff Davis County|     0|  0.000| N/A|     8|  3518.030| N/A|   2,274|
| |Motley County|     0|  0.000| N/A|     4|  3333.333| N/A|   1,200|
| |Cochran County|     0|  0.000| N/A|    27|  9463.722| N/A|   2,853|
| |Childress County|     0|  0.000| N/A|    36|  4927.457| N/A|   7,306|
| |Mitchell County|     0|  0.000| N/A|    56|  6553.540| N/A|   8,545|
| |Mills County|     0|  0.000| N/A|    16|  3283.398| N/A|   4,873|
| |McMullen County|     0|  0.000| N/A|     8| 10767.160| N/A|     743|
| |Menard County|     0|  0.000| N/A|    17|  7951.356| N/A|   2,138|
| |Mason County|     0|  0.000| N/A|    42|  9826.860| N/A|   4,274|
| |Hardeman County|     0|  0.000| N/A|    16|  4068.141| N/A|   3,933|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,397| 640.542| N/A|88,624|  8874.063| N/A|9,986,857|
| |Wayne County| 2,809| 1605.746|  1.554|27,564| 15756.773| 83.721|1,749,343|
| |Oakland County| 1,126| 895.368|  0.000|14,950| 11887.874| 68.783|1,257,584|
| |Macomb County|   937| 1072.117|  1.144| 9,834| 11252.077| 105.022| 873,972|
| |Genesee County|   295| 726.936|  1.306| 3,558|  8767.585| 67.043| 405,813|
| |Kent County|   154| 234.415|  0.000| 7,294| 11102.739| 83.588| 656,955|
| |Saginaw County|   129| 677.027|  0.000| 1,883|  9882.491| 99.717| 190,539|
| |Washtenaw County|   112| 304.678|  0.000| 2,442|  6643.072| 52.411| 367,601|
| |Kalamazoo County|    82| 309.357|  1.603| 1,568|  5915.508| 38.182| 265,066|
| |Berrien County|    65| 423.726|  0.000| 1,299|  8468.002| 30.504| 153,401|
| |Muskegon County|    58| 334.167|  0.000| 1,131|  6516.253| 18.726| 173,566|
| |Ottawa County|    54| 185.039|  0.000| 1,749|  5993.215| 32.985| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   783|  4920.567| 28.467| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   754|  5620.197| 41.669| 134,159|
| |Jackson County|    33| 208.189|  0.000|   695|  4384.581| 33.370| 158,510|
| |Lapeer County|    32| 365.268|  0.000|   429|  4896.869| 73.562|  87,607|
| |Bay County|    31| 300.603|  0.000|   559|  5420.553| 56.275| 103,126|
| |Ingham County|    30| 102.597|  0.153| 1,500|  5129.854| 30.843| 292,406|
| |Tuscola County|    29| 555.077| 19.141|   322|  6163.269| 132.118|  52,245|
| |Livingston County|    28| 145.837|  0.000|   795|  4140.733| 44.569| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   332|  4873.609| 35.383|  68,122|
| |Hillsdale County|    25| 548.186|  0.000|   253|  5547.637| 21.927|  45,605|
| |Monroe County|    22| 146.179|  0.000|   920|  6112.957| 86.333| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   146|  3586.254| 20.713|  40,711|
| |Clinton County|    13| 163.327|  0.000|   416|  5226.459| 19.201|  79,595|
| |Alpena County|    13| 457.666|  0.000|   125|  4400.634|  0.000|  28,405|
| |Lenawee County|    12| 121.888|  0.000|   404|  4103.564| 20.315|  98,451|
| |Iosco County|    12| 477.574|  0.000|   129|  5133.920|  0.000|  25,127|
| |Cass County|    11| 212.409| 19.310|   295|  5696.410| 35.514|  51,787|
| |Marquette County|    11| 164.920|  0.000|   144|  2158.953| 57.526|  66,699|
| |Van Buren County|    11| 145.355|  0.000|   418|  5523.475| 65.280|  75,677|
| |Midland County|    10| 120.256|  0.000|   313|  3764.010| 156.333|  83,156|
| |Otsego County|    10| 405.383|  0.000|   131|  5310.524|  0.000|  24,668|
| |Isabella County|     9| 128.807| N/A|   202|  2891.001| N/A|  69,872|
| |St. Joseph County|     8| 131.225| N/A|   563|  9234.958| N/A|  60,964|
| |Eaton County|     8| 72.551| N/A|   445|  4035.622| N/A| 110,268|
| |Allegan County|     7| 59.281| N/A|   505|  4276.725| N/A| 118,081|
| |Sanilac County|     6| 145.737| N/A|    99|  2404.664| N/A|  41,170|
| |Oceana County|     6| 226.697| N/A|   466| 17606.831| N/A|  26,467|
| |Ionia County|     5| 77.283| N/A|   269|  4157.843| N/A|  64,697|
| |Crawford County|     5| 356.405| N/A|   100|  7128.092| N/A|  14,029|
| |Grand Traverse County|     5| 53.713| N/A|   202|  2169.990| N/A|  93,088|
| |Huron County|     4| 129.111| N/A|   149|  4809.399| N/A|  30,981|
| |Wexford County|     4| 118.938| N/A|    67|  1992.210| N/A|  33,631|
| |Kalkaska County|     4| 221.754| N/A|    48|  2661.049| N/A|  18,038|
| |Arenac County|     3| 201.572| N/A|    41|  2754.821| N/A|  14,883|
| |Delta County|     3| 83.836| N/A|    83|  2319.472| N/A|  35,784|
| |Clare County|     3| 96.931| N/A|    64|  2067.851| N/A|  30,950|
| |Cheboygan County|     2| 79.126| N/A|    39|  1542.966| N/A|  25,276|
| |Dickinson County|     2| 79.242| N/A|    47|  1862.197| N/A|  25,239|
| |Gladwin County|     2| 78.589| N/A|    55|  2161.185| N/A|  25,449|
| |Charlevoix County|     2| 76.502| N/A|    45|  1721.302| N/A|  26,143|
| |Branch County|     2| 45.959| N/A|   340|  7813.039| N/A|  43,517|
| |Barry County|     2| 32.494| N/A|   167|  2713.241| N/A|  61,550|
| |Mecosta County|     2| 46.027| N/A|    59|  1357.789| N/A|  43,453|
| |Emmet County|     2| 59.853| N/A|    59|  1765.674| N/A|  33,415|
| |Ogemaw County|     2| 95.252| N/A|    53|  2524.170| N/A|  20,997|
| |Missaukee County|     1| 66.146| N/A|    40|  2645.853| N/A|  15,118|
| |Alcona County|     1| 96.108| N/A|    28|  2691.014| N/A|  10,405|
| |Benzie County|     1| 56.287| N/A|    28|  1576.044| N/A|  17,766|
| |Presque Isle County|     1| 79.416| N/A|    18|  1429.479| N/A|  12,592|
| |Gogebic County|     1| 71.556| N/A|   106|  7584.973| N/A|  13,975|
| |Oscoda County|     1| 121.344| N/A|    24|  2912.268| N/A|   8,241|
| |Iron County|     1| 90.367| N/A|    17|  1536.237| N/A|  11,066|
| |Montcalm County|     1| 15.652| N/A|   181|  2833.083| N/A|  63,888|
| |Schoolcraft County|     0|  0.000| N/A|    12|  1482.580| N/A|   8,094|
| |Ontonagon County|     0|  0.000| N/A|     7|  1223.776| N/A|   5,720|
| |Roscommon County|     0|  0.000| N/A|    48|  1998.418| N/A|  24,019|
| |Mason County|     0|  0.000| N/A|    98|  3362.613| N/A|  29,144|
| |Lake County|     0|  0.000| N/A|    18|  1518.603| N/A|  11,853|
| |Newaygo County|     0|  0.000| N/A|   247|  5042.875| N/A|  48,980|
| |Montmorency County|     0|  0.000| N/A|     8|   857.633| N/A|   9,328|
| |Menominee County|     0|  0.000| N/A|   108|  4741.001| N/A|  22,780|
| |Manistee County|     0|  0.000| N/A|    34|  1384.478| N/A|  24,558|
| |Mackinac County|     0|  0.000| N/A|    23|  2129.827| N/A|  10,799|
| |Luce County|     0|  0.000| N/A|     3|   481.618| N/A|   6,229|
| |Leelanau County|     0|  0.000| N/A|    66|  3032.949| N/A|  21,761|
| |Keweenaw County|     0|  0.000| N/A|     3|  1417.769| N/A|   2,116|
| |Osceola County|     0|  0.000| N/A|    70|  2983.802| N/A|  23,460|
| |Houghton County|     0|  0.000| N/A|    48|  1345.141| N/A|  35,684|
| |Chippewa County|     0|  0.000| N/A|    35|   937.107| N/A|  37,349|
| |Baraga County|     0|  0.000| N/A|     5|   609.088| N/A|   8,209|
| |Antrim County|     0|  0.000| N/A|    39|  1672.097| N/A|  23,324|
| |Alger County|     0|  0.000| N/A|     8|   878.349| N/A|   9,108|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,437| 1244.500| N/A|49,868| 13987.093| N/A|3,565,287|
| |Hartford County| 1,412| 1583.457|  0.000|12,711| 14254.474|  0.000| 891,720|
| |Fairfield County| 1,408| 1492.582|  0.000|17,876| 18949.850|  6.360| 943,332|
| |New Haven County| 1,104| 1291.595|  1.175|13,100| 15325.993| 28.306| 854,757|
| |Middlesex County|   191| 1175.848|  0.000| 1,391|  8563.373|  0.000| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,600|  8872.475| 11.091| 180,333|
| |New London County|   103| 388.377|  0.000| 1,421|  5358.099| 24.139| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,053|  6986.419|  0.000| 150,721|
| |Windham County|    15| 128.444|  0.000|   716|  6131.082|  0.000| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 3,937| 846.886| N/A|124,243| 26725.856| N/A|4,648,794|
| |Orleans Parish|   560| 1435.367|  0.000|10,487| 26879.819| 133.459| 390,144|
| |Jefferson Parish|   518| 1197.707|  1.814|14,795| 34208.646| 395.382| 432,493|
| |East Baton Rouge Parish|   329| 747.627|  2.272|11,444| 26005.604| 312.458| 440,059|
| |Caddo Parish|   285| 1186.491|  9.670| 6,324| 26327.622| 487.086| 240,204|
| |St. Tammany Parish|   206| 791.033|  6.023| 4,884| 18754.392| 242.802| 260,419|
| |Calcasieu Parish|   127| 624.275| 29.493| 6,594| 32413.142| 796.319| 203,436|
| |Ouachita Parish|   107| 698.073|  5.399| 4,592| 29958.442| 384.919| 153,279|
| |Rapides Parish|   107| 825.312| 12.192| 3,126| 24111.440| 343.237| 129,648|
| |Lafourche Parish|    96| 983.465|  0.000| 2,656| 27209.212| 450.988|  97,614|
| |Lafayette Parish|    89| 364.172|  6.434| 7,280| 29788.453| 1998.659| 244,390|
| |St. John the Baptist Parish|    88| 2054.299|  0.000| 1,374| 32075.075| 303.476|  42,837|
| |Terrebonne Parish|    80| 724.238| 13.212| 2,866| 25945.809| 384.751| 110,461|
| |St. Landry Parish|    78| 949.783| 24.217| 2,530| 30807.072| 2112.659|  82,124|
| |Acadia Parish|    77| 1241.035| 36.716| 2,513| 40502.861| 1071.803|  62,045|
| |Bossier Parish|    73| 574.627|  1.474| 2,192| 17254.544| 318.800| 127,039|
| |Ascension Parish|    71| 560.804|  0.000| 2,681| 21176.266| 300.148| 126,604|
| |Iberia Parish|    66| 945.153| 20.401| 2,408| 34483.746| 1360.447|  69,830|
| |Tangipahoa Parish|    63| 467.505|  1.157| 3,223| 23916.947| 319.091| 134,758|
| |Washington Parish|    58| 1255.574|  0.000| 1,211| 26215.526| 194.830|  46,194|
| |St. Charles Parish|    50| 941.620|  0.000| 1,397| 26308.851| 315.734|  53,100|
| |Livingston Parish|    49| 348.039|  0.000| 2,718| 19305.486| 209.191| 140,789|
| |St. Mary Parish|    49| 992.948|  0.000| 1,504| 30477.426| 761.824|  49,348|
| |Iberville Parish|    47| 1445.665|  0.000| 1,170| 35987.820| 492.141|  32,511|
| |St. Martin Parish|    42| 786.061|  0.000| 1,580| 29570.848| 739.271|  53,431|
| |West Baton Rouge Parish|    36| 1360.287|  0.000|   675| 25505.384| 386.900|  26,465|
| |East Feliciana Parish|    35| 1829.109|  0.000|   532| 27802.456| 372.552|  19,135|
| |Union Parish|    33| 1492.672|  7.096|   646| 29220.192| 610.639|  22,108|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   747| 34376.438| 563.030|  21,730|
| |St. James Parish|    32| 1516.875| 47.402|   667| 31617.368| 592.165|  21,096|
| |Bienville Parish|    30| 2265.690|  0.000|   354| 26735.141| 90.652|  13,241|
| |Avoyelles Parish|    27| 672.579|  3.880|   981| 24437.027| 554.034|  40,144|
| |Allen Parish|    25| 975.534| 56.949| 1,210| 47215.827| 1828.733|  25,627|
| |De Soto Parish|    24| 873.903|  0.000|   675| 24578.524| 368.611|  27,463|
| |Jefferson Davis Parish|    24| 765.111|  0.000|   974| 31050.752| 318.796|  31,368|
| |Lincoln Parish|    24| 513.457|  3.332|   733| 15681.828| 271.854|  46,742|
| |St. Bernard Parish|    23| 486.834|  0.000| 1,058| 22394.378| 317.501|  47,244|
| |Vernon Parish|    22| 463.851|  3.284|   732| 15433.595| 506.020|  47,429|
| |Assumption Parish|    20| 913.617|  0.000|   557| 25444.246| 171.907|  21,891|
| |Vermilion Parish|    19| 319.269| 13.921| 1,467| 24650.905| 1193.057|  59,511|
| |Plaquemines Parish|    19| 819.071|  0.000|   428| 18450.662| 129.327|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   361| 22929.370| 127.033|  15,744|
| |Beauregard Parish|    17| 453.370| 12.551|   797| 21255.034| 399.158|  37,497|
| |Franklin Parish|    17| 849.363|  7.838|   850| 42468.149| 596.580|  20,015|
| |Natchitoches Parish|    17| 445.516|  0.000|   716| 18764.086| 379.999|  38,158|
| |West Feliciana Parish|    16| 1027.749|  0.000|   328| 21068.859| 128.469|  15,568|
| |Webster Parish|    13| 339.071|  0.000|   840| 21909.233| 234.704|  38,340|
| |Morehouse Parish|    11| 442.229|  0.000|   461| 18533.408| 402.026|  24,874|
| |Red River Parish|    11| 1303.009|  0.000|   192| 22743.426| 177.683|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   227| 14486.280| 159.541|  15,670|
| |Grant Parish|    11| 491.313| 44.165|   284| 12684.801| 89.330|  22,389|
| |Sabine Parish|    10| 418.690| 28.990|   585| 24493.385| 1010.004|  23,884|
| |Concordia Parish|     8| 415.390| N/A|   296| 15369.438| N/A|  19,259|
| |Winn Parish|     7| 503.452| N/A|   399| 28696.778| N/A|  13,904|
| |Richland Parish|     6| 298.181| N/A|   551| 27382.964| N/A|  20,122|
| |Madison Parish|     6| 547.895| N/A|   585| 53419.779| N/A|  10,951|
| |Catahoula Parish|     5| 526.648| N/A|   267| 28123.025| N/A|   9,494|
| |West Carroll Parish|     5| 461.681| N/A|   272| 25115.420| N/A|  10,830|
| |LaSalle Parish|     2| 134.300| N/A|   248| 16653.237| N/A|  14,892|
| |Caldwell Parish|     2| 201.654| N/A|   202| 20367.009| N/A|   9,918|
| |Evangeline Parish|     2| 59.889| N/A|   805| 24105.405| N/A|  33,395|
| |East Carroll Parish|     1| 145.751| N/A|   510| 74333.188| N/A|   6,861|
| |St. Helena Parish|     1| 98.697| N/A|   247| 24378.208| N/A|  10,132|
| |Tensas Parish|     0|  0.000| N/A|    68| 15689.894| N/A|   4,334|
| |Cameron Parish|     0|  0.000| N/A|   167| 23949.520| N/A|   6,973|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 3,844| 528.115| N/A|180,505| 24799.013| N/A|7,278,717|
| |Maricopa County| 2,153| 480.000|  5.262|121,789| 27152.232| 184.821|4,485,414|
| |Pima County|   465| 444.008|  1.196|16,809| 16050.164| 64.930|1,047,279|
| |Yuma County|   267| 1248.907| 19.444|11,217| 52468.111| 175.408| 213,787|
| |Navajo County|   192| 1730.915|  0.000| 5,301| 47789.477| 136.433| 110,924|
| |Mohave County|   157| 739.934|  7.880| 3,048| 14365.094| 48.781| 212,181|
| |Pinal County|   142| 306.835|  1.080| 8,304| 17943.382| 92.468| 462,789|
| |Apache County|   136| 1891.858|  0.000| 3,098| 43095.414| 234.209|  71,887|
| |Coconino County|   117| 815.467|  2.699| 3,013| 21000.028| 111.517| 143,476|
| |Yavapai County|    64| 272.226|  8.507| 1,883|  8009.392| 143.029| 235,099|
| |Cochise County|    50| 397.071|  3.414| 1,554| 12340.973| 103.239| 125,922|
| |Santa Cruz County|    50| 1075.315|  0.000| 2,618| 56303.497| 107.532|  46,498|
| |Gila County|    29| 536.858|  0.000|   846| 15661.446| 134.099|  54,018|
| |Graham County|    11| 283.235| 21.332|   492| 12668.332| 74.355|  38,837|
| |La Paz County|    10| 473.754|  0.000|   476| 22550.692| 67.643|  21,108|
| |Greenlee County|     1| 105.285| N/A|    57|  6001.263| N/A|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 3,829| 360.634| N/A|179,928| 16946.485| N/A|10,617,423|
| |Fulton County|   406| 381.602|  3.721|18,566| 17450.281| 207.719|1,063,937|
| |Cobb County|   304| 399.926|  3.352|12,135| 15964.143| 334.149| 760,141|
| |Gwinnett County|   240| 256.342|  0.000|18,201| 19440.320| 224.299| 936,250|
| |DeKalb County|   229| 301.595|  2.244|12,760| 16805.018| 188.118| 759,297|
| |Dougherty County|   169| 1921.415|  4.477| 2,631| 29912.684| 162.558|  87,956|
| |Clayton County|   102| 349.009|  1.944| 4,626| 15828.589| 182.653| 292,256|
| |Hall County|    86| 420.659| 34.240| 5,657| 27670.575| 320.876| 204,441|
| |Richmond County|    84| 414.778|  2.591| 3,840| 18961.278| 358.083| 202,518|
| |Muscogee County|    83| 423.969|  2.707| 4,390| 22424.388| 218.540| 195,769|
| |Chatham County|    66| 228.034|  0.000| 5,210| 18000.898| 394.354| 289,430|
| |Troup County|    64| 915.306| 14.302| 2,193| 31363.519| 166.203|  69,922|
| |Bibb County|    62| 404.808|  2.716| 3,265| 21317.716| 359.401| 153,159|
| |Bartow County|    61| 566.188|  9.282| 1,675| 15546.975| 315.580| 107,738|
| |Cherokee County|    57| 220.270|  1.680| 2,976| 11500.427| 237.946| 258,773|
| |Sumter County|    56| 1896.762|  0.000|   740| 25064.354| 270.966|  29,524|
| |Houston County|    51| 323.065| 12.669| 1,817| 11509.980| 149.704| 157,863|
| |Douglas County|    50| 341.663|  6.833| 2,400| 16399.828| 259.664| 146,343|
| |Habersham County|    48| 1058.948|  0.000| 1,057| 23318.920| 219.294|  45,328|
| |Carroll County|    47| 391.693|  0.000| 1,760| 14667.645| 126.202| 119,992|
| |Upson County|    46| 1747.720|  0.000|   489| 18579.027| 97.842|  26,320|
| |Henry County|    44| 187.584|  8.527| 3,055| 13024.331| 153.478| 234,561|
| |Mitchell County|    41| 1875.314|  0.000|   631| 28861.547| 301.865|  21,863|
| |Spalding County|    40| 599.673| 14.992|   876| 13132.843| 132.343|  66,703|
| |Thomas County|    40| 899.867| 11.921| 1,021| 22969.112| 279.005|  44,451|
| |Baldwin County|    38| 846.514|  0.000|   978| 21786.589| 259.474|  44,890|
| |Glynn County|    38| 445.528| 36.353| 2,359| 27657.928| 292.056|  85,292|
| |Butts County|    37| 1483.799|  0.000|   468| 18768.046| 80.205|  24,936|
| |Newton County|    36| 322.165|  4.668| 1,645| 14721.148| 227.067| 111,744|
| |Tift County|    35| 861.136|  0.000| 1,264| 31099.301| 205.823|  40,644|
| |Walton County|    35| 370.006|  0.000|   982| 10381.318| 153.806|  94,593|
| |Hancock County|    34| 4020.338|  0.000|   290| 34291.120| 417.744|   8,457|
| |Lowndes County|    34| 289.593|  7.101| 3,007| 25611.979| 187.384| 117,406|
| |Barrow County|    32| 384.431|  0.000| 1,152| 13839.500| 240.269|  83,240|
| |Early County|    31| 3042.198|  0.000|   349| 34249.264| 147.203|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   293| 34345.329| 67.416|   8,531|
| |Whitfield County|    27| 258.057|  0.000| 3,272| 31272.699| 430.038| 104,628|
| |Randolph County|    26| 3835.940|  0.000|   261| 38506.934| 124.772|   6,778|
| |Fayette County|    25| 218.491|  0.000|   994|  8687.217| 117.300| 114,421|
| |Coffee County|    25| 577.727|  0.000| 1,370| 31659.464| 342.295|  43,273|
| |Ware County|    24| 671.629| 11.641| 1,084| 30335.255| 97.946|  35,734|
| |Gordon County|    23| 396.805|  0.000| 1,039| 17925.228| 224.281|  57,963|
| |Worth County|    23| 1135.971|  0.000|   429| 21188.324| 148.170|  20,247|
| |Monroe County|    23| 833.998|  0.000|   433| 15700.921| 253.826|  27,578|
| |Colquitt County|    22| 482.456|  0.000| 1,503| 32960.526| 241.228|  45,600|
| |Coweta County|    22| 148.139|  2.801| 1,373|  9245.231| 124.291| 148,509|
| |Forsyth County|    22| 90.071|  4.048| 1,984|  8122.758| 117.820| 244,252|
| |Lee County|    22| 733.529|  0.000|   522| 17404.641| 145.245|  29,992|
| |Jenkins County|    22| 2535.731|  0.000|   231| 26625.173| 52.744|   8,676|
| |Columbia County|    21| 134.002|  0.000| 2,008| 12813.150| 311.311| 156,714|
| |Paulding County|    19| 112.648|  0.000| 1,495|  8863.619| 189.478| 168,667|
| |Turner County|    18| 2254.227|  0.000|   234| 29304.947| 876.644|   7,985|
| |Wilcox County|    18| 2084.540|  0.000|   169| 19571.511| 182.419|   8,635|
| |Putnam County|    17| 768.570|  0.000|   384| 17360.640| 86.304|  22,119|
| |Clarke County|    17| 132.470|  0.000| 1,794| 13979.475| 179.224| 128,331|
| |Brooks County|    17| 1099.825| 129.391|   375| 24260.853| 121.140|  15,457|
| |Appling County|    17| 924.617| 22.624|   601| 32687.915| 190.362|  18,386|
| |Rockdale County|    16| 176.025|  0.000| 1,198| 13179.898| 163.426|  90,896|
| |Harris County|    16| 454.081|  0.000|   626| 17765.921| 87.608|  35,236|
| |Walker County|    16| 229.355|  0.000|   581|  8328.436| 180.592|  69,761|
| |Floyd County|    15| 152.287|  0.000| 1,307| 13269.305| 211.202|  98,498|
| |Oconee County|    15| 372.393|  0.000|   401|  9955.313| 99.889|  40,280|
| |Dooly County|    14| 1045.556|  0.000|   242| 18073.189|  0.000|  13,390|
| |Crisp County|    14| 625.782|  0.000|   364| 16270.338| 44.699|  22,372|
| |Bulloch County|    13| 163.300|  5.261| 1,123| 14106.622| 138.177|  79,608|
| |Jackson County|    13| 178.138|  0.000|   972| 13319.265| 155.959|  72,977|
| |Peach County|    12| 435.635|  0.000|   336| 12197.778| 200.261|  27,546|
| |Greene County|    11| 600.306|  0.000|   262| 14298.188| 382.013|  18,324|
| |Johnson County|    11| 1140.724| 103.702|   232| 24058.903| 393.035|   9,643|
| |Macon County|    10| 772.380|  0.000|   174| 13439.407|  0.000|  12,947|
| |Lamar County|    10| 524.191| 52.419|   239| 12528.175| 104.838|  19,077|
| |McDuffie County|    10| 469.219| 46.922|   301| 14123.498| 234.610|  21,312|
| |Wilkinson County|    10| 1116.819|  0.000|   188| 20996.203| 335.046|   8,954|
| |Stephens County|    10| 385.728|  0.000|   566| 21832.208| 217.016|  25,925|
| |Polk County|     9| 211.203| N/A|   690| 16192.242| N/A|  42,613|
| |Screven County|     9| 644.422| N/A|   178| 12745.238| N/A|  13,966|
| |Catoosa County|     9| 133.175| N/A|   572|  8464.043| N/A|  67,580|
| |Bryan County|     8| 201.883| N/A|   579| 14611.250| N/A|  39,627|
| |Decatur County|     8| 302.984| N/A|   691| 26170.277| N/A|  26,404|
| |Emanuel County|     8| 353.263| N/A|   444| 19606.111| N/A|  22,646|
| |Jeff Davis County|     7| 463.116| N/A|   404| 26728.415| N/A|  15,115|
| |Jefferson County|     7| 455.670| N/A|   458| 29813.826| N/A|  15,362|
| |Burke County|     7| 312.737| N/A|   424| 18942.948| N/A|  22,383|
| |Oglethorpe County|     7| 458.746| N/A|   190| 12451.668| N/A|  15,259|
| |Toombs County|     7| 260.902| N/A|   667| 24860.231| N/A|  26,830|
| |Telfair County|     7| 441.362| N/A|   256| 16141.236| N/A|  15,860|
| |Union County|     6| 244.788| N/A|   235|  9587.532| N/A|  24,511|
| |Bacon County|     6| 537.442| N/A|   419| 37531.351| N/A|  11,164|
| |Lumpkin County|     6| 178.518| N/A|   309|  9193.692| N/A|  33,610|
| |Haralson County|     6| 201.396| N/A|   199|  6679.646| N/A|  29,792|
| |Pierce County|     6| 308.246| N/A|   382| 19624.968| N/A|  19,465|
| |Cook County|     6| 347.423| N/A|   409| 23682.687| N/A|  17,270|
| |Calhoun County|     6| 969.462| N/A|   195| 31507.513| N/A|   6,189|
| |Meriwether County|     6| 283.460| N/A|   358| 16913.119| N/A|  21,167|
| |Laurens County|     5| 105.161| N/A|   774| 16278.972| N/A|  47,546|
| |Pickens County|     5| 153.417| N/A|   321|  9849.345| N/A|  32,591|
| |Wayne County|     5| 167.073| N/A|   678| 22655.127| N/A|  29,927|
| |White County|     5| 162.348| N/A|   308| 10000.649| N/A|  30,798|
| |Franklin County|     5| 214.142| N/A|   381| 16317.615| N/A|  23,349|
| |Grady County|     5| 202.980| N/A|   425| 17253.278| N/A|  24,633|
| |Stewart County|     5| 755.173| N/A|   251| 37909.681| N/A|   6,621|
| |Bleckley County|     5| 388.410| N/A|   150| 11652.296| N/A|  12,873|
| |Gilmer County|     4| 127.514| N/A|   526| 16768.147| N/A|  31,369|
| |Lanier County|     4| 383.767| N/A|   210| 20147.750| N/A|  10,423|
| |Marion County|     4| 478.526| N/A|   145| 17346.573| N/A|   8,359|
| |Madison County|     4| 133.869| N/A|   356| 11914.324| N/A|  29,880|
| |Pike County|     4| 210.948| N/A|   196| 10336.462| N/A|  18,962|
| |Heard County|     4| 335.486| N/A|   134| 11238.782| N/A|  11,923|
| |Hart County|     4| 152.643| N/A|   272| 10379.699| N/A|  26,205|
| |Lincoln County|     4| 504.987| N/A|   129| 16285.822| N/A|   7,921|
| |Clinch County|     4| 604.412| N/A|   176| 26594.137| N/A|   6,618|
| |Candler County|     4| 370.268| N/A|   232| 21475.516| N/A|  10,803|
| |Camden County|     4| 73.172| N/A|   696| 12731.863| N/A|  54,666|
| |Brantley County|     4| 209.325| N/A|   232| 12140.876| N/A|  19,109|
| |Dodge County|     3| 145.596| N/A|   189|  9172.531| N/A|  20,605|
| |Talbot County|     3| 484.262| N/A|   129| 20823.245| N/A|   6,195|
| |Jones County|     3| 104.402| N/A|   275|  9570.211| N/A|  28,735|
| |Dawson County|     3| 114.907| N/A|   318| 12180.175| N/A|  26,108|
| |Charlton County|     3| 224.014| N/A|   391| 29196.535| N/A|  13,392|
| |Ben Hill County|     3| 179.641| N/A|   361| 21616.766| N/A|  16,700|
| |Baker County|     3| 987.492| N/A|    62| 20408.163| N/A|   3,038|
| |Rabun County|     3| 175.060| N/A|   198| 11553.948| N/A|  17,137|
| |Treutlen County|     3| 434.720| N/A|   101| 14635.560| N/A|   6,901|
| |Twiggs County|     3| 369.458| N/A|    96| 11822.660| N/A|   8,120|
| |Fannin County|     3| 114.556| N/A|   290| 11073.774| N/A|  26,188|
| |Banks County|     3| 155.974| N/A|   246| 12789.851| N/A|  19,234|
| |Wilkes County|     3| 306.843| N/A|   180| 18410.555| N/A|   9,777|
| |McIntosh County|     2| 139.101| N/A|   161| 11197.663| N/A|  14,378|
| |Washington County|     2| 98.164| N/A|   435| 21350.741| N/A|  20,374|
| |Webster County|     2| 767.165| N/A|    39| 14959.724| N/A|   2,607|
| |Taylor County|     2| 249.377| N/A|    74|  9226.933| N/A|   8,020|
| |Murray County|     2| 49.880| N/A|   549| 13692.139| N/A|  40,096|
| |Seminole County|     2| 247.219| N/A|   162| 20024.722| N/A|   8,090|
| |Pulaski County|     2| 179.582| N/A|    87|  7811.799| N/A|  11,137|
| |Liberty County|     2| 32.555| N/A|   643| 10466.347| N/A|  61,435|
| |Atkinson County|     2| 244.948| N/A|   301| 36864.666| N/A|   8,165|
| |Clay County|     2| 705.716| N/A|    85| 29992.943| N/A|   2,834|
| |Echols County|     2| 499.251| N/A|   215| 53669.496| N/A|   4,006|
| |Chattooga County|     2| 80.681| N/A|   199|  8027.754| N/A|  24,789|
| |Evans County|     1| 93.861| N/A|   228| 21400.413| N/A|  10,654|
| |Schley County|     1| 190.223| N/A|    55| 10462.241| N/A|   5,257|
| |Chattahoochee County|     1| 91.684| N/A|   665| 60970.019| N/A|  10,907|
| |Dade County|     1| 62.050| N/A|   114|  7073.716| N/A|  16,116|
| |Effingham County|     1| 15.553| N/A|   657| 10218.365| N/A|  64,296|
| |Long County|     1| 51.127| N/A|   126|  6442.047| N/A|  19,559|
| |Irwin County|     1| 106.202| N/A|   157| 16673.747| N/A|   9,416|
| |Montgomery County|     1| 109.027| N/A|   135| 14718.709| N/A|   9,172|
| |Jasper County|     1| 70.328| N/A|   129|  9072.368| N/A|  14,219|
| |Warren County|     1| 190.331| N/A|    56| 10658.546| N/A|   5,254|
| |Elbert County|     1| 52.100| N/A|   326| 16984.474| N/A|  19,194|
| |Tattnall County|     1| 39.548| N/A|   433| 17124.100| N/A|  25,286|
| |Towns County|     1| 83.077| N/A|   120|  9969.261| N/A|  12,037|
| |Wheeler County|     1| 127.307| N/A|    84| 10693.826| N/A|   7,855|
| |Quitman County|     1| 434.972| N/A|    29| 12614.180| N/A|   2,299|
| |Taliaferro County|     0|  0.000| N/A|    12|  7807.417| N/A|   1,537|
| |Morgan County|     0|  0.000| N/A|   231| 11983.814| N/A|  19,276|
| |Miller County|     0|  0.000| N/A|   131| 22910.108| N/A|   5,718|
| |Glascock County|     0|  0.000| N/A|    23|  7741.501| N/A|   2,971|
| |Crawford County|     0|  0.000| N/A|    90|  7255.724| N/A|  12,404|
| |Berrien County|     0|  0.000| N/A|   265| 13661.906| N/A|  19,397|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,570| 305.413| N/A|95,106|  8136.298| N/A|11,689,100|
| |Franklin County|   515| 391.113|  0.435|17,404| 13217.331| 113.517|1,316,756|
| |Cuyahoga County|   482| 390.261|  1.942|12,881| 10429.351| 96.463|1,235,072|
| |Lucas County|   319| 744.722|  1.802| 5,035| 11754.461| 212.444| 428,348|
| |Mahoning County|   253| 1106.335|  0.000| 2,437| 10656.673| 87.482| 228,683|
| |Hamilton County|   248| 303.374|  1.223| 9,248| 11312.912| 82.750| 817,473|
| |Summit County|   217| 401.099|  0.000| 3,338|  6169.907| 77.894| 541,013|
| |Stark County|   137| 369.665|  5.730| 1,713|  4622.159| 46.209| 370,606|
| |Trumbull County|   105| 530.373|  4.995| 1,451|  7329.245| 76.674| 197,974|
| |Montgomery County|    80| 150.464|  2.877| 4,092|  7696.257| 75.648| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,650|  5325.450| 52.804| 309,833|
| |Portage County|    60| 369.308|  0.000|   724|  4456.317| 36.372| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,583| 15537.430| 60.031| 101,883|
| |Butler County|    60| 156.603|  1.079| 2,743|  7159.375| 78.302| 383,134|
| |Wood County|    58| 443.367|  0.000|   954|  7292.630| 158.788| 130,817|
| |Wayne County|    58| 501.253|  0.000|   508|  4390.286| 63.419| 115,710|
| |Ashtabula County|    45| 462.768|  0.000|   544|  5594.348| 28.250|  97,241|
| |Marion County|    44| 675.956|  0.000| 2,896| 44490.191| 156.048|  65,093|
| |Licking County|    44| 248.782|  5.654| 1,158|  6547.478| 118.737| 176,862|
| |Geauga County|    44| 469.840| 10.678|   535|  5712.821| 37.638|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,365| 40457.088| 104.760|  58,457|
| |Allen County|    42| 410.353|  0.000|   667|  6516.790| 103.110| 102,351|
| |Miami County|    37| 345.836|  1.466|   781|  7299.952| 60.158| 106,987|
| |Lake County|    36| 156.420|  2.529| 1,054|  4579.642| 43.401| 230,149|
| |Warren County|    35| 149.189|  0.000| 1,669|  7114.176| 137.211| 234,602|
| |Medina County|    33| 183.592|  0.000|   848|  4717.768| 48.551| 179,746|
| |Fairfield County|    27| 171.348|  8.266| 1,264|  8021.628| 79.583| 157,574|
| |Erie County|    27| 363.558|  0.000|   535|  7203.835| 126.596|  74,266|
| |Darke County|    26| 508.677|  0.000|   341|  6671.493| 58.693|  51,113|
| |Belmont County|    26| 388.025|  0.000|   590|  8805.182|  6.182|  67,006|
| |Ottawa County|    25| 616.903|  0.000|   361|  8908.081| 116.534|  40,525|
| |Washington County|    22| 367.211|  2.618|   198|  3304.902| 13.148|  59,911|
| |Delaware County|    18| 86.052|  0.000| 1,219|  5827.601| 62.148| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    91|  6664.714| 34.428|  13,654|
| |Sandusky County|    17| 290.509|  0.000|   343|  5861.444| 170.888|  58,518|
| |Putnam County|    17| 502.053|  0.000|   198|  5847.435| 67.435|  33,861|
| |Tuscarawas County|    14| 152.195| 10.871|   756|  8218.553| 51.343|  91,987|
| |Clark County|    14| 104.413|  7.458| 1,092|  8144.209| 61.023| 134,083|
| |Mercer County|    13| 315.749|  0.000|   535| 12994.268| 157.837|  41,172|
| |Richland County|    12| 99.047|  7.052|   547|  4514.915| 41.270| 121,154|
| |Hardin County|    12| 382.592|  0.000|   153|  4878.049| 40.601|  31,365|
| |Greene County|    11| 65.113|  0.000|   635|  3758.798| 41.804| 168,937|
| |Clermont County|    11| 53.287|  2.069|   859|  4161.257| 55.813| 206,428|
| |Madison County|    10| 223.559|  0.000|   336|  7511.569| 90.814|  44,731|
| |Hocking County|     9| 318.426| N/A|   111|  3927.257| N/A|  28,264|
| |Wyandot County|     7| 321.514| N/A|   125|  5741.319| N/A|  21,772|
| |Knox County|     7| 112.320| N/A|   185|  2968.454| N/A|  62,322|
| |Guernsey County|     7| 180.064| N/A|   112|  2881.029| N/A|  38,875|
| |Holmes County|     6| 136.488| N/A|   322|  7324.841| N/A|  43,960|
| |Coshocton County|     6| 163.934| N/A|   185|  5054.645| N/A|  36,600|
| |Clinton County|     6| 142.966| N/A|   153|  3645.635| N/A|  41,968|
| |Crawford County|     5| 120.499| N/A|   168|  4048.778| N/A|  41,494|
| |Auglaize County|     5| 109.515| N/A|   226|  4950.061| N/A|  45,656|
| |Carroll County|     5| 185.777| N/A|   110|  4087.092| N/A|  26,914|
| |Ross County|     4| 52.174| N/A|   419|  5465.265| N/A|  76,666|
| |Huron County|     4| 68.651| N/A|   378|  6487.488| N/A|  58,266|
| |Shelby County|     4| 82.321| N/A|   164|  3375.180| N/A|  48,590|
| |Defiance County|     4| 105.023| N/A|   132|  3465.749| N/A|  38,087|
| |Seneca County|     3| 54.369| N/A|   167|  3026.569| N/A|  55,178|
| |Williams County|     3| 81.762| N/A|   124|  3379.483| N/A|  36,692|
| |Perry County|     3| 83.024| N/A|   109|  3016.550| N/A|  36,134|
| |Jefferson County|     3| 45.924| N/A|   210|  3214.696| N/A|  65,325|
| |Ashland County|     3| 56.092| N/A|   133|  2486.725| N/A|  53,484|
| |Morrow County|     2| 56.612| N/A|   160|  4528.986| N/A|  35,328|
| |Vinton County|     2| 152.847| N/A|    30|  2292.702| N/A|  13,085|
| |Preble County|     2| 48.921| N/A|   172|  4207.231| N/A|  40,882|
| |Champaign County|     2| 51.434| N/A|   150|  3857.529| N/A|  38,885|
| |Adams County|     2| 72.207| N/A|    56|  2021.807| N/A|  27,698|
| |Logan County|     2| 43.791| N/A|   130|  2846.383| N/A|  45,672|
| |Hancock County|     2| 26.391| N/A|   333|  4394.125| N/A|  75,783|
| |Athens County|     1| 15.308| N/A|   350|  5357.662| N/A|  65,327|
| |Brown County|     1| 23.024| N/A|   118|  2716.891| N/A|  43,432|
| |Scioto County|     1| 13.278| N/A|   199|  2642.271| N/A|  75,314|
| |Muskingum County|     1| 11.599| N/A|   199|  2308.183| N/A|  86,215|
| |Fulton County|     1| 23.738| N/A|   141|  3347.102| N/A|  42,126|
| |Gallia County|     1| 33.447| N/A|    58|  1939.929| N/A|  29,898|
| |Harrison County|     1| 66.489| N/A|    21|  1396.277| N/A|  15,040|
| |Henry County|     1| 37.029| N/A|   108|  3999.111| N/A|  27,006|
| |Highland County|     1| 23.169| N/A|   136|  3150.993| N/A|  43,161|
| |Van Wert County|     1| 35.367| N/A|    70|  2475.685| N/A|  28,275|
| |Union County|     1| 16.953| N/A|   222|  3763.477| N/A|  58,988|
| |Fayette County|     0|  0.000| N/A|   102|  3575.811| N/A|  28,525|
| |Jackson County|     0|  0.000| N/A|    68|  2097.924| N/A|  32,413|
| |Lawrence County|     0|  0.000| N/A|   225|  3783.866| N/A|  59,463|
| |Pike County|     0|  0.000| N/A|    70|  2520.524| N/A|  27,772|
| |Paulding County|     0|  0.000| N/A|    62|  3320.480| N/A|  18,672|
| |Noble County|     0|  0.000| N/A|    16|  1109.262| N/A|  14,424|
| |Morgan County|     0|  0.000| N/A|    20|  1378.550| N/A|  14,508|
| |Meigs County|     0|  0.000| N/A|    26|  1135.024| N/A|  22,907|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,513| 581.076| N/A|91,854| 15193.328| N/A|6,045,680|
| |Baltimore County|   970| 1172.390|  4.289|24,369| 29453.570| 379.865| 827,370|
| |Montgomery County|   794| 755.695|  1.428|17,910| 17045.974| 88.513|1,050,688|
| |Prince George's County|   744| 818.188|  0.812|23,082| 25383.608| 180.473| 909,327|
| |Anne Arundel County|   218| 376.359|  0.718| 7,071| 12207.502| 110.491| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,016| 11620.246| 34.676| 259,547|
| |Carroll County|   117| 694.580|  0.000| 1,503|  8922.688| 68.050| 168,447|
| |Howard County|   106| 325.463|  0.000| 3,690| 11329.792| 113.229| 325,690|
| |Charles County|    91| 557.403|  0.000| 1,932| 11834.102| 161.368| 163,257|
| |Harford County|    68| 266.206|  0.614| 1,863|  7293.269| 98.040| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   931|  8201.921| 58.181| 113,510|
| |Wicomico County|    44| 424.674|  0.000| 1,309| 12634.038| 71.066| 103,609|
| |Cecil County|    30| 291.673|  0.000|   662|  6436.245| 92.766| 102,855|
| |Washington County|    30| 198.611|  0.000|   986|  6527.683| 26.481| 151,049|
| |Calvert County|    28| 302.621|  0.000|   649|  7014.320| 161.472|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   399|  7919.652| 19.849|  50,381|
| |Kent County|    23| 1184.224|  0.000|   235| 12099.681|  0.000|  19,422|
| |Worcester County|    19| 363.456|  0.000|   639| 12223.583| 490.222|  52,276|
| |Allegany County|    18| 255.624|  0.000|   276|  3919.564| 35.503|  70,416|
| |Dorchester County|     5| 156.597| N/A|   352| 11024.461| N/A|  31,929|
| |Talbot County|     4| 107.582| N/A|   368|  9897.528| N/A|  37,181|
| |Somerset County|     3| 117.114| N/A|   129|  5035.915| N/A|  25,616|
| |Caroline County|     3| 89.804| N/A|   439| 13141.352| N/A|  33,406|
| |Garrett County|     0|  0.000| N/A|    44|  1516.509| N/A|  29,014|
| |Baltimore city|     0|  0.000| N/A|     0|     0.000| N/A| 593,490|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,794| 415.019| N/A|69,255| 10287.099| N/A|6,732,219|
| |Marion County|   724| 750.584|  2.357|15,029| 15580.842| 160.701| 964,582|
| |Lake County|   273| 562.315|  3.493| 7,139| 14704.640| 102.654| 485,493|
| |Allen County|   158| 416.558|  1.122| 3,662|  9654.652| 89.975| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,667| 10539.493| 67.112| 158,167|
| |Hendricks County|   105| 616.519|  0.000| 1,774| 10416.239| 93.946| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,543|  7523.424| 127.215| 338,011|
| |St. Joseph County|    79| 290.627|  0.000| 3,203| 11783.273| 162.687| 271,826|
| |Elkhart County|    77| 373.169|  0.000| 4,630| 22438.585| 111.609| 206,341|
| |Howard County|    65| 787.459|  5.129|   824|  9982.555| 113.133|  82,544|
| |Madison County|    65| 501.663|  1.211|   862|  6652.826| 115.768| 129,569|
| |Delaware County|    52| 455.601|  0.000|   654|  5730.057| 91.996| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   748|  8928.252| 70.364|  83,779|
| |Boone County|    46| 678.036|  0.000|   644|  9492.505| 88.104|  67,843|
| |Clark County|    45| 380.382|  0.000| 1,109|  9374.313| 143.700| 118,302|
| |Floyd County|    45| 573.088| 12.735|   718|  9143.934| 220.467|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,209|  7095.528| 110.280| 170,389|
| |Hancock County|    38| 486.132| 12.793|   628|  8033.978| 102.344|  78,168|
| |Greene County|    34| 1065.096|  0.000|   240|  7518.326| 42.951|  31,922|
| |Decatur County|    32| 1204.865|  0.000|   318| 11973.342| 150.608|  26,559|
| |Morgan County|    32| 453.972|  0.000|   437|  6199.549| 126.843|  70,489|
| |Warrick County|    30| 476.206|  0.000|   528|  8381.218| 208.739|  62,998|
| |Monroe County|    30| 202.114|  0.000|   695|  4682.310| 37.054| 148,431|
| |Grant County|    29| 440.937|  0.000|   507|  7708.799| 72.906|  65,769|
| |Noble County|    29| 607.406| 20.945|   637| 13341.991| 81.175|  47,744|
| |LaPorte County|    29| 263.905|  0.000|   843|  7671.447| 68.119| 109,888|
| |Dearborn County|    28| 566.137|  0.000|   473|  9563.670| 117.926|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   331|  7295.570| 55.747|  45,370|
| |Shelby County|    26| 581.278|  0.000|   522| 11670.281| 126.173|  44,729|
| |Orange County|    24| 1221.623|  0.000|   164|  8347.755| 37.736|  19,646|
| |Marshall County|    22| 475.593|  0.000|   744| 16083.704| 28.131|  46,258|
| |Harrison County|    22| 543.009|  0.000|   300|  7404.665| 148.093|  40,515|
| |Montgomery County|    21| 547.759|  0.000|   342|  8920.653| 52.168|  38,338|
| |Daviess County|    19| 569.698|  0.000|   249|  7466.043| 89.952|  33,351|
| |Henry County|    18| 375.219|  0.000|   364|  7587.760| 39.342|  47,972|
| |Kosciusko County|    13| 163.613|  0.000|   822| 10345.348| 35.782|  79,456|
| |Dubois County|    12| 280.794|  0.000|   643| 15045.863| 215.108|  42,736|
| |Jennings County|    12| 432.666|  0.000|   213|  7679.827| 62.634|  27,735|
| |Perry County|    12| 626.011|  0.000|   172|  8972.821|  0.000|  19,169|
| |Vanderburgh County|    12| 66.134|  0.000| 1,763|  9716.122| 175.117| 181,451|
| |Franklin County|    11| 483.347| 18.278|   229| 10062.396| 500.775|  22,758|
| |Tippecanoe County|    11| 56.199|  0.000| 1,118|  5711.892| 62.153| 195,732|
| |LaGrange County|    10| 252.436|  0.000|   546| 13783.006| 75.731|  39,614|
| |Newton County|    10| 715.103|  0.000|   111|  7937.643| 71.510|  13,984|
| |Scott County|    10| 418.883|  0.000|   252| 10555.858| 108.189|  23,873|
| |Vigo County|    10| 93.425|  0.000|   509|  4755.321| 191.521| 107,038|
| |White County|    10| 414.903|  0.000|   347| 14397.145| 41.590|  24,102|
| |Wayne County|    10| 151.782| 15.178|   334|  5069.516| 132.691|  65,884|
| |Cass County|     9| 238.796| N/A| 1,754| 46538.778| N/A|  37,689|
| |Putnam County|     8| 212.902| N/A|   233|  6200.766| N/A|  37,576|
| |Ripley County|     7| 247.140| N/A|   190|  6708.092| N/A|  28,324|
| |Starke County|     7| 304.414| N/A|   164|  7131.985| N/A|  22,995|
| |Fayette County|     7| 303.004| N/A|   162|  7012.380| N/A|  23,102|
| |Whitley County|     6| 176.658| N/A|   148|  4357.555| N/A|  33,964|
| |Tipton County|     6| 396.092| N/A|   117|  7723.792| N/A|  15,148|
| |Clay County|     5| 190.658| N/A|   101|  3851.287| N/A|  26,225|
| |Ohio County|     4| 680.851| N/A|    51|  8680.851| N/A|   5,875|
| |Jackson County|     4| 90.434| N/A|   554| 12525.152| N/A|  44,231|
| |Randolph County|     4| 162.173| N/A|   107|  4338.131| N/A|  24,665|
| |Rush County|     4| 241.240| N/A|    80|  4824.799| N/A|  16,581|
| |DeKalb County|     4| 92.007| N/A|   221|  5083.381| N/A|  43,475|
| |Gibson County|     4| 118.839| N/A|   202|  6001.367| N/A|  33,659|
| |Clinton County|     3| 92.595| N/A|   360| 11111.454| N/A|  32,399|
| |Wabash County|     3| 96.787| N/A|   161|  5194.219| N/A|  30,996|
| |Huntington County|     3| 82.147| N/A|   119|  3258.488| N/A|  36,520|
| |Steuben County|     3| 86.720| N/A|   201|  5810.256| N/A|  34,594|
| |Spencer County|     3| 147.951| N/A|   112|  5523.500| N/A|  20,277|
| |Jasper County|     2| 59.591| N/A|   210|  6257.076| N/A|  33,562|
| |Fulton County|     2| 100.130| N/A|   147|  7359.567| N/A|  19,974|
| |Miami County|     2| 56.313| N/A|   259|  7292.488| N/A|  35,516|
| |Jefferson County|     2| 61.904| N/A|   152|  4704.717| N/A|  32,308|
| |Carroll County|     2| 98.731| N/A|   148|  7306.116| N/A|  20,257|
| |Adams County|     2| 55.902| N/A|    82|  2291.975| N/A|  35,777|
| |Blackford County|     2| 170.097| N/A|    55|  4677.666| N/A|  11,758|
| |Wells County|     2| 70.681| N/A|   134|  4735.652| N/A|  28,296|
| |Fountain County|     2| 122.354| N/A|    64|  3915.331| N/A|  16,346|
| |Brown County|     1| 66.260| N/A|    70|  4638.219| N/A|  15,092|
| |Parke County|     1| 59.042| N/A|    48|  2834.032| N/A|  16,937|
| |Sullivan County|     1| 48.382| N/A|    78|  3773.767| N/A|  20,669|
| |Owen County|     1| 48.079| N/A|    82|  3942.497| N/A|  20,799|
| |Pulaski County|     1| 80.952| N/A|    71|  5747.592| N/A|  12,353|
| |Warren County|     1| 120.992| N/A|    19|  2298.851| N/A|   8,265|
| |Washington County|     1| 35.668| N/A|   117|  4173.206| N/A|  28,036|
| |Benton County|     0|  0.000| N/A|    60|  6858.711| N/A|   8,748|
| |Jay County|     0|  0.000| N/A|    81|  3963.594| N/A|  20,436|
| |Knox County|     0|  0.000| N/A|   134|  3661.802| N/A|  36,594|
| |Vermillion County|     0|  0.000| N/A|    42|  2710.027| N/A|  15,498|
| |Union County|     0|  0.000| N/A|    33|  4678.197| N/A|   7,054|
| |Switzerland County|     0|  0.000| N/A|    43|  3999.628| N/A|  10,751|
| |Posey County|     0|  0.000| N/A|   160|  6292.524| N/A|  25,427|
| |Pike County|     0|  0.000| N/A|    47|  3793.688| N/A|  12,389|
| |Crawford County|     0|  0.000| N/A|    44|  4159.970| N/A|  10,577|
| |Martin County|     0|  0.000| N/A|    42|  4095.563| N/A|  10,255|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,244| 262.901| N/A|94,251| 11042.211| N/A|8,535,519|
| |Fairfax County|   535| 466.218|  1.981|16,069| 14003.095| 90.682|1,147,532|
| |Henrico County|   182| 550.151|  0.000| 3,690| 11154.169| 121.664| 330,818|
| |Prince William County|   173| 367.823|  0.918| 9,089| 19324.524| 194.387| 470,335|
| |Arlington County|   136| 574.222|  0.000| 2,973| 12552.672| 98.113| 236,842|
| |Loudoun County|   113| 273.252|  2.418| 5,093| 12315.676| 67.448| 413,538|
| |Chesterfield County|    75| 212.584|  0.000| 4,141| 11737.462| 167.669| 352,802|
| |Alexandria city|    60| 376.345|  3.324| 2,867| 17983.039| 117.085| 159,428|
| |Suffolk city|    49| 531.984|  0.000| 1,141| 12387.632| 281.652|  92,108|
| |Virginia Beach city|    49| 108.895|  2.201| 4,529| 10065.026| 268.904| 449,974|
| |Richmond County|    43| 4765.599|  0.000| 3,332| 369278.510| 2841.724|   9,023|
| |Shenandoah County|    42| 962.949|  0.000|   685| 15705.246| 66.525|  43,616|
| |Spotsylvania County|    34| 249.605|  0.000| 1,375| 10094.336| 148.211| 136,215|
| |Mecklenburg County|    32| 1046.196|  0.000|   311| 10167.718| 57.852|  30,587|
| |Hanover County|    31| 287.660|  0.000|   605|  5614.016| 60.559| 107,766|
| |Chesapeake city|    30| 122.532|  1.699| 2,689| 10982.907| 308.371| 244,835|
| |Harrisonburg city|    29| 547.005|  0.000| 1,065| 20088.275| 144.168|  53,016|
| |Northampton County|    29| 2476.516| 85.397|   295| 25192.143| 85.397|  11,710|
| |Norfolk city|    26| 107.110|  0.000| 3,425| 14109.631| 329.568| 242,742|
| |Galax city|    24| 3781.314| 155.791|   341| 53726.170| 667.721|   6,347|
| |Portsmouth city|    24| 254.243|  0.000| 1,631| 17277.908| 488.679|  94,398|
| |Page County|    24| 1004.100|  0.000|   334| 13973.726| 41.838|  23,902|
| |Colonial Heights city|    21| 1208.981|  0.000|   187| 10765.688| 102.118|  17,370|
| |Manassas city|    20| 486.796|  0.000| 1,614| 39284.410| 59.070|  41,085|
| |Newport News city|    18| 100.432|  0.000| 1,717|  9580.137| 217.604| 179,225|
| |Roanoke County|    18| 191.111|  0.000| 1,369| 14535.069| 191.487|  94,186|
| |Rockingham County|    17| 207.449|  0.000|   919| 11214.429| 109.826|  81,948|
| |James City County|    16| 209.087|  0.000|   572|  7474.877| 134.528|  76,523|
| |Petersburg city|    16| 510.432| 39.811|   478| 15249.155| 350.922|  31,346|
| |Emporia city|    15| 2805.836|  0.000|   171| 31986.532| 471.057|   5,346|
| |Accomack County|    15| 464.166|  0.000| 1,082| 33481.867| 48.765|  32,316|
| |Albemarle County|    14| 128.053|  7.609|   790|  7225.830| 147.883| 109,330|
| |Charlottesville city|    13| 275.039|  0.000|   504| 10663.056| 249.188|  47,266|
| |Southampton County|    13| 737.338|  0.000|   245| 13895.979| 183.911|  17,631|
| |Carroll County|    12| 402.806|  0.000|   304| 10204.424|  0.000|  29,791|
| |Culpeper County|    12| 228.115|  0.000|   962| 18287.235| 103.168|  52,605|
| |Greensville County|    10| 882.145| 37.682|   438| 38637.968| 573.394|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   358| 15700.377| 153.495|  22,802|
| |Sussex County|     9| 806.524| N/A|   280| 25091.854| N/A|  11,159|
| |Nottoway County|     9| 590.861| N/A|   177| 11620.273| N/A|  15,232|
| |Isle of Wight County|     9| 242.529| N/A|   363|  9781.994| N/A|  37,109|
| |Frederick County|     9| 100.769| N/A|   672|  7524.101| N/A|  89,313|
| |Fluvanna County|     8| 293.363| N/A|   175|  6417.308| N/A|  27,270|
| |Buckingham County|     8| 466.527| N/A|   596| 34756.240| N/A|  17,148|
| |Fauquier County|     8| 112.325| N/A|   584|  8199.714| N/A|  71,222|
| |Stafford County|     7| 45.787| N/A| 1,294|  8464.044| N/A| 152,882|
| |Danville city|     7| 174.808| N/A|   347|  8665.468| N/A|  40,044|
| |Hampton city|     7| 52.041| N/A| 1,103|  8200.134| N/A| 134,510|
| |Goochland County|     7| 294.700| N/A|   152|  6399.192| N/A|  23,753|
| |Franklin County|     7| 124.906| N/A|   316|  5638.628| N/A|  56,042|
| |Bedford County|     7| 88.611| N/A|   311|  3936.858| N/A|  78,997|
| |Manassas Park city|     7| 400.503| N/A|   502| 28721.822| N/A|  17,478|
| |Botetourt County|     7| 209.462| N/A|   192|  5745.235| N/A|  33,419|
| |Williamsburg city|     6| 401.230| N/A|   117|  7823.994| N/A|  14,954|
| |Dinwiddie County|     6| 210.202| N/A|   210|  7357.063| N/A|  28,544|
| |Warren County|     6| 149.388| N/A|   351|  8739.169| N/A|  40,164|
| |Henry County|     6| 118.678| N/A|   523| 10344.759| N/A|  50,557|
| |Caroline County|     5| 162.734| N/A|   192|  6248.983| N/A|  30,725|
| |Charles City County|     5| 718.081| N/A|    51|  7324.429| N/A|   6,963|
| |Hopewell city|     5| 221.936| N/A|   259| 11496.294| N/A|  22,529|
| |Grayson County|     5| 321.543| N/A|   144|  9260.450| N/A|  15,550|
| |Falls Church city|     5| 342.067| N/A|    58|  3967.982| N/A|  14,617|
| |King George County|     4| 149.054| N/A|   124|  4620.659| N/A|  26,836|
| |Augusta County|     4| 52.939| N/A|   260|  3441.065| N/A|  75,558|
| |Washington County|     4| 74.432| N/A|   184|  3423.893| N/A|  53,740|
| |Powhatan County|     4| 134.898| N/A|   132|  4451.639| N/A|  29,652|
| |Winchester city|     4| 142.460| N/A|   394| 14032.338| N/A|  28,078|
| |Wythe County|     3| 104.588| N/A|   107|  3730.303| N/A|  28,684|
| |Patrick County|     3| 170.377| N/A|   118|  6701.499| N/A|  17,608|
| |Scott County|     3| 139.108| N/A|    62|  2874.896| N/A|  21,566|
| |Pulaski County|     3| 88.165| N/A|    78|  2292.297| N/A|  34,027|
| |Smyth County|     3| 99.655| N/A|   123|  4085.836| N/A|  30,104|
| |Wise County|     3| 80.250| N/A|   102|  2728.513| N/A|  37,383|
| |York County|     3| 43.937| N/A|   330|  4833.040| N/A|  68,280|
| |Martinsville city|     3| 238.968| N/A|   173| 13780.468| N/A|  12,554|
| |Salem city|     3| 118.572| N/A|   140|  5533.378| N/A|  25,301|
| |Waynesboro city|     3| 132.567| N/A|   167|  7379.585| N/A|  22,630|
| |Orange County|     3| 80.969| N/A|   215|  5802.812| N/A|  37,051|
| |Montgomery County|     3| 30.446| N/A|   288|  2922.819| N/A|  98,535|
| |Alleghany County|     3| 201.884| N/A|    56|  3768.506| N/A|  14,860|
| |Brunswick County|     2| 123.221| N/A|   212| 13061.426| N/A|  16,231|
| |Campbell County|     2| 36.440| N/A|   162|  2951.626| N/A|  54,885|
| |Louisa County|     2| 53.204| N/A|   170|  4522.359| N/A|  37,591|
| |King William County|     2| 116.632| N/A|    78|  4548.635| N/A|  17,148|
| |Lynchburg city|     2| 24.340| N/A|   486|  5914.711| N/A|  82,168|
| |Fredericksburg city|     2| 68.880| N/A|   371| 12777.242| N/A|  29,036|
| |Westmoreland County|     2| 111.019| N/A|   195| 10824.313| N/A|  18,015|
| |Greene County|     2| 100.913| N/A|   151|  7618.952| N/A|  19,819|
| |Gloucester County|     2| 53.550| N/A|   147|  3935.954| N/A|  37,348|
| |Pittsylvania County|     2| 33.138| N/A|   380|  6296.186| N/A|  60,354|
| |Rappahannock County|     2| 271.370| N/A|    40|  5427.408| N/A|   7,370|
| |Prince George County|     2| 52.147| N/A|   340|  8865.017| N/A|  38,353|
| |Surry County|     2| 311.429| N/A|    39|  6072.874| N/A|   6,422|
| |Northumberland County|     2| 165.358| N/A|    69|  5704.837| N/A|  12,095|
| |Amelia County|     1| 76.075| N/A|    73|  5553.442| N/A|  13,145|
| |Lee County|     1| 42.693| N/A|   101|  4312.001| N/A|  23,423|
| |Floyd County|     1| 63.496| N/A|    41|  2603.340| N/A|  15,749|
| |Lunenburg County|     1| 81.994| N/A|    59|  4837.652| N/A|  12,196|
| |Essex County|     1| 91.299| N/A|    83|  7577.833| N/A|  10,953|
| |King and Queen County|     1| 142.349| N/A|    37|  5266.904| N/A|   7,025|
| |Halifax County|     1| 29.489| N/A|   143|  4216.921| N/A|  33,911|
| |Buena Vista city|     1| 154.369| N/A|    48|  7409.694| N/A|   6,478|
| |Madison County|     1| 75.409| N/A|    62|  4675.364| N/A|  13,261|
| |Middlesex County|     1| 94.500| N/A|    29|  2740.503| N/A|  10,582|
| |New Kent County|     1| 43.307| N/A|   121|  5240.137| N/A|  23,091|
| |Russell County|     1| 37.614| N/A|    73|  2745.806| N/A|  26,586|
| |Staunton city|     0|  0.000| N/A|   143|  5735.601| N/A|  24,932|
| |Giles County|     0|  0.000| N/A|    23|  1375.598| N/A|  16,720|
| |Nelson County|     0|  0.000| N/A|    34|  2277.294| N/A|  14,930|
| |Mathews County|     0|  0.000| N/A|    15|  1697.985| N/A|   8,834|
| |Fairfax city|     0|  0.000| N/A|     0|     0.000| N/A|  24,019|
| |Radford city|     0|  0.000| N/A|    33|  1808.318| N/A|  18,249|
| |Roanoke city|     0|  0.000| N/A|     0|     0.000| N/A|  99,143|
| |Richmond city|     0|  0.000| N/A|     0|     0.000| N/A| 230,436|
| |Franklin city|     0|  0.000| N/A|     0|     0.000| N/A|   7,967|
| |Lexington city|     0|  0.000| N/A|    33|  4431.910| N/A|   7,446|
| |Highland County|     0|  0.000| N/A|     4|  1826.484| N/A|   2,190|
| |Norton city|     0|  0.000| N/A|    14|  3516.704| N/A|   3,981|
| |Poquoson city|     0|  0.000| N/A|    40|  3259.718| N/A|  12,271|
| |Covington city|     0|  0.000| N/A|    12|  2166.847| N/A|   5,538|
| |Charlotte County|     0|  0.000| N/A|    49|  4124.579| N/A|  11,880|
| |Bland County|     0|  0.000| N/A|     7|  1114.650| N/A|   6,280|
| |Buchanan County|     0|  0.000| N/A|    73|  3475.528| N/A|  21,004|
| |Cumberland County|     0|  0.000| N/A|    69|  6947.241| N/A|   9,932|
| |Dickenson County|     0|  0.000| N/A|    29|  2025.423| N/A|  14,318|
| |Clarke County|     0|  0.000| N/A|    69|  4719.885| N/A|  14,619|
| |Rockbridge County|     0|  0.000| N/A|    66|  2923.847| N/A|  22,573|
| |Tazewell County|     0|  0.000| N/A|   102|  2512.625| N/A|  40,595|
| |Lancaster County|     0|  0.000| N/A|    32|  3018.014| N/A|  10,603|
| |Bristol city|     0|  0.000| N/A|    66|  3937.478| N/A|  16,762|
| |Amherst County|     0|  0.000| N/A|   124|  3923.430| N/A|  31,605|
| |Craig County|     0|  0.000| N/A|    16|  3118.301| N/A|   5,131|
| |Appomattox County|     0|  0.000| N/A|    72|  4525.171| N/A|  15,911|
| |Bath County|     0|  0.000| N/A|     4|   964.553| N/A|   4,147|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,061| 196.509| N/A|128,715| 12272.499| N/A|10,488,084|
| |Mecklenburg County|   222| 199.936|  0.000|21,316| 19197.447| 197.183|1,110,356|
| |Guilford County|   150| 279.239|  2.792| 5,310|  9885.065| 91.546| 537,174|
| |Wake County|   134| 120.530|  0.513|11,337| 10197.336| 105.047|1,111,761|
| |Durham County|    79| 245.732|  0.000| 5,946| 18495.247| 116.645| 321,488|
| |Henderson County|    54| 459.899|  0.000| 1,420| 12093.649| 203.318| 117,417|
| |Robeson County|    51| 390.431|  0.000| 2,682| 20532.057| 179.904| 130,625|
| |Cumberland County|    50| 149.027|  0.000| 2,833|  8443.887| 147.537| 335,509|
| |Chatham County|    50| 671.411|  0.000| 1,255| 16852.424| 148.683|  74,470|
| |Forsyth County|    49| 128.173|  0.000| 5,007| 13097.216| 107.335| 382,295|
| |Cabarrus County|    49| 226.377|  6.624| 2,504| 11568.331| 143.218| 216,453|
| |Rowan County|    48| 337.819|  0.000| 2,060| 14498.058| 197.061| 142,088|
| |Duplin County|    47| 800.123| 68.096| 1,952| 33230.623| 141.399|  58,741|
| |Buncombe County|    46| 176.116|  0.000| 1,741|  6665.620| 102.613| 261,191|
| |Columbus County|    46| 828.709|  0.000|   838| 15096.923| 108.093|  55,508|
| |Orange County|    45| 303.079|  0.000| 1,296|  8728.683| 36.893| 148,476|
| |Johnston County|    44| 210.185|  0.000| 3,117| 14889.724| 166.406| 209,339|
| |Union County|    42| 175.103|  4.169| 2,881| 12011.223| 165.005| 239,859|
| |Gaston County|    41| 182.604|  7.521| 3,083| 13730.966| 155.882| 224,529|
| |Alamance County|    41| 241.875|  0.000| 2,280| 13450.613| 199.732| 169,509|
| |Vance County|    40| 898.170|  0.000|   739| 16593.690| 90.604|  44,535|
| |Wayne County|    37| 300.493|  0.000| 2,330| 18922.936| 105.579| 123,131|
| |Harnett County|    36| 264.753|  0.000| 1,178|  8663.294| 136.584| 135,976|
| |Randolph County|    36| 250.579|  0.000| 2,075| 14443.122| 67.537| 143,667|
| |Wilson County|    35| 427.868|  0.000| 1,436| 17554.798| 226.159|  81,801|
| |Catawba County|    29| 181.760| 14.732| 1,972| 12359.684| 231.901| 159,551|
| |Burke County|    28| 309.444|  9.442| 1,637| 18091.396| 420.509|  90,485|
| |Granville County|    26| 430.157|  8.767| 1,186| 19621.792| 101.167|  60,443|
| |Franklin County|    25| 358.757|  0.000|   805| 11551.984| 153.570|  69,685|
| |New Hanover County|    20| 85.298|  1.805| 2,449| 10444.699| 213.286| 234,473|
| |Moore County|    20| 198.255|  0.000|   933|  9248.612| 181.546| 100,880|
| |Stanly County|    20| 318.441| 61.211|   928| 14775.658| 240.660|  62,806|
| |Davidson County|    18| 107.393|  2.805| 1,675|  9993.497| 87.585| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,771|  9741.153| 204.292| 181,806|
| |Brunswick County|    17| 119.031|  1.098| 1,202|  8416.188| 56.938| 142,820|
| |Cleveland County|    17| 173.563|  0.000| 1,087| 11097.839| 331.130|  97,947|
| |Pasquotank County|    17| 426.878|  0.000|   360|  9039.775| 93.253|  39,824|
| |Northampton County|    16| 821.229|  0.000|   329| 16886.516|  0.000|  19,483|
| |Rutherford County|    14| 208.865|  6.373|   689| 10279.133| 350.595|  67,029|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 907.587|  27,173|
| |Caldwell County|    14| 170.362| 11.441| 1,154| 14042.688| 194.699|  82,178|
| |Sampson County|    13| 204.625|  6.547| 1,431| 22524.437| 76.332|  63,531|
| |McDowell County|    13| 284.116| 27.007|   618| 13506.425| 152.985|  45,756|
| |Lenoir County|    12| 214.481|  0.000|   538|  9615.900| 33.264|  55,949|
| |Edgecombe County|    12| 233.136| 19.428|   596| 11579.111| 154.540|  51,472|
| |Nash County|    12| 127.256|  0.000| 1,074| 11389.425| 254.512|  94,298|
| |Pitt County|    11| 60.860|  0.000| 1,802|  9970.013| 108.128| 180,742|
| |Lee County|    11| 178.054|  6.733| 1,225| 19828.744| 230.975|  61,779|
| |Hertford County|    11| 464.586|  0.000|   307| 12966.170| 253.410|  23,677|
| |Wilkes County|    10| 146.173|  0.000|   741| 10831.433| 54.718|  68,412|
| |Onslow County|    10| 50.521|  0.000|   961|  4855.056| 76.710| 197,938|
| |Craven County|    10| 97.906|  0.000|   673|  6589.060| 181.213| 102,139|
| |Hoke County|     9| 162.943| N/A|   681| 12329.362| N/A|  55,234|
| |Surry County|     9| 125.378| N/A|   877| 12217.377| N/A|  71,783|
| |Richmond County|     8| 178.456| N/A|   486| 10841.197| N/A|  44,829|
| |Rockingham County|     7| 76.915| N/A|   494|  5427.975| N/A|  91,010|
| |Warren County|     7| 354.772| N/A|   246| 12467.690| N/A|  19,731|
| |Bladen County|     7| 213.923| N/A|   591| 18061.243| N/A|  32,722|
| |Haywood County|     7| 112.329| N/A|   356|  5712.727| N/A|  62,317|
| |Yadkin County|     6| 159.291| N/A|   508| 13486.606| N/A|  37,667|
| |Carteret County|     6| 86.364| N/A|   332|  4778.835| N/A|  69,473|
| |Davie County|     6| 140.036| N/A|   387|  9032.348| N/A|  42,846|
| |Martin County|     6| 267.380| N/A|   245| 10918.004| N/A|  22,440|
| |Halifax County|     6| 119.976| N/A|   650| 12997.401| N/A|  50,010|
| |Bertie County|     5| 263.894| N/A|   254| 13405.816| N/A|  18,947|
| |Polk County|     5| 241.266| N/A|   146|  7044.972| N/A|  20,724|
| |Washington County|     4| 345.423| N/A|   121| 10449.050| N/A|  11,580|
| |Pender County|     3| 47.574| N/A|   632| 10022.201| N/A|  63,060|
| |Stokes County|     3| 65.802| N/A|   270|  5922.221| N/A|  45,591|
| |Greene County|     3| 142.389| N/A|   313| 14855.949| N/A|  21,069|
| |Cherokee County|     3| 104.851| N/A|   265|  9261.848| N/A|  28,612|
| |Macon County|     3| 83.663| N/A|   460| 12828.379| N/A|  35,858|
| |Lincoln County|     3| 34.839| N/A|   773|  8976.786| N/A|  86,111|
| |Jones County|     3| 318.505| N/A|    78|  8281.134| N/A|   9,419|
| |Jackson County|     3| 68.278| N/A|   412|  9376.849| N/A|  43,938|
| |Gates County|     2| 172.980| N/A|    45|  3892.060| N/A|  11,562|
| |Mitchell County|     2| 133.654| N/A|   116|  7751.938| N/A|  14,964|
| |Swain County|     2| 140.144| N/A|   106|  7427.650| N/A|  14,271|
| |Scotland County|     2| 57.433| N/A|   302|  8672.429| N/A|  34,823|
| |Person County|     2| 50.646| N/A|   201|  5089.896| N/A|  39,490|
| |Perquimans County|     2| 148.555| N/A|    73|  5422.268| N/A|  13,463|
| |Dare County|     2| 54.041| N/A|   202|  5458.132| N/A|  37,009|
| |Anson County|     2| 81.813| N/A|   308| 12599.198| N/A|  24,446|
| |Alexander County|     2| 53.338| N/A|   295|  7867.296| N/A|  37,497|
| |Caswell County|     2| 88.480| N/A|   189|  8361.352| N/A|  22,604|
| |Beaufort County|     2| 42.559| N/A|   373|  7937.183| N/A|  46,994|
| |Camden County|     2| 184.043| N/A|    63|  5797.368| N/A|  10,867|
| |Ashe County|     1| 36.761| N/A|   126|  4631.842| N/A|  27,203|
| |Chowan County|     1| 71.721| N/A|   145| 10399.484| N/A|  13,943|
| |Tyrrell County|     1| 249.004| N/A|    92| 22908.367| N/A|   4,016|
| |Transylvania County|     1| 29.082| N/A|   132|  3838.883| N/A|  34,385|
| |Pamlico County|     1| 78.579| N/A|    65|  5107.654| N/A|  12,726|
| |Graham County|     0|  0.000| N/A|    29|  3435.612| N/A|   8,441|
| |Yancey County|     0|  0.000| N/A|   101|  5589.684| N/A|  18,069|
| |Watauga County|     0|  0.000| N/A|   283|  5037.649| N/A|  56,177|
| |Madison County|     0|  0.000| N/A|    41|  1884.624| N/A|  21,755|
| |Hyde County|     0|  0.000| N/A|    37|  7494.430| N/A|   4,937|
| |Currituck County|     0|  0.000| N/A|    71|  2557.361| N/A|  27,763|
| |Clay County|     0|  0.000| N/A|    76|  6766.984| N/A|  11,231|
| |Avery County|     0|  0.000| N/A|    99|  5638.777| N/A|  17,557|
| |Alleghany County|     0|  0.000| N/A|   165| 14815.480| N/A|  11,137|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,849| 321.077| N/A|48,376|  8400.455| N/A|5,758,736|
| |Denver County|   412| 566.548| N/A| 9,876| 13580.653| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  1.523| 7,093| 10802.784| 84.247| 656,590|
| |Jefferson County|   227| 389.445|  0.000| 3,994|  6852.171| 39.459| 582,881|
| |Adams County|   173| 334.351|  1.599| 6,181| 11945.785| 107.323| 517,421|
| |Weld County|   142| 437.607|  3.082| 3,580| 11032.629| 54.322| 324,492|
| |El Paso County|   137| 190.171|  0.800| 4,663|  6472.766| 55.568| 720,403|
| |Boulder County|    75| 229.923|  0.000| 1,946|  5965.738| 58.247| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,670|  4755.748| 38.166| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   678| 23324.618| 19.786|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,420|  3978.717| 33.702| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   617|  3663.373| 11.875| 168,424|
| |Broomfield County|    32| 454.126| N/A|   421|  5974.597| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   292| 14344.665| 111.758|  20,356|
| |Montrose County|    13| 304.037|  0.000|   287|  6712.194| 78.065|  42,758|
| |Alamosa County|     9| 554.426| N/A|   224| 13799.051| N/A|  16,233|
| |Eagle County|     9| 163.259| N/A| 1,092| 19808.805| N/A|  55,127|
| |Gunnison County|     6| 343.603| N/A|   262| 15004.009| N/A|  17,462|
| |Otero County|     6| 328.263| N/A|    63|  3446.767| N/A|  18,278|
| |Routt County|     6| 234.028| N/A|   110|  4290.506| N/A|  25,638|
| |Logan County|     5| 223.125| N/A|   649| 28961.578| N/A|  22,409|
| |Garfield County|     4| 66.599| N/A|   734| 12220.909| N/A|  60,061|
| |Montezuma County|     4| 152.771| N/A|   108|  4124.814| N/A|  26,183|
| |Summit County|     4| 128.986| N/A|   324| 10447.906| N/A|  31,011|
| |Teller County|     3| 118.166| N/A|   117|  4608.476| N/A|  25,388|
| |Mesa County|     3| 19.454| N/A|   274|  1776.798| N/A| 154,210|
| |Kit Carson County|     3| 422.714| N/A|    43|  6058.898| N/A|   7,097|
| |Pitkin County|     2| 112.568| N/A|   177|  9962.290| N/A|  17,767|
| |Saguache County|     2| 293.083| N/A|   107| 15679.953| N/A|   6,824|
| |Rio Grande County|     2| 177.510| N/A|    87|  7721.665| N/A|  11,267|
| |La Plata County|     2| 35.574| N/A|   201|  3575.177| N/A|  56,221|
| |Elbert County|     2| 74.825| N/A|    92|  3441.954| N/A|  26,729|
| |Clear Creek County|     1| 103.093| N/A|    28|  2886.598| N/A|   9,700|
| |Ouray County|     1| 201.939| N/A|    12|  2423.263| N/A|   4,952|
| |Sedgwick County|     1| 444.840| N/A|    11|  4893.238| N/A|   2,248|
| |Park County|     1| 53.064| N/A|    42|  2228.708| N/A|  18,845|
| |Crowley County|     1| 164.989| N/A|    72| 11879.228| N/A|   6,061|
| |Delta County|     1| 32.090| N/A|   115|  3690.392| N/A|  31,162|
| |Moffat County|     1| 75.284| N/A|    26|  1957.389| N/A|  13,283|
| |Huerfano County|     1| 144.991| N/A|     6|   869.943| N/A|   6,897|
| |Grand County|     1| 63.557| N/A|    44|  2796.492| N/A|  15,734|
| |Custer County|     0|  0.000| N/A|    11|  2170.481| N/A|   5,068|
| |Costilla County|     0|  0.000| N/A|    22|  5659.892| N/A|   3,887|
| |Conejos County|     0|  0.000| N/A|    23|  2803.169| N/A|   8,205|
| |Cheyenne County|     0|  0.000| N/A|     8|  4369.197| N/A|   1,831|
| |Bent County|     0|  0.000| N/A|     6|  1075.847| N/A|   5,577|
| |Baca County|     0|  0.000| N/A|    14|  3909.522| N/A|   3,581|
| |Archuleta County|     0|  0.000| N/A|    33|  2352.270| N/A|  14,029|
| |Fremont County|     0|  0.000| N/A|   113|  2362.090| N/A|  47,839|
| |Washington County|     0|  0.000| N/A|    47|  9576.202| N/A|   4,908|
| |Dolores County|     0|  0.000| N/A|     1|   486.618| N/A|   2,055|
| |Gilpin County|     0|  0.000| N/A|    16|  2562.870| N/A|   6,243|
| |San Juan County|     0|  0.000| N/A|     2|  2747.253| N/A|     728|
| |Yuma County|     0|  0.000| N/A|    62|  6188.242| N/A|  10,019|
| |San Miguel County|     0|  0.000| N/A|    80|  9781.147| N/A|   8,179|
| |Rio Blanco County|     0|  0.000| N/A|     8|  1265.022| N/A|   6,324|
| |Hinsdale County|     0|  0.000| N/A|     3|  3658.537| N/A|     820|
| |Prowers County|     0|  0.000| N/A|    50|  4107.788| N/A|  12,172|
| |Phillips County|     0|  0.000| N/A|    19|  4454.865| N/A|   4,265|
| |Mineral County|     0|  0.000| N/A|    18| 23407.022| N/A|     769|
| |Lincoln County|     0|  0.000| N/A|     6|  1052.447| N/A|   5,701|
| |Las Animas County|     0|  0.000| N/A|    15|  1034.055| N/A|  14,506|
| |Lake County|     0|  0.000| N/A|    73|  8982.404| N/A|   8,127|
| |Kiowa County|     0|  0.000| N/A|     0|     0.000| N/A|   1,406|
| |Jackson County|     0|  0.000| N/A|     8|  5747.126| N/A|   1,392|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 1,847| 358.730| N/A|94,190| 18293.889| N/A|5,148,714|
| |Greenville County|   196| 374.373|  6.672|10,442| 19944.914| 207.214| 523,542|
| |Charleston County|   178| 432.663|  7.292|11,814| 28716.159| 243.069| 411,406|
| |Richland County|   143| 343.949|  7.843| 8,173| 19658.023| 241.177| 415,759|
| |Horry County|   140| 395.390| 12.645| 8,235| 23257.390| 170.871| 354,081|
| |Lexington County|   105| 351.464|  4.333| 4,750| 15899.582| 174.572| 298,750|
| |Florence County|   100| 723.102|  8.358| 3,133| 22654.798| 417.557| 138,293|
| |Spartanburg County|    92| 287.693| 10.945| 3,838| 12001.814| 151.664| 319,785|
| |Berkeley County|    61| 267.653|  4.342| 3,965| 17397.447| 228.309| 227,907|
| |Orangeburg County|    60| 696.258| 14.506| 2,257| 26190.891| 398.108|  86,175|
| |Beaufort County|    50| 260.251|  1.995| 3,742| 19477.207| 286.085| 192,122|
| |Clarendon County|    50| 1481.701|  0.000|   793| 23499.778| 197.937|  33,745|
| |Anderson County|    48| 236.969|  2.796| 2,155| 10638.928| 221.767| 202,558|
| |Sumter County|    45| 421.660|  0.000| 2,367| 22179.327| 249.959| 106,721|
| |Dorchester County|    40| 245.687|  2.586| 2,855| 17535.886| 228.896| 162,809|
| |Laurens County|    37| 548.205| 18.489| 1,244| 18431.541| 118.531|  67,493|
| |Darlington County|    33| 495.362|  0.000| 1,151| 17277.613| 450.329|  66,618|
| |Colleton County|    31| 822.783|  0.000|   771| 20463.413| 134.717|  37,677|
| |Aiken County|    31| 181.422|  9.993| 1,638|  9586.123| 189.309| 170,872|
| |Williamsburg County|    29| 954.953| 27.395|   947| 31184.141| 499.079|  30,368|
| |York County|    28| 99.652|  0.000| 3,313| 11790.917| 254.467| 280,979|
| |Cherokee County|    28| 488.656| 21.778|   568|  9912.740| 165.794|  57,300|
| |Lee County|    27| 1604.469|  0.000|   532| 31613.977| 333.747|  16,828|
| |Kershaw County|    23| 345.600|  0.000| 1,311| 19699.178| 202.852|  66,551|
| |Pickens County|    23| 181.268|  0.000| 1,767| 13926.106| 165.506| 126,884|
| |Fairfield County|    23| 1029.221|  0.000|   540| 24164.317| 111.678|  22,347|
| |Dillon County|    23| 754.618|  0.000|   583| 19127.924| 327.076|  30,479|
| |Lancaster County|    22| 224.462| 10.203| 1,101| 11233.318| 202.299|  98,012|
| |Chesterfield County|    19| 416.210|  0.000|   712| 15596.933| 175.246|  45,650|
| |Georgetown County|    19| 303.127|  0.000| 1,319| 21043.395| 251.999|  62,680|
| |Bamberg County|    17| 1208.588| 30.368|   445| 31636.570| 199.968|  14,066|
| |Greenwood County|    16| 225.954| 14.122| 1,303| 18401.096| 317.747|  70,811|
| |Jasper County|    13| 432.281|  0.000|   537| 17856.549| 482.599|  30,073|
| |Chester County|    13| 403.176| 26.006|   583| 18080.883| 302.602|  32,244|
| |Marion County|    12| 391.428|  0.000|   527| 17190.201| 149.526|  30,657|
| |Calhoun County|    10| 687.144|  0.000|   339| 23294.166| 770.117|  14,553|
| |Newberry County|     9| 234.131| N/A|   802| 20863.684| N/A|  38,440|
| |Saluda County|     8| 390.759| N/A|   426| 20807.893| N/A|  20,473|
| |Abbeville County|     8| 326.171| N/A|   301| 12272.190| N/A|  24,527|
| |Oconee County|     7| 87.999| N/A|   761|  9566.792| N/A|  79,546|
| |Hampton County|     7| 364.166| N/A|   395| 20549.371| N/A|  19,222|
| |Edgefield County|     6| 220.103| N/A|   292| 10711.665| N/A|  27,260|
| |Barnwell County|     5| 239.624| N/A|   372| 17828.046| N/A|  20,866|
| |Marlboro County|     4| 153.151| N/A|   447| 17114.634| N/A|  26,118|
| |Union County|     3| 109.826| N/A|   342| 12520.135| N/A|  27,316|
| |Allendale County|     3| 345.304| N/A|   195| 22444.751| N/A|   8,688|
| |McCormick County|     2| 211.349| N/A|   107| 11307.196| N/A|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,753| 589.016| N/A|62,199| 20899.155| N/A|2,976,149|
| |Hinds County|   110| 474.465|  8.627| 5,329| 22985.680| 242.407| 231,840|
| |Neshoba County|    88| 3022.186| 14.670| 1,232| 42310.598| 137.372|  29,118|
| |Lauderdale County|    88| 1187.184|  0.000| 1,354| 18266.442| 178.373|  74,125|
| |Madison County|    60| 564.589| 25.172| 2,324| 21868.413| 183.811| 106,272|
| |Leflore County|    60| 2128.943|  0.000|   866| 30727.744| 539.782|  28,183|
| |Jones County|    57| 837.029|  0.000| 1,804| 26491.233| 298.279|  68,098|
| |Forrest County|    53| 707.638|  0.000| 1,653| 22070.310| 157.042|  74,897|
| |Monroe County|    50| 1418.359|  0.000|   716| 20310.904| 271.704|  35,252|
| |Holmes County|    48| 2821.869| 33.951|   851| 50029.394| 272.347|  17,010|
| |Lincoln County|    41| 1200.480| 29.280|   756| 22135.684| 195.983|  34,153|
| |Jackson County|    38| 264.593| 11.758| 2,063| 14364.595| 453.725| 143,617|
| |Pearl River County|    37| 666.247| 18.007|   496|  8931.305| 112.426|  55,535|
| |Oktibbeha County|    36| 725.997| 11.552| 1,060| 21376.570| 93.254|  49,587|
| |Harrison County|    33| 158.593|  2.009| 2,228| 10707.420| 285.321| 208,080|
| |Washington County|    33| 751.554|  9.434| 1,524| 34708.146| 502.275|  43,909|
| |Lowndes County|    32| 546.122|  5.354|   999| 17049.236| 227.859|  58,595|
| |Pike County|    32| 814.498|  0.000|   846| 21533.293| 241.245|  39,288|
| |Bolivar County|    32| 1044.796|  0.000|   987| 32225.415| 694.822|  30,628|
| |Warren County|    30| 661.070| 45.390|   976| 21506.798| 111.248|  45,381|
| |Lee County|    30| 351.140|  0.000| 1,274| 14911.747| 285.368|  85,436|
| |Rankin County|    30| 193.211|  5.337| 2,168| 13962.685| 129.304| 155,271|
| |Simpson County|    28| 1050.341| 31.628|   723| 27121.314| 211.388|  26,658|
| |DeSoto County|    27| 145.989|  0.000| 3,387| 18313.553| 329.828| 184,945|
| |Copiah County|    26| 926.421| 35.233|   924| 32923.570| 249.421|  28,065|
| |Adams County|    25| 814.518|  0.000|   587| 19124.882| 113.058|  30,693|
| |Leake County|    25| 1097.165|  0.000|   771| 33836.566| 108.755|  22,786|
| |Clarke County|    25| 1608.648|  0.000|   310| 19947.236| 335.981|  15,541|
| |Tate County|    24| 847.428| 20.368|   665| 23480.809| 353.095|  28,321|
| |Attala County|    24| 1320.568|  0.000|   502| 27621.877| 220.095|  18,174|
| |Sunflower County|    23| 915.970| 21.104|   926| 36877.738| 350.155|  25,110|
| |Grenada County|    21| 1011.658| 19.956|   816| 39310.145| 172.924|  20,758|
| |Wayne County|    21| 1040.480|  0.000|   736| 36466.333| 49.547|  20,183|
| |Chickasaw County|    19| 1110.916|  0.000|   443| 25901.889| 269.911|  17,103|
| |Marion County|    19| 773.206| 40.695|   625| 25434.420| 81.390|  24,573|
| |Scott County|    19| 675.580| 71.114|   962| 34205.661| 145.452|  28,124|
| |Walthall County|    18| 1259.975|  0.000|   463| 32409.352| 659.054|  14,286|
| |Kemper County|    15| 1539.725|  0.000|   227| 23301.170|  0.000|   9,742|
| |Winston County|    15| 835.422|  0.000|   584| 32525.759| 724.032|  17,955|
| |Hancock County|    14| 293.920|  0.000|   344|  7222.036| 41.989|  47,632|
| |Union County|    14| 485.858| 34.704|   538| 18670.831| 310.615|  28,815|
| |Lamar County|    13| 205.232|  0.000| 1,146| 18091.975| 232.822|  63,343|
| |Clay County|    13| 673.017|  0.000|   374| 19362.187| 207.082|  19,316|
| |Claiborne County|    13| 1446.373|  0.000|   401| 44615.042| 64.298|   8,988|
| |Smith County|    13| 816.788|  0.000|   385| 24189.495| 241.364|  15,916|
| |Wilkinson County|    13| 1506.373| 48.200|   188| 21784.473| 61.404|   8,630|
| |Tippah County|    12| 545.083|  0.000|   316| 14353.850| 181.694|  22,015|
| |Webster County|    12| 1238.518|  0.000|   201| 20745.175| 206.420|   9,689|
| |Lafayette County|    12| 222.144| 23.516|   885| 16383.124| 148.096|  54,019|
| |Covington County|    12| 643.915|  0.000|   601| 32249.410| 697.575|  18,636|
| |Greene County|    11| 809.657|  0.000|   232| 17076.402| 234.026|  13,586|
| |Yazoo County|    11| 370.495|  0.000|   793| 26709.330| 331.558|  29,690|
| |Carroll County|    11| 1105.861|  0.000|   248| 24932.140| 301.598|   9,947|
| |Humphreys County|    11| 1364.087|  0.000|   274| 33978.175| 341.811|   8,064|
| |Panola County|    11| 321.713|  0.000|   936| 27374.825| 424.076|  34,192|
| |Newton County|    11| 523.361|  0.000|   526| 25026.168| 212.324|  21,018|
| |Noxubee County|    11| 1055.966|  0.000|   426| 40894.691| 405.633|  10,417|
| |Tallahatchie County|    10| 724.165|  0.000|   496| 35918.604| 1117.417|  13,809|
| |Yalobusha County|    10| 825.900|  0.000|   313| 25850.677|  0.000|  12,108|
| |Itawamba County|    10| 427.533|  0.000|   317| 13552.800| 187.173|  23,390|
| |Coahoma County|    10| 451.998|  0.000|   677| 30600.253| 419.606|  22,124|
| |Jasper County|     9| 549.350| N/A|   385| 23499.969| N/A|  16,383|
| |Calhoun County|     9| 626.697| N/A|   381| 26530.186| N/A|  14,361|
| |Marshall County|     8| 226.667| N/A|   585| 16575.055| N/A|  35,294|
| |Pontotoc County|     7| 217.567| N/A|   752| 23372.910| N/A|  32,174|
| |Perry County|     7| 584.649| N/A|   226| 18875.804| N/A|  11,973|
| |Amite County|     6| 487.924| N/A|   211| 17158.657| N/A|  12,297|
| |Jefferson Davis County|     6| 539.180| N/A|   214| 19230.769| N/A|  11,128|
| |Prentiss County|     6| 238.796| N/A|   351| 13969.593| N/A|  25,126|
| |Jefferson County|     6| 858.369| N/A|   193| 27610.873| N/A|   6,990|
| |Tunica County|     6| 622.924| N/A|   292| 30315.615| N/A|   9,632|
| |George County|     5| 204.082| N/A|   549| 22408.163| N/A|  24,500|
| |Lawrence County|     5| 397.267| N/A|   315| 25027.809| N/A|  12,586|
| |Choctaw County|     4| 487.211| N/A|   129| 15712.546| N/A|   8,210|
| |Alcorn County|     4| 108.246| N/A|   363|  9823.289| N/A|  36,953|
| |Tishomingo County|     4| 206.366| N/A|   339| 17489.553| N/A|  19,383|
| |Stone County|     3| 163.613| N/A|   159|  8671.466| N/A|  18,336|
| |Montgomery County|     3| 306.905| N/A|   297| 30383.632| N/A|   9,775|
| |Franklin County|     2| 259.302| N/A|   117| 15169.195| N/A|   7,713|
| |Sharkey County|     1| 231.428| N/A|   183| 42351.308| N/A|   4,321|
| |Quitman County|     1| 147.232| N/A|   233| 34305.065| N/A|   6,792|
| |Issaquena County|     1| 753.580| N/A|    21| 15825.170| N/A|   1,327|
| |Benton County|     0|  0.000| N/A|   130| 15740.404| N/A|   8,259|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,620| 287.253| N/A|57,022| 10110.943| N/A|5,639,632|
| |Hennepin County|   820| 647.790|  1.256|18,197| 14375.400| 166.200|1,265,843|
| |Ramsey County|   261| 474.269|  0.909| 7,047| 12805.254| 170.301| 550,321|
| |Anoka County|   113| 316.597|  0.000| 3,410|  9553.935| 119.792| 356,921|
| |Dakota County|   103| 240.081|  0.000| 4,049|  9437.766| 136.288| 429,021|
| |Washington County|    43| 163.847|  0.000| 1,938|  7384.545| 104.201| 262,440|
| |Clay County|    40| 622.840|  0.000|   752| 11709.383| 60.831|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,635| 10328.947| 37.904| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,842| 17643.955| 75.320| 161,075|
| |St. Louis County|    19| 95.444|  0.788|   453|  2275.581| 90.420| 199,070|
| |Scott County|    17| 114.084| 20.132| 1,410|  9462.262| 161.060| 149,013|
| |Winona County|    16| 316.932|  0.000|   249|  4932.256| 39.617|  50,484|
| |Crow Wing County|    13| 199.831|  0.000|   213|  3274.153|  0.000|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   320|  9336.523| 116.707|  34,274|
| |Itasca County|    12| 265.899|  0.000|   134|  2969.200| 44.316|  45,130|
| |Pipestone County|     9| 986.193| N/A|   143| 15669.516| N/A|   9,126|
| |Rice County|     8| 119.453| N/A| 1,002| 14961.476| N/A|  66,972|
| |Goodhue County|     8| 172.637| N/A|   177|  3819.594| N/A|  46,340|
| |Sherburne County|     7| 71.988| N/A|   657|  6756.618| N/A|  97,238|
| |Nobles County|     6| 277.405| N/A| 1,749| 80863.655| N/A|  21,629|
| |Renville County|     5| 343.690| N/A|    60|  4124.278| N/A|  14,548|
| |Martin County|     5| 254.026| N/A|   204| 10364.274| N/A|  19,683|
| |Blue Earth County|     5| 73.907| N/A|   859| 12697.146| N/A|  67,653|
| |Wright County|     5| 36.133| N/A|   820|  5925.840| N/A| 138,377|
| |Koochiching County|     3| 245.319| N/A|    74|  6051.190| N/A|  12,229|
| |Lyon County|     3| 117.767| N/A|   416| 16330.376| N/A|  25,474|
| |Mille Lacs County|     3| 114.168| N/A|    68|  2587.814| N/A|  26,277|
| |Polk County|     3| 95.651| N/A|   135|  4304.298| N/A|  31,364|
| |Otter Tail County|     3| 51.067| N/A|   179|  3047.016| N/A|  58,746|
| |Benton County|     3| 73.369| N/A|   310|  7581.501| N/A|  40,889|
| |Wilkin County|     3| 483.325| N/A|    28|  4511.036| N/A|   6,207|
| |Mower County|     2| 49.923| N/A| 1,084| 27058.060| N/A|  40,062|
| |Meeker County|     2| 86.125| N/A|    83|  3574.197| N/A|  23,222|
| |Cass County|     2| 67.161| N/A|    62|  2082.004| N/A|  29,779|
| |Carver County|     2| 19.031| N/A|   792|  7536.469| N/A| 105,089|
| |Brown County|     2| 79.974| N/A|    85|  3398.912| N/A|  25,008|
| |Sibley County|     2| 134.544| N/A|    80|  5381.769| N/A|  14,865|
| |Todd County|     2| 81.090| N/A|   420| 17028.868| N/A|  24,664|
| |Kanabec County|     1| 61.211| N/A|    28|  1713.901| N/A|  16,337|
| |Kandiyohi County|     1| 23.149| N/A|   677| 15671.659| N/A|  43,199|
| |Freeborn County|     1| 33.024| N/A|   355| 11723.523| N/A|  30,281|
| |Morrison County|     1| 29.953| N/A|    82|  2456.119| N/A|  33,386|
| |Grant County|     1| 167.448| N/A|    51|  8539.853| N/A|   5,972|
| |Chisago County|     1| 17.674| N/A|   182|  3216.741| N/A|  56,579|
| |Swift County|     1| 107.921| N/A|    52|  5611.915| N/A|   9,266|
| |Pennington County|     1| 70.827| N/A|    73|  5170.338| N/A|  14,119|
| |Murray County|     1| 122.041| N/A|   122| 14888.943| N/A|   8,194|
| |Becker County|     1| 29.050| N/A|   147|  4270.401| N/A|  34,423|
| |Steele County|     1| 27.286| N/A|   333|  9086.196| N/A|  36,649|
| |Mahnomen County|     1| 180.930| N/A|    24|  4342.320| N/A|   5,527|
| |Le Sueur County|     1| 34.618| N/A|   202|  6992.765| N/A|  28,887|
| |Chippewa County|     1| 84.746| N/A|    99|  8389.831| N/A|  11,800|
| |Lake of the Woods County|     0|  0.000| N/A|     1|   267.380| N/A|   3,740|
| |McLeod County|     0|  0.000| N/A|   140|  3900.482| N/A|  35,893|
| |Norman County|     0|  0.000| N/A|    37|  5803.922| N/A|   6,375|
| |Pine County|     0|  0.000| N/A|   128|  4327.394| N/A|  29,579|
| |Marshall County|     0|  0.000| N/A|    29|  3106.255| N/A|   9,336|
| |Pope County|     0|  0.000| N/A|    45|  4000.356| N/A|  11,249|
| |Wabasha County|     0|  0.000| N/A|    82|  3791.557| N/A|  21,627|
| |Yellow Medicine County|     0|  0.000| N/A|    49|  5046.864| N/A|   9,709|
| |Watonwan County|     0|  0.000| N/A|   299| 27438.745| N/A|  10,897|
| |Waseca County|     0|  0.000| N/A|   130|  6984.741| N/A|  18,612|
| |Wadena County|     0|  0.000| N/A|    23|  1681.041| N/A|  13,682|
| |Traverse County|     0|  0.000| N/A|    10|  3068.426| N/A|   3,259|
| |Stevens County|     0|  0.000| N/A|    16|  1631.820| N/A|   9,805|
| |Roseau County|     0|  0.000| N/A|    46|  3033.300| N/A|  15,165|
| |Rock County|     0|  0.000| N/A|    75|  8051.530| N/A|   9,315|
| |Redwood County|     0|  0.000| N/A|    32|  2109.426| N/A|  15,170|
| |Red Lake County|     0|  0.000| N/A|    20|  4932.182| N/A|   4,055|
| |Lincoln County|     0|  0.000| N/A|    54|  9576.166| N/A|   5,639|
| |Faribault County|     0|  0.000| N/A|    84|  6152.494| N/A|  13,653|
| |Lake County|     0|  0.000| N/A|    18|  1691.570| N/A|  10,641|
| |Lac qui Parle County|     0|  0.000| N/A|     6|   905.934| N/A|   6,623|
| |Kittson County|     0|  0.000| N/A|     3|   697.999| N/A|   4,298|
| |Jackson County|     0|  0.000| N/A|    70|  7109.486| N/A|   9,846|
| |Isanti County|     0|  0.000| N/A|   110|  2709.627| N/A|  40,596|
| |Hubbard County|     0|  0.000| N/A|    32|  1488.995| N/A|  21,491|
| |Houston County|     0|  0.000| N/A|    39|  2096.774| N/A|  18,600|
| |Fillmore County|     0|  0.000| N/A|    61|  2895.524| N/A|  21,067|
| |Douglas County|     0|  0.000| N/A|   132|  3460.843| N/A|  38,141|
| |Dodge County|     0|  0.000| N/A|   123|  5875.609| N/A|  20,934|
| |Cottonwood County|     0|  0.000| N/A|   173| 15451.947| N/A|  11,196|
| |Cook County|     0|  0.000| N/A|     2|   366.099| N/A|   5,463|
| |Clearwater County|     0|  0.000| N/A|    15|  1701.066| N/A|   8,818|
| |Carlton County|     0|  0.000| N/A|   126|  3512.587| N/A|  35,871|
| |Big Stone County|     0|  0.000| N/A|    22|  4407.934| N/A|   4,991|
| |Beltrami County|     0|  0.000| N/A|   200|  4238.366| N/A|  47,188|
| |Aitkin County|     0|  0.000| N/A|    27|  1699.610| N/A|  15,886|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,616| 212.216| N/A|59,212|  7775.815| N/A|7,614,893|
| |King County|   659| 292.527|  0.539|15,726|  6980.702| 49.771|2,252,782|
| |Yakima County|   210| 837.077| 10.096|10,081| 40183.679| 144.573| 250,873|
| |Snohomish County|   191| 232.337|  1.046| 5,219|  6348.507| 68.120| 822,083|
| |Pierce County|   129| 142.545|  0.939| 5,280|  5834.383| 82.347| 904,980|
| |Benton County|   111| 543.079|  2.815| 3,569| 17461.715| 152.731| 204,390|
| |Spokane County|    67| 128.157|  5.591| 4,005|  7660.703| 109.029| 522,798|
| |Franklin County|    47| 493.583|  0.000| 3,374| 35432.988| 333.950|  95,222|
| |Clark County|    42| 86.023|  0.000| 1,667|  3414.297| 198.672| 488,241|
| |Whatcom County|    38| 165.760|  0.000|   941|  4104.743| 43.424| 229,247|
| |Skagit County|    21| 162.532|  0.000|   836|  6470.338| 80.701| 129,205|
| |Kittitas County|    18| 375.509| 20.862|   353|  7364.139| 104.308|  47,935|
| |Grant County|    12| 122.784|  0.000| 1,321| 13516.417| 303.451|  97,733|
| |Island County|    11| 129.197|  0.000|   241|  2830.599| 13.827|  85,141|
| |Thurston County|    10| 34.419|  6.884|   649|  2233.802| 16.840| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,190| 15414.508| 368.137|  77,200|
| |Douglas County|     7| 161.183| N/A|   840| 19341.914| N/A|  43,429|
| |Cowlitz County|     5| 45.211| N/A|   453|  4096.100| N/A| 110,593|
| |Kitsap County|     4| 14.734| N/A|   674|  2482.752| N/A| 271,473|
| |Adams County|     4| 200.170| N/A|   407| 20367.312| N/A|  19,983|
| |Walla Walla County|     3| 49.375| N/A|   460|  7570.770| N/A|  60,760|
| |Klickitat County|     3| 133.779| N/A|   106|  4726.867| N/A|  22,425|
| |Lewis County|     3| 37.171| N/A|   190|  2354.195| N/A|  80,707|
| |Asotin County|     2| 88.566| N/A|    24|  1062.793| N/A|  22,582|
| |Okanogan County|     2| 47.345| N/A|   783| 18535.615| N/A|  42,243|
| |Pacific County|     2| 89.004| N/A|    41|  1824.574| N/A|  22,471|
| |Grays Harbor County|     1| 13.322| N/A|   101|  1345.572| N/A|  75,061|
| |Skamania County|     1| 82.761| N/A|    54|  4469.089| N/A|  12,083|
| |Stevens County|     1| 21.871| N/A|    94|  2055.858| N/A|  45,723|
| |Mason County|     1| 14.977| N/A|   175|  2621.016| N/A|  66,768|
| |Columbia County|     1| 250.941| N/A|    13|  3262.233| N/A|   3,985|
| |Clallam County|     0|  0.000| N/A|    96|  1241.417| N/A|  77,331|
| |Ferry County|     0|  0.000| N/A|    20|  2622.263| N/A|   7,627|
| |Garfield County|     0|  0.000| N/A|     2|   898.876| N/A|   2,225|
| |Whitman County|     0|  0.000| N/A|    87|  1736.388| N/A|  50,104|
| |Lincoln County|     0|  0.000| N/A|    15|  1371.241| N/A|  10,939|
| |San Juan County|     0|  0.000| N/A|    29|  1649.414| N/A|  17,582|
| |Pend Oreille County|     0|  0.000| N/A|    37|  2696.007| N/A|  13,724|
| |Jefferson County|     0|  0.000| N/A|    54|  1675.926| N/A|  32,221|
| |Wahkiakum County|     0|  0.000| N/A|     5|  1114.082| N/A|   4,488|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,611| 328.562| N/A|90,890| 18536.931| N/A|4,903,185|
| |Jefferson County|   228| 346.203|  1.982|12,039| 18280.434| 295.336| 658,573|
| |Mobile County|   197| 476.755|  7.260| 9,170| 22192.106| 750.224| 413,210|
| |Montgomery County|   147| 649.047|  8.831| 6,305| 27838.365| 247.256| 226,486|
| |Tallapoosa County|    78| 1932.271|  0.000|   822| 20363.168| 197.797|  40,367|
| |Tuscaloosa County|    66| 315.254| 14.330| 3,984| 19029.877| 47.766| 209,355|
| |Walker County|    64| 1007.541| 15.743| 1,474| 23204.924| 130.867|  63,521|
| |Lee County|    40| 243.099|  0.000| 2,519| 15309.161| 218.789| 164,542|
| |Chambers County|    38| 1142.720|  0.000|   828| 24899.260| 210.501|  33,254|
| |Elmore County|    37| 455.615|  0.000| 1,626| 20022.411| 260.110|  81,209|
| |Butler County|    35| 1799.671|  0.000|   751| 38615.796|  0.000|  19,448|
| |Marshall County|    33| 341.001| 12.895| 2,984| 30834.728| 287.916|  96,774|
| |Shelby County|    32| 146.990|  0.000| 3,075| 14124.813| 176.784| 217,702|
| |Etowah County|    28| 273.790| 19.556| 1,957| 19135.996| 240.875| 102,268|
| |Madison County|    27| 72.404|  2.842| 5,082| 13627.990| 218.905| 372,909|
| |Hale County|    26| 1774.623|  0.000|   457| 31192.410| 241.138|  14,651|
| |Lowndes County|    24| 2467.613|  0.000|   558| 57371.993| 530.359|   9,726|
| |Marion County|    24| 807.836|  0.000|   547| 18411.929| 207.211|  29,709|
| |Dallas County|    23| 618.346|  0.000| 1,294| 34788.687| 221.867|  37,196|
| |Baldwin County|    23| 103.031|  2.607| 3,263| 14616.949| 237.419| 223,234|
| |Dale County|    22| 447.409| 29.507|   787| 16005.044| 137.645|  49,172|
| |Autauga County|    20| 357.980|  0.000| 1,030| 18435.984| 214.388|  55,869|
| |Covington County|    20| 539.826|  0.000|   715| 19298.766| 208.847|  37,049|
| |Franklin County|    20| 637.714|  0.000| 1,206| 38454.180| 348.835|  31,362|
| |Sumter County|    18| 1448.459|  0.000|   359| 28888.710|  0.000|  12,427|
| |Morgan County|    15| 125.335|  1.302| 2,243| 18741.801| 199.890| 119,679|
| |Escambia County|    15| 409.467|  0.000|   979| 26724.538| 219.375|  36,633|
| |Marengo County|    14| 742.194|  0.000|   526| 27885.278| 317.966|  18,863|
| |DeKalb County|    13| 181.785|  4.387| 1,718| 24023.604| 301.482|  71,513|
| |Talladega County|    13| 162.545|  0.000|   927| 11590.687| 250.240|  79,978|
| |Macon County|    13| 719.504|  8.682|   311| 17212.752| 106.177|  18,068|
| |Limestone County|    13| 131.426|  1.632| 1,208| 12212.506| 149.067|  98,915|
| |Lauderdale County|    12| 129.409|  0.000| 1,095| 11808.604| 232.830|  92,729|
| |Houston County|    12| 113.334|  0.000| 1,327| 12532.820| 122.145| 105,882|
| |Choctaw County|    12| 953.213|  0.000|   276| 21923.902| 124.925|  12,589|
| |Colbert County|    12| 217.230|  0.000| 1,107| 20039.463| 314.227|  55,241|
| |Calhoun County|    12| 105.629| 26.407| 1,590| 13995.863| 429.133| 113,605|
| |St. Clair County|    12| 134.060|  1.765| 1,236| 13808.204| 245.035|  89,512|
| |Washington County|    12| 735.024| 32.458|   314| 19233.125| 166.103|  16,326|
| |Greene County|    11| 1356.183|  0.000|   245| 30205.893| 278.523|   8,111|
| |Bullock County|    11| 1089.001|  0.000|   441| 43659.044| 198.000|  10,101|
| |Winston County|    11| 465.530|  6.639|   432| 18282.619| 84.642|  23,629|
| |Cullman County|    11| 131.315|  0.000| 1,157| 13811.957| 265.197|  83,768|
| |Conecuh County|    10| 828.706|  0.000|   372| 30827.878| 144.964|  12,067|
| |Randolph County|    10| 440.102|  0.000|   391| 17207.992| 68.794|  22,722|
| |Pickens County|     9| 451.581| N/A|   371| 18615.153| N/A|  19,930|
| |Wilcox County|     9| 867.637| N/A|   408| 39332.883| N/A|  10,373|
| |Clarke County|     9| 381.001| N/A|   487| 20616.375| N/A|  23,622|
| |Cherokee County|     7| 267.216| N/A|   247|  9428.920| N/A|  26,196|
| |Pike County|     7| 211.391| N/A|   660| 19931.147| N/A|  33,114|
| |Chilton County|     6| 135.050| N/A|   722| 16251.013| N/A|  44,428|
| |Coffee County|     5| 95.526| N/A|   716| 13679.263| N/A|  52,342|
| |Fayette County|     5| 306.711| N/A|   176| 10796.221| N/A|  16,302|
| |Clay County|     5| 377.786| N/A|   223| 16849.263| N/A|  13,235|
| |Barbour County|     5| 202.544| N/A|   563| 22806.449| N/A|  24,686|
| |Jackson County|     4| 77.480| N/A|   870| 16851.974| N/A|  51,626|
| |Perry County|     4| 448.280| N/A|   431| 48302.141| N/A|   8,923|
| |Monroe County|     4| 192.929| N/A|   395| 19051.753| N/A|  20,733|
| |Bibb County|     3| 133.964| N/A|   381| 17013.486| N/A|  22,394|
| |Blount County|     3| 51.880| N/A|   741| 12814.305| N/A|  57,826|
| |Henry County|     3| 174.368| N/A|   246| 14298.169| N/A|  17,205|
| |Crenshaw County|     3| 217.833| N/A|   297| 21565.495| N/A|  13,772|
| |Lamar County|     2| 144.875| N/A|   203| 14704.817| N/A|  13,805|
| |Coosa County|     2| 187.564| N/A|    92|  8627.966| N/A|  10,663|
| |Russell County|     1| 17.253| N/A| 1,247| 21514.467| N/A|  57,961|
| |Cleburne County|     1| 67.069| N/A|   121|  8115.359| N/A|  14,910|
| |Lawrence County|     0|  0.000| N/A|   324|  9840.846| N/A|  32,924|
| |Geneva County|     0|  0.000| N/A|   242|  9211.678| N/A|  26,271|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,235| 201.224| N/A|48,285|  7867.302| N/A|6,137,428|
| |St. Louis County|   822| 826.791|  1.006|18,528| 18635.996| 319.854| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,749|  9325.360| 222.187| 402,022|
| |Jackson County|    59| 83.925|  0.000| 3,639|  5176.306| 124.952| 703,011|
| |Jasper County|    27| 222.537|  6.888| 1,675| 13805.552| 94.784| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,428|  6344.383| 161.734| 225,081|
| |Clay County|    20| 80.017|  0.000|   944|  3776.786| 76.274| 249,948|
| |Franklin County|    18| 173.132|  0.000|   554|  5328.614| 121.058| 103,967|
| |Scott County|    13| 339.603|  0.000|   356|  9299.896| 104.493|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,301|  4438.970| 123.976| 293,086|
| |Platte County|    10| 95.769|  0.000|   328|  3141.221| 70.426| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,063| 12167.483| 40.062|  87,364|
| |Gentry County|     9| 1369.655| N/A|    82| 12479.075| N/A|   6,571|
| |Cass County|     9| 85.082| N/A|   673|  6362.261| N/A| 105,780|
| |Stoddard County|     9| 310.078| N/A|   212|  7304.048| N/A|  29,025|
| |Pemiscot County|     8| 506.169| N/A|   220| 13919.646| N/A|  15,805|
| |Saline County|     7| 307.544| N/A|   416| 18276.877| N/A|  22,761|
| |McDonald County|     7| 306.520| N/A|   940| 41161.273| N/A|  22,837|
| |Newton County|     6| 103.029| N/A|   828| 14218.009| N/A|  58,236|
| |Camden County|     5| 107.980| N/A|   317|  6845.913| N/A|  46,305|
| |Perry County|     4| 209.030| N/A|   211| 11026.338| N/A|  19,136|
| |Cape Girardeau County|     4| 50.716| N/A|   613|  7772.185| N/A|  78,871|
| |Dunklin County|     4| 137.311| N/A|   267|  9165.494| N/A|  29,131|
| |Boone County|     3| 16.624| N/A| 1,259|  6976.499| N/A| 180,463|
| |Cole County|     3| 39.090| N/A|   338|  4404.196| N/A|  76,745|
| |Taney County|     3| 53.640| N/A|   480|  8582.463| N/A|  55,928|
| |Henry County|     3| 137.463| N/A|    73|  3344.941| N/A|  21,824|
| |Pettis County|     3| 70.857| N/A|   450| 10628.499| N/A|  42,339|
| |St. Francois County|     2| 29.755| N/A|   320|  4760.842| N/A|  67,215|
| |Moniteau County|     2| 123.977| N/A|   130|  8058.517| N/A|  16,132|
| |Lawrence County|     2| 52.144| N/A|   195|  5084.083| N/A|  38,355|
| |Lafayette County|     2| 61.147| N/A|   164|  5014.064| N/A|  32,708|
| |Johnson County|     2| 36.995| N/A|   473|  8749.214| N/A|  54,062|
| |Howell County|     2| 49.854| N/A|   142|  3539.647| N/A|  40,117|
| |Douglas County|     2| 151.688| N/A|    83|  6295.032| N/A|  13,185|
| |Butler County|     2| 47.083| N/A|   249|  5861.858| N/A|  42,478|
| |Barry County|     2| 55.883| N/A|   233|  6510.380| N/A|  35,789|
| |Harrison County|     1| 119.732| N/A|    60|  7183.908| N/A|   8,352|
| |Grundy County|     1| 101.523| N/A|    25|  2538.071| N/A|   9,850|
| |Dallas County|     1| 59.249| N/A|    52|  3080.934| N/A|  16,878|
| |Christian County|     1| 11.287| N/A|   300|  3386.196| N/A|  88,595|
| |Carter County|     1| 167.168| N/A|    21|  3510.532| N/A|   5,982|
| |Callaway County|     1| 22.350| N/A|   131|  2927.832| N/A|  44,743|
| |Caldwell County|     1| 110.865| N/A|    34|  3769.401| N/A|   9,020|
| |Benton County|     1| 51.432| N/A|    75|  3857.429| N/A|  19,443|
| |Audrain County|     1| 39.389| N/A|   194|  7641.405| N/A|  25,388|
| |Bates County|     1| 61.835| N/A|    40|  2473.411| N/A|  16,172|
| |Andrew County|     1| 56.459| N/A|    85|  4799.006| N/A|  17,712|
| |Pulaski County|     1| 19.009| N/A|   187|  3554.660| N/A|  52,607|
| |Pike County|     1| 54.639| N/A|    78|  4261.829| N/A|  18,302|
| |Osage County|     1| 73.448| N/A|    45|  3305.178| N/A|  13,615|
| |New Madrid County|     1| 58.562| N/A|   200| 11712.345| N/A|  17,076|
| |Marion County|     1| 35.051| N/A|   160|  5608.132| N/A|  28,530|
| |Linn County|     1| 83.893| N/A|    30|  2516.779| N/A|  11,920|
| |Putnam County|     1| 212.947| N/A|    12|  2555.366| N/A|   4,696|
| |Lincoln County|     1| 16.945| N/A|   331|  5608.934| N/A|  59,013|
| |Lewis County|     1| 102.291| N/A|    34|  3477.905| N/A|   9,776|
| |Randolph County|     1| 40.407| N/A|    57|  2303.216| N/A|  24,748|
| |Laclede County|     1| 27.993| N/A|   199|  5570.641| N/A|  35,723|
| |Webster County|     1| 25.258| N/A|   123|  3106.688| N/A|  39,592|
| |Ripley County|     1| 75.256| N/A|    46|  3461.770| N/A|  13,288|
| |Washington County|     1| 40.437| N/A|    60|  2426.203| N/A|  24,730|
| |Stone County|     1| 31.297| N/A|    95|  2973.210| N/A|  31,952|
| |Shannon County|     1| 122.459| N/A|    43|  5265.736| N/A|   8,166|
| |Scotland County|     1| 203.998| N/A|    12|  2447.980| N/A|   4,902|
| |Ste. Genevieve County|     1| 55.885| N/A|    48|  2682.463| N/A|  17,894|
| |DeKalb County|     1| 79.700| N/A|    35|  2789.511| N/A|  12,547|
| |Mississippi County|     0|  0.000| N/A|   131|  9939.302| N/A|  13,180|
| |Hickory County|     0|  0.000| N/A|    17|  1781.224| N/A|   9,544|
| |Carroll County|     0|  0.000| N/A|    99| 11406.844| N/A|   8,679|
| |Cedar County|     0|  0.000| N/A|    35|  2439.194| N/A|  14,349|
| |Chariton County|     0|  0.000| N/A|    17|  2289.254| N/A|   7,426|
| |Maries County|     0|  0.000| N/A|    17|  1954.697| N/A|   8,697|
| |Madison County|     0|  0.000| N/A|    17|  1406.353| N/A|  12,088|
| |Macon County|     0|  0.000| N/A|    54|  3572.137| N/A|  15,117|
| |Livingston County|     0|  0.000| N/A|    53|  3480.659| N/A|  15,227|
| |Knox County|     0|  0.000| N/A|    19|  4799.192| N/A|   3,959|
| |Iron County|     0|  0.000| N/A|    20|  1975.309| N/A|  10,125|
| |Howard County|     0|  0.000| N/A|    47|  4699.530| N/A|  10,001|
| |Holt County|     0|  0.000| N/A|     6|  1362.707| N/A|   4,403|
| |Gasconade County|     0|  0.000| N/A|    21|  1427.989| N/A|  14,706|
| |Dent County|     0|  0.000| N/A|     9|   577.923| N/A|  15,573|
| |Daviess County|     0|  0.000| N/A|    17|  2053.636| N/A|   8,278|
| |Dade County|     0|  0.000| N/A|    21|  2777.410| N/A|   7,561|
| |Crawford County|     0|  0.000| N/A|    58|  2424.749| N/A|  23,920|
| |Cooper County|     0|  0.000| N/A|   103|  5816.252| N/A|  17,709|
| |Clinton County|     0|  0.000| N/A|    65|  3188.306| N/A|  20,387|
| |Clark County|     0|  0.000| N/A|    14|  2059.732| N/A|   6,797|
| |Bollinger County|     0|  0.000| N/A|    58|  4780.351| N/A|  12,133|
| |St. Clair County|     0|  0.000| N/A|    19|  2021.922| N/A|   9,397|
| |Worth County|     0|  0.000| N/A|     9|  4470.939| N/A|   2,013|
| |Wayne County|     0|  0.000| N/A|    44|  3418.007| N/A|  12,873|
| |Vernon County|     0|  0.000| N/A|    47|  2285.659| N/A|  20,563|
| |Warren County|     0|  0.000| N/A|   180|  5049.230| N/A|  35,649|
| |Texas County|     0|  0.000| N/A|    43|  1693.047| N/A|  25,398|
| |Adair County|     0|  0.000| N/A|   137|  5405.832| N/A|  25,343|
| |Monroe County|     0|  0.000| N/A|    22|  2545.118| N/A|   8,644|
| |Miller County|     0|  0.000| N/A|   107|  4176.588| N/A|  25,619|
| |Barton County|     0|  0.000| N/A|    66|  5615.110| N/A|  11,754|
| |Atchison County|     0|  0.000| N/A|    12|  2333.269| N/A|   5,143|
| |Mercer County|     0|  0.000| N/A|    10|  2764.722| N/A|   3,617|
| |Sullivan County|     0|  0.000| N/A|   137| 22499.589| N/A|   6,089|
| |Montgomery County|     0|  0.000| N/A|    40|  3462.904| N/A|  11,551|
| |Shelby County|     0|  0.000| N/A|    30|  5059.022| N/A|   5,930|
| |Schuyler County|     0|  0.000| N/A|     9|  1931.330| N/A|   4,660|
| |Reynolds County|     0|  0.000| N/A|    16|  2551.834| N/A|   6,270|
| |St. Louis city|     0|  0.000| N/A|     0|     0.000| N/A| 300,576|
| |Ralls County|     0|  0.000| N/A|    25|  2425.065| N/A|  10,309|
| |Polk County|     0|  0.000| N/A|   194|  6034.402| N/A|  32,149|
| |Phelps County|     0|  0.000| N/A|    76|  1705.068| N/A|  44,573|
| |Ozark County|     0|  0.000| N/A|     8|   872.030| N/A|   9,174|
| |Oregon County|     0|  0.000| N/A|    14|  1329.661| N/A|  10,529|
| |Nodaway County|     0|  0.000| N/A|   165|  7468.767| N/A|  22,092|
| |Morgan County|     0|  0.000| N/A|    71|  3442.090| N/A|  20,627|
| |Wright County|     0|  0.000| N/A|    58|  3171.305| N/A|  18,289|
| |Ray County|     0|  0.000| N/A|   103|  4474.759| N/A|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,098| 160.781| N/A|106,695| 15623.412| N/A|6,829,174|
| |Shelby County|   293| 312.645|  3.856|21,728| 23184.793| 231.646| 937,166|
| |Davidson County|   205| 295.328|  3.746|19,563| 28182.913| 179.665| 694,144|
| |Sumner County|    70| 365.950|  2.233| 3,219| 16828.469| 148.847| 191,283|
| |Rutherford County|    53| 159.502|  2.498| 6,155| 18523.256| 163.239| 332,285|
| |Hamilton County|    47| 127.785|  0.000| 5,720| 15551.761| 144.585| 367,804|
| |Knox County|    37| 78.671|  3.654| 4,108|  8734.609| 192.350| 470,313|
| |Williamson County|    22| 92.277|  0.000| 3,308| 13875.141| 163.582| 238,412|
| |Wilson County|    22| 152.084|  6.913| 2,102| 14530.925| 135.441| 144,657|
| |McMinn County|    20| 371.789|  0.000|   493|  9164.591| 130.126|  53,794|
| |Robertson County|    19| 264.576| 27.850| 1,459| 20316.656| 208.876|  71,813|
| |Hamblen County|    13| 200.203|  0.000| 1,297| 19974.128| 544.323|  64,934|
| |Macon County|    13| 528.412|  0.000|   841| 34184.213| 137.534|  24,602|
| |Madison County|    13| 132.675|  0.000|   929|  9481.140| 214.133|  97,984|
| |Putnam County|    13| 162.004|  0.000| 1,601| 19951.399| 292.707|  80,245|
| |Montgomery County|    12| 57.418|  2.536| 1,752|  8383.056| 108.873| 208,993|
| |Bedford County|    11| 221.270| 10.659|   877| 17641.261| 150.866|  49,713|
| |Hardeman County|    11| 439.122|  0.000|   830| 33133.733| 652.048|  25,050|
| |Giles County|    10| 339.397| 14.199|   354| 12014.662| 197.099|  29,464|
| |Bradley County|    10| 92.498|  0.000| 1,739| 16085.469| 167.050| 108,110|
| |Sullivan County|     9| 56.837| N/A|   833|  5260.565| N/A| 158,348|
| |Tipton County|     9| 146.106| N/A| 1,123| 18230.815| N/A|  61,599|
| |Monroe County|     9| 193.361| N/A|   377|  8099.688| N/A|  46,545|
| |Fayette County|     8| 194.491| N/A|   642| 15607.906| N/A|  41,133|
| |Hardin County|     7| 272.883| N/A|   409| 15944.176| N/A|  25,652|
| |Anderson County|     7| 90.935| N/A|   630|  8184.157| N/A|  76,978|
| |Dyer County|     7| 188.380| N/A|   568| 15285.664| N/A|  37,159|
| |Maury County|     7| 72.624| N/A| 1,089| 11298.204| N/A|  96,387|
| |Blount County|     7| 52.597| N/A| 1,181|  8873.828| N/A| 133,088|
| |Trousdale County|     6| 531.726| N/A| 1,576| 139666.785| N/A|  11,284|
| |Lawrence County|     6| 135.925| N/A|   491| 11123.193| N/A|  44,142|
| |Cumberland County|     6| 99.141| N/A|   385|  6361.533| N/A|  60,520|
| |Lauderdale County|     6| 234.073| N/A|   438| 17087.348| N/A|  25,633|
| |Cheatham County|     6| 147.540| N/A|   548| 13475.299| N/A|  40,667|
| |Sevier County|     5| 50.891| N/A| 1,756| 17872.774| N/A|  98,250|
| |Carter County|     5| 88.667| N/A|   433|  7678.530| N/A|  56,391|
| |Greene County|     5| 72.391| N/A|   376|  5443.832| N/A|  69,069|
| |McNairy County|     5| 194.598| N/A|   324| 12609.948| N/A|  25,694|
| |Haywood County|     5| 288.951| N/A|   402| 23231.623| N/A|  17,304|
| |Marion County|     4| 138.375| N/A|   209|  7230.083| N/A|  28,907|
| |Obion County|     4| 133.027| N/A|   453| 15065.350| N/A|  30,069|
| |Crockett County|     4| 281.096| N/A|   236| 16584.680| N/A|  14,230|
| |Hawkins County|     4| 70.440| N/A|   369|  6498.081| N/A|  56,786|
| |Warren County|     4| 96.906| N/A|   429| 10393.197| N/A|  41,277|
| |Franklin County|     4| 94.769| N/A|   286|  6775.967| N/A|  42,208|
| |Carroll County|     3| 108.042| N/A|   244|  8787.410| N/A|  27,767|
| |White County|     3| 109.709| N/A|   205|  7496.800| N/A|  27,345|
| |Weakley County|     3| 90.014| N/A|   310|  9301.488| N/A|  33,328|
| |Smith County|     3| 148.832| N/A|   384| 19050.454| N/A|  20,157|
| |Polk County|     3| 178.232| N/A|   179| 10634.506| N/A|  16,832|
| |Loudon County|     3| 55.486| N/A|   682| 12613.746| N/A|  54,068|
| |Jefferson County|     3| 55.051| N/A|   508|  9321.956| N/A|  54,495|
| |Humphreys County|     3| 161.447| N/A|   109|  5865.892| N/A|  18,582|
| |Decatur County|     2| 171.482| N/A|   169| 14490.268| N/A|  11,663|
| |Gibson County|     2| 40.706| N/A|   590| 12008.223| N/A|  49,133|
| |Grundy County|     2| 148.954| N/A|   102|  7596.634| N/A|  13,427|
| |Chester County|     2| 115.627| N/A|   196| 11331.445| N/A|  17,297|
| |Coffee County|     2| 35.386| N/A|   421|  7448.691| N/A|  56,520|
| |Washington County|     2| 15.459| N/A| 1,089|  8417.391| N/A| 129,375|
| |Marshall County|     2| 58.182| N/A|   266|  7738.182| N/A|  34,375|
| |Roane County|     2| 37.466| N/A|   392|  7343.299| N/A|  53,382|
| |Wayne County|     1| 59.977| N/A|   219| 13135.009| N/A|  16,673|
| |Cocke County|     1| 27.775| N/A|   412| 11443.173| N/A|  36,004|
| |DeKalb County|     1| 48.804| N/A|   322| 15714.983| N/A|  20,490|
| |Campbell County|     1| 25.099| N/A|   221|  5546.910| N/A|  39,842|
| |Hancock County|     1| 151.057| N/A|    76| 11480.363| N/A|   6,620|
| |Bledsoe County|     1| 66.383| N/A|   674| 44742.432| N/A|  15,064|
| |Dickson County|     1| 18.536| N/A|   609| 11288.648| N/A|  53,948|
| |Jackson County|     1| 84.846| N/A|   108|  9163.414| N/A|  11,786|
| |Benton County|     1| 61.881| N/A|   108|  6683.168| N/A|  16,160|
| |Lewis County|     1| 81.513| N/A|    58|  4727.747| N/A|  12,268|
| |Lincoln County|     1| 29.099| N/A|   255|  7420.125| N/A|  34,366|
| |Morgan County|     1| 46.722| N/A|    91|  4251.740| N/A|  21,403|
| |Pickett County|     1| 198.098| N/A|    25|  4952.456| N/A|   5,048|
| |Overton County|     1| 44.962| N/A|   139|  6249.719| N/A|  22,241|
| |Rhea County|     1| 30.150| N/A|   511| 15406.880| N/A|  33,167|
| |Cannon County|     0|  0.000| N/A|   126|  8584.276| N/A|  14,678|
| |Claiborne County|     0|  0.000| N/A|   235|  7353.171| N/A|  31,959|
| |Scott County|     0|  0.000| N/A|   105|  4758.021| N/A|  22,068|
| |Perry County|     0|  0.000| N/A|    74|  9162.952| N/A|   8,076|
| |Unicoi County|     0|  0.000| N/A|   139|  7772.745| N/A|  17,883|
| |Van Buren County|     0|  0.000| N/A|    33|  5619.891| N/A|   5,872|
| |Union County|     0|  0.000| N/A|   129|  6459.043| N/A|  19,972|
| |Sequatchie County|     0|  0.000| N/A|    96|  6388.926| N/A|  15,026|
| |Clay County|     0|  0.000| N/A|    64|  8404.465| N/A|   7,615|
| |Grainger County|     0|  0.000| N/A|   179|  7675.815| N/A|  23,320|
| |Fentress County|     0|  0.000| N/A|    76|  4103.007| N/A|  18,523|
| |Lake County|     0|  0.000| N/A|   756| 107753.706| N/A|   7,016|
| |Moore County|     0|  0.000| N/A|    44|  6781.751| N/A|   6,488|
| |Meigs County|     0|  0.000| N/A|    99|  7969.731| N/A|  12,422|
| |Stewart County|     0|  0.000| N/A|    70|  5103.901| N/A|  13,715|
| |Johnson County|     0|  0.000| N/A|   177|  9950.528| N/A|  17,788|
| |Houston County|     0|  0.000| N/A|    54|  6584.563| N/A|   8,201|
| |Hickman County|     0|  0.000| N/A|   233|  9254.111| N/A|  25,178|
| |Henry County|     0|  0.000| N/A|   225|  6956.253| N/A|  32,345|
| |Henderson County|     0|  0.000| N/A|   469| 16680.300| N/A|  28,117|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   961| 165.051| N/A|56,056|  9627.589| N/A|5,822,434|
| |Milwaukee County|   447| 472.653|  0.529|20,003| 21150.946| 157.711| 945,726|
| |Racine County|    77| 392.235|  2.699| 3,311| 16866.095| 184.756| 196,311|
| |Kenosha County|    58| 342.060| 12.266| 2,517| 14844.215| 123.849| 169,561|
| |Waukesha County|    57| 141.020|  4.948| 3,765|  9314.742| 210.293| 404,198|
| |Brown County|    52| 196.566|  3.780| 4,063| 15358.620| 173.885| 264,542|
| |Dane County|    37| 67.679|  0.000| 4,263|  7797.767| 59.448| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,375|  8417.302| 27.548| 163,354|
| |Washington County|    22| 161.724|  0.000|   913|  6711.557| 124.830| 136,034|
| |Walworth County|    21| 202.180|  0.000| 1,265| 12178.919| 134.786| 103,868|
| |Winnebago County|    18| 104.708|  2.485| 1,082|  6294.101| 79.113| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   592|  6635.209| 131.678|  89,221|
| |Waupaca County|    15| 294.175|  0.000|   392|  7687.782| 215.286|  50,990|
| |Grant County|    14| 272.167|  0.000|   331|  6434.806| 56.979|  51,439|
| |Outagamie County|    13| 69.191|  0.000| 1,132|  6024.962| 89.334| 187,885|
| |Marathon County|     7| 51.587| N/A|   589|  4340.713| N/A| 135,692|
| |Clark County|     7| 201.300| N/A|   179|  5147.524| N/A|  34,774|
| |Sheboygan County|     6| 52.020| N/A|   636|  5514.132| N/A| 115,340|
| |Fond du Lac County|     6| 58.025| N/A|   573|  5541.425| N/A| 103,403|
| |Dodge County|     5| 56.922| N/A|   728|  8287.890| N/A|  87,839|
| |Jefferson County|     5| 58.984| N/A|   573|  6759.547| N/A|  84,769|
| |Richland County|     4| 231.857| N/A|    32|  1854.857| N/A|  17,252|
| |Forest County|     4| 444.247| N/A|    59|  6552.643| N/A|   9,004|
| |Eau Claire County|     3| 28.668| N/A|   517|  4940.466| N/A| 104,646|
| |Sauk County|     3| 46.553| N/A|   405|  6284.721| N/A|  64,442|
| |Door County|     3| 108.429| N/A|    91|  3288.998| N/A|  27,668|
| |Barron County|     3| 66.307| N/A|   264|  5835.028| N/A|  45,244|
| |Marinette County|     3| 74.349| N/A|   342|  8475.836| N/A|  40,350|
| |Calumet County|     2| 39.929| N/A|   266|  5310.547| N/A|  50,089|
| |Buffalo County|     2| 153.480| N/A|    42|  3223.083| N/A|  13,031|
| |Adams County|     2| 98.912| N/A|    76|  3758.655| N/A|  20,220|
| |Trempealeau County|     2| 67.456| N/A|   313| 10556.848| N/A|  29,649|
| |St. Croix County|     2| 22.054| N/A|   457|  5039.311| N/A|  90,687|
| |Kewaunee County|     2| 97.876| N/A|   111|  5432.123| N/A|  20,434|
| |Polk County|     2| 45.680| N/A|   125|  2854.989| N/A|  43,783|
| |Green County|     1| 27.056| N/A|   131|  3544.372| N/A|  36,960|
| |Monroe County|     1| 21.620| N/A|   229|  4951.030| N/A|  46,253|
| |Marquette County|     1| 64.210| N/A|    71|  4558.880| N/A|  15,574|
| |Langlade County|     1| 52.113| N/A|    51|  2657.773| N/A|  19,189|
| |Manitowoc County|     1| 12.661| N/A|   311|  3937.656| N/A|  78,981|
| |Iron County|     1| 175.840| N/A|    72| 12660.454| N/A|   5,687|
| |La Crosse County|     1|  8.473| N/A|   836|  7083.785| N/A| 118,016|
| |Rusk County|     1| 70.532| N/A|    16|  1128.509| N/A|  14,178|
| |Jackson County|     1| 48.443| N/A|    49|  2373.686| N/A|  20,643|
| |Juneau County|     1| 37.471| N/A|   129|  4833.814| N/A|  26,687|
| |Wood County|     1| 13.699| N/A|   255|  3493.199| N/A|  72,999|
| |Columbia County|     1| 17.382| N/A|   228|  3963.012| N/A|  57,532|
| |Burnett County|     1| 64.876| N/A|    19|  1232.646| N/A|  15,414|
| |Bayfield County|     1| 66.507| N/A|    21|  1396.648| N/A|  15,036|
| |Pierce County|     0|  0.000| N/A|   178|  4163.353| N/A|  42,754|
| |Menominee County|     0|  0.000| N/A|    21|  4609.306| N/A|   4,556|
| |Vilas County|     0|  0.000| N/A|    39|  1757.153| N/A|  22,195|
| |Washburn County|     0|  0.000| N/A|    38|  2417.303| N/A|  15,720|
| |Price County|     0|  0.000| N/A|    22|  1647.817| N/A|  13,351|
| |Waushara County|     0|  0.000| N/A|   109|  4459.354| N/A|  24,443|
| |Portage County|     0|  0.000| N/A|   358|  5058.498| N/A|  70,772|
| |Douglas County|     0|  0.000| N/A|   139|  3221.321| N/A|  43,150|
| |Oconto County|     0|  0.000| N/A|   191|  5035.592| N/A|  37,930|
| |Vernon County|     0|  0.000| N/A|    60|  1946.661| N/A|  30,822|
| |Oneida County|     0|  0.000| N/A|    93|  2612.727| N/A|  35,595|
| |Dunn County|     0|  0.000| N/A|   107|  2358.491| N/A|  45,368|
| |Florence County|     0|  0.000| N/A|     7|  1629.802| N/A|   4,295|
| |Crawford County|     0|  0.000| N/A|    65|  4029.508| N/A|  16,131|
| |Sawyer County|     0|  0.000| N/A|    43|  2596.932| N/A|  16,558|
| |Green Lake County|     0|  0.000| N/A|    53|  2802.305| N/A|  18,913|
| |Lincoln County|     0|  0.000| N/A|    65|  2355.670| N/A|  27,593|
| |Taylor County|     0|  0.000| N/A|    55|  2703.633| N/A|  20,343|
| |Iowa County|     0|  0.000| N/A|    65|  2745.164| N/A|  23,678|
| |Ashland County|     0|  0.000| N/A|    20|  1285.182| N/A|  15,562|
| |Lafayette County|     0|  0.000| N/A|   112|  6720.672| N/A|  16,665|
| |Pepin County|     0|  0.000| N/A|    41|  5626.458| N/A|   7,287|
| |Chippewa County|     0|  0.000| N/A|   212|  3278.790| N/A|  64,658|
| |Shawano County|     0|  0.000| N/A|   163|  3985.428| N/A|  40,899|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   888| 281.452| N/A|46,231| 14652.924| N/A|3,155,070|
| |Polk County|   203| 414.150|  0.000| 9,781| 19954.668| 117.141| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,145|  9461.593| 123.508| 226,706|
| |Black Hawk County|    62| 472.460|  0.000| 3,022| 23028.622| 99.064| 131,228|
| |Woodbury County|    51| 494.632|  5.664| 3,656| 35458.310| 75.851| 103,107|
| |Muscatine County|    48| 1125.070|  3.677|   830| 19454.341| 95.327|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,796| 19218.217| 214.011|  93,453|
| |Wapello County|    32| 915.096| 13.443|   850| 24307.244| 71.492|  34,969|
| |Tama County|    29| 1720.660|  0.000|   539| 31980.539| 69.711|  16,854|
| |Dubuque County|    29| 298.014|  0.000| 1,549| 15918.036| 153.843|  97,311|
| |Jasper County|    25| 672.314| 26.893|   458| 12316.794| 49.411|  37,185|
| |Marshall County|    24| 609.617|  0.000| 1,394| 35408.570| 139.704|  39,369|
| |Pottawattamie County|    23| 246.765|  3.233| 1,227| 13164.389| 81.008|  93,206|
| |Cerro Gordo County|    17| 400.471|  0.000|   579| 13639.576|  0.000|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   136|  6155.239|  7.090|  22,095|
| |Johnson County|    15| 99.246|  0.000| 1,959| 12961.493| 135.636| 151,140|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644| 12.371|  11,035|
| |Story County|    14| 144.156|  0.000| 1,117| 11501.591| 45.039|  97,117|
| |Scott County|    12| 69.387|  0.000| 1,615|  9338.337| 73.189| 172,943|
| |Buena Vista County|    12| 611.621|  0.000| 1,786| 91029.562| 50.968|  19,620|
| |Washington County|    10| 455.270|  0.000|   288| 13111.769| 33.222|  21,965|
| |Poweshiek County|     8| 432.339| N/A|   150|  8106.355| N/A|  18,504|
| |Plymouth County|     8| 317.750| N/A|   443| 17595.424| N/A|  25,177|
| |Monroe County|     7| 908.265| N/A|    67|  8693.396| N/A|   7,707|
| |Bremer County|     7| 279.307| N/A|   192|  7661.001| N/A|  25,062|
| |Franklin County|     6| 595.829| N/A|   225| 22343.595| N/A|  10,070|
| |Webster County|     6| 167.112| N/A|   736| 20499.109| N/A|  35,904|
| |Guthrie County|     5| 467.771| N/A|   128| 11974.927| N/A|  10,689|
| |Allamakee County|     4| 292.248| N/A|   150| 10959.304| N/A|  13,687|
| |Dickinson County|     4| 231.777| N/A|   375| 21729.053| N/A|  17,258|
| |Lucas County|     4| 465.116| N/A|    50|  5813.953| N/A|   8,600|
| |Appanoose County|     3| 241.429| N/A|    43|  3460.486| N/A|  12,426|
| |Crawford County|     3| 178.359| N/A|   721| 42865.636| N/A|  16,820|
| |Clayton County|     3| 170.950| N/A|    99|  5641.347| N/A|  17,549|
| |Montgomery County|     3| 302.511| N/A|    45|  4537.663| N/A|   9,917|
| |Clinton County|     3| 64.615| N/A|   321|  6913.782| N/A|  46,429|
| |Clarke County|     3| 319.319| N/A|   188| 20010.644| N/A|   9,395|
| |Lee County|     3| 89.135| N/A|    97|  2882.016| N/A|  33,657|
| |Henry County|     3| 150.346| N/A|   114|  5713.140| N/A|  19,954|
| |Madison County|     2| 122.414| N/A|   105|  6426.735| N/A|  16,338|
| |Floyd County|     2| 127.861| N/A|   131|  8374.888| N/A|  15,642|
| |Emmet County|     2| 217.202| N/A|   181| 19656.820| N/A|   9,208|
| |Butler County|     2| 138.514| N/A|   115|  7964.540| N/A|  14,439|
| |Des Moines County|     2| 51.325| N/A|   139|  3567.121| N/A|  38,967|
| |Calhoun County|     2| 206.868| N/A|    82|  8481.589| N/A|   9,668|
| |Hancock County|     2| 188.147| N/A|   117| 11006.585| N/A|  10,630|
| |Sioux County|     2| 57.381| N/A|   602| 17271.554| N/A|  34,855|
| |Jones County|     2| 96.707| N/A|   124|  5995.842| N/A|  20,681|
| |Boone County|     2| 76.237| N/A|   231|  8805.367| N/A|  26,234|
| |Jackson County|     1| 51.443| N/A|   141|  7253.460| N/A|  19,439|
| |Audubon County|     1| 181.951| N/A|    28|  5094.614| N/A|   5,496|
| |Benton County|     1| 38.994| N/A|   145|  5654.124| N/A|  25,645|
| |Cass County|     1| 77.906| N/A|    48|  3739.483| N/A|  12,836|
| |Carroll County|     1| 49.591| N/A|   182|  9025.539| N/A|  20,165|
| |Cedar County|     1| 53.686| N/A|   120|  6442.261| N/A|  18,627|
| |Cherokee County|     1| 89.008| N/A|    98|  8722.741| N/A|  11,235|
| |Clay County|     1| 62.438| N/A|   171| 10676.823| N/A|  16,016|
| |Davis County|     1| 111.111| N/A|    50|  5555.556| N/A|   9,000|
| |Buchanan County|     1| 47.226| N/A|   114|  5383.707| N/A|  21,175|
| |Pocahontas County|     1| 151.080| N/A|   114| 17223.145| N/A|   6,619|
| |Keokuk County|     1| 97.599| N/A|    31|  3025.571| N/A|  10,246|
| |Delaware County|     1| 58.785| N/A|    91|  5349.480| N/A|  17,011|
| |Grundy County|     1| 81.753| N/A|    74|  6049.706| N/A|  12,232|
| |Hamilton County|     1| 67.691| N/A|   241| 16313.545| N/A|  14,773|
| |Humboldt County|     1| 104.624| N/A|    92|  9625.445| N/A|   9,558|
| |O'Brien County|     1| 72.711| N/A|   131|  9525.195| N/A|  13,753|
| |Ringgold County|     1| 204.332| N/A|    21|  4290.969| N/A|   4,894|
| |Iowa County|     1| 61.789| N/A|    90|  5561.048| N/A|  16,184|
| |Wright County|     1| 79.605| N/A|   444| 35344.690| N/A|  12,562|
| |Winneshiek County|     1| 50.023| N/A|    86|  4301.936| N/A|  19,991|
| |Van Buren County|     1| 141.965| N/A|    33|  4684.838| N/A|   7,044|
| |Warren County|     1| 19.430| N/A|   534| 10375.782| N/A|  51,466|
| |Shelby County|     1| 87.306| N/A|   169| 14754.671| N/A|  11,454|
| |Union County|     1| 81.693| N/A|    72|  5881.872| N/A|  12,241|
| |Wayne County|     1| 155.255| N/A|    18|  2794.597| N/A|   6,441|
| |Decatur County|     0|  0.000| N/A|    22|  2795.426| N/A|   7,870|
| |Jefferson County|     0|  0.000| N/A|    77|  4208.800| N/A|  18,295|
| |Ida County|     0|  0.000| N/A|    29|  4227.405| N/A|   6,860|
| |Howard County|     0|  0.000| N/A|    49|  5350.513| N/A|   9,158|
| |Harrison County|     0|  0.000| N/A|    98|  6975.585| N/A|  14,049|
| |Hardin County|     0|  0.000| N/A|   166|  9853.971| N/A|  16,846|
| |Greene County|     0|  0.000| N/A|    38|  4275.428| N/A|   8,888|
| |Fremont County|     0|  0.000| N/A|    35|  5028.736| N/A|   6,960|
| |Fayette County|     0|  0.000| N/A|    81|  4122.137| N/A|  19,650|
| |Chickasaw County|     0|  0.000| N/A|    51|  4273.862| N/A|  11,933|
| |Adams County|     0|  0.000| N/A|    16|  4441.977| N/A|   3,602|
| |Adair County|     0|  0.000| N/A|    21|  2936.242| N/A|   7,152|
| |Kossuth County|     0|  0.000| N/A|    78|  5265.645| N/A|  14,813|
| |Mills County|     0|  0.000| N/A|    83|  5493.415| N/A|  15,109|
| |Lyon County|     0|  0.000| N/A|   106|  9017.439| N/A|  11,755|
| |Worth County|     0|  0.000| N/A|    61|  8264.463| N/A|   7,381|
| |Winnebago County|     0|  0.000| N/A|    77|  7436.739| N/A|  10,354|
| |Taylor County|     0|  0.000| N/A|    93| 15193.596| N/A|   6,121|
| |Sac County|     0|  0.000| N/A|    81|  8332.476| N/A|   9,721|
| |Palo Alto County|     0|  0.000| N/A|    80|  9002.926| N/A|   8,886|
| |Page County|     0|  0.000| N/A|    76|  5030.780| N/A|  15,107|
| |Osceola County|     0|  0.000| N/A|    78| 13091.641| N/A|   5,958|
| |Monona County|     0|  0.000| N/A|    90| 10446.895| N/A|   8,615|
| |Mitchell County|     0|  0.000| N/A|    76|  7179.293| N/A|  10,586|
| |Marion County|     0|  0.000| N/A|   155|  4661.234| N/A|  33,253|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   854| 277.259| N/A|51,856| 16835.511| N/A|3,080,156|
| |Clark County|   716| 315.876|  0.000|44,997| 19851.194| 408.080|2,266,715|
| |Washoe County|   115| 243.893|  0.901| 5,369| 11386.604| 105.576| 471,519|
| |Nye County|     9| 193.453| N/A|   362|  7781.098| N/A|  46,523|
| |Lyon County|     5| 86.941| N/A|   209|  3634.151| N/A|  57,510|
| |Humboldt County|     4| 237.657| N/A|    96|  5703.761| N/A|  16,831|
| |Elko County|     2| 37.895| N/A|   493|  9341.013| N/A|  52,778|
| |Lander County|     1| 180.766| N/A|    50|  9038.322| N/A|   5,532|
| |Churchill County|     1| 40.146| N/A|    49|  1967.160| N/A|  24,909|
| |White Pine County|     1| 104.384| N/A|    14|  1461.378| N/A|   9,580|
| |Carson City|     0|  0.000| N/A|     0|     0.000| N/A|  55,916|
| |Mineral County|     0|  0.000| N/A|    11|  2441.731| N/A|   4,505|
| |Lincoln County|     0|  0.000| N/A|     4|   771.754| N/A|   5,183|
| |Eureka County|     0|  0.000| N/A|     2|   985.707| N/A|   2,029|
| |Esmeralda County|     0|  0.000| N/A|     0|     0.000| N/A|     873|
| |Douglas County|     0|  0.000| N/A|   183|  3741.949| N/A|  48,905|
| |Pershing County|     0|  0.000| N/A|    13|  1933.086| N/A|   6,725|
| |Storey County|     0|  0.000| N/A|     4|   970.167| N/A|   4,123|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   751| 168.096| N/A|32,197|  7206.660| N/A|4,467,673|
| |Jefferson County|   236| 307.790|  1.663| 7,414|  9669.295| 174.957| 766,757|
| |Fayette County|    46| 142.348|  0.000| 2,851|  8822.474| 156.765| 323,152|
| |Kenton County|    38| 227.548|  2.513| 1,351|  8089.917| 119.762| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   412|  9219.890| 100.703|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,048|  7845.427| 109.038| 133,581|
| |Graves County|    22| 590.350|  0.000|   522| 14007.406| 186.542|  37,266|
| |Logan County|    22| 811.748|  0.000|   303| 11179.987| 36.898|  27,102|
| |Shelby County|    22| 448.760|  0.000|   720| 14686.684| 119.206|  49,024|
| |Warren County|    22| 165.543|  0.000| 2,485| 18698.832| 218.216| 132,896|
| |Adair County|    19| 989.480|  0.000|   203| 10571.815| 24.616|  19,202|
| |Butler County|    15| 1164.687|  0.000|   296| 22983.151| 141.266|  12,879|
| |Oldham County|    14| 209.584|  7.485|   582|  8712.705| 190.429|  66,799|
| |Jackson County|    14| 1050.341|  0.000|   143| 10728.487|  0.000|  13,329|
| |Campbell County|    13| 138.913|  0.000|   542|  5791.588| 101.513|  93,584|
| |Edmonson County|    12| 987.654|  0.000|    96|  7901.235| 164.609|  12,150|
| |Grayson County|    11| 416.241|  0.000|   186|  7038.256| 128.837|  26,427|
| |Muhlenberg County|    10| 326.563|  5.123|   618| 20181.569| 101.036|  30,622|
| |Casey County|    10| 618.850|  0.000|   154|  9530.293| 309.425|  16,159|
| |Allen County|     8| 375.323| N/A|   217| 10180.624| N/A|  21,315|
| |Hardin County|     8| 72.099| N/A|   533|  4803.619| N/A| 110,958|
| |Knox County|     8| 256.863| N/A|   216|  6935.303| N/A|  31,145|
| |Gallatin County|     8| 902.018| N/A|    79|  8907.430| N/A|   8,869|
| |Daviess County|     8| 78.809| N/A|   723|  7122.381| N/A| 101,511|
| |Simpson County|     7| 376.911| N/A|   142|  7645.919| N/A|  18,572|
| |Ohio County|     7| 291.740| N/A|   341| 14211.886| N/A|  23,994|
| |Clark County|     7| 193.034| N/A|   162|  4467.363| N/A|  36,263|
| |Christian County|     6| 85.153| N/A|   478|  6783.895| N/A|  70,461|
| |Clay County|     5| 251.244| N/A|   144|  7235.817| N/A|  19,901|
| |Grant County|     5| 199.450| N/A|   106|  4228.330| N/A|  25,069|
| |Franklin County|     5| 98.057| N/A|   260|  5098.939| N/A|  50,991|
| |Russell County|     5| 278.971| N/A|   100|  5579.423| N/A|  17,923|
| |Laurel County|     4| 65.775| N/A|   392|  6445.990| N/A|  60,813|
| |Lyon County|     4| 487.211| N/A|    30|  3654.080| N/A|   8,210|
| |Calloway County|     4| 102.561| N/A|   198|  5076.793| N/A|  39,001|
| |Henderson County|     4| 88.476| N/A|   328|  7255.032| N/A|  45,210|
| |McCracken County|     4| 61.145| N/A|   344|  5258.492| N/A|  65,418|
| |Bullitt County|     4| 48.974| N/A|   318|  3893.433| N/A|  81,676|
| |Boyd County|     3| 64.215| N/A|   179|  3831.500| N/A|  46,718|
| |Perry County|     3| 116.469| N/A|   193|  7492.818| N/A|  25,758|
| |Pike County|     3| 51.835| N/A|   224|  3870.343| N/A|  57,876|
| |Harlan County|     3| 115.340| N/A|   212|  8150.711| N/A|  26,010|
| |Henry County|     2| 124.023| N/A|   100|  6201.166| N/A|  16,126|
| |Marshall County|     2| 64.309| N/A|   128|  4115.756| N/A|  31,100|
| |Meade County|     2| 69.999| N/A|    91|  3184.936| N/A|  28,572|
| |Metcalfe County|     2| 198.590| N/A|    53|  5262.635| N/A|  10,071|
| |Monroe County|     2| 187.793| N/A|    89|  8356.808| N/A|  10,650|
| |Nelson County|     2| 43.259| N/A|   197|  4261.026| N/A|  46,233|
| |Pulaski County|     2| 30.779| N/A|   263|  4047.461| N/A|  64,979|
| |Taylor County|     2| 77.613| N/A|   104|  4035.857| N/A|  25,769|
| |Barren County|     2| 45.199| N/A|   342|  7728.988| N/A|  44,249|
| |Bell County|     2| 76.829| N/A|   285| 10948.064| N/A|  26,032|
| |Breckinridge County|     2| 97.671| N/A|    52|  2539.434| N/A|  20,477|
| |Carroll County|     2| 188.129| N/A|   145| 13639.357| N/A|  10,631|
| |Floyd County|     2| 56.197| N/A|    84|  2360.280| N/A|  35,589|
| |Green County|     2| 182.799| N/A|    31|  2833.379| N/A|  10,941|
| |Bourbon County|     1| 50.536| N/A|    71|  3588.033| N/A|  19,788|
| |Bath County|     1| 80.000| N/A|    36|  2880.000| N/A|  12,500|
| |Knott County|     1| 67.540| N/A|    47|  3174.389| N/A|  14,806|
| |Larue County|     1| 69.454| N/A|    51|  3542.159| N/A|  14,398|
| |Whitley County|     1| 27.576| N/A|   148|  4081.182| N/A|  36,264|
| |Webster County|     1| 77.268| N/A|    83|  6413.228| N/A|  12,942|
| |Livingston County|     1| 108.767| N/A|    33|  3589.297| N/A|   9,194|
| |Mason County|     1| 58.582| N/A|    53|  3104.862| N/A|  17,070|
| |Lincoln County|     1| 40.735| N/A|    99|  4032.751| N/A|  24,549|
| |McLean County|     1| 108.613| N/A|    40|  4344.520| N/A|   9,207|
| |Madison County|     1| 10.754| N/A|   411|  4419.973| N/A|  92,987|
| |Greenup County|     1| 28.492| N/A|    94|  2678.215| N/A|  35,098|
| |Fulton County|     1| 167.532| N/A|    62| 10386.999| N/A|   5,969|
| |Crittenden County|     1| 113.559| N/A|    26|  2952.532| N/A|   8,806|
| |Carter County|     1| 37.318| N/A|    98|  3657.126| N/A|  26,797|
| |Carlisle County|     1| 210.084| N/A|    32|  6722.689| N/A|   4,760|
| |Anderson County|     1| 43.962| N/A|    77|  3385.062| N/A|  22,747|
| |Fleming County|     0|  0.000| N/A|    57|  3909.197| N/A|  14,581|
| |Todd County|     0|  0.000| N/A|    33|  2684.236| N/A|  12,294|
| |Spencer County|     0|  0.000| N/A|   107|  5529.430| N/A|  19,351|
| |Scott County|     0|  0.000| N/A|   346|  6069.749| N/A|  57,004|
| |Rowan County|     0|  0.000| N/A|    69|  2820.932| N/A|  24,460|
| |Rockcastle County|     0|  0.000| N/A|    61|  3653.789| N/A|  16,695|
| |Robertson County|     0|  0.000| N/A|     3|  1423.150| N/A|   2,108|
| |Powell County|     0|  0.000| N/A|    49|  3964.722| N/A|  12,359|
| |Trimble County|     0|  0.000| N/A|    32|  3777.594| N/A|   8,471|
| |Trigg County|     0|  0.000| N/A|    53|  3617.501| N/A|  14,651|
| |Union County|     0|  0.000| N/A|    57|  3963.563| N/A|  14,381|
| |Hickman County|     0|  0.000| N/A|    35|  7990.868| N/A|   4,380|
| |Martin County|     0|  0.000| N/A|    32|  2858.419| N/A|  11,195|
| |Marion County|     0|  0.000| N/A|   113|  5863.125| N/A|  19,273|
| |Magoffin County|     0|  0.000| N/A|    30|  2466.902| N/A|  12,161|
| |McCreary County|     0|  0.000| N/A|    37|  2147.293| N/A|  17,231|
| |Letcher County|     0|  0.000| N/A|    52|  2412.657| N/A|  21,553|
| |Leslie County|     0|  0.000| N/A|    27|  2733.624| N/A|   9,877|
| |Lee County|     0|  0.000| N/A|     4|   540.321| N/A|   7,403|
| |Lawrence County|     0|  0.000| N/A|    34|  2219.756| N/A|  15,317|
| |Johnson County|     0|  0.000| N/A|    40|  1802.776| N/A|  22,188|
| |Jessamine County|     0|  0.000| N/A|   308|  5691.583| N/A|  54,115|
| |Hart County|     0|  0.000| N/A|    84|  4412.924| N/A|  19,035|
| |Washington County|     0|  0.000| N/A|    65|  5374.122| N/A|  12,095|
| |Harrison County|     0|  0.000| N/A|   117|  6195.065| N/A|  18,886|
| |Nicholas County|     0|  0.000| N/A|    20|  2751.410| N/A|   7,269|
| |Owen County|     0|  0.000| N/A|    43|  3944.592| N/A|  10,901|
| |Owsley County|     0|  0.000| N/A|    10|  2265.006| N/A|   4,415|
| |Pendleton County|     0|  0.000| N/A|    36|  2467.443| N/A|  14,590|
| |Woodford County|     0|  0.000| N/A|   135|  5049.749| N/A|  26,734|
| |Wolfe County|     0|  0.000| N/A|    11|  1536.957| N/A|   7,157|
| |Wayne County|     0|  0.000| N/A|    53|  2606.600| N/A|  20,333|
| |Mercer County|     0|  0.000| N/A|    77|  3510.692| N/A|  21,933|
| |Menifee County|     0|  0.000| N/A|    29|  4469.102| N/A|   6,489|
| |Montgomery County|     0|  0.000| N/A|   114|  4048.727| N/A|  28,157|
| |Elliott County|     0|  0.000| N/A|     8|  1064.254| N/A|   7,517|
| |Cumberland County|     0|  0.000| N/A|    40|  6047.777| N/A|   6,614|
| |Clinton County|     0|  0.000| N/A|    27|  2642.396| N/A|  10,218|
| |Caldwell County|     0|  0.000| N/A|    49|  3844.042| N/A|  12,747|
| |Breathitt County|     0|  0.000| N/A|    26|  2058.591| N/A|  12,630|
| |Bracken County|     0|  0.000| N/A|    29|  3492.713| N/A|   8,303|
| |Boyle County|     0|  0.000| N/A|   142|  4723.886| N/A|  30,060|
| |Ballard County|     0|  0.000| N/A|    31|  3930.020| N/A|   7,888|
| |Morgan County|     0|  0.000| N/A|    30|  2254.114| N/A|  13,309|
| |Hancock County|     0|  0.000| N/A|    49|  5617.978| N/A|   8,722|
| |Lewis County|     0|  0.000| N/A|    37|  2787.194| N/A|  13,275|
| |Estill County|     0|  0.000| N/A|    17|  1205.161| N/A|  14,106|
| |Garrard County|     0|  0.000| N/A|    69|  3905.808| N/A|  17,666|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   658| 313.807| N/A|20,072|  9572.550| N/A|2,096,829|
| |McKinley County|   222| 3110.681|  8.087| 4,009| 56174.422| 70.060|  71,367|
| |San Juan County|   182| 1468.239|  8.067| 3,008| 24266.284| 24.018| 123,958|
| |Bernalillo County|   124| 182.589|  0.768| 4,947|  7284.416| 88.349| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,104|  7523.101| 50.546| 146,748|
| |Dona Ana County|    24| 109.993|  1.976| 2,272| 10412.704| 132.909| 218,195|
| |Cibola County|    17| 637.301|  0.000|   345| 12933.458| 159.312|  26,675|
| |Otero County|    10| 148.170|  0.000|   193|  2859.683| 57.927|  67,490|
| |Chaves County|     6| 92.858| N/A|   384|  5942.893| N/A|  64,615|
| |Socorro County|     6| 360.642| N/A|    73|  4387.810| N/A|  16,637|
| |Rio Arriba County|     5| 128.465| N/A|   298|  7656.535| N/A|  38,921|
| |Lea County|     4| 56.283| N/A|   679|  9553.961| N/A|  71,070|
| |Valencia County|     4| 52.159| N/A|   381|  4968.183| N/A|  76,688|
| |Eddy County|     4| 68.423| N/A|   267|  4567.225| N/A|  58,460|
| |Santa Fe County|     3| 19.952| N/A|   602|  4003.778| N/A| 150,358|
| |Luna County|     3| 126.534| N/A|   238| 10038.382| N/A|  23,709|
| |Grant County|     2| 74.080| N/A|    68|  2518.705| N/A|  26,998|
| |Curry County|     2| 40.855| N/A|   493| 10070.679| N/A|  48,954|
| |Colfax County|     1| 83.745| N/A|    14|  1172.431| N/A|  11,941|
| |Lincoln County|     1| 51.093| N/A|   110|  5620.274| N/A|  19,572|
| |Quay County|     1| 121.168| N/A|    34|  4119.714| N/A|   8,253|
| |Roosevelt County|     1| 54.054| N/A|   144|  7783.784| N/A|  18,500|
| |Taos County|     1| 30.560| N/A|    99|  3025.395| N/A|  32,723|
| |Torrance County|     1| 64.679| N/A|    60|  3880.732| N/A|  15,461|
| |Catron County|     1| 283.527| N/A|     4|  1134.108| N/A|   3,527|
| |San Miguel County|     0|  0.000| N/A|    42|  1539.759| N/A|  27,277|
| |Union County|     0|  0.000| N/A|    28|  6898.251| N/A|   4,059|
| |Sierra County|     0|  0.000| N/A|    30|  2780.095| N/A|  10,791|
| |Guadalupe County|     0|  0.000| N/A|    31|  7209.302| N/A|   4,300|
| |Mora County|     0|  0.000| N/A|     6|  1327.140| N/A|   4,521|
| |Los Alamos County|     0|  0.000| N/A|    20|  1032.578| N/A|  19,369|
| |Hidalgo County|     0|  0.000| N/A|    88| 20962.363| N/A|   4,198|
| |Harding County|     0|  0.000| N/A|     1|  1600.000| N/A|     625|
| |De Baca County|     0|  0.000| N/A|     0|     0.000| N/A|   1,748|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   587| 831.740| N/A|12,398| 17567.152| N/A| 705,749|
| |District of Columbia|   587| 831.740|  1.417|12,398| 17567.152|  0.000| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   587| 602.815| N/A|14,905| 15306.584| N/A| 973,764|
| |New Castle County|   289| 517.223|  3.579| 6,994| 12517.159| 112.002| 558,753|
| |Sussex County|   191| 815.455|  0.000| 5,685| 24271.534| 69.972| 234,225|
| |Kent County|   107| 591.860|  0.000| 2,226| 12312.900| 88.502| 180,786|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   566| 143.039| N/A|39,452|  9970.252| N/A|3,956,971|
| |Oklahoma County|   102| 127.910|  5.016| 9,593| 12029.836| 147.975| 797,434|
| |Tulsa County|   101| 155.014|  0.000| 9,418| 14454.717| 257.049| 651,552|
| |Cleveland County|    52| 183.090| 10.563| 2,780|  9788.250| 141.867| 284,014|
| |Washington County|    39| 756.885|  0.000|   589| 11430.900| 163.146|  51,527|
| |McCurtain County|    26| 791.910| 12.605|   835| 25432.505| 153.397|  32,832|
| |Wagoner County|    22| 270.639|  0.000|   762|  9373.962| 169.185|  81,289|
| |Delaware County|    19| 441.768|  0.000|   404|  9393.383| 36.465|  43,009|
| |Rogers County|    16| 173.050|  8.954|   855|  9247.342| 237.943|  92,459|
| |Muskogee County|    16| 235.304|  0.000|   463|  6809.124| 169.264|  67,997|
| |Caddo County|    14| 486.753|  0.000|   383| 13316.181| 278.326|  28,762|
| |Creek County|    13| 181.762|  0.000|   510|  7130.673| 118.845|  71,522|
| |Osage County|    11| 234.227|  0.000|   376|  8006.303| 109.337|  46,963|
| |Comanche County|    10| 82.816|  0.000|   785|  6501.089| 60.467| 120,749|
| |Kay County|    10| 229.684|  0.000|   223|  5121.962| 89.424|  43,538|
| |Greer County|     8| 1400.560| N/A|    81| 14180.672| N/A|   5,712|
| |Pottawatomie County|     8| 110.205| N/A|   414|  5703.108| N/A|  72,592|
| |Texas County|     7| 350.298| N/A| 1,037| 51894.110| N/A|  19,983|
| |Mayes County|     6| 145.985| N/A|   290|  7055.961| N/A|  41,100|
| |Grady County|     6| 107.461| N/A|   417|  7468.568| N/A|  55,834|
| |Canadian County|     6| 40.457| N/A| 1,106|  7457.554| N/A| 148,306|
| |Adair County|     6| 270.343| N/A|   311| 14012.796| N/A|  22,194|
| |Jackson County|     5| 203.832| N/A|   489| 19934.774| N/A|  24,530|
| |Seminole County|     5| 206.118| N/A|   209|  8615.714| N/A|  24,258|
| |Carter County|     4| 83.141| N/A|   312|  6485.003| N/A|  48,111|
| |McClain County|     4| 98.829| N/A|   402|  9932.302| N/A|  40,474|
| |Sequoyah County|     4| 96.226| N/A|   279|  6711.732| N/A|  41,569|
| |Garvin County|     4| 144.347| N/A|   218|  7866.912| N/A|  27,711|
| |Garfield County|     4| 65.514| N/A|   382|  6256.551| N/A|  61,056|
| |Okmulgee County|     3| 77.993| N/A|   405| 10529.052| N/A|  38,465|
| |Payne County|     3| 36.682| N/A|   678|  8290.130| N/A|  81,784|
| |Pittsburg County|     3| 68.722| N/A|   214|  4902.185| N/A|  43,654|
| |Pawnee County|     3| 183.195| N/A|   126|  7694.187| N/A|  16,376|
| |Ottawa County|     2| 64.253| N/A|   348| 11180.004| N/A|  31,127|
| |Lincoln County|     2| 57.344| N/A|   142|  4071.451| N/A|  34,877|
| |Cherokee County|     2| 41.104| N/A|   360|  7398.730| N/A|  48,657|
| |Cotton County|     2| 352.983| N/A|    18|  3176.844| N/A|   5,666|
| |Noble County|     2| 179.678| N/A|    81|  7276.974| N/A|  11,131|
| |Pontotoc County|     2| 52.241| N/A|   185|  4832.306| N/A|  38,284|
| |Stephens County|     2| 46.357| N/A|   182|  4218.529| N/A|  43,143|
| |Logan County|     1| 20.829| N/A|   188|  3915.769| N/A|  48,011|
| |Beckham County|     1| 45.748| N/A|    45|  2058.649| N/A|  21,859|
| |Le Flore County|     1| 20.059| N/A|   261|  5235.392| N/A|  49,853|
| |Latimer County|     1| 99.275| N/A|    77|  7644.197| N/A|  10,073|
| |Kiowa County|     1| 114.837| N/A|    27|  3100.597| N/A|   8,708|
| |Bryan County|     1| 20.836| N/A|   398|  8292.530| N/A|  47,995|
| |Hughes County|     1| 75.307| N/A|   115|  8660.291| N/A|  13,279|
| |Choctaw County|     1| 68.157| N/A|   171| 11654.853| N/A|  14,672|
| |Nowata County|     1| 99.246| N/A|    56|  5557.761| N/A|  10,076|
| |Tillman County|     1| 137.931| N/A|    57|  7862.069| N/A|   7,250|
| |Major County|     1| 131.079| N/A|    26|  3408.048| N/A|   7,629|
| |McIntosh County|     1| 51.031| N/A|   157|  8011.839| N/A|  19,596|
| |Ellis County|     0|  0.000| N/A|     3|   777.403| N/A|   3,859|
| |Custer County|     0|  0.000| N/A|   194|  6688.963| N/A|  29,003|
| |Craig County|     0|  0.000| N/A|    77|  5444.774| N/A|  14,142|
| |Coal County|     0|  0.000| N/A|    31|  5641.492| N/A|   5,495|
| |Cimarron County|     0|  0.000| N/A|     1|   467.946| N/A|   2,137|
| |Blaine County|     0|  0.000| N/A|    38|  4030.120| N/A|   9,429|
| |Beaver County|     0|  0.000| N/A|    36|  6778.384| N/A|   5,311|
| |Atoka County|     0|  0.000| N/A|    65|  4724.524| N/A|  13,758|
| |Alfalfa County|     0|  0.000| N/A|     3|   526.131| N/A|   5,702|
| |Harmon County|     0|  0.000| N/A|    25|  9423.294| N/A|   2,653|
| |Dewey County|     0|  0.000| N/A|     8|  1635.657| N/A|   4,891|
| |Grant County|     0|  0.000| N/A|    12|  2769.444| N/A|   4,333|
| |Woodward County|     0|  0.000| N/A|    35|  1731.730| N/A|  20,211|
| |Pushmataha County|     0|  0.000| N/A|   103|  9282.624| N/A|  11,096|
| |Woods County|     0|  0.000| N/A|    19|  2160.810| N/A|   8,793|
| |Harper County|     0|  0.000| N/A|     9|  2440.347| N/A|   3,688|
| |Washita County|     0|  0.000| N/A|    26|  2381.825| N/A|  10,916|
| |Roger Mills County|     0|  0.000| N/A|     8|  2232.766| N/A|   3,583|
| |Okfuskee County|     0|  0.000| N/A|    57|  4752.772| N/A|  11,993|
| |Murray County|     0|  0.000| N/A|    63|  4476.657| N/A|  14,073|
| |Marshall County|     0|  0.000| N/A|   100|  5906.326| N/A|  16,931|
| |Love County|     0|  0.000| N/A|    65|  6339.608| N/A|  10,253|
| |Kingfisher County|     0|  0.000| N/A|   113|  7167.777| N/A|  15,765|
| |Johnston County|     0|  0.000| N/A|    42|  3788.904| N/A|  11,085|
| |Jefferson County|     0|  0.000| N/A|    32|  5331.556| N/A|   6,002|
| |Haskell County|     0|  0.000| N/A|    47|  3722.183| N/A|  12,627|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   490| 162.370| N/A|43,729| 14490.338| N/A|3,017,804|
| |Pulaski County|    79| 201.576|  0.000| 5,054| 12895.785| 247.696| 391,911|
| |Washington County|    48| 200.680|  3.484| 6,120| 25586.675| 237.710| 239,187|
| |Benton County|    40| 143.297|  1.898| 4,611| 16518.534| 118.220| 279,141|
| |Jefferson County|    39| 583.623|  6.358| 1,404| 21010.415| 329.223|  66,824|
| |Crittenden County|    20| 417.058|  6.542| 1,269| 26462.308| 544.310|  47,955|
| |Union County|    17| 439.481| 10.754|   452| 11685.021| 77.555|  38,682|
| |Sebastian County|    15| 117.346|  1.227| 1,919| 15012.478| 344.215| 127,827|
| |Yell County|    14| 656.014|  0.000| 1,043| 48873.061| 488.363|  21,341|
| |Craighead County|    12| 108.763|  0.000| 1,156| 10477.468| 159.840| 110,332|
| |Lincoln County|    11| 844.595|  0.000| 1,195| 91753.686| 499.079|  13,024|
| |Mississippi County|    11| 270.596| 10.452|   853| 20983.494| 959.386|  40,651|
| |Lawrence County|    10| 609.533|  0.000|   186| 11337.316| 55.942|  16,406|
| |Sevier County|    10| 587.993|  0.000|   944| 55506.556| 241.590|  17,007|
| |Pope County|    10| 156.074| 15.607| 1,241| 19368.835| 324.649|  64,072|
| |Hot Spring County|    10| 296.112| 24.966| 1,475| 43676.527| 266.501|  33,771|
| |Nevada County|     9| 1090.645| N/A|   134| 16238.488| N/A|   8,252|
| |Garland County|     8| 80.494| N/A|   879|  8844.304| N/A|  99,386|
| |Columbia County|     7| 298.418| N/A|   207|  8824.658| N/A|  23,457|
| |Phillips County|     7| 393.657| N/A|   289| 16252.390| N/A|  17,782|
| |Chicot County|     7| 691.836| N/A|   552| 54556.236| N/A|  10,118|
| |Carroll County|     7| 246.653| N/A|   341| 12015.504| N/A|  28,380|
| |Lee County|     7| 790.335| N/A|   890| 100485.492| N/A|   8,857|
| |Saline County|     6| 49.005| N/A|   922|  7530.403| N/A| 122,437|
| |Faulkner County|     5| 39.680| N/A| 1,229|  9753.426| N/A| 126,007|
| |Cleburne County|     5| 200.650| N/A|   183|  7343.794| N/A|  24,919|
| |Sharp County|     5| 286.664| N/A|   106|  6077.285| N/A|  17,442|
| |Miller County|     4| 92.471| N/A|   475| 10980.882| N/A|  43,257|
| |Ashley County|     4| 203.490| N/A|   262| 13328.585| N/A|  19,657|
| |Clay County|     4| 274.895| N/A|   112|  7697.065| N/A|  14,551|
| |Poinsett County|     3| 127.508| N/A|   173|  7352.941| N/A|  23,528|
| |Newton County|     3| 386.947| N/A|   100| 12898.233| N/A|   7,753|
| |Bradley County|     3| 278.733| N/A|   155| 14401.189| N/A|  10,763|
| |Conway County|     3| 143.913| N/A|   138|  6619.975| N/A|  20,846|
| |Crawford County|     3| 47.426| N/A|   566|  8947.626| N/A|  63,257|
| |Randolph County|     3| 167.056| N/A|   178|  9912.017| N/A|  17,958|
| |St. Francis County|     3| 120.029| N/A| 1,144| 45770.985| N/A|  24,994|
| |Drew County|     3| 164.663| N/A|   171|  9385.806| N/A|  18,219|
| |Van Buren County|     2| 120.882| N/A|    52|  3142.943| N/A|  16,545|
| |White County|     2| 25.396| N/A|   271|  3441.139| N/A|  78,753|
| |Cleveland County|     2| 251.383| N/A|    76|  9552.539| N/A|   7,956|
| |Ouachita County|     2| 85.536| N/A|    81|  3464.203| N/A|  23,382|
| |Franklin County|     2| 112.899| N/A|   111|  6265.876| N/A|  17,715|
| |Hempstead County|     2| 92.885| N/A|   224| 10403.121| N/A|  21,532|
| |Howard County|     2| 151.492| N/A|   303| 22951.068| N/A|  13,202|
| |Lonoke County|     2| 27.282| N/A|   469|  6397.577| N/A|  73,309|
| |Lafayette County|     2| 301.932| N/A|    50|  7548.309| N/A|   6,624|
| |Desha County|     2| 176.041| N/A|   165| 14523.369| N/A|  11,361|
| |Cross County|     2| 121.810| N/A|   172| 10475.668| N/A|  16,419|
| |Izard County|     1| 73.373| N/A|    45|  3301.783| N/A|  13,629|
| |Stone County|     1| 79.962| N/A|    59|  4717.735| N/A|  12,506|
| |Jackson County|     1| 59.812| N/A|    61|  3648.544| N/A|  16,719|
| |Pike County|     1| 93.301| N/A|    84|  7837.283| N/A|  10,718|
| |Logan County|     1| 46.585| N/A|   196|  9130.718| N/A|  21,466|
| |Polk County|     1| 50.090| N/A|   132|  6611.901| N/A|  19,964|
| |Madison County|     1| 60.328| N/A|   265| 15986.969| N/A|  16,576|
| |Little River County|     1| 81.573| N/A|   158| 12888.490| N/A|  12,259|
| |Greene County|     1| 22.063| N/A|   403|  8891.340| N/A|  45,325|
| |Independence County|     1| 26.438| N/A|   413| 10918.705| N/A|  37,825|
| |Arkansas County|     1| 57.189| N/A|   206| 11780.853| N/A|  17,486|
| |Boone County|     1| 26.715| N/A|   184|  4915.580| N/A|  37,432|
| |Clark County|     1| 44.803| N/A|   164|  7347.670| N/A|  22,320|
| |Baxter County|     0|  0.000| N/A|    64|  1526.281| N/A|  41,932|
| |Dallas County|     0|  0.000| N/A|    59|  8417.749| N/A|   7,009|
| |Calhoun County|     0|  0.000| N/A|    13|  2505.300| N/A|   5,189|
| |Fulton County|     0|  0.000| N/A|    29|  2324.277| N/A|  12,477|
| |Grant County|     0|  0.000| N/A|   130|  7117.438| N/A|  18,265|
| |Montgomery County|     0|  0.000| N/A|    29|  3227.242| N/A|   8,986|
| |Monroe County|     0|  0.000| N/A|    53|  7909.267| N/A|   6,701|
| |Marion County|     0|  0.000| N/A|    24|  1437.642| N/A|  16,694|
| |Johnson County|     0|  0.000| N/A|   639| 24042.441| N/A|  26,578|
| |Perry County|     0|  0.000| N/A|    49|  4686.753| N/A|  10,455|
| |Woodruff County|     0|  0.000| N/A|    20|  3164.557| N/A|   6,320|
| |Searcy County|     0|  0.000| N/A|    27|  3425.961| N/A|   7,881|
| |Prairie County|     0|  0.000| N/A|    76|  9426.941| N/A|   8,062|
| |Scott County|     0|  0.000| N/A|    45|  4377.006| N/A|  10,281|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   418| 307.418| N/A| 6,689|  4919.428| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  2.398| 3,787|  9080.990| 24.735| 417,025|
| |Rockingham County|    95| 306.680|  0.000| 1,654|  5339.463| 31.110| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   458|  3025.279|  0.000| 151,391|
| |Strafford County|    13| 99.515|  0.000|   338|  2587.401| 25.669| 130,633|
| |Belknap County|     4| 65.250| N/A|   110|  1794.366| N/A|  61,303|
| |Cheshire County|     3| 39.430| N/A|    93|  1222.317| N/A|  76,085|
| |Carroll County|     1| 20.446| N/A|    90|  1840.114| N/A|  48,910|
| |Grafton County|     1| 11.125| N/A|   103|  1145.896| N/A|  89,886|
| |Sullivan County|     1| 23.177| N/A|    40|   927.085| N/A|  43,146|
| |Coos County|     0|  0.000| N/A|    16|   506.923| N/A|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   367| 125.973| N/A|28,782|  9879.471| N/A|2,913,314|
| |Johnson County|    98| 162.682|  0.000| 5,240|  8698.525| 149.402| 602,401|
| |Wyandotte County|    96| 580.309|  2.559| 4,618| 27915.299| 380.828| 165,429|
| |Sedgwick County|    43| 83.327|  0.953| 4,436|  8596.200| 178.719| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,441|  8146.996| 70.088| 176,875|
| |Lyon County|    13| 391.625|  0.000|   680| 20485.013| 338.186|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,755| 48125.703| 204.881|  36,467|
| |Leavenworth County|     8| 97.850| N/A| 1,425| 17429.487| N/A|  81,758|
| |Coffey County|     8| 978.115| N/A|    67|  8191.710| N/A|   8,179|
| |Ford County|     8| 237.961| N/A| 2,042| 60739.463| N/A|  33,619|
| |Phillips County|     8| 1528.468| N/A|    50|  9552.923| N/A|   5,234|
| |Riley County|     5| 67.356| N/A|   452|  6089.018| N/A|  74,232|
| |Montgomery County|     5| 157.089| N/A|   162|  5089.698| N/A|  31,829|
| |Saline County|     5| 92.210| N/A|   343|  6325.612| N/A|  54,224|
| |Douglas County|     4| 32.717| N/A|   684|  5594.680| N/A| 122,259|
| |Seward County|     4| 186.672| N/A| 1,204| 56188.165| N/A|  21,428|
| |Sumner County|     3| 131.372| N/A|    98|  4291.470| N/A|  22,836|
| |Barton County|     3| 116.374| N/A|   126|  4887.699| N/A|  25,779|
| |Clay County|     2| 249.938| N/A|    18|  2249.438| N/A|   8,002|
| |Cowley County|     2| 57.293| N/A|   160|  4583.477| N/A|  34,908|
| |Geary County|     2| 63.151| N/A|   130|  4104.831| N/A|  31,670|
| |Grant County|     2| 279.720| N/A|    97| 13566.434| N/A|   7,150|
| |Morton County|     2| 773.096| N/A|     9|  3478.933| N/A|   2,587|
| |Dickinson County|     1| 54.154| N/A|    43|  2328.604| N/A|  18,466|
| |Franklin County|     1| 39.148| N/A|   155|  6067.961| N/A|  25,544|
| |Trego County|     1| 356.761| N/A|     5|  1783.803| N/A|   2,803|
| |Stanton County|     1| 498.504| N/A|    16|  7976.072| N/A|   2,006|
| |Reno County|     1| 16.130| N/A|   232|  3742.056| N/A|  61,998|
| |Crawford County|     1| 25.761| N/A|   377|  9711.989| N/A|  38,818|
| |Ellis County|     1| 35.023| N/A|   133|  4658.004| N/A|  28,553|
| |Nemaha County|     1| 97.742| N/A|    48|  4691.623| N/A|  10,231|
| |McPherson County|     1| 35.036| N/A|   130|  4554.691| N/A|  28,542|
| |Kearny County|     1| 260.552| N/A|    57| 14851.485| N/A|   3,838|
| |Jackson County|     1| 75.924| N/A|   145| 11009.035| N/A|  13,171|
| |Clark County|     1| 501.505| N/A|    43| 21564.694| N/A|   1,994|
| |Harvey County|     1| 29.045| N/A|   169|  4908.653| N/A|  34,429|
| |Marion County|     1| 84.147| N/A|    46|  3870.751| N/A|  11,884|
| |Bourbon County|     1| 68.804| N/A|    73|  5022.705| N/A|  14,534|
| |Butler County|     1| 14.945| N/A|   218|  3258.059| N/A|  66,911|
| |Cherokee County|     1| 50.153| N/A|    78|  3911.931| N/A|  19,939|
| |Pottawatomie County|     0|  0.000| N/A|   105|  4306.279| N/A|  24,383|
| |Ottawa County|     0|  0.000| N/A|    30|  5259.467| N/A|   5,704|
| |Rush County|     0|  0.000| N/A|     6|  1976.285| N/A|   3,036|
| |Rooks County|     0|  0.000| N/A|    16|  3252.033| N/A|   4,920|
| |Rice County|     0|  0.000| N/A|    30|  3145.643| N/A|   9,537|
| |Republic County|     0|  0.000| N/A|    32|  6902.502| N/A|   4,636|
| |Rawlins County|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Pratt County|     0|  0.000| N/A|    33|  3601.048| N/A|   9,164|
| |Pawnee County|     0|  0.000| N/A|     7|  1091.363| N/A|   6,414|
| |Osborne County|     0|  0.000| N/A|     4|  1169.249| N/A|   3,421|
| |Scott County|     0|  0.000| N/A|    28|  5805.515| N/A|   4,823|
| |Osage County|     0|  0.000| N/A|    38|  2382.595| N/A|  15,949|
| |Norton County|     0|  0.000| N/A|    23|  4290.244| N/A|   5,361|
| |Ness County|     0|  0.000| N/A|     6|  2181.818| N/A|   2,750|
| |Neosho County|     0|  0.000| N/A|    53|  3311.051| N/A|  16,007|
| |Morris County|     0|  0.000| N/A|     9|  1601.423| N/A|   5,620|
| |Mitchell County|     0|  0.000| N/A|    27|  4515.805| N/A|   5,979|
| |Miami County|     0|  0.000| N/A|   120|  3504.980| N/A|  34,237|
| |Meade County|     0|  0.000| N/A|    40|  9918.175| N/A|   4,033|
| |Russell County|     0|  0.000| N/A|    13|  1896.149| N/A|   6,856|
| |Sheridan County|     0|  0.000| N/A|     7|  2776.676| N/A|   2,521|
| |Woodson County|     0|  0.000| N/A|    11|  3505.417| N/A|   3,138|
| |Comanche County|     0|  0.000| N/A|     3|  1764.706| N/A|   1,700|
| |Anderson County|     0|  0.000| N/A|    29|  3690.506| N/A|   7,858|
| |Lincoln County|     0|  0.000| N/A|     6|  2025.658| N/A|   2,962|
| |Decatur County|     0|  0.000| N/A|     5|  1768.659| N/A|   2,827|
| |Barber County|     0|  0.000| N/A|     4|   903.546| N/A|   4,427|
| |Doniphan County|     0|  0.000| N/A|    46|  6052.632| N/A|   7,600|
| |Edwards County|     0|  0.000| N/A|    10|  3573.981| N/A|   2,798|
| |Lane County|     0|  0.000| N/A|     5|  3257.329| N/A|   1,535|
| |Labette County|     0|  0.000| N/A|   118|  6014.884| N/A|  19,618|
| |Kiowa County|     0|  0.000| N/A|     6|  2424.242| N/A|   2,475|
| |Kingman County|     0|  0.000| N/A|    10|  1398.210| N/A|   7,152|
| |Jewell County|     0|  0.000| N/A|    10|  3473.428| N/A|   2,879|
| |Jefferson County|     0|  0.000| N/A|    70|  3675.891| N/A|  19,043|
| |Hodgeman County|     0|  0.000| N/A|    11|  6131.550| N/A|   1,794|
| |Haskell County|     0|  0.000| N/A|    44| 11088.710| N/A|   3,968|
| |Harper County|     0|  0.000| N/A|     9|  1655.629| N/A|   5,436|
| |Atchison County|     0|  0.000| N/A|    62|  3857.401| N/A|  16,073|
| |Brown County|     0|  0.000| N/A|    32|  3345.880| N/A|   9,564|
| |Greenwood County|     0|  0.000| N/A|    19|  3176.195| N/A|   5,982|
| |Wallace County|     0|  0.000| N/A|     0|     0.000| N/A|   1,518|
| |Wilson County|     0|  0.000| N/A|     8|   938.416| N/A|   8,525|
| |Sherman County|     0|  0.000| N/A|    15|  2535.068| N/A|   5,917|
| |Wichita County|     0|  0.000| N/A|     4|  1887.683| N/A|   2,119|
| |Washington County|     0|  0.000| N/A|     2|   369.959| N/A|   5,406|
| |Wabaunsee County|     0|  0.000| N/A|    39|  5626.894| N/A|   6,931|
| |Chase County|     0|  0.000| N/A|    39| 14728.097| N/A|   2,648|
| |Thomas County|     0|  0.000| N/A|    33|  4243.281| N/A|   7,777|
| |Stevens County|     0|  0.000| N/A|    44|  8021.878| N/A|   5,485|
| |Stafford County|     0|  0.000| N/A|     3|   721.848| N/A|   4,156|
| |Smith County|     0|  0.000| N/A|     3|   837.287| N/A|   3,583|
| |Marshall County|     0|  0.000| N/A|     9|   927.166| N/A|   9,707|
| |Logan County|     0|  0.000| N/A|     2|   715.820| N/A|   2,794|
| |Linn County|     0|  0.000| N/A|    35|  3607.132| N/A|   9,703|
| |Allen County|     0|  0.000| N/A|    15|  1212.709| N/A|  12,369|
| |Cloud County|     0|  0.000| N/A|    30|  3414.523| N/A|   8,786|
| |Cheyenne County|     0|  0.000| N/A|     2|   752.729| N/A|   2,657|
| |Chautauqua County|     0|  0.000| N/A|     5|  1538.462| N/A|   3,250|
| |Hamilton County|     0|  0.000| N/A|    37| 14572.666| N/A|   2,539|
| |Greeley County|     0|  0.000| N/A|     3|  2435.065| N/A|   1,232|
| |Gray County|     0|  0.000| N/A|    71| 11857.047| N/A|   5,988|
| |Graham County|     0|  0.000| N/A|    16|  6446.414| N/A|   2,482|
| |Gove County|     0|  0.000| N/A|     6|  2276.176| N/A|   2,636|
| |Ellsworth County|     0|  0.000| N/A|    18|  2949.853| N/A|   6,102|
| |Elk County|     0|  0.000| N/A|     1|   395.257| N/A|   2,530|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   333| 78.952| N/A|19,699|  4670.514| N/A|4,217,737|
| |Multnomah County|    93| 114.412|  0.521| 4,553|  5601.245| 68.893| 812,855|
| |Marion County|    68| 195.505|  1.132| 2,713|  7800.056| 81.316| 347,818|
| |Clackamas County|    37| 88.477|  1.267| 1,443|  3450.609| 52.608| 418,187|
| |Umatilla County|    24| 307.890|  0.000| 2,122| 27222.579| 661.917|  77,950|
| |Washington County|    23| 38.232|  0.000| 2,877|  4782.311| 51.485| 601,592|
| |Malheur County|    12| 392.529| 32.420|   708| 23159.203| 537.795|  30,571|
| |Yamhill County|    12| 112.045|  9.337|   399|  3725.490| 182.831| 107,100|
| |Polk County|    12| 139.397|  0.000|   300|  3484.928| 46.466|  86,085|
| |Linn County|    10| 77.072|  0.000|   255|  1965.333| 26.975| 129,749|
| |Lincoln County|     9| 180.137| N/A|   395|  7906.009| N/A|  49,962|
| |Deschutes County|     8| 40.467| N/A|   548|  2771.989| N/A| 197,692|
| |Benton County|     6| 64.479| N/A|   160|  1719.450| N/A|  93,053|
| |Jefferson County|     3| 121.664| N/A|   324| 13139.752| N/A|  24,658|
| |Lane County|     3|  7.852| N/A|   535|  1400.278| N/A| 382,067|
| |Wasco County|     3| 112.435| N/A|   171|  6408.815| N/A|  26,682|
| |Union County|     2| 74.530| N/A|   392| 14607.788| N/A|  26,835|
| |Morrow County|     2| 172.369| N/A|   316| 27234.336| N/A|  11,603|
| |Crook County|     1| 40.977| N/A|    43|  1762.006| N/A|  24,404|
| |Josephine County|     1| 11.430| N/A|   107|  1223.039| N/A|  87,487|
| |Jackson County|     1|  4.526| N/A|   411|  1860.200| N/A| 220,944|
| |Douglas County|     1|  9.011| N/A|   139|  1252.478| N/A| 110,980|
| |Klamath County|     1| 14.655| N/A|   198|  2901.609| N/A|  68,238|
| |Wallowa County|     1| 138.735| N/A|    19|  2635.960| N/A|   7,208|
| |Harney County|     0|  0.000| N/A|    10|  1352.631| N/A|   7,393|
| |Gilliam County|     0|  0.000| N/A|     4|  2092.050| N/A|   1,912|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|   1,332|
| |Tillamook County|     0|  0.000| N/A|    32|  1183.607| N/A|  27,036|
| |Sherman County|     0|  0.000| N/A|    14|  7865.169| N/A|   1,780|
| |Lake County|     0|  0.000| N/A|    32|  4066.590| N/A|   7,869|
| |Hood River County|     0|  0.000| N/A|   174|  7441.622| N/A|  23,382|
| |Grant County|     0|  0.000| N/A|     2|   277.816| N/A|   7,199|
| |Curry County|     0|  0.000| N/A|    14|   610.687| N/A|  22,925|
| |Coos County|     0|  0.000| N/A|    88|  1364.616| N/A|  64,487|
| |Columbia County|     0|  0.000| N/A|    84|  1604.462| N/A|  52,354|
| |Clatsop County|     0|  0.000| N/A|    82|  2038.584| N/A|  40,224|
| |Baker County|     0|  0.000| N/A|    35|  2170.677| N/A|  16,124|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   332| 171.629| N/A|27,027| 13971.716| N/A|1,934,408|
| |Douglas County|   131| 229.291|  0.000|10,719| 18761.585| 214.893| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,721| 28050.788| 67.541|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,904| 95076.401| 61.878|  20,026|
| |Lancaster County|    15| 47.009|  0.000| 3,163|  9912.564| 113.333| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    96| 10296.010| 17.373|   9,324|
| |Adams County|    11| 350.732|  0.000|   346| 11032.108| 63.769|  31,363|
| |Sarpy County|     9| 48.078| N/A| 2,101| 11223.530| N/A| 187,196|
| |Dawson County|     9| 381.437| N/A|   950| 40262.768| N/A|  23,595|
| |Dodge County|     8| 218.788| N/A|   781| 21359.223| N/A|  36,565|
| |Scotts Bluff County|     6| 168.454| N/A|   291|  8170.026| N/A|  35,618|
| |Madison County|     5| 142.454| N/A|   424| 12080.116| N/A|  35,099|
| |Howard County|     4| 620.636| N/A|    55|  8533.747| N/A|   6,445|
| |Thurston County|     4| 553.710| N/A|   203| 28100.775| N/A|   7,224|
| |Gage County|     4| 185.934| N/A|    82|  3811.649| N/A|  21,513|
| |Colfax County|     4| 373.518| N/A|   695| 64898.683| N/A|  10,709|
| |Custer County|     4| 371.161| N/A|    43|  3989.979| N/A|  10,777|
| |Platte County|     3| 89.633| N/A|   769| 22975.799| N/A|  33,470|
| |Dixon County|     2| 354.862| N/A|    57| 10113.556| N/A|   5,636|
| |Lincoln County|     2| 57.284| N/A|    93|  2663.688| N/A|  34,914|
| |Saline County|     2| 140.607| N/A|   586| 41197.975| N/A|  14,224|
| |Saunders County|     2| 92.687| N/A|   142|  6580.777| N/A|  21,578|
| |Fillmore County|     1| 183.083| N/A|    24|  4393.995| N/A|   5,462|
| |Washington County|     1| 48.242| N/A|   108|  5210.092| N/A|  20,729|
| |Furnas County|     1| 213.858| N/A|    15|  3207.870| N/A|   4,676|
| |Cass County|     1| 38.098| N/A|   160|  6095.703| N/A|  26,248|
| |Buffalo County|     1| 20.137| N/A|   360|  7249.441| N/A|  49,659|
| |Antelope County|     1| 158.781| N/A|    19|  3016.831| N/A|   6,298|
| |Perkins County|     1| 345.901| N/A|    17|  5880.318| N/A|   2,891|
| |Seward County|     1| 57.857| N/A|   104|  6017.126| N/A|  17,284|
| |Richardson County|     1| 127.146| N/A|    20|  2542.912| N/A|   7,865|
| |Jefferson County|     0|  0.000| N/A|    14|  1986.943| N/A|   7,046|
| |Morrill County|     0|  0.000| N/A|    58| 12494.614| N/A|   4,642|
| |Merrick County|     0|  0.000| N/A|    55|  7092.199| N/A|   7,755|
| |McPherson County|     0|  0.000| N/A|     4|  8097.166| N/A|     494|
| |Loup County|     0|  0.000| N/A|     0|     0.000| N/A|     664|
| |Knox County|     0|  0.000| N/A|    32|  3840.614| N/A|   8,332|
| |Phelps County|     0|  0.000| N/A|    37|  4095.639| N/A|   9,034|
| |Kimball County|     0|  0.000| N/A|    15|  4129.956| N/A|   3,632|
| |Keya Paha County|     0|  0.000| N/A|     0|     0.000| N/A|     806|
| |Keith County|     0|  0.000| N/A|    19|  2364.949| N/A|   8,034|
| |Kearney County|     0|  0.000| N/A|    34|  5234.796| N/A|   6,495|
| |Johnson County|     0|  0.000| N/A|    13|  2563.597| N/A|   5,071|
| |Hooker County|     0|  0.000| N/A|     4|  5865.103| N/A|     682|
| |Nemaha County|     0|  0.000| N/A|    21|  3012.048| N/A|   6,972|
| |Holt County|     0|  0.000| N/A|    11|  1092.679| N/A|  10,067|
| |Pawnee County|     0|  0.000| N/A|     9|  3444.317| N/A|   2,613|
| |Pierce County|     0|  0.000| N/A|    17|  2378.288| N/A|   7,148|
| |Wayne County|     0|  0.000| N/A|    37|  3942.461| N/A|   9,385|
| |York County|     0|  0.000| N/A|    73|  5336.647| N/A|  13,679|
| |Nance County|     0|  0.000| N/A|     8|  2273.373| N/A|   3,519|
| |Nuckolls County|     0|  0.000| N/A|     5|  1205.400| N/A|   4,148|
| |Webster County|     0|  0.000| N/A|     9|  2581.015| N/A|   3,487|
| |Otoe County|     0|  0.000| N/A|    43|  2685.486| N/A|  16,012|
| |Logan County|     0|  0.000| N/A|     0|     0.000| N/A|     748|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|     783|
| |Valley County|     0|  0.000| N/A|    10|  2405.002| N/A|   4,158|
| |Franklin County|     0|  0.000| N/A|     9|  3021.148| N/A|   2,979|
| |Boone County|     0|  0.000| N/A|     7|  1348.228| N/A|   5,192|
| |Box Butte County|     0|  0.000| N/A|    11|  1020.124| N/A|  10,783|
| |Boyd County|     0|  0.000| N/A|     1|   521.105| N/A|   1,919|
| |Brown County|     0|  0.000| N/A|     0|     0.000| N/A|   2,955|
| |Grant County|     0|  0.000| N/A|     0|     0.000| N/A|     623|
| |Gosper County|     0|  0.000| N/A|    19|  9547.739| N/A|   1,990|
| |Garfield County|     0|  0.000| N/A|     3|  1523.616| N/A|   1,969|
| |Garden County|     0|  0.000| N/A|     4|  2177.463| N/A|   1,837|
| |Frontier County|     0|  0.000| N/A|     3|  1141.987| N/A|   2,627|
| |Dundy County|     0|  0.000| N/A|     1|   590.667| N/A|   1,693|
| |Deuel County|     0|  0.000| N/A|     1|   557.414| N/A|   1,794|
| |Dawes County|     0|  0.000| N/A|     8|   931.424| N/A|   8,589|
| |Cuming County|     0|  0.000| N/A|    63|  7121.863| N/A|   8,846|
| |Clay County|     0|  0.000| N/A|    48|  7738.191| N/A|   6,203|
| |Cheyenne County|     0|  0.000| N/A|    26|  2918.070| N/A|   8,910|
| |Cherry County|     0|  0.000| N/A|     4|   703.111| N/A|   5,689|
| |Chase County|     0|  0.000| N/A|     6|  1529.052| N/A|   3,924|
| |Cedar County|     0|  0.000| N/A|    21|  2499.405| N/A|   8,402|
| |Butler County|     0|  0.000| N/A|    57|  7110.778| N/A|   8,016|
| |Burt County|     0|  0.000| N/A|    25|  3870.568| N/A|   6,459|
| |Polk County|     0|  0.000| N/A|    24|  4603.875| N/A|   5,213|
| |Thomas County|     0|  0.000| N/A|     1|  1385.042| N/A|     722|
| |Thayer County|     0|  0.000| N/A|    26|  5196.882| N/A|   5,003|
| |Stanton County|     0|  0.000| N/A|    28|  4729.730| N/A|   5,920|
| |Sioux County|     0|  0.000| N/A|     5|  4288.165| N/A|   1,166|
| |Sherman County|     0|  0.000| N/A|    10|  3332.223| N/A|   3,001|
| |Sheridan County|     0|  0.000| N/A|     9|  1715.593| N/A|   5,246|
| |Rock County|     0|  0.000| N/A|     2|  1473.839| N/A|   1,357|
| |Red Willow County|     0|  0.000| N/A|    16|  1491.981| N/A|  10,724|
| |Hitchcock County|     0|  0.000| N/A|     1|   362.056| N/A|   2,762|
| |Hayes County|     0|  0.000| N/A|     0|     0.000| N/A|     922|
| |Harlan County|     0|  0.000| N/A|     1|   295.858| N/A|   3,380|
| |Blaine County|     0|  0.000| N/A|     0|     0.000| N/A|     465|
| |Banner County|     0|  0.000| N/A|     2|  2684.564| N/A|     745|
| |Arthur County|     0|  0.000| N/A|     0|     0.000| N/A|     463|
| |Greeley County|     0|  0.000| N/A|     9|  3820.034| N/A|   2,356|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   264| 82.347| N/A|33,328| 10395.645| N/A|3,205,958|
| |Salt Lake County|   184| 158.561|  2.920|19,683| 16961.714| 122.961|1,160,437|
| |Utah County|    35| 55.011|  0.000| 8,165| 12833.308| 177.971| 636,235|
| |San Juan County|    24| 1567.808|  0.000|   630| 41154.952| 208.414|  15,308|
| |Davis County|    16| 45.009|  2.813| 3,059|  8605.242| 92.832| 355,481|
| |Wasatch County|     4| 117.333| N/A|   536| 15722.625| N/A|  34,091|
| |Summit County|     1| 23.728| N/A|   698| 16561.870| N/A|  42,145|
| |Tooele County|     0|  0.000| N/A|   557|  7708.382| N/A|  72,259|
| |Carbon County|     0|  0.000| N/A|     0|     0.000| N/A|  20,463|
| |Millard County|     0|  0.000| N/A|     0|     0.000| N/A|  13,188|
| |Morgan County|     0|  0.000| N/A|     0|     0.000| N/A|  12,124|
| |Cache County|     0|  0.000| N/A|     0|     0.000| N/A| 128,289|
| |Duchesne County|     0|  0.000| N/A|     0|     0.000| N/A|  19,938|
| |Box Elder County|     0|  0.000| N/A|     0|     0.000| N/A|  56,046|
| |Emery County|     0|  0.000| N/A|     0|     0.000| N/A|  10,012|
| |Kane County|     0|  0.000| N/A|     0|     0.000| N/A|   7,886|
| |Garfield County|     0|  0.000| N/A|     0|     0.000| N/A|   5,051|
| |Grand County|     0|  0.000| N/A|     0|     0.000| N/A|   9,754|
| |Iron County|     0|  0.000| N/A|     0|     0.000| N/A|  54,839|
| |Beaver County|     0|  0.000| N/A|     0|     0.000| N/A|   6,710|
| |Juab County|     0|  0.000| N/A|     0|     0.000| N/A|  12,017|
| |Washington County|     0|  0.000| N/A|     0|     0.000| N/A| 177,556|
| |Wayne County|     0|  0.000| N/A|     0|     0.000| N/A|   2,711|
| |Uintah County|     0|  0.000| N/A|     0|     0.000| N/A|  35,734|
| |Weber County|     0|  0.000| N/A|     0|     0.000| N/A| 260,213|
| |Piute County|     0|  0.000| N/A|     0|     0.000| N/A|   1,479|
| |Daggett County|     0|  0.000| N/A|     0|     0.000| N/A|     950|
| |Rich County|     0|  0.000| N/A|     0|     0.000| N/A|   2,483|
| |Sanpete County|     0|  0.000| N/A|     0|     0.000| N/A|  30,939|
| |Sevier County|     0|  0.000| N/A|     0|     0.000| N/A|  21,620|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   210| 117.511| N/A|22,230| 12439.391| N/A|1,787,065|
| |Ada County|    66| 137.047|  3.517| 8,280| 17193.155| 286.553| 481,587|
| |Canyon County|    42| 182.729|  9.183| 5,111| 22236.338| 499.060| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,257| 14468.565| 198.509|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   138|  3415.165| 83.461|  40,408|
| |Kootenai County|    14| 84.492|  2.510| 1,633|  9855.338| 149.140| 165,697|
| |Jerome County|     6| 245.781| N/A|   439| 17982.959| N/A|  24,412|
| |Blaine County|     6| 260.632| N/A|   571| 24803.440| N/A|  23,021|
| |Washington County|     3| 294.291| N/A|   194| 19030.802| N/A|  10,194|
| |Elmore County|     3| 109.047| N/A|   201|  7306.168| N/A|  27,511|
| |Bonneville County|     2| 16.798| N/A|   808|  6786.380| N/A| 119,062|
| |Bannock County|     2| 22.777| N/A|   329|  3746.811| N/A|  87,808|
| |Bingham County|     2| 42.725| N/A|   207|  4422.038| N/A|  46,811|
| |Owyhee County|     2| 169.162| N/A|   239| 20214.835| N/A|  11,823|
| |Payette County|     2| 83.504| N/A|   348| 14529.665| N/A|  23,951|
| |Minidoka County|     2| 95.062| N/A|   453| 21531.442| N/A|  21,039|
| |Shoshone County|     2| 155.255| N/A|    78|  6054.960| N/A|  12,882|
| |Gooding County|     1| 65.880| N/A|   144|  9486.791| N/A|  15,179|
| |Cassia County|     1| 41.615| N/A|   491| 20432.792| N/A|  24,030|
| |Boise County|     1| 127.698| N/A|    42|  5363.300| N/A|   7,831|
| |Jefferson County|     1| 33.477| N/A|   158|  5289.411| N/A|  29,871|
| |Valley County|     1| 87.781| N/A|    50|  4389.045| N/A|  11,392|
| |Teton County|     0|  0.000| N/A|    62|  5106.243| N/A|  12,142|
| |Caribou County|     0|  0.000| N/A|    23|  3214.535| N/A|   7,155|
| |Clearwater County|     0|  0.000| N/A|    15|  1713.111| N/A|   8,756|
| |Lewis County|     0|  0.000| N/A|     1|   260.552| N/A|   3,838|
| |Lemhi County|     0|  0.000| N/A|    12|  1494.955| N/A|   8,027|
| |Latah County|     0|  0.000| N/A|    88|  2194.076| N/A|  40,108|
| |Idaho County|     0|  0.000| N/A|    30|  1799.964| N/A|  16,667|
| |Gem County|     0|  0.000| N/A|   161|  8889.134| N/A|  18,112|
| |Fremont County|     0|  0.000| N/A|    68|  5191.236| N/A|  13,099|
| |Franklin County|     0|  0.000| N/A|    50|  3603.344| N/A|  13,876|
| |Custer County|     0|  0.000| N/A|     7|  1622.248| N/A|   4,315|
| |Clark County|     0|  0.000| N/A|     5|  5917.160| N/A|     845|
| |Camas County|     0|  0.000| N/A|     1|   904.159| N/A|   1,106|
| |Butte County|     0|  0.000| N/A|     0|     0.000| N/A|   2,597|
| |Boundary County|     0|  0.000| N/A|    34|  2776.644| N/A|  12,245|
| |Bonner County|     0|  0.000| N/A|   156|  3410.656| N/A|  45,739|
| |Benewah County|     0|  0.000| N/A|    58|  6237.901| N/A|   9,298|
| |Bear Lake County|     0|  0.000| N/A|     9|  1469.388| N/A|   6,125|
| |Adams County|     0|  0.000| N/A|    18|  4191.896| N/A|   4,294|
| |Lincoln County|     0|  0.000| N/A|    53|  9877.003| N/A|   5,366|
| |Madison County|     0|  0.000| N/A|   142|  3558.273| N/A|  39,907|
| |Oneida County|     0|  0.000| N/A|    13|  2869.124| N/A|   4,531|
| |Power County|     0|  0.000| N/A|    53|  6900.143| N/A|   7,681|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   136| 153.732| N/A| 9,079| 10262.711| N/A| 884,659|
| |Minnehaha County|    64| 331.376|  0.000| 4,258| 22046.869| 120.330| 193,134|
| |Pennington County|    29| 254.889|  0.000|   848|  7453.307| 26.368| 113,775|
| |Beadle County|     9| 487.726| N/A|   587| 31810.546| N/A|  18,453|
| |Todd County|     4| 393.043| N/A|    66|  6485.212| N/A|  10,177|
| |Union County|     4| 251.067| N/A|   201| 12616.119| N/A|  15,932|
| |Brown County|     3| 77.242| N/A|   412| 10607.894| N/A|  38,839|
| |Buffalo County|     3| 1529.052| N/A|   108| 55045.872| N/A|   1,962|
| |Yankton County|     2| 87.665| N/A|   103|  4514.772| N/A|  22,814|
| |Lyman County|     2| 528.961| N/A|    88| 23274.266| N/A|   3,781|
| |Lake County|     2| 156.287| N/A|    84|  6564.038| N/A|  12,797|
| |Lincoln County|     2| 32.718| N/A|   582|  9521.005| N/A|  61,128|
| |Hughes County|     2| 114.116| N/A|    84|  4792.879| N/A|  17,526|
| |Oglala Lakota County|     1| 70.537| N/A|   151| 10651.055| N/A|  14,177|
| |Roberts County|     1| 96.209| N/A|    71|  6830.864| N/A|  10,394|
| |Faulk County|     1| 434.972| N/A|    26| 11309.265| N/A|   2,299|
| |Meade County|     1| 35.296| N/A|    78|  2753.071| N/A|  28,332|
| |Brookings County|     1| 28.509| N/A|   121|  3449.554| N/A|  35,077|
| |Jackson County|     1| 299.043| N/A|    10|  2990.431| N/A|   3,344|
| |Jerauld County|     1| 496.771| N/A|    40| 19870.840| N/A|   2,013|
| |McCook County|     1| 179.019| N/A|    24|  4296.455| N/A|   5,586|
| |Codington County|     1| 35.703| N/A|   120|  4284.337| N/A|  28,009|
| |Butte County|     1| 95.886| N/A|    11|  1054.751| N/A|  10,429|
| |Dewey County|     0|  0.000| N/A|    63| 10692.464| N/A|   5,892|
| |Hutchinson County|     0|  0.000| N/A|    27|  3703.196| N/A|   7,291|
| |Deuel County|     0|  0.000| N/A|     9|  2068.490| N/A|   4,351|
| |Day County|     0|  0.000| N/A|    21|  3871.681| N/A|   5,424|
| |Davison County|     0|  0.000| N/A|    93|  4702.908| N/A|  19,775|
| |Custer County|     0|  0.000| N/A|    23|  2563.531| N/A|   8,972|
| |Corson County|     0|  0.000| N/A|    29|  7097.406| N/A|   4,086|
| |Clay County|     0|  0.000| N/A|   120|  8528.785| N/A|  14,070|
| |Clark County|     0|  0.000| N/A|    16|  4282.655| N/A|   3,736|
| |Charles Mix County|     0|  0.000| N/A|   100| 10761.946| N/A|   9,292|
| |Harding County|     0|  0.000| N/A|     0|     0.000| N/A|   1,298|
| |Hyde County|     0|  0.000| N/A|     3|  2305.919| N/A|   1,301|
| |Sanborn County|     0|  0.000| N/A|    13|  5546.075| N/A|   2,344|
| |Ziebach County|     0|  0.000| N/A|     8|  2902.758| N/A|   2,756|
| |Walworth County|     0|  0.000| N/A|    18|  3311.868| N/A|   5,435|
| |Turner County|     0|  0.000| N/A|    48|  5725.191| N/A|   8,384|
| |Tripp County|     0|  0.000| N/A|    20|  3675.795| N/A|   5,441|
| |Sully County|     0|  0.000| N/A|     1|   718.907| N/A|   1,391|
| |Stanley County|     0|  0.000| N/A|    14|  4519.045| N/A|   3,098|
| |Spink County|     0|  0.000| N/A|    22|  3450.439| N/A|   6,376|
| |Potter County|     0|  0.000| N/A|     1|   464.468| N/A|   2,153|
| |Jones County|     0|  0.000| N/A|     2|  2214.839| N/A|     903|
| |Perkins County|     0|  0.000| N/A|     6|  2094.241| N/A|   2,865|
| |Edmunds County|     0|  0.000| N/A|    13|  3395.142| N/A|   3,829|
| |Fall River County|     0|  0.000| N/A|    18|  2681.365| N/A|   6,713|
| |Grant County|     0|  0.000| N/A|    23|  3261.486| N/A|   7,052|
| |Gregory County|     0|  0.000| N/A|     7|  1672.640| N/A|   4,185|
| |Douglas County|     0|  0.000| N/A|    16|  5477.576| N/A|   2,921|
| |Hanson County|     0|  0.000| N/A|    21|  6081.668| N/A|   3,453|
| |Hand County|     0|  0.000| N/A|     7|  2193.670| N/A|   3,191|
| |Hamlin County|     0|  0.000| N/A|    14|  2271.252| N/A|   6,164|
| |Haakon County|     0|  0.000| N/A|     2|  1053.186| N/A|   1,899|
| |Miner County|     0|  0.000| N/A|    15|  6768.953| N/A|   2,216|
| |Moody County|     0|  0.000| N/A|    30|  4562.044| N/A|   6,576|
| |Mellette County|     0|  0.000| N/A|    24| 11644.833| N/A|   2,061|
| |Marshall County|     0|  0.000| N/A|     8|  1621.074| N/A|   4,935|
| |Aurora County|     0|  0.000| N/A|    37| 13449.655| N/A|   2,751|
| |McPherson County|     0|  0.000| N/A|     7|  2942.413| N/A|   2,379|
| |Lawrence County|     0|  0.000| N/A|    32|  1238.198| N/A|  25,844|
| |Kingsbury County|     0|  0.000| N/A|    14|  2834.582| N/A|   4,939|
| |Campbell County|     0|  0.000| N/A|     2|  1453.488| N/A|   1,376|
| |Brule County|     0|  0.000| N/A|    40|  7551.444| N/A|   5,297|
| |Bon Homme County|     0|  0.000| N/A|    13|  1883.785| N/A|   6,901|
| |Bennett County|     0|  0.000| N/A|     6|  1783.061| N/A|   3,365|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   124| 69.191| N/A| 7,059|  3938.851| N/A|1,792,147|
| |Kanawha County|    22| 123.509|  3.216|   851|  4777.571| 80.967| 178,124|
| |Jackson County|    19| 664.894|  0.000|   158|  5529.115| 18.544|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   661|  5546.651| 26.219| 119,171|
| |Wayne County|     9| 228.415| N/A|   191|  4847.470| N/A|  39,402|
| |Monongalia County|     5| 47.343| N/A|   929|  8796.349| N/A| 105,612|
| |Wood County|     5| 59.867| N/A|   240|  2873.632| N/A|  83,518|
| |Fayette County|     5| 117.908| N/A|   131|  3089.185| N/A|  42,406|
| |Jefferson County|     4| 69.996| N/A|   292|  5109.719| N/A|  57,146|
| |Preston County|     4| 119.646| N/A|   125|  3738.933| N/A|  33,432|
| |Ohio County|     4| 96.593| N/A|   260|  6278.525| N/A|  41,411|
| |Mineral County|     4| 148.876| N/A|   114|  4242.966| N/A|  26,868|
| |Greenbrier County|     3| 86.550| N/A|    87|  2509.953| N/A|  34,662|
| |Logan County|     3| 93.694| N/A|   157|  4903.339| N/A|  32,019|
| |Mercer County|     3| 51.057| N/A|   167|  2842.166| N/A|  58,758|
| |Mingo County|     3| 128.074| N/A|   144|  6147.541| N/A|  23,424|
| |Lewis County|     2| 125.731| N/A|    27|  1697.366| N/A|  15,907|
| |Marion County|     2| 35.668| N/A|   179|  3192.324| N/A|  56,072|
| |Cabell County|     2| 21.752| N/A|   350|  3806.624| N/A|  91,945|
| |Brooke County|     1| 45.581| N/A|    62|  2826.018| N/A|  21,939|
| |Harrison County|     1| 14.869| N/A|   199|  2958.844| N/A|  67,256|
| |Barbour County|     1| 60.824| N/A|    29|  1763.883| N/A|  16,441|
| |Wyoming County|     1| 49.034| N/A|    23|  1127.783| N/A|  20,394|
| |Raleigh County|     1| 13.631| N/A|   198|  2698.982| N/A|  73,361|
| |Clay County|     1| 117.536| N/A|    18|  2115.656| N/A|   8,508|
| |Grant County|     1| 86.445| N/A|    81|  7002.075| N/A|  11,568|
| |Hampshire County|     1| 43.150| N/A|    74|  3193.096| N/A|  23,175|
| |Roane County|     1| 73.057| N/A|    14|  1022.794| N/A|  13,688|
| |Taylor County|     1| 59.898| N/A|    53|  3174.603| N/A|  16,695|
| |Mason County|     1| 37.713| N/A|    50|  1885.654| N/A|  26,516|
| |Pendleton County|     1| 143.493| N/A|    41|  5883.197| N/A|   6,969|
| |Nicholas County|     1| 40.823| N/A|    33|  1347.159| N/A|  24,496|
| |Marshall County|     1| 32.754| N/A|   129|  4225.214| N/A|  30,531|
| |Monroe County|     0|  0.000| N/A|    19|  1431.262| N/A|  13,275|
| |Morgan County|     0|  0.000| N/A|    26|  1453.813| N/A|  17,884|
| |Summers County|     0|  0.000| N/A|     7|   556.749| N/A|  12,573|
| |Tucker County|     0|  0.000| N/A|    11|  1608.422| N/A|   6,839|
| |Randolph County|     0|  0.000| N/A|   207|  7213.800| N/A|  28,695|
| |Putnam County|     0|  0.000| N/A|   174|  3082.374| N/A|  56,450|
| |Ritchie County|     0|  0.000| N/A|     3|   314.005| N/A|   9,554|
| |Hancock County|     0|  0.000| N/A|   104|  3609.858| N/A|  28,810|
| |Gilmer County|     0|  0.000| N/A|    16|  2045.251| N/A|   7,823|
| |Doddridge County|     0|  0.000| N/A|     4|   473.485| N/A|   8,448|
| |Calhoun County|     0|  0.000| N/A|     6|   844.001| N/A|   7,109|
| |Braxton County|     0|  0.000| N/A|     8|   573.189| N/A|  13,957|
| |Tyler County|     0|  0.000| N/A|    12|  1396.811| N/A|   8,591|
| |McDowell County|     0|  0.000| N/A|    46|  2610.077| N/A|  17,624|
| |Wetzel County|     0|  0.000| N/A|    41|  2721.540| N/A|  15,065|
| |Wirt County|     0|  0.000| N/A|     6|  1030.751| N/A|   5,821|
| |Upshur County|     0|  0.000| N/A|    39|  1613.170| N/A|  24,176|
| |Webster County|     0|  0.000| N/A|     3|   369.731| N/A|   8,114|
| |Boone County|     0|  0.000| N/A|    88|  4101.226| N/A|  21,457|
| |Pleasants County|     0|  0.000| N/A|     8|  1072.386| N/A|   7,460|
| |Pocahontas County|     0|  0.000| N/A|    41|  4971.505| N/A|   8,247|
| |Hardy County|     0|  0.000| N/A|    54|  3919.861| N/A|  13,776|
| |Lincoln County|     0|  0.000| N/A|    69|  3380.861| N/A|  20,409|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   123| 91.503| N/A| 3,975|  2957.123| N/A|1,344,212|
| |Cumberland County|    68| 230.506|  0.000| 2,061|  6986.370| 15.254| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   660|  3178.563| 14.017| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   169|  1381.825|  7.876| 122,302|
| |Androscoggin County|     7| 64.649| N/A|   548|  5061.093| N/A| 108,277|
| |Penobscot County|     5| 32.863| N/A|   150|   985.882| N/A| 152,148|
| |Franklin County|     1| 33.114| N/A|    45|  1490.116| N/A|  30,199|
| |Hancock County|     1| 18.186| N/A|    34|   618.328| N/A|  54,987|
| |Somerset County|     1| 19.808| N/A|    34|   673.481| N/A|  50,484|
| |Aroostook County|     1| 14.913| N/A|    32|   477.220| N/A|  67,055|
| |Lincoln County|     1| 28.873| N/A|    34|   981.694| N/A|  34,634|
| |Knox County|     1| 25.143| N/A|    26|   653.726| N/A|  39,772|
| |Piscataquis County|     0|  0.000| N/A|     3|   178.731| N/A|  16,785|
| |Oxford County|     0|  0.000| N/A|    54|   931.436| N/A|  57,975|
| |Washington County|     0|  0.000| N/A|    12|   382.421| N/A|  31,379|
| |Sagadahoc County|     0|  0.000| N/A|    51|  1422.356| N/A|  35,856|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   107| 140.409| N/A| 6,915|  9074.065| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 2,938| 16149.690| 43.975| 181,923|
| |Burleigh County|     5| 52.287| N/A| 1,007| 10530.609| N/A|  95,626|
| |Grand Forks County|     5| 71.993| N/A|   642|  9243.927| N/A|  69,451|
| |Stark County|     3| 95.271| N/A|   221|  7018.324| N/A|  31,489|
| |Morton County|     3| 95.651| N/A|   292|  9310.037| N/A|  31,364|
| |Ramsey County|     2| 173.626| N/A|    60|  5208.785| N/A|  11,519|
| |Stutsman County|     2| 96.600| N/A|   121|  5844.281| N/A|  20,704|
| |Williams County|     2| 53.207| N/A|   244|  6491.261| N/A|  37,589|
| |Sioux County|     1| 236.407| N/A|    59| 13947.991| N/A|   4,230|
| |McKenzie County|     1| 66.560| N/A|    84|  5591.054| N/A|  15,024|
| |Mountrail County|     1| 94.832| N/A|   122| 11569.464| N/A|  10,545|
| |McIntosh County|     1| 400.481| N/A|    27| 10812.976| N/A|   2,497|
| |McHenry County|     1| 174.064| N/A|    15|  2610.966| N/A|   5,745|
| |Ward County|     1| 14.784| N/A|   195|  2882.867| N/A|  67,641|
| |Benson County|     1| 146.370| N/A|   127| 18588.993| N/A|   6,832|
| |Emmons County|     1| 308.547| N/A|    17|  5245.295| N/A|   3,241|
| |Griggs County|     1| 448.229| N/A|    30| 13446.885| N/A|   2,231|
| |Dunn County|     0|  0.000| N/A|    30|  6781.193| N/A|   4,424|
| |Eddy County|     0|  0.000| N/A|    15|  6558.811| N/A|   2,287|
| |Walsh County|     0|  0.000| N/A|    99|  9303.637| N/A|  10,641|
| |Foster County|     0|  0.000| N/A|    17|  5295.950| N/A|   3,210|
| |Divide County|     0|  0.000| N/A|     1|   441.696| N/A|   2,264|
| |Wells County|     0|  0.000| N/A|    19|  4955.660| N/A|   3,834|
| |Towner County|     0|  0.000| N/A|     5|  2284.148| N/A|   2,189|
| |LaMoure County|     0|  0.000| N/A|    15|  3707.365| N/A|   4,046|
| |Logan County|     0|  0.000| N/A|     6|  3243.243| N/A|   1,850|
| |Kidder County|     0|  0.000| N/A|    11|  4435.484| N/A|   2,480|
| |Hettinger County|     0|  0.000| N/A|     6|  2400.960| N/A|   2,499|
| |Grant County|     0|  0.000| N/A|     4|  1759.015| N/A|   2,274|
| |Golden Valley County|     0|  0.000| N/A|     4|  2271.437| N/A|   1,761|
| |Slope County|     0|  0.000| N/A|     3|  4000.000| N/A|     750|
| |Traill County|     0|  0.000| N/A|    47|  5848.681| N/A|   8,036|
| |Dickey County|     0|  0.000| N/A|    12|  2463.054| N/A|   4,872|
| |Mercer County|     0|  0.000| N/A|    23|  2809.332| N/A|   8,187|
| |Cavalier County|     0|  0.000| N/A|    31|  8240.298| N/A|   3,762|
| |Burke County|     0|  0.000| N/A|    23| 10874.704| N/A|   2,115|
| |Bowman County|     0|  0.000| N/A|     6|  1984.127| N/A|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000| N/A|     2|  2155.172| N/A|     928|
| |Barnes County|     0|  0.000| N/A|    35|  3360.538| N/A|  10,415|
| |Adams County|     0|  0.000| N/A|     2|   902.527| N/A|   2,216|
| |McLean County|     0|  0.000| N/A|    39|  4126.984| N/A|   9,450|
| |Steele County|     0|  0.000| N/A|    13|  6878.307| N/A|   1,890|
| |Nelson County|     0|  0.000| N/A|    19|  6599.514| N/A|   2,879|
| |Oliver County|     0|  0.000| N/A|     7|  3573.252| N/A|   1,959|
| |Sheridan County|     0|  0.000| N/A|     6|  4562.738| N/A|   1,315|
| |Sargent County|     0|  0.000| N/A|    11|  2821.960| N/A|   3,898|
| |Rolette County|     0|  0.000| N/A|    35|  2468.962| N/A|  14,176|
| |Richland County|     0|  0.000| N/A|    95|  5872.535| N/A|  16,177|
| |Renville County|     0|  0.000| N/A|     9|  3867.641| N/A|   2,327|
| |Ransom County|     0|  0.000| N/A|    26|  4982.752| N/A|   5,218|
| |Pierce County|     0|  0.000| N/A|    11|  2767.296| N/A|   3,975|
| |Pembina County|     0|  0.000| N/A|    27|  3970.004| N/A|   6,801|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    64| 59.881| N/A| 4,314|  4036.385| N/A|1,068,778|
| |Yellowstone County|    27| 167.390|  2.621| 1,118|  6931.184| 100.631| 161,300|
| |Big Horn County|    11| 825.888| 64.143|   363| 27254.298| 938.509|  13,319|
| |Toole County|     6| 1266.892| N/A|    35|  7390.203| N/A|   4,736|
| |Gallatin County|     3| 26.216| N/A|   874|  7637.590| N/A| 114,434|
| |Lincoln County|     2| 100.100| N/A|    71|  3553.554| N/A|  19,980|
| |Custer County|     2| 175.408| N/A|    53|  4648.307| N/A|  11,402|
| |Cascade County|     2| 24.580| N/A|   154|  1892.682| N/A|  81,366|
| |Flathead County|     2| 19.267| N/A|   272|  2620.272| N/A| 103,806|
| |Sweet Grass County|     1| 267.594| N/A|     4|  1070.377| N/A|   3,737|
| |Lewis and Clark County|     1| 14.403| N/A|   145|  2088.374| N/A|  69,432|
| |Lake County|     1| 32.832| N/A|   169|  5548.624| N/A|  30,458|
| |Glacier County|     1| 72.711| N/A|    58|  4217.262| N/A|  13,753|
| |Richland County|     1| 92.567| N/A|    46|  4258.076| N/A|  10,803|
| |Rosebud County|     1| 111.894| N/A|    23|  2573.571| N/A|   8,937|
| |Madison County|     1| 116.279| N/A|    78|  9069.767| N/A|   8,600|
| |Missoula County|     1|  8.361| N/A|   267|  2232.441| N/A| 119,600|
| |Ravalli County|     1| 22.828| N/A|    74|  1689.266| N/A|  43,806|
| |Petroleum County|     0|  0.000| N/A|     0|     0.000| N/A|     487|
| |Mineral County|     0|  0.000| N/A|     0|     0.000| N/A|   4,397|
| |Park County|     0|  0.000| N/A|    52|  3131.398| N/A|  16,606|
| |Pondera County|     0|  0.000| N/A|     9|  1522.585| N/A|   5,911|
| |Phillips County|     0|  0.000| N/A|     0|     0.000| N/A|   3,954|
| |Powell County|     0|  0.000| N/A|     2|   290.276| N/A|   6,890|
| |Powder River County|     0|  0.000| N/A|     1|   594.530| N/A|   1,682|
| |Prairie County|     0|  0.000| N/A|     1|   928.505| N/A|   1,077|
| |Stillwater County|     0|  0.000| N/A|    20|  2074.258| N/A|   9,642|
| |Roosevelt County|     0|  0.000| N/A|    20|  1817.521| N/A|  11,004|
| |Wibaux County|     0|  0.000| N/A|     3|  3095.975| N/A|     969|
| |Wheatland County|     0|  0.000| N/A|     3|  1411.101| N/A|   2,126|
| |Valley County|     0|  0.000| N/A|    13|  1757.707| N/A|   7,396|
| |Treasure County|     0|  0.000| N/A|     2|  2873.563| N/A|     696|
| |Teton County|     0|  0.000| N/A|    15|  2440.215| N/A|   6,147|
| |Silver Bow County|     0|  0.000| N/A|    67|  1918.946| N/A|  34,915|
| |Sheridan County|     0|  0.000| N/A|     3|   906.618| N/A|   3,309|
| |Sanders County|     0|  0.000| N/A|     9|   743.003| N/A|  12,113|
| |Dawson County|     0|  0.000| N/A|    16|  1857.657| N/A|   8,613|
| |Daniels County|     0|  0.000| N/A|     3|  1775.148| N/A|   1,690|
| |Chouteau County|     0|  0.000| N/A|     7|  1242.236| N/A|   5,635|
| |Carter County|     0|  0.000| N/A|     0|     0.000| N/A|   1,252|
| |Carbon County|     0|  0.000| N/A|    60|  5594.406| N/A|  10,725|
| |Broadwater County|     0|  0.000| N/A|    11|  1763.668| N/A|   6,237|
| |Fallon County|     0|  0.000| N/A|     2|   702.741| N/A|   2,846|
| |Deer Lodge County|     0|  0.000| N/A|    22|  2407.002| N/A|   9,140|
| |Blaine County|     0|  0.000| N/A|     9|  1347.104| N/A|   6,681|
| |Fergus County|     0|  0.000| N/A|     7|   633.484| N/A|  11,050|
| |Beaverhead County|     0|  0.000| N/A|    50|  5289.326| N/A|   9,453|
| |Musselshell County|     0|  0.000| N/A|     2|   431.686| N/A|   4,633|
| |Garfield County|     0|  0.000| N/A|    12|  9538.951| N/A|   1,258|
| |Meagher County|     0|  0.000| N/A|     4|  2148.228| N/A|   1,862|
| |McCone County|     0|  0.000| N/A|     2|  1201.923| N/A|   1,664|
| |Liberty County|     0|  0.000| N/A|     1|   427.899| N/A|   2,337|
| |Judith Basin County|     0|  0.000| N/A|     3|  1494.768| N/A|   2,007|
| |Jefferson County|     0|  0.000| N/A|    27|  2209.312| N/A|  12,221|
| |Hill County|     0|  0.000| N/A|    41|  2487.260| N/A|  16,484|
| |Granite County|     0|  0.000| N/A|     8|  2367.564| N/A|   3,379|
| |Golden Valley County|     0|  0.000| N/A|     3|  3654.080| N/A|     821|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    57| 91.348| N/A| 1,423|  2280.489| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   723|  4414.620| 10.645| 163,774|
| |Franklin County|     6| 121.453| N/A|   117|  2368.325| N/A|  49,402|
| |Windham County|     3| 71.053| N/A|   101|  2392.118| N/A|  42,222|
| |Windsor County|     2| 36.323| N/A|    71|  1289.456| N/A|  55,062|
| |Washington County|     2| 34.241| N/A|    50|   856.032| N/A|  58,409|
| |Addison County|     2| 54.382| N/A|    73|  1984.936| N/A|  36,777|
| |Rutland County|     1| 17.185| N/A|    89|  1529.446| N/A|  58,191|
| |Lamoille County|     1| 39.429| N/A|    42|  1656.021| N/A|  25,362|
| |Bennington County|     1| 28.193| N/A|    84|  2368.198| N/A|  35,470|
| |Caledonia County|     0|  0.000| N/A|    26|   866.869| N/A|  29,993|
| |Essex County|     0|  0.000| N/A|     4|   649.035| N/A|   6,163|
| |Grand Isle County|     0|  0.000| N/A|    13|  1796.821| N/A|   7,235|
| |Orleans County|     0|  0.000| N/A|    14|   517.809| N/A|  27,037|
| |Orange County|     0|  0.000| N/A|    16|   553.787| N/A|  28,892|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    26| 18.363| N/A| 2,568|  1813.723| N/A|1,415,872|
| |Honolulu County|    20| 20.522| N/A| 2,221|  2278.970| N/A| 974,563|
| |Maui County|     6| 35.839| N/A|   178|  1063.213| N/A| 167,417|
| |Kauai County|     0|  0.000| N/A|    47|   650.132| N/A|  72,293|
| |Kalawao County|     0|  0.000| N/A|     0|     0.000| N/A|      86|
| |Hawaii County|     0|  0.000| N/A|   122|   605.420| N/A| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 2,884|  4983.076| N/A| 578,759|
| |Johnson County|     1| 118.413| N/A|    22|  2605.092| N/A|   8,445|
| |Carbon County|     0|  0.000| N/A|    84|  5675.676| N/A|  14,800|
| |Lincoln County|     0|  0.000| N/A|    93|  4689.864| N/A|  19,830|
| |Natrona County|     0|  0.000| N/A|   224|  2804.979| N/A|  79,858|
| |Uinta County|     0|  0.000| N/A|   267| 13200.831| N/A|  20,226|
| |Niobrara County|     0|  0.000| N/A|     2|   848.896| N/A|   2,356|
| |Park County|     0|  0.000| N/A|   117|  4007.673| N/A|  29,194|
| |Platte County|     0|  0.000| N/A|     5|   595.735| N/A|   8,393|
| |Sheridan County|     0|  0.000| N/A|    62|  2033.787| N/A|  30,485|
| |Sublette County|     0|  0.000| N/A|    39|  3967.043| N/A|   9,831|
| |Sweetwater County|     0|  0.000| N/A|   251|  5927.780| N/A|  42,343|
| |Teton County|     0|  0.000| N/A|   362| 15427.890| N/A|  23,464|
| |Laramie County|     0|  0.000| N/A|   484|  4864.322| N/A|  99,500|
| |Albany County|     0|  0.000| N/A|    88|  2263.374| N/A|  38,880|
| |Big Horn County|     0|  0.000| N/A|    36|  3053.435| N/A|  11,790|
| |Campbell County|     0|  0.000| N/A|   118|  2546.341| N/A|  46,341|
| |Converse County|     0|  0.000| N/A|    32|  2315.150| N/A|  13,822|
| |Crook County|     0|  0.000| N/A|    10|  1318.565| N/A|   7,584|
| |Fremont County|     0|  0.000| N/A|   491| 12506.049| N/A|  39,261|
| |Goshen County|     0|  0.000| N/A|    20|  1513.890| N/A|  13,211|
| |Hot Springs County|     0|  0.000| N/A|    18|  4078.858| N/A|   4,413|
| |Washakie County|     0|  0.000| N/A|    54|  6918.642| N/A|   7,805|
| |Weston County|     0|  0.000| N/A|     5|   721.813| N/A|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Yukon-Koyukuk Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,230|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Valdez-Cordova Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   9,202|
| |Southeast Fairbanks Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   6,893|
| |Skagway Municipality|     0|  0.000| N/A|     0|     0.000| N/A|   1,183|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   6,203|
| |Petersburg Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,266|
| |Bethel Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  18,386|
| |Kusilvak Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   8,314|
| |Kodiak Island Borough|     0|  0.000| N/A|     0|     0.000| N/A|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000| N/A|     0|     0.000| N/A|  13,901|
| |Kenai Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|  58,708|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Hoonah-Angoon Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   2,148|
| |Haines Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Dillingham Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   4,916|
| |Denali Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,097|
| |Bristol Bay Borough|     0|  0.000| N/A|     0|     0.000| N/A|     836|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Fairbanks North Star Borough|     0|  0.000| N/A|     0|     0.000| N/A|  96,849|
| |Aleutians West Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,634|
| |Aleutians East Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,337|
| |Matanuska-Susitna Borough|     0|  0.000| N/A|     0|     0.000| N/A| 108,317|
| |Nome Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  10,004|
| |North Slope Borough|     0|  0.000| N/A|     0|     0.000| N/A|   9,832|
| |Northwest Arctic Borough|     0|  0.000| N/A|     0|     0.000| N/A|   7,621|
| |Lake and Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|   1,592|


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


