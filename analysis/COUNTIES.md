# Analysis of US By County #

Updated: at 2020-08-14

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 133,566 deaths (462.707 deaths/million) and 4,511,190 confirmed cases (15627.929 confirmed cases/million).  This group accounts for 81.12% of all US deaths and for 87.47% of all US cases.

24.43% of this group's deaths (19.82% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.33% of this group's deaths (20.55% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,435 (12.66% of the total US population):



The next 25.19% of this group's deaths (20.43% of the total US deaths) occured in 91 counties in 31 states with a combined population of 68,516,099 (20.87% of the total US population)

The remaining 25.05% of this group's deaths (20.32% of the total US deaths) occured in 852 counties in 50 states with a combined population of 141,290,307 (43.04% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,608 deaths (268.031 deaths/million) and 476,655 confirmed cases (12043.596 confirmed cases/million).  This group accounts for 6.44% of all US deaths and for 9.24% of all US cases.

24.76% of this group's deaths (1.60% of the total US deaths) occured in 60 counties in 16 states with a combined population of 2,015,518 (0.61% of the total US population):



The next 25.21% of this group's deaths (1.62% of the total US deaths) occured in 117 counties in 28 states with a combined population of 3,483,709 (1.06% of the total US population):



The next 24.99% of this group's deaths (1.61% of the total US deaths) occured in 236 counties in 34 states with a combined population of 5,754,615 (1.75% of the total US population)

The remaining 25.04% of this group's deaths (1.61% of the total US deaths) occured in 1,739 counties in 47 states with a combined population of 28,323,622 (8.63% of the total US population) 

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
|NJ|21 counties|15,893| 1789.311| N/A|185,655| 20901.940| N/A|8,882,190|
| |Essex County| 2,110| 2640.884|  0.536|19,840| 24831.816| 35.045| 798,975|
| |Bergen County| 2,035| 2183.003|  0.000|20,940| 22462.943| 41.530| 932,202|
| |Hudson County| 1,508| 2242.743|  1.275|19,792| 29435.254| 45.042| 672,391|
| |Middlesex County| 1,411| 1710.175|  1.731|18,015| 21834.723| 33.591| 825,062|
| |Union County| 1,349| 2424.772|  0.257|16,812| 30218.877| 48.788| 556,341|
| |Passaic County| 1,242| 2474.961|  0.854|17,801| 35472.455| 61.490| 501,826|
| |Ocean County| 1,020| 1679.881|  0.941|10,668| 17569.575| 27.527| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,407| 16818.171| 41.555| 618,795|
| |Morris County|   829| 1685.490|  0.581| 7,304| 14850.207| 27.593| 491,845|
| |Mercer County|   622| 1692.839|  1.555| 8,164| 22219.198| 29.938| 367,430|
| |Camden County|   580| 1145.179|  0.564| 8,689| 17155.967| 63.464| 506,471|
| |Somerset County|   564| 1714.630|  0.869| 5,282| 16057.933| 28.230| 328,934|
| |Burlington County|   474| 1064.334|  0.962| 6,094| 13683.650| 53.570| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,521| 13353.813| 42.802| 263,670|
| |Gloucester County|   214| 733.791|  2.449| 3,339| 11449.204| 71.518| 291,636|
| |Sussex County|   198| 1409.373|  1.017| 1,343|  9559.535| 23.388| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,352| 12843.531| 17.642| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,386| 22644.740| 73.565| 149,527|
| |Hunterdon County|   124| 997.017|  0.000| 1,151|  9254.569|  8.040| 124,371|
| |Cape May County|    88| 956.116|  1.552|   843|  9159.161| 31.043|  92,039|
| |Salem County|    87| 1394.566|  0.000|   912| 14618.899| 59.538|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,324| 633.514| N/A|253,959| 13054.629| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,795| 32275.205| 27.478|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.000|43,987| 29789.361| 34.539|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.000|36,357| 37578.062| 36.914| 967,506|
| |Queens County|   985| 437.190|  0.938| 7,915|  3511.584| 18.936|2,253,858|
| |Kings County|   931| 363.775|  0.781| 1,358|   530.616|  2.861|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,973| 42889.723| 24.117| 325,789|
| |Erie County|   671| 730.378|  0.000| 9,033|  9832.350| 46.028| 918,702|
| |Bronx County|   650| 458.061|  0.983|26,953| 19005.254| 102.486|1,418,207|
| |Orange County|   491| 1275.523|  0.000|11,210| 29121.422| 30.803| 384,940|
| |New York County|   415| 254.624|  0.546|15,545|  9544.440| 51.468|1,628,706|
| |Monroe County|   285| 384.216|  0.000| 5,079|  6847.136| 40.636| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,627|  7875.743| 28.539| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,640| 15770.619| 28.162| 294,218|
| |Richmond County|   148| 311.186|  0.668| 7,915| 16622.342| 89.636| 476,143|
| |Albany County|   128| 418.977|  0.000| 2,636|  8628.308| 33.200| 305,506|
| |Oneida County|   115| 502.906|  0.000| 2,183|  9546.466| 41.232| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,518|  7253.406| 32.765| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,081| 11719.124| 28.962| 177,573|
| |Broome County|    69| 362.228|  0.000| 1,153|  6052.875| 44.247| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,455| 14798.617| 15.983|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   299|  7409.794|  7.081|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,491| 19766.147| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   301|  3155.831|  5.991|  95,379|
| |Columbia County|    37| 622.257|  0.000|   550|  9249.760| 38.441|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,084|  6980.084| 31.276| 155,299|
| |Ontario County|    34| 309.719|  0.000|   365|  3324.922| 13.013| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269| 17.873|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   782|  4927.102| 21.602| 158,714|
| |Tioga County|    25| 518.640|  0.000|   194|  4024.646|  2.964|  48,203|
| |Fulton County|    24| 449.581|  0.000|   300|  5619.767| 24.085|  53,383|
| |Greene County|    18| 381.453|  0.000|   296|  6272.781| 18.164|  47,188|
| |Madison County|    17| 239.636|  0.000|   417|  5878.124| 16.110|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   774|  3367.223| 16.780| 229,863|
| |Washington County|    14| 228.743|  0.000|   260|  4248.088|  9.336|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   260|  2048.809| 18.012| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470|  6.812|  62,914|
| |Yates County|     7| 280.978|  0.000|    58|  2328.102| 11.468|  24,913|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959| 18.157|  47,207|
| |Cattaraugus County|     6| 78.826|  0.000|   169|  2220.266|  9.384|  76,117|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436| 10.752|  39,859|
| |Genesee County|     5| 87.291|  0.000|   280|  4888.268| 14.964|  57,280|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  7.204|  59,493|
| |Montgomery County|     4| 81.266|  0.000|   179|  3636.659| 29.024|  49,221|
| |Clinton County|     4| 49.699|  0.000|   129|  1602.783|  3.550|  80,485|
| |Herkimer County|     4| 65.233|  0.000|   278|  4533.668| 23.297|  61,319|
| |Delaware County|     4| 90.631|  0.000|   107|  2424.380|  9.710|  44,135|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  0.000| 107,740|
| |Seneca County|     3| 88.194|  0.000|    92|  2704.610| 25.198|  34,016|
| |Wayne County|     3| 33.364|  0.000|   263|  2924.887| 22.242|  89,918|
| |Oswego County|     3| 25.614|  0.000|   258|  2202.794|  8.538| 117,124|
| |Chemung County|     3| 35.947|  0.000|   184|  2204.755| 32.524|  83,456|
| |Cayuga County|     2| 26.118|  0.000|   162|  2115.545| 20.521|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697|  6.199|  46,091|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  2.796| 102,180|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594|  0.000|   4,416|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  0.000|  30,999|
| |Lewis County|     0|  0.000|  0.000|    47|  1787.344| 43.461|  26,296|
| |Jefferson County|     0|  0.000|  0.000|   142|  1292.860|  2.601| 109,834|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525|  5.712|  50,022|
| |Essex County|     0|  0.000|  0.000|    56|  1518.232|  3.873|  36,885|
| |Cortland County|     0|  0.000|  0.000|    97|  2038.629|  9.007|  47,581|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,870| 275.105| N/A|597,984| 15134.152| N/A|39,512,223|
| |Los Angeles County| 5,113| 509.308|  3.472|214,425| 21358.971| 188.193|10,039,107|
| |Riverside County|   853| 345.268|  4.799|43,983| 17802.947| 245.290|2,470,546|
| |Orange County|   769| 242.152|  3.239|42,171| 13279.310| 155.647|3,175,692|
| |San Diego County|   608| 182.127|  1.070|33,393| 10002.906| 96.969|3,338,330|
| |San Bernardino County|   555| 254.577|  4.259|38,290| 17563.535| 239.506|2,180,085|
| |Imperial County|   257| 1418.205| 13.402| 9,957| 54945.783| 280.645| 181,215|
| |San Joaquin County|   245| 321.460|  9.934|14,276| 18731.270| 404.308| 762,148|
| |Alameda County|   216| 129.238|  0.855|14,548|  8704.450| 142.231|1,671,329|
| |Santa Clara County|   207| 107.373|  0.815|13,059|  6773.860| 127.677|1,927,852|
| |Tulare County|   205| 439.730|  2.758|11,847| 25412.113| 463.632| 466,195|
| |Sacramento County|   194| 124.995|  3.590|13,216|  8515.146| 245.941|1,552,058|
| |Fresno County|   191| 191.172|  4.862|18,344| 18360.506| 245.792| 999,101|
| |Kern County|   187| 207.731|  5.554|25,499| 28325.865| 599.072| 900,202|
| |Stanislaus County|   182| 330.512|  8.042|11,592| 21051.102| 566.593| 550,660|
| |Contra Costa County|   151| 130.903|  2.105|10,482|  9086.921| 241.496|1,153,526|
| |San Mateo County|   122| 159.150|  0.373| 6,640|  8661.928| 139.582| 766,573|
| |Ventura County|    93| 109.928|  2.364| 8,790| 10389.997| 141.336| 846,006|
| |Marin County|    81| 312.952|  1.656| 5,583| 21570.476| 211.946| 258,826|
| |Merced County|    74| 266.494|  6.174| 6,224| 22414.290| 704.305| 277,680|
| |Santa Barbara County|    73| 163.494|  1.600| 7,083| 15863.417| 137.898| 446,499|
| |San Francisco County|    67| 76.003| N/A| 7,944|  9011.411| N/A| 881,549|
| |Kings County|    62| 405.388|  5.604| 5,127| 33522.950| 629.565| 152,940|
| |Sonoma County|    51| 103.169|  2.601| 3,859|  7806.431| 188.131| 494,336|
| |Yolo County|    45| 204.082|  1.944| 1,918|  8698.413| 167.153| 220,500|
| |Madera County|    44| 279.672|  7.264| 2,759| 17536.723| 500.323| 157,327|
| |Solano County|    41| 91.591|  0.638| 4,414|  9860.536| 145.205| 447,643|
| |Monterey County|    40| 92.153|  1.646| 5,803| 13369.089| 224.787| 434,061|
| |Placer County|    27| 67.783|  2.510| 2,486|  6241.072| 160.313| 398,329|
| |San Luis Obispo County|    18| 63.579|  1.009| 2,324|  8208.794| 139.774| 283,111|
| |Napa County|    11| 79.858|  2.074| 1,142|  8290.742| 121.343| 137,744|
| |Mendocino County|    10| 115.275|  0.000|   489|  5636.953| 207.495|  86,749|
| |Amador County|    10| 251.560| 35.937|   198|  4980.881| 150.936|  39,752|
| |Shasta County|    10| 55.531|  0.793|   476|  2643.270| 51.564| 180,080|
| |Butte County|     8| 36.499|  0.000| 1,305|  5953.847| 159.682| 219,186|
| |Sutter County|     7| 72.187|  1.473| 1,041| 10735.168| 218.033|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,357|  4966.821| 75.294| 273,213|
| |Inyo County|     5| 277.177| 31.677|   115|  6375.076| 245.500|  18,039|
| |Colusa County|     5| 232.051|  6.630|   401| 18610.479| 265.201|  21,547|
| |Humboldt County|     4| 29.508|  0.000|   299|  2205.698| 20.023| 135,558|
| |San Benito County|     4| 63.686|  0.000|   773| 12307.349| 168.313|  62,808|
| |Yuba County|     4| 50.847|  0.000|   688|  8745.614| 210.650|  78,668|
| |Glenn County|     3| 105.660|  0.000|   436| 15355.898| 422.639|  28,393|
| |Lake County|     2| 31.063|  0.000|   267|  4146.864| 122.032|  64,386|
| |Tuolumne County|     2| 36.712|  0.000|   159|  2918.609| 31.467|  54,478|
| |Mariposa County|     2| 116.259|  0.000|    63|  3662.152| 24.913|  17,203|
| |El Dorado County|     2| 10.371|  0.741|   793|  4112.153| 57.041| 192,843|
| |Calaveras County|     1| 21.784|  0.000|   161|  3507.243| 77.800|  45,905|
| |Mono County|     1| 69.233|  0.000|   160| 11077.264| 69.233|  14,444|
| |Nevada County|     1| 10.025|  0.000|   357|  3578.768| 51.555|  99,755|
| |Tehama County|     1| 15.365|  0.000|   305|  4686.252| 74.629|  65,084|
| |Trinity County|     0|  0.000|  0.000|     6|   488.400| 11.629|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   109|  2503.503| 62.341|  43,539|
| |Sierra County|     0|  0.000|  0.000|     5|  1663.894| 95.080|   3,005|
| |Plumas County|     0|  0.000|  0.000|    38|  2020.524| 30.384|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 16.158|   8,841|
| |Lassen County|     0|  0.000|  0.000|   694| 22699.768| 285.032|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   104|  3739.393| 71.911|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 9,771| 336.979| N/A|530,857| 18308.014| N/A|28,995,881|
| |Harris County| 1,713| 363.438|  7.699|89,425| 18972.806| 227.501|4,713,325|
| |Hidalgo County|   881| 1014.151| 19.076|20,767| 23905.644| 273.641| 868,707|
| |Bexar County|   850| 424.246| 10.339|43,673| 21797.765| 123.637|2,003,554|
| |Dallas County|   807| 306.202|  3.849|56,428| 21410.608| 192.914|2,635,516|
| |Cameron County|   506| 1195.757| 34.097|17,316| 40920.402| 489.848| 423,163|
| |Tarrant County|   480| 228.298|  3.941|33,070| 15728.782| 193.170|2,102,515|
| |El Paso County|   330| 393.214|  7.660|17,378| 20706.879| 303.336| 839,238|
| |Travis County|   328| 257.466|  4.485|23,718| 18617.627| 163.944|1,273,954|
| |Nueces County|   270| 745.251| 16.955|16,403| 45275.384| 1124.186| 362,294|
| |Webb County|   184| 665.095| 18.073| 9,126| 32987.291| 882.491| 276,652|
| |Fort Bend County|   183| 225.456|  5.280|10,823| 13333.941| 342.320| 811,688|
| |Galveston County|   117| 341.966|  2.923| 9,800| 28643.329| 237.999| 342,139|
| |Brazoria County|   105| 280.551|  7.634| 7,789| 20811.513| 305.743| 374,264|
| |Williamson County|    99| 167.640|  3.145| 7,148| 12103.950| 263.676| 590,551|
| |Denton County|    98| 110.459|  2.576| 8,077|  9103.851| 113.196| 887,207|
| |Montgomery County|    95| 156.407|  4.234| 6,864| 11300.793| 83.260| 607,391|
| |Collin County|    94| 90.845|  0.966| 8,445|  8161.549| 189.283|1,034,730|
| |Jefferson County|    88| 349.810|  6.814| 6,126| 24351.559| 201.595| 251,565|
| |Starr County|    81| 1253.230| 64.098| 2,294| 35492.705| 448.687|  64,633|
| |Comal County|    77| 492.929|  9.145| 1,993| 12758.548| 210.341| 156,209|
| |Lubbock County|    75| 241.492|  2.760| 6,365| 20494.640| 254.832| 310,569|
| |McLennan County|    60| 233.806|  6.123| 5,164| 20122.904| 231.579| 256,623|
| |Ector County|    57| 342.913|  2.578| 3,716| 22355.510| 175.324| 166,223|
| |Guadalupe County|    56| 335.637|  4.281| 1,735| 10398.749| 55.654| 166,847|
| |Victoria County|    54| 586.421| 26.373| 3,560| 38660.354| 260.632|  92,084|
| |Midland County|    52| 294.064|  4.847| 2,846| 16094.372| 222.972| 176,832|
| |Brazos County|    50| 218.140|  2.493| 4,147| 18092.500| 93.488| 229,211|
| |Angelina County|    49| 565.069| 14.827| 1,869| 21553.364| 164.743|  86,715|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 166.096|  49,025|
| |Ellis County|    48| 259.704|  7.729| 3,244| 17551.643| 390.329| 184,826|
| |Bell County|    46| 126.748|  5.117| 4,071| 11217.225| 133.046| 362,924|
| |Potter County|    45| 383.256|  1.217| 3,759| 32014.649| 139.919| 117,415|
| |Maverick County|    45| 766.323| 19.462| 2,569| 43748.510| 873.365|  58,722|
| |Hays County|    44| 191.146|  4.344| 5,103| 22168.547| 70.749| 230,191|
| |Nacogdoches County|    43| 659.469|  6.573| 1,184| 18158.395| 197.183|  65,204|
| |Walker County|    42| 575.571|  1.958| 3,128| 42866.344| 522.713|  72,971|
| |Washington County|    40| 1114.765|  3.981|   523| 14575.553| 99.533|  35,882|
| |Bowie County|    36| 386.080|  6.128|   774|  8300.713| 102.648|  93,245|
| |Liberty County|    34| 385.405|  3.239| 1,047| 11868.192| 197.560|  88,219|
| |San Patricio County|    33| 494.530| 27.831| 1,051| 15750.037| 361.799|  66,730|
| |Johnson County|    31| 176.320|  0.813| 2,073| 11790.669| 254.323| 175,817|
| |Matagorda County|    31| 846.001| 23.392|   807| 22023.306| 374.268|  36,643|
| |Hale County|    31| 927.977| 29.935| 1,443| 43195.833| 795.409|  33,406|
| |Smith County|    30| 128.893|  6.138| 2,666| 11454.301| 135.031| 232,751|
| |Tom Green County|    30| 251.678|  7.191| 2,809| 23565.436| 298.418| 119,200|
| |Willacy County|    30| 1404.626| 53.510|   734| 34366.514| 434.765|  21,358|
| |Caldwell County|    29| 664.163|  9.815| 1,171| 26818.432| 173.402|  43,664|
| |Medina County|    29| 562.190| 11.078|   949| 18397.177| 908.366|  51,584|
| |Gregg County|    28| 225.907|  5.763| 1,604| 12941.224| 283.536| 123,945|
| |Kaufman County|    28| 205.649|  5.246| 2,364| 17362.692| 307.425| 136,154|
| |Taylor County|    28| 202.849|  6.210| 1,137|  8237.101| 30.013| 138,034|
| |Wharton County|    27| 649.726|  6.875|   945| 22740.398| 959.119|  41,556|
| |Grimes County|    26| 900.277| 29.679|   918| 31786.704| 296.795|  28,880|
| |Harrison County|    24| 360.615|  4.293|   728| 10938.650| 148.110|  66,553|
| |Orange County|    24| 287.784| 10.278| 1,497| 17950.501| 219.264|  83,396|
| |Randall County|    23| 167.014|  4.149| 1,804| 13099.707| 125.520| 137,713|
| |Bastrop County|    23| 259.234|  4.830| 1,409| 15880.888| 104.660|  88,723|
| |Lavaca County|    22| 1091.595| 56.706|   637| 31606.629| 134.677|  20,154|
| |Hunt County|    21| 212.995|  0.000| 1,241| 12586.973| 150.690|  98,594|
| |DeWitt County|    20| 992.063| 35.431|   727| 36061.508| 595.238|  20,160|
| |Atascosa County|    19| 371.435|  8.378|   499|  9755.049| 206.663|  51,153|
| |Wilson County|    19| 372.038|  2.797|   475|  9300.959| 114.689|  51,070|
| |Parker County|    19| 132.981|  1.000| 1,366|  9560.604| 187.973| 142,878|
| |Hardin County|    18| 312.489| 12.400| 1,090| 18922.954| 409.212|  57,602|
| |Lamar County|    18| 361.018|  0.000|   677| 13578.291| 71.631|  49,859|
| |Deaf Smith County|    18| 970.560|  7.703|   702| 37851.828| 446.766|  18,546|
| |Jim Wells County|    18| 444.642| 17.645|   802| 19811.274| 465.815|  40,482|
| |Shelby County|    18| 712.194|  0.000|   411| 16261.771| 79.133|  25,274|
| |Panola County|    18| 776.063|  6.159|   301| 12977.494| 129.344|  23,194|
| |Brown County|    17| 448.975|  7.546|   403| 10643.355| 86.777|  37,864|
| |Aransas County|    16| 680.561| 18.229|   183|  7783.922| 109.376|  23,510|
| |Rockwall County|    15| 142.973|  4.085| 1,057| 10074.822| 332.242| 104,915|
| |Titus County|    15| 458.015|  4.362| 1,393| 42534.351| 453.653|  32,750|
| |Anderson County|    14| 242.487|  9.897| 2,437| 42210.098| 207.846|  57,735|
| |Moore County|    14| 668.577|  6.822| 1,077| 51432.665| 225.133|  20,940|
| |Lamb County|    14| 1085.861| 44.321|   238| 18459.629| 221.604|  12,893|
| |Fayette County|    14| 552.355|  0.000|   403| 15899.945| 140.907|  25,346|
| |Polk County|    14| 272.623|  8.346|   762| 14838.471| 172.476|  51,353|
| |Bee County|    13| 399.202| 17.547| 1,303| 40012.283| 2627.712|  32,565|
| |Grayson County|    13| 95.439|  0.000| 1,199|  8802.455| 112.220| 136,212|
| |Kleberg County|    12| 391.134| 23.282|   471| 15352.021| 256.100|  30,680|
| |Henderson County|    12| 145.038|  1.727|   664|  8025.430| 74.246|  82,737|
| |Jasper County|    12| 337.752| 28.146|   332|  9344.479| 112.584|  35,529|
| |Wichita County|    11| 83.188|  0.000| 1,079|  8160.024| 126.403| 132,230|
| |Red River County|    11| 914.913|  0.000|   140| 11644.348| 47.528|  12,023|
| |Hood County|    11| 178.447|  4.635|   625| 10139.026| 278.099|  61,643|
| |San Augustine County|    11| 1335.438|  0.000|   175| 21245.599| 260.150|   8,237|
| |Lee County|    11| 638.088| 16.574|   177| 10267.417| 116.016|  17,239|
| |Gonzales County|    11| 527.907| 13.712|   703| 33738.062| 226.246|  20,837|
| |Wise County|    10| 142.890|  8.165|   494|  7058.756| 242.913|  69,984|
| |Uvalde County|    10| 373.958|  5.342|   573| 21427.770| 283.139|  26,741|
| |Navarro County|    10| 199.549|  5.701|   917| 18298.645| 245.160|  50,113|
| |Jackson County|    10| 677.507| 48.393|   411| 27845.528| 271.003|  14,760|
| |Burnet County|    10| 207.663|  5.933|   577| 11982.141| 74.165|  48,155|
| |Wood County|     9| 197.633| 12.548|   350|  7685.720| 106.659|  45,539|
| |Karnes County|     9| 576.886| 27.471|   648| 41535.799| 842.437|  15,601|
| |Cherokee County|     9| 170.953| 10.854| 1,184| 22489.838| 626.828|  52,646|
| |Cass County|     9| 299.740|  4.758|   193|  6427.763| 128.460|  30,026|
| |Palo Pinto County|     9| 308.335| 14.683|   328| 11237.110| 411.114|  29,189|
| |Marion County|     9| 913.335| 14.497|   135| 13700.020| 86.984|   9,854|
| |San Jacinto County|     8| 277.210|  0.000|   183|  6341.176| 39.601|  28,859|
| |Fannin County|     8| 225.263|  0.000|   310|  8728.952| 293.647|  35,514|
| |Van Zandt County|     7| 123.697| 10.098|   434|  7669.200| 166.612|  56,590|
| |Duval County|     7| 627.409| 12.804|   193| 17298.557| 371.324|  11,157|
| |Andrews County|     7| 374.231|  7.637|   316| 16893.879| 297.858|  18,705|
| |Parmer County|     7| 728.787|  0.000|   351| 36543.467| 342.084|   9,605|
| |Hill County|     7| 191.001|  3.898|   336|  9168.054| 89.654|  36,649|
| |Houston County|     7| 304.772|  6.220|   320| 13932.428| 74.638|  22,968|
| |Dallam County|     6| 823.384| 19.604|   196| 26897.214| 176.439|   7,287|
| |Calhoun County|     6| 281.822| 13.420|   551| 25880.695| 167.751|  21,290|
| |Camp County|     6| 458.225| 10.910|   247| 18863.602| 283.663|  13,094|
| |Burleson County|     6| 325.327|  0.000|   248| 13446.836| 92.950|  18,443|
| |Erath County|     6| 140.522|  3.346|   577| 13513.514| 234.203|  42,698|
| |Kerr County|     6| 114.068|  0.000|   411|  7813.688| 46.171|  52,600|
| |Howard County|     6| 163.648|  7.793|   184|  5018.547| 77.928|  36,664|
| |Floyd County|     6| 1050.420| 25.010|    91| 15931.373| 75.030|   5,712|
| |Sabine County|     6| 569.152|  0.000|    62|  5881.237| 149.064|  10,542|
| |Zavala County|     6| 506.757| 12.066|   234| 19763.514| 386.100|  11,840|
| |Gillespie County|     6| 222.321|  5.293|   179|  6632.577| 15.880|  26,988|
| |Frio County|     6| 295.479|  7.035|   563| 27725.795| 464.324|  20,306|
| |Martin County|     5| 866.401| 24.754|    65| 11263.213| 297.052|   5,771|
| |Reeves County|     5| 312.969|  0.000|   147|  9201.302|  0.000|  15,976|
| |Coryell County|     5| 65.832|  0.000|   710|  9348.132| 105.331|  75,951|
| |Blanco County|     5| 419.076|  0.000|   114|  9554.941| 191.578|  11,931|
| |Waller County|     5| 90.504|  2.586|   491|  8887.521| 155.150|  55,246|
| |Young County|     5| 277.624|  7.932|   196| 10882.843| 356.945|  18,010|
| |Goliad County|     5| 652.912| 18.655|    96| 12535.910| 354.438|   7,658|
| |Dimmit County|     4| 395.101| 14.111|   161| 15902.805| 268.104|  10,124|
| |Crockett County|     4| 1154.734| 41.241|   157| 45323.326|  0.000|   3,464|
| |Dawson County|     4| 314.268|  0.000|   157| 12335.009| 190.805|  12,728|
| |Kendall County|     4| 84.333|  0.000|   167|  3520.904| 33.131|  47,431|
| |Chambers County|     4| 91.247|  6.518| 1,008| 22994.274| 257.447|  43,837|
| |Castro County|     4| 531.208|  0.000|   206| 27357.238| 303.548|   7,530|
| |Brooks County|     4| 563.936| 60.422|   143| 20160.722| 966.748|   7,093|
| |Lynn County|     4| 672.156|  0.000|    74| 12434.885| 192.045|   5,951|
| |Austin County|     4| 133.191|  4.757|   297|  9889.451| 352.005|  30,032|
| |Newton County|     4| 294.226|  0.000|   116|  8532.549| 241.685|  13,595|
| |Refugio County|     4| 575.705| 20.561|   238| 34254.462| 452.340|   6,948|
| |Hockley County|     4| 173.754|  0.000|   219|  9513.053| 155.138|  23,021|
| |Live Oak County|     4| 327.681| 23.406|   240| 19660.850| 210.652|  12,207|
| |Trinity County|     4| 273.019|  9.751|   162| 11057.266| 68.255|  14,651|
| |Lampasas County|     4| 186.672| 13.334|   126|  5880.157| 253.340|  21,428|
| |Bailey County|     4| 571.429|  0.000|   180| 25714.286| 244.898|   7,000|
| |Zapata County|     3| 211.581| 10.075|   188| 13259.045| 211.581|  14,179|
| |Hutchinson County|     3| 143.280|  6.823|   131|  6256.567| 68.229|  20,938|
| |Gaines County|     3| 139.587| 19.941|   186|  8654.383| 245.939|  21,492|
| |Hamilton County|     3| 354.568|  0.000|    89| 10518.851| 540.294|   8,461|
| |Bandera County|     3| 129.803|  0.000|    95|  4110.419| 37.086|  23,112|
| |Falls County|     3| 173.440|  0.000|   142|  8209.516| 156.922|  17,297|
| |Garza County|     3| 481.618|  0.000|   100| 16053.941| 22.934|   6,229|
| |Callahan County|     3| 215.162|  0.000|    51|  3657.749| 51.229|  13,943|
| |Yoakum County|     3| 344.313|  0.000|   114| 13083.898| 295.126|   8,713|
| |Comanche County|     3| 220.022|  0.000|   171| 12541.254| 314.317|  13,635|
| |Milam County|     3| 120.856|  0.000|   357| 14381.823| 143.876|  24,823|
| |Leon County|     3| 172.374|  8.208|   154|  8848.541| 131.333|  17,404|
| |Hopkins County|     3| 80.897|  7.705|   212|  5716.751| 69.341|  37,084|
| |Limestone County|     3| 128.003|  0.000|   287| 12245.595| 475.439|  23,437|
| |Cooke County|     3| 72.715|  0.000|   256|  6205.008| 152.355|  41,257|
| |Nolan County|     3| 203.887|  0.000|   137|  9310.860| 48.545|  14,714|
| |Morris County|     3| 242.170| 23.064|   130| 10494.026| 345.957|  12,388|
| |Reagan County|     3| 779.423|  0.000|    64| 16627.696| 111.346|   3,849|
| |Presidio County|     3| 447.494| 63.928|    49|  7309.069| 63.928|   6,704|
| |Stephens County|     3| 320.307|  0.000|    47|  5018.151| 198.286|   9,366|
| |Runnels County|     2| 194.856| 13.918|   149| 14516.758| 445.385|  10,264|
| |Montague County|     2| 100.918|  7.208|    79|  3986.275| 108.127|  19,818|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 94.985|   7,520|
| |Ochiltree County|     2| 203.335|  0.000|   100| 10166.734| 130.715|   9,836|
| |Madison County|     2| 140.017|  0.000|   685| 47955.755| 350.042|  14,284|
| |Knox County|     2| 545.852| 38.989|    62| 16921.397| 233.936|   3,664|
| |Robertson County|     2| 117.137|  0.000|   238| 13939.323| 100.403|  17,074|
| |Culberson County|     2| 921.234|  0.000|    21|  9672.962| 263.210|   2,171|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 26.640|  10,725|
| |Hudspeth County|     2| 409.333|  0.000|    33|  6753.991| 292.381|   4,886|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 84.356|   3,387|
| |Colorado County|     2| 93.054|  0.000|   345| 16051.738| 531.735|  21,493|
| |Upshur County|     2| 47.901|  0.000|   262|  6274.998| 188.182|  41,753|
| |Terry County|     2| 162.114|  0.000|   161| 13050.174| 335.808|  12,337|
| |Throckmorton County|     2| 1332.445|  0.000|     4|  2664.890|  0.000|   1,501|
| |Tyler County|     2| 92.285|  0.000|   127|  5860.096| 72.510|  21,672|
| |Swisher County|     2| 270.380|  0.000|    82| 11085.575| 57.939|   7,397|
| |Rusk County|     2| 36.761|  0.000|   396|  7278.609| 110.282|  54,406|
| |Pecos County|     2| 126.398|  9.028|   251| 15862.984| 135.427|  15,823|
| |Gray County|     2| 91.383|  0.000|   221| 10097.779| 65.273|  21,886|
| |Hansford County|     2| 370.439|  0.000|    82| 15187.998| 476.279|   5,399|
| |Bosque County|     2| 107.038|  0.000|   178|  9526.358| 198.784|  18,685|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461| 15.523|   9,203|
| |Crosby County|     1| 174.307|  0.000|    65| 11329.963| 149.406|   5,737|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505|  6.555|  21,795|
| |Rains County|     1| 79.911|  0.000|    52|  4155.346| 11.416|  12,514|
| |Real County|     1| 289.687|  0.000|    90| 26071.842| 124.152|   3,452|
| |Ward County|     1| 83.347|  0.000|    95|  7917.986| 83.347|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Wilbarger County|     1| 78.315|  0.000|    77|  6030.229| 179.005|  12,769|
| |Winkler County|     1| 124.844|  0.000|    86| 10736.579| 231.853|   8,010|
| |Sutton County|     1| 264.831|  0.000|    67| 17743.644| 189.165|   3,776|
| |Hall County|     1| 337.382|  0.000|    15|  5060.729| 240.987|   2,964|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366|  0.000|   2,793|
| |Scurry County|     1| 59.869|  0.000|   503| 30114.351| 256.584|  16,703|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Kimble County|     1| 230.574| 32.939|    15|  3458.612| 65.878|   4,337|
| |McCulloch County|     1| 125.251|  0.000|    54|  6763.527| 161.036|   7,984|
| |Mitchell County|     1| 117.028| 16.718|    69|  8074.898| 167.182|   8,545|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Fisher County|     1| 261.097|  0.000|    30|  7832.898| 149.198|   3,830|
| |Eastland County|     1| 54.466|  0.000|    86|  4684.096| 163.399|  18,360|
| |Clay County|     1| 95.502|  0.000|    45|  4297.584| 95.502|  10,471|
| |Jim Hogg County|     1| 192.308|  0.000|    65| 12500.000| 302.198|   5,200|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Hemphill County|     0|  0.000|  0.000|    44| 11521.341| 74.814|   3,819|
| |Sterling County|     0|  0.000|  0.000|     1|   774.593| 110.656|   1,291|
| |Somervell County|     0|  0.000|  0.000|    83|  9092.901| 266.057|   9,128|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534| 75.706|   1,887|
| |Archer County|     0|  0.000|  0.000|    29|  3390.623| 133.621|   8,553|
| |Sherman County|     0|  0.000|  0.000|    43| 14228.987| 189.090|   3,022|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 50.073|   2,853|
| |Shackelford County|     0|  0.000|  0.000|    21|  6431.853| 175.016|   3,265|
| |Hardeman County|     0|  0.000|  0.000|    22|  5593.694| 181.613|   3,933|
| |San Saba County|     0|  0.000|  0.000|    26|  4293.972| 70.780|   6,055|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Edwards County|     0|  0.000|  0.000|    29| 15010.352| 295.770|   1,932|
| |Stonewall County|     0|  0.000|  0.000|     6|  4444.444| 105.820|   1,350|
| |Childress County|     0|  0.000|  0.000|    50|  6843.690| 254.194|   7,306|
| |Haskell County|     0|  0.000|  0.000|    44|  7776.600| 126.243|   5,658|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Hartley County|     0|  0.000|  0.000|    92| 16499.283| 204.960|   5,576|
| |Carson County|     0|  0.000|  0.000|    17|  2868.714| 72.321|   5,926|
| |Wheeler County|     0|  0.000|  0.000|    35|  6922.468| 56.510|   5,056|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Baylor County|     0|  0.000|  0.000|    13|  3704.759| 203.558|   3,509|
| |Mills County|     0|  0.000|  0.000|    26|  5335.522| 293.161|   4,873|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Mason County|     0|  0.000|  0.000|    60| 14038.372| 300.822|   4,274|
| |McMullen County|     0|  0.000|  0.000|    10| 13458.950| 384.541|     743|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |Concho County|     0|  0.000|  0.000|    32| 11738.811| 314.432|   2,726|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Lipscomb County|     0|  0.000|  0.000|    22|  6804.825| 265.123|   3,233|
| |Kinney County|     0|  0.000|  0.000|    21|  5726.752| 77.915|   3,667|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Coleman County|     0|  0.000|  0.000|    29|  3547.401| 192.224|   8,175|
| |Jones County|     0|  0.000|  0.000|   599| 29826.221|  0.000|  20,083|
| |Jack County|     0|  0.000|  0.000|    70|  7834.359| 303.781|   8,935|
| |Freestone County|     0|  0.000|  0.000|   172|  8723.437| 159.398|  19,717|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 130.742|   3,278|
| |Collingsworth County|     0|  0.000|  0.000|    12|  4109.589| 195.695|   2,920|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,913| 414.988| N/A|556,417| 25906.687| N/A|21,477,737|
| |Miami-Dade County| 1,954| 719.191|  8.939|140,984| 51890.730| 699.684|2,716,940|
| |Palm Beach County|   964| 644.054|  6.872|38,208| 25526.968| 235.841|1,496,770|
| |Broward County|   883| 452.176|  7.389|64,741| 33153.282| 342.589|1,952,778|
| |Pinellas County|   536| 549.746|  9.817|18,329| 18799.051| 142.272| 974,996|
| |Hillsborough County|   427| 290.088|  4.756|33,428| 22709.733| 181.002|1,471,968|
| |Lee County|   368| 477.564|  8.343|17,039| 22112.002| 175.935| 770,577|
| |Polk County|   343| 473.249|  7.687|14,992| 20684.983| 263.726| 724,777|
| |Orange County|   330| 236.822|  5.639|32,575| 23377.196| 184.434|1,393,452|
| |Manatee County|   242| 600.120| 18.776| 9,554| 23692.322| 178.548| 403,253|
| |Duval County|   212| 221.351|  7.010|24,162| 25227.746| 237.758| 957,755|
| |St. Lucie County|   188| 572.652| 17.406| 6,040| 18397.975| 228.887| 328,297|
| |Sarasota County|   167| 385.022| 12.186| 6,479| 14937.451| 149.529| 433,742|
| |Brevard County|   163| 270.790|  6.882| 6,313| 10487.721| 123.173| 601,942|
| |Volusia County|   151| 272.916|  6.971| 8,206| 14831.443| 185.387| 553,284|
| |Collier County|   148| 384.513|  6.681|10,640| 27643.400| 193.741| 384,902|
| |Escambia County|   141| 442.956| 13.464|10,035| 31525.277| 682.161| 318,316|
| |Pasco County|   141| 254.537|  9.542| 7,283| 13147.467| 124.045| 553,947|
| |Seminole County|   138| 292.481|  8.780| 7,323| 15520.552| 118.385| 471,826|
| |Marion County|   108| 295.422|  9.769| 6,921| 18931.613| 474.394| 365,579|
| |Osceola County|   107| 284.763|  4.182|10,037| 26711.838| 285.523| 375,751|
| |Martin County|   101| 627.329| 12.422| 3,883| 24118.012| 151.730| 161,000|
| |Charlotte County|    97| 513.472|  6.050| 2,321| 12286.274| 133.851| 188,910|
| |Lake County|    75| 204.294|  5.837| 5,391| 14684.652| 214.411| 367,118|
| |Clay County|    61| 278.219|  7.167| 3,369| 15365.880| 168.756| 219,252|
| |Indian River County|    58| 362.675|  6.253| 2,584| 16157.776| 142.926| 159,923|
| |Hernando County|    53| 273.309|  8.103| 2,124| 10952.970| 160.596| 193,920|
| |Bay County|    52| 297.645|  5.724| 4,644| 26581.952| 463.639| 174,705|
| |Okaloosa County|    49| 232.516|  9.490| 3,632| 17234.671| 230.483| 210,738|
| |Jackson County|    46| 991.080| 30.779| 1,996| 43004.266| 612.500|  46,414|
| |Suwannee County|    45| 1013.126| 22.514| 2,152| 48449.918| 2733.831|  44,417|
| |Sumter County|    44| 332.276|  4.315| 1,410| 10647.938| 217.921| 132,420|
| |Santa Rosa County|    44| 238.724|  7.751| 4,088| 22179.662| 300.731| 184,313|
| |St. Johns County|    42| 158.687|  4.858| 3,817| 14421.624| 164.624| 264,672|
| |Highlands County|    40| 376.573|  8.069| 1,523| 14338.031| 262.256| 106,221|
| |Hendry County|    38| 904.288|  3.400| 1,839| 43762.791| 441.945|  42,022|
| |Citrus County|    38| 253.914|  1.909| 1,663| 11112.076| 223.368| 149,657|
| |Putnam County|    29| 389.152| 11.502| 1,559| 20920.278| 216.622|  74,521|
| |Alachua County|    26| 96.639|  0.531| 4,391| 16320.811| 233.101| 269,043|
| |Leon County|    26| 88.561|  1.460| 5,235| 17831.475| 288.067| 293,582|
| |Gadsden County|    26| 569.426| 15.644| 1,984| 43451.599| 1004.318|  45,660|
| |Columbia County|    21| 292.944| 15.943| 2,958| 41263.287| 452.370|  71,686|
| |Walton County|    18| 243.010|  5.786| 1,450| 19575.812| 244.939|  74,071|
| |DeSoto County|    18| 473.672|  7.519| 1,393| 36656.930| 270.670|  38,001|
| |Washington County|    14| 549.602|  0.000|   896| 35174.498| 835.619|  25,473|
| |Monroe County|    13| 175.136|  0.000| 1,577| 21245.352| 267.516|  74,228|
| |Flagler County|    13| 112.964|  0.000| 1,107|  9619.312| 146.481| 115,081|
| |Okeechobee County|    12| 284.576| 16.939| 1,087| 25777.841| 332.005|  42,168|
| |Nassau County|    11| 124.118|  0.000| 1,280| 14442.877| 154.745|  88,625|
| |Madison County|     9| 486.671|  7.725|   738| 39906.992| 486.671|  18,493|
| |Hardee County|     8| 296.989|  5.303|   998| 37049.412| 572.765|  26,937|
| |Calhoun County|     8| 567.175| 10.128|   484| 34314.073| 1296.399|  14,105|
| |Liberty County|     7| 837.922| 51.301|   407| 48719.176| 393.310|   8,354|
| |Gilchrist County|     6| 322.893| 23.064|   387| 20826.606| 369.021|  18,582|
| |Jefferson County|     5| 350.976|  0.000|   462| 32430.156| 240.669|  14,246|
| |Levy County|     5| 120.473|  3.442|   720| 17348.144| 258.157|  41,503|
| |Taylor County|     5| 231.814|  6.623| 1,027| 47614.632| 1125.955|  21,569|
| |Wakulla County|     5| 148.196|  4.234|   747| 22140.550| 406.482|  33,739|
| |Union County|     5| 328.149|  9.376|   456| 29927.151| 1987.643|  15,237|
| |Baker County|     4| 136.939|  0.000| 1,052| 36015.063| 2562.723|  29,210|
| |Dixie County|     4| 237.727|  0.000|   570| 33876.144| 1655.601|  16,826|
| |Hamilton County|     4| 277.239|  0.000|   625| 43318.547| 267.337|  14,428|
| |Holmes County|     4| 203.905| 14.565|   518| 26405.669| 305.857|  19,617|
| |Bradford County|     4| 141.839|  0.000|   545| 19325.556| 845.968|  28,201|
| |Glades County|     3| 217.218|  0.000|   410| 29686.482| 124.125|  13,811|
| |Lafayette County|     2| 237.473| 16.962|   469| 55687.485| 5970.757|   8,422|
| |Franklin County|     2| 164.948|  0.000|   448| 36948.454| 2026.510|  12,125|
| |Gulf County|     2| 146.638|  0.000|   712| 52203.241| 2325.265|  13,639|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  0.709|26,565| 16482.606| 36.253|1,611,699|
| |Essex County| 1,194| 1513.243|  0.724|17,930| 22723.989| 56.670| 789,034|
| |Suffolk County| 1,076| 1338.463|  1.777|22,017| 27387.496| 68.594| 803,907|
| |Worcester County| 1,007| 1212.344|  1.548|13,686| 16476.809| 27.690| 830,622|
| |Norfolk County|   997| 1410.633|  0.606|10,682| 15113.721| 33.755| 706,775|
| |Plymouth County|   723| 1387.178|  1.645| 9,288| 17820.346| 26.039| 521,202|
| |Hampden County|   709| 1520.246|  2.757| 7,637| 16375.340| 29.406| 466,372|
| |Bristol County|   637| 1127.001|  2.022| 9,408| 16644.935| 34.374| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,803|  8465.186| 13.414| 212,990|
| |Hampshire County|   130| 808.307|  1.776| 1,184|  7361.811| 23.094| 160,830|
| |Franklin County|    61| 869.194|  0.000|   411|  5856.369|  4.071|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  1.143| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,696| 607.332| N/A|200,342| 15810.040| N/A|12,671,821|
| |Cook County| 4,943| 959.762|  0.860|113,788| 22093.758| 128.649|5,150,233|
| |DuPage County|   523| 566.679|  0.619|12,592| 13643.638| 103.089| 922,921|
| |Lake County|   450| 646.055|  1.231|13,047| 18731.291| 137.620| 696,535|
| |Will County|   347| 502.358|  0.620| 9,576| 13863.333| 133.190| 690,743|
| |Kane County|   305| 572.874|  0.805|10,027| 18833.478| 138.992| 532,403|
| |St. Clair County|   162| 623.830|  1.650| 4,215| 16231.141| 203.543| 259,686|
| |Winnebago County|   134| 474.215|  3.033| 3,814| 13497.445| 34.378| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,308| 10748.146| 115.112| 307,774|
| |Madison County|    79| 300.419|  2.716| 2,855| 10856.917| 241.748| 262,966|
| |Kankakee County|    69| 628.061|  1.300| 1,829| 16648.159| 150.839| 109,862|
| |Rock Island County|    38| 267.834|  4.028| 1,796| 12658.674| 140.965| 141,879|
| |Peoria County|    37| 206.497|  1.595| 1,758|  9811.418| 215.268| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,345|  6909.057| 142.364| 194,672|
| |DeKalb County|    31| 295.528|  1.362|   960|  9151.835| 84.437| 104,897|
| |LaSalle County|    28| 257.663|  9.202|   878|  8079.581| 278.697| 108,669|
| |Macon County|    23| 221.135|  0.000|   702|  6749.416| 208.773| 104,009|
| |Kendall County|    23| 178.308|  0.000| 1,431| 11093.883| 124.041| 128,990|
| |Boone County|    23| 429.553|  0.000|   770| 14380.696| 42.689|  53,544|
| |Union County|    23| 1381.133|  0.000|   337| 20236.594| 240.197|  16,653|
| |Coles County|    21| 414.848|  2.822|   546| 10786.037| 318.896|  50,621|
| |Jackson County|    20| 352.423|  2.517|   743| 13092.511| 146.004|  56,750|
| |Jefferson County|    20| 530.729|  3.791|   317|  8412.058| 375.301|  37,684|
| |Champaign County|    19| 90.610|  0.000| 1,729|  8245.545| 77.666| 209,689|
| |Whiteside County|    17| 308.111|  2.589|   368|  6669.687| 85.442|  55,175|
| |Clinton County|    17| 452.585|  0.000|   433| 11527.608| 209.178|  37,562|
| |McDonough County|    15| 505.357|  0.000|   147|  4952.496| 48.129|  29,682|
| |McLean County|    15| 87.455|  0.000|   703|  4098.719| 76.627| 171,517|
| |Monroe County|    13| 375.321|  0.000|   334|  9642.867| 144.354|  34,637|
| |Iroquois County|    12| 442.576| 15.806|   274| 10105.481| 115.913|  27,114|
| |Cass County|    11| 905.573|  0.000|   245| 20169.589| 305.778|  12,147|
| |Tazewell County|     9| 68.284|  1.084|   612|  4643.293| 177.754| 131,803|
| |Randolph County|     7| 220.250|  0.000|   495| 15574.854| 242.725|  31,782|
| |Jasper County|     7| 728.408|  0.000|    61|  6347.555| 89.193|   9,610|
| |Adams County|     7| 106.976|  4.366|   581|  8879.040| 207.403|  65,435|
| |Williamson County|     7| 105.110|  2.145|   477|  7162.485| 242.396|  66,597|
| |Montgomery County|     7| 246.357|  0.000|   175|  6158.936| 70.388|  28,414|
| |Stephenson County|     6| 134.838|  0.000|   336|  7550.901| 35.315|  44,498|
| |Morgan County|     6| 178.264|  0.000|   291|  8645.790| 292.862|  33,658|
| |Grundy County|     5| 97.936|  0.000|   353|  6914.248| 151.101|  51,054|
| |Ogle County|     5| 98.730|  0.000|   421|  8313.094| 59.238|  50,643|
| |Carroll County|     4| 279.623|  0.000|    68|  4753.583| 199.730|  14,305|
| |Christian County|     4| 123.824|  0.000|   144|  4457.652| 70.756|  32,304|
| |Mercer County|     4| 259.118|  9.254|    77|  4988.016| 37.017|  15,437|
| |Cumberland County|     3| 278.655| 13.269|    60|  5573.101| 119.424|  10,766|
| |Woodford County|     3| 78.005|  0.000|   172|  4472.295| 174.583|  38,459|
| |Bureau County|     3| 91.946|  4.378|   247|  7570.185| 337.134|  32,628|
| |Perry County|     3| 143.431| 13.660|   193|  9227.386| 348.332|  20,916|
| |Bond County|     3| 182.637|  0.000|    68|  4139.778| 78.273|  16,426|
| |Fayette County|     3| 140.607|  0.000|    73|  3421.447| 87.043|  21,336|
| |Livingston County|     3| 84.156|  4.007|   134|  3758.977| 124.231|  35,648|
| |Douglas County|     3| 154.123|  7.339|   133|  6832.777| 198.158|  19,465|
| |Macoupin County|     3| 66.776|  0.000|   209|  4652.095| 174.891|  44,926|
| |Gallatin County|     2| 414.250|  0.000|    51| 10563.380| 88.768|   4,828|
| |Clark County|     2| 129.525|  9.252|    88|  5699.113| 111.022|  15,441|
| |Ford County|     2| 154.309| 11.022|    52|  4012.036| 11.022|  12,961|
| |Jersey County|     2| 91.857|  6.561|   141|  6475.911| 367.428|  21,773|
| |Shelby County|     2| 92.447|  6.603|    92|  4252.565| 158.481|  21,634|
| |Saline County|     2| 85.139|  0.000|   134|  5704.312| 48.651|  23,491|
| |Wayne County|     2| 123.343|  8.810|    67|  4131.977| 105.722|  16,215|
| |Vermilion County|     2| 26.400|  0.000|   257|  3392.381| 66.000|  75,758|
| |Knox County|     1| 20.121|  0.000|   331|  6660.094| 132.225|  49,699|
| |Lee County|     1| 29.329|  0.000|   186|  5455.185| 100.556|  34,096|
| |Logan County|     1| 34.943|  4.992|   179|  6254.805| 444.276|  28,618|
| |Hancock County|     1| 56.472|  0.000|    72|  4065.959| 209.752|  17,708|
| |Henry County|     1| 20.444|  0.000|   266|  5438.227| 122.667|  48,913|
| |Jo Daviess County|     1| 47.092|  0.000|   136|  6404.521| 100.912|  21,235|
| |Pulaski County|     1| 187.441| 26.777|   101| 18931.584| 267.773|   5,335|
| |Washington County|     1| 72.010| 10.287|    69|  4968.676| 92.584|  13,887|
| |Effingham County|     1| 29.405|  0.000|   192|  5645.730| 264.644|  34,008|
| |Franklin County|     1| 25.995|  3.714|   205|  5328.966| 215.387|  38,469|
| |Richland County|     0|  0.000|  0.000|    24|  1547.090| 82.880|  15,513|
| |Pike County|     0|  0.000|  0.000|    30|  1927.897| 110.166|  15,561|
| |Moultrie County|     0|  0.000|  0.000|   100|  6896.076| 305.398|  14,501|
| |Menard County|     0|  0.000|  0.000|    58|  4755.658| 58.567|  12,196|
| |Piatt County|     0|  0.000|  0.000|    65|  3976.995| 96.147|  16,344|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 102.603|   4,177|
| |White County|     0|  0.000|  0.000|    75|  5540.371| 116.084|  13,537|
| |Warren County|     0|  0.000|  0.000|   196| 11636.191| 76.331|  16,844|
| |Wabash County|     0|  0.000|  0.000|    44|  3819.444| 124.008|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    28|  5655.423| 432.813|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    19|  2807.329| 42.215|   6,768|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203| 49.785|   5,739|
| |Fulton County|     0|  0.000|  0.000|    37|  1077.461| 20.800|  34,340|
| |Edwards County|     0|  0.000|  0.000|    24|  3752.932| 156.372|   6,395|
| |Edgar County|     0|  0.000|  0.000|    30|  1748.150| 16.649|  17,161|
| |De Witt County|     0|  0.000|  0.000|    34|  2174.191| 18.271|  15,638|
| |Crawford County|     0|  0.000|  0.000|    31|  1660.685| 15.306|  18,667|
| |Clay County|     0|  0.000|  0.000|    31|  2351.335| 140.863|  13,184|
| |Calhoun County|     0|  0.000|  0.000|    12|  2532.180| 90.435|   4,739|
| |Greene County|     0|  0.000|  0.000|    66|  5089.059| 363.504|  12,969|
| |Hamilton County|     0|  0.000|  0.000|    31|  3819.616| 88.010|   8,116|
| |Henderson County|     0|  0.000|  0.000|    15|  2256.997| 107.476|   6,646|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Brown County|     0|  0.000|  0.000|    15|  2280.328| 43.435|   6,578|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809|  0.000|   3,821|
| |Massac County|     0|  0.000|  0.000|    43|  3122.277| 72.611|  13,772|
| |Mason County|     0|  0.000|  0.000|    58|  4341.642| 139.018|  13,359|
| |Marshall County|     0|  0.000|  0.000|    33|  2885.120| 137.387|  11,438|
| |Marion County|     0|  0.000|  0.000|   168|  4515.522| 57.596|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    52|  3316.750| 72.896|  15,678|
| |Johnson County|     0|  0.000|  0.000|    71|  5717.967| 57.525|  12,417|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,395| 577.645| N/A|126,905|  9912.913| N/A|12,801,989|
| |Philadelphia County| 1,709| 1078.871| N/A|31,910| 20144.388| N/A|1,584,064|
| |Montgomery County|   859| 1033.800|  0.688|10,264| 12352.647| 48.312| 830,915|
| |Delaware County|   707| 1247.470|  3.025| 9,496| 16755.272| 105.867| 566,747|
| |Bucks County|   582| 926.353|  0.227| 7,318| 11647.858| 45.476| 628,270|
| |Lancaster County|   418| 765.955|  2.094| 6,099| 11175.979| 89.789| 545,724|
| |Berks County|   372| 883.266|  1.357| 5,491| 13037.677| 64.108| 421,164|
| |Chester County|   350| 666.681|  0.272| 5,264| 10026.877| 51.430| 524,989|
| |Lehigh County|   340| 920.616|  1.547| 5,036| 13635.945| 52.220| 369,318|
| |Northampton County|   294| 963.035|  0.936| 3,982| 13043.549| 37.436| 305,285|
| |Allegheny County|   260| 213.808|  1.997| 9,192|  7558.931| 68.137|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,952|  9309.690| 24.528| 209,674|
| |Luzerne County|   185| 582.830|  0.450| 3,553| 11193.477| 69.309| 317,417|
| |Dauphin County|   160| 574.921|  1.027| 2,914| 10470.753| 88.805| 278,299|
| |Monroe County|   124| 728.251|  0.000| 1,655|  9719.800| 34.399| 170,271|
| |York County|   100| 222.688|  2.545| 2,751|  6126.157| 97.665| 449,058|
| |Beaver County|    93| 567.319|  1.743| 1,374|  8381.677| 81.917| 163,929|
| |Cumberland County|    71| 280.223|  0.000| 1,339|  5284.761| 38.904| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,632| 11509.736| 41.308| 141,793|
| |Schuylkill County|    51| 360.784|  1.011|   930|  6578.994| 23.244| 141,359|
| |Westmoreland County|    47| 134.709|  0.409| 1,586|  4545.728| 41.764| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,393|  8985.532| 64.505| 155,027|
| |Columbia County|    35| 538.760|  0.000|   483|  7434.887| 28.587|  64,964|
| |Carbon County|    28| 436.259|  0.000|   379|  5905.082| 26.710|  64,182|
| |Susquehanna County|    27| 669.510|  0.000|   218|  5405.673| 21.254|  40,328|
| |Erie County|    22| 81.564|  2.648| 1,163|  4311.751| 61.967| 269,728|
| |Pike County|    21| 376.283|  0.000|   527|  9442.921|  2.560|  55,809|
| |Adams County|    21| 203.866|  1.387|   539|  5232.552| 67.955| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   426|  3759.963| 90.784| 113,299|
| |Butler County|    16| 85.173|  0.760|   707|  3763.581| 53.233| 187,853|
| |Lawrence County|    16| 187.108|  3.341|   414|  4841.426| 51.789|  85,512|
| |Northumberland County|    15| 165.120|  4.718|   524|  5768.193| 152.539|  90,843|
| |Washington County|    14| 67.677|  2.072|   880|  4253.982| 49.722| 206,865|
| |Mercer County|    12| 109.665|  3.917|   468|  4276.941| 103.137| 109,424|
| |Centre County|    10| 61.582|  0.000|   380|  2340.118| 14.076| 162,385|
| |Wayne County|    10| 194.700|  5.563|   162|  3154.144| 13.907|  51,361|
| |Armstrong County|     8| 123.581|  4.414|   237|  3661.080| 81.652|  64,735|
| |Wyoming County|     8| 298.574|  0.000|    62|  2313.951| 21.327|  26,794|
| |Indiana County|     7| 83.261|  1.699|   343|  4079.788| 78.163|  84,073|
| |Blair County|     7| 57.458|  4.690|   304|  2495.301| 57.458| 121,829|
| |Fayette County|     6| 46.413|  1.105|   595|  4602.627| 143.659| 129,274|
| |Juniata County|     6| 242.297|  0.000|   135|  5451.682| 34.614|  24,763|
| |Clinton County|     5| 129.426|  0.000|   125|  3235.660| 25.885|  38,632|
| |Perry County|     5| 108.057|  0.000|   128|  2766.252| 24.699|  46,272|
| |Huntingdon County|     5| 110.757|  3.164|   313|  6933.369| 53.796|  45,144|
| |Bedford County|     4| 83.528|  0.000|   145|  3027.898| 26.848|  47,888|
| |Cambria County|     3| 23.043|  0.000|   353|  2711.380| 34.016| 130,192|
| |Montour County|     3| 164.564|  0.000|   106|  5814.591| 62.691|  18,230|
| |Bradford County|     3| 49.732|  0.000|    91|  1508.546| 14.209|  60,323|
| |Tioga County|     3| 73.908|  0.000|    40|   985.440| 10.558|  40,591|
| |Somerset County|     3| 40.846|  0.000|   138|  1878.906| 21.395|  73,447|
| |Elk County|     2| 66.867|  0.000|    54|  1805.416| 28.657|  29,910|
| |Clarion County|     2| 52.032|  0.000|    84|  2185.337| 26.016|  38,438|
| |Union County|     2| 44.521|  0.000|   276|  6143.846| 222.603|  44,923|
| |Fulton County|     2| 137.646|  0.000|    28|  1927.047| 19.664|  14,530|
| |Snyder County|     2| 49.539|  0.000|   113|  2798.970| 42.462|  40,372|
| |Crawford County|     1| 11.816|  0.000|   161|  1902.421| 38.825|  84,629|
| |Clearfield County|     1| 12.618|  1.803|   182|  2296.385| 57.680|  79,255|
| |Greene County|     1| 27.599|  0.000|   121|  3339.497| 43.370|  36,233|
| |Jefferson County|     1| 23.028|  0.000|    75|  1727.116| 46.056|  43,425|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  0.000|  40,625|
| |Mifflin County|     1| 21.674|  0.000|   123|  2665.915| 24.770|  46,138|
| |Warren County|     1| 25.516|  0.000|    22|   561.353|  7.290|  39,191|
| |Forest County|     0|  0.000|  0.000|    11|  1517.869| 39.425|   7,247|
| |Venango County|     0|  0.000|  0.000|    67|  1322.334| 11.278|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Cameron County|     0|  0.000|  0.000|     8|  1798.966| 64.249|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,479| 648.753| N/A|94,914|  9503.891| N/A|9,986,857|
| |Wayne County| 2,833| 1619.465|  0.980|28,690| 16400.443| 69.740|1,749,343|
| |Oakland County| 1,136| 903.319|  0.795|16,083| 12788.808| 103.032|1,257,584|
| |Macomb County|   949| 1085.847|  1.144|10,953| 12532.438| 148.910| 873,972|
| |Genesee County|   299| 736.793|  1.408| 3,699|  9115.036| 33.443| 405,813|
| |Kent County|   157| 238.981|  0.000| 7,671| 11676.599| 63.279| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,115| 11100.090| 135.705| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,640|  7181.700| 61.013| 367,601|
| |Kalamazoo County|    83| 313.130|  0.000| 1,700|  6413.497| 53.356| 265,066|
| |Berrien County|    67| 436.764|  0.931| 1,408|  9178.558| 68.914| 153,401|
| |Muskegon County|    61| 351.451|  2.469| 1,202|  6925.319| 37.861| 173,566|
| |Ottawa County|    59| 202.172|  1.958| 1,873|  6418.120| 46.505| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   837|  5259.917| 38.603| 159,128|
| |Calhoun County|    42| 313.061|  1.065|   819|  6104.697| 45.788| 134,159|
| |Jackson County|    34| 214.498|  0.000|   724|  4567.535| 15.321| 158,510|
| |Lapeer County|    33| 376.682|  0.000|   482|  5501.843| 42.397|  87,607|
| |Ingham County|    32| 109.437|  0.977| 1,588|  5430.805| 33.222| 292,406|
| |Bay County|    31| 300.603|  0.000|   686|  6652.057| 126.059| 103,126|
| |Tuscola County|    29| 555.077|  0.000|   367|  7024.596| 101.172|  52,245|
| |Livingston County|    28| 145.837|  0.000|   869|  4526.160| 43.156| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   350|  5137.841| 27.262|  68,122|
| |Monroe County|    25| 166.113|  1.898| 1,032|  6857.143| 82.582| 150,500|
| |Hillsdale County|    25| 548.186|  0.000|   281|  6161.605| 72.047|  45,605|
| |Gratiot County|    15| 368.451|  0.000|   161|  3954.705| 35.091|  40,711|
| |Cass County|    14| 270.338|  0.000|   345|  6661.904| 88.274|  51,787|
| |Clinton County|    13| 163.327|  0.000|   430|  5402.349| 16.153|  79,595|
| |Alpena County|    13| 457.666|  0.000|   130|  4576.659| 15.088|  28,405|
| |Iosco County|    12| 477.574|  0.000|   135|  5372.707| 28.427|  25,127|
| |Lenawee County|    12| 121.888|  0.000|   458|  4652.060| 65.297|  98,451|
| |Otsego County|    11| 445.922|  5.791|   135|  5472.677| 23.165|  24,668|
| |Marquette County|    11| 164.920|  0.000|   179|  2683.698| 64.255|  66,699|
| |Van Buren County|    10| 132.141|  0.000|   478|  6316.318| 94.386|  75,677|
| |Midland County|    10| 120.256|  0.000|   348|  4184.905| 39.513|  83,156|
| |St. Joseph County|    10| 164.031|  4.687|   608|  9973.099| 86.702|  60,964|
| |Isabella County|     9| 128.807|  0.000|   222|  3177.238| 34.757|  69,872|
| |Eaton County|     8| 72.551|  0.000|   465|  4216.999| 12.955| 110,268|
| |Ionia County|     7| 108.197|  2.208|   275|  4250.583|  2.208|  64,697|
| |Allegan County|     6| 50.813|  0.000|   548|  4640.882| 49.603| 118,081|
| |Sanilac County|     6| 145.737|  0.000|   111|  2696.138| 31.229|  41,170|
| |Oceana County|     6| 226.697|  0.000|   479| 18098.009| 48.578|  26,467|
| |Grand Traverse County|     5| 53.713|  0.000|   224|  2406.325| 33.762|  93,088|
| |Crawford County|     5| 356.405|  0.000|   107|  7627.058| 40.732|  14,029|
| |Wexford County|     4| 118.938|  0.000|    70|  2081.413|  0.000|  33,631|
| |Huron County|     4| 129.111|  0.000|   165|  5325.845| 50.722|  30,981|
| |Kalkaska County|     4| 221.754|  0.000|    54|  2993.680| 39.599|  18,038|
| |Clare County|     3| 96.931|  0.000|    80|  2584.814| 64.620|  30,950|
| |Delta County|     3| 83.836|  0.000|   106|  2962.218| 75.852|  35,784|
| |Ogemaw County|     3| 142.878|  6.804|    54|  2571.796|  6.804|  20,997|
| |Arenac County|     3| 201.572|  0.000|    44|  2956.393| 28.796|  14,883|
| |Barry County|     2| 32.494|  0.000|   192|  3119.415| 44.099|  61,550|
| |Roscommon County|     2| 83.267| 11.895|    57|  2373.121| 29.738|  24,019|
| |Emmet County|     2| 59.853|  0.000|    67|  2005.088| 29.927|  33,415|
| |Charlevoix County|     2| 76.502|  0.000|    51|  1950.809| 32.787|  26,143|
| |Cheboygan County|     2| 79.126|  0.000|    53|  2096.851| 56.519|  25,276|
| |Gladwin County|     2| 78.589|  0.000|    62|  2436.245| 28.067|  25,449|
| |Mecosta County|     2| 46.027|  0.000|    70|  1610.936| 16.438|  43,453|
| |Montcalm County|     2| 31.305|  2.236|   199|  3114.826| 33.541|  63,888|
| |Dickinson County|     2| 79.242|  0.000|    62|  2456.516| 62.262|  25,239|
| |Branch County|     2| 45.959|  0.000|   369|  8479.445| 55.807|  43,517|
| |Presque Isle County|     1| 79.416|  0.000|    21|  1667.726| 22.690|  12,592|
| |Missaukee County|     1| 66.146|  0.000|    42|  2778.145|  9.449|  15,118|
| |Iron County|     1| 90.367|  0.000|    20|  1807.338| 25.819|  11,066|
| |Gogebic County|     1| 71.556|  0.000|   130|  9302.326| 214.669|  13,975|
| |Benzie County|     1| 56.287|  0.000|    30|  1688.619| 16.082|  17,766|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846|  6.125|  23,324|
| |Chippewa County|     0|  0.000|  0.000|    44|  1178.077| 19.125|  37,349|
| |Alger County|     0|  0.000|  0.000|    15|  1646.904| 109.794|   9,108|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128|  0.000|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Ontonagon County|     0|  0.000|  0.000|    20|  3496.503| 349.650|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   258|  5267.456| 23.333|  48,980|
| |Montmorency County|     0|  0.000|  0.000|     8|   857.633|  0.000|   9,328|
| |Menominee County|     0|  0.000|  0.000|   153|  6716.418| 225.762|  22,780|
| |Mason County|     0|  0.000|  0.000|   103|  3534.175| 19.607|  29,144|
| |Manistee County|     0|  0.000|  0.000|    40|  1628.797| 34.903|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    26|  2407.630| 26.457|  10,799|
| |Luce County|     0|  0.000|  0.000|     4|   642.158| 22.934|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    74|  3400.579| 32.824|  21,761|
| |Lake County|     0|  0.000|  0.000|    27|  2277.904| 96.419|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    51|  1429.212|  8.007|  35,684|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,450| 1248.146| N/A|50,566| 14182.869| N/A|3,565,287|
| |Hartford County| 1,416| 1587.942|  0.320|12,855| 14415.960| 17.622| 891,720|
| |Fairfield County| 1,410| 1494.702|  0.606|18,126| 19214.868| 30.288| 943,332|
| |New Haven County| 1,109| 1297.445|  0.836|13,272| 15527.220| 24.067| 854,757|
| |Middlesex County|   192| 1182.004|  0.879| 1,411|  8686.498| 14.071| 162,436|
| |Litchfield County|   139| 770.796|  0.792| 1,620|  8983.381| 10.298| 180,333|
| |New London County|   104| 392.148|  0.539| 1,475|  5561.714| 23.701| 265,206|
| |Tolland County|    65| 431.260|  0.000| 1,056|  7006.323|  0.948| 150,721|
| |Windham County|    15| 128.444|  0.000|   751|  6430.786| 33.029| 116,782|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,432| 417.427| N/A|209,226| 19705.912| N/A|10,617,423|
| |Fulton County|   462| 434.236|  6.982|21,373| 20088.595| 287.745|1,063,937|
| |Cobb County|   332| 436.761|  3.571|14,463| 19026.733| 327.947| 760,141|
| |Gwinnett County|   282| 301.202|  5.798|20,900| 22323.097| 312.188| 936,250|
| |DeKalb County|   251| 330.569|  3.198|14,563| 19179.583| 249.479| 759,297|
| |Dougherty County|   172| 1955.523|  3.248| 2,776| 31561.235| 186.782|  87,956|
| |Clayton County|   115| 393.491|  5.866| 5,301| 18138.208| 249.781| 292,256|
| |Muscogee County|   105| 536.346| 10.946| 4,930| 25182.741| 303.565| 195,769|
| |Hall County|   103| 503.813| 10.482| 6,339| 31006.501| 343.795| 204,441|
| |Richmond County|    95| 469.094|  5.643| 4,718| 23296.695| 517.767| 202,518|
| |Chatham County|    90| 310.956|  7.897| 6,040| 20868.604| 295.655| 289,430|
| |Bibb County|    75| 489.687|  8.395| 3,835| 25039.338| 410.405| 153,159|
| |Troup County|    73| 1044.020| 12.259| 2,354| 33666.085| 236.999|  69,922|
| |Cherokee County|    66| 255.050|  4.416| 3,796| 14669.227| 353.868| 258,773|
| |Bartow County|    64| 594.034|  3.978| 1,968| 18266.535| 259.890| 107,738|
| |Houston County|    62| 392.746|  9.954| 2,079| 13169.647| 188.228| 157,863|
| |Henry County|    56| 238.744|  7.308| 3,537| 15079.233| 214.991| 234,561|
| |Douglas County|    56| 382.663|  5.857| 2,812| 19215.132| 311.401| 146,343|
| |Sumter County|    56| 1896.762|  0.000|   768| 26012.735| 125.806|  29,524|
| |Glynn County|    53| 621.395| 18.424| 2,672| 31327.674| 418.730|  85,292|
| |Carroll County|    52| 433.362|  5.953| 1,933| 16109.407| 145.248| 119,992|
| |Habersham County|    51| 1125.132|  9.455| 1,183| 26098.659| 255.282|  45,328|
| |Lowndes County|    50| 425.873| 15.818| 3,257| 27741.342| 219.020| 117,406|
| |Upson County|    49| 1861.702| 16.283|   574| 21808.511| 423.361|  26,320|
| |Newton County|    46| 411.655| 14.063| 1,914| 17128.436| 282.534| 111,744|
| |Thomas County|    44| 989.854|  9.641| 1,147| 25803.694| 289.243|  44,451|
| |Tift County|    44| 1082.571| 31.634| 1,380| 33953.351| 291.732|  40,644|
| |Baldwin County|    42| 935.620| 12.730| 1,115| 24838.494| 334.150|  44,890|
| |Spalding County|    42| 629.657|  2.142|   990| 14841.911| 207.744|  66,703|
| |Mitchell County|    41| 1875.314|  0.000|   659| 30142.249| 163.355|  21,863|
| |Walton County|    40| 422.864|  1.510| 1,210| 12791.644| 250.698|  94,593|
| |Butts County|    39| 1564.004| 11.458|   497| 19931.023| 120.308|  24,936|
| |Hancock County|    35| 4138.583| 16.892|   331| 39139.175| 557.442|   8,457|
| |Whitfield County|    34| 324.961|  8.192| 3,654| 34923.730| 404.153| 104,628|
| |Barrow County|    33| 396.444|  1.716| 1,367| 16422.393| 262.580|  83,240|
| |Early County|    32| 3140.334| 14.019|   373| 36604.514| 252.348|  10,190|
| |Fayette County|    32| 279.669|  7.491| 1,210| 10574.982| 203.509| 114,421|
| |Ware County|    31| 867.521| 23.987| 1,186| 33189.679| 291.839|  35,734|
| |Terrell County|    30| 3516.587|  0.000|   307| 35986.403| 184.202|   8,531|
| |Coffee County|    30| 693.273| 16.506| 1,537| 35518.684| 399.457|  43,273|
| |Monroe County|    29| 1051.563| 20.720|   474| 17187.613| 170.944|  27,578|
| |Columbia County|    28| 178.669|  6.381| 2,456| 15671.861| 335.461| 156,714|
| |Forsyth County|    26| 106.447|  2.340| 2,455| 10051.095| 216.989| 244,252|
| |Coweta County|    26| 175.074|  3.848| 1,625| 10942.098| 192.389| 148,509|
| |Randolph County|    26| 3835.940|  0.000|   276| 40719.976| 210.766|   6,778|
| |Paulding County|    25| 148.221|  3.388| 1,809| 10725.275| 195.652| 168,667|
| |Colquitt County|    24| 526.316|  6.266| 1,586| 34780.702| 203.634|  45,600|
| |Rockdale County|    24| 264.038| 11.002| 1,411| 15523.235| 265.610|  90,896|
| |Jenkins County|    24| 2766.252|  0.000|   256| 29506.685| 329.316|   8,676|
| |Gordon County|    23| 396.805|  0.000| 1,285| 22169.315| 441.168|  57,963|
| |Lee County|    23| 766.871|  4.763|   569| 18971.726| 200.053|  29,992|
| |Worth County|    23| 1135.971|  0.000|   461| 22768.805| 148.170|  20,247|
| |Clarke County|    19| 148.055|  1.113| 2,166| 16878.229| 302.788| 128,331|
| |Wilcox County|    19| 2200.347| 16.544|   188| 21771.859| 198.528|   8,635|
| |Appling County|    19| 1033.395|  0.000|   733| 39867.290| 885.767|  18,386|
| |Putnam County|    18| 813.780|  6.459|   454| 20525.340| 342.304|  22,119|
| |Turner County|    18| 2254.227|  0.000|   260| 32561.052| 411.486|   7,985|
| |Floyd County|    18| 182.745|  1.450| 1,692| 17178.014| 440.908|  98,498|
| |Harris County|    17| 482.461|  4.054|   674| 19128.164| 150.009|  35,236|
| |Laurens County|    17| 357.548| 27.041| 1,075| 22609.683| 742.138|  47,546|
| |Bulloch County|    17| 213.546|  5.384| 1,338| 16807.356| 292.505|  79,608|
| |Brooks County|    17| 1099.825|  0.000|   419| 27107.459| 360.447|  15,457|
| |Jackson County|    17| 232.950|  7.830| 1,122| 15374.707| 205.544|  72,977|
| |Decatur County|    16| 605.969| 32.463|   837| 31699.742| 589.737|  26,404|
| |Walker County|    16| 229.355|  0.000|   760| 10894.339| 255.976|  69,761|
| |Oconee County|    15| 372.393|  0.000|   459| 11395.233| 145.411|  40,280|
| |Peach County|    15| 544.544| 15.558|   411| 14920.497| 269.679|  27,546|
| |Crisp County|    15| 670.481|  6.386|   401| 17924.191| 197.952|  22,372|
| |Dooly County|    14| 1045.556|  0.000|   262| 19566.841| 181.372|  13,390|
| |Stephens County|    14| 540.019| 11.021|   676| 26075.217| 484.915|  25,925|
| |Lamar County|    13| 681.449| 14.977|   283| 14834.618| 194.700|  19,077|
| |Greene County|    12| 654.879|  7.796|   339| 18500.327| 405.401|  18,324|
| |Wayne County|    12| 400.976| 23.868|   846| 28268.787| 692.160|  29,927|
| |Wilkinson County|    12| 1340.183| 31.909|   223| 24905.070| 351.000|   8,954|
| |Telfair County|    12| 756.620| 45.037|   299| 18852.459| 234.192|  15,860|
| |Johnson County|    12| 1244.426| 14.815|   253| 26236.648| 325.921|   9,643|
| |Polk County|    11| 258.137|  0.000|   901| 21143.782| 529.684|  42,613|
| |Emanuel County|    11| 485.737| 12.617|   547| 24154.376| 555.128|  22,646|
| |Catoosa County|    11| 162.770|  4.228|   686| 10150.932| 196.592|  67,580|
| |McDuffie County|    10| 469.219|  0.000|   389| 18252.628| 482.625|  21,312|
| |Bleckley County|    10| 776.820| 44.390|   260| 20197.312| 1043.158|  12,873|
| |Macon County|    10| 772.380|  0.000|   185| 14289.024| 99.306|  12,947|
| |Stewart County|     9| 1359.311| 86.305|   257| 38815.889| 64.729|   6,621|
| |Pierce County|     9| 462.368| 22.018|   429| 22039.558| 308.246|  19,465|
| |Screven County|     9| 644.422|  0.000|   220| 15752.542| 358.012|  13,966|
| |Toombs County|     9| 335.445| 10.649|   816| 30413.716| 622.970|  26,830|
| |Jefferson County|     9| 585.861| 18.599|   536| 34891.290| 623.059|  15,362|
| |Bacon County|     8| 716.589| 25.592|   452| 40487.281| 358.295|  11,164|
| |Jeff Davis County|     8| 529.276|  0.000|   491| 32484.287| 689.948|  15,115|
| |Hart County|     8| 305.285| 21.806|   331| 12631.177| 256.222|  26,205|
| |Bryan County|     8| 201.883|  0.000|   701| 17689.959| 335.269|  39,627|
| |Candler County|     7| 647.968| 39.672|   271| 25085.624| 370.268|  10,803|
| |Burke County|     7| 312.737|  0.000|   508| 22695.796| 453.150|  22,383|
| |Oglethorpe County|     7| 458.746|  0.000|   238| 15597.352| 346.400|  15,259|
| |Grady County|     7| 284.172| 11.599|   538| 21840.620| 492.951|  24,633|
| |Union County|     7| 285.586|  0.000|   313| 12769.777| 413.808|  24,511|
| |Haralson County|     7| 234.962|  4.795|   237|  7955.156| 148.650|  29,792|
| |Madison County|     7| 234.270|  9.562|   428| 14323.963| 272.519|  29,880|
| |Lumpkin County|     7| 208.271|  4.250|   381| 11335.912| 259.277|  33,610|
| |Liberty County|     7| 113.942|  9.301|   784| 12761.455| 251.137|  61,435|
| |White County|     6| 194.818|  4.639|   376| 12208.585| 259.757|  30,798|
| |Pike County|     6| 316.422| 15.068|   232| 12234.996| 241.084|  18,962|
| |Meriwether County|     6| 283.460|  0.000|   411| 19417.017| 256.464|  21,167|
| |Cook County|     6| 347.423|  0.000|   456| 26404.169| 248.159|  17,270|
| |Franklin County|     6| 256.970|  6.118|   434| 18587.520| 269.207|  23,349|
| |Calhoun County|     6| 969.462|  0.000|   211| 34092.745| 253.907|   6,189|
| |Brantley County|     6| 313.988| 14.952|   261| 13658.486| 171.946|  19,109|
| |Seminole County|     5| 618.047|  0.000|   229| 28306.551| 865.266|   8,090|
| |Fannin County|     5| 190.927| 10.910|   360| 13746.754| 310.938|  26,188|
| |Pickens County|     5| 153.417|  0.000|   430| 13193.827| 390.116|  32,591|
| |Marion County|     5| 598.158| 17.090|   157| 18782.151| 170.902|   8,359|
| |Lincoln County|     5| 631.233| 18.035|   154| 19441.990| 396.775|   7,921|
| |Effingham County|     5| 77.765|  8.887|   775| 12053.627| 202.190|  64,296|
| |Heard County|     5| 419.358| 11.982|   149| 12496.855| 119.816|  11,923|
| |Ben Hill County|     5| 299.401| 17.109|   495| 29640.719| 915.312|  16,700|
| |Banks County|     5| 259.956| 14.855|   288| 14973.484| 245.102|  19,234|
| |Dawson County|     5| 191.512| 10.944|   450| 17236.096| 629.254|  26,108|
| |Camden County|     5| 91.465|  2.613|   825| 15091.647| 292.686|  54,666|
| |Twiggs County|     4| 492.611| 17.593|   127| 15640.394| 369.458|   8,120|
| |Chattooga County|     4| 161.362|  5.763|   324| 13070.313| 535.952|  24,789|
| |Lanier County|     4| 383.767|  0.000|   227| 21778.759| 191.883|  10,423|
| |Gilmer County|     4| 127.514|  0.000|   658| 20976.123| 396.206|  31,369|
| |Clinch County|     4| 604.412|  0.000|   209| 31580.538| 604.412|   6,618|
| |Jones County|     4| 139.203|  4.972|   327| 11379.850| 169.032|  28,735|
| |Atkinson County|     3| 367.422| 17.496|   331| 40538.885| 437.407|   8,165|
| |Charlton County|     3| 224.014|  0.000|   444| 33154.122| 437.361|  13,392|
| |Dodge County|     3| 145.596|  0.000|   240| 11647.658| 270.392|  20,605|
| |Evans County|     3| 281.584| 26.818|   291| 27313.685| 737.483|  10,654|
| |Baker County|     3| 987.492|  0.000|    68| 22383.147| 235.117|   3,038|
| |Taylor County|     3| 374.065| 17.813|    99| 12344.140| 374.065|   8,020|
| |McIntosh County|     3| 208.652|  9.936|   201| 13979.691| 367.625|  14,378|
| |Pulaski County|     3| 269.372| 12.827|   132| 11852.384| 538.745|  11,137|
| |Treutlen County|     3| 434.720|  0.000|   135| 19562.382| 579.626|   6,901|
| |Wilkes County|     3| 306.843|  0.000|   196| 20047.049| 189.950|   9,777|
| |Rabun County|     3| 175.060|  0.000|   230| 13421.252| 225.077|  17,137|
| |Talbot County|     3| 484.262|  0.000|   143| 23083.132| 230.601|   6,195|
| |Jasper County|     2| 140.657| 10.047|   171| 12026.162| 221.032|  14,219|
| |Echols County|     2| 499.251|  0.000|   225| 56165.751| 285.286|   4,006|
| |Dade County|     2| 124.100|  8.864|   138|  8562.919| 150.693|  16,116|
| |Clay County|     2| 705.716|  0.000|    96| 33874.382| 554.491|   2,834|
| |Chattahoochee County|     2| 183.368| 13.098|   778| 71330.338| 576.301|  10,907|
| |Washington County|     2| 98.164|  0.000|   518| 25424.561| 490.822|  20,374|
| |Tattnall County|     2| 79.095|  5.650|   558| 22067.547| 519.768|  25,286|
| |Murray County|     2| 49.880|  0.000|   627| 15637.470| 224.461|  40,096|
| |Long County|     2| 102.255|  7.304|   136|  6953.321| 160.686|  19,559|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724|  0.000|   2,607|
| |Montgomery County|     2| 218.055| 15.575|   159| 17335.369| 202.480|   9,172|
| |Towns County|     2| 166.154| 11.868|   155| 12876.963| 367.913|  12,037|
| |Berrien County|     1| 51.554|  7.365|   324| 16703.614| 331.421|  19,397|
| |Schley County|     1| 190.223|  0.000|    77| 14647.137| 516.318|   5,257|
| |Quitman County|     1| 434.972|  0.000|    31| 13484.124| 124.278|   2,299|
| |Elbert County|     1| 52.100|  0.000|   376| 19589.455| 275.384|  19,194|
| |Glascock County|     1| 336.587| 48.084|    26|  8751.262| 96.168|   2,971|
| |Irwin County|     1| 106.202|  0.000|   174| 18479.184| 227.576|   9,416|
| |Warren County|     1| 190.331|  0.000|    89| 16939.475| 734.135|   5,254|
| |Wheeler County|     1| 127.307|  0.000|   100| 12730.745| 236.428|   7,855|
| |Taliaferro County|     0|  0.000|  0.000|    14|  9108.653| 185.891|   1,537|
| |Morgan County|     0|  0.000|  0.000|   301| 15615.273| 407.613|  19,276|
| |Miller County|     0|  0.000|  0.000|   152| 26582.721| 424.724|   5,718|
| |Crawford County|     0|  0.000|  0.000|   107|  8626.250| 80.619|  12,404|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,382| 602.029| N/A|190,793| 26212.449| N/A|7,278,717|
| |Maricopa County| 2,517| 561.152|  8.217|127,768| 28485.219| 119.307|4,485,414|
| |Pima County|   511| 487.931|  4.229|19,001| 18143.207| 232.985|1,047,279|
| |Yuma County|   291| 1361.168| 10.023|11,703| 54741.401| 224.523| 213,787|
| |Navajo County|   204| 1839.097|  9.015| 5,430| 48952.436| 128.788| 110,924|
| |Mohave County|   180| 848.332| 12.792| 3,285| 15482.065| 139.369| 212,181|
| |Pinal County|   164| 354.373|  5.248| 8,616| 18617.556| 90.445| 462,789|
| |Apache County|   140| 1947.501|  3.974| 3,218| 44764.700| 196.737|  71,887|
| |Coconino County|   119| 829.407|  3.983| 3,146| 21927.012| 102.556| 143,476|
| |Yavapai County|    71| 302.000|  3.646| 2,084|  8864.351| 89.932| 235,099|
| |Cochise County|    57| 452.661|  5.672| 1,747| 13873.668| 206.477| 125,922|
| |Santa Cruz County|    55| 1182.847| 12.289| 2,698| 58024.001| 168.978|  46,498|
| |Gila County|    41| 759.006| 13.223|   978| 18105.076| 248.594|  54,018|
| |Graham County|    19| 489.224| 25.749|   574| 14779.720| 205.989|  38,837|
| |La Paz County|    12| 568.505|  6.768|   488| 23119.197| 74.447|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,279| 920.454| N/A|135,199| 29082.596| N/A|4,648,794|
| |Orleans Parish|   565| 1448.183|  1.465|10,899| 27935.839| 119.370| 390,144|
| |Jefferson Parish|   529| 1223.141|  2.642|15,597| 36063.011| 196.535| 432,493|
| |East Baton Rouge Parish|   369| 838.524| 10.064|12,587| 28602.983| 276.262| 440,059|
| |Caddo Parish|   296| 1232.286|  4.163| 6,851| 28521.590| 169.499| 240,204|
| |St. Tammany Parish|   217| 833.273|  4.937| 5,429| 20847.173| 239.175| 260,419|
| |Calcasieu Parish|   154| 756.995| 16.853| 6,960| 34212.234| 186.089| 203,436|
| |Rapides Parish|   122| 941.010| 11.019| 3,410| 26301.987| 238.007| 129,648|
| |Ouachita Parish|   117| 763.314|  7.456| 5,027| 32796.404| 296.378| 153,279|
| |Lafourche Parish|   102| 1044.932|  8.781| 2,916| 29872.764| 288.308|  97,614|
| |Lafayette Parish|   100| 409.182|  5.261| 7,846| 32104.423| 246.678| 244,390|
| |St. John the Baptist Parish|    92| 2147.676|  3.335| 1,448| 33802.554| 163.410|  42,837|
| |St. Landry Parish|    92| 1120.257| 15.656| 2,841| 34594.029| 448.799|  82,124|
| |Acadia Parish|    88| 1418.325| 20.722| 2,673| 43081.634| 271.692|  62,045|
| |Terrebonne Parish|    86| 778.555|  2.587| 3,115| 28199.998| 225.031| 110,461|
| |Bossier Parish|    82| 645.471|  7.872| 2,428| 19112.241| 149.560| 127,039|
| |Ascension Parish|    79| 623.993|  9.027| 2,970| 23458.974| 227.932| 126,604|
| |Tangipahoa Parish|    78| 578.815|  9.541| 3,619| 26855.548| 304.249| 134,758|
| |Iberia Parish|    74| 1059.716|  8.183| 2,588| 37061.435| 310.959|  69,830|
| |St. Mary Parish|    59| 1195.591| 23.159| 1,658| 33598.119| 379.231|  49,348|
| |Washington Parish|    58| 1255.574|  0.000| 1,312| 28401.957| 238.126|  46,194|
| |St. Charles Parish|    55| 1035.782| 10.761| 1,515| 28531.073| 244.821|  53,100|
| |Livingston Parish|    54| 383.553|  4.059| 3,027| 21500.259| 230.335| 140,789|
| |Iberville Parish|    50| 1537.941| 13.182| 1,267| 38971.425| 333.953|  32,511|
| |St. Martin Parish|    46| 860.923|  8.021| 1,760| 32939.679| 403.725|  53,431|
| |East Feliciana Parish|    39| 2038.150| 29.863|   612| 31983.277| 462.877|  19,135|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   745| 28150.387| 302.286|  26,465|
| |Union Parish|    35| 1583.137| 12.924|   732| 33110.186| 407.092|  22,108|
| |Avoyelles Parish|    34| 846.951| 17.793| 1,128| 28098.844| 448.386|  40,144|
| |Pointe Coupee Parish|    33| 1518.638|  6.574|   818| 37643.810| 322.135|  21,730|
| |St. James Parish|    32| 1516.875|  0.000|   730| 34603.716| 331.816|  21,096|
| |Lincoln Parish|    32| 684.609| 12.225|   819| 17521.715| 198.659|  46,742|
| |Bienville Parish|    30| 2265.690|  0.000|   388| 29302.923| 280.514|  13,241|
| |Allen Parish|    30| 1170.640| 11.149| 1,332| 51976.431| 557.448|  25,627|
| |Vernon Parish|    29| 611.440| 12.048|   798| 16825.149| 177.709|  47,429|
| |Jefferson Davis Parish|    29| 924.509| 13.663| 1,056| 33664.881| 273.254|  31,368|
| |Vermilion Parish|    28| 470.501| 14.403| 1,689| 28381.308| 422.491|  59,511|
| |De Soto Parish|    27| 983.141|  5.202|   756| 27527.947| 265.292|  27,463|
| |St. Bernard Parish|    24| 508.001|  0.000| 1,125| 23812.548| 133.048|  47,244|
| |Beauregard Parish|    21| 560.045| 15.239|   868| 23148.519| 205.731|  37,497|
| |Assumption Parish|    20| 913.617|  0.000|   600| 27408.524| 202.301|  21,891|
| |Franklin Parish|    19| 949.288| 14.275|   964| 48163.877| 635.238|  20,015|
| |Grant Parish|    19| 848.631| 19.142|   335| 14962.705| 274.369|  22,389|
| |Plaquemines Parish|    19| 819.071|  0.000|   465| 20045.696| 203.228|  23,197|
| |West Feliciana Parish|    18| 1156.218| 18.353|   397| 25501.028| 587.285|  15,568|
| |Jackson Parish|    18| 1143.293|  0.000|   386| 24517.276| 163.328|  15,744|
| |Natchitoches Parish|    17| 445.516|  0.000|   816| 21384.769| 258.324|  38,158|
| |Webster Parish|    17| 443.401| 11.178|   916| 23891.497| 204.933|  38,340|
| |Morehouse Parish|    13| 522.634| 11.486|   542| 21789.821| 361.824|  24,874|
| |Red River Parish|    13| 1539.919| 33.844|   252| 29850.746| 693.810|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   290| 18506.701| 446.713|  15,670|
| |Sabine Parish|    11| 460.559|  5.981|   671| 28094.122| 358.877|  23,884|
| |Evangeline Parish|     9| 269.501| 25.667|   946| 28327.594| 474.836|  33,395|
| |Concordia Parish|     9| 467.314|  0.000|   352| 18277.169| 385.719|  19,259|
| |Richland Parish|     8| 397.575|  7.100|   624| 31010.834| 333.679|  20,122|
| |West Carroll Parish|     7| 646.353| 26.382|   302| 27885.503| 329.772|  10,830|
| |Winn Parish|     7| 503.452|  0.000|   453| 32580.552| 441.805|  13,904|
| |Madison Parish|     6| 547.895|  0.000|   628| 57346.361| 352.218|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   305| 32125.553| 436.366|   9,494|
| |Caldwell Parish|     3| 302.480| 14.404|   230| 23190.159| 331.288|   9,918|
| |St. Helena Parish|     2| 197.394| 14.100|   279| 27536.518| 366.590|  10,132|
| |LaSalle Parish|     2| 134.300|  0.000|   324| 21756.648| 537.201|  14,892|
| |East Carroll Parish|     2| 291.503| 20.822|   520| 75790.701| 124.930|   6,861|
| |Tensas Parish|     0|  0.000|  0.000|    91| 20996.770| 758.125|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   172| 24666.571| 102.436|   6,973|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,755| 321.239| N/A|105,426|  9019.172| N/A|11,689,100|
| |Franklin County|   533| 404.783|  1.302|19,124| 14523.572| 139.954|1,316,756|
| |Cuyahoga County|   519| 420.218|  3.239|13,999| 11334.562| 99.242|1,235,072|
| |Lucas County|   324| 756.394|  1.334| 5,544| 12942.747| 129.734| 428,348|
| |Hamilton County|   260| 318.053|  1.398| 9,917| 12131.288| 94.892| 817,473|
| |Mahoning County|   258| 1128.199|  2.499| 2,644| 11561.856| 104.324| 228,683|
| |Summit County|   224| 414.038|  1.584| 3,712|  6861.203| 73.671| 541,013|
| |Stark County|   142| 383.156|  1.927| 1,931|  5210.385| 63.602| 370,606|
| |Trumbull County|   111| 560.680|  4.330| 1,578|  7970.744| 69.995| 197,974|
| |Montgomery County|   101| 189.961|  3.762| 4,544|  8546.382| 99.414| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,867|  6025.827| 82.072| 309,833|
| |Butler County|    64| 167.043|  0.746| 3,070|  8012.862| 92.470| 383,134|
| |Portage County|    63| 387.773|  1.759|   780|  4801.005| 32.534| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,699| 16675.991| 113.576| 101,883|
| |Wayne County|    59| 509.895|  1.235|   567|  4900.181| 59.261| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,101|  8416.337| 117.940| 130,817|
| |Licking County|    51| 288.360|  3.231| 1,367|  7729.190| 133.276| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   580|  5964.562| 44.073|  97,241|
| |Allen County|    46| 449.434|  5.583|   817|  7982.335| 164.699| 102,351|
| |Geauga County|    45| 480.518|  1.525|   565|  6033.166| 25.933|  93,649|
| |Marion County|    45| 691.319|  0.000| 2,952| 45350.499| 92.176|  65,093|
| |Lake County|    43| 186.835|  3.104| 1,154|  5014.143| 50.278| 230,149|
| |Pickaway County|    42| 718.477|  0.000| 2,404| 41124.245| 63.539|  58,457|
| |Miami County|    39| 364.530|  2.671|   881|  8234.645| 93.469| 106,987|
| |Warren County|    39| 166.239|  1.827| 1,877|  8000.784| 101.083| 234,602|
| |Medina County|    36| 200.283|  0.795|   977|  5435.448| 71.530| 179,746|
| |Fairfield County|    33| 209.425|  1.813| 1,449|  9195.679| 126.924| 157,574|
| |Darke County|    29| 567.370|  5.590|   425|  8314.910| 181.670|  51,113|
| |Erie County|    28| 377.023|  1.924|   619|  8334.904| 121.186|  74,266|
| |Ottawa County|    27| 666.255|  7.050|   405|  9993.831| 130.431|  40,525|
| |Belmont County|    26| 388.025|  0.000|   628|  9372.295| 76.752|  67,006|
| |Washington County|    22| 367.211|  0.000|   212|  3538.582| 33.383|  59,911|
| |Delaware County|    19| 90.832|  0.000| 1,378|  6587.722| 78.539| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    94|  6884.429| 31.388|  13,654|
| |Putnam County|    17| 502.053|  0.000|   215|  6349.488| 67.503|  33,861|
| |Sandusky County|    17| 290.509|  2.441|   407|  6955.125| 107.415|  58,518|
| |Clark County|    15| 111.871|  1.065| 1,218|  9083.926| 109.740| 134,083|
| |Tuscarawas County|    14| 152.195|  0.000|   801|  8707.752| 60.568|  91,987|
| |Mercer County|    13| 315.749|  0.000|   668| 16224.619| 329.628|  41,172|
| |Richland County|    12| 99.047|  1.179|   626|  5166.978| 43.628| 121,154|
| |Hardin County|    12| 382.592|  0.000|   180|  5738.881| 95.648|  31,365|
| |Greene County|    12| 71.032|  0.846|   742|  4392.170| 72.724| 168,937|
| |Clermont County|    11| 53.287|  0.000|   981|  4752.262| 61.592| 206,428|
| |Madison County|    10| 223.559|  0.000|   580| 12966.399| 737.743|  44,731|
| |Hocking County|     9| 318.426|  0.000|   122|  4316.445| 40.435|  28,264|
| |Coshocton County|     9| 245.902| 11.710|   199|  5437.158| 42.935|  36,600|
| |Wyandot County|     9| 413.375|  6.562|   155|  7119.236| 124.669|  21,772|
| |Knox County|     9| 144.411|  4.584|   218|  3497.962| 61.891|  62,322|
| |Guernsey County|     7| 180.064|  0.000|   121|  3112.540| 25.723|  38,875|
| |Clinton County|     6| 142.966|  0.000|   174|  4146.016| 54.463|  41,968|
| |Auglaize County|     6| 131.418|  3.129|   286|  6264.237| 147.063|  45,656|
| |Holmes County|     6| 136.488|  0.000|   331|  7529.572| 16.249|  43,960|
| |Huron County|     5| 85.813|  0.000|   413|  7088.182| 61.295|  58,266|
| |Carroll County|     5| 185.777|  0.000|   114|  4235.714| 21.232|  26,914|
| |Crawford County|     5| 120.499|  0.000|   177|  4265.677| 20.657|  41,494|
| |Ross County|     4| 52.174|  0.000|   520|  6782.668| 141.616|  76,666|
| |Seneca County|     4| 72.493|  2.589|   242|  4385.806| 134.629|  55,178|
| |Defiance County|     4| 105.023|  0.000|   155|  4069.630| 82.518|  38,087|
| |Shelby County|     4| 82.321|  0.000|   219|  4507.100| 123.482|  48,590|
| |Ashland County|     3| 56.092|  0.000|   156|  2916.760| 50.749|  53,484|
| |Williams County|     3| 81.762|  0.000|   139|  3788.292| 35.041|  36,692|
| |Hancock County|     3| 39.587|  0.000|   410|  5410.184| 107.450|  75,783|
| |Jefferson County|     3| 45.924|  2.187|   240|  3673.938| 45.924|  65,325|
| |Perry County|     3| 83.024|  0.000|   164|  4538.662| 189.770|  36,134|
| |Preble County|     2| 48.921|  0.000|   219|  5356.881| 150.258|  40,882|
| |Morrow County|     2| 56.612|  0.000|   185|  5236.639| 80.875|  35,328|
| |Logan County|     2| 43.791|  0.000|   169|  3700.298| 90.709|  45,672|
| |Highland County|     2| 46.338|  3.310|   169|  3915.572| 76.127|  43,161|
| |Henry County|     2| 74.058|  0.000|   124|  4591.572| 58.188|  27,006|
| |Van Wert County|     2| 70.734|  5.052|    73|  2581.786| 15.157|  28,275|
| |Champaign County|     2| 51.434|  3.674|   192|  4937.637| 128.584|  38,885|
| |Athens County|     2| 30.615|  2.187|   364|  5571.969| 24.055|  65,327|
| |Adams County|     2| 72.207|  0.000|    68|  2455.051| 46.419|  27,698|
| |Brown County|     2| 46.049|  0.000|   150|  3453.675| 88.809|  43,432|
| |Vinton County|     2| 152.847|  0.000|    32|  2445.548| 21.835|  13,085|
| |Scioto County|     1| 13.278|  0.000|   260|  3452.213| 92.944|  75,314|
| |Union County|     1| 16.953|  0.000|   277|  4695.870| 106.559|  58,988|
| |Muskingum County|     1| 11.599|  0.000|   256|  2969.321| 67.936|  86,215|
| |Fulton County|     1| 23.738|  0.000|   158|  3750.653| 47.477|  42,126|
| |Gallia County|     1| 33.447|  0.000|    78|  2608.870| 76.450|  29,898|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 37.994|  15,040|
| |Fayette County|     0|  0.000|  0.000|   126|  4417.178| 85.138|  28,525|
| |Jackson County|     0|  0.000|  0.000|    78|  2406.442| 22.037|  32,413|
| |Pike County|     0|  0.000|  0.000|    80|  2880.599| 25.720|  27,772|
| |Paulding County|     0|  0.000|  0.000|    72|  3856.041| 61.207|  18,672|
| |Noble County|     0|  0.000|  0.000|    19|  1317.249| 19.808|  14,424|
| |Morgan County|     0|  0.000|  0.000|    31|  2136.752| 78.774|  14,508|
| |Meigs County|     0|  0.000|  0.000|    63|  2750.251| 187.092|  22,907|
| |Lawrence County|     0|  0.000|  0.000|   323|  5431.949| 194.599|  59,463|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,608| 596.790| N/A|98,160| 16236.387| N/A|6,045,680|
| |Baltimore County| 1,007| 1217.110|  4.835|26,656| 32217.750| 311.486| 827,370|
| |Montgomery County|   807| 768.068|  1.360|18,752| 17847.353| 97.895|1,050,688|
| |Prince George's County|   766| 842.381|  2.828|24,301| 26724.160| 169.042| 909,327|
| |Anne Arundel County|   228| 393.623|  1.973| 7,528| 12996.475| 80.895| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,154| 12151.942| 67.150| 259,547|
| |Carroll County|   118| 700.517|  0.848| 1,583|  9397.615| 56.822| 168,447|
| |Howard County|   112| 343.885|  2.632| 3,967| 12180.294| 104.394| 325,690|
| |Charles County|    92| 563.529|  0.875| 2,102| 12875.405| 123.381| 163,257|
| |Harford County|    69| 270.121|  0.000| 2,055|  8044.911| 83.329| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,022|  9003.612| 89.357| 113,510|
| |Wicomico County|    45| 434.325|  0.000| 1,374| 13261.396| 71.698| 103,609|
| |Washington County|    31| 205.231|  0.000| 1,066|  7057.313| 66.204| 151,049|
| |Cecil County|    30| 291.673|  0.000|   715|  6951.534| 47.223| 102,855|
| |Calvert County|    28| 302.621|  0.000|   724|  7824.912| 88.007|  92,525|
| |Queen Anne's County|    26| 516.068|  2.836|   446|  8852.544| 113.421|  50,381|
| |Kent County|    23| 1184.224|  0.000|   242| 12460.097| 44.133|  19,422|
| |Worcester County|    20| 382.585|  0.000|   707| 13524.371| 117.508|  52,276|
| |Allegany County|    18| 255.624|  0.000|   312|  4430.811| 66.949|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   393| 12308.560| 147.649|  31,929|
| |Talbot County|     4| 107.582|  0.000|   411| 11054.033| 153.688|  37,181|
| |Caroline County|     3| 89.804|  0.000|   455| 13620.308| 47.040|  33,406|
| |Somerset County|     3| 117.114|  0.000|   141|  5504.372| 61.346|  25,616|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    54|  1861.170| 44.314|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,898| 430.467| N/A|77,565| 11521.461| N/A|6,732,219|
| |Marion County|   733| 759.915|  1.481|16,304| 16902.658| 145.437| 964,582|
| |Lake County|   283| 582.913|  2.648| 7,840| 16148.534| 146.243| 485,493|
| |Allen County|   164| 432.377|  1.507| 4,103| 10817.324| 142.368| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,800| 11380.376| 95.740| 158,167|
| |Hendricks County|   109| 640.006|  2.516| 1,972| 11578.818| 132.531| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,941|  8700.900| 139.894| 338,011|
| |Elkhart County|    87| 421.632|  4.846| 4,992| 24192.962| 193.162| 206,341|
| |St. Joseph County|    83| 305.342|  2.102| 3,681| 13541.751| 199.708| 271,826|
| |Madison County|    66| 509.381|  1.103| 1,048|  8088.354| 168.691| 129,569|
| |Howard County|    65| 787.459|  0.000|   938| 11363.636| 143.646|  82,544|
| |Delaware County|    52| 455.601|  0.000|   768|  6728.874| 110.145| 114,135|
| |Floyd County|    50| 636.764|  9.097|   837| 10659.433| 176.475|  78,522|
| |Clark County|    50| 422.647|  4.830| 1,333| 11267.772| 223.399| 118,302|
| |Bartholomew County|    47| 561.000|  0.000|   844| 10074.124| 153.465|  83,779|
| |Boone County|    46| 678.036|  0.000|   704| 10376.900| 107.391|  67,843|
| |Porter County|    39| 228.888|  0.000| 1,391|  8163.673| 128.278| 170,389|
| |Hancock County|    39| 498.925|  1.828|   694|  8878.313| 102.344|  78,168|
| |Morgan County|    35| 496.531|  2.027|   492|  6979.812| 83.093|  70,489|
| |Greene County|    34| 1065.096|  0.000|   256|  8019.548| 67.128|  31,922|
| |Monroe County|    32| 215.588|  1.925|   777|  5234.756| 66.409| 148,431|
| |Decatur County|    32| 1204.865|  0.000|   347| 13065.251| 123.714|  26,559|
| |Warrick County|    30| 476.206|  0.000|   600|  9524.112| 106.579|  62,998|
| |Grant County|    30| 456.142|  2.172|   532|  8088.917| 26.065|  65,769|
| |LaPorte County|    30| 273.005|  0.000|   957|  8708.867| 114.402| 109,888|
| |Noble County|    29| 607.406|  0.000|   708| 14829.088| 188.505|  47,744|
| |Shelby County|    28| 625.992|  3.194|   572| 12788.124| 118.172|  44,729|
| |Dearborn County|    28| 566.137|  0.000|   522| 10554.410| 124.204|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   358|  7890.677| 66.123|  45,370|
| |Harrison County|    24| 592.373|  3.526|   355|  8762.187| 162.197|  40,515|
| |Orange County|    24| 1221.623|  0.000|   179|  9111.269| 94.530|  19,646|
| |Marshall County|    23| 497.211|  3.088|   801| 17315.924| 132.796|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   363|  9468.413| 63.346|  38,338|
| |Daviess County|    20| 599.682|  0.000|   284|  8515.487| 107.086|  33,351|
| |Henry County|    20| 416.910|  2.978|   460|  9588.927| 270.991|  47,972|
| |Tipton County|    16| 1056.245| 94.308|   154| 10166.359| 235.769|  15,148|
| |Franklin County|    15| 659.109| 12.554|   249| 10941.207| 94.158|  22,758|
| |Vanderburgh County|    15| 82.667|  1.575| 2,082| 11474.172| 188.953| 181,451|
| |Vigo County|    13| 121.452|  4.004|   752|  7025.542| 278.940| 107,038|
| |Perry County|    13| 678.178|  7.453|   188|  9807.502| 67.073|  19,169|
| |Tippecanoe County|    12| 61.308|  0.730| 1,263|  6452.701| 85.394| 195,732|
| |Jennings County|    12| 432.666|  0.000|   232|  8364.882| 87.563|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   872| 10974.627| 80.907|  79,456|
| |Dubois County|    12| 280.794|  0.000|   718| 16800.824| 200.567|  42,736|
| |White County|    11| 456.394|  5.927|   380| 15766.326| 171.889|  24,102|
| |Newton County|    10| 715.103|  0.000|   121|  8652.746| 71.510|  13,984|
| |Scott County|    10| 418.883|  0.000|   278| 11644.955| 125.665|  23,873|
| |Wayne County|    10| 151.782|  0.000|   402|  6101.633| 121.426|  65,884|
| |LaGrange County|    10| 252.436|  0.000|   569| 14363.609| 54.093|  39,614|
| |Cass County|     9| 238.796|  0.000| 1,809| 47998.090| 162.988|  37,689|
| |Ripley County|     8| 282.446|  5.044|   220|  7767.265| 131.136|  28,324|
| |Putnam County|     8| 212.902|  0.000|   328|  8728.976| 193.893|  37,576|
| |Fayette County|     7| 303.004|  0.000|   205|  8873.691| 173.145|  23,102|
| |Starke County|     7| 304.414|  0.000|   181|  7871.276| 43.488|  22,995|
| |Ohio County|     6| 1021.277| 48.632|    65| 11063.830| 194.529|   5,875|
| |Whitley County|     6| 176.658|  0.000|   160|  4710.870| 54.680|  33,964|
| |Wabash County|     5| 161.311|  9.218|   179|  5774.939| 82.960|  30,996|
| |Clay County|     5| 190.658|  0.000|   141|  5376.549| 201.552|  26,225|
| |Randolph County|     5| 202.716|  5.792|   132|  5351.713| 104.254|  24,665|
| |Jackson County|     5| 113.043|  0.000|   606| 13700.798| 142.111|  44,231|
| |Clinton County|     4| 123.461|  4.409|   456| 14074.508| 229.284|  32,399|
| |Gibson County|     4| 118.839|  0.000|   243|  7219.466| 148.549|  33,659|
| |DeKalb County|     4| 92.007|  0.000|   242|  5566.417| 62.433|  43,475|
| |Rush County|     4| 241.240|  0.000|    91|  5488.209| 172.314|  16,581|
| |Huntington County|     3| 82.147|  0.000|   130|  3559.693| 35.206|  36,520|
| |Steuben County|     3| 86.720|  0.000|   217|  6272.764| 53.684|  34,594|
| |Spencer County|     3| 147.951|  0.000|   139|  6855.057| 140.906|  20,277|
| |Carroll County|     3| 148.097|  7.052|   203| 10021.227| 324.403|  20,257|
| |Miami County|     2| 56.313|  0.000|   279|  7855.614| 60.335|  35,516|
| |Jefferson County|     2| 61.904|  0.000|   172|  5323.759| 84.013|  32,308|
| |Wells County|     2| 70.681|  0.000|   178|  6290.642| 121.168|  28,296|
| |Jasper County|     2| 59.591|  0.000|   259|  7717.061| 170.261|  33,562|
| |Fulton County|     2| 100.130|  0.000|   174|  8711.325| 107.282|  19,974|
| |Blackford County|     2| 170.097|  0.000|    66|  5613.200| 85.048|  11,758|
| |Brown County|     2| 132.521|  9.466|    75|  4969.520| 37.863|  15,092|
| |Fountain County|     2| 122.354|  0.000|    76|  4649.456| 104.875|  16,346|
| |Adams County|     2| 55.902|  0.000|   120|  3354.110| 123.783|  35,777|
| |Owen County|     1| 48.079|  0.000|   110|  5288.716| 185.448|  20,799|
| |Washington County|     1| 35.668|  0.000|   148|  5278.927| 137.578|  28,036|
| |Warren County|     1| 120.992|  0.000|    25|  3024.803| 86.423|   8,265|
| |Sullivan County|     1| 48.382|  0.000|   152|  7354.008| 421.611|  20,669|
| |Pulaski County|     1| 80.952|  0.000|    84|  6799.968| 104.081|  12,353|
| |Parke County|     1| 59.042|  0.000|    59|  3483.498| 75.912|  16,937|
| |Knox County|     1| 27.327|  3.904|   168|  4590.917| 101.500|  36,594|
| |Vermillion County|     0|  0.000|  0.000|    61|  3935.992| 119.831|  15,498|
| |Martin County|     0|  0.000|  0.000|    50|  4875.670| 111.444|  10,255|
| |Union County|     0|  0.000|  0.000|    41|  5812.305| 121.512|   7,054|
| |Switzerland County|     0|  0.000|  0.000|    56|  5208.818| 159.454|  10,751|
| |Posey County|     0|  0.000|  0.000|   181|  7118.417| 89.893|  25,427|
| |Pike County|     0|  0.000|  0.000|    66|  5327.306| 161.434|  12,389|
| |Jay County|     0|  0.000|  0.000|    94|  4599.726| 69.905|  20,436|
| |Crawford County|     0|  0.000|  0.000|    48|  4538.149| 54.026|  10,577|
| |Benton County|     0|  0.000|  0.000|    63|  7201.646| 48.991|   8,748|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,363| 276.843| N/A|103,622| 12140.094| N/A|8,535,519|
| |Fairfax County|   537| 467.961|  0.373|16,795| 14635.757| 78.056|1,147,532|
| |Henrico County|   187| 565.265|  2.159| 3,999| 12088.218| 110.980| 330,818|
| |Prince William County|   178| 378.454|  0.304| 9,686| 20593.832| 158.853| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,134| 13232.450| 72.984| 236,842|
| |Loudoun County|   115| 278.088|  0.000| 5,403| 13065.305| 87.399| 413,538|
| |Chesterfield County|    80| 226.756|  1.215| 4,512| 12789.043| 119.857| 352,802|
| |Alexandria city|    60| 376.345|  0.000| 3,020| 18942.720| 119.176| 159,428|
| |Virginia Beach city|    54| 120.007|  0.635| 5,204| 11565.113| 173.343| 449,974|
| |Suffolk city|    53| 575.411|  6.204| 1,351| 14667.564| 259.013|  92,108|
| |Shenandoah County|    46| 1054.659|  9.826|   728| 16691.123| 127.738|  43,616|
| |Richmond County|    45| 4987.255|  0.000| 3,601| 399091.211| 3419.832|   9,023|
| |Chesapeake city|    41| 167.460|  2.334| 3,082| 12588.070| 187.298| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,570| 11525.897| 156.266| 136,215|
| |Hanover County|    33| 306.219|  1.326|   676|  6272.850| 80.863| 107,766|
| |Norfolk city|    33| 135.947|  2.354| 3,858| 15893.418| 213.042| 242,742|
| |Mecklenburg County|    32| 1046.196|  0.000|   449| 14679.439| 415.676|  30,587|
| |Harrisonburg city|    31| 584.729|  2.695| 1,086| 20484.382| 43.114|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   297| 25362.938| 24.399|  11,710|
| |Portsmouth city|    25| 264.836|  0.000| 1,907| 20201.699| 349.584|  94,398|
| |Galax city|    25| 3938.869| 22.508|   352| 55459.272| 225.078|   6,347|
| |Page County|    25| 1045.938|  5.977|   349| 14601.289| 83.675|  23,902|
| |Colonial Heights city|    22| 1266.552|  8.224|   204| 11744.387| 123.365|  17,370|
| |Manassas city|    22| 535.475|  6.954| 1,679| 40866.496| 187.764|  41,085|
| |Newport News city|    20| 111.592|  1.594| 1,898| 10590.040| 129.127| 179,225|
| |Rockingham County|    20| 244.057|  3.487|   963| 11751.355| 66.244|  81,948|
| |Roanoke County|    19| 201.728|  1.517| 1,547| 16424.946| 156.226|  94,186|
| |Petersburg city|    19| 606.138|  0.000|   531| 16939.960| 173.182|  31,346|
| |Accomack County|    17| 526.055|  4.421| 1,111| 34379.255| 114.936|  32,316|
| |James City County|    17| 222.155|  1.867|   624|  8154.411| 91.476|  76,523|
| |Albemarle County|    16| 146.346|  0.000|   869|  7948.413| 92.773| 109,330|
| |Emporia city|    15| 2805.836|  0.000|   182| 34044.145| 267.222|   5,346|
| |Charlottesville city|    15| 317.353|  0.000|   554| 11720.899| 148.098|  47,266|
| |Nottoway County|    14| 919.118| 37.515|   183| 12014.181| 46.894|  15,232|
| |Carroll County|    14| 469.941|  9.591|   335| 11245.007| 124.678|  29,791|
| |Southampton County|    13| 737.338|  0.000|   278| 15767.682| 234.976|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,021| 19408.801| 119.489|  52,605|
| |Greensville County|    11| 970.360|  0.000|   535| 47194.778| 1184.595|  11,336|
| |Stafford County|    10| 65.410|  1.869| 1,446|  9458.275| 121.476| 152,882|
| |Prince Edward County|    10| 438.558|  0.000|   427| 18726.428| 238.074|  22,802|
| |Fluvanna County|     9| 330.033|  0.000|   197|  7224.056| 94.295|  27,270|
| |Fauquier County|     9| 126.365|  0.000|   624|  8761.338| 64.186|  71,222|
| |Frederick County|     9| 100.769|  0.000|   688|  7703.246| 20.794|  89,313|
| |Henry County|     9| 178.017|  5.651|   644| 12738.098| 285.392|  50,557|
| |Isle of Wight County|     9| 242.529|  0.000|   415| 11183.271| 173.235|  37,109|
| |Sussex County|     9| 806.524|  0.000|   313| 28049.108| 384.059|  11,159|
| |Buckingham County|     8| 466.527|  0.000|   612| 35689.293| 116.632|  17,148|
| |Bedford County|     8| 101.270|  1.808|   377|  4772.333| 90.419|  78,997|
| |Danville city|     8| 199.780|  3.568|   430| 10738.188| 242.590|  40,044|
| |Dinwiddie County|     7| 245.235|  0.000|   226|  7917.601| 75.072|  28,544|
| |Manassas Park city|     7| 400.503|  0.000|   520| 29751.688| 114.430|  17,478|
| |Hampton city|     7| 52.041|  0.000| 1,291|  9597.799| 169.929| 134,510|
| |Franklin County|     7| 124.906|  0.000|   378|  6744.941| 145.299|  56,042|
| |Goochland County|     7| 294.700|  0.000|   169|  7114.891| 72.171|  23,753|
| |Botetourt County|     7| 209.462|  0.000|   217|  6493.312| 72.670|  33,419|
| |Washington County|     6| 111.649|  2.658|   242|  4503.163| 103.674|  53,740|
| |Williamsburg city|     6| 401.230|  0.000|   130|  8693.326| 105.084|  14,954|
| |Warren County|     6| 149.388|  0.000|   360|  8963.251| 24.898|  40,164|
| |Falls Church city|     6| 410.481|  0.000|    63|  4310.050| 29.320|  14,617|
| |Charles City County|     5| 718.081|  0.000|    53|  7611.662| 41.033|   6,963|
| |Grayson County|     5| 321.543|  0.000|   157| 10096.463| 110.243|  15,550|
| |Lynchburg city|     5| 60.851|  1.739|   680|  8275.728| 288.607|  82,168|
| |Caroline County|     5| 162.734|  0.000|   221|  7192.840| 125.538|  30,725|
| |Hopewell city|     5| 221.936|  0.000|   279| 12384.038| 120.480|  22,529|
| |Augusta County|     4| 52.939|  0.000|   296|  3917.520| 66.174|  75,558|
| |Alleghany County|     4| 269.179|  0.000|    62|  4172.275| 38.454|  14,860|
| |Powhatan County|     4| 134.898|  0.000|   156|  5261.028| 101.174|  29,652|
| |Patrick County|     4| 227.169|  0.000|   167|  9484.325| 332.641|  17,608|
| |King George County|     4| 149.054|  0.000|   158|  5887.614| 175.670|  26,836|
| |York County|     4| 58.582|  0.000|   383|  5609.256| 94.150|  68,280|
| |Wise County|     4| 107.001|  3.821|   201|  5376.776| 347.752|  37,383|
| |Winchester city|     4| 142.460|  0.000|   408| 14530.949| 61.054|  28,078|
| |Fredericksburg city|     4| 137.760|  4.920|   421| 14499.242| 162.360|  29,036|
| |Scott County|     3| 139.108|  0.000|   111|  5146.991| 298.088|  21,566|
| |Westmoreland County|     3| 166.528|  0.000|   216| 11990.008| 150.668|  18,015|
| |Montgomery County|     3| 30.446|  0.000|   313|  3176.536| 24.647|  98,535|
| |Wythe County|     3| 104.588|  0.000|   120|  4183.517| 59.765|  28,684|
| |Smyth County|     3| 99.655|  0.000|   158|  5248.472| 132.873|  30,104|
| |Martinsville city|     3| 238.968|  0.000|   229| 18241.198| 512.074|  12,554|
| |Waynesboro city|     3| 132.567|  0.000|   180|  7954.043| 82.066|  22,630|
| |Salem city|     3| 118.572|  0.000|   164|  6481.957| 62.109|  25,301|
| |Northumberland County|     3| 248.036| 11.811|    77|  6366.267| 94.490|  12,095|
| |Pulaski County|     3| 88.165|  0.000|    90|  2644.958| 33.587|  34,027|
| |Orange County|     3| 80.969|  0.000|   232|  6261.639| 38.557|  37,051|
| |Louisa County|     2| 53.204|  0.000|   198|  5267.218| 91.207|  37,591|
| |King William County|     2| 116.632|  0.000|    93|  5423.373| 116.632|  17,148|
| |Russell County|     2| 75.228|  0.000|   136|  5115.474| 241.803|  26,586|
| |Rappahannock County|     2| 271.370|  0.000|    44|  5970.149| 58.151|   7,370|
| |Amelia County|     2| 152.149|  0.000|    82|  6238.113| 54.339|  13,145|
| |Pittsylvania County|     2| 33.138|  0.000|   530|  8781.522| 326.644|  60,354|
| |Prince George County|     2| 52.147|  0.000|   424| 11055.198| 249.561|  38,353|
| |Surry County|     2| 311.429|  0.000|    52|  8097.166| 177.960|   6,422|
| |Campbell County|     2| 36.440|  0.000|   228|  4154.140| 135.348|  54,885|
| |Halifax County|     2| 58.978|  4.213|   160|  4718.233| 63.191|  33,911|
| |Floyd County|     2| 126.992|  9.071|   109|  6921.074| 598.677|  15,749|
| |Gloucester County|     2| 53.550|  0.000|   171|  4578.558| 91.801|  37,348|
| |Greene County|     2| 100.913|  0.000|   172|  8678.541| 136.954|  19,819|
| |Brunswick County|     2| 123.221|  0.000|   240| 14786.520| 211.236|  16,231|
| |Dickenson County|     1| 69.842|  0.000|    49|  3422.266| 109.752|  14,318|
| |Essex County|     1| 91.299|  0.000|   107|  9769.013| 299.983|  10,953|
| |Amherst County|     1| 31.641|  4.520|   196|  6201.550| 266.685|  31,605|
| |Buchanan County|     1| 47.610|  6.801|    81|  3856.408| 47.610|  21,004|
| |Rockbridge County|     1| 44.301|  0.000|    71|  3145.351| 31.643|  22,573|
| |Madison County|     1| 75.409|  0.000|    73|  5504.864| 96.955|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    66|  5411.610| 93.708|  12,196|
| |Lee County|     1| 42.693|  0.000|   135|  5763.566| 182.970|  23,423|
| |New Kent County|     1| 43.307|  0.000|   132|  5716.513| 61.867|  23,091|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 101.678|   7,025|
| |Middlesex County|     1| 94.500|  0.000|    49|  4630.505| 216.000|  10,582|
| |Buena Vista city|     1| 154.369|  0.000|    62|  9570.855| 264.632|   6,478|
| |Lancaster County|     0|  0.000|  0.000|    45|  4244.082| 175.153|  10,603|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 34.926|  12,271|
| |Bristol city|     0|  0.000|  0.000|    90|  5369.288| 161.931|  16,762|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418|  0.000|   5,538|
| |Norton city|     0|  0.000|  0.000|    22|  5526.250| 251.193|   3,981|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Lexington city|     0|  0.000|  0.000|    34|  4566.210| 19.186|   7,446|
| |Nelson County|     0|  0.000|  0.000|    57|  3817.816| 200.938|  14,930|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Bland County|     0|  0.000|  0.000|    27|  4299.363| 409.463|   6,280|
| |Appomattox County|     0|  0.000|  0.000|    93|  5845.013| 143.656|  15,911|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Charlotte County|     0|  0.000|  0.000|    55|  4629.630| 60.125|  11,880|
| |Tazewell County|     0|  0.000|  0.000|   126|  3103.831| 70.382|  40,595|
| |Mathews County|     0|  0.000|  0.000|    20|  2263.980| 64.685|   8,834|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Cumberland County|     0|  0.000|  0.000|    78|  7853.403| 86.301|   9,932|
| |Radford city|     0|  0.000|  0.000|    60|  3287.851| 187.877|  18,249|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Staunton city|     0|  0.000|  0.000|   155|  6216.910| 68.758|  24,932|
| |Giles County|     0|  0.000|  0.000|    27|  1614.833| 34.176|  16,720|
| |Craig County|     0|  0.000|  0.000|    18|  3508.088| 27.842|   5,131|
| |Clarke County|     0|  0.000|  0.000|    72|  4925.097| 29.316|  14,619|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 130.463|   2,190|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,287| 218.057| N/A|140,824| 13427.047| N/A|10,488,084|
| |Mecklenburg County|   246| 221.551|  3.088|22,803| 20536.657| 141.396|1,110,356|
| |Wake County|   179| 161.006|  3.469|12,406| 11158.873| 106.652|1,111,761|
| |Guilford County|   158| 294.132|  1.330| 5,826| 10845.648| 105.845| 537,174|
| |Durham County|    80| 248.843|  0.444| 6,298| 19590.156| 115.534| 321,488|
| |Gaston County|    56| 249.411|  5.726| 3,438| 15312.053| 137.431| 224,529|
| |Henderson County|    56| 476.933|  2.433| 1,517| 12919.765| 79.083| 117,417|
| |Chatham County|    55| 738.552|  5.755| 1,323| 17765.543| 93.998|  74,470|
| |Cumberland County|    55| 163.930|  1.703| 3,276|  9764.269| 108.577| 335,509|
| |Robeson County|    55| 421.053|  2.187| 2,856| 21864.115| 142.174| 130,625|
| |Forsyth County|    53| 138.636|  0.747| 5,440| 14229.849| 130.415| 382,295|
| |Buncombe County|    52| 199.088|  3.282| 1,965|  7523.230| 98.450| 261,191|
| |Cabarrus County|    50| 230.997|  0.660| 2,714| 12538.519| 128.038| 216,453|
| |Rowan County|    50| 351.895|  2.011| 2,291| 16123.811| 168.909| 142,088|
| |Columbus County|    48| 864.740|  0.000|   950| 17114.650| 221.332|  55,508|
| |Orange County|    48| 323.285|  1.924| 1,389|  9355.047| 70.237| 148,476|
| |Duplin County|    48| 817.146|  0.000| 2,017| 34337.175| 124.031|  58,741|
| |Johnston County|    45| 214.962|  0.000| 3,381| 16150.837| 141.943| 209,339|
| |Union County|    43| 179.272|  0.596| 3,222| 13432.892| 147.110| 239,859|
| |Wayne County|    42| 341.100|  2.320| 2,463| 20003.086| 105.579| 123,131|
| |Alamance County|    42| 247.774|  0.843| 2,567| 15143.739| 188.781| 169,509|
| |Vance County|    41| 920.624|  3.208|   793| 17806.220| 134.725|  44,535|
| |Harnett County|    40| 294.170|  1.051| 1,357|  9979.702| 144.984| 135,976|
| |Randolph County|    38| 264.501|  0.994| 2,211| 15389.755| 85.515| 143,667|
| |Wilson County|    36| 440.092|  1.746| 1,525| 18642.804| 85.574|  81,801|
| |Catawba County|    32| 200.563|  2.686| 2,203| 13807.497| 165.643| 159,551|
| |Stanly County|    31| 493.583| 15.922| 1,171| 18644.715| 388.953|  62,806|
| |Granville County|    29| 479.791|  4.727| 1,293| 21392.055| 198.534|  60,443|
| |Burke County|    27| 298.392|  0.000| 1,679| 18555.562| 66.309|  90,485|
| |Franklin County|    26| 373.108|  2.050|   905| 12987.013| 157.853|  69,685|
| |Cleveland County|    22| 224.611|  5.834| 1,255| 12813.052| 185.231|  97,947|
| |Davidson County|    22| 131.258|  3.409| 1,836| 10954.066| 108.245| 167,609|
| |Brunswick County|    22| 154.040|  3.001| 1,287|  9011.343| 56.015| 142,820|
| |New Hanover County|    21| 89.563|  0.609| 2,644| 11276.352| 47.523| 234,473|
| |Moore County|    20| 198.255|  0.000| 1,046| 10368.755| 110.457| 100,880|
| |Pasquotank County|    20| 502.210|  3.587|   430| 10797.509| 211.646|  39,824|
| |McDowell County|    19| 415.246| 18.733|   696| 15211.120| 106.153|  45,756|
| |Sampson County|    18| 283.326| 11.243| 1,504| 23673.482| 114.680|  63,531|
| |Haywood County|    18| 288.846| 18.339|   445|  7140.909| 160.470|  62,317|
| |Iredell County|    17| 93.506|  0.000| 1,912| 10516.705| 110.793| 181,806|
| |Craven County|    16| 156.649|  6.993|   742|  7264.610| 65.737| 102,139|
| |Northampton County|    16| 821.229|  0.000|   311| 15962.634|  0.000|  19,483|
| |Montgomery County|    14| 515.217|  0.000|   659| 24252.015| 78.860|  27,173|
| |Edgecombe County|    13| 252.565|  2.775|   691| 13424.775| 208.158|  51,472|
| |Rutherford County|    13| 193.946|  0.000|   787| 11741.187| 193.946|  67,029|
| |Onslow County|    12| 60.625|  1.443| 1,154|  5830.108| 100.320| 197,938|
| |Nash County|    12| 127.256|  0.000| 1,252| 13277.058| 216.638|  94,298|
| |Caldwell County|    12| 146.024|  0.000| 1,246| 15162.209| 116.472|  82,178|
| |Wilkes County|    12| 175.408|  4.176|   871| 12731.684| 227.613|  68,412|
| |Pitt County|    11| 60.860|  0.000| 2,161| 11956.269| 226.052| 180,742|
| |Hertford County|    11| 464.586|  0.000|   365| 15415.804| 313.746|  23,677|
| |Hoke County|    11| 199.153|  5.173|   761| 13777.746| 150.011|  55,234|
| |Lee County|    11| 178.054|  0.000| 1,311| 21220.803| 134.119|  61,779|
| |Lenoir County|    11| 196.608|  0.000|   600| 10724.052| 120.007|  55,949|
| |Lincoln County|    10| 116.129| 11.613|   893| 10370.336| 150.968|  86,111|
| |Surry County|    10| 139.309|  1.990|   974| 13568.672| 153.240|  71,783|
| |Richmond County|     9| 200.763|  0.000|   534| 11911.932| 114.722|  44,829|
| |Jackson County|     7| 159.315|  6.503|   460| 10469.298| 78.032|  43,938|
| |Halifax County|     7| 139.972|  2.857|   746| 14917.017| 222.813|  50,010|
| |Warren County|     6| 304.090|  0.000|   264| 13379.960| 72.402|  19,731|
| |Yadkin County|     6| 159.291|  0.000|   558| 14814.028| 128.950|  37,667|
| |Polk County|     6| 289.519|  6.893|   165|  7961.783| 117.186|  20,724|
| |Bladen County|     6| 183.363|  0.000|   634| 19375.344| 122.242|  32,722|
| |Martin County|     6| 267.380|  0.000|   265| 11809.269| 50.929|  22,440|
| |Bertie County|     5| 263.894|  0.000|   294| 15516.968| 233.735|  18,947|
| |Carteret County|     5| 71.970|  0.000|   362|  5210.657| 61.689|  69,473|
| |Davie County|     5| 116.697|  0.000|   430| 10035.943| 90.023|  42,846|
| |Scotland County|     5| 143.583| 12.307|   388| 11142.061| 278.962|  34,823|
| |Washington County|     4| 345.423|  0.000|   136| 11744.387| 61.683|  11,580|
| |Cherokee County|     4| 139.801|  4.993|   277|  9681.253| 59.915|  28,612|
| |Rockingham County|     4| 43.951|  0.000|   574|  6306.999| 102.030|  91,010|
| |Jones County|     4| 424.674|  0.000|    99| 10510.670| 303.338|   9,419|
| |Stokes County|     3| 65.802|  0.000|   295|  6470.575| 40.735|  45,591|
| |Pender County|     3| 47.574|  0.000|   675| 10704.091| 83.820|  63,060|
| |Mitchell County|     3| 200.481|  9.547|    81|  5412.991|  0.000|  14,964|
| |Anson County|     3| 122.719|  5.844|   358| 14644.523| 233.751|  24,446|
| |Greene County|     3| 142.389|  0.000|   336| 15947.601| 94.926|  21,069|
| |Chowan County|     2| 143.441| 10.246|   160| 11475.292| 122.950|  13,943|
| |Dare County|     2| 54.041|  0.000|   211|  5701.316| 23.160|  37,009|
| |Caswell County|     2| 88.480|  0.000|   198|  8759.512| 44.240|  22,604|
| |Camden County|     2| 184.043|  0.000|    76|  6993.651| 144.606|  10,867|
| |Beaufort County|     2| 42.559|  0.000|   419|  8916.032| 85.117|  46,994|
| |Alexander County|     2| 53.338|  0.000|   323|  8614.022| 106.675|  37,497|
| |Gates County|     2| 172.980|  0.000|    49|  4238.021| 49.423|  11,562|
| |Macon County|     2| 55.776|  0.000|   469| 13079.369| 35.856|  35,858|
| |Person County|     2| 50.646|  0.000|   234|  5925.551| 112.144|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    90|  6684.988| 148.555|  13,463|
| |Swain County|     2| 140.144|  0.000|   123|  8618.877| 160.165|  14,271|
| |Tyrrell County|     2| 498.008| 35.572|   100| 24900.398| 213.432|   4,016|
| |Transylvania County|     1| 29.082|  0.000|   146|  4246.038| 58.165|  34,385|
| |Madison County|     1| 45.966|  6.567|    48|  2206.389| 45.966|  21,755|
| |Pamlico County|     1| 78.579|  0.000|    73|  5736.288| 67.354|  12,726|
| |Ashe County|     1| 36.761|  0.000|   167|  6139.029| 131.288|  27,203|
| |Clay County|     0|  0.000|  0.000|    72|  6410.827|  0.000|  11,231|
| |Alleghany County|     0|  0.000|  0.000|   171| 15354.225| 76.964|  11,137|
| |Avery County|     0|  0.000|  0.000|    95|  5410.947|  0.000|  17,557|
| |Graham County|     0|  0.000|  0.000|    44|  5212.653| 220.015|   8,441|
| |Currituck County|     0|  0.000|  0.000|    78|  2809.495| 36.019|  27,763|
| |Yancey County|     0|  0.000|  0.000|    78|  4316.786|  0.000|  18,069|
| |Watauga County|     0|  0.000|  0.000|   309|  5500.472| 66.118|  56,177|
| |Hyde County|     0|  0.000|  0.000|    48|  9722.504| 289.360|   4,937|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,184| 424.184| N/A|103,909| 20181.544| N/A|5,148,714|
| |Greenville County|   222| 424.035|  5.730|11,109| 21218.928| 129.339| 523,542|
| |Charleston County|   209| 508.014|  6.598|12,631| 30702.032| 212.512| 411,406|
| |Horry County|   167| 471.643|  8.876| 8,743| 24692.090| 150.087| 354,081|
| |Richland County|   159| 382.433|  3.780| 9,142| 21988.700| 232.965| 415,759|
| |Florence County|   123| 889.416| 15.495| 3,614| 26132.921| 367.749| 138,293|
| |Lexington County|   116| 388.285|  3.825| 5,078| 16997.490| 114.286| 298,750|
| |Spartanburg County|   111| 347.108|  5.807| 4,299| 13443.407| 150.994| 319,785|
| |Berkeley County|    70| 307.143|  3.761| 4,324| 18972.651| 172.376| 227,907|
| |Orangeburg County|    70| 812.301| 14.920| 2,494| 28941.108| 314.974|  86,175|
| |Anderson County|    70| 345.580| 10.579| 2,489| 12287.839| 177.727| 202,558|
| |Beaufort County|    60| 312.302|  4.461| 4,256| 22152.591| 249.098| 192,122|
| |Clarendon County|    55| 1629.871| 16.934|   874| 25900.133| 241.306|  33,745|
| |Dorchester County|    53| 325.535|  5.265| 3,176| 19507.521| 182.510| 162,809|
| |Sumter County|    53| 496.622|  8.032| 2,604| 24400.071| 247.642| 106,721|
| |Laurens County|    47| 696.369| 10.583| 1,354| 20061.340| 167.213|  67,493|
| |Aiken County|    42| 245.798|  7.524| 2,017| 11804.157| 191.455| 170,872|
| |Darlington County|    36| 540.394|  2.144| 1,362| 20444.925| 370.985|  66,618|
| |Colleton County|    34| 902.407|  3.792|   837| 22215.145| 174.415|  37,677|
| |Cherokee County|    31| 541.012|  7.479|   692| 12076.789| 231.862|  57,300|
| |Williamsburg County|    31| 1020.811|  9.408| 1,042| 34312.434| 381.040|  30,368|
| |Lee County|    30| 1782.743| 25.468|   564| 33515.569| 186.764|  16,828|
| |York County|    29| 103.211|  0.000| 3,705| 13186.039| 154.053| 280,979|
| |Kershaw County|    27| 405.704|  8.586| 1,425| 21412.150| 145.968|  66,551|
| |Lancaster County|    27| 275.476|  5.830| 1,297| 13233.074| 231.750|  98,012|
| |Pickens County|    27| 212.793|  1.126| 1,897| 14950.664| 117.092| 126,884|
| |Bamberg County|    26| 1848.429| 60.937|   482| 34267.027| 274.217|  14,066|
| |Dillon County|    25| 820.237|  4.687|   661| 21687.063| 253.102|  30,479|
| |Georgetown County|    25| 398.851| 13.675| 1,498| 23899.170| 348.710|  62,680|
| |Fairfield County|    24| 1073.970|  6.393|   578| 25864.769| 153.424|  22,347|
| |Chesterfield County|    22| 481.928|  3.129|   803| 17590.361| 231.576|  45,650|
| |Greenwood County|    20| 282.442|  6.052| 1,489| 21027.806| 308.669|  70,811|
| |Jasper County|    18| 598.544| 19.001|   611| 20317.228| 242.268|  30,073|
| |Marion County|    14| 456.666|  4.660|   573| 18690.674| 177.074|  30,657|
| |Chester County|    14| 434.189|  4.431|   716| 22205.682| 456.342|  32,244|
| |Calhoun County|    13| 893.287| 29.449|   384| 26386.312| 127.612|  14,553|
| |Hampton County|    13| 676.308| 44.592|   457| 23774.841| 386.462|  19,222|
| |Oconee County|    12| 150.856|  7.184|   854| 10735.926| 120.326|  79,546|
| |Newberry County|    11| 286.160|  7.433|   881| 22918.835| 196.967|  38,440|
| |Saluda County|     9| 439.603|  6.978|   469| 22908.221| 181.424|  20,473|
| |Barnwell County|     8| 383.399| 20.539|   439| 21039.011| 335.474|  20,866|
| |Abbeville County|     8| 326.171|  0.000|   355| 14473.845| 244.628|  24,527|
| |Edgefield County|     7| 256.787|  5.241|   349| 12802.641| 241.065|  27,260|
| |Allendale County|     6| 690.608| 49.329|   242| 27854.512| 624.836|   8,688|
| |Marlboro County|     4| 153.151|  0.000|   529| 20254.231| 333.651|  26,118|
| |Union County|     4| 146.434|  5.230|   383| 14021.087| 193.502|  27,316|
| |McCormick County|     2| 211.349|  0.000|   131| 13843.390| 347.217|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 2,011| 675.705| N/A|69,986| 23515.624| N/A|2,976,149|
| |Hinds County|   124| 534.852|  4.930| 5,803| 25030.193| 194.716| 231,840|
| |Lauderdale County|    94| 1268.128|  7.709| 1,458| 19669.477| 131.053|  74,125|
| |Neshoba County|    94| 3228.244| 14.718| 1,309| 44955.011| 152.091|  29,118|
| |Madison County|    72| 677.507| 12.098| 2,503| 23552.770| 155.934| 106,272|
| |Leflore County|    68| 2412.802| 30.413|   963| 34169.535| 354.824|  28,183|
| |Jones County|    62| 910.453|  8.391| 1,945| 28561.779| 216.075|  68,098|
| |Forrest County|    57| 761.045|  3.815| 1,865| 24900.864| 274.663|  74,897|
| |Monroe County|    55| 1560.195| 16.210|   839| 23800.068| 372.826|  35,252|
| |Holmes County|    49| 2880.658|  8.398|   928| 54556.143| 545.897|  17,010|
| |Jackson County|    47| 327.259|  4.974| 2,411| 16787.706| 208.889| 143,617|
| |Washington County|    45| 1024.847| 26.028| 1,739| 39604.637| 510.797|  43,909|
| |Lincoln County|    43| 1259.040|  8.366|   849| 24858.724| 246.789|  34,153|
| |Lee County|    42| 491.596| 16.721| 1,610| 18844.515| 464.843|  85,436|
| |Pearl River County|    40| 720.266|  7.717|   571| 10281.804| 131.191|  55,535|
| |Lowndes County|    40| 682.652| 12.190| 1,114| 19011.861| 182.853|  58,595|
| |Oktibbeha County|    39| 786.496|  5.762| 1,145| 23090.729| 158.452|  49,587|
| |Rankin County|    38| 244.733|  5.520| 2,337| 15051.104| 107.646| 155,271|
| |Pike County|    37| 941.763| 10.908|   960| 24434.942| 301.801|  39,288|
| |Bolivar County|    37| 1208.045| 18.657| 1,167| 38102.390| 18.657|  30,628|
| |Harrison County|    36| 173.010|  0.687| 2,663| 12797.962| 195.667| 208,080|
| |Warren County|    36| 793.284| 15.740| 1,151| 25363.037| 453.305|  45,381|
| |DeSoto County|    32| 173.024|  3.090| 3,796| 20525.021| 210.874| 184,945|
| |Simpson County|    31| 1162.878|  5.359|   822| 30835.021| 230.432|  26,658|
| |Tate County|    30| 1059.285| 15.133|   753| 26588.044| 307.697|  28,321|
| |Copiah County|    29| 1033.316|  5.090|   973| 34669.517| 162.887|  28,065|
| |Clarke County|    28| 1801.686| 27.577|   355| 22842.803| 284.961|  15,541|
| |Sunflower County|    28| 1115.094| 28.446| 1,086| 43249.701| 677.021|  25,110|
| |Leake County|    27| 1184.938| 12.539|   804| 35284.824| 156.738|  22,786|
| |Grenada County|    26| 1252.529| 34.410|   861| 41477.984| 213.343|  20,758|
| |Adams County|    26| 847.099|  4.654|   647| 21079.725| 209.447|  30,693|
| |Attala County|    25| 1375.592|  7.861|   539| 29657.753| 204.374|  18,174|
| |Walthall County|    22| 1539.969| 29.999|   519| 36329.273| 299.994|  14,286|
| |Wayne County|    21| 1040.480|  0.000|   790| 39141.852| 290.202|  20,183|
| |Marion County|    21| 854.597| 11.627|   692| 28160.990| 313.933|  24,573|
| |Scott County|    20| 711.136|  0.000| 1,017| 36161.286| 152.386|  28,124|
| |Lafayette County|    20| 370.240| 15.867| 1,025| 18974.805| 232.722|  54,019|
| |Chickasaw County|    19| 1110.916|  0.000|   491| 28708.414| 417.638|  17,103|
| |Panola County|    18| 526.439| 25.069| 1,096| 32054.282| 484.658|  34,192|
| |Union County|    17| 589.971|  9.915|   732| 25403.436| 842.815|  28,815|
| |Lamar County|    16| 252.593|  4.511| 1,246| 19670.682| 139.828|  63,343|
| |Winston County|    16| 891.117|  7.956|   637| 35477.583| 262.561|  17,955|
| |Hancock County|    15| 314.914|  2.999|   414|  8691.636| 152.958|  47,632|
| |Covington County|    15| 804.894| 15.331|   641| 34395.793| 260.632|  18,636|
| |Kemper County|    14| 1437.077|  0.000|   241| 24738.247| 190.633|   9,742|
| |Clay County|    14| 724.788|  0.000|   406| 21018.844| 177.499|  19,316|
| |Tippah County|    14| 635.930|  6.489|   411| 18669.089| 558.061|  22,015|
| |Claiborne County|    14| 1557.632| 15.894|   410| 45616.377| 174.836|   8,988|
| |Wilkinson County|    14| 1622.248| 16.554|   227| 26303.592| 546.267|   8,630|
| |Yazoo County|    13| 437.858|  4.812|   874| 29437.521| 322.379|  29,690|
| |Webster County|    13| 1341.728| 14.744|   250| 25802.456| 501.305|   9,689|
| |Coahoma County|    13| 587.597| 12.914|   798| 36069.427| 652.168|  22,124|
| |Smith County|    13| 816.788|  0.000|   415| 26074.391| 188.490|  15,916|
| |Greene County|    13| 956.867| 21.030|   262| 19284.558| 325.966|  13,586|
| |Noxubee County|    12| 1151.963| 13.714|   466| 44734.568| 301.705|  10,417|
| |Humphreys County|    12| 1488.095| 17.715|   303| 37574.405| 372.024|   8,064|
| |Newton County|    11| 523.361|  0.000|   567| 26976.877| 217.501|  21,018|
| |Tallahatchie County|    11| 796.582| 10.345|   550| 39829.097| 1479.366|  13,809|
| |Carroll County|    11| 1105.861|  0.000|   263| 26440.133| 129.256|   9,947|
| |Marshall County|    10| 283.334|  4.048|   740| 20966.737| 412.859|  35,294|
| |Itawamba County|    10| 427.533|  0.000|   404| 17272.339| 409.210|  23,390|
| |Yalobusha County|    10| 825.900|  0.000|   318| 26263.627| 129.784|  12,108|
| |Prentiss County|    10| 397.994|  5.686|   462| 18387.328| 432.108|  25,126|
| |Tishomingo County|     9| 464.324| 29.481|   453| 23370.995| 759.134|  19,383|
| |George County|     9| 367.347| 29.155|   605| 24693.878| 332.362|  24,500|
| |Calhoun County|     9| 626.697|  0.000|   428| 29802.939| 278.532|  14,361|
| |Jasper County|     9| 549.350|  0.000|   412| 25148.019| 270.315|  16,383|
| |Pontotoc County|     9| 279.729|  4.440|   866| 26916.143| 333.011|  32,174|
| |Lawrence County|     8| 635.627| 11.350|   332| 26378.516| 295.112|  12,586|
| |Perry County|     8| 668.170| 11.932|   249| 20796.793| 346.017|  11,973|
| |Tunica County|     7| 726.744| 14.832|   367| 38102.159| 741.576|   9,632|
| |Sharkey County|     7| 1619.995| 132.245|   209| 48368.433| 628.161|   4,321|
| |Montgomery County|     7| 716.113| 58.458|   346| 35396.419| 569.967|   9,775|
| |Jefferson County|     7| 1001.431| 20.437|   197| 28183.119| 61.312|   6,990|
| |Stone County|     6| 327.225| 23.373|   225| 12270.942| 483.047|  18,336|
| |Jefferson Davis County|     6| 539.180|  0.000|   243| 21836.808| 218.240|  11,128|
| |Amite County|     6| 487.924|  0.000|   242| 19679.597| 255.579|  12,297|
| |Alcorn County|     5| 135.307|  0.000|   445| 12042.324| 243.553|  36,953|
| |Choctaw County|     4| 487.211|  0.000|   138| 16808.770| 139.203|   8,210|
| |Franklin County|     2| 259.302|  0.000|   137| 17762.220| 388.954|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    27| 20346.647| 215.308|   1,327|
| |Quitman County|     1| 147.232|  0.000|   275| 40488.810| 736.160|   6,792|
| |Benton County|     1| 121.080| 17.297|   157| 19009.565| 415.132|   8,259|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,882| 326.808| N/A|52,200|  9064.489| N/A|5,758,736|
| |Denver County|   417| 573.424| N/A|10,426| 14336.967| N/A| 727,211|
| |Arapahoe County|   363| 552.856|  0.000| 7,461| 11363.256| 58.092| 656,590|
| |Jefferson County|   233| 399.739|  1.471| 4,334|  7435.480| 60.782| 582,881|
| |Adams County|   178| 344.014|  0.828| 6,677| 12904.385| 102.155| 517,421|
| |Weld County|   145| 446.852|  1.321| 3,774| 11630.487| 61.195| 324,492|
| |El Paso County|   142| 197.112|  0.992| 5,334|  7404.189| 99.547| 720,403|
| |Boulder County|    76| 232.989|  0.438| 2,114|  6480.766| 51.240| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,788|  5091.783| 34.987| 351,154|
| |Morgan County|    47| 1616.898|  4.915|   693| 23840.650| 58.975|  29,068|
| |Larimer County|    37| 103.671|  0.801| 1,630|  4567.118| 62.042| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   723|  4292.737| 53.437| 168,424|
| |Broomfield County|    32| 454.126| N/A|   482|  6840.275| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   305| 14983.297| 70.179|  20,356|
| |Montrose County|    13| 304.037|  0.000|   316|  7390.430| 80.185|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,139| 20661.382| 85.517|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   232| 14291.875| 70.403|  16,233|
| |Routt County|     8| 312.037| 11.144|   124|  4836.571| 72.437|  25,638|
| |Gunnison County|     7| 400.870|  8.181|   278| 15920.284| 89.991|  17,462|
| |Otero County|     6| 328.263|  0.000|    78|  4267.425| 62.526|  18,278|
| |Logan County|     5| 223.125|  0.000|   655| 29229.328| 38.250|  22,409|
| |Montezuma County|     5| 190.964|  5.456|   113|  4315.777| 21.824|  26,183|
| |Mesa County|     4| 25.939|  0.000|   351|  2276.117| 57.436| 154,210|
| |Garfield County|     4| 66.599|  0.000|   780| 12986.797| 64.220|  60,061|
| |Summit County|     4| 128.986|  0.000|   342| 11028.345| 69.100|  31,011|
| |Teller County|     3| 118.166|  0.000|   143|  5632.582| 118.166|  25,388|
| |La Plata County|     3| 53.361|  2.541|   226|  4019.850| 55.902|  56,221|
| |Kit Carson County|     3| 422.714|  0.000|    69|  9722.418| 523.360|   7,097|
| |Pitkin County|     2| 112.568|  0.000|   190| 10693.983| 72.365|  17,767|
| |Rio Grande County|     2| 177.510|  0.000|    91|  8076.684| 25.359|  11,267|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Elbert County|     2| 74.825|  0.000|   108|  4040.555| 32.068|  26,729|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Delta County|     1| 32.090|  0.000|   130|  4171.748| 59.596|  31,162|
| |Crowley County|     1| 164.989|  0.000|    73| 12044.217| 23.570|   6,061|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925|  0.000|   6,897|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Grand County|     1| 63.557|  0.000|    54|  3432.058| 81.716|  15,734|
| |Clear Creek County|     1| 103.093|  0.000|    31|  3195.876| 29.455|   9,700|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 64.529|  13,283|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Gilpin County|     0|  0.000|  0.000|    17|  2723.050| 22.883|   6,243|
| |Fremont County|     0|  0.000|  0.000|   132|  2759.255| 47.779|  47,839|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481|  0.000|   5,068|
| |Costilla County|     0|  0.000|  0.000|    23|  5917.160| 36.753|   3,887|
| |Conejos County|     0|  0.000|  0.000|    26|  3168.800| 52.233|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 25.615|   5,577|
| |Archuleta County|     0|  0.000|  0.000|    39|  2779.956| 40.732|  14,029|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517|  0.000|   1,392|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Washington County|     0|  0.000|  0.000|    50| 10187.449| 87.321|   4,908|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053|  0.000|  10,019|
| |San Miguel County|     0|  0.000|  0.000|    92| 11248.319| 209.596|   8,179|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684| 87.890|   8,127|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 248.486|   6,324|
| |Prowers County|     0|  0.000|  0.000|    61|  5011.502| 129.102|  12,172|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263|  0.000|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866| 29.544|  14,506|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,821| 371.391| N/A|101,496| 20700.014| N/A|4,903,185|
| |Jefferson County|   262| 397.830|  6.508|13,578| 20617.304| 236.876| 658,573|
| |Mobile County|   221| 534.837|  5.877|10,747| 26008.567| 458.777| 413,210|
| |Montgomery County|   153| 675.538|  3.154| 6,999| 30902.572| 346.915| 226,486|
| |Tuscaloosa County|    80| 382.126|  7.506| 4,350| 20778.104| 199.934| 209,355|
| |Tallapoosa County|    79| 1957.044|  0.000|   878| 21750.440| 130.941|  40,367|
| |Walker County|    65| 1023.284|  2.249| 1,562| 24590.293| 143.934|  63,521|
| |Lee County|    47| 285.641|  2.605| 2,736| 16627.973| 128.495| 164,542|
| |Elmore County|    39| 480.242|  1.759| 1,783| 21955.695| 195.263|  81,209|
| |Marshall County|    38| 392.667|  5.905| 3,207| 33139.066| 217.000|  96,774|
| |Chambers County|    38| 1142.720|  0.000|   848| 25500.692| 55.847|  33,254|
| |Shelby County|    37| 169.957|  3.281| 3,381| 15530.404| 142.396| 217,702|
| |Butler County|    36| 1851.090|  7.346|   775| 39849.856| 139.566|  19,448|
| |Madison County|    35| 93.857|  1.915| 5,550| 14882.988| 149.021| 372,909|
| |Etowah County|    34| 332.460|  8.381| 2,209| 21600.110| 234.678| 102,268|
| |Dale County|    29| 589.767| 17.432|   856| 17408.281| 156.884|  49,172|
| |Baldwin County|    29| 129.909|  3.840| 3,744| 16771.639| 232.939| 223,234|
| |Marion County|    26| 875.156|  9.617|   592| 19926.622| 144.256|  29,709|
| |Hale County|    26| 1774.623|  0.000|   487| 33240.052| 224.266|  14,651|
| |Dallas County|    25| 672.115|  7.681| 1,348| 36240.456| 165.148|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   575| 59119.885| 117.505|   9,726|
| |Franklin County|    22| 701.486|  9.110| 1,310| 41770.295| 327.967|  31,362|
| |Autauga County|    22| 393.778|  2.557| 1,196| 21407.220| 373.322|  55,869|
| |Covington County|    21| 566.817|  3.856|   755| 20378.418| 150.380|  37,049|
| |Morgan County|    20| 167.114|  3.581| 2,443| 20412.938| 176.663| 119,679|
| |St. Clair County|    20| 223.434|  7.980| 1,381| 15428.099| 146.828|  89,512|
| |Lauderdale County|    20| 215.682|  7.703| 1,213| 13081.129| 138.653|  92,729|
| |Sumter County|    19| 1528.929| 11.496|   370| 29773.879| 114.957|  12,427|
| |Calhoun County|    19| 167.246|  7.545| 1,853| 16310.902| 227.606| 113,605|
| |Colbert County|    18| 325.845| 12.930| 1,232| 22302.275| 235.332|  55,241|
| |Escambia County|    17| 464.062|  3.900| 1,094| 29863.784| 194.984|  36,633|
| |Marengo County|    17| 901.235| 22.720|   572| 30323.915| 272.643|  18,863|
| |Macon County|    14| 774.851|  7.907|   344| 19039.185| 189.759|  18,068|
| |Talladega County|    14| 175.048|  1.786| 1,087| 13591.238| 214.345|  79,978|
| |DeKalb County|    14| 195.769|  1.998| 1,866| 26093.158| 241.714|  71,513|
| |Houston County|    13| 122.778|  1.349| 1,459| 13779.490| 149.762| 105,882|
| |Limestone County|    13| 131.426|  0.000| 1,393| 14082.798| 190.640|  98,915|
| |Washington County|    13| 796.276|  8.750|   453| 27747.152| 1163.788|  16,326|
| |Choctaw County|    12| 953.213|  0.000|   290| 23035.984| 147.521|  12,589|
| |Cullman County|    12| 143.253|  0.000| 1,246| 14874.415| 97.207|  83,768|
| |Bullock County|    11| 1089.001|  0.000|   493| 48807.049| 608.143|  10,101|
| |Greene County|    11| 1356.183|  0.000|   255| 31438.787| 105.677|   8,111|
| |Winston County|    11| 465.530|  0.000|   456| 19298.320| 96.733|  23,629|
| |Randolph County|    11| 484.112|  6.287|   404| 17780.125| 62.872|  22,722|
| |Pickens County|    10| 501.756|  7.168|   413| 20722.529| 258.046|  19,930|
| |Clarke County|    10| 423.334|  6.048|   827| 35009.737| 2013.861|  23,622|
| |Wilcox County|    10| 964.041|  0.000|   445| 42899.836| 426.933|  10,373|
| |Conecuh County|    10| 828.706|  0.000|   397| 32899.644| 224.935|  12,067|
| |Chilton County|     9| 202.575|  9.646|   830| 18681.912| 273.315|  44,428|
| |Cherokee County|     8| 305.390|  5.453|   288| 10994.045| 163.602|  26,196|
| |Crenshaw County|     8| 580.889| 51.865|   333| 24179.495| 217.833|  13,772|
| |Pike County|     7| 211.391|  0.000|   716| 21622.275| 125.109|  33,114|
| |Barbour County|     6| 243.053|  5.787|   586| 23738.151| 121.526|  24,686|
| |Coffee County|     6| 114.631|  2.729|   781| 14921.096| 122.819|  52,342|
| |Monroe County|     6| 289.394| 13.781|   425| 20498.722| 117.136|  20,733|
| |Clay County|     5| 377.786|  0.000|   278| 21004.911| 442.550|  13,235|
| |Fayette County|     5| 306.711|  0.000|   227| 13924.672| 385.579|  16,302|
| |Bibb County|     5| 223.274|  6.379|   457| 20407.252| 280.687|  22,394|
| |Blount County|     5| 86.466|  4.941|   835| 14439.871| 187.755|  57,826|
| |Jackson County|     4| 77.480|  0.000| 1,079| 20900.322| 428.909|  51,626|
| |Perry County|     4| 448.280|  0.000|   448| 50207.329| 192.120|   8,923|
| |Lawrence County|     3| 91.119|  8.678|   360| 10934.273| 121.492|  32,924|
| |Henry County|     3| 174.368|  0.000|   268| 15576.867| 157.761|  17,205|
| |Coosa County|     3| 281.347| 13.397|   106|  9940.917| 66.987|  10,663|
| |Geneva County|     2| 76.130| 10.876|   269| 10239.428| 114.194|  26,271|
| |Lamar County|     2| 144.875|  0.000|   237| 17167.693| 258.705|  13,805|
| |Russell County|     2| 34.506|  0.000| 1,391| 23998.896| 280.977|  57,961|
| |Cleburne County|     1| 67.069|  0.000|   130|  8718.981| 47.906|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,734| 227.712| N/A|65,129|  8552.845| N/A|7,614,893|
| |King County|   686| 304.512|  1.395|17,118|  7598.605| 65.950|2,252,782|
| |Yakima County|   217| 864.979|  3.417|10,467| 41722.306| 170.832| 250,873|
| |Snohomish County|   199| 242.068|  1.390| 5,621|  6837.509| 51.264| 822,083|
| |Pierce County|   144| 159.120|  1.105| 5,940|  6563.681| 73.088| 904,980|
| |Benton County|   120| 587.113|  4.893| 3,802| 18601.693| 118.820| 204,390|
| |Spokane County|    95| 181.715|  4.372| 4,667|  8926.966| 129.796| 522,798|
| |Franklin County|    51| 535.591|  4.501| 3,605| 37858.898| 289.549|  95,222|
| |Clark County|    46| 94.216|  1.170| 1,874|  3838.268| 47.400| 488,241|
| |Whatcom County|    39| 170.122|  0.623| 1,007|  4392.642| 26.173| 229,247|
| |Skagit County|    22| 170.272|  1.106|   909|  7035.331| 56.389| 129,205|
| |Kittitas County|    20| 417.232|  5.960|   412|  8594.972| 169.873|  47,935|
| |Grant County|    13| 133.015|  0.000| 1,627| 16647.396| 342.040|  97,733|
| |Island County|    11| 129.197|  0.000|   249|  2924.560| 13.423|  85,141|
| |Thurston County|    11| 37.861|  0.000|   761|  2619.297| 39.828| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,449| 18769.430| 358.993|  77,200|
| |Douglas County|     7| 161.183|  0.000|   985| 22680.697| 312.497|  43,429|
| |Kitsap County|     7| 25.785|  1.052|   778|  2865.847| 37.362| 271,473|
| |Okanogan County|     5| 118.363| 10.145|   885| 20950.217| 219.817|  42,243|
| |Cowlitz County|     5| 45.211|  0.000|   502|  4539.166| 51.670| 110,593|
| |Adams County|     5| 250.213|  7.149|   460| 23019.567| 307.404|  19,983|
| |Lewis County|     4| 49.562|  1.770|   233|  2886.986| 63.723|  80,707|
| |Grays Harbor County|     3| 39.967|  1.903|   127|  1691.957| 34.258|  75,061|
| |Klickitat County|     3| 133.779|  0.000|   119|  5306.577| 70.075|  22,425|
| |Walla Walla County|     3| 49.375|  0.000|   572|  9414.088| 199.850|  60,760|
| |Asotin County|     2| 88.566|  0.000|    31|  1372.775| 37.957|  22,582|
| |Pacific County|     2| 89.004|  0.000|    54|  2403.097| 44.502|  22,471|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 23.646|  12,083|
| |Stevens County|     1| 21.871|  0.000|   113|  2471.404| 43.742|  45,723|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Mason County|     1| 14.977|  0.000|   240|  3594.536| 113.399|  66,768|
| |San Juan County|     0|  0.000|  0.000|    30|  1706.291| 16.250|  17,582|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Pend Oreille County|     0|  0.000|  0.000|    46|  3351.792| 83.274|  13,724|
| |Jefferson County|     0|  0.000|  0.000|    56|  1737.997|  8.867|  32,221|
| |Lincoln County|     0|  0.000|  0.000|    27|  2468.233| 91.416|  10,939|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489| 18.730|   7,627|
| |Whitman County|     0|  0.000|  0.000|   118|  2355.101| 82.685|  50,104|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Clallam County|     0|  0.000|  0.000|   144|  1862.125| 81.283|  77,331|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,685| 298.778| N/A|62,858| 11145.763| N/A|5,639,632|
| |Hennepin County|   842| 665.169|  1.580|19,873| 15699.419| 139.038|1,265,843|
| |Ramsey County|   270| 490.623|  2.336| 7,827| 14222.608| 154.196| 550,321|
| |Anoka County|   115| 322.200|  0.400| 3,841| 10761.485| 130.481| 356,921|
| |Dakota County|   106| 247.074|  0.666| 4,610| 10745.395| 140.519| 429,021|
| |Washington County|    48| 182.899|  2.177| 2,227|  8485.749| 118.667| 262,440|
| |Clay County|    40| 622.840|  0.000|   794| 12363.365| 57.835|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,791| 11314.461| 92.956| 158,293|
| |Scott County|    22| 147.638|  3.835| 1,634| 10965.486| 148.597| 149,013|
| |St. Louis County|    20| 100.467|  0.718|   621|  3119.506| 96.879| 199,070|
| |Stearns County|    20| 124.166|  0.000| 2,928| 18177.867| 56.761| 161,075|
| |Winona County|    16| 316.932|  0.000|   266|  5268.996| 33.957|  50,484|
| |Crow Wing County|    14| 215.203|  0.000|   252|  3873.645| 59.290|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   356| 10386.882| 112.538|  34,274|
| |Itasca County|    12| 265.899|  0.000|   146|  3235.099| 34.820|  45,130|
| |Sherburne County|    10| 102.840|  4.407|   753|  7743.886| 73.457|  97,238|
| |Pipestone County|     9| 986.193|  0.000|   158| 17313.171| 172.192|   9,126|
| |Goodhue County|     9| 194.217|  3.083|   205|  4423.824| 55.490|  46,340|
| |Rice County|     8| 119.453|  0.000| 1,046| 15618.467| 70.392|  66,972|
| |Nobles County|     7| 323.640|  6.605| 1,777| 82158.214| 158.517|  21,629|
| |Blue Earth County|     5| 73.907|  0.000|   946| 13983.120| 152.036|  67,653|
| |Renville County|     5| 343.690|  0.000|    67|  4605.444| 49.099|  14,548|
| |Martin County|     5| 254.026|  0.000|   210| 10669.105| 43.547|  19,683|
| |Wright County|     5| 36.133|  0.000|   918|  6634.050| 73.299| 138,377|
| |Otter Tail County|     4| 68.090|  2.432|   204|  3472.577| 46.204|  58,746|
| |Polk County|     4| 127.535|  4.555|   156|  4973.855| 50.103|  31,364|
| |Wilkin County|     3| 483.325|  0.000|    35|  5638.795| 69.046|   6,207|
| |Benton County|     3| 73.369|  0.000|   325|  7948.348| 34.938|  40,889|
| |Mille Lacs County|     3| 114.168|  0.000|    73|  2778.095| 21.746|  26,277|
| |Koochiching County|     3| 245.319|  0.000|    83|  6787.145| 105.137|  12,229|
| |Grant County|     3| 502.344|  0.000|    56|  9377.093| 95.685|   5,972|
| |Lyon County|     3| 117.767|  0.000|   426| 16722.933| 28.040|  25,474|
| |Carver County|     3| 28.547|  1.359|   899|  8554.654| 112.830| 105,089|
| |Todd County|     2| 81.090|  0.000|   430| 17434.317| 46.337|  24,664|
| |Kanabec County|     2| 122.421|  8.744|    37|  2264.798| 43.722|  16,337|
| |Mower County|     2| 49.923|  0.000| 1,111| 27732.015| 60.620|  40,062|
| |Meeker County|     2| 86.125|  0.000|    87|  3746.447| 12.304|  23,222|
| |Brown County|     2| 79.974|  0.000|    92|  3678.823| 34.275|  25,008|
| |Cass County|     2| 67.161|  0.000|    80|  2686.457| 43.175|  29,779|
| |Douglas County|     2| 52.437|  7.491|   144|  3775.465| 29.964|  38,141|
| |Sibley County|     2| 134.544|  0.000|    86|  5785.402| 38.441|  14,865|
| |Steele County|     2| 54.572|  3.898|   356|  9713.771| 70.164|  36,649|
| |Freeborn County|     1| 33.024|  0.000|   361| 11921.667| 14.153|  30,281|
| |Kandiyohi County|     1| 23.149|  0.000|   714| 16528.160| 89.288|  43,199|
| |Aitkin County|     1| 62.949|  0.000|    41|  2580.889| 107.912|  15,886|
| |Becker County|     1| 29.050|  0.000|   162|  4706.156| 49.801|  34,423|
| |Chisago County|     1| 17.674|  0.000|   209|  3693.950| 50.498|  56,579|
| |Chippewa County|     1| 84.746|  0.000|   117|  9915.254| 193.705|  11,800|
| |Watonwan County|     1| 91.768| 13.110|   367| 33678.994| 865.245|  10,897|
| |Waseca County|     1| 53.729|  7.676|   156|  8381.689| 138.160|  18,612|
| |Swift County|     1| 107.921|  0.000|    56|  6043.600| 61.669|   9,266|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 20.236|  14,119|
| |Murray County|     1| 122.041|  0.000|   125| 15255.065| 52.303|   8,194|
| |Morrison County|     1| 29.953|  0.000|    94|  2815.551| 38.511|  33,386|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 25.847|   5,527|
| |Le Sueur County|     1| 34.618|  0.000|   230|  7962.059| 98.908|  28,887|
| |Roseau County|     0|  0.000|  0.000|    53|  3494.890| 65.941|  15,165|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 35.230|   4,055|
| |Redwood County|     0|  0.000|  0.000|    37|  2439.024| 47.085|  15,170|
| |Rock County|     0|  0.000|  0.000|    86|  9232.421| 138.026|   9,315|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 14.570|   9,805|
| |Traverse County|     0|  0.000|  0.000|    13|  3988.954| 131.504|   3,259|
| |Yellow Medicine County|     0|  0.000|  0.000|    53|  5458.853| 29.428|   9,709|
| |Wadena County|     0|  0.000|  0.000|    28|  2046.484| 41.765|  13,682|
| |Wabasha County|     0|  0.000|  0.000|    93|  4300.180| 39.633|  21,627|
| |Carlton County|     0|  0.000|  0.000|   147|  4098.018| 59.738|  35,871|
| |Big Stone County|     0|  0.000|  0.000|    25|  5009.016| 85.869|   4,991|
| |Lac qui Parle County|     0|  0.000|  0.000|     8|  1207.912| 43.140|   6,623|
| |Dodge County|     0|  0.000|  0.000|   131|  6257.762| 40.945|  20,934|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    79|  8023.563| 101.564|   9,846|
| |Isanti County|     0|  0.000|  0.000|   137|  3374.717| 73.899|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    36|  1675.120| 39.884|  21,491|
| |Houston County|     0|  0.000|  0.000|    45|  2419.355| 30.722|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    72|  3417.667| 74.592|  21,067|
| |Faribault County|     0|  0.000|  0.000|    92|  6738.446| 94.171|  13,653|
| |Beltrami County|     0|  0.000|  0.000|   264|  5594.643| 148.343|  47,188|
| |Lake of the Woods County|     0|  0.000|  0.000|     4|  1069.519| 114.591|   3,740|
| |Lincoln County|     0|  0.000|  0.000|    61| 10817.521| 177.336|   5,639|
| |McLeod County|     0|  0.000|  0.000|   224|  6240.771| 302.486|  35,893|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255|  0.000|   9,336|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Cook County|     0|  0.000|  0.000|     5|   915.248| 78.450|   5,463|
| |Cottonwood County|     0|  0.000|  0.000|   178| 15898.535| 38.279|  11,196|
| |Lake County|     0|  0.000|  0.000|    22|  2067.475| 26.850|  10,641|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 25.399|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202|  4.830|  29,579|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510| 67.227|   6,375|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,291| 210.349| N/A|57,144|  9310.741| N/A|6,137,428|
| |St. Louis County|   851| 855.960|  3.880|21,302| 21426.165| 278.471| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,408| 10964.574| 182.293| 402,022|
| |Jackson County|    66| 93.882|  0.813| 4,363|  6206.162| 112.374| 703,011|
| |Jasper County|    31| 255.506|  3.532| 1,874| 15445.734| 197.811| 121,328|
| |Jefferson County|    26| 115.514|  1.269| 1,769|  7859.393| 164.385| 225,081|
| |Clay County|    22| 88.018|  1.143| 1,098|  4392.914| 65.156| 249,948|
| |Franklin County|    18| 173.132|  0.000|   680|  6540.537| 129.162| 103,967|
| |Scott County|    13| 339.603|  0.000|   429| 11206.897| 227.646|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,737|  5926.588| 164.262| 293,086|
| |Platte County|    10| 95.769|  0.000|   393|  3763.719| 75.247| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,112| 12728.355| 60.502|  87,364|
| |Stoddard County|     9| 310.078|  0.000|   237|  8165.375| 83.672|  29,025|
| |Gentry County|     9| 1369.655|  0.000|    86| 13087.810| 65.222|   6,571|
| |Cass County|     9| 85.082|  0.000|   811|  7666.856| 160.711| 105,780|
| |Pemiscot County|     9| 569.440|  0.000|   244| 15438.152| 153.658|  15,805|
| |McDonald County|     8| 350.309|  6.256|   955| 41818.102| 56.300|  22,837|
| |Camden County|     7| 151.172|  6.170|   382|  8249.649| 145.001|  46,305|
| |Saline County|     7| 307.544|  0.000|   472| 20737.226| 320.096|  22,761|
| |Newton County|     6| 103.029|  0.000|   920| 15797.788| 186.434|  58,236|
| |Cape Girardeau County|     5| 63.395|  0.000|   705|  8938.647| 141.280|  78,871|
| |Barry County|     4| 111.766|  7.983|   273|  7628.042| 111.766|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   339| 11637.088| 250.102|  29,131|
| |Perry County|     4| 209.030|  0.000|   249| 13012.124| 231.426|  19,136|
| |Pettis County|     4| 94.476|  3.374|   589| 13911.524| 391.399|  42,339|
| |Boone County|     3| 16.624|  0.000| 1,500|  8311.953| 160.698| 180,463|
| |Johnson County|     3| 55.492|  2.642|   501|  9267.138| 66.062|  54,062|
| |Henry County|     3| 137.463|  0.000|    92|  4215.543| 104.734|  21,824|
| |Cole County|     3| 39.090|  0.000|   477|  6215.389| 214.067|  76,745|
| |Taney County|     3| 53.640|  0.000|   678| 12122.729| 401.026|  55,928|
| |New Madrid County|     3| 175.685| 16.732|   279| 16338.721| 527.056|  17,076|
| |Lawrence County|     2| 52.144|  0.000|   246|  6413.766| 152.709|  38,355|
| |Lafayette County|     2| 61.147|  0.000|   189|  5778.403| 78.618|  32,708|
| |St. Francois County|     2| 29.755|  0.000|   462|  6873.466| 250.794|  67,215|
| |Butler County|     2| 47.083|  0.000|   297|  6991.855| 110.982|  42,478|
| |Howell County|     2| 49.854|  0.000|   164|  4088.042| 67.659|  40,117|
| |Douglas County|     2| 151.688|  0.000|    89|  6750.095| 54.174|  13,185|
| |Moniteau County|     2| 123.977|  0.000|   156|  9670.221| 159.399|  16,132|
| |Pike County|     1| 54.639|  0.000|   140|  7649.437| 421.500|  18,302|
| |Osage County|     1| 73.448|  0.000|    54|  3966.214| 104.926|  13,615|
| |Miller County|     1| 39.034|  0.000|   138|  5386.627| 150.558|  25,619|
| |Marion County|     1| 35.051|  0.000|   236|  8271.994| 325.472|  28,530|
| |Lincoln County|     1| 16.945|  0.000|   416|  7049.294| 154.930|  59,013|
| |Linn County|     1| 83.893|  0.000|    38|  3187.919| 95.877|  11,920|
| |Laclede County|     1| 27.993|  0.000|   212|  5934.552| 83.980|  35,723|
| |Lewis County|     1| 102.291|  0.000|    52|  5319.149| 219.196|   9,776|
| |Pulaski County|     1| 19.009|  0.000|   254|  4828.255| 160.218|  52,607|
| |Webster County|     1| 25.258|  0.000|   142|  3586.583| 50.515|  39,592|
| |Stone County|     1| 31.297|  0.000|   156|  4882.323| 201.195|  31,952|
| |Shannon County|     1| 122.459|  0.000|    44|  5388.195| 17.494|   8,166|
| |Scotland County|     1| 203.998|  0.000|    16|  3263.974| 58.285|   4,902|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908| 17.105|   8,352|
| |Grundy County|     1| 101.523|  0.000|    30|  3045.685| 72.516|   9,850|
| |DeKalb County|     1| 79.700|  0.000|    38|  3028.612| 22.772|  12,547|
| |Dallas County|     1| 59.249|  0.000|    72|  4265.908| 118.497|  16,878|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313|  0.000|   4,696|
| |Randolph County|     1| 40.407|  0.000|    75|  3030.548| 63.497|  24,748|
| |Ste. Genevieve County|     1| 55.885|  0.000|    63|  3520.733| 95.802|  17,894|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131|  0.000|   9,020|
| |Bollinger County|     1| 82.420|  0.000|    77|  6346.328| 176.614|  12,133|
| |Bates County|     1| 61.835|  0.000|    52|  3215.434| 70.669|  16,172|
| |Benton County|     1| 51.432|  0.000|   112|  5760.428| 183.687|  19,443|
| |Carter County|     1| 167.168|  0.000|    21|  3510.532| 23.881|   5,982|
| |Audrain County|     1| 39.389|  0.000|   210|  8271.624| 67.523|  25,388|
| |Callaway County|     1| 22.350|  0.000|   168|  3754.777| 98.978|  44,743|
| |Washington County|     1| 40.437|  0.000|   105|  4245.855| 219.514|  24,730|
| |Christian County|     1| 11.287|  0.000|   403|  4548.789| 127.385|  88,595|
| |Andrew County|     1| 56.459|  0.000|    94|  5307.136| 48.393|  17,712|
| |Ripley County|     0|  0.000|  0.000|    58|  4364.840| 107.508|  13,288|
| |Holt County|     0|  0.000|  0.000|    31|  7040.654| 811.135|   4,403|
| |Hickory County|     0|  0.000|  0.000|    36|  3772.003| 164.651|   9,544|
| |Mississippi County|     0|  0.000|  0.000|   153| 11608.498| 205.940|  13,180|
| |Phelps County|     0|  0.000|  0.000|   104|  2333.251| 64.100|  44,573|
| |Ozark County|     0|  0.000|  0.000|    16|  1744.059| 109.004|   9,174|
| |Oregon County|     0|  0.000|  0.000|    19|  1804.540| 67.840|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   192|  8690.929| 116.396|  22,092|
| |Morgan County|     0|  0.000|  0.000|    94|  4557.134| 124.663|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    43|  3722.621| 24.735|  11,551|
| |Monroe County|     0|  0.000|  0.000|    33|  3817.677| 115.687|   8,644|
| |Mercer County|     0|  0.000|  0.000|    13|  3594.139| 118.488|   3,617|
| |Maries County|     0|  0.000|  0.000|    27|  3104.519| 114.982|   8,697|
| |Madison County|     0|  0.000|  0.000|    29|  2399.073| 59.090|  12,088|
| |Macon County|     0|  0.000|  0.000|    66|  4365.946| 94.501|  15,117|
| |Livingston County|     0|  0.000|  0.000|    64|  4203.060| 93.818|  15,227|
| |Knox County|     0|  0.000|  0.000|    33|  8335.438| 252.589|   3,959|
| |Iron County|     0|  0.000|  0.000|    24|  2370.370| 14.109|  10,125|
| |Howard County|     0|  0.000|  0.000|    60|  5999.400| 185.696|  10,001|
| |Gasconade County|     0|  0.000|  0.000|    31|  2107.983| 106.856|  14,706|
| |Dent County|     0|  0.000|  0.000|    16|  1027.419| 55.040|  15,573|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Cooper County|     0|  0.000|  0.000|   148|  8357.332| 298.476|  17,709|
| |Ralls County|     0|  0.000|  0.000|    45|  4365.118| 277.150|  10,309|
| |Polk County|     0|  0.000|  0.000|   221|  6874.242| 93.315|  32,149|
| |Daviess County|     0|  0.000|  0.000|    18|  2174.438| 17.257|   8,278|
| |Dade County|     0|  0.000|  0.000|    17|  2248.380| 56.682|   7,561|
| |Crawford County|     0|  0.000|  0.000|    90|  3762.542| 125.418|  23,920|
| |Clinton County|     0|  0.000|  0.000|    88|  4316.476| 112.116|  20,387|
| |Wright County|     0|  0.000|  0.000|    67|  3663.404| 54.678|  18,289|
| |Clark County|     0|  0.000|  0.000|    24|  3530.970| 126.106|   6,797|
| |Chariton County|     0|  0.000|  0.000|    20|  2693.240| 76.950|   7,426|
| |Cedar County|     0|  0.000|  0.000|    41|  2857.342| 39.824|  14,349|
| |Carroll County|     0|  0.000|  0.000|   102| 11752.506| 49.380|   8,679|
| |Barton County|     0|  0.000|  0.000|    71|  6040.497| 60.770|  11,754|
| |Atchison County|     0|  0.000|  0.000|    19|  3694.342| 138.885|   5,143|
| |Adair County|     0|  0.000|  0.000|   178|  7023.636| 157.835|  25,343|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    63|  4893.964| 122.072|  12,873|
| |Warren County|     0|  0.000|  0.000|   216|  6059.076| 108.198|  35,649|
| |Vernon County|     0|  0.000|  0.000|    58|  2820.600| 69.473|  20,563|
| |Texas County|     0|  0.000|  0.000|    64|  2519.883| 95.621|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   149| 24470.356| 211.154|   6,089|
| |Shelby County|     0|  0.000|  0.000|    42|  7082.631| 264.996|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    10|  2145.923|  0.000|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    23|  2447.590| 76.012|   9,397|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867| 12.413|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,291| 189.042| N/A|122,336| 17913.733| N/A|6,829,174|
| |Shelby County|   319| 340.388|  2.896|23,943| 25548.302| 263.865| 937,166|
| |Davidson County|   221| 318.378|  2.058|21,280| 30656.463| 263.222| 694,144|
| |Sumner County|    73| 381.633|  0.747| 3,538| 18496.155| 165.798| 191,283|
| |Hamilton County|    56| 152.255|  2.719| 6,547| 17800.241| 257.513| 367,804|
| |Rutherford County|    55| 165.521|  0.860| 6,834| 20566.682| 230.439| 332,285|
| |Knox County|    41| 87.176|  1.215| 4,946| 10516.401| 196.829| 470,313|
| |Williamson County|    25| 104.860|  0.000| 3,702| 15527.742| 177.963| 238,412|
| |Madison County|    23| 234.732| 11.664| 1,244| 12695.950| 379.071|  97,984|
| |Wilson County|    23| 158.997|  0.000| 2,411| 16667.012| 218.250| 144,657|
| |Robertson County|    21| 292.426|  3.979| 1,596| 22224.388| 179.036|  71,813|
| |Putnam County|    20| 249.237|  7.121| 1,878| 23403.327| 357.833|  80,245|
| |McMinn County|    20| 371.789|  0.000|   583| 10837.640| 196.517|  53,794|
| |Hardeman County|    18| 718.563| 17.109|   975| 38922.156| 667.237|  25,050|
| |Sullivan County|    15| 94.728|  2.707| 1,106|  6984.616| 190.358| 158,348|
| |Bradley County|    15| 138.748|  3.964| 2,066| 19110.166| 329.030| 108,110|
| |Blount County|    15| 112.707|  6.440| 1,373| 10316.482| 162.084| 133,088|
| |Hamblen County|    15| 231.004|  2.200| 1,456| 22422.768| 242.004|  64,934|
| |Montgomery County|    15| 71.773|  1.367| 2,041|  9765.877| 154.482| 208,993|
| |Giles County|    13| 441.216|  0.000|   402| 13643.769| 160.002|  29,464|
| |Macon County|    13| 528.412|  0.000|   873| 35484.920| 104.521|  24,602|
| |Tipton County|    12| 194.808|  6.957| 1,233| 20016.559| 180.893|  61,599|
| |Bedford County|    11| 221.270|  0.000|   955| 19210.267| 155.176|  49,713|
| |Hawkins County|    10| 176.100|  7.547|   520|  9157.187| 261.634|  56,786|
| |Monroe County|    10| 214.846|  3.069|   469| 10076.270| 220.984|  46,545|
| |Lauderdale County|     9| 351.110|  5.573|   535| 20871.533| 445.854|  25,633|
| |Sevier County|     9| 91.603|  4.362| 1,947| 19816.794| 226.827|  98,250|
| |Dyer County|     9| 242.202|  7.689|   696| 18730.321| 395.982|  37,159|
| |Gibson County|     9| 183.176| 14.538|   765| 15569.984| 351.815|  49,133|
| |Maury County|     9| 93.374|  2.964| 1,329| 13788.166| 251.960|  96,387|
| |Cheatham County|     9| 221.310|  7.026|   622| 15294.957| 186.181|  40,667|
| |Greene County|     9| 130.304|  4.137|   552|  7992.008| 277.156|  69,069|
| |Fayette County|     8| 194.491|  0.000|   725| 17625.751| 253.533|  41,133|
| |Hardin County|     8| 311.867|  5.569|   493| 19218.774| 272.883|  25,652|
| |Lawrence County|     7| 158.579|  3.236|   613| 13887.001| 278.323|  44,142|
| |Haywood County|     7| 404.531|  8.256|   547| 31611.188| 924.642|  17,304|
| |Anderson County|     7| 90.935|  1.856|   722|  9379.303| 131.763|  76,978|
| |Cumberland County|     7| 115.664|  2.360|   502|  8294.779| 245.491|  60,520|
| |McNairy County|     6| 233.518|  5.560|   400| 15567.837| 272.437|  25,694|
| |Carter County|     6| 106.400|  2.533|   593| 10515.862| 304.000|  56,391|
| |Carroll County|     6| 216.084| 15.435|   352| 12676.919| 411.588|  27,767|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 63.301|  11,284|
| |Marion County|     5| 172.968|  4.942|   239|  8267.894| 128.491|  28,907|
| |Polk County|     5| 297.053| 16.974|   224| 13307.985| 331.002|  16,832|
| |Cocke County|     5| 138.873| 11.903|   514| 14276.192| 297.586|  36,004|
| |Crockett County|     5| 351.370| 10.039|   285| 20028.110| 321.253|  14,230|
| |Weakley County|     5| 150.024|  8.573|   529| 15872.540| 711.542|  33,328|
| |White County|     5| 182.849|  0.000|   315| 11519.473| 360.473|  27,345|
| |Marshall County|     4| 116.364|  4.156|   325|  9454.545| 207.792|  34,375|
| |Jefferson County|     4| 73.401|  2.621|   616| 11303.789| 238.554|  54,495|
| |Obion County|     4| 133.027|  0.000|   619| 20585.986| 612.876|  30,069|
| |Smith County|     4| 198.442|  0.000|   467| 23168.130| 269.314|  20,157|
| |Warren County|     4| 96.906|  0.000|   567| 13736.463| 304.563|  41,277|
| |Franklin County|     4| 94.769|  0.000|   359|  8505.497| 192.922|  42,208|
| |Humphreys County|     3| 161.447|  0.000|   131|  7049.833| 99.943|  18,582|
| |Coffee County|     3| 53.079|  0.000|   584| 10332.626| 257.810|  56,520|
| |Dickson County|     3| 55.609|  5.296|   743| 13772.522| 240.973|  53,948|
| |Loudon County|     3| 55.486|  0.000|   779| 14407.783| 195.521|  54,068|
| |Decatur County|     3| 257.224|  0.000|   226| 19377.519| 465.452|  11,663|
| |Chester County|     2| 115.627|  0.000|   240| 13875.238| 280.808|  17,297|
| |Wayne County|     2| 119.954|  0.000|   231| 13854.735| 59.977|  16,673|
| |Washington County|     2| 15.459|  0.000| 1,382| 10682.126| 277.157| 129,375|
| |Grundy County|     2| 148.954|  0.000|   124|  9235.123| 170.233|  13,427|
| |Henderson County|     2| 71.131|  0.000|   636| 22619.767| 604.616|  28,117|
| |Hancock County|     2| 302.115| 21.580|    83| 12537.764| 129.478|   6,620|
| |Scott County|     2| 90.629| 12.947|   130|  5890.883| 129.470|  22,068|
| |Roane County|     2| 37.466|  0.000|   510|  9553.782| 232.823|  53,382|
| |Rhea County|     2| 60.301|  4.307|   566| 17065.155| 211.053|  33,167|
| |Bledsoe County|     2| 132.767|  9.483|   727| 48260.754| 388.817|  15,064|
| |Pickett County|     1| 198.098|  0.000|    40|  7923.930| 282.998|   5,048|
| |Sequatchie County|     1| 66.551|  9.507|   115|  7653.401| 142.610|  15,026|
| |Benton County|     1| 61.881|  0.000|   173| 10705.446| 415.488|  16,160|
| |DeKalb County|     1| 48.804|  0.000|   379| 18496.828| 334.658|  20,490|
| |Lincoln County|     1| 29.099|  0.000|   325|  9457.021| 236.945|  34,366|
| |Lewis County|     1| 81.513|  0.000|    80|  6521.030| 151.381|  12,268|
| |Henry County|     1| 30.917|  4.417|   307|  9491.421| 260.583|  32,345|
| |Jackson County|     1| 84.846|  0.000|   137| 11623.961| 303.023|  11,786|
| |Hickman County|     1| 39.717|  5.674|   290| 11517.992| 238.303|  25,178|
| |Morgan County|     1| 46.722|  0.000|   133|  6214.082| 233.612|  21,403|
| |Overton County|     1| 44.962|  0.000|   235| 10566.072| 513.852|  22,241|
| |Campbell County|     1| 25.099|  0.000|   261|  6550.876| 114.739|  39,842|
| |Houston County|     0|  0.000|  0.000|    63|  7681.990| 121.936|   8,201|
| |Grainger County|     0|  0.000|  0.000|   212|  9090.909| 140.897|  23,320|
| |Fentress County|     0|  0.000|  0.000|   104|  5614.641| 192.810|  18,523|
| |Clay County|     0|  0.000|  0.000|    84| 11030.860| 243.880|   7,615|
| |Claiborne County|     0|  0.000|  0.000|   296|  9261.867| 241.381|  31,959|
| |Cannon County|     0|  0.000|  0.000|   159| 10832.538| 223.853|  14,678|
| |Van Buren County|     0|  0.000|  0.000|    39|  6641.689| 97.314|   5,872|
| |Lake County|     0|  0.000|  0.000|   798| 113740.023| 671.934|   7,016|
| |Stewart County|     0|  0.000|  0.000|    79|  5760.117| 52.081|  13,715|
| |Perry County|     0|  0.000|  0.000|    84| 10401.189| 123.824|   8,076|
| |Meigs County|     0|  0.000|  0.000|   113|  9096.764| 161.005|  12,422|
| |Unicoi County|     0|  0.000|  0.000|   180| 10065.425| 255.630|  17,883|
| |Union County|     0|  0.000|  0.000|   166|  8311.636| 178.822|  19,972|
| |Moore County|     0|  0.000|  0.000|    68| 10480.888| 286.243|   6,488|
| |Johnson County|     0|  0.000|  0.000|   318| 17877.221| 746.892|  17,788|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties| 1,022| 331.801| N/A|58,279| 18920.795| N/A|3,080,156|
| |Clark County|   869| 383.374|  7.374|50,569| 22309.377| 276.360|2,266,715|
| |Washoe County|   124| 262.980|  2.121| 5,962| 12644.241| 138.761| 471,519|
| |Nye County|    12| 257.937|  9.212|   416|  8941.814| 128.968|  46,523|
| |Lyon County|     6| 104.330|  2.484|   250|  4347.070| 81.973|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074| 42.439|  16,831|
| |Elko County|     3| 56.842|  2.707|   579| 10970.480| 181.353|  52,778|
| |White Pine County|     1| 104.384|  0.000|    16|  1670.146| 29.824|   9,580|
| |Lander County|     1| 180.766|  0.000|    52|  9399.855| 51.648|   5,532|
| |Douglas County|     1| 20.448|  2.921|   209|  4273.592| 52.580|  48,905|
| |Churchill County|     1| 40.146|  0.000|    82|  3291.983| 183.525|  24,909|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     6|  1455.251| 69.298|   4,123|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Eureka County|     0|  0.000|  0.000|     4|  1971.414| 140.815|   2,029|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,018| 174.841| N/A|63,206| 10855.598| N/A|5,822,434|
| |Milwaukee County|   462| 488.514|  1.511|21,666| 22909.384| 192.898| 945,726|
| |Racine County|    78| 397.329|  0.000| 3,599| 18333.155| 171.011| 196,311|
| |Waukesha County|    61| 150.916|  1.414| 4,515| 11170.268| 206.759| 404,198|
| |Kenosha County|    60| 353.855|  1.685| 2,718| 16029.629| 101.944| 169,561|
| |Brown County|    54| 204.126|  1.080| 4,391| 16598.499| 129.604| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,666|  8534.923| 75.780| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,462|  8949.888| 58.593| 163,354|
| |Walworth County|    24| 231.063|  2.751| 1,401| 13488.274| 160.919| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,147|  8431.716| 189.028| 136,034|
| |Winnebago County|    18| 104.708|  0.000| 1,235|  7184.117| 103.046| 171,907|
| |Ozaukee County|    18| 201.746|  1.601|   737|  8260.387| 180.931|  89,221|
| |Grant County|    16| 311.048|  5.554|   375|  7290.188| 94.425|  51,439|
| |Waupaca County|    16| 313.787|  2.802|   494|  9688.174| 215.729|  50,990|
| |Outagamie County|    14| 74.514|  0.000| 1,326|  7057.509| 111.010| 187,885|
| |Marathon County|    10| 73.696|  2.106|   671|  4945.023| 62.115| 135,692|
| |Sheboygan County|     8| 69.360|  0.000|   804|  6970.695| 104.040| 115,340|
| |Fond du Lac County|     8| 77.367|  2.763|   712|  6885.680| 157.498| 103,403|
| |Clark County|     8| 230.057|  4.108|   191|  5492.609| 45.190|  34,774|
| |Dodge County|     5| 56.922|  0.000|   875|  9961.407| 191.910|  87,839|
| |Marinette County|     5| 123.916|  7.081|   449| 11127.633| 329.262|  40,350|
| |St. Croix County|     5| 55.135|  1.575|   524|  5778.116| 75.613|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   677|  7986.410| 136.505|  84,769|
| |Forest County|     4| 444.247|  0.000|    60|  6663.705| 15.866|   9,004|
| |Eau Claire County|     4| 38.224|  0.000|   629|  6010.741| 120.133| 104,646|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 24.842|  17,252|
| |Barron County|     3| 66.307|  0.000|   315|  6962.249| 123.142|  45,244|
| |Pierce County|     3| 70.169| 10.024|   230|  5379.614| 110.265|  42,754|
| |Door County|     3| 108.429|  0.000|   109|  3939.569| 41.306|  27,668|
| |Sauk County|     3| 46.553|  0.000|   484|  7510.630| 135.227|  64,442|
| |Buffalo County|     2| 153.480|  0.000|    45|  3453.304| 32.889|  13,031|
| |Calumet County|     2| 39.929|  0.000|   355|  7087.384| 191.088|  50,089|
| |Kewaunee County|     2| 97.876|  0.000|   137|  6704.512| 104.867|  20,434|
| |Columbia County|     2| 34.763|  2.483|   274|  4762.567| 89.391|  57,532|
| |Trempealeau County|     2| 67.456|  0.000|   360| 12142.062| 149.367|  29,649|
| |Monroe County|     2| 43.240|  0.000|   249|  5383.435| 24.709|  46,253|
| |Polk County|     2| 45.680|  0.000|   138|  3151.908| 39.154|  43,783|
| |Wood County|     2| 27.398|  1.957|   339|  4643.899| 138.945|  72,999|
| |Adams County|     2| 98.912|  0.000|    91|  4500.495| 63.586|  20,220|
| |Marquette County|     1| 64.210|  0.000|    80|  5136.766| 36.691|  15,574|
| |Iron County|     1| 175.840|  0.000|    76| 13363.812| 75.360|   5,687|
| |Jackson County|     1| 48.443|  0.000|    60|  2906.554| 55.363|  20,643|
| |La Crosse County|     1|  8.473|  0.000|   945|  8007.389| 77.471| 118,016|
| |Juneau County|     1| 37.471|  0.000|   145|  5433.357| 53.531|  26,687|
| |Manitowoc County|     1| 12.661|  0.000|   361|  4570.720| 72.350|  78,981|
| |Oconto County|     1| 26.364|  3.766|   262|  6907.461| 207.149|  37,930|
| |Langlade County|     1| 52.113|  0.000|    67|  3491.584| 74.447|  19,189|
| |Rusk County|     1| 70.532|  0.000|    21|  1481.168| 40.304|  14,178|
| |Taylor County|     1| 49.157|  7.022|    73|  3588.458| 84.269|  20,343|
| |Green County|     1| 27.056|  0.000|   186|  5032.468| 189.394|  36,960|
| |Ashland County|     1| 64.259|  0.000|    29|  1863.514| 64.259|  15,562|
| |Burnett County|     1| 64.876|  0.000|    25|  1621.902| 27.804|  15,414|
| |Bayfield County|     1| 66.507|  0.000|    30|  1995.211| 85.509|  15,036|
| |Waushara County|     1| 40.912|  5.845|   122|  4991.204| 58.445|  24,443|
| |Vilas County|     0|  0.000|  0.000|    66|  2973.643| 135.166|  22,195|
| |Sawyer County|     0|  0.000|  0.000|    86|  5193.864| 293.341|  16,558|
| |Washburn County|     0|  0.000|  0.000|    49|  3117.048| 72.701|  15,720|
| |Dunn County|     0|  0.000|  0.000|   134|  2953.624| 69.275|  45,368|
| |Lafayette County|     0|  0.000|  0.000|   159|  9540.954| 368.608|  16,665|
| |Portage County|     0|  0.000|  0.000|   438|  6188.888| 123.132|  70,772|
| |Crawford County|     0|  0.000|  0.000|    82|  5083.380| 106.273|  16,131|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689|  0.000|   7,287|
| |Vernon County|     0|  0.000|  0.000|    68|  2206.216| 41.714|  30,822|
| |Shawano County|     0|  0.000|  0.000|   207|  5061.248| 118.759|  40,899|
| |Chippewa County|     0|  0.000|  0.000|   252|  3897.430| 75.121|  64,658|
| |Oneida County|     0|  0.000|  0.000|   160|  4495.013| 232.777|  35,595|
| |Price County|     0|  0.000|  0.000|    32|  2396.824| 64.201|  13,351|
| |Iowa County|     0|  0.000|  0.000|    88|  3716.530| 108.600|  23,678|
| |Lincoln County|     0|  0.000|  0.000|    71|  2573.116| 31.064|  27,593|
| |Florence County|     0|  0.000|  0.000|    10|  2328.289| 133.045|   4,295|
| |Douglas County|     0|  0.000|  0.000|   207|  4797.219| 192.021|  43,150|
| |Menominee County|     0|  0.000|  0.000|    26|  5706.760| 188.135|   4,556|
| |Green Lake County|     0|  0.000|  0.000|    60|  3172.421| 45.320|  18,913|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   960| 304.272| N/A|50,371| 15965.097| N/A|3,155,070|
| |Polk County|   210| 428.431|  1.166|10,612| 21650.029| 169.041| 490,161|
| |Linn County|    89| 392.579|  1.260| 2,456| 10833.414| 111.535| 226,706|
| |Black Hawk County|    66| 502.941|  3.266| 3,200| 24385.040| 126.280| 131,228|
| |Woodbury County|    52| 504.330|  1.386| 3,770| 36563.958| 109.456| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   860| 20157.510| 66.968|  42,664|
| |Wapello County|    35| 1000.886|  8.171|   934| 26709.371| 253.286|  34,969|
| |Dallas County|    35| 374.520|  0.000| 1,932| 20673.494| 131.464|  93,453|
| |Dubuque County|    31| 318.566|  0.000| 1,734| 17819.157| 162.953|  97,311|
| |Pottawattamie County|    29| 311.139|  4.598| 1,367| 14666.438| 127.214|  93,206|
| |Tama County|    29| 1720.660|  0.000|   557| 33048.534| 101.714|  16,854|
| |Marshall County|    27| 685.819|  7.257| 1,456| 36983.413| 112.489|  39,369|
| |Jasper County|    27| 726.099|  3.842|   484| 13016.001| 69.152|  37,185|
| |Johnson County|    20| 132.328|  3.781| 2,138| 14145.825| 110.588| 151,140|
| |Cerro Gordo County|    17| 400.471|  0.000|   656| 15453.475| 201.918|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   142|  6426.793| 19.397|  22,095|
| |Scott County|    15| 86.734|  0.826| 1,768| 10223.021| 93.342| 172,943|
| |Story County|    15| 154.453|  1.471| 1,189| 12242.965| 70.607|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Buena Vista County|    12| 611.621|  0.000| 1,800| 91743.119| 65.531|  19,620|
| |Plymouth County|    12| 476.625| 22.696|   479| 19025.301| 153.201|  25,177|
| |Franklin County|    12| 1191.658| 42.559|   255| 25322.741| 312.101|  10,070|
| |Washington County|    10| 455.270|  0.000|   305| 13885.727| 78.046|  21,965|
| |Monroe County|     8| 1038.017| 18.536|    75|  9731.413| 111.216|   7,707|
| |Webster County|     8| 222.816|  3.979|   849| 23646.390| 306.373|  35,904|
| |Poweshiek County|     8| 432.339|  0.000|   160|  8646.779| 54.042|  18,504|
| |Bremer County|     7| 279.307|  0.000|   233|  9296.944| 171.004|  25,062|
| |Guthrie County|     5| 467.771|  0.000|   138| 12910.469| 93.554|  10,689|
| |O'Brien County|     5| 363.557| 31.162|   143| 10397.731| 83.099|  13,753|
| |Lucas County|     4| 465.116|  0.000|    73|  8488.372| 265.781|   8,600|
| |Clinton County|     4| 86.153|  3.077|   434|  9347.606| 221.536|  46,429|
| |Allamakee County|     4| 292.248|  0.000|   158| 11543.801| 41.750|  13,687|
| |Dickinson County|     4| 231.777|  0.000|   384| 22250.550| 57.944|  17,258|
| |Henry County|     4| 200.461|  7.159|   140|  7016.137| 150.346|  19,954|
| |Emmet County|     4| 434.405| 31.029|   193| 20960.035| 77.572|   9,208|
| |Montgomery County|     4| 403.348|  0.000|    61|  6151.054| 115.242|   9,917|
| |Lee County|     4| 118.846|  4.245|   129|  3832.784| 93.379|  33,657|
| |Crawford County|     3| 178.359|  0.000|   739| 43935.791| 110.413|  16,820|
| |Clayton County|     3| 170.950|  0.000|   109|  6211.180| 56.983|  17,549|
| |Clarke County|     3| 319.319|  0.000|   206| 21926.557| 167.262|   9,395|
| |Boone County|     3| 114.355|  5.445|   272| 10368.224| 152.474|  26,234|
| |Sioux County|     3| 86.071|  0.000|   653| 18734.758| 159.846|  34,855|
| |Appanoose County|     3| 241.429|  0.000|    52|  4184.774| 57.483|  12,426|
| |Floyd County|     3| 191.791|  9.133|   167| 10676.384| 219.190|  15,642|
| |Lyon County|     2| 170.140|  0.000|   123| 10463.632| 170.140|  11,755|
| |Pocahontas County|     2| 302.160| 21.583|   121| 18280.707| 129.497|   6,619|
| |Carroll County|     2| 99.182|  7.084|   201|  9967.766| 113.351|  20,165|
| |Hancock County|     2| 188.147|  0.000|   124| 11665.099| 40.317|  10,630|
| |Davis County|     2| 222.222| 15.873|    61|  6777.778| 142.857|   9,000|
| |Jones County|     2| 96.707|  0.000|   135|  6527.731| 55.261|  20,681|
| |Des Moines County|     2| 51.325|  0.000|   199|  5106.885| 172.307|  38,967|
| |Butler County|     2| 138.514|  0.000|   131|  9072.650| 118.726|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    87|  8998.759| 59.105|   9,668|
| |Madison County|     2| 122.414|  0.000|   128|  7834.496| 122.414|  16,338|
| |Grundy County|     1| 81.753|  0.000|    83|  6785.481| 81.753|  12,232|
| |Delaware County|     1| 58.785|  0.000|   123|  7230.615| 201.550|  17,011|
| |Clay County|     1| 62.438|  0.000|   202| 12612.388| 231.911|  16,016|
| |Hamilton County|     1| 67.691|  0.000|   255| 17261.220| 106.372|  14,773|
| |Cherokee County|     1| 89.008|  0.000|   110|  9790.832| 89.008|  11,235|
| |Mills County|     1| 66.186|  9.455|    94|  6221.457| 85.096|  15,109|
| |Keokuk County|     1| 97.599|  0.000|    40|  3903.963| 97.599|  10,246|
| |Jackson County|     1| 51.443|  0.000|   160|  8230.876| 88.188|  19,439|
| |Iowa County|     1| 61.789|  0.000|    98|  6055.363| 35.308|  16,184|
| |Humboldt County|     1| 104.624|  0.000|   124| 12973.425| 358.712|   9,558|
| |Harrison County|     1| 71.179| 10.168|   113|  8043.277| 111.853|  14,049|
| |Cedar County|     1| 53.686|  0.000|   135|  7247.544| 53.686|  18,627|
| |Shelby County|     1| 87.306|  0.000|   188| 16413.480| 137.195|  11,454|
| |Union County|     1| 81.693|  0.000|    81|  6617.106| 70.022|  12,241|
| |Van Buren County|     1| 141.965|  0.000|    38|  5394.662| 81.123|   7,044|
| |Warren County|     1| 19.430|  0.000|   586| 11386.158| 108.255|  51,466|
| |Wright County|     1| 79.605|  0.000|   482| 38369.686| 307.048|  12,562|
| |Winneshiek County|     1| 50.023|  0.000|   102|  5102.296| 78.607|  19,991|
| |Wayne County|     1| 155.255|  0.000|    21|  3260.363| 44.359|   6,441|
| |Audubon County|     1| 181.951|  0.000|    29|  5276.565| 25.993|   5,496|
| |Cass County|     1| 77.906|  0.000|    87|  6777.812| 411.788|  12,836|
| |Ringgold County|     1| 204.332|  0.000|    23|  4699.632| 58.381|   4,894|
| |Buchanan County|     1| 47.226|  0.000|   135|  6375.443| 80.958|  21,175|
| |Benton County|     1| 38.994|  0.000|   162|  6317.021| 89.129|  25,645|
| |Ida County|     0|  0.000|  0.000|    33|  4810.496| 83.299|   6,860|
| |Kossuth County|     0|  0.000|  0.000|    97|  6548.302| 135.017|  14,813|
| |Sac County|     0|  0.000|  0.000|    86|  8846.826| 58.783|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    91| 10240.828| 176.843|   8,886|
| |Page County|     0|  0.000|  0.000|   100|  6619.448| 141.845|  15,107|
| |Osceola County|     0|  0.000|  0.000|    85| 14266.532| 143.864|   5,958|
| |Monona County|     0|  0.000|  0.000|    92| 10679.048| 16.582|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    80|  7557.151| 26.990|  10,586|
| |Marion County|     0|  0.000|  0.000|   183|  5503.263| 90.217|  33,253|
| |Jefferson County|     0|  0.000|  0.000|    87|  4755.398| 54.660|  18,295|
| |Chickasaw County|     0|  0.000|  0.000|    60|  5028.073| 71.830|  11,933|
| |Howard County|     0|  0.000|  0.000|    51|  5568.902| 31.198|   9,158|
| |Adair County|     0|  0.000|  0.000|    38|  5313.199| 219.719|   7,152|
| |Hardin County|     0|  0.000|  0.000|   186| 11041.197| 110.242|  16,846|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473| 48.219|   8,888|
| |Fremont County|     0|  0.000|  0.000|    45|  6465.517| 164.204|   6,960|
| |Fayette County|     0|  0.000|  0.000|    90|  4580.153| 65.431|  19,650|
| |Decatur County|     0|  0.000|  0.000|    27|  3430.750| 72.608|   7,870|
| |Adams County|     0|  0.000|  0.000|    17|  4719.600| 39.661|   3,602|
| |Taylor County|     0|  0.000|  0.000|   100| 16337.200| 93.355|   6,121|
| |Winnebago County|     0|  0.000|  0.000|    92|  8885.455| 206.959|  10,354|
| |Worth County|     0|  0.000|  0.000|    68|  9212.844| 58.064|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   796| 178.169| N/A|37,686|  8435.264| N/A|4,467,673|
| |Jefferson County|   247| 322.136|  1.863| 8,976| 11706.447| 244.071| 766,757|
| |Fayette County|    49| 151.631|  0.884| 3,299| 10208.818| 157.378| 323,152|
| |Kenton County|    41| 245.512|  1.711| 1,472|  8814.477| 88.111| 166,998|
| |Hopkins County|    34| 760.865|  3.197|   433|  9689.836| 54.347|  44,686|
| |Graves County|    25| 670.853|  7.667|   576| 15456.448| 161.005|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,126|  8429.342| 68.444| 133,581|
| |Logan County|    23| 848.646|  0.000|   352| 12987.971| 195.030|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,721| 20474.657| 177.367| 132,896|
| |Shelby County|    21| 428.362|  0.000|   797| 16257.343| 189.412|  49,024|
| |Adair County|    19| 989.480|  0.000|   218| 11352.984| 96.716|  19,202|
| |Oldham County|    16| 239.525|  4.277|   645|  9655.833| 104.792|  66,799|
| |Butler County|    15| 1164.687|  0.000|   300| 23293.734| 22.185|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   154| 11553.755| 96.460|  13,329|
| |Campbell County|    13| 138.913|  0.000|   603|  6443.409| 79.379|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   112|  9218.107| 152.851|  12,150|
| |Muhlenberg County|    11| 359.219|  4.665|   633| 20671.413| 51.317|  30,622|
| |Grayson County|    11| 416.241|  0.000|   214|  8097.779| 118.926|  26,427|
| |Casey County|    10| 618.850|  0.000|   204| 12624.544| 380.151|  16,159|
| |Daviess County|     9| 88.660|  1.407|   805|  7930.175| 91.475| 101,511|
| |Christian County|     9| 127.730|  6.082|   529|  7507.699| 97.318|  70,461|
| |Ohio County|     9| 375.094|  5.954|   362| 15087.105| 101.216|  23,994|
| |Knox County|     8| 256.863|  0.000|   262|  8412.265| 155.953|  31,145|
| |Hardin County|     8| 72.099|  0.000|   703|  6335.731| 176.386| 110,958|
| |Allen County|     8| 375.323|  0.000|   233| 10931.269| 60.320|  21,315|
| |Clark County|     7| 193.034|  0.000|   167|  4605.245|  0.000|  36,263|
| |Gallatin County|     7| 789.266|  0.000|    82|  9245.687| 32.215|   8,869|
| |Franklin County|     7| 137.279|  0.000|   343|  6726.677| 182.105|  50,991|
| |Simpson County|     7| 376.911|  0.000|   156|  8399.742| 76.921|  18,572|
| |Grant County|     6| 239.339|  5.699|   126|  5026.128| 108.273|  25,069|
| |Clay County|     5| 251.244|  0.000|   181|  9095.020| 236.887|  19,901|
| |Pulaski County|     5| 76.948|  6.596|   358|  5509.472| 197.866|  64,979|
| |Russell County|     5| 278.971|  0.000|   130|  7253.250| 231.148|  17,923|
| |Laurel County|     5| 82.219|  2.349|   466|  7662.835| 140.947|  60,813|
| |Bullitt County|     5| 61.217|  1.749|   421|  5154.513| 153.918|  81,676|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686|  0.000|   8,210|
| |McCracken County|     4| 61.145|  0.000|   391|  5976.948| 78.615|  65,418|
| |Bell County|     4| 153.657|  5.488|   327| 12561.463| 159.145|  26,032|
| |Calloway County|     4| 102.561|  0.000|   270|  6922.899| 194.134|  39,001|
| |Pike County|     3| 51.835|  0.000|   253|  4371.415| 49.367|  57,876|
| |Perry County|     3| 116.469|  0.000|   251|  9744.545| 266.214|  25,758|
| |Taylor County|     3| 116.419|  5.544|   150|  5820.948| 243.925|  25,769|
| |Henderson County|     3| 66.357|  0.000|   365|  8073.435| 97.956|  45,210|
| |Harlan County|     3| 115.340|  0.000|   243|  9342.561| 131.817|  26,010|
| |Boyd County|     3| 64.215|  0.000|   196|  4195.385| 36.694|  46,718|
| |Meade County|     3| 104.998|  5.000|   101|  3534.929| 39.999|  28,572|
| |Barren County|     3| 67.798|  3.228|   404|  9130.150| 158.196|  44,249|
| |Breckinridge County|     2| 97.671|  0.000|    79|  3857.987| 153.482|  20,477|
| |Nelson County|     2| 43.259|  0.000|   245|  5299.245| 123.598|  46,233|
| |Henry County|     2| 124.023|  0.000|   134|  8309.562| 212.611|  16,126|
| |Lincoln County|     2| 81.470|  5.819|   118|  4806.713| 104.747|  24,549|
| |Green County|     2| 182.799|  0.000|    52|  4752.765| 274.198|  10,941|
| |Metcalfe County|     2| 198.590|  0.000|    63|  6255.585| 85.110|  10,071|
| |Carroll County|     2| 188.129|  0.000|   164| 15426.583| 188.129|  10,631|
| |Carter County|     2| 74.635|  5.331|   104|  3881.031| 15.993|  26,797|
| |Marshall County|     2| 64.309|  0.000|   142|  4565.916| 50.528|  31,100|
| |Monroe County|     2| 187.793|  0.000|    98|  9201.878| 67.069|  10,650|
| |Floyd County|     2| 56.197|  0.000|   115|  3231.336| 88.310|  35,589|
| |Fulton County|     2| 335.064| 23.933|    93| 15580.499| 526.530|   5,969|
| |Knott County|     1| 67.540|  0.000|    70|  4727.813| 202.621|  14,806|
| |Livingston County|     1| 108.767|  0.000|    35|  3806.831| 31.076|   9,194|
| |McLean County|     1| 108.613|  0.000|    43|  4670.360|  0.000|   9,207|
| |Mason County|     1| 58.582|  0.000|    54|  3163.445|  8.369|  17,070|
| |Larue County|     1| 69.454|  0.000|    61|  4236.700| 79.376|  14,398|
| |Webster County|     1| 77.268|  0.000|    90|  6954.103| 66.230|  12,942|
| |Whitley County|     1| 27.576|  0.000|   168|  4632.694| 23.636|  36,264|
| |Madison County|     1| 10.754|  0.000|   603|  6484.777| 244.274|  92,987|
| |Greenup County|     1| 28.492|  0.000|   125|  3561.456| 89.545|  35,098|
| |Crittenden County|     1| 113.559|  0.000|    32|  3633.886| 64.891|   8,806|
| |Clinton County|     1| 97.867| 13.981|    39|  3816.794| 153.790|  10,218|
| |Carlisle County|     1| 210.084|  0.000|    46|  9663.866| 300.120|   4,760|
| |Bourbon County|     1| 50.536|  0.000|    90|  4548.211| 108.291|  19,788|
| |Anderson County|     1| 43.962|  0.000|    89|  3912.604| 50.242|  22,747|
| |Bath County|     1| 80.000|  0.000|    41|  3280.000| 57.143|  12,500|
| |Fleming County|     0|  0.000|  0.000|    62|  4252.109| 39.190|  14,581|
| |Johnson County|     0|  0.000|  0.000|    73|  3290.067| 173.839|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   361|  6670.978| 95.036|  54,115|
| |Hickman County|     0|  0.000|  0.000|    56| 12785.388| 554.468|   4,380|
| |Hart County|     0|  0.000|  0.000|   109|  5726.294| 157.604|  19,035|
| |Harrison County|     0|  0.000|  0.000|   123|  6512.761| 30.257|  18,886|
| |Hancock County|     0|  0.000|  0.000|    52|  5961.935| 49.137|   8,722|
| |Garrard County|     0|  0.000|  0.000|    84|  4754.896| 105.125|  17,666|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 91.147|  14,106|
| |Elliott County|     0|  0.000|  0.000|    14|  1862.445| 114.027|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    62|  9374.055| 345.587|   6,614|
| |Trimble County|     0|  0.000|  0.000|    34|  4013.694| 16.864|   8,471|
| |Marion County|     0|  0.000|  0.000|   123|  6381.985| 29.649|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    49|  4029.274| 176.207|  12,161|
| |McCreary County|     0|  0.000|  0.000|    48|  2785.677| 91.198|  17,231|
| |Lewis County|     0|  0.000|  0.000|    54|  4067.797| 182.943|  13,275|
| |Scott County|     0|  0.000|  0.000|   415|  7280.191| 147.859|  57,004|
| |Spencer County|     0|  0.000|  0.000|   136|  7028.061| 177.178|  19,351|
| |Todd County|     0|  0.000|  0.000|    34|  2765.577|  0.000|  12,294|
| |Union County|     0|  0.000|  0.000|    70|  4867.534| 79.470|  14,381|
| |Trigg County|     0|  0.000|  0.000|    57|  3890.519| 29.252|  14,651|
| |Woodford County|     0|  0.000|  0.000|   170|  6358.944| 117.560|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    17|  2375.297| 99.802|   7,157|
| |Wayne County|     0|  0.000|  0.000|    76|  3737.766| 161.595|  20,333|
| |Washington County|     0|  0.000|  0.000|    93|  7689.128| 248.036|  12,095|
| |Caldwell County|     0|  0.000|  0.000|    55|  4314.741| 67.243|  12,747|
| |Martin County|     0|  0.000|  0.000|    38|  3394.372| 51.043|  11,195|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Mercer County|     0|  0.000|  0.000|    87|  3966.626| 45.593|  21,933|
| |Lawrence County|     0|  0.000|  0.000|    37|  2415.617|  9.327|  15,317|
| |Leslie County|     0|  0.000|  0.000|    33|  3341.095| 72.318|   9,877|
| |Montgomery County|     0|  0.000|  0.000|   129|  4581.454| 65.957|  28,157|
| |Breathitt County|     0|  0.000|  0.000|    33|  2612.827| 56.555|  12,630|
| |Bracken County|     0|  0.000|  0.000|    33|  3974.467| 51.616|   8,303|
| |Boyle County|     0|  0.000|  0.000|   163|  5422.488| 66.534|  30,060|
| |Ballard County|     0|  0.000|  0.000|    36|  4563.895| 72.443|   7,888|
| |Lee County|     0|  0.000|  0.000|     6|   810.482| 19.297|   7,403|
| |Letcher County|     0|  0.000|  0.000|    62|  2876.630| 39.769|  21,553|
| |Rowan County|     0|  0.000|  0.000|    87|  3556.827| 105.128|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    77|  4612.159| 128.353|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    67|  5421.151| 184.943|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    48|  3289.925| 48.957|  14,590|
| |Owsley County|     0|  0.000|  0.000|    14|  3171.008| 64.714|   4,415|
| |Owen County|     0|  0.000|  0.000|    64|  5871.021| 262.099|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    32|  2404.388| 21.468|  13,309|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   697| 332.407| N/A|21,682| 10340.376| N/A|2,096,829|
| |McKinley County|   230| 3222.778| 16.014| 4,087| 57267.364| 108.093|  71,367|
| |San Juan County|   185| 1492.441|  2.305| 3,072| 24782.588| 53.013| 123,958|
| |Bernalillo County|   134| 197.314|  1.052| 5,264|  7751.196| 49.434| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,149|  7829.749| 31.152| 146,748|
| |Dona Ana County|    31| 142.075|  2.619| 2,572| 11787.621| 146.658| 218,195|
| |Cibola County|    18| 674.789|  5.355|   374| 14020.619| 149.953|  26,675|
| |Otero County|    10| 148.170|  0.000|   204|  3022.670| 14.817|  67,490|
| |Rio Arriba County|     8| 205.545| 11.011|   323|  8298.862| 40.375|  38,921|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024| 17.173|  16,637|
| |Chaves County|     6| 92.858|  0.000|   504|  7800.046| 205.613|  64,615|
| |Lea County|     5| 70.353|  2.010|   876| 12325.876| 295.483|  71,070|
| |Luna County|     5| 210.890| 12.051|   255| 10755.409| 84.356|  23,709|
| |Eddy County|     4| 68.423|  0.000|   350|  5987.000| 175.944|  58,460|
| |Valencia County|     4| 52.159|  0.000|   446|  5815.773| 87.553|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   672|  4469.333| 51.306| 150,358|
| |Curry County|     2| 40.855|  0.000|   575| 11745.720| 172.173|  48,954|
| |Grant County|     2| 74.080|  0.000|    72|  2666.864|  5.291|  26,998|
| |Lincoln County|     2| 102.187|  7.299|   144|  7357.449| 197.075|  19,572|
| |Union County|     2| 492.732|  0.000|    30|  7390.983| 70.390|   4,059|
| |Taos County|     1| 30.560|  0.000|   112|  3422.669| 26.194|  32,723|
| |Torrance County|     1| 64.679|  0.000|    62|  4010.090|  9.240|  15,461|
| |Roosevelt County|     1| 54.054|  0.000|   169|  9135.135| 92.664|  18,500|
| |Quay County|     1| 121.168|  0.000|    41|  4967.890| 121.168|   8,253|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 23.927|  11,941|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635|  0.000|   3,527|
| |Sierra County|     1| 92.670| 13.239|    32|  2965.434| 13.239|  10,791|
| |San Miguel County|     0|  0.000|  0.000|    46|  1686.402| 20.949|  27,277|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Los Alamos County|     0|  0.000|  0.000|    24|  1239.093| 29.502|  19,369|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 34.030|   4,198|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   638| 161.234| N/A|46,101| 11650.578| N/A|3,956,971|
| |Oklahoma County|   121| 151.737|  2.150|11,148| 13979.840| 185.416| 797,434|
| |Tulsa County|   113| 173.432|  1.754|10,999| 16881.231| 225.834| 651,552|
| |Cleveland County|    56| 197.173|  0.503| 3,123| 10995.937| 107.641| 284,014|
| |Washington County|    39| 756.885|  0.000|   661| 12828.226| 152.486|  51,527|
| |McCurtain County|    28| 852.827|  0.000|   879| 26772.661| 174.046|  32,832|
| |Wagoner County|    23| 282.941|  0.000|   922| 11342.248| 205.616|  81,289|
| |Delaware County|    20| 465.019|  3.322|   451| 10486.177| 129.541|  43,009|
| |Rogers County|    19| 205.496|  4.635| 1,053| 11388.832| 233.308|  92,459|
| |Caddo County|    18| 625.826|  9.934|   436| 15158.890| 218.542|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   540|  7941.527| 113.450|  67,997|
| |Creek County|    15| 209.726|  3.995|   657|  9185.985| 209.726|  71,522|
| |Osage County|    11| 234.227|  0.000|   446|  9496.838| 167.305|  46,963|
| |Kay County|    11| 252.653|  0.000|   254|  5833.984| 68.905|  43,538|
| |Comanche County|    10| 82.816|  0.000|   868|  7188.465| 86.366| 120,749|
| |Pottawatomie County|     9| 123.981|  0.000|   475|  6543.421| 94.461|  72,592|
| |Canadian County|     9| 60.685|  1.927| 1,275|  8597.090| 118.481| 148,306|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 25.010|   5,712|
| |Jackson County|     7| 285.365| 11.648|   532| 21687.729| 163.066|  24,530|
| |Grady County|     7| 125.372|  0.000|   453|  8113.336| 63.965|  55,834|
| |Mayes County|     7| 170.316|  3.476|   353|  8588.808| 166.840|  41,100|
| |Texas County|     7| 350.298|  0.000| 1,066| 53345.344| 142.979|  19,983|
| |Garfield County|     6| 98.270|  2.340|   529|  8664.177| 311.190|  61,056|
| |Adair County|     6| 270.343|  0.000|   358| 16130.486| 212.413|  22,194|
| |Carter County|     5| 103.926|  2.969|   358|  7441.126| 95.018|  48,111|
| |Seminole County|     5| 206.118|  0.000|   248| 10223.431| 159.005|  24,258|
| |Garvin County|     4| 144.347|  0.000|   235|  8480.387| 77.329|  27,711|
| |Payne County|     4| 48.909|  0.000|   773|  9451.726| 131.007|  81,784|
| |Pittsburg County|     4| 91.630|  3.272|   395|  9048.426| 467.966|  43,654|
| |Sequoyah County|     4| 96.226|  0.000|   369|  8876.807| 206.198|  41,569|
| |McClain County|     4| 98.829|  0.000|   464| 11464.150| 141.184|  40,474|
| |Pawnee County|     3| 183.195|  0.000|   151|  9220.811| 183.195|  16,376|
| |Ottawa County|     3| 96.379|  0.000|   401| 12882.706| 197.348|  31,127|
| |Okmulgee County|     3| 77.993|  0.000|   496| 12894.839| 204.267|  38,465|
| |Lincoln County|     3| 86.017|  4.096|   190|  5447.716| 155.649|  34,877|
| |Stephens County|     3| 69.536|  3.311|   209|  4844.355| 56.291|  43,143|
| |Cotton County|     2| 352.983|  0.000|    20|  3529.827| 50.426|   5,666|
| |Cherokee County|     2| 41.104|  0.000|   470|  9659.453| 231.944|  48,657|
| |Hughes County|     2| 150.614| 10.758|   152| 11446.645| 301.228|  13,279|
| |Latimer County|     2| 198.551| 14.182|    94|  9331.877| 198.551|  10,073|
| |Noble County|     2| 179.678|  0.000|    87|  7816.009| 51.337|  11,131|
| |Pontotoc County|     2| 52.241|  0.000|   205|  5354.717| 63.436|  38,284|
| |Beckham County|     1| 45.748|  0.000|    61|  2790.613| 58.819|  21,859|
| |Bryan County|     1| 20.836|  0.000|   487| 10146.890| 229.191|  47,995|
| |Choctaw County|     1| 68.157|  0.000|   202| 13767.721| 282.365|  14,672|
| |Craig County|     1| 70.711| 10.102|    90|  6364.022| 121.219|  14,142|
| |Marshall County|     1| 59.063|  0.000|   118|  6969.464| 135.002|  16,931|
| |Le Flore County|     1| 20.059|  0.000|   386|  7742.764| 252.170|  49,853|
| |Major County|     1| 131.079|  0.000|    37|  4849.915| 187.255|   7,629|
| |McIntosh County|     1| 51.031|  0.000|   202| 10308.226| 262.444|  19,596|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 19.704|   7,250|
| |Roger Mills County|     1| 279.096| 39.871|     9|  2511.862| 39.871|   3,583|
| |Nowata County|     1| 99.246|  0.000|    63|  6252.481| 85.068|  10,076|
| |Okfuskee County|     1| 83.382| 11.912|    74|  6170.266| 166.764|  11,993|
| |Kiowa County|     1| 114.837|  0.000|    31|  3559.945| 65.621|   8,708|
| |Logan County|     1| 20.829|  0.000|   235|  4894.712| 110.094|  48,011|
| |Haskell County|     1| 79.195| 11.314|    74|  5860.458| 271.527|  12,627|
| |Harper County|     0|  0.000|  0.000|    11|  2982.646| 77.471|   3,688|
| |Custer County|     0|  0.000|  0.000|   217|  7481.985| 73.884|  29,003|
| |Beaver County|     0|  0.000|  0.000|    39|  7343.250| 80.695|   5,311|
| |Grant County|     0|  0.000|  0.000|    16|  3692.592| 131.878|   4,333|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Dewey County|     0|  0.000|  0.000|    11|  2249.029| 87.624|   4,891|
| |Coal County|     0|  0.000|  0.000|    40|  7279.345| 233.979|   5,495|
| |Cimarron County|     0|  0.000|  0.000|     2|   935.891| 66.849|   2,137|
| |Blaine County|     0|  0.000|  0.000|    45|  4772.510| 75.754|   9,429|
| |Atoka County|     0|  0.000|  0.000|    80|  5814.799| 134.986|  13,758|
| |Alfalfa County|     0|  0.000|  0.000|     4|   701.508| 25.054|   5,702|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 269.237|   2,653|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 23.802|   6,002|
| |Johnston County|     0|  0.000|  0.000|    52|  4691.024| 90.212|  11,085|
| |Woodward County|     0|  0.000|  0.000|    45|  2226.510| 63.615|  20,211|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    31|  2839.868| 65.435|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   112| 10093.727| 90.123|  11,096|
| |Murray County|     0|  0.000|  0.000|    78|  5542.528| 91.360|  14,073|
| |Love County|     0|  0.000|  0.000|    78|  7607.530| 125.399|  10,253|
| |Kingfisher County|     0|  0.000|  0.000|   144|  9134.158| 262.788|  15,765|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   594| 841.659| N/A|13,024| 18454.153| N/A| 705,749|
| |District of Columbia|   594| 841.659|  1.417|13,024| 18454.153| 102.424| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   593| 608.977| N/A|15,709| 16132.246| N/A| 973,764|
| |New Castle County|   293| 524.382|  1.023| 7,379| 13206.193| 73.378| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,928| 25308.998| 86.608| 234,225|
| |Kent County|   108| 597.391|  0.790| 2,402| 13286.427| 122.481| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   582| 192.855| N/A|49,950| 16551.771| N/A|3,017,804|
| |Pulaski County|    88| 224.541|  2.552| 5,880| 15003.406| 239.850| 391,911|
| |Washington County|    53| 221.584|  1.195| 6,373| 26644.425| 110.493| 239,187|
| |Benton County|    43| 154.044|  1.535| 4,864| 17424.886| 102.867| 279,141|
| |Jefferson County|    41| 613.552|  2.138| 1,644| 24601.939| 472.456|  66,824|
| |Crittenden County|    24| 500.469| 11.916| 1,442| 30069.857| 378.331|  47,955|
| |Sebastian County|    21| 164.285|  4.470| 2,344| 18337.284| 341.980| 127,827|
| |Union County|    19| 491.185|  7.386|   532| 13753.167| 251.132|  38,682|
| |Garland County|    17| 171.050| 12.937| 1,134| 11410.058| 280.292|  99,386|
| |Yell County|    17| 796.589| 20.082| 1,084| 50794.246| 194.127|  21,341|
| |Mississippi County|    14| 344.395|  3.514| 1,089| 26789.009| 614.991|  40,651|
| |Craighead County|    12| 108.763|  0.000| 1,445| 13096.835| 234.358| 110,332|
| |Columbia County|    12| 511.574| 24.361|   226|  9634.651| 103.533|  23,457|
| |Lincoln County|    12| 921.376| 10.969| 1,224| 93980.344| 296.157|  13,024|
| |Hot Spring County|    12| 355.334|  0.000| 1,569| 46459.980| 359.565|  33,771|
| |Sevier County|    11| 646.792|  8.400| 1,017| 59798.906| 403.195|  17,007|
| |Pope County|    11| 171.682|  2.230| 1,380| 21538.269| 231.882|  64,072|
| |Newton County|    10| 1289.823| 73.704|   107| 13801.109| 92.130|   7,753|
| |Chicot County|     9| 889.504| 14.119|   746| 73729.986| 550.645|  10,118|
| |Nevada County|     9| 1090.645|  0.000|   147| 17813.863| 190.430|   8,252|
| |Lawrence County|     9| 548.580|  0.000|   223| 13592.588| 156.737|  16,406|
| |Phillips County|     9| 506.130| 16.068|   334| 18783.039| 289.217|  17,782|
| |Lee County|     8| 903.240|  0.000|   901| 101727.447| 177.422|   8,857|
| |Saline County|     8| 65.340|  2.334| 1,158|  9457.925| 213.521| 122,437|
| |Carroll County|     7| 246.653|  0.000|   380| 13389.711| 151.012|  28,380|
| |Faulkner County|     6| 47.616|  1.134| 1,361| 10800.987| 123.576| 126,007|
| |Crawford County|     5| 79.043|  4.517|   682| 10781.415| 225.836|  63,257|
| |Ashley County|     5| 254.362|  0.000|   337| 17144.020| 283.432|  19,657|
| |Cleburne County|     5| 200.650|  0.000|   210|  8427.304| 126.123|  24,919|
| |Sharp County|     5| 286.664|  0.000|   120|  6879.945| 106.475|  17,442|
| |Miller County|     5| 115.588|  0.000|   527| 12182.999| 105.681|  43,257|
| |Howard County|     4| 302.984| 10.821|   362| 27420.088| 432.835|  13,202|
| |Bradley County|     4| 371.644| 13.273|   212| 19697.110| 517.646|  10,763|
| |Clay County|     4| 274.895|  0.000|   140|  9621.332| 215.989|  14,551|
| |Cross County|     4| 243.620|  8.701|   217| 13216.396| 295.825|  16,419|
| |Randolph County|     4| 222.742|  7.955|   245| 13642.945| 365.933|  17,958|
| |Poinsett County|     4| 170.010|  6.072|   319| 13558.313| 619.323|  23,528|
| |White County|     3| 38.094|  1.814|   342|  4342.692| 96.141|  78,753|
| |Drew County|     3| 164.663|  0.000|   234| 12843.735| 407.738|  18,219|
| |Conway County|     3| 143.913|  0.000|   161|  7723.304| 123.354|  20,846|
| |St. Francis County|     3| 120.029|  0.000| 1,231| 49251.820| 377.233|  24,994|
| |Greene County|     3| 66.189|  6.304|   523| 11538.886| 245.844|  45,325|
| |Desha County|     2| 176.041|  0.000|   206| 18132.207| 339.507|  11,361|
| |Franklin County|     2| 112.899|  0.000|   136|  7677.110| 137.091|  17,715|
| |Cleveland County|     2| 251.383|  0.000|   115| 14454.500| 502.765|   7,956|
| |Hempstead County|     2| 92.885|  0.000|   255| 11842.839| 185.770|  21,532|
| |Independence County|     2| 52.875|  3.777|   584| 15439.524| 532.528|  37,825|
| |Johnson County|     2| 75.250|  0.000|   679| 25547.445| 145.125|  26,578|
| |Lafayette County|     2| 301.932|  0.000|    58|  8756.039| 129.400|   6,624|
| |Ouachita County|     2| 85.536|  0.000|   110|  4704.474| 158.852|  23,382|
| |Little River County|     2| 163.145| 11.653|   193| 15743.535| 337.944|  12,259|
| |Lonoke County|     2| 27.282|  0.000|   546|  7447.926| 124.717|  73,309|
| |Madison County|     2| 120.656|  0.000|   275| 16590.251| 51.710|  16,576|
| |Boone County|     2| 53.430|  3.816|   222|  5930.754| 110.677|  37,432|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385|  8.634|  16,545|
| |Stone County|     1| 79.962|  0.000|    76|  6077.083| 171.346|  12,506|
| |Polk County|     1| 50.090|  0.000|   157|  7864.155| 143.115|  19,964|
| |Dallas County|     1| 142.674| 20.382|    67|  9559.138| 163.056|   7,009|
| |Montgomery County|     1| 111.284|  0.000|    38|  4228.800| 63.591|   8,986|
| |Logan County|     1| 46.585|  0.000|   321| 14953.881| 638.884|  21,466|
| |Jackson County|     1| 59.812|  0.000|   119|  7117.651| 478.498|  16,719|
| |Izard County|     1| 73.373|  0.000|    62|  4549.123| 157.228|  13,629|
| |Pike County|     1| 93.301|  0.000|   126| 11755.925| 466.505|  10,718|
| |Arkansas County|     1| 57.189|  0.000|   241| 13782.455| 269.603|  17,486|
| |Clark County|     1| 44.803|  0.000|   183|  8198.925| 51.203|  22,320|
| |Woodruff County|     0|  0.000|  0.000|    22|  3481.013| 45.208|   6,320|
| |Baxter County|     0|  0.000|  0.000|    78|  1860.155| 34.069|  41,932|
| |Prairie County|     0|  0.000|  0.000|   104| 12900.025| 425.276|   8,062|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 68.320|  10,455|
| |Monroe County|     0|  0.000|  0.000|    65|  9700.045| 213.188|   6,701|
| |Marion County|     0|  0.000|  0.000|    31|  1856.955| 51.344|  16,694|
| |Grant County|     0|  0.000|  0.000|   144|  7883.931| 101.678|  18,265|
| |Fulton County|     0|  0.000|  0.000|    44|  3526.489| 160.295|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    17|  3276.161| 110.123|   5,189|
| |Searcy County|     0|  0.000|  0.000|    32|  4060.398| 72.507|   7,881|
| |Scott County|     0|  0.000|  0.000|    70|  6808.676| 264.010|  10,281|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   422| 310.360| N/A| 6,921|  5090.052| N/A|1,359,711|
| |Hillsborough County|   280| 671.423|  0.343| 3,891|  9330.376| 28.775| 417,025|
| |Rockingham County|    96| 309.908|  0.000| 1,712|  5526.699| 21.675| 309,769|
| |Merrimack County|    23| 151.924|  1.887|   472|  3117.755| 11.324| 151,391|
| |Strafford County|    13| 99.515|  0.000|   363|  2778.777| 18.591| 130,633|
| |Belknap County|     4| 65.250|  0.000|   119|  1941.177| 13.982|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   103|  1353.749| 13.143|  76,085|
| |Sullivan County|     1| 23.177|  0.000|    44|  1019.793| 13.244|  43,146|
| |Grafton County|     1| 11.125|  0.000|   105|  1168.146|  3.179|  89,886|
| |Carroll County|     1| 20.446|  0.000|    95|  1942.343|  5.842|  48,910|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   402| 137.987| N/A|32,484| 11150.188| N/A|2,913,314|
| |Wyandotte County|   108| 652.848|  8.636| 5,087| 30750.352| 299.654| 165,429|
| |Johnson County|   106| 175.963|  0.949| 6,127| 10170.966| 163.157| 602,401|
| |Sedgwick County|    46| 89.140|  0.554| 5,141|  9962.367| 148.936| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,682|  9509.541| 151.843| 176,875|
| |Lyon County|    14| 421.750|  4.304|   731| 22021.389| 193.661|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,798| 49304.851| 70.514|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,093| 62256.462| 161.473|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,503| 18383.522| 103.092|  81,758|
| |Coffey County|     8| 978.115|  0.000|    68|  8313.975| 17.466|   8,179|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982|  0.000|   5,234|
| |Saline County|     7| 129.094|  5.269|   389|  7173.945| 71.133|  54,224|
| |Montgomery County|     5| 157.089|  0.000|   177|  5560.966| 67.324|  31,829|
| |Douglas County|     5| 40.897|  0.000|   783|  6404.436| 101.658| 122,259|
| |Riley County|     5| 67.356|  0.000|   489|  6587.456| 46.187|  74,232|
| |Seward County|     4| 186.672|  0.000| 1,252| 58428.225| 246.673|  21,428|
| |Sumner County|     3| 131.372|  0.000|   101|  4422.841| 18.767|  22,836|
| |Barton County|     3| 116.374|  0.000|   157|  6090.228| 171.790|  25,779|
| |Grant County|     2| 279.720|  0.000|   120| 16783.217| 379.620|   7,150|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Geary County|     2| 63.151|  0.000|   157|  4957.373| 103.748|  31,670|
| |Bourbon County|     2| 137.608|  0.000|    79|  5435.530| 58.975|  14,534|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 35.705|   8,002|
| |Cowley County|     2| 57.293|  0.000|   178|  5099.118| 73.663|  34,908|
| |Jewell County|     1| 347.343| 49.620|    12|  4168.114| 99.241|   2,879|
| |Nemaha County|     1| 97.742|  0.000|    49|  4789.366| 13.963|  10,231|
| |Jackson County|     1| 75.924|  0.000|   163| 12375.674| 184.388|  13,171|
| |Kearny County|     1| 260.552|  0.000|    63| 16414.799| 223.331|   3,838|
| |Labette County|     1| 50.974|  7.282|   148|  7544.092| 182.049|  19,618|
| |McPherson County|     1| 35.036|  0.000|   151|  5290.449| 70.072|  28,542|
| |Ellis County|     1| 35.023|  0.000|   145|  5078.275| 50.032|  28,553|
| |Franklin County|     1| 39.148|  0.000|   210|  8221.109| 212.518|  25,544|
| |Harvey County|     1| 29.045|  0.000|   211|  6128.554| 124.480|  34,429|
| |Dickinson County|     1| 54.154|  0.000|    50|  2707.679| 46.417|  18,466|
| |Crawford County|     1| 25.761|  0.000|   389| 10021.124| 44.162|  38,818|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199|  0.000|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   152|  7623.251| 437.047|  19,939|
| |Butler County|     1| 14.945|  0.000|   290|  4334.115| 111.022|  66,911|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 24.042|  11,884|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090| 284.860|   2,006|
| |Stafford County|     1| 240.616|  0.000|     6|  1443.696| 103.121|   4,156|
| |Reno County|     1| 16.130|  0.000|   397|  6403.432| 345.633|  61,998|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Scott County|     0|  0.000|  0.000|    64| 13269.749| 888.599|   4,823|
| |Russell County|     0|  0.000|  0.000|    16|  2333.722| 62.510|   6,856|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 59.917|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   109|  4470.328| 17.577|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     8|  1247.272| 22.273|   6,414|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Sherman County|     0|  0.000|  0.000|    16|  2704.073| 24.144|   5,917|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 16.757|   8,525|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 26.045|   5,485|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 20.611|   6,931|
| |Thomas County|     0|  0.000|  0.000|    44|  5657.709| 165.323|   7,777|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946| 57.748|  12,369|
| |Linn County|     0|  0.000|  0.000|    43|  4431.619| 103.061|   9,703|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 71.644|   5,982|
| |Hamilton County|     0|  0.000|  0.000|    39| 15360.378| 112.530|   2,539|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818|  0.000|   2,750|
| |Neosho County|     0|  0.000|  0.000|    66|  4123.196| 89.247|  16,007|
| |Morris County|     0|  0.000|  0.000|    13|  2313.167| 50.839|   5,620|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Miami County|     0|  0.000|  0.000|   150|  4381.225| 70.934|  34,237|
| |Meade County|     0|  0.000|  0.000|    52| 12893.628| 354.221|   4,033|
| |Marshall County|     0|  0.000|  0.000|    15|  1545.277| 88.302|   9,707|
| |Harper County|     0|  0.000|  0.000|    14|  2575.423| 105.119|   5,436|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024| 36.360|   7,858|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    20|  2796.421| 159.795|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    85|  4463.582| 75.018|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Atchison County|     0|  0.000|  0.000|    82|  5101.723| 159.984|  16,073|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Ottawa County|     0|  0.000|  0.000|    35|  6136.045| 75.135|   5,704|
| |Osage County|     0|  0.000|  0.000|    46|  2884.193| 71.657|  15,949|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Gray County|     0|  0.000|  0.000|    87| 14529.058| 238.572|   5,988|
| |Graham County|     0|  0.000|  0.000|    17|  6849.315| 57.557|   2,482|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495|  0.000|   6,102|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 18.797|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Comanche County|     0|  0.000|  0.000|     7|  4117.647| 336.134|   1,700|
| |Cloud County|     0|  0.000|  0.000|    40|  4552.697| 162.596|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     4|  1505.457| 107.533|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Chase County|     0|  0.000|  0.000|    48| 18126.888| 323.694|   2,648|
| |Brown County|     0|  0.000|  0.000|    41|  4286.909| 89.622|   9,564|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   383| 90.807| N/A|22,300|  5287.195| N/A|4,217,737|
| |Multnomah County|   101| 124.253|  1.406| 5,135|  6317.240| 84.710| 812,855|
| |Marion County|    73| 209.880|  2.054| 3,040|  8740.203| 103.092| 347,818|
| |Clackamas County|    49| 117.172|  3.758| 1,607|  3842.778| 42.018| 418,187|
| |Umatilla County|    31| 397.691|  9.163| 2,362| 30301.475| 357.372|  77,950|
| |Washington County|    27| 44.881|  0.712| 3,235|  5377.399| 69.340| 601,592|
| |Malheur County|    15| 490.661| 14.019|   851| 27836.839| 546.737|  30,571|
| |Yamhill County|    13| 121.382|  1.334|   483|  4509.804| 93.371| 107,100|
| |Polk County|    12| 139.397|  0.000|   337|  3914.735| 59.742|  86,085|
| |Linn County|    11| 84.779|  1.101|   306|  2358.400| 45.142| 129,749|
| |Deschutes County|    11| 55.642|  2.168|   621|  3141.250| 39.022| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   428|  8566.511| 48.608|  49,962|
| |Benton County|     6| 64.479|  0.000|   181|  1945.128| 30.704|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   392| 15897.477| 295.471|  24,658|
| |Morrow County|     3| 258.554|  0.000|   384| 33094.889| 677.165|  11,603|
| |Lane County|     3|  7.852|  0.000|   611|  1599.196| 22.060| 382,067|
| |Wasco County|     3| 112.435|  0.000|   197|  7383.255| 101.727|  26,682|
| |Josephine County|     2| 22.861|  0.000|   130|  1485.935| 32.658|  87,487|
| |Jackson County|     2|  9.052|  0.647|   515|  2330.907| 50.433| 220,944|
| |Klamath County|     2| 29.309|  2.094|   206|  3018.846| 12.561|  68,238|
| |Union County|     2| 74.530|  0.000|   397| 14794.112| 26.618|  26,835|
| |Wallowa County|     1| 138.735|  0.000|    20|  2774.695| 19.819|   7,208|
| |Columbia County|     1| 19.101|  2.729|   103|  1967.376| 35.473|  52,354|
| |Douglas County|     1|  9.011|  0.000|   159|  1432.691| 18.021| 110,980|
| |Crook County|     1| 40.977|  0.000|    51|  2089.821| 46.831|  24,404|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137|  2.215|  64,487|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 80.257|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Hood River County|     0|  0.000|  0.000|   207|  8852.964| 177.181|  23,382|
| |Harney County|     0|  0.000|  0.000|    11|  1487.894| 19.323|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 19.844|   7,199|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Curry County|     0|  0.000|  0.000|    17|   741.549| 18.695|  22,925|
| |Clatsop County|     0|  0.000|  0.000|    87|  2162.888| 14.206|  40,224|
| |Baker County|     0|  0.000|  0.000|    45|  2790.871| 70.879|  16,124|
| |Tillamook County|     0|  0.000|  0.000|    35|  1294.570|  5.284|  27,036|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   360| 186.103| N/A|29,505| 15252.728| N/A|1,934,408|
| |Douglas County|   142| 248.544|  2.750|11,802| 20657.172| 195.035| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,763| 28735.351| 67.525|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,935| 96624.388| 142.672|  20,026|
| |Lancaster County|    19| 59.544|  0.895| 3,390| 10623.962| 76.557| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   101| 10832.261| 30.643|   9,324|
| |Adams County|    11| 350.732|  0.000|   363| 11574.148| 59.214|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,409| 12868.865| 175.523| 187,196|
| |Dodge County|    10| 273.486|  7.814|   832| 22754.000| 171.905|  36,565|
| |Dawson County|     9| 381.437|  0.000|   968| 41025.641| 84.764|  23,595|
| |Perkins County|     7| 2421.308| 49.414|    19|  6572.120| 98.829|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   309|  8675.389| 48.130|  35,618|
| |Howard County|     5| 775.795| 22.166|    55|  8533.747|  0.000|   6,445|
| |Madison County|     5| 142.454|  0.000|   477| 13590.131| 175.015|  35,099|
| |Custer County|     4| 371.161|  0.000|    53|  4917.881| 145.813|  10,777|
| |Colfax County|     4| 373.518|  0.000|   705| 65832.477| 93.379|  10,709|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 118.652|   7,224|
| |Gage County|     4| 185.934|  0.000|    93|  4322.968| 39.843|  21,513|
| |Platte County|     3| 89.633|  0.000|   804| 24021.512| 89.633|  33,470|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Saline County|     2| 140.607|  0.000|   597| 41971.316| 30.130|  14,224|
| |Saunders County|     2| 92.687|  0.000|   170|  7878.395| 132.410|  21,578|
| |Lincoln County|     2| 57.284|  0.000|   154|  4410.838| 233.226|  34,914|
| |Cass County|     2| 76.196|  0.000|   203|  7733.923| 185.048|  26,248|
| |Buffalo County|     1| 20.137|  0.000|   462|  9303.450| 221.511|  49,659|
| |Antelope County|     1| 158.781|  0.000|    20|  3175.611| 22.683|   6,298|
| |Fillmore County|     1| 183.083|  0.000|    28|  5126.327| 104.619|   5,462|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Washington County|     1| 48.242|  0.000|   134|  6464.374| 124.050|  20,729|
| |Seward County|     1| 57.857|  0.000|   127|  7347.836| 140.510|  17,284|
| |Richardson County|     1| 127.146|  0.000|    24|  3051.494| 54.491|   7,865|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Otoe County|     0|  0.000|  0.000|    57|  3559.830| 115.984|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     6|  1446.480| 34.440|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    48|  6884.682| 471.273|   6,972|
| |Nance County|     0|  0.000|  0.000|     9|  2557.545| 40.596|   3,519|
| |Morrill County|     0|  0.000|  0.000|    63| 13571.736| 153.875|   4,642|
| |Merrick County|     0|  0.000|  0.000|    62|  7994.842| 55.264|   7,755|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457|  0.000|     494|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    39|  4680.749| 85.728|   8,332|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Phelps County|     0|  0.000|  0.000|    42|  4649.103| 79.066|   9,034|
| |Keith County|     0|  0.000|  0.000|    32|  3983.072| 213.379|   8,034|
| |Red Willow County|     0|  0.000|  0.000|    18|  1678.478| 26.643|  10,724|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759|  0.000|   1,357|
| |Sheridan County|     0|  0.000|  0.000|    12|  2287.457| 81.695|   5,246|
| |York County|     0|  0.000|  0.000|    89|  6506.324| 125.322|  13,679|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |Pierce County|     0|  0.000|  0.000|    37|  5176.273| 359.741|   7,148|
| |Polk County|     0|  0.000|  0.000|    27|  5179.359| 27.404|   5,213|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139| 182.448|     783|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Cedar County|     0|  0.000|  0.000|    24|  2856.463| 34.006|   8,402|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Garfield County|     0|  0.000|  0.000|     4|  2031.488| 72.553|   1,969|
| |Holt County|     0|  0.000|  0.000|    14|  1390.682| 28.381|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 60.635|   2,356|
| |Gosper County|     0|  0.000|  0.000|    20| 10050.251| 71.788|   1,990|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Cheyenne County|     0|  0.000|  0.000|    27|  3030.303| 16.033|   8,910|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Franklin County|     0|  0.000|  0.000|    15|  5035.247| 143.864|   2,979|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827|  0.000|   1,794|
| |Dawes County|     0|  0.000|  0.000|    12|  1397.136| 49.898|   8,589|
| |Cuming County|     0|  0.000|  0.000|    68|  7687.090| 16.149|   8,846|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 23.030|   6,203|
| |Sherman County|     0|  0.000|  0.000|    12|  3998.667| 47.603|   3,001|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Wayne County|     0|  0.000|  0.000|    38|  4049.014| 15.222|   9,385|
| |Valley County|     0|  0.000|  0.000|    11|  2645.503| 34.357|   4,158|
| |Thomas County|     0|  0.000|  0.000|     2|  2770.083| 197.863|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 28.554|   5,003|
| |Stanton County|     0|  0.000|  0.000|    32|  5405.405| 96.525|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Kearney County|     0|  0.000|  0.000|    67| 10315.627| 395.909|   6,495|
| |Johnson County|     0|  0.000|  0.000|    14|  2760.797| 28.171|   5,071|
| |Jefferson County|     0|  0.000|  0.000|    18|  2554.641| 60.825|   7,046|
| |Butler County|     0|  0.000|  0.000|    63|  7859.281| 89.107|   8,016|
| |Burt County|     0|  0.000|  0.000|    45|  6967.023| 353.881|   6,459|
| |Brown County|     0|  0.000|  0.000|     1|   338.409| 48.344|   2,955|
| |Boyd County|     0|  0.000|  0.000|     7|  3647.733| 223.331|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    15|  1391.079| 52.993|  10,783|
| |Boone County|     0|  0.000|  0.000|    10|  1926.040| 82.545|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827|  0.000|     463|
| |Chase County|     0|  0.000|  0.000|     7|  1783.894| 36.406|   3,924|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   292| 91.080| N/A|36,128| 11269.018| N/A|3,205,958|
| |Salt Lake County|   204| 175.796|  2.216|21,199| 18268.118| 137.510|1,160,437|
| |Utah County|    37| 58.155|  0.000| 9,062| 14243.165| 141.008| 636,235|
| |San Juan County|    25| 1633.133|  0.000|   651| 42526.783| 55.993|  15,308|
| |Davis County|    21| 59.075|  0.804| 3,316|  9328.206| 75.150| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   584| 17130.621| 163.428|  34,091|
| |Summit County|     1| 23.728|  0.000|   718| 17036.422| 40.676|  42,145|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Tooele County|     0|  0.000|  0.000|   598|  8275.786| 49.425|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   251| 140.454| N/A|26,624| 14898.171| N/A|1,787,065|
| |Ada County|    90| 186.882|  5.339| 9,595| 19923.711| 304.351| 481,587|
| |Canyon County|    51| 221.885|  3.108| 6,137| 26700.138| 425.124| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,482| 17058.404| 282.827|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   168|  4157.593| 98.990|  40,408|
| |Kootenai County|    16| 96.562|  0.862| 1,946| 11744.329| 187.088| 165,697|
| |Jerome County|     6| 245.781|  0.000|   505| 20686.548| 275.040|  24,412|
| |Blaine County|     6| 260.632|  0.000|   582| 25281.265| 43.439|  23,021|
| |Bonneville County|     4| 33.596|  1.200| 1,206| 10129.176| 350.358| 119,062|
| |Elmore County|     3| 109.047|  0.000|   229|  8323.943| 124.625|  27,511|
| |Payette County|     3| 125.256|  5.965|   424| 17702.810| 339.980|  23,951|
| |Washington County|     3| 294.291|  0.000|   224| 21973.710| 336.332|  10,194|
| |Owyhee County|     3| 253.743| 12.083|   272| 23006.005| 205.411|  11,823|
| |Bingham County|     2| 42.725|  0.000|   320|  6836.000| 277.713|  46,811|
| |Bannock County|     2| 22.777|  0.000|   464|  5284.257| 144.796|  87,808|
| |Minidoka County|     2| 95.062|  0.000|   498| 23670.327| 230.864|  21,039|
| |Shoshone County|     2| 155.255|  0.000|   154| 11954.665| 798.456|  12,882|
| |Boise County|     1| 127.698|  0.000|    52|  6640.276| 164.183|   7,831|
| |Cassia County|     1| 41.615|  0.000|   543| 22596.754| 237.798|  24,030|
| |Jefferson County|     1| 33.477|  0.000|   229|  7666.298| 263.036|  29,871|
| |Benewah County|     1| 107.550| 15.364|    80|  8604.001| 307.286|   9,298|
| |Gem County|     1| 55.212|  0.000|   187| 10324.647| 126.199|  18,112|
| |Gooding County|     1| 65.880|  0.000|   175| 11529.086| 216.464|  15,179|
| |Valley County|     1| 87.781|  0.000|    69|  6056.882| 163.022|  11,392|
| |Bonner County|     0|  0.000|  0.000|   189|  4132.141| 46.850|  45,739|
| |Power County|     0|  0.000|  0.000|    64|  8332.248| 167.389|   7,681|
| |Madison County|     0|  0.000|  0.000|   177|  4435.312| 96.653|  39,907|
| |Bear Lake County|     0|  0.000|  0.000|    20|  3265.306| 186.589|   6,125|
| |Oneida County|     0|  0.000|  0.000|    16|  3531.229| 94.586|   4,531|
| |Lincoln County|     0|  0.000|  0.000|    60| 11181.513| 106.491|   5,366|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Butte County|     0|  0.000|  0.000|     1|   385.060| 55.009|   2,597|
| |Lemhi County|     0|  0.000|  0.000|    35|  4360.284| 373.739|   8,027|
| |Latah County|     0|  0.000|  0.000|   124|  3091.653| 103.293|  40,108|
| |Idaho County|     0|  0.000|  0.000|    33|  1979.960| 25.714|  16,667|
| |Fremont County|     0|  0.000|  0.000|    90|  6870.753| 196.307|  13,099|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 20.591|  13,876|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 66.214|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|    10| 11834.320| 338.123|     845|
| |Caribou County|     0|  0.000|  0.000|    34|  4751.922| 59.898|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Boundary County|     0|  0.000|  0.000|    38|  3103.307| 23.333|  12,245|
| |Teton County|     0|  0.000|  0.000|    90|  7412.288| 235.311|  12,142|
| |Adams County|     0|  0.000|  0.000|    21|  4890.545| 66.538|   4,294|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   153| 85.372| N/A| 8,163|  4554.872| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  1.604| 1,020|  5726.348| 115.489| 178,124|
| |Jackson County|    19| 664.894|  0.000|   166|  5809.071| 29.995|  28,576|
| |Mercer County|    16| 272.303| 31.607|   216|  3676.095| 102.114|  58,758|
| |Berkeley County|    11| 92.304|  0.000|   720|  6041.738| 53.944| 119,171|
| |Wayne County|     9| 228.415|  0.000|   214|  5431.196| 65.261|  39,402|
| |Logan County|     7| 218.620| 17.847|   276|  8619.882| 446.164|  32,019|
| |Fayette County|     7| 165.071|  6.738|   160|  3773.051| 77.482|  42,406|
| |Mingo County|     5| 213.456| 12.198|   195|  8324.795| 237.851|  23,424|
| |Monongalia County|     5| 47.343|  0.000|   962|  9108.813| 44.638| 105,612|
| |Wood County|     5| 59.867|  0.000|   266|  3184.942| 41.052|  83,518|
| |Jefferson County|     4| 69.996|  0.000|   302|  5284.709| 19.999|  57,146|
| |Mineral County|     4| 148.876|  0.000|   127|  4726.813| 58.487|  26,868|
| |Preston County|     4| 119.646|  0.000|   125|  3738.933|  8.546|  33,432|
| |Ohio County|     4| 96.593|  0.000|   272|  6568.303| 24.148|  41,411|
| |Grant County|     4| 345.781| 37.048|   131| 11324.343| 419.877|  11,568|
| |Greenbrier County|     3| 86.550|  0.000|    93|  2683.053| 20.607|  34,662|
| |Cabell County|     3| 32.628|  1.554|   431|  4687.585| 99.438|  91,945|
| |Marion County|     2| 35.668|  0.000|   195|  3477.672| 40.764|  56,072|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097|  8.981|  15,907|
| |Wyoming County|     2| 98.068|  7.005|    43|  2108.463| 98.068|  20,394|
| |Brooke County|     1| 45.581|  0.000|    70|  3190.665| 58.604|  21,939|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Nicholas County|     1| 40.823|  0.000|    40|  1632.920| 29.159|  24,496|
| |Taylor County|     1| 59.898|  0.000|    60|  3593.890| 34.228|  16,695|
| |Roane County|     1| 73.057|  0.000|    19|  1388.077| 52.183|  13,688|
| |Pleasants County|     1| 134.048| 19.150|    14|  1876.676| 76.599|   7,460|
| |Harrison County|     1| 14.869|  0.000|   238|  3538.718| 65.846|  67,256|
| |Hampshire County|     1| 43.150|  0.000|    84|  3624.595| 49.314|  23,175|
| |Mason County|     1| 37.713|  0.000|    67|  2526.776| 75.426|  26,516|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  9.358|  30,531|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Raleigh County|     1| 13.631|  0.000|   276|  3762.217| 128.523|  73,361|
| |Pendleton County|     1| 143.493|  0.000|    42|  6026.690|  0.000|   6,969|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Tucker County|     0|  0.000|  0.000|    11|  1608.422|  0.000|   6,839|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  5.909|  24,176|
| |Webster County|     0|  0.000|  0.000|     4|   492.975|  0.000|   8,114|
| |Wetzel County|     0|  0.000|  0.000|    44|  2920.677| 28.448|  15,065|
| |Randolph County|     0|  0.000|  0.000|   212|  7388.047| 29.871|  28,695|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 24.793|  28,810|
| |Lincoln County|     0|  0.000|  0.000|    96|  4703.807| 118.995|  20,409|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |Morgan County|     0|  0.000|  0.000|    31|  1733.393| 39.940|  17,884|
| |Boone County|     0|  0.000|  0.000|   112|  5219.742| 113.183|  21,457|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Putnam County|     0|  0.000|  0.000|   204|  3613.818| 65.798|  56,450|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 33.257|   8,591|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |Hardy County|     0|  0.000|  0.000|    62|  4500.581| 51.850|  13,776|
| |McDowell County|     0|  0.000|  0.000|    64|  3631.412| 121.587|  17,624|
| |Summers County|     0|  0.000|  0.000|    16|  1272.568| 102.260|  12,573|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 16.910|   8,448|
| |Gilmer County|     0|  0.000|  0.000|    17|  2173.079| 18.261|   7,823|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   148| 167.296| N/A| 9,897| 11187.361| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  2.219| 4,521| 23408.618| 142.018| 193,134|
| |Pennington County|    32| 281.257|  1.256|   915|  8042.189| 65.292| 113,775|
| |Beadle County|     9| 487.726|  0.000|   596| 32298.271| 69.675|  18,453|
| |Todd County|     5| 491.304| 14.037|    74|  7271.298| 98.261|  10,177|
| |Union County|     4| 251.067|  0.000|   220| 13808.687| 107.600|  15,932|
| |Brown County|     3| 77.242|  0.000|   456| 11740.776| 125.058|  38,839|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556|  0.000|   1,962|
| |Hughes County|     3| 171.174|  8.151|    93|  5306.402| 40.756|  17,526|
| |Lyman County|     3| 793.441| 37.783|    91| 24067.707| 113.349|   3,781|
| |Lincoln County|     2| 32.718|  0.000|   672| 10993.325| 163.591|  61,128|
| |Lake County|     2| 156.287|  0.000|   100|  7814.331| 122.797|  12,797|
| |Oglala Lakota County|     2| 141.074|  0.000|   157| 11074.275| 50.383|  14,177|
| |Yankton County|     2| 87.665|  0.000|   128|  5610.590| 150.284|  22,814|
| |Meade County|     1| 35.296|  0.000|    98|  3458.986| 80.676|  28,332|
| |Roberts County|     1| 96.209|  0.000|    80|  7696.748| 96.209|  10,394|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474|  0.000|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |McCook County|     1| 179.019|  0.000|    30|  5370.569| 102.297|   5,586|
| |Codington County|     1| 35.703|  0.000|   147|  5248.313| 117.309|  28,009|
| |Butte County|     1| 95.886|  0.000|    18|  1725.956| 54.792|  10,429|
| |Brookings County|     1| 28.509|  0.000|   143|  4076.745| 65.163|  35,077|
| |Davison County|     1| 50.569|  0.000|    99|  5006.321| 36.121|  19,775|
| |Faulk County|     1| 434.972|  0.000|    29| 12614.180| 186.416|   2,299|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Grant County|     0|  0.000|  0.000|    28|  3970.505| 81.031|   7,052|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 42.561|   6,713|
| |Edmunds County|     0|  0.000|  0.000|    18|  4700.966| 186.546|   3,829|
| |Douglas County|     0|  0.000|  0.000|    19|  6504.622| 146.721|   2,921|
| |Dewey County|     0|  0.000|  0.000|    49|  8316.361|  0.000|   5,892|
| |Marshall County|     0|  0.000|  0.000|    12|  2431.611| 115.791|   4,935|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 1295.874|   2,756|
| |Turner County|     0|  0.000|  0.000|    56|  6679.389| 119.275|   8,384|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180|  0.000|   6,576|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Spink County|     0|  0.000|  0.000|    26|  4077.792| 89.622|   6,376|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    25|  4055.808| 208.584|   6,164|
| |Hand County|     0|  0.000|  0.000|    10|  3133.814| 134.306|   3,191|
| |Hanson County|     0|  0.000|  0.000|    22|  6371.271| 41.372|   3,453|
| |Day County|     0|  0.000|  0.000|    24|  4424.779| 79.014|   5,424|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757|  0.000|   2,379|
| |Lawrence County|     0|  0.000|  0.000|    62|  2399.009| 121.609|  25,844|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582|  0.000|   4,939|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     4|  3074.558| 109.806|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    29|  3977.507| 39.187|   7,291|
| |Harding County|     0|  0.000|  0.000|     2|  1540.832| 220.119|   1,298|
| |Potter County|     0|  0.000|  0.000|     2|   928.936| 66.353|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Deuel County|     0|  0.000|  0.000|    13|  2987.819| 131.333|   4,351|
| |Charles Mix County|     0|  0.000|  0.000|   103| 11084.804| 46.123|   9,292|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233|  0.000|   1,376|
| |Brule County|     0|  0.000|  0.000|    46|  8684.161| 26.969|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    14|  2028.691| 20.701|   6,901|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Clay County|     0|  0.000|  0.000|   135|  9594.883| 121.840|  14,070|
| |Clark County|     0|  0.000|  0.000|    17|  4550.321| 38.238|   3,736|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159|  0.000|   2,751|
| |Custer County|     0|  0.000|  0.000|    36|  4012.483| 159.226|   8,972|
| |Corson County|     0|  0.000|  0.000|    37|  9055.311| 244.738|   4,086|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   126| 93.735| N/A| 4,088|  3041.187| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,103|  7128.741| 15.980| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    13| 62.608|  0.688|   680|  3274.883|  9.632| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   171|  1398.178|  2.336| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   570|  5264.276| 29.026| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   156|  1025.317|  3.756| 152,148|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Somerset County|     1| 19.808|  0.000|    35|   693.289|  5.660|  50,484|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  0.000|  67,055|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  0.000|  39,772|
| |Hancock County|     1| 18.186|  0.000|    40|   727.445| 12.990|  54,987|
| |Oxford County|     0|  0.000|  0.000|    55|   948.685|  2.464|  57,975|
| |Washington County|     0|  0.000|  0.000|    13|   414.290|  4.553|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    57|  1589.692| 11.953|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|     6|   357.462| 25.533|  16,785|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   120| 157.468| N/A| 8,150| 10694.668| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,088| 16974.214| 87.164| 181,923|
| |Burleigh County|     8| 83.659|  4.482| 1,294| 13531.885| 316.710|  95,626|
| |Grand Forks County|     7| 100.790|  2.057|   728| 10482.210| 146.043|  69,451|
| |Stark County|     5| 158.786|  9.073|   349| 11083.235| 544.408|  31,489|
| |Morton County|     4| 127.535|  4.555|   425| 13550.568| 505.584|  31,364|
| |Stutsman County|     3| 144.900|  6.900|   127|  6134.080| 13.800|  20,704|
| |Ramsey County|     2| 173.626|  0.000|    80|  6945.047| 186.028|  11,519|
| |Williams County|     2| 53.207|  0.000|   293|  7794.834| 163.422|  37,589|
| |McKenzie County|     2| 133.120|  9.509|    91|  6056.976| 57.052|  15,024|
| |McIntosh County|     2| 800.961|  0.000|    41| 16419.704| 800.961|   2,497|
| |Benson County|     2| 292.740| 20.910|   157| 22980.094| 543.660|   6,832|
| |Richland County|     1| 61.816|  8.831|   114|  7047.042| 114.801|  16,177|
| |Emmons County|     1| 308.547|  0.000|    18|  5553.841| 44.078|   3,241|
| |Griggs County|     1| 448.229|  0.000|    37| 16584.491| 384.197|   2,231|
| |McHenry County|     1| 174.064|  0.000|    19|  3307.224| 74.599|   5,745|
| |Mountrail County|     1| 94.832|  0.000|   146| 13845.424| 311.590|  10,545|
| |Ward County|     1| 14.784|  0.000|   245|  3622.064| 86.592|  67,641|
| |Sioux County|     1| 236.407|  0.000|    91| 21513.002| 1046.944|   4,230|
| |Foster County|     0|  0.000|  0.000|    26|  8099.688| 133.511|   3,210|
| |Bowman County|     0|  0.000|  0.000|    11|  3637.566| 236.206|   3,024|
| |Golden Valley County|     0|  0.000|  0.000|     8|  4542.873| 324.491|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Kidder County|     0|  0.000|  0.000|    19|  7661.290| 345.622|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523|  0.000|   4,046|
| |Walsh County|     0|  0.000|  0.000|   107| 10055.446| 53.701|  10,641|
| |Dunn County|     0|  0.000|  0.000|    31|  7007.233| 32.291|   4,424|
| |Wells County|     0|  0.000|  0.000|    23|  5998.957| 74.521|   3,834|
| |Eddy County|     0|  0.000|  0.000|    20|  8745.081| 187.395|   2,287|
| |Divide County|     0|  0.000|  0.000|     4|  1766.784| 189.298|   2,264|
| |Dickey County|     0|  0.000|  0.000|    13|  2668.309| 29.322|   4,872|
| |McLean County|     0|  0.000|  0.000|    83|  8783.069| 559.335|   9,450|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000|  0.000|     3|  3232.759| 153.941|     928|
| |Barnes County|     0|  0.000|  0.000|    39|  3744.599| 27.433|  10,415|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784|  0.000|   1,850|
| |Mercer County|     0|  0.000|  0.000|    32|  3908.636| 139.594|   8,187|
| |Nelson County|     0|  0.000|  0.000|    26|  9030.914| 198.482|   2,879|
| |Traill County|     0|  0.000|  0.000|    58|  7217.521| 142.217|   8,036|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Steele County|     0|  0.000|  0.000|    15|  7936.508| 151.172|   1,890|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 325.910|   1,315|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    85|  5996.050| 372.864|  14,176|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641| 61.391|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Pierce County|     0|  0.000|  0.000|    15|  3773.585| 143.756|   3,975|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    81| 75.787| N/A| 5,407|  5059.049| N/A|1,068,778|
| |Yellowstone County|    32| 198.388|  3.543| 1,424|  8828.270| 206.359| 161,300|
| |Big Horn County|    14| 1051.130| 32.177|   477| 35813.500| 890.243|  13,319|
| |Toole County|     6| 1266.892|  0.000|    44|  9290.541| 120.656|   4,736|
| |Cascade County|     4| 49.161|  3.511|   170|  2089.325| 15.802|  81,366|
| |Flathead County|     3| 28.900|  1.376|   364|  3506.541| 86.700| 103,806|
| |Gallatin County|     3| 26.216|  0.000|   970|  8476.502| 77.400| 114,434|
| |Richland County|     2| 185.134|  0.000|    48|  4443.210| 13.224|  10,803|
| |Ravalli County|     2| 45.656|  3.261|    84|  1917.546| 32.611|  43,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 37.587|  11,402|
| |Lewis and Clark County|     2| 28.805|  2.058|   168|  2419.634| 34.978|  69,432|
| |Hill County|     2| 121.330| 17.333|    46|  2790.585| 43.332|  16,484|
| |Lincoln County|     2| 100.100|  0.000|    78|  3903.904| 35.750|  19,980|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972|  0.000|   3,737|
| |Missoula County|     1|  8.361|  1.194|   346|  2892.977| 57.334| 119,600|
| |Madison County|     1| 116.279|  0.000|    83|  9651.163| 66.445|   8,600|
| |Lake County|     1| 32.832|  0.000|   184|  6041.106| 37.522|  30,458|
| |Glacier County|     1| 72.711|  0.000|    82|  5962.335| 197.360|  13,753|
| |Rosebud County|     1| 111.894|  0.000|    58|  6489.874| 415.608|   8,937|
| |Stillwater County|     1| 103.713| 14.816|    29|  3007.675| 103.713|   9,642|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Roosevelt County|     0|  0.000|  0.000|    25|  2271.901| 51.929|  11,004|
| |Sanders County|     0|  0.000|  0.000|    11|   908.115| 23.587|  12,113|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 43.172|   3,309|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Silver Bow County|     0|  0.000|  0.000|   103|  2950.021| 114.564|  34,915|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    30|  4056.247| 309.047|   7,396|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 76.055|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Carbon County|     0|  0.000|  0.000|    75|  6993.007| 199.800|  10,725|
| |Broadwater County|     0|  0.000|  0.000|    14|  2244.669| 68.714|   6,237|
| |Blaine County|     0|  0.000|  0.000|    13|  1945.816| 64.148|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    68|  7193.484| 151.124|   9,453|
| |Granite County|     0|  0.000|  0.000|    18|  5327.020| 211.390|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fergus County|     0|  0.000|  0.000|    18|  1628.959| 116.354|  11,050|
| |Jefferson County|     0|  0.000|  0.000|    29|  2372.965| 23.379|  12,221|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Dawson County|     0|  0.000|  0.000|    27|  3134.796| 182.448|   8,613|
| |Deer Lodge County|     0|  0.000|  0.000|    26|  2844.639| 46.890|   9,140|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 24.168|   5,911|
| |Phillips County|     0|  0.000|  0.000|    78| 19726.859| 2637.474|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    60|  3613.152| 43.014|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529|  0.000|   4,633|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 171.703|   1,664|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,476|  2365.426| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   738|  4506.210| 13.084| 163,774|
| |Franklin County|     7| 141.695|  0.000|   118|  2388.567|  0.000|  49,402|
| |Windham County|     3| 71.053|  0.000|   104|  2463.171|  6.767|  42,222|
| |Addison County|     2| 54.382|  0.000|    74|  2012.127|  3.884|  36,777|
| |Washington County|     2| 34.241|  0.000|    57|   975.877|  9.783|  58,409|
| |Windsor County|     2| 36.323|  0.000|    73|  1325.778|  2.594|  55,062|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  0.000|  25,362|
| |Bennington County|     1| 28.193|  0.000|    91|  2565.548| 24.165|  35,470|
| |Rutland County|     1| 17.185|  0.000|   101|  1735.664|  9.820|  58,191|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Orange County|     0|  0.000|  0.000|    16|   553.787|  9.889|  28,892|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    39| 27.545| N/A| 4,289|  3029.229| N/A|1,415,872|
| |Honolulu County|    33| 33.861| N/A| 3,900|  4001.794| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   198|  1182.676| 15.359| 167,417|
| |Kauai County|     0|  0.000|  0.000|    52|   719.295|  9.880|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   139|   689.782| 11.343| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,119|  5389.117| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    25|  2960.332| 33.832|   8,445|
| |Natrona County|     0|  0.000|  0.000|   240|  3005.334| 21.467|  79,858|
| |Washakie County|     0|  0.000|  0.000|    86| 11018.578| 494.189|   7,805|
| |Sweetwater County|     0|  0.000|  0.000|   267|  6305.647| 47.233|  42,343|
| |Teton County|     0|  0.000|  0.000|   375| 15981.930| 48.707|  23,464|
| |Uinta County|     0|  0.000|  0.000|   278| 13744.685| 42.378|  20,226|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762| 29.063|   9,831|
| |Park County|     0|  0.000|  0.000|   139|  4761.252| 53.827|  29,194|
| |Platte County|     0|  0.000|  0.000|     6|   714.881| 17.021|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    74|  2427.423| 28.117|  30,485|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Goshen County|     0|  0.000|  0.000|    36|  2725.002| 140.575|  13,211|
| |Fremont County|     0|  0.000|  0.000|   500| 12735.284|  7.277|  39,261|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 129.488|   4,413|
| |Laramie County|     0|  0.000|  0.000|   509|  5115.578| 24.408|  99,500|
| |Carbon County|     0|  0.000|  0.000|   105|  7094.595| 164.093|  14,800|
| |Lincoln County|     0|  0.000|  0.000|   101|  5093.293|  0.000|  19,830|
| |Converse County|     0|  0.000|  0.000|    32|  2315.150|  0.000|  13,822|
| |Campbell County|     0|  0.000|  0.000|   139|  2999.504| 64.737|  46,341|
| |Albany County|     0|  0.000|  0.000|    90|  2314.815|  7.349|  38,880|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565|  0.000|   7,584|
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
|RI|5 counties|     0|  0.000| N/A|18,536| 17497.340| N/A|1,059,361|
| |Bristol County|     0|  0.000|  0.000|   322|  6642.051| 17.681|  48,479|
| |Washington County|     0|  0.000|  0.000|   621|  4945.173| 15.926| 125,577|
| |Providence County|     0|  0.000|  0.000|15,644| 24484.647| 133.482| 638,931|
| |Newport County|     0|  0.000|  0.000|   405|  4934.090| 15.664|  82,082|
| |Kent County|     0|  0.000|  0.000| 1,544|  9397.901| 43.477| 164,292|


