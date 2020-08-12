# Analysis of US By County #

Updated: at 2020-08-12

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 131,405 deaths (455.220 deaths/million) and 4,421,141 confirmed cases (15315.977 confirmed cases/million).  This group accounts for 81.04% of all US deaths and for 87.51% of all US cases.

24.52% of this group's deaths (19.87% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 24.96% of this group's deaths (20.22% of the total US deaths) occured in 33 counties in 14 states with a combined population of 41,047,233 (12.51% of the total US population):



The next 25.42% of this group's deaths (20.60% of the total US deaths) occured in 90 counties in 31 states with a combined population of 67,257,463 (20.49% of the total US population)

The remaining 25.11% of this group's deaths (20.35% of the total US deaths) occured in 854 counties in 50 states with a combined population of 143,070,145 (43.59% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,284 deaths (259.845 deaths/million) and 462,344 confirmed cases (11682.002 confirmed cases/million).  This group accounts for 6.34% of all US deaths and for 9.15% of all US cases.

24.78% of this group's deaths (1.57% of the total US deaths) occured in 59 counties in 16 states with a combined population of 1,948,603 (0.59% of the total US population):



The next 25.17% of this group's deaths (1.60% of the total US deaths) occured in 115 counties in 27 states with a combined population of 3,420,982 (1.04% of the total US population):



The next 25.00% of this group's deaths (1.59% of the total US deaths) occured in 234 counties in 33 states with a combined population of 5,710,152 (1.74% of the total US population)

The remaining 25.06% of this group's deaths (1.59% of the total US deaths) occured in 1,744 counties in 47 states with a combined population of 28,497,727 (8.68% of the total US population) 

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
|NJ|21 counties|15,890| 1788.973| N/A|184,815| 20807.368| N/A|8,882,190|
| |Essex County| 2,113| 2644.638|  1.252|19,776| 24751.713| 33.614| 798,975|
| |Bergen County| 2,038| 2186.221|  0.000|20,864| 22381.415| 39.078| 932,202|
| |Hudson County| 1,505| 2238.281|  0.425|19,717| 29323.712| 36.756| 672,391|
| |Middlesex County| 1,408| 1706.538|  0.866|17,959| 21766.849| 33.591| 825,062|
| |Union County| 1,349| 2424.772|  0.257|16,749| 30105.637| 40.828| 556,341|
| |Passaic County| 1,242| 2474.961|  0.000|17,705| 35281.153| 49.249| 501,826|
| |Ocean County| 1,020| 1679.881|  0.706|10,640| 17523.461| 32.704| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,348| 16722.824| 41.094| 618,795|
| |Morris County|   829| 1685.490|  0.000| 7,273| 14787.179| 27.302| 491,845|
| |Mercer County|   621| 1690.118|  0.389| 8,139| 22151.158| 29.549| 367,430|
| |Camden County|   580| 1145.179|  1.128| 8,614| 17007.884| 60.362| 506,471|
| |Somerset County|   562| 1708.549|  1.737| 5,265| 16006.250| 28.664| 328,934|
| |Burlington County|   474| 1064.334|  1.283| 6,042| 13566.888| 51.966| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,497| 13262.791| 41.719| 263,670|
| |Gloucester County|   213| 730.363|  1.959| 3,283| 11257.184| 74.947| 291,636|
| |Sussex County|   198| 1409.373|  2.034| 1,336|  9509.709| 22.371| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,347| 12796.033| 21.713| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,366| 22510.985| 86.941| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,149|  9238.488| 11.486| 124,371|
| |Cape May County|    87| 945.251|  0.000|   840|  9126.566| 35.699|  92,039|
| |Salem County|    87| 1394.566|  4.580|   906| 14522.722| 59.538|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,322| 633.391| N/A|253,131| 13012.086| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,724| 32222.881| 30.321|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.097|43,893| 29725.701| 41.118|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.148|36,272| 37490.207| 32.927| 967,506|
| |Queens County|   985| 436.857|  0.719| 7,886|  3498.958| 17.339|2,253,858|
| |Kings County|   931| 363.498|  0.598| 1,353|   528.708|  2.620|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,954| 42831.403| 26.748| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,987|  9782.280| 49.760| 918,702|
| |Bronx County|   649| 457.712|  0.753|26,856| 18936.919| 93.843|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,180| 29043.487| 27.834| 384,940|
| |New York County|   414| 254.430|  0.418|15,489|  9510.122| 47.128|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 5,002|  6743.330| 34.859| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,602|  7821.457| 26.988| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,619| 15699.243| 30.104| 294,218|
| |Richmond County|   148| 310.949|  0.511| 7,886| 16562.574| 82.077| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,614|  8556.297| 33.200| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,175|  9511.482| 44.980| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,512|  7224.736| 36.861| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,076| 11690.967| 29.766| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,143|  6000.378| 48.747| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,449| 14737.592| 17.436|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   298|  7385.012| 10.621|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,490| 19752.890| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   300|  3145.346|  8.987|  95,379|
| |Columbia County|    37| 622.257|  0.000|   546|  9182.489| 40.843|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,075|  6922.131| 31.276| 155,299|
| |Ontario County|    34| 309.719|  0.000|   362|  3297.594| 13.013| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269| 22.341|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   770|  4851.494| 19.802| 158,714|
| |Tioga County|    25| 518.640|  0.000|   194|  4024.646|  8.891|  48,203|
| |Fulton County|    24| 449.581|  0.000|   297|  5563.569| 32.113|  53,383|
| |Greene County|    18| 381.453|  0.000|   294|  6230.398| 15.137|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   767|  3336.770| 17.402| 229,863|
| |Madison County|    17| 239.636|  0.000|   413|  5821.739| 16.110|  70,941|
| |Washington County|    14| 228.743|  0.000|   260|  4248.088| 11.671|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   258|  2033.049| 19.137| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470| 13.624|  62,914|
| |Yates County|     7| 280.978|  0.000|    57|  2287.962|  5.734|  24,913|
| |Cattaraugus County|     6| 78.826|  0.000|   168|  2207.128|  7.507|  76,117|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959| 18.157|  47,207|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436| 17.920|  39,859|
| |Genesee County|     5| 87.291|  0.000|   279|  4870.810| 14.964|  57,280|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  7.204|  59,493|
| |Herkimer County|     4| 65.233|  0.000|   277|  4517.360| 34.946|  61,319|
| |Montgomery County|     4| 81.266|  0.000|   177|  3596.026| 49.340|  49,221|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  1.326| 107,740|
| |Delaware County|     4| 90.631|  0.000|   106|  2401.722|  6.474|  44,135|
| |Clinton County|     4| 49.699|  0.000|   129|  1602.783|  3.550|  80,485|
| |Seneca County|     3| 88.194|  0.000|    91|  2675.212| 20.999|  34,016|
| |Oswego County|     3| 25.614|  0.000|   255|  2177.180|  7.318| 117,124|
| |Wayne County|     3| 33.364|  0.000|   252|  2802.553|  6.355|  89,918|
| |Chemung County|     3| 35.947|  0.000|   176|  2108.896| 22.253|  83,456|
| |Cayuga County|     2| 26.118|  0.000|   157|  2050.251| 13.059|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697| 15.497|  46,091|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  5.592| 102,180|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Lewis County|     0|  0.000|  0.000|    45|  1711.287| 43.461|  26,296|
| |Cortland County|     0|  0.000|  0.000|    95|  1996.595|  6.005|  47,581|
| |Jefferson County|     0|  0.000|  0.000|   142|  1292.860|  3.902| 109,834|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525| 11.424|  50,022|
| |Essex County|     0|  0.000|  0.000|    56|  1518.232|  3.873|  36,885|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,523| 266.323| N/A|578,946| 14652.327| N/A|39,512,223|
| |Los Angeles County| 4,999| 497.953|  3.401|210,874| 21005.255| 214.433|10,039,107|
| |Riverside County|   820| 331.910|  4.742|41,983| 16993.410| 202.153|2,470,546|
| |Orange County|   724| 227.982|  3.194|40,527| 12761.628| 110.707|3,175,692|
| |San Diego County|   594| 177.933|  1.113|32,975|  9877.693| 105.228|3,338,330|
| |San Bernardino County|   546| 250.449|  4.521|36,072| 16546.144| 134.661|2,180,085|
| |Imperial County|   244| 1346.467|  9.460| 9,867| 54449.135| 279.069| 181,215|
| |San Joaquin County|   235| 308.339| 10.309|13,870| 18198.565| 358.386| 762,148|
| |Santa Clara County|   207| 107.373|  1.112|12,962|  6723.545| 143.165|1,927,852|
| |Alameda County|   205| 122.657|  1.111|13,631|  8155.785| 147.188|1,671,329|
| |Tulare County|   198| 424.715|  1.532|11,549| 24772.895| 477.728| 466,195|
| |Kern County|   183| 203.288|  5.078|24,995| 27765.990| 597.802| 900,202|
| |Sacramento County|   179| 115.331|  2.853|12,274|  7908.210| 193.292|1,552,058|
| |Fresno County|   171| 171.154|  4.719|17,846| 17862.058| 298.411| 999,101|
| |Stanislaus County|   169| 306.904|  8.821|10,264| 18639.451| 248.014| 550,660|
| |Contra Costa County|   146| 126.568|  1.858| 9,787|  8484.421| 199.513|1,153,526|
| |San Mateo County|   122| 159.150|  0.373| 6,431|  8389.286| 128.028| 766,573|
| |Ventura County|    93| 109.928|  2.702| 8,740| 10330.896| 145.727| 846,006|
| |Marin County|    81| 312.952|  2.760| 5,404| 20878.892| 123.635| 258,826|
| |Santa Barbara County|    72| 161.255|  2.880| 6,996| 15668.568| 150.376| 446,499|
| |Merced County|    70| 252.089|  9.775| 5,736| 20656.871| 593.180| 277,680|
| |San Francisco County|    67| 76.003| N/A| 7,692|  8725.550| N/A| 881,549|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993|  0.000| 152,940|
| |Sonoma County|    50| 101.146|  3.179| 3,753|  7592.002| 184.952| 494,336|
| |Yolo County|    44| 199.546|  1.296| 1,834|  8317.460| 142.533| 220,500|
| |Solano County|    41| 91.591|  0.957| 4,274|  9547.787| 149.354| 447,643|
| |Madera County|    39| 247.891|  6.356| 2,463| 15655.291| 316.901| 157,327|
| |Monterey County|    37| 85.241|  0.987| 5,494| 12657.207| 173.774| 434,061|
| |Placer County|    24| 60.252|  2.152| 2,377|  5967.429| 152.064| 398,329|
| |San Luis Obispo County|    17| 60.047|  0.505| 2,278|  8046.314| 177.618| 283,111|
| |Napa County|    11| 79.858|  2.074| 1,129|  8196.364| 154.531| 137,744|
| |Mendocino County|    10| 115.275|  1.647|   472|  5440.985| 215.729|  86,749|
| |Shasta County|    10| 55.531|  0.793|   469|  2604.398| 57.117| 180,080|
| |Butte County|     8| 36.499|  0.000| 1,238|  5648.171| 147.298| 219,186|
| |Sutter County|     7| 72.187|  1.473|   996| 10271.112| 229.818|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,287|  4710.610| 47.582| 273,213|
| |Colusa County|     5| 232.051|  6.630|   396| 18378.429| 258.571|  21,547|
| |Humboldt County|     4| 29.508|  0.000|   286|  2109.798| 43.208| 135,558|
| |Yuba County|     4| 50.847|  0.000|   666|  8465.958| 241.521|  78,668|
| |San Benito County|     4| 63.686|  0.000|   765| 12179.977| 172.862|  62,808|
| |Inyo County|     3| 166.306| 15.839|   106|  5876.157| 332.613|  18,039|
| |Glenn County|     3| 105.660| 10.063|   436| 15355.898| 523.268|  28,393|
| |Amador County|     3| 75.468| 10.781|   185|  4653.854| 172.498|  39,752|
| |Lake County|     2| 31.063|  2.219|   240|  3727.518| 64.344|  64,386|
| |Tuolumne County|     2| 36.712|  0.000|   155|  2845.185| 28.845|  54,478|
| |El Dorado County|     2| 10.371|  0.741|   755|  3915.102| 64.449| 192,843|
| |Mariposa County|     2| 116.259|  0.000|    62|  3604.023| 24.913|  17,203|
| |Tehama County|     1| 15.365|  0.000|   303|  4655.522| 125.113|  65,084|
| |Nevada County|     1| 10.025|  0.000|   357|  3578.768| 58.715|  99,755|
| |Calaveras County|     1| 21.784|  0.000|   147|  3202.266| 34.232|  45,905|
| |Mono County|     1| 69.233|  0.000|   158| 10938.798| 128.575|  14,444|
| |Trinity County|     0|  0.000|  0.000|     5|   407.000|  0.000|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   102|  2342.727| 45.936|  43,539|
| |Sierra County|     0|  0.000|  0.000|     4|  1331.115| 47.540|   3,005|
| |Plumas County|     0|  0.000|  0.000|    36|  1914.181| 22.788|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 16.158|   8,841|
| |Lassen County|     0|  0.000|  0.000|   683| 22339.973| 238.306|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   100|  3595.570| 51.365|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 9,222| 318.045| N/A|517,700| 17854.260| N/A|28,995,881|
| |Harris County| 1,616| 342.858| 25.066|87,505| 18565.450| 241.534|4,713,325|
| |Hidalgo County|   849| 977.315| 31.738|20,431| 23518.862| 440.721| 868,707|
| |Bexar County|   806| 402.285| 11.408|43,164| 21543.717| 134.761|2,003,554|
| |Dallas County|   785| 297.854|  3.415|55,553| 21078.605| 185.488|2,635,516|
| |Tarrant County|   457| 217.359|  4.009|32,469| 15442.934| 211.447|2,102,515|
| |Cameron County|   454| 1072.873| 23.969|16,906| 39951.508| 717.387| 423,163|
| |Travis County|   307| 240.982|  7.513|23,249| 18249.482| 190.633|1,273,954|
| |El Paso County|   307| 365.808|  9.022|16,936| 20180.211| 305.379| 839,238|
| |Nueces County|   249| 687.287| 17.744|15,731| 43420.537| 1150.605| 362,294|
| |Webb County|   175| 632.564| 49.572| 8,490| 30688.374| 960.980| 276,652|
| |Fort Bend County|   164| 202.048|  3.168|10,335| 12732.725| 536.448| 811,688|
| |Galveston County|   114| 333.198|  3.340| 9,605| 28073.385| 253.030| 342,139|
| |Brazoria County|    96| 256.503|  6.871| 7,591| 20282.474| 327.882| 374,264|
| |Williamson County|    95| 160.867|  3.629| 7,011| 11871.964| 261.499| 590,551|
| |Montgomery County|    94| 154.760|  4.939| 6,776| 11155.911| 89.140| 607,391|
| |Collin County|    93| 89.879|  2.899| 8,052|  7781.740| 225.180|1,034,730|
| |Denton County|    91| 102.569|  2.093| 7,867|  8867.153| 134.451| 887,207|
| |Jefferson County|    84| 333.910|  6.247| 5,977| 23759.267| 208.978| 251,565|
| |Lubbock County|    75| 241.492|  4.140| 6,222| 20034.195| 262.192| 310,569|
| |Starr County|    73| 1129.454| 46.416| 2,249| 34796.466| 592.356|  64,633|
| |Comal County|    70| 448.118|  4.573| 1,929| 12348.840| 191.136| 156,209|
| |Ector County|    57| 342.913|  4.297| 3,616| 21753.909| 151.260| 166,223|
| |McLennan County|    57| 222.116|  9.464| 5,031| 19604.634| 256.073| 256,623|
| |Guadalupe County|    56| 335.637|  9.418| 1,696| 10165.001| 73.635| 166,847|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 375.902|  49,025|
| |Midland County|    49| 277.099|  5.655| 2,788| 15766.377| 344.152| 176,832|
| |Brazos County|    49| 213.777|  3.740| 4,092| 17852.546| 97.228| 229,211|
| |Victoria County|    47| 510.404| 23.271| 3,494| 37943.617| 252.875|  92,084|
| |Angelina County|    46| 530.473| 14.827| 1,828| 21080.551| 136.737|  86,715|
| |Potter County|    45| 383.256|  7.300| 3,711| 31605.843| 200.753| 117,415|
| |Maverick County|    44| 749.293|  0.000| 2,321| 39525.221| 270.038|  58,722|
| |Ellis County|    43| 232.651|  6.183| 3,120| 16880.742| 444.433| 184,826|
| |Nacogdoches County|    42| 644.132| 10.955| 1,167| 17897.675| 247.575|  65,204|
| |Hays County|    41| 178.113|  4.344| 5,066| 22007.811| 83.781| 230,191|
| |Walker County|    41| 561.867|  5.873| 3,074| 42126.324| 454.192|  72,971|
| |Bell County|    39| 107.461|  2.362| 3,957| 10903.109| 141.313| 362,924|
| |Washington County|    39| 1086.896|  3.981|   515| 14352.600| 67.682|  35,882|
| |Liberty County|    34| 385.405|  9.716| 1,002| 11358.097| 238.044|  88,219|
| |Bowie County|    33| 353.906|  3.064|   762|  8172.020| 85.795|  93,245|
| |Johnson County|    30| 170.632|  2.438| 1,980| 11261.710| 293.324| 175,817|
| |San Patricio County|    30| 449.573| 27.831|   972| 14566.162| 295.434|  66,730|
| |Willacy County|    30| 1404.626| 60.198|   710| 33242.813| 642.115|  21,358|
| |Hale County|    29| 868.108| 21.382| 1,439| 43076.094| 893.766|  33,406|
| |Matagorda County|    28| 764.130| 19.493|   770| 21013.563| 319.687|  36,643|
| |Gregg County|    27| 217.839|  6.916| 1,416| 11424.422| 108.343| 123,945|
| |Taylor County|    27| 195.604|  6.210| 1,130|  8186.389| 24.839| 138,034|
| |Medina County|    26| 504.032|  5.539|   892| 17292.184| 767.126|  51,584|
| |Wharton County|    26| 625.662| 10.313|   815| 19612.090| 598.160|  41,556|
| |Tom Green County|    26| 218.121|  0.000| 2,740| 22986.577| 316.395| 119,200|
| |Caldwell County|    26| 595.456|  6.543| 1,158| 26520.704| 255.196|  43,664|
| |Kaufman County|    25| 183.616|  3.148| 2,289| 16811.845| 408.151| 136,154|
| |Smith County|    24| 103.114|  3.683| 2,524| 10844.207| 95.135| 232,751|
| |Harrison County|    23| 345.589|  2.147|   713| 10713.266| 178.161|  66,553|
| |Grimes County|    23| 796.399| 14.840|   891| 30851.801| 183.023|  28,880|
| |Orange County|    22| 263.802|  8.565| 1,493| 17902.537| 416.258|  83,396|
| |Hunt County|    21| 212.995|  1.449| 1,202| 12191.411| 140.548|  98,594|
| |Randall County|    21| 152.491|  3.112| 1,747| 12685.803| 128.632| 137,713|
| |Bastrop County|    21| 236.692|  4.830| 1,375| 15497.673| 117.541|  88,723|
| |DeWitt County|    19| 942.460| 28.345|   700| 34722.222| 524.376|  20,160|
| |Parker County|    19| 132.981|  3.999| 1,292|  9042.680| 168.975| 142,878|
| |Lavaca County|    19| 942.741| 35.441|   633| 31408.157| 141.766|  20,154|
| |Wilson County|    19| 372.038|  8.392|   448|  8772.273| 72.729|  51,070|
| |Lamar County|    18| 361.018|  5.730|   655| 13137.046| 42.978|  49,859|
| |Shelby County|    18| 712.194|  5.652|   405| 16024.373| 124.351|  25,274|
| |Panola County|    18| 776.063|  6.159|   297| 12805.036| 160.140|  23,194|
| |Atascosa County|    18| 351.886|  8.378|   456|  8914.433| 120.088|  51,153|
| |Deaf Smith County|    17| 916.640|  0.000|   674| 36342.068| 477.577|  18,546|
| |Jim Wells County|    16| 395.237| 17.645|   777| 19193.716| 494.047|  40,482|
| |Brown County|    16| 422.565|  3.773|   398| 10511.304| 158.462|  37,864|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Hardin County|    15| 260.408|  9.920|   973| 16891.775| 282.728|  57,602|
| |Aransas County|    15| 638.026| 18.229|   182|  7741.387| 145.835|  23,510|
| |Anderson County|    14| 242.487|  9.897| 2,406| 41673.162| 190.526|  57,735|
| |Moore County|    14| 668.577| 13.644| 1,063| 50764.088| 272.889|  20,940|
| |Fayette County|    14| 552.355|  5.636|   390| 15387.043| 101.453|  25,346|
| |Grayson County|    13| 95.439|  2.098| 1,169|  8582.210| 140.537| 136,212|
| |Rockwall County|    13| 123.910|  0.000| 1,031|  9827.003| 400.324| 104,915|
| |Henderson County|    12| 145.038|  1.727|   641|  7747.441| 63.886|  82,737|
| |Polk County|    12| 233.677|  2.782|   750| 14604.794| 178.039|  51,353|
| |San Augustine County|    11| 1335.438|  0.000|   162| 19667.355| 104.060|   8,237|
| |Wichita County|    11| 83.188|  1.080| 1,039|  7857.521| 115.599| 132,230|
| |Bee County|    11| 337.786|  8.774| 1,246| 38261.938| 2531.201|  32,565|
| |Red River County|    11| 914.913|  0.000|   137| 11394.827| 35.646|  12,023|
| |Jasper County|    11| 309.606| 24.125|   332|  9344.479| 124.647|  35,529|
| |Lamb County|    11| 853.176| 33.241|   233| 18071.822| 288.085|  12,893|
| |Gonzales County|    10| 479.916| 13.712|   684| 32826.223| 363.365|  20,837|
| |Hood County|    10| 162.224|  2.317|   567|  9198.125| 201.622|  61,643|
| |Uvalde County|    10| 373.958| 16.027|   555| 20754.646| 288.482|  26,741|
| |Lee County|    10| 580.080| 16.574|   177| 10267.417| 190.598|  17,239|
| |Burnet County|     9| 186.896|  5.933|   567| 11774.478| 68.232|  48,155|
| |Palo Pinto County|     9| 308.335| 14.683|   297| 10175.066| 357.277|  29,189|
| |Marion County|     9| 913.335| 14.497|   134| 13598.539| 101.482|   9,854|
| |Navarro County|     9| 179.594|  2.851|   883| 17620.178| 253.712|  50,113|
| |Cherokee County|     8| 151.958|  8.141| 1,151| 21863.010| 933.459|  52,646|
| |Cass County|     8| 266.436|  4.758|   185|  6161.327| 128.460|  30,026|
| |Kleberg County|     8| 260.756|  9.313|   451| 14700.130| 353.883|  30,680|
| |Wise County|     8| 114.312|  6.124|   449|  6415.752| 244.954|  69,984|
| |San Jacinto County|     8| 277.210|  0.000|   182|  6306.525| 158.406|  28,859|
| |Fannin County|     8| 225.263|  0.000|   266|  7490.004| 189.060|  35,514|
| |Hill County|     7| 191.001| 11.694|   328|  8949.767| 66.266|  36,649|
| |Jackson County|     7| 474.255| 19.357|   408| 27642.276| 619.435|  14,760|
| |Karnes County|     7| 448.689| 18.314|   644| 41279.405| 2747.077|  15,601|
| |Parmer County|     7| 728.787|  0.000|   345| 35918.792| 446.196|   9,605|
| |Houston County|     7| 304.772|  6.220|   317| 13801.811| 80.858|  22,968|
| |Andrews County|     7| 374.231|  7.637|   304| 16252.339| 274.946|  18,705|
| |Wood County|     7| 153.714|  6.274|   321|  7048.903| 59.604|  45,539|
| |Floyd County|     6| 1050.420| 25.010|    91| 15931.373| 150.060|   5,712|
| |Gillespie County|     6| 222.321|  5.293|   176|  6521.417| 26.467|  26,988|
| |Duval County|     6| 537.779| 25.609|   188| 16850.408| 460.953|  11,157|
| |Sabine County|     6| 569.152|  0.000|    62|  5881.237| 176.166|  10,542|
| |Zavala County|     6| 506.757| 12.066|   220| 18581.081| 446.429|  11,840|
| |Kerr County|     6| 114.068|  0.000|   400|  7604.563| 76.046|  52,600|
| |Burleson County|     6| 325.327|  7.746|   248| 13446.836| 123.934|  18,443|
| |Howard County|     6| 163.648| 11.689|   177|  4827.624| 62.342|  36,664|
| |Camp County|     6| 458.225| 10.910|   242| 18481.747| 261.843|  13,094|
| |Blanco County|     5| 419.076|  0.000|   114|  9554.941| 191.578|  11,931|
| |Young County|     5| 277.624|  7.932|   185| 10272.071| 317.284|  18,010|
| |Erath County|     5| 117.102|  0.000|   555| 12998.267| 264.315|  42,698|
| |Dallam County|     5| 686.153|  0.000|   193| 26485.522| 254.857|   7,287|
| |Calhoun County|     5| 234.852|  6.710|   546| 25645.843| 355.633|  21,290|
| |Goliad County|     5| 652.912| 37.309|    96| 12535.910| 354.438|   7,658|
| |Martin County|     5| 866.401| 49.509|    63| 10916.652| 420.823|   5,771|
| |Waller County|     5| 90.504|  2.586|   465|  8416.899| 134.464|  55,246|
| |Coryell County|     5| 65.832|  0.000|   686|  9032.139| 124.140|  75,951|
| |Frio County|     5| 246.233|  0.000|   514| 25312.715| 267.338|  20,306|
| |Reeves County|     5| 312.969| 17.884|   148|  9263.896| 62.594|  15,976|
| |Kendall County|     4| 84.333|  0.000|   163|  3436.571| 45.178|  47,431|
| |Hockley County|     4| 173.754|  0.000|   214|  9295.860| 155.138|  23,021|
| |Castro County|     4| 531.208|  0.000|   205| 27224.436| 436.350|   7,530|
| |Refugio County|     4| 575.705| 82.244|   234| 33678.756| 411.218|   6,948|
| |Newton County|     4| 294.226|  0.000|   116|  8532.549| 283.718|  13,595|
| |Dawson County|     4| 314.268|  0.000|   157| 12335.009| 224.477|  12,728|
| |Lynn County|     4| 672.156|  0.000|    73| 12266.846| 168.039|   5,951|
| |Live Oak County|     4| 327.681| 23.406|   230| 18841.648| 269.166|  12,207|
| |Bailey County|     4| 571.429|  0.000|   175| 25000.000| 326.531|   7,000|
| |Trinity County|     4| 273.019| 19.501|   156| 10647.737| 39.003|  14,651|
| |Austin County|     4| 133.191|  4.757|   269|  8957.112| 252.112|  30,032|
| |Comanche County|     3| 220.022|  0.000|   150| 11001.100|  0.000|  13,635|
| |Callahan County|     3| 215.162|  0.000|    47|  3370.867| 40.983|  13,943|
| |Brooks County|     3| 422.952| 40.281|   135| 19032.849| 886.186|   7,093|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402| 45.868|   6,229|
| |Yoakum County|     3| 344.313| 16.396|   106| 12165.729| 278.730|   8,713|
| |Dimmit County|     3| 296.326| 28.221|   155| 15310.154| 338.658|  10,124|
| |Bandera County|     3| 129.803|  0.000|    92|  3980.616| 55.630|  23,112|
| |Falls County|     3| 173.440|  8.259|   135|  7804.822| 189.959|  17,297|
| |Crockett County|     3| 866.051|  0.000|   158| 45612.009| 82.481|   3,464|
| |Chambers County|     3| 68.435|  3.259|   981| 22378.356| 224.859|  43,837|
| |Cooke County|     3| 72.715|  0.000|   248|  6011.101| 159.280|  41,257|
| |Gaines County|     3| 139.587| 19.941|   172|  8002.978| 239.292|  21,492|
| |Van Zandt County|     3| 53.013|  0.000|   394|  6962.361| 108.550|  56,590|
| |Stephens County|     3| 320.307| 15.253|    49|  5231.689| 289.802|   9,366|
| |Hamilton County|     3| 354.568| 16.884|    91| 10755.230| 607.831|   8,461|
| |Hutchinson County|     3| 143.280|  6.823|   128|  6113.287| 68.229|  20,938|
| |Lampasas County|     3| 140.004|  6.667|   110|  5133.470| 180.005|  21,428|
| |Milam County|     3| 120.856|  0.000|   350| 14099.827| 132.366|  24,823|
| |Nolan County|     3| 203.887|  0.000|   136|  9242.898| 48.545|  14,714|
| |Leon County|     3| 172.374| 16.417|   145|  8331.418| 57.458|  17,404|
| |Limestone County|     3| 128.003|  0.000|   254| 10837.565| 323.055|  23,437|
| |Morris County|     3| 242.170| 23.064|   125| 10090.410| 322.893|  12,388|
| |Reagan County|     3| 779.423|  0.000|    63| 16367.888| 111.346|   3,849|
| |Ochiltree County|     2| 203.335|  0.000|    95|  9658.398| 130.715|   9,836|
| |Zapata County|     2| 141.054|  0.000|   179| 12624.304| 191.430|  14,179|
| |Montague County|     2| 100.918|  7.208|    77|  3885.357| 122.544|  19,818|
| |Robertson County|     2| 117.137|  0.000|   234| 13705.049| 150.605|  17,074|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 94.985|   7,520|
| |Swisher County|     2| 270.380|  0.000|    82| 11085.575| 115.877|   7,397|
| |Madison County|     2| 140.017|  0.000|   667| 46695.603| 220.026|  14,284|
| |Runnels County|     2| 194.856| 13.918|   129| 12568.200| 236.611|  10,264|
| |Terry County|     2| 162.114|  0.000|   159| 12888.060| 440.024|  12,337|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890|  0.000|   1,501|
| |Tyler County|     2| 92.285|  0.000|   127|  5860.096| 79.101|  21,672|
| |Upshur County|     2| 47.901|  0.000|   250|  5987.594| 191.603|  41,753|
| |Presidio County|     2| 298.329| 42.618|    47|  7010.740| 63.928|   6,704|
| |Rusk County|     2| 36.761|  0.000|   377|  6929.383| 102.405|  54,406|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 66.600|  10,725|
| |Hudspeth County|     2| 409.333|  0.000|    24|  4911.993| 58.476|   4,886|
| |Hansford County|     2| 370.439|  0.000|    80| 14817.559| 582.118|   5,399|
| |Colorado County|     2| 93.054|  0.000|   308| 14330.247| 338.981|  21,493|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461| 15.523|   9,203|
| |Bosque County|     2| 107.038|  0.000|   166|  8884.132| 237.012|  18,685|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 84.356|   3,387|
| |Hopkins County|     2| 53.932|  3.852|   206|  5554.956| 100.159|  37,084|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Gray County|     2| 91.383|  0.000|   218|  9960.705| 143.601|  21,886|
| |Culberson County|     2| 921.234|  0.000|    17|  7830.493| 65.802|   2,171|
| |Hall County|     1| 337.382|  0.000|    14|  4723.347| 240.987|   2,964|
| |Mitchell County|     1| 117.028| 16.718|    68|  7957.870| 200.619|   8,545|
| |Sutton County|     1| 264.831|  0.000|    66| 17478.814| 226.998|   3,776|
| |Ward County|     1| 83.347|  0.000|    93|  7751.292| 107.161|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Jim Hogg County|     1| 192.308|  0.000|    64| 12307.692| 274.725|   5,200|
| |Fisher County|     1| 261.097|  0.000|    29|  7571.802| 111.899|   3,830|
| |Real County|     1| 289.687| 41.384|    88| 25492.468| 455.223|   3,452|
| |Scurry County|     1| 59.869|  0.000|   488| 29216.308| 290.795|  16,703|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 68.495|  12,514|
| |Eastland County|     1| 54.466|  0.000|    79|  4302.832| 163.399|  18,360|
| |Wilbarger County|     1| 78.315|  0.000|    75|  5873.600| 257.320|  12,769|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 51.148|   2,793|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Pecos County|     1| 63.199|  0.000|   249| 15736.586| 243.768|  15,823|
| |Crosby County|     1| 174.307|  0.000|    63| 10981.349| 224.109|   5,737|
| |Winkler County|     1| 124.844|  0.000|    85| 10611.735| 249.688|   8,010|
| |Kimble County|     1| 230.574| 32.939|    14|  3228.038| 32.939|   4,337|
| |Knox County|     1| 272.926| 38.989|    60| 16375.546| 467.873|   3,664|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505| 19.664|  21,795|
| |McCulloch County|     1| 125.251|  0.000|    51|  6387.776| 143.143|   7,984|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Clay County|     1| 95.502|  0.000|    43|  4106.580| 109.145|  10,471|
| |Edwards County|     0|  0.000|  0.000|    28| 14492.754| 221.828|   1,932|
| |Mills County|     0|  0.000|  0.000|    22|  4514.673| 175.896|   4,873|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Mason County|     0|  0.000|  0.000|    54| 12634.534| 401.096|   4,274|
| |Archer County|     0|  0.000|  0.000|    27|  3156.787| 116.918|   8,553|
| |McMullen County|     0|  0.000|  0.000|     9| 12113.055| 192.271|     743|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 28.255|   5,056|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Freestone County|     0|  0.000|  0.000|   162|  8216.260| 166.644|  19,717|
| |Carson County|     0|  0.000|  0.000|    16|  2699.966| 48.214|   5,926|
| |Hardeman County|     0|  0.000|  0.000|    21|  5339.436| 181.613|   3,933|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Hartley County|     0|  0.000|  0.000|    90| 16140.603| 204.960|   5,576|
| |Concho County|     0|  0.000|  0.000|    31| 11371.974| 262.027|   2,726|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    67|  7498.601| 383.724|   8,935|
| |Lipscomb County|     0|  0.000|  0.000|    20|  6186.205| 220.936|   3,233|
| |Kinney County|     0|  0.000|  0.000|    19|  5181.347| 77.915|   3,667|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Haskell County|     0|  0.000|  0.000|    43|  7599.859| 100.995|   5,658|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Somervell County|     0|  0.000|  0.000|    77|  8435.583| 250.407|   9,128|
| |Sherman County|     0|  0.000|  0.000|    41| 13567.174| 189.090|   3,022|
| |Shackelford County|     0|  0.000|  0.000|    19|  5819.296| 87.508|   3,265|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |San Saba County|     0|  0.000|  0.000|    24|  3963.666| 47.187|   6,055|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704| 105.820|   1,350|
| |Baylor County|     0|  0.000|  0.000|    12|  3419.778| 203.558|   3,509|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 217.903|   3,278|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 250.363|   2,853|
| |Hemphill County|     0|  0.000|  0.000|    42| 10997.643|  0.000|   3,819|
| |Jones County|     0|  0.000|  0.000|   600| 29876.015|  0.000|  20,083|
| |Childress County|     0|  0.000|  0.000|    47|  6433.069| 215.087|   7,306|
| |Coleman County|     0|  0.000|  0.000|    24|  2935.780| 192.224|   8,175|
| |Collingsworth County|     0|  0.000|  0.000|    12|  4109.589| 244.618|   2,920|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  1.507|26,565| 16482.606| 47.687|1,611,699|
| |Essex County| 1,194| 1513.243|  1.448|17,930| 22723.989| 78.939| 789,034|
| |Suffolk County| 1,076| 1338.463|  2.488|22,017| 27387.496| 95.249| 803,907|
| |Worcester County| 1,007| 1212.344|  2.408|13,686| 16476.809| 37.321| 830,622|
| |Norfolk County|   997| 1410.633|  1.213|10,682| 15113.721| 47.499| 706,775|
| |Plymouth County|   723| 1387.178|  2.467| 9,288| 17820.346| 34.261| 521,202|
| |Hampden County|   709| 1520.246|  3.063| 7,637| 16375.340| 42.272| 466,372|
| |Bristol County|   637| 1127.001|  2.780| 9,408| 16644.935| 46.506| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,803|  8465.186| 22.134| 212,990|
| |Hampshire County|   130| 808.307|  2.665| 1,184|  7361.811| 34.642| 160,830|
| |Franklin County|    61| 869.194|  2.036|   411|  5856.369| 10.178|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  6.860| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,553| 398.226| N/A|542,071| 25238.739| N/A|21,477,737|
| |Miami-Dade County| 1,909| 702.629|  9.727|135,130| 49736.100| 545.309|2,716,940|
| |Palm Beach County|   940| 628.019|  7.540|37,641| 25148.152| 258.843|1,496,770|
| |Broward County|   856| 438.350|  6.657|63,605| 32571.547| 340.321|1,952,778|
| |Pinellas County|   513| 526.156|  7.766|18,103| 18567.256| 154.726| 974,996|
| |Hillsborough County|   395| 268.348|  2.523|32,996| 22416.248| 213.320|1,471,968|
| |Lee County|   351| 455.503|  7.230|16,718| 21695.431| 156.469| 770,577|
| |Polk County|   326| 449.794|  7.884|14,645| 20206.215| 278.706| 724,777|
| |Orange County|   315| 226.057|  7.587|32,042| 22994.692| 194.994|1,393,452|
| |Manatee County|   234| 580.281| 16.650| 9,395| 23298.029| 179.965| 403,253|
| |Duval County|   198| 206.733|  5.370|23,741| 24788.177| 254.613| 957,755|
| |St. Lucie County|   180| 548.284| 21.757| 5,920| 18032.452| 257.171| 328,297|
| |Sarasota County|   162| 373.494| 11.198| 6,314| 14557.041| 151.505| 433,742|
| |Brevard County|   157| 260.822|  8.069| 6,190| 10283.383| 123.173| 601,942|
| |Collier County|   143| 371.523|  5.196|10,487| 27245.896| 218.980| 384,902|
| |Volusia County|   140| 253.035|  5.680| 8,040| 14531.416| 194.165| 553,284|
| |Escambia County|   131| 411.541| 13.464| 9,807| 30809.007| 693.381| 318,316|
| |Pasco County|   131| 236.485|  7.737| 7,172| 12947.087| 138.229| 553,947|
| |Seminole County|   130| 275.525| 12.414| 7,219| 15300.132| 138.974| 471,826|
| |Osceola County|   106| 282.102|  6.843| 9,858| 26235.459| 319.360| 375,751|
| |Marion County|   102| 279.009| 10.160| 6,668| 18239.560| 482.210| 365,579|
| |Martin County|    99| 614.907| 16.859| 3,852| 23925.466| 172.138| 161,000|
| |Charlotte County|    94| 497.591|  3.781| 2,281| 12074.533| 155.025| 188,910|
| |Lake County|    68| 185.227|  6.226| 5,229| 14243.377| 179.000| 367,118|
| |Indian River County|    57| 356.422|  6.253| 2,555| 15976.439| 166.151| 159,923|
| |Bay County|    52| 297.645| 12.266| 4,523| 25889.356| 492.258| 174,705|
| |Clay County|    52| 237.170|  1.955| 3,327| 15174.320| 223.487| 219,252|
| |Hernando County|    50| 257.838|  9.577| 2,069| 10669.348| 196.694| 193,920|
| |Okaloosa County|    45| 213.535|  7.457| 3,587| 17021.135| 326.065| 210,738|
| |Suwannee County|    44| 990.612| 22.514| 1,507| 33928.451| 977.747|  44,417|
| |Sumter County|    42| 317.173|  4.315| 1,344| 10149.524| 195.266| 132,420|
| |Jackson County|    41| 883.354| 24.623| 1,936| 41711.553| 901.821|  46,414|
| |Santa Rosa County|    40| 217.022|  7.751| 4,013| 21772.745| 357.311| 184,313|
| |Hendry County|    38| 904.288|  3.400| 1,805| 42953.691| 387.552|  42,022|
| |Highlands County|    37| 348.330|  9.414| 1,474| 13876.729| 239.393| 106,221|
| |Citrus County|    37| 247.232|  2.864| 1,594| 10651.022| 259.641| 149,657|
| |St. Johns County|    36| 136.017|  3.239| 3,738| 14123.141| 170.562| 264,672|
| |Putnam County|    27| 362.314| 13.419| 1,539| 20651.897| 272.215|  74,521|
| |Leon County|    26| 88.561|  5.353| 5,116| 17426.136| 305.099| 293,582|
| |Alachua County|    26| 96.639|  0.531| 4,246| 15781.864| 232.570| 269,043|
| |Gadsden County|    21| 459.921|  0.000| 1,928| 42225.142| 1026.219|  45,660|
| |DeSoto County|    18| 473.672|  7.519| 1,377| 36235.889| 259.392|  38,001|
| |Walton County|    16| 216.009|  3.857| 1,428| 19278.800| 273.869|  74,071|
| |Columbia County|    16| 223.196|  5.978| 2,917| 40691.348| 557.989|  71,686|
| |Washington County|    14| 549.602|  0.000|   877| 34428.611| 1127.244|  25,473|
| |Monroe County|    13| 175.136|  0.000| 1,548| 20854.664| 306.007|  74,228|
| |Flagler County|    13| 112.964|  0.000| 1,095|  9515.037| 166.342| 115,081|
| |Okeechobee County|    12| 284.576| 20.327| 1,077| 25540.694| 372.659|  42,168|
| |Nassau County|    11| 124.118|  0.000| 1,253| 14138.223| 185.372|  88,625|
| |Madison County|     8| 432.596|  0.000|   710| 38392.905| 378.522|  18,493|
| |Calhoun County|     8| 567.175| 10.128|   481| 34101.382| 1498.962|  14,105|
| |Liberty County|     7| 837.922| 85.502|   407| 48719.176|  0.000|   8,354|
| |Hardee County|     7| 259.866|  0.000|   986| 36603.928| 684.136|  26,937|
| |Gilchrist County|     6| 322.893| 23.064|   369| 19857.927| 269.078|  18,582|
| |Taylor County|     5| 231.814|  6.623|   981| 45481.942| 2848.003|  21,569|
| |Wakulla County|     5| 148.196|  4.234|   726| 21518.124| 419.184|  33,739|
| |Union County|     5| 328.149|  9.376|   435| 28548.927| 1950.140|  15,237|
| |Levy County|     5| 120.473|  3.442|   698| 16818.061| 244.389|  41,503|
| |Jefferson County|     5| 350.976|  0.000|   462| 32430.156| 451.254|  14,246|
| |Bradford County|     4| 141.839|  0.000|   519| 18403.603| 901.690|  28,201|
| |Dixie County|     4| 237.727|  0.000|   562| 33400.689| 2360.293|  16,826|
| |Hamilton County|     4| 277.239|  9.901|   623| 43179.928| 306.943|  14,428|
| |Baker County|     4| 136.939|  0.000|   964| 33002.396| 2645.865|  29,210|
| |Glades County|     3| 217.218|  0.000|   406| 29396.858| 144.812|  13,811|
| |Holmes County|     3| 152.929|  7.282|   509| 25946.883| 378.680|  19,617|
| |Lafayette County|     2| 237.473| 16.962|   189| 22441.225| 1289.141|   8,422|
| |Franklin County|     2| 164.948|  0.000|   433| 35711.340| 2874.816|  12,125|
| |Gulf County|     2| 146.638|  0.000|   685| 50223.623| 2828.025|  13,639|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,657| 604.254| N/A|196,900| 15538.414| N/A|12,671,821|
| |Cook County| 4,933| 957.821|  0.860|112,484| 21840.565| 131.478|5,150,233|
| |DuPage County|   522| 565.596|  1.393|12,427| 13464.858| 114.234| 922,921|
| |Lake County|   447| 641.748|  1.436|12,852| 18451.334| 129.006| 696,535|
| |Will County|   346| 500.910|  1.241| 9,413| 13627.355| 141.463| 690,743|
| |Kane County|   305| 572.874|  1.878| 9,878| 18553.614| 145.432| 532,403|
| |St. Clair County|   161| 619.980|  2.751| 4,107| 15815.254| 226.097| 259,686|
| |Winnebago County|   131| 463.599|  2.022| 3,797| 13437.283| 47.017| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,250| 10559.696| 120.218| 307,774|
| |Madison County|    76| 289.011|  1.630| 2,702| 10275.093| 236.858| 262,966|
| |Kankakee County|    69| 628.061|  1.300| 1,802| 16402.396| 135.235| 109,862|
| |Peoria County|    36| 200.916|  0.797| 1,667|  9303.546| 213.673| 179,179|
| |Rock Island County|    36| 253.737|  4.028| 1,764| 12433.130| 150.027| 141,879|
| |Sangamon County|    33| 169.516|  0.000| 1,297|  6662.489| 176.120| 194,672|
| |DeKalb County|    30| 285.995|  1.362|   947|  9027.904| 103.503| 104,897|
| |LaSalle County|    24| 220.854|  5.258|   801|  7371.007| 294.472| 108,669|
| |Kendall County|    23| 178.308|  0.000| 1,398| 10838.049| 114.073| 128,990|
| |Boone County|    23| 429.553|  0.000|   769| 14362.020| 80.041|  53,544|
| |Macon County|    23| 221.135|  0.000|   650|  6249.459| 203.279| 104,009|
| |Union County|    23| 1381.133| 17.157|   327| 19636.102| 188.726|  16,653|
| |Coles County|    21| 414.848|  5.644|   492|  9719.286| 228.589|  50,621|
| |Jackson County|    20| 352.423|  2.517|   731| 12881.057| 183.763|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,693|  8073.862| 79.710| 209,689|
| |Jefferson County|    19| 504.193|  7.582|   292|  7748.647| 382.883|  37,684|
| |Whiteside County|    17| 308.111|  2.589|   366|  6633.439| 119.102|  55,175|
| |Clinton County|    17| 452.585|  0.000|   415| 11048.400| 235.801|  37,562|
| |McDonough County|    15| 505.357|  0.000|   145|  4885.116| 57.755|  29,682|
| |McLean County|    15| 87.455|  0.000|   670|  3906.318| 71.630| 171,517|
| |Monroe County|    13| 375.321|  0.000|   323|  9325.288| 160.852|  34,637|
| |Cass County|    11| 905.573|  0.000|   233| 19181.691| 352.821|  12,147|
| |Iroquois County|    11| 405.694| 10.538|   267|  9847.311| 89.569|  27,114|
| |Tazewell County|     8| 60.697|  0.000|   610|  4628.119| 221.109| 131,803|
| |Randolph County|     7| 220.250|  0.000|   474| 14914.102| 175.301|  31,782|
| |Jasper County|     7| 728.408|  0.000|    60|  6243.496| 74.327|   9,610|
| |Montgomery County|     7| 246.357|  0.000|   171|  6018.160| 120.665|  28,414|
| |Morgan County|     6| 178.264|  0.000|   269|  7992.156| 271.640|  33,658|
| |Stephenson County|     6| 134.838|  0.000|   334|  7505.955| 41.735|  44,498|
| |Williamson County|     6| 90.094|  2.145|   434|  6516.810| 193.059|  66,597|
| |Adams County|     6| 91.694|  2.183|   557|  8512.264| 224.869|  65,435|
| |Grundy County|     5| 97.936|  0.000|   334|  6542.093| 131.513|  51,054|
| |Ogle County|     5| 98.730|  0.000|   416|  8214.363| 93.089|  50,643|
| |Christian County|     4| 123.824|  0.000|   143|  4426.696| 114.979|  32,304|
| |Mercer County|     4| 259.118|  9.254|    76|  4923.236| 27.763|  15,437|
| |Carroll County|     4| 279.623|  9.987|    61|  4264.243| 149.798|  14,305|
| |Livingston County|     3| 84.156|  4.007|   122|  3422.352| 104.193|  35,648|
| |Fayette County|     3| 140.607|  0.000|    69|  3233.971| 73.652|  21,336|
| |Woodford County|     3| 78.005|  0.000|   158|  4108.271| 193.156|  38,459|
| |Cumberland County|     3| 278.655| 13.269|    57|  5294.445| 132.693|  10,766|
| |Macoupin County|     3| 66.776|  0.000|   182|  4051.106| 127.193|  44,926|
| |Bureau County|     3| 91.946|  4.378|   231|  7079.809| 337.134|  32,628|
| |Bond County|     3| 182.637|  8.697|    62|  3774.504| 43.485|  16,426|
| |Saline County|     2| 85.139|  6.081|   134|  5704.312| 115.546|  23,491|
| |Vermilion County|     2| 26.400|  0.000|   234|  3088.783| 30.171|  75,758|
| |Perry County|     2| 95.621|  6.830|   184|  8797.093| 396.142|  20,916|
| |Wayne County|     2| 123.343|  8.810|    66|  4070.305| 140.963|  16,215|
| |Jersey County|     2| 91.857|  6.561|   117|  5373.628| 288.693|  21,773|
| |Gallatin County|     2| 414.250| 59.179|    51| 10563.380| 177.536|   4,828|
| |Ford County|     2| 154.309| 11.022|    50|  3857.727| 88.177|  12,961|
| |Clark County|     2| 129.525| 18.504|    87|  5634.350| 157.281|  15,441|
| |Douglas County|     2| 102.749|  0.000|   122|  6267.660| 139.444|  19,465|
| |Hancock County|     1| 56.472|  0.000|    63|  3557.714| 225.887|  17,708|
| |Effingham County|     1| 29.405|  0.000|   163|  4792.990| 184.830|  34,008|
| |Franklin County|     1| 25.995|  3.714|   194|  5043.022| 222.814|  38,469|
| |Pulaski County|     1| 187.441| 26.777|    94| 17619.494| 80.332|   5,335|
| |Shelby County|     1| 46.224|  0.000|    86|  3975.224| 151.877|  21,634|
| |Logan County|     1| 34.943|  4.992|   157|  5486.058| 349.430|  28,618|
| |Lee County|     1| 29.329|  0.000|   178|  5220.554| 125.696|  34,096|
| |Henry County|     1| 20.444|  0.000|   253|  5172.449| 131.429|  48,913|
| |Knox County|     1| 20.121|  0.000|   313|  6297.913| 137.973|  49,699|
| |Jo Daviess County|     1| 47.092|  0.000|   130|  6121.968| 94.184|  21,235|
| |Schuyler County|     0|  0.000|  0.000|    18|  2659.574| 21.108|   6,768|
| |Pike County|     0|  0.000|  0.000|    24|  1542.317| 100.985|  15,561|
| |Piatt County|     0|  0.000|  0.000|    63|  3854.626| 104.888|  16,344|
| |Moultrie County|     0|  0.000|  0.000|    75|  5172.057| 128.070|  14,501|
| |Menard County|     0|  0.000|  0.000|    57|  4673.663| 93.708|  12,196|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 102.603|   4,177|
| |White County|     0|  0.000|  0.000|    71|  5244.884| 116.084|  13,537|
| |Washington County|     0|  0.000|  0.000|    67|  4824.656| 82.297|  13,887|
| |Warren County|     0|  0.000|  0.000|   191| 11339.349| 59.368|  16,844|
| |Wabash County|     0|  0.000|  0.000|    40|  3472.222| 86.806|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    21|  4241.567| 288.542|   4,951|
| |Richland County|     0|  0.000|  0.000|    20|  1289.241| 55.253|  15,513|
| |Putnam County|     0|  0.000|  0.000|    14|  2439.449| 124.462|   5,739|
| |Fulton County|     0|  0.000|  0.000|    35|  1019.220| 29.121|  34,340|
| |Edwards County|     0|  0.000|  0.000|    20|  3127.443| 134.033|   6,395|
| |Edgar County|     0|  0.000|  0.000|    29|  1689.878| 24.974|  17,161|
| |De Witt County|     0|  0.000|  0.000|    34|  2174.191| 27.406|  15,638|
| |Crawford County|     0|  0.000|  0.000|    30|  1607.114|  7.653|  18,667|
| |Clay County|     0|  0.000|  0.000|    26|  1972.087| 119.192|  13,184|
| |Greene County|     0|  0.000|  0.000|    59|  4549.310| 418.581|  12,969|
| |Calhoun County|     0|  0.000|  0.000|     9|  1899.135| 30.145|   4,739|
| |Hamilton County|     0|  0.000|  0.000|    29|  3573.189| 105.611|   8,116|
| |Henderson County|     0|  0.000|  0.000|    13|  1956.064| 85.981|   6,646|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Brown County|     0|  0.000|  0.000|    15|  2280.328| 43.435|   6,578|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 37.387|   3,821|
| |Massac County|     0|  0.000|  0.000|    41|  2977.055| 72.611|  13,772|
| |Mason County|     0|  0.000|  0.000|    56|  4191.931| 139.018|  13,359|
| |Marshall County|     0|  0.000|  0.000|    28|  2447.980| 74.938|  11,438|
| |Marion County|     0|  0.000|  0.000|   165|  4434.888| 95.993|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    51|  3252.966| 72.896|  15,678|
| |Johnson County|     0|  0.000|  0.000|    71|  5717.967| 138.060|  12,417|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,343| 573.583| N/A|125,016|  9765.358| N/A|12,801,989|
| |Philadelphia County| 1,700| 1073.189| N/A|31,584| 19938.588| N/A|1,584,064|
| |Montgomery County|   858| 1032.597|  1.203|10,187| 12259.978| 47.968| 830,915|
| |Delaware County|   701| 1236.883|  2.017| 9,347| 16492.368| 98.557| 566,747|
| |Bucks County|   582| 926.353|  0.455| 7,231| 11509.383| 39.792| 628,270|
| |Lancaster County|   414| 758.625|  1.571| 5,999| 10992.736| 76.962| 545,724|
| |Berks County|   369| 876.143|  0.678| 5,431| 12895.214| 62.073| 421,164|
| |Chester County|   349| 664.776|  0.272| 5,194|  9893.541| 48.981| 524,989|
| |Lehigh County|   338| 915.200|  1.160| 4,992| 13516.807| 46.804| 369,318|
| |Northampton County|   292| 956.483|  0.936| 3,944| 12919.076| 30.884| 305,285|
| |Allegheny County|   254| 208.874|  1.997| 9,008|  7407.621| 66.492|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,944|  9271.536| 27.935| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,477| 10954.045| 56.258| 317,417|
| |Dauphin County|   159| 571.328|  1.540| 2,850| 10240.784| 75.972| 278,299|
| |Monroe County|   124| 728.251|  0.000| 1,642|  9643.451| 28.526| 170,271|
| |York County|    94| 209.327|  1.591| 2,637|  5872.293| 86.530| 449,058|
| |Beaver County|    92| 561.219|  2.614| 1,332|  8125.469| 61.873| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,311|  5174.251| 40.596| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,621| 11432.158| 40.300| 141,793|
| |Schuylkill County|    51| 360.784|  2.021|   922|  6522.400| 22.233| 141,359|
| |Westmoreland County|    47| 134.709|  0.409| 1,555|  4456.877| 37.260| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,375|  8869.423| 74.641| 155,027|
| |Columbia County|    35| 538.760|  0.000|   478|  7357.921| 30.786|  64,964|
| |Carbon County|    28| 436.259|  0.000|   372|  5796.018| 17.807|  64,182|
| |Susquehanna County|    27| 669.510|  0.000|   215|  5331.283| 10.627|  40,328|
| |Erie County|    21| 77.856|  2.119| 1,126|  4174.576| 53.493| 269,728|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  0.000|  55,809|
| |Adams County|    20| 194.158|  0.000|   531|  5154.889| 69.342| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   407|  3592.265| 81.958| 113,299|
| |Lawrence County|    16| 187.108|  6.682|   392|  4584.152| 65.154|  85,512|
| |Butler County|    15| 79.850|  0.000|   677|  3603.882| 47.149| 187,853|
| |Washington County|    13| 62.843|  1.381|   862|  4166.969| 61.462| 206,865|
| |Northumberland County|    13| 143.104|  3.145|   507|  5581.057| 143.104|  90,843|
| |Mercer County|    11| 100.526|  2.611|   446|  4075.888| 107.054| 109,424|
| |Centre County|    10| 61.582|  0.000|   373|  2297.010| 12.316| 162,385|
| |Wayne County|    10| 194.700|  5.563|   162|  3154.144| 13.907|  51,361|
| |Armstrong County|     8| 123.581|  4.414|   222|  3429.366| 66.204|  64,735|
| |Wyoming County|     8| 298.574|  0.000|    61|  2276.629| 15.995|  26,794|
| |Indiana County|     7| 83.261|  1.699|   326|  3877.583| 79.863|  84,073|
| |Juniata County|     6| 242.297|  0.000|   133|  5370.916| 28.845|  24,763|
| |Fayette County|     6| 46.413|  2.210|   562|  4347.355| 153.605| 129,274|
| |Blair County|     6| 49.249|  3.518|   298|  2446.051| 70.356| 121,829|
| |Clinton County|     5| 129.426|  0.000|   123|  3183.889| 29.583|  38,632|
| |Perry County|     5| 108.057|  0.000|   124|  2679.806| 12.349|  46,272|
| |Huntingdon County|     4| 88.605|  0.000|   310|  6866.915| 63.290|  45,144|
| |Bedford County|     4| 83.528|  0.000|   143|  2986.134| 29.832|  47,888|
| |Montour County|     3| 164.564|  0.000|   104|  5704.882| 78.364|  18,230|
| |Somerset County|     3| 40.846|  0.000|   136|  1851.675| 15.560|  73,447|
| |Tioga County|     3| 73.908|  0.000|    38|   936.168|  7.039|  40,591|
| |Bradford County|     3| 49.732|  0.000|    90|  1491.968| 14.209|  60,323|
| |Cambria County|     3| 23.043|  0.000|   349|  2680.656| 73.518| 130,192|
| |Clarion County|     2| 52.032|  0.000|    81|  2107.290| 14.866|  38,438|
| |Elk County|     2| 66.867|  0.000|    50|  1671.682| 19.105|  29,910|
| |Fulton County|     2| 137.646|  0.000|    27|  1858.224| 19.664|  14,530|
| |Union County|     2| 44.521|  0.000|   262|  5832.202| 225.783|  44,923|
| |Snyder County|     2| 49.539|  0.000|   109|  2699.891| 31.847|  40,372|
| |Crawford County|     1| 11.816|  0.000|   158|  1866.972| 42.201|  84,629|
| |Clearfield County|     1| 12.618|  1.803|   174|  2195.445| 57.680|  79,255|
| |Greene County|     1| 27.599|  0.000|   117|  3229.101| 27.599|  36,233|
| |Jefferson County|     1| 23.028|  0.000|    73|  1681.059| 42.767|  43,425|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  3.516|  40,625|
| |Warren County|     1| 25.516|  0.000|    23|   586.869| 10.935|  39,191|
| |Mifflin County|     1| 21.674|  0.000|   120|  2600.893| 27.867|  46,138|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Venango County|     0|  0.000|  0.000|    65|  1282.861|  8.458|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Forest County|     0|  0.000|  0.000|    10|  1379.881| 19.713|   7,247|
| |Cameron County|     0|  0.000|  0.000|     7|  1574.095| 32.124|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,457| 646.550| N/A|93,329|  9345.182| N/A|9,986,857|
| |Wayne County| 2,828| 1616.607|  1.552|28,423| 16247.814| 70.149|1,749,343|
| |Oakland County| 1,131| 899.344|  0.568|15,751| 12524.809| 90.991|1,257,584|
| |Macomb County|   948| 1084.703|  1.798|10,676| 12215.494| 137.631| 873,972|
| |Genesee County|   297| 731.864|  0.704| 3,674|  9053.431| 40.835| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,600| 11568.524| 66.541| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,054| 10779.945| 128.208| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,582|  7023.920| 54.407| 367,601|
| |Kalamazoo County|    83| 313.130|  0.539| 1,655|  6243.728| 46.889| 265,066|
| |Berrien County|    67| 436.764|  1.863| 1,381|  9002.549| 76.364| 153,401|
| |Muskegon County|    59| 339.928|  0.823| 1,187|  6838.897| 46.092| 173,566|
| |Ottawa County|    56| 191.893|  0.979| 1,852|  6346.160| 50.421| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   826|  5190.790| 38.603| 159,128|
| |Calhoun County|    42| 313.061|  1.065|   802|  5977.981| 51.112| 134,159|
| |Jackson County|    34| 214.498|  0.901|   713|  4498.139| 16.223| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   471|  5376.283| 68.488|  87,607|
| |Bay County|    31| 300.603|  0.000|   650|  6302.969| 126.059| 103,126|
| |Ingham County|    31| 106.017|  0.489| 1,558|  5328.208| 28.336| 292,406|
| |Tuscola County|    29| 555.077|  0.000|   356|  6814.049| 92.969|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   350|  5137.841| 37.747|  68,122|
| |Livingston County|    28| 145.837|  0.000|   842|  4385.531| 34.971| 191,995|
| |Hillsdale County|    25| 548.186|  0.000|   272|  5964.258| 59.517|  45,605|
| |Monroe County|    24| 159.468|  1.898| 1,005|  6677.741| 80.683| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   157|  3856.452| 38.600|  40,711|
| |Cass County|    14| 270.338|  8.276|   336|  6488.115| 113.101|  51,787|
| |Clinton County|    13| 163.327|  0.000|   425|  5339.531| 16.153|  79,595|
| |Alpena County|    13| 457.666|  0.000|   130|  4576.659| 25.146|  28,405|
| |Lenawee County|    12| 121.888|  0.000|   436|  4428.599| 46.434|  98,451|
| |Iosco County|    12| 477.574|  0.000|   134|  5332.909| 28.427|  25,127|
| |Otsego County|    11| 445.922|  5.791|   135|  5472.677| 23.165|  24,668|
| |Marquette County|    11| 164.920|  0.000|   173|  2593.742| 62.113|  66,699|
| |Midland County|    10| 120.256|  0.000|   342|  4112.752| 49.820|  83,156|
| |Van Buren County|    10| 132.141|  0.000|   457|  6038.823| 73.621|  75,677|
| |Isabella County|     9| 128.807|  0.000|   209|  2991.184| 14.312|  69,872|
| |St. Joseph County|     9| 147.628|  2.343|   600|  9841.874| 86.702|  60,964|
| |Eaton County|     8| 72.551|  0.000|   463|  4198.861| 23.320| 110,268|
| |Ionia County|     7| 108.197|  4.416|   274|  4235.127| 11.040|  64,697|
| |Allegan County|     6| 50.813|  0.000|   532|  4505.382| 32.665| 118,081|
| |Oceana County|     6| 226.697|  0.000|   479| 18098.009| 70.168|  26,467|
| |Sanilac County|     6| 145.737|  0.000|   110|  2671.848| 38.169|  41,170|
| |Crawford County|     5| 356.405|  0.000|   107|  7627.058| 71.281|  14,029|
| |Grand Traverse County|     5| 53.713|  0.000|   217|  2331.128| 23.020|  93,088|
| |Huron County|     4| 129.111|  0.000|   159|  5132.178| 46.111|  30,981|
| |Wexford County|     4| 118.938|  0.000|    69|  2051.679|  8.496|  33,631|
| |Kalkaska County|     4| 221.754|  0.000|    54|  2993.680| 47.519|  18,038|
| |Ogemaw County|     3| 142.878|  6.804|    54|  2571.796|  6.804|  20,997|
| |Delta County|     3| 83.836|  0.000|   101|  2822.490| 71.860|  35,784|
| |Arenac County|     3| 201.572|  0.000|    43|  2889.202| 19.197|  14,883|
| |Clare County|     3| 96.931|  0.000|    74|  2390.953| 46.157|  30,950|
| |Gladwin County|     2| 78.589|  0.000|    59|  2318.362| 22.454|  25,449|
| |Dickinson County|     2| 79.242|  0.000|    58|  2298.031| 62.262|  25,239|
| |Charlevoix County|     2| 76.502|  0.000|    49|  1874.307| 21.858|  26,143|
| |Cheboygan County|     2| 79.126|  0.000|    50|  1978.161| 62.171|  25,276|
| |Branch County|     2| 45.959|  0.000|   366|  8410.506| 85.353|  43,517|
| |Emmet County|     2| 59.853|  0.000|    64|  1915.307| 21.376|  33,415|
| |Mecosta County|     2| 46.027|  0.000|    69|  1587.923| 32.876|  43,453|
| |Barry County|     2| 32.494|  0.000|   194|  3151.909| 62.667|  61,550|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  9.449|  15,118|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Roscommon County|     1| 41.634|  5.948|    54|  2248.220| 35.686|  24,019|
| |Presque Isle County|     1| 79.416|  0.000|    20|  1588.310| 22.690|  12,592|
| |Montmorency County|     1| 107.204| 15.315|     9|   964.837| 15.315|   9,328|
| |Gogebic County|     1| 71.556|  0.000|   125|  8944.544| 194.224|  13,975|
| |Iron County|     1| 90.367|  0.000|    20|  1807.338| 38.729|  11,066|
| |Montcalm County|     1| 15.652|  0.000|   195|  3052.216| 31.305|  63,888|
| |Benzie County|     1| 56.287|  0.000|    30|  1688.619| 16.082|  17,766|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Chippewa County|     0|  0.000|  0.000|    42|  1124.528| 26.774|  37,349|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846| 12.250|  23,324|
| |Alger County|     0|  0.000|  0.000|    12|  1317.523| 62.739|   9,108|
| |Leelanau County|     0|  0.000|  0.000|    75|  3446.533| 59.083|  21,761|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128| 17.650|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Ontonagon County|     0|  0.000|  0.000|    16|  2797.203| 224.775|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   251|  5124.541| 11.667|  48,980|
| |Menominee County|     0|  0.000|  0.000|   147|  6453.029| 244.575|  22,780|
| |Mason County|     0|  0.000|  0.000|   103|  3534.175| 24.509|  29,144|
| |Manistee County|     0|  0.000|  0.000|    40|  1628.797| 34.903|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    26|  2407.630| 39.686|  10,799|
| |Luce County|     0|  0.000|  0.000|     3|   481.618|  0.000|   6,229|
| |Lake County|     0|  0.000|  0.000|    25|  2109.171| 84.367|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    50|  1401.188|  8.007|  35,684|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,444| 1246.463| N/A|50,441| 14147.809| N/A|3,565,287|
| |Hartford County| 1,415| 1586.821|  0.481|12,826| 14383.439| 18.423| 891,720|
| |Fairfield County| 1,409| 1493.642|  0.151|18,081| 19167.165| 31.045| 943,332|
| |New Haven County| 1,106| 1293.935|  0.334|13,240| 15489.782| 23.398| 854,757|
| |Middlesex County|   192| 1182.004|  0.879| 1,408|  8668.029| 14.951| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,618|  8972.290| 14.259| 180,333|
| |New London County|   103| 388.377|  0.000| 1,467|  5531.549| 24.779| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,056|  7006.323|  2.843| 150,721|
| |Windham County|    15| 128.444|  0.000|   745|  6379.408| 35.475| 116,782|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,243| 399.626| N/A|203,255| 19143.534| N/A|10,617,423|
| |Fulton County|   445| 418.258|  5.237|20,874| 19619.583| 309.900|1,063,937|
| |Cobb County|   323| 424.921|  3.571|14,006| 18425.529| 351.626| 760,141|
| |Gwinnett County|   272| 290.521|  4.883|20,382| 21769.826| 332.787| 936,250|
| |DeKalb County|   242| 318.716|  2.446|14,292| 18822.674| 288.237| 759,297|
| |Dougherty County|   172| 1955.523|  4.873| 2,754| 31311.110| 199.775|  87,956|
| |Clayton County|   111| 379.804|  4.399| 5,154| 17635.224| 258.091| 292,256|
| |Muscogee County|   102| 521.022| 13.865| 4,826| 24651.503| 318.159| 195,769|
| |Hall County|    99| 484.247|  9.084| 6,206| 30355.946| 383.624| 204,441|
| |Richmond County|    94| 464.156|  7.054| 4,509| 22264.688| 471.916| 202,518|
| |Chatham County|    76| 262.585|  4.936| 5,914| 20433.265| 347.481| 289,430|
| |Troup County|    72| 1029.719| 16.345| 2,312| 33065.416| 243.128|  69,922|
| |Bibb County|    71| 463.571|  8.395| 3,715| 24255.839| 419.732| 153,159|
| |Bartow County|    64| 594.034|  3.978| 1,914| 17765.320| 316.906| 107,738|
| |Cherokee County|    64| 247.321|  3.864| 3,609| 13946.586| 349.451| 258,773|
| |Houston County|    62| 392.746|  9.954| 2,023| 12814.909| 186.418| 157,863|
| |Sumter County|    56| 1896.762|  0.000|   775| 26249.831| 169.354|  29,524|
| |Douglas County|    54| 368.996|  3.905| 2,728| 18641.138| 320.187| 146,343|
| |Glynn County|    52| 609.670| 23.449| 2,593| 30401.444| 391.931|  85,292|
| |Carroll County|    51| 425.028|  4.762| 1,905| 15876.058| 172.631| 119,992|
| |Habersham County|    50| 1103.071|  6.303| 1,157| 25525.062| 315.163|  45,328|
| |Henry County|    49| 208.901|  3.045| 3,457| 14738.170| 244.834| 234,561|
| |Upson County|    46| 1747.720|  0.000|   567| 21542.553| 423.361|  26,320|
| |Lowndes County|    45| 383.285| 13.385| 3,229| 27502.853| 270.125| 117,406|
| |Thomas County|    43| 967.357|  9.641| 1,135| 25533.734| 366.375|  44,451|
| |Mitchell County|    41| 1875.314|  0.000|   657| 30050.771| 169.889|  21,863|
| |Spalding County|    41| 614.665|  2.142|   967| 14497.099| 194.894|  66,703|
| |Baldwin County|    41| 913.344|  9.547| 1,070| 23836.044| 292.779|  44,890|
| |Tift County|    40| 984.155| 17.574| 1,363| 33535.085| 347.969|  40,644|
| |Newton County|    40| 357.961|  5.114| 1,865| 16689.934| 281.255| 111,744|
| |Walton County|    39| 412.293|  6.041| 1,153| 12189.063| 258.249|  94,593|
| |Butts County|    38| 1523.901|  5.729|   494| 19810.715| 148.953|  24,936|
| |Hancock County|    35| 4138.583| 16.892|   324| 38311.458| 574.334|   8,457|
| |Barrow County|    32| 384.431|  0.000| 1,323| 15893.801| 293.472|  83,240|
| |Early County|    32| 3140.334| 14.019|   368| 36113.837| 266.368|  10,190|
| |Whitfield County|    32| 305.845|  6.827| 3,575| 34168.674| 413.711| 104,628|
| |Terrell County|    30| 3516.587|  0.000|   301| 35283.085| 133.965|   8,531|
| |Fayette County|    30| 262.190|  6.243| 1,159| 10129.259| 206.006| 114,421|
| |Coffee County|    30| 693.273| 16.506| 1,497| 34594.320| 419.265|  43,273|
| |Ware County|    29| 811.552| 19.989| 1,170| 32741.926| 343.810|  35,734|
| |Monroe County|    27| 979.041| 20.720|   467| 16933.788| 176.124|  27,578|
| |Randolph County|    26| 3835.940|  0.000|   273| 40277.368| 252.919|   6,778|
| |Columbia County|    25| 159.526|  3.646| 2,346| 14969.945| 308.114| 156,714|
| |Forsyth County|    24| 98.259|  1.170| 2,357|  9649.870| 218.159| 244,252|
| |Colquitt County|    24| 526.316|  6.266| 1,565| 34320.175| 194.236|  45,600|
| |Jenkins County|    24| 2766.252| 32.932|   249| 28699.862| 296.384|   8,676|
| |Worth County|    23| 1135.971|  0.000|   450| 22225.515| 148.170|  20,247|
| |Paulding County|    23| 136.363|  3.388| 1,744| 10339.901| 210.897| 168,667|
| |Gordon County|    23| 396.805|  0.000| 1,225| 21134.172| 458.421|  57,963|
| |Coweta County|    22| 148.139|  0.000| 1,539| 10363.008| 159.682| 148,509|
| |Lee County|    22| 733.529|  0.000|   551| 18371.566| 138.132|  29,992|
| |Wilcox County|    19| 2200.347| 16.544|   186| 21540.243| 281.247|   8,635|
| |Clarke County|    19| 148.055|  2.226| 2,117| 16496.404| 359.561| 128,331|
| |Appling County|    19| 1033.395| 15.540|   689| 37474.165| 683.750|  18,386|
| |Putnam County|    18| 813.780|  6.459|   437| 19756.770| 342.304|  22,119|
| |Brooks County|    18| 1164.521|  9.242|   416| 26913.373| 378.931|  15,457|
| |Rockdale County|    18| 198.029|  3.143| 1,371| 15083.172| 271.896|  90,896|
| |Floyd County|    18| 182.745|  4.351| 1,580| 16040.935| 395.947|  98,498|
| |Turner County|    18| 2254.227|  0.000|   251| 31433.939| 304.142|   7,985|
| |Walker County|    17| 243.689|  2.048|   723| 10363.957| 290.789|  69,761|
| |Jackson County|    17| 232.950|  7.830| 1,098| 15045.836| 246.653|  72,977|
| |Harris County|    17| 482.461|  4.054|   659| 18702.463| 133.792|  35,236|
| |Crisp County|    15| 670.481|  6.386|   391| 17477.204| 172.409|  22,372|
| |Oconee County|    15| 372.393|  0.000|   450| 11171.797| 173.784|  40,280|
| |Laurens County|    14| 294.452| 27.041|   993| 20885.038| 658.009|  47,546|
| |Peach County|    14| 508.241| 10.372|   394| 14303.347| 300.796|  27,546|
| |Dooly County|    14| 1045.556|  0.000|   258| 19268.111| 170.703|  13,390|
| |Decatur County|    14| 530.223| 32.463|   809| 30639.297| 638.431|  26,404|
| |Bulloch County|    14| 175.862|  1.795| 1,310| 16455.633| 335.573|  79,608|
| |Stephens County|    13| 501.446| 16.531|   655| 25265.188| 490.426|  25,925|
| |Greene County|    12| 654.879|  7.796|   325| 17736.302| 491.159|  18,324|
| |Lamar County|    12| 629.030| 14.977|   280| 14677.360| 307.026|  19,077|
| |Emanuel County|    11| 485.737| 18.925|   534| 23580.323| 567.745|  22,646|
| |Johnson County|    11| 1140.724|  0.000|   248| 25718.138| 237.034|   9,643|
| |Wilkinson County|    11| 1228.501| 15.955|   220| 24570.025| 510.546|   8,954|
| |Wayne County|    11| 367.561| 28.641|   790| 26397.567| 534.634|  29,927|
| |Polk County|    11| 258.137|  6.705|   837| 19641.893| 492.807|  42,613|
| |Catoosa County|    10| 147.973|  2.114|   660|  9766.203| 186.023|  67,580|
| |McDuffie County|    10| 469.219|  0.000|   365| 17126.502| 429.000|  21,312|
| |Macon County|    10| 772.380|  0.000|   180| 13902.835| 66.204|  12,947|
| |Bleckley County|    10| 776.820| 55.487|   252| 19575.856| 1131.937|  12,873|
| |Telfair County|    10| 630.517| 27.022|   289| 18221.942| 297.244|  15,860|
| |Toombs County|     9| 335.445| 10.649|   783| 29183.750| 617.645|  26,830|
| |Pierce County|     9| 462.368| 22.018|   413| 21217.570| 227.515|  19,465|
| |Screven County|     9| 644.422|  0.000|   215| 15394.530| 378.470|  13,966|
| |Jeff Davis County|     8| 529.276|  9.451|   466| 30830.301| 585.984|  15,115|
| |Bacon County|     8| 716.589| 25.592|   438| 39233.250| 243.128|  11,164|
| |Jefferson County|     8| 520.766|  9.299|   517| 33654.472| 548.664|  15,362|
| |Bryan County|     8| 201.883|  0.000|   677| 17084.311| 353.294|  39,627|
| |Oglethorpe County|     7| 458.746|  0.000|   226| 14810.931| 337.038|  15,259|
| |Union County|     7| 285.586|  5.828|   285| 11627.433| 291.414|  24,511|
| |Stewart County|     7| 1057.242| 43.153|   256| 38664.854| 107.882|   6,621|
| |Burke County|     7| 312.737|  0.000|   481| 21489.523| 363.797|  22,383|
| |Hart County|     7| 267.125| 16.355|   322| 12287.731| 272.576|  26,205|
| |Madison County|     6| 200.803|  9.562|   417| 13955.823| 291.643|  29,880|
| |Cook County|     6| 347.423|  0.000|   445| 25767.226| 297.791|  17,270|
| |Brantley County|     6| 313.988| 14.952|   255| 13344.497| 171.946|  19,109|
| |Meriwether County|     6| 283.460|  0.000|   403| 19039.070| 303.707|  21,167|
| |Calhoun County|     6| 969.462|  0.000|   207| 33446.437| 276.989|   6,189|
| |Lumpkin County|     6| 178.518|  0.000|   357| 10621.839| 204.021|  33,610|
| |Grady County|     6| 243.576|  5.799|   503| 20419.762| 452.355|  24,633|
| |Candler County|     6| 555.401| 26.448|   267| 24715.357| 462.834|  10,803|
| |Haralson County|     6| 201.396|  0.000|   230|  7720.193| 148.650|  29,792|
| |Franklin County|     6| 256.970|  6.118|   416| 17816.609| 214.142|  23,349|
| |Heard County|     5| 419.358| 11.982|   147| 12329.112| 155.761|  11,923|
| |Pike County|     5| 263.685|  7.534|   224| 11813.100| 210.948|  18,962|
| |White County|     5| 162.348|  0.000|   359| 11656.601| 236.565|  30,798|
| |Marion County|     5| 598.158| 17.090|   152| 18183.993| 119.632|   8,359|
| |Camden County|     5| 91.465|  2.613|   780| 14268.467| 219.515|  54,666|
| |Pickens County|     5| 153.417|  0.000|   410| 12580.160| 390.116|  32,591|
| |Banks County|     4| 207.965|  7.427|   275| 14297.598| 215.392|  19,234|
| |Gilmer County|     4| 127.514|  0.000|   635| 20242.915| 496.395|  31,369|
| |Twiggs County|     4| 492.611| 17.593|   122| 15024.631| 457.424|   8,120|
| |Seminole County|     4| 494.438| 35.317|   212| 26205.192| 882.924|   8,090|
| |Lincoln County|     4| 504.987|  0.000|   150| 18937.003| 378.740|   7,921|
| |Chattooga County|     4| 161.362| 11.526|   280| 11295.333| 466.797|  24,789|
| |Lanier County|     4| 383.767|  0.000|   221| 21203.109| 150.765|  10,423|
| |Ben Hill County|     4| 239.521|  8.554|   464| 27784.431| 881.095|  16,700|
| |Liberty County|     4| 65.109|  4.651|   766| 12468.463| 286.017|  61,435|
| |Clinch County|     4| 604.412|  0.000|   200| 30220.610| 518.068|   6,618|
| |Baker County|     3| 987.492|  0.000|    65| 21395.655| 141.070|   3,038|
| |Atkinson County|     3| 367.422| 17.496|   324| 39681.568| 402.414|   8,165|
| |Fannin County|     3| 114.556|  0.000|   349| 13326.715| 321.849|  26,188|
| |Treutlen County|     3| 434.720|  0.000|   130| 18837.850| 600.327|   6,901|
| |Rabun County|     3| 175.060|  0.000|   227| 13246.192| 241.749|  17,137|
| |Dawson County|     3| 114.907|  0.000|   401| 15359.277| 454.157|  26,108|
| |Charlton County|     3| 224.014|  0.000|   438| 32706.093| 501.365|  13,392|
| |Effingham County|     3| 46.659|  4.444|   758| 11789.225| 224.409|  64,296|
| |Evans County|     3| 281.584| 26.818|   270| 25342.594| 563.169|  10,654|
| |Dodge County|     3| 145.596|  0.000|   236| 11453.531| 325.857|  20,605|
| |Wilkes County|     3| 306.843|  0.000|   193| 19740.207| 189.950|   9,777|
| |Talbot County|     3| 484.262|  0.000|   140| 22598.870| 253.661|   6,195|
| |Jones County|     3| 104.402|  0.000|   322| 11205.847| 233.662|  28,735|
| |Clay County|     2| 705.716|  0.000|    91| 32110.092| 302.450|   2,834|
| |Pulaski County|     2| 179.582|  0.000|   127| 11403.430| 513.090|  11,137|
| |Echols County|     2| 499.251|  0.000|   225| 56165.751| 356.608|   4,006|
| |Chattahoochee County|     2| 183.368| 13.098|   767| 70321.812| 1335.970|  10,907|
| |Webster County|     2| 767.165|  0.000|    40| 15343.306| 54.798|   2,607|
| |Washington County|     2| 98.164|  0.000|   486| 23853.931| 357.599|  20,374|
| |Taylor County|     2| 249.377|  0.000|    93| 11596.010| 338.440|   8,020|
| |Murray County|     2| 49.880|  0.000|   609| 15188.547| 213.773|  40,096|
| |Montgomery County|     2| 218.055| 15.575|   157| 17117.314| 342.658|   9,172|
| |McIntosh County|     2| 139.101|  0.000|   190| 13214.633| 288.139|  14,378|
| |Quitman County|     1| 434.972|  0.000|    31| 13484.124| 124.278|   2,299|
| |Dade County|     1| 62.050|  0.000|   129|  8004.468| 132.965|  16,116|
| |Schley County|     1| 190.223|  0.000|    69| 13125.357| 380.445|   5,257|
| |Glascock County|     1| 336.587| 48.084|    25|  8414.675| 96.168|   2,971|
| |Elbert County|     1| 52.100|  0.000|   366| 19068.459| 297.712|  19,194|
| |Irwin County|     1| 106.202|  0.000|   168| 17841.971| 166.889|   9,416|
| |Jasper County|     1| 70.328|  0.000|   168| 11815.177| 391.830|  14,219|
| |Long County|     1| 51.127|  0.000|   132|  6748.811| 43.823|  19,559|
| |Wheeler County|     1| 127.307|  0.000|    95| 12094.208| 200.055|   7,855|
| |Warren County|     1| 190.331|  0.000|    80| 15226.494| 652.564|   5,254|
| |Towns County|     1| 83.077|  0.000|   151| 12544.654| 367.913|  12,037|
| |Tattnall County|     1| 39.548|  0.000|   520| 20564.739| 491.520|  25,286|
| |Taliaferro County|     0|  0.000|  0.000|    13|  8458.035| 92.945|   1,537|
| |Morgan County|     0|  0.000|  0.000|   283| 14681.469| 385.379|  19,276|
| |Miller County|     0|  0.000|  0.000|   146| 25533.403| 374.756|   5,718|
| |Crawford County|     0|  0.000|  0.000|   106|  8545.630| 184.272|  12,404|
| |Berrien County|     0|  0.000|  0.000|   304| 15672.527| 287.231|  19,397|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,198| 576.750| N/A|188,736| 25929.845| N/A|7,278,717|
| |Maricopa County| 2,382| 531.055|  7.293|126,791| 28267.402| 159.310|4,485,414|
| |Pima County|   501| 478.383|  4.911|18,381| 17551.197| 214.433|1,047,279|
| |Yuma County|   285| 1333.103| 12.028|11,633| 54413.973| 277.980| 213,787|
| |Navajo County|   202| 1821.067| 12.879| 5,391| 48600.844| 115.909| 110,924|
| |Mohave County|   171| 805.916|  9.426| 3,226| 15204.000| 119.844| 212,181|
| |Pinal County|   156| 337.087|  4.322| 8,509| 18386.349| 63.281| 462,789|
| |Apache County|   139| 1933.590|  5.962| 3,197| 44472.575| 196.737|  71,887|
| |Coconino County|   117| 815.467|  0.000| 3,128| 21801.556| 114.504| 143,476|
| |Yavapai County|    68| 289.240|  2.431| 2,040|  8677.196| 95.401| 235,099|
| |Cochise County|    54| 428.837|  4.538| 1,730| 13738.664| 199.670| 125,922|
| |Santa Cruz County|    53| 1139.834|  9.217| 2,669| 57400.318| 156.689|  46,498|
| |Gila County|    40| 740.494| 29.091|   950| 17586.730| 275.041|  54,018|
| |Graham County|    17| 437.727| 22.070|   555| 14290.496| 231.738|  38,837|
| |La Paz County|    12| 568.505| 13.536|   479| 22692.818| 20.304|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,195| 902.385| N/A|132,870| 28581.606| N/A|4,648,794|
| |Orleans Parish|   562| 1440.494|  0.732|10,805| 27694.902| 116.441| 390,144|
| |Jefferson Parish|   529| 1223.141|  3.633|15,452| 35727.746| 217.014| 432,493|
| |East Baton Rouge Parish|   354| 804.438|  8.116|12,377| 28125.774| 302.881| 440,059|
| |Caddo Parish|   296| 1232.286|  6.542| 6,739| 28055.320| 246.814| 240,204|
| |St. Tammany Parish|   215| 825.593|  4.937| 5,323| 20440.137| 240.821| 260,419|
| |Calcasieu Parish|   146| 717.670| 13.342| 6,862| 33730.510| 188.195| 203,436|
| |Rapides Parish|   114| 879.304|  7.713| 3,327| 25661.792| 221.479| 129,648|
| |Ouachita Parish|   114| 743.742|  6.524| 4,923| 32117.903| 308.494| 153,279|
| |Lafourche Parish|    99| 1014.199|  4.390| 2,863| 29329.809| 302.942|  97,614|
| |Lafayette Parish|    96| 392.815|  4.092| 7,723| 31601.129| 258.954| 244,390|
| |St. John the Baptist Parish|    92| 2147.676| 13.340| 1,434| 33475.734| 200.094|  42,837|
| |St. Landry Parish|    91| 1108.080| 22.614| 2,778| 33826.896| 431.403|  82,124|
| |Terrebonne Parish|    85| 769.502|  6.466| 3,072| 27810.721| 266.416| 110,461|
| |Acadia Parish|    85| 1369.973| 18.420| 2,634| 42453.058| 278.600|  62,045|
| |Bossier Parish|    82| 645.471| 10.121| 2,374| 18687.175| 204.662| 127,039|
| |Tangipahoa Parish|    78| 578.815| 15.902| 3,540| 26269.312| 336.052| 134,758|
| |Ascension Parish|    77| 608.196|  6.770| 2,930| 23143.029| 280.966| 126,604|
| |Iberia Parish|    73| 1045.396| 14.320| 2,561| 36674.782| 313.005|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,293| 27990.648| 253.589|  46,194|
| |St. Mary Parish|    55| 1114.534| 17.369| 1,631| 33050.985| 367.651|  49,348|
| |St. Charles Parish|    52| 979.284|  5.381| 1,492| 28097.928| 255.582|  53,100|
| |Livingston Parish|    52| 369.347|  3.044| 2,975| 21130.912| 260.775| 140,789|
| |Iberville Parish|    49| 1507.182|  8.788| 1,259| 38725.354| 391.076|  32,511|
| |St. Martin Parish|    46| 860.923| 10.695| 1,734| 32453.070| 411.746|  53,431|
| |East Feliciana Parish|    38| 1985.890| 22.397|   603| 31512.934| 530.068|  19,135|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   727| 27470.244| 280.694|  26,465|
| |Union Parish|    35| 1583.137| 12.924|   711| 32160.304| 420.016|  22,108|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   810| 37275.656| 414.174|  21,730|
| |Avoyelles Parish|    32| 797.130| 17.793| 1,096| 27301.714| 409.241|  40,144|
| |St. James Parish|    32| 1516.875|  0.000|   722| 34224.498| 372.447|  21,096|
| |Lincoln Parish|    31| 663.215| 21.394|   806| 17243.592| 223.109|  46,742|
| |Bienville Parish|    30| 2265.690|  0.000|   386| 29151.877| 345.248|  13,241|
| |Allen Parish|    30| 1170.640| 27.872| 1,284| 50103.407| 412.511|  25,627|
| |Vernon Parish|    29| 611.440| 21.084|   772| 16276.961| 120.481|  47,429|
| |Jefferson Davis Parish|    28| 892.629| 18.217| 1,033| 32931.650| 268.700|  31,368|
| |Vermilion Parish|    27| 453.698| 19.204| 1,611| 27070.626| 345.674|  59,511|
| |De Soto Parish|    26| 946.728| 10.404|   743| 27054.583| 353.723|  27,463|
| |St. Bernard Parish|    24| 508.001|  3.024| 1,113| 23558.547| 166.310|  47,244|
| |Assumption Parish|    20| 913.617|  0.000|   591| 26997.396| 221.879|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   461| 19873.259| 203.228|  23,197|
| |Beauregard Parish|    19| 506.707|  7.620|   837| 22321.786| 152.393|  37,497|
| |Franklin Parish|    19| 949.288| 14.275|   940| 46964.776| 642.375|  20,015|
| |Jackson Parish|    18| 1143.293|  0.000|   378| 24009.146| 154.254|  15,744|
| |Grant Parish|    18| 803.966| 44.665|   307| 13712.091| 146.756|  22,389|
| |Natchitoches Parish|    17| 445.516|  0.000|   791| 20729.598| 280.787|  38,158|
| |West Feliciana Parish|    17| 1091.984|  9.176|   355| 22803.186| 247.761|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   898| 23422.014| 216.111|  38,340|
| |Morehouse Parish|    12| 482.431|  5.743|   536| 21548.605| 430.742|  24,874|
| |Red River Parish|    12| 1421.464| 16.922|   244| 28903.104| 879.954|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   282| 17996.171| 501.413|  15,670|
| |Sabine Parish|    11| 460.559|  5.981|   658| 27549.824| 436.634|  23,884|
| |Concordia Parish|     9| 467.314|  7.418|   337| 17498.312| 304.125|  19,259|
| |Richland Parish|     8| 397.575| 14.199|   604| 30016.897| 376.276|  20,122|
| |Winn Parish|     7| 503.452|  0.000|   426| 30638.665| 277.412|  13,904|
| |Evangeline Parish|     7| 209.612| 21.389|   908| 27189.699| 440.613|  33,395|
| |West Carroll Parish|     6| 554.017| 13.191|   296| 27331.487| 316.581|  10,830|
| |Madison Parish|     6| 547.895|  0.000|   618| 56433.202| 430.489|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   296| 31177.586| 436.366|   9,494|
| |Caldwell Parish|     3| 302.480| 14.404|   224| 22585.199| 316.884|   9,918|
| |St. Helena Parish|     2| 197.394| 14.100|   275| 27141.729| 394.789|  10,132|
| |LaSalle Parish|     2| 134.300|  0.000|   308| 20682.246| 575.573|  14,892|
| |East Carroll Parish|     2| 291.503| 20.822|   521| 75936.452| 229.038|   6,861|
| |Tensas Parish|     0|  0.000|  0.000|    91| 20996.770| 758.125|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   170| 24379.750| 61.462|   6,973|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,708| 317.219| N/A|102,826|  8796.742| N/A|11,689,100|
| |Franklin County|   529| 401.745|  1.519|18,697| 14199.290| 140.280|1,316,756|
| |Cuyahoga County|   505| 408.883|  2.660|13,734| 11119.999| 98.664|1,235,072|
| |Lucas County|   326| 761.063|  2.335| 5,448| 12718.631| 137.738| 428,348|
| |Hamilton County|   257| 314.383|  1.573| 9,766| 11946.572| 90.523| 817,473|
| |Mahoning County|   255| 1115.081|  1.249| 2,595| 11347.586| 98.702| 228,683|
| |Summit County|   223| 412.190|  1.584| 3,614|  6680.061| 72.879| 541,013|
| |Stark County|   140| 377.760|  1.156| 1,884|  5083.566| 65.915| 370,606|
| |Trumbull County|   108| 545.526|  2.165| 1,549|  7824.260| 70.716| 197,974|
| |Montgomery County|    96| 180.557|  4.299| 4,438|  8347.016| 92.966| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,813|  5851.539| 75.156| 309,833|
| |Butler County|    63| 164.433|  1.119| 2,976|  7767.517| 86.877| 383,134|
| |Portage County|    63| 387.773|  2.638|   771|  4745.608| 41.327| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,671| 16401.166| 123.391| 101,883|
| |Wayne County|    58| 501.253|  0.000|   545|  4710.051| 45.681| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,068|  8164.077| 124.492| 130,817|
| |Licking County|    51| 288.360|  5.654| 1,319|  7457.792| 130.045| 176,862|
| |Allen County|    46| 449.434|  5.583|   769|  7513.361| 142.367| 102,351|
| |Ashtabula County|    46| 473.051|  1.469|   576|  5923.427| 47.011|  97,241|
| |Marion County|    45| 691.319|  2.195| 2,935| 45089.334| 85.592|  65,093|
| |Geauga County|    44| 469.840|  0.000|   559|  5969.097| 36.611|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,391| 40901.859| 63.539|  58,457|
| |Lake County|    41| 178.145|  3.104| 1,131|  4914.208| 47.795| 230,149|
| |Miami County|    39| 364.530|  2.671|   858|  8019.666| 102.816| 106,987|
| |Warren County|    39| 166.239|  2.436| 1,821|  7762.082| 92.558| 234,602|
| |Medina County|    35| 194.719|  1.590|   945|  5257.419| 77.093| 179,746|
| |Fairfield County|    32| 203.079|  4.533| 1,416|  8986.254| 137.804| 157,574|
| |Darke County|    29| 567.370|  8.385|   406|  7943.185| 181.670|  51,113|
| |Erie County|    28| 377.023|  1.924|   597|  8038.672| 119.262|  74,266|
| |Ottawa County|    26| 641.579|  3.525|   396|  9771.746| 123.381|  40,525|
| |Belmont County|    26| 388.025|  0.000|   623|  9297.675| 70.356|  67,006|
| |Washington County|    22| 367.211|  0.000|   209|  3488.508| 26.229|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,344|  6425.181| 85.369| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    94|  6884.429| 31.388|  13,654|
| |Sandusky County|    17| 290.509|  0.000|   390|  6664.616| 114.739|  58,518|
| |Putnam County|    17| 502.053|  0.000|   211|  6231.358| 54.846|  33,861|
| |Clark County|    15| 111.871|  1.065| 1,178|  8785.603| 91.628| 134,083|
| |Tuscarawas County|    14| 152.195|  0.000|   793|  8620.783| 57.462|  91,987|
| |Mercer County|    13| 315.749|  0.000|   631| 15325.950| 333.097|  41,172|
| |Richland County|    12| 99.047|  0.000|   614|  5067.930| 79.002| 121,154|
| |Greene County|    12| 71.032|  0.846|   718|  4250.105| 70.187| 168,937|
| |Hardin County|    12| 382.592|  0.000|   170|  5420.054| 77.429|  31,365|
| |Clermont County|    11| 53.287|  0.000|   953|  4616.622| 65.052| 206,428|
| |Madison County|    10| 223.559|  0.000|   401|  8964.700| 207.590|  44,731|
| |Wyandot County|     9| 413.375| 13.123|   150|  6889.583| 164.038|  21,772|
| |Hocking County|     9| 318.426|  0.000|   118|  4174.922| 35.381|  28,264|
| |Guernsey County|     7| 180.064|  0.000|   119|  3061.093| 25.723|  38,875|
| |Knox County|     7| 112.320|  0.000|   212|  3401.688| 61.891|  62,322|
| |Coshocton County|     7| 191.257|  3.903|   196|  5355.191| 42.935|  36,600|
| |Auglaize County|     6| 131.418|  3.129|   263|  5760.470| 115.773|  45,656|
| |Clinton County|     6| 142.966|  0.000|   169|  4026.878| 54.463|  41,968|
| |Holmes County|     6| 136.488|  0.000|   328|  7461.328| 19.498|  43,960|
| |Huron County|     5| 85.813|  2.452|   404|  6933.718| 63.747|  58,266|
| |Carroll County|     5| 185.777|  0.000|   113|  4198.558| 15.924|  26,914|
| |Crawford County|     5| 120.499|  0.000|   175|  4217.477| 24.100|  41,494|
| |Shelby County|     4| 82.321|  0.000|   210|  4321.877| 135.242|  48,590|
| |Ross County|     4| 52.174|  0.000|   494|  6443.534| 139.753|  76,666|
| |Defiance County|     4| 105.023|  0.000|   150|  3938.352| 67.515|  38,087|
| |Hancock County|     3| 39.587|  1.885|   389|  5133.077| 105.565|  75,783|
| |Perry County|     3| 83.024|  0.000|   140|  3874.467| 122.560|  36,134|
| |Williams County|     3| 81.762|  0.000|   136|  3706.530| 46.721|  36,692|
| |Seneca County|     3| 54.369|  0.000|   228|  4132.082| 157.930|  55,178|
| |Jefferson County|     3| 45.924|  0.000|   237|  3628.014| 59.045|  65,325|
| |Ashland County|     3| 56.092|  0.000|   154|  2879.366| 56.092|  53,484|
| |Logan County|     2| 43.791|  0.000|   160|  3503.240| 93.837|  45,672|
| |Champaign County|     2| 51.434|  0.000|   181|  4654.751| 113.889|  38,885|
| |Adams County|     2| 72.207|  0.000|    61|  2202.325| 25.788|  27,698|
| |Athens County|     2| 30.615|  2.187|   360|  5510.738| 21.868|  65,327|
| |Vinton County|     2| 152.847|  0.000|    32|  2445.548| 21.835|  13,085|
| |Van Wert County|     2| 70.734|  5.052|    73|  2581.786| 15.157|  28,275|
| |Preble County|     2| 48.921|  0.000|   207|  5063.353| 122.303|  40,882|
| |Brown County|     2| 46.049|  3.289|   146|  3361.577| 92.098|  43,432|
| |Henry County|     2| 74.058|  5.290|   122|  4517.515| 74.058|  27,006|
| |Morrow County|     2| 56.612|  0.000|   176|  4981.884| 64.700|  35,328|
| |Muskingum County|     1| 11.599|  0.000|   243|  2818.535| 72.907|  86,215|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 47.492|  15,040|
| |Union County|     1| 16.953|  0.000|   260|  4407.676| 92.028|  58,988|
| |Highland County|     1| 23.169|  0.000|   166|  3846.065| 99.296|  43,161|
| |Scioto County|     1| 13.278|  0.000|   242|  3213.214| 81.563|  75,314|
| |Fulton County|     1| 23.738|  0.000|   153|  3631.961| 40.694|  42,126|
| |Gallia County|     1| 33.447|  0.000|    70|  2341.294| 57.338|  29,898|
| |Fayette County|     0|  0.000|  0.000|   121|  4241.893| 95.155|  28,525|
| |Lawrence County|     0|  0.000|  0.000|   300|  5045.154| 180.184|  59,463|
| |Meigs County|     0|  0.000|  0.000|    54|  2357.358| 174.619|  22,907|
| |Pike County|     0|  0.000|  0.000|    79|  2844.592| 46.295|  27,772|
| |Paulding County|     0|  0.000|  0.000|    70|  3748.929| 61.207|  18,672|
| |Noble County|     0|  0.000|  0.000|    16|  1109.262|  0.000|  14,424|
| |Morgan County|     0|  0.000|  0.000|    30|  2067.825| 98.468|  14,508|
| |Jackson County|     0|  0.000|  0.000|    76|  2344.738| 35.259|  32,413|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,585| 592.985| N/A|96,843| 16018.545| N/A|6,045,680|
| |Baltimore County|   997| 1205.023|  4.662|26,267| 31747.586| 327.717| 827,370|
| |Montgomery County|   803| 764.261|  1.224|18,558| 17662.712| 88.106|1,050,688|
| |Prince George's County|   761| 836.883|  2.671|24,009| 26403.043| 145.634| 909,327|
| |Anne Arundel County|   227| 391.897|  2.220| 7,450| 12861.814| 93.473| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,093| 11916.917| 42.382| 259,547|
| |Carroll County|   117| 694.580|  0.000| 1,567|  9302.629| 54.277| 168,447|
| |Howard County|   112| 343.885|  2.632| 3,913| 12014.492| 97.814| 325,690|
| |Charles County|    91| 557.403|  0.000| 2,067| 12661.019| 118.131| 163,257|
| |Harford County|    69| 270.121|  0.559| 2,012|  7876.574| 83.329| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,003|  8836.226| 90.615| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,356| 13087.666| 64.804| 103,609|
| |Washington County|    31| 205.231|  0.946| 1,029|  6812.359| 40.668| 151,049|
| |Cecil County|    30| 291.673|  0.000|   708|  6883.477| 63.890| 102,855|
| |Calvert County|    28| 302.621|  0.000|   713|  7706.025| 98.815|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   433|  8594.510| 96.408|  50,381|
| |Kent County|    23| 1184.224|  0.000|   242| 12460.097| 51.488|  19,422|
| |Worcester County|    20| 382.585|  2.733|   697| 13333.078| 158.499|  52,276|
| |Allegany County|    18| 255.624|  0.000|   300|  4260.395| 48.690|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   378| 11838.767| 116.330|  31,929|
| |Talbot County|     4| 107.582|  0.000|   403| 10838.869| 134.477|  37,181|
| |Somerset County|     3| 117.114|  0.000|   141|  5504.372| 66.922|  25,616|
| |Caroline County|     3| 89.804|  0.000|   453| 13560.438| 59.869|  33,406|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    51|  1757.772| 34.466|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,863| 425.268| N/A|75,862| 11268.499| N/A|6,732,219|
| |Marion County|   730| 756.805|  0.889|16,088| 16678.727| 156.841| 964,582|
| |Lake County|   278| 572.614|  1.471| 7,688| 15835.450| 161.544| 485,493|
| |Allen County|   163| 429.740|  1.883| 4,002| 10551.043| 128.056| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,789| 11310.830| 110.191| 158,167|
| |Hendricks County|   108| 634.134|  2.516| 1,927| 11314.595| 128.337| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,829|  8369.550| 120.875| 338,011|
| |Elkhart County|    85| 411.939|  5.539| 4,926| 23873.103| 204.931| 206,341|
| |St. Joseph County|    83| 305.342|  2.102| 3,578| 13162.832| 197.080| 271,826|
| |Howard County|    65| 787.459|  0.000|   913| 11060.768| 154.030|  82,544|
| |Madison County|    65| 501.663|  0.000| 1,006|  7764.203| 158.768| 129,569|
| |Delaware County|    52| 455.601|  0.000|   745|  6527.358| 113.900| 114,135|
| |Clark County|    49| 414.194|  4.830| 1,287| 10878.937| 214.946| 118,302|
| |Floyd County|    48| 611.294|  5.458|   809| 10302.845| 165.559|  78,522|
| |Bartholomew County|    47| 561.000|  0.000|   817|  9751.847| 117.656|  83,779|
| |Boone County|    46| 678.036|  0.000|   687| 10126.321| 90.545|  67,843|
| |Hancock County|    39| 498.925|  1.828|   683|  8737.591| 100.516|  78,168|
| |Porter County|    39| 228.888|  0.000| 1,355|  7952.391| 122.409| 170,389|
| |Greene County|    34| 1065.096|  0.000|   254|  7956.895| 62.653|  31,922|
| |Morgan County|    34| 482.345|  4.053|   493|  6993.999| 113.493|  70,489|
| |Decatur County|    32| 1204.865|  0.000|   341| 12839.339| 123.714|  26,559|
| |Monroe County|    31| 208.851|  0.962|   766|  5160.647| 68.334| 148,431|
| |Grant County|    30| 456.142|  2.172|   529|  8043.303| 47.786|  65,769|
| |LaPorte County|    30| 273.005|  1.300|   931|  8472.263| 114.402| 109,888|
| |Warrick County|    30| 476.206|  0.000|   588|  9333.630| 136.059|  62,998|
| |Noble County|    29| 607.406|  0.000|   688| 14410.188| 152.600|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   512| 10352.218| 112.650|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   352|  7758.431| 66.123|  45,370|
| |Shelby County|    27| 603.635|  3.194|   565| 12631.626| 137.335|  44,729|
| |Orange County|    24| 1221.623|  0.000|   174|  8856.765| 72.716|  19,646|
| |Marshall County|    23| 497.211|  3.088|   793| 17142.981| 151.325|  46,258|
| |Harrison County|    23| 567.691|  3.526|   348|  8589.411| 169.249|  40,515|
| |Montgomery County|    21| 547.759|  0.000|   359|  9364.077| 63.346|  38,338|
| |Daviess County|    20| 599.682|  4.283|   277|  8305.598| 119.936|  33,351|
| |Henry County|    20| 416.910|  5.956|   406|  8463.270| 125.073|  47,972|
| |Franklin County|    15| 659.109| 25.109|   246| 10809.386| 106.713|  22,758|
| |Perry County|    13| 678.178|  7.453|   187|  9755.334| 111.788|  19,169|
| |Vanderburgh County|    13| 71.645|  0.787| 2,022| 11143.504| 203.912| 181,451|
| |Tipton County|    12| 792.184| 56.585|   143|  9440.190| 245.200|  15,148|
| |Dubois County|    12| 280.794|  0.000|   708| 16566.829| 217.281|  42,736|
| |Jennings County|    12| 432.666|  0.000|   227|  8184.604| 72.111|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   868| 10924.285| 82.705|  79,456|
| |Vigo County|    11| 102.767|  1.335|   699|  6530.391| 253.582| 107,038|
| |Tippecanoe County|    11| 56.199|  0.000| 1,238|  6324.975| 87.583| 195,732|
| |White County|    11| 456.394|  5.927|   376| 15600.365| 171.889|  24,102|
| |Newton County|    10| 715.103|  0.000|   120|  8581.236| 91.942|  13,984|
| |LaGrange County|    10| 252.436|  0.000|   563| 14212.147| 61.306|  39,614|
| |Scott County|    10| 418.883|  0.000|   272| 11393.625| 119.681|  23,873|
| |Wayne County|    10| 151.782|  0.000|   385|  5843.604| 110.584|  65,884|
| |Cass County|     9| 238.796|  0.000| 1,802| 47812.359| 181.940|  37,689|
| |Ripley County|     8| 282.446|  5.044|   213|  7520.124| 116.005|  28,324|
| |Putnam County|     8| 212.902|  0.000|   312|  8303.172| 300.344|  37,576|
| |Fayette County|     7| 303.004|  0.000|   194|  8397.541| 197.880|  23,102|
| |Starke County|     7| 304.414|  0.000|   178|  7740.813| 86.975|  22,995|
| |Ohio County|     6| 1021.277| 48.632|    65| 11063.830| 340.426|   5,875|
| |Whitley County|     6| 176.658|  0.000|   155|  4563.656| 29.443|  33,964|
| |Jackson County|     5| 113.043|  3.230|   596| 13474.712| 135.651|  44,231|
| |Clay County|     5| 190.658|  0.000|   124|  4728.313| 125.289|  26,225|
| |Randolph County|     4| 162.173|  0.000|   124|  5027.367| 98.462|  24,665|
| |Rush County|     4| 241.240|  0.000|    85|  5126.349| 43.079|  16,581|
| |Clinton County|     4| 123.461|  4.409|   444| 13704.127| 370.382|  32,399|
| |DeKalb County|     4| 92.007|  0.000|   238|  5474.411| 55.861|  43,475|
| |Gibson County|     4| 118.839|  0.000|   231|  6862.949| 123.083|  33,659|
| |Steuben County|     3| 86.720|  0.000|   213|  6157.137| 49.554|  34,594|
| |Wabash County|     3| 96.787|  0.000|   170|  5484.579| 41.480|  30,996|
| |Spencer County|     3| 147.951|  0.000|   137|  6756.424| 176.132|  20,277|
| |Huntington County|     3| 82.147|  0.000|   124|  3395.400| 19.559|  36,520|
| |Carroll County|     2| 98.731|  0.000|   196|  9675.668| 338.507|  20,257|
| |Blackford County|     2| 170.097|  0.000|    65|  5528.151| 121.498|  11,758|
| |Wells County|     2| 70.681|  0.000|   174|  6149.279| 201.947|  28,296|
| |Fountain County|     2| 122.354|  0.000|    74|  4527.101| 87.396|  16,346|
| |Fulton County|     2| 100.130|  0.000|   172|  8611.195| 178.804|  19,974|
| |Miami County|     2| 56.313|  0.000|   277|  7799.302| 72.402|  35,516|
| |Adams County|     2| 55.902|  0.000|   109|  3046.650| 107.811|  35,777|
| |Jasper County|     2| 59.591|  0.000|   255|  7597.879| 191.543|  33,562|
| |Jefferson County|     2| 61.904|  0.000|   167|  5168.998| 66.326|  32,308|
| |Brown County|     1| 66.260|  0.000|    74|  4903.260| 37.863|  15,092|
| |Sullivan County|     1| 48.382|  0.000|   138|  6676.666| 414.700|  20,669|
| |Warren County|     1| 120.992|  0.000|    24|  2903.811| 86.423|   8,265|
| |Washington County|     1| 35.668|  0.000|   142|  5064.917| 127.387|  28,036|
| |Pulaski County|     1| 80.952|  0.000|    81|  6557.112| 115.646|  12,353|
| |Parke County|     1| 59.042|  0.000|    51|  3011.159| 25.304|  16,937|
| |Owen County|     1| 48.079|  0.000|    99|  4759.844| 116.764|  20,799|
| |Vermillion County|     0|  0.000|  0.000|    58|  3742.418| 147.484|  15,498|
| |Switzerland County|     0|  0.000|  0.000|    53|  4929.774| 132.878|  10,751|
| |Jay County|     0|  0.000|  0.000|    92|  4501.859| 76.895|  20,436|
| |Union County|     0|  0.000|  0.000|    41|  5812.305| 162.015|   7,054|
| |Posey County|     0|  0.000|  0.000|   179|  7039.761| 106.748|  25,427|
| |Pike County|     0|  0.000|  0.000|    59|  4762.289| 138.372|  12,389|
| |Martin County|     0|  0.000|  0.000|    48|  4680.644| 83.583|  10,255|
| |Knox County|     0|  0.000|  0.000|   161|  4399.628| 105.404|  36,594|
| |Crawford County|     0|  0.000|  0.000|    45|  4254.515| 13.506|  10,577|
| |Benton County|     0|  0.000|  0.000|    64|  7315.958| 65.321|   8,748|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,344| 274.617| N/A|101,745| 11920.189| N/A|8,535,519|
| |Fairfax County|   536| 467.089|  0.124|16,635| 14496.328| 70.462|1,147,532|
| |Henrico County|   186| 562.243|  1.727| 3,948| 11934.054| 111.412| 330,818|
| |Prince William County|   176| 374.201|  0.911| 9,566| 20338.695| 144.882| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,105| 13110.006| 79.619| 236,842|
| |Loudoun County|   115| 278.088|  0.691| 5,346| 12927.470| 87.399| 413,538|
| |Chesterfield County|    80| 226.756|  2.025| 4,439| 12582.128| 120.667| 352,802|
| |Alexandria city|    60| 376.345|  0.000| 2,995| 18785.910| 114.696| 159,428|
| |Virginia Beach city|    54| 120.007|  1.587| 5,111| 11358.434| 184.773| 449,974|
| |Suffolk city|    51| 553.698|  3.102| 1,316| 14287.575| 271.421|  92,108|
| |Shenandoah County|    46| 1054.659| 13.101|   722| 16553.558| 121.188|  43,616|
| |Richmond County|    45| 4987.255| 31.665| 3,551| 393549.817| 3467.330|   9,023|
| |Chesapeake city|    38| 155.207|  4.668| 2,958| 12081.606| 156.957| 244,835|
| |Spotsylvania County|    36| 264.288|  2.098| 1,514| 11114.782| 145.778| 136,215|
| |Hanover County|    32| 296.940|  1.326|   656|  6087.263| 67.607| 107,766|
| |Norfolk city|    32| 131.827|  3.531| 3,787| 15600.926| 213.042| 242,742|
| |Mecklenburg County|    32| 1046.196|  0.000|   446| 14581.358| 630.520|  30,587|
| |Harrisonburg city|    31| 584.729|  5.389| 1,082| 20408.933| 45.808|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   296| 25277.541| 12.200|  11,710|
| |Page County|    25| 1045.938|  5.977|   346| 14475.776| 71.721|  23,902|
| |Portsmouth city|    25| 264.836|  1.513| 1,833| 19417.784| 305.697|  94,398|
| |Galax city|    24| 3781.314|  0.000|   350| 55144.163| 202.570|   6,347|
| |Manassas city|    22| 535.475|  6.954| 1,666| 40550.079| 180.810|  41,085|
| |Colonial Heights city|    21| 1208.981|  0.000|   200| 11514.105| 106.917|  17,370|
| |Roanoke County|    19| 201.728|  1.517| 1,530| 16244.452| 244.198|  94,186|
| |Rockingham County|    19| 231.854|  3.487|   950| 11592.717| 54.041|  81,948|
| |Petersburg city|    19| 606.138| 13.672|   526| 16780.450| 218.757|  31,346|
| |Newport News city|    19| 106.012|  0.797| 1,855| 10350.119| 109.997| 179,225|
| |James City County|    17| 222.155|  1.867|   618|  8076.003| 85.875|  76,523|
| |Albemarle County|    16| 146.346|  2.613|   848|  7756.334| 75.786| 109,330|
| |Accomack County|    16| 495.111|  4.421| 1,106| 34224.533| 106.095|  32,316|
| |Charlottesville city|    15| 317.353|  6.045|   546| 11551.644| 126.941|  47,266|
| |Emporia city|    15| 2805.836|  0.000|   178| 33295.922| 187.056|   5,346|
| |Nottoway County|    14| 919.118| 46.894|   182| 11948.529| 46.894|  15,232|
| |Carroll County|    14| 469.941|  9.591|   332| 11144.305| 134.269|  29,791|
| |Southampton County|    13| 737.338|  0.000|   274| 15540.809| 234.976|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,012| 19237.715| 135.783|  52,605|
| |Prince Edward County|    11| 482.414|  6.265|   423| 18551.004| 407.232|  22,802|
| |Greensville County|    11| 970.360| 12.602|   497| 43842.625| 743.523|  11,336|
| |Fluvanna County|     9| 330.033|  5.239|   194|  7114.045| 99.534|  27,270|
| |Stafford County|     9| 58.869|  1.869| 1,405|  9190.094| 103.721| 152,882|
| |Sussex County|     9| 806.524|  0.000|   308| 27601.040| 358.455|  11,159|
| |Henry County|     9| 178.017|  8.477|   596| 11788.674| 206.274|  50,557|
| |Isle of Wight County|     9| 242.529|  0.000|   390| 10509.580| 103.941|  37,109|
| |Frederick County|     9| 100.769|  0.000|   685|  7669.656| 20.794|  89,313|
| |Fauquier County|     9| 126.365|  2.006|   623|  8747.297| 78.226|  71,222|
| |Buckingham County|     8| 466.527|  0.000|   610| 35572.662| 116.632|  17,148|
| |Bedford County|     8| 101.270|  1.808|   367|  4645.746| 101.270|  78,997|
| |Hampton city|     7| 52.041|  0.000| 1,257|  9345.030| 163.557| 134,510|
| |Franklin County|     7| 124.906|  0.000|   360|  6423.754| 112.161|  56,042|
| |Danville city|     7| 174.808|  0.000|   415| 10363.600| 242.590|  40,044|
| |Goochland County|     7| 294.700|  0.000|   165|  6946.491| 78.186|  23,753|
| |Manassas Park city|     7| 400.503|  0.000|   516| 29522.829| 114.430|  17,478|
| |Botetourt County|     7| 209.462|  0.000|   215|  6433.466| 98.319|  33,419|
| |Dinwiddie County|     7| 245.235|  5.005|   223|  7812.500| 65.062|  28,544|
| |Falls Church city|     6| 410.481|  9.773|    60|  4104.809| 19.547|  14,617|
| |Washington County|     6| 111.649|  5.317|   231|  4298.474| 124.940|  53,740|
| |Warren County|     6| 149.388|  0.000|   356|  8863.659| 17.784|  40,164|
| |Williamsburg city|     6| 401.230|  0.000|   128|  8559.583| 105.084|  14,954|
| |Caroline County|     5| 162.734|  0.000|   216|  7030.106| 111.589|  30,725|
| |Charles City County|     5| 718.081|  0.000|    53|  7611.662| 41.033|   6,963|
| |Hopewell city|     5| 221.936|  0.000|   275| 12206.489| 101.457|  22,529|
| |Lynchburg city|     5| 60.851|  5.216|   644|  7837.601| 274.699|  82,168|
| |Grayson County|     5| 321.543|  0.000|   156| 10032.154| 110.243|  15,550|
| |Augusta County|     4| 52.939|  0.000|   282|  3732.232| 41.595|  75,558|
| |York County|     4| 58.582|  2.092|   374|  5477.446| 92.058|  68,280|
| |Alleghany County|     4| 269.179|  9.614|    62|  4172.275| 57.681|  14,860|
| |Patrick County|     4| 227.169|  8.113|   161|  9143.571| 348.867|  17,608|
| |Powhatan County|     4| 134.898|  0.000|   149|  5024.956| 81.902|  29,652|
| |Winchester city|     4| 142.460|  0.000|   403| 14352.874| 45.791|  28,078|
| |King George County|     4| 149.054|  0.000|   149|  5552.243| 133.083|  26,836|
| |Salem city|     3| 118.572|  0.000|   163|  6442.433| 129.865|  25,301|
| |Waynesboro city|     3| 132.567|  0.000|   177|  7821.476| 63.127|  22,630|
| |Martinsville city|     3| 238.968|  0.000|   215| 17126.016| 477.935|  12,554|
| |Smyth County|     3| 99.655|  0.000|   151|  5015.945| 132.873|  30,104|
| |Northumberland County|     3| 248.036| 11.811|    78|  6448.946| 106.301|  12,095|
| |Wythe County|     3| 104.588|  0.000|   116|  4044.066| 44.823|  28,684|
| |Wise County|     3| 80.250|  0.000|   168|  4494.021| 252.215|  37,383|
| |Orange County|     3| 80.969|  0.000|   230|  6207.660| 57.835|  37,051|
| |Montgomery County|     3| 30.446|  0.000|   307|  3115.644| 27.546|  98,535|
| |Pulaski County|     3| 88.165|  0.000|    90|  2644.958| 50.380|  34,027|
| |Fredericksburg city|     3| 103.320|  4.920|   406| 13982.642| 172.200|  29,036|
| |Scott County|     3| 139.108|  0.000|   111|  5146.991| 324.585|  21,566|
| |Westmoreland County|     3| 166.528|  7.930|   213| 11823.480| 142.738|  18,015|
| |Floyd County|     2| 126.992|  9.071|    77|  4889.199| 326.551|  15,749|
| |Gloucester County|     2| 53.550|  0.000|   162|  4337.582| 57.375|  37,348|
| |Amelia County|     2| 152.149| 10.868|    81|  6162.039| 86.942|  13,145|
| |Surry County|     2| 311.429|  0.000|    52|  8097.166| 289.184|   6,422|
| |Campbell County|     2| 36.440|  0.000|   218|  3971.941| 145.759|  54,885|
| |Pittsylvania County|     2| 33.138|  0.000|   507|  8400.437| 300.607|  60,354|
| |Russell County|     2| 75.228|  5.373|   130|  4889.792| 306.284|  26,586|
| |Rappahannock County|     2| 271.370|  0.000|    44|  5970.149| 77.534|   7,370|
| |Prince George County|     2| 52.147|  0.000|   416| 10846.609| 283.085|  38,353|
| |Louisa County|     2| 53.204|  0.000|   190|  5054.401| 76.006|  37,591|
| |Brunswick County|     2| 123.221|  0.000|   237| 14601.688| 220.037|  16,231|
| |King William County|     2| 116.632|  0.000|    90|  5248.425| 99.970|  17,148|
| |Greene County|     2| 100.913|  0.000|   167|  8426.258| 115.329|  19,819|
| |Halifax County|     1| 29.489|  0.000|   157|  4629.766| 58.978|  33,911|
| |Amherst County|     1| 31.641|  4.520|   183|  5790.223| 266.685|  31,605|
| |Dickenson County|     1| 69.842|  9.977|    48|  3352.424| 189.572|  14,318|
| |Buchanan County|     1| 47.610|  6.801|    80|  3808.798| 47.610|  21,004|
| |Essex County|     1| 91.299|  0.000|   104|  9495.115| 273.898|  10,953|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 101.678|   7,025|
| |Lee County|     1| 42.693|  0.000|   125|  5336.635| 146.376|  23,423|
| |Madison County|     1| 75.409|  0.000|    70|  5278.637| 86.182|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    64|  5247.622| 58.567|  12,196|
| |Buena Vista city|     1| 154.369|  0.000|    56|  8644.643| 176.421|   6,478|
| |Middlesex County|     1| 94.500|  0.000|    46|  4347.004| 229.500|  10,582|
| |Rockbridge County|     1| 44.301|  6.329|    68|  3012.449| 12.657|  22,573|
| |New Kent County|     1| 43.307|  0.000|   128|  5543.285| 43.307|  23,091|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Cumberland County|     0|  0.000|  0.000|    76|  7652.034| 100.685|   9,932|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Bland County|     0|  0.000|  0.000|    22|  3503.185| 341.219|   6,280|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 27.842|   5,131|
| |Staunton city|     0|  0.000|  0.000|   154|  6176.801| 63.029|  24,932|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Radford city|     0|  0.000|  0.000|    56|  3068.661| 180.049|  18,249|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 46.567|  12,271|
| |Norton city|     0|  0.000|  0.000|    21|  5275.057| 251.193|   3,981|
| |Appomattox County|     0|  0.000|  0.000|    88|  5530.765| 143.656|  15,911|
| |Nelson County|     0|  0.000|  0.000|    52|  3482.920| 172.232|  14,930|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 130.463|   2,190|
| |Mathews County|     0|  0.000|  0.000|    18|  2037.582| 48.514|   8,834|
| |Lancaster County|     0|  0.000|  0.000|    40|  3772.517| 107.786|  10,603|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Giles County|     0|  0.000|  0.000|    26|  1555.024| 25.632|  16,720|
| |Tazewell County|     0|  0.000|  0.000|   122|  3005.296| 70.382|  40,595|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Bristol city|     0|  0.000|  0.000|    88|  5249.970| 187.499|  16,762|
| |Charlotte County|     0|  0.000|  0.000|    54|  4545.455| 60.125|  11,880|
| |Clarke County|     0|  0.000|  0.000|    71|  4856.693| 19.544|  14,619|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910|  0.000|   7,446|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,248| 214.338| N/A|138,743| 13228.632| N/A|10,488,084|
| |Mecklenburg County|   233| 209.843|  1.415|22,462| 20229.548| 147.443|1,110,356|
| |Wake County|   176| 158.307|  5.397|12,148| 10926.809| 104.210|1,111,761|
| |Guilford County|   156| 290.409|  1.596| 5,704| 10618.533| 104.781| 537,174|
| |Durham County|    80| 248.843|  0.444| 6,221| 19350.645| 122.200| 321,488|
| |Orange County|    58| 390.636| 12.508| 1,356|  9132.789| 57.729| 148,476|
| |Chatham County|    55| 738.552|  9.592| 1,305| 17523.835| 95.916|  74,470|
| |Henderson County|    54| 459.899|  0.000| 1,495| 12732.398| 91.250| 117,417|
| |Robeson County|    53| 405.742|  2.187| 2,845| 21779.904| 178.264| 130,625|
| |Gaston County|    52| 231.596|  6.999| 3,358| 14955.752| 174.969| 224,529|
| |Forsyth County|    52| 136.021|  1.121| 5,317| 13908.108| 115.842| 382,295|
| |Cumberland County|    51| 152.008|  0.426| 3,286|  9794.074| 192.884| 335,509|
| |Cabarrus County|    50| 230.997|  0.660| 2,655| 12265.942| 99.659| 216,453|
| |Buncombe County|    49| 187.602|  1.641| 1,905|  7293.513| 89.699| 261,191|
| |Duplin County|    48| 817.146|  2.432| 2,016| 34320.151| 155.647|  58,741|
| |Rowan County|    48| 337.819|  0.000| 2,220| 15624.120| 160.866| 142,088|
| |Columbus County|    48| 864.740|  5.147|   918| 16538.157| 205.891|  55,508|
| |Johnston County|    46| 219.739|  1.365| 3,334| 15926.320| 148.085| 209,339|
| |Union County|    43| 179.272|  0.596| 3,146| 13116.039| 157.831| 239,859|
| |Wayne County|    42| 341.100|  5.801| 2,435| 19775.686| 121.821| 123,131|
| |Vance County|    41| 920.624|  3.208|   778| 17469.406| 125.102|  44,535|
| |Alamance County|    41| 241.875|  0.000| 2,496| 14724.882| 182.038| 169,509|
| |Harnett County|    39| 286.815|  3.152| 1,318|  9692.887| 147.085| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,191| 15250.545| 115.346| 143,667|
| |Wilson County|    35| 427.868|  0.000| 1,514| 18508.331| 136.219|  81,801|
| |Catawba County|    30| 188.028|  0.895| 2,161| 13544.259| 169.225| 159,551|
| |Granville County|    29| 479.791|  7.091| 1,262| 20879.175| 179.626|  60,443|
| |Burke County|    28| 309.444|  0.000| 1,776| 19627.563| 219.452|  90,485|
| |Franklin County|    26| 373.108|  2.050|   872| 12513.453| 137.353|  69,685|
| |Stanly County|    26| 413.973| 13.647| 1,089| 17339.108| 366.207|  62,806|
| |Cleveland County|    22| 224.611|  7.293| 1,208| 12333.201| 176.480|  97,947|
| |Brunswick County|    22| 154.040|  5.001| 1,260|  8822.294| 58.015| 142,820|
| |New Hanover County|    20| 85.298|  0.000| 2,696| 11498.126| 150.489| 234,473|
| |Pasquotank County|    20| 502.210| 10.762|   423| 10621.736| 225.994|  39,824|
| |Moore County|    20| 198.255|  0.000| 1,021| 10120.936| 124.618| 100,880|
| |Davidson County|    18| 107.393|  0.000| 1,797| 10721.381| 103.984| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,905| 10478.202| 105.293| 181,806|
| |Caldwell County|    16| 194.699|  3.477| 1,227| 14931.003| 126.902|  82,178|
| |Northampton County|    16| 821.229|  0.000|   352| 18067.033| 168.645|  19,483|
| |Sampson County|    15| 236.105|  4.497| 1,516| 23862.366| 191.133|  63,531|
| |Rutherford County|    15| 223.784|  2.131|   781| 11651.673| 196.077|  67,029|
| |Craven County|    15| 146.859|  6.993|   753|  7372.306| 111.892| 102,139|
| |Montgomery County|    14| 515.217|  0.000|   740| 27232.915| 504.703|  27,173|
| |Haywood County|    14| 224.658| 16.047|   438|  7028.580| 187.979|  62,317|
| |McDowell County|    14| 305.971|  3.122|   693| 15145.555| 234.161|  45,756|
| |Edgecombe County|    13| 252.565|  2.775|   664| 12900.218| 188.730|  51,472|
| |Lenoir County|    12| 214.481|  0.000|   599| 10706.179| 155.754|  55,949|
| |Nash County|    12| 127.256|  0.000| 1,209| 12821.057| 204.519|  94,298|
| |Wilkes County|    12| 175.408|  4.176|   843| 12322.400| 212.995|  68,412|
| |Onslow County|    11| 55.573|  0.722| 1,108|  5597.712| 106.094| 197,938|
| |Pitt County|    11| 60.860|  0.000| 2,054| 11364.265| 199.179| 180,742|
| |Lee County|    11| 178.054|  0.000| 1,302| 21075.123| 178.054|  61,779|
| |Hoke County|    11| 199.153|  5.173|   726| 13144.078| 116.388|  55,234|
| |Hertford County|    11| 464.586|  0.000|   353| 14908.983| 277.545|  23,677|
| |Surry County|    10| 139.309|  1.990|   960| 13373.640| 165.180|  71,783|
| |Richmond County|     9| 200.763|  3.187|   521| 11621.941| 111.535|  44,829|
| |Lincoln County|     9| 104.516|  9.954|   858|  9963.884| 141.014|  86,111|
| |Rockingham County|     8| 87.902|  1.570|   567|  6230.085| 114.587|  91,010|
| |Jones County|     8| 849.347| 75.835|    99| 10510.670| 318.505|   9,419|
| |Jackson County|     7| 159.315| 13.005|   457| 10401.020| 146.310|  43,938|
| |Bladen County|     7| 213.923|  0.000|   626| 19130.860| 152.802|  32,722|
| |Davie County|     7| 163.376|  3.334|   431| 10059.282| 146.705|  42,846|
| |Warren County|     7| 354.772|  0.000|   260| 13177.234| 101.363|  19,731|
| |Halifax County|     6| 119.976|  0.000|   715| 14297.141| 185.677|  50,010|
| |Yadkin County|     6| 159.291|  0.000|   552| 14654.738| 166.876|  37,667|
| |Martin County|     6| 267.380|  0.000|   268| 11942.959| 146.422|  22,440|
| |Carteret County|     6| 86.364|  0.000|   376|  5412.175| 90.477|  69,473|
| |Polk County|     5| 241.266|  0.000|   164|  7913.530| 124.080|  20,724|
| |Bertie County|     5| 263.894|  0.000|   280| 14778.065| 196.036|  18,947|
| |Cherokee County|     4| 139.801|  4.993|   296| 10345.310| 154.780|  28,612|
| |Macon County|     4| 111.551|  3.984|   480| 13386.134| 79.679|  35,858|
| |Washington County|     4| 345.423|  0.000|   135| 11658.031| 172.712|  11,580|
| |Stokes County|     3| 65.802|  0.000|   296|  6492.509| 81.470|  45,591|
| |Anson County|     3| 122.719|  5.844|   332| 13580.954| 140.251|  24,446|
| |Mitchell County|     3| 200.481|  9.547|   120|  8019.246| 38.187|  14,964|
| |Greene County|     3| 142.389|  0.000|   332| 15757.748| 128.828|  21,069|
| |Pender County|     3| 47.574|  0.000|   666| 10561.370| 77.024|  63,060|
| |Alexander County|     2| 53.338|  0.000|   312|  8320.666| 64.767|  37,497|
| |Gates County|     2| 172.980|  0.000|    45|  3892.060|  0.000|  11,562|
| |Swain County|     2| 140.144|  0.000|   120|  8408.661| 140.144|  14,271|
| |Scotland County|     2| 57.433|  0.000|   365| 10481.578| 258.450|  34,823|
| |Beaufort County|     2| 42.559|  0.000|   437|  9299.059| 194.554|  46,994|
| |Camden County|     2| 184.043|  0.000|    73|  6717.585| 131.460|  10,867|
| |Person County|     2| 50.646|  0.000|   226|  5722.968| 90.439|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    88|  6536.433| 159.166|  13,463|
| |Dare County|     2| 54.041|  0.000|   210|  5674.295| 30.881|  37,009|
| |Chowan County|     2| 143.441| 10.246|   158| 11331.851| 133.195|  13,943|
| |Caswell County|     2| 88.480|  0.000|   196|  8671.032| 44.240|  22,604|
| |Transylvania County|     1| 29.082|  0.000|   145|  4216.955| 54.010|  34,385|
| |Pamlico County|     1| 78.579|  0.000|    73|  5736.288| 89.805|  12,726|
| |Tyrrell County|     1| 249.004|  0.000|    99| 24651.394| 249.004|   4,016|
| |Ashe County|     1| 36.761|  0.000|   165|  6065.507| 204.809|  27,203|
| |Avery County|     0|  0.000|  0.000|   109|  6208.350| 81.368|  17,557|
| |Alleghany County|     0|  0.000|  0.000|   169| 15174.643| 51.309|  11,137|
| |Currituck County|     0|  0.000|  0.000|    73|  2629.399| 10.291|  27,763|
| |Graham County|     0|  0.000|  0.000|    40|  4738.775| 186.166|   8,441|
| |Hyde County|     0|  0.000|  0.000|    47|  9519.951| 289.360|   4,937|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984|  0.000|  11,231|
| |Madison County|     0|  0.000|  0.000|    45|  2068.490| 26.267|  21,755|
| |Yancey County|     0|  0.000|  0.000|   114|  6309.148| 102.781|  18,069|
| |Watauga County|     0|  0.000|  0.000|   316|  5625.078| 83.918|  56,177|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,098| 407.480| N/A|102,130| 19836.021| N/A|5,148,714|
| |Greenville County|   213| 406.844|  4.639|11,028| 21064.213| 159.900| 523,542|
| |Charleston County|   203| 493.430|  8.681|12,454| 30271.800| 222.234| 411,406|
| |Horry County|   160| 451.874|  8.069| 8,678| 24508.516| 178.732| 354,081|
| |Richland County|   154| 370.407|  3.780| 8,917| 21447.521| 255.643| 415,759|
| |Florence County|   117| 846.030| 17.561| 3,511| 25388.125| 390.475| 138,293|
| |Lexington County|   113| 378.243|  3.825| 5,032| 16843.515| 134.848| 298,750|
| |Spartanburg County|   102| 318.964|  4.467| 4,172| 13046.265| 149.207| 319,785|
| |Berkeley County|    68| 298.367|  4.388| 4,272| 18744.488| 192.434| 227,907|
| |Orangeburg County|    68| 789.092| 13.262| 2,450| 28430.519| 319.947|  86,175|
| |Anderson County|    67| 330.769| 13.400| 2,405| 11873.143| 176.316| 202,558|
| |Beaufort County|    57| 296.686|  5.205| 4,194| 21829.879| 336.096| 192,122|
| |Clarendon County|    53| 1570.603| 12.700|   859| 25455.623| 279.406|  33,745|
| |Sumter County|    52| 487.252|  9.370| 2,557| 23959.671| 254.335| 106,721|
| |Dorchester County|    50| 307.108|  8.775| 3,113| 19120.565| 226.383| 162,809|
| |Laurens County|    46| 681.552| 19.050| 1,349| 19987.258| 222.245|  67,493|
| |Aiken County|    39| 228.241|  6.688| 1,934| 11318.414| 247.470| 170,872|
| |Darlington County|    36| 540.394|  6.433| 1,335| 20039.629| 394.574|  66,618|
| |Colleton County|    34| 902.407| 11.375|   828| 21976.272| 216.123|  37,677|
| |Williamsburg County|    31| 1020.811|  9.408| 1,026| 33785.564| 371.632|  30,368|
| |Cherokee County|    30| 523.560|  4.986|   668| 11657.941| 249.314|  57,300|
| |Lee County|    29| 1723.318| 16.979|   559| 33218.445| 229.210|  16,828|
| |York County|    29| 103.211|  0.508| 3,637| 12944.028| 164.730| 280,979|
| |Pickens County|    27| 212.793|  4.504| 1,876| 14785.158| 122.722| 126,884|
| |Kershaw County|    27| 405.704|  8.586| 1,409| 21171.733| 210.365|  66,551|
| |Lancaster County|    26| 265.274|  5.830| 1,247| 12722.932| 212.802|  98,012|
| |Dillon County|    25| 820.237|  9.374|   654| 21457.397| 332.782|  30,479|
| |Bamberg County|    24| 1706.242| 71.093|   480| 34124.840| 355.467|  14,066|
| |Fairfield County|    24| 1073.970|  6.393|   572| 25596.277| 204.566|  22,347|
| |Chesterfield County|    21| 460.022|  6.259|   783| 17152.245| 222.187|  45,650|
| |Georgetown County|    19| 303.127|  0.000| 1,479| 23596.043| 364.664|  62,680|
| |Greenwood County|    18| 254.198|  4.035| 1,442| 20364.068| 280.425|  70,811|
| |Jasper County|    17| 565.291| 19.001|   609| 20250.723| 342.025|  30,073|
| |Chester County|    14| 434.189|  4.431|   691| 21430.344| 478.494|  32,244|
| |Marion County|    13| 424.047|  4.660|   560| 18266.628| 153.775|  30,657|
| |Calhoun County|    13| 893.287| 29.449|   377| 25905.312| 373.021|  14,553|
| |Hampton County|    12| 624.285| 37.160|   444| 23098.533| 364.166|  19,222|
| |Oconee County|    11| 138.285|  7.184|   844| 10610.213| 149.060|  79,546|
| |Newberry County|    10| 260.146|  3.716|   855| 22242.456| 196.967|  38,440|
| |Abbeville County|     9| 366.943|  5.824|   346| 14106.903| 262.102|  24,527|
| |Saluda County|     8| 390.759|  0.000|   465| 22712.841| 272.135|  20,473|
| |Edgefield County|     7| 256.787|  5.241|   338| 12399.120| 241.065|  27,260|
| |Barnwell County|     7| 335.474| 13.693|   431| 20655.612| 403.938|  20,866|
| |Allendale County|     5| 575.506| 32.886|   232| 26703.499| 608.393|   8,688|
| |Marlboro County|     4| 153.151|  0.000|   516| 19756.490| 377.408|  26,118|
| |Union County|     4| 146.434|  5.230|   375| 13728.218| 172.583|  27,316|
| |McCormick County|     2| 211.349|  0.000|   127| 13420.691| 301.928|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,944| 653.193| N/A|68,293| 22946.768| N/A|2,976,149|
| |Hinds County|   119| 513.285|  5.546| 5,700| 24585.921| 228.606| 231,840|
| |Neshoba County|    92| 3159.558| 19.625| 1,288| 44233.807| 274.744|  29,118|
| |Lauderdale County|    92| 1241.147|  7.709| 1,415| 19089.376| 117.562|  74,125|
| |Madison County|    69| 649.277| 12.098| 2,455| 23101.099| 176.098| 106,272|
| |Leflore County|    66| 2341.837| 30.413|   949| 33672.781| 420.720|  28,183|
| |Jones County|    59| 866.398|  4.196| 1,931| 28356.193| 266.423|  68,098|
| |Forrest County|    56| 747.693|  5.722| 1,826| 24380.149| 329.977|  74,897|
| |Monroe County|    55| 1560.195| 20.262|   821| 23289.459| 425.508|  35,252|
| |Holmes County|    49| 2880.658|  8.398|   910| 53497.942| 495.507|  17,010|
| |Jackson County|    44| 306.370|  5.968| 2,314| 16112.299| 249.672| 143,617|
| |Lee County|    42| 491.596| 20.065| 1,521| 17802.800| 413.008|  85,436|
| |Lincoln County|    42| 1229.760|  4.183|   834| 24419.524| 326.263|  34,153|
| |Washington County|    42| 956.524| 29.281| 1,701| 38739.211| 575.866|  43,909|
| |Pearl River County|    40| 720.266|  7.717|   559| 10065.724| 162.060|  55,535|
| |Oktibbeha County|    39| 786.496|  8.643| 1,133| 22848.731| 210.309|  49,587|
| |Lowndes County|    39| 665.586| 17.066| 1,092| 18636.402| 226.738|  58,595|
| |Pike County|    37| 941.763| 18.181|   940| 23925.881| 341.798|  39,288|
| |Harrison County|    36| 173.010|  2.060| 2,601| 12500.000| 256.083| 208,080|
| |Rankin County|    35| 225.412|  4.600| 2,307| 14857.894| 127.887| 155,271|
| |Bolivar County|    35| 1142.745| 13.993| 1,136| 37090.244| 694.976|  30,628|
| |Warren County|    35| 771.248| 15.740| 1,125| 24790.110| 469.045|  45,381|
| |DeSoto County|    31| 167.617|  3.090| 3,710| 20060.018| 249.495| 184,945|
| |Simpson County|    31| 1162.878| 16.077|   806| 30234.826| 444.787|  26,658|
| |Tate County|    30| 1059.285| 30.265|   743| 26234.949| 393.449|  28,321|
| |Copiah County|    28| 997.684| 10.180|   962| 34277.570| 193.429|  28,065|
| |Leake County|    26| 1141.052|  6.270|   795| 34889.845| 150.468|  22,786|
| |Clarke County|    26| 1672.994|  9.192|   336| 21620.230| 238.999|  15,541|
| |Adams County|    25| 814.518|  0.000|   632| 20591.014| 209.447|  30,693|
| |Attala County|    25| 1375.592|  7.861|   527| 28997.469| 196.513|  18,174|
| |Sunflower County|    25| 995.619| 11.379| 1,056| 42054.958| 739.603|  25,110|
| |Grenada County|    23| 1108.007| 13.764|   851| 40996.242| 240.871|  20,758|
| |Wayne County|    21| 1040.480|  0.000|   780| 38646.386| 311.436|  20,183|
| |Walthall County|    21| 1469.971| 29.999|   502| 35139.297| 389.992|  14,286|
| |Scott County|    20| 711.136|  5.080| 1,011| 35947.945| 248.898|  28,124|
| |Marion County|    20| 813.901|  5.814|   684| 27835.429| 343.001|  24,573|
| |Lafayette County|    19| 351.728| 18.512|   987| 18271.349| 269.746|  54,019|
| |Chickasaw County|    19| 1110.916|  0.000|   476| 27831.375| 275.641|  17,103|
| |Winston County|    16| 891.117|  7.956|   629| 35032.025| 358.038|  17,955|
| |Union County|    16| 555.266|  9.915|   662| 22974.145| 614.759|  28,815|
| |Panola County|    16| 467.946| 20.890| 1,068| 31235.377| 551.507|  34,192|
| |Lamar County|    15| 236.806|  4.511| 1,231| 19433.876| 191.700|  63,343|
| |Kemper County|    14| 1437.077|  0.000|   233| 23917.060| 87.984|   9,742|
| |Clay County|    14| 724.788|  7.396|   401| 20759.992| 199.686|  19,316|
| |Tippah County|    14| 635.930| 12.978|   374| 16988.417| 376.367|  22,015|
| |Hancock County|    14| 293.920|  0.000|   402|  8439.704| 173.953|  47,632|
| |Covington County|    14| 751.234| 15.331|   622| 33376.261| 160.979|  18,636|
| |Claiborne County|    14| 1557.632| 15.894|   409| 45505.118| 127.154|   8,988|
| |Yazoo County|    13| 437.858|  9.623|   841| 28326.036| 230.958|  29,690|
| |Wilkinson County|    13| 1506.373|  0.000|   215| 24913.094| 446.946|   8,630|
| |Coahoma County|    13| 587.597| 19.371|   781| 35301.031| 671.540|  22,124|
| |Smith County|    13| 816.788|  0.000|   406| 25508.922| 188.490|  15,916|
| |Noxubee County|    12| 1151.963| 13.714|   461| 44254.584| 479.985|  10,417|
| |Webster County|    12| 1238.518|  0.000|   237| 24460.729| 530.793|   9,689|
| |Greene County|    12| 883.262| 10.515|   256| 18842.927| 252.361|  13,586|
| |Humphreys County|    12| 1488.095| 17.715|   297| 36830.357| 407.455|   8,064|
| |Carroll County|    11| 1105.861|  0.000|   261| 26239.067| 186.704|   9,947|
| |Tallahatchie County|    11| 796.582| 10.345|   541| 39177.348| 465.535|  13,809|
| |Newton County|    11| 523.361|  0.000|   545| 25930.155| 129.141|  21,018|
| |Prentiss County|    10| 397.994| 22.743|   423| 16835.151| 409.365|  25,126|
| |Itawamba County|    10| 427.533|  0.000|   387| 16545.532| 427.533|  23,390|
| |Yalobusha County|    10| 825.900|  0.000|   316| 26098.447| 35.396|  12,108|
| |Calhoun County|     9| 626.697|  0.000|   425| 29594.039| 437.693|  14,361|
| |Marshall County|     9| 255.001|  4.048|   712| 20173.401| 514.049|  35,294|
| |Pontotoc County|     9| 279.729|  8.880|   842| 26170.200| 399.613|  32,174|
| |Jasper County|     9| 549.350|  0.000|   394| 24049.319| 78.479|  16,383|
| |Lawrence County|     8| 635.627| 34.051|   323| 25663.436| 90.804|  12,586|
| |Perry County|     8| 668.170| 11.932|   242| 20212.144| 190.906|  11,973|
| |Jefferson County|     7| 1001.431| 20.437|   195| 27896.996| 40.875|   6,990|
| |Tishomingo County|     7| 361.141| 22.111|   437| 22545.530| 722.282|  19,383|
| |Tunica County|     7| 726.744| 14.832|   358| 37167.774| 978.880|   9,632|
| |George County|     6| 244.898|  5.831|   595| 24285.714| 268.222|  24,500|
| |Jefferson Davis County|     6| 539.180|  0.000|   233| 20938.174| 243.915|  11,128|
| |Amite County|     6| 487.924|  0.000|   237| 19272.993| 302.048|  12,297|
| |Alcorn County|     5| 135.307|  3.866|   435| 11771.710| 278.346|  36,953|
| |Stone County|     5| 272.688| 15.582|   211| 11507.417| 405.136|  18,336|
| |Sharkey County|     5| 1157.140| 132.245|   204| 47211.294| 694.284|   4,321|
| |Montgomery County|     5| 511.509| 29.229|   329| 33657.289| 467.665|   9,775|
| |Choctaw County|     4| 487.211|  0.000|   135| 16443.362| 104.402|   8,210|
| |Franklin County|     2| 259.302|  0.000|   131| 16984.312| 259.302|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    27| 20346.647| 645.925|   1,327|
| |Benton County|     1| 121.080| 17.297|   145| 17556.605| 259.457|   8,259|
| |Quitman County|     1| 147.232|  0.000|   269| 39605.418| 757.193|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,874| 325.419| N/A|51,422|  8929.390| N/A|5,758,736|
| |Denver County|   417| 573.424| N/A|10,319| 14189.829| N/A| 727,211|
| |Arapahoe County|   362| 551.333|  0.000| 7,377| 11235.322| 61.791| 656,590|
| |Jefferson County|   233| 399.739|  1.471| 4,258|  7305.093| 64.703| 582,881|
| |Adams County|   177| 342.081|  1.104| 6,581| 12718.850| 110.438| 517,421|
| |Weld County|   145| 446.852|  1.321| 3,742| 11531.871| 71.320| 324,492|
| |El Paso County|   140| 194.336|  0.595| 5,183|  7194.584| 103.117| 720,403|
| |Boulder County|    76| 232.989|  0.438| 2,086|  6394.928| 61.313| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,759|  5009.198| 36.207| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   687| 23634.237| 44.231|  29,068|
| |Larimer County|    37| 103.671|  0.801| 1,590|  4455.042| 68.046| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   709|  4209.614| 78.034| 168,424|
| |Broomfield County|    32| 454.126| N/A|   482|  6840.275| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   304| 14934.172| 84.215|  20,356|
| |Montrose County|    13| 304.037|  0.000|   312|  7296.880| 83.527|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,126| 20425.563| 88.108|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   231| 14230.272| 61.603|  16,233|
| |Routt County|     8| 312.037| 11.144|   125|  4875.575| 83.581|  25,638|
| |Gunnison County|     6| 343.603|  0.000|   274| 15691.215| 98.172|  17,462|
| |Otero County|     6| 328.263|  0.000|    76|  4158.004| 101.605|  18,278|
| |Logan County|     5| 223.125|  0.000|   655| 29229.328| 38.250|  22,409|
| |Garfield County|     4| 66.599|  0.000|   773| 12870.249| 92.763|  60,061|
| |Mesa County|     4| 25.939|  0.926|   329|  2133.454| 50.951| 154,210|
| |Summit County|     4| 128.986|  0.000|   338| 10899.358| 64.493|  31,011|
| |Montezuma County|     4| 152.771|  0.000|   112|  4277.585| 21.824|  26,183|
| |Kit Carson County|     3| 422.714|  0.000|    56|  7890.658| 261.680|   7,097|
| |Teller County|     3| 118.166|  0.000|   136|  5356.862| 106.912|  25,388|
| |Elbert County|     2| 74.825|  0.000|   107|  4003.143| 80.170|  26,729|
| |La Plata County|     2| 35.574|  0.000|   222|  3948.702| 53.361|  56,221|
| |Pitkin County|     2| 112.568|  0.000|   188| 10581.415| 88.446|  17,767|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Rio Grande County|     2| 177.510|  0.000|    89|  7899.175| 25.359|  11,267|
| |Grand County|     1| 63.557|  0.000|    51|  3241.388| 63.557|  15,734|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 64.529|  13,283|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Crowley County|     1| 164.989|  0.000|    72| 11879.228|  0.000|   6,061|
| |Delta County|     1| 32.090|  0.000|   128|  4107.567| 59.596|  31,162|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 29.455|   9,700|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 41.426|   6,897|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Gilpin County|     0|  0.000|  0.000|    16|  2562.870|  0.000|   6,243|
| |Fremont County|     0|  0.000|  0.000|   128|  2675.641| 44.793|  47,839|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481|  0.000|   5,068|
| |Costilla County|     0|  0.000|  0.000|    23|  5917.160| 36.753|   3,887|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 76.846|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    36|  2566.113| 30.549|  14,029|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684| 105.469|   8,127|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053| 14.259|  10,019|
| |Washington County|     0|  0.000|  0.000|    49|  9983.700| 58.214|   4,908|
| |San Miguel County|     0|  0.000|  0.000|    90| 11003.790| 174.663|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 271.076|   6,324|
| |Prowers County|     0|  0.000|  0.000|    54|  4436.411| 46.946|  12,172|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 50.117|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866| 29.544|  14,506|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,781| 363.233| N/A|99,926| 20379.814| N/A|4,903,185|
| |Jefferson County|   246| 373.535|  3.905|13,366| 20295.396| 287.852| 658,573|
| |Mobile County|   212| 513.056|  5.186|10,581| 25606.834| 487.818| 413,210|
| |Montgomery County|   151| 666.708|  2.523| 6,825| 30134.313| 327.993| 226,486|
| |Tuscaloosa County|    79| 377.349|  8.871| 4,269| 20391.202| 194.475| 209,355|
| |Tallapoosa County|    79| 1957.044|  3.539|   875| 21676.122| 187.565|  40,367|
| |Walker County|    65| 1023.284|  2.249| 1,544| 24306.922| 157.428|  63,521|
| |Lee County|    47| 285.641|  6.077| 2,708| 16457.804| 164.092| 164,542|
| |Elmore County|    39| 480.242|  3.518| 1,760| 21672.475| 235.723|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   847| 25470.620| 81.623|  33,254|
| |Marshall County|    38| 392.667|  7.381| 3,194| 33004.733| 310.001|  96,774|
| |Shelby County|    37| 169.957|  3.281| 3,334| 15314.512| 169.957| 217,702|
| |Butler County|    36| 1851.090|  7.346|   770| 39592.760| 139.566|  19,448|
| |Madison County|    34| 91.175|  2.682| 5,469| 14665.776| 148.255| 372,909|
| |Etowah County|    34| 332.460|  8.381| 2,180| 21316.541| 311.506| 102,268|
| |Baldwin County|    29| 129.909|  3.840| 3,670| 16440.148| 260.457| 223,234|
| |Dale County|    29| 589.767| 20.337|   843| 17143.903| 162.694|  49,172|
| |Marion County|    26| 875.156|  9.617|   582| 19590.023| 168.299|  29,709|
| |Hale County|    26| 1774.623|  0.000|   485| 33103.542| 273.019|  14,651|
| |Dallas County|    24| 645.231|  3.841| 1,336| 35917.841| 161.308|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   571| 58708.616| 190.946|   9,726|
| |Franklin County|    22| 701.486|  9.110| 1,297| 41355.781| 414.514|  31,362|
| |Autauga County|    22| 393.778|  5.114| 1,162| 20798.654| 337.524|  55,869|
| |Covington County|    21| 566.817|  3.856|   740| 19973.549| 96.397|  37,049|
| |Lauderdale County|    20| 215.682| 12.325| 1,190| 12833.094| 146.356|  92,729|
| |St. Clair County|    20| 223.434| 12.768| 1,363| 15227.009| 202.686|  89,512|
| |Morgan County|    19| 158.758|  4.775| 2,418| 20204.046| 208.892| 119,679|
| |Sumter County|    18| 1448.459|  0.000|   366| 29452.000| 80.470|  12,427|
| |Calhoun County|    18| 158.444|  7.545| 1,819| 16011.619| 287.965| 113,605|
| |Escambia County|    17| 464.062|  7.799| 1,088| 29699.997| 425.066|  36,633|
| |Colbert County|    17| 307.742| 12.930| 1,215| 21994.533| 279.296|  55,241|
| |Marengo County|    16| 848.221| 15.147|   566| 30005.832| 302.936|  18,863|
| |DeKalb County|    14| 195.769|  1.998| 1,834| 25645.687| 231.726|  71,513|
| |Talladega County|    14| 175.048|  1.786| 1,054| 13178.624| 226.848|  79,978|
| |Macon County|    14| 774.851|  7.907|   339| 18762.453| 221.386|  18,068|
| |Houston County|    13| 122.778|  1.349| 1,428| 13486.712| 136.270| 105,882|
| |Limestone County|    13| 131.426|  0.000| 1,359| 13739.069| 218.080|  98,915|
| |Washington County|    12| 735.024|  0.000|   444| 27195.884| 1137.537|  16,326|
| |Choctaw County|    12| 953.213|  0.000|   289| 22956.549| 147.521|  12,589|
| |Cullman County|    12| 143.253|  1.705| 1,230| 14683.411| 124.493|  83,768|
| |Bullock County|    11| 1089.001|  0.000|   481| 47619.048| 565.715|  10,101|
| |Winston County|    11| 465.530|  0.000|   457| 19340.641| 151.146|  23,629|
| |Randolph County|    11| 484.112|  6.287|   402| 17692.105| 69.159|  22,722|
| |Greene County|    11| 1356.183|  0.000|   252| 31068.919| 123.289|   8,111|
| |Wilcox County|    10| 964.041| 13.772|   434| 41839.391| 358.072|  10,373|
| |Conecuh County|    10| 828.706|  0.000|   393| 32568.161| 248.612|  12,067|
| |Clarke County|    10| 423.334|  6.048|   826| 34967.403| 2050.147|  23,622|
| |Pickens County|     9| 451.581|  0.000|   408| 20471.651| 265.214|  19,930|
| |Chilton County|     9| 202.575|  9.646|   818| 18411.812| 308.686|  44,428|
| |Cherokee County|     8| 305.390|  5.453|   276| 10535.960| 158.148|  26,196|
| |Pike County|     7| 211.391|  0.000|   713| 21531.678| 228.647|  33,114|
| |Monroe County|     6| 289.394| 13.781|   423| 20402.257| 192.929|  20,733|
| |Barbour County|     6| 243.053|  5.787|   579| 23454.590| 92.592|  24,686|
| |Crenshaw County|     6| 435.667| 31.119|   332| 24106.884| 363.055|  13,772|
| |Coffee County|     6| 114.631|  2.729|   765| 14615.414| 133.736|  52,342|
| |Fayette County|     5| 306.711|  0.000|   223| 13679.303| 411.869|  16,302|
| |Clay County|     5| 377.786|  0.000|   267| 20173.782| 474.931|  13,235|
| |Bibb County|     5| 223.274| 12.759|   444| 19826.739| 401.893|  22,394|
| |Blount County|     5| 86.466|  4.941|   816| 14111.299| 185.285|  57,826|
| |Jackson County|     4| 77.480|  0.000| 1,026| 19873.707| 431.676|  51,626|
| |Perry County|     4| 448.280|  0.000|   445| 49871.120| 224.140|   8,923|
| |Henry County|     3| 174.368|  0.000|   264| 15344.377| 149.458|  17,205|
| |Coosa County|     3| 281.347| 13.397|   105|  9847.135| 174.167|  10,663|
| |Lamar County|     2| 144.875|  0.000|   230| 16660.630| 279.402|  13,805|
| |Russell County|     2| 34.506|  2.465| 1,389| 23964.390| 349.989|  57,961|
| |Lawrence County|     2| 60.746|  8.678|   354| 10752.035| 130.170|  32,924|
| |Geneva County|     2| 76.130| 10.876|   265| 10087.168| 125.070|  26,271|
| |Cleburne County|     1| 67.069|  0.000|   129|  8651.911| 76.650|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,714| 225.085| N/A|63,942|  8396.966| N/A|7,614,893|
| |King County|   686| 304.512|  1.712|16,808|  7460.997| 68.614|2,252,782|
| |Yakima County|   211| 841.063|  0.569|10,389| 41411.391| 175.388| 250,873|
| |Snohomish County|   198| 240.852|  1.216| 5,532|  6729.248| 54.391| 822,083|
| |Pierce County|   143| 158.015|  2.210| 5,801|  6410.086| 82.243| 904,980|
| |Benton County|   117| 572.435|  4.194| 3,776| 18474.485| 144.681| 204,390|
| |Spokane County|    93| 177.889|  7.105| 4,561|  8724.211| 151.930| 522,798|
| |Franklin County|    49| 514.587|  3.001| 3,560| 37386.318| 279.047|  95,222|
| |Clark County|    43| 88.071|  0.293| 1,823|  3733.812| 45.645| 488,241|
| |Whatcom County|    39| 170.122|  0.623|   991|  4322.848| 31.158| 229,247|
| |Skagit County|    21| 162.532|  0.000|   891|  6896.018| 60.811| 129,205|
| |Kittitas County|    20| 417.232|  5.960|   394|  8219.464| 122.189|  47,935|
| |Grant County|    13| 133.015|  1.462| 1,562| 15982.319| 352.272|  97,733|
| |Thurston County|    11| 37.861|  0.492|   742|  2553.900| 45.728| 290,536|
| |Island County|    11| 129.197|  0.000|   249|  2924.560| 13.423|  85,141|
| |Chelan County|    10| 129.534|  0.000| 1,363| 17655.440| 320.133|  77,200|
| |Kitsap County|     7| 25.785|  1.579|   761|  2803.225| 45.782| 271,473|
| |Douglas County|     7| 161.183|  0.000|   965| 22220.175| 411.180|  43,429|
| |Cowlitz County|     5| 45.211|  0.000|   495|  4475.871| 54.253| 110,593|
| |Adams County|     5| 250.213|  7.149|   457| 22869.439| 357.447|  19,983|
| |Okanogan County|     5| 118.363| 10.145|   877| 20760.836| 317.889|  42,243|
| |Lewis County|     4| 49.562|  1.770|   229|  2837.424| 69.033|  80,707|
| |Klickitat County|     3| 133.779|  0.000|   118|  5261.984| 76.445|  22,425|
| |Walla Walla County|     3| 49.375|  0.000|   549|  9035.550| 209.254|  60,760|
| |Asotin County|     2| 88.566|  0.000|    28|  1239.926| 25.305|  22,582|
| |Pacific County|     2| 89.004|  0.000|    51|  2269.592| 63.574|  22,471|
| |Grays Harbor County|     2| 26.645|  1.903|   122|  1625.345| 39.967|  75,061|
| |Mason County|     1| 14.977|  0.000|   229|  3429.787| 115.539|  66,768|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 35.469|  12,083|
| |Stevens County|     1| 21.871|  0.000|   112|  2449.533| 56.239|  45,723|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Ferry County|     0|  0.000|  0.000|    23|  3015.602| 56.191|   7,627|
| |Pend Oreille County|     0|  0.000|  0.000|    44|  3206.062| 72.865|  13,724|
| |San Juan County|     0|  0.000|  0.000|    30|  1706.291|  8.125|  17,582|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Jefferson County|     0|  0.000|  0.000|    55|  1706.961|  4.434|  32,221|
| |Lincoln County|     0|  0.000|  0.000|    27|  2468.233| 156.713|  10,939|
| |Whitman County|     0|  0.000|  0.000|   110|  2195.433| 65.578|  50,104|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Clallam County|     0|  0.000|  0.000|   139|  1797.468| 79.436|  77,331|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,666| 295.409| N/A|61,708| 10941.849| N/A|5,639,632|
| |Hennepin County|   839| 662.799|  2.144|19,569| 15459.263| 154.838|1,265,843|
| |Ramsey County|   268| 486.989|  1.817| 7,717| 14022.725| 173.924| 550,321|
| |Anoka County|   115| 322.200|  0.800| 3,752| 10512.130| 136.885| 356,921|
| |Dakota County|   106| 247.074|  0.999| 4,507| 10505.313| 152.507| 429,021|
| |Washington County|    45| 171.468|  1.089| 2,163|  8241.884| 122.477| 262,440|
| |Clay County|    40| 622.840|  0.000|   788| 12269.939| 80.079|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,767| 11162.844| 119.128| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,909| 18059.910| 59.422| 161,075|
| |Scott County|    20| 134.216|  2.876| 1,590| 10670.210| 172.564| 149,013|
| |St. Louis County|    19| 95.444|  0.000|   573|  2878.384| 86.115| 199,070|
| |Winona County|    16| 316.932|  0.000|   264|  5229.380| 42.446|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   238|  3658.443| 54.899|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   347| 10124.292| 112.538|  34,274|
| |Itasca County|    12| 265.899|  0.000|   146|  3235.099| 37.986|  45,130|
| |Goodhue County|     9| 194.217|  3.083|   199|  4294.346| 67.822|  46,340|
| |Pipestone County|     9| 986.193|  0.000|   158| 17313.171| 234.808|   9,126|
| |Rice County|     8| 119.453|  0.000| 1,038| 15499.015| 76.791|  66,972|
| |Sherburne County|     8| 82.272|  1.469|   732|  7527.921| 110.186|  97,238|
| |Nobles County|     6| 277.405|  0.000| 1,768| 81742.106| 125.493|  21,629|
| |Blue Earth County|     5| 73.907|  0.000|   932| 13776.181| 154.148|  67,653|
| |Martin County|     5| 254.026|  0.000|   209| 10618.300| 36.289|  19,683|
| |Renville County|     5| 343.690|  0.000|    66|  4536.706| 58.918|  14,548|
| |Wright County|     5| 36.133|  0.000|   897|  6482.291| 79.493| 138,377|
| |Polk County|     4| 127.535|  4.555|   155|  4941.972| 91.096|  31,364|
| |Carver County|     3| 28.547|  1.359|   878|  8354.823| 116.908| 105,089|
| |Mille Lacs County|     3| 114.168|  0.000|    72|  2740.039| 21.746|  26,277|
| |Lyon County|     3| 117.767|  0.000|   425| 16683.677| 50.472|  25,474|
| |Wilkin County|     3| 483.325|  0.000|    34|  5477.686| 138.093|   6,207|
| |Koochiching County|     3| 245.319|  0.000|    79|  6460.054| 58.409|  12,229|
| |Grant County|     3| 502.344| 47.842|    56|  9377.093| 119.606|   5,972|
| |Benton County|     3| 73.369|  0.000|   320|  7826.066| 34.938|  40,889|
| |Otter Tail County|     3| 51.067|  0.000|   198|  3370.442| 46.204|  58,746|
| |Mower County|     2| 49.923|  0.000| 1,105| 27582.248| 74.884|  40,062|
| |Todd County|     2| 81.090|  0.000|   429| 17393.772| 52.129|  24,664|
| |Steele County|     2| 54.572|  3.898|   351|  9577.342| 70.164|  36,649|
| |Sibley County|     2| 134.544|  0.000|    84|  5650.858| 38.441|  14,865|
| |Meeker County|     2| 86.125|  0.000|    87|  3746.447| 24.607|  23,222|
| |Brown County|     2| 79.974|  0.000|    89|  3558.861| 22.850|  25,008|
| |Cass County|     2| 67.161|  0.000|    74|  2484.973| 57.567|  29,779|
| |Freeborn County|     1| 33.024|  0.000|   360| 11888.643| 23.589|  30,281|
| |Swift County|     1| 107.921|  0.000|    55|  5935.679| 46.252|   9,266|
| |Kanabec County|     1| 61.211|  0.000|    37|  2264.798| 78.700|  16,337|
| |Kandiyohi County|     1| 23.149|  0.000|   702| 16250.376| 82.674|  43,199|
| |Le Sueur County|     1| 34.618|  0.000|   226|  7823.588| 118.689|  28,887|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 77.541|   5,527|
| |Murray County|     1| 122.041|  0.000|   124| 15133.024| 34.869|   8,194|
| |Morrison County|     1| 29.953|  0.000|    93|  2785.599| 47.068|  33,386|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 20.236|  14,119|
| |Chippewa County|     1| 84.746|  0.000|   107|  9067.797| 96.852|  11,800|
| |Becker County|     1| 29.050|  0.000|   161|  4677.105| 58.101|  34,423|
| |Aitkin County|     1| 62.949|  8.993|    41|  2580.889| 125.897|  15,886|
| |Douglas County|     1| 26.219|  3.746|   144|  3775.465| 44.946|  38,141|
| |Chisago County|     1| 17.674|  0.000|   204|  3605.578| 55.548|  56,579|
| |Rock County|     0|  0.000|  0.000|    85|  9125.067| 153.362|   9,315|
| |Roseau County|     0|  0.000|  0.000|    52|  3428.948| 56.521|  15,165|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 29.140|   9,805|
| |Wabasha County|     0|  0.000|  0.000|    93|  4300.180| 72.660|  21,627|
| |Traverse County|     0|  0.000|  0.000|    11|  3375.268| 43.835|   3,259|
| |Yellow Medicine County|     0|  0.000|  0.000|    52|  5355.855| 44.142|   9,709|
| |Watonwan County|     0|  0.000|  0.000|   323| 29641.186| 314.634|  10,897|
| |Waseca County|     0|  0.000|  0.000|   149|  8005.588| 145.835|  18,612|
| |Wadena County|     0|  0.000|  0.000|    27|  1973.396| 41.765|  13,682|
| |Cottonwood County|     0|  0.000|  0.000|   178| 15898.535| 63.798|  11,196|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Carlton County|     0|  0.000|  0.000|   142|  3958.630| 63.720|  35,871|
| |Lake of the Woods County|     0|  0.000|  0.000|     4|  1069.519| 114.591|   3,740|
| |Lake County|     0|  0.000|  0.000|    21|  1973.499| 40.275|  10,641|
| |Lac qui Parle County|     0|  0.000|  0.000|     8|  1207.912| 43.140|   6,623|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    79|  8023.563| 130.582|   9,846|
| |Isanti County|     0|  0.000|  0.000|   129|  3177.653| 66.861|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    35|  1628.589| 19.942|  21,491|
| |Houston County|     0|  0.000|  0.000|    42|  2258.065| 23.041|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    67|  3180.329| 40.687|  21,067|
| |McLeod County|     0|  0.000|  0.000|   202|  5627.838| 246.765|  35,893|
| |Lincoln County|     0|  0.000|  0.000|    58| 10285.512| 101.335|   5,639|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255|  0.000|   9,336|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   244|  5170.806| 133.206|  47,188|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510| 67.227|   6,375|
| |Cook County|     0|  0.000|  0.000|     5|   915.248| 78.450|   5,463|
| |Dodge County|     0|  0.000|  0.000|   129|  6162.224| 40.945|  20,934|
| |Faribault County|     0|  0.000|  0.000|    89|  6518.714| 52.317|  13,653|
| |Redwood County|     0|  0.000|  0.000|    36|  2373.105| 37.668|  15,170|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 140.919|   4,055|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 38.099|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202|  4.830|  29,579|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,282| 208.882| N/A|54,555|  8888.903| N/A|6,137,428|
| |St. Louis County|   849| 853.949|  3.880|20,579| 20698.950| 294.708| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,226| 10511.863| 169.500| 402,022|
| |Jackson County|    66| 93.882|  1.422| 4,155|  5910.292| 104.855| 703,011|
| |Jasper County|    31| 255.506|  4.710| 1,780| 14670.975| 123.632| 121,328|
| |Jefferson County|    26| 115.514|  1.269| 1,663|  7388.451| 149.153| 225,081|
| |Clay County|    20| 80.017|  0.000| 1,064|  4256.885| 68.586| 249,948|
| |Franklin County|    18| 173.132|  0.000|   642|  6175.036| 120.917| 103,967|
| |Scott County|    13| 339.603|  0.000|   406| 10606.061| 186.595|  38,280|
| |Platte County|    10| 95.769|  0.000|   373|  3572.181| 61.566| 104,418|
| |Greene County|    10| 34.120|  0.000| 1,621|  5530.800| 155.976| 293,086|
| |Buchanan County|    10| 114.464|  0.000| 1,092| 12499.428| 47.421|  87,364|
| |Cass County|     9| 85.082|  0.000|   770|  7279.259| 131.000| 105,780|
| |Gentry County|     9| 1369.655|  0.000|    85| 12935.626| 65.222|   6,571|
| |Pemiscot County|     9| 569.440|  9.039|   237| 14995.255| 153.658|  15,805|
| |Stoddard County|     9| 310.078|  0.000|   232|  7993.109| 98.437|  29,025|
| |Saline County|     7| 307.544|  0.000|   441| 19375.247| 156.910|  22,761|
| |McDonald County|     7| 306.520|  0.000|   953| 41730.525| 81.322|  22,837|
| |Newton County|     6| 103.029|  0.000|   886| 15213.957| 142.278|  58,236|
| |Camden County|     5| 107.980|  0.000|   363|  7839.326| 141.916|  46,305|
| |Cape Girardeau County|     5| 63.395|  1.811|   668|  8469.526| 99.620|  78,871|
| |Barry County|     4| 111.766|  7.983|   263|  7348.627| 119.749|  35,789|
| |Perry County|     4| 209.030|  0.000|   235| 12280.518| 179.169|  19,136|
| |Dunklin County|     4| 137.311|  0.000|   319| 10950.534| 255.006|  29,131|
| |Pettis County|     4| 94.476|  3.374|   560| 13226.576| 371.154|  42,339|
| |Henry County|     3| 137.463|  0.000|    84|  3848.974| 72.005|  21,824|
| |Boone County|     3| 16.624|  0.000| 1,429|  7918.521| 134.574| 180,463|
| |Cole County|     3| 39.090|  0.000|   438|  5707.212| 186.145|  76,745|
| |Taney County|     3| 53.640|  0.000|   632| 11300.243| 388.254|  55,928|
| |New Madrid County|     2| 117.123|  8.366|   259| 15167.487| 493.592|  17,076|
| |Johnson County|     2| 36.995|  0.000|   494|  9137.657| 55.492|  54,062|
| |Moniteau County|     2| 123.977|  0.000|   151|  9360.278| 185.966|  16,132|
| |Lafayette County|     2| 61.147|  0.000|   180|  5503.241| 69.882|  32,708|
| |Lawrence County|     2| 52.144|  0.000|   233|  6074.827| 141.535|  38,355|
| |Douglas County|     2| 151.688|  0.000|    89|  6750.095| 65.009|  13,185|
| |Butler County|     2| 47.083|  0.000|   286|  6732.897| 124.434|  42,478|
| |St. Francois County|     2| 29.755|  0.000|   392|  5832.032| 153.027|  67,215|
| |Howell County|     2| 49.854|  0.000|   157|  3913.553| 53.415|  40,117|
| |Webster County|     1| 25.258|  0.000|   138|  3485.553| 54.123|  39,592|
| |Stone County|     1| 31.297|  0.000|   138|  4318.978| 192.253|  31,952|
| |Shannon County|     1| 122.459|  0.000|    43|  5265.736|  0.000|   8,166|
| |Scotland County|     1| 203.998|  0.000|    15|  3059.976| 87.428|   4,902|
| |Ste. Genevieve County|     1| 55.885|  0.000|    57|  3185.425| 71.852|  17,894|
| |Washington County|     1| 40.437|  0.000|    87|  3517.994| 155.970|  24,730|
| |Caldwell County|     1| 110.865|  0.000|    35|  3880.266| 15.838|   9,020|
| |Christian County|     1| 11.287|  0.000|   373|  4210.170| 117.711|  88,595|
| |Carter County|     1| 167.168|  0.000|    22|  3677.700| 23.881|   5,982|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Callaway County|     1| 22.350|  0.000|   161|  3598.328| 95.785|  44,743|
| |Bollinger County|     1| 82.420| 11.774|    69|  5686.969| 129.517|  12,133|
| |Audrain County|     1| 39.389|  0.000|   205|  8074.681| 61.897|  25,388|
| |Randolph County|     1| 40.407|  0.000|    73|  2949.733| 92.360|  24,748|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313| 30.421|   4,696|
| |Miller County|     1| 39.034|  5.576|   135|  5269.527| 156.134|  25,619|
| |Pulaski County|     1| 19.009|  0.000|   230|  4372.042| 116.769|  52,607|
| |Pike County|     1| 54.639|  0.000|   110|  6010.272| 249.778|  18,302|
| |Osage County|     1| 73.448|  0.000|    52|  3819.317| 73.448|  13,615|
| |Marion County|     1| 35.051|  0.000|   204|  7150.368| 220.319|  28,530|
| |Grundy County|     1| 101.523|  0.000|    29|  2944.162| 58.013|   9,850|
| |Linn County|     1| 83.893|  0.000|    33|  2768.456| 35.954|  11,920|
| |Bates County|     1| 61.835|  0.000|    48|  2968.093| 70.669|  16,172|
| |Lincoln County|     1| 16.945|  0.000|   398|  6744.277| 162.192|  59,013|
| |Lewis County|     1| 102.291|  0.000|    48|  4909.984| 204.583|   9,776|
| |Benton County|     1| 51.432|  0.000|   107|  5503.266| 235.120|  19,443|
| |Dallas County|     1| 59.249|  0.000|    68|  4028.913| 135.426|  16,878|
| |Laclede County|     1| 27.993|  0.000|   203|  5682.613| 15.996|  35,723|
| |DeKalb County|     1| 79.700|  0.000|    36|  2869.212| 11.386|  12,547|
| |Andrew County|     1| 56.459|  0.000|    88|  4968.383| 24.197|  17,712|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Gasconade County|     0|  0.000|  0.000|    26|  1767.986| 48.571|  14,706|
| |Maries County|     0|  0.000|  0.000|    24|  2759.572| 114.982|   8,697|
| |Mississippi County|     0|  0.000|  0.000|   141| 10698.027| 108.389|  13,180|
| |Phelps County|     0|  0.000|  0.000|    90|  2019.160| 44.870|  44,573|
| |Ozark County|     0|  0.000|  0.000|    15|  1635.056| 109.004|   9,174|
| |Oregon County|     0|  0.000|  0.000|    16|  1519.612| 27.136|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   186|  8419.337| 135.796|  22,092|
| |Morgan County|     0|  0.000|  0.000|    87|  4217.773| 110.812|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    41|  3549.476| 12.368|  11,551|
| |Monroe County|     0|  0.000|  0.000|    31|  3586.303| 148.741|   8,644|
| |Mercer County|     0|  0.000|  0.000|    11|  3041.194| 39.496|   3,617|
| |Holt County|     0|  0.000|  0.000|     8|  1816.943| 64.891|   4,403|
| |Madison County|     0|  0.000|  0.000|    25|  2068.167| 94.545|  12,088|
| |Macon County|     0|  0.000|  0.000|    60|  3969.041| 56.701|  15,117|
| |Livingston County|     0|  0.000|  0.000|    63|  4137.388| 93.818|  15,227|
| |Knox County|     0|  0.000|  0.000|    27|  6819.904| 288.673|   3,959|
| |Iron County|     0|  0.000|  0.000|    22|  2172.840| 28.219|  10,125|
| |Howard County|     0|  0.000|  0.000|    53|  5299.470| 85.706|  10,001|
| |Hickory County|     0|  0.000|  0.000|    34|  3562.448| 254.461|   9,544|
| |Dent County|     0|  0.000|  0.000|    12|   770.564| 27.520|  15,573|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    62|  3390.016| 31.244|  18,289|
| |Clinton County|     0|  0.000|  0.000|    85|  4169.324| 140.145|  20,387|
| |Ripley County|     0|  0.000|  0.000|    54|  4063.817| 86.007|  13,288|
| |Ralls County|     0|  0.000|  0.000|    34|  3298.089| 124.718|  10,309|
| |Polk County|     0|  0.000|  0.000|   213|  6625.400| 84.428|  32,149|
| |Daviess County|     0|  0.000|  0.000|    17|  2053.636|  0.000|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865|  0.000|   7,561|
| |Crawford County|     0|  0.000|  0.000|    79|  3302.676| 125.418|  23,920|
| |Cooper County|     0|  0.000|  0.000|   135|  7623.242| 258.142|  17,709|
| |Clark County|     0|  0.000|  0.000|    21|  3089.598| 147.124|   6,797|
| |Chariton County|     0|  0.000|  0.000|    20|  2693.240| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    41|  2857.342| 59.735|  14,349|
| |Carroll County|     0|  0.000|  0.000|   101| 11637.285| 32.920|   8,679|
| |Barton County|     0|  0.000|  0.000|    70|  5955.419| 48.616|  11,754|
| |Atchison County|     0|  0.000|  0.000|    19|  3694.342| 194.439|   5,143|
| |Adair County|     0|  0.000|  0.000|   161|  6352.839| 135.287|  25,343|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    60|  4660.918| 177.559|  12,873|
| |Warren County|     0|  0.000|  0.000|   208|  5834.666| 112.205|  35,649|
| |Vernon County|     0|  0.000|  0.000|    54|  2626.076| 48.631|  20,563|
| |Texas County|     0|  0.000|  0.000|    57|  2244.271| 78.746|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   145| 23813.434| 187.692|   6,089|
| |Shelby County|     0|  0.000|  0.000|    38|  6408.094| 192.725|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    11|  2360.515| 61.312|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    24|  2554.007| 76.012|   9,397|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867| 99.301|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,252| 183.331| N/A|118,846| 17402.690| N/A|6,829,174|
| |Shelby County|   314| 335.053|  3.201|23,625| 25208.981| 289.170| 937,166|
| |Davidson County|   219| 315.496|  2.881|20,865| 30058.605| 267.956| 694,144|
| |Sumner County|    73| 381.633|  2.241| 3,473| 18156.344| 189.696| 191,283|
| |Rutherford County|    55| 165.521|  0.860| 6,629| 19949.742| 203.784| 332,285|
| |Hamilton County|    55| 149.536|  3.107| 6,315| 17169.471| 231.101| 367,804|
| |Knox County|    40| 85.050|  0.911| 4,750| 10099.657| 195.007| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,607| 15129.272| 179.162| 238,412|
| |Wilson County|    23| 158.997|  0.988| 2,339| 16169.283| 234.051| 144,657|
| |McMinn County|    20| 371.789|  0.000|   559| 10391.493| 175.272|  53,794|
| |Robertson County|    20| 278.501|  1.989| 1,578| 21973.737| 236.726|  71,813|
| |Madison County|    20| 204.115| 10.206| 1,189| 12134.634| 379.071|  97,984|
| |Hardeman County|    18| 718.563| 39.920|   942| 37604.790| 638.723|  25,050|
| |Putnam County|    18| 224.313|  8.901| 1,800| 22431.304| 354.272|  80,245|
| |Hamblen County|    16| 246.404|  6.600| 1,420| 21868.359| 270.604|  64,934|
| |Bradley County|    15| 138.748|  6.607| 1,991| 18416.428| 332.994| 108,110|
| |Sullivan County|    15| 94.728|  5.413| 1,048|  6618.334| 193.967| 158,348|
| |Montgomery County|    14| 66.988|  1.367| 1,986|  9502.711| 159.951| 208,993|
| |Giles County|    13| 441.216| 14.546|   387| 13134.673| 160.002|  29,464|
| |Macon County|    13| 528.412|  0.000|   867| 35241.037| 150.975|  24,602|
| |Blount County|    12| 90.166|  5.367| 1,324|  9948.305| 153.497| 133,088|
| |Bedford County|    11| 221.270|  0.000|   930| 18707.380| 152.303|  49,713|
| |Tipton County|    10| 162.340|  2.319| 1,217| 19756.814| 218.000|  61,599|
| |Lauderdale County|     9| 351.110| 16.720|   522| 20364.374| 468.147|  25,633|
| |Greene County|     9| 130.304|  8.273|   504|  7297.051| 264.746|  69,069|
| |Hawkins County|     9| 158.490| 12.579|   485|  8540.838| 291.822|  56,786|
| |Monroe County|     9| 193.361|  0.000|   451|  9689.548| 227.123|  46,545|
| |Sevier County|     9| 91.603|  5.816| 1,902| 19358.779| 212.286|  98,250|
| |Hardin County|     8| 311.867|  5.569|   479| 18673.008| 389.833|  25,652|
| |Fayette County|     8| 194.491|  0.000|   704| 17115.212| 215.329|  41,133|
| |Dyer County|     8| 215.291|  3.844|   668| 17976.802| 384.448|  37,159|
| |Cheatham County|     8| 196.720|  7.026|   601| 14778.567| 186.181|  40,667|
| |Gibson County|     7| 142.470| 14.538|   735| 14959.396| 421.596|  49,133|
| |Haywood County|     7| 404.531| 16.511|   510| 29472.954| 891.619|  17,304|
| |Maury County|     7| 72.624|  0.000| 1,284| 13321.299| 289.013|  96,387|
| |Lawrence County|     7| 158.579|  3.236|   584| 13230.030| 300.977|  44,142|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 88.621|  11,284|
| |Anderson County|     6| 77.944|  0.000|   698|  9067.526| 126.196|  76,978|
| |Carter County|     6| 106.400|  2.533|   532|  9434.130| 250.800|  56,391|
| |Cumberland County|     6| 99.141|  0.000|   463|  7650.364| 184.119|  60,520|
| |McNairy County|     6| 233.518|  5.560|   388| 15100.802| 355.836|  25,694|
| |Marion County|     5| 172.968|  4.942|   228|  7887.363| 93.897|  28,907|
| |Crockett County|     5| 351.370| 10.039|   274| 19255.095| 381.488|  14,230|
| |White County|     5| 182.849| 10.449|   294| 10751.509| 464.958|  27,345|
| |Smith County|     4| 198.442|  7.087|   458| 22721.635| 524.454|  20,157|
| |Marshall County|     4| 116.364|  8.312|   305|  8872.727| 162.078|  34,375|
| |Cocke County|     4| 111.099| 11.903|   482| 13387.401| 277.747|  36,004|
| |Franklin County|     4| 94.769|  0.000|   338|  8007.961| 175.999|  42,208|
| |Obion County|     4| 133.027|  0.000|   588| 19555.023| 641.382|  30,069|
| |Jefferson County|     4| 73.401|  2.621|   587| 10771.630| 207.096|  54,495|
| |Weakley County|     4| 120.019|  4.286|   482| 14462.314| 737.261|  33,328|
| |Warren County|     4| 96.906|  0.000|   540| 13082.346| 384.164|  41,277|
| |Loudon County|     3| 55.486|  0.000|   754| 13945.402| 190.237|  54,068|
| |Humphreys County|     3| 161.447|  0.000|   129|  6942.202| 153.759|  18,582|
| |Henderson County|     3| 106.697| 15.242|   613| 21801.757| 731.637|  28,117|
| |Decatur County|     3| 257.224| 12.249|   215| 18434.365| 563.442|  11,663|
| |Polk County|     3| 178.232|  0.000|   213| 12654.468| 288.566|  16,832|
| |Carroll County|     3| 108.042|  0.000|   330| 11884.611| 442.457|  27,767|
| |Coffee County|     3| 53.079|  2.528|   558|  9872.611| 346.274|  56,520|
| |Washington County|     2| 15.459|  0.000| 1,291|  9978.744| 223.050| 129,375|
| |Hancock County|     2| 302.115| 21.580|    81| 12235.650| 107.898|   6,620|
| |Wayne County|     2| 119.954|  8.568|   229| 13734.781| 85.682|  16,673|
| |Grundy County|     2| 148.954|  0.000|   118|  8788.262| 170.233|  13,427|
| |Dickson County|     2| 37.073|  2.648|   705| 13068.140| 254.213|  53,948|
| |DeKalb County|     2| 97.609|  6.972|   366| 17862.372| 306.770|  20,490|
| |Chester County|     2| 115.627|  0.000|   225| 13008.036| 239.513|  17,297|
| |Bledsoe County|     2| 132.767|  9.483|   716| 47530.536| 398.301|  15,064|
| |Rhea County|     2| 60.301|  4.307|   544| 16401.845| 142.138|  33,167|
| |Roane County|     2| 37.466|  0.000|   488|  9141.658| 256.908|  53,382|
| |Pickett County|     1| 198.098|  0.000|    39|  7725.832| 396.197|   5,048|
| |Overton County|     1| 44.962|  0.000|   209|  9397.059| 449.620|  22,241|
| |Morgan County|     1| 46.722|  0.000|   127|  5933.748| 240.287|  21,403|
| |Scott County|     1| 45.314|  6.473|   124|  5618.996| 122.996|  22,068|
| |Jackson County|     1| 84.846|  0.000|   130| 11030.036| 266.660|  11,786|
| |Lincoln County|     1| 29.099|  0.000|   315|  9166.036| 249.416|  34,366|
| |Sequatchie County|     1| 66.551|  9.507|   113|  7520.298| 161.625|  15,026|
| |Lewis County|     1| 81.513|  0.000|    74|  6031.953| 186.315|  12,268|
| |Benton County|     1| 61.881|  0.000|   158|  9777.228| 442.008|  16,160|
| |Campbell County|     1| 25.099|  0.000|   254|  6375.182| 118.325|  39,842|
| |Henry County|     0|  0.000|  0.000|   299|  9244.087| 326.833|  32,345|
| |Houston County|     0|  0.000|  0.000|    61|  7438.117| 121.936|   8,201|
| |Hickman County|     0|  0.000|  0.000|   272| 10803.082| 221.282|  25,178|
| |Grainger County|     0|  0.000|  0.000|   204|  8747.856| 153.149|  23,320|
| |Fentress County|     0|  0.000|  0.000|    96|  5182.746| 154.248|  18,523|
| |Clay County|     0|  0.000|  0.000|    79| 10374.261| 281.399|   7,615|
| |Claiborne County|     0|  0.000|  0.000|   277|  8667.355| 187.741|  31,959|
| |Cannon County|     0|  0.000|  0.000|   154| 10491.893| 272.517|  14,678|
| |Lake County|     0|  0.000|  0.000|   794| 113169.897| 773.742|   7,016|
| |Van Buren County|     0|  0.000|  0.000|    36|  6130.790| 72.986|   5,872|
| |Union County|     0|  0.000|  0.000|   162|  8111.356| 236.045|  19,972|
| |Unicoi County|     0|  0.000|  0.000|   168|  9394.397| 231.665|  17,883|
| |Stewart County|     0|  0.000|  0.000|    79|  5760.117| 93.745|  13,715|
| |Perry County|     0|  0.000|  0.000|    81| 10029.718| 123.824|   8,076|
| |Moore County|     0|  0.000|  0.000|    60|  9247.842| 352.299|   6,488|
| |Meigs County|     0|  0.000|  0.000|   108|  8694.252| 103.503|  12,422|
| |Johnson County|     0|  0.000|  0.000|   288| 16190.690| 891.452|  17,788|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,006| 172.780| N/A|61,785| 10611.541| N/A|5,822,434|
| |Milwaukee County|   458| 484.284|  1.662|21,331| 22555.159| 200.602| 945,726|
| |Racine County|    79| 402.423|  1.455| 3,567| 18170.148| 186.293| 196,311|
| |Kenosha County|    60| 353.855|  1.685| 2,692| 15876.292| 147.440| 169,561|
| |Waukesha County|    59| 145.968|  0.707| 4,354| 10771.948| 208.172| 404,198|
| |Brown County|    54| 204.126|  1.080| 4,340| 16405.713| 149.585| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,578|  8373.956| 82.313| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,444|  8839.698| 60.342| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,359| 13083.914| 129.285| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,108|  8145.023| 204.781| 136,034|
| |Winnebago County|    18| 104.708|  0.000| 1,212|  7050.324| 108.032| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   716|  8025.017| 198.544|  89,221|
| |Waupaca County|    15| 294.175|  0.000|   473|  9276.329| 226.935|  50,990|
| |Grant County|    15| 291.608|  2.777|   362|  7037.462| 86.094|  51,439|
| |Outagamie County|    14| 74.514|  0.760| 1,299|  6913.804| 126.977| 187,885|
| |Marathon County|    10| 73.696|  3.158|   662|  4878.696| 76.855| 135,692|
| |Clark County|     8| 230.057|  4.108|   189|  5435.095| 41.082|  34,774|
| |Sheboygan County|     8| 69.360|  2.477|   776|  6727.935| 173.400| 115,340|
| |Fond du Lac County|     7| 67.696|  1.382|   676|  6537.528| 142.300| 103,403|
| |St. Croix County|     5| 55.135|  4.726|   512|  5645.793| 86.640|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   647|  7632.507| 124.709|  84,769|
| |Dodge County|     5| 56.922|  0.000|   845|  9619.873| 190.283|  87,839|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 41.403|  17,252|
| |Marinette County|     4| 99.133|  3.540|   432| 10706.320| 318.640|  40,350|
| |Eau Claire County|     4| 38.224|  1.365|   596|  5695.392| 107.847| 104,646|
| |Forest County|     4| 444.247|  0.000|    60|  6663.705| 15.866|   9,004|
| |Sauk County|     3| 46.553|  0.000|   452|  7014.059| 104.191|  64,442|
| |Pierce County|     3| 70.169| 10.024|   224|  5239.276| 153.703|  42,754|
| |Barron County|     3| 66.307|  0.000|   296|  6542.304| 101.039|  45,244|
| |Door County|     3| 108.429|  0.000|   107|  3867.284| 82.612|  27,668|
| |Adams County|     2| 98.912|  0.000|    86|  4253.215| 70.651|  20,220|
| |Monroe County|     2| 43.240|  3.089|   245|  5296.954| 49.418|  46,253|
| |Wood County|     2| 27.398|  1.957|   322|  4411.019| 131.117|  72,999|
| |Calumet County|     2| 39.929|  0.000|   334|  6668.131| 193.941|  50,089|
| |Columbia County|     2| 34.763|  2.483|   255|  4432.316| 67.043|  57,532|
| |Buffalo County|     2| 153.480|  0.000|    44|  3376.564| 21.926|  13,031|
| |Polk County|     2| 45.680|  0.000|   137|  3129.068| 39.154|  43,783|
| |Kewaunee County|     2| 97.876|  0.000|   135|  6606.636| 167.788|  20,434|
| |Trempealeau County|     2| 67.456|  0.000|   345| 11636.143| 154.185|  29,649|
| |Ashland County|     1| 64.259|  9.180|    26|  1670.736| 55.079|  15,562|
| |Bayfield County|     1| 66.507|  0.000|    29|  1928.704| 76.008|  15,036|
| |Burnett County|     1| 64.876|  0.000|    22|  1427.274| 27.804|  15,414|
| |Langlade County|     1| 52.113|  0.000|    63|  3283.131| 89.337|  19,189|
| |Jackson County|     1| 48.443|  0.000|    58|  2809.669| 62.283|  20,643|
| |Juneau County|     1| 37.471|  0.000|   138|  5171.057| 48.178|  26,687|
| |Iron County|     1| 175.840|  0.000|    76| 13363.812| 100.480|   5,687|
| |La Crosse County|     1|  8.473|  0.000|   921|  7804.027| 102.892| 118,016|
| |Green County|     1| 27.056|  0.000|   169|  4572.511| 146.877|  36,960|
| |Marquette County|     1| 64.210|  0.000|    80|  5136.766| 82.555|  15,574|
| |Rusk County|     1| 70.532|  0.000|    21|  1481.168| 50.380|  14,178|
| |Manitowoc County|     1| 12.661|  0.000|   351|  4444.107| 72.350|  78,981|
| |Taylor County|     1| 49.157|  7.022|    71|  3490.144| 112.359|  20,343|
| |Waushara County|     1| 40.912|  5.845|   120|  4909.381| 64.290|  24,443|
| |Washburn County|     0|  0.000|  0.000|    47|  2989.822| 81.788|  15,720|
| |Florence County|     0|  0.000|  0.000|     8|  1862.631| 33.261|   4,295|
| |Price County|     0|  0.000|  0.000|    33|  2471.725| 117.701|  13,351|
| |Portage County|     0|  0.000|  0.000|   426|  6019.330| 137.262|  70,772|
| |Sawyer County|     0|  0.000|  0.000|    76|  4589.926| 284.713|  16,558|
| |Vernon County|     0|  0.000|  0.000|    66|  2141.328| 27.809|  30,822|
| |Vilas County|     0|  0.000|  0.000|    60|  2703.312| 135.166|  22,195|
| |Oneida County|     0|  0.000|  0.000|   153|  4298.357| 240.804|  35,595|
| |Oconto County|     0|  0.000|  0.000|   259|  6828.368| 256.111|  37,930|
| |Lafayette County|     0|  0.000|  0.000|   147|  8820.882| 300.030|  16,665|
| |Green Lake County|     0|  0.000|  0.000|    57|  3013.800| 30.214|  18,913|
| |Menominee County|     0|  0.000|  0.000|    25|  5487.270| 125.423|   4,556|
| |Iowa County|     0|  0.000|  0.000|    83|  3505.364| 108.600|  23,678|
| |Lincoln County|     0|  0.000|  0.000|    69|  2500.634| 20.709|  27,593|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689| 19.604|   7,287|
| |Shawano County|     0|  0.000|  0.000|   204|  4987.897| 143.210|  40,899|
| |Dunn County|     0|  0.000|  0.000|   128|  2821.372| 66.126|  45,368|
| |Douglas County|     0|  0.000|  0.000|   191|  4426.419| 172.157|  43,150|
| |Crawford County|     0|  0.000|  0.000|    76|  4711.425| 97.417|  16,131|
| |Chippewa County|     0|  0.000|  0.000|   241|  3727.304| 64.073|  64,658|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   973| 315.893| N/A|57,163| 18558.476| N/A|3,080,156|
| |Clark County|   828| 365.286|  7.059|49,646| 21902.180| 292.998|2,266,715|
| |Washoe County|   120| 254.497|  1.515| 5,835| 12374.899| 141.185| 471,519|
| |Nye County|     9| 193.453|  0.000|   408|  8769.856| 141.251|  46,523|
| |Lyon County|     6| 104.330|  2.484|   235|  4086.246| 64.585|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074| 67.902|  16,831|
| |Elko County|     2| 37.895|  0.000|   555| 10515.745| 167.819|  52,778|
| |Churchill County|     1| 40.146|  0.000|    69|  2770.083| 114.703|  24,909|
| |Douglas County|     1| 20.448|  2.921|   206|  4212.248| 67.186|  48,905|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 25.824|   5,532|
| |White Pine County|     1| 104.384|  0.000|    15|  1565.762| 14.912|   9,580|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     5|  1212.709| 34.649|   4,123|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Eureka County|     0|  0.000|  0.000|     4|  1971.414| 140.815|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   946| 299.835| N/A|49,520| 15695.373| N/A|3,155,070|
| |Polk County|   208| 424.350|  1.457|10,444| 21307.285| 193.231| 490,161|
| |Linn County|    88| 388.168|  0.630| 2,428| 10709.906| 178.330| 226,706|
| |Black Hawk County|    66| 502.941|  4.354| 3,157| 24057.366| 146.963| 131,228|
| |Woodbury County|    52| 504.330|  1.386| 3,734| 36214.806| 108.071| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   851| 19946.559| 70.317|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,898| 20309.674| 155.923|  93,453|
| |Wapello County|    33| 943.693|  4.085|   905| 25880.065| 224.689|  34,969|
| |Dubuque County|    31| 318.566|  2.936| 1,698| 17449.209| 218.739|  97,311|
| |Tama County|    29| 1720.660|  0.000|   554| 32870.535| 127.142|  16,854|
| |Pottawattamie County|    28| 300.410|  7.664| 1,332| 14290.925| 160.934|  93,206|
| |Jasper County|    27| 726.099|  7.684|   481| 12935.323| 88.361|  37,185|
| |Marshall County|    26| 660.418|  7.257| 1,450| 36831.009| 203.206|  39,369|
| |Johnson County|    19| 125.711|  3.781| 2,118| 14013.497| 150.286| 151,140|
| |Mahaska County|    17| 769.405|  0.000|   142|  6426.793| 38.794|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   634| 14935.218| 185.092|  42,450|
| |Story County|    15| 154.453|  1.471| 1,173| 12078.215| 82.375|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Scott County|    14| 80.952|  1.652| 1,743| 10078.465| 105.733| 172,943|
| |Buena Vista County|    12| 611.621|  0.000| 1,794| 91437.309| 58.250|  19,620|
| |Franklin County|    12| 1191.658| 85.118|   245| 24329.692| 283.728|  10,070|
| |Plymouth County|    11| 436.907| 17.022|   470| 18667.832| 153.201|  25,177|
| |Washington County|    10| 455.270|  0.000|   305| 13885.727| 110.566|  21,965|
| |Poweshiek County|     8| 432.339|  0.000|   160|  8646.779| 77.203|  18,504|
| |Webster County|     8| 222.816|  7.958|   826| 23005.793| 358.098|  35,904|
| |Monroe County|     8| 1038.017| 18.536|    74|  9601.661| 129.752|   7,707|
| |Bremer County|     7| 279.307|  0.000|   230|  9177.240| 216.606|  25,062|
| |Guthrie County|     5| 467.771|  0.000|   135| 12629.806| 93.554|  10,689|
| |Lucas County|     4| 465.116|  0.000|    73|  8488.372| 382.060|   8,600|
| |Clinton County|     4| 86.153|  3.077|   416|  8959.917| 292.305|  46,429|
| |Dickinson County|     4| 231.777|  0.000|   384| 22250.550| 74.500|  17,258|
| |Emmet County|     4| 434.405| 31.029|   193| 20960.035| 186.174|   9,208|
| |Allamakee County|     4| 292.248|  0.000|   156| 11397.677| 62.625|  13,687|
| |O'Brien County|     4| 290.846| 31.162|   141| 10252.309| 103.873|  13,753|
| |Montgomery County|     4| 403.348| 14.405|    60|  6050.217| 216.079|   9,917|
| |Henry County|     4| 200.461|  7.159|   127|  6364.639| 93.071|  19,954|
| |Appanoose County|     3| 241.429|  0.000|    51|  4104.297| 91.973|  12,426|
| |Boone County|     3| 114.355|  5.445|   262|  9987.040| 168.810|  26,234|
| |Sioux County|     3| 86.071|  4.099|   643| 18447.855| 168.043|  34,855|
| |Lee County|     3| 89.135|  0.000|   118|  3505.957| 89.135|  33,657|
| |Crawford County|     3| 178.359|  0.000|   731| 43460.166| 84.933|  16,820|
| |Clayton County|     3| 170.950|  0.000|   106|  6040.230| 56.983|  17,549|
| |Clarke County|     3| 319.319|  0.000|   204| 21713.677| 243.291|   9,395|
| |Pocahontas County|     2| 302.160| 21.583|   117| 17676.386| 64.749|   6,619|
| |Madison County|     2| 122.414|  0.000|   125|  7650.875| 174.877|  16,338|
| |Lyon County|     2| 170.140| 24.306|   115|  9783.071| 109.376|  11,755|
| |Hancock County|     2| 188.147|  0.000|   121| 11382.879| 53.756|  10,630|
| |Floyd County|     2| 127.861|  0.000|   158| 10101.010| 246.589|  15,642|
| |Jones County|     2| 96.707|  0.000|   133|  6431.024| 62.169|  20,681|
| |Des Moines County|     2| 51.325|  0.000|   187|  4798.932| 175.973|  38,967|
| |Davis County|     2| 222.222| 15.873|    61|  6777.778| 174.603|   9,000|
| |Butler County|     2| 138.514|  0.000|   125|  8657.109| 98.938|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    86|  8895.325| 59.105|   9,668|
| |Carroll County|     2| 99.182|  7.084|   194|  9620.630| 85.013|  20,165|
| |Cedar County|     1| 53.686|  0.000|   134|  7193.858| 107.371|  18,627|
| |Buchanan County|     1| 47.226|  0.000|   129|  6092.090| 101.198|  21,175|
| |Audubon County|     1| 181.951|  0.000|    29|  5276.565| 25.993|   5,496|
| |Cass County|     1| 77.906|  0.000|    79|  6154.565| 345.012|  12,836|
| |Benton County|     1| 38.994|  0.000|   160|  6239.033| 83.558|  25,645|
| |Cherokee County|     1| 89.008|  0.000|   110|  9790.832| 152.584|  11,235|
| |Union County|     1| 81.693|  0.000|    78|  6372.028| 70.022|  12,241|
| |Van Buren County|     1| 141.965|  0.000|    36|  5110.733| 60.842|   7,044|
| |Warren County|     1| 19.430|  0.000|   572| 11114.134| 105.479|  51,466|
| |Wayne County|     1| 155.255|  0.000|    20|  3105.108| 44.359|   6,441|
| |Winneshiek County|     1| 50.023|  0.000|    97|  4852.183| 78.607|  19,991|
| |Wright County|     1| 79.605|  0.000|   475| 37812.450| 352.537|  12,562|
| |Shelby County|     1| 87.306|  0.000|   186| 16238.869| 212.028|  11,454|
| |Ringgold County|     1| 204.332|  0.000|    23|  4699.632| 58.381|   4,894|
| |Harrison County|     1| 71.179| 10.168|   110|  7829.739| 122.022|  14,049|
| |Hamilton County|     1| 67.691|  0.000|   251| 16990.456| 96.702|  14,773|
| |Clay County|     1| 62.438|  0.000|   201| 12549.950| 267.590|  16,016|
| |Delaware County|     1| 58.785|  0.000|   117|  6877.903| 218.346|  17,011|
| |Grundy County|     1| 81.753|  0.000|    80|  6540.222| 70.074|  12,232|
| |Humboldt County|     1| 104.624|  0.000|   118| 12345.679| 388.605|   9,558|
| |Iowa County|     1| 61.789|  0.000|    97|  5993.574| 61.789|  16,184|
| |Jackson County|     1| 51.443|  0.000|   156|  8025.104| 110.235|  19,439|
| |Keokuk County|     1| 97.599|  0.000|    37|  3611.165| 83.656|  10,246|
| |Adair County|     0|  0.000|  0.000|    30|  4194.631| 179.770|   7,152|
| |Page County|     0|  0.000|  0.000|    95|  6288.476| 179.671|  15,107|
| |Osceola County|     0|  0.000|  0.000|    84| 14098.691| 143.864|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972| 16.582|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    79|  7462.687| 40.485|  10,586|
| |Mills County|     0|  0.000|  0.000|    89|  5890.529| 56.731|  15,109|
| |Marion County|     0|  0.000|  0.000|   175|  5262.683| 85.921|  33,253|
| |Kossuth County|     0|  0.000|  0.000|    90|  6075.744| 115.728|  14,813|
| |Jefferson County|     0|  0.000|  0.000|    87|  4755.398| 78.085|  18,295|
| |Ida County|     0|  0.000|  0.000|    31|  4518.950| 41.649|   6,860|
| |Howard County|     0|  0.000|  0.000|    50|  5459.707| 15.599|   9,158|
| |Hardin County|     0|  0.000|  0.000|   184| 10922.474| 152.643|  16,846|
| |Greene County|     0|  0.000|  0.000|    43|  4837.984| 80.365|   8,888|
| |Fremont County|     0|  0.000|  0.000|    43|  6178.161| 164.204|   6,960|
| |Fayette County|     0|  0.000|  0.000|    85|  4325.700| 29.080|  19,650|
| |Decatur County|     0|  0.000|  0.000|    25|  3176.620| 54.456|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    55|  4609.067| 47.886|  11,933|
| |Adams County|     0|  0.000|  0.000|    16|  4441.977|  0.000|   3,602|
| |Palo Alto County|     0|  0.000|  0.000|    88|  9903.219| 128.613|   8,886|
| |Sac County|     0|  0.000|  0.000|    86|  8846.826| 73.479|   9,721|
| |Taylor County|     0|  0.000|  0.000|   100| 16337.200| 163.372|   6,121|
| |Winnebago County|     0|  0.000|  0.000|    86|  8305.969| 124.176|  10,354|
| |Worth County|     0|  0.000|  0.000|    67|  9077.361| 116.128|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   783| 175.259| N/A|35,793|  8011.553| N/A|4,467,673|
| |Jefferson County|   242| 315.615|  1.118| 8,279| 10797.423| 161.161| 766,757|
| |Fayette County|    47| 145.442|  0.442| 3,182|  9846.759| 146.327| 323,152|
| |Kenton County|    41| 245.512|  2.566| 1,431|  8568.965| 68.435| 166,998|
| |Hopkins County|    34| 760.865|  3.197|   428|  9577.944| 51.151|  44,686|
| |Graves County|    25| 670.853| 11.500|   560| 15027.102| 145.671|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,111|  8317.051| 67.375| 133,581|
| |Logan County|    23| 848.646|  5.271|   332| 12250.018| 152.862|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,670| 20090.898| 198.867| 132,896|
| |Shelby County|    21| 428.362|  0.000|   779| 15890.176| 171.927|  49,024|
| |Adair County|    19| 989.480|  0.000|   210| 10936.361| 52.078|  19,202|
| |Oldham County|    15| 224.554|  2.139|   633|  9476.190| 109.069|  66,799|
| |Butler County|    15| 1164.687|  0.000|   298| 23138.442| 22.185|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   150| 11253.657| 75.024|  13,329|
| |Campbell County|    13| 138.913|  0.000|   582|  6219.012| 61.060|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   108|  8888.889| 141.093|  12,150|
| |Muhlenberg County|    11| 359.219|  4.665|   627| 20475.475| 41.987|  30,622|
| |Grayson County|    11| 416.241|  0.000|   206|  7795.058| 108.115|  26,427|
| |Casey County|    10| 618.850|  0.000|   193| 11943.808| 344.788|  16,159|
| |Daviess County|     9| 88.660|  1.407|   769|  7575.534| 64.736| 101,511|
| |Ohio County|     9| 375.094| 11.908|   357| 14878.720| 95.262|  23,994|
| |Allen County|     8| 375.323|  0.000|   227| 10649.777| 67.022|  21,315|
| |Hardin County|     8| 72.099|  0.000|   655|  5903.135| 157.074| 110,958|
| |Knox County|     8| 256.863|  0.000|   243|  7802.215| 123.845|  31,145|
| |Christian County|     8| 113.538|  4.055|   511|  7252.239| 66.906|  70,461|
| |Gallatin County|     7| 789.266|  0.000|    81|  9132.935| 32.215|   8,869|
| |Clark County|     7| 193.034|  0.000|   166|  4577.669| 15.758|  36,263|
| |Simpson County|     7| 376.911|  0.000|   152|  8184.364| 76.921|  18,572|
| |Franklin County|     7| 137.279|  5.603|   323|  6334.451| 176.502|  50,991|
| |Grant County|     6| 239.339|  5.699|   124|  4946.348| 102.574|  25,069|
| |Clay County|     5| 251.244|  0.000|   157|  7889.051| 93.319|  19,901|
| |Laurel County|     5| 82.219|  2.349|   453|  7449.065| 143.296|  60,813|
| |Russell County|     5| 278.971|  0.000|   116|  6472.131| 127.530|  17,923|
| |Pulaski County|     5| 76.948|  6.596|   319|  4909.278| 123.117|  64,979|
| |Bullitt County|     5| 61.217|  1.749|   382|  4677.017| 111.941|  81,676|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686| 34.801|   8,210|
| |McCracken County|     4| 61.145|  0.000|   372|  5686.508| 61.145|  65,418|
| |Calloway County|     4| 102.561|  0.000|   254|  6512.654| 205.123|  39,001|
| |Bell County|     4| 153.657| 10.976|   318| 12215.734| 181.096|  26,032|
| |Pike County|     3| 51.835|  0.000|   251|  4336.858| 66.645|  57,876|
| |Boyd County|     3| 64.215|  0.000|   193|  4131.170| 42.810|  46,718|
| |Perry County|     3| 116.469|  0.000|   232|  9006.910| 216.299|  25,758|
| |Harlan County|     3| 115.340|  0.000|   232|  8919.646| 109.848|  26,010|
| |Henderson County|     3| 66.357|  0.000|   351|  7763.769| 72.677|  45,210|
| |Barren County|     2| 45.199|  0.000|   375|  8474.768| 106.540|  44,249|
| |Breckinridge County|     2| 97.671|  0.000|    75|  3662.646| 160.459|  20,477|
| |Carroll County|     2| 188.129|  0.000|   159| 14956.260| 188.129|  10,631|
| |Floyd County|     2| 56.197|  0.000|    96|  2697.463| 48.169|  35,589|
| |Fulton County|     2| 335.064| 23.933|    85| 14240.241| 550.463|   5,969|
| |Green County|     2| 182.799|  0.000|    38|  3473.174| 91.399|  10,941|
| |Henry County|     2| 124.023|  0.000|   129|  7999.504| 256.905|  16,126|
| |Lincoln County|     2| 81.470|  5.819|   116|  4725.243| 98.928|  24,549|
| |Marshall County|     2| 64.309|  0.000|   139|  4469.453| 50.528|  31,100|
| |Meade County|     2| 69.999|  0.000|    95|  3324.934| 20.000|  28,572|
| |Metcalfe County|     2| 198.590|  0.000|    61|  6056.995| 113.480|  10,071|
| |Monroe County|     2| 187.793|  0.000|    94|  8826.291| 67.069|  10,650|
| |Nelson County|     2| 43.259|  0.000|   221|  4780.135| 74.159|  46,233|
| |Taylor County|     2| 77.613|  0.000|   141|  5471.691| 205.119|  25,769|
| |Bourbon County|     1| 50.536|  0.000|    84|  4244.997| 93.852|  19,788|
| |Bath County|     1| 80.000|  0.000|    37|  2960.000| 11.429|  12,500|
| |Carlisle County|     1| 210.084|  0.000|    45|  9453.782| 390.156|   4,760|
| |Anderson County|     1| 43.962|  0.000|    87|  3824.680| 62.803|  22,747|
| |Whitley County|     1| 27.576|  0.000|   166|  4577.542| 70.909|  36,264|
| |Webster County|     1| 77.268|  0.000|    89|  6876.835| 66.230|  12,942|
| |Knott County|     1| 67.540|  0.000|    62|  4187.492| 144.729|  14,806|
| |Clinton County|     1| 97.867| 13.981|    37|  3621.061| 139.809|  10,218|
| |Crittenden County|     1| 113.559|  0.000|    32|  3633.886| 97.336|   8,806|
| |Greenup County|     1| 28.492|  0.000|   110|  3134.082| 65.124|  35,098|
| |Larue County|     1| 69.454|  0.000|    56|  3889.429| 49.610|  14,398|
| |Livingston County|     1| 108.767|  0.000|    35|  3806.831| 31.076|   9,194|
| |McLean County|     1| 108.613|  0.000|    42|  4561.746| 31.032|   9,207|
| |Madison County|     1| 10.754|  0.000|   549|  5904.051| 212.011|  92,987|
| |Carter County|     1| 37.318|  0.000|   101|  3769.079| 15.993|  26,797|
| |Mason County|     1| 58.582|  0.000|    55|  3222.027| 16.738|  17,070|
| |Johnson County|     0|  0.000|  0.000|    64|  2884.442| 154.524|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   350|  6467.708| 110.875|  54,115|
| |Hickman County|     0|  0.000|  0.000|    53| 12100.457| 587.084|   4,380|
| |Hart County|     0|  0.000|  0.000|   103|  5411.085| 142.594|  19,035|
| |Harrison County|     0|  0.000|  0.000|   121|  6406.862| 30.257|  18,886|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 16.379|   8,722|
| |Garrard County|     0|  0.000|  0.000|    80|  4528.473| 88.952|  17,666|
| |Fleming County|     0|  0.000|  0.000|    60|  4114.944| 29.392|  14,581|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 101.274|  14,106|
| |Cumberland County|     0|  0.000|  0.000|    57|  8618.083| 367.186|   6,614|
| |Elliott County|     0|  0.000|  0.000|    11|  1463.350| 57.014|   7,517|
| |Caldwell County|     0|  0.000|  0.000|    53|  4157.841| 44.828|  12,747|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Trimble County|     0|  0.000|  0.000|    32|  3777.594|  0.000|   8,471|
| |Marion County|     0|  0.000|  0.000|   124|  6433.871| 81.535|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    40|  3289.203| 117.472|  12,161|
| |McCreary County|     0|  0.000|  0.000|    42|  2437.467| 41.454|  17,231|
| |Lewis County|     0|  0.000|  0.000|    41|  3088.512| 43.045|  13,275|
| |Scott County|     0|  0.000|  0.000|   388|  6806.540| 105.256|  57,004|
| |Spencer County|     0|  0.000|  0.000|   123|  6356.261| 118.119|  19,351|
| |Todd County|     0|  0.000|  0.000|    35|  2846.917| 23.240|  12,294|
| |Union County|     0|  0.000|  0.000|    67|  4658.925| 99.337|  14,381|
| |Trigg County|     0|  0.000|  0.000|    54|  3685.755|  9.751|  14,651|
| |Woodford County|     0|  0.000|  0.000|   157|  5872.672| 117.560|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    14|  1956.127| 59.881|   7,157|
| |Wayne County|     0|  0.000|  0.000|    69|  3393.498| 112.414|  20,333|
| |Washington County|     0|  0.000|  0.000|    86|  7110.376| 248.036|  12,095|
| |Martin County|     0|  0.000|  0.000|    37|  3305.047| 63.804|  11,195|
| |Mercer County|     0|  0.000|  0.000|    84|  3829.845| 45.593|  21,933|
| |Breathitt County|     0|  0.000|  0.000|    31|  2454.473| 56.555|  12,630|
| |Montgomery County|     0|  0.000|  0.000|   124|  4403.878| 50.736|  28,157|
| |Lawrence County|     0|  0.000|  0.000|    36|  2350.330| 18.653|  15,317|
| |Lee County|     0|  0.000|  0.000|     7|   945.563| 57.892|   7,403|
| |Leslie County|     0|  0.000|  0.000|    31|  3138.605| 57.854|   9,877|
| |Bracken County|     0|  0.000|  0.000|    33|  3974.467| 68.822|   8,303|
| |Boyle County|     0|  0.000|  0.000|   157|  5222.888| 71.286|  30,060|
| |Ballard County|     0|  0.000|  0.000|    36|  4563.895| 90.553|   7,888|
| |Rowan County|     0|  0.000|  0.000|    75|  3066.231| 35.043|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    72|  4312.668| 94.126|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    60|  4854.762| 127.149|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    46|  3152.844| 97.914|  14,590|
| |Owsley County|     0|  0.000|  0.000|    12|  2718.007| 64.714|   4,415|
| |Owen County|     0|  0.000|  0.000|    50|  4586.735| 91.735|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    30|  2254.114|  0.000|  13,309|
| |Letcher County|     0|  0.000|  0.000|    60|  2783.835| 53.025|  21,553|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   693| 330.499| N/A|21,339| 10176.796| N/A|2,096,829|
| |McKinley County|   227| 3180.742| 10.009| 4,067| 56987.123| 116.100|  71,367|
| |San Juan County|   185| 1492.441|  3.457| 3,064| 24718.050| 64.538| 123,958|
| |Bernalillo County|   134| 197.314|  2.104| 5,196|  7651.067| 52.379| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,142|  7782.048| 36.992| 146,748|
| |Dona Ana County|    31| 142.075|  4.583| 2,517| 11535.553| 160.407| 218,195|
| |Cibola County|    18| 674.789|  5.355|   371| 13908.154| 139.242|  26,675|
| |Otero County|    10| 148.170|  0.000|   203|  3007.853| 21.167|  67,490|
| |Rio Arriba County|     7| 179.851|  7.341|   318|  8170.396| 73.409|  38,921|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024| 17.173|  16,637|
| |Chaves County|     6| 92.858|  0.000|   475|  7351.234| 201.192|  64,615|
| |Luna County|     5| 210.890| 12.051|   255| 10755.409| 102.432|  23,709|
| |Lea County|     5| 70.353|  2.010|   830| 11678.627| 303.524|  71,070|
| |Eddy County|     4| 68.423|  0.000|   318|  5439.617| 124.627|  58,460|
| |Valencia County|     4| 52.159|  0.000|   432|  5633.215| 95.005|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   658|  4376.222| 53.206| 150,358|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824| 15.874|  26,998|
| |Curry County|     2| 40.855|  0.000|   564| 11521.020| 207.192|  48,954|
| |Lincoln County|     2| 102.187|  7.299|   130|  6642.142| 145.981|  19,572|
| |Union County|     2| 492.732| 70.390|    30|  7390.983| 70.390|   4,059|
| |Quay County|     1| 121.168|  0.000|    34|  4119.714|  0.000|   8,253|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 47.854|  11,941|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |Roosevelt County|     1| 54.054|  0.000|   167|  9027.027| 177.606|  18,500|
| |Sierra County|     1| 92.670| 13.239|    32|  2965.434| 26.477|  10,791|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411|  9.240|  15,461|
| |Taos County|     1| 30.560|  0.000|   109|  3330.990| 43.656|  32,723|
| |San Miguel County|     0|  0.000|  0.000|    45|  1649.742| 15.712|  27,277|
| |Los Alamos County|     0|  0.000|  0.000|    23|  1187.465| 22.127|  19,369|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 68.060|   4,198|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   618| 156.180| N/A|44,725| 11302.837| N/A|3,956,971|
| |Oklahoma County|   115| 144.213|  2.329|10,794| 13535.916| 215.154| 797,434|
| |Tulsa County|   108| 165.758|  1.535|10,747| 16494.462| 291.392| 651,552|
| |Cleveland County|    56| 197.173|  2.012| 3,048| 10731.865| 134.802| 284,014|
| |Washington County|    39| 756.885|  0.000|   642| 12459.487| 146.941|  51,527|
| |McCurtain County|    28| 852.827|  8.702|   865| 26346.248| 130.535|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   890| 10948.591| 224.947|  81,289|
| |Delaware County|    20| 465.019|  3.322|   438| 10183.915| 112.933|  43,009|
| |Rogers County|    17| 183.865|  1.545| 1,020| 11031.917| 254.939|  92,459|
| |Caddo County|    17| 591.058| 14.901|   427| 14845.977| 218.542|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   520|  7647.396| 119.753|  67,997|
| |Creek County|    14| 195.744|  1.997|   621|  8682.643| 221.710|  71,522|
| |Osage County|    11| 234.227|  0.000|   431|  9177.438| 167.305|  46,963|
| |Kay County|    11| 252.653|  3.281|   251|  5765.079| 91.874|  43,538|
| |Comanche County|    10| 82.816|  0.000|   840|  6956.579| 65.070| 120,749|
| |Pottawatomie County|     9| 123.981|  1.968|   459|  6323.011| 88.558|  72,592|
| |Canadian County|     9| 60.685|  2.890| 1,238|  8347.606| 127.150| 148,306|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 50.020|   5,712|
| |Jackson County|     7| 285.365| 11.648|   527| 21483.897| 221.303|  24,530|
| |Texas County|     7| 350.298|  0.000| 1,058| 52945.003| 150.128|  19,983|
| |Grady County|     7| 125.372|  2.559|   445|  7970.054| 71.641|  55,834|
| |Mayes County|     6| 145.985|  0.000|   326|  7931.873| 125.130|  41,100|
| |Adair County|     6| 270.343|  0.000|   344| 15499.685| 212.413|  22,194|
| |Seminole County|     5| 206.118|  0.000|   241|  9934.867| 188.450|  24,258|
| |Carter County|     5| 103.926|  2.969|   349|  7254.058| 109.865|  48,111|
| |Garfield County|     5| 81.892|  2.340|   492|  8058.176| 257.375|  61,056|
| |Garvin County|     4| 144.347|  0.000|   235|  8480.387| 87.639|  27,711|
| |Pittsburg County|     4| 91.630|  3.272|   377|  8636.093| 533.415|  43,654|
| |Payne County|     4| 48.909|  1.747|   754|  9219.407| 132.754|  81,784|
| |McClain County|     4| 98.829|  0.000|   454| 11217.078| 183.539|  40,474|
| |Sequoyah County|     4| 96.226|  0.000|   354|  8515.961| 257.747|  41,569|
| |Stephens County|     3| 69.536|  3.311|   202|  4682.104| 66.225|  43,143|
| |Pawnee County|     3| 183.195|  0.000|   149|  9098.681| 200.642|  16,376|
| |Ottawa County|     3| 96.379|  4.589|   387| 12432.936| 178.990|  31,127|
| |Okmulgee County|     3| 77.993|  0.000|   479| 12452.879| 274.832|  38,465|
| |Pontotoc County|     2| 52.241|  0.000|   207|  5406.959| 82.093|  38,284|
| |Noble County|     2| 179.678|  0.000|    87|  7816.009| 77.005|  11,131|
| |Hughes County|     2| 150.614| 10.758|   141| 10618.269| 279.711|  13,279|
| |Lincoln County|     2| 57.344|  0.000|   174|  4988.961| 131.073|  34,877|
| |Cherokee County|     2| 41.104|  0.000|   449|  9227.860| 261.304|  48,657|
| |Cotton County|     2| 352.983|  0.000|    19|  3353.336| 25.213|   5,666|
| |Beckham County|     1| 45.748|  0.000|    61|  2790.613| 104.566|  21,859|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 39.409|   7,250|
| |Nowata County|     1| 99.246|  0.000|    58|  5756.252| 28.356|  10,076|
| |Marshall County|     1| 59.063|  8.438|   110|  6496.958| 84.376|  16,931|
| |Roger Mills County|     1| 279.096| 39.871|     9|  2511.862| 39.871|   3,583|
| |Okfuskee County|     1| 83.382| 11.912|    71|  5920.120| 166.764|  11,993|
| |Major County|     1| 131.079|  0.000|    35|  4587.757| 168.530|   7,629|
| |Choctaw County|     1| 68.157|  0.000|   191| 13017.993| 194.734|  14,672|
| |McIntosh County|     1| 51.031|  0.000|   194|  9899.980| 269.734|  19,596|
| |Craig County|     1| 70.711| 10.102|    86|  6081.177| 90.915|  14,142|
| |Kiowa County|     1| 114.837|  0.000|    30|  3445.108| 49.216|   8,708|
| |Latimer County|     1| 99.275|  0.000|    93|  9232.602| 226.915|  10,073|
| |Le Flore County|     1| 20.059|  0.000|   360|  7221.230| 283.691|  49,853|
| |Logan County|     1| 20.829|  0.000|   225|  4686.426| 110.094|  48,011|
| |Bryan County|     1| 20.836|  0.000|   465|  9688.509| 199.426|  47,995|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Custer County|     0|  0.000|  0.000|   209|  7206.151| 73.884|  29,003|
| |Johnston County|     0|  0.000|  0.000|    48|  4330.176| 77.325|  11,085|
| |Haskell County|     0|  0.000|  0.000|    62|  4910.113| 169.704|  12,627|
| |Harper County|     0|  0.000|  0.000|    10|  2711.497| 38.736|   3,688|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 376.932|   2,653|
| |Grant County|     0|  0.000|  0.000|    16|  3692.592| 131.878|   4,333|
| |Dewey County|     0|  0.000|  0.000|    10|  2044.572| 58.416|   4,891|
| |Coal County|     0|  0.000|  0.000|    39|  7097.361| 207.981|   5,495|
| |Cimarron County|     0|  0.000|  0.000|     1|   467.946|  0.000|   2,137|
| |Blaine County|     0|  0.000|  0.000|    45|  4772.510| 106.056|   9,429|
| |Beaver County|     0|  0.000|  0.000|    37|  6966.673| 26.898|   5,311|
| |Atoka County|     0|  0.000|  0.000|    76|  5524.059| 114.219|  13,758|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Love County|     0|  0.000|  0.000|    75|  7314.932| 139.332|  10,253|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 23.802|   6,002|
| |Kingfisher County|     0|  0.000|  0.000|   138|  8753.568| 226.542|  15,765|
| |Woodward County|     0|  0.000|  0.000|    41|  2028.598| 42.410|  20,211|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    29|  2656.651| 39.261|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   109|  9823.360| 77.248|  11,096|
| |Murray County|     0|  0.000|  0.000|    76|  5400.412| 131.965|  14,073|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   593| 840.242| N/A|12,896| 18272.785| N/A| 705,749|
| |District of Columbia|   593| 840.242|  1.215|12,896| 18272.785| 100.805| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   591| 606.923| N/A|15,449| 15865.240| N/A| 973,764|
| |New Castle County|   291| 520.803|  0.511| 7,276| 13021.854| 72.099| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,867| 25048.564| 111.004| 234,225|
| |Kent County|   108| 597.391|  0.790| 2,306| 12755.412| 63.216| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   566| 187.554| N/A|48,600| 16104.426| N/A|3,017,804|
| |Pulaski County|    86| 219.438|  2.552| 5,706| 14559.428| 237.663| 391,911|
| |Washington County|    52| 217.403|  2.389| 6,321| 26427.022| 120.050| 239,187|
| |Benton County|    43| 154.044|  1.535| 4,805| 17213.523| 99.284| 279,141|
| |Jefferson County|    40| 598.587|  2.138| 1,584| 23704.058| 384.806|  66,824|
| |Crittenden County|    23| 479.616|  8.937| 1,381| 28797.831| 333.646|  47,955|
| |Sebastian County|    20| 156.461|  5.588| 2,250| 17601.915| 369.920| 127,827|
| |Union County|    18| 465.333|  3.693|   508| 13132.723| 206.815|  38,682|
| |Yell County|    17| 796.589| 20.082| 1,069| 50091.373| 174.045|  21,341|
| |Garland County|    17| 171.050| 12.937| 1,071| 10776.166| 275.980|  99,386|
| |Mississippi County|    14| 344.395| 10.543| 1,044| 25682.025| 671.219|  40,651|
| |Craighead County|    12| 108.763|  0.000| 1,389| 12589.276| 301.687| 110,332|
| |Lincoln County|    12| 921.376| 10.969| 1,224| 93980.344| 318.094|  13,024|
| |Hot Spring County|    12| 355.334|  8.460| 1,557| 46104.646| 346.874|  33,771|
| |Columbia County|    12| 511.574| 30.451|   220|  9378.863| 79.172|  23,457|
| |Pope County|    10| 156.074|  0.000| 1,333| 20804.720| 205.126|  64,072|
| |Sevier County|    10| 587.993|  0.000|   996| 58564.121| 436.795|  17,007|
| |Newton County|    10| 1289.823| 128.982|   106| 13672.127| 110.556|   7,753|
| |Chicot County|     9| 889.504| 28.238|   736| 72741.649| 2597.916|  10,118|
| |Lawrence County|     9| 548.580|  0.000|   217| 13226.868| 269.936|  16,406|
| |Phillips County|     9| 506.130| 16.068|   329| 18501.856| 321.352|  17,782|
| |Nevada County|     9| 1090.645|  0.000|   143| 17329.132| 155.806|   8,252|
| |Lee County|     8| 903.240| 16.129|   896| 101162.922| 96.776|   8,857|
| |Carroll County|     7| 246.653|  0.000|   379| 13354.475| 191.282|  28,380|
| |Saline County|     7| 57.172|  1.167| 1,113|  9090.389| 222.855| 122,437|
| |Faulkner County|     6| 47.616|  1.134| 1,330| 10554.969| 114.506| 126,007|
| |Sharp County|     5| 286.664|  0.000|   114|  6535.948| 65.523|  17,442|
| |Miller County|     5| 115.588|  3.303|   518| 11974.940| 142.008|  43,257|
| |Ashley County|     5| 254.362|  7.267|   330| 16787.913| 494.190|  19,657|
| |Cleburne County|     5| 200.650|  0.000|   202|  8106.264| 108.924|  24,919|
| |Randolph County|     4| 222.742|  7.955|   222| 12362.178| 350.023|  17,958|
| |Bradley County|     4| 371.644| 13.273|   207| 19232.556| 690.195|  10,763|
| |Clay County|     4| 274.895|  0.000|   138|  9483.884| 255.260|  14,551|
| |Crawford County|     4| 63.234|  2.258|   648| 10243.926| 185.186|  63,257|
| |Howard County|     4| 302.984| 21.642|   355| 26889.865| 562.685|  13,202|
| |Cross County|     4| 243.620| 17.401|   208| 12668.250| 313.226|  16,419|
| |Conway County|     3| 143.913|  0.000|   153|  7339.538| 102.795|  20,846|
| |Drew County|     3| 164.663|  0.000|   217| 11910.643| 360.691|  18,219|
| |Poinsett County|     3| 127.508|  0.000|   292| 12410.745| 722.543|  23,528|
| |St. Francis County|     3| 120.029|  0.000| 1,226| 49051.772| 468.684|  24,994|
| |Franklin County|     2| 112.899|  0.000|   128|  7225.515| 137.091|  17,715|
| |Lonoke County|     2| 27.282|  0.000|   531|  7243.313| 120.819|  73,309|
| |White County|     2| 25.396|  0.000|   328|  4164.921| 103.397|  78,753|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385|  8.634|  16,545|
| |Johnson County|     2| 75.250| 10.750|   672| 25284.070| 177.375|  26,578|
| |Ouachita County|     2| 85.536|  0.000|   105|  4490.634| 146.633|  23,382|
| |Madison County|     2| 120.656|  8.618|   270| 16288.610| 43.092|  16,576|
| |Cleveland County|     2| 251.383|  0.000|   103| 12946.204| 484.809|   7,956|
| |Boone County|     2| 53.430|  3.816|   214|  5717.034| 114.493|  37,432|
| |Desha County|     2| 176.041|  0.000|   201| 17692.105| 452.676|  11,361|
| |Greene County|     2| 44.126|  3.152|   492| 10854.937| 280.514|  45,325|
| |Hempstead County|     2| 92.885|  0.000|   249| 11564.184| 165.866|  21,532|
| |Lafayette County|     2| 301.932|  0.000|    56|  8454.106| 129.400|   6,624|
| |Jackson County|     1| 59.812|  0.000|   117|  6998.026| 478.498|  16,719|
| |Izard County|     1| 73.373|  0.000|    53|  3888.767| 83.855|  13,629|
| |Independence County|     1| 26.438|  0.000|   550| 14540.648| 517.420|  37,825|
| |Logan County|     1| 46.585|  0.000|   277| 12904.127| 539.058|  21,466|
| |Polk County|     1| 50.090|  0.000|   150|  7513.524| 128.803|  19,964|
| |Pike County|     1| 93.301|  0.000|   111| 10356.410| 359.875|  10,718|
| |Montgomery County|     1| 111.284| 15.898|    38|  4228.800| 143.080|   8,986|
| |Dallas County|     1| 142.674| 20.382|    64|  9131.117| 101.910|   7,009|
| |Clark County|     1| 44.803|  0.000|   177|  7930.108| 83.205|  22,320|
| |Arkansas County|     1| 57.189|  0.000|   227| 12981.814| 171.566|  17,486|
| |Little River County|     1| 81.573|  0.000|   185| 15090.954| 314.638|  12,259|
| |Stone County|     1| 79.962|  0.000|    69|  5517.352| 114.231|  12,506|
| |Baxter County|     0|  0.000|  0.000|    73|  1740.914| 30.662|  41,932|
| |Prairie County|     0|  0.000|  0.000|   100| 12403.870| 425.276|   8,062|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 81.984|  10,455|
| |Monroe County|     0|  0.000|  0.000|    64|  9550.813| 234.507|   6,701|
| |Marion County|     0|  0.000|  0.000|    29|  1737.151| 42.787|  16,694|
| |Grant County|     0|  0.000|  0.000|   140|  7664.933| 78.214|  18,265|
| |Fulton County|     0|  0.000|  0.000|    44|  3526.489| 171.745|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    17|  3276.161| 110.123|   5,189|
| |Woodruff County|     0|  0.000|  0.000|    22|  3481.013| 45.208|   6,320|
| |Searcy County|     0|  0.000|  0.000|    33|  4187.286| 108.761|   7,881|
| |Scott County|     0|  0.000|  0.000|    66|  6419.609| 291.800|  10,281|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,861|  5045.925| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.000| 3,863|  9263.234| 26.035| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,698|  5481.504| 20.292| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   466|  3078.122|  7.549| 151,391|
| |Strafford County|    13| 99.515|  0.000|   362|  2771.122| 26.246| 130,633|
| |Belknap County|     4| 65.250|  0.000|   115|  1875.928| 11.652|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   101|  1327.463| 15.021|  76,085|
| |Sullivan County|     1| 23.177|  0.000|    41|   950.262|  3.311|  43,146|
| |Carroll County|     1| 20.446|  0.000|    94|  1921.897| 11.683|  48,910|
| |Grafton County|     1| 11.125|  0.000|   104|  1157.021|  1.589|  89,886|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   392| 134.555| N/A|31,468| 10801.445| N/A|2,913,314|
| |Johnson County|   105| 174.302|  1.660| 5,869|  9742.680| 149.165| 602,401|
| |Wyandotte County|   101| 610.534|  4.318| 4,959| 29976.606| 294.472| 165,429|
| |Sedgwick County|    46| 89.140|  0.830| 4,990|  9669.756| 153.365| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,611|  9108.127| 137.304| 176,875|
| |Lyon County|    14| 421.750|  4.304|   716| 21569.513| 154.929|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,795| 49222.585| 156.697|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,088| 62107.737| 195.468|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,483| 18138.898| 101.344|  81,758|
| |Coffey County|     8| 978.115|  0.000|    67|  8191.710|  0.000|   8,179|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 27.294|   5,234|
| |Douglas County|     5| 40.897|  1.168|   750|  6134.518| 77.120| 122,259|
| |Saline County|     5| 92.210|  0.000|   384|  7081.735| 108.018|  54,224|
| |Riley County|     5| 67.356|  0.000|   483|  6506.628| 59.659|  74,232|
| |Montgomery County|     5| 157.089|  0.000|   170|  5341.041| 35.906|  31,829|
| |Seward County|     4| 186.672|  0.000| 1,243| 58008.214| 260.007|  21,428|
| |Barton County|     3| 116.374|  0.000|   148|  5741.107| 121.915|  25,779|
| |Sumner County|     3| 131.372|  0.000|   101|  4422.841| 18.767|  22,836|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Grant County|     2| 279.720|  0.000|   116| 16223.776| 379.620|   7,150|
| |Bourbon County|     2| 137.608|  9.829|    79|  5435.530| 58.975|  14,534|
| |Cowley County|     2| 57.293|  0.000|   174|  4984.531| 57.293|  34,908|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 35.705|   8,002|
| |Geary County|     2| 63.151|  0.000|   152|  4799.495| 99.238|  31,670|
| |Jackson County|     1| 75.924|  0.000|   155| 11768.279| 108.463|  13,171|
| |Jewell County|     1| 347.343| 49.620|    12|  4168.114| 99.241|   2,879|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199| 71.644|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   129|  6469.733| 365.400|  19,939|
| |Butler County|     1| 14.945|  0.000|   285|  4259.389| 143.047|  66,911|
| |Crawford County|     1| 25.761|  0.000|   385|  9918.079| 29.441|  38,818|
| |Dickinson County|     1| 54.154|  0.000|    48|  2599.372| 38.681|  18,466|
| |Ellis County|     1| 35.023|  0.000|   145|  5078.275| 60.039|  28,553|
| |Franklin County|     1| 39.148|  0.000|   194|  7594.738| 218.111|  25,544|
| |McPherson County|     1| 35.036|  0.000|   148|  5185.341| 90.093|  28,542|
| |Labette County|     1| 50.974|  7.282|   138|  7034.356| 145.639|  19,618|
| |Kearny County|     1| 260.552|  0.000|    63| 16414.799| 223.331|   3,838|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 24.042|  11,884|
| |Nemaha County|     1| 97.742|  0.000|    49|  4789.366| 13.963|  10,231|
| |Harvey County|     1| 29.045|  0.000|   204|  5925.237| 145.226|  34,429|
| |Stafford County|     1| 240.616| 34.374|     6|  1443.696| 103.121|   4,156|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090| 284.860|   2,006|
| |Reno County|     1| 16.130|  0.000|   286|  4613.052| 124.428|  61,998|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 134.813|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   108|  4429.316| 17.577|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     8|  1247.272| 22.273|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    35|  6136.045| 125.225|   5,704|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Osage County|     0|  0.000|  0.000|    41|  2570.694| 26.871|  15,949|
| |Scott County|     0|  0.000|  0.000|    52| 10781.671| 710.879|   4,823|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 50.272|   8,525|
| |Russell County|     0|  0.000|  0.000|    16|  2333.722| 62.510|   6,856|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Sherman County|     0|  0.000|  0.000|    16|  2704.073| 24.144|   5,917|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 82.445|   6,931|
| |Thomas County|     0|  0.000|  0.000|    40|  5143.371| 128.584|   7,777|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 52.090|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818|  0.000|   2,750|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 95.525|   5,982|
| |Neosho County|     0|  0.000|  0.000|    65|  4060.723| 107.096|  16,007|
| |Morris County|     0|  0.000|  0.000|    13|  2313.167| 101.678|   5,620|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Miami County|     0|  0.000|  0.000|   134|  3913.894| 58.416|  34,237|
| |Meade County|     0|  0.000|  0.000|    45| 11157.947| 177.110|   4,033|
| |Marshall County|     0|  0.000|  0.000|    10|  1030.184| 14.717|   9,707|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Linn County|     0|  0.000|  0.000|    40|  4122.436| 73.615|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 115.440|   2,475|
| |Kingman County|     0|  0.000|  0.000|    20|  2796.421| 199.744|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    76|  3990.968| 45.011|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Harper County|     0|  0.000|  0.000|    12|  2207.506| 78.839|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    38| 14966.522| 56.265|   2,539|
| |Graham County|     0|  0.000|  0.000|    17|  6849.315| 57.557|   2,482|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946| 57.748|  12,369|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Gray County|     0|  0.000|  0.000|    84| 14028.056| 310.144|   5,988|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495| 70.235|   6,102|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024| 36.360|   7,858|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 37.594|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Comanche County|     0|  0.000|  0.000|     6|  3529.412| 252.101|   1,700|
| |Cloud County|     0|  0.000|  0.000|    37|  4211.245| 113.817|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     3|  1129.093| 53.766|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Chase County|     0|  0.000|  0.000|    48| 18126.888| 485.542|   2,648|
| |Brown County|     0|  0.000|  0.000|    40|  4182.350| 119.496|   9,564|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Atchison County|     0|  0.000|  0.000|    64|  3981.833| 17.776|  16,073|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   368| 87.251| N/A|21,774|  5162.484| N/A|4,217,737|
| |Multnomah County|    98| 120.563|  0.879| 5,014|  6168.382| 81.020| 812,855|
| |Marion County|    73| 209.880|  2.054| 2,979|  8564.824| 109.253| 347,818|
| |Clackamas County|    44| 105.216|  2.391| 1,571|  3756.693| 43.726| 418,187|
| |Umatilla County|    30| 384.862| 10.996| 2,312| 29660.038| 348.209|  77,950|
| |Washington County|    25| 41.556|  0.475| 3,161|  5254.392| 67.440| 601,592|
| |Malheur County|    13| 425.240|  4.673|   822| 26888.227| 532.718|  30,571|
| |Yamhill County|    13| 121.382|  1.334|   470|  4388.422| 94.705| 107,100|
| |Polk County|    12| 139.397|  0.000|   326|  3786.955| 43.147|  86,085|
| |Linn County|    11| 84.779|  1.101|   296|  2281.328| 45.142| 129,749|
| |Deschutes County|    10| 50.584|  1.445|   616|  3115.958| 49.138| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   419|  8386.374| 68.624|  49,962|
| |Benton County|     6| 64.479|  0.000|   171|  1837.662| 16.887|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   377| 15289.156| 307.058|  24,658|
| |Lane County|     3|  7.852|  0.000|   596|  1559.936| 22.808| 382,067|
| |Morrow County|     3| 258.554| 12.312|   377| 32491.597| 751.037|  11,603|
| |Wasco County|     3| 112.435|  0.000|   194|  7270.819| 123.143|  26,682|
| |Union County|     2| 74.530|  0.000|   395| 14719.583| 15.971|  26,835|
| |Klamath County|     2| 29.309|  2.094|   204|  2989.537| 12.561|  68,238|
| |Josephine County|     2| 22.861|  1.633|   124|  1417.353| 27.759|  87,487|
| |Jackson County|     2|  9.052|  0.647|   486|  2199.652| 48.493| 220,944|
| |Crook County|     1| 40.977|  0.000|    50|  2048.844| 40.977|  24,404|
| |Douglas County|     1|  9.011|  0.000|   156|  1405.659| 21.883| 110,980|
| |Wallowa County|     1| 138.735|  0.000|    19|  2635.960|  0.000|   7,208|
| |Curry County|     0|  0.000|  0.000|    17|   741.549| 18.695|  22,925|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582| 10.568|  27,036|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 160.514|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Hood River County|     0|  0.000|  0.000|   201|  8596.356| 164.962|  23,382|
| |Harney County|     0|  0.000|  0.000|    10|  1352.631|  0.000|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137|  6.646|  64,487|
| |Columbia County|     0|  0.000|  0.000|   101|  1929.174| 46.388|  52,354|
| |Clatsop County|     0|  0.000|  0.000|    89|  2212.609| 24.861|  40,224|
| |Baker County|     0|  0.000|  0.000|    40|  2480.774| 44.300|  16,124|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   351| 181.451| N/A|28,876| 14927.564| N/A|1,934,408|
| |Douglas County|   136| 238.042|  1.250|11,532| 20184.588| 203.286| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,750| 28523.463| 67.525|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,930| 96374.713| 185.473|  20,026|
| |Lancaster County|    17| 53.277|  0.895| 3,344| 10479.802| 81.034| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   100| 10725.011| 61.286|   9,324|
| |Adams County|    11| 350.732|  0.000|   361| 11510.378| 68.324|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,323| 12409.453| 169.418| 187,196|
| |Dodge County|    10| 273.486|  7.814|   820| 22425.817| 152.371|  36,565|
| |Dawson County|     9| 381.437|  0.000|   967| 40983.259| 102.927|  23,595|
| |Perkins County|     7| 2421.308| 296.487|    18|  6226.219| 49.414|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   304|  8535.010| 52.141|  35,618|
| |Madison County|     5| 142.454|  0.000|   463| 13191.259| 158.735|  35,099|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 158.203|   7,224|
| |Custer County|     4| 371.161|  0.000|    50|  4639.510| 92.790|  10,777|
| |Gage County|     4| 185.934|  0.000|    90|  4183.517| 53.124|  21,513|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747|  0.000|   6,445|
| |Colfax County|     4| 373.518|  0.000|   704| 65739.098| 120.059|  10,709|
| |Platte County|     3| 89.633|  0.000|   799| 23872.124| 128.046|  33,470|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Cass County|     2| 76.196|  5.443|   182|  6933.862| 119.737|  26,248|
| |Saunders County|     2| 92.687|  0.000|   167|  7739.364| 165.512|  21,578|
| |Lincoln County|     2| 57.284|  0.000|   129|  3694.793| 147.301|  34,914|
| |Saline County|     2| 140.607|  0.000|   597| 41971.316| 110.477|  14,224|
| |Antelope County|     1| 158.781|  0.000|    19|  3016.831|  0.000|   6,298|
| |Buffalo County|     1| 20.137|  0.000|   449|  9041.664| 256.032|  49,659|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Fillmore County|     1| 183.083|  0.000|    24|  4393.995|  0.000|   5,462|
| |Washington County|     1| 48.242|  0.000|   130|  6271.407| 151.616|  20,729|
| |Seward County|     1| 57.857|  0.000|   125|  7232.122| 173.571|  17,284|
| |Richardson County|     1| 127.146|  0.000|    24|  3051.494| 72.655|   7,865|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |Otoe County|     0|  0.000|  0.000|    55|  3434.924| 107.063|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    34|  4876.649| 266.372|   6,972|
| |Nance County|     0|  0.000|  0.000|     8|  2273.373|  0.000|   3,519|
| |Morrill County|     0|  0.000|  0.000|    59| 12710.039| 30.775|   4,642|
| |Merrick County|     0|  0.000|  0.000|    63|  8123.791| 147.370|   7,755|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    36|  4320.691| 68.582|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Sheridan County|     0|  0.000|  0.000|    11|  2096.836| 54.463|   5,246|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Stanton County|     0|  0.000|  0.000|    33|  5574.324| 120.656|   5,920|
| |Phelps County|     0|  0.000|  0.000|    40|  4427.718| 47.440|   9,034|
| |Pierce County|     0|  0.000|  0.000|    23|  3217.683| 119.914|   7,148|
| |Polk County|     0|  0.000|  0.000|    27|  5179.359| 82.212|   5,213|
| |Red Willow County|     0|  0.000|  0.000|    17|  1585.229| 13.321|  10,724|
| |Sherman County|     0|  0.000|  0.000|    11|  3665.445| 47.603|   3,001|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759| 105.274|   1,357|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 46.061|   6,203|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Jefferson County|     0|  0.000|  0.000|    18|  2554.641| 81.100|   7,046|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 28.381|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 60.635|   2,356|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739|  0.000|   1,990|
| |Cuming County|     0|  0.000|  0.000|    68|  7687.090| 80.747|   8,846|
| |Garfield County|     0|  0.000|  0.000|     4|  2031.488| 72.553|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Franklin County|     0|  0.000|  0.000|    13|  4363.880| 191.819|   2,979|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827| 79.631|   1,794|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 33.265|   8,589|
| |York County|     0|  0.000|  0.000|    84|  6140.800| 114.879|  13,679|
| |Chase County|     0|  0.000|  0.000|     7|  1783.894| 36.406|   3,924|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139| 182.448|     783|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Wayne County|     0|  0.000|  0.000|    38|  4049.014| 15.222|   9,385|
| |Valley County|     0|  0.000|  0.000|    10|  2405.002|  0.000|   4,158|
| |Thomas County|     0|  0.000|  0.000|     1|  1385.042|  0.000|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 28.554|   5,003|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    23|  2862.833| 71.126|   8,034|
| |Kearney County|     0|  0.000|  0.000|    58|  8929.946| 527.879|   6,495|
| |Johnson County|     0|  0.000|  0.000|    14|  2760.797| 28.171|   5,071|
| |Cedar County|     0|  0.000|  0.000|    23|  2737.443| 34.006|   8,402|
| |Butler County|     0|  0.000|  0.000|    62|  7734.531| 89.107|   8,016|
| |Burt County|     0|  0.000|  0.000|    40|  6192.909| 331.763|   6,459|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Boyd County|     0|  0.000|  0.000|     5|  2605.524| 297.774|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    13|  1205.601| 26.497|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832| 27.515|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   288| 89.833| N/A|35,573| 11095.903| N/A|3,205,958|
| |Salt Lake County|   200| 172.349|  1.970|20,903| 18013.042| 150.190|1,160,437|
| |Utah County|    37| 58.155|  0.449| 8,887| 13968.109| 162.114| 636,235|
| |San Juan County|    25| 1633.133|  9.332|   653| 42657.434| 214.640|  15,308|
| |Davis County|    21| 59.075|  2.009| 3,256|  9159.421| 79.168| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   576| 16895.955| 167.619|  34,091|
| |Summit County|     1| 23.728|  0.000|   714| 16941.511| 54.235|  42,145|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Tooele County|     0|  0.000|  0.000|   584|  8082.038| 53.379|  72,259|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   246| 137.656| N/A|25,593| 14321.247| N/A|1,787,065|
| |Ada County|    85| 176.500|  5.636| 9,315| 19342.300| 307.021| 481,587|
| |Canyon County|    51| 221.885|  5.594| 5,951| 25890.911| 522.082| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,435| 16517.415| 292.693|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   161|  3984.360| 81.313|  40,408|
| |Kootenai County|    16| 96.562|  1.724| 1,856| 11201.168| 192.261| 165,697|
| |Blaine County|     6| 260.632|  0.000|   578| 25107.511| 43.439|  23,021|
| |Jerome County|     6| 245.781|  0.000|   488| 19990.169| 286.744|  24,412|
| |Bonneville County|     4| 33.596|  2.400| 1,112|  9339.672| 364.756| 119,062|
| |Elmore County|     3| 109.047|  0.000|   215|  7815.056| 72.698|  27,511|
| |Washington County|     3| 294.291|  0.000|   216| 21188.935| 308.305|  10,194|
| |Payette County|     3| 125.256|  5.965|   405| 16909.524| 339.980|  23,951|
| |Owyhee County|     3| 253.743| 12.083|   266| 22498.520| 326.241|  11,823|
| |Shoshone County|     2| 155.255|  0.000|   117|  9082.441| 432.497|  12,882|
| |Minidoka County|     2| 95.062|  0.000|   479| 22767.242| 176.543|  21,039|
| |Bingham County|     2| 42.725|  0.000|   269|  5746.513| 189.211|  46,811|
| |Bannock County|     2| 22.777|  0.000|   427|  4862.883| 159.439|  87,808|
| |Gooding County|     1| 65.880|  0.000|   170| 11199.684| 244.699|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   214|  7164.139| 267.818|  29,871|
| |Valley County|     1| 87.781|  0.000|    65|  5705.758| 188.102|  11,392|
| |Gem County|     1| 55.212|  7.887|   180|  9938.163| 149.861|  18,112|
| |Cassia County|     1| 41.615|  0.000|   527| 21930.920| 214.018|  24,030|
| |Boise County|     1| 127.698|  0.000|    51|  6512.578| 164.183|   7,831|
| |Benewah County|     1| 107.550| 15.364|    72|  7743.601| 215.100|   9,298|
| |Madison County|     0|  0.000|  0.000|   172|  4310.021| 107.393|  39,907|
| |Power County|     0|  0.000|  0.000|    58|  7551.100| 92.994|   7,681|
| |Bonner County|     0|  0.000|  0.000|   184|  4022.825| 87.453|  45,739|
| |Bear Lake County|     0|  0.000|  0.000|    17|  2775.510| 186.589|   6,125|
| |Oneida County|     0|  0.000|  0.000|    15|  3310.527| 63.058|   4,531|
| |Lincoln County|     0|  0.000|  0.000|    59| 10995.155| 159.736|   5,366|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Lemhi County|     0|  0.000|  0.000|    28|  3488.227| 284.753|   8,027|
| |Latah County|     0|  0.000|  0.000|   107|  2667.797| 67.674|  40,108|
| |Idaho County|     0|  0.000|  0.000|    32|  1919.962| 17.143|  16,667|
| |Fremont County|     0|  0.000|  0.000|    87|  6641.728| 207.213|  13,099|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 20.591|  13,876|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 132.428|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 32.631|   8,756|
| |Clark County|     0|  0.000|  0.000|     9| 10650.888| 676.247|     845|
| |Caribou County|     0|  0.000|  0.000|    32|  4472.397| 179.695|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Boundary County|     0|  0.000|  0.000|    38|  3103.307| 46.666|  12,245|
| |Teton County|     0|  0.000|  0.000|    85|  7000.494| 270.607|  12,142|
| |Adams County|     0|  0.000|  0.000|    20|  4657.662| 66.538|   4,294|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   147| 82.025| N/A| 7,879|  4396.403| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  1.604|   960|  5389.504| 87.419| 178,124|
| |Jackson County|    19| 664.894|  0.000|   165|  5774.076| 34.994|  28,576|
| |Mercer County|    13| 221.246| 24.313|   203|  3454.849| 87.526|  58,758|
| |Berkeley County|    11| 92.304|  0.000|   699|  5865.521| 45.553| 119,171|
| |Wayne County|     9| 228.415|  0.000|   212|  5380.438| 76.138|  39,402|
| |Fayette County|     7| 165.071|  6.738|   154|  3631.562| 77.482|  42,406|
| |Wood County|     5| 59.867|  0.000|   256|  3065.208| 27.368|  83,518|
| |Logan County|     5| 156.157|  8.923|   246|  7682.938| 397.086|  32,019|
| |Mingo County|     5| 213.456| 12.198|   182|  7769.809| 231.753|  23,424|
| |Monongalia County|     5| 47.343|  0.000|   950|  8995.190| 28.406| 105,612|
| |Preston County|     4| 119.646|  0.000|   125|  3738.933|  0.000|  33,432|
| |Ohio County|     4| 96.593|  0.000|   272|  6568.303| 41.397|  41,411|
| |Mineral County|     4| 148.876|  0.000|   125|  4652.375| 58.487|  26,868|
| |Jefferson County|     4| 69.996|  0.000|   296|  5179.715|  9.999|  57,146|
| |Cabell County|     3| 32.628|  1.554|   409|  4448.311| 91.670|  91,945|
| |Greenbrier County|     3| 86.550|  0.000|    93|  2683.053| 24.729|  34,662|
| |Grant County|     3| 259.336| 24.699|   121| 10459.889| 493.974|  11,568|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097| 17.962|  15,907|
| |Marion County|     2| 35.668|  0.000|   192|  3424.169| 33.121|  56,072|
| |Wyoming County|     2| 98.068|  7.005|    34|  1667.157| 77.053|  20,394|
| |Mason County|     1| 37.713|  0.000|    63|  2375.924| 70.039|  26,516|
| |Hampshire County|     1| 43.150|  0.000|    76|  3279.396| 12.329|  23,175|
| |Pendleton County|     1| 143.493|  0.000|    42|  6026.690| 20.499|   6,969|
| |Pleasants County|     1| 134.048| 19.150|    14|  1876.676| 114.899|   7,460|
| |Taylor County|     1| 59.898|  0.000|    59|  3533.992| 51.341|  16,695|
| |Roane County|     1| 73.057|  0.000|    16|  1168.907| 20.873|  13,688|
| |Raleigh County|     1| 13.631|  0.000|   259|  3530.486| 118.786|  73,361|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  4.679|  30,531|
| |Harrison County|     1| 14.869|  0.000|   232|  3449.506| 70.095|  67,256|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Brooke County|     1| 45.581|  0.000|    67|  3053.922| 32.558|  21,939|
| |Nicholas County|     1| 40.823|  0.000|    37|  1510.451| 23.327|  24,496|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Hardy County|     0|  0.000|  0.000|    61|  4427.991| 72.590|  13,776|
| |Lincoln County|     0|  0.000|  0.000|    94|  4605.811| 174.993|  20,409|
| |McDowell County|     0|  0.000|  0.000|    64|  3631.412| 145.905|  17,624|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Gilmer County|     0|  0.000|  0.000|    17|  2173.079| 18.261|   7,823|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 33.820|   8,448|
| |Wetzel County|     0|  0.000|  0.000|    44|  2920.677| 28.448|  15,065|
| |Summers County|     0|  0.000|  0.000|    14|  1113.497| 79.536|  12,573|
| |Tucker County|     0|  0.000|  0.000|    10|  1462.202|  0.000|   6,839|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 49.886|   8,591|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  5.909|  24,176|
| |Boone County|     0|  0.000|  0.000|   105|  4893.508| 113.183|  21,457|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Morgan County|     0|  0.000|  0.000|    30|  1677.477| 31.952|  17,884|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Randolph County|     0|  0.000|  0.000|   211|  7353.197| 19.914|  28,695|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 39.669|  28,810|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |Putnam County|     0|  0.000|  0.000|   200|  3542.958| 65.798|  56,450|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   146| 165.035| N/A| 9,713| 10979.372| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  2.959| 4,457| 23077.242| 147.196| 193,134|
| |Pennington County|    32| 281.257|  3.767|   898|  7892.771| 62.781| 113,775|
| |Beadle County|     9| 487.726|  0.000|   594| 32189.888| 54.192|  18,453|
| |Todd County|     5| 491.304| 14.037|    69|  6779.994| 42.112|  10,177|
| |Union County|     4| 251.067|  0.000|   216| 13557.620| 134.500|  15,932|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556| 72.812|   1,962|
| |Brown County|     3| 77.242|  0.000|   451| 11612.039| 143.449|  38,839|
| |Hughes County|     2| 114.116|  0.000|    93|  5306.402| 73.360|  17,526|
| |Yankton County|     2| 87.665|  0.000|   119|  5216.095| 100.189|  22,814|
| |Lake County|     2| 156.287|  0.000|    94|  7345.472| 111.633|  12,797|
| |Lincoln County|     2| 32.718|  0.000|   653| 10682.502| 165.928|  61,128|
| |Lyman County|     2| 528.961|  0.000|    90| 23803.227| 75.566|   3,781|
| |Oglala Lakota County|     2| 141.074| 10.077|   156| 11003.738| 50.383|  14,177|
| |Meade County|     1| 35.296|  0.000|    96|  3388.395| 90.761|  28,332|
| |Roberts County|     1| 96.209|  0.000|    80|  7696.748| 123.698|  10,394|
| |McCook County|     1| 179.019|  0.000|    29|  5191.550| 127.871|   5,586|
| |Brookings County|     1| 28.509|  0.000|   140|  3991.219| 77.381|  35,077|
| |Davison County|     1| 50.569|  7.224|    96|  4854.614| 21.672|  19,775|
| |Faulk County|     1| 434.972|  0.000|    27| 11744.237| 62.139|   2,299|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474| 42.720|   3,344|
| |Butte County|     1| 95.886|  0.000|    18|  1725.956| 95.886|  10,429|
| |Codington County|     1| 35.703|  0.000|   138|  4926.988| 91.807|  28,009|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Grant County|     0|  0.000|  0.000|    27|  3828.701| 81.031|   7,052|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 85.123|   6,713|
| |Edmunds County|     0|  0.000|  0.000|    17|  4439.802| 149.237|   3,829|
| |Douglas County|     0|  0.000|  0.000|    19|  6504.622| 146.721|   2,921|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 1399.544|   2,756|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Turner County|     0|  0.000|  0.000|    52|  6202.290| 68.157|   8,384|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    22|  3569.111| 185.408|   6,164|
| |Hand County|     0|  0.000|  0.000|     8|  2507.051| 44.769|   3,191|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668|  0.000|   3,453|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Marshall County|     0|  0.000|  0.000|     9|  1823.708| 28.948|   4,935|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 60.049|   2,379|
| |Lawrence County|     0|  0.000|  0.000|    61|  2360.316| 160.302|  25,844|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582|  0.000|   4,939|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     3|  2305.919|  0.000|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    29|  3977.507| 39.187|   7,291|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Spink County|     0|  0.000|  0.000|    26|  4077.792| 89.622|   6,376|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Dewey County|     0|  0.000|  0.000|    48|  8146.640|  0.000|   5,892|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Charles Mix County|     0|  0.000|  0.000|   103| 11084.804| 46.123|   9,292|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233| 103.821|   1,376|
| |Brule County|     0|  0.000|  0.000|    46|  8684.161| 161.817|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159| 51.929|   2,751|
| |Clay County|     0|  0.000|  0.000|   131|  9310.590| 111.686|  14,070|
| |Corson County|     0|  0.000|  0.000|    36|  8810.573| 244.738|   4,086|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Deuel County|     0|  0.000|  0.000|    11|  2528.154| 65.666|   4,351|
| |Day County|     0|  0.000|  0.000|    23|  4240.413| 52.676|   5,424|
| |Custer County|     0|  0.000|  0.000|    36|  4012.483| 206.993|   8,972|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   126| 93.735| N/A| 4,050|  3012.918| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.484| 2,090|  7084.674| 14.043| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    13| 62.608|  0.688|   675|  3250.803| 10.320| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   171|  1398.178|  2.336| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   565|  5218.098| 22.429| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   151|   992.455|  0.939| 152,148|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  3.592|  39,772|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Hancock County|     1| 18.186|  0.000|    36|   654.700|  5.196|  54,987|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Oxford County|     0|  0.000|  0.000|    55|   948.685|  2.464|  57,975|
| |Washington County|     0|  0.000|  0.000|    13|   414.290|  4.553|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    55|  1533.913| 15.937|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|     4|   238.308|  8.511|  16,785|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   118| 154.843| N/A| 7,865| 10320.683| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,058| 16809.309| 94.231| 181,923|
| |Burleigh County|     8| 83.659|  4.482| 1,244| 13009.014| 354.058|  95,626|
| |Grand Forks County|     6| 86.392|  2.057|   701| 10093.447| 121.360|  69,451|
| |Stark County|     5| 158.786|  9.073|   292|  9273.079| 322.108|  31,489|
| |Stutsman County|     3| 144.900|  6.900|   128|  6182.380| 48.300|  20,704|
| |Morton County|     3| 95.651|  0.000|   402| 12817.243| 501.029|  31,364|
| |McIntosh County|     2| 800.961| 57.212|    37| 14817.781| 572.115|   2,497|
| |McKenzie County|     2| 133.120|  9.509|    91|  6056.976| 66.560|  15,024|
| |Ramsey County|     2| 173.626|  0.000|    75|  6510.982| 186.028|  11,519|
| |Benson County|     2| 292.740| 20.910|   142| 20784.543| 313.650|   6,832|
| |Williams County|     2| 53.207|  0.000|   276|  7342.574| 121.616|  37,589|
| |Griggs County|     1| 448.229|  0.000|    35| 15688.032| 320.164|   2,231|
| |Emmons County|     1| 308.547|  0.000|    17|  5245.295|  0.000|   3,241|
| |McHenry County|     1| 174.064|  0.000|    17|  2959.095| 49.733|   5,745|
| |Mountrail County|     1| 94.832|  0.000|   136| 12897.108| 189.663|  10,545|
| |Sioux County|     1| 236.407|  0.000|    86| 20330.969| 911.854|   4,230|
| |Ward County|     1| 14.784|  0.000|   237|  3503.792| 88.704|  67,641|
| |Richland County|     1| 61.816|  8.831|   110|  6799.777| 132.463|  16,177|
| |Golden Valley County|     0|  0.000|  0.000|     5|  2839.296| 81.123|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Kidder County|     0|  0.000|  0.000|    18|  7258.065| 403.226|   2,480|
| |Eddy County|     0|  0.000|  0.000|    18|  7870.573| 187.395|   2,287|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 35.308|   4,046|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784| 77.220|   1,850|
| |Foster County|     0|  0.000|  0.000|    27|  8411.215| 445.038|   3,210|
| |Dunn County|     0|  0.000|  0.000|    31|  7007.233| 32.291|   4,424|
| |Divide County|     0|  0.000|  0.000|     2|   883.392| 63.099|   2,264|
| |Mercer County|     0|  0.000|  0.000|    32|  3908.636| 157.043|   8,187|
| |Dickey County|     0|  0.000|  0.000|    13|  2668.309| 29.322|   4,872|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Bowman County|     0|  0.000|  0.000|    10|  3306.878| 188.964|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Barnes County|     0|  0.000|  0.000|    38|  3648.584| 41.149|  10,415|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |McLean County|     0|  0.000|  0.000|    77|  8148.148| 574.452|   9,450|
| |Nelson County|     0|  0.000|  0.000|    26|  9030.914| 347.343|   2,879|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Wells County|     0|  0.000|  0.000|    21|  5477.308| 74.521|   3,834|
| |Walsh County|     0|  0.000|  0.000|   106|  9961.470| 93.976|  10,641|
| |Traill County|     0|  0.000|  0.000|    57|  7093.081| 177.771|   8,036|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Steele County|     0|  0.000|  0.000|    15|  7936.508| 151.172|   1,890|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 325.910|   1,315|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    82|  5784.424| 473.638|  14,176|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641|  0.000|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Pierce County|     0|  0.000|  0.000|    12|  3018.868| 35.939|   3,975|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    77| 72.045| N/A| 5,104|  4775.547| N/A|1,068,778|
| |Yellowstone County|    30| 185.989|  2.657| 1,316|  8158.710| 175.361| 161,300|
| |Big Horn County|    14| 1051.130| 32.177|   444| 33335.836| 868.791|  13,319|
| |Toole County|     6| 1266.892|  0.000|    44|  9290.541| 271.477|   4,736|
| |Cascade County|     4| 49.161|  3.511|   168|  2064.744| 24.580|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   948|  8284.251| 92.380| 114,434|
| |Flathead County|     2| 19.267|  0.000|   352|  3390.941| 110.095| 103,806|
| |Richland County|     2| 185.134| 13.224|    47|  4350.643| 13.224|  10,803|
| |Lincoln County|     2| 100.100|  0.000|    77|  3853.854| 42.900|  19,980|
| |Lewis and Clark County|     2| 28.805|  2.058|   162|  2333.218| 34.978|  69,432|
| |Hill County|     2| 121.330| 17.333|    43|  2608.590| 17.333|  16,484|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 100.233|  11,402|
| |Madison County|     1| 116.279|  0.000|    84|  9767.442| 99.668|   8,600|
| |Missoula County|     1|  8.361|  0.000|   328|  2742.475| 72.862| 119,600|
| |Lake County|     1| 32.832|  0.000|   183|  6008.274| 65.664|  30,458|
| |Glacier County|     1| 72.711|  0.000|    77|  5598.778| 197.360|  13,753|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972| 38.228|   3,737|
| |Stillwater County|     1| 103.713| 14.816|    26|  2696.536| 88.897|   9,642|
| |Ravalli County|     1| 22.828|  0.000|    83|  1894.718| 29.350|  43,806|
| |Rosebud County|     1| 111.894|  0.000|    34|  3804.409| 175.834|   8,937|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 86.345|   3,309|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Sanders County|     0|  0.000|  0.000|     9|   743.003|  0.000|  12,113|
| |Silver Bow County|     0|  0.000|  0.000|   101|  2892.740| 139.113|  34,915|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Valley County|     0|  0.000|  0.000|    23|  3109.789| 193.155|   7,396|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Dawson County|     0|  0.000|  0.000|    20|  2322.071| 66.345|   8,613|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 76.055|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Carbon County|     0|  0.000|  0.000|    73|  6806.527| 173.160|  10,725|
| |Broadwater County|     0|  0.000|  0.000|    12|  1924.002| 22.905|   6,237|
| |Blaine County|     0|  0.000|  0.000|    11|  1646.460| 42.765|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    64|  6770.337| 211.573|   9,453|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fergus County|     0|  0.000|  0.000|    14|  1266.968| 90.498|  11,050|
| |Jefferson County|     0|  0.000|  0.000|    29|  2372.965| 23.379|  12,221|
| |Granite County|     0|  0.000|  0.000|    17|  5031.074| 380.501|   3,379|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Roosevelt County|     0|  0.000|  0.000|    23|  2090.149| 38.947|  11,004|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Deer Lodge County|     0|  0.000|  0.000|    25|  2735.230| 46.890|   9,140|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 48.336|   5,911|
| |Phillips County|     0|  0.000|  0.000|    55| 13909.965| 1987.138|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    55|  3312.056| 25.808|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 257.555|   1,664|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,464|  2346.195| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   735|  4487.892| 10.467| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  2.892|  49,402|
| |Windham County|     3| 71.053|  0.000|   104|  2463.171| 10.150|  42,222|
| |Addison County|     2| 54.382|  0.000|    74|  2012.127|  3.884|  36,777|
| |Windsor County|     2| 36.323|  0.000|    72|  1307.617|  2.594|  55,062|
| |Washington County|     2| 34.241|  0.000|    53|   907.394|  7.337|  58,409|
| |Bennington County|     1| 28.193|  0.000|    90|  2537.356| 24.165|  35,470|
| |Rutland County|     1| 17.185|  0.000|    99|  1701.294| 24.550|  58,191|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Orange County|     0|  0.000|  0.000|    15|   519.175|  0.000|  28,892|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    33| 23.307| N/A| 3,733|  2636.538| N/A|1,415,872|
| |Honolulu County|    27| 27.705| N/A| 3,361|  3448.725| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   190|  1134.891| 10.240| 167,417|
| |Kauai County|     0|  0.000|  0.000|    49|   677.797|  3.952|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   133|   660.007|  7.798| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,073|  5309.637| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    24|  2841.918| 33.832|   8,445|
| |Fremont County|     0|  0.000|  0.000|   497| 12658.873| 21.832|  39,261|
| |Goshen County|     0|  0.000|  0.000|    34|  2573.613| 151.389|  13,211|
| |Laramie County|     0|  0.000|  0.000|   500|  5025.126| 22.972|  99,500|
| |Lincoln County|     0|  0.000|  0.000|   103|  5194.150| 72.041|  19,830|
| |Natrona County|     0|  0.000|  0.000|   238|  2980.290| 25.044|  79,858|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565|  0.000|   7,584|
| |Converse County|     0|  0.000|  0.000|    31|  2242.801|  0.000|  13,822|
| |Carbon County|     0|  0.000|  0.000|   103|  6959.459| 183.398|  14,800|
| |Campbell County|     0|  0.000|  0.000|   129|  2783.712| 33.910|  46,341|
| |Park County|     0|  0.000|  0.000|   135|  4624.238| 88.081|  29,194|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 161.859|   4,413|
| |Albany County|     0|  0.000|  0.000|    88|  2263.374|  0.000|  38,880|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Uinta County|     0|  0.000|  0.000|   279| 13794.126| 84.757|  20,226|
| |Teton County|     0|  0.000|  0.000|   372| 15854.074| 60.884|  23,464|
| |Sweetwater County|     0|  0.000|  0.000|   267|  6305.647| 53.981|  42,343|
| |Sublette County|     0|  0.000|  0.000|    39|  3967.043|  0.000|   9,831|
| |Washakie County|     0|  0.000|  0.000|    79| 10121.717| 457.582|   7,805|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    73|  2394.620| 51.548|  30,485|
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
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
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
|RI|5 counties|     0|  0.000| N/A|17,860| 16859.220| N/A|1,059,361|
| |Washington County|     0|  0.000|  0.000|   607|  4833.688| 19.339| 125,577|
| |Providence County|     0|  0.000|  0.000|15,047| 23550.274| 111.347| 638,931|
| |Newport County|     0|  0.000|  0.000|   396|  4824.444| 27.847|  82,082|
| |Kent County|     0|  0.000|  0.000| 1,494|  9093.565| 63.476| 164,292|
| |Bristol County|     0|  0.000|  0.000|   316|  6518.286| 35.361|  48,479|


