# Analysis of US By County #

Updated: at 2020-08-07

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 127,491 deaths (441.661 deaths/million) and 4,206,810 confirmed cases (14573.478 confirmed cases/million).  This group accounts for 80.92% of all US deaths and for 87.59% of all US cases.

24.81% of this group's deaths (20.08% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 24.67% of this group's deaths (19.97% of the total US deaths) occured in 32 counties in 14 states with a combined population of 36,389,189 (11.09% of the total US population):



The next 25.43% of this group's deaths (20.58% of the total US deaths) occured in 87 counties in 30 states with a combined population of 68,852,556 (20.98% of the total US population)

The remaining 25.08% of this group's deaths (20.30% of the total US deaths) occured in 858 counties in 50 states with a combined population of 146,133,096 (44.52% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,628 deaths (243.270 deaths/million) and 428,176 confirmed cases (10818.682 confirmed cases/million).  This group accounts for 6.11% of all US deaths and for 8.92% of all US cases.

24.95% of this group's deaths (1.52% of the total US deaths) occured in 57 counties in 16 states with a combined population of 1,883,834 (0.57% of the total US population):



The next 24.97% of this group's deaths (1.53% of the total US deaths) occured in 109 counties in 26 states with a combined population of 3,275,587 (1.00% of the total US population):



The next 25.04% of this group's deaths (1.53% of the total US deaths) occured in 227 counties in 33 states with a combined population of 5,607,796 (1.71% of the total US population)

The remaining 25.04% of this group's deaths (1.53% of the total US deaths) occured in 1,759 counties in 47 states with a combined population of 28,810,247 (8.78% of the total US population) 

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
|NJ|21 counties|15,849| 1784.357| N/A|183,059| 20609.669| N/A|8,882,190|
| |Essex County| 2,107| 2637.129|  1.252|19,644| 24586.501| 36.297| 798,975|
| |Bergen County| 2,037| 2185.149|  0.000|20,669| 22172.233| 39.384| 932,202|
| |Hudson County| 1,502| 2233.819|  0.637|19,580| 29119.961| 31.019| 672,391|
| |Middlesex County| 1,401| 1698.054|  0.000|17,821| 21599.589| 33.764| 825,062|
| |Union County| 1,348| 2422.974|  0.514|16,622| 29877.359| 42.625| 556,341|
| |Passaic County| 1,239| 2468.983|  0.000|17,585| 35042.027| 57.220| 501,826|
| |Ocean County| 1,016| 1673.293|  0.471|10,551| 17376.883| 45.879| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,227| 16527.283| 51.483| 618,795|
| |Morris County|   827| 1681.424|  0.000| 7,209| 14657.057| 29.045| 491,845|
| |Mercer County|   618| 1681.953|  2.333| 8,087| 22009.634| 33.826| 367,430|
| |Camden County|   578| 1141.230|  1.974| 8,464| 16711.717| 63.182| 506,471|
| |Somerset County|   562| 1708.549|  3.474| 5,217| 15860.325| 20.412| 328,934|
| |Burlington County|   471| 1057.598|  0.642| 5,927| 13308.664| 62.551| 445,349|
| |Atlantic County|   252| 955.740|  1.084| 3,442| 13054.197| 60.140| 263,670|
| |Gloucester County|   209| 716.647|  1.470| 3,193| 10948.580| 79.355| 291,636|
| |Sussex County|   197| 1402.255|  2.034| 1,320|  9395.820| 27.455| 140,488|
| |Warren County|   171| 1624.441|  1.357| 1,339| 12720.036| 17.642| 105,267|
| |Cumberland County|   158| 1056.665|  0.955| 3,309| 22129.783| 119.424| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,144|  9198.286| 21.824| 124,371|
| |Cape May County|    87| 945.251|  1.552|   823|  8941.862| 31.043|  92,039|
| |Salem County|    87| 1394.566|  9.160|   886| 14202.132| 43.509|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,316| 633.091| N/A|251,113| 12908.343| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,534| 32082.858| 39.585|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.193|43,630| 29547.589| 44.504|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.295|36,107| 37319.665| 28.645| 967,506|
| |Queens County|   983| 436.320|  0.758| 7,837|  3477.061| 17.238|2,253,858|
| |Kings County|   929| 363.051|  0.631| 1,345|   525.399|  2.605|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,918| 42720.902| 25.433| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,737|  9510.157| 47.116| 918,702|
| |Bronx County|   648| 457.149|  0.795|26,688| 18818.409| 93.297|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,127| 28905.804| 20.411| 384,940|
| |New York County|   414| 254.117|  0.442|15,392|  9450.606| 46.854|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 4,868|  6562.681| 36.785| 741,770|
| |Onondaga County|   200| 434.284|  1.861| 3,535|  7675.972| 23.575| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,582| 15573.486| 55.353| 294,218|
| |Richmond County|   148| 310.566|  0.540| 7,837| 16458.923| 81.599| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,565|  8395.907| 33.668| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,117|  9257.842| 34.360| 228,671|
| |Niagara County|    98| 468.270|  1.365| 1,470|  7024.049| 24.574| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,045| 11516.390| 28.157| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,094|  5743.144| 48.747| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,444| 14686.737| 37.778|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   297|  7360.230| 21.242|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,485| 19686.605| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   297|  3113.893| 10.484|  95,379|
| |Columbia County|    37| 622.257|  0.000|   534|  8980.676| 50.453|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,050|  6761.151| 29.436| 155,299|
| |Ontario County|    34| 309.719|  0.000|   355|  3233.829|  7.808| 109,777|
| |Warren County|    33| 516.077|  0.000|   304|  4754.160| 13.405|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   758|  4775.886| 36.004| 158,714|
| |Tioga County|    25| 518.640|  2.964|   193|  4003.900| 26.673|  48,203|
| |Fulton County|    24| 449.581|  0.000|   291|  5451.174| 42.817|  53,383|
| |Greene County|    18| 381.453|  0.000|   290|  6145.630|  9.082|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   747|  3249.762| 23.617| 229,863|
| |Madison County|    17| 239.636|  0.000|   409|  5765.354| 26.179|  70,941|
| |Washington County|    14| 228.743|  0.000|   256|  4182.733|  4.668|  61,204|
| |Chautauqua County|     9| 70.920| N/A|   244|  1922.728| N/A| 126,903|
| |Livingston County|     8| 127.158| N/A|   173|  2749.785| N/A|  62,914|
| |Yates County|     7| 280.978| N/A|    56|  2247.822| N/A|  24,913|
| |Chenango County|     6| 127.100| N/A|   212|  4490.859| N/A|  47,207|
| |Cattaraugus County|     6| 78.826| N/A|   164|  2154.578| N/A|  76,117|
| |Wyoming County|     5| 125.442| N/A|   115|  2885.170| N/A|  39,859|
| |Otsego County|     5| 84.044| N/A|   115|  1933.001| N/A|  59,493|
| |Genesee County|     5| 87.291| N/A|   274|  4783.520| N/A|  57,280|
| |Delaware County|     4| 90.631| N/A|   104|  2356.406| N/A|  44,135|
| |St. Lawrence County|     4| 37.126| N/A|   263|  2441.062| N/A| 107,740|
| |Herkimer County|     4| 65.233| N/A|   268|  4370.587| N/A|  61,319|
| |Clinton County|     4| 49.699| N/A|   127|  1577.934| N/A|  80,485|
| |Montgomery County|     4| 81.266| N/A|   169|  3433.494| N/A|  49,221|
| |Chemung County|     3| 35.947| N/A|   165|  1977.090| N/A|  83,456|
| |Seneca County|     3| 88.194| N/A|    86|  2528.222| N/A|  34,016|
| |Oswego County|     3| 25.614| N/A|   251|  2143.028| N/A| 117,124|
| |Wayne County|     3| 33.364| N/A|   249|  2769.190| N/A|  89,918|
| |Cayuga County|     2| 26.118| N/A|   151|  1971.897| N/A|  76,576|
| |Allegany County|     1| 21.696| N/A|    78|  1692.304| N/A|  46,091|
| |Essex County|     0|  0.000| N/A|    55|  1491.121| N/A|  36,885|
| |Schoharie County|     0|  0.000| N/A|    69|  2225.878| N/A|  30,999|
| |Tompkins County|     0|  0.000| N/A|   232|  2270.503| N/A| 102,180|
| |Lewis County|     0|  0.000| N/A|    39|  1483.115| N/A|  26,296|
| |Jefferson County|     0|  0.000| N/A|   140|  1274.651| N/A| 109,834|
| |Hamilton County|     0|  0.000| N/A|     8|  1811.594| N/A|   4,416|
| |Franklin County|     0|  0.000| N/A|    52|  1039.543| N/A|  50,022|
| |Cortland County|     0|  0.000| N/A|    94|  1975.578| N/A|  47,581|
| |Schuyler County|     0|  0.000| N/A|    22|  1235.469| N/A|  17,807|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,021| 253.618| N/A|541,339| 13700.545| N/A|39,512,223|
| |Los Angeles County| 4,869| 485.003|  4.411|201,200| 20041.623| 215.785|10,039,107|
| |Riverside County|   770| 311.672|  4.742|39,741| 16085.918| 179.949|2,470,546|
| |Orange County|   697| 219.480|  4.184|38,711| 12189.784| 131.940|3,175,692|
| |San Diego County|   583| 174.638|  1.070|31,127|  9324.123| 104.372|3,338,330|
| |San Bernardino County|   490| 224.762|  4.653|34,635| 15886.995| 193.112|2,180,085|
| |Imperial County|   240| 1324.394| 31.533| 9,601| 52981.265| 238.864| 181,215|
| |Alameda County|   206| 123.255|  2.051|12,884|  7708.835| 149.838|1,671,329|
| |Tulare County|   196| 420.425|  7.048|10,334| 22166.690| 334.930| 466,195|
| |Santa Clara County|   196| 101.668|  0.445|11,336|  5880.119| 118.933|1,927,852|
| |San Joaquin County|   192| 251.920|  7.685|12,119| 15901.111| 145.641| 762,148|
| |Fresno County|   157| 157.141|  5.290|16,625| 16639.959| 330.726| 999,101|
| |Sacramento County|   155| 99.867|  2.577|10,544|  6793.561| 80.998|1,552,058|
| |Kern County|   152| 168.851|  2.063|21,724| 24132.361| 525.755| 900,202|
| |Stanislaus County|   151| 274.216| 12.193| 9,408| 17084.953| 172.001| 550,660|
| |Contra Costa County|   134| 116.166|  2.229| 8,532|  7396.452| 118.271|1,153,526|
| |San Mateo County|   120| 156.541|  0.373| 5,891|  7684.852| 91.875| 766,573|
| |Ventura County|    79| 93.380|  0.844| 7,953|  9400.643| 143.532| 846,006|
| |Marin County|    78| 301.361|  7.727| 5,199| 20086.854| 146.265| 258,826|
| |Santa Barbara County|    68| 152.296| 11.518| 6,652| 14898.130| 178.532| 446,499|
| |San Francisco County|    63| 71.465| N/A| 7,228|  8199.204| N/A| 881,549|
| |Merced County|    62| 223.279| 11.833| 4,855| 17484.154| 406.429| 277,680|
| |Kings County|    56| 366.157|  4.670| 4,453| 29115.993| 324.123| 152,940|
| |Yolo County|    42| 190.476|  0.648| 1,660|  7528.345| 107.548| 220,500|
| |Sonoma County|    42| 84.962|  3.179| 3,208|  6489.513| 132.934| 494,336|
| |Solano County|    39| 87.123|  0.638| 3,959|  8844.101| 140.099| 447,643|
| |Madera County|    36| 228.823|  7.264| 2,208| 14034.463| 292.385| 157,327|
| |Monterey County|    35| 80.634|  2.962| 5,120| 11795.577| 218.205| 434,061|
| |Placer County|    20| 50.210|  1.793| 2,039|  5118.884| 77.825| 398,329|
| |San Luis Obispo County|    16| 56.515|  1.009| 2,047|  7230.380| 154.911| 283,111|
| |Mendocino County|    10| 115.275|  6.587|   363|  4184.486| 115.275|  86,749|
| |Napa County|     9| 65.339| N/A| 1,025|  7441.340| N/A| 137,744|
| |Shasta County|     9| 49.978| N/A|   411|  2282.319| N/A| 180,080|
| |Butte County|     8| 36.499| N/A| 1,060|  4836.075| N/A| 219,186|
| |Sutter County|     6| 61.874| N/A|   893|  9208.939| N/A|  96,971|
| |Colusa County|     4| 185.641| N/A|   361| 16754.072| N/A|  21,547|
| |Yuba County|     4| 50.847| N/A|   572|  7271.063| N/A|  78,668|
| |San Benito County|     4| 63.686| N/A|   699| 11129.156| N/A|  62,808|
| |Santa Cruz County|     4| 14.641| N/A| 1,213|  4439.759| N/A| 273,213|
| |Humboldt County|     4| 29.508| N/A|   280|  2065.537| N/A| 135,558|
| |Glenn County|     3| 105.660| N/A|   352| 12397.422| N/A|  28,393|
| |Tuolumne County|     2| 36.712| N/A|   147|  2698.337| N/A|  54,478|
| |Mariposa County|     2| 116.259| N/A|    60|  3487.764| N/A|  17,203|
| |Lake County|     2| 31.063| N/A|   212|  3292.641| N/A|  64,386|
| |Calaveras County|     1| 21.784| N/A|   136|  2962.640| N/A|  45,905|
| |El Dorado County|     1|  5.186| N/A|   716|  3712.865| N/A| 192,843|
| |Inyo County|     1| 55.435| N/A|    84|  4656.577| N/A|  18,039|
| |Mono County|     1| 69.233| N/A|   153| 10592.634| N/A|  14,444|
| |Nevada County|     1| 10.025| N/A|   321|  3217.884| N/A|  99,755|
| |Tehama County|     1| 15.365| N/A|   271|  4163.850| N/A|  65,084|
| |Del Norte County|     0|  0.000| N/A|    90|  3236.013| N/A|  27,812|
| |Trinity County|     0|  0.000| N/A|     5|   407.000| N/A|  12,285|
| |Siskiyou County|     0|  0.000| N/A|    90|  2067.112| N/A|  43,539|
| |Sierra County|     0|  0.000| N/A|     3|   998.336| N/A|   3,005|
| |Plumas County|     0|  0.000| N/A|    34|  1807.838| N/A|  18,807|
| |Modoc County|     0|  0.000| N/A|     4|   452.438| N/A|   8,841|
| |Lassen County|     0|  0.000| N/A|   633| 20704.543| N/A|  30,573|
| |Amador County|     0|  0.000| N/A|   156|  3924.331| N/A|  39,752|
| |Alpine County|     0|  0.000| N/A|     2|  1771.479| N/A|   1,129|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,684| 1259.920| N/A|119,466| 17332.745| N/A|6,892,503|
| |Middlesex County| 1,998| 1239.686|  2.393|26,156| 16228.837| 47.776|1,611,699|
| |Essex County| 1,190| 1508.173|  2.716|17,617| 22327.301| 81.112| 789,034|
| |Suffolk County| 1,066| 1326.024|  2.132|21,631| 26907.341| 92.050| 803,907|
| |Worcester County|   998| 1201.509|  2.064|13,525| 16282.978| 48.501| 830,622|
| |Norfolk County|   994| 1406.388|  3.032|10,515| 14877.436| 71.754| 706,775|
| |Plymouth County|   717| 1375.666|  2.741| 9,193| 17638.075| 37.002| 521,202|
| |Hampden County|   700| 1500.948|  2.451| 7,541| 16169.496| 49.011| 466,372|
| |Bristol County|   629| 1112.847|  1.769| 9,272| 16404.319| 61.418| 565,217|
| |Barnstable County|   157| 737.124|  1.341| 1,783|  8371.285| 27.500| 212,990|
| |Hampshire County|   128| 795.871|  0.888| 1,158|  7200.149| 45.301| 160,830|
| |Franklin County|    61| 869.194|  2.036|   409|  5827.871| 22.391|  70,180|
| |Berkshire County|    46| 368.165|  1.143|   666|  5330.388| 20.581| 124,944|
| |Dukes County|     0|  0.000| N/A|     0|     0.000| N/A|  17,332|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 8,330| 287.282| N/A|483,920| 16689.267| N/A|28,995,881|
| |Harris County| 1,459| 309.548| 22.793|81,919| 17380.299| 335.584|4,713,325|
| |Hidalgo County|   765| 880.619| 24.503|19,103| 21990.153| 448.614| 868,707|
| |Dallas County|   736| 279.262|  3.903|52,869| 20060.208| 195.137|2,635,516|
| |Bexar County|   705| 351.875| 11.408|41,939| 20932.303| 120.215|2,003,554|
| |Tarrant County|   422| 200.712|  4.281|30,227| 14376.592| 209.001|2,102,515|
| |Cameron County|   405| 957.078| 34.097|15,865| 37491.463| 2174.441| 423,163|
| |Travis County|   288| 226.068|  7.625|22,256| 17470.019| 232.011|1,273,954|
| |El Paso County|   285| 339.594|  9.022|15,596| 18583.525| 282.059| 839,238|
| |Nueces County|   227| 626.563| 24.053|13,552| 37406.085| 852.504| 362,294|
| |Fort Bend County|   153| 188.496|  2.992| 8,878| 10937.700| 337.568| 811,688|
| |Webb County|   149| 538.583| 39.761| 7,417| 26809.855| 899.015| 276,652|
| |Galveston County|   110| 321.507|  7.516| 9,230| 26977.340| 260.963| 342,139|
| |Collin County|    87| 84.080|  2.761| 7,074|  6836.566| 123.842|1,034,730|
| |Williamson County|    86| 145.627|  1.693| 6,058| 10258.216| 106.922| 590,551|
| |Brazoria County|    85| 227.112|  8.779| 6,988| 18671.312| 293.910| 374,264|
| |Denton County|    82| 92.425|  2.254| 7,374|  8311.476| 141.858| 887,207|
| |Montgomery County|    77| 126.772|  1.882| 6,510| 10717.972| 101.841| 607,391|
| |Jefferson County|    76| 302.109|  6.814| 5,771| 22940.393| 228.285| 251,565|
| |Lubbock County|    69| 222.173|  2.760| 5,811| 18710.818| 222.173| 310,569|
| |Comal County|    67| 428.913|  8.231| 1,763| 11286.161| 117.059| 156,209|
| |Ector County|    54| 324.865|  4.297| 3,512| 21128.243| 211.420| 166,223|
| |Starr County|    52| 804.543| 30.944| 2,091| 32351.895| 678.557|  64,633|
| |Guadalupe County|    51| 305.669| 11.987| 1,670| 10009.170| 65.929| 166,847|
| |Val Verde County|    49| 999.490| 78.677| 1,636| 33370.729| 699.352|  49,025|
| |McLennan County|    49| 190.942|  5.567| 4,748| 18501.849| 309.515| 256,623|
| |Brazos County|    46| 200.688|  2.493| 3,997| 17438.081| 114.679| 229,211|
| |Midland County|    46| 260.134|  4.847| 2,570| 14533.569| 367.581| 176,832|
| |Potter County|    44| 374.739|  8.517| 3,644| 31035.217| 231.170| 117,415|
| |Walker County|    41| 561.867|  3.915| 2,861| 39207.356| 174.238|  72,971|
| |Angelina County|    40| 461.281| 13.179| 1,769| 20400.161| 268.532|  86,715|
| |Nacogdoches County|    40| 613.459| 15.336| 1,094| 16778.112| 300.157|  65,204|
| |Washington County|    39| 1086.896|  7.963|   498| 13878.825| 183.140|  35,882|
| |Ellis County|    38| 205.599|  3.865| 2,739| 14819.344| 256.612| 184,826|
| |Victoria County|    37| 401.807| 15.514| 3,392| 36835.932| 421.975|  92,084|
| |Maverick County|    37| 630.088|  2.433| 2,210| 37634.958| 870.932|  58,722|
| |Hays County|    37| 160.736|  4.965| 4,989| 21673.306| 429.457| 230,191|
| |Bell County|    33| 90.928|  1.575| 3,733| 10285.900| 140.919| 362,924|
| |Liberty County|    32| 362.734| 12.955|   925| 10485.270| 178.128|  88,219|
| |Bowie County|    32| 343.182|  9.192|   707|  7582.176| 21.449|  93,245|
| |Johnson County|    30| 170.632|  6.500| 1,760| 10010.409| 266.511| 175,817|
| |Caldwell County|    26| 595.456| 13.087| 1,118| 25604.617| 202.848|  43,664|
| |Matagorda County|    25| 682.259| 19.493|   711| 19403.433| 261.208|  36,643|
| |Wharton County|    25| 601.598| 20.626|   666| 16026.567| 257.828|  41,556|
| |Medina County|    25| 484.646| 13.847|   621| 12038.617| 108.007|  51,584|
| |Tom Green County|    24| 201.342|  5.992| 2,560| 21476.510| 461.409| 119,200|
| |Hale County|    24| 718.434| 17.106| 1,257| 37627.971| 406.257|  33,406|
| |Gregg County|    23| 185.566|  4.610| 1,358| 10956.473| 101.427| 123,945|
| |Kaufman County|    23| 168.926|  4.197| 2,071| 15210.717| 409.201| 136,154|
| |Harrison County|    22| 330.564|  0.000|   659|  9901.883| 118.058|  66,553|
| |Willacy County|    22| 1030.059| 26.755|   669| 31323.158| 615.360|  21,358|
| |Taylor County|    22| 159.381|  4.140| 1,108|  8027.008| 41.398| 138,034|
| |Hunt County|    21| 212.995|  1.449| 1,137| 11532.142| 184.016|  98,594|
| |Bastrop County|    20| 225.421|  3.220| 1,344| 15148.270| 107.880|  88,723|
| |Smith County|    20| 85.929|  3.069| 2,446| 10509.085| 119.686| 232,751|
| |Grimes County|    20| 692.521|  4.947|   858| 29709.141| 128.611|  28,880|
| |San Patricio County|    20| 299.715| 10.704|   882| 13217.443| 402.475|  66,730|
| |Randall County|    19| 137.968|  3.112| 1,683| 12221.068| 160.790| 137,713|
| |Wilson County|    18| 352.457|  5.595|   434|  8498.140| 55.946|  51,070|
| |Shelby County|    18| 712.194| 11.305|   397| 15707.842| 146.961|  25,274|
| |Parker County|    18| 125.982|  5.999| 1,178|  8244.796| 151.978| 142,878|
| |Lamar County|    18| 361.018|  5.730|   652| 13076.877| 134.665|  49,859|
| |Orange County|    18| 215.838|  5.139| 1,369| 16415.655| 633.809|  83,396|
| |Deaf Smith County|    17| 916.640|  0.000|   644| 34724.469| 608.526|  18,546|
| |Panola County|    17| 732.948|  0.000|   280| 12072.088| 80.070|  23,194|
| |Atascosa County|    16| 312.787|  8.378|   425|  8308.408| 55.855|  51,153|
| |DeWitt County|    15| 744.048| 14.172|   643| 31894.841| 857.426|  20,160|
| |Brown County|    15| 396.155|  7.546|   380| 10035.918| 120.733|  37,864|
| |Lavaca County|    14| 694.651|  7.088|   618| 30663.888| 177.207|  20,154|
| |Titus County|    14| 427.481|  0.000| 1,289| 39358.779| 56.707|  32,750|
| |Fayette County|    14| 552.355|  5.636|   378| 14913.596| 73.272|  25,346|
| |Grayson County|    13| 95.439|  2.098| 1,092|  8016.915| 125.854| 136,212|
| |Hardin County|    13| 225.687|  7.440|   925| 16058.470| 310.009|  57,602|
| |Jim Wells County|    13| 321.130| 28.231|   670| 16550.566| 342.304|  40,482|
| |Moore County|    13| 620.821|  6.822| 1,044| 49856.734| 245.600|  20,940|
| |Aransas County|    13| 552.956|  6.076|   165|  7018.290| 97.223|  23,510|
| |Rockwall County|    12| 114.378|  0.000|   813|  7749.130| 129.356| 104,915|
| |Polk County|    11| 214.204|  8.346|   700| 13631.141| 122.402|  51,353|
| |Red River County|    11| 914.913|  0.000|   136| 11311.653| 35.646|  12,023|
| |San Augustine County|    11| 1335.438| 17.343|   160| 19424.548| 121.403|   8,237|
| |Henderson County|    11| 132.951|  5.180|   621|  7505.711| 136.405|  82,737|
| |Wichita County|    11| 83.188|  2.161|   962|  7275.202| 82.108| 132,230|
| |Anderson County|    10| 173.205|  7.423| 2,353| 40755.175| 442.910|  57,735|
| |Lamb County|    10| 775.615| 55.401|   218| 16908.400| 243.765|  12,893|
| |Lee County|     9| 522.072| N/A|   163|  9455.305| N/A|  17,239|
| |Uvalde County|     9| 336.562| N/A|   520| 19445.795| N/A|  26,741|
| |Hood County|     9| 146.002| N/A|   505|  8192.333| N/A|  61,643|
| |Bee County|     9| 276.370| N/A|   704| 21618.302| N/A|  32,565|
| |Gonzales County|     9| 431.924| N/A|   670| 32154.341| N/A|  20,837|
| |Navarro County|     8| 159.639| N/A|   831| 16582.523| N/A|  50,113|
| |San Jacinto County|     8| 277.210| N/A|   175|  6063.966| N/A|  28,859|
| |Fannin County|     8| 225.263| N/A|   237|  6673.425| N/A|  35,514|
| |Marion County|     8| 811.853| N/A|   129| 13091.131| N/A|   9,854|
| |Cass County|     8| 266.436| N/A|   166|  5528.542| N/A|  30,026|
| |Burnet County|     8| 166.130| N/A|   552| 11462.984| N/A|  48,155|
| |Kleberg County|     7| 228.162| N/A|   416| 13559.322| N/A|  30,680|
| |Parmer County|     7| 728.787| N/A|   328| 34148.881| N/A|   9,605|
| |Sabine County|     6| 569.152| N/A|    51|  4837.792| N/A|  10,542|
| |Duval County|     6| 537.779| N/A|   164| 14699.292| N/A|  11,157|
| |Hill County|     6| 163.715| N/A|   313|  8540.479| N/A|  36,649|
| |Palo Pinto County|     6| 205.557| N/A|   244|  8359.313| N/A|  29,189|
| |Houston County|     6| 261.233| N/A|   308| 13409.962| N/A|  22,968|
| |Wise County|     6| 85.734| N/A|   375|  5358.368| N/A|  69,984|
| |Andrews County|     6| 320.770| N/A|   277| 14808.875| N/A|  18,705|
| |Karnes County|     6| 384.591| N/A|   556| 35638.741| N/A|  15,601|
| |Burleson County|     6| 325.327| N/A|   236| 12796.183| N/A|  18,443|
| |Kerr County|     6| 114.068| N/A|   394|  7490.494| N/A|  52,600|
| |Blanco County|     5| 419.076| N/A|    98|  8213.897| N/A|  11,931|
| |Erath County|     5| 117.102| N/A|   507| 11874.092| N/A|  42,698|
| |Frio County|     5| 246.233| N/A|   497| 24475.524| N/A|  20,306|
| |Floyd County|     5| 875.350| N/A|    88| 15406.162| N/A|   5,712|
| |Dallam County|     5| 686.153| N/A|   187| 25662.138| N/A|   7,287|
| |Coryell County|     5| 65.832| N/A|   654|  8610.815| N/A|  75,951|
| |Gillespie County|     5| 185.268| N/A|   176|  6521.417| N/A|  26,988|
| |Jasper County|     5| 140.730| N/A|   304|  8556.391| N/A|  35,529|
| |Jackson County|     5| 338.753| N/A|   383| 25948.509| N/A|  14,760|
| |Cherokee County|     5| 94.974| N/A|   953| 18102.040| N/A|  52,646|
| |Zavala County|     5| 422.297| N/A|   202| 17060.811| N/A|  11,840|
| |Reeves County|     5| 312.969| N/A|   147|  9201.302| N/A|  15,976|
| |Camp County|     5| 381.854| N/A|   221| 16877.959| N/A|  13,094|
| |Wood County|     5| 109.796| N/A|   316|  6939.107| N/A|  45,539|
| |Bailey County|     4| 571.429| N/A|   168| 24000.000| N/A|   7,000|
| |Goliad County|     4| 522.330| N/A|    77| 10054.845| N/A|   7,658|
| |Dawson County|     4| 314.268| N/A|   140| 10999.371| N/A|  12,728|
| |Calhoun County|     4| 187.882| N/A|   526| 24706.435| N/A|  21,290|
| |Waller County|     4| 72.403| N/A|   431|  7801.470| N/A|  55,246|
| |Newton County|     4| 294.226| N/A|    93|  6840.750| N/A|  13,595|
| |Young County|     4| 222.099| N/A|   151|  8384.231| N/A|  18,010|
| |Lynn County|     4| 672.156| N/A|    66| 11090.573| N/A|   5,951|
| |Hockley County|     4| 173.754| N/A|   194|  8427.088| N/A|  23,021|
| |Howard County|     4| 109.099| N/A|   164|  4473.053| N/A|  36,664|
| |Kendall County|     4| 84.333| N/A|   156|  3288.988| N/A|  47,431|
| |Martin County|     4| 693.121| N/A|    53|  9183.850| N/A|   5,771|
| |Castro County|     4| 531.208| N/A|   190| 25232.404| N/A|   7,530|
| |Yoakum County|     3| 344.313| N/A|    96| 11018.019| N/A|   8,713|
| |Bandera County|     3| 129.803| N/A|    89|  3850.813| N/A|  23,112|
| |Austin County|     3| 99.893| N/A|   223|  7425.413| N/A|  30,032|
| |Van Zandt County|     3| 53.013| N/A|   368|  6502.916| N/A|  56,590|
| |Callahan County|     3| 215.162| N/A|    46|  3299.147| N/A|  13,943|
| |Comanche County|     3| 220.022| N/A|   141| 10341.034| N/A|  13,635|
| |Cooke County|     3| 72.715| N/A|   212|  5138.522| N/A|  41,257|
| |Crockett County|     3| 866.051| N/A|   157| 45323.326| N/A|   3,464|
| |Hamilton County|     3| 354.568| N/A|    57|  6736.792| N/A|   8,461|
| |Falls County|     3| 173.440| N/A|   123|  7111.060| N/A|  17,297|
| |Refugio County|     3| 431.779| N/A|   216| 31088.083| N/A|   6,948|
| |Reagan County|     3| 779.423| N/A|    61| 15848.272| N/A|   3,849|
| |Stephens County|     3| 320.307| N/A|    34|  3630.152| N/A|   9,366|
| |Limestone County|     3| 128.003| N/A|   209|  8917.524| N/A|  23,437|
| |Dimmit County|     3| 296.326| N/A|   142| 14026.077| N/A|  10,124|
| |Milam County|     3| 120.856| N/A|   332| 13374.693| N/A|  24,823|
| |Trinity County|     3| 204.764| N/A|   155| 10579.483| N/A|  14,651|
| |Garza County|     3| 481.618| N/A|    99| 15893.402| N/A|   6,229|
| |Nolan County|     3| 203.887| N/A|   132|  8971.048| N/A|  14,714|
| |Ochiltree County|     2| 203.335| N/A|    91|  9251.728| N/A|   9,836|
| |Chambers County|     2| 45.624| N/A|   929| 21192.144| N/A|  43,837|
| |Brewster County|     2| 217.320| N/A|   186| 20210.801| N/A|   9,203|
| |Zapata County|     2| 141.054| N/A|   167| 11777.982| N/A|  14,179|
| |Madison County|     2| 140.017| N/A|   650| 45505.461| N/A|  14,284|
| |Bosque County|     2| 107.038| N/A|   152|  8134.868| N/A|  18,685|
| |Robertson County|     2| 117.137| N/A|   226| 13236.500| N/A|  17,074|
| |Live Oak County|     2| 163.840| N/A|   222| 18186.287| N/A|  12,207|
| |Leon County|     2| 114.916| N/A|   138|  7929.212| N/A|  17,404|
| |Lampasas County|     2| 93.336| N/A|    88|  4106.776| N/A|  21,428|
| |Hutchinson County|     2| 95.520| N/A|   121|  5778.966| N/A|  20,938|
| |Hudspeth County|     2| 409.333| N/A|    23|  4707.327| N/A|   4,886|
| |Swisher County|     2| 270.380| N/A|    79| 10680.005| N/A|   7,397|
| |Terry County|     2| 162.114| N/A|   132| 10699.522| N/A|  12,337|
| |Throckmorton County|     2| 1332.445| N/A|     4|  2664.890| N/A|   1,501|
| |Upshur County|     2| 47.901| N/A|   207|  4957.728| N/A|  41,753|
| |Tyler County|     2| 92.285| N/A|   116|  5352.529| N/A|  21,672|
| |Hansford County|     2| 370.439| N/A|    64| 11854.047| N/A|   5,399|
| |Rusk County|     2| 36.761| N/A|   354|  6506.635| N/A|  54,406|
| |Cottle County|     2| 1430.615| N/A|    14| 10014.306| N/A|   1,398|
| |Gray County|     2| 91.383| N/A|   211|  9640.866| N/A|  21,886|
| |Culberson County|     2| 921.234| N/A|    17|  7830.493| N/A|   2,171|
| |Crane County|     2| 416.927| N/A|    71| 14800.917| N/A|   4,797|
| |Colorado County|     2| 93.054| N/A|   265| 12329.596| N/A|  21,493|
| |Kenedy County|     1| 2475.248| N/A|     6| 14851.485| N/A|     404|
| |Hopkins County|     1| 26.966| N/A|   194|  5231.367| N/A|  37,084|
| |Jim Hogg County|     1| 192.308| N/A|    54| 10384.615| N/A|   5,200|
| |Knox County|     1| 272.926| N/A|    56| 15283.843| N/A|   3,664|
| |La Salle County|     1| 132.979| N/A|   357| 47473.404| N/A|   7,520|
| |Llano County|     1| 45.882| N/A|    88|  4037.623| N/A|  21,795|
| |Scurry County|     1| 59.869| N/A|   473| 28318.266| N/A|  16,703|
| |McCulloch County|     1| 125.251| N/A|    45|  5636.273| N/A|   7,984|
| |Wilbarger County|     1| 78.315| N/A|    61|  4777.195| N/A|  12,769|
| |Winkler County|     1| 124.844| N/A|    73|  9113.608| N/A|   8,010|
| |Ward County|     1| 83.347| N/A|    88|  7334.556| N/A|  11,998|
| |Upton County|     1| 273.448| N/A|    17|  4648.619| N/A|   3,657|
| |Morris County|     1| 80.723| N/A|   100|  8072.328| N/A|  12,388|
| |Oldham County|     1| 473.485| N/A|    14|  6628.788| N/A|   2,112|
| |Pecos County|     1| 63.199| N/A|   236| 14914.997| N/A|  15,823|
| |Montague County|     1| 50.459| N/A|    64|  3229.387| N/A|  19,818|
| |Real County|     1| 289.687| N/A|    87| 25202.781| N/A|   3,452|
| |Runnels County|     1| 97.428| N/A|   117| 11399.065| N/A|  10,264|
| |Schleicher County|     1| 358.038| N/A|    36| 12889.366| N/A|   2,793|
| |Rains County|     1| 79.911| N/A|    51|  4075.436| N/A|  12,514|
| |Sutton County|     1| 264.831| N/A|    62| 16419.492| N/A|   3,776|
| |Franklin County|     1| 93.240| N/A|    90|  8391.608| N/A|  10,725|
| |Hall County|     1| 337.382| N/A|    10|  3373.819| N/A|   2,964|
| |Eastland County|     1| 54.466| N/A|    65|  3540.305| N/A|  18,360|
| |Briscoe County|     1| 646.831| N/A|    11|  7115.136| N/A|   1,546|
| |Brooks County|     1| 140.984| N/A|    95| 13393.487| N/A|   7,093|
| |Coke County|     1| 295.247| N/A|    40| 11809.861| N/A|   3,387|
| |Dickens County|     1| 452.284| N/A|     4|  1809.136| N/A|   2,211|
| |Fisher County|     1| 261.097| N/A|    26|  6788.512| N/A|   3,830|
| |Crosby County|     1| 174.307| N/A|    59| 10284.121| N/A|   5,737|
| |Clay County|     1| 95.502| N/A|    38|  3629.071| N/A|  10,471|
| |Mills County|     0|  0.000| N/A|    16|  3283.398| N/A|   4,873|
| |Jeff Davis County|     0|  0.000| N/A|     8|  3518.030| N/A|   2,274|
| |Jack County|     0|  0.000| N/A|    51|  5707.890| N/A|   8,935|
| |Irion County|     0|  0.000| N/A|     9|  5859.375| N/A|   1,536|
| |Hemphill County|     0|  0.000| N/A|    42| 10997.643| N/A|   3,819|
| |Terrell County|     0|  0.000| N/A|     2|  2577.320| N/A|     776|
| |Mitchell County|     0|  0.000| N/A|    59|  6904.623| N/A|   8,545|
| |Carson County|     0|  0.000| N/A|    14|  2362.470| N/A|   5,926|
| |Stonewall County|     0|  0.000| N/A|     5|  3703.704| N/A|   1,350|
| |Sterling County|     0|  0.000| N/A|     0|     0.000| N/A|   1,291|
| |Somervell County|     0|  0.000| N/A|    66|  7230.500| N/A|   9,128|
| |Sherman County|     0|  0.000| N/A|    39| 12905.361| N/A|   3,022|
| |Shackelford County|     0|  0.000| N/A|    17|  5206.738| N/A|   3,265|
| |San Saba County|     0|  0.000| N/A|    23|  3798.514| N/A|   6,055|
| |Motley County|     0|  0.000| N/A|     4|  3333.333| N/A|   1,200|
| |Wheeler County|     0|  0.000| N/A|    33|  6526.899| N/A|   5,056|
| |Jones County|     0|  0.000| N/A|   632| 31469.402| N/A|  20,083|
| |Armstrong County|     0|  0.000| N/A|     7|  3709.592| N/A|   1,887|
| |Menard County|     0|  0.000| N/A|    17|  7951.356| N/A|   2,138|
| |Mason County|     0|  0.000| N/A|    51| 11932.616| N/A|   4,274|
| |Childress County|     0|  0.000| N/A|    37|  5064.331| N/A|   7,306|
| |McMullen County|     0|  0.000| N/A|     8| 10767.160| N/A|     743|
| |Loving County|     0|  0.000| N/A|     0|     0.000| N/A|     169|
| |Lipscomb County|     0|  0.000| N/A|    16|  4948.964| N/A|   3,233|
| |Archer County|     0|  0.000| N/A|    21|  2455.279| N/A|   8,553|
| |Kinney County|     0|  0.000| N/A|    19|  5181.347| N/A|   3,667|
| |King County|     0|  0.000| N/A|     0|     0.000| N/A|     272|
| |Kimble County|     0|  0.000| N/A|    13|  2997.464| N/A|   4,337|
| |Kent County|     0|  0.000| N/A|     3|  3937.008| N/A|     762|
| |Hardeman County|     0|  0.000| N/A|    17|  4322.400| N/A|   3,933|
| |Borden County|     0|  0.000| N/A|     0|     0.000| N/A|     654|
| |Edwards County|     0|  0.000| N/A|    25| 12939.959| N/A|   1,932|
| |Gaines County|     0|  0.000| N/A|   149|  6932.812| N/A|  21,492|
| |Freestone County|     0|  0.000| N/A|   150|  7607.648| N/A|  19,717|
| |Collingsworth County|     0|  0.000| N/A|     8|  2739.726| N/A|   2,920|
| |Concho County|     0|  0.000| N/A|    26|  9537.784| N/A|   2,726|
| |Hartley County|     0|  0.000| N/A|    84| 15064.562| N/A|   5,576|
| |Haskell County|     0|  0.000| N/A|    39|  6892.895| N/A|   5,658|
| |Baylor County|     0|  0.000| N/A|     8|  2279.852| N/A|   3,509|
| |Coleman County|     0|  0.000| N/A|    18|  2201.835| N/A|   8,175|
| |Cochran County|     0|  0.000| N/A|    31| 10865.755| N/A|   2,853|
| |Glasscock County|     0|  0.000| N/A|     6|  4258.339| N/A|   1,409|
| |Roberts County|     0|  0.000| N/A|     6|  7025.761| N/A|     854|
| |Presidio County|     0|  0.000| N/A|    46|  6861.575| N/A|   6,704|
| |Donley County|     0|  0.000| N/A|    46| 14032.947| N/A|   3,278|
| |Foard County|     0|  0.000| N/A|     2|  1731.602| N/A|   1,155|
| |Delta County|     0|  0.000| N/A|    16|  3001.313| N/A|   5,331|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 7,747| 360.699| N/A|509,743| 23733.553| N/A|21,477,737|
| |Miami-Dade County| 1,784| 656.621| 14.144|127,677| 46992.941| 618.395|2,716,940|
| |Palm Beach County|   892| 595.950|  8.208|35,737| 23876.080| 290.244|1,496,770|
| |Broward County|   782| 400.455|  7.755|60,058| 30755.160| 420.354|1,952,778|
| |Pinellas County|   469| 481.028|  7.473|17,358| 17803.150| 182.272| 974,996|
| |Hillsborough County|   378| 256.799|  4.561|31,563| 21442.722| 273.783|1,471,968|
| |Lee County|   323| 419.166|  6.859|16,090| 20880.457| 176.677| 770,577|
| |Polk County|   304| 419.439|  8.278|13,654| 18838.898| 270.625| 724,777|
| |Orange County|   275| 197.352|  6.459|30,776| 22086.157| 224.007|1,393,452|
| |Manatee County|   189| 468.688|  4.605| 9,050| 22442.486| 252.589| 403,253|
| |Duval County|   165| 172.278|  1.939|22,568| 23563.437| 261.325| 957,755|
| |St. Lucie County|   148| 450.811| 13.054| 5,514| 16795.767| 265.874| 328,297|
| |Brevard County|   134| 222.613|  6.171| 5,794|  9625.512| 109.408| 601,942|
| |Collier County|   130| 337.748|  3.340|10,118| 26287.211| 283.189| 384,902|
| |Sarasota County|   130| 299.717|  3.623| 6,025| 13890.746| 191.687| 433,742|
| |Volusia County|   124| 224.116|  3.873| 7,488| 13533.737| 201.653| 553,284|
| |Escambia County|   111| 348.710|  8.527| 8,515| 26750.148| 411.541| 318,316|
| |Seminole County|   109| 231.017| 11.203| 6,932| 14691.857| 155.324| 471,826|
| |Pasco County|   104| 187.744|  2.579| 6,802| 12279.153| 154.992| 553,947|
| |Osceola County|    96| 255.488| 12.166| 9,286| 24713.174| 382.092| 375,751|
| |Charlotte County|    89| 471.124|  3.025| 2,144| 11349.320| 192.836| 188,910|
| |Martin County|    87| 540.373| 12.422| 3,712| 23055.901| 133.984| 161,000|
| |Marion County|    83| 227.037| 10.551| 5,707| 15610.853| 400.539| 365,579|
| |Lake County|    60| 163.435|  3.502| 4,840| 13183.772| 168.105| 367,118|
| |Indian River County|    51| 318.903|  8.933| 2,424| 15157.294| 229.575| 159,923|
| |Clay County|    50| 228.048|  1.955| 3,110| 14184.591| 229.351| 219,252|
| |Bay County|    45| 257.577| 19.625| 4,077| 23336.481| 588.748| 174,705|
| |Hernando County|    42| 216.584|  9.577| 1,906|  9828.795| 212.901| 193,920|
| |Sumter County|    40| 302.069| 14.025| 1,208|  9122.489| 161.823| 132,420|
| |Suwannee County|    38| 855.528| 19.298| 1,302| 29313.101| 707.580|  44,417|
| |Hendry County|    37| 880.491|  6.799| 1,709| 40669.173| 309.362|  42,022|
| |Jackson County|    36| 775.628| 24.623| 1,797| 38716.766| 751.005|  46,414|
| |Citrus County|    36| 240.550|  9.546| 1,429|  9548.501| 226.232| 149,657|
| |Okaloosa County|    35| 166.083|  7.457| 3,292| 15621.293| 398.599| 210,738|
| |Santa Rosa County|    34| 184.469|  9.301| 3,700| 20074.547| 326.308| 184,313|
| |Highlands County|    34| 320.087| 10.759| 1,328| 12502.236| 263.601| 106,221|
| |St. Johns County|    33| 124.683|  4.858| 3,512| 13269.254| 185.675| 264,672|
| |Alachua County|    25| 92.922|  2.655| 3,952| 14689.102| 267.615| 269,043|
| |Putnam County|    23| 308.638| 15.336| 1,446| 19403.926| 354.646|  74,521|
| |Leon County|    23| 78.343|  4.379| 4,643| 15815.002| 263.251| 293,582|
| |Gadsden County|    21| 459.921| 12.515| 1,663| 36421.375| 1088.793|  45,660|
| |DeSoto County|    16| 421.042|  7.519| 1,321| 34762.243| 263.151|  38,001|
| |Walton County|    15| 202.508|  5.786| 1,323| 17861.241| 335.585|  74,071|
| |Washington County|    14| 549.602|  5.608|   747| 29325.168| 1452.518|  25,473|
| |Columbia County|    13| 181.346|  5.978| 2,731| 38096.699| 585.888|  71,686|
| |Flagler County|    13| 112.964|  3.724|   989|  8593.947| 151.446| 115,081|
| |Monroe County|    13| 175.136| 13.472| 1,438| 19372.743| 400.311|  74,228|
| |Nassau County|    11| 124.118|  1.612| 1,184| 13359.661| 236.953|  88,625|
| |Madison County|     8| 432.596| N/A|   675| 36500.297| N/A|  18,493|
| |Okeechobee County|     7| 166.003| N/A|   989| 23453.804| N/A|  42,168|
| |Hardee County|     7| 259.866| N/A|   890| 33040.056| N/A|  26,937|
| |Calhoun County|     7| 496.278| N/A|   356| 25239.277| N/A|  14,105|
| |Jefferson County|     5| 350.976| N/A|   438| 30745.472| N/A|  14,246|
| |Hamilton County|     4| 277.239| N/A|   598| 41447.186| N/A|  14,428|
| |Taylor County|     4| 185.451| N/A|   857| 39732.950| N/A|  21,569|
| |Dixie County|     4| 237.727| N/A|   375| 22286.937| N/A|  16,826|
| |Liberty County|     4| 478.813| N/A|   384| 45966.004| N/A|   8,354|
| |Levy County|     4| 96.379| N/A|   645| 15541.045| N/A|  41,503|
| |Bradford County|     4| 141.839| N/A|   378| 13403.780| N/A|  28,201|
| |Union County|     4| 262.519| N/A|   244| 16013.651| N/A|  15,237|
| |Wakulla County|     4| 118.557| N/A|   651| 19295.178| N/A|  33,739|
| |Baker County|     4| 136.939| N/A|   528| 18076.001| N/A|  29,210|
| |Glades County|     3| 217.218| N/A|   398| 28817.609| N/A|  13,811|
| |Gilchrist County|     3| 161.447| N/A|   339| 18243.461| N/A|  18,582|
| |Holmes County|     2| 101.952| N/A|   476| 24264.668| N/A|  19,617|
| |Franklin County|     2| 164.948| N/A|   276| 22762.887| N/A|  12,125|
| |Gulf County|     2| 146.638| N/A|   490| 35926.388| N/A|  13,639|
| |Lafayette County|     1| 118.737| N/A|   117| 13892.187| N/A|   8,422|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,594| 599.282| N/A|188,363| 14864.714| N/A|12,671,821|
| |Cook County| 4,912| 953.743|  1.110|109,150| 21193.216| 123.795|5,150,233|
| |DuPage County|   519| 562.345|  1.548|11,926| 12922.016| 115.936| 922,921|
| |Lake County|   444| 637.441|  0.820|12,376| 17767.951| 127.980| 696,535|
| |Will County|   344| 498.014|  1.241| 8,932| 12931.003| 119.954| 690,743|
| |Kane County|   302| 567.239|  1.878| 9,509| 17860.530| 146.237| 532,403|
| |St. Clair County|   159| 612.278|  2.751| 3,845| 14806.343| 234.349| 259,686|
| |Winnebago County|   128| 452.982|  3.033| 3,746| 13256.798| 68.756| 282,572|
| |McHenry County|   114| 370.402|  0.928| 3,060|  9942.360| 109.542| 307,774|
| |Madison County|    74| 281.405|  1.087| 2,410|  9164.683| 197.201| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,713| 15592.289| 91.023| 109,862|
| |Peoria County|    35| 195.335|  0.797| 1,488|  8304.545| 238.389| 179,179|
| |Rock Island County|    34| 239.641|  4.028| 1,656| 11671.918| 132.910| 141,879|
| |Sangamon County|    33| 169.516|  0.000| 1,151|  5912.509| 179.790| 194,672|
| |DeKalb County|    30| 285.995|  2.724|   898|  8560.779| 132.102| 104,897|
| |Boone County|    23| 429.553|  0.000|   754| 14081.877| 112.057|  53,544|
| |Union County|    23| 1381.133| 17.157|   309| 18555.215| 283.089|  16,653|
| |Macon County|    23| 221.135|  0.000|   550|  5288.004| 173.062| 104,009|
| |Kendall County|    23| 178.308|  1.108| 1,319| 10225.599| 79.740| 128,990|
| |LaSalle County|    21| 193.247|  3.944|   666|  6128.703| 266.865| 108,669|
| |Coles County|    20| 395.093|  2.822|   433|  8553.762| 189.080|  50,621|
| |Champaign County|    19| 90.610|  0.000| 1,615|  7701.882| 110.368| 209,689|
| |Jackson County|    19| 334.802|  0.000|   685| 12070.485| 236.627|  56,750|
| |Jefferson County|    19| 504.193|  7.582|   218|  5784.949| 178.173|  37,684|
| |Clinton County|    17| 452.585|  0.000|   378| 10063.362| 216.784|  37,562|
| |Whiteside County|    16| 289.986|  0.000|   335|  6071.590| 85.442|  55,175|
| |McLean County|    15| 87.455|  0.000|   611|  3562.329| 75.794| 171,517|
| |McDonough County|    15| 505.357|  0.000|   137|  4615.592| 67.381|  29,682|
| |Monroe County|    13| 375.321|  0.000|   299|  8632.387| 210.345|  34,637|
| |Cass County|    11| 905.573|  0.000|   219| 18029.143| 352.821|  12,147|
| |Iroquois County|     9| 331.932| N/A|   252|  9294.092| N/A|  27,114|
| |Tazewell County|     8| 60.697| N/A|   448|  3399.012| N/A| 131,803|
| |Jasper County|     7| 728.408| N/A|    55|  5723.205| N/A|   9,610|
| |Randolph County|     7| 220.250| N/A|   441| 13875.779| N/A|  31,782|
| |Montgomery County|     7| 246.357| N/A|   161|  5666.221| N/A|  28,414|
| |Morgan County|     6| 178.264| N/A|   222|  6595.757| N/A|  33,658|
| |Stephenson County|     6| 134.838| N/A|   325|  7303.699| N/A|  44,498|
| |Williamson County|     6| 90.094| N/A|   364|  5465.712| N/A|  66,597|
| |Ogle County|     5| 98.730| N/A|   400|  7898.426| N/A|  50,643|
| |Grundy County|     5| 97.936| N/A|   299|  5856.544| N/A|  51,054|
| |Adams County|     5| 76.412| N/A|   486|  7427.218| N/A|  65,435|
| |Carroll County|     4| 279.623| N/A|    48|  3355.470| N/A|  14,305|
| |Christian County|     4| 123.824| N/A|   128|  3962.358| N/A|  32,304|
| |Bond County|     3| 182.637| N/A|    59|  3591.867| N/A|  16,426|
| |Woodford County|     3| 78.005| N/A|   125|  3250.215| N/A|  38,459|
| |Mercer County|     3| 194.338| N/A|    73|  4728.898| N/A|  15,437|
| |Fayette County|     3| 140.607| N/A|    60|  2812.148| N/A|  21,336|
| |Macoupin County|     3| 66.776| N/A|   154|  3427.859| N/A|  44,926|
| |Douglas County|     2| 102.749| N/A|   106|  5445.672| N/A|  19,465|
| |Cumberland County|     2| 185.770| N/A|    51|  4737.135| N/A|  10,766|
| |Bureau County|     2| 61.297| N/A|   170|  5210.249| N/A|  32,628|
| |Gallatin County|     2| 414.250| N/A|    48|  9942.005| N/A|   4,828|
| |Livingston County|     2| 56.104| N/A|   103|  2889.363| N/A|  35,648|
| |Saline County|     2| 85.139| N/A|   126|  5363.756| N/A|  23,491|
| |Knox County|     2| 40.242| N/A|   285|  5734.522| N/A|  49,699|
| |Vermilion County|     2| 26.400| N/A|   222|  2930.384| N/A|  75,758|
| |Clark County|     1| 64.763| N/A|    76|  4921.961| N/A|  15,441|
| |Perry County|     1| 47.810| N/A|   142|  6789.061| N/A|  20,916|
| |Lee County|     1| 29.329| N/A|   162|  4751.290| N/A|  34,096|
| |Wayne County|     1| 61.671| N/A|    55|  3391.921| N/A|  16,215|
| |Shelby County|     1| 46.224| N/A|    68|  3143.201| N/A|  21,634|
| |Henry County|     1| 20.444| N/A|   224|  4579.560| N/A|  48,913|
| |Jo Daviess County|     1| 47.092| N/A|   121|  5698.140| N/A|  21,235|
| |Jersey County|     1| 45.928| N/A|    85|  3903.918| N/A|  21,773|
| |Effingham County|     1| 29.405| N/A|   129|  3793.225| N/A|  34,008|
| |Ford County|     1| 77.155| N/A|    51|  3934.882| N/A|  12,961|
| |Hancock County|     1| 56.472| N/A|    46|  2597.696| N/A|  17,708|
| |Warren County|     0|  0.000| N/A|   187| 11101.876| N/A|  16,844|
| |Pike County|     0|  0.000| N/A|    18|  1156.738| N/A|  15,561|
| |Piatt County|     0|  0.000| N/A|    54|  3303.965| N/A|  16,344|
| |Moultrie County|     0|  0.000| N/A|    69|  4758.293| N/A|  14,501|
| |Massac County|     0|  0.000| N/A|    36|  2613.999| N/A|  13,772|
| |Pope County|     0|  0.000| N/A|     8|  1915.250| N/A|   4,177|
| |Pulaski County|     0|  0.000| N/A|    91| 17057.170| N/A|   5,335|
| |Putnam County|     0|  0.000| N/A|    11|  1916.710| N/A|   5,739|
| |Richland County|     0|  0.000| N/A|    15|   966.931| N/A|  15,513|
| |Stark County|     0|  0.000| N/A|     7|  1310.371| N/A|   5,342|
| |White County|     0|  0.000| N/A|    64|  4727.783| N/A|  13,537|
| |Washington County|     0|  0.000| N/A|    60|  4320.588| N/A|  13,887|
| |Wabash County|     0|  0.000| N/A|    34|  2951.389| N/A|  11,520|
| |Scott County|     0|  0.000| N/A|    13|  2625.732| N/A|   4,951|
| |Schuyler County|     0|  0.000| N/A|    17|  2511.820| N/A|   6,768|
| |Menard County|     0|  0.000| N/A|    53|  4345.687| N/A|  12,196|
| |Mason County|     0|  0.000| N/A|    45|  3368.516| N/A|  13,359|
| |Hamilton County|     0|  0.000| N/A|    26|  3203.549| N/A|   8,116|
| |Greene County|     0|  0.000| N/A|    33|  2544.529| N/A|  12,969|
| |Fulton County|     0|  0.000| N/A|    32|   931.858| N/A|  34,340|
| |Franklin County|     0|  0.000| N/A|   147|  3821.259| N/A|  38,469|
| |Edwards County|     0|  0.000| N/A|    17|  2658.327| N/A|   6,395|
| |Edgar County|     0|  0.000| N/A|    28|  1631.607| N/A|  17,161|
| |De Witt County|     0|  0.000| N/A|    32|  2046.297| N/A|  15,638|
| |Crawford County|     0|  0.000| N/A|    29|  1553.544| N/A|  18,667|
| |Clay County|     0|  0.000| N/A|    18|  1365.291| N/A|  13,184|
| |Calhoun County|     0|  0.000| N/A|     9|  1899.135| N/A|   4,739|
| |Brown County|     0|  0.000| N/A|    13|  1976.285| N/A|   6,578|
| |Hardin County|     0|  0.000| N/A|    18|  4710.809| N/A|   3,821|
| |Henderson County|     0|  0.000| N/A|    10|  1504.664| N/A|   6,646|
| |Johnson County|     0|  0.000| N/A|    66|  5315.294| N/A|  12,417|
| |Lawrence County|     0|  0.000| N/A|    44|  2806.480| N/A|  15,678|
| |Marshall County|     0|  0.000| N/A|    22|  1923.413| N/A|  11,438|
| |Alexander County|     0|  0.000| N/A|    36|  6248.915| N/A|   5,761|
| |Marion County|     0|  0.000| N/A|   153|  4112.350| N/A|  37,205|
| |Logan County|     0|  0.000| N/A|    90|  3144.874| N/A|  28,618|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,282| 568.818| N/A|121,247|  9470.950| N/A|12,801,989|
| |Philadelphia County| 1,695| 1070.033| N/A|30,986| 19561.078| N/A|1,584,064|
| |Montgomery County|   855| 1028.986|  1.375| 9,983| 12014.466| 44.701| 830,915|
| |Delaware County|   695| 1226.297|  2.773| 9,076| 16014.200| 117.462| 566,747|
| |Bucks County|   581| 924.762|  0.910| 7,118| 11329.524| 61.620| 628,270|
| |Lancaster County|   410| 751.296|  1.047| 5,756| 10547.456| 70.156| 545,724|
| |Berks County|   368| 873.769|  1.357| 5,302| 12588.920| 60.038| 421,164|
| |Chester County|   349| 664.776|  0.816| 5,075|  9666.869| 65.035| 524,989|
| |Lehigh County|   336| 909.785|  0.387| 4,901| 13270.407| 41.002| 369,318|
| |Northampton County|   292| 956.483|  1.404| 3,902| 12781.499| 40.243| 305,285|
| |Allegheny County|   243| 199.828|  1.880| 8,612|  7081.975| 89.517|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,916|  9137.995| 21.121| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,399| 10708.311| 72.010| 317,417|
| |Dauphin County|   158| 567.735|  1.540| 2,741|  9849.119| 58.005| 278,299|
| |Monroe County|   124| 728.251|  0.839| 1,614|  9479.007| 34.399| 170,271|
| |York County|    92| 204.873|  2.227| 2,444|  5442.504| 63.943| 449,058|
| |Beaver County|    91| 555.118|  2.614| 1,280|  7808.258| 79.303| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,270|  5012.432| 45.670| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,591| 11220.582| 29.218| 141,793|
| |Schuylkill County|    50| 353.709|  1.011|   907|  6416.288| 32.339| 141,359|
| |Franklin County|    46| 296.723|  0.000| 1,323|  8533.997| 58.976| 155,027|
| |Westmoreland County|    46| 131.843|  0.409| 1,484|  4253.380| 41.764| 348,899|
| |Columbia County|    35| 538.760|  0.000|   470|  7234.776| 30.786|  64,964|
| |Carbon County|    28| 436.259|  0.000|   367|  5718.114| 24.484|  64,182|
| |Susquehanna County|    27| 669.510|  3.542|   212|  5256.893| 14.170|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  5.120|  55,809|
| |Adams County|    20| 194.158|  1.387|   490|  4756.866| 40.218| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   354|  3124.476| 50.435| 113,299|
| |Erie County|    17| 63.026|  1.059| 1,046|  3877.981| 74.678| 269,728|
| |Butler County|    15| 79.850|  0.000|   637|  3390.949| 33.461| 187,853|
| |Lawrence County|    14| 163.720|  5.012|   383|  4478.904| 98.566|  85,512|
| |Northumberland County|    12| 132.096|  1.573|   427|  4700.417| 42.459|  90,843|
| |Washington County|    11| 53.175|  0.000|   808|  3905.929| 58.699| 206,865|
| |Centre County|    10| 61.582|  0.000|   364|  2241.586|  9.677| 162,385|
| |Mercer County|     9| 82.249| N/A|   389|  3554.979| N/A| 109,424|
| |Wayne County|     8| 155.760| N/A|   157|  3056.794| N/A|  51,361|
| |Wyoming County|     8| 298.574| N/A|    58|  2164.664| N/A|  26,794|
| |Armstrong County|     6| 92.686| N/A|   200|  3089.519| N/A|  64,735|
| |Indiana County|     6| 71.367| N/A|   297|  3532.644| N/A|  84,073|
| |Juniata County|     6| 242.297| N/A|   129|  5209.385| N/A|  24,763|
| |Clinton County|     5| 129.426| N/A|   118|  3054.463| N/A|  38,632|
| |Fayette County|     5| 38.678| N/A|   465|  3597.011| N/A| 129,274|
| |Perry County|     5| 108.057| N/A|   120|  2593.361| N/A|  46,272|
| |Huntingdon County|     4| 88.605| N/A|   296|  6556.796| N/A|  45,144|
| |Bedford County|     4| 83.528| N/A|   136|  2839.960| N/A|  47,888|
| |Bradford County|     3| 49.732| N/A|    85|  1409.081| N/A|  60,323|
| |Cambria County|     3| 23.043| N/A|   322|  2473.270| N/A| 130,192|
| |Montour County|     3| 164.564| N/A|    98|  5375.754| N/A|  18,230|
| |Somerset County|     3| 40.846| N/A|   127|  1729.138| N/A|  73,447|
| |Blair County|     3| 24.625| N/A|   255|  2093.098| N/A| 121,829|
| |Tioga County|     3| 73.908| N/A|    37|   911.532| N/A|  40,591|
| |Union County|     2| 44.521| N/A|   206|  4585.624| N/A|  44,923|
| |Fulton County|     2| 137.646| N/A|    26|  1789.401| N/A|  14,530|
| |Clarion County|     2| 52.032| N/A|    77|  2003.226| N/A|  38,438|
| |Elk County|     2| 66.867| N/A|    48|  1604.814| N/A|  29,910|
| |Snyder County|     2| 49.539| N/A|   101|  2501.734| N/A|  40,372|
| |Crawford County|     1| 11.816| N/A|   138|  1630.647| N/A|  84,629|
| |Jefferson County|     1| 23.028| N/A|    61|  1404.721| N/A|  43,425|
| |Greene County|     1| 27.599| N/A|   110|  3035.906| N/A|  36,233|
| |Warren County|     1| 25.516| N/A|    20|   510.321| N/A|  39,191|
| |Mifflin County|     1| 21.674| N/A|   115|  2492.522| N/A|  46,138|
| |McKean County|     1| 24.615| N/A|    34|   836.923| N/A|  40,625|
| |Potter County|     0|  0.000| N/A|    20|  1210.214| N/A|  16,526|
| |Venango County|     0|  0.000| N/A|    63|  1243.388| N/A|  50,668|
| |Sullivan County|     0|  0.000| N/A|    10|  1648.533| N/A|   6,066|
| |Forest County|     0|  0.000| N/A|     9|  1241.893| N/A|   7,247|
| |Clearfield County|     0|  0.000| N/A|   150|  1892.625| N/A|  79,255|
| |Cameron County|     0|  0.000| N/A|     6|  1349.224| N/A|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,431| 643.946| N/A|90,055|  9017.352| N/A|9,986,857|
| |Wayne County| 2,821| 1612.605|  1.878|27,836| 15912.260| 74.477|1,749,343|
| |Oakland County| 1,129| 897.753|  0.341|15,176| 12067.584| 77.473|1,257,584|
| |Macomb County|   942| 1077.838|  0.981|10,042| 11490.071| 118.997| 873,972|
| |Genesee County|   295| 726.936|  0.352| 3,604|  8880.938| 66.533| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,380| 11233.646| 84.589| 656,955|
| |Saginaw County|   130| 682.275|  0.750| 1,934| 10150.153| 95.219| 190,539|
| |Washtenaw County|   112| 304.678|  0.000| 2,483|  6754.606| 53.630| 367,601|
| |Kalamazoo County|    83| 313.130|  2.695| 1,601|  6040.005| 60.362| 265,066|
| |Berrien County|    66| 430.245|  1.863| 1,334|  8696.162| 68.914| 153,401|
| |Muskegon County|    58| 334.167|  0.823| 1,156|  6660.291| 40.330| 173,566|
| |Ottawa County|    55| 188.466|  0.490| 1,778|  6092.588| 59.232| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   794|  4989.694| 43.092| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   776|  5784.181| 62.825| 134,159|
| |Jackson County|    34| 214.498|  0.901|   707|  4460.286| 36.951| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   456|  5205.064| 92.948|  87,607|
| |Bay County|    31| 300.603|  0.000|   595|  5769.641| 81.731| 103,126|
| |Ingham County|    30| 102.597|  0.000| 1,520|  5198.252| 40.062| 292,406|
| |Tuscola County|    29| 555.077|  5.469|   330|  6316.394| 90.234|  52,245|
| |Livingston County|    28| 145.837|  0.000|   811|  4224.068| 49.108| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   337|  4947.007| 46.136|  68,122|
| |Hillsdale County|    25| 548.186|  0.000|   258|  5657.274| 43.855|  45,605|
| |Monroe County|    23| 152.824|  1.898|   945|  6279.070| 86.379| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   151|  3709.071| 31.581|  40,711|
| |Cass County|    14| 270.338| 13.793|   313|  6043.988| 113.101|  51,787|
| |Alpena County|    13| 457.666|  0.000|   127|  4471.044| 10.059|  28,405|
| |Clinton County|    13| 163.327|  0.000|   421|  5289.277| 43.075|  79,595|
| |Lenawee County|    12| 121.888|  0.000|   413|  4194.980| 37.727|  98,451|
| |Iosco County|    12| 477.574|  0.000|   130|  5173.718| 11.371|  25,127|
| |Van Buren County|    11| 145.355|  0.000|   428|  5655.615| 81.172|  75,677|
| |Marquette County|    11| 164.920|  0.000|   149|  2233.917| 57.829|  66,699|
| |Otsego County|    10| 405.383|  0.000|   131|  5310.524|  0.000|  24,668|
| |Midland County|    10| 120.256|  1.718|   325|  3908.317| 61.846|  83,156|
| |Isabella County|     9| 128.807| N/A|   205|  2933.936| N/A|  69,872|
| |Eaton County|     8| 72.551| N/A|   455|  4126.310| N/A| 110,268|
| |St. Joseph County|     8| 131.225| N/A|   571|  9366.183| N/A|  60,964|
| |Allegan County|     7| 59.281| N/A|   507|  4293.663| N/A| 118,081|
| |Ionia County|     6| 92.740| N/A|   274|  4235.127| N/A|  64,697|
| |Oceana County|     6| 226.697| N/A|   470| 17757.963| N/A|  26,467|
| |Sanilac County|     6| 145.737| N/A|   102|  2477.532| N/A|  41,170|
| |Grand Traverse County|     5| 53.713| N/A|   202|  2169.990| N/A|  93,088|
| |Crawford County|     5| 356.405| N/A|   103|  7341.935| N/A|  14,029|
| |Huron County|     4| 129.111| N/A|   154|  4970.789| N/A|  30,981|
| |Wexford County|     4| 118.938| N/A|    70|  2081.413| N/A|  33,631|
| |Kalkaska County|     4| 221.754| N/A|    49|  2716.487| N/A|  18,038|
| |Delta County|     3| 83.836| N/A|    87|  2431.254| N/A|  35,784|
| |Clare County|     3| 96.931| N/A|    66|  2132.472| N/A|  30,950|
| |Arenac County|     3| 201.572| N/A|    41|  2754.821| N/A|  14,883|
| |Gladwin County|     2| 78.589| N/A|    57|  2239.774| N/A|  25,449|
| |Mecosta County|     2| 46.027| N/A|    65|  1495.869| N/A|  43,453|
| |Dickinson County|     2| 79.242| N/A|    51|  2020.682| N/A|  25,239|
| |Emmet County|     2| 59.853| N/A|    60|  1795.601| N/A|  33,415|
| |Branch County|     2| 45.959| N/A|   352|  8088.793| N/A|  43,517|
| |Charlevoix County|     2| 76.502| N/A|    45|  1721.302| N/A|  26,143|
| |Barry County|     2| 32.494| N/A|   173|  2810.723| N/A|  61,550|
| |Cheboygan County|     2| 79.126| N/A|    43|  1701.219| N/A|  25,276|
| |Ogemaw County|     2| 95.252| N/A|    53|  2524.170| N/A|  20,997|
| |Iron County|     1| 90.367| N/A|    18|  1626.604| N/A|  11,066|
| |Gogebic County|     1| 71.556| N/A|   109|  7799.642| N/A|  13,975|
| |Benzie County|     1| 56.287| N/A|    28|  1576.044| N/A|  17,766|
| |Alcona County|     1| 96.108| N/A|    28|  2691.014| N/A|  10,405|
| |Montcalm County|     1| 15.652| N/A|   184|  2880.040| N/A|  63,888|
| |Oscoda County|     1| 121.344| N/A|    24|  2912.268| N/A|   8,241|
| |Presque Isle County|     1| 79.416| N/A|    19|  1508.895| N/A|  12,592|
| |Missaukee County|     1| 66.146| N/A|    41|  2711.999| N/A|  15,118|
| |Alger County|     0|  0.000| N/A|     8|   878.349| N/A|   9,108|
| |Manistee County|     0|  0.000| N/A|    34|  1384.478| N/A|  24,558|
| |Schoolcraft County|     0|  0.000| N/A|    13|  1606.128| N/A|   8,094|
| |Roscommon County|     0|  0.000| N/A|    52|  2164.953| N/A|  24,019|
| |Osceola County|     0|  0.000| N/A|    70|  2983.802| N/A|  23,460|
| |Ontonagon County|     0|  0.000| N/A|     6|  1048.951| N/A|   5,720|
| |Newaygo County|     0|  0.000| N/A|   250|  5104.124| N/A|  48,980|
| |Montmorency County|     0|  0.000| N/A|     8|   857.633| N/A|   9,328|
| |Menominee County|     0|  0.000| N/A|   117|  5136.084| N/A|  22,780|
| |Mason County|     0|  0.000| N/A|    99|  3396.926| N/A|  29,144|
| |Mackinac County|     0|  0.000| N/A|    24|  2222.428| N/A|  10,799|
| |Luce County|     0|  0.000| N/A|     3|   481.618| N/A|   6,229|
| |Leelanau County|     0|  0.000| N/A|    69|  3170.810| N/A|  21,761|
| |Lake County|     0|  0.000| N/A|    19|  1602.970| N/A|  11,853|
| |Keweenaw County|     0|  0.000| N/A|     3|  1417.769| N/A|   2,116|
| |Houghton County|     0|  0.000| N/A|    49|  1373.164| N/A|  35,684|
| |Chippewa County|     0|  0.000| N/A|    39|  1044.205| N/A|  37,349|
| |Baraga County|     0|  0.000| N/A|     5|   609.088| N/A|   8,209|
| |Antrim County|     0|  0.000| N/A|    40|  1714.972| N/A|  23,324|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,437| 1244.500| N/A|50,011| 14027.202| N/A|3,565,287|
| |Hartford County| 1,414| 1585.700|  0.481|12,745| 14292.603| 29.478| 891,720|
| |Fairfield County| 1,406| 1490.461|  0.000|17,926| 19002.854| 21.201| 943,332|
| |New Haven County| 1,104| 1291.595|  0.501|13,128| 15358.751| 19.220| 854,757|
| |Middlesex County|   191| 1175.848|  0.000| 1,395|  8587.998| 15.830| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,607|  8911.292|  6.337| 180,333|
| |New London County|   103| 388.377|  0.000| 1,431|  5395.806| 18.853| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,055|  6999.688| 41.704| 150,721|
| |Windham County|    15| 128.444|  0.000|   724|  6199.586| 47.708| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,028| 866.461| N/A|127,034| 27326.227| N/A|4,648,794|
| |Orleans Parish|   561| 1437.931|  0.366|10,573| 27100.250| 135.115| 390,144|
| |Jefferson Parish|   521| 1204.644|  2.642|15,002| 34687.267| 322.383| 432,493|
| |East Baton Rouge Parish|   338| 768.079|  4.220|11,736| 26669.151| 376.573| 440,059|
| |Caddo Parish|   289| 1203.144|  7.732| 6,566| 27335.098| 332.456| 240,204|
| |St. Tammany Parish|   208| 798.713|  3.840| 4,993| 19172.948| 233.141| 260,419|
| |Calcasieu Parish|   130| 639.022|  9.129| 6,695| 32909.613| 549.137| 203,436|
| |Rapides Parish|   112| 863.878| 12.121| 3,194| 24635.937| 322.852| 129,648|
| |Ouachita Parish|   109| 711.122|  4.660| 4,709| 30721.756| 377.463| 153,279|
| |Lafourche Parish|    96| 983.465|  0.000| 2,719| 27854.611| 367.336|  97,614|
| |St. John the Baptist Parish|    91| 2124.332| 10.005| 1,399| 32658.683| 246.783|  42,837|
| |Lafayette Parish|    91| 372.356|  4.676| 7,424| 30377.675| 776.277| 244,390|
| |Terrebonne Parish|    84| 760.449| 14.226| 2,941| 26624.782| 372.465| 110,461|
| |St. Landry Parish|    83| 1010.667| 22.614| 2,583| 31452.438| 920.211|  82,124|
| |Acadia Parish|    79| 1273.269| 18.420| 2,555| 41179.789| 589.434|  62,045|
| |Bossier Parish|    75| 590.370| 10.121| 2,295| 18065.319| 312.615| 127,039|
| |Ascension Parish|    71| 560.804|  4.514| 2,768| 21863.448| 365.594| 126,604|
| |Iberia Parish|    70| 1002.434| 18.412| 2,436| 34884.720| 634.193|  69,830|
| |Tangipahoa Parish|    69| 512.029|  8.481| 3,332| 24725.805| 350.894| 134,758|
| |Washington Parish|    58| 1255.574|  0.000| 1,235| 26735.074| 259.774|  46,194|
| |St. Charles Parish|    51| 960.452|  2.690| 1,424| 26817.326| 279.796|  53,100|
| |St. Mary Parish|    51| 1033.477| 11.580| 1,527| 30943.503| 495.027|  49,348|
| |Livingston Parish|    50| 355.141|  2.029| 2,800| 19887.917| 283.098| 140,789|
| |Iberville Parish|    47| 1445.665|  0.000| 1,191| 36633.755| 474.565|  32,511|
| |St. Martin Parish|    43| 804.776|  0.000| 1,609| 30113.604| 395.704|  53,431|
| |West Baton Rouge Parish|    36| 1360.287|  5.398|   689| 26034.385| 431.837|  26,465|
| |East Feliciana Parish|    35| 1829.109|  0.000|   550| 28743.141| 477.808|  19,135|
| |Union Parish|    33| 1492.672|  6.462|   669| 30260.539| 620.331|  22,108|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   769| 35388.863| 565.380|  21,730|
| |St. James Parish|    32| 1516.875| 13.544|   681| 32281.001| 474.024|  21,096|
| |Bienville Parish|    30| 2265.690| 10.789|   362| 27339.325| 151.046|  13,241|
| |Avoyelles Parish|    29| 722.399| 10.676| 1,002| 24960.143| 380.772|  40,144|
| |Lincoln Parish|    28| 599.033| 15.281|   754| 16131.103| 250.616|  46,742|
| |Allen Parish|    28| 1092.598| 50.170| 1,232| 48074.297| 1131.619|  25,627|
| |De Soto Parish|    26| 946.728| 10.404|   705| 25670.903| 426.548|  27,463|
| |Jefferson Davis Parish|    26| 828.870|  9.108|   996| 31752.104| 282.362|  31,368|
| |Vernon Parish|    25| 527.104| 12.048|   739| 15581.185| 256.022|  47,429|
| |St. Bernard Parish|    24| 508.001|  3.024| 1,081| 22881.212| 250.977|  47,244|
| |Vermilion Parish|    22| 369.680| 14.403| 1,513| 25423.871| 741.760|  59,511|
| |Assumption Parish|    20| 913.617|  6.526|   569| 25992.417| 247.982|  21,891|
| |Plaquemines Parish|    19| 819.071|  6.158|   432| 18623.098| 80.060|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   368| 23373.984| 190.549|  15,744|
| |Franklin Parish|    17| 849.363|  7.138|   875| 43717.212| 827.950|  20,015|
| |Beauregard Parish|    17| 453.370| 15.239|   814| 21708.403| 445.750|  37,497|
| |Natchitoches Parish|    17| 445.516|  3.744|   747| 19576.498| 348.176|  38,158|
| |Grant Parish|    16| 714.637| 51.045|   292| 13042.119| 165.898|  22,389|
| |West Feliciana Parish|    16| 1027.749|  9.176|   333| 21390.031| 110.116|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   861| 22456.964| 227.290|  38,340|
| |Morehouse Parish|    11| 442.229|  0.000|   479| 19257.056| 327.364|  24,874|
| |Red River Parish|    11| 1303.009| 16.922|   211| 24994.077| 676.888|   8,442|
| |Claiborne Parish|    11| 701.978|  0.000|   241| 15379.706| 246.148|  15,670|
| |Sabine Parish|    10| 418.690| 17.944|   611| 25581.980| 628.036|  23,884|
| |Concordia Parish|     9| 467.314| N/A|   300| 15577.133| N/A|  19,259|
| |Richland Parish|     7| 347.878| N/A|   577| 28675.082| N/A|  20,122|
| |Winn Parish|     7| 503.452| N/A|   410| 29487.917| N/A|  13,904|
| |Madison Parish|     6| 547.895| N/A|   601| 54880.833| N/A|  10,951|
| |West Carroll Parish|     5| 461.681| N/A|   277| 25577.101| N/A|  10,830|
| |Catahoula Parish|     5| 526.648| N/A|   276| 29070.992| N/A|   9,494|
| |Evangeline Parish|     3| 89.834| N/A|   835| 25003.743| N/A|  33,395|
| |Caldwell Parish|     2| 201.654| N/A|   207| 20871.143| N/A|   9,918|
| |LaSalle Parish|     2| 134.300| N/A|   268| 17996.240| N/A|  14,892|
| |East Carroll Parish|     1| 145.751| N/A|   514| 74916.193| N/A|   6,861|
| |St. Helena Parish|     1| 98.697| N/A|   253| 24970.391| N/A|  10,132|
| |Tensas Parish|     0|  0.000| N/A|    68| 15689.894| N/A|   4,334|
| |Cameron Parish|     0|  0.000| N/A|   167| 23949.520| N/A|   6,973|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,001| 549.685| N/A|183,656| 25231.919| N/A|7,278,717|
| |Maricopa County| 2,259| 503.632|  7.899|124,022| 27650.068| 292.058|4,485,414|
| |Pima County|   480| 458.331|  4.092|17,293| 16512.314| 192.199|1,047,279|
| |Yuma County|   276| 1291.005| 19.378|11,367| 53169.744| 404.942| 213,787|
| |Navajo County|   197| 1775.991| 12.879| 5,330| 48050.918| 190.607| 110,924|
| |Mohave County|   161| 758.786|  8.079| 3,078| 14506.483| 143.409| 212,181|
| |Pinal County|   147| 317.639|  4.630| 8,323| 17984.438| 138.292| 462,789|
| |Apache County|   138| 1919.679| 17.885| 3,119| 43387.539| 298.087|  71,887|
| |Coconino County|   115| 801.528|  0.000| 3,043| 21209.122| 109.526| 143,476|
| |Yavapai County|    65| 276.479|  3.646| 1,936|  8234.829| 144.620| 235,099|
| |Cochise County|    52| 412.954|  5.672| 1,565| 12428.329| 111.180| 125,922|
| |Santa Cruz County|    51| 1096.821|  3.072| 2,643| 56841.154| 202.774|  46,498|
| |Gila County|    36| 666.445| 18.512|   884| 16364.915| 280.330|  54,018|
| |Graham County|    12| 308.984| 14.714|   518| 13337.796| 305.305|  38,837|
| |La Paz County|    11| 521.129|  6.768|   477| 22598.067| 60.911|  21,108|
| |Greenlee County|     1| 105.285| N/A|    58|  6106.549| N/A|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 3,933| 370.429| N/A|186,828| 17596.360| N/A|10,617,423|
| |Fulton County|   410| 385.361|  3.625|19,230| 18074.378| 261.025|1,063,937|
| |Cobb County|   313| 411.766|  3.007|12,718| 16731.106| 337.907| 760,141|
| |Gwinnett County|   244| 260.614|  2.441|18,854| 20137.784| 326.988| 936,250|
| |DeKalb County|   234| 308.180|  3.951|13,237| 17433.231| 248.538| 759,297|
| |Dougherty County|   170| 1932.785|  4.873| 2,661| 30253.763| 173.788|  87,956|
| |Clayton County|   103| 352.431|  3.910| 4,790| 16389.741| 220.453| 292,256|
| |Muscogee County|    90| 459.725|  7.297| 4,514| 23057.787| 275.106| 195,769|
| |Hall County|    88| 430.442| 11.180| 5,847| 28599.938| 401.792| 204,441|
| |Richmond County|    87| 429.591|  7.054| 3,984| 19672.325| 458.513| 202,518|
| |Chatham County|    74| 255.675|  3.949| 5,441| 18799.019| 362.288| 289,430|
| |Troup County|    67| 958.211| 26.560| 2,238| 32007.094| 200.223|  69,922|
| |Bibb County|    66| 430.925|  7.462| 3,395| 22166.507| 371.230| 153,159|
| |Bartow County|    61| 566.188|  7.956| 1,772| 16447.307| 367.293| 107,738|
| |Cherokee County|    58| 224.135|  2.760| 3,155| 12192.153| 258.362| 258,773|
| |Sumter County|    56| 1896.762|  0.000|   742| 25132.096| 140.322|  29,524|
| |Houston County|    51| 323.065|  6.335| 1,871| 11852.049| 220.806| 157,863|
| |Douglas County|    50| 341.663|  2.929| 2,493| 17035.321| 283.092| 146,343|
| |Habersham County|    48| 1058.948|  3.152| 1,102| 24311.684| 315.163|  45,328|
| |Carroll County|    47| 391.693|  4.762| 1,811| 15092.673| 161.916| 119,992|
| |Upson County|    46| 1747.720|  5.428|   496| 18844.985| 195.397|  26,320|
| |Henry County|    44| 187.584|  3.045| 3,184| 13574.294| 208.901| 234,561|
| |Glynn County|    42| 492.426| 26.799| 2,422| 28396.567| 311.535|  85,292|
| |Mitchell County|    41| 1875.314|  0.000|   634| 28998.765| 261.368|  21,863|
| |Spalding County|    41| 614.665|  6.425|   893| 13387.704| 149.918|  66,703|
| |Thomas County|    41| 922.364|  6.428| 1,057| 23778.993| 466.003|  44,451|
| |Walton County|    39| 412.293| 10.572| 1,044| 11036.757| 247.678|  94,593|
| |Baldwin County|    38| 846.514|  0.000| 1,010| 22499.443| 308.691|  44,890|
| |Butts County|    37| 1483.799|  5.729|   476| 19088.868| 183.326|  24,936|
| |Lowndes County|    37| 315.146| 13.385| 3,077| 26208.201| 306.628| 117,406|
| |Newton County|    35| 313.216|  7.671| 1,693| 15150.702| 242.902| 111,744|
| |Tift County|    35| 861.136|  3.515| 1,297| 31911.229| 312.821|  40,644|
| |Hancock County|    34| 4020.338|  0.000|   298| 35237.082| 304.059|   8,457|
| |Barrow County|    32| 384.431|  0.000| 1,214| 14584.334| 315.782|  83,240|
| |Early County|    31| 3042.198|  0.000|   355| 34838.077| 224.310|  10,190|
| |Terrell County|    30| 3516.587| 16.746|   296| 34696.987| 133.965|   8,531|
| |Whitfield County|    28| 267.615|  5.462| 3,358| 32094.659| 542.056| 104,628|
| |Randolph County|    26| 3835.940|  0.000|   266| 39244.615| 421.532|   6,778|
| |Fayette County|    26| 227.231|  2.497| 1,047|  9150.418| 186.030| 114,421|
| |Monroe County|    25| 906.520| 10.360|   441| 15991.007| 191.664|  27,578|
| |Coffee County|    25| 577.727|  3.301| 1,416| 32722.483| 445.675|  43,273|
| |Ware County|    25| 699.614|  7.996| 1,113| 31146.807| 267.852|  35,734|
| |Jenkins County|    24| 2766.252| 65.863|   236| 27201.475| 214.055|   8,676|
| |Worth County|    23| 1135.971|  0.000|   440| 21731.615| 176.393|  20,247|
| |Gordon County|    23| 396.805|  0.000| 1,106| 19081.138| 364.765|  57,963|
| |Lee County|    22| 733.529|  0.000|   527| 17571.352| 147.658|  29,992|
| |Colquitt County|    22| 482.456|  3.133| 1,521| 33355.263| 238.095|  45,600|
| |Forsyth County|    22| 90.071|  1.755| 2,084|  8532.172| 168.444| 244,252|
| |Coweta County|    22| 148.139|  3.848| 1,425|  9595.378| 144.291| 148,509|
| |Columbia County|    21| 134.002|  1.823| 2,088| 13323.634| 318.141| 156,714|
| |Paulding County|    21| 124.506|  2.541| 1,578|  9355.713| 199.040| 168,667|
| |Appling County|    19| 1033.395| 23.310|   619| 33666.920| 582.742|  18,386|
| |Brooks County|    18| 1164.521| 27.727|   380| 24584.331| 231.056|  15,457|
| |Wilcox County|    18| 2084.540|  0.000|   176| 20382.166| 347.423|   8,635|
| |Turner County|    18| 2254.227|  0.000|   237| 29680.651| 375.704|   7,985|
| |Clarke County|    18| 140.262|  2.226| 1,894| 14758.710| 337.297| 128,331|
| |Rockdale County|    17| 187.027|  3.143| 1,242| 13663.968| 238.892|  90,896|
| |Putnam County|    17| 768.570|  0.000|   401| 18129.210| 297.094|  22,119|
| |Floyd County|    17| 172.592|  2.901| 1,388| 14091.657| 319.078|  98,498|
| |Harris County|    16| 454.081|  4.054|   637| 18078.102| 154.063|  35,236|
| |Walker County|    16| 229.355|  4.096|   635|  9102.507| 233.450|  69,761|
| |Oconee County|    15| 372.393|  0.000|   418| 10377.358| 177.330|  40,280|
| |Crisp County|    14| 625.782|  0.000|   370| 16538.530| 89.397|  22,372|
| |Bulloch County|    14| 175.862|  5.384| 1,175| 14759.823| 256.615|  79,608|
| |Dooly County|    14| 1045.556|  0.000|   245| 18297.237| 74.683|  13,390|
| |Jackson County|    13| 178.138|  0.000| 1,017| 13935.898| 260.356|  72,977|
| |Stephens County|    12| 462.874| 11.021|   588| 22680.810| 330.624|  25,925|
| |Peach County|    12| 435.635|  5.186|   359| 13032.745| 337.098|  27,546|
| |Lamar County|    11| 576.611| 14.977|   257| 13471.720| 299.538|  19,077|
| |Polk County|    11| 258.137| 16.762|   743| 17435.994| 432.464|  42,613|
| |Johnson County|    11| 1140.724| 44.444|   231| 23955.201| 222.219|   9,643|
| |Greene County|    11| 600.306|  0.000|   287| 15662.519| 483.363|  18,324|
| |Wilkinson County|    10| 1116.819|  0.000|   201| 22448.068| 542.455|   8,954|
| |McDuffie County|    10| 469.219|  6.703|   317| 14874.249| 301.641|  21,312|
| |Macon County|    10| 772.380|  0.000|   176| 13593.883| 66.204|  12,947|
| |Decatur County|    10| 378.730| 10.821|   728| 27571.580| 757.461|  26,404|
| |Catoosa County|     9| 133.175| N/A|   593|  8774.785| N/A|  67,580|
| |Bryan County|     9| 227.118| N/A|   608| 15343.074| N/A|  39,627|
| |Screven County|     9| 644.422| N/A|   185| 13246.456| N/A|  13,966|
| |Emanuel County|     9| 397.421| N/A|   459| 20268.480| N/A|  22,646|
| |Jeff Davis County|     8| 529.276| N/A|   418| 27654.648| N/A|  15,115|
| |Laurens County|     8| 168.258| N/A|   828| 17414.714| N/A|  47,546|
| |Burke County|     7| 312.737| N/A|   437| 19523.746| N/A|  22,383|
| |Oglethorpe County|     7| 458.746| N/A|   201| 13172.554| N/A|  15,259|
| |Toombs County|     7| 260.902| N/A|   699| 26052.926| N/A|  26,830|
| |Jefferson County|     7| 455.670| N/A|   469| 30529.879| N/A|  15,362|
| |Union County|     7| 285.586| N/A|   242|  9873.118| N/A|  24,511|
| |Telfair County|     7| 441.362| N/A|   273| 17213.115| N/A|  15,860|
| |Wayne County|     7| 233.902| N/A|   701| 23423.664| N/A|  29,927|
| |Meriwether County|     6| 283.460| N/A|   373| 17621.770| N/A|  21,167|
| |Pierce County|     6| 308.246| N/A|   387| 19881.839| N/A|  19,465|
| |Lumpkin County|     6| 178.518| N/A|   320|  9520.976| N/A|  33,610|
| |Bleckley County|     6| 466.092| N/A|   166| 12895.207| N/A|  12,873|
| |Haralson County|     6| 201.396| N/A|   206|  6914.608| N/A|  29,792|
| |Calhoun County|     6| 969.462| N/A|   200| 32315.398| N/A|   6,189|
| |Bacon County|     6| 537.442| N/A|   424| 37979.219| N/A|  11,164|
| |Cook County|     6| 347.423| N/A|   426| 24667.053| N/A|  17,270|
| |Grady County|     5| 202.980| N/A|   453| 18389.965| N/A|  24,633|
| |White County|     5| 162.348| N/A|   320| 10390.285| N/A|  30,798|
| |Madison County|     5| 167.336| N/A|   371| 12416.332| N/A|  29,880|
| |Pickens County|     5| 153.417| N/A|   341| 10463.011| N/A|  32,591|
| |Stewart County|     5| 755.173| N/A|   254| 38362.785| N/A|   6,621|
| |Seminole County|     5| 618.047| N/A|   180| 22249.691| N/A|   8,090|
| |Franklin County|     5| 214.142| N/A|   390| 16703.071| N/A|  23,349|
| |Hart County|     4| 152.643| N/A|   284| 10837.626| N/A|  26,205|
| |Gilmer County|     4| 127.514| N/A|   571| 18202.684| N/A|  31,369|
| |Heard County|     4| 335.486| N/A|   139| 11658.140| N/A|  11,923|
| |Pike County|     4| 210.948| N/A|   200| 10547.411| N/A|  18,962|
| |Marion County|     4| 478.526| N/A|   147| 17585.836| N/A|   8,359|
| |Clinch County|     4| 604.412| N/A|   181| 27349.652| N/A|   6,618|
| |Lanier County|     4| 383.767| N/A|   213| 20435.575| N/A|  10,423|
| |Camden County|     4| 73.172| N/A|   713| 13042.842| N/A|  54,666|
| |Candler County|     4| 370.268| N/A|   243| 22493.752| N/A|  10,803|
| |Brantley County|     4| 209.325| N/A|   238| 12454.864| N/A|  19,109|
| |Lincoln County|     4| 504.987| N/A|   132| 16664.563| N/A|   7,921|
| |Wilkes County|     3| 306.843| N/A|   183| 18717.398| N/A|   9,777|
| |Banks County|     3| 155.974| N/A|   255| 13257.773| N/A|  19,234|
| |Ben Hill County|     3| 179.641| N/A|   388| 23233.533| N/A|  16,700|
| |Baker County|     3| 987.492| N/A|    63| 20737.327| N/A|   3,038|
| |Treutlen County|     3| 434.720| N/A|   107| 15504.999| N/A|   6,901|
| |Charlton County|     3| 224.014| N/A|   403| 30092.593| N/A|  13,392|
| |Twiggs County|     3| 369.458| N/A|   106| 13054.187| N/A|   8,120|
| |Dawson County|     3| 114.907| N/A|   335| 12831.316| N/A|  26,108|
| |Dodge County|     3| 145.596| N/A|   201|  9754.914| N/A|  20,605|
| |Jones County|     3| 104.402| N/A|   293| 10196.624| N/A|  28,735|
| |Chattooga County|     3| 121.021| N/A|   231|  9318.649| N/A|  24,789|
| |Liberty County|     3| 48.832| N/A|   676| 11003.500| N/A|  61,435|
| |Rabun County|     3| 175.060| N/A|   203| 11845.714| N/A|  17,137|
| |Fannin County|     3| 114.556| N/A|   303| 11570.185| N/A|  26,188|
| |Talbot County|     3| 484.262| N/A|   133| 21468.927| N/A|   6,195|
| |Atkinson County|     2| 244.948| N/A|   306| 37477.036| N/A|   8,165|
| |Clay County|     2| 705.716| N/A|    85| 29992.943| N/A|   2,834|
| |Murray County|     2| 49.880| N/A|   564| 14066.241| N/A|  40,096|
| |Pulaski County|     2| 179.582| N/A|    90|  8081.171| N/A|  11,137|
| |Echols County|     2| 499.251| N/A|   217| 54168.747| N/A|   4,006|
| |Washington County|     2| 98.164| N/A|   448| 21988.809| N/A|  20,374|
| |Taylor County|     2| 249.377| N/A|    78|  9725.686| N/A|   8,020|
| |Webster County|     2| 767.165| N/A|    39| 14959.724| N/A|   2,607|
| |McIntosh County|     2| 139.101| N/A|   164| 11406.315| N/A|  14,378|
| |Long County|     1| 51.127| N/A|   114|  5828.519| N/A|  19,559|
| |Jasper County|     1| 70.328| N/A|   149| 10478.937| N/A|  14,219|
| |Chattahoochee County|     1| 91.684| N/A|   734| 67296.232| N/A|  10,907|
| |Dade County|     1| 62.050| N/A|   121|  7508.067| N/A|  16,116|
| |Effingham County|     1| 15.553| N/A|   684| 10638.298| N/A|  64,296|
| |Montgomery County|     1| 109.027| N/A|   146| 15918.011| N/A|   9,172|
| |Evans County|     1| 93.861| N/A|   236| 22151.305| N/A|  10,654|
| |Irwin County|     1| 106.202| N/A|   159| 16886.151| N/A|   9,416|
| |Tattnall County|     1| 39.548| N/A|   466| 18429.170| N/A|  25,286|
| |Wheeler County|     1| 127.307| N/A|    87| 11075.748| N/A|   7,855|
| |Warren County|     1| 190.331| N/A|    62| 11800.533| N/A|   5,254|
| |Towns County|     1| 83.077| N/A|   124| 10301.570| N/A|  12,037|
| |Quitman County|     1| 434.972| N/A|    29| 12614.180| N/A|   2,299|
| |Schley County|     1| 190.223| N/A|    58| 11032.909| N/A|   5,257|
| |Elbert County|     1| 52.100| N/A|   339| 17661.769| N/A|  19,194|
| |Taliaferro County|     0|  0.000| N/A|    12|  7807.417| N/A|   1,537|
| |Morgan County|     0|  0.000| N/A|   246| 12761.984| N/A|  19,276|
| |Miller County|     0|  0.000| N/A|   135| 23609.654| N/A|   5,718|
| |Glascock County|     0|  0.000| N/A|    24|  8078.088| N/A|   2,971|
| |Crawford County|     0|  0.000| N/A|   100|  8061.916| N/A|  12,404|
| |Berrien County|     0|  0.000| N/A|   279| 14383.668| N/A|  19,397|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,618| 309.519| N/A|97,471|  8338.623| N/A|11,689,100|
| |Franklin County|   521| 395.669|  1.519|17,834| 13543.891| 130.624|1,316,756|
| |Cuyahoga County|   491| 397.548|  3.007|13,141| 10639.866| 107.455|1,235,072|
| |Lucas County|   320| 747.056|  2.335| 5,155| 12034.607| 211.444| 428,348|
| |Mahoning County|   254| 1110.708|  3.123| 2,477| 10831.588| 79.961| 228,683|
| |Hamilton County|   252| 308.267|  1.922| 9,374| 11467.045| 87.727| 817,473|
| |Summit County|   218| 402.948|  0.528| 3,433|  6345.504| 79.745| 541,013|
| |Stark County|   137| 369.665|  3.855| 1,766|  4765.168| 56.664| 370,606|
| |Trumbull County|   105| 530.373|  5.051| 1,481|  7480.780| 77.211| 197,974|
| |Montgomery County|    87| 163.630|  4.568| 4,174|  7850.483| 88.398| 531,687|
| |Lorain County|    77| 248.521|  0.922| 1,689|  5451.324| 58.096| 309,833|
| |Butler County|    62| 161.823|  1.491| 2,822|  7365.569| 80.912| 383,134|
| |Portage County|    61| 375.463|  0.879|   743|  4573.265| 43.965| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,618| 15880.961| 99.554| 101,883|
| |Wood County|    58| 443.367|  0.000|   993|  7590.757| 153.977| 130,817|
| |Wayne County|    58| 501.253|  0.000|   519|  4485.351| 58.027| 115,710|
| |Licking County|    47| 265.744| 12.924| 1,202|  6796.259| 115.506| 176,862|
| |Ashtabula County|    45| 462.768|  1.469|   550|  5656.050| 29.382|  97,241|
| |Marion County|    45| 691.319|  6.584| 2,910| 44705.268| 120.706|  65,093|
| |Geauga County|    44| 469.840|  1.525|   548|  5851.637| 50.340|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,378| 40679.474| 87.977|  58,457|
| |Allen County|    42| 410.353|  0.000|   699|  6829.440| 133.993| 102,351|
| |Lake County|    38| 165.110|  3.104| 1,073|  4662.197| 55.864| 230,149|
| |Miami County|    37| 345.836|  1.335|   811|  7580.360| 110.828| 106,987|
| |Warren County|    36| 153.451|  1.218| 1,711|  7293.203| 118.133| 234,602|
| |Medina County|    35| 194.719|  1.590|   887|  4934.741| 73.119| 179,746|
| |Fairfield County|    31| 196.733|  8.159| 1,309|  8307.208| 119.672| 157,574|
| |Darke County|    27| 528.241|  2.795|   360|  7043.218| 145.336|  51,113|
| |Erie County|    27| 363.558|  3.847|   556|  7486.602| 130.804|  74,266|
| |Belmont County|    26| 388.025|  0.000|   592|  8835.030|  8.528|  67,006|
| |Ottawa County|    25| 616.903|  0.000|   368|  9080.814| 116.330|  40,525|
| |Washington County|    22| 367.211|  2.384|   198|  3304.902| 16.691|  59,911|
| |Delaware County|    19| 90.832|  1.366| 1,263|  6037.949| 83.320| 209,177|
| |Monroe County|    18| 1318.295| 10.463|    91|  6664.714| 20.925|  13,654|
| |Putnam County|    17| 502.053|  0.000|   199|  5876.968| 75.941|  33,861|
| |Sandusky County|    16| 273.420|  0.000|   363|  6203.220| 158.681|  58,518|
| |Clark County|    14| 104.413|  1.065| 1,115|  8315.745| 73.515| 134,083|
| |Tuscarawas County|    14| 152.195|  1.553|   762|  8283.779| 49.696|  91,987|
| |Mercer County|    13| 315.749|  0.000|   573| 13917.225| 336.567|  41,172|
| |Hardin County|    12| 382.592|  0.000|   159|  5069.345| 54.656|  31,365|
| |Clermont County|    11| 53.287|  0.692|   892|  4321.119| 69.204| 206,428|
| |Richland County|    11| 90.794|  1.179|   589|  4861.581| 94.331| 121,154|
| |Greene County|    11| 65.113|  0.000|   656|  3883.104| 48.201| 168,937|
| |Madison County|    10| 223.559|  3.194|   349|  7802.195| 130.941|  44,731|
| |Hocking County|     9| 318.426| N/A|   114|  4033.399| N/A|  28,264|
| |Wyandot County|     8| 367.444| N/A|   136|  6246.555| N/A|  21,772|
| |Knox County|     7| 112.320| N/A|   191|  3064.728| N/A|  62,322|
| |Guernsey County|     7| 180.064| N/A|   114|  2932.476| N/A|  38,875|
| |Clinton County|     6| 142.966| N/A|   158|  3764.773| N/A|  41,968|
| |Holmes County|     6| 136.488| N/A|   326|  7415.833| N/A|  43,960|
| |Coshocton County|     6| 163.934| N/A|   188|  5136.612| N/A|  36,600|
| |Huron County|     5| 85.813| N/A|   388|  6659.115| N/A|  58,266|
| |Carroll County|     5| 185.777| N/A|   110|  4087.092| N/A|  26,914|
| |Auglaize County|     5| 109.515| N/A|   239|  5234.799| N/A|  45,656|
| |Crawford County|     5| 120.499| N/A|   171|  4121.078| N/A|  41,494|
| |Shelby County|     4| 82.321| N/A|   177|  3642.725| N/A|  48,590|
| |Ross County|     4| 52.174| N/A|   444|  5791.355| N/A|  76,666|
| |Defiance County|     4| 105.023| N/A|   133|  3492.005| N/A|  38,087|
| |Williams County|     3| 81.762| N/A|   130|  3543.007| N/A|  36,692|
| |Ashland County|     3| 56.092| N/A|   137|  2561.514| N/A|  53,484|
| |Perry County|     3| 83.024| N/A|   116|  3210.273| N/A|  36,134|
| |Seneca County|     3| 54.369| N/A|   190|  3443.401| N/A|  55,178|
| |Hancock County|     3| 39.587| N/A|   353|  4658.037| N/A|  75,783|
| |Logan County|     2| 43.791| N/A|   140|  3065.335| N/A|  45,672|
| |Henry County|     2| 74.058| N/A|   113|  4184.255| N/A|  27,006|
| |Jefferson County|     2| 30.616| N/A|   219|  3352.468| N/A|  65,325|
| |Morrow County|     2| 56.612| N/A|   165|  4670.516| N/A|  35,328|
| |Preble County|     2| 48.921| N/A|   176|  4305.073| N/A|  40,882|
| |Vinton County|     2| 152.847| N/A|    30|  2292.702| N/A|  13,085|
| |Brown County|     2| 46.049| N/A|   123|  2832.013| N/A|  43,432|
| |Adams County|     2| 72.207| N/A|    59|  2130.118| N/A|  27,698|
| |Athens County|     1| 15.308| N/A|   353|  5403.585| N/A|  65,327|
| |Champaign County|     1| 25.717| N/A|   157|  4037.547| N/A|  38,885|
| |Van Wert County|     1| 35.367| N/A|    70|  2475.685| N/A|  28,275|
| |Fulton County|     1| 23.738| N/A|   144|  3418.316| N/A|  42,126|
| |Gallia County|     1| 33.447| N/A|    62|  2073.717| N/A|  29,898|
| |Harrison County|     1| 66.489| N/A|    22|  1462.766| N/A|  15,040|
| |Highland County|     1| 23.169| N/A|   146|  3382.683| N/A|  43,161|
| |Muskingum County|     1| 11.599| N/A|   215|  2493.766| N/A|  86,215|
| |Scioto County|     1| 13.278| N/A|   211|  2801.604| N/A|  75,314|
| |Union County|     1| 16.953| N/A|   233|  3949.956| N/A|  58,988|
| |Fayette County|     0|  0.000| N/A|   109|  3821.209| N/A|  28,525|
| |Jackson County|     0|  0.000| N/A|    73|  2252.183| N/A|  32,413|
| |Lawrence County|     0|  0.000| N/A|   242|  4069.758| N/A|  59,463|
| |Pike County|     0|  0.000| N/A|    75|  2700.562| N/A|  27,772|
| |Paulding County|     0|  0.000| N/A|    64|  3427.592| N/A|  18,672|
| |Noble County|     0|  0.000| N/A|    17|  1178.591| N/A|  14,424|
| |Morgan County|     0|  0.000| N/A|    23|  1585.332| N/A|  14,508|
| |Meigs County|     0|  0.000| N/A|    33|  1440.608| N/A|  22,907|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,535| 584.715| N/A|93,005| 15383.712| N/A|6,045,680|
| |Baltimore County|   979| 1183.267|  4.835|24,852| 30037.347| 385.559| 827,370|
| |Montgomery County|   797| 758.551|  1.088|18,032| 17162.088| 86.338|1,050,688|
| |Prince George's County|   748| 822.586|  2.199|23,225| 25540.867| 163.700| 909,327|
| |Anne Arundel County|   220| 379.812|  0.987| 7,200| 12430.210| 127.262| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,032| 11681.892| 37.428| 259,547|
| |Carroll County|   117| 694.580|  0.848| 1,516|  8999.863| 68.695| 168,447|
| |Howard County|   106| 325.463|  0.439| 3,729| 11449.538| 112.728| 325,690|
| |Charles County|    91| 557.403|  0.875| 1,961| 12011.736| 124.256| 163,257|
| |Harford County|    69| 270.121|  1.119| 1,906|  7461.606| 106.259| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   951|  8378.116| 96.908| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,322| 12759.509| 73.077| 103,609|
| |Washington County|    31| 205.231|  0.946|   996|  6593.887| 56.746| 151,049|
| |Cecil County|    30| 291.673|  0.000|   681|  6620.971| 86.113| 102,855|
| |Calvert County|    28| 302.621|  1.544|   667|  7208.862| 157.486|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   406|  8058.594| 79.395|  50,381|
| |Kent County|    23| 1184.224|  0.000|   236| 12151.169| 51.488|  19,422|
| |Worcester County|    20| 382.585|  5.465|   664| 12701.813| 398.981|  52,276|
| |Allegany County|    18| 255.624|  0.000|   279|  3962.168| 30.431|  70,416|
| |Dorchester County|     5| 156.597| N/A|   360| 11275.016| N/A|  31,929|
| |Talbot County|     4| 107.582| N/A|   371|  9978.215| N/A|  37,181|
| |Caroline County|     3| 89.804| N/A|   444| 13291.026| N/A|  33,406|
| |Somerset County|     3| 117.114| N/A|   130|  5074.953| N/A|  25,616|
| |Baltimore city|     0|  0.000| N/A|     0|     0.000| N/A| 593,490|
| |Garrett County|     0|  0.000| N/A|    45|  1550.975| N/A|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,811| 417.544| N/A|71,015| 10548.528| N/A|6,732,219|
| |Marion County|   723| 749.547|  0.889|15,322| 15884.601| 155.804| 964,582|
| |Lake County|   274| 564.375|  2.354| 7,343| 15124.832| 136.827| 485,493|
| |Allen County|   160| 421.831|  1.883| 3,725|  9820.748| 92.275| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,694| 10710.199| 84.901| 158,167|
| |Hendricks County|   106| 622.391|  0.839| 1,814| 10651.103| 109.883| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,610|  7721.642| 103.124| 338,011|
| |Elkhart County|    80| 387.708|  3.462| 4,713| 22840.831| 170.314| 206,341|
| |St. Joseph County|    79| 290.627|  0.526| 3,301| 12143.798| 175.532| 271,826|
| |Howard County|    65| 787.459|  3.461|   855| 10358.112| 134.993|  82,544|
| |Madison County|    65| 501.663|  1.103|   895|  6907.516| 116.871| 129,569|
| |Delaware County|    52| 455.601|  0.000|   680|  5957.857| 103.887| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   754|  8999.869| 66.501|  83,779|
| |Boone County|    46| 678.036|  2.106|   653|  9625.164| 92.651|  67,843|
| |Clark County|    46| 388.835|  1.208| 1,148|  9703.978| 185.965| 118,302|
| |Floyd County|    45| 573.088|  1.819|   740|  9424.110| 189.210|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,238|  7265.727| 98.095| 170,389|
| |Hancock County|    38| 486.132|  1.828|   638|  8161.908| 85.896|  78,168|
| |Morgan County|    34| 482.345|  4.053|   451|  6398.161| 87.146|  70,489|
| |Greene County|    34| 1065.096|  0.000|   241|  7549.652| 44.752|  31,922|
| |Decatur County|    32| 1204.865|  0.000|   324| 12199.254| 107.577|  26,559|
| |Monroe County|    30| 202.114|  0.000|   708|  4769.893| 53.897| 148,431|
| |Warrick County|    30| 476.206|  2.268|   553|  8778.056| 215.426|  62,998|
| |LaPorte County|    30| 273.005|  1.300|   869|  7908.052| 106.602| 109,888|
| |Noble County|    29| 607.406|  2.992|   645| 13509.551| 95.749|  47,744|
| |Grant County|    29| 440.937|  0.000|   520|  7906.460| 69.507|  65,769|
| |Dearborn County|    28| 566.137|  2.888|   479|  9684.985| 109.761|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   337|  7427.816| 81.867|  45,370|
| |Shelby County|    27| 603.635|  3.194|   535| 11960.920| 114.978|  44,729|
| |Orange County|    24| 1221.623|  0.000|   166|  8449.557| 58.173|  19,646|
| |Harrison County|    23| 567.691|  3.526|   309|  7626.805| 144.567|  40,515|
| |Marshall County|    22| 475.593|  3.088|   758| 16386.355| 111.178|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   346|  9024.988| 74.525|  38,338|
| |Daviess County|    20| 599.682|  4.283|   259|  7765.884| 149.921|  33,351|
| |Henry County|    19| 396.064|  2.978|   369|  7691.987| 44.669|  47,972|
| |Franklin County|    13| 571.228| 31.386|   234| 10282.099| 295.030|  22,758|
| |Vanderburgh County|    13| 71.645|  3.937| 1,842| 10151.501| 207.061| 181,451|
| |Dubois County|    12| 280.794|  6.686|   658| 15396.855| 237.338|  42,736|
| |Jennings County|    12| 432.666|  0.000|   215|  7751.938| 61.809|  27,735|
| |Kosciusko County|    12| 151.027|  1.798|   827| 10408.276| 70.120|  79,456|
| |Perry County|    12| 626.011|  0.000|   179|  9337.994| 67.073|  19,169|
| |Tippecanoe County|    11| 56.199|  0.000| 1,146|  5854.945| 83.934| 195,732|
| |Scott County|    10| 418.883|  0.000|   257| 10765.300| 125.665|  23,873|
| |White County|    10| 414.903|  0.000|   351| 14563.107| 100.762|  24,102|
| |LaGrange County|    10| 252.436|  0.000|   554| 13984.955| 68.518|  39,614|
| |Newton County|    10| 715.103|  0.000|   114|  8152.174| 61.295|  13,984|
| |Wayne County|    10| 151.782|  4.337|   346|  5251.654| 117.089|  65,884|
| |Vigo County|    10| 93.425|  0.000|   543|  5072.965| 182.846| 107,038|
| |Cass County|     9| 238.796| N/A| 1,766| 46857.173| N/A|  37,689|
| |Putnam County|     8| 212.902| N/A|   277|  7371.727| N/A|  37,576|
| |Starke County|     7| 304.414| N/A|   174|  7566.862| N/A|  22,995|
| |Ripley County|     7| 247.140| N/A|   194|  6849.315| N/A|  28,324|
| |Fayette County|     7| 303.004| N/A|   177|  7661.674| N/A|  23,102|
| |Tipton County|     6| 396.092| N/A|   129|  8515.976| N/A|  15,148|
| |Whitley County|     6| 176.658| N/A|   147|  4328.112| N/A|  33,964|
| |Jackson County|     5| 113.043| N/A|   562| 12706.021| N/A|  44,231|
| |Clay County|     5| 190.658| N/A|   104|  3965.682| N/A|  26,225|
| |Ohio County|     4| 680.851| N/A|    57|  9702.128| N/A|   5,875|
| |Randolph County|     4| 162.173| N/A|   114|  4621.934| N/A|  24,665|
| |Rush County|     4| 241.240| N/A|    71|  4282.010| N/A|  16,581|
| |Gibson County|     4| 118.839| N/A|   208|  6179.625| N/A|  33,659|
| |DeKalb County|     4| 92.007| N/A|   223|  5129.385| N/A|  43,475|
| |Huntington County|     3| 82.147| N/A|   121|  3313.253| N/A|  36,520|
| |Wabash County|     3| 96.787| N/A|   161|  5194.219| N/A|  30,996|
| |Steuben County|     3| 86.720| N/A|   204|  5896.976| N/A|  34,594|
| |Spencer County|     3| 147.951| N/A|   119|  5868.718| N/A|  20,277|
| |Clinton County|     3| 92.595| N/A|   404| 12469.521| N/A|  32,399|
| |Adams County|     2| 55.902| N/A|    89|  2487.632| N/A|  35,777|
| |Blackford County|     2| 170.097| N/A|    59|  5017.860| N/A|  11,758|
| |Carroll County|     2| 98.731| N/A|   157|  7750.407| N/A|  20,257|
| |Fountain County|     2| 122.354| N/A|    64|  3915.331| N/A|  16,346|
| |Wells County|     2| 70.681| N/A|   154|  5442.465| N/A|  28,296|
| |Fulton County|     2| 100.130| N/A|   159|  7960.348| N/A|  19,974|
| |Jasper County|     2| 59.591| N/A|   219|  6525.237| N/A|  33,562|
| |Jefferson County|     2| 61.904| N/A|   153|  4735.669| N/A|  32,308|
| |Miami County|     2| 56.313| N/A|   264|  7433.270| N/A|  35,516|
| |Brown County|     1| 66.260| N/A|    71|  4704.479| N/A|  15,092|
| |Warren County|     1| 120.992| N/A|    20|  2419.843| N/A|   8,265|
| |Sullivan County|     1| 48.382| N/A|    91|  4402.729| N/A|  20,669|
| |Pulaski County|     1| 80.952| N/A|    75|  6071.400| N/A|  12,353|
| |Parke County|     1| 59.042| N/A|    50|  2952.117| N/A|  16,937|
| |Owen County|     1| 48.079| N/A|    83|  3990.576| N/A|  20,799|
| |Washington County|     1| 35.668| N/A|   121|  4315.880| N/A|  28,036|
| |Martin County|     0|  0.000| N/A|    42|  4095.563| N/A|  10,255|
| |Pike County|     0|  0.000| N/A|    52|  4197.272| N/A|  12,389|
| |Posey County|     0|  0.000| N/A|   165|  6489.165| N/A|  25,427|
| |Switzerland County|     0|  0.000| N/A|    44|  4092.643| N/A|  10,751|
| |Vermillion County|     0|  0.000| N/A|    48|  3097.174| N/A|  15,498|
| |Union County|     0|  0.000| N/A|    35|  4961.724| N/A|   7,054|
| |Knox County|     0|  0.000| N/A|   142|  3880.418| N/A|  36,594|
| |Jay County|     0|  0.000| N/A|    84|  4110.393| N/A|  20,436|
| |Crawford County|     0|  0.000| N/A|    44|  4159.970| N/A|  10,577|
| |Benton County|     0|  0.000| N/A|    60|  6858.711| N/A|   8,748|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,299| 269.345| N/A|95,867| 11231.537| N/A|8,535,519|
| |Fairfax County|   534| 465.347|  0.996|16,168| 14089.367| 59.880|1,147,532|
| |Henrico County|   182| 550.151|  1.727| 3,742| 11311.355| 100.616| 330,818|
| |Prince William County|   177| 376.328|  2.430| 9,163| 19481.859| 115.116| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,013| 12721.561| 83.841| 236,842|
| |Loudoun County|   115| 278.088|  2.073| 5,150| 12453.511| 56.999| 413,538|
| |Chesterfield County|    77| 218.253|  2.430| 4,216| 11950.046| 137.268| 352,802|
| |Alexandria city|    60| 376.345|  2.688| 2,887| 18108.488| 96.775| 159,428|
| |Virginia Beach city|    52| 115.562|  2.857| 4,658| 10351.709| 215.568| 449,974|
| |Suffolk city|    49| 531.984|  1.551| 1,184| 12854.475| 283.828|  92,108|
| |Richmond County|    45| 4987.255| 47.498| 3,385| 375152.388| 3340.669|   9,023|
| |Shenandoah County|    43| 985.877|  9.826|   689| 15796.955| 78.608|  43,616|
| |Chesapeake city|    37| 151.122|  5.835| 2,761| 11276.982| 215.889| 244,835|
| |Spotsylvania County|    35| 256.947|  2.098| 1,421| 10432.038| 136.339| 136,215|
| |Mecklenburg County|    32| 1046.196|  4.671|   360| 11769.706| 266.220|  30,587|
| |Hanover County|    32| 296.940|  2.651|   615|  5706.809| 42.420| 107,766|
| |Harrisonburg city|    30| 565.867|  2.695| 1,070| 20182.586| 88.922|  53,016|
| |Norfolk city|    29| 119.468|  4.120| 3,496| 14402.122| 244.822| 242,742|
| |Northampton County|    29| 2476.516| 12.200|   295| 25192.143| 36.599|  11,710|
| |Portsmouth city|    25| 264.836|  4.540| 1,676| 17754.613| 391.957|  94,398|
| |Galax city|    24| 3781.314| 157.555|   342| 53883.725| 292.602|   6,347|
| |Page County|    24| 1004.100|  0.000|   335| 14015.564| 23.907|  23,902|
| |Colonial Heights city|    21| 1208.981|  0.000|   189| 10880.829| 98.692|  17,370|
| |Manassas city|    20| 486.796|  0.000| 1,625| 39552.148| 100.836|  41,085|
| |Petersburg city|    19| 606.138| 41.017|   493| 15727.685| 305.348|  31,346|
| |Rockingham County|    18| 219.651|  1.743|   925| 11287.646| 73.217|  81,948|
| |Roanoke County|    18| 191.111|  1.517| 1,444| 15331.366| 324.586|  94,186|
| |Newport News city|    18| 100.432|  1.594| 1,736|  9686.149| 153.040| 179,225|
| |James City County|    16| 209.087|  0.000|   575|  7514.081| 82.142|  76,523|
| |Albemarle County|    16| 146.346|  7.840|   798|  7299.003| 84.933| 109,330|
| |Accomack County|    16| 495.111|  4.421| 1,085| 33574.700| 48.627|  32,316|
| |Emporia city|    15| 2805.836|  0.000|   172| 32173.588| 240.500|   5,346|
| |Charlottesville city|    15| 317.353| 18.134|   505| 10684.213| 163.210|  47,266|
| |Southampton County|    13| 737.338|  8.103|   249| 14122.852| 162.052|  17,631|
| |Carroll County|    12| 402.806|  4.795|   309| 10372.260| 19.181|  29,791|
| |Culpeper County|    12| 228.115|  0.000|   977| 18572.379| 105.911|  52,605|
| |Greensville County|    11| 970.360| 25.204|   441| 38902.611| 327.654|  11,336|
| |Nottoway County|    10| 656.513| 18.758|   178| 11685.924| 84.409|  15,232|
| |Prince Edward County|    10| 438.558|  6.265|   389| 17059.907| 557.595|  22,802|
| |Sussex County|     9| 806.524| N/A|   283| 25360.695| N/A|  11,159|
| |Isle of Wight County|     9| 242.529| N/A|   370|  9970.627| N/A|  37,109|
| |Fauquier County|     9| 126.365| N/A|   592|  8312.038| N/A|  71,222|
| |Frederick County|     9| 100.769| N/A|   675|  7557.690| N/A|  89,313|
| |Fluvanna County|     9| 330.033| N/A|   179|  6563.990| N/A|  27,270|
| |Buckingham County|     8| 466.527| N/A|   598| 34872.871| N/A|  17,148|
| |Stafford County|     8| 52.328| N/A| 1,316|  8607.946| N/A| 152,882|
| |Franklin County|     7| 124.906| N/A|   321|  5727.847| N/A|  56,042|
| |Hampton city|     7| 52.041| N/A| 1,131|  8408.297| N/A| 134,510|
| |Goochland County|     7| 294.700| N/A|   157|  6609.691| N/A|  23,753|
| |Dinwiddie County|     7| 245.235| N/A|   211|  7392.096| N/A|  28,544|
| |Danville city|     7| 174.808| N/A|   362|  9040.056| N/A|  40,044|
| |Bedford County|     7| 88.611| N/A|   327|  4139.398| N/A|  78,997|
| |Henry County|     7| 138.458| N/A|   543| 10740.352| N/A|  50,557|
| |Manassas Park city|     7| 400.503| N/A|   506| 28950.681| N/A|  17,478|
| |Botetourt County|     7| 209.462| N/A|   200|  5984.620| N/A|  33,419|
| |Williamsburg city|     6| 401.230| N/A|   119|  7957.737| N/A|  14,954|
| |Falls Church city|     6| 410.481| N/A|    60|  4104.809| N/A|  14,617|
| |Warren County|     6| 149.388| N/A|   353|  8788.965| N/A|  40,164|
| |Caroline County|     5| 162.734| N/A|   194|  6314.076| N/A|  30,725|
| |Charles City County|     5| 718.081| N/A|    51|  7324.429| N/A|   6,963|
| |Grayson County|     5| 321.543| N/A|   145|  9324.759| N/A|  15,550|
| |Hopewell city|     5| 221.936| N/A|   260| 11540.681| N/A|  22,529|
| |Washington County|     5| 93.041| N/A|   203|  3777.447| N/A|  53,740|
| |Alleghany County|     4| 269.179| N/A|    58|  3903.096| N/A|  14,860|
| |Augusta County|     4| 52.939| N/A|   261|  3454.300| N/A|  75,558|
| |Patrick County|     4| 227.169| N/A|   126|  7155.838| N/A|  17,608|
| |Winchester city|     4| 142.460| N/A|   396| 14103.569| N/A|  28,078|
| |Powhatan County|     4| 134.898| N/A|   135|  4552.813| N/A|  29,652|
| |Lynchburg city|     4| 48.681| N/A|   514|  6255.477| N/A|  82,168|
| |King George County|     4| 149.054| N/A|   125|  4657.922| N/A|  26,836|
| |York County|     4| 58.582| N/A|   338|  4950.205| N/A|  68,280|
| |Pulaski County|     3| 88.165| N/A|    82|  2409.851| N/A|  34,027|
| |Montgomery County|     3| 30.446| N/A|   296|  3004.009| N/A|  98,535|
| |Orange County|     3| 80.969| N/A|   222|  5991.741| N/A|  37,051|
| |Scott County|     3| 139.108| N/A|    66|  3060.373| N/A|  21,566|
| |Smyth County|     3| 99.655| N/A|   130|  4318.363| N/A|  30,104|
| |Wythe County|     3| 104.588| N/A|   108|  3765.165| N/A|  28,684|
| |Westmoreland County|     3| 166.528| N/A|   197| 10935.332| N/A|  18,015|
| |Wise County|     3| 80.250| N/A|   110|  2942.514| N/A|  37,383|
| |Fredericksburg city|     3| 103.320| N/A|   388| 13362.722| N/A|  29,036|
| |Martinsville city|     3| 238.968| N/A|   184| 14656.683| N/A|  12,554|
| |Salem city|     3| 118.572| N/A|   153|  6047.192| N/A|  25,301|
| |Waynesboro city|     3| 132.567| N/A|   167|  7379.585| N/A|  22,630|
| |Russell County|     2| 75.228| N/A|    91|  3422.854| N/A|  26,586|
| |Surry County|     2| 311.429| N/A|    44|  6851.448| N/A|   6,422|
| |Prince George County|     2| 52.147| N/A|   357|  9308.268| N/A|  38,353|
| |Northumberland County|     2| 165.358| N/A|    69|  5704.837| N/A|  12,095|
| |King William County|     2| 116.632| N/A|    79|  4606.951| N/A|  17,148|
| |Rappahannock County|     2| 271.370| N/A|    41|  5563.094| N/A|   7,370|
| |Pittsylvania County|     2| 33.138| N/A|   392|  6495.013| N/A|  60,354|
| |Louisa County|     2| 53.204| N/A|   174|  4628.768| N/A|  37,591|
| |Campbell County|     2| 36.440| N/A|   176|  3206.705| N/A|  54,885|
| |Brunswick County|     2| 123.221| N/A|   216| 13307.868| N/A|  16,231|
| |Greene County|     2| 100.913| N/A|   153|  7719.865| N/A|  19,819|
| |Gloucester County|     2| 53.550| N/A|   147|  3935.954| N/A|  37,348|
| |Amelia County|     2| 152.149| N/A|    77|  5857.741| N/A|  13,145|
| |Rockbridge County|     1| 44.301| N/A|    66|  2923.847| N/A|  22,573|
| |Buena Vista city|     1| 154.369| N/A|    50|  7718.432| N/A|   6,478|
| |Floyd County|     1| 63.496| N/A|    43|  2730.332| N/A|  15,749|
| |Middlesex County|     1| 94.500| N/A|    33|  3118.503| N/A|  10,582|
| |New Kent County|     1| 43.307| N/A|   122|  5283.444| N/A|  23,091|
| |Madison County|     1| 75.409| N/A|    64|  4826.182| N/A|  13,261|
| |Essex County|     1| 91.299| N/A|    84|  7669.132| N/A|  10,953|
| |Dickenson County|     1| 69.842| N/A|    38|  2654.002| N/A|  14,318|
| |Halifax County|     1| 29.489| N/A|   145|  4275.899| N/A|  33,911|
| |King and Queen County|     1| 142.349| N/A|    37|  5266.904| N/A|   7,025|
| |Lee County|     1| 42.693| N/A|   105|  4482.773| N/A|  23,423|
| |Lunenburg County|     1| 81.994| N/A|    58|  4755.658| N/A|  12,196|
| |Highland County|     0|  0.000| N/A|     4|  1826.484| N/A|   2,190|
| |Tazewell County|     0|  0.000| N/A|   106|  2611.159| N/A|  40,595|
| |Bristol city|     0|  0.000| N/A|    71|  4235.771| N/A|  16,762|
| |Covington city|     0|  0.000| N/A|    13|  2347.418| N/A|   5,538|
| |Fairfax city|     0|  0.000| N/A|     0|     0.000| N/A|  24,019|
| |Franklin city|     0|  0.000| N/A|     0|     0.000| N/A|   7,967|
| |Amherst County|     0|  0.000| N/A|   137|  4334.757| N/A|  31,605|
| |Giles County|     0|  0.000| N/A|    23|  1375.598| N/A|  16,720|
| |Clarke County|     0|  0.000| N/A|    69|  4719.885| N/A|  14,619|
| |Craig County|     0|  0.000| N/A|    17|  3313.194| N/A|   5,131|
| |Cumberland County|     0|  0.000| N/A|    72|  7249.295| N/A|   9,932|
| |Lexington city|     0|  0.000| N/A|    33|  4431.910| N/A|   7,446|
| |Norton city|     0|  0.000| N/A|    15|  3767.898| N/A|   3,981|
| |Lancaster County|     0|  0.000| N/A|    32|  3018.014| N/A|  10,603|
| |Mathews County|     0|  0.000| N/A|    16|  1811.184| N/A|   8,834|
| |Nelson County|     0|  0.000| N/A|    36|  2411.253| N/A|  14,930|
| |Charlotte County|     0|  0.000| N/A|    50|  4208.754| N/A|  11,880|
| |Roanoke city|     0|  0.000| N/A|     0|     0.000| N/A|  99,143|
| |Richmond city|     0|  0.000| N/A|     0|     0.000| N/A| 230,436|
| |Staunton city|     0|  0.000| N/A|   143|  5735.601| N/A|  24,932|
| |Appomattox County|     0|  0.000| N/A|    77|  4839.419| N/A|  15,911|
| |Buchanan County|     0|  0.000| N/A|    74|  3523.138| N/A|  21,004|
| |Poquoson city|     0|  0.000| N/A|    41|  3341.211| N/A|  12,271|
| |Bland County|     0|  0.000| N/A|     9|  1433.121| N/A|   6,280|
| |Bath County|     0|  0.000| N/A|     4|   964.553| N/A|   4,147|
| |Radford city|     0|  0.000| N/A|    36|  1972.711| N/A|  18,249|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,126| 202.706| N/A|131,802| 12566.833| N/A|10,488,084|
| |Mecklenburg County|   222| 199.936|  3.474|21,704| 19546.884| 185.655|1,110,356|
| |Guilford County|   153| 284.824|  2.925| 5,428| 10104.733| 102.654| 537,174|
| |Wake County|   152| 136.720|  3.341|11,576| 10412.310| 114.619|1,111,761|
| |Durham County|    79| 245.732|  0.889| 6,038| 18781.416| 155.971| 321,488|
| |Henderson County|    54| 459.899|  1.217| 1,452| 12366.182| 154.516| 117,417|
| |Robeson County|    53| 405.742|  3.281| 2,726| 20868.900| 213.260| 130,625|
| |Chatham County|    52| 698.268|  5.755| 1,274| 17107.560| 141.956|  74,470|
| |Forsyth County|    51| 133.405|  0.747| 5,091| 13316.941| 112.105| 382,295|
| |Cumberland County|    51| 152.008|  0.426| 3,021|  9004.229| 196.290| 335,509|
| |Cabarrus County|    49| 226.377|  5.280| 2,520| 11642.250| 134.638| 216,453|
| |Rowan County|    48| 337.819|  2.011| 2,123| 14941.445| 183.991| 142,088|
| |Duplin County|    48| 817.146| 14.592| 1,966| 33468.957| 160.511|  58,741|
| |Columbus County|    48| 864.740| 10.295|   864| 15565.324| 167.286|  55,508|
| |Gaston County|    47| 209.327|  8.908| 3,222| 14350.039| 228.415| 224,529|
| |Johnston County|    46| 219.739|  1.365| 3,173| 15157.233| 189.713| 209,339|
| |Buncombe County|    46| 176.116|  0.000| 1,785|  6834.079| 114.312| 261,191|
| |Orange County|    46| 309.814|  0.962| 1,316|  8863.385| 63.502| 148,476|
| |Union County|    42| 175.103|  1.787| 2,975| 12403.120| 181.059| 239,859|
| |Alamance County|    41| 241.875|  0.000| 2,343| 13822.275| 203.950| 169,509|
| |Wayne County|    40| 324.857|  3.481| 2,372| 19264.036| 100.938| 123,131|
| |Vance County|    40| 898.170|  0.000|   751| 16863.141| 131.518|  44,535|
| |Harnett County|    39| 286.815|  3.152| 1,219|  8964.817| 152.338| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,125| 14791.149| 125.290| 143,667|
| |Wilson County|    35| 427.868|  3.493| 1,476| 18043.789| 206.075|  81,801|
| |Catawba County|    29| 181.760|  4.477| 2,018| 12647.993| 169.225| 159,551|
| |Burke County|    28| 309.444|  4.736| 1,637| 18091.396| 175.246|  90,485|
| |Granville County|    27| 446.702|  4.727| 1,209| 20002.316| 167.809|  60,443|
| |Franklin County|    25| 358.757|  0.000|   828| 11882.041| 166.053|  69,685|
| |Stanly County|    24| 382.129| 31.844| 1,000| 15922.046| 332.088|  62,806|
| |Moore County|    20| 198.255|  0.000|   968|  9595.559| 155.772| 100,880|
| |New Hanover County|    20| 85.298|  1.219| 2,566| 10943.691| 172.423| 234,473|
| |Pasquotank County|    19| 477.099|  7.174|   371|  9315.990| 125.552|  39,824|
| |Brunswick County|    19| 133.035|  3.001| 1,231|  8619.241| 81.021| 142,820|
| |Cleveland County|    18| 183.773|  7.293| 1,128| 11516.432| 280.035|  97,947|
| |Iredell County|    18| 99.007|  0.000| 1,771|  9741.153| 130.437| 181,806|
| |Davidson County|    18| 107.393|  0.852| 1,709| 10196.350| 87.789| 167,609|
| |Northampton County|    16| 821.229|  0.000|   329| 16886.516| 161.313|  19,483|
| |Caldwell County|    14| 170.362|  3.477| 1,179| 14346.905| 196.438|  82,178|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 425.843|  27,173|
| |Rutherford County|    14| 208.865|  2.131|   696| 10383.565| 164.108|  67,029|
| |McDowell County|    13| 284.116| 15.611|   662| 14468.048| 384.025|  45,756|
| |Sampson County|    13| 204.625|  4.497| 1,453| 22870.725| 114.680|  63,531|
| |Nash County|    12| 127.256|  1.515| 1,109| 11760.589| 221.183|  94,298|
| |Lenoir County|    12| 214.481|  0.000|   553|  9884.002| 107.241|  55,949|
| |Edgecombe County|    12| 233.136|  2.775|   616| 11967.672| 155.424|  51,472|
| |Lee County|    11| 178.054|  4.625| 1,253| 20281.973| 298.298|  61,779|
| |Hertford County|    11| 464.586|  0.000|   313| 13219.580| 289.612|  23,677|
| |Pitt County|    11| 60.860|  0.000| 1,875| 10373.903| 186.533| 180,742|
| |Craven County|    11| 107.696|  2.797|   695|  6804.453| 104.899| 102,139|
| |Onslow County|    10| 50.521|  0.000| 1,015|  5127.868| 127.746| 197,938|
| |Wilkes County|    10| 146.173|  2.088|   762| 11138.397| 85.616|  68,412|
| |Haywood County|    10| 160.470| 18.339|   375|  6017.620| 245.290|  62,317|
| |Surry County|     9| 125.378| N/A|   897| 12495.995| N/A|  71,783|
| |Richmond County|     9| 200.763| N/A|   498| 11108.880| N/A|  44,829|
| |Hoke County|     9| 162.943| N/A|   703| 12727.668| N/A|  55,234|
| |Bladen County|     7| 213.923| N/A|   606| 18519.650| N/A|  32,722|
| |Rockingham County|     7| 76.915| N/A|   509|  5592.792| N/A|  91,010|
| |Warren County|     7| 354.772| N/A|   254| 12873.144| N/A|  19,731|
| |Davie County|     6| 140.036| N/A|   403|  9405.779| N/A|  42,846|
| |Halifax County|     6| 119.976| N/A|   668| 13357.329| N/A|  50,010|
| |Carteret County|     6| 86.364| N/A|   332|  4778.835| N/A|  69,473|
| |Yadkin County|     6| 159.291| N/A|   524| 13911.381| N/A|  37,667|
| |Martin County|     6| 267.380| N/A|   257| 11452.763| N/A|  22,440|
| |Polk County|     5| 241.266| N/A|   148|  7141.478| N/A|  20,724|
| |Bertie County|     5| 263.894| N/A|   263| 13880.825| N/A|  18,947|
| |Jackson County|     5| 113.797| N/A|   436|  9923.073| N/A|  43,938|
| |Washington County|     4| 345.423| N/A|   131| 11312.608| N/A|  11,580|
| |Jones County|     4| 424.674| N/A|    79|  8387.302| N/A|   9,419|
| |Pender County|     3| 47.574| N/A|   638| 10117.349| N/A|  63,060|
| |Cherokee County|     3| 104.851| N/A|   265|  9261.848| N/A|  28,612|
| |Stokes County|     3| 65.802| N/A|   282|  6185.431| N/A|  45,591|
| |Lincoln County|     3| 34.839| N/A|   802|  9313.560| N/A|  86,111|
| |Greene County|     3| 142.389| N/A|   322| 15283.117| N/A|  21,069|
| |Macon County|     3| 83.663| N/A|   460| 12828.379| N/A|  35,858|
| |Anson County|     2| 81.813| N/A|   318| 13008.263| N/A|  24,446|
| |Mitchell County|     2| 133.654| N/A|   116|  7751.938| N/A|  14,964|
| |Beaufort County|     2| 42.559| N/A|   391|  8320.211| N/A|  46,994|
| |Dare County|     2| 54.041| N/A|   205|  5539.193| N/A|  37,009|
| |Caswell County|     2| 88.480| N/A|   191|  8449.832| N/A|  22,604|
| |Camden County|     2| 184.043| N/A|    65|  5981.412| N/A|  10,867|
| |Scotland County|     2| 57.433| N/A|   320|  9189.329| N/A|  34,823|
| |Perquimans County|     2| 148.555| N/A|    76|  5645.101| N/A|  13,463|
| |Swain County|     2| 140.144| N/A|   107|  7497.723| N/A|  14,271|
| |Person County|     2| 50.646| N/A|   203|  5140.542| N/A|  39,490|
| |Gates County|     2| 172.980| N/A|    45|  3892.060| N/A|  11,562|
| |Alexander County|     2| 53.338| N/A|   295|  7867.296| N/A|  37,497|
| |Ashe County|     1| 36.761| N/A|   142|  5220.012| N/A|  27,203|
| |Pamlico County|     1| 78.579| N/A|    67|  5264.812| N/A|  12,726|
| |Chowan County|     1| 71.721| N/A|   148| 10614.645| N/A|  13,943|
| |Tyrrell County|     1| 249.004| N/A|    94| 23406.375| N/A|   4,016|
| |Transylvania County|     1| 29.082| N/A|   132|  3838.883| N/A|  34,385|
| |Avery County|     0|  0.000| N/A|    99|  5638.777| N/A|  17,557|
| |Alleghany County|     0|  0.000| N/A|   165| 14815.480| N/A|  11,137|
| |Hyde County|     0|  0.000| N/A|    38|  7696.982| N/A|   4,937|
| |Yancey County|     0|  0.000| N/A|   101|  5589.684| N/A|  18,069|
| |Watauga County|     0|  0.000| N/A|   283|  5037.649| N/A|  56,177|
| |Madison County|     0|  0.000| N/A|    41|  1884.624| N/A|  21,755|
| |Graham County|     0|  0.000| N/A|    31|  3672.551| N/A|   8,441|
| |Currituck County|     0|  0.000| N/A|    71|  2557.361| N/A|  27,763|
| |Clay County|     0|  0.000| N/A|    76|  6766.984| N/A|  11,231|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 1,942| 377.182| N/A|96,797| 18800.229| N/A|5,148,714|
| |Greenville County|   201| 383.923|  7.095|10,635| 20313.557| 207.106| 523,542|
| |Charleston County|   190| 461.831| 11.112|12,019| 29214.450| 263.556| 411,406|
| |Richland County|   148| 355.975|  6.529| 8,464| 20357.948| 291.034| 415,759|
| |Horry County|   145| 409.511|  9.683| 8,371| 23641.483| 200.923| 354,081|
| |Lexington County|   108| 361.506|  5.260| 4,839| 16197.490| 167.842| 298,750|
| |Florence County|   108| 780.951| 17.561| 3,258| 23558.676| 484.479| 138,293|
| |Spartanburg County|    98| 306.456|  7.594| 3,961| 12386.447| 157.249| 319,785|
| |Berkeley County|    64| 280.816|  4.388| 4,049| 17766.019| 199.329| 227,907|
| |Orangeburg County|    61| 707.862| 14.920| 2,304| 26736.292| 402.835|  86,175|
| |Anderson County|    55| 271.527|  9.874| 2,237| 11043.750| 250.369| 202,558|
| |Beaufort County|    54| 281.071|  7.436| 3,921| 20408.907| 388.890| 192,122|
| |Clarendon County|    51| 1511.335|  4.233|   817| 24210.994| 325.974|  33,745|
| |Dorchester County|    47| 288.682|  8.775| 2,968| 18229.950| 276.397| 162,809|
| |Sumter County|    47| 440.401|  6.693| 2,419| 22666.579| 291.816| 106,721|
| |Laurens County|    42| 622.287| 19.050| 1,275| 18890.848| 209.546|  67,493|
| |Darlington County|    35| 525.384|  4.289| 1,189| 17848.029| 418.162|  66,618|
| |Colleton County|    33| 875.866|  7.583|   791| 20994.241| 242.664|  37,677|
| |Aiken County|    33| 193.127|  7.524| 1,788| 10463.973| 287.600| 170,872|
| |Williamsburg County|    29| 954.953| 28.225|   961| 31645.153| 531.575|  30,368|
| |York County|    29| 103.211|  1.017| 3,402| 12107.666| 193.202| 280,979|
| |Cherokee County|    28| 488.656|  9.973|   599| 10453.752| 209.424|  57,300|
| |Lee County|    27| 1604.469|  8.489|   542| 32208.224| 483.887|  16,828|
| |Pickens County|    26| 204.912|  6.755| 1,793| 14131.017| 157.624| 126,884|
| |Dillon County|    24| 787.427|  4.687|   607| 19915.352| 332.782|  30,479|
| |Fairfield County|    23| 1029.221|  0.000|   554| 24790.800| 236.529|  22,347|
| |Kershaw County|    23| 345.600|  2.147| 1,357| 20390.377| 238.271|  66,551|
| |Lancaster County|    23| 234.665|  2.915| 1,138| 11610.823| 196.769|  98,012|
| |Chesterfield County|    21| 460.022|  6.259|   729| 15969.332| 215.929|  45,650|
| |Bamberg County|    20| 1421.868| 50.781|   455| 32347.505| 416.404|  14,066|
| |Georgetown County|    19| 303.127|  4.558| 1,345| 21458.200| 305.406|  62,680|
| |Greenwood County|    17| 240.076|  4.035| 1,336| 18867.125| 326.826|  70,811|
| |Jasper County|    14| 465.534| 14.251|   560| 18621.355| 408.530|  30,073|
| |Marion County|    13| 424.047|  4.660|   535| 17451.153| 172.415|  30,657|
| |Chester County|    13| 403.176| 13.292|   613| 19011.289| 398.745|  32,244|
| |Calhoun County|    10| 687.144| 39.265|   371| 25493.025| 854.021|  14,553|
| |Newberry County|     9| 234.131| N/A|   828| 21540.062| N/A|  38,440|
| |Abbeville County|     8| 326.171| N/A|   313| 12761.447| N/A|  24,527|
| |Oconee County|     8| 100.571| N/A|   787|  9893.646| N/A|  79,546|
| |Saluda County|     8| 390.759| N/A|   443| 21638.255| N/A|  20,473|
| |Hampton County|     7| 364.166| N/A|   405| 21069.608| N/A|  19,222|
| |Edgefield County|     6| 220.103| N/A|   303| 11115.187| N/A|  27,260|
| |Barnwell County|     5| 239.624| N/A|   390| 18690.693| N/A|  20,866|
| |Marlboro County|     4| 153.151| N/A|   468| 17918.677| N/A|  26,118|
| |Allendale County|     3| 345.304| N/A|   204| 23480.663| N/A|   8,688|
| |Union County|     3| 109.826| N/A|   346| 12666.569| N/A|  27,316|
| |McCormick County|     2| 211.349| N/A|   108| 11412.871| N/A|   9,463|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,852| 321.598| N/A|49,418|  8581.397| N/A|5,758,736|
| |Denver County|   413| 567.923| N/A|10,052| 13822.673| N/A| 727,211|
| |Arapahoe County|   363| 552.856|  0.218| 7,194| 10956.609| 86.159| 656,590|
| |Jefferson County|   227| 389.445|  0.245| 4,086|  7010.007| 64.948| 582,881|
| |Adams County|   175| 338.216|  1.933| 6,307| 12189.300| 121.206| 517,421|
| |Weld County|   142| 437.607|  0.440| 3,635| 11202.125| 69.559| 324,492|
| |El Paso County|   137| 190.171|  1.388| 4,832|  6707.357| 89.434| 720,403|
| |Boulder County|    75| 229.923|  0.000| 1,997|  6122.086| 68.758| 326,196|
| |Douglas County|    59| 168.017|  0.407| 1,702|  4846.876| 43.937| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   681| 23427.824| 39.317|  29,068|
| |Larimer County|    35| 98.067|  0.400| 1,475|  4132.822| 56.038| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   660|  3918.681| 59.374| 168,424|
| |Broomfield County|    32| 454.126| N/A|   445|  6315.192| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   295| 14492.042| 98.251|  20,356|
| |Montrose County|    13| 304.037|  0.000|   292|  6829.131| 90.209|  42,758|
| |Alamosa County|     9| 554.426| N/A|   224| 13799.051| N/A|  16,233|
| |Eagle County|     9| 163.259| N/A| 1,106| 20062.764| N/A|  55,127|
| |Gunnison County|     6| 343.603| N/A|   267| 15290.345| N/A|  17,462|
| |Routt County|     6| 234.028| N/A|   111|  4329.511| N/A|  25,638|
| |Otero County|     6| 328.263| N/A|    70|  3829.741| N/A|  18,278|
| |Logan County|     5| 223.125| N/A|   649| 28961.578| N/A|  22,409|
| |Mesa County|     4| 25.939| N/A|   289|  1874.068| N/A| 154,210|
| |Garfield County|     4| 66.599| N/A|   753| 12537.254| N/A|  60,061|
| |Montezuma County|     4| 152.771| N/A|   109|  4163.007| N/A|  26,183|
| |Summit County|     4| 128.986| N/A|   327| 10544.645| N/A|  31,011|
| |Teller County|     3| 118.166| N/A|   122|  4805.420| N/A|  25,388|
| |Kit Carson County|     3| 422.714| N/A|    43|  6058.898| N/A|   7,097|
| |Saguache County|     2| 293.083| N/A|   106| 15533.411| N/A|   6,824|
| |Rio Grande County|     2| 177.510| N/A|    89|  7899.175| N/A|  11,267|
| |Pitkin County|     2| 112.568| N/A|   181| 10187.426| N/A|  17,767|
| |Elbert County|     2| 74.825| N/A|   102|  3816.080| N/A|  26,729|
| |La Plata County|     2| 35.574| N/A|   204|  3628.537| N/A|  56,221|
| |Sedgwick County|     1| 444.840| N/A|    11|  4893.238| N/A|   2,248|
| |Crowley County|     1| 164.989| N/A|    72| 11879.228| N/A|   6,061|
| |Delta County|     1| 32.090| N/A|   117|  3754.573| N/A|  31,162|
| |Grand County|     1| 63.557| N/A|    45|  2860.048| N/A|  15,734|
| |Huerfano County|     1| 144.991| N/A|     8|  1159.925| N/A|   6,897|
| |Park County|     1| 53.064| N/A|    42|  2228.708| N/A|  18,845|
| |Moffat County|     1| 75.284| N/A|    26|  1957.389| N/A|  13,283|
| |Clear Creek County|     1| 103.093| N/A|    29|  2989.691| N/A|   9,700|
| |Ouray County|     1| 201.939| N/A|    12|  2423.263| N/A|   4,952|
| |Dolores County|     0|  0.000| N/A|     1|   486.618| N/A|   2,055|
| |Baca County|     0|  0.000| N/A|    14|  3909.522| N/A|   3,581|
| |Gilpin County|     0|  0.000| N/A|    16|  2562.870| N/A|   6,243|
| |Fremont County|     0|  0.000| N/A|   116|  2424.800| N/A|  47,839|
| |Custer County|     0|  0.000| N/A|    11|  2170.481| N/A|   5,068|
| |Costilla County|     0|  0.000| N/A|    22|  5659.892| N/A|   3,887|
| |Conejos County|     0|  0.000| N/A|    23|  2803.169| N/A|   8,205|
| |Cheyenne County|     0|  0.000| N/A|     8|  4369.197| N/A|   1,831|
| |Bent County|     0|  0.000| N/A|     8|  1434.463| N/A|   5,577|
| |Archuleta County|     0|  0.000| N/A|    35|  2494.832| N/A|  14,029|
| |Hinsdale County|     0|  0.000| N/A|     3|  3658.537| N/A|     820|
| |Jackson County|     0|  0.000| N/A|     9|  6465.517| N/A|   1,392|
| |Kiowa County|     0|  0.000| N/A|     0|     0.000| N/A|   1,406|
| |Lake County|     0|  0.000| N/A|    74|  9105.451| N/A|   8,127|
| |Yuma County|     0|  0.000| N/A|    63|  6288.053| N/A|  10,019|
| |Washington County|     0|  0.000| N/A|    47|  9576.202| N/A|   4,908|
| |San Miguel County|     0|  0.000| N/A|    80|  9781.147| N/A|   8,179|
| |San Juan County|     0|  0.000| N/A|     2|  2747.253| N/A|     728|
| |Rio Blanco County|     0|  0.000| N/A|     9|  1423.150| N/A|   6,324|
| |Prowers County|     0|  0.000| N/A|    50|  4107.788| N/A|  12,172|
| |Phillips County|     0|  0.000| N/A|    19|  4454.865| N/A|   4,265|
| |Mineral County|     0|  0.000| N/A|    18| 23407.022| N/A|     769|
| |Lincoln County|     0|  0.000| N/A|     8|  1403.263| N/A|   5,701|
| |Las Animas County|     0|  0.000| N/A|    15|  1034.055| N/A|  14,506|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,825| 613.209| N/A|64,400| 21638.702| N/A|2,976,149|
| |Hinds County|   116| 500.345| 11.708| 5,487| 23667.184| 299.468| 231,840|
| |Neshoba County|    91| 3125.215| 29.437| 1,278| 43890.377| 544.582|  29,118|
| |Lauderdale County|    90| 1214.165|  3.854| 1,390| 18752.108| 210.070|  74,125|
| |Madison County|    63| 592.818| 17.475| 2,387| 22461.232| 236.590| 106,272|
| |Leflore County|    62| 2199.908| 15.207|   893| 31685.768| 517.029|  28,183|
| |Jones County|    58| 851.714|  2.098| 1,842| 27049.253| 352.433|  68,098|
| |Forrest County|    55| 734.342|  9.537| 1,721| 22978.223| 345.236|  74,897|
| |Monroe County|    51| 1446.726|  8.105|   747| 21190.287| 397.141|  35,252|
| |Holmes County|    48| 2821.869| 25.195|   863| 50734.862| 453.515|  17,010|
| |Jackson County|    42| 292.444|  7.958| 2,201| 15325.484| 378.984| 143,617|
| |Lincoln County|    41| 1200.480| 12.549|   790| 23131.204| 309.531|  34,153|
| |Pearl River County|    37| 666.247|  5.145|   520|  9363.464| 149.198|  55,535|
| |Oktibbeha County|    37| 746.163| 17.286| 1,090| 21981.568| 190.142|  49,587|
| |Washington County|    37| 842.652| 29.281| 1,582| 36029.060| 627.922|  43,909|
| |Harrison County|    35| 168.205|  4.119| 2,378| 11428.297| 271.873| 208,080|
| |Lowndes County|    35| 597.321| 21.942| 1,039| 17731.888| 285.251|  58,595|
| |Pike County|    34| 865.404| 14.545|   877| 22322.338| 269.075|  39,288|
| |Bolivar County|    33| 1077.445| 18.657| 1,163| 37971.791| 1278.009|  30,628|
| |Rankin County|    32| 206.091|  4.600| 2,220| 14297.583| 158.249| 155,271|
| |Lee County|    32| 374.549|  6.688| 1,332| 15590.618| 362.845|  85,436|
| |Warren County|    31| 683.105| 22.036| 1,007| 22189.903| 242.392|  45,381|
| |Simpson County|    30| 1125.366| 69.665|   779| 29221.997| 503.735|  26,658|
| |DeSoto County|    28| 151.396|  1.545| 3,523| 19048.906| 356.090| 184,945|
| |Copiah County|    28| 997.684| 25.451|   941| 33529.307| 285.053|  28,065|
| |Tate County|    27| 953.356| 30.265|   692| 24434.165| 494.333|  28,321|
| |Adams County|    25| 814.518|  9.309|   602| 19613.593| 232.719|  30,693|
| |Clarke County|    25| 1608.648|  0.000|   324| 20848.079| 330.922|  15,541|
| |Leake County|    25| 1097.165|  0.000|   779| 34187.659| 244.511|  22,786|
| |Attala County|    24| 1320.568|  7.861|   513| 28227.138| 259.397|  18,174|
| |Sunflower County|    23| 915.970| 17.068|   967| 38510.554| 534.790|  25,110|
| |Wayne County|    21| 1040.480|  0.000|   749| 37110.439| 226.499|  20,183|
| |Grenada County|    21| 1011.658| 13.764|   830| 39984.584| 282.163|  20,758|
| |Scott County|    20| 711.136| 15.239|   987| 35094.581| 218.420|  28,124|
| |Walthall County|    19| 1329.973| 20.000|   489| 34229.315| 689.986|  14,286|
| |Chickasaw County|    19| 1110.916|  0.000|   441| 25784.950| 233.877|  17,103|
| |Marion County|    19| 773.206| 17.441|   638| 25963.456| 401.137|  24,573|
| |Union County|    15| 520.562|  9.915|   562| 19503.731| 470.985|  28,815|
| |Kemper County|    15| 1539.725|  0.000|   228| 23403.819| 87.984|   9,742|
| |Winston County|    15| 835.422|  7.956|   604| 33639.655| 477.384|  17,955|
| |Clay County|    14| 724.788|  7.396|   382| 19776.351| 162.707|  19,316|
| |Hancock County|    14| 293.920|  0.000|   363|  7620.927| 158.957|  47,632|
| |Lafayette County|    14| 259.168| 21.157|   937| 17345.749| 306.770|  54,019|
| |Lamar County|    14| 221.019|  4.511| 1,184| 18691.884| 272.891|  63,343|
| |Claiborne County|    13| 1446.373| 15.894|   399| 44392.523| 143.048|   8,988|
| |Tippah County|    13| 590.506|  6.489|   325| 14762.662| 363.389|  22,015|
| |Wilkinson County|    13| 1506.373| 16.554|   194| 22479.722| 347.625|   8,630|
| |Smith County|    13| 816.788|  8.976|   394| 24754.964| 251.319|  15,916|
| |Covington County|    13| 697.575| 22.997|   607| 32571.367| 291.295|  18,636|
| |Yazoo County|    12| 404.176|  4.812|   807| 27180.869| 288.697|  29,690|
| |Panola County|    12| 350.959|  4.178|   980| 28661.675| 472.124|  34,192|
| |Webster County|    12| 1238.518|  0.000|   216| 22293.322| 589.770|   9,689|
| |Greene County|    11| 809.657| 10.515|   231| 17002.797| 126.180|  13,586|
| |Coahoma County|    11| 497.198| 25.828|   697| 31504.249| 458.455|  22,124|
| |Carroll County|    11| 1105.861|  0.000|   254| 25535.337| 244.151|   9,947|
| |Humphreys County|    11| 1364.087|  0.000|   282| 34970.238| 442.885|   8,064|
| |Newton County|    11| 523.361|  0.000|   535| 25454.372| 176.719|  21,018|
| |Noxubee County|    11| 1055.966| 13.714|   444| 42622.636| 562.268|  10,417|
| |Itawamba County|    10| 427.533|  6.108|   337| 14407.867| 299.273|  23,390|
| |Yalobusha County|    10| 825.900|  0.000|   307| 25355.137| 47.194|  12,108|
| |Tallahatchie County|    10| 724.165| 10.345|   407| 29473.532| 124.143|  13,809|
| |Marshall County|     9| 255.001| N/A|   638| 18076.727| N/A|  35,294|
| |Prentiss County|     9| 358.195| N/A|   386| 15362.573| N/A|  25,126|
| |Calhoun County|     9| 626.697| N/A|   400| 27853.214| N/A|  14,361|
| |Jasper County|     9| 549.350| N/A|   381| 23255.814| N/A|  16,383|
| |Pontotoc County|     8| 248.648| N/A|   791| 24585.069| N/A|  32,174|
| |Perry County|     7| 584.649| N/A|   220| 18374.676| N/A|  11,973|
| |Lawrence County|     7| 556.174| N/A|   306| 24312.728| N/A|  12,586|
| |Tunica County|     6| 622.924| N/A|   317| 32911.130| N/A|   9,632|
| |Amite County|     6| 487.924| N/A|   220| 17890.542| N/A|  12,297|
| |Jefferson Davis County|     6| 539.180| N/A|   226| 20309.130| N/A|  11,128|
| |Jefferson County|     6| 858.369| N/A|   194| 27753.934| N/A|   6,990|
| |Tishomingo County|     5| 257.958| N/A|   350| 18057.060| N/A|  19,383|
| |Alcorn County|     5| 135.307| N/A|   382| 10337.456| N/A|  36,953|
| |Choctaw County|     4| 487.211| N/A|   130| 15834.348| N/A|   8,210|
| |George County|     4| 163.265| N/A|   548| 22367.347| N/A|  24,500|
| |Stone County|     3| 163.613| N/A|   163|  8889.616| N/A|  18,336|
| |Sharkey County|     3| 694.284| N/A|   190| 43971.303| N/A|   4,321|
| |Montgomery County|     3| 306.905| N/A|   307| 31406.650| N/A|   9,775|
| |Franklin County|     2| 259.302| N/A|   116| 15039.544| N/A|   7,713|
| |Quitman County|     1| 147.232| N/A|   240| 35335.689| N/A|   6,792|
| |Issaquena County|     1| 753.580| N/A|    25| 18839.488| N/A|   1,327|
| |Benton County|     0|  0.000| N/A|   133| 16103.645| N/A|   8,259|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,654| 337.332| N/A|93,402| 19049.251| N/A|4,903,185|
| |Jefferson County|   232| 352.277|  2.603|12,486| 18959.174| 335.574| 658,573|
| |Mobile County|   204| 493.696|  7.952| 9,420| 22797.125| 532.763| 413,210|
| |Montgomery County|   148| 653.462|  5.677| 6,449| 28474.166| 310.331| 226,486|
| |Tallapoosa County|    79| 1957.044|  3.539|   841| 20833.849| 212.338|  40,367|
| |Tuscaloosa County|    69| 329.584|  5.459| 4,057| 19378.568| 206.075| 209,355|
| |Walker County|    64| 1007.541|  8.996| 1,498| 23582.752| 175.420|  63,521|
| |Lee County|    44| 267.409|  3.473| 2,588| 15728.507| 175.379| 164,542|
| |Elmore County|    38| 467.928|  5.277| 1,672| 20588.851| 277.942|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   835| 25109.761| 150.358|  33,254|
| |Butler County|    35| 1799.671|  0.000|   756| 38872.892| 168.949|  19,448|
| |Marshall County|    34| 351.334|  8.857| 3,060| 31620.063| 391.191|  96,774|
| |Shelby County|    32| 146.990|  0.656| 3,164| 14533.629| 215.235| 217,702|
| |Madison County|    30| 80.449|  1.915| 5,161| 13839.838| 192.694| 372,909|
| |Etowah County|    28| 273.790| 12.572| 2,041| 19957.367| 340.841| 102,268|
| |Hale County|    26| 1774.623|  9.751|   464| 31670.193| 253.518|  14,651|
| |Marion County|    24| 807.836|  0.000|   562| 18916.827| 250.044|  29,709|
| |Lowndes County|    24| 2467.613|  0.000|   567| 58297.347| 293.763|   9,726|
| |Dale County|    23| 467.746| 14.526|   802| 16310.095| 185.936|  49,172|
| |Baldwin County|    23| 103.031|  1.920| 3,380| 15141.063| 253.418| 223,234|
| |Dallas County|    23| 618.346|  0.000| 1,305| 35084.418| 276.527|  37,196|
| |Autauga County|    21| 375.879|  2.557| 1,050| 18793.964| 222.459|  55,869|
| |Covington County|    20| 539.826|  0.000|   716| 19325.758| 219.786|  37,049|
| |Franklin County|    20| 637.714|  0.000| 1,238| 39474.523| 428.180|  31,362|
| |Sumter County|    18| 1448.459| 11.496|   360| 28969.180| 91.966|  12,427|
| |Morgan County|    17| 142.047|  3.581| 2,295| 19176.297| 235.153| 119,679|
| |Escambia County|    16| 436.765|  3.900| 1,044| 28498.894| 526.457|  36,633|
| |St. Clair County|    15| 167.575|  9.576| 1,289| 14400.304| 282.484|  89,512|
| |Lauderdale County|    15| 161.762|  7.703| 1,123| 12110.559| 204.898|  92,729|
| |Marengo County|    14| 742.194|  0.000|   536| 28415.416| 257.496|  18,863|
| |Calhoun County|    13| 114.432|  6.287| 1,672| 14717.662| 471.559| 113,605|
| |Colbert County|    13| 235.332|  5.172| 1,141| 20654.948| 346.534|  55,241|
| |Talladega County|    13| 162.545|  1.786|   967| 12090.825| 269.717|  79,978|
| |Macon County|    13| 719.504|  7.907|   320| 17710.870| 173.946|  18,068|
| |Limestone County|    13| 131.426|  2.888| 1,261| 12748.319| 207.971|  98,915|
| |DeKalb County|    13| 181.785|  5.993| 1,745| 24401.158| 301.643|  71,513|
| |Cullman County|    12| 143.253|  1.705| 1,189| 14193.964| 237.049|  83,768|
| |Choctaw County|    12| 953.213|  0.000|   277| 22003.336| 136.173|  12,589|
| |Washington County|    12| 735.024| 17.501|   320| 19600.637| 210.007|  16,326|
| |Houston County|    12| 113.334|  0.000| 1,348| 12731.154| 174.048| 105,882|
| |Bullock County|    11| 1089.001|  0.000|   450| 44550.045| 311.143|  10,101|
| |Greene County|    11| 1356.183|  0.000|   249| 30699.051| 193.740|   8,111|
| |Winston County|    11| 465.530|  6.046|   440| 18621.186| 175.329|  23,629|
| |Wilcox County|    10| 964.041| 13.772|   414| 39911.308| 261.668|  10,373|
| |Conecuh County|    10| 828.706|  0.000|   378| 31325.102| 284.128|  12,067|
| |Randolph County|    10| 440.102|  0.000|   394| 17340.023| 100.595|  22,722|
| |Clarke County|     9| 381.001| N/A|   494| 20912.708| N/A|  23,622|
| |Pickens County|     9| 451.581| N/A|   377| 18916.207| N/A|  19,930|
| |Pike County|     7| 211.391| N/A|   687| 20746.512| N/A|  33,114|
| |Cherokee County|     7| 267.216| N/A|   258|  9848.832| N/A|  26,196|
| |Chilton County|     6| 135.050| N/A|   745| 16768.704| N/A|  44,428|
| |Barbour County|     5| 202.544| N/A|   565| 22887.467| N/A|  24,686|
| |Coffee County|     5| 95.526| N/A|   736| 14061.366| N/A|  52,342|
| |Clay County|     5| 377.786| N/A|   237| 17907.065| N/A|  13,235|
| |Fayette County|     5| 306.711| N/A|   183| 11225.616| N/A|  16,302|
| |Jackson County|     4| 77.480| N/A|   924| 17897.958| N/A|  51,626|
| |Bibb County|     4| 178.619| N/A|   413| 18442.440| N/A|  22,394|
| |Monroe County|     4| 192.929| N/A|   408| 19678.773| N/A|  20,733|
| |Perry County|     4| 448.280| N/A|   436| 48862.490| N/A|   8,923|
| |Henry County|     3| 174.368| N/A|   249| 14472.537| N/A|  17,205|
| |Crenshaw County|     3| 217.833| N/A|   312| 22654.662| N/A|  13,772|
| |Blount County|     3| 51.880| N/A|   759| 13125.584| N/A|  57,826|
| |Lamar County|     2| 144.875| N/A|   212| 15356.755| N/A|  13,805|
| |Coosa County|     2| 187.564| N/A|   101|  9472.006| N/A|  10,663|
| |Russell County|     2| 34.506| N/A| 1,277| 22032.056| N/A|  57,961|
| |Lawrence County|     1| 30.373| N/A|   332| 10083.829| N/A|  32,924|
| |Cleburne County|     1| 67.069| N/A|   125|  8383.635| N/A|  14,910|
| |Geneva County|     0|  0.000| N/A|   248|  9440.067| N/A|  26,271|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,649| 216.549| N/A|60,723|  7974.242| N/A|7,614,893|
| |King County|   664| 294.747|  0.951|16,078|  7136.953| 66.775|2,252,782|
| |Yakima County|   211| 841.063|  3.986|10,167| 40526.482| 171.971| 250,873|
| |Snohomish County|   191| 232.337|  0.869| 5,326|  6478.665| 65.513| 822,083|
| |Pierce County|   137| 151.385|  1.894| 5,477|  6052.067| 101.186| 904,980|
| |Benton County|   113| 552.865|  4.194| 3,632| 17769.950| 138.391| 204,390|
| |Spokane County|    79| 151.110|  6.012| 4,192|  8018.393| 158.215| 522,798|
| |Franklin County|    48| 504.085|  3.001| 3,412| 35832.056| 303.051|  95,222|
| |Clark County|    42| 86.023|  0.878| 1,712|  3506.465| 88.071| 488,241|
| |Whatcom County|    38| 165.760|  0.623|   965|  4209.433| 44.244| 229,247|
| |Skagit County|    21| 162.532|  1.106|   858|  6640.610| 82.925| 129,205|
| |Kittitas County|    18| 375.509|  2.980|   355|  7405.862| 86.427|  47,935|
| |Grant County|    13| 133.015|  1.462| 1,393| 14253.118| 302.574|  97,733|
| |Island County|    11| 129.197|  0.000|   241|  2830.599| 11.745|  85,141|
| |Thurston County|    11| 37.861|  1.967|   680|  2340.502| 37.861| 290,536|
| |Chelan County|    10| 129.534|  1.850| 1,255| 16256.477| 436.714|  77,200|
| |Douglas County|     7| 161.183| N/A|   890| 20493.219| N/A|  43,429|
| |Kitsap County|     5| 18.418| N/A|   707|  2604.311| N/A| 271,473|
| |Cowlitz County|     5| 45.211| N/A|   462|  4177.480| N/A| 110,593|
| |Adams County|     4| 200.170| N/A|   417| 20867.738| N/A|  19,983|
| |Klickitat County|     3| 133.779| N/A|   108|  4816.054| N/A|  22,425|
| |Lewis County|     3| 37.171| N/A|   197|  2440.928| N/A|  80,707|
| |Walla Walla County|     3| 49.375| N/A|   487|  8015.142| N/A|  60,760|
| |Grays Harbor County|     2| 26.645| N/A|   109|  1452.152| N/A|  75,061|
| |Okanogan County|     2| 47.345| N/A|   820| 19411.500| N/A|  42,243|
| |Pacific County|     2| 89.004| N/A|    47|  2091.585| N/A|  22,471|
| |Asotin County|     2| 88.566| N/A|    25|  1107.076| N/A|  22,582|
| |Columbia County|     1| 250.941| N/A|    13|  3262.233| N/A|   3,985|
| |Mason County|     1| 14.977| N/A|   187|  2800.743| N/A|  66,768|
| |Skamania County|     1| 82.761| N/A|    55|  4551.850| N/A|  12,083|
| |Stevens County|     1| 21.871| N/A|    99|  2165.212| N/A|  45,723|
| |Jefferson County|     0|  0.000| N/A|    54|  1675.926| N/A|  32,221|
| |Clallam County|     0|  0.000| N/A|   100|  1293.142| N/A|  77,331|
| |Pend Oreille County|     0|  0.000| N/A|    38|  2768.872| N/A|  13,724|
| |Lincoln County|     0|  0.000| N/A|    20|  1828.321| N/A|  10,939|
| |San Juan County|     0|  0.000| N/A|    28|  1592.538| N/A|  17,582|
| |Ferry County|     0|  0.000| N/A|    21|  2753.376| N/A|   7,627|
| |Garfield County|     0|  0.000| N/A|     2|   898.876| N/A|   2,225|
| |Wahkiakum County|     0|  0.000| N/A|     5|  1114.082| N/A|   4,488|
| |Whitman County|     0|  0.000| N/A|    89|  1776.305| N/A|  50,104|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,636| 290.090| N/A|58,508| 10374.436| N/A|5,639,632|
| |Hennepin County|   828| 654.110|  2.031|18,641| 14726.155| 174.813|1,265,843|
| |Ramsey County|   261| 474.269|  0.779| 7,233| 13143.238| 162.503| 550,321|
| |Anoka County|   114| 319.398|  0.800| 3,515|  9848.118| 130.081| 356,921|
| |Dakota County|   104| 242.412|  0.666| 4,188|  9761.760| 159.166| 429,021|
| |Washington County|    44| 167.657|  0.544| 2,009|  7655.083| 118.122| 262,440|
| |Clay County|    40| 622.840|  2.224|   768| 11958.519| 75.631|  64,222|
| |Olmsted County|    23| 145.300|  0.902| 1,688| 10663.769| 109.201| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,864| 17780.537| 89.577| 161,075|
| |St. Louis County|    19| 95.444|  0.718|   486|  2441.352| 86.115| 199,070|
| |Scott County|    18| 120.795|  6.711| 1,479|  9925.309| 198.449| 149,013|
| |Winona County|    16| 316.932|  0.000|   254|  5031.297| 42.446|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   225|  3458.612| 92.230|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   329|  9599.113| 175.060|  34,274|
| |Itasca County|    12| 265.899|  0.000|   135|  2991.358| 37.986|  45,130|
| |Pipestone County|     9| 986.193| N/A|   147| 16107.824| N/A|   9,126|
| |Goodhue County|     8| 172.637| N/A|   187|  4035.391| N/A|  46,340|
| |Rice County|     8| 119.453| N/A| 1,013| 15125.724| N/A|  66,972|
| |Sherburne County|     7| 71.988| N/A|   703|  7229.684| N/A|  97,238|
| |Nobles County|     6| 277.405| N/A| 1,753| 81048.592| N/A|  21,629|
| |Blue Earth County|     5| 73.907| N/A|   874| 12918.865| N/A|  67,653|
| |Wright County|     5| 36.133| N/A|   847|  6120.959| N/A| 138,377|
| |Renville County|     5| 343.690| N/A|    62|  4261.754| N/A|  14,548|
| |Martin County|     5| 254.026| N/A|   204| 10364.274| N/A|  19,683|
| |Polk County|     3| 95.651| N/A|   145|  4623.135| N/A|  31,364|
| |Benton County|     3| 73.369| N/A|   315|  7703.783| N/A|  40,889|
| |Koochiching County|     3| 245.319| N/A|    74|  6051.190| N/A|  12,229|
| |Grant County|     3| 502.344| N/A|    52|  8707.301| N/A|   5,972|
| |Mille Lacs County|     3| 114.168| N/A|    69|  2625.871| N/A|  26,277|
| |Otter Tail County|     3| 51.067| N/A|   185|  3149.151| N/A|  58,746|
| |Lyon County|     3| 117.767| N/A|   421| 16526.655| N/A|  25,474|
| |Wilkin County|     3| 483.325| N/A|    32|  5155.470| N/A|   6,207|
| |Todd County|     2| 81.090| N/A|   422| 17109.958| N/A|  24,664|
| |Sibley County|     2| 134.544| N/A|    82|  5516.313| N/A|  14,865|
| |Mower County|     2| 49.923| N/A| 1,094| 27307.673| N/A|  40,062|
| |Meeker County|     2| 86.125| N/A|    85|  3660.322| N/A|  23,222|
| |Brown County|     2| 79.974| N/A|    86|  3438.900| N/A|  25,008|
| |Cass County|     2| 67.161| N/A|    71|  2384.230| N/A|  29,779|
| |Carver County|     2| 19.031| N/A|   816|  7764.847| N/A| 105,089|
| |Freeborn County|     1| 33.024| N/A|   358| 11822.595| N/A|  30,281|
| |Kanabec County|     1| 61.211| N/A|    32|  1958.744| N/A|  16,337|
| |Kandiyohi County|     1| 23.149| N/A|   687| 15903.146| N/A|  43,199|
| |Swift County|     1| 107.921| N/A|    52|  5611.915| N/A|   9,266|
| |Steele County|     1| 27.286| N/A|   338|  9222.625| N/A|  36,649|
| |Chisago County|     1| 17.674| N/A|   189|  3340.462| N/A|  56,579|
| |Chippewa County|     1| 84.746| N/A|   101|  8559.322| N/A|  11,800|
| |Becker County|     1| 29.050| N/A|   150|  4357.552| N/A|  34,423|
| |Aitkin County|     1| 62.949| N/A|    29|  1825.507| N/A|  15,886|
| |Pennington County|     1| 70.827| N/A|    73|  5170.338| N/A|  14,119|
| |Murray County|     1| 122.041| N/A|   122| 14888.943| N/A|   8,194|
| |Morrison County|     1| 29.953| N/A|    85|  2545.977| N/A|  33,386|
| |Le Sueur County|     1| 34.618| N/A|   210|  7269.706| N/A|  28,887|
| |Mahnomen County|     1| 180.930| N/A|    26|  4704.179| N/A|   5,527|
| |Red Lake County|     0|  0.000| N/A|    23|  5672.010| N/A|   4,055|
| |Norman County|     0|  0.000| N/A|    37|  5803.922| N/A|   6,375|
| |Pope County|     0|  0.000| N/A|    46|  4089.252| N/A|  11,249|
| |Redwood County|     0|  0.000| N/A|    32|  2109.426| N/A|  15,170|
| |Rock County|     0|  0.000| N/A|    77|  8266.237| N/A|   9,315|
| |Roseau County|     0|  0.000| N/A|    46|  3033.300| N/A|  15,165|
| |Yellow Medicine County|     0|  0.000| N/A|    51|  5252.858| N/A|   9,709|
| |Watonwan County|     0|  0.000| N/A|   301| 27622.281| N/A|  10,897|
| |Waseca County|     0|  0.000| N/A|   138|  7414.571| N/A|  18,612|
| |Wadena County|     0|  0.000| N/A|    24|  1754.130| N/A|  13,682|
| |Wabasha County|     0|  0.000| N/A|    87|  4022.749| N/A|  21,627|
| |Traverse County|     0|  0.000| N/A|    10|  3068.426| N/A|   3,259|
| |Stevens County|     0|  0.000| N/A|    17|  1733.809| N/A|   9,805|
| |Clearwater County|     0|  0.000| N/A|    15|  1701.066| N/A|   8,818|
| |McLeod County|     0|  0.000| N/A|   148|  4123.367| N/A|  35,893|
| |Lincoln County|     0|  0.000| N/A|    54|  9576.166| N/A|   5,639|
| |Lake of the Woods County|     0|  0.000| N/A|     1|   267.380| N/A|   3,740|
| |Lake County|     0|  0.000| N/A|    20|  1879.523| N/A|  10,641|
| |Lac qui Parle County|     0|  0.000| N/A|     6|   905.934| N/A|   6,623|
| |Kittson County|     0|  0.000| N/A|     3|   697.999| N/A|   4,298|
| |Jackson County|     0|  0.000| N/A|    72|  7312.614| N/A|   9,846|
| |Isanti County|     0|  0.000| N/A|   116|  2857.424| N/A|  40,596|
| |Hubbard County|     0|  0.000| N/A|    30|  1395.933| N/A|  21,491|
| |Houston County|     0|  0.000| N/A|    41|  2204.301| N/A|  18,600|
| |Fillmore County|     0|  0.000| N/A|    61|  2895.524| N/A|  21,067|
| |Faribault County|     0|  0.000| N/A|    83|  6079.250| N/A|  13,653|
| |Douglas County|     0|  0.000| N/A|   136|  3565.717| N/A|  38,141|
| |Dodge County|     0|  0.000| N/A|   125|  5971.147| N/A|  20,934|
| |Cottonwood County|     0|  0.000| N/A|   175| 15630.582| N/A|  11,196|
| |Cook County|     0|  0.000| N/A|     2|   366.099| N/A|   5,463|
| |Marshall County|     0|  0.000| N/A|    29|  3106.255| N/A|   9,336|
| |Carlton County|     0|  0.000| N/A|   132|  3679.853| N/A|  35,871|
| |Big Stone County|     0|  0.000| N/A|    22|  4407.934| N/A|   4,991|
| |Pine County|     0|  0.000| N/A|   128|  4327.394| N/A|  29,579|
| |Beltrami County|     0|  0.000| N/A|   215|  4556.243| N/A|  47,188|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,244| 202.691| N/A|50,408|  8213.212| N/A|6,137,428|
| |St. Louis County|   824| 828.803|  1.006|19,364| 19476.868| 345.574| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,895|  9688.525| 215.695| 402,022|
| |Jackson County|    62| 88.192|  1.219| 3,810|  5419.545| 126.192| 703,011|
| |Jasper County|    28| 230.779|  5.887| 1,706| 14061.058| 115.390| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,510|  6708.696| 177.079| 225,081|
| |Clay County|    20| 80.017|  0.572|   984|  3936.819| 72.587| 249,948|
| |Franklin County|    18| 173.132|  0.000|   586|  5636.404| 131.910| 103,967|
| |Scott County|    13| 339.603|  0.000|   368|  9613.375| 141.812|  38,280|
| |Greene County|    10| 34.120|  0.000| 1,400|  4776.755| 133.554| 293,086|
| |Buchanan County|    10| 114.464|  0.000| 1,075| 12304.840| 42.515|  87,364|
| |Platte County|    10| 95.769|  4.104|   338|  3236.990| 58.829| 104,418|
| |Pemiscot County|     9| 569.440| N/A|   227| 14362.543| N/A|  15,805|
| |Gentry County|     9| 1369.655| N/A|    83| 12631.259| N/A|   6,571|
| |Cass County|     9| 85.082| N/A|   692|  6541.879| N/A| 105,780|
| |Stoddard County|     9| 310.078| N/A|   220|  7579.673| N/A|  29,025|
| |Saline County|     7| 307.544| N/A|   421| 18496.551| N/A|  22,761|
| |McDonald County|     7| 306.520| N/A|   946| 41424.005| N/A|  22,837|
| |Newton County|     6| 103.029| N/A|   844| 14492.754| N/A|  58,236|
| |Camden County|     5| 107.980| N/A|   335|  7234.640| N/A|  46,305|
| |Cape Girardeau County|     5| 63.395| N/A|   627|  7949.690| N/A|  78,871|
| |Perry County|     4| 209.030| N/A|   218| 11392.140| N/A|  19,136|
| |Dunklin County|     4| 137.311| N/A|   288|  9886.375| N/A|  29,131|
| |Cole County|     3| 39.090| N/A|   362|  4716.920| N/A|  76,745|
| |Pettis County|     3| 70.857| N/A|   473| 11171.733| N/A|  42,339|
| |Henry County|     3| 137.463| N/A|    76|  3482.405| N/A|  21,824|
| |Boone County|     3| 16.624| N/A| 1,297|  7187.069| N/A| 180,463|
| |Taney County|     3| 53.640| N/A|   521|  9315.549| N/A|  55,928|
| |Butler County|     2| 47.083| N/A|   264|  6214.982| N/A|  42,478|
| |Barry County|     2| 55.883| N/A|   245|  6845.679| N/A|  35,789|
| |Lafayette County|     2| 61.147| N/A|   171|  5228.079| N/A|  32,708|
| |Johnson County|     2| 36.995| N/A|   476|  8804.706| N/A|  54,062|
| |Howell County|     2| 49.854| N/A|   145|  3614.428| N/A|  40,117|
| |Moniteau County|     2| 123.977| N/A|   138|  8554.426| N/A|  16,132|
| |Douglas County|     2| 151.688| N/A|    84|  6370.876| N/A|  13,185|
| |Lawrence County|     2| 52.144| N/A|   205|  5344.805| N/A|  38,355|
| |St. Francois County|     2| 29.755| N/A|   344|  5117.905| N/A|  67,215|
| |Bollinger County|     1| 82.420| N/A|    62|  5110.030| N/A|  12,133|
| |Pulaski County|     1| 19.009| N/A|   195|  3706.731| N/A|  52,607|
| |Bates County|     1| 61.835| N/A|    44|  2720.752| N/A|  16,172|
| |Caldwell County|     1| 110.865| N/A|    36|  3991.131| N/A|   9,020|
| |Scotland County|     1| 203.998| N/A|    14|  2855.977| N/A|   4,902|
| |Christian County|     1| 11.287| N/A|   324|  3657.091| N/A|  88,595|
| |Pike County|     1| 54.639| N/A|    86|  4698.940| N/A|  18,302|
| |Marion County|     1| 35.051| N/A|   171|  5993.691| N/A|  28,530|
| |Carter County|     1| 167.168| N/A|    20|  3343.363| N/A|   5,982|
| |Stone County|     1| 31.297| N/A|   111|  3473.961| N/A|  31,952|
| |Harrison County|     1| 119.732| N/A|    59|  7064.176| N/A|   8,352|
| |Linn County|     1| 83.893| N/A|    30|  2516.779| N/A|  11,920|
| |Shannon County|     1| 122.459| N/A|    43|  5265.736| N/A|   8,166|
| |DeKalb County|     1| 79.700| N/A|    36|  2869.212| N/A|  12,547|
| |Ste. Genevieve County|     1| 55.885| N/A|    51|  2850.117| N/A|  17,894|
| |Laclede County|     1| 27.993| N/A|   191|  5346.695| N/A|  35,723|
| |Washington County|     1| 40.437| N/A|    67|  2709.260| N/A|  24,730|
| |Lewis County|     1| 102.291| N/A|    37|  3784.779| N/A|   9,776|
| |Callaway County|     1| 22.350| N/A|   137|  3061.931| N/A|  44,743|
| |Lincoln County|     1| 16.945| N/A|   352|  5964.787| N/A|  59,013|
| |Webster County|     1| 25.258| N/A|   128|  3232.976| N/A|  39,592|
| |Osage County|     1| 73.448| N/A|    44|  3231.730| N/A|  13,615|
| |Grundy County|     1| 101.523| N/A|    25|  2538.071| N/A|   9,850|
| |New Madrid County|     1| 58.562| N/A|   216| 12649.332| N/A|  17,076|
| |Putnam County|     1| 212.947| N/A|    13|  2768.313| N/A|   4,696|
| |Dallas County|     1| 59.249| N/A|    58|  3436.426| N/A|  16,878|
| |Miller County|     1| 39.034| N/A|   111|  4332.722| N/A|  25,619|
| |Randolph County|     1| 40.407| N/A|    64|  2586.068| N/A|  24,748|
| |Audrain County|     1| 39.389| N/A|   198|  7798.960| N/A|  25,388|
| |Andrew County|     1| 56.459| N/A|    88|  4968.383| N/A|  17,712|
| |Benton County|     1| 51.432| N/A|    87|  4474.618| N/A|  19,443|
| |Oregon County|     0|  0.000| N/A|    14|  1329.661| N/A|  10,529|
| |Cooper County|     0|  0.000| N/A|   111|  6267.999| N/A|  17,709|
| |Crawford County|     0|  0.000| N/A|    69|  2884.615| N/A|  23,920|
| |Dade County|     0|  0.000| N/A|    14|  1851.607| N/A|   7,561|
| |Morgan County|     0|  0.000| N/A|    76|  3684.491| N/A|  20,627|
| |Montgomery County|     0|  0.000| N/A|    41|  3549.476| N/A|  11,551|
| |Monroe County|     0|  0.000| N/A|    26|  3007.867| N/A|   8,644|
| |Mississippi County|     0|  0.000| N/A|   134| 10166.920| N/A|  13,180|
| |Mercer County|     0|  0.000| N/A|    10|  2764.722| N/A|   3,617|
| |Maries County|     0|  0.000| N/A|    20|  2299.644| N/A|   8,697|
| |Madison County|     0|  0.000| N/A|    24|  1985.440| N/A|  12,088|
| |Macon County|     0|  0.000| N/A|    56|  3704.439| N/A|  15,117|
| |Livingston County|     0|  0.000| N/A|    54|  3546.332| N/A|  15,227|
| |Knox County|     0|  0.000| N/A|    26|  6567.315| N/A|   3,959|
| |Iron County|     0|  0.000| N/A|    23|  2271.605| N/A|  10,125|
| |Howard County|     0|  0.000| N/A|    47|  4699.530| N/A|  10,001|
| |Holt County|     0|  0.000| N/A|     6|  1362.707| N/A|   4,403|
| |Hickory County|     0|  0.000| N/A|    25|  2619.447| N/A|   9,544|
| |Gasconade County|     0|  0.000| N/A|    20|  1359.989| N/A|  14,706|
| |Dent County|     0|  0.000| N/A|    10|   642.137| N/A|  15,573|
| |Daviess County|     0|  0.000| N/A|    17|  2053.636| N/A|   8,278|
| |Clinton County|     0|  0.000| N/A|    72|  3531.662| N/A|  20,387|
| |St. Louis city|     0|  0.000| N/A|     0|     0.000| N/A| 300,576|
| |Vernon County|     0|  0.000| N/A|    48|  2334.290| N/A|  20,563|
| |Wright County|     0|  0.000| N/A|    60|  3280.661| N/A|  18,289|
| |Cedar County|     0|  0.000| N/A|    37|  2578.577| N/A|  14,349|
| |Phelps County|     0|  0.000| N/A|    84|  1884.549| N/A|  44,573|
| |Clark County|     0|  0.000| N/A|    18|  2648.227| N/A|   6,797|
| |Chariton County|     0|  0.000| N/A|    16|  2154.592| N/A|   7,426|
| |Carroll County|     0|  0.000| N/A|    99| 11406.844| N/A|   8,679|
| |Worth County|     0|  0.000| N/A|     9|  4470.939| N/A|   2,013|
| |Barton County|     0|  0.000| N/A|    66|  5615.110| N/A|  11,754|
| |Atchison County|     0|  0.000| N/A|    14|  2722.147| N/A|   5,143|
| |Adair County|     0|  0.000| N/A|   150|  5918.794| N/A|  25,343|
| |Nodaway County|     0|  0.000| N/A|   174|  7876.154| N/A|  22,092|
| |Wayne County|     0|  0.000| N/A|    52|  4039.462| N/A|  12,873|
| |Warren County|     0|  0.000| N/A|   189|  5301.691| N/A|  35,649|
| |Texas County|     0|  0.000| N/A|    47|  1850.539| N/A|  25,398|
| |Ozark County|     0|  0.000| N/A|     9|   981.033| N/A|   9,174|
| |Sullivan County|     0|  0.000| N/A|   140| 22992.281| N/A|   6,089|
| |Shelby County|     0|  0.000| N/A|    31|  5227.656| N/A|   5,930|
| |Schuyler County|     0|  0.000| N/A|    10|  2145.923| N/A|   4,660|
| |St. Clair County|     0|  0.000| N/A|    18|  1915.505| N/A|   9,397|
| |Ripley County|     0|  0.000| N/A|    48|  3612.282| N/A|  13,288|
| |Reynolds County|     0|  0.000| N/A|    16|  2551.834| N/A|   6,270|
| |Ralls County|     0|  0.000| N/A|    25|  2425.065| N/A|  10,309|
| |Polk County|     0|  0.000| N/A|   200|  6221.033| N/A|  32,149|
| |Ray County|     0|  0.000| N/A|   117|  5082.979| N/A|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,162| 170.152| N/A|110,483| 16178.091| N/A|6,829,174|
| |Shelby County|   300| 320.114|  3.811|22,212| 23701.244| 324.687| 937,166|
| |Davidson County|   211| 303.972|  3.293|20,001| 28813.906| 272.689| 694,144|
| |Sumner County|    72| 376.406|  2.987| 3,316| 17335.571| 203.140| 191,283|
| |Rutherford County|    53| 159.502|  1.720| 6,298| 18953.609| 234.308| 332,285|
| |Hamilton County|    49| 133.223|  1.554| 5,884| 15997.651| 189.930| 367,804|
| |Knox County|    37| 78.671|  2.734| 4,298|  9138.595| 219.611| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,405| 14281.999| 209.122| 238,412|
| |Wilson County|    23| 158.997|  2.963| 2,190| 15139.260| 214.300| 144,657|
| |McMinn County|    20| 371.789|  0.000|   509|  9462.022| 151.371|  53,794|
| |Robertson County|    19| 264.576|  5.968| 1,506| 20971.133| 262.587|  71,813|
| |Putnam County|    16| 199.389|  5.341| 1,677| 20898.498| 311.546|  80,245|
| |Hardeman County|    15| 598.802| 22.812|   858| 34251.497| 633.020|  25,050|
| |Madison County|    15| 153.086|  5.832|   984| 10042.456| 357.201|  97,984|
| |Hamblen County|    14| 215.604|  2.200| 1,346| 20728.740| 486.208|  64,934|
| |Giles County|    13| 441.216| 24.243|   369| 12523.758| 295.760|  29,464|
| |Macon County|    13| 528.412|  0.000|   855| 34753.272| 301.950|  24,602|
| |Montgomery County|    13| 62.203|  1.367| 1,815|  8684.501| 168.837| 208,993|
| |Bradley County|    12| 110.998|  2.643| 1,817| 16806.956| 295.995| 108,110|
| |Sullivan County|    12| 75.782|  4.511|   895|  5652.108| 190.358| 158,348|
| |Bedford County|    11| 221.270|  2.874|   901| 18124.032| 267.248|  49,713|
| |Tipton County|     9| 146.106| N/A| 1,155| 18750.304| N/A|  61,599|
| |Monroe County|     9| 193.361| N/A|   397|  8529.380| N/A|  46,545|
| |Blount County|     9| 67.624| N/A| 1,222|  9181.895| N/A| 133,088|
| |Fayette County|     8| 194.491| N/A|   652| 15851.020| N/A|  41,133|
| |Lauderdale County|     8| 312.098| N/A|   455| 17750.556| N/A|  25,633|
| |Cheatham County|     7| 172.130| N/A|   569| 13991.689| N/A|  40,667|
| |Hawkins County|     7| 123.270| N/A|   416|  7325.749| N/A|  56,786|
| |Hardin County|     7| 272.883| N/A|   444| 17308.592| N/A|  25,652|
| |Maury County|     7| 72.624| N/A| 1,159| 12024.443| N/A|  96,387|
| |Dyer County|     7| 188.380| N/A|   593| 15958.449| N/A|  37,159|
| |Greene County|     7| 101.348| N/A|   418|  6051.919| N/A|  69,069|
| |Lawrence County|     6| 135.925| N/A|   527| 11938.743| N/A|  44,142|
| |Sevier County|     6| 61.069| N/A| 1,791| 18229.008| N/A|  98,250|
| |Trousdale County|     6| 531.726| N/A| 1,578| 139844.027| N/A|  11,284|
| |Cumberland County|     6| 99.141| N/A|   398|  6576.338| N/A|  60,520|
| |Anderson County|     6| 77.944| N/A|   651|  8456.962| N/A|  76,978|
| |Haywood County|     6| 346.741| N/A|   435| 25138.696| N/A|  17,304|
| |White County|     5| 182.849| N/A|   246|  8996.160| N/A|  27,345|
| |Carter County|     5| 88.667| N/A|   473|  8387.863| N/A|  56,391|
| |McNairy County|     5| 194.598| N/A|   351| 13660.777| N/A|  25,694|
| |Gibson County|     4| 81.412| N/A|   644| 13107.280| N/A|  49,133|
| |Obion County|     4| 133.027| N/A|   490| 16295.853| N/A|  30,069|
| |Franklin County|     4| 94.769| N/A|   302|  7155.042| N/A|  42,208|
| |Crockett County|     4| 281.096| N/A|   253| 17779.339| N/A|  14,230|
| |Smith County|     4| 198.442| N/A|   429| 21282.929| N/A|  20,157|
| |Warren County|     4| 96.906| N/A|   479| 11604.526| N/A|  41,277|
| |Marion County|     4| 138.375| N/A|   213|  7368.457| N/A|  28,907|
| |Weakley County|     3| 90.014| N/A|   363| 10891.743| N/A|  33,328|
| |Polk County|     3| 178.232| N/A|   185| 10990.970| N/A|  16,832|
| |Humphreys County|     3| 161.447| N/A|   118|  6350.231| N/A|  18,582|
| |Decatur County|     3| 257.224| N/A|   188| 16119.352| N/A|  11,663|
| |Loudon County|     3| 55.486| N/A|   705| 13039.136| N/A|  54,068|
| |Coffee County|     3| 53.079| N/A|   482|  8527.955| N/A|  56,520|
| |Jefferson County|     3| 55.051| N/A|   525|  9633.911| N/A|  54,495|
| |Marshall County|     3| 87.273| N/A|   275|  8000.000| N/A|  34,375|
| |Carroll County|     3| 108.042| N/A|   272|  9795.801| N/A|  27,767|
| |Roane County|     2| 37.466| N/A|   423|  7924.019| N/A|  53,382|
| |Washington County|     2| 15.459| N/A| 1,131|  8742.029| N/A| 129,375|
| |Henderson County|     2| 71.131| N/A|   517| 18387.452| N/A|  28,117|
| |Chester County|     2| 115.627| N/A|   206| 11909.580| N/A|  17,297|
| |Wayne County|     2| 119.954| N/A|   224| 13434.895| N/A|  16,673|
| |Cocke County|     2| 55.549| N/A|   439| 12193.090| N/A|  36,004|
| |DeKalb County|     2| 97.609| N/A|   331| 16154.222| N/A|  20,490|
| |Grundy County|     2| 148.954| N/A|   108|  8043.494| N/A|  13,427|
| |Hancock County|     1| 151.057| N/A|    77| 11631.420| N/A|   6,620|
| |Morgan County|     1| 46.722| N/A|    98|  4578.797| N/A|  21,403|
| |Overton County|     1| 44.962| N/A|   155|  6969.111| N/A|  22,241|
| |Lincoln County|     1| 29.099| N/A|   268|  7798.405| N/A|  34,366|
| |Benton County|     1| 61.881| N/A|   126|  7797.030| N/A|  16,160|
| |Bledsoe County|     1| 66.383| N/A|   686| 45539.033| N/A|  15,064|
| |Campbell County|     1| 25.099| N/A|   229|  5747.703| N/A|  39,842|
| |Jackson County|     1| 84.846| N/A|   112|  9502.800| N/A|  11,786|
| |Dickson County|     1| 18.536| N/A|   652| 12085.712| N/A|  53,948|
| |Rhea County|     1| 30.150| N/A|   517| 15587.783| N/A|  33,167|
| |Pickett County|     1| 198.098| N/A|    30|  5942.948| N/A|   5,048|
| |Lewis County|     1| 81.513| N/A|    67|  5461.363| N/A|  12,268|
| |Clay County|     0|  0.000| N/A|    71|  9323.703| N/A|   7,615|
| |Claiborne County|     0|  0.000| N/A|   242|  7572.202| N/A|  31,959|
| |Cannon County|     0|  0.000| N/A|   136|  9265.568| N/A|  14,678|
| |Fentress County|     0|  0.000| N/A|    79|  4264.968| N/A|  18,523|
| |Union County|     0|  0.000| N/A|   141|  7059.884| N/A|  19,972|
| |Van Buren County|     0|  0.000| N/A|    35|  5960.490| N/A|   5,872|
| |Grainger County|     0|  0.000| N/A|   189|  8104.631| N/A|  23,320|
| |Stewart County|     0|  0.000| N/A|    74|  5395.552| N/A|  13,715|
| |Scott County|     0|  0.000| N/A|   110|  4984.593| N/A|  22,068|
| |Moore County|     0|  0.000| N/A|    55|  8477.189| N/A|   6,488|
| |Sequatchie County|     0|  0.000| N/A|   100|  6655.131| N/A|  15,026|
| |Meigs County|     0|  0.000| N/A|    99|  7969.731| N/A|  12,422|
| |Perry County|     0|  0.000| N/A|    77|  9534.423| N/A|   8,076|
| |Hickman County|     0|  0.000| N/A|   248|  9849.869| N/A|  25,178|
| |Henry County|     0|  0.000| N/A|   248|  7667.337| N/A|  32,345|
| |Unicoi County|     0|  0.000| N/A|   148|  8276.016| N/A|  17,883|
| |Houston County|     0|  0.000| N/A|    56|  6828.436| N/A|   8,201|
| |Lake County|     0|  0.000| N/A|   765| 109036.488| N/A|   7,016|
| |Johnson County|     0|  0.000| N/A|   225| 12648.977| N/A|  17,788|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   978| 167.971| N/A|57,779|  9923.513| N/A|5,822,434|
| |Milwaukee County|   452| 477.940|  2.870|20,389| 21559.099| 199.393| 945,726|
| |Racine County|    78| 397.329|  2.183| 3,364| 17136.075| 222.679| 196,311|
| |Kenosha County|    58| 342.060|  5.898| 2,597| 15316.022| 187.880| 169,561|
| |Waukesha County|    57| 141.020|  2.121| 3,930|  9722.958| 194.388| 404,198|
| |Brown County|    52| 196.566|  1.080| 4,151| 15691.270| 137.704| 264,542|
| |Dane County|    37| 67.679|  0.523| 4,376|  8004.463| 96.424| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,395|  8539.736| 56.844| 163,354|
| |Walworth County|    22| 211.807|  1.375| 1,284| 12361.844| 195.303| 103,868|
| |Washington County|    22| 161.724|  0.000|   967|  7108.517| 184.828| 136,034|
| |Winnebago County|    18| 104.708|  1.662| 1,111|  6462.797| 94.736| 171,907|
| |Ozaukee County|    17| 190.538|  1.601|   624|  6993.869| 176.128|  89,221|
| |Waupaca County|    15| 294.175|  2.802|   417|  8178.074| 204.522|  50,990|
| |Grant County|    14| 272.167|  0.000|   341|  6629.211| 77.762|  51,439|
| |Outagamie County|    14| 74.514|  1.521| 1,180|  6280.438| 108.729| 187,885|
| |Sheboygan County|     9| 78.030| N/A|   720|  6242.414| N/A| 115,340|
| |Marathon County|     8| 58.957| N/A|   612|  4510.214| N/A| 135,692|
| |Clark County|     7| 201.300| N/A|   180|  5176.281| N/A|  34,774|
| |Fond du Lac County|     6| 58.025| N/A|   598|  5783.198| N/A| 103,403|
| |Dodge County|     5| 56.922| N/A|   757|  8618.040| N/A|  87,839|
| |Jefferson County|     5| 58.984| N/A|   596|  7030.872| N/A|  84,769|
| |Richland County|     4| 231.857| N/A|    34|  1970.786| N/A|  17,252|
| |Forest County|     4| 444.247| N/A|    59|  6552.643| N/A|   9,004|
| |Eau Claire County|     4| 38.224| N/A|   541|  5169.811| N/A| 104,646|
| |St. Croix County|     4| 44.108| N/A|   476|  5248.823| N/A|  90,687|
| |Barron County|     3| 66.307| N/A|   276|  6100.256| N/A|  45,244|
| |Door County|     3| 108.429| N/A|   101|  3650.426| N/A|  27,668|
| |Marinette County|     3| 74.349| N/A|   356|  8822.800| N/A|  40,350|
| |Sauk County|     3| 46.553| N/A|   423|  6564.042| N/A|  64,442|
| |Trempealeau County|     2| 67.456| N/A|   329| 11096.496| N/A|  29,649|
| |Monroe County|     2| 43.240| N/A|   241|  5210.473| N/A|  46,253|
| |Adams County|     2| 98.912| N/A|    82|  4055.391| N/A|  20,220|
| |Kewaunee County|     2| 97.876| N/A|   122|  5970.441| N/A|  20,434|
| |Buffalo County|     2| 153.480| N/A|    42|  3223.083| N/A|  13,031|
| |Polk County|     2| 45.680| N/A|   126|  2877.829| N/A|  43,783|
| |Calumet County|     2| 39.929| N/A|   288|  5749.765| N/A|  50,089|
| |Green County|     1| 27.056| N/A|   137|  3706.710| N/A|  36,960|
| |Manitowoc County|     1| 12.661| N/A|   321|  4064.269| N/A|  78,981|
| |Langlade County|     1| 52.113| N/A|    57|  2970.452| N/A|  19,189|
| |Juneau County|     1| 37.471| N/A|   135|  5058.643| N/A|  26,687|
| |La Crosse County|     1|  8.473| N/A|   881|  7465.089| N/A| 118,016|
| |Jackson County|     1| 48.443| N/A|    52|  2519.014| N/A|  20,643|
| |Iron County|     1| 175.840| N/A|    73| 12836.293| N/A|   5,687|
| |Marquette County|     1| 64.210| N/A|    76|  4879.928| N/A|  15,574|
| |Rusk County|     1| 70.532| N/A|    17|  1199.041| N/A|  14,178|
| |Wood County|     1| 13.699| N/A|   268|  3671.283| N/A|  72,999|
| |Burnett County|     1| 64.876| N/A|    22|  1427.274| N/A|  15,414|
| |Bayfield County|     1| 66.507| N/A|    21|  1396.648| N/A|  15,036|
| |Columbia County|     1| 17.382| N/A|   238|  4136.828| N/A|  57,532|
| |Ashland County|     1| 64.259| N/A|    22|  1413.700| N/A|  15,562|
| |Waushara County|     0|  0.000| N/A|   112|  4582.089| N/A|  24,443|
| |Washburn County|     0|  0.000| N/A|    41|  2608.142| N/A|  15,720|
| |Green Lake County|     0|  0.000| N/A|    54|  2855.179| N/A|  18,913|
| |Vernon County|     0|  0.000| N/A|    59|  1914.217| N/A|  30,822|
| |Taylor County|     0|  0.000| N/A|    61|  2998.574| N/A|  20,343|
| |Douglas County|     0|  0.000| N/A|   149|  3453.071| N/A|  43,150|
| |Dunn County|     0|  0.000| N/A|   112|  2468.700| N/A|  45,368|
| |Lincoln County|     0|  0.000| N/A|    65|  2355.670| N/A|  27,593|
| |Portage County|     0|  0.000| N/A|   377|  5326.965| N/A|  70,772|
| |Florence County|     0|  0.000| N/A|     6|  1396.973| N/A|   4,295|
| |Sawyer County|     0|  0.000| N/A|    52|  3140.476| N/A|  16,558|
| |Price County|     0|  0.000| N/A|    26|  1947.420| N/A|  13,351|
| |Lafayette County|     0|  0.000| N/A|   116|  6960.696| N/A|  16,665|
| |Pierce County|     0|  0.000| N/A|   197|  4607.756| N/A|  42,754|
| |Iowa County|     0|  0.000| N/A|    70|  2956.331| N/A|  23,678|
| |Crawford County|     0|  0.000| N/A|    70|  4339.471| N/A|  16,131|
| |Chippewa County|     0|  0.000| N/A|   218|  3371.586| N/A|  64,658|
| |Pepin County|     0|  0.000| N/A|    42|  5763.689| N/A|   7,287|
| |Vilas County|     0|  0.000| N/A|    45|  2027.484| N/A|  22,195|
| |Shawano County|     0|  0.000| N/A|   173|  4229.932| N/A|  40,899|
| |Oneida County|     0|  0.000| N/A|   102|  2865.571| N/A|  35,595|
| |Menominee County|     0|  0.000| N/A|    20|  4389.816| N/A|   4,556|
| |Oconto County|     0|  0.000| N/A|   207|  5457.422| N/A|  37,930|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   912| 289.059| N/A|47,556| 15072.883| N/A|3,155,070|
| |Polk County|   206| 420.270|  1.457|10,032| 20466.745| 187.693| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,279| 10052.667| 194.714| 226,706|
| |Black Hawk County|    63| 480.080|  1.089| 3,084| 23501.082| 149.141| 131,228|
| |Woodbury County|    51| 494.632|  5.542| 3,691| 35797.763| 109.456| 103,107|
| |Muscatine County|    48| 1125.070|  3.348|   840| 19688.731| 150.679|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,846| 19753.245| 189.553|  93,453|
| |Wapello County|    33| 943.693|  8.171|   872| 24936.372| 208.348|  34,969|
| |Dubuque County|    31| 318.566|  4.404| 1,623| 16678.484| 251.036|  97,311|
| |Tama County|    29| 1720.660|  0.000|   545| 32336.537| 110.190|  16,854|
| |Jasper County|    26| 699.207|  7.684|   466| 12531.935| 80.678|  37,185|
| |Pottawattamie County|    26| 278.952|  7.664| 1,284| 13775.937| 225.307|  93,206|
| |Marshall County|    25| 635.017|  3.629| 1,425| 36195.992| 221.349|  39,369|
| |Mahaska County|    17| 769.405|  0.000|   139|  6291.016| 38.794|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   596| 14040.047| 97.594|  42,450|
| |Johnson County|    16| 105.862|  1.890| 2,021| 13371.708| 155.958| 151,140|
| |Story County|    14| 144.156|  1.471| 1,141| 11748.715| 83.846|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   380| 34435.886| 38.837|  11,035|
| |Scott County|    14| 80.952|  2.478| 1,655|  9569.627| 93.342| 172,943|
| |Buena Vista County|    12| 611.621|  0.000| 1,791| 91284.404| 65.531|  19,620|
| |Washington County|    10| 455.270|  0.000|   293| 13339.404| 58.535|  21,965|
| |Franklin County|     9| 893.744| N/A|   233| 23138.034| N/A|  10,070|
| |Plymouth County|     8| 317.750| N/A|   452| 17952.894| N/A|  25,177|
| |Poweshiek County|     8| 432.339| N/A|   153|  8268.482| N/A|  18,504|
| |Webster County|     7| 194.964| N/A|   772| 21501.783| N/A|  35,904|
| |Bremer County|     7| 279.307| N/A|   203|  8099.912| N/A|  25,062|
| |Monroe County|     7| 908.265| N/A|    69|  8952.900| N/A|   7,707|
| |Guthrie County|     5| 467.771| N/A|   131| 12255.590| N/A|  10,689|
| |Allamakee County|     4| 292.248| N/A|   154| 11251.553| N/A|  13,687|
| |Montgomery County|     4| 403.348| N/A|    53|  5344.358| N/A|   9,917|
| |Dickinson County|     4| 231.777| N/A|   377| 21844.941| N/A|  17,258|
| |Lucas County|     4| 465.116| N/A|    57|  6627.907| N/A|   8,600|
| |Clarke County|     3| 319.319| N/A|   195| 20755.721| N/A|   9,395|
| |Appanoose County|     3| 241.429| N/A|    47|  3782.392| N/A|  12,426|
| |Clayton County|     3| 170.950| N/A|   102|  5812.297| N/A|  17,549|
| |Lee County|     3| 89.135| N/A|   107|  3179.131| N/A|  33,657|
| |Henry County|     3| 150.346| N/A|   119|  5963.717| N/A|  19,954|
| |Crawford County|     3| 178.359| N/A|   726| 43162.901| N/A|  16,820|
| |Clinton County|     3| 64.615| N/A|   362|  7796.851| N/A|  46,429|
| |Sioux County|     3| 86.071| N/A|   614| 17615.837| N/A|  34,855|
| |O'Brien County|     2| 145.423| N/A|   135|  9816.040| N/A|  13,753|
| |Madison County|     2| 122.414| N/A|   114|  6977.598| N/A|  16,338|
| |Lyon County|     2| 170.140| N/A|   109|  9272.650| N/A|  11,755|
| |Jones County|     2| 96.707| N/A|   127|  6140.902| N/A|  20,681|
| |Hancock County|     2| 188.147| N/A|   121| 11382.879| N/A|  10,630|
| |Floyd County|     2| 127.861| N/A|   143|  9142.053| N/A|  15,642|
| |Emmet County|     2| 217.202| N/A|   188| 20417.029| N/A|   9,208|
| |Des Moines County|     2| 51.325| N/A|   152|  3900.737| N/A|  38,967|
| |Calhoun County|     2| 206.868| N/A|    83|  8585.023| N/A|   9,668|
| |Boone County|     2| 76.237| N/A|   244|  9300.907| N/A|  26,234|
| |Butler County|     2| 138.514| N/A|   119|  8241.568| N/A|  14,439|
| |Shelby County|     1| 87.306| N/A|   177| 15453.117| N/A|  11,454|
| |Wright County|     1| 79.605| N/A|   455| 36220.347| N/A|  12,562|
| |Winneshiek County|     1| 50.023| N/A|    91|  4552.048| N/A|  19,991|
| |Wayne County|     1| 155.255| N/A|    19|  2949.853| N/A|   6,441|
| |Warren County|     1| 19.430| N/A|   547| 10628.376| N/A|  51,466|
| |Van Buren County|     1| 141.965| N/A|    34|  4826.803| N/A|   7,044|
| |Union County|     1| 81.693| N/A|    75|  6126.950| N/A|  12,241|
| |Ringgold County|     1| 204.332| N/A|    21|  4290.969| N/A|   4,894|
| |Audubon County|     1| 181.951| N/A|    28|  5094.614| N/A|   5,496|
| |Jackson County|     1| 51.443| N/A|   148|  7613.560| N/A|  19,439|
| |Iowa County|     1| 61.789| N/A|    94|  5808.206| N/A|  16,184|
| |Humboldt County|     1| 104.624| N/A|   100| 10462.440| N/A|   9,558|
| |Hamilton County|     1| 67.691| N/A|   244| 16516.618| N/A|  14,773|
| |Grundy County|     1| 81.753| N/A|    76|  6213.211| N/A|  12,232|
| |Keokuk County|     1| 97.599| N/A|    33|  3220.769| N/A|  10,246|
| |Delaware County|     1| 58.785| N/A|    99|  5819.764| N/A|  17,011|
| |Pocahontas County|     1| 151.080| N/A|   115| 17374.226| N/A|   6,619|
| |Davis County|     1| 111.111| N/A|    52|  5777.778| N/A|   9,000|
| |Carroll County|     1| 49.591| N/A|   185|  9174.312| N/A|  20,165|
| |Cass County|     1| 77.906| N/A|    50|  3895.294| N/A|  12,836|
| |Cedar County|     1| 53.686| N/A|   128|  6871.745| N/A|  18,627|
| |Cherokee County|     1| 89.008| N/A|   103|  9167.779| N/A|  11,235|
| |Clay County|     1| 62.438| N/A|   176| 10989.011| N/A|  16,016|
| |Buchanan County|     1| 47.226| N/A|   123|  5808.737| N/A|  21,175|
| |Benton County|     1| 38.994| N/A|   146|  5693.118| N/A|  25,645|
| |Ida County|     0|  0.000| N/A|    29|  4227.405| N/A|   6,860|
| |Mills County|     0|  0.000| N/A|    85|  5625.786| N/A|  15,109|
| |Marion County|     0|  0.000| N/A|   162|  4871.741| N/A|  33,253|
| |Kossuth County|     0|  0.000| N/A|    83|  5603.186| N/A|  14,813|
| |Jefferson County|     0|  0.000| N/A|    80|  4372.779| N/A|  18,295|
| |Howard County|     0|  0.000| N/A|    49|  5350.513| N/A|   9,158|
| |Harrison County|     0|  0.000| N/A|   102|  7260.303| N/A|  14,049|
| |Hardin County|     0|  0.000| N/A|   173| 10269.500| N/A|  16,846|
| |Greene County|     0|  0.000| N/A|    39|  4387.939| N/A|   8,888|
| |Fremont County|     0|  0.000| N/A|    37|  5316.092| N/A|   6,960|
| |Fayette County|     0|  0.000| N/A|    81|  4122.137| N/A|  19,650|
| |Decatur County|     0|  0.000| N/A|    23|  2922.490| N/A|   7,870|
| |Chickasaw County|     0|  0.000| N/A|    54|  4525.266| N/A|  11,933|
| |Adams County|     0|  0.000| N/A|    16|  4441.977| N/A|   3,602|
| |Adair County|     0|  0.000| N/A|    27|  3775.168| N/A|   7,152|
| |Page County|     0|  0.000| N/A|    85|  5626.531| N/A|  15,107|
| |Osceola County|     0|  0.000| N/A|    79| 13259.483| N/A|   5,958|
| |Monona County|     0|  0.000| N/A|    91| 10562.972| N/A|   8,615|
| |Mitchell County|     0|  0.000| N/A|    78|  7368.222| N/A|  10,586|
| |Worth County|     0|  0.000| N/A|    65|  8806.395| N/A|   7,381|
| |Winnebago County|     0|  0.000| N/A|    77|  7436.739| N/A|  10,354|
| |Taylor County|     0|  0.000| N/A|    96| 15683.712| N/A|   6,121|
| |Sac County|     0|  0.000| N/A|    82|  8435.346| N/A|   9,721|
| |Palo Alto County|     0|  0.000| N/A|    80|  9002.926| N/A|   8,886|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   892| 289.596| N/A|53,229| 17281.268| N/A|3,080,156|
| |Clark County|   752| 331.758|  5.546|46,184| 20374.860| 377.576|2,266,715|
| |Washoe County|   117| 248.134|  1.818| 5,504| 11672.912| 163.302| 471,519|
| |Nye County|     9| 193.453| N/A|   374|  8039.034| N/A|  46,523|
| |Lyon County|     5| 86.941| N/A|   217|  3773.257| N/A|  57,510|
| |Humboldt County|     4| 237.657| N/A|    99|  5882.003| N/A|  16,831|
| |Elko County|     2| 37.895| N/A|   512|  9701.012| N/A|  52,778|
| |Lander County|     1| 180.766| N/A|    50|  9038.322| N/A|   5,532|
| |White Pine County|     1| 104.384| N/A|    14|  1461.378| N/A|   9,580|
| |Churchill County|     1| 40.146| N/A|    50|  2007.307| N/A|  24,909|
| |Pershing County|     0|  0.000| N/A|    13|  1933.086| N/A|   6,725|
| |Mineral County|     0|  0.000| N/A|    11|  2441.731| N/A|   4,505|
| |Lincoln County|     0|  0.000| N/A|     4|   771.754| N/A|   5,183|
| |Eureka County|     0|  0.000| N/A|     2|   985.707| N/A|   2,029|
| |Esmeralda County|     0|  0.000| N/A|     0|     0.000| N/A|     873|
| |Douglas County|     0|  0.000| N/A|   191|  3905.531| N/A|  48,905|
| |Carson City|     0|  0.000| N/A|     0|     0.000| N/A|  55,916|
| |Storey County|     0|  0.000| N/A|     4|   970.167| N/A|   4,123|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   760| 170.111| N/A|33,254|  7443.248| N/A|4,467,673|
| |Jefferson County|   237| 309.094|  1.118| 7,666|  9997.952| 182.401| 766,757|
| |Fayette County|    47| 145.442|  0.884| 2,943|  9107.169| 149.863| 323,152|
| |Kenton County|    39| 233.536|  1.711| 1,369|  8197.703| 100.087| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   416|  9309.403| 83.120|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,062|  7950.232| 103.736| 133,581|
| |Logan County|    23| 848.646|  5.271|   315| 11622.758| 94.880|  27,102|
| |Graves County|    23| 617.185|  3.833|   534| 14329.416| 241.507|  37,266|
| |Warren County|    22| 165.543|  0.000| 2,556| 19233.085| 246.165| 132,896|
| |Shelby County|    22| 448.760|  0.000|   732| 14931.462| 128.217|  49,024|
| |Adair County|    19| 989.480|  0.000|   205| 10675.971| 59.518|  19,202|
| |Butler County|    15| 1164.687|  0.000|   298| 23138.442| 88.738|  12,879|
| |Oldham County|    14| 209.584|  8.554|   596|  8922.289| 141.148|  66,799|
| |Jackson County|    14| 1050.341|  0.000|   145| 10878.536| 85.742|  13,329|
| |Campbell County|    13| 138.913|  0.000|   551|  5887.759| 103.803|  93,584|
| |Edmonson County|    12| 987.654|  0.000|    99|  8148.148| 117.578|  12,150|
| |Grayson County|    11| 416.241|  0.000|   192|  7265.297| 113.520|  26,427|
| |Casey County|    10| 618.850|  0.000|   161|  9963.488| 150.292|  16,159|
| |Muhlenberg County|    10| 326.563|  4.665|   622| 20312.194| 69.978|  30,622|
| |Ohio County|     8| 333.417| N/A|   345| 14378.595| N/A|  23,994|
| |Hardin County|     8| 72.099| N/A|   566|  5101.029| N/A| 110,958|
| |Knox County|     8| 256.863| N/A|   228|  7320.597| N/A|  31,145|
| |Daviess County|     8| 78.809| N/A|   740|  7289.850| N/A| 101,511|
| |Allen County|     8| 375.323| N/A|   224| 10509.031| N/A|  21,315|
| |Gallatin County|     8| 902.018| N/A|    80|  9020.183| N/A|   8,869|
| |Franklin County|     7| 137.279| N/A|   278|  5451.942| N/A|  50,991|
| |Simpson County|     7| 376.911| N/A|   146|  7861.297| N/A|  18,572|
| |Clark County|     7| 193.034| N/A|   168|  4632.821| N/A|  36,263|
| |Christian County|     6| 85.153| N/A|   481|  6826.471| N/A|  70,461|
| |Clay County|     5| 251.244| N/A|   148|  7436.812| N/A|  19,901|
| |Russell County|     5| 278.971| N/A|   101|  5635.217| N/A|  17,923|
| |Grant County|     5| 199.450| N/A|   107|  4268.220| N/A|  25,069|
| |McCracken County|     4| 61.145| N/A|   355|  5426.641| N/A|  65,418|
| |Lyon County|     4| 487.211| N/A|    33|  4019.488| N/A|   8,210|
| |Laurel County|     4| 65.775| N/A|   406|  6676.204| N/A|  60,813|
| |Henderson County|     4| 88.476| N/A|   334|  7387.746| N/A|  45,210|
| |Calloway County|     4| 102.561| N/A|   217|  5563.960| N/A|  39,001|
| |Bullitt County|     4| 48.974| N/A|   333|  4077.085| N/A|  81,676|
| |Harlan County|     3| 115.340| N/A|   219|  8419.839| N/A|  26,010|
| |Pike County|     3| 51.835| N/A|   233|  4025.848| N/A|  57,876|
| |Perry County|     3| 116.469| N/A|   203|  7881.047| N/A|  25,758|
| |Boyd County|     3| 64.215| N/A|   184|  3938.525| N/A|  46,718|
| |Bell County|     3| 115.243| N/A|   298| 11447.449| N/A|  26,032|
| |Barren County|     2| 45.199| N/A|   355|  8022.780| N/A|  44,249|
| |Carroll County|     2| 188.129| N/A|   150| 14109.679| N/A|  10,631|
| |Floyd County|     2| 56.197| N/A|    93|  2613.167| N/A|  35,589|
| |Green County|     2| 182.799| N/A|    31|  2833.379| N/A|  10,941|
| |Breckinridge County|     2| 97.671| N/A|    57|  2783.611| N/A|  20,477|
| |Nelson County|     2| 43.259| N/A|   205|  4434.062| N/A|  46,233|
| |Monroe County|     2| 187.793| N/A|    93|  8732.394| N/A|  10,650|
| |Henry County|     2| 124.023| N/A|   110|  6821.282| N/A|  16,126|
| |Marshall County|     2| 64.309| N/A|   131|  4212.219| N/A|  31,100|
| |Meade County|     2| 69.999| N/A|    93|  3254.935| N/A|  28,572|
| |Metcalfe County|     2| 198.590| N/A|    57|  5659.815| N/A|  10,071|
| |Taylor County|     2| 77.613| N/A|   106|  4113.470| N/A|  25,769|
| |Pulaski County|     2| 30.779| N/A|   268|  4124.409| N/A|  64,979|
| |Carter County|     1| 37.318| N/A|   101|  3769.079| N/A|  26,797|
| |Carlisle County|     1| 210.084| N/A|    36|  7563.025| N/A|   4,760|
| |Bourbon County|     1| 50.536| N/A|    75|  3790.176| N/A|  19,788|
| |Anderson County|     1| 43.962| N/A|    81|  3560.909| N/A|  22,747|
| |Bath County|     1| 80.000| N/A|    36|  2880.000| N/A|  12,500|
| |Crittenden County|     1| 113.559| N/A|    28|  3179.650| N/A|   8,806|
| |Fulton County|     1| 167.532| N/A|    71| 11894.790| N/A|   5,969|
| |Greenup County|     1| 28.492| N/A|   103|  2934.640| N/A|  35,098|
| |Livingston County|     1| 108.767| N/A|    33|  3589.297| N/A|   9,194|
| |Larue County|     1| 69.454| N/A|    53|  3681.067| N/A|  14,398|
| |Knott County|     1| 67.540| N/A|    49|  3309.469| N/A|  14,806|
| |Lincoln County|     1| 40.735| N/A|   100|  4073.486| N/A|  24,549|
| |McLean County|     1| 108.613| N/A|    43|  4670.360| N/A|   9,207|
| |Webster County|     1| 77.268| N/A|    84|  6490.496| N/A|  12,942|
| |Whitley County|     1| 27.576| N/A|   162|  4467.240| N/A|  36,264|
| |Mason County|     1| 58.582| N/A|    53|  3104.862| N/A|  17,070|
| |Madison County|     1| 10.754| N/A|   444|  4774.861| N/A|  92,987|
| |Hancock County|     0|  0.000| N/A|    49|  5617.978| N/A|   8,722|
| |Garrard County|     0|  0.000| N/A|    71|  4019.020| N/A|  17,666|
| |Fleming County|     0|  0.000| N/A|    58|  3977.779| N/A|  14,581|
| |Estill County|     0|  0.000| N/A|    18|  1276.053| N/A|  14,106|
| |Trimble County|     0|  0.000| N/A|    33|  3895.644| N/A|   8,471|
| |Trigg County|     0|  0.000| N/A|    54|  3685.755| N/A|  14,651|
| |Todd County|     0|  0.000| N/A|    34|  2765.577| N/A|  12,294|
| |Spencer County|     0|  0.000| N/A|   112|  5787.815| N/A|  19,351|
| |Scott County|     0|  0.000| N/A|   356|  6245.176| N/A|  57,004|
| |Union County|     0|  0.000| N/A|    62|  4311.244| N/A|  14,381|
| |Washington County|     0|  0.000| N/A|    72|  5952.873| N/A|  12,095|
| |Wayne County|     0|  0.000| N/A|    53|  2606.600| N/A|  20,333|
| |Wolfe County|     0|  0.000| N/A|    12|  1676.680| N/A|   7,157|
| |Menifee County|     0|  0.000| N/A|    29|  4469.102| N/A|   6,489|
| |Marion County|     0|  0.000| N/A|   119|  6174.441| N/A|  19,273|
| |Magoffin County|     0|  0.000| N/A|    34|  2795.823| N/A|  12,161|
| |McCreary County|     0|  0.000| N/A|    37|  2147.293| N/A|  17,231|
| |Lewis County|     0|  0.000| N/A|    37|  2787.194| N/A|  13,275|
| |Letcher County|     0|  0.000| N/A|    56|  2598.246| N/A|  21,553|
| |Leslie County|     0|  0.000| N/A|    28|  2834.869| N/A|   9,877|
| |Lee County|     0|  0.000| N/A|     5|   675.402| N/A|   7,403|
| |Lawrence County|     0|  0.000| N/A|    36|  2350.330| N/A|  15,317|
| |Johnson County|     0|  0.000| N/A|    46|  2073.193| N/A|  22,188|
| |Powell County|     0|  0.000| N/A|    51|  4126.547| N/A|  12,359|
| |Robertson County|     0|  0.000| N/A|     3|  1423.150| N/A|   2,108|
| |Rockcastle County|     0|  0.000| N/A|    62|  3713.687| N/A|  16,695|
| |Rowan County|     0|  0.000| N/A|    69|  2820.932| N/A|  24,460|
| |Woodford County|     0|  0.000| N/A|   148|  5536.022| N/A|  26,734|
| |Elliott County|     0|  0.000| N/A|     8|  1064.254| N/A|   7,517|
| |Mercer County|     0|  0.000| N/A|    80|  3647.472| N/A|  21,933|
| |Montgomery County|     0|  0.000| N/A|   116|  4119.757| N/A|  28,157|
| |Morgan County|     0|  0.000| N/A|    30|  2254.114| N/A|  13,309|
| |Nicholas County|     0|  0.000| N/A|    20|  2751.410| N/A|   7,269|
| |Cumberland County|     0|  0.000| N/A|    46|  6954.944| N/A|   6,614|
| |Clinton County|     0|  0.000| N/A|    28|  2740.262| N/A|  10,218|
| |Caldwell County|     0|  0.000| N/A|    49|  3844.042| N/A|  12,747|
| |Breathitt County|     0|  0.000| N/A|    28|  2216.944| N/A|  12,630|
| |Bracken County|     0|  0.000| N/A|    30|  3613.152| N/A|   8,303|
| |Boyle County|     0|  0.000| N/A|   149|  4956.753| N/A|  30,060|
| |Ballard County|     0|  0.000| N/A|    32|  4056.795| N/A|   7,888|
| |Hart County|     0|  0.000| N/A|    88|  4623.063| N/A|  19,035|
| |Jessamine County|     0|  0.000| N/A|   325|  6005.729| N/A|  54,115|
| |Martin County|     0|  0.000| N/A|    34|  3037.070| N/A|  11,195|
| |Pendleton County|     0|  0.000| N/A|    43|  2947.224| N/A|  14,590|
| |Owsley County|     0|  0.000| N/A|    12|  2718.007| N/A|   4,415|
| |Owen County|     0|  0.000| N/A|    44|  4036.327| N/A|  10,901|
| |Harrison County|     0|  0.000| N/A|   119|  6300.964| N/A|  18,886|
| |Hickman County|     0|  0.000| N/A|    39|  8904.110| N/A|   4,380|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   669| 319.053| N/A|20,488|  9770.945| N/A|2,096,829|
| |McKinley County|   222| 3110.681|  6.005| 4,033| 56510.712| 112.097|  71,367|
| |San Juan County|   183| 1476.306|  4.610| 3,026| 24411.494| 46.099| 123,958|
| |Bernalillo County|   129| 189.951|  2.524| 5,029|  7405.160| 71.731| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,117|  7611.688| 52.568| 146,748|
| |Dona Ana County|    27| 123.743|  5.238| 2,348| 10761.017| 136.837| 218,195|
| |Cibola County|    17| 637.301|  0.000|   346| 12970.947| 149.953|  26,675|
| |Otero County|    10| 148.170|  0.000|   197|  2918.951| 40.218|  67,490|
| |Chaves County|     6| 92.858| N/A|   411|  6360.752| N/A|  64,615|
| |Socorro County|     6| 360.642| N/A|    73|  4387.810| N/A|  16,637|
| |Rio Arriba County|     5| 128.465| N/A|   312|  8016.238| N/A|  38,921|
| |Eddy County|     4| 68.423| N/A|   278|  4755.388| N/A|  58,460|
| |Valencia County|     4| 52.159| N/A|   399|  5202.900| N/A|  76,688|
| |Lea County|     4| 56.283| N/A|   729| 10257.493| N/A|  71,070|
| |Luna County|     3| 126.534| N/A|   241| 10164.916| N/A|  23,709|
| |Santa Fe County|     3| 19.952| N/A|   618|  4110.190| N/A| 150,358|
| |Union County|     2| 492.732| N/A|    28|  6898.251| N/A|   4,059|
| |Curry County|     2| 40.855| N/A|   516| 10540.507| N/A|  48,954|
| |Grant County|     2| 74.080| N/A|    71|  2629.824| N/A|  26,998|
| |Roosevelt County|     1| 54.054| N/A|   157|  8486.486| N/A|  18,500|
| |Quay County|     1| 121.168| N/A|    34|  4119.714| N/A|   8,253|
| |Lincoln County|     1| 51.093| N/A|   117|  5977.928| N/A|  19,572|
| |Colfax County|     1| 83.745| N/A|    16|  1339.921| N/A|  11,941|
| |Catron County|     1| 283.527| N/A|     5|  1417.635| N/A|   3,527|
| |Taos County|     1| 30.560| N/A|   106|  3239.312| N/A|  32,723|
| |Torrance County|     1| 64.679| N/A|    61|  3945.411| N/A|  15,461|
| |Sierra County|     0|  0.000| N/A|    31|  2872.764| N/A|  10,791|
| |Guadalupe County|     0|  0.000| N/A|    31|  7209.302| N/A|   4,300|
| |San Miguel County|     0|  0.000| N/A|    42|  1539.759| N/A|  27,277|
| |Mora County|     0|  0.000| N/A|     6|  1327.140| N/A|   4,521|
| |Los Alamos County|     0|  0.000| N/A|    20|  1032.578| N/A|  19,369|
| |Hidalgo County|     0|  0.000| N/A|    89| 21200.572| N/A|   4,198|
| |Harding County|     0|  0.000| N/A|     1|  1600.000| N/A|     625|
| |De Baca County|     0|  0.000| N/A|     0|     0.000| N/A|   1,748|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   593| 149.862| N/A|41,395| 10461.285| N/A|3,956,971|
| |Oklahoma County|   109| 136.688|  2.329|10,113| 12681.927| 258.687| 797,434|
| |Tulsa County|   105| 161.154|  1.535| 9,969| 15300.390| 292.269| 651,552|
| |Cleveland County|    55| 193.652|  4.024| 2,909| 10242.453| 212.263| 284,014|
| |Washington County|    39| 756.885|  0.000|   606| 11760.824| 138.624|  51,527|
| |McCurtain County|    28| 852.827| 13.053|   839| 25554.337| 108.779|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   805|  9902.939| 231.977|  81,289|
| |Delaware County|    19| 441.768|  0.000|   412|  9579.390| 89.682|  43,009|
| |Rogers County|    16| 173.050|  4.635|   902|  9755.675| 242.579|  92,459|
| |Caddo County|    16| 556.290|  9.934|   392| 13629.094| 298.012|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   486|  7147.374| 157.570|  67,997|
| |Creek County|    13| 181.762|  1.997|   552|  7717.905| 167.781|  71,522|
| |Kay County|    11| 252.653|  3.281|   233|  5351.647| 91.874|  43,538|
| |Osage County|    11| 234.227|  0.000|   391|  8325.703| 136.886|  46,963|
| |Comanche County|    10| 82.816|  0.000|   795|  6583.905| 52.056| 120,749|
| |Pottawatomie County|     9| 123.981| N/A|   427|  5882.191| N/A|  72,592|
| |Greer County|     8| 1400.560| N/A|    82| 14355.742| N/A|   5,712|
| |Canadian County|     7| 47.200| N/A| 1,152|  7767.723| N/A| 148,306|
| |Texas County|     7| 350.298| N/A| 1,046| 52344.493| N/A|  19,983|
| |Grady County|     7| 125.372| N/A|   428|  7665.580| N/A|  55,834|
| |Adair County|     6| 270.343| N/A|   325| 14643.597| N/A|  22,194|
| |Mayes County|     6| 145.985| N/A|   305|  7420.925| N/A|  41,100|
| |Garfield County|     5| 81.892| N/A|   396|  6485.849| N/A|  61,056|
| |Jackson County|     5| 203.832| N/A|   504| 20546.270| N/A|  24,530|
| |Seminole County|     5| 206.118| N/A|   221|  9110.397| N/A|  24,258|
| |Payne County|     4| 48.909| N/A|   698|  8534.677| N/A|  81,784|
| |Sequoyah County|     4| 96.226| N/A|   309|  7433.424| N/A|  41,569|
| |McClain County|     4| 98.829| N/A|   424| 10475.861| N/A|  40,474|
| |Carter County|     4| 83.141| N/A|   326|  6775.997| N/A|  48,111|
| |Garvin County|     4| 144.347| N/A|   220|  7939.086| N/A|  27,711|
| |Okmulgee County|     3| 77.993| N/A|   441| 11464.968| N/A|  38,465|
| |Pittsburg County|     3| 68.722| N/A|   252|  5772.667| N/A|  43,654|
| |Pawnee County|     3| 183.195| N/A|   130|  7938.447| N/A|  16,376|
| |Ottawa County|     3| 96.379| N/A|   358| 11501.269| N/A|  31,127|
| |Cotton County|     2| 352.983| N/A|    18|  3176.844| N/A|   5,666|
| |Cherokee County|     2| 41.104| N/A|   391|  8035.843| N/A|  48,657|
| |Stephens County|     2| 46.357| N/A|   192|  4450.316| N/A|  43,143|
| |Noble County|     2| 179.678| N/A|    83|  7456.653| N/A|  11,131|
| |Lincoln County|     2| 57.344| N/A|   152|  4358.173| N/A|  34,877|
| |Pontotoc County|     2| 52.241| N/A|   188|  4910.668| N/A|  38,284|
| |Hughes County|     1| 75.307| N/A|   124|  9338.053| N/A|  13,279|
| |Tillman County|     1| 137.931| N/A|    58|  8000.000| N/A|   7,250|
| |Logan County|     1| 20.829| N/A|   198|  4124.055| N/A|  48,011|
| |Bryan County|     1| 20.836| N/A|   410|  8542.557| N/A|  47,995|
| |Choctaw County|     1| 68.157| N/A|   173| 11791.167| N/A|  14,672|
| |Beckham County|     1| 45.748| N/A|    52|  2378.883| N/A|  21,859|
| |Le Flore County|     1| 20.059| N/A|   298|  5977.574| N/A|  49,853|
| |Latimer County|     1| 99.275| N/A|    80|  7942.023| N/A|  10,073|
| |McIntosh County|     1| 51.031| N/A|   166|  8471.117| N/A|  19,596|
| |Major County|     1| 131.079| N/A|    27|  3539.127| N/A|   7,629|
| |Marshall County|     1| 59.063| N/A|   102|  6024.452| N/A|  16,931|
| |Kiowa County|     1| 114.837| N/A|    27|  3100.597| N/A|   8,708|
| |Nowata County|     1| 99.246| N/A|    57|  5657.007| N/A|  10,076|
| |Grant County|     0|  0.000| N/A|    12|  2769.444| N/A|   4,333|
| |Dewey County|     0|  0.000| N/A|     8|  1635.657| N/A|   4,891|
| |Custer County|     0|  0.000| N/A|   202|  6964.797| N/A|  29,003|
| |Craig County|     0|  0.000| N/A|    78|  5515.486| N/A|  14,142|
| |Coal County|     0|  0.000| N/A|    31|  5641.492| N/A|   5,495|
| |Cimarron County|     0|  0.000| N/A|     1|   467.946| N/A|   2,137|
| |Blaine County|     0|  0.000| N/A|    40|  4242.231| N/A|   9,429|
| |Beaver County|     0|  0.000| N/A|    36|  6778.384| N/A|   5,311|
| |Atoka County|     0|  0.000| N/A|    67|  4869.894| N/A|  13,758|
| |Alfalfa County|     0|  0.000| N/A|     3|   526.131| N/A|   5,702|
| |Ellis County|     0|  0.000| N/A|     3|   777.403| N/A|   3,859|
| |Harmon County|     0|  0.000| N/A|    27| 10177.158| N/A|   2,653|
| |Haskell County|     0|  0.000| N/A|    50|  3959.769| N/A|  12,627|
| |Harper County|     0|  0.000| N/A|     9|  2440.347| N/A|   3,688|
| |Washita County|     0|  0.000| N/A|    26|  2381.825| N/A|  10,916|
| |Woodward County|     0|  0.000| N/A|    36|  1781.208| N/A|  20,211|
| |Woods County|     0|  0.000| N/A|    19|  2160.810| N/A|   8,793|
| |Roger Mills County|     0|  0.000| N/A|     8|  2232.766| N/A|   3,583|
| |Pushmataha County|     0|  0.000| N/A|   105|  9462.870| N/A|  11,096|
| |Okfuskee County|     0|  0.000| N/A|    60|  5002.918| N/A|  11,993|
| |Murray County|     0|  0.000| N/A|    69|  4903.006| N/A|  14,073|
| |Love County|     0|  0.000| N/A|    69|  6729.738| N/A|  10,253|
| |Kingfisher County|     0|  0.000| N/A|   115|  7294.640| N/A|  15,765|
| |Johnston County|     0|  0.000| N/A|    45|  4059.540| N/A|  11,085|
| |Jefferson County|     0|  0.000| N/A|    32|  5331.556| N/A|   6,002|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   587| 831.740| N/A|12,518| 17737.184| N/A| 705,749|
| |District of Columbia|   587| 831.740|  0.607|12,518| 17737.184| 93.315| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   587| 602.815| N/A|15,125| 15532.511| N/A| 973,764|
| |New Castle County|   289| 517.223|  1.023| 7,092| 12692.549| 89.229| 558,753|
| |Sussex County|   191| 815.455|  0.000| 5,786| 24702.743| 123.813| 234,225|
| |Kent County|   107| 591.860|  9.482| 2,247| 12429.060| 75.859| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   515| 170.654| N/A|45,295| 15009.258| N/A|3,017,804|
| |Pulaski County|    81| 206.680|  1.823| 5,222| 13324.454| 207.044| 391,911|
| |Washington County|    51| 213.222|  4.778| 6,188| 25870.971| 198.888| 239,187|
| |Benton County|    40| 143.297|  2.559| 4,663| 16704.819| 130.502| 279,141|
| |Jefferson County|    40| 598.587|  6.413| 1,423| 21294.744| 327.085|  66,824|
| |Crittenden County|    20| 417.058|  8.937| 1,315| 27421.541| 536.217|  47,955|
| |Union County|    17| 439.481|  3.693|   464| 11995.243| 251.132|  38,682|
| |Sebastian County|    17| 132.992|  3.353| 2,038| 15943.424| 488.383| 127,827|
| |Yell County|    14| 656.014|  0.000| 1,055| 49435.359| 428.417|  21,341|
| |Mississippi County|    13| 319.795| 17.571|   914| 22484.072| 934.786|  40,651|
| |Hot Spring County|    12| 355.334| 21.151| 1,484| 43943.028| 232.659|  33,771|
| |Craighead County|    12| 108.763|  1.295| 1,264| 11456.332| 261.548| 110,332|
| |Lincoln County|    11| 844.595|  0.000| 1,197| 91907.248| 394.875|  13,024|
| |Pope County|    10| 156.074|  4.459| 1,276| 19915.096| 280.934|  64,072|
| |Sevier County|    10| 587.993|  0.000|   969| 56976.539| 352.796|  17,007|
| |Lawrence County|     9| 548.580| N/A|   205| 12495.429| N/A|  16,406|
| |Nevada County|     9| 1090.645| N/A|   136| 16480.853| N/A|   8,252|
| |Lee County|     8| 903.240| N/A|   890| 100485.492| N/A|   8,857|
| |Chicot County|     8| 790.670| N/A|   707| 69875.469| N/A|  10,118|
| |Garland County|     8| 80.494| N/A|   939|  9448.011| N/A|  99,386|
| |Columbia County|     8| 341.050| N/A|   209|  8909.920| N/A|  23,457|
| |Phillips County|     7| 393.657| N/A|   298| 16758.520| N/A|  17,782|
| |Carroll County|     7| 246.653| N/A|   350| 12332.629| N/A|  28,380|
| |Newton County|     6| 773.894| N/A|   102| 13156.198| N/A|   7,753|
| |Saline County|     6| 49.005| N/A|   975|  7963.279| N/A| 122,437|
| |Sharp County|     5| 286.664| N/A|   107|  6134.618| N/A|  17,442|
| |Ashley County|     5| 254.362| N/A|   298| 15159.994| N/A|  19,657|
| |Miller County|     5| 115.588| N/A|   495| 11443.235| N/A|  43,257|
| |Cleburne County|     5| 200.650| N/A|   188|  7544.444| N/A|  24,919|
| |Faulkner County|     5| 39.680| N/A| 1,252|  9935.956| N/A| 126,007|
| |Clay County|     4| 274.895| N/A|   118|  8109.408| N/A|  14,551|
| |Bradley County|     3| 278.733| N/A|   173| 16073.585| N/A|  10,763|
| |Howard County|     3| 227.238| N/A|   322| 24390.244| N/A|  13,202|
| |Crawford County|     3| 47.426| N/A|   582|  9200.563| N/A|  63,257|
| |Cross County|     3| 182.715| N/A|   183| 11145.624| N/A|  16,419|
| |Poinsett County|     3| 127.508| N/A|   217|  9223.053| N/A|  23,528|
| |Conway County|     3| 143.913| N/A|   143|  6859.829| N/A|  20,846|
| |Randolph County|     3| 167.056| N/A|   199| 11081.412| N/A|  17,958|
| |St. Francis County|     3| 120.029| N/A| 1,165| 46611.187| N/A|  24,994|
| |Drew County|     3| 164.663| N/A|   182|  9989.571| N/A|  18,219|
| |Desha County|     2| 176.041| N/A|   179| 15755.655| N/A|  11,361|
| |Franklin County|     2| 112.899| N/A|   119|  6717.471| N/A|  17,715|
| |Hempstead County|     2| 92.885| N/A|   227| 10542.448| N/A|  21,532|
| |Johnson County|     2| 75.250| N/A|   652| 24531.567| N/A|  26,578|
| |Cleveland County|     2| 251.383| N/A|    87| 10935.143| N/A|   7,956|
| |Lafayette County|     2| 301.932| N/A|    52|  7850.242| N/A|   6,624|
| |Madison County|     2| 120.656| N/A|   269| 16228.282| N/A|  16,576|
| |Lonoke County|     2| 27.282| N/A|   482|  6574.909| N/A|  73,309|
| |Van Buren County|     2| 120.882| N/A|    52|  3142.943| N/A|  16,545|
| |White County|     2| 25.396| N/A|   289|  3669.701| N/A|  78,753|
| |Ouachita County|     2| 85.536| N/A|    84|  3592.507| N/A|  23,382|
| |Pike County|     1| 93.301| N/A|    91|  8490.390| N/A|  10,718|
| |Polk County|     1| 50.090| N/A|   137|  6862.352| N/A|  19,964|
| |Stone County|     1| 79.962| N/A|    61|  4877.659| N/A|  12,506|
| |Boone County|     1| 26.715| N/A|   193|  5156.016| N/A|  37,432|
| |Little River County|     1| 81.573| N/A|   164| 13377.926| N/A|  12,259|
| |Greene County|     1| 22.063| N/A|   445|  9817.981| N/A|  45,325|
| |Arkansas County|     1| 57.189| N/A|   208| 11895.230| N/A|  17,486|
| |Clark County|     1| 44.803| N/A|   175|  7840.502| N/A|  22,320|
| |Montgomery County|     1| 111.284| N/A|    34|  3783.663| N/A|   8,986|
| |Logan County|     1| 46.585| N/A|   225| 10481.692| N/A|  21,466|
| |Jackson County|     1| 59.812| N/A|    63|  3768.168| N/A|  16,719|
| |Izard County|     1| 73.373| N/A|    47|  3448.529| N/A|  13,629|
| |Independence County|     1| 26.438| N/A|   443| 11711.831| N/A|  37,825|
| |Calhoun County|     0|  0.000| N/A|    13|  2505.300| N/A|   5,189|
| |Baxter County|     0|  0.000| N/A|    68|  1621.673| N/A|  41,932|
| |Dallas County|     0|  0.000| N/A|    59|  8417.749| N/A|   7,009|
| |Fulton County|     0|  0.000| N/A|    30|  2404.424| N/A|  12,477|
| |Woodruff County|     0|  0.000| N/A|    20|  3164.557| N/A|   6,320|
| |Scott County|     0|  0.000| N/A|    51|  4960.607| N/A|  10,281|
| |Prairie County|     0|  0.000| N/A|    80|  9923.096| N/A|   8,062|
| |Perry County|     0|  0.000| N/A|    50|  4782.401| N/A|  10,455|
| |Monroe County|     0|  0.000| N/A|    55|  8207.730| N/A|   6,701|
| |Marion County|     0|  0.000| N/A|    25|  1497.544| N/A|  16,694|
| |Grant County|     0|  0.000| N/A|   131|  7172.187| N/A|  18,265|
| |Searcy County|     0|  0.000| N/A|    28|  3552.849| N/A|   7,881|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,739|  4956.200| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.685| 3,807|  9128.949| 30.831| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,665|  5374.973| 23.981| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   460|  3038.490|  3.775| 151,391|
| |Strafford County|    13| 99.515|  0.000|   346|  2648.642| 25.152| 130,633|
| |Belknap County|     4| 65.250| N/A|   113|  1843.303| N/A|  61,303|
| |Cheshire County|     3| 39.430| N/A|    96|  1261.747| N/A|  76,085|
| |Grafton County|     1| 11.125| N/A|   103|  1145.896| N/A|  89,886|
| |Carroll County|     1| 20.446| N/A|    93|  1901.452| N/A|  48,910|
| |Sullivan County|     1| 23.177| N/A|    40|   927.085| N/A|  43,146|
| |Coos County|     0|  0.000| N/A|    16|   506.923| N/A|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   377| 129.406| N/A|29,617| 10166.086| N/A|2,913,314|
| |Johnson County|   102| 169.322|  0.949| 5,439|  9028.869| 156.042| 602,401|
| |Wyandotte County|    98| 592.399|  2.591| 4,740| 28652.776| 358.376| 165,429|
| |Sedgwick County|    44| 85.264|  1.384| 4,603|  8919.817| 177.450| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,494|  8446.643| 92.882| 176,875|
| |Lyon County|    13| 391.625|  8.607|   686| 20665.763| 197.964|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,780| 48811.254| 250.716|  36,467|
| |Phillips County|     8| 1528.468| N/A|    51|  9743.982| N/A|   5,234|
| |Coffey County|     8| 978.115| N/A|    67|  8191.710| N/A|   8,179|
| |Leavenworth County|     8| 97.850| N/A| 1,444| 17661.880| N/A|  81,758|
| |Ford County|     8| 237.961| N/A| 2,055| 61126.149| N/A|  33,619|
| |Riley County|     5| 67.356| N/A|   465|  6264.145| N/A|  74,232|
| |Montgomery County|     5| 157.089| N/A|   162|  5089.698| N/A|  31,829|
| |Saline County|     5| 92.210| N/A|   362|  6676.011| N/A|  54,224|
| |Douglas County|     5| 40.897| N/A|   696|  5692.832| N/A| 122,259|
| |Seward County|     4| 186.672| N/A| 1,215| 56701.512| N/A|  21,428|
| |Sumner County|     3| 131.372| N/A|    98|  4291.470| N/A|  22,836|
| |Barton County|     3| 116.374| N/A|   126|  4887.699| N/A|  25,779|
| |Clay County|     2| 249.938| N/A|    18|  2249.438| N/A|   8,002|
| |Cowley County|     2| 57.293| N/A|   160|  4583.477| N/A|  34,908|
| |Morton County|     2| 773.096| N/A|     9|  3478.933| N/A|   2,587|
| |Geary County|     2| 63.151| N/A|   134|  4231.134| N/A|  31,670|
| |Grant County|     2| 279.720| N/A|   101| 14125.874| N/A|   7,150|
| |Bourbon County|     2| 137.608| N/A|    73|  5022.705| N/A|  14,534|
| |Butler County|     1| 14.945| N/A|   238|  3556.964| N/A|  66,911|
| |Franklin County|     1| 39.148| N/A|   172|  6733.479| N/A|  25,544|
| |Harvey County|     1| 29.045| N/A|   181|  5257.196| N/A|  34,429|
| |Jackson County|     1| 75.924| N/A|   146| 11084.959| N/A|  13,171|
| |Clark County|     1| 501.505| N/A|    45| 22567.703| N/A|   1,994|
| |Cherokee County|     1| 50.153| N/A|    91|  4563.920| N/A|  19,939|
| |Crawford County|     1| 25.761| N/A|   377|  9711.989| N/A|  38,818|
| |Dickinson County|     1| 54.154| N/A|    44|  2382.758| N/A|  18,466|
| |Ellis County|     1| 35.023| N/A|   135|  4728.050| N/A|  28,553|
| |Trego County|     1| 356.761| N/A|     5|  1783.803| N/A|   2,803|
| |Stafford County|     1| 240.616| N/A|     3|   721.848| N/A|   4,156|
| |Reno County|     1| 16.130| N/A|   247|  3983.999| N/A|  61,998|
| |Nemaha County|     1| 97.742| N/A|    48|  4691.623| N/A|  10,231|
| |Marion County|     1| 84.147| N/A|    46|  3870.751| N/A|  11,884|
| |McPherson County|     1| 35.036| N/A|   137|  4799.944| N/A|  28,542|
| |Kearny County|     1| 260.552| N/A|    57| 14851.485| N/A|   3,838|
| |Stanton County|     1| 498.504| N/A|    16|  7976.072| N/A|   2,006|
| |Pottawatomie County|     0|  0.000| N/A|   106|  4347.291| N/A|  24,383|
| |Rawlins County|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Sherman County|     0|  0.000| N/A|    15|  2535.068| N/A|   5,917|
| |Sheridan County|     0|  0.000| N/A|     7|  2776.676| N/A|   2,521|
| |Scott County|     0|  0.000| N/A|    34|  7049.554| N/A|   4,823|
| |Russell County|     0|  0.000| N/A|    13|  1896.149| N/A|   6,856|
| |Rush County|     0|  0.000| N/A|     6|  1976.285| N/A|   3,036|
| |Rooks County|     0|  0.000| N/A|    16|  3252.033| N/A|   4,920|
| |Rice County|     0|  0.000| N/A|    35|  3669.917| N/A|   9,537|
| |Republic County|     0|  0.000| N/A|    32|  6902.502| N/A|   4,636|
| |Pratt County|     0|  0.000| N/A|    33|  3601.048| N/A|   9,164|
| |Mitchell County|     0|  0.000| N/A|    27|  4515.805| N/A|   5,979|
| |Pawnee County|     0|  0.000| N/A|     7|  1091.363| N/A|   6,414|
| |Ottawa County|     0|  0.000| N/A|    32|  5610.098| N/A|   5,704|
| |Osborne County|     0|  0.000| N/A|     4|  1169.249| N/A|   3,421|
| |Osage County|     0|  0.000| N/A|    38|  2382.595| N/A|  15,949|
| |Norton County|     0|  0.000| N/A|    23|  4290.244| N/A|   5,361|
| |Ness County|     0|  0.000| N/A|     6|  2181.818| N/A|   2,750|
| |Neosho County|     0|  0.000| N/A|    56|  3498.469| N/A|  16,007|
| |Smith County|     0|  0.000| N/A|     3|   837.287| N/A|   3,583|
| |Stevens County|     0|  0.000| N/A|    45|  8204.193| N/A|   5,485|
| |Thomas County|     0|  0.000| N/A|    35|  4500.450| N/A|   7,777|
| |Wabaunsee County|     0|  0.000| N/A|    42|  6059.732| N/A|   6,931|
| |Marshall County|     0|  0.000| N/A|     9|   927.166| N/A|   9,707|
| |Anderson County|     0|  0.000| N/A|    29|  3690.506| N/A|   7,858|
| |Allen County|     0|  0.000| N/A|    15|  1212.709| N/A|  12,369|
| |Elk County|     0|  0.000| N/A|     1|   395.257| N/A|   2,530|
| |Ellsworth County|     0|  0.000| N/A|    21|  3441.495| N/A|   6,102|
| |Gove County|     0|  0.000| N/A|     6|  2276.176| N/A|   2,636|
| |Graham County|     0|  0.000| N/A|    16|  6446.414| N/A|   2,482|
| |Logan County|     0|  0.000| N/A|     2|   715.820| N/A|   2,794|
| |Linn County|     0|  0.000| N/A|    36|  3710.193| N/A|   9,703|
| |Lincoln County|     0|  0.000| N/A|     6|  2025.658| N/A|   2,962|
| |Lane County|     0|  0.000| N/A|     5|  3257.329| N/A|   1,535|
| |Labette County|     0|  0.000| N/A|   123|  6269.752| N/A|  19,618|
| |Kiowa County|     0|  0.000| N/A|     7|  2828.283| N/A|   2,475|
| |Kingman County|     0|  0.000| N/A|    12|  1677.852| N/A|   7,152|
| |Jewell County|     0|  0.000| N/A|    10|  3473.428| N/A|   2,879|
| |Jefferson County|     0|  0.000| N/A|    75|  3938.455| N/A|  19,043|
| |Hodgeman County|     0|  0.000| N/A|    11|  6131.550| N/A|   1,794|
| |Haskell County|     0|  0.000| N/A|    44| 11088.710| N/A|   3,968|
| |Harper County|     0|  0.000| N/A|    10|  1839.588| N/A|   5,436|
| |Atchison County|     0|  0.000| N/A|    64|  3981.833| N/A|  16,073|
| |Meade County|     0|  0.000| N/A|    42| 10414.084| N/A|   4,033|
| |Barber County|     0|  0.000| N/A|     4|   903.546| N/A|   4,427|
| |Chase County|     0|  0.000| N/A|    42| 15861.027| N/A|   2,648|
| |Woodson County|     0|  0.000| N/A|    11|  3505.417| N/A|   3,138|
| |Wilson County|     0|  0.000| N/A|    10|  1173.021| N/A|   8,525|
| |Wichita County|     0|  0.000| N/A|     4|  1887.683| N/A|   2,119|
| |Washington County|     0|  0.000| N/A|     3|   554.939| N/A|   5,406|
| |Wallace County|     0|  0.000| N/A|     0|     0.000| N/A|   1,518|
| |Morris County|     0|  0.000| N/A|    11|  1957.295| N/A|   5,620|
| |Miami County|     0|  0.000| N/A|   133|  3884.686| N/A|  34,237|
| |Brown County|     0|  0.000| N/A|    35|  3659.557| N/A|   9,564|
| |Edwards County|     0|  0.000| N/A|    10|  3573.981| N/A|   2,798|
| |Doniphan County|     0|  0.000| N/A|    47|  6184.211| N/A|   7,600|
| |Decatur County|     0|  0.000| N/A|     5|  1768.659| N/A|   2,827|
| |Comanche County|     0|  0.000| N/A|     3|  1764.706| N/A|   1,700|
| |Cloud County|     0|  0.000| N/A|    30|  3414.523| N/A|   8,786|
| |Cheyenne County|     0|  0.000| N/A|     2|   752.729| N/A|   2,657|
| |Chautauqua County|     0|  0.000| N/A|     5|  1538.462| N/A|   3,250|
| |Hamilton County|     0|  0.000| N/A|    37| 14572.666| N/A|   2,539|
| |Greenwood County|     0|  0.000| N/A|    20|  3343.363| N/A|   5,982|
| |Greeley County|     0|  0.000| N/A|     3|  2435.065| N/A|   1,232|
| |Gray County|     0|  0.000| N/A|    77| 12859.051| N/A|   5,988|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   340| 175.764| N/A|27,674| 14306.186| N/A|1,934,408|
| |Douglas County|   131| 229.291|  1.000|11,022| 19291.929| 243.043| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,734| 28262.677| 76.839|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,915| 95625.687| 135.538|  20,026|
| |Lancaster County|    17| 53.277|  1.343| 3,219| 10088.063| 112.821| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    99| 10617.761| 107.250|   9,324|
| |Adams County|    11| 350.732|  0.000|   350| 11159.647| 63.769|  31,363|
| |Sarpy County|     9| 48.078| N/A| 2,179| 11640.206| N/A| 187,196|
| |Dawson County|     9| 381.437| N/A|   954| 40432.295| N/A|  23,595|
| |Dodge County|     8| 218.788| N/A|   788| 21550.663| N/A|  36,565|
| |Scotts Bluff County|     6| 168.454| N/A|   297|  8338.481| N/A|  35,618|
| |Perkins County|     6| 2075.406| N/A|    17|  5880.318| N/A|   2,891|
| |Madison County|     5| 142.454| N/A|   434| 12365.025| N/A|  35,099|
| |Gage County|     4| 185.934| N/A|    87|  4044.066| N/A|  21,513|
| |Thurston County|     4| 553.710| N/A|   205| 28377.630| N/A|   7,224|
| |Howard County|     4| 620.636| N/A|    55|  8533.747| N/A|   6,445|
| |Custer County|     4| 371.161| N/A|    42|  3897.188| N/A|  10,777|
| |Colfax County|     4| 373.518| N/A|   698| 65178.822| N/A|  10,709|
| |Platte County|     3| 89.633| N/A|   783| 23394.084| N/A|  33,470|
| |Cass County|     2| 76.196| N/A|   169|  6438.586| N/A|  26,248|
| |Dixon County|     2| 354.862| N/A|    57| 10113.556| N/A|   5,636|
| |Lincoln County|     2| 57.284| N/A|    97|  2778.255| N/A|  34,914|
| |Saunders County|     2| 92.687| N/A|   150|  6951.525| N/A|  21,578|
| |Saline County|     2| 140.607| N/A|   594| 41760.405| N/A|  14,224|
| |Washington County|     1| 48.242| N/A|   116|  5596.025| N/A|  20,729|
| |Furnas County|     1| 213.858| N/A|    15|  3207.870| N/A|   4,676|
| |Richardson County|     1| 127.146| N/A|    21|  2670.057| N/A|   7,865|
| |Seward County|     1| 57.857| N/A|   110|  6364.268| N/A|  17,284|
| |Fillmore County|     1| 183.083| N/A|    24|  4393.995| N/A|   5,462|
| |Buffalo County|     1| 20.137| N/A|   385|  7752.875| N/A|  49,659|
| |Antelope County|     1| 158.781| N/A|    19|  3016.831| N/A|   6,298|
| |Keith County|     0|  0.000| N/A|    20|  2489.420| N/A|   8,034|
| |Nuckolls County|     0|  0.000| N/A|     5|  1205.400| N/A|   4,148|
| |Nemaha County|     0|  0.000| N/A|    25|  3585.772| N/A|   6,972|
| |Nance County|     0|  0.000| N/A|     8|  2273.373| N/A|   3,519|
| |Morrill County|     0|  0.000| N/A|    58| 12494.614| N/A|   4,642|
| |Merrick County|     0|  0.000| N/A|    59|  7607.995| N/A|   7,755|
| |Loup County|     0|  0.000| N/A|     0|     0.000| N/A|     664|
| |Logan County|     0|  0.000| N/A|     0|     0.000| N/A|     748|
| |Knox County|     0|  0.000| N/A|    34|  4080.653| N/A|   8,332|
| |Kimball County|     0|  0.000| N/A|    15|  4129.956| N/A|   3,632|
| |Keya Paha County|     0|  0.000| N/A|     0|     0.000| N/A|     806|
| |Kearney County|     0|  0.000| N/A|    49|  7544.265| N/A|   6,495|
| |York County|     0|  0.000| N/A|    77|  5629.066| N/A|  13,679|
| |Johnson County|     0|  0.000| N/A|    13|  2563.597| N/A|   5,071|
| |Jefferson County|     0|  0.000| N/A|    15|  2128.867| N/A|   7,046|
| |Pierce County|     0|  0.000| N/A|    19|  2658.086| N/A|   7,148|
| |Polk County|     0|  0.000| N/A|    26|  4987.531| N/A|   5,213|
| |Red Willow County|     0|  0.000| N/A|    16|  1491.981| N/A|  10,724|
| |Rock County|     0|  0.000| N/A|     3|  2210.759| N/A|   1,357|
| |Otoe County|     0|  0.000| N/A|    44|  2747.939| N/A|  16,012|
| |Pawnee County|     0|  0.000| N/A|     9|  3444.317| N/A|   2,613|
| |Phelps County|     0|  0.000| N/A|    37|  4095.639| N/A|   9,034|
| |McPherson County|     0|  0.000| N/A|     5| 10121.457| N/A|     494|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|     783|
| |Garden County|     0|  0.000| N/A|     4|  2177.463| N/A|   1,837|
| |Boyd County|     0|  0.000| N/A|     4|  2084.419| N/A|   1,919|
| |Burt County|     0|  0.000| N/A|    29|  4489.859| N/A|   6,459|
| |Hayes County|     0|  0.000| N/A|     0|     0.000| N/A|     922|
| |Butler County|     0|  0.000| N/A|    58|  7235.529| N/A|   8,016|
| |Harlan County|     0|  0.000| N/A|     1|   295.858| N/A|   3,380|
| |Greeley County|     0|  0.000| N/A|     9|  3820.034| N/A|   2,356|
| |Grant County|     0|  0.000| N/A|     0|     0.000| N/A|     623|
| |Gosper County|     0|  0.000| N/A|    19|  9547.739| N/A|   1,990|
| |Garfield County|     0|  0.000| N/A|     3|  1523.616| N/A|   1,969|
| |Frontier County|     0|  0.000| N/A|     3|  1141.987| N/A|   2,627|
| |Webster County|     0|  0.000| N/A|     9|  2581.015| N/A|   3,487|
| |Franklin County|     0|  0.000| N/A|    12|  4028.197| N/A|   2,979|
| |Dundy County|     0|  0.000| N/A|     1|   590.667| N/A|   1,693|
| |Deuel County|     0|  0.000| N/A|     2|  1114.827| N/A|   1,794|
| |Dawes County|     0|  0.000| N/A|     9|  1047.852| N/A|   8,589|
| |Cuming County|     0|  0.000| N/A|    67|  7574.045| N/A|   8,846|
| |Clay County|     0|  0.000| N/A|    49|  7899.404| N/A|   6,203|
| |Cheyenne County|     0|  0.000| N/A|    26|  2918.070| N/A|   8,910|
| |Cherry County|     0|  0.000| N/A|     4|   703.111| N/A|   5,689|
| |Chase County|     0|  0.000| N/A|     6|  1529.052| N/A|   3,924|
| |Cedar County|     0|  0.000| N/A|    22|  2618.424| N/A|   8,402|
| |Wayne County|     0|  0.000| N/A|    37|  3942.461| N/A|   9,385|
| |Valley County|     0|  0.000| N/A|    10|  2405.002| N/A|   4,158|
| |Thomas County|     0|  0.000| N/A|     1|  1385.042| N/A|     722|
| |Thayer County|     0|  0.000| N/A|    26|  5196.882| N/A|   5,003|
| |Stanton County|     0|  0.000| N/A|    28|  4729.730| N/A|   5,920|
| |Sioux County|     0|  0.000| N/A|     5|  4288.165| N/A|   1,166|
| |Sherman County|     0|  0.000| N/A|    11|  3665.445| N/A|   3,001|
| |Sheridan County|     0|  0.000| N/A|     9|  1715.593| N/A|   5,246|
| |Hooker County|     0|  0.000| N/A|     4|  5865.103| N/A|     682|
| |Holt County|     0|  0.000| N/A|    12|  1192.014| N/A|  10,067|
| |Hitchcock County|     0|  0.000| N/A|     1|   362.056| N/A|   2,762|
| |Brown County|     0|  0.000| N/A|     0|     0.000| N/A|   2,955|
| |Box Butte County|     0|  0.000| N/A|    11|  1020.124| N/A|  10,783|
| |Boone County|     0|  0.000| N/A|     7|  1348.228| N/A|   5,192|
| |Blaine County|     0|  0.000| N/A|     0|     0.000| N/A|     465|
| |Banner County|     0|  0.000| N/A|     2|  2684.564| N/A|     745|
| |Arthur County|     0|  0.000| N/A|     1|  2159.827| N/A|     463|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   339| 80.375| N/A|20,224|  4794.988| N/A|4,217,737|
| |Multnomah County|    93| 114.412|  0.527| 4,653|  5724.268| 69.069| 812,855|
| |Marion County|    68| 195.505|  0.411| 2,789|  8018.561| 105.145| 347,818|
| |Clackamas County|    38| 90.868|  0.683| 1,484|  3548.652| 49.534| 418,187|
| |Umatilla County|    26| 333.547|  7.331| 2,167| 27799.872| 485.659|  77,950|
| |Washington County|    24| 39.894|  0.475| 2,943|  4892.020| 57.704| 601,592|
| |Malheur County|    12| 392.529| 14.019|   734| 24009.682| 467.296|  30,571|
| |Yamhill County|    12| 112.045|  2.668|   413|  3856.209| 126.717| 107,100|
| |Polk County|    12| 139.397|  0.000|   301|  3496.544| 41.487|  86,085|
| |Linn County|    10| 77.072|  0.000|   265|  2042.405| 35.233| 129,749|
| |Lincoln County|     9| 180.137| N/A|   411|  8226.252| N/A|  49,962|
| |Deschutes County|     8| 40.467| N/A|   567|  2868.098| N/A| 197,692|
| |Benton County|     6| 64.479| N/A|   161|  1730.197| N/A|  93,053|
| |Lane County|     3|  7.852| N/A|   552|  1444.773| N/A| 382,067|
| |Jefferson County|     3| 121.664| N/A|   341| 13829.183| N/A|  24,658|
| |Morrow County|     3| 258.554| N/A|   329| 28354.736| N/A|  11,603|
| |Wasco County|     3| 112.435| N/A|   178|  6671.164| N/A|  26,682|
| |Josephine County|     2| 22.861| N/A|   110|  1257.330| N/A|  87,487|
| |Union County|     2| 74.530| N/A|   392| 14607.788| N/A|  26,835|
| |Douglas County|     1|  9.011| N/A|   145|  1306.542| N/A| 110,980|
| |Crook County|     1| 40.977| N/A|    43|  1762.006| N/A|  24,404|
| |Wallowa County|     1| 138.735| N/A|    19|  2635.960| N/A|   7,208|
| |Klamath County|     1| 14.655| N/A|   200|  2930.918| N/A|  68,238|
| |Jackson County|     1|  4.526| N/A|   437|  1977.877| N/A| 220,944|
| |Lake County|     0|  0.000| N/A|    32|  4066.590| N/A|   7,869|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|   1,332|
| |Tillamook County|     0|  0.000| N/A|    34|  1257.582| N/A|  27,036|
| |Sherman County|     0|  0.000| N/A|    15|  8426.966| N/A|   1,780|
| |Hood River County|     0|  0.000| N/A|   178|  7612.694| N/A|  23,382|
| |Harney County|     0|  0.000| N/A|    10|  1352.631| N/A|   7,393|
| |Grant County|     0|  0.000| N/A|     3|   416.725| N/A|   7,199|
| |Gilliam County|     0|  0.000| N/A|     4|  2092.050| N/A|   1,912|
| |Curry County|     0|  0.000| N/A|    14|   610.687| N/A|  22,925|
| |Coos County|     0|  0.000| N/A|    90|  1395.630| N/A|  64,487|
| |Columbia County|     0|  0.000| N/A|    90|  1719.066| N/A|  52,354|
| |Clatsop County|     0|  0.000| N/A|    83|  2063.445| N/A|  40,224|
| |Baker County|     0|  0.000| N/A|    37|  2294.716| N/A|  16,124|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   272| 84.842| N/A|34,114| 10640.813| N/A|3,205,958|
| |Salt Lake County|   186| 160.284|  1.847|20,082| 17305.550| 155.730|1,160,437|
| |Utah County|    37| 58.155|  0.898| 8,434| 13256.108| 190.855| 636,235|
| |San Juan County|    25| 1633.133| 27.997|   645| 42134.831| 363.955|  15,308|
| |Davis County|    19| 53.449|  2.411| 3,129|  8802.158| 108.505| 355,481|
| |Wasatch County|     4| 117.333| N/A|   545| 15986.624| N/A|  34,091|
| |Summit County|     1| 23.728| N/A|   706| 16751.691| N/A|  42,145|
| |Washington County|     0|  0.000| N/A|     0|     0.000| N/A| 177,556|
| |Tooele County|     0|  0.000| N/A|   573|  7929.808| N/A|  72,259|
| |Rich County|     0|  0.000| N/A|     0|     0.000| N/A|   2,483|
| |Grand County|     0|  0.000| N/A|     0|     0.000| N/A|   9,754|
| |Uintah County|     0|  0.000| N/A|     0|     0.000| N/A|  35,734|
| |Beaver County|     0|  0.000| N/A|     0|     0.000| N/A|   6,710|
| |Box Elder County|     0|  0.000| N/A|     0|     0.000| N/A|  56,046|
| |Sanpete County|     0|  0.000| N/A|     0|     0.000| N/A|  30,939|
| |Sevier County|     0|  0.000| N/A|     0|     0.000| N/A|  21,620|
| |Weber County|     0|  0.000| N/A|     0|     0.000| N/A| 260,213|
| |Cache County|     0|  0.000| N/A|     0|     0.000| N/A| 128,289|
| |Wayne County|     0|  0.000| N/A|     0|     0.000| N/A|   2,711|
| |Duchesne County|     0|  0.000| N/A|     0|     0.000| N/A|  19,938|
| |Iron County|     0|  0.000| N/A|     0|     0.000| N/A|  54,839|
| |Carbon County|     0|  0.000| N/A|     0|     0.000| N/A|  20,463|
| |Morgan County|     0|  0.000| N/A|     0|     0.000| N/A|  12,124|
| |Juab County|     0|  0.000| N/A|     0|     0.000| N/A|  12,017|
| |Garfield County|     0|  0.000| N/A|     0|     0.000| N/A|   5,051|
| |Emery County|     0|  0.000| N/A|     0|     0.000| N/A|  10,012|
| |Daggett County|     0|  0.000| N/A|     0|     0.000| N/A|     950|
| |Piute County|     0|  0.000| N/A|     0|     0.000| N/A|   1,479|
| |Millard County|     0|  0.000| N/A|     0|     0.000| N/A|  13,188|
| |Kane County|     0|  0.000| N/A|     0|     0.000| N/A|   7,886|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   223| 124.786| N/A|23,396| 13091.857| N/A|1,787,065|
| |Ada County|    72| 149.506|  5.043| 8,569| 17793.254| 263.415| 481,587|
| |Canyon County|    46| 200.131|  7.458| 5,453| 23724.271| 533.269| 229,849|
| |Twin Falls County|    32| 368.333|  3.289| 1,310| 15078.616| 228.564|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   140|  3464.660| 38.889|  40,408|
| |Kootenai County|    15| 90.527|  6.035| 1,729| 10434.709| 198.297| 165,697|
| |Jerome County|     6| 245.781| N/A|   458| 18761.265| N/A|  24,412|
| |Blaine County|     6| 260.632| N/A|   575| 24977.195| N/A|  23,021|
| |Bonneville County|     3| 25.197| N/A|   914|  7676.673| N/A| 119,062|
| |Elmore County|     3| 109.047| N/A|   205|  7451.565| N/A|  27,511|
| |Washington County|     3| 294.291| N/A|   200| 19619.384| N/A|  10,194|
| |Shoshone County|     2| 155.255| N/A|    82|  6365.471| N/A|  12,882|
| |Payette County|     2| 83.504| N/A|   367| 15322.951| N/A|  23,951|
| |Owyhee County|     2| 169.162| N/A|   255| 21568.130| N/A|  11,823|
| |Minidoka County|     2| 95.062| N/A|   464| 22054.280| N/A|  21,039|
| |Bannock County|     2| 22.777| N/A|   375|  4270.681| N/A|  87,808|
| |Bingham County|     2| 42.725| N/A|   229|  4892.013| N/A|  46,811|
| |Valley County|     1| 87.781| N/A|    56|  4915.730| N/A|  11,392|
| |Boise County|     1| 127.698| N/A|    43|  5490.997| N/A|   7,831|
| |Cassia County|     1| 41.615| N/A|   503| 20932.168| N/A|  24,030|
| |Gooding County|     1| 65.880| N/A|   152| 10013.835| N/A|  15,179|
| |Jefferson County|     1| 33.477| N/A|   174|  5825.048| N/A|  29,871|
| |Gem County|     1| 55.212| N/A|   171|  9441.254| N/A|  18,112|
| |Adams County|     0|  0.000| N/A|    19|  4424.779| N/A|   4,294|
| |Bear Lake County|     0|  0.000| N/A|    12|  1959.184| N/A|   6,125|
| |Power County|     0|  0.000| N/A|    55|  7160.526| N/A|   7,681|
| |Madison County|     0|  0.000| N/A|   150|  3758.739| N/A|  39,907|
| |Lincoln County|     0|  0.000| N/A|    56| 10436.079| N/A|   5,366|
| |Lewis County|     0|  0.000| N/A|     1|   260.552| N/A|   3,838|
| |Lemhi County|     0|  0.000| N/A|    14|  1744.114| N/A|   8,027|
| |Latah County|     0|  0.000| N/A|    95|  2368.605| N/A|  40,108|
| |Idaho County|     0|  0.000| N/A|    30|  1799.964| N/A|  16,667|
| |Fremont County|     0|  0.000| N/A|    72|  5496.603| N/A|  13,099|
| |Franklin County|     0|  0.000| N/A|    50|  3603.344| N/A|  13,876|
| |Custer County|     0|  0.000| N/A|     9|  2085.747| N/A|   4,315|
| |Clearwater County|     0|  0.000| N/A|    16|  1827.318| N/A|   8,756|
| |Clark County|     0|  0.000| N/A|     8|  9467.456| N/A|     845|
| |Caribou County|     0|  0.000| N/A|    31|  4332.635| N/A|   7,155|
| |Camas County|     0|  0.000| N/A|     1|   904.159| N/A|   1,106|
| |Butte County|     0|  0.000| N/A|     0|     0.000| N/A|   2,597|
| |Boundary County|     0|  0.000| N/A|    36|  2939.976| N/A|  12,245|
| |Bonner County|     0|  0.000| N/A|   174|  3804.193| N/A|  45,739|
| |Benewah County|     0|  0.000| N/A|    60|  6453.001| N/A|   9,298|
| |Oneida County|     0|  0.000| N/A|    13|  2869.124| N/A|   4,531|
| |Teton County|     0|  0.000| N/A|    70|  5765.113| N/A|  12,142|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   141| 159.383| N/A| 9,273| 10482.005| N/A| 884,659|
| |Minnehaha County|    65| 336.554|  1.479| 4,329| 22414.489| 144.977| 193,134|
| |Pennington County|    31| 272.468|  6.278|   863|  7585.146| 74.081| 113,775|
| |Beadle County|     9| 487.726| N/A|   587| 31810.546| N/A|  18,453|
| |Union County|     4| 251.067| N/A|   208| 13055.486| N/A|  15,932|
| |Todd County|     4| 393.043| N/A|    67|  6583.473| N/A|  10,177|
| |Brown County|     3| 77.242| N/A|   422| 10865.367| N/A|  38,839|
| |Buffalo County|     3| 1529.052| N/A|   109| 55555.556| N/A|   1,962|
| |Oglala Lakota County|     2| 141.074| N/A|   152| 10721.591| N/A|  14,177|
| |Hughes County|     2| 114.116| N/A|    88|  5021.111| N/A|  17,526|
| |Lake County|     2| 156.287| N/A|    89|  6954.755| N/A|  12,797|
| |Lincoln County|     2| 32.718| N/A|   602|  9848.187| N/A|  61,128|
| |Lyman County|     2| 528.961| N/A|    88| 23274.266| N/A|   3,781|
| |Yankton County|     2| 87.665| N/A|   104|  4558.604| N/A|  22,814|
| |Faulk County|     1| 434.972| N/A|    26| 11309.265| N/A|   2,299|
| |Jerauld County|     1| 496.771| N/A|    40| 19870.840| N/A|   2,013|
| |Davison County|     1| 50.569| N/A|    94|  4753.477| N/A|  19,775|
| |Meade County|     1| 35.296| N/A|    82|  2894.254| N/A|  28,332|
| |Jackson County|     1| 299.043| N/A|    11|  3289.474| N/A|   3,344|
| |Brookings County|     1| 28.509| N/A|   127|  3620.606| N/A|  35,077|
| |Codington County|     1| 35.703| N/A|   124|  4427.148| N/A|  28,009|
| |Butte County|     1| 95.886| N/A|    14|  1342.411| N/A|  10,429|
| |McCook County|     1| 179.019| N/A|    26|  4654.493| N/A|   5,586|
| |Roberts County|     1| 96.209| N/A|    73|  7023.283| N/A|  10,394|
| |McPherson County|     0|  0.000| N/A|     8|  3362.757| N/A|   2,379|
| |Lawrence County|     0|  0.000| N/A|    40|  1547.748| N/A|  25,844|
| |Charles Mix County|     0|  0.000| N/A|   100| 10761.946| N/A|   9,292|
| |Edmunds County|     0|  0.000| N/A|    13|  3395.142| N/A|   3,829|
| |Douglas County|     0|  0.000| N/A|    16|  5477.576| N/A|   2,921|
| |Dewey County|     0|  0.000| N/A|    65| 11031.908| N/A|   5,892|
| |Deuel County|     0|  0.000| N/A|     9|  2068.490| N/A|   4,351|
| |Day County|     0|  0.000| N/A|    21|  3871.681| N/A|   5,424|
| |Custer County|     0|  0.000| N/A|    26|  2897.905| N/A|   8,972|
| |Corson County|     0|  0.000| N/A|    30|  7342.144| N/A|   4,086|
| |Clay County|     0|  0.000| N/A|   123|  8742.004| N/A|  14,070|
| |Jones County|     0|  0.000| N/A|     2|  2214.839| N/A|     903|
| |Kingsbury County|     0|  0.000| N/A|    14|  2834.582| N/A|   4,939|
| |Gregory County|     0|  0.000| N/A|     7|  1672.640| N/A|   4,185|
| |Ziebach County|     0|  0.000| N/A|    10|  3628.447| N/A|   2,756|
| |Walworth County|     0|  0.000| N/A|    18|  3311.868| N/A|   5,435|
| |Turner County|     0|  0.000| N/A|    49|  5844.466| N/A|   8,384|
| |Tripp County|     0|  0.000| N/A|    20|  3675.795| N/A|   5,441|
| |Sully County|     0|  0.000| N/A|     1|   718.907| N/A|   1,391|
| |Stanley County|     0|  0.000| N/A|    14|  4519.045| N/A|   3,098|
| |Spink County|     0|  0.000| N/A|    22|  3450.439| N/A|   6,376|
| |Sanborn County|     0|  0.000| N/A|    13|  5546.075| N/A|   2,344|
| |Fall River County|     0|  0.000| N/A|    20|  2979.294| N/A|   6,713|
| |Haakon County|     0|  0.000| N/A|     2|  1053.186| N/A|   1,899|
| |Hamlin County|     0|  0.000| N/A|    16|  2595.717| N/A|   6,164|
| |Grant County|     0|  0.000| N/A|    24|  3403.290| N/A|   7,052|
| |Hyde County|     0|  0.000| N/A|     3|  2305.919| N/A|   1,301|
| |Hutchinson County|     0|  0.000| N/A|    27|  3703.196| N/A|   7,291|
| |Harding County|     0|  0.000| N/A|     0|     0.000| N/A|   1,298|
| |Hanson County|     0|  0.000| N/A|    21|  6081.668| N/A|   3,453|
| |Hand County|     0|  0.000| N/A|     7|  2193.670| N/A|   3,191|
| |Perkins County|     0|  0.000| N/A|     6|  2094.241| N/A|   2,865|
| |Potter County|     0|  0.000| N/A|     1|   464.468| N/A|   2,153|
| |Moody County|     0|  0.000| N/A|    32|  4866.180| N/A|   6,576|
| |Miner County|     0|  0.000| N/A|    15|  6768.953| N/A|   2,216|
| |Bon Homme County|     0|  0.000| N/A|    13|  1883.785| N/A|   6,901|
| |Bennett County|     0|  0.000| N/A|     6|  1783.061| N/A|   3,365|
| |Aurora County|     0|  0.000| N/A|    38| 13813.159| N/A|   2,751|
| |Mellette County|     0|  0.000| N/A|    24| 11644.833| N/A|   2,061|
| |Marshall County|     0|  0.000| N/A|     8|  1621.074| N/A|   4,935|
| |Clark County|     0|  0.000| N/A|    16|  4282.655| N/A|   3,736|
| |Campbell County|     0|  0.000| N/A|     3|  2180.233| N/A|   1,376|
| |Brule County|     0|  0.000| N/A|    45|  8495.375| N/A|   5,297|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   124| 92.247| N/A| 3,997|  2973.489| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.484| 2,070|  7016.878| 18.402| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   666|  3207.459| 17.200| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   169|  1381.825|  8.176| 122,302|
| |Androscoggin County|     7| 64.649| N/A|   548|  5061.093| N/A| 108,277|
| |Penobscot County|     5| 32.863| N/A|   152|   999.027| N/A| 152,148|
| |Somerset County|     1| 19.808| N/A|    33|   653.672| N/A|  50,484|
| |Lincoln County|     1| 28.873| N/A|    34|   981.694| N/A|  34,634|
| |Knox County|     1| 25.143| N/A|    27|   678.870| N/A|  39,772|
| |Hancock County|     1| 18.186| N/A|    35|   636.514| N/A|  54,987|
| |Franklin County|     1| 33.114| N/A|    45|  1490.116| N/A|  30,199|
| |Aroostook County|     1| 14.913| N/A|    33|   492.133| N/A|  67,055|
| |Washington County|     0|  0.000| N/A|    12|   382.421| N/A|  31,379|
| |Sagadahoc County|     0|  0.000| N/A|    54|  1506.024| N/A|  35,856|
| |Piscataquis County|     0|  0.000| N/A|     3|   178.731| N/A|  16,785|
| |Oxford County|     0|  0.000| N/A|    54|   931.436| N/A|  57,975|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   124| 69.191| N/A| 7,278|  4061.051| N/A|1,792,147|
| |Kanawha County|    22| 123.509|  1.604|   876|  4917.922| 103.459| 178,124|
| |Jackson County|    19| 664.894|  0.000|   160|  5599.104| 14.998|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   675|  5664.130| 49.149| 119,171|
| |Wayne County|     9| 228.415| N/A|   196|  4974.367| N/A|  39,402|
| |Fayette County|     5| 117.908| N/A|   137|  3230.675| N/A|  42,406|
| |Monongalia County|     5| 47.343| N/A|   929|  8796.349| N/A| 105,612|
| |Wood County|     5| 59.867| N/A|   242|  2897.579| N/A|  83,518|
| |Mineral County|     4| 148.876| N/A|   116|  4317.404| N/A|  26,868|
| |Preston County|     4| 119.646| N/A|   123|  3679.110| N/A|  33,432|
| |Jefferson County|     4| 69.996| N/A|   294|  5144.717| N/A|  57,146|
| |Ohio County|     4| 96.593| N/A|   265|  6399.266| N/A|  41,411|
| |Greenbrier County|     3| 86.550| N/A|    88|  2538.803| N/A|  34,662|
| |Logan County|     3| 93.694| N/A|   176|  5496.736| N/A|  32,019|
| |Mingo County|     3| 128.074| N/A|   156|  6659.836| N/A|  23,424|
| |Mercer County|     3| 51.057| N/A|   174|  2961.299| N/A|  58,758|
| |Cabell County|     2| 21.752| N/A|   367|  3991.517| N/A|  91,945|
| |Lewis County|     2| 125.731| N/A|    28|  1760.231| N/A|  15,907|
| |Marion County|     2| 35.668| N/A|   179|  3192.324| N/A|  56,072|
| |Pendleton County|     1| 143.493| N/A|    58|  8322.571| N/A|   6,969|
| |Roane County|     1| 73.057| N/A|    14|  1022.794| N/A|  13,688|
| |Mason County|     1| 37.713| N/A|    53|  1998.793| N/A|  26,516|
| |Marshall County|     1| 32.754| N/A|   128|  4192.460| N/A|  30,531|
| |Harrison County|     1| 14.869| N/A|   207|  3077.792| N/A|  67,256|
| |Clay County|     1| 117.536| N/A|    18|  2115.656| N/A|   8,508|
| |Grant County|     1| 86.445| N/A|    97|  8385.201| N/A|  11,568|
| |Brooke County|     1| 45.581| N/A|    61|  2780.437| N/A|  21,939|
| |Nicholas County|     1| 40.823| N/A|    35|  1428.805| N/A|  24,496|
| |Raleigh County|     1| 13.631| N/A|   210|  2862.556| N/A|  73,361|
| |Barbour County|     1| 60.824| N/A|    29|  1763.883| N/A|  16,441|
| |Hampshire County|     1| 43.150| N/A|    76|  3279.396| N/A|  23,175|
| |Taylor County|     1| 59.898| N/A|    56|  3354.298| N/A|  16,695|
| |Wyoming County|     1| 49.034| N/A|    29|  1421.987| N/A|  20,394|
| |Wetzel County|     0|  0.000| N/A|    41|  2721.540| N/A|  15,065|
| |Ritchie County|     0|  0.000| N/A|     3|   314.005| N/A|   9,554|
| |Randolph County|     0|  0.000| N/A|   206|  7178.951| N/A|  28,695|
| |Summers County|     0|  0.000| N/A|     7|   556.749| N/A|  12,573|
| |Webster County|     0|  0.000| N/A|     4|   492.975| N/A|   8,114|
| |Upshur County|     0|  0.000| N/A|    39|  1613.170| N/A|  24,176|
| |Tyler County|     0|  0.000| N/A|    13|  1513.212| N/A|   8,591|
| |Tucker County|     0|  0.000| N/A|    11|  1608.422| N/A|   6,839|
| |Wirt County|     0|  0.000| N/A|     6|  1030.751| N/A|   5,821|
| |Putnam County|     0|  0.000| N/A|   178|  3153.233| N/A|  56,450|
| |Pocahontas County|     0|  0.000| N/A|    41|  4971.505| N/A|   8,247|
| |Boone County|     0|  0.000| N/A|    95|  4427.460| N/A|  21,457|
| |Braxton County|     0|  0.000| N/A|     8|   573.189| N/A|  13,957|
| |McDowell County|     0|  0.000| N/A|    49|  2780.300| N/A|  17,624|
| |Pleasants County|     0|  0.000| N/A|    10|  1340.483| N/A|   7,460|
| |Lincoln County|     0|  0.000| N/A|    79|  3870.841| N/A|  20,409|
| |Calhoun County|     0|  0.000| N/A|     6|   844.001| N/A|   7,109|
| |Hardy County|     0|  0.000| N/A|    57|  4137.631| N/A|  13,776|
| |Hancock County|     0|  0.000| N/A|   107|  3713.988| N/A|  28,810|
| |Doddridge County|     0|  0.000| N/A|     5|   591.856| N/A|   8,448|
| |Gilmer County|     0|  0.000| N/A|    16|  2045.251| N/A|   7,823|
| |Morgan County|     0|  0.000| N/A|    26|  1453.813| N/A|  17,884|
| |Monroe County|     0|  0.000| N/A|    19|  1431.262| N/A|  13,275|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   109| 143.033| N/A| 7,159|  9394.249| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 2,977| 16364.066| 82.452| 181,923|
| |Grand Forks County|     6| 86.392| N/A|   657|  9459.907| N/A|  69,451|
| |Burleigh County|     5| 52.287| N/A| 1,082| 11314.914| N/A|  95,626|
| |Stark County|     3| 95.271| N/A|   229|  7272.381| N/A|  31,489|
| |Morton County|     3| 95.651| N/A|   314| 10011.478| N/A|  31,364|
| |Stutsman County|     2| 96.600| N/A|   125|  6037.481| N/A|  20,704|
| |Williams County|     2| 53.207| N/A|   250|  6650.882| N/A|  37,589|
| |McIntosh County|     2| 800.961| N/A|    27| 10812.976| N/A|   2,497|
| |Ramsey County|     2| 173.626| N/A|    65|  5642.851| N/A|  11,519|
| |McHenry County|     1| 174.064| N/A|    16|  2785.030| N/A|   5,745|
| |Ward County|     1| 14.784| N/A|   204|  3015.922| N/A|  67,641|
| |Emmons County|     1| 308.547| N/A|    17|  5245.295| N/A|   3,241|
| |Griggs County|     1| 448.229| N/A|    31| 13895.114| N/A|   2,231|
| |Sioux County|     1| 236.407| N/A|    60| 14184.397| N/A|   4,230|
| |Benson County|     1| 146.370| N/A|   131| 19174.473| N/A|   6,832|
| |Mountrail County|     1| 94.832| N/A|   123| 11664.296| N/A|  10,545|
| |McKenzie County|     1| 66.560| N/A|    85|  5657.614| N/A|  15,024|
| |Foster County|     0|  0.000| N/A|    23|  7165.109| N/A|   3,210|
| |Eddy County|     0|  0.000| N/A|    17|  7433.319| N/A|   2,287|
| |Grant County|     0|  0.000| N/A|     4|  1759.015| N/A|   2,274|
| |Wells County|     0|  0.000| N/A|    21|  5477.308| N/A|   3,834|
| |Logan County|     0|  0.000| N/A|     7|  3783.784| N/A|   1,850|
| |McLean County|     0|  0.000| N/A|    46|  4867.725| N/A|   9,450|
| |LaMoure County|     0|  0.000| N/A|    16|  3954.523| N/A|   4,046|
| |Kidder County|     0|  0.000| N/A|    13|  5241.935| N/A|   2,480|
| |Hettinger County|     0|  0.000| N/A|     6|  2400.960| N/A|   2,499|
| |Towner County|     0|  0.000| N/A|     5|  2284.148| N/A|   2,189|
| |Traill County|     0|  0.000| N/A|    50|  6222.001| N/A|   8,036|
| |Walsh County|     0|  0.000| N/A|   103|  9679.541| N/A|  10,641|
| |Dunn County|     0|  0.000| N/A|    30|  6781.193| N/A|   4,424|
| |Nelson County|     0|  0.000| N/A|    22|  7641.542| N/A|   2,879|
| |Divide County|     0|  0.000| N/A|     1|   441.696| N/A|   2,264|
| |Dickey County|     0|  0.000| N/A|    12|  2463.054| N/A|   4,872|
| |Cavalier County|     0|  0.000| N/A|    31|  8240.298| N/A|   3,762|
| |Burke County|     0|  0.000| N/A|    23| 10874.704| N/A|   2,115|
| |Bowman County|     0|  0.000| N/A|     6|  1984.127| N/A|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000| N/A|     2|  2155.172| N/A|     928|
| |Barnes County|     0|  0.000| N/A|    37|  3552.568| N/A|  10,415|
| |Adams County|     0|  0.000| N/A|     2|   902.527| N/A|   2,216|
| |Mercer County|     0|  0.000| N/A|    24|  2931.477| N/A|   8,187|
| |Oliver County|     0|  0.000| N/A|     7|  3573.252| N/A|   1,959|
| |Golden Valley County|     0|  0.000| N/A|     4|  2271.437| N/A|   1,761|
| |Pierce County|     0|  0.000| N/A|    11|  2767.296| N/A|   3,975|
| |Steele County|     0|  0.000| N/A|    13|  6878.307| N/A|   1,890|
| |Slope County|     0|  0.000| N/A|     3|  4000.000| N/A|     750|
| |Sheridan County|     0|  0.000| N/A|     6|  4562.738| N/A|   1,315|
| |Sargent County|     0|  0.000| N/A|    10|  2565.418| N/A|   3,898|
| |Rolette County|     0|  0.000| N/A|    48|  3386.005| N/A|  14,176|
| |Richland County|     0|  0.000| N/A|   101|  6243.432| N/A|  16,177|
| |Renville County|     0|  0.000| N/A|     8|  3437.903| N/A|   2,327|
| |Ransom County|     0|  0.000| N/A|    26|  4982.752| N/A|   5,218|
| |Pembina County|     0|  0.000| N/A|    28|  4117.042| N/A|   6,801|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    65| 60.817| N/A| 4,602|  4305.852| N/A|1,068,778|
| |Yellowstone County|    28| 173.590|  2.657| 1,191|  7383.757| 184.218| 161,300|
| |Big Horn County|    11| 825.888| 53.629|   394| 29581.800| 997.501|  13,319|
| |Toole County|     6| 1266.892| N/A|    40|  8445.946| N/A|   4,736|
| |Gallatin County|     3| 26.216| N/A|   908|  7934.705| N/A| 114,434|
| |Richland County|     2| 185.134| N/A|    47|  4350.643| N/A|  10,803|
| |Lincoln County|     2| 100.100| N/A|    73|  3653.654| N/A|  19,980|
| |Cascade County|     2| 24.580| N/A|   161|  1978.713| N/A|  81,366|
| |Custer County|     2| 175.408| N/A|    58|  5086.827| N/A|  11,402|
| |Flathead County|     2| 19.267| N/A|   301|  2899.640| N/A| 103,806|
| |Sweet Grass County|     1| 267.594| N/A|     5|  1337.972| N/A|   3,737|
| |Rosebud County|     1| 111.894| N/A|    32|  3580.620| N/A|   8,937|
| |Ravalli County|     1| 22.828| N/A|    74|  1689.266| N/A|  43,806|
| |Madison County|     1| 116.279| N/A|    79|  9186.047| N/A|   8,600|
| |Lewis and Clark County|     1| 14.403| N/A|   151|  2174.790| N/A|  69,432|
| |Lake County|     1| 32.832| N/A|   176|  5778.449| N/A|  30,458|
| |Glacier County|     1| 72.711| N/A|    63|  4580.819| N/A|  13,753|
| |Powder River County|     0|  0.000| N/A|     1|   594.530| N/A|   1,682|
| |Petroleum County|     0|  0.000| N/A|     0|     0.000| N/A|     487|
| |Phillips County|     0|  0.000| N/A|     5|  1264.542| N/A|   3,954|
| |Pondera County|     0|  0.000| N/A|    10|  1691.761| N/A|   5,911|
| |Prairie County|     0|  0.000| N/A|     1|   928.505| N/A|   1,077|
| |Powell County|     0|  0.000| N/A|     2|   290.276| N/A|   6,890|
| |Roosevelt County|     0|  0.000| N/A|    21|  1908.397| N/A|  11,004|
| |Sanders County|     0|  0.000| N/A|     9|   743.003| N/A|  12,113|
| |Sheridan County|     0|  0.000| N/A|     4|  1208.824| N/A|   3,309|
| |Silver Bow County|     0|  0.000| N/A|    75|  2148.074| N/A|  34,915|
| |Wibaux County|     0|  0.000| N/A|     3|  3095.975| N/A|     969|
| |Wheatland County|     0|  0.000| N/A|     3|  1411.101| N/A|   2,126|
| |Valley County|     0|  0.000| N/A|    14|  1892.915| N/A|   7,396|
| |Treasure County|     0|  0.000| N/A|     2|  2873.563| N/A|     696|
| |Teton County|     0|  0.000| N/A|    15|  2440.215| N/A|   6,147|
| |Stillwater County|     0|  0.000| N/A|    22|  2281.684| N/A|   9,642|
| |Broadwater County|     0|  0.000| N/A|    11|  1763.668| N/A|   6,237|
| |Blaine County|     0|  0.000| N/A|    10|  1496.782| N/A|   6,681|
| |Beaverhead County|     0|  0.000| N/A|    58|  6135.618| N/A|   9,453|
| |Golden Valley County|     0|  0.000| N/A|     3|  3654.080| N/A|     821|
| |Garfield County|     0|  0.000| N/A|    12|  9538.951| N/A|   1,258|
| |Fergus County|     0|  0.000| N/A|     9|   814.480| N/A|  11,050|
| |Fallon County|     0|  0.000| N/A|     2|   702.741| N/A|   2,846|
| |Deer Lodge County|     0|  0.000| N/A|    23|  2516.411| N/A|   9,140|
| |Dawson County|     0|  0.000| N/A|    16|  1857.657| N/A|   8,613|
| |Granite County|     0|  0.000| N/A|    13|  3847.292| N/A|   3,379|
| |Hill County|     0|  0.000| N/A|    41|  2487.260| N/A|  16,484|
| |Jefferson County|     0|  0.000| N/A|    27|  2209.312| N/A|  12,221|
| |Judith Basin County|     0|  0.000| N/A|     3|  1494.768| N/A|   2,007|
| |Carbon County|     0|  0.000| N/A|    60|  5594.406| N/A|  10,725|
| |Carter County|     0|  0.000| N/A|     0|     0.000| N/A|   1,252|
| |Chouteau County|     0|  0.000| N/A|     7|  1242.236| N/A|   5,635|
| |Daniels County|     0|  0.000| N/A|     3|  1775.148| N/A|   1,690|
| |Park County|     0|  0.000| N/A|    55|  3312.056| N/A|  16,606|
| |Musselshell County|     0|  0.000| N/A|     3|   647.529| N/A|   4,633|
| |Missoula County|     0|  0.000| N/A|   298|  2491.639| N/A| 119,600|
| |Mineral County|     0|  0.000| N/A|     0|     0.000| N/A|   4,397|
| |Meagher County|     0|  0.000| N/A|     4|  2148.228| N/A|   1,862|
| |McCone County|     0|  0.000| N/A|     3|  1802.885| N/A|   1,664|
| |Liberty County|     0|  0.000| N/A|     1|   427.899| N/A|   2,337|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,437|  2302.925| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   723|  4414.620|  6.978| 163,774|
| |Franklin County|     7| 141.695| N/A|   118|  2388.567| N/A|  49,402|
| |Windham County|     3| 71.053| N/A|   102|  2415.802| N/A|  42,222|
| |Addison County|     2| 54.382| N/A|    73|  1984.936| N/A|  36,777|
| |Windsor County|     2| 36.323| N/A|    72|  1307.617| N/A|  55,062|
| |Washington County|     2| 34.241| N/A|    53|   907.394| N/A|  58,409|
| |Lamoille County|     1| 39.429| N/A|    43|  1695.450| N/A|  25,362|
| |Rutland County|     1| 17.185| N/A|    97|  1666.924| N/A|  58,191|
| |Bennington County|     1| 28.193| N/A|    85|  2396.391| N/A|  35,470|
| |Grand Isle County|     0|  0.000| N/A|    13|  1796.821| N/A|   7,235|
| |Orange County|     0|  0.000| N/A|    14|   484.563| N/A|  28,892|
| |Essex County|     0|  0.000| N/A|     4|   649.035| N/A|   6,163|
| |Orleans County|     0|  0.000| N/A|    14|   517.809| N/A|  27,037|
| |Caledonia County|     0|  0.000| N/A|    26|   866.869| N/A|  29,993|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    28| 19.776| N/A| 2,891|  2041.851| N/A|1,415,872|
| |Honolulu County|    22| 22.574| N/A| 2,541|  2607.322| N/A| 974,563|
| |Maui County|     6| 35.839| N/A|   180|  1075.160| N/A| 167,417|
| |Kalawao County|     0|  0.000| N/A|     0|     0.000| N/A|      86|
| |Kauai County|     0|  0.000| N/A|    47|   650.132| N/A|  72,293|
| |Hawaii County|     0|  0.000| N/A|   123|   610.382| N/A| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 2,953|  5102.296| N/A| 578,759|
| |Johnson County|     1| 118.413| N/A|    23|  2723.505| N/A|   8,445|
| |Platte County|     0|  0.000| N/A|     5|   595.735| N/A|   8,393|
| |Campbell County|     0|  0.000| N/A|   118|  2546.341| N/A|  46,341|
| |Washakie County|     0|  0.000| N/A|    59|  7559.257| N/A|   7,805|
| |Converse County|     0|  0.000| N/A|    32|  2315.150| N/A|  13,822|
| |Lincoln County|     0|  0.000| N/A|   101|  5093.293| N/A|  19,830|
| |Laramie County|     0|  0.000| N/A|   492|  4944.724| N/A|  99,500|
| |Park County|     0|  0.000| N/A|   128|  4384.463| N/A|  29,194|
| |Niobrara County|     0|  0.000| N/A|     2|   848.896| N/A|   2,356|
| |Natrona County|     0|  0.000| N/A|   228|  2855.068| N/A|  79,858|
| |Crook County|     0|  0.000| N/A|    10|  1318.565| N/A|   7,584|
| |Fremont County|     0|  0.000| N/A|   498| 12684.343| N/A|  39,261|
| |Goshen County|     0|  0.000| N/A|    23|  1740.973| N/A|  13,211|
| |Hot Springs County|     0|  0.000| N/A|    19|  4305.461| N/A|   4,413|
| |Carbon County|     0|  0.000| N/A|    88|  5945.946| N/A|  14,800|
| |Albany County|     0|  0.000| N/A|    88|  2263.374| N/A|  38,880|
| |Big Horn County|     0|  0.000| N/A|    36|  3053.435| N/A|  11,790|
| |Sublette County|     0|  0.000| N/A|    38|  3865.324| N/A|   9,831|
| |Sheridan County|     0|  0.000| N/A|    68|  2230.605| N/A|  30,485|
| |Sweetwater County|     0|  0.000| N/A|   253|  5975.014| N/A|  42,343|
| |Teton County|     0|  0.000| N/A|   367| 15640.982| N/A|  23,464|
| |Uinta County|     0|  0.000| N/A|   272| 13448.037| N/A|  20,226|
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
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Kodiak Island Borough|     0|  0.000| N/A|     0|     0.000| N/A|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000| N/A|     0|     0.000| N/A|  13,901|
| |Kenai Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|  58,708|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Hoonah-Angoon Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   2,148|
| |Fairbanks North Star Borough|     0|  0.000| N/A|     0|     0.000| N/A|  96,849|
| |Dillingham Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   4,916|
| |Denali Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,097|
| |Bristol Bay Borough|     0|  0.000| N/A|     0|     0.000| N/A|     836|
| |Bethel Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  18,386|
| |Aleutians West Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,634|
| |Aleutians East Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,337|
| |Nome Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  10,004|
| |North Slope Borough|     0|  0.000| N/A|     0|     0.000| N/A|   9,832|
| |Northwest Arctic Borough|     0|  0.000| N/A|     0|     0.000| N/A|   7,621|
| |Petersburg Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,266|
| |Kusilvak Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   8,314|
| |Lake and Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|   1,592|
| |Matanuska-Susitna Borough|     0|  0.000| N/A|     0|     0.000| N/A| 108,317|
| |Haines Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|17,860| 16859.220| N/A|1,059,361|
| |Washington County|     0|  0.000| N/A|   607|  4833.688| N/A| 125,577|
| |Providence County|     0|  0.000| N/A|15,047| 23550.274| N/A| 638,931|
| |Newport County|     0|  0.000| N/A|   396|  4824.444| N/A|  82,082|
| |Kent County|     0|  0.000| N/A| 1,494|  9093.565| N/A| 164,292|
| |Bristol County|     0|  0.000| N/A|   316|  6518.286| N/A|  48,479|


