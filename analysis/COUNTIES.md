# Analysis of US By County #

Updated: at 2020-08-11

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 130,334 deaths (451.510 deaths/million) and 4,382,357 confirmed cases (15181.618 confirmed cases/million).  This group accounts for 81.02% of all US deaths and for 87.53% of all US cases.

24.64% of this group's deaths (19.96% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.04% of this group's deaths (20.29% of the total US deaths) occured in 33 counties in 14 states with a combined population of 41,047,233 (12.51% of the total US population):



The next 25.26% of this group's deaths (20.46% of the total US deaths) occured in 89 counties in 30 states with a combined population of 65,771,319 (20.04% of the total US population)

The remaining 25.06% of this group's deaths (20.31% of the total US deaths) occured in 855 counties in 50 states with a combined population of 144,556,289 (44.04% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,070 deaths (254.438 deaths/million) and 455,720 confirmed cases (11514.634 confirmed cases/million).  This group accounts for 6.26% of all US deaths and for 9.10% of all US cases.

24.77% of this group's deaths (1.55% of the total US deaths) occured in 58 counties in 16 states with a combined population of 1,934,772 (0.59% of the total US population):



The next 25.15% of this group's deaths (1.57% of the total US deaths) occured in 113 counties in 27 states with a combined population of 3,349,504 (1.02% of the total US population):



The next 25.06% of this group's deaths (1.57% of the total US deaths) occured in 233 counties in 32 states with a combined population of 5,680,817 (1.73% of the total US population)

The remaining 25.01% of this group's deaths (1.57% of the total US deaths) occured in 1,748 counties in 47 states with a combined population of 28,612,371 (8.72% of the total US population) 

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
|NJ|21 counties|15,878| 1787.622| N/A|184,386| 20759.070| N/A|8,882,190|
| |Essex County| 2,111| 2642.135|  1.252|19,747| 24715.417| 33.793| 798,975|
| |Bergen County| 2,038| 2186.221|  0.000|20,825| 22339.579| 41.836| 932,202|
| |Hudson County| 1,505| 2238.281|  0.425|19,683| 29273.146| 32.932| 672,391|
| |Middlesex County| 1,403| 1700.478|  0.000|17,932| 21734.124| 34.110| 825,062|
| |Union County| 1,350| 2426.569|  0.514|16,725| 30062.498| 34.665| 556,341|
| |Passaic County| 1,242| 2474.961|  0.000|17,665| 35201.444| 44.979| 501,826|
| |Ocean County| 1,018| 1676.587|  0.471|10,603| 17462.524| 31.527| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,326| 16687.271| 43.633| 618,795|
| |Morris County|   829| 1685.490|  0.000| 7,261| 14762.781| 27.302| 491,845|
| |Mercer County|   620| 1687.396|  0.389| 8,127| 22118.499| 29.549| 367,430|
| |Camden County|   580| 1145.179|  1.410| 8,580| 16940.753| 57.823| 506,471|
| |Somerset County|   561| 1705.509|  2.606| 5,253| 15969.769| 25.190| 328,934|
| |Burlington County|   473| 1062.088|  0.962| 6,025| 13528.716| 57.419| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,469| 13156.597| 33.050| 263,670|
| |Gloucester County|   212| 726.934|  1.470| 3,258| 11171.460| 74.457| 291,636|
| |Sussex County|   198| 1409.373|  3.051| 1,333|  9488.355| 26.438| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,345| 12777.034| 20.356| 105,267|
| |Cumberland County|   158| 1056.665|  0.955| 3,348| 22390.605| 90.762| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,149|  9238.488| 12.635| 124,371|
| |Salem County|    87| 1394.566|  4.580|   898| 14394.486| 48.088|  62,385|
| |Cape May County|    87| 945.251|  0.000|   834|  9061.376| 32.595|  92,039|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,321| 633.350| N/A|252,667| 12988.216| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,690| 32197.824| 32.637|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.097|43,844| 29692.517| 43.440|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.148|36,233| 37449.897| 32.336| 967,506|
| |Queens County|   984| 436.746|  0.719| 7,877|  3494.759| 17.692|2,253,858|
| |Kings County|   930| 363.405|  0.598| 1,352|   528.073|  2.673|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,949| 42816.056| 28.064| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,918|  9707.174| 45.406| 918,702|
| |Bronx County|   649| 457.596|  0.753|26,824| 18914.195| 95.754|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,168| 29012.314| 26.720| 384,940|
| |New York County|   414| 254.365|  0.418|15,471|  9498.710| 48.087|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 4,976|  6708.279| 35.822| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,585|  7784.543| 29.469| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,613| 15678.850| 33.988| 294,218|
| |Richmond County|   148| 310.869|  0.511| 7,877| 16542.700| 83.748| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,600|  8510.471| 32.265| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,150|  9402.154| 37.484| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,500|  7167.397| 34.813| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,072| 11668.441| 32.984| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,131|  5937.382| 50.247| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,449| 14737.592| 23.248|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   298|  7385.012| 10.621|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,489| 19739.633| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   298|  3124.377|  8.987|  95,379|
| |Schenectady County|    37| 238.250|  0.000| 1,060|  6825.543| 21.157| 155,299|
| |Columbia County|    37| 622.257|  0.000|   541|  9098.401| 43.246|  59,461|
| |Ontario County|    34| 309.719|  0.000|   361|  3288.485| 13.013| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269| 26.809|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   766|  4826.291| 23.402| 158,714|
| |Tioga County|    25| 518.640|  0.000|   193|  4003.900|  8.891|  48,203|
| |Fulton County|    24| 449.581|  0.000|   297|  5563.569| 32.113|  53,383|
| |Greene County|    18| 381.453|  0.000|   293|  6209.206| 12.110|  47,188|
| |Madison County|    17| 239.636|  0.000|   412|  5807.643| 22.151|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   760|  3306.317| 16.780| 229,863|
| |Washington County|    14| 228.743|  0.000|   260|  4248.088| 11.671|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   257|  2025.169| 25.892| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470| 20.436|  62,914|
| |Yates County|     7| 280.978|  0.000|    57|  2287.962| 11.468|  24,913|
| |Chenango County|     6| 127.100|  0.000|   216|  4575.593| 15.131|  47,207|
| |Cattaraugus County|     6| 78.826|  0.000|   166|  2180.853|  7.507|  76,117|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436| 17.920|  39,859|
| |Genesee County|     5| 87.291|  0.000|   277|  4835.894|  9.976|  57,280|
| |Otsego County|     5| 84.044|  0.000|   116|  1949.809|  4.802|  59,493|
| |Montgomery County|     4| 81.266|  0.000|   177|  3596.026| 49.340|  49,221|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  1.326| 107,740|
| |Herkimer County|     4| 65.233|  0.000|   274|  4468.436| 65.233|  61,319|
| |Clinton County|     4| 49.699|  0.000|   128|  1590.358|  1.775|  80,485|
| |Delaware County|     4| 90.631|  0.000|   105|  2379.064|  3.237|  44,135|
| |Chemung County|     3| 35.947|  0.000|   172|  2060.966| 15.406|  83,456|
| |Oswego County|     3| 25.614|  0.000|   253|  2160.104|  6.099| 117,124|
| |Seneca County|     3| 88.194|  0.000|    90|  2645.814| 16.799|  34,016|
| |Wayne County|     3| 33.364|  0.000|   252|  2802.553|  7.944|  89,918|
| |Cayuga County|     2| 26.118|  0.000|   152|  1984.956|  7.462|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697| 15.497|  46,091|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  5.592| 102,180|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525| 11.424|  50,022|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Essex County|     0|  0.000|  0.000|    55|  1491.121|  0.000|  36,885|
| |Lewis County|     0|  0.000|  0.000|    41|  1559.172| 32.596|  26,296|
| |Jefferson County|     0|  0.000|  0.000|   142|  1292.860| 10.405| 109,834|
| |Cortland County|     0|  0.000|  0.000|    95|  1996.595|  9.007|  47,581|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,476| 265.133| N/A|574,231| 14532.997| N/A|39,512,223|
| |Los Angeles County| 4,998| 497.853|  4.212|210,543| 20972.284| 237.158|10,039,107|
| |Riverside County|   820| 331.910|  7.228|41,983| 16993.410| 287.502|2,470,546|
| |Orange County|   726| 228.612|  3.374|40,527| 12761.628| 122.088|3,175,692|
| |San Diego County|   594| 177.933|  1.241|32,975|  9877.693| 132.316|3,338,330|
| |San Bernardino County|   546| 250.449|  8.388|36,072| 16546.144| 172.995|2,180,085|
| |Imperial County|   244| 1346.467| 17.343| 9,693| 53488.950| 193.141| 181,215|
| |San Joaquin County|   223| 292.594|  8.060|12,864| 16878.612| 183.504| 762,148|
| |Alameda County|   209| 125.050|  1.710|13,631|  8155.785| 180.096|1,671,329|
| |Santa Clara County|   205| 106.336|  1.037|12,694|  6584.530| 140.793|1,927,852|
| |Tulare County|   196| 420.425|  2.145|10,862| 23299.263| 342.285| 466,195|
| |Sacramento County|   177| 114.042|  2.945|12,040|  7757.442| 176.540|1,552,058|
| |Kern County|   171| 189.957|  4.285|24,440| 27149.462| 601.294| 900,202|
| |Fresno County|   171| 171.154|  4.719|17,846| 17862.058| 395.069| 999,101|
| |Stanislaus County|   169| 306.904| 14.787|10,264| 18639.451| 270.584| 550,660|
| |Contra Costa County|   139| 120.500|  1.486| 9,404|  8152.395| 169.790|1,153,526|
| |San Mateo County|   120| 156.541|  0.186| 6,318|  8241.877| 118.337| 766,573|
| |Ventura County|    92| 108.746|  2.702| 8,634| 10205.601| 217.830| 846,006|
| |Marin County|    81| 312.952|  6.071| 5,404| 20878.892| 172.206| 258,826|
| |Merced County|    70| 252.089| 10.289| 5,736| 20656.871| 746.491| 277,680|
| |Santa Barbara County|    69| 154.536|  2.880| 6,704| 15014.591| 171.813| 446,499|
| |San Francisco County|    67| 76.003| N/A| 7,623|  8647.279| N/A| 881,549|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993|  0.000| 152,940|
| |Sonoma County|    47| 95.077|  2.312| 3,670|  7424.100| 160.966| 494,336|
| |Yolo County|    44| 199.546|  1.296| 1,834|  8317.460| 169.744| 220,500|
| |Solano County|    41| 91.591|  1.277| 4,274|  9547.787| 211.584| 447,643|
| |Madera County|    39| 247.891|  8.172| 2,463| 15655.291| 472.174| 157,327|
| |Monterey County|    35| 80.634|  1.646| 5,446| 12546.624| 171.799| 434,061|
| |Placer County|    22| 55.231|  2.152| 2,319|  5821.821| 141.305| 398,329|
| |San Luis Obispo County|    16| 56.515|  0.000| 2,254|  7961.542| 177.618| 283,111|
| |Napa County|    11| 79.858|  3.111| 1,074|  7797.073| 192.904| 137,744|
| |Mendocino County|    10| 115.275|  1.647|   472|  5440.985| 247.018|  86,749|
| |Shasta County|    10| 55.531|  0.793|   459|  2548.867| 54.738| 180,080|
| |Butte County|     8| 36.499|  0.652| 1,238|  5648.171| 193.573| 219,186|
| |Sutter County|     7| 72.187|  1.473|   952|  9817.368| 228.345|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,243|  4549.564| 47.582| 273,213|
| |Yuba County|     4| 50.847|  0.000|   646|  8211.725| 261.497|  78,668|
| |San Benito County|     4| 63.686|  0.000|   765| 12179.977| 268.392|  62,808|
| |Humboldt County|     4| 29.508|  0.000|   286|  2109.798| 55.854| 135,558|
| |Colusa County|     4| 185.641|  0.000|   391| 18146.378| 397.801|  21,547|
| |Inyo County|     3| 166.306| 15.839|   106|  5876.157| 356.371|  18,039|
| |Glenn County|     3| 105.660| 10.063|   360| 12679.181| 140.880|  28,393|
| |Tuolumne County|     3| 55.068|  2.622|   155|  2845.185| 36.712|  54,478|
| |Amador County|     2| 50.312|  7.187|   182|  4578.386| 201.248|  39,752|
| |El Dorado County|     2| 10.371|  0.741|   755|  3915.102| 87.414| 192,843|
| |Lake County|     2| 31.063|  2.219|   240|  3727.518| 71.000|  64,386|
| |Mariposa County|     2| 116.259|  0.000|    62|  3604.023| 41.521|  17,203|
| |Calaveras County|     1| 21.784|  0.000|   147|  3202.266| 68.464|  45,905|
| |Tehama County|     1| 15.365|  0.000|   276|  4240.674| 92.189|  65,084|
| |Nevada County|     1| 10.025|  0.000|   357|  3578.768| 83.061|  99,755|
| |Mono County|     1| 69.233|  0.000|   158| 10938.798| 128.575|  14,444|
| |Del Norte County|     0|  0.000|  0.000|   100|  3595.570| 61.638|  27,812|
| |Lassen County|     0|  0.000|  0.000|   683| 22339.973| 266.341|  30,573|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|
| |Siskiyou County|     0|  0.000|  0.000|   102|  2342.727| 95.153|  43,539|
| |Sierra County|     0|  0.000|  0.000|     4|  1331.115| 95.080|   3,005|
| |Plumas County|     0|  0.000|  0.000|    36|  1914.181| 22.788|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 48.475|   8,841|
| |Trinity County|     0|  0.000|  0.000|     5|   407.000|  0.000|  12,285|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 8,991| 310.079| N/A|509,581| 17574.255| N/A|28,995,881|
| |Harris County| 1,583| 335.856| 24.732|86,563| 18365.591| 256.507|4,713,325|
| |Hidalgo County|   829| 954.292| 28.450|20,148| 23193.090| 459.632| 868,707|
| |Bexar County|   784| 391.305| 11.551|42,959| 21441.399| 129.841|2,003,554|
| |Dallas County|   756| 286.851|  3.523|55,255| 20965.534| 204.080|2,635,516|
| |Tarrant County|   449| 213.554|  3.941|32,177| 15304.053| 212.195|2,102,515|
| |Cameron County|   430| 1016.157| 20.931|16,590| 39204.751| 1037.763| 423,163|
| |Travis County|   303| 237.842|  7.513|22,953| 18017.134| 195.006|1,273,954|
| |El Paso County|   300| 357.467|  8.341|16,396| 19536.770| 252.270| 839,238|
| |Nueces County|   243| 670.726| 18.927|15,423| 42570.399| 1123.003| 362,294|
| |Webb County|   174| 628.949| 50.089| 8,262| 29864.234| 955.817| 276,652|
| |Fort Bend County|   162| 199.584|  2.816|10,021| 12345.877| 498.080| 811,688|
| |Galveston County|   113| 330.275|  4.175| 9,514| 27807.412| 287.686| 342,139|
| |Brazoria County|    93| 248.488|  7.634| 7,481| 19988.564| 285.894| 374,264|
| |Williamson County|    93| 157.480|  3.145| 6,893| 11672.150| 256.661| 590,551|
| |Collin County|    90| 86.979|  2.485| 7,833|  7570.091| 197.429|1,034,730|
| |Montgomery County|    90| 148.175|  3.998| 6,654| 10955.052| 85.377| 607,391|
| |Denton County|    88| 99.188|  2.093| 7,745|  8729.643| 129.942| 887,207|
| |Jefferson County|    84| 333.910|  6.247| 5,880| 23373.681| 212.385| 251,565|
| |Lubbock County|    73| 235.052|  3.680| 6,059| 19509.352| 214.353| 310,569|
| |Comal County|    70| 448.118|  6.402| 1,839| 11772.689| 146.324| 156,209|
| |Starr County|    68| 1052.094| 37.575| 2,213| 34239.475| 705.080|  64,633|
| |Guadalupe County|    55| 329.643|  9.418| 1,679| 10063.112| 70.210| 166,847|
| |McLennan County|    55| 214.322|  8.907| 4,970| 19366.931| 297.268| 256,623|
| |Ector County|    55| 330.881|  5.157| 3,587| 21579.444| 257.829| 166,223|
| |Midland County|    49| 277.099|  5.655| 2,676| 15133.008| 401.511| 176,832|
| |Brazos County|    49| 213.777|  4.363| 4,069| 17752.202| 91.619| 229,211|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 541.998|  49,025|
| |Potter County|    45| 383.256|  7.300| 3,689| 31418.473| 223.870| 117,415|
| |Angelina County|    45| 518.941| 14.827| 1,796| 20711.526| 245.468|  86,715|
| |Maverick County|    43| 732.264|  9.731| 2,321| 39525.221| 807.680|  58,722|
| |Nacogdoches County|    42| 644.132| 13.146| 1,148| 17606.282| 247.575|  65,204|
| |Victoria County|    42| 456.105| 20.168| 3,448| 37444.073| 380.088|  92,084|
| |Ellis County|    42| 227.241|  6.183| 2,855| 15446.961| 296.031| 184,826|
| |Walker County|    41| 561.867|  5.873| 3,051| 41811.130| 413.080|  72,971|
| |Hays County|    39| 169.425|  3.724| 5,050| 21938.303| 97.435| 230,191|
| |Washington County|    39| 1086.896|  3.981|   515| 14352.600| 71.663|  35,882|
| |Bell County|    38| 104.705|  2.362| 3,831| 10555.929| 131.865| 362,924|
| |Liberty County|    34| 385.405| 14.574|   987| 11188.066| 220.231|  88,219|
| |Bowie County|    32| 343.182|  1.532|   764|  8193.469| 85.795|  93,245|
| |Johnson County|    30| 170.632|  4.063| 1,861| 10584.869| 260.011| 175,817|
| |Willacy County|    30| 1404.626| 66.887|   699| 32727.784| 702.313|  21,358|
| |Matagorda County|    27| 736.839| 15.594|   752| 20522.337| 276.802|  36,643|
| |Gregg County|    27| 217.839|  6.916| 1,416| 11424.422| 118.716| 123,945|
| |Hale County|    26| 778.303| 17.106| 1,285| 38466.144| 427.639|  33,406|
| |Caldwell County|    26| 595.456|  9.815| 1,149| 26314.584| 255.196|  43,664|
| |San Patricio County|    26| 389.630| 21.408|   935| 14011.689| 295.434|  66,730|
| |Tom Green County|    26| 218.121|  2.397| 2,671| 22407.718| 299.616| 119,200|
| |Medina County|    26| 504.032|  5.539|   878| 17020.782| 783.742|  51,584|
| |Wharton County|    25| 601.598| 13.751|   761| 18312.638| 433.150|  41,556|
| |Kaufman County|    25| 183.616|  3.148| 2,158| 15849.700| 358.837| 136,154|
| |Taylor County|    23| 166.626|  4.140| 1,130|  8186.389| 39.328| 138,034|
| |Grimes County|    23| 796.399| 14.840|   880| 30470.914| 153.344|  28,880|
| |Harrison County|    23| 345.589|  2.147|   693| 10412.754| 148.110|  66,553|
| |Smith County|    23| 98.818|  3.683| 2,524| 10844.207| 131.962| 232,751|
| |Hunt County|    21| 212.995|  1.449| 1,182| 11988.559| 178.220|  98,594|
| |Bastrop County|    21| 236.692|  4.830| 1,365| 15384.962| 111.100|  88,723|
| |Randall County|    21| 152.491|  4.149| 1,725| 12526.051| 144.192| 137,713|
| |Orange County|    20| 239.820|  5.139| 1,477| 17710.682| 781.127|  83,396|
| |Parker County|    19| 132.981|  6.999| 1,225|  8573.748| 154.977| 142,878|
| |Wilson County|    19| 372.038|  8.392|   439|  8596.045| 69.932|  51,070|
| |DeWitt County|    19| 942.460| 28.345|   693| 34375.000| 1147.959|  20,160|
| |Panola County|    18| 776.063|  6.159|   292| 12589.463| 135.503|  23,194|
| |Shelby County|    18| 712.194| 11.305|   401| 15866.107| 113.047|  25,274|
| |Atascosa County|    18| 351.886|  8.378|   437|  8542.998| 89.368|  51,153|
| |Lamar County|    18| 361.018|  5.730|   647| 12976.594| 63.035|  49,859|
| |Lavaca County|    17| 843.505| 21.265|   627| 31110.450| 241.001|  20,154|
| |Deaf Smith County|    17| 916.640|  0.000|   667| 35964.628| 539.200|  18,546|
| |Brown County|    16| 422.565|  7.546|   391| 10326.431| 150.916|  37,864|
| |Jim Wells County|    15| 370.535| 24.702|   724| 17884.492| 331.717|  40,482|
| |Aransas County|    15| 638.026| 18.229|   177|  7528.711| 115.452|  23,510|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Hardin County|    15| 260.408|  9.920|   973| 16891.775| 401.772|  57,602|
| |Fayette County|    14| 552.355|  5.636|   388| 15308.135| 118.362|  25,346|
| |Anderson County|    14| 242.487| 12.372| 2,403| 41621.200| 237.539|  57,735|
| |Grayson County|    13| 95.439|  2.098| 1,139|  8361.965| 119.562| 136,212|
| |Moore County|    13| 620.821|  6.822| 1,050| 50143.266| 252.422|  20,940|
| |Rockwall County|    13| 123.910|  0.000|   896|  8540.247| 239.650| 104,915|
| |Polk County|    12| 233.677|  8.346|   748| 14565.848| 247.586|  51,353|
| |Henderson County|    12| 145.038|  5.180|   641|  7747.441| 110.505|  82,737|
| |Bee County|    11| 337.786|  8.774| 1,207| 37064.333| 2548.749|  32,565|
| |Lamb County|    11| 853.176| 44.321|   226| 17528.892| 254.845|  12,893|
| |Red River County|    11| 914.913|  0.000|   136| 11311.653| 23.764|  12,023|
| |Jasper County|    11| 309.606| 24.125|   304|  8556.391| 52.271|  35,529|
| |San Augustine County|    11| 1335.438|  0.000|   162| 19667.355| 121.403|   8,237|
| |Wichita County|    11| 83.188|  1.080| 1,001|  7570.143| 106.956| 132,230|
| |Uvalde County|    10| 373.958| 16.027|   551| 20605.063| 293.824|  26,741|
| |Hood County|    10| 162.224|  2.317|   528|  8565.449| 210.892|  61,643|
| |Lee County|    10| 580.080| 16.574|   173| 10035.385| 165.737|  17,239|
| |Burnet County|     9| 186.896|  5.933|   563| 11691.413| 62.299|  48,155|
| |Gonzales County|     9| 431.924| 13.712|   683| 32778.231| 452.492|  20,837|
| |Navarro County|     8| 159.639|  0.000|   856| 17081.396| 253.712|  50,113|
| |San Jacinto County|     8| 277.210|  0.000|   177|  6133.269| 143.555|  28,859|
| |Kleberg County|     8| 260.756| 13.969|   442| 14406.780| 377.165|  30,680|
| |Fannin County|     8| 225.263|  0.000|   246|  6926.846| 128.722|  35,514|
| |Marion County|     8| 811.853| 14.497|   133| 13497.057| 86.984|   9,854|
| |Cass County|     8| 266.436|  4.758|   176|  5861.587| 109.429|  30,026|
| |Wood County|     7| 153.714|  6.274|   316|  6939.107| 78.426|  45,539|
| |Palo Pinto County|     7| 239.816|  4.894|   265|  9078.763| 347.489|  29,189|
| |Wise County|     7| 100.023|  4.083|   409|  5844.193| 200.046|  69,984|
| |Cherokee County|     7| 132.964|  8.141| 1,119| 21255.176| 911.750|  52,646|
| |Andrews County|     7| 374.231|  7.637|   304| 16252.339| 282.583|  18,705|
| |Hill County|     7| 191.001| 15.592|   328|  8949.767| 77.960|  36,649|
| |Jackson County|     7| 474.255| 19.357|   406| 27506.775| 832.365|  14,760|
| |Houston County|     7| 304.772|  6.220|   314| 13671.195| 404.289|  22,968|
| |Parmer County|     7| 728.787|  0.000|   340| 35398.230| 431.323|   9,605|
| |Sabine County|     6| 569.152|  0.000|    51|  4837.792| 94.859|  10,542|
| |Burleson County|     6| 325.327|  7.746|   242| 13121.510| 85.205|  18,443|
| |Duval County|     6| 537.779| 38.413|   177| 15864.480| 320.107|  11,157|
| |Camp County|     6| 458.225| 21.820|   233| 17794.410| 163.652|  13,094|
| |Howard County|     6| 163.648| 11.689|   173|  4718.525| 62.342|  36,664|
| |Karnes County|     6| 384.591| 18.314|   639| 40958.913| 3104.197|  15,601|
| |Kerr County|     6| 114.068|  0.000|   398|  7566.540| 135.796|  52,600|
| |Floyd County|     6| 1050.420| 25.010|    89| 15581.232| 150.060|   5,712|
| |Gillespie County|     6| 222.321| 10.587|   175|  6484.363| 21.173|  26,988|
| |Dallam County|     5| 686.153|  0.000|   190| 26073.830| 215.648|   7,287|
| |Blanco County|     5| 419.076| 11.974|    98|  8213.897|  0.000|  11,931|
| |Waller County|     5| 90.504|  5.172|   454|  8217.790| 118.948|  55,246|
| |Coryell County|     5| 65.832|  0.000|   669|  8808.311| 103.450|  75,951|
| |Calhoun County|     5| 234.852| 13.420|   544| 25551.902| 610.615|  21,290|
| |Reeves County|     5| 312.969| 17.884|   146|  9138.708| 89.420|  15,976|
| |Martin County|     5| 866.401| 49.509|    55|  9530.411| 247.543|   5,771|
| |Young County|     5| 277.624|  7.932|   169|  9383.676| 237.963|  18,010|
| |Erath County|     5| 117.102|  0.000|   527| 12342.498| 217.474|  42,698|
| |Zavala County|     5| 422.297|  0.000|   210| 17736.486| 422.297|  11,840|
| |Frio County|     5| 246.233|  0.000|   512| 25214.222| 260.303|  20,306|
| |Newton County|     4| 294.226|  0.000|    93|  6840.750| 73.556|  13,595|
| |Refugio County|     4| 575.705| 82.244|   226| 32527.346| 349.535|   6,948|
| |Trinity County|     4| 273.019| 19.501|   156| 10647.737| 126.759|  14,651|
| |Goliad County|     4| 522.330| 18.655|    89| 11621.833| 223.856|   7,658|
| |Castro County|     4| 531.208| 18.972|   200| 26560.425| 569.152|   7,530|
| |Austin County|     4| 133.191|  4.757|   249|  8291.156| 171.246|  30,032|
| |Lynn County|     4| 672.156|  0.000|    67| 11258.612| 48.011|   5,951|
| |Bailey County|     4| 571.429|  0.000|   171| 24428.571| 265.306|   7,000|
| |Hockley County|     4| 173.754|  0.000|   206|  8948.352| 155.138|  23,021|
| |Kendall County|     4| 84.333|  6.024|   158|  3331.155| 39.155|  47,431|
| |Dawson County|     4| 314.268|  0.000|   145| 11392.206| 89.791|  12,728|
| |Bandera County|     3| 129.803|  0.000|    91|  3937.349| 49.449|  23,112|
| |Chambers County|     3| 68.435|  3.259|   951| 21694.003| 185.753|  43,837|
| |Callahan County|     3| 215.162|  0.000|    46|  3299.147| 51.229|  13,943|
| |Comanche County|     3| 220.022|  0.000|   142| 10414.375|  0.000|  13,635|
| |Cooke County|     3| 72.715|  0.000|   223|  5405.143| 79.640|  41,257|
| |Crockett County|     3| 866.051|  0.000|   155| 44745.958| 41.241|   3,464|
| |Dimmit County|     3| 296.326| 28.221|   150| 14816.278| 366.879|  10,124|
| |Falls County|     3| 173.440|  8.259|   128|  7400.127| 148.663|  17,297|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402| 45.868|   6,229|
| |Hamilton County|     3| 354.568| 16.884|    83|  9809.715| 472.757|   8,461|
| |Lampasas County|     3| 140.004| 13.334|   104|  4853.463| 133.337|  21,428|
| |Hutchinson County|     3| 143.280|  6.823|   126|  6017.767| 81.874|  20,938|
| |Brooks County|     3| 422.952| 40.281|   113| 15931.200| 523.655|   7,093|
| |Milam County|     3| 120.856|  0.000|   346| 13938.686| 230.201|  24,823|
| |Nolan County|     3| 203.887|  0.000|   134|  9106.973| 29.127|  14,714|
| |Morris County|     3| 242.170| 23.064|   117|  9444.624| 230.638|  12,388|
| |Stephens County|     3| 320.307| 15.253|    42|  4484.305| 198.286|   9,366|
| |Yoakum County|     3| 344.313| 32.792|   102| 11706.645| 278.730|   8,713|
| |Reagan County|     3| 779.423|  0.000|    63| 16367.888| 185.577|   3,849|
| |Van Zandt County|     3| 53.013|  0.000|   375|  6626.612| 108.550|  56,590|
| |Gaines County|     3| 139.587| 19.941|   161|  7491.160| 192.763|  21,492|
| |Limestone County|     3| 128.003|  0.000|   241| 10282.886| 256.005|  23,437|
| |Gray County|     2| 91.383|  0.000|   215|  9823.632| 208.875|  21,886|
| |Bosque County|     2| 107.038|  0.000|   162|  8670.056| 259.949|  18,685|
| |Brewster County|     2| 217.320|  0.000|   188| 20428.121| 62.092|   9,203|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 126.534|   3,387|
| |Colorado County|     2| 93.054|  0.000|   296| 13771.926| 332.334|  21,493|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Culberson County|     2| 921.234|  0.000|    17|  7830.493| 131.605|   2,171|
| |Hopkins County|     2| 53.932|  3.852|   201|  5420.127| 123.272|  37,084|
| |Hudspeth County|     2| 409.333|  0.000|    24|  4911.993| 58.476|   4,886|
| |La Salle County|     2| 265.957| 18.997|   361| 48005.319| 75.988|   7,520|
| |Leon County|     2| 114.916|  8.208|   144|  8273.960| 49.250|  17,404|
| |Live Oak County|     2| 163.840| 11.703|   230| 18841.648| 269.166|  12,207|
| |Ochiltree County|     2| 203.335|  0.000|    95|  9658.398| 159.763|   9,836|
| |Presidio County|     2| 298.329| 42.618|    46|  6861.575| 42.618|   6,704|
| |Robertson County|     2| 117.137|  8.367|   234| 13705.049| 150.605|  17,074|
| |Madison County|     2| 140.017|  0.000|   668| 46765.612| 230.028|  14,284|
| |Rusk County|     2| 36.761|  0.000|   370|  6800.721| 94.527|  54,406|
| |Swisher County|     2| 270.380|  0.000|    80| 10815.195| 96.564|   7,397|
| |Terry County|     2| 162.114|  0.000|   143| 11591.149| 312.648|  12,337|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 106.560|  10,725|
| |Tyler County|     2| 92.285|  0.000|   116|  5352.529|  6.592|  21,672|
| |Zapata County|     2| 141.054|  0.000|   174| 12271.669| 171.279|  14,179|
| |Upshur County|     2| 47.901|  0.000|   226|  5412.785| 112.909|  41,753|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890|  0.000|   1,501|
| |Hansford County|     2| 370.439|  0.000|    73| 13521.022| 370.439|   5,399|
| |Real County|     1| 289.687| 41.384|    87| 25202.781| 455.223|   3,452|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 68.495|  12,514|
| |Pecos County|     1| 63.199|  0.000|   244| 15420.590| 315.996|  15,823|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788| 67.641|   2,112|
| |Runnels County|     1| 97.428|  0.000|   124| 12081.060| 236.611|  10,264|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 51.148|   2,793|
| |Scurry County|     1| 59.869|  0.000|   481| 28797.222| 410.534|  16,703|
| |Kimble County|     1| 230.574| 32.939|    14|  3228.038| 32.939|   4,337|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Jim Hogg County|     1| 192.308|  0.000|    62| 11923.077| 247.253|   5,200|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Ward County|     1| 83.347|  0.000|    89|  7417.903| 71.440|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Sutton County|     1| 264.831|  0.000|    62| 16419.492| 151.332|   3,776|
| |Mitchell County|     1| 117.028| 16.718|    61|  7138.678| 150.464|   8,545|
| |Wilbarger County|     1| 78.315|  0.000|    69|  5403.712| 212.568|  12,769|
| |Winkler County|     1| 124.844|  0.000|    84| 10486.891| 285.358|   8,010|
| |Clay County|     1| 95.502|  0.000|    40|  3820.074| 81.859|  10,471|
| |McCulloch County|     1| 125.251|  0.000|    48|  6012.024| 125.251|   7,984|
| |Montague County|     1| 50.459|  0.000|    70|  3532.142| 93.710|  19,818|
| |Fisher County|     1| 261.097|  0.000|    28|  7310.705| 149.198|   3,830|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505| 19.664|  21,795|
| |Knox County|     1| 272.926| 38.989|    60| 16375.546| 545.852|   3,664|
| |Crosby County|     1| 174.307|  0.000|    63| 10981.349| 273.911|   5,737|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Eastland County|     1| 54.466|  0.000|    73|  3976.035| 171.180|  18,360|
| |Hall County|     1| 337.382|  0.000|    11|  3711.201| 144.592|   2,964|
| |Freestone County|     0|  0.000|  0.000|   157|  7962.672| 130.417|  19,717|
| |Delta County|     0|  0.000|  0.000|    16|  3001.313|  0.000|   5,331|
| |Donley County|     0|  0.000|  0.000|    48| 14643.075| 217.903|   3,278|
| |Edwards County|     0|  0.000|  0.000|    28| 14492.754| 295.770|   1,932|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Concho County|     0|  0.000|  0.000|    28| 10271.460| 104.811|   2,726|
| |Carson County|     0|  0.000|  0.000|    15|  2531.218| 48.214|   5,926|
| |Childress County|     0|  0.000|  0.000|    40|  5474.952| 117.320|   7,306|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 550.799|   2,853|
| |Coleman County|     0|  0.000|  0.000|    19|  2324.159| 139.799|   8,175|
| |Collingsworth County|     0|  0.000|  0.000|    11|  3767.123| 195.695|   2,920|
| |Archer County|     0|  0.000|  0.000|    21|  2455.279| 16.703|   8,553|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Baylor County|     0|  0.000|  0.000|    11|  3134.796| 162.847|   3,509|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Jones County|     0|  0.000|  0.000|   596| 29676.841|  0.000|  20,083|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008| 187.477|     762|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Kinney County|     0|  0.000|  0.000|    19|  5181.347| 77.915|   3,667|
| |Mason County|     0|  0.000|  0.000|    53| 12400.562| 434.521|   4,274|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |McMullen County|     0|  0.000|  0.000|     9| 12113.055| 192.271|     743|
| |Mills County|     0|  0.000|  0.000|    22|  4514.673| 205.212|   4,873|
| |Menard County|     0|  0.000|  0.000|    17|  7951.356| 66.818|   2,138|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Hardeman County|     0|  0.000|  0.000|    18|  4576.659| 108.968|   3,933|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    59|  6603.246| 303.781|   8,935|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Hartley County|     0|  0.000|  0.000|    85| 15243.902| 76.860|   5,576|
| |Haskell County|     0|  0.000|  0.000|    42|  7423.118| 176.741|   5,658|
| |Hemphill County|     0|  0.000|  0.000|    42| 10997.643| 37.407|   3,819|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Lipscomb County|     0|  0.000|  0.000|    18|  5567.584| 132.562|   3,233|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Somervell County|     0|  0.000|  0.000|    74|  8106.924| 250.407|   9,128|
| |Sherman County|     0|  0.000|  0.000|    40| 13236.267| 141.817|   3,022|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704| 105.820|   1,350|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 56.510|   5,056|
| |San Saba County|     0|  0.000|  0.000|    24|  3963.666| 47.187|   6,055|
| |Shackelford County|     0|  0.000|  0.000|    18|  5513.017| 43.754|   3,265|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,734| 1267.174| N/A|120,883| 17538.331| N/A|6,892,503|
| |Middlesex County| 2,005| 1244.029|  1.507|26,470| 16423.662| 47.687|1,611,699|
| |Essex County| 1,194| 1513.243|  1.629|17,883| 22664.423| 83.466| 789,034|
| |Suffolk County| 1,074| 1335.975|  2.666|21,929| 27278.031| 97.915| 803,907|
| |Worcester County| 1,006| 1211.141|  2.236|13,654| 16438.284| 36.461| 830,622|
| |Norfolk County|   997| 1410.633|  1.819|10,639| 15052.881| 56.191| 706,775|
| |Plymouth County|   722| 1385.259|  2.467| 9,258| 17762.787| 36.180| 521,202|
| |Hampden County|   707| 1515.957|  2.451| 7,619| 16336.744| 43.497| 466,372|
| |Bristol County|   635| 1123.462|  2.275| 9,371| 16579.473| 55.099| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,802|  8460.491| 25.487| 212,990|
| |Hampshire County|   129| 802.089|  1.776| 1,179|  7330.722| 35.530| 160,830|
| |Franklin County|    61| 869.194|  2.036|   411|  5856.369| 12.213|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   668|  5346.395| 12.577| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,277| 385.376| N/A|536,264| 24968.366| N/A|21,477,737|
| |Miami-Dade County| 1,874| 689.747|  9.464|133,623| 49181.432| 524.697|2,716,940|
| |Palm Beach County|   936| 625.347|  8.685|37,297| 24918.324| 262.184|1,496,770|
| |Broward County|   821| 420.427|  5.340|62,898| 32209.498| 319.472|1,952,778|
| |Pinellas County|   500| 512.823|  8.498|17,941| 18401.101| 154.579| 974,996|
| |Hillsborough County|   388| 263.593|  3.882|32,731| 22236.217| 221.375|1,471,968|
| |Lee County|   334| 433.441|  6.303|16,632| 21583.826| 154.430| 770,577|
| |Polk County|   314| 433.237|  8.476|14,475| 19971.660| 263.726| 724,777|
| |Orange County|   298| 213.857|  6.049|31,851| 22857.623| 197.249|1,393,452|
| |Manatee County|   227| 562.922| 14.170| 9,340| 23161.638| 182.445| 403,253|
| |Duval County|   189| 197.336|  4.326|23,530| 24567.870| 253.569| 957,755|
| |St. Lucie County|   166| 505.640| 17.841| 5,824| 17740.034| 247.163| 328,297|
| |Brevard County|   151| 250.855|  8.069| 6,099| 10132.205| 113.917| 601,942|
| |Sarasota County|   147| 338.911|  8.563| 6,256| 14423.321| 145.577| 433,742|
| |Collier County|   136| 353.337|  4.454|10,448| 27144.572| 236.424| 384,902|
| |Volusia County|   135| 243.998|  4.906| 7,960| 14386.825| 197.780| 553,284|
| |Pasco County|   129| 232.874|  7.737| 7,114| 12842.384| 145.965| 553,947|
| |Escambia County|   120| 376.984| 10.322| 9,632| 30259.239| 676.327| 318,316|
| |Seminole County|   119| 252.212|  9.386| 7,152| 15158.130| 140.790| 471,826|
| |Osceola County|   104| 276.779|  8.744| 9,769| 25998.600| 332.667| 375,751|
| |Martin County|    94| 583.851| 15.084| 3,838| 23838.509| 172.138| 161,000|
| |Charlotte County|    91| 481.711|  1.512| 2,257| 11947.488| 147.463| 188,910|
| |Marion County|    89| 243.449|  9.769| 6,573| 17979.698| 502.920| 365,579|
| |Lake County|    68| 185.227|  6.615| 5,177| 14101.733| 182.503| 367,118|
| |Indian River County|    56| 350.169|  7.146| 2,543| 15901.403| 181.337| 159,923|
| |Clay County|    51| 232.609|  1.955| 3,298| 15042.052| 236.518| 219,252|
| |Bay County|    51| 291.921| 23.713| 4,447| 25454.337| 610.008| 174,705|
| |Hernando County|    48| 247.525| 11.050| 2,028| 10457.921| 193.010| 193,920|
| |Suwannee County|    44| 990.612| 25.730| 1,471| 33117.950| 903.772|  44,417|
| |Sumter County|    41| 309.621|  6.473| 1,307|  9870.110| 178.005| 132,420|
| |Okaloosa County|    41| 194.554|  7.457| 3,541| 16802.855| 345.724| 210,738|
| |Hendry County|    38| 904.288|  3.400| 1,783| 42430.156| 394.351|  42,022|
| |Santa Rosa County|    38| 206.171| 10.851| 3,963| 21501.468| 371.263| 184,313|
| |Jackson County|    38| 818.718| 15.389| 1,897| 40871.289| 858.731|  46,414|
| |Highlands County|    37| 348.330| 10.759| 1,449| 13641.370| 231.324| 106,221|
| |St. Johns County|    36| 136.017|  3.778| 3,660| 13828.437| 160.846| 264,672|
| |Citrus County|    36| 240.550|  5.727| 1,548| 10343.652| 237.686| 149,657|
| |Putnam County|    27| 362.314| 15.336| 1,519| 20383.516| 268.381|  74,521|
| |Alachua County|    26| 96.639|  1.593| 4,171| 15503.098| 224.075| 269,043|
| |Leon County|    25| 85.155|  4.866| 5,006| 17051.454| 271.523| 293,582|
| |Gadsden County|    21| 459.921|  3.129| 1,903| 41677.617| 1023.090|  45,660|
| |DeSoto County|    16| 421.042|  3.759| 1,358| 35735.902| 229.317|  38,001|
| |Walton County|    15| 202.508|  3.857| 1,414| 19089.792| 304.727|  74,071|
| |Columbia County|    15| 209.246|  7.971| 2,893| 40356.555| 587.881|  71,686|
| |Washington County|    14| 549.602|  0.000|   872| 34232.324| 1542.249|  25,473|
| |Flagler County|    13| 112.964|  2.483| 1,078|  9367.315| 165.101| 115,081|
| |Monroe County|    13| 175.136|  3.849| 1,531| 20625.640| 292.535|  74,228|
| |Okeechobee County|    12| 284.576| 20.327| 1,055| 25018.972| 328.618|  42,168|
| |Nassau County|    11| 124.118|  0.000| 1,239| 13980.254| 190.208|  88,625|
| |Madison County|     8| 432.596|  0.000|   708| 38284.756| 409.421|  18,493|
| |Hardee County|     7| 259.866|  0.000|   976| 36232.691| 631.102|  26,937|
| |Calhoun County|     7| 496.278|  0.000|   475| 33676.001| 1488.834|  14,105|
| |Liberty County|     6| 718.219| 68.402|   400| 47881.254|  0.000|   8,354|
| |Union County|     5| 328.149|  9.376|   374| 24545.514| 1396.975|  15,237|
| |Gilchrist County|     5| 269.078| 15.376|   366| 19696.480| 269.078|  18,582|
| |Levy County|     5| 120.473|  6.884|   687| 16553.020| 237.504|  41,503|
| |Jefferson County|     5| 350.976|  0.000|   455| 31938.790| 922.565|  14,246|
| |Taylor County|     5| 231.814| 13.247|   965| 44740.136| 3768.636|  21,569|
| |Baker County|     4| 136.939|  0.000|   932| 31906.881| 2587.177|  29,210|
| |Wakulla County|     4| 118.557|  0.000|   707| 20954.978| 402.248|  33,739|
| |Hamilton County|     4| 277.239|  9.901|   618| 42833.380| 316.844|  14,428|
| |Dixie County|     4| 237.727|  0.000|   553| 32865.803| 2343.312|  16,826|
| |Bradford County|     4| 141.839|  0.000|   508| 18013.546| 851.034|  28,201|
| |Glades County|     3| 217.218|  0.000|   405| 29324.452| 134.468|  13,811|
| |Lafayette County|     2| 237.473| 16.962|   148| 17573.023| 593.683|   8,422|
| |Franklin County|     2| 164.948|  0.000|   430| 35463.918| 3204.713|  12,125|
| |Gulf County|     2| 146.638|  0.000|   659| 48317.325| 2817.551|  13,639|
| |Holmes County|     2| 101.952|  0.000|   507| 25844.930| 378.680|  19,617|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,637| 602.676| N/A|195,341| 15415.385| N/A|12,671,821|
| |Cook County| 4,928| 956.850|  0.860|111,948| 21736.492| 130.396|5,150,233|
| |DuPage County|   520| 563.429|  1.548|12,312| 13340.253| 116.710| 922,921|
| |Lake County|   446| 640.312|  1.231|12,741| 18291.974| 133.723| 696,535|
| |Will County|   344| 498.014|  1.034| 9,315| 13485.479| 137.533| 690,743|
| |Kane County|   305| 572.874|  1.878| 9,803| 18412.744| 151.335| 532,403|
| |St. Clair County|   161| 619.980|  2.751| 4,028| 15511.040| 205.193| 259,686|
| |Winnebago County|   131| 463.599|  3.033| 3,784| 13391.277| 48.534| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,218| 10455.724| 119.290| 307,774|
| |Madison County|    76| 289.011|  1.630| 2,634| 10016.504| 223.820| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,787| 16265.861| 131.334| 109,862|
| |Rock Island County|    36| 253.737|  5.034| 1,756| 12376.744| 152.041| 141,879|
| |Peoria County|    35| 195.335|  0.000| 1,630|  9097.048| 230.416| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,274|  6544.341| 173.919| 194,672|
| |DeKalb County|    30| 285.995|  1.362|   938|  8942.105| 119.845| 104,897|
| |LaSalle County|    24| 220.854|  5.258|   783|  7205.367| 293.158| 108,669|
| |Boone County|    23| 429.553|  0.000|   766| 14305.991| 82.709|  53,544|
| |Kendall County|    23| 178.308|  0.000| 1,379| 10690.751| 97.460| 128,990|
| |Union County|    23| 1381.133| 17.157|   324| 19455.954| 180.148|  16,653|
| |Macon County|    23| 221.135|  0.000|   641|  6162.928| 208.773| 104,009|
| |Coles County|    20| 395.093|  2.822|   487|  9620.513| 242.700|  50,621|
| |Jackson County|    19| 334.802|  0.000|   722| 12722.467| 181.246|  56,750|
| |Jefferson County|    19| 504.193|  7.582|   290|  7695.574| 371.510|  37,684|
| |Champaign County|    19| 90.610|  0.000| 1,686|  8040.479| 94.698| 209,689|
| |Whiteside County|    17| 308.111|  2.589|   359|  6506.570| 119.102|  55,175|
| |Clinton County|    17| 452.585|  0.000|   411| 10941.909| 235.801|  37,562|
| |McDonough County|    15| 505.357|  0.000|   146|  4918.806| 86.633|  29,682|
| |McLean County|    15| 87.455|  0.000|   655|  3818.863| 69.131| 171,517|
| |Monroe County|    13| 375.321|  0.000|   318|  9180.934| 164.976|  34,637|
| |Iroquois County|    11| 405.694| 21.075|   265|  9773.549| 84.300|  27,114|
| |Cass County|    11| 905.573|  0.000|   231| 19017.041| 341.060|  12,147|
| |Tazewell County|     8| 60.697|  0.000|   591|  4483.965| 220.025| 131,803|
| |Montgomery County|     7| 246.357|  0.000|   169|  5947.772| 110.609|  28,414|
| |Randolph County|     7| 220.250|  0.000|   470| 14788.245| 157.322|  31,782|
| |Jasper County|     7| 728.408|  0.000|    59|  6139.438| 89.193|   9,610|
| |Williamson County|     6| 90.094|  2.145|   409|  6141.418| 145.867|  66,597|
| |Stephenson County|     6| 134.838|  0.000|   330|  7416.064| 38.525|  44,498|
| |Morgan County|     6| 178.264|  4.244|   268|  7962.446| 275.884|  33,658|
| |Grundy County|     5| 97.936|  0.000|   326|  6385.396| 123.119|  51,054|
| |Adams County|     5| 76.412|  2.183|   542|  8283.029| 211.770|  65,435|
| |Ogle County|     5| 98.730|  0.000|   411|  8115.633| 95.909|  50,643|
| |Mercer County|     4| 259.118| 37.017|    76|  4923.236| 55.525|  15,437|
| |Carroll County|     4| 279.623|  9.987|    59|  4124.432| 129.825|  14,305|
| |Christian County|     4| 123.824|  0.000|   143|  4426.696| 123.824|  32,304|
| |Macoupin County|     3| 66.776|  0.000|   181|  4028.847| 139.913|  44,926|
| |Bond County|     3| 182.637|  8.697|    62|  3774.504| 43.485|  16,426|
| |Woodford County|     3| 78.005|  0.000|   152|  3952.261| 200.585|  38,459|
| |Fayette County|     3| 140.607|  0.000|    67|  3140.232| 60.260|  21,336|
| |Cumberland County|     3| 278.655| 13.269|    57|  5294.445| 132.693|  10,766|
| |Bureau County|     3| 91.946|  4.378|   215|  6589.432| 310.864|  32,628|
| |Douglas County|     2| 102.749|  0.000|   122|  6267.660| 146.784|  19,465|
| |Clark County|     2| 129.525| 18.504|    83|  5375.300| 138.777|  15,441|
| |Ford County|     2| 154.309| 11.022|    49|  3780.572| 88.177|  12,961|
| |Jersey County|     2| 91.857|  6.561|   115|  5281.771| 295.254|  21,773|
| |Gallatin County|     2| 414.250| 59.179|    51| 10563.380| 177.536|   4,828|
| |Vermilion County|     2| 26.400|  0.000|   236|  3115.183| 39.600|  75,758|
| |Saline County|     2| 85.139|  6.081|   132|  5619.173| 115.546|  23,491|
| |Livingston County|     2| 56.104|  0.000|   116|  3254.039| 96.179|  35,648|
| |Perry County|     1| 47.810|  0.000|   184|  8797.093| 396.142|  20,916|
| |Lee County|     1| 29.329|  0.000|   173|  5073.909| 104.746|  34,096|
| |Pulaski County|     1| 187.441| 26.777|    94| 17619.494| 80.332|   5,335|
| |Shelby County|     1| 46.224|  0.000|    80|  3697.883| 132.067|  21,634|
| |Knox County|     1| 20.121|  0.000|   303|  6096.702| 117.852|  49,699|
| |Wayne County|     1| 61.671|  0.000|    62|  3823.620| 105.722|  16,215|
| |Effingham County|     1| 29.405|  0.000|   162|  4763.585| 193.232|  34,008|
| |Hancock County|     1| 56.472|  0.000|    62|  3501.242| 225.887|  17,708|
| |Henry County|     1| 20.444|  0.000|   248|  5070.227| 119.746|  48,913|
| |Jo Daviess County|     1| 47.092|  0.000|   127|  5980.692| 94.184|  21,235|
| |Moultrie County|     0|  0.000|  0.000|    74|  5103.096| 187.179|  14,501|
| |Pope County|     0|  0.000|  0.000|     9|  2154.656| 34.201|   4,177|
| |Pike County|     0|  0.000|  0.000|    23|  1478.054| 91.805|  15,561|
| |Piatt County|     0|  0.000|  0.000|    63|  3854.626| 131.110|  16,344|
| |White County|     0|  0.000|  0.000|    69|  5097.141| 116.084|  13,537|
| |Menard County|     0|  0.000|  0.000|    56|  4591.669| 93.708|  12,196|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203| 124.462|   5,739|
| |Richland County|     0|  0.000|  0.000|    20|  1289.241| 64.462|  15,513|
| |Washington County|     0|  0.000|  0.000|    67|  4824.656| 92.584|  13,887|
| |Warren County|     0|  0.000|  0.000|   191| 11339.349| 67.850|  16,844|
| |Wabash County|     0|  0.000|  0.000|    35|  3038.194| 37.202|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    21|  4241.567| 288.542|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    18|  2659.574| 21.108|   6,768|
| |Logan County|     0|  0.000|  0.000|   122|  4263.051| 179.707|  28,618|
| |Henderson County|     0|  0.000|  0.000|    13|  1956.064| 85.981|   6,646|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 37.387|   3,821|
| |Hamilton County|     0|  0.000|  0.000|    29|  3573.189| 105.611|   8,116|
| |Greene County|     0|  0.000|  0.000|    58|  4472.203| 418.581|  12,969|
| |Fulton County|     0|  0.000|  0.000|    34|   990.099| 33.281|  34,340|
| |Massac County|     0|  0.000|  0.000|    40|  2904.444| 62.238|  13,772|
| |Mason County|     0|  0.000|  0.000|    53|  3967.363| 117.631|  13,359|
| |Marshall County|     0|  0.000|  0.000|    27|  2360.553| 74.938|  11,438|
| |Marion County|     0|  0.000|  0.000|   161|  4327.375| 88.314|  37,205|
| |Johnson County|     0|  0.000|  0.000|    69|  5556.898| 138.060|  12,417|
| |Edwards County|     0|  0.000|  0.000|    18|  2814.699| 111.694|   6,395|
| |Edgar County|     0|  0.000|  0.000|    29|  1689.878| 24.974|  17,161|
| |De Witt County|     0|  0.000|  0.000|    33|  2110.244| 27.406|  15,638|
| |Crawford County|     0|  0.000|  0.000|    29|  1553.544|  0.000|  18,667|
| |Clay County|     0|  0.000|  0.000|    23|  1744.539| 97.521|  13,184|
| |Calhoun County|     0|  0.000|  0.000|    10|  2110.150| 90.435|   4,739|
| |Brown County|     0|  0.000|  0.000|    14|  2128.306| 21.717|   6,578|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Lawrence County|     0|  0.000|  0.000|    50|  3189.182| 72.896|  15,678|
| |Franklin County|     0|  0.000|  0.000|   191|  4965.037| 219.100|  38,469|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,314| 571.317| N/A|124,221|  9703.258| N/A|12,801,989|
| |Philadelphia County| 1,699| 1072.558| N/A|31,448| 19852.733| N/A|1,584,064|
| |Montgomery County|   857| 1031.393|  1.203|10,149| 12214.246| 47.968| 830,915|
| |Delaware County|   699| 1233.355|  3.025| 9,274| 16363.563| 104.607| 566,747|
| |Bucks County|   582| 926.353|  0.682| 7,210| 11475.958| 43.203| 628,270|
| |Lancaster County|   411| 753.128|  1.047| 5,975| 10948.758| 76.700| 545,724|
| |Berks County|   368| 873.769|  1.018| 5,407| 12838.229| 64.108| 421,164|
| |Chester County|   349| 664.776|  0.272| 5,157|  9823.063| 52.246| 524,989|
| |Lehigh County|   337| 912.493|  0.774| 4,975| 13470.776| 47.191| 369,318|
| |Northampton County|   292| 956.483|  0.936| 3,931| 12876.492| 31.820| 305,285|
| |Allegheny County|   247| 203.117|  1.527| 8,932|  7345.123| 73.071|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,940|  9252.459| 26.572| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,462| 10906.788| 55.808| 317,417|
| |Dauphin County|   159| 571.328|  2.053| 2,829| 10165.326| 75.458| 278,299|
| |Monroe County|   124| 728.251|  0.839| 1,636|  9608.213| 31.882| 170,271|
| |York County|    93| 207.100|  1.591| 2,591|  5769.856| 76.668| 449,058|
| |Beaver County|    92| 561.219|  2.614| 1,326|  8088.868| 77.560| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,300|  5130.836| 39.468| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,617| 11403.948| 40.300| 141,793|
| |Schuylkill County|    51| 360.784|  2.021|   919|  6501.178| 23.244| 141,359|
| |Westmoreland County|    46| 131.843|  0.000| 1,553|  4451.145| 39.307| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,368|  8824.269| 77.406| 155,027|
| |Columbia County|    35| 538.760|  0.000|   477|  7342.528| 32.985|  64,964|
| |Carbon County|    28| 436.259|  0.000|   372|  5796.018| 26.710|  64,182|
| |Susquehanna County|    27| 669.510|  3.542|   214|  5306.487| 14.170|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  0.000|  55,809|
| |Adams County|    20| 194.158|  0.000|   524|  5086.934| 61.021| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   400|  3530.481| 76.914| 113,299|
| |Erie County|    19| 70.441|  1.589| 1,110|  4115.257| 67.264| 269,728|
| |Lawrence County|    16| 187.108|  6.682|   392|  4584.152| 71.836|  85,512|
| |Butler County|    15| 79.850|  0.000|   671|  3571.942| 50.191| 187,853|
| |Northumberland County|    13| 143.104|  3.145|   475|  5228.801| 106.935|  90,843|
| |Washington County|    13| 62.843|  1.381|   855|  4133.130| 62.843| 206,865|
| |Centre County|    10| 61.582|  0.000|   372|  2290.852| 12.316| 162,385|
| |Mercer County|     9| 82.249|  0.000|   442|  4039.333| 112.276| 109,424|
| |Wayne County|     9| 175.230|  2.781|   162|  3154.144| 11.126|  51,361|
| |Wyoming County|     8| 298.574|  0.000|    61|  2276.629| 21.327|  26,794|
| |Armstrong County|     7| 108.133|  2.207|   216|  3336.680| 61.790|  64,735|
| |Indiana County|     6| 71.367|  0.000|   322|  3830.005| 79.863|  84,073|
| |Juniata County|     6| 242.297|  0.000|   133|  5370.916| 34.614|  24,763|
| |Clinton County|     5| 129.426|  0.000|   122|  3158.004| 25.885|  38,632|
| |Fayette County|     5| 38.678|  1.105|   501|  3875.489| 96.141| 129,274|
| |Blair County|     5| 41.041|  2.345|   293|  2405.010| 70.356| 121,829|
| |Perry County|     5| 108.057|  0.000|   124|  2679.806| 12.349|  46,272|
| |Bedford County|     4| 83.528|  0.000|   143|  2986.134| 38.781|  47,888|
| |Huntingdon County|     4| 88.605|  0.000|   308|  6822.612| 56.961|  45,144|
| |Tioga County|     3| 73.908|  3.519|    38|   936.168| 10.558|  40,591|
| |Somerset County|     3| 40.846|  1.945|   135|  1838.060| 19.450|  73,447|
| |Montour County|     3| 164.564|  0.000|   102|  5595.173| 70.527|  18,230|
| |Bradford County|     3| 49.732|  0.000|    86|  1425.659|  9.473|  60,323|
| |Cambria County|     3| 23.043|  0.000|   341|  2619.209| 73.518| 130,192|
| |Clarion County|     2| 52.032|  0.000|    80|  2081.274| 14.866|  38,438|
| |Elk County|     2| 66.867|  0.000|    49|  1638.248| 19.105|  29,910|
| |Fulton County|     2| 137.646|  0.000|    27|  1858.224| 29.496|  14,530|
| |Snyder County|     2| 49.539|  0.000|   106|  2625.582| 28.308|  40,372|
| |Union County|     2| 44.521|  0.000|   238|  5297.954| 206.703|  44,923|
| |Crawford County|     1| 11.816|  0.000|   154|  1819.707| 37.137|  84,629|
| |Jefferson County|     1| 23.028|  0.000|    73|  1681.059| 49.346|  43,425|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  3.516|  40,625|
| |Greene County|     1| 27.599|  0.000|   116|  3201.501| 27.599|  36,233|
| |Mifflin County|     1| 21.674|  0.000|   120|  2600.893| 34.059|  46,138|
| |Warren County|     1| 25.516|  0.000|    23|   586.869| 14.581|  39,191|
| |Venango County|     0|  0.000|  0.000|    64|  1263.125|  5.639|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Cameron County|     0|  0.000|  0.000|     7|  1574.095| 32.124|   4,447|
| |Clearfield County|     0|  0.000|  0.000|   174|  2195.445| 59.483|  79,255|
| |Forest County|     0|  0.000|  0.000|    10|  1379.881| 19.713|   7,247|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,450| 645.849| N/A|92,603|  9272.487| N/A|9,986,857|
| |Wayne County| 2,826| 1615.464|  1.715|28,273| 16162.068| 73.170|1,749,343|
| |Oakland County| 1,129| 897.753|  0.341|15,615| 12416.666| 85.652|1,257,584|
| |Macomb County|   947| 1083.559|  1.798|10,545| 12065.604| 134.525| 873,972|
| |Genesee County|   296| 729.400|  0.704| 3,664|  9028.789| 49.988| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,549| 11490.894| 68.715| 656,955|
| |Saginaw County|   130| 682.275|  0.750| 2,032| 10664.483| 132.706| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,551|  6939.589| 53.241| 367,601|
| |Kalamazoo County|    83| 313.130|  0.539| 1,648|  6217.319| 47.428| 265,066|
| |Berrien County|    66| 430.245|  0.931| 1,376|  8969.955| 78.226| 153,401|
| |Muskegon County|    59| 339.928|  0.823| 1,179|  6792.805| 42.800| 173,566|
| |Ottawa County|    56| 191.893|  0.979| 1,841|  6308.467| 46.505| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   820|  5153.084| 37.705| 159,128|
| |Calhoun County|    42| 313.061|  0.000|   795|  5925.804| 48.982| 134,159|
| |Jackson County|    34| 214.498|  0.901|   711|  4485.521| 18.926| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   470|  5364.868| 79.902|  87,607|
| |Bay County|    31| 300.603|  0.000|   638|  6186.607| 121.904| 103,126|
| |Ingham County|    31| 106.017|  0.000| 1,554|  5314.528| 29.802| 292,406|
| |Tuscola County|    29| 555.077|  2.734|   356|  6814.049| 125.781|  52,245|
| |Livingston County|    28| 145.837|  0.000|   837|  4359.489| 39.436| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   343|  5035.084| 29.359|  68,122|
| |Monroe County|    25| 166.113|  2.848|   987|  6558.140| 78.785| 150,500|
| |Hillsdale County|    25| 548.186|  0.000|   271|  5942.331| 62.650|  45,605|
| |Gratiot County|    15| 368.451|  0.000|   156|  3831.888| 38.600|  40,711|
| |Cass County|    14| 270.338| 11.034|   326|  6295.016| 93.791|  51,787|
| |Alpena County|    13| 457.666|  0.000|   130|  4576.659| 25.146|  28,405|
| |Clinton County|    13| 163.327|  0.000|   423|  5314.404| 16.153|  79,595|
| |Iosco County|    12| 477.574|  0.000|   134|  5332.909| 28.427|  25,127|
| |Lenawee County|    12| 121.888|  0.000|   433|  4398.127| 44.982|  98,451|
| |Otsego County|    11| 445.922|  5.791|   135|  5472.677| 23.165|  24,668|
| |Marquette County|    11| 164.920|  0.000|   160|  2398.837| 47.120|  66,699|
| |Midland County|    10| 120.256|  0.000|   338|  4064.650| 46.384|  83,156|
| |Van Buren County|    10| 132.141|  0.000|   454|  5999.181| 75.509|  75,677|
| |Isabella County|     9| 128.807|  0.000|   207|  2962.560| 12.267|  69,872|
| |St. Joseph County|     8| 131.225|  2.343|   591|  9694.246| 70.299|  60,964|
| |Eaton County|     8| 72.551|  0.000|   462|  4189.792|  7.773| 110,268|
| |Ionia County|     7| 108.197|  4.416|   274|  4235.127| 17.665|  64,697|
| |Allegan County|     6| 50.813|  0.000|   529|  4479.976| 26.616| 118,081|
| |Sanilac County|     6| 145.737|  0.000|   110|  2671.848| 45.109|  41,170|
| |Oceana County|     6| 226.697|  0.000|   478| 18060.226| 59.373|  26,467|
| |Crawford County|     5| 356.405|  0.000|   106|  7555.777| 91.647|  14,029|
| |Grand Traverse County|     5| 53.713|  0.000|   213|  2288.157| 16.881|  93,088|
| |Kalkaska County|     4| 221.754|  0.000|    54|  2993.680| 47.519|  18,038|
| |Huron County|     4| 129.111|  0.000|   158|  5099.900| 55.333|  30,981|
| |Wexford County|     4| 118.938|  0.000|    69|  2051.679| 12.743|  33,631|
| |Delta County|     3| 83.836|  0.000|    97|  2710.709| 63.875|  35,784|
| |Clare County|     3| 96.931|  0.000|    72|  2326.333| 50.773|  30,950|
| |Arenac County|     3| 201.572|  0.000|    42|  2822.012|  9.599|  14,883|
| |Barry County|     2| 32.494|  0.000|   191|  3103.168| 44.099|  61,550|
| |Charlevoix County|     2| 76.502|  0.000|    49|  1874.307| 27.322|  26,143|
| |Branch County|     2| 45.959|  0.000|   365|  8387.527| 114.898|  43,517|
| |Cheboygan County|     2| 79.126|  0.000|    49|  1938.598| 62.171|  25,276|
| |Ogemaw County|     2| 95.252|  0.000|    54|  2571.796| 20.411|  20,997|
| |Mecosta County|     2| 46.027|  0.000|    68|  1564.909| 36.164|  43,453|
| |Gladwin County|     2| 78.589|  0.000|    59|  2318.362| 33.681|  25,449|
| |Emmet County|     2| 59.853|  0.000|    62|  1855.454| 17.101|  33,415|
| |Dickinson County|     2| 79.242|  0.000|    55|  2179.167| 50.942|  25,239|
| |Gogebic County|     1| 71.556|  0.000|   120|  8586.762| 214.669|  13,975|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  9.449|  15,118|
| |Iron County|     1| 90.367|  0.000|    20|  1807.338| 38.729|  11,066|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Benzie County|     1| 56.287|  0.000|    29|  1632.331|  8.041|  17,766|
| |Montmorency County|     1| 107.204| 15.315|     9|   964.837| 15.315|   9,328|
| |Presque Isle County|     1| 79.416|  0.000|    20|  1588.310| 34.035|  12,592|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Montcalm County|     1| 15.652|  0.000|   192|  3005.259| 24.597|  63,888|
| |Manistee County|     0|  0.000|  0.000|    39|  1588.077| 29.086|  24,558|
| |Ontonagon County|     0|  0.000|  0.000|    14|  2447.552| 224.775|   5,720|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Roscommon County|     0|  0.000|  0.000|    53|  2206.586| 29.738|  24,019|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128| 17.650|   8,094|
| |Newaygo County|     0|  0.000|  0.000|   251|  5124.541| 11.667|  48,980|
| |Menominee County|     0|  0.000|  0.000|   141|  6189.640| 257.118|  22,780|
| |Mason County|     0|  0.000|  0.000|   102|  3499.863| 24.509|  29,144|
| |Mackinac County|     0|  0.000|  0.000|    26|  2407.630| 79.372|  10,799|
| |Luce County|     0|  0.000|  0.000|     6|   963.236| 68.803|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    72|  3308.671| 39.389|  21,761|
| |Lake County|     0|  0.000|  0.000|    23|  1940.437| 60.262|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    50|  1401.188|  8.007|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    40|  1070.979| 30.599|  37,349|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846| 18.375|  23,324|
| |Alger County|     0|  0.000|  0.000|    11|  1207.729| 31.370|   9,108|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,444| 1246.463| N/A|50,330| 14116.676| N/A|3,565,287|
| |Hartford County| 1,415| 1586.821|  0.481|12,800| 14354.282| 15.860| 891,720|
| |Fairfield County| 1,409| 1493.642|  0.151|18,035| 19118.402| 24.987| 943,332|
| |New Haven County| 1,106| 1293.935|  0.334|13,224| 15471.064| 23.064| 854,757|
| |Middlesex County|   192| 1182.004|  0.879| 1,405|  8649.560| 14.951| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,615|  8955.654| 13.467| 180,333|
| |New London County|   103| 388.377|  0.000| 1,457|  5493.843| 23.163| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,056|  7006.323|  5.687| 150,721|
| |Windham County|    15| 128.444|  0.000|   738|  6319.467| 31.805| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,169| 896.792| N/A|131,707| 28331.434| N/A|4,648,794|
| |Orleans Parish|   562| 1440.494|  0.732|10,768| 27600.066| 125.228| 390,144|
| |Jefferson Parish|   529| 1223.141|  3.633|15,350| 35491.904| 269.864| 432,493|
| |East Baton Rouge Parish|   350| 795.348|  7.142|12,244| 27823.542| 318.464| 440,059|
| |Caddo Parish|   295| 1228.123|  8.326| 6,688| 27843.000| 231.351| 240,204|
| |St. Tammany Parish|   214| 821.753|  6.034| 5,266| 20221.259| 251.243| 260,419|
| |Calcasieu Parish|   146| 717.670| 13.342| 6,815| 33499.479| 202.240| 203,436|
| |Rapides Parish|   114| 879.304|  8.815| 3,304| 25484.388| 260.045| 129,648|
| |Ouachita Parish|   113| 737.218|  7.456| 4,896| 31941.753| 360.687| 153,279|
| |Lafourche Parish|    99| 1014.199|  4.390| 2,839| 29083.943| 365.873|  97,614|
| |Lafayette Parish|    96| 392.815|  5.261| 7,643| 31273.784| 713.146| 244,390|
| |St. John the Baptist Parish|    92| 2147.676| 13.340| 1,430| 33382.356| 250.118|  42,837|
| |St. Landry Parish|    90| 1095.904| 26.093| 2,735| 33303.297| 885.421|  82,124|
| |Acadia Parish|    85| 1369.973| 18.420| 2,601| 41921.186| 455.890|  62,045|
| |Terrebonne Parish|    85| 769.502|  9.053| 3,057| 27674.926| 332.373| 110,461|
| |Bossier Parish|    81| 637.599|  8.996| 2,339| 18411.669| 248.518| 127,039|
| |Tangipahoa Parish|    77| 571.395| 14.841| 3,498| 25957.643| 359.374| 134,758|
| |Ascension Parish|    74| 584.500|  3.385| 2,890| 22827.083| 278.709| 126,604|
| |Iberia Parish|    72| 1031.075| 14.320| 2,539| 36359.731| 597.369|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,281| 27730.874| 253.589|  46,194|
| |St. Mary Parish|    55| 1114.534| 17.369| 1,611| 32645.700| 480.552|  49,348|
| |St. Charles Parish|    52| 979.284|  5.381| 1,484| 27947.269| 293.247|  53,100|
| |Livingston Parish|    51| 362.244|  2.029| 2,938| 20868.108| 261.790| 140,789|
| |Iberville Parish|    48| 1476.423|  4.394| 1,250| 38448.525| 430.623|  32,511|
| |St. Martin Parish|    46| 860.923| 10.695| 1,714| 32078.756| 521.367|  53,431|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   722| 27281.315| 329.276|  26,465|
| |East Feliciana Parish|    36| 1881.369|  7.466|   591| 30885.811| 515.137|  19,135|
| |Union Parish|    33| 1492.672|  0.000|   708| 32024.606| 549.252|  22,108|
| |St. James Parish|    32| 1516.875|  6.772|   719| 34082.290| 474.024|  21,096|
| |Avoyelles Parish|    32| 797.130| 17.793| 1,070| 26654.045| 423.475|  40,144|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   794| 36539.347| 361.580|  21,730|
| |Lincoln Parish|    31| 663.215| 21.394|   805| 17222.198| 259.785|  46,742|
| |Allen Parish|    30| 1170.640| 39.021| 1,278| 49869.278| 680.086|  25,627|
| |Bienville Parish|    30| 2265.690|  0.000|   382| 28849.785| 312.881|  13,241|
| |Jefferson Davis Parish|    28| 892.629| 18.217| 1,028| 32772.252| 296.025|  31,368|
| |Vernon Parish|    28| 590.356| 18.072|   770| 16234.793| 198.793|  47,429|
| |De Soto Parish|    26| 946.728| 10.404|   727| 26471.980| 338.117|  27,463|
| |Vermilion Parish|    26| 436.894| 21.605| 1,584| 26616.928| 494.506|  59,511|
| |St. Bernard Parish|    24| 508.001|  3.024| 1,109| 23473.880| 217.715|  47,244|
| |Assumption Parish|    20| 913.617|  0.000|   588| 26860.354| 215.353|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   460| 19830.150| 215.545|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   376| 23882.114| 154.254|  15,744|
| |Franklin Parish|    18| 899.326|  7.138|   938| 46864.851| 706.613|  20,015|
| |Grant Parish|    18| 803.966| 57.426|   306| 13667.426| 153.136|  22,389|
| |Beauregard Parish|    18| 480.038|  3.810|   835| 22268.448| 175.252|  37,497|
| |Natchitoches Parish|    17| 445.516|  0.000|   774| 20284.082| 310.738|  38,158|
| |West Feliciana Parish|    16| 1027.749|  0.000|   348| 22353.546| 201.879|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   894| 23317.684| 253.372|  38,340|
| |Red River Parish|    12| 1421.464| 16.922|   237| 28073.916| 812.265|   8,442|
| |Morehouse Parish|    12| 482.431|  5.743|   531| 21347.592| 505.404|  24,874|
| |Claiborne Parish|    11| 701.978|  0.000|   277| 17677.090| 510.530|  15,670|
| |Sabine Parish|    10| 418.690|  0.000|   647| 27089.265| 669.905|  23,884|
| |Concordia Parish|     9| 467.314|  7.418|   334| 17342.541| 348.631|  19,259|
| |Richland Parish|     8| 397.575| 14.199|   602| 29917.503| 411.774|  20,122|
| |Evangeline Parish|     7| 209.612| 21.389|   895| 26800.419| 697.281|  33,395|
| |Winn Parish|     7| 503.452|  0.000|   425| 30566.743| 277.412|  13,904|
| |West Carroll Parish|     6| 554.017| 13.191|   294| 27146.814| 461.681|  10,830|
| |Madison Parish|     6| 547.895|  0.000|   613| 55976.623| 613.121|  10,951|
| |Catahoula Parish|     5| 526.648| 15.047|   295| 31072.256| 466.460|   9,494|
| |Caldwell Parish|     3| 302.480| 14.404|   221| 22282.718| 302.480|   9,918|
| |East Carroll Parish|     2| 291.503| 20.822|   520| 75790.701| 395.611|   6,861|
| |LaSalle Parish|     2| 134.300|  0.000|   305| 20480.795| 604.351|  14,892|
| |St. Helena Parish|     2| 197.394| 14.100|   267| 26352.152| 296.092|  10,132|
| |Tensas Parish|     0|  0.000|  0.000|    89| 20535.302| 791.087|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   169| 24236.340| 40.974|   6,973|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,153| 570.568| N/A|187,523| 25763.194| N/A|7,278,717|
| |Maricopa County| 2,356| 525.258|  7.899|126,371| 28173.765| 172.336|4,485,414|
| |Pima County|   489| 466.924|  3.683|17,996| 17183.578| 171.192|1,047,279|
| |Yuma County|   289| 1351.813| 17.374|11,609| 54301.712| 271.298| 213,787|
| |Navajo County|   200| 1803.036| 15.455| 5,375| 48456.601| 117.197| 110,924|
| |Mohave County|   168| 791.777| 10.099| 3,202| 15090.889| 109.071| 212,181|
| |Pinal County|   156| 337.087|  4.630| 8,378| 18103.282| 23.769| 462,789|
| |Apache County|   139| 1933.590|  5.962| 3,194| 44430.843| 218.597|  71,887|
| |Coconino County|   117| 815.467|  0.996| 3,099| 21599.431| 101.560| 143,476|
| |Yavapai County|    67| 284.986|  3.038| 2,018|  8583.618| 97.223| 235,099|
| |Santa Cruz County|    53| 1139.834|  9.217| 2,671| 57443.331| 187.412|  46,498|
| |Cochise County|    52| 412.954|  2.269| 1,611| 12793.634| 61.262| 125,922|
| |Gila County|    38| 703.469| 23.802|   916| 16957.311| 198.347|  54,018|
| |Graham County|    16| 411.978| 25.749|   549| 14136.004| 217.024|  38,837|
| |La Paz County|    12| 568.505| 13.536|   477| 22598.067| 20.304|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,129| 388.889| N/A|199,420| 18782.335| N/A|10,617,423|
| |Fulton County|   433| 406.979|  4.700|20,468| 19237.981| 301.307|1,063,937|
| |Cobb County|   320| 420.975|  4.135|13,729| 18061.123| 354.258| 760,141|
| |Gwinnett County|   262| 279.840|  3.357|19,971| 21330.841| 311.883| 936,250|
| |DeKalb County|   238| 313.448|  2.446|14,047| 18500.007| 271.492| 759,297|
| |Dougherty County|   171| 1944.154|  3.248| 2,732| 31060.985| 180.285|  87,956|
| |Clayton County|   110| 376.382|  4.399| 5,059| 17310.166| 245.382| 292,256|
| |Muscogee County|    98| 500.590| 11.676| 4,780| 24416.532| 300.646| 195,769|
| |Hall County|    91| 445.116|  8.385| 6,114| 29905.939| 396.202| 204,441|
| |Richmond County|    90| 444.405|  4.938| 4,412| 21785.718| 441.583| 202,518|
| |Chatham County|    75| 259.130|  3.949| 5,764| 19915.005| 351.923| 289,430|
| |Troup County|    69| 986.814| 12.259| 2,298| 32865.193| 251.300|  69,922|
| |Bibb County|    68| 443.983|  6.529| 3,645| 23798.797| 402.010| 153,159|
| |Cherokee County|    64| 247.321|  4.416| 3,535| 13660.621| 358.836| 258,773|
| |Bartow County|    63| 584.752|  3.978| 1,885| 17496.148| 354.033| 107,738|
| |Houston County|    60| 380.076|  9.954| 1,992| 12618.536| 171.939| 157,863|
| |Sumter County|    56| 1896.762|  0.000|   768| 26012.735| 174.192|  29,524|
| |Douglas County|    51| 348.496|  1.952| 2,678| 18299.475| 338.735| 146,343|
| |Carroll County|    50| 416.694|  3.572| 1,894| 15784.386| 164.297| 119,992|
| |Habersham County|    49| 1081.010|  3.152| 1,145| 25260.325| 305.708|  45,328|
| |Henry County|    47| 200.374|  3.045| 3,411| 14542.059| 238.744| 234,561|
| |Glynn County|    47| 551.048| 21.774| 2,557| 29979.365| 380.206|  85,292|
| |Upson County|    46| 1747.720|  0.000|   541| 20554.711| 287.668|  26,320|
| |Lowndes County|    44| 374.768| 14.601| 3,193| 27196.225| 253.090| 117,406|
| |Thomas County|    42| 944.861|  9.641| 1,125| 25308.767| 404.940|  44,451|
| |Spalding County|    41| 614.665|  4.283|   949| 14227.246| 173.477|  66,703|
| |Mitchell County|    41| 1875.314|  0.000|   652| 29822.074| 228.697|  21,863|
| |Newton County|    40| 357.961|  6.392| 1,823| 16314.075| 262.079| 111,744|
| |Walton County|    39| 412.293|  7.551| 1,118| 11819.056| 225.024|  94,593|
| |Baldwin County|    39| 868.790|  3.182| 1,051| 23412.787| 251.408|  44,890|
| |Tift County|    39| 959.551| 14.059| 1,345| 33092.215| 337.425|  40,644|
| |Butts County|    38| 1523.901|  5.729|   497| 19931.023| 177.598|  24,936|
| |Hancock County|    35| 4138.583| 16.892|   318| 37601.987| 591.226|   8,457|
| |Early County|    32| 3140.334| 14.019|   360| 35328.754| 196.271|  10,190|
| |Whitfield County|    32| 305.845|  6.827| 3,549| 33920.174| 432.826| 104,628|
| |Barrow County|    32| 384.431|  0.000| 1,296| 15569.438| 290.039|  83,240|
| |Terrell County|    30| 3516.587|  0.000|   302| 35400.305| 167.457|   8,531|
| |Fayette County|    29| 253.450|  4.994| 1,131|  9884.549| 188.527| 114,421|
| |Ware County|    29| 811.552| 23.987| 1,153| 32266.189| 279.846|  35,734|
| |Coffee County|    29| 670.164| 13.205| 1,468| 33924.156| 399.457|  43,273|
| |Randolph County|    26| 3835.940|  0.000|   272| 40129.832| 231.843|   6,778|
| |Monroe County|    25| 906.520| 10.360|   460| 16679.962| 165.764|  27,578|
| |Jenkins County|    24| 2766.252| 32.932|   244| 28123.559| 230.521|   8,676|
| |Columbia County|    24| 153.145|  4.558| 2,284| 14574.320| 287.147| 156,714|
| |Colquitt County|    24| 526.316|  6.266| 1,555| 34100.877| 231.830|  45,600|
| |Paulding County|    23| 136.363|  3.388| 1,694| 10043.458| 204.969| 168,667|
| |Worth County|    23| 1135.971|  0.000|   449| 22176.125| 155.226|  20,247|
| |Gordon County|    23| 396.805|  0.000| 1,193| 20582.095| 411.593|  57,963|
| |Coweta County|    22| 148.139|  0.962| 1,514| 10194.668| 149.101| 148,509|
| |Lee County|    22| 733.529|  0.000|   544| 18138.170| 114.316|  29,992|
| |Forsyth County|    22| 90.071|  1.170| 2,293|  9387.845| 205.291| 244,252|
| |Wilcox County|    19| 2200.347| 16.544|   184| 21308.628| 281.247|   8,635|
| |Appling County|    19| 1033.395| 23.310|   678| 36875.884| 590.511|  18,386|
| |Turner County|    18| 2254.227|  0.000|   250| 31308.704| 411.486|   7,985|
| |Clarke County|    18| 140.262|  1.113| 2,081| 16215.879| 378.486| 128,331|
| |Putnam County|    18| 813.780|  6.459|   430| 19440.300| 297.094|  22,119|
| |Brooks County|    18| 1164.521| 27.727|   413| 26719.286| 360.447|  15,457|
| |Rockdale County|    18| 198.029|  3.143| 1,347| 14819.134| 268.753|  90,896|
| |Harris County|    17| 482.461|  4.054|   657| 18645.703| 133.792|  35,236|
| |Floyd County|    17| 172.592|  2.901| 1,517| 15401.328| 339.383|  98,498|
| |Walker County|    17| 243.689|  2.048|   710| 10177.606| 315.362|  69,761|
| |Jackson County|    16| 219.247|  5.873| 1,070| 14662.154| 219.247|  72,977|
| |Oconee County|    15| 372.393|  0.000|   441| 10948.361| 159.597|  40,280|
| |Peach County|    14| 508.241| 10.372|   387| 14049.227| 274.865|  27,546|
| |Dooly County|    14| 1045.556|  0.000|   254| 18969.380| 128.027|  13,390|
| |Bulloch County|    14| 175.862|  3.589| 1,304| 16380.263| 344.545|  79,608|
| |Crisp County|    14| 625.782|  0.000|   385| 17209.011| 140.482|  22,372|
| |Stephens County|    12| 462.874| 11.021|   623| 24030.858| 341.645|  25,925|
| |Lamar County|    12| 629.030| 22.465|   275| 14415.264| 284.561|  19,077|
| |Greene County|    12| 654.879|  7.796|   313| 17081.423| 459.974|  18,324|
| |Polk County|    11| 258.137|  6.705|   808| 18961.350| 422.406|  42,613|
| |Decatur County|    11| 416.604| 16.231|   797| 30184.820| 649.252|  26,404|
| |Johnson County|    11| 1140.724| 14.815|   241| 24992.222| 207.404|   9,643|
| |Wilkinson County|    11| 1228.501| 15.955|   215| 24011.615| 478.637|   8,954|
| |Telfair County|    10| 630.517| 27.022|   281| 17717.528| 243.199|  15,860|
| |Macon County|    10| 772.380|  0.000|   177| 13671.121| 22.068|  12,947|
| |McDuffie County|    10| 469.219|  6.703|   356| 16704.204| 402.188|  21,312|
| |Emanuel County|    10| 441.579| 18.925|   513| 22653.007| 548.820|  22,646|
| |Wayne County|     9| 300.732| 23.868|   785| 26230.494| 739.896|  29,927|
| |Laurens County|     9| 189.290| 15.023|   951| 20001.683| 567.871|  47,546|
| |Screven County|     9| 644.422|  0.000|   210| 15036.517| 358.012|  13,966|
| |Bleckley County|     9| 699.138| 66.585|   242| 18799.037| 1209.619|  12,873|
| |Catoosa County|     9| 133.175|  0.000|   637|  9425.866| 192.365|  67,580|
| |Bacon County|     8| 716.589| 25.592|   438| 39233.250| 294.313|  11,164|
| |Toombs County|     8| 298.174| 10.649|   759| 28289.228| 585.698|  26,830|
| |Bryan County|     8| 201.883|  3.605|   661| 16680.546| 342.479|  39,627|
| |Pierce County|     8| 410.994| 14.678|   410| 21063.447| 220.175|  19,465|
| |Jefferson County|     8| 520.766| 18.599|   504| 32808.228| 511.466|  15,362|
| |Jeff Davis County|     8| 529.276| 18.903|   457| 30234.866| 500.922|  15,115|
| |Hart County|     7| 267.125| 27.258|   310| 11829.803| 223.512|  26,205|
| |Stewart County|     7| 1057.242| 43.153|   255| 38513.820| 107.882|   6,621|
| |Union County|     7| 285.586|  5.828|   264| 10770.674| 215.647|  24,511|
| |Oglethorpe County|     7| 458.746|  0.000|   218| 14286.651| 271.503|  15,259|
| |Burke County|     7| 312.737|  0.000|   470| 20998.079| 351.032|  22,383|
| |Lumpkin County|     6| 178.518|  0.000|   344| 10235.049| 178.518|  33,610|
| |Franklin County|     6| 256.970| 12.237|   406| 17388.325| 189.669|  23,349|
| |Meriwether County|     6| 283.460|  6.749|   396| 18708.367| 256.464|  21,167|
| |Madison County|     6| 200.803|  9.562|   403| 13487.282| 296.424|  29,880|
| |Calhoun County|     6| 969.462|  0.000|   203| 32800.129| 207.742|   6,189|
| |Cook County|     6| 347.423|  0.000|   440| 25477.707| 289.519|  17,270|
| |Haralson County|     6| 201.396|  0.000|   222|  7451.665| 124.674|  29,792|
| |Camden County|     5| 91.465|  2.613|   762| 13939.194| 190.769|  54,666|
| |Pickens County|     5| 153.417|  0.000|   390| 11966.494| 416.416|  32,591|
| |White County|     5| 162.348|  0.000|   353| 11461.783| 236.565|  30,798|
| |Grady County|     5| 202.980|  0.000|   493| 20013.803| 429.157|  24,633|
| |Brantley County|     5| 261.657|  7.476|   251| 13135.172| 171.946|  19,109|
| |Marion County|     5| 598.158| 17.090|   150| 17944.730| 85.451|   8,359|
| |Ben Hill County|     4| 239.521|  8.554|   452| 27065.868| 863.986|  16,700|
| |Candler County|     4| 370.268|  0.000|   260| 24067.389| 409.939|  10,803|
| |Clinch County|     4| 604.412|  0.000|   200| 30220.610| 518.068|   6,618|
| |Gilmer County|     4| 127.514|  4.554|   633| 20179.158| 523.720|  31,369|
| |Wilkes County|     4| 409.123| 14.612|   193| 19740.207| 204.562|   9,777|
| |Lanier County|     4| 383.767|  0.000|   219| 21011.225| 54.824|  10,423|
| |Lincoln County|     4| 504.987|  0.000|   143| 18053.276| 252.493|   7,921|
| |Pike County|     4| 210.948|  0.000|   216| 11391.203| 158.211|  18,962|
| |Heard County|     4| 335.486| 11.982|   143| 11993.626| 143.780|  11,923|
| |Banks County|     4| 207.965|  7.427|   271| 14089.633| 200.538|  19,234|
| |Seminole County|     4| 494.438| 35.317|   196| 24227.441| 900.583|   8,090|
| |Baker County|     3| 987.492|  0.000|    63| 20737.327| 235.117|   3,038|
| |Fannin County|     3| 114.556|  5.455|   335| 12792.119| 278.208|  26,188|
| |Liberty County|     3| 48.832|  2.325|   727| 11833.645| 239.510|  61,435|
| |Jones County|     3| 104.402|  0.000|   309| 10753.437| 193.890|  28,735|
| |Twiggs County|     3| 369.458|  0.000|   121| 14901.478| 475.018|   8,120|
| |Treutlen County|     3| 434.720|  0.000|   129| 18692.943| 600.327|   6,901|
| |Rabun County|     3| 175.060|  0.000|   215| 12545.953| 183.396|  17,137|
| |Talbot County|     3| 484.262|  0.000|   138| 22276.029| 230.601|   6,195|
| |Dodge County|     3| 145.596|  0.000|   221| 10725.552| 221.860|  20,605|
| |Dawson County|     3| 114.907|  0.000|   378| 14478.321| 421.327|  26,108|
| |Charlton County|     3| 224.014|  0.000|   437| 32631.422| 512.033|  13,392|
| |Chattooga County|     3| 121.021|  5.763|   267| 10770.906| 397.642|  24,789|
| |Washington County|     2| 98.164|  0.000|   479| 23510.356| 364.610|  20,374|
| |McIntosh County|     2| 139.101|  0.000|   187| 13005.981| 298.074|  14,378|
| |Montgomery County|     2| 218.055| 15.575|   155| 16899.259| 264.781|   9,172|
| |Murray County|     2| 49.880|  0.000|   608| 15163.607| 249.401|  40,096|
| |Taylor County|     2| 249.377|  0.000|    88| 10972.569| 302.814|   8,020|
| |Pulaski County|     2| 179.582|  0.000|   123| 11044.267| 448.954|  11,137|
| |Atkinson County|     2| 244.948|  0.000|   320| 39191.672| 419.911|   8,165|
| |Chattahoochee County|     2| 183.368| 13.098|   761| 69771.706| 1257.384|  10,907|
| |Clay County|     2| 705.716|  0.000|    86| 30345.801| 302.450|   2,834|
| |Echols County|     2| 499.251|  0.000|   222| 55416.875| 142.643|   4,006|
| |Effingham County|     2| 31.106|  2.222|   745| 11587.035| 208.855|  64,296|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724| 109.595|   2,607|
| |Evans County|     1| 93.861|  0.000|   261| 24497.841| 455.899|  10,654|
| |Wheeler County|     1| 127.307|  0.000|    94| 11966.900| 181.868|   7,855|
| |Warren County|     1| 190.331|  0.000|    79| 15036.163| 652.564|   5,254|
| |Towns County|     1| 83.077|  0.000|   144| 11963.114| 296.704|  12,037|
| |Dade County|     1| 62.050|  0.000|   127|  7880.367| 141.829|  16,116|
| |Elbert County|     1| 52.100|  0.000|   360| 18755.861| 267.941|  19,194|
| |Schley County|     1| 190.223|  0.000|    68| 12935.134| 353.270|   5,257|
| |Quitman County|     1| 434.972|  0.000|    30| 13049.152| 62.139|   2,299|
| |Irwin County|     1| 106.202|  0.000|   167| 17735.769| 151.717|   9,416|
| |Tattnall County|     1| 39.548|  0.000|   511| 20208.811| 485.870|  25,286|
| |Long County|     1| 51.127|  0.000|   129|  6595.429| 36.520|  19,559|
| |Jasper County|     1| 70.328|  0.000|   164| 11533.863| 381.783|  14,219|
| |Taliaferro County|     0|  0.000|  0.000|    13|  8458.035|  0.000|   1,537|
| |Berrien County|     0|  0.000|  0.000|   295| 15208.537| 235.677|  19,397|
| |Crawford County|     0|  0.000|  0.000|   104|  8384.392| 172.755|  12,404|
| |Morgan County|     0|  0.000|  0.000|   279| 14473.957| 392.790|  19,276|
| |Glascock County|     0|  0.000|  0.000|    25|  8414.675| 96.168|   2,971|
| |Miller County|     0|  0.000|  0.000|   143| 25008.744| 349.773|   5,718|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,673| 314.224| N/A|101,731|  8703.065| N/A|11,689,100|
| |Franklin County|   525| 398.707|  1.193|18,483| 14036.769| 133.336|1,316,756|
| |Cuyahoga County|   500| 404.835|  2.660|13,640| 11043.891| 102.597|1,235,072|
| |Lucas County|   323| 754.060|  1.668| 5,377| 12552.878| 144.409| 428,348|
| |Hamilton County|   255| 311.937|  1.223| 9,689| 11852.379| 92.445| 817,473|
| |Mahoning County|   254| 1110.708|  0.625| 2,566| 11220.773| 96.828| 228,683|
| |Summit County|   223| 412.190|  1.584| 3,573|  6604.278| 73.671| 541,013|
| |Stark County|   139| 375.061|  2.698| 1,844|  4975.635| 59.362| 370,606|
| |Trumbull County|   107| 540.475|  2.886| 1,534|  7748.492| 72.881| 197,974|
| |Montgomery County|    94| 176.796|  4.299| 4,398|  8271.784| 91.622| 531,687|
| |Lorain County|    78| 251.749|  0.922| 1,802|  5816.036| 77.461| 309,833|
| |Butler County|    63| 164.433|  1.491| 2,944|  7683.996| 85.759| 383,134|
| |Portage County|    61| 375.463|  0.879|   765|  4708.678| 42.207| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,665| 16342.275| 116.380| 101,883|
| |Wayne County|    58| 501.253|  0.000|   544|  4701.409| 55.558| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,058|  8087.634| 146.333| 130,817|
| |Licking County|    49| 277.052|  4.846| 1,299|  7344.709| 140.545| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   574|  5902.860| 51.419|  97,241|
| |Marion County|    45| 691.319|  2.195| 2,929| 44997.158| 98.760|  65,093|
| |Geauga County|    44| 469.840|  1.525|   558|  5958.419| 41.187|  93,649|
| |Allen County|    44| 429.893|  2.792|   760|  7425.428| 147.950| 102,351|
| |Pickaway County|    42| 718.477|  0.000| 2,387| 40833.433| 73.314|  58,457|
| |Warren County|    39| 166.239|  2.436| 1,803|  7685.356| 102.910| 234,602|
| |Miami County|    38| 355.183|  1.335|   853|  7972.931| 112.163| 106,987|
| |Lake County|    38| 165.110|  1.241| 1,124|  4883.793| 50.278| 230,149|
| |Medina County|    35| 194.719|  1.590|   930|  5173.968| 75.503| 179,746|
| |Fairfield County|    32| 203.079|  6.346| 1,400|  8884.714| 132.364| 157,574|
| |Darke County|    29| 567.370|  5.590|   402|  7864.927| 226.389|  51,113|
| |Erie County|    27| 363.558|  0.000|   592|  7971.346| 130.804|  74,266|
| |Ottawa County|    26| 641.579|  3.525|   390|  9623.689| 109.280|  40,525|
| |Belmont County|    26| 388.025|  0.000|   621|  9267.827| 68.224|  67,006|
| |Washington County|    22| 367.211|  0.000|   205|  3421.742| 19.076|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,316|  6291.323| 75.124| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    93|  6811.191| 20.925|  13,654|
| |Sandusky County|    17| 290.509|  0.000|   384|  6562.083| 126.945|  58,518|
| |Putnam County|    17| 502.053|  0.000|   208|  6142.760| 67.503|  33,861|
| |Clark County|    14| 104.413|  1.065| 1,158|  8636.442| 76.712| 134,083|
| |Tuscarawas County|    14| 152.195|  1.553|   788|  8566.428| 63.674|  91,987|
| |Mercer County|    13| 315.749|  0.000|   625| 15180.220| 312.279|  41,172|
| |Greene County|    12| 71.032|  0.846|   703|  4161.315| 65.113| 168,937|
| |Hardin County|    12| 382.592|  0.000|   169|  5388.172| 86.539|  31,365|
| |Richland County|    12| 99.047|  0.000|   608|  5018.406| 80.181| 121,154|
| |Clermont County|    11| 53.287|  0.000|   941|  4558.490| 59.516| 206,428|
| |Madison County|    10| 223.559|  0.000|   388|  8674.074| 175.653|  44,731|
| |Hocking County|     9| 318.426|  0.000|   118|  4174.922| 35.381|  28,264|
| |Wyandot County|     8| 367.444|  6.562|   148|  6797.722| 183.722|  21,772|
| |Knox County|     7| 112.320| 11.461|   206|  3305.414| 84.813|  62,322|
| |Guernsey County|     7| 180.064|  0.000|   118|  3035.370| 25.723|  38,875|
| |Coshocton County|     6| 163.934|  0.000|   194|  5300.546| 31.226|  36,600|
| |Auglaize County|     6| 131.418|  3.129|   256|  5607.149| 106.386|  45,656|
| |Holmes County|     6| 136.488|  0.000|   328|  7461.328| 19.498|  43,960|
| |Clinton County|     6| 142.966|  0.000|   165|  3931.567| 57.867|  41,968|
| |Huron County|     5| 85.813|  2.452|   401|  6882.230| 61.295|  58,266|
| |Crawford County|     5| 120.499|  0.000|   174|  4193.377| 20.657|  41,494|
| |Carroll County|     5| 185.777|  0.000|   110|  4087.092| 10.616|  26,914|
| |Shelby County|     4| 82.321|  0.000|   200|  4116.073| 117.602|  48,590|
| |Defiance County|     4| 105.023|  0.000|   148|  3885.840| 71.265|  38,087|
| |Ross County|     4| 52.174|  0.000|   490|  6391.360| 165.840|  76,666|
| |Perry County|     3| 83.024|  3.954|   136|  3763.768| 118.606|  36,134|
| |Williams County|     3| 81.762|  0.000|   135|  3679.276| 42.828|  36,692|
| |Hancock County|     3| 39.587|  1.885|   379|  5001.122| 111.220|  75,783|
| |Ashland County|     3| 56.092|  0.000|   149|  2785.880| 42.736|  53,484|
| |Seneca County|     3| 54.369|  0.000|   222|  4023.343| 157.930|  55,178|
| |Logan County|     2| 43.791|  3.128|   155|  3393.764| 100.093|  45,672|
| |Jefferson County|     2| 30.616|  0.000|   234|  3582.090| 61.232|  65,325|
| |Henry County|     2| 74.058|  5.290|   117|  4332.371| 58.188|  27,006|
| |Vinton County|     2| 152.847|  0.000|    31|  2369.125| 10.918|  13,085|
| |Morrow County|     2| 56.612|  0.000|   172|  4868.659| 56.612|  35,328|
| |Preble County|     2| 48.921|  0.000|   204|  4989.971| 132.786|  40,882|
| |Adams County|     2| 72.207|  0.000|    61|  2202.325| 41.261|  27,698|
| |Brown County|     2| 46.049|  3.289|   138|  3177.381| 85.520|  43,432|
| |Champaign County|     2| 51.434|  3.674|   178|  4577.601| 146.953|  38,885|
| |Athens County|     1| 15.308|  0.000|   359|  5495.431| 30.615|  65,327|
| |Highland County|     1| 23.169|  0.000|   159|  3683.881| 89.366|  43,161|
| |Fulton County|     1| 23.738|  0.000|   147|  3489.531| 23.738|  42,126|
| |Gallia County|     1| 33.447|  0.000|    65|  2174.058| 33.447|  29,898|
| |Van Wert County|     1| 35.367|  0.000|    72|  2546.419| 15.157|  28,275|
| |Muskingum County|     1| 11.599|  0.000|   239|  2772.139| 96.105|  86,215|
| |Scioto County|     1| 13.278|  0.000|   234|  3106.992| 87.254|  75,314|
| |Union County|     1| 16.953|  0.000|   254|  4305.961| 92.028|  58,988|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 56.991|  15,040|
| |Morgan County|     0|  0.000|  0.000|    28|  1929.970| 78.774|  14,508|
| |Noble County|     0|  0.000|  0.000|    16|  1109.262|  0.000|  14,424|
| |Paulding County|     0|  0.000|  0.000|    70|  3748.929| 68.858|  18,672|
| |Pike County|     0|  0.000|  0.000|    77|  2772.577| 56.583|  27,772|
| |Meigs County|     0|  0.000|  0.000|    50|  2182.739| 155.910|  22,907|
| |Fayette County|     0|  0.000|  0.000|   115|  4031.551| 90.146|  28,525|
| |Jackson County|     0|  0.000|  0.000|    75|  2313.886| 35.259|  32,413|
| |Lawrence County|     0|  0.000|  0.000|   288|  4843.348| 163.367|  59,463|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,573| 591.001| N/A|96,258| 15921.782| N/A|6,045,680|
| |Baltimore County|   993| 1200.189|  5.007|26,104| 31550.576| 337.558| 827,370|
| |Montgomery County|   803| 764.261|  1.360|18,489| 17597.041| 87.970|1,050,688|
| |Prince George's County|   755| 830.284|  1.885|23,832| 26208.394| 149.561| 909,327|
| |Anne Arundel County|   225| 388.444|  1.973| 7,416| 12803.116| 100.872| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,082| 11874.535| 39.629| 259,547|
| |Carroll County|   117| 694.580|  0.000| 1,554|  9225.454| 53.429| 168,447|
| |Howard County|   112| 343.885|  2.632| 3,881| 11916.239| 96.937| 325,690|
| |Charles County|    91| 557.403|  0.000| 2,040| 12495.636| 114.631| 163,257|
| |Harford County|    69| 270.121|  0.559| 1,994|  7806.108| 78.855| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   999|  8800.987| 85.581| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,348| 13010.453| 68.941| 103,609|
| |Washington County|    31| 205.231|  0.946| 1,018|  6739.535| 34.048| 151,049|
| |Cecil County|    30| 291.673|  0.000|   706|  6864.032| 70.835| 102,855|
| |Calvert County|    28| 302.621|  0.000|   707|  7641.178| 111.167|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   434|  8614.359| 99.244|  50,381|
| |Kent County|    23| 1184.224|  0.000|   243| 12511.585| 58.843|  19,422|
| |Worcester County|    20| 382.585|  2.733|   694| 13275.691| 226.818|  52,276|
| |Allegany County|    18| 255.624|  0.000|   299|  4246.194| 52.748|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   375| 11744.809| 102.907|  31,929|
| |Talbot County|     4| 107.582|  0.000|   402| 10811.974| 130.635|  37,181|
| |Caroline County|     3| 89.804|  0.000|   453| 13560.438| 64.146|  33,406|
| |Somerset County|     3| 117.114|  0.000|   139|  5426.296| 89.230|  25,616|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    49|  1688.840| 29.542|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,838| 421.555| N/A|74,992| 11139.269| N/A|6,732,219|
| |Marion County|   725| 751.621|  0.889|15,963| 16549.137| 162.913| 964,582|
| |Lake County|   275| 566.435|  1.177| 7,632| 15720.103| 156.248| 485,493|
| |Allen County|   163| 429.740|  1.883| 3,937| 10379.674| 113.744| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,767| 11171.736| 103.869| 158,167|
| |Hendricks County|   108| 634.134|  2.516| 1,901| 11161.933| 126.659| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,803|  8292.630| 122.566| 338,011|
| |Elkhart County|    85| 411.939|  5.539| 4,883| 23664.710| 198.008| 206,341|
| |St. Joseph County|    82| 301.664|  1.577| 3,546| 13045.110| 206.014| 271,826|
| |Madison County|    65| 501.663|  0.000|   987|  7617.563| 154.358| 129,569|
| |Howard County|    65| 787.459|  0.000|   905| 10963.850| 164.414|  82,544|
| |Delaware County|    52| 455.601|  0.000|   738|  6466.027| 125.165| 114,135|
| |Clark County|    47| 397.288|  2.415| 1,244| 10515.460| 196.833| 118,302|
| |Bartholomew County|    47| 561.000|  0.000|   801|  9560.868| 98.900|  83,779|
| |Boone County|    46| 678.036|  0.000|   683| 10067.361| 101.074|  67,843|
| |Floyd County|    46| 585.823|  3.639|   791| 10073.610| 176.475|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,338|  7852.620| 119.894| 170,389|
| |Hancock County|    38| 486.132|  1.828|   670|  8571.282| 85.896|  78,168|
| |Morgan County|    34| 482.345|  4.053|   483|  6852.133| 117.546|  70,489|
| |Greene County|    34| 1065.096|  0.000|   251|  7862.916| 53.702|  31,922|
| |Decatur County|    32| 1204.865|  0.000|   338| 12726.383| 129.093|  26,559|
| |Monroe County|    30| 202.114|  0.000|   759|  5113.487| 70.259| 148,431|
| |Warrick County|    30| 476.206|  0.000|   586|  9301.883| 158.735|  62,998|
| |LaPorte County|    30| 273.005|  1.300|   921|  8381.261| 107.902| 109,888|
| |Grant County|    30| 456.142|  2.172|   528|  8028.098| 69.507|  65,769|
| |Noble County|    29| 607.406|  2.992|   684| 14326.408| 140.631|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   508| 10271.341| 124.204|  49,458|
| |Shelby County|    27| 603.635|  3.194|   558| 12475.128| 150.110|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   350|  7714.349| 69.272|  45,370|
| |Orange County|    24| 1221.623|  0.000|   173|  8805.864| 65.444|  19,646|
| |Harrison County|    23| 567.691|  3.526|   341|  8416.636| 165.723|  40,515|
| |Marshall County|    22| 475.593|  0.000|   790| 17078.127| 148.237|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   354|  9233.659| 40.989|  38,338|
| |Daviess County|    20| 599.682|  4.283|   273|  8185.662| 115.653|  33,351|
| |Henry County|    20| 416.910|  5.956|   385|  8025.515| 71.470|  47,972|
| |Franklin County|    14| 615.168| 25.109|   243| 10677.564| 119.267|  22,758|
| |Vanderburgh County|    13| 71.645|  0.787| 1,997| 11005.726| 213.359| 181,451|
| |Jennings County|    12| 432.666|  0.000|   226|  8148.549| 82.413|  27,735|
| |Perry County|    12| 626.011|  0.000|   186|  9703.167| 104.335|  19,169|
| |Kosciusko County|    12| 151.027|  0.000|   862| 10848.772| 77.311|  79,456|
| |Dubois County|    12| 280.794|  0.000|   700| 16379.633| 247.366|  42,736|
| |Tipton County|    11| 726.168| 56.585|   143|  9440.190| 339.507|  15,148|
| |Tippecanoe County|    11| 56.199|  0.000| 1,221|  6238.122| 86.124| 195,732|
| |Vigo County|    10| 93.425|  0.000|   668|  6240.774| 258.920| 107,038|
| |Scott County|    10| 418.883|  0.000|   268| 11226.071| 107.713|  23,873|
| |Wayne County|    10| 151.782|  2.168|   377|  5722.178| 130.099|  65,884|
| |White County|    10| 414.903|  0.000|   372| 15434.404| 148.180|  24,102|
| |LaGrange County|    10| 252.436|  0.000|   559| 14111.173| 61.306|  39,614|
| |Newton County|    10| 715.103|  0.000|   118|  8438.215| 81.726|  13,984|
| |Cass County|     9| 238.796|  0.000| 1,796| 47653.161| 170.569|  37,689|
| |Putnam County|     8| 212.902|  0.000|   290|  7717.692| 258.524|  37,576|
| |Starke County|     7| 304.414|  0.000|   178|  7740.813| 80.763|  22,995|
| |Ripley County|     7| 247.140|  0.000|   208|  7343.596| 100.874|  28,324|
| |Fayette County|     7| 303.004|  0.000|   190|  8224.396| 216.431|  23,102|
| |Whitley County|     6| 176.658|  0.000|   154|  4534.213| 25.237|  33,964|
| |Clay County|     5| 190.658|  0.000|   124|  4728.313| 147.079|  26,225|
| |Ohio County|     5| 851.064| 24.316|    65| 11063.830| 340.426|   5,875|
| |Jackson County|     5| 113.043|  3.230|   588| 13293.844| 116.273|  44,231|
| |Gibson County|     4| 118.839|  0.000|   228|  6773.820| 118.839|  33,659|
| |DeKalb County|     4| 92.007|  0.000|   235|  5405.405| 42.717|  43,475|
| |Randolph County|     4| 162.173|  0.000|   123|  4986.823| 115.838|  24,665|
| |Rush County|     4| 241.240|  0.000|    80|  4824.799|  8.616|  16,581|
| |Spencer County|     3| 147.951|  0.000|   136|  6707.107| 154.996|  20,277|
| |Steuben County|     3| 86.720|  0.000|   211|  6099.324| 45.425|  34,594|
| |Wabash County|     3| 96.787|  0.000|   170|  5484.579| 41.480|  30,996|
| |Clinton County|     3| 92.595|  0.000|   440| 13580.666| 365.972|  32,399|
| |Huntington County|     3| 82.147|  0.000|   124|  3395.400| 23.471|  36,520|
| |Jefferson County|     2| 61.904|  0.000|   165|  5107.094| 70.748|  32,308|
| |Jasper County|     2| 59.591|  0.000|   245|  7299.923| 157.491|  33,562|
| |Fulton County|     2| 100.130|  0.000|   169|  8460.999| 164.500|  19,974|
| |Fountain County|     2| 122.354|  0.000|    74|  4527.101| 96.135|  16,346|
| |Carroll County|     2| 98.731|  0.000|   193|  9527.571| 338.507|  20,257|
| |Blackford County|     2| 170.097|  0.000|    65|  5528.151| 145.797|  11,758|
| |Adams County|     2| 55.902|  0.000|   102|  2850.994| 83.853|  35,777|
| |Wells County|     2| 70.681|  0.000|   171|  6043.257| 186.801|  28,296|
| |Miami County|     2| 56.313|  0.000|   274|  7714.833| 64.357|  35,516|
| |Washington County|     1| 35.668|  0.000|   142|  5064.917| 132.483|  28,036|
| |Warren County|     1| 120.992|  0.000|    23|  2782.819| 69.138|   8,265|
| |Brown County|     1| 66.260|  0.000|    74|  4903.260| 37.863|  15,092|
| |Owen County|     1| 48.079|  0.000|    91|  4375.210| 89.290|  20,799|
| |Pulaski County|     1| 80.952|  0.000|    83|  6719.016| 127.210|  12,353|
| |Sullivan County|     1| 48.382|  0.000|   134|  6483.139| 400.876|  20,669|
| |Parke County|     1| 59.042|  0.000|    52|  3070.201| 59.042|  16,937|
| |Vermillion County|     0|  0.000|  0.000|    55|  3548.845| 156.702|  15,498|
| |Union County|     0|  0.000|  0.000|    41|  5812.305| 182.267|   7,054|
| |Switzerland County|     0|  0.000|  0.000|    52|  4836.759| 119.590|  10,751|
| |Posey County|     0|  0.000|  0.000|   177|  6961.104| 106.748|  25,427|
| |Pike County|     0|  0.000|  0.000|    56|  4520.139| 115.310|  12,389|
| |Jay County|     0|  0.000|  0.000|    92|  4501.859| 69.905|  20,436|
| |Benton County|     0|  0.000|  0.000|    62|  7087.334| 32.661|   8,748|
| |Crawford County|     0|  0.000|  0.000|    45|  4254.515| 40.519|  10,577|
| |Martin County|     0|  0.000|  0.000|    45|  4388.103| 41.791|  10,255|
| |Knox County|     0|  0.000|  0.000|   159|  4344.975| 109.308|  36,594|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,327| 272.625| N/A|100,749| 11803.500| N/A|8,535,519|
| |Fairfax County|   536| 467.089|  0.747|16,535| 14409.184| 67.972|1,147,532|
| |Henrico County|   185| 559.220|  1.295| 3,904| 11801.051| 107.958| 330,818|
| |Prince William County|   176| 374.201|  0.911| 9,516| 20232.388| 160.372| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,091| 13050.895| 88.064| 236,842|
| |Loudoun County|   115| 278.088|  1.036| 5,306| 12830.743| 85.326| 413,538|
| |Chesterfield County|    80| 226.756|  2.025| 4,370| 12386.551| 110.544| 352,802|
| |Alexandria city|    60| 376.345|  0.896| 2,976| 18666.734| 118.280| 159,428|
| |Virginia Beach city|    54| 120.007|  2.222| 5,050| 11222.871| 197.789| 449,974|
| |Suffolk city|    50| 542.841|  1.551| 1,297| 14081.296| 286.930|  92,108|
| |Richmond County|    45| 4987.255| 31.665| 3,511| 389116.702| 3198.176|   9,023|
| |Shenandoah County|    44| 1008.804|  6.551|   717| 16438.921| 117.912|  43,616|
| |Chesapeake city|    37| 151.122|  4.668| 2,949| 12044.847| 193.716| 244,835|
| |Spotsylvania County|    35| 256.947|  1.049| 1,499| 11004.662| 148.924| 136,215|
| |Mecklenburg County|    32| 1046.196|  0.000|   446| 14581.358| 639.861|  30,587|
| |Norfolk city|    32| 131.827|  3.531| 3,703| 15254.880| 210.688| 242,742|
| |Hanover County|    32| 296.940|  1.326|   653|  6059.425| 74.235| 107,766|
| |Harrisonburg city|    31| 584.729|  5.389| 1,079| 20352.346| 64.671|  53,016|
| |Northampton County|    29| 2476.516| 12.200|   296| 25277.541| 24.399|  11,710|
| |Portsmouth city|    25| 264.836|  1.513| 1,788| 18941.079| 375.311|  94,398|
| |Page County|    25| 1045.938|  5.977|   346| 14475.776| 77.698|  23,902|
| |Galax city|    24| 3781.314| 45.016|   347| 54671.498| 202.570|   6,347|
| |Manassas city|    22| 535.475|  6.954| 1,662| 40452.720| 173.856|  41,085|
| |Colonial Heights city|    21| 1208.981|  0.000|   197| 11341.393| 98.692|  17,370|
| |Roanoke County|    19| 201.728|  1.517| 1,511| 16042.724| 221.446|  94,186|
| |Rockingham County|    19| 231.854|  3.487|   946| 11543.906| 66.244|  81,948|
| |Petersburg city|    19| 606.138| 27.345|   520| 16589.038| 214.199|  31,346|
| |Newport News city|    18| 100.432|  1.594| 1,847| 10305.482| 140.287| 179,225|
| |James City County|    16| 209.087|  0.000|   617|  8062.935| 102.677|  76,523|
| |Albemarle County|    16| 146.346|  5.227|   842|  7701.454| 87.546| 109,330|
| |Accomack County|    16| 495.111|  4.421| 1,102| 34100.755| 97.254|  32,316|
| |Charlottesville city|    15| 317.353|  6.045|   543| 11488.173| 145.076|  47,266|
| |Emporia city|    15| 2805.836|  0.000|   178| 33295.922| 293.945|   5,346|
| |Nottoway County|    13| 853.466| 37.515|   182| 11948.529| 56.273|  15,232|
| |Southampton County|    13| 737.338|  0.000|   267| 15143.781| 218.771|  17,631|
| |Carroll County|    13| 436.373|  0.000|   334| 11211.440| 95.906|  29,791|
| |Culpeper County|    12| 228.115|  0.000| 1,008| 19161.677| 138.499|  52,605|
| |Greensville County|    11| 970.360| 12.602|   495| 43666.196| 730.920|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   410| 17980.879| 338.316|  22,802|
| |Fauquier County|     9| 126.365|  2.006|   620|  8705.175| 80.232|  71,222|
| |Fluvanna County|     9| 330.033|  5.239|   193|  7077.374| 94.295|  27,270|
| |Isle of Wight County|     9| 242.529|  0.000|   387| 10428.737| 130.889|  37,109|
| |Frederick County|     9| 100.769|  0.000|   681|  7624.870| 17.595|  89,313|
| |Sussex County|     9| 806.524|  0.000|   307| 27511.426| 358.455|  11,159|
| |Stafford County|     9| 58.869|  1.869| 1,385|  9059.274| 95.312| 152,882|
| |Buckingham County|     8| 466.527| 16.662|   605| 35281.082| 74.978|  17,148|
| |Dinwiddie County|     7| 245.235|  5.005|   221|  7742.433| 60.058|  28,544|
| |Franklin County|     7| 124.906|  0.000|   357|  6370.222| 124.906|  56,042|
| |Danville city|     7| 174.808|  0.000|   411| 10263.710| 239.023|  40,044|
| |Hampton city|     7| 52.041|  2.124| 1,245|  9255.817| 185.860| 134,510|
| |Manassas Park city|     7| 400.503|  0.000|   515| 29465.614| 122.603|  17,478|
| |Henry County|     7| 138.458|  2.826|   591| 11689.776| 226.053|  50,557|
| |Bedford County|     7| 88.611|  1.808|   361|  4569.794| 97.653|  78,997|
| |Botetourt County|     7| 209.462|  0.000|   215|  6433.466| 98.319|  33,419|
| |Goochland County|     7| 294.700|  0.000|   164|  6904.391| 78.186|  23,753|
| |Williamsburg city|     6| 401.230|  0.000|   128|  8559.583| 133.743|  14,954|
| |Warren County|     6| 149.388|  0.000|   355|  8838.761| 24.898|  40,164|
| |Falls Church city|     6| 410.481|  0.000|    61|  4173.223| 19.547|  14,617|
| |Grayson County|     5| 321.543|  9.187|   157| 10096.463| 211.300|  15,550|
| |Caroline County|     5| 162.734|  4.650|   214|  6965.012| 106.939|  30,725|
| |Charles City County|     5| 718.081|  0.000|    52|  7468.045| 41.033|   6,963|
| |Lynchburg city|     5| 60.851|  5.216|   627|  7630.708| 274.699|  82,168|
| |Hopewell city|     5| 221.936|  0.000|   272| 12073.328| 88.774|  22,529|
| |Washington County|     5| 93.041|  2.658|   233|  4335.690| 138.232|  53,740|
| |York County|     4| 58.582|  2.092|   373|  5462.800| 115.072|  68,280|
| |Fredericksburg city|     4| 137.760|  9.840|   406| 13982.642| 186.960|  29,036|
| |King George County|     4| 149.054|  0.000|   145|  5403.190| 111.790|  26,836|
| |Powhatan County|     4| 134.898|  0.000|   147|  4957.507| 91.538|  29,652|
| |Patrick County|     4| 227.169|  8.113|   158|  8973.194| 348.867|  17,608|
| |Augusta County|     4| 52.939|  0.000|   280|  3705.762| 51.049|  75,558|
| |Alleghany County|     4| 269.179|  9.614|    62|  4172.275| 57.681|  14,860|
| |Winchester city|     4| 142.460|  0.000|   399| 14210.414| 35.615|  28,078|
| |Montgomery County|     3| 30.446|  0.000|   305|  3095.347| 23.197|  98,535|
| |Martinsville city|     3| 238.968|  0.000|   212| 16887.048| 466.556|  12,554|
| |Wise County|     3| 80.250|  0.000|   141|  3771.768| 179.608|  37,383|
| |Westmoreland County|     3| 166.528|  7.930|   211| 11712.462| 126.878|  18,015|
| |Wythe County|     3| 104.588|  0.000|   115|  4009.204| 34.863|  28,684|
| |Waynesboro city|     3| 132.567|  0.000|   174|  7688.909| 44.189|  22,630|
| |Salem city|     3| 118.572|  0.000|   161|  6363.385| 124.219|  25,301|
| |Smyth County|     3| 99.655|  0.000|   150|  4982.727| 128.127|  30,104|
| |Scott County|     3| 139.108|  0.000|   102|  4729.667| 278.216|  21,566|
| |Orange County|     3| 80.969|  0.000|   231|  6234.650| 69.402|  37,051|
| |Pulaski County|     3| 88.165|  0.000|    89|  2615.570| 58.777|  34,027|
| |Prince George County|     2| 52.147|  0.000|   384| 10012.255| 160.166|  38,353|
| |Rappahannock County|     2| 271.370|  0.000|    43|  5834.464| 58.151|   7,370|
| |Russell County|     2| 75.228|  5.373|   128|  4814.564| 311.657|  26,586|
| |Surry County|     2| 311.429|  0.000|    52|  8097.166| 311.429|   6,422|
| |Pittsylvania County|     2| 33.138|  0.000|   493|  8168.473| 279.304|  60,354|
| |Amelia County|     2| 152.149| 10.868|    79|  6009.890| 65.207|  13,145|
| |Northumberland County|     2| 165.358|  0.000|    74|  6118.231| 94.490|  12,095|
| |Brunswick County|     2| 123.221|  8.801|   230| 14170.415| 158.427|  16,231|
| |Louisa County|     2| 53.204|  0.000|   183|  4868.187| 60.805|  37,591|
| |King William County|     2| 116.632|  0.000|    90|  5248.425| 108.301|  17,148|
| |Greene County|     2| 100.913|  0.000|   166|  8375.801| 136.954|  19,819|
| |Gloucester County|     2| 53.550|  0.000|   161|  4310.806| 61.200|  37,348|
| |Floyd County|     2| 126.992|  9.071|    75|  4762.207| 326.551|  15,749|
| |Campbell County|     2| 36.440|  0.000|   213|  3880.842| 145.759|  54,885|
| |Buena Vista city|     1| 154.369| 22.053|    50|  7718.432| 44.105|   6,478|
| |Middlesex County|     1| 94.500|  0.000|    42|  3969.004| 189.000|  10,582|
| |Lee County|     1| 42.693|  0.000|   121|  5165.863| 128.079|  23,423|
| |Dickenson County|     1| 69.842|  9.977|    43|  3003.213| 139.684|  14,318|
| |New Kent County|     1| 43.307|  0.000|   129|  5586.592| 61.867|  23,091|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 122.013|   7,025|
| |Halifax County|     1| 29.489|  0.000|   156|  4600.277| 63.191|  33,911|
| |Madison County|     1| 75.409|  0.000|    69|  5203.228| 75.409|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    62|  5083.634| 81.994|  12,196|
| |Essex County|     1| 91.299|  0.000|   103|  9403.816| 260.855|  10,953|
| |Rockbridge County|     1| 44.301|  6.329|    69|  3056.749| 12.657|  22,573|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 27.842|   5,131|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Bland County|     0|  0.000|  0.000|    19|  3025.478| 272.975|   6,280|
| |Buchanan County|     0|  0.000|  0.000|    80|  3808.798| 54.411|  21,004|
| |Cumberland County|     0|  0.000|  0.000|    76|  7652.034| 115.068|   9,932|
| |Charlotte County|     0|  0.000|  0.000|    53|  4461.279| 48.100|  11,880|
| |Clarke County|     0|  0.000|  0.000|    71|  4856.693| 19.544|  14,619|
| |Radford city|     0|  0.000|  0.000|    54|  2959.066| 219.190|  18,249|
| |Giles County|     0|  0.000|  0.000|    24|  1435.407|  8.544|  16,720|
| |Staunton city|     0|  0.000|  0.000|   152|  6096.583| 51.569|  24,932|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Bristol city|     0|  0.000|  0.000|    80|  4772.700| 127.840|  16,762|
| |Mathews County|     0|  0.000|  0.000|    18|  2037.582| 64.685|   8,834|
| |Amherst County|     0|  0.000|  0.000|   176|  5568.739| 262.165|  31,605|
| |Appomattox County|     0|  0.000|  0.000|    87|  5467.915| 143.656|  15,911|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910|  0.000|   7,446|
| |Nelson County|     0|  0.000|  0.000|    49|  3281.983| 143.527|  14,930|
| |Lancaster County|     0|  0.000|  0.000|    40|  3772.517| 121.259|  10,603|
| |Tazewell County|     0|  0.000|  0.000|   119|  2931.395| 73.901|  40,595|
| |Norton city|     0|  0.000|  0.000|    19|  4772.670| 215.308|   3,981|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 195.695|   2,190|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 58.209|  12,271|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,199| 209.667| N/A|137,562| 13116.028| N/A|10,488,084|
| |Mecklenburg County|   232| 208.942|  1.287|22,315| 20097.158| 162.239|1,110,356|
| |Wake County|   170| 152.911|  4.754|12,110| 10892.629| 103.439|1,111,761|
| |Guilford County|   156| 290.409|  2.393| 5,670| 10555.239| 110.632| 537,174|
| |Durham County|    80| 248.843|  0.444| 6,200| 19285.323| 125.755| 321,488|
| |Henderson County|    54| 459.899|  0.000| 1,490| 12689.815| 107.067| 117,417|
| |Robeson County|    53| 405.742|  2.187| 2,817| 21565.550| 173.889| 130,625|
| |Gaston County|    52| 231.596|  6.999| 3,339| 14871.130| 193.421| 224,529|
| |Forsyth County|    52| 136.021|  1.121| 5,286| 13827.018| 123.689| 382,295|
| |Chatham County|    52| 698.268|  3.837| 1,305| 17523.835| 115.099|  74,470|
| |Cumberland County|    51| 152.008|  0.426| 3,162|  9424.486| 146.898| 335,509|
| |Cabarrus County|    50| 230.997|  0.660| 2,630| 12150.444| 83.159| 216,453|
| |Rowan County|    48| 337.819|  0.000| 2,205| 15518.552| 173.936| 142,088|
| |Columbus County|    48| 864.740|  5.147|   907| 16339.987| 190.449|  55,508|
| |Duplin County|    48| 817.146| 12.160| 2,015| 34303.127| 184.831|  58,741|
| |Orange County|    47| 316.549|  1.924| 1,353|  9112.584| 57.729| 148,476|
| |Buncombe County|    47| 179.945|  0.547| 1,898|  7266.713| 100.091| 261,191|
| |Johnston County|    46| 219.739|  1.365| 3,315| 15835.559| 156.957| 209,339|
| |Union County|    43| 179.272|  1.191| 3,109| 12961.782| 170.338| 239,859|
| |Wayne County|    42| 341.100|  5.801| 2,424| 19686.350| 111.380| 123,131|
| |Alamance County|    41| 241.875|  0.000| 2,472| 14583.296| 175.296| 169,509|
| |Vance County|    41| 920.624|  3.208|   777| 17446.952| 125.102|  44,535|
| |Harnett County|    39| 286.815|  3.152| 1,303|  9582.573| 152.338| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,180| 15173.979| 108.386| 143,667|
| |Wilson County|    35| 427.868|  0.000| 1,514| 18508.331| 136.219|  81,801|
| |Catawba County|    29| 181.760|  0.000| 2,123| 13306.090| 135.201| 159,551|
| |Burke County|    28| 309.444|  0.000| 1,763| 19483.892| 198.928|  90,485|
| |Granville County|    27| 446.702|  4.727| 1,247| 20631.008| 146.537|  60,443|
| |Franklin County|    26| 373.108|  2.050|   871| 12499.103| 151.703|  69,685|
| |Stanly County|    26| 413.973| 13.647| 1,075| 17116.199| 370.756|  62,806|
| |Brunswick County|    21| 147.038|  4.001| 1,259|  8815.292| 61.016| 142,820|
| |New Hanover County|    20| 85.298|  0.000| 2,630| 11216.643| 110.278| 234,473|
| |Moore County|    20| 198.255|  0.000| 1,018| 10091.197| 154.356| 100,880|
| |Pasquotank County|    20| 502.210| 10.762|   402| 10094.415| 154.250|  39,824|
| |Cleveland County|    20| 204.192|  4.376| 1,193| 12180.057| 227.528|  97,947|
| |Davidson County|    18| 107.393|  0.000| 1,793| 10697.516| 119.325| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,905| 10478.202| 105.293| 181,806|
| |Caldwell County|    16| 194.699|  3.477| 1,215| 14784.979| 133.856|  82,178|
| |Northampton County|    16| 821.229|  0.000|   351| 18015.706| 161.313|  19,483|
| |Montgomery County|    14| 515.217|  0.000|   647| 23810.400| 15.772|  27,173|
| |Sampson County|    14| 220.365|  4.497| 1,511| 23783.665| 188.884|  63,531|
| |McDowell County|    14| 305.971|  3.122|   683| 14927.004| 231.039|  45,756|
| |Rutherford County|    14| 208.865|  0.000|   752| 11219.025| 134.270|  67,029|
| |Edgecombe County|    13| 252.565|  5.551|   656| 12744.793| 185.954|  51,472|
| |Haywood County|    12| 192.564| 13.755|   435|  6980.439| 199.441|  62,317|
| |Lenoir County|    12| 214.481|  0.000|   599| 10706.179| 160.861|  55,949|
| |Nash County|    12| 127.256|  1.515| 1,194| 12661.986| 198.459|  94,298|
| |Craven County|    12| 117.487|  2.797|   753|  7372.306| 111.892| 102,139|
| |Wilkes County|    11| 160.791|  2.088|   843| 12322.400| 223.436|  68,412|
| |Hertford County|    11| 464.586|  0.000|   349| 14740.043| 325.813|  23,677|
| |Pitt County|    11| 60.860|  0.000| 2,036| 11264.676| 190.485| 180,742|
| |Lee County|    11| 178.054|  2.312| 1,296| 20978.002| 182.679|  61,779|
| |Surry County|    10| 139.309|  3.980|   956| 13317.916| 167.170|  71,783|
| |Onslow County|    10| 50.521|  0.000| 1,079|  5451.202| 104.650| 197,938|
| |Richmond County|     9| 200.763|  3.187|   521| 11621.941| 111.535|  44,829|
| |Lincoln County|     9| 104.516|  9.954|   850|  9870.980| 164.240|  86,111|
| |Hoke County|     9| 162.943|  2.586|   720| 13035.449| 118.974|  55,234|
| |Rockingham County|     8| 87.902|  1.570|   567|  6230.085| 114.587|  91,010|
| |Bladen County|     7| 213.923|  0.000|   625| 19100.299| 157.168|  32,722|
| |Warren County|     7| 354.772|  0.000|   258| 13075.870| 108.604|  19,731|
| |Davie County|     7| 163.376|  3.334|   431| 10059.282| 150.039|  42,846|
| |Martin County|     6| 267.380|  0.000|   261| 11631.016| 108.225|  22,440|
| |Carteret County|     6| 86.364|  0.000|   376|  5412.175| 90.477|  69,473|
| |Yadkin County|     6| 159.291|  0.000|   542| 14389.253| 128.950|  37,667|
| |Halifax County|     6| 119.976|  0.000|   705| 14097.181| 157.111|  50,010|
| |Jackson County|     5| 113.797|  6.503|   451| 10264.464| 126.802|  43,938|
| |Polk County|     5| 241.266|  0.000|   164|  7913.530| 165.440|  20,724|
| |Bertie County|     5| 263.894|  0.000|   275| 14514.171| 196.036|  18,947|
| |Jones County|     4| 424.674| 15.167|    93|  9873.660| 227.504|   9,419|
| |Washington County|     4| 345.423| 12.337|   133| 11485.320| 148.038|  11,580|
| |Cherokee County|     4| 139.801|  4.993|   290| 10135.607| 124.823|  28,612|
| |Macon County|     3| 83.663|  0.000|   470| 13107.256| 39.840|  35,858|
| |Pender County|     3| 47.574|  0.000|   659| 10450.365| 74.759|  63,060|
| |Stokes County|     3| 65.802|  0.000|   296|  6492.509| 94.004|  45,591|
| |Greene County|     3| 142.389|  0.000|   331| 15710.285| 135.609|  21,069|
| |Anson County|     3| 122.719|  5.844|   328| 13417.328| 140.251|  24,446|
| |Mitchell County|     2| 133.654|  0.000|   120|  8019.246| 38.187|  14,964|
| |Swain County|     2| 140.144|  0.000|   119|  8338.589| 140.144|  14,271|
| |Scotland County|     2| 57.433|  0.000|   365| 10481.578| 295.371|  34,823|
| |Person County|     2| 50.646|  0.000|   223|  5646.999| 79.586|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    87|  6462.156| 169.777|  13,463|
| |Gates County|     2| 172.980|  0.000|    46|  3978.550| 12.356|  11,562|
| |Dare County|     2| 54.041|  0.000|   210|  5674.295| 30.881|  37,009|
| |Caswell County|     2| 88.480|  0.000|   196|  8671.032| 63.200|  22,604|
| |Alexander County|     2| 53.338|  0.000|   303|  8080.646| 30.479|  37,497|
| |Camden County|     2| 184.043|  0.000|    73|  6717.585| 131.460|  10,867|
| |Beaufort County|     2| 42.559|  0.000|   428|  9107.546| 167.195|  46,994|
| |Pamlico County|     1| 78.579|  0.000|    72|  5657.709| 78.579|  12,726|
| |Transylvania County|     1| 29.082|  0.000|   145|  4216.955| 54.010|  34,385|
| |Tyrrell County|     1| 249.004|  0.000|    98| 24402.390| 213.432|   4,016|
| |Ashe County|     1| 36.761|  0.000|   158|  5808.183| 168.049|  27,203|
| |Chowan County|     1| 71.721|  0.000|   157| 11260.131| 133.195|  13,943|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984|  0.000|  11,231|
| |Currituck County|     0|  0.000|  0.000|    73|  2629.399| 15.437|  27,763|
| |Graham County|     0|  0.000|  0.000|    39|  4620.306| 203.090|   8,441|
| |Alleghany County|     0|  0.000|  0.000|   169| 15174.643| 51.309|  11,137|
| |Avery County|     0|  0.000|  0.000|   109|  6208.350| 81.368|  17,557|
| |Hyde County|     0|  0.000|  0.000|    45|  9114.847| 231.488|   4,937|
| |Madison County|     0|  0.000|  0.000|    45|  2068.490| 32.833|  21,755|
| |Watauga County|     0|  0.000|  0.000|   316|  5625.078| 83.918|  56,177|
| |Yancey County|     0|  0.000|  0.000|   114|  6309.148| 102.781|  18,069|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,048| 397.769| N/A|101,159| 19647.430| N/A|5,148,714|
| |Greenville County|   208| 397.294|  5.184|11,001| 21012.641| 189.642| 523,542|
| |Charleston County|   196| 476.415|  8.681|12,377| 30084.637| 230.221| 411,406|
| |Horry County|   156| 440.577| 10.490| 8,625| 24358.833| 181.960| 354,081|
| |Richland County|   153| 368.002|  4.123| 8,836| 21252.697| 273.510| 415,759|
| |Florence County|   116| 838.799| 17.561| 3,480| 25163.963| 401.838| 138,293|
| |Lexington County|   111| 371.548|  3.347| 4,980| 16669.456| 141.064| 298,750|
| |Spartanburg County|   103| 322.091|  7.148| 4,100| 12821.114| 137.146| 319,785|
| |Berkeley County|    67| 293.980|  5.015| 4,186| 18367.141| 191.808| 227,907|
| |Orangeburg County|    65| 754.279| 11.604| 2,441| 28326.081| 348.129|  86,175|
| |Anderson County|    63| 311.022| 10.579| 2,350| 11601.615| 174.201| 202,558|
| |Beaufort County|    56| 291.481|  5.205| 4,131| 21501.962| 333.865| 192,122|
| |Clarendon County|    52| 1540.969|  8.467|   846| 25070.381| 254.006|  33,745|
| |Sumter County|    51| 477.882|  8.032| 2,539| 23791.006| 298.509| 106,721|
| |Dorchester County|    47| 288.682|  6.142| 3,135| 19255.692| 259.726| 162,809|
| |Laurens County|    46| 681.552| 25.399| 1,340| 19853.911| 220.129|  67,493|
| |Aiken County|    38| 222.389|  7.524| 1,883| 11019.945| 241.618| 170,872|
| |Darlington County|    36| 540.394|  6.433| 1,312| 19694.377| 383.852|  66,618|
| |Colleton County|    34| 902.407| 11.375|   825| 21896.648| 227.498|  37,677|
| |Williamsburg County|    31| 1020.811| 18.817| 1,020| 33587.987| 381.040|  30,368|
| |York County|    29| 103.211|  0.508| 3,590| 12776.756| 174.899| 280,979|
| |Lee County|    29| 1723.318| 16.979|   566| 33634.419| 339.570|  16,828|
| |Cherokee County|    28| 488.656|  7.479|   641| 11186.736| 199.452|  57,300|
| |Pickens County|    27| 212.793|  4.504| 1,863| 14682.702| 130.603| 126,884|
| |Lancaster County|    26| 265.274|  7.288| 1,227| 12518.875| 206.972|  98,012|
| |Kershaw County|    25| 375.652|  4.293| 1,407| 21141.681| 240.417|  66,551|
| |Dillon County|    25| 820.237|  9.374|   644| 21129.302| 304.659|  30,479|
| |Fairfield County|    23| 1029.221|  0.000|   573| 25641.026| 217.351|  22,347|
| |Bamberg County|    22| 1564.055| 50.781|   479| 34053.747| 335.155|  14,066|
| |Chesterfield County|    21| 460.022|  6.259|   777| 17020.811| 219.058|  45,650|
| |Georgetown County|    19| 303.127|  0.000| 1,461| 23308.870| 350.989|  62,680|
| |Greenwood County|    18| 254.198|  6.052| 1,416| 19996.893| 284.459|  70,811|
| |Jasper County|    16| 532.039| 14.251|   597| 19851.694| 413.280|  30,073|
| |Chester County|    14| 434.189|  8.861|   671| 20810.073| 412.037|  32,244|
| |Marion County|    13| 424.047|  4.660|   558| 18201.390| 163.095|  30,657|
| |Calhoun County|    11| 755.858|  9.816|   383| 26317.598| 451.551|  14,553|
| |Hampton County|    11| 572.261| 29.728|   441| 22942.462| 364.166|  19,222|
| |Newberry County|    10| 260.146|  3.716|   854| 22216.441| 267.578|  38,440|
| |Oconee County|    10| 125.713|  5.388|   839| 10547.356| 150.856|  79,546|
| |Abbeville County|     9| 366.943| 11.649|   335| 13658.417| 215.506|  24,527|
| |Saluda County|     8| 390.759|  0.000|   459| 22419.772| 265.158|  20,473|
| |Edgefield County|     7| 256.787|  5.241|   332| 12179.017| 225.343|  27,260|
| |Barnwell County|     5| 239.624|  6.846|   420| 20128.439| 349.167|  20,866|
| |Union County|     4| 146.434| 10.460|   364| 13325.524| 151.664|  27,316|
| |Marlboro County|     4| 153.151|  0.000|   507| 19411.900| 350.060|  26,118|
| |Allendale County|     3| 345.304|  0.000|   228| 26243.094| 575.506|   8,688|
| |McCormick County|     2| 211.349|  0.000|   120| 12680.968| 211.349|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,912| 642.441| N/A|67,649| 22730.381| N/A|2,976,149|
| |Hinds County|   118| 508.972|  7.394| 5,656| 24396.135| 238.465| 231,840|
| |Neshoba County|    92| 3159.558| 19.625| 1,286| 44165.121| 436.647|  29,118|
| |Lauderdale County|    92| 1241.147|  7.709| 1,411| 19035.413| 158.034|  74,125|
| |Madison County|    68| 639.868| 16.131| 2,443| 22988.181| 196.262| 106,272|
| |Leflore County|    65| 2306.355| 30.413|   947| 33601.817| 542.374|  28,183|
| |Jones County|    59| 866.398|  4.196| 1,916| 28135.922| 297.890|  68,098|
| |Forrest County|    56| 747.693|  5.722| 1,820| 24300.039| 343.329|  74,897|
| |Monroe County|    55| 1560.195| 20.262|   801| 22722.115| 401.193|  35,252|
| |Holmes County|    49| 2880.658| 16.797|   900| 52910.053| 445.116|  17,010|
| |Jackson County|    43| 299.407|  8.952| 2,288| 15931.262| 292.444| 143,617|
| |Washington County|    42| 956.524| 32.535| 1,689| 38465.918| 640.936|  43,909|
| |Lincoln County|    41| 1200.480|  4.183|   832| 24360.964| 363.909|  34,153|
| |Lee County|    41| 479.891| 18.393| 1,479| 17311.204| 401.303|  85,436|
| |Oktibbeha County|    39| 786.496| 11.524| 1,127| 22727.731| 210.309|  49,587|
| |Pearl River County|    39| 702.260|  7.717|   554|  9975.691| 177.494|  55,535|
| |Lowndes County|    38| 648.519| 14.628| 1,085| 18516.938| 234.052|  58,595|
| |Harrison County|    36| 173.010|  2.746| 2,530| 12158.785| 259.516| 208,080|
| |Pike County|    36| 916.310| 14.545|   938| 23874.975| 385.432|  39,288|
| |Rankin County|    35| 225.412|  6.440| 2,292| 14761.288| 134.327| 155,271|
| |Bolivar County|    34| 1110.095|  9.329| 1,118| 36502.547| 792.925|  30,628|
| |Warren County|    33| 727.177| 18.888| 1,095| 24129.041| 412.382|  45,381|
| |DeSoto County|    31| 167.617|  3.090| 3,680| 19897.807| 273.440| 184,945|
| |Simpson County|    30| 1125.366| 16.077|   803| 30122.290| 487.658|  26,658|
| |Tate County|    29| 1023.975| 30.265|   736| 25987.783| 433.802|  28,321|
| |Copiah County|    28| 997.684| 20.361|   957| 34099.412| 203.609|  28,065|
| |Clarke County|    26| 1672.994|  9.192|   326| 20976.771| 238.999|  15,541|
| |Adams County|    25| 814.518|  0.000|   629| 20493.272| 209.447|  30,693|
| |Attala County|    25| 1375.592|  7.861|   523| 28777.374| 196.513|  18,174|
| |Sunflower County|    25| 995.619| 17.068| 1,054| 41975.309| 830.631|  25,110|
| |Leake County|    25| 1097.165|  0.000|   790| 34670.412| 137.929|  22,786|
| |Wayne County|    21| 1040.480|  0.000|   774| 38349.106| 290.202|  20,183|
| |Grenada County|    21| 1011.658|  6.882|   849| 40899.894| 247.753|  20,758|
| |Marion County|    20| 813.901| 11.627|   684| 27835.429| 482.527|  24,573|
| |Scott County|    20| 711.136| 15.239| 1,003| 35663.490| 243.818|  28,124|
| |Walthall County|    20| 1399.972| 20.000|   501| 35069.299| 479.990|  14,286|
| |Chickasaw County|    19| 1110.916|  0.000|   470| 27480.559| 267.288|  17,103|
| |Lafayette County|    17| 314.704| 15.867|   983| 18197.301| 269.746|  54,019|
| |Union County|    16| 555.266| 14.873|   643| 22314.767| 555.266|  28,815|
| |Winston County|    16| 891.117|  7.956|   623| 34697.856| 413.733|  17,955|
| |Panola County|    14| 409.453| 12.534| 1,062| 31059.897| 626.713|  34,192|
| |Lamar County|    14| 221.019|  4.511| 1,226| 19354.941| 236.806|  63,343|
| |Kemper County|    14| 1437.077|  0.000|   234| 24019.708| 161.305|   9,742|
| |Hancock County|    14| 293.920|  0.000|   395|  8292.744| 176.952|  47,632|
| |Clay County|    14| 724.788|  7.396|   397| 20552.910| 199.686|  19,316|
| |Tippah County|    13| 590.506|  6.489|   367| 16670.452| 356.900|  22,015|
| |Wilkinson County|    13| 1506.373| 16.554|   211| 24449.594| 397.285|   8,630|
| |Smith County|    13| 816.788|  0.000|   406| 25508.922| 233.368|  15,916|
| |Claiborne County|    13| 1446.373|  0.000|   409| 45505.118| 143.048|   8,988|
| |Covington County|    13| 697.575| 15.331|   621| 33322.601| 252.967|  18,636|
| |Coahoma County|    13| 587.597| 19.371|   772| 34894.233| 703.825|  22,124|
| |Greene County|    12| 883.262| 10.515|   255| 18769.321| 304.936|  13,586|
| |Yazoo County|    12| 404.176|  4.812|   833| 28056.585| 226.146|  29,690|
| |Webster County|    12| 1238.518|  0.000|   235| 24254.309| 530.793|   9,689|
| |Noxubee County|    12| 1151.963| 27.428|   459| 44062.590| 548.554|  10,417|
| |Humphreys County|    11| 1364.087|  0.000|   294| 36458.333| 407.455|   8,064|
| |Newton County|    11| 523.361|  0.000|   543| 25834.999| 183.516|  21,018|
| |Carroll County|    11| 1105.861|  0.000|   261| 26239.067| 229.789|   9,947|
| |Tallahatchie County|    11| 796.582| 10.345|   530| 38380.766| 382.773|  13,809|
| |Yalobusha County|    10| 825.900|  0.000|   315| 26015.857| 35.396|  12,108|
| |Itawamba County|    10| 427.533|  0.000|   375| 16032.493| 415.318|  23,390|
| |Prentiss County|    10| 397.994| 22.743|   417| 16596.354| 426.422|  25,126|
| |Jasper County|     9| 549.350|  8.720|   388| 23683.086| 104.638|  16,383|
| |Calhoun County|     9| 626.697|  9.948|   420| 29245.874| 417.798|  14,361|
| |Marshall County|     9| 255.001|  4.048|   701| 19861.733| 526.192|  35,294|
| |Lawrence County|     8| 635.627| 34.051|   322| 25583.982| 102.154|  12,586|
| |Pontotoc County|     8| 248.648|  4.440|   830| 25797.228| 412.933|  32,174|
| |Perry County|     7| 584.649|  0.000|   243| 20295.665| 250.564|  11,973|
| |Jefferson County|     7| 1001.431| 20.437|   195| 27896.996| 40.875|   6,990|
| |Tunica County|     7| 726.744| 14.832|   351| 36441.030| 1082.701|   9,632|
| |Tishomingo County|     6| 309.550| 14.740|   421| 21720.064| 744.393|  19,383|
| |Amite County|     6| 487.924| 11.617|   235| 19110.352| 290.431|  12,297|
| |Jefferson Davis County|     6| 539.180|  0.000|   233| 20938.174| 397.967|  11,128|
| |Sharkey County|     5| 1157.140| 132.245|   199| 46054.154| 628.161|   4,321|
| |Stone County|     5| 272.688| 15.582|   205| 11180.192| 412.927|  18,336|
| |Alcorn County|     5| 135.307|  3.866|   434| 11744.649| 297.675|  36,953|
| |Montgomery County|     5| 511.509| 29.229|   326| 33350.384| 482.280|   9,775|
| |George County|     5| 204.082|  0.000|   589| 24040.816| 244.898|  24,500|
| |Choctaw County|     4| 487.211|  0.000|   135| 16443.362| 139.203|   8,210|
| |Franklin County|     2| 259.302|  0.000|   131| 16984.312| 277.824|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    26| 19593.067| 538.271|   1,327|
| |Benton County|     1| 121.080| 17.297|   143| 17314.445| 311.349|   8,259|
| |Quitman County|     1| 147.232|  0.000|   270| 39752.650| 946.492|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,862| 323.335| N/A|51,020|  8859.583| N/A|5,758,736|
| |Denver County|   415| 570.673| N/A|10,263| 14112.823| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.218| 7,340| 11178.970| 68.971| 656,590|
| |Jefferson County|   228| 391.160|  0.245| 4,210|  7222.744| 58.576| 582,881|
| |Adams County|   176| 340.149|  1.380| 6,529| 12618.351| 114.303| 517,421|
| |Weld County|   145| 446.852|  1.761| 3,723| 11473.318| 75.283| 324,492|
| |El Paso County|   138| 191.559|  0.397| 5,134|  7126.567| 100.936| 720,403|
| |Boulder County|    74| 226.857|  0.000| 2,059|  6312.156| 57.809| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,744|  4966.482| 37.021| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   686| 23599.835| 44.231|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,575|  4413.013| 63.243| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   699|  4150.240| 71.249| 168,424|
| |Broomfield County|    32| 454.126| N/A|   475|  6740.935| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   303| 14885.046| 112.287|  20,356|
| |Montrose County|    13| 304.037|  0.000|   310|  7250.105| 90.209|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,124| 20389.283| 142.528|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   230| 14168.669| 52.802|  16,233|
| |Routt County|     8| 312.037| 11.144|   125|  4875.575| 94.725|  25,638|
| |Gunnison County|     6| 343.603|  0.000|   273| 15633.948| 130.896|  17,462|
| |Otero County|     6| 328.263|  0.000|    71|  3884.451| 78.158|  18,278|
| |Logan County|     5| 223.125|  0.000|   651| 29050.828| 19.125|  22,409|
| |Summit County|     4| 128.986|  0.000|   333| 10738.125| 46.067|  31,011|
| |Garfield County|     4| 66.599|  0.000|   768| 12787.000| 111.791|  60,061|
| |Mesa County|     4| 25.939|  0.926|   316|  2049.154| 41.687| 154,210|
| |Montezuma County|     4| 152.771|  0.000|   112|  4277.585| 21.824|  26,183|
| |Kit Carson County|     3| 422.714|  0.000|    56|  7890.658| 261.680|   7,097|
| |Teller County|     3| 118.166|  0.000|   133|  5238.695| 112.539|  25,388|
| |Pitkin County|     2| 112.568|  0.000|   186| 10468.847| 112.568|  17,767|
| |Rio Grande County|     2| 177.510|  0.000|    89|  7899.175| 25.359|  11,267|
| |La Plata County|     2| 35.574|  0.000|   219|  3895.342| 53.361|  56,221|
| |Elbert County|     2| 74.825|  0.000|   105|  3928.318| 96.204|  26,729|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Crowley County|     1| 164.989|  0.000|    72| 11879.228|  0.000|   6,061|
| |Delta County|     1| 32.090|  0.000|   125|  4011.296| 68.765|  31,162|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 44.183|   9,700|
| |Grand County|     1| 63.557|  0.000|    46|  2923.605| 18.159|  15,734|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 41.426|   6,897|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Ouray County|     1| 201.939|  0.000|    14|  2827.141| 57.697|   4,952|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 75.284|  13,283|
| |Rio Blanco County|     0|  0.000|  0.000|    16|  2530.044| 180.717|   6,324|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Washington County|     0|  0.000|  0.000|    49|  9983.700| 58.214|   4,908|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 50.117|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    17|  1171.929| 19.696|  14,506|
| |Prowers County|     0|  0.000|  0.000|    53|  4354.256| 58.683|  12,172|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Gilpin County|     0|  0.000|  0.000|    16|  2562.870|  0.000|   6,243|
| |Fremont County|     0|  0.000|  0.000|   125|  2612.931| 38.821|  47,839|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |San Miguel County|     0|  0.000|  0.000|    89| 10881.526| 227.062|   8,179|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684| 105.469|   8,127|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053| 14.259|  10,019|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Costilla County|     0|  0.000|  0.000|    23|  5917.160| 36.753|   3,887|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481| 28.188|   5,068|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 102.462|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    36|  2566.113| 30.549|  14,029|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,733| 353.444| N/A|99,390| 20270.498| N/A|4,903,185|
| |Jefferson County|   244| 370.498|  4.121|13,258| 20131.405| 303.470| 658,573|
| |Mobile County|   207| 500.956|  5.532|10,517| 25451.949| 494.733| 413,210|
| |Montgomery County|   149| 657.877|  3.785| 6,835| 30178.466| 369.622| 226,486|
| |Tallapoosa County|    79| 1957.044|  3.539|   865| 21428.394| 180.487|  40,367|
| |Tuscaloosa County|    76| 363.020|  8.871| 4,230| 20204.915| 174.686| 209,355|
| |Walker County|    64| 1007.541|  2.249| 1,539| 24228.208| 155.179|  63,521|
| |Lee County|    47| 285.641|  6.077| 2,700| 16409.184| 169.301| 164,542|
| |Elmore County|    38| 467.928|  1.759| 1,731| 21315.371| 226.928|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   844| 25380.405| 98.807|  33,254|
| |Marshall County|    37| 382.334| 10.333| 3,189| 32953.066| 329.191|  96,774|
| |Shelby County|    36| 165.364|  2.625| 3,309| 15199.677| 169.957| 217,702|
| |Butler County|    36| 1851.090|  7.346|   767| 39438.503| 110.184|  19,448|
| |Madison County|    34| 91.175|  3.448| 5,447| 14606.781| 165.877| 372,909|
| |Etowah County|    32| 312.903|  8.381| 2,162| 21140.533| 324.078| 102,268|
| |Hale County|    26| 1774.623|  0.000|   478| 32625.759| 185.263|  14,651|
| |Marion County|    26| 875.156|  9.617|   580| 19522.704| 182.725|  29,709|
| |Dale County|    25| 508.419| 14.526|   835| 16981.209| 145.263|  49,172|
| |Baldwin County|    25| 111.990|  1.280| 3,651| 16355.036| 282.215| 223,234|
| |Lowndes County|    24| 2467.613|  0.000|   573| 58914.250| 308.452|   9,726|
| |Dallas County|    23| 618.346|  0.000| 1,331| 35783.418| 165.148|  37,196|
| |Autauga County|    21| 375.879|  2.557| 1,174| 21013.442| 383.550|  55,869|
| |Franklin County|    20| 637.714|  0.000| 1,288| 41068.809| 419.069|  31,362|
| |Covington County|    20| 539.826|  0.000|   737| 19892.575| 107.965|  37,049|
| |Lauderdale County|    19| 204.898| 10.784| 1,189| 12822.310| 181.789|  92,729|
| |Morgan County|    18| 150.402|  3.581| 2,411| 20145.556| 224.410| 119,679|
| |Sumter County|    18| 1448.459|  0.000|   364| 29291.060| 34.487|  12,427|
| |St. Clair County|    18| 201.090|  9.576| 1,354| 15126.463| 218.646|  89,512|
| |Escambia County|    17| 464.062|  7.799| 1,087| 29672.699| 421.166|  36,633|
| |Calhoun County|    17| 149.641| 10.060| 1,807| 15905.990| 310.600| 113,605|
| |Colbert County|    16| 289.640| 10.344| 1,207| 21849.713| 294.812|  55,241|
| |Marengo County|    15| 795.208|  7.573|   565| 29952.818| 340.803|  18,863|
| |Macon County|    14| 774.851|  7.907|   339| 18762.453| 237.199|  18,068|
| |Talladega County|    14| 175.048|  1.786| 1,048| 13103.603| 232.207|  79,978|
| |DeKalb County|    13| 181.785|  0.000| 1,830| 25589.753| 257.695|  71,513|
| |Limestone County|    13| 131.426|  0.000| 1,349| 13637.972| 220.969|  98,915|
| |Choctaw County|    12| 953.213|  0.000|   287| 22797.681| 147.521|  12,589|
| |Cullman County|    12| 143.253|  1.705| 1,227| 14647.598| 146.664|  83,768|
| |Houston County|    12| 113.334|  0.000| 1,419| 13401.711| 134.921| 105,882|
| |Washington County|    12| 735.024|  8.750|   443| 27134.632| 1163.788|  16,326|
| |Winston County|    11| 465.530|  0.000|   457| 19340.641| 169.284|  23,629|
| |Bullock County|    11| 1089.001|  0.000|   466| 46134.046| 396.000|  10,101|
| |Greene County|    11| 1356.183|  0.000|   252| 31068.919| 176.128|   8,111|
| |Wilcox County|    10| 964.041| 13.772|   432| 41646.582| 371.844|  10,373|
| |Randolph County|    10| 440.102|  0.000|   403| 17736.115| 94.308|  22,722|
| |Clarke County|    10| 423.334|  6.048|   826| 34967.403| 2056.195|  23,622|
| |Conecuh County|    10| 828.706|  0.000|   393| 32568.161| 236.773|  12,067|
| |Pickens County|     9| 451.581|  0.000|   404| 20270.948| 265.214|  19,930|
| |Cherokee County|     8| 305.390|  5.453|   275| 10497.786| 179.962|  26,196|
| |Pike County|     7| 211.391|  0.000|   708| 21380.685| 207.077|  33,114|
| |Chilton County|     7| 157.558|  3.215|   809| 18209.237| 318.332|  44,428|
| |Coffee County|     6| 114.631|  2.729|   764| 14596.309| 150.112|  52,342|
| |Clay County|     5| 377.786|  0.000|   263| 19871.553| 496.519|  13,235|
| |Fayette County|     5| 306.711|  0.000|   212| 13004.539| 333.000|  16,302|
| |Bibb County|     5| 223.274| 12.759|   442| 19737.430| 433.790|  22,394|
| |Monroe County|     5| 241.161|  6.890|   421| 20305.793| 206.710|  20,733|
| |Barbour County|     5| 202.544|  0.000|   576| 23333.063| 75.231|  24,686|
| |Crenshaw County|     5| 363.055| 20.746|   326| 23671.217| 414.921|  13,772|
| |Blount County|     4| 69.173|  2.470|   812| 14042.126| 187.755|  57,826|
| |Jackson County|     4| 77.480|  2.767| 1,014| 19641.266| 514.691|  51,626|
| |Perry County|     4| 448.280|  0.000|   445| 49871.120| 256.160|   8,923|
| |Coosa County|     3| 281.347| 13.397|   103|  9659.570| 147.372|  10,663|
| |Henry County|     3| 174.368|  0.000|   264| 15344.377| 157.761|  17,205|
| |Russell County|     2| 34.506|  2.465| 1,387| 23929.884| 379.566|  57,961|
| |Lamar County|     2| 144.875|  0.000|   229| 16588.193| 320.795|  13,805|
| |Lawrence County|     2| 60.746|  8.678|   351| 10660.916| 177.899|  32,924|
| |Cleburne County|     1| 67.069|  0.000|   127|  8517.773| 57.488|  14,910|
| |Geneva County|     1| 38.065|  5.438|   263| 10011.039| 168.573|  26,271|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,695| 222.590| N/A|63,445|  8331.699| N/A|7,614,893|
| |King County|   676| 300.073|  1.141|16,707|  7416.164| 70.009|2,252,782|
| |Yakima County|   212| 845.049|  3.986|10,367| 41323.698| 182.221| 250,873|
| |Snohomish County|   193| 234.769|  0.521| 5,486|  6673.292| 56.824| 822,083|
| |Pierce County|   142| 156.910|  2.052| 5,751|  6354.837| 84.453| 904,980|
| |Benton County|   116| 567.542|  4.194| 3,748| 18337.492| 163.553| 204,390|
| |Spokane County|    90| 172.151|  7.924| 4,504|  8615.182| 162.587| 522,798|
| |Franklin County|    49| 514.587|  3.001| 3,540| 37176.283| 322.555|  95,222|
| |Clark County|    43| 88.071|  0.293| 1,787|  3660.078| 48.863| 488,241|
| |Whatcom County|    40| 174.484|  1.246|   990|  4318.486| 33.651| 229,247|
| |Skagit County|    22| 170.272|  1.106|   890|  6888.278| 70.762| 129,205|
| |Kittitas County|    20| 417.232|  8.941|   375|  7823.094| 80.466|  47,935|
| |Grant County|    13| 133.015|  1.462| 1,540| 15757.216| 359.580|  97,733|
| |Island County|    11| 129.197|  0.000|   247|  2901.070| 13.423|  85,141|
| |Thurston County|    11| 37.861|  1.475|   732|  2519.481| 45.237| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,358| 17590.674| 334.937|  77,200|
| |Kitsap County|     7| 25.785|  1.579|   746|  2747.971| 46.308| 271,473|
| |Douglas County|     7| 161.183|  0.000|   961| 22128.071| 430.917|  43,429|
| |Adams County|     5| 250.213|  7.149|   452| 22619.226| 371.745|  19,983|
| |Cowlitz County|     5| 45.211|  0.000|   485|  4385.449| 50.378| 110,593|
| |Okanogan County|     4| 94.690|  6.764|   877| 20760.836| 358.470|  42,243|
| |Walla Walla County|     3| 49.375|  0.000|   547|  9002.633| 218.659|  60,760|
| |Lewis County|     3| 37.171|  0.000|   225|  2787.862| 63.723|  80,707|
| |Klickitat County|     3| 133.779|  0.000|   113|  5039.019| 44.593|  22,425|
| |Grays Harbor County|     2| 26.645|  1.903|   122|  1625.345| 43.774|  75,061|
| |Pacific County|     2| 89.004|  0.000|    50|  2225.090| 63.574|  22,471|
| |Asotin County|     2| 88.566|  0.000|    27|  1195.643| 18.978|  22,582|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Mason County|     1| 14.977|  0.000|   226|  3384.855| 134.795|  66,768|
| |Stevens County|     1| 21.871|  0.000|   110|  2405.791| 56.239|  45,723|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 47.292|  12,083|
| |Whitman County|     0|  0.000|  0.000|   105|  2095.641| 51.322|  50,104|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Ferry County|     0|  0.000|  0.000|    23|  3015.602| 93.652|   7,627|
| |San Juan County|     0|  0.000|  0.000|    28|  1592.538|  0.000|  17,582|
| |Pend Oreille County|     0|  0.000|  0.000|    44|  3206.062| 83.274|  13,724|
| |Lincoln County|     0|  0.000|  0.000|    27|  2468.233| 182.832|  10,939|
| |Jefferson County|     0|  0.000|  0.000|    54|  1675.926|  4.434|  32,221|
| |Clallam County|     0|  0.000|  0.000|   122|  1577.634| 51.726|  77,331|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,660| 294.345| N/A|61,382| 10884.043| N/A|5,639,632|
| |Hennepin County|   835| 659.639|  1.806|19,472| 15382.634| 165.107|1,265,843|
| |Ramsey County|   267| 485.171|  1.558| 7,658| 13915.515| 185.346| 550,321|
| |Anoka County|   115| 322.200|  0.800| 3,739| 10475.708| 149.693| 356,921|
| |Dakota County|   106| 247.074|  0.999| 4,480| 10442.379| 162.829| 429,021|
| |Washington County|    45| 171.468|  1.089| 2,155|  8211.401| 129.553| 262,440|
| |Clay County|    40| 622.840|  0.000|   785| 12223.226| 88.977|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,747| 11036.496| 106.493| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,906| 18041.285| 66.517| 161,075|
| |St. Louis County|    19| 95.444|  0.000|   570|  2863.314| 96.161| 199,070|
| |Scott County|    19| 127.506|  4.793| 1,574| 10562.837| 176.399| 149,013|
| |Winona County|    16| 316.932|  0.000|   264|  5229.380| 48.106|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   239|  3673.814| 57.095|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   342|  9978.409| 125.043|  34,274|
| |Itasca County|    12| 265.899|  0.000|   147|  3257.257| 47.482|  45,130|
| |Goodhue County|     9| 194.217|  3.083|   197|  4251.187| 64.739|  46,340|
| |Pipestone County|     9| 986.193|  0.000|   157| 17203.594| 219.154|   9,126|
| |Rice County|     8| 119.453|  0.000| 1,038| 15499.015| 83.190|  66,972|
| |Sherburne County|     8| 82.272|  1.469|   732|  7527.921| 121.939|  97,238|
| |Nobles County|     6| 277.405|  0.000| 1,765| 81603.403| 125.493|  21,629|
| |Martin County|     5| 254.026|  0.000|   207| 10516.690| 21.774|  19,683|
| |Wright County|     5| 36.133|  0.000|   892|  6446.158| 81.558| 138,377|
| |Blue Earth County|     5| 73.907|  0.000|   927| 13702.275| 158.371|  67,653|
| |Renville County|     5| 343.690|  0.000|    65|  4467.968| 58.918|  14,548|
| |Polk County|     4| 127.535|  4.555|   154|  4910.088| 104.761|  31,364|
| |Benton County|     3| 73.369|  0.000|   320|  7826.066| 48.913|  40,889|
| |Carver County|     3| 28.547|  1.359|   873|  8307.244| 127.783| 105,089|
| |Grant County|     3| 502.344| 47.842|    56|  9377.093| 167.448|   5,972|
| |Koochiching County|     3| 245.319|  0.000|    79|  6460.054| 58.409|  12,229|
| |Lyon County|     3| 117.767|  0.000|   425| 16683.677| 50.472|  25,474|
| |Otter Tail County|     3| 51.067|  0.000|   197|  3353.420| 51.067|  58,746|
| |Mille Lacs County|     3| 114.168|  0.000|    71|  2701.983| 32.620|  26,277|
| |Wilkin County|     3| 483.325|  0.000|    34|  5477.686| 138.093|   6,207|
| |Todd County|     2| 81.090|  0.000|   426| 17272.138| 34.753|  24,664|
| |Steele County|     2| 54.572|  3.898|   351|  9577.342| 81.858|  36,649|
| |Sibley County|     2| 134.544|  0.000|    84|  5650.858| 48.052|  14,865|
| |Mower County|     2| 49.923|  0.000| 1,103| 27532.325| 78.450|  40,062|
| |Meeker County|     2| 86.125|  0.000|    86|  3703.385| 18.455|  23,222|
| |Cass County|     2| 67.161|  0.000|    73|  2451.392| 71.959|  29,779|
| |Brown County|     2| 79.974|  0.000|    89|  3558.861| 22.850|  25,008|
| |Kanabec County|     1| 61.211|  0.000|    37|  2264.798| 69.955|  16,337|
| |Douglas County|     1| 26.219|  3.746|   143|  3749.246| 48.692|  38,141|
| |Murray County|     1| 122.041|  0.000|   122| 14888.943|  0.000|   8,194|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 103.389|   5,527|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 30.354|  14,119|
| |Becker County|     1| 29.050|  0.000|   161|  4677.105| 74.701|  34,423|
| |Aitkin County|     1| 62.949|  8.993|    40|  2517.940| 116.904|  15,886|
| |Morrison County|     1| 29.953|  0.000|    93|  2785.599| 42.790|  33,386|
| |Chippewa County|     1| 84.746|  0.000|   106|  8983.051| 96.852|  11,800|
| |Le Sueur County|     1| 34.618|  0.000|   224|  7754.353| 113.744|  28,887|
| |Swift County|     1| 107.921|  0.000|    55|  5935.679| 46.252|   9,266|
| |Freeborn County|     1| 33.024|  0.000|   360| 11888.643| 28.306|  30,281|
| |Chisago County|     1| 17.674|  0.000|   204|  3605.578| 63.123|  56,579|
| |Kandiyohi County|     1| 23.149|  0.000|   698| 16157.781| 72.753|  43,199|
| |Lake of the Woods County|     0|  0.000|  0.000|     4|  1069.519| 114.591|   3,740|
| |Lac qui Parle County|     0|  0.000|  0.000|     8|  1207.912| 43.140|   6,623|
| |Lake County|     0|  0.000|  0.000|    21|  1973.499| 40.275|  10,641|
| |Dodge County|     0|  0.000|  0.000|   128|  6114.455| 34.121|  20,934|
| |Cook County|     0|  0.000|  0.000|     5|   915.248| 78.450|   5,463|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Carlton County|     0|  0.000|  0.000|   138|  3847.119| 51.773|  35,871|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   241|  5107.231| 145.315|  47,188|
| |Cottonwood County|     0|  0.000|  0.000|   178| 15898.535| 89.318|  11,196|
| |Faribault County|     0|  0.000|  0.000|    87|  6372.226| 41.854|  13,653|
| |Jackson County|     0|  0.000|  0.000|    86|  8734.511| 232.146|   9,846|
| |Isanti County|     0|  0.000|  0.000|   128|  3153.020| 63.342|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    34|  1582.058| 39.884|  21,491|
| |Houston County|     0|  0.000|  0.000|    40|  2150.538|  7.680|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    65|  3085.394| 27.124|  21,067|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Roseau County|     0|  0.000|  0.000|    52|  3428.948| 56.521|  15,165|
| |Rock County|     0|  0.000|  0.000|    85|  9125.067| 168.699|   9,315|
| |Redwood County|     0|  0.000|  0.000|    36|  2373.105| 56.502|  15,170|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 140.919|   4,055|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 63.498|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202|  9.659|  29,579|
| |Norman County|     0|  0.000|  0.000|    41|  6431.373| 156.863|   6,375|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255| 15.302|   9,336|
| |McLeod County|     0|  0.000|  0.000|   197|  5488.535| 234.825|  35,893|
| |Lincoln County|     0|  0.000|  0.000|    58| 10285.512| 101.335|   5,639|
| |Yellow Medicine County|     0|  0.000|  0.000|    52|  5355.855| 44.142|   9,709|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 43.709|   9,805|
| |Watonwan County|     0|  0.000|  0.000|   308| 28264.660| 131.098|  10,897|
| |Waseca County|     0|  0.000|  0.000|   149|  8005.588| 161.186|  18,612|
| |Wadena County|     0|  0.000|  0.000|    27|  1973.396| 41.765|  13,682|
| |Wabasha County|     0|  0.000|  0.000|    92|  4253.942| 72.660|  21,627|
| |Traverse County|     0|  0.000|  0.000|    11|  3375.268| 43.835|   3,259|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,278| 208.231| N/A|53,573|  8728.901| N/A|6,137,428|
| |St. Louis County|   847| 851.937|  3.736|20,176| 20293.601| 292.409| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,123| 10255.658| 173.054| 402,022|
| |Jackson County|    65| 92.459|  1.219| 4,083|  5807.875| 110.951| 703,011|
| |Jasper County|    31| 255.506|  7.065| 1,771| 14596.795| 131.874| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,628|  7232.952| 147.883| 225,081|
| |Clay County|    20| 80.017|  0.000| 1,053|  4212.876| 79.445| 249,948|
| |Franklin County|    18| 173.132|  0.000|   631|  6069.234| 122.292| 103,967|
| |Scott County|    13| 339.603|  0.000|   400| 10449.321| 179.131|  38,280|
| |Platte County|    10| 95.769|  0.000|   367|  3514.720| 67.038| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,091| 12487.981| 47.421|  87,364|
| |Greene County|    10| 34.120|  0.000| 1,573|  5367.025| 154.513| 293,086|
| |Pemiscot County|     9| 569.440|  9.039|   234| 14805.441| 180.775|  15,805|
| |Gentry County|     9| 1369.655|  0.000|    85| 12935.626| 65.222|   6,571|
| |Cass County|     9| 85.082|  0.000|   755|  7137.455| 136.402| 105,780|
| |Stoddard County|     9| 310.078|  0.000|   231|  7958.656| 108.281|  29,025|
| |McDonald County|     7| 306.520|  0.000|   951| 41642.948| 93.833|  22,837|
| |Saline County|     7| 307.544|  0.000|   435| 19111.638| 125.528|  22,761|
| |Newton County|     6| 103.029|  0.000|   874| 15007.899| 164.356|  58,236|
| |Cape Girardeau County|     5| 63.395|  3.623|   663|  8406.132| 101.431|  78,871|
| |Camden County|     5| 107.980|  3.085|   356|  7688.155| 145.001|  46,305|
| |Pettis County|     4| 94.476|  3.374|   550| 12990.387| 388.025|  42,339|
| |Perry County|     4| 209.030|  0.000|   232| 12123.746| 179.169|  19,136|
| |Barry County|     4| 111.766| 15.967|   258|  7208.919| 111.766|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   317| 10881.878| 304.045|  29,131|
| |Cole County|     3| 39.090|  1.861|   427|  5563.880| 189.868|  76,745|
| |Boone County|     3| 16.624|  0.000| 1,397|  7741.199| 127.450| 180,463|
| |Henry County|     3| 137.463|  0.000|    82|  3757.331| 65.459|  21,824|
| |Taney County|     3| 53.640|  0.000|   616| 11014.161| 408.689|  55,928|
| |St. Francois County|     2| 29.755|  0.000|   376|  5593.989| 146.651|  67,215|
| |Moniteau County|     2| 123.977|  0.000|   148|  9174.312| 221.388|  16,132|
| |Butler County|     2| 47.083|  0.000|   283|  6662.272| 121.071|  42,478|
| |Johnson County|     2| 36.995|  0.000|   489|  9045.170| 42.279|  54,062|
| |Douglas County|     2| 151.688|  0.000|    87|  6598.407| 65.009|  13,185|
| |Howell County|     2| 49.854|  0.000|   153|  3813.845| 46.293|  40,117|
| |Lawrence County|     2| 52.144|  0.000|   230|  5996.611| 141.535|  38,355|
| |Lafayette County|     2| 61.147|  0.000|   178|  5442.094| 87.353|  32,708|
| |Ray County|     2| 86.889| 12.413|   119|  5169.867| 142.745|  23,018|
| |Stone County|     1| 31.297|  0.000|   136|  4256.385| 214.608|  31,952|
| |Shannon County|     1| 122.459|  0.000|    43|  5265.736|  0.000|   8,166|
| |Scotland County|     1| 203.998|  0.000|    16|  3263.974| 116.570|   4,902|
| |Washington County|     1| 40.437|  0.000|    82|  3315.811| 150.194|  24,730|
| |Webster County|     1| 25.258|  0.000|   137|  3460.295| 68.556|  39,592|
| |Dallas County|     1| 59.249|  0.000|    69|  4088.162| 160.818|  16,878|
| |Grundy County|     1| 101.523|  0.000|    29|  2944.162| 72.516|   9,850|
| |Linn County|     1| 83.893|  0.000|    33|  2768.456| 23.969|  11,920|
| |Andrew County|     1| 56.459|  0.000|    88|  4968.383| 32.262|  17,712|
| |Audrain County|     1| 39.389|  0.000|   203|  7995.904| 50.643|  25,388|
| |Bates County|     1| 61.835|  0.000|    48|  2968.093| 70.669|  16,172|
| |Callaway County|     1| 22.350|  0.000|   159|  3553.629| 92.592|  44,743|
| |Miller County|     1| 39.034|  5.576|   132|  5152.426| 156.134|  25,619|
| |Marion County|     1| 35.051|  0.000|   201|  7045.216| 220.319|  28,530|
| |Bollinger County|     1| 82.420| 11.774|    68|  5604.550| 141.291|  12,133|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Christian County|     1| 11.287|  0.000|   364|  4108.584| 125.773|  88,595|
| |Caldwell County|     1| 110.865|  0.000|    35|  3880.266|  0.000|   9,020|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313| 91.263|   4,696|
| |Pulaski County|     1| 19.009|  0.000|   226|  4296.006| 116.769|  52,607|
| |Pike County|     1| 54.639|  0.000|   106|  5791.717| 249.778|  18,302|
| |Randolph County|     1| 40.407|  0.000|    71|  2868.919| 80.815|  24,748|
| |Osage County|     1| 73.448| 10.493|    49|  3598.972| 73.448|  13,615|
| |Lincoln County|     1| 16.945|  0.000|   382|  6473.150| 164.613|  59,013|
| |New Madrid County|     1| 58.562|  0.000|   256| 14991.801| 518.690|  17,076|
| |Carter County|     1| 167.168|  0.000|    21|  3510.532| 47.762|   5,982|
| |Lewis County|     1| 102.291|  0.000|    46|  4705.401| 175.357|   9,776|
| |Laclede County|     1| 27.993|  0.000|   202|  5654.620|  7.998|  35,723|
| |DeKalb County|     1| 79.700|  0.000|    36|  2869.212| 45.543|  12,547|
| |Benton County|     1| 51.432|  0.000|   104|  5348.969| 213.077|  19,443|
| |Ste. Genevieve County|     1| 55.885|  0.000|    57|  3185.425| 87.819|  17,894|
| |Clinton County|     0|  0.000|  0.000|    84|  4120.273| 133.138|  20,387|
| |Gasconade County|     0|  0.000|  0.000|    24|  1631.987| 38.857|  14,706|
| |Dent County|     0|  0.000|  0.000|    12|   770.564| 27.520|  15,573|
| |Daviess County|     0|  0.000|  0.000|    17|  2053.636|  0.000|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865|  0.000|   7,561|
| |Crawford County|     0|  0.000|  0.000|    78|  3260.870| 125.418|  23,920|
| |Cooper County|     0|  0.000|  0.000|   131|  7397.369| 266.208|  17,709|
| |Clark County|     0|  0.000|  0.000|    20|  2942.475| 126.106|   6,797|
| |Chariton County|     0|  0.000|  0.000|    18|  2423.916| 38.475|   7,426|
| |Cedar County|     0|  0.000|  0.000|    40|  2787.651| 59.735|  14,349|
| |Carroll County|     0|  0.000|  0.000|   101| 11637.285| 32.920|   8,679|
| |Barton County|     0|  0.000|  0.000|    69|  5870.342| 48.616|  11,754|
| |Atchison County|     0|  0.000|  0.000|    18|  3499.903| 166.662|   5,143|
| |Hickory County|     0|  0.000|  0.000|    33|  3457.670| 239.492|   9,544|
| |Holt County|     0|  0.000|  0.000|     8|  1816.943| 64.891|   4,403|
| |Howard County|     0|  0.000|  0.000|    53|  5299.470| 99.990|  10,001|
| |Mercer County|     0|  0.000|  0.000|    11|  3041.194| 78.992|   3,617|
| |Texas County|     0|  0.000|  0.000|    55|  2165.525| 95.621|  25,398|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    62|  3390.016| 31.244|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    57|  4427.872| 221.948|  12,873|
| |Mississippi County|     0|  0.000|  0.000|   140| 10622.155| 97.550|  13,180|
| |Monroe County|     0|  0.000|  0.000|    31|  3586.303| 165.267|   8,644|
| |Montgomery County|     0|  0.000|  0.000|    41|  3549.476| 37.103|  11,551|
| |Shelby County|     0|  0.000|  0.000|    38|  6408.094| 216.815|   5,930|
| |St. Clair County|     0|  0.000|  0.000|    23|  2447.590| 76.012|   9,397|
| |Madison County|     0|  0.000|  0.000|    25|  2068.167| 94.545|  12,088|
| |Ripley County|     0|  0.000|  0.000|    52|  3913.305| 75.256|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    34|  3298.089| 152.433|  10,309|
| |Polk County|     0|  0.000|  0.000|   210|  6532.085| 79.985|  32,149|
| |Phelps County|     0|  0.000|  0.000|    89|  1996.724| 48.075|  44,573|
| |Ozark County|     0|  0.000|  0.000|    14|  1526.052| 109.004|   9,174|
| |Oregon County|     0|  0.000|  0.000|    16|  1519.612| 27.136|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   186|  8419.337| 155.195|  22,092|
| |Morgan County|     0|  0.000|  0.000|    83|  4023.852| 83.109|  20,627|
| |Warren County|     0|  0.000|  0.000|   203|  5694.409| 128.234|  35,649|
| |Livingston County|     0|  0.000|  0.000|    63|  4137.388| 93.818|  15,227|
| |Adair County|     0|  0.000|  0.000|   160|  6313.380| 146.561|  25,343|
| |Knox County|     0|  0.000|  0.000|    27|  6819.904| 288.673|   3,959|
| |Iron County|     0|  0.000|  0.000|    22|  2172.840| 70.547|  10,125|
| |Vernon County|     0|  0.000|  0.000|    53|  2577.445| 48.631|  20,563|
| |Maries County|     0|  0.000|  0.000|    24|  2759.572| 114.982|   8,697|
| |Macon County|     0|  0.000|  0.000|    59|  3902.891| 56.701|  15,117|
| |Sullivan County|     0|  0.000|  0.000|   144| 23649.203| 187.692|   6,089|
| |Schuyler County|     0|  0.000|  0.000|    11|  2360.515| 61.312|   4,660|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,215| 177.913| N/A|117,825| 17253.185| N/A|6,829,174|
| |Shelby County|   308| 328.650|  3.049|23,485| 25059.595| 303.803| 937,166|
| |Davidson County|   217| 312.615|  3.087|20,722| 29852.595| 272.072| 694,144|
| |Sumner County|    72| 376.406|  1.494| 3,449| 18030.876| 202.393| 191,283|
| |Rutherford County|    55| 165.521|  0.860| 6,589| 19829.363| 222.270| 332,285|
| |Hamilton County|    53| 144.098|  2.330| 6,220| 16911.181| 217.119| 367,804|
| |Knox County|    40| 85.050|  1.215| 4,685|  9961.451| 198.348| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,577| 15003.439| 184.554| 238,412|
| |Wilson County|    23| 158.997|  1.975| 2,321| 16044.851| 245.902| 144,657|
| |McMinn County|    20| 371.789|  0.000|   553| 10279.957| 169.961|  53,794|
| |Robertson County|    20| 278.501|  5.968| 1,567| 21820.562| 232.747|  71,813|
| |Madison County|    18| 183.703|  7.290| 1,160| 11838.668| 361.575|  97,984|
| |Putnam County|    18| 224.313|  8.901| 1,785| 22244.377| 429.043|  80,245|
| |Hardeman County|    17| 678.643| 34.217|   930| 37125.749| 735.672|  25,050|
| |Sullivan County|    14| 88.413|  4.511| 1,037|  6548.867| 208.402| 158,348|
| |Hamblen County|    14| 215.604|  2.200| 1,405| 21637.355| 387.206|  64,934|
| |Bradley County|    13| 120.248|  3.964| 1,956| 18092.683| 321.102| 108,110|
| |Giles County|    13| 441.216| 19.394|   385| 13066.793| 164.850|  29,464|
| |Montgomery County|    13| 62.203|  1.367| 1,952|  9340.026| 149.014| 208,993|
| |Macon County|    13| 528.412|  0.000|   860| 34956.508| 162.588|  24,602|
| |Blount County|    11| 82.652|  4.294| 1,314|  9873.167| 208.240| 133,088|
| |Bedford County|    11| 221.270|  2.874|   928| 18667.149| 163.797|  49,713|
| |Tipton County|    10| 162.340|  2.319| 1,211| 19659.410| 243.510|  61,599|
| |Monroe County|     9| 193.361|  0.000|   452|  9711.032| 263.953|  46,545|
| |Dyer County|     8| 215.291|  3.844|   663| 17842.245| 415.204|  37,159|
| |Lauderdale County|     8| 312.098| 11.146|   514| 20052.276| 507.159|  25,633|
| |Fayette County|     8| 194.491|  0.000|   702| 17066.589| 284.790|  41,133|
| |Hardin County|     8| 311.867|  5.569|   482| 18789.958| 451.093|  25,652|
| |Greene County|     8| 115.826|  6.205|   504|  7297.051| 275.087|  69,069|
| |Sevier County|     7| 71.247|  2.908| 1,894| 19277.354| 263.177|  98,250|
| |Maury County|     7| 72.624|  2.964| 1,272| 13196.800| 283.085|  96,387|
| |Cheatham County|     7| 172.130|  7.026|   599| 14729.387| 179.155|  40,667|
| |Hawkins County|     7| 123.270|  7.547|   483|  8505.618| 304.401|  56,786|
| |Cumberland County|     6| 99.141|  0.000|   458|  7567.746| 186.479|  60,520|
| |Gibson County|     6| 122.118| 11.630|   726| 14776.220| 462.302|  49,133|
| |Carter County|     6| 106.400|  2.533|   524|  9292.263| 245.733|  56,391|
| |Anderson County|     6| 77.944|  1.856|   693|  9002.572| 159.600|  76,978|
| |Lawrence County|     6| 135.925|  0.000|   575| 13026.143| 313.922|  44,142|
| |Haywood County|     6| 346.741|  8.256|   510| 29472.954| 1122.779|  17,304|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 139.262|  11,284|
| |Crockett County|     5| 351.370| 20.078|   269| 18903.725| 431.684|  14,230|
| |McNairy County|     5| 194.598|  0.000|   381| 14828.365| 361.396|  25,694|
| |White County|     5| 182.849| 10.449|   294| 10751.509| 522.425|  27,345|
| |Jefferson County|     4| 73.401|  5.243|   584| 10716.580| 230.690|  54,495|
| |Marshall County|     4| 116.364|  8.312|   304|  8843.636| 162.078|  34,375|
| |Obion County|     4| 133.027|  0.000|   579| 19255.712| 684.141|  30,069|
| |Smith County|     4| 198.442|  7.087|   455| 22572.803| 652.024|  20,157|
| |Warren County|     4| 96.906|  0.000|   533| 12912.760| 449.922|  41,277|
| |Weakley County|     4| 120.019|  4.286|   463| 13892.223| 801.557|  33,328|
| |Franklin County|     4| 94.769|  0.000|   332|  7865.807| 155.692|  42,208|
| |Marion County|     4| 138.375|  0.000|   227|  7852.769| 108.723|  28,907|
| |Carroll County|     3| 108.042|  0.000|   325| 11704.541| 499.051|  27,767|
| |Cocke County|     3| 83.324|  7.936|   478| 13276.303| 309.489|  36,004|
| |Decatur County|     3| 257.224| 12.249|   216| 18520.106| 673.681|  11,663|
| |Humphreys County|     3| 161.447|  0.000|   128|  6888.387| 176.822|  18,582|
| |Loudon County|     3| 55.486|  0.000|   749| 13852.926| 253.649|  54,068|
| |Henderson County|     3| 106.697| 15.242|   604| 21481.666| 878.980|  28,117|
| |Polk County|     3| 178.232| 16.974|   207| 12298.004| 356.464|  16,832|
| |Coffee County|     3| 53.079|  2.528|   548|  9695.683| 331.109|  56,520|
| |Washington County|     2| 15.459|  0.000| 1,277|  9870.531| 232.988| 129,375|
| |Chester County|     2| 115.627|  0.000|   223| 12892.409| 247.772|  17,297|
| |Roane County|     2| 37.466|  0.000|   485|  9085.460| 323.812|  53,382|
| |Rhea County|     2| 60.301|  4.307|   538| 16220.943| 155.059|  33,167|
| |Hancock County|     2| 302.115| 21.580|    81| 12235.650| 107.898|   6,620|
| |Wayne County|     2| 119.954|  8.568|   228| 13674.804| 102.818|  16,673|
| |DeKalb County|     2| 97.609|  6.972|   365| 17813.568| 418.323|  20,490|
| |Dickson County|     2| 37.073|  2.648|   698| 12938.385| 272.749|  53,948|
| |Grundy County|     2| 148.954|  0.000|   114|  8490.355| 138.314|  13,427|
| |Benton County|     1| 61.881|  0.000|   159|  9839.109| 548.091|  16,160|
| |Bledsoe County|     1| 66.383|  0.000|   708| 46999.469| 341.401|  15,064|
| |Campbell County|     1| 25.099|  0.000|   254|  6375.182| 147.009|  39,842|
| |Jackson County|     1| 84.846|  0.000|   129| 10945.189| 278.781|  11,786|
| |Lincoln County|     1| 29.099|  0.000|   309|  8991.445| 228.631|  34,366|
| |Lewis County|     1| 81.513|  0.000|    74|  6031.953| 209.605|  12,268|
| |Overton County|     1| 44.962|  0.000|   198|  8902.477| 411.081|  22,241|
| |Morgan County|     1| 46.722|  0.000|   126|  5887.025| 293.684|  21,403|
| |Pickett County|     1| 198.098|  0.000|    37|  7329.635| 424.496|   5,048|
| |Perry County|     0|  0.000|  0.000|    81| 10029.718| 123.824|   8,076|
| |Grainger County|     0|  0.000|  0.000|   200|  8576.329| 189.904|  23,320|
| |Moore County|     0|  0.000|  0.000|    61|  9401.973| 352.299|   6,488|
| |Henry County|     0|  0.000|  0.000|   290|  8965.837| 326.833|  32,345|
| |Hickman County|     0|  0.000|  0.000|   273| 10842.799| 238.303|  25,178|
| |Houston County|     0|  0.000|  0.000|    59|  7194.245| 69.678|   8,201|
| |Johnson County|     0|  0.000|  0.000|   285| 16022.037| 907.514|  17,788|
| |Lake County|     0|  0.000|  0.000|   792| 112884.835| 875.550|   7,016|
| |Scott County|     0|  0.000|  0.000|   122|  5528.367| 116.523|  22,068|
| |Meigs County|     0|  0.000|  0.000|   106|  8533.247| 92.003|  12,422|
| |Cannon County|     0|  0.000|  0.000|   151| 10287.505| 321.180|  14,678|
| |Claiborne County|     0|  0.000|  0.000|   276|  8636.065| 245.851|  31,959|
| |Stewart County|     0|  0.000|  0.000|    78|  5687.204| 83.329|  13,715|
| |Clay County|     0|  0.000|  0.000|    78| 10242.942| 318.919|   7,615|
| |Fentress County|     0|  0.000|  0.000|    96|  5182.746| 169.673|  18,523|
| |Sequatchie County|     0|  0.000|  0.000|   106|  7054.439| 114.088|  15,026|
| |Unicoi County|     0|  0.000|  0.000|   169|  9450.316| 247.641|  17,883|
| |Union County|     0|  0.000|  0.000|   162|  8111.356| 300.421|  19,972|
| |Van Buren County|     0|  0.000|  0.000|    36|  6130.790| 72.986|   5,872|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   998| 171.406| N/A|61,061| 10487.195| N/A|5,822,434|
| |Milwaukee County|   456| 482.169|  1.511|21,178| 22393.378| 199.846| 945,726|
| |Racine County|    78| 397.329|  1.455| 3,526| 17961.296| 201.575| 196,311|
| |Kenosha County|    60| 353.855|  5.898| 2,681| 15811.419| 153.337| 169,561|
| |Waukesha County|    59| 145.968|  1.414| 4,299| 10635.876| 214.181| 404,198|
| |Brown County|    54| 204.126|  1.620| 4,264| 16118.424| 136.624| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,554|  8330.056| 84.665| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,441|  8821.333| 61.217| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,335| 12852.852| 105.904| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,066|  7836.276| 195.329| 136,034|
| |Winnebago County|    18| 104.708|  0.000| 1,193|  6939.799| 108.032| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   692|  7756.022| 198.544|  89,221|
| |Grant County|    15| 291.608|  2.777|   357|  6940.259| 77.762|  51,439|
| |Waupaca County|    15| 294.175|  0.000|   468|  9178.270| 249.349|  50,990|
| |Outagamie County|    14| 74.514|  0.760| 1,276|  6791.388| 123.936| 187,885|
| |Sheboygan County|     9| 78.030|  4.954|   753|  6528.524| 162.253| 115,340|
| |Marathon County|     9| 66.327|  3.158|   655|  4827.108| 78.960| 135,692|
| |Clark County|     7| 201.300|  0.000|   188|  5406.338| 45.190|  34,774|
| |Fond du Lac County|     7| 67.696|  1.382|   671|  6489.173| 138.156| 103,403|
| |Dodge County|     5| 56.922|  0.000|   835|  9506.028| 211.426|  87,839|
| |St. Croix County|     5| 55.135|  4.726|   502|  5535.523| 78.764|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   637|  7514.540| 123.023|  84,769|
| |Eau Claire County|     4| 38.224|  1.365|   590|  5638.056| 113.307| 104,646|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 41.403|  17,252|
| |Forest County|     4| 444.247|  0.000|    59|  6552.643|  0.000|   9,004|
| |Barron County|     3| 66.307|  0.000|   295|  6520.202| 113.669|  45,244|
| |Door County|     3| 108.429|  0.000|   106|  3831.141| 108.429|  27,668|
| |Marinette County|     3| 74.349|  0.000|   411| 10185.874| 283.236|  40,350|
| |Sauk County|     3| 46.553|  0.000|   444|  6889.917| 115.275|  64,442|
| |Adams County|     2| 98.912|  0.000|    86|  4253.215| 91.847|  20,220|
| |Pierce County|     2| 46.779|  6.683|   224|  5239.276| 167.069|  42,754|
| |Polk County|     2| 45.680|  0.000|   132|  3014.869| 39.154|  43,783|
| |Monroe County|     2| 43.240|  3.089|   244|  5275.333| 55.595|  46,253|
| |Buffalo County|     2| 153.480|  0.000|    44|  3376.564| 32.889|  13,031|
| |Calumet County|     2| 39.929|  0.000|   330|  6588.273| 205.349|  50,089|
| |Kewaunee County|     2| 97.876|  0.000|   131|  6410.884| 146.814|  20,434|
| |Trempealeau County|     2| 67.456|  0.000|   338| 11400.047| 149.367|  29,649|
| |Wood County|     1| 13.699|  0.000|   305|  4178.139| 125.246|  72,999|
| |Waushara County|     1| 40.912|  5.845|   120|  4909.381| 75.979|  24,443|
| |Taylor County|     1| 49.157|  7.022|    71|  3490.144| 119.381|  20,343|
| |Manitowoc County|     1| 12.661|  0.000|   345|  4368.139| 70.541|  78,981|
| |Marquette County|     1| 64.210|  0.000|    80|  5136.766| 82.555|  15,574|
| |Rusk County|     1| 70.532|  0.000|    21|  1481.168| 50.380|  14,178|
| |Langlade County|     1| 52.113|  0.000|    65|  3387.357| 119.116|  19,189|
| |La Crosse County|     1|  8.473|  0.000|   914|  7744.713| 107.734| 118,016|
| |Juneau County|     1| 37.471|  0.000|   138|  5171.057| 48.178|  26,687|
| |Jackson County|     1| 48.443|  0.000|    58|  2809.669| 62.283|  20,643|
| |Iron County|     1| 175.840|  0.000|    75| 13187.973| 75.360|   5,687|
| |Green County|     1| 27.056|  0.000|   167|  4518.398| 139.147|  36,960|
| |Ashland County|     1| 64.259|  9.180|    25|  1606.477| 45.899|  15,562|
| |Columbia County|     1| 17.382|  0.000|   252|  4380.171| 62.077|  57,532|
| |Burnett County|     1| 64.876|  0.000|    22|  1427.274| 37.072|  15,414|
| |Bayfield County|     1| 66.507|  0.000|    28|  1862.197| 76.008|  15,036|
| |Shawano County|     0|  0.000|  0.000|   200|  4890.095| 136.224|  40,899|
| |Price County|     0|  0.000|  0.000|    33|  2471.725| 128.401|  13,351|
| |Sawyer County|     0|  0.000|  0.000|    69|  4167.170| 250.203|  16,558|
| |Portage County|     0|  0.000|  0.000|   420|  5934.550| 131.206|  70,772|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689| 39.209|   7,287|
| |Oneida County|     0|  0.000|  0.000|   141|  3961.231| 208.697|  35,595|
| |Oconto County|     0|  0.000|  0.000|   256|  6749.275| 274.943|  37,930|
| |Menominee County|     0|  0.000|  0.000|    22|  4828.797| 62.712|   4,556|
| |Florence County|     0|  0.000|  0.000|     8|  1862.631| 33.261|   4,295|
| |Chippewa County|     0|  0.000|  0.000|   239|  3696.372| 64.073|  64,658|
| |Green Lake County|     0|  0.000|  0.000|    56|  2960.926| 30.214|  18,913|
| |Iowa County|     0|  0.000|  0.000|    82|  3463.130| 102.567|  23,678|
| |Lafayette County|     0|  0.000|  0.000|   143|  8580.858| 282.885|  16,665|
| |Lincoln County|     0|  0.000|  0.000|    68|  2464.393| 20.709|  27,593|
| |Washburn County|     0|  0.000|  0.000|    48|  3053.435| 118.139|  15,720|
| |Vilas County|     0|  0.000|  0.000|    55|  2478.036| 109.420|  22,195|
| |Vernon County|     0|  0.000|  0.000|    64|  2076.439| 27.809|  30,822|
| |Crawford County|     0|  0.000|  0.000|    75|  4649.433| 115.129|  16,131|
| |Douglas County|     0|  0.000|  0.000|   186|  4310.545| 168.846|  43,150|
| |Dunn County|     0|  0.000|  0.000|   126|  2777.288| 66.126|  45,368|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   955| 310.049| N/A|56,617| 18381.212| N/A|3,080,156|
| |Clark County|   811| 357.786|  6.870|49,151| 21683.802| 320.476|2,266,715|
| |Washoe County|   120| 254.497|  1.515| 5,792| 12283.704| 136.035| 471,519|
| |Nye County|     9| 193.453|  0.000|   408|  8769.856| 159.675|  46,523|
| |Lyon County|     6| 104.330|  2.484|   230|  3999.304| 59.617|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   105|  6238.489| 76.390|  16,831|
| |Elko County|     2| 37.895|  0.000|   553| 10477.851| 175.939|  52,778|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 25.824|   5,532|
| |Churchill County|     1| 40.146|  0.000|    69|  2770.083| 120.438|  24,909|
| |White Pine County|     1| 104.384|  0.000|    15|  1565.762| 14.912|   9,580|
| |Storey County|     0|  0.000|  0.000|     5|  1212.709| 34.649|   4,123|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Eureka County|     0|  0.000|  0.000|     3|  1478.561| 70.408|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Douglas County|     0|  0.000|  0.000|   205|  4191.800| 73.028|  48,905|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   934| 296.031| N/A|49,162| 15581.905| N/A|3,155,070|
| |Polk County|   207| 422.310|  1.166|10,351| 21117.551| 183.030| 490,161|
| |Linn County|    88| 388.168|  0.630| 2,399| 10581.987| 183.372| 226,706|
| |Black Hawk County|    66| 502.941|  4.354| 3,134| 23882.098| 142.609| 131,228|
| |Woodbury County|    52| 504.330|  1.386| 3,727| 36146.915| 105.300| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   848| 19876.242| 73.665|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,888| 20202.669| 151.337|  93,453|
| |Wapello County|    33| 943.693|  4.085|   904| 25851.468| 224.689|  34,969|
| |Dubuque County|    31| 318.566|  2.936| 1,686| 17325.893| 218.739|  97,311|
| |Tama County|    29| 1720.660|  0.000|   553| 32811.202| 135.619|  16,854|
| |Pottawattamie County|    26| 278.952|  4.598| 1,325| 14215.823| 165.532|  93,206|
| |Jasper County|    26| 699.207|  7.684|   479| 12881.538| 92.203|  37,185|
| |Marshall County|    26| 660.418|  7.257| 1,446| 36729.406| 206.834|  39,369|
| |Johnson County|    19| 125.711|  3.781| 2,107| 13940.717| 164.464| 151,140|
| |Mahaska County|    17| 769.405|  0.000|   140|  6336.275| 25.862|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   634| 14935.218| 195.188|  42,450|
| |Scott County|    14| 80.952|  1.652| 1,727|  9985.949| 110.689| 172,943|
| |Story County|    14| 144.156|  0.000| 1,167| 12016.434| 85.317|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Buena Vista County|    12| 611.621|  0.000| 1,794| 91437.309| 65.531|  19,620|
| |Washington County|    10| 455.270|  0.000|   300| 13658.092| 84.550|  21,965|
| |Franklin County|    10| 993.049| 70.932|   241| 23932.473| 297.915|  10,070|
| |Plymouth County|     9| 357.469|  5.674|   463| 18389.800| 113.482|  25,177|
| |Webster County|     8| 222.816| 11.937|   813| 22643.717| 350.140|  35,904|
| |Poweshiek County|     8| 432.339|  0.000|   159|  8592.737| 100.364|  18,504|
| |Monroe County|     7| 908.265|  0.000|    74|  9601.661| 129.752|   7,707|
| |Bremer County|     7| 279.307|  0.000|   227|  9057.537| 228.006|  25,062|
| |Guthrie County|     5| 467.771|  0.000|   132| 12349.144| 80.189|  10,689|
| |O'Brien County|     4| 290.846| 31.162|   141| 10252.309| 103.873|  13,753|
| |Montgomery County|     4| 403.348| 14.405|    59|  5949.380| 230.484|   9,917|
| |Lucas County|     4| 465.116|  0.000|    71|  8255.814| 431.894|   8,600|
| |Henry County|     4| 200.461|  7.159|   127|  6364.639| 100.231|  19,954|
| |Allamakee County|     4| 292.248|  0.000|   155| 11324.615| 41.750|  13,687|
| |Emmet County|     4| 434.405| 46.543|   192| 20851.434| 201.688|   9,208|
| |Dickinson County|     4| 231.777|  0.000|   382| 22134.662| 57.944|  17,258|
| |Clinton County|     3| 64.615|  0.000|   410|  8830.688| 286.151|  46,429|
| |Crawford County|     3| 178.359|  0.000|   730| 43400.713| 93.426|  16,820|
| |Appanoose County|     3| 241.429|  0.000|    49|  3943.345| 80.476|  12,426|
| |Boone County|     3| 114.355|  5.445|   259|  9872.684| 168.810|  26,234|
| |Sioux County|     3| 86.071|  4.099|   637| 18275.714| 172.142|  34,855|
| |Clayton County|     3| 170.950|  0.000|   104|  5926.264| 48.843|  17,549|
| |Clarke County|     3| 319.319|  0.000|   202| 21500.798| 243.291|   9,395|
| |Lee County|     3| 89.135|  0.000|   117|  3476.246| 93.379|  33,657|
| |Madison County|     2| 122.414|  0.000|   122|  7467.254| 174.877|  16,338|
| |Jones County|     2| 96.707|  0.000|   132|  6382.670| 55.261|  20,681|
| |Pocahontas County|     2| 302.160| 21.583|   116| 17525.306| 64.749|   6,619|
| |Hancock County|     2| 188.147|  0.000|   122| 11476.952| 67.195|  10,630|
| |Floyd County|     2| 127.861|  0.000|   157| 10037.080| 255.722|  15,642|
| |Des Moines County|     2| 51.325|  0.000|   186|  4773.270| 172.307|  38,967|
| |Davis County|     2| 222.222| 15.873|    60|  6666.667| 190.476|   9,000|
| |Calhoun County|     2| 206.868|  0.000|    83|  8585.023| 14.776|   9,668|
| |Butler County|     2| 138.514|  0.000|   121|  8380.082| 69.257|  14,439|
| |Lyon County|     2| 170.140| 24.306|   114|  9698.001| 145.835|  11,755|
| |Audubon County|     1| 181.951|  0.000|    28|  5094.614|  0.000|   5,496|
| |Benton County|     1| 38.994|  0.000|   160|  6239.033| 94.700|  25,645|
| |Buchanan County|     1| 47.226|  0.000|   129|  6092.090| 121.437|  21,175|
| |Keokuk County|     1| 97.599|  0.000|    37|  3611.165| 97.599|  10,246|
| |Carroll County|     1| 49.591|  0.000|   193|  9571.039| 85.013|  20,165|
| |Cass County|     1| 77.906|  0.000|    74|  5765.036| 289.365|  12,836|
| |Cedar County|     1| 53.686|  0.000|   133|  7140.173| 99.702|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   108|  9612.817| 139.869|  11,235|
| |Jackson County|     1| 51.443|  0.000|   156|  8025.104| 110.235|  19,439|
| |Clay County|     1| 62.438|  0.000|   196| 12237.762| 222.991|  16,016|
| |Iowa County|     1| 61.789|  0.000|    98|  6055.363| 79.444|  16,184|
| |Wayne County|     1| 155.255|  0.000|    20|  3105.108| 88.717|   6,441|
| |Van Buren County|     1| 141.965|  0.000|    36|  5110.733| 81.123|   7,044|
| |Delaware County|     1| 58.785|  0.000|   115|  6760.332| 209.948|  17,011|
| |Wright County|     1| 79.605|  0.000|   473| 37653.240| 341.165|  12,562|
| |Winneshiek County|     1| 50.023|  0.000|    97|  4852.183| 85.753|  19,991|
| |Grundy County|     1| 81.753|  0.000|    79|  6458.470| 58.395|  12,232|
| |Humboldt County|     1| 104.624|  0.000|   118| 12345.679| 388.605|   9,558|
| |Warren County|     1| 19.430|  0.000|   569| 11055.843| 113.806|  51,466|
| |Union County|     1| 81.693|  0.000|    77|  6290.336| 81.693|  12,241|
| |Hamilton County|     1| 67.691|  0.000|   248| 16787.382| 67.691|  14,773|
| |Shelby County|     1| 87.306|  0.000|   184| 16064.257| 286.862|  11,454|
| |Ringgold County|     1| 204.332|  0.000|    22|  4495.300| 29.190|   4,894|
| |Harrison County|     1| 71.179| 10.168|   109|  7758.559| 122.022|  14,049|
| |Worth County|     0|  0.000|  0.000|    66|  8941.878| 96.774|   7,381|
| |Winnebago County|     0|  0.000|  0.000|    84|  8112.807| 110.378|  10,354|
| |Taylor County|     0|  0.000|  0.000|    98| 16010.456| 116.694|   6,121|
| |Sac County|     0|  0.000|  0.000|    85|  8743.956| 58.783|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    86|  9678.145| 112.537|   8,886|
| |Page County|     0|  0.000|  0.000|    94|  6222.281| 170.214|  15,107|
| |Osceola County|     0|  0.000|  0.000|    83| 13930.849| 143.864|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972| 16.582|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    78|  7368.222| 26.990|  10,586|
| |Mills County|     0|  0.000|  0.000|    89|  5890.529| 66.186|  15,109|
| |Marion County|     0|  0.000|  0.000|   174|  5232.611| 90.217|  33,253|
| |Adams County|     0|  0.000|  0.000|    16|  4441.977|  0.000|   3,602|
| |Adair County|     0|  0.000|  0.000|    30|  4194.631| 179.770|   7,152|
| |Decatur County|     0|  0.000|  0.000|    23|  2922.490| 18.152|   7,870|
| |Howard County|     0|  0.000|  0.000|    49|  5350.513| 15.599|   9,158|
| |Ida County|     0|  0.000|  0.000|    31|  4518.950| 41.649|   6,860|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473| 64.292|   8,888|
| |Chickasaw County|     0|  0.000|  0.000|    54|  4525.266| 35.915|  11,933|
| |Fremont County|     0|  0.000|  0.000|    42|  6034.483| 143.678|   6,960|
| |Fayette County|     0|  0.000|  0.000|    84|  4274.809| 21.810|  19,650|
| |Jefferson County|     0|  0.000|  0.000|    86|  4700.738| 70.277|  18,295|
| |Hardin County|     0|  0.000|  0.000|   184| 10922.474| 161.123|  16,846|
| |Kossuth County|     0|  0.000|  0.000|    90|  6075.744| 115.728|  14,813|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   775| 173.468| N/A|35,254|  7890.909| N/A|4,467,673|
| |Jefferson County|   237| 309.094|  0.745| 8,188| 10678.742| 182.960| 766,757|
| |Fayette County|    47| 145.442|  0.442| 3,149|  9744.640| 151.189| 323,152|
| |Kenton County|    41| 245.512|  3.422| 1,416|  8479.143| 79.556| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   421|  9421.295| 57.544|  44,686|
| |Graves County|    25| 670.853| 11.500|   560| 15027.102| 187.839|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,104|  8264.648| 88.764| 133,581|
| |Logan County|    23| 848.646|  5.271|   328| 12102.428| 137.048|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,641| 19872.682| 204.241| 132,896|
| |Shelby County|    21| 428.362|  0.000|   774| 15788.185| 183.584|  49,024|
| |Adair County|    19| 989.480|  0.000|   205| 10675.971| 14.879|  19,202|
| |Oldham County|    15| 224.554|  2.139|   632|  9461.219| 121.901|  66,799|
| |Butler County|    15| 1164.687|  0.000|   293| 22750.214|  0.000|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   150| 11253.657| 75.024|  13,329|
| |Campbell County|    13| 138.913|  0.000|   571|  6101.470| 70.220|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   108|  8888.889| 152.851|  12,150|
| |Muhlenberg County|    11| 359.219|  4.665|   626| 20442.819| 65.313|  30,622|
| |Grayson County|    11| 416.241|  0.000|   202|  7643.698| 113.520|  26,427|
| |Casey County|    10| 618.850|  0.000|   189| 11696.268| 309.425|  16,159|
| |Daviess County|     9| 88.660|  2.815|   765|  7536.129| 70.365| 101,511|
| |Ohio County|     8| 333.417| 11.908|   356| 14837.043| 95.262|  23,994|
| |Knox County|     8| 256.863|  0.000|   235|  7545.352| 155.953|  31,145|
| |Allen County|     8| 375.323|  0.000|   226| 10602.862| 60.320|  21,315|
| |Christian County|     8| 113.538|  4.055|   502|  7124.509| 52.714|  70,461|
| |Hardin County|     8| 72.099|  0.000|   629|  5668.812| 137.761| 110,958|
| |Franklin County|     7| 137.279|  5.603|   315|  6177.561| 162.494|  50,991|
| |Gallatin County|     7| 789.266|  0.000|    80|  9020.183| 16.107|   8,869|
| |Clark County|     7| 193.034|  0.000|   166|  4577.669| 39.395|  36,263|
| |Simpson County|     7| 376.911|  0.000|   150|  8076.675| 84.613|  18,572|
| |Pulaski County|     5| 76.948|  6.596|   309|  4755.383| 107.727|  64,979|
| |Bullitt County|     5| 61.217|  1.749|   373|  4566.825| 101.446|  81,676|
| |Russell County|     5| 278.971|  0.000|   111|  6193.160| 87.677|  17,923|
| |Laurel County|     5| 82.219|  2.349|   433|  7120.188| 138.598|  60,813|
| |Clay County|     5| 251.244|  0.000|   152|  7637.807| 64.606|  19,901|
| |Grant County|     5| 199.450|  0.000|   121|  4826.678| 113.971|  25,069|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686| 34.801|   8,210|
| |McCracken County|     4| 61.145|  0.000|   367|  5610.077| 72.064|  65,418|
| |Calloway County|     4| 102.561|  3.663|   244|  6256.250| 175.820|  39,001|
| |Bell County|     4| 153.657| 10.976|   312| 11985.249| 170.120|  26,032|
| |Boyd County|     3| 64.215|  0.000|   191|  4088.360| 51.984|  46,718|
| |Harlan County|     3| 115.340|  0.000|   232|  8919.646| 137.310|  26,010|
| |Henderson County|     3| 66.357|  0.000|   344|  7608.936| 63.197|  45,210|
| |Perry County|     3| 116.469|  0.000|   226|  8773.973| 205.207|  25,758|
| |Pike County|     3| 51.835|  0.000|   249|  4302.301| 74.050|  57,876|
| |Metcalfe County|     2| 198.590|  0.000|    60|  5957.700| 127.665|  10,071|
| |Taylor County|     2| 77.613|  0.000|   137|  5316.466| 199.575|  25,769|
| |Nelson County|     2| 43.259|  0.000|   218|  4715.247| 86.518|  46,233|
| |Monroe County|     2| 187.793|  0.000|    94|  8826.291| 80.483|  10,650|
| |Meade County|     2| 69.999|  0.000|    94|  3289.934| 44.999|  28,572|
| |Marshall County|     2| 64.309|  0.000|   138|  4437.299| 59.715|  31,100|
| |Lincoln County|     2| 81.470|  5.819|   106|  4317.895| 40.735|  24,549|
| |Henry County|     2| 124.023|  0.000|   120|  7441.399| 230.329|  16,126|
| |Carroll County|     2| 188.129|  0.000|   158| 14862.195| 215.005|  10,631|
| |Breckinridge County|     2| 97.671|  0.000|    74|  3613.811| 153.482|  20,477|
| |Barren County|     2| 45.199|  0.000|   364|  8226.175| 96.854|  44,249|
| |Green County|     2| 182.799|  0.000|    37|  3381.775| 91.399|  10,941|
| |Floyd County|     2| 56.197|  0.000|    95|  2669.364| 48.169|  35,589|
| |Fulton County|     2| 335.064| 23.933|    83| 13905.177| 550.463|   5,969|
| |Carter County|     1| 37.318|  0.000|   101|  3769.079| 31.987|  26,797|
| |Bourbon County|     1| 50.536|  0.000|    83|  4194.461| 101.071|  19,788|
| |Crittenden County|     1| 113.559|  0.000|    31|  3520.327| 81.114|   8,806|
| |Clinton County|     1| 97.867| 13.981|    36|  3523.194| 125.828|  10,218|
| |Carlisle County|     1| 210.084|  0.000|    43|  9033.613| 360.144|   4,760|
| |Bath County|     1| 80.000|  0.000|    37|  2960.000| 22.857|  12,500|
| |Anderson County|     1| 43.962|  0.000|    84|  3692.795| 56.522|  22,747|
| |Greenup County|     1| 28.492|  0.000|   110|  3134.082| 85.475|  35,098|
| |Whitley County|     1| 27.576|  0.000|   163|  4494.816| 74.848|  36,264|
| |Webster County|     1| 77.268|  0.000|    89|  6876.835| 88.306|  12,942|
| |Mason County|     1| 58.582|  0.000|    54|  3163.445|  8.369|  17,070|
| |Madison County|     1| 10.754|  0.000|   516|  5549.163| 184.358|  92,987|
| |McLean County|     1| 108.613|  0.000|    42|  4561.746| 62.065|   9,207|
| |Livingston County|     1| 108.767|  0.000|    35|  3806.831| 46.614|   9,194|
| |Larue County|     1| 69.454|  0.000|    56|  3889.429| 49.610|  14,398|
| |Knott County|     1| 67.540|  0.000|    60|  4052.411| 144.729|  14,806|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 49.137|   8,722|
| |Garrard County|     0|  0.000|  0.000|    79|  4471.867| 88.952|  17,666|
| |Fleming County|     0|  0.000|  0.000|    59|  4046.362| 29.392|  14,581|
| |Estill County|     0|  0.000|  0.000|    22|  1559.620| 101.274|  14,106|
| |Cumberland County|     0|  0.000|  0.000|    57|  8618.083| 367.186|   6,614|
| |Elliott County|     0|  0.000|  0.000|    11|  1463.350| 57.014|   7,517|
| |Hart County|     0|  0.000|  0.000|   100|  5253.480| 150.099|  19,035|
| |Johnson County|     0|  0.000|  0.000|    49|  2208.401| 64.385|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   344|  6356.833| 116.155|  54,115|
| |Trigg County|     0|  0.000|  0.000|    54|  3685.755| 39.003|  14,651|
| |Todd County|     0|  0.000|  0.000|    35|  2846.917| 23.240|  12,294|
| |Spencer County|     0|  0.000|  0.000|   121|  6252.907| 140.266|  19,351|
| |Scott County|     0|  0.000|  0.000|   378|  6631.114| 120.292|  57,004|
| |Rowan County|     0|  0.000|  0.000|    70|  2861.815| 11.681|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    71|  4252.770| 85.569|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    59|  4773.849| 104.031|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    44|  3015.764| 78.332|  14,590|
| |Owsley County|     0|  0.000|  0.000|    12|  2718.007| 64.714|   4,415|
| |Owen County|     0|  0.000|  0.000|    48|  4403.266| 78.630|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    31|  2329.251| 10.734|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   121|  4297.333| 40.589|  28,157|
| |Mercer County|     0|  0.000|  0.000|    83|  3784.252| 58.620|  21,933|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Martin County|     0|  0.000|  0.000|    36|  3215.721| 76.565|  11,195|
| |Marion County|     0|  0.000|  0.000|   124|  6433.871| 103.772|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    39|  3206.973| 187.954|  12,161|
| |McCreary County|     0|  0.000|  0.000|    41|  2379.432| 33.163|  17,231|
| |Lewis County|     0|  0.000|  0.000|    41|  3088.512| 53.807|  13,275|
| |Letcher County|     0|  0.000|  0.000|    59|  2737.438| 53.025|  21,553|
| |Trimble County|     0|  0.000|  0.000|    32|  3777.594|  0.000|   8,471|
| |Union County|     0|  0.000|  0.000|    65|  4519.853| 109.271|  14,381|
| |Washington County|     0|  0.000|  0.000|    86|  7110.376| 259.848|  12,095|
| |Hickman County|     0|  0.000|  0.000|    49| 11187.215| 489.237|   4,380|
| |Wayne County|     0|  0.000|  0.000|    67|  3295.136| 98.362|  20,333|
| |Lawrence County|     0|  0.000|  0.000|    36|  2350.330| 27.980|  15,317|
| |Lee County|     0|  0.000|  0.000|     6|   810.482| 38.594|   7,403|
| |Leslie County|     0|  0.000|  0.000|    31|  3138.605| 72.318|   9,877|
| |Woodford County|     0|  0.000|  0.000|   156|  5835.266| 122.904|  26,734|
| |Wolfe County|     0|  0.000|  0.000|    14|  1956.127| 59.881|   7,157|
| |Caldwell County|     0|  0.000|  0.000|    53|  4157.841| 44.828|  12,747|
| |Breathitt County|     0|  0.000|  0.000|    31|  2454.473| 56.555|  12,630|
| |Bracken County|     0|  0.000|  0.000|    34|  4094.905| 86.027|   8,303|
| |Boyle County|     0|  0.000|  0.000|   154|  5123.087| 80.791|  30,060|
| |Ballard County|     0|  0.000|  0.000|    35|  4437.120| 72.443|   7,888|
| |Harrison County|     0|  0.000|  0.000|   121|  6406.862| 37.821|  18,886|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   690| 329.068| N/A|21,142| 10082.844| N/A|2,096,829|
| |McKinley County|   226| 3166.730| 10.009| 4,057| 56847.002| 106.091|  71,367|
| |San Juan County|   184| 1484.374|  3.457| 3,047| 24580.906| 50.708| 123,958|
| |Bernalillo County|   134| 197.314|  2.314| 5,161|  7599.529| 59.320| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,137|  7747.976| 39.913| 146,748|
| |Dona Ana County|    31| 142.075|  4.583| 2,466| 11301.817| 147.967| 218,195|
| |Cibola County|    18| 674.789|  5.355|   369| 13833.177| 155.309|  26,675|
| |Otero County|    10| 148.170|  0.000|   203|  3007.853| 31.751|  67,490|
| |Rio Arriba County|     7| 179.851|  7.341|   318|  8170.396| 80.750|  38,921|
| |Chaves County|     6| 92.858|  0.000|   462|  7150.043| 210.035|  64,615|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024| 17.173|  16,637|
| |Lea County|     5| 70.353|  2.010|   798| 11228.366| 285.433|  71,070|
| |Eddy County|     4| 68.423|  0.000|   306|  5234.348| 117.296|  58,460|
| |Valencia County|     4| 52.159|  0.000|   428|  5581.056| 102.456|  76,688|
| |Luna County|     4| 168.712|  6.025|   254| 10713.231| 114.483|  23,709|
| |Santa Fe County|     3| 19.952|  0.000|   654|  4349.619| 54.156| 150,358|
| |Curry County|     2| 40.855|  0.000|   558| 11398.456| 218.864|  48,954|
| |Lincoln County|     2| 102.187|  7.299|   128|  6539.955| 138.682|  19,572|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824| 15.874|  26,998|
| |Union County|     2| 492.732| 70.390|    30|  7390.983| 105.585|   4,059|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 47.854|  11,941|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |Quay County|     1| 121.168|  0.000|    34|  4119.714| 17.310|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   166|  8972.973| 185.328|  18,500|
| |Sierra County|     1| 92.670| 13.239|    32|  2965.434| 26.477|  10,791|
| |Taos County|     1| 30.560|  0.000|   109|  3330.990| 43.656|  32,723|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411|  9.240|  15,461|
| |Guadalupe County|     0|  0.000|  0.000|    31|  7209.302|  0.000|   4,300|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 68.060|   4,198|
| |Los Alamos County|     0|  0.000|  0.000|    23|  1187.465| 22.127|  19,369|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |San Miguel County|     0|  0.000|  0.000|    44|  1613.081| 10.475|  27,277|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   605| 152.895| N/A|43,962| 11110.013| N/A|3,956,971|
| |Oklahoma County|   112| 140.450|  2.508|10,665| 13374.148| 219.633| 797,434|
| |Tulsa County|   107| 164.223|  1.316|10,562| 16210.525| 307.617| 651,552|
| |Cleveland County|    55| 193.652|  3.018| 3,017| 10622.716| 146.874| 284,014|
| |Washington County|    39| 756.885|  0.000|   636| 12343.043| 169.121|  51,527|
| |McCurtain County|    28| 852.827| 13.053|   858| 26133.041| 126.184|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   864| 10628.744| 221.432|  81,289|
| |Delaware County|    19| 441.768|  0.000|   431| 10021.158| 93.004|  43,009|
| |Rogers County|    16| 173.050|  3.090|   986| 10664.186| 251.849|  92,459|
| |Caddo County|    16| 556.290|  9.934|   425| 14776.441| 258.277|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   509|  7485.624| 128.157|  67,997|
| |Creek County|    14| 195.744|  1.997|   607|  8486.899| 213.720|  71,522|
| |Kay County|    11| 252.653|  3.281|   244|  5604.300| 88.593|  43,538|
| |Osage County|    11| 234.227|  0.000|   426|  9070.971| 179.473|  46,963|
| |Comanche County|    10| 82.816|  0.000|   831|  6882.045| 62.704| 120,749|
| |Pottawatomie County|     9| 123.981|  1.968|   448|  6171.479| 94.461|  72,592|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 50.020|   5,712|
| |Canadian County|     7| 47.200|  1.927| 1,224|  8253.206| 130.040| 148,306|
| |Grady County|     7| 125.372|  2.559|   442|  7916.323| 76.758|  55,834|
| |Texas County|     7| 350.298|  0.000| 1,056| 52844.918| 142.979|  19,983|
| |Jackson County|     7| 285.365| 17.471|   523| 21320.832| 215.480|  24,530|
| |Mayes County|     6| 145.985|  0.000|   322|  7834.550| 128.606|  41,100|
| |Adair County|     6| 270.343|  6.437|   341| 15364.513| 231.723|  22,194|
| |Garfield County|     5| 81.892|  2.340|   460|  7534.067| 205.900|  61,056|
| |Seminole County|     5| 206.118|  0.000|   236|  9728.749| 253.230|  24,258|
| |Garvin County|     4| 144.347|  0.000|   227|  8191.693| 97.950|  27,711|
| |Payne County|     4| 48.909|  1.747|   740|  9048.225| 118.780|  81,784|
| |Sequoyah County|     4| 96.226|  0.000|   339|  8155.116| 257.747|  41,569|
| |McClain County|     4| 98.829|  0.000|   445| 10994.713| 169.421|  40,474|
| |Carter County|     4| 83.141|  2.969|   342|  7108.561| 100.957|  48,111|
| |Okmulgee County|     3| 77.993|  0.000|   469| 12192.903| 271.118|  38,465|
| |Stephens County|     3| 69.536|  3.311|   201|  4658.925| 86.092|  43,143|
| |Pittsburg County|     3| 68.722|  0.000|   361|  8269.574| 523.598|  43,654|
| |Ottawa County|     3| 96.379|  4.589|   371| 11918.913| 110.148|  31,127|
| |Pawnee County|     3| 183.195|  0.000|   138|  8426.966| 139.577|  16,376|
| |Cotton County|     2| 352.983|  0.000|    18|  3176.844| 25.213|   5,666|
| |Hughes County|     2| 150.614| 10.758|   138| 10392.349| 290.469|  13,279|
| |Lincoln County|     2| 57.344|  0.000|   167|  4788.256| 143.361|  34,877|
| |Noble County|     2| 179.678|  0.000|    84|  7546.492| 89.839|  11,131|
| |Pontotoc County|     2| 52.241|  0.000|   201|  5250.235| 89.556|  38,284|
| |Cherokee County|     2| 41.104|  2.936|   445|  9145.652| 275.984|  48,657|
| |Choctaw County|     1| 68.157|  0.000|   188| 12813.522| 214.208|  14,672|
| |Beckham County|     1| 45.748|  0.000|    59|  2699.117| 91.495|  21,859|
| |Bryan County|     1| 20.836|  0.000|   458|  9542.661| 217.285|  47,995|
| |McIntosh County|     1| 51.031|  0.000|   181|  9236.579| 218.704|  19,596|
| |Roger Mills County|     1| 279.096| 39.871|     8|  2232.766|  0.000|   3,583|
| |Logan County|     1| 20.829|  0.000|   222|  4623.940| 98.192|  48,011|
| |Le Flore County|     1| 20.059|  0.000|   345|  6920.346| 275.094|  49,853|
| |Major County|     1| 131.079|  0.000|    34|  4456.678| 168.530|   7,629|
| |Marshall County|     1| 59.063|  8.438|   107|  6319.768| 84.376|  16,931|
| |Okfuskee County|     1| 83.382| 11.912|    67|  5586.592| 119.117|  11,993|
| |Nowata County|     1| 99.246|  0.000|    58|  5756.252| 28.356|  10,076|
| |Kiowa County|     1| 114.837|  0.000|    29|  3330.271| 32.811|   8,708|
| |Tillman County|     1| 137.931|  0.000|    58|  8000.000| 39.409|   7,250|
| |Latimer County|     1| 99.275|  0.000|    92|  9133.327| 297.826|  10,073|
| |Beaver County|     0|  0.000|  0.000|    36|  6778.384|  0.000|   5,311|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Atoka County|     0|  0.000|  0.000|    70|  5087.949| 62.301|  13,758|
| |Blaine County|     0|  0.000|  0.000|    42|  4454.343| 60.603|   9,429|
| |Washita County|     0|  0.000|  0.000|    28|  2565.042| 52.348|  10,916|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 81.233|   8,793|
| |Woodward County|     0|  0.000|  0.000|    37|  1830.686| 35.341|  20,211|
| |Kingfisher County|     0|  0.000|  0.000|   139|  8817.000| 253.727|  15,765|
| |Love County|     0|  0.000|  0.000|    75|  7314.932| 139.332|  10,253|
| |Murray County|     0|  0.000|  0.000|    73|  5187.238| 131.965|  14,073|
| |Pushmataha County|     0|  0.000|  0.000|   108|  9733.237| 102.997|  11,096|
| |Coal County|     0|  0.000|  0.000|    37|  6733.394| 259.977|   5,495|
| |Cimarron County|     0|  0.000|  0.000|     1|   467.946|  0.000|   2,137|
| |Johnston County|     0|  0.000|  0.000|    48|  4330.176| 103.099|  11,085|
| |Haskell County|     0|  0.000|  0.000|    60|  4751.722| 192.332|  12,627|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 47.603|   6,002|
| |Harper County|     0|  0.000|  0.000|    10|  2711.497| 38.736|   3,688|
| |Craig County|     0|  0.000|  0.000|    86|  6081.177| 90.915|  14,142|
| |Custer County|     0|  0.000|  0.000|   206|  7102.714| 68.958|  29,003|
| |Dewey County|     0|  0.000|  0.000|    10|  2044.572| 58.416|   4,891|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Grant County|     0|  0.000|  0.000|    15|  3461.805| 98.909|   4,333|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 376.932|   2,653|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   591| 837.408| N/A|12,807| 18146.678| N/A| 705,749|
| |District of Columbia|   591| 837.408|  1.012|12,807| 18146.678| 99.995| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   591| 606.923| N/A|15,385| 15799.516| N/A| 973,764|
| |New Castle County|   291| 520.803|  1.023| 7,243| 12962.794| 77.980| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,848| 24967.446| 106.735| 234,225|
| |Kent County|   108| 597.391|  0.790| 2,294| 12689.036| 62.426| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   555| 183.909| N/A|48,205| 15973.536| N/A|3,017,804|
| |Pulaski County|    85| 216.886|  2.187| 5,639| 14388.471| 271.928| 391,911|
| |Washington County|    51| 213.222|  2.389| 6,310| 26381.032| 142.148| 239,187|
| |Benton County|    43| 154.044|  2.047| 4,794| 17174.116| 113.614| 279,141|
| |Jefferson County|    40| 598.587|  2.138| 1,574| 23554.412| 410.460|  66,824|
| |Crittenden County|    23| 479.616|  8.937| 1,369| 28547.597| 378.331|  47,955|
| |Sebastian County|    20| 156.461|  5.588| 2,229| 17437.631| 416.858| 127,827|
| |Union County|    18| 465.333|  7.386|   504| 13029.316| 254.825|  38,682|
| |Yell County|    17| 796.589| 20.082| 1,067| 49997.657| 247.679|  21,341|
| |Garland County|    16| 160.988| 11.499| 1,058| 10645.363| 263.044|  99,386|
| |Mississippi County|    14| 344.395| 10.543| 1,033| 25411.429| 829.359|  40,651|
| |Lincoln County|    12| 921.376| 10.969| 1,223| 93903.563| 405.844|  13,024|
| |Columbia County|    12| 511.574| 36.541|   217|  9250.970| 91.353|  23,457|
| |Craighead County|    12| 108.763|  0.000| 1,374| 12453.323| 310.750| 110,332|
| |Hot Spring County|    11| 325.723|  8.460| 1,554| 46015.812| 376.485|  33,771|
| |Sevier County|    10| 587.993|  0.000|   992| 58328.923| 445.195|  17,007|
| |Pope County|    10| 156.074|  2.230| 1,319| 20586.216| 229.652|  64,072|
| |Lawrence County|     9| 548.580|  0.000|   214| 13044.008| 252.521|  16,406|
| |Nevada County|     9| 1090.645|  0.000|   143| 17329.132| 173.118|   8,252|
| |Phillips County|     9| 506.130| 24.101|   325| 18276.909| 329.386|  17,782|
| |Lee County|     8| 903.240| 16.129|   896| 101162.922| 96.776|   8,857|
| |Chicot County|     8| 790.670| 28.238|   739| 73038.150| 2866.179|  10,118|
| |Carroll County|     7| 246.653|  5.034|   359| 12649.753| 95.641|  28,380|
| |Saline County|     6| 49.005|  1.167| 1,095|  8943.375| 236.857| 122,437|
| |Faulkner County|     6| 47.616|  1.134| 1,319| 10467.672| 121.308| 126,007|
| |Newton County|     6| 773.894| 55.278|   106| 13672.127| 147.408|   7,753|
| |Miller County|     5| 115.588|  3.303|   518| 11974.940| 158.521|  43,257|
| |Sharp County|     5| 286.664|  0.000|   112|  6421.282| 49.142|  17,442|
| |Cleburne County|     5| 200.650|  0.000|   202|  8106.264| 114.657|  24,919|
| |Ashley County|     5| 254.362|  7.267|   330| 16787.913| 552.330|  19,657|
| |Bradley County|     4| 371.644| 13.273|   204| 18953.823| 756.560|  10,763|
| |Crawford County|     4| 63.234|  2.258|   635| 10038.415| 182.927|  63,257|
| |Cross County|     4| 243.620| 17.401|   204| 12424.630| 278.423|  16,419|
| |Clay County|     4| 274.895|  0.000|   136|  9346.437| 265.078|  14,551|
| |Randolph County|     4| 222.742|  7.955|   219| 12195.122| 350.023|  17,958|
| |Howard County|     4| 302.984| 21.642|   342| 25905.166| 454.477|  13,202|
| |Conway County|     3| 143.913|  0.000|   153|  7339.538| 109.648|  20,846|
| |Poinsett County|     3| 127.508|  0.000|   286| 12155.729| 722.543|  23,528|
| |St. Francis County|     3| 120.029|  0.000| 1,223| 48931.744| 474.400|  24,994|
| |Drew County|     3| 164.663|  7.841|   209| 11471.541| 337.168|  18,219|
| |Lafayette County|     2| 301.932|  0.000|    54|  8152.174| 107.833|   6,624|
| |Johnson County|     2| 75.250| 10.750|   670| 25208.819| 182.751|  26,578|
| |Lonoke County|     2| 27.282|  0.000|   524|  7147.826| 140.306|  73,309|
| |Cleveland County|     2| 251.383|  0.000|   102| 12820.513| 556.633|   7,956|
| |Madison County|     2| 120.656|  8.618|   270| 16288.610| 68.946|  16,576|
| |Desha County|     2| 176.041|  0.000|   197| 17340.023| 465.251|  11,361|
| |Franklin County|     2| 112.899|  0.000|   127|  7169.066| 153.220|  17,715|
| |White County|     2| 25.396|  0.000|   326|  4139.525| 108.839|  78,753|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385|  8.634|  16,545|
| |Greene County|     2| 44.126|  3.152|   485| 10700.496| 289.969|  45,325|
| |Hempstead County|     2| 92.885|  0.000|   247| 11471.299| 179.135|  21,532|
| |Ouachita County|     2| 85.536|  6.110|   102|  4362.330| 128.304|  23,382|
| |Boone County|     2| 53.430|  3.816|   212|  5663.603| 137.392|  37,432|
| |Little River County|     1| 81.573|  0.000|   181| 14764.663| 291.331|  12,259|
| |Clark County|     1| 44.803|  6.400|   177|  7930.108| 115.207|  22,320|
| |Stone County|     1| 79.962|  0.000|    69|  5517.352| 159.923|  12,506|
| |Polk County|     1| 50.090|  0.000|   148|  7413.344| 121.648|  19,964|
| |Logan County|     1| 46.585|  0.000|   273| 12717.786| 519.093|  21,466|
| |Montgomery County|     1| 111.284| 15.898|    38|  4228.800| 190.773|   8,986|
| |Pike County|     1| 93.301|  0.000|   108| 10076.507| 359.875|  10,718|
| |Independence County|     1| 26.438|  3.777|   537| 14196.960| 524.974|  37,825|
| |Izard County|     1| 73.373|  0.000|    53|  3888.767| 83.855|  13,629|
| |Jackson County|     1| 59.812|  0.000|   117|  6998.026| 495.587|  16,719|
| |Arkansas County|     1| 57.189|  8.170|   221| 12638.682| 163.396|  17,486|
| |Perry County|     0|  0.000|  0.000|    54|  5164.993| 68.320|  10,455|
| |Marion County|     0|  0.000|  0.000|    29|  1737.151| 51.344|  16,694|
| |Monroe County|     0|  0.000|  0.000|    62|  9252.350| 191.869|   6,701|
| |Woodruff County|     0|  0.000|  0.000|    22|  3481.013| 45.208|   6,320|
| |Calhoun County|     0|  0.000|  0.000|    17|  3276.161| 110.123|   5,189|
| |Prairie County|     0|  0.000|  0.000|    96| 11907.715| 389.836|   8,062|
| |Scott County|     0|  0.000|  0.000|    61|  5933.275| 236.219|  10,281|
| |Searcy County|     0|  0.000|  0.000|    32|  4060.398| 90.634|   7,881|
| |Baxter County|     0|  0.000|  0.000|    71|  1693.218| 30.662|  41,932|
| |Dallas County|     0|  0.000|  0.000|    64|  9131.117| 122.292|   7,009|
| |Fulton County|     0|  0.000|  0.000|    44|  3526.489| 171.745|  12,477|
| |Grant County|     0|  0.000|  0.000|   137|  7500.684| 78.214|  18,265|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,840|  5030.481| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.000| 3,855|  9244.050| 27.405| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,691|  5458.906| 22.597| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   466|  3078.122|  7.549| 151,391|
| |Strafford County|    13| 99.515|  0.000|   360|  2755.812| 27.339| 130,633|
| |Belknap County|     4| 65.250|  0.000|   115|  1875.928| 13.982|  61,303|
| |Cheshire County|     3| 39.430|  1.878|    99|  1301.176| 13.143|  76,085|
| |Sullivan County|     1| 23.177|  0.000|    40|   927.085|  0.000|  43,146|
| |Grafton County|     1| 11.125|  0.000|   103|  1145.896|  0.000|  89,886|
| |Carroll County|     1| 20.446|  0.000|    94|  1921.897| 14.604|  48,910|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   385| 132.152| N/A|31,183| 10703.618| N/A|2,913,314|
| |Johnson County|   103| 170.982|  1.186| 5,800|  9628.138| 154.145| 602,401|
| |Wyandotte County|    99| 598.444|  2.591| 4,916| 29716.676| 329.015| 165,429|
| |Sedgwick County|    44| 85.264|  0.277| 4,945|  9582.553| 165.269| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,588|  8978.092| 124.382| 176,875|
| |Lyon County|    14| 421.750|  4.304|   710| 21388.763| 146.322|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,787| 49003.208| 184.119|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,088| 62107.737| 195.468|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,483| 18138.898| 101.344|  81,758|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 54.588|   5,234|
| |Coffey County|     8| 978.115|  0.000|    67|  8191.710|  0.000|   8,179|
| |Riley County|     5| 67.356|  0.000|   483|  6506.628| 63.507|  74,232|
| |Saline County|     5| 92.210|  0.000|   384|  7081.735| 108.018|  54,224|
| |Montgomery County|     5| 157.089|  0.000|   170|  5341.041| 40.394|  31,829|
| |Douglas County|     5| 40.897|  1.168|   744|  6085.442| 75.951| 122,259|
| |Seward County|     4| 186.672|  0.000| 1,220| 56934.852| 213.339|  21,428|
| |Sumner County|     3| 131.372|  0.000|   101|  4422.841| 18.767|  22,836|
| |Barton County|     3| 116.374|  0.000|   139|  5391.986| 127.457|  25,779|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Bourbon County|     2| 137.608|  9.829|    79|  5435.530| 58.975|  14,534|
| |Grant County|     2| 279.720|  0.000|   114| 15944.056| 339.660|   7,150|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 35.705|   8,002|
| |Cowley County|     2| 57.293|  0.000|   173|  4955.884| 61.386|  34,908|
| |Geary County|     2| 63.151|  0.000|   148|  4673.192| 90.216|  31,670|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stafford County|     1| 240.616| 34.374|     5|  1203.080| 68.747|   4,156|
| |Stanton County|     1| 498.504|  0.000|    20|  9970.090| 284.860|   2,006|
| |Jewell County|     1| 347.343| 49.620|    12|  4168.114| 99.241|   2,879|
| |Harvey County|     1| 29.045|  0.000|   204|  5925.237| 145.226|  34,429|
| |Franklin County|     1| 39.148|  0.000|   178|  6968.368| 128.630|  25,544|
| |Jackson County|     1| 75.924|  0.000|   148| 11236.808| 43.385|  13,171|
| |Kearny County|     1| 260.552|  0.000|    63| 16414.799| 223.331|   3,838|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199| 71.644|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   129|  6469.733| 365.400|  19,939|
| |Dickinson County|     1| 54.154|  0.000|    48|  2599.372| 38.681|  18,466|
| |Ellis County|     1| 35.023|  0.000|   145|  5078.275| 60.039|  28,553|
| |Reno County|     1| 16.130|  0.000|   284|  4580.793| 129.036|  61,998|
| |Nemaha County|     1| 97.742|  0.000|    49|  4789.366| 13.963|  10,231|
| |McPherson County|     1| 35.036|  0.000|   148|  5185.341| 90.093|  28,542|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 48.084|  11,884|
| |Labette County|     1| 50.974|  7.282|   138|  7034.356| 203.894|  19,618|
| |Crawford County|     1| 25.761|  0.000|   385|  9918.079| 29.441|  38,818|
| |Butler County|     1| 14.945|  2.135|   278|  4154.773| 134.507|  66,911|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 58.072|   4,920|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818|  0.000|   2,750|
| |Neosho County|     0|  0.000|  0.000|    65|  4060.723| 107.096|  16,007|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 50.272|   8,525|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Osage County|     0|  0.000|  0.000|    41|  2570.694| 26.871|  15,949|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 82.445|   6,931|
| |Thomas County|     0|  0.000|  0.000|    39|  5014.787| 128.584|   7,777|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 52.090|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    16|  2704.073| 24.144|   5,917|
| |Scott County|     0|  0.000|  0.000|    52| 10781.671| 710.879|   4,823|
| |Russell County|     0|  0.000|  0.000|    16|  2333.722| 62.510|   6,856|
| |Rush County|     0|  0.000|  0.000|     6|  1976.285|  0.000|   3,036|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 134.813|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   108|  4429.316| 17.577|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     8|  1247.272| 22.273|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    35|  6136.045| 125.225|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Mitchell County|     0|  0.000|  0.000|    27|  4515.805|  0.000|   5,979|
| |Comanche County|     0|  0.000|  0.000|     6|  3529.412| 252.101|   1,700|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 37.594|   7,600|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Miami County|     0|  0.000|  0.000|   134|  3913.894| 58.416|  34,237|
| |Meade County|     0|  0.000|  0.000|    45| 11157.947| 177.110|   4,033|
| |Anderson County|     0|  0.000|  0.000|    31|  3945.024| 36.360|   7,858|
| |Atchison County|     0|  0.000|  0.000|    64|  3981.833| 17.776|  16,073|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Morris County|     0|  0.000|  0.000|    12|  2135.231| 76.258|   5,620|
| |Allen County|     0|  0.000|  0.000|    20|  1616.946| 57.748|  12,369|
| |Cloud County|     0|  0.000|  0.000|    37|  4211.245| 113.817|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     3|  1129.093| 53.766|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Chase County|     0|  0.000|  0.000|    48| 18126.888| 755.287|   2,648|
| |Brown County|     0|  0.000|  0.000|    40|  4182.350| 119.496|   9,564|
| |Marshall County|     0|  0.000|  0.000|    10|  1030.184| 14.717|   9,707|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Linn County|     0|  0.000|  0.000|    40|  4122.436| 73.615|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 115.440|   2,475|
| |Kingman County|     0|  0.000|  0.000|    21|  2936.242| 219.719|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    76|  3990.968| 45.011|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Harper County|     0|  0.000|  0.000|    12|  2207.506| 78.839|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    38| 14966.522| 56.265|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 95.525|   5,982|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Gray County|     0|  0.000|  0.000|    77| 12859.051| 143.143|   5,988|
| |Graham County|     0|  0.000|  0.000|    17|  6849.315| 57.557|   2,482|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176|  0.000|   2,636|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495| 70.235|   6,102|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   357| 84.643| N/A|21,488|  5094.675| N/A|4,217,737|
| |Multnomah County|    96| 118.102|  0.527| 4,960|  6101.949| 81.371| 812,855|
| |Marion County|    70| 201.255|  0.821| 2,938|  8446.946| 101.038| 347,818|
| |Clackamas County|    40| 95.651|  1.366| 1,549|  3704.085| 43.726| 418,187|
| |Umatilla County|    28| 359.205|  7.331| 2,302| 29531.751| 443.508|  77,950|
| |Washington County|    25| 41.556|  0.475| 3,119|  5184.577| 64.116| 601,592|
| |Malheur County|    14| 457.950| 18.692|   804| 26299.434| 598.139|  30,571|
| |Yamhill County|    13| 121.382|  2.668|   467|  4360.411| 108.043| 107,100|
| |Polk County|    12| 139.397|  0.000|   319|  3705.640| 38.168|  86,085|
| |Deschutes County|    10| 50.584|  1.445|   611|  3090.666| 51.306| 197,692|
| |Linn County|    10| 77.072|  0.000|   284|  2188.842| 33.031| 129,749|
| |Lincoln County|     9| 180.137|  0.000|   418|  8366.358| 65.764|  49,962|
| |Benton County|     6| 64.479|  0.000|   169|  1816.169| 18.423|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   371| 15045.827| 347.612|  24,658|
| |Wasco County|     3| 112.435|  0.000|   192|  7195.862| 117.789|  26,682|
| |Morrow County|     3| 258.554| 24.624|   372| 32060.674| 824.910|  11,603|
| |Lane County|     3|  7.852|  0.000|   590|  1544.232| 25.052| 382,067|
| |Jackson County|     2|  9.052|  0.647|   473|  2140.814| 51.080| 220,944|
| |Josephine County|     2| 22.861|  1.633|   115|  1314.481| 13.063|  87,487|
| |Klamath County|     2| 29.309|  2.094|   201|  2945.573| 10.468|  68,238|
| |Union County|     2| 74.530|  0.000|   394| 14682.318| 31.941|  26,835|
| |Wallowa County|     1| 138.735|  0.000|    19|  2635.960|  0.000|   7,208|
| |Crook County|     1| 40.977|  0.000|    49|  2007.868| 35.123|  24,404|
| |Douglas County|     1|  9.011|  0.000|   151|  1360.606| 21.883| 110,980|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 80.257|   1,780|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582| 21.136|  27,036|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Baker County|     0|  0.000|  0.000|    40|  2480.774| 62.019|  16,124|
| |Clatsop County|     0|  0.000|  0.000|    85|  2113.166| 10.655|  40,224|
| |Columbia County|     0|  0.000|  0.000|    97|  1852.772| 49.116|  52,354|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137| 13.292|  64,487|
| |Curry County|     0|  0.000|  0.000|    15|   654.308|  6.232|  22,925|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Harney County|     0|  0.000|  0.000|    10|  1352.631| 38.647|   7,393|
| |Hood River County|     0|  0.000|  0.000|   193|  8254.213| 146.633|  23,382|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   348| 179.900| N/A|28,541| 14754.385| N/A|1,934,408|
| |Douglas County|   133| 232.791|  0.500|11,354| 19873.032| 185.783| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,746| 28458.266| 67.525|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,928| 96274.843| 192.607|  20,026|
| |Lancaster County|    17| 53.277|  0.895| 3,312| 10379.517| 80.139| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   100| 10725.011| 61.286|   9,324|
| |Adams County|    11| 350.732|  0.000|   358| 11414.724| 63.769|  31,363|
| |Sarpy County|    11| 58.762|  3.816| 2,290| 12233.167| 172.470| 187,196|
| |Dodge County|    10| 273.486|  7.814|   817| 22343.771| 164.091|  36,565|
| |Dawson County|     9| 381.437|  0.000|   961| 40728.968| 72.655|  23,595|
| |Perkins County|     7| 2421.308| 296.487|    18|  6226.219| 49.414|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   301|  8450.783| 48.130|  35,618|
| |Madison County|     5| 142.454|  0.000|   461| 13134.277| 166.875|  35,099|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747| 22.166|   6,445|
| |Colfax County|     4| 373.518|  0.000|   703| 65645.719| 106.719|  10,709|
| |Thurston County|     4| 553.710|  0.000|   205| 28377.630| 59.326|   7,224|
| |Gage County|     4| 185.934|  0.000|    90|  4183.517| 53.124|  21,513|
| |Custer County|     4| 371.161|  0.000|    48|  4453.930| 66.279|  10,777|
| |Platte County|     3| 89.633|  0.000|   797| 23812.369| 128.046|  33,470|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556| 25.347|   5,636|
| |Cass County|     2| 76.196| 10.885|   180|  6857.665| 108.852|  26,248|
| |Lincoln County|     2| 57.284|  0.000|   125|  3580.226| 126.842|  34,914|
| |Saunders County|     2| 92.687|  0.000|   161|  7461.303| 145.651|  21,578|
| |Saline County|     2| 140.607|  0.000|   597| 41971.316| 150.651|  14,224|
| |Seward County|     1| 57.857|  0.000|   122|  7058.551| 181.836|  17,284|
| |Washington County|     1| 48.242|  0.000|   126|  6078.441| 124.050|  20,729|
| |Richardson County|     1| 127.146|  0.000|    23|  2924.348| 54.491|   7,865|
| |Antelope County|     1| 158.781|  0.000|    19|  3016.831|  0.000|   6,298|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Fillmore County|     1| 183.083|  0.000|    24|  4393.995|  0.000|   5,462|
| |Buffalo County|     1| 20.137|  0.000|   435|  8759.741| 224.387|  49,659|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 46.061|   6,203|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Chase County|     0|  0.000|  0.000|     7|  1783.894| 36.406|   3,924|
| |Cedar County|     0|  0.000|  0.000|    22|  2618.424| 17.003|   8,402|
| |Cuming County|     0|  0.000|  0.000|    67|  7574.045| 129.195|   8,846|
| |Butler County|     0|  0.000|  0.000|    60|  7485.030| 71.286|   8,016|
| |Burt County|     0|  0.000|  0.000|    40|  6192.909| 331.763|   6,459|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Boyd County|     0|  0.000|  0.000|     5|  2605.524| 297.774|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    12|  1112.863| 13.248|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832|  0.000|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Banner County|     0|  0.000|  0.000|     3|  4026.846| 191.755|     745|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827| 79.631|   1,794|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 33.265|   8,589|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Franklin County|     0|  0.000|  0.000|    12|  4028.197| 143.864|   2,979|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739|  0.000|   1,990|
| |Garfield County|     0|  0.000|  0.000|     4|  2031.488| 72.553|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 121.271|   2,356|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759| 105.274|   1,357|
| |Red Willow County|     0|  0.000|  0.000|    17|  1585.229| 13.321|  10,724|
| |Polk County|     0|  0.000|  0.000|    27|  5179.359| 82.212|   5,213|
| |Pierce County|     0|  0.000|  0.000|    21|  2937.885| 59.957|   7,148|
| |Phelps County|     0|  0.000|  0.000|    40|  4427.718| 63.253|   9,034|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317| 54.672|   2,613|
| |Otoe County|     0|  0.000|  0.000|    53|  3310.017| 89.219|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    33|  4733.219| 245.881|   6,972|
| |Nance County|     0|  0.000|  0.000|     8|  2273.373|  0.000|   3,519|
| |Morrill County|     0|  0.000|  0.000|    58| 12494.614|  0.000|   4,642|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    36|  4320.691| 68.582|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    23|  2862.833| 71.126|   8,034|
| |Kearney County|     0|  0.000|  0.000|    53|  8160.123| 417.904|   6,495|
| |Sheridan County|     0|  0.000|  0.000|    11|  2096.836| 54.463|   5,246|
| |Merrick County|     0|  0.000|  0.000|    62|  7994.842| 147.370|   7,755|
| |Johnson County|     0|  0.000|  0.000|    14|  2760.797| 28.171|   5,071|
| |Jefferson County|     0|  0.000|  0.000|    17|  2412.716| 60.825|   7,046|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 28.554|   5,003|
| |Stanton County|     0|  0.000|  0.000|    32|  5405.405| 96.525|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Thomas County|     0|  0.000|  0.000|     1|  1385.042|  0.000|     722|
| |Valley County|     0|  0.000|  0.000|    10|  2405.002|  0.000|   4,158|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 28.381|  10,067|
| |Sherman County|     0|  0.000|  0.000|    11|  3665.445| 95.206|   3,001|
| |York County|     0|  0.000|  0.000|    80|  5848.381| 83.548|  13,679|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139| 182.448|     783|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Wayne County|     0|  0.000|  0.000|    37|  3942.461| 30.444|   9,385|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   284| 88.585| N/A|35,288| 11007.006| N/A|3,205,958|
| |Salt Lake County|   196| 168.902|  2.216|20,748| 17879.471| 146.743|1,160,437|
| |Utah County|    37| 58.155|  0.449| 8,794| 13821.937| 167.728| 636,235|
| |San Juan County|    25| 1633.133|  9.332|   650| 42461.458| 205.308|  15,308|
| |Davis County|    21| 59.075|  2.411| 3,232|  9091.906| 82.785| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   568| 16661.289| 146.666|  34,091|
| |Summit County|     1| 23.728|  0.000|   713| 16917.784| 54.235|  42,145|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Tooele County|     0|  0.000|  0.000|   583|  8068.199| 71.173|  72,259|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   239| 133.739| N/A|25,099| 14044.817| N/A|1,787,065|
| |Ada County|    83| 172.347|  5.636| 9,144| 18987.223| 318.886| 481,587|
| |Canyon County|    48| 208.833|  6.837| 5,869| 25534.155| 565.589| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,430| 16459.863| 315.714|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   161|  3984.360| 95.455|  40,408|
| |Kootenai County|    16| 96.562|  2.586| 1,792| 10814.921| 148.291| 165,697|
| |Blaine County|     6| 260.632|  0.000|   577| 25064.072| 43.439|  23,021|
| |Jerome County|     6| 245.781|  0.000|   483| 19785.351| 292.596|  24,412|
| |Bonneville County|     4| 33.596|  2.400| 1,075|  9028.909| 361.156| 119,062|
| |Washington County|     3| 294.291| 14.014|   209| 20502.256| 252.249|  10,194|
| |Elmore County|     3| 109.047|  0.000|   213|  7742.358| 62.313|  27,511|
| |Owyhee County|     3| 253.743| 24.166|   265| 22413.939| 326.241|  11,823|
| |Payette County|     2| 83.504|  0.000|   394| 16450.253| 304.192|  23,951|
| |Minidoka County|     2| 95.062|  0.000|   480| 22814.773| 244.444|  21,039|
| |Bingham County|     2| 42.725|  0.000|   254|  5426.075| 204.470|  46,811|
| |Bannock County|     2| 22.777|  0.000|   400|  4555.394| 143.170|  87,808|
| |Shoshone County|     2| 155.255|  0.000|   100|  7762.770| 243.973|  12,882|
| |Valley County|     1| 87.781|  0.000|    61|  5354.635| 175.562|  11,392|
| |Boise County|     1| 127.698|  0.000|    50|  6384.881| 200.668|   7,831|
| |Cassia County|     1| 41.615|  0.000|   525| 21847.690| 249.688|  24,030|
| |Gem County|     1| 55.212|  7.887|   180|  9938.163| 165.636|  18,112|
| |Gooding County|     1| 65.880|  0.000|   169| 11133.803| 254.110|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   201|  6728.934| 263.036|  29,871|
| |Idaho County|     0|  0.000|  0.000|    32|  1919.962| 17.143|  16,667|
| |Fremont County|     0|  0.000|  0.000|    85|  6489.045| 239.931|  13,099|
| |Boundary County|     0|  0.000|  0.000|    36|  2939.976| 23.333|  12,245|
| |Bonner County|     0|  0.000|  0.000|   183|  4000.962| 84.329|  45,739|
| |Benewah County|     0|  0.000|  0.000|    64|  6883.201| 107.550|   9,298|
| |Bear Lake County|     0|  0.000|  0.000|    17|  2775.510| 233.236|   6,125|
| |Adams County|     0|  0.000|  0.000|    19|  4424.779| 33.269|   4,294|
| |Latah County|     0|  0.000|  0.000|   102|  2543.134| 49.865|  40,108|
| |Lewis County|     0|  0.000|  0.000|     1|   260.552|  0.000|   3,838|
| |Lemhi County|     0|  0.000|  0.000|    25|  3114.489| 231.362|   8,027|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 51.476|  13,876|
| |Custer County|     0|  0.000|  0.000|    10|  2317.497| 99.321|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 32.631|   8,756|
| |Clark County|     0|  0.000|  0.000|     8|  9467.456| 845.309|     845|
| |Caribou County|     0|  0.000|  0.000|    32|  4472.397| 179.695|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Teton County|     0|  0.000|  0.000|    83|  6835.777| 258.842|  12,142|
| |Lincoln County|     0|  0.000|  0.000|    59| 10995.155| 159.736|   5,366|
| |Power County|     0|  0.000|  0.000|    57|  7420.909| 260.383|   7,681|
| |Oneida County|     0|  0.000|  0.000|    14|  3089.826| 157.644|   4,531|
| |Madison County|     0|  0.000|  0.000|   170|  4259.904| 125.291|  39,907|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   146| 165.035| N/A| 9,663| 10922.853| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  2.959| 4,437| 22973.687| 150.894| 193,134|
| |Pennington County|    32| 281.257|  3.767|   896|  7875.192| 64.036| 113,775|
| |Beadle County|     9| 487.726|  0.000|   594| 32189.888| 54.192|  18,453|
| |Todd County|     5| 491.304| 14.037|    69|  6779.994| 42.112|  10,177|
| |Union County|     4| 251.067|  0.000|   216| 13557.620| 152.434|  15,932|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556| 72.812|   1,962|
| |Brown County|     3| 77.242|  0.000|   446| 11483.303| 132.415|  38,839|
| |Yankton County|     2| 87.665|  0.000|   117|  5128.430| 93.927|  22,814|
| |Oglala Lakota County|     2| 141.074| 10.077|   156| 11003.738| 70.537|  14,177|
| |Hughes County|     2| 114.116|  0.000|    93|  5306.402| 73.360|  17,526|
| |Lake County|     2| 156.287|  0.000|    94|  7345.472| 111.633|  12,797|
| |Lincoln County|     2| 32.718|  0.000|   642| 10502.552| 147.232|  61,128|
| |Lyman County|     2| 528.961|  0.000|    90| 23803.227| 75.566|   3,781|
| |Roberts County|     1| 96.209|  0.000|    80|  7696.748| 137.442|  10,394|
| |Codington County|     1| 35.703|  5.100|   137|  4891.285| 91.807|  28,009|
| |Davison County|     1| 50.569|  7.224|    97|  4905.183| 65.017|  19,775|
| |Faulk County|     1| 434.972|  0.000|    27| 11744.237| 62.139|   2,299|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474| 42.720|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |Brookings County|     1| 28.509|  0.000|   139|  3962.711| 77.381|  35,077|
| |McCook County|     1| 179.019|  0.000|    29|  5191.550| 127.871|   5,586|
| |Meade County|     1| 35.296|  0.000|    94|  3317.803| 90.761|  28,332|
| |Butte County|     1| 95.886|  0.000|    18|  1725.956| 95.886|  10,429|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Spink County|     0|  0.000|  0.000|    26|  4077.792| 112.027|   6,376|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Turner County|     0|  0.000|  0.000|    52|  6202.290| 136.314|   8,384|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 1399.544|   2,756|
| |Douglas County|     0|  0.000|  0.000|    17|  5819.925| 48.907|   2,921|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Brule County|     0|  0.000|  0.000|    45|  8495.375| 134.847|   5,297|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233| 103.821|   1,376|
| |Charles Mix County|     0|  0.000|  0.000|   104| 11192.424| 61.497|   9,292|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Clay County|     0|  0.000|  0.000|   130|  9239.517| 121.840|  14,070|
| |Corson County|     0|  0.000|  0.000|    34|  8321.096| 174.813|   4,086|
| |Custer County|     0|  0.000|  0.000|    36|  4012.483| 206.993|   8,972|
| |Day County|     0|  0.000|  0.000|    23|  4240.413| 52.676|   5,424|
| |Deuel County|     0|  0.000|  0.000|    11|  2528.154| 98.500|   4,351|
| |Dewey County|     0|  0.000|  0.000|    48|  8146.640|  0.000|   5,892|
| |Edmunds County|     0|  0.000|  0.000|    16|  4178.637| 111.928|   3,829|
| |Hutchinson County|     0|  0.000|  0.000|    29|  3977.507| 39.187|   7,291|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 127.684|   6,713|
| |Grant County|     0|  0.000|  0.000|    27|  3828.701| 81.031|   7,052|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    22|  3569.111| 185.408|   6,164|
| |Hand County|     0|  0.000|  0.000|     8|  2507.051| 44.769|   3,191|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668|  0.000|   3,453|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Hyde County|     0|  0.000|  0.000|     3|  2305.919|  0.000|   1,301|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582|  0.000|   4,939|
| |Lawrence County|     0|  0.000|  0.000|    60|  2321.622| 154.775|  25,844|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159|  0.000|   2,751|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 60.049|   2,379|
| |Marshall County|     0|  0.000|  0.000|     9|  1823.708| 28.948|   4,935|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   141| 78.677| N/A| 7,757|  4328.328| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  2.406|   938|  5265.994| 69.775| 178,124|
| |Jackson County|    19| 664.894|  0.000|   165|  5774.076| 39.994|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   698|  5857.130| 49.149| 119,171|
| |Mercer County|    11| 187.209| 19.450|   200|  3403.792| 85.095|  58,758|
| |Wayne County|     9| 228.415|  0.000|   210|  5329.679| 90.641|  39,402|
| |Fayette County|     7| 165.071|  6.738|   151|  3560.817| 67.376|  42,406|
| |Mingo County|     5| 213.456| 18.296|   173|  7385.587| 237.851|  23,424|
| |Monongalia County|     5| 47.343|  0.000|   945|  8947.847| 27.053| 105,612|
| |Wood County|     5| 59.867|  1.710|   250|  2993.367| 23.947|  83,518|
| |Preston County|     4| 119.646|  4.273|   125|  3738.933|  4.273|  33,432|
| |Ohio County|     4| 96.593|  0.000|   269|  6495.859| 48.296|  41,411|
| |Mineral County|     4| 148.876|  0.000|   123|  4577.937| 53.170|  26,868|
| |Logan County|     4| 124.926|  4.462|   234|  7308.161| 356.931|  32,019|
| |Jefferson County|     4| 69.996|  0.000|   296|  5179.715|  9.999|  57,146|
| |Greenbrier County|     3| 86.550|  0.000|    93|  2683.053| 24.729|  34,662|
| |Cabell County|     3| 32.628|  1.554|   404|  4393.931| 102.546|  91,945|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097| 17.962|  15,907|
| |Marion County|     2| 35.668|  0.000|   191|  3406.335| 30.573|  56,072|
| |Raleigh County|     1| 13.631|  0.000|   255|  3475.961| 114.892|  73,361|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Brooke County|     1| 45.581|  0.000|    64|  2917.179| 13.023|  21,939|
| |Pleasants County|     1| 134.048| 19.150|    13|  1742.627| 95.749|   7,460|
| |Pendleton County|     1| 143.493|  0.000|    41|  5883.197| 61.497|   6,969|
| |Roane County|     1| 73.057|  0.000|    15|  1095.850| 10.437|  13,688|
| |Grant County|     1| 86.445| 12.349|   121| 10459.889| 493.974|  11,568|
| |Mason County|     1| 37.713|  0.000|    56|  2111.932| 37.713|  26,516|
| |Harrison County|     1| 14.869|  0.000|   226|  3360.295| 59.474|  67,256|
| |Hampshire County|     1| 43.150|  0.000|    76|  3279.396| 12.329|  23,175|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656| 16.791|   8,508|
| |Marshall County|     1| 32.754|  4.679|   131|  4290.721| 18.716|  30,531|
| |Wyoming County|     1| 49.034|  0.000|    34|  1667.157| 77.053|  20,394|
| |Taylor County|     1| 59.898|  8.557|    56|  3354.298| 25.671|  16,695|
| |Nicholas County|     1| 40.823|  0.000|    37|  1510.451| 29.159|  24,496|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533| 11.818|  24,176|
| |Boone County|     0|  0.000|  0.000|   101|  4707.089| 146.472|  21,457|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Putnam County|     0|  0.000|  0.000|   195|  3454.384| 58.206|  56,450|
| |Pocahontas County|     0|  0.000|  0.000|    41|  4971.505|  0.000|   8,247|
| |Summers County|     0|  0.000|  0.000|    12|   954.426| 56.811|  12,573|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Wetzel County|     0|  0.000|  0.000|    43|  2854.298| 18.965|  15,065|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Randolph County|     0|  0.000|  0.000|   210|  7318.348| 14.935|  28,695|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Lincoln County|     0|  0.000|  0.000|    88|  4311.823| 139.994|  20,409|
| |Morgan County|     0|  0.000|  0.000|    29|  1621.561| 23.964|  17,884|
| |McDowell County|     0|  0.000|  0.000|    64|  3631.412| 162.117|  17,624|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |Gilmer County|     0|  0.000|  0.000|    17|  2173.079| 18.261|   7,823|
| |Tyler County|     0|  0.000|  0.000|    13|  1513.212| 16.629|   8,591|
| |Tucker County|     0|  0.000|  0.000|    10|  1462.202|  0.000|   6,839|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 33.820|   8,448|
| |Hardy County|     0|  0.000|  0.000|    61|  4427.991| 72.590|  13,776|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 49.586|  28,810|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   125| 92.991| N/A| 4,049|  3012.174| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,089|  7081.284| 15.012| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   675|  3250.803| 11.696| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   172|  1406.355|  3.504| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   565|  5218.098| 22.429| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   150|   985.882|  0.000| 152,148|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  3.592|  39,772|
| |Hancock County|     1| 18.186|  0.000|    36|   654.700|  5.196|  54,987|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Oxford County|     0|  0.000|  0.000|    54|   931.436|  0.000|  57,975|
| |Piscataquis County|     0|  0.000|  0.000|     4|   238.308|  8.511|  16,785|
| |Washington County|     0|  0.000|  0.000|    13|   414.290| 18.211|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    56|  1561.803| 19.921|  35,856|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   113| 148.282| N/A| 7,694| 10096.291| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,046| 16743.347| 89.520| 181,923|
| |Burleigh County|     6| 62.744|  1.494| 1,201| 12559.346| 331.649|  95,626|
| |Grand Forks County|     6| 86.392|  2.057|   683|  9834.272| 94.620|  69,451|
| |Stutsman County|     3| 144.900|  6.900|   127|  6134.080| 62.100|  20,704|
| |Stark County|     3| 95.271|  0.000|   264|  8383.880| 226.837|  31,489|
| |Morton County|     3| 95.651|  0.000|   383| 12211.453| 464.591|  31,364|
| |Williams County|     2| 53.207|  0.000|   272|  7236.160| 148.220|  37,589|
| |Ramsey County|     2| 173.626|  0.000|    70|  6076.916| 285.243|  11,519|
| |McIntosh County|     2| 800.961| 57.212|    37| 14817.781| 629.327|   2,497|
| |Benson County|     2| 292.740| 20.910|   137| 20052.693| 899.130|   6,832|
| |Sioux County|     1| 236.407| 33.772|    83| 19621.749| 810.537|   4,230|
| |Richland County|     1| 61.816|  8.831|   109|  6737.961| 141.294|  16,177|
| |Ward County|     1| 14.784|  0.000|   234|  3459.440| 90.816|  67,641|
| |Mountrail County|     1| 94.832|  0.000|   135| 12802.276| 216.758|  10,545|
| |Emmons County|     1| 308.547|  0.000|    17|  5245.295| 44.078|   3,241|
| |Griggs County|     1| 448.229| 64.033|    34| 15239.803| 256.131|   2,231|
| |McHenry County|     1| 174.064|  0.000|    17|  2959.095| 49.733|   5,745|
| |McKenzie County|     1| 66.560|  0.000|    90|  5990.415| 104.595|  15,024|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Nelson County|     0|  0.000|  0.000|    26|  9030.914| 396.963|   2,879|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |Barnes County|     0|  0.000|  0.000|    39|  3744.599| 68.582|  10,415|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Bowman County|     0|  0.000|  0.000|     8|  2645.503| 94.482|   3,024|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704| 67.545|   2,115|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Dickey County|     0|  0.000|  0.000|    13|  2668.309| 58.644|   4,872|
| |Divide County|     0|  0.000|  0.000|     2|   883.392| 63.099|   2,264|
| |Dunn County|     0|  0.000|  0.000|    30|  6781.193|  0.000|   4,424|
| |Eddy County|     0|  0.000|  0.000|    18|  7870.573| 312.324|   2,287|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641|  0.000|   2,327|
| |Rolette County|     0|  0.000|  0.000|    73|  5149.549| 393.018|  14,176|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418| 36.649|   3,898|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 434.546|   1,315|
| |Slope County|     0|  0.000|  0.000|     3|  4000.000|  0.000|     750|
| |Steele County|     0|  0.000|  0.000|    14|  7407.407| 226.757|   1,890|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Traill County|     0|  0.000|  0.000|    55|  6844.201| 159.994|   8,036|
| |Walsh County|     0|  0.000|  0.000|   104|  9773.518| 80.551|  10,641|
| |Wells County|     0|  0.000|  0.000|    21|  5477.308| 149.042|   3,834|
| |Foster County|     0|  0.000|  0.000|    26|  8099.688| 311.526|   3,210|
| |Golden Valley County|     0|  0.000|  0.000|     5|  2839.296| 81.123|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Kidder County|     0|  0.000|  0.000|    18|  7258.065| 403.226|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 70.616|   4,046|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784| 77.220|   1,850|
| |McLean County|     0|  0.000|  0.000|    72|  7619.048| 498.866|   9,450|
| |Mercer County|     0|  0.000|  0.000|    29|  3542.201| 104.696|   8,187|
| |Pierce County|     0|  0.000|  0.000|    12|  3018.868| 35.939|   3,975|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    75| 70.174| N/A| 5,017|  4694.146| N/A|1,068,778|
| |Yellowstone County|    30| 185.989|  2.657| 1,295|  8028.518| 163.847| 161,300|
| |Big Horn County|    13| 976.049| 21.452|   437| 32810.271| 954.598|  13,319|
| |Toole County|     6| 1266.892|  0.000|    45|  9501.689| 422.297|   4,736|
| |Cascade County|     4| 49.161|  3.511|   166|  2040.164| 28.092|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   947|  8275.513| 98.622| 114,434|
| |Lincoln County|     2| 100.100|  0.000|    77|  3853.854| 50.050|  19,980|
| |Hill County|     2| 121.330| 17.333|    42|  2547.925| 17.333|  16,484|
| |Flathead County|     2| 19.267|  0.000|   347|  3342.774| 115.600| 103,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 112.762|  11,402|
| |Richland County|     2| 185.134| 13.224|    47|  4350.643| 13.224|  10,803|
| |Missoula County|     1|  8.361|  0.000|   332|  2775.920| 77.640| 119,600|
| |Madison County|     1| 116.279|  0.000|    84|  9767.442| 132.890|   8,600|
| |Rosebud County|     1| 111.894|  0.000|    34|  3804.409| 191.819|   8,937|
| |Lewis and Clark County|     1| 14.403|  0.000|   158|  2275.608| 47.323|  69,432|
| |Ravalli County|     1| 22.828|  0.000|    83|  1894.718| 32.611|  43,806|
| |Lake County|     1| 32.832|  0.000|   181|  5942.609| 79.735|  30,458|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972| 38.228|   3,737|
| |Stillwater County|     1| 103.713| 14.816|    26|  2696.536| 103.713|   9,642|
| |Glacier County|     1| 72.711|  0.000|    76|  5526.067| 186.972|  13,753|
| |McCone County|     0|  0.000|  0.000|     3|  1802.885| 171.703|   1,664|
| |Deer Lodge County|     0|  0.000|  0.000|    25|  2735.230| 78.149|   9,140|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Jefferson County|     0|  0.000|  0.000|    29|  2372.965| 23.379|  12,221|
| |Granite County|     0|  0.000|  0.000|    16|  4735.129| 338.223|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fergus County|     0|  0.000|  0.000|    14|  1266.968| 90.498|  11,050|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Dawson County|     0|  0.000|  0.000|    17|  1973.761| 16.586|   8,613|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148| 84.531|   1,690|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 76.055|   5,635|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    19|  2568.956| 115.893|   7,396|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |Mineral County|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,397|
| |Park County|     0|  0.000|  0.000|    55|  3312.056| 25.808|  16,606|
| |Carbon County|     0|  0.000|  0.000|    71|  6620.047| 173.160|  10,725|
| |Blaine County|     0|  0.000|  0.000|    10|  1496.782| 21.383|   6,681|
| |Silver Bow County|     0|  0.000|  0.000|    95|  2720.894| 118.656|  34,915|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 86.345|   3,309|
| |Sanders County|     0|  0.000|  0.000|     9|   743.003|  0.000|  12,113|
| |Roosevelt County|     0|  0.000|  0.000|    23|  2090.149| 51.929|  11,004|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505| 132.644|   1,077|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 48.336|   5,911|
| |Phillips County|     0|  0.000|  0.000|    28|  7081.437| 1011.634|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Beaverhead County|     0|  0.000|  0.000|    64|  6770.337| 256.910|   9,453|
| |Broadwater County|     0|  0.000|  0.000|    12|  1924.002| 22.905|   6,237|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,454|  2330.169| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   730|  4457.362|  7.851| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  2.892|  49,402|
| |Windham County|     3| 71.053|  0.000|   102|  2415.802|  3.383|  42,222|
| |Addison County|     2| 54.382|  0.000|    73|  1984.936|  3.884|  36,777|
| |Washington County|     2| 34.241|  0.000|    53|   907.394|  9.783|  58,409|
| |Windsor County|     2| 36.323|  0.000|    72|  1307.617|  2.594|  55,062|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Rutland County|     1| 17.185|  0.000|   100|  1718.479| 27.005|  58,191|
| |Bennington County|     1| 28.193|  0.000|    88|  2480.970| 16.110|  35,470|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|
| |Orange County|     0|  0.000|  0.000|    14|   484.563|  0.000|  28,892|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    33| 23.307| N/A| 3,615|  2553.197| N/A|1,415,872|
| |Honolulu County|    27| 27.705| N/A| 3,249|  3333.802| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   186|  1110.998|  6.826| 167,417|
| |Hawaii County|     0|  0.000|  0.000|   131|   650.082|  9.925| 201,513|
| |Kauai County|     0|  0.000|  0.000|    49|   677.797|  3.952|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,042|  5256.074| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    23|  2723.505| 16.916|   8,445|
| |Park County|     0|  0.000|  0.000|   135|  4624.238| 88.081|  29,194|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Sheridan County|     0|  0.000|  0.000|    73|  2394.620| 56.234|  30,485|
| |Fremont County|     0|  0.000|  0.000|   497| 12658.873| 32.748|  39,261|
| |Goshen County|     0|  0.000|  0.000|    34|  2573.613| 162.202|  13,211|
| |Washakie County|     0|  0.000|  0.000|    77|  9865.471| 512.492|   7,805|
| |Teton County|     0|  0.000|  0.000|   370| 15768.837| 73.060|  23,464|
| |Sweetwater County|     0|  0.000|  0.000|   260|  6140.330| 33.738|  42,343|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 161.859|   4,413|
| |Albany County|     0|  0.000|  0.000|    86|  2211.934|  0.000|  38,880|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Natrona County|     0|  0.000|  0.000|   235|  2942.723| 32.200|  79,858|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565| 18.837|   7,584|
| |Laramie County|     0|  0.000|  0.000|   495|  4974.874| 22.972|  99,500|
| |Lincoln County|     0|  0.000|  0.000|   103|  5194.150| 79.245|  19,830|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Campbell County|     0|  0.000|  0.000|   124|  2675.816| 18.496|  46,341|
| |Carbon County|     0|  0.000|  0.000|   100|  6756.757| 173.745|  14,800|
| |Uinta County|     0|  0.000|  0.000|   277| 13695.244| 84.757|  20,226|
| |Sublette County|     0|  0.000|  0.000|    39|  3967.043| 29.063|   9,831|
| |Converse County|     0|  0.000|  0.000|    31|  2242.801|  0.000|  13,822|
| |Weston County|     0|  0.000|  0.000|     6|   866.176| 20.623|   6,927|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|17,860| 16859.220| N/A|1,059,361|
| |Kent County|     0|  0.000|  0.000| 1,494|  9093.565| 63.476| 164,292|
| |Providence County|     0|  0.000|  0.000|15,047| 23550.274| 111.347| 638,931|
| |Bristol County|     0|  0.000|  0.000|   316|  6518.286| 35.361|  48,479|
| |Washington County|     0|  0.000|  0.000|   607|  4833.688| 19.339| 125,577|
| |Newport County|     0|  0.000|  0.000|   396|  4824.444| 27.847|  82,082|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|


