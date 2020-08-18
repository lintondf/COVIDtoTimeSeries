# Analysis of US By County #

Updated: at 2020-08-18

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 136,392 deaths (472.498 deaths/million) and 4,671,077 confirmed cases (16181.819 confirmed cases/million).  This group accounts for 81.21% of all US deaths and for 87.44% of all US cases.

24.31% of this group's deaths (19.75% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.17% of this group's deaths (20.44% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,435 (12.66% of the total US population):



The next 25.44% of this group's deaths (20.66% of the total US deaths) occured in 93 counties in 31 states with a combined population of 71,506,932 (21.78% of the total US population)

The remaining 25.08% of this group's deaths (20.37% of the total US deaths) occured in 850 counties in 50 states with a combined population of 138,299,474 (42.13% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 11,051 deaths (279.225 deaths/million) and 500,323 confirmed cases (12641.613 confirmed cases/million).  This group accounts for 6.58% of all US deaths and for 9.37% of all US cases.

24.72% of this group's deaths (1.63% of the total US deaths) occured in 61 counties in 16 states with a combined population of 2,075,887 (0.63% of the total US population):



The next 25.22% of this group's deaths (1.66% of the total US deaths) occured in 120 counties in 28 states with a combined population of 3,537,853 (1.08% of the total US population):



The next 25.03% of this group's deaths (1.65% of the total US deaths) occured in 239 counties in 33 states with a combined population of 5,741,942 (1.75% of the total US population)

The remaining 25.03% of this group's deaths (1.65% of the total US deaths) occured in 1,732 counties in 47 states with a combined population of 28,221,782 (8.60% of the total US population) 

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
|NJ|21 counties|15,916| 1791.900| N/A|187,341| 21091.758| N/A|8,882,190|
| |Essex County| 2,111| 2642.135|  0.000|19,938| 24954.473| 34.151| 798,975|
| |Bergen County| 2,036| 2184.076|  0.000|21,277| 22824.452| 69.268| 932,202|
| |Hudson County| 1,508| 2242.743|  0.637|19,911| 29612.235| 48.441| 672,391|
| |Middlesex County| 1,415| 1715.023|  2.078|18,119| 21960.774| 32.379| 825,062|
| |Union County| 1,350| 2426.569|  0.000|16,879| 30339.306| 39.544| 556,341|
| |Passaic County| 1,244| 2478.947|  0.569|17,963| 35795.276| 84.833| 501,826|
| |Ocean County| 1,020| 1679.881|  0.471|10,763| 17726.035| 37.644| 607,186|
| |Monmouth County|   858| 1386.566|  0.462|10,496| 16961.999| 39.247| 618,795|
| |Morris County|   830| 1687.524|  0.290| 7,350| 14943.732| 25.850| 491,845|
| |Mercer County|   622| 1692.839|  0.778| 8,199| 22314.454| 27.994| 367,430|
| |Camden County|   583| 1151.102|  0.846| 8,820| 17414.620| 67.695| 506,471|
| |Somerset County|   566| 1720.710|  2.172| 5,317| 16164.337| 27.795| 328,934|
| |Burlington County|   477| 1071.070|  1.283| 6,159| 13829.603| 42.984| 445,349|
| |Atlantic County|   253| 959.533|  0.542| 3,602| 13661.016| 72.060| 263,670|
| |Gloucester County|   215| 737.220|  1.470| 3,445| 11812.671| 91.601| 291,636|
| |Sussex County|   198| 1409.373|  0.000| 1,353|  9630.716| 20.337| 140,488|
| |Warren County|   172| 1633.940|  0.000| 1,368| 12995.526| 31.213| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,438| 22992.503| 85.985| 149,527|
| |Hunterdon County|   124| 997.017|  0.000| 1,163|  9351.055| 16.081| 124,371|
| |Cape May County|    89| 966.981|  3.104|   848|  9213.486| 21.730|  92,039|
| |Salem County|    87| 1394.566|  0.000|   933| 14955.518| 80.147|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,344| 634.551| N/A|255,480| 13132.827| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.000|43,955| 32393.119| 27.899|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.000|44,185| 29923.453| 32.991|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.000|36,486| 37711.394| 37.357| 967,506|
| |Queens County|   986| 437.635|  0.958| 7,959|  3531.366| 20.079|2,253,858|
| |Kings County|   932| 364.145|  0.797| 1,366|   533.605|  3.034|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|14,011| 43006.363| 27.187| 325,789|
| |Erie County|   674| 733.644|  0.466| 9,157|  9967.323| 37.164| 918,702|
| |Bronx County|   650| 458.527|  1.004|27,105| 19112.320| 108.672|1,418,207|
| |Orange County|   491| 1275.523|  0.000|11,256| 29240.921| 32.658| 384,940|
| |New York County|   415| 254.883|  0.558|15,633|  9598.208| 54.575|1,628,706|
| |Monroe County|   285| 384.216|  0.000| 5,183|  6987.341| 39.866| 741,770|
| |Onondaga County|   203| 440.798|  0.931| 3,680|  7990.828| 29.469| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,700| 15974.549| 42.243| 294,218|
| |Richmond County|   148| 311.502|  0.682| 7,959| 16715.983| 95.047| 476,143|
| |Albany County|   129| 422.250|  0.468| 2,657|  8697.047| 26.654| 305,506|
| |Oneida County|   117| 511.652|  1.249| 2,201|  9625.182| 31.861| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,532|  7320.301| 21.843| 209,281|
| |Ulster County|    92| 518.097|  0.000| 2,098| 11814.859| 20.917| 177,573|
| |Broome County|    69| 362.228|  0.000| 1,172|  6152.619| 30.748| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,463| 14879.984| 20.342|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   302|  7484.140| 14.161|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,493| 19792.661|  7.575|  75,432|
| |Steuben County|    42| 440.349|  0.000|   307|  3218.738| 13.480|  95,379|
| |Rensselaer County|    38| 239.424|  7.201|   795|  5009.010| 26.103| 158,714|
| |Schenectady County|    37| 238.250|  0.000| 1,121|  7218.334| 56.113| 155,299|
| |Columbia County|    37| 622.257|  0.000|   552|  9283.396| 26.428|  59,461|
| |Ontario County|    34| 309.719|  0.000|   369|  3361.360| 10.411| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269|  0.000|  63,944|
| |Tioga County|    25| 518.640|  0.000|   196|  4066.137|  8.891|  48,203|
| |Fulton County|    24| 449.581|  0.000|   303|  5675.964| 16.056|  53,383|
| |Greene County|    18| 381.453|  0.000|   298|  6315.165| 15.137|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   795|  3458.582| 21.752| 229,863|
| |Madison County|    17| 239.636|  0.000|   421|  5934.509| 18.124|  70,941|
| |Washington County|    14| 228.743|  0.000|   261|  4264.427|  2.334|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   265|  2088.209|  9.006| 126,903|
| |Livingston County|     8| 127.158|  0.000|   178|  2829.259|  4.541|  62,914|
| |Yates County|     7| 280.978|  0.000|    59|  2368.241| 11.468|  24,913|
| |Cattaraugus County|     6| 78.826|  0.000|   171|  2246.542|  9.384|  76,117|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959|  6.052|  47,207|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436|  0.000|  39,859|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  4.802|  59,493|
| |Genesee County|     5| 87.291|  0.000|   285|  4975.559| 19.952|  57,280|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  0.000| 107,740|
| |Delaware County|     4| 90.631|  0.000|   107|  2424.380|  6.474|  44,135|
| |Clinton County|     4| 49.699|  0.000|   133|  1652.482|  8.875|  80,485|
| |Herkimer County|     4| 65.233|  0.000|   284|  4631.517| 23.297|  61,319|
| |Montgomery County|     4| 81.266|  0.000|   188|  3819.508| 31.926|  49,221|
| |Wayne County|     3| 33.364|  0.000|   269|  2991.615| 27.009|  89,918|
| |Oswego County|     3| 25.614|  0.000|   272|  2322.325| 23.174| 117,124|
| |Chemung County|     3| 35.947|  0.000|   190|  2276.649| 30.812|  83,456|
| |Seneca County|     3| 88.194|  0.000|    94|  2763.405| 16.799|  34,016|
| |Cayuga County|     2| 26.118|  0.000|   164|  2141.663| 22.387|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697|  0.000|  46,091|
| |Lewis County|     0|  0.000|  0.000|    47|  1787.344| 32.596|  26,296|
| |Jefferson County|     0|  0.000|  0.000|   143|  1301.965|  1.301| 109,834|
| |Hamilton County|     0|  0.000|  0.000|    11|  2490.942| 97.050|   4,416|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525|  0.000|  50,022|
| |Essex County|     0|  0.000|  0.000|    59|  1599.566| 15.492|  36,885|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  0.000|  30,999|
| |Cortland County|     0|  0.000|  0.000|    97|  2038.629|  6.005|  47,581|
| |Schuyler County|     0|  0.000|  0.000|    23|  1291.627|  8.023|  17,807|
| |Tompkins County|     0|  0.000|  0.000|   238|  2329.223|  5.592| 102,180|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|11,296| 285.886| N/A|629,415| 15929.628| N/A|39,512,223|
| |Los Angeles County| 5,273| 525.246|  3.913|223,230| 22236.042| 180.537|10,039,107|
| |Riverside County|   881| 356.601|  3.527|45,662| 18482.554| 212.735|2,470,546|
| |Orange County|   810| 255.063|  3.779|43,925| 13831.631| 152.858|3,175,692|
| |San Diego County|   626| 187.519|  1.369|34,678| 10387.829| 72.876|3,338,330|
| |San Bernardino County|   568| 260.540|  1.442|41,564| 19065.312| 359.881|2,180,085|
| |San Joaquin County|   269| 352.950|  8.622|15,008| 19691.713| 401.872| 762,148|
| |Imperial County|   257| 1418.205| 10.248|10,145| 55983.224| 356.325| 181,215|
| |Alameda County|   221| 132.230|  1.026|15,123|  9048.488| 127.529|1,671,329|
| |Sacramento County|   218| 140.459|  3.774|14,326|  9230.325| 210.412|1,552,058|
| |Santa Clara County|   209| 108.411|  0.296|14,429|  7484.496| 128.566|1,927,852|
| |Tulare County|   206| 441.875|  3.064|12,451| 26707.708| 486.921| 466,195|
| |Kern County|   204| 226.616|  5.237|26,788| 29757.765| 372.615| 900,202|
| |Fresno County|   203| 203.183|  4.576|19,900| 19917.906| 293.693| 999,101|
| |Stanislaus County|   198| 359.569|  7.523|12,541| 22774.489| 590.720| 550,660|
| |Contra Costa County|   157| 136.104|  2.229|11,408|  9889.677| 248.183|1,153,526|
| |San Mateo County|   126| 164.368|  1.118| 7,150|  9327.227| 155.050| 766,573|
| |Ventura County|    95| 112.292|  0.507| 9,090| 10744.605| 77.000| 846,006|
| |Merced County|    89| 320.513|  9.775| 6,777| 24405.791| 535.560| 277,680|
| |Marin County|    82| 316.815|  0.552| 5,774| 22308.423| 204.219| 258,826|
| |Santa Barbara County|    77| 172.453|  2.560| 7,274| 16291.190| 182.371| 446,499|
| |San Francisco County|    69| 78.271| N/A| 8,346|  9467.426| N/A| 881,549|
| |Kings County|    66| 431.542|  9.341| 5,514| 36053.354| 991.052| 152,940|
| |Sonoma County|    57| 115.306|  2.890| 4,377|  8854.302| 204.314| 494,336|
| |Madera County|    47| 298.741|  7.264| 2,924| 18585.494| 418.600| 157,327|
| |Monterey County|    46| 105.976|  3.620| 6,548| 15085.437| 362.688| 434,061|
| |Yolo County|    46| 208.617|  1.296| 2,046|  9278.912| 137.350| 220,500|
| |Solano County|    41| 91.591|  0.000| 4,596| 10267.110| 102.760| 447,643|
| |Placer County|    28| 70.294|  2.152| 2,625|  6590.030| 109.744| 398,329|
| |San Luis Obispo County|    19| 67.111|  1.514| 2,562|  9049.454| 155.416| 283,111|
| |Napa County|    13| 94.378|  2.074| 1,245|  9038.506| 177.348| 137,744|
| |Butte County|    12| 54.748|  2.607| 1,370|  6250.399| 86.033| 219,186|
| |Amador County|    11| 276.716| 32.343|   210|  5282.753| 100.624|  39,752|
| |Shasta County|    10| 55.531|  0.000|   488|  2709.907| 23.006| 180,080|
| |Mendocino County|    10| 115.275|  0.000|   541|  6236.383| 113.628|  86,749|
| |Sutter County|     7| 72.187|  0.000| 1,137| 11725.155| 272.541|  96,971|
| |Santa Cruz County|     7| 25.621|  0.523| 1,454|  5321.855| 110.327| 273,213|
| |Inyo County|     5| 277.177| 15.839|   127|  7040.302| 166.306|  18,039|
| |Colusa County|     5| 232.051|  6.630|   415| 19260.222| 159.121|  21,547|
| |Yuba County|     4| 50.847|  0.000|   758|  9635.430| 203.386|  78,668|
| |San Benito County|     4| 63.686|  0.000|   836| 13310.406| 161.490|  62,808|
| |Humboldt County|     4| 29.508|  0.000|   309|  2279.467| 24.238| 135,558|
| |Glenn County|     3| 105.660|  0.000|   413| 14545.839| 266.665|  28,393|
| |Nevada County|     2| 20.049|  1.432|   373|  3739.161| 22.913|  99,755|
| |Mariposa County|     2| 116.259|  0.000|    64|  3720.281| 16.608|  17,203|
| |Lake County|     2| 31.063|  0.000|   272|  4224.521| 71.000|  64,386|
| |El Dorado County|     2| 10.371|  0.000|   827|  4288.463| 53.337| 192,843|
| |Tuolumne County|     2| 36.712|  0.000|   160|  2936.965| 13.111|  54,478|
| |Calaveras County|     1| 21.784|  0.000|   174|  3790.437| 84.024|  45,905|
| |Tehama County|     1| 15.365|  0.000|   318|  4885.993| 92.189|  65,084|
| |Mono County|     1| 69.233|  0.000|   161| 11146.497| 29.671|  14,444|
| |Trinity County|     0|  0.000|  0.000|     8|   651.201| 34.886|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   113|  2595.374| 36.092|  43,539|
| |Sierra County|     0|  0.000|  0.000|     6|  1996.672| 95.080|   3,005|
| |Plumas County|     0|  0.000|  0.000|    39|  2073.696| 22.788|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547|  0.000|   8,841|
| |Lassen County|     0|  0.000|  0.000|   703| 22994.145| 93.453|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   106|  3811.304| 30.819|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties|10,447| 360.293| N/A|561,110| 19351.369| N/A|28,995,881|
| |Harris County| 1,838| 389.958|  7.729|92,944| 19719.413| 193.403|4,713,325|
| |Hidalgo County|   955| 1099.335| 20.720|22,013| 25339.959| 306.696| 868,707|
| |Bexar County|   892| 445.209|  7.701|44,122| 22021.867| 82.924|2,003,554|
| |Dallas County|   829| 314.549|  3.957|65,278| 24768.584| 543.293|2,635,516|
| |Cameron County|   565| 1335.183| 45.575|18,005| 42548.616| 477.695| 423,163|
| |Tarrant County|   504| 239.713|  3.737|35,997| 17120.924| 259.553|2,102,515|
| |El Paso County|   361| 430.152| 10.384|18,486| 22027.125| 355.765| 839,238|
| |Travis County|   335| 262.961|  3.588|24,409| 19160.032| 163.271|1,273,954|
| |Nueces County|   290| 800.455| 18.533|17,124| 47265.481| 670.726| 362,294|
| |Webb County|   202| 730.159| 14.459| 9,646| 34866.909| 714.668| 276,652|
| |Fort Bend County|   194| 239.008|  5.632|12,623| 15551.542| 457.952| 811,688|
| |Galveston County|   125| 365.349|  5.010|10,033| 29324.339| 216.704| 342,139|
| |Brazoria County|   111| 296.582|  6.871| 8,233| 21997.841| 287.040| 374,264|
| |Denton County|   105| 118.349|  2.737| 8,427|  9498.347| 109.815| 887,207|
| |Montgomery County|   103| 169.578|  3.058| 7,160| 11788.123| 119.010| 607,391|
| |Williamson County|   103| 174.413|  2.419| 7,482| 12669.524| 142.482| 590,551|
| |Collin County|   100| 96.644|  1.381|10,169|  9827.685| 322.513|1,034,730|
| |Jefferson County|    95| 377.636|  6.247| 6,247| 24832.548| 208.410| 251,565|
| |Starr County|    94| 1454.365| 57.467| 2,443| 37798.029| 508.365|  64,633|
| |Lubbock County|    80| 257.592|  3.220| 6,542| 21064.562| 222.173| 310,569|
| |Comal County|    80| 512.134|  9.145| 2,132| 13648.381| 267.956| 156,209|
| |McLennan County|    62| 241.600|  3.897| 5,356| 20871.083| 214.879| 256,623|
| |Midland County|    60| 339.305|  8.887| 2,948| 16671.191| 219.740| 176,832|
| |Ector County|    60| 360.961|  4.297| 3,814| 22945.080| 195.091| 166,223|
| |Guadalupe County|    59| 353.617|  3.425| 1,799| 10782.334| 102.746| 166,847|
| |Victoria County|    57| 619.000| 23.271| 3,584| 38920.985| 210.987|  92,084|
| |Angelina County|    54| 622.730| 14.827| 1,906| 21980.050| 181.218|  86,715|
| |Maverick County|    54| 919.587| 26.760| 2,596| 44208.304| 669.012|  58,722|
| |Ellis County|    51| 275.935|  6.956| 3,255| 17611.159| 309.171| 184,826|
| |Brazos County|    51| 222.502|  1.247| 4,192| 18288.826| 76.660| 229,211|
| |Bell County|    49| 135.014|  4.330| 4,281| 11795.858| 177.133| 362,924|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401|  0.000|  49,025|
| |Potter County|    47| 400.290|  2.433| 3,823| 32559.724| 163.036| 117,415|
| |Hays County|    46| 199.834|  4.344| 5,150| 22372.725| 62.060| 230,191|
| |Walker County|    44| 602.979|  5.873| 3,190| 43715.997| 272.124|  72,971|
| |Nacogdoches County|    43| 659.469|  2.191| 1,204| 18465.125| 122.692|  65,204|
| |Washington County|    41| 1142.634|  7.963|   526| 14659.161| 43.794|  35,882|
| |Bowie County|    39| 418.253| 10.724|   791|  8483.029| 41.366|  93,245|
| |Liberty County|    36| 408.075|  3.239| 1,115| 12639.001| 207.276|  88,219|
| |Matagorda County|    35| 955.162| 31.189|   832| 22705.565| 311.890|  36,643|
| |San Patricio County|    35| 524.502| 19.267| 1,114| 16694.141| 383.207|  66,730|
| |Tom Green County|    34| 285.235|  9.588| 2,923| 24521.812| 302.013| 119,200|
| |Smith County|    34| 146.079|  6.752| 2,750| 11815.202| 138.714| 232,751|
| |Johnson County|    34| 193.383|  3.250| 2,159| 12279.814| 242.135| 175,817|
| |Medina County|    32| 620.347| 16.616|   987| 19133.840| 301.865|  51,584|
| |Kaufman County|    32| 235.028|  7.345| 2,446| 17964.951| 302.179| 136,154|
| |Gregg County|    32| 258.179|  5.763| 1,646| 13280.084| 265.095| 123,945|
| |Hale County|    31| 927.977| 21.382| 1,478| 44243.549| 825.344|  33,406|
| |Wharton County|    30| 721.917| 17.189| 1,020| 24545.192| 890.365|  41,556|
| |Willacy County|    30| 1404.626|  0.000|   774| 36239.348| 501.652|  21,358|
| |Taylor County|    29| 210.093|  6.210| 1,158|  8389.237| 28.978| 138,034|
| |Orange County|    29| 347.739| 15.417| 1,579| 18933.762| 174.726|  83,396|
| |Caldwell County|    29| 664.163|  9.815| 1,183| 27093.258| 111.239|  43,664|
| |Grimes County|    27| 934.903| 19.786|   933| 32306.094| 262.169|  28,880|
| |Lavaca County|    25| 1240.449| 56.706|   641| 31805.101| 99.236|  20,154|
| |Randall County|    25| 181.537|  4.149| 1,899| 13789.548| 180.500| 137,713|
| |Harrison County|    24| 360.615|  2.147|   735| 11043.830| 90.154|  66,553|
| |Bastrop County|    23| 259.234|  3.220| 1,452| 16365.542| 140.083|  88,723|
| |DeWitt County|    21| 1041.667| 14.172|   745| 36954.365| 368.481|  20,160|
| |Hunt County|    21| 212.995|  0.000| 1,284| 13023.105| 147.792|  98,594|
| |Wilson County|    20| 391.619|  2.797|   499|  9770.903| 167.837|  51,070|
| |Parker County|    20| 139.980|  1.000| 1,401|  9805.568| 175.974| 142,878|
| |Atascosa County|    19| 371.435|  2.793|   517| 10106.934| 223.419|  51,153|
| |Lamar County|    19| 381.075|  2.865|   730| 14641.288| 237.813|  49,859|
| |Jim Wells County|    19| 469.344| 14.116|   841| 20774.665| 412.882|  40,482|
| |Panola County|    18| 776.063|  0.000|   301| 12977.494| 55.433|  23,194|
| |Brown County|    18| 475.386|  7.546|   408| 10775.407| 64.139|  37,864|
| |Shelby County|    18| 712.194|  0.000|   411| 16261.771| 56.523|  25,274|
| |Kleberg County|    18| 586.701| 46.564|   498| 16232.073| 260.756|  30,680|
| |Hardin County|    18| 312.489|  7.440| 1,124| 19513.211| 374.491|  57,602|
| |Deaf Smith County|    18| 970.560|  7.703|   726| 39145.907| 454.468|  18,546|
| |Bee County|    17| 522.033| 26.321| 1,387| 42591.740| 789.630|  32,565|
| |Lamb County|    17| 1318.545| 66.481|   246| 19080.121| 221.604|  12,893|
| |Titus County|    17| 519.084|  8.724| 1,397| 42656.489| 471.101|  32,750|
| |Anderson County|    17| 294.449|  7.423| 2,434| 42158.136| 76.705|  57,735|
| |Aransas County|    16| 680.561|  6.076|   187|  7954.062| 60.764|  23,510|
| |Rockwall County|    16| 152.504|  4.085| 1,105| 10532.336| 284.584| 104,915|
| |Grayson County|    16| 117.464|  3.146| 1,272|  9338.384| 139.488| 136,212|
| |Jasper County|    15| 422.190| 16.083|   362| 10188.860| 233.210|  35,529|
| |Fayette County|    14| 552.355|  0.000|   408| 16097.215| 112.726|  25,346|
| |Moore County|    14| 668.577|  6.822| 1,082| 51671.442| 218.311|  20,940|
| |Polk County|    14| 272.623|  5.564|   769| 14974.782| 58.419|  51,353|
| |Hood County|    13| 210.892|  6.952|   657| 10658.144| 298.956|  61,643|
| |Red River County|    12| 998.087| 11.882|   141| 11727.522| 59.410|  12,023|
| |Henderson County|    12| 145.038|  0.000|   697|  8424.284| 96.692|  82,737|
| |Wichita County|    12| 90.751|  1.080| 1,117|  8447.402| 125.323| 132,230|
| |Uvalde County|    12| 448.749| 10.685|   604| 22587.039| 283.139|  26,741|
| |Lee County|    12| 696.096| 16.574|   181| 10499.449| 66.295|  17,239|
| |Jackson County|    11| 745.257| 38.715|   418| 28319.783| 116.144|  14,760|
| |San Augustine County|    11| 1335.438|  0.000|   178| 21609.809| 277.494|   8,237|
| |Navarro County|    11| 219.504|  8.552|   942| 18797.518| 245.160|  50,113|
| |Gonzales County|    11| 527.907| 13.712|   721| 34601.910| 260.526|  20,837|
| |Cherokee County|    11| 208.943| 10.854| 1,234| 23439.578| 312.057|  52,646|
| |Burnet County|    11| 228.429|  5.933|   577| 11982.141| 41.533|  48,155|
| |Palo Pinto County|    10| 342.595| 14.683|   347| 11888.040| 401.325|  29,189|
| |Wise County|    10| 142.890|  6.124|   536|  7658.893| 259.243|  69,984|
| |Karnes County|    10| 640.985| 36.628|   672| 43074.162| 302.178|  15,601|
| |Marion County|     9| 913.335| 14.497|   136| 13801.502| 43.492|   9,854|
| |Refugio County|     9| 1295.337| 102.805|   246| 35405.872| 411.218|   6,948|
| |Wood County|     9| 197.633|  6.274|   360|  7905.312| 138.029|  45,539|
| |Cass County|     9| 299.740|  4.758|   203|  6760.807| 128.460|  30,026|
| |Fannin County|     9| 253.421|  4.023|   321|  9038.689| 301.692|  35,514|
| |Houston County|     8| 348.311|  6.220|   323| 14063.044| 55.979|  22,968|
| |Van Zandt County|     8| 141.368| 12.622|   446|  7881.251| 179.234|  56,590|
| |San Jacinto County|     8| 277.210|  0.000|   187|  6479.781| 49.502|  28,859|
| |Erath County|     7| 163.942|  6.692|   580| 13583.774| 177.325|  42,698|
| |Calhoun County|     7| 328.793| 13.420|   555| 26068.577| 73.811|  21,290|
| |Hill County|     7| 191.001|  0.000|   341|  9304.483| 50.674|  36,649|
| |Parmer County|     7| 728.787|  0.000|   360| 37480.479| 297.464|   9,605|
| |Howard County|     7| 190.923|  3.896|   201|  5482.217| 109.099|  36,664|
| |Duval County|     7| 627.409| 12.804|   198| 17746.706| 268.889|  11,157|
| |Andrews County|     7| 374.231|  0.000|   338| 18070.035| 259.671|  18,705|
| |Coryell County|     6| 78.998|  1.881|   727|  9571.961| 109.093|  75,951|
| |Sabine County|     6| 569.152|  0.000|    66|  6260.672| 203.269|  10,542|
| |Frio County|     6| 295.479|  7.035|   571| 28119.768| 415.078|  20,306|
| |Gillespie County|     6| 222.321|  0.000|   188|  6966.059| 68.814|  26,988|
| |Brooks County|     6| 845.904| 60.422|   148| 20865.642| 704.920|   7,093|
| |Burleson County|     6| 325.327|  0.000|   251| 13609.500| 69.713|  18,443|
| |Kerr County|     6| 114.068|  0.000|   416|  7908.745| 48.886|  52,600|
| |Floyd County|     6| 1050.420|  0.000|    94| 16456.583| 125.050|   5,712|
| |Dallam County|     6| 823.384| 19.604|   196| 26897.214| 117.626|   7,287|
| |Goliad County|     6| 783.494| 37.309|   119| 15539.305| 559.639|   7,658|
| |Young County|     6| 333.148|  7.932|   200| 11104.942| 245.895|  18,010|
| |Camp County|     6| 458.225|  0.000|   253| 19321.827| 218.202|  13,094|
| |Zavala County|     6| 506.757| 12.066|   243| 20523.649| 398.166|  11,840|
| |Waller County|     5| 90.504|  0.000|   526|  9521.051| 186.180|  55,246|
| |Knox County|     5| 1364.629| 155.958|    62| 16921.397| 77.979|   3,664|
| |Lampasas County|     5| 233.340| 13.334|   131|  6113.496| 180.005|  21,428|
| |Dawson County|     5| 392.835| 11.224|   172| 13513.514| 303.044|  12,728|
| |Reeves County|     5| 312.969|  0.000|   152|  9514.271| 53.652|  15,976|
| |Martin County|     5| 866.401|  0.000|    67| 11609.773| 297.052|   5,771|
| |Chambers County|     5| 114.059|  6.518| 1,028| 23450.510| 250.930|  43,837|
| |Live Oak County|     5| 409.601| 35.109|   240| 19660.850| 117.029|  12,207|
| |Hockley County|     5| 217.193|  6.206|   223|  9686.808| 105.494|  23,021|
| |Blanco County|     5| 419.076|  0.000|   126| 10560.724| 335.261|  11,931|
| |Kendall County|     4| 84.333|  0.000|   180|  3794.986| 66.262|  47,431|
| |Gaines County|     4| 186.116|  6.647|   199|  9259.259| 252.586|  21,492|
| |Dimmit County|     4| 395.101| 14.111|   164| 16199.131| 197.550|  10,124|
| |Castro County|     4| 531.208|  0.000|   209| 27755.644| 170.746|   7,530|
| |Crockett County|     4| 1154.734| 41.241|   157| 45323.326| 82.481|   3,464|
| |Austin County|     4| 133.191|  0.000|   332| 11054.875| 394.817|  30,032|
| |Bailey County|     4| 571.429|  0.000|   187| 26714.286| 326.531|   7,000|
| |Reagan County|     4| 1039.231| 37.115|    66| 17147.311| 111.346|   3,849|
| |Presidio County|     4| 596.659| 42.618|    49|  7309.069| 63.928|   6,704|
| |Newton County|     4| 294.226|  0.000|   124|  9121.000| 325.750|  13,595|
| |Trinity County|     4| 273.019|  0.000|   163| 11125.520| 68.255|  14,651|
| |Lynn County|     4| 672.156|  0.000|    74| 12434.885| 168.039|   5,951|
| |Franklin County|     3| 279.720| 13.320|    98|  9137.529| 79.920|  10,725|
| |Garza County|     3| 481.618|  0.000|   101| 16214.481| 45.868|   6,229|
| |Zapata County|     3| 211.581| 10.075|   204| 14387.474| 302.258|  14,179|
| |Swisher County|     3| 405.570| 19.313|    83| 11220.765| 57.939|   7,397|
| |Hopkins County|     3| 80.897|  3.852|   217|  5851.580| 61.636|  37,084|
| |Yoakum County|     3| 344.313|  0.000|   124| 14231.608| 360.709|   8,713|
| |Falls County|     3| 173.440|  0.000|   145|  8382.957| 140.404|  17,297|
| |Stephens County|     3| 320.307|  0.000|   131| 13986.761| 1357.494|   9,366|
| |Leon County|     3| 172.374|  8.208|   158|  9078.373| 114.916|  17,404|
| |Robertson County|     3| 175.706|  8.367|   239| 13997.892| 41.835|  17,074|
| |Cooke County|     3| 72.715|  0.000|   265|  6423.152| 145.430|  41,257|
| |Limestone County|     3| 128.003|  0.000|   308| 13141.614| 408.390|  23,437|
| |Hamilton County|     3| 354.568|  0.000|    92| 10873.419| 151.958|   8,461|
| |Callahan County|     3| 215.162|  0.000|    52|  3729.470| 61.475|  13,943|
| |Real County|     3| 869.061| 82.768|    91| 26361.530| 165.536|   3,452|
| |Milam County|     3| 120.856|  0.000|   366| 14744.390| 115.101|  24,823|
| |Tyler County|     3| 138.427|  6.592|   152|  7013.658| 237.304|  21,672|
| |Bandera County|     3| 129.803|  0.000|   100|  4326.757| 55.630|  23,112|
| |Hutchinson County|     3| 143.280|  0.000|   133|  6352.087| 47.760|  20,938|
| |Madison County|     3| 210.025| 10.001|   684| 47885.746| 160.019|  14,284|
| |Nolan County|     3| 203.887|  0.000|   140|  9514.748| 58.254|  14,714|
| |Morris County|     3| 242.170|  0.000|   134| 10816.920| 196.042|  12,388|
| |Comanche County|     3| 220.022|  0.000|   172| 12614.595| 314.317|  13,635|
| |Terry County|     2| 162.114|  0.000|   173| 14022.858| 347.387|  12,337|
| |Throckmorton County|     2| 1332.445|  0.000|     4|  2664.890|  0.000|   1,501|
| |Upshur County|     2| 47.901|  0.000|   269|  6442.651| 147.124|  41,753|
| |Scurry County|     2| 119.739|  8.553|   505| 30234.090| 205.267|  16,703|
| |Rusk County|     2| 36.761|  0.000|   398|  7315.370| 73.521|  54,406|
| |Runnels County|     2| 194.856| 13.918|   152| 14809.041| 389.712|  10,264|
| |Pecos County|     2| 126.398|  9.028|   258| 16305.378| 126.398|  15,823|
| |La Salle County|     2| 265.957|  0.000|   364| 48404.255| 56.991|   7,520|
| |Ochiltree County|     2| 203.335|  0.000|   100| 10166.734| 72.620|   9,836|
| |Montague County|     2| 100.918|  7.208|    86|  4339.489| 115.335|  19,818|
| |Culberson County|     2| 921.234|  0.000|    21|  9672.962| 263.210|   2,171|
| |Hudspeth County|     2| 409.333|  0.000|    35|  7163.324| 321.619|   4,886|
| |Gray County|     2| 91.383|  0.000|   226| 10326.236| 71.801|  21,886|
| |Coke County|     2| 590.493|  0.000|    43| 12695.601| 42.178|   3,387|
| |Colorado County|     2| 93.054|  0.000|   362| 16842.693| 438.681|  21,493|
| |Jim Hogg County|     2| 384.615| 27.473|    65| 12500.000| 82.418|   5,200|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461|  0.000|   9,203|
| |Bosque County|     2| 107.038|  0.000|   180|  9633.396| 137.620|  18,685|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536|  0.000|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Hansford County|     2| 370.439|  0.000|    93| 17225.412| 529.199|   5,399|
| |Mitchell County|     1| 117.028|  0.000|    70|  8191.925| 150.464|   8,545|
| |McCulloch County|     1| 125.251|  0.000|    58|  7264.529| 178.929|   7,984|
| |Llano County|     1| 45.882|  0.000|    92|  4221.152| 19.664|  21,795|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Kimble County|     1| 230.574|  0.000|    16|  3689.186| 65.878|   4,337|
| |Fisher County|     1| 261.097|  0.000|    31|  8093.995| 111.899|   3,830|
| |Hall County|     1| 337.382|  0.000|    15|  5060.729| 192.790|   2,964|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966|  0.000|   1,546|
| |Crosby County|     1| 174.307|  0.000|    65| 11329.963| 49.802|   5,737|
| |Eastland County|     1| 54.466|  0.000|    92|  5010.893| 147.837|  18,360|
| |Clay County|     1| 95.502|  0.000|    47|  4488.588| 95.502|  10,471|
| |Sutton County|     1| 264.831|  0.000|    68| 18008.475| 226.998|   3,776|
| |Winkler County|     1| 124.844|  0.000|    88| 10986.267| 71.339|   8,010|
| |Wilbarger County|     1| 78.315|  0.000|    78|  6108.544| 100.690|  12,769|
| |Ward County|     1| 83.347|  0.000|    99|  8251.375| 119.067|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Rains County|     1| 79.911|  0.000|    54|  4315.167| 34.247|  12,514|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420|  0.000|   2,211|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366|  0.000|   2,793|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Freestone County|     0|  0.000|  0.000|   185|  9382.766| 202.871|  19,717|
| |Haskell County|     0|  0.000|  0.000|    52|  9190.527| 252.487|   5,658|
| |Baylor County|     0|  0.000|  0.000|    13|  3704.759| 81.423|   3,509|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Archer County|     0|  0.000|  0.000|    33|  3858.295| 200.431|   8,553|
| |Hartley County|     0|  0.000|  0.000|    94| 16857.963| 230.580|   5,576|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Sherman County|     0|  0.000|  0.000|    44| 14559.894| 189.090|   3,022|
| |Somervell County|     0|  0.000|  0.000|    85|  9312.007| 172.155|   9,128|
| |Sterling County|     0|  0.000|  0.000|     1|   774.593| 110.656|   1,291|
| |Hemphill County|     0|  0.000|  0.000|    45| 11783.189| 112.221|   3,819|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Lipscomb County|     0|  0.000|  0.000|    22|  6804.825| 176.749|   3,233|
| |Childress County|     0|  0.000|  0.000|    53|  7254.312| 254.194|   7,306|
| |Jones County|     0|  0.000|  0.000|   600| 29876.015| 28.453|  20,083|
| |Cochran County|     0|  0.000|  0.000|    33| 11566.772| 50.073|   2,853|
| |Shackelford County|     0|  0.000|  0.000|    19|  5819.296| 43.754|   3,265|
| |Stonewall County|     0|  0.000|  0.000|     7|  5185.185| 211.640|   1,350|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Wheeler County|     0|  0.000|  0.000|    36|  7120.253| 84.765|   5,056|
| |Edwards County|     0|  0.000|  0.000|    30| 15527.950| 147.885|   1,932|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Mason County|     0|  0.000|  0.000|    60| 14038.372| 233.973|   4,274|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Mills County|     0|  0.000|  0.000|    26|  5335.522| 117.264|   4,873|
| |Carson County|     0|  0.000|  0.000|    17|  2868.714| 48.214|   5,926|
| |Collingsworth County|     0|  0.000|  0.000|    13|  4452.055| 97.847|   2,920|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000|  0.000|   1,200|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Jack County|     0|  0.000|  0.000|    99| 11080.022| 639.540|   8,935|
| |Concho County|     0|  0.000|  0.000|    34| 12472.487| 314.432|   2,726|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |San Saba County|     0|  0.000|  0.000|    27|  4459.125| 70.780|   6,055|
| |McMullen County|     0|  0.000|  0.000|    10| 13458.950| 192.271|     743|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Coleman County|     0|  0.000|  0.000|    33|  4036.697| 244.648|   8,175|
| |Foard County|     0|  0.000|  0.000|     3|  2597.403| 123.686|   1,155|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 43.581|   3,278|
| |Kinney County|     0|  0.000|  0.000|    21|  5726.752| 77.915|   3,667|
| |Hardeman County|     0|  0.000|  0.000|    22|  5593.694| 145.291|   3,933|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 9,539| 444.134| N/A|575,318| 26786.714| N/A|21,477,737|
| |Miami-Dade County| 2,081| 765.935| 10.884|146,026| 53746.494| 652.152|2,716,940|
| |Broward County| 1,013| 518.748| 14.046|66,826| 34220.992| 287.356|1,952,778|
| |Palm Beach County|   992| 662.760|  5.345|39,274| 26239.168| 188.692|1,496,770|
| |Pinellas County|   558| 572.310|  8.498|18,774| 19255.464| 122.052| 974,996|
| |Hillsborough County|   487| 330.850|  9.608|34,368| 23348.334| 158.874|1,471,968|
| |Lee County|   375| 486.648|  7.601|17,451| 22646.666| 151.834| 770,577|
| |Polk County|   360| 496.705|  9.067|15,506| 21394.167| 203.215| 724,777|
| |Orange County|   351| 251.892|  5.434|33,486| 24030.968| 167.621|1,393,452|
| |Manatee County|   245| 607.559|  6.377| 9,843| 24408.994| 178.194| 403,253|
| |Duval County|   222| 231.792|  4.922|24,731| 25821.844| 179.139| 957,755|
| |St. Lucie County|   197| 600.066| 13.490| 6,283| 19138.158| 199.732| 328,297|
| |Brevard County|   178| 295.710|  6.408| 6,538| 10861.512| 104.187| 601,942|
| |Sarasota County|   173| 398.855|  8.563| 6,728| 15511.525| 155.458| 433,742|
| |Volusia County|   169| 305.449|  8.779| 8,482| 15330.282| 134.780| 553,284|
| |Collier County|   154| 400.102|  6.681|10,918| 28365.662| 174.441| 384,902|
| |Pasco County|   152| 274.394|  5.931| 7,490| 13521.149| 96.966| 553,947|
| |Escambia County|   152| 477.513| 14.361|10,317| 32411.189| 307.421| 318,316|
| |Seminole County|   145| 307.317|  7.872| 7,492| 15878.735| 102.944| 471,826|
| |Osceola County|   119| 316.699|  5.703|10,373| 27606.048| 229.635| 375,751|
| |Marion County|   115| 314.569| 10.160| 7,319| 20020.297| 291.514| 365,579|
| |Martin County|   104| 645.963|  8.873| 3,937| 24453.416| 87.844| 161,000|
| |Charlotte County|   101| 534.646|  7.562| 2,388| 12640.940| 99.065| 188,910|
| |Lake County|    86| 234.257|  7.004| 5,650| 15390.147| 184.059| 367,118|
| |Indian River County|    67| 418.952|  9.826| 2,661| 16639.258| 105.408| 159,923|
| |Clay County|    65| 296.463|  9.122| 3,484| 15890.391| 121.191| 219,252|
| |Bay County|    64| 366.332| 10.630| 4,836| 27680.948| 318.087| 174,705|
| |Hernando County|    60| 309.406|  8.840| 2,255| 11628.507| 167.227| 193,920|
| |Jackson County|    53| 1141.897| 46.168| 2,036| 43866.075| 427.827|  46,414|
| |Okaloosa County|    50| 237.261|  6.101| 3,742| 17756.646| 136.256| 210,738|
| |Suwannee County|    47| 1058.153|  9.649| 2,259| 50858.905| 2534.422|  44,417|
| |Santa Rosa County|    47| 255.001|  6.976| 4,237| 22988.069| 212.372| 184,313|
| |St. Johns County|    47| 177.578|  5.937| 3,978| 15029.924| 171.641| 264,672|
| |Sumter County|    44| 332.276|  3.236| 1,558| 11765.594| 270.783| 132,420|
| |Highlands County|    41| 385.988|  5.380| 1,632| 15364.194| 246.118| 106,221|
| |Citrus County|    40| 267.278|  3.818| 1,799| 12020.821| 239.595| 149,657|
| |Hendry County|    39| 928.085|  3.400| 1,884| 44833.659| 343.358|  42,022|
| |Putnam County|    33| 442.828| 11.502| 1,611| 21618.067| 176.364|  74,521|
| |Alachua County|    29| 107.789|  1.593| 4,670| 17357.820| 264.960| 269,043|
| |Gadsden County|    28| 613.228| 21.901| 2,046| 44809.461| 447.406|  45,660|
| |Leon County|    27| 91.967|  0.973| 5,443| 18539.965| 212.644| 293,582|
| |Columbia County|    26| 362.693| 21.921| 3,045| 42476.913| 302.908|  71,686|
| |DeSoto County|    20| 526.302| 15.037| 1,422| 37420.068| 240.595|  38,001|
| |Walton County|    18| 243.010|  5.786| 1,491| 20129.335| 148.506|  74,071|
| |Flagler County|    14| 121.653|  1.241| 1,163| 10105.925| 105.516| 115,081|
| |Washington County|    14| 549.602|  0.000|   933| 36627.017| 342.099|  25,473|
| |Nassau County|    13| 146.685|  3.224| 1,345| 15176.305| 170.864|  88,625|
| |Monroe County|    13| 175.136|  0.000| 1,643| 22134.504| 215.552|  74,228|
| |Okeechobee County|    12| 284.576|  0.000| 1,148| 27224.436| 315.066|  42,168|
| |Madison County|    11| 594.820| 23.175|   766| 41421.078| 448.046|  18,493|
| |Calhoun County|     8| 567.175| 10.128|   503| 35661.113| 283.587|  14,105|
| |Hardee County|     8| 296.989|  5.303| 1,012| 37569.143| 190.922|  26,937|
| |Gilchrist County|     7| 376.709| 15.376|   405| 21795.286| 299.829|  18,582|
| |Liberty County|     7| 837.922| 17.100|   411| 49197.989| 188.105|   8,354|
| |Levy County|     6| 144.568|  3.442|   785| 18914.295| 337.325|  41,503|
| |Jefferson County|     5| 350.976|  0.000|   469| 32921.522| 140.390|  14,246|
| |Taylor County|     5| 231.814|  0.000| 1,102| 51091.845| 907.387|  21,569|
| |Union County|     5| 328.149|  0.000|   489| 32092.932| 1078.202|  15,237|
| |Wakulla County|     5| 148.196|  4.234|   781| 23148.285| 313.330|  33,739|
| |Holmes County|     4| 203.905| 14.565|   534| 27221.288| 196.622|  19,617|
| |Gulf County|     4| 293.277| 20.948|   756| 55429.284| 1015.994|  13,639|
| |Hamilton County|     4| 277.239|  0.000|   635| 44011.644| 168.323|  14,428|
| |Baker County|     4| 136.939|  0.000| 1,078| 36905.169| 714.041|  29,210|
| |Dixie County|     4| 237.727|  0.000|   595| 35361.940| 356.591|  16,826|
| |Bradford County|     4| 141.839|  0.000|   573| 20318.428| 329.269|  28,201|
| |Glades County|     3| 217.218|  0.000|   422| 30555.354| 175.843|  13,811|
| |Franklin County|     3| 247.423| 11.782|   472| 38927.835| 494.845|  12,125|
| |Lafayette County|     2| 237.473|  0.000| 1,009| 119805.272| 14604.607|   8,422|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  0.089|26,565| 16482.606|  8.421|1,611,699|
| |Essex County| 1,194| 1513.243|  0.000|17,930| 22723.989|  8.510| 789,034|
| |Suffolk County| 1,076| 1338.463|  0.355|22,017| 27387.496| 15.638| 803,907|
| |Worcester County| 1,007| 1212.344|  0.172|13,686| 16476.809|  5.504| 830,622|
| |Norfolk County|   997| 1410.633|  0.000|10,682| 15113.721|  8.691| 706,775|
| |Plymouth County|   723| 1387.178|  0.274| 9,288| 17820.346|  8.223| 521,202|
| |Hampden County|   709| 1520.246|  0.613| 7,637| 16375.340|  5.514| 466,372|
| |Bristol County|   637| 1127.001|  0.505| 9,408| 16644.935|  9.352| 565,217|
| |Barnstable County|   158| 741.819|  0.000| 1,803|  8465.186|  0.671| 212,990|
| |Hampshire County|   130| 808.307|  0.888| 1,184|  7361.811|  4.441| 160,830|
| |Franklin County|    61| 869.194|  0.000|   411|  5856.369|  0.000|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  0.000| 124,944|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,756| 612.067| N/A|207,805| 16398.985| N/A|12,671,821|
| |Cook County| 4,964| 963.840|  0.999|116,620| 22643.636| 129.592|5,150,233|
| |DuPage County|   526| 569.930|  0.929|13,032| 14120.385| 111.447| 922,921|
| |Lake County|   450| 646.055|  0.820|13,375| 19202.194| 130.031| 696,535|
| |Will County|   351| 508.148|  1.448|10,013| 14495.985| 144.358| 690,743|
| |Kane County|   304| 570.996|  0.000|10,314| 19372.543| 137.114| 532,403|
| |St. Clair County|   162| 623.830|  0.550| 4,484| 17267.007| 250.852| 259,686|
| |Winnebago County|   135| 477.754|  2.022| 3,885| 13748.708| 51.062| 282,572|
| |McHenry County|   115| 373.651|  0.464| 3,417| 11102.302| 92.368| 307,774|
| |Madison County|    85| 323.236|  4.889| 3,152| 11986.340| 281.405| 262,966|
| |Kankakee County|    70| 637.163|  2.601| 1,900| 17294.424| 146.938| 109,862|
| |Rock Island County|    41| 288.979|  5.034| 1,884| 13278.921| 128.882| 141,879|
| |Peoria County|    37| 206.497|  1.595| 1,917| 10698.798| 228.821| 179,179|
| |Sangamon County|    35| 179.790|  1.468| 1,462|  7510.068| 137.961| 194,672|
| |LaSalle County|    33| 303.674| 11.831|   960|  8834.166| 232.686| 108,669|
| |DeKalb County|    32| 305.061|  2.724|   993|  9466.429| 74.903| 104,897|
| |Union County|    23| 1381.133|  0.000|   363| 21797.874| 334.560|  16,653|
| |Macon County|    23| 221.135|  0.000|   762|  7326.289| 166.194| 104,009|
| |Kendall County|    23| 178.308|  0.000| 1,479| 11466.005| 110.751| 128,990|
| |Boone County|    23| 429.553|  0.000|   771| 14399.372| 13.340|  53,544|
| |Jefferson County|    22| 583.802| 11.373|   356|  9446.980| 250.201|  37,684|
| |Coles County|    21| 414.848|  2.822|   630| 12445.428| 403.559|  50,621|
| |Jackson County|    20| 352.423|  2.517|   778| 13709.251| 140.969|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,776|  8469.686| 61.315| 209,689|
| |Clinton County|    17| 452.585|  0.000|   492| 13098.344| 308.062|  37,562|
| |Whiteside County|    17| 308.111|  0.000|   399|  7231.536| 103.567|  55,175|
| |McLean County|    16| 93.285|  0.833|   782|  4559.315| 105.779| 171,517|
| |McDonough County|    15| 505.357|  0.000|   157|  5289.401| 52.942|  29,682|
| |Iroquois County|    14| 516.338| 15.806|   280| 10326.768| 79.031|  27,114|
| |Monroe County|    13| 375.321|  0.000|   358| 10335.768| 164.976|  34,637|
| |Cass County|    11| 905.573|  0.000|   258| 21239.812| 317.539|  12,147|
| |Morgan County|    11| 326.817| 21.222|   402| 11943.669| 568.746|  33,658|
| |Tazewell County|     9| 68.284|  1.084|   724|  5493.046| 144.155| 131,803|
| |Adams County|     7| 106.976|  4.366|   665| 10162.757| 268.533|  65,435|
| |Williamson County|     7| 105.110|  2.145|   552|  8288.662| 306.749|  66,597|
| |Montgomery County|     7| 246.357|  0.000|   192|  6757.232| 115.637|  28,414|
| |Jasper County|     7| 728.408|  0.000|    72|  7492.196| 193.251|   9,610|
| |Randolph County|     7| 220.250|  0.000|   539| 16959.285| 310.149|  31,782|
| |Stephenson County|     6| 134.838|  0.000|   348|  7820.576| 57.788|  44,498|
| |Ogle County|     5| 98.730|  0.000|   437|  8629.031| 73.343|  50,643|
| |Grundy County|     5| 97.936|  0.000|   391|  7658.558| 181.880|  51,054|
| |Christian County|     4| 123.824|  0.000|   157|  4860.079| 61.912|  32,304|
| |Carroll County|     4| 279.623|  0.000|    89|  6221.601| 299.596|  14,305|
| |Bureau County|     4| 122.594|  4.378|   276|  8458.992| 267.080|  32,628|
| |Mercer County|     4| 259.118|  0.000|    81|  5247.134| 46.271|  15,437|
| |Perry County|     3| 143.431| 13.660|   213| 10183.592| 198.071|  20,916|
| |Macoupin County|     3| 66.776|  0.000|   245|  5453.412| 203.509|  44,926|
| |Cumberland County|     3| 278.655|  0.000|    69|  6409.066| 159.231|  10,766|
| |Woodford County|     3| 78.005|  0.000|   188|  4888.323| 133.723|  38,459|
| |Fayette County|     3| 140.607|  0.000|    80|  3749.531| 87.043|  21,336|
| |Livingston County|     3| 84.156|  4.007|   151|  4235.862| 140.260|  35,648|
| |Bond County|     3| 182.637|  0.000|    82|  4992.086| 173.940|  16,426|
| |Douglas County|     3| 154.123|  7.339|   151|  7757.513| 212.836|  19,465|
| |Wayne County|     2| 123.343|  8.810|    75|  4625.347| 114.532|  16,215|
| |Jersey County|     2| 91.857|  0.000|   157|  7210.766| 275.571|  21,773|
| |Jo Daviess County|     2| 94.184|  6.727|   145|  6828.349| 121.094|  21,235|
| |Clark County|     2| 129.525|  0.000|    96|  6217.214| 120.273|  15,441|
| |Gallatin County|     2| 414.250|  0.000|    54| 11184.756| 88.768|   4,828|
| |Ford County|     2| 154.309|  0.000|    60|  4629.272| 121.243|  12,961|
| |Vermilion County|     2| 26.400|  0.000|   273|  3603.580| 69.771|  75,758|
| |Shelby County|     2| 92.447|  6.603|   109|  5038.366| 191.498|  21,634|
| |Saline County|     2| 85.139|  0.000|   140|  5959.729| 48.651|  23,491|
| |Hancock County|     1| 56.472|  0.000|    95|  5364.807| 266.223|  17,708|
| |Lee County|     1| 29.329|  0.000|   198|  5807.133| 104.746|  34,096|
| |Effingham County|     1| 29.405|  0.000|   252|  7410.021| 378.062|  34,008|
| |Franklin County|     1| 25.995|  3.714|   249|  6472.744| 215.387|  38,469|
| |Knox County|     1| 20.121|  0.000|   370|  7444.818| 192.588|  49,699|
| |Logan County|     1| 34.943|  4.992|   201|  7023.552| 394.357|  28,618|
| |Henry County|     1| 20.444|  0.000|   313|  6399.117| 189.841|  48,913|
| |Washington County|     1| 72.010| 10.287|    75|  5400.734| 82.297|  13,887|
| |Wabash County|     1| 86.806| 12.401|    70|  6076.389| 434.028|  11,520|
| |Pulaski County|     1| 187.441|  0.000|   101| 18931.584| 187.441|   5,335|
| |Moultrie County|     0|  0.000|  0.000|   113|  7792.566| 384.210|  14,501|
| |Menard County|     0|  0.000|  0.000|    62|  5083.634| 70.281|  12,196|
| |Mason County|     0|  0.000|  0.000|    63|  4715.922| 106.937|  13,359|
| |Massac County|     0|  0.000|  0.000|    45|  3267.499| 51.865|  13,772|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |White County|     0|  0.000|  0.000|    87|  6426.830| 189.956|  13,537|
| |Warren County|     0|  0.000|  0.000|   205| 12170.506| 118.737|  16,844|
| |Scott County|     0|  0.000|  0.000|    35|  7069.279| 403.959|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    19|  2807.329| 21.108|   6,768|
| |Richland County|     0|  0.000|  0.000|    42|  2707.407| 202.595|  15,513|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203|  0.000|   5,739|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 68.402|   4,177|
| |Pike County|     0|  0.000|  0.000|    35|  2249.213| 110.166|  15,561|
| |Piatt County|     0|  0.000|  0.000|    70|  4282.917| 61.185|  16,344|
| |Crawford County|     0|  0.000|  0.000|    37|  1982.107| 61.223|  18,667|
| |Clay County|     0|  0.000|  0.000|    38|  2882.282| 162.535|  13,184|
| |Calhoun County|     0|  0.000|  0.000|    14|  2954.210| 120.580|   4,739|
| |Brown County|     0|  0.000|  0.000|    16|  2432.350| 43.435|   6,578|
| |Alexander County|     0|  0.000|  0.000|    40|  6943.239| 74.392|   5,761|
| |De Witt County|     0|  0.000|  0.000|    38|  2429.978| 45.676|  15,638|
| |Edgar County|     0|  0.000|  0.000|    35|  2039.508| 49.947|  17,161|
| |Edwards County|     0|  0.000|  0.000|    27|  4222.048| 201.050|   6,395|
| |Marshall County|     0|  0.000|  0.000|    35|  3059.976| 99.918|  11,438|
| |Fulton County|     0|  0.000|  0.000|    48|  1397.787| 58.241|  34,340|
| |Marion County|     0|  0.000|  0.000|   188|  5053.084| 103.673|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    65|  4145.937| 136.679|  15,678|
| |Johnson County|     0|  0.000|  0.000|    79|  6362.245| 115.050|  12,417|
| |Henderson County|     0|  0.000|  0.000|    24|  3611.195| 236.447|   6,646|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809|  0.000|   3,821|
| |Hamilton County|     0|  0.000|  0.000|    37|  4558.896| 140.815|   8,116|
| |Greene County|     0|  0.000|  0.000|    73|  5628.807| 165.229|  12,969|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,453| 582.175| N/A|129,647| 10127.098| N/A|12,801,989|
| |Philadelphia County| 1,717| 1083.921| N/A|32,348| 20420.892| N/A|1,584,064|
| |Montgomery County|   859| 1033.800|  0.344|10,433| 12556.038| 48.827| 830,915|
| |Delaware County|   713| 1258.057|  3.529| 9,731| 17169.919| 115.194| 566,747|
| |Bucks County|   583| 927.945|  0.227| 7,441| 11843.634| 52.525| 628,270|
| |Lancaster County|   421| 771.452|  2.618| 6,228| 11412.362| 66.229| 545,724|
| |Berks County|   375| 890.389|  2.374| 5,601| 13298.857| 65.804| 421,164|
| |Chester County|   350| 666.681|  0.272| 5,347| 10184.975| 51.702| 524,989|
| |Lehigh County|   341| 923.324|  1.547| 5,073| 13736.130| 37.908| 369,318|
| |Northampton County|   295| 966.310|  1.404| 4,013| 13145.094| 38.372| 305,285|
| |Allegheny County|   270| 222.031|  2.702| 9,504|  7815.500| 67.197|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,966|  9376.461| 17.715| 209,674|
| |Luzerne County|   185| 582.830|  0.450| 3,621| 11407.707| 71.560| 317,417|
| |Dauphin County|   160| 574.921|  0.513| 2,995| 10761.807| 85.212| 278,299|
| |Monroe County|   125| 734.124|  0.839| 1,669|  9802.021| 27.687| 170,271|
| |York County|   105| 233.823|  3.818| 2,907|  6473.551| 100.528| 449,058|
| |Beaver County|    94| 573.419|  1.743| 1,410|  8601.285| 73.202| 163,929|
| |Cumberland County|    71| 280.223|  0.000| 1,373|  5418.953| 41.159| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,651| 11643.734| 34.255| 141,793|
| |Schuylkill County|    51| 360.784|  0.000|   950|  6720.478| 31.329| 141,359|
| |Westmoreland County|    48| 137.576|  0.819| 1,627|  4663.241| 30.299| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,417|  9140.343| 45.153| 155,027|
| |Columbia County|    35| 538.760|  0.000|   492|  7573.425| 32.985|  64,964|
| |Carbon County|    28| 436.259|  0.000|   397|  6185.535| 55.645|  64,182|
| |Erie County|    27| 100.101|  4.237| 1,217|  4511.953| 56.671| 269,728|
| |Susquehanna County|    27| 669.510|  0.000|   221|  5480.063| 24.797|  40,328|
| |Adams County|    22| 213.574|  2.774|   548|  5319.924| 33.284| 103,009|
| |Pike County|    21| 376.283|  0.000|   528|  9460.840|  5.120|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   444|  3918.834| 55.479| 113,299|
| |Northumberland County|    18| 198.144|  7.863|   575|  6329.602| 157.257|  90,843|
| |Butler County|    17| 90.496|  1.521|   723|  3848.754| 39.545| 187,853|
| |Washington County|    17| 82.179|  2.762|   910|  4399.004| 37.982| 206,865|
| |Lawrence County|    16| 187.108|  0.000|   429|  5016.840| 61.813|  85,512|
| |Mercer County|    12| 109.665|  3.917|   495|  4523.688| 69.193| 109,424|
| |Centre County|    11| 67.740|  0.880|   393|  2420.174| 18.475| 162,385|
| |Wayne County|    10| 194.700|  2.781|   164|  3193.084|  5.563|  51,361|
| |Armstrong County|     9| 139.028|  4.414|   244|  3769.213| 61.790|  64,735|
| |Blair County|     8| 65.666|  3.518|   354|  2905.712| 71.529| 121,829|
| |Indiana County|     8| 95.155|  3.398|   359|  4270.099| 62.871|  84,073|
| |Wyoming County|     8| 298.574|  0.000|    63|  2351.273| 10.663|  26,794|
| |Fayette County|     6| 46.413|  1.105|   628|  4857.899| 140.344| 129,274|
| |Juniata County|     6| 242.297|  0.000|   139|  5613.213| 34.614|  24,763|
| |Clinton County|     5| 129.426|  0.000|   128|  3313.315| 22.187|  38,632|
| |Huntingdon County|     5| 110.757|  3.164|   336|  7442.850| 88.605|  45,144|
| |Perry County|     5| 108.057|  0.000|   145|  3133.645| 64.834|  46,272|
| |Bedford County|     4| 83.528|  0.000|   154|  3215.837| 32.815|  47,888|
| |Cambria County|     3| 23.043|  0.000|   393|  3018.619| 57.059| 130,192|
| |Montour County|     3| 164.564|  0.000|   113|  6198.574| 86.200|  18,230|
| |Tioga County|     3| 73.908|  0.000|    41|  1010.076| 10.558|  40,591|
| |Bradford County|     3| 49.732|  0.000|    93|  1541.701| 16.577|  60,323|
| |Somerset County|     3| 40.846|  0.000|   143|  1946.982| 15.560|  73,447|
| |Fulton County|     2| 137.646|  0.000|    28|  1927.047|  9.832|  14,530|
| |Clarion County|     2| 52.032|  0.000|    90|  2341.433| 37.166|  38,438|
| |Union County|     2| 44.521|  0.000|   305|  6789.395| 213.063|  44,923|
| |Elk County|     2| 66.867|  0.000|    58|  1939.151| 42.986|  29,910|
| |Snyder County|     2| 49.539|  0.000|   124|  3071.436| 63.693|  40,372|
| |Warren County|     1| 25.516|  0.000|    23|   586.869|  0.000|  39,191|
| |Crawford County|     1| 11.816|  0.000|   169|  1996.951| 25.321|  84,629|
| |Jefferson County|     1| 23.028|  0.000|    78|  1796.200| 16.449|  43,425|
| |Greene County|     1| 27.599|  0.000|   126|  3477.493| 39.427|  36,233|
| |Clearfield County|     1| 12.618|  1.803|   194|  2447.795| 36.050|  79,255|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  0.000|  40,625|
| |Mifflin County|     1| 21.674|  0.000|   126|  2730.938| 18.578|  46,138|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Venango County|     0|  0.000|  0.000|    67|  1322.334|  8.458|  50,668|
| |Potter County|     0|  0.000|  0.000|    21|  1270.725|  8.644|  16,526|
| |Forest County|     0|  0.000|  0.000|    12|  1655.858| 39.425|   7,247|
| |Cameron County|     0|  0.000|  0.000|     8|  1798.966| 32.124|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,516| 652.458| N/A|97,512|  9764.033| N/A|9,986,857|
| |Wayne County| 2,839| 1622.895|  1.062|29,217| 16701.699| 77.090|1,749,343|
| |Oakland County| 1,142| 908.090|  1.477|16,547| 13157.769| 105.872|1,257,584|
| |Macomb County|   955| 1092.712|  1.308|11,405| 13049.617| 140.573| 873,972|
| |Genesee County|   298| 734.328|  0.704| 3,758|  9260.423| 33.091| 405,813|
| |Kent County|   158| 240.504|  0.217| 7,802| 11876.004| 55.016| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,188| 11483.213| 116.961| 190,539|
| |Washtenaw County|   114| 310.119|  0.389| 2,657|  7227.946| 41.194| 367,601|
| |Kalamazoo County|    86| 324.447|  1.617| 1,754|  6617.220| 57.129| 265,066|
| |Berrien County|    68| 443.283|  1.863| 1,467|  9563.171| 84.745| 153,401|
| |Muskegon County|    63| 362.974|  3.292| 1,227|  7069.357| 39.507| 173,566|
| |Ottawa County|    59| 202.172|  1.469| 1,930|  6613.439| 43.567| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   842|  5291.338| 19.750| 159,128|
| |Calhoun County|    43| 320.515|  1.065|   849|  6328.312| 57.501| 134,159|
| |Jackson County|    35| 220.806|  0.901|   745|  4700.019| 30.643| 158,510|
| |Bay County|    35| 339.391|  5.541|   712|  6904.175| 102.510| 103,126|
| |Ingham County|    33| 112.857|  0.977| 1,641|  5612.060| 42.505| 292,406|
| |Lapeer County|    33| 376.682|  0.000|   506|  5775.794| 58.704|  87,607|
| |Tuscola County|    29| 555.077|  0.000|   386|  7388.267| 82.031|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   354|  5196.559| 23.068|  68,122|
| |Livingston County|    28| 145.837|  0.000|   923|  4807.417| 63.990| 191,995|
| |Hillsdale County|    25| 548.186|  0.000|   283|  6205.460| 37.590|  45,605|
| |Monroe County|    23| 152.824|  0.000| 1,074|  7136.213| 82.582| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   166|  4077.522| 35.091|  40,711|
| |Cass County|    15| 289.648|  2.759|   363|  7009.481| 102.066|  51,787|
| |Lenawee County|    13| 132.045|  1.451|   476|  4834.892| 62.395|  98,451|
| |Clinton County|    13| 163.327|  0.000|   440|  5527.985| 30.512|  79,595|
| |Alpena County|    13| 457.666|  0.000|   130|  4576.659|  0.000|  28,405|
| |Van Buren County|    13| 171.783|  5.663|   509|  6725.954| 103.825|  75,677|
| |Iosco County|    12| 477.574|  0.000|   136|  5412.504| 11.371|  25,127|
| |Otsego County|    11| 445.922|  0.000|   136|  5513.216|  5.791|  24,668|
| |Marquette County|    11| 164.920|  0.000|   196|  2938.575| 77.105|  66,699|
| |Midland County|    10| 120.256|  0.000|   360|  4329.213| 37.795|  83,156|
| |St. Joseph County|    10| 164.031|  4.687|   637| 10448.789| 107.792|  60,964|
| |Isabella County|     9| 128.807|  0.000|   227|  3248.798| 40.891|  69,872|
| |Eaton County|     8| 72.551|  0.000|   474|  4298.618| 15.547| 110,268|
| |Ionia County|     7| 108.197|  0.000|   277|  4281.497|  6.624|  64,697|
| |Allegan County|     6| 50.813|  0.000|   572|  4844.132| 52.022| 118,081|
| |Oceana County|     6| 226.697|  0.000|   488| 18438.055| 53.976|  26,467|
| |Sanilac County|     6| 145.737|  0.000|   117|  2841.875| 24.290|  41,170|
| |Grand Traverse County|     5| 53.713|  0.000|   245|  2631.918| 49.109|  93,088|
| |Crawford County|     5| 356.405|  0.000|   110|  7840.901| 40.732|  14,029|
| |Wexford County|     4| 118.938|  0.000|    74|  2200.351| 21.239|  33,631|
| |Huron County|     4| 129.111|  0.000|   176|  5680.901| 83.000|  30,981|
| |Kalkaska County|     4| 221.754|  0.000|    56|  3104.557| 15.840|  18,038|
| |Arenac County|     3| 201.572|  0.000|    49|  3292.347| 67.191|  14,883|
| |Montcalm County|     3| 46.957|  4.472|   204|  3193.088| 26.833|  63,888|
| |Clare County|     3| 96.931|  0.000|    84|  2714.055| 55.389|  30,950|
| |Ogemaw County|     3| 142.878|  6.804|    55|  2619.422|  6.804|  20,997|
| |Delta County|     3| 83.836|  0.000|   116|  3241.672| 75.852|  35,784|
| |Gladwin County|     2| 78.589|  0.000|    68|  2672.011| 50.521|  25,449|
| |Barry County|     2| 32.494|  0.000|   200|  3249.391| 20.889|  61,550|
| |Branch County|     2| 45.959|  0.000|   383|  8801.158| 59.090|  43,517|
| |Emmet County|     2| 59.853|  0.000|    79|  2364.208| 72.679|  33,415|
| |Charlevoix County|     2| 76.502|  0.000|    58|  2218.567| 49.180|  26,143|
| |Mecosta County|     2| 46.027|  0.000|    74|  1702.989| 19.726|  43,453|
| |Roscommon County|     2| 83.267| 11.895|    58|  2414.755| 29.738|  24,019|
| |Cheboygan County|     2| 79.126|  0.000|    57|  2255.104| 45.215|  25,276|
| |Dickinson County|     2| 79.242|  0.000|    59|  2337.652| 22.641|  25,239|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122|  0.000|  10,405|
| |Benzie County|     1| 56.287|  0.000|    35|  1970.055| 48.246|  17,766|
| |Oscoda County|     1| 121.344|  0.000|    27|  3276.301| 52.005|   8,241|
| |Presque Isle County|     1| 79.416|  0.000|    21|  1667.726| 11.345|  12,592|
| |Missaukee County|     1| 66.146|  0.000|    42|  2778.145|  9.449|  15,118|
| |Manistee County|     1| 40.720|  5.817|    43|  1750.957| 23.269|  24,558|
| |Iron County|     1| 90.367|  0.000|    24|  2168.805| 51.638|  11,066|
| |Gogebic County|     1| 71.556|  0.000|   135|  9660.107| 153.335|  13,975|
| |Mackinac County|     0|  0.000|  0.000|    27|  2500.232| 13.229|  10,799|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128|  0.000|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  0.000|  23,460|
| |Alger County|     0|  0.000|  0.000|    17|  1866.491| 94.109|   9,108|
| |Ontonagon County|     0|  0.000|  0.000|    29|  5069.930| 374.625|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   268|  5471.621| 49.583|  48,980|
| |Montmorency County|     0|  0.000|  0.000|     8|   857.633|  0.000|   9,328|
| |Menominee County|     0|  0.000|  0.000|   182|  7989.464| 257.118|  22,780|
| |Mason County|     0|  0.000|  0.000|   107|  3671.425| 24.509|  29,144|
| |Luce County|     0|  0.000|  0.000|     4|   642.158|  0.000|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    76|  3492.487| 26.259|  21,761|
| |Lake County|     0|  0.000|  0.000|    28|  2362.271| 60.262|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    55|  1541.307| 20.017|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    44|  1178.077| 15.300|  37,349|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Antrim County|     0|  0.000|  0.000|    43|  1843.595| 12.250|  23,324|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,619| 435.040| N/A|219,080| 20634.009| N/A|10,617,423|
| |Fulton County|   476| 447.395|  5.774|22,107| 20778.486| 220.072|1,063,937|
| |Cobb County|   340| 447.285|  3.759|14,962| 19683.190| 231.724| 760,141|
| |Gwinnett County|   290| 309.746|  4.272|21,655| 23129.506| 256.952| 936,250|
| |DeKalb County|   264| 347.690|  4.892|15,101| 19888.133| 198.304| 759,297|
| |Dougherty County|   173| 1966.893|  3.248| 2,837| 32254.764| 170.540|  87,956|
| |Clayton County|   116| 396.912|  2.933| 5,570| 19058.634| 249.781| 292,256|
| |Muscogee County|   110| 561.887|  8.757| 5,092| 26010.247| 227.674| 195,769|
| |Hall County|   105| 513.596|  9.783| 6,581| 32190.216| 326.325| 204,441|
| |Richmond County|    98| 483.908|  5.643| 5,192| 25637.227| 550.216| 202,518|
| |Chatham County|    96| 331.686| 10.365| 6,317| 21825.657| 272.950| 289,430|
| |Bibb County|    84| 548.450| 14.924| 4,134| 26991.558| 456.109| 153,159|
| |Troup County|    77| 1101.227| 16.345| 2,419| 34595.692| 247.214|  69,922|
| |Cherokee County|    67| 258.914|  1.656| 4,005| 15476.885| 259.466| 258,773|
| |Bartow County|    64| 594.034|  1.326| 2,063| 19148.304| 236.022| 107,738|
| |Houston County|    62| 392.746|  1.810| 2,251| 14259.199| 234.380| 157,863|
| |Henry County|    59| 251.534|  7.308| 3,786| 16140.791| 228.390| 234,561|
| |Douglas County|    58| 396.329|  6.833| 2,892| 19761.793| 208.903| 146,343|
| |Glynn County|    56| 656.568| 15.074| 2,754| 32289.078| 329.959|  85,292|
| |Sumter County|    56| 1896.762|  0.000|   789| 26724.021| 101.612|  29,524|
| |Carroll County|    54| 450.030|  4.762| 2,052| 17101.140| 188.108| 119,992|
| |Habersham County|    52| 1147.194|  9.455| 1,212| 26738.440| 211.159|  45,328|
| |Newton County|    50| 447.451| 12.784| 2,038| 18238.116| 274.863| 111,744|
| |Lowndes County|    50| 425.873|  7.301| 3,259| 27758.377| 80.307| 117,406|
| |Upson County|    49| 1861.702| 16.283|   632| 24012.158| 493.921|  26,320|
| |Tift County|    45| 1107.174| 21.089| 1,402| 34494.636| 200.346|  40,644|
| |Thomas County|    44| 989.854|  6.428| 1,250| 28120.852| 401.726|  44,451|
| |Baldwin County|    44| 980.174| 15.912| 1,182| 26331.031| 416.892|  44,890|
| |Spalding County|    43| 644.649|  4.283| 1,039| 15576.511| 192.752|  66,703|
| |Walton County|    43| 454.579|  6.041| 1,280| 13531.657| 244.657|  94,593|
| |Mitchell County|    41| 1875.314|  0.000|   674| 30828.340| 143.752|  21,863|
| |Butts County|    40| 1604.107| 11.458|   512| 20532.563| 85.934|  24,936|
| |Whitfield County|    40| 382.307| 10.923| 3,730| 35650.113| 247.134| 104,628|
| |Hancock County|    35| 4138.583|  0.000|   340| 40203.382| 371.628|   8,457|
| |Fayette County|    34| 297.148|  6.243| 1,305| 11405.249| 217.243| 114,421|
| |Barrow County|    34| 408.457|  3.432| 1,438| 17275.348| 243.702|  83,240|
| |Ware County|    34| 951.475| 19.989| 1,237| 34616.891| 335.815|  35,734|
| |Columbia County|    34| 216.956|  9.116| 2,695| 17196.932| 374.659| 156,714|
| |Coffee County|    33| 762.600| 13.205| 1,608| 37159.430| 462.182|  43,273|
| |Early County|    32| 3140.334|  0.000|   383| 37585.868| 322.445|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   308| 36103.622| 100.474|   8,531|
| |Monroe County|    30| 1087.824| 25.901|   505| 18311.698| 233.105|  27,578|
| |Rockdale County|    27| 297.043| 14.145| 1,487| 16359.356| 220.032|  90,896|
| |Forsyth County|    27| 110.542|  2.924| 2,586| 10587.426| 171.369| 244,252|
| |Paulding County|    26| 154.150|  2.541| 1,894| 11229.227| 169.395| 168,667|
| |Coweta County|    26| 175.074|  3.848| 1,793| 12073.342| 268.382| 148,509|
| |Randolph County|    26| 3835.940|  0.000|   287| 42342.874| 316.149|   6,778|
| |Jenkins County|    24| 2766.252|  0.000|   264| 30428.769| 329.316|   8,676|
| |Gordon County|    24| 414.057|  2.465| 1,338| 23083.691| 357.371|  57,963|
| |Colquitt County|    24| 526.316|  0.000| 1,627| 35679.825| 225.564|  45,600|
| |Worth County|    23| 1135.971|  0.000|   472| 23312.096| 162.282|  20,247|
| |Lee County|    23| 766.871|  4.763|   611| 20372.099| 319.133|  29,992|
| |Clarke County|    21| 163.639|  3.340| 2,264| 17641.879| 203.714| 128,331|
| |Floyd County|    20| 203.050|  4.351| 1,823| 18507.990| 443.809|  98,498|
| |Wilcox County|    19| 2200.347|  0.000|   199| 23045.744| 248.159|   8,635|
| |Laurens County|    19| 399.613| 30.046| 1,142| 24018.845| 573.880|  47,546|
| |Appling County|    19| 1033.395|  0.000|   804| 43728.924| 979.006|  18,386|
| |Turner County|    18| 2254.227|  0.000|   263| 32936.756| 232.579|   7,985|
| |Brooks County|    18| 1164.521|  0.000|   432| 27948.502| 175.602|  15,457|
| |Putnam County|    18| 813.780|  0.000|   489| 22107.690| 381.056|  22,119|
| |Stephens County|    18| 694.311| 33.062|   700| 27000.964| 424.301|  25,925|
| |Walker County|    17| 243.689|  0.000|   823| 11797.423| 231.402|  69,761|
| |Bulloch County|    17| 213.546|  5.384| 1,405| 17648.980| 181.245|  79,608|
| |Catoosa County|    17| 251.554| 16.911|   713| 10550.459| 160.656|  67,580|
| |Decatur County|    17| 643.842| 32.463|   850| 32192.092| 286.753|  26,404|
| |Harris County|    17| 482.461|  0.000|   688| 19525.485| 125.683|  35,236|
| |Jackson County|    17| 232.950|  1.958| 1,190| 16306.508| 234.908|  72,977|
| |Peach County|    16| 580.847| 10.372|   464| 16844.551| 399.332|  27,546|
| |Oconee County|    16| 397.219|  3.547|   474| 11767.627| 117.038|  40,280|
| |Crisp County|    15| 670.481|  6.386|   416| 18594.672| 197.952|  22,372|
| |Wayne County|    14| 467.805| 23.868|   877| 29304.641| 439.164|  29,927|
| |Lamar County|    14| 733.868| 14.977|   296| 15516.066| 157.257|  19,077|
| |Dooly County|    14| 1045.556|  0.000|   264| 19716.206| 106.689|  13,390|
| |Emanuel County|    14| 618.211| 25.233|   599| 26450.587| 542.511|  22,646|
| |Greene County|    13| 709.452|  7.796|   371| 20246.671| 452.178|  18,324|
| |Wilkinson County|    12| 1340.183| 15.955|   240| 26803.663| 398.864|   8,954|
| |Telfair County|    12| 756.620| 18.015|   313| 19735.183| 288.236|  15,860|
| |Johnson County|    12| 1244.426| 14.815|   266| 27584.777| 370.365|   9,643|
| |Jefferson County|    11| 716.053| 27.898|   577| 37560.214| 678.855|  15,362|
| |Polk County|    11| 258.137|  0.000|   961| 22551.803| 512.922|  42,613|
| |Bleckley County|    10| 776.820| 11.097|   281| 21828.634| 432.800|  12,873|
| |Stewart County|    10| 1510.346| 64.729|   275| 41534.511| 431.527|   6,621|
| |McDuffie County|    10| 469.219|  0.000|   436| 20457.958| 536.251|  21,312|
| |Macon County|    10| 772.380|  0.000|   189| 14597.976| 132.408|  12,947|
| |Cook County|     9| 521.135| 24.816|   472| 27330.631| 264.703|  17,270|
| |Lumpkin County|     9| 267.777| 12.751|   417| 12407.022| 310.282|  33,610|
| |Candler County|     9| 833.102| 66.119|   282| 26103.860| 290.924|  10,803|
| |Pierce County|     9| 462.368|  7.339|   466| 23940.406| 410.994|  19,465|
| |Bryan County|     9| 227.118|  3.605|   740| 18674.136| 284.799|  39,627|
| |Screven County|     9| 644.422|  0.000|   240| 17184.591| 306.868|  13,966|
| |Toombs County|     9| 335.445|  5.325|   878| 32724.562| 633.619|  26,830|
| |Bacon County|     8| 716.589|  0.000|   472| 42278.753| 435.072|  11,164|
| |Brantley County|     8| 418.651| 22.428|   275| 14391.125| 179.422|  19,109|
| |Oglethorpe County|     8| 524.281|  9.362|   252| 16514.844| 318.313|  15,259|
| |Grady County|     8| 324.768| 17.398|   564| 22896.115| 411.759|  24,633|
| |Jeff Davis County|     8| 529.276|  0.000|   541| 35792.259| 793.913|  15,115|
| |Hart County|     8| 305.285|  5.452|   351| 13394.390| 223.512|  26,205|
| |Camden County|     7| 128.050|  5.227|   863| 15786.778| 263.941|  54,666|
| |Burke County|     7| 312.737|  0.000|   563| 25153.018| 593.563|  22,383|
| |Ben Hill County|     7| 419.162| 25.663|   544| 32574.850| 786.997|  16,700|
| |Liberty County|     7| 113.942|  9.301|   805| 13103.280| 181.376|  61,435|
| |Union County|     7| 285.586|  0.000|   335| 13667.333| 413.808|  24,511|
| |Meriwether County|     7| 330.703|  6.749|   440| 20787.074| 296.958|  21,167|
| |Haralson County|     7| 234.962|  4.795|   256|  8592.911| 163.035|  29,792|
| |Madison County|     7| 234.270|  4.781|   450| 15060.241| 224.708|  29,880|
| |Effingham County|     6| 93.318|  8.887|   833| 12955.705| 195.524|  64,296|
| |Franklin County|     6| 256.970|  0.000|   460| 19701.058| 330.390|  23,349|
| |White County|     6| 194.818|  4.639|   395| 12825.508| 194.818|  30,798|
| |Calhoun County|     6| 969.462|  0.000|   215| 34739.053| 276.989|   6,189|
| |Banks County|     6| 311.948| 14.855|   302| 15701.362| 230.247|  19,234|
| |Pickens County|     6| 184.100|  4.383|   446| 13684.760| 245.467|  32,591|
| |Pike County|     6| 316.422| 15.068|   246| 12973.315| 226.016|  18,962|
| |Seminole County|     6| 741.656| 35.317|   242| 29913.473| 812.290|   8,090|
| |Lincoln County|     5| 631.233| 18.035|   169| 21335.690| 468.916|   7,921|
| |Marion County|     5| 598.158|  0.000|   162| 19380.309| 205.083|   8,359|
| |Dawson County|     5| 191.512| 10.944|   486| 18614.984| 590.952|  26,108|
| |Fannin County|     5| 190.927| 10.910|   374| 14281.350| 212.747|  26,188|
| |Talbot County|     5| 807.103| 46.120|   147| 23728.814| 207.541|   6,195|
| |Heard County|     5| 419.358| 11.982|   152| 12748.469| 107.835|  11,923|
| |Lanier County|     5| 479.708| 13.706|   232| 22258.467| 178.177|  10,423|
| |Chattooga County|     4| 161.362|  5.763|   366| 14764.613| 570.530|  24,789|
| |Jones County|     4| 139.203|  4.972|   353| 12284.670| 218.748|  28,735|
| |Clinch County|     4| 604.412|  0.000|   217| 32789.362| 366.965|   6,618|
| |Gilmer County|     4| 127.514|  0.000|   685| 21836.845| 236.813|  31,369|
| |Twiggs County|     4| 492.611| 17.593|   139| 17118.227| 316.678|   8,120|
| |Taylor County|     4| 498.753| 35.625|   107| 13341.646| 338.440|   8,020|
| |Wilkes County|     3| 306.843|  0.000|   202| 20660.734| 131.504|   9,777|
| |Treutlen County|     3| 434.720|  0.000|   145| 21011.448| 331.215|   6,901|
| |Murray County|     3| 74.820|  3.563|   656| 16360.734| 171.018|  40,096|
| |Evans County|     3| 281.584| 26.818|   319| 29941.806| 777.709|  10,654|
| |Rabun County|     3| 175.060|  0.000|   234| 13654.665| 158.387|  17,137|
| |Pulaski County|     3| 269.372| 12.827|   143| 12840.083| 256.545|  11,137|
| |Charlton County|     3| 224.014|  0.000|   497| 37111.708| 640.041|  13,392|
| |Baker County|     3| 987.492|  0.000|    72| 23699.803| 423.211|   3,038|
| |Atkinson County|     3| 367.422| 17.496|   357| 43723.209| 647.362|   8,165|
| |Washington County|     3| 147.246|  7.012|   540| 26504.368| 427.716|  20,374|
| |Dodge County|     3| 145.596|  0.000|   254| 12327.105| 228.793|  20,605|
| |McIntosh County|     3| 208.652|  9.936|   213| 14814.300| 258.331|  14,378|
| |Echols County|     2| 499.251|  0.000|   226| 56415.377| 142.643|   4,006|
| |Clay County|     2| 705.716|  0.000|   103| 36344.390| 856.941|   2,834|
| |Chattahoochee County|     2| 183.368|  0.000|   810| 74264.234| 641.790|  10,907|
| |Dade County|     2| 124.100|  8.864|   157|  9741.871| 265.929|  16,116|
| |Towns County|     2| 166.154| 11.868|   159| 13209.271| 178.023|  12,037|
| |Jasper County|     2| 140.657| 10.047|   183| 12870.103| 190.891|  14,219|
| |Long County|     2| 102.255|  7.304|   149|  7617.976| 146.078|  19,559|
| |Montgomery County|     2| 218.055|  0.000|   180| 19624.945| 389.384|   9,172|
| |Wheeler County|     2| 254.615| 18.187|   107| 13621.897| 236.428|   7,855|
| |Warren County|     2| 380.662| 27.190|    92| 17510.468| 353.472|   5,254|
| |Webster County|     2| 767.165|  0.000|    40| 15343.306| 54.798|   2,607|
| |Tattnall County|     2| 79.095|  5.650|   603| 23847.188| 519.768|  25,286|
| |Glascock County|     1| 336.587| 48.084|    29|  9761.023| 192.335|   2,971|
| |Quitman County|     1| 434.972|  0.000|    32| 13919.095| 124.278|   2,299|
| |Morgan County|     1| 51.878|  7.411|   329| 17067.856| 370.557|  19,276|
| |Schley County|     1| 190.223|  0.000|    79| 15027.582| 298.921|   5,257|
| |Berrien County|     1| 51.554|  7.365|   338| 17425.375| 316.691|  19,397|
| |Irwin County|     1| 106.202|  0.000|   180| 19116.398| 197.233|   9,416|
| |Elbert County|     1| 52.100|  0.000|   386| 20110.451| 193.513|  19,194|
| |Miller County|     0|  0.000|  0.000|   164| 28681.357| 524.659|   5,718|
| |Taliaferro County|     0|  0.000|  0.000|    17| 11060.507| 371.782|   1,537|
| |Crawford County|     0|  0.000|  0.000|   120|  9674.299| 184.272|  12,404|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,505| 618.928| N/A|194,005| 26653.736| N/A|7,278,717|
| |Maricopa County| 2,596| 578.765|  7.644|129,562| 28885.182| 101.631|4,485,414|
| |Pima County|   531| 507.028|  5.729|19,743| 18851.710| 238.305|1,047,279|
| |Yuma County|   294| 1375.201|  3.341|11,886| 55597.394| 185.097| 213,787|
| |Navajo County|   208| 1875.158| 10.303| 5,455| 49177.815| 103.031| 110,924|
| |Mohave County|   184| 867.184| 10.772| 3,368| 15873.240| 111.764| 212,181|
| |Pinal County|   169| 365.177|  4.013| 8,777| 18965.446| 123.166| 462,789|
| |Apache County|   142| 1975.322|  5.962| 3,241| 45084.647| 93.401|  71,887|
| |Coconino County|   120| 836.377|  2.987| 3,188| 22219.744| 88.616| 143,476|
| |Yavapai County|    73| 310.507|  3.646| 2,160|  9187.619| 86.286| 235,099|
| |Cochise County|    57| 452.661|  5.672| 1,762| 13992.789| 171.308| 125,922|
| |Santa Cruz County|    55| 1182.847|  6.145| 2,705| 58174.545| 104.459|  46,498|
| |Gila County|    42| 777.519| 10.578| 1,002| 18549.372| 227.437|  54,018|
| |Graham County|    21| 540.721| 18.392|   609| 15680.923| 220.703|  38,837|
| |La Paz County|    12| 568.505|  0.000|   490| 23213.947| 87.983|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,456| 1249.829| N/A|51,033| 14313.855| N/A|3,565,287|
| |Hartford County| 1,420| 1592.428|  0.801|12,956| 14529.224| 24.992| 891,720|
| |Fairfield County| 1,411| 1495.762|  0.303|18,317| 19417.342| 42.706| 943,332|
| |New Haven County| 1,109| 1297.445|  0.501|13,378| 15651.232| 25.738| 854,757|
| |Middlesex County|   192| 1182.004|  0.000| 1,425|  8772.686| 17.589| 162,436|
| |Litchfield County|   139| 770.796|  0.792| 1,637|  9077.651| 17.428| 180,333|
| |New London County|   105| 395.919|  1.077| 1,499|  5652.210| 22.624| 265,206|
| |Tolland County|    65| 431.260|  0.000| 1,059|  7026.227|  2.843| 150,721|
| |Windham County|    15| 128.444|  0.000|   762|  6524.978| 29.359| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,403| 947.127| N/A|138,249| 29738.681| N/A|4,648,794|
| |Orleans Parish|   568| 1455.873|  2.197|11,027| 28263.923| 94.837| 390,144|
| |Jefferson Parish|   531| 1227.766|  0.661|15,815| 36567.066| 153.595| 432,493|
| |East Baton Rouge Parish|   384| 872.610| 11.037|12,875| 29257.440| 204.843| 440,059|
| |Caddo Parish|   300| 1248.938|  2.974| 6,949| 28929.577| 155.225| 240,204|
| |St. Tammany Parish|   221| 848.632|  3.840| 5,600| 21503.807| 183.221| 260,419|
| |Calcasieu Parish|   157| 771.741|  7.724| 7,045| 34630.056| 161.511| 203,436|
| |Rapides Parish|   128| 987.289| 15.426| 3,472| 26780.205| 185.117| 129,648|
| |Ouachita Parish|   117| 763.314|  3.728| 5,161| 33670.627| 246.982| 153,279|
| |Lafourche Parish|   105| 1075.665|  8.781| 3,014| 30876.719| 256.111|  97,614|
| |Lafayette Parish|   101| 413.274|  2.923| 7,976| 32636.360| 194.654| 244,390|
| |St. Landry Parish|    96| 1168.964| 10.437| 2,908| 35409.868| 300.939|  82,124|
| |St. John the Baptist Parish|    93| 2171.020|  3.335| 1,465| 34199.407| 116.722|  42,837|
| |Acadia Parish|    90| 1450.560| 11.512| 2,701| 43532.920| 230.248|  62,045|
| |Terrebonne Parish|    90| 814.767|  6.466| 3,212| 29078.136| 200.459| 110,461|
| |Bossier Parish|    84| 661.214|  3.374| 2,471| 19450.720| 148.436| 127,039|
| |Tangipahoa Parish|    83| 615.919|  6.361| 3,756| 27872.186| 273.506| 134,758|
| |Ascension Parish|    81| 639.790|  7.899| 3,084| 24359.420| 218.905| 126,604|
| |Iberia Parish|    79| 1131.319| 14.320| 2,627| 37619.934| 180.029|  69,830|
| |St. Mary Parish|    61| 1236.119| 17.369| 1,685| 34145.254| 214.222|  49,348|
| |Washington Parish|    59| 1277.222|  3.093| 1,346| 29137.983| 201.016|  46,194|
| |Livingston Parish|    57| 404.861|  6.088| 3,119| 22153.719| 183.659| 140,789|
| |St. Charles Parish|    54| 1016.949|  5.381| 1,545| 29096.045| 164.111|  53,100|
| |Iberville Parish|    51| 1568.700| 13.182| 1,288| 39617.360| 166.976|  32,511|
| |St. Martin Parish|    48| 898.355|  5.347| 1,790| 33501.151| 203.199|  53,431|
| |East Feliciana Parish|    40| 2090.410| 29.863|   637| 33289.783| 343.425|  19,135|
| |Avoyelles Parish|    37| 921.682| 17.793| 1,149| 28621.961| 281.131|  40,144|
| |West Baton Rouge Parish|    37| 1398.073|  0.000|   757| 28603.816| 188.929|  26,465|
| |Lincoln Parish|    35| 748.791| 12.225|   856| 18313.294| 155.871|  46,742|
| |Union Parish|    35| 1583.137| 12.924|   754| 34105.301| 297.242|  22,108|
| |Allen Parish|    33| 1287.704| 16.723| 1,382| 53927.498| 579.746|  25,627|
| |Pointe Coupee Parish|    33| 1518.638|  6.574|   850| 39116.429| 368.155|  21,730|
| |St. James Parish|    32| 1516.875|  0.000|   741| 35125.142| 148.979|  21,096|
| |Vernon Parish|    31| 653.609|  9.036|   814| 17162.496| 132.529|  47,429|
| |Bienville Parish|    30| 2265.690|  0.000|   399| 30133.676| 183.413|  13,241|
| |Jefferson Davis Parish|    30| 956.389|  9.108| 1,080| 34429.992| 236.820|  31,368|
| |Vermilion Parish|    30| 504.108|  9.602| 1,735| 29154.274| 362.478|  59,511|
| |De Soto Parish|    28| 1019.554| 10.404|   780| 28401.850| 275.696|  27,463|
| |Beauregard Parish|    27| 720.058| 34.288|   886| 23628.557| 194.301|  37,497|
| |St. Bernard Parish|    24| 508.001|  0.000| 1,141| 24151.215| 96.762|  47,244|
| |Grant Parish|    24| 1071.955| 38.284|   359| 16034.660| 338.176|  22,389|
| |Franklin Parish|    22| 1099.176| 28.550|   996| 49762.678| 413.975|  20,015|
| |Assumption Parish|    20| 913.617|  0.000|   616| 28139.418| 182.723|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   478| 20606.113| 110.852|  23,197|
| |Jackson Parish|    19| 1206.809|  9.074|   403| 25597.053| 244.991|  15,744|
| |Natchitoches Parish|    18| 471.723|  3.744|   843| 22092.353| 258.324|  38,158|
| |West Feliciana Parish|    18| 1156.218| 18.353|   408| 26207.605| 550.580|  15,568|
| |Webster Parish|    17| 443.401| 11.178|   949| 24752.217| 204.933|  38,340|
| |Evangeline Parish|    17| 509.058| 42.778|   966| 28926.486| 303.724|  33,395|
| |Red River Parish|    16| 1895.285| 67.689|   290| 34352.049| 896.876|   8,442|
| |Morehouse Parish|    14| 562.837| 11.486|   553| 22232.050| 126.351|  24,874|
| |Claiborne Parish|    12| 765.795|  9.117|   303| 19336.311| 237.032|  15,670|
| |Sabine Parish|    11| 460.559|  5.981|   705| 29517.669| 346.915|  23,884|
| |Concordia Parish|     9| 467.314|  0.000|   376| 19523.340| 311.543|  19,259|
| |Winn Parish|     9| 647.296| 20.549|   492| 35385.501| 688.394|  13,904|
| |West Carroll Parish|     8| 738.689| 26.382|   306| 28254.848| 158.290|  10,830|
| |Richland Parish|     8| 397.575|  0.000|   642| 31905.377| 283.982|  20,122|
| |Madison Parish|     6| 547.895|  0.000|   646| 58990.047| 430.489|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   321| 33810.828| 391.225|   9,494|
| |LaSalle Parish|     4| 268.601| 19.186|   350| 23502.552| 431.680|  14,892|
| |Caldwell Parish|     3| 302.480|  0.000|   245| 24702.561| 345.692|   9,918|
| |East Carroll Parish|     2| 291.503|  0.000|   525| 76519.458| 104.108|   6,861|
| |St. Helena Parish|     2| 197.394|  0.000|   294| 29016.976| 380.689|  10,132|
| |Tensas Parish|     0|  0.000|  0.000|   117| 26995.847| 922.935|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   174| 24953.392| 102.436|   6,973|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,832| 327.827| N/A|109,062|  9330.231| N/A|11,689,100|
| |Franklin County|   537| 407.820|  1.302|19,683| 14948.100| 130.190|1,316,756|
| |Cuyahoga County|   528| 427.505|  3.239|14,418| 11673.813| 89.989|1,235,072|
| |Lucas County|   329| 768.067|  2.001| 5,744| 13409.658| 122.397| 428,348|
| |Hamilton County|   270| 330.286|  2.621|10,184| 12457.904| 86.504| 817,473|
| |Mahoning County|   260| 1136.945|  3.748| 2,691| 11767.381| 78.087| 228,683|
| |Summit County|   228| 421.432|  1.320| 3,818|  7057.132| 64.693| 541,013|
| |Stark County|   143| 385.855|  1.542| 2,023|  5458.627| 68.999| 370,606|
| |Trumbull County|   112| 565.731|  3.608| 1,637|  8268.763| 74.324| 197,974|
| |Montgomery County|   105| 197.485|  2.956| 4,716|  8869.880| 85.442| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,937|  6251.755| 62.246| 309,833|
| |Butler County|    69| 180.094|  2.237| 3,218|  8399.150| 102.165| 383,134|
| |Portage County|    65| 400.084|  3.517|   791|  4868.711| 22.862| 162,466|
| |Columbiana County|    62| 608.541|  2.804| 1,729| 16970.446| 89.739| 101,883|
| |Wayne County|    60| 518.538|  2.469|   604|  5219.946| 74.077| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,162|  8882.638| 113.572| 130,817|
| |Licking County|    55| 310.977|  4.846| 1,431|  8091.054| 106.621| 176,862|
| |Allen County|    46| 449.434|  2.792|   888|  8676.027| 178.657| 102,351|
| |Geauga County|    46| 491.196|  3.051|   574|  6129.270| 24.407|  93,649|
| |Ashtabula County|    46| 473.051|  0.000|   588|  6046.832| 20.567|  97,241|
| |Marion County|    45| 691.319|  0.000| 2,966| 45565.575| 81.202|  65,093|
| |Lake County|    43| 186.835|  3.104| 1,187|  5157.528| 39.105| 230,149|
| |Pickaway County|    42| 718.477|  0.000| 2,421| 41415.057| 83.089|  58,457|
| |Warren County|    40| 170.502|  0.609| 1,962|  8363.100| 96.821| 234,602|
| |Miami County|    39| 364.530|  1.335|   921|  8608.523| 90.799| 106,987|
| |Medina County|    36| 200.283|  0.795| 1,002|  5574.533| 57.224| 179,746|
| |Fairfield County|    35| 222.118|  2.720| 1,514|  9608.184| 103.353| 157,574|
| |Erie County|    31| 417.418|  7.694|   637|  8577.276| 86.561|  74,266|
| |Darke County|    30| 586.935|  2.795|   476|  9312.699| 206.825|  51,113|
| |Ottawa County|    27| 666.255|  3.525|   413| 10191.240| 81.079|  40,525|
| |Belmont County|    26| 388.025|  0.000|   640|  9551.383| 40.508|  67,006|
| |Washington County|    22| 367.211|  0.000|   213|  3555.274| 19.076|  59,911|
| |Delaware County|    19| 90.832|  0.000| 1,434|  6855.438| 80.588| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    98|  7177.384| 52.313|  13,654|
| |Sandusky County|    17| 290.509|  0.000|   450|  7689.942| 161.123|  58,518|
| |Putnam County|    17| 502.053|  0.000|   227|  6703.878| 80.160|  33,861|
| |Clark County|    16| 119.329|  2.131| 1,261|  9404.623| 109.740| 134,083|
| |Mercer County|    14| 340.037|  3.470|   694| 16856.116| 239.414|  41,172|
| |Tuscarawas County|    14| 152.195|  0.000|   816|  8870.819| 43.484|  91,987|
| |Greene County|    13| 76.952|  0.846|   806|  4771.009| 87.099| 168,937|
| |Richland County|    12| 99.047|  0.000|   652|  5381.580| 51.882| 121,154|
| |Hardin County|    12| 382.592|  0.000|   189|  6025.825| 91.093|  31,365|
| |Clermont County|    11| 53.287|  0.000| 1,043|  5052.609| 70.588| 206,428|
| |Madison County|    10| 223.559|  0.000|   595| 13301.737| 661.095|  44,731|
| |Wyandot County|    10| 459.306| 13.123|   159|  7302.958| 72.177|  21,772|
| |Hocking County|     9| 318.426|  0.000|   126|  4457.968| 40.435|  28,264|
| |Knox County|     9| 144.411|  4.584|   225|  3610.282| 43.553|  62,322|
| |Coshocton County|     9| 245.902| 11.710|   203|  5546.448| 35.129|  36,600|
| |Auglaize County|     8| 175.223|  6.258|   301|  6592.781| 140.805|  45,656|
| |Guernsey County|     7| 180.064|  0.000|   121|  3112.540| 11.024|  38,875|
| |Holmes County|     7| 159.236|  3.250|   338|  7688.808| 32.497|  43,960|
| |Ross County|     6| 78.262|  3.727|   560|  7304.411| 130.436|  76,666|
| |Clinton County|     6| 142.966|  0.000|   186|  4431.948| 71.483|  41,968|
| |Huron County|     5| 85.813|  0.000|   420|  7208.320| 46.584|  58,266|
| |Lawrence County|     5| 84.086| 12.012|   355|  5970.099| 160.964|  59,463|
| |Carroll County|     5| 185.777|  0.000|   117|  4347.180| 37.155|  26,914|
| |Crawford County|     5| 120.499|  0.000|   183|  4410.276| 30.986|  41,494|
| |Seneca County|     4| 72.493|  2.589|   251|  4548.914| 75.082|  55,178|
| |Defiance County|     4| 105.023|  0.000|   172|  4515.977| 90.019|  38,087|
| |Shelby County|     4| 82.321|  0.000|   257|  5289.154| 167.583|  48,590|
| |Jefferson County|     3| 45.924|  2.187|   250|  3827.019| 34.990|  65,325|
| |Ashland County|     3| 56.092|  0.000|   162|  3028.943| 34.723|  53,484|
| |Perry County|     3| 83.024|  0.000|   180|  4981.458| 173.956|  36,134|
| |Williams County|     3| 81.762|  0.000|   142|  3870.053| 27.254|  36,692|
| |Hancock County|     3| 39.587|  0.000|   433|  5713.682| 101.794|  75,783|
| |Preble County|     2| 48.921|  0.000|   259|  6335.306| 192.191|  40,882|
| |Athens County|     2| 30.615|  2.187|   368|  5633.199| 19.681|  65,327|
| |Champaign County|     2| 51.434|  0.000|   205|  5271.956| 99.194|  38,885|
| |Morrow County|     2| 56.612|  0.000|   191|  5406.476| 76.831|  35,328|
| |Logan County|     2| 43.791|  0.000|   186|  4072.517| 96.965|  45,672|
| |Brown County|     2| 46.049|  0.000|   165|  3799.042| 88.809|  43,432|
| |Van Wert County|     2| 70.734|  5.052|    74|  2617.153| 10.105|  28,275|
| |Highland County|     2| 46.338|  3.310|   174|  4031.417| 49.648|  43,161|
| |Henry County|     2| 74.058|  0.000|   128|  4739.687| 58.188|  27,006|
| |Vinton County|     2| 152.847|  0.000|    33|  2521.972| 21.835|  13,085|
| |Gallia County|     2| 66.894|  4.778|    89|  2976.788| 114.676|  29,898|
| |Adams County|     2| 72.207|  0.000|    72|  2599.466| 56.734|  27,698|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723|  0.000|  15,040|
| |Muskingum County|     1| 11.599|  0.000|   267|  3096.909| 46.396|  86,215|
| |Fulton County|     1| 23.738|  0.000|   165|  3916.821| 61.041|  42,126|
| |Scioto County|     1| 13.278|  0.000|   274|  3638.102| 75.873|  75,314|
| |Union County|     1| 16.953|  0.000|   293|  4967.112| 94.450|  58,988|
| |Pike County|     0|  0.000|  0.000|    85|  3060.637| 41.151|  27,772|
| |Paulding County|     0|  0.000|  0.000|    75|  4016.710| 38.254|  18,672|
| |Noble County|     0|  0.000|  0.000|    20|  1386.578| 39.617|  14,424|
| |Morgan County|     0|  0.000|  0.000|    33|  2274.607| 49.234|  14,508|
| |Meigs County|     0|  0.000|  0.000|    69|  3012.180| 118.492|  22,907|
| |Jackson County|     0|  0.000|  0.000|    83|  2560.701| 35.259|  32,413|
| |Fayette County|     0|  0.000|  0.000|   134|  4697.634| 95.155|  28,525|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,632| 600.760| N/A|100,715| 16659.003| N/A|6,045,680|
| |Baltimore County| 1,018| 1230.405|  4.317|27,550| 33298.283| 249.672| 827,370|
| |Montgomery County|   810| 770.923|  0.952|19,071| 18150.964| 79.132|1,050,688|
| |Prince George's County|   768| 844.581|  2.042|24,719| 27183.840| 139.350| 909,327|
| |Anne Arundel County|   229| 395.350|  0.987| 7,700| 13293.419| 70.043| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,231| 12448.612| 82.011| 259,547|
| |Carroll County|   119| 706.454|  1.696| 1,613|  9575.712| 50.037| 168,447|
| |Howard County|   116| 356.167|  1.755| 4,089| 12554.883| 91.235| 325,690|
| |Charles County|    93| 569.654|  1.750| 2,175| 13322.553| 118.131| 163,257|
| |Harford County|    69| 270.121|  0.000| 2,167|  8483.368| 96.751| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,061|  9347.194| 78.030| 113,510|
| |Wicomico County|    45| 434.325|  0.000| 1,405| 13560.598| 78.592| 103,609|
| |Washington County|    31| 205.231|  0.000| 1,138|  7533.979| 113.492| 151,049|
| |Cecil County|    30| 291.673|  0.000|   736|  7155.705| 41.668| 102,855|
| |Calvert County|    28| 302.621|  0.000|   742|  8019.454| 54.039|  92,525|
| |Queen Anne's County|    26| 516.068|  2.836|   487|  9666.342| 150.283|  50,381|
| |Kent County|    23| 1184.224|  0.000|   246| 12666.049| 22.066|  19,422|
| |Worcester County|    20| 382.585|  0.000|   731| 13983.472| 101.112|  52,276|
| |Allegany County|    19| 269.825|  2.029|   343|  4871.052| 89.265|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   413| 12934.949| 170.020|  31,929|
| |Talbot County|     4| 107.582|  0.000|   421| 11322.988| 73.002|  37,181|
| |Somerset County|     3| 117.114|  0.000|   154|  6011.868| 83.653|  25,616|
| |Caroline County|     3| 89.804|  0.000|   465| 13919.655| 51.317|  33,406|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    58|  1999.035| 44.314|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,926| 434.626| N/A|81,006| 12032.585| N/A|6,732,219|
| |Marion County|   735| 761.988|  1.481|16,706| 17319.419| 110.040| 964,582|
| |Lake County|   284| 584.972|  2.648| 8,171| 16830.315| 158.602| 485,493|
| |Allen County|   166| 437.649|  1.130| 4,314| 11373.613| 141.991| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,848| 11683.853| 73.160| 158,167|
| |Hendricks County|   109| 640.006|  0.839| 2,018| 11848.912| 98.140| 170,311|
| |Hamilton County|   105| 310.641|  0.423| 3,169|  9375.435| 154.686| 338,011|
| |Elkhart County|    92| 445.864|  4.846| 5,153| 24973.224| 186.931| 206,341|
| |St. Joseph County|    85| 312.700|  1.577| 3,884| 14288.552| 177.635| 271,826|
| |Madison County|    66| 509.381|  1.103| 1,106|  8535.992| 131.204| 129,569|
| |Howard County|    61| 739.000|  0.000|   982| 11896.685| 133.262|  82,544|
| |Delaware County|    53| 464.362|  1.252|   806|  7061.813| 85.112| 114,135|
| |Floyd County|    50| 636.764|  7.277|   902| 11487.227| 201.945|  78,522|
| |Clark County|    50| 422.647|  3.623| 1,421| 12011.631| 213.739| 118,302|
| |Bartholomew County|    47| 561.000|  0.000|   924| 11029.017| 209.735|  83,779|
| |Boone County|    46| 678.036|  0.000|   740| 10907.537| 120.025|  67,843|
| |Hancock County|    41| 524.511|  5.483|   720|  9210.930| 91.378|  78,168|
| |Porter County|    39| 228.888|  0.000| 1,469|  8621.449| 109.833| 170,389|
| |Morgan County|    35| 496.531|  2.027|   512|  7263.545| 58.773|  70,489|
| |Greene County|    34| 1065.096|  0.000|   273|  8552.096| 98.454|  31,922|
| |Monroe County|    33| 222.326|  2.887|   804|  5416.658| 43.310| 148,431|
| |Decatur County|    32| 1204.865|  0.000|   359| 13517.075| 112.956|  26,559|
| |Grant County|    30| 456.142|  0.000|   544|  8271.374| 34.754|  65,769|
| |LaPorte County|    30| 273.005|  0.000| 1,010|  9191.176| 115.702| 109,888|
| |Warrick County|    30| 476.206|  0.000|   633| 10047.938| 106.579|  62,998|
| |Noble County|    29| 607.406|  0.000|   741| 15520.275| 170.552|  47,744|
| |Shelby County|    28| 625.992|  3.194|   582| 13011.693| 76.652|  44,729|
| |Dearborn County|    28| 566.137|  0.000|   536| 10837.478| 80.877|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   368|  8111.087| 56.677|  45,370|
| |Orange County|    24| 1221.623|  0.000|   193|  9823.883| 145.431|  19,646|
| |Harrison County|    24| 592.373|  3.526|   389|  9601.382| 169.249|  40,515|
| |Marshall County|    23| 497.211|  3.088|   814| 17596.956| 74.118|  46,258|
| |Daviess County|    21| 629.666|  4.283|   320|  9594.915| 201.322|  33,351|
| |Henry County|    21| 437.755|  2.978|   504| 10506.129| 354.373|  47,972|
| |Montgomery County|    21| 547.759|  0.000|   370|  9650.999| 59.620|  38,338|
| |Franklin County|    19| 834.871| 31.386|   253| 11116.970| 62.772|  22,758|
| |Tipton County|    17| 1122.260| 56.585|   164| 10826.512| 198.046|  15,148|
| |Vanderburgh County|    15| 82.667|  1.575| 2,200| 12124.485| 159.823| 181,451|
| |Vigo County|    13| 121.452|  4.004|   860|  8034.530| 256.251| 107,038|
| |Perry County|    13| 678.178|  7.453|   194| 10120.507| 59.620|  19,169|
| |Dubois County|    13| 304.193|  3.343|   747| 17479.408| 157.111|  42,736|
| |Jennings County|    12| 432.666|  0.000|   237|  8545.160| 56.659|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   886| 11150.826| 43.151|  79,456|
| |Tippecanoe County|    12| 61.308|  0.730| 1,352|  6907.404| 95.612| 195,732|
| |White County|    11| 456.394|  5.927|   397| 16471.662| 148.180|  24,102|
| |Newton County|    10| 715.103|  0.000|   122|  8724.256| 40.863|  13,984|
| |LaGrange County|    10| 252.436|  0.000|   574| 14489.827| 54.093|  39,614|
| |Scott County|    10| 418.883|  0.000|   290| 12147.614| 131.649|  23,873|
| |Wayne County|    10| 151.782|  0.000|   435|  6602.514| 125.762|  65,884|
| |Cass County|     9| 238.796|  0.000| 1,820| 48289.952| 90.970|  37,689|
| |Ripley County|     8| 282.446|  5.044|   226|  7979.099| 90.786|  28,324|
| |Putnam County|     8| 212.902|  0.000|   343|  9128.167| 201.496|  37,576|
| |Carroll County|     7| 345.560| 35.261|   230| 11354.100| 260.933|  20,257|
| |Fayette County|     7| 303.004|  0.000|   223|  9652.844| 204.064|  23,102|
| |Ohio County|     7| 1191.489| 48.632|    68| 11574.468| 72.948|   5,875|
| |Starke County|     7| 304.414|  0.000|   186|  8088.715| 49.700|  22,995|
| |Whitley County|     6| 176.658|  0.000|   170|  5005.300| 67.298|  33,964|
| |Randolph County|     5| 202.716|  5.792|   138|  5594.973| 86.878|  24,665|
| |Jackson County|     5| 113.043|  0.000|   632| 14288.621| 142.111|  44,231|
| |Clay County|     5| 190.658|  0.000|   175|  6673.022| 277.816|  26,225|
| |Wabash County|     5| 161.311|  9.218|   184|  5936.250| 64.524|  30,996|
| |DeKalb County|     4| 92.007|  0.000|   254|  5842.438| 62.433|  43,475|
| |Rush County|     4| 241.240|  0.000|   105|  6332.549| 215.393|  16,581|
| |Clinton County|     4| 123.461|  4.409|   478| 14753.542| 167.554|  32,399|
| |Gibson County|     4| 118.839|  0.000|   249|  7397.724| 89.129|  33,659|
| |Steuben County|     3| 86.720|  0.000|   225|  6504.018| 57.813|  34,594|
| |Spencer County|     3| 147.951|  0.000|   141|  6953.691| 35.226|  20,277|
| |Huntington County|     3| 82.147|  0.000|   137|  3751.369| 50.853|  36,520|
| |Knox County|     3| 81.981| 11.712|   196|  5356.069| 144.442|  36,594|
| |Wells County|     2| 70.681|  0.000|   183|  6467.345| 60.584|  28,296|
| |Fulton County|     2| 100.130|  0.000|   180|  9011.715| 78.674|  19,974|
| |Adams County|     2| 55.902|  0.000|   139|  3885.178| 147.741|  35,777|
| |Blackford County|     2| 170.097|  0.000|    67|  5698.248| 24.300|  11,758|
| |Brown County|     2| 132.521|  9.466|    79|  5234.561| 47.329|  15,092|
| |Fountain County|     2| 122.354|  0.000|    76|  4649.456| 17.479|  16,346|
| |Jasper County|     2| 59.591|  0.000|   272|  8104.404| 114.926|  33,562|
| |Jefferson County|     2| 61.904|  0.000|   184|  5695.184| 84.013|  32,308|
| |Miami County|     2| 56.313|  0.000|   286|  8052.709| 48.268|  35,516|
| |Washington County|     1| 35.668|  0.000|   162|  5778.285| 101.910|  28,036|
| |Warren County|     1| 120.992|  0.000|    27|  3266.788| 69.138|   8,265|
| |Sullivan County|     1| 48.382|  0.000|   193|  9337.655| 407.788|  20,669|
| |Pulaski County|     1| 80.952|  0.000|    86|  6961.872| 34.694|  12,353|
| |Parke County|     1| 59.042|  0.000|    64|  3778.709| 101.215|  16,937|
| |Owen County|     1| 48.079|  0.000|   115|  5529.112| 164.843|  20,799|
| |Vermillion County|     0|  0.000|  0.000|    68|  4387.663| 119.831|  15,498|
| |Union County|     0|  0.000|  0.000|    47|  6662.886| 121.512|   7,054|
| |Posey County|     0|  0.000|  0.000|   190|  7472.372| 73.038|  25,427|
| |Pike County|     0|  0.000|  0.000|    73|  5892.324| 196.026|  12,389|
| |Martin County|     0|  0.000|  0.000|    56|  5460.751| 153.235|  10,255|
| |Jay County|     0|  0.000|  0.000|   102|  4991.192| 69.905|  20,436|
| |Crawford County|     0|  0.000|  0.000|    52|  4916.328| 94.545|  10,577|
| |Benton County|     0|  0.000|  0.000|    69|  7887.517| 114.312|   8,748|
| |Switzerland County|     0|  0.000|  0.000|    60|  5580.876| 106.302|  10,751|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,385| 279.421| N/A|107,421| 12585.175| N/A|8,535,519|
| |Fairfax County|   542| 472.318|  0.747|17,173| 14965.160| 79.425|1,147,532|
| |Henrico County|   187| 565.265|  0.864| 4,149| 12541.639| 105.798| 330,818|
| |Prince William County|   178| 378.454|  0.607| 9,924| 21099.854| 123.924| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,246| 13705.339| 93.492| 236,842|
| |Loudoun County|   115| 278.088|  0.000| 5,528| 13367.574| 76.690| 413,538|
| |Chesterfield County|    80| 226.756|  0.000| 4,623| 13103.667| 102.445| 352,802|
| |Alexandria city|    61| 382.618|  0.896| 3,130| 19632.687| 137.993| 159,428|
| |Virginia Beach city|    55| 122.229|  0.317| 5,444| 12098.477| 125.087| 449,974|
| |Suffolk city|    53| 575.411|  4.653| 1,438| 15612.108| 218.687|  92,108|
| |Shenandoah County|    47| 1077.586|  9.826|   743| 17035.033| 85.159|  43,616|
| |Richmond County|    46| 5098.083| 15.833| 3,731| 413498.836| 3483.162|   9,023|
| |Chesapeake city|    41| 167.460|  2.334| 3,303| 13490.718| 206.553| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,621| 11900.305| 127.949| 136,215|
| |Norfolk city|    34| 140.066|  1.177| 4,002| 16486.640| 175.966| 242,742|
| |Hanover County|    33| 306.219|  1.326|   703|  6523.393| 66.281| 107,766|
| |Mecklenburg County|    32| 1046.196|  0.000|   459| 15006.375| 60.717|  30,587|
| |Harrisonburg city|    31| 584.729|  0.000| 1,106| 20861.627| 72.754|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   299| 25533.732| 36.599|  11,710|
| |Galax city|    27| 4253.978| 67.523|   354| 55774.382| 157.555|   6,347|
| |Page County|    25| 1045.938|  0.000|   353| 14768.639| 41.838|  23,902|
| |Portsmouth city|    25| 264.836|  0.000| 1,995| 21133.922| 313.263|  94,398|
| |Manassas city|    22| 535.475|  0.000| 1,716| 41767.068| 187.764|  41,085|
| |Colonial Heights city|    22| 1266.552|  8.224|   207| 11917.098| 82.244|  17,370|
| |Newport News city|    20| 111.592|  1.594| 1,993| 11120.100| 116.374| 179,225|
| |Rockingham County|    20| 244.057|  1.743|   979| 11946.600| 57.528|  81,948|
| |Petersburg city|    19| 606.138|  0.000|   544| 17354.686| 109.378|  31,346|
| |Roanoke County|    19| 201.728|  0.000| 1,604| 17030.132| 141.058|  94,186|
| |Accomack County|    17| 526.055|  4.421| 1,127| 34874.366| 110.516|  32,316|
| |James City County|    17| 222.155|  1.867|   651|  8507.246| 63.473|  76,523|
| |Albemarle County|    16| 146.346|  0.000|   913|  8350.864| 92.773| 109,330|
| |Charlottesville city|    15| 317.353|  0.000|   560| 11847.840| 51.381|  47,266|
| |Emporia city|    15| 2805.836|  0.000|   192| 35914.703| 374.111|   5,346|
| |Carroll County|    14| 469.941|  4.795|   344| 11547.112| 47.953|  29,791|
| |Nottoway County|    14| 919.118|  9.379|   183| 12014.181|  9.379|  15,232|
| |Southampton County|    13| 737.338|  0.000|   309| 17525.949| 340.310|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,041| 19788.993| 89.617|  52,605|
| |Greensville County|    11| 970.360|  0.000|   572| 50458.716| 970.360|  11,336|
| |Stafford County|    10| 65.410|  0.934| 1,506|  9850.735| 113.066| 152,882|
| |Prince Edward County|    10| 438.558|  0.000|   449| 19691.255| 244.339|  22,802|
| |Frederick County|    10| 111.966|  1.600|   701|  7848.801| 31.990|  89,313|
| |Danville city|     9| 224.753|  7.135|   477| 11911.897| 235.455|  40,044|
| |Fluvanna County|     9| 330.033|  0.000|   203|  7444.078| 52.386|  27,270|
| |Fauquier County|     9| 126.365|  0.000|   642|  9014.069| 44.128|  71,222|
| |Hampton city|     9| 66.910|  2.124| 1,349| 10028.994| 110.454| 134,510|
| |Henry County|     9| 178.017|  5.651|   672| 13291.928| 228.879|  50,557|
| |Isle of Wight County|     9| 242.529|  0.000|   437| 11776.119| 192.483|  37,109|
| |Sussex County|     9| 806.524|  0.000|   317| 28407.563| 128.020|  11,159|
| |Bedford County|     8| 101.270|  1.808|   418|  5291.340| 103.078|  78,997|
| |Buckingham County|     8| 466.527|  0.000|   620| 36155.820| 124.963|  17,148|
| |Manassas Park city|     7| 400.503|  0.000|   538| 30781.554| 187.991|  17,478|
| |Dinwiddie County|     7| 245.235|  0.000|   240|  8408.072| 95.091|  28,544|
| |Botetourt County|     7| 209.462|  0.000|   223|  6672.851| 34.198|  33,419|
| |Franklin County|     7| 124.906|  0.000|   394|  7030.441| 94.317|  56,042|
| |Goochland County|     7| 294.700|  0.000|   173|  7283.291| 54.129|  23,753|
| |Washington County|     6| 111.649|  2.658|   288|  5359.137| 146.207|  53,740|
| |Warren County|     6| 149.388|  0.000|   367|  9137.536| 42.682|  40,164|
| |Williamsburg city|     6| 401.230|  0.000|   136|  9094.557| 76.425|  14,954|
| |Falls Church city|     6| 410.481|  0.000|    63|  4310.050| 19.547|  14,617|
| |Lynchburg city|     5| 60.851|  0.000|   735|  8945.088| 187.769|  82,168|
| |Hopewell city|     5| 221.936|  0.000|   297| 13183.009| 158.526|  22,529|
| |Grayson County|     5| 321.543|  0.000|   165| 10610.932| 73.496|  15,550|
| |Caroline County|     5| 162.734|  0.000|   229|  7453.214| 69.743|  30,725|
| |Patrick County|     5| 283.962|  8.113|   176|  9995.457| 146.038|  17,608|
| |Wise County|     5| 133.751|  7.643|   244|  6527.031| 393.609|  37,383|
| |Charles City County|     5| 718.081|  0.000|    56|  8042.510| 82.066|   6,963|
| |Winchester city|     4| 142.460|  0.000|   421| 14993.945| 111.933|  28,078|
| |Alleghany County|     4| 269.179|  0.000|    60|  4037.685|  0.000|  14,860|
| |Fredericksburg city|     4| 137.760|  0.000|   428| 14740.322| 108.240|  29,036|
| |Augusta County|     4| 52.939|  0.000|   313|  4142.513| 62.393|  75,558|
| |York County|     4| 58.582|  0.000|   409|  5990.041| 75.320|  68,280|
| |Powhatan County|     4| 134.898|  0.000|   167|  5631.998| 96.356|  29,652|
| |King George County|     4| 149.054|  0.000|   169|  6297.511| 127.760|  26,836|
| |Campbell County|     3| 54.660|  2.603|   253|  4609.638| 104.114|  54,885|
| |Northumberland County|     3| 248.036| 11.811|    81|  6696.982| 82.679|  12,095|
| |Montgomery County|     3| 30.446|  0.000|   332|  3369.361| 39.145|  98,535|
| |Orange County|     3| 80.969|  0.000|   236|  6369.599| 19.278|  37,051|
| |Smyth County|     3| 99.655|  0.000|   171|  5680.308| 99.655|  30,104|
| |Wythe County|     3| 104.588|  0.000|   127|  4427.555| 59.765|  28,684|
| |Waynesboro city|     3| 132.567|  0.000|   195|  8616.880| 132.567|  22,630|
| |Salem city|     3| 118.572|  0.000|   170|  6719.102| 50.817|  25,301|
| |Martinsville city|     3| 238.968|  0.000|   241| 19197.069| 330.003|  12,554|
| |Russell County|     3| 112.841|  5.373|   157|  5905.364| 155.829|  26,586|
| |Scott County|     3| 139.108|  0.000|   120|  5564.314| 119.235|  21,566|
| |Pulaski County|     3| 88.165|  0.000|    91|  2674.347|  8.397|  34,027|
| |Westmoreland County|     3| 166.528|  0.000|   217| 12045.518| 47.579|  18,015|
| |Gloucester County|     2| 53.550|  0.000|   179|  4792.760| 68.851|  37,348|
| |Floyd County|     2| 126.992|  0.000|   114|  7238.555| 353.764|  15,749|
| |Amelia County|     2| 152.149|  0.000|    85|  6466.337| 65.207|  13,145|
| |Halifax County|     2| 58.978|  4.213|   170|  5013.123| 58.978|  33,911|
| |Greene County|     2| 100.913|  0.000|   179|  9031.737| 93.705|  19,819|
| |Brunswick County|     2| 123.221|  0.000|   248| 15279.404| 158.427|  16,231|
| |Rappahannock County|     2| 271.370|  0.000|    46|  6241.520| 58.151|   7,370|
| |Surry County|     2| 311.429|  0.000|    52|  8097.166|  0.000|   6,422|
| |Pittsylvania County|     2| 33.138|  0.000|   571|  9460.848| 184.625|  60,354|
| |Prince George County|     2| 52.147|  0.000|   459| 11967.773| 279.360|  38,353|
| |King William County|     2| 116.632|  0.000|   105|  6123.163| 124.963|  17,148|
| |Lee County|     2| 85.386|  6.099|   150|  6403.962| 176.871|  23,423|
| |Louisa County|     2| 53.204|  0.000|   209|  5559.841| 98.808|  37,591|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648|  0.000|   7,025|
| |Amherst County|     1| 31.641|  4.520|   217|  6866.002| 185.323|  31,605|
| |Essex County|     1| 91.299|  0.000|   109|  9951.611| 78.256|  10,953|
| |Dickenson County|     1| 69.842|  0.000|    52|  3631.792| 89.797|  14,318|
| |Buchanan County|     1| 47.610|  6.801|    84|  3999.238| 27.206|  21,004|
| |Lunenburg County|     1| 81.994|  0.000|    70|  5739.587| 93.708|  12,196|
| |Madison County|     1| 75.409|  0.000|    76|  5731.091| 75.409|  13,261|
| |Middlesex County|     1| 94.500|  0.000|    52|  4914.005| 135.000|  10,582|
| |New Kent County|     1| 43.307|  0.000|   136|  5889.741| 43.307|  23,091|
| |Buena Vista city|     1| 154.369|  0.000|    65| 10033.961| 330.790|   6,478|
| |Bristol city|     1| 59.659|  8.523|   100|  5965.875| 170.454|  16,762|
| |Rockbridge County|     1| 44.301|  0.000|    80|  3544.057| 69.615|  22,573|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Radford city|     0|  0.000|  0.000|    68|  3726.232| 109.595|  18,249|
| |Poquoson city|     0|  0.000|  0.000|    48|  3911.662| 46.567|  12,271|
| |Norton city|     0|  0.000|  0.000|    23|  5777.443| 143.539|   3,981|
| |Lexington city|     0|  0.000|  0.000|    37|  4969.111| 76.743|   7,446|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418|  0.000|   5,538|
| |Nelson County|     0|  0.000|  0.000|    70|  4688.547| 200.938|  14,930|
| |Mathews County|     0|  0.000|  0.000|    23|  2603.577| 80.856|   8,834|
| |Lancaster County|     0|  0.000|  0.000|    49|  4621.334| 121.259|  10,603|
| |Staunton city|     0|  0.000|  0.000|   159|  6377.346| 40.109|  24,932|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Giles County|     0|  0.000|  0.000|    33|  1973.684| 76.897|  16,720|
| |Cumberland County|     0|  0.000|  0.000|    84|  8457.511| 115.068|   9,932|
| |Appomattox County|     0|  0.000|  0.000|   103|  6473.509| 143.656|  15,911|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726|  0.000|   2,190|
| |Tazewell County|     0|  0.000|  0.000|   131|  3226.998| 42.229|  40,595|
| |Craig County|     0|  0.000|  0.000|    19|  3702.982| 55.684|   5,131|
| |Bland County|     0|  0.000|  0.000|    37|  5891.720| 409.463|   6,280|
| |Charlotte County|     0|  0.000|  0.000|    58|  4882.155| 60.125|  11,880|
| |Clarke County|     0|  0.000|  0.000|    74|  5061.906| 29.316|  14,619|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,348| 223.873| N/A|145,516| 13874.412| N/A|10,488,084|
| |Mecklenburg County|   258| 232.358|  3.345|23,164| 20861.778| 109.231|1,110,356|
| |Wake County|   183| 164.604|  1.670|12,754| 11471.890| 82.752|1,111,761|
| |Guilford County|   158| 294.132|  0.532| 5,974| 11121.164| 80.846| 537,174|
| |Durham County|    79| 245.732|  0.000| 6,428| 19994.525| 101.315| 321,488|
| |Gaston County|    57| 253.865|  3.181| 3,579| 15940.034| 152.701| 224,529|
| |Robeson County|    56| 428.708|  3.281| 3,039| 23265.072| 242.789| 130,625|
| |Henderson County|    56| 476.933|  2.433| 1,568| 13354.114| 94.900| 117,417|
| |Forsyth County|    56| 146.484|  1.495| 5,561| 14546.358| 102.763| 382,295|
| |Cumberland County|    56| 166.911|  2.129| 3,434| 10235.195| 115.816| 335,509|
| |Chatham County|    55| 738.552|  5.755| 1,363| 18302.672| 111.262|  74,470|
| |Buncombe County|    54| 206.745|  3.829| 2,092|  8009.464| 106.107| 261,191|
| |Rowan County|    51| 358.932|  3.016| 2,367| 16658.690| 162.877| 142,088|
| |Cabarrus County|    50| 230.997|  0.000| 2,809| 12977.413| 118.138| 216,453|
| |Duplin County|    49| 834.170|  2.432| 2,025| 34473.366| 24.320|  58,741|
| |Orange County|    48| 323.285|  0.962| 1,475|  9934.265| 117.383| 148,476|
| |Columbus County|    48| 864.740|  0.000|   973| 17529.005| 169.860|  55,508|
| |Johnston County|    45| 214.962|  0.000| 3,444| 16451.784| 88.032| 209,339|
| |Union County|    44| 183.441|  0.596| 3,384| 14108.289| 163.787| 239,859|
| |Wayne County|    42| 341.100|  0.000| 2,532| 20563.465| 125.302| 123,131|
| |Alamance County|    42| 247.774|  0.843| 2,653| 15651.086| 152.541| 169,509|
| |Vance County|    41| 920.624|  0.000|   820| 18412.485| 137.933|  44,535|
| |Harnett County|    40| 294.170|  1.051| 1,414| 10398.894| 116.617| 135,976|
| |Randolph County|    39| 271.461|  1.989| 2,256| 15702.980| 75.572| 143,667|
| |Wilson County|    36| 440.092|  1.746| 1,563| 19107.346| 85.574|  81,801|
| |Catawba County|    33| 206.830|  3.581| 2,266| 14202.355| 128.038| 159,551|
| |Stanly County|    31| 493.583| 11.373| 1,237| 19695.570| 368.482|  62,806|
| |Granville County|    29| 479.791|  4.727| 1,360| 22500.538| 267.076|  60,443|
| |Burke County|    27| 298.392|  0.000| 1,716| 18964.469|  0.000|  90,485|
| |Franklin County|    26| 373.108|  0.000|   932| 13374.471| 125.053|  69,685|
| |Cleveland County|    24| 245.030|  5.834| 1,332| 13599.191| 202.734|  97,947|
| |Haywood County|    24| 385.128| 27.509|   463|  7429.754| 64.188|  62,317|
| |Davidson County|    23| 137.224|  4.262| 1,886| 11252.379| 79.266| 167,609|
| |Brunswick County|    22| 154.040|  1.000| 1,312|  9186.388| 53.014| 142,820|
| |New Hanover County|    21| 89.563|  0.609| 2,710| 11557.834| 48.742| 234,473|
| |Pasquotank County|    20| 502.210|  0.000|   456| 11450.382| 193.709|  39,824|
| |Moore County|    20| 198.255|  0.000| 1,105| 10953.608| 123.202| 100,880|
| |McDowell County|    20| 437.101| 18.733|   714| 15604.511| 96.787|  45,756|
| |Sampson County|    19| 299.067| 11.243| 1,518| 23893.847| 15.740|  63,531|
| |Wilkes County|    18| 263.112| 14.617|   914| 13360.229| 148.261|  68,412|
| |Craven County|    18| 176.230|  8.392|   785|  7685.605| 44.757| 102,139|
| |Iredell County|    17| 93.506|  0.000| 2,013| 11072.242| 84.863| 181,806|
| |Montgomery County|    16| 588.820| 10.515|   714| 26276.083| 352.240|  27,173|
| |Northampton County|    16| 821.229|  0.000|   319| 16373.248|  0.000|  19,483|
| |Pitt County|    14| 77.458|  2.371| 2,308| 12769.583| 214.987| 180,742|
| |Rutherford County|    14| 208.865|  0.000|   837| 12487.132| 181.158|  67,029|
| |Nash County|    14| 148.466|  3.030| 1,335| 14157.246| 213.609|  94,298|
| |Edgecombe County|    13| 252.565|  0.000|   745| 14473.889| 247.014|  51,472|
| |Caldwell County|    13| 158.193|  0.000| 1,283| 15612.451| 118.210|  82,178|
| |Onslow County|    12| 60.625|  1.443| 1,208|  6102.921| 93.103| 197,938|
| |Lenoir County|    11| 196.608|  0.000|   646| 11546.230| 120.007|  55,949|
| |Hertford County|    11| 464.586|  0.000|   404| 17062.973| 331.847|  23,677|
| |Lee County|    11| 178.054|  0.000| 1,339| 21674.032| 99.433|  61,779|
| |Hoke County|    11| 199.153|  5.173|   782| 14157.946| 160.357|  55,234|
| |Surry County|    10| 139.309|  0.000| 1,007| 14028.391| 101.496|  71,783|
| |Lincoln County|    10| 116.129|  1.659|   933| 10834.853| 137.696|  86,111|
| |Richmond County|     9| 200.763|  0.000|   569| 12692.677| 152.962|  44,829|
| |Halifax County|     8| 159.968|  5.713|   755| 15096.981| 142.829|  50,010|
| |Jackson County|     7| 159.315|  6.503|   460| 10469.298| 29.262|  43,938|
| |Bladen County|     7| 213.923|  0.000|   653| 19955.993| 122.242|  32,722|
| |Warren County|     6| 304.090|  0.000|   271| 13734.732| 94.123|  19,731|
| |Rockingham County|     6| 65.927|  0.000|   594|  6526.755| 42.382|  91,010|
| |Polk County|     6| 289.519|  6.893|   182|  8782.088| 124.080|  20,724|
| |Martin County|     6| 267.380|  0.000|   285| 12700.535| 152.788|  22,440|
| |Yadkin County|     6| 159.291|  0.000|   565| 14999.867| 87.231|  37,667|
| |Carteret County|     5| 71.970|  0.000|   381|  5484.145| 10.281|  69,473|
| |Bertie County|     5| 263.894|  0.000|   323| 17047.554| 361.912|  18,947|
| |Davie County|     5| 116.697|  0.000|   439| 10245.997| 26.674|  42,846|
| |Scotland County|     5| 143.583| 12.307|   436| 12520.461| 291.269|  34,823|
| |Washington County|     4| 345.423|  0.000|   144| 12435.233| 135.702|  11,580|
| |Jones County|     4| 424.674|  0.000|   114| 12103.196| 318.505|   9,419|
| |Cherokee County|     4| 139.801|  0.000|   294| 10275.409| 19.972|  28,612|
| |Pender County|     3| 47.574|  0.000|   696| 11037.108| 83.820|  63,060|
| |Mitchell County|     3| 200.481|  9.547|    80|  5346.164|  0.000|  14,964|
| |Stokes County|     3| 65.802|  0.000|   303|  6646.049| 21.934|  45,591|
| |Greene County|     3| 142.389|  0.000|   343| 16279.842| 81.365|  21,069|
| |Anson County|     3| 122.719|  0.000|   377| 15421.746| 286.345|  24,446|
| |Dare County|     2| 54.041|  0.000|   215|  5809.398| 19.300|  37,009|
| |Gates County|     2| 172.980|  0.000|    57|  4929.943| 135.913|  11,562|
| |Tyrrell County|     2| 498.008| 35.572|   103| 25647.410| 177.860|   4,016|
| |Swain County|     2| 140.144|  0.000|   121|  8478.733| 20.021|  14,271|
| |Person County|     2| 50.646|  0.000|   247|  6254.748| 86.821|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    93|  6907.821| 63.667|  13,463|
| |Chowan County|     2| 143.441| 10.246|   167| 11977.336| 102.458|  13,943|
| |Beaufort County|     2| 42.559|  0.000|   460|  9788.484| 97.277|  46,994|
| |Macon County|     2| 55.776|  0.000|   480| 13386.134| 39.840|  35,858|
| |Alexander County|     2| 53.338|  0.000|   342|  9120.730| 148.583|  37,497|
| |Caswell County|     2| 88.480|  0.000|   203|  8980.711| 44.240|  22,604|
| |Camden County|     2| 184.043|  0.000|    78|  7177.694| 65.730|  10,867|
| |Madison County|     1| 45.966|  6.567|    49|  2252.356| 26.267|  21,755|
| |Pamlico County|     1| 78.579|  0.000|    74|  5814.867| 22.451|  12,726|
| |Ashe County|     1| 36.761|  0.000|   174|  6396.353| 84.024|  27,203|
| |Clay County|     1| 89.039| 12.720|    76|  6766.984|  0.000|  11,231|
| |Transylvania County|     1| 29.082|  0.000|   161|  4682.274| 66.474|  34,385|
| |Yancey County|     0|  0.000|  0.000|    80|  4427.472|  0.000|  18,069|
| |Watauga County|     0|  0.000|  0.000|   344|  6123.503| 71.204|  56,177|
| |Hyde County|     0|  0.000|  0.000|    58| 11748.025| 376.168|   4,937|
| |Graham County|     0|  0.000|  0.000|    49|  5804.999| 169.242|   8,441|
| |Currituck County|     0|  0.000|  0.000|    83|  2989.590| 51.456|  27,763|
| |Avery County|     0|  0.000|  0.000|   108|  6151.393|  0.000|  17,557|
| |Alleghany County|     0|  0.000|  0.000|   180| 16162.342| 141.100|  11,137|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,288| 444.383| N/A|106,953| 20772.760| N/A|5,148,714|
| |Greenville County|   229| 437.405|  5.730|11,277| 21539.819| 75.311| 523,542|
| |Charleston County|   214| 520.167|  6.250|12,911| 31382.624| 185.427| 411,406|
| |Richland County|   170| 408.891|  5.841| 9,404| 22618.873| 195.168| 415,759|
| |Horry County|   169| 477.292|  5.245| 8,889| 25104.425| 106.513| 354,081|
| |Florence County|   131| 947.264| 15.495| 3,791| 27412.812| 321.264| 138,293|
| |Lexington County|   121| 405.021|  4.782| 5,235| 17523.013| 121.937| 298,750|
| |Spartanburg County|   115| 359.617|  5.361| 4,400| 13759.244| 134.019| 319,785|
| |Orangeburg County|    78| 905.135| 21.551| 2,596| 30124.746| 256.952|  86,175|
| |Anderson County|    76| 375.201|  9.168| 2,605| 12860.514| 179.843| 202,558|
| |Berkeley County|    74| 324.694|  4.388| 4,462| 19578.161| 173.003| 227,907|
| |Beaufort County|    60| 312.302|  2.974| 4,372| 22756.374| 179.202| 192,122|
| |Clarendon County|    59| 1748.407| 29.634|   909| 26937.324| 266.706|  33,745|
| |Dorchester County|    58| 356.246|  9.652| 3,282| 20158.591| 128.985| 162,809|
| |Sumter County|    56| 524.733|  6.693| 2,643| 24765.510| 139.215| 106,721|
| |Laurens County|    49| 726.001|  6.350| 1,379| 20431.748| 82.548|  67,493|
| |Aiken County|    46| 269.207|  6.688| 2,137| 12506.438| 212.356| 170,872|
| |Darlington County|    38| 570.416|  4.289| 1,459| 21900.988| 315.230|  66,618|
| |Colleton County|    36| 955.490|  7.583|   850| 22560.183| 94.791|  37,677|
| |Williamsburg County|    32| 1053.741|  4.704| 1,087| 35794.257| 315.181|  30,368|
| |York County|    32| 113.888|  1.525| 3,807| 13549.055| 110.329| 280,979|
| |Cherokee County|    31| 541.012|  7.479|   718| 12530.541| 191.972|  57,300|
| |Lee County|    30| 1782.743|  8.489|   588| 34941.764| 186.764|  16,828|
| |Pickens County|    30| 236.436|  3.378| 1,934| 15242.269| 79.938| 126,884|
| |Kershaw County|    29| 435.756|  8.586| 1,461| 21953.089| 115.915|  66,551|
| |Lancaster County|    27| 275.476|  1.458| 1,392| 14202.343| 240.495|  98,012|
| |Bamberg County|    27| 1919.522| 50.781|   490| 34835.774| 111.718|  14,066|
| |Dillon County|    26| 853.046|  4.687|   679| 22277.634| 164.047|  30,479|
| |Georgetown County|    26| 414.805| 15.954| 1,543| 24617.103| 186.890|  62,680|
| |Fairfield County|    24| 1073.970|  6.393|   587| 26267.508| 89.497|  22,347|
| |Chesterfield County|    22| 481.928|  3.129|   837| 18335.159| 187.764|  45,650|
| |Greenwood County|    20| 282.442|  4.035| 1,569| 22157.574| 308.669|  70,811|
| |Jasper County|    19| 631.796| 14.251|   635| 21115.286| 180.513|  30,073|
| |Hampton County|    15| 780.356| 29.728|   480| 24971.387| 289.846|  19,222|
| |Marion County|    14| 456.666|  4.660|   590| 19245.197| 149.115|  30,657|
| |Chester County|    14| 434.189|  0.000|   753| 23353.182| 363.301|  32,244|
| |Calhoun County|    14| 962.001| 29.449|   392| 26936.027| 88.347|  14,553|
| |Newberry County|    13| 338.189| 11.149|   895| 23283.039| 152.371|  38,440|
| |Oconee County|    13| 163.427|  5.388|   882| 11087.924| 77.224|  79,546|
| |Saluda County|    10| 488.448| 13.956|   491| 23982.807| 223.291|  20,473|
| |Barnwell County|     9| 431.324| 27.386|   460| 22045.433| 273.856|  20,866|
| |Abbeville County|     8| 326.171|  0.000|   363| 14800.016| 163.086|  24,527|
| |Edgefield County|     7| 256.787|  0.000|   368| 13499.633| 188.659|  27,260|
| |Allendale County|     6| 690.608| 49.329|   253| 29120.626| 411.076|   8,688|
| |Marlboro County|     5| 191.439|  5.470|   554| 21211.425| 257.075|  26,118|
| |Union County|     4| 146.434|  0.000|   403| 14753.258| 203.962|  27,316|
| |McCormick County|     2| 211.349|  0.000|   141| 14900.137| 317.024|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 2,095| 703.930| N/A|72,412| 24330.771| N/A|2,976,149|
| |Hinds County|   129| 556.418|  6.778| 5,917| 25521.912| 160.825| 231,840|
| |Lauderdale County|    98| 1322.091| 11.563| 1,497| 20195.616| 165.743|  74,125|
| |Neshoba County|    96| 3296.930| 19.625| 1,328| 45607.528| 206.058|  29,118|
| |Madison County|    74| 696.326|  8.066| 2,556| 24051.491| 151.901| 106,272|
| |Leflore County|    70| 2483.767| 25.345|   998| 35411.418| 258.515|  28,183|
| |Jones County|    65| 954.507| 12.587| 2,002| 29398.808| 180.412|  68,098|
| |Forrest County|    57| 761.045|  1.907| 1,924| 25688.612| 198.368|  74,897|
| |Monroe County|    55| 1560.195|  0.000|   883| 25048.224| 332.301|  35,252|
| |Holmes County|    50| 2939.447|  8.398|   957| 56261.023| 478.710|  17,010|
| |Jackson County|    47| 327.259|  3.979| 2,482| 17282.077| 192.974| 143,617|
| |Washington County|    46| 1047.621| 13.014| 1,818| 41403.812| 419.699|  43,909|
| |Lincoln County|    45| 1317.600| 16.731|   879| 25737.124| 196.594|  34,153|
| |Lee County|    43| 503.301|  3.344| 1,737| 20331.008| 431.401|  85,436|
| |Pearl River County|    42| 756.280|  7.717|   613| 11038.084| 151.770|  55,535|
| |Lowndes County|    42| 716.785|  9.752| 1,140| 19455.585| 134.092|  58,595|
| |Rankin County|    42| 270.495|  6.440| 2,437| 15695.139| 133.407| 155,271|
| |Oktibbeha County|    42| 846.996|  8.643| 1,183| 23857.059| 161.333|  49,587|
| |Bolivar County|    40| 1305.995| 27.986| 1,224| 39963.432| 494.412|  30,628|
| |Harrison County|    38| 182.622|  1.373| 2,804| 13475.586| 188.114| 208,080|
| |Pike County|    38| 967.216|  7.272|   984| 25045.816| 167.263|  39,288|
| |Warren County|    37| 815.319| 12.592| 1,182| 26046.143| 273.872|  45,381|
| |Simpson County|    36| 1350.439| 32.153|   861| 32297.997| 310.815|  26,658|
| |DeSoto County|    34| 183.838|  2.317| 3,913| 21157.641| 179.976| 184,945|
| |Tate County|    30| 1059.285|  5.044|   774| 27329.543| 191.680|  28,321|
| |Copiah County|    30| 1068.947| 10.180|   987| 35168.359| 152.707|  28,065|
| |Sunflower County|    29| 1154.918| 22.757| 1,116| 44444.444| 352.734|  25,110|
| |Adams County|    28| 912.260| 13.963|   669| 21796.501| 186.176|  30,693|
| |Clarke County|    28| 1801.686| 18.385|   372| 23936.684| 422.845|  15,541|
| |Grenada County|    27| 1300.703| 41.292|   870| 41911.552| 144.523|  20,758|
| |Leake County|    27| 1184.938| 12.539|   813| 35679.803| 144.199|  22,786|
| |Attala County|    25| 1375.592|  0.000|   551| 30318.037| 220.095|  18,174|
| |Marion County|    22| 895.292| 11.627|   713| 29015.586| 168.594|  24,573|
| |Lamar County|    22| 347.315| 18.042| 1,297| 20475.822| 160.126|  63,343|
| |Walthall County|    22| 1539.969| 20.000|   525| 36749.265| 239.995|  14,286|
| |Scott County|    21| 746.693|  5.080| 1,033| 36730.195| 152.386|  28,124|
| |Lafayette County|    21| 388.752| 10.578| 1,072| 19844.869| 235.367|  54,019|
| |Wayne County|    21| 1040.480|  0.000|   810| 40132.785| 254.811|  20,183|
| |Union County|    19| 659.379| 14.873|   772| 26791.602| 639.548|  28,815|
| |Chickasaw County|    19| 1110.916|  0.000|   513| 29994.738| 359.168|  17,103|
| |Winston County|    18| 1002.506| 15.913|   653| 36368.700| 238.692|  17,955|
| |Panola County|    18| 526.439| 16.712| 1,143| 33428.872| 338.425|  34,192|
| |Hancock County|    16| 335.909|  5.998|   432|  9069.533| 110.970|  47,632|
| |Covington County|    16| 858.553| 22.997|   666| 35737.283| 344.954|  18,636|
| |Yazoo County|    14| 471.539|  9.623|   891| 30010.104| 279.074|  29,690|
| |Tippah County|    14| 635.930|  6.489|   443| 20122.644| 493.170|  22,015|
| |Claiborne County|    14| 1557.632| 15.894|   414| 46061.415| 79.471|   8,988|
| |Clay County|    14| 724.788|  0.000|   420| 21743.632| 170.103|  19,316|
| |Wilkinson County|    14| 1622.248| 16.554|   234| 27114.716| 380.732|   8,630|
| |Kemper County|    14| 1437.077|  0.000|   251| 25764.730| 249.289|   9,742|
| |Webster County|    13| 1341.728| 14.744|   257| 26524.925| 324.374|   9,689|
| |Smith County|    13| 816.788|  0.000|   422| 26514.200| 143.611|  15,916|
| |Coahoma County|    13| 587.597|  0.000|   830| 37515.820| 374.512|  22,124|
| |Greene County|    13| 956.867| 10.515|   276| 20315.030| 220.816|  13,586|
| |Newton County|    12| 570.939|  6.797|   588| 27976.021| 305.860|  21,018|
| |Noxubee County|    12| 1151.963|  0.000|   486| 46654.507| 370.274|  10,417|
| |Humphreys County|    12| 1488.095| 17.715|   313| 38814.484| 336.593|   8,064|
| |Tishomingo County|    12| 619.099| 44.221|   476| 24557.602| 405.363|  19,383|
| |Prentiss County|    11| 437.794|  5.686|   498| 19820.107| 460.536|  25,126|
| |Jasper County|    11| 671.428| 17.440|   432| 26368.797| 383.673|  16,383|
| |Tallahatchie County|    11| 796.582|  0.000|   568| 41132.595| 393.118|  13,809|
| |Carroll County|    11| 1105.861|  0.000|   268| 26942.797| 100.533|   9,947|
| |Montgomery County|    10| 1023.018| 73.073|   369| 37749.361| 628.425|   9,775|
| |Marshall County|    10| 283.334|  4.048|   770| 21816.739| 279.287|  35,294|
| |Yalobusha County|    10| 825.900|  0.000|   326| 26924.348| 129.784|  12,108|
| |George County|    10| 408.163| 29.155|   639| 26081.633| 291.545|  24,500|
| |Itawamba County|    10| 427.533|  0.000|   427| 18255.665| 317.596|  23,390|
| |Calhoun County|     9| 626.697|  0.000|   435| 30290.370| 149.214|  14,361|
| |Tunica County|     9| 934.385| 29.663|   381| 39555.648| 444.945|   9,632|
| |Pontotoc County|     9| 279.729|  4.440|   892| 27724.249| 275.289|  32,174|
| |Lawrence County|     8| 635.627|  0.000|   342| 27173.049| 227.010|  12,586|
| |Jefferson County|     8| 1144.492| 20.437|   198| 28326.180| 61.312|   6,990|
| |Perry County|     8| 668.170| 11.932|   262| 21882.569| 226.701|  11,973|
| |Sharkey County|     7| 1619.995| 66.122|   219| 50682.712| 661.223|   4,321|
| |Jefferson Davis County|     7| 629.044| 12.838|   255| 22915.169| 282.428|  11,128|
| |Stone County|     6| 327.225|  7.791|   256| 13961.606| 397.345|  18,336|
| |Amite County|     6| 487.924|  0.000|   249| 20248.841| 162.641|  12,297|
| |Alcorn County|     5| 135.307|  0.000|   457| 12367.061| 88.916|  36,953|
| |Choctaw County|     4| 487.211|  0.000|   141| 17174.178| 104.402|   8,210|
| |Franklin County|     2| 259.302|  0.000|   153| 19836.639| 407.475|   7,713|
| |Issaquena County|     2| 1507.159|  0.000|    28| 21100.226| 215.308|   1,327|
| |Benton County|     1| 121.080|  0.000|   167| 20220.366| 415.132|   8,259|
| |Quitman County|     1| 147.232|  0.000|   279| 41077.739| 189.298|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,896| 329.239| N/A|53,351|  9264.359| N/A|5,758,736|
| |Denver County|   420| 577.549| N/A|10,607| 14585.863| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.000| 7,610| 11590.186| 58.745| 656,590|
| |Jefferson County|   235| 403.170|  1.716| 4,429|  7598.463| 53.674| 582,881|
| |Adams County|   184| 355.610|  2.209| 6,848| 13234.871| 88.074| 517,421|
| |Weld County|   145| 446.852|  0.000| 3,836| 11821.555| 49.748| 324,492|
| |El Paso County|   144| 199.888|  1.190| 5,509|  7647.109| 74.363| 720,403|
| |Boulder County|    77| 236.054|  1.314| 2,141|  6563.538| 35.912| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,840|  5239.866| 39.055| 351,154|
| |Morgan County|    47| 1616.898|  4.915|   699| 24047.062| 63.890|  29,068|
| |Larimer County|    36| 100.869|  0.400| 1,700|  4763.252| 50.034| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   757|  4494.609| 49.196| 168,424|
| |Broomfield County|    32| 454.126| N/A|   492|  6982.190| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   304| 14934.172|  7.018|  20,356|
| |Montrose County|    13| 304.037|  0.000|   323|  7554.142| 43.434|  42,758|
| |Alamosa County|     9| 554.426|  0.000|   233| 14353.477| 26.401|  16,233|
| |Eagle County|     9| 163.259|  0.000| 1,154| 20933.481| 77.743|  55,127|
| |Routt County|     8| 312.037|  0.000|   128|  4992.589| 16.716|  25,638|
| |Gunnison County|     7| 400.870|  8.181|   279| 15977.551| 49.086|  17,462|
| |Otero County|     6| 328.263|  0.000|    78|  4267.425| 54.711|  18,278|
| |Montezuma County|     5| 190.964|  5.456|   117|  4468.548| 27.281|  26,183|
| |Logan County|     5| 223.125|  0.000|   658| 29363.202| 44.625|  22,409|
| |Mesa County|     5| 32.423|  0.926|   368|  2386.356| 48.172| 154,210|
| |Summit County|     4| 128.986|  0.000|   345| 11125.085| 55.280|  31,011|
| |Garfield County|     4| 66.599|  0.000|   802| 13353.091| 80.870|  60,061|
| |Teller County|     3| 118.166|  0.000|   145|  5711.360| 67.523|  25,388|
| |Kit Carson County|     3| 422.714|  0.000|    70|  9863.323| 281.809|   7,097|
| |Saguache County|     2| 293.083|  0.000|   107| 15679.953| 20.935|   6,824|
| |Elbert County|     2| 74.825|  0.000|   111|  4152.793| 32.068|  26,729|
| |Pitkin County|     2| 112.568|  0.000|   190| 10693.983| 32.162|  17,767|
| |Rio Grande County|     2| 177.510|  0.000|    92|  8165.439| 38.038|  11,267|
| |La Plata County|     2| 35.574|  0.000|   233|  4144.359| 35.574|  56,221|
| |Grand County|     1| 63.557|  0.000|    54|  3432.058| 72.636|  15,734|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925|  0.000|   6,897|
| |Delta County|     1| 32.090|  0.000|   133|  4268.019| 36.675|  31,162|
| |Clear Creek County|     1| 103.093|  0.000|    31|  3195.876| 14.728|   9,700|
| |Crowley County|     1| 164.989|  0.000|    73| 12044.217| 23.570|   6,061|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094|  0.000|  13,283|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202|  0.000|   4,952|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Fremont County|     0|  0.000|  0.000|   138|  2884.676| 38.821|  47,839|
| |Custer County|     0|  0.000|  0.000|    13|  2565.114| 56.376|   5,068|
| |Costilla County|     0|  0.000|  0.000|    24|  6174.428| 36.753|   3,887|
| |Conejos County|     0|  0.000|  0.000|    27|  3290.676| 69.644|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347|  0.000|   1,831|
| |Bent County|     0|  0.000|  0.000|    11|  1972.387| 51.231|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774|  0.000|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    41|  2922.518| 50.915|  14,029|
| |Dolores County|     0|  0.000|  0.000|     2|   973.236| 69.517|   2,055|
| |Gilpin County|     0|  0.000|  0.000|    17|  2723.050| 22.883|   6,243|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 90.359|   6,324|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053|  0.000|  10,019|
| |Washington County|     0|  0.000|  0.000|    51| 10391.198| 58.214|   4,908|
| |San Miguel County|     0|  0.000|  0.000|    93| 11370.583| 69.865|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Prowers County|     0|  0.000|  0.000|    69|  5668.748| 187.785|  12,172|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263|  0.000|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866|  9.848|  14,506|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684|  0.000|   8,127|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517|  0.000|   1,392|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,855| 378.326| N/A|104,595| 21332.053| N/A|4,903,185|
| |Jefferson County|   262| 397.830|  3.905|14,059| 21347.671| 173.752| 658,573|
| |Mobile County|   228| 551.778|  7.260|11,074| 26799.932| 192.569| 413,210|
| |Montgomery County|   153| 675.538|  2.523| 7,165| 31635.509| 208.149| 226,486|
| |Tuscaloosa County|    85| 406.009|  6.141| 4,484| 21418.165| 173.321| 209,355|
| |Tallapoosa County|    79| 1957.044|  0.000|   889| 22022.940| 84.935|  40,367|
| |Walker County|    66| 1039.026|  4.498| 1,628| 25629.319| 200.159|  63,521|
| |Lee County|    47| 285.641|  0.000| 2,779| 16889.305| 68.589| 164,542|
| |Elmore County|    39| 480.242|  1.759| 1,826| 22485.193| 167.117|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   855| 25711.193| 47.255|  33,254|
| |Shelby County|    38| 174.551|  1.312| 3,517| 16155.111| 136.491| 217,702|
| |Marshall County|    38| 392.667|  1.476| 3,253| 33614.401| 94.476|  96,774|
| |Madison County|    37| 99.220|  1.149| 5,735| 15379.087| 110.329| 372,909|
| |Butler County|    36| 1851.090|  0.000|   795| 40878.239| 205.677|  19,448|
| |Etowah County|    35| 342.238|  4.191| 2,292| 22411.703| 181.596| 102,268|
| |Dale County|    30| 610.103| 14.526|   885| 17998.048| 145.263|  49,172|
| |Baldwin County|    29| 129.909|  2.560| 3,888| 17416.702| 151.667| 223,234|
| |Marion County|    27| 908.816|  4.809|   608| 20465.179| 134.639|  29,709|
| |Hale County|    26| 1774.623|  0.000|   497| 33922.599| 185.263|  14,651|
| |Dallas County|    25| 672.115|  7.681| 1,365| 36697.494| 130.582|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   580| 59633.971| 102.817|   9,726|
| |St. Clair County|    22| 245.777|  6.384| 1,419| 15852.623| 103.737|  89,512|
| |Autauga County|    22| 393.778|  2.557| 1,219| 21818.898| 115.065|  55,869|
| |Franklin County|    22| 701.486|  9.110| 1,360| 43364.581| 327.967|  31,362|
| |Covington County|    22| 593.808|  7.712|   775| 20918.243| 146.524|  37,049|
| |Morgan County|    21| 175.469|  3.581| 2,515| 21014.547| 124.142| 119,679|
| |Calhoun County|    21| 184.851|  5.030| 1,936| 17041.503| 162.216| 113,605|
| |Lauderdale County|    21| 226.466|  3.081| 1,240| 13372.300| 78.570|  92,729|
| |Sumter County|    19| 1528.929| 11.496|   378| 30417.639| 160.940|  12,427|
| |Colbert County|    18| 325.845|  5.172| 1,276| 23098.785| 178.439|  55,241|
| |Marengo County|    17| 901.235| 15.147|   591| 31331.177| 196.909|  18,863|
| |Escambia County|    17| 464.062|  0.000| 1,114| 30409.740| 105.291|  36,633|
| |Talladega County|    15| 187.552|  1.786| 1,144| 14303.934| 171.476|  79,978|
| |Macon County|    15| 830.197|  7.907|   346| 19149.878| 55.346|  18,068|
| |DeKalb County|    14| 195.769|  1.998| 1,899| 26554.612| 137.837|  71,513|
| |Limestone County|    13| 131.426|  0.000| 1,455| 14709.599| 153.090|  98,915|
| |Washington County|    13| 796.276|  8.750|   467| 28604.680| 210.007|  16,326|
| |Houston County|    13| 122.778|  1.349| 1,532| 14468.937| 152.461| 105,882|
| |Greene County|    13| 1602.762| 35.226|   258| 31808.655| 105.677|   8,111|
| |Bullock County|    13| 1287.001| 28.286|   496| 49104.049| 424.286|  10,101|
| |Cullman County|    12| 143.253|  0.000| 1,284| 15328.049| 97.207|  83,768|
| |Choctaw County|    12| 953.213|  0.000|   296| 23512.590| 102.130|  12,589|
| |Winston County|    11| 465.530|  0.000|   478| 20229.379| 126.963|  23,629|
| |Randolph County|    11| 484.112|  6.287|   409| 18000.176| 37.723|  22,722|
| |Clarke County|    10| 423.334|  0.000|   835| 35348.404| 54.429|  23,622|
| |Conecuh County|    10| 828.706|  0.000|   403| 33396.867| 118.387|  12,067|
| |Pickens County|    10| 501.756|  7.168|   440| 22077.270| 258.046|  19,930|
| |Wilcox County|    10| 964.041|  0.000|   455| 43863.877| 316.756|  10,373|
| |Crenshaw County|     9| 653.500| 41.492|   350| 25413.883| 248.952|  13,772|
| |Chilton County|     9| 202.575|  6.431|   864| 19447.195| 176.851|  44,428|
| |Cherokee County|     8| 305.390|  0.000|   306| 11681.173| 169.055|  26,196|
| |Pike County|     7| 211.391|  0.000|   725| 21894.063| 73.340|  33,114|
| |Coffee County|     6| 114.631|  0.000|   816| 15589.775| 141.924|  52,342|
| |Monroe County|     6| 289.394|  6.890|   432| 20836.348| 75.794|  20,733|
| |Barbour County|     6| 243.053|  5.787|   605| 24507.818| 167.822|  24,686|
| |Jackson County|     5| 96.850|  2.767| 1,130| 21888.196| 320.990|  51,626|
| |Bibb County|     5| 223.274|  0.000|   474| 21166.384| 204.136|  22,394|
| |Blount County|     5| 86.466|  2.470|   863| 14924.083| 125.994|  57,826|
| |Clay County|     5| 377.786|  0.000|   304| 22969.399| 442.550|  13,235|
| |Fayette County|     5| 306.711|  0.000|   246| 15090.173| 297.948|  16,302|
| |Perry County|     4| 448.280|  0.000|   457| 51215.959| 192.120|   8,923|
| |Lawrence County|     3| 91.119|  4.339|   370| 11238.003| 82.441|  32,924|
| |Henry County|     3| 174.368|  0.000|   277| 16099.971| 107.942|  17,205|
| |Coosa County|     3| 281.347|  0.000|   106|  9940.917| 40.192|  10,663|
| |Geneva County|     2| 76.130|  5.438|   287| 10924.594| 130.508|  26,271|
| |Lamar County|     2| 144.875|  0.000|   245| 17747.193| 165.571|  13,805|
| |Russell County|     2| 34.506|  0.000| 1,410| 24326.702| 56.688|  57,961|
| |Cleburne County|     1| 67.069|  0.000|   134|  8987.257| 67.069|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,781| 233.884| N/A|67,497|  8863.815| N/A|7,614,893|
| |King County|   694| 308.064|  1.141|17,745|  7876.927| 65.823|2,252,782|
| |Yakima County|   221| 880.924|  5.125|10,645| 42431.828| 158.304| 250,873|
| |Snohomish County|   203| 246.934|  1.738| 5,741|  6983.480| 44.313| 822,083|
| |Pierce County|   147| 162.435|  0.789| 6,177|  6825.565| 67.247| 904,980|
| |Benton County|   121| 592.005|  3.495| 3,860| 18885.464| 78.282| 204,390|
| |Spokane County|   109| 208.494|  5.192| 4,806|  9192.843| 82.523| 522,798|
| |Franklin County|    54| 567.096|  7.501| 3,735| 39224.129| 292.549|  95,222|
| |Clark County|    49| 100.360|  1.756| 1,938|  3969.351| 44.182| 488,241|
| |Whatcom County|    39| 170.122|  0.000| 1,029|  4488.608| 24.303| 229,247|
| |Skagit County|    23| 178.012|  1.106|   934|  7228.822| 48.649| 129,205|
| |Kittitas County|    20| 417.232|  0.000|   448|  9345.989| 217.557|  47,935|
| |Grant County|    14| 143.247|  1.462| 1,833| 18755.180| 428.281|  97,733|
| |Island County|    12| 140.943|  1.678|   254|  2983.287| 11.745|  85,141|
| |Thurston County|    11| 37.861|  0.000|   798|  2746.648| 32.452| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,548| 20051.813| 351.591|  77,200|
| |Kitsap County|     7| 25.785|  0.000|   812|  2991.089| 34.731| 271,473|
| |Douglas County|     7| 161.183|  0.000| 1,034| 23808.976| 240.129|  43,429|
| |Adams County|     6| 300.255|  7.149|   504| 25221.438| 371.745|  19,983|
| |Okanogan County|     6| 142.035|  6.764|   925| 21897.119| 162.326|  42,243|
| |Cowlitz County|     5| 45.211|  0.000|   506|  4575.335| 27.126| 110,593|
| |Lewis County|     4| 49.562|  1.770|   262|  3246.311| 65.493|  80,707|
| |Walla Walla County|     4| 65.833|  2.351|   642| 10566.162| 223.361|  60,760|
| |Klickitat County|     3| 133.779|  0.000|   134|  5975.474| 133.779|  22,425|
| |Grays Harbor County|     3| 39.967|  1.903|   144|  1918.440| 41.871|  75,061|
| |Asotin County|     2| 88.566|  0.000|    41|  1815.605| 88.566|  22,582|
| |Pacific County|     2| 89.004|  0.000|    58|  2581.105| 50.859|  22,471|
| |Mason County|     1| 14.977|  0.000|   264|  3953.990| 81.305|  66,768|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Clallam County|     1| 12.931|  1.847|   169|  2185.411| 86.825|  77,331|
| |Skamania County|     1| 82.761|  0.000|    58|  4800.132| 11.823|  12,083|
| |Stevens County|     1| 21.871|  0.000|   116|  2537.016| 18.746|  45,723|
| |Jefferson County|     0|  0.000|  0.000|    59|  1831.104| 22.168|  32,221|
| |Lincoln County|     0|  0.000|  0.000|    31|  2833.897| 52.238|  10,939|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489|  0.000|   7,627|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753|  0.000|   2,225|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Whitman County|     0|  0.000|  0.000|   124|  2474.852| 54.173|  50,104|
| |Pend Oreille County|     0|  0.000|  0.000|    50|  3643.253| 62.456|  13,724|
| |San Juan County|     0|  0.000|  0.000|    29|  1649.414|  8.125|  17,582|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,712| 303.566| N/A|65,568| 11626.291| N/A|5,639,632|
| |Hennepin County|   851| 672.279|  1.806|20,625| 16293.490| 130.122|1,265,843|
| |Ramsey County|   274| 497.891|  1.817| 8,132| 14776.830| 123.045| 550,321|
| |Anoka County|   115| 322.200|  0.000| 4,064| 11386.273| 130.081| 356,921|
| |Dakota County|   106| 247.074|  0.000| 4,881| 11377.065| 133.527| 429,021|
| |Washington County|    48| 182.899|  1.633| 2,392|  9114.464| 129.009| 262,440|
| |Clay County|    40| 622.840|  0.000|   799| 12441.220| 31.142|  64,222|
| |Scott County|    24| 161.060|  4.793| 1,734| 11636.569| 153.390| 149,013|
| |Olmsted County|    23| 145.300|  0.000| 1,843| 11642.966| 86.639| 158,293|
| |St. Louis County|    21| 105.491|  1.435|   677|  3400.814| 76.786| 199,070|
| |Stearns County|    21| 130.374|  0.887| 2,962| 18388.949| 49.666| 161,075|
| |Winona County|    17| 336.740|  2.830|   279|  5526.503| 42.446|  50,484|
| |Crow Wing County|    14| 215.203|  0.000|   271|  4165.706| 70.270|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   378| 11028.768| 150.051|  34,274|
| |Itasca County|    12| 265.899|  0.000|   148|  3279.415|  3.165|  45,130|
| |Sherburne County|    10| 102.840|  2.938|   782|  8042.123| 73.457|  97,238|
| |Nobles County|     9| 416.108| 19.815| 1,799| 83175.366| 224.566|  21,629|
| |Goodhue County|     9| 194.217|  0.000|   215|  4639.620| 55.490|  46,340|
| |Pipestone County|     9| 986.193|  0.000|   164| 17970.633| 109.577|   9,126|
| |Rice County|     8| 119.453|  0.000| 1,067| 15932.031| 61.860|  66,972|
| |Martin County|     6| 304.832|  7.258|   212| 10770.716| 36.289|  19,683|
| |Blue Earth County|     5| 73.907|  0.000|   994| 14692.623| 141.478|  67,653|
| |Renville County|     5| 343.690|  0.000|    69|  4742.920| 39.279|  14,548|
| |Wright County|     5| 36.133|  0.000|   985|  7118.235| 96.011| 138,377|
| |Grant County|     4| 669.792| 23.921|    57|  9544.541| 23.921|   5,972|
| |Otter Tail County|     4| 68.090|  2.432|   223|  3796.003| 63.226|  58,746|
| |Polk County|     4| 127.535|  0.000|   161|  5133.274| 31.884|  31,364|
| |Carver County|     3| 28.547|  0.000|   964|  9173.177| 123.705| 105,089|
| |Cass County|     3| 100.742|  4.797|    81|  2720.038| 38.378|  29,779|
| |Koochiching County|     3| 245.319|  0.000|    84|  6868.918| 58.409|  12,229|
| |Wilkin County|     3| 483.325|  0.000|    39|  6283.229| 115.077|   6,207|
| |Lyon County|     3| 117.767|  0.000|   432| 16958.467| 39.256|  25,474|
| |Kanabec County|     3| 183.632| 17.489|    43|  2632.062| 52.466|  16,337|
| |Mille Lacs County|     3| 114.168|  0.000|    79|  3006.431| 43.493|  26,277|
| |Benton County|     3| 73.369|  0.000|   332|  8119.543| 41.925|  40,889|
| |Meeker County|     2| 86.125|  0.000|    90|  3875.635| 24.607|  23,222|
| |Steele County|     2| 54.572|  0.000|   369| 10068.488| 70.164|  36,649|
| |Todd County|     2| 81.090|  0.000|   435| 17637.042| 52.129|  24,664|
| |Sibley County|     2| 134.544|  0.000|    91|  6121.763| 67.272|  14,865|
| |Mower County|     2| 49.923|  0.000| 1,126| 28106.435| 82.016|  40,062|
| |Le Sueur County|     2| 69.235|  4.945|   255|  8827.500| 153.307|  28,887|
| |Brown County|     2| 79.974|  0.000|    99|  3958.733| 57.125|  25,008|
| |Watonwan County|     2| 183.537| 26.220|   393| 36064.972| 1114.330|  10,897|
| |Swift County|     1| 107.921|  0.000|    58|  6259.443| 46.252|   9,266|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991|  0.000|  14,119|
| |Aitkin County|     1| 62.949|  0.000|    44|  2769.734| 35.971|  15,886|
| |Chisago County|     1| 17.674|  0.000|   221|  3906.043| 42.924|  56,579|
| |Murray County|     1| 122.041|  0.000|   129| 15743.227| 122.041|   8,194|
| |Morrison County|     1| 29.953|  0.000|   104|  3115.078| 47.068|  33,386|
| |Mahnomen County|     1| 180.930|  0.000|    28|  5066.039| 25.847|   5,527|
| |Kandiyohi County|     1| 23.149|  0.000|   739| 17106.877| 135.585|  43,199|
| |Freeborn County|     1| 33.024|  0.000|   370| 12218.883| 47.177|  30,281|
| |Douglas County|     1| 26.219|  0.000|   147|  3854.120| 14.982|  38,141|
| |Chippewa County|     1| 84.746|  0.000|   124| 10508.475| 217.918|  11,800|
| |Carlton County|     1| 27.878|  3.983|   158|  4404.672| 79.650|  35,871|
| |Beltrami County|     1| 21.192|  3.027|   275|  5827.753| 102.932|  47,188|
| |Becker County|     1| 29.050|  0.000|   166|  4822.357| 20.750|  34,423|
| |Waseca County|     1| 53.729|  7.676|   172|  9241.350| 176.537|  18,612|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046|  0.000|  11,249|
| |Redwood County|     0|  0.000|  0.000|    38|  2504.944| 18.834|  15,170|
| |Rock County|     0|  0.000|  0.000|    90|  9661.836| 76.681|   9,315|
| |Roseau County|     0|  0.000|  0.000|    56|  3692.713| 37.681|  15,165|
| |Yellow Medicine County|     0|  0.000|  0.000|    54|  5561.850| 29.428|   9,709|
| |Wadena County|     0|  0.000|  0.000|    30|  2192.662| 31.324|  13,682|
| |Wabasha County|     0|  0.000|  0.000|   101|  4670.088| 59.449|  21,627|
| |Traverse County|     0|  0.000|  0.000|    16|  4909.481| 219.173|   3,259|
| |Stevens County|     0|  0.000|  0.000|    22|  2243.753| 58.279|   9,805|
| |Red Lake County|     0|  0.000|  0.000|    26|  6411.837| 70.460|   4,055|
| |Lake County|     0|  0.000|  0.000|    25|  2349.403| 53.701|  10,641|
| |Cottonwood County|     0|  0.000|  0.000|   187| 16702.394| 114.837|  11,196|
| |Jackson County|     0|  0.000|  0.000|    84|  8531.383|  0.000|   9,846|
| |Isanti County|     0|  0.000|  0.000|   148|  3645.679| 70.380|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    37|  1721.651| 19.942|  21,491|
| |Houston County|     0|  0.000|  0.000|    59|  3172.043| 145.929|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    76|  3607.538| 74.592|  21,067|
| |Faribault County|     0|  0.000|  0.000|    96|  7031.422| 94.171|  13,653|
| |Dodge County|     0|  0.000|  0.000|   137|  6544.378| 61.418|  20,934|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Lake of the Woods County|     0|  0.000|  0.000|     7|  1871.658| 114.591|   3,740|
| |Lincoln County|     0|  0.000|  0.000|    61| 10817.521| 76.001|   5,639|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Big Stone County|     0|  0.000|  0.000|    25|  5009.016| 85.869|   4,991|
| |Cook County|     0|  0.000|  0.000|     6|  1098.298| 26.150|   5,463|
| |Lac qui Parle County|     0|  0.000|  0.000|    10|  1509.890| 43.140|   6,623|
| |Pine County|     0|  0.000|  0.000|   133|  4496.433| 19.319|  29,579|
| |Norman County|     0|  0.000|  0.000|    43|  6745.098| 44.818|   6,375|
| |Marshall County|     0|  0.000|  0.000|    30|  3213.368| 15.302|   9,336|
| |McLeod County|     0|  0.000|  0.000|   271|  7550.219| 294.526|  35,893|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,361| 199.292| N/A|128,556| 18824.531| N/A|6,829,174|
| |Shelby County|   334| 356.394|  3.963|24,798| 26460.627| 200.147| 937,166|
| |Davidson County|   230| 331.343|  2.675|22,005| 31700.915| 264.046| 694,144|
| |Sumner County|    76| 397.317|  2.987| 3,649| 19076.447| 149.367| 191,283|
| |Hamilton County|    60| 163.130|  2.719| 6,862| 18656.676| 249.356| 367,804|
| |Rutherford County|    59| 177.558|  1.720| 7,137| 21478.550| 235.598| 332,285|
| |Knox County|    43| 91.428|  0.911| 5,297| 11262.712| 185.894| 470,313|
| |Madison County|    26| 265.349| 11.664| 1,373| 14012.492| 310.546|  97,984|
| |Williamson County|    26| 109.055|  0.599| 3,893| 16328.876| 189.348| 238,412|
| |Wilson County|    25| 172.823|  1.975| 2,501| 17289.174| 177.760| 144,657|
| |Robertson County|    21| 292.426|  1.989| 1,647| 22934.566| 159.143|  71,813|
| |Putnam County|    20| 249.237|  3.561| 1,959| 24412.736| 309.766|  80,245|
| |McMinn County|    20| 371.789|  0.000|   617| 11469.681| 169.961|  53,794|
| |Sullivan County|    18| 113.674|  3.609| 1,202|  7590.876| 148.858| 158,348|
| |Hardeman County|    18| 718.563|  5.703| 1,082| 43193.613| 866.838|  25,050|
| |Montgomery County|    16| 76.558|  2.051| 2,169| 10378.338| 148.330| 208,993|
| |Bradley County|    16| 147.997|  3.964| 2,175| 20118.398| 289.388| 108,110|
| |Blount County|    15| 112.707|  4.294| 1,507| 11323.335| 207.167| 133,088|
| |Hamblen County|    15| 231.004|  2.200| 1,507| 23208.181| 224.404|  64,934|
| |Giles County|    14| 475.156|  4.849|   416| 14118.925| 150.304|  29,464|
| |Macon County|    13| 528.412|  0.000|   871| 35403.626| 63.874|  24,602|
| |Tipton County|    12| 194.808|  4.638| 1,268| 20584.750| 132.191|  61,599|
| |Bedford County|    12| 241.386|  2.874|   987| 19853.962| 169.545|  49,713|
| |Sevier County|    10| 101.781|  4.362| 2,055| 20916.031| 234.097|  98,250|
| |Maury County|    10| 103.748|  4.446| 1,445| 14991.648| 256.407|  96,387|
| |Hawkins County|    10| 176.100|  7.547|   579| 10196.175| 241.508|  56,786|
| |Monroe County|    10| 214.846|  3.069|   524| 11257.922| 220.984|  46,545|
| |Cheatham County|     9| 221.310|  7.026|   648| 15934.296| 172.130|  40,667|
| |Dyer County|     9| 242.202|  3.844|   747| 20102.801| 322.937|  37,159|
| |Gibson County|     9| 183.176|  8.723|   832| 16933.629| 308.201|  49,133|
| |Greene County|     9| 130.304|  2.068|   609|  8817.270| 217.174|  69,069|
| |Lauderdale County|     9| 351.110|  5.573|   569| 22197.948| 306.525|  25,633|
| |Hardin County|     8| 311.867|  0.000|   517| 20154.374| 194.917|  25,652|
| |Polk County|     8| 475.285| 42.436|   270| 16040.875| 534.696|  16,832|
| |Fayette County|     8| 194.491|  0.000|   759| 18452.338| 197.964|  41,133|
| |Lawrence County|     7| 158.579|  3.236|   646| 14634.588| 229.778|  44,142|
| |Haywood County|     7| 404.531|  8.256|   619| 35772.076| 899.875|  17,304|
| |Crockett County|     7| 491.918| 20.078|   308| 21644.413| 391.527|  14,230|
| |Cumberland County|     7| 115.664|  2.360|   592|  9781.890| 316.306|  60,520|
| |Anderson County|     6| 77.944|  0.000|   772| 10028.839| 146.610|  76,978|
| |Trousdale County|     6| 531.726|  0.000| 1,587| 140641.616| 50.641|  11,284|
| |Warren County|     6| 145.359|  6.922|   626| 15165.831| 321.867|  41,277|
| |White County|     6| 219.419|  5.224|   345| 12616.566| 266.437|  27,345|
| |Carter County|     6| 106.400|  0.000|   643| 11402.529| 301.467|  56,391|
| |McNairy County|     6| 233.518|  5.560|   430| 16735.425| 272.437|  25,694|
| |Carroll County|     6| 216.084| 15.435|   401| 14441.603| 391.009|  27,767|
| |Marion County|     5| 172.968|  4.942|   258|  8925.174| 153.201|  28,907|
| |Weakley County|     5| 150.024|  4.286|   625| 18753.000| 694.397|  33,328|
| |Cocke County|     5| 138.873|  7.936|   557| 15470.503| 313.457|  36,004|
| |Jefferson County|     4| 73.401|  0.000|   651| 11946.050| 175.639|  54,495|
| |Marshall County|     4| 116.364|  0.000|   372| 10821.818| 282.597|  34,375|
| |Obion County|     4| 133.027|  0.000|   681| 22647.910| 484.600|  30,069|
| |Coffee County|     4| 70.771|  2.528|   617| 10916.490| 174.401|  56,520|
| |Franklin County|     4| 94.769|  0.000|   383|  9074.109| 172.615|  42,208|
| |Dickson County|     4| 74.145|  5.296|   784| 14532.513| 227.733|  53,948|
| |Smith County|     4| 198.442|  0.000|   483| 23961.899| 198.442|  20,157|
| |Decatur County|     3| 257.224|  0.000|   244| 20920.861| 342.965|  11,663|
| |Loudon County|     3| 55.486|  0.000|   815| 15073.611| 174.384|  54,068|
| |Humphreys County|     3| 161.447|  0.000|   140|  7534.173| 92.255|  18,582|
| |Henderson County|     3| 106.697|  0.000|   695| 24718.142| 462.354|  28,117|
| |Bledsoe County|     2| 132.767|  9.483|   751| 49853.956| 407.784|  15,064|
| |Benton County|     2| 123.762|  8.840|   187| 11571.782| 247.525|  16,160|
| |Campbell County|     2| 50.198|  3.586|   275|  6902.264| 75.297|  39,842|
| |Wayne County|     2| 119.954|  0.000|   239| 14334.553| 94.250|  16,673|
| |Washington County|     2| 15.459|  0.000| 1,466| 11331.401| 208.696| 129,375|
| |Grundy County|     2| 148.954|  0.000|   130|  9681.984| 170.233|  13,427|
| |Hancock County|     2| 302.115|  0.000|    84| 12688.822| 64.739|   6,620|
| |Scott County|     2| 90.629| 12.947|   144|  6525.285| 142.417|  22,068|
| |Chester County|     2| 115.627|  0.000|   278| 16072.151| 454.249|  17,297|
| |DeKalb County|     2| 97.609|  0.000|   390| 19033.675| 174.301|  20,490|
| |Roane County|     2| 37.466|  0.000|   542| 10153.235| 152.539|  53,382|
| |Rhea County|     2| 60.301|  0.000|   583| 17577.713| 193.824|  33,167|
| |Pickett County|     1| 198.098|  0.000|    38|  7527.734| 28.300|   5,048|
| |Henry County|     1| 30.917|  4.417|   336| 10388.004| 203.167|  32,345|
| |Sequatchie County|     1| 66.551|  9.507|   124|  8252.363| 171.132|  15,026|
| |Claiborne County|     1| 31.290|  4.470|   313|  9793.798| 165.390|  31,959|
| |Grainger County|     1| 42.882|  6.126|   223|  9562.607| 140.897|  23,320|
| |Overton County|     1| 44.962|  0.000|   280| 12589.362| 526.698|  22,241|
| |Hickman County|     1| 39.717|  5.674|   305| 12113.750| 181.564|  25,178|
| |Jackson County|     1| 84.846|  0.000|   153| 12981.503| 290.902|  11,786|
| |Johnson County|     1| 56.218|  8.031|   349| 19619.969| 513.990|  17,788|
| |Lewis County|     1| 81.513|  0.000|    89|  7254.646| 174.670|  12,268|
| |Lincoln County|     1| 29.099|  0.000|   349| 10155.386| 166.277|  34,366|
| |Meigs County|     1| 80.502| 11.500|   121|  9740.782| 172.505|  12,422|
| |Morgan County|     1| 46.722|  0.000|   145|  6774.751| 126.818|  21,403|
| |Lake County|     1| 142.531| 20.362|   804| 114595.211| 244.339|   7,016|
| |Fentress County|     0|  0.000|  0.000|   124|  6694.380| 215.948|  18,523|
| |Clay County|     0|  0.000|  0.000|    91| 11950.098| 243.880|   7,615|
| |Houston County|     0|  0.000|  0.000|    67|  8169.735| 139.356|   8,201|
| |Cannon County|     0|  0.000|  0.000|   166| 11309.443| 145.991|  14,678|
| |Moore County|     0|  0.000|  0.000|    77| 11868.064| 352.299|   6,488|
| |Perry County|     0|  0.000|  0.000|    91| 11267.954| 176.891|   8,076|
| |Unicoi County|     0|  0.000|  0.000|   184| 10289.101| 119.826|  17,883|
| |Van Buren County|     0|  0.000|  0.000|    45|  7663.488| 218.957|   5,872|
| |Stewart County|     0|  0.000|  0.000|    84|  6124.681| 62.497|  13,715|
| |Union County|     0|  0.000|  0.000|   179|  8962.548| 121.599|  19,972|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,349| 219.799| N/A|61,452| 10012.663| N/A|6,137,428|
| |St. Louis County|   882| 887.141|  5.029|22,416| 22546.658| 321.865| 994,205|
| |St. Charles County|    95| 236.305|  2.843| 4,760| 11840.148| 226.356| 402,022|
| |Jackson County|    66| 93.882|  0.203| 4,640|  6600.181| 113.187| 703,011|
| |Jasper County|    32| 263.748|  1.177| 1,968| 16220.493| 231.957| 121,328|
| |Jefferson County|    30| 133.285|  3.808| 1,998|  8876.804| 234.836| 225,081|
| |Clay County|    30| 120.025|  5.715| 1,158|  4632.964| 60.012| 249,948|
| |Franklin County|    19| 182.750|  1.374|   762|  7329.249| 180.002| 103,967|
| |Scott County|    13| 339.603|  0.000|   492| 12852.665| 343.335|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,940|  6619.218| 178.885| 293,086|
| |Platte County|    10| 95.769|  0.000|   412|  3945.680| 61.566| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,141| 13060.299| 81.760|  87,364|
| |Cass County|     9| 85.082|  0.000|   883|  8347.514| 172.866| 105,780|
| |Stoddard County|     9| 310.078|  0.000|   244|  8406.546| 63.984|  29,025|
| |Gentry County|     9| 1369.655|  0.000|    87| 13239.994| 43.481|   6,571|
| |Pemiscot County|     9| 569.440|  0.000|   268| 16956.659| 307.317|  15,805|
| |McDonald County|     8| 350.309|  6.256|   962| 42124.622| 68.811|  22,837|
| |Saline County|     7| 307.544|  0.000|   483| 21220.509| 301.267|  22,761|
| |Camden County|     7| 151.172|  6.170|   412|  8897.527| 172.768|  46,305|
| |Cape Girardeau County|     6| 76.074|  1.811|   770|  9762.777| 193.807|  78,871|
| |Newton County|     6| 103.029|  0.000|   962| 16518.992| 215.870|  58,236|
| |Pettis County|     5| 118.094|  3.374|   656| 15493.989| 357.657|  42,339|
| |Barry County|     4| 111.766|  0.000|   296|  8270.698| 151.683|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   398| 13662.421| 397.220|  29,131|
| |Perry County|     4| 209.030|  0.000|   263| 13743.729| 231.426|  19,136|
| |St. Francois County|     4| 59.511|  4.251|   599|  8911.701| 473.959|  67,215|
| |Cole County|     3| 39.090|  0.000|   597|  7779.008| 316.447|  76,745|
| |Henry County|     3| 137.463|  0.000|    95|  4353.006| 85.096|  21,824|
| |Johnson County|     3| 55.492|  2.642|   517|  9563.094| 73.989|  54,062|
| |Boone County|     3| 16.624|  0.000| 1,610|  8921.496| 168.614| 180,463|
| |Taney County|     3| 53.640|  0.000|   763| 13642.540| 375.483|  55,928|
| |New Madrid County|     3| 175.685| 16.732|   304| 17802.764| 401.566|  17,076|
| |Douglas County|     2| 151.688|  0.000|    94|  7129.314| 75.844|  13,185|
| |Butler County|     2| 47.083|  0.000|   321|  7556.853| 127.797|  42,478|
| |Moniteau County|     2| 123.977|  0.000|   164| 10166.129| 141.688|  16,132|
| |Lawrence County|     2| 52.144|  0.000|   271|  7065.572| 152.709|  38,355|
| |Lafayette County|     2| 61.147|  0.000|   199|  6084.138| 91.721|  32,708|
| |Howell County|     2| 49.854|  0.000|   177|  4412.095| 85.464|  40,117|
| |Pike County|     1| 54.639|  0.000|   145|  7922.631| 304.416|  18,302|
| |Pulaski County|     1| 19.009|  0.000|   275|  5227.441| 133.062|  52,607|
| |Putnam County|     1| 212.947|  0.000|    14|  2981.261| 30.421|   4,696|
| |Randolph County|     1| 40.407|  0.000|    84|  3394.214| 75.042|  24,748|
| |Ste. Genevieve County|     1| 55.885|  0.000|    72|  4023.695| 119.753|  17,894|
| |Scotland County|     1| 203.998|  0.000|    19|  3875.969| 87.428|   4,902|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131| 15.838|   9,020|
| |Bollinger County|     1| 82.420|  0.000|    82|  6758.427| 164.840|  12,133|
| |Miller County|     1| 39.034|  0.000|   159|  6206.331| 150.558|  25,619|
| |Benton County|     1| 51.432|  0.000|   118|  6069.022| 102.865|  19,443|
| |Osage County|     1| 73.448|  0.000|    62|  4553.801| 136.404|  13,615|
| |Dallas County|     1| 59.249|  0.000|    78|  4621.401| 76.177|  16,878|
| |Marion County|     1| 35.051|  0.000|   272|  9533.824| 355.515|  28,530|
| |Carter County|     1| 167.168|  0.000|    23|  3844.868| 47.762|   5,982|
| |Christian County|     1| 11.287|  0.000|   453|  5113.155| 143.510|  88,595|
| |DeKalb County|     1| 79.700|  0.000|    44|  3506.814| 91.086|  12,547|
| |Grundy County|     1| 101.523|  0.000|    31|  3147.208| 29.007|   9,850|
| |Harrison County|     1| 119.732|  0.000|    62|  7423.372| 34.209|   8,352|
| |Laclede County|     1| 27.993|  0.000|   238|  6662.374| 143.965|  35,723|
| |Lewis County|     1| 102.291|  0.000|    54|  5523.732| 116.904|   9,776|
| |Lincoln County|     1| 16.945|  0.000|   449|  7608.493| 162.192|  59,013|
| |Linn County|     1| 83.893|  0.000|    41|  3439.597| 95.877|  11,920|
| |Callaway County|     1| 22.350|  0.000|   202|  4514.673| 137.292|  44,743|
| |Stone County|     1| 31.297|  0.000|   196|  6134.201| 268.260|  31,952|
| |Texas County|     1| 39.373|  5.625|    68|  2677.376| 73.122|  25,398|
| |Washington County|     1| 40.437|  0.000|   143|  5782.450| 352.377|  24,730|
| |Shannon County|     1| 122.459|  0.000|    44|  5388.195| 17.494|   8,166|
| |Bates County|     1| 61.835|  0.000|    54|  3339.105| 53.002|  16,172|
| |Audrain County|     1| 39.389|  0.000|   226|  8901.843| 129.420|  25,388|
| |Andrew County|     1| 56.459|  0.000|   101|  5702.349| 104.852|  17,712|
| |Webster County|     1| 25.258|  0.000|   157|  3965.448| 72.165|  39,592|
| |Maries County|     0|  0.000|  0.000|    31|  3564.448| 114.982|   8,697|
| |Oregon County|     0|  0.000|  0.000|    25|  2374.395| 122.112|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   232| 10501.539| 297.457|  22,092|
| |Morgan County|     0|  0.000|  0.000|    98|  4751.054| 103.886|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    45|  3895.767| 49.470|  11,551|
| |Monroe County|     0|  0.000|  0.000|    37|  4280.426| 99.160|   8,644|
| |Mississippi County|     0|  0.000|  0.000|   174| 13201.821| 368.524|  13,180|
| |Mercer County|     0|  0.000|  0.000|    15|  4147.083| 157.984|   3,617|
| |Madison County|     0|  0.000|  0.000|    38|  3143.614| 153.635|  12,088|
| |Gasconade County|     0|  0.000|  0.000|    38|  2583.979| 135.999|  14,706|
| |Macon County|     0|  0.000|  0.000|    69|  4564.398| 94.501|  15,117|
| |Livingston County|     0|  0.000|  0.000|    65|  4268.733| 18.764|  15,227|
| |Knox County|     0|  0.000|  0.000|    36|  9093.205| 324.757|   3,959|
| |Iron County|     0|  0.000|  0.000|    27|  2666.667| 70.547|  10,125|
| |Howard County|     0|  0.000|  0.000|    71|  7099.290| 257.117|  10,001|
| |Holt County|     0|  0.000|  0.000|    46| 10447.422| 1232.926|   4,403|
| |Hickory County|     0|  0.000|  0.000|    43|  4505.448| 149.683|   9,544|
| |Ozark County|     0|  0.000|  0.000|    16|  1744.059| 31.144|   9,174|
| |Dent County|     0|  0.000|  0.000|    23|  1476.915| 100.907|  15,573|
| |Dade County|     0|  0.000|  0.000|    17|  2248.380| 37.788|   7,561|
| |Wayne County|     0|  0.000|  0.000|    68|  5282.374| 122.072|  12,873|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    73|  3991.470| 85.922|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Ralls County|     0|  0.000|  0.000|    58|  5626.152| 332.580|  10,309|
| |Phelps County|     0|  0.000|  0.000|   128|  2871.694| 124.996|  44,573|
| |Barton County|     0|  0.000|  0.000|    73|  6210.652| 48.616|  11,754|
| |Crawford County|     0|  0.000|  0.000|   115|  4807.692| 220.975|  23,920|
| |Cooper County|     0|  0.000|  0.000|   162|  9147.891| 250.075|  17,709|
| |Clinton County|     0|  0.000|  0.000|   101|  4954.137| 119.124|  20,387|
| |Clark County|     0|  0.000|  0.000|    29|  4266.588| 189.159|   6,797|
| |Chariton County|     0|  0.000|  0.000|    21|  2827.902| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    45|  3136.107| 49.779|  14,349|
| |Carroll County|     0|  0.000|  0.000|   104| 11982.947| 49.380|   8,679|
| |Atchison County|     0|  0.000|  0.000|    20|  3888.781| 55.554|   5,143|
| |Daviess County|     0|  0.000|  0.000|    19|  2295.240| 34.515|   8,278|
| |Adair County|     0|  0.000|  0.000|   184|  7260.387| 135.287|  25,343|
| |Warren County|     0|  0.000|  0.000|   264|  7405.537| 244.447|  35,649|
| |Vernon County|     0|  0.000|  0.000|    63|  3063.755| 69.473|  20,563|
| |Sullivan County|     0|  0.000|  0.000|   155| 25455.740| 258.077|   6,089|
| |Shelby County|     0|  0.000|  0.000|    43|  7251.265| 120.453|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    13|  2789.700| 61.312|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    23|  2447.590|  0.000|   9,397|
| |Ripley County|     0|  0.000|  0.000|    74|  5568.934| 236.518|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Polk County|     0|  0.000|  0.000|   243|  7558.555| 146.639|  32,149|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867|  0.000|  23,018|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties| 1,069| 347.060| N/A|61,579| 19992.169| N/A|3,080,156|
| |Clark County|   913| 402.786|  6.428|53,458| 23583.909| 271.444|2,266,715|
| |Washoe County|   127| 269.342|  2.121| 6,258| 13272.000| 141.185| 471,519|
| |Nye County|    12| 257.937|  9.212|   441|  9479.182| 101.332|  46,523|
| |Lyon County|     6| 104.330|  0.000|   271|  4712.224| 101.846|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074|  0.000|  16,831|
| |Elko County|     3| 56.842|  2.707|   640| 12126.265| 235.488|  52,778|
| |Churchill County|     1| 40.146|  0.000|    82|  3291.983| 74.557|  24,909|
| |Douglas County|     1| 20.448|  2.921|   216|  4416.726| 32.132|  48,905|
| |Lander County|     1| 180.766|  0.000|    52|  9399.855| 25.824|   5,532|
| |White Pine County|     1| 104.384|  0.000|    16|  1670.146| 14.912|   9,580|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692|  0.000|   5,183|
| |Eureka County|     0|  0.000|  0.000|     5|  2464.268| 140.815|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784|  0.000|   6,725|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     6|  1455.251| 34.649|   4,123|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,039| 178.448| N/A|66,196| 11369.128| N/A|5,822,434|
| |Milwaukee County|   466| 492.743|  1.511|22,334| 23615.720| 174.620| 945,726|
| |Racine County|    81| 412.611|  2.183| 3,689| 18791.611| 118.616| 196,311|
| |Waukesha County|    65| 160.812|  2.121| 4,854| 12008.966| 196.156| 404,198|
| |Kenosha County|    60| 353.855|  0.000| 2,792| 16466.051| 93.519| 169,561|
| |Brown County|    55| 207.906|  0.540| 4,505| 17029.432| 130.144| 264,542|
| |Dane County|    39| 71.338|  0.261| 4,874|  8915.392| 83.619| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,494|  9145.782| 46.350| 163,354|
| |Walworth County|    25| 240.690|  2.751| 1,516| 14595.448| 248.942| 103,868|
| |Washington County|    23| 169.075|  1.050| 1,259|  9255.039| 202.680| 136,034|
| |Winnebago County|    19| 110.525|  0.831| 1,288|  7492.423| 78.946| 171,907|
| |Ozaukee County|    18| 201.746|  1.601|   784|  8787.169| 147.307|  89,221|
| |Waupaca County|    16| 313.787|  2.802|   531| 10413.807| 176.505|  50,990|
| |Grant County|    16| 311.048|  2.777|   398|  7737.320| 113.866|  51,439|
| |Outagamie County|    14| 74.514|  0.000| 1,401|  7456.689| 95.043| 187,885|
| |Marathon County|    12| 88.436|  3.158|   703|  5180.851| 50.535| 135,692|
| |Fond du Lac County|     8| 77.367|  1.382|   791|  7649.681| 165.787| 103,403|
| |Clark County|     8| 230.057|  4.108|   200|  5751.423| 49.298|  34,774|
| |Sheboygan County|     8| 69.360|  0.000|   850|  7369.516| 120.142| 115,340|
| |St. Croix County|     6| 66.162|  1.575|   544|  5998.655| 66.162|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   732|  8635.232| 160.099|  84,769|
| |Dodge County|     5| 56.922|  0.000|   942| 10724.166| 174.020|  87,839|
| |Marinette County|     5| 123.916|  7.081|   501| 12416.357| 318.640|  40,350|
| |Forest County|     4| 444.247|  0.000|    61|  6774.767| 31.732|   9,004|
| |Richland County|     4| 231.857|  0.000|    38|  2202.643|  8.281|  17,252|
| |Eau Claire County|     4| 38.224|  0.000|   668|  6383.426| 106.481| 104,646|
| |Pierce County|     4| 93.558|  6.683|   247|  5777.237| 76.852|  42,754|
| |Door County|     3| 108.429|  0.000|   118|  4264.855| 61.959|  27,668|
| |Sauk County|     3| 46.553|  0.000|   513|  7960.647| 152.961|  64,442|
| |Barron County|     3| 66.307|  0.000|   328|  7249.580| 104.197|  45,244|
| |Wood County|     2| 27.398|  1.957|   381|  5219.250| 148.730|  72,999|
| |Polk County|     2| 45.680|  0.000|   143|  3266.108| 35.891|  43,783|
| |Adams County|     2| 98.912|  0.000|    94|  4648.863| 56.521|  20,220|
| |Monroe County|     2| 43.240|  0.000|   254|  5491.536| 30.886|  46,253|
| |Kewaunee County|     2| 97.876|  0.000|   143|  6998.140| 83.894|  20,434|
| |Columbia County|     2| 34.763|  2.483|   291|  5058.055| 96.841|  57,532|
| |Buffalo County|     2| 153.480|  0.000|    47|  3606.784| 32.889|  13,031|
| |Calumet County|     2| 39.929|  0.000|   402|  8025.714| 205.349|  50,089|
| |Taylor County|     2| 98.314|  7.022|    78|  3834.243| 49.157|  20,343|
| |Trempealeau County|     2| 67.456|  0.000|   370| 12479.342| 154.185|  29,649|
| |Manitowoc County|     1| 12.661|  0.000|   406|  5140.477| 110.334|  78,981|
| |Langlade County|     1| 52.113|  0.000|    74|  3856.376| 67.003|  19,189|
| |Rusk County|     1| 70.532|  0.000|    23|  1622.232| 20.152|  14,178|
| |La Crosse County|     1|  8.473|  0.000|   973|  8244.645| 71.419| 118,016|
| |Waushara County|     1| 40.912|  0.000|   128|  5236.673| 46.756|  24,443|
| |Marquette County|     1| 64.210|  0.000|    81|  5200.976|  9.173|  15,574|
| |Green County|     1| 27.056|  0.000|   220|  5952.381| 204.855|  36,960|
| |Iron County|     1| 175.840|  0.000|    85| 14946.369| 251.199|   5,687|
| |Burnett County|     1| 64.876|  0.000|    28|  1816.530| 55.608|  15,414|
| |Ashland County|     1| 64.259|  0.000|    30|  1927.773| 45.899|  15,562|
| |Bayfield County|     1| 66.507|  0.000|    37|  2460.761| 85.509|  15,036|
| |Juneau County|     1| 37.471|  0.000|   152|  5695.657| 74.943|  26,687|
| |Oconto County|     1| 26.364|  3.766|   290|  7645.663| 128.055|  37,930|
| |Jackson County|     1| 48.443|  0.000|    62|  3003.439| 27.681|  20,643|
| |Vernon County|     0|  0.000|  0.000|    77|  2498.216| 60.254|  30,822|
| |Price County|     0|  0.000|  0.000|    33|  2471.725|  0.000|  13,351|
| |Green Lake County|     0|  0.000|  0.000|    63|  3331.042| 52.874|  18,913|
| |Iowa County|     0|  0.000|  0.000|   100|  4223.330| 108.600|  23,678|
| |Oneida County|     0|  0.000|  0.000|   179|  5028.796| 152.509|  35,595|
| |Pepin County|     0|  0.000|  0.000|    46|  6312.611| 78.418|   7,287|
| |Portage County|     0|  0.000|  0.000|   470|  6641.044| 100.928|  70,772|
| |Florence County|     0|  0.000|  0.000|    16|  3725.262| 266.090|   4,295|
| |Sawyer County|     0|  0.000|  0.000|   113|  6824.496| 379.618|  16,558|
| |Shawano County|     0|  0.000|  0.000|   221|  5403.555| 73.351|  40,899|
| |Chippewa County|     0|  0.000|  0.000|   279|  4315.011| 88.377|  64,658|
| |Crawford County|     0|  0.000|  0.000|    90|  5579.319| 132.841|  16,131|
| |Vilas County|     0|  0.000|  0.000|    74|  3334.084| 122.293|  22,195|
| |Washburn County|     0|  0.000|  0.000|    50|  3180.662| 18.175|  15,720|
| |Douglas County|     0|  0.000|  0.000|   225|  5214.368| 129.118|  43,150|
| |Dunn County|     0|  0.000|  0.000|   142|  3129.959| 50.382|  45,368|
| |Lafayette County|     0|  0.000|  0.000|   172| 10321.032| 248.596|  16,665|
| |Lincoln County|     0|  0.000|  0.000|    73|  2645.599| 25.886|  27,593|
| |Menominee County|     0|  0.000|  0.000|    26|  5706.760| 125.423|   4,556|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   987| 312.830| N/A|52,823| 16742.259| N/A|3,155,070|
| |Polk County|   211| 430.471|  1.166|11,036| 22515.051| 199.643| 490,161|
| |Linn County|    89| 392.579|  0.630| 2,568| 11327.446| 106.494| 226,706|
| |Black Hawk County|    67| 510.562|  1.089| 3,322| 25314.719| 204.660| 131,228|
| |Woodbury County|    54| 523.728|  2.771| 3,828| 37126.480| 139.938| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   892| 20907.557| 147.331|  42,664|
| |Wapello County|    38| 1086.677| 20.426|   959| 27424.290| 224.689|  34,969|
| |Dallas County|    35| 374.520|  0.000| 1,996| 21358.330| 165.094|  93,453|
| |Dubuque County|    31| 318.566|  0.000| 1,816| 18661.816| 190.846|  97,311|
| |Pottawattamie County|    30| 321.868|  6.131| 1,427| 15310.173| 156.336|  93,206|
| |Tama County|    29| 1720.660|  0.000|   562| 33345.200| 76.285|  16,854|
| |Jasper County|    28| 752.992|  7.684|   501| 13473.175| 84.519|  37,185|
| |Marshall County|    27| 685.819|  3.629| 1,515| 38482.054| 250.378|  39,369|
| |Johnson County|    21| 138.944|  1.890| 2,208| 14608.972| 95.465| 151,140|
| |Cerro Gordo County|    19| 447.585|  6.731|   687| 16183.746| 178.361|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   147|  6653.089| 45.259|  22,095|
| |Scott County|    16| 92.516|  1.652| 1,863| 10772.335| 112.341| 172,943|
| |Franklin County|    15| 1489.573| 70.932|   271| 26911.619| 425.592|  10,070|
| |Story County|    15| 154.453|  1.471| 1,413| 14549.461| 361.861|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Plymouth County|    13| 516.344| 22.696|   523| 20772.928| 340.447|  25,177|
| |Buena Vista County|    12| 611.621|  0.000| 1,806| 92048.930| 87.374|  19,620|
| |Washington County|    10| 455.270|  0.000|   310| 14113.362| 65.039|  21,965|
| |Monroe County|     8| 1038.017| 18.536|    79| 10250.422| 92.680|   7,707|
| |Poweshiek County|     8| 432.339|  0.000|   163|  8808.906| 30.881|  18,504|
| |Webster County|     8| 222.816|  0.000|   899| 25038.993| 342.182|  35,904|
| |Bremer County|     7| 279.307|  0.000|   245|  9775.756| 102.603|  25,062|
| |Guthrie County|     5| 467.771|  0.000|   147| 13752.456| 200.473|  10,689|
| |O'Brien County|     5| 363.557| 10.387|   150| 10906.711| 93.486|  13,753|
| |Lee County|     5| 148.558|  8.489|   167|  4961.821| 212.225|  33,657|
| |Emmet County|     5| 543.006| 15.514|   200| 21720.243| 124.116|   9,208|
| |Montgomery County|     4| 403.348|  0.000|    64|  6453.565| 72.026|   9,917|
| |Lucas County|     4| 465.116|  0.000|    78|  9069.767| 116.279|   8,600|
| |Allamakee County|     4| 292.248|  0.000|   163| 11909.111| 83.499|  13,687|
| |Henry County|     4| 200.461|  0.000|   166|  8319.134| 279.214|  19,954|
| |Clinton County|     4| 86.153|  3.077|   537| 11566.047| 390.766|  46,429|
| |Dickinson County|     4| 231.777|  0.000|   392| 22714.104| 82.777|  17,258|
| |Boone County|     3| 114.355|  0.000|   295| 11244.949| 196.038|  26,234|
| |Crawford County|     3| 178.359|  0.000|   757| 45005.945| 229.319|  16,820|
| |Floyd County|     3| 191.791|  9.133|   179| 11443.549| 200.924|  15,642|
| |Warren County|     3| 58.291|  5.552|   606| 11774.764| 102.703|  51,466|
| |Appanoose County|     3| 241.429|  0.000|    58|  4667.632| 103.470|  12,426|
| |Sioux County|     3| 86.071|  0.000|   698| 20025.821| 250.015|  34,855|
| |Union County|     3| 245.078| 23.341|    88|  7188.955| 128.374|  12,241|
| |Clarke County|     3| 319.319|  0.000|   212| 22565.194| 152.057|   9,395|
| |Clayton County|     3| 170.950|  0.000|   122|  6951.963| 146.528|  17,549|
| |Jones County|     2| 96.707|  0.000|   138|  6672.791| 41.446|  20,681|
| |Des Moines County|     2| 51.325|  0.000|   271|  6954.603| 311.619|  38,967|
| |Davis County|     2| 222.222|  0.000|    69|  7666.667| 142.857|   9,000|
| |Cass County|     2| 155.812| 11.129|    95|  7401.060| 233.718|  12,836|
| |Carroll County|     2| 99.182|  7.084|   223| 11058.765| 212.532|  20,165|
| |Calhoun County|     2| 206.868|  0.000|    97| 10033.099| 206.868|   9,668|
| |Butler County|     2| 138.514|  0.000|   141|  9765.219| 197.877|  14,439|
| |Madison County|     2| 122.414|  0.000|   136|  8324.152| 122.414|  16,338|
| |Pocahontas County|     2| 302.160|  0.000|   122| 18431.787| 129.497|   6,619|
| |Wayne County|     2| 310.511| 22.179|    26|  4036.640| 133.076|   6,441|
| |Lyon County|     2| 170.140|  0.000|   130| 11059.124| 194.446|  11,755|
| |Humboldt County|     2| 209.249| 14.946|   135| 14124.294| 254.088|   9,558|
| |Hancock County|     2| 188.147|  0.000|   128| 12041.392| 80.634|  10,630|
| |Clay County|     1| 62.438|  0.000|   219| 13673.826| 205.152|  16,016|
| |Winneshiek County|     1| 50.023|  0.000|   113|  5652.544| 114.337|  19,991|
| |Shelby County|     1| 87.306|  0.000|   193| 16850.009| 112.250|  11,454|
| |Audubon County|     1| 181.951|  0.000|    30|  5458.515| 51.986|   5,496|
| |Van Buren County|     1| 141.965|  0.000|    42|  5962.521| 121.684|   7,044|
| |Wright County|     1| 79.605|  0.000|   497| 39563.764| 272.932|  12,562|
| |Keokuk County|     1| 97.599|  0.000|    43|  4196.760| 83.656|  10,246|
| |Jackson County|     1| 51.443|  0.000|   171|  8796.749| 110.235|  19,439|
| |Iowa County|     1| 61.789|  0.000|   100|  6178.942| 17.654|  16,184|
| |Harrison County|     1| 71.179|  0.000|   118|  8399.174| 91.516|  14,049|
| |Hamilton County|     1| 67.691|  0.000|   264| 17870.439| 154.722|  14,773|
| |Grundy County|     1| 81.753|  0.000|    91|  7439.503| 140.148|  12,232|
| |Delaware County|     1| 58.785|  0.000|   139|  8171.183| 201.550|  17,011|
| |Mills County|     1| 66.186|  9.455|    99|  6552.386| 94.551|  15,109|
| |Monona County|     1| 116.077| 16.582|    93| 10795.125| 33.165|   8,615|
| |Benton County|     1| 38.994|  0.000|   172|  6706.960| 66.847|  25,645|
| |Buchanan County|     1| 47.226|  0.000|   149|  7036.600| 134.930|  21,175|
| |Cedar County|     1| 53.686|  0.000|   137|  7354.915| 30.677|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   114| 10146.862| 76.292|  11,235|
| |Ringgold County|     1| 204.332|  0.000|    25|  5108.296| 87.571|   4,894|
| |Fremont County|     0|  0.000|  0.000|    46|  6609.195| 82.102|   6,960|
| |Page County|     0|  0.000|  0.000|   102|  6751.837| 75.651|  15,107|
| |Osceola County|     0|  0.000|  0.000|    89| 14937.899| 143.864|   5,958|
| |Mitchell County|     0|  0.000|  0.000|    83|  7840.544| 67.475|  10,586|
| |Marion County|     0|  0.000|  0.000|   209|  6285.147| 150.362|  33,253|
| |Kossuth County|     0|  0.000|  0.000|   106|  7155.877| 154.305|  14,813|
| |Jefferson County|     0|  0.000|  0.000|    94|  5138.016| 62.468|  18,295|
| |Ida County|     0|  0.000|  0.000|    34|  4956.268| 62.474|   6,860|
| |Hardin County|     0|  0.000|  0.000|   193| 11456.726| 76.322|  16,846|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473|  0.000|   8,888|
| |Fayette County|     0|  0.000|  0.000|   105|  5343.511| 152.672|  19,650|
| |Decatur County|     0|  0.000|  0.000|    30|  3811.944| 127.065|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    68|  5698.483| 167.602|  11,933|
| |Adams County|     0|  0.000|  0.000|    17|  4719.600| 39.661|   3,602|
| |Adair County|     0|  0.000|  0.000|    40|  5592.841| 199.744|   7,152|
| |Howard County|     0|  0.000|  0.000|    67|  7316.008| 280.785|   9,158|
| |Palo Alto County|     0|  0.000|  0.000|   103| 11591.267| 273.303|   8,886|
| |Sac County|     0|  0.000|  0.000|    90|  9258.307| 73.479|   9,721|
| |Taylor County|     0|  0.000|  0.000|   104| 16990.688| 140.033|   6,121|
| |Winnebago County|     0|  0.000|  0.000|   117| 11299.981| 455.311|  10,354|
| |Worth County|     0|  0.000|  0.000|    71|  9619.293| 96.774|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   818| 183.093| N/A|39,691|  8884.043| N/A|4,467,673|
| |Jefferson County|   251| 327.353|  2.608| 9,629| 12558.086| 268.478| 766,757|
| |Fayette County|    50| 154.726|  1.326| 3,460| 10707.036| 137.485| 323,152|
| |Kenton County|    41| 245.512|  0.000| 1,526|  9137.834| 94.099| 166,998|
| |Hopkins County|    35| 783.243|  6.394|   440|  9846.484| 60.741|  44,686|
| |Graves County|    26| 697.687|  3.833|   582| 15617.453| 84.336|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,157|  8661.411| 56.680| 133,581|
| |Logan County|    23| 848.646|  0.000|   359| 13246.255| 163.404|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,802| 21084.156| 173.068| 132,896|
| |Shelby County|    21| 428.362|  0.000|   820| 16726.501| 134.045|  49,024|
| |Adair County|    19| 989.480|  0.000|   233| 12134.153| 208.312|  19,202|
| |Oldham County|    17| 254.495|  4.277|   675| 10104.942| 91.960|  66,799|
| |Butler County|    15| 1164.687|  0.000|   304| 23604.317| 122.015|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   158| 11853.853| 85.742|  13,329|
| |Campbell County|    13| 138.913|  0.000|   622|  6646.435| 77.852|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   115|  9465.021| 82.305|  12,150|
| |Muhlenberg County|    11| 359.219|  0.000|   639| 20867.350| 60.647|  30,622|
| |Casey County|    11| 680.735|  8.841|   213| 13181.509| 212.177|  16,159|
| |Grayson County|    11| 416.241|  0.000|   220|  8324.819| 97.303|  26,427|
| |Franklin County|    11| 215.724| 11.206|   357|  7001.236| 117.668|  50,991|
| |Christian County|    10| 141.922|  4.055|   540|  7663.814| 77.044|  70,461|
| |Ohio County|     9| 375.094|  5.954|   365| 15212.136| 53.585|  23,994|
| |Daviess County|     9| 88.660|  0.000|   827|  8146.900| 87.253| 101,511|
| |Knox County|     8| 256.863|  0.000|   269|  8637.020| 155.953|  31,145|
| |Allen County|     8| 375.323|  0.000|   236| 11072.015| 67.022|  21,315|
| |Hardin County|     8| 72.099|  0.000|   750|  6759.314| 155.786| 110,958|
| |Clark County|     7| 193.034|  0.000|   189|  5211.924| 90.608|  36,263|
| |Gallatin County|     7| 789.266|  0.000|    82|  9245.687| 32.215|   8,869|
| |Simpson County|     7| 376.911|  0.000|   173|  9315.098| 176.918|  18,572|
| |Grant County|     6| 239.339|  5.699|   128|  5105.908| 39.890|  25,069|
| |Bell County|     5| 192.071|  5.488|   350| 13444.991| 208.535|  26,032|
| |Laurel County|     5| 82.219|  0.000|   480|  7893.049| 110.409|  60,813|
| |Russell County|     5| 278.971|  0.000|   140|  7811.192| 231.148|  17,923|
| |Pulaski County|     5| 76.948|  0.000|   385|  5924.991| 167.087|  64,979|
| |McCracken County|     5| 76.432|  2.184|   409|  6252.102| 91.718|  65,418|
| |Clay County|     5| 251.244|  0.000|   190|  9547.259| 272.779|  19,901|
| |Calloway County|     5| 128.202|  3.663|   294|  7538.268| 183.145|  39,001|
| |Bullitt County|     5| 61.217|  0.000|   448|  5485.087| 131.180|  81,676|
| |Boyd County|     4| 85.620|  3.058|   203|  4345.220| 36.694|  46,718|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686|  0.000|   8,210|
| |Perry County|     4| 155.292|  5.546|   256|  9938.660| 166.384|  25,758|
| |Taylor County|     3| 116.419|  5.544|   158|  6131.398| 116.419|  25,769|
| |Pike County|     3| 51.835|  0.000|   270|  4665.146| 51.835|  57,876|
| |Henderson County|     3| 66.357|  0.000|   376|  8316.744| 101.115|  45,210|
| |Henry County|     3| 186.035|  8.859|   146|  9053.702| 230.329|  16,126|
| |Barren County|     3| 67.798|  3.228|   432|  9762.932| 219.537|  44,249|
| |Meade County|     3| 104.998|  5.000|   103|  3604.928| 44.999|  28,572|
| |Harlan County|     3| 115.340|  0.000|   257|  9880.815| 137.310|  26,010|
| |Nelson County|     2| 43.259|  0.000|   255|  5515.541| 114.328|  46,233|
| |Breckinridge County|     2| 97.671|  0.000|    87|  4248.669| 90.694|  20,477|
| |Marshall County|     2| 64.309|  0.000|   155|  4983.923| 78.089|  31,100|
| |Lincoln County|     2| 81.470|  0.000|   121|  4928.918| 87.289|  24,549|
| |Monroe County|     2| 187.793|  0.000|   107| 10046.948| 174.380|  10,650|
| |Carroll County|     2| 188.129|  0.000|   170| 15990.970| 161.253|  10,631|
| |Green County|     2| 182.799|  0.000|    57|  5209.761| 261.141|  10,941|
| |Fulton County|     2| 335.064|  0.000|   101| 16920.757| 430.797|   5,969|
| |Floyd County|     2| 56.197|  0.000|   119|  3343.730| 96.338|  35,589|
| |Carter County|     2| 74.635|  5.331|   105|  3918.349| 21.324|  26,797|
| |Metcalfe County|     2| 198.590|  0.000|    66|  6553.470| 85.110|  10,071|
| |Clinton County|     1| 97.867|  0.000|    48|  4697.592| 167.771|  10,218|
| |Carlisle County|     1| 210.084|  0.000|    50| 10504.202| 210.084|   4,760|
| |Bourbon County|     1| 50.536|  0.000|    99|  5003.032| 115.510|  19,788|
| |Nicholas County|     1| 137.571| 19.653|    21|  2888.981| 19.653|   7,269|
| |Greenup County|     1| 28.492|  0.000|   147|  4188.273| 150.599|  35,098|
| |Larue County|     1| 69.454|  0.000|    67|  4653.424| 109.142|  14,398|
| |Whitley County|     1| 27.576|  0.000|   170|  4687.845| 27.576|  36,264|
| |Webster County|     1| 77.268|  0.000|    95|  7340.442| 66.230|  12,942|
| |Anderson County|     1| 43.962|  0.000|    92|  4044.489| 50.242|  22,747|
| |Bath County|     1| 80.000|  0.000|    41|  3280.000| 45.714|  12,500|
| |Crittenden County|     1| 113.559|  0.000|    34|  3861.004| 48.668|   8,806|
| |Lewis County|     1| 75.330| 10.761|    86|  6478.343| 484.262|  13,275|
| |Livingston County|     1| 108.767|  0.000|    37|  4024.364| 31.076|   9,194|
| |Knott County|     1| 67.540|  0.000|    79|  5335.675| 183.323|  14,806|
| |McLean County|     1| 108.613|  0.000|    44|  4778.973| 31.032|   9,207|
| |Mason County|     1| 58.582|  0.000|    59|  3456.356| 41.845|  17,070|
| |Madison County|     1| 10.754|  0.000|   676|  7269.833| 245.810|  92,987|
| |Bracken County|     0|  0.000|  0.000|    37|  4456.221| 51.616|   8,303|
| |Caldwell County|     0|  0.000|  0.000|    57|  4471.640| 44.828|  12,747|
| |Harrison County|     0|  0.000|  0.000|   123|  6512.761| 15.128|  18,886|
| |Hancock County|     0|  0.000|  0.000|    54|  6191.241| 65.516|   8,722|
| |Garrard County|     0|  0.000|  0.000|    93|  5264.350| 113.212|  17,666|
| |Fleming County|     0|  0.000|  0.000|    64|  4389.274| 48.987|  14,581|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 50.637|  14,106|
| |Elliott County|     0|  0.000|  0.000|    15|  1995.477| 76.018|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    67| 10130.027| 215.992|   6,614|
| |Breathitt County|     0|  0.000|  0.000|    33|  2612.827| 22.622|  12,630|
| |Boyle County|     0|  0.000|  0.000|   172|  5721.890| 85.543|  30,060|
| |Spencer County|     0|  0.000|  0.000|   141|  7286.445| 147.648|  19,351|
| |Todd County|     0|  0.000|  0.000|    38|  3090.939| 34.860|  12,294|
| |Leslie County|     0|  0.000|  0.000|    38|  3847.322| 101.245|   9,877|
| |Lee County|     0|  0.000|  0.000|     7|   945.563| 19.297|   7,403|
| |Lawrence County|     0|  0.000|  0.000|    38|  2480.904| 18.653|  15,317|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Rowan County|     0|  0.000|  0.000|    88|  3597.711| 105.128|  24,460|
| |Woodford County|     0|  0.000|  0.000|   183|  6845.216| 144.279|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    18|  2515.020| 79.842|   7,157|
| |Scott County|     0|  0.000|  0.000|   437|  7666.129| 147.859|  57,004|
| |Wayne County|     0|  0.000|  0.000|    80|  3934.491| 91.336|  20,333|
| |Washington County|     0|  0.000|  0.000|   102|  8433.237| 188.980|  12,095|
| |Union County|     0|  0.000|  0.000|    76|  5284.751| 109.271|  14,381|
| |Trimble County|     0|  0.000|  0.000|    35|  4131.744| 50.593|   8,471|
| |Trigg County|     0|  0.000|  0.000|    60|  4095.284| 58.504|  14,651|
| |Ballard County|     0|  0.000|  0.000|    37|  4690.669| 36.221|   7,888|
| |Letcher County|     0|  0.000|  0.000|    67|  3108.616| 53.025|  21,553|
| |McCreary County|     0|  0.000|  0.000|    54|  3133.887| 107.779|  17,231|
| |Magoffin County|     0|  0.000|  0.000|    53|  4358.194| 164.460|  12,161|
| |Marion County|     0|  0.000|  0.000|   142|  7367.820| 133.421|  19,273|
| |Hart County|     0|  0.000|  0.000|   110|  5778.828| 75.050|  19,035|
| |Hickman County|     0|  0.000|  0.000|    62| 14155.251| 424.005|   4,380|
| |Jessamine County|     0|  0.000|  0.000|   377|  6966.645| 87.116|  54,115|
| |Johnson County|     0|  0.000|  0.000|    84|  3785.830| 225.347|  22,188|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Powell County|     0|  0.000|  0.000|    69|  5582.976| 115.590|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    51|  3495.545| 68.540|  14,590|
| |Owsley County|     0|  0.000|  0.000|    16|  3624.009| 129.429|   4,415|
| |Owen County|     0|  0.000|  0.000|    65|  5962.756| 222.784|  10,901|
| |Morgan County|     0|  0.000|  0.000|    36|  2704.937| 53.669|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   141|  5007.636| 101.472|  28,157|
| |Mercer County|     0|  0.000|  0.000|    92|  4194.593| 58.620|  21,933|
| |Martin County|     0|  0.000|  0.000|    42|  3751.675| 76.565|  11,195|
| |Rockcastle County|     0|  0.000|  0.000|    92|  5510.632| 179.695|  16,695|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   718| 342.422| N/A|22,189| 10582.170| N/A|2,096,829|
| |McKinley County|   233| 3264.814| 14.012| 4,125| 57799.823| 136.117|  71,367|
| |San Juan County|   187| 1508.575|  3.457| 3,104| 25040.740| 65.690| 123,958|
| |Bernalillo County|   139| 204.676|  1.052| 5,365|  7899.918| 42.913| 679,121|
| |Dona Ana County|    35| 160.407|  2.619| 2,640| 12099.269| 113.922| 218,195|
| |Sandoval County|    33| 224.875|  0.000| 1,161|  7911.522| 23.364| 146,748|
| |Cibola County|    19| 712.277|  5.355|   383| 14358.013| 74.977|  26,675|
| |Otero County|    11| 162.987|  2.117|   209|  3096.755| 12.700|  67,490|
| |Rio Arriba County|    10| 256.931| 11.011|   326|  8375.941| 29.364|  38,921|
| |Chaves County|     6| 92.858|  0.000|   544|  8419.098| 181.294|  64,615|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024|  0.000|  16,637|
| |Lea County|     6| 84.424|  2.010|   930| 13085.690| 265.332|  71,070|
| |Luna County|     5| 210.890|  6.025|   257| 10839.765| 18.076|  23,709|
| |Eddy County|     5| 85.529|  2.444|   376|  6431.748| 171.057|  58,460|
| |Valencia County|     4| 52.159|  0.000|   464|  6050.490| 67.062|  76,688|
| |Curry County|     3| 61.282|  2.918|   597| 12195.122| 113.809|  48,954|
| |Santa Fe County|     3| 19.952|  0.000|   701|  4662.206| 44.655| 150,358|
| |Union County|     2| 492.732|  0.000|    30|  7390.983|  0.000|   4,059|
| |Lincoln County|     2| 102.187|  0.000|   157|  8021.664| 211.673|  19,572|
| |Grant County|     2| 74.080|  0.000|    72|  2666.864|  5.291|  26,998|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411|  0.000|  11,941|
| |Roosevelt County|     1| 54.054|  0.000|   175|  9459.459| 69.498|  18,500|
| |Quay County|     1| 121.168|  0.000|    50|  6058.403| 276.956|   8,253|
| |Torrance County|     1| 64.679|  0.000|    63|  4074.769| 18.480|  15,461|
| |Sierra County|     1| 92.670|  0.000|    34|  3150.774| 26.477|  10,791|
| |Taos County|     1| 30.560|  0.000|   115|  3514.348| 26.194|  32,723|
| |Catron County|     1| 283.527|  0.000|     6|  1701.162| 40.504|   3,527|
| |San Miguel County|     0|  0.000|  0.000|    55|  2016.351| 57.610|  27,277|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Los Alamos County|     0|  0.000|  0.000|    24|  1239.093|  7.376|  19,369|
| |Hidalgo County|     0|  0.000|  0.000|    93| 22153.406| 102.089|   4,198|
| |Harding County|     0|  0.000|  0.000|     2|  3200.000| 228.571|     625|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   665| 168.058| N/A|48,709| 12309.668| N/A|3,956,971|
| |Oklahoma County|   132| 165.531|  3.583|11,715| 14690.871| 188.103| 797,434|
| |Tulsa County|   116| 178.036|  1.973|11,443| 17562.681| 193.165| 651,552|
| |Cleveland County|    58| 204.215|  1.509| 3,215| 11319.865| 99.593| 284,014|
| |Washington County|    39| 756.885|  0.000|   705| 13682.147| 191.301|  51,527|
| |McCurtain County|    28| 852.827|  0.000|   896| 27290.448| 165.344|  32,832|
| |Wagoner County|    23| 282.941|  0.000|   968| 11908.130| 182.769|  81,289|
| |Rogers County|    21| 227.128|  7.725| 1,139| 12318.974| 236.398|  92,459|
| |Delaware County|    20| 465.019|  3.322|   473| 10997.698| 139.506|  43,009|
| |Caddo County|    19| 660.594| 14.901|   470| 16341.005| 223.509|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   588|  8647.440| 165.974|  67,997|
| |Creek County|    15| 209.726|  1.997|   681|  9521.546| 147.807|  71,522|
| |Osage County|    12| 255.520|  3.042|   564| 12009.454| 419.783|  46,963|
| |Comanche County|    11| 91.098|  1.183|   884|  7320.972| 62.704| 120,749|
| |Kay County|    11| 252.653|  0.000|   267|  6132.574| 75.468|  43,538|
| |Canadian County|     9| 60.685|  1.927| 1,339|  9028.630| 110.775| 148,306|
| |Pottawatomie County|     9| 123.981|  0.000|   595|  8196.495| 289.288|  72,592|
| |Mayes County|     8| 194.647|  6.952|   368|  8953.771| 159.889|  41,100|
| |Garfield County|     8| 131.027|  7.019|   617| 10105.477| 367.344|  61,056|
| |Greer County|     8| 1400.560|  0.000|    85| 14880.952| 50.020|   5,712|
| |Jackson County|     7| 285.365|  0.000|   538| 21932.328| 87.357|  24,530|
| |Texas County|     7| 350.298|  0.000| 1,079| 53995.897| 164.425|  19,983|
| |Grady County|     7| 125.372|  0.000|   472|  8453.630| 76.758|  55,834|
| |Adair County|     6| 270.343|  0.000|   383| 17256.916| 270.343|  22,194|
| |Carter County|     5| 103.926|  2.969|   370|  7690.549| 83.141|  48,111|
| |Seminole County|     5| 206.118|  0.000|   257| 10594.443| 123.671|  24,258|
| |Garvin County|     4| 144.347|  0.000|   242|  8732.994| 77.329|  27,711|
| |Sequoyah County|     4| 96.226|  0.000|   439| 10560.754| 343.663|  41,569|
| |Pittsburg County|     4| 91.630|  3.272|   437| 10010.537| 248.709|  43,654|
| |McClain County|     4| 98.829|  0.000|   483| 11933.587| 134.125|  40,474|
| |Payne County|     4| 48.909|  0.000|   800|  9781.864| 104.806|  81,784|
| |Lincoln County|     3| 86.017|  4.096|   248|  7110.703| 331.778|  34,877|
| |Stephens County|     3| 69.536|  0.000|   218|  5052.963| 56.291|  43,143|
| |Pawnee County|     3| 183.195|  0.000|   168| 10258.915| 261.707|  16,376|
| |Ottawa County|     3| 96.379|  0.000|   418| 13428.856| 215.706|  31,127|
| |Okmulgee County|     3| 77.993|  0.000|   508| 13206.811| 144.844|  38,465|
| |Latimer County|     2| 198.551| 14.182|   100|  9927.529| 113.457|  10,073|
| |Pontotoc County|     2| 52.241|  0.000|   215|  5615.923| 52.241|  38,284|
| |McIntosh County|     2| 102.062|  7.290|   207| 10563.380| 189.543|  19,596|
| |Bryan County|     2| 41.671|  2.977|   512| 10667.778| 160.731|  47,995|
| |Noble County|     2| 179.678|  0.000|    92|  8265.205| 102.673|  11,131|
| |Cherokee County|     2| 41.104|  0.000|   535| 10995.335| 264.240|  48,657|
| |Cotton County|     2| 352.983|  0.000|    21|  3706.318| 75.639|   5,666|
| |Hughes County|     2| 150.614|  0.000|   179| 13479.931| 441.083|  13,279|
| |Logan County|     1| 20.829|  0.000|   244|  5082.169| 65.461|  48,011|
| |Kiowa County|     1| 114.837|  0.000|    33|  3789.619| 65.621|   8,708|
| |Choctaw County|     1| 68.157|  0.000|   209| 14244.820| 204.471|  14,672|
| |Nowata County|     1| 99.246|  0.000|    63|  6252.481| 70.890|  10,076|
| |Marshall County|     1| 59.063|  0.000|   121|  7146.654| 118.127|  16,931|
| |Okfuskee County|     1| 83.382|  0.000|    83|  6920.704| 190.587|  11,993|
| |Major County|     1| 131.079|  0.000|    40|  5243.151| 112.353|   7,629|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 19.704|   7,250|
| |Atoka County|     1| 72.685| 10.384|    88|  6396.279| 186.904|  13,758|
| |Beckham County|     1| 45.748|  0.000|   101|  4620.522| 274.486|  21,859|
| |Craig County|     1| 70.711| 10.102|    94|  6646.867| 80.813|  14,142|
| |Le Flore County|     1| 20.059|  0.000|   436|  8745.712| 260.767|  49,853|
| |Haskell County|     1| 79.195| 11.314|    88|  6969.193| 316.781|  12,627|
| |Roger Mills County|     1| 279.096|  0.000|     9|  2511.862| 39.871|   3,583|
| |Coal County|     0|  0.000|  0.000|    46|  8371.247| 233.979|   5,495|
| |Alfalfa County|     0|  0.000|  0.000|     6|  1052.262| 75.162|   5,702|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672|  0.000|   3,859|
| |Dewey County|     0|  0.000|  0.000|    13|  2657.943| 87.624|   4,891|
| |Custer County|     0|  0.000|  0.000|   241|  8309.485| 172.396|  29,003|
| |Cimarron County|     0|  0.000|  0.000|    11|  5147.403| 668.494|   2,137|
| |Blaine County|     0|  0.000|  0.000|    46|  4878.566| 60.603|   9,429|
| |Beaver County|     0|  0.000|  0.000|    40|  7531.538| 107.593|   5,311|
| |Grant County|     0|  0.000|  0.000|    17|  3923.379| 65.939|   4,333|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817|  0.000|   2,653|
| |Harper County|     0|  0.000|  0.000|    13|  3524.946| 116.207|   3,688|
| |Jefferson County|     0|  0.000|  0.000|    34|  5664.778| 23.802|   6,002|
| |Woodward County|     0|  0.000|  0.000|    52|  2572.856| 106.024|  20,211|
| |Woods County|     0|  0.000|  0.000|    21|  2388.263| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    35|  3206.303| 91.609|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   116| 10454.218| 102.997|  11,096|
| |Murray County|     0|  0.000|  0.000|    82|  5826.760| 91.360|  14,073|
| |Love County|     0|  0.000|  0.000|    83|  8095.192| 111.466|  10,253|
| |Kingfisher County|     0|  0.000|  0.000|   160| 10149.064| 190.295|  15,765|
| |Johnston County|     0|  0.000|  0.000|    55|  4961.660| 90.212|  11,085|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   603| 199.814| N/A|52,303| 17331.477| N/A|3,017,804|
| |Pulaski County|    88| 224.541|  1.094| 6,146| 15682.132| 184.809| 391,911|
| |Washington County|    53| 221.584|  1.195| 6,442| 26932.902| 78.838| 239,187|
| |Benton County|    43| 154.044|  0.000| 4,933| 17672.073| 71.137| 279,141|
| |Jefferson County|    41| 613.552|  2.138| 1,710| 25589.609| 290.742|  66,824|
| |Crittenden County|    24| 500.469|  2.979| 1,493| 31133.354| 369.394|  47,955|
| |Sebastian County|    22| 172.108|  2.235| 2,456| 19213.468| 253.691| 127,827|
| |Union County|    20| 517.036|  7.386|   561| 14502.870| 210.508|  38,682|
| |Yell County|    18| 843.447|  6.694| 1,088| 50981.678| 140.574|  21,341|
| |Garland County|    17| 171.050|  1.437| 1,201| 12084.197| 205.548|  99,386|
| |Craighead County|    14| 126.890|  2.590| 1,498| 13577.203| 160.554| 110,332|
| |Mississippi County|    14| 344.395|  0.000| 1,159| 28510.984| 442.794|  40,651|
| |Hot Spring County|    13| 384.946|  8.460| 1,644| 48680.821| 380.715|  33,771|
| |Pope County|    12| 187.289|  4.459| 1,465| 22864.902| 325.527|  64,072|
| |Columbia County|    12| 511.574|  0.000|   244| 10402.012| 164.435|  23,457|
| |Lincoln County|    12| 921.376|  0.000| 1,348| 103501.229| 1371.095|  13,024|
| |Newton County|    11| 1418.806| 92.130|   107| 13801.109| 18.426|   7,753|
| |Randolph County|    11| 612.540| 55.685|   265| 14756.654| 365.933|  17,958|
| |Sevier County|    11| 646.792|  8.400| 1,067| 62738.872| 629.993|  17,007|
| |Lawrence County|     9| 548.580|  0.000|   231| 14080.215| 148.029|  16,406|
| |Chicot County|     9| 889.504| 14.119|   925| 91421.229| 2626.154|  10,118|
| |Nevada County|     9| 1090.645|  0.000|   147| 17813.863| 69.247|   8,252|
| |Phillips County|     9| 506.130|  0.000|   355| 19964.009| 241.014|  17,782|
| |Lee County|     8| 903.240|  0.000|   979| 110534.041| 1338.731|   8,857|
| |Saline County|     8| 65.340|  2.334| 1,277| 10429.854| 212.354| 122,437|
| |Carroll County|     7| 246.653|  0.000|   395| 13918.252| 181.214|  28,380|
| |Ashley County|     6| 305.235|  7.267|   363| 18466.704| 239.827|  19,657|
| |Faulkner County|     6| 47.616|  0.000| 1,402| 11126.366| 94.099| 126,007|
| |Sharp County|     5| 286.664|  0.000|   128|  7338.608| 131.047|  17,442|
| |Crawford County|     5| 79.043|  2.258|   746| 11793.161| 250.678|  63,257|
| |Clay County|     5| 343.619|  9.818|   147| 10102.398| 107.995|  14,551|
| |Cleburne County|     5| 200.650|  0.000|   228|  9149.645| 149.054|  24,919|
| |Miller County|     5| 115.588|  0.000|   538| 12437.293| 66.050|  43,257|
| |Bradley County|     4| 371.644|  0.000|   227| 21090.774| 305.279|  10,763|
| |Cross County|     4| 243.620|  0.000|   228| 13886.351| 208.817|  16,419|
| |Howard County|     4| 302.984|  0.000|   376| 28480.533| 367.910|  13,202|
| |Poinsett County|     4| 170.010|  6.072|   347| 14748.385| 370.379|  23,528|
| |Conway County|     3| 143.913|  0.000|   168|  8059.100| 102.795|  20,846|
| |Little River County|     3| 244.718| 23.306|   219| 17864.426| 442.823|  12,259|
| |Drew County|     3| 164.663|  0.000|   270| 14819.694| 478.308|  18,219|
| |St. Francis County|     3| 120.029|  0.000| 1,243| 49731.936| 114.313|  24,994|
| |Ouachita County|     3| 128.304|  6.110|   118|  5046.617| 97.755|  23,382|
| |White County|     3| 38.094|  1.814|   408|  5180.755| 148.747|  78,753|
| |Greene County|     3| 66.189|  3.152|   544| 12002.206| 185.959|  45,325|
| |Clark County|     2| 89.606|  6.400|   192|  8602.151| 96.006|  22,320|
| |Boone County|     2| 53.430|  0.000|   230|  6144.475| 68.696|  37,432|
| |Arkansas County|     2| 114.377|  8.170|   249| 14239.963| 228.754|  17,486|
| |Van Buren County|     2| 120.882|  0.000|    58|  3505.591| 43.172|  16,545|
| |Cleveland County|     2| 251.383|  0.000|   121| 15208.648| 341.162|   7,956|
| |Madison County|     2| 120.656|  0.000|   279| 16831.564| 77.565|  16,576|
| |Lonoke County|     2| 27.282|  0.000|   580|  7911.716| 109.127|  73,309|
| |Lafayette County|     2| 301.932|  0.000|    61|  9208.937| 150.966|   6,624|
| |Johnson County|     2| 75.250|  0.000|   695| 26149.447| 134.375|  26,578|
| |Independence County|     2| 52.875|  3.777|   621| 16417.713| 317.250|  37,825|
| |Franklin County|     2| 112.899|  0.000|   141|  7959.356| 112.899|  17,715|
| |Desha County|     2| 176.041|  0.000|   211| 18572.309| 176.041|  11,361|
| |Dallas County|     2| 285.347| 40.764|    68|  9701.812| 81.528|   7,009|
| |Hempstead County|     2| 92.885|  0.000|   271| 12585.919| 159.231|  21,532|
| |Stone County|     1| 79.962|  0.000|    87|  6956.661| 205.616|  12,506|
| |Polk County|     1| 50.090|  0.000|   171|  8565.418| 164.582|  19,964|
| |Pike County|     1| 93.301|  0.000|   144| 13435.342| 479.834|  10,718|
| |Montgomery County|     1| 111.284|  0.000|    44|  4896.506| 95.386|   8,986|
| |Logan County|     1| 46.585|  0.000|   338| 15745.831| 432.578|  21,466|
| |Jackson County|     1| 59.812|  0.000|   124|  7416.712| 59.812|  16,719|
| |Woodruff County|     0|  0.000|  0.000|    25|  3955.696| 67.812|   6,320|
| |Scott County|     0|  0.000|  0.000|    78|  7586.811| 236.219|  10,281|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 13.664|  10,455|
| |Monroe County|     0|  0.000|  0.000|    76| 11341.591| 298.463|   6,701|
| |Marion County|     0|  0.000|  0.000|    34|  2036.660| 42.787|  16,694|
| |Izard County|     0|  0.000|  0.000|    61|  4475.750| 83.855|  13,629|
| |Grant County|     0|  0.000|  0.000|   154|  8431.426| 132.963|  18,265|
| |Fulton County|     0|  0.000|  0.000|    49|  3927.226| 57.248|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    16|  3083.446|  0.000|   5,189|
| |Baxter County|     0|  0.000|  0.000|    89|  2122.484| 61.324|  41,932|
| |Searcy County|     0|  0.000|  0.000|    34|  4314.173| 36.254|   7,881|
| |Prairie County|     0|  0.000|  0.000|   111| 13768.296| 265.797|   8,062|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   597| 845.910| N/A|13,273| 18806.970| N/A| 705,749|
| |District of Columbia|   597| 845.910|  1.215|13,273| 18806.970| 94.327| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   593| 608.977| N/A|16,273| 16711.441| N/A| 973,764|
| |New Castle County|   293| 524.382|  0.511| 7,580| 13565.923| 86.161| 558,753|
| |Sussex County|   192| 819.725|  0.000| 6,197| 26457.466| 212.860| 234,225|
| |Kent County|   108| 597.391|  0.000| 2,496| 13806.379| 159.620| 180,786|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   423| 311.096| N/A| 7,004|  5151.095| N/A|1,359,711|
| |Hillsborough County|   281| 673.821|  0.685| 3,942|  9452.671| 29.803| 417,025|
| |Rockingham County|    96| 309.908|  0.000| 1,729|  5581.579| 17.525| 309,769|
| |Merrimack County|    23| 151.924|  1.887|   474|  3130.966|  7.549| 151,391|
| |Strafford County|    13| 99.515|  0.000|   367|  2809.397|  7.655| 130,633|
| |Belknap County|     4| 65.250|  0.000|   121|  1973.802| 13.982|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   107|  1406.322| 15.021|  76,085|
| |Carroll County|     1| 20.446|  0.000|    96|  1962.789|  5.842|  48,910|
| |Grafton County|     1| 11.125|  0.000|   107|  1190.397|  6.357|  89,886|
| |Sullivan County|     1| 23.177|  0.000|    44|  1019.793| 13.244|  43,146|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  0.000|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   406| 139.360| N/A|34,614| 11881.315| N/A|2,913,314|
| |Johnson County|   108| 179.283|  1.186| 6,582| 10926.277| 185.448| 602,401|
| |Wyandotte County|   107| 646.803|  6.908| 5,405| 32672.627| 422.279| 165,429|
| |Sedgwick County|    47| 91.078|  0.830| 5,429| 10520.462| 133.987| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,788| 10108.834| 161.535| 176,875|
| |Lyon County|    14| 421.750|  0.000|   762| 22955.264| 223.786|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,820| 49908.136| 129.275|  36,467|
| |Ford County|    10| 297.451|  0.000| 2,180| 64844.284| 390.935|  33,619|
| |Leavenworth County|     9| 110.081|  0.000| 1,548| 18933.927| 113.576|  81,758|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982|  0.000|   5,234|
| |Coffey County|     8| 978.115|  0.000|    71|  8680.768| 69.865|   8,179|
| |Saline County|     7| 129.094|  5.269|   416|  7671.880| 84.306|  54,224|
| |Riley County|     5| 67.356|  0.000|   512|  6897.295| 55.810|  74,232|
| |Montgomery County|     5| 157.089|  0.000|   193|  6063.653| 103.230|  31,829|
| |Douglas County|     5| 40.897|  0.000|   839|  6862.480| 111.006| 122,259|
| |Seward County|     4| 186.672|  0.000| 1,306| 60948.292| 573.349|  21,428|
| |Barton County|     3| 116.374|  0.000|   186|  7215.175| 260.456|  25,779|
| |Sumner County|     3| 131.372|  0.000|   107|  4685.584| 37.535|  22,836|
| |Cowley County|     2| 57.293|  0.000|   198|  5672.052| 102.310|  34,908|
| |Bourbon County|     2| 137.608|  0.000|    82|  5641.943| 29.488|  14,534|
| |Morton County|     2| 773.096|  0.000|    10|  3865.481| 55.221|   2,587|
| |Butler County|     2| 29.890|  2.135|   330|  4931.924| 111.022|  66,911|
| |Clay County|     2| 249.938|  0.000|    21|  2624.344| 17.853|   8,002|
| |Harvey County|     2| 58.091|  4.149|   246|  7145.139| 174.272|  34,429|
| |Grant County|     2| 279.720|  0.000|   130| 18181.818| 319.680|   7,150|
| |Franklin County|     2| 78.296|  5.593|   237|  9278.108| 329.963|  25,544|
| |Geary County|     2| 63.151|  0.000|   174|  5494.159| 117.281|  31,670|
| |Dickinson County|     1| 54.154|  0.000|    53|  2870.140| 38.681|  18,466|
| |Crawford County|     1| 25.761|  0.000|   400| 10304.498| 55.203|  38,818|
| |Clark County|     1| 501.505|  0.000|    45| 22567.703| 71.644|   1,994|
| |Ellis County|     1| 35.023|  0.000|   161|  5638.637| 80.052|  28,553|
| |Reno County|     1| 16.130|  0.000|   491|  7919.610| 476.974|  61,998|
| |Jackson County|     1| 75.924|  0.000|   166| 12603.447| 195.234|  13,171|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090|  0.000|   2,006|
| |Jewell County|     1| 347.343|  0.000|    14|  4862.800| 99.241|   2,879|
| |Trego County|     1| 356.761|  0.000|     7|  2497.324| 50.966|   2,803|
| |Kearny County|     1| 260.552|  0.000|    67| 17457.009| 148.887|   3,838|
| |Stafford County|     1| 240.616|  0.000|    12|  2887.392| 240.616|   4,156|
| |Labette County|     1| 50.974|  0.000|   159|  8104.802| 152.921|  19,618|
| |McPherson County|     1| 35.036|  0.000|   169|  5921.099| 105.108|  28,542|
| |Marion County|     1| 84.147|  0.000|    59|  4964.658| 132.231|  11,884|
| |Nemaha County|     1| 97.742|  0.000|    50|  4887.108| 13.963|  10,231|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509|  0.000|   5,485|
| |Rice County|     0|  0.000|  0.000|    41|  4299.046| 29.959|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293|  0.000|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   119|  4880.449| 64.448|  24,383|
| |Pawnee County|     0|  0.000|  0.000|    65| 10134.082| 1269.544|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    39|  6837.307| 100.180|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Osage County|     0|  0.000|  0.000|    50|  3134.993| 80.614|  15,949|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Thomas County|     0|  0.000|  0.000|    51|  6557.799| 220.430|   7,777|
| |Wabaunsee County|     0|  0.000|  0.000|    45|  6492.570| 41.223|   6,931|
| |Rooks County|     0|  0.000|  0.000|    19|  3861.789| 29.036|   4,920|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Russell County|     0|  0.000|  0.000|    17|  2479.580| 20.837|   6,856|
| |Scott County|     0|  0.000|  0.000|    79| 16379.847| 799.739|   4,823|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    17|  2873.078| 24.144|   5,917|
| |Sheridan County|     0|  0.000|  0.000|     9|  3570.012| 113.334|   2,521|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Kingman County|     0|  0.000|  0.000|    27|  3775.168| 119.847|   7,152|
| |Graham County|     0|  0.000|  0.000|    23|  9266.720| 345.344|   2,482|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323|  0.000|   2,475|
| |Miami County|     0|  0.000|  0.000|   150|  4381.225| 66.762|  34,237|
| |Meade County|     0|  0.000|  0.000|    52| 12893.628| 247.954|   4,033|
| |Marshall County|     0|  0.000|  0.000|    15|  1545.277| 73.585|   9,707|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Linn County|     0|  0.000|  0.000|    50|  5153.045| 147.230|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     6|  3908.795| 93.067|   1,535|
| |Gray County|     0|  0.000|  0.000|    90| 15030.060| 310.144|   5,988|
| |Jefferson County|     0|  0.000|  0.000|    95|  4988.710| 142.535|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Harper County|     0|  0.000|  0.000|    24|  4415.011| 315.358|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    42| 16541.946| 225.060|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868|  0.000|   5,982|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753|  0.000|   1,232|
| |Ellsworth County|     0|  0.000|  0.000|    22|  3605.375| 23.412|   6,102|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946|  0.000|  12,369|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024|  0.000|   7,858|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092|  0.000|   3,138|
| |Wilson County|     0|  0.000|  0.000|    16|  1876.833| 83.787|   8,525|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Washington County|     0|  0.000|  0.000|     2|   369.959| 26.426|   5,406|
| |Ness County|     0|  0.000|  0.000|     8|  2909.091| 103.896|   2,750|
| |Neosho County|     0|  0.000|  0.000|    66|  4123.196|  8.925|  16,007|
| |Morris County|     0|  0.000|  0.000|    12|  2135.231|  0.000|   5,620|
| |Cherokee County|     0|  0.000|  0.000|   168|  8425.698| 279.424|  19,939|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Edwards County|     0|  0.000|  0.000|    12|  4288.778| 102.114|   2,798|
| |Doniphan County|     0|  0.000|  0.000|    50|  6578.947| 37.594|   7,600|
| |Decatur County|     0|  0.000|  0.000|     6|  2122.391| 50.533|   2,827|
| |Comanche County|     0|  0.000|  0.000|     9|  5294.118| 252.101|   1,700|
| |Cloud County|     0|  0.000|  0.000|    42|  4780.332| 81.298|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     5|  1881.822| 107.533|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154|  0.000|   3,250|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Chase County|     0|  0.000|  0.000|    58| 21903.323| 539.491|   2,648|
| |Brown County|     0|  0.000|  0.000|    53|  5541.614| 194.181|   9,564|
| |Barber County|     0|  0.000|  0.000|     6|  1355.320| 64.539|   4,427|
| |Atchison County|     0|  0.000|  0.000|    99|  6159.398| 311.081|  16,073|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   388| 91.992| N/A|23,451|  5560.091| N/A|4,217,737|
| |Multnomah County|   102| 125.484|  1.054| 5,387|  6627.258| 75.044| 812,855|
| |Marion County|    73| 209.880|  1.232| 3,234|  9297.966| 121.574| 347,818|
| |Clackamas County|    50| 119.564|  3.416| 1,699|  4062.776| 51.242| 418,187|
| |Umatilla County|    32| 410.520|  7.331| 2,456| 31507.377| 282.232|  77,950|
| |Washington County|    27| 44.881|  0.475| 3,358|  5581.856| 56.754| 601,592|
| |Malheur County|    15| 490.661|  4.673|   916| 29963.037| 523.372|  30,571|
| |Yamhill County|    13| 121.382|  0.000|   523|  4883.287| 74.697| 107,100|
| |Polk County|    12| 139.397|  0.000|   367|  4263.228| 79.655|  86,085|
| |Linn County|    11| 84.779|  1.101|   338|  2605.030| 59.455| 129,749|
| |Deschutes County|    11| 55.642|  0.723|   645|  3262.651| 24.569| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   440|  8806.693| 62.905|  49,962|
| |Benton County|     6| 64.479|  0.000|   186|  1998.861| 26.099|  93,053|
| |Jefferson County|     5| 202.774|  5.794|   413| 16749.128| 243.329|  24,658|
| |Lane County|     4| 10.469|  0.374|   629|  1646.308| 14.582| 382,067|
| |Morrow County|     3| 258.554|  0.000|   407| 35077.135| 430.923|  11,603|
| |Wasco County|     3| 112.435|  0.000|   203|  7608.125| 58.895|  26,682|
| |Klamath County|     2| 29.309|  0.000|   210|  3077.464| 18.842|  68,238|
| |Union County|     2| 74.530|  0.000|   398| 14831.377| 21.294|  26,835|
| |Jackson County|     2|  9.052|  0.000|   576|  2606.995| 66.597| 220,944|
| |Josephine County|     2| 22.861|  0.000|   140|  1600.238| 40.822|  87,487|
| |Columbia County|     1| 19.101|  2.729|   113|  2158.383| 43.659|  52,354|
| |Wallowa County|     1| 138.735|  0.000|    21|  2913.430| 39.638|   7,208|
| |Crook County|     1| 40.977|  0.000|    53|  2171.775| 23.415|  24,404|
| |Douglas County|     1|  9.011|  0.000|   162|  1459.722| 14.160| 110,980|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|
| |Baker County|     0|  0.000|  0.000|    53|  3287.026| 115.179|  16,124|
| |Hood River County|     0|  0.000|  0.000|   218|  9323.411| 152.743|  23,382|
| |Harney County|     0|  0.000|  0.000|    11|  1487.894| 19.323|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633|  0.000|   7,199|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Curry County|     0|  0.000|  0.000|    19|   828.790| 24.926|  22,925|
| |Coos County|     0|  0.000|  0.000|    93|  1442.151|  4.431|  64,487|
| |Clatsop County|     0|  0.000|  0.000|    92|  2287.192| 24.861|  40,224|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764|  0.000|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Tillamook County|     0|  0.000|  0.000|    35|  1294.570|  5.284|  27,036|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   361| 186.620| N/A|30,404| 15717.470| N/A|1,934,408|
| |Douglas County|   143| 250.294|  2.500|12,137| 21243.526| 195.785| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,773| 28898.342| 62.868|  61,353|
| |Dakota County|    42| 2097.274|  0.000| 1,944| 97073.804| 114.137|  20,026|
| |Lancaster County|    19| 59.544|  0.895| 3,451| 10815.131| 62.231| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   104| 11154.011| 61.286|   9,324|
| |Sarpy County|    11| 58.762|  0.000| 2,506| 13387.038| 164.839| 187,196|
| |Adams County|    11| 350.732|  0.000|   370| 11797.341| 54.659|  31,363|
| |Dodge County|    10| 273.486|  0.000|   849| 23218.925| 125.022|  36,565|
| |Dawson County|     9| 381.437|  0.000|   980| 41534.223| 115.036|  23,595|
| |Perkins County|     7| 2421.308|  0.000|    24|  8301.626| 296.487|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   315|  8843.843| 56.151|  35,618|
| |Madison County|     5| 142.454|  0.000|   492| 14017.493| 126.174|  35,099|
| |Howard County|     5| 775.795| 22.166|    57|  8844.065| 44.331|   6,445|
| |Colfax County|     4| 373.518|  0.000|   709| 66205.995| 80.039|  10,709|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 118.652|   7,224|
| |Custer County|     4| 371.161|  0.000|    59|  5474.622| 145.813|  10,777|
| |Gage County|     4| 185.934|  0.000|   100|  4648.352| 66.405|  21,513|
| |Platte County|     3| 89.633|  0.000|   821| 24529.429| 102.437|  33,470|
| |Cass County|     2| 76.196|  0.000|   215|  8191.100| 190.491|  26,248|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Saunders County|     2| 92.687|  0.000|   181|  8388.173| 132.410|  21,578|
| |Saline County|     2| 140.607|  0.000|   604| 42463.442| 70.304|  14,224|
| |Lincoln County|     2| 57.284|  0.000|   200|  5728.361| 306.876|  34,914|
| |Richardson County|     1| 127.146|  0.000|    28|  3560.076| 90.818|   7,865|
| |Seward County|     1| 57.857|  0.000|   134|  7752.835| 99.183|  17,284|
| |Washington County|     1| 48.242|  0.000|   148|  7139.756| 151.616|  20,729|
| |Buffalo County|     1| 20.137|  0.000|   512| 10310.316| 221.511|  49,659|
| |Furnas County|     1| 213.858|  0.000|    17|  3635.586| 61.102|   4,676|
| |Fillmore County|     1| 183.083|  0.000|    29|  5309.410| 130.774|   5,462|
| |Antelope County|     1| 158.781|  0.000|    21|  3334.392| 45.366|   6,298|
| |Kearney County|     0|  0.000|  0.000|    84| 12933.025| 681.843|   6,495|
| |Nance County|     0|  0.000|  0.000|    11|  3125.888| 121.788|   3,519|
| |Morrill County|     0|  0.000|  0.000|    63| 13571.736| 153.875|   4,642|
| |Merrick County|     0|  0.000|  0.000|    63|  8123.791| 18.421|   7,755|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Pierce County|     0|  0.000|  0.000|    48|  6715.165| 539.611|   7,148|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    43|  5160.826| 120.019|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    41|  5103.311| 320.068|   8,034|
| |Johnson County|     0|  0.000|  0.000|    19|  3746.796| 140.857|   5,071|
| |Valley County|     0|  0.000|  0.000|    13|  3126.503| 103.072|   4,158|
| |Phelps County|     0|  0.000|  0.000|    49|  5423.954| 142.319|   9,034|
| |Polk County|     0|  0.000|  0.000|    28|  5371.187| 27.404|   5,213|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Wayne County|     0|  0.000|  0.000|    39|  4155.567| 30.444|   9,385|
| |York County|     0|  0.000|  0.000|    93|  6798.743| 135.766|  13,679|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139|  0.000|     783|
| |Nemaha County|     0|  0.000|  0.000|    52|  7458.405| 389.312|   6,972|
| |Nuckolls County|     0|  0.000|  0.000|     6|  1446.480| 34.440|   4,148|
| |Otoe County|     0|  0.000|  0.000|    70|  4371.721| 151.672|  16,012|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |McPherson County|     0|  0.000|  0.000|     6| 12145.749| 289.184|     494|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795|  0.000|   3,487|
| |Red Willow County|     0|  0.000|  0.000|    18|  1678.478| 13.321|  10,724|
| |Garfield County|     0|  0.000|  0.000|     6|  3047.232| 145.106|   1,969|
| |Burt County|     0|  0.000|  0.000|    54|  8360.427| 309.645|   6,459|
| |Cedar County|     0|  0.000|  0.000|    29|  3451.559| 119.019|   8,402|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Frontier County|     0|  0.000|  0.000|     4|  1522.649| 54.380|   2,627|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Harlan County|     0|  0.000|  0.000|     2|   591.716| 42.265|   3,380|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482|  0.000|   2,356|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Gosper County|     0|  0.000|  0.000|    22| 11055.276| 215.363|   1,990|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Thomas County|     0|  0.000|  0.000|     2|  2770.083| 197.863|     722|
| |Franklin County|     0|  0.000|  0.000|    15|  5035.247| 143.864|   2,979|
| |Chase County|     0|  0.000|  0.000|     9|  2293.578| 72.812|   3,924|
| |Dundy County|     0|  0.000|  0.000|     3|  1772.002| 168.762|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827|  0.000|   1,794|
| |Dawes County|     0|  0.000|  0.000|    17|  1979.276| 116.428|   8,589|
| |Cuming County|     0|  0.000|  0.000|    73|  8252.317| 96.896|   8,846|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616|  0.000|   6,203|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762|  0.000|   5,003|
| |Stanton County|     0|  0.000|  0.000|    33|  5574.324| 24.131|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Sherman County|     0|  0.000|  0.000|    15|  4998.334| 190.413|   3,001|
| |Sheridan County|     0|  0.000|  0.000|    12|  2287.457| 27.232|   5,246|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759|  0.000|   1,357|
| |Jefferson County|     0|  0.000|  0.000|    19|  2696.565| 40.550|   7,046|
| |Holt County|     0|  0.000|  0.000|    14|  1390.682| 14.191|  10,067|
| |Brown County|     0|  0.000|  0.000|     2|   676.819| 96.688|   2,955|
| |Boyd County|     0|  0.000|  0.000|     8|  4168.838| 223.331|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    17|  1576.556| 66.242|  10,783|
| |Boone County|     0|  0.000|  0.000|    14|  2696.456| 165.089|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827|  0.000|     463|
| |Butler County|     0|  0.000|  0.000|    66|  8233.533| 106.929|   8,016|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   303| 94.512| N/A|37,388| 11662.037| N/A|3,205,958|
| |Salt Lake County|   212| 182.690|  1.970|21,870| 18846.348| 138.125|1,160,437|
| |Utah County|    39| 61.298|  0.449| 9,478| 14897.011| 153.582| 636,235|
| |San Juan County|    26| 1698.458|  9.332|   653| 42657.434| 27.997|  15,308|
| |Davis County|    21| 59.075|  0.000| 3,422|  9626.394| 76.355| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   600| 17599.953| 134.095|  34,091|
| |Summit County|     1| 23.728|  0.000|   746| 17700.795| 111.859|  42,145|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Tooele County|     0|  0.000|  0.000|   619|  8566.407| 71.173|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   273| 152.764| N/A|27,934| 15631.217| N/A|1,787,065|
| |Ada County|    95| 197.264|  3.560|10,030| 20826.974| 262.822| 481,587|
| |Canyon County|    58| 252.340|  6.215| 6,422| 27940.082| 343.704| 229,849|
| |Twin Falls County|    33| 379.843|  1.644| 1,533| 17645.434| 169.367|  86,878|
| |Kootenai County|    21| 126.737|  4.311| 1,994| 12034.014| 174.156| 165,697|
| |Nez Perce County|    19| 470.204|  0.000|   188|  4652.544| 95.455|  40,408|
| |Blaine County|     6| 260.632|  0.000|   586| 25455.019| 55.850|  23,021|
| |Bonneville County|     6| 50.394|  2.400| 1,338| 11237.842| 315.562| 119,062|
| |Jerome County|     6| 245.781|  0.000|   528| 21628.707| 263.337|  24,412|
| |Owyhee County|     4| 338.324| 12.083|   281| 23767.233| 193.328|  11,823|
| |Elmore County|     3| 109.047|  0.000|   234|  8505.689| 109.047|  27,511|
| |Washington County|     3| 294.291|  0.000|   241| 23641.358| 448.443|  10,194|
| |Shoshone County|     3| 232.883| 11.090|   168| 13041.453| 754.098|  12,882|
| |Payette County|     3| 125.256|  5.965|   451| 18830.111| 339.980|  23,951|
| |Minidoka County|     2| 95.062|  0.000|   507| 24098.104| 183.333|  21,039|
| |Bingham County|     2| 42.725|  0.000|   351|  7498.238| 296.023|  46,811|
| |Bannock County|     2| 22.777|  0.000|   507|  5773.961| 174.081|  87,808|
| |Valley County|     1| 87.781|  0.000|    76|  6671.348| 188.102|  11,392|
| |Jefferson County|     1| 33.477|  0.000|   260|  8704.094| 282.166|  29,871|
| |Boise County|     1| 127.698|  0.000|    54|  6895.671| 72.970|   7,831|
| |Benewah County|     1| 107.550| 15.364|    80|  8604.001| 245.829|   9,298|
| |Cassia County|     1| 41.615|  0.000|   553| 23012.901| 166.459|  24,030|
| |Gem County|     1| 55.212|  0.000|   195| 10766.343| 118.311|  18,112|
| |Gooding County|     1| 65.880|  0.000|   183| 12056.130| 131.761|  15,179|
| |Latah County|     0|  0.000|  0.000|   146|  3640.172| 156.720|  40,108|
| |Adams County|     0|  0.000|  0.000|    22|  5123.428| 99.807|   4,294|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 33.107|   4,315|
| |Lincoln County|     0|  0.000|  0.000|    62| 11554.230| 79.868|   5,366|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Lemhi County|     0|  0.000|  0.000|    51|  6353.557| 462.724|   8,027|
| |Idaho County|     0|  0.000|  0.000|    36|  2159.957| 34.285|  16,667|
| |Fremont County|     0|  0.000|  0.000|    94|  7176.120| 98.154|  13,099|
| |Teton County|     0|  0.000|  0.000|   101|  8318.234| 211.780|  12,142|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478|  0.000|  13,876|
| |Clearwater County|     0|  0.000|  0.000|    18|  2055.733| 16.315|   8,756|
| |Oneida County|     0|  0.000|  0.000|    16|  3531.229| 63.058|   4,531|
| |Clark County|     0|  0.000|  0.000|    14| 16568.047| 1014.370|     845|
| |Caribou County|     0|  0.000|  0.000|    34|  4751.922| 39.932|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     1|   385.060| 55.009|   2,597|
| |Boundary County|     0|  0.000|  0.000|    40|  3266.639| 46.666|  12,245|
| |Bonner County|     0|  0.000|  0.000|   192|  4197.731| 28.110|  45,739|
| |Bear Lake County|     0|  0.000|  0.000|    21|  3428.571| 93.294|   6,125|
| |Madison County|     0|  0.000|  0.000|   195|  4886.361| 89.494|  39,907|
| |Power County|     0|  0.000|  0.000|    67|  8722.823| 185.988|   7,681|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   160| 89.278| N/A| 8,641|  4821.591| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  0.000| 1,095|  6147.403| 125.915| 178,124|
| |Jackson County|    19| 664.894|  0.000|   168|  5879.059| 14.998|  28,576|
| |Mercer County|    18| 306.341| 17.019|   243|  4135.607| 104.545|  58,758|
| |Logan County|    11| 343.546| 31.231|   362| 11305.787| 571.089|  32,019|
| |Berkeley County|    11| 92.304|  0.000|   738|  6192.782| 47.950| 119,171|
| |Wayne County|     9| 228.415|  0.000|   221|  5608.852| 39.882|  39,402|
| |Fayette County|     7| 165.071|  0.000|   170|  4008.867| 64.007|  42,406|
| |Wood County|     5| 59.867|  0.000|   283|  3388.491| 56.446|  83,518|
| |Monongalia County|     5| 47.343|  0.000|   992|  9392.872| 63.575| 105,612|
| |Mingo County|     5| 213.456|  0.000|   202|  8623.634| 176.864|  23,424|
| |Ohio County|     4| 96.593|  0.000|   283|  6833.933| 48.296|  41,411|
| |Preston County|     4| 119.646|  0.000|   130|  3888.490| 21.365|  33,432|
| |Mineral County|     4| 148.876|  0.000|   127|  4726.813| 21.268|  26,868|
| |Grant County|     4| 345.781| 37.048|   131| 11324.343| 123.493|  11,568|
| |Jefferson County|     4| 69.996|  0.000|   305|  5337.206| 22.499|  57,146|
| |Greenbrier County|     3| 86.550|  0.000|    96|  2769.604| 12.364|  34,662|
| |Cabell County|     3| 32.628|  0.000|   459|  4992.115| 85.455|  91,945|
| |Pleasants County|     2| 268.097| 19.150|    14|  1876.676| 19.150|   7,460|
| |Wyoming County|     2| 98.068|  7.005|    48|  2353.633| 98.068|  20,394|
| |Marion County|     2| 35.668|  0.000|   199|  3549.008| 20.382|  56,072|
| |Lewis County|     2| 125.731|  0.000|    28|  1760.231|  0.000|  15,907|
| |Nicholas County|     1| 40.823|  0.000|    40|  1632.920| 17.496|  24,496|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Roane County|     1| 73.057|  0.000|    20|  1461.134| 52.183|  13,688|
| |Taylor County|     1| 59.898|  0.000|    81|  4851.752| 213.922|  16,695|
| |Raleigh County|     1| 13.631|  0.000|   304|  4143.891| 95.419|  73,361|
| |Hampshire County|     1| 43.150|  0.000|    89|  3840.345| 80.136|  23,175|
| |Pendleton County|     1| 143.493|  0.000|    43|  6170.182| 40.998|   6,969|
| |Barbour County|     1| 60.824|  0.000|    33|  2007.177| 34.756|  16,441|
| |Brooke County|     1| 45.581|  0.000|    77|  3509.732| 84.650|  21,939|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  0.000|  30,531|
| |Harrison County|     1| 14.869|  0.000|   248|  3687.403| 46.730|  67,256|
| |Mason County|     1| 37.713|  0.000|    74|  2790.768| 96.976|  26,516|
| |Hancock County|     0|  0.000|  0.000|   114|  3956.959|  9.917|  28,810|
| |Calhoun County|     0|  0.000|  0.000|     7|   984.667| 20.095|   7,109|
| |Boone County|     0|  0.000|  0.000|   120|  5592.581| 126.499|  21,457|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227|  0.000|   8,448|
| |Gilmer County|     0|  0.000|  0.000|    18|  2300.908| 18.261|   7,823|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  0.000|  24,176|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921|  0.000|  13,275|
| |Morgan County|     0|  0.000|  0.000|    33|  1845.225| 31.952|  17,884|
| |McDowell County|     0|  0.000|  0.000|    67|  3801.634| 24.317|  17,624|
| |Putnam County|     0|  0.000|  0.000|   225|  3985.828| 75.921|  56,450|
| |Webster County|     0|  0.000|  0.000|     4|   492.975|  0.000|   8,114|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 33.257|   8,591|
| |Tucker County|     0|  0.000|  0.000|    11|  1608.422| 20.889|   6,839|
| |Wetzel County|     0|  0.000|  0.000|    45|  2987.056| 18.965|  15,065|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543|  0.000|   5,821|
| |Randolph County|     0|  0.000|  0.000|   214|  7457.745| 19.914|  28,695|
| |Lincoln County|     0|  0.000|  0.000|   108|  5291.783| 139.994|  20,409|
| |Summers County|     0|  0.000|  0.000|    19|  1511.175| 79.536|  12,573|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Hardy County|     0|  0.000|  0.000|    63|  4573.171| 20.740|  13,776|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   153| 172.948| N/A|10,360| 11710.727| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  0.000| 4,655| 24102.437| 161.250| 193,134|
| |Pennington County|    33| 290.046|  1.256|   951|  8358.603| 69.059| 113,775|
| |Beadle County|     9| 487.726|  0.000|   598| 32406.655| 30.967|  18,453|
| |Todd County|     5| 491.304|  0.000|    75|  7369.559| 84.224|  10,177|
| |Union County|     4| 251.067|  0.000|   223| 13996.987| 62.767|  15,932|
| |Lake County|     4| 312.573| 22.327|   103|  8048.761| 100.470|  12,797|
| |Lyman County|     3| 793.441| 37.783|    91| 24067.707| 37.783|   3,781|
| |Yankton County|     3| 131.498|  6.262|   157|  6881.739| 250.473|  22,814|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556|  0.000|   1,962|
| |Brown County|     3| 77.242|  0.000|   485| 12487.448| 143.449|  38,839|
| |Hughes County|     3| 171.174|  8.151|   100|  5705.809| 57.058|  17,526|
| |Oglala Lakota County|     2| 141.074|  0.000|   158| 11144.812| 20.153|  14,177|
| |Lincoln County|     2| 32.718|  0.000|   711| 11631.331| 161.254|  61,128|
| |Butte County|     1| 95.886|  0.000|    20|  1917.729| 27.396|  10,429|
| |Brookings County|     1| 28.509|  0.000|   156|  4447.359| 69.235|  35,077|
| |Roberts County|     1| 96.209|  0.000|    87|  8370.214| 96.209|  10,394|
| |Davison County|     1| 50.569|  0.000|   101|  5107.459| 28.897|  19,775|
| |Faulk County|     1| 434.972|  0.000|    29| 12614.180| 124.278|   2,299|
| |Jackson County|     1| 299.043|  0.000|    12|  3588.517| 42.720|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |Lawrence County|     1| 38.694|  5.528|    74|  2863.334| 77.387|  25,844|
| |McCook County|     1| 179.019|  0.000|    36|  6444.683| 179.019|   5,586|
| |Meade County|     1| 35.296|  0.000|   106|  3741.353| 60.507|  28,332|
| |Codington County|     1| 35.703|  0.000|   169|  6033.775| 163.213|  28,009|
| |Edmunds County|     0|  0.000|  0.000|    19|  4962.131| 111.928|   3,829|
| |Douglas County|     0|  0.000|  0.000|    20|  6846.970| 146.721|   2,921|
| |Dewey County|     0|  0.000|  0.000|    59| 10013.578| 266.705|   5,892|
| |Deuel County|     0|  0.000|  0.000|    24|  5515.973| 426.831|   4,351|
| |Day County|     0|  0.000|  0.000|    28|  5162.242| 131.690|   5,424|
| |Kingsbury County|     0|  0.000|  0.000|    15|  3037.052| 28.924|   4,939|
| |Marshall County|     0|  0.000|  0.000|    12|  2431.611| 86.843|   4,935|
| |Corson County|     0|  0.000|  0.000|    47| 11502.692| 454.514|   4,086|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565|  0.000|   2,756|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Turner County|     0|  0.000|  0.000|    60|  7156.489| 136.314|   8,384|
| |Sully County|     0|  0.000|  0.000|     4|  2875.629| 102.701|   1,391|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Stanley County|     0|  0.000|  0.000|    16|  5164.622| 92.225|   3,098|
| |Spink County|     0|  0.000|  0.000|    27|  4234.630| 22.405|   6,376|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Potter County|     0|  0.000|  0.000|     2|   928.936| 66.353|   2,153|
| |Fall River County|     0|  0.000|  0.000|    23|  3426.188| 21.281|   6,713|
| |Grant County|     0|  0.000|  0.000|    33|  4679.524| 121.546|   7,052|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757|  0.000|   2,379|
| |Gregory County|     0|  0.000|  0.000|     8|  1911.589| 34.136|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     4|  3074.558| 109.806|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    31|  4251.817| 39.187|   7,291|
| |Harding County|     0|  0.000|  0.000|     2|  1540.832| 220.119|   1,298|
| |Hanson County|     0|  0.000|  0.000|    22|  6371.271| 41.372|   3,453|
| |Hand County|     0|  0.000|  0.000|    12|  3760.577| 179.075|   3,191|
| |Hamlin County|     0|  0.000|  0.000|    31|  5029.202| 208.584|   6,164|
| |Moody County|     0|  0.000|  0.000|    33|  5018.248| 21.724|   6,576|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Custer County|     0|  0.000|  0.000|    47|  5238.520| 175.148|   8,972|
| |Brule County|     0|  0.000|  0.000|    47|  8872.947| 53.939|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    26|  3767.570| 269.112|   6,901|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Aurora County|     0|  0.000|  0.000|    40| 14540.167| 103.858|   2,751|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233|  0.000|   1,376|
| |Charles Mix County|     0|  0.000|  0.000|   113| 12160.999| 138.368|   9,292|
| |Clark County|     0|  0.000|  0.000|    17|  4550.321| 38.238|   3,736|
| |Clay County|     0|  0.000|  0.000|   141| 10021.322| 111.686|  14,070|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   127| 94.479| N/A| 4,196|  3121.531| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,130|  7220.266| 19.855| 295,003|
| |Waldo County|    14| 352.512|  0.000|    63|  1586.302|  3.597|  39,715|
| |York County|    13| 62.608|  0.688|   693|  3337.491| 12.384| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   172|  1406.355|  0.000| 122,302|
| |Androscoggin County|     9| 83.120|  1.319|   580|  5356.632| 19.791| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   191|  1255.357| 38.496| 152,148|
| |Knox County|     1| 25.143|  0.000|    28|   704.013|  3.592|  39,772|
| |Franklin County|     1| 33.114|  0.000|    47|  1556.343|  9.461|  30,199|
| |Hancock County|     1| 18.186|  0.000|    40|   727.445| 10.392|  54,987|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  0.000|  34,634|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  0.000|  67,055|
| |Somerset County|     1| 19.808|  0.000|    40|   792.330| 19.808|  50,484|
| |Washington County|     0|  0.000|  0.000|    15|   478.027|  9.105|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    58|  1617.581|  7.968|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|    12|   714.924| 68.088|  16,785|
| |Oxford County|     0|  0.000|  0.000|    59|  1017.680| 12.321|  57,975|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   126| 165.341| N/A| 8,625| 11317.977| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,135| 17232.565| 69.888| 181,923|
| |Burleigh County|    11| 115.031|  7.470| 1,409| 14734.486| 310.734|  95,626|
| |Grand Forks County|     8| 115.189|  4.114|   799| 11504.514| 238.606|  69,451|
| |Stark County|     6| 190.543| 13.610|   395| 12544.063| 594.312|  31,489|
| |Morton County|     4| 127.535|  4.555|   455| 14507.078| 327.947|  31,364|
| |Stutsman County|     3| 144.900|  0.000|   130|  6278.980| 20.700|  20,704|
| |Benson County|     2| 292.740|  0.000|   173| 25322.014| 752.760|   6,832|
| |Williams County|     2| 53.207|  0.000|   303|  8060.869| 117.816|  37,589|
| |Sioux County|     2| 472.813| 33.772|    97| 22931.442| 472.813|   4,230|
| |Ramsey County|     2| 173.626|  0.000|    89|  7726.365| 235.636|  11,519|
| |McIntosh County|     2| 800.961|  0.000|    41| 16419.704| 228.846|   2,497|
| |McKenzie County|     2| 133.120|  9.509|    94|  6256.656| 38.034|  15,024|
| |Griggs County|     1| 448.229|  0.000|    37| 16584.491| 192.098|   2,231|
| |Ward County|     1| 14.784|  0.000|   277|  4095.149| 90.816|  67,641|
| |Richland County|     1| 61.816|  0.000|   117|  7232.491| 70.647|  16,177|
| |Mountrail County|     1| 94.832|  0.000|   155| 14698.909| 270.948|  10,545|
| |McHenry County|     1| 174.064|  0.000|    24|  4177.546| 174.064|   5,745|
| |Emmons County|     1| 308.547|  0.000|    23|  7096.575| 264.469|   3,241|
| |Dickey County|     0|  0.000|  0.000|    14|  2873.563| 29.322|   4,872|
| |Dunn County|     0|  0.000|  0.000|    32|  7233.273| 64.583|   4,424|
| |Barnes County|     0|  0.000|  0.000|    46|  4416.707| 96.015|  10,415|
| |Divide County|     0|  0.000|  0.000|     4|  1766.784| 126.199|   2,264|
| |Eddy County|     0|  0.000|  0.000|    20|  8745.081| 124.930|   2,287|
| |Foster County|     0|  0.000|  0.000|    27|  8411.215| 44.504|   3,210|
| |Towner County|     0|  0.000|  0.000|     6|  2740.978| 65.261|   2,189|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Traill County|     0|  0.000|  0.000|    64|  7964.161| 159.994|   8,036|
| |Steele County|     0|  0.000|  0.000|    16|  8465.608| 151.172|   1,890|
| |Walsh County|     0|  0.000|  0.000|   116| 10901.231| 161.102|  10,641|
| |Wells County|     0|  0.000|  0.000|    24|  6259.781| 111.782|   3,834|
| |Golden Valley County|     0|  0.000|  0.000|    12|  6814.310| 567.859|   1,761|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Bowman County|     0|  0.000|  0.000|    11|  3637.566| 141.723|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Hettinger County|     0|  0.000|  0.000|     8|  3201.281| 114.331|   2,499|
| |Billings County|     0|  0.000|  0.000|     3|  3232.759| 153.941|     928|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791|  0.000|   2,216|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Kidder County|     0|  0.000|  0.000|    23|  9274.194| 288.018|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523|  0.000|   4,046|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106|  0.000|   1,315|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    88|  6207.675| 151.161|  14,176|
| |Renville County|     0|  0.000|  0.000|    10|  4297.379| 61.391|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041|  0.000|   5,218|
| |Pierce County|     0|  0.000|  0.000|    16|  4025.157| 143.756|   3,975|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Nelson County|     0|  0.000|  0.000|    27|  9378.256| 49.620|   2,879|
| |Mercer County|     0|  0.000|  0.000|    34|  4152.925| 87.246|   8,187|
| |McLean County|     0|  0.000|  0.000|   102| 10793.651| 453.515|   9,450|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784|  0.000|   1,850|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    82| 76.723| N/A| 5,792|  5419.273| N/A|1,068,778|
| |Yellowstone County|    32| 198.388|  1.771| 1,533|  9504.030| 210.787| 161,300|
| |Big Horn County|    14| 1051.130| 10.726|   529| 39717.697| 986.775|  13,319|
| |Toole County|     6| 1266.892|  0.000|    46|  9712.838| 30.164|   4,736|
| |Cascade County|     4| 49.161|  0.000|   183|  2249.097| 29.847|  81,366|
| |Flathead County|     3| 28.900|  1.376|   407|  3920.775| 82.572| 103,806|
| |Gallatin County|     3| 26.216|  0.000|   992|  8668.752| 56.177| 114,434|
| |Missoula County|     2| 16.722|  1.194|   385|  3219.064| 63.306| 119,600|
| |Ravalli County|     2| 45.656|  3.261|    85|  1940.373|  6.522|  43,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939|  0.000|  11,402|
| |Lincoln County|     2| 100.100|  0.000|    78|  3903.904|  7.150|  19,980|
| |Lewis and Clark County|     2| 28.805|  2.058|   178|  2563.659| 41.150|  69,432|
| |Hill County|     2| 121.330|  0.000|    48|  2911.915| 51.998|  16,484|
| |Richland County|     2| 185.134|  0.000|    50|  4628.344| 39.672|  10,803|
| |Glacier County|     1| 72.711|  0.000|    88|  6398.604| 124.648|  13,753|
| |Lake County|     1| 32.832|  0.000|   187|  6139.602| 28.142|  30,458|
| |Madison County|     1| 116.279|  0.000|    86| 10000.000| 33.223|   8,600|
| |Rosebud County|     1| 111.894|  0.000|    78|  8727.761| 703.336|   8,937|
| |Sweet Grass County|     1| 267.594|  0.000|     6|  1605.566| 38.228|   3,737|
| |Stillwater County|     1| 103.713|  0.000|    31|  3215.101| 74.081|   9,642|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937|  0.000|   5,911|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Roosevelt County|     0|  0.000|  0.000|    35|  3180.662| 155.788|  11,004|
| |Sanders County|     0|  0.000|  0.000|    18|  1486.007| 106.143|  12,113|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031|  0.000|   3,309|
| |Silver Bow County|     0|  0.000|  0.000|   105|  3007.303| 40.916|  34,915|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Valley County|     0|  0.000|  0.000|    30|  4056.247| 212.470|   7,396|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Carbon County|     0|  0.000|  0.000|    77|  7179.487| 79.920|  10,725|
| |Broadwater County|     0|  0.000|  0.000|    14|  2244.669| 45.810|   6,237|
| |Blaine County|     0|  0.000|  0.000|    14|  2095.495| 85.530|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    68|  7193.484| 60.449|   9,453|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Fergus County|     0|  0.000|  0.000|    23|  2081.448| 116.354|  11,050|
| |Deer Lodge County|     0|  0.000|  0.000|    30|  3282.276| 78.149|   9,140|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Granite County|     0|  0.000|  0.000|    18|  5327.020| 84.556|   3,379|
| |Jefferson County|     0|  0.000|  0.000|    31|  2536.617| 23.379|  12,221|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623|  0.000|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Phillips County|     0|  0.000|  0.000|    93| 23520.486| 2348.436|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    63|  3793.809| 68.822|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     4|   863.371| 30.835|   4,633|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 171.703|   1,664|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Dawson County|     0|  0.000|  0.000|    30|  3483.107| 215.621|   8,613|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,519|  2434.338| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   763|  4658.859| 28.785| 163,774|
| |Franklin County|     7| 141.695|  0.000|   121|  2449.294|  8.675|  49,402|
| |Windham County|     3| 71.053|  0.000|   107|  2534.224| 16.917|  42,222|
| |Washington County|     2| 34.241|  0.000|    58|   992.998| 12.229|  58,409|
| |Windsor County|     2| 36.323|  0.000|    75|  1362.101|  7.783|  55,062|
| |Addison County|     2| 54.382|  0.000|    76|  2066.509| 11.653|  36,777|
| |Rutland County|     1| 17.185|  0.000|   101|  1735.664|  2.455|  58,191|
| |Bennington County|     1| 28.193|  0.000|    92|  2593.741| 16.110|  35,470|
| |Lamoille County|     1| 39.429|  0.000|    45|  1774.308| 11.265|  25,362|
| |Essex County|     0|  0.000|  0.000|     6|   973.552|  0.000|   6,163|
| |Caledonia County|     0|  0.000|  0.000|    29|   966.892|  4.763|  29,993|
| |Orleans County|     0|  0.000|  0.000|    15|   554.795|  5.284|  27,037|
| |Orange County|     0|  0.000|  0.000|    18|   623.010| 19.778|  28,892|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    39| 27.545| N/A| 5,192|  3666.998| N/A|1,415,872|
| |Honolulu County|    33| 33.861| N/A| 4,754|  4878.084| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   235|  1403.681| 41.812| 167,417|
| |Hawaii County|     0|  0.000|  0.000|   149|   739.406| 12.761| 201,513|
| |Kauai County|     0|  0.000|  0.000|    54|   746.960|  9.880|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,331|  5755.418| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    25|  2960.332| 33.832|   8,445|
| |Lincoln County|     0|  0.000|  0.000|   104|  5244.579|  7.204|  19,830|
| |Laramie County|     0|  0.000|  0.000|   523|  5256.281| 40.201|  99,500|
| |Uinta County|     0|  0.000|  0.000|   277| 13695.244|  0.000|  20,226|
| |Natrona County|     0|  0.000|  0.000|   248|  3105.512| 23.256|  79,858|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Park County|     0|  0.000|  0.000|   146|  5001.028| 53.827|  29,194|
| |Platte County|     0|  0.000|  0.000|     6|   714.881| 17.021|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    86|  2821.060| 60.920|  30,485|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762| 14.531|   9,831|
| |Sweetwater County|     0|  0.000|  0.000|   278|  6565.430| 60.729|  42,343|
| |Teton County|     0|  0.000|  0.000|   390| 16621.207| 121.767|  23,464|
| |Washakie County|     0|  0.000|  0.000|   100| 12812.300| 420.976|   7,805|
| |Converse County|     0|  0.000|  0.000|    33|  2387.498| 20.671|  13,822|
| |Albany County|     0|  0.000|  0.000|   103|  2649.177| 62.463|  38,880|
| |Big Horn County|     0|  0.000|  0.000|    39|  3307.888| 24.234|  11,790|
| |Campbell County|     0|  0.000|  0.000|   148|  3193.716| 73.986|  46,341|
| |Carbon County|     0|  0.000|  0.000|   169| 11418.919| 666.023|  14,800|
| |Crook County|     0|  0.000|  0.000|    11|  1450.422| 18.837|   7,584|
| |Fremont County|     0|  0.000|  0.000|   533| 13575.813| 130.991|  39,261|
| |Goshen County|     0|  0.000|  0.000|    39|  2952.085| 54.067|  13,211|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874|  0.000|   4,413|
| |Weston County|     0|  0.000|  0.000|     8|  1154.901| 41.246|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
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
| |Washington County|     0|  0.000|  0.000|   621|  4945.173| 15.926| 125,577|
| |Newport County|     0|  0.000|  0.000|   405|  4934.090| 15.664|  82,082|
| |Kent County|     0|  0.000|  0.000| 1,544|  9397.901| 43.477| 164,292|
| |Bristol County|     0|  0.000|  0.000|   322|  6642.051| 17.681|  48,479|
| |Providence County|     0|  0.000|  0.000|15,644| 24484.647| 133.482| 638,931|


