# Analysis of US By County #

Updated: at 2020-08-08

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 128,559 deaths (445.363 deaths/million) and 4,254,008 confirmed cases (14736.983 confirmed cases/million).  This group accounts for 80.97% of all US deaths and for 87.55% of all US cases.

24.76% of this group's deaths (20.05% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.16% of this group's deaths (20.37% of the total US deaths) occured in 33 counties in 14 states with a combined population of 38,392,743 (11.70% of the total US population):



The next 24.98% of this group's deaths (20.23% of the total US deaths) occured in 87 counties in 30 states with a combined population of 67,315,197 (20.51% of the total US population)

The remaining 25.10% of this group's deaths (20.32% of the total US deaths) occured in 857 counties in 50 states with a combined population of 145,666,901 (44.38% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,767 deaths (246.782 deaths/million) and 437,049 confirmed cases (11042.875 confirmed cases/million).  This group accounts for 6.15% of all US deaths and for 8.99% of all US cases.

24.84% of this group's deaths (1.53% of the total US deaths) occured in 57 counties in 16 states with a combined population of 1,876,234 (0.57% of the total US population):



The next 25.14% of this group's deaths (1.55% of the total US deaths) occured in 111 counties in 27 states with a combined population of 3,328,397 (1.01% of the total US population):



The next 24.99% of this group's deaths (1.54% of the total US deaths) occured in 230 counties in 32 states with a combined population of 5,664,202 (1.73% of the total US population)

The remaining 25.03% of this group's deaths (1.54% of the total US deaths) occured in 1,754 counties in 47 states with a combined population of 28,708,631 (8.75% of the total US population) 

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
|NJ|21 counties|15,849| 1784.357| N/A|183,408| 20648.962| N/A|8,882,190|
| |Essex County| 2,107| 2637.129|  0.894|19,686| 24639.069| 35.403| 798,975|
| |Bergen County| 2,037| 2185.149|  0.000|20,694| 22199.051| 34.021| 932,202|
| |Hudson County| 1,502| 2233.819|  0.425|19,607| 29160.117| 27.408| 672,391|
| |Middlesex County| 1,401| 1698.054|  0.000|17,857| 21643.222| 31.859| 825,062|
| |Union County| 1,348| 2422.974|  0.257|16,636| 29902.524| 29.016| 556,341|
| |Passaic County| 1,239| 2468.983|  0.000|17,599| 35069.925| 48.395| 501,826|
| |Ocean County| 1,016| 1673.293|  0.471|10,564| 17398.293| 35.292| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,267| 16591.925| 48.481| 618,795|
| |Morris County|   827| 1681.424|  0.000| 7,224| 14687.554| 25.560| 491,845|
| |Mercer County|   618| 1681.953|  1.555| 8,104| 22055.902| 32.659| 367,430|
| |Camden County|   578| 1141.230|  1.410| 8,499| 16780.823| 55.849| 506,471|
| |Somerset County|   562| 1708.549|  3.474| 5,223| 15878.565| 19.978| 328,934|
| |Burlington County|   471| 1057.598|  0.642| 5,952| 13364.799| 54.853| 445,349|
| |Atlantic County|   252| 955.740|  1.084| 3,446| 13069.367| 44.428| 263,670|
| |Gloucester County|   209| 716.647|  0.980| 3,216| 11027.445| 76.906| 291,636|
| |Sussex County|   197| 1402.255|  2.034| 1,322|  9410.056| 27.455| 140,488|
| |Warren County|   171| 1624.441|  1.357| 1,340| 12729.535| 14.928| 105,267|
| |Cumberland County|   158| 1056.665|  0.955| 3,318| 22189.972| 98.406| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,146|  9214.367| 18.378| 124,371|
| |Salem County|    87| 1394.566|  9.160|   886| 14202.132| 48.088|  62,385|
| |Cape May County|    87| 945.251|  1.552|   822|  8930.997| 24.834|  92,039|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,316| 633.118| N/A|251,573| 12931.968| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,580| 32116.758| 39.691|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.193|43,681| 29582.128| 44.214|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.295|36,136| 37349.639| 29.974| 967,506|
| |Queens County|   984| 436.394|  0.719| 7,849|  3482.332| 17.734|2,253,858|
| |Kings County|   930| 363.113|  0.598| 1,347|   526.195|  2.680|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,925| 42742.388| 26.748| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,791|  9568.935| 46.494| 918,702|
| |Bronx County|   648| 457.227|  0.753|26,729| 18846.937| 95.981|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,129| 28910.999| 17.442| 384,940|
| |New York County|   414| 254.160|  0.418|15,416|  9464.933| 48.202|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 4,901|  6607.169| 36.785| 741,770|
| |Onondaga County|   200| 434.284|  1.861| 3,556|  7721.572| 28.539| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,589| 15597.278| 48.069| 294,218|
| |Richmond County|   148| 310.619|  0.511| 7,849| 16483.875| 83.947| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,573|  8422.093| 32.733| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,129|  9310.319| 36.859| 228,671|
| |Niagara County|    98| 468.270|  1.365| 1,491|  7124.393| 34.813| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,049| 11538.916| 22.526| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,115|  5853.387| 58.496| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,446| 14707.079| 36.325|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   297|  7360.230| 14.161|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,488| 19726.376| 15.151|  75,432|
| |Steuben County|    42| 440.349|  0.000|   297|  3113.893| 10.484|  95,379|
| |Columbia County|    37| 622.257|  0.000|   535|  8997.494| 45.648|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,055|  6793.347| 29.436| 155,299|
| |Ontario County|    34| 309.719|  0.000|   357|  3252.047| 10.411| 109,777|
| |Warren County|    33| 516.077|  0.000|   307|  4801.076| 15.639|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   759|  4782.187| 31.503| 158,714|
| |Tioga County|    25| 518.640|  2.964|   193|  4003.900| 17.782|  48,203|
| |Fulton County|    24| 449.581|  0.000|   293|  5488.639| 48.169|  53,383|
| |Greene County|    18| 381.453|  0.000|   291|  6166.822|  6.055|  47,188|
| |Madison County|    17| 239.636|  0.000|   412|  5807.643| 28.192|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   752|  3271.514| 22.995| 229,863|
| |Washington County|    14| 228.743|  0.000|   256|  4182.733|  4.668|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   249|  1962.129| 23.640| 126,903|
| |Livingston County|     8| 127.158|  0.000|   174|  2765.680| 20.436|  62,914|
| |Yates County|     7| 280.978|  0.000|    56|  2247.822| 17.203|  24,913|
| |Cattaraugus County|     6| 78.826|  0.000|   164|  2154.578| 11.261|  76,117|
| |Chenango County|     6| 127.100|  0.000|   215|  4554.409| 24.209|  47,207|
| |Wyoming County|     5| 125.442|  0.000|   116|  2910.259| 14.336|  39,859|
| |Otsego County|     5| 84.044|  0.000|   116|  1949.809|  9.605|  59,493|
| |Genesee County|     5| 87.291|  0.000|   277|  4835.894| 17.458|  57,280|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  3.978| 107,740|
| |Montgomery County|     4| 81.266|  0.000|   170|  3453.810| 46.438|  49,221|
| |Herkimer County|     4| 65.233|  0.000|   270|  4403.203| 72.222|  61,319|
| |Clinton County|     4| 49.699|  0.000|   127|  1577.934|  1.775|  80,485|
| |Delaware County|     4| 90.631|  0.000|   104|  2356.406|  6.474|  44,135|
| |Chemung County|     3| 35.947|  0.000|   168|  2013.037|  8.559|  83,456|
| |Oswego County|     3| 25.614|  0.000|   251|  2143.028| 12.197| 117,124|
| |Seneca County|     3| 88.194|  0.000|    87|  2557.620| 12.599|  34,016|
| |Wayne County|     3| 33.364|  0.000|   249|  2769.190|  6.355|  89,918|
| |Cayuga County|     2| 26.118|  0.000|   151|  1971.897| 14.924|  76,576|
| |Allegany County|     1| 21.696|  0.000|    79|  1714.001| 15.497|  46,091|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  8.023|  17,807|
| |Tompkins County|     0|  0.000|  0.000|   233|  2280.290|  6.990| 102,180|
| |Essex County|     0|  0.000|  0.000|    55|  1491.121|  0.000|  36,885|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525| 11.424|  50,022|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Jefferson County|     0|  0.000|  0.000|   140|  1274.651| 14.307| 109,834|
| |Lewis County|     0|  0.000|  0.000|    39|  1483.115| 27.163|  26,296|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Cortland County|     0|  0.000|  0.000|    95|  1996.595| 12.010|  47,581|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,133| 256.452| N/A|546,814| 13839.110| N/A|39,512,223|
| |Los Angeles County| 4,919| 489.984|  4.198|204,258| 20346.232| 223.654|10,039,107|
| |Riverside County|   799| 323.410|  6.014|40,452| 16373.708| 198.973|2,470,546|
| |Orange County|   704| 221.684|  3.869|38,754| 12203.325| 115.071|3,175,692|
| |San Diego County|   583| 174.638|  0.941|31,127|  9324.123| 88.967|3,338,330|
| |San Bernardino County|   497| 227.973|  5.766|34,939| 16026.439| 177.516|2,180,085|
| |Imperial County|   240| 1324.394| 23.650| 9,601| 52981.265| 185.257| 181,215|
| |Alameda County|   206| 123.255|  2.051|12,884|  7708.835| 149.154|1,671,329|
| |Tulare County|   196| 420.425|  5.516|10,475| 22469.138| 312.867| 466,195|
| |Santa Clara County|   196| 101.668|  0.371|11,336|  5880.119| 105.447|1,927,852|
| |San Joaquin County|   192| 251.920|  4.499|12,119| 15901.111| 119.212| 762,148|
| |Kern County|   160| 177.738|  3.174|22,009| 24448.957| 424.349| 900,202|
| |Fresno County|   157| 157.141|  2.717|16,625| 16639.959| 312.567| 999,101|
| |Sacramento County|   155| 99.867|  2.025|10,544|  6793.561| 66.640|1,552,058|
| |Stanislaus County|   151| 274.216| 12.193| 9,408| 17084.953| 134.384| 550,660|
| |Contra Costa County|   136| 117.899|  2.105| 8,760|  7594.107| 134.990|1,153,526|
| |San Mateo County|   120| 156.541|  0.186| 5,978|  7798.344| 94.856| 766,573|
| |Ventura County|    82| 96.926|  1.013| 8,035|  9497.569| 116.683| 846,006|
| |Marin County|    78| 301.361|  4.416| 5,257| 20310.942| 149.025| 258,826|
| |Santa Barbara County|    68| 152.296|  2.560| 6,652| 14898.130| 155.176| 446,499|
| |San Francisco County|    64| 72.599| N/A| 7,326|  8310.372| N/A| 881,549|
| |Merced County|    62| 223.279| 11.833| 4,855| 17484.154| 406.429| 277,680|
| |Kings County|    56| 366.157|  1.868| 4,453| 29115.993| 286.760| 152,940|
| |Sonoma County|    44| 89.008|  3.468| 3,358|  6792.951| 149.118| 494,336|
| |Yolo County|    42| 190.476|  0.648| 1,660|  7528.345| 97.182| 220,500|
| |Solano County|    39| 87.123|  0.638| 3,959|  8844.101| 111.058| 447,643|
| |Madera County|    36| 228.823|  5.448| 2,267| 14409.478| 294.201| 157,327|
| |Monterey County|    35| 80.634|  2.962| 5,156| 11878.515| 202.078| 434,061|
| |Placer County|    20| 50.210|  1.793| 2,099|  5269.513| 79.977| 398,329|
| |San Luis Obispo County|    16| 56.515|  0.505| 2,047|  7230.380| 133.214| 283,111|
| |Napa County|    10| 72.598|  2.074| 1,046|  7593.797| 163.865| 137,744|
| |Mendocino County|    10| 115.275|  1.647|   363|  4184.486| 83.986|  86,749|
| |Shasta County|     9| 49.978|  0.000|   411|  2282.319| 33.319| 180,080|
| |Butte County|     8| 36.499|  0.652| 1,060|  4836.075| 77.560| 219,186|
| |Sutter County|     6| 61.874|  0.000|   893|  9208.939| 203.301|  96,971|
| |Yuba County|     4| 50.847|  0.000|   572|  7271.063| 194.307|  78,668|
| |Santa Cruz County|     4| 14.641|  0.000| 1,229|  4498.322| 62.745| 273,213|
| |Colusa County|     4| 185.641|  0.000|   362| 16800.483| 258.571|  21,547|
| |San Benito County|     4| 63.686|  0.000|   699| 11129.156| 175.137|  62,808|
| |Humboldt County|     4| 29.508|  0.000|   280|  2065.537| 49.531| 135,558|
| |Glenn County|     3| 105.660| 10.063|   360| 12679.181| 176.100|  28,393|
| |Inyo County|     3| 166.306| 15.839|    86|  4767.448| 285.097|  18,039|
| |Lake County|     2| 31.063|  2.219|   220|  3416.892| 55.469|  64,386|
| |Mariposa County|     2| 116.259|  0.000|    60|  3487.764| 58.129|  17,203|
| |Tuolumne County|     2| 36.712|  0.000|   147|  2698.337| 15.734|  54,478|
| |Calaveras County|     1| 21.784|  0.000|   136|  2962.640| 34.232|  45,905|
| |Mono County|     1| 69.233|  0.000|   153| 10592.634| 108.795|  14,444|
| |Nevada County|     1| 10.025|  0.000|   321|  3217.884| 31.506|  99,755|
| |El Dorado County|     1|  5.186|  0.000|   716|  3712.865| 58.523| 192,843|
| |Tehama County|     1| 15.365|  0.000|   271|  4163.850| 96.578|  65,084|
| |Lassen County|     0|  0.000|  0.000|   638| 20868.086| 32.709|  30,573|
| |Modoc County|     0|  0.000|  0.000|     4|   452.438| 32.317|   8,841|
| |Plumas County|     0|  0.000|  0.000|    34|  1807.838|  7.596|  18,807|
| |Sierra County|     0|  0.000|  0.000|     3|   998.336| 47.540|   3,005|
| |Siskiyou County|     0|  0.000|  0.000|    92|  2113.048| 65.623|  43,539|
| |Del Norte County|     0|  0.000|  0.000|    96|  3451.747| 41.092|  27,812|
| |Trinity County|     0|  0.000|  0.000|     5|   407.000|  0.000|  12,285|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|
| |Amador County|     0|  0.000|  0.000|   162|  4075.267| 168.904|  39,752|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,702| 1262.531| N/A|119,875| 17392.085| N/A|6,892,503|
| |Middlesex County| 1,999| 1240.306|  1.861|26,254| 16289.642| 48.573|1,611,699|
| |Essex County| 1,191| 1509.441|  2.535|17,699| 22431.226| 84.552| 789,034|
| |Suffolk County| 1,071| 1332.244|  2.843|21,717| 27014.319| 87.963| 803,907|
| |Worcester County|   999| 1202.713|  1.548|13,555| 16319.096| 40.073| 830,622|
| |Norfolk County|   996| 1409.218|  2.426|10,554| 14932.616| 64.276| 706,775|
| |Plymouth County|   718| 1377.585|  2.193| 9,212| 17674.529| 34.536| 521,202|
| |Hampden County|   703| 1507.380|  2.144| 7,556| 16201.659| 46.560| 466,372|
| |Bristol County|   632| 1118.155|  2.275| 9,295| 16445.011| 56.110| 565,217|
| |Barnstable County|   157| 737.124|  0.671| 1,794|  8422.931| 32.865| 212,990|
| |Hampshire County|   129| 802.089|  1.776| 1,162|  7225.020| 31.977| 160,830|
| |Franklin County|    61| 869.194|  2.036|   410|  5842.120| 16.285|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392| 16.007| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 8,608| 296.870| N/A|491,304| 16943.924| N/A|28,995,881|
| |Harris County| 1,514| 321.217| 23.762|83,183| 17648.475| 309.821|4,713,325|
| |Hidalgo County|   790| 909.398| 24.009|19,534| 22486.293| 415.725| 868,707|
| |Dallas County|   746| 283.057|  4.065|53,291| 20220.329| 179.688|2,635,516|
| |Bexar County|   739| 368.845| 11.480|42,299| 21111.984| 106.668|2,003,554|
| |Tarrant County|   437| 207.846|  4.892|30,650| 14577.779| 192.083|2,102,515|
| |Cameron County|   415| 980.710| 30.383|15,865| 37491.463| 1927.660| 423,163|
| |Travis County|   295| 231.563|  7.401|22,480| 17645.849| 225.956|1,273,954|
| |El Paso County|   286| 340.785|  8.341|15,908| 18955.290| 277.803| 839,238|
| |Nueces County|   229| 632.083| 20.899|13,918| 38416.314| 637.604| 362,294|
| |Fort Bend County|   158| 194.656|  3.168| 9,151| 11274.036| 364.144| 811,688|
| |Webb County|   155| 560.271| 42.859| 7,540| 27254.457| 858.221| 276,652|
| |Galveston County|   111| 324.430|  6.681| 9,291| 27155.630| 237.999| 342,139|
| |Williamson County|    90| 152.400|  2.661| 6,245| 10574.870| 128.210| 590,551|
| |Collin County|    89| 86.013|  2.485| 7,268|  7024.055| 140.133|1,034,730|
| |Brazoria County|    88| 235.128|  8.016| 7,090| 18943.847| 269.481| 374,264|
| |Denton County|    84| 94.679|  2.093| 7,519|  8474.911| 134.934| 887,207|
| |Montgomery County|    82| 135.004|  2.587| 6,577| 10828.280| 89.610| 607,391|
| |Jefferson County|    77| 306.084|  6.814| 5,828| 23166.975| 225.446| 251,565|
| |Lubbock County|    71| 228.613|  3.680| 5,959| 19187.363| 241.952| 310,569|
| |Comal County|    68| 435.314|  8.231| 1,775| 11362.982| 103.341| 156,209|
| |Starr County|    64| 990.206| 33.154| 2,117| 32754.166| 718.342|  64,633|
| |Ector County|    56| 336.897|  6.016| 3,531| 21242.548| 209.701| 166,223|
| |Guadalupe County|    52| 311.663| 11.131| 1,673| 10027.151| 68.497| 166,847|
| |McLennan County|    52| 202.632|  7.237| 4,846| 18883.732| 324.545| 256,623|
| |Val Verde County|    49| 999.490| 78.677| 1,666| 33982.662| 786.771|  49,025|
| |Midland County|    48| 271.444|  4.847| 2,592| 14657.980| 333.650| 176,832|
| |Brazos County|    47| 205.051|  3.116| 4,024| 17555.876| 108.447| 229,211|
| |Potter County|    44| 374.739|  6.083| 3,661| 31180.003| 219.003| 117,415|
| |Angelina County|    43| 495.877| 18.122| 1,796| 20711.526| 313.012|  86,715|
| |Nacogdoches County|    41| 628.796| 13.146| 1,133| 17376.235| 269.484|  65,204|
| |Walker County|    41| 561.867|  5.873| 2,874| 39385.509| 160.533|  72,971|
| |Ellis County|    40| 216.420|  5.410| 2,808| 15192.668| 275.162| 184,826|
| |Victoria County|    40| 434.386| 18.617| 3,436| 37313.757| 361.471|  92,084|
| |Washington County|    39| 1086.896|  3.981|   499| 13906.694| 135.364|  35,882|
| |Maverick County|    38| 647.117|  0.000| 2,321| 39525.221| 807.680|  58,722|
| |Hays County|    37| 160.736|  3.724| 5,012| 21773.223| 443.731| 230,191|
| |Bell County|    36| 99.194|  2.362| 3,785| 10429.181| 125.174| 362,924|
| |Liberty County|    33| 374.069| 12.955|   962| 10904.680| 216.992|  88,219|
| |Bowie County|    32| 343.182|  6.128|   764|  8193.469| 108.776|  93,245|
| |Johnson County|    30| 170.632|  5.688| 1,810| 10294.795| 252.698| 175,817|
| |Caldwell County|    26| 595.456|  9.815| 1,122| 25696.226| 189.761|  43,664|
| |Medina County|    26| 504.032|  8.308|   762| 14772.022| 481.877|  51,584|
| |Hale County|    25| 748.369| 12.829| 1,257| 37627.971| 359.217|  33,406|
| |Matagorda County|    25| 682.259| 15.594|   733| 20003.821| 307.991|  36,643|
| |Wharton County|    25| 601.598| 17.189|   690| 16604.100| 275.016|  41,556|
| |Kaufman County|    24| 176.271|  5.246| 2,125| 15607.327| 406.053| 136,154|
| |Tom Green County|    24| 201.342|  0.000| 2,604| 21845.638| 352.349| 119,200|
| |Willacy County|    24| 1123.701| 40.132|   682| 31931.829| 682.247|  21,358|
| |Gregg County|    24| 193.634|  5.763| 1,379| 11125.903| 108.343| 123,945|
| |Harrison County|    23| 345.589|  2.147|   681| 10232.446| 154.549|  66,553|
| |San Patricio County|    22| 329.687| 14.986|   905| 13562.116| 293.293|  66,730|
| |Taylor County|    22| 159.381|  3.105| 1,117|  8092.209| 41.398| 138,034|
| |Smith County|    21| 90.225|  3.683| 2,470| 10612.199| 109.252| 232,751|
| |Randall County|    21| 152.491|  4.149| 1,714| 12446.174| 161.827| 137,713|
| |Grimes County|    21| 727.147|  9.893|   872| 30193.906| 168.184|  28,880|
| |Hunt County|    21| 212.995|  1.449| 1,137| 11532.142| 166.629|  98,594|
| |Bastrop County|    21| 236.692|  4.830| 1,350| 15215.897| 98.219|  88,723|
| |Shelby County|    18| 712.194| 11.305|   398| 15747.408| 124.351|  25,274|
| |Parker County|    18| 125.982|  5.999| 1,201|  8405.773| 143.979| 142,878|
| |Panola County|    18| 776.063|  6.159|   285| 12287.661| 98.548|  23,194|
| |Orange County|    18| 215.838|  5.139| 1,369| 16415.655| 633.809|  83,396|
| |DeWitt County|    18| 892.857| 28.345|   643| 31894.841| 814.909|  20,160|
| |Atascosa County|    18| 351.886|  8.378|   434|  8484.351| 80.990|  51,153|
| |Lamar County|    18| 361.018|  5.730|   658| 13197.216| 151.857|  49,859|
| |Wilson County|    18| 352.457|  5.595|   434|  8498.140| 55.946|  51,070|
| |Deaf Smith County|    17| 916.640|  0.000|   657| 35425.429| 585.417|  18,546|
| |Brown County|    16| 422.565| 11.319|   388| 10247.201| 139.597|  37,864|
| |Hardin County|    15| 260.408| 12.400|   947| 16440.401| 364.571|  57,602|
| |Lavaca County|    15| 744.269|  7.088|   620| 30763.124| 191.383|  20,154|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Fayette County|    14| 552.355|  5.636|   378| 14913.596| 61.999|  25,346|
| |Grayson County|    13| 95.439|  2.098| 1,103|  8097.671| 121.659| 136,212|
| |Moore County|    13| 620.821|  6.822| 1,047| 50000.000| 266.066|  20,940|
| |Jim Wells County|    13| 321.130| 28.231|   705| 17415.147| 426.998|  40,482|
| |Aransas County|    13| 552.956|  6.076|   169|  7188.430| 97.223|  23,510|
| |Henderson County|    12| 145.038|  5.180|   633|  7650.749| 108.778|  82,737|
| |Rockwall County|    12| 114.378|  0.000|   875|  8340.085| 204.247| 104,915|
| |Lamb County|    11| 853.176| 44.321|   219| 16985.961| 188.364|  12,893|
| |San Augustine County|    11| 1335.438|  0.000|   162| 19667.355| 156.090|   8,237|
| |Wichita County|    11| 83.188|  1.080|   983|  7434.016| 87.510| 132,230|
| |Red River County|    11| 914.913|  0.000|   137| 11394.827| 35.646|  12,023|
| |Polk County|    11| 214.204|  5.564|   748| 14565.848| 255.932|  51,353|
| |Anderson County|    10| 173.205|  4.949| 2,379| 41205.508| 452.808|  57,735|
| |Burnet County|     9| 186.896|  5.933|   551| 11442.218| 35.599|  48,155|
| |Gonzales County|     9| 431.924| 13.712|   680| 32634.256| 459.348|  20,837|
| |Hood County|     9| 146.002|  4.635|   522|  8468.115| 224.797|  61,643|
| |Uvalde County|     9| 336.562| 10.685|   526| 19670.169| 293.824|  26,741|
| |Bee County|     9| 276.370|  0.000|   885| 27176.416| 1697.703|  32,565|
| |Jasper County|     9| 253.314| 16.083|   304|  8556.391| 72.375|  35,529|
| |Lee County|     9| 522.072|  8.287|   171|  9919.369| 165.737|  17,239|
| |Cass County|     8| 266.436|  9.516|   171|  5695.064| 104.671|  30,026|
| |Marion County|     8| 811.853| 14.497|   130| 13192.612| 101.482|   9,854|
| |Fannin County|     8| 225.263|  0.000|   242|  6814.214| 112.632|  35,514|
| |Navarro County|     8| 159.639|  0.000|   841| 16782.073| 222.355|  50,113|
| |San Jacinto County|     8| 277.210|  4.950|   177|  6133.269| 168.306|  28,859|
| |Hill County|     7| 191.001| 15.592|   318|  8676.908| 46.776|  36,649|
| |Kleberg County|     7| 228.162| 13.969|   424| 13820.078| 386.478|  30,680|
| |Parmer County|     7| 728.787|  0.000|   335| 34877.668| 342.084|   9,605|
| |Sabine County|     6| 569.152|  0.000|    51|  4837.792| 162.615|  10,542|
| |Jackson County|     6| 406.504| 19.357|   400| 27100.271| 783.972|  14,760|
| |Karnes County|     6| 384.591| 27.471|   562| 36023.332| 2710.449|  15,601|
| |Burleson County|     6| 325.327|  7.746|   240| 13013.067| 85.205|  18,443|
| |Houston County|     6| 261.233| 12.440|   312| 13584.117| 441.608|  22,968|
| |Wood County|     6| 131.755|  3.137|   316|  6939.107| 100.385|  45,539|
| |Duval County|     6| 537.779| 38.413|   164| 14699.292| 179.260|  11,157|
| |Cherokee County|     6| 113.969|  5.427|   953| 18102.040| 523.714|  52,646|
| |Gillespie County|     6| 222.321| 21.173|   175|  6484.363| 21.173|  26,988|
| |Wise County|     6| 85.734|  2.041|   390|  5572.702| 165.344|  69,984|
| |Andrews County|     6| 320.770|  0.000|   279| 14915.798| 183.297|  18,705|
| |Floyd County|     6| 1050.420| 25.010|    88| 15406.162| 125.050|   5,712|
| |Palo Pinto County|     6| 205.557|  0.000|   256|  8770.427| 313.230|  29,189|
| |Kerr County|     6| 114.068|  0.000|   396|  7528.517| 130.364|  52,600|
| |Reeves County|     5| 312.969| 17.884|   144|  9013.520| 134.130|  15,976|
| |Camp County|     5| 381.854| 10.910|   229| 17488.926| 196.382|  13,094|
| |Howard County|     5| 136.374|  7.793|   168|  4582.151| 70.135|  36,664|
| |Zavala County|     5| 422.297|  0.000|   205| 17314.189| 422.297|  11,840|
| |Blanco County|     5| 419.076| 23.947|    98|  8213.897| 23.947|  11,931|
| |Coryell County|     5| 65.832|  0.000|   660|  8689.813| 107.212|  75,951|
| |Frio County|     5| 246.233|  0.000|   505| 24869.497| 330.655|  20,306|
| |Dallam County|     5| 686.153|  0.000|   187| 25662.138| 176.439|   7,287|
| |Erath County|     5| 117.102|  0.000|   520| 12178.556| 210.783|  42,698|
| |Waller County|     5| 90.504|  7.758|   441|  7982.478| 124.120|  55,246|
| |Refugio County|     4| 575.705| 82.244|   217| 31232.009| 699.071|   6,948|
| |Castro County|     4| 531.208| 18.972|   197| 26162.019| 569.152|   7,530|
| |Hockley County|     4| 173.754|  0.000|   200|  8687.720| 117.905|  23,021|
| |Dawson County|     4| 314.268|  0.000|   143| 11235.072| 112.238|  12,728|
| |Calhoun County|     4| 187.882|  6.710|   529| 24847.346| 509.964|  21,290|
| |Lynn County|     4| 672.156|  0.000|    66| 11090.573| 72.017|   5,951|
| |Kendall County|     4| 84.333|  6.024|   157|  3310.071| 36.143|  47,431|
| |Martin County|     4| 693.121| 24.754|    55|  9530.411| 247.543|   5,771|
| |Goliad County|     4| 522.330| 18.655|    77| 10054.845|  0.000|   7,658|
| |Bailey County|     4| 571.429|  0.000|   170| 24285.714| 285.714|   7,000|
| |Newton County|     4| 294.226|  0.000|    93|  6840.750| 105.081|  13,595|
| |Young County|     4| 222.099|  7.932|   160|  8883.953| 214.167|  18,010|
| |Austin County|     3| 99.893|  0.000|   230|  7658.498| 85.623|  30,032|
| |Bandera County|     3| 129.803|  0.000|    89|  3850.813| 37.086|  23,112|
| |Chambers County|     3| 68.435|  3.259|   942| 21488.697| 234.635|  43,837|
| |Stephens County|     3| 320.307| 15.253|    34|  3630.152| 76.264|   9,366|
| |Limestone County|     3| 128.003|  0.000|   220|  9386.867| 128.003|  23,437|
| |Reagan County|     3| 779.423|  0.000|    62| 16108.080| 259.808|   3,849|
| |Nolan County|     3| 203.887|  0.000|   133|  9039.010| 38.836|  14,714|
| |Milam County|     3| 120.856|  0.000|   333| 13414.978| 178.406|  24,823|
| |Morris County|     3| 242.170| 23.064|   105|  8475.944| 161.447|  12,388|
| |Dimmit County|     3| 296.326| 28.221|   146| 14421.177| 352.769|  10,124|
| |Comanche County|     3| 220.022|  0.000|   141| 10341.034|  0.000|  13,635|
| |Crockett County|     3| 866.051| 41.241|   155| 44745.958| 82.481|   3,464|
| |Cooke County|     3| 72.715|  3.463|   223|  5405.143| 90.028|  41,257|
| |Trinity County|     3| 204.764|  9.751|   156| 10647.737| 263.268|  14,651|
| |Yoakum County|     3| 344.313| 32.792|   100| 11477.103| 377.105|   8,713|
| |Callahan County|     3| 215.162|  0.000|    46|  3299.147| 61.475|  13,943|
| |Van Zandt County|     3| 53.013|  0.000|   375|  6626.612| 118.648|  56,590|
| |Falls County|     3| 173.440|  8.259|   124|  7168.873| 123.886|  17,297|
| |Gaines County|     3| 139.587| 19.941|   158|  7351.573| 259.233|  21,492|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402| 68.803|   6,229|
| |Hamilton County|     3| 354.568| 16.884|    80|  9455.147| 422.105|   8,461|
| |Swisher County|     2| 270.380|  0.000|    80| 10815.195| 96.564|   7,397|
| |Bosque County|     2| 107.038|  0.000|   155|  8295.424| 259.949|  18,685|
| |Zapata County|     2| 141.054|  0.000|   170| 11989.562| 141.054|  14,179|
| |Franklin County|     2| 186.480| 13.320|    90|  8391.608| 93.240|  10,725|
| |Brewster County|     2| 217.320|  0.000|   188| 20428.121| 124.183|   9,203|
| |Culberson County|     2| 921.234|  0.000|    17|  7830.493| 131.605|   2,171|
| |Madison County|     2| 140.017| 20.002|   658| 46065.528| 130.016|  14,284|
| |Rusk County|     2| 36.761|  0.000|   366|  6727.199| 112.908|  54,406|
| |Terry County|     2| 162.114| 11.580|   137| 11104.807| 312.648|  12,337|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890| 95.175|   1,501|
| |Ochiltree County|     2| 203.335|  0.000|    94|  9556.730| 174.287|   9,836|
| |Robertson County|     2| 117.137|  8.367|   231| 13529.343| 158.972|  17,074|
| |Lampasas County|     2| 93.336|  6.667|    90|  4200.112| 46.668|  21,428|
| |Leon County|     2| 114.916|  8.208|   141|  8101.586| 32.833|  17,404|
| |Live Oak County|     2| 163.840| 11.703|   222| 18186.287| 175.543|  12,207|
| |Colorado County|     2| 93.054|  0.000|   272| 12655.283| 225.987|  21,493|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 94.985|   7,520|
| |Tyler County|     2| 92.285|  6.592|   116|  5352.529| 26.367|  21,672|
| |Gray County|     2| 91.383|  0.000|   214|  9777.940| 228.457|  21,886|
| |Hansford County|     2| 370.439|  0.000|    69| 12780.144| 264.599|   5,399|
| |Hutchinson County|     2| 95.520|  0.000|   123|  5874.487| 81.874|  20,938|
| |Cottle County|     2| 1430.615|  0.000|    16| 11444.921| 204.374|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Brooks County|     2| 281.968| 20.141|    99| 13957.423| 302.109|   7,093|
| |Hudspeth County|     2| 409.333|  0.000|    23|  4707.327| 116.952|   4,886|
| |Upshur County|     2| 47.901|  0.000|   212|  5077.479| 82.116|  41,753|
| |Ward County|     1| 83.347|  0.000|    89|  7417.903| 71.440|  11,998|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485| 353.607|     404|
| |Kimble County|     1| 230.574| 32.939|    13|  2997.464|  0.000|   4,337|
| |Knox County|     1| 272.926| 38.989|    59| 16102.620| 584.841|   3,664|
| |Wilbarger County|     1| 78.315|  0.000|    64|  5012.139| 167.817|  12,769|
| |Winkler County|     1| 124.844|  0.000|    80|  9987.516| 249.688|   8,010|
| |Jim Hogg County|     1| 192.308|  0.000|    62| 11923.077| 274.725|   5,200|
| |Eastland County|     1| 54.466|  0.000|    70|  3812.636| 140.056|  18,360|
| |Dickens County|     1| 452.284|  0.000|     4|  1809.136|  0.000|   2,211|
| |Crosby County|     1| 174.307|  0.000|    59| 10284.121| 174.307|   5,737|
| |Clay County|     1| 95.502|  0.000|    40|  3820.074| 95.502|  10,471|
| |Hall County|     1| 337.382|  0.000|    11|  3711.201| 144.592|   2,964|
| |Coke County|     1| 295.247|  0.000|    42| 12400.354| 210.890|   3,387|
| |Fisher County|     1| 261.097|  0.000|    26|  6788.512| 74.599|   3,830|
| |Briscoe County|     1| 646.831|  0.000|    11|  7115.136|  0.000|   1,546|
| |Real County|     1| 289.687| 41.384|    87| 25202.781| 455.223|   3,452|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 68.495|  12,514|
| |Pecos County|     1| 63.199|  0.000|   242| 15294.192| 306.967|  15,823|
| |Llano County|     1| 45.882|  0.000|    88|  4037.623| 13.109|  21,795|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788| 67.641|   2,112|
| |Montague County|     1| 50.459|  0.000|    67|  3380.765| 93.710|  19,818|
| |Hopkins County|     1| 26.966|  0.000|   200|  5393.161| 142.534|  37,084|
| |Mitchell County|     1| 117.028| 16.718|    59|  6904.623| 167.182|   8,545|
| |Scurry County|     1| 59.869|  0.000|   474| 28378.136| 350.664|  16,703|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 102.297|   2,793|
| |Runnels County|     1| 97.428|  0.000|   121| 11788.776| 222.692|  10,264|
| |McCulloch County|     1| 125.251|  0.000|    46|  5761.523| 143.143|   7,984|
| |Sutton County|     1| 264.831|  0.000|    61| 16154.661| 113.499|   3,776|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171| 39.064|   3,657|
| |Childress County|     0|  0.000|  0.000|    40|  5474.952| 136.874|   7,306|
| |Collingsworth County|     0|  0.000|  0.000|    11|  3767.123| 195.695|   2,920|
| |Concho County|     0|  0.000|  0.000|    28| 10271.460| 209.622|   2,726|
| |Delta County|     0|  0.000|  0.000|    16|  3001.313| 53.595|   5,331|
| |Donley County|     0|  0.000|  0.000|    48| 14643.075| 217.903|   3,278|
| |Edwards County|     0|  0.000|  0.000|    25| 12939.959| 73.943|   1,932|
| |Cochran County|     0|  0.000|  0.000|    31| 10865.755| 500.726|   2,853|
| |Coleman County|     0|  0.000|  0.000|    19|  2324.159| 122.324|   8,175|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Carson County|     0|  0.000|  0.000|    15|  2531.218| 48.214|   5,926|
| |Baylor County|     0|  0.000|  0.000|     9|  2564.833| 122.135|   3,509|
| |Archer County|     0|  0.000|  0.000|    21|  2455.279| 66.810|   8,553|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534| 227.118|   1,887|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Jones County|     0|  0.000|  0.000|   629| 31320.022| 35.567|  20,083|
| |Lipscomb County|     0|  0.000|  0.000|    18|  5567.584| 132.562|   3,233|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008| 187.477|     762|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375| 93.006|   1,536|
| |Jack County|     0|  0.000|  0.000|    56|  6267.487| 271.804|   8,935|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Motley County|     0|  0.000|  0.000|     5|  4166.667| 119.048|   1,200|
| |Presidio County|     0|  0.000|  0.000|    46|  6861.575| 106.546|   6,704|
| |Mills County|     0|  0.000|  0.000|    19|  3899.036| 117.264|   4,873|
| |Menard County|     0|  0.000|  0.000|    17|  7951.356| 66.818|   2,138|
| |Mason County|     0|  0.000|  0.000|    51| 11932.616| 401.096|   4,274|
| |McMullen County|     0|  0.000|  0.000|     9| 12113.055| 384.541|     743|
| |Freestone County|     0|  0.000|  0.000|   161|  8165.542| 166.644|  19,717|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Kinney County|     0|  0.000|  0.000|    19|  5181.347| 77.915|   3,667|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Hardeman County|     0|  0.000|  0.000|    17|  4322.400| 72.645|   3,933|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Hartley County|     0|  0.000|  0.000|    84| 15064.562| 51.240|   5,576|
| |Haskell County|     0|  0.000|  0.000|    42|  7423.118| 201.990|   5,658|
| |Hemphill County|     0|  0.000|  0.000|    42| 10997.643| 37.407|   3,819|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 56.510|   5,056|
| |San Saba County|     0|  0.000|  0.000|    23|  3798.514| 47.187|   6,055|
| |Shackelford County|     0|  0.000|  0.000|    18|  5513.017| 43.754|   3,265|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Sherman County|     0|  0.000|  0.000|    40| 13236.267| 141.817|   3,022|
| |Somervell County|     0|  0.000|  0.000|    73|  7997.371| 266.057|   9,128|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704| 105.820|   1,350|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 7,927| 369.080| N/A|517,415| 24090.760| N/A|21,477,737|
| |Miami-Dade County| 1,809| 665.823| 10.411|129,409| 47630.422| 575.595|2,716,940|
| |Palm Beach County|   919| 613.989|  9.926|36,114| 24127.956| 271.060|1,496,770|
| |Broward County|   782| 400.455|  5.340|60,746| 31107.479| 390.286|1,952,778|
| |Pinellas County|   481| 493.335|  7.180|17,541| 17990.843| 173.627| 974,996|
| |Hillsborough County|   386| 262.234|  4.950|31,865| 21647.889| 266.795|1,471,968|
| |Lee County|   329| 426.953|  6.303|16,248| 21085.498| 154.244| 770,577|
| |Polk County|   304| 419.439|  7.096|13,839| 19094.149| 266.289| 724,777|
| |Orange County|   287| 205.963|  7.279|31,026| 22265.568| 206.578|1,393,452|
| |Manatee County|   189| 468.688|  2.480| 9,124| 22625.994| 215.037| 403,253|
| |Duval County|   177| 184.807|  3.580|22,889| 23898.596| 276.092| 957,755|
| |St. Lucie County|   160| 487.364| 17.406| 5,625| 17133.876| 271.096| 328,297|
| |Brevard County|   140| 232.581|  6.171| 5,851|  9720.206| 102.288| 601,942|
| |Collier County|   131| 340.346|  3.340|10,202| 26505.448| 230.485| 384,902|
| |Sarasota County|   130| 299.717|  3.294| 6,095| 14052.132| 166.985| 433,742|
| |Volusia County|   126| 227.731|  3.615| 7,654| 13833.763| 211.723| 553,284|
| |Pasco County|   122| 220.238|  6.705| 6,893| 12443.429| 153.186| 553,947|
| |Escambia County|   115| 361.276|  8.976| 8,757| 27510.398| 457.317| 318,316|
| |Seminole County|   110| 233.137|  8.478| 6,976| 14785.111| 148.057| 471,826|
| |Osceola County|   100| 266.134| 11.026| 9,401| 25019.228| 353.958| 375,751|
| |Martin County|    91| 565.217| 14.197| 3,767| 23397.516| 156.167| 161,000|
| |Charlotte County|    90| 476.417|  3.025| 2,174| 11508.126| 172.418| 188,910|
| |Marion County|    86| 235.243| 10.160| 5,984| 16368.555| 426.720| 365,579|
| |Lake County|    61| 166.159|  3.891| 4,958| 13505.195| 171.996| 367,118|
| |Indian River County|    52| 325.156|  6.253| 2,450| 15319.873| 219.749| 159,923|
| |Clay County|    50| 228.048|  1.303| 3,186| 14531.224| 246.292| 219,252|
| |Bay County|    45| 257.577| 19.625| 4,194| 24006.182| 587.930| 174,705|
| |Hernando County|    43| 221.741|  8.103| 1,929|  9947.401| 187.854| 193,920|
| |Sumter County|    41| 309.621| 11.867| 1,237|  9341.489| 172.611| 132,420|
| |Suwannee County|    40| 900.556| 25.730| 1,356| 30528.852| 723.661|  44,417|
| |Okaloosa County|    38| 180.319|  6.779| 3,391| 16091.070| 424.359| 210,738|
| |Jackson County|    37| 797.173| 18.467| 1,832| 39470.849| 818.718|  46,414|
| |Hendry County|    37| 880.491|  3.400| 1,725| 41049.926| 316.161|  42,022|
| |Citrus County|    36| 240.550|  8.591| 1,473|  9842.507| 255.823| 149,657|
| |Santa Rosa County|    36| 195.320| 10.851| 3,791| 20568.272| 352.661| 184,313|
| |Highlands County|    36| 338.916| 13.449| 1,355| 12756.423| 258.222| 106,221|
| |St. Johns County|    34| 128.461|  4.318| 3,552| 13420.384| 181.357| 264,672|
| |Alachua County|    26| 96.639|  2.655| 4,006| 14889.813| 254.872| 269,043|
| |Putnam County|    25| 335.476| 19.170| 1,465| 19658.888| 314.389|  74,521|
| |Leon County|    24| 81.749|  4.866| 4,814| 16397.463| 312.884| 293,582|
| |Gadsden County|    21| 459.921|  9.386| 1,781| 39005.694| 1357.862|  45,660|
| |DeSoto County|    16| 421.042|  7.519| 1,327| 34920.134| 236.836|  38,001|
| |Walton County|    15| 202.508|  3.857| 1,345| 18158.254| 270.011|  74,071|
| |Washington County|    14| 549.602|  0.000|   807| 31680.603| 1749.752|  25,473|
| |Columbia County|    14| 195.296|  7.971| 2,784| 38836.035| 613.788|  71,686|
| |Flagler County|    13| 112.964|  3.724| 1,008|  8759.048| 132.826| 115,081|
| |Monroe County|    13| 175.136|  9.623| 1,456| 19615.240| 300.233|  74,228|
| |Nassau County|    11| 124.118|  1.612| 1,202| 13562.764| 238.565|  88,625|
| |Okeechobee County|     9| 213.432| 10.163| 1,013| 24022.956| 406.537|  42,168|
| |Madison County|     8| 432.596|  7.725|   686| 37095.117| 633.444|  18,493|
| |Hardee County|     7| 259.866|  0.000|   908| 33708.282| 397.753|  26,937|
| |Calhoun County|     7| 496.278|  0.000|   417| 29563.984| 1377.424|  14,105|
| |Jefferson County|     5| 350.976|  0.000|   447| 31377.229| 2186.077|  14,246|
| |Levy County|     4| 96.379|  3.442|   652| 15709.708| 265.041|  41,503|
| |Wakulla County|     4| 118.557|  4.234|   662| 19621.210| 381.077|  33,739|
| |Union County|     4| 262.519|  0.000|   291| 19098.248| 712.551|  15,237|
| |Liberty County|     4| 478.813| 34.201|   395| 47282.739| 427.511|   8,354|
| |Taylor County|     4| 185.451|  6.623|   936| 43395.614| 4013.697|  21,569|
| |Hamilton County|     4| 277.239|  9.901|   612| 42417.521| 415.858|  14,428|
| |Dixie County|     4| 237.727|  0.000|   424| 25199.097| 1460.325|  16,826|
| |Bradford County|     4| 141.839|  5.066|   434| 15389.525| 552.159|  28,201|
| |Baker County|     4| 136.939|  0.000|   630| 21567.956| 1340.050|  29,210|
| |Glades County|     3| 217.218|  0.000|   398| 28817.609| 93.093|  13,811|
| |Gilchrist County|     3| 161.447|  0.000|   345| 18566.355| 276.766|  18,582|
| |Holmes County|     2| 101.952|  0.000|   486| 24774.430| 466.068|  19,617|
| |Gulf County|     2| 146.638| 10.474|   569| 41718.601| 2440.481|  13,639|
| |Franklin County|     2| 164.948| 11.782|   377| 31092.784| 3169.367|  12,125|
| |Lafayette County|     1| 118.737|  0.000|   129| 15317.027| 457.984|   8,422|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,613| 600.782| N/A|190,443| 15028.858| N/A|12,671,821|
| |Cook County| 4,920| 955.297|  0.943|110,002| 21358.645| 125.071|5,150,233|
| |DuPage County|   519| 562.345|  1.393|12,021| 13024.950| 116.710| 922,921|
| |Lake County|   445| 638.877|  1.025|12,491| 17933.054| 130.442| 696,535|
| |Will County|   344| 498.014|  1.034| 9,053| 13106.177| 126.158| 690,743|
| |Kane County|   303| 569.118|  2.683| 9,629| 18085.924| 150.262| 532,403|
| |St. Clair County|   160| 616.129|  2.751| 3,897| 15006.585| 214.545| 259,686|
| |Winnebago County|   129| 456.521|  3.539| 3,755| 13288.649| 57.634| 282,572|
| |McHenry County|   114| 370.402|  0.928| 3,123| 10147.056| 119.290| 307,774|
| |Madison County|    74| 281.405|  1.087| 2,470|  9392.849| 201.547| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,725| 15701.516| 85.822| 109,862|
| |Peoria County|    35| 195.335|  0.797| 1,525|  8511.042| 217.659| 179,179|
| |Rock Island County|    34| 239.641|  4.028| 1,679| 11834.028| 130.896| 141,879|
| |Sangamon County|    33| 169.516|  0.000| 1,194|  6133.394| 176.854| 194,672|
| |DeKalb County|    30| 285.995|  1.362|   917|  8741.909| 148.445| 104,897|
| |LaSalle County|    24| 220.854|  7.888|   684|  6294.343| 268.180| 108,669|
| |Kendall County|    23| 178.308|  0.000| 1,343| 10411.660| 89.708| 128,990|
| |Boone County|    23| 429.553|  0.000|   758| 14156.582| 96.049|  53,544|
| |Macon County|    23| 221.135|  0.000|   578|  5557.211| 197.785| 104,009|
| |Union County|    23| 1381.133| 17.157|   318| 19095.658| 360.295|  16,653|
| |Coles County|    20| 395.093|  2.822|   448|  8850.082| 228.589|  50,621|
| |Champaign County|    19| 90.610|  0.000| 1,625|  7749.572| 94.698| 209,689|
| |Jefferson County|    19| 504.193|  7.582|   247|  6554.506| 269.156|  37,684|
| |Jackson County|    19| 334.802|  0.000|   695| 12246.696| 198.867|  56,750|
| |Clinton County|    17| 452.585|  0.000|   387| 10302.966| 216.784|  37,562|
| |Whiteside County|    16| 289.986|  0.000|   339|  6144.087| 90.621|  55,175|
| |McLean County|    15| 87.455|  0.000|   624|  3638.123| 73.296| 171,517|
| |McDonough County|    15| 505.357|  0.000|   139|  4682.973| 77.007|  29,682|
| |Monroe County|    13| 375.321|  0.000|   305|  8805.612| 181.474|  34,637|
| |Iroquois County|    11| 405.694| 21.075|   257|  9478.498| 89.569|  27,114|
| |Cass County|    11| 905.573|  0.000|   223| 18358.442| 364.581|  12,147|
| |Tazewell County|     8| 60.697|  0.000|   486|  3687.321| 163.664| 131,803|
| |Jasper County|     7| 728.408|  0.000|    59|  6139.438| 133.789|   9,610|
| |Randolph County|     7| 220.250|  0.000|   452| 14221.887| 157.322|  31,782|
| |Montgomery County|     7| 246.357|  5.028|   161|  5666.221| 115.637|  28,414|
| |Morgan County|     6| 178.264|  4.244|   229|  6803.732| 190.997|  33,658|
| |Williamson County|     6| 90.094|  2.145|   374|  5615.869| 156.592|  66,597|
| |Stephenson County|     6| 134.838|  0.000|   325|  7303.699| 38.525|  44,498|
| |Grundy County|     5| 97.936|  0.000|   307|  6013.241| 106.330|  51,054|
| |Ogle County|     5| 98.730|  0.000|   403|  7957.664| 98.730|  50,643|
| |Adams County|     5| 76.412|  8.733|   506|  7732.865| 246.701|  65,435|
| |Christian County|     4| 123.824|  0.000|   134|  4148.093| 145.935|  32,304|
| |Carroll County|     4| 279.623|  9.987|    50|  3495.281| 69.906|  14,305|
| |Macoupin County|     3| 66.776|  0.000|   156|  3472.377| 92.215|  44,926|
| |Mercer County|     3| 194.338| 27.763|    73|  4728.898| 74.034|  15,437|
| |Woodford County|     3| 78.005|  0.000|   134|  3484.230| 174.583|  38,459|
| |Fayette County|     3| 140.607|  0.000|    60|  2812.148| 46.869|  21,336|
| |Bond County|     3| 182.637|  8.697|    59|  3591.867| 95.667|  16,426|
| |Clark County|     2| 129.525| 18.504|    79|  5116.249| 120.273|  15,441|
| |Douglas County|     2| 102.749|  0.000|   108|  5548.420| 36.696|  19,465|
| |Cumberland County|     2| 185.770|  0.000|    53|  4922.905| 92.885|  10,766|
| |Ford County|     2| 154.309| 11.022|    49|  3780.572| 121.243|  12,961|
| |Gallatin County|     2| 414.250| 59.179|    49| 10149.130| 207.125|   4,828|
| |Bureau County|     2| 61.297|  0.000|   179|  5486.086| 245.188|  32,628|
| |Jersey County|     2| 91.857|  6.561|    98|  4500.987| 236.203|  21,773|
| |Vermilion County|     2| 26.400|  0.000|   229|  3022.783| 75.428|  75,758|
| |Saline County|     2| 85.139|  6.081|   130|  5534.034| 170.278|  23,491|
| |Livingston County|     2| 56.104|  0.000|   105|  2945.467| 80.149|  35,648|
| |Perry County|     1| 47.810|  0.000|   149|  7123.733| 327.842|  20,916|
| |Shelby County|     1| 46.224|  0.000|    75|  3466.765| 145.274|  21,634|
| |Wayne County|     1| 61.671|  0.000|    59|  3638.606| 167.394|  16,215|
| |Jo Daviess County|     1| 47.092|  0.000|   124|  5839.416| 94.184|  21,235|
| |Lee County|     1| 29.329|  0.000|   165|  4839.277| 121.506|  34,096|
| |Henry County|     1| 20.444|  0.000|   232|  4743.115| 110.984|  48,913|
| |Knox County|     1| 20.121|  0.000|   291|  5855.249| 143.722|  49,699|
| |Hancock County|     1| 56.472|  0.000|    47|  2654.168| 153.280|  17,708|
| |Effingham County|     1| 29.405|  0.000|   139|  4087.274| 235.239|  34,008|
| |Schuyler County|     0|  0.000|  0.000|    17|  2511.820| 42.215|   6,768|
| |Scott County|     0|  0.000|  0.000|    16|  3231.670| 201.979|   4,951|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Moultrie County|     0|  0.000|  0.000|    72|  4965.175| 197.031|  14,501|
| |Wabash County|     0|  0.000|  0.000|    34|  2951.389| 62.004|  11,520|
| |Menard County|     0|  0.000|  0.000|    53|  4345.687| 105.421|  12,196|
| |Pike County|     0|  0.000|  0.000|    20|  1285.264| 64.263|  15,561|
| |Warren County|     0|  0.000|  0.000|   189| 11220.613| 84.812|  16,844|
| |Washington County|     0|  0.000|  0.000|    64|  4608.627| 82.297|  13,887|
| |Massac County|     0|  0.000|  0.000|    37|  2686.611| 41.492|  13,772|
| |Richland County|     0|  0.000|  0.000|    18|  1160.317| 55.253|  15,513|
| |Mason County|     0|  0.000|  0.000|    45|  3368.516| 32.081|  13,359|
| |Logan County|     0|  0.000|  0.000|   106|  3703.963| 134.780|  28,618|
| |Marion County|     0|  0.000|  0.000|   152|  4085.472| 84.474|  37,205|
| |White County|     0|  0.000|  0.000|    64|  4727.783| 84.425|  13,537|
| |Marshall County|     0|  0.000|  0.000|    24|  2098.269| 74.938|  11,438|
| |Pope County|     0|  0.000|  0.000|     8|  1915.250| 34.201|   4,177|
| |Pulaski County|     0|  0.000|  0.000|    92| 17244.611| 53.555|   5,335|
| |Piatt County|     0|  0.000|  0.000|    56|  3426.334| 166.072|  16,344|
| |Putnam County|     0|  0.000|  0.000|    11|  1916.710| 99.569|   5,739|
| |Brown County|     0|  0.000|  0.000|    13|  1976.285|  0.000|   6,578|
| |Alexander County|     0|  0.000|  0.000|    36|  6248.915| 24.797|   5,761|
| |Fulton County|     0|  0.000|  0.000|    33|   960.978| 37.441|  34,340|
| |Greene County|     0|  0.000|  0.000|    38|  2930.064| 231.321|  12,969|
| |Lawrence County|     0|  0.000|  0.000|    45|  2870.264| 45.560|  15,678|
| |Johnson County|     0|  0.000|  0.000|    66|  5315.294| 149.565|  12,417|
| |Henderson County|     0|  0.000|  0.000|    10|  1504.664| 21.495|   6,646|
| |Clay County|     0|  0.000|  0.000|    20|  1516.990| 86.685|  13,184|
| |Franklin County|     0|  0.000|  0.000|   156|  4055.213| 148.543|  38,469|
| |Edwards County|     0|  0.000|  0.000|    17|  2658.327| 111.694|   6,395|
| |Edgar County|     0|  0.000|  0.000|    28|  1631.607| 24.974|  17,161|
| |De Witt County|     0|  0.000|  0.000|    33|  2110.244| 54.812|  15,638|
| |Crawford County|     0|  0.000|  0.000|    29|  1553.544|  0.000|  18,667|
| |Calhoun County|     0|  0.000|  0.000|     9|  1899.135| 90.435|   4,739|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 74.775|   3,821|
| |Hamilton County|     0|  0.000|  0.000|    28|  3449.975| 158.417|   8,116|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,296| 569.911| N/A|122,028|  9531.956| N/A|12,801,989|
| |Philadelphia County| 1,698| 1071.926| N/A|31,120| 19645.671| N/A|1,584,064|
| |Montgomery County|   855| 1028.986|  1.203|10,015| 12052.978| 43.670| 830,915|
| |Delaware County|   697| 1229.826|  3.025| 9,121| 16093.601| 113.933| 566,747|
| |Bucks County|   582| 926.353|  0.910| 7,147| 11375.682| 55.709| 628,270|
| |Lancaster County|   410| 751.296|  1.047| 5,822| 10668.396| 77.747| 545,724|
| |Berks County|   368| 873.769|  1.018| 5,321| 12634.033| 57.324| 421,164|
| |Chester County|   349| 664.776|  0.000| 5,102|  9718.299| 59.049| 524,989|
| |Lehigh County|   336| 909.785|  0.774| 4,918| 13316.437| 41.776| 369,318|
| |Northampton County|   292| 956.483|  0.936| 3,913| 12817.531| 40.243| 305,285|
| |Allegheny County|   244| 200.650|  1.645| 8,709|  7161.742| 72.248|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,922|  9166.611| 19.077| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,409| 10739.815| 70.660| 317,417|
| |Dauphin County|   158| 567.735|  1.540| 2,757|  9906.611| 60.059| 278,299|
| |Monroe County|   124| 728.251|  0.839| 1,618|  9502.499| 31.882| 170,271|
| |York County|    93| 207.100|  2.227| 2,485|  5533.806| 68.715| 449,058|
| |Beaver County|    91| 555.118|  2.614| 1,294|  7893.661| 71.460| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,276|  5036.113| 41.159| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,594| 11241.740| 31.233| 141,793|
| |Schuylkill County|    50| 353.709|  1.011|   908|  6423.362| 28.297| 141,359|
| |Franklin County|    46| 296.723|  0.000| 1,328|  8566.250| 55.290| 155,027|
| |Westmoreland County|    46| 131.843|  0.000| 1,500|  4299.238| 37.260| 348,899|
| |Columbia County|    35| 538.760|  0.000|   470|  7234.776| 28.587|  64,964|
| |Carbon County|    28| 436.259|  0.000|   368|  5733.695| 26.710|  64,182|
| |Susquehanna County|    27| 669.510|  3.542|   213|  5281.690| 14.170|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  5.120|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   369|  3256.869| 55.479| 113,299|
| |Adams County|    20| 194.158|  0.000|   497|  4824.821| 48.539| 103,009|
| |Erie County|    18| 66.734|  1.059| 1,058|  3922.470| 71.501| 269,728|
| |Butler County|    15| 79.850|  0.000|   645|  3433.536| 36.503| 187,853|
| |Lawrence County|    15| 175.414|  6.682|   389|  4549.069| 85.201|  85,512|
| |Northumberland County|    12| 132.096|  1.573|   449|  4942.593| 75.483|  90,843|
| |Washington County|    12| 58.009|  0.691|   821|  3968.772| 55.937| 206,865|
| |Centre County|    10| 61.582|  0.000|   368|  2266.219|  9.677| 162,385|
| |Mercer County|     9| 82.249|  0.000|   404|  3692.060| 95.304| 109,424|
| |Wayne County|     9| 175.230|  2.781|   158|  3076.264|  0.000|  51,361|
| |Wyoming County|     8| 298.574|  0.000|    58|  2164.664|  5.332|  26,794|
| |Juniata County|     6| 242.297|  0.000|   131|  5290.151| 34.614|  24,763|
| |Indiana County|     6| 71.367|  0.000|   309|  3675.377| 90.058|  84,073|
| |Armstrong County|     6| 92.686|  0.000|   204|  3151.309| 55.170|  64,735|
| |Blair County|     5| 41.041|  2.345|   265|  2175.180| 71.529| 121,829|
| |Fayette County|     5| 38.678|  1.105|   472|  3651.160| 93.931| 129,274|
| |Clinton County|     5| 129.426|  0.000|   119|  3080.348| 22.187|  38,632|
| |Perry County|     5| 108.057|  0.000|   121|  2614.972| 24.699|  46,272|
| |Bedford County|     4| 83.528|  0.000|   138|  2881.724| 29.832|  47,888|
| |Huntingdon County|     4| 88.605|  0.000|   300|  6645.401| 41.138|  45,144|
| |Somerset County|     3| 40.846|  1.945|   129|  1756.369| 17.505|  73,447|
| |Montour County|     3| 164.564|  0.000|   100|  5485.464| 54.855|  18,230|
| |Bradford County|     3| 49.732|  0.000|    85|  1409.081| 11.841|  60,323|
| |Cambria County|     3| 23.043|  0.000|   328|  2519.356| 85.588| 130,192|
| |Tioga County|     3| 73.908|  3.519|    37|   911.532|  7.039|  40,591|
| |Union County|     2| 44.521|  0.000|   216|  4808.227| 267.124|  44,923|
| |Elk County|     2| 66.867|  0.000|    48|  1604.814| 23.881|  29,910|
| |Clarion County|     2| 52.032|  0.000|    78|  2029.242| 11.150|  38,438|
| |Fulton County|     2| 137.646|  0.000|    26|  1789.401| 39.327|  14,530|
| |Snyder County|     2| 49.539|  0.000|   101|  2501.734| 28.308|  40,372|
| |Greene County|     1| 27.599|  3.943|   112|  3091.105| 19.714|  36,233|
| |Jefferson County|     1| 23.028|  0.000|    62|  1427.749| 16.449|  43,425|
| |Crawford County|     1| 11.816|  0.000|   139|  1642.463| 25.321|  84,629|
| |Mifflin County|     1| 21.674|  0.000|   116|  2514.197| 49.541|  46,138|
| |McKean County|     1| 24.615|  0.000|    34|   836.923| 21.099|  40,625|
| |Warren County|     1| 25.516|  0.000|    22|   561.353| 25.516|  39,191|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Venango County|     0|  0.000|  0.000|    63|  1243.388|  2.819|  50,668|
| |Cameron County|     0|  0.000|  0.000|     6|  1349.224| 32.124|   4,447|
| |Clearfield County|     0|  0.000|  0.000|   156|  1968.330| 45.063|  79,255|
| |Forest County|     0|  0.000|  0.000|     9|  1241.893|  0.000|   7,247|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,448| 645.649| N/A|90,803|  9092.250| N/A|9,986,857|
| |Wayne County| 2,827| 1616.035|  2.042|27,955| 15980.285| 72.517|1,749,343|
| |Oakland County| 1,133| 900.934|  0.795|15,292| 12159.824| 77.018|1,257,584|
| |Macomb County|   944| 1080.126|  1.308|10,205| 11676.575| 123.737| 873,972|
| |Genesee County|   295| 726.936|  0.352| 3,630|  8945.007| 58.789| 405,813|
| |Kent County|   158| 240.504|  0.870| 7,448| 11337.154| 85.894| 656,955|
| |Saginaw County|   130| 682.275|  0.750| 1,953| 10249.870| 98.218| 190,539|
| |Washtenaw County|   112| 304.678|  0.000| 2,512|  6833.496| 53.630| 367,601|
| |Kalamazoo County|    83| 313.130|  1.617| 1,618|  6104.140| 51.739| 265,066|
| |Berrien County|    66| 430.245|  1.863| 1,347|  8780.908| 72.639| 153,401|
| |Muskegon County|    59| 339.928|  1.646| 1,160|  6683.337| 28.807| 173,566|
| |Ottawa County|    55| 188.466|  0.490| 1,787|  6123.428| 56.295| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   805|  5058.821| 45.785| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   782|  5828.905| 57.501| 134,159|
| |Jackson County|    34| 214.498|  0.901|   709|  4472.904| 34.248| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   461|  5262.137| 92.948|  87,607|
| |Bay County|    31| 300.603|  0.000|   600|  5818.125| 84.501| 103,126|
| |Ingham County|    30| 102.597|  0.000| 1,536|  5252.970| 37.619| 292,406|
| |Tuscola County|    29| 555.077|  5.469|   334|  6392.956| 92.969|  52,245|
| |Livingston County|    28| 145.837|  0.000|   816|  4250.111| 41.668| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   338|  4961.686| 35.650|  68,122|
| |Monroe County|    25| 166.113|  2.848|   955|  6345.515| 83.531| 150,500|
| |Hillsdale County|    25| 548.186|  0.000|   260|  5701.129| 43.855|  45,605|
| |Gratiot County|    15| 368.451|  0.000|   154|  3782.761| 38.600|  40,711|
| |Cass County|    14| 270.338| 13.793|   316|  6101.917| 88.274|  51,787|
| |Alpena County|    13| 457.666|  0.000|   127|  4471.044| 10.059|  28,405|
| |Clinton County|    13| 163.327|  0.000|   422|  5301.841| 32.306|  79,595|
| |Lenawee County|    12| 121.888|  0.000|   419|  4255.924| 44.982|  98,451|
| |Iosco County|    12| 477.574|  0.000|   130|  5173.718|  5.685|  25,127|
| |Marquette County|    11| 164.920|  0.000|   152|  2278.895| 53.545|  66,699|
| |Otsego County|    10| 405.383|  0.000|   134|  5432.139| 17.374|  24,668|
| |Midland County|    10| 120.256|  1.718|   325|  3908.317| 56.692|  83,156|
| |Van Buren County|    10| 132.141|  0.000|   440|  5814.184| 86.835|  75,677|
| |Isabella County|     9| 128.807|  2.045|   206|  2948.248| 14.312|  69,872|
| |Eaton County|     8| 72.551|  1.296|   456|  4135.379| 11.660| 110,268|
| |St. Joseph County|     8| 131.225|  2.343|   580|  9513.811| 72.642|  60,964|
| |Allegan County|     7| 59.281|  0.000|   510|  4319.069| 18.147| 118,081|
| |Ionia County|     6| 92.740|  2.208|   274|  4235.127| 19.873|  64,697|
| |Oceana County|     6| 226.697|  0.000|   474| 17909.094| 70.168|  26,467|
| |Sanilac County|     6| 145.737|  0.000|   106|  2574.690| 48.579|  41,170|
| |Crawford County|     5| 356.405|  0.000|   105|  7484.496| 122.196|  14,029|
| |Grand Traverse County|     5| 53.713|  0.000|   207|  2223.702| 24.554|  93,088|
| |Wexford County|     4| 118.938|  0.000|    70|  2081.413| 29.734|  33,631|
| |Kalkaska County|     4| 221.754|  0.000|    51|  2827.364| 23.759|  18,038|
| |Huron County|     4| 129.111|  0.000|   156|  5035.344| 46.111|  30,981|
| |Clare County|     3| 96.931|  0.000|    70|  2261.712| 55.389|  30,950|
| |Delta County|     3| 83.836|  0.000|    89|  2487.145| 67.868|  35,784|
| |Arenac County|     3| 201.572|  0.000|    41|  2754.821|  9.599|  14,883|
| |Barry County|     2| 32.494|  0.000|   175|  2843.217| 11.605|  61,550|
| |Branch County|     2| 45.959|  0.000|   355|  8157.731| 118.180|  43,517|
| |Ogemaw County|     2| 95.252|  0.000|    53|  2524.170| 20.411|  20,997|
| |Charlevoix County|     2| 76.502|  0.000|    45|  1721.302| 16.393|  26,143|
| |Cheboygan County|     2| 79.126|  0.000|    44|  1740.782| 39.563|  25,276|
| |Dickinson County|     2| 79.242|  0.000|    52|  2060.303| 45.281|  25,239|
| |Emmet County|     2| 59.853|  0.000|    61|  1825.527| 12.826|  33,415|
| |Gladwin County|     2| 78.589|  0.000|    58|  2279.068| 39.294|  25,449|
| |Mecosta County|     2| 46.027|  0.000|    66|  1518.882| 36.164|  43,453|
| |Alcona County|     1| 96.108|  0.000|    28|  2691.014|  0.000|  10,405|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  9.449|  15,118|
| |Montcalm County|     1| 15.652|  0.000|   185|  2895.692| 24.597|  63,888|
| |Iron County|     1| 90.367|  0.000|    19|  1716.971| 25.819|  11,066|
| |Gogebic County|     1| 71.556|  0.000|   110|  7871.199| 276.003|  13,975|
| |Presque Isle County|     1| 79.416|  0.000|    19|  1508.895| 45.380|  12,592|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Montmorency County|     1| 107.204| 15.315|     9|   964.837| 15.315|   9,328|
| |Antrim County|     1| 42.874|  6.125|    41|  1757.846| 30.624|  23,324|
| |Benzie County|     1| 56.287|  0.000|    29|  1632.331| 16.082|  17,766|
| |Mason County|     0|  0.000|  0.000|    99|  3396.926| 19.607|  29,144|
| |Ontonagon County|     0|  0.000|  0.000|     7|  1223.776| 74.925|   5,720|
| |Roscommon County|     0|  0.000|  0.000|    52|  2164.953| 29.738|  24,019|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128| 88.249|   8,094|
| |Newaygo County|     0|  0.000|  0.000|   250|  5104.124|  8.750|  48,980|
| |Menominee County|     0|  0.000|  0.000|   124|  5443.371| 238.304|  22,780|
| |Manistee County|     0|  0.000|  0.000|    35|  1425.197| 23.269|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    26|  2407.630| 79.372|  10,799|
| |Luce County|     0|  0.000|  0.000|     3|   481.618|  0.000|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    69|  3170.810| 32.824|  21,761|
| |Lake County|     0|  0.000|  0.000|    19|  1602.970| 36.157|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    49|  1373.164|  8.007|  35,684|
| |Osceola County|     0|  0.000|  0.000|    70|  2983.802| 24.358|  23,460|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Alger County|     0|  0.000|  0.000|     9|   988.142| 15.685|   9,108|
| |Chippewa County|     0|  0.000|  0.000|    39|  1044.205| 38.249|  37,349|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,441| 1245.622| N/A|50,083| 14047.396| N/A|3,565,287|
| |Hartford County| 1,415| 1586.821|  0.481|12,761| 14310.546| 18.584| 891,720|
| |Fairfield County| 1,408| 1492.582|  0.303|17,956| 19034.656| 24.685| 943,332|
| |New Haven County| 1,104| 1291.595|  0.501|13,145| 15378.640| 17.382| 854,757|
| |Middlesex County|   192| 1182.004|  0.879| 1,396|  8594.154| 16.710| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,610|  8927.928| 10.298| 180,333|
| |New London County|   103| 388.377|  0.000| 1,433|  5403.347| 16.699| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,056|  7006.323| 35.070| 150,721|
| |Windham County|    15| 128.444|  0.000|   726|  6216.711| 40.368| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,089| 879.583| N/A|128,533| 27648.676| N/A|4,648,794|
| |Orleans Parish|   562| 1440.494|  0.732|10,637| 27264.292| 139.875| 390,144|
| |Jefferson Parish|   523| 1209.268|  3.303|15,103| 34920.796| 313.135| 432,493|
| |East Baton Rouge Parish|   344| 781.713|  5.843|11,946| 27146.360| 407.738| 440,059|
| |Caddo Parish|   293| 1219.797|  9.516| 6,610| 27518.276| 277.145| 240,204|
| |St. Tammany Parish|   211| 810.233|  5.486| 5,086| 19530.065| 255.083| 260,419|
| |Calcasieu Parish|   146| 717.670| 17.556| 6,752| 33189.799| 332.853| 203,436|
| |Rapides Parish|   114| 879.304| 13.223| 3,223| 24859.620| 306.324| 129,648|
| |Ouachita Parish|   111| 724.170|  5.592| 4,787| 31230.632| 386.783| 153,279|
| |Lafourche Parish|    97| 993.710|  1.463| 2,759| 28264.388| 355.628|  97,614|
| |St. John the Baptist Parish|    92| 2147.676| 13.340| 1,403| 32752.060| 230.108|  42,837|
| |Lafayette Parish|    91| 372.356|  4.092| 7,468| 30557.715| 767.509| 244,390|
| |Terrebonne Parish|    85| 769.502| 14.226| 2,986| 27032.165| 378.931| 110,461|
| |St. Landry Parish|    85| 1035.020| 22.614| 2,631| 32036.920| 955.002|  82,124|
| |Acadia Parish|    79| 1273.269| 18.420| 2,570| 41421.549| 550.292|  62,045|
| |Bossier Parish|    79| 621.856| 13.494| 2,311| 18191.264| 289.000| 127,039|
| |Tangipahoa Parish|    72| 534.291| 10.601| 3,397| 25208.151| 381.636| 134,758|
| |Ascension Parish|    71| 560.804|  3.385| 2,798| 22100.408| 383.648| 126,604|
| |Iberia Parish|    70| 1002.434| 16.366| 2,450| 35085.207| 593.278|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,247| 26994.848| 250.496|  46,194|
| |St. Mary Parish|    52| 1053.741| 11.580| 1,543| 31267.731| 468.973|  49,348|
| |Livingston Parish|    51| 362.244|  3.044| 2,845| 20207.545| 288.172| 140,789|
| |St. Charles Parish|    51| 960.452|  2.690| 1,442| 27156.309| 274.415|  53,100|
| |Iberville Parish|    47| 1445.665|  0.000| 1,219| 37495.002| 522.900|  32,511|
| |St. Martin Parish|    43| 804.776|  2.674| 1,616| 30244.615| 395.704|  53,431|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   701| 26487.814| 475.021|  26,465|
| |East Feliciana Parish|    36| 1881.369|  7.466|   567| 29631.565| 574.863|  19,135|
| |Union Parish|    33| 1492.672|  6.462|   675| 30531.934| 510.481|  22,108|
| |St. James Parish|    32| 1516.875|  6.772|   693| 32849.829| 467.252|  21,096|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   780| 35895.076| 486.490|  21,730|
| |Avoyelles Parish|    31| 772.220| 17.793| 1,021| 25433.440| 405.682|  40,144|
| |Bienville Parish|    30| 2265.690|  0.000|   364| 27490.371| 172.624|  13,241|
| |Lincoln Parish|    29| 620.427| 18.338|   766| 16387.831| 216.997|  46,742|
| |Allen Parish|    29| 1131.619| 55.745| 1,245| 48581.574| 1165.066|  25,627|
| |Vernon Parish|    27| 569.272| 18.072|   748| 15770.942| 256.022|  47,429|
| |De Soto Parish|    26| 946.728| 10.404|   710| 25852.966| 400.539|  27,463|
| |Jefferson Davis Parish|    26| 828.870|  9.108| 1,005| 32039.021| 277.808|  31,368|
| |Vermilion Parish|    24| 403.287| 16.804| 1,529| 25692.729| 732.158|  59,511|
| |St. Bernard Parish|    24| 508.001|  3.024| 1,091| 23092.880| 272.143|  47,244|
| |Assumption Parish|    20| 913.617|  6.526|   577| 26357.864| 261.034|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   451| 19442.169| 190.911|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   368| 23373.984| 172.401|  15,744|
| |Beauregard Parish|    17| 453.370| 11.429|   819| 21841.747| 289.547|  37,497|
| |Natchitoches Parish|    17| 445.516|  0.000|   761| 19943.393| 370.639|  38,158|
| |Franklin Parish|    17| 849.363|  7.138|   896| 44766.425| 792.263|  20,015|
| |Grant Parish|    16| 714.637| 51.045|   298| 13310.108| 178.659|  22,389|
| |West Feliciana Parish|    16| 1027.749|  9.176|   345| 22160.843| 211.056|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   868| 22639.541| 212.385|  38,340|
| |Morehouse Parish|    11| 442.229|  0.000|   494| 19860.095| 379.053|  24,874|
| |Red River Parish|    11| 1303.009| 16.922|   212| 25112.533| 558.432|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   251| 16017.869| 319.081|  15,670|
| |Sabine Parish|    10| 418.690| 17.944|   622| 26042.539| 622.054|  23,884|
| |Concordia Parish|     9| 467.314| 14.835|   303| 15732.904| 311.543|  19,259|
| |Richland Parish|     7| 347.878|  7.100|   586| 29122.354| 518.267|  20,122|
| |Winn Parish|     7| 503.452|  0.000|   413| 29703.682| 400.707|  13,904|
| |Madison Parish|     6| 547.895|  0.000|   609| 55611.360| 756.617|  10,951|
| |West Carroll Parish|     5| 461.681|  0.000|   287| 26500.462| 527.635|  10,830|
| |Catahoula Parish|     5| 526.648| 15.047|   280| 29492.311| 466.460|   9,494|
| |Evangeline Parish|     4| 119.778|  8.556|   861| 25782.303| 693.004|  33,395|
| |Caldwell Parish|     2| 201.654| 14.404|   212| 21375.277| 316.884|   9,918|
| |LaSalle Parish|     2| 134.300|  0.000|   283| 19003.492| 613.944|  14,892|
| |St. Helena Parish|     1| 98.697|  0.000|   258| 25463.877| 281.992|  10,132|
| |East Carroll Parish|     1| 145.751|  0.000|   518| 75499.198| 520.541|   6,861|
| |Cameron Parish|     0|  0.000|  0.000|   167| 23949.520| 61.462|   6,973|
| |Tensas Parish|     0|  0.000|  0.000|    70| 16151.361| 461.467|   4,334|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,080| 560.538| N/A|185,053| 25423.849| N/A|7,278,717|
| |Maricopa County| 2,307| 514.334|  8.058|124,924| 27851.164| 243.042|4,485,414|
| |Pima County|   482| 460.240|  3.137|17,497| 16707.105| 181.423|1,047,279|
| |Yuma County|   280| 1309.715| 17.374|11,448| 53548.626| 379.550| 213,787|
| |Navajo County|   199| 1794.021| 15.455| 5,352| 48249.252| 193.182| 110,924|
| |Mohave County|   165| 777.638| 10.772| 3,147| 14831.677| 154.181| 212,181|
| |Pinal County|   157| 339.247|  6.482| 8,327| 17993.081| 104.028| 462,789|
| |Apache County|   138| 1919.679| 15.898| 3,151| 43832.682| 311.998|  71,887|
| |Coconino County|   117| 815.467|  0.000| 3,065| 21362.458| 117.491| 143,476|
| |Yavapai County|    67| 284.986|  4.254| 1,966|  8362.435| 141.582| 235,099|
| |Cochise County|    52| 412.954|  4.538| 1,573| 12491.860| 79.414| 125,922|
| |Santa Cruz County|    52| 1118.328|  6.145| 2,651| 57013.205| 159.761|  46,498|
| |Gila County|    38| 703.469| 23.802|   887| 16420.452| 206.280|  54,018|
| |Graham County|    13| 334.732| 14.714|   529| 13621.031| 286.913|  38,837|
| |La Paz County|    12| 568.505| 13.536|   478| 22645.442| 60.911|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    58|  6106.549| 45.122|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,020| 378.623| N/A|190,772| 17967.825| N/A|10,617,423|
| |Fulton County|   420| 394.760|  4.162|19,647| 18466.319| 268.679|1,063,937|
| |Cobb County|   317| 417.028|  3.759|13,049| 17166.552| 346.364| 760,141|
| |Gwinnett County|   254| 271.295|  2.441|19,187| 20493.458| 313.866| 936,250|
| |DeKalb County|   237| 312.131|  2.822|13,509| 17791.457| 260.015| 759,297|
| |Dougherty County|   170| 1932.785|  3.248| 2,661| 30253.763| 146.177|  87,956|
| |Clayton County|   105| 359.274|  3.910| 4,879| 16694.268| 227.785| 292,256|
| |Muscogee County|    94| 480.158|  9.486| 4,595| 23471.540| 287.511| 195,769|
| |Hall County|    92| 450.008| 10.482| 5,947| 29089.077| 401.792| 204,441|
| |Richmond County|    88| 434.529|  6.349| 4,121| 20348.809| 450.754| 202,518|
| |Chatham County|    74| 255.675|  3.455| 5,526| 19092.699| 354.391| 289,430|
| |Troup County|    69| 986.814| 22.474| 2,257| 32278.825| 202.266|  69,922|
| |Bibb County|    67| 437.454|  7.462| 3,473| 22675.781| 392.682| 153,159|
| |Bartow County|    61| 566.188|  7.956| 1,816| 16855.706| 359.337| 107,738|
| |Cherokee County|    61| 235.728|  3.864| 3,269| 12632.694| 290.381| 258,773|
| |Sumter County|    56| 1896.762|  0.000|   749| 25369.191| 154.838|  29,524|
| |Houston County|    54| 342.069|  7.240| 1,898| 12023.083| 166.510| 157,863|
| |Douglas County|    50| 341.663|  1.952| 2,549| 17417.984| 296.759| 146,343|
| |Carroll County|    49| 408.361|  3.572| 1,842| 15351.023| 184.536| 119,992|
| |Habersham County|    48| 1058.948|  0.000| 1,125| 24819.096| 359.286|  45,328|
| |Henry County|    47| 200.374|  4.263| 3,252| 13864.197| 217.427| 234,561|
| |Glynn County|    47| 551.048| 31.823| 2,450| 28724.851| 334.984|  85,292|
| |Upson County|    46| 1747.720|  5.428|   507| 19262.918| 195.397|  26,320|
| |Thomas County|    42| 944.861|  9.641| 1,084| 24386.403| 453.147|  44,451|
| |Mitchell County|    41| 1875.314|  0.000|   642| 29364.680| 248.299|  21,863|
| |Spalding County|    41| 614.665|  6.425|   913| 13687.540| 162.768|  66,703|
| |Lowndes County|    40| 340.698| 10.951| 3,114| 26523.346| 267.691| 117,406|
| |Newton County|    39| 349.012|  8.949| 1,736| 15535.510| 259.522| 111,744|
| |Walton County|    39| 412.293|  7.551| 1,077| 11385.621| 267.311|  94,593|
| |Baldwin County|    38| 846.514|  0.000| 1,023| 22789.040| 337.333|  44,890|
| |Butts County|    37| 1483.799|  0.000|   482| 19329.483| 126.037|  24,936|
| |Tift County|    36| 885.740|  7.030| 1,313| 32304.891| 326.880|  40,644|
| |Hancock County|    35| 4138.583| 16.892|   308| 36419.534| 472.981|   8,457|
| |Early County|    32| 3140.334| 14.019|   355| 34838.077| 182.252|  10,190|
| |Barrow County|    32| 384.431|  0.000| 1,250| 15016.819| 324.363|  83,240|
| |Terrell County|    30| 3516.587|  0.000|   295| 34579.768| 100.474|   8,531|
| |Whitfield County|    29| 277.172|  5.462| 3,419| 32677.677| 488.807| 104,628|
| |Fayette County|    28| 244.710|  4.994| 1,078|  9421.347| 199.764| 114,421|
| |Randolph County|    26| 3835.940|  0.000|   268| 39539.687| 231.843|   6,778|
| |Ware County|    25| 699.614|  7.996| 1,125| 31482.622| 279.846|  35,734|
| |Monroe County|    25| 906.520| 10.360|   444| 16099.790| 186.484|  27,578|
| |Coffee County|    25| 577.727|  3.301| 1,433| 33115.338| 442.374|  43,273|
| |Jenkins County|    24| 2766.252| 32.932|   241| 27777.778| 263.453|   8,676|
| |Worth County|    23| 1135.971|  0.000|   440| 21731.615| 155.226|  20,247|
| |Gordon County|    23| 396.805|  0.000| 1,144| 19736.729| 391.876|  57,963|
| |Lee County|    22| 733.529|  0.000|   530| 17671.379| 138.132|  29,992|
| |Columbia County|    22| 140.383|  2.735| 2,134| 13617.162| 310.848| 156,714|
| |Forsyth County|    22| 90.071|  1.755| 2,143|  8773.725| 166.690| 244,252|
| |Coweta County|    22| 148.139|  2.886| 1,465|  9864.722| 162.568| 148,509|
| |Paulding County|    22| 130.435|  2.541| 1,615|  9575.080| 207.509| 168,667|
| |Colquitt County|    22| 482.456|  3.133| 1,532| 33596.491| 244.361|  45,600|
| |Appling County|    19| 1033.395| 23.310|   631| 34319.591| 590.511|  18,386|
| |Clarke County|    18| 140.262|  1.113| 1,968| 15335.344| 337.297| 128,331|
| |Brooks County|    18| 1164.521| 27.727|   391| 25295.982| 249.540|  15,457|
| |Turner County|    18| 2254.227|  0.000|   241| 30181.590| 339.923|   7,985|
| |Wilcox County|    18| 2084.540|  0.000|   176| 20382.166| 248.159|   8,635|
| |Putnam County|    18| 813.780|  6.459|   408| 18445.680| 284.177|  22,119|
| |Floyd County|    17| 172.592|  2.901| 1,428| 14497.756| 321.979|  98,498|
| |Rockdale County|    17| 187.027|  3.143| 1,270| 13972.012| 232.605|  90,896|
| |Walker County|    17| 243.689|  6.143|   658|  9432.204| 243.689|  69,761|
| |Harris County|    16| 454.081|  4.054|   645| 18305.142| 154.063|  35,236|
| |Oconee County|    15| 372.393|  0.000|   429| 10650.447| 180.877|  40,280|
| |Dooly County|    14| 1045.556|  0.000|   248| 18521.285| 96.020|  13,390|
| |Crisp County|    14| 625.782|  0.000|   371| 16583.229| 83.012|  22,372|
| |Jackson County|    14| 191.841|  1.958| 1,040| 14251.065| 250.568|  72,977|
| |Bulloch County|    14| 175.862|  5.384| 1,200| 15073.862| 260.204|  79,608|
| |Stephens County|    12| 462.874| 11.021|   599| 23105.111| 314.093|  25,925|
| |Peach County|    12| 435.635|  0.000|   364| 13214.260| 290.423|  27,546|
| |Greene County|    12| 654.879|  7.796|   297| 16208.251| 475.567|  18,324|
| |Polk County|    11| 258.137| 16.762|   765| 17952.268| 429.111|  42,613|
| |Lamar County|    11| 576.611| 14.977|   269| 14100.750| 374.422|  19,077|
| |Wilkinson County|    11| 1228.501| 15.955|   205| 22894.796| 526.501|   8,954|
| |Johnson County|    11| 1140.724| 29.629|   237| 24577.414| 325.921|   9,643|
| |McDuffie County|    10| 469.219|  6.703|   331| 15531.156| 341.860|  21,312|
| |Macon County|    10| 772.380|  0.000|   177| 13671.121| 66.204|  12,947|
| |Decatur County|    10| 378.730| 10.821|   750| 28404.787| 789.924|  26,404|
| |Catoosa County|     9| 133.175|  0.000|   609|  9011.542| 173.340|  67,580|
| |Screven County|     9| 644.422|  0.000|   189| 13532.866| 225.036|  13,966|
| |Emanuel County|     9| 397.421| 12.617|   469| 20710.059| 492.045|  22,646|
| |Wayne County|     8| 267.317| 19.094|   722| 24125.372| 778.084|  29,927|
| |Laurens County|     8| 168.258| 12.018|   865| 18192.908| 477.733|  47,546|
| |Jeff Davis County|     8| 529.276| 18.903|   429| 28382.402| 756.108|  15,115|
| |Bryan County|     8| 201.883|  3.605|   634| 15999.192| 374.925|  39,627|
| |Pierce County|     7| 359.620|  7.339|   392| 20138.711| 139.444|  19,465|
| |Oglethorpe County|     7| 458.746|  0.000|   211| 13827.905| 280.865|  15,259|
| |Union County|     7| 285.586|  5.828|   256| 10444.290| 343.869|  24,511|
| |Jefferson County|     7| 455.670| 18.599|   476| 30985.549| 548.664|  15,362|
| |Toombs County|     7| 260.902|  5.325|   710| 26462.915| 628.295|  26,830|
| |Telfair County|     7| 441.362|  9.007|   274| 17276.166| 207.170|  15,860|
| |Burke County|     7| 312.737|  0.000|   451| 20149.220| 389.326|  22,383|
| |Meriwether County|     6| 283.460|  6.749|   379| 17905.230| 215.970|  21,167|
| |Cook County|     6| 347.423|  0.000|   426| 24667.053| 264.703|  17,270|
| |Stewart County|     6| 906.208| 21.576|   255| 38513.820| 215.764|   6,621|
| |Calhoun County|     6| 969.462|  0.000|   201| 32476.975| 276.989|   6,189|
| |Bacon County|     6| 537.442|  0.000|   427| 38247.940| 294.313|  11,164|
| |Franklin County|     6| 256.970| 12.237|   390| 16703.071| 244.734|  23,349|
| |Lumpkin County|     6| 178.518|  0.000|   327|  9729.247| 153.016|  33,610|
| |Haralson County|     6| 201.396|  0.000|   207|  6948.174| 86.313|  29,792|
| |Hart County|     6| 228.964| 27.258|   292| 11142.912| 201.706|  26,205|
| |Bleckley County|     6| 466.092| 33.292|   181| 14060.437| 599.261|  12,873|
| |Madison County|     5| 167.336|  4.781|   375| 12550.201| 258.176|  29,880|
| |Camden County|     5| 91.465|  2.613|   725| 13262.357| 308.366|  54,666|
| |Grady County|     5| 202.980|  5.799|   471| 19120.692| 446.555|  24,633|
| |Seminole County|     5| 618.047| 52.975|   185| 22867.738| 882.924|   8,090|
| |Pickens County|     5| 153.417|  0.000|   362| 11107.361| 385.733|  32,591|
| |White County|     5| 162.348|  0.000|   347| 11266.965| 255.119|  30,798|
| |Pike County|     4| 210.948|  0.000|   203| 10705.622| 128.076|  18,962|
| |Marion County|     4| 478.526|  0.000|   147| 17585.836| 187.992|   8,359|
| |Lincoln County|     4| 504.987|  0.000|   134| 16917.056| 180.352|   7,921|
| |Clinch County|     4| 604.412|  0.000|   188| 28407.374| 410.137|   6,618|
| |Lanier County|     4| 383.767|  0.000|   214| 20531.517| 27.412|  10,423|
| |Candler County|     4| 370.268|  0.000|   245| 22678.885| 449.611|  10,803|
| |Gilmer County|     4| 127.514|  4.554|   583| 18585.227| 450.855|  31,369|
| |Brantley County|     4| 209.325|  0.000|   242| 12664.190| 171.946|  19,109|
| |Banks County|     4| 207.965|  7.427|   259| 13465.738| 178.256|  19,234|
| |Heard County|     4| 335.486| 11.982|   140| 11742.011| 143.780|  11,923|
| |Jones County|     3| 104.402|  0.000|   297| 10335.827| 218.748|  28,735|
| |Talbot County|     3| 484.262|  0.000|   134| 21630.347| 276.721|   6,195|
| |Twiggs County|     3| 369.458|  0.000|   111| 13669.951| 316.678|   8,120|
| |Rabun County|     3| 175.060|  0.000|   212| 12370.893| 216.741|  17,137|
| |Liberty County|     3| 48.832|  2.325|   695| 11312.770| 279.041|  61,435|
| |Charlton County|     3| 224.014|  0.000|   412| 30764.636| 682.710|  13,392|
| |Chattooga County|     3| 121.021|  5.763|   241|  9722.054| 380.353|  24,789|
| |Ben Hill County|     3| 179.641|  0.000|   393| 23532.934| 496.151|  16,700|
| |Baker County|     3| 987.492|  0.000|    63| 20737.327| 376.187|   3,038|
| |Treutlen County|     3| 434.720|  0.000|   113| 16374.438| 496.822|   6,901|
| |Fannin County|     3| 114.556|  5.455|   313| 11952.039| 256.388|  26,188|
| |Dodge County|     3| 145.596|  6.933|   209| 10143.169| 159.462|  20,605|
| |Wilkes County|     3| 306.843|  0.000|   187| 19126.521| 160.727|   9,777|
| |Dawson County|     3| 114.907|  0.000|   359| 13750.575| 377.553|  26,108|
| |Clay County|     2| 705.716|  0.000|    86| 30345.801| 705.716|   2,834|
| |Montgomery County|     2| 218.055| 31.151|   148| 16136.066| 373.808|   9,172|
| |Effingham County|     2| 31.106|  2.222|   703| 10933.806| 197.746|  64,296|
| |Echols County|     2| 499.251| 35.661|   220| 54917.624|  0.000|   4,006|
| |Atkinson County|     2| 244.948|  0.000|   312| 38211.880| 507.392|   8,165|
| |McIntosh County|     2| 139.101|  0.000|   167| 11614.967| 218.588|  14,378|
| |Murray County|     2| 49.880|  0.000|   575| 14340.583| 195.958|  40,096|
| |Pulaski County|     2| 179.582|  0.000|    96|  8619.916| 192.409|  11,137|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724| 164.393|   2,607|
| |Washington County|     2| 98.164|  0.000|   454| 22283.302| 378.634|  20,374|
| |Taylor County|     2| 249.377|  0.000|    81| 10099.751| 213.751|   8,020|
| |Chattahoochee County|     1| 91.684|  0.000|   736| 67479.600| 1859.880|  10,907|
| |Dade County|     1| 62.050|  0.000|   122|  7570.117| 132.965|  16,116|
| |Evans County|     1| 93.861|  0.000|   242| 22714.473| 536.351|  10,654|
| |Irwin County|     1| 106.202|  0.000|   160| 16992.353| 121.374|   9,416|
| |Jasper County|     1| 70.328|  0.000|   153| 10760.250| 321.501|  14,219|
| |Long County|     1| 51.127|  0.000|   118|  6033.028| 29.216|  19,559|
| |Quitman County|     1| 434.972|  0.000|    29| 12614.180|  0.000|   2,299|
| |Schley County|     1| 190.223|  0.000|    63| 11984.021| 380.445|   5,257|
| |Tattnall County|     1| 39.548|  0.000|   483| 19101.479| 502.819|  25,286|
| |Towns County|     1| 83.077|  0.000|   134| 11132.342| 320.441|  12,037|
| |Warren County|     1| 190.331| 27.190|    68| 12942.520| 407.853|   5,254|
| |Wheeler County|     1| 127.307|  0.000|    89| 11330.363| 90.934|   7,855|
| |Elbert County|     1| 52.100|  0.000|   348| 18130.666| 223.284|  19,194|
| |Taliaferro County|     0|  0.000|  0.000|    12|  7807.417|  0.000|   1,537|
| |Crawford County|     0|  0.000|  0.000|   101|  8142.535| 149.721|  12,404|
| |Berrien County|     0|  0.000|  0.000|   281| 14486.776| 184.123|  19,397|
| |Miller County|     0|  0.000|  0.000|   135| 23609.654| 249.838|   5,718|
| |Morgan County|     0|  0.000|  0.000|   253| 13125.130| 459.491|  19,276|
| |Glascock County|     0|  0.000|  0.000|    24|  8078.088| 144.252|   2,971|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,652| 312.428| N/A|98,675|  8441.625| N/A|11,689,100|
| |Franklin County|   522| 396.429|  1.193|18,006| 13674.515| 126.284|1,316,756|
| |Cuyahoga County|   498| 403.215|  3.239|13,269| 10743.503| 100.630|1,235,072|
| |Lucas County|   321| 749.391|  2.335| 5,207| 12156.004| 183.095| 428,348|
| |Mahoning County|   255| 1115.081|  3.123| 2,502| 10940.909| 81.835| 228,683|
| |Hamilton County|   253| 309.490|  1.398| 9,493| 11612.616| 90.173| 817,473|
| |Summit County|   220| 406.645|  1.056| 3,486|  6443.468| 78.688| 541,013|
| |Stark County|   139| 375.061|  3.084| 1,783|  4811.039| 53.966| 370,606|
| |Trumbull County|   106| 535.424|  4.330| 1,500|  7576.753| 77.211| 197,974|
| |Montgomery County|    91| 171.153|  5.642| 4,229|  7953.928| 81.412| 531,687|
| |Lorain County|    78| 251.749|  0.922| 1,713|  5528.785| 59.479| 309,833|
| |Butler County|    63| 164.433|  1.491| 2,861|  7467.361| 90.233| 383,134|
| |Portage County|    61| 375.463|  0.879|   746|  4591.730| 36.931| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,634| 16038.004| 96.750| 101,883|
| |Wayne County|    58| 501.253|  0.000|   525|  4537.205| 49.385| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,013|  7743.642| 145.241| 130,817|
| |Licking County|    49| 277.052|  7.270| 1,224|  6920.650| 115.506| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   559|  5748.604| 36.728|  97,241|
| |Marion County|    45| 691.319|  2.195| 2,919| 44843.532| 129.485|  65,093|
| |Geauga County|    44| 469.840|  1.525|   552|  5894.350| 50.340|  93,649|
| |Allen County|    44| 429.893|  2.792|   718|  7015.076| 125.618| 102,351|
| |Pickaway County|    42| 718.477|  0.000| 2,380| 40713.687| 85.533|  58,457|
| |Lake County|    38| 165.110|  2.483| 1,087|  4723.027| 49.037| 230,149|
| |Warren County|    38| 161.976|  1.827| 1,742|  7425.342| 116.306| 234,602|
| |Miami County|    38| 355.183|  2.671|   819|  7655.136| 96.140| 106,987|
| |Medina County|    35| 194.719|  1.590|   896|  4984.812| 66.761| 179,746|
| |Fairfield County|    31| 196.733|  8.159| 1,332|  8453.171| 105.166| 157,574|
| |Erie County|    27| 363.558|  1.924|   564|  7594.323| 125.033|  74,266|
| |Darke County|    27| 528.241|  0.000|   385|  7532.330| 204.030|  51,113|
| |Ottawa County|    26| 641.579|  3.525|   371|  9154.843| 105.755|  40,525|
| |Belmont County|    26| 388.025|  0.000|   614|  9163.359| 53.300|  67,006|
| |Washington County|    22| 367.211|  2.384|   200|  3338.285| 19.076|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,273|  6085.755| 71.710| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    91|  6664.714| 20.925|  13,654|
| |Putnam County|    17| 502.053|  0.000|   202|  5965.565| 59.065|  33,861|
| |Sandusky County|    16| 273.420|  0.000|   368|  6288.663| 129.386|  58,518|
| |Clark County|    14| 104.413|  1.065| 1,133|  8449.990| 79.908| 134,083|
| |Tuscarawas County|    14| 152.195|  1.553|   772|  8392.490| 55.909|  91,987|
| |Mercer County|    13| 315.749|  0.000|   591| 14354.416| 322.688|  41,172|
| |Hardin County|    12| 382.592|  0.000|   161|  5133.110| 54.656|  31,365|
| |Greene County|    12| 71.032|  0.846|   662|  3918.621| 43.972| 168,937|
| |Clermont County|    11| 53.287|  0.692|   902|  4369.562| 69.204| 206,428|
| |Richland County|    11| 90.794|  1.179|   596|  4919.359| 83.719| 121,154|
| |Madison County|    10| 223.559|  0.000|   353|  7891.619| 127.748|  44,731|
| |Hocking County|     9| 318.426|  0.000|   115|  4068.780| 45.489|  28,264|
| |Wyandot County|     8| 367.444| 19.685|   142|  6522.139| 150.915|  21,772|
| |Knox County|     7| 112.320| 11.461|   199|  3193.094| 103.151|  62,322|
| |Guernsey County|     7| 180.064|  3.675|   116|  2983.923| 33.073|  38,875|
| |Coshocton County|     6| 163.934|  0.000|   190|  5191.257| 19.516|  36,600|
| |Auglaize County|     6| 131.418|  3.129|   244|  5344.314| 137.676|  45,656|
| |Holmes County|     6| 136.488|  0.000|   327|  7438.581| 29.247|  43,960|
| |Clinton County|     6| 142.966|  0.000|   158|  3764.773| 47.655|  41,968|
| |Carroll County|     5| 185.777|  0.000|   110|  4087.092| 15.924|  26,914|
| |Crawford County|     5| 120.499|  0.000|   172|  4145.178| 30.986|  41,494|
| |Huron County|     5| 85.813|  2.452|   393|  6744.928| 58.843|  58,266|
| |Defiance County|     4| 105.023|  0.000|   139|  3649.539| 45.010|  38,087|
| |Shelby County|     4| 82.321|  0.000|   186|  3827.948| 111.722|  48,590|
| |Ross County|     4| 52.174|  0.000|   450|  5869.616| 141.616|  76,666|
| |Williams County|     3| 81.762|  0.000|   132|  3597.514| 58.401|  36,692|
| |Seneca County|     3| 54.369|  0.000|   196|  3552.140| 144.985|  55,178|
| |Perry County|     3| 83.024|  7.907|   121|  3348.647| 83.024|  36,134|
| |Hancock County|     3| 39.587|  1.885|   355|  4684.428| 98.024|  75,783|
| |Ashland County|     3| 56.092|  0.000|   140|  2617.605| 37.394|  53,484|
| |Jefferson County|     2| 30.616|  0.000|   219|  3352.468| 50.298|  65,325|
| |Henry County|     2| 74.058|  5.290|   115|  4258.313| 74.058|  27,006|
| |Morrow County|     2| 56.612|  0.000|   168|  4755.435| 44.481|  35,328|
| |Logan County|     2| 43.791|  3.128|   145|  3174.812| 96.965|  45,672|
| |Vinton County|     2| 152.847|  0.000|    30|  2292.702| 10.918|  13,085|
| |Adams County|     2| 72.207|  0.000|    59|  2130.118| 30.946|  27,698|
| |Champaign County|     2| 51.434|  3.674|   159|  4088.980| 209.409|  38,885|
| |Preble County|     2| 48.921|  0.000|   180|  4402.916| 90.854|  40,882|
| |Brown County|     2| 46.049|  3.289|   126|  2901.087| 62.495|  43,432|
| |Athens County|     1| 15.308|  0.000|   356|  5449.508| 37.176|  65,327|
| |Scioto County|     1| 13.278|  0.000|   222|  2947.659| 81.563|  75,314|
| |Van Wert County|     1| 35.367|  0.000|    71|  2511.052| 30.315|  28,275|
| |Highland County|     1| 23.169|  0.000|   148|  3429.022| 99.296|  43,161|
| |Union County|     1| 16.953|  0.000|   237|  4017.766| 67.810|  58,988|
| |Harrison County|     1| 66.489|  0.000|    24|  1595.745| 47.492|  15,040|
| |Gallia County|     1| 33.447|  0.000|    62|  2073.717| 62.116|  29,898|
| |Fulton County|     1| 23.738|  0.000|   147|  3489.531| 33.912|  42,126|
| |Muskingum County|     1| 11.599|  0.000|   221|  2563.359| 81.192|  86,215|
| |Jackson County|     0|  0.000|  0.000|    73|  2252.183| 39.667|  32,413|
| |Lawrence County|     0|  0.000|  0.000|   267|  4490.187| 146.550|  59,463|
| |Meigs County|     0|  0.000|  0.000|    36|  1571.572| 81.073|  22,907|
| |Morgan County|     0|  0.000|  0.000|    25|  1723.187| 78.774|  14,508|
| |Noble County|     0|  0.000|  0.000|    16|  1109.262|  0.000|  14,424|
| |Paulding County|     0|  0.000|  0.000|    65|  3481.148| 53.556|  18,672|
| |Pike County|     0|  0.000|  0.000|    76|  2736.569| 77.159|  27,772|
| |Fayette County|     0|  0.000|  0.000|   110|  3856.266| 110.179|  28,525|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,546| 586.535| N/A|93,806| 15516.203| N/A|6,045,680|
| |Baltimore County|   983| 1188.102|  5.007|25,154| 30402.359| 370.192| 827,370|
| |Montgomery County|   801| 762.358|  1.632|18,139| 17263.926| 77.636|1,050,688|
| |Prince George's County|   749| 823.686|  1.885|23,372| 25702.525| 150.190| 909,327|
| |Anne Arundel County|   222| 383.265|  1.480| 7,243| 12504.446| 116.657| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,050| 11751.244| 35.226| 259,547|
| |Carroll County|   117| 694.580|  0.848| 1,530|  9082.976| 68.695| 168,447|
| |Howard County|   106| 325.463|  0.000| 3,779| 11603.058| 109.219| 325,690|
| |Charles County|    91| 557.403|  0.000| 1,983| 12146.493| 132.132| 163,257|
| |Harford County|    69| 270.121|  1.119| 1,922|  7524.242| 96.192| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   962|  8475.024| 83.064| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,322| 12759.509| 59.289| 103,609|
| |Washington County|    31| 205.231|  0.946| 1,003|  6640.229| 48.234| 151,049|
| |Cecil County|    30| 291.673|  0.000|   689|  6698.751| 93.057| 102,855|
| |Calvert County|    28| 302.621|  0.000|   672|  7262.902| 129.695|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   420|  8336.476| 104.915|  50,381|
| |Kent County|    23| 1184.224|  0.000|   238| 12254.145| 44.133|  19,422|
| |Worcester County|    20| 382.585|  5.465|   675| 12912.235| 341.594|  52,276|
| |Allegany County|    18| 255.624|  0.000|   280|  3976.369| 28.403|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   365| 11431.614| 111.855|  31,929|
| |Talbot County|     4| 107.582|  0.000|   384| 10327.856| 169.057|  37,181|
| |Caroline County|     3| 89.804|  0.000|   445| 13320.960| 94.081|  33,406|
| |Somerset County|     3| 117.114|  0.000|   133|  5192.067| 78.076|  25,616|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    46|  1585.442|  4.924|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,821| 419.030| N/A|72,254| 10732.568| N/A|6,732,219|
| |Marion County|   725| 751.621|  1.037|15,503| 16072.247| 158.618| 964,582|
| |Lake County|   274| 564.375|  2.060| 7,447| 15339.047| 150.657| 485,493|
| |Allen County|   161| 424.467|  1.507| 3,789|  9989.481| 105.458| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,719| 10868.259| 93.030| 158,167|
| |Hendricks County|   106| 622.391|  0.839| 1,833| 10762.664| 102.334| 170,311|
| |Hamilton County|   105| 310.641|  0.423| 2,668|  7893.234| 109.041| 338,011|
| |Elkhart County|    82| 397.400|  4.154| 4,760| 23068.610| 165.468| 206,341|
| |St. Joseph County|    81| 297.985|  1.051| 3,373| 12408.673| 188.146| 271,826|
| |Madison County|    65| 501.663|  1.103|   915|  7061.874| 113.563| 129,569|
| |Howard County|    65| 787.459|  1.731|   872| 10564.063| 148.838|  82,544|
| |Delaware County|    52| 455.601|  0.000|   701|  6141.850| 108.894| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   766|  9143.103| 73.322|  83,779|
| |Boone County|    46| 678.036|  0.000|   662|  9757.823| 103.179|  67,843|
| |Clark County|    46| 388.835|  1.208| 1,178|  9957.566| 187.172| 118,302|
| |Floyd County|    45| 573.088|  1.819|   760|  9678.816| 185.571|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,266|  7430.057| 114.025| 170,389|
| |Hancock County|    38| 486.132|  1.828|   641|  8200.287| 80.413|  78,168|
| |Morgan County|    34| 482.345|  4.053|   459|  6511.654| 99.306|  70,489|
| |Greene County|    34| 1065.096|  0.000|   246|  7706.284| 58.178|  31,922|
| |Decatur County|    32| 1204.865|  0.000|   332| 12500.471| 139.850|  26,559|
| |Grant County|    30| 456.142|  2.172|   521|  7921.665| 60.819|  65,769|
| |Warrick County|    30| 476.206|  2.268|   570|  9047.906| 224.497|  62,998|
| |Monroe County|    30| 202.114|  0.000|   722|  4864.213| 58.709| 148,431|
| |LaPorte County|    30| 273.005|  1.300|   883|  8035.454| 107.902| 109,888|
| |Noble County|    29| 607.406|  2.992|   659| 13802.782| 125.670|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   493|  9968.054| 132.869|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   336|  7405.775| 59.826|  45,370|
| |Shelby County|    27| 603.635|  3.194|   542| 12117.418| 134.141|  44,729|
| |Orange County|    24| 1221.623|  0.000|   166|  8449.557| 58.173|  19,646|
| |Harrison County|    23| 567.691|  3.526|   321|  7922.991| 183.354|  40,515|
| |Marshall County|    22| 475.593|  0.000|   771| 16667.387| 120.442|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   348|  9077.156| 52.168|  38,338|
| |Henry County|    20| 416.910|  5.956|   373|  7775.369| 50.625|  47,972|
| |Daviess County|    20| 599.682|  4.283|   263|  7885.821| 119.936|  33,351|
| |Franklin County|    13| 571.228| 25.109|   238| 10457.861| 295.030|  22,758|
| |Vanderburgh County|    13| 71.645|  2.362| 1,888| 10405.013| 210.210| 181,451|
| |Dubois County|    12| 280.794|  0.000|   676| 15818.046| 237.338|  42,736|
| |Kosciusko County|    12| 151.027|  0.000|   840| 10571.889| 79.109|  79,456|
| |Jennings County|    12| 432.666|  0.000|   220|  7932.216| 72.111|  27,735|
| |Perry County|    12| 626.011|  0.000|   181|  9442.329| 81.978|  19,169|
| |Tippecanoe County|    11| 56.199|  0.000| 1,177|  6013.324| 90.503| 195,732|
| |Newton County|    10| 715.103|  0.000|   115|  8223.684| 71.510|  13,984|
| |LaGrange County|    10| 252.436|  0.000|   556| 14035.442| 72.125|  39,614|
| |White County|    10| 414.903|  0.000|   354| 14687.578| 77.053|  24,102|
| |Vigo County|    10| 93.425|  0.000|   586|  5474.691| 216.212| 107,038|
| |Wayne County|    10| 151.782|  2.168|   354|  5373.080| 108.416|  65,884|
| |Scott County|    10| 418.883|  0.000|   263| 11016.630| 119.681|  23,873|
| |Cass County|     9| 238.796|  0.000| 1,774| 47069.437| 128.874|  37,689|
| |Putnam County|     8| 212.902|  0.000|   286|  7611.241| 262.325|  37,576|
| |Starke County|     7| 304.414|  0.000|   176|  7653.838| 124.251|  22,995|
| |Ripley County|     7| 247.140|  0.000|   197|  6955.232| 60.524|  28,324|
| |Fayette County|     7| 303.004|  0.000|   183|  7921.392| 210.248|  23,102|
| |Tipton County|     6| 396.092|  9.431|   133|  8780.037| 348.938|  15,148|
| |Whitley County|     6| 176.658|  0.000|   150|  4416.441| 29.443|  33,964|
| |Jackson County|     5| 113.043|  3.230|   572| 12932.106| 93.664|  44,231|
| |Clay County|     5| 190.658|  0.000|   109|  4156.339| 81.710|  26,225|
| |Gibson County|     4| 118.839|  4.244|   214|  6357.883| 84.885|  33,659|
| |Ohio County|     4| 680.851|  0.000|    62| 10553.191| 462.006|   5,875|
| |DeKalb County|     4| 92.007|  0.000|   226|  5198.390| 46.003|  43,475|
| |Rush County|     4| 241.240|  0.000|    74|  4462.940|  0.000|  16,581|
| |Randolph County|     4| 162.173|  0.000|   115|  4662.477| 81.087|  24,665|
| |Huntington County|     3| 82.147|  0.000|   121|  3313.253|  7.824|  36,520|
| |Spencer County|     3| 147.951|  0.000|   131|  6460.522| 147.951|  20,277|
| |Clinton County|     3| 92.595|  0.000|   409| 12623.846| 299.833|  32,399|
| |Steuben County|     3| 86.720|  0.000|   206|  5954.790| 53.684|  34,594|
| |Wabash County|     3| 96.787|  0.000|   163|  5258.743| 55.307|  30,996|
| |Blackford County|     2| 170.097|  0.000|    62|  5273.006| 133.648|  11,758|
| |Adams County|     2| 55.902|  0.000|    95|  2655.337| 83.853|  35,777|
| |Fulton County|     2| 100.130|  7.152|   161|  8060.479| 193.108|  19,974|
| |Jasper County|     2| 59.591|  0.000|   227|  6763.602| 127.695|  33,562|
| |Jefferson County|     2| 61.904|  0.000|   155|  4797.573| 44.217|  32,308|
| |Wells County|     2| 70.681|  0.000|   162|  5725.191| 191.849|  28,296|
| |Miami County|     2| 56.313|  0.000|   267|  7517.738| 80.447|  35,516|
| |Carroll County|     2| 98.731|  0.000|   177|  8737.720| 345.560|  20,257|
| |Fountain County|     2| 122.354|  0.000|    68|  4160.039| 61.177|  16,346|
| |Sullivan County|     1| 48.382|  0.000|   103|  4983.308| 234.997|  20,669|
| |Pulaski County|     1| 80.952|  0.000|    76|  6152.352| 57.823|  12,353|
| |Warren County|     1| 120.992|  0.000|    22|  2661.827| 51.854|   8,265|
| |Washington County|     1| 35.668|  0.000|   131|  4672.564| 137.578|  28,036|
| |Brown County|     1| 66.260|  0.000|    73|  4837.000| 47.329|  15,092|
| |Parke County|     1| 59.042|  0.000|    51|  3011.159| 50.608|  16,937|
| |Owen County|     1| 48.079|  0.000|    84|  4038.656| 75.553|  20,799|
| |Union County|     0|  0.000|  0.000|    37|  5245.251| 182.267|   7,054|
| |Switzerland County|     0|  0.000|  0.000|    45|  4185.657| 66.439|  10,751|
| |Vermillion County|     0|  0.000|  0.000|    50|  3226.223| 184.356|  15,498|
| |Martin County|     0|  0.000|  0.000|    43|  4193.077| 13.930|  10,255|
| |Knox County|     0|  0.000|  0.000|   149|  4071.706| 93.692|  36,594|
| |Jay County|     0|  0.000|  0.000|    86|  4208.260| 41.943|  20,436|
| |Benton County|     0|  0.000|  0.000|    60|  6858.711| 16.330|   8,748|
| |Crawford County|     0|  0.000|  0.000|    44|  4159.970| 54.026|  10,577|
| |Posey County|     0|  0.000|  0.000|   167|  6567.822| 67.420|  25,427|
| |Pike County|     0|  0.000|  0.000|    52|  4197.272| 172.964|  12,389|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,317| 271.454| N/A|97,882| 11467.610| N/A|8,535,519|
| |Fairfax County|   537| 467.961|  1.245|16,325| 14226.183| 78.429|1,147,532|
| |Henrico County|   184| 556.197|  1.727| 3,811| 11519.929| 116.594| 330,818|
| |Prince William County|   177| 376.328|  2.126| 9,340| 19858.186| 152.475| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,037| 12822.895| 84.444| 236,842|
| |Loudoun County|   115| 278.088|  1.727| 5,196| 12564.746| 69.436| 413,538|
| |Chesterfield County|    80| 226.756|  3.239| 4,283| 12139.954| 140.103| 352,802|
| |Alexandria city|    60| 376.345|  1.792| 2,917| 18296.661| 106.631| 159,428|
| |Virginia Beach city|    53| 117.785|  2.540| 4,781| 10625.058| 230.490| 449,974|
| |Suffolk city|    49| 531.984|  0.000| 1,231| 13364.746| 305.542|  92,108|
| |Richmond County|    45| 4987.255| 31.665| 3,430| 380139.643| 3498.995|   9,023|
| |Shenandoah County|    43| 985.877|  3.275|   690| 15819.883| 75.333|  43,616|
| |Chesapeake city|    37| 151.122|  5.251| 2,828| 11550.636| 220.557| 244,835|
| |Spotsylvania County|    35| 256.947|  2.098| 1,449| 10637.595| 151.022| 136,215|
| |Mecklenburg County|    32| 1046.196|  0.000|   385| 12587.047| 382.982|  30,587|
| |Hanover County|    32| 296.940|  1.326|   637|  5910.955| 70.258| 107,766|
| |Harrisonburg city|    31| 584.729|  5.389| 1,075| 20276.898| 97.006|  53,016|
| |Norfolk city|    30| 123.588|  3.531| 3,629| 14950.029| 264.243| 242,742|
| |Northampton County|    29| 2476.516| 12.200|   295| 25192.143| 36.599|  11,710|
| |Portsmouth city|    25| 264.836|  4.540| 1,726| 18284.286| 399.524|  94,398|
| |Galax city|    24| 3781.314| 112.539|   348| 54829.053| 382.633|   6,347|
| |Page County|    24| 1004.100|  0.000|   337| 14099.239| 41.838|  23,902|
| |Manassas city|    21| 511.135|  3.477| 1,636| 39819.886| 111.268|  41,085|
| |Colonial Heights city|    21| 1208.981|  0.000|   195| 11226.252| 139.814|  17,370|
| |Rockingham County|    19| 231.854|  3.487|   933| 11385.269| 74.960|  81,948|
| |Petersburg city|    19| 606.138| 36.459|   506| 16142.411| 291.675|  31,346|
| |Roanoke County|    18| 191.111|  0.000| 1,495| 15872.847| 380.706|  94,186|
| |Newport News city|    18| 100.432|  1.594| 1,788|  9976.287| 171.373| 179,225|
| |James City County|    16| 209.087|  0.000|   596|  7788.508| 108.277|  76,523|
| |Accomack County|    16| 495.111|  4.421| 1,087| 33636.589| 57.468|  32,316|
| |Albemarle County|    16| 146.346|  6.533|   817|  7472.789| 107.146| 109,330|
| |Emporia city|    15| 2805.836|  0.000|   174| 32547.699| 293.945|   5,346|
| |Charlottesville city|    15| 317.353| 12.090|   520| 11001.566| 163.210|  47,266|
| |Nottoway County|    13| 853.466| 37.515|   181| 11882.878| 84.409|  15,232|
| |Southampton County|    13| 737.338|  8.103|   257| 14576.598| 186.360|  17,631|
| |Culpeper County|    12| 228.115|  0.000|   988| 18781.485| 124.920|  52,605|
| |Carroll County|    12| 402.806|  0.000|   321| 10775.066| 67.134|  29,791|
| |Greensville County|    11| 970.360| 25.204|   452| 39872.971| 441.073|  11,336|
| |Prince Edward County|    10| 438.558|  6.265|   397| 17410.753| 463.618|  22,802|
| |Fluvanna County|     9| 330.033|  5.239|   184|  6747.341| 57.625|  27,270|
| |Fauquier County|     9| 126.365|  2.006|   606|  8508.607| 70.203|  71,222|
| |Sussex County|     9| 806.524|  0.000|   290| 25987.992| 179.228|  11,159|
| |Frederick County|     9| 100.769|  3.199|   680|  7613.673| 46.386|  89,313|
| |Isle of Wight County|     9| 242.529|  0.000|   378| 10186.208| 204.032|  37,109|
| |Stafford County|     8| 52.328|  0.934| 1,350|  8830.340| 99.984| 152,882|
| |Buckingham County|     8| 466.527| 16.662|   601| 35047.819| 66.647|  17,148|
| |Goochland County|     7| 294.700|  0.000|   159|  6693.891| 54.129|  23,753|
| |Dinwiddie County|     7| 245.235| 15.014|   212|  7427.130| 75.072|  28,544|
| |Danville city|     7| 174.808|  7.135|   386|  9639.397| 306.805|  40,044|
| |Manassas Park city|     7| 400.503|  0.000|   507| 29007.896| 81.735|  17,478|
| |Bedford County|     7| 88.611|  1.808|   341|  4316.620| 99.461|  78,997|
| |Franklin County|     7| 124.906|  0.000|   342|  6102.566| 183.536|  56,042|
| |Henry County|     7| 138.458|  5.651|   573| 11333.742| 271.264|  50,557|
| |Hampton city|     7| 52.041|  2.124| 1,173|  8720.541| 176.301| 134,510|
| |Botetourt County|     7| 209.462|  8.549|   210|  6283.851| 106.868|  33,419|
| |Williamsburg city|     6| 401.230|  0.000|   121|  8091.481| 133.743|  14,954|
| |Falls Church city|     6| 410.481|  0.000|    60|  4104.809|  0.000|  14,617|
| |Warren County|     6| 149.388|  0.000|   354|  8813.863| 21.341|  40,164|
| |Washington County|     5| 93.041|  2.658|   211|  3926.312| 108.990|  53,740|
| |Hopewell city|     5| 221.936|  0.000|   265| 11762.617| 69.751|  22,529|
| |Lynchburg city|     5| 60.851|  5.216|   553|  6730.114| 215.586|  82,168|
| |Grayson County|     5| 321.543|  9.187|   148|  9517.685| 183.739|  15,550|
| |Caroline County|     5| 162.734|  4.650|   200|  6509.357| 79.042|  30,725|
| |Charles City County|     5| 718.081| 41.033|    51|  7324.429| 41.033|   6,963|
| |Alleghany County|     4| 269.179|  9.614|    61|  4104.980| 48.068|  14,860|
| |York County|     4| 58.582|  2.092|   355|  5199.180| 112.980|  68,280|
| |Winchester city|     4| 142.460|  0.000|   399| 14210.414| 40.703|  28,078|
| |Augusta County|     4| 52.939|  0.000|   264|  3494.005| 28.360|  75,558|
| |Patrick County|     4| 227.169|  8.113|   134|  7610.177| 210.943|  17,608|
| |King George County|     4| 149.054|  0.000|   137|  5105.083| 79.850|  26,836|
| |Powhatan County|     4| 134.898|  0.000|   141|  4755.160| 91.538|  29,652|
| |Salem city|     3| 118.572|  0.000|   157|  6205.288| 146.804|  25,301|
| |Waynesboro city|     3| 132.567|  6.313|   168|  7423.774| 12.625|  22,630|
| |Martinsville city|     3| 238.968|  0.000|   196| 15612.554| 421.038|  12,554|
| |Orange County|     3| 80.969|  0.000|   226|  6099.700| 73.258|  37,051|
| |Wythe County|     3| 104.588|  0.000|   112|  3904.616| 59.765|  28,684|
| |Wise County|     3| 80.250|  0.000|   117|  3129.765| 145.215|  37,383|
| |Westmoreland County|     3| 166.528|  7.930|   202| 11212.878| 71.369|  18,015|
| |Smyth County|     3| 99.655|  0.000|   140|  4650.545| 156.600|  30,104|
| |Scott County|     3| 139.108|  0.000|    85|  3941.389| 225.222|  21,566|
| |Pulaski County|     3| 88.165|  0.000|    84|  2468.628| 41.983|  34,027|
| |Fredericksburg city|     3| 103.320|  4.920|   396| 13638.242| 236.160|  29,036|
| |Montgomery County|     3| 30.446|  0.000|   301|  3054.752| 40.595|  98,535|
| |Pittsylvania County|     2| 33.138|  0.000|   418|  6925.804| 241.433|  60,354|
| |Brunswick County|     2| 123.221|  8.801|   226| 13923.973| 255.243|  16,231|
| |Campbell County|     2| 36.440|  0.000|   190|  3461.784| 119.731|  54,885|
| |Amelia County|     2| 152.149| 10.868|    78|  5933.815| 65.207|  13,145|
| |Prince George County|     2| 52.147|  0.000|   377|  9829.740| 178.790|  38,353|
| |Northumberland County|     2| 165.358|  0.000|    70|  5787.516| 82.679|  12,095|
| |Russell County|     2| 75.228|  5.373|   101|  3798.992| 220.309|  26,586|
| |Louisa County|     2| 53.204|  0.000|   181|  4814.982| 60.805|  37,591|
| |Surry County|     2| 311.429|  0.000|    47|  7318.592| 266.940|   6,422|
| |King William County|     2| 116.632|  0.000|    83|  4840.215| 49.985|  17,148|
| |Rappahannock County|     2| 271.370|  0.000|    41|  5563.094| 19.384|   7,370|
| |Greene County|     2| 100.913|  0.000|   153|  7719.865| 136.954|  19,819|
| |Floyd County|     2| 126.992|  9.071|    51|  3238.301| 172.347|  15,749|
| |Gloucester County|     2| 53.550|  0.000|   152|  4069.830| 42.075|  37,348|
| |Buena Vista city|     1| 154.369| 22.053|    50|  7718.432| 66.158|   6,478|
| |Halifax County|     1| 29.489|  0.000|   152|  4482.321| 92.680|  33,911|
| |New Kent County|     1| 43.307|  0.000|   124|  5370.058| 55.680|  23,091|
| |Rockbridge County|     1| 44.301|  6.329|    66|  2923.847|  0.000|  22,573|
| |Lee County|     1| 42.693|  0.000|   110|  4696.239| 115.881|  23,423|
| |King and Queen County|     1| 142.349|  0.000|    39|  5551.601| 81.342|   7,025|
| |Middlesex County|     1| 94.500|  0.000|    34|  3213.003| 108.000|  10,582|
| |Essex County|     1| 91.299|  0.000|    94|  8582.124| 247.812|  10,953|
| |Dickenson County|     1| 69.842|  9.977|    38|  2654.002| 159.639|  14,318|
| |Lunenburg County|     1| 81.994|  0.000|    60|  4919.646| 58.567|  12,196|
| |Madison County|     1| 75.409|  0.000|    66|  4977.000| 64.636|  13,261|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Bland County|     0|  0.000|  0.000|    11|  1751.592| 90.992|   6,280|
| |Buchanan County|     0|  0.000|  0.000|    78|  3713.578| 47.610|  21,004|
| |Charlotte County|     0|  0.000|  0.000|    52|  4377.104| 24.050|  11,880|
| |Staunton city|     0|  0.000|  0.000|   147|  5896.037| 40.109|  24,932|
| |Clarke County|     0|  0.000|  0.000|    70|  4788.289|  9.772|  14,619|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 55.684|   5,131|
| |Cumberland County|     0|  0.000|  0.000|    75|  7551.349| 143.835|   9,932|
| |Mathews County|     0|  0.000|  0.000|    17|  1924.383| 80.856|   8,834|
| |Bristol city|     0|  0.000|  0.000|    76|  4534.065| 161.931|  16,762|
| |Nelson County|     0|  0.000|  0.000|    39|  2612.190| 66.979|  14,930|
| |Tazewell County|     0|  0.000|  0.000|   116|  2857.495| 102.053|  40,595|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Norton city|     0|  0.000|  0.000|    18|  4521.477| 251.193|   3,981|
| |Poquoson city|     0|  0.000|  0.000|    43|  3504.197| 81.493|  12,271|
| |Radford city|     0|  0.000|  0.000|    48|  2630.281| 164.393|  18,249|
| |Amherst County|     0|  0.000|  0.000|   154|  4872.647| 221.484|  31,605|
| |Appomattox County|     0|  0.000|  0.000|    83|  5216.517| 134.678|  15,911|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Giles County|     0|  0.000|  0.000|    23|  1375.598|  0.000|  16,720|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 195.695|   2,190|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910| 95.929|   7,446|
| |Lancaster County|     0|  0.000|  0.000|    35|  3300.953| 80.840|  10,603|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,160| 205.948| N/A|133,337| 12713.190| N/A|10,488,084|
| |Mecklenburg County|   225| 202.638|  3.345|21,876| 19701.789| 176.777|1,110,356|
| |Wake County|   164| 147.514|  4.626|11,774| 10590.406| 117.574|1,111,761|
| |Guilford County|   154| 286.686|  3.191| 5,498| 10235.045| 107.707| 537,174|
| |Durham County|    79| 245.732|  0.889| 6,080| 18912.059| 141.752| 321,488|
| |Henderson County|    54| 459.899|  1.217| 1,459| 12425.799| 139.916| 117,417|
| |Robeson County|    53| 405.742|  2.187| 2,745| 21014.354| 199.043| 130,625|
| |Forsyth County|    52| 136.021|  1.121| 5,148| 13466.041| 117.710| 382,295|
| |Chatham County|    52| 698.268|  3.837| 1,290| 17322.412| 157.302|  74,470|
| |Cumberland County|    51| 152.008|  0.426| 3,021|  9004.229| 163.930| 335,509|
| |Cabarrus County|    49| 226.377|  4.620| 2,594| 11984.126| 166.318| 216,453|
| |Duplin County|    48| 817.146| 14.592| 1,970| 33537.052| 138.623|  58,741|
| |Columbus County|    48| 864.740|  7.721|   881| 15871.586| 190.449|  55,508|
| |Rowan County|    48| 337.819|  0.000| 2,151| 15138.506| 195.050| 142,088|
| |Buncombe County|    47| 179.945|  0.547| 1,815|  6948.938| 114.858| 261,191|
| |Gaston County|    47| 209.327|  8.908| 3,263| 14532.644| 206.146| 224,529|
| |Orange County|    47| 316.549|  1.924| 1,329|  8950.942| 60.616| 148,476|
| |Johnston County|    46| 219.739|  1.365| 3,207| 15319.649| 189.713| 209,339|
| |Union County|    42| 175.103|  1.787| 3,016| 12574.054| 176.294| 239,859|
| |Alamance County|    41| 241.875|  0.000| 2,365| 13952.062| 182.881| 169,509|
| |Vance County|    40| 898.170|  0.000|   759| 17042.775| 121.894|  44,535|
| |Wayne County|    40| 324.857|  3.481| 2,401| 19499.557| 134.584| 123,131|
| |Harnett County|    39| 286.815|  3.152| 1,243|  9141.319| 156.540| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,149| 14958.202| 122.307| 143,667|
| |Wilson County|    35| 427.868|  3.493| 1,476| 18043.789| 185.118|  81,801|
| |Catawba County|    29| 181.760|  4.477| 2,074| 12998.978| 192.505| 159,551|
| |Burke County|    28| 309.444|  4.736| 1,637| 18091.396| 157.879|  90,485|
| |Granville County|    27| 446.702|  4.727| 1,227| 20300.117| 196.171|  60,443|
| |Franklin County|    25| 358.757|  0.000|   846| 12140.346| 172.203|  69,685|
| |Stanly County|    24| 382.129| 29.570| 1,026| 16336.019| 363.932|  62,806|
| |New Hanover County|    20| 85.298|  0.609| 2,566| 10943.691| 171.205| 234,473|
| |Moore County|    20| 198.255|  0.000|   980|  9714.512| 152.940| 100,880|
| |Brunswick County|    20| 140.036|  4.001| 1,234|  8640.246| 69.018| 142,820|
| |Pasquotank County|    19| 477.099|  7.174|   388|  9742.869| 150.663|  39,824|
| |Davidson County|    18| 107.393|  0.852| 1,730| 10321.641| 93.756| 167,609|
| |Cleveland County|    18| 183.773|  5.834| 1,143| 11669.576| 261.074|  97,947|
| |Iredell County|    18| 99.007|  0.000| 1,782|  9801.657| 95.078| 181,806|
| |Northampton County|    16| 821.229|  0.000|   334| 17143.150| 197.975|  19,483|
| |Caldwell County|    14| 170.362|  3.477| 1,197| 14565.942| 194.699|  82,178|
| |Rutherford County|    14| 208.865|  2.131|   707| 10547.673| 168.371|  67,029|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 394.299|  27,173|
| |Sampson County|    14| 220.365|  4.497| 1,455| 22902.205| 98.939|  63,531|
| |McDowell County|    13| 284.116| 15.611|   675| 14752.164| 318.459|  45,756|
| |Haywood County|    12| 192.564| 20.632|   393|  6306.465| 268.214|  62,317|
| |Nash County|    12| 127.256|  1.515| 1,130| 11983.287| 206.034|  94,298|
| |Lenoir County|    12| 214.481|  0.000|   558|  9973.369| 91.920|  55,949|
| |Craven County|    12| 117.487|  2.797|   695|  6804.453| 103.500| 102,139|
| |Edgecombe County|    12| 233.136|  2.775|   626| 12161.952| 172.077|  51,472|
| |Hertford County|    11| 464.586|  0.000|   316| 13346.285| 259.444|  23,677|
| |Lee County|    11| 178.054|  4.625| 1,261| 20411.467| 277.487|  61,779|
| |Pitt County|    11| 60.860|  0.000| 1,899| 10506.689| 158.079| 180,742|
| |Wilkes County|    11| 160.791|  4.176|   780| 11401.509| 119.027|  68,412|
| |Onslow County|    10| 50.521|  0.000| 1,026|  5183.441| 98.155| 197,938|
| |Richmond County|     9| 200.763|  3.187|   505| 11265.029| 95.601|  44,829|
| |Surry County|     9| 125.378|  3.980|   916| 12760.681| 141.299|  71,783|
| |Lincoln County|     9| 104.516|  9.954|   825|  9580.658| 172.535|  86,111|
| |Hoke County|     9| 162.943|  2.586|   710| 12854.401| 131.906|  55,234|
| |Rockingham County|     8| 87.902|  1.570|   541|  5944.402| 142.841|  91,010|
| |Bladen County|     7| 213.923|  0.000|   608| 18580.771| 196.460|  32,722|
| |Warren County|     7| 354.772|  7.240|   256| 12974.507| 130.324|  19,731|
| |Yadkin County|     6| 159.291|  0.000|   529| 14044.124| 185.839|  37,667|
| |Martin County|     6| 267.380|  0.000|   258| 11497.326| 140.056|  22,440|
| |Halifax County|     6| 119.976|  0.000|   678| 13557.289| 194.247|  50,010|
| |Carteret County|     6| 86.364|  2.056|   332|  4778.835| 98.702|  69,473|
| |Davie County|     6| 140.036|  6.668|   407|  9499.136| 193.384|  42,846|
| |Bertie County|     5| 263.894|  7.540|   263| 13880.825| 233.735|  18,947|
| |Polk County|     5| 241.266|  0.000|   149|  7189.732| 117.186|  20,724|
| |Jackson County|     5| 113.797|  6.503|   438|  9968.592| 159.315|  43,938|
| |Washington County|     4| 345.423| 12.337|   132| 11398.964| 222.058|  11,580|
| |Cherokee County|     4| 139.801|  4.993|   266|  9296.799| 174.752|  28,612|
| |Jones County|     4| 424.674| 15.167|    79|  8387.302| 318.505|   9,419|
| |Pender County|     3| 47.574|  0.000|   643| 10196.638| 74.759|  63,060|
| |Stokes County|     3| 65.802|  0.000|   291|  6382.839| 134.738|  45,591|
| |Macon County|     3| 83.663|  3.984|   460| 12828.379| 59.760|  35,858|
| |Greene County|     3| 142.389|  0.000|   324| 15378.044| 183.072|  21,069|
| |Anson County|     3| 122.719|  5.844|   317| 12967.357| 93.501|  24,446|
| |Person County|     2| 50.646|  0.000|   207|  5241.833| 65.116|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    80|  5942.212| 169.777|  13,463|
| |Mitchell County|     2| 133.654|  0.000|   116|  7751.938| 76.374|  14,964|
| |Beaufort County|     2| 42.559|  0.000|   406|  8639.401| 215.833|  46,994|
| |Dare County|     2| 54.041|  3.860|   206|  5566.214| 65.621|  37,009|
| |Caswell County|     2| 88.480|  0.000|   191|  8449.832| 50.560|  22,604|
| |Camden County|     2| 184.043|  0.000|    68|  6257.477| 157.752|  10,867|
| |Swain County|     2| 140.144|  0.000|   117|  8198.444| 140.144|  14,271|
| |Scotland County|     2| 57.433|  0.000|   331|  9505.212| 278.962|  34,823|
| |Alexander County|     2| 53.338|  0.000|   295|  7867.296|  0.000|  37,497|
| |Gates County|     2| 172.980|  0.000|    46|  3978.550| 61.779|  11,562|
| |Pamlico County|     1| 78.579|  0.000|    67|  5264.812| 145.933|  12,726|
| |Ashe County|     1| 36.761|  0.000|   152|  5587.619| 199.558|  27,203|
| |Tyrrell County|     1| 249.004|  0.000|    95| 23655.378| 142.288|   4,016|
| |Chowan County|     1| 71.721|  0.000|   150| 10758.086| 307.374|  13,943|
| |Transylvania County|     1| 29.082|  0.000|   132|  3838.883| 45.701|  34,385|
| |Alleghany County|     0|  0.000|  0.000|   166| 14905.271| 1269.898|  11,137|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984| 139.919|  11,231|
| |Madison County|     0|  0.000|  0.000|    42|  1930.591| 26.267|  21,755|
| |Currituck County|     0|  0.000|  0.000|    72|  2593.380| 10.291|  27,763|
| |Avery County|     0|  0.000|  0.000|    99|  5638.777| 138.325|  17,557|
| |Hyde County|     0|  0.000|  0.000|    38|  7696.982| 28.936|   4,937|
| |Graham County|     0|  0.000|  0.000|    35|  4146.428| 203.090|   8,441|
| |Yancey County|     0|  0.000|  0.000|   101|  5589.684| 55.343|  18,069|
| |Watauga County|     0|  0.000|  0.000|   283|  5037.649| 81.375|  56,177|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 1,962| 381.066| N/A|98,219| 19076.414| N/A|5,148,714|
| |Greenville County|   204| 389.654|  5.457|10,745| 20523.664| 194.008| 523,542|
| |Charleston County|   189| 459.400|  9.376|12,118| 29455.088| 268.418| 411,406|
| |Richland County|   148| 355.975|  5.841| 8,579| 20634.550| 274.541| 415,759|
| |Horry County|   146| 412.335|  8.069| 8,486| 23966.268| 206.168| 354,081|
| |Florence County|   108| 780.951| 15.495| 3,329| 24072.079| 491.710| 138,293|
| |Lexington County|   108| 361.506|  5.260| 4,877| 16324.686| 165.451| 298,750|
| |Spartanburg County|    99| 309.583|  7.594| 4,005| 12524.040| 155.908| 319,785|
| |Berkeley County|    66| 289.592|  5.641| 4,079| 17897.651| 199.956| 227,907|
| |Orangeburg County|    61| 707.862|  6.631| 2,353| 27304.903| 386.257|  86,175|
| |Anderson County|    59| 291.275| 11.284| 2,271| 11211.604| 234.148| 202,558|
| |Beaufort County|    55| 286.276|  5.949| 3,999| 20814.899| 368.813| 192,122|
| |Clarendon County|    51| 1511.335|  4.233|   826| 24477.700| 325.974|  33,745|
| |Sumter County|    47| 440.401|  5.354| 2,463| 23078.869| 315.911| 106,721|
| |Dorchester County|    47| 288.682|  7.020| 3,021| 18555.485| 279.907| 162,809|
| |Laurens County|    43| 637.103| 19.050| 1,292| 19142.726| 218.012|  67,493|
| |Darlington County|    35| 525.384|  4.289| 1,234| 18523.522| 452.473|  66,618|
| |Colleton County|    34| 902.407| 11.375|   798| 21180.030| 223.706|  37,677|
| |Aiken County|    34| 198.979|  8.360| 1,810| 10592.724| 266.699| 170,872|
| |Williamsburg County|    30| 987.882| 28.225|   983| 32369.600| 578.617|  30,368|
| |York County|    29| 103.211|  1.017| 3,474| 12363.913| 201.845| 280,979|
| |Cherokee County|    28| 488.656|  7.479|   624| 10890.052| 239.342|  57,300|
| |Lee County|    27| 1604.469|  8.489|   556| 33040.171| 585.758|  16,828|
| |Pickens County|    27| 212.793|  5.629| 1,818| 14328.048| 151.995| 126,884|
| |Dillon County|    24| 787.427|  4.687|   619| 20309.065| 365.591|  30,479|
| |Lancaster County|    23| 234.665|  2.915| 1,161| 11845.488| 208.429|  98,012|
| |Kershaw County|    23| 345.600|  2.147| 1,365| 20510.586| 225.391|  66,551|
| |Fairfield County|    23| 1029.221|  0.000|   557| 24925.046| 204.566|  22,347|
| |Chesterfield County|    21| 460.022|  6.259|   743| 16276.013| 228.446|  45,650|
| |Bamberg County|    20| 1421.868| 40.625|   463| 32916.252| 406.248|  14,066|
| |Georgetown County|    19| 303.127|  2.279| 1,419| 22638.800| 414.805|  62,680|
| |Greenwood County|    18| 254.198|  6.052| 1,355| 19135.445| 318.756|  70,811|
| |Jasper County|    15| 498.786| 19.001|   571| 18987.131| 418.030|  30,073|
| |Chester County|    13| 403.176|  8.861|   633| 19631.559| 447.481|  32,244|
| |Marion County|    13| 424.047|  4.660|   542| 17679.486| 144.455|  30,657|
| |Calhoun County|    10| 687.144| 29.449|   367| 25218.168| 706.776|  14,553|
| |Newberry County|     9| 234.131|  3.716|   830| 21592.092| 315.891|  38,440|
| |Oconee County|     9| 113.142|  5.388|   802| 10082.217| 154.448|  79,546|
| |Saluda County|     8| 390.759|  6.978|   449| 21931.324| 355.869|  20,473|
| |Abbeville County|     8| 326.171|  5.824|   321| 13087.618| 227.155|  24,527|
| |Hampton County|     7| 364.166|  0.000|   412| 21433.774| 683.740|  19,222|
| |Edgefield County|     6| 220.103|  0.000|   314| 11518.709| 214.862|  27,260|
| |Barnwell County|     5| 239.624|  6.846|   402| 19265.791| 561.405|  20,866|
| |Marlboro County|     4| 153.151|  0.000|   473| 18110.116| 273.484|  26,118|
| |Union County|     4| 146.434| 10.460|   355| 12996.046| 162.124|  27,316|
| |Allendale County|     3| 345.304|  0.000|   213| 24516.575| 657.722|   8,688|
| |McCormick County|     2| 211.349|  0.000|   113| 11941.245| 211.349|   9,463|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,857| 322.467| N/A|49,875|  8660.755| N/A|5,758,736|
| |Denver County|   414| 569.298| N/A|10,122| 13918.931| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.435| 7,234| 11017.530| 77.674| 656,590|
| |Jefferson County|   228| 391.160|  0.245| 4,124|  7075.201| 61.272| 582,881|
| |Adams County|   176| 340.149|  1.380| 6,375| 12320.721| 115.408| 517,421|
| |Weld County|   142| 437.607|  0.440| 3,662| 11285.332| 70.000| 324,492|
| |El Paso County|   137| 190.171|  0.397| 4,911|  6817.018| 86.856| 720,403|
| |Boulder County|    75| 229.923|  0.000| 2,019|  6189.530| 64.378| 326,196|
| |Douglas County|    59| 168.017|  0.407| 1,718|  4892.440| 41.496| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   683| 23496.629| 44.231|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,493|  4183.256| 53.637| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   674|  4001.805| 65.311| 168,424|
| |Broomfield County|    32| 454.126| N/A|   453|  6428.723| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   296| 14541.167| 70.179|  20,356|
| |Montrose County|    13| 304.037|  0.000|   293|  6852.519| 63.480|  42,758|
| |Alamosa County|     9| 554.426|  0.000|   226| 13922.257| 17.601|  16,233|
| |Eagle County|     9| 163.259|  0.000| 1,116| 20244.163| 233.228|  55,127|
| |Routt County|     7| 273.032|  5.572|   117|  4563.538| 100.298|  25,638|
| |Gunnison County|     6| 343.603|  0.000|   268| 15347.612| 179.983|  17,462|
| |Otero County|     6| 328.263|  7.816|    71|  3884.451| 148.500|  18,278|
| |Logan County|     5| 223.125|  0.000|   650| 29006.203| 19.125|  22,409|
| |Garfield County|     4| 66.599|  0.000|   757| 12603.853| 156.983|  60,061|
| |Mesa County|     4| 25.939|  0.926|   293|  1900.006| 35.202| 154,210|
| |Montezuma County|     4| 152.771|  0.000|   111|  4239.392| 21.824|  26,183|
| |Summit County|     4| 128.986|  0.000|   327| 10544.645| 23.033|  31,011|
| |Kit Carson County|     3| 422.714|  0.000|    44|  6199.803| 40.258|   7,097|
| |Teller County|     3| 118.166|  0.000|   123|  4844.809| 73.150|  25,388|
| |La Plata County|     2| 35.574|  0.000|   204|  3628.537| 17.787|  56,221|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Rio Grande County|     2| 177.510|  0.000|    89|  7899.175| 25.359|  11,267|
| |Pitkin County|     2| 112.568|  0.000|   182| 10243.710| 128.649|  17,767|
| |Elbert County|     2| 74.825|  0.000|   103|  3853.492| 96.204|  26,729|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 58.910|   9,700|
| |Crowley County|     1| 164.989|  0.000|    72| 11879.228|  0.000|   6,061|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 41.426|   6,897|
| |Moffat County|     1| 75.284|  0.000|    26|  1957.389| 21.510|  13,283|
| |Delta County|     1| 32.090|  0.000|   118|  3786.663| 64.181|  31,162|
| |Grand County|     1| 63.557|  0.000|    46|  2923.605| 36.318|  15,734|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Prowers County|     0|  0.000|  0.000|    51|  4189.944| 46.946|  12,172|
| |Gilpin County|     0|  0.000|  0.000|    16|  2562.870| 68.648|   6,243|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Lake County|     0|  0.000|  0.000|    77|  9474.591| 123.047|   8,127|
| |Las Animas County|     0|  0.000|  0.000|    15|  1034.055|  0.000|  14,506|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 50.117|   5,701|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053| 14.259|  10,019|
| |Washington County|     0|  0.000|  0.000|    47|  9576.202|  0.000|   4,908|
| |San Miguel County|     0|  0.000|  0.000|    82| 10025.676| 157.197|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Fremont County|     0|  0.000|  0.000|   117|  2445.703| 44.793|  47,839|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Archuleta County|     0|  0.000|  0.000|    35|  2494.832| 30.549|  14,029|
| |Baca County|     0|  0.000|  0.000|    14|  3909.522|  0.000|   3,581|
| |Rio Blanco County|     0|  0.000|  0.000|    15|  2371.917| 203.307|   6,324|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 102.462|   5,577|
| |Cheyenne County|     0|  0.000|  0.000|     8|  4369.197|  0.000|   1,831|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|
| |Costilla County|     0|  0.000|  0.000|    22|  5659.892|  0.000|   3,887|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481| 28.188|   5,068|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,848| 620.937| N/A|65,436| 21986.802| N/A|2,976,149|
| |Hinds County|   117| 504.658|  9.243| 5,544| 23913.043| 279.133| 231,840|
| |Neshoba County|    92| 3159.558| 24.531| 1,284| 44096.435| 480.802|  29,118|
| |Lauderdale County|    90| 1214.165|  3.854| 1,397| 18846.543| 156.107|  74,125|
| |Madison County|    64| 602.228| 18.820| 2,396| 22545.920| 196.262| 106,272|
| |Leflore County|    62| 2199.908| 15.207|   907| 32182.521| 471.409|  28,183|
| |Jones County|    58| 851.714|  2.098| 1,850| 27166.730| 304.183|  68,098|
| |Forrest County|    55| 734.342|  9.537| 1,758| 23472.235| 370.032|  74,897|
| |Monroe County|    52| 1475.094|  8.105|   769| 21814.365| 380.931|  35,252|
| |Holmes County|    48| 2821.869| 16.797|   873| 51322.751| 403.124|  17,010|
| |Jackson County|    42| 292.444|  7.958| 2,225| 15492.595| 385.947| 143,617|
| |Lincoln County|    41| 1200.480| 12.549|   796| 23306.884| 276.069|  34,153|
| |Washington County|    40| 910.975| 26.028| 1,606| 36575.645| 608.401|  43,909|
| |Oktibbeha County|    38| 766.330| 11.524| 1,096| 22102.567| 164.214|  49,587|
| |Lowndes County|    37| 631.453| 17.066| 1,058| 18056.148| 285.251|  58,595|
| |Pearl River County|    37| 666.247|  2.572|   529|  9525.524| 149.198|  55,535|
| |Harrison County|    35| 168.205|  2.746| 2,406| 11562.860| 245.785| 208,080|
| |Pike County|    35| 890.857| 18.181|   896| 22805.946| 319.981|  39,288|
| |Bolivar County|    33| 1077.445|  4.664| 1,093| 35686.300| 820.911|  30,628|
| |Lee County|    33| 386.254|  6.688| 1,383| 16187.556| 369.533|  85,436|
| |Warren County|    32| 705.141| 22.036| 1,033| 22762.830| 273.872|  45,381|
| |Rankin County|    32| 206.091|  3.680| 2,251| 14497.234| 147.208| 155,271|
| |DeSoto County|    30| 162.210|  3.090| 3,574| 19324.664| 356.090| 184,945|
| |Simpson County|    30| 1125.366| 32.153|   786| 29484.582| 482.300|  26,658|
| |Copiah County|    28| 997.684| 25.451|   945| 33671.833| 244.331|  28,065|
| |Tate County|    27| 953.356| 30.265|   705| 24893.189| 423.714|  28,321|
| |Clarke County|    25| 1608.648|  0.000|   325| 20912.425| 257.384|  15,541|
| |Leake County|    25| 1097.165|  0.000|   786| 34494.865| 194.355|  22,786|
| |Adams County|    25| 814.518|  9.309|   610| 19874.238| 209.447|  30,693|
| |Attala County|    25| 1375.592| 15.721|   515| 28337.185| 227.955|  18,174|
| |Sunflower County|    24| 955.795| 17.068|   992| 39506.173| 563.236|  25,110|
| |Wayne County|    21| 1040.480|  0.000|   753| 37308.626| 169.874|  20,183|
| |Grenada County|    21| 1011.658|  6.882|   838| 40369.978| 289.045|  20,758|
| |Marion County|    20| 813.901| 17.441|   643| 26166.931| 360.442|  24,573|
| |Scott County|    20| 711.136| 15.239|   995| 35379.036| 243.818|  28,124|
| |Chickasaw County|    19| 1110.916|  0.000|   450| 26311.173| 250.583|  17,103|
| |Walthall County|    19| 1329.973| 10.000|   491| 34369.313| 659.987|  14,286|
| |Winston County|    16| 891.117| 15.913|   611| 34029.518| 405.776|  17,955|
| |Union County|    16| 555.266| 14.873|   601| 20857.192| 485.858|  28,815|
| |Lafayette County|    15| 277.680| 21.157|   956| 17697.477| 314.704|  54,019|
| |Lamar County|    14| 221.019|  4.511| 1,192| 18818.180| 252.593|  63,343|
| |Clay County|    14| 724.788|  0.000|   392| 20294.057| 214.478|  19,316|
| |Kemper County|    14| 1437.077|  0.000|   227| 23301.170| 58.656|   9,742|
| |Hancock County|    14| 293.920|  0.000|   373|  7830.870| 149.959|  47,632|
| |Tippah County|    13| 590.506|  6.489|   342| 15534.863| 369.878|  22,015|
| |Smith County|    13| 816.788|  8.976|   397| 24943.453| 269.271|  15,916|
| |Covington County|    13| 697.575| 15.331|   610| 32732.346| 268.298|  18,636|
| |Claiborne County|    13| 1446.373| 15.894|   398| 44281.264|  0.000|   8,988|
| |Wilkinson County|    13| 1506.373| 16.554|   201| 23290.846| 380.732|   8,630|
| |Webster County|    12| 1238.518|  0.000|   225| 23222.211| 648.747|   9,689|
| |Yazoo County|    12| 404.176|  4.812|   815| 27450.320| 279.074|  29,690|
| |Panola County|    12| 350.959|  4.178| 1,026| 30007.019| 622.535|  34,192|
| |Noxubee County|    11| 1055.966| 13.714|   448| 43006.624| 507.412|  10,417|
| |Carroll County|    11| 1105.861|  0.000|   260| 26138.534| 287.237|   9,947|
| |Newton County|    11| 523.361|  0.000|   537| 25549.529| 156.329|  21,018|
| |Greene County|    11| 809.657|  0.000|   236| 17370.823| 136.695|  13,586|
| |Coahoma County|    11| 497.198|  6.457|   715| 32317.845| 535.940|  22,124|
| |Humphreys County|    11| 1364.087|  0.000|   283| 35094.246| 372.024|   8,064|
| |Prentiss County|    10| 397.994| 22.743|   403| 16039.163| 483.279|  25,126|
| |Yalobusha County|    10| 825.900|  0.000|   312| 25768.087| 47.194|  12,108|
| |Tallahatchie County|    10| 724.165|  0.000|   522| 37801.434| 1272.462|  13,809|
| |Itawamba County|    10| 427.533|  0.000|   348| 14878.153| 311.488|  23,390|
| |Jasper County|     9| 549.350|  8.720|   381| 23255.814| 113.358|  16,383|
| |Marshall County|     9| 255.001|  4.048|   674| 19096.730| 558.573|  35,294|
| |Calhoun County|     9| 626.697|  9.948|   407| 28340.645| 407.851|  14,361|
| |Pontotoc County|     8| 248.648|  4.440|   809| 25144.527| 488.416|  32,174|
| |Perry County|     7| 584.649|  0.000|   223| 18625.240| 167.043|  11,973|
| |Lawrence County|     7| 556.174| 22.701|   312| 24789.449| 136.206|  12,586|
| |Amite County|     6| 487.924| 23.234|   225| 18297.146| 371.752|  12,297|
| |Tunica County|     6| 622.924| 14.832|   322| 33430.233| 1394.162|   9,632|
| |Jefferson County|     6| 858.369|  0.000|   194| 27753.934| 122.624|   6,990|
| |Jefferson Davis County|     6| 539.180| 12.838|   228| 20488.857| 474.992|  11,128|
| |Alcorn County|     5| 135.307|  7.732|   397| 10743.377| 239.687|  36,953|
| |Tishomingo County|     5| 257.958| 14.740|   363| 18727.751| 471.695|  19,383|
| |Choctaw County|     4| 487.211|  0.000|   131| 15956.151| 121.803|   8,210|
| |George County|     4| 163.265|  0.000|   549| 22408.163| 139.942|  24,500|
| |Stone County|     4| 218.150|  7.791|   186| 10143.979| 327.225|  18,336|
| |Sharkey County|     4| 925.712| 99.183|   194| 44897.015| 1818.362|   4,321|
| |Montgomery County|     3| 306.905|  0.000|   315| 32225.064| 569.967|   9,775|
| |Franklin County|     2| 259.302|  0.000|   119| 15428.497| 148.173|   7,713|
| |Quitman County|     1| 147.232|  0.000|   252| 37102.473| 862.359|   6,792|
| |Issaquena County|     1| 753.580|  0.000|    25| 18839.488| 538.271|   1,327|
| |Benton County|     0|  0.000|  0.000|   142| 17193.365| 415.132|   8,259|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,674| 341.411| N/A|94,827| 19339.878| N/A|4,903,185|
| |Jefferson County|   242| 367.461|  4.121|12,743| 19349.412| 336.008| 658,573|
| |Mobile County|   206| 498.536|  6.569| 9,565| 23148.036| 512.019| 413,210|
| |Montgomery County|   148| 653.462|  4.415| 6,521| 28792.067| 298.978| 226,486|
| |Tallapoosa County|    79| 1957.044|  3.539|   849| 21032.031| 180.487|  40,367|
| |Tuscaloosa County|    71| 339.137|  6.824| 4,103| 19598.290| 203.346| 209,355|
| |Walker County|    64| 1007.541|  6.747| 1,502| 23645.723| 137.187|  63,521|
| |Lee County|    44| 267.409|  3.473| 2,628| 15971.606| 171.906| 164,542|
| |Elmore County|    38| 467.928|  5.277| 1,694| 20859.757| 263.869|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   835| 25109.761| 124.582|  33,254|
| |Butler County|    35| 1799.671|  0.000|   759| 39027.149| 146.912|  19,448|
| |Marshall County|    34| 351.334|  8.857| 3,090| 31930.064| 394.144|  96,774|
| |Shelby County|    33| 151.583|  1.312| 3,201| 14703.586| 190.299| 217,702|
| |Madison County|    30| 80.449|  1.915| 5,250| 14078.502| 203.037| 372,909|
| |Etowah County|    30| 293.347| 15.366| 2,075| 20289.827| 304.522| 102,268|
| |Hale County|    26| 1774.623|  9.751|   467| 31874.957| 204.764|  14,651|
| |Marion County|    24| 807.836|  0.000|   567| 19085.126| 211.576|  29,709|
| |Lowndes County|    24| 2467.613|  0.000|   567| 58297.347| 308.452|   9,726|
| |Dale County|    23| 467.746| 14.526|   823| 16737.167| 214.989|  49,172|
| |Baldwin County|    23| 103.031|  1.280| 3,443| 15423.278| 247.658| 223,234|
| |Dallas County|    23| 618.346|  0.000| 1,311| 35245.725| 199.714|  37,196|
| |Autauga County|    21| 375.879|  2.557| 1,065| 19062.450| 237.801|  55,869|
| |Franklin County|    20| 637.714|  0.000| 1,258| 40112.238| 437.290|  31,362|
| |Covington County|    20| 539.826|  0.000|   726| 19595.671| 177.371|  37,049|
| |Sumter County|    18| 1448.459| 11.496|   362| 29130.120| 22.991|  12,427|
| |Morgan County|    17| 142.047|  3.581| 2,330| 19468.746| 239.928| 119,679|
| |Lauderdale County|    17| 183.330| 10.784| 1,139| 12283.105| 192.573|  92,729|
| |St. Clair County|    16| 178.747| 11.172| 1,310| 14634.909| 253.757|  89,512|
| |Escambia County|    16| 436.765|  3.900| 1,054| 28771.872| 432.865|  36,633|
| |Marengo County|    14| 742.194|  0.000|   546| 28945.555| 318.083|  18,863|
| |Colbert County|    13| 235.332|  5.172| 1,156| 20926.486| 297.398|  55,241|
| |Talladega County|    13| 162.545|  1.786|   986| 12328.390| 248.283|  79,978|
| |DeKalb County|    13| 181.785|  3.995| 1,771| 24764.728| 285.662|  71,513|
| |Macon County|    13| 719.504|  7.907|   332| 18375.028| 253.012|  18,068|
| |Calhoun County|    13| 114.432|  5.030| 1,704| 14999.340| 370.960| 113,605|
| |Limestone County|    13| 131.426|  2.888| 1,284| 12980.842| 199.305|  98,915|
| |Cullman County|    12| 143.253|  1.705| 1,201| 14337.217| 214.879|  83,768|
| |Washington County|    12| 735.024| 17.501|   327| 20029.401| 227.507|  16,326|
| |Houston County|    12| 113.334|  0.000| 1,364| 12882.265| 164.604| 105,882|
| |Choctaw County|    12| 953.213|  0.000|   279| 22162.205| 90.782|  12,589|
| |Greene County|    11| 1356.183|  0.000|   250| 30822.340| 193.740|   8,111|
| |Winston County|    11| 465.530|  6.046|   444| 18790.469| 157.192|  23,629|
| |Bullock County|    11| 1089.001|  0.000|   454| 44946.045| 339.429|  10,101|
| |Wilcox County|    10| 964.041| 13.772|   418| 40296.925| 289.212|  10,373|
| |Randolph County|    10| 440.102|  0.000|   394| 17340.023| 62.872|  22,722|
| |Conecuh County|    10| 828.706|  0.000|   382| 31656.584| 284.128|  12,067|
| |Clarke County|     9| 381.001|  0.000|   496| 20997.375| 139.096|  23,622|
| |Pickens County|     9| 451.581|  0.000|   384| 19267.436| 207.870|  19,930|
| |Pike County|     7| 211.391|  0.000|   690| 20837.108| 215.705|  33,114|
| |Cherokee County|     7| 267.216|  0.000|   263| 10039.701| 239.949|  26,196|
| |Chilton County|     6| 135.050|  3.215|   767| 17263.888| 344.056|  44,428|
| |Clay County|     5| 377.786|  0.000|   249| 18813.751| 593.664|  13,235|
| |Barbour County|     5| 202.544|  0.000|   569| 23049.502| 109.952|  24,686|
| |Coffee County|     5| 95.526|  0.000|   747| 14271.522| 158.300|  52,342|
| |Fayette County|     5| 306.711|  0.000|   198| 12145.749| 306.711|  16,302|
| |Jackson County|     4| 77.480|  2.767|   945| 18304.730| 542.362|  51,626|
| |Perry County|     4| 448.280| 16.010|   436| 48862.490| 304.190|   8,923|
| |Monroe County|     4| 192.929|  6.890|   415| 20016.399| 213.600|  20,733|
| |Bibb County|     4| 178.619| 12.759|   416| 18576.404| 389.135|  22,394|
| |Henry County|     3| 174.368|  0.000|   252| 14646.905| 157.761|  17,205|
| |Crenshaw County|     3| 217.833|  0.000|   313| 22727.273| 383.802|  13,772|
| |Blount County|     3| 51.880|  0.000|   774| 13384.983| 219.871|  57,826|
| |Russell County|     2| 34.506|  2.465| 1,342| 23153.500| 446.113|  57,961|
| |Lamar County|     2| 144.875|  0.000|   217| 15718.942| 269.054|  13,805|
| |Coosa County|     2| 187.564|  0.000|   101|  9472.006| 160.770|  10,663|
| |Cleburne County|     1| 67.069|  0.000|   125|  8383.635| 134.138|  14,910|
| |Lawrence County|     1| 30.373|  4.339|   344| 10448.305| 212.611|  32,924|
| |Geneva County|     0|  0.000|  0.000|   255|  9706.520| 244.702|  26,271|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,669| 219.176| N/A|61,419|  8065.642| N/A|7,614,893|
| |King County|   670| 297.410|  1.332|16,222|  7200.874| 75.906|2,252,782|
| |Yakima County|   212| 845.049|  4.556|10,210| 40697.883| 196.457| 250,873|
| |Snohomish County|   191| 232.337|  0.869| 5,369|  6530.971| 72.985| 822,083|
| |Pierce County|   137| 151.385|  1.894| 5,522|  6101.792| 108.290| 904,980|
| |Benton County|   114| 557.757|  4.893| 3,690| 18053.721| 178.930| 204,390|
| |Spokane County|    88| 168.325|  8.471| 4,277|  8180.980| 181.441| 522,798|
| |Franklin County|    48| 504.085|  3.001| 3,447| 36199.618| 355.560|  95,222|
| |Clark County|    43| 88.071|  1.170| 1,749|  3582.247| 98.897| 488,241|
| |Whatcom County|    39| 170.122|  1.246|   970|  4231.244| 47.360| 229,247|
| |Skagit County|    21| 162.532|  1.106|   858|  6640.610| 82.925| 129,205|
| |Kittitas County|    18| 375.509|  2.980|   360|  7510.170| 101.328|  47,935|
| |Grant County|    12| 122.784|  0.000| 1,422| 14549.845| 344.963|  97,733|
| |Island County|    11| 129.197|  0.000|   247|  2901.070| 21.813|  85,141|
| |Thurston County|    11| 37.861|  1.967|   694|  2388.688| 44.745| 290,536|
| |Chelan County|    10| 129.534|  1.850| 1,276| 16528.497| 475.574|  77,200|
| |Kitsap County|     7| 25.785|  2.105|   721|  2655.881| 64.726| 271,473|
| |Douglas County|     7| 161.183|  0.000|   908| 20907.688| 598.678|  43,429|
| |Cowlitz County|     5| 45.211|  0.000|   472|  4267.901| 59.420| 110,593|
| |Adams County|     4| 200.170|  7.149|   423| 21167.993| 350.298|  19,983|
| |Lewis County|     3| 37.171|  0.000|   207|  2564.833| 72.573|  80,707|
| |Klickitat County|     3| 133.779|  0.000|   109|  4860.647| 57.334|  22,425|
| |Okanogan County|     3| 71.018|  3.382|   836| 19790.261| 497.124|  42,243|
| |Walla Walla County|     2| 32.916|  0.000|   495|  8146.807| 235.117|  60,760|
| |Pacific County|     2| 89.004|  0.000|    48|  2136.087| 95.361|  22,471|
| |Grays Harbor County|     2| 26.645|  0.000|   109|  1452.152| 32.355|  75,061|
| |Asotin County|     2| 88.566|  0.000|    25|  1107.076|  6.326|  22,582|
| |Stevens County|     1| 21.871|  0.000|   105|  2296.437| 71.861|  45,723|
| |Columbia County|     1| 250.941| 35.849|    13|  3262.233|  0.000|   3,985|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 118.230|  12,083|
| |Mason County|     1| 14.977|  0.000|   201|  3010.424| 119.818|  66,768|
| |Clallam County|     0|  0.000|  0.000|   102|  1319.005| 20.321|  77,331|
| |Jefferson County|     0|  0.000|  0.000|    54|  1675.926| 13.301|  32,221|
| |Garfield County|     0|  0.000|  0.000|     2|   898.876|  0.000|   2,225|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489| 187.305|   7,627|
| |Lincoln County|     0|  0.000|  0.000|    22|  2011.153| 156.713|  10,939|
| |Pend Oreille County|     0|  0.000|  0.000|    39|  2841.737| 31.228|  13,724|
| |Whitman County|     0|  0.000|  0.000|   103|  2055.724| 54.173|  50,104|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |San Juan County|     0|  0.000|  0.000|    28|  1592.538|  0.000|  17,582|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,640| 290.799| N/A|59,059| 10472.137| N/A|5,639,632|
| |Hennepin County|   828| 654.110|  1.693|18,774| 14831.223| 164.543|1,265,843|
| |Ramsey County|   263| 477.903|  1.038| 7,307| 13277.705| 161.205| 550,321|
| |Anoka County|   114| 319.398|  0.800| 3,553|  9954.584| 123.277| 356,921|
| |Dakota County|   104| 242.412|  0.666| 4,250|  9906.275| 150.842| 429,021|
| |Washington County|    44| 167.657|  0.544| 2,037|  7761.774| 119.755| 262,440|
| |Clay County|    40| 622.840|  2.224|   771| 12005.232| 68.957|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,700| 10739.578| 101.078| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,874| 17842.620| 73.613| 161,075|
| |St. Louis County|    19| 95.444|  0.718|   502|  2521.726| 85.397| 199,070|
| |Scott County|    18| 120.795|  5.752| 1,503| 10086.368| 198.449| 149,013|
| |Winona County|    16| 316.932|  0.000|   257|  5090.722| 48.106|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   228|  3504.727| 79.054|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   329|  9599.113| 129.211|  34,274|
| |Itasca County|    12| 265.899|  0.000|   136|  3013.517| 34.820|  45,130|
| |Pipestone County|     9| 986.193|  0.000|   149| 16326.978| 109.577|   9,126|
| |Rice County|     8| 119.453|  0.000| 1,019| 15215.314| 93.856|  66,972|
| |Goodhue County|     8| 172.637|  0.000|   192|  4143.289| 70.904|  46,340|
| |Sherburne County|     7| 71.988|  1.469|   710|  7301.672| 139.569|  97,238|
| |Nobles County|     6| 277.405|  0.000| 1,754| 81094.826| 105.678|  21,629|
| |Blue Earth County|     5| 73.907|  2.112|   893| 13199.710| 145.701|  67,653|
| |Renville County|     5| 343.690|  0.000|    62|  4261.754| 58.918|  14,548|
| |Wright County|     5| 36.133|  0.000|   855|  6178.772| 87.752| 138,377|
| |Martin County|     5| 254.026|  0.000|   206| 10465.884| 29.032|  19,683|
| |Polk County|     4| 127.535|  4.555|   149|  4750.670| 109.316|  31,364|
| |Wilkin County|     3| 483.325|  0.000|    33|  5316.578| 161.108|   6,207|
| |Mille Lacs County|     3| 114.168|  0.000|    69|  2625.871| 81.549|  26,277|
| |Lyon County|     3| 117.767|  0.000|   424| 16644.422| 56.080|  25,474|
| |Koochiching County|     3| 245.319|  0.000|    74|  6051.190| 70.091|  12,229|
| |Grant County|     3| 502.344| 47.842|    53|  8874.749| 215.290|   5,972|
| |Otter Tail County|     3| 51.067|  0.000|   189|  3217.240| 60.794|  58,746|
| |Benton County|     3| 73.369|  0.000|   316|  7728.240| 59.394|  40,889|
| |Carver County|     3| 28.547|  1.359|   829|  7888.552| 115.548| 105,089|
| |Meeker County|     2| 86.125|  0.000|    84|  3617.259|  6.152|  23,222|
| |Mower County|     2| 49.923|  0.000| 1,095| 27332.634| 110.543|  40,062|
| |Sibley County|     2| 134.544|  0.000|    83|  5583.586| 67.272|  14,865|
| |Todd County|     2| 81.090|  0.000|   422| 17109.958| 52.129|  24,664|
| |Brown County|     2| 79.974|  0.000|    87|  3478.887| 45.700|  25,008|
| |Cass County|     2| 67.161|  0.000|    70|  2350.650| 76.756|  29,779|
| |Swift County|     1| 107.921|  0.000|    52|  5611.915| 15.417|   9,266|
| |Freeborn County|     1| 33.024|  0.000|   358| 11822.595| 23.589|  30,281|
| |Steele County|     1| 27.286|  0.000|   338|  9222.625| 66.266|  36,649|
| |Murray County|     1| 122.041|  0.000|   122| 14888.943| 34.869|   8,194|
| |Morrison County|     1| 29.953|  0.000|    85|  2545.977| 17.116|  33,386|
| |Kandiyohi County|     1| 23.149|  0.000|   687| 15903.146| 82.674|  43,199|
| |Kanabec County|     1| 61.211|  0.000|    34|  2081.165| 96.188|  16,337|
| |Pennington County|     1| 70.827|  0.000|    73|  5170.338| 30.354|  14,119|
| |Chisago County|     1| 17.674|  0.000|   190|  3358.136| 58.073|  56,579|
| |Chippewa County|     1| 84.746|  0.000|   101|  8559.322| 96.852|  11,800|
| |Becker County|     1| 29.050|  0.000|   149|  4328.501| 62.251|  34,423|
| |Aitkin County|     1| 62.949|  8.993|    34|  2140.249| 62.949|  15,886|
| |Le Sueur County|     1| 34.618|  0.000|   213|  7373.559| 84.071|  28,887|
| |Mahnomen County|     1| 180.930|  0.000|    26|  4704.179| 103.389|   5,527|
| |Lake County|     0|  0.000|  0.000|    20|  1879.523| 67.126|  10,641|
| |Lake of the Woods County|     0|  0.000|  0.000|     2|   534.759| 38.197|   3,740|
| |Watonwan County|     0|  0.000|  0.000|   307| 28172.892| 104.878|  10,897|
| |Yellow Medicine County|     0|  0.000|  0.000|    51|  5252.858| 58.856|   9,709|
| |Carlton County|     0|  0.000|  0.000|   133|  3707.730| 47.790|  35,871|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   217|  4598.627| 99.904|  47,188|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    72|  7312.614| 58.037|   9,846|
| |Isanti County|     0|  0.000|  0.000|   121|  2980.589| 66.861|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    32|  1488.995| 33.237|  21,491|
| |Houston County|     0|  0.000|  0.000|    39|  2096.774| 15.361|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    63|  2990.459| 27.124|  21,067|
| |Faribault County|     0|  0.000|  0.000|    85|  6225.738| 52.317|  13,653|
| |Douglas County|     0|  0.000|  0.000|   138|  3618.154| 52.437|  38,141|
| |Dodge County|     0|  0.000|  0.000|   125|  5971.147| 20.473|  20,934|
| |Cottonwood County|     0|  0.000|  0.000|   176| 15719.900| 114.837|  11,196|
| |Cook County|     0|  0.000|  0.000|     3|   549.149| 26.150|   5,463|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Lac qui Parle County|     0|  0.000|  0.000|     6|   905.934|  0.000|   6,623|
| |Wadena County|     0|  0.000|  0.000|    25|  1827.218| 20.882|  13,682|
| |Norman County|     0|  0.000|  0.000|    38|  5960.784| 89.636|   6,375|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255| 30.604|   9,336|
| |McLeod County|     0|  0.000|  0.000|   173|  4819.881| 191.044|  35,893|
| |Lincoln County|     0|  0.000|  0.000|    56|  9930.839| 76.001|   5,639|
| |Wabasha County|     0|  0.000|  0.000|    88|  4068.988| 66.055|  21,627|
| |Waseca County|     0|  0.000|  0.000|   138|  7414.571| 76.755|  18,612|
| |Pope County|     0|  0.000|  0.000|    46|  4089.252| 101.596|  11,249|
| |Red Lake County|     0|  0.000|  0.000|    23|  5672.010| 246.609|   4,055|
| |Pine County|     0|  0.000|  0.000|   128|  4327.394| 19.319|  29,579|
| |Traverse County|     0|  0.000|  0.000|    10|  3068.426|  0.000|   3,259|
| |Stevens County|     0|  0.000|  0.000|    17|  1733.809| 29.140|   9,805|
| |Roseau County|     0|  0.000|  0.000|    47|  3099.242| 47.101|  15,165|
| |Rock County|     0|  0.000|  0.000|    79|  8480.945| 107.354|   9,315|
| |Redwood County|     0|  0.000|  0.000|    33|  2175.346| 28.251|  15,170|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,263| 205.787| N/A|51,361|  8368.489| N/A|6,137,428|
| |St. Louis County|   834| 838.861|  2.155|19,621| 19735.366| 323.302| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,954|  9835.283| 185.491| 402,022|
| |Jackson County|    64| 91.037|  1.422| 3,909|  5560.368| 119.689| 703,011|
| |Jasper County|    30| 247.264|  7.065| 1,738| 14324.805| 131.874| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,544|  6859.753| 158.038| 225,081|
| |Clay County|    20| 80.017|  0.572| 1,011|  4044.841| 73.730| 249,948|
| |Franklin County|    18| 173.132|  0.000|   590|  5674.878| 111.299| 103,967|
| |Scott County|    13| 339.603|  0.000|   381|  9952.978| 145.544|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,440|  4913.234| 125.755| 293,086|
| |Platte County|    10| 95.769|  4.104|   343|  3284.874| 57.461| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,076| 12316.286| 35.974|  87,364|
| |Stoddard County|     9| 310.078|  0.000|   224|  7717.485| 78.750|  29,025|
| |Gentry County|     9| 1369.655|  0.000|    83| 12631.259| 86.962|   6,571|
| |Cass County|     9| 85.082|  0.000|   705|  6664.776| 113.443| 105,780|
| |Pemiscot County|     9| 569.440|  9.039|   234| 14805.441| 316.356|  15,805|
| |Saline County|     7| 307.544|  0.000|   424| 18628.356| 106.699|  22,761|
| |McDonald County|     7| 306.520|  0.000|   950| 41599.159| 156.388|  22,837|
| |Newton County|     6| 103.029|  2.453|   868| 14904.870| 181.527|  58,236|
| |Cape Girardeau County|     5| 63.395|  3.623|   636|  8063.800| 76.074|  78,871|
| |Camden County|     5| 107.980|  3.085|   339|  7321.024| 166.597|  46,305|
| |Perry County|     4| 209.030|  0.000|   223| 11653.428| 164.238|  19,136|
| |Pettis County|     4| 94.476|  3.374|   487| 11502.397| 276.678|  42,339|
| |Barry County|     4| 111.766| 15.967|   248|  6929.503| 119.749|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   300| 10298.308| 299.141|  29,131|
| |Boone County|     3| 16.624|  0.000| 1,328|  7358.849| 139.324| 180,463|
| |Henry County|     3| 137.463|  0.000|    76|  3482.405| 45.821|  21,824|
| |Cole County|     3| 39.090|  1.861|   376|  4899.342| 163.808|  76,745|
| |Taney County|     3| 53.640|  0.000|   548|  9798.312| 401.026|  55,928|
| |Johnson County|     2| 36.995|  0.000|   486|  8989.679| 84.559|  54,062|
| |Howell County|     2| 49.854|  3.561|   152|  3788.917| 89.025|  40,117|
| |Douglas County|     2| 151.688|  0.000|    83|  6295.032| 162.522|  13,185|
| |Butler County|     2| 47.083|  0.000|   275|  6473.939| 131.160|  42,478|
| |St. Francois County|     2| 29.755|  0.000|   350|  5207.171| 138.149|  67,215|
| |Moniteau County|     2| 123.977|  0.000|   139|  8616.415| 247.954|  16,132|
| |Lawrence County|     2| 52.144|  0.000|   211|  5501.238| 108.013|  38,355|
| |Lafayette County|     2| 61.147|  0.000|   175|  5350.373| 109.191|  32,708|
| |Ray County|     2| 86.889| 12.413|   116|  5039.534| 179.983|  23,018|
| |Osage County|     1| 73.448| 10.493|    45|  3305.178| 94.434|  13,615|
| |New Madrid County|     1| 58.562|  0.000|   230| 13469.197| 493.592|  17,076|
| |Pike County|     1| 54.639|  0.000|    95|  5190.690| 210.750|  18,302|
| |Stone County|     1| 31.297|  0.000|   123|  3849.524| 192.253|  31,952|
| |Ste. Genevieve County|     1| 55.885|  0.000|    53|  2961.887| 55.885|  17,894|
| |Scotland County|     1| 203.998|  0.000|    14|  2855.977| 58.285|   4,902|
| |Miller County|     1| 39.034|  5.576|   114|  4449.822| 139.405|  25,619|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313| 152.105|   4,696|
| |Pulaski County|     1| 19.009|  0.000|   197|  3744.749| 51.596|  52,607|
| |Shannon County|     1| 122.459|  0.000|    43|  5265.736|  0.000|   8,166|
| |Lewis County|     1| 102.291|  0.000|    40|  4091.653| 189.970|   9,776|
| |Lincoln County|     1| 16.945|  0.000|   360|  6100.351| 174.296|  59,013|
| |Linn County|     1| 83.893|  0.000|    29|  2432.886|  0.000|  11,920|
| |Benton County|     1| 51.432|  0.000|    90|  4628.915| 139.602|  19,443|
| |Carter County|     1| 167.168|  0.000|    20|  3343.363| 47.762|   5,982|
| |Andrew County|     1| 56.459|  0.000|    88|  4968.383| 56.459|  17,712|
| |Callaway County|     1| 22.350|  0.000|   142|  3173.681| 76.628|  44,743|
| |Audrain County|     1| 39.389|  0.000|   199|  7838.349| 39.389|  25,388|
| |Laclede County|     1| 27.993|  0.000|   195|  5458.668| 27.993|  35,723|
| |Marion County|     1| 35.051|  0.000|   181|  6344.199| 210.305|  28,530|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908| 17.105|   8,352|
| |Grundy County|     1| 101.523|  0.000|    25|  2538.071| 14.503|   9,850|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131| 95.027|   9,020|
| |Bollinger County|     1| 82.420| 11.774|    64|  5274.870| 94.194|  12,133|
| |Bates County|     1| 61.835|  0.000|    44|  2720.752| 70.669|  16,172|
| |Washington County|     1| 40.437|  0.000|    69|  2790.133| 80.873|  24,730|
| |Webster County|     1| 25.258|  0.000|   128|  3232.976| 61.340|  39,592|
| |Randolph County|     1| 40.407|  0.000|    67|  2707.289| 86.587|  24,748|
| |DeKalb County|     1| 79.700|  0.000|    35|  2789.511| 34.157|  12,547|
| |Dallas County|     1| 59.249|  0.000|    60|  3554.924| 110.033|  16,878|
| |Christian County|     1| 11.287|  0.000|   335|  3781.252| 112.873|  88,595|
| |Adair County|     0|  0.000|  0.000|   152|  5997.711| 112.739|  25,343|
| |Dent County|     0|  0.000|  0.000|    10|   642.137|  9.173|  15,573|
| |Daviess County|     0|  0.000|  0.000|    17|  2053.636|  0.000|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865| 18.894|   7,561|
| |Crawford County|     0|  0.000|  0.000|    71|  2968.227| 143.335|  23,920|
| |Clinton County|     0|  0.000|  0.000|    79|  3875.018| 126.131|  20,387|
| |Clark County|     0|  0.000|  0.000|    20|  2942.475| 189.159|   6,797|
| |Chariton County|     0|  0.000|  0.000|    17|  2289.254| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    38|  2648.268| 39.824|  14,349|
| |Carroll County|     0|  0.000|  0.000|   100| 11522.065| 82.300|   8,679|
| |Barton County|     0|  0.000|  0.000|    69|  5870.342| 48.616|  11,754|
| |Atchison County|     0|  0.000|  0.000|    14|  2722.147| 83.331|   5,143|
| |Hickory County|     0|  0.000|  0.000|    28|  2933.780| 179.619|   9,544|
| |Gasconade County|     0|  0.000|  0.000|    21|  1427.989| 19.428|  14,706|
| |Holt County|     0|  0.000|  0.000|     8|  1816.943| 64.891|   4,403|
| |Howard County|     0|  0.000|  0.000|    49|  4899.510| 85.706|  10,001|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939| 70.967|   2,013|
| |Monroe County|     0|  0.000|  0.000|    27|  3123.554| 214.848|   8,644|
| |Mississippi County|     0|  0.000|  0.000|   134| 10166.920| 54.195|  13,180|
| |Maries County|     0|  0.000|  0.000|    20|  2299.644| 147.834|   8,697|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    61|  3335.338| 39.055|  18,289|
| |Wayne County|     0|  0.000|  0.000|    55|  4272.508| 266.338|  12,873|
| |Warren County|     0|  0.000|  0.000|   191|  5357.794| 152.278|  35,649|
| |Vernon County|     0|  0.000|  0.000|    49|  2382.921| 34.736|  20,563|
| |Texas County|     0|  0.000|  0.000|    50|  1968.659| 101.245|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   141| 23156.512| 164.231|   6,089|
| |Shelby County|     0|  0.000|  0.000|    30|  5059.022| 385.449|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    10|  2145.923| 30.656|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    18|  1915.505| 15.202|   9,397|
| |Montgomery County|     0|  0.000|  0.000|    41|  3549.476| 98.940|  11,551|
| |Morgan County|     0|  0.000|  0.000|    78|  3781.451| 110.812|  20,627|
| |Nodaway County|     0|  0.000|  0.000|   175|  7921.420| 181.061|  22,092|
| |Oregon County|     0|  0.000|  0.000|    14|  1329.661| 13.568|  10,529|
| |Ralls County|     0|  0.000|  0.000|    29|  2813.076| 124.718|  10,309|
| |Polk County|     0|  0.000|  0.000|   209|  6500.980| 97.759|  32,149|
| |Phelps County|     0|  0.000|  0.000|    81|  1817.244| 28.845|  44,573|
| |Ozark County|     0|  0.000|  0.000|    12|  1308.044| 93.432|   9,174|
| |Macon County|     0|  0.000|  0.000|    57|  3770.589| 47.250|  15,117|
| |Cooper County|     0|  0.000|  0.000|   116|  6550.342| 242.008|  17,709|
| |Livingston County|     0|  0.000|  0.000|    60|  3940.369| 84.436|  15,227|
| |Knox County|     0|  0.000|  0.000|    27|  6819.904| 649.515|   3,959|
| |Iron County|     0|  0.000|  0.000|    21|  2074.074| 126.984|  10,125|
| |Ripley County|     0|  0.000|  0.000|    51|  3838.049| 107.508|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Mercer County|     0|  0.000|  0.000|    10|  2764.722| 78.992|   3,617|
| |Madison County|     0|  0.000|  0.000|    24|  1985.440| 82.727|  12,088|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,181| 172.935| N/A|112,860| 16526.157| N/A|6,829,174|
| |Shelby County|   302| 322.248|  3.506|22,635| 24152.605| 312.340| 937,166|
| |Davidson County|   212| 305.412|  2.881|20,185| 29078.981| 248.405| 694,144|
| |Sumner County|    73| 381.633|  2.987| 3,365| 17591.736| 193.431| 191,283|
| |Rutherford County|    53| 159.502|  0.860| 6,404| 19272.612| 217.111| 332,285|
| |Hamilton County|    52| 141.380|  1.942| 5,970| 16231.471| 189.154| 367,804|
| |Knox County|    37| 78.671|  2.126| 4,407|  9370.355| 213.232| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,448| 14462.359| 189.348| 238,412|
| |Wilson County|    23| 158.997|  2.963| 2,229| 15408.864| 225.163| 144,657|
| |McMinn County|    20| 371.789|  0.000|   524|  9740.863| 164.649|  53,794|
| |Robertson County|    19| 264.576|  5.968| 1,521| 21180.009| 222.801|  71,813|
| |Putnam County|    17| 211.851|  7.121| 1,717| 21396.972| 354.272|  80,245|
| |Madison County|    17| 173.498|  7.290| 1,024| 10450.686| 371.781|  97,984|
| |Hardeman County|    17| 678.643| 34.217|   875| 34930.140| 655.831|  25,050|
| |Hamblen County|    14| 215.604|  2.200| 1,372| 21129.147| 415.807|  64,934|
| |Montgomery County|    13| 62.203|  1.367| 1,883|  9009.871| 162.001| 208,993|
| |Giles County|    13| 441.216| 24.243|   369| 12523.758| 232.730|  29,464|
| |Macon County|    13| 528.412|  0.000|   856| 34793.919| 209.042|  24,602|
| |Bradley County|    12| 110.998|  2.643| 1,874| 17334.197| 294.673| 108,110|
| |Sullivan County|    12| 75.782|  3.609|   933|  5892.086| 184.043| 158,348|
| |Bedford County|    11| 221.270|  2.874|   908| 18264.840| 244.259|  49,713|
| |Blount County|    10| 75.138|  3.220| 1,243|  9339.685| 214.681| 133,088|
| |Tipton County|     9| 146.106|  0.000| 1,183| 19204.857| 273.659|  61,599|
| |Monroe County|     9| 193.361|  0.000|   407|  8744.226| 227.123|  46,545|
| |Lauderdale County|     8| 312.098| 11.146|   487| 18998.947| 423.561|  25,633|
| |Fayette County|     8| 194.491|  0.000|   670| 16288.625| 257.006|  41,133|
| |Hardin County|     8| 311.867|  5.569|   453| 17659.442| 373.126|  25,652|
| |Cheatham County|     7| 172.130|  7.026|   573| 14090.048| 200.233|  40,667|
| |Greene County|     7| 101.348|  4.137|   447|  6471.789| 213.037|  69,069|
| |Dyer County|     7| 188.380|  3.844|   619| 16658.145| 399.826|  37,159|
| |Hawkins County|     7| 123.270|  7.547|   435|  7660.339| 362.262|  56,786|
| |Maury County|     7| 72.624|  2.964| 1,178| 12221.565| 248.996|  96,387|
| |Sevier County|     7| 71.247|  2.908| 1,830| 18625.954| 270.447|  98,250|
| |Anderson County|     6| 77.944|  1.856|   668|  8677.804| 180.014|  76,978|
| |Haywood County|     6| 346.741|  8.256|   457| 26410.079| 776.039|  17,304|
| |Trousdale County|     6| 531.726|  0.000| 1,582| 140198.511| 151.922|  11,284|
| |Lawrence County|     6| 135.925|  0.000|   534| 12097.322| 291.268|  44,142|
| |Cumberland County|     6| 99.141|  0.000|   412|  6807.667| 110.943|  60,520|
| |Carter County|     6| 106.400|  2.533|   497|  8813.463| 271.067|  56,391|
| |White County|     5| 182.849| 10.449|   273|  9983.544| 454.510|  27,345|
| |McNairy County|     5| 194.598|  0.000|   366| 14244.571| 366.956|  25,694|
| |Gibson County|     5| 101.765|  8.723|   670| 13636.456| 386.705|  49,133|
| |Weakley County|     4| 120.019|  4.286|   397| 11911.906| 720.115|  33,328|
| |Crockett County|     4| 281.096| 10.039|   260| 18271.258| 441.723|  14,230|
| |Franklin County|     4| 94.769|  0.000|   313|  7415.656| 186.153|  42,208|
| |Marion County|     4| 138.375|  0.000|   216|  7472.239| 103.781|  28,907|
| |Obion County|     4| 133.027|  0.000|   519| 17260.301| 674.639|  30,069|
| |Warren County|     4| 96.906|  0.000|   498| 12064.830| 425.695|  41,277|
| |Smith County|     4| 198.442|  7.087|   446| 22126.308| 751.246|  20,157|
| |Loudon County|     3| 55.486|  0.000|   718| 13279.574| 295.924|  54,068|
| |Humphreys County|     3| 161.447|  0.000|   120|  6457.862| 161.447|  18,582|
| |Jefferson County|     3| 55.051|  2.621|   552| 10129.370| 204.475|  54,495|
| |Marshall County|     3| 87.273|  4.156|   283|  8232.727| 103.896|  34,375|
| |Polk County|     3| 178.232| 16.974|   195| 11585.076| 466.798|  16,832|
| |Carroll County|     3| 108.042|  0.000|   290| 10444.052| 509.340|  27,767|
| |Coffee County|     3| 53.079|  2.528|   507|  8970.276| 346.274|  56,520|
| |Decatur County|     3| 257.224| 24.497|   198| 16976.764| 587.940|  11,663|
| |Wayne County|     2| 119.954|  8.568|   225| 13494.872| 162.795|  16,673|
| |Washington County|     2| 15.459|  0.000| 1,200|  9275.362| 283.782| 129,375|
| |Roane County|     2| 37.466|  2.676|   433|  8111.348| 275.641|  53,382|
| |Chester County|     2| 115.627|  8.259|   211| 12198.647| 247.772|  17,297|
| |Dickson County|     2| 37.073|  2.648|   666| 12345.221| 240.973|  53,948|
| |DeKalb County|     2| 97.609|  6.972|   339| 16544.656| 306.770|  20,490|
| |Cocke County|     2| 55.549|  3.968|   450| 12498.611| 321.393|  36,004|
| |Henderson County|     2| 71.131| 10.162|   547| 19454.423| 645.263|  28,117|
| |Grundy County|     2| 148.954|  0.000|   111|  8266.925| 148.954|  13,427|
| |Rhea County|     1| 30.150|  0.000|   522| 15738.535| 176.595|  33,167|
| |Benton County|     1| 61.881|  0.000|   139|  8601.485| 521.570|  16,160|
| |Bledsoe County|     1| 66.383|  0.000|   690| 45804.567| 293.984|  15,064|
| |Campbell County|     1| 25.099|  0.000|   239|  5998.695| 175.694|  39,842|
| |Lincoln County|     1| 29.099|  0.000|   276|  8031.194| 174.591|  34,366|
| |Lewis County|     1| 81.513|  0.000|    71|  5787.414| 279.473|  12,268|
| |Hancock County|     1| 151.057|  0.000|    78| 11782.477| 151.057|   6,620|
| |Jackson County|     1| 84.846|  0.000|   118| 10011.878| 157.572|  11,786|
| |Pickett County|     1| 198.098|  0.000|    31|  6141.046| 282.998|   5,048|
| |Overton County|     1| 44.962|  0.000|   175|  7868.351| 321.157|  22,241|
| |Morgan County|     1| 46.722|  0.000|   103|  4812.409| 220.263|  21,403|
| |Meigs County|     0|  0.000|  0.000|   101|  8130.736| 103.503|  12,422|
| |Fentress County|     0|  0.000|  0.000|    88|  4750.850| 131.111|  18,523|
| |Grainger County|     0|  0.000|  0.000|   194|  8319.039| 196.030|  23,320|
| |Henry County|     0|  0.000|  0.000|   266|  8223.837| 393.083|  32,345|
| |Hickman County|     0|  0.000|  0.000|   253| 10048.455| 255.325|  25,178|
| |Houston County|     0|  0.000|  0.000|    57|  6950.372| 52.258|   8,201|
| |Johnson County|     0|  0.000|  0.000|   258| 14504.160| 1140.416|  17,788|
| |Lake County|     0|  0.000|  0.000|   782| 111459.521| 936.635|   7,016|
| |Unicoi County|     0|  0.000|  0.000|   156|  8723.369| 215.688|  17,883|
| |Moore County|     0|  0.000|  0.000|    60|  9247.842| 396.336|   6,488|
| |Perry County|     0|  0.000|  0.000|    77|  9534.423| 141.513|   8,076|
| |Cannon County|     0|  0.000|  0.000|   142|  9674.343| 311.448|  14,678|
| |Claiborne County|     0|  0.000|  0.000|   255|  7978.973| 219.031|  31,959|
| |Clay County|     0|  0.000|  0.000|    74|  9717.663| 300.159|   7,615|
| |Scott County|     0|  0.000|  0.000|   118|  5347.109| 174.784|  22,068|
| |Sequatchie County|     0|  0.000|  0.000|   102|  6788.234| 85.566|  15,026|
| |Stewart County|     0|  0.000|  0.000|    73|  5322.639| 83.329|  13,715|
| |Union County|     0|  0.000|  0.000|   150|  7510.515| 286.115|  19,972|
| |Van Buren County|     0|  0.000|  0.000|    35|  5960.490| 121.643|   5,872|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   990| 170.032| N/A|58,768| 10093.373| N/A|5,822,434|
| |Milwaukee County|   453| 478.997|  2.266|20,637| 21821.331| 209.816| 945,726|
| |Racine County|    78| 397.329|  0.728| 3,459| 17620.001| 264.886| 196,311|
| |Kenosha County|    59| 347.957|  5.898| 2,609| 15386.793| 154.180| 169,561|
| |Waukesha County|    58| 143.494|  1.767| 4,030|  9970.361| 191.561| 404,198|
| |Brown County|    52| 196.566|  0.540| 4,193| 15850.035| 147.965| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,436|  8114.214| 91.459| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,410|  8631.561| 59.468| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,298| 12496.630| 163.669| 103,868|
| |Washington County|    22| 161.724|  0.000|   991|  7284.943| 195.329| 136,034|
| |Winnebago County|    18| 104.708|  0.831| 1,124|  6538.419| 91.412| 171,907|
| |Ozaukee County|    17| 190.538|  1.601|   647|  7251.656| 190.538|  89,221|
| |Waupaca County|    15| 294.175|  2.802|   430|  8433.026| 224.134|  50,990|
| |Grant County|    15| 291.608|  2.777|   346|  6726.414| 77.762|  51,439|
| |Outagamie County|    14| 74.514|  1.521| 1,208|  6429.465| 111.770| 187,885|
| |Sheboygan County|     9| 78.030|  4.954|   733|  6355.124| 191.979| 115,340|
| |Marathon County|     9| 66.327|  4.211|   623|  4591.280| 80.013| 135,692|
| |Fond du Lac County|     7| 67.696|  1.382|   612|  5918.590| 114.669| 103,403|
| |Clark County|     7| 201.300|  0.000|   183|  5262.552| 61.622|  34,774|
| |Jefferson County|     5| 58.984|  0.000|   612|  7219.620| 114.597|  84,769|
| |Dodge County|     5| 56.922|  0.000|   782|  8902.651| 206.547|  87,839|
| |St. Croix County|     5| 55.135|  4.726|   481|  5303.958| 66.162|  90,687|
| |Richland County|     4| 231.857|  0.000|    36|  2086.715| 91.087|  17,252|
| |Forest County|     4| 444.247|  0.000|    59|  6552.643| 15.866|   9,004|
| |Eau Claire County|     4| 38.224|  1.365|   563|  5380.043| 121.498| 104,646|
| |Sauk County|     3| 46.553|  0.000|   425|  6595.078| 172.913|  64,442|
| |Marinette County|     3| 74.349|  0.000|   376|  9318.463| 339.883|  40,350|
| |Barron County|     3| 66.307|  0.000|   282|  6232.871| 170.504|  45,244|
| |Door County|     3| 108.429|  0.000|   102|  3686.569| 92.939|  27,668|
| |Trempealeau County|     2| 67.456|  0.000|   332| 11197.680| 149.367|  29,649|
| |Buffalo County|     2| 153.480|  0.000|    44|  3376.564| 32.889|  13,031|
| |Adams County|     2| 98.912|  0.000|    82|  4055.391| 91.847|  20,220|
| |Pierce County|     2| 46.779|  6.683|   204|  4771.483| 133.655|  42,754|
| |Polk County|     2| 45.680|  0.000|   126|  2877.829| 48.943|  43,783|
| |Calumet County|     2| 39.929|  0.000|   296|  5909.481| 171.124|  50,089|
| |Monroe County|     2| 43.240|  3.089|   242|  5232.093| 114.278|  46,253|
| |Kewaunee County|     2| 97.876|  0.000|   127|  6215.132| 125.841|  20,434|
| |Waushara County|     1| 40.912|  5.845|   114|  4663.912| 87.668|  24,443|
| |Wood County|     1| 13.699|  0.000|   276|  3780.874| 117.418|  72,999|
| |Burnett County|     1| 64.876|  0.000|    21|  1362.398| 74.144|  15,414|
| |La Crosse County|     1|  8.473|  0.000|   889|  7532.877| 122.259| 118,016|
| |Juneau County|     1| 37.471|  0.000|   135|  5058.643| 85.649|  26,687|
| |Jackson County|     1| 48.443|  0.000|    55|  2664.341| 62.283|  20,643|
| |Langlade County|     1| 52.113|  0.000|    59|  3074.678| 119.116|  19,189|
| |Manitowoc County|     1| 12.661|  0.000|   325|  4114.914| 68.733|  78,981|
| |Columbia County|     1| 17.382|  0.000|   241|  4188.973| 69.527|  57,532|
| |Rusk County|     1| 70.532|  0.000|    17|  1199.041| 30.228|  14,178|
| |Iron County|     1| 175.840|  0.000|    74| 13012.133| 75.360|   5,687|
| |Green County|     1| 27.056|  0.000|   149|  4031.385| 100.495|  36,960|
| |Ashland County|     1| 64.259|  9.180|    24|  1542.218| 82.619|  15,562|
| |Bayfield County|     1| 66.507|  0.000|    22|  1463.155| 38.004|  15,036|
| |Marquette County|     1| 64.210|  0.000|    76|  4879.928| 64.210|  15,574|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689| 39.209|   7,287|
| |Iowa County|     0|  0.000|  0.000|    74|  3125.264| 72.400|  23,678|
| |Oneida County|     0|  0.000|  0.000|   112|  3146.509| 124.416|  35,595|
| |Price County|     0|  0.000|  0.000|    29|  2172.122| 107.001|  13,351|
| |Portage County|     0|  0.000|  0.000|   389|  5496.524| 104.965|  70,772|
| |Lafayette County|     0|  0.000|  0.000|   122|  7320.732| 162.873|  16,665|
| |Lincoln County|     0|  0.000|  0.000|    67|  2428.152| 36.241|  27,593|
| |Chippewa County|     0|  0.000|  0.000|   223|  3448.916| 33.141|  64,658|
| |Crawford County|     0|  0.000|  0.000|    72|  4463.455| 141.697|  16,131|
| |Green Lake County|     0|  0.000|  0.000|    55|  2908.053| 22.660|  18,913|
| |Florence County|     0|  0.000|  0.000|     7|  1629.802|  0.000|   4,295|
| |Dunn County|     0|  0.000|  0.000|   119|  2622.994| 53.530|  45,368|
| |Douglas County|     0|  0.000|  0.000|   159|  3684.820| 152.293|  43,150|
| |Shawano County|     0|  0.000|  0.000|   178|  4352.185| 108.281|  40,899|
| |Sawyer County|     0|  0.000|  0.000|    52|  3140.476| 155.298|  16,558|
| |Oconto County|     0|  0.000|  0.000|   219|  5773.794| 207.149|  37,930|
| |Menominee County|     0|  0.000|  0.000|    20|  4389.816| 62.712|   4,556|
| |Washburn County|     0|  0.000|  0.000|    41|  2608.142| 181.752|  15,720|
| |Vilas County|     0|  0.000|  0.000|    48|  2162.649| 122.293|  22,195|
| |Vernon County|     0|  0.000|  0.000|    59|  1914.217| 18.540|  30,822|
| |Taylor County|     0|  0.000|  0.000|    64|  3146.045| 119.381|  20,343|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   915| 290.009| N/A|48,039| 15225.970| N/A|3,155,070|
| |Polk County|   206| 420.270|  1.457|10,132| 20670.759| 190.316| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,314| 10207.052| 194.714| 226,706|
| |Black Hawk County|    63| 480.080|  1.089| 3,099| 23615.387| 140.432| 131,228|
| |Woodbury County|    51| 494.632|  2.771| 3,709| 35972.339| 123.312| 103,107|
| |Muscatine County|    48| 1125.070|  3.348|   845| 19805.925| 127.240|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,859| 19892.352| 183.438|  93,453|
| |Wapello County|    33| 943.693|  8.171|   876| 25050.759| 200.177|  34,969|
| |Dubuque County|    31| 318.566|  4.404| 1,653| 16986.774| 248.100|  97,311|
| |Tama County|    29| 1720.660|  0.000|   547| 32455.204| 110.190|  16,854|
| |Pottawattamie County|    26| 278.952|  7.664| 1,294| 13883.226| 216.111|  93,206|
| |Jasper County|    26| 699.207|  7.684|   471| 12666.398| 80.678|  37,185|
| |Marshall County|    25| 635.017|  3.629| 1,432| 36373.797| 214.092|  39,369|
| |Mahaska County|    17| 769.405|  0.000|   138|  6245.757| 32.328|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   598| 14087.161| 87.498|  42,450|
| |Johnson County|    16| 105.862|  0.945| 2,054| 13590.049| 163.519| 151,140|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Story County|    14| 144.156|  1.471| 1,151| 11851.684| 92.672|  97,117|
| |Scott County|    14| 80.952|  1.652| 1,674|  9679.490| 96.646| 172,943|
| |Buena Vista County|    12| 611.621|  0.000| 1,791| 91284.404| 65.531|  19,620|
| |Washington County|    10| 455.270|  0.000|   294| 13384.931| 65.039|  21,965|
| |Franklin County|     9| 893.744| 70.932|   235| 23336.643| 368.847|  10,070|
| |Plymouth County|     9| 357.469|  5.674|   455| 18072.050| 113.482|  25,177|
| |Poweshiek County|     8| 432.339|  0.000|   156|  8430.610| 146.686|  18,504|
| |Bremer County|     7| 279.307|  0.000|   210|  8379.220| 165.304|  25,062|
| |Webster County|     7| 194.964|  7.958|   793| 22086.676| 374.013|  35,904|
| |Monroe County|     7| 908.265|  0.000|    72|  9342.156| 111.216|   7,707|
| |Guthrie County|     5| 467.771|  0.000|   131| 12255.590| 93.554|  10,689|
| |Allamakee County|     4| 292.248|  0.000|   154| 11251.553| 62.625|  13,687|
| |Dickinson County|     4| 231.777|  0.000|   378| 21902.886| 57.944|  17,258|
| |Montgomery County|     4| 403.348| 14.405|    57|  5747.706| 216.079|   9,917|
| |Emmet County|     4| 434.405| 46.543|   190| 20634.231| 186.174|   9,208|
| |Lucas County|     4| 465.116|  0.000|    60|  6976.744| 299.003|   8,600|
| |Sioux County|     3| 86.071|  4.099|   619| 17759.288| 127.057|  34,855|
| |Appanoose County|     3| 241.429|  0.000|    48|  3862.868| 91.973|  12,426|
| |Lee County|     3| 89.135|  0.000|   108|  3208.842| 80.646|  33,657|
| |Henry County|     3| 150.346|  0.000|   119|  5963.717| 71.593|  19,954|
| |Crawford County|     3| 178.359|  0.000|   726| 43162.901| 161.373|  16,820|
| |Clinton County|     3| 64.615|  0.000|   370|  7969.157| 252.305|  46,429|
| |Clayton County|     3| 170.950|  0.000|   104|  5926.264| 81.405|  17,549|
| |Clarke County|     3| 319.319|  0.000|   197| 20968.600| 349.730|   9,395|
| |Hancock County|     2| 188.147|  0.000|   121| 11382.879| 94.073|  10,630|
| |Butler County|     2| 138.514|  0.000|   119|  8241.568| 79.151|  14,439|
| |Des Moines County|     2| 51.325|  0.000|   158|  4054.713| 51.325|  38,967|
| |Boone County|     2| 76.237|  0.000|   246|  9377.144| 108.910|  26,234|
| |Floyd County|     2| 127.861|  0.000|   145|  9269.914| 328.785|  15,642|
| |O'Brien County|     2| 145.423| 10.387|   136|  9888.752| 207.747|  13,753|
| |Lyon County|     2| 170.140| 24.306|   110|  9357.720| 133.682|  11,755|
| |Madison County|     2| 122.414|  0.000|   114|  6977.598| 183.621|  16,338|
| |Calhoun County|     2| 206.868|  0.000|    83|  8585.023| 29.553|   9,668|
| |Jones County|     2| 96.707|  6.908|   128|  6189.256| 41.446|  20,681|
| |Audubon County|     1| 181.951|  0.000|    28|  5094.614|  0.000|   5,496|
| |Benton County|     1| 38.994|  0.000|   151|  5888.087| 116.982|  25,645|
| |Jackson County|     1| 51.443|  0.000|   150|  7716.446| 132.282|  19,439|
| |Iowa County|     1| 61.789|  0.000|    96|  5931.784| 79.444|  16,184|
| |Humboldt County|     1| 104.624|  0.000|   106| 11090.186| 283.981|   9,558|
| |Pocahontas County|     1| 151.080|  0.000|   115| 17374.226| 43.166|   6,619|
| |Ringgold County|     1| 204.332|  0.000|    21|  4290.969|  0.000|   4,894|
| |Shelby County|     1| 87.306|  0.000|   180| 15715.034| 311.806|  11,454|
| |Keokuk County|     1| 97.599|  0.000|    34|  3318.368| 83.656|  10,246|
| |Warren County|     1| 19.430|  0.000|   550| 10686.667| 130.461|  51,466|
| |Grundy County|     1| 81.753|  0.000|    78|  6376.717| 70.074|  12,232|
| |Wayne County|     1| 155.255|  0.000|    19|  2949.853| 88.717|   6,441|
| |Winneshiek County|     1| 50.023|  0.000|    94|  4702.116| 121.483|  19,991|
| |Union County|     1| 81.693|  0.000|    76|  6208.643| 116.704|  12,241|
| |Hamilton County|     1| 67.691|  0.000|   245| 16584.309| 77.361|  14,773|
| |Delaware County|     1| 58.785|  0.000|   103|  6054.906| 151.163|  17,011|
| |Davis County|     1| 111.111|  0.000|    54|  6000.000| 79.365|   9,000|
| |Wright County|     1| 79.605|  0.000|   463| 36857.188| 272.932|  12,562|
| |Carroll County|     1| 49.591|  0.000|   185|  9174.312| 70.844|  20,165|
| |Clay County|     1| 62.438|  0.000|   181| 11301.199| 115.955|  16,016|
| |Cedar County|     1| 53.686|  0.000|   129|  6925.431| 92.032|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   104|  9256.787| 89.008|  11,235|
| |Cass County|     1| 77.906|  0.000|    61|  4752.259| 211.459|  12,836|
| |Buchanan County|     1| 47.226|  0.000|   124|  5855.962| 128.184|  21,175|
| |Van Buren County|     1| 141.965|  0.000|    34|  4826.803| 101.403|   7,044|
| |Marion County|     0|  0.000|  0.000|   166|  4992.031| 81.625|  33,253|
| |Worth County|     0|  0.000|  0.000|    66|  8941.878| 135.483|   7,381|
| |Winnebago County|     0|  0.000|  0.000|    79|  7629.901| 110.378|  10,354|
| |Taylor County|     0|  0.000|  0.000|    96| 15683.712| 70.017|   6,121|
| |Sac County|     0|  0.000|  0.000|    82|  8435.346| 44.087|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    82|  9227.999| 128.613|   8,886|
| |Page County|     0|  0.000|  0.000|    94|  6222.281| 236.409|  15,107|
| |Osceola County|     0|  0.000|  0.000|    80| 13427.325| 71.932|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972| 33.165|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    78|  7368.222| 26.990|  10,586|
| |Mills County|     0|  0.000|  0.000|    87|  5758.157| 104.006|  15,109|
| |Adams County|     0|  0.000|  0.000|    16|  4441.977| 39.661|   3,602|
| |Adair County|     0|  0.000|  0.000|    28|  3914.989| 159.795|   7,152|
| |Fremont County|     0|  0.000|  0.000|    40|  5747.126| 164.204|   6,960|
| |Fayette County|     0|  0.000|  0.000|    82|  4173.028| 36.350|  19,650|
| |Howard County|     0|  0.000|  0.000|    49|  5350.513| 31.198|   9,158|
| |Harrison County|     0|  0.000|  0.000|   103|  7331.483| 132.190|  14,049|
| |Hardin County|     0|  0.000|  0.000|   175| 10388.223| 118.723|  16,846|
| |Ida County|     0|  0.000|  0.000|    29|  4227.405|  0.000|   6,860|
| |Decatur County|     0|  0.000|  0.000|    23|  2922.490| 36.304|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    54|  4525.266| 71.830|  11,933|
| |Greene County|     0|  0.000|  0.000|    41|  4612.961| 48.219|   8,888|
| |Jefferson County|     0|  0.000|  0.000|    82|  4482.099| 54.660|  18,295|
| |Kossuth County|     0|  0.000|  0.000|    84|  5670.695| 77.152|  14,813|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   912| 296.089| N/A|54,203| 17597.485| N/A|3,080,156|
| |Clark County|   770| 339.699|  5.231|46,990| 20730.440| 362.072|2,266,715|
| |Washoe County|   118| 250.255|  1.515| 5,627| 11933.771| 146.336| 471,519|
| |Nye County|     9| 193.453|  0.000|   400|  8597.898| 178.099|  46,523|
| |Lyon County|     6| 104.330|  2.484|   218|  3790.645| 59.617|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   100|  5941.418| 33.951|  16,831|
| |Elko County|     2| 37.895|  0.000|   525|  9947.327| 173.232|  52,778|
| |Churchill County|     1| 40.146|  0.000|    50|  2007.307| 34.411|  24,909|
| |White Pine County|     1| 104.384|  0.000|    14|  1461.378| 14.912|   9,580|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 51.648|   5,532|
| |Eureka County|     0|  0.000|  0.000|     2|   985.707|  0.000|   2,029|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     4|   970.167|  0.000|   4,123|
| |Pershing County|     0|  0.000|  0.000|    13|  1933.086|  0.000|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     4|   771.754| 27.563|   5,183|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Douglas County|     0|  0.000|  0.000|   194|  3966.875| 93.476|  48,905|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   764| 171.006| N/A|33,796|  7564.564| N/A|4,467,673|
| |Jefferson County|   237| 309.094|  0.932| 7,823| 10202.711| 174.203| 766,757|
| |Fayette County|    47| 145.442|  0.442| 2,984|  9234.045| 145.884| 323,152|
| |Kenton County|    40| 239.524|  2.566| 1,378|  8251.596| 93.243| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   416|  9309.403| 63.938|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,076|  8055.038| 98.389| 133,581|
| |Graves County|    24| 644.019|  7.667|   541| 14517.254| 180.172|  37,266|
| |Logan County|    23| 848.646|  5.271|   320| 11807.247| 121.235|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,580| 19413.677| 223.591| 132,896|
| |Shelby County|    21| 428.362|  0.000|   740| 15094.648| 119.475|  49,024|
| |Adair County|    19| 989.480|  0.000|   204| 10623.893| 22.319|  19,202|
| |Butler County|    15| 1164.687|  0.000|   292| 22672.568| 11.092|  12,879|
| |Oldham County|    15| 224.554| 10.693|   612|  9161.814| 149.703|  66,799|
| |Jackson County|    14| 1050.341|  0.000|   149| 11178.633| 96.460|  13,329|
| |Campbell County|    13| 138.913|  0.000|   557|  5951.872| 96.170|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   100|  8230.453| 129.336|  12,150|
| |Grayson County|    11| 416.241|  0.000|   194|  7340.977| 102.709|  26,427|
| |Casey County|    10| 618.850|  0.000|   162| 10025.373| 123.770|  16,159|
| |Muhlenberg County|    10| 326.563|  4.665|   619| 20214.225| 46.652|  30,622|
| |Daviess County|     9| 88.660|  2.815|   750|  7388.362| 85.846| 101,511|
| |Ohio County|     8| 333.417| 11.908|   353| 14712.011| 83.354|  23,994|
| |Hardin County|     8| 72.099|  0.000|   576|  5191.153| 83.687| 110,958|
| |Allen County|     8| 375.323|  0.000|   224| 10509.031| 53.618|  21,315|
| |Knox County|     8| 256.863|  0.000|   232|  7449.029| 174.300|  31,145|
| |Gallatin County|     7| 789.266|  0.000|    79|  8907.430| 32.215|   8,869|
| |Clark County|     7| 193.034|  0.000|   164|  4522.516| 63.032|  36,263|
| |Franklin County|     7| 137.279|  5.603|   291|  5706.889| 128.874|  50,991|
| |Simpson County|     7| 376.911|  7.692|   147|  7915.141| 84.613|  18,572|
| |Christian County|     6| 85.153|  0.000|   489|  6940.009| 38.522|  70,461|
| |Grant County|     5| 199.450|  0.000|   112|  4467.669| 108.273|  25,069|
| |Clay County|     5| 251.244|  0.000|   149|  7487.061| 50.249|  19,901|
| |Russell County|     5| 278.971|  0.000|   102|  5691.012| 55.794|  17,923|
| |Bullitt County|     5| 61.217|  1.749|   348|  4260.738| 83.955|  81,676|
| |Laurel County|     5| 82.219|  2.349|   419|  6889.974| 122.154|  60,813|
| |McCracken County|     4| 61.145|  0.000|   365|  5579.504| 87.350|  65,418|
| |Lyon County|     4| 487.211|  0.000|    34|  4141.291| 87.002|   8,210|
| |Calloway County|     4| 102.561|  7.326|   220|  5640.881| 164.831|  39,001|
| |Henderson County|     3| 66.357|  0.000|   337|  7454.103| 72.677|  45,210|
| |Harlan County|     3| 115.340|  0.000|   223|  8573.626| 164.772|  26,010|
| |Perry County|     3| 116.469|  0.000|   213|  8269.276| 199.661|  25,758|
| |Pulaski County|     3| 46.169|  2.199|   268|  4124.409| 70.352|  64,979|
| |Pike County|     3| 51.835|  0.000|   233|  4025.848| 51.835|  57,876|
| |Bell County|     3| 115.243|  5.488|   303| 11639.521| 197.559|  26,032|
| |Boyd County|     3| 64.215|  0.000|   185|  3959.930| 61.157|  46,718|
| |Floyd County|     2| 56.197|  4.014|    94|  2641.266| 56.197|  35,589|
| |Nelson County|     2| 43.259|  0.000|   207|  4477.321| 64.889|  46,233|
| |Marshall County|     2| 64.309|  0.000|   137|  4405.145| 78.089|  31,100|
| |Meade County|     2| 69.999|  0.000|   100|  3499.930| 94.998|  28,572|
| |Monroe County|     2| 187.793|  0.000|    93|  8732.394| 80.483|  10,650|
| |Taylor County|     2| 77.613|  0.000|   107|  4152.276| 38.806|  25,769|
| |Carroll County|     2| 188.129|  0.000|   150| 14109.679| 134.378|  10,631|
| |Green County|     2| 182.799|  0.000|    31|  2833.379| 26.114|  10,941|
| |Barren County|     2| 45.199|  0.000|   360|  8135.777| 145.282|  44,249|
| |Breckinridge County|     2| 97.671|  0.000|    65|  3174.293| 111.623|  20,477|
| |Henry County|     2| 124.023|  0.000|   119|  7379.387| 274.623|  16,126|
| |Metcalfe County|     2| 198.590|  0.000|    57|  5659.815| 156.035|  10,071|
| |Mason County|     1| 58.582|  0.000|    53|  3104.862|  8.369|  17,070|
| |Knott County|     1| 67.540|  0.000|    49|  3309.469| 106.135|  14,806|
| |Greenup County|     1| 28.492|  0.000|   106|  3020.115| 73.264|  35,098|
| |Fulton County|     1| 167.532|  0.000|    75| 12564.919| 622.263|   5,969|
| |Larue County|     1| 69.454|  0.000|    54|  3750.521| 79.376|  14,398|
| |Madison County|     1| 10.754|  0.000|   456|  4903.911| 132.123|  92,987|
| |McLean County|     1| 108.613|  0.000|    42|  4561.746| 62.065|   9,207|
| |Livingston County|     1| 108.767|  0.000|    33|  3589.297| 15.538|   9,194|
| |Lincoln County|     1| 40.735|  0.000|   101|  4114.221| 29.096|  24,549|
| |Bourbon County|     1| 50.536|  0.000|    75|  3790.176| 50.536|  19,788|
| |Bath County|     1| 80.000|  0.000|    37|  2960.000| 57.143|  12,500|
| |Anderson County|     1| 43.962|  0.000|    82|  3604.871| 62.803|  22,747|
| |Whitley County|     1| 27.576|  0.000|   161|  4439.665| 185.150|  36,264|
| |Webster County|     1| 77.268|  0.000|    88|  6799.567| 99.344|  12,942|
| |Crittenden County|     1| 113.559|  0.000|    29|  3293.209| 48.668|   8,806|
| |Carter County|     1| 37.318|  0.000|   102|  3806.396| 42.649|  26,797|
| |Carlisle County|     1| 210.084|  0.000|    42|  8823.529| 600.240|   4,760|
| |Cumberland County|     0|  0.000|  0.000|    46|  6954.944| 280.790|   6,614|
| |Clinton County|     0|  0.000|  0.000|    28|  2740.262| 69.905|  10,218|
| |Caldwell County|     0|  0.000|  0.000|    49|  3844.042| 44.828|  12,747|
| |Woodford County|     0|  0.000|  0.000|   149|  5573.427| 117.560|  26,734|
| |Johnson County|     0|  0.000|  0.000|    48|  2163.332| 103.016|  22,188|
| |Jessamine County|     0|  0.000|  0.000|   337|  6227.479| 192.711|  54,115|
| |Hickman County|     0|  0.000|  0.000|    41|  9360.731| 260.926|   4,380|
| |Hart County|     0|  0.000|  0.000|    93|  4885.737| 127.585|  19,035|
| |Harrison County|     0|  0.000|  0.000|   119|  6300.964| 45.385|  18,886|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 114.653|   8,722|
| |Garrard County|     0|  0.000|  0.000|    74|  4188.837| 56.606|  17,666|
| |Fleming County|     0|  0.000|  0.000|    58|  3977.779| 48.987|  14,581|
| |Wolfe County|     0|  0.000|  0.000|    13|  1816.404| 79.842|   7,157|
| |Estill County|     0|  0.000|  0.000|    18|  1276.053| 60.764|  14,106|
| |Spencer County|     0|  0.000|  0.000|   111|  5736.138| 125.501|  19,351|
| |Scott County|     0|  0.000|  0.000|   362|  6350.432| 127.811|  57,004|
| |Rowan County|     0|  0.000|  0.000|    70|  2861.815| 17.521|  24,460|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Letcher County|     0|  0.000|  0.000|    58|  2691.041| 79.538|  21,553|
| |Powell County|     0|  0.000|  0.000|    53|  4288.373| 127.149|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    45|  3084.304| 107.706|  14,590|
| |Owsley County|     0|  0.000|  0.000|    13|  2944.507| 129.429|   4,415|
| |Owen County|     0|  0.000|  0.000|    46|  4219.796| 52.420|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    32|  2404.388| 42.936|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   120|  4261.818| 50.736|  28,157|
| |Mercer County|     0|  0.000|  0.000|    81|  3693.065| 71.647|  21,933|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Martin County|     0|  0.000|  0.000|    35|  3126.396| 76.565|  11,195|
| |Marion County|     0|  0.000|  0.000|   120|  6226.327| 140.834|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    34|  2795.823| 187.954|  12,161|
| |McCreary County|     0|  0.000|  0.000|    37|  2147.293| 33.163|  17,231|
| |Lewis County|     0|  0.000|  0.000|    38|  2862.524| 53.807|  13,275|
| |Todd County|     0|  0.000|  0.000|    34|  2765.577| 34.860|  12,294|
| |Trigg County|     0|  0.000|  0.000|    55|  3754.010| 68.255|  14,651|
| |Lee County|     0|  0.000|  0.000|     6|   810.482| 57.892|   7,403|
| |Lawrence County|     0|  0.000|  0.000|    36|  2350.330| 37.307|  15,317|
| |Leslie County|     0|  0.000|  0.000|    28|  2834.869| 43.391|   9,877|
| |Wayne County|     0|  0.000|  0.000|    53|  2606.600| 21.078|  20,333|
| |Rockcastle County|     0|  0.000|  0.000|    65|  3893.381| 42.784|  16,695|
| |Washington County|     0|  0.000|  0.000|    76|  6283.588| 248.036|  12,095|
| |Union County|     0|  0.000|  0.000|    65|  4519.853| 119.205|  14,381|
| |Trimble County|     0|  0.000|  0.000|    33|  3895.644| 16.864|   8,471|
| |Breathitt County|     0|  0.000|  0.000|    28|  2216.944| 45.244|  12,630|
| |Bracken County|     0|  0.000|  0.000|    30|  3613.152| 17.205|   8,303|
| |Boyle County|     0|  0.000|  0.000|   149|  4956.753| 95.048|  30,060|
| |Ballard County|     0|  0.000|  0.000|    33|  4183.570| 54.332|   7,888|
| |Elliott County|     0|  0.000|  0.000|     8|  1064.254| 19.005|   7,517|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   675| 321.915| N/A|20,670|  9857.742| N/A|2,096,829|
| |McKinley County|   222| 3110.681|  6.005| 4,037| 56566.761| 98.085|  71,367|
| |San Juan County|   183| 1476.306|  3.457| 3,037| 24500.234| 49.556| 123,958|
| |Bernalillo County|   130| 191.424|  2.104| 5,059|  7449.335| 68.155| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,126|  7673.018| 54.515| 146,748|
| |Dona Ana County|    30| 137.492|  5.893| 2,398| 10990.169| 148.622| 218,195|
| |Cibola County|    17| 637.301|  0.000|   361| 13533.271| 160.664|  26,675|
| |Otero County|    10| 148.170|  0.000|   199|  2948.585| 35.984|  67,490|
| |Socorro County|     6| 360.642|  0.000|    72|  4327.703|  0.000|  16,637|
| |Chaves County|     6| 92.858|  2.211|   419|  6484.562| 187.926|  64,615|
| |Rio Arriba County|     6| 154.158|  7.341|   313|  8041.931| 73.409|  38,921|
| |Lea County|     4| 56.283|  2.010|   740| 10412.270| 271.362|  71,070|
| |Eddy County|     4| 68.423|  2.444|   284|  4858.023| 102.634|  58,460|
| |Valencia County|     4| 52.159|  0.000|   404|  5268.099| 93.142|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   626|  4163.397| 61.757| 150,358|
| |Luna County|     3| 126.534|  0.000|   241| 10164.916| 108.458|  23,709|
| |Curry County|     2| 40.855|  0.000|   533| 10887.772| 233.455|  48,954|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824| 26.457|  26,998|
| |Union County|     2| 492.732| 70.390|    29|  7144.617| 140.781|   4,059|
| |Lincoln County|     2| 102.187|  7.299|   118|  6029.021| 153.280|  19,572|
| |Taos County|     1| 30.560|  0.000|   106|  3239.312| 52.388|  32,723|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411| 18.480|  15,461|
| |Colfax County|     1| 83.745|  0.000|    17|  1423.666| 47.854|  11,941|
| |Quay County|     1| 121.168|  0.000|    34|  4119.714| 51.929|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   160|  8648.649| 162.162|  18,500|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |Sierra County|     0|  0.000|  0.000|    31|  2872.764| 39.716|  10,791|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |San Miguel County|     0|  0.000|  0.000|    42|  1539.759|  5.237|  27,277|
| |Guadalupe County|     0|  0.000|  0.000|    31|  7209.302|  0.000|   4,300|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Hidalgo County|     0|  0.000|  0.000|    89| 21200.572| 136.119|   4,198|
| |Los Alamos County|     0|  0.000|  0.000|    20|  1032.578|  0.000|  19,369|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   600| 151.631| N/A|42,234| 10673.316| N/A|3,956,971|
| |Oklahoma County|   112| 140.450|  2.687|10,300| 12916.429| 249.013| 797,434|
| |Tulsa County|   106| 162.688|  1.754|10,135| 15555.167| 312.441| 651,552|
| |Cleveland County|    55| 193.652|  3.018| 2,932| 10323.435| 189.628| 284,014|
| |Washington County|    39| 756.885|  0.000|   616| 11954.897| 163.576|  51,527|
| |McCurtain County|    28| 852.827| 13.053|   848| 25828.460| 143.588|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   825| 10148.975| 244.278|  81,289|
| |Delaware County|    19| 441.768|  0.000|   419|  9742.147| 96.325|  43,009|
| |Caddo County|    16| 556.290|  9.934|   404| 14046.311| 278.145|  28,762|
| |Rogers County|    16| 173.050|  3.090|   939| 10155.853| 282.751|  92,459|
| |Muskogee County|    16| 235.304|  0.000|   490|  7206.200| 155.469|  67,997|
| |Creek County|    14| 195.744|  1.997|   580|  8109.393| 213.720|  71,522|
| |Kay County|    11| 252.653|  3.281|   238|  5466.489| 101.717|  43,538|
| |Osage County|    11| 234.227|  0.000|   397|  8453.463| 139.928|  46,963|
| |Comanche County|    10| 82.816|  0.000|   798|  6608.750| 49.690| 120,749|
| |Pottawatomie County|     9| 123.981|  5.904|   433|  5964.845| 145.628|  72,592|
| |Greer County|     8| 1400.560| 25.010|    82| 14355.742| 50.020|   5,712|
| |Canadian County|     7| 47.200|  1.927| 1,174|  7916.065| 158.938| 148,306|
| |Grady County|     7| 125.372|  2.559|   430|  7701.401| 84.434|  55,834|
| |Texas County|     7| 350.298|  0.000| 1,049| 52494.620| 128.681|  19,983|
| |Mayes County|     6| 145.985|  0.000|   309|  7518.248| 132.082|  41,100|
| |Adair County|     6| 270.343|  6.437|   328| 14778.769| 289.654|  22,194|
| |Seminole County|     5| 206.118|  0.000|   227|  9357.738| 235.563|  24,258|
| |Garfield County|     5| 81.892|  2.340|   420|  6878.931| 210.580|  61,056|
| |Jackson County|     5| 203.832| 11.648|   514| 20953.934| 267.894|  24,530|
| |Carter County|     4| 83.141|  2.969|   331|  6879.924| 124.712|  48,111|
| |McClain County|     4| 98.829|  0.000|   427| 10549.983| 155.303|  40,474|
| |Garvin County|     4| 144.347|  0.000|   221|  7975.172| 123.726|  27,711|
| |Sequoyah County|     4| 96.226|  0.000|   319|  7673.988| 340.226|  41,569|
| |Payne County|     4| 48.909|  1.747|   717|  8766.996| 115.286|  81,784|
| |Ottawa County|     3| 96.379|  4.589|   367| 11790.407| 183.580|  31,127|
| |Okmulgee County|     3| 77.993|  3.714|   453| 11776.940| 308.258|  38,465|
| |Pawnee County|     3| 183.195|  0.000|   134|  8182.706| 157.024|  16,376|
| |Stephens County|     3| 69.536|  3.311|   193|  4473.495| 82.781|  43,143|
| |Pittsburg County|     3| 68.722|  0.000|   310|  7101.297| 454.876|  43,654|
| |Cotton County|     2| 352.983|  0.000|    18|  3176.844| 25.213|   5,666|
| |Lincoln County|     2| 57.344|  0.000|   156|  4472.862| 155.649|  34,877|
| |Noble County|     2| 179.678|  0.000|    83|  7456.653| 77.005|  11,131|
| |Pontotoc County|     2| 52.241|  0.000|   193|  5041.271| 108.214|  38,284|
| |Cherokee County|     2| 41.104|  2.936|   398|  8179.707| 284.792|  48,657|
| |Choctaw County|     1| 68.157|  0.000|   175| 11927.481| 146.051|  14,672|
| |Marshall County|     1| 59.063|  8.438|   106|  6260.705| 109.689|  16,931|
| |Hughes County|     1| 75.307|  0.000|   126|  9488.666| 279.711|  13,279|
| |Bryan County|     1| 20.836|  0.000|   431|  8980.102| 169.661|  47,995|
| |Beckham County|     1| 45.748|  6.535|    52|  2378.883| 65.354|  21,859|
| |Nowata County|     1| 99.246|  0.000|    57|  5657.007| 85.068|  10,076|
| |Okfuskee County|     1| 83.382| 11.912|    62|  5169.682| 107.205|  11,993|
| |Le Flore County|     1| 20.059|  0.000|   311|  6238.341| 266.498|  49,853|
| |Latimer County|     1| 99.275|  0.000|    86|  8537.675| 312.008|  10,073|
| |Kiowa County|     1| 114.837|  0.000|    27|  3100.597| 49.216|   8,708|
| |Tillman County|     1| 137.931|  0.000|    58|  8000.000| 98.522|   7,250|
| |Major County|     1| 131.079|  0.000|    34|  4456.678| 149.804|   7,629|
| |McIntosh County|     1| 51.031|  0.000|   178|  9083.486| 255.154|  19,596|
| |Logan County|     1| 20.829|  0.000|   202|  4207.369| 95.216|  48,011|
| |Murray County|     0|  0.000|  0.000|    69|  4903.006| 101.512|  14,073|
| |Washita County|     0|  0.000|  0.000|    27|  2473.433| 39.261|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   107|  9643.115| 231.744|  11,096|
| |Roger Mills County|     0|  0.000|  0.000|     8|  2232.766|  0.000|   3,583|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 81.233|   8,793|
| |Woodward County|     0|  0.000|  0.000|    37|  1830.686| 35.341|  20,211|
| |Craig County|     0|  0.000|  0.000|    79|  5586.197| 101.016|  14,142|
| |Dewey County|     0|  0.000|  0.000|     9|  1840.114| 58.416|   4,891|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Grant County|     0|  0.000|  0.000|    13|  3000.231| 65.939|   4,333|
| |Harmon County|     0|  0.000|  0.000|    27| 10177.158| 269.237|   2,653|
| |Harper County|     0|  0.000|  0.000|     9|  2440.347| 154.943|   3,688|
| |Haskell County|     0|  0.000|  0.000|    55|  4355.746| 226.272|  12,627|
| |Jefferson County|     0|  0.000|  0.000|    32|  5331.556| 71.405|   6,002|
| |Johnston County|     0|  0.000|  0.000|    46|  4149.752| 90.212|  11,085|
| |Kingfisher County|     0|  0.000|  0.000|   123|  7802.093| 199.357|  15,765|
| |Love County|     0|  0.000|  0.000|    73|  7119.867| 125.399|  10,253|
| |Custer County|     0|  0.000|  0.000|   202|  6964.797| 83.735|  29,003|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Atoka County|     0|  0.000|  0.000|    68|  4942.579| 83.069|  13,758|
| |Beaver County|     0|  0.000|  0.000|    36|  6778.384|  0.000|   5,311|
| |Blaine County|     0|  0.000|  0.000|    41|  4348.287|  0.000|   9,429|
| |Cimarron County|     0|  0.000|  0.000|     1|   467.946|  0.000|   2,137|
| |Coal County|     0|  0.000|  0.000|    32|  5823.476| 103.991|   5,495|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   589| 834.574| N/A|12,589| 17837.787| N/A| 705,749|
| |District of Columbia|   589| 834.574|  1.012|12,589| 17837.787| 107.687| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   588| 603.842| N/A|15,201| 15610.559| N/A| 973,764|
| |New Castle County|   289| 517.223|  0.511| 7,130| 12760.558| 85.906| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,803| 24775.323| 118.933| 234,225|
| |Kent County|   107| 591.860|  7.902| 2,268| 12545.219| 79.810| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   521| 172.642| N/A|46,254| 15327.039| N/A|3,017,804|
| |Pulaski County|    83| 211.783|  2.187| 5,407| 13796.500| 245.683| 391,911|
| |Washington County|    51| 213.222|  3.584| 6,231| 26050.747| 200.083| 239,187|
| |Benton County|    41| 146.879|  1.535| 4,698| 16830.204| 122.826| 279,141|
| |Jefferson County|    40| 598.587|  6.413| 1,484| 22207.590| 408.322|  66,824|
| |Crittenden County|    20| 417.058|  8.937| 1,327| 27671.776| 461.742|  47,955|
| |Sebastian County|    19| 148.638|  5.588| 2,079| 16264.170| 435.857| 127,827|
| |Union County|    17| 439.481|  3.693|   472| 12202.058| 162.497|  38,682|
| |Yell County|    14| 656.014|  0.000| 1,062| 49763.366| 388.253|  21,341|
| |Mississippi County|    13| 319.795| 14.057|   958| 23566.456| 987.500|  40,651|
| |Craighead County|    12| 108.763|  1.295| 1,318| 11945.764| 297.802| 110,332|
| |Hot Spring County|    11| 325.723| 12.691| 1,496| 44298.363| 253.810|  33,771|
| |Lincoln County|    11| 844.595|  0.000| 1,209| 92828.624| 482.625|  13,024|
| |Pope County|    10| 156.074|  2.230| 1,282| 20008.740| 269.786|  64,072|
| |Sevier County|    10| 587.993|  0.000|   976| 57388.134| 394.795|  17,007|
| |Lawrence County|     9| 548.580|  0.000|   206| 12556.382| 235.106|  16,406|
| |Nevada County|     9| 1090.645|  0.000|   137| 16602.036| 138.495|   8,252|
| |Garland County|     9| 90.556|  2.875|   964|  9699.555| 215.610|  99,386|
| |Lee County|     8| 903.240| 32.259|   893| 100824.207| 177.422|   8,857|
| |Columbia County|     8| 341.050| 12.180|   212|  9037.814| 170.525|  23,457|
| |Chicot County|     8| 790.670| 28.238|   718| 70962.641| 2993.251|  10,118|
| |Carroll County|     7| 246.653|  5.034|   350| 12332.629| 95.641|  28,380|
| |Phillips County|     7| 393.657|  8.034|   303| 17039.703| 265.116|  17,782|
| |Faulkner County|     6| 47.616|  1.134| 1,278| 10142.294| 116.774| 126,007|
| |Saline County|     6| 49.005|  2.334|   999|  8159.298| 168.016| 122,437|
| |Newton County|     6| 773.894| 55.278|   104| 13414.162| 239.539|   7,753|
| |Miller County|     5| 115.588|  3.303|   499| 11535.705| 158.521|  43,257|
| |Cleburne County|     5| 200.650|  0.000|   194|  7785.224| 91.726|  24,919|
| |Sharp County|     5| 286.664|  0.000|   109|  6249.283| 81.904|  17,442|
| |Ashley County|     5| 254.362|  7.267|   304| 15465.229| 537.795|  19,657|
| |Clay County|     4| 274.895|  0.000|   127|  8727.922| 245.442|  14,551|
| |Randolph County|     3| 167.056|  7.955|   206| 11471.211| 334.113|  17,958|
| |St. Francis County|     3| 120.029|  0.000| 1,186| 47451.388| 422.959|  24,994|
| |Poinsett County|     3| 127.508|  0.000|   240| 10200.612| 540.390|  23,528|
| |Howard County|     3| 227.238| 10.821|   327| 24768.974| 389.551|  13,202|
| |Drew County|     3| 164.663|  7.841|   186| 10209.122| 243.074|  18,219|
| |Conway County|     3| 143.913|  0.000|   147|  7051.713| 89.089|  20,846|
| |Cross County|     3| 182.715| 17.401|   190| 11571.959| 287.124|  16,419|
| |Crawford County|     3| 47.426|  0.000|   597|  9437.691| 187.444|  63,257|
| |Bradley County|     3| 278.733|  0.000|   179| 16631.051| 544.192|  10,763|
| |Franklin County|     2| 112.899|  0.000|   123|  6943.268| 153.220|  17,715|
| |White County|     2| 25.396|  0.000|   312|  3961.754| 112.467|  78,753|
| |Cleveland County|     2| 251.383| 17.956|    93| 11689.291| 538.677|   7,956|
| |Desha County|     2| 176.041|  0.000|   187| 16459.819| 565.846|  11,361|
| |Johnson County|     2| 75.250| 10.750|   662| 24907.818| 268.751|  26,578|
| |Lafayette County|     2| 301.932|  0.000|    52|  7850.242| 86.266|   6,624|
| |Lonoke County|     2| 27.282|  0.000|   495|  6752.241| 175.383|  73,309|
| |Madison County|     2| 120.656|  8.618|   269| 16228.282| 137.893|  16,576|
| |Ouachita County|     2| 85.536|  6.110|    92|  3934.651| 103.865|  23,382|
| |Van Buren County|     2| 120.882|  0.000|    52|  3142.943| 17.269|  16,545|
| |Hempstead County|     2| 92.885|  0.000|   233| 10821.103| 218.943|  21,532|
| |Clark County|     1| 44.803|  6.400|   177|  7930.108| 160.010|  22,320|
| |Greene County|     1| 22.063|  0.000|   459| 10126.862| 523.205|  45,325|
| |Independence County|     1| 26.438|  3.777|   483| 12769.332| 574.072|  37,825|
| |Little River County|     1| 81.573|  0.000|   168| 13704.217| 221.412|  12,259|
| |Logan County|     1| 46.585|  6.655|   233| 10854.374| 625.574|  21,466|
| |Montgomery County|     1| 111.284| 15.898|    34|  3783.663| 143.080|   8,986|
| |Pike County|     1| 93.301|  0.000|    97|  9050.196| 266.574|  10,718|
| |Jackson County|     1| 59.812|  0.000|    77|  4605.539| 170.892|  16,719|
| |Polk County|     1| 50.090|  0.000|   140|  7012.623| 107.336|  19,964|
| |Izard County|     1| 73.373|  0.000|    50|  3668.648| 73.373|  13,629|
| |Stone County|     1| 79.962|  0.000|    64|  5117.544| 137.077|  12,506|
| |Arkansas County|     1| 57.189|  0.000|   210| 12009.608| 171.566|  17,486|
| |Boone County|     1| 26.715|  0.000|   201|  5369.737| 167.924|  37,432|
| |Baxter County|     0|  0.000|  0.000|    69|  1645.521| 23.848|  41,932|
| |Prairie County|     0|  0.000|  0.000|    87| 10791.367| 496.155|   8,062|
| |Scott County|     0|  0.000|  0.000|    55|  5349.674| 194.534|  10,281|
| |Searcy County|     0|  0.000|  0.000|    28|  3552.849| 54.380|   7,881|
| |Woodruff County|     0|  0.000|  0.000|    21|  3322.785| 67.812|   6,320|
| |Fulton County|     0|  0.000|  0.000|    35|  2805.161| 91.597|  12,477|
| |Grant County|     0|  0.000|  0.000|   133|  7281.686| 70.392|  18,265|
| |Dallas County|     0|  0.000|  0.000|    61|  8703.096| 101.910|   7,009|
| |Perry County|     0|  0.000|  0.000|    50|  4782.401| 13.664|  10,455|
| |Calhoun County|     0|  0.000|  0.000|    15|  2890.730| 82.592|   5,189|
| |Marion County|     0|  0.000|  0.000|    25|  1497.544| 17.115|  16,694|
| |Monroe County|     0|  0.000|  0.000|    58|  8655.425| 191.869|   6,701|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,776|  4983.412| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.685| 3,824|  9169.714| 27.748| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,678|  5416.940| 24.903| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   463|  3058.306|  5.662| 151,391|
| |Strafford County|    13| 99.515|  0.000|   348|  2663.952| 25.152| 130,633|
| |Belknap County|     4| 65.250|  0.000|   115|  1875.928| 25.634|  61,303|
| |Cheshire County|     3| 39.430|  1.878|    96|  1261.747| 20.654|  76,085|
| |Sullivan County|     1| 23.177|  0.000|    40|   927.085|  3.311|  43,146|
| |Carroll County|     1| 20.446|  0.000|    93|  1901.452| 20.446|  48,910|
| |Grafton County|     1| 11.125|  0.000|   103|  1145.896|  0.000|  89,886|
| |Coos County|     0|  0.000|  0.000|    16|   506.923|  0.000|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   378| 129.749| N/A|30,137| 10344.577| N/A|2,913,314|
| |Johnson County|   102| 169.322|  0.949| 5,522|  9166.651| 151.536| 602,401|
| |Wyandotte County|    99| 598.444|  3.454| 4,810| 29075.918| 377.374| 165,429|
| |Sedgwick County|    44| 85.264|  1.384| 4,716|  9138.791| 178.280| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,509|  8531.449| 96.921| 176,875|
| |Lyon County|    13| 391.625|  8.607|   697| 20997.138| 228.089|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,783| 48893.520| 180.202|  36,467|
| |Coffey County|     8| 978.115|  0.000|    67|  8191.710| 34.933|   8,179|
| |Ford County|     8| 237.961|  0.000| 2,069| 61542.580| 182.720|  33,619|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 109.176|   5,234|
| |Leavenworth County|     8| 97.850|  0.000| 1,459| 17845.348| 117.070|  81,758|
| |Montgomery County|     5| 157.089|  0.000|   164|  5152.534| 53.859|  31,829|
| |Douglas County|     5| 40.897|  2.337|   714|  5840.061| 74.783| 122,259|
| |Riley County|     5| 67.356|  0.000|   477|  6425.800| 53.885|  74,232|
| |Saline County|     5| 92.210|  0.000|   372|  6860.431| 84.306|  54,224|
| |Seward County|     4| 186.672|  0.000| 1,220| 56934.852| 213.339|  21,428|
| |Barton County|     3| 116.374|  0.000|   133|  5159.238| 132.999|  25,779|
| |Sumner County|     3| 131.372|  0.000|    99|  4335.260| 12.512|  22,836|
| |Grant County|     2| 279.720|  0.000|   106| 14825.175| 279.720|   7,150|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Geary County|     2| 63.151|  0.000|   135|  4262.709| 31.576|  31,670|
| |Bourbon County|     2| 137.608|  9.829|    73|  5022.705| 78.633|  14,534|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 53.558|   8,002|
| |Cowley County|     2| 57.293|  0.000|   165|  4726.710| 57.293|  34,908|
| |Kearny County|     1| 260.552|  0.000|    59| 15372.590| 74.444|   3,838|
| |Franklin County|     1| 39.148|  0.000|   178|  6968.368| 162.185|  25,544|
| |Jackson County|     1| 75.924|  0.000|   146| 11084.959| 21.693|  13,171|
| |Harvey County|     1| 29.045|  0.000|   194|  5634.785| 153.525|  34,429|
| |Dickinson County|     1| 54.154|  0.000|    47|  2545.218| 54.154|  18,466|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199| 71.644|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   101|  5065.450| 200.612|  19,939|
| |Butler County|     1| 14.945|  2.135|   255|  3811.033| 117.427|  66,911|
| |Crawford County|     1| 25.761|  0.000|   380|  9789.273| 44.162|  38,818|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stanton County|     1| 498.504|  0.000|    18|  8973.081| 142.430|   2,006|
| |Stafford County|     1| 240.616| 34.374|     3|   721.848|  0.000|   4,156|
| |McPherson County|     1| 35.036|  0.000|   142|  4975.124| 65.067|  28,542|
| |Ellis County|     1| 35.023|  0.000|   141|  4938.185| 65.042|  28,553|
| |Reno County|     1| 16.130|  0.000|   267|  4306.591| 122.124|  61,998|
| |Nemaha County|     1| 97.742| 13.963|    49|  4789.366| 27.926|  10,231|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044|  0.000|  11,884|
| |Pratt County|     0|  0.000|  0.000|    33|  3601.048|  0.000|   9,164|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818| 51.948|   2,750|
| |Morris County|     0|  0.000|  0.000|    11|  1957.295| 50.839|   5,620|
| |Mitchell County|     0|  0.000|  0.000|    27|  4515.805|  0.000|   5,979|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683| 67.417|   2,119|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 50.272|   8,525|
| |Neosho County|     0|  0.000|  0.000|    58|  3623.415| 71.397|  16,007|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244| 26.647|   5,361|
| |Wabaunsee County|     0|  0.000|  0.000|    42|  6059.732| 61.834|   6,931|
| |Osage County|     0|  0.000|  0.000|    40|  2507.994| 17.914|  15,949|
| |Thomas County|     0|  0.000|  0.000|    36|  4629.034| 73.477|   7,777|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 78.135|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    15|  2535.068| 24.144|   5,917|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Scott County|     0|  0.000|  0.000|    34|  7049.554| 177.720|   4,823|
| |Russell County|     0|  0.000|  0.000|    13|  1896.149| 62.510|   6,856|
| |Rush County|     0|  0.000|  0.000|     6|  1976.285| 47.054|   3,036|
| |Rooks County|     0|  0.000|  0.000|    17|  3455.285| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    37|  3879.627| 149.793|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502| 154.074|   4,636|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Pottawatomie County|     0|  0.000|  0.000|   107|  4388.303| 29.294|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     7|  1091.363|  0.000|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    34|  5960.729| 100.180|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 75.188|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Marshall County|     0|  0.000|  0.000|     9|   927.166|  0.000|   9,707|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Allen County|     0|  0.000|  0.000|    15|  1212.709| 11.550|  12,369|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Anderson County|     0|  0.000|  0.000|    29|  3690.506| 36.360|   7,858|
| |Woodson County|     0|  0.000|  0.000|    11|  3505.417|  0.000|   3,138|
| |Miami County|     0|  0.000|  0.000|   133|  3884.686| 66.762|  34,237|
| |Meade County|     0|  0.000|  0.000|    44| 10909.993| 177.110|   4,033|
| |Comanche County|     0|  0.000|  0.000|     5|  2941.176| 168.067|   1,700|
| |Cloud County|     0|  0.000|  0.000|    32|  3642.158| 48.779|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     3|  1129.093| 53.766|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     5|  1538.462|  0.000|   3,250|
| |Chase County|     0|  0.000|  0.000|    42| 15861.027| 1942.167|   2,648|
| |Brown County|     0|  0.000|  0.000|    37|  3868.674| 74.685|   9,564|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Atchison County|     0|  0.000|  0.000|    64|  3981.833| 26.664|  16,073|
| |Linn County|     0|  0.000|  0.000|    35|  3607.132| 73.615|   9,703|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Labette County|     0|  0.000|  0.000|   133|  6779.488| 189.330|  19,618|
| |Kiowa County|     0|  0.000|  0.000|     7|  2828.283| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    17|  2376.957| 159.795|   7,152|
| |Jewell County|     0|  0.000|  0.000|    11|  3820.771| 99.241|   2,879|
| |Jefferson County|     0|  0.000|  0.000|    76|  3990.968| 127.531|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Harper County|     0|  0.000|  0.000|    10|  1839.588| 52.560|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    37| 14572.666|  0.000|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    20|  3343.363| 119.406|   5,982|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Gray County|     0|  0.000|  0.000|    77| 12859.051| 143.143|   5,988|
| |Graham County|     0|  0.000|  0.000|    16|  6446.414|  0.000|   2,482|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176| 162.584|   2,636|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495| 70.235|   6,102|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   348| 82.509| N/A|20,635|  4892.434| N/A|4,217,737|
| |Multnomah County|    93| 114.412|  0.176| 4,762|  5858.363| 75.044| 812,855|
| |Marion County|    69| 198.380|  0.821| 2,837|  8156.565| 107.610| 347,818|
| |Clackamas County|    39| 93.260|  1.025| 1,500|  3586.912| 47.484| 418,187|
| |Umatilla County|    27| 346.376|  7.331| 2,221| 28492.623| 509.484|  77,950|
| |Washington County|    24| 39.894|  0.475| 2,991|  4971.808| 59.604| 601,592|
| |Yamhill County|    13| 121.382|  4.002|   429|  4005.602| 124.050| 107,100|
| |Malheur County|    13| 425.240| 18.692|   755| 24696.608| 509.353|  30,571|
| |Polk County|    12| 139.397|  0.000|   308|  3577.859| 43.147|  86,085|
| |Linn County|    10| 77.072|  0.000|   271|  2088.648| 36.334| 129,749|
| |Lincoln County|     9| 180.137|  0.000|   412|  8246.267| 60.046|  49,962|
| |Deschutes County|     9| 45.525|  1.445|   582|  2943.973| 46.971| 197,692|
| |Benton County|     6| 64.479|  0.000|   164|  1762.436| 19.958|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   346| 14031.957| 272.296|  24,658|
| |Lane County|     3|  7.852|  0.000|   565|  1478.798| 23.930| 382,067|
| |Wasco County|     3| 112.435|  0.000|   181|  6783.599| 144.560|  26,682|
| |Morrow County|     3| 258.554| 12.312|   349| 30078.428| 738.725|  11,603|
| |Union County|     2| 74.530|  0.000|   394| 14682.318| 31.941|  26,835|
| |Josephine County|     2| 22.861|  1.633|   113|  1291.620| 24.493|  87,487|
| |Klamath County|     2| 29.309|  2.094|   201|  2945.573| 14.655|  68,238|
| |Jackson County|     2|  9.052|  0.647|   447|  2023.137| 61.425| 220,944|
| |Crook County|     1| 40.977|  0.000|    43|  1762.006|  5.854|  24,404|
| |Wallowa County|     1| 138.735|  0.000|    19|  2635.960|  0.000|   7,208|
| |Douglas County|     1|  9.011|  0.000|   148|  1333.574| 29.606| 110,980|
| |Curry County|     0|  0.000|  0.000|    14|   610.687|  0.000|  22,925|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Harney County|     0|  0.000|  0.000|    10|  1352.631| 38.647|   7,393|
| |Hood River County|     0|  0.000|  0.000|   181|  7740.997| 97.755|  23,382|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Coos County|     0|  0.000|  0.000|    90|  1395.630| 13.292|  64,487|
| |Columbia County|     0|  0.000|  0.000|    91|  1738.167| 49.116|  52,354|
| |Clatsop County|     0|  0.000|  0.000|    84|  2088.305| 39.067|  40,224|
| |Baker County|     0|  0.000|  0.000|    38|  2356.735| 88.599|  16,124|
| |Sherman County|     0|  0.000|  0.000|    15|  8426.966| 481.541|   1,780|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582| 52.840|  27,036|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   345| 178.349| N/A|27,962| 14455.068| N/A|1,934,408|
| |Douglas County|   132| 231.041|  0.250|11,139| 19496.716| 224.540| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,738| 28327.873| 69.853|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,922| 95975.232| 149.805|  20,026|
| |Lancaster County|    17| 53.277|  0.895| 3,253| 10194.616| 100.733| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    99| 10617.761| 45.964|   9,324|
| |Adams County|    11| 350.732|  0.000|   353| 11255.301| 63.769|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,220| 11859.228| 184.680| 187,196|
| |Dawson County|     9| 381.437|  0.000|   956| 40517.059| 84.764|  23,595|
| |Dodge County|     9| 246.137|  3.907|   791| 21632.709| 140.650|  36,565|
| |Perkins County|     7| 2421.308| 296.487|    19|  6572.120| 197.658|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   298|  8366.556| 56.151|  35,618|
| |Madison County|     5| 142.454|  0.000|   445| 12678.424| 126.174|  35,099|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747|  0.000|   6,445|
| |Gage County|     4| 185.934|  0.000|    89|  4137.033| 53.124|  21,513|
| |Custer County|     4| 371.161|  0.000|    44|  4082.769| 13.256|  10,777|
| |Colfax County|     4| 373.518|  0.000|   700| 65365.580| 106.719|  10,709|
| |Thurston County|     4| 553.710|  0.000|   205| 28377.630| 98.877|   7,224|
| |Platte County|     3| 89.633|  0.000|   784| 23423.962| 76.828|  33,470|
| |Cass County|     2| 76.196|  5.443|   172|  6552.880| 97.967|  26,248|
| |Lincoln County|     2| 57.284|  0.000|    99|  2835.539| 16.367|  34,914|
| |Saunders County|     2| 92.687|  0.000|   153|  7090.555| 165.512|  21,578|
| |Saline County|     2| 140.607|  0.000|   595| 41830.709| 140.607|  14,224|
| |Dixon County|     2| 354.862|  0.000|    58| 10290.987| 50.695|   5,636|
| |Buffalo County|     1| 20.137|  0.000|   401|  8075.072| 207.127|  49,659|
| |Richardson County|     1| 127.146|  0.000|    21|  2670.057| 18.164|   7,865|
| |Seward County|     1| 57.857|  0.000|   116|  6711.409| 181.836|  17,284|
| |Fillmore County|     1| 183.083|  0.000|    24|  4393.995| 52.309|   5,462|
| |Antelope County|     1| 158.781|  0.000|    19|  3016.831| 22.683|   6,298|
| |Washington County|     1| 48.242|  0.000|   117|  5644.266| 110.267|  20,729|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Chase County|     0|  0.000|  0.000|     6|  1529.052|  0.000|   3,924|
| |Cuming County|     0|  0.000|  0.000|    67|  7574.045| 161.493|   8,846|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 69.091|   6,203|
| |Cedar County|     0|  0.000|  0.000|    22|  2618.424| 17.003|   8,402|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Butler County|     0|  0.000|  0.000|    60|  7485.030| 71.286|   8,016|
| |Burt County|     0|  0.000|  0.000|    31|  4799.505| 265.410|   6,459|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Boyd County|     0|  0.000|  0.000|     4|  2084.419| 223.331|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    11|  1020.124| 13.248|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832| 27.515|   5,192|
| |Banner County|     0|  0.000|  0.000|     3|  4026.846| 191.755|     745|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827| 79.631|   1,794|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 33.265|   8,589|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Franklin County|     0|  0.000|  0.000|    12|  4028.197| 143.864|   2,979|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739| 287.150|   1,990|
| |Garfield County|     0|  0.000|  0.000|     3|  1523.616|  0.000|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317| 109.343|   2,613|
| |Otoe County|     0|  0.000|  0.000|    45|  2810.392| 26.766|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    28|  4016.064| 184.411|   6,972|
| |Nance County|     0|  0.000|  0.000|     8|  2273.373|  0.000|   3,519|
| |Morrill County|     0|  0.000|  0.000|    58| 12494.614|  0.000|   4,642|
| |Merrick County|     0|  0.000|  0.000|    61|  7865.893| 257.898|   7,755|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Polk County|     0|  0.000|  0.000|    26|  4987.531| 54.808|   5,213|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    34|  4080.653| 68.582|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    20|  2489.420| 35.563|   8,034|
| |Kearney County|     0|  0.000|  0.000|    50|  7698.229| 483.889|   6,495|
| |Johnson County|     0|  0.000|  0.000|    13|  2563.597| 56.343|   5,071|
| |Jefferson County|     0|  0.000|  0.000|    15|  2128.867| 20.275|   7,046|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Phelps County|     0|  0.000|  0.000|    37|  4095.639| 47.440|   9,034|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 85.144|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     2|   724.113| 51.722|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Pierce County|     0|  0.000|  0.000|    20|  2797.985| 59.957|   7,148|
| |Thayer County|     0|  0.000|  0.000|    26|  5196.882| 28.554|   5,003|
| |Stanton County|     0|  0.000|  0.000|    29|  4898.649| 72.394|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Sherman County|     0|  0.000|  0.000|    11|  3665.445| 190.413|   3,001|
| |Sheridan County|     0|  0.000|  0.000|    10|  1906.214| 27.232|   5,246|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759| 105.274|   1,357|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Thomas County|     0|  0.000|  0.000|     1|  1385.042|  0.000|     722|
| |Valley County|     0|  0.000|  0.000|    10|  2405.002|  0.000|   4,158|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 121.271|   2,356|
| |York County|     0|  0.000|  0.000|    78|  5702.171| 93.992|  13,679|
| |Red Willow County|     0|  0.000|  0.000|    17|  1585.229| 26.643|  10,724|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|     783|
| |Webster County|     0|  0.000|  0.000|     9|  2581.015|  0.000|   3,487|
| |Wayne County|     0|  0.000|  0.000|    37|  3942.461| 30.444|   9,385|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   277| 86.402| N/A|34,464| 10749.985| N/A|3,205,958|
| |Salt Lake County|   189| 162.870|  1.970|20,287| 17482.207| 154.006|1,160,437|
| |Utah County|    37| 58.155|  0.898| 8,536| 13416.426| 190.406| 636,235|
| |San Juan County|    25| 1633.133| 18.664|   648| 42330.807| 326.627|  15,308|
| |Davis County|    21| 59.075|  3.215| 3,156|  8878.112| 99.262| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   552| 16191.957| 113.143|  34,091|
| |Summit County|     1| 23.728|  0.000|   706| 16751.691| 64.404|  42,145|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Tooele County|     0|  0.000|  0.000|   579|  8012.843| 102.805|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   229| 128.143| N/A|23,920| 13385.076| N/A|1,787,065|
| |Ada County|    76| 157.812|  4.746| 8,720| 18106.801| 264.601| 481,587|
| |Canyon County|    48| 208.833|  6.837| 5,620| 24450.835| 568.075| 229,849|
| |Twin Falls County|    32| 368.333|  1.644| 1,313| 15113.147| 187.455|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   145|  3588.398| 53.031|  40,408|
| |Kootenai County|    15| 90.527|  6.035| 1,764| 10645.938| 194.848| 165,697|
| |Jerome County|     6| 245.781|  0.000|   461| 18884.155| 275.040|  24,412|
| |Blaine County|     6| 260.632|  0.000|   575| 24977.195| 43.439|  23,021|
| |Bonneville County|     3| 25.197|  1.200|   958|  8046.228| 327.560| 119,062|
| |Elmore County|     3| 109.047|  0.000|   207|  7524.263| 51.927|  27,511|
| |Washington County|     3| 294.291| 14.014|   201| 19717.481| 252.249|  10,194|
| |Minidoka County|     2| 95.062|  0.000|   469| 22291.934| 339.506|  21,039|
| |Payette County|     2| 83.504|  0.000|   377| 15740.470| 322.086|  23,951|
| |Bingham County|     2| 42.725|  0.000|   236|  5041.550| 183.107|  46,811|
| |Bannock County|     2| 22.777|  0.000|   388|  4418.732| 141.543|  87,808|
| |Owyhee County|     2| 169.162| 24.166|   258| 21821.873| 374.573|  11,823|
| |Shoshone County|     2| 155.255| 11.090|    87|  6753.610| 221.793|  12,882|
| |Valley County|     1| 87.781|  0.000|    56|  4915.730| 125.401|  11,392|
| |Boise County|     1| 127.698|  0.000|    47|  6001.788| 164.183|   7,831|
| |Cassia County|     1| 41.615|  0.000|   513| 21348.315| 309.137|  24,030|
| |Jefferson County|     1| 33.477|  0.000|   185|  6193.298| 258.253|  29,871|
| |Gem County|     1| 55.212|  7.887|   174|  9606.890| 189.298|  18,112|
| |Gooding County|     1| 65.880|  0.000|   157| 10343.237| 244.699|  15,179|
| |Benewah County|     0|  0.000|  0.000|    63|  6775.651| 199.736|   9,298|
| |Bear Lake County|     0|  0.000|  0.000|    15|  2448.980| 209.913|   6,125|
| |Adams County|     0|  0.000|  0.000|    19|  4424.779| 33.269|   4,294|
| |Bonner County|     0|  0.000|  0.000|   178|  3891.646| 103.069|  45,739|
| |Franklin County|     0|  0.000|  0.000|    51|  3675.411| 41.181|  13,876|
| |Boundary County|     0|  0.000|  0.000|    36|  2939.976| 35.000|  12,245|
| |Custer County|     0|  0.000|  0.000|    10|  2317.497| 99.321|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    16|  1827.318| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|     8|  9467.456| 1183.432|     845|
| |Caribou County|     0|  0.000|  0.000|    31|  4332.635| 159.728|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Teton County|     0|  0.000|  0.000|    77|  6341.624| 235.311|  12,142|
| |Fremont County|     0|  0.000|  0.000|    77|  5878.311| 348.991|  13,099|
| |Madison County|     0|  0.000|  0.000|   156|  3909.089| 89.494|  39,907|
| |Lincoln County|     0|  0.000|  0.000|    56| 10436.079| 159.736|   5,366|
| |Lewis County|     0|  0.000|  0.000|     1|   260.552|  0.000|   3,838|
| |Lemhi County|     0|  0.000|  0.000|    16|  1993.273| 71.188|   8,027|
| |Power County|     0|  0.000|  0.000|    55|  7160.526| 260.383|   7,681|
| |Oneida County|     0|  0.000|  0.000|    13|  2869.124| 157.644|   4,531|
| |Latah County|     0|  0.000|  0.000|    99|  2468.335| 74.798|  40,108|
| |Idaho County|     0|  0.000|  0.000|    31|  1859.963| 17.143|  16,667|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   144| 162.775| N/A| 9,371| 10592.782| N/A| 884,659|
| |Minnehaha County|    67| 346.909|  2.959| 4,349| 22518.044| 147.196| 193,134|
| |Pennington County|    31| 272.468|  5.022|   875|  7690.617| 80.359| 113,775|
| |Beadle County|     9| 487.726|  0.000|   587| 31810.546|  7.742|  18,453|
| |Todd County|     5| 491.304| 14.037|    68|  6681.733| 28.075|  10,177|
| |Union County|     4| 251.067|  8.967|   209| 13118.253| 161.400|  15,932|
| |Brown County|     3| 77.242|  0.000|   428| 11019.851| 114.024|  38,839|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556| 218.436|   1,962|
| |Hughes County|     2| 114.116|  0.000|    88|  5021.111| 40.756|  17,526|
| |Lake County|     2| 156.287|  0.000|    90|  7032.898| 133.960|  12,797|
| |Lincoln County|     2| 32.718|  0.000|   609|  9962.701| 156.580|  61,128|
| |Yankton County|     2| 87.665|  0.000|   110|  4821.601| 56.356|  22,814|
| |Oglala Lakota County|     2| 141.074| 10.077|   153| 10792.128| 120.920|  14,177|
| |Lyman County|     2| 528.961|  0.000|    88| 23274.266| 37.783|   3,781|
| |Brookings County|     1| 28.509|  4.073|   128|  3649.115| 61.090|  35,077|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474| 128.161|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |McCook County|     1| 179.019|  0.000|    26|  4654.493| 51.148|   5,586|
| |Meade County|     1| 35.296|  0.000|    87|  3070.733| 80.676|  28,332|
| |Roberts County|     1| 96.209|  0.000|    75|  7215.701| 82.465|  10,394|
| |Butte County|     1| 95.886|  0.000|    14|  1342.411| 54.792|  10,429|
| |Codington County|     1| 35.703|  5.100|   129|  4605.662| 61.205|  28,009|
| |Faulk County|     1| 434.972|  0.000|    26| 11309.265|  0.000|   2,299|
| |Davison County|     1| 50.569|  7.224|    94|  4753.477| 57.793|  19,775|
| |Lawrence County|     0|  0.000|  0.000|    46|  1779.910| 110.553|  25,844|
| |Spink County|     0|  0.000|  0.000|    24|  3764.115| 112.027|   6,376|
| |Hyde County|     0|  0.000|  0.000|     3|  2305.919|  0.000|   1,301|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582| 57.849|   4,939|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 120.098|   2,379|
| |Marshall County|     0|  0.000|  0.000|     8|  1621.074|  0.000|   4,935|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953| 64.466|   2,216|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Sully County|     0|  0.000|  0.000|     2|  1437.815| 102.701|   1,391|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Turner County|     0|  0.000|  0.000|    50|  5963.740| 102.236|   8,384|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668| 41.372|   3,453|
| |Charles Mix County|     0|  0.000|  0.000|   101| 10869.565| 30.748|   9,292|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159| 51.929|   2,751|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061| 42.454|   3,365|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Brule County|     0|  0.000|  0.000|    45|  8495.375| 134.847|   5,297|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233| 103.821|   1,376|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Clay County|     0|  0.000|  0.000|   124|  8813.077| 111.686|  14,070|
| |Corson County|     0|  0.000|  0.000|    32|  7831.620| 209.776|   4,086|
| |Custer County|     0|  0.000|  0.000|    29|  3232.278| 175.148|   8,972|
| |Day County|     0|  0.000|  0.000|    21|  3871.681|  0.000|   5,424|
| |Deuel County|     0|  0.000|  0.000|    10|  2298.322| 32.833|   4,351|
| |Dewey County|     0|  0.000|  0.000|    50|  8486.083|  0.000|   5,892|
| |Douglas County|     0|  0.000|  0.000|    17|  5819.925| 48.907|   2,921|
| |Edmunds County|     0|  0.000|  0.000|    14|  3656.307| 37.309|   3,829|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 170.245|   6,713|
| |Grant County|     0|  0.000|  0.000|    24|  3403.290| 121.546|   7,052|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186| 75.228|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    17|  2757.949| 69.528|   6,164|
| |Hand County|     0|  0.000|  0.000|     7|  2193.670|  0.000|   3,191|
| |Ziebach County|     0|  0.000|  0.000|    33| 11973.875| 1295.874|   2,756|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Hutchinson County|     0|  0.000|  0.000|    27|  3703.196| 19.594|   7,291|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   127| 70.865| N/A| 7,452|  4158.141| N/A|1,792,147|
| |Kanawha County|    22| 123.509|  1.604|   898|  5041.432| 87.419| 178,124|
| |Jackson County|    19| 664.894|  0.000|   162|  5669.093| 24.996|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   686|  5756.434| 52.745| 119,171|
| |Wayne County|     9| 228.415|  0.000|   200|  5075.884| 76.138|  39,402|
| |Mingo County|     5| 213.456| 18.296|   158|  6745.219| 250.049|  23,424|
| |Fayette County|     5| 117.908|  0.000|   140|  3301.420| 50.532|  42,406|
| |Wood County|     5| 59.867|  1.710|   243|  2909.552| 20.526|  83,518|
| |Monongalia County|     5| 47.343|  0.000|   935|  8853.161| 67.633| 105,612|
| |Jefferson County|     4| 69.996|  0.000|   294|  5144.717| 17.499|  57,146|
| |Mineral County|     4| 148.876|  0.000|   117|  4354.623| 53.170|  26,868|
| |Preston County|     4| 119.646|  4.273|   123|  3679.110|  0.000|  33,432|
| |Ohio County|     4| 96.593|  0.000|   266|  6423.414| 68.995|  41,411|
| |Greenbrier County|     3| 86.550|  0.000|    91|  2625.353| 24.729|  34,662|
| |Logan County|     3| 93.694|  0.000|   209|  6527.374| 348.008|  32,019|
| |Mercer County|     3| 51.057|  0.000|   177|  3012.356| 99.682|  58,758|
| |Cabell County|     2| 21.752|  0.000|   373|  4056.773| 94.777|  91,945|
| |Marion County|     2| 35.668|  0.000|   183|  3263.661| 33.121|  56,072|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097| 26.942|  15,907|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Harrison County|     1| 14.869|  0.000|   214|  3181.872| 74.343|  67,256|
| |Marshall County|     1| 32.754|  4.679|   130|  4257.967| 37.433|  30,531|
| |Mason County|     1| 37.713|  0.000|    54|  2036.506| 48.488|  26,516|
| |Wyoming County|     1| 49.034|  0.000|    31|  1520.055| 70.049|  20,394|
| |Pendleton County|     1| 143.493|  0.000|    58|  8322.571| 430.478|   6,969|
| |Nicholas County|     1| 40.823|  0.000|    36|  1469.628| 23.327|  24,496|
| |Brooke County|     1| 45.581|  0.000|    62|  2826.018| 13.023|  21,939|
| |Grant County|     1| 86.445| 12.349|   117| 10114.108| 617.467|  11,568|
| |Hampshire County|     1| 43.150|  0.000|    76|  3279.396| 30.821|  23,175|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656| 16.791|   8,508|
| |Taylor County|     1| 59.898|  8.557|    56|  3354.298| 34.228|  16,695|
| |Roane County|     1| 73.057|  0.000|    15|  1095.850| 10.437|  13,688|
| |Pleasants County|     1| 134.048| 19.150|    12|  1608.579| 95.749|   7,460|
| |Raleigh County|     1| 13.631|  0.000|   215|  2930.713| 99.313|  73,361|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Wirt County|     0|  0.000|  0.000|     6|  1030.751|  0.000|   5,821|
| |Wetzel County|     0|  0.000|  0.000|    42|  2787.919|  9.483|  15,065|
| |Lincoln County|     0|  0.000|  0.000|    81|  3968.837| 153.994|  20,409|
| |Hardy County|     0|  0.000|  0.000|    58|  4210.221| 41.480|  13,776|
| |Hancock County|     0|  0.000|  0.000|   109|  3783.409| 64.462|  28,810|
| |Morgan County|     0|  0.000|  0.000|    26|  1453.813|  0.000|  17,884|
| |Tyler County|     0|  0.000|  0.000|    13|  1513.212| 16.629|   8,591|
| |Tucker County|     0|  0.000|  0.000|    11|  1608.422| 41.777|   6,839|
| |Summers County|     0|  0.000|  0.000|     7|   556.749|  0.000|  12,573|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Randolph County|     0|  0.000|  0.000|   208|  7248.650|  4.978|  28,695|
| |Putnam County|     0|  0.000|  0.000|   186|  3294.951| 70.859|  56,450|
| |Pocahontas County|     0|  0.000|  0.000|    41|  4971.505|  0.000|   8,247|
| |McDowell County|     0|  0.000|  0.000|    58|  3290.967| 259.387|  17,624|
| |Upshur County|     0|  0.000|  0.000|    39|  1613.170|  5.909|  24,176|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Boone County|     0|  0.000|  0.000|    97|  4520.669| 146.472|  21,457|
| |Gilmer County|     0|  0.000|  0.000|    16|  2045.251|  0.000|   7,823|
| |Doddridge County|     0|  0.000|  0.000|     5|   591.856| 16.910|   8,448|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   124| 92.247| N/A| 4,014|  2986.136| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.484| 2,075|  7033.827| 17.433| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   668|  3217.091| 15.824| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   170|  1390.002|  7.008| 122,302|
| |Androscoggin County|     7| 64.649|  0.000|   558|  5153.449| 13.194| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   152|   999.027|  6.573| 152,148|
| |Lincoln County|     1| 28.873|  0.000|    34|   981.694|  4.125|  34,634|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Hancock County|     1| 18.186|  0.000|    35|   636.514| 20.784|  54,987|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  3.592|  39,772|
| |Oxford County|     0|  0.000|  0.000|    53|   914.187|  0.000|  57,975|
| |Piscataquis County|     0|  0.000|  0.000|     3|   178.731|  0.000|  16,785|
| |Sagadahoc County|     0|  0.000|  0.000|    54|  1506.024| 31.874|  35,856|
| |Washington County|     0|  0.000|  0.000|    12|   382.421| 22.763|  31,379|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   110| 144.345| N/A| 7,309|  9591.083| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,006| 16523.474| 85.594| 181,923|
| |Grand Forks County|     6| 86.392|  4.114|   662|  9531.900| 88.449|  69,451|
| |Burleigh County|     5| 52.287|  1.494| 1,108| 11586.807| 288.326|  95,626|
| |Stark County|     3| 95.271|  0.000|   248|  7875.766| 299.424|  31,489|
| |Morton County|     3| 95.651|  0.000|   333| 10617.268| 323.392|  31,364|
| |McIntosh County|     2| 800.961| 57.212|    27| 10812.976| 514.904|   2,497|
| |Benson County|     2| 292.740| 20.910|   132| 19320.843| 961.860|   6,832|
| |Stutsman County|     2| 96.600|  0.000|   126|  6085.781| 144.900|  20,704|
| |Williams County|     2| 53.207|  0.000|   263|  6996.728| 148.220|  37,589|
| |Ramsey County|     2| 173.626|  0.000|    66|  5729.664| 359.654|  11,519|
| |McKenzie County|     1| 66.560|  0.000|    86|  5724.175| 123.612|  15,024|
| |Ward County|     1| 14.784|  0.000|   209|  3089.842| 73.920|  67,641|
| |Sioux County|     1| 236.407| 33.772|    63| 14893.617| 202.634|   4,230|
| |Emmons County|     1| 308.547|  0.000|    17|  5245.295| 88.156|   3,241|
| |Griggs County|     1| 448.229| 64.033|    32| 14343.344| 448.229|   2,231|
| |McHenry County|     1| 174.064|  0.000|    16|  2785.030| 49.733|   5,745|
| |Mountrail County|     1| 94.832|  0.000|   123| 11664.296| 203.211|  10,545|
| |Kidder County|     0|  0.000|  0.000|    13|  5241.935| 115.207|   2,480|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Adams County|     0|  0.000|  0.000|     2|   902.527|  0.000|   2,216|
| |Golden Valley County|     0|  0.000|  0.000|     4|  2271.437|  0.000|   1,761|
| |Barnes County|     0|  0.000|  0.000|    37|  3552.568| 82.299|  10,415|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784| 231.660|   1,850|
| |McLean County|     0|  0.000|  0.000|    51|  5396.825| 241.875|   9,450|
| |Mercer County|     0|  0.000|  0.000|    26|  3175.766| 52.348|   8,187|
| |Nelson County|     0|  0.000|  0.000|    24|  8336.228| 545.824|   2,879|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252| 72.924|   1,959|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Pierce County|     0|  0.000|  0.000|    11|  2767.296|  0.000|   3,975|
| |Ransom County|     0|  0.000|  0.000|    27|  5174.396| 27.378|   5,218|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641|  0.000|   2,327|
| |Richland County|     0|  0.000|  0.000|   104|  6428.881| 150.125|  16,177|
| |Rolette County|     0|  0.000|  0.000|    52|  3668.172| 231.780|  14,176|
| |Sargent County|     0|  0.000|  0.000|    11|  2821.960| 109.946|   3,898|
| |Slope County|     0|  0.000|  0.000|     3|  4000.000|  0.000|     750|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Steele County|     0|  0.000|  0.000|    14|  7407.407| 302.343|   1,890|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Traill County|     0|  0.000|  0.000|    52|  6470.881| 195.549|   8,036|
| |Walsh County|     0|  0.000|  0.000|   103|  9679.541| 93.976|  10,641|
| |Wells County|     0|  0.000|  0.000|    21|  5477.308| 223.564|   3,834|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Bowman County|     0|  0.000|  0.000|     6|  1984.127|  0.000|   3,024|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704| 405.268|   2,115|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Dickey County|     0|  0.000|  0.000|    12|  2463.054| 29.322|   4,872|
| |Divide County|     0|  0.000|  0.000|     2|   883.392| 63.099|   2,264|
| |Dunn County|     0|  0.000|  0.000|    30|  6781.193| 64.583|   4,424|
| |Eddy County|     0|  0.000|  0.000|    15|  6558.811| 124.930|   2,287|
| |Foster County|     0|  0.000|  0.000|    27|  8411.215| 667.557|   3,210|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 70.616|   4,046|
| |Sheridan County|     0|  0.000|  0.000|     8|  6083.650| 325.910|   1,315|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    70| 65.495| N/A| 4,757|  4450.878| N/A|1,068,778|
| |Yellowstone County|    28| 173.590|  1.771| 1,212|  7513.949| 168.276| 161,300|
| |Big Horn County|    13| 976.049| 42.903|   407| 30557.850| 1018.953|  13,319|
| |Toole County|     6| 1266.892|  0.000|    42|  8868.243| 331.805|   4,736|
| |Cascade County|     3| 36.870|  1.756|   162|  1991.004| 45.649|  81,366|
| |Gallatin County|     3| 26.216|  1.248|   915|  7995.875| 82.393| 114,434|
| |Hill County|     2| 121.330| 17.333|    42|  2547.925| 17.333|  16,484|
| |Lincoln County|     2| 100.100|  0.000|    74|  3703.704| 42.900|  19,980|
| |Richland County|     2| 185.134| 13.224|    47|  4350.643| 26.448|  10,803|
| |Flathead County|     2| 19.267|  0.000|   322|  3101.940| 116.976| 103,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 112.762|  11,402|
| |Madison County|     1| 116.279|  0.000|    82|  9534.884| 149.502|   8,600|
| |Lewis and Clark County|     1| 14.403|  0.000|   152|  2189.192| 61.725|  69,432|
| |Glacier County|     1| 72.711|  0.000|    69|  5017.087| 166.198|  13,753|
| |Lake County|     1| 32.832|  0.000|   179|  5876.945| 65.664|  30,458|
| |Ravalli County|     1| 22.828|  0.000|    82|  1871.890| 55.439|  43,806|
| |Rosebud County|     1| 111.894|  0.000|    32|  3580.620| 159.849|   8,937|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972| 38.228|   3,737|
| |Valley County|     0|  0.000|  0.000|    15|  2028.123| 77.262|   7,396|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975| 294.855|     969|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Fergus County|     0|  0.000|  0.000|     9|   814.480| 38.785|  11,050|
| |McCone County|     0|  0.000|  0.000|     3|  1802.885| 171.703|   1,664|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Jefferson County|     0|  0.000|  0.000|    27|  2209.312| 58.447|  12,221|
| |Granite County|     0|  0.000|  0.000|    13|  3847.292| 295.946|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Deer Lodge County|     0|  0.000|  0.000|    25|  2735.230| 78.149|   9,140|
| |Dawson County|     0|  0.000|  0.000|    17|  1973.761| 49.759|   8,613|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Mineral County|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,397|
| |Missoula County|     0|  0.000|  0.000|   318|  2658.863| 84.806| 119,600|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Chouteau County|     0|  0.000|  0.000|     8|  1419.698| 50.704|   5,635|
| |Carbon County|     0|  0.000|  0.000|    67|  6247.086| 133.200|  10,725|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148| 84.531|   1,690|
| |Stillwater County|     0|  0.000|  0.000|    23|  2385.397| 74.081|   9,642|
| |Silver Bow County|     0|  0.000|  0.000|    85|  2434.484| 98.198|  34,915|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 86.345|   3,309|
| |Sanders County|     0|  0.000|  0.000|     9|   743.003|  0.000|  12,113|
| |Roosevelt County|     0|  0.000|  0.000|    21|  1908.397| 51.929|  11,004|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505| 132.644|   1,077|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 48.336|   5,911|
| |Phillips County|     0|  0.000|  0.000|    21|  5311.077| 758.725|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    55|  3312.056| 68.822|  16,606|
| |Broadwater County|     0|  0.000|  0.000|    11|  1763.668| 22.905|   6,237|
| |Blaine County|     0|  0.000|  0.000|    10|  1496.782| 64.148|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    61|  6452.978| 241.798|   9,453|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,440|  2307.733| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   724|  4420.726|  7.851| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  2.892|  49,402|
| |Windham County|     3| 71.053|  0.000|   102|  2415.802|  3.383|  42,222|
| |Washington County|     2| 34.241|  0.000|    53|   907.394| 14.675|  58,409|
| |Addison County|     2| 54.382|  0.000|    73|  1984.936|  7.769|  36,777|
| |Windsor County|     2| 36.323|  0.000|    72|  1307.617|  5.189|  55,062|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Bennington County|     1| 28.193|  0.000|    85|  2396.391|  8.055|  35,470|
| |Rutland County|     1| 17.185|  0.000|    99|  1701.294| 24.550|  58,191|
| |Orange County|     0|  0.000|  0.000|    14|   484.563|  0.000|  28,892|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|
| |Essex County|     0|  0.000|  0.000|     4|   649.035|  0.000|   6,163|
| |Caledonia County|     0|  0.000|  0.000|    26|   866.869|  0.000|  29,993|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    30| 21.188| N/A| 3,092|  2183.813| N/A|1,415,872|
| |Honolulu County|    24| 24.626| N/A| 2,741|  2812.543| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   181|  1081.133|  8.533| 167,417|
| |Kauai County|     0|  0.000|  0.000|    47|   650.132|  0.000|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   123|   610.382|  5.671| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,000|  5183.505| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    23|  2723.505| 16.916|   8,445|
| |Park County|     0|  0.000|  0.000|   132|  4521.477| 83.187|  29,194|
| |Big Horn County|     0|  0.000|  0.000|    36|  3053.435| 12.117|  11,790|
| |Fremont County|     0|  0.000|  0.000|   502| 12786.226| 123.714|  39,261|
| |Sweetwater County|     0|  0.000|  0.000|   257|  6069.480| 57.355|  42,343|
| |Sublette County|     0|  0.000|  0.000|    38|  3865.324| 58.125|   9,831|
| |Sheridan County|     0|  0.000|  0.000|    69|  2263.408| 51.548|  30,485|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Natrona County|     0|  0.000|  0.000|   229|  2867.590| 25.044|  79,858|
| |Lincoln County|     0|  0.000|  0.000|   100|  5042.864| 79.245|  19,830|
| |Teton County|     0|  0.000|  0.000|   371| 15811.456| 219.181|  23,464|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565| 18.837|   7,584|
| |Converse County|     0|  0.000|  0.000|    32|  2315.150| 20.671|  13,822|
| |Carbon County|     0|  0.000|  0.000|    95|  6418.919| 193.050|  14,800|
| |Campbell County|     0|  0.000|  0.000|   122|  2632.658| 21.579|  46,341|
| |Albany County|     0|  0.000|  0.000|    88|  2263.374| 14.697|  38,880|
| |Goshen County|     0|  0.000|  0.000|    26|  1968.057| 129.762|  13,211|
| |Hot Springs County|     0|  0.000|  0.000|    19|  4305.461| 32.372|   4,413|
| |Laramie County|     0|  0.000|  0.000|   496|  4984.925| 57.430|  99,500|
| |Washakie County|     0|  0.000|  0.000|    69|  8840.487| 384.369|   7,805|
| |Uinta County|     0|  0.000|  0.000|   274| 13546.920| 141.261|  20,226|
| |Weston County|     0|  0.000|  0.000|     5|   721.813|  0.000|   6,927|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|17,860| 16859.220| N/A|1,059,361|
| |Bristol County|     0|  0.000|  0.000|   316|  6518.286| 35.361|  48,479|
| |Newport County|     0|  0.000|  0.000|   396|  4824.444| 27.847|  82,082|
| |Providence County|     0|  0.000|  0.000|15,047| 23550.274| 111.347| 638,931|
| |Washington County|     0|  0.000|  0.000|   607|  4833.688| 19.339| 125,577|
| |Kent County|     0|  0.000|  0.000| 1,494|  9093.565| 63.476| 164,292|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|


