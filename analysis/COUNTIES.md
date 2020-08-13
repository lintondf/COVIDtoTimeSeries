# Analysis of US By County #

Updated: at 2020-08-13

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 132,682 deaths (459.645 deaths/million) and 4,469,153 confirmed cases (15482.301 confirmed cases/million).  This group accounts for 81.09% of all US deaths and for 87.50% of all US cases.

24.53% of this group's deaths (19.89% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.37% of this group's deaths (20.57% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,435 (12.66% of the total US population):



The next 25.02% of this group's deaths (20.29% of the total US deaths) occured in 90 counties in 31 states with a combined population of 67,694,016 (20.62% of the total US population)

The remaining 25.09% of this group's deaths (20.34% of the total US deaths) occured in 853 counties in 50 states with a combined population of 142,112,390 (43.30% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,473 deaths (264.620 deaths/million) and 469,506 confirmed cases (11862.963 confirmed cases/million).  This group accounts for 6.40% of all US deaths and for 9.19% of all US cases.

24.85% of this group's deaths (1.59% of the total US deaths) occured in 60 counties in 16 states with a combined population of 1,996,612 (0.61% of the total US population):



The next 25.11% of this group's deaths (1.61% of the total US deaths) occured in 116 counties in 28 states with a combined population of 3,411,596 (1.04% of the total US population):



The next 25.01% of this group's deaths (1.60% of the total US deaths) occured in 236 counties in 34 states with a combined population of 5,807,110 (1.77% of the total US population)

The remaining 25.03% of this group's deaths (1.60% of the total US deaths) occured in 1,740 counties in 47 states with a combined population of 28,362,146 (8.64% of the total US population) 

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
|NJ|21 counties|15,885| 1788.410| N/A|185,198| 20850.488| N/A|8,882,190|
| |Essex County| 2,110| 2640.884|  0.894|19,813| 24798.022| 36.118| 798,975|
| |Bergen County| 2,036| 2184.076|  0.000|20,899| 22418.961| 39.844| 932,202|
| |Hudson County| 1,505| 2238.281|  0.637|19,749| 29371.303| 39.305| 672,391|
| |Middlesex County| 1,409| 1707.750|  1.558|17,988| 21801.998| 32.898| 825,062|
| |Union County| 1,348| 2422.974|  0.257|16,780| 30161.358| 44.936| 556,341|
| |Passaic County| 1,242| 2474.961|  0.854|17,748| 35366.840| 56.366| 501,826|
| |Ocean County| 1,020| 1679.881|  0.941|10,652| 17543.224| 31.057| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,368| 16755.145| 40.632| 618,795|
| |Morris County|   829| 1685.490|  0.581| 7,286| 14813.610| 26.431| 491,845|
| |Mercer County|   621| 1690.118|  1.166| 8,143| 22162.044| 26.050| 367,430|
| |Camden County|   579| 1143.205|  0.564| 8,645| 17069.092| 57.259| 506,471|
| |Somerset County|   564| 1714.630|  1.303| 5,275| 16036.652| 31.704| 328,934|
| |Burlington County|   473| 1062.088|  0.962| 6,069| 13627.515| 51.966| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,509| 13308.302| 39.552| 263,670|
| |Gloucester County|   214| 733.791|  2.449| 3,310| 11349.765| 71.518| 291,636|
| |Sussex County|   198| 1409.373|  1.017| 1,341|  9545.299| 25.422| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,347| 12796.033| 14.928| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,377| 22584.550| 83.119| 149,527|
| |Hunterdon County|   124| 997.017|  0.000| 1,150|  9246.529|  6.892| 124,371|
| |Cape May County|    88| 956.116|  1.552|   842|  9148.296| 35.699|  92,039|
| |Salem County|    87| 1394.566|  2.290|   907| 14538.751| 59.538|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,323| 633.459| N/A|253,546| 13033.395| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,761| 32250.148| 29.373|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.097|43,948| 29762.949| 38.215|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.148|36,324| 37543.953| 36.766| 967,506|
| |Queens County|   985| 437.042|  0.778| 7,899|  3504.872| 18.054|2,253,858|
| |Kings County|   931| 363.652|  0.648| 1,356|   529.601|  2.728|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,966| 42868.237| 27.625| 325,789|
| |Erie County|   671| 730.378|  0.000| 9,013|  9810.581| 48.360| 918,702|
| |Bronx County|   649| 457.906|  0.816|26,902| 18968.930| 97.710|1,418,207|
| |Orange County|   491| 1275.523|  0.000|11,191| 29072.063| 28.947| 384,940|
| |New York County|   415| 254.538|  0.453|15,515|  9526.198| 49.070|1,628,706|
| |Monroe County|   285| 384.216|  0.000| 5,035|  6787.818| 37.362| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,613|  7845.343| 27.298| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,631| 15740.030| 30.590| 294,218|
| |Richmond County|   148| 311.080|  0.554| 7,899| 16590.572| 85.459| 476,143|
| |Albany County|   128| 418.977|  0.000| 2,624|  8589.029| 31.797| 305,506|
| |Oneida County|   115| 502.906|  0.000| 2,180|  9533.347| 41.232| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,514|  7234.293| 32.765| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,077| 11696.598| 30.571| 177,573|
| |Broome County|    69| 362.228|  0.000| 1,150|  6037.126| 50.997| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,450| 14747.762| 15.983|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   298|  7385.012|  3.540|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,491| 19766.147| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   300|  3145.346|  4.493|  95,379|
| |Schenectady County|    37| 238.250|  0.000| 1,079|  6947.888| 31.276| 155,299|
| |Columbia County|    37| 622.257|  0.000|   548|  9216.125| 40.843|  59,461|
| |Ontario County|    34| 309.719|  0.000|   363|  3306.704| 14.315| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269| 17.873|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   780|  4914.500| 22.502| 158,714|
| |Tioga County|    25| 518.640|  0.000|   194|  4024.646|  2.964|  48,203|
| |Fulton County|    24| 449.581|  0.000|   299|  5601.034| 32.113|  53,383|
| |Greene County|    18| 381.453|  0.000|   295|  6251.589| 18.164|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   768|  3341.121| 14.916| 229,863|
| |Madison County|    17| 239.636|  0.000|   414|  5835.835| 16.110|  70,941|
| |Washington County|    14| 228.743|  0.000|   260|  4248.088| 11.671|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   258|  2033.049| 19.137| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470| 11.353|  62,914|
| |Yates County|     7| 280.978|  0.000|    57|  2287.962|  5.734|  24,913|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959| 18.157|  47,207|
| |Cattaraugus County|     6| 78.826|  0.000|   168|  2207.128|  7.507|  76,117|
| |Genesee County|     5| 87.291|  0.000|   280|  4888.268| 14.964|  57,280|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  7.204|  59,493|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436| 14.336|  39,859|
| |Delaware County|     4| 90.631|  0.000|   106|  2401.722|  6.474|  44,135|
| |Clinton County|     4| 49.699|  0.000|   129|  1602.783|  3.550|  80,485|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  1.326| 107,740|
| |Montgomery County|     4| 81.266|  0.000|   177|  3596.026| 46.438|  49,221|
| |Herkimer County|     4| 65.233|  0.000|   277|  4517.360| 30.287|  61,319|
| |Chemung County|     3| 35.947|  0.000|   177|  2120.878| 20.541|  83,456|
| |Seneca County|     3| 88.194|  0.000|    91|  2675.212| 20.999|  34,016|
| |Wayne County|     3| 33.364|  0.000|   258|  2869.281| 15.887|  89,918|
| |Oswego County|     3| 25.614|  0.000|   257|  2194.256|  8.538| 117,124|
| |Cayuga County|     2| 26.118|  0.000|   161|  2102.486| 20.521|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697| 12.398|  46,091|
| |Lewis County|     0|  0.000|  0.000|    46|  1749.315| 48.894|  26,296|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  4.194| 102,180|
| |Jefferson County|     0|  0.000|  0.000|   142|  1292.860|  2.601| 109,834|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525|  5.712|  50,022|
| |Essex County|     0|  0.000|  0.000|    56|  1518.232|  3.873|  36,885|
| |Cortland County|     0|  0.000|  0.000|    96|  2017.612|  6.005|  47,581|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,753| 272.144| N/A|591,376| 14966.913| N/A|39,512,223|
| |Los Angeles County| 5,112| 509.209|  4.056|214,283| 21344.827| 229.360|10,039,107|
| |Riverside County|   824| 333.530|  4.973|43,376| 17557.253| 282.702|2,470,546|
| |Orange County|   745| 234.595|  3.599|41,823| 13169.728| 166.083|3,175,692|
| |San Diego County|   602| 180.330|  1.455|33,157|  9932.212| 113.016|3,338,330|
| |San Bernardino County|   555| 254.577|  4.456|38,290| 17563.535| 265.586|2,180,085|
| |Imperial County|   252| 1390.613| 15.767| 9,919| 54736.087| 320.062| 181,215|
| |San Joaquin County|   235| 308.339|  8.997|13,870| 18198.565| 344.140| 762,148|
| |Alameda County|   209| 125.050|  1.368|14,112|  8443.580| 168.899|1,671,329|
| |Santa Clara County|   207| 107.373|  1.112|12,962|  6723.545| 143.165|1,927,852|
| |Tulare County|   205| 439.730|  3.677|11,643| 24974.528| 479.566| 466,195|
| |Fresno County|   191| 191.172|  4.862|17,978| 17994.177| 290.690| 999,101|
| |Kern County|   183| 203.288|  4.920|25,179| 27970.389| 594.470| 900,202|
| |Sacramento County|   179| 115.331|  2.853|12,274|  7908.210| 193.292|1,552,058|
| |Stanislaus County|   177| 321.432| 10.896|10,855| 19712.708| 401.337| 550,660|
| |Contra Costa County|   149| 129.169|  2.229|10,103|  8758.363| 220.318|1,153,526|
| |San Mateo County|   122| 159.150|  0.373| 6,535|  8524.955| 144.800| 766,573|
| |Ventura County|    93| 109.928|  2.702| 8,740| 10330.896| 145.727| 846,006|
| |Marin County|    81| 312.952|  2.760| 5,471| 21137.753| 160.615| 258,826|
| |Merced County|    74| 266.494| 11.833| 6,102| 21974.935| 781.475| 277,680|
| |Santa Barbara County|    73| 163.494|  2.880| 7,074| 15843.261| 175.332| 446,499|
| |San Francisco County|    67| 76.003| N/A| 7,834|  8886.630| N/A| 881,549|
| |Kings County|    62| 405.388|  5.604| 5,067| 33130.639| 573.521| 152,940|
| |Sonoma County|    51| 103.169|  2.601| 3,825|  7737.652| 178.306| 494,336|
| |Yolo County|    45| 204.082|  1.944| 1,898|  8607.710| 183.997| 220,500|
| |Solano County|    41| 91.591|  0.957| 4,338|  9690.758| 169.778| 447,643|
| |Madera County|    40| 254.248|  7.264| 2,590| 16462.527| 432.221| 157,327|
| |Monterey County|    39| 89.849|  1.646| 5,628| 12965.920| 217.876| 434,061|
| |Placer County|    24| 60.252|  1.793| 2,377|  5967.429| 135.925| 398,329|
| |San Luis Obispo County|    17| 60.047|  0.505| 2,300|  8124.022| 166.517| 283,111|
| |Napa County|    11| 79.858|  2.074| 1,142|  8290.742| 140.011| 137,744|
| |Shasta County|    10| 55.531|  0.793|   469|  2604.398| 51.564| 180,080|
| |Mendocino County|    10| 115.275|  1.647|   478|  5510.150| 225.610|  86,749|
| |Amador County|    10| 251.560| 35.937|   195|  4905.414| 208.435|  39,752|
| |Butte County|     8| 36.499|  0.000| 1,280|  5839.789| 174.672| 219,186|
| |Sutter County|     7| 72.187|  1.473| 1,019| 10508.296| 263.702|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,316|  4816.755| 62.745| 273,213|
| |Inyo County|     5| 277.177| 31.677|   113|  6264.205| 372.209|  18,039|
| |Colusa County|     5| 232.051|  6.630|   397| 18424.839| 251.941|  21,547|
| |San Benito County|     4| 63.686|  0.000|   767| 12211.820| 177.411|  62,808|
| |Yuba County|     4| 50.847|  0.000|   678|  8618.498| 263.313|  78,668|
| |Humboldt County|     4| 29.508|  0.000|   293|  2161.436| 50.585| 135,558|
| |Glenn County|     3| 105.660|  5.031|   436| 15355.898| 452.828|  28,393|
| |Tuolumne County|     2| 36.712|  0.000|   159|  2918.609| 39.334|  54,478|
| |Mariposa County|     2| 116.259|  0.000|    63|  3662.152| 33.217|  17,203|
| |Lake County|     2| 31.063|  2.219|   253|  3929.426| 93.188|  64,386|
| |El Dorado County|     2| 10.371|  0.741|   785|  4070.669| 86.673| 192,843|
| |Tehama County|     1| 15.365|  0.000|   304|  4670.887| 120.723|  65,084|
| |Calaveras County|     1| 21.784|  0.000|   161|  3507.243| 77.800|  45,905|
| |Mono County|     1| 69.233|  0.000|   160| 11077.264| 138.466|  14,444|
| |Nevada County|     1| 10.025|  0.000|   357|  3578.768| 58.715|  99,755|
| |Trinity County|     0|  0.000|  0.000|     6|   488.400| 11.629|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   106|  2434.599| 59.060|  43,539|
| |Sierra County|     0|  0.000|  0.000|     5|  1663.894| 95.080|   3,005|
| |Plumas County|     0|  0.000|  0.000|    37|  1967.353| 30.384|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 16.158|   8,841|
| |Lassen County|     0|  0.000|  0.000|   683| 22339.973| 238.306|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   104|  3739.393| 71.911|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 9,527| 328.564| N/A|523,977| 18070.739| N/A|28,995,881|
| |Harris County| 1,679| 356.224| 26.490|88,494| 18775.281| 229.744|4,713,325|
| |Hidalgo County|   881| 1014.151| 22.694|20,767| 23905.644| 340.078| 868,707|
| |Bexar County|   826| 412.267| 10.909|43,455| 21688.959| 131.267|2,003,554|
| |Dallas County|   794| 301.269|  3.686|55,787| 21167.392| 170.636|2,635,516|
| |Cameron County|   485| 1146.130| 30.721|17,069| 40336.702| 508.078| 423,163|
| |Tarrant County|   469| 223.066|  4.009|32,666| 15536.631| 170.136|2,102,515|
| |Travis County|   313| 245.692|  2.916|23,421| 18384.494| 156.655|1,273,954|
| |El Paso County|   310| 369.383|  5.107|17,210| 20506.698| 303.507| 839,238|
| |Nueces County|   259| 714.889| 16.561|16,234| 44808.912| 1148.633| 362,294|
| |Webb County|   179| 647.022| 18.073| 8,814| 31859.520| 875.262| 276,652|
| |Fort Bend County|   173| 213.136|  3.872|10,487| 12919.989| 339.328| 811,688|
| |Galveston County|   116| 339.043|  4.175| 9,707| 28371.510| 225.055| 342,139|
| |Brazoria County|   100| 267.191|  6.107| 7,591| 20282.474| 268.718| 374,264|
| |Williamson County|    98| 165.947|  3.629| 7,075| 11980.337| 272.385| 590,551|
| |Montgomery County|    95| 156.407|  4.469| 6,820| 11228.352| 84.906| 607,391|
| |Denton County|    95| 107.078|  2.415| 7,959|  8970.849| 113.035| 887,207|
| |Collin County|    93| 89.879|  1.104| 8,313|  8033.980| 201.019|1,034,730|
| |Jefferson County|    88| 349.810|  7.950| 6,067| 24117.027| 196.484| 251,565|
| |Starr County|    79| 1222.286| 59.678| 2,264| 35028.546| 528.257|  64,633|
| |Lubbock County|    75| 241.492|  3.680| 6,295| 20269.248| 250.232| 310,569|
| |Comal County|    72| 460.921|  4.573| 1,929| 12348.840| 191.136| 156,209|
| |McLennan County|    58| 226.012|  8.350| 5,106| 19896.892| 229.353| 256,623|
| |Ector County|    57| 342.913|  4.297| 3,670| 22078.774| 162.432| 166,223|
| |Guadalupe County|    56| 335.637|  6.850| 1,723| 10326.826| 62.504| 166,847|
| |Victoria County|    52| 564.702| 27.925| 3,543| 38475.740| 328.892|  92,084|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 326.364|  49,025|
| |Midland County|    49| 277.099|  3.231| 2,788| 15766.377| 239.129| 176,832|
| |Brazos County|    49| 213.777|  1.870| 4,107| 17917.988| 83.516| 229,211|
| |Ellis County|    48| 259.704|  8.502| 3,218| 17410.970| 407.333| 184,826|
| |Angelina County|    47| 542.005| 14.827| 1,869| 21553.364| 187.807|  86,715|
| |Potter County|    45| 383.256|  2.433| 3,731| 31776.179| 150.869| 117,415|
| |Bell County|    44| 121.238|  4.330| 4,036| 11120.786| 140.132| 362,924|
| |Maverick County|    44| 749.293| 36.492| 2,321| 39525.221| 1140.969|  58,722|
| |Nacogdoches County|    42| 644.132|  8.764| 1,171| 17959.021| 227.856|  65,204|
| |Walker County|    42| 575.571|  3.915| 3,095| 42414.110| 503.135|  72,971|
| |Hays County|    42| 182.457|  4.344| 5,083| 22081.663| 70.749| 230,191|
| |Washington County|    39| 1086.896|  3.981|   520| 14491.946| 87.589|  35,882|
| |Bowie County|    36| 386.080|  7.660|   775|  8311.438| 102.648|  93,245|
| |Liberty County|    34| 385.405|  6.477| 1,041| 11800.179| 278.528|  88,219|
| |Hale County|    31| 927.977| 29.935| 1,439| 43076.094| 833.896|  33,406|
| |San Patricio County|    31| 464.559| 25.690|   972| 14566.162| 224.786|  66,730|
| |Matagorda County|    31| 846.001| 31.189|   786| 21450.209| 366.470|  36,643|
| |Johnson County|    31| 176.320|  0.813| 2,037| 11585.910| 249.448| 175,817|
| |Willacy County|    30| 1404.626| 60.198|   720| 33711.022| 508.341|  21,358|
| |Medina County|    29| 562.190| 13.847|   934| 18106.390| 883.441|  51,584|
| |Gregg County|    28| 225.907|  6.916| 1,589| 12820.203| 277.773| 123,945|
| |Tom Green County|    28| 234.899|  4.794| 2,775| 23280.201| 313.998| 119,200|
| |Caldwell County|    28| 641.261| 13.087| 1,163| 26635.214| 219.206|  43,664|
| |Smith County|    28| 120.300|  6.138| 2,612| 11222.293| 120.300| 232,751|
| |Taylor County|    28| 202.849|  7.245| 1,137|  8237.101| 32.083| 138,034|
| |Kaufman County|    27| 198.305|  5.246| 2,321| 17046.873| 329.459| 136,154|
| |Wharton County|    26| 625.662|  3.438|   862| 20743.094| 749.419|  41,556|
| |Grimes County|    25| 865.651| 24.733|   895| 30990.305| 168.184|  28,880|
| |Harrison County|    24| 360.615|  4.293|   711| 10683.215| 143.817|  66,553|
| |Orange County|    23| 275.793|  8.565| 1,493| 17902.537| 212.412|  83,396|
| |Bastrop County|    22| 247.963|  3.220| 1,390| 15666.738| 123.981|  88,723|
| |Lavaca County|    22| 1091.595| 56.706|   635| 31507.393| 70.883|  20,154|
| |Randall County|    21| 152.491|  3.112| 1,765| 12816.510| 123.445| 137,713|
| |Hunt County|    21| 212.995|  0.000| 1,202| 12191.411| 140.548|  98,594|
| |DeWitt County|    20| 992.063| 35.431|   716| 35515.873| 531.463|  20,160|
| |Wilson County|    19| 372.038|  5.595|   458|  8968.083| 78.324|  51,070|
| |Parker County|    19| 132.981|  3.999| 1,329|  9301.642| 168.975| 142,878|
| |Atascosa County|    19| 371.435|  8.378|   487|  9520.458| 189.906|  51,153|
| |Deaf Smith County|    18| 970.560|  7.703|   680| 36665.588| 392.846|  18,546|
| |Panola County|    18| 776.063|  6.159|   297| 12805.036| 147.821|  23,194|
| |Shelby County|    18| 712.194|  0.000|   406| 16063.939| 90.437|  25,274|
| |Lamar County|    18| 361.018|  5.730|   668| 13397.782| 74.496|  49,859|
| |Brown County|    17| 448.975|  7.546|   402| 10616.945| 173.553|  37,864|
| |Jim Wells County|    16| 395.237| 10.587|   787| 19440.739| 455.229|  40,482|
| |Hardin County|    16| 277.768| 12.400|   999| 17343.148| 240.567|  57,602|
| |Aransas County|    16| 680.561| 24.306|   183|  7783.922| 127.605|  23,510|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Rockwall County|    15| 142.973|  4.085| 1,033|  9846.066| 336.327| 104,915|
| |Moore County|    14| 668.577| 13.644| 1,064| 50811.843| 197.844|  20,940|
| |Fayette County|    14| 552.355|  0.000|   390| 15387.043| 78.908|  25,346|
| |Lamb County|    14| 1085.861| 44.321|   233| 18071.822| 221.604|  12,893|
| |Anderson County|    14| 242.487|  9.897| 2,428| 42054.213| 180.628|  57,735|
| |Grayson County|    13| 95.439|  2.098| 1,191|  8743.723| 146.830| 136,212|
| |Polk County|    13| 253.150|  5.564|   762| 14838.471| 191.949|  51,353|
| |Jasper County|    12| 337.752| 28.146|   332|  9344.479| 120.626|  35,529|
| |Bee County|    12| 368.494| 13.160| 1,277| 39213.880| 2548.749|  32,565|
| |Henderson County|    12| 145.038|  1.727|   657|  7940.825| 82.879|  82,737|
| |San Augustine County|    11| 1335.438|  0.000|   175| 21245.599| 312.180|   8,237|
| |Lee County|    11| 638.088| 16.574|   177| 10267.417| 116.016|  17,239|
| |Red River County|    11| 914.913|  0.000|   137| 11394.827| 23.764|  12,023|
| |Wichita County|    11| 83.188|  0.000| 1,056|  7986.085| 118.841| 132,230|
| |Burnet County|    10| 207.663|  8.900|   571| 11857.543| 80.098|  48,155|
| |Gonzales County|    10| 479.916|  6.856|   699| 33546.096| 363.365|  20,837|
| |Hood County|    10| 162.224|  2.317|   588|  9538.796| 227.114|  61,643|
| |Uvalde County|    10| 373.958| 16.027|   562| 21016.417| 299.166|  26,741|
| |Marion County|     9| 913.335| 14.497|   134| 13598.539| 86.984|   9,854|
| |Palo Pinto County|     9| 308.335| 14.683|   304| 10414.882| 332.806|  29,189|
| |Navarro County|     9| 179.594|  2.851|   905| 18059.186| 270.817|  50,113|
| |Jackson County|     9| 609.756| 38.715|   411| 27845.528| 300.039|  14,760|
| |Wise County|     8| 114.312|  4.083|   475|  6787.266| 224.541|  69,984|
| |Kleberg County|     8| 260.756|  9.313|   459| 14960.887| 325.945|  30,680|
| |Fannin County|     8| 225.263|  0.000|   269|  7574.478| 128.722|  35,514|
| |San Jacinto County|     8| 277.210|  0.000|   182|  6306.525| 34.651|  28,859|
| |Cherokee County|     8| 151.958|  8.141| 1,167| 22166.926| 909.037|  52,646|
| |Wood County|     8| 175.674|  9.411|   345|  7575.924| 100.385|  45,539|
| |Cass County|     8| 266.436|  4.758|   185|  6161.327| 118.945|  30,026|
| |Hill County|     7| 191.001|  7.796|   331|  9031.624| 70.164|  36,649|
| |Houston County|     7| 304.772|  6.220|   318| 13845.350| 68.418|  22,968|
| |Parmer County|     7| 728.787|  0.000|   349| 36335.242| 386.703|   9,605|
| |Andrews County|     7| 374.231|  7.637|   304| 16252.339| 236.759|  18,705|
| |Karnes County|     7| 448.689| 18.314|   646| 41407.602| 2335.015|  15,601|
| |Floyd County|     6| 1050.420| 25.010|    90| 15756.303| 100.040|   5,712|
| |Burleson County|     6| 325.327|  0.000|   247| 13392.615| 92.950|  18,443|
| |Duval County|     6| 537.779| 12.804|   191| 17119.297| 384.128|  11,157|
| |Gillespie County|     6| 222.321|  5.293|   177|  6558.470| 15.880|  26,988|
| |Zavala County|     6| 506.757| 12.066|   233| 19679.054| 434.363|  11,840|
| |Howard County|     6| 163.648| 11.689|   178|  4854.899| 62.342|  36,664|
| |Sabine County|     6| 569.152|  0.000|    62|  5881.237| 149.064|  10,542|
| |Kerr County|     6| 114.068|  0.000|   404|  7680.608| 54.318|  52,600|
| |Calhoun County|     6| 281.822| 13.420|   547| 25692.814| 241.562|  21,290|
| |Camp County|     6| 458.225| 10.910|   239| 18252.635| 218.202|  13,094|
| |Erath County|     5| 117.102|  0.000|   564| 13209.050| 250.932|  42,698|
| |Blanco County|     5| 419.076|  0.000|   114|  9554.941| 191.578|  11,931|
| |Goliad County|     5| 652.912| 18.655|    96| 12535.910| 354.438|   7,658|
| |Frio County|     5| 246.233|  0.000|   516| 25411.209| 147.740|  20,306|
| |Dallam County|     5| 686.153|  0.000|   195| 26759.984| 235.253|   7,287|
| |Young County|     5| 277.624|  7.932|   190| 10549.695| 301.420|  18,010|
| |Martin County|     5| 866.401| 49.509|    64| 11089.932| 396.069|   5,771|
| |Waller County|     5| 90.504|  2.586|   485|  8778.916| 175.837|  55,246|
| |Coryell County|     5| 65.832|  0.000|   696|  9163.803| 112.855|  75,951|
| |Reeves County|     5| 312.969|  8.942|   148|  9263.896| 44.710|  15,976|
| |Kendall County|     4| 84.333|  0.000|   165|  3478.738| 30.119|  47,431|
| |Dawson County|     4| 314.268|  0.000|   157| 12335.009| 224.477|  12,728|
| |Lynn County|     4| 672.156|  0.000|    74| 12434.885| 192.045|   5,951|
| |Hockley County|     4| 173.754|  0.000|   216|  9382.738| 155.138|  23,021|
| |Live Oak County|     4| 327.681| 23.406|   236| 19333.169| 163.840|  12,207|
| |Brooks County|     4| 563.936| 60.422|   135| 19032.849| 825.764|   7,093|
| |Austin County|     4| 133.191|  4.757|   287|  9556.473| 328.221|  30,032|
| |Chambers County|     4| 91.247|  6.518|   993| 22652.098| 224.859|  43,837|
| |Castro County|     4| 531.208|  0.000|   205| 27224.436| 322.519|   7,530|
| |Newton County|     4| 294.226|  0.000|   116|  8532.549| 252.194|  13,595|
| |Refugio County|     4| 575.705| 61.683|   235| 33822.683| 390.657|   6,948|
| |Trinity County|     4| 273.019|  9.751|   157| 10715.992| 39.003|  14,651|
| |Dimmit County|     4| 395.101| 14.111|   158| 15606.480| 282.215|  10,124|
| |Bailey County|     4| 571.429|  0.000|   179| 25571.429| 265.306|   7,000|
| |Van Zandt County|     4| 70.684|  2.524|   432|  7633.858| 176.710|  56,590|
| |Zapata County|     3| 211.581| 10.075|   179| 12624.304| 141.054|  14,179|
| |Yoakum County|     3| 344.313| 16.396|   114| 13083.898| 393.501|   8,713|
| |Bandera County|     3| 129.803|  0.000|    93|  4023.884| 24.724|  23,112|
| |Falls County|     3| 173.440|  0.000|   139|  8036.076| 206.477|  17,297|
| |Cooke County|     3| 72.715|  0.000|   252|  6108.054| 159.280|  41,257|
| |Hopkins County|     3| 80.897|  7.705|   205|  5527.991| 84.750|  37,084|
| |Hutchinson County|     3| 143.280|  6.823|   129|  6161.047| 61.406|  20,938|
| |Milam County|     3| 120.856|  0.000|   355| 14301.253| 161.141|  24,823|
| |Morris County|     3| 242.170| 23.064|   127| 10251.857| 334.425|  12,388|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402|  0.000|   6,229|
| |Lampasas County|     3| 140.004|  6.667|   114|  5320.142| 186.672|  21,428|
| |Leon County|     3| 172.374|  8.208|   145|  8331.418| 57.458|  17,404|
| |Comanche County|     3| 220.022|  0.000|   160| 11734.507| 408.612|  13,635|
| |Gaines County|     3| 139.587| 19.941|   186|  8654.383| 272.527|  21,492|
| |Nolan County|     3| 203.887|  0.000|   136|  9242.898| 38.836|  14,714|
| |Callahan County|     3| 215.162|  0.000|    48|  3442.588| 20.492|  13,943|
| |Crockett County|     3| 866.051|  0.000|   156| 45034.642|  0.000|   3,464|
| |Reagan County|     3| 779.423|  0.000|    64| 16627.696| 111.346|   3,849|
| |Limestone County|     3| 128.003|  0.000|   258| 11008.235| 347.436|  23,437|
| |Hamilton County|     3| 354.568| 16.884|    89| 10518.851| 574.063|   8,461|
| |Stephens County|     3| 320.307| 15.253|    49|  5231.689| 274.549|   9,366|
| |Robertson County|     2| 117.137|  0.000|   236| 13822.186| 133.871|  17,074|
| |Rusk County|     2| 36.761|  0.000|   384|  7058.045| 112.908|  54,406|
| |Runnels County|     2| 194.856| 13.918|   140| 13639.906| 334.039|  10,264|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Terry County|     2| 162.114|  0.000|   161| 13050.174| 416.864|  12,337|
| |Upshur County|     2| 47.901|  0.000|   257|  6155.246| 195.024|  41,753|
| |Colorado County|     2| 93.054|  0.000|   333| 15493.416| 505.148|  21,493|
| |Madison County|     2| 140.017|  0.000|   676| 47325.679| 310.037|  14,284|
| |Montague County|     2| 100.918|  7.208|    79|  3986.275| 129.752|  19,818|
| |Presidio County|     2| 298.329| 42.618|    47|  7010.740| 42.618|   6,704|
| |Crane County|     2| 416.927|  0.000|    71| 14800.917| 29.781|   4,797|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 84.356|   3,387|
| |Swisher County|     2| 270.380|  0.000|    82| 11085.575| 57.939|   7,397|
| |Gray County|     2| 91.383|  0.000|   218|  9960.705| 84.855|  21,886|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461| 15.523|   9,203|
| |Knox County|     2| 545.852| 77.979|    61| 16648.472| 311.915|   3,664|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 113.982|   7,520|
| |Tyler County|     2| 92.285|  0.000|   127|  5860.096| 79.101|  21,672|
| |Hudspeth County|     2| 409.333|  0.000|    33|  6753.991| 321.619|   4,886|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890|  0.000|   1,501|
| |Bosque County|     2| 107.038|  0.000|   174|  9312.283| 290.531|  18,685|
| |Hansford County|     2| 370.439|  0.000|    82| 15187.998| 635.038|   5,399|
| |Ochiltree County|     2| 203.335|  0.000|    99| 10065.067| 145.239|   9,836|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 39.960|  10,725|
| |Pecos County|     2| 126.398|  9.028|   249| 15736.586| 207.654|  15,823|
| |Culberson County|     2| 921.234|  0.000|    18|  8291.110| 131.605|   2,171|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Kimble County|     1| 230.574| 32.939|    14|  3228.038| 32.939|   4,337|
| |Hall County|     1| 337.382|  0.000|    14|  4723.347| 192.790|   2,964|
| |McCulloch County|     1| 125.251|  0.000|    53|  6638.277| 143.143|   7,984|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505| 19.664|  21,795|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 45.663|  12,514|
| |Winkler County|     1| 124.844|  0.000|    85| 10611.735| 267.523|   8,010|
| |Fisher County|     1| 261.097|  0.000|    29|  7571.802| 111.899|   3,830|
| |Mitchell County|     1| 117.028| 16.718|    69|  8074.898| 183.900|   8,545|
| |Real County|     1| 289.687| 41.384|    88| 25492.468| 82.768|   3,452|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 51.148|   2,793|
| |Scurry County|     1| 59.869|  0.000|   488| 29216.308| 290.795|  16,703|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Jim Hogg County|     1| 192.308|  0.000|    64| 12307.692| 274.725|   5,200|
| |Ward County|     1| 83.347|  0.000|    93|  7751.292| 107.161|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Sutton County|     1| 264.831|  0.000|    66| 17478.814| 226.998|   3,776|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Wilbarger County|     1| 78.315|  0.000|    77|  6030.229| 234.944|  12,769|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Eastland County|     1| 54.466|  0.000|    83|  4520.697| 155.618|  18,360|
| |Clay County|     1| 95.502|  0.000|    43|  4106.580| 95.502|  10,471|
| |Crosby County|     1| 174.307|  0.000|    63| 10981.349| 124.505|   5,737|
| |Baylor County|     0|  0.000|  0.000|    12|  3419.778| 162.847|   3,509|
| |Carson County|     0|  0.000|  0.000|    16|  2699.966| 48.214|   5,926|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Kinney County|     0|  0.000|  0.000|    20|  5454.050| 77.915|   3,667|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534| 75.706|   1,887|
| |Archer County|     0|  0.000|  0.000|    28|  3273.705| 133.621|   8,553|
| |Edwards County|     0|  0.000|  0.000|    28| 14492.754| 73.943|   1,932|
| |Coleman County|     0|  0.000|  0.000|    28|  3425.076| 209.699|   8,175|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Mills County|     0|  0.000|  0.000|    24|  4925.097| 234.528|   4,873|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 174.322|   3,278|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Freestone County|     0|  0.000|  0.000|   164|  8317.695| 159.398|  19,717|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Hardeman County|     0|  0.000|  0.000|    22|  5593.694| 181.613|   3,933|
| |Hartley County|     0|  0.000|  0.000|    91| 16319.943| 230.580|   5,576|
| |Haskell County|     0|  0.000|  0.000|    43|  7599.859| 100.995|   5,658|
| |Hemphill County|     0|  0.000|  0.000|    44| 11521.341| 74.814|   3,819|
| |Mason County|     0|  0.000|  0.000|    60| 14038.372| 501.370|   4,274|
| |Lipscomb County|     0|  0.000|  0.000|    21|  6495.515| 220.936|   3,233|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    68|  7610.520| 335.758|   8,935|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Jones County|     0|  0.000|  0.000|   599| 29826.221|  0.000|  20,083|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |McMullen County|     0|  0.000|  0.000|    10| 13458.950| 384.541|     743|
| |San Saba County|     0|  0.000|  0.000|    25|  4128.819| 70.780|   6,055|
| |Shackelford County|     0|  0.000|  0.000|    20|  6125.574| 131.262|   3,265|
| |Sherman County|     0|  0.000|  0.000|    43| 14228.987| 189.090|   3,022|
| |Somervell County|     0|  0.000|  0.000|    79|  8654.689| 219.106|   9,128|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Concho County|     0|  0.000|  0.000|    31| 11371.974| 262.027|   2,726|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704|  0.000|   1,350|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Collingsworth County|     0|  0.000|  0.000|    12|  4109.589| 244.618|   2,920|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 28.255|   5,056|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 50.073|   2,853|
| |Childress County|     0|  0.000|  0.000|    48|  6569.943| 234.641|   7,306|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,765| 408.097| N/A|550,198| 25617.131| N/A|21,477,737|
| |Miami-Dade County| 1,939| 713.671|  8.623|139,271| 51260.241| 700.473|2,716,940|
| |Palm Beach County|   954| 637.372|  6.872|37,934| 25343.907| 253.021|1,496,770|
| |Broward County|   859| 439.886|  5.560|64,080| 32814.790| 345.735|1,952,778|
| |Pinellas County|   522| 535.387|  8.059|18,217| 18684.179| 148.719| 974,996|
| |Hillsborough County|   426| 289.408|  4.756|33,198| 22553.479| 194.201|1,471,968|
| |Lee County|   362| 469.778|  8.343|16,872| 21895.281| 168.890| 770,577|
| |Polk County|   334| 460.831|  7.096|14,812| 20436.631| 274.567| 724,777|
| |Orange County|   325| 233.234|  7.689|32,341| 23209.267| 196.429|1,393,452|
| |Manatee County|   242| 600.120| 19.130| 9,468| 23479.057| 187.759| 403,253|
| |Duval County|   210| 219.263|  6.861|23,972| 25029.366| 262.071| 957,755|
| |St. Lucie County|   183| 557.422| 18.276| 5,968| 18178.661| 248.904| 328,297|
| |Sarasota County|   166| 382.716| 12.186| 6,394| 14741.482| 149.529| 433,742|
| |Brevard County|   160| 265.806|  6.645| 6,248| 10379.738| 127.207| 601,942|
| |Collier County|   146| 379.317|  6.310|10,530| 27357.613| 178.153| 384,902|
| |Volusia County|   146| 263.879|  6.455| 8,129| 14692.274| 195.456| 553,284|
| |Seminole County|   137| 290.361|  9.689| 7,264| 15395.506| 132.615| 471,826|
| |Escambia County|   137| 430.390| 13.464| 9,929| 31192.274| 701.010| 318,316|
| |Pasco County|   136| 245.511|  8.252| 7,213| 13021.101| 130.234| 553,947|
| |Osceola County|   107| 284.763|  4.942| 9,936| 26443.043| 296.549| 375,751|
| |Marion County|   104| 284.480| 10.942| 6,798| 18595.160| 490.416| 365,579|
| |Martin County|   100| 621.118| 14.197| 3,863| 23993.789| 154.392| 161,000|
| |Charlotte County|    96| 508.178|  5.294| 2,297| 12159.229| 145.950| 188,910|
| |Lake County|    74| 201.570|  5.837| 5,291| 14412.260| 193.398| 367,118|
| |Indian River County|    57| 356.422|  6.253| 2,574| 16095.246| 168.831| 159,923|
| |Clay County|    53| 241.731|  2.606| 3,335| 15210.808| 204.592| 219,252|
| |Hernando County|    53| 273.309| 11.050| 2,106| 10860.149| 194.484| 193,920|
| |Bay County|    52| 297.645|  5.724| 4,551| 26049.627| 460.368| 174,705|
| |Okaloosa County|    49| 232.516| 10.168| 3,608| 17120.785| 303.695| 210,738|
| |Suwannee County|    45| 1013.126| 22.514| 1,919| 43204.179| 2235.309|  44,417|
| |Sumter County|    44| 332.276|  4.315| 1,383| 10444.042| 219.000| 132,420|
| |Jackson County|    43| 926.445| 24.623| 1,953| 42077.821| 640.201|  46,414|
| |Santa Rosa County|    41| 222.448|  6.976| 4,053| 21989.767| 343.360| 184,313|
| |St. Johns County|    39| 147.352|  4.318| 3,774| 14259.159| 174.880| 264,672|
| |Citrus County|    38| 253.914|  3.818| 1,614| 10784.661| 230.050| 149,657|
| |Hendry County|    38| 904.288|  3.400| 1,814| 43167.864| 407.950|  42,022|
| |Highlands County|    37| 348.330|  9.414| 1,501| 14130.916| 255.532| 106,221|
| |Putnam County|    28| 375.733| 11.502| 1,550| 20799.506| 245.377|  74,521|
| |Leon County|    26| 88.561|  2.433| 5,150| 17541.947| 298.286| 293,582|
| |Alachua County|    26| 96.639|  0.531| 4,309| 16016.027| 237.349| 269,043|
| |Gadsden County|    21| 459.921|  0.000| 1,964| 43013.579| 1095.050|  45,660|
| |Columbia County|    20| 278.995| 13.950| 2,941| 41026.142| 536.068|  71,686|
| |DeSoto County|    18| 473.672|  7.519| 1,382| 36367.464| 259.392|  38,001|
| |Walton County|    18| 243.010|  7.715| 1,443| 19481.308| 273.869|  74,071|
| |Washington County|    14| 549.602|  0.000|   887| 34821.183| 958.999|  25,473|
| |Flagler County|    13| 112.964|  0.000| 1,101|  9567.174| 156.412| 115,081|
| |Monroe County|    13| 175.136|  0.000| 1,556| 20962.440| 292.535|  74,228|
| |Okeechobee County|    12| 284.576| 20.327| 1,081| 25635.553| 359.108|  42,168|
| |Nassau County|    11| 124.118|  0.000| 1,270| 14330.042| 185.372|  88,625|
| |Madison County|     8| 432.596|  0.000|   732| 39582.545| 533.020|  18,493|
| |Hardee County|     8| 296.989|  5.303|   992| 36826.670| 668.226|  26,937|
| |Calhoun County|     8| 567.175| 10.128|   482| 34172.279| 1498.962|  14,105|
| |Liberty County|     7| 837.922| 85.502|   407| 48719.176| 239.406|   8,354|
| |Gilchrist County|     6| 322.893| 23.064|   380| 20449.898| 384.397|  18,582|
| |Jefferson County|     5| 350.976|  0.000|   462| 32430.156| 290.808|  14,246|
| |Taylor County|     5| 231.814|  6.623| 1,000| 46362.836| 1536.597|  21,569|
| |Union County|     5| 328.149|  9.376|   448| 29402.113| 1772.002|  15,237|
| |Wakulla County|     5| 148.196|  4.234|   730| 21636.682| 402.248|  33,739|
| |Levy County|     5| 120.473|  3.442|   709| 17083.102| 265.041|  41,503|
| |Baker County|     4| 136.939|  0.000| 1,044| 35741.185| 3007.776|  29,210|
| |Dixie County|     4| 237.727|  0.000|   566| 33638.417| 2351.802|  16,826|
| |Bradford County|     4| 141.839|  0.000|   535| 18970.958| 972.610|  28,201|
| |Holmes County|     4| 203.905| 14.565|   513| 26150.788| 385.963|  19,617|
| |Hamilton County|     4| 277.239|  0.000|   625| 43318.547| 297.041|  14,428|
| |Glades County|     3| 217.218|  0.000|   408| 29541.670| 124.125|  13,811|
| |Lafayette County|     2| 237.473| 16.962|   193| 22916.172| 1356.990|   8,422|
| |Franklin County|     2| 164.948|  0.000|   433| 35711.340| 2780.560|  12,125|
| |Gulf County|     2| 146.638|  0.000|   695| 50956.815| 2712.809|  13,639|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  1.507|26,565| 16482.606| 40.419|1,611,699|
| |Essex County| 1,194| 1513.243|  1.448|17,930| 22723.989| 64.998| 789,034|
| |Suffolk County| 1,076| 1338.463|  2.310|22,017| 27387.496| 77.834| 803,907|
| |Worcester County| 1,007| 1212.344|  2.408|13,686| 16476.809| 32.506| 830,622|
| |Norfolk County|   997| 1410.633|  1.213|10,682| 15113.721| 39.212| 706,775|
| |Plymouth County|   723| 1387.178|  2.467| 9,288| 17820.346| 28.231| 521,202|
| |Hampden County|   709| 1520.246|  3.063| 7,637| 16375.340| 36.452| 466,372|
| |Bristol County|   637| 1127.001|  2.780| 9,408| 16644.935| 38.670| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,803|  8465.186| 16.768| 212,990|
| |Hampshire County|   130| 808.307|  2.665| 1,184|  7361.811| 30.200| 160,830|
| |Franklin County|    61| 869.194|  0.000|   411|  5856.369|  8.142|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  3.430| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,672| 605.438| N/A|198,498| 15664.521| N/A|12,671,821|
| |Cook County| 4,934| 958.015|  0.693|113,044| 21949.298| 128.122|5,150,233|
| |DuPage County|   522| 565.596|  1.084|12,511| 13555.873| 109.435| 922,921|
| |Lake County|   449| 644.619|  1.231|12,939| 18576.238| 127.980| 696,535|
| |Will County|   346| 500.910|  1.034| 9,486| 13733.038| 137.533| 690,743|
| |Kane County|   305| 572.874|  1.073| 9,948| 18685.094| 142.481| 532,403|
| |St. Clair County|   162| 623.830|  1.650| 4,155| 16000.092| 221.146| 259,686|
| |Winnebago County|   131| 463.599|  1.517| 3,806| 13469.134| 38.423| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,279| 10653.921| 120.218| 307,774|
| |Madison County|    78| 296.616|  2.716| 2,777| 10560.301| 248.267| 262,966|
| |Kankakee County|    69| 628.061|  1.300| 1,807| 16447.907| 128.733| 109,862|
| |Rock Island County|    38| 267.834|  5.034| 1,784| 12574.095| 135.931| 141,879|
| |Peoria County|    36| 200.916|  0.797| 1,717|  9582.596| 216.862| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,323|  6796.047| 166.581| 194,672|
| |DeKalb County|    31| 295.528|  2.724|   956|  9113.702| 98.055| 104,897|
| |LaSalle County|    25| 230.056|  5.258|   825|  7591.862| 308.933| 108,669|
| |Boone County|    23| 429.553|  0.000|   770| 14380.696| 56.029|  53,544|
| |Macon County|    23| 221.135|  0.000|   678|  6518.667| 221.135| 104,009|
| |Kendall County|    23| 178.308|  0.000| 1,412| 10946.585| 112.966| 128,990|
| |Union County|    23| 1381.133|  8.578|   330| 19816.249| 205.883|  16,653|
| |Coles County|    21| 414.848|  2.822|   520| 10272.417| 276.565|  50,621|
| |Jefferson County|    20| 530.729|  3.791|   304|  8067.084| 344.974|  37,684|
| |Jackson County|    20| 352.423|  2.517|   740| 13039.648| 161.108|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,709|  8150.165| 79.029| 209,689|
| |Clinton County|    17| 452.585|  0.000|   419| 11154.891| 201.571|  37,562|
| |Whiteside County|    17| 308.111|  2.589|   367|  6651.563| 98.388|  55,175|
| |McDonough County|    15| 505.357|  0.000|   147|  4952.496| 62.568|  29,682|
| |McLean County|    15| 87.455|  0.000|   686|  3999.604| 75.794| 171,517|
| |Monroe County|    13| 375.321|  0.000|   332|  9585.126| 164.976|  34,637|
| |Iroquois County|    12| 442.576| 15.806|   269|  9921.074| 100.106|  27,114|
| |Cass County|    11| 905.573|  0.000|   238| 19593.315| 282.257|  12,147|
| |Tazewell County|     8| 60.697|  0.000|   581|  4408.094| 154.993| 131,803|
| |Montgomery County|     7| 246.357|  0.000|   174|  6123.742| 105.582|  28,414|
| |Jasper County|     7| 728.408|  0.000|    59|  6139.438| 59.462|   9,610|
| |Randolph County|     7| 220.250|  0.000|   486| 15291.675| 206.766|  31,782|
| |Williamson County|     7| 105.110|  4.290|   454|  6817.124| 225.235|  66,597|
| |Morgan County|     6| 178.264|  0.000|   286|  8497.237| 309.839|  33,658|
| |Stephenson County|     6| 134.838|  0.000|   335|  7528.428| 35.315|  44,498|
| |Adams County|     6| 91.694|  2.183|   580|  8863.758| 259.800|  65,435|
| |Ogle County|     5| 98.730|  0.000|   420|  8293.348| 78.984|  50,643|
| |Grundy County|     5| 97.936|  0.000|   343|  6718.377| 131.513|  51,054|
| |Mercer County|     4| 259.118|  9.254|    77|  4988.016| 37.017|  15,437|
| |Christian County|     4| 123.824|  0.000|   144|  4457.652| 79.601|  32,304|
| |Carroll County|     4| 279.623|  0.000|    64|  4473.960| 179.757|  14,305|
| |Macoupin County|     3| 66.776|  0.000|   200|  4451.765| 184.430|  44,926|
| |Bond County|     3| 182.637|  8.697|    64|  3896.262| 43.485|  16,426|
| |Cumberland County|     3| 278.655| 13.269|    57|  5294.445| 132.693|  10,766|
| |Bureau County|     3| 91.946|  4.378|   241|  7386.294| 350.269|  32,628|
| |Douglas County|     3| 154.123|  7.339|   129|  6627.280| 183.480|  19,465|
| |Woodford County|     3| 78.005|  0.000|   170|  4420.292| 182.012|  38,459|
| |Perry County|     3| 143.431| 13.660|   185|  8844.903| 334.672|  20,916|
| |Livingston County|     3| 84.156|  4.007|   130|  3646.768| 124.231|  35,648|
| |Fayette County|     3| 140.607|  0.000|    71|  3327.709| 87.043|  21,336|
| |Gallatin County|     2| 414.250| 29.589|    51| 10563.380| 177.536|   4,828|
| |Wayne County|     2| 123.343|  8.810|    66|  4070.305| 105.722|  16,215|
| |Ford County|     2| 154.309| 11.022|    50|  3857.727| 55.110|  12,961|
| |Clark County|     2| 129.525|  9.252|    87|  5634.350| 129.525|  15,441|
| |Saline County|     2| 85.139|  6.081|   134|  5704.312| 103.383|  23,491|
| |Jersey County|     2| 91.857|  6.561|   122|  5603.270| 314.938|  21,773|
| |Vermilion County|     2| 26.400|  0.000|   249|  3286.782| 58.457|  75,758|
| |Pulaski County|     1| 187.441| 26.777|    97| 18181.818| 160.664|   5,335|
| |Lee County|     1| 29.329|  0.000|   186|  5455.185| 155.024|  34,096|
| |Effingham County|     1| 29.405|  0.000|   183|  5381.087| 273.045|  34,008|
| |Knox County|     1| 20.121|  0.000|   324|  6519.246| 129.350|  49,699|
| |Shelby County|     1| 46.224|  0.000|    90|  4160.118| 151.877|  21,634|
| |Logan County|     1| 34.943|  4.992|   166|  5800.545| 379.382|  28,618|
| |Jo Daviess County|     1| 47.092|  0.000|   133|  6263.245| 94.184|  21,235|
| |Hancock County|     1| 56.472|  0.000|    68|  3840.072| 233.954|  17,708|
| |Franklin County|     1| 25.995|  3.714|   198|  5147.001| 211.673|  38,469|
| |Henry County|     1| 20.444|  0.000|   262|  5356.449| 134.349|  48,913|
| |Putnam County|     0|  0.000|  0.000|    14|  2439.449| 124.462|   5,739|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 102.603|   4,177|
| |Pike County|     0|  0.000|  0.000|    26|  1670.844| 82.624|  15,561|
| |Piatt County|     0|  0.000|  0.000|    64|  3915.810| 104.888|  16,344|
| |Moultrie County|     0|  0.000|  0.000|    93|  6413.351| 265.992|  14,501|
| |White County|     0|  0.000|  0.000|    72|  5318.756| 116.084|  13,537|
| |Washington County|     0|  0.000|  0.000|    67|  4824.656| 72.010|  13,887|
| |Warren County|     0|  0.000|  0.000|   194| 11517.454| 76.331|  16,844|
| |Wabash County|     0|  0.000|  0.000|    42|  3645.833| 111.607|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    27|  5453.444| 432.813|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    19|  2807.329| 42.215|   6,768|
| |Richland County|     0|  0.000|  0.000|    22|  1418.165| 73.671|  15,513|
| |Fulton County|     0|  0.000|  0.000|    37|  1077.461| 20.800|  34,340|
| |Edwards County|     0|  0.000|  0.000|    24|  3752.932| 178.711|   6,395|
| |Edgar County|     0|  0.000|  0.000|    29|  1689.878| 16.649|  17,161|
| |De Witt County|     0|  0.000|  0.000|    34|  2174.191| 18.271|  15,638|
| |Crawford County|     0|  0.000|  0.000|    29|  1553.544|  0.000|  18,667|
| |Hamilton County|     0|  0.000|  0.000|    30|  3696.402| 88.010|   8,116|
| |Greene County|     0|  0.000|  0.000|    66|  5089.059| 418.581|  12,969|
| |Clay County|     0|  0.000|  0.000|    27|  2047.937| 108.356|  13,184|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 37.387|   3,821|
| |Brown County|     0|  0.000|  0.000|    15|  2280.328| 43.435|   6,578|
| |Calhoun County|     0|  0.000|  0.000|    11|  2321.165| 90.435|   4,739|
| |Henderson County|     0|  0.000|  0.000|    14|  2106.530| 85.981|   6,646|
| |Menard County|     0|  0.000|  0.000|    58|  4755.658| 93.708|  12,196|
| |Massac County|     0|  0.000|  0.000|    42|  3049.666| 72.611|  13,772|
| |Mason County|     0|  0.000|  0.000|    57|  4266.786| 139.018|  13,359|
| |Marshall County|     0|  0.000|  0.000|    28|  2447.980| 87.428|  11,438|
| |Marion County|     0|  0.000|  0.000|   169|  4542.400| 99.833|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    51|  3252.966| 63.784|  15,678|
| |Johnson County|     0|  0.000|  0.000|    70|  5637.433| 92.040|  12,417|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,380| 576.473| N/A|125,918|  9835.815| N/A|12,801,989|
| |Philadelphia County| 1,709| 1078.871| N/A|31,725| 20027.600| N/A|1,584,064|
| |Montgomery County|   859| 1033.800|  1.032|10,219| 12298.490| 45.905| 830,915|
| |Delaware County|   706| 1245.706|  3.277| 9,436| 16649.404| 101.834| 566,747|
| |Bucks County|   582| 926.353|  0.455| 7,275| 11579.416| 43.203| 628,270|
| |Lancaster County|   417| 764.123|  2.356| 6,028| 11045.877| 79.318| 545,724|
| |Berks County|   372| 883.266|  1.696| 5,470| 12987.815| 68.857| 421,164|
| |Chester County|   350| 666.681|  0.272| 5,234|  9969.733| 52.790| 524,989|
| |Lehigh County|   338| 915.200|  1.160| 5,022| 13598.037| 52.220| 369,318|
| |Northampton County|   293| 959.759|  0.936| 3,956| 12958.383| 30.417| 305,285|
| |Allegheny County|   259| 212.986|  2.350| 9,078|  7465.184| 66.492|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,946|  9281.074| 23.165| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,526| 11108.416| 67.059| 317,417|
| |Dauphin County|   159| 571.328|  1.540| 2,873| 10323.429| 76.998| 278,299|
| |Monroe County|   124| 728.251|  0.000| 1,650|  9690.435| 32.721| 170,271|
| |York County|    97| 216.008|  2.545| 2,680|  5968.049| 89.075| 449,058|
| |Beaver County|    93| 567.319|  3.486| 1,351|  8241.373| 71.460| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,327|  5237.400| 38.340| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,626| 11467.421| 42.315| 141,793|
| |Schuylkill County|    51| 360.784|  2.021|   928|  6564.846| 23.244| 141,359|
| |Westmoreland County|    47| 134.709|  0.409| 1,573|  4508.468| 40.126| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,385|  8933.928| 73.720| 155,027|
| |Columbia County|    35| 538.760|  0.000|   481|  7404.101| 28.587|  64,964|
| |Carbon County|    28| 436.259|  0.000|   377|  5873.921| 28.936|  64,182|
| |Susquehanna County|    27| 669.510|  0.000|   217|  5380.877| 17.712|  40,328|
| |Erie County|    22| 81.564|  2.648| 1,143|  4237.602| 56.141| 269,728|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  0.000|  55,809|
| |Adams County|    20| 194.158|  0.000|   535|  5193.721| 72.116| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   411|  3627.570| 75.653| 113,299|
| |Butler County|    16| 85.173|  0.760|   695|  3699.701| 53.994| 187,853|
| |Lawrence County|    16| 187.108|  6.682|   401|  4689.400| 70.166|  85,512|
| |Northumberland County|    15| 165.120|  6.290|   513|  5647.105| 144.677|  90,843|
| |Washington County|    13| 62.843|  1.381|   871|  4210.475| 59.390| 206,865|
| |Mercer County|    11| 100.526|  2.611|   456|  4167.276| 104.443| 109,424|
| |Centre County|    10| 61.582|  0.000|   377|  2321.643| 14.076| 162,385|
| |Wayne County|    10| 194.700|  5.563|   162|  3154.144| 13.907|  51,361|
| |Armstrong County|     8| 123.581|  4.414|   230|  3552.947| 75.031|  64,735|
| |Wyoming County|     8| 298.574|  0.000|    61|  2276.629| 15.995|  26,794|
| |Indiana County|     7| 83.261|  1.699|   335|  3984.632| 88.359|  84,073|
| |Blair County|     7| 57.458|  4.690|   302|  2478.884| 71.529| 121,829|
| |Fayette County|     6| 46.413|  2.210|   582|  4502.065| 166.866| 129,274|
| |Juniata County|     6| 242.297|  0.000|   135|  5451.682| 40.383|  24,763|
| |Perry County|     5| 108.057|  0.000|   125|  2701.418| 15.437|  46,272|
| |Clinton County|     5| 129.426|  0.000|   124|  3209.774| 22.187|  38,632|
| |Bedford County|     4| 83.528|  0.000|   145|  3027.898| 32.815|  47,888|
| |Huntingdon County|     4| 88.605|  0.000|   309|  6844.763| 44.303|  45,144|
| |Tioga County|     3| 73.908|  0.000|    39|   960.804| 10.558|  40,591|
| |Cambria County|     3| 23.043|  0.000|   351|  2696.018| 42.794| 130,192|
| |Montour County|     3| 164.564|  0.000|   104|  5704.882| 54.855|  18,230|
| |Bradford County|     3| 49.732|  0.000|    90|  1491.968| 11.841|  60,323|
| |Somerset County|     3| 40.846|  0.000|   138|  1878.906| 21.395|  73,447|
| |Fulton County|     2| 137.646|  0.000|    27|  1858.224| 19.664|  14,530|
| |Elk County|     2| 66.867|  0.000|    54|  1805.416| 38.210|  29,910|
| |Clarion County|     2| 52.032|  0.000|    83|  2159.322| 22.299|  38,438|
| |Union County|     2| 44.521|  0.000|   276|  6143.846| 238.503|  44,923|
| |Snyder County|     2| 49.539|  0.000|   112|  2774.200| 42.462|  40,372|
| |Warren County|     1| 25.516|  0.000|    23|   586.869| 10.935|  39,191|
| |Greene County|     1| 27.599|  0.000|   118|  3256.700| 31.542|  36,233|
| |Jefferson County|     1| 23.028|  0.000|    74|  1704.088| 42.767|  43,425|
| |Mifflin County|     1| 21.674|  0.000|   121|  2622.567| 24.770|  46,138|
| |Crawford County|     1| 11.816|  0.000|   162|  1914.237| 43.889|  84,629|
| |Clearfield County|     1| 12.618|  1.803|   177|  2233.298| 59.483|  79,255|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  3.516|  40,625|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Venango County|     0|  0.000|  0.000|    67|  1322.334| 14.097|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Forest County|     0|  0.000|  0.000|    10|  1379.881| 19.713|   7,247|
| |Cameron County|     0|  0.000|  0.000|     7|  1574.095| 32.124|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,463| 647.151| N/A|93,786|  9390.943| N/A|9,986,857|
| |Wayne County| 2,828| 1616.607|  1.552|28,391| 16229.522| 57.409|1,749,343|
| |Oakland County| 1,133| 900.934|  0.682|15,876| 12624.206| 96.103|1,257,584|
| |Macomb County|   949| 1085.847|  1.961|10,794| 12350.510| 140.900| 873,972|
| |Genesee County|   296| 729.400|  0.352| 3,683|  9075.609| 35.907| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,629| 11612.668| 63.714| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,071| 10869.166| 122.210| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,613|  7108.251| 55.184| 367,601|
| |Kalamazoo County|    83| 313.130|  0.539| 1,686|  6360.680| 52.817| 265,066|
| |Berrien County|    67| 436.764|  0.931| 1,387|  9041.662| 67.051| 153,401|
| |Muskegon County|    59| 339.928|  0.823| 1,195|  6884.989| 42.800| 173,566|
| |Ottawa County|    57| 195.319|  0.979| 1,856|  6359.867| 45.526| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   829|  5209.643| 35.012| 159,128|
| |Calhoun County|    42| 313.061|  1.065|   811|  6045.066| 45.788| 134,159|
| |Jackson County|    34| 214.498|  0.901|   722|  4554.918| 18.926| 158,510|
| |Lapeer County|    33| 376.682|  0.000|   472|  5387.697| 32.613|  87,607|
| |Ingham County|    32| 109.437|  0.977| 1,570|  5369.247| 32.733| 292,406|
| |Bay County|    32| 310.300|  1.385|   654|  6341.757| 120.518| 103,126|
| |Tuscola County|    29| 555.077|  0.000|   362|  6928.893| 103.906|  52,245|
| |Livingston County|    28| 145.837|  0.000|   850|  4427.199| 33.483| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   348|  5108.482| 27.262|  68,122|
| |Hillsdale County|    25| 548.186|  0.000|   278|  6095.823| 78.312|  45,605|
| |Monroe County|    25| 166.113|  2.848| 1,016|  6750.831| 76.887| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   157|  3856.452| 38.600|  40,711|
| |Cass County|    14| 270.338|  5.517|   340|  6565.354| 104.825|  51,787|
| |Clinton County|    13| 163.327|  0.000|   426|  5352.095| 12.564|  79,595|
| |Alpena County|    13| 457.666|  0.000|   130|  4576.659| 15.088|  28,405|
| |Iosco County|    12| 477.574|  0.000|   134|  5332.909| 28.427|  25,127|
| |Lenawee County|    12| 121.888|  0.000|   440|  4469.228| 44.982|  98,451|
| |Otsego County|    11| 445.922|  5.791|   135|  5472.677| 23.165|  24,668|
| |Marquette County|    11| 164.920|  0.000|   172|  2578.749| 55.687|  66,699|
| |Van Buren County|    10| 132.141|  0.000|   461|  6091.679| 67.958|  75,677|
| |Midland County|    10| 120.256|  0.000|   344|  4136.803| 49.820|  83,156|
| |Isabella County|     9| 128.807|  0.000|   210|  3005.496| 12.267|  69,872|
| |St. Joseph County|     9| 147.628|  2.343|   603|  9891.083| 79.672|  60,964|
| |Eaton County|     8| 72.551|  0.000|   461|  4180.723| 15.547| 110,268|
| |Ionia County|     7| 108.197|  4.416|   274|  4235.127|  4.416|  64,697|
| |Allegan County|     6| 50.813|  0.000|   542|  4590.070| 45.973| 118,081|
| |Sanilac County|     6| 145.737|  0.000|   109|  2647.559| 27.759|  41,170|
| |Oceana County|     6| 226.697|  0.000|   479| 18098.009| 64.771|  26,467|
| |Grand Traverse County|     5| 53.713|  0.000|   220|  2363.355| 32.228|  93,088|
| |Crawford County|     5| 356.405|  0.000|   107|  7627.058| 40.732|  14,029|
| |Huron County|     4| 129.111|  0.000|   161|  5196.733| 55.333|  30,981|
| |Wexford County|     4| 118.938|  0.000|    70|  2081.413|  8.496|  33,631|
| |Kalkaska County|     4| 221.754|  0.000|    54|  2993.680| 39.599|  18,038|
| |Ogemaw County|     3| 142.878|  6.804|    54|  2571.796|  6.804|  20,997|
| |Clare County|     3| 96.931|  0.000|    74|  2390.953| 46.157|  30,950|
| |Delta County|     3| 83.836|  0.000|   104|  2906.327| 75.852|  35,784|
| |Arenac County|     3| 201.572|  0.000|    43|  2889.202| 19.197|  14,883|
| |Roscommon County|     2| 83.267| 11.895|    55|  2289.854| 23.791|  24,019|
| |Emmet County|     2| 59.853|  0.000|    65|  1945.234| 21.376|  33,415|
| |Dickinson County|     2| 79.242|  0.000|    58|  2298.031| 56.602|  25,239|
| |Gladwin County|     2| 78.589|  0.000|    59|  2318.362| 16.840|  25,449|
| |Mecosta County|     2| 46.027|  0.000|    69|  1587.923| 23.013|  43,453|
| |Cheboygan County|     2| 79.126|  0.000|    50|  1978.161| 50.867|  25,276|
| |Barry County|     2| 32.494|  0.000|   191|  3103.168| 48.741|  61,550|
| |Branch County|     2| 45.959|  0.000|   367|  8433.486| 62.373|  43,517|
| |Charlevoix County|     2| 76.502|  0.000|    50|  1912.558| 27.322|  26,143|
| |Montcalm County|     1| 15.652|  0.000|   193|  3020.912| 26.833|  63,888|
| |Iron County|     1| 90.367|  0.000|    20|  1807.338| 38.729|  11,066|
| |Gogebic County|     1| 71.556|  0.000|   125|  8944.544| 204.447|  13,975|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  0.000|  15,118|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Benzie County|     1| 56.287|  0.000|    30|  1688.619|  8.041|  17,766|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Presque Isle County|     1| 79.416|  0.000|    20|  1588.310|  0.000|  12,592|
| |Alger County|     0|  0.000|  0.000|    15|  1646.904| 109.794|   9,108|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Houghton County|     0|  0.000|  0.000|    50|  1401.188|  4.003|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    43|  1151.303| 26.774|  37,349|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846|  6.125|  23,324|
| |Leelanau County|     0|  0.000|  0.000|    73|  3354.625| 39.389|  21,761|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128|  0.000|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Ontonagon County|     0|  0.000|  0.000|    18|  3146.853| 274.725|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   254|  5185.790| 14.583|  48,980|
| |Montmorency County|     0|  0.000|  0.000|     8|   857.633|  0.000|   9,328|
| |Menominee County|     0|  0.000|  0.000|   150|  6584.723| 244.575|  22,780|
| |Mason County|     0|  0.000|  0.000|   103|  3534.175| 19.607|  29,144|
| |Manistee County|     0|  0.000|  0.000|    40|  1628.797| 34.903|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    26|  2407.630| 13.229|  10,799|
| |Luce County|     0|  0.000|  0.000|     4|   642.158| 22.934|   6,229|
| |Lake County|     0|  0.000|  0.000|    26|  2193.538| 84.367|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,450| 1248.146| N/A|50,470| 14155.943| N/A|3,565,287|
| |Hartford County| 1,416| 1587.942|  0.641|12,830| 14387.924| 15.540| 891,720|
| |Fairfield County| 1,410| 1494.702|  0.303|18,088| 19174.585| 26.653| 943,332|
| |New Haven County| 1,109| 1297.445|  0.836|13,254| 15506.161| 22.730| 854,757|
| |Middlesex County|   192| 1182.004|  0.879| 1,408|  8668.029| 10.554| 162,436|
| |Litchfield County|   139| 770.796|  0.792| 1,617|  8966.745|  8.714| 180,333|
| |New London County|   104| 392.148|  0.539| 1,469|  5539.090| 22.085| 265,206|
| |Tolland County|    65| 431.260|  0.000| 1,056|  7006.323|  0.000| 150,721|
| |Windham County|    15| 128.444|  0.000|   748|  6405.097| 31.805| 116,782|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,352| 409.892| N/A|206,953| 19491.830| N/A|10,617,423|
| |Fulton County|   455| 427.657|  6.445|21,140| 19869.598| 287.880|1,063,937|
| |Cobb County|   326| 428.868|  3.007|14,279| 18784.673| 336.404| 760,141|
| |Gwinnett County|   275| 293.725|  5.188|20,685| 22093.458| 325.768| 936,250|
| |DeKalb County|   247| 325.301|  3.010|14,485| 19076.857| 279.770| 759,297|
| |Dougherty County|   172| 1955.523|  4.873| 2,774| 31538.497| 198.151|  87,956|
| |Clayton County|   114| 390.069|  5.866| 5,245| 17946.595| 258.580| 292,256|
| |Hall County|   104| 508.704| 12.578| 6,298| 30805.954| 376.637| 204,441|
| |Muscogee County|   104| 531.238| 10.946| 4,879| 24922.230| 309.403| 195,769|
| |Richmond County|    95| 469.094|  5.643| 4,672| 23069.554| 529.759| 202,518|
| |Chatham County|    87| 300.591|  6.910| 5,990| 20695.850| 310.956| 289,430|
| |Bibb County|    73| 476.629|  7.462| 3,795| 24778.172| 412.270| 153,159|
| |Troup County|    71| 1015.417| 10.215| 2,335| 33394.354| 249.257|  69,922|
| |Cherokee County|    65| 251.185|  4.416| 3,707| 14325.297| 343.379| 258,773|
| |Bartow County|    64| 594.034|  3.978| 1,953| 18127.309| 289.061| 107,738|
| |Houston County|    62| 392.746| 10.859| 2,048| 12973.274| 181.894| 157,863|
| |Sumter County|    56| 1896.762|  0.000|   784| 26554.667| 208.063|  29,524|
| |Henry County|    54| 230.217|  6.090| 3,513| 14976.914| 228.390| 234,561|
| |Douglas County|    54| 368.996|  3.905| 2,773| 18948.634| 301.640| 146,343|
| |Glynn County|    53| 621.395| 18.424| 2,625| 30776.626| 390.256|  85,292|
| |Carroll County|    52| 433.362|  5.953| 1,910| 15917.728| 155.963| 119,992|
| |Habersham County|    50| 1103.071|  6.303| 1,173| 25878.044| 264.737|  45,328|
| |Lowndes County|    48| 408.838| 17.035| 3,273| 27877.621| 293.244| 117,406|
| |Upson County|    46| 1747.720|  0.000|   574| 21808.511| 434.216|  26,320|
| |Newton County|    45| 402.706| 10.227| 1,895| 16958.405| 264.635| 111,744|
| |Thomas County|    44| 989.854| 12.855| 1,147| 25803.694| 359.947|  44,451|
| |Baldwin County|    42| 935.620| 12.730| 1,095| 24392.961| 340.515|  44,890|
| |Spalding County|    41| 614.665|  2.142|   983| 14736.968| 212.027|  66,703|
| |Tift County|    41| 1008.759| 21.089| 1,373| 33781.124| 302.276|  40,644|
| |Mitchell County|    41| 1875.314|  0.000|   658| 30096.510| 163.355|  21,863|
| |Walton County|    39| 412.293|  3.020| 1,188| 12559.069| 253.719|  94,593|
| |Butts County|    38| 1523.901|  5.729|   495| 19850.818| 148.953|  24,936|
| |Hancock County|    35| 4138.583| 16.892|   328| 38784.439| 574.334|   8,457|
| |Barrow County|    34| 408.457|  3.432| 1,355| 16278.232| 300.336|  83,240|
| |Early County|    32| 3140.334| 14.019|   372| 36506.379| 280.387|  10,190|
| |Whitfield County|    32| 305.845|  5.462| 3,621| 34608.327| 420.538| 104,628|
| |Fayette County|    31| 270.929|  7.491| 1,187| 10373.970| 198.515| 114,421|
| |Terrell County|    30| 3516.587|  0.000|   306| 35869.183| 167.457|   8,531|
| |Coffee County|    30| 693.273| 16.506| 1,529| 35333.811| 445.675|  43,273|
| |Ware County|    29| 811.552| 19.989| 1,178| 32965.803| 323.821|  35,734|
| |Monroe County|    28| 1015.302| 15.540|   473| 17151.353| 170.944|  27,578|
| |Columbia County|    27| 172.288|  5.469| 2,443| 15588.907| 358.250| 156,714|
| |Forsyth County|    26| 106.447|  2.340| 2,416|  9891.424| 222.838| 244,252|
| |Randolph County|    26| 3835.940|  0.000|   274| 40424.904| 168.613|   6,778|
| |Colquitt County|    24| 526.316|  6.266| 1,581| 34671.053| 194.236|  45,600|
| |Jenkins County|    24| 2766.252|  0.000|   251| 28930.383| 263.453|   8,676|
| |Gordon County|    23| 396.805|  0.000| 1,264| 21807.015| 446.097|  57,963|
| |Rockdale County|    23| 253.036| 11.002| 1,395| 15347.210| 273.468|  90,896|
| |Worth County|    23| 1135.971|  0.000|   457| 22571.245| 148.170|  20,247|
| |Lee County|    23| 766.871|  4.763|   565| 18838.357| 185.764|  29,992|
| |Paulding County|    23| 136.363|  1.694| 1,789| 10606.698| 212.591| 168,667|
| |Coweta County|    22| 148.139|  0.000| 1,568| 10558.283| 157.759| 148,509|
| |Wilcox County|    19| 2200.347| 16.544|   188| 21771.859| 248.159|   8,635|
| |Appling County|    19| 1033.395|  0.000|   721| 39214.620| 823.608|  18,386|
| |Clarke County|    19| 148.055|  2.226| 2,150| 16753.551| 319.486| 128,331|
| |Putnam County|    18| 813.780|  6.459|   449| 20299.290| 361.680|  22,119|
| |Floyd County|    18| 182.745|  2.901| 1,648| 16731.304| 427.855|  98,498|
| |Turner County|    18| 2254.227|  0.000|   257| 32185.348| 357.814|   7,985|
| |Brooks County|    17| 1099.825|  0.000|   419| 27107.459| 295.751|  15,457|
| |Harris County|    17| 482.461|  4.054|   668| 18957.884| 162.172|  35,236|
| |Laurens County|    17| 357.548| 33.051| 1,064| 22378.328| 838.286|  47,546|
| |Jackson County|    17| 232.950|  7.830| 1,118| 15319.895| 230.993|  72,977|
| |Walker County|    17| 243.689|  2.048|   742| 10636.315| 255.976|  69,761|
| |Decatur County|    16| 605.969| 32.463|   834| 31586.123| 665.484|  26,404|
| |Bulloch County|    16| 200.985|  3.589| 1,334| 16757.110| 353.518|  79,608|
| |Oconee County|    15| 372.393|  0.000|   455| 11295.929| 148.957|  40,280|
| |Peach County|    15| 544.544| 15.558|   402| 14593.770| 264.493|  27,546|
| |Crisp County|    15| 670.481|  6.386|   398| 17790.095| 204.337|  22,372|
| |Dooly County|    14| 1045.556|  0.000|   261| 19492.158| 181.372|  13,390|
| |Stephens County|    13| 501.446| 11.021|   663| 25573.770| 462.874|  25,925|
| |Greene County|    12| 654.879|  7.796|   331| 18063.742| 374.216|  18,324|
| |Lamar County|    12| 629.030| 14.977|   280| 14677.360| 209.677|  19,077|
| |Telfair County|    12| 756.620| 45.037|   302| 19041.614| 351.288|  15,860|
| |Johnson County|    12| 1244.426| 14.815|   252| 26132.946| 296.292|   9,643|
| |Emanuel County|    11| 485.737| 18.925|   537| 23712.797| 548.820|  22,646|
| |Polk County|    11| 258.137|  0.000|   877| 20580.574| 546.446|  42,613|
| |Wayne County|    11| 367.561| 19.094|   825| 27567.080| 615.784|  29,927|
| |Wilkinson County|    11| 1228.501| 15.955|   221| 24681.706| 351.000|   8,954|
| |Macon County|    10| 772.380|  0.000|   181| 13980.073| 66.204|  12,947|
| |McDuffie County|    10| 469.219|  0.000|   386| 18111.862| 536.251|  21,312|
| |Catoosa County|    10| 147.973|  2.114|   677| 10017.757| 190.251|  67,580|
| |Bleckley County|    10| 776.820| 55.487|   261| 20274.994| 1098.645|  12,873|
| |Screven County|     9| 644.422|  0.000|   216| 15466.132| 347.783|  13,966|
| |Pierce County|     9| 462.368| 22.018|   420| 21577.190| 249.532|  19,465|
| |Jefferson County|     9| 585.861| 18.599|   532| 34630.907| 669.556|  15,362|
| |Toombs County|     9| 335.445| 10.649|   789| 29407.380| 596.347|  26,830|
| |Jeff Davis County|     8| 529.276|  9.451|   485| 32087.330| 661.594|  15,115|
| |Bacon County|     8| 716.589| 25.592|   448| 40128.986| 358.295|  11,164|
| |Bryan County|     8| 201.883|  0.000|   695| 17538.547| 338.874|  39,627|
| |Burke County|     7| 312.737|  0.000|   504| 22517.089| 491.444|  22,383|
| |Grady County|     7| 284.172| 11.599|   522| 21191.085| 481.352|  24,633|
| |Lumpkin County|     7| 208.271|  4.250|   371| 11038.381| 233.774|  33,610|
| |Union County|     7| 285.586|  5.828|   298| 12157.807| 349.697|  24,511|
| |Oglethorpe County|     7| 458.746|  0.000|   236| 15466.282| 355.762|  15,259|
| |Stewart County|     7| 1057.242| 43.153|   256| 38664.854| 64.729|   6,621|
| |Madison County|     7| 234.270|  9.562|   424| 14190.094| 267.738|  29,880|
| |Hart County|     7| 267.125| 16.355|   325| 12402.213| 261.673|  26,205|
| |Haralson County|     7| 234.962|  4.795|   231|  7753.759| 143.855|  29,792|
| |White County|     6| 194.818|  4.639|   370| 12013.767| 259.757|  30,798|
| |Candler County|     6| 555.401| 26.448|   271| 25085.624| 502.506|  10,803|
| |Calhoun County|     6| 969.462|  0.000|   210| 33931.168| 253.907|   6,189|
| |Cook County|     6| 347.423|  0.000|   454| 26288.361| 314.335|  17,270|
| |Meriwether County|     6| 283.460|  0.000|   409| 19322.530| 283.460|  21,167|
| |Franklin County|     6| 256.970|  6.118|   423| 18116.408| 232.497|  23,349|
| |Liberty County|     6| 97.664|  6.976|   780| 12696.346| 281.366|  61,435|
| |Brantley County|     6| 313.988| 14.952|   257| 13449.160| 149.518|  19,109|
| |Marion County|     5| 598.158| 17.090|   156| 18662.519| 187.992|   8,359|
| |Effingham County|     5| 77.765|  8.887|   770| 11975.862| 217.743|  64,296|
| |Camden County|     5| 91.465|  2.613|   804| 14707.496| 250.874|  54,666|
| |Dawson County|     5| 191.512| 10.944|   431| 16508.350| 558.121|  26,108|
| |Banks County|     5| 259.956| 14.855|   280| 14557.554| 245.102|  19,234|
| |Heard County|     5| 419.358| 11.982|   148| 12412.983| 143.780|  11,923|
| |Pickens County|     5| 153.417|  0.000|   420| 12886.993| 372.583|  32,591|
| |Ben Hill County|     5| 299.401| 17.109|   478| 28622.754| 915.312|  16,700|
| |Pike County|     5| 263.685|  7.534|   228| 12024.048| 226.016|  18,962|
| |Lincoln County|     4| 504.987|  0.000|   153| 19315.743| 414.811|   7,921|
| |Fannin County|     4| 152.742|  5.455|   354| 13517.642| 294.573|  26,188|
| |Twiggs County|     4| 492.611| 17.593|   124| 15270.936| 387.051|   8,120|
| |Clinch County|     4| 604.412|  0.000|   204| 30825.023| 518.068|   6,618|
| |Seminole County|     4| 494.438|  0.000|   220| 27194.067| 882.924|   8,090|
| |Chattooga County|     4| 161.362| 11.526|   302| 12182.823| 518.663|  24,789|
| |Lanier County|     4| 383.767|  0.000|   225| 21586.875| 205.589|  10,423|
| |Jones County|     4| 139.203|  4.972|   326| 11345.050| 218.748|  28,735|
| |Gilmer County|     4| 127.514|  0.000|   651| 20752.973| 446.300|  31,369|
| |Evans County|     3| 281.584| 26.818|   282| 26468.932| 616.804|  10,654|
| |McIntosh County|     3| 208.652|  9.936|   194| 13492.836| 298.074|  14,378|
| |Wilkes County|     3| 306.843|  0.000|   195| 19944.768| 189.950|   9,777|
| |Pulaski County|     3| 269.372| 12.827|   133| 11942.175| 551.572|  11,137|
| |Dodge County|     3| 145.596|  0.000|   243| 11793.254| 298.125|  20,605|
| |Talbot County|     3| 484.262|  0.000|   142| 22921.711| 299.781|   6,195|
| |Rabun County|     3| 175.060|  0.000|   230| 13421.252| 250.085|  17,137|
| |Baker County|     3| 987.492|  0.000|    67| 22053.983| 235.117|   3,038|
| |Atkinson County|     3| 367.422| 17.496|   330| 40416.412| 507.392|   8,165|
| |Charlton County|     3| 224.014|  0.000|   439| 32780.765| 405.359|  13,392|
| |Treutlen County|     3| 434.720|  0.000|   132| 19127.663| 579.626|   6,901|
| |Chattahoochee County|     2| 183.368| 13.098|   766| 70230.127| 916.842|  10,907|
| |Echols County|     2| 499.251|  0.000|   225| 56165.751| 320.947|   4,006|
| |Dade County|     2| 124.100|  8.864|   136|  8438.819| 150.693|  16,116|
| |Clay County|     2| 705.716|  0.000|    93| 32815.808| 403.266|   2,834|
| |Jasper County|     2| 140.657| 10.047|   170| 11955.834| 351.642|  14,219|
| |Murray County|     2| 49.880|  0.000|   623| 15537.709| 238.713|  40,096|
| |Montgomery County|     2| 218.055| 15.575|   157| 17117.314| 218.055|   9,172|
| |Taylor County|     2| 249.377|  0.000|    94| 11720.698| 285.002|   8,020|
| |Tattnall County|     2| 79.095|  5.650|   546| 21592.976| 497.170|  25,286|
| |Washington County|     2| 98.164|  0.000|   497| 24393.835| 336.563|  20,374|
| |Webster County|     2| 767.165|  0.000|    40| 15343.306| 54.798|   2,607|
| |Long County|     1| 51.127|  0.000|   132|  6748.811| 131.470|  19,559|
| |Schley County|     1| 190.223|  0.000|    74| 14076.469| 489.144|   5,257|
| |Towns County|     1| 83.077|  0.000|   154| 12793.886| 403.518|  12,037|
| |Warren County|     1| 190.331|  0.000|    87| 16558.812| 734.135|   5,254|
| |Quitman County|     1| 434.972|  0.000|    31| 13484.124| 124.278|   2,299|
| |Wheeler County|     1| 127.307|  0.000|    97| 12348.822| 218.241|   7,855|
| |Elbert County|     1| 52.100|  0.000|   369| 19224.758| 260.498|  19,194|
| |Glascock County|     1| 336.587| 48.084|    24|  8078.088|  0.000|   2,971|
| |Irwin County|     1| 106.202|  0.000|   172| 18266.780| 227.576|   9,416|
| |Berrien County|     1| 51.554|  7.365|   318| 16394.288| 412.435|  19,397|
| |Taliaferro County|     0|  0.000|  0.000|    13|  8458.035| 92.945|   1,537|
| |Morgan County|     0|  0.000|  0.000|   295| 15304.005| 437.257|  19,276|
| |Miller County|     0|  0.000|  0.000|   149| 26058.062| 424.724|   5,718|
| |Crawford County|     0|  0.000|  0.000|   107|  8626.250| 103.653|  12,404|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,346| 597.083| N/A|189,442| 26026.840| N/A|7,278,717|
| |Maricopa County| 2,493| 555.802|  9.204|127,188| 28355.911| 130.773|4,485,414|
| |Pima County|   505| 482.202|  4.911|18,508| 17672.464| 210.614|1,047,279|
| |Yuma County|   290| 1356.490|  9.355|11,641| 54451.393| 218.509| 213,787|
| |Navajo County|   204| 1839.097|  9.015| 5,408| 48754.102| 127.500| 110,924|
| |Mohave County|   178| 838.906| 11.446| 3,250| 15317.111| 119.170| 212,181|
| |Pinal County|   164| 354.373|  5.865| 8,555| 18485.746| 79.641| 462,789|
| |Apache County|   139| 1933.590|  3.974| 3,212| 44681.236| 184.814|  71,887|
| |Coconino County|   119| 829.407|  1.991| 3,130| 21815.495| 96.582| 143,476|
| |Yavapai County|    71| 302.000|  3.646| 2,065|  8783.534| 97.831| 235,099|
| |Cochise County|    56| 444.720|  4.538| 1,732| 13754.546| 195.132| 125,922|
| |Santa Cruz County|    54| 1161.340|  9.217| 2,675| 57529.356| 129.038|  46,498|
| |Gila County|    41| 759.006| 18.512|   976| 18068.051| 277.685|  54,018|
| |Graham County|    19| 489.224| 25.749|   559| 14393.491| 176.562|  38,837|
| |La Paz County|    12| 568.505| 13.536|   486| 23024.446| 67.679|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,238| 911.634| N/A|134,068| 28839.308| N/A|4,648,794|
| |Orleans Parish|   564| 1445.620|  1.465|10,851| 27812.808| 119.004| 390,144|
| |Jefferson Parish|   529| 1223.141|  2.973|15,509| 35859.540| 196.535| 432,493|
| |East Baton Rouge Parish|   360| 818.072|  9.090|12,477| 28353.016| 287.948| 440,059|
| |Caddo Parish|   296| 1232.286|  5.947| 6,771| 28188.540| 151.657| 240,204|
| |St. Tammany Parish|   216| 829.433|  4.389| 5,364| 20597.575| 233.141| 260,419|
| |Calcasieu Parish|   147| 722.586| 14.044| 6,924| 34035.274| 198.729| 203,436|
| |Rapides Parish|   119| 917.870|  8.815| 3,380| 26070.591| 247.924| 129,648|
| |Ouachita Parish|   114| 743.742|  6.524| 4,967| 32404.961| 301.038| 153,279|
| |Lafourche Parish|   100| 1024.443|  5.854| 2,895| 29657.631| 308.796|  97,614|
| |Lafayette Parish|   100| 409.182|  6.430| 7,793| 31887.557| 262.461| 244,390|
| |St. John the Baptist Parish|    92| 2147.676| 10.005| 1,441| 33639.144| 183.420|  42,837|
| |St. Landry Parish|    92| 1120.257| 19.135| 2,824| 34387.024| 466.194|  82,124|
| |Acadia Parish|    87| 1402.208| 23.025| 2,652| 42743.170| 267.087|  62,045|
| |Terrebonne Parish|    86| 778.555|  7.760| 3,095| 28018.939| 253.483| 110,461|
| |Bossier Parish|    82| 645.471|  7.872| 2,390| 18813.120| 129.319| 127,039|
| |Tangipahoa Parish|    78| 578.815|  9.541| 3,570| 26491.934| 295.768| 134,758|
| |Ascension Parish|    78| 616.094|  7.899| 2,941| 23229.914| 243.730| 126,604|
| |Iberia Parish|    73| 1045.396|  8.183| 2,575| 36875.269| 333.463|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,298| 28098.887| 241.219|  46,194|
| |St. Mary Parish|    56| 1134.798| 14.474| 1,642| 33273.892| 379.231|  49,348|
| |St. Charles Parish|    55| 1035.782| 13.452| 1,500| 28248.588| 217.918|  53,100|
| |Livingston Parish|    52| 369.347|  3.044| 2,992| 21251.660| 241.496| 140,789|
| |Iberville Parish|    50| 1537.941| 13.182| 1,262| 38817.631| 342.741|  32,511|
| |St. Martin Parish|    46| 860.923|  8.021| 1,757| 32883.532| 446.504|  53,431|
| |East Feliciana Parish|    39| 2038.150| 29.863|   609| 31826.496| 500.205|  19,135|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   734| 27734.744| 302.286|  26,465|
| |Union Parish|    35| 1583.137| 12.924|   720| 32567.396| 439.401|  22,108|
| |Avoyelles Parish|    34| 846.951| 17.793| 1,107| 27575.727| 427.034|  40,144|
| |Pointe Coupee Parish|    33| 1518.638|  6.574|   816| 37551.772| 355.006|  21,730|
| |St. James Parish|    32| 1516.875|  0.000|   723| 34271.900| 331.816|  21,096|
| |Lincoln Parish|    32| 684.609| 24.450|   815| 17436.139| 216.997|  46,742|
| |Bienville Parish|    30| 2265.690|  0.000|   387| 29227.400| 302.092|  13,241|
| |Allen Parish|    30| 1170.640| 22.298| 1,321| 51547.196| 568.597|  25,627|
| |Vernon Parish|    29| 611.440| 18.072|   789| 16635.392| 168.673|  47,429|
| |Jefferson Davis Parish|    28| 892.629| 18.217| 1,046| 33346.085| 286.917|  31,368|
| |Vermilion Parish|    28| 470.501| 19.204| 1,657| 27843.592| 393.685|  59,511|
| |De Soto Parish|    26| 946.728|  0.000|   745| 27127.408| 254.888|  27,463|
| |St. Bernard Parish|    24| 508.001|  0.000| 1,120| 23706.714| 160.262|  47,244|
| |Beauregard Parish|    20| 533.376| 11.429|   863| 23015.175| 240.019|  37,497|
| |Assumption Parish|    20| 913.617|  0.000|   598| 27317.162| 241.456|  21,891|
| |Grant Parish|    19| 848.631| 31.903|   330| 14739.381| 267.989|  22,389|
| |Franklin Parish|    19| 949.288| 14.275|   954| 47664.252| 670.925|  20,015|
| |Plaquemines Parish|    19| 819.071|  0.000|   462| 19916.368| 197.070|  23,197|
| |West Feliciana Parish|    18| 1156.218| 18.353|   393| 25244.090| 559.756|  15,568|
| |Jackson Parish|    18| 1143.293|  0.000|   383| 24326.728| 154.254|  15,744|
| |Natchitoches Parish|    17| 445.516|  0.000|   809| 21201.321| 269.556|  38,158|
| |Webster Parish|    16| 417.319| 11.178|   903| 23552.426| 178.851|  38,340|
| |Morehouse Parish|    13| 522.634| 11.486|   536| 21548.605| 396.283|  24,874|
| |Red River Parish|    13| 1539.919| 33.844|   250| 29613.836| 693.810|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   286| 18251.436| 446.713|  15,670|
| |Sabine Parish|    11| 460.559|  5.981|   664| 27801.038| 352.896|  23,884|
| |Concordia Parish|     9| 467.314|  7.418|   347| 18017.550| 363.466|  19,259|
| |Richland Parish|     8| 397.575| 14.199|   615| 30563.562| 390.475|  20,122|
| |Winn Parish|     7| 503.452|  0.000|   450| 32364.787| 503.452|  13,904|
| |Evangeline Parish|     7| 209.612| 21.389|   932| 27908.370| 491.947|  33,395|
| |West Carroll Parish|     6| 554.017| 13.191|   298| 27516.159| 303.390|  10,830|
| |Madison Parish|     6| 547.895|  0.000|   625| 57072.413| 378.309|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   300| 31598.905| 406.272|   9,494|
| |Caldwell Parish|     3| 302.480| 14.404|   228| 22988.506| 360.096|   9,918|
| |St. Helena Parish|     2| 197.394| 14.100|   277| 27339.124| 366.590|  10,132|
| |East Carroll Parish|     2| 291.503| 20.822|   520| 75790.701| 187.395|   6,861|
| |LaSalle Parish|     2| 134.300|  0.000|   324| 21756.648| 623.537|  14,892|
| |Tensas Parish|     0|  0.000|  0.000|    91| 20996.770| 758.125|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   171| 24523.161| 81.949|   6,973|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,734| 319.443| N/A|104,248|  8918.394| N/A|11,689,100|
| |Franklin County|   531| 403.264|  1.519|18,965| 14402.820| 146.030|1,316,756|
| |Cuyahoga County|   512| 414.551|  2.892|13,869| 11229.305| 99.242|1,235,072|
| |Lucas County|   326| 761.063|  2.001| 5,512| 12868.042| 132.736| 428,348|
| |Hamilton County|   259| 316.830|  1.748| 9,844| 12041.988| 95.591| 817,473|
| |Mahoning County|   256| 1119.454|  1.874| 2,623| 11470.026| 95.578| 228,683|
| |Summit County|   224| 414.038|  1.584| 3,667|  6778.026| 70.767| 541,013|
| |Stark County|   142| 383.156|  1.927| 1,904|  5137.532| 57.049| 370,606|
| |Trumbull County|   110| 555.629|  3.608| 1,563|  7894.976| 70.716| 197,974|
| |Montgomery County|    98| 184.319|  3.493| 4,489|  8442.937| 100.757| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,831|  5909.635| 76.539| 309,833|
| |Portage County|    64| 393.929|  3.517|   776|  4776.384| 36.931| 162,466|
| |Butler County|    64| 167.043|  1.119| 3,033|  7916.290| 95.080| 383,134|
| |Columbiana County|    60| 588.911|  0.000| 1,683| 16518.948| 106.565| 101,883|
| |Wayne County|    59| 509.895|  1.235|   554|  4787.832| 45.681| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,090|  8332.250| 127.768| 130,817|
| |Licking County|    51| 288.360|  3.231| 1,345|  7604.799| 134.084| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   577|  5933.711| 38.197|  97,241|
| |Allen County|    46| 449.434|  5.583|   794|  7757.618| 156.325| 102,351|
| |Marion County|    45| 691.319|  0.000| 2,942| 45196.872| 89.981|  65,093|
| |Geauga County|    44| 469.840|  0.000|   561|  5990.454| 32.035|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,400| 41055.819| 63.539|  58,457|
| |Lake County|    42| 182.490|  3.104| 1,146|  4979.383| 50.899| 230,149|
| |Warren County|    39| 166.239|  2.436| 1,850|  7885.696| 98.038| 234,602|
| |Miami County|    39| 364.530|  2.671|   868|  8113.135| 106.822| 106,987|
| |Medina County|    36| 200.283|  0.795|   959|  5335.306| 71.530| 179,746|
| |Fairfield County|    32| 203.079|  2.720| 1,432|  9087.794| 133.271| 157,574|
| |Darke County|    29| 567.370|  5.590|   414|  8099.701| 184.465|  51,113|
| |Erie County|    28| 377.023|  1.924|   610|  8213.718| 123.110|  74,266|
| |Ottawa County|    26| 641.579|  3.525|   404|  9969.155| 137.481|  40,525|
| |Belmont County|    26| 388.025|  0.000|   627|  9357.371| 76.752|  67,006|
| |Washington County|    22| 367.211|  0.000|   211|  3521.891| 30.998|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,365|  6525.574| 84.686| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    94|  6884.429| 31.388|  13,654|
| |Sandusky County|    17| 290.509|  2.441|   399|  6818.415| 109.856|  58,518|
| |Putnam County|    17| 502.053|  0.000|   212|  6260.890| 59.065|  33,861|
| |Clark County|    15| 111.871|  1.065| 1,213|  9046.635| 116.133| 134,083|
| |Tuscarawas County|    14| 152.195|  0.000|   797|  8664.268| 59.015|  91,987|
| |Mercer County|    13| 315.749|  0.000|   641| 15568.833| 277.581|  41,172|
| |Richland County|    12| 99.047|  1.179|   619|  5109.200| 70.748| 121,154|
| |Hardin County|    12| 382.592|  0.000|   175|  5579.468| 77.429|  31,365|
| |Greene County|    12| 71.032|  0.846|   730|  4321.137| 72.724| 168,937|
| |Clermont County|    11| 53.287|  0.000|   962|  4660.221| 60.900| 206,428|
| |Madison County|    10| 223.559|  0.000|   503| 11244.998| 510.991|  44,731|
| |Wyandot County|     9| 413.375| 13.123|   151|  6935.514| 150.915|  21,772|
| |Hocking County|     9| 318.426|  0.000|   122|  4316.445| 40.435|  28,264|
| |Coshocton County|     7| 191.257|  3.903|   196|  5355.191| 39.032|  36,600|
| |Guernsey County|     7| 180.064|  0.000|   119|  3061.093| 22.049|  38,875|
| |Knox County|     7| 112.320|  0.000|   214|  3433.779| 57.306|  62,322|
| |Holmes County|     6| 136.488|  0.000|   331|  7529.572| 16.249|  43,960|
| |Auglaize County|     6| 131.418|  3.129|   275|  6023.305| 131.418|  45,656|
| |Clinton County|     6| 142.966|  0.000|   171|  4074.533| 57.867|  41,968|
| |Carroll County|     5| 185.777|  0.000|   113|  4198.558| 15.924|  26,914|
| |Huron County|     5| 85.813|  0.000|   411|  7053.856| 68.651|  58,266|
| |Crawford County|     5| 120.499|  0.000|   177|  4265.677| 30.986|  41,494|
| |Shelby County|     4| 82.321|  0.000|   215|  4424.779| 138.182|  48,590|
| |Seneca County|     4| 72.493|  2.589|   234|  4240.821| 147.574|  55,178|
| |Ross County|     4| 52.174|  0.000|   509|  6639.188| 145.343|  76,666|
| |Defiance County|     4| 105.023|  0.000|   154|  4043.374| 78.767|  38,087|
| |Perry County|     3| 83.024|  0.000|   148|  4095.865| 138.374|  36,134|
| |Ashland County|     3| 56.092|  0.000|   155|  2898.063| 53.421|  53,484|
| |Jefferson County|     3| 45.924|  2.187|   240|  3673.938| 61.232|  65,325|
| |Hancock County|     3| 39.587|  0.000|   397|  5238.642| 99.909|  75,783|
| |Williams County|     3| 81.762|  0.000|   137|  3733.784| 31.147|  36,692|
| |Morrow County|     2| 56.612|  0.000|   179|  5066.803| 64.700|  35,328|
| |Preble County|     2| 48.921|  0.000|   212|  5185.656| 129.292|  40,882|
| |Van Wert County|     2| 70.734|  5.052|    73|  2581.786| 15.157|  28,275|
| |Athens County|     2| 30.615|  2.187|   361|  5526.046| 19.681|  65,327|
| |Logan County|     2| 43.791|  0.000|   167|  3656.507| 96.965|  45,672|
| |Vinton County|     2| 152.847|  0.000|    32|  2445.548| 21.835|  13,085|
| |Brown County|     2| 46.049|  3.289|   150|  3453.675| 98.676|  43,432|
| |Henry County|     2| 74.058|  0.000|   122|  4517.515| 63.478|  27,006|
| |Highland County|     2| 46.338|  3.310|   169|  3915.572| 92.676|  43,161|
| |Adams County|     2| 72.207|  0.000|    64|  2310.636| 25.788|  27,698|
| |Champaign County|     2| 51.434|  0.000|   188|  4834.769| 135.932|  38,885|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 37.994|  15,040|
| |Gallia County|     1| 33.447|  0.000|    74|  2475.082| 57.338|  29,898|
| |Fulton County|     1| 23.738|  0.000|   155|  3679.438| 40.694|  42,126|
| |Muskingum County|     1| 11.599|  0.000|   248|  2876.530| 67.936|  86,215|
| |Union County|     1| 16.953|  0.000|   273|  4628.060| 108.981|  58,988|
| |Scioto County|     1| 13.278|  0.000|   259|  3438.936| 104.325|  75,314|
| |Fayette County|     0|  0.000|  0.000|   124|  4347.064| 100.163|  28,525|
| |Lawrence County|     0|  0.000|  0.000|   318|  5347.863| 201.806|  59,463|
| |Meigs County|     0|  0.000|  0.000|    58|  2531.977| 180.856|  22,907|
| |Pike County|     0|  0.000|  0.000|    80|  2880.599| 36.007|  27,772|
| |Paulding County|     0|  0.000|  0.000|    70|  3748.929| 45.905|  18,672|
| |Noble County|     0|  0.000|  0.000|    17|  1178.591|  9.904|  14,424|
| |Morgan County|     0|  0.000|  0.000|    30|  2067.825| 88.621|  14,508|
| |Jackson County|     0|  0.000|  0.000|    77|  2375.590| 30.852|  32,413|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,598| 595.136| N/A|97,384| 16108.031| N/A|6,045,680|
| |Baltimore County| 1,001| 1209.858|  4.317|26,454| 31973.603| 316.839| 827,370|
| |Montgomery County|   806| 767.116|  1.632|18,641| 17741.708| 90.417|1,050,688|
| |Prince George's County|   764| 840.182|  2.828|24,098| 26500.918| 147.990| 909,327|
| |Anne Arundel County|   228| 393.623|  1.973| 7,479| 12911.880| 90.020| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,118| 12013.238| 53.940| 259,547|
| |Carroll County|   118| 700.517|  0.848| 1,572|  9332.312| 51.733| 168,447|
| |Howard County|   112| 343.885|  2.632| 3,941| 12100.464| 98.253| 325,690|
| |Charles County|    91| 557.403|  0.000| 2,084| 12765.149| 119.881| 163,257|
| |Harford County|    69| 270.121|  0.000| 2,034|  7962.700| 87.244| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,012|  8915.514| 84.322| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,361| 13135.924| 62.046| 103,609|
| |Washington County|    31| 205.231|  0.000| 1,041|  6891.803| 49.180| 151,049|
| |Cecil County|    30| 291.673|  0.000|   714|  6941.811| 58.335| 102,855|
| |Calvert County|    28| 302.621|  0.000|   715|  7727.641| 84.919|  92,525|
| |Queen Anne's County|    26| 516.068|  2.836|   440|  8733.451| 107.750|  50,381|
| |Kent County|    23| 1184.224|  0.000|   243| 12511.585| 58.843|  19,422|
| |Worcester County|    20| 382.585|  0.000|   704| 13466.983| 131.172|  52,276|
| |Allegany County|    18| 255.624|  0.000|   303|  4302.999| 54.777|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   378| 11838.767| 111.855|  31,929|
| |Talbot County|     4| 107.582|  0.000|   404| 10865.765| 134.477|  37,181|
| |Somerset County|     3| 117.114|  0.000|   141|  5504.372| 66.922|  25,616|
| |Caroline County|     3| 89.804|  0.000|   454| 13590.373| 55.593|  33,406|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    53|  1826.704| 39.390|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,878| 427.496| N/A|76,522| 11366.535| N/A|6,732,219|
| |Marion County|   731| 757.841|  1.037|16,194| 16788.619| 154.323| 964,582|
| |Lake County|   281| 578.793|  2.354| 7,742| 15946.677| 153.011| 485,493|
| |Allen County|   163| 429.740|  1.130| 4,040| 10651.228| 129.939| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,794| 11342.442| 108.385| 158,167|
| |Hendricks County|   108| 634.134|  2.516| 1,943| 11408.541| 123.304| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,887|  8541.142| 133.132| 338,011|
| |Elkhart County|    86| 416.786|  4.846| 4,955| 24013.647| 190.392| 206,341|
| |St. Joseph County|    83| 305.342|  2.102| 3,610| 13280.554| 202.861| 271,826|
| |Madison County|    66| 509.381|  1.103| 1,030|  7949.432| 174.204| 129,569|
| |Howard County|    65| 787.459|  0.000|   920| 11145.571| 157.492|  82,544|
| |Delaware County|    52| 455.601|  0.000|   760|  6658.781| 118.907| 114,135|
| |Clark County|    50| 422.647|  4.830| 1,307| 11047.996| 218.569| 118,302|
| |Floyd County|    49| 624.029|  7.277|   822| 10468.404| 169.197|  78,522|
| |Bartholomew County|    47| 561.000|  0.000|   821|  9799.592| 122.772|  83,779|
| |Boone County|    46| 678.036|  0.000|   697| 10273.720| 101.074|  67,843|
| |Hancock County|    39| 498.925|  1.828|   688|  8801.556| 98.689|  78,168|
| |Porter County|    39| 228.888|  0.000| 1,362|  7993.474| 124.924| 170,389|
| |Greene County|    34| 1065.096|  0.000|   254|  7956.895| 62.653|  31,922|
| |Morgan County|    34| 482.345|  0.000|   489|  6937.253| 99.306|  70,489|
| |Monroe County|    32| 215.588|  1.925|   767|  5167.384| 65.446| 148,431|
| |Decatur County|    32| 1204.865|  0.000|   342| 12876.991| 107.577|  26,559|
| |LaPorte County|    30| 273.005|  1.300|   935|  8508.663| 110.502| 109,888|
| |Warrick County|    30| 476.206|  0.000|   588|  9333.630| 108.847|  62,998|
| |Grant County|    30| 456.142|  2.172|   531|  8073.713| 43.442|  65,769|
| |Noble County|    29| 607.406|  0.000|   690| 14452.078| 155.592|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   516| 10433.095| 112.650|  49,458|
| |Shelby County|    28| 625.992|  3.194|   568| 12698.697| 121.366|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   357|  7868.636| 78.718|  45,370|
| |Orange County|    24| 1221.623|  0.000|   178|  9060.369| 101.802|  19,646|
| |Harrison County|    24| 592.373|  7.052|   352|  8688.140| 169.249|  40,515|
| |Marshall County|    23| 497.211|  3.088|   794| 17164.599| 129.707|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   360|  9390.161| 63.346|  38,338|
| |Daviess County|    20| 599.682|  4.283|   279|  8365.566| 119.936|  33,351|
| |Henry County|    20| 416.910|  2.978|   418|  8713.416| 157.830|  47,972|
| |Franklin County|    15| 659.109| 12.554|   247| 10853.326| 100.436|  22,758|
| |Vanderburgh County|    13| 71.645|  0.000| 2,053| 11314.349| 199.188| 181,451|
| |Perry County|    13| 678.178|  7.453|   187|  9755.334| 111.788|  19,169|
| |Dubois County|    12| 280.794|  0.000|   713| 16683.826| 193.881|  42,736|
| |Kosciusko County|    12| 151.027|  0.000|   872| 10974.627| 86.301|  79,456|
| |Jennings County|    12| 432.666|  0.000|   228|  8220.660| 72.111|  27,735|
| |Tipton County|    12| 792.184| 56.585|   149|  9836.282| 216.907|  15,148|
| |Vigo County|    11| 102.767|  1.335|   714|  6670.528| 248.243| 107,038|
| |White County|    11| 456.394|  5.927|   377| 15641.855| 165.961|  24,102|
| |Tippecanoe County|    11| 56.199|  0.000| 1,245|  6360.738| 89.043| 195,732|
| |Wayne County|    10| 151.782|  0.000|   388|  5889.138| 110.584|  65,884|
| |Newton County|    10| 715.103|  0.000|   121|  8652.746| 71.510|  13,984|
| |Scott County|    10| 418.883|  0.000|   273| 11435.513| 125.665|  23,873|
| |LaGrange County|    10| 252.436|  0.000|   566| 14287.878| 61.306|  39,614|
| |Cass County|     9| 238.796|  0.000| 1,806| 47918.491| 174.359|  37,689|
| |Putnam County|     8| 212.902|  0.000|   321|  8542.687| 330.758|  37,576|
| |Ripley County|     8| 282.446|  5.044|   213|  7520.124| 95.830|  28,324|
| |Starke County|     7| 304.414|  0.000|   180|  7827.789| 62.125|  22,995|
| |Fayette County|     7| 303.004|  0.000|   195|  8440.828| 197.880|  23,102|
| |Whitley County|     6| 176.658|  0.000|   156|  4593.099| 29.443|  33,964|
| |Ohio County|     6| 1021.277| 48.632|    65| 11063.830| 218.845|   5,875|
| |Clay County|     5| 190.658|  0.000|   131|  4995.234| 157.974|  26,225|
| |Jackson County|     5| 113.043|  3.230|   597| 13497.321| 132.422|  44,231|
| |Wabash County|     5| 161.311|  9.218|   171|  5516.841| 46.089|  30,996|
| |Gibson County|     4| 118.839|  0.000|   233|  6922.368| 123.083|  33,659|
| |Randolph County|     4| 162.173|  0.000|   127|  5148.997| 104.254|  24,665|
| |DeKalb County|     4| 92.007|  0.000|   238|  5474.411| 52.575|  43,475|
| |Clinton County|     4| 123.461|  4.409|   450| 13889.318| 273.377|  32,399|
| |Rush County|     4| 241.240|  0.000|    89|  5367.589| 77.541|  16,581|
| |Huntington County|     3| 82.147|  0.000|   127|  3477.547| 31.294|  36,520|
| |Steuben County|     3| 86.720|  0.000|   215|  6214.951| 49.554|  34,594|
| |Spencer County|     3| 147.951|  0.000|   139|  6855.057| 162.041|  20,277|
| |Carroll County|     3| 148.097|  7.052|   200|  9873.130| 338.507|  20,257|
| |Miami County|     2| 56.313|  0.000|   277|  7799.302| 68.380|  35,516|
| |Wells County|     2| 70.681|  0.000|   178|  6290.642| 171.655|  28,296|
| |Jefferson County|     2| 61.904|  0.000|   166|  5138.046| 57.482|  32,308|
| |Jasper County|     2| 59.591|  0.000|   257|  7657.470| 174.517|  33,562|
| |Fulton County|     2| 100.130|  0.000|   173|  8661.260| 164.500|  19,974|
| |Brown County|     2| 132.521|  9.466|    75|  4969.520| 47.329|  15,092|
| |Blackford County|     2| 170.097|  0.000|    66|  5613.200| 121.498|  11,758|
| |Fountain County|     2| 122.354|  0.000|    76|  4649.456| 104.875|  16,346|
| |Adams County|     2| 55.902|  0.000|   117|  3270.257| 131.769|  35,777|
| |Warren County|     1| 120.992|  0.000|    24|  2903.811| 86.423|   8,265|
| |Washington County|     1| 35.668|  0.000|   144|  5136.253| 137.578|  28,036|
| |Parke County|     1| 59.042|  0.000|    55|  3247.328| 50.608|  16,937|
| |Pulaski County|     1| 80.952|  0.000|    82|  6638.064| 80.952|  12,353|
| |Sullivan County|     1| 48.382|  0.000|   141|  6821.810| 400.876|  20,669|
| |Owen County|     1| 48.079|  0.000|   105|  5048.320| 157.975|  20,799|
| |Jay County|     0|  0.000|  0.000|    92|  4501.859| 69.905|  20,436|
| |Vermillion County|     0|  0.000|  0.000|    59|  3806.943| 110.613|  15,498|
| |Switzerland County|     0|  0.000|  0.000|    53|  4929.774| 132.878|  10,751|
| |Posey County|     0|  0.000|  0.000|   180|  7079.089| 106.748|  25,427|
| |Pike County|     0|  0.000|  0.000|    62|  5004.439| 138.372|  12,389|
| |Martin County|     0|  0.000|  0.000|    50|  4875.670| 111.444|  10,255|
| |Knox County|     0|  0.000|  0.000|   164|  4481.609| 93.692|  36,594|
| |Crawford County|     0|  0.000|  0.000|    45|  4254.515| 13.506|  10,577|
| |Union County|     0|  0.000|  0.000|    41|  5812.305| 162.015|   7,054|
| |Benton County|     0|  0.000|  0.000|    64|  7315.958| 65.321|   8,748|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,352| 275.554| N/A|102,521| 12011.103| N/A|8,535,519|
| |Fairfax County|   536| 467.089|  0.000|16,734| 14582.600| 78.803|1,147,532|
| |Henrico County|   186| 562.243|  1.727| 3,968| 11994.511| 109.685| 330,818|
| |Prince William County|   176| 374.201|  0.304| 9,605| 20421.614| 141.540| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,118| 13164.895| 72.984| 236,842|
| |Loudoun County|   115| 278.088|  0.691| 5,372| 12990.342| 88.090| 413,538|
| |Chesterfield County|    80| 226.756|  2.025| 4,475| 12684.168| 123.501| 352,802|
| |Alexandria city|    60| 376.345|  0.000| 3,014| 18905.086| 127.241| 159,428|
| |Virginia Beach city|    54| 120.007|  1.587| 5,139| 11420.660| 176.518| 449,974|
| |Suffolk city|    53| 575.411|  6.204| 1,334| 14482.998| 259.013|  92,108|
| |Shenandoah County|    46| 1054.659| 13.101|   724| 16599.413| 124.463|  43,616|
| |Richmond County|    45| 4987.255| 31.665| 3,570| 395655.547| 3467.330|   9,023|
| |Chesapeake city|    38| 155.207|  2.917| 3,008| 12285.825| 171.544| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,536| 11276.291| 153.119| 136,215|
| |Hanover County|    33| 306.219|  1.326|   660|  6124.381| 64.956| 107,766|
| |Norfolk city|    33| 135.947|  2.943| 3,802| 15662.720| 181.851| 242,742|
| |Mecklenburg County|    32| 1046.196|  0.000|   447| 14614.052| 551.121|  30,587|
| |Harrisonburg city|    31| 584.729|  2.695| 1,083| 20427.795| 37.724|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   296| 25277.541| 12.200|  11,710|
| |Portsmouth city|    25| 264.836|  0.000| 1,855| 19650.840| 290.563|  94,398|
| |Page County|    25| 1045.938|  5.977|   347| 14517.614| 59.768|  23,902|
| |Galax city|    24| 3781.314|  0.000|   351| 55301.717| 202.570|   6,347|
| |Manassas city|    23| 559.815| 10.431| 1,670| 40647.438| 173.856|  41,085|
| |Colonial Heights city|    22| 1266.552|  8.224|   203| 11686.816| 123.365|  17,370|
| |Newport News city|    19| 106.012|  0.797| 1,872| 10444.971| 109.997| 179,225|
| |Roanoke County|    19| 201.728|  1.517| 1,538| 16329.391| 221.446|  94,186|
| |Rockingham County|    19| 231.854|  3.487|   957| 11678.137| 64.501|  81,948|
| |Petersburg city|    19| 606.138|  4.557|   531| 16939.960| 195.969|  31,346|
| |Accomack County|    17| 526.055|  8.841| 1,108| 34286.422| 101.675|  32,316|
| |James City County|    17| 222.155|  1.867|   621|  8115.207| 89.609|  76,523|
| |Albemarle County|    16| 146.346|  0.000|   856|  7829.507| 84.933| 109,330|
| |Charlottesville city|    15| 317.353|  6.045|   550| 11636.271| 139.031|  47,266|
| |Emporia city|    15| 2805.836|  0.000|   180| 33670.034| 240.500|   5,346|
| |Carroll County|    14| 469.941|  9.591|   333| 11177.873| 134.269|  29,791|
| |Nottoway County|    14| 919.118| 46.894|   182| 11948.529| 37.515|  15,232|
| |Southampton County|    13| 737.338|  0.000|   285| 16164.710| 307.899|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,012| 19237.715| 130.352|  52,605|
| |Prince Edward County|    11| 482.414|  6.265|   423| 18551.004| 231.809|  22,802|
| |Greensville County|    11| 970.360| 12.602|   529| 46665.490| 1146.789|  11,336|
| |Fauquier County|     9| 126.365|  0.000|   623|  8747.297| 70.203|  71,222|
| |Frederick County|     9| 100.769|  0.000|   686|  7680.853| 20.794|  89,313|
| |Henry County|     9| 178.017|  8.477|   611| 12085.369| 228.879|  50,557|
| |Sussex County|     9| 806.524|  0.000|   310| 27780.267| 371.257|  11,159|
| |Stafford County|     9| 58.869|  0.934| 1,424|  9314.373| 115.869| 152,882|
| |Fluvanna County|     9| 330.033|  5.239|   196|  7187.385| 104.772|  27,270|
| |Isle of Wight County|     9| 242.529|  0.000|   401| 10806.004| 138.588|  37,109|
| |Buckingham County|     8| 466.527|  0.000|   611| 35630.977| 116.632|  17,148|
| |Bedford County|     8| 101.270|  1.808|   370|  4683.722| 88.611|  78,997|
| |Goochland County|     7| 294.700|  0.000|   167|  7030.691| 84.200|  23,753|
| |Hampton city|     7| 52.041|  0.000| 1,273|  9463.980| 152.936| 134,510|
| |Danville city|     7| 174.808|  0.000|   419| 10463.490| 231.888|  40,044|
| |Franklin County|     7| 124.906|  0.000|   364|  6495.129| 112.161|  56,042|
| |Dinwiddie County|     7| 245.235|  0.000|   223|  7812.500| 70.067|  28,544|
| |Manassas Park city|     7| 400.503|  0.000|   518| 29637.258| 106.256|  17,478|
| |Botetourt County|     7| 209.462|  0.000|   216|  6463.389| 98.319|  33,419|
| |Williamsburg city|     6| 401.230|  0.000|   128|  8559.583| 85.978|  14,954|
| |Falls Church city|     6| 410.481|  9.773|    61|  4173.223| 19.547|  14,617|
| |Warren County|     6| 149.388|  0.000|   356|  8863.659| 14.227|  40,164|
| |Washington County|     6| 111.649|  2.658|   237|  4410.123| 122.282|  53,740|
| |Caroline County|     5| 162.734|  0.000|   218|  7095.199| 116.239|  30,725|
| |Grayson County|     5| 321.543|  0.000|   156| 10032.154| 101.056|  15,550|
| |Hopewell city|     5| 221.936|  0.000|   278| 12339.651| 120.480|  22,529|
| |Lynchburg city|     5| 60.851|  1.739|   654|  7959.303| 262.528|  82,168|
| |Charles City County|     5| 718.081|  0.000|    53|  7611.662| 41.033|   6,963|
| |Alleghany County|     4| 269.179|  0.000|    62|  4172.275| 48.068|  14,860|
| |Augusta County|     4| 52.939|  0.000|   287|  3798.407| 47.267|  75,558|
| |King George County|     4| 149.054|  0.000|   153|  5701.297| 154.377|  26,836|
| |Patrick County|     4| 227.169|  0.000|   161|  9143.571| 340.754|  17,608|
| |Fredericksburg city|     4| 137.760|  4.920|   414| 14258.162| 167.280|  29,036|
| |Powhatan County|     4| 134.898|  0.000|   151|  5092.405| 77.085|  29,652|
| |Winchester city|     4| 142.460|  0.000|   404| 14388.489| 40.703|  28,078|
| |York County|     4| 58.582|  0.000|   375|  5492.091| 83.689|  68,280|
| |Martinsville city|     3| 238.968|  0.000|   219| 17444.639| 455.176|  12,554|
| |Waynesboro city|     3| 132.567|  0.000|   177|  7821.476| 63.127|  22,630|
| |Scott County|     3| 139.108|  0.000|   111|  5146.991| 317.961|  21,566|
| |Smyth County|     3| 99.655|  0.000|   154|  5115.599| 132.873|  30,104|
| |Westmoreland County|     3| 166.528|  0.000|   214| 11878.990| 134.808|  18,015|
| |Wise County|     3| 80.250|  0.000|   181|  4841.773| 275.144|  37,383|
| |Salem city|     3| 118.572|  0.000|   163|  6442.433| 107.280|  25,301|
| |Wythe County|     3| 104.588|  0.000|   119|  4148.654| 54.784|  28,684|
| |Pulaski County|     3| 88.165|  0.000|    90|  2644.958| 46.182|  34,027|
| |Northumberland County|     3| 248.036| 11.811|    78|  6448.946| 106.301|  12,095|
| |Orange County|     3| 80.969|  0.000|   231|  6234.650| 38.557|  37,051|
| |Montgomery County|     3| 30.446|  0.000|   312|  3166.388| 30.446|  98,535|
| |Amelia County|     2| 152.149| 10.868|    82|  6238.113| 86.942|  13,145|
| |Campbell County|     2| 36.440|  0.000|   216|  3935.502| 124.937|  54,885|
| |Floyd County|     2| 126.992|  9.071|    90|  5714.649| 444.473|  15,749|
| |Brunswick County|     2| 123.221|  0.000|   239| 14724.909| 211.236|  16,231|
| |Russell County|     2| 75.228|  0.000|   134|  5040.247| 241.803|  26,586|
| |Rappahannock County|     2| 271.370|  0.000|    44|  5970.149| 58.151|   7,370|
| |Prince George County|     2| 52.147|  0.000|   424| 11055.198| 294.259|  38,353|
| |Pittsylvania County|     2| 33.138|  0.000|   516|  8549.558| 314.809|  60,354|
| |Surry County|     2| 311.429|  0.000|    51|  7941.451| 200.205|   6,422|
| |Gloucester County|     2| 53.550|  0.000|   166|  4444.682| 72.676|  37,348|
| |Halifax County|     2| 58.978|  4.213|   159|  4688.744| 58.978|  33,911|
| |Greene County|     2| 100.913|  0.000|   169|  8527.171| 122.538|  19,819|
| |Louisa County|     2| 53.204|  0.000|   195|  5187.412| 91.207|  37,591|
| |King William County|     2| 116.632|  0.000|    91|  5306.741| 99.970|  17,148|
| |Dickenson County|     1| 69.842|  0.000|    49|  3422.266| 159.639|  14,318|
| |Essex County|     1| 91.299|  0.000|   105|  9586.415| 273.898|  10,953|
| |Lee County|     1| 42.693|  0.000|   130|  5550.100| 158.574|  23,423|
| |Lunenburg County|     1| 81.994|  0.000|    66|  5411.610| 81.994|  12,196|
| |Madison County|     1| 75.409|  0.000|    71|  5354.046| 75.409|  13,261|
| |Middlesex County|     1| 94.500|  0.000|    46|  4347.004| 189.000|  10,582|
| |Rockbridge County|     1| 44.301|  6.329|    69|  3056.749| 18.986|  22,573|
| |New Kent County|     1| 43.307|  0.000|   129|  5586.592| 49.494|  23,091|
| |Buena Vista city|     1| 154.369|  0.000|    58|  8953.381| 176.421|   6,478|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 101.678|   7,025|
| |Amherst County|     1| 31.641|  4.520|   184|  5821.864| 244.084|  31,605|
| |Buchanan County|     1| 47.610|  6.801|    80|  3808.798| 47.610|  21,004|
| |Lancaster County|     0|  0.000|  0.000|    41|  3866.830| 121.259|  10,603|
| |Mathews County|     0|  0.000|  0.000|    18|  2037.582| 48.514|   8,834|
| |Nelson County|     0|  0.000|  0.000|    54|  3616.879| 191.369|  14,930|
| |Clarke County|     0|  0.000|  0.000|    72|  4925.097| 29.316|  14,619|
| |Charlotte County|     0|  0.000|  0.000|    55|  4629.630| 60.125|  11,880|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 130.463|   2,190|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 27.842|   5,131|
| |Cumberland County|     0|  0.000|  0.000|    77|  7752.718| 86.301|   9,932|
| |Giles County|     0|  0.000|  0.000|    27|  1614.833| 34.176|  16,720|
| |Appomattox County|     0|  0.000|  0.000|    89|  5593.614| 125.699|  15,911|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Bland County|     0|  0.000|  0.000|    25|  3980.892| 386.715|   6,280|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910|  0.000|   7,446|
| |Norton city|     0|  0.000|  0.000|    21|  5275.057| 215.308|   3,981|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 34.926|  12,271|
| |Radford city|     0|  0.000|  0.000|    58|  3178.256| 187.877|  18,249|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Staunton city|     0|  0.000|  0.000|   154|  6176.801| 57.299|  24,932|
| |Bristol city|     0|  0.000|  0.000|    88|  5249.970| 153.408|  16,762|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Tazewell County|     0|  0.000|  0.000|   123|  3029.930| 70.382|  40,595|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,290| 218.343| N/A|139,739| 13323.597| N/A|10,488,084|
| |Mecklenburg County|   243| 218.849|  2.702|22,612| 20364.640| 140.881|1,110,356|
| |Wake County|   178| 160.106|  5.268|12,263| 11030.248| 107.680|1,111,761|
| |Guilford County|   156| 290.409|  0.798| 5,753| 10709.751| 111.164| 537,174|
| |Durham County|    80| 248.843|  0.444| 6,231| 19381.750| 107.536| 321,488|
| |Orange County|    58| 390.636| 12.508| 1,361|  9166.465| 50.994| 148,476|
| |Robeson County|    55| 421.053|  4.375| 2,854| 21848.804| 153.110| 130,625|
| |Gaston County|    55| 244.957|  8.908| 3,392| 15107.180| 170.516| 224,529|
| |Chatham County|    55| 738.552|  7.673| 1,308| 17564.120| 90.161|  74,470|
| |Henderson County|    55| 468.416|  1.217| 1,505| 12817.565| 92.467| 117,417|
| |Cumberland County|    54| 160.949|  1.703| 3,286|  9794.074| 172.872| 335,509|
| |Forsyth County|    53| 138.636|  0.747| 5,381| 14075.518| 131.910| 382,295|
| |Buncombe County|    50| 191.431|  2.188| 1,929|  7385.400| 94.075| 261,191|
| |Cabarrus County|    50| 230.997|  0.660| 2,681| 12386.061| 116.818| 216,453|
| |Rowan County|    49| 344.857|  1.005| 2,248| 15821.181| 176.953| 142,088|
| |Duplin County|    48| 817.146|  0.000| 2,015| 34303.127| 131.327|  58,741|
| |Columbus County|    48| 864.740|  5.147|   931| 16772.357| 205.891|  55,508|
| |Johnston County|    46| 219.739|  1.365| 3,357| 16036.190| 151.497| 209,339|
| |Union County|    43| 179.272|  0.596| 3,170| 13216.098| 142.941| 239,859|
| |Wayne County|    42| 341.100|  2.320| 2,445| 19856.900| 127.622| 123,131|
| |Vance County|    41| 920.624|  3.208|   787| 17671.494| 131.518|  44,535|
| |Alamance County|    41| 241.875|  0.000| 2,526| 14901.864| 192.152| 169,509|
| |Harnett County|    40| 294.170|  2.101| 1,337|  9832.618| 155.490| 135,976|
| |Randolph County|    38| 264.501|  1.989| 2,199| 15306.229| 113.357| 143,667|
| |Wilson County|    35| 427.868|  0.000| 1,514| 18508.331| 117.009|  81,801|
| |Stanly County|    31| 493.583| 15.922| 1,103| 17562.016| 375.305|  62,806|
| |Catawba County|    30| 188.028|  0.895| 2,180| 13663.343| 173.702| 159,551|
| |Granville County|    29| 479.791|  4.727| 1,278| 21143.888| 198.534|  60,443|
| |Burke County|    28| 309.444|  0.000| 1,776| 19627.563| 219.452|  90,485|
| |Franklin County|    26| 373.108|  2.050|   891| 12786.109| 164.003|  69,685|
| |Cleveland County|    22| 224.611|  7.293| 1,217| 12425.087| 175.022|  97,947|
| |Brunswick County|    22| 154.040|  5.001| 1,273|  8913.317| 60.016| 142,820|
| |Moore County|    20| 198.255|  0.000| 1,031| 10220.063| 118.953| 100,880|
| |Pasquotank County|    20| 502.210| 10.762|   423| 10621.736| 225.994|  39,824|
| |New Hanover County|    20| 85.298|  0.000| 2,696| 11498.126| 150.489| 234,473|
| |Davidson County|    18| 107.393|  0.000| 1,817| 10840.707| 108.245| 167,609|
| |Sampson County|    18| 283.326| 11.243| 1,511| 23783.665| 161.901|  63,531|
| |Iredell County|    18| 99.007|  0.000| 1,905| 10478.202| 105.293| 181,806|
| |Northampton County|    16| 821.229|  0.000|   351| 18015.706| 161.313|  19,483|
| |Caldwell County|    16| 194.699|  3.477| 1,234| 15016.184| 130.379|  82,178|
| |McDowell County|    16| 349.681|  9.366|   690| 15079.990| 215.428|  45,756|
| |Haywood County|    15| 240.705| 16.047|   441|  7076.721| 181.102|  62,317|
| |Rutherford County|    15| 223.784|  2.131|   781| 11651.673| 196.077|  67,029|
| |Craven County|    15| 146.859|  6.993|   753|  7372.306| 111.892| 102,139|
| |Montgomery County|    14| 515.217|  0.000|   740| 27232.915| 504.703|  27,173|
| |Edgecombe County|    13| 252.565|  2.775|   672| 13055.642| 185.954|  51,472|
| |Wilkes County|    12| 175.408|  4.176|   852| 12453.955| 225.524|  68,412|
| |Nash County|    12| 127.256|  0.000| 1,220| 12937.708| 203.004|  94,298|
| |Lenoir County|    12| 214.481|  0.000|   599| 10706.179| 150.647|  55,949|
| |Pitt County|    11| 60.860|  0.000| 2,105| 11646.435| 214.987| 180,742|
| |Onslow County|    11| 55.573|  0.722| 1,138|  5749.275| 108.981| 197,938|
| |Lee County|    11| 178.054|  0.000| 1,306| 21139.870| 152.618|  61,779|
| |Hoke County|    11| 199.153|  5.173|   738| 13361.335| 116.388|  55,234|
| |Hertford County|    11| 464.586|  0.000|   358| 15120.159| 289.612|  23,677|
| |Surry County|    10| 139.309|  1.990|   967| 13471.156| 177.121|  71,783|
| |Lincoln County|    10| 116.129| 11.613|   869| 10091.626| 145.991|  86,111|
| |Richmond County|     9| 200.763|  0.000|   524| 11688.862| 108.348|  44,829|
| |Rockingham County|     8| 87.902|  1.570|   567|  6230.085| 114.587|  91,010|
| |Jones County|     8| 849.347| 60.668|    99| 10510.670| 303.338|   9,419|
| |Bladen County|     7| 213.923|  0.000|   627| 19161.420| 135.339|  32,722|
| |Jackson County|     7| 159.315|  9.754|   457| 10401.020| 136.556|  43,938|
| |Davie County|     7| 163.376|  3.334|   431| 10059.282| 133.368|  42,846|
| |Warren County|     7| 354.772|  0.000|   261| 13227.915| 65.162|  19,731|
| |Yadkin County|     6| 159.291|  0.000|   557| 14787.480| 166.876|  37,667|
| |Polk County|     6| 289.519|  6.893|   164|  7913.530| 124.080|  20,724|
| |Halifax County|     6| 119.976|  0.000|   721| 14417.117| 182.821|  50,010|
| |Martin County|     6| 267.380|  0.000|   268| 11942.959| 146.422|  22,440|
| |Carteret County|     6| 86.364|  0.000|   376|  5412.175| 90.477|  69,473|
| |Scotland County|     5| 143.583| 12.307|   374| 10740.028| 254.347|  34,823|
| |Bertie County|     5| 263.894|  0.000|   287| 15147.517| 248.814|  18,947|
| |Washington County|     4| 345.423|  0.000|   136| 11744.387| 148.038|  11,580|
| |Cherokee County|     4| 139.801|  4.993|   296| 10345.310| 154.780|  28,612|
| |Macon County|     4| 111.551|  3.984|   480| 13386.134| 79.679|  35,858|
| |Mitchell County|     3| 200.481|  9.547|   120|  8019.246| 38.187|  14,964|
| |Greene County|     3| 142.389|  0.000|   333| 15805.211| 101.707|  21,069|
| |Pender County|     3| 47.574|  0.000|   669| 10608.944| 81.555|  63,060|
| |Stokes County|     3| 65.802|  0.000|   296|  6492.509| 59.536|  45,591|
| |Anson County|     3| 122.719|  5.844|   339| 13867.299| 163.626|  24,446|
| |Swain County|     2| 140.144|  0.000|   121|  8478.733| 150.155|  14,271|
| |Gates County|     2| 172.980|  0.000|    47|  4065.041| 12.356|  11,562|
| |Perquimans County|     2| 148.555|  0.000|    88|  6536.433| 148.555|  13,463|
| |Person County|     2| 50.646|  0.000|   228|  5773.614| 94.056|  39,490|
| |Caswell County|     2| 88.480|  0.000|   196|  8671.032| 44.240|  22,604|
| |Chowan County|     2| 143.441| 10.246|   158| 11331.851| 133.195|  13,943|
| |Camden County|     2| 184.043|  0.000|    75|  6901.629| 144.606|  10,867|
| |Dare County|     2| 54.041|  0.000|   210|  5674.295| 27.020|  37,009|
| |Alexander County|     2| 53.338|  0.000|   314|  8374.003| 72.387|  37,497|
| |Beaufort County|     2| 42.559|  0.000|   437|  9299.059| 194.554|  46,994|
| |Tyrrell County|     1| 249.004|  0.000|    99| 24651.394| 249.004|   4,016|
| |Ashe County|     1| 36.761|  0.000|   166|  6102.268| 141.791|  27,203|
| |Pamlico County|     1| 78.579|  0.000|    73|  5736.288| 89.805|  12,726|
| |Transylvania County|     1| 29.082|  0.000|   145|  4216.955| 54.010|  34,385|
| |Avery County|     0|  0.000|  0.000|   109|  6208.350| 81.368|  17,557|
| |Alleghany County|     0|  0.000|  0.000|   170| 15264.434| 64.136|  11,137|
| |Currituck County|     0|  0.000|  0.000|    77|  2773.475| 30.874|  27,763|
| |Graham County|     0|  0.000|  0.000|    43|  5094.183| 236.939|   8,441|
| |Hyde County|     0|  0.000|  0.000|    46|  9317.399| 260.424|   4,937|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984|  0.000|  11,231|
| |Madison County|     0|  0.000|  0.000|    49|  2252.356| 52.533|  21,755|
| |Yancey County|     0|  0.000|  0.000|   114|  6309.148| 102.781|  18,069|
| |Watauga County|     0|  0.000|  0.000|   316|  5625.078| 83.918|  56,177|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,144| 416.415| N/A|102,974| 19999.946| N/A|5,148,714|
| |Greenville County|   218| 416.394|  5.457|11,056| 21117.694| 153.078| 523,542|
| |Charleston County|   206| 500.722|  8.334|12,555| 30517.299| 218.415| 411,406|
| |Horry County|   162| 457.522|  8.473| 8,706| 24587.594| 156.946| 354,081|
| |Richland County|   158| 380.028|  3.436| 9,049| 21765.013| 242.242| 415,759|
| |Florence County|   119| 860.492| 14.462| 3,551| 25677.366| 377.046| 138,293|
| |Lexington County|   115| 384.937|  3.825| 5,054| 16917.155| 119.068| 298,750|
| |Spartanburg County|   108| 337.727|  6.254| 4,222| 13202.621| 144.740| 319,785|
| |Orangeburg County|    70| 812.301| 16.578| 2,462| 28569.771| 306.685|  86,175|
| |Berkeley County|    69| 302.755|  5.015| 4,298| 18858.570| 176.764| 227,907|
| |Anderson County|    67| 330.769| 11.284| 2,440| 12045.933| 184.074| 202,558|
| |Beaufort County|    58| 301.892|  3.718| 4,214| 21933.979| 270.661| 192,122|
| |Clarendon County|    54| 1600.237| 16.934|   867| 25692.695| 266.706|  33,745|
| |Sumter County|    53| 496.622|  9.370| 2,586| 24231.407| 255.673| 106,721|
| |Dorchester County|    51| 313.250|  7.020| 3,147| 19329.398| 207.956| 162,809|
| |Laurens County|    46| 681.552| 10.583| 1,353| 20046.523| 207.429|  67,493|
| |Aiken County|    42| 245.798|  7.524| 1,991| 11651.997| 238.274| 170,872|
| |Darlington County|    36| 540.394|  2.144| 1,346| 20204.749| 368.841|  66,618|
| |Colleton County|    34| 902.407|  7.583|   831| 22055.896| 197.165|  37,677|
| |Williamsburg County|    31| 1020.811|  9.408| 1,036| 34114.858| 371.632|  30,368|
| |Cherokee County|    31| 541.012|  7.479|   679| 11849.913| 256.794|  57,300|
| |Lee County|    30| 1782.743| 25.468|   561| 33337.295| 203.742|  16,828|
| |York County|    29| 103.211|  0.508| 3,678| 13089.946| 171.340| 280,979|
| |Kershaw County|    27| 405.704|  8.586| 1,418| 21306.968| 169.580|  66,551|
| |Pickens County|    27| 212.793|  3.378| 1,882| 14832.445| 118.218| 126,884|
| |Lancaster County|    26| 265.274|  4.373| 1,265| 12906.583| 227.377|  98,012|
| |Dillon County|    25| 820.237|  9.374|   657| 21555.825| 299.972|  30,479|
| |Bamberg County|    25| 1777.335| 50.781|   481| 34195.933| 294.530|  14,066|
| |Fairfield County|    24| 1073.970|  6.393|   574| 25685.774| 166.210|  22,347|
| |Georgetown County|    24| 382.897| 11.396| 1,492| 23803.446| 360.106|  62,680|
| |Chesterfield County|    21| 460.022|  3.129|   791| 17327.492| 212.799|  45,650|
| |Greenwood County|    20| 282.442|  8.070| 1,455| 20547.655| 284.459|  70,811|
| |Jasper County|    17| 565.291| 19.001|   608| 20217.471| 275.520|  30,073|
| |Chester County|    14| 434.189|  4.431|   709| 21988.587| 487.355|  32,244|
| |Calhoun County|    13| 893.287| 29.449|   380| 26111.455| 107.980|  14,553|
| |Hampton County|    13| 676.308| 44.592|   445| 23150.557| 327.006|  19,222|
| |Marion County|    13| 424.047|  0.000|   566| 18462.341| 163.095|  30,657|
| |Oconee County|    11| 138.285|  7.184|   847| 10647.927| 136.489|  79,546|
| |Newberry County|    10| 260.146|  3.716|   873| 22710.718| 211.833|  38,440|
| |Abbeville County|     9| 366.943|  5.824|   354| 14433.074| 291.224|  24,527|
| |Saluda County|     9| 439.603|  6.978|   468| 22859.376| 258.180|  20,473|
| |Barnwell County|     7| 335.474| 13.693|   433| 20751.462| 369.706|  20,866|
| |Edgefield County|     7| 256.787|  5.241|   341| 12509.171| 230.584|  27,260|
| |Allendale County|     5| 575.506| 32.886|   231| 26588.398| 575.506|   8,688|
| |Union County|     4| 146.434|  5.230|   378| 13838.044| 177.813|  27,316|
| |Marlboro County|     4| 153.151|  0.000|   517| 19794.778| 311.772|  26,118|
| |McCormick County|     2| 211.349|  0.000|   127| 13420.691| 286.831|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,989| 668.313| N/A|69,374| 23309.989| N/A|2,976,149|
| |Hinds County|   121| 521.912|  5.546| 5,768| 24879.227| 216.898| 231,840|
| |Neshoba County|    94| 3228.244| 19.625| 1,306| 44851.982| 206.058|  29,118|
| |Lauderdale County|    93| 1254.637|  5.782| 1,439| 19413.153| 115.635|  74,125|
| |Madison County|    72| 677.507| 16.131| 2,489| 23421.033| 169.377| 106,272|
| |Leflore County|    68| 2412.802| 35.482|   959| 34027.605| 390.306|  28,183|
| |Jones County|    62| 910.453| 10.489| 1,947| 28591.148| 249.640|  68,098|
| |Forrest County|    57| 761.045|  3.815| 1,858| 24807.402| 299.459|  74,897|
| |Monroe County|    55| 1560.195| 16.210|   831| 23573.131| 405.245|  35,252|
| |Holmes County|    49| 2880.658|  8.398|   923| 54262.199| 537.499|  17,010|
| |Jackson County|    45| 313.333|  3.979| 2,391| 16648.447| 233.757| 143,617|
| |Washington County|    44| 1002.072| 29.281| 1,722| 39217.472| 566.106|  43,909|
| |Lincoln County|    43| 1259.040|  8.366|   846| 24770.884| 246.789|  34,153|
| |Lee County|    42| 491.596| 16.721| 1,563| 18294.396| 444.777|  85,436|
| |Lowndes County|    40| 682.652| 17.066| 1,102| 18807.065| 192.605|  58,595|
| |Pearl River County|    40| 720.266|  7.717|   567| 10209.778| 133.764|  55,535|
| |Oktibbeha County|    39| 786.496|  5.762| 1,136| 22909.230| 169.975|  49,587|
| |Rankin County|    38| 244.733|  6.440| 2,322| 14954.499| 110.406| 155,271|
| |Pike County|    37| 941.763| 14.545|   951| 24205.864| 327.254|  39,288|
| |Bolivar County|    36| 1175.395| 18.657| 1,156| 37743.241| 680.983|  30,628|
| |Harrison County|    36| 173.010|  0.687| 2,651| 12740.292| 249.904| 208,080|
| |Warren County|    35| 771.248| 12.592| 1,137| 25054.538| 447.009|  45,381|
| |Simpson County|    31| 1162.878|  5.359|   821| 30797.509| 289.380|  26,658|
| |DeSoto County|    31| 167.617|  3.090| 3,753| 20292.519| 217.053| 184,945|
| |Tate County|    30| 1059.285| 15.133|   746| 26340.878| 317.785|  28,321|
| |Copiah County|    28| 997.684|  0.000|   971| 34598.254| 213.789|  28,065|
| |Clarke County|    28| 1801.686| 27.577|   343| 22070.652| 193.038|  15,541|
| |Sunflower County|    27| 1075.269| 22.757| 1,071| 42652.330| 733.914|  25,110|
| |Leake County|    27| 1184.938| 12.539|   799| 35065.391| 144.199|  22,786|
| |Grenada County|    26| 1252.529| 34.410|   856| 41237.113| 254.635|  20,758|
| |Adams County|    26| 847.099|  4.654|   642| 20916.821| 214.102|  30,693|
| |Attala County|    25| 1375.592|  7.861|   533| 29327.611| 180.792|  18,174|
| |Walthall County|    21| 1469.971| 20.000|   511| 35769.285| 289.994|  14,286|
| |Wayne County|    21| 1040.480|  0.000|   789| 39092.305| 283.124|  20,183|
| |Marion County|    21| 854.597| 11.627|   689| 28038.904| 319.747|  24,573|
| |Scott County|    20| 711.136|  0.000| 1,017| 36161.286| 198.102|  28,124|
| |Lafayette County|    20| 370.240| 15.867| 1,018| 18845.221| 293.548|  54,019|
| |Chickasaw County|    19| 1110.916|  0.000|   488| 28533.006| 417.638|  17,103|
| |Union County|    17| 589.971|  9.915|   700| 24292.903| 733.745|  28,815|
| |Panola County|    17| 497.192| 20.890| 1,091| 31908.049| 547.329|  34,192|
| |Winston County|    16| 891.117|  7.956|   635| 35366.193| 334.169|  17,955|
| |Lamar County|    15| 236.806|  4.511| 1,241| 19591.747| 144.339|  63,343|
| |Covington County|    15| 804.894| 15.331|   637| 34181.155| 260.632|  18,636|
| |Hancock County|    15| 314.914|  2.999|   409|  8586.664| 179.951|  47,632|
| |Claiborne County|    14| 1557.632| 15.894|   409| 45505.118| 158.942|   8,988|
| |Kemper County|    14| 1437.077|  0.000|   240| 24635.598| 190.633|   9,742|
| |Tippah County|    14| 635.930|  6.489|   388| 17624.347| 441.258|  22,015|
| |Clay County|    14| 724.788|  0.000|   404| 20915.303| 177.499|  19,316|
| |Webster County|    13| 1341.728| 14.744|   248| 25596.037| 545.538|   9,689|
| |Wilkinson County|    13| 1506.373|  0.000|   220| 25492.468| 446.946|   8,630|
| |Greene County|    13| 956.867| 21.030|   262| 19284.558| 336.481|  13,586|
| |Yazoo County|    13| 437.858|  4.812|   870| 29302.796| 322.379|  29,690|
| |Coahoma County|    13| 587.597| 19.371|   789| 35662.629| 677.997|  22,124|
| |Smith County|    13| 816.788|  0.000|   412| 25885.901| 206.441|  15,916|
| |Humphreys County|    12| 1488.095| 17.715|   299| 37078.373| 318.878|   8,064|
| |Noxubee County|    12| 1151.963| 13.714|   463| 44446.578| 342.846|  10,417|
| |Carroll County|    11| 1105.861|  0.000|   262| 26339.600| 201.066|   9,947|
| |Newton County|    11| 523.361|  0.000|   555| 26405.938| 169.922|  21,018|
| |Tallahatchie County|    11| 796.582| 10.345|   547| 39611.847| 362.083|  13,809|
| |Yalobusha County|    10| 825.900|  0.000|   318| 26263.627| 165.180|  12,108|
| |Prentiss County|    10| 397.994|  5.686|   441| 17551.540| 409.365|  25,126|
| |Itawamba County|    10| 427.533|  0.000|   395| 16887.559| 439.748|  23,390|
| |Jasper County|     9| 549.350|  0.000|   408| 24903.864| 252.875|  16,383|
| |Pontotoc County|     9| 279.729|  4.440|   857| 26636.414| 341.891|  32,174|
| |Tishomingo County|     9| 464.324| 29.481|   444| 22906.671| 737.023|  19,383|
| |Calhoun County|     9| 626.697|  0.000|   426| 29663.672| 338.218|  14,361|
| |Marshall County|     9| 255.001|  0.000|   729| 20655.069| 457.382|  35,294|
| |Perry County|     8| 668.170| 11.932|   248| 20713.272| 334.085|  11,973|
| |George County|     8| 326.531| 23.324|   603| 24612.245| 338.192|  24,500|
| |Lawrence County|     8| 635.627| 11.350|   329| 26140.156| 306.463|  12,586|
| |Tunica County|     7| 726.744| 14.832|   365| 37894.518| 860.228|   9,632|
| |Jefferson County|     7| 1001.431| 20.437|   196| 28040.057| 61.312|   6,990|
| |Montgomery County|     6| 613.811| 43.844|   345| 35294.118| 628.425|   9,775|
| |Jefferson Davis County|     6| 539.180|  0.000|   240| 21567.218| 192.564|  11,128|
| |Amite County|     6| 487.924|  0.000|   240| 19516.955| 267.196|  12,297|
| |Stone County|     5| 272.688| 15.582|   224| 12216.405| 498.629|  18,336|
| |Alcorn County|     5| 135.307|  0.000|   439| 11879.956| 239.687|  36,953|
| |Sharkey County|     5| 1157.140| 66.122|   206| 47674.150| 495.917|   4,321|
| |Choctaw County|     4| 487.211|  0.000|   138| 16808.770| 156.603|   8,210|
| |Franklin County|     2| 259.302|  0.000|   135| 17502.917| 370.432|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    27| 20346.647| 322.963|   1,327|
| |Benton County|     1| 121.080| 17.297|   154| 18646.325| 449.726|   8,259|
| |Quitman County|     1| 147.232|  0.000|   275| 40488.810| 778.226|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,875| 325.592| N/A|51,737|  8984.090| N/A|5,758,736|
| |Denver County|   417| 573.424| N/A|10,370| 14259.960| N/A| 727,211|
| |Arapahoe County|   363| 552.856|  0.000| 7,405| 11277.966| 54.176| 656,590|
| |Jefferson County|   233| 399.739|  1.471| 4,289|  7358.277| 58.331| 582,881|
| |Adams County|   176| 340.149|  0.276| 6,621| 12796.156| 102.983| 517,421|
| |Weld County|   145| 446.852|  1.321| 3,754| 11568.852| 60.314| 324,492|
| |El Paso County|   140| 194.336|  0.595| 5,229|  7258.437| 94.193| 720,403|
| |Boulder County|    76| 232.989|  0.438| 2,098|  6431.716| 50.802| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,765|  5026.285| 30.918| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   687| 23634.237| 29.488|  29,068|
| |Larimer County|    37| 103.671|  0.801| 1,605|  4497.071| 59.641| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   711|  4221.489| 55.981| 168,424|
| |Broomfield County|    32| 454.126| N/A|   482|  6840.275| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   306| 15032.423| 98.251|  20,356|
| |Montrose County|    13| 304.037|  0.000|   313|  7320.268| 86.868|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,133| 20552.542| 95.882|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   232| 14291.875| 70.403|  16,233|
| |Routt County|     8| 312.037| 11.144|   124|  4836.571| 78.009|  25,638|
| |Gunnison County|     7| 400.870|  8.181|   275| 15748.482| 73.629|  17,462|
| |Otero County|     6| 328.263|  0.000|    78|  4267.425| 101.605|  18,278|
| |Logan County|     5| 223.125|  0.000|   655| 29229.328| 38.250|  22,409|
| |Montezuma County|     4| 152.771|  0.000|   113|  4315.777| 27.281|  26,183|
| |Summit County|     4| 128.986|  0.000|   344| 11092.838| 78.313|  31,011|
| |Mesa County|     4| 25.939|  0.926|   343|  2224.240| 58.362| 154,210|
| |Garfield County|     4| 66.599|  0.000|   776| 12920.198| 80.870|  60,061|
| |Kit Carson County|     3| 422.714|  0.000|    66|  9299.704| 462.972|   7,097|
| |Teller County|     3| 118.166|  0.000|   137|  5396.250| 90.031|  25,388|
| |Pitkin County|     2| 112.568|  0.000|   190| 10693.983| 80.406|  17,767|
| |Rio Grande County|     2| 177.510|  0.000|    91|  8076.684| 38.038|  11,267|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |La Plata County|     2| 35.574|  0.000|   225|  4002.063| 60.984|  56,221|
| |Elbert County|     2| 74.825|  0.000|   108|  4040.555| 58.791|  26,729|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 64.529|  13,283|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Delta County|     1| 32.090|  0.000|   129|  4139.657| 64.181|  31,162|
| |Crowley County|     1| 164.989|  0.000|    73| 12044.217| 23.570|   6,061|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 29.455|   9,700|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 20.713|   6,897|
| |Grand County|     1| 63.557|  0.000|    53|  3368.501| 81.716|  15,734|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Gilpin County|     0|  0.000|  0.000|    17|  2723.050| 22.883|   6,243|
| |Fremont County|     0|  0.000|  0.000|   131|  2738.352| 41.807|  47,839|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481|  0.000|   5,068|
| |Costilla County|     0|  0.000|  0.000|    23|  5917.160| 36.753|   3,887|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 25.615|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    38|  2708.675| 40.732|  14,029|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Lake County|     0|  0.000|  0.000|    80|  9843.731| 105.469|   8,127|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 25.058|   5,701|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053|  0.000|  10,019|
| |Washington County|     0|  0.000|  0.000|    49|  9983.700| 58.214|   4,908|
| |San Miguel County|     0|  0.000|  0.000|    91| 11126.055| 192.130|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 271.076|   6,324|
| |Prowers County|     0|  0.000|  0.000|    58|  4765.035| 93.892|  12,172|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866| 29.544|  14,506|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,814| 369.964| N/A|100,801| 20558.270| N/A|4,903,185|
| |Jefferson County|   261| 396.311|  6.724|13,463| 20442.684| 277.006| 658,573|
| |Mobile County|   216| 522.737|  4.149|10,671| 25824.641| 484.707| 413,210|
| |Montgomery County|   153| 675.538|  3.154| 6,955| 30708.300| 381.607| 226,486|
| |Tuscaloosa County|    80| 382.126|  7.506| 4,327| 20668.243| 221.770| 209,355|
| |Tallapoosa County|    79| 1957.044|  3.539|   876| 21700.894| 173.409|  40,367|
| |Walker County|    65| 1023.284|  2.249| 1,548| 24369.893| 155.179|  63,521|
| |Lee County|    47| 285.641|  4.341| 2,724| 16555.044| 147.596| 164,542|
| |Elmore County|    39| 480.242|  3.518| 1,767| 21758.672| 235.723|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   848| 25500.692| 68.735|  33,254|
| |Marshall County|    38| 392.667|  5.905| 3,199| 33056.399| 292.286|  96,774|
| |Shelby County|    37| 169.957|  3.281| 3,361| 15438.535| 158.802| 217,702|
| |Butler County|    36| 1851.090|  7.346|   773| 39747.018| 139.566|  19,448|
| |Madison County|    35| 93.857|  3.065| 5,510| 14775.723| 148.638| 372,909|
| |Etowah County|    34| 332.460|  8.381| 2,190| 21414.323| 311.506| 102,268|
| |Dale County|    29| 589.767| 17.432|   850| 17286.260| 151.073|  49,172|
| |Baldwin County|    29| 129.909|  3.840| 3,710| 16619.332| 248.298| 223,234|
| |Hale County|    26| 1774.623|  0.000|   488| 33308.307| 282.770|  14,651|
| |Marion County|    26| 875.156|  9.617|   587| 19758.322| 192.342|  29,709|
| |Dallas County|    25| 672.115|  7.681| 1,347| 36213.571| 188.192|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   575| 59119.885| 205.634|   9,726|
| |Franklin County|    22| 701.486|  9.110| 1,308| 41706.524| 423.625|  31,362|
| |Autauga County|    22| 393.778|  2.557| 1,188| 21264.028| 404.006|  55,869|
| |Covington County|    21| 566.817|  3.856|   746| 20135.496| 115.677|  37,049|
| |St. Clair County|    20| 223.434|  9.576| 1,375| 15361.069| 196.302|  89,512|
| |Lauderdale County|    20| 215.682| 10.784| 1,203| 12973.288| 141.734|  92,729|
| |Morgan County|    20| 167.114|  5.968| 2,425| 20262.536| 185.019| 119,679|
| |Calhoun County|    19| 167.246|  7.545| 1,828| 16090.841| 252.755| 113,605|
| |Colbert County|    18| 325.845| 12.930| 1,225| 22175.558| 266.365|  55,241|
| |Sumter County|    18| 1448.459|  0.000|   366| 29452.000| 68.974|  12,427|
| |Marengo County|    17| 901.235| 22.720|   568| 30111.859| 295.363|  18,863|
| |Escambia County|    17| 464.062|  7.799| 1,094| 29863.784| 440.664|  36,633|
| |DeKalb County|    14| 195.769|  1.998| 1,852| 25897.389| 261.691|  71,513|
| |Talladega County|    14| 175.048|  1.786| 1,069| 13366.176| 219.703|  79,978|
| |Macon County|    14| 774.851|  7.907|   341| 18873.146| 197.666|  18,068|
| |Limestone County|    13| 131.426|  0.000| 1,378| 13931.153| 218.080|  98,915|
| |Washington County|    13| 796.276|  8.750|   449| 27502.144| 1172.538|  16,326|
| |Houston County|    13| 122.778|  1.349| 1,450| 13694.490| 156.508| 105,882|
| |Choctaw County|    12| 953.213|  0.000|   289| 22956.549| 147.521|  12,589|
| |Cullman County|    12| 143.253|  0.000| 1,238| 14778.913| 114.261|  83,768|
| |Randolph County|    11| 484.112|  6.287|   403| 17736.115| 69.159|  22,722|
| |Bullock County|    11| 1089.001|  0.000|   492| 48708.049| 678.858|  10,101|
| |Greene County|    11| 1356.183|  0.000|   253| 31192.208| 105.677|   8,111|
| |Winston County|    11| 465.530|  0.000|   457| 19340.641| 133.008|  23,629|
| |Conecuh County|    10| 828.706|  0.000|   394| 32651.032| 248.612|  12,067|
| |Clarke County|    10| 423.334|  6.048|   821| 34755.736| 1995.718|  23,622|
| |Pickens County|    10| 501.756|  7.168|   411| 20622.178| 250.878|  19,930|
| |Wilcox County|    10| 964.041|  0.000|   436| 42032.199| 344.300|  10,373|
| |Chilton County|     9| 202.575|  9.646|   827| 18614.387| 286.177|  44,428|
| |Cherokee County|     8| 305.390|  5.453|   279| 10650.481| 163.602|  26,196|
| |Crenshaw County|     8| 580.889| 51.865|   331| 24034.272| 248.952|  13,772|
| |Pike County|     7| 211.391|  0.000|   716| 21622.275| 189.820|  33,114|
| |Coffee County|     6| 114.631|  2.729|   779| 14882.886| 147.382|  52,342|
| |Monroe County|     6| 289.394| 13.781|   424| 20450.490| 192.929|  20,733|
| |Barbour County|     6| 243.053|  5.787|   581| 23535.607| 98.378|  24,686|
| |Fayette County|     5| 306.711|  0.000|   223| 13679.303| 394.342|  16,302|
| |Blount County|     5| 86.466|  4.941|   825| 14266.939| 197.637|  57,826|
| |Clay County|     5| 377.786|  0.000|   277| 20929.354| 561.282|  13,235|
| |Bibb County|     5| 223.274|  6.379|   453| 20228.633| 440.169|  22,394|
| |Jackson County|     4| 77.480|  0.000| 1,072| 20764.731| 503.622|  51,626|
| |Perry County|     4| 448.280|  0.000|   446| 49983.190| 224.140|   8,923|
| |Lawrence County|     3| 91.119|  8.678|   356| 10812.781| 134.509|  32,924|
| |Coosa County|     3| 281.347| 13.397|   105|  9847.135| 133.975|  10,663|
| |Henry County|     3| 174.368|  0.000|   264| 15344.377| 141.155|  17,205|
| |Geneva County|     2| 76.130| 10.876|   265| 10087.168| 119.632|  26,271|
| |Lamar County|     2| 144.875|  0.000|   230| 16660.630| 258.705|  13,805|
| |Russell County|     2| 34.506|  0.000| 1,391| 23998.896| 305.624|  57,961|
| |Cleburne County|     1| 67.069|  0.000|   129|  8651.911| 76.650|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,722| 226.136| N/A|64,498|  8469.981| N/A|7,614,893|
| |King County|   684| 303.625|  1.585|16,941|  7520.035| 68.233|2,252,782|
| |Yakima County|   215| 857.007|  2.847|10,412| 41503.071| 153.749| 250,873|
| |Snohomish County|   197| 239.635|  1.216| 5,582|  6790.069| 55.782| 822,083|
| |Pierce County|   143| 158.015|  2.210| 5,874|  6490.751| 83.033| 904,980|
| |Benton County|   119| 582.220|  5.592| 3,787| 18528.304| 121.616| 204,390|
| |Spokane County|    93| 177.889|  5.738| 4,602|  8802.635| 140.453| 522,798|
| |Franklin County|    51| 535.591|  6.001| 3,577| 37564.848| 280.547|  95,222|
| |Clark County|    45| 92.168|  0.878| 1,849|  3787.064| 42.134| 488,241|
| |Whatcom County|    39| 170.122|  0.623| 1,000|  4362.107| 26.796| 229,247|
| |Skagit County|    21| 162.532|  0.000|   904|  6996.633| 60.811| 129,205|
| |Kittitas County|    20| 417.232|  5.960|   412|  8594.972| 172.853|  47,935|
| |Grant County|    13| 133.015|  1.462| 1,584| 16207.422| 366.889|  97,733|
| |Thurston County|    11| 37.861|  0.492|   752|  2588.320| 45.728| 290,536|
| |Island County|    11| 129.197|  0.000|   249|  2924.560| 13.423|  85,141|
| |Chelan County|    10| 129.534|  0.000| 1,405| 18199.482| 334.937|  77,200|
| |Kitsap County|     7| 25.785|  1.579|   768|  2829.011| 41.046| 271,473|
| |Douglas County|     7| 161.183|  0.000|   976| 22473.462| 355.260|  43,429|
| |Adams County|     5| 250.213|  7.149|   457| 22869.439| 357.447|  19,983|
| |Cowlitz County|     5| 45.211|  0.000|   496|  4484.913| 54.253| 110,593|
| |Okanogan County|     5| 118.363| 10.145|   881| 20855.526| 290.834|  42,243|
| |Lewis County|     4| 49.562|  1.770|   231|  2862.205| 65.493|  80,707|
| |Grays Harbor County|     3| 39.967|  1.903|   125|  1665.312| 30.451|  75,061|
| |Klickitat County|     3| 133.779|  0.000|   119|  5306.577| 70.075|  22,425|
| |Walla Walla County|     3| 49.375|  0.000|   564|  9282.423| 221.010|  60,760|
| |Asotin County|     2| 88.566|  0.000|    28|  1239.926| 25.305|  22,582|
| |Pacific County|     2| 89.004|  0.000|    55|  2447.599| 69.931|  22,471|
| |Stevens County|     1| 21.871|  0.000|   112|  2449.533| 49.990|  45,723|
| |Mason County|     1| 14.977|  0.000|   242|  3624.491| 130.516|  66,768|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 11.823|  12,083|
| |Clallam County|     0|  0.000|  0.000|   142|  1836.262| 81.283|  77,331|
| |San Juan County|     0|  0.000|  0.000|    30|  1706.291| 16.250|  17,582|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489|  0.000|   7,627|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Jefferson County|     0|  0.000|  0.000|    55|  1706.961|  4.434|  32,221|
| |Lincoln County|     0|  0.000|  0.000|    27|  2468.233| 104.475|  10,939|
| |Whitman County|     0|  0.000|  0.000|   113|  2255.309| 74.132|  50,104|
| |Pend Oreille County|     0|  0.000|  0.000|    46|  3351.792| 72.865|  13,724|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,678| 297.537| N/A|62,170| 11023.769| N/A|5,639,632|
| |Hennepin County|   840| 663.589|  1.693|19,677| 15544.582| 144.906|1,265,843|
| |Ramsey County|   269| 488.806|  2.077| 7,775| 14128.118| 167.435| 550,321|
| |Anoka County|   115| 322.200|  0.800| 3,792| 10624.200| 134.484| 356,921|
| |Dakota County|   106| 247.074|  0.666| 4,558| 10624.189| 148.511| 429,021|
| |Washington County|    47| 179.089|  2.177| 2,192|  8352.385| 116.489| 262,440|
| |Clay County|    40| 622.840|  0.000|   792| 12332.223| 75.631|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,781| 11251.287| 119.128| 158,293|
| |Scott County|    22| 147.638|  3.835| 1,608| 10791.005| 162.018| 149,013|
| |Stearns County|    20| 124.166|  0.000| 2,913| 18084.743| 58.535| 161,075|
| |St. Louis County|    20| 100.467|  0.718|   600|  3014.015| 89.703| 199,070|
| |Winona County|    16| 316.932|  0.000|   265|  5249.188| 36.787|  50,484|
| |Crow Wing County|    14| 215.203|  0.000|   246|  3781.416| 54.899|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   351| 10240.999| 120.875|  34,274|
| |Itasca County|    12| 265.899|  0.000|   146|  3235.099| 34.820|  45,130|
| |Sherburne County|    10| 102.840|  4.407|   737|  7579.341| 102.840|  97,238|
| |Pipestone County|     9| 986.193|  0.000|   158| 17313.171| 219.154|   9,126|
| |Goodhue County|     9| 194.217|  3.083|   202|  4359.085| 58.573|  46,340|
| |Rice County|     8| 119.453|  0.000| 1,042| 15558.741| 76.791|  66,972|
| |Nobles County|     6| 277.405|  0.000| 1,773| 81973.277| 145.308|  21,629|
| |Blue Earth County|     5| 73.907|  0.000|   941| 13909.213| 160.483|  67,653|
| |Wright County|     5| 36.133|  0.000|   903|  6525.651| 78.461| 138,377|
| |Renville County|     5| 343.690|  0.000|    67|  4605.444| 68.738|  14,548|
| |Martin County|     5| 254.026|  0.000|   209| 10618.300| 36.289|  19,683|
| |Polk County|     4| 127.535|  4.555|   156|  4973.855| 77.432|  31,364|
| |Carver County|     3| 28.547|  1.359|   890|  8469.012| 115.548| 105,089|
| |Wilkin County|     3| 483.325|  0.000|    35|  5638.795| 92.062|   6,207|
| |Lyon County|     3| 117.767|  0.000|   425| 16683.677| 28.040|  25,474|
| |Koochiching County|     3| 245.319|  0.000|    80|  6541.827| 70.091|  12,229|
| |Otter Tail County|     3| 51.067|  0.000|   198|  3370.442| 38.908|  58,746|
| |Grant County|     3| 502.344| 47.842|    56|  9377.093| 95.685|   5,972|
| |Benton County|     3| 73.369|  0.000|   323|  7899.435| 34.938|  40,889|
| |Mille Lacs County|     3| 114.168|  0.000|    72|  2740.039| 16.310|  26,277|
| |Todd County|     2| 81.090|  0.000|   429| 17393.772| 46.337|  24,664|
| |Sibley County|     2| 134.544|  0.000|    84|  5650.858| 38.441|  14,865|
| |Steele County|     2| 54.572|  3.898|   351|  9577.342| 66.266|  36,649|
| |Douglas County|     2| 52.437|  7.491|   144|  3775.465| 29.964|  38,141|
| |Kanabec County|     2| 122.421|  8.744|    37|  2264.798| 61.211|  16,337|
| |Mower County|     2| 49.923|  0.000| 1,107| 27632.170| 67.752|  40,062|
| |Meeker County|     2| 86.125|  0.000|    87|  3746.447| 12.304|  23,222|
| |Brown County|     2| 79.974|  0.000|    89|  3558.861| 22.850|  25,008|
| |Cass County|     2| 67.161|  0.000|    76|  2552.134| 47.972|  29,779|
| |Watonwan County|     1| 91.768| 13.110|   328| 30100.028| 367.074|  10,897|
| |Murray County|     1| 122.041|  0.000|   124| 15133.024| 34.869|   8,194|
| |Swift County|     1| 107.921|  0.000|    55|  5935.679| 46.252|   9,266|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 20.236|  14,119|
| |Morrison County|     1| 29.953|  0.000|    93|  2785.599| 47.068|  33,386|
| |Aitkin County|     1| 62.949|  0.000|    40|  2517.940| 98.919|  15,886|
| |Kandiyohi County|     1| 23.149|  0.000|   705| 16319.822| 79.367|  43,199|
| |Freeborn County|     1| 33.024|  0.000|   360| 11888.643| 18.871|  30,281|
| |Le Sueur County|     1| 34.618|  0.000|   230|  7962.059| 133.525|  28,887|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 51.694|   5,527|
| |Chippewa County|     1| 84.746|  0.000|   109|  9237.288| 96.852|  11,800|
| |Chisago County|     1| 17.674|  0.000|   207|  3658.601| 58.073|  56,579|
| |Becker County|     1| 29.050|  0.000|   161|  4677.105| 53.951|  34,423|
| |Traverse County|     0|  0.000|  0.000|    11|  3375.268| 43.835|   3,259|
| |Rock County|     0|  0.000|  0.000|    85|  9125.067| 153.362|   9,315|
| |Roseau County|     0|  0.000|  0.000|    53|  3494.890| 65.941|  15,165|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 29.140|   9,805|
| |Wabasha County|     0|  0.000|  0.000|    92|  4253.942| 52.844|  21,627|
| |Wadena County|     0|  0.000|  0.000|    27|  1973.396| 31.324|  13,682|
| |Yellow Medicine County|     0|  0.000|  0.000|    52|  5355.855| 29.428|   9,709|
| |Waseca County|     0|  0.000|  0.000|   149|  8005.588| 122.809|  18,612|
| |Cottonwood County|     0|  0.000|  0.000|   177| 15809.218| 51.039|  11,196|
| |Carlton County|     0|  0.000|  0.000|   145|  4042.263| 59.738|  35,871|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Lake County|     0|  0.000|  0.000|    22|  2067.475| 53.701|  10,641|
| |Lac qui Parle County|     0|  0.000|  0.000|     8|  1207.912| 43.140|   6,623|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    79|  8023.563| 116.073|   9,846|
| |Isanti County|     0|  0.000|  0.000|   131|  3226.919| 59.823|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    35|  1628.589| 33.237|  21,491|
| |Houston County|     0|  0.000|  0.000|    44|  2365.591| 30.722|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    71|  3370.200| 67.811|  21,067|
| |Lincoln County|     0|  0.000|  0.000|    59| 10462.848| 126.669|   5,639|
| |Lake of the Woods County|     0|  0.000|  0.000|     4|  1069.519| 114.591|   3,740|
| |McLeod County|     0|  0.000|  0.000|   208|  5795.002| 250.745|  35,893|
| |Beltrami County|     0|  0.000|  0.000|   249|  5276.765| 127.151|  47,188|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255|  0.000|   9,336|
| |Cook County|     0|  0.000|  0.000|     5|   915.248| 78.450|   5,463|
| |Dodge County|     0|  0.000|  0.000|   131|  6257.762| 40.945|  20,934|
| |Faribault County|     0|  0.000|  0.000|    89|  6518.714| 62.781|  13,653|
| |Redwood County|     0|  0.000|  0.000|    36|  2373.105| 37.668|  15,170|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 105.690|   4,055|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 25.399|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202|  4.830|  29,579|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510| 67.227|   6,375|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,289| 210.023| N/A|55,879|  9104.628| N/A|6,137,428|
| |St. Louis County|   850| 854.954|  3.880|20,849| 20970.524| 275.597| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,316| 10735.731| 168.434| 402,022|
| |Jackson County|    66| 93.882|  1.016| 4,272|  6076.719| 113.593| 703,011|
| |Jasper County|    31| 255.506|  4.710| 1,838| 15149.018| 169.552| 121,328|
| |Jefferson County|    26| 115.514|  1.269| 1,730|  7686.122| 154.865| 225,081|
| |Clay County|    22| 88.018|  1.143| 1,087|  4348.905| 64.585| 249,948|
| |Franklin County|    18| 173.132|  0.000|   669|  6434.734| 141.528| 103,967|
| |Scott County|    13| 339.603|  0.000|   421| 10997.910| 235.110|  38,280|
| |Platte County|    10| 95.769|  0.000|   385|  3687.104| 72.511| 104,418|
| |Greene County|    10| 34.120|  0.000| 1,686|  5752.578| 163.774| 293,086|
| |Buchanan County|    10| 114.464|  0.000| 1,106| 12659.677| 60.502|  87,364|
| |Gentry County|     9| 1369.655|  0.000|    85| 12935.626| 65.222|   6,571|
| |Pemiscot County|     9| 569.440|  0.000|   243| 15374.881| 153.658|  15,805|
| |Cass County|     9| 85.082|  0.000|   785|  7421.063| 143.154| 105,780|
| |Stoddard County|     9| 310.078|  0.000|   236|  8130.922| 103.359|  29,025|
| |McDonald County|     8| 350.309|  6.256|   953| 41730.525| 68.811|  22,837|
| |Saline County|     7| 307.544|  0.000|   459| 20166.074| 238.503|  22,761|
| |Newton County|     6| 103.029|  0.000|   916| 15729.102| 203.605|  58,236|
| |Camden County|     6| 129.576|  3.085|   370|  7990.498| 135.746|  46,305|
| |Cape Girardeau County|     5| 63.395|  0.000|   689|  8735.784| 135.846|  78,871|
| |Barry County|     4| 111.766|  7.983|   266|  7432.451| 95.800|  35,789|
| |Pettis County|     4| 94.476|  3.374|   580| 13698.954| 425.140|  42,339|
| |Dunklin County|     4| 137.311|  0.000|   336| 11534.105| 294.237|  29,131|
| |Perry County|     4| 209.030|  0.000|   244| 12750.836| 223.961|  19,136|
| |New Madrid County|     3| 175.685| 16.732|   269| 15753.104| 535.421|  17,076|
| |Taney County|     3| 53.640|  0.000|   658| 11765.127| 385.700|  55,928|
| |Johnson County|     3| 55.492|  2.642|   499|  9230.143| 66.062|  54,062|
| |Boone County|     3| 16.624|  0.000| 1,457|  8073.677| 137.741| 180,463|
| |Cole County|     3| 39.090|  0.000|   460|  5993.876| 197.314|  76,745|
| |Henry County|     3| 137.463|  0.000|    89|  4078.079| 104.734|  21,824|
| |Moniteau County|     2| 123.977|  0.000|   155|  9608.232| 168.255|  16,132|
| |Lawrence County|     2| 52.144|  0.000|   240|  6257.333| 141.535|  38,355|
| |St. Francois County|     2| 29.755|  0.000|   421|  6263.483| 184.908|  67,215|
| |Douglas County|     2| 151.688|  0.000|    89|  6750.095| 65.009|  13,185|
| |Howell County|     2| 49.854|  0.000|   159|  3963.407| 56.976|  40,117|
| |Lafayette County|     2| 61.147|  0.000|   183|  5594.961| 74.250|  32,708|
| |Butler County|     2| 47.083|  0.000|   289|  6803.522| 121.071|  42,478|
| |Osage County|     1| 73.448|  0.000|    53|  3892.765| 73.448|  13,615|
| |Pike County|     1| 54.639|  0.000|   120|  6556.660| 320.027|  18,302|
| |Pulaski County|     1| 19.009|  0.000|   249|  4733.210| 154.787|  52,607|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313|  0.000|   4,696|
| |Randolph County|     1| 40.407|  0.000|    74|  2990.141| 80.815|  24,748|
| |Ste. Genevieve County|     1| 55.885|  0.000|    62|  3464.849| 87.819|  17,894|
| |Scotland County|     1| 203.998|  0.000|    15|  3059.976| 29.143|   4,902|
| |Shannon County|     1| 122.459|  0.000|    44|  5388.195|  0.000|   8,166|
| |Stone County|     1| 31.297|  0.000|   150|  4694.542| 196.724|  31,952|
| |Washington County|     1| 40.437|  0.000|    94|  3801.051| 161.747|  24,730|
| |Webster County|     1| 25.258|  0.000|   140|  3536.068| 54.123|  39,592|
| |Carter County|     1| 167.168|  0.000|    21|  3510.532| 23.881|   5,982|
| |DeKalb County|     1| 79.700|  0.000|    38|  3028.612| 34.157|  12,547|
| |Dallas County|     1| 59.249|  0.000|    68|  4028.913| 126.962|  16,878|
| |Christian County|     1| 11.287|  0.000|   392|  4424.629| 130.610|  88,595|
| |Andrew County|     1| 56.459|  0.000|    89|  5024.842| 16.131|  17,712|
| |Lincoln County|     1| 16.945|  0.000|   412|  6981.513| 167.033|  59,013|
| |Audrain County|     1| 39.389|  0.000|   207|  8153.458| 50.643|  25,388|
| |Callaway County|     1| 22.350|  0.000|   163|  3643.028| 95.785|  44,743|
| |Bates County|     1| 61.835|  0.000|    51|  3153.599| 79.502|  16,172|
| |Bollinger County|     1| 82.420| 11.774|    75|  6181.489| 188.388|  12,133|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Miller County|     1| 39.034|  5.576|   137|  5347.594| 156.134|  25,619|
| |Marion County|     1| 35.051|  0.000|   223|  7816.334| 295.428|  28,530|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131|  0.000|   9,020|
| |Grundy County|     1| 101.523|  0.000|    29|  2944.162| 58.013|   9,850|
| |Linn County|     1| 83.893|  0.000|    35|  2936.242| 47.939|  11,920|
| |Lewis County|     1| 102.291|  0.000|    50|  5114.566| 219.196|   9,776|
| |Laclede County|     1| 27.993|  0.000|   209|  5850.572| 47.988|  35,723|
| |Benton County|     1| 51.432|  0.000|   113|  5811.860| 257.162|  19,443|
| |Howard County|     0|  0.000|  0.000|    55|  5499.450| 114.274|  10,001|
| |Holt County|     0|  0.000|  0.000|    27|  6132.183| 681.354|   4,403|
| |Monroe County|     0|  0.000|  0.000|    33|  3817.677| 148.741|   8,644|
| |Polk County|     0|  0.000|  0.000|   219|  6812.031| 102.203|  32,149|
| |Phelps County|     0|  0.000|  0.000|   100|  2243.511| 67.305|  44,573|
| |Ozark County|     0|  0.000|  0.000|    15|  1635.056| 109.004|   9,174|
| |Oregon County|     0|  0.000|  0.000|    16|  1519.612| 27.136|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   190|  8600.398| 142.262|  22,092|
| |Morgan County|     0|  0.000|  0.000|    87|  4217.773| 90.035|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    42|  3636.049| 12.368|  11,551|
| |Mississippi County|     0|  0.000|  0.000|   148| 11229.135| 162.584|  13,180|
| |Mercer County|     0|  0.000|  0.000|    13|  3594.139| 78.992|   3,617|
| |Maries County|     0|  0.000|  0.000|    24|  2759.572| 98.556|   8,697|
| |Madison County|     0|  0.000|  0.000|    28|  2316.347| 118.181|  12,088|
| |Macon County|     0|  0.000|  0.000|    62|  4101.343| 66.151|  15,117|
| |Livingston County|     0|  0.000|  0.000|    63|  4137.388| 93.818|  15,227|
| |Knox County|     0|  0.000|  0.000|    32|  8082.849| 288.673|   3,959|
| |Iron County|     0|  0.000|  0.000|    22|  2172.840|  0.000|  10,125|
| |Hickory County|     0|  0.000|  0.000|    35|  3667.225| 209.556|   9,544|
| |Gasconade County|     0|  0.000|  0.000|    29|  1971.984| 87.428|  14,706|
| |Crawford County|     0|  0.000|  0.000|    83|  3469.900| 125.418|  23,920|
| |St. Clair County|     0|  0.000|  0.000|    24|  2554.007| 76.012|   9,397|
| |Ripley County|     0|  0.000|  0.000|    58|  4364.840| 118.259|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    42|  4074.110| 235.578|  10,309|
| |Dent County|     0|  0.000|  0.000|    15|   963.206| 55.040|  15,573|
| |Daviess County|     0|  0.000|  0.000|    18|  2174.438| 17.257|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865|  0.000|   7,561|
| |Cooper County|     0|  0.000|  0.000|   140|  7905.585| 266.208|  17,709|
| |Clinton County|     0|  0.000|  0.000|    90|  4414.578| 154.160|  20,387|
| |Clark County|     0|  0.000|  0.000|    23|  3383.846| 168.141|   6,797|
| |Chariton County|     0|  0.000|  0.000|    19|  2558.578| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    41|  2857.342| 49.779|  14,349|
| |Carroll County|     0|  0.000|  0.000|   102| 11752.506| 49.380|   8,679|
| |Barton County|     0|  0.000|  0.000|    70|  5955.419| 48.616|  11,754|
| |Atchison County|     0|  0.000|  0.000|    18|  3499.903| 111.108|   5,143|
| |Adair County|     0|  0.000|  0.000|   174|  6865.801| 174.745|  25,343|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    65|  3554.049| 54.678|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    62|  4816.282| 188.656|  12,873|
| |Warren County|     0|  0.000|  0.000|   212|  5946.871| 108.198|  35,649|
| |Vernon County|     0|  0.000|  0.000|    56|  2723.338| 62.526|  20,563|
| |Texas County|     0|  0.000|  0.000|    60|  2362.391| 84.371|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   147| 24141.895| 187.692|   6,089|
| |Shelby County|     0|  0.000|  0.000|    40|  6745.363| 264.996|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    10|  2145.923| 30.656|   4,660|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867| 55.857|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,268| 185.674| N/A|120,365| 17625.118| N/A|6,829,174|
| |Shelby County|   315| 336.120|  2.591|23,785| 25379.709| 283.682| 937,166|
| |Davidson County|   221| 318.378|  2.675|21,044| 30316.476| 253.550| 694,144|
| |Sumner County|    73| 381.633|  1.494| 3,501| 18302.724| 177.000| 191,283|
| |Rutherford County|    56| 168.530|  1.290| 6,719| 20220.594| 199.914| 332,285|
| |Hamilton County|    55| 149.536|  3.107| 6,408| 17422.323| 234.985| 367,804|
| |Knox County|    40| 85.050|  0.607| 4,852| 10316.534| 202.297| 470,313|
| |Williamson County|    26| 109.055|  2.397| 3,656| 15334.799| 175.566| 238,412|
| |Wilson County|    23| 158.997|  0.000| 2,374| 16411.235| 219.238| 144,657|
| |Madison County|    21| 214.321| 10.206| 1,222| 12471.424| 386.360|  97,984|
| |McMinn County|    20| 371.789|  0.000|   567| 10540.209| 183.239|  53,794|
| |Robertson County|    20| 278.501|  1.989| 1,587| 22099.063| 222.801|  71,813|
| |Putnam County|    18| 224.313|  8.901| 1,840| 22929.778| 345.371|  80,245|
| |Hardeman County|    18| 718.563| 34.217|   968| 38642.715| 712.860|  25,050|
| |Hamblen County|    15| 231.004|  4.400| 1,425| 21945.360| 250.804|  64,934|
| |Sullivan County|    15| 94.728|  3.609| 1,075|  6788.845| 194.869| 158,348|
| |Blount County|    15| 112.707|  7.514| 1,333| 10015.929| 157.790| 133,088|
| |Bradley County|    15| 138.748|  3.964| 2,013| 18619.924| 319.780| 108,110|
| |Montgomery County|    14| 66.988|  0.684| 2,015|  9641.471| 159.951| 208,993|
| |Macon County|    13| 528.412|  0.000|   870| 35362.979| 133.555|  24,602|
| |Giles County|    13| 441.216|  4.849|   391| 13270.432| 150.304|  29,464|
| |Bedford County|    11| 221.270|  0.000|   940| 18908.535| 143.682|  49,713|
| |Hawkins County|    10| 176.100| 12.579|   500|  8804.987| 274.212|  56,786|
| |Tipton County|    10| 162.340|  2.319| 1,217| 19756.814| 185.532|  61,599|
| |Cheatham County|     9| 221.310| 10.539|   607| 14926.107| 186.181|  40,667|
| |Monroe County|     9| 193.361|  0.000|   458|  9839.940| 239.400|  46,545|
| |Sevier County|     9| 91.603|  4.362| 1,916| 19501.272| 222.465|  98,250|
| |Greene County|     9| 130.304|  6.205|   524|  7586.616| 260.609|  69,069|
| |Lauderdale County|     9| 351.110| 11.146|   523| 20403.386| 434.707|  25,633|
| |Dyer County|     8| 215.291|  3.844|   679| 18272.828| 384.448|  37,159|
| |Fayette County|     8| 194.491|  0.000|   718| 17455.571| 250.060|  41,133|
| |Maury County|     8| 82.999|  1.482| 1,299| 13476.921| 284.567|  96,387|
| |Gibson County|     8| 162.823| 17.445|   749| 15244.337| 389.613|  49,133|
| |Hardin County|     8| 311.867|  5.569|   486| 18945.891| 334.143|  25,652|
| |Lawrence County|     7| 158.579|  3.236|   593| 13433.918| 310.686|  44,142|
| |Haywood County|     7| 404.531| 16.511|   522| 30166.436| 891.619|  17,304|
| |Carter County|     6| 106.400|  2.533|   564| 10001.596| 283.733|  56,391|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 88.621|  11,284|
| |McNairy County|     6| 233.518|  5.560|   397| 15451.078| 344.716|  25,694|
| |Cumberland County|     6| 99.141|  0.000|   483|  7980.833| 203.003|  60,520|
| |Anderson County|     6| 77.944|  0.000|   711|  9236.405| 137.331|  76,978|
| |Cocke County|     5| 138.873| 11.903|   485| 13470.725| 253.940|  36,004|
| |Carroll County|     5| 180.070| 10.290|   341| 12280.765| 463.037|  27,767|
| |Crockett County|     5| 351.370| 10.039|   277| 19465.917| 311.214|  14,230|
| |White County|     5| 182.849| 10.449|   310| 11336.625| 407.492|  27,345|
| |Marion County|     5| 172.968|  4.942|   230|  7956.550| 98.839|  28,907|
| |Franklin County|     4| 94.769|  0.000|   343|  8126.422| 159.076|  42,208|
| |Marshall County|     4| 116.364|  4.156|   310|  9018.182| 162.078|  34,375|
| |Jefferson County|     4| 73.401|  2.621|   596| 10936.783| 217.582|  54,495|
| |Warren County|     4| 96.906|  0.000|   545| 13203.479| 314.945|  41,277|
| |Weakley County|     4| 120.019|  4.286|   503| 15092.415| 745.834|  33,328|
| |Smith County|     4| 198.442|  7.087|   461| 22870.467| 481.931|  20,157|
| |Polk County|     4| 237.643|  8.487|   213| 12654.468| 271.592|  16,832|
| |Obion County|     4| 133.027|  0.000|   598| 19887.592| 636.631|  30,069|
| |Decatur County|     3| 257.224| 12.249|   218| 18691.589| 538.945|  11,663|
| |Dickson County|     3| 55.609|  5.296|   718| 13309.112| 233.029|  53,948|
| |Coffee County|     3| 53.079|  2.528|   573| 10138.004| 315.944|  56,520|
| |Humphreys County|     3| 161.447|  0.000|   131|  7049.833| 138.383|  18,582|
| |Loudon County|     3| 55.486|  0.000|   774| 14315.307| 232.511|  54,068|
| |Hancock County|     2| 302.115| 21.580|    82| 12386.707| 129.478|   6,620|
| |Washington County|     2| 15.459|  0.000| 1,352| 10450.242| 262.802| 129,375|
| |Scott County|     2| 90.629| 12.947|   124|  5618.996| 122.996|  22,068|
| |Grundy County|     2| 148.954|  0.000|   122|  9086.170| 191.512|  13,427|
| |Henderson County|     2| 71.131| 10.162|   626| 22264.111| 726.556|  28,117|
| |Wayne County|     2| 119.954|  0.000|   230| 13794.758| 68.545|  16,673|
| |Chester County|     2| 115.627|  0.000|   230| 13297.104| 239.513|  17,297|
| |Rhea County|     2| 60.301|  4.307|   547| 16492.297| 142.138|  33,167|
| |Roane County|     2| 37.466|  0.000|   496|  9291.521| 262.261|  53,382|
| |Bledsoe County|     2| 132.767|  9.483|   717| 47596.920| 407.784|  15,064|
| |Lincoln County|     1| 29.099|  0.000|   320|  9311.529| 253.573|  34,366|
| |Jackson County|     1| 84.846|  0.000|   131| 11114.882| 266.660|  11,786|
| |DeKalb County|     1| 48.804|  0.000|   369| 18008.785| 299.798|  20,490|
| |Campbell County|     1| 25.099|  0.000|   257|  6450.479| 118.325|  39,842|
| |Benton County|     1| 61.881|  0.000|   161|  9962.871| 442.008|  16,160|
| |Morgan County|     1| 46.722|  0.000|   130|  6073.915| 240.287|  21,403|
| |Overton County|     1| 44.962|  0.000|   221|  9936.604| 513.852|  22,241|
| |Lewis County|     1| 81.513|  0.000|    76|  6194.979| 163.026|  12,268|
| |Pickett County|     1| 198.098|  0.000|    40|  7923.930| 367.897|   5,048|
| |Sequatchie County|     1| 66.551|  9.507|   113|  7520.298| 161.625|  15,026|
| |Hickman County|     0|  0.000|  0.000|   276| 10961.951| 204.260|  25,178|
| |Houston County|     0|  0.000|  0.000|    62|  7560.054| 139.356|   8,201|
| |Henry County|     0|  0.000|  0.000|   303|  9367.754| 318.000|  32,345|
| |Grainger County|     0|  0.000|  0.000|   206|  8833.619| 153.149|  23,320|
| |Fentress County|     0|  0.000|  0.000|    98|  5290.720| 169.673|  18,523|
| |Clay County|     0|  0.000|  0.000|    83| 10899.540| 318.919|   7,615|
| |Claiborne County|     0|  0.000|  0.000|   281|  8792.515| 205.621|  31,959|
| |Cannon County|     0|  0.000|  0.000|   157| 10696.280| 253.051|  14,678|
| |Lake County|     0|  0.000|  0.000|   796| 113454.960| 773.742|   7,016|
| |Van Buren County|     0|  0.000|  0.000|    37|  6301.090| 97.314|   5,872|
| |Perry County|     0|  0.000|  0.000|    83| 10277.365| 106.135|   8,076|
| |Moore County|     0|  0.000|  0.000|    64|  9864.365| 242.205|   6,488|
| |Unicoi County|     0|  0.000|  0.000|   175|  9785.830| 271.607|  17,883|
| |Union County|     0|  0.000|  0.000|   165|  8261.566| 228.892|  19,972|
| |Stewart County|     0|  0.000|  0.000|    79|  5760.117| 72.913|  13,715|
| |Meigs County|     0|  0.000|  0.000|   109|  8774.754| 115.003|  12,422|
| |Johnson County|     0|  0.000|  0.000|   307| 17258.826| 746.892|  17,788|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,011| 173.639| N/A|62,263| 10693.638| N/A|5,822,434|
| |Milwaukee County|   462| 488.514|  1.813|21,396| 22623.889| 184.439| 945,726|
| |Racine County|    78| 397.329|  0.000| 3,571| 18190.524| 165.917| 196,311|
| |Kenosha County|    59| 347.957|  0.843| 2,699| 15917.575| 116.267| 169,561|
| |Waukesha County|    59| 145.968|  0.707| 4,402| 10890.702| 198.276| 404,198|
| |Brown County|    54| 204.126|  1.080| 4,352| 16451.074| 136.084| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,630|  8469.073| 75.780| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,447|  8858.063| 56.844| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,369| 13180.190| 107.279| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,115|  8196.480| 178.527| 136,034|
| |Ozaukee County|    18| 201.746|  1.601|   723|  8103.473| 188.937|  89,221|
| |Winnebago County|    18| 104.708|  0.000| 1,216|  7073.592| 101.384| 171,907|
| |Waupaca County|    15| 294.175|  0.000|   480|  9413.611| 201.720|  50,990|
| |Grant County|    15| 291.608|  2.777|   368|  7154.105| 99.980|  51,439|
| |Outagamie County|    14| 74.514|  0.760| 1,310|  6972.350| 115.572| 187,885|
| |Marathon County|    10| 73.696|  3.158|   668|  4922.914| 66.327| 135,692|
| |Sheboygan County|     8| 69.360|  0.000|   786|  6814.635| 128.812| 115,340|
| |Fond du Lac County|     8| 77.367|  2.763|   700|  6769.630| 160.261| 103,403|
| |Clark County|     8| 230.057|  4.108|   190|  5463.852| 45.190|  34,774|
| |St. Croix County|     5| 55.135|  4.726|   514|  5667.847| 69.312|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   657|  7750.475| 128.079|  84,769|
| |Dodge County|     5| 56.922|  0.000|   857|  9756.486| 185.404|  87,839|
| |Forest County|     4| 444.247|  0.000|    60|  6663.705| 15.866|   9,004|
| |Eau Claire County|     4| 38.224|  0.000|   612|  5848.289| 110.577| 104,646|
| |Marinette County|     4| 99.133|  3.540|   432| 10706.320| 290.317|  40,350|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 24.842|  17,252|
| |Barron County|     3| 66.307|  0.000|   308|  6807.532| 110.512|  45,244|
| |Door County|     3| 108.429|  0.000|   107|  3867.284| 46.469|  27,668|
| |Sauk County|     3| 46.553|  0.000|   472|  7324.416| 135.227|  64,442|
| |Pierce County|     3| 70.169| 10.024|   230|  5379.614| 157.045|  42,754|
| |Kewaunee County|     2| 97.876|  0.000|   135|  6606.636| 139.823|  20,434|
| |Wood County|     2| 27.398|  1.957|   327|  4479.513| 125.246|  72,999|
| |Calumet County|     2| 39.929|  0.000|   340|  6787.918| 182.532|  50,089|
| |Monroe County|     2| 43.240|  0.000|   248|  5361.814| 43.240|  46,253|
| |Columbia County|     2| 34.763|  2.483|   273|  4745.185| 99.324|  57,532|
| |Trempealeau County|     2| 67.456|  0.000|   354| 11939.694| 154.185|  29,649|
| |Adams County|     2| 98.912|  0.000|    89|  4401.583| 70.651|  20,220|
| |Polk County|     2| 45.680|  0.000|   138|  3151.908| 39.154|  43,783|
| |Buffalo County|     2| 153.480|  0.000|    45|  3453.304| 32.889|  13,031|
| |Green County|     1| 27.056|  0.000|   179|  4843.074| 170.068|  36,960|
| |Iron County|     1| 175.840|  0.000|    76| 13363.812| 75.360|   5,687|
| |Jackson County|     1| 48.443|  0.000|    59|  2858.112| 62.283|  20,643|
| |Juneau County|     1| 37.471|  0.000|   139|  5208.528| 32.118|  26,687|
| |La Crosse County|     1|  8.473|  0.000|   932|  7897.234| 94.418| 118,016|
| |Langlade County|     1| 52.113|  0.000|    64|  3335.244| 96.782|  19,189|
| |Oconto County|     1| 26.364|  3.766|   253|  6670.182| 199.616|  37,930|
| |Bayfield County|     1| 66.507|  0.000|    29|  1928.704| 76.008|  15,036|
| |Marquette County|     1| 64.210|  0.000|    80|  5136.766| 45.864|  15,574|
| |Rusk County|     1| 70.532|  0.000|    21|  1481.168| 50.380|  14,178|
| |Manitowoc County|     1| 12.661|  0.000|   354|  4482.091| 65.115|  78,981|
| |Taylor County|     1| 49.157|  7.022|    73|  3588.458| 98.314|  20,343|
| |Waushara County|     1| 40.912|  5.845|   120|  4909.381| 46.756|  24,443|
| |Ashland County|     1| 64.259|  0.000|    27|  1734.996| 55.079|  15,562|
| |Burnett County|     1| 64.876|  0.000|    23|  1492.150| 18.536|  15,414|
| |Shawano County|     0|  0.000|  0.000|   205|  5012.347| 129.238|  40,899|
| |Iowa County|     0|  0.000|  0.000|    86|  3632.064| 108.600|  23,678|
| |Chippewa County|     0|  0.000|  0.000|   244|  3773.702| 68.492|  64,658|
| |Crawford County|     0|  0.000|  0.000|    78|  4835.410| 79.705|  16,131|
| |Douglas County|     0|  0.000|  0.000|   198|  4588.644| 175.468|  43,150|
| |Green Lake County|     0|  0.000|  0.000|    57|  3013.800| 22.660|  18,913|
| |Dunn County|     0|  0.000|  0.000|   131|  2887.498| 59.828|  45,368|
| |Florence County|     0|  0.000|  0.000|     8|  1862.631| 66.523|   4,295|
| |Washburn County|     0|  0.000|  0.000|    47|  2989.822| 72.701|  15,720|
| |Vernon County|     0|  0.000|  0.000|    67|  2173.772| 37.079|  30,822|
| |Price County|     0|  0.000|  0.000|    33|  2471.725| 85.601|  13,351|
| |Oneida County|     0|  0.000|  0.000|   156|  4382.638| 240.804|  35,595|
| |Sawyer County|     0|  0.000|  0.000|    82|  4952.289| 276.086|  16,558|
| |Portage County|     0|  0.000|  0.000|   428|  6047.589| 123.132|  70,772|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689|  0.000|   7,287|
| |Menominee County|     0|  0.000|  0.000|    26|  5706.760| 188.135|   4,556|
| |Lincoln County|     0|  0.000|  0.000|    70|  2536.875| 20.709|  27,593|
| |Lafayette County|     0|  0.000|  0.000|   154|  9240.924| 342.891|  16,665|
| |Vilas County|     0|  0.000|  0.000|    65|  2928.588| 160.911|  22,195|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   988| 320.763| N/A|57,684| 18727.623| N/A|3,080,156|
| |Clark County|   842| 371.463|  6.176|50,081| 22094.088| 284.742|2,266,715|
| |Washoe County|   121| 256.617|  1.818| 5,907| 12527.597| 145.730| 471,519|
| |Nye County|     9| 193.453|  0.000|   408|  8769.856| 141.251|  46,523|
| |Lyon County|     6| 104.330|  2.484|   239|  4155.799| 59.617|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074| 67.902|  16,831|
| |Elko County|     2| 37.895|  0.000|   562| 10648.376| 154.285|  52,778|
| |White Pine County|     1| 104.384|  0.000|    15|  1565.762| 14.912|   9,580|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 25.824|   5,532|
| |Churchill County|     1| 40.146|  0.000|    69|  2770.083| 114.703|  24,909|
| |Douglas County|     1| 20.448|  2.921|   208|  4253.144| 55.501|  48,905|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     6|  1455.251| 69.298|   4,123|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Eureka County|     0|  0.000|  0.000|     4|  1971.414| 140.815|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   953| 302.054| N/A|49,966| 15836.733| N/A|3,155,070|
| |Polk County|   208| 424.350|  1.166|10,535| 21492.938| 192.648| 490,161|
| |Linn County|    88| 388.168|  0.630| 2,445| 10784.893| 155.645| 226,706|
| |Black Hawk County|    66| 502.941|  4.354| 3,180| 24232.633| 137.166| 131,228|
| |Woodbury County|    52| 504.330|  1.386| 3,754| 36408.779| 112.227| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   857| 20087.193| 60.272|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,913| 20470.183| 162.037|  93,453|
| |Wapello County|    33| 943.693|  0.000|   927| 26509.194| 249.200|  34,969|
| |Dubuque County|    31| 318.566|  0.000| 1,722| 17695.841| 187.910|  97,311|
| |Pottawattamie County|    29| 311.139|  7.664| 1,350| 14484.046| 142.541|  93,206|
| |Tama County|    29| 1720.660|  0.000|   556| 32989.201| 110.190|  16,854|
| |Jasper County|    27| 726.099|  7.684|   484| 13016.001| 99.887|  37,185|
| |Marshall County|    26| 660.418|  3.629| 1,452| 36881.811| 163.290|  39,369|
| |Johnson County|    20| 132.328|  3.781| 2,123| 14046.579| 114.369| 151,140|
| |Mahaska County|    17| 769.405|  0.000|   142|  6426.793| 32.328|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   644| 15170.789| 195.188|  42,450|
| |Story County|    15| 154.453|  1.471| 1,181| 12160.590| 80.904|  97,117|
| |Scott County|    14| 80.952|  0.826| 1,758| 10165.199| 100.776| 172,943|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Franklin County|    12| 1191.658| 56.746|   248| 24627.607| 297.915|  10,070|
| |Buena Vista County|    12| 611.621|  0.000| 1,797| 91590.214| 50.968|  19,620|
| |Plymouth County|    12| 476.625| 22.696|   474| 18826.707| 147.527|  25,177|
| |Washington County|    10| 455.270|  0.000|   305| 13885.727| 110.566|  21,965|
| |Poweshiek County|     8| 432.339|  0.000|   159|  8592.737| 61.763|  18,504|
| |Monroe County|     8| 1038.017| 18.536|    74|  9601.661| 74.144|   7,707|
| |Webster County|     8| 222.816|  3.979|   842| 23451.426| 314.330|  35,904|
| |Bremer County|     7| 279.307|  0.000|   231|  9217.141| 199.505|  25,062|
| |O'Brien County|     5| 363.557| 41.549|   143| 10397.731| 114.261|  13,753|
| |Guthrie County|     5| 467.771|  0.000|   137| 12816.915| 120.284|  10,689|
| |Dickinson County|     4| 231.777|  0.000|   385| 22308.495| 57.944|  17,258|
| |Allamakee County|     4| 292.248|  0.000|   158| 11543.801| 62.625|  13,687|
| |Emmet County|     4| 434.405| 31.029|   193| 20960.035| 124.116|   9,208|
| |Lee County|     4| 118.846|  4.245|   121|  3595.092| 93.379|  33,657|
| |Henry County|     4| 200.461|  7.159|   136|  6815.676| 157.505|  19,954|
| |Clinton County|     4| 86.153|  3.077|   421|  9067.609| 255.382|  46,429|
| |Montgomery County|     4| 403.348|  0.000|    60|  6050.217| 216.079|   9,917|
| |Lucas County|     4| 465.116|  0.000|    73|  8488.372| 332.226|   8,600|
| |Appanoose County|     3| 241.429|  0.000|    52|  4184.774| 103.470|  12,426|
| |Crawford County|     3| 178.359|  0.000|   736| 43757.432| 84.933|  16,820|
| |Sioux County|     3| 86.071|  4.099|   650| 18648.687| 176.240|  34,855|
| |Boone County|     3| 114.355|  5.445|   266| 10139.514| 174.256|  26,234|
| |Clarke County|     3| 319.319|  0.000|   206| 21926.557| 243.291|   9,395|
| |Clayton County|     3| 170.950|  0.000|   108|  6154.197| 56.983|  17,549|
| |Floyd County|     3| 191.791|  9.133|   163| 10420.662| 283.121|  15,642|
| |Butler County|     2| 138.514|  0.000|   127|  8795.623| 89.045|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    86|  8895.325| 59.105|   9,668|
| |Carroll County|     2| 99.182|  7.084|   196|  9719.812| 92.097|  20,165|
| |Davis County|     2| 222.222| 15.873|    61|  6777.778| 158.730|   9,000|
| |Pocahontas County|     2| 302.160| 21.583|   118| 17827.466| 86.332|   6,619|
| |Hancock County|     2| 188.147|  0.000|   123| 11571.025| 80.634|  10,630|
| |Madison County|     2| 122.414|  0.000|   127|  7773.289| 174.877|  16,338|
| |Jones County|     2| 96.707|  0.000|   134|  6479.377| 55.261|  20,681|
| |Des Moines County|     2| 51.325|  0.000|   194|  4978.572| 186.971|  38,967|
| |Lyon County|     2| 170.140| 24.306|   119| 10123.352| 133.682|  11,755|
| |Benton County|     1| 38.994|  0.000|   160|  6239.033| 83.558|  25,645|
| |Audubon County|     1| 181.951|  0.000|    29|  5276.565| 25.993|   5,496|
| |Cedar County|     1| 53.686|  0.000|   135|  7247.544| 92.032|  18,627|
| |Cass County|     1| 77.906|  0.000|    82|  6388.283| 378.400|  12,836|
| |Buchanan County|     1| 47.226|  0.000|   130|  6139.315| 80.958|  21,175|
| |Cherokee County|     1| 89.008|  0.000|   110|  9790.832| 139.869|  11,235|
| |Clay County|     1| 62.438|  0.000|   203| 12674.825| 258.670|  16,016|
| |Delaware County|     1| 58.785|  0.000|   123|  7230.615| 243.540|  17,011|
| |Jackson County|     1| 51.443|  0.000|   158|  8127.990| 88.188|  19,439|
| |Iowa County|     1| 61.789|  0.000|    97|  5993.574| 26.481|  16,184|
| |Harrison County|     1| 71.179| 10.168|   110|  7829.739| 111.853|  14,049|
| |Hamilton County|     1| 67.691|  0.000|   252| 17058.147| 87.031|  14,773|
| |Grundy County|     1| 81.753|  0.000|    82|  6703.728| 70.074|  12,232|
| |Humboldt County|     1| 104.624|  0.000|   122| 12764.177| 418.498|   9,558|
| |Keokuk County|     1| 97.599|  0.000|    39|  3806.363| 111.542|  10,246|
| |Warren County|     1| 19.430|  0.000|   582| 11308.437| 111.030|  51,466|
| |Wayne County|     1| 155.255|  0.000|    20|  3105.108| 22.179|   6,441|
| |Winneshiek County|     1| 50.023|  0.000|    97|  4852.183| 50.023|  19,991|
| |Van Buren County|     1| 141.965|  0.000|    36|  5110.733| 40.561|   7,044|
| |Shelby County|     1| 87.306|  0.000|   187| 16326.174| 137.195|  11,454|
| |Mills County|     1| 66.186|  9.455|    93|  6155.272| 75.641|  15,109|
| |Wright County|     1| 79.605|  0.000|   478| 38051.266| 307.048|  12,562|
| |Union County|     1| 81.693|  0.000|    78|  6372.028| 46.682|  12,241|
| |Ringgold County|     1| 204.332|  0.000|    23|  4699.632| 58.381|   4,894|
| |Sac County|     0|  0.000|  0.000|    86|  8846.826| 73.479|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    90| 10128.292| 160.767|   8,886|
| |Page County|     0|  0.000|  0.000|    96|  6354.670| 179.671|  15,107|
| |Osceola County|     0|  0.000|  0.000|    85| 14266.532| 167.842|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972|  0.000|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    80|  7557.151| 26.990|  10,586|
| |Marion County|     0|  0.000|  0.000|   177|  5322.828| 77.329|  33,253|
| |Kossuth County|     0|  0.000|  0.000|    95|  6413.286| 125.373|  14,813|
| |Jefferson County|     0|  0.000|  0.000|    87|  4755.398| 78.085|  18,295|
| |Ida County|     0|  0.000|  0.000|    32|  4664.723| 62.474|   6,860|
| |Howard County|     0|  0.000|  0.000|    50|  5459.707| 15.599|   9,158|
| |Hardin County|     0|  0.000|  0.000|   185| 10981.835| 118.723|  16,846|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473| 64.292|   8,888|
| |Fremont County|     0|  0.000|  0.000|    44|  6321.839| 205.255|   6,960|
| |Fayette County|     0|  0.000|  0.000|    86|  4376.590| 36.350|  19,650|
| |Decatur County|     0|  0.000|  0.000|    26|  3303.685| 54.456|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    56|  4692.869| 47.886|  11,933|
| |Adams County|     0|  0.000|  0.000|    17|  4719.600| 39.661|   3,602|
| |Adair County|     0|  0.000|  0.000|    34|  4753.915| 219.719|   7,152|
| |Taylor County|     0|  0.000|  0.000|   100| 16337.200| 140.033|   6,121|
| |Winnebago County|     0|  0.000|  0.000|    89|  8595.712| 179.365|  10,354|
| |Worth County|     0|  0.000|  0.000|    68|  9212.844| 77.419|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   790| 176.826| N/A|36,945|  8269.406| N/A|4,467,673|
| |Jefferson County|   244| 318.223|  1.491| 8,802| 11479.517| 239.226| 766,757|
| |Fayette County|    48| 148.537|  0.884| 3,241| 10029.336| 146.327| 323,152|
| |Kenton County|    41| 245.512|  2.566| 1,449|  8676.751| 74.423| 166,998|
| |Hopkins County|    34| 760.865|  3.197|   431|  9645.079| 54.347|  44,686|
| |Graves County|    25| 670.853| 11.500|   574| 15402.780| 187.839|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,117|  8361.968| 67.375| 133,581|
| |Logan County|    23| 848.646|  0.000|   341| 12582.097| 163.404|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,702| 20331.688| 177.367| 132,896|
| |Shelby County|    21| 428.362|  0.000|   786| 16032.963| 177.756|  49,024|
| |Adair County|    19| 989.480|  0.000|   215| 11196.750| 81.837|  19,202|
| |Oldham County|    16| 239.525|  4.277|   640|  9580.982| 115.485|  66,799|
| |Butler County|    15| 1164.687|  0.000|   298| 23138.442| 11.092|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   151| 11328.682| 85.742|  13,329|
| |Campbell County|    13| 138.913|  0.000|   592|  6325.868| 67.167|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   112|  9218.107| 188.125|  12,150|
| |Grayson County|    11| 416.241|  0.000|   213|  8059.939| 140.549|  26,427|
| |Muhlenberg County|    11| 359.219|  4.665|   629| 20540.788| 32.656|  30,622|
| |Casey County|    10| 618.850|  0.000|   201| 12438.889| 388.992|  16,159|
| |Daviess County|     9| 88.660|  1.407|   793|  7811.961| 81.624| 101,511|
| |Ohio County|     9| 375.094| 11.908|   361| 15045.428| 101.216|  23,994|
| |Christian County|     9| 127.730|  6.082|   523|  7422.546| 85.153|  70,461|
| |Hardin County|     8| 72.099|  0.000|   683|  6155.482| 167.373| 110,958|
| |Allen County|     8| 375.323|  0.000|   230| 10790.523| 67.022|  21,315|
| |Knox County|     8| 256.863|  0.000|   254|  8155.402| 146.779|  31,145|
| |Simpson County|     7| 376.911|  0.000|   152|  8184.364| 53.844|  18,572|
| |Gallatin County|     7| 789.266|  0.000|    81|  9132.935| 32.215|   8,869|
| |Clark County|     7| 193.034|  0.000|   167|  4605.245|  0.000|  36,263|
| |Franklin County|     7| 137.279|  5.603|   329|  6452.119| 168.097|  50,991|
| |Grant County|     6| 239.339|  5.699|   126|  5026.128| 108.273|  25,069|
| |Laurel County|     5| 82.219|  2.349|   456|  7498.397| 138.598|  60,813|
| |Clay County|     5| 251.244|  0.000|   159|  7989.548| 100.497|  19,901|
| |Russell County|     5| 278.971|  0.000|   124|  6918.485| 191.295|  17,923|
| |Bullitt County|     5| 61.217|  1.749|   401|  4909.643| 125.933|  81,676|
| |Pulaski County|     5| 76.948|  6.596|   338|  5201.681| 164.888|  64,979|
| |McCracken County|     4| 61.145|  0.000|   377|  5762.940| 63.329|  65,418|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686|  0.000|   8,210|
| |Bell County|     4| 153.657| 10.976|   324| 12446.220| 203.047|  26,032|
| |Calloway County|     4| 102.561|  0.000|   257|  6589.575| 201.460|  39,001|
| |Henderson County|     3| 66.357|  0.000|   360|  7962.840| 94.796|  45,210|
| |Harlan County|     3| 115.340|  0.000|   239|  9188.774| 137.310|  26,010|
| |Boyd County|     3| 64.215|  0.000|   195|  4173.980| 39.752|  46,718|
| |Barren County|     3| 67.798|  3.228|   383|  8655.563| 100.083|  44,249|
| |Perry County|     3| 116.469|  0.000|   247|  9589.254| 260.668|  25,758|
| |Meade County|     3| 104.998|  5.000|    99|  3464.931| 39.999|  28,572|
| |Pike County|     3| 51.835|  0.000|   252|  4354.136| 46.898|  57,876|
| |Henry County|     2| 124.023|  0.000|   129|  7999.504| 212.611|  16,126|
| |Monroe County|     2| 187.793|  0.000|    96|  9014.085| 80.483|  10,650|
| |Lincoln County|     2| 81.470|  5.819|   117|  4765.978| 104.747|  24,549|
| |Marshall County|     2| 64.309|  0.000|   140|  4501.608| 55.122|  31,100|
| |Metcalfe County|     2| 198.590|  0.000|    62|  6156.290| 85.110|  10,071|
| |Green County|     2| 182.799|  0.000|    40|  3655.973| 117.513|  10,941|
| |Fulton County|     2| 335.064| 23.933|    90| 15077.902| 502.597|   5,969|
| |Floyd County|     2| 56.197|  0.000|   106|  2978.448| 68.239|  35,589|
| |Carroll County|     2| 188.129|  0.000|   164| 15426.583| 215.005|  10,631|
| |Breckinridge County|     2| 97.671|  0.000|    76|  3711.481| 146.506|  20,477|
| |Nelson County|     2| 43.259|  0.000|   230|  4974.802| 83.428|  46,233|
| |Taylor County|     2| 77.613|  0.000|   144|  5588.110| 216.207|  25,769|
| |Madison County|     1| 10.754|  0.000|   583|  6269.694| 241.201|  92,987|
| |Carlisle County|     1| 210.084|  0.000|    45|  9453.782| 360.144|   4,760|
| |McLean County|     1| 108.613|  0.000|    43|  4670.360| 31.032|   9,207|
| |Livingston County|     1| 108.767|  0.000|    35|  3806.831| 31.076|   9,194|
| |Larue County|     1| 69.454|  0.000|    60|  4167.245| 79.376|  14,398|
| |Webster County|     1| 77.268|  0.000|    90|  6954.103| 77.268|  12,942|
| |Whitley County|     1| 27.576|  0.000|   168|  4632.694| 51.212|  36,264|
| |Bourbon County|     1| 50.536|  0.000|    86|  4346.068| 93.852|  19,788|
| |Greenup County|     1| 28.492|  0.000|   121|  3447.490| 77.334|  35,098|
| |Bath County|     1| 80.000|  0.000|    41|  3280.000| 57.143|  12,500|
| |Anderson County|     1| 43.962|  0.000|    89|  3912.604| 56.522|  22,747|
| |Mason County|     1| 58.582|  0.000|    54|  3163.445|  8.369|  17,070|
| |Knott County|     1| 67.540|  0.000|    66|  4457.652| 173.675|  14,806|
| |Crittenden County|     1| 113.559|  0.000|    32|  3633.886| 97.336|   8,806|
| |Clinton County|     1| 97.867| 13.981|    38|  3718.927| 153.790|  10,218|
| |Carter County|     1| 37.318|  0.000|   104|  3881.031| 26.655|  26,797|
| |Leslie County|     0|  0.000|  0.000|    32|  3239.850| 57.854|   9,877|
| |Lawrence County|     0|  0.000|  0.000|    37|  2415.617|  9.327|  15,317|
| |Johnson County|     0|  0.000|  0.000|    66|  2974.581| 148.085|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   356|  6578.583| 100.315|  54,115|
| |Hickman County|     0|  0.000|  0.000|    55| 12557.078| 587.084|   4,380|
| |Hart County|     0|  0.000|  0.000|   108|  5673.759| 150.099|  19,035|
| |Harrison County|     0|  0.000|  0.000|   123|  6512.761| 45.385|  18,886|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 16.379|   8,722|
| |Garrard County|     0|  0.000|  0.000|    83|  4698.291| 97.039|  17,666|
| |Fleming County|     0|  0.000|  0.000|    62|  4252.109| 48.987|  14,581|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 91.147|  14,106|
| |Elliott County|     0|  0.000|  0.000|    14|  1862.445| 114.027|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    63|  9525.249| 496.782|   6,614|
| |Caldwell County|     0|  0.000|  0.000|    53|  4157.841| 44.828|  12,747|
| |Breathitt County|     0|  0.000|  0.000|    32|  2533.650| 45.244|  12,630|
| |Marion County|     0|  0.000|  0.000|   124|  6433.871| 51.886|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    41|  3371.433| 117.472|  12,161|
| |McCreary County|     0|  0.000|  0.000|    42|  2437.467| 41.454|  17,231|
| |Spencer County|     0|  0.000|  0.000|   128|  6614.645| 132.883|  19,351|
| |Todd County|     0|  0.000|  0.000|    34|  2765.577|  0.000|  12,294|
| |Trigg County|     0|  0.000|  0.000|    56|  3822.265| 29.252|  14,651|
| |Union County|     0|  0.000|  0.000|    70|  4867.534| 119.205|  14,381|
| |Trimble County|     0|  0.000|  0.000|    33|  3895.644| 16.864|   8,471|
| |Woodford County|     0|  0.000|  0.000|   165|  6171.916| 122.904|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    16|  2235.574| 99.802|   7,157|
| |Wayne County|     0|  0.000|  0.000|    73|  3590.223| 140.518|  20,333|
| |Washington County|     0|  0.000|  0.000|    92|  7606.449| 307.093|  12,095|
| |Martin County|     0|  0.000|  0.000|    37|  3305.047| 51.043|  11,195|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Mercer County|     0|  0.000|  0.000|    86|  3921.032| 39.080|  21,933|
| |Lee County|     0|  0.000|  0.000|     7|   945.563| 38.594|   7,403|
| |Letcher County|     0|  0.000|  0.000|    62|  2876.630| 59.654|  21,553|
| |Bracken County|     0|  0.000|  0.000|    33|  3974.467| 51.616|   8,303|
| |Boyle County|     0|  0.000|  0.000|   161|  5355.955| 80.791|  30,060|
| |Ballard County|     0|  0.000|  0.000|    36|  4563.895| 90.553|   7,888|
| |Montgomery County|     0|  0.000|  0.000|   128|  4545.939| 65.957|  28,157|
| |Scott County|     0|  0.000|  0.000|   407|  7139.850| 127.811|  57,004|
| |Rowan County|     0|  0.000|  0.000|    84|  3434.178| 87.607|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    74|  4432.465| 111.239|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    62|  5016.587| 138.707|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    47|  3221.385| 58.749|  14,590|
| |Owsley County|     0|  0.000|  0.000|    13|  2944.507| 32.357|   4,415|
| |Owen County|     0|  0.000|  0.000|    54|  4953.674| 144.155|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    30|  2254.114|  0.000|  13,309|
| |Lewis County|     0|  0.000|  0.000|    53|  3992.467| 172.182|  13,275|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   695| 331.453| N/A|21,512| 10259.301| N/A|2,096,829|
| |McKinley County|   229| 3208.766| 14.012| 4,077| 57127.244| 104.090|  71,367|
| |San Juan County|   185| 1492.441|  3.457| 3,069| 24758.386| 59.928| 123,958|
| |Bernalillo County|   134| 197.314|  1.262| 5,226|  7695.241| 49.854| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,146|  7809.306| 34.072| 146,748|
| |Dona Ana County|    31| 142.075|  2.619| 2,554| 11705.126| 156.479| 218,195|
| |Cibola County|    18| 674.789|  5.355|   371| 13908.154| 139.242|  26,675|
| |Otero County|    10| 148.170|  0.000|   204|  3022.670| 19.050|  67,490|
| |Rio Arriba County|     7| 179.851|  7.341|   319|  8196.090| 47.716|  38,921|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024| 17.173|  16,637|
| |Chaves County|     6| 92.858|  0.000|   485|  7505.997| 198.981|  64,615|
| |Luna County|     5| 210.890| 12.051|   254| 10713.231| 84.356|  23,709|
| |Lea County|     5| 70.353|  2.010|   863| 12142.958| 315.584|  71,070|
| |Valencia County|     4| 52.159|  0.000|   441|  5750.574| 96.867|  76,688|
| |Eddy County|     4| 68.423|  0.000|   336|  5747.520| 163.726|  58,460|
| |Santa Fe County|     3| 19.952|  0.000|   660|  4389.524| 47.506| 150,358|
| |Lincoln County|     2| 102.187|  7.299|   130|  6642.142| 124.084|  19,572|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824|  5.291|  26,998|
| |Curry County|     2| 40.855|  0.000|   569| 11623.156| 183.846|  48,954|
| |Union County|     2| 492.732|  0.000|    30|  7390.983| 70.390|   4,059|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411|  9.240|  15,461|
| |Quay County|     1| 121.168|  0.000|    37|  4483.218| 51.929|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   168|  9081.081| 123.552|  18,500|
| |Sierra County|     1| 92.670| 13.239|    32|  2965.434| 13.239|  10,791|
| |Taos County|     1| 30.560|  0.000|   112|  3422.669| 43.656|  32,723|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 35.891|  11,941|
| |San Miguel County|     0|  0.000|  0.000|    46|  1686.402| 20.949|  27,277|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Los Alamos County|     0|  0.000|  0.000|    24|  1239.093| 29.502|  19,369|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 68.060|   4,198|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   627| 158.455| N/A|45,392| 11471.401| N/A|3,956,971|
| |Oklahoma County|   119| 149.229|  2.150|10,951| 13732.798| 179.325| 797,434|
| |Tulsa County|   110| 168.828|  1.535|10,898| 16726.217| 253.461| 651,552|
| |Cleveland County|    56| 197.173|  1.006| 3,084| 10858.620| 107.138| 284,014|
| |Washington County|    39| 756.885|  0.000|   647| 12556.524| 149.713|  51,527|
| |McCurtain County|    28| 852.827|  0.000|   876| 26681.287| 165.344|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   903| 11108.514| 203.858|  81,289|
| |Delaware County|    20| 465.019|  3.322|   445| 10346.672| 132.863|  43,009|
| |Rogers County|    18| 194.681|  3.090| 1,031| 11150.889| 242.579|  92,459|
| |Caddo County|    17| 591.058|  4.967|   434| 15089.354| 248.344|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   531|  7809.168| 107.148|  67,997|
| |Creek County|    15| 209.726|  3.995|   637|  8906.350| 201.736|  71,522|
| |Osage County|    11| 234.227|  0.000|   436|  9283.904| 155.137|  46,963|
| |Kay County|    11| 252.653|  0.000|   252|  5788.047| 68.905|  43,538|
| |Comanche County|    10| 82.816|  0.000|   854|  7072.522| 73.352| 120,749|
| |Pottawatomie County|     9| 123.981|  1.968|   465|  6405.665| 96.429|  72,592|
| |Canadian County|     9| 60.685|  2.890| 1,256|  8468.976| 123.297| 148,306|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 50.020|   5,712|
| |Mayes County|     7| 170.316|  3.476|   332|  8077.859| 132.082|  41,100|
| |Grady County|     7| 125.372|  0.000|   451|  8077.515| 76.758|  55,834|
| |Texas County|     7| 350.298|  0.000| 1,060| 53045.088| 114.383|  19,983|
| |Jackson County|     7| 285.365| 11.648|   531| 21646.963| 198.008|  24,530|
| |Adair County|     6| 270.343|  0.000|   346| 15589.799| 205.976|  22,194|
| |Carter County|     5| 103.926|  2.969|   352|  7316.414| 109.865|  48,111|
| |Seminole County|     5| 206.118|  0.000|   248| 10223.431| 200.228|  24,258|
| |Garfield County|     5| 81.892|  2.340|   512|  8385.744| 287.792|  61,056|
| |McClain County|     4| 98.829|  0.000|   457| 11291.199| 130.595|  40,474|
| |Sequoyah County|     4| 96.226|  0.000|   361|  8684.356| 244.001|  41,569|
| |Garvin County|     4| 144.347|  0.000|   236|  8516.474| 108.260|  27,711|
| |Pittsburg County|     4| 91.630|  3.272|   383|  8773.537| 510.508|  43,654|
| |Payne County|     4| 48.909|  0.000|   766|  9366.135| 137.994|  81,784|
| |Ottawa County|     3| 96.379|  4.589|   395| 12689.948| 197.348|  31,127|
| |Okmulgee County|     3| 77.993|  0.000|   494| 12842.844| 308.258|  38,465|
| |Pawnee County|     3| 183.195|  0.000|   148|  9037.616| 183.195|  16,376|
| |Stephens County|     3| 69.536|  3.311|   204|  4728.461| 46.357|  43,143|
| |Noble County|     2| 179.678|  0.000|    87|  7816.009| 51.337|  11,131|
| |Cotton County|     2| 352.983|  0.000|    19|  3353.336|  0.000|   5,666|
| |Cherokee County|     2| 41.104|  0.000|   456|  9371.725| 208.456|  48,657|
| |Hughes County|     2| 150.614| 10.758|   146| 10994.804| 301.228|  13,279|
| |Lincoln County|     2| 57.344|  0.000|   180|  5160.994| 135.169|  34,877|
| |Pontotoc County|     2| 52.241|  0.000|   207|  5406.959| 78.362|  38,284|
| |Okfuskee County|     1| 83.382| 11.912|    74|  6170.266| 190.587|  11,993|
| |McIntosh County|     1| 51.031|  0.000|   202| 10308.226| 306.185|  19,596|
| |Latimer County|     1| 99.275|  0.000|    93|  9232.602| 226.915|  10,073|
| |Craig County|     1| 70.711| 10.102|    89|  6293.311| 121.219|  14,142|
| |Le Flore County|     1| 20.059|  0.000|   376|  7542.174| 283.691|  49,853|
| |Logan County|     1| 20.829|  0.000|   228|  4748.912| 95.216|  48,011|
| |Choctaw County|     1| 68.157|  0.000|   196| 13358.779| 243.418|  14,672|
| |Major County|     1| 131.079|  0.000|    35|  4587.757| 168.530|   7,629|
| |Marshall County|     1| 59.063|  8.438|   111|  6556.021| 101.251|  16,931|
| |Nowata County|     1| 99.246|  0.000|    60|  5954.744| 56.712|  10,076|
| |Bryan County|     1| 20.836|  0.000|   479|  9980.206| 229.191|  47,995|
| |Roger Mills County|     1| 279.096| 39.871|     9|  2511.862| 39.871|   3,583|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 39.409|   7,250|
| |Beckham County|     1| 45.748|  0.000|    61|  2790.613| 104.566|  21,859|
| |Kiowa County|     1| 114.837|  0.000|    30|  3445.108| 49.216|   8,708|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Johnston County|     0|  0.000|  0.000|    48|  4330.176| 38.662|  11,085|
| |Haskell County|     0|  0.000|  0.000|    66|  5226.895| 203.645|  12,627|
| |Harper County|     0|  0.000|  0.000|    10|  2711.497| 38.736|   3,688|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 269.237|   2,653|
| |Grant County|     0|  0.000|  0.000|    16|  3692.592| 131.878|   4,333|
| |Dewey County|     0|  0.000|  0.000|    10|  2044.572| 58.416|   4,891|
| |Custer County|     0|  0.000|  0.000|   211|  7275.109| 88.661|  29,003|
| |Coal County|     0|  0.000|  0.000|    40|  7279.345| 233.979|   5,495|
| |Cimarron County|     0|  0.000|  0.000|     3|  1403.837| 133.699|   2,137|
| |Blaine County|     0|  0.000|  0.000|    43|  4560.399| 60.603|   9,429|
| |Beaver County|     0|  0.000|  0.000|    39|  7343.250| 80.695|   5,311|
| |Atoka County|     0|  0.000|  0.000|    79|  5742.114| 124.603|  13,758|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Love County|     0|  0.000|  0.000|    76|  7412.465| 153.265|  10,253|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 23.802|   6,002|
| |Kingfisher County|     0|  0.000|  0.000|   139|  8817.000| 226.542|  15,765|
| |Woodward County|     0|  0.000|  0.000|    44|  2177.032| 63.615|  20,211|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    31|  2839.868| 78.522|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   112| 10093.727| 141.621|  11,096|
| |Murray County|     0|  0.000|  0.000|    76|  5400.412| 81.209|  14,073|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   593| 840.242| N/A|12,959| 18362.052| N/A| 705,749|
| |District of Columbia|   593| 840.242|  1.215|12,959| 18362.052| 104.448| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   592| 607.950| N/A|15,509| 15926.857| N/A| 973,764|
| |New Castle County|   291| 520.803|  0.511| 7,309| 13080.914| 68.264| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,881| 25108.336| 62.821| 234,225|
| |Kent County|   109| 602.923|  1.580| 2,319| 12827.321| 64.006| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   572| 189.542| N/A|49,295| 16334.726| N/A|3,017,804|
| |Pulaski County|    87| 221.989|  2.187| 5,787| 14766.108| 231.831| 391,911|
| |Washington County|    53| 221.584|  1.792| 6,352| 26556.627| 109.896| 239,187|
| |Benton County|    43| 154.044|  1.535| 4,825| 17285.171| 97.749| 279,141|
| |Jefferson County|    40| 598.587|  0.000| 1,617| 24197.893| 438.251|  66,824|
| |Crittenden County|    24| 500.469| 11.916| 1,402| 29235.742| 330.667|  47,955|
| |Sebastian County|    21| 164.285|  4.470| 2,297| 17969.600| 357.626| 127,827|
| |Union County|    19| 491.185|  7.386|   523| 13520.500| 240.053|  38,682|
| |Garland County|    17| 171.050| 12.937| 1,115| 11218.884| 294.666|  99,386|
| |Yell County|    17| 796.589| 20.082| 1,077| 50466.239| 167.351|  21,341|
| |Mississippi County|    14| 344.395|  7.028| 1,068| 26272.416| 622.019|  40,651|
| |Craighead County|    12| 108.763|  0.000| 1,419| 12861.183| 288.739| 110,332|
| |Hot Spring County|    12| 355.334|  0.000| 1,564| 46311.924| 359.565|  33,771|
| |Lincoln County|    12| 921.376| 10.969| 1,224| 93980.344| 307.125|  13,024|
| |Columbia County|    12| 511.574| 30.451|   223|  9506.757| 85.262|  23,457|
| |Sevier County|    10| 587.993|  0.000| 1,009| 59328.512| 428.395|  17,007|
| |Newton County|    10| 1289.823| 92.130|   106| 13672.127| 110.556|   7,753|
| |Pope County|    10| 156.074|  0.000| 1,363| 21272.943| 216.275|  64,072|
| |Chicot County|     9| 889.504| 14.119|   738| 72939.316| 536.526|  10,118|
| |Phillips County|     9| 506.130| 16.068|   332| 18670.566| 273.149|  17,782|
| |Nevada County|     9| 1090.645|  0.000|   146| 17692.681| 207.742|   8,252|
| |Lawrence County|     9| 548.580|  0.000|   221| 13470.681| 261.228|  16,406|
| |Lee County|     8| 903.240|  0.000|   898| 101388.732| 129.034|   8,857|
| |Saline County|     7| 57.172|  1.167| 1,133|  9253.739| 214.688| 122,437|
| |Carroll County|     7| 246.653|  0.000|   379| 13354.475| 166.113|  28,380|
| |Faulkner County|     6| 47.616|  1.134| 1,340| 10634.330| 114.506| 126,007|
| |Miller County|     5| 115.588|  0.000|   519| 11998.058| 99.076|  43,257|
| |Ashley County|     5| 254.362|  0.000|   335| 17042.275| 370.642|  19,657|
| |Crawford County|     5| 79.043|  4.517|   668| 10560.096| 223.578|  63,257|
| |Sharp County|     5| 286.664|  0.000|   117|  6707.946| 90.095|  17,442|
| |Cleburne County|     5| 200.650|  0.000|   206|  8266.784| 108.924|  24,919|
| |Cross County|     4| 243.620|  8.701|   212| 12911.870| 339.328|  16,419|
| |Howard County|     4| 302.984| 21.642|   360| 27268.596| 562.685|  13,202|
| |Bradley County|     4| 371.644| 13.273|   207| 19232.556| 530.919|  10,763|
| |Clay County|     4| 274.895|  0.000|   140|  9621.332| 255.260|  14,551|
| |Randolph County|     4| 222.742|  7.955|   239| 13308.832| 326.158|  17,958|
| |Drew County|     3| 164.663|  0.000|   221| 12130.194| 360.691|  18,219|
| |Poinsett County|     3| 127.508|  0.000|   308| 13090.785| 716.472|  23,528|
| |Conway County|     3| 143.913|  0.000|   156|  7483.450| 89.089|  20,846|
| |St. Francis County|     3| 120.029|  0.000| 1,228| 49131.792| 457.253|  24,994|
| |Cleveland County|     2| 251.383|  0.000|   112| 14077.426| 520.721|   7,956|
| |Ouachita County|     2| 85.536|  0.000|   107|  4576.170| 140.523|  23,382|
| |Franklin County|     2| 112.899|  0.000|   133|  7507.762| 161.284|  17,715|
| |Desha County|     2| 176.041|  0.000|   203| 17868.145| 364.656|  11,361|
| |Greene County|     2| 44.126|  3.152|   505| 11141.754| 261.603|  45,325|
| |Hempstead County|     2| 92.885|  0.000|   253| 11749.954| 172.501|  21,532|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385|  8.634|  16,545|
| |White County|     2| 25.396|  0.000|   341|  4329.994| 103.397|  78,753|
| |Madison County|     2| 120.656|  8.618|   271| 16348.938| 34.473|  16,576|
| |Johnson County|     2| 75.250|  0.000|   676| 25434.570| 161.250|  26,578|
| |Boone County|     2| 53.430|  3.816|   217|  5797.179| 125.943|  37,432|
| |Lonoke County|     2| 27.282|  0.000|   539|  7352.440| 126.665|  73,309|
| |Lafayette County|     2| 301.932|  0.000|    58|  8756.039| 129.400|   6,624|
| |Polk County|     1| 50.090|  0.000|   154|  7713.885| 143.115|  19,964|
| |Stone County|     1| 79.962|  0.000|    74|  5917.160| 171.346|  12,506|
| |Montgomery County|     1| 111.284| 15.898|    38|  4228.800| 111.284|   8,986|
| |Pike County|     1| 93.301|  0.000|   118| 11009.517| 399.861|  10,718|
| |Independence County|     1| 26.438|  0.000|   550| 14540.648| 441.885|  37,825|
| |Izard County|     1| 73.373|  0.000|    58|  4255.631| 136.264|  13,629|
| |Little River County|     1| 81.573|  0.000|   189| 15417.244| 337.944|  12,259|
| |Logan County|     1| 46.585|  0.000|   323| 15047.051| 765.330|  21,466|
| |Jackson County|     1| 59.812|  0.000|   117|  6998.026| 469.953|  16,719|
| |Dallas County|     1| 142.674| 20.382|    65|  9273.791| 122.292|   7,009|
| |Clark County|     1| 44.803|  0.000|   182|  8154.122| 76.805|  22,320|
| |Arkansas County|     1| 57.189|  0.000|   233| 13324.946| 196.075|  17,486|
| |Baxter County|     0|  0.000|  0.000|    76|  1812.458| 27.255|  41,932|
| |Prairie County|     0|  0.000|  0.000|   102| 12651.947| 425.276|   8,062|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 68.320|  10,455|
| |Monroe County|     0|  0.000|  0.000|    64|  9550.813| 255.825|   6,701|
| |Marion County|     0|  0.000|  0.000|    30|  1797.053| 34.230|  16,694|
| |Grant County|     0|  0.000|  0.000|   142|  7774.432| 93.856|  18,265|
| |Fulton County|     0|  0.000|  0.000|    44|  3526.489| 160.295|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    17|  3276.161| 110.123|   5,189|
| |Woodruff County|     0|  0.000|  0.000|    22|  3481.013| 45.208|   6,320|
| |Searcy County|     0|  0.000|  0.000|    32|  4060.398| 72.507|   7,881|
| |Scott County|     0|  0.000|  0.000|    68|  6614.143| 305.696|  10,281|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   420| 308.889| N/A| 6,886|  5064.311| N/A|1,359,711|
| |Hillsborough County|   280| 671.423|  0.343| 3,872|  9284.815| 24.322| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,703|  5497.645| 19.830| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   467|  3084.728|  7.549| 151,391|
| |Strafford County|    13| 99.515|  0.000|   363|  2778.777| 27.339| 130,633|
| |Belknap County|     4| 65.250|  0.000|   117|  1908.553|  9.321|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   103|  1353.749| 15.021|  76,085|
| |Carroll County|     1| 20.446|  0.000|    95|  1942.343| 11.683|  48,910|
| |Grafton County|     1| 11.125|  0.000|   105|  1168.146|  3.179|  89,886|
| |Sullivan County|     1| 23.177|  0.000|    44|  1019.793| 13.244|  43,146|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   396| 135.928| N/A|32,097| 11017.350| N/A|2,913,314|
| |Johnson County|   106| 175.963|  1.897| 6,009|  9975.083| 163.394| 602,401|
| |Wyandotte County|   102| 616.579|  3.454| 5,031| 30411.838| 308.289| 165,429|
| |Sedgwick County|    46| 89.140|  0.830| 5,068|  9820.906| 146.168| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,650|  9328.622| 142.958| 176,875|
| |Lyon County|    14| 421.750|  4.304|   716| 21569.513| 154.929|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,796| 49250.007| 148.863|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,093| 62256.462| 161.473|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,503| 18383.522| 103.092|  81,758|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 27.294|   5,234|
| |Coffey County|     8| 978.115|  0.000|    68|  8313.975| 17.466|   8,179|
| |Saline County|     7| 129.094|  5.269|   389|  7173.945| 71.133|  54,224|
| |Montgomery County|     5| 157.089|  0.000|   170|  5341.041| 35.906|  31,829|
| |Douglas County|     5| 40.897|  0.000|   765|  6257.208| 92.310| 122,259|
| |Riley County|     5| 67.356|  0.000|   489|  6587.456| 46.187|  74,232|
| |Seward County|     4| 186.672|  0.000| 1,243| 58008.214| 186.672|  21,428|
| |Sumner County|     3| 131.372|  0.000|   101|  4422.841| 18.767|  22,836|
| |Barton County|     3| 116.374|  0.000|   157|  6090.228| 171.790|  25,779|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 35.705|   8,002|
| |Cowley County|     2| 57.293|  0.000|   178|  5099.118| 73.663|  34,908|
| |Bourbon County|     2| 137.608|  0.000|    79|  5435.530| 58.975|  14,534|
| |Grant County|     2| 279.720|  0.000|   119| 16643.357| 439.560|   7,150|
| |Geary County|     2| 63.151|  0.000|   153|  4831.070| 103.748|  31,670|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Jackson County|     1| 75.924|  0.000|   155| 11768.279| 97.617|  13,171|
| |Jewell County|     1| 347.343| 49.620|    12|  4168.114| 99.241|   2,879|
| |Kearny County|     1| 260.552|  0.000|    63| 16414.799| 223.331|   3,838|
| |Labette County|     1| 50.974|  7.282|   149|  7595.066| 225.740|  19,618|
| |McPherson County|     1| 35.036|  0.000|   148|  5185.341| 55.057|  28,542|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 24.042|  11,884|
| |Nemaha County|     1| 97.742|  0.000|    49|  4789.366| 13.963|  10,231|
| |Reno County|     1| 16.130|  0.000|   390|  6290.526| 343.329|  61,998|
| |Crawford County|     1| 25.761|  0.000|   389| 10021.124| 44.162|  38,818|
| |Cherokee County|     1| 50.153|  0.000|   132|  6620.192| 293.753|  19,939|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199|  0.000|   1,994|
| |Dickinson County|     1| 54.154|  0.000|    50|  2707.679| 46.417|  18,466|
| |Harvey County|     1| 29.045|  0.000|   211|  6128.554| 174.272|  34,429|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090| 284.860|   2,006|
| |Stafford County|     1| 240.616| 34.374|     6|  1443.696| 103.121|   4,156|
| |Butler County|     1| 14.945|  0.000|   290|  4334.115| 132.372|  66,911|
| |Ellis County|     1| 35.023|  0.000|   145|  5078.275| 50.032|  28,553|
| |Franklin County|     1| 39.148|  0.000|   210|  8221.109| 212.518|  25,544|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 59.917|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   109|  4470.328| 17.577|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     8|  1247.272| 22.273|   6,414|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 16.757|   8,525|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Scott County|     0|  0.000|  0.000|    53| 10989.011| 562.780|   4,823|
| |Russell County|     0|  0.000|  0.000|    16|  2333.722| 62.510|   6,856|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Sherman County|     0|  0.000|  0.000|    16|  2704.073| 24.144|   5,917|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 20.611|   6,931|
| |Thomas County|     0|  0.000|  0.000|    44|  5657.709| 165.323|   7,777|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 26.045|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946| 57.748|  12,369|
| |Harper County|     0|  0.000|  0.000|    14|  2575.423| 105.119|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    39| 15360.378| 112.530|   2,539|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818|  0.000|   2,750|
| |Neosho County|     0|  0.000|  0.000|    65|  4060.723| 80.322|  16,007|
| |Morris County|     0|  0.000|  0.000|    13|  2313.167| 50.839|   5,620|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Miami County|     0|  0.000|  0.000|   150|  4381.225| 112.660|  34,237|
| |Meade County|     0|  0.000|  0.000|    52| 12893.628| 354.221|   4,033|
| |Marshall County|     0|  0.000|  0.000|    15|  1545.277| 88.302|   9,707|
| |Linn County|     0|  0.000|  0.000|    43|  4431.619| 103.061|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    20|  2796.421| 159.795|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    85|  4463.582| 75.018|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 71.644|   5,982|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024| 36.360|   7,858|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495|  0.000|   6,102|
| |Ottawa County|     0|  0.000|  0.000|    35|  6136.045| 75.135|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Osage County|     0|  0.000|  0.000|    46|  2884.193| 71.657|  15,949|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Gray County|     0|  0.000|  0.000|    84| 14028.056| 167.001|   5,988|
| |Graham County|     0|  0.000|  0.000|    17|  6849.315| 57.557|   2,482|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Atchison County|     0|  0.000|  0.000|    82|  5101.723| 177.760|  16,073|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 18.797|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Comanche County|     0|  0.000|  0.000|     7|  4117.647| 336.134|   1,700|
| |Cloud County|     0|  0.000|  0.000|    40|  4552.697| 162.596|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     4|  1505.457| 107.533|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Chase County|     0|  0.000|  0.000|    48| 18126.888| 323.694|   2,648|
| |Brown County|     0|  0.000|  0.000|    41|  4286.909| 89.622|   9,564|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   375| 88.910| N/A|22,022|  5221.283| N/A|4,217,737|
| |Multnomah County|    98| 120.563|  0.879| 5,056|  6220.052| 78.735| 812,855|
| |Marion County|    73| 209.880|  2.054| 3,005|  8639.576| 102.681| 347,818|
| |Clackamas County|    47| 112.390|  3.074| 1,595|  3814.083| 44.751| 418,187|
| |Umatilla County|    31| 397.691|  9.163| 2,342| 30044.901| 368.368|  77,950|
| |Washington County|    27| 44.881|  0.712| 3,202|  5322.544| 66.728| 601,592|
| |Malheur County|    14| 457.950|  9.346|   839| 27444.310| 579.447|  30,571|
| |Yamhill County|    13| 121.382|  1.334|   474|  4425.770| 93.371| 107,100|
| |Polk County|    12| 139.397|  0.000|   330|  3833.420| 48.125|  86,085|
| |Linn County|    11| 84.779|  1.101|   303|  2335.278| 44.041| 129,749|
| |Deschutes County|    10| 50.584|  1.445|   617|  3121.017| 44.803| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   421|  8426.404| 20.015|  49,962|
| |Benton County|     6| 64.479|  0.000|   178|  1912.888| 24.564|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   379| 15370.265| 272.296|  24,658|
| |Lane County|     3|  7.852|  0.000|   606|  1586.109| 24.678| 382,067|
| |Wasco County|     3| 112.435|  0.000|   195|  7308.298| 123.143|  26,682|
| |Morrow County|     3| 258.554| 12.312|   378| 32577.782| 627.916|  11,603|
| |Josephine County|     2| 22.861|  0.000|   128|  1463.075| 32.658|  87,487|
| |Union County|     2| 74.530|  0.000|   395| 14719.583| 15.971|  26,835|
| |Klamath County|     2| 29.309|  2.094|   204|  2989.537|  8.374|  68,238|
| |Jackson County|     2|  9.052|  0.647|   499|  2258.491| 50.433| 220,944|
| |Douglas County|     1|  9.011|  0.000|   159|  1432.691| 24.457| 110,980|
| |Crook County|     1| 40.977|  0.000|    50|  2048.844| 46.831|  24,404|
| |Wallowa County|     1| 138.735|  0.000|    20|  2774.695| 19.819|   7,208|
| |Curry County|     0|  0.000|  0.000|    17|   741.549| 18.695|  22,925|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582|  0.000|  27,036|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 160.514|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Hood River County|     0|  0.000|  0.000|   205|  8767.428| 164.962|  23,382|
| |Harney County|     0|  0.000|  0.000|    11|  1487.894| 19.323|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137|  4.431|  64,487|
| |Columbia County|     0|  0.000|  0.000|   102|  1948.275| 43.659|  52,354|
| |Clatsop County|     0|  0.000|  0.000|    89|  2212.609| 21.309|  40,224|
| |Baker County|     0|  0.000|  0.000|    42|  2604.813| 53.159|  16,124|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   356| 184.036| N/A|29,084| 15035.091| N/A|1,934,408|
| |Douglas County|   139| 243.293|  2.000|11,608| 20317.611| 183.283| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,755| 28604.958| 65.196|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,931| 96424.648| 164.072|  20,026|
| |Lancaster County|    19| 59.544|  0.895| 3,358| 10523.677| 79.691| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   100| 10725.011| 45.964|   9,324|
| |Adams County|    11| 350.732|  0.000|   362| 11542.263| 72.879|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,349| 12548.345| 160.260| 187,196|
| |Dodge County|    10| 273.486|  7.814|   822| 22480.514| 148.464|  36,565|
| |Dawson County|     9| 381.437|  0.000|   968| 41025.641| 102.927|  23,595|
| |Perkins County|     7| 2421.308| 296.487|    19|  6572.120| 98.829|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   305|  8563.086| 32.087|  35,618|
| |Madison County|     5| 142.454|  0.000|   466| 13276.732| 158.735|  35,099|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 158.203|   7,224|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747|  0.000|   6,445|
| |Gage County|     4| 185.934|  0.000|    93|  4322.968| 66.405|  21,513|
| |Custer County|     4| 371.161|  0.000|    52|  4825.090| 119.302|  10,777|
| |Colfax County|     4| 373.518|  0.000|   704| 65739.098| 106.719|  10,709|
| |Platte County|     3| 89.633|  0.000|   800| 23902.002| 93.901|  33,470|
| |Lincoln County|     2| 57.284|  0.000|   146|  4181.704| 212.768|  34,914|
| |Cass County|     2| 76.196|  0.000|   189|  7200.549| 141.507|  26,248|
| |Saunders County|     2| 92.687|  0.000|   165|  7646.677| 145.651|  21,578|
| |Saline County|     2| 140.607|  0.000|   597| 41971.316| 50.217|  14,224|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Richardson County|     1| 127.146|  0.000|    24|  3051.494| 72.655|   7,865|
| |Antelope County|     1| 158.781|  0.000|    21|  3334.392| 45.366|   6,298|
| |Buffalo County|     1| 20.137|  0.000|   456|  9182.626| 230.141|  49,659|
| |Fillmore County|     1| 183.083|  0.000|    27|  4943.244| 78.464|   5,462|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Washington County|     1| 48.242|  0.000|   131|  6319.649| 124.050|  20,729|
| |Seward County|     1| 57.857|  0.000|   125|  7232.122| 148.775|  17,284|
| |Pierce County|     0|  0.000|  0.000|    29|  4057.079| 219.842|   7,148|
| |Phelps County|     0|  0.000|  0.000|    41|  4538.410| 63.253|   9,034|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |Otoe County|     0|  0.000|  0.000|    56|  3497.377| 115.984|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    39|  5593.804| 327.842|   6,972|
| |Nance County|     0|  0.000|  0.000|     9|  2557.545| 40.596|   3,519|
| |Morrill County|     0|  0.000|  0.000|    63| 13571.736| 153.875|   4,642|
| |Merrick County|     0|  0.000|  0.000|    63|  8123.791| 110.528|   7,755|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    35|  4200.672| 34.291|   8,332|
| |Sherman County|     0|  0.000|  0.000|    12|  3998.667| 95.206|   3,001|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Stanton County|     0|  0.000|  0.000|    32|  5405.405| 96.525|   5,920|
| |Polk County|     0|  0.000|  0.000|    27|  5179.359| 27.404|   5,213|
| |Red Willow County|     0|  0.000|  0.000|    17|  1585.229| 13.321|  10,724|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759|  0.000|   1,357|
| |Sheridan County|     0|  0.000|  0.000|    11|  2096.836| 54.463|   5,246|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 28.554|   5,003|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 23.030|   6,203|
| |Cuming County|     0|  0.000|  0.000|    68|  7687.090| 48.448|   8,846|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 60.635|   2,356|
| |Johnson County|     0|  0.000|  0.000|    14|  2760.797| 28.171|   5,071|
| |Jefferson County|     0|  0.000|  0.000|    18|  2554.641| 81.100|   7,046|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 14.191|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 16.633|   8,589|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739|  0.000|   1,990|
| |Garfield County|     0|  0.000|  0.000|     4|  2031.488| 72.553|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Franklin County|     0|  0.000|  0.000|    13|  4363.880| 143.864|   2,979|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827|  0.000|   1,794|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |York County|     0|  0.000|  0.000|    87|  6360.114| 104.435|  13,679|
| |Wheeler County|     0|  0.000|  0.000|     2|  2554.278| 364.897|     783|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Wayne County|     0|  0.000|  0.000|    38|  4049.014| 15.222|   9,385|
| |Valley County|     0|  0.000|  0.000|    11|  2645.503| 34.357|   4,158|
| |Thomas County|     0|  0.000|  0.000|     2|  2770.083| 197.863|     722|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keith County|     0|  0.000|  0.000|    28|  3485.188| 160.034|   8,034|
| |Kearney County|     0|  0.000|  0.000|    62|  9545.804| 417.904|   6,495|
| |Chase County|     0|  0.000|  0.000|     7|  1783.894| 36.406|   3,924|
| |Cedar County|     0|  0.000|  0.000|    23|  2737.443| 17.003|   8,402|
| |Butler County|     0|  0.000|  0.000|    63|  7859.281| 106.929|   8,016|
| |Burt County|     0|  0.000|  0.000|    41|  6347.732| 331.763|   6,459|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Boyd County|     0|  0.000|  0.000|     6|  3126.628| 372.218|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    14|  1298.340| 39.745|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832| 27.515|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   290| 90.457| N/A|35,849| 11181.993| N/A|3,205,958|
| |Salt Lake County|   202| 174.072|  2.093|21,034| 18125.930| 142.680|1,160,437|
| |Utah County|    37| 58.155|  0.225| 8,983| 14118.997| 159.869| 636,235|
| |San Juan County|    25| 1633.133|  0.000|   650| 42461.458| 167.979|  15,308|
| |Davis County|    21| 59.075|  1.206| 3,294|  9266.318| 80.374| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   583| 17101.288| 188.571|  34,091|
| |Summit County|     1| 23.728|  0.000|   717| 17012.694| 54.235|  42,145|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Tooele County|     0|  0.000|  0.000|   588|  8137.395| 47.448|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   246| 137.656| N/A|26,129| 14621.181| N/A|1,787,065|
| |Ada County|    85| 176.500|  4.153| 9,425| 19570.711| 299.605| 481,587|
| |Canyon County|    51| 221.885|  4.972| 6,064| 26382.538| 537.620| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,464| 16851.217| 297.626|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   162|  4009.107| 84.849|  40,408|
| |Kootenai County|    16| 96.562|  1.724| 1,922| 11599.486| 218.988| 165,697|
| |Jerome County|     6| 245.781|  0.000|   499| 20440.767| 292.596|  24,412|
| |Blaine County|     6| 260.632|  0.000|   578| 25107.511| 31.028|  23,021|
| |Bonneville County|     4| 33.596|  2.400| 1,176|  9877.207| 381.554| 119,062|
| |Payette County|     3| 125.256|  5.965|   417| 17410.547| 375.767|  23,951|
| |Owyhee County|     3| 253.743| 12.083|   269| 22752.263| 338.324|  11,823|
| |Elmore County|     3| 109.047|  0.000|   218|  7924.103| 83.084|  27,511|
| |Washington County|     3| 294.291|  0.000|   217| 21287.032| 294.291|  10,194|
| |Bingham County|     2| 42.725|  0.000|   297|  6344.663| 225.832|  46,811|
| |Bannock County|     2| 22.777|  0.000|   443|  5045.098| 136.662|  87,808|
| |Shoshone County|     2| 155.255|  0.000|   132| 10246.856| 565.573|  12,882|
| |Minidoka County|     2| 95.062|  0.000|   486| 23099.957| 183.333|  21,039|
| |Cassia County|     1| 41.615|  0.000|   532| 22138.993| 202.128|  24,030|
| |Benewah County|     1| 107.550| 15.364|    77|  8281.351| 276.557|   9,298|
| |Boise County|     1| 127.698|  0.000|    51|  6512.578| 145.940|   7,831|
| |Valley County|     1| 87.781|  0.000|    66|  5793.539| 150.482|  11,392|
| |Gem County|     1| 55.212|  0.000|   183| 10103.799| 141.974|  18,112|
| |Gooding County|     1| 65.880|  0.000|   174| 11463.206| 235.287|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   219|  7331.526| 263.036|  29,871|
| |Teton County|     0|  0.000|  0.000|    86|  7082.853| 235.311|  12,142|
| |Power County|     0|  0.000|  0.000|    62|  8071.866| 148.790|   7,681|
| |Boundary County|     0|  0.000|  0.000|    38|  3103.307| 46.666|  12,245|
| |Adams County|     0|  0.000|  0.000|    20|  4657.662| 66.538|   4,294|
| |Bonner County|     0|  0.000|  0.000|   189|  4132.141| 78.083|  45,739|
| |Oneida County|     0|  0.000|  0.000|    16|  3531.229| 94.586|   4,531|
| |Madison County|     0|  0.000|  0.000|   175|  4385.196| 110.972|  39,907|
| |Lincoln County|     0|  0.000|  0.000|    59| 10995.155| 133.113|   5,366|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Lemhi County|     0|  0.000|  0.000|    35|  4360.284| 391.536|   8,027|
| |Latah County|     0|  0.000|  0.000|   113|  2817.393| 71.236|  40,108|
| |Idaho County|     0|  0.000|  0.000|    33|  1979.960| 25.714|  16,667|
| |Fremont County|     0|  0.000|  0.000|    89|  6794.412| 218.119|  13,099|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 20.591|  13,876|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 132.428|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|     9| 10650.888| 338.123|     845|
| |Caribou County|     0|  0.000|  0.000|    33|  4612.159| 99.830|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Bear Lake County|     0|  0.000|  0.000|    20|  3265.306| 209.913|   6,125|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   153| 85.372| N/A| 8,018|  4473.963| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  1.604|   976|  5479.329| 96.241| 178,124|
| |Jackson County|    19| 664.894|  0.000|   166|  5809.071| 39.994|  28,576|
| |Mercer County|    16| 272.303| 31.607|   209|  3556.962| 87.526|  58,758|
| |Berkeley County|    11| 92.304|  0.000|   713|  5982.999| 51.547| 119,171|
| |Wayne County|     9| 228.415|  0.000|   214|  5431.196| 72.513|  39,402|
| |Logan County|     7| 218.620| 17.847|   264|  8245.104| 455.087|  32,019|
| |Fayette County|     7| 165.071|  6.738|   155|  3655.143| 70.745|  42,406|
| |Wood County|     5| 59.867|  0.000|   264|  3160.995| 41.052|  83,518|
| |Mingo County|     5| 213.456| 12.198|   183|  7812.500| 182.963|  23,424|
| |Monongalia County|     5| 47.343|  0.000|   953|  9023.596| 32.464| 105,612|
| |Ohio County|     4| 96.593|  0.000|   272|  6568.303| 31.048|  41,411|
| |Mineral County|     4| 148.876|  0.000|   127|  4726.813| 58.487|  26,868|
| |Jefferson County|     4| 69.996|  0.000|   299|  5232.212| 17.499|  57,146|
| |Grant County|     4| 345.781| 37.048|   129| 11151.452| 493.974|  11,568|
| |Preston County|     4| 119.646|  0.000|   125|  3738.933|  0.000|  33,432|
| |Greenbrier County|     3| 86.550|  0.000|    93|  2683.053| 20.607|  34,662|
| |Cabell County|     3| 32.628|  1.554|   428|  4654.957| 102.546|  91,945|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097|  8.981|  15,907|
| |Marion County|     2| 35.668|  0.000|   193|  3442.003| 35.668|  56,072|
| |Wyoming County|     2| 98.068|  7.005|    37|  1814.259| 91.063|  20,394|
| |Brooke County|     1| 45.581|  0.000|    70|  3190.665| 52.092|  21,939|
| |Nicholas County|     1| 40.823|  0.000|    40|  1632.920| 40.823|  24,496|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Roane County|     1| 73.057|  0.000|    16|  1168.907| 20.873|  13,688|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  4.679|  30,531|
| |Mason County|     1| 37.713|  0.000|    66|  2489.063| 80.814|  26,516|
| |Hampshire County|     1| 43.150|  0.000|    80|  3451.996| 30.821|  23,175|
| |Harrison County|     1| 14.869|  0.000|   235|  3494.112| 65.846|  67,256|
| |Pendleton County|     1| 143.493|  0.000|    42|  6026.690|  0.000|   6,969|
| |Raleigh County|     1| 13.631|  0.000|   267|  3639.536| 116.839|  73,361|
| |Taylor County|     1| 59.898|  0.000|    59|  3533.992| 34.228|  16,695|
| |Pleasants County|     1| 134.048| 19.150|    14|  1876.676| 95.749|   7,460|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Wetzel County|     0|  0.000|  0.000|    44|  2920.677| 28.448|  15,065|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  5.909|  24,176|
| |Randolph County|     0|  0.000|  0.000|   211|  7353.197| 19.914|  28,695|
| |Summers County|     0|  0.000|  0.000|    15|  1193.033| 90.898|  12,573|
| |Gilmer County|     0|  0.000|  0.000|    17|  2173.079| 18.261|   7,823|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 33.820|   8,448|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Tucker County|     0|  0.000|  0.000|    10|  1462.202|  0.000|   6,839|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |McDowell County|     0|  0.000|  0.000|    64|  3631.412| 129.693|  17,624|
| |Morgan County|     0|  0.000|  0.000|    30|  1677.477| 31.952|  17,884|
| |Hardy County|     0|  0.000|  0.000|    61|  4427.991| 72.590|  13,776|
| |Lincoln County|     0|  0.000|  0.000|    95|  4654.809| 139.994|  20,409|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 29.752|  28,810|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Boone County|     0|  0.000|  0.000|   109|  5079.927| 113.183|  21,457|
| |Putnam County|     0|  0.000|  0.000|   203|  3596.103| 73.390|  56,450|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 49.886|   8,591|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   147| 166.166| N/A| 9,815| 11094.670| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  2.959| 4,498| 23289.530| 157.552| 193,134|
| |Pennington County|    32| 281.257|  3.767|   910|  7998.242| 65.292| 113,775|
| |Beadle County|     9| 487.726|  0.000|   594| 32189.888| 54.192|  18,453|
| |Todd County|     5| 491.304| 14.037|    73|  7173.037| 84.224|  10,177|
| |Union County|     4| 251.067|  0.000|   217| 13620.387| 116.567|  15,932|
| |Brown County|     3| 77.242|  0.000|   452| 11637.787| 121.380|  38,839|
| |Lyman County|     3| 793.441| 37.783|    90| 23803.227| 75.566|   3,781|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556|  0.000|   1,962|
| |Lincoln County|     2| 32.718|  0.000|   667| 10911.530| 184.624|  61,128|
| |Hughes County|     2| 114.116|  0.000|    93|  5306.402| 73.360|  17,526|
| |Oglala Lakota County|     2| 141.074| 10.077|   156| 11003.738| 40.307|  14,177|
| |Lake County|     2| 156.287|  0.000|    95|  7423.615| 100.470|  12,797|
| |Yankton County|     2| 87.665|  0.000|   125|  5479.092| 131.498|  22,814|
| |Meade County|     1| 35.296|  0.000|    97|  3423.691| 75.634|  28,332|
| |Roberts County|     1| 96.209|  0.000|    80|  7696.748| 123.698|  10,394|
| |Davison County|     1| 50.569|  0.000|    96|  4854.614| 21.672|  19,775|
| |Brookings County|     1| 28.509|  0.000|   142|  4048.237| 81.453|  35,077|
| |Butte County|     1| 95.886|  0.000|    18|  1725.956| 82.188|  10,429|
| |Faulk County|     1| 434.972|  0.000|    28| 12179.208| 124.278|   2,299|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474|  0.000|   3,344|
| |McCook County|     1| 179.019|  0.000|    30|  5370.569| 102.297|   5,586|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |Codington County|     1| 35.703|  0.000|   143|  5105.502| 102.008|  28,009|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Grant County|     0|  0.000|  0.000|    27|  3828.701| 81.031|   7,052|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 42.561|   6,713|
| |Edmunds County|     0|  0.000|  0.000|    18|  4700.966| 186.546|   3,829|
| |Douglas County|     0|  0.000|  0.000|    19|  6504.622| 146.721|   2,921|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 1347.709|   2,756|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Turner County|     0|  0.000|  0.000|    53|  6321.565| 68.157|   8,384|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    24|  3893.576| 185.408|   6,164|
| |Hand County|     0|  0.000|  0.000|     9|  2820.432| 89.538|   3,191|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668|  0.000|   3,453|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Marshall County|     0|  0.000|  0.000|    10|  2026.342| 57.895|   4,935|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 60.049|   2,379|
| |Lawrence County|     0|  0.000|  0.000|    62|  2399.009| 149.247|  25,844|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582|  0.000|   4,939|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     4|  3074.558| 109.806|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    30|  4114.662| 58.781|   7,291|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Spink County|     0|  0.000|  0.000|    26|  4077.792| 89.622|   6,376|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Dewey County|     0|  0.000|  0.000|    49|  8316.361|  0.000|   5,892|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Charles Mix County|     0|  0.000|  0.000|   103| 11084.804| 46.123|   9,292|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233|  0.000|   1,376|
| |Brule County|     0|  0.000|  0.000|    46|  8684.161| 26.969|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159|  0.000|   2,751|
| |Corson County|     0|  0.000|  0.000|    37|  9055.311| 244.738|   4,086|
| |Clay County|     0|  0.000|  0.000|   132|  9381.663| 121.840|  14,070|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Deuel County|     0|  0.000|  0.000|    11|  2528.154| 65.666|   4,351|
| |Day County|     0|  0.000|  0.000|    23|  4240.413| 52.676|   5,424|
| |Custer County|     0|  0.000|  0.000|    36|  4012.483| 206.993|   8,972|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   126| 93.735| N/A| 4,069|  3027.052| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,097|  7108.402| 15.012| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    13| 62.608|  0.688|   680|  3274.883|  9.632| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   171|  1398.178|  2.336| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   568|  5245.805| 25.068| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   153|  1005.600|  2.817| 152,148|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  0.000|  39,772|
| |Hancock County|     1| 18.186|  0.000|    37|   672.886|  2.598|  54,987|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  8.250|  34,634|
| |Piscataquis County|     0|  0.000|  0.000|     4|   238.308|  8.511|  16,785|
| |Washington County|     0|  0.000|  0.000|    13|   414.290|  4.553|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    56|  1561.803|  7.968|  35,856|
| |Oxford County|     0|  0.000|  0.000|    55|   948.685|  2.464|  57,975|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   120| 157.468| N/A| 7,950| 10432.222| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,073| 16891.762| 90.305| 181,923|
| |Burleigh County|     8| 83.659|  4.482| 1,255| 13124.046| 307.747|  95,626|
| |Grand Forks County|     7| 100.790|  2.057|   710| 10223.035| 123.417|  69,451|
| |Stark County|     5| 158.786|  9.073|   300|  9527.136| 331.181|  31,489|
| |Morton County|     4| 127.535|  4.555|   407| 12976.661| 501.029|  31,364|
| |Stutsman County|     3| 144.900|  6.900|   128|  6182.380| 48.300|  20,704|
| |Ramsey County|     2| 173.626|  0.000|    75|  6510.982| 124.019|  11,519|
| |Benson County|     2| 292.740| 20.910|   145| 21223.653| 313.650|   6,832|
| |Williams County|     2| 53.207|  0.000|   288|  7661.816| 155.821|  37,589|
| |McIntosh County|     2| 800.961| 57.212|    39| 15618.742| 686.538|   2,497|
| |McKenzie County|     2| 133.120|  9.509|    91|  6056.976| 66.560|  15,024|
| |Richland County|     1| 61.816|  8.831|   113|  6985.226| 105.971|  16,177|
| |Griggs County|     1| 448.229|  0.000|    35| 15688.032| 320.164|   2,231|
| |Emmons County|     1| 308.547|  0.000|    18|  5553.841| 44.078|   3,241|
| |Mountrail County|     1| 94.832|  0.000|   141| 13371.266| 257.400|  10,545|
| |McHenry County|     1| 174.064|  0.000|    17|  2959.095| 49.733|   5,745|
| |Ward County|     1| 14.784|  0.000|   238|  3518.576| 86.592|  67,641|
| |Sioux County|     1| 236.407|  0.000|    89| 21040.189| 1013.171|   4,230|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Golden Valley County|     0|  0.000|  0.000|     6|  3407.155| 162.245|   1,761|
| |Kidder County|     0|  0.000|  0.000|    18|  7258.065| 345.622|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 35.308|   4,046|
| |Eddy County|     0|  0.000|  0.000|    19|  8307.827| 124.930|   2,287|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784|  0.000|   1,850|
| |Foster County|     0|  0.000|  0.000|    26|  8099.688| 133.511|   3,210|
| |Dunn County|     0|  0.000|  0.000|    31|  7007.233| 32.291|   4,424|
| |Divide County|     0|  0.000|  0.000|     3|  1325.088| 126.199|   2,264|
| |Mercer County|     0|  0.000|  0.000|    31|  3786.491| 122.145|   8,187|
| |Dickey County|     0|  0.000|  0.000|    13|  2668.309| 29.322|   4,872|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Bowman County|     0|  0.000|  0.000|    11|  3637.566| 236.206|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Barnes County|     0|  0.000|  0.000|    38|  3648.584| 27.433|  10,415|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |McLean County|     0|  0.000|  0.000|    79|  8359.788| 559.335|   9,450|
| |Nelson County|     0|  0.000|  0.000|    26|  9030.914| 198.482|   2,879|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Walsh County|     0|  0.000|  0.000|   106|  9961.470| 67.126|  10,641|
| |Wells County|     0|  0.000|  0.000|    23|  5998.957| 111.782|   3,834|
| |Traill County|     0|  0.000|  0.000|    57|  7093.081| 142.217|   8,036|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Steele County|     0|  0.000|  0.000|    15|  7936.508| 151.172|   1,890|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 325.910|   1,315|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    82|  5784.424| 443.405|  14,176|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641| 61.391|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Pierce County|     0|  0.000|  0.000|    13|  3270.440| 71.878|   3,975|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    80| 74.852| N/A| 5,268|  4928.994| N/A|1,068,778|
| |Yellowstone County|    31| 192.188|  3.543| 1,387|  8598.884| 215.216| 161,300|
| |Big Horn County|    14| 1051.130| 32.177|   464| 34837.450| 954.598|  13,319|
| |Toole County|     6| 1266.892|  0.000|    44|  9290.541| 241.313|   4,736|
| |Cascade County|     4| 49.161|  3.511|   167|  2052.454| 14.046|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   959|  8380.376| 89.883| 114,434|
| |Flathead County|     3| 28.900|  1.376|   357|  3439.108| 111.472| 103,806|
| |Richland County|     2| 185.134|  0.000|    47|  4350.643|  0.000|  10,803|
| |Ravalli County|     2| 45.656|  3.261|    83|  1894.718| 29.350|  43,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 37.587|  11,402|
| |Hill County|     2| 121.330| 17.333|    46|  2790.585| 43.332|  16,484|
| |Lincoln County|     2| 100.100|  0.000|    77|  3853.854| 28.600|  19,980|
| |Lewis and Clark County|     2| 28.805|  2.058|   163|  2347.621| 32.920|  69,432|
| |Missoula County|     1|  8.361|  0.000|   336|  2809.365| 82.418| 119,600|
| |Stillwater County|     1| 103.713| 14.816|    28|  2903.962| 118.529|   9,642|
| |Rosebud County|     1| 111.894|  0.000|    53|  5930.402| 351.668|   8,937|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972|  0.000|   3,737|
| |Glacier County|     1| 72.711|  0.000|    77|  5598.778| 176.585|  13,753|
| |Lake County|     1| 32.832|  0.000|   184|  6041.106| 65.664|  30,458|
| |Madison County|     1| 116.279|  0.000|    83|  9651.163| 83.056|   8,600|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Roosevelt County|     0|  0.000|  0.000|    24|  2181.025| 51.929|  11,004|
| |Sanders County|     0|  0.000|  0.000|    10|   825.559| 11.794|  12,113|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 43.172|   3,309|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Valley County|     0|  0.000|  0.000|    23|  3109.789| 193.155|   7,396|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Silver Bow County|     0|  0.000|  0.000|   102|  2921.380| 110.472|  34,915|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Deer Lodge County|     0|  0.000|  0.000|    26|  2844.639| 46.890|   9,140|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 76.055|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Carbon County|     0|  0.000|  0.000|    74|  6899.767| 186.480|  10,725|
| |Blaine County|     0|  0.000|  0.000|    13|  1945.816| 64.148|   6,681|
| |Broadwater County|     0|  0.000|  0.000|    14|  2244.669| 68.714|   6,237|
| |Beaverhead County|     0|  0.000|  0.000|    65|  6876.124| 120.899|   9,453|
| |Jefferson County|     0|  0.000|  0.000|    29|  2372.965| 23.379|  12,221|
| |Granite County|     0|  0.000|  0.000|    17|  5031.074| 169.112|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 257.555|   1,664|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Dawson County|     0|  0.000|  0.000|    20|  2322.071| 66.345|   8,613|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |Fergus County|     0|  0.000|  0.000|    14|  1266.968| 77.569|  11,050|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 24.168|   5,911|
| |Phillips County|     0|  0.000|  0.000|    68| 17197.774| 2276.176|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    57|  3432.494| 25.808|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,470|  2355.811| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   735|  4487.892| 10.467| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  0.000|  49,402|
| |Windham County|     3| 71.053|  0.000|   104|  2463.171|  6.767|  42,222|
| |Addison County|     2| 54.382|  0.000|    74|  2012.127|  3.884|  36,777|
| |Washington County|     2| 34.241|  0.000|    57|   975.877| 12.229|  58,409|
| |Windsor County|     2| 36.323|  0.000|    73|  1325.778|  5.189|  55,062|
| |Bennington County|     1| 28.193|  0.000|    90|  2537.356| 24.165|  35,470|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Rutland County|     1| 17.185|  0.000|   100|  1718.479| 19.640|  58,191|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|
| |Orange County|     0|  0.000|  0.000|    15|   519.175|  4.945|  28,892|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    37| 26.132| N/A| 3,935|  2779.206| N/A|1,415,872|
| |Honolulu County|    31| 31.809| N/A| 3,558|  3650.867| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   191|  1140.864| 11.946| 167,417|
| |Kauai County|     0|  0.000|  0.000|    51|   705.462|  7.904|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   135|   669.932|  9.216| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,086|  5332.099| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    24|  2841.918| 33.832|   8,445|
| |Lincoln County|     0|  0.000|  0.000|   100|  5042.864| 21.612|  19,830|
| |Laramie County|     0|  0.000|  0.000|   504|  5065.327| 21.536|  99,500|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Washakie County|     0|  0.000|  0.000|    82| 10506.086| 439.279|   7,805|
| |Natrona County|     0|  0.000|  0.000|   238|  2980.290| 21.467|  79,858|
| |Park County|     0|  0.000|  0.000|   135|  4624.238| 53.827|  29,194|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    73|  2394.620| 42.175|  30,485|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762| 14.531|   9,831|
| |Sweetwater County|     0|  0.000|  0.000|   266|  6282.030| 47.233|  42,343|
| |Teton County|     0|  0.000|  0.000|   373| 15896.693| 60.884|  23,464|
| |Uinta County|     0|  0.000|  0.000|   278| 13744.685| 70.630|  20,226|
| |Fremont County|     0|  0.000|  0.000|   500| 12735.284| 14.555|  39,261|
| |Albany County|     0|  0.000|  0.000|    89|  2289.095|  3.674|  38,880|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Campbell County|     0|  0.000|  0.000|   132|  2848.450| 43.158|  46,341|
| |Converse County|     0|  0.000|  0.000|    31|  2242.801|  0.000|  13,822|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565|  0.000|   7,584|
| |Goshen County|     0|  0.000|  0.000|    34|  2573.613| 129.762|  13,211|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 129.488|   4,413|
| |Carbon County|     0|  0.000|  0.000|   105|  7094.595| 164.093|  14,800|
| |Weston County|     0|  0.000|  0.000|     5|   721.813|  0.000|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|


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


