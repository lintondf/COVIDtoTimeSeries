# Analysis of US By County #

Updated: at 2020-08-15

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 134,722 deaths (466.711 deaths/million) and 4,565,749 confirmed cases (15816.934 confirmed cases/million).  This group accounts for 81.18% of all US deaths and for 87.46% of all US cases.

24.40% of this group's deaths (19.81% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.26% of this group's deaths (20.50% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,435 (12.66% of the total US population):



The next 25.32% of this group's deaths (20.55% of the total US deaths) occured in 92 counties in 31 states with a combined population of 69,593,319 (21.20% of the total US population)

The remaining 25.02% of this group's deaths (20.31% of the total US deaths) occured in 851 counties in 50 states with a combined population of 140,213,087 (42.72% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,753 deaths (271.695 deaths/million) and 484,655 confirmed cases (12245.732 confirmed cases/million).  This group accounts for 6.48% of all US deaths and for 9.28% of all US cases.

24.96% of this group's deaths (1.62% of the total US deaths) occured in 61 counties in 16 states with a combined population of 2,074,170 (0.63% of the total US population):



The next 24.98% of this group's deaths (1.62% of the total US deaths) occured in 117 counties in 28 states with a combined population of 3,478,678 (1.06% of the total US population):



The next 24.99% of this group's deaths (1.62% of the total US deaths) occured in 237 counties in 34 states with a combined population of 5,797,456 (1.77% of the total US population)

The remaining 25.07% of this group's deaths (1.62% of the total US deaths) occured in 1,737 counties in 47 states with a combined population of 28,227,160 (8.60% of the total US population) 

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
|NJ|21 counties|15,903| 1790.437| N/A|186,163| 20959.133| N/A|8,882,190|
| |Essex County| 2,110| 2640.884|  0.536|19,870| 24869.364| 32.899| 798,975|
| |Bergen County| 2,036| 2184.076|  0.000|21,058| 22589.525| 55.782| 932,202|
| |Hudson County| 1,508| 2242.743|  1.275|19,830| 29491.769| 47.379| 672,391|
| |Middlesex County| 1,412| 1711.387|  1.905|18,045| 21871.084| 32.552| 825,062|
| |Union County| 1,349| 2424.772|  0.257|16,827| 30245.838| 49.045| 556,341|
| |Passaic County| 1,244| 2478.947|  1.423|17,858| 35586.040| 73.731| 501,826|
| |Ocean County| 1,020| 1679.881|  0.941|10,708| 17635.453| 33.880| 607,186|
| |Monmouth County|   857| 1384.950|  0.231|10,434| 16861.804| 38.554| 618,795|
| |Morris County|   829| 1685.490|  0.581| 7,315| 14872.572| 26.431| 491,845|
| |Mercer County|   621| 1690.118|  1.166| 8,169| 22232.806| 25.272| 367,430|
| |Camden County|   581| 1147.154|  0.846| 8,733| 17242.843| 66.003| 506,471|
| |Somerset County|   564| 1714.630|  0.869| 5,291| 16085.294| 29.533| 328,934|
| |Burlington County|   477| 1071.070|  1.925| 6,108| 13715.086| 50.041| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,535| 13406.910| 48.220| 263,670|
| |Gloucester County|   215| 737.220|  2.939| 3,368| 11548.643| 74.457| 291,636|
| |Sussex County|   198| 1409.373|  1.017| 1,344|  9566.653| 22.371| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,355| 12872.030| 20.356| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,396| 22711.617| 74.521| 149,527|
| |Hunterdon County|   124| 997.017|  0.000| 1,154|  9278.690|  9.189| 124,371|
| |Cape May County|    89| 966.981|  3.104|   846|  9191.756| 37.251|  92,039|
| |Salem County|    87| 1394.566|  0.000|   919| 14731.105| 75.568|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,342| 634.422| N/A|254,415| 13078.048| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,840| 32308.368| 27.373|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.000|44,045| 29828.640| 35.216|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.000|36,402| 37624.573| 39.276| 967,506|
| |Queens County|   986| 437.283|  0.958| 7,927|  3517.208| 19.130|2,253,858|
| |Kings County|   931| 363.852|  0.797| 1,360|   531.465|  2.891|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,981| 42914.279| 24.556| 325,789|
| |Erie County|   674| 733.644|  0.466| 9,064|  9866.094| 42.451| 918,702|
| |Bronx County|   650| 458.158|  1.004|26,997| 19035.690| 103.532|1,418,207|
| |Orange County|   491| 1275.523|  0.000|11,217| 29139.606| 32.658| 384,940|
| |New York County|   415| 254.678|  0.558|15,570|  9559.725| 51.994|1,628,706|
| |Monroe County|   285| 384.216|  0.000| 5,122|  6905.105| 42.562| 741,770|
| |Onondaga County|   203| 440.798|  0.931| 3,646|  7917.000| 27.918| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,655| 15821.602| 32.046| 294,218|
| |Richmond County|   148| 311.252|  0.682| 7,927| 16648.962| 90.551| 476,143|
| |Albany County|   129| 422.250|  0.468| 2,639|  8638.128| 30.862| 305,506|
| |Oneida County|   117| 511.652|  1.249| 2,189|  9572.705| 37.484| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,524|  7282.075| 22.526| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,086| 11747.281| 29.766| 177,573|
| |Broome County|    69| 362.228|  0.000| 1,165|  6115.871| 37.498| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,457| 14818.959| 15.983|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   299|  7409.794|  7.081|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,491| 19766.147|  5.682|  75,432|
| |Steuben County|    42| 440.349|  0.000|   303|  3176.800|  8.987|  95,379|
| |Rensselaer County|    38| 239.424|  7.201|   785|  4946.004| 23.402| 158,714|
| |Columbia County|    37| 622.257|  0.000|   551|  9266.578| 38.441|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,092|  7031.597| 34.036| 155,299|
| |Ontario County|    34| 309.719|  0.000|   366|  3334.032| 11.712| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269| 11.170|  63,944|
| |Tioga County|    25| 518.640|  0.000|   195|  4045.391|  5.927|  48,203|
| |Fulton County|    24| 449.581|  0.000|   303|  5675.964| 26.761|  53,383|
| |Greene County|    18| 381.453|  0.000|   296|  6272.781| 15.137|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   782|  3402.026| 18.645| 229,863|
| |Madison County|    17| 239.636|  0.000|   419|  5906.317| 14.096|  70,941|
| |Washington County|    14| 228.743|  0.000|   260|  4248.088|  9.336|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   260|  2048.809| 12.383| 126,903|
| |Livingston County|     8| 127.158|  0.000|   178|  2829.259|  9.083|  62,914|
| |Yates County|     7| 280.978|  0.000|    58|  2328.102| 11.468|  24,913|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959|  9.079|  47,207|
| |Cattaraugus County|     6| 78.826|  0.000|   169|  2220.266|  9.384|  76,117|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  4.802|  59,493|
| |Genesee County|     5| 87.291|  0.000|   284|  4958.101| 17.458|  57,280|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436|  7.168|  39,859|
| |Clinton County|     4| 49.699|  0.000|   130|  1615.208|  5.325|  80,485|
| |Herkimer County|     4| 65.233|  0.000|   278|  4533.668| 18.638|  61,319|
| |Delaware County|     4| 90.631|  0.000|   107|  2424.380|  9.710|  44,135|
| |Montgomery County|     4| 81.266|  0.000|   181|  3677.292| 31.926|  49,221|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  0.000| 107,740|
| |Oswego County|     3| 25.614|  0.000|   264|  2254.021| 15.856| 117,124|
| |Wayne County|     3| 33.364|  0.000|   265|  2947.130| 25.420|  89,918|
| |Seneca County|     3| 88.194|  0.000|    93|  2734.008| 25.198|  34,016|
| |Chemung County|     3| 35.947|  0.000|   187|  2240.702| 32.524|  83,456|
| |Cayuga County|     2| 26.118|  0.000|   163|  2128.604| 22.387|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697|  3.099|  46,091|
| |Tompkins County|     0|  0.000|  0.000|   236|  2309.650|  4.194| 102,180|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  0.000|  30,999|
| |Lewis County|     0|  0.000|  0.000|    47|  1787.344| 43.461|  26,296|
| |Jefferson County|     0|  0.000|  0.000|   143|  1301.965|  3.902| 109,834|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594|  0.000|   4,416|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525|  0.000|  50,022|
| |Essex County|     0|  0.000|  0.000|    57|  1545.344|  7.746|  36,885|
| |Cortland County|     0|  0.000|  0.000|    97|  2038.629|  6.005|  47,581|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|11,148| 282.141| N/A|613,101| 15516.743| N/A|39,512,223|
| |Los Angeles County| 5,215| 519.469|  4.212|218,831| 21797.855| 207.375|10,039,107|
| |Riverside County|   881| 356.601|  4.742|45,662| 18482.554| 301.264|2,470,546|
| |Orange County|   789| 248.450|  3.824|42,854| 13494.382| 184.437|3,175,692|
| |San Diego County|   622| 186.321|  1.669|34,065| 10204.204| 125.726|3,338,330|
| |San Bernardino County|   561| 257.329|  4.194|39,374| 18060.764| 290.618|2,180,085|
| |San Joaquin County|   261| 342.453| 12.933|14,651| 19223.300| 474.598| 762,148|
| |Imperial County|   257| 1418.205| 13.402|10,035| 55376.211| 342.135| 181,215|
| |Alameda County|   219| 131.033|  1.111|14,558|  8710.433| 143.085|1,671,329|
| |Santa Clara County|   208| 107.892|  0.889|13,865|  7191.942| 187.403|1,927,852|
| |Tulare County|   205| 439.730|  2.758|12,105| 25965.529| 499.484| 466,195|
| |Kern County|   204| 226.616|  6.983|25,888| 28757.990| 615.576| 900,202|
| |Fresno County|   203| 203.183|  6.577|19,157| 19174.238| 362.040| 999,101|
| |Sacramento County|   199| 128.217|  4.050|13,615|  8772.224| 282.666|1,552,058|
| |Stanislaus County|   195| 354.121| 11.415|11,953| 21706.679| 660.247| 550,660|
| |Contra Costa County|   152| 131.770|  1.982|10,756|  9324.454| 247.192|1,153,526|
| |San Mateo County|   126| 164.368|  1.118| 6,803|  8874.563| 153.745| 766,573|
| |Ventura County|    95| 112.292|  2.195| 9,090| 10744.605| 178.148| 846,006|
| |Merced County|    89| 320.513| 13.891| 6,777| 24405.791| 988.805| 277,680|
| |Marin County|    82| 316.815|  2.208| 5,674| 21922.063| 230.160| 258,826|
| |Santa Barbara County|    77| 172.453|  2.880| 7,274| 16291.190| 199.009| 446,499|
| |San Francisco County|    69| 78.271| N/A| 8,053|  9135.057| N/A| 881,549|
| |Kings County|    64| 418.465|  7.473| 5,243| 34281.418| 737.918| 152,940|
| |Sonoma County|    51| 103.169|  2.023| 4,063|  8219.106| 203.736| 494,336|
| |Madera County|    47| 298.741|  9.988| 2,924| 18585.494| 596.574| 157,327|
| |Yolo County|    46| 208.617|  2.592| 1,966|  8916.100| 198.251| 220,500|
| |Solano County|    41| 91.591|  0.638| 4,596| 10267.110| 203.287| 447,643|
| |Monterey County|    41| 94.457|  1.975| 5,890| 13569.521| 241.572| 434,061|
| |Placer County|    27| 67.783|  2.510| 2,543|  6384.170| 159.237| 398,329|
| |San Luis Obispo County|    18| 63.579|  1.009| 2,439|  8614.996| 197.802| 283,111|
| |Butte County|    12| 54.748|  2.607| 1,370|  6250.399| 202.046| 219,186|
| |Napa County|    11| 79.858|  1.037| 1,206|  8755.372| 165.939| 137,744|
| |Amador County|    11| 276.716| 39.531|   208|  5232.441| 165.311|  39,752|
| |Mendocino County|    10| 115.275|  0.000|   529|  6098.053| 273.367|  86,749|
| |Shasta County|    10| 55.531|  0.793|   488|  2709.907| 61.084| 180,080|
| |Sutter County|     7| 72.187|  1.473| 1,091| 11250.786| 291.693|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,371|  5018.063| 74.249| 273,213|
| |Inyo County|     5| 277.177| 15.839|   127|  7040.302| 324.693|  18,039|
| |Colusa County|     5| 232.051|  6.630|   409| 18981.761| 311.611|  21,547|
| |San Benito County|     4| 63.686|  0.000|   815| 12976.054| 263.843|  62,808|
| |Humboldt County|     4| 29.508|  0.000|   309|  2279.467| 30.562| 135,558|
| |Yuba County|     4| 50.847|  0.000|   740|  9406.620| 305.080|  78,668|
| |Glenn County|     3| 105.660|  0.000|   436| 15355.898| 382.388|  28,393|
| |Tuolumne County|     2| 36.712|  0.000|   160|  2936.965| 34.090|  54,478|
| |Mariposa County|     2| 116.259|  0.000|    63|  3662.152| 24.913|  17,203|
| |Lake County|     2| 31.063|  0.000|   268|  4162.396| 106.501|  64,386|
| |El Dorado County|     2| 10.371|  0.741|   827|  4288.463| 82.228| 192,843|
| |Calaveras County|     1| 21.784|  0.000|   174|  3790.437| 118.257|  45,905|
| |Nevada County|     1| 10.025|  0.000|   362|  3628.891| 58.715|  99,755|
| |Mono County|     1| 69.233|  0.000|   160| 11077.264| 69.233|  14,444|
| |Tehama County|     1| 15.365|  0.000|   312|  4793.805| 89.994|  65,084|
| |Trinity County|     0|  0.000|  0.000|     8|   651.201| 34.886|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   111|  2549.438| 62.341|  43,539|
| |Sierra County|     0|  0.000|  0.000|     6|  1996.672| 142.619|   3,005|
| |Plumas County|     0|  0.000|  0.000|    39|  2073.696| 37.980|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 16.158|   8,841|
| |Lassen County|     0|  0.000|  0.000|   695| 22732.476| 266.341|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   106|  3811.304| 51.365|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties|10,078| 347.567| N/A|539,673| 18612.057| N/A|28,995,881|
| |Harris County| 1,771| 375.743|  7.789|90,574| 19216.583| 224.015|4,713,325|
| |Hidalgo County|   931| 1071.708| 23.187|21,806| 25101.674| 373.626| 868,707|
| |Bexar County|   865| 431.733|  8.984|43,823| 21872.632| 108.664|2,003,554|
| |Dallas County|   816| 309.617|  3.794|57,313| 21746.406| 218.011|2,635,516|
| |Cameron County|   528| 1247.746| 38.148|17,618| 41634.075| 591.802| 423,163|
| |Tarrant County|   492| 234.005|  3.737|33,403| 15887.164| 187.055|2,102,515|
| |El Paso County|   354| 421.811| 11.575|17,632| 21009.535| 293.463| 839,238|
| |Travis County|   332| 260.606|  4.149|23,870| 18736.940| 155.870|1,273,954|
| |Nueces County|   277| 764.572| 18.927|16,527| 45617.648| 1028.762| 362,294|
| |Fort Bend County|   189| 232.848|  5.456|11,369| 14006.613| 390.368| 811,688|
| |Webb County|   185| 668.710| 15.491| 9,303| 33627.084| 910.375| 276,652|
| |Galveston County|   122| 356.580|  4.593| 9,888| 28900.535| 249.272| 342,139|
| |Brazoria County|   105| 280.551|  6.489| 7,917| 21153.517| 315.667| 374,264|
| |Williamson County|   102| 172.720|  2.903| 7,330| 12412.137| 262.467| 590,551|
| |Denton County|   100| 112.713|  2.576| 8,214|  9258.268| 111.908| 887,207|
| |Collin County|    98| 94.711|  1.243| 9,612|  9289.380| 323.618|1,034,730|
| |Montgomery County|    97| 159.699|  3.528| 6,957| 11453.907| 89.375| 607,391|
| |Jefferson County|    91| 361.736|  7.950| 6,165| 24506.589| 191.373| 251,565|
| |Starr County|    83| 1284.174| 41.995| 2,368| 36637.631| 554.781|  64,633|
| |Comal County|    80| 512.134| 10.974| 2,008| 12854.573| 213.084| 156,209|
| |Lubbock County|    76| 244.712|  2.300| 6,429| 20700.714| 216.193| 310,569|
| |McLennan County|    60| 233.806|  4.453| 5,248| 20450.232| 223.786| 256,623|
| |Ector County|    59| 354.945|  2.578| 3,771| 22686.391| 206.263| 166,223|
| |Guadalupe County|    58| 347.624|  5.137| 1,762| 10560.573| 76.203| 166,847|
| |Victoria County|    55| 597.281| 23.271| 3,569| 38758.090| 206.333|  92,084|
| |Midland County|    53| 299.720|  4.039| 2,888| 16331.886| 239.129| 176,832|
| |Brazos County|    51| 222.502|  2.493| 4,158| 18140.491| 83.516| 229,211|
| |Angelina County|    49| 565.069|  9.885| 1,898| 21887.793| 168.038|  86,715|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 78.677|  49,025|
| |Ellis County|    48| 259.704|  6.183| 3,238| 17519.180| 332.359| 184,826|
| |Maverick County|    47| 800.381| 21.895| 2,596| 44208.304| 669.012|  58,722|
| |Potter County|    46| 391.773|  2.433| 3,802| 32380.871| 171.553| 117,415|
| |Bell County|    46| 126.748|  3.936| 4,195| 11558.894| 161.388| 362,924|
| |Hays County|    45| 195.490|  4.965| 5,111| 22203.301| 61.440| 230,191|
| |Nacogdoches County|    43| 659.469|  4.382| 1,187| 18204.405| 118.310|  65,204|
| |Walker County|    42| 575.571|  1.958| 3,184| 43633.772| 606.895|  72,971|
| |Washington County|    40| 1114.765|  3.981|   523| 14575.553| 95.551|  35,882|
| |Bowie County|    38| 407.529|  9.192|   774|  8300.713| 15.321|  93,245|
| |Liberty County|    35| 396.740|  3.239| 1,085| 12298.938| 199.180|  88,219|
| |San Patricio County|    34| 509.516| 25.690| 1,082| 16214.596| 378.926|  66,730|
| |Tom Green County|    32| 268.456|  9.588| 2,844| 23859.060| 287.632| 119,200|
| |Johnson County|    32| 182.007|  1.625| 2,103| 11961.301| 238.072| 175,817|
| |Matagorda County|    32| 873.291| 27.290|   828| 22596.403| 370.369|  36,643|
| |Medina County|    31| 600.962| 13.847|   963| 18668.579| 556.651|  51,584|
| |Hale County|    31| 927.977| 25.658| 1,474| 44123.810| 927.977|  33,406|
| |Smith County|    31| 133.190|  6.138| 2,717| 11673.419| 151.603| 232,751|
| |Wharton County|    30| 721.917| 17.189|   982| 23630.763| 1003.809|  41,556|
| |Willacy County|    30| 1404.626| 40.132|   751| 35162.468| 461.520|  21,358|
| |Caldwell County|    29| 664.163|  9.815| 1,171| 26818.432| 160.315|  43,664|
| |Gregg County|    29| 233.975|  5.763| 1,630| 13150.994| 289.299| 123,945|
| |Kaufman County|    29| 212.994|  5.246| 2,406| 17671.166| 294.834| 136,154|
| |Taylor County|    28| 202.849|  6.210| 1,145|  8295.058| 28.978| 138,034|
| |Orange County|    27| 323.757| 15.417| 1,521| 18238.285| 260.376|  83,396|
| |Grimes County|    27| 934.903| 29.679|   920| 31855.956| 237.436|  28,880|
| |Harrison County|    24| 360.615|  2.147|   729| 10953.676| 103.033|  66,553|
| |Lavaca County|    23| 1141.213| 56.706|   638| 31656.247| 127.589|  20,154|
| |Bastrop County|    23| 259.234|  3.220| 1,421| 16016.140| 114.320|  88,723|
| |Randall County|    23| 167.014|  2.075| 1,847| 13411.951| 137.968| 137,713|
| |Hunt County|    21| 212.995|  0.000| 1,261| 12789.825| 179.669|  98,594|
| |DeWitt County|    21| 1041.667| 21.259|   728| 36111.111| 602.324|  20,160|
| |Wilson County|    20| 391.619|  5.595|   484|  9477.188| 139.864|  51,070|
| |Parker County|    19| 132.981|  1.000| 1,379|  9651.591| 177.974| 142,878|
| |Atascosa County|    19| 371.435|  2.793|   509|  9950.541| 209.456|  51,153|
| |Lamar County|    19| 381.075|  2.865|   690| 13839.026| 91.687|  49,859|
| |Jim Wells County|    18| 444.642| 17.645|   813| 20083.000| 381.122|  40,482|
| |Hardin County|    18| 312.489|  7.440| 1,099| 19079.199| 376.971|  57,602|
| |Shelby County|    18| 712.194|  0.000|   411| 16261.771| 73.480|  25,274|
| |Panola County|    18| 776.063|  0.000|   301| 12977.494| 98.548|  23,194|
| |Deaf Smith County|    18| 970.560|  7.703|   723| 38984.148| 508.388|  18,546|
| |Brown County|    17| 448.975|  3.773|   502| 13257.976| 430.111|  37,864|
| |Kleberg County|    17| 554.107| 46.564|   476| 15514.993| 242.131|  30,680|
| |Titus County|    17| 519.084|  8.724| 1,397| 42656.489| 471.101|  32,750|
| |Grayson County|    16| 117.464|  3.146| 1,204|  8839.162| 105.927| 136,212|
| |Aransas County|    16| 680.561| 18.229|   186|  7911.527| 103.300|  23,510|
| |Lamb County|    16| 1240.983| 55.401|   242| 18769.875| 254.845|  12,893|
| |Rockwall County|    15| 142.973|  4.085| 1,090| 10389.363| 292.754| 104,915|
| |Bee County|    15| 460.617| 26.321| 1,344| 41271.304| 2013.555|  32,565|
| |Anderson County|    15| 259.808| 12.372| 2,435| 42175.457| 138.564|  57,735|
| |Fayette County|    14| 552.355|  0.000|   405| 15978.853| 152.180|  25,346|
| |Polk County|    14| 272.623|  8.346|   769| 14974.782| 58.419|  51,353|
| |Moore County|    14| 668.577|  6.822| 1,080| 51575.931| 225.133|  20,940|
| |Jasper County|    13| 365.898| 16.083|   332|  9344.479| 112.584|  35,529|
| |Hood County|    13| 210.892|  9.270|   650| 10544.587| 296.639|  61,643|
| |Red River County|    12| 998.087| 11.882|   140| 11644.348| 35.646|  12,023|
| |Henderson County|    12| 145.038|  0.000|   677|  8182.554| 75.972|  82,737|
| |Gonzales County|    11| 527.907| 13.712|   716| 34361.952| 246.814|  20,837|
| |Jackson County|    11| 745.257| 48.393|   415| 28116.531| 145.180|  14,760|
| |San Augustine County|    11| 1335.438|  0.000|   178| 21609.809| 277.494|   8,237|
| |Lee County|    11| 638.088| 16.574|   177| 10267.417| 49.721|  17,239|
| |Wichita County|    11| 83.188|  0.000| 1,099|  8311.276| 125.323| 132,230|
| |Navarro County|    11| 219.504|  8.552|   925| 18458.284| 239.459|  50,113|
| |Cherokee County|    11| 208.943| 13.568| 1,217| 23116.666| 716.375|  52,646|
| |Uvalde County|    10| 373.958|  5.342|   584| 21839.123| 309.851|  26,741|
| |Wise County|    10| 142.890|  8.165|   508|  7258.802| 240.871|  69,984|
| |Burnet County|    10| 207.663|  2.967|   572| 11878.310| 62.299|  48,155|
| |Palo Pinto County|    10| 342.595| 19.577|   342| 11716.743| 420.902|  29,189|
| |Wood County|     9| 197.633|  9.411|   358|  7861.394| 131.755|  45,539|
| |Fannin County|     9| 253.421|  4.023|   276|  7771.583| 136.767|  35,514|
| |Karnes County|     9| 576.886| 27.471|   661| 42369.079| 906.535|  15,601|
| |Marion County|     9| 913.335| 14.497|   135| 13700.020| 72.487|   9,854|
| |Cass County|     9| 299.740|  4.758|   197|  6560.980| 123.702|  30,026|
| |San Jacinto County|     8| 277.210|  0.000|   185|  6410.479| 39.601|  28,859|
| |Parmer County|     7| 728.787|  0.000|   359| 37376.366| 356.957|   9,605|
| |Howard County|     7| 190.923|  7.793|   189|  5154.920| 81.824|  36,664|
| |Houston County|     7| 304.772|  6.220|   320| 13932.428| 49.759|  22,968|
| |Erath County|     7| 163.942|  6.692|   574| 13443.253| 180.671|  42,698|
| |Van Zandt County|     7| 123.697| 10.098|   440|  7775.225| 164.088|  56,590|
| |Duval County|     7| 627.409| 12.804|   195| 17477.817| 396.932|  11,157|
| |Andrews County|     7| 374.231|  7.637|   338| 18070.035| 450.605|  18,705|
| |Hill County|     7| 191.001|  0.000|   339|  9249.911| 81.858|  36,649|
| |Young County|     6| 333.148| 15.864|   199| 11049.417| 309.352|  18,010|
| |Goliad County|     6| 783.494| 37.309|   117| 15278.141| 746.185|   7,658|
| |Gillespie County|     6| 222.321|  0.000|   185|  6854.898| 52.934|  26,988|
| |Frio County|     6| 295.479|  7.035|   567| 27922.781| 436.184|  20,306|
| |Floyd County|     6| 1050.420|  0.000|    92| 16106.443| 100.040|   5,712|
| |Burleson County|     6| 325.327|  0.000|   248| 13446.836| 61.967|  18,443|
| |Camp County|     6| 458.225| 10.910|   248| 18939.973| 207.292|  13,094|
| |Calhoun County|     6| 281.822| 13.420|   552| 25927.666| 154.331|  21,290|
| |Zavala County|     6| 506.757| 12.066|   236| 19932.432| 374.035|  11,840|
| |Coryell County|     6| 78.998|  1.881|   712|  9374.465| 97.807|  75,951|
| |Dallam County|     6| 823.384| 19.604|   196| 26897.214| 176.439|   7,287|
| |Sabine County|     6| 569.152|  0.000|    62|  5881.237| 149.064|  10,542|
| |Kerr County|     6| 114.068|  0.000|   415|  7889.734| 51.602|  52,600|
| |Waller County|     5| 90.504|  0.000|   515|  9321.942| 191.352|  55,246|
| |Dawson County|     5| 392.835| 11.224|   162| 12727.844| 213.253|  12,728|
| |Martin County|     5| 866.401| 24.754|    65| 11263.213| 247.543|   5,771|
| |Hockley County|     5| 217.193|  6.206|   221|  9599.930| 130.316|  23,021|
| |Reeves County|     5| 312.969|  0.000|   150|  9389.084| 53.652|  15,976|
| |Refugio County|     5| 719.632| 20.561|   241| 34686.241| 493.462|   6,948|
| |Blanco County|     5| 419.076|  0.000|   115|  9638.756| 203.551|  11,931|
| |Chambers County|     5| 114.059|  6.518| 1,018| 23222.392| 247.671|  43,837|
| |Bailey County|     4| 571.429|  0.000|   183| 26142.857| 265.306|   7,000|
| |Dimmit County|     4| 395.101| 14.111|   163| 16100.356| 239.883|  10,124|
| |Newton County|     4| 294.226|  0.000|   116|  8532.549| 241.685|  13,595|
| |Brooks County|     4| 563.936| 40.281|   144| 20301.706| 906.326|   7,093|
| |Crockett County|     4| 1154.734| 41.241|   157| 45323.326| 82.481|   3,464|
| |Austin County|     4| 133.191|  4.757|   315| 10488.812| 404.331|  30,032|
| |Kendall County|     4| 84.333|  0.000|   171|  3605.237| 42.167|  47,431|
| |Castro County|     4| 531.208|  0.000|   205| 27224.436| 151.774|   7,530|
| |Live Oak County|     4| 327.681| 23.406|   240| 19660.850| 210.652|  12,207|
| |Lynn County|     4| 672.156|  0.000|    74| 12434.885| 192.045|   5,951|
| |Trinity County|     4| 273.019|  9.751|   163| 11125.520| 68.255|  14,651|
| |Presidio County|     4| 596.659| 85.237|    49|  7309.069| 63.928|   6,704|
| |Knox County|     4| 1091.703| 116.968|    62| 16921.397| 116.968|   3,664|
| |Lampasas County|     4| 186.672| 13.334|   129|  6020.161| 260.007|  21,428|
| |Zapata County|     3| 211.581| 10.075|   190| 13400.099| 201.505|  14,179|
| |Bandera County|     3| 129.803|  0.000|    98|  4240.222| 55.630|  23,112|
| |Hamilton County|     3| 354.568|  0.000|    91| 10755.230| 185.726|   8,461|
| |Yoakum County|     3| 344.313|  0.000|   119| 13657.753| 311.521|   8,713|
| |Garza County|     3| 481.618|  0.000|   101| 16214.481| 45.868|   6,229|
| |Stephens County|     3| 320.307|  0.000|    48|  5124.920| 213.538|   9,366|
| |Gaines County|     3| 139.587|  0.000|   191|  8887.028| 219.351|  21,492|
| |Hopkins County|     3| 80.897|  7.705|   213|  5743.717| 50.079|  37,084|
| |Falls County|     3| 173.440|  0.000|   142|  8209.516| 148.663|  17,297|
| |Morris County|     3| 242.170|  0.000|   131| 10574.750| 299.829|  12,388|
| |Milam County|     3| 120.856|  0.000|   366| 14744.390| 189.916|  24,823|
| |Nolan County|     3| 203.887|  0.000|   137|  9310.860| 38.836|  14,714|
| |Reagan County|     3| 779.423|  0.000|    65| 16887.503| 111.346|   3,849|
| |Limestone County|     3| 128.003|  0.000|   290| 12373.597| 426.676|  23,437|
| |Leon County|     3| 172.374|  8.208|   156|  8963.457| 123.124|  17,404|
| |Comanche County|     3| 220.022|  0.000|   171| 12541.254| 314.317|  13,635|
| |Hutchinson County|     3| 143.280|  6.823|   133|  6352.087| 68.229|  20,938|
| |Cooke County|     3| 72.715|  0.000|   264|  6398.914| 141.967|  41,257|
| |Callahan County|     3| 215.162|  0.000|    51|  3657.749| 51.229|  13,943|
| |Upshur County|     2| 47.901|  0.000|   264|  6322.899| 177.917|  41,753|
| |Pecos County|     2| 126.398|  9.028|   256| 16178.980| 126.398|  15,823|
| |Rusk County|     2| 36.761|  0.000|   398|  7315.370| 84.024|  54,406|
| |Terry County|     2| 162.114|  0.000|   166| 13455.459| 335.808|  12,337|
| |Montague County|     2| 100.918|  7.208|    83|  4188.112| 115.335|  19,818|
| |Robertson County|     2| 117.137|  0.000|   238| 13939.323| 58.569|  17,074|
| |Scurry County|     2| 119.739|  8.553|   505| 30234.090| 265.136|  16,703|
| |Ochiltree County|     2| 203.335|  0.000|   100| 10166.734| 87.143|   9,836|
| |La Salle County|     2| 265.957|  0.000|   361| 48005.319|  0.000|   7,520|
| |Throckmorton County|     2| 1332.445|  0.000|     4|  2664.890|  0.000|   1,501|
| |Swisher County|     2| 270.380|  0.000|    82| 11085.575| 38.626|   7,397|
| |Runnels County|     2| 194.856| 13.918|   150| 14614.186| 403.630|  10,264|
| |Madison County|     2| 140.017|  0.000|   686| 48025.763| 280.034|  14,284|
| |Tyler County|     2| 92.285|  0.000|   127|  5860.096| 72.510|  21,672|
| |Gray County|     2| 91.383|  0.000|   221| 10097.779| 45.691|  21,886|
| |Culberson County|     2| 921.234|  0.000|    21|  9672.962| 263.210|   2,171|
| |Hansford County|     2| 370.439|  0.000|    91| 16854.973| 582.118|   5,399|
| |Jim Hogg County|     2| 384.615| 27.473|    65| 12500.000| 82.418|   5,200|
| |Colorado County|     2| 93.054|  0.000|   354| 16470.479| 545.028|  21,493|
| |Franklin County|     2| 186.480|  0.000|    92|  8578.089| 26.640|  10,725|
| |Bosque County|     2| 107.038|  0.000|   179|  9579.877| 183.493|  18,685|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 204.374|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461|  0.000|   9,203|
| |Hudspeth County|     2| 409.333|  0.000|    35|  7163.324| 350.857|   4,886|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354|  0.000|   3,387|
| |Eastland County|     1| 54.466|  0.000|    90|  4901.961| 155.618|  18,360|
| |Sutton County|     1| 264.831|  0.000|    67| 17743.644| 226.998|   3,776|
| |Fisher County|     1| 261.097|  0.000|    30|  7832.898| 149.198|   3,830|
| |Kimble County|     1| 230.574|  0.000|    16|  3689.186| 98.817|   4,337|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Winkler County|     1| 124.844|  0.000|    88| 10986.267| 142.679|   8,010|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366|  0.000|   2,793|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Hall County|     1| 337.382|  0.000|    15|  5060.729| 192.790|   2,964|
| |Crosby County|     1| 174.307|  0.000|    65| 11329.963| 149.406|   5,737|
| |Wilbarger County|     1| 78.315|  0.000|    77|  6030.229| 145.442|  12,769|
| |Ward County|     1| 83.347|  0.000|    96|  8001.334| 83.347|  11,998|
| |Real County|     1| 289.687|  0.000|    90| 26071.842| 124.152|   3,452|
| |Rains County|     1| 79.911|  0.000|    54|  4315.167| 34.247|  12,514|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Clay County|     1| 95.502|  0.000|    45|  4297.584| 68.216|  10,471|
| |McCulloch County|     1| 125.251|  0.000|    55|  6888.778| 161.036|   7,984|
| |Llano County|     1| 45.882|  0.000|    90|  4129.387| 13.109|  21,795|
| |Mitchell County|     1| 117.028|  0.000|    70|  8191.925| 183.900|   8,545|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Stonewall County|     0|  0.000|  0.000|     7|  5185.185| 211.640|   1,350|
| |Sterling County|     0|  0.000|  0.000|     1|   774.593| 110.656|   1,291|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Baylor County|     0|  0.000|  0.000|    13|  3704.759| 162.847|   3,509|
| |Somervell County|     0|  0.000|  0.000|    84|  9202.454| 172.155|   9,128|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 119.048|   1,200|
| |Carson County|     0|  0.000|  0.000|    17|  2868.714| 48.214|   5,926|
| |San Saba County|     0|  0.000|  0.000|    26|  4293.972| 70.780|   6,055|
| |Sherman County|     0|  0.000|  0.000|    44| 14559.894| 189.090|   3,022|
| |Kinney County|     0|  0.000|  0.000|    21|  5726.752| 77.915|   3,667|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    66|  7386.682| 159.885|   8,935|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Childress County|     0|  0.000|  0.000|    50|  6843.690| 195.534|   7,306|
| |Coleman County|     0|  0.000|  0.000|    33|  4036.697| 244.648|   8,175|
| |Wheeler County|     0|  0.000|  0.000|    35|  6922.468| 56.510|   5,056|
| |Haskell County|     0|  0.000|  0.000|    51|  9013.786| 227.238|   5,658|
| |Hartley County|     0|  0.000|  0.000|    93| 16678.623| 230.580|   5,576|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |Hardeman County|     0|  0.000|  0.000|    22|  5593.694| 181.613|   3,933|
| |Jones County|     0|  0.000|  0.000|   601| 29925.808|  0.000|  20,083|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Archer County|     0|  0.000|  0.000|    31|  3624.459| 167.026|   8,553|
| |Freestone County|     0|  0.000|  0.000|   174|  8824.872| 94.190|  19,717|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Mills County|     0|  0.000|  0.000|    26|  5335.522| 205.212|   4,873|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Lipscomb County|     0|  0.000|  0.000|    22|  6804.825| 176.749|   3,233|
| |Edwards County|     0|  0.000|  0.000|    30| 15527.950| 369.713|   1,932|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 50.073|   2,853|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Collingsworth County|     0|  0.000|  0.000|    12|  4109.589| 48.924|   2,920|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 43.581|   3,278|
| |Hemphill County|     0|  0.000|  0.000|    44| 11521.341| 74.814|   3,819|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Concho County|     0|  0.000|  0.000|    33| 12105.649| 262.027|   2,726|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Shackelford County|     0|  0.000|  0.000|    19|  5819.296| 43.754|   3,265|
| |Mason County|     0|  0.000|  0.000|    60| 14038.372| 300.822|   4,274|
| |McMullen County|     0|  0.000|  0.000|    10| 13458.950| 192.271|     743|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 9,141| 425.603| N/A|562,550| 26192.238| N/A|21,477,737|
| |Miami-Dade County| 1,999| 735.754|  9.990|142,662| 52508.337| 696.845|2,716,940|
| |Palm Beach County|   976| 652.071|  5.440|38,575| 25772.163| 234.887|1,496,770|
| |Broward County|   914| 468.051|  9.657|65,369| 33474.875| 338.200|1,952,778|
| |Pinellas County|   541| 554.874|  8.791|18,466| 18939.565| 135.532| 974,996|
| |Hillsborough County|   458| 311.148|  6.988|33,694| 22890.443| 177.508|1,471,968|
| |Lee County|   371| 481.457|  7.786|17,178| 22292.386| 172.413| 770,577|
| |Polk County|   353| 487.046|  9.658|15,108| 20845.032| 250.126| 724,777|
| |Orange County|   335| 240.410|  4.921|32,861| 23582.441| 188.125|1,393,452|
| |Manatee County|   245| 607.559| 19.839| 9,662| 23960.144| 190.593| 403,253|
| |Duval County|   214| 223.439|  5.519|24,300| 25371.833| 210.462| 957,755|
| |St. Lucie County|   195| 593.974| 15.230| 6,125| 18656.887| 217.573| 328,297|
| |Sarasota County|   174| 401.160| 14.492| 6,604| 15225.641| 167.644| 433,742|
| |Brevard County|   168| 279.097|  6.645| 6,392| 10618.963| 128.394| 601,942|
| |Volusia County|   151| 272.916|  6.455| 8,308| 15015.797| 168.862| 553,284|
| |Collier County|   151| 392.308|  7.423|10,734| 27887.618| 197.453| 384,902|
| |Escambia County|   147| 461.805| 14.361|10,122| 31798.590| 612.599| 318,316|
| |Pasco County|   145| 261.758|  5.931| 7,348| 13264.807| 117.340| 553,947|
| |Seminole County|   143| 303.078|  9.992| 7,370| 15620.165| 119.293| 471,826|
| |Marion County|   111| 303.628|  9.769| 7,030| 19229.770| 408.745| 365,579|
| |Osceola County|   109| 290.086|  3.422|10,146| 27001.924| 283.242| 375,751|
| |Martin County|   104| 645.963| 11.535| 3,907| 24267.081| 124.224| 161,000|
| |Charlotte County|    97| 513.472|  5.294| 2,340| 12386.851| 125.532| 188,910|
| |Lake County|    79| 215.190|  7.004| 5,489| 14951.596| 206.629| 367,118|
| |Indian River County|    62| 387.687|  8.933| 2,618| 16370.378| 150.072| 159,923|
| |Clay County|    61| 278.219|  7.167| 3,389| 15457.100| 132.268| 219,252|
| |Bay County|    61| 349.160| 13.083| 4,720| 27016.971| 430.113| 174,705|
| |Hernando County|    56| 288.779|  9.577| 2,160| 11138.614| 170.173| 193,920|
| |Okaloosa County|    50| 237.261|  8.135| 3,653| 17334.320| 177.607| 210,738|
| |Jackson County|    47| 1012.626| 30.779| 2,007| 43241.263| 538.631|  46,414|
| |Suwannee County|    46| 1035.640| 19.298| 2,203| 49598.127| 2724.182|  44,417|
| |Santa Rosa County|    45| 244.150|  6.976| 4,125| 22380.407| 258.876| 184,313|
| |Sumter County|    44| 332.276|  3.236| 1,436| 10844.283| 214.685| 132,420|
| |St. Johns County|    42| 158.687|  4.318| 3,883| 14670.989| 178.658| 264,672|
| |Highlands County|    40| 376.573|  5.380| 1,548| 14573.389| 259.567| 106,221|
| |Citrus County|    38| 253.914|  1.909| 1,708| 11412.764| 224.322| 149,657|
| |Hendry County|    38| 904.288|  3.400| 1,852| 44072.153| 431.747|  42,022|
| |Putnam County|    30| 402.571|  9.585| 1,576| 21148.401| 212.788|  74,521|
| |Alachua County|    27| 100.356|  0.531| 4,483| 16662.764| 253.279| 269,043|
| |Gadsden County|    26| 569.426| 15.644| 1,999| 43780.114| 682.060|  45,660|
| |Leon County|    26| 88.561|  0.973| 5,290| 18018.816| 231.622| 293,582|
| |Columbia County|    24| 334.793| 19.928| 2,985| 41639.930| 400.556|  71,686|
| |DeSoto County|    19| 499.987| 11.278| 1,398| 36788.506| 266.910|  38,001|
| |Walton County|    18| 243.010|  5.786| 1,466| 19791.821| 233.367|  74,071|
| |Washington County|    14| 549.602|  0.000|   910| 35724.100| 577.642|  25,473|
| |Flagler County|    14| 121.653|  1.241| 1,127|  9793.102| 147.722| 115,081|
| |Monroe County|    13| 175.136|  0.000| 1,603| 21595.624| 282.912|  74,228|
| |Okeechobee County|    12| 284.576| 10.163| 1,093| 25920.129| 271.025|  42,168|
| |Nassau County|    11| 124.118|  0.000| 1,296| 14623.413| 151.521|  88,625|
| |Madison County|    10| 540.745| 15.450|   748| 40447.737| 478.946|  18,493|
| |Hardee County|     8| 296.989|  5.303| 1,006| 37346.401| 519.731|  26,937|
| |Calhoun County|     8| 567.175| 10.128|   488| 34597.660| 719.097|  14,105|
| |Gilchrist County|     7| 376.709| 30.752|   398| 21418.577| 407.460|  18,582|
| |Liberty County|     7| 837.922| 51.301|   410| 49078.286| 256.507|   8,354|
| |Wakulla County|     5| 148.196|  4.234|   753| 22318.385| 385.311|  33,739|
| |Taylor County|     5| 231.814|  6.623| 1,069| 49561.871| 880.894|  21,569|
| |Union County|     5| 328.149|  9.376|   459| 30124.040| 1575.113|  15,237|
| |Levy County|     5| 120.473|  3.442|   736| 17733.658| 289.136|  41,503|
| |Jefferson County|     5| 350.976|  0.000|   462| 32430.156| 150.418|  14,246|
| |Bradford County|     4| 141.839|  0.000|   554| 19644.693| 607.881|  28,201|
| |Dixie County|     4| 237.727|  0.000|   572| 33995.008| 1256.559|  16,826|
| |Baker County|     4| 136.939|  0.000| 1,059| 36254.707| 2098.107|  29,210|
| |Holmes County|     4| 203.905| 14.565|   524| 26711.526| 276.728|  19,617|
| |Gulf County|     4| 293.277| 20.948|   720| 52789.794| 1581.599|  13,639|
| |Hamilton County|     4| 277.239|  0.000|   629| 43595.786| 168.323|  14,428|
| |Franklin County|     3| 247.423| 11.782|   449| 37030.928| 848.306|  12,125|
| |Glades County|     3| 217.218|  0.000|   419| 30338.136| 217.218|  13,811|
| |Lafayette County|     2| 237.473| 16.962|   777| 92258.371| 10991.621|   8,422|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  0.620|26,565| 16482.606| 27.566|1,611,699|
| |Essex County| 1,194| 1513.243|  0.543|17,930| 22723.989| 41.823| 789,034|
| |Suffolk County| 1,076| 1338.463|  0.889|22,017| 27387.496| 53.311| 803,907|
| |Worcester County| 1,007| 1212.344|  1.376|13,686| 16476.809| 22.530| 830,622|
| |Norfolk County|   997| 1410.633|  0.202|10,682| 15113.721| 25.872| 706,775|
| |Plymouth County|   723| 1387.178|  1.370| 9,288| 17820.346| 20.831| 521,202|
| |Hampden County|   709| 1520.246|  1.838| 7,637| 16375.340| 24.812| 466,372|
| |Bristol County|   637| 1127.001|  1.264| 9,408| 16644.935| 28.560| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,803|  8465.186|  6.037| 212,990|
| |Hampshire County|   130| 808.307|  0.888| 1,184|  7361.811| 19.541| 160,830|
| |Franklin County|    61| 869.194|  0.000|   411|  5856.369|  2.036|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  0.000| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,721| 609.305| N/A|202,641| 15991.466| N/A|12,671,821|
| |Cook County| 4,951| 961.316|  0.860|114,724| 22275.497| 130.979|5,150,233|
| |DuPage County|   525| 568.846|  0.929|12,693| 13753.073| 104.018| 922,921|
| |Lake County|   450| 646.055|  1.025|13,144| 18870.552| 133.928| 696,535|
| |Will County|   348| 503.805|  0.827| 9,692| 14031.268| 132.156| 690,743|
| |Kane County|   305| 572.874|  0.537|10,100| 18970.592| 126.381| 532,403|
| |St. Clair County|   162| 623.830|  1.100| 4,289| 16516.100| 215.645| 259,686|
| |Winnebago County|   134| 474.215|  2.528| 3,835| 13571.762| 40.445| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,335| 10835.873| 98.402| 307,774|
| |Madison County|    85| 323.236|  5.976| 2,969| 11290.433| 271.083| 262,966|
| |Kankakee County|    69| 628.061|  1.300| 1,857| 16903.024| 171.644| 109,862|
| |Rock Island County|    38| 267.834|  4.028| 1,831| 12905.363| 153.048| 141,879|
| |Peoria County|    37| 206.497|  1.595| 1,807| 10084.887| 224.835| 179,179|
| |Sangamon County|    35| 179.790|  1.468| 1,391|  7145.352| 144.566| 194,672|
| |DeKalb County|    32| 305.061|  2.724|   970|  9247.166| 72.180| 104,897|
| |LaSalle County|    28| 257.663|  5.258|   910|  8374.053| 297.101| 108,669|
| |Boone County|    23| 429.553|  0.000|   768| 14343.344| 26.680|  53,544|
| |Kendall County|    23| 178.308|  0.000| 1,443| 11186.914| 110.751| 128,990|
| |Macon County|    23| 221.135|  0.000|   721|  6932.092| 196.412| 104,009|
| |Union County|    23| 1381.133|  0.000|   339| 20356.692| 180.148|  16,653|
| |Coles County|    21| 414.848|  2.822|   564| 11141.621| 327.363|  50,621|
| |Jefferson County|    20| 530.729|  3.791|   320|  8491.668| 276.737|  37,684|
| |Jackson County|    20| 352.423|  2.517|   755| 13303.965| 151.038|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,737|  8283.696| 76.303| 209,689|
| |Clinton County|    17| 452.585|  0.000|   454| 12086.683| 254.817|  37,562|
| |Whiteside County|    17| 308.111|  2.589|   384|  6959.674| 116.512|  55,175|
| |McLean County|    15| 87.455|  0.000|   730|  4256.138| 88.288| 171,517|
| |McDonough County|    15| 505.357|  0.000|   149|  5019.877| 48.129|  29,682|
| |Monroe County|    13| 375.321|  0.000|   339|  9787.222| 140.230|  34,637|
| |Iroquois County|    13| 479.457| 10.538|   276| 10179.243| 100.106|  27,114|
| |Cass County|    11| 905.573|  0.000|   252| 20745.863| 341.060|  12,147|
| |Morgan County|     9| 267.396| 12.733|   353| 10487.848| 526.302|  33,658|
| |Tazewell County|     9| 68.284|  1.084|   653|  4954.364| 181.006| 131,803|
| |Jasper County|     7| 728.408|  0.000|    61|  6347.555| 29.731|   9,610|
| |Williamson County|     7| 105.110|  2.145|   499|  7492.830| 268.137|  66,597|
| |Adams County|     7| 106.976|  4.366|   607|  9276.381| 220.502|  65,435|
| |Randolph County|     7| 220.250|  0.000|   497| 15637.782| 202.271|  31,782|
| |Montgomery County|     7| 246.357|  0.000|   179|  6299.711| 90.499|  28,414|
| |Stephenson County|     6| 134.838|  0.000|   340|  7640.793| 48.156|  44,498|
| |Grundy County|     5| 97.936|  0.000|   368|  7208.054| 170.688|  51,054|
| |Ogle County|     5| 98.730|  0.000|   429|  8471.062| 73.343|  50,643|
| |Christian County|     4| 123.824|  0.000|   146|  4519.564| 53.067|  32,304|
| |Carroll County|     4| 279.623|  0.000|    72|  5033.205| 219.703|  14,305|
| |Bureau County|     4| 122.594|  8.757|   262|  8029.913| 363.404|  32,628|
| |Mercer County|     4| 259.118|  9.254|    76|  4923.236| 27.763|  15,437|
| |Perry County|     3| 143.431| 13.660|   193|  9227.386| 300.522|  20,916|
| |Bond County|     3| 182.637|  0.000|    69|  4200.657| 86.970|  16,426|
| |Macoupin County|     3| 66.776|  0.000|   222|  4941.459| 209.869|  44,926|
| |Douglas County|     3| 154.123|  7.339|   135|  6935.525| 198.158|  19,465|
| |Cumberland County|     3| 278.655| 13.269|    61|  5665.986| 106.154|  10,766|
| |Woodford County|     3| 78.005|  0.000|   171|  4446.293| 137.438|  38,459|
| |Livingston County|     3| 84.156|  4.007|   140|  3927.289| 140.260|  35,648|
| |Fayette County|     3| 140.607|  0.000|    73|  3421.447| 87.043|  21,336|
| |Saline County|     2| 85.139|  0.000|   136|  5789.451| 36.488|  23,491|
| |Clark County|     2| 129.525|  0.000|    91|  5893.401| 111.022|  15,441|
| |Shelby County|     2| 92.447|  6.603|    94|  4345.012| 125.464|  21,634|
| |Vermilion County|     2| 26.400|  0.000|   259|  3418.781| 56.571|  75,758|
| |Wayne County|     2| 123.343|  8.810|    72|  4440.333| 114.532|  16,215|
| |Ford County|     2| 154.309|  0.000|    57|  4397.809| 88.177|  12,961|
| |Gallatin County|     2| 414.250|  0.000|    51| 10563.380| 59.179|   4,828|
| |Jersey County|     2| 91.857|  0.000|   143|  6567.767| 295.254|  21,773|
| |Henry County|     1| 20.444|  0.000|   274|  5601.783| 122.667|  48,913|
| |Franklin County|     1| 25.995|  3.714|   222|  5770.880| 245.095|  38,469|
| |Effingham County|     1| 29.405|  0.000|   208|  6116.208| 289.848|  34,008|
| |Hancock County|     1| 56.472|  0.000|    76|  4291.845| 233.954|  17,708|
| |Jo Daviess County|     1| 47.092|  0.000|   139|  6545.797| 100.912|  21,235|
| |Knox County|     1| 20.121|  0.000|   344|  6921.668| 152.346|  49,699|
| |Lee County|     1| 29.329|  0.000|   191|  5601.830| 108.936|  34,096|
| |Logan County|     1| 34.943|  4.992|   187|  6534.349| 404.341|  28,618|
| |Pulaski County|     1| 187.441| 26.777|   101| 18931.584| 240.996|   5,335|
| |Washington County|     1| 72.010| 10.287|    69|  4968.676| 51.436|  13,887|
| |Richland County|     0|  0.000|  0.000|    24|  1547.090| 55.253|  15,513|
| |Piatt County|     0|  0.000|  0.000|    66|  4038.179| 87.406|  16,344|
| |Moultrie County|     0|  0.000|  0.000|   103|  7102.958| 305.398|  14,501|
| |Menard County|     0|  0.000|  0.000|    60|  4919.646| 81.994|  12,196|
| |Pike County|     0|  0.000|  0.000|    32|  2056.423| 110.166|  15,561|
| |White County|     0|  0.000|  0.000|    80|  5909.729| 168.849|  13,537|
| |Warren County|     0|  0.000|  0.000|   196| 11636.191| 59.368|  16,844|
| |Wabash County|     0|  0.000|  0.000|    49|  4253.472| 186.012|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    32|  6463.341| 461.667|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    18|  2659.574| 21.108|   6,768|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203| 49.785|   5,739|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 102.603|   4,177|
| |Edwards County|     0|  0.000|  0.000|    24|  3752.932| 156.372|   6,395|
| |Edgar County|     0|  0.000|  0.000|    34|  1981.237| 49.947|  17,161|
| |De Witt County|     0|  0.000|  0.000|    39|  2493.925| 54.812|  15,638|
| |Crawford County|     0|  0.000|  0.000|    35|  1874.967| 45.918|  18,667|
| |Clay County|     0|  0.000|  0.000|    32|  2427.184| 130.028|  13,184|
| |Calhoun County|     0|  0.000|  0.000|    12|  2532.180| 90.435|   4,739|
| |Fulton County|     0|  0.000|  0.000|    42|  1223.063| 37.441|  34,340|
| |Brown County|     0|  0.000|  0.000|    15|  2280.328| 43.435|   6,578|
| |Greene County|     0|  0.000|  0.000|    69|  5320.379| 341.474|  12,969|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809|  0.000|   3,821|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Massac County|     0|  0.000|  0.000|    43|  3122.277| 62.238|  13,772|
| |Hamilton County|     0|  0.000|  0.000|    33|  4066.042| 88.010|   8,116|
| |Mason County|     0|  0.000|  0.000|    60|  4491.354| 160.406|  13,359|
| |Marshall County|     0|  0.000|  0.000|    35|  3059.976| 137.387|  11,438|
| |Marion County|     0|  0.000|  0.000|   172|  4623.035| 76.795|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    55|  3508.101| 91.119|  15,678|
| |Johnson County|     0|  0.000|  0.000|    76|  6120.641| 115.050|  12,417|
| |Henderson County|     0|  0.000|  0.000|    21|  3159.795| 236.447|   6,646|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,434| 580.691| N/A|127,732|  9977.512| N/A|12,801,989|
| |Philadelphia County| 1,715| 1082.658| N/A|32,057| 20237.187| N/A|1,584,064|
| |Montgomery County|   859| 1033.800|  0.688|10,307| 12404.398| 50.203| 830,915|
| |Delaware County|   710| 1252.764|  3.277| 9,551| 16852.317| 108.388| 566,747|
| |Bucks County|   583| 927.945|  0.227| 7,344| 11689.242| 44.794| 628,270|
| |Lancaster County|   420| 769.620|  2.618| 6,146| 11262.103| 84.815| 545,724|
| |Berks County|   374| 888.015|  2.035| 5,529| 13127.903| 70.553| 421,164|
| |Chester County|   350| 666.681|  0.272| 5,293| 10082.116| 51.974| 524,989|
| |Lehigh County|   340| 920.616|  1.547| 5,047| 13665.730| 49.899| 369,318|
| |Northampton County|   295| 966.310|  1.404| 3,991| 13073.030| 36.500| 305,285|
| |Allegheny County|   265| 217.920|  2.467| 9,282|  7632.941| 67.314|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,957|  9333.537| 23.847| 209,674|
| |Luzerne County|   185| 582.830|  0.450| 3,576| 11265.937| 75.160| 317,417|
| |Dauphin County|   160| 574.921|  1.027| 2,940| 10564.177| 93.938| 278,299|
| |Monroe County|   125| 734.124|  0.839| 1,657|  9731.546| 32.721| 170,271|
| |York County|   105| 233.823|  3.818| 2,801|  6237.502| 100.528| 449,058|
| |Beaver County|    93| 567.319|  1.743| 1,382|  8430.479| 76.688| 163,929|
| |Cumberland County|    71| 280.223|  0.000| 1,353|  5340.017| 43.415| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,640| 11566.156| 46.345| 141,793|
| |Schuylkill County|    51| 360.784|  1.011|   938|  6635.587| 30.318| 141,359|
| |Westmoreland County|    47| 134.709|  0.409| 1,593|  4565.791| 38.079| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,407|  9075.838| 72.798| 155,027|
| |Columbia County|    35| 538.760|  0.000|   483|  7434.887| 28.587|  64,964|
| |Carbon County|    28| 436.259|  0.000|   382|  5951.824| 31.161|  64,182|
| |Erie County|    27| 100.101|  4.767| 1,182|  4382.192| 65.675| 269,728|
| |Susquehanna County|    27| 669.510|  0.000|   219|  5430.470| 21.254|  40,328|
| |Adams County|    22| 213.574|  2.774|   544|  5281.092| 65.182| 103,009|
| |Pike County|    21| 376.283|  0.000|   527|  9442.921|  2.560|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   430|  3795.267| 76.914| 113,299|
| |Butler County|    17| 90.496|  1.521|   710|  3779.551| 49.431| 187,853|
| |Northumberland County|    17| 187.136|  7.863|   526|  5790.209| 121.088|  90,843|
| |Washington County|    16| 77.345|  2.762|   891|  4307.157| 48.341| 206,865|
| |Lawrence County|    16| 187.108|  1.671|   420|  4911.591| 51.789|  85,512|
| |Mercer County|    12| 109.665|  3.917|   480|  4386.606| 99.221| 109,424|
| |Centre County|    11| 67.740|  0.880|   386|  2377.067| 15.835| 162,385|
| |Wayne County|    10| 194.700|  2.781|   162|  3154.144| 11.126|  51,361|
| |Wyoming County|     8| 298.574|  0.000|    63|  2351.273| 26.658|  26,794|
| |Blair County|     8| 65.666|  3.518|   317|  2602.008| 60.975| 121,829|
| |Armstrong County|     8| 123.581|  4.414|   242|  3738.318| 83.858|  64,735|
| |Indiana County|     7| 83.261|  1.699|   351|  4174.943| 71.367|  84,073|
| |Fayette County|     6| 46.413|  1.105|   609|  4710.924| 151.395| 129,274|
| |Juniata County|     6| 242.297|  0.000|   137|  5532.448| 34.614|  24,763|
| |Huntingdon County|     5| 110.757|  3.164|   320|  7088.428| 63.290|  45,144|
| |Clinton County|     5| 129.426|  0.000|   128|  3313.315| 33.281|  38,632|
| |Perry County|     5| 108.057|  0.000|   132|  2852.697| 33.961|  46,272|
| |Bedford County|     4| 83.528|  0.000|   150|  3132.309| 35.798|  47,888|
| |Montour County|     3| 164.564|  0.000|   106|  5814.591| 47.018|  18,230|
| |Somerset County|     3| 40.846|  0.000|   140|  1906.136| 21.395|  73,447|
| |Bradford County|     3| 49.732|  0.000|    92|  1525.123| 16.577|  60,323|
| |Tioga County|     3| 73.908|  0.000|    41|  1010.076| 14.078|  40,591|
| |Cambria County|     3| 23.043|  0.000|   365|  2803.552| 40.599| 130,192|
| |Snyder County|     2| 49.539|  0.000|   116|  2873.279| 53.078|  40,372|
| |Clarion County|     2| 52.032|  0.000|    84|  2185.337| 22.299|  38,438|
| |Fulton County|     2| 137.646|  0.000|    28|  1927.047| 19.664|  14,530|
| |Elk County|     2| 66.867|  0.000|    54|  1805.416| 28.657|  29,910|
| |Union County|     2| 44.521|  0.000|   279|  6210.627| 200.343|  44,923|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  0.000|  40,625|
| |Crawford County|     1| 11.816|  0.000|   165|  1949.686| 43.889|  84,629|
| |Greene County|     1| 27.599|  0.000|   123|  3394.695| 43.370|  36,233|
| |Jefferson County|     1| 23.028|  0.000|    75|  1727.116| 42.767|  43,425|
| |Warren County|     1| 25.516|  0.000|    22|   561.353|  0.000|  39,191|
| |Clearfield County|     1| 12.618|  1.803|   186|  2346.855| 54.075|  79,255|
| |Mifflin County|     1| 21.674|  0.000|   122|  2644.241| 18.578|  46,138|
| |Potter County|     0|  0.000|  0.000|    21|  1270.725|  8.644|  16,526|
| |Venango County|     0|  0.000|  0.000|    67|  1322.334| 11.278|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Cameron County|     0|  0.000|  0.000|     8|  1798.966| 64.249|   4,447|
| |Forest County|     0|  0.000|  0.000|    12|  1655.858| 59.138|   7,247|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,490| 649.854| N/A|95,790|  9591.606| N/A|9,986,857|
| |Wayne County| 2,835| 1620.608|  0.653|28,877| 16507.340| 75.294|1,749,343|
| |Oakland County| 1,136| 903.319|  0.341|16,236| 12910.470| 107.235|1,257,584|
| |Macomb County|   950| 1086.991|  0.981|11,084| 12682.328| 143.679| 873,972|
| |Genesee County|   299| 736.793|  1.408| 3,717|  9159.391| 30.626| 405,813|
| |Kent County|   157| 238.981|  0.000| 7,702| 11723.786| 55.233| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,152| 11294.276| 149.201| 190,539|
| |Washtenaw County|   114| 310.119|  0.777| 2,659|  7233.386| 57.127| 367,601|
| |Kalamazoo County|    84| 316.902|  0.539| 1,705|  6432.360| 46.889| 265,066|
| |Berrien County|    67| 436.764|  0.931| 1,429|  9315.454| 76.364| 153,401|
| |Muskegon County|    61| 351.451|  1.646| 1,209|  6965.650| 40.330| 173,566|
| |Ottawa County|    59| 202.172|  1.958| 1,893|  6486.653| 51.889| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   841|  5285.054| 32.319| 159,128|
| |Calhoun County|    43| 320.515|  2.130|   829|  6179.235| 50.047| 134,159|
| |Bay County|    35| 339.391|  5.541|   697|  6758.722| 134.371| 103,126|
| |Jackson County|    34| 214.498|  0.000|   734|  4630.623| 22.531| 158,510|
| |Lapeer County|    33| 376.682|  0.000|   490|  5593.160| 47.289|  87,607|
| |Ingham County|    32| 109.437|  0.977| 1,597|  5461.584| 29.802| 292,406|
| |Tuscola County|    29| 555.077|  0.000|   377|  7216.002| 117.578|  52,245|
| |Livingston County|    28| 145.837|  0.000|   880|  4583.453| 47.620| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   351|  5152.520| 27.262|  68,122|
| |Monroe County|    25| 166.113|  0.000| 1,050|  6976.744| 90.176| 150,500|
| |Hillsdale County|    25| 548.186|  0.000|   281|  6161.605| 65.782|  45,605|
| |Gratiot County|    15| 368.451|  0.000|   162|  3979.269| 28.072|  40,711|
| |Cass County|    14| 270.338|  0.000|   348|  6719.833| 88.274|  51,787|
| |Alpena County|    13| 457.666|  0.000|   129|  4541.454| 10.059|  28,405|
| |Clinton County|    13| 163.327|  0.000|   431|  5414.913| 16.153|  79,595|
| |Lenawee County|    12| 121.888|  0.000|   466|  4733.319| 68.199|  98,451|
| |Iosco County|    12| 477.574|  0.000|   136|  5412.504| 34.112|  25,127|
| |Otsego County|    11| 445.922|  5.791|   135|  5472.677|  5.791|  24,668|
| |Marquette County|    11| 164.920|  0.000|   184|  2758.662| 68.538|  66,699|
| |Midland County|    10| 120.256|  0.000|   352|  4233.008| 46.384|  83,156|
| |Van Buren County|    10| 132.141|  0.000|   491|  6488.101| 96.274|  75,677|
| |St. Joseph County|    10| 164.031|  4.687|   618| 10137.130| 89.046|  60,964|
| |Isabella County|     9| 128.807|  0.000|   221|  3162.926| 30.668|  69,872|
| |Eaton County|     8| 72.551|  0.000|   471|  4271.411| 19.433| 110,268|
| |Ionia County|     7| 108.197|  2.208|   277|  4281.497|  6.624|  64,697|
| |Sanilac County|     6| 145.737|  0.000|   111|  2696.138| 17.350|  41,170|
| |Allegan County|     6| 50.813|  0.000|   549|  4649.351| 47.183| 118,081|
| |Oceana County|     6| 226.697|  0.000|   484| 18286.923| 53.976|  26,467|
| |Crawford County|     5| 356.405|  0.000|   108|  7698.339| 30.549|  14,029|
| |Grand Traverse County|     5| 53.713|  0.000|   235|  2524.493| 42.970|  93,088|
| |Wexford County|     4| 118.938|  0.000|    71|  2111.147|  4.248|  33,631|
| |Huron County|     4| 129.111|  0.000|   166|  5358.123| 46.111|  30,981|
| |Kalkaska County|     4| 221.754|  0.000|    54|  2993.680| 23.759|  18,038|
| |Clare County|     3| 96.931|  0.000|    80|  2584.814| 46.157|  30,950|
| |Delta County|     3| 83.836|  0.000|   111|  3101.945| 87.829|  35,784|
| |Arenac County|     3| 201.572|  0.000|    47|  3157.965| 57.592|  14,883|
| |Ogemaw County|     3| 142.878|  6.804|    54|  2571.796|  6.804|  20,997|
| |Branch County|     2| 45.959|  0.000|   378|  8686.261| 75.504|  43,517|
| |Barry County|     2| 32.494|  0.000|   195|  3168.156| 46.420|  61,550|
| |Dickinson County|     2| 79.242|  0.000|    59|  2337.652| 39.621|  25,239|
| |Charlevoix County|     2| 76.502|  0.000|    51|  1950.809| 32.787|  26,143|
| |Cheboygan County|     2| 79.126|  0.000|    54|  2136.414| 56.519|  25,276|
| |Emmet County|     2| 59.853|  0.000|    72|  2154.721| 47.028|  33,415|
| |Gladwin County|     2| 78.589|  0.000|    63|  2475.539| 28.067|  25,449|
| |Roscommon County|     2| 83.267| 11.895|    57|  2373.121| 29.738|  24,019|
| |Montcalm County|     2| 31.305|  2.236|   201|  3146.131| 35.777|  63,888|
| |Mecosta County|     2| 46.027|  0.000|    71|  1633.949| 16.438|  43,453|
| |Presque Isle County|     1| 79.416|  0.000|    21|  1667.726| 22.690|  12,592|
| |Missaukee County|     1| 66.146|  0.000|    42|  2778.145|  9.449|  15,118|
| |Manistee County|     1| 40.720|  5.817|    42|  1710.237| 40.720|  24,558|
| |Benzie County|     1| 56.287|  0.000|    35|  1970.055| 48.246|  17,766|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Oscoda County|     1| 121.344|  0.000|    26|  3154.957| 34.670|   8,241|
| |Gogebic County|     1| 71.556|  0.000|   132|  9445.438| 224.891|  13,975|
| |Iron County|     1| 90.367|  0.000|    20|  1807.338| 12.910|  11,066|
| |Alger County|     0|  0.000|  0.000|    17|  1866.491| 125.478|   9,108|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Chippewa County|     0|  0.000|  0.000|    44|  1178.077| 19.125|  37,349|
| |Antrim County|     0|  0.000|  0.000|    42|  1800.720|  6.125|  23,324|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128|  0.000|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Ontonagon County|     0|  0.000|  0.000|    21|  3671.329| 349.650|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   263|  5369.539| 37.916|  48,980|
| |Montmorency County|     0|  0.000|  0.000|     8|   857.633|  0.000|   9,328|
| |Menominee County|     0|  0.000|  0.000|   165|  7243.196| 257.118|  22,780|
| |Mason County|     0|  0.000|  0.000|   104|  3568.488| 24.509|  29,144|
| |Mackinac County|     0|  0.000|  0.000|    27|  2500.232| 13.229|  10,799|
| |Luce County|     0|  0.000|  0.000|    23|  3692.406| 458.684|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    74|  3400.579| 32.824|  21,761|
| |Lake County|     0|  0.000|  0.000|    28|  2362.271| 108.472|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    53|  1485.260| 16.014|  35,684|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,467| 420.724| N/A|212,563| 20020.206| N/A|10,617,423|
| |Fulton County|   463| 435.176|  5.774|21,601| 20302.894| 262.368|1,063,937|
| |Cobb County|   334| 439.392|  3.195|14,690| 19325.362| 308.401| 760,141|
| |Gwinnett County|   283| 302.270|  4.425|21,175| 22616.822| 303.338| 936,250|
| |DeKalb County|   254| 334.520|  3.198|14,746| 19420.596| 232.734| 759,297|
| |Dougherty County|   172| 1955.523|  3.248| 2,786| 31674.928| 203.024|  87,956|
| |Clayton County|   115| 393.491|  4.888| 5,380| 18408.519| 244.893| 292,256|
| |Muscogee County|   107| 546.563|  9.486| 4,992| 25499.441| 289.700| 195,769|
| |Hall County|   104| 508.704|  8.385| 6,420| 31402.703| 330.518| 204,441|
| |Richmond County|    96| 474.032|  5.643| 4,829| 23844.794| 499.427| 202,518|
| |Chatham County|    91| 314.411|  8.391| 6,146| 21234.841| 306.020| 289,430|
| |Bibb County|    79| 515.804| 11.193| 3,951| 25796.721| 445.849| 153,159|
| |Troup County|    74| 1058.322| 10.215| 2,380| 34037.928| 251.300|  69,922|
| |Cherokee County|    66| 255.050|  2.760| 3,861| 14920.413| 326.817| 258,773|
| |Bartow County|    64| 594.034|  3.978| 1,999| 18554.271| 242.652| 107,738|
| |Houston County|    62| 392.746|  7.240| 2,133| 13511.716| 212.662| 157,863|
| |Henry County|    56| 238.744|  5.481| 3,588| 15296.661| 204.638| 234,561|
| |Douglas County|    56| 382.663|  5.857| 2,838| 19392.796| 282.116| 146,343|
| |Sumter County|    56| 1896.762|  0.000|   778| 26351.443| 140.322|  29,524|
| |Glynn County|    55| 644.844| 13.399| 2,698| 31632.509| 415.380|  85,292|
| |Carroll County|    52| 433.362|  3.572| 1,997| 16642.776| 184.536| 119,992|
| |Habersham County|    51| 1125.132|  9.455| 1,188| 26208.966| 198.553|  45,328|
| |Lowndes County|    50| 425.873| 12.168| 3,237| 27570.993| 149.664| 117,406|
| |Upson County|    49| 1861.702| 16.283|   620| 23556.231| 613.330|  26,320|
| |Newton County|    46| 411.655|  8.949| 1,944| 17396.907| 265.914| 111,744|
| |Thomas County|    44| 989.854|  6.428| 1,165| 26208.634| 260.319|  44,451|
| |Tift County|    44| 1082.571| 28.119| 1,390| 34199.390| 270.643|  40,644|
| |Spalding County|    43| 644.649|  4.283| 1,019| 15276.674| 227.019|  66,703|
| |Baldwin County|    43| 957.897| 15.912| 1,130| 25172.644| 340.515|  44,890|
| |Walton County|    41| 433.436|  3.020| 1,233| 13034.791| 235.596|  94,593|
| |Mitchell County|    41| 1875.314|  0.000|   660| 30187.989| 117.616|  21,863|
| |Butts County|    40| 1604.107| 17.187|   502| 20131.537| 114.579|  24,936|
| |Hancock County|    35| 4138.583|  0.000|   336| 39730.401| 472.981|   8,457|
| |Whitfield County|    34| 324.961|  6.827| 3,678| 35153.114| 353.634| 104,628|
| |Barrow County|    33| 396.444|  1.716| 1,391| 16710.716| 241.985|  83,240|
| |Fayette County|    33| 288.409|  6.243| 1,243| 10863.390| 206.006| 114,421|
| |Ware County|    32| 895.506| 27.985| 1,201| 33609.448| 303.832|  35,734|
| |Early County|    32| 3140.334|  0.000|   377| 36997.056| 308.426|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   307| 35986.403| 200.948|   8,531|
| |Coffee County|    30| 693.273| 16.506| 1,566| 36188.848| 439.073|  43,273|
| |Columbia County|    29| 185.050|  6.381| 2,511| 16022.819| 343.665| 156,714|
| |Monroe County|    29| 1051.563| 20.720|   486| 17622.743| 217.565|  27,578|
| |Coweta County|    26| 175.074|  3.848| 1,688| 11366.314| 214.513| 148,509|
| |Randolph County|    26| 3835.940|  0.000|   278| 41015.049| 210.766|   6,778|
| |Forsyth County|    26| 106.447|  2.340| 2,507| 10263.990| 212.895| 244,252|
| |Rockdale County|    26| 286.041| 14.145| 1,439| 15831.280| 265.610|  90,896|
| |Paulding County|    25| 148.221|  2.541| 1,851| 10974.287| 199.887| 168,667|
| |Colquitt County|    24| 526.316|  6.266| 1,593| 34934.211| 191.103|  45,600|
| |Jenkins County|    24| 2766.252|  0.000|   258| 29737.206| 279.918|   8,676|
| |Worth County|    23| 1135.971|  0.000|   465| 22966.365| 176.393|  20,247|
| |Lee County|    23| 766.871|  4.763|   597| 19905.308| 319.133|  29,992|
| |Gordon County|    23| 396.805|  0.000| 1,310| 22600.625| 409.128|  57,963|
| |Clarke County|    21| 163.639|  3.340| 2,209| 17213.300| 268.279| 128,331|
| |Appling County|    19| 1033.395|  0.000|   765| 41607.745| 1041.165|  18,386|
| |Wilcox County|    19| 2200.347| 16.544|   192| 22235.090| 264.703|   8,635|
| |Turner County|    18| 2254.227|  0.000|   261| 32686.287| 357.814|   7,985|
| |Floyd County|    18| 182.745|  1.450| 1,751| 17777.011| 468.465|  98,498|
| |Putnam County|    18| 813.780|  0.000|   465| 21022.650| 368.139|  22,119|
| |Jackson County|    17| 232.950|  5.873| 1,148| 15730.984| 211.417|  72,977|
| |Bulloch County|    17| 213.546|  5.384| 1,365| 17146.518| 296.094|  79,608|
| |Harris County|    17| 482.461|  4.054|   676| 19184.925| 125.683|  35,236|
| |Brooks County|    17| 1099.825|  0.000|   421| 27236.851| 277.267|  15,457|
| |Laurens County|    17| 357.548| 27.041| 1,086| 22841.038| 664.019|  47,546|
| |Peach County|    16| 580.847| 20.745|   428| 15537.646| 331.912|  27,546|
| |Decatur County|    16| 605.969| 32.463|   845| 32002.727| 513.991|  26,404|
| |Walker County|    16| 229.355|  0.000|   791| 11338.714| 272.358|  69,761|
| |Crisp County|    15| 670.481|  6.386|   405| 18102.986| 217.108|  22,372|
| |Oconee County|    15| 372.393|  0.000|   464| 11519.364| 124.131|  40,280|
| |Dooly County|    14| 1045.556|  0.000|   262| 19566.841| 149.365|  13,390|
| |Stephens County|    14| 540.019| 11.021|   679| 26190.935| 440.832|  25,925|
| |Lamar County|    13| 681.449| 14.977|   288| 15096.713| 142.281|  19,077|
| |Telfair County|    12| 756.620| 45.037|   299| 18852.459| 225.185|  15,860|
| |Wilkinson County|    12| 1340.183| 15.955|   234| 26133.572| 462.682|   8,954|
| |Greene County|    12| 654.879|  0.000|   348| 18991.487| 397.605|  18,324|
| |Johnson County|    12| 1244.426| 14.815|   256| 26547.755| 281.477|   9,643|
| |Wayne County|    12| 400.976| 19.094|   857| 28636.348| 644.425|  29,927|
| |Emanuel County|    11| 485.737| 12.617|   566| 24993.376| 611.902|  22,646|
| |Polk County|    11| 258.137|  0.000|   927| 21753.925| 543.094|  42,613|
| |Catoosa County|    11| 162.770|  4.228|   699| 10343.297| 190.251|  67,580|
| |Bleckley County|    10| 776.820| 44.390|   264| 20508.040| 921.086|  12,873|
| |McDuffie County|    10| 469.219|  0.000|   399| 18721.847| 455.813|  21,312|
| |Macon County|    10| 772.380|  0.000|   187| 14443.500| 110.340|  12,947|
| |Screven County|     9| 644.422|  0.000|   223| 15967.349| 347.783|  13,966|
| |Stewart County|     9| 1359.311| 64.729|   258| 38966.923| 64.729|   6,621|
| |Jefferson County|     9| 585.861| 18.599|   545| 35477.151| 641.658|  15,362|
| |Toombs County|     9| 335.445| 10.649|   841| 31345.509| 697.513|  26,830|
| |Pierce County|     9| 462.368| 14.678|   434| 22296.429| 308.246|  19,465|
| |Hart County|     8| 305.285| 10.903|   336| 12821.981| 239.867|  26,205|
| |Bacon County|     8| 716.589| 25.592|   462| 41383.017| 447.868|  11,164|
| |Bryan County|     8| 201.883|  0.000|   717| 18093.724| 299.219|  39,627|
| |Jeff Davis County|     8| 529.276|  0.000|   505| 33410.519| 718.303|  15,115|
| |Lumpkin County|     8| 238.024|  8.501|   394| 11722.702| 284.779|  33,610|
| |Haralson County|     7| 234.962|  4.795|   241|  8089.420| 163.035|  29,792|
| |Candler County|     7| 647.968| 39.672|   277| 25641.026| 423.163|  10,803|
| |Madison County|     7| 234.270|  9.562|   437| 14625.167| 296.424|  29,880|
| |Burke County|     7| 312.737|  0.000|   518| 23142.564| 427.620|  22,383|
| |Grady County|     7| 284.172| 11.599|   543| 22043.600| 417.558|  24,633|
| |Oglethorpe County|     7| 458.746|  0.000|   243| 15925.028| 299.589|  15,259|
| |Meriwether County|     7| 330.703|  6.749|   421| 19889.451| 283.460|  21,167|
| |Liberty County|     7| 113.942|  9.301|   789| 12842.842| 218.582|  61,435|
| |Union County|     7| 285.586|  0.000|   324| 13218.555| 396.324|  24,511|
| |White County|     6| 194.818|  4.639|   381| 12370.933| 157.710|  30,798|
| |Franklin County|     6| 256.970|  0.000|   443| 18972.975| 324.272|  23,349|
| |Brantley County|     6| 313.988| 14.952|   269| 14077.136| 201.850|  19,109|
| |Cook County|     6| 347.423|  0.000|   462| 26751.592| 297.791|  17,270|
| |Calhoun County|     6| 969.462|  0.000|   211| 34092.745| 230.824|   6,189|
| |Pickens County|     6| 184.100|  4.383|   434| 13316.560| 315.600|  32,591|
| |Pike County|     6| 316.422| 15.068|   239| 12604.156| 271.219|  18,962|
| |Lincoln County|     5| 631.233| 18.035|   164| 20704.457| 541.057|   7,921|
| |Banks County|     5| 259.956|  7.427|   290| 15077.467| 230.247|  19,234|
| |Heard County|     5| 419.358| 11.982|   151| 12664.598| 131.798|  11,923|
| |Marion County|     5| 598.158| 17.090|   161| 19260.677| 239.263|   8,359|
| |Camden County|     5| 91.465|  0.000|   831| 15201.405| 277.007|  54,666|
| |Dawson County|     5| 191.512| 10.944|   458| 17542.516| 541.706|  26,108|
| |Fannin County|     5| 190.927| 10.910|   362| 13823.125| 267.298|  26,188|
| |Effingham County|     5| 77.765|  6.666|   793| 12333.582| 199.968|  64,296|
| |Ben Hill County|     5| 299.401| 17.109|   509| 30479.042| 992.301|  16,700|
| |Seminole County|     5| 618.047|  0.000|   231| 28553.770| 812.290|   8,090|
| |Lanier County|     4| 383.767|  0.000|   227| 21778.759| 178.177|  10,423|
| |Gilmer County|     4| 127.514|  0.000|   665| 21199.273| 373.435|  31,369|
| |Chattooga County|     4| 161.362|  5.763|   349| 14078.825| 622.396|  24,789|
| |Clinch County|     4| 604.412|  0.000|   212| 32033.847| 518.068|   6,618|
| |Jones County|     4| 139.203|  4.972|   331| 11519.053| 169.032|  28,735|
| |Twiggs County|     4| 492.611| 17.593|   131| 16133.005| 351.865|   8,120|
| |Wilkes County|     3| 306.843|  0.000|   197| 20149.330| 146.116|   9,777|
| |Atkinson County|     3| 367.422| 17.496|   339| 41518.677| 472.400|   8,165|
| |Treutlen County|     3| 434.720|  0.000|   137| 19852.195| 496.822|   6,901|
| |Taylor County|     3| 374.065| 17.813|   102| 12718.204| 374.065|   8,020|
| |Talbot County|     3| 484.262|  0.000|   145| 23405.973| 253.661|   6,195|
| |Rabun County|     3| 175.060|  0.000|   231| 13479.606| 158.387|  17,137|
| |Pulaski County|     3| 269.372| 12.827|   135| 12121.756| 500.263|  11,137|
| |Murray County|     3| 74.820|  3.563|   643| 16036.512| 242.276|  40,096|
| |Baker County|     3| 987.492|  0.000|    70| 23041.475| 329.164|   3,038|
| |McIntosh County|     3| 208.652|  9.936|   203| 14118.793| 357.689|  14,378|
| |Evans County|     3| 281.584| 26.818|   304| 28533.884| 831.344|  10,654|
| |Dodge County|     3| 145.596|  0.000|   246| 11938.850| 256.526|  20,605|
| |Charlton County|     3| 224.014|  0.000|   451| 33676.822| 416.027|  13,392|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724|  0.000|   2,607|
| |Washington County|     2| 98.164|  0.000|   529| 25964.465| 525.880|  20,374|
| |Jasper County|     2| 140.657| 10.047|   175| 12307.476| 221.032|  14,219|
| |Dade County|     2| 124.100|  8.864|   147|  9121.370| 221.608|  16,116|
| |Long County|     2| 102.255|  7.304|   141|  7208.958| 167.990|  19,559|
| |Montgomery County|     2| 218.055|  0.000|   163| 17771.478| 233.630|   9,172|
| |Towns County|     2| 166.154| 11.868|   155| 12876.963| 249.232|  12,037|
| |Echols County|     2| 499.251|  0.000|   226| 56415.377| 213.965|   4,006|
| |Tattnall County|     2| 79.095|  5.650|   578| 22858.499| 536.717|  25,286|
| |Chattahoochee County|     2| 183.368| 13.098|   794| 72797.286| 759.669|  10,907|
| |Clay County|     2| 705.716|  0.000|   100| 35285.815| 705.716|   2,834|
| |Elbert County|     1| 52.100|  0.000|   381| 19849.953| 245.612|  19,194|
| |Berrien County|     1| 51.554|  7.365|   329| 16961.386| 353.516|  19,397|
| |Warren County|     1| 190.331|  0.000|    89| 16939.475| 570.994|   5,254|
| |Wheeler County|     1| 127.307|  0.000|   101| 12858.052| 218.241|   7,855|
| |Glascock County|     1| 336.587| 48.084|    26|  8751.262| 96.168|   2,971|
| |Schley County|     1| 190.223|  0.000|    79| 15027.582| 434.794|   5,257|
| |Quitman County|     1| 434.972|  0.000|    31| 13484.124| 124.278|   2,299|
| |Irwin County|     1| 106.202|  0.000|   178| 18903.993| 273.091|   9,416|
| |Taliaferro County|     0|  0.000|  0.000|    15|  9759.271| 278.836|   1,537|
| |Morgan County|     0|  0.000|  0.000|   308| 15978.419| 407.613|  19,276|
| |Miller County|     0|  0.000|  0.000|   157| 27457.153| 549.643|   5,718|
| |Crawford County|     0|  0.000|  0.000|   112|  9029.345| 126.687|  12,404|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,453| 1248.988| N/A|50,681| 14215.125| N/A|3,565,287|
| |Hartford County| 1,419| 1591.307|  0.641|12,871| 14433.903| 17.622| 891,720|
| |Fairfield County| 1,410| 1494.702|  0.303|18,160| 19250.911| 30.894| 943,332|
| |New Haven County| 1,109| 1297.445|  0.836|13,316| 15578.697| 28.580| 854,757|
| |Middlesex County|   192| 1182.004|  0.000| 1,414|  8704.967| 15.830| 162,436|
| |Litchfield County|   139| 770.796|  0.792| 1,632|  9049.924| 17.428| 180,333|
| |New London County|   104| 392.148|  0.539| 1,477|  5569.256| 23.701| 265,206|
| |Tolland County|    65| 431.260|  0.000| 1,056|  7006.323|  0.000| 150,721|
| |Windham County|    15| 128.444|  0.000|   755|  6465.037| 35.475| 116,782|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,422| 607.525| N/A|191,721| 26339.944| N/A|7,278,717|
| |Maricopa County| 2,536| 565.388|  7.293|128,352| 28615.419| 109.179|4,485,414|
| |Pima County|   524| 500.344|  5.729|19,164| 18298.849| 227.392|1,047,279|
| |Yuma County|   292| 1365.845|  8.019|11,766| 55036.087| 212.495| 213,787|
| |Navajo County|   205| 1848.112|  7.727| 5,446| 49096.679| 121.061| 110,924|
| |Mohave County|   181| 853.045| 10.772| 3,294| 15524.481| 98.972| 212,181|
| |Pinal County|   166| 358.695|  2.778| 8,665| 18723.436| 104.336| 462,789|
| |Apache County|   140| 1947.501|  3.974| 3,221| 44806.432| 139.107|  71,887|
| |Coconino County|   119| 829.407|  1.991| 3,149| 21947.922| 83.638| 143,476|
| |Yavapai County|    72| 306.254|  3.038| 2,105|  8953.675| 84.463| 235,099|
| |Cochise County|    57| 452.661|  5.672| 1,751| 13905.434| 201.939| 125,922|
| |Santa Cruz County|    55| 1182.847|  9.217| 2,696| 57980.988| 138.255|  46,498|
| |Gila County|    42| 777.519| 10.578|   982| 18179.125| 251.239|  54,018|
| |Graham County|    20| 514.973| 25.749|   584| 15037.207| 202.311|  38,837|
| |La Paz County|    12| 568.505|  0.000|   489| 23166.572| 74.447|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,307| 926.477| N/A|136,499| 29362.239| N/A|4,648,794|
| |Orleans Parish|   566| 1450.746|  1.465|10,939| 28038.365| 110.582| 390,144|
| |Jefferson Parish|   530| 1225.453|  2.312|15,703| 36308.102| 198.187| 432,493|
| |East Baton Rouge Parish|   372| 845.341|  9.090|12,716| 28896.125| 249.966| 440,059|
| |Caddo Parish|   297| 1236.449|  2.379| 6,887| 28671.463| 164.741| 240,204|
| |St. Tammany Parish|   218| 837.112|  3.840| 5,480| 21043.011| 216.135| 260,419|
| |Calcasieu Parish|   154| 756.995|  5.618| 7,013| 34472.758| 183.280| 203,436|
| |Rapides Parish|   123| 948.723|  9.917| 3,447| 26587.375| 246.822| 129,648|
| |Ouachita Parish|   117| 763.314|  5.592| 5,067| 33057.366| 260.962| 153,279|
| |Lafourche Parish|   104| 1065.421| 10.244| 2,949| 30210.830| 278.063|  97,614|
| |Lafayette Parish|   100| 409.182|  5.261| 7,916| 32390.851| 261.877| 244,390|
| |St. Landry Parish|    93| 1132.434| 13.916| 2,866| 34898.446| 408.789|  82,124|
| |St. John the Baptist Parish|    93| 2171.020|  3.335| 1,455| 33965.964| 173.415|  42,837|
| |Acadia Parish|    89| 1434.443| 23.025| 2,684| 43258.925| 262.482|  62,045|
| |Terrebonne Parish|    86| 778.555|  1.293| 3,160| 28607.382| 225.031| 110,461|
| |Bossier Parish|    82| 645.471|  3.374| 2,445| 19246.058| 150.685| 127,039|
| |Tangipahoa Parish|    80| 593.657|  8.481| 3,664| 27189.480| 283.047| 134,758|
| |Ascension Parish|    79| 623.993|  9.027| 3,016| 23822.312| 245.986| 126,604|
| |Iberia Parish|    75| 1074.037| 10.229| 2,602| 37261.922| 310.959|  69,830|
| |St. Mary Parish|    59| 1195.591| 20.264| 1,666| 33760.233| 356.072|  49,348|
| |Washington Parish|    58| 1255.574|  0.000| 1,320| 28575.140| 225.756|  46,194|
| |St. Charles Parish|    54| 1016.949|  8.071| 1,526| 28738.230| 225.989|  53,100|
| |Livingston Parish|    54| 383.553|  3.044| 3,071| 21812.784| 229.320| 140,789|
| |Iberville Parish|    50| 1537.941| 13.182| 1,279| 39340.531| 263.647|  32,511|
| |St. Martin Parish|    47| 879.639| 10.695| 1,784| 33388.857| 449.177|  53,431|
| |East Feliciana Parish|    39| 2038.150| 22.397|   619| 32349.099| 388.219|  19,135|
| |West Baton Rouge Parish|    37| 1398.073|  0.000|   754| 28490.459| 286.092|  26,465|
| |Avoyelles Parish|    36| 896.772| 17.793| 1,138| 28347.947| 416.358|  40,144|
| |Union Parish|    35| 1583.137| 12.924|   737| 33336.349| 400.631|  22,108|
| |Lincoln Parish|    34| 727.397| 15.281|   839| 17949.596| 223.109|  46,742|
| |Pointe Coupee Parish|    33| 1518.638|  6.574|   838| 38564.197| 381.303|  21,730|
| |Allen Parish|    32| 1248.683| 16.723| 1,367| 53342.178| 680.086|  25,627|
| |St. James Parish|    32| 1516.875|  0.000|   734| 34793.326| 277.642|  21,096|
| |Vernon Parish|    30| 632.524|  9.036|   806| 16993.822| 174.697|  47,429|
| |Bienville Parish|    30| 2265.690|  0.000|   390| 29453.969| 280.514|  13,241|
| |Jefferson Davis Parish|    29| 924.509| 13.663| 1,071| 34143.076| 300.579|  31,368|
| |Vermilion Parish|    28| 470.501|  9.602| 1,714| 28801.398| 444.096|  59,511|
| |De Soto Parish|    27| 983.141|  5.202|   765| 27855.660| 286.099|  27,463|
| |St. Bernard Parish|    24| 508.001|  0.000| 1,126| 23833.714| 105.834|  47,244|
| |Beauregard Parish|    21| 560.045| 15.239|   878| 23415.207| 224.780|  37,497|
| |Grant Parish|    21| 937.961| 31.903|   350| 15632.677| 331.796|  22,389|
| |Assumption Parish|    20| 913.617|  0.000|   606| 27682.609| 189.249|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   469| 20218.132| 110.852|  23,197|
| |Jackson Parish|    19| 1206.809|  9.074|   397| 25215.955| 263.139|  15,744|
| |Franklin Parish|    19| 949.288| 14.275|   980| 48963.278| 599.550|  20,015|
| |West Feliciana Parish|    18| 1156.218| 18.353|   399| 25629.496| 495.522|  15,568|
| |Natchitoches Parish|    17| 445.516|  0.000|   823| 21568.216| 232.118|  38,158|
| |Webster Parish|    16| 417.319|  7.452|   939| 24491.393| 264.550|  38,340|
| |Red River Parish|    14| 1658.375| 50.767|   276| 32693.674| 1083.020|   8,442|
| |Morehouse Parish|    14| 562.837| 17.230|   549| 22071.239| 315.878|  24,874|
| |Sabine Parish|    11| 460.559|  5.981|   682| 28554.681| 358.877|  23,884|
| |Claiborne Parish|    11| 701.978|  0.000|   292| 18634.333| 373.781|  15,670|
| |Evangeline Parish|     9| 269.501| 21.389|   958| 28686.929| 414.947|  33,395|
| |Concordia Parish|     9| 467.314|  0.000|   356| 18484.864| 393.137|  19,259|
| |Richland Parish|     8| 397.575|  7.100|   635| 31557.499| 347.878|  20,122|
| |West Carroll Parish|     7| 646.353| 26.382|   307| 28347.184| 263.817|  10,830|
| |Winn Parish|     7| 503.452|  0.000|   467| 33587.457| 554.825|  13,904|
| |Madison Parish|     6| 547.895|  0.000|   631| 57620.309| 286.993|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   312| 32862.861| 481.507|   9,494|
| |LaSalle Parish|     3| 201.450|  9.593|   339| 22763.900| 537.201|  14,892|
| |Caldwell Parish|     3| 302.480| 14.404|   234| 23593.466| 316.884|   9,918|
| |East Carroll Parish|     2| 291.503| 20.822|   520| 75790.701| 41.643|   6,861|
| |St. Helena Parish|     2| 197.394| 14.100|   280| 27635.215| 310.191|  10,132|
| |Tensas Parish|     0|  0.000|  0.000|    94| 21688.971| 791.087|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   173| 24809.981| 122.923|   6,973|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,784| 323.720| N/A|106,557|  9115.929| N/A|11,689,100|
| |Franklin County|   533| 404.783|  1.193|19,287| 14647.361| 138.978|1,316,756|
| |Cuyahoga County|   523| 423.457|  2.892|14,120| 11432.532| 98.433|1,235,072|
| |Lucas County|   324| 756.394|  1.001| 5,609| 13094.493| 134.070| 428,348|
| |Hamilton County|   262| 320.500|  1.573|10,001| 12234.043| 88.775| 817,473|
| |Mahoning County|   259| 1132.572|  2.499| 2,665| 11653.687| 101.825| 228,683|
| |Summit County|   225| 415.886|  1.320| 3,749|  6929.593| 69.446| 541,013|
| |Stark County|   142| 383.156|  1.156| 1,947|  5253.558| 63.217| 370,606|
| |Trumbull County|   112| 565.731|  4.330| 1,598|  8071.767| 70.716| 197,974|
| |Montgomery County|   101| 189.961|  2.687| 4,619|  8687.442| 104.788| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,884|  6080.695| 78.844| 309,833|
| |Butler County|    69| 180.094|  2.237| 3,105|  8104.214| 90.979| 383,134|
| |Portage County|    64| 393.929|  2.638|   782|  4813.315| 31.655| 162,466|
| |Columbiana County|    61| 598.726|  1.402| 1,704| 16725.067| 98.152| 101,883|
| |Wayne County|    60| 518.538|  2.469|   581|  5021.174| 69.138| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,115|  8523.357| 111.388| 130,817|
| |Licking County|    53| 299.669|  3.231| 1,390|  7859.235| 134.084| 176,862|
| |Allen County|    46| 449.434|  2.792|   842|  8226.593| 173.074| 102,351|
| |Ashtabula County|    46| 473.051|  0.000|   582|  5985.130| 33.789|  97,241|
| |Marion County|    45| 691.319|  0.000| 2,956| 45411.949| 81.202|  65,093|
| |Geauga County|    45| 480.518|  1.525|   564|  6022.488| 18.305|  93,649|
| |Lake County|    43| 186.835|  3.104| 1,163|  5053.248| 47.174| 230,149|
| |Pickaway County|    42| 718.477|  0.000| 2,411| 41243.991| 75.758|  58,457|
| |Warren County|    40| 170.502|  1.218| 1,914|  8158.498| 104.737| 234,602|
| |Miami County|    39| 364.530|  1.335|   893|  8346.808| 98.810| 106,987|
| |Medina County|    36| 200.283|  0.795|   988|  5496.645| 73.119| 179,746|
| |Fairfield County|    34| 215.772|  2.720| 1,473|  9347.989| 127.831| 157,574|
| |Darke County|    30| 586.935|  8.385|   442|  8647.507| 159.311|  51,113|
| |Erie County|    30| 403.953|  5.771|   626|  8429.160| 119.262|  74,266|
| |Ottawa County|    27| 666.255|  3.525|   408| 10067.859| 130.431|  40,525|
| |Belmont County|    26| 388.025|  0.000|   629|  9387.219| 31.980|  67,006|
| |Washington County|    22| 367.211|  0.000|   212|  3538.582| 28.614|  59,911|
| |Delaware County|    19| 90.832|  0.000| 1,392|  6654.651| 81.271| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    96|  7030.907| 52.313|  13,654|
| |Putnam County|    17| 502.053|  0.000|   221|  6526.683| 80.160|  33,861|
| |Sandusky County|    17| 290.509|  2.441|   421|  7194.368| 129.386|  58,518|
| |Clark County|    16| 119.329|  2.131| 1,235|  9210.713| 108.675| 134,083|
| |Tuscarawas County|    14| 152.195|  0.000|   806|  8762.108| 52.802|  91,987|
| |Mercer County|    13| 315.749|  0.000|   676| 16418.925| 294.930|  41,172|
| |Richland County|    12| 99.047|  1.179|   635|  5241.263| 45.986| 121,154|
| |Greene County|    12| 71.032|  0.000|   765|  4528.315| 87.099| 168,937|
| |Hardin County|    12| 382.592|  0.000|   183|  5834.529| 100.203|  31,365|
| |Clermont County|    11| 53.287|  0.000| 1,000|  4844.304| 67.820| 206,428|
| |Madison County|    10| 223.559|  0.000|   587| 13122.890| 747.324|  44,731|
| |Knox County|     9| 144.411|  4.584|   219|  3514.008| 45.845|  62,322|
| |Hocking County|     9| 318.426|  0.000|   123|  4351.826| 40.435|  28,264|
| |Coshocton County|     9| 245.902| 11.710|   199|  5437.158| 35.129|  36,600|
| |Wyandot County|     9| 413.375|  6.562|   158|  7257.027| 104.984|  21,772|
| |Auglaize County|     8| 175.223|  6.258|   288|  6308.043| 137.676|  45,656|
| |Guernsey County|     7| 180.064|  0.000|   121|  3112.540| 18.374|  38,875|
| |Clinton County|     6| 142.966|  0.000|   180|  4288.982| 74.887|  41,968|
| |Holmes County|     6| 136.488|  0.000|   332|  7552.320| 16.249|  43,960|
| |Ross County|     5| 65.218|  1.863|   528|  6887.016| 145.343|  76,666|
| |Huron County|     5| 85.813|  0.000|   414|  7105.344| 51.488|  58,266|
| |Carroll County|     5| 185.777|  0.000|   115|  4272.869| 26.540|  26,914|
| |Crawford County|     5| 120.499|  0.000|   181|  4362.076| 30.986|  41,494|
| |Defiance County|     4| 105.023|  0.000|   157|  4122.141| 67.515|  38,087|
| |Seneca County|     4| 72.493|  2.589|   245|  4440.175| 126.862|  55,178|
| |Shelby County|     4| 82.321|  0.000|   234|  4815.806| 141.123|  48,590|
| |Jefferson County|     3| 45.924|  2.187|   240|  3673.938| 45.924|  65,325|
| |Hancock County|     3| 39.587|  0.000|   415|  5476.162| 113.105|  75,783|
| |Ashland County|     3| 56.092|  0.000|   159|  2972.852| 50.749|  53,484|
| |Perry County|     3| 83.024|  0.000|   169|  4677.035| 189.770|  36,134|
| |Williams County|     3| 81.762|  0.000|   139|  3788.292| 27.254|  36,692|
| |Preble County|     2| 48.921|  0.000|   230|  5625.948| 174.719|  40,882|
| |Morrow County|     2| 56.612|  0.000|   188|  5321.558| 80.875|  35,328|
| |Adams County|     2| 72.207|  0.000|    68|  2455.051| 46.419|  27,698|
| |Athens County|     2| 30.615|  2.187|   366|  5602.584| 21.868|  65,327|
| |Champaign County|     2| 51.434|  0.000|   192|  4937.637| 121.237|  38,885|
| |Brown County|     2| 46.049|  0.000|   153|  3522.748| 88.809|  43,432|
| |Highland County|     2| 46.338|  3.310|   171|  3961.910| 76.127|  43,161|
| |Gallia County|     2| 66.894|  4.778|    85|  2843.000| 109.897|  29,898|
| |Logan County|     2| 43.791|  0.000|   174|  3809.774| 90.709|  45,672|
| |Van Wert County|     2| 70.734|  5.052|    73|  2581.786| 10.105|  28,275|
| |Henry County|     2| 74.058|  0.000|   125|  4628.601| 52.898|  27,006|
| |Vinton County|     2| 152.847|  0.000|    32|  2445.548| 21.835|  13,085|
| |Muskingum County|     1| 11.599|  0.000|   265|  3073.711| 72.907|  86,215|
| |Scioto County|     1| 13.278|  0.000|   265|  3518.602| 81.563|  75,314|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 18.997|  15,040|
| |Union County|     1| 16.953|  0.000|   280|  4746.728| 104.137|  58,988|
| |Fulton County|     1| 23.738|  0.000|   160|  3798.129| 44.085|  42,126|
| |Fayette County|     0|  0.000|  0.000|   127|  4452.235| 85.138|  28,525|
| |Jackson County|     0|  0.000|  0.000|    79|  2437.294| 26.444|  32,413|
| |Lawrence County|     0|  0.000|  0.000|   334|  5616.938| 160.964|  59,463|
| |Meigs County|     0|  0.000|  0.000|    66|  2881.215| 187.092|  22,907|
| |Pike County|     0|  0.000|  0.000|    81|  2916.607| 25.720|  27,772|
| |Paulding County|     0|  0.000|  0.000|    74|  3963.153| 68.858|  18,672|
| |Noble County|     0|  0.000|  0.000|    19|  1317.249| 29.712|  14,424|
| |Morgan County|     0|  0.000|  0.000|    32|  2205.680| 68.927|  14,508|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,617| 598.278| N/A|98,875| 16354.653| N/A|6,045,680|
| |Baltimore County| 1,012| 1223.153|  5.007|26,909| 32523.538| 303.026| 827,370|
| |Montgomery County|   808| 769.020|  0.952|18,819| 17911.121| 92.456|1,050,688|
| |Prince George's County|   766| 842.381|  2.671|24,442| 26879.219| 168.099| 909,327|
| |Anne Arundel County|   228| 393.623|  1.480| 7,564| 13058.626| 79.169| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,173| 12225.146| 67.700| 259,547|
| |Carroll County|   118| 700.517|  0.848| 1,596|  9474.790| 55.974| 168,447|
| |Howard County|   115| 353.097|  3.948| 4,009| 12309.251| 100.885| 325,690|
| |Charles County|    92| 563.529|  0.875| 2,119| 12979.535| 119.006| 163,257|
| |Harford County|    69| 270.121|  0.000| 2,085|  8162.355| 91.159| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,039|  9153.379| 96.908| 113,510|
| |Wicomico County|    45| 434.325|  0.000| 1,381| 13328.958| 81.350| 103,609|
| |Washington County|    31| 205.231|  0.000| 1,090|  7216.201| 82.282| 151,049|
| |Cecil County|    30| 291.673|  0.000|   719|  6990.423| 41.668| 102,855|
| |Calvert County|    28| 302.621|  0.000|   725|  7835.720| 81.831|  92,525|
| |Queen Anne's County|    26| 516.068|  2.836|   468|  9289.216| 136.106|  50,381|
| |Kent County|    23| 1184.224|  0.000|   242| 12460.097| 29.422|  19,422|
| |Worcester County|    20| 382.585|  0.000|   710| 13581.758| 95.646|  52,276|
| |Allegany County|    18| 255.624|  0.000|   326|  4629.630| 93.323|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   394| 12339.879| 129.752|  31,929|
| |Talbot County|     4| 107.582|  0.000|   412| 11080.928| 107.582|  37,181|
| |Somerset County|     3| 117.114|  0.000|   142|  5543.410| 50.192|  25,616|
| |Caroline County|     3| 89.804|  0.000|   457| 13680.177| 51.317|  33,406|
| |Garrett County|     0|  0.000|  0.000|    54|  1861.170| 39.390|  29,014|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,906| 431.656| N/A|78,632| 11679.953| N/A|6,732,219|
| |Marion County|   734| 760.951|  1.333|16,437| 17040.542| 138.328| 964,582|
| |Lake County|   283| 582.913|  2.648| 7,952| 16379.227| 148.597| 485,493|
| |Allen County|   164| 432.377|  1.130| 4,161| 10970.237| 140.108| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,819| 11500.503| 90.320| 158,167|
| |Hendricks County|   109| 640.006|  2.516| 1,978| 11614.047| 121.626| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 3,033|  8973.081| 154.264| 338,011|
| |Elkhart County|    91| 441.018|  6.231| 5,051| 24478.897| 201.470| 206,341|
| |St. Joseph County|    83| 305.342|  1.051| 3,766| 13854.451| 206.540| 271,826|
| |Madison County|    66| 509.381|  1.103| 1,062|  8196.405| 162.076| 129,569|
| |Howard County|    65| 787.459|  0.000|   948| 11484.784| 131.532|  82,544|
| |Delaware County|    52| 455.601|  0.000|   777|  6807.728| 95.125| 114,135|
| |Clark County|    50| 422.647|  4.830| 1,352| 11428.378| 210.116| 118,302|
| |Floyd County|    50| 636.764|  9.097|   861| 10965.080| 183.752|  78,522|
| |Bartholomew County|    47| 561.000|  0.000|   867| 10348.655| 172.222|  83,779|
| |Boone County|    46| 678.036|  0.000|   716| 10553.779| 113.708|  67,843|
| |Hancock County|    39| 498.925|  1.828|   702|  8980.657| 111.481|  78,168|
| |Porter County|    39| 228.888|  0.000| 1,415|  8304.527| 124.924| 170,389|
| |Morgan County|    35| 496.531|  2.027|   501|  7107.492| 85.120|  70,489|
| |Greene County|    34| 1065.096|  0.000|   259|  8113.527| 58.178|  31,922|
| |Monroe County|    32| 215.588|  1.925|   784|  5281.916| 59.672| 148,431|
| |Decatur County|    32| 1204.865|  0.000|   353| 13291.163| 112.956|  26,559|
| |Grant County|    30| 456.142|  0.000|   533|  8104.122| 26.065|  65,769|
| |Warrick County|    30| 476.206|  0.000|   612|  9714.594| 95.241|  62,998|
| |LaPorte County|    30| 273.005|  0.000|   967|  8799.869| 109.202| 109,888|
| |Noble County|    29| 607.406|  0.000|   717| 15017.594| 173.545|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   528| 10675.725| 101.096|  49,458|
| |Shelby County|    28| 625.992|  3.194|   573| 12810.481| 99.009|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   359|  7912.718| 72.420|  45,370|
| |Orange County|    24| 1221.623|  0.000|   188|  9569.378| 159.974|  19,646|
| |Harrison County|    24| 592.373|  3.526|   365|  9009.009| 155.145|  40,515|
| |Marshall County|    23| 497.211|  3.088|   805| 17402.395| 105.001|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   367|  9572.748| 70.799|  38,338|
| |Daviess County|    20| 599.682|  0.000|   296|  8875.296| 141.354|  33,351|
| |Henry County|    20| 416.910|  0.000|   467|  9734.845| 279.925|  47,972|
| |Franklin County|    16| 703.049| 18.832|   251| 11029.089| 81.604|  22,758|
| |Tipton County|    16| 1056.245| 94.308|   155| 10232.374| 207.477|  15,148|
| |Vanderburgh County|    15| 82.667|  1.575| 2,122| 11694.617| 184.229| 181,451|
| |Perry County|    13| 678.178|  7.453|   189|  9859.669| 59.620|  19,169|
| |Vigo County|    13| 121.452|  4.004|   779|  7277.789| 257.585| 107,038|
| |Tippecanoe County|    12| 61.308|  0.730| 1,293|  6605.971| 84.664| 195,732|
| |Kosciusko County|    12| 151.027|  0.000|   878| 11050.141| 68.322|  79,456|
| |Jennings County|    12| 432.666|  0.000|   233|  8400.937| 66.960|  27,735|
| |Dubois County|    12| 280.794|  0.000|   729| 17058.218| 177.167|  42,736|
| |White County|    11| 456.394|  5.927|   384| 15932.288| 177.816|  24,102|
| |LaGrange County|    10| 252.436|  0.000|   571| 14414.096| 54.093|  39,614|
| |Newton County|    10| 715.103|  0.000|   121|  8652.746| 61.295|  13,984|
| |Scott County|    10| 418.883|  0.000|   281| 11770.620| 107.713|  23,873|
| |Wayne County|    10| 151.782|  0.000|   410|  6223.059| 121.426|  65,884|
| |Cass County|     9| 238.796|  0.000| 1,813| 48104.221| 147.826|  37,689|
| |Putnam County|     8| 212.902|  0.000|   331|  8808.814| 171.082|  37,576|
| |Ripley County|     8| 282.446|  5.044|   221|  7802.570| 121.048|  28,324|
| |Fayette County|     7| 303.004|  0.000|   209|  9046.836| 160.778|  23,102|
| |Starke County|     7| 304.414|  0.000|   181|  7871.276| 31.063|  22,995|
| |Whitley County|     6| 176.658|  0.000|   162|  4769.756| 50.474|  33,964|
| |Ohio County|     6| 1021.277| 48.632|    63| 10723.404| 24.316|   5,875|
| |Clay County|     5| 190.658|  0.000|   150|  5719.733| 223.342|  26,225|
| |Carroll County|     5| 246.828| 21.157|   213| 10514.884| 253.880|  20,257|
| |Randolph County|     5| 202.716|  5.792|   134|  5432.800| 110.046|  24,665|
| |Wabash County|     5| 161.311|  9.218|   180|  5807.201| 78.351|  30,996|
| |Jackson County|     5| 113.043|  0.000|   607| 13723.407| 113.043|  44,231|
| |Clinton County|     4| 123.461|  4.409|   462| 14259.699| 233.693|  32,399|
| |DeKalb County|     4| 92.007|  0.000|   244|  5612.421| 59.147|  43,475|
| |Gibson County|     4| 118.839|  0.000|   246|  7308.595| 135.816|  33,659|
| |Rush County|     4| 241.240|  0.000|   100|  6030.999| 224.009|  16,581|
| |Spencer County|     3| 147.951|  0.000|   140|  6904.374| 63.408|  20,277|
| |Steuben County|     3| 86.720|  0.000|   217|  6272.764| 45.425|  34,594|
| |Huntington County|     3| 82.147|  0.000|   130|  3559.693| 35.206|  36,520|
| |Adams County|     2| 55.902|  0.000|   124|  3465.914| 115.797|  35,777|
| |Blackford County|     2| 170.097|  0.000|    66|  5613.200| 48.599|  11,758|
| |Brown County|     2| 132.521|  9.466|    76|  5035.781| 28.397|  15,092|
| |Fountain County|     2| 122.354|  0.000|    76|  4649.456| 69.917|  16,346|
| |Fulton County|     2| 100.130|  0.000|   175|  8761.390| 100.130|  19,974|
| |Jasper County|     2| 59.591|  0.000|   266|  7925.630| 166.004|  33,562|
| |Jefferson County|     2| 61.904|  0.000|   175|  5416.615| 88.435|  32,308|
| |Miami County|     2| 56.313|  0.000|   279|  7855.614| 48.268|  35,516|
| |Wells County|     2| 70.681|  0.000|   180|  6361.323| 90.876|  28,296|
| |Knox County|     1| 27.327|  3.904|   171|  4672.897| 85.884|  36,594|
| |Owen County|     1| 48.079|  0.000|   113|  5432.954| 199.185|  20,799|
| |Parke County|     1| 59.042|  0.000|    58|  3424.455| 59.042|  16,937|
| |Pulaski County|     1| 80.952|  0.000|    84|  6799.968| 92.517|  12,353|
| |Sullivan County|     1| 48.382|  0.000|   163|  7886.206| 414.700|  20,669|
| |Warren County|     1| 120.992|  0.000|    25|  3024.803| 51.854|   8,265|
| |Washington County|     1| 35.668|  0.000|   153|  5457.269| 112.101|  28,036|
| |Vermillion County|     0|  0.000|  0.000|    62|  4000.516| 110.613|  15,498|
| |Union County|     0|  0.000|  0.000|    42|  5954.069| 101.260|   7,054|
| |Jay County|     0|  0.000|  0.000|    97|  4746.526| 76.895|  20,436|
| |Switzerland County|     0|  0.000|  0.000|    59|  5487.862| 186.029|  10,751|
| |Posey County|     0|  0.000|  0.000|   184|  7236.402| 95.512|  25,427|
| |Pike County|     0|  0.000|  0.000|    67|  5408.023| 172.964|  12,389|
| |Martin County|     0|  0.000|  0.000|    53|  5168.211| 139.305|  10,255|
| |Crawford County|     0|  0.000|  0.000|    50|  4727.238| 81.038|  10,577|
| |Benton County|     0|  0.000|  0.000|    64|  7315.958| 65.321|   8,748|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,370| 277.663| N/A|104,838| 12282.557| N/A|8,535,519|
| |Fairfax County|   538| 468.832|  0.124|16,909| 14735.101| 72.703|1,147,532|
| |Henrico County|   187| 565.265|  1.295| 4,042| 12218.199| 99.753| 330,818|
| |Prince William County|   178| 378.454|  0.304| 9,773| 20778.807| 131.517| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,176| 13409.784| 83.841| 236,842|
| |Loudoun County|   115| 278.088|  0.000| 5,441| 13157.195| 84.636| 413,538|
| |Chesterfield County|    80| 226.756|  0.000| 4,542| 12874.077| 104.875| 352,802|
| |Alexandria city|    61| 382.618|  0.896| 3,050| 19130.893| 119.176| 159,428|
| |Virginia Beach city|    55| 122.229|  0.635| 5,277| 11727.344| 157.469| 449,974|
| |Suffolk city|    53| 575.411|  6.204| 1,379| 14971.555| 229.544|  92,108|
| |Shenandoah County|    46| 1054.659|  9.826|   732| 16782.832| 137.564|  43,616|
| |Richmond County|    45| 4987.255|  0.000| 3,630| 402305.220| 3166.511|   9,023|
| |Chesapeake city|    41| 167.460|  2.334| 3,158| 12898.483| 192.550| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,581| 11606.651| 138.437| 136,215|
| |Norfolk city|    33| 135.947|  1.766| 3,895| 16045.843| 156.545| 242,742|
| |Hanover County|    33| 306.219|  1.326|   690|  6402.762| 70.258| 107,766|
| |Mecklenburg County|    32| 1046.196|  0.000|   454| 14842.907| 322.266|  30,587|
| |Harrisonburg city|    31| 584.729|  0.000| 1,088| 20522.107| 35.030|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   298| 25448.335| 36.599|  11,710|
| |Galax city|    27| 4253.978| 67.523|   353| 55616.827| 112.539|   6,347|
| |Page County|    25| 1045.938|  5.977|   351| 14684.964| 83.675|  23,902|
| |Portsmouth city|    25| 264.836|  0.000| 1,952| 20678.404| 342.017|  94,398|
| |Manassas city|    22| 535.475|  3.477| 1,689| 41109.894| 184.287|  41,085|
| |Colonial Heights city|    22| 1266.552|  8.224|   204| 11744.387| 74.019|  17,370|
| |Newport News city|    20| 111.592|  1.594| 1,936| 10802.064| 117.968| 179,225|
| |Rockingham County|    20| 244.057|  1.743|   964| 11763.557| 54.041|  81,948|
| |Petersburg city|    19| 606.138|  0.000|   531| 16939.960| 113.936|  31,346|
| |Roanoke County|    19| 201.728|  1.517| 1,564| 16605.440| 104.656|  94,186|
| |Accomack County|    17| 526.055|  4.421| 1,116| 34533.977| 128.198|  32,316|
| |James City County|    17| 222.155|  1.867|   632|  8258.955| 67.207|  76,523|
| |Albemarle County|    16| 146.346|  0.000|   883|  8076.466| 86.240| 109,330|
| |Emporia city|    15| 2805.836|  0.000|   183| 34231.201| 240.500|   5,346|
| |Charlottesville city|    15| 317.353|  0.000|   555| 11742.056| 105.784|  47,266|
| |Nottoway County|    14| 919.118|  9.379|   183| 12014.181| 18.758|  15,232|
| |Carroll County|    14| 469.941|  9.591|   339| 11379.276| 86.316|  29,791|
| |Southampton County|    13| 737.338|  0.000|   293| 16618.456| 291.694|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,029| 19560.878| 111.342|  52,605|
| |Greensville County|    11| 970.360|  0.000|   569| 50194.072| 1474.443|  11,336|
| |Stafford County|    10| 65.410|  1.869| 1,460|  9549.849| 102.787| 152,882|
| |Prince Edward County|    10| 438.558|  0.000|   436| 19121.130| 244.339|  22,802|
| |Sussex County|     9| 806.524|  0.000|   315| 28228.336| 320.049|  11,159|
| |Isle of Wight County|     9| 242.529|  0.000|   424| 11425.800| 177.084|  37,109|
| |Fluvanna County|     9| 330.033|  0.000|   199|  7297.396| 78.579|  27,270|
| |Henry County|     9| 178.017|  5.651|   660| 13054.572| 245.833|  50,557|
| |Fauquier County|     9| 126.365|  0.000|   627|  8803.460| 42.122|  71,222|
| |Frederick County|     9| 100.769|  0.000|   690|  7725.639| 15.995|  89,313|
| |Bedford County|     8| 101.270|  1.808|   384|  4860.944| 77.761|  78,997|
| |Danville city|     8| 199.780|  3.568|   441| 11012.886| 196.213|  40,044|
| |Buckingham County|     8| 466.527|  0.000|   613| 35747.609| 99.970|  17,148|
| |Botetourt County|     7| 209.462|  0.000|   219|  6553.158| 38.473|  33,419|
| |Franklin County|     7| 124.906|  0.000|   384|  6852.004| 107.063|  56,042|
| |Goochland County|     7| 294.700|  0.000|   170|  7156.991| 66.157|  23,753|
| |Manassas Park city|     7| 400.503|  0.000|   530| 30323.836| 187.991|  17,478|
| |Dinwiddie County|     7| 245.235|  0.000|   227|  7952.635| 75.072|  28,544|
| |Hampton city|     7| 52.041|  0.000| 1,309|  9731.618| 144.440| 134,510|
| |Falls Church city|     6| 410.481|  0.000|    63|  4310.050| 29.320|  14,617|
| |Warren County|     6| 149.388|  0.000|   366|  9112.638| 42.682|  40,164|
| |Washington County|     6| 111.649|  2.658|   250|  4652.028| 103.674|  53,740|
| |Williamsburg city|     6| 401.230|  0.000|   132|  8827.070| 105.084|  14,954|
| |Hopewell city|     5| 221.936|  0.000|   282| 12517.200| 107.798|  22,529|
| |Caroline County|     5| 162.734|  0.000|   223|  7257.933| 106.939|  30,725|
| |Charles City County|     5| 718.081|  0.000|    53|  7611.662| 41.033|   6,963|
| |Wise County|     5| 133.751|  7.643|   208|  5564.026| 347.752|  37,383|
| |Lynchburg city|     5| 60.851|  0.000|   703|  8555.642| 260.790|  82,168|
| |Grayson County|     5| 321.543|  0.000|   161| 10353.698| 119.430|  15,550|
| |Alleghany County|     4| 269.179|  0.000|    62|  4172.275|  9.614|  14,860|
| |York County|     4| 58.582|  0.000|   394|  5770.357| 81.597|  68,280|
| |Powhatan County|     4| 134.898|  0.000|   159|  5362.202| 86.720|  29,652|
| |Patrick County|     4| 227.169|  0.000|   174|  9881.872| 324.528|  17,608|
| |Winchester city|     4| 142.460|  0.000|   412| 14673.410| 66.142|  28,078|
| |Augusta County|     4| 52.939|  0.000|   300|  3970.460| 68.065|  75,558|
| |Fredericksburg city|     4| 137.760|  4.920|   424| 14602.562| 137.760|  29,036|
| |King George County|     4| 149.054|  0.000|   160|  5962.140| 122.437|  26,836|
| |Wythe County|     3| 104.588|  0.000|   122|  4253.242| 49.804|  28,684|
| |Martinsville city|     3| 238.968|  0.000|   238| 18958.101| 477.935|  12,554|
| |Orange County|     3| 80.969|  0.000|   233|  6288.629| 26.990|  37,051|
| |Salem city|     3| 118.572|  0.000|   165|  6521.481| 45.170|  25,301|
| |Westmoreland County|     3| 166.528|  0.000|   215| 11934.499| 103.089|  18,015|
| |Russell County|     3| 112.841|  5.373|   140|  5265.929| 209.562|  26,586|
| |Scott County|     3| 139.108|  0.000|   112|  5193.360| 178.853|  21,566|
| |Waynesboro city|     3| 132.567|  0.000|   185|  8174.989| 107.316|  22,630|
| |Pulaski County|     3| 88.165|  0.000|    90|  2644.958| 25.190|  34,027|
| |Smyth County|     3| 99.655|  0.000|   160|  5314.908| 94.909|  30,104|
| |Northumberland County|     3| 248.036| 11.811|    79|  6531.625| 106.301|  12,095|
| |Montgomery County|     3| 30.446|  0.000|   315|  3196.834| 20.297|  98,535|
| |Surry County|     2| 311.429|  0.000|    51|  7941.451| 88.980|   6,422|
| |Halifax County|     2| 58.978|  4.213|   164|  4836.189| 50.552|  33,911|
| |Rappahannock County|     2| 271.370|  0.000|    45|  6105.834| 77.534|   7,370|
| |Greene County|     2| 100.913|  0.000|   173|  8728.997| 144.162|  19,819|
| |Prince George County|     2| 52.147|  0.000|   443| 11550.596| 245.837|  38,353|
| |King William County|     2| 116.632|  0.000|   100|  5831.584| 141.624|  17,148|
| |Louisa County|     2| 53.204|  0.000|   198|  5267.218| 64.605|  37,591|
| |Pittsylvania County|     2| 33.138|  0.000|   553|  9162.607| 319.543|  60,354|
| |Brunswick County|     2| 123.221|  0.000|   247| 15217.793| 184.831|  16,231|
| |Amelia County|     2| 152.149|  0.000|    83|  6314.188| 54.339|  13,145|
| |Campbell County|     2| 36.440|  0.000|   237|  4318.120| 122.334|  54,885|
| |Floyd County|     2| 126.992|  0.000|   111|  7048.067| 544.252|  15,749|
| |Gloucester County|     2| 53.550|  0.000|   173|  4632.109| 80.326|  37,348|
| |Buena Vista city|     1| 154.369|  0.000|    64|  9879.592| 308.737|   6,478|
| |Buchanan County|     1| 47.610|  6.801|    83|  3951.628| 34.007|  21,004|
| |Amherst County|     1| 31.641|  4.520|   202|  6391.394| 216.964|  31,605|
| |Dickenson County|     1| 69.842|  0.000|    49|  3422.266| 109.752|  14,318|
| |Essex County|     1| 91.299|  0.000|   108|  9860.312| 182.598|  10,953|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 61.007|   7,025|
| |Middlesex County|     1| 94.500|  0.000|    50|  4725.005| 216.000|  10,582|
| |Madison County|     1| 75.409|  0.000|    73|  5504.864| 75.409|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    66|  5411.610| 70.281|  12,196|
| |Lee County|     1| 42.693|  0.000|   140|  5977.031| 182.970|  23,423|
| |Rockbridge County|     1| 44.301|  0.000|    72|  3189.651| 37.972|  22,573|
| |New Kent County|     1| 43.307|  0.000|   133|  5759.820| 55.680|  23,091|
| |Lancaster County|     0|  0.000|  0.000|    45|  4244.082| 134.733|  10,603|
| |Mathews County|     0|  0.000|  0.000|    21|  2377.179| 64.685|   8,834|
| |Giles County|     0|  0.000|  0.000|    28|  1674.641| 42.720|  16,720|
| |Nelson County|     0|  0.000|  0.000|    59|  3951.775| 191.369|  14,930|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 11.642|  12,271|
| |Radford city|     0|  0.000|  0.000|    63|  3452.244| 117.423|  18,249|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Staunton city|     0|  0.000|  0.000|   156|  6257.019| 51.569|  24,932|
| |Norton city|     0|  0.000|  0.000|    22|  5526.250| 143.539|   3,981|
| |Appomattox County|     0|  0.000|  0.000|    98|  6159.261| 134.678|  15,911|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418|  0.000|   5,538|
| |Bristol city|     0|  0.000|  0.000|    91|  5428.946| 127.840|  16,762|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Tazewell County|     0|  0.000|  0.000|   127|  3128.464| 38.710|  40,595|
| |Clarke County|     0|  0.000|  0.000|    73|  4993.502| 29.316|  14,619|
| |Craig County|     0|  0.000|  0.000|    19|  3702.982| 55.684|   5,131|
| |Charlotte County|     0|  0.000|  0.000|    56|  4713.805| 48.100|  11,880|
| |Cumberland County|     0|  0.000|  0.000|    79|  7954.088| 57.534|   9,932|
| |Bland County|     0|  0.000|  0.000|    30|  4777.070| 432.211|   6,280|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Lexington city|     0|  0.000|  0.000|    35|  4700.510| 38.372|   7,446|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726|  0.000|   2,190|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,313| 220.536| N/A|142,170| 13555.383| N/A|10,488,084|
| |Mecklenburg County|   253| 227.855|  3.602|22,850| 20578.985| 125.314|1,110,356|
| |Wake County|   181| 162.805|  2.184|12,508| 11250.620| 94.316|1,111,761|
| |Guilford County|   158| 294.132|  1.064| 5,858| 10905.219| 95.739| 537,174|
| |Durham County|    80| 248.843|  0.444| 6,330| 19689.693| 111.091| 321,488|
| |Gaston County|    57| 253.865|  6.363| 3,495| 15565.918| 147.611| 224,529|
| |Henderson County|    56| 476.933|  2.433| 1,526| 12996.414| 81.517| 117,417|
| |Robeson County|    56| 428.708|  3.281| 2,952| 22599.043| 226.384| 130,625|
| |Forsyth County|    56| 146.484|  1.495| 5,477| 14326.633| 122.942| 382,295|
| |Chatham County|    55| 738.552|  5.755| 1,332| 17886.397| 80.569|  74,470|
| |Cumberland County|    55| 163.930|  1.703| 3,324|  9907.335| 129.015| 335,509|
| |Buncombe County|    52| 199.088|  2.735| 2,001|  7661.060| 101.732| 261,191|
| |Rowan County|    50| 351.895|  2.011| 2,316| 16299.758| 165.893| 142,088|
| |Cabarrus County|    50| 230.997|  0.660| 2,753| 12718.696| 104.939| 216,453|
| |Orange County|    48| 323.285|  0.962| 1,403|  9449.339| 71.200| 148,476|
| |Columbus County|    48| 864.740|  0.000|   961| 17312.820| 205.891|  55,508|
| |Duplin County|    48| 817.146|  0.000| 2,019| 34371.223| 119.167|  58,741|
| |Johnston County|    45| 214.962|  0.000| 3,399| 16236.822| 131.025| 209,339|
| |Union County|    43| 179.272|  0.596| 3,276| 13658.024| 154.853| 239,859|
| |Wayne County|    42| 341.100|  2.320| 2,485| 20181.758| 97.457| 123,131|
| |Alamance County|    42| 247.774|  0.843| 2,586| 15255.827| 186.252| 169,509|
| |Vance County|    41| 920.624|  3.208|   801| 17985.854| 134.725|  44,535|
| |Harnett County|    40| 294.170|  1.051| 1,367| 10053.245| 130.275| 135,976|
| |Randolph County|    39| 271.461|  1.989| 2,225| 15487.203| 75.572| 143,667|
| |Wilson County|    36| 440.092|  1.746| 1,536| 18777.277| 104.784|  81,801|
| |Catawba County|    33| 206.830|  3.581| 2,216| 13888.976| 127.143| 159,551|
| |Stanly County|    31| 493.583| 15.922| 1,207| 19217.909| 411.699|  62,806|
| |Granville County|    29| 479.791|  4.727| 1,313| 21722.946| 203.261|  60,443|
| |Burke County|    27| 298.392|  0.000| 1,686| 18632.923| 77.361|  90,485|
| |Franklin County|    26| 373.108|  2.050|   915| 13130.516| 141.453|  69,685|
| |Cleveland County|    23| 234.821|  7.293| 1,286| 13129.550| 208.568|  97,947|
| |Davidson County|    22| 131.258|  3.409| 1,849| 11031.627| 101.427| 167,609|
| |Brunswick County|    22| 154.040|  2.001| 1,293|  9053.354| 59.015| 142,820|
| |New Hanover County|    21| 89.563|  0.609| 2,666| 11370.179| 60.927| 234,473|
| |Pasquotank County|    20| 502.210|  3.587|   436| 10948.172| 172.186|  39,824|
| |McDowell County|    20| 437.101| 21.855|   701| 15320.395| 81.176|  45,756|
| |Moore County|    20| 198.255|  0.000| 1,062| 10527.359| 116.121| 100,880|
| |Haywood County|    19| 304.893| 16.047|   455|  7301.378| 142.130|  62,317|
| |Sampson County|    18| 283.326|  8.994| 1,504| 23673.482| 110.182|  63,531|
| |Craven County|    18| 176.230|  8.392|   758|  7421.259| 88.115| 102,139|
| |Iredell County|    17| 93.506|  0.000| 1,946| 10703.717| 128.866| 181,806|
| |Northampton County|    16| 821.229|  0.000|   314| 16116.614|  0.000|  19,483|
| |Montgomery County|    15| 552.019|  5.257|   673| 24767.232| 152.462|  27,173|
| |Pitt County|    14| 77.458|  2.371| 2,205| 12199.710| 241.860| 180,742|
| |Edgecombe County|    13| 252.565|  2.775|   709| 13774.479| 230.361|  51,472|
| |Rutherford County|    13| 193.946|  0.000|   799| 11920.214| 196.077|  67,029|
| |Onslow County|    12| 60.625|  1.443| 1,178|  5951.359| 109.702| 197,938|
| |Caldwell County|    12| 146.024|  0.000| 1,252| 15235.221| 95.611|  82,178|
| |Nash County|    12| 127.256|  0.000| 1,290| 13680.036| 242.393|  94,298|
| |Wilkes County|    12| 175.408|  2.088|   897| 13111.735| 244.318|  68,412|
| |Lee County|    11| 178.054|  0.000| 1,323| 21415.044| 143.368|  61,779|
| |Hertford County|    11| 464.586|  0.000|   375| 15838.155| 355.981|  23,677|
| |Hoke County|    11| 199.153|  5.173|   767| 13886.374| 147.425|  55,234|
| |Lenoir County|    11| 196.608|  0.000|   613| 10956.407| 140.434|  55,949|
| |Lincoln County|    10| 116.129|  1.659|   908| 10544.530| 137.696|  86,111|
| |Surry County|    10| 139.309|  1.990|   984| 13707.981| 135.328|  71,783|
| |Richmond County|     9| 200.763|  0.000|   543| 12112.695| 121.095|  44,829|
| |Jackson County|     7| 159.315|  6.503|   460| 10469.298| 71.529|  43,938|
| |Halifax County|     7| 139.972|  2.857|   747| 14937.013| 197.103|  50,010|
| |Warren County|     6| 304.090|  0.000|   266| 13481.324| 72.402|  19,731|
| |Yadkin County|     6| 159.291|  0.000|   561| 14893.674| 121.364|  37,667|
| |Martin County|     6| 267.380|  0.000|   273| 12165.775| 95.493|  22,440|
| |Polk County|     6| 289.519|  6.893|   165|  7961.783| 110.293|  20,724|
| |Bladen County|     6| 183.363|  0.000|   640| 19558.707| 139.705|  32,722|
| |Scotland County|     5| 143.583| 12.307|   395| 11343.078| 262.552|  34,823|
| |Bertie County|     5| 263.894|  0.000|   299| 15780.862| 271.434|  18,947|
| |Carteret County|     5| 71.970|  0.000|   369|  5311.416| 76.083|  69,473|
| |Davie County|     5| 116.697|  0.000|   431| 10059.282| 80.021|  42,846|
| |Cherokee County|     4| 139.801|  0.000|   279|  9751.153| 64.908|  28,612|
| |Washington County|     4| 345.423|  0.000|   137| 11830.743| 61.683|  11,580|
| |Rockingham County|     4| 43.951|  0.000|   577|  6339.963| 56.509|  91,010|
| |Jones County|     4| 424.674|  0.000|    99| 10510.670| 303.338|   9,419|
| |Mitchell County|     3| 200.481|  9.547|    80|  5346.164|  0.000|  14,964|
| |Pender County|     3| 47.574|  0.000|   676| 10719.949| 74.759|  63,060|
| |Stokes County|     3| 65.802|  0.000|   295|  6470.575| 12.534|  45,591|
| |Greene County|     3| 142.389|  0.000|   338| 16042.527| 94.926|  21,069|
| |Anson County|     3| 122.719|  0.000|   363| 14849.055| 268.814|  24,446|
| |Chowan County|     2| 143.441| 10.246|   162| 11618.733| 122.950|  13,943|
| |Beaufort County|     2| 42.559|  0.000|   425|  9043.708| 57.758|  46,994|
| |Gates County|     2| 172.980|  0.000|    49|  4238.021| 37.067|  11,562|
| |Camden County|     2| 184.043|  0.000|    76|  6993.651| 105.168|  10,867|
| |Person County|     2| 50.646|  0.000|   237|  6001.519| 108.527|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    92|  6833.544| 127.333|  13,463|
| |Caswell County|     2| 88.480|  0.000|   198|  8759.512| 44.240|  22,604|
| |Alexander County|     2| 53.338|  0.000|   327|  8720.698| 121.915|  37,497|
| |Macon County|     2| 55.776|  0.000|   469| 13079.369| 35.856|  35,858|
| |Tyrrell County|     2| 498.008| 35.572|   100| 24900.398| 177.860|   4,016|
| |Swain County|     2| 140.144|  0.000|   119|  8338.589| 20.021|  14,271|
| |Dare County|     2| 54.041|  0.000|   211|  5701.316| 19.300|  37,009|
| |Madison County|     1| 45.966|  6.567|    49|  2252.356| 45.966|  21,755|
| |Transylvania County|     1| 29.082|  0.000|   150|  4362.367| 74.783|  34,385|
| |Clay County|     1| 89.039| 12.720|    74|  6588.906|  0.000|  11,231|
| |Pamlico County|     1| 78.579|  0.000|    73|  5736.288| 67.354|  12,726|
| |Ashe County|     1| 36.761|  0.000|   168|  6175.789| 84.024|  27,203|
| |Graham County|     0|  0.000|  0.000|    46|  5449.591| 186.166|   8,441|
| |Alleghany County|     0|  0.000|  0.000|   172| 15444.015| 76.964|  11,137|
| |Currituck County|     0|  0.000|  0.000|    78|  2809.495| 30.874|  27,763|
| |Avery County|     0|  0.000|  0.000|    99|  5638.777|  0.000|  17,557|
| |Watauga County|     0|  0.000|  0.000|   314|  5589.476| 78.832|  56,177|
| |Hyde County|     0|  0.000|  0.000|    51| 10330.160| 376.168|   4,937|
| |Yancey County|     0|  0.000|  0.000|    78|  4316.786|  0.000|  18,069|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,204| 428.068| N/A|104,841| 20362.560| N/A|5,148,714|
| |Greenville County|   222| 424.035|  4.912|11,186| 21366.003| 120.334| 523,542|
| |Charleston County|   210| 510.445|  7.292|12,726| 30932.947| 211.123| 411,406|
| |Horry County|   168| 474.468|  8.876| 8,792| 24830.477| 123.458| 354,081|
| |Richland County|   163| 392.054|  5.154| 9,224| 22185.930| 221.626| 415,759|
| |Florence County|   124| 896.647| 16.528| 3,659| 26458.317| 340.891| 138,293|
| |Lexington County|   118| 394.979|  4.782| 5,132| 17178.243| 121.937| 298,750|
| |Spartanburg County|   111| 347.108|  5.361| 4,335| 13555.983| 147.420| 319,785|
| |Orangeburg County|    72| 835.509| 18.235| 2,514| 29173.194| 266.899|  86,175|
| |Anderson County|    71| 350.517|  8.463| 2,537| 12524.808| 187.601| 202,558|
| |Berkeley County|    70| 307.143|  2.507| 4,384| 19235.916| 191.181| 227,907|
| |Beaufort County|    60| 312.302|  3.718| 4,297| 22365.997| 221.585| 192,122|
| |Clarendon County|    56| 1659.505| 21.167|   883| 26166.840| 241.306|  33,745|
| |Sumter County|    53| 496.622|  8.032| 2,589| 24259.518| 168.664| 106,721|
| |Dorchester County|    53| 325.535|  5.265| 3,203| 19673.360| 159.696| 162,809|
| |Laurens County|    48| 711.185| 10.583| 1,369| 20283.585| 162.980|  67,493|
| |Aiken County|    44| 257.503|  8.360| 2,047| 11979.728| 198.143| 170,872|
| |Darlington County|    37| 555.405|  4.289| 1,386| 20805.188| 325.952|  66,618|
| |Colleton County|    34| 902.407|  0.000|   840| 22294.769| 159.248|  37,677|
| |Williamsburg County|    31| 1020.811|  4.704| 1,052| 34641.728| 324.590|  30,368|
| |Cherokee County|    31| 541.012|  7.479|   710| 12390.925| 214.410|  57,300|
| |York County|    30| 106.770|  0.508| 3,728| 13267.895| 129.140| 280,979|
| |Lee County|    30| 1782.743| 25.468|   572| 33990.967| 135.828|  16,828|
| |Kershaw County|    27| 405.704|  8.586| 1,437| 21592.463| 154.554|  66,551|
| |Lancaster County|    27| 275.476|  5.830| 1,322| 13488.144| 234.665|  98,012|
| |Pickens County|    27| 212.793|  0.000| 1,908| 15037.357| 101.330| 126,884|
| |Bamberg County|    27| 1919.522| 71.093|   484| 34409.214| 213.280|  14,066|
| |Georgetown County|    25| 398.851| 13.675| 1,504| 23994.895| 193.728|  62,680|
| |Dillon County|    25| 820.237|  4.687|   663| 21752.682| 206.231|  30,479|
| |Fairfield County|    24| 1073.970|  6.393|   578| 25864.769| 134.246|  22,347|
| |Chesterfield County|    22| 481.928|  3.129|   806| 17656.079| 197.152|  45,650|
| |Greenwood County|    20| 282.442|  4.035| 1,533| 21649.179| 359.105|  70,811|
| |Jasper County|    18| 598.544| 14.251|   615| 20450.238| 209.015|  30,073|
| |Calhoun County|    14| 962.001| 39.265|   385| 26455.026| 176.694|  14,553|
| |Marion County|    14| 456.666|  4.660|   577| 18821.150| 163.095|  30,657|
| |Chester County|    14| 434.189|  4.431|   730| 22639.871| 429.759|  32,244|
| |Hampton County|    13| 676.308| 44.592|   464| 24139.007| 386.462|  19,222|
| |Oconee County|    12| 150.856|  5.388|   864| 10861.640| 111.346|  79,546|
| |Newberry County|    11| 286.160|  7.433|   887| 23074.922| 211.833|  38,440|
| |Saluda County|     9| 439.603|  6.978|   473| 23103.600| 167.468|  20,473|
| |Abbeville County|     8| 326.171|  0.000|   353| 14392.302| 186.384|  24,527|
| |Barnwell County|     8| 383.399| 20.539|   444| 21278.635| 287.549|  20,866|
| |Edgefield County|     7| 256.787|  5.241|   353| 12949.376| 204.381|  27,260|
| |Allendale County|     6| 690.608| 49.329|   243| 27969.613| 493.291|   8,688|
| |Union County|     4| 146.434|  0.000|   386| 14130.912| 162.124|  27,316|
| |Marlboro County|     4| 153.151|  0.000|   536| 20522.245| 344.590|  26,118|
| |McCormick County|     2| 211.349|  0.000|   131| 13843.390| 271.735|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 2,043| 686.458| N/A|70,930| 23832.812| N/A|2,976,149|
| |Hinds County|   126| 543.478|  5.546| 5,852| 25241.546| 189.786| 231,840|
| |Lauderdale County|    96| 1295.110| 11.563| 1,481| 19979.764| 161.889|  74,125|
| |Neshoba County|    95| 3262.587| 14.718| 1,320| 45332.784| 176.621|  29,118|
| |Madison County|    72| 677.507| 10.754| 2,521| 23722.147| 168.032| 106,272|
| |Leflore County|    69| 2448.284| 35.482|   971| 34453.394| 324.410|  28,183|
| |Jones County|    62| 910.453|  8.391| 1,965| 28855.473| 241.249|  68,098|
| |Forrest County|    57| 761.045|  3.815| 1,889| 25221.304| 249.867|  74,897|
| |Monroe County|    55| 1560.195| 12.157|   858| 24339.045| 360.668|  35,252|
| |Holmes County|    50| 2939.447| 16.797|   938| 55144.033| 545.897|  17,010|
| |Jackson County|    47| 327.259|  4.974| 2,430| 16920.003| 203.915| 143,617|
| |Washington County|    46| 1047.621| 19.521| 1,771| 40333.417| 536.825|  43,909|
| |Lincoln County|    44| 1288.320| 12.549|   862| 25239.364| 276.069|  34,153|
| |Lee County|    42| 491.596| 15.049| 1,657| 19394.635| 458.154|  85,436|
| |Rankin County|    41| 264.054|  8.280| 2,382| 15340.920| 120.527| 155,271|
| |Bolivar County|    40| 1305.995| 32.650| 1,189| 38820.687| 447.770|  30,628|
| |Lowndes County|    40| 682.652|  7.314| 1,121| 19131.325| 153.597|  58,595|
| |Pearl River County|    40| 720.266|  7.717|   584| 10515.891| 141.481|  55,535|
| |Oktibbeha County|    39| 786.496|  2.881| 1,157| 23332.728| 175.737|  49,587|
| |Pike County|    38| 967.216| 10.908|   966| 24587.660| 254.531|  39,288|
| |Warren County|    37| 815.319| 15.740| 1,166| 25693.572| 418.677|  45,381|
| |Harrison County|    36| 173.010|  0.687| 2,710| 13023.837| 208.711| 208,080|
| |DeSoto County|    33| 178.431|  2.317| 3,832| 20719.673| 199.287| 184,945|
| |Simpson County|    32| 1200.390| 10.718|   842| 31585.265| 300.098|  26,658|
| |Tate County|    30| 1059.285| 15.133|   760| 26835.211| 277.432|  28,321|
| |Copiah County|    29| 1033.316|  5.090|   980| 34918.938| 178.158|  28,065|
| |Sunflower County|    28| 1115.094| 22.757| 1,101| 43847.073| 620.129|  25,110|
| |Adams County|    28| 912.260| 13.963|   655| 21340.371| 209.447|  30,693|
| |Clarke County|    28| 1801.686| 27.577|   359| 23100.187| 312.537|  15,541|
| |Leake County|    27| 1184.938| 12.539|   811| 35592.030| 156.738|  22,786|
| |Grenada County|    26| 1252.529| 34.410|   863| 41574.333| 172.051|  20,758|
| |Attala County|    25| 1375.592|  0.000|   544| 29932.871| 227.955|  18,174|
| |Walthall County|    22| 1539.969| 29.999|   521| 36469.271| 299.994|  14,286|
| |Marion County|    21| 854.597|  5.814|   698| 28405.160| 319.747|  24,573|
| |Lafayette County|    21| 388.752| 15.867| 1,043| 19308.021| 230.078|  54,019|
| |Wayne County|    21| 1040.480|  0.000|   805| 39885.052| 368.061|  20,183|
| |Scott County|    21| 746.693|  5.080| 1,025| 36445.740| 152.386|  28,124|
| |Chickasaw County|    19| 1110.916|  0.000|   502| 29351.576| 434.343|  17,103|
| |Panola County|    18| 526.439| 25.069| 1,108| 32405.241| 342.603|  34,192|
| |Lamar County|    18| 284.167|  9.021| 1,265| 19970.636| 164.637|  63,343|
| |Union County|    17| 589.971|  4.958|   750| 26028.110| 738.703|  28,815|
| |Winston County|    17| 946.811|  7.956|   644| 35867.446| 262.561|  17,955|
| |Hancock County|    15| 314.914|  2.999|   419|  8796.607| 137.962|  47,632|
| |Covington County|    15| 804.894| 15.331|   650| 34878.729| 306.626|  18,636|
| |Wilkinson County|    14| 1622.248| 16.554|   231| 26767.092| 496.607|   8,630|
| |Tippah County|    14| 635.930|  6.489|   426| 19350.443| 545.083|  22,015|
| |Kemper County|    14| 1437.077|  0.000|   246| 25251.488| 278.617|   9,742|
| |Clay County|    14| 724.788|  0.000|   411| 21277.697| 140.520|  19,316|
| |Claiborne County|    14| 1557.632| 15.894|   411| 45727.637| 206.625|   8,988|
| |Yazoo County|    14| 471.539|  9.623|   882| 29706.972| 322.379|  29,690|
| |Webster County|    13| 1341.728| 14.744|   254| 26215.296| 427.584|   9,689|
| |Smith County|    13| 816.788|  0.000|   419| 26325.710| 197.465|  15,916|
| |Greene County|    13| 956.867| 21.030|   267| 19652.584| 325.966|  13,586|
| |Coahoma County|    13| 587.597| 12.914|   810| 36611.824| 613.426|  22,124|
| |Humphreys County|    12| 1488.095| 17.715|   309| 38318.452| 460.601|   8,064|
| |Newton County|    12| 570.939|  6.797|   575| 27357.503| 258.282|  21,018|
| |Noxubee County|    12| 1151.963| 13.714|   472| 45310.550| 329.132|  10,417|
| |Carroll County|    11| 1105.861|  0.000|   264| 26540.666| 57.447|   9,947|
| |Tallahatchie County|    11| 796.582| 10.345|   563| 40770.512| 424.154|  13,809|
| |Prentiss County|    10| 397.994|  0.000|   475| 18904.720| 409.365|  25,126|
| |Marshall County|    10| 283.334|  4.048|   757| 21448.405| 335.954|  35,294|
| |Itawamba County|    10| 427.533|  0.000|   414| 17699.872| 403.103|  23,390|
| |Jasper County|    10| 610.389|  8.720|   416| 25392.175| 305.194|  16,383|
| |Yalobusha County|    10| 825.900|  0.000|   320| 26428.807| 94.389|  12,108|
| |Pontotoc County|     9| 279.729|  4.440|   876| 27226.953| 297.490|  32,174|
| |George County|     9| 367.347| 29.155|   626| 25551.020| 448.980|  24,500|
| |Tishomingo County|     9| 464.324| 29.481|   463| 23886.911| 737.023|  19,383|
| |Calhoun County|     9| 626.697|  0.000|   430| 29942.205| 228.794|  14,361|
| |Lawrence County|     8| 635.627| 11.350|   340| 27014.143| 317.813|  12,586|
| |Perry County|     8| 668.170| 11.932|   251| 20963.835| 334.085|  11,973|
| |Tunica County|     8| 830.565| 29.663|   370| 38413.621| 711.913|   9,632|
| |Jefferson County|     8| 1144.492| 40.875|   197| 28183.119| 61.312|   6,990|
| |Montgomery County|     8| 818.414| 73.073|   355| 36317.136| 584.582|   9,775|
| |Sharkey County|     7| 1619.995| 99.183|   214| 49525.573| 661.223|   4,321|
| |Stone County|     6| 327.225| 15.582|   235| 12816.318| 381.763|  18,336|
| |Jefferson Davis County|     6| 539.180|  0.000|   252| 22645.579| 308.103|  11,128|
| |Amite County|     6| 487.924|  0.000|   244| 19842.238| 220.727|  12,297|
| |Alcorn County|     5| 135.307|  0.000|   447| 12096.447| 193.296|  36,953|
| |Choctaw County|     4| 487.211|  0.000|   138| 16808.770| 121.803|   8,210|
| |Franklin County|     2| 259.302|  0.000|   142| 18410.476| 425.997|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    27| 20346.647| 215.308|   1,327|
| |Benton County|     1| 121.080| 17.297|   159| 19251.725| 294.052|   8,259|
| |Quitman County|     1| 147.232|  0.000|   275| 40488.810| 483.762|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,888| 327.850| N/A|52,519|  9119.883| N/A|5,758,736|
| |Denver County|   418| 574.799| N/A|10,471| 14398.847| N/A| 727,211|
| |Arapahoe County|   363| 552.856|  0.000| 7,497| 11418.084| 57.222| 656,590|
| |Jefferson County|   234| 401.454|  1.471| 4,362|  7483.517| 58.331| 582,881|
| |Adams County|   181| 349.812|  1.380| 6,721| 12989.423| 95.529| 517,421|
| |Weld County|   145| 446.852|  1.321| 3,794| 11692.122| 58.113| 324,492|
| |El Paso County|   143| 198.500|  1.190| 5,389|  7480.535| 94.788| 720,403|
| |Boulder County|    76| 232.989|  0.438| 2,120|  6499.160| 44.233| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,803|  5134.499| 34.580| 351,154|
| |Morgan County|    47| 1616.898|  4.915|   694| 23875.052| 54.060|  29,068|
| |Larimer County|    37| 103.671|  0.801| 1,651|  4625.959| 63.243| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   729|  4328.362| 46.651| 168,424|
| |Broomfield County|    32| 454.126| N/A|   484|  6868.658| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   303| 14885.046| 49.126|  20,356|
| |Montrose County|    13| 304.037|  0.000|   317|  7413.817| 80.185|  42,758|
| |Alamosa County|     9| 554.426|  0.000|   232| 14291.875| 52.802|  16,233|
| |Eagle County|     9| 163.259|  0.000| 1,145| 20770.221| 75.151|  55,127|
| |Routt County|     8| 312.037|  5.572|   125|  4875.575| 44.577|  25,638|
| |Gunnison County|     7| 400.870|  8.181|   279| 15977.551| 89.991|  17,462|
| |Otero County|     6| 328.263|  0.000|    78|  4267.425| 54.711|  18,278|
| |Logan County|     5| 223.125|  0.000|   655| 29229.328| 31.875|  22,409|
| |Montezuma County|     5| 190.964|  5.456|   113|  4315.777| 10.912|  26,183|
| |Summit County|     4| 128.986|  0.000|   344| 11092.838| 78.313|  31,011|
| |Garfield County|     4| 66.599|  0.000|   784| 13053.396| 64.220|  60,061|
| |Mesa County|     4| 25.939|  0.000|   361|  2340.964| 62.994| 154,210|
| |Kit Carson County|     3| 422.714|  0.000|    70|  9863.323| 523.360|   7,097|
| |Teller County|     3| 118.166|  0.000|   144|  5671.971| 118.166|  25,388|
| |La Plata County|     3| 53.361|  2.541|   229|  4073.211| 63.525|  56,221|
| |Elbert County|     2| 74.825|  0.000|   109|  4077.968| 32.068|  26,729|
| |Pitkin County|     2| 112.568|  0.000|   190| 10693.983| 64.325|  17,767|
| |Rio Grande County|     2| 177.510|  0.000|    92|  8165.439| 38.038|  11,267|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Grand County|     1| 63.557|  0.000|    54|  3432.058| 72.636|  15,734|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925|  0.000|   6,897|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Clear Creek County|     1| 103.093|  0.000|    31|  3195.876| 14.728|   9,700|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202|  0.000|   4,952|
| |Crowley County|     1| 164.989|  0.000|    73| 12044.217| 23.570|   6,061|
| |Delta County|     1| 32.090|  0.000|   132|  4235.928| 64.181|  31,162|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 64.529|  13,283|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Archuleta County|     0|  0.000|  0.000|    40|  2851.237| 50.915|  14,029|
| |Gilpin County|     0|  0.000|  0.000|    17|  2723.050| 22.883|   6,243|
| |Fremont County|     0|  0.000|  0.000|   135|  2821.965| 53.752|  47,839|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Custer County|     0|  0.000|  0.000|    12|  2367.798| 28.188|   5,068|
| |Costilla County|     0|  0.000|  0.000|    24|  6174.428| 73.505|   3,887|
| |Conejos County|     0|  0.000|  0.000|    27|  3290.676| 69.644|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771|  0.000|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517|  0.000|   1,392|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Washington County|     0|  0.000|  0.000|    50| 10187.449| 87.321|   4,908|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053|  0.000|  10,019|
| |San Miguel County|     0|  0.000|  0.000|    92| 11248.319| 174.663|   8,179|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684| 35.156|   8,127|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 112.948|   6,324|
| |Prowers County|     0|  0.000|  0.000|    62|  5093.658| 129.102|  12,172|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263|  0.000|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866| 29.544|  14,506|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,825| 372.207| N/A|102,196| 20842.779| N/A|4,903,185|
| |Jefferson County|   262| 397.830|  4.338|13,682| 20775.222| 203.687| 658,573|
| |Mobile County|   223| 539.677|  5.877|10,836| 26223.954| 439.417| 413,210|
| |Montgomery County|   153| 675.538|  3.154| 7,009| 30946.725| 307.808| 226,486|
| |Tuscaloosa County|    80| 382.126|  6.141| 4,378| 20911.848| 187.651| 209,355|
| |Tallapoosa County|    79| 1957.044|  0.000|   883| 21874.303| 120.325|  40,367|
| |Walker County|    66| 1039.026|  4.498| 1,584| 24936.635| 184.416|  63,521|
| |Lee County|    47| 285.641|  2.605| 2,735| 16621.896| 92.899| 164,542|
| |Elmore County|    39| 480.242|  1.759| 1,789| 22029.578| 167.117|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   852| 25620.978| 73.031|  33,254|
| |Marshall County|    38| 392.667|  5.905| 3,214| 33211.400| 183.048|  96,774|
| |Shelby County|    37| 169.957|  2.625| 3,414| 15681.987| 139.772| 217,702|
| |Butler County|    36| 1851.090|  7.346|   779| 40055.533| 146.912|  19,448|
| |Madison County|    35| 93.857|  1.915| 5,581| 14966.118| 126.802| 372,909|
| |Etowah County|    34| 332.460|  5.588| 2,219| 21697.892| 201.152| 102,268|
| |Dale County|    29| 589.767| 17.432|   863| 17550.639| 116.210|  49,172|
| |Baldwin County|    29| 129.909|  3.840| 3,791| 16982.180| 222.700| 223,234|
| |Marion County|    26| 875.156|  9.617|   594| 19993.941| 129.831|  29,709|
| |Hale County|    26| 1774.623|  0.000|   490| 33444.816| 224.266|  14,651|
| |Dallas County|    25| 672.115|  7.681| 1,349| 36267.341| 145.945|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   576| 59222.702| 132.194|   9,726|
| |Autauga County|    22| 393.778|  2.557| 1,196| 21407.220| 334.967|  55,869|
| |Franklin County|    22| 701.486|  9.110| 1,315| 41929.724| 259.641|  31,362|
| |Covington County|    21| 566.817|  3.856|   763| 20594.348| 142.668|  37,049|
| |St. Clair County|    20| 223.434|  6.384| 1,388| 15506.301| 124.485|  89,512|
| |Morgan County|    20| 167.114|  3.581| 2,457| 20529.918| 151.596| 119,679|
| |Lauderdale County|    20| 215.682|  4.622| 1,219| 13145.834| 123.247|  92,729|
| |Calhoun County|    19| 167.246|  7.545| 1,867| 16434.136| 204.971| 113,605|
| |Sumter County|    19| 1528.929| 11.496|   371| 29854.349| 103.461|  12,427|
| |Colbert County|    18| 325.845| 12.930| 1,243| 22501.403| 224.988|  55,241|
| |Escambia County|    17| 464.062|  3.900| 1,099| 30000.273| 175.486|  36,633|
| |Marengo County|    17| 901.235| 22.720|   578| 30641.998| 242.349|  18,863|
| |Macon County|    15| 830.197| 15.813|   344| 19039.185| 94.880|  18,068|
| |Talladega County|    14| 175.048|  1.786| 1,103| 13791.293| 208.986|  79,978|
| |DeKalb County|    14| 195.769|  1.998| 1,870| 26149.092| 197.766|  71,513|
| |Houston County|    13| 122.778|  1.349| 1,493| 14100.603| 174.048| 105,882|
| |Limestone County|    13| 131.426|  0.000| 1,407| 14224.334| 177.642|  98,915|
| |Washington County|    13| 796.276|  8.750|   461| 28237.168| 1172.538|  16,326|
| |Choctaw County|    12| 953.213|  0.000|   292| 23194.853| 147.521|  12,589|
| |Cullman County|    12| 143.253|  0.000| 1,252| 14946.041| 86.975|  83,768|
| |Bullock County|    11| 1089.001|  0.000|   494| 48906.049| 565.715|  10,101|
| |Greene County|    11| 1356.183|  0.000|   256| 31562.076| 105.677|   8,111|
| |Winston County|    11| 465.530|  0.000|   459| 19425.282| 90.688|  23,629|
| |Randolph County|    11| 484.112|  6.287|   405| 17824.135| 69.159|  22,722|
| |Pickens County|    10| 501.756|  7.168|   420| 21073.758| 258.046|  19,930|
| |Conecuh County|    10| 828.706|  0.000|   398| 32982.514| 189.419|  12,067|
| |Wilcox County|    10| 964.041|  0.000|   445| 42899.836| 371.844|  10,373|
| |Clarke County|    10| 423.334|  6.048|   830| 35136.737| 2019.909|  23,622|
| |Chilton County|     9| 202.575|  9.646|   843| 18974.521| 244.376|  44,428|
| |Crenshaw County|     8| 580.889| 51.865|   339| 24615.161| 269.698|  13,772|
| |Cherokee County|     8| 305.390|  5.453|   293| 11184.914| 163.602|  26,196|
| |Pike County|     7| 211.391|  0.000|   718| 21682.672| 120.795|  33,114|
| |Coffee County|     6| 114.631|  2.729|   792| 15131.252| 122.819|  52,342|
| |Monroe County|     6| 289.394| 13.781|   427| 20595.186| 82.684|  20,733|
| |Barbour County|     6| 243.053|  5.787|   590| 23900.186| 121.526|  24,686|
| |Blount County|     5| 86.466|  4.941|   848| 14664.684| 182.814|  57,826|
| |Bibb County|     5| 223.274|  6.379|   465| 20764.490| 312.584|  22,394|
| |Clay County|     5| 377.786|  0.000|   278| 21004.911| 313.023|  13,235|
| |Fayette County|     5| 306.711|  0.000|   234| 14354.067| 315.474|  16,302|
| |Perry County|     4| 448.280|  0.000|   452| 50655.609| 256.160|   8,923|
| |Jackson County|     4| 77.480|  0.000| 1,091| 21132.763| 404.005|  51,626|
| |Coosa County|     3| 281.347| 13.397|   106|  9940.917| 66.987|  10,663|
| |Henry County|     3| 174.368|  0.000|   273| 15867.480| 174.368|  17,205|
| |Lawrence County|     3| 91.119|  8.678|   364| 11055.765| 86.780|  32,924|
| |Russell County|     2| 34.506|  0.000| 1,398| 24119.667| 138.024|  57,961|
| |Geneva County|     2| 76.130| 10.876|   274| 10429.751| 103.319|  26,271|
| |Lamar County|     2| 144.875|  0.000|   237| 17167.693| 206.964|  13,805|
| |Cleburne County|     1| 67.069|  0.000|   131|  8786.050| 57.488|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,753| 230.207| N/A|65,922|  8656.983| N/A|7,614,893|
| |King County|   689| 305.844|  1.205|17,308|  7682.945| 68.867|2,252,782|
| |Yakima County|   218| 868.966|  3.417|10,523| 41945.526| 178.235| 250,873|
| |Snohomish County|   202| 245.717|  1.912| 5,668|  6894.681| 51.959| 822,083|
| |Pierce County|   146| 161.330|  1.421| 6,038|  6671.971| 81.454| 904,980|
| |Benton County|   121| 592.005|  4.893| 3,815| 18665.297| 87.368| 204,390|
| |Spokane County|   101| 193.191|  3.552| 4,723|  9034.082| 121.872| 522,798|
| |Franklin County|    51| 535.591|  4.501| 3,667| 38510.008| 330.056|  95,222|
| |Clark County|    47| 96.264|  1.170| 1,897|  3885.376| 43.304| 488,241|
| |Whatcom County|    39| 170.122|  0.000| 1,012|  4414.453| 26.173| 229,247|
| |Skagit County|    22| 170.272|  1.106|   916|  7089.509| 64.128| 129,205|
| |Kittitas County|    20| 417.232|  5.960|   426|  8887.035| 196.695|  47,935|
| |Island County|    13| 152.688|  3.356|   249|  2924.560|  3.356|  85,141|
| |Grant County|    13| 133.015|  1.462| 1,676| 17148.762| 371.274|  97,733|
| |Thurston County|    11| 37.861|  0.000|   774|  2664.042| 39.336| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,482| 19196.891| 381.199|  77,200|
| |Kitsap County|     7| 25.785|  0.000|   793|  2921.101| 37.889| 271,473|
| |Douglas County|     7| 161.183|  0.000| 1,007| 23187.271| 325.655|  43,429|
| |Okanogan County|     5| 118.363|  6.764|   903| 21376.323| 226.580|  42,243|
| |Cowlitz County|     5| 45.211|  0.000|   504|  4557.250| 41.336| 110,593|
| |Adams County|     5| 250.213|  7.149|   479| 23970.375| 400.340|  19,983|
| |Lewis County|     4| 49.562|  1.770|   241|  2986.110| 60.182|  80,707|
| |Walla Walla County|     3| 49.375|  2.351|   581|  9562.212| 202.201|  60,760|
| |Klickitat County|     3| 133.779|  0.000|   121|  5395.764| 76.445|  22,425|
| |Grays Harbor County|     3| 39.967|  1.903|   132|  1758.570| 43.774|  75,061|
| |Asotin County|     2| 88.566|  0.000|    33|  1461.341| 50.609|  22,582|
| |Pacific County|     2| 89.004|  0.000|    55|  2447.599| 44.502|  22,471|
| |Mason County|     1| 14.977|  0.000|   254|  3804.218| 113.399|  66,768|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Skamania County|     1| 82.761|  0.000|    58|  4800.132| 11.823|  12,083|
| |Stevens County|     1| 21.871|  0.000|   114|  2493.275| 28.120|  45,723|
| |Pend Oreille County|     0|  0.000|  0.000|    46|  3351.792| 72.865|  13,724|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Whitman County|     0|  0.000|  0.000|   120|  2395.018| 48.471|  50,104|
| |Clallam County|     0|  0.000|  0.000|   146|  1887.988| 81.283|  77,331|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489|  0.000|   7,627|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Lincoln County|     0|  0.000|  0.000|    30|  2742.481| 104.475|  10,939|
| |Jefferson County|     0|  0.000|  0.000|    57|  1769.033| 13.301|  32,221|
| |San Juan County|     0|  0.000|  0.000|    30|  1706.291| 16.250|  17,582|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,693| 300.197| N/A|63,579| 11273.608| N/A|5,639,632|
| |Hennepin County|   845| 667.539|  1.919|20,063| 15849.517| 145.471|1,265,843|
| |Ramsey County|   270| 490.623|  1.817| 7,904| 14362.527| 154.974| 550,321|
| |Anoka County|   115| 322.200|  0.400| 3,891| 10901.572| 135.284| 356,921|
| |Dakota County|   106| 247.074|  0.666| 4,670| 10885.248| 139.853| 429,021|
| |Washington County|    48| 182.899|  2.177| 2,255|  8592.440| 118.667| 262,440|
| |Clay County|    40| 622.840|  0.000|   795| 12378.936| 53.386|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,809| 11428.174| 98.371| 158,293|
| |Scott County|    22| 147.638|  3.835| 1,669| 11200.365| 159.142| 149,013|
| |Stearns County|    20| 124.166|  0.000| 2,935| 18221.325| 54.101| 161,075|
| |St. Louis County|    20| 100.467|  0.718|   636|  3194.856| 96.161| 199,070|
| |Winona County|    16| 316.932|  0.000|   272|  5387.846| 42.446|  50,484|
| |Crow Wing County|    14| 215.203|  0.000|   265|  4073.476| 81.250|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   363| 10591.119| 141.715|  34,274|
| |Itasca County|    12| 265.899|  0.000|   146|  3235.099| 31.655|  45,130|
| |Sherburne County|    10| 102.840|  4.407|   758|  7795.306| 70.519|  97,238|
| |Goodhue County|     9| 194.217|  3.083|   208|  4488.563| 49.325|  46,340|
| |Nobles County|     9| 416.108| 19.815| 1,781| 82343.150| 178.332|  21,629|
| |Pipestone County|     9| 986.193|  0.000|   161| 17641.902| 187.846|   9,126|
| |Rice County|     8| 119.453|  0.000| 1,048| 15648.331| 61.860|  66,972|
| |Blue Earth County|     6| 88.688|  2.112|   960| 14190.058| 141.478|  67,653|
| |Wright County|     5| 36.133|  0.000|   939|  6785.810| 86.720| 138,377|
| |Renville County|     5| 343.690|  0.000|    67|  4605.444| 49.099|  14,548|
| |Martin County|     5| 254.026|  0.000|   212| 10770.716| 43.547|  19,683|
| |Otter Tail County|     4| 68.090|  2.432|   209|  3557.689| 48.636|  58,746|
| |Polk County|     4| 127.535|  0.000|   161|  5133.274| 54.658|  31,364|
| |Grant County|     4| 669.792| 23.921|    57|  9544.541| 95.685|   5,972|
| |Mille Lacs County|     3| 114.168|  0.000|    73|  2778.095| 21.746|  26,277|
| |Wilkin County|     3| 483.325|  0.000|    35|  5638.795| 46.031|   6,207|
| |Carver County|     3| 28.547|  0.000|   915|  8706.906| 116.908| 105,089|
| |Lyon County|     3| 117.767|  0.000|   427| 16762.189| 16.824|  25,474|
| |Cass County|     3| 100.742|  4.797|    79|  2652.876| 43.175|  29,779|
| |Koochiching County|     3| 245.319|  0.000|    83|  6787.145| 105.137|  12,229|
| |Benton County|     3| 73.369|  0.000|   327|  7997.261| 38.432|  40,889|
| |Steele County|     2| 54.572|  3.898|   363|  9904.772| 97.450|  36,649|
| |Todd County|     2| 81.090|  0.000|   431| 17474.862| 52.129|  24,664|
| |Watonwan County|     2| 183.537| 26.220|   384| 35239.057| 1009.452|  10,897|
| |Brown County|     2| 79.974|  0.000|    92|  3678.823| 28.562|  25,008|
| |Sibley County|     2| 134.544|  0.000|    86|  5785.402| 28.831|  14,865|
| |Mower County|     2| 49.923|  0.000| 1,117| 27881.783| 78.450|  40,062|
| |Kanabec County|     2| 122.421|  8.744|    37|  2264.798| 26.233|  16,337|
| |Meeker County|     2| 86.125|  0.000|    88|  3789.510| 24.607|  23,222|
| |Waseca County|     1| 53.729|  7.676|   157|  8435.418| 145.835|  18,612|
| |Freeborn County|     1| 33.024|  0.000|   365| 12053.763| 33.024|  30,281|
| |Douglas County|     1| 26.219|  3.746|   144|  3775.465| 22.473|  38,141|
| |Chisago County|     1| 17.674|  0.000|   211|  3729.299| 53.023|  56,579|
| |Swift County|     1| 107.921|  0.000|    57|  6151.522| 77.087|   9,266|
| |Kandiyohi County|     1| 23.149|  0.000|   725| 16782.796| 125.664|  43,199|
| |Murray County|     1| 122.041|  0.000|   125| 15255.065| 52.303|   8,194|
| |Morrison County|     1| 29.953|  0.000|    97|  2905.409| 51.347|  33,386|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 20.236|  14,119|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 25.847|   5,527|
| |Le Sueur County|     1| 34.618|  0.000|   237|  8204.383| 118.689|  28,887|
| |Becker County|     1| 29.050|  0.000|   164|  4764.256| 62.251|  34,423|
| |Aitkin County|     1| 62.949|  0.000|    42|  2643.837| 71.941|  15,886|
| |Chippewa County|     1| 84.746|  0.000|   119| 10084.746| 217.918|  11,800|
| |Stevens County|     0|  0.000|  0.000|    22|  2243.753| 72.849|   9,805|
| |Redwood County|     0|  0.000|  0.000|    37|  2439.024| 37.668|  15,170|
| |Rock County|     0|  0.000|  0.000|    89|  9554.482| 153.362|   9,315|
| |Roseau County|     0|  0.000|  0.000|    53|  3494.890| 56.521|  15,165|
| |Traverse County|     0|  0.000|  0.000|    15|  4602.639| 219.173|   3,259|
| |Yellow Medicine County|     0|  0.000|  0.000|    53|  5458.853| 29.428|   9,709|
| |Wadena County|     0|  0.000|  0.000|    28|  2046.484| 31.324|  13,682|
| |Wabasha County|     0|  0.000|  0.000|    97|  4485.134| 59.449|  21,627|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Carlton County|     0|  0.000|  0.000|   149|  4153.773| 63.720|  35,871|
| |Lake County|     0|  0.000|  0.000|    24|  2255.427| 53.701|  10,641|
| |Faribault County|     0|  0.000|  0.000|    93|  6811.690| 83.707|  13,653|
| |Lac qui Parle County|     0|  0.000|  0.000|     9|  1358.901| 64.710|   6,623|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    81|  8226.691| 130.582|   9,846|
| |Isanti County|     0|  0.000|  0.000|   141|  3473.249| 70.380|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    37|  1721.651| 33.237|  21,491|
| |Houston County|     0|  0.000|  0.000|    49|  2634.409| 76.805|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    73|  3465.135| 67.811|  21,067|
| |Big Stone County|     0|  0.000|  0.000|    25|  5009.016| 85.869|   4,991|
| |Lincoln County|     0|  0.000|  0.000|    61| 10817.521| 126.669|   5,639|
| |McLeod County|     0|  0.000|  0.000|   240|  6686.541| 266.666|  35,893|
| |Marshall County|     0|  0.000|  0.000|    30|  3213.368| 15.302|   9,336|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510| 44.818|   6,375|
| |Beltrami County|     0|  0.000|  0.000|   267|  5658.218| 151.370|  47,188|
| |Cook County|     0|  0.000|  0.000|     6|  1098.298| 78.450|   5,463|
| |Cottonwood County|     0|  0.000|  0.000|   180| 16077.170| 51.039|  11,196|
| |Dodge County|     0|  0.000|  0.000|   136|  6496.608| 75.066|  20,934|
| |Lake of the Woods County|     0|  0.000|  0.000|     7|  1871.658| 190.985|   3,740|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 35.230|   4,055|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 25.399|  11,249|
| |Pine County|     0|  0.000|  0.000|   132|  4462.626| 19.319|  29,579|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,303| 190.799| N/A|124,343| 18207.619| N/A|6,829,174|
| |Shelby County|   321| 342.522|  2.896|24,251| 25876.952| 246.335| 937,166|
| |Davidson County|   221| 318.378|  1.852|21,528| 31013.738| 276.394| 694,144|
| |Sumner County|    74| 386.861|  0.747| 3,581| 18720.953| 161.317| 191,283|
| |Hamilton County|    58| 157.693|  2.330| 6,605| 17957.934| 246.638| 367,804|
| |Rutherford County|    57| 171.539|  1.720| 6,938| 20879.667| 229.579| 332,285|
| |Knox County|    41| 87.176|  1.215| 5,051| 10739.656| 195.614| 470,313|
| |Williamson County|    25| 104.860|  0.000| 3,741| 15691.324| 175.566| 238,412|
| |Madison County|    23| 234.732|  8.748| 1,282| 13083.769| 376.155|  97,984|
| |Wilson County|    23| 158.997|  0.000| 2,434| 16826.009| 202.449| 144,657|
| |Robertson County|    21| 292.426|  3.979| 1,616| 22502.889| 188.983|  71,813|
| |Putnam County|    20| 249.237|  5.341| 1,932| 24076.266| 382.756|  80,245|
| |McMinn County|    20| 371.789|  0.000|   591| 10986.355| 177.927|  53,794|
| |Hardeman County|    18| 718.563|  5.703| 1,027| 40998.004| 866.838|  25,050|
| |Sullivan County|    16| 101.043|  3.609| 1,136|  7174.072| 183.141| 158,348|
| |Montgomery County|    15| 71.773|  1.367| 2,085|  9976.411| 138.077| 208,993|
| |Hamblen County|    15| 231.004|  2.200| 1,476| 22730.773| 228.804|  64,934|
| |Bradley County|    15| 138.748|  3.964| 2,102| 19443.160| 301.280| 108,110|
| |Blount County|    15| 112.707|  5.367| 1,414| 10624.549| 183.552| 133,088|
| |Macon County|    13| 528.412|  0.000|   874| 35525.567| 104.521|  24,602|
| |Giles County|    13| 441.216|  0.000|   402| 13643.769| 160.002|  29,464|
| |Tipton County|    12| 194.808|  6.957| 1,247| 20243.835| 148.425|  61,599|
| |Bedford County|    11| 221.270|  0.000|   962| 19351.075| 155.176|  49,713|
| |Hawkins County|    10| 176.100|  7.547|   534|  9403.726| 249.055|  56,786|
| |Monroe County|    10| 214.846|  3.069|   479| 10291.116| 220.984|  46,545|
| |Cheatham County|     9| 221.310|  7.026|   624| 15344.137| 179.155|  40,667|
| |Maury County|     9| 93.374|  2.964| 1,367| 14182.410| 280.121|  96,387|
| |Greene County|     9| 130.304|  4.137|   561|  8122.312| 235.789|  69,069|
| |Dyer County|     9| 242.202|  7.689|   715| 19241.637| 369.070|  37,159|
| |Sevier County|     9| 91.603|  2.908| 1,989| 20244.275| 231.189|  98,250|
| |Gibson County|     9| 183.176| 11.630|   787| 16017.748| 340.185|  49,133|
| |Lauderdale County|     9| 351.110|  5.573|   552| 21534.740| 362.256|  25,633|
| |Fayette County|     8| 194.491|  0.000|   744| 18087.667| 257.006|  41,133|
| |Hardin County|     8| 311.867|  0.000|   499| 19452.674| 256.176|  25,652|
| |Cumberland County|     7| 115.664|  2.360|   530|  8757.436| 278.538|  60,520|
| |Haywood County|     7| 404.531|  8.256|   581| 33576.052| 1023.710|  17,304|
| |Lawrence County|     7| 158.579|  3.236|   619| 14022.926| 275.086|  44,142|
| |Anderson County|     7| 90.935|  1.856|   743|  9652.108| 139.186|  76,978|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 12.660|  11,284|
| |Carroll County|     6| 216.084| 15.435|   379| 13649.296| 457.892|  27,767|
| |Carter County|     6| 106.400|  0.000|   602| 10675.462| 266.000|  56,391|
| |Crockett County|     6| 421.644| 20.078|   294| 20660.576| 341.331|  14,230|
| |McNairy County|     6| 233.518|  5.560|   410| 15957.033| 244.637|  25,694|
| |Marion County|     5| 172.968|  4.942|   240|  8302.487| 118.607|  28,907|
| |White County|     5| 182.849|  0.000|   327| 11958.310| 282.110|  27,345|
| |Polk County|     5| 297.053| 16.974|   237| 14080.323| 356.464|  16,832|
| |Cocke County|     5| 138.873| 11.903|   525| 14581.713| 297.586|  36,004|
| |Weakley County|     5| 150.024|  4.286|   557| 16712.674| 685.824|  33,328|
| |Warren County|     4| 96.906|  0.000|   587| 14220.995| 308.023|  41,277|
| |Marshall County|     4| 116.364|  4.156|   336|  9774.545| 220.260|  34,375|
| |Obion County|     4| 133.027|  0.000|   639| 21251.122| 570.117|  30,069|
| |Jefferson County|     4| 73.401|  2.621|   639| 11725.846| 228.068|  54,495|
| |Smith County|     4| 198.442|  0.000|   476| 23614.625| 212.617|  20,157|
| |Dickson County|     4| 74.145|  5.296|   757| 14032.031| 240.973|  53,948|
| |Franklin County|     4| 94.769|  0.000|   363|  8600.265| 169.230|  42,208|
| |Humphreys County|     3| 161.447|  0.000|   135|  7265.095| 115.319|  18,582|
| |Decatur County|     3| 257.224|  0.000|   234| 20063.449| 440.955|  11,663|
| |Coffee County|     3| 53.079|  0.000|   594| 10509.554| 219.897|  56,520|
| |Loudon County|     3| 55.486|  0.000|   788| 14574.240| 184.952|  54,068|
| |Washington County|     2| 15.459|  0.000| 1,391| 10751.691| 210.904| 129,375|
| |Scott County|     2| 90.629| 12.947|   134|  6072.141| 103.576|  22,068|
| |Henderson County|     2| 71.131|  0.000|   661| 23508.909| 579.212|  28,117|
| |Wayne County|     2| 119.954|  0.000|   232| 13914.712| 59.977|  16,673|
| |Rhea County|     2| 60.301|  4.307|   574| 17306.359| 223.975|  33,167|
| |Chester County|     2| 115.627|  0.000|   251| 14511.187| 330.363|  17,297|
| |Bledsoe County|     2| 132.767|  9.483|   734| 48725.438| 417.267|  15,064|
| |Roane County|     2| 37.466|  0.000|   516|  9666.180| 222.119|  53,382|
| |Hancock County|     2| 302.115| 21.580|    84| 12688.822| 129.478|   6,620|
| |DeKalb County|     2| 97.609|  0.000|   384| 18740.849| 313.742|  20,490|
| |Grundy County|     2| 148.954|  0.000|   126|  9384.077| 159.593|  13,427|
| |Morgan County|     1| 46.722|  0.000|   135|  6307.527| 213.588|  21,403|
| |Lincoln County|     1| 29.099|  0.000|   335|  9748.007| 245.259|  34,366|
| |Henry County|     1| 30.917|  4.417|   316|  9769.671| 220.833|  32,345|
| |Hickman County|     1| 39.717|  5.674|   292| 11597.426| 221.282|  25,178|
| |Pickett County|     1| 198.098|  0.000|    40|  7923.930| 254.698|   5,048|
| |Jackson County|     1| 84.846|  0.000|   145| 12302.732| 327.265|  11,786|
| |Overton County|     1| 44.962|  0.000|   250| 11240.502| 481.736|  22,241|
| |Lewis County|     1| 81.513|  0.000|    81|  6602.543| 116.447|  12,268|
| |Campbell County|     1| 25.099|  0.000|   264|  6626.173| 89.640|  39,842|
| |Grainger County|     1| 42.882|  6.126|   217|  9305.317| 140.897|  23,320|
| |Sequatchie County|     1| 66.551|  9.507|   117|  7786.503| 142.610|  15,026|
| |Benton County|     1| 61.881|  0.000|   179| 11076.733| 353.607|  16,160|
| |Lake County|     0|  0.000|  0.000|   800| 114025.086| 366.509|   7,016|
| |Johnson County|     0|  0.000|  0.000|   319| 17933.438| 489.897|  17,788|
| |Houston County|     0|  0.000|  0.000|    63|  7681.990| 104.517|   8,201|
| |Fentress County|     0|  0.000|  0.000|   106|  5722.615| 138.824|  18,523|
| |Clay County|     0|  0.000|  0.000|    86| 11293.500| 225.120|   7,615|
| |Claiborne County|     0|  0.000|  0.000|   301|  9418.317| 205.621|  31,959|
| |Cannon County|     0|  0.000|  0.000|   160| 10900.668| 175.189|  14,678|
| |Moore County|     0|  0.000|  0.000|    74| 11405.672| 308.261|   6,488|
| |Perry County|     0|  0.000|  0.000|    86| 10648.836| 159.202|   8,076|
| |Van Buren County|     0|  0.000|  0.000|    43|  7322.888| 194.628|   5,872|
| |Union County|     0|  0.000|  0.000|   170|  8511.917| 143.057|  19,972|
| |Unicoi County|     0|  0.000|  0.000|   180| 10065.425| 191.722|  17,883|
| |Stewart County|     0|  0.000|  0.000|    81|  5905.942| 83.329|  13,715|
| |Meigs County|     0|  0.000|  0.000|   115|  9257.768| 161.005|  12,422|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,300| 211.815| N/A|58,353|  9507.729| N/A|6,137,428|
| |St. Louis County|   854| 858.978|  2.874|21,612| 21737.972| 286.086| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,520| 11243.166| 201.126| 402,022|
| |Jackson County|    66| 93.882|  0.406| 4,451|  6331.338| 110.138| 703,011|
| |Jasper County|    32| 263.748|  2.355| 1,891| 15585.850| 180.149| 121,328|
| |Jefferson County|    27| 119.957|  1.904| 1,833|  8143.735| 183.426| 225,081|
| |Clay County|    22| 88.018|  1.143| 1,126|  4504.937| 65.728| 249,948|
| |Franklin County|    18| 173.132|  0.000|   704|  6771.379| 156.643| 103,967|
| |Scott County|    13| 339.603|  0.000|   449| 11729.363| 253.769|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,775|  6056.243| 163.287| 293,086|
| |Platte County|    10| 95.769|  0.000|   401|  3840.334| 79.351| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,117| 12785.587| 67.043|  87,364|
| |Stoddard County|     9| 310.078|  0.000|   239|  8234.281| 73.828|  29,025|
| |Pemiscot County|     9| 569.440|  0.000|   251| 15881.050| 153.658|  15,805|
| |Cass County|     9| 85.082|  0.000|   830|  7846.474| 168.814| 105,780|
| |Gentry County|     9| 1369.655|  0.000|    86| 13087.810| 65.222|   6,571|
| |McDonald County|     8| 350.309|  6.256|   955| 41818.102| 31.278|  22,837|
| |Saline County|     7| 307.544|  0.000|   478| 21000.835| 338.926|  22,761|
| |Camden County|     7| 151.172|  6.170|   388|  8379.225| 151.172|  46,305|
| |Newton County|     6| 103.029|  0.000|   923| 15849.303| 134.919|  58,236|
| |Pettis County|     6| 141.713|  6.748|   624| 14738.185| 462.255|  42,339|
| |Cape Girardeau County|     5| 63.395|  0.000|   732|  9280.978| 173.882|  78,871|
| |Barry County|     4| 111.766|  0.000|   280|  7823.633| 127.733|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   372| 12769.901| 353.085|  29,131|
| |Perry County|     4| 209.030|  0.000|   254| 13273.411| 231.426|  19,136|
| |Cole County|     3| 39.090|  0.000|   496|  6462.962| 223.374|  76,745|
| |New Madrid County|     3| 175.685| 16.732|   285| 16690.091| 460.128|  17,076|
| |Boone County|     3| 16.624|  0.000| 1,525|  8450.486| 155.948| 180,463|
| |Johnson County|     3| 55.492|  2.642|   504|  9322.630| 47.564|  54,062|
| |Taney County|     3| 53.640|  0.000|   685| 12247.890| 349.940|  55,928|
| |Henry County|     3| 137.463|  0.000|    92|  4215.543| 104.734|  21,824|
| |Moniteau County|     2| 123.977|  0.000|   160|  9918.175| 185.966|  16,132|
| |St. Francois County|     2| 29.755|  0.000|   478|  7111.508| 272.048|  67,215|
| |Lawrence County|     2| 52.144|  0.000|   247|  6439.838| 134.086|  38,355|
| |Lafayette County|     2| 61.147|  0.000|   194|  5931.271| 82.985|  32,708|
| |Howell County|     2| 49.854|  0.000|   169|  4212.678| 60.537|  40,117|
| |Douglas County|     2| 151.688|  0.000|    89|  6750.095| 65.009|  13,185|
| |Butler County|     2| 47.083|  0.000|   302|  7109.563| 90.803|  42,478|
| |Benton County|     2| 102.865|  7.347|   116|  5966.157| 191.035|  19,443|
| |Pulaski County|     1| 19.009|  0.000|   262|  4980.326| 176.511|  52,607|
| |Audrain County|     1| 39.389|  0.000|   217|  8547.345| 101.285|  25,388|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313|  0.000|   4,696|
| |Pike County|     1| 54.639|  0.000|   142|  7758.715| 366.861|  18,302|
| |Randolph County|     1| 40.407|  0.000|    76|  3070.955| 51.952|  24,748|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Andrew County|     1| 56.459|  0.000|    95|  5363.595| 56.459|  17,712|
| |Grundy County|     1| 101.523|  0.000|    30|  3045.685| 72.516|   9,850|
| |Dallas County|     1| 59.249|  0.000|    73|  4325.157| 110.033|  16,878|
| |Bates County|     1| 61.835|  0.000|    54|  3339.105| 88.336|  16,172|
| |Laclede County|     1| 27.993|  0.000|   221|  6186.490| 103.975|  35,723|
| |Lewis County|     1| 102.291|  0.000|    54|  5523.732| 204.583|   9,776|
| |DeKalb County|     1| 79.700|  0.000|    40|  3188.013| 56.929|  12,547|
| |Lincoln County|     1| 16.945|  0.000|   421|  7134.021| 147.667|  59,013|
| |Linn County|     1| 83.893|  0.000|    38|  3187.919| 107.862|  11,920|
| |Osage County|     1| 73.448|  0.000|    55|  4039.662| 104.926|  13,615|
| |Callaway County|     1| 22.350|  0.000|   170|  3799.477| 89.399|  44,743|
| |Christian County|     1| 11.287|  0.000|   411|  4639.088| 122.548|  88,595|
| |Shannon County|     1| 122.459|  0.000|    44|  5388.195| 17.494|   8,166|
| |Webster County|     1| 25.258|  0.000|   147|  3712.871| 68.556|  39,592|
| |Washington County|     1| 40.437|  0.000|   124|  5014.153| 317.717|  24,730|
| |Texas County|     1| 39.373|  5.625|    63|  2480.510| 73.122|  25,398|
| |Stone County|     1| 31.297|  0.000|   161|  5038.808| 169.898|  31,952|
| |Scotland County|     1| 203.998|  0.000|    16|  3263.974| 58.285|   4,902|
| |Carter County|     1| 167.168|  0.000|    21|  3510.532| 23.881|   5,982|
| |Marion County|     1| 35.051|  0.000|   256|  8973.011| 375.545|  28,530|
| |Miller County|     1| 39.034|  0.000|   144|  5620.828| 167.287|  25,619|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131|  0.000|   9,020|
| |Bollinger County|     1| 82.420|  0.000|    80|  6593.588| 188.388|  12,133|
| |Ste. Genevieve County|     1| 55.885|  0.000|    66|  3688.387| 103.786|  17,894|
| |Ripley County|     0|  0.000|  0.000|    60|  4515.352| 96.758|  13,288|
| |Hickory County|     0|  0.000|  0.000|    37|  3876.781| 134.714|   9,544|
| |Maries County|     0|  0.000|  0.000|    27|  3104.519| 114.982|   8,697|
| |Mississippi County|     0|  0.000|  0.000|   167| 12670.713| 357.685|  13,180|
| |Phelps County|     0|  0.000|  0.000|   114|  2557.602| 105.766|  44,573|
| |Ozark County|     0|  0.000|  0.000|    16|  1744.059| 62.288|   9,174|
| |Oregon County|     0|  0.000|  0.000|    21|  1994.491| 94.976|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   220|  9958.356| 290.991|  22,092|
| |Morgan County|     0|  0.000|  0.000|    92|  4460.174| 96.960|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    44|  3809.194| 37.103|  11,551|
| |Monroe County|     0|  0.000|  0.000|    34|  3933.364| 115.687|   8,644|
| |Mercer County|     0|  0.000|  0.000|    15|  4147.083| 197.480|   3,617|
| |Holt County|     0|  0.000|  0.000|    41|  9311.833| 1070.699|   4,403|
| |Madison County|     0|  0.000|  0.000|    30|  2481.800| 70.909|  12,088|
| |Macon County|     0|  0.000|  0.000|    66|  4365.946| 85.051|  15,117|
| |Livingston County|     0|  0.000|  0.000|    64|  4203.060| 37.527|  15,227|
| |Knox County|     0|  0.000|  0.000|    35|  8840.616| 288.673|   3,959|
| |Iron County|     0|  0.000|  0.000|    23|  2271.605| 28.219|  10,125|
| |Howard County|     0|  0.000|  0.000|    65|  6499.350| 228.549|  10,001|
| |Polk County|     0|  0.000|  0.000|   227|  7060.873| 79.985|  32,149|
| |Dent County|     0|  0.000|  0.000|    18|  1155.847| 73.387|  15,573|
| |Cooper County|     0|  0.000|  0.000|   157|  8865.549| 330.744|  17,709|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    49|  4753.128| 277.150|  10,309|
| |Cedar County|     0|  0.000|  0.000|    41|  2857.342| 29.868|  14,349|
| |Daviess County|     0|  0.000|  0.000|    19|  2295.240| 34.515|   8,278|
| |Dade County|     0|  0.000|  0.000|    17|  2248.380| 37.788|   7,561|
| |Crawford County|     0|  0.000|  0.000|    97|  4055.184| 155.280|  23,920|
| |Clinton County|     0|  0.000|  0.000|    93|  4561.731| 98.102|  20,387|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Clark County|     0|  0.000|  0.000|    27|  3972.341| 147.124|   6,797|
| |Chariton County|     0|  0.000|  0.000|    21|  2827.902| 76.950|   7,426|
| |Carroll County|     0|  0.000|  0.000|   102| 11752.506| 32.920|   8,679|
| |Gasconade County|     0|  0.000|  0.000|    34|  2311.982| 126.285|  14,706|
| |Barton County|     0|  0.000|  0.000|    71|  6040.497| 24.308|  11,754|
| |Atchison County|     0|  0.000|  0.000|    19|  3694.342| 138.885|   5,143|
| |Adair County|     0|  0.000|  0.000|   178|  7023.636| 146.561|  25,343|
| |Wright County|     0|  0.000|  0.000|    70|  3827.437| 70.300|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    63|  4893.964| 88.779|  12,873|
| |Warren County|     0|  0.000|  0.000|   226|  6339.589| 140.256|  35,649|
| |Vernon County|     0|  0.000|  0.000|    59|  2869.231| 69.473|  20,563|
| |Sullivan County|     0|  0.000|  0.000|   152| 24963.048| 258.077|   6,089|
| |Shelby County|     0|  0.000|  0.000|    42|  7082.631| 289.087|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    10|  2145.923|  0.000|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    23|  2447.590| 76.012|   9,397|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867| 18.619|  23,018|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties| 1,037| 336.671| N/A|59,375| 19276.621| N/A|3,080,156|
| |Clark County|   884| 389.992|  7.185|51,457| 22701.134| 281.528|2,266,715|
| |Washoe County|   124| 262.980|  1.818| 6,117| 12972.966| 148.456| 471,519|
| |Nye County|    12| 257.937|  9.212|   421|  9049.287| 64.484|  46,523|
| |Lyon County|     6| 104.330|  0.000|   259|  4503.565| 101.846|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074| 33.951|  16,831|
| |Elko County|     3| 56.842|  2.707|   613| 11614.688| 238.194|  52,778|
| |Churchill County|     1| 40.146|  0.000|    81|  3251.837| 177.790|  24,909|
| |Douglas County|     1| 20.448|  2.921|   215|  4396.278| 61.343|  48,905|
| |White Pine County|     1| 104.384|  0.000|    16|  1670.146| 29.824|   9,580|
| |Lander County|     1| 180.766|  0.000|    52|  9399.855| 25.824|   5,532|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     6|  1455.251| 69.298|   4,123|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Eureka County|     0|  0.000|  0.000|     4|  1971.414| 140.815|   2,029|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,025| 176.043| N/A|64,227| 11030.954| N/A|5,822,434|
| |Milwaukee County|   462| 488.514|  1.359|21,879| 23134.608| 187.611| 945,726|
| |Racine County|    78| 397.329|  0.000| 3,643| 18557.289| 133.898| 196,311|
| |Waukesha County|    63| 155.864|  1.767| 4,657| 11521.581| 221.603| 404,198|
| |Kenosha County|    60| 353.855|  0.843| 2,734| 16123.991| 105.314| 169,561|
| |Brown County|    55| 207.906|  1.620| 4,425| 16727.023| 125.284| 264,542|
| |Dane County|    38| 69.509|  0.000| 4,749|  8686.745| 81.790| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,470|  8998.861| 52.471| 163,354|
| |Walworth County|    24| 231.063|  1.375| 1,430| 13767.474| 181.549| 103,868|
| |Washington County|    23| 169.075|  1.050| 1,188|  8733.111| 206.881| 136,034|
| |Winnebago County|    19| 110.525|  0.831| 1,248|  7259.739| 103.046| 171,907|
| |Ozaukee County|    18| 201.746|  1.601|   757|  8484.550| 176.128|  89,221|
| |Grant County|    16| 311.048|  2.777|   387|  7523.474| 113.866|  51,439|
| |Waupaca County|    16| 313.787|  2.802|   507|  9943.126| 215.729|  50,990|
| |Outagamie County|    14| 74.514|  0.000| 1,354|  7206.536| 111.010| 187,885|
| |Marathon County|    11| 81.066|  2.106|   680|  5011.349| 60.010| 135,692|
| |Fond du Lac County|     8| 77.367|  1.382|   744|  7195.149| 182.366| 103,403|
| |Sheboygan County|     8| 69.360|  0.000|   814|  7057.396| 100.325| 115,340|
| |Clark County|     8| 230.057|  4.108|   196|  5636.395| 53.406|  34,774|
| |St. Croix County|     6| 66.162|  1.575|   528|  5822.224| 74.038|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   690|  8139.768| 131.450|  84,769|
| |Dodge County|     5| 56.922|  0.000|   894| 10177.711| 182.151|  87,839|
| |Marinette County|     5| 123.916|  7.081|   479| 11871.128| 364.666|  40,350|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679|  8.281|  17,252|
| |Eau Claire County|     4| 38.224|  0.000|   645|  6163.637| 111.942| 104,646|
| |Forest County|     4| 444.247|  0.000|    60|  6663.705| 15.866|   9,004|
| |Barron County|     3| 66.307|  0.000|   320|  7072.761| 119.984|  45,244|
| |Door County|     3| 108.429|  0.000|   109|  3939.569| 36.143|  27,668|
| |Sauk County|     3| 46.553|  0.000|   495|  7681.326| 155.178|  64,442|
| |Pierce County|     3| 70.169|  3.341|   232|  5426.393| 93.558|  42,754|
| |Columbia County|     2| 34.763|  2.483|   279|  4849.475| 94.357|  57,532|
| |Calumet County|     2| 39.929|  0.000|   372|  7426.780| 216.757|  50,089|
| |Buffalo County|     2| 153.480|  0.000|    45|  3453.304| 10.963|  13,031|
| |Adams County|     2| 98.912|  0.000|    93|  4599.407| 77.717|  20,220|
| |Polk County|     2| 45.680|  0.000|   140|  3197.588| 45.680|  43,783|
| |Trempealeau County|     2| 67.456|  0.000|   364| 12276.974| 154.185|  29,649|
| |Monroe County|     2| 43.240|  0.000|   249|  5383.435| 21.620|  46,253|
| |Kewaunee County|     2| 97.876|  0.000|   141|  6900.264| 97.876|  20,434|
| |Wood County|     2| 27.398|  1.957|   357|  4890.478| 158.515|  72,999|
| |Manitowoc County|     1| 12.661|  0.000|   373|  4722.655| 86.820|  78,981|
| |Rusk County|     1| 70.532|  0.000|    21|  1481.168| 40.304|  14,178|
| |Langlade County|     1| 52.113|  0.000|    70|  3647.923| 81.892|  19,189|
| |Oconto County|     1| 26.364|  3.766|   263|  6933.825| 165.719|  37,930|
| |Jackson County|     1| 48.443|  0.000|    61|  2954.997| 41.522|  20,643|
| |Burnett County|     1| 64.876|  0.000|    28|  1816.530| 64.876|  15,414|
| |Bayfield County|     1| 66.507|  0.000|    32|  2128.226| 95.010|  15,036|
| |Ashland County|     1| 64.259|  0.000|    30|  1927.773| 55.079|  15,562|
| |Green County|     1| 27.056|  0.000|   194|  5248.918| 173.933|  36,960|
| |Juneau County|     1| 37.471|  0.000|   149|  5583.243| 74.943|  26,687|
| |La Crosse County|     1|  8.473|  0.000|   951|  8058.229| 75.050| 118,016|
| |Marquette County|     1| 64.210|  0.000|    81|  5200.976| 45.864|  15,574|
| |Iron County|     1| 175.840|  0.000|    78| 13715.491| 100.480|   5,687|
| |Taylor County|     1| 49.157|  7.022|    77|  3785.086| 91.291|  20,343|
| |Waushara County|     1| 40.912|  0.000|   122|  4991.204| 46.756|  24,443|
| |Crawford County|     0|  0.000|  0.000|    84|  5207.365| 106.273|  16,131|
| |Oneida County|     0|  0.000|  0.000|   170|  4775.952| 232.777|  35,595|
| |Shawano County|     0|  0.000|  0.000|   210|  5134.600| 111.774|  40,899|
| |Vilas County|     0|  0.000|  0.000|    69|  3108.808| 135.166|  22,195|
| |Portage County|     0|  0.000|  0.000|   448|  6330.187| 119.095|  70,772|
| |Pepin County|     0|  0.000|  0.000|    43|  5900.919| 19.604|   7,287|
| |Green Lake County|     0|  0.000|  0.000|    61|  3225.295| 45.320|  18,913|
| |Sawyer County|     0|  0.000|  0.000|    92|  5556.227| 345.107|  16,558|
| |Florence County|     0|  0.000|  0.000|    12|  2793.946| 166.306|   4,295|
| |Price County|     0|  0.000|  0.000|    32|  2396.824| 32.100|  13,351|
| |Chippewa County|     0|  0.000|  0.000|   259|  4005.691| 79.539|  64,658|
| |Washburn County|     0|  0.000|  0.000|    48|  3053.435| 63.613|  15,720|
| |Dunn County|     0|  0.000|  0.000|   138|  3041.792| 59.828|  45,368|
| |Lafayette County|     0|  0.000|  0.000|   166|  9960.996| 377.181|  16,665|
| |Douglas County|     0|  0.000|  0.000|   212|  4913.094| 175.468|  43,150|
| |Lincoln County|     0|  0.000|  0.000|    73|  2645.599| 31.064|  27,593|
| |Iowa County|     0|  0.000|  0.000|    93|  3927.697| 114.633|  23,678|
| |Menominee County|     0|  0.000|  0.000|    26|  5706.760| 188.135|   4,556|
| |Vernon County|     0|  0.000|  0.000|    70|  2271.105| 50.984|  30,822|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   970| 307.442| N/A|51,242| 16241.161| N/A|3,155,070|
| |Polk County|   210| 428.431|  1.166|10,800| 22033.577| 194.688| 490,161|
| |Linn County|    89| 392.579|  1.260| 2,503| 11040.731| 119.097| 226,706|
| |Black Hawk County|    66| 502.941|  3.266| 3,245| 24727.954| 158.938| 131,228|
| |Woodbury County|    54| 523.728|  4.157| 3,783| 36690.040| 102.529| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   880| 20626.289| 117.195|  42,664|
| |Wapello County|    36| 1029.483| 12.256|   943| 26966.742| 273.712|  34,969|
| |Dallas County|    35| 374.520|  0.000| 1,951| 20876.804| 140.636|  93,453|
| |Dubuque County|    31| 318.566|  0.000| 1,770| 18189.105| 171.762|  97,311|
| |Tama County|    29| 1720.660|  0.000|   561| 33285.867| 118.666|  16,854|
| |Pottawattamie County|    29| 311.139|  4.598| 1,400| 15020.492| 162.467|  93,206|
| |Jasper County|    28| 752.992|  7.684|   490| 13177.356| 72.994|  37,185|
| |Marshall County|    27| 685.819|  7.257| 1,475| 37466.027| 156.033|  39,369|
| |Johnson County|    21| 138.944|  4.726| 2,165| 14324.467| 104.917| 151,140|
| |Cerro Gordo County|    19| 447.585|  6.731|   671| 15806.832| 245.667|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   144|  6517.312| 38.794|  22,095|
| |Scott County|    15| 86.734|  0.826| 1,808| 10454.312| 110.689| 172,943|
| |Story County|    15| 154.453|  1.471| 1,203| 12387.121| 76.491|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Plymouth County|    12| 476.625| 17.022|   493| 19581.364| 215.616|  25,177|
| |Buena Vista County|    12| 611.621|  0.000| 1,801| 91794.088| 72.812|  19,620|
| |Franklin County|    12| 1191.658| 42.559|   259| 25719.960| 340.474|  10,070|
| |Washington County|    10| 455.270|  0.000|   307| 13976.781| 84.550|  21,965|
| |Webster County|     8| 222.816|  3.979|   867| 24147.727| 294.436|  35,904|
| |Poweshiek County|     8| 432.339|  0.000|   160|  8646.779| 30.881|  18,504|
| |Monroe County|     8| 1038.017| 18.536|    75|  9731.413| 55.608|   7,707|
| |Bremer County|     7| 279.307|  0.000|   240|  9576.251| 171.004|  25,062|
| |O'Brien County|     5| 363.557| 31.162|   146| 10615.866| 103.873|  13,753|
| |Lee County|     5| 148.558|  8.489|   141|  4189.322| 140.069|  33,657|
| |Guthrie County|     5| 467.771|  0.000|   142| 13284.685| 147.014|  10,689|
| |Emmet County|     4| 434.405|  0.000|   197| 21394.440| 108.601|   9,208|
| |Clinton County|     4| 86.153|  3.077|   450|  9692.218| 246.152|  46,429|
| |Allamakee County|     4| 292.248|  0.000|   162| 11836.049| 83.499|  13,687|
| |Dickinson County|     4| 231.777|  0.000|   387| 22424.383| 74.500|  17,258|
| |Montgomery County|     4| 403.348|  0.000|    62|  6251.891| 72.026|   9,917|
| |Henry County|     4| 200.461|  7.159|   146|  7316.829| 193.302|  19,954|
| |Lucas County|     4| 465.116|  0.000|    74|  8604.651| 232.558|   8,600|
| |Appanoose County|     3| 241.429|  0.000|    53|  4265.250| 57.483|  12,426|
| |Boone County|     3| 114.355|  5.445|   278| 10596.935| 174.256|  26,234|
| |Floyd County|     3| 191.791|  9.133|   175| 11187.828| 273.988|  15,642|
| |Clayton County|     3| 170.950|  0.000|   116|  6610.063| 97.686|  17,549|
| |Crawford County|     3| 178.359|  0.000|   743| 44173.603| 144.386|  16,820|
| |Clarke County|     3| 319.319|  0.000|   210| 22352.315| 197.674|   9,395|
| |Sioux County|     3| 86.071|  0.000|   671| 19251.183| 213.128|  34,855|
| |Des Moines County|     2| 51.325|  0.000|   226|  5799.779| 249.295|  38,967|
| |Davis County|     2| 222.222| 15.873|    62|  6888.889| 126.984|   9,000|
| |Jones County|     2| 96.707|  0.000|   136|  6576.084| 55.261|  20,681|
| |Hancock County|     2| 188.147|  0.000|   125| 11759.172| 53.756|  10,630|
| |Madison County|     2| 122.414|  0.000|   130|  7956.910| 139.902|  16,338|
| |Lyon County|     2| 170.140|  0.000|   124| 10548.703| 170.140|  11,755|
| |Warren County|     2| 38.861|  2.776|   597| 11599.891| 130.461|  51,466|
| |Butler County|     2| 138.514|  0.000|   133|  9211.164| 138.514|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    92|  9515.929| 132.987|   9,668|
| |Carroll County|     2| 99.182|  7.084|   208| 10314.902| 162.941|  20,165|
| |Pocahontas County|     2| 302.160| 21.583|   120| 18129.627| 107.914|   6,619|
| |Grundy County|     1| 81.753|  0.000|    86|  7030.739| 93.432|  12,232|
| |Hamilton County|     1| 67.691|  0.000|   256| 17328.911| 106.372|  14,773|
| |Buchanan County|     1| 47.226|  0.000|   140|  6611.570| 107.944|  21,175|
| |Audubon County|     1| 181.951|  0.000|    30|  5458.515| 51.986|   5,496|
| |Benton County|     1| 38.994|  0.000|   164|  6395.009| 72.417|  25,645|
| |Delaware County|     1| 58.785|  0.000|   129|  7583.328| 218.346|  17,011|
| |Harrison County|     1| 71.179| 10.168|   116|  8256.815| 132.190|  14,049|
| |Wright County|     1| 79.605|  0.000|   485| 38608.502| 250.188|  12,562|
| |Mills County|     1| 66.186|  9.455|    95|  6287.643| 75.641|  15,109|
| |Winneshiek County|     1| 50.023|  0.000|   106|  5302.386| 85.753|  19,991|
| |Cass County|     1| 77.906|  0.000|    90|  7011.530| 322.753|  12,836|
| |Cedar County|     1| 53.686|  0.000|   136|  7301.229| 53.686|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   110|  9790.832| 76.292|  11,235|
| |Clay County|     1| 62.438|  0.000|   210| 13111.888| 258.670|  16,016|
| |Wayne County|     1| 155.255|  0.000|    21|  3260.363| 44.359|   6,441|
| |Keokuk County|     1| 97.599|  0.000|    41|  4001.562| 97.599|  10,246|
| |Van Buren County|     1| 141.965|  0.000|    39|  5536.627| 101.403|   7,044|
| |Union County|     1| 81.693|  0.000|    83|  6780.492| 81.693|  12,241|
| |Monona County|     1| 116.077| 16.582|    93| 10795.125| 33.165|   8,615|
| |Shelby County|     1| 87.306|  0.000|   193| 16850.009| 162.139|  11,454|
| |Ringgold County|     1| 204.332|  0.000|    24|  4903.964| 87.571|   4,894|
| |Humboldt County|     1| 104.624|  0.000|   127| 13287.299| 313.873|   9,558|
| |Iowa County|     1| 61.789|  0.000|    98|  6055.363| 17.654|  16,184|
| |Jackson County|     1| 51.443|  0.000|   167|  8590.977| 124.933|  19,439|
| |Howard County|     0|  0.000|  0.000|    55|  6005.678| 93.595|   9,158|
| |Jefferson County|     0|  0.000|  0.000|    89|  4864.717| 54.660|  18,295|
| |Sac County|     0|  0.000|  0.000|    87|  8949.697| 73.479|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    98| 11028.584| 257.226|   8,886|
| |Page County|     0|  0.000|  0.000|   101|  6685.642| 66.194|  15,107|
| |Osceola County|     0|  0.000|  0.000|    88| 14770.057| 191.819|   5,958|
| |Mitchell County|     0|  0.000|  0.000|    83|  7840.544| 67.475|  10,586|
| |Marion County|     0|  0.000|  0.000|   193|  5803.988| 115.994|  33,253|
| |Kossuth County|     0|  0.000|  0.000|   102|  6885.844| 173.593|  14,813|
| |Ida County|     0|  0.000|  0.000|    33|  4810.496| 83.299|   6,860|
| |Adams County|     0|  0.000|  0.000|    17|  4719.600| 39.661|   3,602|
| |Hardin County|     0|  0.000|  0.000|   189| 11219.281| 118.723|  16,846|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473| 16.073|   8,888|
| |Fremont County|     0|  0.000|  0.000|    45|  6465.517| 102.627|   6,960|
| |Fayette County|     0|  0.000|  0.000|    96|  4885.496| 101.781|  19,650|
| |Decatur County|     0|  0.000|  0.000|    28|  3557.814| 90.761|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    62|  5195.676| 95.773|  11,933|
| |Adair County|     0|  0.000|  0.000|    38|  5313.199| 199.744|   7,152|
| |Winnebago County|     0|  0.000|  0.000|   108| 10430.751| 400.121|  10,354|
| |Taylor County|     0|  0.000|  0.000|   100| 16337.200| 93.355|   6,121|
| |Worth County|     0|  0.000|  0.000|    71|  9619.293| 96.774|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   804| 179.959| N/A|38,298|  8572.248| N/A|4,467,673|
| |Jefferson County|   249| 324.744|  2.236| 9,149| 11932.072| 247.052| 766,757|
| |Fayette County|    49| 151.631|  0.884| 3,342| 10341.882| 158.263| 323,152|
| |Kenton County|    41| 245.512|  0.855| 1,490|  8922.263| 95.810| 166,998|
| |Hopkins County|    35| 783.243|  6.394|   438|  9801.728| 70.332|  44,686|
| |Graves County|    25| 670.853|  3.833|   574| 15402.780| 126.504|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,143|  8556.606| 71.653| 133,581|
| |Logan County|    23| 848.646|  0.000|   351| 12951.074| 163.404|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,737| 20595.052| 168.768| 132,896|
| |Shelby County|    21| 428.362|  0.000|   801| 16338.936| 177.756|  49,024|
| |Adair County|    19| 989.480|  0.000|   220| 11457.140| 119.035|  19,202|
| |Oldham County|    16| 239.525|  2.139|   653|  9775.595| 87.683|  66,799|
| |Butler County|    15| 1164.687|  0.000|   302| 23449.026| 110.923|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   154| 11553.755| 53.589|  13,329|
| |Campbell County|    13| 138.913|  0.000|   605|  6464.780| 73.273|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   112|  9218.107| 141.093|  12,150|
| |Casey County|    11| 680.735|  8.841|   209| 12933.969| 415.514|  16,159|
| |Muhlenberg County|    11| 359.219|  4.665|   633| 20671.413| 65.313|  30,622|
| |Grayson County|    11| 416.241|  0.000|   214|  8097.779| 108.115|  26,427|
| |Christian County|    10| 141.922|  8.110|   532|  7550.276| 87.181|  70,461|
| |Franklin County|     9| 176.502|  5.603|   348|  6824.734| 159.692|  50,991|
| |Daviess County|     9| 88.660|  0.000|   807|  7949.877| 80.217| 101,511|
| |Ohio County|     9| 375.094|  5.954|   364| 15170.459| 65.493|  23,994|
| |Hardin County|     8| 72.099|  0.000|   730|  6579.066| 198.273| 110,958|
| |Allen County|     8| 375.323|  0.000|   233| 10931.269| 60.320|  21,315|
| |Knox County|     8| 256.863|  0.000|   264|  8476.481| 146.779|  31,145|
| |Simpson County|     7| 376.911|  0.000|   160|  8615.120| 99.997|  18,572|
| |Clark County|     7| 193.034|  0.000|   179|  4936.161| 59.092|  36,263|
| |Gallatin County|     7| 789.266|  0.000|    82|  9245.687| 48.322|   8,869|
| |Grant County|     6| 239.339|  5.699|   127|  5066.018| 85.478|  25,069|
| |Bullitt County|     5| 61.217|  0.000|   434|  5313.678| 150.420|  81,676|
| |Pulaski County|     5| 76.948|  4.397|   367|  5647.979| 217.653|  64,979|
| |Russell County|     5| 278.971|  0.000|   136|  7588.015| 271.001|  17,923|
| |Clay County|     5| 251.244|  0.000|   184|  9245.767| 251.244|  19,901|
| |Laurel County|     5| 82.219|  0.000|   476|  7827.274| 133.900|  60,813|
| |Bell County|     5| 192.071| 10.976|   336| 12907.191| 181.096|  26,032|
| |McCracken County|     4| 61.145|  0.000|   397|  6068.666| 69.880|  65,418|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686|  0.000|   8,210|
| |Calloway County|     4| 102.561|  0.000|   273|  6999.821| 194.134|  39,001|
| |Barren County|     3| 67.798|  3.228|   421|  9514.339| 196.937|  44,249|
| |Boyd County|     3| 64.215|  0.000|   197|  4216.790| 36.694|  46,718|
| |Harlan County|     3| 115.340|  0.000|   257|  9880.815| 186.741|  26,010|
| |Henderson County|     3| 66.357|  0.000|   370|  8184.030| 104.275|  45,210|
| |Pike County|     3| 51.835|  0.000|   253|  4371.415| 49.367|  57,876|
| |Perry County|     3| 116.469|  0.000|   251|  9744.545| 210.753|  25,758|
| |Meade County|     3| 104.998|  5.000|   102|  3569.929| 10.000|  28,572|
| |Taylor County|     3| 116.419|  5.544|   150|  5820.948| 238.382|  25,769|
| |Carroll County|     2| 188.129|  0.000|   170| 15990.970| 268.756|  10,631|
| |Carter County|     2| 74.635|  5.331|   104|  3881.031| 10.662|  26,797|
| |Floyd County|     2| 56.197|  0.000|   114|  3203.237| 80.282|  35,589|
| |Fulton County|     2| 335.064| 23.933|    97| 16250.628| 526.530|   5,969|
| |Green County|     2| 182.799|  0.000|    54|  4935.563| 300.312|  10,941|
| |Lincoln County|     2| 81.470|  5.819|   118|  4806.713| 98.928|  24,549|
| |Marshall County|     2| 64.309|  0.000|   147|  4726.688| 45.935|  31,100|
| |Metcalfe County|     2| 198.590|  0.000|    64|  6354.880| 99.295|  10,071|
| |Nelson County|     2| 43.259|  0.000|   247|  5342.504| 123.598|  46,233|
| |Monroe County|     2| 187.793|  0.000|    99|  9295.775| 80.483|  10,650|
| |Breckinridge County|     2| 97.671|  0.000|    80|  3906.822| 104.647|  20,477|
| |Anderson County|     1| 43.962|  0.000|    89|  3912.604| 43.962|  22,747|
| |Clinton County|     1| 97.867| 13.981|    40|  3914.660| 167.771|  10,218|
| |Carlisle County|     1| 210.084|  0.000|    50| 10504.202| 240.096|   4,760|
| |Bourbon County|     1| 50.536|  0.000|    91|  4598.747| 115.510|  19,788|
| |Bath County|     1| 80.000|  0.000|    41|  3280.000| 45.714|  12,500|
| |Crittenden County|     1| 113.559|  0.000|    32|  3633.886| 48.668|   8,806|
| |Whitley County|     1| 27.576|  0.000|   168|  4632.694| 27.576|  36,264|
| |Webster County|     1| 77.268|  0.000|    91|  7031.371| 33.115|  12,942|
| |Henry County|     1| 62.012|  0.000|   136|  8433.586| 150.600|  16,126|
| |Knott County|     1| 67.540|  0.000|    73|  4930.434| 231.566|  14,806|
| |Mason County|     1| 58.582|  0.000|    56|  3280.609| 25.107|  17,070|
| |Madison County|     1| 10.754|  0.000|   623|  6699.861| 256.564|  92,987|
| |McLean County|     1| 108.613|  0.000|    44|  4778.973| 31.032|   9,207|
| |Livingston County|     1| 108.767|  0.000|    36|  3915.597| 46.614|   9,194|
| |Lewis County|     1| 75.330| 10.761|    84|  6327.684| 495.023|  13,275|
| |Larue County|     1| 69.454|  0.000|    65|  4514.516| 109.142|  14,398|
| |Greenup County|     1| 28.492|  0.000|   130|  3703.915| 97.686|  35,098|
| |Fleming County|     0|  0.000|  0.000|    64|  4389.274| 58.785|  14,581|
| |Johnson County|     0|  0.000|  0.000|    80|  3605.553| 206.032|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   366|  6763.374| 76.557|  54,115|
| |Hickman County|     0|  0.000|  0.000|    57| 13013.699| 521.853|   4,380|
| |Hart County|     0|  0.000|  0.000|   109|  5726.294| 120.080|  19,035|
| |Harrison County|     0|  0.000|  0.000|   123|  6512.761| 30.257|  18,886|
| |Hancock County|     0|  0.000|  0.000|    52|  5961.935| 32.758|   8,722|
| |Garrard County|     0|  0.000|  0.000|    90|  5094.532| 129.385|  17,666|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 91.147|  14,106|
| |Elliott County|     0|  0.000|  0.000|    14|  1862.445| 114.027|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    63|  9525.249| 367.186|   6,614|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Marion County|     0|  0.000|  0.000|   124|  6433.871| 29.649|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    49|  4029.274| 176.207|  12,161|
| |McCreary County|     0|  0.000|  0.000|    49|  2843.712| 99.488|  17,231|
| |Scott County|     0|  0.000|  0.000|   421|  7385.447| 147.859|  57,004|
| |Todd County|     0|  0.000|  0.000|    34|  2765.577|  0.000|  12,294|
| |Trimble County|     0|  0.000|  0.000|    34|  4013.694| 16.864|   8,471|
| |Trigg County|     0|  0.000|  0.000|    58|  3958.774| 29.252|  14,651|
| |Woodford County|     0|  0.000|  0.000|   175|  6545.971| 138.935|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    16|  2235.574| 59.881|   7,157|
| |Wayne County|     0|  0.000|  0.000|    76|  3737.766| 161.595|  20,333|
| |Washington County|     0|  0.000|  0.000|    96|  7937.164| 236.225|  12,095|
| |Union County|     0|  0.000|  0.000|    73|  5076.142| 79.470|  14,381|
| |Martin County|     0|  0.000|  0.000|    41|  3662.349| 76.565|  11,195|
| |Mercer County|     0|  0.000|  0.000|    87|  3966.626| 39.080|  21,933|
| |Caldwell County|     0|  0.000|  0.000|    55|  4314.741| 67.243|  12,747|
| |Lawrence County|     0|  0.000|  0.000|    37|  2415.617|  9.327|  15,317|
| |Lee County|     0|  0.000|  0.000|     6|   810.482|  0.000|   7,403|
| |Leslie County|     0|  0.000|  0.000|    33|  3341.095| 72.318|   9,877|
| |Montgomery County|     0|  0.000|  0.000|   130|  4616.969| 50.736|  28,157|
| |Breathitt County|     0|  0.000|  0.000|    32|  2533.650| 45.244|  12,630|
| |Bracken County|     0|  0.000|  0.000|    37|  4456.221| 120.438|   8,303|
| |Boyle County|     0|  0.000|  0.000|   167|  5555.556| 85.543|  30,060|
| |Ballard County|     0|  0.000|  0.000|    37|  4690.669| 72.443|   7,888|
| |Letcher County|     0|  0.000|  0.000|    63|  2923.027| 33.141|  21,553|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Rowan County|     0|  0.000|  0.000|    88|  3597.711| 105.128|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    84|  5031.447| 162.581|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    68|  5502.063| 173.384|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    50|  3427.005| 48.957|  14,590|
| |Owsley County|     0|  0.000|  0.000|    15|  3397.508| 64.714|   4,415|
| |Owen County|     0|  0.000|  0.000|    64|  5871.021| 235.889|  10,901|
| |Morgan County|     0|  0.000|  0.000|    33|  2479.525| 10.734|  13,309|
| |Spencer County|     0|  0.000|  0.000|   138|  7131.414| 199.325|  19,351|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   703| 335.268| N/A|21,855| 10422.881| N/A|2,096,829|
| |McKinley County|   232| 3250.802| 20.017| 4,104| 57505.570| 134.116|  71,367|
| |San Juan County|   187| 1508.575|  4.610| 3,084| 24879.395| 54.166| 123,958|
| |Bernalillo County|   134| 197.314|  0.841| 5,303|  7808.623| 51.327| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,152|  7850.192| 25.311| 146,748|
| |Dona Ana County|    32| 146.658|  1.309| 2,602| 11925.113| 133.563| 218,195|
| |Cibola County|    18| 674.789|  5.355|   377| 14133.083| 85.688|  26,675|
| |Otero County|    10| 148.170|  0.000|   204|  3022.670| 10.584|  67,490|
| |Rio Arriba County|     9| 231.238| 11.011|   323|  8298.862| 36.704|  38,921|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024| 25.760|  16,637|
| |Chaves County|     6| 92.858|  0.000|   518|  8016.714| 218.879|  64,615|
| |Lea County|     5| 70.353|  2.010|   890| 12522.865| 301.514|  71,070|
| |Luna County|     5| 210.890| 12.051|   256| 10797.587| 90.382|  23,709|
| |Eddy County|     4| 68.423|  0.000|   352|  6021.211| 166.170|  58,460|
| |Valencia County|     4| 52.159|  0.000|   449|  5854.893| 83.828|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   681|  4529.190| 52.256| 150,358|
| |Lincoln County|     2| 102.187|  0.000|   150|  7664.010| 233.570|  19,572|
| |Curry County|     2| 40.855|  0.000|   583| 11909.139| 145.910|  48,954|
| |Grant County|     2| 74.080|  0.000|    72|  2666.864|  5.291|  26,998|
| |Union County|     2| 492.732|  0.000|    30|  7390.983| 35.195|   4,059|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 11.964|  11,941|
| |Catron County|     1| 283.527|  0.000|     6|  1701.162| 40.504|   3,527|
| |Taos County|     1| 30.560|  0.000|   114|  3483.788| 34.925|  32,723|
| |Torrance County|     1| 64.679|  0.000|    62|  4010.090|  9.240|  15,461|
| |Quay County|     1| 121.168|  0.000|    44|  5331.395| 173.097|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   170|  9189.189| 77.220|  18,500|
| |Sierra County|     1| 92.670| 13.239|    32|  2965.434| 13.239|  10,791|
| |San Miguel County|     0|  0.000|  0.000|    51|  1869.707| 47.135|  27,277|
| |Los Alamos County|     0|  0.000|  0.000|    24|  1239.093| 29.502|  19,369|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 34.030|   4,198|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   644| 162.751| N/A|46,893| 11850.731| N/A|3,956,971|
| |Oklahoma County|   124| 155.499|  2.150|11,312| 14185.500| 181.296| 797,434|
| |Tulsa County|   113| 173.432|  1.535|11,130| 17082.290| 218.160| 651,552|
| |Cleveland County|    56| 197.173|  0.503| 3,151| 11094.524| 110.156| 284,014|
| |Washington County|    39| 756.885|  0.000|   676| 13119.335| 166.348|  51,527|
| |McCurtain County|    28| 852.827|  0.000|   884| 26924.951| 156.642|  32,832|
| |Wagoner County|    23| 282.941|  0.000|   940| 11563.680| 202.101|  81,289|
| |Delaware County|    20| 465.019|  3.322|   461| 10718.687| 139.506|  43,009|
| |Rogers County|    20| 216.312|  6.180| 1,081| 11691.669| 219.402|  92,459|
| |Caddo County|    18| 625.826|  9.934|   456| 15854.252| 258.277|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   559|  8220.951| 144.964|  67,997|
| |Creek County|    15| 209.726|  1.997|   663|  9269.875| 165.783|  71,522|
| |Osage County|    12| 255.520|  3.042|   456|  9709.772| 179.473|  46,963|
| |Kay County|    11| 252.653|  0.000|   256|  5879.921| 59.062|  43,538|
| |Comanche County|    10| 82.816|  0.000|   875|  7246.437| 91.098| 120,749|
| |Canadian County|     9| 60.685|  1.927| 1,298|  8752.175| 119.444| 148,306|
| |Pottawatomie County|     9| 123.981|  0.000|   480|  6612.299| 92.493|  72,592|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 25.010|   5,712|
| |Mayes County|     7| 170.316|  3.476|   360|  8759.124| 177.268|  41,100|
| |Jackson County|     7| 285.365| 11.648|   535| 21810.029| 122.299|  24,530|
| |Garfield County|     7| 114.649|  4.680|   555|  9090.016| 315.869|  61,056|
| |Texas County|     7| 350.298|  0.000| 1,076| 53845.769| 193.021|  19,983|
| |Grady County|     7| 125.372|  0.000|   460|  8238.708| 76.758|  55,834|
| |Adair County|     6| 270.343|  0.000|   361| 16265.657| 212.413|  22,194|
| |Carter County|     5| 103.926|  2.969|   361|  7503.482| 89.080|  48,111|
| |Seminole County|     5| 206.118|  0.000|   253| 10429.549| 153.116|  24,258|
| |Garvin County|     4| 144.347|  0.000|   238|  8588.647| 87.639|  27,711|
| |Sequoyah County|     4| 96.226|  0.000|   384|  9237.653| 223.381|  41,569|
| |Payne County|     4| 48.909|  0.000|   788|  9635.136| 124.020|  81,784|
| |McClain County|     4| 98.829|  0.000|   473| 11686.515| 162.362|  40,474|
| |Pittsburg County|     4| 91.630|  3.272|   419|  9598.204| 356.701|  43,654|
| |Okmulgee County|     3| 77.993|  0.000|   500| 12998.830| 174.556|  38,465|
| |Stephens County|     3| 69.536|  0.000|   215|  4983.427| 72.847|  43,143|
| |Pawnee County|     3| 183.195|  0.000|   153|  9342.941| 165.748|  16,376|
| |Ottawa County|     3| 96.379|  0.000|   405| 13011.212| 174.401|  31,127|
| |Lincoln County|     3| 86.017|  4.096|   224|  6422.571| 278.530|  34,877|
| |Pontotoc County|     2| 52.241|  0.000|   208|  5433.079| 55.973|  38,284|
| |Cotton County|     2| 352.983|  0.000|    21|  3706.318| 75.639|   5,666|
| |Noble County|     2| 179.678|  0.000|    89|  7995.688| 77.005|  11,131|
| |Hughes County|     2| 150.614| 10.758|   172| 12952.783| 494.874|  13,279|
| |Latimer County|     2| 198.551| 14.182|    96|  9530.428| 141.822|  10,073|
| |Cherokee County|     2| 41.104|  0.000|   481|  9885.525| 243.688|  48,657|
| |Nowata County|     1| 99.246|  0.000|    62|  6153.235| 70.890|  10,076|
| |Choctaw County|     1| 68.157|  0.000|   207| 14108.506| 311.575|  14,672|
| |Kiowa County|     1| 114.837|  0.000|    31|  3559.945| 65.621|   8,708|
| |Le Flore County|     1| 20.059|  0.000|   405|  8123.884| 269.363|  49,853|
| |Logan County|     1| 20.829|  0.000|   237|  4936.369| 104.143|  48,011|
| |McIntosh County|     1| 51.031|  0.000|   207| 10563.380| 211.413|  19,596|
| |Major County|     1| 131.079|  0.000|    38|  4980.994| 74.902|   7,629|
| |Beckham County|     1| 45.748|  0.000|    67|  3065.099| 98.031|  21,859|
| |Bryan County|     1| 20.836|  0.000|   494| 10292.739| 187.520|  47,995|
| |Marshall County|     1| 59.063|  0.000|   119|  7028.528| 109.689|  16,931|
| |Haskell County|     1| 79.195| 11.314|    81|  6414.825| 294.154|  12,627|
| |Craig County|     1| 70.711| 10.102|    92|  6505.445| 131.321|  14,142|
| |Roger Mills County|     1| 279.096| 39.871|     9|  2511.862| 39.871|   3,583|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 19.704|   7,250|
| |Okfuskee County|     1| 83.382|  0.000|    76|  6337.030| 166.764|  11,993|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672|  0.000|   3,859|
| |Cimarron County|     0|  0.000|  0.000|     3|  1403.837| 133.699|   2,137|
| |Harper County|     0|  0.000|  0.000|    11|  2982.646| 77.471|   3,688|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 269.237|   2,653|
| |Grant County|     0|  0.000|  0.000|    17|  3923.379| 131.878|   4,333|
| |Dewey County|     0|  0.000|  0.000|    12|  2453.486| 87.624|   4,891|
| |Custer County|     0|  0.000|  0.000|   222|  7654.381| 98.512|  29,003|
| |Coal County|     0|  0.000|  0.000|    43|  7825.296| 285.974|   5,495|
| |Blaine County|     0|  0.000|  0.000|    45|  4772.510| 60.603|   9,429|
| |Beaver County|     0|  0.000|  0.000|    39|  7343.250| 80.695|   5,311|
| |Atoka County|     0|  0.000|  0.000|    81|  5887.484| 134.986|  13,758|
| |Alfalfa County|     0|  0.000|  0.000|     5|   876.885| 50.108|   5,702|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 23.802|   6,002|
| |Johnston County|     0|  0.000|  0.000|    53|  4781.236| 90.212|  11,085|
| |Kingfisher County|     0|  0.000|  0.000|   151|  9578.180| 253.727|  15,765|
| |Love County|     0|  0.000|  0.000|    79|  7705.062| 83.599|  10,253|
| |Woodward County|     0|  0.000|  0.000|    47|  2325.466| 70.683|  20,211|
| |Woods County|     0|  0.000|  0.000|    21|  2388.263| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    32|  2931.477| 65.435|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   111| 10003.605| 51.499|  11,096|
| |Murray County|     0|  0.000|  0.000|    79|  5613.586| 101.512|  14,073|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   594| 841.659| N/A|13,118| 18587.345| N/A| 705,749|
| |District of Columbia|   594| 841.659|  1.012|13,118| 18587.345| 107.080| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   593| 608.977| N/A|16,080| 16513.241| N/A| 973,764|
| |New Castle County|   293| 524.382|  1.023| 7,450| 13333.262| 81.815| 558,753|
| |Sussex County|   192| 819.725|  0.000| 6,167| 26329.384| 222.009| 234,225|
| |Kent County|   108| 597.391|  0.790| 2,463| 13623.843| 154.089| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   587| 194.512| N/A|50,557| 16752.910| N/A|3,017,804|
| |Pulaski County|    88| 224.541|  1.823| 5,937| 15148.848| 193.193| 391,911|
| |Washington County|    53| 221.584|  1.195| 6,394| 26732.222| 97.354| 239,187|
| |Benton County|    43| 154.044|  1.024| 4,879| 17478.622| 92.631| 279,141|
| |Jefferson County|    41| 613.552|  2.138| 1,657| 24796.480| 369.841|  66,824|
| |Crittenden County|    24| 500.469| 11.916| 1,455| 30340.945| 381.310|  47,955|
| |Sebastian County|    21| 164.285|  2.235| 2,358| 18446.807| 311.805| 127,827|
| |Union County|    20| 517.036| 11.079|   539| 13934.130| 247.439|  38,682|
| |Garland County|    17| 171.050| 11.499| 1,155| 11621.355| 274.543|  99,386|
| |Yell County|    17| 796.589| 20.082| 1,086| 50887.962| 160.657|  21,341|
| |Mississippi County|    14| 344.395|  3.514| 1,097| 26985.806| 488.479|  40,651|
| |Hot Spring County|    13| 384.946|  8.460| 1,599| 47348.317| 435.708|  33,771|
| |Columbia County|    12| 511.574| 24.361|   227|  9677.282| 91.353|  23,457|
| |Lincoln County|    12| 921.376| 10.969| 1,228| 94287.469| 208.406|  13,024|
| |Craighead County|    12| 108.763|  0.000| 1,451| 13151.216| 172.208| 110,332|
| |Pope County|    11| 171.682|  2.230| 1,401| 21866.026| 265.327|  64,072|
| |Sevier County|    11| 646.792|  8.400| 1,034| 60798.495| 487.194|  17,007|
| |Newton County|    10| 1289.823| 73.704|   107| 13801.109| 55.278|   7,753|
| |Phillips County|     9| 506.130| 16.068|   336| 18895.512| 265.116|  17,782|
| |Chicot County|     9| 889.504| 14.119|   887| 87665.547| 2386.129|  10,118|
| |Nevada County|     9| 1090.645|  0.000|   146| 17692.681| 155.806|   8,252|
| |Lawrence County|     9| 548.580|  0.000|   226| 13775.448| 174.152|  16,406|
| |Lee County|     8| 903.240|  0.000|   901| 101727.447| 129.034|   8,857|
| |Saline County|     8| 65.340|  2.334| 1,184|  9670.279| 215.854| 122,437|
| |Carroll County|     7| 246.653|  0.000|   380| 13389.711| 151.012|  28,380|
| |Faulkner County|     6| 47.616|  0.000| 1,370| 10872.412| 104.303| 126,007|
| |Sharp County|     5| 286.664|  0.000|   125|  7166.609| 131.047|  17,442|
| |Ashley County|     5| 254.362|  0.000|   342| 17398.382| 276.165|  19,657|
| |Cleburne County|     5| 200.650|  0.000|   210|  8427.304| 91.726|  24,919|
| |Crawford County|     5| 79.043|  4.517|   695| 10986.926| 221.319|  63,257|
| |Miller County|     5| 115.588|  0.000|   533| 12321.705| 112.286|  43,257|
| |Randolph County|     4| 222.742|  7.955|   252| 14032.743| 365.933|  17,958|
| |Poinsett County|     4| 170.010|  6.072|   324| 13770.826| 510.031|  23,528|
| |Bradley County|     4| 371.644| 13.273|   213| 19790.021| 451.282|  10,763|
| |Clay County|     4| 274.895|  0.000|   143|  9827.503| 157.083|  14,551|
| |Cross County|     4| 243.620|  8.701|   220| 13399.111| 261.022|  16,419|
| |Howard County|     4| 302.984| 10.821|   364| 27571.580| 400.372|  13,202|
| |Ouachita County|     3| 128.304|  6.110|   111|  4747.241| 116.084|  23,382|
| |Little River County|     3| 244.718| 23.306|   196| 15988.254| 326.291|  12,259|
| |St. Francis County|     3| 120.029|  0.000| 1,236| 49451.868| 285.783|  24,994|
| |Conway County|     3| 143.913|  0.000|   161|  7723.304| 95.942|  20,846|
| |White County|     3| 38.094|  1.814|   370|  4698.234| 105.211|  78,753|
| |Drew County|     3| 164.663|  0.000|   240| 13173.061| 423.420|  18,219|
| |Greene County|     3| 66.189|  6.304|   526| 11605.074| 211.173|  45,325|
| |Johnson County|     2| 75.250|  0.000|   687| 25848.446| 134.375|  26,578|
| |Hempstead County|     2| 92.885|  0.000|   260| 12075.051| 179.135|  21,532|
| |Boone County|     2| 53.430|  3.816|   223|  5957.470| 83.962|  37,432|
| |Lafayette County|     2| 301.932|  0.000|    59|  8907.005| 150.966|   6,624|
| |Clark County|     2| 89.606|  6.400|   185|  8288.530| 51.203|  22,320|
| |Franklin County|     2| 112.899|  0.000|   138|  7790.008| 120.963|  17,715|
| |Lonoke County|     2| 27.282|  0.000|   556|  7584.335| 118.871|  73,309|
| |Independence County|     2| 52.875|  3.777|   589| 15571.712| 400.340|  37,825|
| |Madison County|     2| 120.656|  0.000|   277| 16710.907| 68.946|  16,576|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385|  8.634|  16,545|
| |Cleveland County|     2| 251.383|  0.000|   115| 14454.500| 395.030|   7,956|
| |Desha County|     2| 176.041|  0.000|   207| 18220.227| 251.487|  11,361|
| |Stone County|     1| 79.962|  0.000|    79|  6316.968| 171.346|  12,506|
| |Pike County|     1| 93.301|  0.000|   130| 12129.129| 439.848|  10,718|
| |Polk County|     1| 50.090|  0.000|   157|  7864.155| 121.648|  19,964|
| |Montgomery County|     1| 111.284|  0.000|    40|  4451.369| 95.386|   8,986|
| |Logan County|     1| 46.585|  0.000|   331| 15419.734| 652.194|  21,466|
| |Jackson County|     1| 59.812|  0.000|   120|  7177.463| 367.418|  16,719|
| |Izard County|     1| 73.373|  0.000|    64|  4695.869| 146.746|  13,629|
| |Arkansas County|     1| 57.189|  0.000|   243| 13896.832| 269.603|  17,486|
| |Dallas County|     1| 142.674| 20.382|    67|  9559.138| 122.292|   7,009|
| |Woodruff County|     0|  0.000|  0.000|    23|  3639.241| 45.208|   6,320|
| |Baxter County|     0|  0.000|  0.000|    81|  1931.699| 40.883|  41,932|
| |Prairie County|     0|  0.000|  0.000|   107| 13272.141| 354.396|   8,062|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 68.320|  10,455|
| |Monroe County|     0|  0.000|  0.000|    71| 10595.434| 277.144|   6,701|
| |Marion County|     0|  0.000|  0.000|    33|  1976.758| 68.459|  16,694|
| |Grant County|     0|  0.000|  0.000|   144|  7883.931| 86.035|  18,265|
| |Fulton County|     0|  0.000|  0.000|    47|  3766.931| 137.396|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    17|  3276.161| 55.062|   5,189|
| |Searcy County|     0|  0.000|  0.000|    32|  4060.398| 72.507|   7,881|
| |Scott County|     0|  0.000|  0.000|    72|  7003.210| 236.219|  10,281|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   423| 311.096| N/A| 6,964|  5121.677| N/A|1,359,711|
| |Hillsborough County|   281| 673.821|  0.685| 3,919|  9397.518| 32.543| 417,025|
| |Rockingham County|    96| 309.908|  0.000| 1,719|  5549.296| 18.908| 309,769|
| |Merrimack County|    23| 151.924|  1.887|   472|  3117.755|  8.493| 151,391|
| |Strafford County|    13| 99.515|  0.000|   366|  2801.742| 19.684| 130,633|
| |Belknap County|     4| 65.250|  0.000|   120|  1957.490| 11.652|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   106|  1393.179| 18.776|  76,085|
| |Carroll County|     1| 20.446|  0.000|    95|  1942.343|  5.842|  48,910|
| |Sullivan County|     1| 23.177|  0.000|    44|  1019.793| 13.244|  43,146|
| |Grafton County|     1| 11.125|  0.000|   106|  1179.272|  4.768|  89,886|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   403| 138.330| N/A|33,030| 11337.604| N/A|2,913,314|
| |Wyandotte County|   107| 646.803|  6.908| 5,137| 31052.597| 282.383| 165,429|
| |Johnson County|   106| 175.963|  0.949| 6,228| 10338.628| 167.425| 602,401|
| |Sedgwick County|    47| 91.078|  0.830| 5,213| 10101.891| 137.586| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,712|  9679.152| 163.958| 176,875|
| |Lyon County|    14| 421.750|  4.304|   734| 22111.764| 159.232|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,801| 49387.117| 70.514|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,106| 62643.148| 157.224|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,519| 18579.222| 104.839|  81,758|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982|  0.000|   5,234|
| |Coffey County|     8| 978.115|  0.000|    68|  8313.975| 17.466|   8,179|
| |Saline County|     7| 129.094|  5.269|   399|  7358.365| 71.133|  54,224|
| |Douglas County|     5| 40.897|  0.000|   812|  6641.638| 114.511| 122,259|
| |Riley County|     5| 67.356|  0.000|   495|  6668.283| 34.640|  74,232|
| |Montgomery County|     5| 157.089|  0.000|   183|  5749.474| 85.277|  31,829|
| |Seward County|     4| 186.672|  0.000| 1,257| 58661.564| 246.673|  21,428|
| |Barton County|     3| 116.374|  0.000|   165|  6400.559| 177.331|  25,779|
| |Sumner County|     3| 131.372|  0.000|   104|  4554.213| 31.279|  22,836|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Grant County|     2| 279.720|  0.000|   120| 16783.217| 279.720|   7,150|
| |Geary County|     2| 63.151|  0.000|   165|  5209.978| 135.324|  31,670|
| |Cowley County|     2| 57.293|  0.000|   182|  5213.705| 69.571|  34,908|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375|  0.000|   8,002|
| |Butler County|     2| 29.890|  2.135|   306|  4573.239| 108.887|  66,911|
| |Bourbon County|     2| 137.608|  0.000|    79|  5435.530| 58.975|  14,534|
| |Trego County|     1| 356.761|  0.000|     7|  2497.324| 50.966|   2,803|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090| 142.430|   2,006|
| |Stafford County|     1| 240.616|  0.000|     7|  1684.312| 137.495|   4,156|
| |Cherokee County|     1| 50.153|  0.000|   152|  7623.251| 365.400|  19,939|
| |Labette County|     1| 50.974|  7.282|   153|  7798.960| 145.639|  19,618|
| |Kearny County|     1| 260.552|  0.000|    66| 17196.456| 260.552|   3,838|
| |Jewell County|     1| 347.343| 49.620|    13|  4515.457| 99.241|   2,879|
| |Harvey County|     1| 29.045|  0.000|   216|  6273.781| 91.285|  34,429|
| |Franklin County|     1| 39.148|  0.000|   224|  8769.183| 257.259|  25,544|
| |Ellis County|     1| 35.023|  0.000|   150|  5253.388| 45.029|  28,553|
| |Dickinson County|     1| 54.154|  0.000|    50|  2707.679| 23.209|  18,466|
| |Crawford County|     1| 25.761|  0.000|   395| 10175.692| 55.203|  38,818|
| |McPherson County|     1| 35.036|  0.000|   151|  5290.449| 45.046|  28,542|
| |Jackson County|     1| 75.924|  0.000|   163| 12375.674| 184.388|  13,171|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044|  0.000|  11,884|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199|  0.000|   1,994|
| |Reno County|     1| 16.130|  0.000|   408|  6580.857| 324.895|  61,998|
| |Nemaha County|     1| 97.742|  0.000|    50|  4887.108| 13.963|  10,231|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Scott County|     0|  0.000|  0.000|    69| 14306.448| 1036.699|   4,823|
| |Russell County|     0|  0.000|  0.000|    16|  2333.722| 62.510|   6,856|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 29.036|   4,920|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 29.959|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   111|  4552.352| 23.436|  24,383|
| |Pawnee County|     0|  0.000|  0.000|    60|  9354.537| 1180.453|   6,414|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323|  0.000|   8,525|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Sherman County|     0|  0.000|  0.000|    17|  2873.078| 48.287|   5,917|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509|  0.000|   5,485|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 20.611|   6,931|
| |Thomas County|     0|  0.000|  0.000|    45|  5786.293| 165.323|   7,777|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946| 57.748|  12,369|
| |Linn County|     0|  0.000|  0.000|    46|  4740.802| 161.953|   9,703|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 71.644|   5,982|
| |Hamilton County|     0|  0.000|  0.000|    39| 15360.378| 112.530|   2,539|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818|  0.000|   2,750|
| |Neosho County|     0|  0.000|  0.000|    66|  4123.196| 71.397|  16,007|
| |Morris County|     0|  0.000|  0.000|    12|  2135.231| 25.419|   5,620|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Miami County|     0|  0.000|  0.000|   150|  4381.225| 70.934|  34,237|
| |Meade County|     0|  0.000|  0.000|    52| 12893.628| 283.376|   4,033|
| |Marshall County|     0|  0.000|  0.000|    15|  1545.277| 88.302|   9,707|
| |Harper County|     0|  0.000|  0.000|    16|  2943.341| 157.679|   5,436|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024| 36.360|   7,858|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     6|  3908.795| 93.067|   1,535|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    24|  3355.705| 139.821|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    88|  4621.121| 90.022|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753|  0.000|   1,232|
| |Atchison County|     0|  0.000|  0.000|    99|  6159.398| 311.081|  16,073|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Ottawa County|     0|  0.000|  0.000|    37|  6486.676| 75.135|   5,704|
| |Osage County|     0|  0.000|  0.000|    46|  2884.193| 53.743|  15,949|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Gray County|     0|  0.000|  0.000|    87| 14529.058| 238.572|   5,988|
| |Graham County|     0|  0.000|  0.000|    17|  6849.315| 57.557|   2,482|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495|  0.000|   6,102|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Edwards County|     0|  0.000|  0.000|    12|  4288.778| 102.114|   2,798|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789|  0.000|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Comanche County|     0|  0.000|  0.000|     9|  5294.118| 336.134|   1,700|
| |Cloud County|     0|  0.000|  0.000|    41|  4666.515| 146.337|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     5|  1881.822| 107.533|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Chase County|     0|  0.000|  0.000|    48| 18126.888| 323.694|   2,648|
| |Brown County|     0|  0.000|  0.000|    53|  5541.614| 238.991|   9,564|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   385| 91.281| N/A|22,613|  5361.406| N/A|4,217,737|
| |Multnomah County|   101| 124.253|  1.406| 5,186|  6379.982| 74.517| 812,855|
| |Marion County|    73| 209.880|  1.643| 3,090|  8883.957| 103.913| 347,818|
| |Clackamas County|    49| 117.172|  3.416| 1,627|  3890.604| 43.385| 418,187|
| |Umatilla County|    32| 410.520|  9.163| 2,398| 30763.310| 324.384|  77,950|
| |Washington County|    27| 44.881|  0.712| 3,258|  5415.631| 63.403| 601,592|
| |Malheur County|    15| 490.661|  9.346|   869| 28425.632| 532.718|  30,571|
| |Yamhill County|    13| 121.382|  0.000|   502|  4687.208| 97.372| 107,100|
| |Polk County|    12| 139.397|  0.000|   350|  4065.749| 69.699|  86,085|
| |Deschutes County|    11| 55.642|  1.445|   627|  3171.600| 32.518| 197,692|
| |Linn County|    11| 84.779|  1.101|   315|  2427.764| 48.445| 129,749|
| |Lincoln County|     9| 180.137|  0.000|   431|  8626.556| 54.327|  49,962|
| |Benton County|     6| 64.479|  0.000|   182|  1955.875| 27.634|  93,053|
| |Lane County|     4| 10.469|  0.374|   615|  1609.665| 18.695| 382,067|
| |Jefferson County|     4| 162.219|  0.000|   396| 16059.697| 289.677|  24,658|
| |Morrow County|     3| 258.554|  0.000|   393| 33870.551| 541.732|  11,603|
| |Wasco County|     3| 112.435|  0.000|   199|  7458.212| 96.373|  26,682|
| |Klamath County|     2| 29.309|  0.000|   206|  3018.846| 10.468|  68,238|
| |Josephine County|     2| 22.861|  0.000|   136|  1554.517| 37.557|  87,487|
| |Jackson County|     2|  9.052|  0.000|   536|  2425.954| 57.545| 220,944|
| |Union County|     2| 74.530|  0.000|   397| 14794.112| 15.971|  26,835|
| |Wallowa County|     1| 138.735|  0.000|    20|  2774.695| 19.819|   7,208|
| |Douglas County|     1|  9.011|  0.000|   159|  1432.691| 14.160| 110,980|
| |Crook County|     1| 40.977|  0.000|    51|  2089.821| 46.831|  24,404|
| |Columbia County|     1| 19.101|  2.729|   103|  1967.376| 32.744|  52,354|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Curry County|     0|  0.000|  0.000|    17|   741.549| 18.695|  22,925|
| |Tillamook County|     0|  0.000|  0.000|    35|  1294.570|  5.284|  27,036|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 80.257|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Hood River County|     0|  0.000|  0.000|   215|  9195.107| 207.730|  23,382|
| |Harney County|     0|  0.000|  0.000|    11|  1487.894| 19.323|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633|  0.000|   7,199|
| |Coos County|     0|  0.000|  0.000|    93|  1442.151|  6.646|  64,487|
| |Clatsop County|     0|  0.000|  0.000|    88|  2187.749| 14.206|  40,224|
| |Baker County|     0|  0.000|  0.000|    52|  3225.006| 124.039|  16,124|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   361| 186.620| N/A|29,827| 15419.188| N/A|1,934,408|
| |Douglas County|   143| 250.294|  2.750|11,929| 20879.461| 197.535| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,766| 28784.249| 65.196|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,934| 96574.453| 85.603|  20,026|
| |Lancaster County|    19| 59.544|  0.895| 3,407| 10677.238| 68.946| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   102| 10939.511| 45.964|   9,324|
| |Sarpy County|    11| 58.762|  0.000| 2,441| 13039.809| 168.654| 187,196|
| |Adams County|    11| 350.732|  0.000|   364| 11606.033| 50.105|  31,363|
| |Dodge County|    10| 273.486|  3.907|   832| 22754.000| 160.184|  36,565|
| |Dawson County|     9| 381.437|  0.000|   970| 41110.405| 84.764|  23,595|
| |Perkins County|     7| 2421.308|  0.000|    21|  7263.923| 98.829|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   311|  8731.540| 52.141|  35,618|
| |Howard County|     5| 775.795| 22.166|    55|  8533.747|  0.000|   6,445|
| |Madison County|     5| 142.454|  0.000|   482| 13732.585| 150.594|  35,099|
| |Colfax County|     4| 373.518|  0.000|   707| 66019.236| 93.379|  10,709|
| |Custer County|     4| 371.161|  0.000|    57|  5289.041| 172.325|  10,777|
| |Gage County|     4| 185.934|  0.000|    95|  4415.935| 39.843|  21,513|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 118.652|   7,224|
| |Platte County|     3| 89.633|  0.000|   812| 24260.532| 119.510|  33,470|
| |Saline County|     2| 140.607|  0.000|   600| 42182.227| 50.217|  14,224|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Saunders County|     2| 92.687|  0.000|   173|  8017.425| 132.410|  21,578|
| |Cass County|     2| 76.196|  0.000|   209|  7962.511| 201.376|  26,248|
| |Lincoln County|     2| 57.284|  0.000|   172|  4926.391| 298.693|  34,914|
| |Antelope County|     1| 158.781|  0.000|    20|  3175.611| 22.683|   6,298|
| |Buffalo County|     1| 20.137|  0.000|   481|  9686.059| 230.141|  49,659|
| |Richardson County|     1| 127.146|  0.000|    27|  3432.931| 108.982|   7,865|
| |Fillmore County|     1| 183.083|  0.000|    29|  5309.410| 130.774|   5,462|
| |Seward County|     1| 57.857|  0.000|   130|  7521.407| 115.714|  17,284|
| |Washington County|     1| 48.242|  0.000|   138|  6657.340| 144.725|  20,729|
| |Furnas County|     1| 213.858|  0.000|    16|  3421.728| 30.551|   4,676|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Otoe County|     0|  0.000|  0.000|    63|  3934.549| 160.594|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     6|  1446.480| 34.440|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    50|  7171.543| 450.783|   6,972|
| |Nance County|     0|  0.000|  0.000|    10|  2841.716| 81.192|   3,519|
| |Morrill County|     0|  0.000|  0.000|    63| 13571.736| 153.875|   4,642|
| |Merrick County|     0|  0.000|  0.000|    62|  7994.842| 18.421|   7,755|
| |McPherson County|     0|  0.000|  0.000|     6| 12145.749| 289.184|     494|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    41|  4920.787| 120.019|   8,332|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Phelps County|     0|  0.000|  0.000|    43|  4759.796| 94.880|   9,034|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759|  0.000|   1,357|
| |Sheridan County|     0|  0.000|  0.000|    12|  2287.457| 54.463|   5,246|
| |Sherman County|     0|  0.000|  0.000|    14|  4665.112| 142.810|   3,001|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |Pierce County|     0|  0.000|  0.000|    37|  5176.273| 339.755|   7,148|
| |Polk County|     0|  0.000|  0.000|    28|  5371.187| 54.808|   5,213|
| |Red Willow County|     0|  0.000|  0.000|    18|  1678.478| 13.321|  10,724|
| |York County|     0|  0.000|  0.000|    90|  6579.428| 125.322|  13,679|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482|  0.000|   2,356|
| |Chase County|     0|  0.000|  0.000|     7|  1783.894| 36.406|   3,924|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Jefferson County|     0|  0.000|  0.000|    19|  2696.565| 81.100|   7,046|
| |Gosper County|     0|  0.000|  0.000|    20| 10050.251| 71.788|   1,990|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Holt County|     0|  0.000|  0.000|    14|  1390.682| 14.191|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Harlan County|     0|  0.000|  0.000|     2|   591.716| 42.265|   3,380|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139| 182.448|     783|
| |Garfield County|     0|  0.000|  0.000|     4|  2031.488| 72.553|   1,969|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616|  0.000|   6,203|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Franklin County|     0|  0.000|  0.000|    15|  5035.247| 143.864|   2,979|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827|  0.000|   1,794|
| |Dawes County|     0|  0.000|  0.000|    14|  1629.992| 66.530|   8,589|
| |Cuming County|     0|  0.000|  0.000|    72|  8139.272| 80.747|   8,846|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Wayne County|     0|  0.000|  0.000|    40|  4262.120| 45.666|   9,385|
| |Valley County|     0|  0.000|  0.000|    12|  2886.003| 68.714|   4,158|
| |Thomas County|     0|  0.000|  0.000|     2|  2770.083| 197.863|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 28.554|   5,003|
| |Stanton County|     0|  0.000|  0.000|    32|  5405.405| 72.394|   5,920|
| |Keith County|     0|  0.000|  0.000|    33|  4107.543| 231.160|   8,034|
| |Kearney County|     0|  0.000|  0.000|    81| 12471.132| 681.843|   6,495|
| |Johnson County|     0|  0.000|  0.000|    14|  2760.797| 28.171|   5,071|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Cedar County|     0|  0.000|  0.000|    26|  3094.501| 68.011|   8,402|
| |Butler County|     0|  0.000|  0.000|    66|  8233.533| 106.929|   8,016|
| |Burt County|     0|  0.000|  0.000|    48|  7431.491| 375.998|   6,459|
| |Brown County|     0|  0.000|  0.000|     2|   676.819| 96.688|   2,955|
| |Boyd County|     0|  0.000|  0.000|     8|  4168.838| 297.774|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    16|  1483.817| 66.242|  10,783|
| |Boone County|     0|  0.000|  0.000|    11|  2118.644| 82.545|   5,192|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827|  0.000|     463|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   299| 93.264| N/A|36,608| 11418.740| N/A|3,205,958|
| |Salt Lake County|   209| 180.105|  2.462|21,462| 18494.757| 144.650|1,160,437|
| |Utah County|    38| 59.726|  0.225| 9,216| 14485.214| 152.684| 636,235|
| |San Juan County|    26| 1698.458|  9.332|   655| 42788.085| 65.325|  15,308|
| |Davis County|    21| 59.075|  0.000| 3,360|  9451.982| 81.981| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   588| 17247.954| 150.857|  34,091|
| |Summit County|     1| 23.728|  0.000|   724| 17178.788| 61.014|  42,145|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Tooele County|     0|  0.000|  0.000|   603|  8344.981| 47.448|  72,259|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   265| 148.288| N/A|27,166| 15201.462| N/A|1,787,065|
| |Ada County|    93| 193.112|  5.043| 9,753| 20251.793| 306.427| 481,587|
| |Canyon County|    56| 243.638|  4.972| 6,257| 27222.220| 395.912| 229,849|
| |Twin Falls County|    33| 379.843|  1.644| 1,506| 17334.653| 317.358|  86,878|
| |Kootenai County|    20| 120.702|  4.311| 1,972| 11901.241| 179.329| 165,697|
| |Nez Perce County|    19| 470.204|  0.000|   174|  4306.078| 102.526|  40,408|
| |Jerome County|     6| 245.781|  0.000|   517| 21178.109| 327.708|  24,412|
| |Blaine County|     6| 260.632|  0.000|   584| 25368.142| 55.850|  23,021|
| |Bonneville County|     4| 33.596|  1.200| 1,266| 10633.116| 369.555| 119,062|
| |Elmore County|     3| 109.047|  0.000|   230|  8360.292| 119.433|  27,511|
| |Payette County|     3| 125.256|  5.965|   441| 18412.592| 381.732|  23,951|
| |Owyhee County|     3| 253.743| 12.083|   276| 23344.329| 217.494|  11,823|
| |Washington County|     3| 294.291|  0.000|   229| 22464.195| 392.388|  10,194|
| |Shoshone County|     3| 232.883| 11.090|   163| 12653.315| 842.815|  12,882|
| |Bannock County|     2| 22.777|  0.000|   488|  5557.580| 162.693|  87,808|
| |Minidoka County|     2| 95.062|  0.000|   503| 23907.980| 230.864|  21,039|
| |Bingham County|     2| 42.725|  0.000|   338|  7220.525| 311.282|  46,811|
| |Benewah County|     1| 107.550| 15.364|    80|  8604.001| 261.193|   9,298|
| |Cassia County|     1| 41.615|  0.000|   544| 22638.369| 184.293|  24,030|
| |Boise County|     1| 127.698|  0.000|    52|  6640.276| 91.213|   7,831|
| |Gem County|     1| 55.212|  0.000|   188| 10379.859| 110.424|  18,112|
| |Gooding County|     1| 65.880|  0.000|   179| 11792.608| 207.053|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   239|  8001.071| 258.253|  29,871|
| |Valley County|     1| 87.781|  0.000|    71|  6232.444| 188.102|  11,392|
| |Fremont County|     0|  0.000|  0.000|    92|  7023.437| 163.589|  13,099|
| |Oneida County|     0|  0.000|  0.000|    16|  3531.229| 94.586|   4,531|
| |Adams County|     0|  0.000|  0.000|    22|  5123.428| 99.807|   4,294|
| |Bear Lake County|     0|  0.000|  0.000|    21|  3428.571| 139.942|   6,125|
| |Bonner County|     0|  0.000|  0.000|   191|  4175.867| 40.603|  45,739|
| |Madison County|     0|  0.000|  0.000|   180|  4510.487| 85.914|  39,907|
| |Lincoln County|     0|  0.000|  0.000|    61| 11367.872| 133.113|   5,366|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Lemhi County|     0|  0.000|  0.000|    41|  5107.761| 444.927|   8,027|
| |Latah County|     0|  0.000|  0.000|   133|  3316.047| 121.102|  40,108|
| |Idaho County|     0|  0.000|  0.000|    34|  2039.959| 25.714|  16,667|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 10.295|  13,876|
| |Teton County|     0|  0.000|  0.000|    95|  7824.082| 211.780|  12,142|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 33.107|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|    10| 11834.320| 338.123|     845|
| |Caribou County|     0|  0.000|  0.000|    34|  4751.922| 59.898|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     1|   385.060| 55.009|   2,597|
| |Boundary County|     0|  0.000|  0.000|    38|  3103.307| 23.333|  12,245|
| |Power County|     0|  0.000|  0.000|    66|  8592.631| 204.586|   7,681|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   157| 87.604| N/A| 8,277|  4618.483| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  1.604| 1,046|  5872.314| 118.697| 178,124|
| |Jackson County|    19| 664.894|  0.000|   166|  5809.071| 19.997|  28,576|
| |Mercer County|    17| 289.322| 34.038|   219|  3727.152| 102.114|  58,758|
| |Berkeley County|    11| 92.304|  0.000|   727|  6100.477| 49.149| 119,171|
| |Logan County|    10| 312.315| 31.231|   285|  8900.965| 339.084|  32,019|
| |Wayne County|     9| 228.415|  0.000|   214|  5431.196| 50.759|  39,402|
| |Fayette County|     7| 165.071|  6.738|   166|  3914.540| 87.589|  42,406|
| |Monongalia County|     5| 47.343|  0.000|   973|  9212.968| 51.401| 105,612|
| |Wood County|     5| 59.867|  0.000|   269|  3220.863| 44.473|  83,518|
| |Mingo County|     5| 213.456|  0.000|   198|  8452.869| 243.950|  23,424|
| |Preston County|     4| 119.646|  0.000|   127|  3798.756| 17.092|  33,432|
| |Ohio County|     4| 96.593|  0.000|   275|  6640.748| 31.048|  41,411|
| |Mineral County|     4| 148.876|  0.000|   127|  4726.813| 53.170|  26,868|
| |Jefferson County|     4| 69.996|  0.000|   303|  5302.208| 22.499|  57,146|
| |Grant County|     4| 345.781| 37.048|   131| 11324.343| 172.891|  11,568|
| |Greenbrier County|     3| 86.550|  0.000|    94|  2711.904| 12.364|  34,662|
| |Cabell County|     3| 32.628|  1.554|   436|  4741.965| 97.885|  91,945|
| |Wyoming County|     2| 98.068|  7.005|    46|  2255.565| 105.073|  20,394|
| |Lewis County|     2| 125.731|  0.000|    28|  1760.231|  0.000|  15,907|
| |Marion County|     2| 35.668|  0.000|   198|  3531.174| 38.216|  56,072|
| |Taylor County|     1| 59.898|  0.000|    61|  3653.789| 42.784|  16,695|
| |Roane County|     1| 73.057|  0.000|    19|  1388.077| 41.747|  13,688|
| |Pleasants County|     1| 134.048|  0.000|    14|  1876.676| 38.300|   7,460|
| |Raleigh County|     1| 13.631|  0.000|   282|  3844.004| 130.470|  73,361|
| |Barbour County|     1| 60.824|  0.000|    31|  1885.530| 17.378|  16,441|
| |Pendleton County|     1| 143.493|  0.000|    42|  6026.690|  0.000|   6,969|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  0.000|  30,531|
| |Mason County|     1| 37.713|  0.000|    70|  2639.916| 86.201|  26,516|
| |Nicholas County|     1| 40.823|  0.000|    40|  1632.920| 23.327|  24,496|
| |Harrison County|     1| 14.869|  0.000|   240|  3568.455| 55.226|  67,256|
| |Hampshire County|     1| 43.150|  0.000|    86|  3710.895| 61.643|  23,175|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Brooke County|     1| 45.581|  0.000|    72|  3281.827| 65.116|  21,939|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  5.909|  24,176|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Morgan County|     0|  0.000|  0.000|    32|  1789.309| 47.928|  17,884|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921|  0.000|  13,275|
| |Putnam County|     0|  0.000|  0.000|   207|  3666.962| 53.144|  56,450|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 16.910|   8,448|
| |McDowell County|     0|  0.000|  0.000|    65|  3688.153| 56.741|  17,624|
| |Boone County|     0|  0.000|  0.000|   114|  5312.951| 113.183|  21,457|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 33.257|   8,591|
| |Webster County|     0|  0.000|  0.000|     4|   492.975|  0.000|   8,114|
| |Wetzel County|     0|  0.000|  0.000|    44|  2920.677| 18.965|  15,065|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Gilmer County|     0|  0.000|  0.000|    18|  2300.908| 36.522|   7,823|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 14.876|  28,810|
| |Lincoln County|     0|  0.000|  0.000|    97|  4752.805| 111.995|  20,409|
| |Tucker County|     0|  0.000|  0.000|    11|  1608.422|  0.000|   6,839|
| |Randolph County|     0|  0.000|  0.000|   213|  7422.896| 24.892|  28,695|
| |Hardy County|     0|  0.000|  0.000|    62|  4500.581| 41.480|  13,776|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Summers County|     0|  0.000|  0.000|    17|  1352.104| 113.622|  12,573|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   150| 169.557| N/A|10,024| 11330.920| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  0.740| 4,561| 23615.728| 156.812| 193,134|
| |Pennington County|    33| 290.046|  2.511|   924|  8121.292| 61.525| 113,775|
| |Beadle County|     9| 487.726|  0.000|   596| 32298.271| 69.675|  18,453|
| |Todd County|     5| 491.304|  0.000|    75|  7369.559| 98.261|  10,177|
| |Union County|     4| 251.067|  0.000|   221| 13871.454| 107.600|  15,932|
| |Lyman County|     3| 793.441| 37.783|    91| 24067.707| 113.349|   3,781|
| |Lake County|     3| 234.430| 11.163|   100|  7814.331| 111.633|  12,797|
| |Brown County|     3| 77.242|  0.000|   463| 11921.007| 128.737|  38,839|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556|  0.000|   1,962|
| |Hughes County|     3| 171.174|  8.151|    97|  5534.634| 73.360|  17,526|
| |Yankton County|     2| 87.665|  0.000|   136|  5961.252| 162.807|  22,814|
| |Lincoln County|     2| 32.718|  0.000|   687| 11238.712| 182.287|  61,128|
| |Oglala Lakota County|     2| 141.074|  0.000|   157| 11074.275| 40.307|  14,177|
| |Faulk County|     1| 434.972|  0.000|    29| 12614.180| 186.416|   2,299|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474|  0.000|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |McCook County|     1| 179.019|  0.000|    32|  5728.607| 153.445|   5,586|
| |Meade County|     1| 35.296|  0.000|    97|  3423.691| 50.423|  28,332|
| |Davison County|     1| 50.569|  0.000|    99|  5006.321| 36.121|  19,775|
| |Codington County|     1| 35.703|  0.000|   151|  5391.124| 112.209|  28,009|
| |Butte County|     1| 95.886|  0.000|    18|  1725.956| 54.792|  10,429|
| |Brookings County|     1| 28.509|  0.000|   145|  4133.763| 69.235|  35,077|
| |Roberts County|     1| 96.209|  0.000|    83|  7985.376| 109.954|  10,394|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Grant County|     0|  0.000|  0.000|    31|  4395.916| 141.804|   7,052|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223|  0.000|   6,713|
| |Edmunds County|     0|  0.000|  0.000|    19|  4962.131| 186.546|   3,829|
| |Douglas County|     0|  0.000|  0.000|    19|  6504.622| 97.814|   2,921|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Moody County|     0|  0.000|  0.000|    33|  5018.248| 21.724|   6,576|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 103.670|   2,756|
| |Hand County|     0|  0.000|  0.000|    10|  3133.814| 134.306|   3,191|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Turner County|     0|  0.000|  0.000|    56|  6679.389| 102.236|   8,384|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Sully County|     0|  0.000|  0.000|     4|  2875.629| 205.402|   1,391|
| |Hamlin County|     0|  0.000|  0.000|    27|  4380.273| 231.760|   6,164|
| |Hanson County|     0|  0.000|  0.000|    22|  6371.271| 41.372|   3,453|
| |Harding County|     0|  0.000|  0.000|     2|  1540.832| 220.119|   1,298|
| |Marshall County|     0|  0.000|  0.000|    12|  2431.611| 115.791|   4,935|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757|  0.000|   2,379|
| |Lawrence County|     0|  0.000|  0.000|    63|  2437.703| 93.970|  25,844|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582|  0.000|   4,939|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     4|  3074.558| 109.806|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    29|  3977.507| 39.187|   7,291|
| |Spink County|     0|  0.000|  0.000|    26|  4077.792| 44.811|   6,376|
| |Stanley County|     0|  0.000|  0.000|    15|  4841.833| 46.113|   3,098|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Potter County|     0|  0.000|  0.000|     2|   928.936| 66.353|   2,153|
| |Clark County|     0|  0.000|  0.000|    17|  4550.321| 38.238|   3,736|
| |Charles Mix County|     0|  0.000|  0.000|   109| 11730.521| 122.994|   9,292|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233|  0.000|   1,376|
| |Brule County|     0|  0.000|  0.000|    46|  8684.161| 26.969|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    15|  2173.598| 41.402|   6,901|
| |Aurora County|     0|  0.000|  0.000|    39| 14176.663| 51.929|   2,751|
| |Corson County|     0|  0.000|  0.000|    41| 10034.263| 314.663|   4,086|
| |Clay County|     0|  0.000|  0.000|   136|  9665.956| 121.840|  14,070|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Dewey County|     0|  0.000|  0.000|    57|  9674.134| 169.722|   5,892|
| |Deuel County|     0|  0.000|  0.000|    13|  2987.819| 98.500|   4,351|
| |Day County|     0|  0.000|  0.000|    24|  4424.779| 79.014|   5,424|
| |Custer County|     0|  0.000|  0.000|    37|  4123.941| 127.380|   8,972|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   126| 93.735| N/A| 4,115|  3061.273| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,113|  7162.639| 18.402| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    13| 62.608|  0.688|   681|  3279.699|  8.944| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   171|  1398.178|  1.168| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   575|  5310.454| 22.429| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   162|  1064.753|  9.389| 152,148|
| |Somerset County|     1| 19.808|  0.000|    35|   693.289|  5.660|  50,484|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  0.000|  39,772|
| |Hancock County|     1| 18.186|  0.000|    40|   727.445| 12.990|  54,987|
| |Franklin County|     1| 33.114|  0.000|    47|  1556.343|  9.461|  30,199|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  0.000|  67,055|
| |Oxford County|     0|  0.000|  0.000|    56|   965.934|  7.392|  57,975|
| |Washington County|     0|  0.000|  0.000|    14|   446.158|  9.105|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    58|  1617.581| 15.937|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|     6|   357.462| 25.533|  16,785|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   121| 158.780| N/A| 8,300| 10891.502| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,104| 17062.164| 76.956| 181,923|
| |Grand Forks County|     8| 115.189|  4.114|   737| 10611.798| 154.271|  69,451|
| |Burleigh County|     8| 83.659|  4.482| 1,325| 13856.064| 324.180|  95,626|
| |Stark County|     5| 158.786|  9.073|   373| 11845.406| 567.091|  31,489|
| |Morton County|     4| 127.535|  4.555|   435| 13869.404| 464.591|  31,364|
| |Stutsman County|     3| 144.900|  6.900|   129|  6230.680| 20.700|  20,704|
| |McIntosh County|     2| 800.961|  0.000|    41| 16419.704| 800.961|   2,497|
| |McKenzie County|     2| 133.120|  9.509|    92|  6123.536| 57.052|  15,024|
| |Benson County|     2| 292.740|  0.000|   163| 23858.314| 648.210|   6,832|
| |Williams County|     2| 53.207|  0.000|   299|  7954.455| 136.818|  37,589|
| |Ramsey County|     2| 173.626|  0.000|    83|  7205.487| 210.832|  11,519|
| |Ward County|     1| 14.784|  0.000|   254|  3755.119| 95.040|  67,641|
| |Richland County|     1| 61.816|  8.831|   115|  7108.858| 97.140|  16,177|
| |Sioux County|     1| 236.407|  0.000|    93| 21985.816| 1013.171|   4,230|
| |Mountrail County|     1| 94.832|  0.000|   149| 14129.919| 352.232|  10,545|
| |McHenry County|     1| 174.064|  0.000|    21|  3655.352| 124.332|   5,745|
| |Griggs County|     1| 448.229|  0.000|    37| 16584.491| 320.164|   2,231|
| |Emmons County|     1| 308.547|  0.000|    19|  5862.388| 88.156|   3,241|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Hettinger County|     0|  0.000|  0.000|     7|  2801.120| 57.166|   2,499|
| |Kidder County|     0|  0.000|  0.000|    19|  7661.290| 345.622|   2,480|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784|  0.000|   1,850|
| |McLean County|     0|  0.000|  0.000|    90|  9523.810| 589.569|   9,450|
| |Foster County|     0|  0.000|  0.000|    27|  8411.215|  0.000|   3,210|
| |Golden Valley County|     0|  0.000|  0.000|    10|  5678.592| 486.736|   1,761|
| |Eddy County|     0|  0.000|  0.000|    18|  7870.573| 187.395|   2,287|
| |Nelson County|     0|  0.000|  0.000|    26|  9030.914| 99.241|   2,879|
| |Dunn County|     0|  0.000|  0.000|    31|  7007.233| 32.291|   4,424|
| |Divide County|     0|  0.000|  0.000|     4|  1766.784| 126.199|   2,264|
| |Dickey County|     0|  0.000|  0.000|    14|  2873.563| 58.644|   4,872|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Bowman County|     0|  0.000|  0.000|    11|  3637.566| 236.206|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000|  0.000|     3|  3232.759| 153.941|     928|
| |Barnes County|     0|  0.000|  0.000|    39|  3744.599| 27.433|  10,415|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |Mercer County|     0|  0.000|  0.000|    34|  4152.925| 139.594|   8,187|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Wells County|     0|  0.000|  0.000|    25|  6520.605| 149.042|   3,834|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523|  0.000|   4,046|
| |Walsh County|     0|  0.000|  0.000|   112| 10525.327| 120.826|  10,641|
| |Traill County|     0|  0.000|  0.000|    60|  7466.401| 142.217|   8,036|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Steele County|     0|  0.000|  0.000|    16|  8465.608| 151.172|   1,890|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 108.637|   1,315|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    86|  6066.591| 342.631|  14,176|
| |Renville County|     0|  0.000|  0.000|    10|  4297.379| 61.391|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 27.378|   5,218|
| |Pierce County|     0|  0.000|  0.000|    15|  3773.585| 143.756|   3,975|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    81| 75.787| N/A| 5,541|  5184.426| N/A|1,068,778|
| |Yellowstone County|    32| 198.388|  3.543| 1,463|  9070.056| 222.301| 161,300|
| |Big Horn County|    14| 1051.130| 10.726|   492| 36939.710| 911.694|  13,319|
| |Toole County|     6| 1266.892|  0.000|    44|  9290.541| 60.328|   4,736|
| |Cascade County|     4| 49.161|  1.756|   179|  2199.936| 29.847|  81,366|
| |Flathead County|     3| 28.900|  1.376|   376|  3622.141| 74.314| 103,806|
| |Gallatin County|     3| 26.216|  0.000|   977|  8537.672| 77.400| 114,434|
| |Hill County|     2| 121.330|  0.000|    48|  2911.915| 51.998|  16,484|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939|  0.000|  11,402|
| |Ravalli County|     2| 45.656|  3.261|    85|  1940.373|  9.783|  43,806|
| |Lewis and Clark County|     2| 28.805|  2.058|   171|  2462.841| 39.093|  69,432|
| |Richland County|     2| 185.134|  0.000|    48|  4443.210| 13.224|  10,803|
| |Lincoln County|     2| 100.100|  0.000|    78|  3903.904| 28.600|  19,980|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972|  0.000|   3,737|
| |Rosebud County|     1| 111.894|  0.000|    65|  7273.134| 527.502|   8,937|
| |Missoula County|     1|  8.361|  1.194|   357|  2984.950| 46.584| 119,600|
| |Stillwater County|     1| 103.713| 14.816|    29|  3007.675| 88.897|   9,642|
| |Lake County|     1| 32.832|  0.000|   184|  6041.106| 23.451|  30,458|
| |Glacier County|     1| 72.711|  0.000|    87|  6325.893| 186.972|  13,753|
| |Madison County|     1| 116.279|  0.000|    84|  9767.442| 33.223|   8,600|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Sanders County|     0|  0.000|  0.000|    11|   908.115| 23.587|  12,113|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031|  0.000|   3,309|
| |Silver Bow County|     0|  0.000|  0.000|   104|  2978.662| 77.740|  34,915|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    30|  4056.247| 289.732|   7,396|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Roosevelt County|     0|  0.000|  0.000|    29|  2635.405| 103.858|  11,004|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 50.704|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Carbon County|     0|  0.000|  0.000|    75|  6993.007| 106.560|  10,725|
| |Broadwater County|     0|  0.000|  0.000|    14|  2244.669| 68.714|   6,237|
| |Blaine County|     0|  0.000|  0.000|    14|  2095.495| 85.530|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    68|  7193.484| 105.787|   9,453|
| |Jefferson County|     0|  0.000|  0.000|    30|  2454.791| 35.068|  12,221|
| |Granite County|     0|  0.000|  0.000|    18|  5327.020| 211.390|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 171.703|   1,664|
| |Fergus County|     0|  0.000|  0.000|    19|  1719.457| 129.282|  11,050|
| |Dawson County|     0|  0.000|  0.000|    29|  3367.003| 199.035|   8,613|
| |Deer Lodge County|     0|  0.000|  0.000|    28|  3063.457| 46.890|   9,140|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937|  0.000|   5,911|
| |Phillips County|     0|  0.000|  0.000|    85| 21497.218| 2312.306|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    62|  3733.590| 60.219|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     4|   863.371| 30.835|   4,633|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,493|  2392.670| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   749|  4573.376| 21.807| 163,774|
| |Franklin County|     7| 141.695|  0.000|   120|  2429.051|  5.783|  49,402|
| |Windham County|     3| 71.053|  0.000|   105|  2486.855| 10.150|  42,222|
| |Addison County|     2| 54.382|  0.000|    74|  2012.127|  3.884|  36,777|
| |Windsor County|     2| 36.323|  0.000|    74|  1343.940|  5.189|  55,062|
| |Washington County|     2| 34.241|  0.000|    57|   975.877|  9.783|  58,409|
| |Rutland County|     1| 17.185|  0.000|   101|  1735.664|  4.910|  58,191|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  0.000|  25,362|
| |Bennington County|     1| 28.193|  0.000|    92|  2593.741| 28.193|  35,470|
| |Orleans County|     0|  0.000|  0.000|    15|   554.795|  5.284|  27,037|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|
| |Orange County|     0|  0.000|  0.000|    16|   553.787|  9.889|  28,892|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    39| 27.545| N/A| 4,520|  3192.379| N/A|1,415,872|
| |Honolulu County|    33| 33.861| N/A| 4,117|  4224.458| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   206|  1230.460| 21.333| 167,417|
| |Kauai County|     0|  0.000|  0.000|    53|   733.128| 11.857|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   144|   714.594| 14.887| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,183|  5499.698| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    25|  2960.332| 33.832|   8,445|
| |Natrona County|     0|  0.000|  0.000|   245|  3067.946| 28.622|  79,858|
| |Lincoln County|     0|  0.000|  0.000|   101|  5093.293|  7.204|  19,830|
| |Laramie County|     0|  0.000|  0.000|   512|  5145.729| 22.972|  99,500|
| |Washakie County|     0|  0.000|  0.000|    96| 12299.808| 494.189|   7,805|
| |Uinta County|     0|  0.000|  0.000|   277| 13695.244| 21.189|  20,226|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Park County|     0|  0.000|  0.000|   144|  4932.520| 58.720|  29,194|
| |Platte County|     0|  0.000|  0.000|     6|   714.881| 17.021|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    78|  2558.635| 42.175|  30,485|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762| 29.063|   9,831|
| |Sweetwater County|     0|  0.000|  0.000|   271|  6400.113| 47.233|  42,343|
| |Teton County|     0|  0.000|  0.000|   383| 16322.878| 73.060|  23,464|
| |Albany County|     0|  0.000|  0.000|    92|  2366.255| 14.697|  38,880|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Campbell County|     0|  0.000|  0.000|   146|  3150.558| 73.986|  46,341|
| |Carbon County|     0|  0.000|  0.000|   106|  7162.162| 106.178|  14,800|
| |Converse County|     0|  0.000|  0.000|    31|  2242.801|  0.000|  13,822|
| |Crook County|     0|  0.000|  0.000|    11|  1450.422| 18.837|   7,584|
| |Fremont County|     0|  0.000|  0.000|   515| 13117.343| 47.302|  39,261|
| |Goshen County|     0|  0.000|  0.000|    37|  2800.696| 118.948|  13,211|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 129.488|   4,413|
| |Weston County|     0|  0.000|  0.000|     5|   721.813|  0.000|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|18,536| 17497.340| N/A|1,059,361|
| |Kent County|     0|  0.000|  0.000| 1,544|  9397.901| 43.477| 164,292|
| |Washington County|     0|  0.000|  0.000|   621|  4945.173| 15.926| 125,577|
| |Providence County|     0|  0.000|  0.000|15,644| 24484.647| 133.482| 638,931|
| |Newport County|     0|  0.000|  0.000|   405|  4934.090| 15.664|  82,082|
| |Bristol County|     0|  0.000|  0.000|   322|  6642.051| 17.681|  48,479|


