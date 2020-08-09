# Analysis of US By County #

Updated: at 2020-08-09

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 129,488 deaths (448.581 deaths/million) and 4,300,684 confirmed cases (14898.680 confirmed cases/million).  This group accounts for 81.01% of all US deaths and for 87.52% of all US cases.

24.72% of this group's deaths (20.03% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.07% of this group's deaths (20.31% of the total US deaths) occured in 33 counties in 14 states with a combined population of 38,392,743 (11.70% of the total US population):



The next 25.10% of this group's deaths (20.34% of the total US deaths) occured in 88 counties in 30 states with a combined population of 68,077,345 (20.74% of the total US population)

The remaining 25.11% of this group's deaths (20.34% of the total US deaths) occured in 856 counties in 50 states with a combined population of 144,904,753 (44.15% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,897 deaths (250.067 deaths/million) and 444,779 confirmed cases (11238.188 confirmed cases/million).  This group accounts for 6.19% of all US deaths and for 9.05% of all US cases.

24.96% of this group's deaths (1.55% of the total US deaths) occured in 58 counties in 16 states with a combined population of 1,923,978 (0.59% of the total US population):



The next 24.95% of this group's deaths (1.54% of the total US deaths) occured in 111 counties in 27 states with a combined population of 3,317,497 (1.01% of the total US population):



The next 25.06% of this group's deaths (1.55% of the total US deaths) occured in 232 counties in 33 states with a combined population of 5,751,187 (1.75% of the total US population)

The remaining 25.04% of this group's deaths (1.55% of the total US deaths) occured in 1,751 counties in 47 states with a combined population of 28,584,802 (8.71% of the total US population) 

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
|NJ|21 counties|15,869| 1786.609| N/A|183,787| 20691.631| N/A|8,882,190|
| |Essex County| 2,111| 2642.135|  1.609|19,715| 24675.365| 37.548| 798,975|
| |Bergen County| 2,038| 2186.221|  0.000|20,751| 22260.197| 39.384| 932,202|
| |Hudson County| 1,504| 2236.794|  0.637|19,641| 29210.682| 30.594| 672,391|
| |Middlesex County| 1,403| 1700.478|  0.000|17,884| 21675.947| 31.859| 825,062|
| |Union County| 1,350| 2426.569|  0.770|16,663| 29951.055| 30.300| 556,341|
| |Passaic County| 1,239| 2468.983|  0.000|17,623| 35117.750| 44.979| 501,826|
| |Ocean County| 1,018| 1676.587|  0.706|10,585| 17432.879| 34.351| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,284| 16619.397| 44.095| 618,795|
| |Morris County|   828| 1683.457|  0.000| 7,235| 14709.919| 26.431| 491,845|
| |Mercer County|   619| 1684.675|  1.555| 8,115| 22085.839| 34.214| 367,430|
| |Camden County|   578| 1141.230|  1.410| 8,525| 16832.158| 53.874| 506,471|
| |Somerset County|   561| 1705.509|  2.606| 5,231| 15902.886| 19.544| 328,934|
| |Burlington County|   472| 1059.843|  0.642| 5,977| 13420.935| 52.928| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,456| 13107.293| 40.635| 263,670|
| |Gloucester County|   212| 726.934|  1.470| 3,236| 11096.024| 76.416| 291,636|
| |Sussex County|   198| 1409.373|  3.051| 1,327|  9445.647| 27.455| 140,488|
| |Warren County|   172| 1633.940|  2.714| 1,343| 12758.034| 18.999| 105,267|
| |Cumberland County|   158| 1056.665|  0.955| 3,332| 22283.601| 99.361| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,148|  9230.448| 13.784| 124,371|
| |Cape May County|    87| 945.251|  0.000|   824|  8952.727| 23.282|  92,039|
| |Salem County|    87| 1394.566|  9.160|   892| 14298.309| 52.668|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,317| 633.172| N/A|252,035| 12955.712| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,628| 32152.132| 37.585|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.193|43,749| 29628.180| 43.440|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.295|36,180| 37395.117| 30.417| 967,506|
| |Queens County|   984| 436.542|  0.778| 7,860|  3487.327| 17.852|2,253,858|
| |Kings County|   930| 363.236|  0.648| 1,349|   526.950|  2.698|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,936| 42776.153| 24.556| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,850|  9633.156| 46.961| 918,702|
| |Bronx County|   649| 457.382|  0.816|26,767| 18873.973| 96.618|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,156| 28981.140| 25.236| 384,940|
| |New York County|   414| 254.246|  0.453|15,438|  9478.511| 48.522|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 4,922|  6635.480| 34.666| 741,770|
| |Onondaga County|   200| 434.284|  1.861| 3,565|  7741.115| 27.298| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,600| 15634.665| 46.613| 294,218|
| |Richmond County|   148| 310.725|  0.554| 7,860| 16507.521| 84.504| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,581|  8448.279| 30.862| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,142|  9367.169| 38.108| 228,671|
| |Niagara County|    98| 468.270|  1.365| 1,494|  7138.727| 34.130| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,057| 11583.968| 24.939| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,120|  5879.635| 53.997| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,447| 14717.250| 31.966|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   298|  7385.012| 10.621|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,488| 19726.376|  9.469|  75,432|
| |Steuben County|    42| 440.349|  0.000|   298|  3124.377| 11.982|  95,379|
| |Columbia County|    37| 622.257|  0.000|   539|  9064.765| 48.051|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,058|  6812.665| 23.917| 155,299|
| |Ontario County|    34| 309.719|  0.000|   357|  3252.047| 10.411| 109,777|
| |Warren County|    33| 516.077|  0.000|   308|  4816.715| 17.873|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   761|  4794.788| 24.302| 158,714|
| |Tioga County|    25| 518.640|  2.964|   193|  4003.900| 14.818|  48,203|
| |Fulton County|    24| 449.581|  0.000|   295|  5526.104| 34.789|  53,383|
| |Greene County|    18| 381.453|  0.000|   291|  6166.822|  6.055|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   755|  3284.565| 18.023| 229,863|
| |Madison County|    17| 239.636|  0.000|   412|  5807.643| 26.179|  70,941|
| |Washington County|    14| 228.743|  0.000|   257|  4199.072|  4.668|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   253|  1993.649| 24.766| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470| 22.707|  62,914|
| |Yates County|     7| 280.978|  0.000|    56|  2247.822|  5.734|  24,913|
| |Chenango County|     6| 127.100|  0.000|   215|  4554.409| 18.157|  47,207|
| |Cattaraugus County|     6| 78.826|  0.000|   165|  2167.715| 13.138|  76,117|
| |Genesee County|     5| 87.291|  0.000|   277|  4835.894| 12.470|  57,280|
| |Otsego County|     5| 84.044|  0.000|   116|  1949.809|  9.605|  59,493|
| |Wyoming County|     5| 125.442|  0.000|   116|  2910.259| 14.336|  39,859|
| |Clinton County|     4| 49.699|  0.000|   127|  1577.934|  0.000|  80,485|
| |Herkimer County|     4| 65.233|  0.000|   273|  4452.127| 76.881|  61,319|
| |Montgomery County|     4| 81.266|  0.000|   172|  3494.443| 49.340|  49,221|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  2.652| 107,740|
| |Delaware County|     4| 90.631|  0.000|   105|  2379.064|  6.474|  44,135|
| |Seneca County|     3| 88.194|  0.000|    89|  2616.416| 16.799|  34,016|
| |Chemung County|     3| 35.947|  0.000|   171|  2048.984| 13.694|  83,456|
| |Wayne County|     3| 33.364|  0.000|   249|  2769.190|  6.355|  89,918|
| |Oswego County|     3| 25.614|  0.000|   253|  2160.104| 10.977| 117,124|
| |Cayuga County|     2| 26.118|  0.000|   151|  1971.897| 13.059|  76,576|
| |Allegany County|     1| 21.696|  0.000|    79|  1714.001| 15.497|  46,091|
| |Jefferson County|     0|  0.000|  0.000|   140|  1274.651| 13.007| 109,834|
| |Lewis County|     0|  0.000|  0.000|    41|  1559.172| 38.029|  26,296|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Cortland County|     0|  0.000|  0.000|    95|  1996.595| 12.010|  47,581|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  5.592| 102,180|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525| 11.424|  50,022|
| |Essex County|     0|  0.000|  0.000|    55|  1491.121|  0.000|  36,885|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,307| 260.856| N/A|554,388| 14030.798| N/A|39,512,223|
| |Los Angeles County| 4,967| 494.765|  4.241|206,778| 20597.250| 226.557|10,039,107|
| |Riverside County|   799| 323.410|  6.014|40,452| 16373.708| 198.973|2,470,546|
| |Orange County|   720| 226.722|  3.194|39,076| 12304.720| 100.900|3,175,692|
| |San Diego County|   586| 175.537|  1.070|31,779|  9519.430| 116.868|3,338,330|
| |San Bernardino County|   502| 230.266|  5.570|35,452| 16261.751| 180.596|2,180,085|
| |Imperial County|   244| 1346.467| 18.920| 9,693| 53488.950| 223.886| 181,215|
| |San Joaquin County|   211| 276.849|  8.060|12,303| 16142.534| 153.701| 762,148|
| |Alameda County|   208| 124.452|  1.624|13,213|  7905.685| 147.787|1,671,329|
| |Santa Clara County|   203| 105.299|  0.889|11,475|  5952.220| 85.513|1,927,852|
| |Tulare County|   196| 420.425|  5.516|10,475| 22469.138| 312.867| 466,195|
| |Kern County|   171| 189.957|  4.285|22,626| 25134.359| 435.458| 900,202|
| |Fresno County|   171| 171.154|  4.719|17,031| 17046.325| 370.619| 999,101|
| |Stanislaus County|   161| 292.376| 14.787| 9,566| 17371.881| 175.374| 550,660|
| |Sacramento County|   161| 103.733|  2.577|10,795|  6955.281| 89.743|1,552,058|
| |Contra Costa County|   138| 119.633|  2.105| 9,022|  7821.237| 150.594|1,153,526|
| |San Mateo County|   120| 156.541|  0.186| 6,110|  7970.539| 105.479| 766,573|
| |Ventura County|    89| 105.200|  2.195| 8,146|  9628.773| 135.426| 846,006|
| |Marin County|    79| 305.224|  4.967| 5,287| 20426.850| 161.719| 258,826|
| |Santa Barbara County|    69| 154.536|  2.880| 6,704| 15014.591| 171.813| 446,499|
| |San Francisco County|    67| 76.003| N/A| 7,432|  8430.615| N/A| 881,549|
| |Merced County|    64| 230.481|  7.203| 5,012| 18049.553| 374.017| 277,680|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993| 68.187| 152,940|
| |Sonoma County|    47| 95.077|  2.890| 3,431|  6940.623| 140.737| 494,336|
| |Yolo County|    43| 195.011|  1.296| 1,690|  7664.399| 116.618| 220,500|
| |Solano County|    40| 89.357|  0.957| 4,029|  9000.476| 133.397| 447,643|
| |Madera County|    39| 247.891|  8.172| 2,302| 14631.945| 325.982| 157,327|
| |Monterey County|    35| 80.634|  1.646| 5,212| 12007.529| 136.584| 434,061|
| |Placer County|    20| 50.210|  1.793| 2,186|  5487.926| 98.268| 398,329|
| |San Luis Obispo County|    15| 52.983|  0.000| 2,093|  7392.860| 156.425| 283,111|
| |Mendocino County|    10| 115.275|  1.647|   380|  4380.454| 111.982|  86,749|
| |Shasta County|    10| 55.531|  0.793|   418|  2321.191| 38.872| 180,080|
| |Napa County|    10| 72.598|  2.074| 1,046|  7593.797| 163.865| 137,744|
| |Butte County|     8| 36.499|  0.652| 1,095|  4995.757| 100.371| 219,186|
| |Sutter County|     7| 72.187|  1.473|   921|  9497.685| 225.399|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,238|  4531.263| 44.968| 273,213|
| |San Benito County|     4| 63.686|  0.000|   709| 11288.371| 197.882|  62,808|
| |Yuba County|     4| 50.847|  0.000|   588|  7474.450| 212.466|  78,668|
| |Humboldt County|     4| 29.508|  0.000|   282|  2080.290| 51.638| 135,558|
| |Colusa County|     4| 185.641|  0.000|   362| 16800.483| 258.571|  21,547|
| |Glenn County|     3| 105.660| 10.063|   360| 12679.181| 176.100|  28,393|
| |Inyo County|     3| 166.306| 15.839|    64|  3547.869| 102.952|  18,039|
| |Mariposa County|     2| 116.259|  0.000|    60|  3487.764| 49.825|  17,203|
| |Lake County|     2| 31.063|  2.219|   220|  3416.892| 55.469|  64,386|
| |Amador County|     2| 50.312|  7.187|   164|  4125.579| 140.155|  39,752|
| |Tuolumne County|     2| 36.712|  0.000|   152|  2790.117| 28.845|  54,478|
| |Calaveras County|     1| 21.784|  0.000|   147|  3202.266| 68.464|  45,905|
| |Tehama County|     1| 15.365|  0.000|   276|  4240.674| 92.189|  65,084|
| |Nevada County|     1| 10.025|  0.000|   322|  3227.908| 32.938|  99,755|
| |Mono County|     1| 69.233|  0.000|   153| 10592.634| 108.795|  14,444|
| |El Dorado County|     1|  5.186|  0.000|   729|  3780.277| 68.153| 192,843|
| |Trinity County|     0|  0.000|  0.000|     5|   407.000|  0.000|  12,285|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 48.475|   8,841|
| |Del Norte County|     0|  0.000|  0.000|    99|  3559.615| 56.502|  27,812|
| |Siskiyou County|     0|  0.000|  0.000|    93|  2136.016| 65.623|  43,539|
| |Sierra County|     0|  0.000|  0.000|     3|   998.336| 47.540|   3,005|
| |Plumas County|     0|  0.000|  0.000|    34|  1807.838|  7.596|  18,807|
| |Lassen County|     0|  0.000|  0.000|   638| 20868.086| 32.709|  30,573|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 8,819| 304.147| N/A|497,632| 17162.162| N/A|28,995,881|
| |Harris County| 1,562| 331.401| 24.641|84,600| 17949.112| 294.575|4,713,325|
| |Hidalgo County|   790| 909.398| 24.009|19,534| 22486.293| 415.725| 868,707|
| |Bexar County|   773| 385.814| 11.551|42,531| 21227.778| 123.210|2,003,554|
| |Dallas County|   751| 284.954|  3.794|53,831| 20425.222| 175.677|2,635,516|
| |Tarrant County|   445| 211.651|  4.552|30,922| 14707.148| 170.680|2,102,515|
| |Cameron County|   425| 1004.341| 26.670|16,290| 38495.804| 1795.661| 423,163|
| |Travis County|   298| 233.917|  7.177|22,602| 17741.614| 208.238|1,273,954|
| |El Paso County|   291| 346.743|  7.320|16,040| 19112.576| 277.463| 839,238|
| |Nueces County|   234| 645.884| 22.870|14,073| 38844.143| 698.722| 362,294|
| |Webb County|   163| 589.188| 44.409| 7,825| 28284.632| 874.745| 276,652|
| |Fort Bend County|   161| 198.352|  2.816| 9,533| 11744.661| 431.376| 811,688|
| |Galveston County|   113| 330.275|  6.681| 9,376| 27404.067| 273.490| 342,139|
| |Brazoria County|    92| 245.816|  7.634| 7,215| 19277.836| 259.939| 374,264|
| |Williamson County|    91| 154.093|  2.903| 6,245| 10574.870| 128.210| 590,551|
| |Collin County|    89| 86.013|  2.347| 7,439|  7189.315| 149.936|1,034,730|
| |Denton County|    87| 98.061|  2.093| 7,586|  8550.428| 126.078| 887,207|
| |Montgomery County|    82| 135.004|  2.352| 6,577| 10828.280| 89.610| 607,391|
| |Jefferson County|    80| 318.009|  7.382| 5,870| 23333.930| 215.224| 251,565|
| |Lubbock County|    73| 235.052|  4.140| 6,018| 19377.336| 232.753| 310,569|
| |Comal County|    69| 441.716|  7.316| 1,816| 11625.451| 134.435| 156,209|
| |Starr County|    66| 1021.150| 35.365| 2,148| 33233.797| 755.916|  64,633|
| |Ector County|    56| 336.897|  6.016| 3,531| 21242.548| 209.701| 166,223|
| |McLennan County|    55| 214.322|  8.907| 4,889| 19051.293| 313.411| 256,623|
| |Guadalupe County|    54| 323.650|  9.418| 1,679| 10063.112| 70.210| 166,847|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 541.998|  49,025|
| |Brazos County|    48| 209.414|  3.740| 4,040| 17625.681| 101.591| 229,211|
| |Midland County|    48| 271.444|  4.847| 2,592| 14657.980| 333.650| 176,832|
| |Angelina County|    45| 518.941| 16.474| 1,796| 20711.526| 245.468|  86,715|
| |Potter County|    44| 374.739|  6.083| 3,661| 31180.003| 189.803| 117,415|
| |Nacogdoches County|    42| 644.132| 13.146| 1,147| 17590.945| 271.675|  65,204|
| |Maverick County|    42| 715.234|  7.298| 2,321| 39525.221| 807.680|  58,722|
| |Ellis County|    41| 221.830|  5.410| 2,855| 15446.961| 296.031| 184,826|
| |Victoria County|    41| 445.246| 20.168| 3,448| 37444.073| 380.088|  92,084|
| |Walker County|    41| 561.867|  5.873| 2,902| 39769.223| 172.280|  72,971|
| |Washington County|    39| 1086.896|  3.981|   515| 14352.600| 151.290|  35,882|
| |Bell County|    37| 101.950|  2.362| 3,831| 10555.929| 131.865| 362,924|
| |Hays County|    37| 160.736|  3.103| 5,012| 21773.223| 443.731| 230,191|
| |Liberty County|    34| 385.405| 14.574|   973| 11029.370| 212.134|  88,219|
| |Bowie County|    32| 343.182|  3.064|   764|  8193.469| 85.795|  93,245|
| |Johnson County|    30| 170.632|  4.875| 1,861| 10584.869| 260.011| 175,817|
| |Willacy County|    29| 1357.805| 73.576|   691| 32353.217| 702.313|  21,358|
| |Matagorda County|    26| 709.549| 19.493|   739| 20167.563| 257.309|  36,643|
| |Caldwell County|    26| 595.456|  9.815| 1,136| 26016.856| 215.935|  43,664|
| |Tom Green County|    26| 218.121|  2.397| 2,628| 22046.980| 341.563| 119,200|
| |Medina County|    26| 504.032|  5.539|   811| 15721.929| 600.962|  51,584|
| |Hale County|    26| 778.303| 17.106| 1,285| 38466.144| 427.639|  33,406|
| |Kaufman County|    25| 183.616|  6.295| 2,158| 15849.700| 358.837| 136,154|
| |Wharton County|    25| 601.598| 13.751|   704| 16940.995| 275.016|  41,556|
| |Gregg County|    25| 201.702|  6.916| 1,416| 11424.422| 118.716| 123,945|
| |San Patricio County|    23| 344.673| 14.986|   935| 14011.689| 295.434|  66,730|
| |Smith County|    23| 98.818|  3.683| 2,524| 10844.207| 131.962| 232,751|
| |Taylor County|    23| 166.626|  4.140| 1,126|  8157.410| 45.537| 138,034|
| |Harrison County|    23| 345.589|  2.147|   692| 10397.728| 154.549|  66,553|
| |Grimes County|    23| 796.399| 14.840|   874| 30263.158| 173.130|  28,880|
| |Randall County|    21| 152.491|  4.149| 1,725| 12526.051| 144.192| 137,713|
| |Bastrop County|    21| 236.692|  4.830| 1,358| 15306.065| 99.829|  88,723|
| |Hunt County|    21| 212.995|  1.449| 1,182| 11988.559| 192.709|  98,594|
| |Orange County|    19| 227.829|  5.139| 1,412| 16931.268| 669.782|  83,396|
| |Parker County|    19| 132.981|  6.999| 1,225|  8573.748| 154.977| 142,878|
| |Wilson County|    19| 372.038|  8.392|   439|  8596.045| 69.932|  51,070|
| |DeWitt County|    18| 892.857| 21.259|   693| 34375.000| 1147.959|  20,160|
| |Atascosa County|    18| 351.886|  8.378|   437|  8542.998| 89.368|  51,153|
| |Lamar County|    18| 361.018|  5.730|   629| 12615.576| 25.787|  49,859|
| |Shelby County|    18| 712.194| 11.305|   400| 15826.541| 118.699|  25,274|
| |Panola County|    18| 776.063|  6.159|   291| 12546.348| 135.503|  23,194|
| |Lavaca County|    17| 843.505| 21.265|   627| 31110.450| 241.001|  20,154|
| |Deaf Smith County|    17| 916.640|  0.000|   667| 35964.628| 539.200|  18,546|
| |Brown County|    16| 422.565|  7.546|   391| 10326.431| 150.916|  37,864|
| |Jim Wells County|    15| 370.535| 31.760|   717| 17711.576| 444.642|  40,482|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Hardin County|    15| 260.408|  9.920|   973| 16891.775| 401.772|  57,602|
| |Fayette County|    14| 552.355|  5.636|   378| 14913.596| 61.999|  25,346|
| |Moore County|    13| 620.821|  6.822| 1,050| 50143.266| 252.422|  20,940|
| |Grayson County|    13| 95.439|  2.098| 1,118|  8207.794| 118.513| 136,212|
| |Aransas County|    13| 552.956|  6.076|   172|  7316.036| 115.452|  23,510|
| |Rockwall County|    13| 123.910|  0.000|   896|  8540.247| 239.650| 104,915|
| |Anderson County|    12| 207.846|  9.897| 2,402| 41603.880| 477.551|  57,735|
| |Polk County|    12| 233.677|  8.346|   748| 14565.848| 247.586|  51,353|
| |Henderson County|    12| 145.038|  5.180|   641|  7747.441| 110.505|  82,737|
| |San Augustine County|    11| 1335.438|  0.000|   162| 19667.355| 121.403|   8,237|
| |Red River County|    11| 914.913|  0.000|   136| 11311.653| 23.764|  12,023|
| |Wichita County|    11| 83.188|  1.080| 1,001|  7570.143| 106.956| 132,230|
| |Lamb County|    11| 853.176| 44.321|   226| 17528.892| 254.845|  12,893|
| |Jasper County|    11| 309.606| 24.125|   304|  8556.391| 52.271|  35,529|
| |Uvalde County|    10| 373.958| 16.027|   536| 20044.127| 288.482|  26,741|
| |Hood County|    10| 162.224|  4.635|   528|  8565.449| 210.892|  61,643|
| |Lee County|    10| 580.080| 16.574|   172|  9977.377| 165.737|  17,239|
| |Gonzales County|     9| 431.924| 13.712|   683| 32778.231| 452.492|  20,837|
| |Bee County|     9| 276.370|  0.000| 1,073| 32949.486| 2465.399|  32,565|
| |Burnet County|     9| 186.896|  5.933|   552| 11462.984| 29.666|  48,155|
| |San Jacinto County|     8| 277.210|  0.000|   177|  6133.269| 158.406|  28,859|
| |Cass County|     8| 266.436|  4.758|   174|  5794.978| 99.913|  30,026|
| |Navarro County|     8| 159.639|  0.000|   856| 17081.396| 253.712|  50,113|
| |Marion County|     8| 811.853| 14.497|   133| 13497.057| 144.974|   9,854|
| |Fannin County|     8| 225.263|  0.000|   246|  6926.846| 128.722|  35,514|
| |Cherokee County|     7| 132.964|  8.141| 1,107| 21027.239| 879.188|  52,646|
| |Parmer County|     7| 728.787|  0.000|   340| 35398.230| 431.323|   9,605|
| |Houston County|     7| 304.772|  6.220|   314| 13671.195| 410.509|  22,968|
| |Wood County|     7| 153.714|  6.274|   316|  6939.107| 78.426|  45,539|
| |Kleberg County|     7| 228.162|  9.313|   431| 14048.240| 395.791|  30,680|
| |Hill County|     7| 191.001| 15.592|   319|  8704.194| 42.878|  36,649|
| |Palo Pinto County|     7| 239.816|  4.894|   265|  9078.763| 347.489|  29,189|
| |Andrews County|     7| 374.231|  7.637|   297| 15878.107| 320.770|  18,705|
| |Jackson County|     6| 406.504| 19.357|   406| 27506.775| 832.365|  14,760|
| |Wise County|     6| 85.734|  2.041|   409|  5844.193| 200.046|  69,984|
| |Kerr County|     6| 114.068|  0.000|   398|  7566.540| 135.796|  52,600|
| |Sabine County|     6| 569.152|  0.000|    51|  4837.792| 94.859|  10,542|
| |Gillespie County|     6| 222.321| 10.587|   175|  6484.363| 21.173|  26,988|
| |Karnes County|     6| 384.591| 18.314|   632| 40510.224| 3058.412|  15,601|
| |Floyd County|     6| 1050.420| 25.010|    89| 15581.232| 150.060|   5,712|
| |Burleson County|     6| 325.327|  7.746|   240| 13013.067| 69.713|  18,443|
| |Duval County|     6| 537.779| 38.413|   173| 15505.960| 294.498|  11,157|
| |Frio County|     5| 246.233|  0.000|   512| 25214.222| 260.303|  20,306|
| |Reeves County|     5| 312.969| 17.884|   146|  9138.708| 98.362|  15,976|
| |Erath County|     5| 117.102|  0.000|   527| 12342.498| 217.474|  42,698|
| |Martin County|     5| 866.401| 49.509|    55|  9530.411| 247.543|   5,771|
| |Dallam County|     5| 686.153|  0.000|   190| 26073.830| 215.648|   7,287|
| |Waller County|     5| 90.504|  5.172|   443|  8018.680| 113.777|  55,246|
| |Coryell County|     5| 65.832|  0.000|   667|  8781.978| 103.450|  75,951|
| |Howard County|     5| 136.374|  7.793|   171|  4663.976| 54.549|  36,664|
| |Blanco County|     5| 419.076| 11.974|    98|  8213.897|  0.000|  11,931|
| |Camp County|     5| 381.854| 10.910|   233| 17794.410| 207.292|  13,094|
| |Zavala County|     5| 422.297|  0.000|   210| 17736.486| 422.297|  11,840|
| |Newton County|     4| 294.226|  0.000|    93|  6840.750| 73.556|  13,595|
| |Refugio County|     4| 575.705| 82.244|   220| 31663.788| 514.023|   6,948|
| |Young County|     4| 222.099|  0.000|   169|  9383.676| 237.963|  18,010|
| |Trinity County|     4| 273.019| 19.501|   156| 10647.737| 204.764|  14,651|
| |Hockley County|     4| 173.754|  0.000|   206|  8948.352| 155.138|  23,021|
| |Bailey County|     4| 571.429|  0.000|   171| 24428.571| 265.306|   7,000|
| |Dawson County|     4| 314.268|  0.000|   145| 11392.206| 89.791|  12,728|
| |Lynn County|     4| 672.156|  0.000|    67| 11258.612| 48.011|   5,951|
| |Castro County|     4| 531.208| 18.972|   200| 26560.425| 569.152|   7,530|
| |Kendall County|     4| 84.333|  6.024|   158|  3331.155| 39.155|  47,431|
| |Goliad County|     4| 522.330| 18.655|    89| 11621.833| 223.856|   7,658|
| |Calhoun County|     4| 187.882|  6.710|   544| 25551.902| 610.615|  21,290|
| |Comanche County|     3| 220.022|  0.000|   142| 10414.375|  0.000|  13,635|
| |Van Zandt County|     3| 53.013|  0.000|   375|  6626.612| 108.550|  56,590|
| |Nolan County|     3| 203.887|  0.000|   134|  9106.973| 29.127|  14,714|
| |Yoakum County|     3| 344.313| 32.792|   102| 11706.645| 278.730|   8,713|
| |Brooks County|     3| 422.952| 40.281|    99| 13957.423| 281.968|   7,093|
| |Reagan County|     3| 779.423|  0.000|    63| 16367.888| 185.577|   3,849|
| |Bandera County|     3| 129.803|  0.000|    91|  3937.349| 49.449|  23,112|
| |Milam County|     3| 120.856|  0.000|   333| 13414.978| 155.386|  24,823|
| |Hutchinson County|     3| 143.280|  6.823|   126|  6017.767| 81.874|  20,938|
| |Chambers County|     3| 68.435|  3.259|   951| 21694.003| 208.565|  43,837|
| |Cooke County|     3| 72.715|  3.463|   223|  5405.143| 79.640|  41,257|
| |Crockett County|     3| 866.051|  0.000|   155| 44745.958| 82.481|   3,464|
| |Callahan County|     3| 215.162|  0.000|    46|  3299.147| 51.229|  13,943|
| |Morris County|     3| 242.170| 23.064|   115|  9283.177| 219.106|  12,388|
| |Limestone County|     3| 128.003|  0.000|   233|  9941.545| 207.243|  23,437|
| |Gaines County|     3| 139.587| 19.941|   161|  7491.160| 192.763|  21,492|
| |Austin County|     3| 99.893|  0.000|   230|  7658.498| 80.866|  30,032|
| |Dimmit County|     3| 296.326| 28.221|   150| 14816.278| 366.879|  10,124|
| |Stephens County|     3| 320.307| 15.253|    42|  4484.305| 198.286|   9,366|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402| 45.868|   6,229|
| |Falls County|     3| 173.440|  8.259|   125|  7226.687| 123.886|  17,297|
| |Lampasas County|     3| 140.004| 13.334|   102|  4760.127| 120.003|  21,428|
| |Hamilton County|     3| 354.568| 16.884|    82|  9691.526| 455.873|   8,461|
| |Ochiltree County|     2| 203.335|  0.000|    95|  9658.398| 159.763|   9,836|
| |Madison County|     2| 140.017|  0.000|   666| 46625.595| 210.025|  14,284|
| |Colorado County|     2| 93.054|  0.000|   278| 12934.444| 239.281|  21,493|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Culberson County|     2| 921.234|  0.000|    17|  7830.493| 131.605|   2,171|
| |Brewster County|     2| 217.320|  0.000|   188| 20428.121| 108.660|   9,203|
| |Upshur County|     2| 47.901|  0.000|   220|  5269.082| 99.223|  41,753|
| |Robertson County|     2| 117.137|  8.367|   234| 13705.049| 167.339|  17,074|
| |Zapata County|     2| 141.054|  0.000|   172| 12130.616| 161.204|  14,179|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890|  0.000|   1,501|
| |Hudspeth County|     2| 409.333|  0.000|    23|  4707.327| 29.238|   4,886|
| |Swisher County|     2| 270.380|  0.000|    80| 10815.195| 96.564|   7,397|
| |Terry County|     2| 162.114| 11.580|   143| 11591.149| 312.648|  12,337|
| |Rusk County|     2| 36.761|  0.000|   369|  6782.340| 97.153|  54,406|
| |Tyler County|     2| 92.285|  6.592|   116|  5352.529|  6.592|  21,672|
| |Hopkins County|     2| 53.932|  3.852|   198|  5339.230| 111.715|  37,084|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 94.985|   7,520|
| |Live Oak County|     2| 163.840| 11.703|   230| 18841.648| 269.166|  12,207|
| |Leon County|     2| 114.916|  8.208|   143|  8216.502| 41.041|  17,404|
| |Hansford County|     2| 370.439|  0.000|    73| 13521.022| 370.439|   5,399|
| |Presidio County|     2| 298.329| 42.618|    46|  6861.575| 42.618|   6,704|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 106.560|  10,725|
| |Bosque County|     2| 107.038|  0.000|   161|  8616.537| 275.240|  18,685|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 126.534|   3,387|
| |Gray County|     2| 91.383|  0.000|   215|  9823.632| 208.875|  21,886|
| |Runnels County|     1| 97.428|  0.000|   124| 12081.060| 236.611|  10,264|
| |Real County|     1| 289.687| 41.384|    87| 25202.781| 455.223|   3,452|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 68.495|  12,514|
| |Pecos County|     1| 63.199|  0.000|   244| 15420.590| 315.996|  15,823|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788| 67.641|   2,112|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 51.148|   2,793|
| |Scurry County|     1| 59.869|  0.000|   481| 28797.222| 410.534|  16,703|
| |Sutton County|     1| 264.831|  0.000|    62| 16419.492| 151.332|   3,776|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Jim Hogg County|     1| 192.308|  0.000|    62| 11923.077| 247.253|   5,200|
| |Wilbarger County|     1| 78.315|  0.000|    69|  5403.712| 212.568|  12,769|
| |Ward County|     1| 83.347|  0.000|    89|  7417.903| 71.440|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Montague County|     1| 50.459|  0.000|    70|  3532.142| 93.710|  19,818|
| |Mitchell County|     1| 117.028| 16.718|    61|  7138.678| 150.464|   8,545|
| |Winkler County|     1| 124.844|  0.000|    84| 10486.891| 285.358|   8,010|
| |Clay County|     1| 95.502|  0.000|    40|  3820.074| 81.859|  10,471|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505| 19.664|  21,795|
| |Kimble County|     1| 230.574| 32.939|    13|  2997.464|  0.000|   4,337|
| |McCulloch County|     1| 125.251|  0.000|    48|  6012.024| 125.251|   7,984|
| |Knox County|     1| 272.926| 38.989|    60| 16375.546| 545.852|   3,664|
| |Hall County|     1| 337.382|  0.000|    11|  3711.201| 144.592|   2,964|
| |Crosby County|     1| 174.307|  0.000|    63| 10981.349| 273.911|   5,737|
| |Fisher County|     1| 261.097|  0.000|    28|  7310.705| 149.198|   3,830|
| |Eastland County|     1| 54.466|  0.000|    73|  3976.035| 171.180|  18,360|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Concho County|     0|  0.000|  0.000|    28| 10271.460| 104.811|   2,726|
| |Delta County|     0|  0.000|  0.000|    16|  3001.313| 53.595|   5,331|
| |Donley County|     0|  0.000|  0.000|    48| 14643.075| 217.903|   3,278|
| |Edwards County|     0|  0.000|  0.000|    28| 14492.754| 295.770|   1,932|
| |Collingsworth County|     0|  0.000|  0.000|    11|  3767.123| 195.695|   2,920|
| |Coleman County|     0|  0.000|  0.000|    19|  2324.159| 139.799|   8,175|
| |Carson County|     0|  0.000|  0.000|    15|  2531.218| 48.214|   5,926|
| |Childress County|     0|  0.000|  0.000|    40|  5474.952| 117.320|   7,306|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 550.799|   2,853|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Archer County|     0|  0.000|  0.000|    21|  2455.279| 16.703|   8,553|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Baylor County|     0|  0.000|  0.000|    11|  3134.796| 162.847|   3,509|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    59|  6603.246| 303.781|   8,935|
| |Jones County|     0|  0.000|  0.000|   596| 29676.841|  0.000|  20,083|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008| 187.477|     762|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Kinney County|     0|  0.000|  0.000|    19|  5181.347| 77.915|   3,667|
| |Menard County|     0|  0.000|  0.000|    17|  7951.356| 66.818|   2,138|
| |Mills County|     0|  0.000|  0.000|    22|  4514.673| 205.212|   4,873|
| |Mason County|     0|  0.000|  0.000|    53| 12400.562| 434.521|   4,274|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Lipscomb County|     0|  0.000|  0.000|    18|  5567.584| 132.562|   3,233|
| |McMullen County|     0|  0.000|  0.000|     9| 12113.055| 192.271|     743|
| |Hemphill County|     0|  0.000|  0.000|    42| 10997.643| 37.407|   3,819|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Haskell County|     0|  0.000|  0.000|    42|  7423.118| 176.741|   5,658|
| |Hardeman County|     0|  0.000|  0.000|    18|  4576.659| 108.968|   3,933|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |Hartley County|     0|  0.000|  0.000|    85| 15243.902| 76.860|   5,576|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704| 105.820|   1,350|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Sherman County|     0|  0.000|  0.000|    40| 13236.267| 141.817|   3,022|
| |Shackelford County|     0|  0.000|  0.000|    18|  5513.017| 43.754|   3,265|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Somervell County|     0|  0.000|  0.000|    74|  8106.924| 250.407|   9,128|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 56.510|   5,056|
| |San Saba County|     0|  0.000|  0.000|    24|  3963.666| 47.187|   6,055|
| |Freestone County|     0|  0.000|  0.000|   156|  7911.954| 130.417|  19,717|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,714| 1264.272| N/A|120,293| 17452.731| N/A|6,892,503|
| |Middlesex County| 2,002| 1242.167|  1.684|26,345| 16346.104| 48.219|1,611,699|
| |Essex County| 1,192| 1510.708|  1.811|17,789| 22545.290| 87.630| 789,034|
| |Suffolk County| 1,073| 1334.732|  2.843|21,778| 27090.198| 88.674| 803,907|
| |Worcester County| 1,000| 1203.917|  1.548|13,602| 16375.680| 38.869| 830,622|
| |Norfolk County|   997| 1410.633|  2.223|10,601| 14999.116| 59.829| 706,775|
| |Plymouth County|   720| 1381.422|  2.467| 9,226| 17701.390| 32.617| 521,202|
| |Hampden County|   704| 1509.525|  2.144| 7,582| 16257.408| 45.641| 466,372|
| |Bristol County|   632| 1118.155|  2.275| 9,324| 16496.319| 59.648| 565,217|
| |Barnstable County|   158| 741.819|  1.341| 1,798|  8441.711| 28.841| 212,990|
| |Hampshire County|   129| 802.089|  1.776| 1,170|  7274.762| 33.753| 160,830|
| |Franklin County|    61| 869.194|  2.036|   411|  5856.369| 14.249|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392| 14.864| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,109| 377.554| N/A|525,899| 24485.773| N/A|21,477,737|
| |Miami-Dade County| 1,838| 676.496| 10.043|131,217| 48295.877| 526.327|2,716,940|
| |Palm Beach County|   929| 620.670|  9.163|36,600| 24452.655| 262.088|1,496,770|
| |Broward County|   789| 404.040|  3.438|61,614| 31551.974| 352.392|1,952,778|
| |Pinellas County|   497| 509.746|  8.791|17,725| 18179.562| 164.250| 974,996|
| |Hillsborough County|   388| 263.593|  4.561|32,268| 21921.672| 260.002|1,471,968|
| |Lee County|   334| 433.441|  6.303|16,431| 21322.983| 163.143| 770,577|
| |Polk County|   312| 430.477|  8.476|14,124| 19487.373| 273.779| 724,777|
| |Orange County|   297| 213.140|  6.664|31,395| 22530.378| 197.762|1,393,452|
| |Manatee County|   191| 473.648|  2.126| 9,199| 22811.982| 192.718| 403,253|
| |Duval County|   188| 196.292|  4.624|23,166| 24187.814| 275.048| 957,755|
| |St. Lucie County|   163| 496.502| 16.536| 5,695| 17347.097| 256.301| 328,297|
| |Brevard County|   142| 235.903|  6.408| 5,963|  9906.270| 104.899| 601,942|
| |Sarasota County|   138| 318.161|  5.599| 6,164| 14211.213| 162.045| 433,742|
| |Collier County|   133| 345.543|  3.340|10,265| 26669.126| 223.805| 384,902|
| |Volusia County|   131| 236.768|  4.648| 7,779| 14059.687| 211.723| 553,284|
| |Pasco County|   127| 229.264|  7.995| 6,982| 12604.094| 151.639| 553,947|
| |Escambia County|   120| 376.984| 10.322| 9,297| 29206.826| 623.370| 318,316|
| |Seminole County|   118| 250.092| 10.294| 7,048| 14937.710| 145.938| 471,826|
| |Osceola County|   104| 276.779|  9.505| 9,568| 25463.671| 349.396| 375,751|
| |Martin County|    92| 571.429| 15.084| 3,802| 23614.907| 156.167| 161,000|
| |Charlotte County|    91| 481.711|  1.512| 2,214| 11719.867| 173.930| 188,910|
| |Marion County|    89| 243.449| 10.942| 6,260| 17123.522| 465.407| 365,579|
| |Lake County|    67| 182.503|  6.226| 5,073| 13818.445| 179.390| 367,118|
| |Indian River County|    55| 343.916|  6.253| 2,488| 15557.487| 194.737| 159,923|
| |Clay County|    51| 232.609|  1.955| 3,245| 14800.321| 255.414| 219,252|
| |Bay County|    51| 291.921| 24.531| 4,388| 25116.625| 627.997| 174,705|
| |Hernando County|    47| 242.368| 10.314| 1,975| 10184.612| 197.430| 193,920|
| |Suwannee County|    43| 968.098| 35.379| 1,404| 31609.519| 800.852|  44,417|
| |Okaloosa County|    41| 194.554|  7.457| 3,448| 16361.548| 405.378| 210,738|
| |Sumter County|    41| 309.621|  9.709| 1,284|  9696.420| 208.212| 132,420|
| |Hendry County|    38| 904.288|  6.799| 1,750| 41644.853| 343.358|  42,022|
| |Santa Rosa County|    37| 200.745| 10.076| 3,857| 20926.359| 354.986| 184,313|
| |Highlands County|    37| 348.330| 10.759| 1,396| 13142.411| 267.636| 106,221|
| |Jackson County|    37| 797.173| 15.389| 1,817| 39147.671| 704.837|  46,414|
| |Citrus County|    36| 240.550|  6.682| 1,514| 10116.466| 273.005| 149,657|
| |St. Johns County|    34| 128.461|  3.239| 3,593| 13575.293| 177.578| 264,672|
| |Putnam County|    26| 348.895| 19.170| 1,481| 19873.593| 314.389|  74,521|
| |Alachua County|    26| 96.639|  2.655| 4,088| 15194.597| 264.429| 269,043|
| |Leon County|    24| 81.749|  4.866| 4,922| 16765.333| 305.585| 293,582|
| |Gadsden County|    21| 459.921|  6.257| 1,866| 40867.280| 1342.219|  45,660|
| |DeSoto County|    16| 421.042|  3.759| 1,339| 35235.915| 203.002|  38,001|
| |Walton County|    15| 202.508|  3.857| 1,383| 18671.275| 277.726|  74,071|
| |Columbia County|    15| 209.246|  9.964| 2,835| 39547.471| 567.953|  71,686|
| |Washington County|    14| 549.602|  0.000|   839| 32936.835| 1575.898|  25,473|
| |Monroe County|    13| 175.136|  7.698| 1,514| 20396.616| 363.744|  74,228|
| |Flagler County|    13| 112.964|  3.724| 1,052|  9141.387| 165.101| 115,081|
| |Nassau County|    11| 124.118|  1.612| 1,219| 13754.584| 225.670|  88,625|
| |Okeechobee County|    10| 237.147| 13.551| 1,027| 24354.961| 362.496|  42,168|
| |Madison County|     8| 432.596|  7.725|   700| 37852.160| 633.444|  18,493|
| |Calhoun County|     7| 496.278|  0.000|   462| 32754.342| 1772.421|  14,105|
| |Hardee County|     7| 259.866|  0.000|   950| 35267.476| 578.068|  26,937|
| |Liberty County|     6| 718.219| 68.402|   400| 47881.254| 17.100|   8,354|
| |Union County|     5| 328.149|  9.376|   297| 19492.026| 740.678|  15,237|
| |Jefferson County|     5| 350.976|  0.000|   448| 31447.424| 1113.094|  14,246|
| |Taylor County|     4| 185.451|  6.623|   947| 43905.605| 3887.855|  21,569|
| |Wakulla County|     4| 118.557|  0.000|   680| 20154.717| 347.203|  33,739|
| |Bradford County|     4| 141.839|  0.000|   469| 16630.616| 693.998|  28,201|
| |Baker County|     4| 136.939|  0.000|   827| 28312.222| 2230.156|  29,210|
| |Dixie County|     4| 237.727|  0.000|   475| 28230.120| 1791.445|  16,826|
| |Levy County|     4| 96.379|  3.442|   673| 16215.695| 309.788|  41,503|
| |Hamilton County|     4| 277.239|  9.901|   617| 42764.070| 425.759|  14,428|
| |Gilchrist County|     3| 161.447|  0.000|   355| 19104.510| 199.886|  18,582|
| |Glades County|     3| 217.218|  0.000|   401| 29034.827| 103.437|  13,811|
| |Franklin County|     2| 164.948|  0.000|   398| 32824.742| 3322.533|  12,125|
| |Gulf County|     2| 146.638|  0.000|   599| 43918.176| 2367.161|  13,639|
| |Holmes County|     2| 101.952|  0.000|   494| 25182.240| 444.221|  19,617|
| |Lafayette County|     1| 118.737|  0.000|   134| 15910.710| 390.135|   8,422|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,631| 602.202| N/A|192,645| 15202.630| N/A|12,671,821|
| |Cook County| 4,924| 956.073|  0.999|110,865| 21526.211| 131.312|5,150,233|
| |DuPage County|   520| 563.429|  1.548|12,155| 13170.141| 119.961| 922,921|
| |Lake County|   446| 640.312|  1.231|12,617| 18113.950| 136.389| 696,535|
| |Will County|   344| 498.014|  1.034| 9,151| 13248.053| 134.224| 690,743|
| |Kane County|   305| 572.874|  2.147| 9,710| 18238.064| 153.482| 532,403|
| |St. Clair County|   161| 619.980|  2.751| 3,953| 15222.230| 211.244| 259,686|
| |Winnebago County|   131| 463.599|  4.550| 3,772| 13348.810| 55.106| 282,572|
| |McHenry County|   114| 370.402|  0.464| 3,163| 10277.021| 117.897| 307,774|
| |Madison County|    76| 289.011|  2.173| 2,530|  9621.016| 213.499| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,768| 16092.917| 124.832| 109,862|
| |Rock Island County|    36| 253.737|  6.041| 1,731| 12200.537| 168.151| 141,879|
| |Peoria County|    35| 195.335|  0.797| 1,574|  8784.512| 234.402| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,229|  6313.183| 178.322| 194,672|
| |DeKalb County|    30| 285.995|  1.362|   927|  8837.240| 136.188| 104,897|
| |LaSalle County|    24| 220.854|  7.888|   739|  6800.467| 318.135| 108,669|
| |Kendall County|    23| 178.308|  0.000| 1,364| 10574.463| 96.353| 128,990|
| |Union County|    23| 1381.133| 17.157|   321| 19275.806| 214.462|  16,653|
| |Macon County|    23| 221.135|  0.000|   611|  5874.492| 221.135| 104,009|
| |Boone County|    23| 429.553|  0.000|   761| 14212.610| 90.713|  53,544|
| |Coles County|    20| 395.093|  2.822|   474|  9363.703| 251.166|  50,621|
| |Jefferson County|    19| 504.193|  7.582|   282|  7483.282| 371.510|  37,684|
| |Jackson County|    19| 334.802|  0.000|   708| 12475.771| 193.833|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,663|  7930.793| 102.192| 209,689|
| |Clinton County|    17| 452.585|  0.000|   396| 10542.570| 239.604|  37,562|
| |Whiteside County|    17| 308.111|  2.589|   351|  6361.577| 113.923|  55,175|
| |McDonough County|    15| 505.357|  0.000|   141|  4750.354| 77.007|  29,682|
| |McLean County|    15| 87.455|  0.000|   638|  3719.748| 71.630| 171,517|
| |Monroe County|    13| 375.321|  0.000|   312|  9007.709| 173.225|  34,637|
| |Iroquois County|    11| 405.694| 21.075|   261|  9626.023| 84.300|  27,114|
| |Cass County|    11| 905.573|  0.000|   230| 18934.716| 376.342|  12,147|
| |Tazewell County|     8| 60.697|  0.000|   497|  3770.779| 147.406| 131,803|
| |Randolph County|     7| 220.250|  0.000|   457| 14379.208| 157.322|  31,782|
| |Jasper County|     7| 728.408|  0.000|    58|  6035.380| 104.058|   9,610|
| |Montgomery County|     7| 246.357|  5.028|   165|  5806.997| 120.665|  28,414|
| |Williamson County|     6| 90.094|  2.145|   388|  5826.088| 156.592|  66,597|
| |Stephenson County|     6| 134.838|  0.000|   327|  7348.645| 44.946|  44,498|
| |Morgan County|     6| 178.264|  4.244|   242|  7189.970| 224.952|  33,658|
| |Ogle County|     5| 98.730|  0.000|   409|  8076.141| 107.193|  50,643|
| |Grundy County|     5| 97.936|  0.000|   316|  6189.525| 117.523|  51,054|
| |Adams County|     5| 76.412|  8.733|   517|  7900.970| 233.602|  65,435|
| |Mercer County|     4| 259.118| 37.017|    74|  4793.678| 55.525|  15,437|
| |Carroll County|     4| 279.623|  9.987|    54|  3774.904| 99.865|  14,305|
| |Christian County|     4| 123.824|  0.000|   137|  4240.961| 114.979|  32,304|
| |Bureau County|     3| 91.946|  4.378|   190|  5823.219| 253.945|  32,628|
| |Bond County|     3| 182.637|  8.697|    60|  3652.746| 95.667|  16,426|
| |Fayette County|     3| 140.607|  0.000|    65|  3046.494| 73.652|  21,336|
| |Woodford County|     3| 78.005|  0.000|   146|  3796.251| 204.299|  38,459|
| |Macoupin County|     3| 66.776|  0.000|   170|  3784.000| 124.013|  44,926|
| |Douglas County|     2| 102.749|  0.000|   115|  5908.040| 95.409|  19,465|
| |Ford County|     2| 154.309| 11.022|    49|  3780.572| 110.221|  12,961|
| |Cumberland County|     2| 185.770|  0.000|    54|  5015.790| 106.154|  10,766|
| |Saline County|     2| 85.139|  6.081|   131|  5576.604| 158.115|  23,491|
| |Vermilion County|     2| 26.400|  0.000|   234|  3088.783| 64.114|  75,758|
| |Jersey County|     2| 91.857|  6.561|   104|  4776.558| 255.887|  21,773|
| |Gallatin County|     2| 414.250| 59.179|    51| 10563.380| 236.714|   4,828|
| |Clark County|     2| 129.525| 18.504|    81|  5245.774| 138.777|  15,441|
| |Livingston County|     2| 56.104|  0.000|   110|  3085.727| 72.134|  35,648|
| |Lee County|     1| 29.329|  0.000|   170|  4985.922| 100.556|  34,096|
| |Perry County|     1| 47.810|  0.000|   156|  7458.405| 375.652|  20,916|
| |Knox County|     1| 20.121|  0.000|   297|  5975.975| 132.225|  49,699|
| |Jo Daviess County|     1| 47.092|  0.000|   124|  5839.416| 80.729|  21,235|
| |Henry County|     1| 20.444|  0.000|   234|  4784.004| 113.905|  48,913|
| |Shelby County|     1| 46.224|  0.000|    79|  3651.659| 151.877|  21,634|
| |Effingham County|     1| 29.405|  0.000|   150|  4410.727| 231.038|  34,008|
| |Hancock County|     1| 56.472|  0.000|    53|  2992.998| 185.550|  17,708|
| |Wayne County|     1| 61.671|  0.000|    61|  3761.949| 158.583|  16,215|
| |Mason County|     0|  0.000|  0.000|    47|  3518.227| 53.469|  13,359|
| |Marshall County|     0|  0.000|  0.000|    26|  2273.125| 62.448|  11,438|
| |Putnam County|     0|  0.000|  0.000|    11|  1916.710| 99.569|   5,739|
| |Pulaski County|     0|  0.000|  0.000|    93| 17432.052| 80.332|   5,335|
| |Pope County|     0|  0.000|  0.000|     9|  2154.656| 68.402|   4,177|
| |Pike County|     0|  0.000|  0.000|    21|  1349.528| 73.444|  15,561|
| |Piatt County|     0|  0.000|  0.000|    61|  3732.256| 183.554|  16,344|
| |Moultrie County|     0|  0.000|  0.000|    73|  5034.136| 206.882|  14,501|
| |Menard County|     0|  0.000|  0.000|    54|  4427.681| 105.421|  12,196|
| |Massac County|     0|  0.000|  0.000|    39|  2831.833| 51.865|  13,772|
| |Schuyler County|     0|  0.000|  0.000|    18|  2659.574| 63.323|   6,768|
| |White County|     0|  0.000|  0.000|    67|  4949.398| 105.531|  13,537|
| |Richland County|     0|  0.000|  0.000|    19|  1224.779| 64.462|  15,513|
| |Washington County|     0|  0.000|  0.000|    66|  4752.646| 102.871|  13,887|
| |Warren County|     0|  0.000|  0.000|   190| 11279.981| 84.812|  16,844|
| |Wabash County|     0|  0.000|  0.000|    34|  2951.389| 49.603|  11,520|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    19|  3837.609| 259.688|   4,951|
| |Hamilton County|     0|  0.000|  0.000|    29|  3573.189| 158.417|   8,116|
| |Greene County|     0|  0.000|  0.000|    39|  3007.171| 220.306|  12,969|
| |Fulton County|     0|  0.000|  0.000|    33|   960.978| 33.281|  34,340|
| |Franklin County|     0|  0.000|  0.000|   168|  4367.153| 185.678|  38,469|
| |Marion County|     0|  0.000|  0.000|   156|  4192.985| 92.154|  37,205|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 74.775|   3,821|
| |Henderson County|     0|  0.000|  0.000|    12|  1805.597| 64.486|   6,646|
| |Logan County|     0|  0.000|  0.000|   111|  3878.678| 129.788|  28,618|
| |Edwards County|     0|  0.000|  0.000|    17|  2658.327| 89.356|   6,395|
| |Edgar County|     0|  0.000|  0.000|    29|  1689.878| 33.298|  17,161|
| |De Witt County|     0|  0.000|  0.000|    32|  2046.297| 45.676|  15,638|
| |Crawford County|     0|  0.000|  0.000|    29|  1553.544|  0.000|  18,667|
| |Clay County|     0|  0.000|  0.000|    23|  1744.539| 108.356|  13,184|
| |Calhoun County|     0|  0.000|  0.000|     9|  1899.135| 60.290|   4,739|
| |Brown County|     0|  0.000|  0.000|    13|  1976.285|  0.000|   6,578|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Lawrence County|     0|  0.000|  0.000|    48|  3061.615| 72.896|  15,678|
| |Johnson County|     0|  0.000|  0.000|    66|  5315.294| 126.555|  12,417|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,310| 571.005| N/A|122,665|  9581.714| N/A|12,801,989|
| |Philadelphia County| 1,698| 1071.926| N/A|31,120| 19645.671| N/A|1,584,064|
| |Montgomery County|   857| 1031.393|  1.203|10,077| 12127.594| 45.389| 830,915|
| |Delaware County|   698| 1231.590|  3.025| 9,170| 16180.059| 100.826| 566,747|
| |Bucks County|   582| 926.353|  0.910| 7,173| 11417.066| 48.660| 628,270|
| |Lancaster County|   411| 753.128|  1.047| 5,856| 10730.699| 69.632| 545,724|
| |Berks County|   368| 873.769|  1.018| 5,353| 12710.013| 62.751| 421,164|
| |Chester County|   349| 664.776|  0.000| 5,102|  9718.299| 59.049| 524,989|
| |Lehigh County|   337| 912.493|  0.774| 4,934| 13359.760| 41.002| 369,318|
| |Northampton County|   292| 956.483|  0.936| 3,918| 12833.909| 35.096| 305,285|
| |Allegheny County|   247| 203.117|  1.645| 8,796|  7233.285| 74.715|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,927|  9190.458| 19.759| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,438| 10831.178| 72.910| 317,417|
| |Dauphin County|   159| 571.328|  2.053| 2,774|  9967.697| 64.165| 278,299|
| |Monroe County|   124| 728.251|  0.839| 1,624|  9537.737| 31.043| 170,271|
| |York County|    93| 207.100|  1.909| 2,501|  5569.436| 68.397| 449,058|
| |Beaver County|    92| 561.219|  2.614| 1,312|  8003.465| 81.046| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,282|  5059.794| 35.521| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,595| 11248.792| 30.225| 141,793|
| |Schuylkill County|    51| 360.784|  2.021|   909|  6430.436| 24.254| 141,359|
| |Franklin County|    46| 296.723|  0.000| 1,343|  8663.007| 61.740| 155,027|
| |Westmoreland County|    46| 131.843|  0.000| 1,523|  4365.160| 41.355| 348,899|
| |Columbia County|    35| 538.760|  0.000|   471|  7250.169| 26.388|  64,964|
| |Carbon County|    28| 436.259|  0.000|   370|  5764.856| 24.484|  64,182|
| |Susquehanna County|    27| 669.510|  3.542|   214|  5306.487| 17.712|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  5.120|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   381|  3362.783| 61.783| 113,299|
| |Adams County|    20| 194.158|  0.000|   498|  4834.529| 40.218| 103,009|
| |Erie County|    18| 66.734|  1.059| 1,094|  4055.938| 74.149| 269,728|
| |Lawrence County|    16| 187.108|  6.682|   390|  4560.763| 86.872|  85,512|
| |Butler County|    15| 79.850|  0.000|   656|  3492.092| 42.586| 187,853|
| |Northumberland County|    13| 143.104|  3.145|   460|  5063.681| 92.782|  90,843|
| |Washington County|    12| 58.009|  0.691|   829|  4007.444| 56.628| 206,865|
| |Centre County|    10| 61.582|  0.000|   370|  2278.536| 14.076| 162,385|
| |Wayne County|     9| 175.230|  2.781|   160|  3115.204|  5.563|  51,361|
| |Mercer County|     9| 82.249|  0.000|   419|  3829.142| 101.832| 109,424|
| |Wyoming County|     8| 298.574|  0.000|    60|  2239.307| 15.995|  26,794|
| |Armstrong County|     7| 108.133|  2.207|   208|  3213.100| 52.963|  64,735|
| |Indiana County|     6| 71.367|  0.000|   313|  3722.955| 81.562|  84,073|
| |Juniata County|     6| 242.297|  0.000|   132|  5330.533| 34.614|  24,763|
| |Fayette County|     5| 38.678|  1.105|   485|  3751.721| 90.616| 129,274|
| |Clinton County|     5| 129.426|  0.000|   119|  3080.348| 14.792|  38,632|
| |Perry County|     5| 108.057|  0.000|   123|  2658.195| 15.437|  46,272|
| |Blair County|     5| 41.041|  2.345|   274|  2249.054| 70.356| 121,829|
| |Huntingdon County|     4| 88.605|  0.000|   305|  6756.158| 53.796|  45,144|
| |Bedford County|     4| 83.528|  0.000|   141|  2944.370| 38.781|  47,888|
| |Tioga County|     3| 73.908|  3.519|    38|   936.168| 10.558|  40,591|
| |Somerset County|     3| 40.846|  1.945|   133|  1810.830| 17.505|  73,447|
| |Bradford County|     3| 49.732|  0.000|    85|  1409.081|  9.473|  60,323|
| |Cambria County|     3| 23.043|  0.000|   335|  2573.123| 83.393| 130,192|
| |Montour County|     3| 164.564|  0.000|   101|  5540.318| 62.691|  18,230|
| |Union County|     2| 44.521|  0.000|   218|  4852.748| 168.542|  44,923|
| |Snyder County|     2| 49.539|  0.000|   102|  2526.504| 28.308|  40,372|
| |Clarion County|     2| 52.032|  0.000|    78|  2029.242|  7.433|  38,438|
| |Fulton County|     2| 137.646|  0.000|    27|  1858.224| 49.159|  14,530|
| |Elk County|     2| 66.867|  0.000|    48|  1604.814| 23.881|  29,910|
| |McKean County|     1| 24.615|  0.000|    34|   836.923| 21.099|  40,625|
| |Mifflin County|     1| 21.674|  0.000|   120|  2600.893| 46.445|  46,138|
| |Jefferson County|     1| 23.028|  0.000|    68|  1565.918| 32.897|  43,425|
| |Crawford County|     1| 11.816|  0.000|   141|  1666.096| 25.321|  84,629|
| |Greene County|     1| 27.599|  0.000|   114|  3146.303| 27.599|  36,233|
| |Warren County|     1| 25.516|  0.000|    23|   586.869| 25.516|  39,191|
| |Cameron County|     0|  0.000|  0.000|     6|  1349.224|  0.000|   4,447|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Venango County|     0|  0.000|  0.000|    63|  1243.388|  2.819|  50,668|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Clearfield County|     0|  0.000|  0.000|   166|  2094.505| 57.680|  79,255|
| |Forest County|     0|  0.000|  0.000|    10|  1379.881| 19.713|   7,247|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,444| 645.248| N/A|91,525|  9164.545| N/A|9,986,857|
| |Wayne County| 2,826| 1615.464|  1.878|28,090| 16057.457| 74.069|1,749,343|
| |Oakland County| 1,129| 897.753|  0.341|15,427| 12267.173| 80.199|1,257,584|
| |Macomb County|   946| 1082.415|  1.635|10,339| 11829.898| 126.516| 873,972|
| |Genesee County|   295| 726.936|  0.352| 3,639|  8967.184| 53.508| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,485| 11393.474| 82.632| 656,955|
| |Saginaw County|   131| 687.523|  1.500| 1,986| 10423.063| 112.463| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,522|  6860.700| 53.241| 367,601|
| |Kalamazoo County|    83| 313.130|  1.078| 1,631|  6153.184| 48.505| 265,066|
| |Berrien County|    66| 430.245|  0.931| 1,357|  8846.096| 68.914| 153,401|
| |Muskegon County|    59| 339.928|  0.823| 1,170|  6740.952| 39.507| 173,566|
| |Ottawa County|    56| 191.893|  0.979| 1,800|  6167.975| 29.861| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   810|  5090.242| 35.012| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   789|  5881.081| 55.371| 134,159|
| |Jackson County|    34| 214.498|  0.901|   709|  4472.904| 26.136| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   464|  5296.380| 84.794|  87,607|
| |Bay County|    31| 300.603|  0.000|   620|  6012.063| 108.051| 103,126|
| |Ingham County|    30| 102.597|  0.000| 1,541|  5270.070| 33.222| 292,406|
| |Tuscola County|    29| 555.077|  5.469|   342|  6546.081| 103.906|  52,245|
| |Livingston County|    28| 145.837|  0.000|   826|  4302.195| 42.412| 191,995|
| |Shiawassee County|    28| 411.027|  0.000|   340|  4991.045| 31.456|  68,122|
| |Hillsdale County|    25| 548.186|  0.000|   265|  5810.766| 46.987|  45,605|
| |Monroe County|    24| 159.468|  1.898|   972|  6458.472| 85.430| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   155|  3807.325| 38.600|  40,711|
| |Cass County|    14| 270.338| 11.034|   320|  6179.157| 82.757|  51,787|
| |Alpena County|    13| 457.666|  0.000|   128|  4506.249| 15.088|  28,405|
| |Clinton County|    13| 163.327|  0.000|   422|  5301.841| 17.948|  79,595|
| |Lenawee County|    12| 121.888|  0.000|   422|  4286.396| 46.434|  98,451|
| |Iosco County|    12| 477.574|  0.000|   130|  5173.718|  5.685|  25,127|
| |Marquette County|    11| 164.920|  0.000|   153|  2293.887| 42.836|  66,699|
| |Midland County|    10| 120.256|  1.718|   330|  3968.445| 54.974|  83,156|
| |Otsego County|    10| 405.383|  0.000|   134|  5432.139| 17.374|  24,668|
| |Van Buren County|     9| 118.926|  0.000|   442|  5840.612| 71.733|  75,677|
| |Isabella County|     9| 128.807|  0.000|   205|  2933.936| 14.312|  69,872|
| |St. Joseph County|     8| 131.225|  2.343|   587|  9628.633| 84.359|  60,964|
| |Eaton County|     8| 72.551|  1.296|   459|  4162.586| 10.364| 110,268|
| |Allegan County|     7| 59.281|  0.000|   522|  4420.694| 29.036| 118,081|
| |Ionia County|     6| 92.740|  2.208|   274|  4235.127| 17.665|  64,697|
| |Oceana County|     6| 226.697|  0.000|   475| 17946.877| 70.168|  26,467|
| |Sanilac County|     6| 145.737|  0.000|   106|  2574.690| 52.049|  41,170|
| |Grand Traverse County|     5| 53.713|  0.000|   208|  2234.445| 18.416|  93,088|
| |Crawford County|     5| 356.405|  0.000|   106|  7555.777| 112.013|  14,029|
| |Huron County|     4| 129.111|  0.000|   156|  5035.344| 46.111|  30,981|
| |Kalkaska County|     4| 221.754|  0.000|    52|  2882.803| 31.679|  18,038|
| |Wexford County|     4| 118.938|  0.000|    69|  2051.679| 21.239|  33,631|
| |Arenac County|     3| 201.572|  0.000|    41|  2754.821|  9.599|  14,883|
| |Clare County|     3| 96.931|  0.000|    71|  2294.023| 55.389|  30,950|
| |Delta County|     3| 83.836|  0.000|    90|  2515.091| 51.899|  35,784|
| |Barry County|     2| 32.494|  0.000|   180|  2924.452| 20.889|  61,550|
| |Branch County|     2| 45.959|  0.000|   364|  8364.547| 121.463|  43,517|
| |Cheboygan County|     2| 79.126|  0.000|    46|  1819.908| 45.215|  25,276|
| |Charlevoix County|     2| 76.502|  0.000|    47|  1797.804| 27.322|  26,143|
| |Mecosta County|     2| 46.027|  0.000|    68|  1564.909| 39.451|  43,453|
| |Gladwin County|     2| 78.589|  0.000|    58|  2279.068| 33.681|  25,449|
| |Ogemaw County|     2| 95.252|  0.000|    54|  2571.796| 20.411|  20,997|
| |Emmet County|     2| 59.853|  0.000|    62|  1855.454| 25.651|  33,415|
| |Dickinson County|     2| 79.242|  0.000|    53|  2099.925| 45.281|  25,239|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Montmorency County|     1| 107.204| 15.315|     9|   964.837| 15.315|   9,328|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  9.449|  15,118|
| |Presque Isle County|     1| 79.416|  0.000|    20|  1588.310| 45.380|  12,592|
| |Iron County|     1| 90.367|  0.000|    19|  1716.971| 25.819|  11,066|
| |Gogebic County|     1| 71.556|  0.000|   119|  8515.206| 316.892|  13,975|
| |Montcalm County|     1| 15.652|  0.000|   188|  2942.650| 20.125|  63,888|
| |Benzie County|     1| 56.287|  0.000|    28|  1576.044|  0.000|  17,766|
| |Alcona County|     1| 96.108|  0.000|    28|  2691.014|  0.000|  10,405|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128| 70.599|   8,094|
| |Ontonagon County|     0|  0.000|  0.000|    11|  1923.077| 174.825|   5,720|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428| 18.268|  23,460|
| |Roscommon County|     0|  0.000|  0.000|    53|  2206.586| 35.686|  24,019|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|
| |Newaygo County|     0|  0.000|  0.000|   250|  5104.124| 11.667|  48,980|
| |Menominee County|     0|  0.000|  0.000|   131|  5750.658| 250.847|  22,780|
| |Mason County|     0|  0.000|  0.000|   101|  3465.550| 19.607|  29,144|
| |Manistee County|     0|  0.000|  0.000|    35|  1425.197| 17.451|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    27|  2500.232| 92.601|  10,799|
| |Luce County|     0|  0.000|  0.000|     3|   481.618|  0.000|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    71|  3262.718| 45.954|  21,761|
| |Lake County|     0|  0.000|  0.000|    21|  1771.703| 48.210|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    50|  1401.188| 12.010|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    39|  1044.205| 30.599|  37,349|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846| 30.624|  23,324|
| |Alger County|     0|  0.000|  0.000|    11|  1207.729| 47.054|   9,108|


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


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,136| 568.232| N/A|186,107| 25568.654| N/A|7,278,717|
| |Maricopa County| 2,347| 523.252|  8.217|125,545| 27989.613| 199.058|4,485,414|
| |Pima County|   489| 466.924|  3.683|17,728| 16927.676| 170.919|1,047,279|
| |Yuma County|   286| 1337.780| 21.383|11,512| 53847.989| 290.008| 213,787|
| |Navajo County|   199| 1794.021| 14.167| 5,368| 48393.495| 145.531| 110,924|
| |Mohave County|   165| 777.638|  8.079| 3,150| 14845.816| 107.725| 212,181|
| |Pinal County|   156| 337.087|  4.939| 8,356| 18055.745| 62.664| 462,789|
| |Apache County|   139| 1933.590|  7.949| 3,155| 43888.325| 200.712|  71,887|
| |Coconino County|   117| 815.467|  0.000| 3,076| 21439.126| 111.517| 143,476|
| |Yavapai County|    67| 284.986|  4.254| 1,980|  8421.984| 122.745| 235,099|
| |Santa Cruz County|    53| 1139.834|  9.217| 2,658| 57163.749| 147.472|  46,498|
| |Cochise County|    52| 412.954|  3.403| 1,600| 12706.278| 87.356| 125,922|
| |Gila County|    38| 703.469| 23.802|   905| 16753.675| 219.504|  54,018|
| |Graham County|    15| 386.230| 22.070|   539| 13878.518| 224.381|  38,837|
| |La Paz County|    12| 568.505| 13.536|   478| 22645.442| 40.607|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263| 30.082|   9,498|


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
| |St. Landry Parish|    85| 1035.020| 22.614| 2,631| 32036.920| 955.002|  82,124|
| |Terrebonne Parish|    85| 769.502| 14.226| 2,986| 27032.165| 378.931| 110,461|
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
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   780| 35895.076| 486.490|  21,730|
| |St. James Parish|    32| 1516.875|  6.772|   693| 32849.829| 467.252|  21,096|
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
| |Franklin Parish|    17| 849.363|  7.138|   896| 44766.425| 792.263|  20,015|
| |Natchitoches Parish|    17| 445.516|  0.000|   761| 19943.393| 370.639|  38,158|
| |Grant Parish|    16| 714.637| 51.045|   298| 13310.108| 178.659|  22,389|
| |West Feliciana Parish|    16| 1027.749|  9.176|   345| 22160.843| 211.056|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   868| 22639.541| 212.385|  38,340|
| |Red River Parish|    11| 1303.009| 16.922|   212| 25112.533| 558.432|   8,442|
| |Morehouse Parish|    11| 442.229|  0.000|   494| 19860.095| 379.053|  24,874|
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
| |East Carroll Parish|     1| 145.751|  0.000|   518| 75499.198| 520.541|   6,861|
| |St. Helena Parish|     1| 98.697|  0.000|   258| 25463.877| 281.992|  10,132|
| |Cameron Parish|     0|  0.000|  0.000|   167| 23949.520| 61.462|   6,973|
| |Tensas Parish|     0|  0.000|  0.000|    70| 16151.361| 461.467|   4,334|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,086| 384.839| N/A|194,749| 18342.398| N/A|10,617,423|
| |Fulton County|   430| 404.159|  4.297|20,049| 18844.161| 294.190|1,063,937|
| |Cobb County|   319| 419.659|  3.947|13,336| 17544.114| 357.077| 760,141|
| |Gwinnett County|   260| 277.704|  3.052|19,548| 20879.039| 310.814| 936,250|
| |DeKalb County|   237| 312.131|  2.258|13,752| 18111.490| 264.154| 759,297|
| |Dougherty County|   170| 1932.785|  3.248| 2,684| 30515.258| 154.298|  87,956|
| |Clayton County|   110| 376.382|  4.888| 4,952| 16944.049| 236.583| 292,256|
| |Muscogee County|    96| 490.374| 10.216| 4,685| 23931.266| 310.862| 195,769|
| |Hall County|    91| 445.116|  8.385| 6,035| 29519.519| 386.420| 204,441|
| |Richmond County|    90| 444.405|  4.938| 4,218| 20827.778| 444.405| 202,518|
| |Chatham County|    75| 259.130|  3.949| 5,665| 19572.954| 372.160| 289,430|
| |Troup County|    69| 986.814| 12.259| 2,280| 32607.763| 247.214|  69,922|
| |Bibb County|    68| 443.983|  6.529| 3,554| 23204.644| 416.934| 153,159|
| |Cherokee County|    63| 243.457|  3.864| 3,398| 13131.200| 335.098| 258,773|
| |Bartow County|    62| 575.470|  3.978| 1,853| 17199.131| 358.011| 107,738|
| |Houston County|    58| 367.407|  8.144| 1,948| 12339.814| 182.799| 157,863|
| |Sumter County|    56| 1896.762|  0.000|   757| 25640.157| 159.676|  29,524|
| |Douglas County|    51| 348.496|  1.952| 2,602| 17780.147| 315.306| 146,343|
| |Habersham County|    49| 1081.010|  3.152| 1,135| 25039.711| 343.528|  45,328|
| |Carroll County|    49| 408.361|  2.381| 1,862| 15517.701| 191.679| 119,992|
| |Glynn County|    47| 551.048| 30.149| 2,487| 29158.655| 345.033|  85,292|
| |Henry County|    47| 200.374|  3.654| 3,320| 14154.101| 222.909| 234,561|
| |Upson County|    46| 1747.720|  0.000|   523| 19870.821| 227.964|  26,320|
| |Lowndes County|    44| 374.768| 14.601| 3,156| 26881.079| 273.775| 117,406|
| |Thomas County|    42| 944.861|  9.641| 1,109| 24948.820| 408.154|  44,451|
| |Mitchell County|    41| 1875.314|  0.000|   648| 29639.116| 254.834|  21,863|
| |Spalding County|    41| 614.665|  4.283|   931| 13957.393| 182.044|  66,703|
| |Newton County|    40| 357.961|  6.392| 1,764| 15786.082| 253.130| 111,744|
| |Walton County|    39| 412.293|  7.551| 1,103| 11660.482| 255.229|  94,593|
| |Baldwin County|    39| 868.790|  3.182| 1,035| 23056.360| 292.779|  44,890|
| |Butts County|    37| 1483.799|  0.000|   487| 19529.997| 137.495|  24,936|
| |Tift County|    36| 885.740|  3.515| 1,321| 32501.722| 281.187|  40,644|
| |Hancock County|    35| 4138.583| 16.892|   315| 37247.251| 574.334|   8,457|
| |Barrow County|    32| 384.431|  0.000| 1,278| 15353.196| 312.350|  83,240|
| |Early County|    32| 3140.334| 14.019|   359| 35230.618| 182.252|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   301| 35283.085| 167.457|   8,531|
| |Whitfield County|    29| 277.172|  4.096| 3,496| 33413.618| 492.903| 104,628|
| |Fayette County|    28| 244.710|  3.746| 1,100|  9613.620| 188.527| 114,421|
| |Coffee County|    28| 647.055|  9.904| 1,447| 33438.865| 406.060|  43,273|
| |Monroe County|    26| 942.780| 15.540|   453| 16426.137| 191.664|  27,578|
| |Randolph County|    26| 3835.940|  0.000|   270| 39834.760| 231.843|   6,778|
| |Ware County|    25| 699.614|  7.996| 1,135| 31762.467| 247.863|  35,734|
| |Jenkins County|    24| 2766.252| 32.932|   243| 28008.299| 214.055|   8,676|
| |Colquitt County|    23| 504.386|  3.133| 1,537| 33706.140| 200.501|  45,600|
| |Columbia County|    23| 146.764|  3.646| 2,188| 13961.739| 309.937| 156,714|
| |Gordon County|    23| 396.805|  0.000| 1,171| 20202.543| 418.986|  57,963|
| |Worth County|    23| 1135.971|  0.000|   444| 21929.175| 162.282|  20,247|
| |Forsyth County|    22| 90.071|  1.755| 2,224|  9105.350| 190.670| 244,252|
| |Coweta County|    22| 148.139|  0.962| 1,485|  9999.394| 165.454| 148,509|
| |Lee County|    22| 733.529|  0.000|   535| 17838.090| 138.132|  29,992|
| |Paulding County|    22| 130.435|  2.541| 1,651|  9788.518| 211.744| 168,667|
| |Wilcox County|    19| 2200.347| 16.544|   181| 20961.204| 281.247|   8,635|
| |Appling County|    19| 1033.395| 23.310|   645| 35081.040| 458.423|  18,386|
| |Brooks County|    18| 1164.521| 27.727|   408| 26395.808| 351.205|  15,457|
| |Clarke County|    18| 140.262|  1.113| 2,027| 15795.092| 370.693| 128,331|
| |Turner County|    18| 2254.227|  0.000|   245| 30682.530| 375.704|   7,985|
| |Putnam County|    18| 813.780|  6.459|   424| 19169.040| 303.553|  22,119|
| |Rockdale County|    17| 187.027|  1.572| 1,302| 14324.063| 235.748|  90,896|
| |Floyd County|    17| 172.592|  2.901| 1,488| 15106.906| 355.337|  98,498|
| |Walker County|    17| 243.689|  2.048|   684|  9804.905| 278.502|  69,761|
| |Harris County|    17| 482.461|  4.054|   652| 18503.803| 145.955|  35,236|
| |Jackson County|    16| 219.247|  5.873| 1,059| 14511.421| 240.780|  72,977|
| |Oconee County|    15| 372.393|  0.000|   432| 10724.926| 159.597|  40,280|
| |Crisp County|    14| 625.782|  0.000|   374| 16717.325| 83.012|  22,372|
| |Dooly County|    14| 1045.556|  0.000|   252| 18820.015| 106.689|  13,390|
| |Bulloch County|    14| 175.862|  3.589| 1,242| 15601.447| 267.382|  79,608|
| |Peach County|    12| 435.635|  0.000|   374| 13577.289| 290.423|  27,546|
| |Greene County|    12| 654.879|  7.796|   308| 16808.557| 475.567|  18,324|
| |Lamar County|    12| 629.030| 22.465|   273| 14310.426| 389.399|  19,077|
| |Stephens County|    12| 462.874| 11.021|   611| 23567.985| 352.666|  25,925|
| |Polk County|    11| 258.137| 16.762|   789| 18515.476| 419.054|  42,613|
| |Wilkinson County|    11| 1228.501| 15.955|   211| 23564.887| 526.501|   8,954|
| |Johnson County|    11| 1140.724| 14.815|   240| 24888.520| 281.477|   9,643|
| |Decatur County|    11| 416.604| 16.231|   770| 29162.248| 757.461|  26,404|
| |McDuffie County|    10| 469.219|  6.703|   338| 15859.610| 348.563|  21,312|
| |Macon County|    10| 772.380|  0.000|   177| 13671.121| 33.102|  12,947|
| |Emanuel County|     9| 397.421| 12.617|   501| 22123.112| 580.361|  22,646|
| |Catoosa County|     9| 133.175|  0.000|   631|  9337.082| 194.479|  67,580|
| |Telfair County|     9| 567.465| 18.015|   278| 17528.373| 243.199|  15,860|
| |Screven County|     9| 644.422|  0.000|   195| 13962.480| 235.265|  13,966|
| |Pierce County|     8| 410.994| 14.678|   398| 20446.956| 161.462|  19,465|
| |Laurens County|     8| 168.258| 12.018|   886| 18634.585| 477.733|  47,546|
| |Jeff Davis County|     8| 529.276| 18.903|   436| 28845.518| 661.594|  15,115|
| |Wayne County|     8| 267.317| 19.094|   736| 24593.177| 577.596|  29,927|
| |Bryan County|     8| 201.883|  3.605|   651| 16428.193| 378.530|  39,627|
| |Toombs County|     8| 298.174| 10.649|   741| 27618.338| 633.619|  26,830|
| |Bleckley County|     7| 543.774| 44.390|   184| 14293.482| 610.358|  12,873|
| |Burke County|     7| 312.737|  0.000|   462| 20640.665| 395.708|  22,383|
| |Bacon County|     7| 627.015| 12.796|   433| 38785.382| 294.313|  11,164|
| |Hart County|     7| 267.125| 27.258|   300| 11448.197| 201.706|  26,205|
| |Oglethorpe County|     7| 458.746|  0.000|   214| 14024.510| 280.865|  15,259|
| |Union County|     7| 285.586|  5.828|   260| 10607.482| 320.556|  24,511|
| |Jefferson County|     7| 455.670|  9.299|   485| 31571.410| 585.861|  15,362|
| |Stewart County|     7| 1057.242| 43.153|   255| 38513.820| 172.611|   6,621|
| |Calhoun County|     6| 969.462|  0.000|   203| 32800.129| 230.824|   6,189|
| |Meriwether County|     6| 283.460|  6.749|   384| 18141.447| 249.715|  21,167|
| |Madison County|     6| 200.803|  9.562|   392| 13119.143| 315.548|  29,880|
| |Franklin County|     6| 256.970| 12.237|   396| 16960.041| 256.970|  23,349|
| |Cook County|     6| 347.423|  0.000|   432| 25014.476| 289.519|  17,270|
| |Lumpkin County|     6| 178.518|  0.000|   339| 10086.284| 161.517|  33,610|
| |Haralson County|     6| 201.396|  0.000|   208|  6981.740| 81.518|  29,792|
| |Pickens County|     5| 153.417|  0.000|   369| 11322.144| 407.650|  32,591|
| |Marion County|     5| 598.158| 17.090|   150| 17944.730| 136.722|   8,359|
| |White County|     5| 162.348|  0.000|   353| 11461.783| 250.480|  30,798|
| |Camden County|     5| 91.465|  2.613|   730| 13353.821| 250.874|  54,666|
| |Grady County|     5| 202.980|  0.000|   476| 19323.671| 440.756|  24,633|
| |Brantley County|     5| 261.657|  7.476|   244| 12768.852| 149.518|  19,109|
| |Gilmer County|     4| 127.514|  4.554|   616| 19637.221| 569.261|  31,369|
| |Heard County|     4| 335.486| 11.982|   142| 11909.754| 155.761|  11,923|
| |Lanier County|     4| 383.767|  0.000|   219| 21011.225| 68.530|  10,423|
| |Pike County|     4| 210.948|  0.000|   210| 11074.781| 173.279|  18,962|
| |Banks County|     4| 207.965|  7.427|   270| 14037.642| 215.392|  19,234|
| |Clinch County|     4| 604.412|  0.000|   192| 29011.786| 431.723|   6,618|
| |Seminole County|     4| 494.438| 35.317|   196| 24227.441| 918.241|   8,090|
| |Candler County|     4| 370.268|  0.000|   252| 23326.854| 383.491|  10,803|
| |Lincoln County|     4| 504.987|  0.000|   137| 17295.796| 216.423|   7,921|
| |Wilkes County|     4| 409.123| 14.612|   189| 19331.083| 189.950|   9,777|
| |Fannin County|     3| 114.556|  5.455|   329| 12563.006| 321.849|  26,188|
| |Dodge County|     3| 145.596|  0.000|   210| 10191.701| 152.529|  20,605|
| |Ben Hill County|     3| 179.641|  0.000|   416| 24910.180| 624.465|  16,700|
| |Rabun County|     3| 175.060|  0.000|   215| 12545.953| 208.405|  17,137|
| |Treutlen County|     3| 434.720|  0.000|   118| 17098.971| 455.421|   6,901|
| |Jones County|     3| 104.402|  0.000|   302| 10509.831| 218.748|  28,735|
| |Liberty County|     3| 48.832|  2.325|   713| 11605.762| 276.715|  61,435|
| |Baker County|     3| 987.492|  0.000|    63| 20737.327| 235.117|   3,038|
| |Charlton County|     3| 224.014|  0.000|   417| 31137.993| 426.694|  13,392|
| |Dawson County|     3| 114.907|  0.000|   369| 14133.599| 404.911|  26,108|
| |Talbot County|     3| 484.262|  0.000|   136| 21953.188| 230.601|   6,195|
| |Chattooga County|     3| 121.021|  5.763|   255| 10286.821| 391.879|  24,789|
| |Twiggs County|     3| 369.458|  0.000|   116| 14285.714| 404.645|   8,120|
| |Pulaski County|     2| 179.582|  0.000|   100|  8979.079| 192.409|  11,137|
| |Washington County|     2| 98.164|  0.000|   458| 22479.631| 336.563|  20,374|
| |Taylor County|     2| 249.377|  0.000|    82| 10224.439| 231.564|   8,020|
| |McIntosh County|     2| 139.101|  0.000|   174| 12101.822| 268.267|  14,378|
| |Montgomery County|     2| 218.055| 31.151|   150| 16354.121| 342.658|   9,172|
| |Atkinson County|     2| 244.948|  0.000|   317| 38824.250| 489.896|   8,165|
| |Clay County|     2| 705.716|  0.000|    86| 30345.801| 504.083|   2,834|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724| 164.393|   2,607|
| |Effingham County|     2| 31.106|  2.222|   719| 11182.655| 206.634|  64,296|
| |Murray County|     2| 49.880|  0.000|   589| 14689.745| 220.898|  40,096|
| |Echols County|     2| 499.251|  0.000|   221| 55167.249| 106.982|   4,006|
| |Irwin County|     1| 106.202|  0.000|   166| 17629.567| 197.233|   9,416|
| |Tattnall County|     1| 39.548|  0.000|   494| 19536.502| 491.520|  25,286|
| |Towns County|     1| 83.077|  0.000|   142| 11796.959| 367.913|  12,037|
| |Wheeler County|     1| 127.307|  0.000|    91| 11584.978| 127.307|   7,855|
| |Warren County|     1| 190.331| 27.190|    75| 14274.838| 543.803|   5,254|
| |Evans County|     1| 93.861|  0.000|   249| 23371.504| 522.942|  10,654|
| |Elbert County|     1| 52.100|  0.000|   354| 18443.264| 230.727|  19,194|
| |Jasper County|     1| 70.328|  0.000|   161| 11322.878| 381.783|  14,219|
| |Chattahoochee County|     1| 91.684|  0.000|   759| 69588.338| 1296.677|  10,907|
| |Dade County|     1| 62.050|  0.000|   125|  7756.267| 141.829|  16,116|
| |Long County|     1| 51.127|  0.000|   123|  6288.665|  7.304|  19,559|
| |Quitman County|     1| 434.972|  0.000|    29| 12614.180|  0.000|   2,299|
| |Schley County|     1| 190.223|  0.000|    66| 12554.689| 434.794|   5,257|
| |Morgan County|     0|  0.000|  0.000|   271| 14058.933| 407.613|  19,276|
| |Taliaferro County|     0|  0.000|  0.000|    13|  8458.035| 92.945|   1,537|
| |Crawford County|     0|  0.000|  0.000|   102|  8223.154| 138.204|  12,404|
| |Berrien County|     0|  0.000|  0.000|   289| 14899.211| 220.947|  19,397|
| |Glascock County|     0|  0.000|  0.000|    24|  8078.088| 96.168|   2,971|
| |Miller County|     0|  0.000|  0.000|   142| 24833.858| 299.805|   5,718|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,668| 313.797| N/A|99,969|  8552.327| N/A|11,689,100|
| |Franklin County|   523| 397.188|  1.085|18,182| 13808.177| 133.445|1,316,756|
| |Cuyahoga County|   499| 404.025|  2.776|13,414| 10860.905| 103.638|1,235,072|
| |Lucas County|   323| 754.060|  2.335| 5,288| 12345.103| 175.425| 428,348|
| |Hamilton County|   255| 311.937|  1.573| 9,583| 11722.711| 93.494| 817,473|
| |Mahoning County|   255| 1115.081|  1.249| 2,532| 11072.095| 93.080| 228,683|
| |Summit County|   222| 410.341|  1.320| 3,523|  6511.858| 82.121| 541,013|
| |Stark County|   139| 375.061|  2.698| 1,813|  4891.988| 58.591| 370,606|
| |Trumbull County|   106| 535.424|  2.886| 1,518|  7667.674| 79.376| 197,974|
| |Montgomery County|    94| 176.796|  5.105| 4,318|  8121.319| 93.503| 531,687|
| |Lorain County|    78| 251.749|  0.922| 1,736|  5603.018| 64.551| 309,833|
| |Butler County|    63| 164.433|  1.491| 2,891|  7545.663| 89.115| 383,134|
| |Portage County|    61| 375.463|  0.879|   754|  4640.971| 40.448| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,656| 16253.938| 126.195| 101,883|
| |Wayne County|    58| 501.253|  0.000|   529|  4571.774| 50.619| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,030|  7873.594| 147.425| 130,817|
| |Licking County|    49| 277.052|  6.462| 1,260|  7124.199| 134.084| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   562|  5779.455| 36.728|  97,241|
| |Marion County|    45| 691.319|  2.195| 2,922| 44889.619| 120.706|  65,093|
| |Allen County|    44| 429.893|  2.792|   732|  7151.860| 135.388| 102,351|
| |Geauga County|    44| 469.840|  1.525|   554|  5915.707| 48.814|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,383| 40765.007| 85.533|  58,457|
| |Warren County|    39| 166.239|  2.436| 1,767|  7531.905| 114.480| 234,602|
| |Lake County|    38| 165.110|  2.483| 1,111|  4827.308| 54.002| 230,149|
| |Miami County|    38| 355.183|  2.671|   832|  7776.646| 93.469| 106,987|
| |Medina County|    35| 194.719|  1.590|   914|  5084.953| 73.914| 179,746|
| |Fairfield County|    32| 203.079|  9.066| 1,367|  8675.289| 126.018| 157,574|
| |Darke County|    29| 567.370|  5.590|   393|  7688.846| 223.594|  51,113|
| |Erie County|    27| 363.558|  0.000|   570|  7675.114| 121.186|  74,266|
| |Belmont County|    26| 388.025|  0.000|   621|  9267.827| 68.224|  67,006|
| |Ottawa County|    26| 641.579|  3.525|   377|  9302.899| 109.280|  40,525|
| |Washington County|    22| 367.211|  2.384|   202|  3371.668| 16.691|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,292|  6176.587| 76.490| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    91|  6664.714| 20.925|  13,654|
| |Putnam County|    17| 502.053|  0.000|   205|  6054.163| 54.846|  33,861|
| |Sandusky County|    16| 273.420|  0.000|   373|  6374.107| 131.828|  58,518|
| |Tuscarawas County|    14| 152.195|  1.553|   781|  8490.330| 59.015|  91,987|
| |Clark County|    14| 104.413|  1.065| 1,142|  8517.113| 79.908| 134,083|
| |Mercer County|    13| 315.749|  0.000|   605| 14694.453| 305.339|  41,172|
| |Greene County|    12| 71.032|  0.846|   684|  4048.847| 56.657| 168,937|
| |Hardin County|    12| 382.592|  0.000|   164|  5228.758| 63.765|  31,365|
| |Richland County|    12| 99.047|  2.358|   600|  4952.375| 81.360| 121,154|
| |Clermont County|    11| 53.287|  0.692|   921|  4461.604| 69.204| 206,428|
| |Madison County|    10| 223.559|  0.000|   355|  7936.331| 105.392|  44,731|
| |Hocking County|     9| 318.426|  0.000|   116|  4104.161| 50.544|  28,264|
| |Wyandot County|     8| 367.444| 19.685|   145|  6659.930| 170.599|  21,772|
| |Guernsey County|     7| 180.064|  3.675|   116|  2983.923| 22.049|  38,875|
| |Knox County|     7| 112.320| 11.461|   203|  3257.277| 105.443|  62,322|
| |Holmes County|     6| 136.488|  0.000|   327|  7438.581| 25.998|  43,960|
| |Auglaize County|     6| 131.418|  3.129|   250|  5475.732| 131.418|  45,656|
| |Coshocton County|     6| 163.934|  0.000|   192|  5245.902| 27.322|  36,600|
| |Clinton County|     6| 142.966|  0.000|   162|  3860.084| 61.271|  41,968|
| |Carroll County|     5| 185.777|  0.000|   111|  4124.248| 21.232|  26,914|
| |Crawford County|     5| 120.499|  0.000|   174|  4193.377| 34.428|  41,494|
| |Huron County|     5| 85.813|  2.452|   395|  6779.254| 66.199|  58,266|
| |Ross County|     4| 52.174|  0.000|   468|  6104.401| 162.113|  76,666|
| |Shelby County|     4| 82.321|  0.000|   190|  3910.270| 108.782|  48,590|
| |Defiance County|     4| 105.023|  0.000|   142|  3728.306| 48.761|  38,087|
| |Perry County|     3| 83.024|  3.954|   123|  3403.996| 83.024|  36,134|
| |Hancock County|     3| 39.587|  1.885|   372|  4908.753| 118.760|  75,783|
| |Seneca County|     3| 54.369|  0.000|   204|  3697.126| 147.574|  55,178|
| |Ashland County|     3| 56.092|  0.000|   143|  2673.697| 42.736|  53,484|
| |Williams County|     3| 81.762|  0.000|   134|  3652.022| 54.508|  36,692|
| |Adams County|     2| 72.207|  0.000|    59|  2130.118| 30.946|  27,698|
| |Champaign County|     2| 51.434|  3.674|   173|  4449.016| 260.842|  38,885|
| |Brown County|     2| 46.049|  3.289|   127|  2924.111| 46.049|  43,432|
| |Vinton County|     2| 152.847|  0.000|    31|  2369.125| 10.918|  13,085|
| |Morrow County|     2| 56.612|  0.000|   168|  4755.435| 40.437|  35,328|
| |Logan County|     2| 43.791|  3.128|   152|  3328.078| 112.604|  45,672|
| |Jefferson County|     2| 30.616|  0.000|   224|  3429.009| 45.924|  65,325|
| |Henry County|     2| 74.058|  5.290|   116|  4295.342| 63.478|  27,006|
| |Preble County|     2| 48.921|  0.000|   201|  4916.589| 136.281|  40,882|
| |Union County|     1| 16.953|  0.000|   246|  4170.340| 82.341|  58,988|
| |Van Wert County|     1| 35.367|  0.000|    71|  2511.052| 25.262|  28,275|
| |Scioto County|     1| 13.278|  0.000|   224|  2974.215| 83.460|  75,314|
| |Fulton County|     1| 23.738|  0.000|   147|  3489.531| 30.521|  42,126|
| |Highland County|     1| 23.169|  0.000|   156|  3614.374| 115.845|  43,161|
| |Athens County|     1| 15.308|  0.000|   356|  5449.508| 30.615|  65,327|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 66.489|  15,040|
| |Muskingum County|     1| 11.599|  0.000|   225|  2609.755| 82.849|  86,215|
| |Gallia County|     1| 33.447|  0.000|    65|  2174.058| 33.447|  29,898|
| |Paulding County|     0|  0.000|  0.000|    67|  3588.260| 61.207|  18,672|
| |Meigs County|     0|  0.000|  0.000|    38|  1658.882| 93.546|  22,907|
| |Morgan County|     0|  0.000|  0.000|    25|  1723.187| 68.927|  14,508|
| |Noble County|     0|  0.000|  0.000|    17|  1178.591|  9.904|  14,424|
| |Pike County|     0|  0.000|  0.000|    76|  2736.569| 66.871|  27,772|
| |Lawrence County|     0|  0.000|  0.000|   279|  4691.993| 163.367|  59,463|
| |Jackson County|     0|  0.000|  0.000|    74|  2283.035| 39.667|  32,413|
| |Fayette County|     0|  0.000|  0.000|   112|  3926.380| 105.171|  28,525|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,559| 588.685| N/A|94,581| 15644.394| N/A|6,045,680|
| |Baltimore County|   989| 1195.354|  5.353|25,435| 30741.990| 350.854| 827,370|
| |Montgomery County|   802| 763.309|  1.768|18,260| 17379.089| 80.899|1,050,688|
| |Prince George's County|   751| 825.886|  1.571|23,554| 25902.673| 148.933| 909,327|
| |Anne Arundel County|   222| 383.265|  1.233| 7,295| 12594.219| 108.518| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,055| 11770.508| 36.327| 259,547|
| |Carroll County|   117| 694.580|  0.848| 1,537|  9124.532| 59.366| 168,447|
| |Howard County|   110| 337.744|  1.755| 3,809| 11695.170| 104.832| 325,690|
| |Charles County|    91| 557.403|  0.000| 2,000| 12250.623| 126.881| 163,257|
| |Harford County|    69| 270.121|  1.119| 1,934|  7571.220| 86.126| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   965|  8501.454| 76.771| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,324| 12778.813| 51.016| 103,609|
| |Washington County|    31| 205.231|  0.946| 1,007|  6666.711| 37.831| 151,049|
| |Cecil County|    30| 291.673|  0.000|   698|  6786.252| 94.446| 102,855|
| |Calvert County|    28| 302.621|  0.000|   685|  7403.404| 112.711|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   422|  8376.174| 102.079|  50,381|
| |Kent County|    23| 1184.224|  0.000|   239| 12305.633| 29.422|  19,422|
| |Worcester County|    20| 382.585|  2.733|   682| 13046.140| 270.542|  52,276|
| |Allegany County|    18| 255.624|  0.000|   287|  4075.778| 40.575|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   371| 11619.531| 98.433|  31,929|
| |Talbot County|     4| 107.582|  0.000|   394| 10596.810| 126.793|  37,181|
| |Somerset County|     3| 117.114|  0.000|   134|  5231.106| 72.499|  25,616|
| |Caroline County|     3| 89.804|  0.000|   445| 13320.960| 64.146|  33,406|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    49|  1688.840| 29.542|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,834| 420.961| N/A|73,287| 10886.010| N/A|6,732,219|
| |Marion County|   725| 751.621|  1.037|15,701| 16277.517| 166.319| 964,582|
| |Lake County|   275| 566.435|  1.766| 7,496| 15439.975| 147.714| 485,493|
| |Allen County|   163| 429.740|  2.260| 3,835| 10110.757| 104.704| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,741| 11007.353| 99.352| 158,167|
| |Hendricks County|   108| 634.134|  2.516| 1,871| 10985.785| 117.432| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,723|  8055.951| 117.071| 338,011|
| |Elkhart County|    84| 407.093|  5.539| 4,801| 23267.310| 162.699| 206,341|
| |St. Joseph County|    81| 297.985|  1.051| 3,423| 12592.614| 184.992| 271,826|
| |Madison County|    65| 501.663|  1.103|   943|  7277.975| 121.281| 129,569|
| |Howard County|    65| 787.459|  1.731|   884| 10709.440| 148.838|  82,544|
| |Delaware County|    52| 455.601|  0.000|   714|  6255.750| 107.642| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   780|  9310.209| 90.374|  83,779|
| |Clark County|    47| 397.288|  2.415| 1,202| 10160.437| 169.059| 118,302|
| |Boone County|    46| 678.036|  0.000|   672|  9905.222| 96.862|  67,843|
| |Floyd County|    46| 585.823|  3.639|   772|  9831.640| 194.668|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,294|  7594.387| 125.763| 170,389|
| |Hancock County|    38| 486.132|  1.828|   647|  8277.044| 71.275|  78,168|
| |Greene County|    34| 1065.096|  0.000|   246|  7706.284| 49.227|  31,922|
| |Morgan County|    34| 482.345|  4.053|   467|  6625.147| 111.466|  70,489|
| |Decatur County|    32| 1204.865|  0.000|   335| 12613.427| 134.472|  26,559|
| |Monroe County|    30| 202.114|  0.000|   746|  5025.904| 69.296| 148,431|
| |Warrick County|    30| 476.206|  0.000|   579|  9190.768| 206.356|  62,998|
| |Grant County|    30| 456.142|  2.172|   526|  7997.689| 65.163|  65,769|
| |LaPorte County|    30| 273.005|  1.300|   894|  8135.556| 98.802| 109,888|
| |Noble County|    29| 607.406|  2.992|   663| 13886.562| 116.694|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   496| 10028.711| 115.538|  49,458|
| |Shelby County|    27| 603.635|  3.194|   546| 12206.846| 121.366|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   342|  7538.021| 53.528|  45,370|
| |Orange County|    24| 1221.623|  0.000|   169|  8602.260| 58.173|  19,646|
| |Harrison County|    23| 567.691|  3.526|   327|  8071.085| 158.671|  40,515|
| |Marshall County|    22| 475.593|  0.000|   774| 16732.241| 108.089|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   352|  9181.491| 59.620|  38,338|
| |Daviess County|    20| 599.682|  4.283|   264|  7915.805| 102.803|  33,351|
| |Henry County|    20| 416.910|  5.956|   376|  7837.905| 53.603|  47,972|
| |Franklin County|    14| 615.168| 25.109|   241| 10589.683| 276.198|  22,758|
| |Vanderburgh County|    13| 71.645|  0.787| 1,922| 10592.391| 191.315| 181,451|
| |Dubois County|    12| 280.794|  0.000|   687| 16075.440| 237.338|  42,736|
| |Jennings County|    12| 432.666|  0.000|   224|  8076.438| 82.413|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   847| 10659.988| 59.332|  79,456|
| |Perry County|    12| 626.011|  0.000|   184|  9598.831| 104.335|  19,169|
| |Tippecanoe County|    11| 56.199|  0.000| 1,189|  6074.633| 75.906| 195,732|
| |White County|    10| 414.903|  0.000|   361| 14978.010| 100.762|  24,102|
| |Wayne County|    10| 151.782|  2.168|   368|  5585.575| 119.257|  65,884|
| |LaGrange County|    10| 252.436|  0.000|   557| 14060.686| 64.912|  39,614|
| |Vigo County|    10| 93.425|  0.000|   619|  5782.993| 220.216| 107,038|
| |Newton County|    10| 715.103|  0.000|   118|  8438.215| 91.942|  13,984|
| |Scott County|    10| 418.883|  0.000|   266| 11142.295| 131.649|  23,873|
| |Cass County|     9| 238.796|  0.000| 1,786| 47387.832| 162.988|  37,689|
| |Tipton County|     9| 594.138| 37.723|   137|  9044.098| 330.077|  15,148|
| |Putnam County|     8| 212.902|  0.000|   286|  7611.241| 262.325|  37,576|
| |Fayette County|     7| 303.004|  0.000|   186|  8051.251| 222.615|  23,102|
| |Starke County|     7| 304.414|  0.000|   177|  7697.326| 99.400|  22,995|
| |Ripley County|     7| 247.140|  0.000|   199|  7025.844| 65.568|  28,324|
| |Whitley County|     6| 176.658|  0.000|   151|  4445.884| 29.443|  33,964|
| |Jackson County|     5| 113.043|  3.230|   585| 13226.018| 122.732|  44,231|
| |Clay County|     5| 190.658|  0.000|   116|  4423.260| 119.842|  26,225|
| |Ohio County|     5| 851.064| 24.316|    63| 10723.404| 437.690|   5,875|
| |DeKalb County|     4| 92.007|  0.000|   230|  5290.397| 52.575|  43,475|
| |Rush County|     4| 241.240|  0.000|    76|  4583.559|  0.000|  16,581|
| |Randolph County|     4| 162.173|  0.000|   118|  4784.107| 92.670|  24,665|
| |Gibson County|     4| 118.839|  4.244|   221|  6565.852| 106.106|  33,659|
| |Huntington County|     3| 82.147|  0.000|   122|  3340.635| 15.647|  36,520|
| |Clinton County|     3| 92.595|  0.000|   430| 13272.015| 357.154|  32,399|
| |Wabash County|     3| 96.787|  0.000|   165|  5323.268| 46.089|  30,996|
| |Steuben County|     3| 86.720|  0.000|   207|  5983.697| 49.554|  34,594|
| |Spencer County|     3| 147.951|  0.000|   131|  6460.522| 147.951|  20,277|
| |Fulton County|     2| 100.130|  7.152|   164|  8210.674| 178.804|  19,974|
| |Fountain County|     2| 122.354|  0.000|    73|  4465.924| 96.135|  16,346|
| |Carroll County|     2| 98.731|  0.000|   185|  9132.646| 324.403|  20,257|
| |Blackford County|     2| 170.097|  0.000|    63|  5358.054| 145.797|  11,758|
| |Adams County|     2| 55.902|  0.000|    96|  2683.288| 67.881|  35,777|
| |Miami County|     2| 56.313|  0.000|   269|  7574.051| 52.290|  35,516|
| |Jefferson County|     2| 61.904|  0.000|   160|  4952.334| 53.061|  32,308|
| |Wells County|     2| 70.681|  0.000|   162|  5725.191| 166.606|  28,296|
| |Jasper County|     2| 59.591|  0.000|   234|  6972.171| 148.978|  33,562|
| |Warren County|     1| 120.992|  0.000|    22|  2661.827| 51.854|   8,265|
| |Washington County|     1| 35.668|  0.000|   139|  4957.911| 163.056|  28,036|
| |Pulaski County|     1| 80.952|  0.000|    79|  6395.208| 92.517|  12,353|
| |Brown County|     1| 66.260|  0.000|    73|  4837.000| 37.863|  15,092|
| |Parke County|     1| 59.042|  0.000|    51|  3011.159| 42.173|  16,937|
| |Sullivan County|     1| 48.382|  0.000|   113|  5467.125| 269.555|  20,669|
| |Owen County|     1| 48.079|  0.000|    87|  4182.893| 61.816|  20,799|
| |Vermillion County|     0|  0.000|  0.000|    49|  3161.698| 138.267|  15,498|
| |Union County|     0|  0.000|  0.000|    39|  5528.778| 222.771|   7,054|
| |Switzerland County|     0|  0.000|  0.000|    46|  4278.672| 39.863|  10,751|
| |Jay County|     0|  0.000|  0.000|    91|  4452.926| 69.905|  20,436|
| |Knox County|     0|  0.000|  0.000|   151|  4126.360| 97.596|  36,594|
| |Benton County|     0|  0.000|  0.000|    61|  6973.022| 16.330|   8,748|
| |Martin County|     0|  0.000|  0.000|    43|  4193.077| 13.930|  10,255|
| |Crawford County|     0|  0.000|  0.000|    44|  4159.970| 40.519|  10,577|
| |Pike County|     0|  0.000|  0.000|    53|  4277.989| 138.372|  12,389|
| |Posey County|     0|  0.000|  0.000|   170|  6685.806| 89.893|  25,427|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,322| 272.040| N/A|99,189| 11620.734| N/A|8,535,519|
| |Fairfax County|   536| 467.089|  0.871|16,387| 14280.212| 76.935|1,147,532|
| |Henrico County|   184| 556.197|  0.864| 3,839| 11604.568| 102.776| 330,818|
| |Prince William County|   176| 374.201|  1.215| 9,428| 20045.287| 162.498| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,062| 12928.450| 94.095| 236,842|
| |Loudoun County|   115| 278.088|  1.036| 5,254| 12704.999| 82.908| 413,538|
| |Chesterfield County|    80| 226.756|  2.025| 4,350| 12329.862| 154.680| 352,802|
| |Alexandria city|    60| 376.345|  0.896| 2,949| 18497.378| 123.656| 159,428|
| |Virginia Beach city|    54| 120.007|  2.540| 4,895| 10878.406| 227.632| 449,974|
| |Suffolk city|    50| 542.841|  1.551| 1,258| 13657.880| 308.644|  92,108|
| |Richmond County|    46| 5098.083| 47.498| 3,451| 382467.029| 3119.013|   9,023|
| |Shenandoah County|    44| 1008.804|  6.551|   700| 16049.156| 81.883|  43,616|
| |Chesapeake city|    37| 151.122|  4.668| 2,872| 11730.349| 239.228| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,471| 10799.104| 160.461| 136,215|
| |Hanover County|    32| 296.940|  1.326|   641|  5948.073| 70.258| 107,766|
| |Mecklenburg County|    32| 1046.196|  0.000|   440| 14385.196| 630.520|  30,587|
| |Harrisonburg city|    31| 584.729|  5.389| 1,076| 20295.760| 83.533|  53,016|
| |Norfolk city|    30| 123.588|  2.354| 3,700| 15242.521| 303.085| 242,742|
| |Northampton County|    29| 2476.516| 12.200|   296| 25277.541| 48.798|  11,710|
| |Portsmouth city|    25| 264.836|  1.513| 1,758| 18623.276| 402.551|  94,398|
| |Page County|    24| 1004.100|  0.000|   343| 14350.264| 71.721|  23,902|
| |Galax city|    24| 3781.314| 67.523|   346| 54513.944| 337.617|   6,347|
| |Manassas city|    22| 535.475|  6.954| 1,643| 39990.264| 125.176|  41,085|
| |Colonial Heights city|    21| 1208.981|  0.000|   197| 11341.393| 131.590|  17,370|
| |Rockingham County|    19| 231.854|  3.487|   938| 11446.283| 69.731|  81,948|
| |Petersburg city|    19| 606.138| 27.345|   507| 16174.313| 241.544|  31,346|
| |Roanoke County|    19| 201.728|  1.517| 1,502| 15947.168| 309.418|  94,186|
| |Newport News city|    18| 100.432|  1.594| 1,816| 10132.515| 180.938| 179,225|
| |James City County|    16| 209.087|  0.000|   602|  7866.916| 113.878|  76,523|
| |Albemarle County|    16| 146.346|  5.227|   833|  7619.135| 120.213| 109,330|
| |Accomack County|    16| 495.111|  4.421| 1,095| 33884.144| 79.571|  32,316|
| |Emporia city|    15| 2805.836|  0.000|   174| 32547.699| 240.500|   5,346|
| |Charlottesville city|    15| 317.353|  6.045|   537| 11361.232| 199.479|  47,266|
| |Southampton County|    13| 737.338|  0.000|   264| 14973.626| 226.873|  17,631|
| |Nottoway County|    13| 853.466| 37.515|   182| 11948.529| 75.030|  15,232|
| |Carroll County|    13| 436.373|  0.000|   327| 10976.469| 91.111|  29,791|
| |Culpeper County|    12| 228.115|  0.000|   996| 18933.561| 135.783|  52,605|
| |Greensville County|    11| 970.360| 25.204|   463| 40843.331| 541.889|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   411| 18024.735| 438.558|  22,802|
| |Isle of Wight County|     9| 242.529|  0.000|   383| 10320.946| 200.182|  37,109|
| |Fluvanna County|     9| 330.033|  5.239|   188|  6894.023| 78.579|  27,270|
| |Frederick County|     9| 100.769|  0.000|   680|  7613.673| 30.391|  89,313|
| |Fauquier County|     9| 126.365|  2.006|   614|  8620.932| 84.244|  71,222|
| |Sussex County|     9| 806.524|  0.000|   297| 26615.288| 256.039|  11,159|
| |Stafford County|     8| 52.328|  0.934| 1,366|  8934.996| 100.918| 152,882|
| |Buckingham County|     8| 466.527| 16.662|   605| 35281.082| 91.639|  17,148|
| |Bedford County|     7| 88.611|  1.808|   347|  4392.572| 97.653|  78,997|
| |Botetourt County|     7| 209.462|  0.000|   212|  6343.697| 115.418|  33,419|
| |Danville city|     7| 174.808|  0.000|   395|  9864.149| 288.968|  40,044|
| |Manassas Park city|     7| 400.503|  0.000|   513| 29351.184| 122.603|  17,478|
| |Henry County|     7| 138.458|  2.826|   579| 11452.420| 217.576|  50,557|
| |Goochland County|     7| 294.700|  0.000|   161|  6778.091| 60.143|  23,753|
| |Dinwiddie County|     7| 245.235|  5.005|   217|  7602.298| 95.091|  28,544|
| |Hampton city|     7| 52.041|  2.124| 1,210|  8995.614| 213.473| 134,510|
| |Franklin County|     7| 124.906|  0.000|   346|  6173.941| 178.438|  56,042|
| |Williamsburg city|     6| 401.230|  0.000|   122|  8158.352| 124.190|  14,954|
| |Falls Church city|     6| 410.481|  0.000|    60|  4104.809|  9.773|  14,617|
| |Warren County|     6| 149.388|  0.000|   355|  8838.761| 24.898|  40,164|
| |Grayson County|     5| 321.543|  9.187|   152|  9774.920| 211.300|  15,550|
| |Hopewell city|     5| 221.936|  0.000|   269| 11940.166| 101.457|  22,529|
| |Washington County|     5| 93.041|  2.658|   217|  4037.961| 119.624|  53,740|
| |Lynchburg city|     5| 60.851|  5.216|   591|  7192.581| 262.528|  82,168|
| |Charles City County|     5| 718.081|  0.000|    52|  7468.045| 41.033|   6,963|
| |Caroline County|     5| 162.734|  4.650|   206|  6704.638| 74.393|  30,725|
| |King George County|     4| 149.054|  0.000|   141|  5254.136| 90.497|  26,836|
| |Augusta County|     4| 52.939|  0.000|   275|  3639.588| 45.377|  75,558|
| |Alleghany County|     4| 269.179|  9.614|    62|  4172.275| 57.681|  14,860|
| |York County|     4| 58.582|  2.092|   361|  5287.053| 110.888|  68,280|
| |Winchester city|     4| 142.460|  0.000|   399| 14210.414| 40.703|  28,078|
| |Patrick County|     4| 227.169|  8.113|   154|  8746.025| 348.867|  17,608|
| |Powhatan County|     4| 134.898|  0.000|   144|  4856.333| 105.991|  29,652|
| |Pulaski County|     3| 88.165|  0.000|    88|  2586.182| 58.777|  34,027|
| |Montgomery County|     3| 30.446|  0.000|   301|  3054.752| 37.695|  98,535|
| |Fredericksburg city|     3| 103.320|  4.920|   400| 13776.002| 216.480|  29,036|
| |Scott County|     3| 139.108|  0.000|    90|  4173.236| 245.095|  21,566|
| |Smyth County|     3| 99.655|  0.000|   146|  4849.854| 161.345|  30,104|
| |Westmoreland County|     3| 166.528|  7.930|   209| 11601.443| 126.878|  18,015|
| |Wythe County|     3| 104.588|  0.000|   115|  4009.204| 64.745|  28,684|
| |Wise County|     3| 80.250|  0.000|   126|  3370.516| 160.501|  37,383|
| |Salem city|     3| 118.572|  0.000|   161|  6363.385| 169.389|  25,301|
| |Waynesboro city|     3| 132.567|  0.000|   173|  7644.719| 44.189|  22,630|
| |Martinsville city|     3| 238.968|  0.000|   202| 16090.489| 386.900|  12,554|
| |Orange County|     3| 80.969|  0.000|   231|  6234.650| 80.969|  37,051|
| |Floyd County|     2| 126.992|  9.071|    57|  3619.277| 217.701|  15,749|
| |Russell County|     2| 75.228|  5.373|   112|  4212.744| 279.417|  26,586|
| |Louisa County|     2| 53.204|  0.000|   182|  4841.584| 60.805|  37,591|
| |Amelia County|     2| 152.149| 10.868|    79|  6009.890| 65.207|  13,145|
| |Campbell County|     2| 36.440|  0.000|   206|  3753.302| 148.362|  54,885|
| |Brunswick County|     2| 123.221|  8.801|   227| 13985.583| 202.434|  16,231|
| |Pittsylvania County|     2| 33.138|  0.000|   424|  7025.218| 224.864|  60,354|
| |Surry County|     2| 311.429|  0.000|    49|  7630.022| 266.940|   6,422|
| |Greene County|     2| 100.913|  0.000|   154|  7770.321| 122.538|  19,819|
| |Prince George County|     2| 52.147|  0.000|   380|  9907.960| 178.790|  38,353|
| |King William County|     2| 116.632|  0.000|    87|  5073.478| 83.308|  17,148|
| |Rappahannock County|     2| 271.370|  0.000|    42|  5698.779| 38.767|   7,370|
| |Northumberland County|     2| 165.358|  0.000|    71|  5870.194| 70.868|  12,095|
| |Gloucester County|     2| 53.550|  0.000|   156|  4176.930| 49.725|  37,348|
| |Buena Vista city|     1| 154.369| 22.053|    50|  7718.432| 66.158|   6,478|
| |New Kent County|     1| 43.307|  0.000|   127|  5499.978| 68.054|  23,091|
| |King and Queen County|     1| 142.349|  0.000|    39|  5551.601| 81.342|   7,025|
| |Lee County|     1| 42.693|  0.000|   114|  4867.011| 115.881|  23,423|
| |Essex County|     1| 91.299|  0.000|    99|  9038.620| 299.983|  10,953|
| |Dickenson County|     1| 69.842|  9.977|    40|  2793.686| 169.617|  14,318|
| |Rockbridge County|     1| 44.301|  6.329|    67|  2968.148|  6.329|  22,573|
| |Halifax County|     1| 29.489|  0.000|   153|  4511.810| 75.829|  33,911|
| |Middlesex County|     1| 94.500|  0.000|    37|  3496.503| 135.000|  10,582|
| |Madison County|     1| 75.409|  0.000|    68|  5127.818| 75.409|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    62|  5083.634| 81.994|  12,196|
| |Poquoson city|     0|  0.000|  0.000|    43|  3504.197| 81.493|  12,271|
| |Radford city|     0|  0.000|  0.000|    51|  2794.674| 195.705|  18,249|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Bland County|     0|  0.000|  0.000|    11|  1751.592| 90.992|   6,280|
| |Buchanan County|     0|  0.000|  0.000|    77|  3665.968| 40.809|  21,004|
| |Cumberland County|     0|  0.000|  0.000|    76|  7652.034| 158.219|   9,932|
| |Charlotte County|     0|  0.000|  0.000|    53|  4461.279| 48.100|  11,880|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Giles County|     0|  0.000|  0.000|    23|  1375.598|  0.000|  16,720|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Nelson County|     0|  0.000|  0.000|    45|  3014.066| 124.390|  14,930|
| |Bristol city|     0|  0.000|  0.000|    77|  4593.724| 153.408|  16,762|
| |Tazewell County|     0|  0.000|  0.000|   117|  2882.128| 87.977|  40,595|
| |Clarke County|     0|  0.000|  0.000|    71|  4856.693| 19.544|  14,619|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 27.842|   5,131|
| |Mathews County|     0|  0.000|  0.000|    18|  2037.582| 80.856|   8,834|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Staunton city|     0|  0.000|  0.000|   151|  6056.474| 57.299|  24,932|
| |Amherst County|     0|  0.000|  0.000|   165|  5220.693| 257.645|  31,605|
| |Appomattox County|     0|  0.000|  0.000|    84|  5279.366| 143.656|  15,911|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910| 76.743|   7,446|
| |Lancaster County|     0|  0.000|  0.000|    36|  3395.265| 67.366|  10,603|
| |Norton city|     0|  0.000|  0.000|    18|  4521.477| 179.424|   3,981|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 195.695|   2,190|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,184| 208.236| N/A|134,948| 12866.792| N/A|10,488,084|
| |Mecklenburg County|   226| 203.538|  2.059|22,066| 19872.906| 178.450|1,110,356|
| |Wake County|   168| 151.112|  4.626|11,906| 10709.136| 120.401|1,111,761|
| |Guilford County|   156| 290.409|  2.393| 5,580| 10387.696| 109.834| 537,174|
| |Durham County|    80| 248.843|  1.333| 6,114| 19017.817| 126.199| 321,488|
| |Henderson County|    54| 459.899|  1.217| 1,472| 12536.515| 138.700| 117,417|
| |Robeson County|    53| 405.742|  2.187| 2,784| 21312.919| 194.668| 130,625|
| |Chatham County|    52| 698.268|  3.837| 1,295| 17389.553| 143.874|  74,470|
| |Forsyth County|    52| 136.021|  1.121| 5,213| 13636.066| 123.315| 382,295|
| |Gaston County|    51| 227.142|  8.908| 3,299| 14692.980| 194.057| 224,529|
| |Cumberland County|    51| 152.008|  0.426| 3,042|  9066.821| 148.176| 335,509|
| |Cabarrus County|    50| 230.997|  3.300| 2,603| 12025.705| 150.478| 216,453|
| |Columbus County|    48| 864.740|  5.147|   896| 16141.817| 193.022|  55,508|
| |Rowan County|    48| 337.819|  0.000| 2,173| 15293.339| 188.012| 142,088|
| |Duplin County|    48| 817.146| 14.592| 2,006| 34149.912| 199.423|  58,741|
| |Orange County|    47| 316.549|  1.924| 1,341|  9031.763| 60.616| 148,476|
| |Buncombe County|    47| 179.945|  0.547| 1,850|  7082.939| 105.560| 261,191|
| |Johnston County|    46| 219.739|  1.365| 3,275| 15644.481| 187.666| 209,339|
| |Wayne County|    42| 341.100|  5.801| 2,401| 19499.557| 118.341| 123,131|
| |Union County|    42| 175.103|  1.787| 3,072| 12807.524| 184.632| 239,859|
| |Alamance County|    41| 241.875|  0.000| 2,396| 14134.943| 174.453| 169,509|
| |Vance County|    40| 898.170|  0.000|   765| 17177.501| 121.894|  44,535|
| |Harnett County|    39| 286.815|  3.152| 1,260|  9266.341| 143.933| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,170| 15104.373| 120.318| 143,667|
| |Wilson County|    35| 427.868|  1.746| 1,476| 18043.789| 164.161|  81,801|
| |Catawba County|    29| 181.760|  4.477| 2,107| 13205.809| 200.563| 159,551|
| |Burke County|    28| 309.444|  3.158| 1,643| 18157.706| 146.828|  90,485|
| |Granville County|    27| 446.702|  4.727| 1,231| 20366.296| 158.355|  60,443|
| |Franklin County|    26| 373.108|  2.050|   860| 12341.250| 176.304|  69,685|
| |Stanly County|    26| 413.973| 34.119| 1,049| 16702.226| 375.305|  62,806|
| |Brunswick County|    21| 147.038|  5.001| 1,240|  8682.257| 66.017| 142,820|
| |Pasquotank County|    20| 502.210| 10.762|   395|  9918.642| 157.837|  39,824|
| |Moore County|    20| 198.255|  0.000| 1,005|  9962.331| 165.685| 100,880|
| |New Hanover County|    20| 85.298|  0.609| 2,566| 10943.691| 148.662| 234,473|
| |Cleveland County|    20| 204.192|  8.751| 1,167| 11914.607| 245.030|  97,947|
| |Davidson County|    18| 107.393|  0.852| 1,758| 10488.697| 104.836| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,805|  9928.165| 106.079| 181,806|
| |Northampton County|    16| 821.229|  0.000|   349| 17913.052| 307.961|  19,483|
| |Caldwell County|    14| 170.362|  3.477| 1,209| 14711.967| 184.269|  82,178|
| |Sampson County|    14| 220.365|  4.497| 1,500| 23610.521| 186.636|  63,531|
| |McDowell County|    14| 305.971| 15.611|   675| 14752.164| 249.772|  45,756|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 310.182|  27,173|
| |Rutherford County|    14| 208.865|  2.131|   712| 10622.268| 157.714|  67,029|
| |Edgecombe County|    13| 252.565|  5.551|   632| 12278.520| 160.975|  51,472|
| |Lenoir County|    12| 214.481|  0.000|   568| 10152.103| 94.474|  55,949|
| |Haywood County|    12| 192.564| 13.755|   421|  6755.781| 288.846|  62,317|
| |Craven County|    12| 117.487|  2.797|   697|  6824.034| 99.304| 102,139|
| |Nash County|    12| 127.256|  1.515| 1,158| 12280.218| 218.153|  94,298|
| |Wilkes County|    11| 160.791|  2.088|   792| 11576.916| 131.556|  68,412|
| |Pitt County|    11| 60.860|  0.000| 1,962| 10855.252| 176.258| 180,742|
| |Lee County|    11| 178.054|  2.312| 1,281| 20735.201| 238.176|  61,779|
| |Hertford County|    11| 464.586|  0.000|   334| 14106.517| 343.914|  23,677|
| |Onslow County|    10| 50.521|  0.000| 1,047|  5289.535| 93.824| 197,938|
| |Hoke County|     9| 162.943|  2.586|   713| 12908.716| 121.561|  55,234|
| |Lincoln County|     9| 104.516|  9.954|   840|  9754.851| 184.148|  86,111|
| |Richmond County|     9| 200.763|  3.187|   505| 11265.029| 86.041|  44,829|
| |Surry County|     9| 125.378|  3.980|   928| 12927.852| 135.328|  71,783|
| |Rockingham County|     8| 87.902|  1.570|   543|  5966.377| 128.714|  91,010|
| |Warren County|     7| 354.772|  7.240|   256| 12974.507| 123.084|  19,731|
| |Bladen County|     7| 213.923|  0.000|   623| 19039.179| 200.826|  32,722|
| |Carteret County|     6| 86.364|  2.056|   339|  4879.594| 108.984|  69,473|
| |Halifax County|     6| 119.976|  0.000|   698| 13957.209| 217.099|  50,010|
| |Davie County|     6| 140.036|  6.668|   414|  9662.512| 176.713|  42,846|
| |Martin County|     6| 267.380|  0.000|   258| 11497.326| 120.957|  22,440|
| |Yadkin County|     6| 159.291|  0.000|   532| 14123.769| 174.461|  37,667|
| |Bertie County|     5| 263.894|  0.000|   269| 14197.498| 180.956|  18,947|
| |Jackson County|     5| 113.797|  6.503|   444| 10105.148| 159.315|  43,938|
| |Polk County|     5| 241.266|  0.000|   161|  7768.771| 172.333|  20,724|
| |Jones County|     4| 424.674| 15.167|    82|  8705.807| 364.006|   9,419|
| |Washington County|     4| 345.423| 12.337|   132| 11398.964| 172.712|  11,580|
| |Cherokee County|     4| 139.801|  4.993|   269|  9401.650| 169.759|  28,612|
| |Stokes County|     3| 65.802|  0.000|   291|  6382.839| 109.671|  45,591|
| |Macon County|     3| 83.663|  3.984|   460| 12828.379| 59.760|  35,858|
| |Pender County|     3| 47.574|  0.000|   654| 10371.075| 95.147|  63,060|
| |Greene County|     3| 142.389|  0.000|   326| 15472.970| 142.389|  21,069|
| |Anson County|     3| 122.719|  5.844|   327| 13376.422| 151.938|  24,446|
| |Mitchell County|     2| 133.654|  0.000|   116|  7751.938| 76.374|  14,964|
| |Gates County|     2| 172.980|  0.000|    46|  3978.550| 37.067|  11,562|
| |Scotland County|     2| 57.433|  0.000|   339|  9734.945| 270.757|  34,823|
| |Person County|     2| 50.646|  0.000|   208|  5267.156| 61.498|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    85|  6313.600| 212.222|  13,463|
| |Alexander County|     2| 53.338|  0.000|   295|  7867.296|  0.000|  37,497|
| |Swain County|     2| 140.144|  0.000|   119|  8338.589| 160.165|  14,271|
| |Beaufort County|     2| 42.559|  0.000|   406|  8639.401| 203.673|  46,994|
| |Camden County|     2| 184.043|  0.000|    69|  6349.498| 92.022|  10,867|
| |Caswell County|     2| 88.480|  0.000|   193|  8538.312| 63.200|  22,604|
| |Dare County|     2| 54.041|  3.860|   209|  5647.275| 42.461|  37,009|
| |Pamlico County|     1| 78.579|  0.000|    67|  5264.812| 112.256|  12,726|
| |Transylvania County|     1| 29.082|  0.000|   135|  3926.131| 54.010|  34,385|
| |Tyrrell County|     1| 249.004|  0.000|    98| 24402.390| 249.004|   4,016|
| |Ashe County|     1| 36.761|  0.000|   157|  5771.422| 199.558|  27,203|
| |Chowan County|     1| 71.721|  0.000|   155| 11116.689| 297.128|  13,943|
| |Avery County|     0|  0.000|  0.000|    99|  5638.777| 138.325|  17,557|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984| 139.919|  11,231|
| |Currituck County|     0|  0.000|  0.000|    73|  2629.399| 15.437|  27,763|
| |Alleghany County|     0|  0.000|  0.000|   167| 14995.062| 1282.726|  11,137|
| |Madison County|     0|  0.000|  0.000|    45|  2068.490| 45.966|  21,755|
| |Graham County|     0|  0.000|  0.000|    35|  4146.428| 152.318|   8,441|
| |Hyde County|     0|  0.000|  0.000|    42|  8507.191| 144.680|   4,937|
| |Watauga County|     0|  0.000|  0.000|   287|  5108.852| 91.547|  56,177|
| |Yancey County|     0|  0.000|  0.000|   101|  5589.684| 55.343|  18,069|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,007| 389.806| N/A|99,460| 19317.445| N/A|5,148,714|
| |Greenville County|   206| 393.474|  5.184|10,819| 20665.009| 185.549| 523,542|
| |Charleston County|   194| 471.554| 10.070|12,213| 29686.004| 257.653| 411,406|
| |Horry County|   151| 426.456|  8.876| 8,555| 24161.138| 203.747| 354,081|
| |Richland County|   151| 363.191|  6.185| 8,707| 20942.421| 288.972| 415,759|
| |Florence County|   112| 809.875| 16.528| 3,371| 24375.782| 447.290| 138,293|
| |Lexington County|   110| 368.201|  4.304| 4,923| 16478.661| 164.017| 298,750|
| |Spartanburg County|   101| 315.837|  8.488| 4,057| 12686.649| 159.482| 319,785|
| |Berkeley County|    66| 289.592|  5.015| 4,133| 18134.590| 197.449| 227,907|
| |Orangeburg County|    64| 742.675| 11.604| 2,383| 27653.032| 382.942|  86,175|
| |Anderson County|    62| 306.085| 11.284| 2,321| 11458.446| 184.780| 202,558|
| |Beaufort County|    55| 286.276|  5.205| 4,046| 21059.535| 348.737| 192,122|
| |Clarendon County|    51| 1511.335|  4.233|   836| 24774.041| 249.772|  33,745|
| |Sumter County|    50| 468.511|  6.693| 2,515| 23566.121| 302.524| 106,721|
| |Dorchester County|    47| 288.682|  7.020| 3,070| 18856.451| 286.049| 162,809|
| |Laurens County|    44| 651.919| 21.166| 1,311| 19424.237| 222.245|  67,493|
| |Aiken County|    37| 216.536|  9.197| 1,843| 10785.851| 254.995| 170,872|
| |Darlington County|    35| 525.384|  4.289| 1,261| 18928.818| 433.173|  66,618|
| |Colleton County|    34| 902.407| 11.375|   807| 21418.903| 208.540|  37,677|
| |Williamsburg County|    31| 1020.811| 18.817|   993| 32698.894| 432.786|  30,368|
| |York County|    29| 103.211|  0.508| 3,531| 12566.775| 201.845| 280,979|
| |Cherokee County|    28| 488.656|  7.479|   630| 10994.764| 206.931|  57,300|
| |Lee County|    27| 1604.469|  0.000|   561| 33337.295| 407.484|  16,828|
| |Pickens County|    27| 212.793|  4.504| 1,841| 14509.316| 149.743| 126,884|
| |Dillon County|    24| 787.427|  4.687|   634| 20801.207| 384.340|  30,479|
| |Kershaw County|    24| 360.626|  2.147| 1,390| 20886.238| 264.030|  66,551|
| |Fairfield County|    23| 1029.221|  0.000|   564| 25238.287| 210.958|  22,347|
| |Lancaster County|    23| 234.665|  2.915| 1,181| 12049.545| 206.972|  98,012|
| |Bamberg County|    22| 1564.055| 60.937|   468| 33271.719| 345.311|  14,066|
| |Chesterfield County|    21| 460.022|  6.259|   758| 16604.600| 222.187|  45,650|
| |Georgetown County|    20| 319.081|  2.279| 1,446| 23069.560| 389.735|  62,680|
| |Greenwood County|    18| 254.198|  6.052| 1,375| 19417.887| 278.407|  70,811|
| |Jasper County|    15| 498.786|  9.501|   578| 19219.898| 370.527|  30,073|
| |Chester County|    14| 434.189| 13.292|   654| 20282.843| 460.772|  32,244|
| |Marion County|    13| 424.047|  4.660|   549| 17907.819| 167.755|  30,657|
| |Calhoun County|    10| 687.144|  9.816|   374| 25699.169| 638.062|  14,553|
| |Newberry County|     9| 234.131|  3.716|   841| 21878.252| 301.026|  38,440|
| |Oconee County|     9| 113.142|  3.592|   815| 10245.644| 138.285|  79,546|
| |Hampton County|     9| 468.214| 14.864|   421| 21901.987| 564.829|  19,222|
| |Saluda County|     8| 390.759|  6.978|   452| 22077.859| 307.025|  20,473|
| |Abbeville County|     8| 326.171|  5.824|   325| 13250.703| 215.506|  24,527|
| |Edgefield County|     7| 256.787|  5.241|   318| 11665.444| 214.862|  27,260|
| |Barnwell County|     5| 239.624|  6.846|   409| 19601.265| 554.559|  20,866|
| |Union County|     4| 146.434| 10.460|   360| 13179.089| 146.434|  27,316|
| |Marlboro County|     4| 153.151|  0.000|   489| 18722.720| 328.181|  26,118|
| |Allendale County|     3| 345.304|  0.000|   216| 24861.878| 608.393|   8,688|
| |McCormick County|     2| 211.349|  0.000|   116| 12258.269| 196.253|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,874| 629.673| N/A|66,646| 22393.368| N/A|2,976,149|
| |Hinds County|   118| 508.972|  7.394| 5,599| 24150.276| 260.648| 231,840|
| |Neshoba County|    92| 3159.558| 24.531| 1,285| 44130.778| 466.084|  29,118|
| |Lauderdale County|    92| 1241.147|  7.709| 1,407| 18981.450| 165.743|  74,125|
| |Madison County|    64| 602.228| 14.787| 2,414| 22715.297| 190.885| 106,272|
| |Leflore County|    62| 2199.908| 15.207|   925| 32821.204| 496.753|  28,183|
| |Jones County|    58| 851.714|  2.098| 1,885| 27680.695| 304.183|  68,098|
| |Forrest County|    56| 747.693|  9.537| 1,778| 23739.269| 310.903|  74,897|
| |Monroe County|    53| 1503.461| 12.157|   778| 22069.670| 368.773|  35,252|
| |Holmes County|    48| 2821.869| 16.797|   890| 52322.163| 461.913|  17,010|
| |Jackson County|    42| 292.444|  7.958| 2,269| 15798.965| 392.910| 143,617|
| |Lincoln County|    41| 1200.480|  8.366|   809| 23687.524| 309.531|  34,153|
| |Washington County|    41| 933.749| 29.281| 1,646| 37486.620| 614.908|  43,909|
| |Lee County|    39| 456.482| 15.049| 1,428| 16714.266| 391.270|  85,436|
| |Oktibbeha County|    38| 766.330| 11.524| 1,118| 22546.232| 213.190|  49,587|
| |Pearl River County|    38| 684.253|  5.145|   540|  9723.598| 154.343|  55,535|
| |Lowndes County|    37| 631.453| 17.066| 1,074| 18329.209| 282.813|  58,595|
| |Harrison County|    36| 173.010|  2.746| 2,498| 12004.998| 295.903| 208,080|
| |Pike County|    36| 916.310| 14.545|   928| 23620.444| 396.341|  39,288|
| |Bolivar County|    34| 1110.095|  9.329| 1,108| 36176.048| 816.247|  30,628|
| |Rankin County|    33| 212.532|  4.600| 2,276| 14658.243| 151.808| 155,271|
| |Warren County|    32| 705.141| 22.036| 1,089| 23996.827| 393.494|  45,381|
| |DeSoto County|    30| 162.210|  2.317| 3,632| 19638.271| 322.103| 184,945|
| |Simpson County|    30| 1125.366| 21.436|   795| 29822.192| 471.582|  26,658|
| |Copiah County|    28| 997.684| 25.451|   950| 33849.991| 239.241|  28,065|
| |Tate County|    28| 988.666| 30.265|   720| 25422.831| 413.625|  28,321|
| |Sunflower County|    25| 995.619| 17.068| 1,024| 40780.566| 688.400|  25,110|
| |Attala County|    25| 1375.592|  7.861|   521| 28667.327| 204.374|  18,174|
| |Clarke County|    25| 1608.648|  0.000|   326| 20976.771| 266.576|  15,541|
| |Leake County|    25| 1097.165|  0.000|   786| 34494.865| 150.468|  22,786|
| |Adams County|    25| 814.518|  0.000|   617| 20102.303| 181.521|  30,693|
| |Wayne County|    21| 1040.480|  0.000|   764| 37853.639| 233.577|  20,183|
| |Grenada County|    21| 1011.658|  6.882|   843| 40610.849| 261.517|  20,758|
| |Scott County|    20| 711.136| 15.239|   998| 35485.706| 238.739|  28,124|
| |Marion County|    20| 813.901| 11.627|   657| 26736.662| 366.256|  24,573|
| |Chickasaw County|    20| 1169.385|  8.353|   459| 26837.397| 267.288|  17,103|
| |Walthall County|    19| 1329.973| 10.000|   498| 34859.303| 589.988|  14,286|
| |Winston County|    16| 891.117|  7.956|   620| 34530.771| 429.646|  17,955|
| |Lafayette County|    16| 296.192| 18.512|   964| 17845.573| 272.391|  54,019|
| |Union County|    16| 555.266| 14.873|   627| 21759.500| 565.182|  28,815|
| |Hancock County|    14| 293.920|  0.000|   388|  8145.784| 191.948|  47,632|
| |Kemper County|    14| 1437.077|  0.000|   232| 23814.412| 131.976|   9,742|
| |Lamar County|    14| 221.019|  4.511| 1,202| 18976.051| 218.764|  63,343|
| |Covington County|    13| 697.575| 15.331|   612| 32839.665| 275.964|  18,636|
| |Claiborne County|    13| 1446.373|  0.000|   404| 44948.821| 79.471|   8,988|
| |Clay County|    13| 673.017|  0.000|   394| 20397.598| 221.874|  19,316|
| |Wilkinson County|    13| 1506.373| 16.554|   205| 23754.345| 364.178|   8,630|
| |Smith County|    13| 816.788|  0.000|   404| 25383.262| 269.271|  15,916|
| |Tippah County|    13| 590.506|  6.489|   360| 16352.487| 428.279|  22,015|
| |Panola County|    12| 350.959|  4.178| 1,054| 30825.924| 660.138|  34,192|
| |Webster County|    12| 1238.518|  0.000|   228| 23531.840| 486.561|   9,689|
| |Yazoo County|    12| 404.176|  4.812|   829| 27921.859| 312.756|  29,690|
| |Coahoma County|    12| 542.397| 12.914|   743| 33583.439| 613.426|  22,124|
| |Noxubee County|    11| 1055.966| 13.714|   453| 43486.608| 534.840|  10,417|
| |Carroll County|    11| 1105.861|  0.000|   261| 26239.067| 229.789|   9,947|
| |Greene County|    11| 809.657|  0.000|   241| 17738.849| 157.725|  13,586|
| |Humphreys County|    11| 1364.087|  0.000|   291| 36086.310| 460.601|   8,064|
| |Newton County|    11| 523.361|  0.000|   542| 25787.420| 190.313|  21,018|
| |Itawamba County|    10| 427.533|  0.000|   358| 15305.686| 317.596|  23,390|
| |Prentiss County|    10| 397.994| 22.743|   417| 16596.354| 488.964|  25,126|
| |Yalobusha County|    10| 825.900|  0.000|   313| 25850.677| 11.799|  12,108|
| |Tallahatchie County|    10| 724.165|  0.000|   530| 38380.766| 868.998|  13,809|
| |Calhoun County|     9| 626.697|  9.948|   417| 29036.975| 437.693|  14,361|
| |Jasper County|     9| 549.350|  8.720|   387| 23622.047| 122.078|  16,383|
| |Marshall County|     9| 255.001|  4.048|   688| 19493.398| 534.287|  35,294|
| |Pontotoc County|     8| 248.648|  4.440|   821| 25517.499| 466.215|  32,174|
| |Perry County|     7| 584.649|  0.000|   232| 19376.931| 226.701|  11,973|
| |Lawrence County|     7| 556.174| 22.701|   319| 25345.622| 136.206|  12,586|
| |Jefferson County|     7| 1001.431| 20.437|   195| 27896.996| 81.749|   6,990|
| |Tunica County|     7| 726.744| 14.832|   333| 34572.259| 1201.353|   9,632|
| |Jefferson Davis County|     6| 539.180|  0.000|   231| 20758.447| 449.317|  11,128|
| |Amite County|     6| 487.924| 11.617|   230| 18703.749| 302.048|  12,297|
| |George County|     5| 204.082|  0.000|   559| 22816.327| 116.618|  24,500|
| |Sharkey County|     5| 1157.140| 132.245|   197| 45591.298| 562.039|   4,321|
| |Alcorn County|     5| 135.307|  3.866|   419| 11338.728| 270.614|  36,953|
| |Tishomingo County|     5| 257.958| 14.740|   409| 21100.965| 759.134|  19,383|
| |Choctaw County|     4| 487.211|  0.000|   133| 16199.756| 139.203|   8,210|
| |Stone County|     4| 218.150|  7.791|   194| 10580.279| 373.972|  18,336|
| |Montgomery County|     3| 306.905|  0.000|   321| 32838.875| 438.436|   9,775|
| |Franklin County|     2| 259.302|  0.000|   124| 16076.754| 240.781|   7,713|
| |Quitman County|     1| 147.232|  0.000|   262| 38574.794| 883.392|   6,792|
| |Issaquena County|     1| 753.580|  0.000|    26| 19593.067| 538.271|   1,327|
| |Benton County|     1| 121.080| 17.297|   143| 17314.445| 328.646|   8,259|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,857| 322.467| N/A|50,306|  8735.598| N/A|5,758,736|
| |Denver County|   414| 569.298| N/A|10,173| 13989.062| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.218| 7,286| 11096.727| 77.021| 656,590|
| |Jefferson County|   228| 391.160|  0.245| 4,160|  7136.963| 60.047| 582,881|
| |Adams County|   176| 340.149|  1.380| 6,438| 12442.479| 115.960| 517,421|
| |Weld County|   142| 437.607|  0.440| 3,696| 11390.111| 75.283| 324,492|
| |El Paso County|   137| 190.171|  0.397| 4,958|  6882.259| 82.692| 720,403|
| |Boulder County|    75| 229.923|  0.000| 2,026|  6210.990| 59.561| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,726|  4915.222| 41.496| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   684| 23531.031| 39.317|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,531|  4289.729| 62.042| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   687|  4078.991| 64.463| 168,424|
| |Broomfield County|    32| 454.126| N/A|   460|  6528.064| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   302| 14835.921| 112.287|  20,356|
| |Montrose County|    13| 304.037|  0.000|   297|  6946.069| 63.480|  42,758|
| |Alamosa County|     9| 554.426|  0.000|   227| 13983.860| 26.401|  16,233|
| |Eagle County|     9| 163.259|  0.000| 1,120| 20316.723| 204.722|  55,127|
| |Routt County|     7| 273.032|  5.572|   122|  4758.562| 89.153|  25,638|
| |Gunnison County|     6| 343.603|  0.000|   269| 15404.879| 188.164|  17,462|
| |Otero County|     6| 328.263|  0.000|    71|  3884.451| 132.869|  18,278|
| |Logan County|     5| 223.125|  0.000|   651| 29050.828| 25.500|  22,409|
| |Garfield County|     4| 66.599|  0.000|   764| 12720.401| 140.334|  60,061|
| |Mesa County|     4| 25.939|  0.926|   301|  1951.884| 37.982| 154,210|
| |Montezuma County|     4| 152.771|  0.000|   112|  4277.585| 21.824|  26,183|
| |Summit County|     4| 128.986|  0.000|   327| 10544.645| 23.033|  31,011|
| |Teller County|     3| 118.166|  0.000|   123|  4844.809| 61.897|  25,388|
| |Kit Carson County|     3| 422.714|  0.000|    51|  7186.135| 161.034|   7,097|
| |Rio Grande County|     2| 177.510|  0.000|    89|  7899.175| 25.359|  11,267|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |La Plata County|     2| 35.574|  0.000|   207|  3681.898| 22.869|  56,221|
| |Pitkin County|     2| 112.568|  0.000|   187| 10525.131| 152.771|  17,767|
| |Elbert County|     2| 74.825|  0.000|   104|  3890.905| 101.548|  26,729|
| |Moffat County|     1| 75.284|  0.000|    27|  2032.673| 21.510|  13,283|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 44.183|   9,700|
| |Delta County|     1| 32.090|  0.000|   121|  3882.934| 73.349|  31,162|
| |Crowley County|     1| 164.989|  0.000|    72| 11879.228|  0.000|   6,061|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 41.426|   6,897|
| |Grand County|     1| 63.557|  0.000|    46|  2923.605| 27.239|  15,734|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  7.581|  18,845|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Washington County|     0|  0.000|  0.000|    47|  9576.202|  0.000|   4,908|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Gilpin County|     0|  0.000|  0.000|    16|  2562.870|  0.000|   6,243|
| |San Miguel County|     0|  0.000|  0.000|    88| 10759.262| 209.596|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053| 14.259|  10,019|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 50.117|   5,701|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Las Animas County|     0|  0.000|  0.000|    17|  1171.929| 19.696|  14,506|
| |Prowers County|     0|  0.000|  0.000|    52|  4272.100| 46.946|  12,172|
| |Rio Blanco County|     0|  0.000|  0.000|    16|  2530.044| 203.307|   6,324|
| |Lake County|     0|  0.000|  0.000|    77|  9474.591| 123.047|   8,127|
| |Costilla County|     0|  0.000|  0.000|    22|  5659.892|  0.000|   3,887|
| |Fremont County|     0|  0.000|  0.000|   123|  2571.124| 38.821|  47,839|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481| 28.188|   5,068|
| |Cheyenne County|     0|  0.000|  0.000|     8|  4369.197|  0.000|   1,831|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 102.462|   5,577|
| |Baca County|     0|  0.000|  0.000|    14|  3909.522|  0.000|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    35|  2494.832| 20.366|  14,029|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,694| 345.490| N/A|96,613| 19704.131| N/A|4,903,185|
| |Jefferson County|   243| 368.980|  3.905|12,969| 19692.578| 326.247| 658,573|
| |Mobile County|   206| 498.536|  6.223| 9,836| 23803.877| 473.644| 413,210|
| |Montgomery County|   148| 653.462|  4.415| 6,609| 29180.612| 325.470| 226,486|
| |Tallapoosa County|    79| 1957.044|  3.539|   854| 21155.895| 187.565|  40,367|
| |Tuscaloosa County|    73| 348.690|  8.188| 4,190| 20013.852| 231.323| 209,355|
| |Walker County|    64| 1007.541|  2.249| 1,520| 23929.094| 157.428|  63,521|
| |Lee County|    45| 273.486|  4.341| 2,660| 16166.085| 177.983| 164,542|
| |Elmore County|    38| 467.928|  1.759| 1,715| 21118.349| 269.147|  81,209|
| |Chambers County|    38| 1142.720|  0.000|   840| 25260.119| 141.766|  33,254|
| |Butler County|    36| 1851.090|  7.346|   758| 38975.730| 110.184|  19,448|
| |Marshall County|    35| 361.667|  7.381| 3,130| 32343.398| 372.001|  96,774|
| |Shelby County|    35| 160.770|  2.625| 3,260| 14974.598| 200.799| 217,702|
| |Madison County|    33| 88.493|  3.065| 5,314| 14250.125| 190.395| 372,909|
| |Etowah County|    31| 303.125|  9.778| 2,104| 20573.395| 307.316| 102,268|
| |Hale County|    26| 1774.623|  9.751|   473| 32284.486| 243.767|  14,651|
| |Marion County|    24| 807.836|  0.000|   570| 19186.105| 201.959|  29,709|
| |Lowndes County|    24| 2467.613|  0.000|   571| 58708.616| 381.892|   9,726|
| |Baldwin County|    24| 107.511|  1.920| 3,502| 15687.574| 260.457| 223,234|
| |Dale County|    23| 467.746| 14.526|   827| 16818.515| 185.936|  49,172|
| |Dallas County|    23| 618.346|  0.000| 1,318| 35433.918| 203.555|  37,196|
| |Autauga County|    21| 375.879|  2.557| 1,086| 19438.329| 250.586|  55,869|
| |Covington County|    20| 539.826|  0.000|   734| 19811.601| 192.795|  37,049|
| |Franklin County|    20| 637.714|  0.000| 1,270| 40494.866| 478.286|  31,362|
| |Morgan County|    18| 150.402|  4.775| 2,369| 19794.617| 254.252| 119,679|
| |Sumter County|    18| 1448.459|  0.000|   360| 28969.180|  0.000|  12,427|
| |Lauderdale County|    17| 183.330|  7.703| 1,157| 12477.219| 198.736|  92,729|
| |St. Clair County|    17| 189.919|  9.576| 1,328| 14836.000| 253.757|  89,512|
| |Escambia County|    16| 436.765|  3.900| 1,075| 29345.126| 479.661|  36,633|
| |Marengo County|    15| 795.208|  7.573|   553| 29316.652| 355.950|  18,863|
| |Macon County|    14| 774.851| 15.813|   334| 18485.721| 237.199|  18,068|
| |Calhoun County|    13| 114.432|  5.030| 1,761| 15501.078| 406.169| 113,605|
| |Limestone County|    13| 131.426|  1.444| 1,318| 13324.572| 235.411|  98,915|
| |Colbert County|    13| 235.332|  5.172| 1,171| 21198.023| 312.915|  55,241|
| |Talladega County|    13| 162.545|  0.000| 1,009| 12615.969| 262.572|  79,978|
| |DeKalb County|    13| 181.785|  3.995| 1,798| 25142.282| 295.651|  71,513|
| |Cullman County|    12| 143.253|  1.705| 1,220| 14564.034| 221.701|  83,768|
| |Choctaw County|    12| 953.213|  0.000|   281| 22321.074| 113.478|  12,589|
| |Houston County|    12| 113.334|  0.000| 1,386| 13090.044| 149.762| 105,882|
| |Washington County|    12| 735.024|  8.750|   386| 23643.268| 717.523|  16,326|
| |Winston County|    11| 465.530|  6.046|   450| 19044.395| 145.100|  23,629|
| |Greene County|    11| 1356.183|  0.000|   250| 30822.340| 193.740|   8,111|
| |Bullock County|    11| 1089.001|  0.000|   463| 45837.046| 381.858|  10,101|
| |Conecuh County|    10| 828.706|  0.000|   388| 32153.808| 295.967|  12,067|
| |Randolph County|    10| 440.102|  0.000|   396| 17428.043| 62.872|  22,722|
| |Wilcox County|    10| 964.041| 13.772|   426| 41068.158| 358.072|  10,373|
| |Clarke County|     9| 381.001|  0.000|   662| 28024.723| 1106.716|  23,622|
| |Pickens County|     9| 451.581|  0.000|   392| 19668.841| 236.542|  19,930|
| |Cherokee County|     7| 267.216|  0.000|   270| 10306.917| 261.763|  26,196|
| |Pike County|     7| 211.391|  0.000|   703| 21229.691| 254.532|  33,114|
| |Coffee County|     6| 114.631|  2.729|   756| 14443.468| 166.487|  52,342|
| |Chilton County|     6| 135.050|  3.215|   788| 17736.563| 369.780|  44,428|
| |Fayette County|     5| 306.711|  0.000|   204| 12513.802| 324.237|  16,302|
| |Bibb County|     5| 223.274| 19.138|   426| 19022.953| 421.031|  22,394|
| |Barbour County|     5| 202.544|  0.000|   573| 23211.537| 109.952|  24,686|
| |Clay County|     5| 377.786|  0.000|   252| 19040.423| 561.282|  13,235|
| |Monroe County|     4| 192.929|  6.890|   419| 20209.328| 234.271|  20,733|
| |Perry County|     4| 448.280| 16.010|   440| 49310.770| 336.210|   8,923|
| |Jackson County|     4| 77.480|  2.767|   968| 18750.242| 511.924|  51,626|
| |Blount County|     4| 69.173|  2.470|   788| 13627.088| 207.519|  57,826|
| |Crenshaw County|     3| 217.833|  0.000|   314| 22799.884| 363.055|  13,772|
| |Henry County|     3| 174.368|  0.000|   259| 15053.763| 174.368|  17,205|
| |Lamar County|     2| 144.875|  0.000|   220| 15936.255| 300.098|  13,805|
| |Coosa County|     2| 187.564|  0.000|   101|  9472.006| 160.770|  10,663|
| |Russell County|     2| 34.506|  2.465| 1,358| 23429.547| 426.395|  57,961|
| |Lawrence County|     1| 30.373|  4.339|   348| 10569.797| 216.950|  32,924|
| |Cleburne County|     1| 67.069|  0.000|   126|  8450.704| 134.138|  14,910|
| |Geneva County|     0|  0.000|  0.000|   257|  9782.650| 222.951|  26,271|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,686| 221.408| N/A|62,331|  8185.407| N/A|7,614,893|
| |King County|   674| 299.186|  1.205|16,439|  7297.200| 66.521|2,252,782|
| |Yakima County|   212| 845.049|  4.556|10,269| 40933.062| 175.388| 250,873|
| |Snohomish County|   192| 233.553|  0.521| 5,423|  6596.658| 58.388| 822,083|
| |Pierce County|   140| 154.700|  2.052| 5,606|  6194.612| 85.558| 904,980|
| |Benton County|   115| 562.650|  4.194| 3,714| 18171.143| 160.058| 204,390|
| |Spokane County|    89| 170.238|  7.924| 4,415|  8444.944| 166.412| 522,798|
| |Franklin County|    49| 514.587|  3.001| 3,486| 36609.187| 307.552|  95,222|
| |Clark County|    43| 88.071|  0.293| 1,767|  3619.114| 74.319| 488,241|
| |Whatcom County|    40| 174.484|  1.246|   982|  4283.589| 44.867| 229,247|
| |Skagit County|    21| 162.532|  0.000|   876|  6779.923| 78.502| 129,205|
| |Kittitas County|    19| 396.370|  5.960|   373|  7781.371| 77.486|  47,935|
| |Grant County|    13| 133.015|  0.000| 1,459| 14928.427| 333.270|  97,733|
| |Thurston County|    11| 37.861|  1.475|   708|  2436.875| 35.403| 290,536|
| |Island County|    11| 129.197|  0.000|   249|  2924.560| 20.135|  85,141|
| |Chelan County|    10| 129.534|  0.000| 1,306| 16917.098| 370.096|  77,200|
| |Douglas County|     7| 161.183|  0.000|   938| 21598.471| 493.416|  43,429|
| |Kitsap County|     7| 25.785|  1.579|   730|  2689.034| 51.044| 271,473|
| |Okanogan County|     5| 118.363| 10.145|   861| 20382.075| 426.106|  42,243|
| |Adams County|     5| 250.213|  7.149|   434| 21718.461| 343.149|  19,983|
| |Cowlitz County|     5| 45.211|  0.000|   477|  4313.112| 46.503| 110,593|
| |Klickitat County|     3| 133.779|  0.000|   111|  4949.833| 50.964|  22,425|
| |Lewis County|     3| 37.171|  0.000|   213|  2639.176| 65.493|  80,707|
| |Walla Walla County|     2| 32.916|  0.000|   522|  8591.178| 256.278|  60,760|
| |Grays Harbor County|     2| 26.645|  1.903|   119|  1585.377| 43.774|  75,061|
| |Asotin County|     2| 88.566|  0.000|    27|  1195.643| 18.978|  22,582|
| |Pacific County|     2| 89.004|  0.000|    49|  2180.588| 57.217|  22,471|
| |Columbia County|     1| 250.941| 35.849|    13|  3262.233|  0.000|   3,985|
| |Stevens County|     1| 21.871|  0.000|   108|  2362.050| 59.364|  45,723|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 59.115|  12,083|
| |Mason County|     1| 14.977|  0.000|   212|  3175.174| 134.795|  66,768|
| |Whitman County|     0|  0.000|  0.000|   104|  2075.683| 45.619|  50,104|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Pend Oreille County|     0|  0.000|  0.000|    40|  2914.602| 52.046|  13,724|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489| 168.574|   7,627|
| |Clallam County|     0|  0.000|  0.000|   103|  1331.937| 22.168|  77,331|
| |San Juan County|     0|  0.000|  0.000|    28|  1592.538|  0.000|  17,582|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Lincoln County|     0|  0.000|  0.000|    28|  2559.649| 195.892|  10,939|
| |Jefferson County|     0|  0.000|  0.000|    54|  1675.926| 13.301|  32,221|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,648| 292.218| N/A|59,964| 10632.609| N/A|5,639,632|
| |Hennepin County|   831| 656.480|  1.806|19,057| 15054.790| 170.412|1,265,843|
| |Ramsey County|   265| 481.537|  1.298| 7,444| 13526.651| 176.780| 550,321|
| |Anoka County|   114| 319.398|  0.800| 3,618| 10136.697| 136.485| 356,921|
| |Dakota County|   104| 242.412|  0.666| 4,334| 10102.070| 157.834| 429,021|
| |Washington County|    44| 167.657|  0.544| 2,077|  7914.190| 122.477| 262,440|
| |Clay County|    40| 622.840|  0.000|   779| 12129.800| 82.304|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,718| 10853.291| 99.273| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,886| 17917.119| 70.065| 161,075|
| |St. Louis County|    19| 95.444|  0.718|   521|  2617.170| 80.374| 199,070|
| |Scott County|    18| 120.795|  4.793| 1,532| 10280.982| 185.027| 149,013|
| |Winona County|    16| 316.932|  0.000|   259|  5130.338| 45.276|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   232|  3566.213| 74.662|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   333|  9715.820| 125.043|  34,274|
| |Itasca County|    12| 265.899|  0.000|   138|  3057.833| 41.151|  45,130|
| |Goodhue County|     9| 194.217|  3.083|   192|  4143.289| 58.573|  46,340|
| |Pipestone County|     9| 986.193|  0.000|   155| 16984.440| 203.500|   9,126|
| |Sherburne County|     8| 82.272|  1.469|   718|  7383.945| 130.754|  97,238|
| |Rice County|     8| 119.453|  0.000| 1,029| 15364.630| 100.255|  66,972|
| |Nobles County|     6| 277.405|  0.000| 1,762| 81464.700| 145.308|  21,629|
| |Blue Earth County|     5| 73.907|  2.112|   911| 13465.774| 147.813|  67,653|
| |Renville County|     5| 343.690|  0.000|    63|  4330.492| 58.918|  14,548|
| |Martin County|     5| 254.026|  0.000|   207| 10516.690| 43.547|  19,683|
| |Wright County|     5| 36.133|  0.000|   869|  6279.945| 85.687| 138,377|
| |Polk County|     4| 127.535|  4.555|   150|  4782.553| 104.761|  31,364|
| |Koochiching County|     3| 245.319|  0.000|    77|  6296.508| 81.773|  12,229|
| |Otter Tail County|     3| 51.067|  0.000|   193|  3285.330| 53.499|  58,746|
| |Lyon County|     3| 117.767|  0.000|   426| 16722.933| 67.296|  25,474|
| |Mille Lacs County|     3| 114.168|  0.000|    71|  2701.983| 81.549|  26,277|
| |Benton County|     3| 73.369|  0.000|   320|  7826.066| 69.876|  40,889|
| |Carver County|     3| 28.547|  1.359|   841|  8002.741| 122.345| 105,089|
| |Grant County|     3| 502.344| 47.842|    53|  8874.749| 119.606|   5,972|
| |Wilkin County|     3| 483.325|  0.000|    34|  5477.686| 161.108|   6,207|
| |Todd County|     2| 81.090|  0.000|   424| 17191.048| 63.713|  24,664|
| |Meeker County|     2| 86.125|  0.000|    85|  3660.322| 12.304|  23,222|
| |Sibley County|     2| 134.544|  0.000|    83|  5583.586| 57.662|  14,865|
| |Mower County|     2| 49.923|  0.000| 1,099| 27432.480| 114.109|  40,062|
| |Brown County|     2| 79.974|  0.000|    88|  3518.874| 34.275|  25,008|
| |Cass County|     2| 67.161|  0.000|    69|  2317.069| 57.567|  29,779|
| |Kanabec County|     1| 61.211|  0.000|    34|  2081.165| 61.211|  16,337|
| |Murray County|     1| 122.041|  0.000|   122| 14888.943| 34.869|   8,194|
| |Kandiyohi County|     1| 23.149|  0.000|   689| 15949.443| 72.753|  43,199|
| |Freeborn County|     1| 33.024|  0.000|   359| 11855.619| 23.589|  30,281|
| |Chisago County|     1| 17.674|  0.000|   199|  3517.206| 68.173|  56,579|
| |Chippewa County|     1| 84.746|  0.000|   103|  8728.814| 84.746|  11,800|
| |Morrison County|     1| 29.953|  0.000|    89|  2665.788| 34.232|  33,386|
| |Becker County|     1| 29.050|  0.000|   152|  4415.652| 58.101|  34,423|
| |Aitkin County|     1| 62.949|  8.993|    40|  2517.940| 107.912|  15,886|
| |Swift County|     1| 107.921|  0.000|    52|  5611.915| 15.417|   9,266|
| |Steele County|     1| 27.286|  0.000|   345|  9413.627| 74.062|  36,649|
| |Douglas County|     1| 26.219|  3.746|   139|  3644.372| 48.692|  38,141|
| |Le Sueur County|     1| 34.618|  0.000|   217|  7512.030| 103.853|  28,887|
| |Mahnomen County|     1| 180.930|  0.000|    26|  4704.179| 103.389|   5,527|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 50.590|  14,119|
| |Lac qui Parle County|     0|  0.000|  0.000|     7|  1056.923| 21.570|   6,623|
| |Lake County|     0|  0.000|  0.000|    20|  1879.523| 40.275|  10,641|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Yellow Medicine County|     0|  0.000|  0.000|    52|  5355.855| 44.142|   9,709|
| |Cook County|     0|  0.000|  0.000|     3|   549.149| 26.150|   5,463|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Carlton County|     0|  0.000|  0.000|   135|  3763.486| 55.755|  35,871|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   223|  4725.778| 105.959|  47,188|
| |Cottonwood County|     0|  0.000|  0.000|   177| 15809.218| 89.318|  11,196|
| |Jackson County|     0|  0.000|  0.000|    81|  8226.691| 174.110|   9,846|
| |Isanti County|     0|  0.000|  0.000|   123|  3029.855| 73.899|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    33|  1535.526| 39.884|  21,491|
| |Houston County|     0|  0.000|  0.000|    39|  2096.774|  7.680|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    64|  3037.927| 20.343|  21,067|
| |Faribault County|     0|  0.000|  0.000|    87|  6372.226| 52.317|  13,653|
| |Dodge County|     0|  0.000|  0.000|   126|  6018.917| 27.297|  20,934|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 246.609|   4,055|
| |Pope County|     0|  0.000|  0.000|    46|  4089.252| 88.897|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202| 14.489|  29,579|
| |Norman County|     0|  0.000|  0.000|    39|  6117.647| 112.045|   6,375|
| |Marshall County|     0|  0.000|  0.000|    30|  3213.368| 30.604|   9,336|
| |McLeod County|     0|  0.000|  0.000|   173|  4819.881| 163.183|  35,893|
| |Lincoln County|     0|  0.000|  0.000|    57| 10108.175| 101.335|   5,639|
| |Lake of the Woods County|     0|  0.000|  0.000|     2|   534.759| 38.197|   3,740|
| |Waseca County|     0|  0.000|  0.000|   148|  7951.859| 161.186|  18,612|
| |Watonwan County|     0|  0.000|  0.000|   308| 28264.660| 131.098|  10,897|
| |Redwood County|     0|  0.000|  0.000|    36|  2373.105| 56.502|  15,170|
| |Rock County|     0|  0.000|  0.000|    83|  8910.360| 153.362|   9,315|
| |Roseau County|     0|  0.000|  0.000|    47|  3099.242| 47.101|  15,165|
| |Wadena County|     0|  0.000|  0.000|    26|  1900.307| 31.324|  13,682|
| |Wabasha County|     0|  0.000|  0.000|    91|  4207.703| 85.871|  21,627|
| |Traverse County|     0|  0.000|  0.000|    10|  3068.426|  0.000|   3,259|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 43.709|   9,805|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,266| 206.275| N/A|51,545|  8398.469| N/A|6,137,428|
| |St. Louis County|   837| 841.879|  2.586|19,805| 19920.439| 296.576| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,954|  9835.283| 158.485| 402,022|
| |Jackson County|    64| 91.037|  1.016| 3,909|  5560.368| 104.245| 703,011|
| |Jasper County|    30| 247.264|  5.887| 1,738| 14324.805| 108.325| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,544|  6859.753| 137.094| 225,081|
| |Clay County|    20| 80.017|  0.000| 1,011|  4044.841| 65.728| 249,948|
| |Franklin County|    18| 173.132|  0.000|   590|  5674.878| 101.681| 103,967|
| |Scott County|    13| 339.603|  0.000|   381|  9952.978| 149.276|  38,280|
| |Platte County|    10| 95.769|  0.000|   343|  3284.874| 47.884| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,076| 12316.286| 32.704|  87,364|
| |Greene County|    10| 34.120|  0.000| 1,440|  4913.234| 115.032| 293,086|
| |Stoddard County|     9| 310.078|  0.000|   224|  7717.485| 83.672|  29,025|
| |Pemiscot County|     9| 569.440|  9.039|   234| 14805.441| 271.162|  15,805|
| |Gentry County|     9| 1369.655|  0.000|    83| 12631.259| 86.962|   6,571|
| |Cass County|     9| 85.082|  0.000|   705|  6664.776| 101.288| 105,780|
| |McDonald County|     7| 306.520|  0.000|   950| 41599.159| 150.132|  22,837|
| |Saline County|     7| 307.544|  0.000|   424| 18628.356| 94.146|  22,761|
| |Newton County|     6| 103.029|  0.000|   868| 14904.870| 169.262|  58,236|
| |Camden County|     5| 107.980|  3.085|   339|  7321.024| 138.831|  46,305|
| |Cape Girardeau County|     5| 63.395|  3.623|   636|  8063.800| 72.451|  78,871|
| |Barry County|     4| 111.766| 15.967|   248|  6929.503| 83.825|  35,789|
| |Pettis County|     4| 94.476|  3.374|   487| 11502.397| 269.930|  42,339|
| |Perry County|     4| 209.030|  0.000|   223| 11653.428| 156.773|  19,136|
| |Dunklin County|     4| 137.311|  0.000|   300| 10298.308| 284.429|  29,131|
| |Cole County|     3| 39.090|  1.861|   376|  4899.342| 128.440|  76,745|
| |Taney County|     3| 53.640|  0.000|   548|  9798.312| 370.374|  55,928|
| |Henry County|     3| 137.463|  0.000|    76|  3482.405| 45.821|  21,824|
| |Boone County|     3| 16.624|  0.000| 1,328|  7358.849| 97.369| 180,463|
| |Moniteau County|     2| 123.977|  0.000|   139|  8616.415| 159.399|  16,132|
| |Lafayette County|     2| 61.147|  0.000|   175|  5350.373| 104.824|  32,708|
| |Lawrence County|     2| 52.144|  0.000|   211|  5501.238| 100.564|  38,355|
| |Howell County|     2| 49.854|  0.000|   152|  3788.917| 67.659|  40,117|
| |Douglas County|     2| 151.688|  0.000|    83|  6295.032| 108.348|  13,185|
| |Butler County|     2| 47.083|  0.000|   275|  6473.939| 121.071|  42,478|
| |St. Francois County|     2| 29.755|  0.000|   350|  5207.171| 112.645|  67,215|
| |Johnson County|     2| 36.995|  0.000|   486|  8989.679| 60.777|  54,062|
| |Ray County|     2| 86.889| 12.413|   116|  5039.534| 161.364|  23,018|
| |Ste. Genevieve County|     1| 55.885|  0.000|    53|  2961.887| 79.835|  17,894|
| |Scotland County|     1| 203.998|  0.000|    14|  2855.977| 58.285|   4,902|
| |Randolph County|     1| 40.407|  0.000|    67|  2707.289| 69.270|  24,748|
| |Stone County|     1| 31.297|  0.000|   123|  3849.524| 183.311|  31,952|
| |Shannon County|     1| 122.459|  0.000|    43|  5265.736|  0.000|   8,166|
| |Webster County|     1| 25.258|  0.000|   128|  3232.976| 54.123|  39,592|
| |Washington County|     1| 40.437|  0.000|    69|  2790.133| 86.650|  24,730|
| |Miller County|     1| 39.034|  5.576|   114|  4449.822| 117.101|  25,619|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Carter County|     1| 167.168|  0.000|    20|  3343.363| 23.881|   5,982|
| |Linn County|     1| 83.893|  0.000|    29|  2432.886|  0.000|  11,920|
| |Grundy County|     1| 101.523|  0.000|    25|  2538.071| 14.503|   9,850|
| |Callaway County|     1| 22.350|  0.000|   142|  3173.681| 60.664|  44,743|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131| 95.027|   9,020|
| |New Madrid County|     1| 58.562|  0.000|   230| 13469.197| 426.664|  17,076|
| |DeKalb County|     1| 79.700|  0.000|    35|  2789.511| 34.157|  12,547|
| |Osage County|     1| 73.448| 10.493|    45|  3305.178| 83.941|  13,615|
| |Bollinger County|     1| 82.420| 11.774|    64|  5274.870| 94.194|  12,133|
| |Audrain County|     1| 39.389|  0.000|   199|  7838.349| 39.389|  25,388|
| |Pulaski County|     1| 19.009|  0.000|   197|  3744.749| 48.880|  52,607|
| |Marion County|     1| 35.051|  0.000|   181|  6344.199| 155.225|  28,530|
| |Benton County|     1| 51.432|  0.000|    90|  4628.915| 139.602|  19,443|
| |Dallas County|     1| 59.249|  0.000|    60|  3554.924| 101.569|  16,878|
| |Laclede County|     1| 27.993|  0.000|   195|  5458.668|  3.999|  35,723|
| |Bates County|     1| 61.835|  0.000|    44|  2720.752| 44.168|  16,172|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313| 91.263|   4,696|
| |Lewis County|     1| 102.291|  0.000|    40|  4091.653| 116.904|   9,776|
| |Lincoln County|     1| 16.945|  0.000|   360|  6100.351| 162.192|  59,013|
| |Christian County|     1| 11.287|  0.000|   335|  3781.252| 96.748|  88,595|
| |Pike County|     1| 54.639|  0.000|    95|  5190.690| 202.944|  18,302|
| |Andrew County|     1| 56.459|  0.000|    88|  4968.383| 40.328|  17,712|
| |Adair County|     0|  0.000|  0.000|   152|  5997.711| 101.465|  25,343|
| |Gasconade County|     0|  0.000|  0.000|    21|  1427.989|  9.714|  14,706|
| |Dent County|     0|  0.000|  0.000|    10|   642.137|  9.173|  15,573|
| |Daviess County|     0|  0.000|  0.000|    17|  2053.636|  0.000|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865| 18.894|   7,561|
| |Crawford County|     0|  0.000|  0.000|    71|  2968.227| 113.473|  23,920|
| |Cooper County|     0|  0.000|  0.000|   116|  6550.342| 201.673|  17,709|
| |Clinton County|     0|  0.000|  0.000|    79|  3875.018| 126.131|  20,387|
| |Clark County|     0|  0.000|  0.000|    20|  2942.475| 147.124|   6,797|
| |Chariton County|     0|  0.000|  0.000|    17|  2289.254| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    38|  2648.268| 39.824|  14,349|
| |Carroll County|     0|  0.000|  0.000|   100| 11522.065| 32.920|   8,679|
| |Barton County|     0|  0.000|  0.000|    69|  5870.342| 48.616|  11,754|
| |Atchison County|     0|  0.000|  0.000|    14|  2722.147| 83.331|   5,143|
| |Holt County|     0|  0.000|  0.000|     8|  1816.943| 64.891|   4,403|
| |Hickory County|     0|  0.000|  0.000|    28|  2933.780| 179.619|   9,544|
| |Howard County|     0|  0.000|  0.000|    49|  4899.510| 57.137|  10,001|
| |Monroe County|     0|  0.000|  0.000|    27|  3123.554| 165.267|   8,644|
| |Mercer County|     0|  0.000|  0.000|    10|  2764.722| 78.992|   3,617|
| |Maries County|     0|  0.000|  0.000|    20|  2299.644| 98.556|   8,697|
| |Schuyler County|     0|  0.000|  0.000|    10|  2145.923| 30.656|   4,660|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    61|  3335.338| 23.433|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939| 70.967|   2,013|
| |Wayne County|     0|  0.000|  0.000|    55|  4272.508| 233.046|  12,873|
| |Warren County|     0|  0.000|  0.000|   191|  5357.794| 136.249|  35,649|
| |Vernon County|     0|  0.000|  0.000|    49|  2382.921| 34.736|  20,563|
| |Texas County|     0|  0.000|  0.000|    50|  1968.659| 84.371|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   141| 23156.512| 164.231|   6,089|
| |Mississippi County|     0|  0.000|  0.000|   134| 10166.920| 54.195|  13,180|
| |Montgomery County|     0|  0.000|  0.000|    41|  3549.476| 98.940|  11,551|
| |Shelby County|     0|  0.000|  0.000|    30|  5059.022| 48.181|   5,930|
| |Morgan County|     0|  0.000|  0.000|    78|  3781.451| 110.812|  20,627|
| |St. Clair County|     0|  0.000|  0.000|    18|  1915.505|  0.000|   9,397|
| |Ripley County|     0|  0.000|  0.000|    51|  3838.049| 107.508|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    29|  2813.076| 110.860|  10,309|
| |Polk County|     0|  0.000|  0.000|   209|  6500.980| 88.872|  32,149|
| |Phelps County|     0|  0.000|  0.000|    81|  1817.244| 19.230|  44,573|
| |Ozark County|     0|  0.000|  0.000|    12|  1308.044| 93.432|   9,174|
| |Oregon County|     0|  0.000|  0.000|    14|  1329.661| 13.568|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   175|  7921.420| 142.262|  22,092|
| |Livingston County|     0|  0.000|  0.000|    60|  3940.369| 65.673|  15,227|
| |Knox County|     0|  0.000|  0.000|    27|  6819.904| 577.346|   3,959|
| |Iron County|     0|  0.000|  0.000|    21|  2074.074| 98.765|  10,125|
| |Madison County|     0|  0.000|  0.000|    24|  1985.440| 82.727|  12,088|
| |Macon County|     0|  0.000|  0.000|    57|  3770.589| 37.800|  15,117|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,191| 174.399| N/A|114,597| 16780.507| N/A|6,829,174|
| |Shelby County|   301| 321.181|  2.591|22,916| 24452.445| 288.865| 937,166|
| |Davidson County|   213| 306.853|  3.087|20,383| 29364.224| 248.405| 694,144|
| |Sumner County|    73| 381.633|  2.987| 3,404| 17795.622| 200.152| 191,283|
| |Rutherford County|    54| 162.511|  1.290| 6,463| 19450.171| 199.485| 332,285|
| |Hamilton County|    53| 144.098|  2.330| 6,062| 16481.604| 199.252| 367,804|
| |Knox County|    38| 80.797|  2.126| 4,513|  9595.737| 201.993| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,478| 14588.192| 170.773| 238,412|
| |Wilson County|    23| 158.997|  2.963| 2,262| 15636.990| 218.250| 144,657|
| |McMinn County|    20| 371.789|  0.000|   531|  9870.989| 156.682|  53,794|
| |Robertson County|    19| 264.576|  5.968| 1,535| 21374.960| 234.737|  71,813|
| |Putnam County|    18| 224.313|  8.901| 1,740| 21683.594| 350.712|  80,245|
| |Madison County|    17| 173.498|  7.290| 1,064| 10858.916| 293.051|  97,984|
| |Hardeman County|    17| 678.643| 34.217|   898| 35848.303| 633.020|  25,050|
| |Hamblen County|    14| 215.604|  2.200| 1,383| 21298.549| 385.006|  64,934|
| |Sullivan County|    14| 88.413|  5.413|   962|  6075.227| 184.043| 158,348|
| |Macon County|    13| 528.412|  0.000|   858| 34875.213| 139.361|  24,602|
| |Giles County|    13| 441.216| 19.394|   378| 12829.215| 213.335|  29,464|
| |Montgomery County|    13| 62.203|  1.367| 1,902|  9100.783| 153.799| 208,993|
| |Bradley County|    12| 110.998|  2.643| 1,903| 17602.442| 293.352| 108,110|
| |Blount County|    11| 82.652|  4.294| 1,277|  9595.155| 201.800| 133,088|
| |Bedford County|    11| 221.270|  2.874|   918| 18465.995| 192.534|  49,713|
| |Monroe County|     9| 193.361|  0.000|   418|  8980.556| 202.569|  46,545|
| |Tipton County|     9| 146.106|  0.000| 1,195| 19399.666| 234.234|  61,599|
| |Greene County|     8| 115.826|  6.205|   467|  6761.355| 217.174|  69,069|
| |Hardin County|     8| 311.867|  5.569|   462| 18010.292| 378.695|  25,652|
| |Lauderdale County|     8| 312.098| 11.146|   489| 19076.971| 384.549|  25,633|
| |Fayette County|     8| 194.491|  0.000|   686| 16677.607| 243.114|  41,133|
| |Dyer County|     7| 188.380|  0.000|   628| 16900.347| 361.381|  37,159|
| |Hawkins County|     7| 123.270|  7.547|   451|  7942.098| 369.809|  56,786|
| |Maury County|     7| 72.624|  2.964| 1,225| 12709.183| 259.371|  96,387|
| |Cheatham County|     7| 172.130|  7.026|   578| 14212.998| 158.078|  40,667|
| |Sevier County|     7| 71.247|  2.908| 1,850| 18829.517| 248.637|  98,250|
| |Trousdale County|     6| 531.726|  0.000| 1,582| 140198.511| 126.602|  11,284|
| |Lawrence County|     6| 135.925|  0.000|   550| 12459.789| 297.740|  44,142|
| |Cumberland County|     6| 99.141|  0.000|   450|  7435.558| 179.398|  60,520|
| |Haywood County|     6| 346.741|  8.256|   463| 26756.819| 800.806|  17,304|
| |Anderson County|     6| 77.944|  1.856|   676|  8781.730| 172.591|  76,978|
| |Carter County|     6| 106.400|  2.533|   512|  9079.463| 266.000|  56,391|
| |White County|     5| 182.849| 10.449|   281| 10276.102| 485.855|  27,345|
| |McNairy County|     5| 194.598|  0.000|   371| 14439.169| 344.716|  25,694|
| |Gibson County|     5| 101.765|  8.723|   693| 14104.573| 415.781|  49,133|
| |Franklin County|     4| 94.769|  0.000|   325|  7699.962| 182.768|  42,208|
| |Crockett County|     4| 281.096| 10.039|   266| 18692.902| 461.801|  14,230|
| |Obion County|     4| 133.027|  0.000|   546| 18158.236| 603.374|  30,069|
| |Marion County|     4| 138.375|  0.000|   222|  7679.801| 113.665|  28,907|
| |Smith County|     4| 198.442|  7.087|   445| 22076.698| 602.414|  20,157|
| |Weakley County|     4| 120.019|  4.286|   421| 12632.021| 728.688|  33,328|
| |Warren County|     4| 96.906|  0.000|   507| 12282.869| 394.547|  41,277|
| |Humphreys County|     3| 161.447|  0.000|   120|  6457.862| 153.759|  18,582|
| |Coffee County|     3| 53.079|  2.528|   522|  9235.669| 320.999|  56,520|
| |Polk County|     3| 178.232| 16.974|   204| 12119.772| 398.900|  16,832|
| |Decatur County|     3| 257.224| 24.497|   198| 16976.764| 477.701|  11,663|
| |Carroll County|     3| 108.042|  0.000|   296| 10660.136| 411.588|  27,767|
| |Jefferson County|     3| 55.051|  2.621|   559| 10257.822| 207.096|  54,495|
| |Loudon County|     3| 55.486|  0.000|   725| 13409.040| 216.658|  54,068|
| |Marshall County|     3| 87.273|  4.156|   290|  8436.364| 120.519|  34,375|
| |Dickson County|     2| 37.073|  2.648|   679| 12586.194| 262.157|  53,948|
| |Henderson County|     2| 71.131| 10.162|   563| 20023.473| 711.313|  28,117|
| |DeKalb County|     2| 97.609|  6.972|   349| 17032.699| 320.714|  20,490|
| |Wayne County|     2| 119.954|  8.568|   225| 13494.872| 111.386|  16,673|
| |Washington County|     2| 15.459|  0.000| 1,225|  9468.599| 256.177| 129,375|
| |Rhea County|     2| 60.301|  4.307|   528| 15919.438| 159.367|  33,167|
| |Roane County|     2| 37.466|  2.676|   461|  8635.870| 305.079|  53,382|
| |Hancock County|     2| 302.115| 21.580|    78| 11782.477| 129.478|   6,620|
| |Cocke County|     2| 55.549|  3.968|   457| 12693.034| 285.683|  36,004|
| |Chester County|     2| 115.627|  8.259|   217| 12545.528| 222.995|  17,297|
| |Grundy County|     2| 148.954|  0.000|   113|  8415.878| 159.593|  13,427|
| |Benton County|     1| 61.881|  0.000|   148|  9158.416| 503.890|  16,160|
| |Bledsoe County|     1| 66.383|  0.000|   695| 46136.484| 322.434|  15,064|
| |Campbell County|     1| 25.099|  0.000|   247|  6199.488| 157.766|  39,842|
| |Jackson County|     1| 84.846|  0.000|   124| 10520.957| 230.297|  11,786|
| |Lewis County|     1| 81.513|  0.000|    73|  5950.440| 256.183|  12,268|
| |Lincoln County|     1| 29.099|  0.000|   280|  8147.588| 124.708|  34,366|
| |Morgan County|     1| 46.722|  0.000|   118|  5513.246| 280.335|  21,403|
| |Overton County|     1| 44.962|  0.000|   180|  8093.161| 295.465|  22,241|
| |Pickett County|     1| 198.098|  0.000|    31|  6141.046| 254.698|   5,048|
| |Meigs County|     0|  0.000|  0.000|   104|  8372.243| 92.003|  12,422|
| |Moore County|     0|  0.000|  0.000|    61|  9401.973| 396.336|   6,488|
| |Perry County|     0|  0.000|  0.000|    79|  9782.070| 106.135|   8,076|
| |Fentress County|     0|  0.000|  0.000|    92|  4966.798| 146.536|  18,523|
| |Grainger County|     0|  0.000|  0.000|   196|  8404.803| 196.030|  23,320|
| |Henry County|     0|  0.000|  0.000|   276|  8533.004| 313.583|  32,345|
| |Hickman County|     0|  0.000|  0.000|   259| 10286.758| 232.629|  25,178|
| |Johnson County|     0|  0.000|  0.000|   265| 14897.684| 995.856|  17,788|
| |Lake County|     0|  0.000|  0.000|   782| 111459.521| 855.188|   7,016|
| |Cannon County|     0|  0.000|  0.000|   143|  9742.472| 272.517|  14,678|
| |Scott County|     0|  0.000|  0.000|   118|  5347.109| 129.470|  22,068|
| |Sequatchie County|     0|  0.000|  0.000|   105|  6987.888| 104.581|  15,026|
| |Claiborne County|     0|  0.000|  0.000|   266|  8323.164| 250.321|  31,959|
| |Clay County|     0|  0.000|  0.000|    75|  9848.982| 262.640|   7,615|
| |Stewart County|     0|  0.000|  0.000|    74|  5395.552| 72.913|  13,715|
| |Unicoi County|     0|  0.000|  0.000|   161|  9002.964| 199.711|  17,883|
| |Union County|     0|  0.000|  0.000|   154|  7710.795| 286.115|  19,972|
| |Van Buren County|     0|  0.000|  0.000|    36|  6130.790| 97.314|   5,872|
| |Houston County|     0|  0.000|  0.000|    57|  6950.372| 52.258|   8,201|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   996| 171.062| N/A|59,933| 10293.461| N/A|5,822,434|
| |Milwaukee County|   456| 482.169|  1.511|20,920| 22120.572| 211.629| 945,726|
| |Racine County|    78| 397.329|  1.455| 3,499| 17823.759| 224.134| 196,311|
| |Kenosha County|    60| 353.855|  5.898| 2,659| 15681.672| 173.557| 169,561|
| |Waukesha County|    58| 143.494|  1.414| 4,188| 10361.259| 215.594| 404,198|
| |Brown County|    54| 204.126|  1.620| 4,240| 16027.701| 150.125| 264,542|
| |Dane County|    38| 69.509|  0.261| 4,492|  8216.647| 99.298| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,425|  8723.386| 59.468| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,314| 12650.672| 122.408| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,039|  7637.796| 187.978| 136,034|
| |Winnebago County|    18| 104.708|  0.831| 1,164|  6771.103| 102.215| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   676|  7576.692| 188.937|  89,221|
| |Waupaca County|    15| 294.175|  0.000|   442|  8668.366| 232.539|  50,990|
| |Grant County|    15| 291.608|  2.777|   352|  6843.057| 88.871|  51,439|
| |Outagamie County|    14| 74.514|  0.760| 1,236|  6578.492| 120.895| 187,885|
| |Sheboygan County|     9| 78.030|  4.954|   742|  6433.154| 193.218| 115,340|
| |Marathon County|     9| 66.327|  3.158|   629|  4635.498| 71.591| 135,692|
| |Fond du Lac County|     7| 67.696|  1.382|   635|  6141.021| 124.340| 103,403|
| |Clark County|     7| 201.300|  0.000|   183|  5262.552| 41.082|  34,774|
| |St. Croix County|     5| 55.135|  4.726|   485|  5348.065| 67.737|  90,687|
| |Dodge County|     5| 56.922|  0.000|   808|  9198.648| 216.305|  87,839|
| |Jefferson County|     5| 58.984|  0.000|   624|  7361.182| 124.709|  84,769|
| |Eau Claire County|     4| 38.224|  1.365|   574|  5485.159| 121.498| 104,646|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 82.806|  17,252|
| |Forest County|     4| 444.247|  0.000|    59|  6552.643|  0.000|   9,004|
| |Door County|     3| 108.429|  0.000|   103|  3722.712| 92.939|  27,668|
| |Marinette County|     3| 74.349|  0.000|   387|  9591.078| 315.100|  40,350|
| |Barron County|     3| 66.307|  0.000|   291|  6431.792| 119.984|  45,244|
| |Sauk County|     3| 46.553|  0.000|   433|  6719.220| 135.227|  64,442|
| |Kewaunee County|     2| 97.876|  0.000|   130|  6361.946| 139.823|  20,434|
| |Monroe County|     2| 43.240|  3.089|   242|  5232.093| 92.658|  46,253|
| |Polk County|     2| 45.680|  0.000|   131|  2992.029| 45.680|  43,783|
| |Adams County|     2| 98.912|  0.000|    85|  4203.759| 113.042|  20,220|
| |Trempealeau County|     2| 67.456|  0.000|   336| 11332.591| 149.367|  29,649|
| |Calumet County|     2| 39.929|  0.000|   313|  6248.877| 191.088|  50,089|
| |Pierce County|     2| 46.779|  6.683|   209|  4888.431| 133.655|  42,754|
| |Buffalo County|     2| 153.480|  0.000|    43|  3299.823| 21.926|  13,031|
| |Rusk County|     1| 70.532|  0.000|    20|  1410.636| 50.380|  14,178|
| |Marquette County|     1| 64.210|  0.000|    79|  5072.557| 91.728|  15,574|
| |Manitowoc County|     1| 12.661|  0.000|   332|  4203.543| 66.924|  78,981|
| |Waushara County|     1| 40.912|  5.845|   115|  4704.823| 87.668|  24,443|
| |Wood County|     1| 13.699|  0.000|   286|  3917.862| 111.548|  72,999|
| |Jackson County|     1| 48.443|  0.000|    58|  2809.669| 76.124|  20,643|
| |Juneau County|     1| 37.471|  0.000|   137|  5133.586| 80.296|  26,687|
| |La Crosse County|     1|  8.473|  0.000|   896|  7592.191| 122.259| 118,016|
| |Langlade County|     1| 52.113|  0.000|    63|  3283.131| 126.561|  19,189|
| |Burnett County|     1| 64.876|  0.000|    22|  1427.274| 74.144|  15,414|
| |Iron County|     1| 175.840|  0.000|    74| 13012.133| 75.360|   5,687|
| |Green County|     1| 27.056|  0.000|   158|  4274.892| 127.551|  36,960|
| |Columbia County|     1| 17.382|  0.000|   245|  4258.500| 64.560|  57,532|
| |Bayfield County|     1| 66.507|  0.000|    23|  1529.662| 38.004|  15,036|
| |Ashland County|     1| 64.259|  9.180|    24|  1542.218| 45.899|  15,562|
| |Vilas County|     0|  0.000|  0.000|    53|  2387.925| 148.038|  22,195|
| |Vernon County|     0|  0.000|  0.000|    62|  2011.550| 18.540|  30,822|
| |Taylor County|     0|  0.000|  0.000|    69|  3391.830| 133.426|  20,343|
| |Shawano County|     0|  0.000|  0.000|   190|  4645.590| 129.238|  40,899|
| |Sawyer County|     0|  0.000|  0.000|    59|  3563.232| 198.437|  16,558|
| |Washburn County|     0|  0.000|  0.000|    45|  2862.595| 145.402|  15,720|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689| 39.209|   7,287|
| |Price County|     0|  0.000|  0.000|    33|  2471.725| 128.401|  13,351|
| |Portage County|     0|  0.000|  0.000|   405|  5722.602| 123.132|  70,772|
| |Oneida County|     0|  0.000|  0.000|   124|  3483.635| 148.496|  35,595|
| |Oconto County|     0|  0.000|  0.000|   237|  6248.352| 222.214|  37,930|
| |Chippewa County|     0|  0.000|  0.000|   227|  3510.780| 39.770|  64,658|
| |Crawford County|     0|  0.000|  0.000|    74|  4587.440| 150.553|  16,131|
| |Florence County|     0|  0.000|  0.000|     8|  1862.631| 33.261|   4,295|
| |Menominee County|     0|  0.000|  0.000|    22|  4828.797| 125.423|   4,556|
| |Green Lake County|     0|  0.000|  0.000|    55|  2908.053| 22.660|  18,913|
| |Iowa County|     0|  0.000|  0.000|    79|  3336.430| 96.533|  23,678|
| |Lincoln County|     0|  0.000|  0.000|    68|  2464.393| 36.241|  27,593|
| |Lafayette County|     0|  0.000|  0.000|   130|  7800.780| 214.307|  16,665|
| |Dunn County|     0|  0.000|  0.000|   122|  2689.120| 53.530|  45,368|
| |Douglas County|     0|  0.000|  0.000|   172|  3986.095| 165.536|  43,150|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   941| 305.504| N/A|55,080| 17882.211| N/A|3,080,156|
| |Clark County|   799| 352.492|  6.996|47,739| 21060.874| 351.169|2,266,715|
| |Washoe County|   118| 250.255|  1.212| 5,715| 12120.402| 160.272| 471,519|
| |Nye County|     9| 193.453|  0.000|   405|  8705.372| 199.594|  46,523|
| |Lyon County|     6| 104.330|  2.484|   222|  3860.198| 52.165|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   102|  6060.246| 50.926|  16,831|
| |Elko County|     2| 37.895|  0.000|   535| 10136.799| 184.059|  52,778|
| |White Pine County|     1| 104.384|  0.000|    15|  1565.762| 29.824|   9,580|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 25.824|   5,532|
| |Churchill County|     1| 40.146|  0.000|    62|  2489.060| 103.233|  24,909|
| |Storey County|     0|  0.000|  0.000|     4|   970.167|  0.000|   4,123|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Pershing County|     0|  0.000|  0.000|    13|  1933.086|  0.000|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 55.125|   5,183|
| |Eureka County|     0|  0.000|  0.000|     2|   985.707|  0.000|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Douglas County|     0|  0.000|  0.000|   199|  4069.114| 87.633|  48,905|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   927| 293.813| N/A|48,528| 15380.958| N/A|3,155,070|
| |Polk County|   207| 422.310|  1.457|10,223| 20856.412| 178.950| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,348| 10357.026| 178.961| 226,706|
| |Black Hawk County|    66| 502.941|  4.354| 3,115| 23737.312| 142.609| 131,228|
| |Woodbury County|    52| 504.330|  4.157| 3,716| 36040.230| 119.155| 103,107|
| |Muscatine County|    48| 1125.070|  3.348|   846| 19829.364| 103.801|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,878| 20095.663| 169.680|  93,453|
| |Wapello County|    33| 943.693|  8.171|   881| 25193.743| 212.433|  34,969|
| |Dubuque County|    31| 318.566|  2.936| 1,665| 17110.090| 237.824|  97,311|
| |Tama County|    29| 1720.660|  0.000|   549| 32573.870| 118.666|  16,854|
| |Jasper County|    26| 699.207|  7.684|   476| 12800.861| 88.361|  37,185|
| |Marshall County|    26| 660.418|  7.257| 1,438| 36526.201| 206.834|  39,369|
| |Pottawattamie County|    26| 278.952|  7.664| 1,314| 14097.805| 168.597|  93,206|
| |Johnson County|    19| 125.711|  3.781| 2,067| 13676.062| 156.903| 151,140|
| |Mahaska County|    17| 769.405|  0.000|   139|  6291.016| 25.862|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   609| 14346.290| 104.324|  42,450|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644| 12.946|  11,035|
| |Scott County|    14| 80.952|  1.652| 1,716|  9922.344| 115.645| 172,943|
| |Story County|    14| 144.156|  1.471| 1,160| 11944.356| 86.788|  97,117|
| |Buena Vista County|    12| 611.621|  0.000| 1,791| 91284.404| 58.250|  19,620|
| |Washington County|    10| 455.270|  0.000|   298| 13567.038| 84.550|  21,965|
| |Franklin County|    10| 993.049| 85.118|   239| 23733.863| 383.033|  10,070|
| |Plymouth County|     9| 357.469|  5.674|   457| 18151.487| 96.460|  25,177|
| |Poweshiek County|     8| 432.339|  0.000|   157|  8484.652| 92.644|  18,504|
| |Bremer County|     7| 279.307|  0.000|   224|  8937.834| 210.906|  25,062|
| |Webster County|     7| 194.964|  7.958|   801| 22309.492| 366.056|  35,904|
| |Monroe County|     7| 908.265|  0.000|    72|  9342.156| 111.216|   7,707|
| |Guthrie County|     5| 467.771|  0.000|   131| 12255.590| 80.189|  10,689|
| |Dickinson County|     4| 231.777|  0.000|   380| 22018.774| 49.666|  17,258|
| |Emmet County|     4| 434.405| 46.543|   191| 20742.832| 201.688|   9,208|
| |Lucas County|     4| 465.116|  0.000|    63|  7325.581| 348.837|   8,600|
| |Montgomery County|     4| 403.348| 14.405|    59|  5949.380| 230.484|   9,917|
| |Allamakee County|     4| 292.248|  0.000|   154| 11251.553| 52.187|  13,687|
| |Boone County|     3| 114.355|  5.445|   255|  9720.210| 147.028|  26,234|
| |Appanoose County|     3| 241.429|  0.000|    48|  3862.868| 91.973|  12,426|
| |Sioux County|     3| 86.071|  4.099|   625| 17931.430| 151.649|  34,855|
| |Lee County|     3| 89.135|  0.000|   113|  3357.400| 106.113|  33,657|
| |Clarke County|     3| 319.319|  0.000|   199| 21181.480| 319.319|   9,395|
| |Clayton County|     3| 170.950|  0.000|   104|  5926.264| 73.264|  17,549|
| |Crawford County|     3| 178.359|  0.000|   727| 43222.354| 144.386|  16,820|
| |Henry County|     3| 150.346|  0.000|   120|  6013.832| 64.434|  19,954|
| |Clinton County|     3| 64.615|  0.000|   379|  8163.002| 230.767|  46,429|
| |Calhoun County|     2| 206.868|  0.000|    83|  8585.023| 29.553|   9,668|
| |Hancock County|     2| 188.147|  0.000|   122| 11476.952| 107.512|  10,630|
| |Madison County|     2| 122.414|  0.000|   118|  7222.426| 192.365|  16,338|
| |O'Brien County|     2| 145.423| 10.387|   137|  9961.463| 218.134|  13,753|
| |Lyon County|     2| 170.140| 24.306|   113|  9612.931| 170.140|  11,755|
| |Pocahontas County|     2| 302.160| 21.583|   115| 17374.226| 43.166|   6,619|
| |Jones County|     2| 96.707|  6.908|   130|  6285.963| 55.261|  20,681|
| |Butler County|     2| 138.514|  0.000|   121|  8380.082| 98.938|  14,439|
| |Floyd County|     2| 127.861|  0.000|   153|  9781.358| 337.918|  15,642|
| |Des Moines County|     2| 51.325|  0.000|   169|  4337.003| 113.649|  38,967|
| |Keokuk County|     1| 97.599|  0.000|    34|  3318.368| 55.771|  10,246|
| |Audubon County|     1| 181.951|  0.000|    28|  5094.614|  0.000|   5,496|
| |Benton County|     1| 38.994|  0.000|   155|  6044.063| 89.129|  25,645|
| |Carroll County|     1| 49.591|  0.000|   188|  9323.085| 85.013|  20,165|
| |Cass County|     1| 77.906|  0.000|    71|  5531.318| 311.624|  12,836|
| |Cedar County|     1| 53.686|  0.000|   131|  7032.802| 92.032|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   108|  9612.817| 139.869|  11,235|
| |Clay County|     1| 62.438|  0.000|   186| 11613.387| 142.714|  16,016|
| |Davis County|     1| 111.111|  0.000|    55|  6111.111| 95.238|   9,000|
| |Buchanan County|     1| 47.226|  0.000|   127|  5997.639| 128.184|  21,175|
| |Delaware County|     1| 58.785|  0.000|   111|  6525.190| 201.550|  17,011|
| |Shelby County|     1| 87.306|  0.000|   183| 15976.951| 336.751|  11,454|
| |Wright County|     1| 79.605|  0.000|   465| 37016.399| 284.304|  12,562|
| |Winneshiek County|     1| 50.023|  0.000|    95|  4752.138| 121.483|  19,991|
| |Wayne County|     1| 155.255|  0.000|    19|  2949.853| 88.717|   6,441|
| |Van Buren County|     1| 141.965|  0.000|    34|  4826.803| 81.123|   7,044|
| |Union County|     1| 81.693|  0.000|    77|  6290.336| 81.693|  12,241|
| |Warren County|     1| 19.430|  0.000|   557| 10822.679| 111.030|  51,466|
| |Grundy County|     1| 81.753|  0.000|    79|  6458.470| 81.753|  12,232|
| |Hamilton County|     1| 67.691|  0.000|   246| 16652.000| 77.361|  14,773|
| |Jackson County|     1| 51.443|  0.000|   151|  7767.889| 124.933|  19,439|
| |Iowa County|     1| 61.789|  0.000|    97|  5993.574| 61.789|  16,184|
| |Humboldt County|     1| 104.624|  0.000|   108| 11299.435| 283.981|   9,558|
| |Ringgold County|     1| 204.332|  0.000|    21|  4290.969|  0.000|   4,894|
| |Worth County|     0|  0.000|  0.000|    66|  8941.878| 116.128|   7,381|
| |Winnebago County|     0|  0.000|  0.000|    79|  7629.901| 110.378|  10,354|
| |Taylor County|     0|  0.000|  0.000|    98| 16010.456| 116.694|   6,121|
| |Sac County|     0|  0.000|  0.000|    84|  8641.086| 44.087|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    84|  9453.072| 160.767|   8,886|
| |Page County|     0|  0.000|  0.000|    94|  6222.281| 217.496|  15,107|
| |Osceola County|     0|  0.000|  0.000|    83| 13930.849| 143.864|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972| 16.582|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    78|  7368.222| 26.990|  10,586|
| |Mills County|     0|  0.000|  0.000|    89|  5890.529| 94.551|  15,109|
| |Marion County|     0|  0.000|  0.000|   169|  5082.248| 90.217|  33,253|
| |Adams County|     0|  0.000|  0.000|    16|  4441.977|  0.000|   3,602|
| |Adair County|     0|  0.000|  0.000|    29|  4054.810| 179.770|   7,152|
| |Chickasaw County|     0|  0.000|  0.000|    54|  4525.266| 47.886|  11,933|
| |Jefferson County|     0|  0.000|  0.000|    83|  4536.759| 54.660|  18,295|
| |Ida County|     0|  0.000|  0.000|    29|  4227.405|  0.000|   6,860|
| |Howard County|     0|  0.000|  0.000|    49|  5350.513| 15.599|   9,158|
| |Harrison County|     0|  0.000|  0.000|   106|  7545.021| 111.853|  14,049|
| |Hardin County|     0|  0.000|  0.000|   178| 10566.307| 135.683|  16,846|
| |Decatur County|     0|  0.000|  0.000|    23|  2922.490| 36.304|   7,870|
| |Greene County|     0|  0.000|  0.000|    41|  4612.961| 48.219|   8,888|
| |Fremont County|     0|  0.000|  0.000|    42|  6034.483| 143.678|   6,960|
| |Fayette County|     0|  0.000|  0.000|    82|  4173.028| 36.350|  19,650|
| |Kossuth County|     0|  0.000|  0.000|    89|  6008.236| 115.728|  14,813|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   772| 172.797| N/A|34,578|  7739.600| N/A|4,467,673|
| |Jefferson County|   237| 309.094|  0.745| 7,984| 10412.686| 175.880| 766,757|
| |Fayette County|    47| 145.442|  0.442| 3,071|  9503.268| 165.336| 323,152|
| |Kenton County|    41| 245.512|  3.422| 1,402|  8395.310| 89.821| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   421|  9421.295| 57.544|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,097|  8212.246| 97.319| 133,581|
| |Graves County|    24| 644.019|  7.667|   558| 14973.434| 218.506|  37,266|
| |Logan County|    23| 848.646|  5.271|   327| 12065.530| 142.319|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,617| 19692.090| 228.965| 132,896|
| |Shelby County|    21| 428.362|  0.000|   770| 15706.593| 195.240|  49,024|
| |Adair County|    19| 989.480|  0.000|   203| 10571.815| 14.879|  19,202|
| |Butler County|    15| 1164.687|  0.000|   294| 22827.859| 33.277|  12,879|
| |Oldham County|    15| 224.554|  4.277|   620|  9281.576| 158.257|  66,799|
| |Jackson County|    14| 1050.341|  0.000|   150| 11253.657| 107.178|  13,329|
| |Campbell County|    13| 138.913|  0.000|   567|  6058.728| 76.326|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   101|  8312.757| 117.578|  12,150|
| |Muhlenberg County|    11| 359.219|  9.330|   620| 20246.881| 46.652|  30,622|
| |Grayson County|    11| 416.241|  0.000|   197|  7454.497| 113.520|  26,427|
| |Casey County|    10| 618.850|  0.000|   175| 10829.878| 229.859|  16,159|
| |Daviess County|     9| 88.660|  2.815|   765|  7536.129| 92.882| 101,511|
| |Christian County|     8| 113.538|  4.055|   500|  7096.124| 56.769|  70,461|
| |Knox County|     8| 256.863|  0.000|   232|  7449.029| 146.779|  31,145|
| |Ohio County|     8| 333.417| 11.908|   358| 14920.397| 113.124|  23,994|
| |Allen County|     8| 375.323|  0.000|   226| 10602.862| 60.320|  21,315|
| |Hardin County|     8| 72.099|  0.000|   604|  5443.501| 112.011| 110,958|
| |Simpson County|     7| 376.911|  0.000|   149|  8022.830| 84.613|  18,572|
| |Clark County|     7| 193.034|  0.000|   166|  4577.669| 55.153|  36,263|
| |Gallatin County|     7| 789.266|  0.000|    79|  8907.430|  0.000|   8,869|
| |Franklin County|     7| 137.279|  5.603|   296|  5804.946| 128.874|  50,991|
| |Grant County|     5| 199.450|  0.000|   115|  4587.339| 102.574|  25,069|
| |Clay County|     5| 251.244|  0.000|   150|  7537.310| 57.427|  19,901|
| |Bullitt County|     5| 61.217|  1.749|   363|  4444.390| 90.952|  81,676|
| |Laurel County|     5| 82.219|  2.349|   432|  7103.744| 138.598|  60,813|
| |Russell County|     5| 278.971|  0.000|   108|  6025.777| 103.618|  17,923|
| |Bell County|     4| 153.657| 10.976|   312| 11985.249| 230.486|  26,032|
| |Calloway County|     4| 102.561|  7.326|   230|  5897.285| 190.471|  39,001|
| |Lyon County|     4| 487.211|  0.000|    33|  4019.488| 52.201|   8,210|
| |McCracken County|     4| 61.145|  0.000|   366|  5594.790| 82.983|  65,418|
| |Pulaski County|     4| 61.558|  4.397|   279|  4293.695| 87.940|  64,979|
| |Boyd County|     3| 64.215|  0.000|   190|  4066.955| 73.389|  46,718|
| |Pike County|     3| 51.835|  0.000|   250|  4319.580| 76.518|  57,876|
| |Perry County|     3| 116.469|  0.000|   222|  8618.682| 210.753|  25,758|
| |Harlan County|     3| 115.340|  0.000|   231|  8881.200| 181.249|  26,010|
| |Henderson County|     3| 66.357|  0.000|   343|  7586.817| 75.837|  45,210|
| |Monroe County|     2| 187.793|  0.000|    94|  8826.291| 80.483|  10,650|
| |Metcalfe County|     2| 198.590|  0.000|    58|  5759.110| 113.480|  10,071|
| |Meade County|     2| 69.999|  0.000|    99|  3464.931| 84.998|  28,572|
| |Marshall County|     2| 64.309|  0.000|   137|  4405.145| 59.715|  31,100|
| |Nelson County|     2| 43.259|  0.000|   215|  4650.358| 86.518|  46,233|
| |Taylor County|     2| 77.613|  0.000|   113|  4385.114| 72.069|  25,769|
| |Floyd County|     2| 56.197|  4.014|    94|  2641.266| 52.183|  35,589|
| |Fulton County|     2| 335.064| 23.933|    79| 13235.048| 550.463|   5,969|
| |Green County|     2| 182.799|  0.000|    31|  2833.379| 13.057|  10,941|
| |Breckinridge County|     2| 97.671|  0.000|    67|  3271.964| 111.623|  20,477|
| |Barren County|     2| 45.199|  0.000|   362|  8180.976| 122.682|  44,249|
| |Henry County|     2| 124.023|  0.000|   121|  7503.411| 283.482|  16,126|
| |Carroll County|     2| 188.129|  0.000|   158| 14862.195| 241.880|  10,631|
| |Crittenden County|     1| 113.559|  0.000|    30|  3406.768| 64.891|   8,806|
| |Clinton County|     1| 97.867| 13.981|    29|  2838.129| 83.886|  10,218|
| |Carter County|     1| 37.318|  0.000|   101|  3769.079| 31.987|  26,797|
| |Carlisle County|     1| 210.084|  0.000|    42|  8823.529| 480.192|   4,760|
| |Bourbon County|     1| 50.536|  0.000|    78|  3941.783| 64.974|  19,788|
| |Bath County|     1| 80.000|  0.000|    37|  2960.000| 34.286|  12,500|
| |Anderson County|     1| 43.962|  0.000|    83|  3648.833| 56.522|  22,747|
| |Greenup County|     1| 28.492|  0.000|   110|  3134.082| 89.545|  35,098|
| |Whitley County|     1| 27.576|  0.000|   167|  4605.118| 133.938|  36,264|
| |Webster County|     1| 77.268|  0.000|    88|  6799.567| 99.344|  12,942|
| |Mason County|     1| 58.582|  0.000|    54|  3163.445|  8.369|  17,070|
| |Madison County|     1| 10.754|  0.000|   492|  5291.062| 172.067|  92,987|
| |McLean County|     1| 108.613|  0.000|    42|  4561.746| 62.065|   9,207|
| |Livingston County|     1| 108.767|  0.000|    33|  3589.297| 15.538|   9,194|
| |Lincoln County|     1| 40.735|  0.000|   102|  4154.955| 23.277|  24,549|
| |Larue County|     1| 69.454|  0.000|    55|  3819.975| 79.376|  14,398|
| |Knott County|     1| 67.540|  0.000|    54|  3647.170| 135.080|  14,806|
| |Fleming County|     0|  0.000|  0.000|    58|  3977.779| 39.190|  14,581|
| |Estill County|     0|  0.000|  0.000|    21|  1488.728| 91.147|  14,106|
| |Elliott County|     0|  0.000|  0.000|    11|  1463.350| 76.018|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    49|  7408.527| 259.190|   6,614|
| |Woodford County|     0|  0.000|  0.000|   155|  5797.860| 149.622|  26,734|
| |Jessamine County|     0|  0.000|  0.000|   340|  6282.916| 163.673|  54,115|
| |Hickman County|     0|  0.000|  0.000|    42|  9589.041| 293.542|   4,380|
| |Hart County|     0|  0.000|  0.000|    96|  5043.341| 142.594|  19,035|
| |Harrison County|     0|  0.000|  0.000|   121|  6406.862| 45.385|  18,886|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 81.895|   8,722|
| |Union County|     0|  0.000|  0.000|    65|  4519.853| 119.205|  14,381|
| |Trigg County|     0|  0.000|  0.000|    53|  3617.501| 48.753|  14,651|
| |Todd County|     0|  0.000|  0.000|    35|  2846.917| 23.240|  12,294|
| |Spencer County|     0|  0.000|  0.000|   113|  5839.491| 125.501|  19,351|
| |Scott County|     0|  0.000|  0.000|   373|  6543.400| 137.835|  57,004|
| |Rowan County|     0|  0.000|  0.000|    69|  2820.932|  5.840|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    69|  4132.974| 77.012|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    53|  4288.373| 104.031|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    45|  3084.304| 88.123|  14,590|
| |Owsley County|     0|  0.000|  0.000|    13|  2944.507| 129.429|   4,415|
| |Owen County|     0|  0.000|  0.000|    48|  4403.266| 78.630|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    31|  2329.251| 32.202|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   120|  4261.818| 50.736|  28,157|
| |Mercer County|     0|  0.000|  0.000|    82|  3738.659| 58.620|  21,933|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Martin County|     0|  0.000|  0.000|    36|  3215.721| 89.326|  11,195|
| |Marion County|     0|  0.000|  0.000|   121|  6278.213| 140.834|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    39|  3206.973| 234.943|  12,161|
| |McCreary County|     0|  0.000|  0.000|    38|  2205.328| 24.872|  17,231|
| |Lewis County|     0|  0.000|  0.000|    40|  3013.183| 75.330|  13,275|
| |Letcher County|     0|  0.000|  0.000|    60|  2783.835| 72.910|  21,553|
| |Trimble County|     0|  0.000|  0.000|    33|  3895.644| 16.864|   8,471|
| |Washington County|     0|  0.000|  0.000|    80|  6614.303| 248.036|  12,095|
| |Wayne County|     0|  0.000|  0.000|    54|  2655.781| 28.104|  20,333|
| |Johnson County|     0|  0.000|  0.000|    50|  2253.470| 83.700|  22,188|
| |Lawrence County|     0|  0.000|  0.000|    36|  2350.330| 27.980|  15,317|
| |Lee County|     0|  0.000|  0.000|     7|   945.563| 77.189|   7,403|
| |Leslie County|     0|  0.000|  0.000|    30|  3037.360| 57.854|   9,877|
| |Caldwell County|     0|  0.000|  0.000|    52|  4079.391| 33.621|  12,747|
| |Breathitt County|     0|  0.000|  0.000|    28|  2216.944| 33.933|  12,630|
| |Bracken County|     0|  0.000|  0.000|    33|  3974.467| 68.822|   8,303|
| |Boyle County|     0|  0.000|  0.000|   155|  5156.354| 114.058|  30,060|
| |Ballard County|     0|  0.000|  0.000|    36|  4563.895| 108.664|   7,888|
| |Wolfe County|     0|  0.000|  0.000|    14|  1956.127| 99.802|   7,157|
| |Garrard County|     0|  0.000|  0.000|    75|  4245.443| 64.692|  17,666|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   681| 324.776| N/A|20,813|  9925.941| N/A|2,096,829|
| |McKinley County|   224| 3138.706|  8.007| 4,043| 56650.833| 88.076|  71,367|
| |San Juan County|   183| 1476.306|  2.305| 3,040| 24524.436| 47.251| 123,958|
| |Bernalillo County|   132| 194.369|  1.893| 5,089|  7493.510| 60.793| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,126|  7673.018| 42.833| 146,748|
| |Dona Ana County|    30| 137.492|  4.583| 2,417| 11077.247| 156.479| 218,195|
| |Cibola County|    18| 674.789|  5.355|   362| 13570.759| 155.309|  26,675|
| |Otero County|    10| 148.170|  0.000|   201|  2978.219| 38.101|  67,490|
| |Rio Arriba County|     7| 179.851| 11.011|   316|  8119.010| 80.750|  38,921|
| |Socorro County|     6| 360.642|  0.000|    73|  4387.810|  0.000|  16,637|
| |Chaves County|     6| 92.858|  2.211|   435|  6732.183| 192.348|  64,615|
| |Valencia County|     4| 52.159|  0.000|   406|  5294.179| 91.279|  76,688|
| |Lea County|     4| 56.283|  0.000|   751| 10567.047| 251.261|  71,070|
| |Eddy County|     4| 68.423|  0.000|   293|  5011.974| 112.409|  58,460|
| |Luna County|     3| 126.534|  0.000|   247| 10417.985| 132.560|  23,709|
| |Santa Fe County|     3| 19.952|  0.000|   637|  4236.555| 57.957| 150,358|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824| 21.166|  26,998|
| |Union County|     2| 492.732| 70.390|    29|  7144.617| 70.390|   4,059|
| |Curry County|     2| 40.855|  0.000|   541| 11051.191| 239.292|  48,954|
| |Lincoln County|     2| 102.187|  7.299|   125|  6386.675| 189.775|  19,572|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 59.818|  11,941|
| |Quay County|     1| 121.168|  0.000|    34|  4119.714| 51.929|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   161|  8702.703| 162.162|  18,500|
| |Taos County|     1| 30.560|  0.000|   108|  3300.431| 52.388|  32,723|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411| 18.480|  15,461|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |San Miguel County|     0|  0.000|  0.000|    43|  1576.420| 10.475|  27,277|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Guadalupe County|     0|  0.000|  0.000|    31|  7209.302|  0.000|   4,300|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 68.060|   4,198|
| |Los Alamos County|     0|  0.000|  0.000|    21|  1084.207|  7.376|  19,369|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Sierra County|     0|  0.000|  0.000|    32|  2965.434| 39.716|  10,791|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   603| 152.389| N/A|43,070| 10884.588| N/A|3,956,971|
| |Oklahoma County|   112| 140.450|  2.508|10,424| 13071.928| 216.767| 797,434|
| |Tulsa County|   107| 164.223|  1.316|10,389| 15945.005| 307.617| 651,552|
| |Cleveland County|    55| 193.652|  3.018| 2,967| 10446.668| 158.443| 284,014|
| |Washington County|    39| 756.885|  0.000|   623| 12090.749| 158.031|  51,527|
| |McCurtain County|    28| 852.827| 13.053|   856| 26072.125| 165.344|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   848| 10431.916| 214.403|  81,289|
| |Delaware County|    19| 441.768|  0.000|   424|  9858.402| 83.039|  43,009|
| |Rogers County|    16| 173.050|  3.090|   958| 10361.349| 278.116|  92,459|
| |Caddo County|    16| 556.290|  9.934|   413| 14359.224| 268.211|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   503|  7397.385| 147.065|  67,997|
| |Creek County|    14| 195.744|  1.997|   588|  8221.247| 185.757|  71,522|
| |Kay County|    11| 252.653|  3.281|   242|  5558.363| 91.874|  43,538|
| |Osage County|    11| 234.227|  0.000|   404|  8602.517| 133.844|  46,963|
| |Comanche County|    10| 82.816|  0.000|   803|  6650.159| 48.507| 120,749|
| |Pottawatomie County|     9| 123.981|  3.936|   442|  6088.825| 116.109|  72,592|
| |Greer County|     8| 1400.560| 25.010|    83| 14530.812| 75.030|   5,712|
| |Grady County|     7| 125.372|  2.559|   437|  7826.772| 79.317|  55,834|
| |Texas County|     7| 350.298|  0.000| 1,055| 52794.876| 150.128|  19,983|
| |Canadian County|     7| 47.200|  1.927| 1,194|  8050.922| 130.040| 148,306|
| |Adair County|     6| 270.343|  6.437|   339| 15274.398| 321.837|  22,194|
| |Mayes County|     6| 145.985|  0.000|   313|  7615.572| 107.751|  41,100|
| |Jackson County|     5| 203.832|  5.824|   518| 21117.000| 232.951|  24,530|
| |Garfield County|     5| 81.892|  2.340|   447|  7321.148| 196.541|  61,056|
| |Seminole County|     5| 206.118|  0.000|   234|  9646.302| 265.008|  24,258|
| |Payne County|     4| 48.909|  1.747|   721|  8815.905| 104.806|  81,784|
| |Sequoyah County|     4| 96.226|  0.000|   333|  8010.777| 278.367|  41,569|
| |McClain County|     4| 98.829|  0.000|   430| 10624.104| 144.714|  40,474|
| |Carter County|     4| 83.141|  2.969|   337|  7004.635| 103.926|  48,111|
| |Garvin County|     4| 144.347|  0.000|   225|  8119.519| 118.571|  27,711|
| |Stephens County|     3| 69.536|  3.311|   198|  4589.389| 79.470|  43,143|
| |Pittsburg County|     3| 68.722|  0.000|   339|  7765.611| 484.328|  43,654|
| |Pawnee County|     3| 183.195|  0.000|   136|  8304.836| 122.130|  16,376|
| |Ottawa County|     3| 96.379|  4.589|   368| 11822.533| 142.274|  31,127|
| |Okmulgee County|     3| 77.993|  0.000|   466| 12114.910| 267.405|  38,465|
| |Pontotoc County|     2| 52.241|  0.000|   198|  5171.873| 100.751|  38,284|
| |Cherokee County|     2| 41.104|  2.936|   421|  8652.404| 293.600|  48,657|
| |Cotton County|     2| 352.983|  0.000|    18|  3176.844| 25.213|   5,666|
| |Hughes County|     2| 150.614| 10.758|   134| 10091.121| 290.469|  13,279|
| |Lincoln County|     2| 57.344|  0.000|   165|  4730.911| 163.841|  34,877|
| |Noble County|     2| 179.678|  0.000|    83|  7456.653| 77.005|  11,131|
| |Beckham County|     1| 45.748|  0.000|    53|  2424.631| 65.354|  21,859|
| |Major County|     1| 131.079|  0.000|    34|  4456.678| 168.530|   7,629|
| |McIntosh County|     1| 51.031|  0.000|   181|  9236.579| 218.704|  19,596|
| |Logan County|     1| 20.829|  0.000|   212|  4415.655| 95.216|  48,011|
| |Nowata County|     1| 99.246|  0.000|    57|  5657.007| 28.356|  10,076|
| |Tillman County|     1| 137.931|  0.000|    58|  8000.000| 59.113|   7,250|
| |Roger Mills County|     1| 279.096| 39.871|     8|  2232.766|  0.000|   3,583|
| |Marshall County|     1| 59.063|  8.438|   107|  6319.768| 84.376|  16,931|
| |Choctaw County|     1| 68.157|  0.000|   183| 12472.737| 184.998|  14,672|
| |Kiowa County|     1| 114.837|  0.000|    27|  3100.597|  0.000|   8,708|
| |Okfuskee County|     1| 83.382| 11.912|    63|  5253.064| 95.294|  11,993|
| |Latimer County|     1| 99.275|  0.000|    87|  8636.950| 283.644|  10,073|
| |Le Flore County|     1| 20.059|  0.000|   326|  6539.225| 277.960|  49,853|
| |Bryan County|     1| 20.836|  0.000|   453|  9438.483| 214.308|  47,995|
| |Pushmataha County|     0|  0.000|  0.000|   109|  9823.360| 102.997|  11,096|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Atoka County|     0|  0.000|  0.000|    70|  5087.949| 83.069|  13,758|
| |Washita County|     0|  0.000|  0.000|    27|  2473.433| 39.261|  10,916|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 81.233|   8,793|
| |Woodward County|     0|  0.000|  0.000|    38|  1880.164| 42.410|  20,211|
| |Grant County|     0|  0.000|  0.000|    15|  3461.805| 131.878|   4,333|
| |Harper County|     0|  0.000|  0.000|     9|  2440.347|  0.000|   3,688|
| |Haskell County|     0|  0.000|  0.000|    57|  4514.136| 192.332|  12,627|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 71.405|   6,002|
| |Johnston County|     0|  0.000|  0.000|    46|  4149.752| 77.325|  11,085|
| |Kingfisher County|     0|  0.000|  0.000|   129|  8182.683| 199.357|  15,765|
| |Love County|     0|  0.000|  0.000|    75|  7314.932| 153.265|  10,253|
| |Murray County|     0|  0.000|  0.000|    71|  5045.122| 121.814|  14,073|
| |Blaine County|     0|  0.000|  0.000|    41|  4348.287|  0.000|   9,429|
| |Beaver County|     0|  0.000|  0.000|    36|  6778.384|  0.000|   5,311|
| |Harmon County|     0|  0.000|  0.000|    27| 10177.158| 161.542|   2,653|
| |Cimarron County|     0|  0.000|  0.000|     1|   467.946|  0.000|   2,137|
| |Coal County|     0|  0.000|  0.000|    36|  6551.410| 259.977|   5,495|
| |Craig County|     0|  0.000|  0.000|    82|  5798.331| 101.016|  14,142|
| |Custer County|     0|  0.000|  0.000|   206|  7102.714| 78.810|  29,003|
| |Dewey County|     0|  0.000|  0.000|     9|  1840.114| 58.416|   4,891|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   590| 835.991| N/A|12,653| 17928.470| N/A| 705,749|
| |District of Columbia|   590| 835.991|  1.215|12,653| 17928.470| 120.642| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   590| 605.896| N/A|15,259| 15670.121| N/A| 973,764|
| |New Castle County|   291| 520.803|  1.023| 7,161| 12816.039| 81.303| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,821| 24852.172| 116.494| 234,225|
| |Kent County|   107| 591.860|  0.000| 2,277| 12595.002| 74.279| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   535| 177.281| N/A|47,039| 15587.162| N/A|3,017,804|
| |Pulaski County|    85| 216.886|  2.916| 5,480| 13982.766| 246.776| 391,911|
| |Washington County|    51| 213.222|  2.986| 6,268| 26205.438| 188.735| 239,187|
| |Benton County|    43| 154.044|  2.047| 4,755| 17034.402| 133.061| 279,141|
| |Jefferson County|    40| 598.587|  4.276| 1,519| 22731.354| 436.114|  66,824|
| |Crittenden County|    21| 437.911|  8.937| 1,351| 28172.245| 476.637|  47,955|
| |Sebastian County|    20| 156.461|  6.705| 2,133| 16686.616| 457.091| 127,827|
| |Union County|    17| 439.481|  3.693|   478| 12357.169| 177.270|  38,682|
| |Yell County|    14| 656.014|  0.000| 1,065| 49903.941| 354.783|  21,341|
| |Mississippi County|    14| 344.395| 14.057|   982| 24156.847| 808.274|  40,651|
| |Lincoln County|    12| 921.376| 10.969| 1,212| 93058.968| 482.625|  13,024|
| |Garland County|    12| 120.741|  7.187|   992|  9981.285| 222.797|  99,386|
| |Craighead County|    12| 108.763|  1.295| 1,336| 12108.908| 300.392| 110,332|
| |Hot Spring County|    11| 325.723| 12.691| 1,530| 45305.143| 334.184|  33,771|
| |Sevier County|    10| 587.993|  0.000|   988| 58093.726| 461.995|  17,007|
| |Pope County|    10| 156.074|  2.230| 1,306| 20383.319| 294.312|  64,072|
| |Nevada County|     9| 1090.645|  0.000|   137| 16602.036| 138.495|   8,252|
| |Columbia County|     9| 383.681| 18.271|   214|  9123.076| 170.525|  23,457|
| |Lawrence County|     9| 548.580|  0.000|   209| 12739.242| 235.106|  16,406|
| |Chicot County|     8| 790.670| 28.238|   729| 72049.812| 2922.656|  10,118|
| |Lee County|     8| 903.240| 32.259|   893| 100824.207| 129.034|   8,857|
| |Carroll County|     7| 246.653|  5.034|   353| 12438.337| 80.540|  28,380|
| |Phillips County|     7| 393.657|  8.034|   311| 17489.596| 305.285|  17,782|
| |Newton County|     6| 773.894| 55.278|   102| 13156.198| 165.834|   7,753|
| |Saline County|     6| 49.005|  2.334| 1,017|  8306.313| 173.850| 122,437|
| |Faulkner County|     6| 47.616|  1.134| 1,290| 10237.526| 113.372| 126,007|
| |Ashley County|     5| 254.362|  7.267|   322| 16380.933| 610.470|  19,657|
| |Cleburne County|     5| 200.650|  0.000|   194|  7785.224| 85.993|  24,919|
| |Miller County|     5| 115.588|  3.303|   508| 11743.764| 168.429|  43,257|
| |Sharp County|     5| 286.664|  0.000|   111|  6363.949| 73.714|  17,442|
| |Crawford County|     4| 63.234|  2.258|   620|  9801.287| 221.319|  63,257|
| |Clay County|     4| 274.895|  0.000|   130|  8934.094| 245.442|  14,551|
| |Cross County|     4| 243.620| 26.102|   195| 11876.485| 287.124|  16,419|
| |St. Francis County|     3| 120.029|  0.000| 1,193| 47731.456| 434.390|  24,994|
| |Conway County|     3| 143.913|  0.000|   150|  7195.625| 109.648|  20,846|
| |Howard County|     3| 227.238| 10.821|   336| 25450.689| 454.477|  13,202|
| |Poinsett County|     3| 127.508|  0.000|   269| 11433.186| 686.113|  23,528|
| |Bradley County|     3| 278.733|  0.000|   186| 17281.427| 584.011|  10,763|
| |Randolph County|     3| 167.056|  7.955|   209| 11638.267| 310.248|  17,958|
| |Drew County|     3| 164.663|  7.841|   198| 10867.775| 337.168|  18,219|
| |Johnson County|     2| 75.250| 10.750|   663| 24945.444| 247.251|  26,578|
| |Ouachita County|     2| 85.536|  6.110|    98|  4191.258| 134.414|  23,382|
| |Lonoke County|     2| 27.282|  0.000|   508|  6929.572| 179.280|  73,309|
| |Madison County|     2| 120.656|  8.618|   270| 16288.610| 137.893|  16,576|
| |Cleveland County|     2| 251.383|  0.000|    97| 12192.056| 538.677|   7,956|
| |Franklin County|     2| 112.899|  0.000|   126|  7112.616| 169.348|  17,715|
| |Desha County|     2| 176.041|  0.000|   192| 16899.921| 603.569|  11,361|
| |White County|     2| 25.396|  0.000|   318|  4037.941| 116.095|  78,753|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385| 25.903|  16,545|
| |Hempstead County|     2| 92.885|  0.000|   239| 11099.758| 212.309|  21,532|
| |Lafayette County|     2| 301.932|  0.000|    53|  8001.208| 86.266|   6,624|
| |Logan County|     1| 46.585|  6.655|   252| 11739.495| 738.710|  21,466|
| |Stone County|     1| 79.962|  0.000|    67|  5357.428| 171.346|  12,506|
| |Little River County|     1| 81.573|  0.000|   180| 14683.090| 326.291|  12,259|
| |Clark County|     1| 44.803|  6.400|   177|  7930.108| 160.010|  22,320|
| |Polk County|     1| 50.090|  0.000|   140|  7012.623| 85.869|  19,964|
| |Boone County|     1| 26.715|  0.000|   208|  5556.743| 175.556|  37,432|
| |Montgomery County|     1| 111.284| 15.898|    34|  3783.663| 143.080|   8,986|
| |Pike County|     1| 93.301|  0.000|   101|  9423.400| 319.889|  10,718|
| |Greene County|     1| 22.063|  0.000|   473| 10435.742| 359.310|  45,325|
| |Izard County|     1| 73.373|  0.000|    52|  3815.394| 83.855|  13,629|
| |Jackson County|     1| 59.812|  0.000|   109|  6519.529| 435.775|  16,719|
| |Independence County|     1| 26.438|  3.777|   492| 13007.270| 555.188|  37,825|
| |Arkansas County|     1| 57.189|  8.170|   212| 12123.985| 147.056|  17,486|
| |Marion County|     0|  0.000|  0.000|    25|  1497.544| 17.115|  16,694|
| |Monroe County|     0|  0.000|  0.000|    58|  8655.425| 149.231|   6,701|
| |Perry County|     0|  0.000|  0.000|    50|  4782.401| 13.664|  10,455|
| |Calhoun County|     0|  0.000|  0.000|    16|  3083.446| 82.592|   5,189|
| |Woodruff County|     0|  0.000|  0.000|    21|  3322.785| 45.208|   6,320|
| |Prairie County|     0|  0.000|  0.000|    90| 11163.483| 478.435|   8,062|
| |Scott County|     0|  0.000|  0.000|    58|  5641.475| 236.219|  10,281|
| |Searcy County|     0|  0.000|  0.000|    29|  3679.736| 72.507|   7,881|
| |Baxter County|     0|  0.000|  0.000|    71|  1693.218| 37.476|  41,932|
| |Fulton County|     0|  0.000|  0.000|    40|  3205.899| 148.845|  12,477|
| |Dallas County|     0|  0.000|  0.000|    61|  8703.096| 101.910|   7,009|
| |Grant County|     0|  0.000|  0.000|   135|  7391.185| 86.035|  18,265|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,812|  5009.888| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.343| 3,842|  9212.877| 29.803| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,688|  5449.222| 27.209| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   464|  3064.911|  5.662| 151,391|
| |Strafford County|    13| 99.515|  0.000|   353|  2702.227| 27.339| 130,633|
| |Belknap County|     4| 65.250|  0.000|   115|  1875.928| 23.303|  61,303|
| |Cheshire County|     3| 39.430|  1.878|    97|  1274.890| 13.143|  76,085|
| |Grafton County|     1| 11.125|  0.000|   103|  1145.896|  0.000|  89,886|
| |Carroll County|     1| 20.446|  0.000|    93|  1901.452| 11.683|  48,910|
| |Sullivan County|     1| 23.177|  0.000|    40|   927.085|  0.000|  43,146|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   379| 130.092| N/A|30,463| 10456.477| N/A|2,913,314|
| |Johnson County|   103| 170.982|  1.186| 5,643|  9367.514| 149.165| 602,401|
| |Wyandotte County|    99| 598.444|  3.454| 4,864| 29402.342| 424.006| 165,429|
| |Sedgwick County|    44| 85.264|  1.384| 4,818|  9336.449| 182.709| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,509|  8531.449| 96.921| 176,875|
| |Lyon County|    13| 391.625|  8.607|   697| 20997.138| 228.089|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,783| 48893.520| 180.202|  36,467|
| |Coffey County|     8| 978.115|  0.000|    67|  8191.710| 34.933|   8,179|
| |Leavenworth County|     8| 97.850|  0.000| 1,459| 17845.348| 117.070|  81,758|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 109.176|   5,234|
| |Ford County|     8| 237.961|  0.000| 2,069| 61542.580| 182.720|  33,619|
| |Douglas County|     5| 40.897|  2.337|   714|  5840.061| 74.783| 122,259|
| |Riley County|     5| 67.356|  0.000|   477|  6425.800| 53.885|  74,232|
| |Montgomery County|     5| 157.089|  0.000|   164|  5152.534| 53.859|  31,829|
| |Saline County|     5| 92.210|  0.000|   372|  6860.431| 84.306|  54,224|
| |Seward County|     4| 186.672|  0.000| 1,220| 56934.852| 213.339|  21,428|
| |Barton County|     3| 116.374|  0.000|   139|  5391.986| 138.540|  25,779|
| |Sumner County|     3| 131.372|  0.000|    99|  4335.260| 12.512|  22,836|
| |Bourbon County|     2| 137.608|  9.829|    73|  5022.705| 78.633|  14,534|
| |Cowley County|     2| 57.293|  0.000|   165|  4726.710| 57.293|  34,908|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 53.558|   8,002|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Grant County|     2| 279.720|  0.000|   110| 15384.615| 319.680|   7,150|
| |Geary County|     2| 63.151|  0.000|   140|  4420.587| 54.130|  31,670|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stanton County|     1| 498.504|  0.000|    18|  8973.081| 142.430|   2,006|
| |Stafford County|     1| 240.616| 34.374|     3|   721.848|  0.000|   4,156|
| |Franklin County|     1| 39.148|  0.000|   178|  6968.368| 162.185|  25,544|
| |Ellis County|     1| 35.023|  0.000|   141|  4938.185| 65.042|  28,553|
| |Harvey County|     1| 29.045|  0.000|   194|  5634.785| 153.525|  34,429|
| |Jackson County|     1| 75.924|  0.000|   146| 11084.959| 21.693|  13,171|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199| 71.644|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   118|  5918.050| 322.412|  19,939|
| |Kearny County|     1| 260.552|  0.000|    59| 15372.590| 74.444|   3,838|
| |Butler County|     1| 14.945|  2.135|   255|  3811.033| 117.427|  66,911|
| |Reno County|     1| 16.130|  0.000|   272|  4387.238| 122.124|  61,998|
| |Nemaha County|     1| 97.742| 13.963|    49|  4789.366| 27.926|  10,231|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 72.126|  11,884|
| |McPherson County|     1| 35.036|  0.000|   142|  4975.124| 65.067|  28,542|
| |Dickinson County|     1| 54.154|  0.000|    47|  2545.218| 54.154|  18,466|
| |Crawford County|     1| 25.761|  0.000|   380|  9789.273| 44.162|  38,818|
| |Morris County|     0|  0.000|  0.000|    11|  1957.295| 50.839|   5,620|
| |Wabaunsee County|     0|  0.000|  0.000|    42|  6059.732| 61.834|   6,931|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Neosho County|     0|  0.000|  0.000|    58|  3623.415| 71.397|  16,007|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818| 51.948|   2,750|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502| 154.074|   4,636|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Thomas County|     0|  0.000|  0.000|    36|  4629.034| 73.477|   7,777|
| |Stevens County|     0|  0.000|  0.000|    45|  8204.193| 52.090|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    15|  2535.068| 24.144|   5,917|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Scott County|     0|  0.000|  0.000|    47|  9744.972| 562.780|   4,823|
| |Russell County|     0|  0.000|  0.000|    13|  1896.149| 62.510|   6,856|
| |Rush County|     0|  0.000|  0.000|     6|  1976.285| 47.054|   3,036|
| |Rooks County|     0|  0.000|  0.000|    17|  3455.285| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    37|  3879.627| 149.793|   9,537|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    33|  3601.048|  0.000|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   107|  4388.303| 29.294|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     7|  1091.363|  0.000|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    34|  5960.729| 100.180|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Osage County|     0|  0.000|  0.000|    40|  2507.994| 17.914|  15,949|
| |Atchison County|     0|  0.000|  0.000|    64|  3981.833| 26.664|  16,073|
| |Anderson County|     0|  0.000|  0.000|    29|  3690.506| 36.360|   7,858|
| |Marshall County|     0|  0.000|  0.000|     9|   927.166|  0.000|   9,707|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 75.188|   7,600|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Woodson County|     0|  0.000|  0.000|    11|  3505.417|  0.000|   3,138|
| |Wilson County|     0|  0.000|  0.000|    11|  1290.323| 50.272|   8,525|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683| 67.417|   2,119|
| |Mitchell County|     0|  0.000|  0.000|    27|  4515.805|  0.000|   5,979|
| |Miami County|     0|  0.000|  0.000|   133|  3884.686| 66.762|  34,237|
| |Meade County|     0|  0.000|  0.000|    44| 10909.993| 177.110|   4,033|
| |Allen County|     0|  0.000|  0.000|    15|  1212.709| 11.550|  12,369|
| |Comanche County|     0|  0.000|  0.000|     5|  2941.176| 168.067|   1,700|
| |Cloud County|     0|  0.000|  0.000|    32|  3642.158| 48.779|   8,786|
| |Cheyenne County|     0|  0.000|  0.000|     3|  1129.093| 53.766|   2,657|
| |Chautauqua County|     0|  0.000|  0.000|     5|  1538.462|  0.000|   3,250|
| |Chase County|     0|  0.000|  0.000|    42| 15861.027| 1942.167|   2,648|
| |Brown County|     0|  0.000|  0.000|    37|  3868.674| 74.685|   9,564|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Linn County|     0|  0.000|  0.000|    35|  3607.132| 73.615|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Labette County|     0|  0.000|  0.000|   133|  6779.488| 189.330|  19,618|
| |Kiowa County|     0|  0.000|  0.000|     7|  2828.283| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    17|  2376.957| 159.795|   7,152|
| |Jewell County|     0|  0.000|  0.000|    11|  3820.771| 99.241|   2,879|
| |Jefferson County|     0|  0.000|  0.000|    76|  3990.968| 127.531|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Harper County|     0|  0.000|  0.000|    10|  1839.588| 52.560|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    37| 14572.666|  0.000|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    20|  3343.363| 23.881|   5,982|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Gray County|     0|  0.000|  0.000|    77| 12859.051| 143.143|   5,988|
| |Graham County|     0|  0.000|  0.000|    16|  6446.414|  0.000|   2,482|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176| 162.584|   2,636|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495| 70.235|   6,102|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   355| 84.168| N/A|21,010|  4981.344| N/A|4,217,737|
| |Multnomah County|    94| 115.642|  0.351| 4,849|  5965.394| 78.383| 812,855|
| |Marion County|    70| 201.255|  1.232| 2,883|  8288.818| 110.485| 347,818|
| |Clackamas County|    40| 95.651|  1.366| 1,523|  3641.911| 49.875| 418,187|
| |Umatilla County|    28| 359.205|  7.331| 2,251| 28877.486| 502.153|  77,950|
| |Washington County|    25| 41.556|  0.475| 3,047|  5064.894| 62.691| 601,592|
| |Malheur County|    14| 457.950| 23.365|   768| 25121.848| 490.661|  30,571|
| |Yamhill County|    13| 121.382|  2.668|   450|  4201.681| 133.387| 107,100|
| |Polk County|    12| 139.397|  0.000|   313|  3635.941| 44.806|  86,085|
| |Linn County|    10| 77.072|  0.000|   277|  2134.891| 36.334| 129,749|
| |Deschutes County|    10| 50.584|  1.445|   596|  3014.791| 47.693| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   414|  8286.298| 65.764|  49,962|
| |Benton County|     6| 64.479|  0.000|   169|  1816.169| 23.028|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   355| 14396.950| 301.264|  24,658|
| |Morrow County|     3| 258.554| 24.624|   354| 30509.351| 714.101|  11,603|
| |Lane County|     3|  7.852|  0.000|   579|  1515.441| 25.426| 382,067|
| |Wasco County|     3| 112.435|  0.000|   189|  7083.427| 165.976|  26,682|
| |Jackson County|     2|  9.052|  0.647|   461|  2086.502| 58.838| 220,944|
| |Josephine County|     2| 22.861|  1.633|   114|  1303.051| 17.962|  87,487|
| |Klamath County|     2| 29.309|  2.094|   201|  2945.573| 14.655|  68,238|
| |Union County|     2| 74.530|  0.000|   394| 14682.318| 31.941|  26,835|
| |Wallowa County|     1| 138.735|  0.000|    19|  2635.960|  0.000|   7,208|
| |Crook County|     1| 40.977|  0.000|    47|  1925.914| 23.415|  24,404|
| |Douglas County|     1|  9.011|  0.000|   150|  1351.595| 28.319| 110,980|
| |Hood River County|     0|  0.000|  0.000|   184|  7869.301| 116.084|  23,382|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 240.770|   1,780|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582| 52.840|  27,036|
| |Harney County|     0|  0.000|  0.000|    10|  1352.631| 38.647|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|
| |Baker County|     0|  0.000|  0.000|    38|  2356.735| 70.879|  16,124|
| |Clatsop County|     0|  0.000|  0.000|    85|  2113.166| 24.861|  40,224|
| |Columbia County|     0|  0.000|  0.000|    94|  1795.469| 43.659|  52,354|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137| 15.507|  64,487|
| |Curry County|     0|  0.000|  0.000|    15|   654.308|  6.232|  22,925|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   345| 178.349| N/A|28,106| 14529.510| N/A|1,934,408|
| |Douglas County|   132| 231.041|  0.250|11,190| 19585.981| 212.538| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,741| 28376.770| 76.839|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,924| 96075.102| 164.072|  20,026|
| |Lancaster County|    17| 53.277|  0.895| 3,269| 10244.759| 96.704| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    99| 10617.761| 61.286|   9,324|
| |Adams County|    11| 350.732|  0.000|   353| 11255.301| 59.214|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,238| 11955.384| 175.523| 187,196|
| |Dawson County|     9| 381.437|  0.000|   956| 40517.059| 78.709|  23,595|
| |Dodge County|     9| 246.137|  3.907|   799| 21851.497| 160.184|  36,565|
| |Perkins County|     7| 2421.308| 296.487|    19|  6572.120| 197.658|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   301|  8450.783| 56.151|  35,618|
| |Madison County|     5| 142.454|  0.000|   449| 12792.387| 138.384|  35,099|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747|  0.000|   6,445|
| |Thurston County|     4| 553.710|  0.000|   205| 28377.630| 79.101|   7,224|
| |Gage County|     4| 185.934|  0.000|    89|  4137.033| 53.124|  21,513|
| |Colfax County|     4| 373.518|  0.000|   701| 65458.960| 120.059|  10,709|
| |Custer County|     4| 371.161|  0.000|    45|  4175.559| 26.511|  10,777|
| |Platte County|     3| 89.633|  0.000|   792| 23662.982| 119.510|  33,470|
| |Cass County|     2| 76.196|  5.443|   176|  6705.273| 108.852|  26,248|
| |Dixon County|     2| 354.862|  0.000|    58| 10290.987| 50.695|   5,636|
| |Saunders County|     2| 92.687|  0.000|   156|  7229.586| 185.374|  21,578|
| |Lincoln County|     2| 57.284|  0.000|   109|  3121.957| 61.375|  34,914|
| |Saline County|     2| 140.607|  0.000|   595| 41830.709| 140.607|  14,224|
| |Richardson County|     1| 127.146|  0.000|    22|  2797.203| 36.327|   7,865|
| |Seward County|     1| 57.857|  0.000|   118|  6827.123| 190.101|  17,284|
| |Washington County|     1| 48.242|  0.000|   118|  5692.508| 96.483|  20,729|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Fillmore County|     1| 183.083|  0.000|    24|  4393.995| 26.155|   5,462|
| |Buffalo County|     1| 20.137|  0.000|   406|  8175.759| 210.004|  49,659|
| |Antelope County|     1| 158.781|  0.000|    19|  3016.831| 22.683|   6,298|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827| 79.631|   1,794|
| |Franklin County|     0|  0.000|  0.000|    12|  4028.197| 143.864|   2,979|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 33.265|   8,589|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|
| |Cuming County|     0|  0.000|  0.000|    67|  7574.045| 161.493|   8,846|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 69.091|   6,203|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Banner County|     0|  0.000|  0.000|     3|  4026.846| 191.755|     745|
| |Chase County|     0|  0.000|  0.000|     6|  1529.052|  0.000|   3,924|
| |Cedar County|     0|  0.000|  0.000|    22|  2618.424| 17.003|   8,402|
| |Butler County|     0|  0.000|  0.000|    60|  7485.030| 71.286|   8,016|
| |Burt County|     0|  0.000|  0.000|    31|  4799.505| 199.058|   6,459|
| |Boyd County|     0|  0.000|  0.000|     4|  2084.419| 223.331|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    12|  1112.863| 13.248|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832| 27.515|   5,192|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 121.271|   2,356|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739| 287.150|   1,990|
| |Garfield County|     0|  0.000|  0.000|     3|  1523.616|  0.000|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Jefferson County|     0|  0.000|  0.000|    16|  2270.792| 40.550|   7,046|
| |Red Willow County|     0|  0.000|  0.000|    16|  1491.981|  0.000|  10,724|
| |Polk County|     0|  0.000|  0.000|    26|  4987.531| 54.808|   5,213|
| |Pierce County|     0|  0.000|  0.000|    20|  2797.985| 39.971|   7,148|
| |Phelps County|     0|  0.000|  0.000|    37|  4095.639| 47.440|   9,034|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317| 109.343|   2,613|
| |Otoe County|     0|  0.000|  0.000|    45|  2810.392| 26.766|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    28|  4016.064| 163.921|   6,972|
| |Nance County|     0|  0.000|  0.000|     8|  2273.373|  0.000|   3,519|
| |Morrill County|     0|  0.000|  0.000|    58| 12494.614|  0.000|   4,642|
| |Merrick County|     0|  0.000|  0.000|    61|  7865.893| 239.477|   7,755|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759| 105.274|   1,357|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    34|  4080.653| 51.437|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    22|  2738.362| 71.126|   8,034|
| |Kearney County|     0|  0.000|  0.000|    51|  7852.194| 483.889|   6,495|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Johnson County|     0|  0.000|  0.000|    13|  2563.597| 56.343|   5,071|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 85.144|  10,067|
| |Thomas County|     0|  0.000|  0.000|     1|  1385.042|  0.000|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 57.109|   5,003|
| |Stanton County|     0|  0.000|  0.000|    29|  4898.649| 72.394|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Sherman County|     0|  0.000|  0.000|    11|  3665.445| 190.413|   3,001|
| |Sheridan County|     0|  0.000|  0.000|     9|  1715.593|  0.000|   5,246|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Valley County|     0|  0.000|  0.000|    10|  2405.002|  0.000|   4,158|
| |Wayne County|     0|  0.000|  0.000|    37|  3942.461| 30.444|   9,385|
| |Webster County|     0|  0.000|  0.000|     9|  2581.015|  0.000|   3,487|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|     783|
| |York County|     0|  0.000|  0.000|    78|  5702.171| 52.218|  13,679|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   277| 86.402| N/A|34,761| 10842.625| N/A|3,205,958|
| |Salt Lake County|   189| 162.870|  1.600|20,446| 17619.224| 148.836|1,160,437|
| |Utah County|    37| 58.155|  0.449| 8,630| 13564.170| 184.568| 636,235|
| |San Juan County|    25| 1633.133|  9.332|   648| 42330.807| 242.637|  15,308|
| |Davis County|    21| 59.075|  3.215| 3,194|  8985.009| 96.851| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   558| 16367.956| 138.285|  34,091|
| |Summit County|     1| 23.728|  0.000|   706| 16751.691| 57.624|  42,145|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Tooele County|     0|  0.000|  0.000|   579|  8012.843| 92.920|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   235| 131.501| N/A|24,492| 13705.153| N/A|1,787,065|
| |Ada County|    81| 168.194|  5.636| 8,932| 18547.012| 275.280| 481,587|
| |Canyon County|    48| 208.833|  6.837| 5,726| 24912.007| 589.207| 229,849|
| |Twin Falls County|    32| 368.333|  1.644| 1,384| 15930.385| 292.693|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   158|  3910.117| 98.990|  40,408|
| |Kootenai County|    16| 96.562|  2.586| 1,790| 10802.851| 186.226| 165,697|
| |Blaine County|     6| 260.632|  0.000|   575| 24977.195| 37.233|  23,021|
| |Jerome County|     6| 245.781|  0.000|   471| 19293.790| 298.448|  24,412|
| |Washington County|     3| 294.291| 14.014|   203| 19913.675| 196.194|  10,194|
| |Elmore County|     3| 109.047|  0.000|   212|  7706.009| 62.313|  27,511|
| |Bonneville County|     3| 25.197|  1.200| 1,003|  8424.182| 352.757| 119,062|
| |Minidoka County|     2| 95.062|  0.000|   475| 22577.119| 319.135|  21,039|
| |Bingham County|     2| 42.725|  0.000|   243|  5191.088| 195.314|  46,811|
| |Owyhee County|     2| 169.162| 12.083|   262| 22160.196| 362.490|  11,823|
| |Bannock County|     2| 22.777|  0.000|   391|  4452.897| 144.796|  87,808|
| |Payette County|     2| 83.504|  0.000|   384| 16032.733| 345.944|  23,951|
| |Shoshone County|     2| 155.255|  0.000|    96|  7452.259| 255.062|  12,882|
| |Boise County|     1| 127.698|  0.000|    48|  6129.485| 182.425|   7,831|
| |Cassia County|     1| 41.615|  0.000|   516| 21473.159| 261.578|  24,030|
| |Valley County|     1| 87.781|  0.000|    59|  5179.073| 163.022|  11,392|
| |Gem County|     1| 55.212|  7.887|   179|  9882.951| 220.848|  18,112|
| |Gooding County|     1| 65.880|  0.000|   161| 10606.759| 254.110|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   190|  6360.684| 263.036|  29,871|
| |Fremont County|     0|  0.000|  0.000|    79|  6030.995| 316.273|  13,099|
| |Boundary County|     0|  0.000|  0.000|    35|  2858.310| 23.333|  12,245|
| |Bonner County|     0|  0.000|  0.000|   183|  4000.962| 96.823|  45,739|
| |Benewah County|     0|  0.000|  0.000|    64|  6883.201| 199.736|   9,298|
| |Bear Lake County|     0|  0.000|  0.000|    15|  2448.980| 209.913|   6,125|
| |Adams County|     0|  0.000|  0.000|    19|  4424.779| 33.269|   4,294|
| |Franklin County|     0|  0.000|  0.000|    51|  3675.411| 41.181|  13,876|
| |Idaho County|     0|  0.000|  0.000|    31|  1859.963| 17.143|  16,667|
| |Latah County|     0|  0.000|  0.000|    99|  2468.335| 71.236|  40,108|
| |Custer County|     0|  0.000|  0.000|    10|  2317.497| 99.321|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    16|  1827.318| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|     8|  9467.456| 1183.432|     845|
| |Caribou County|     0|  0.000|  0.000|    31|  4332.635| 159.728|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Power County|     0|  0.000|  0.000|    55|  7160.526| 241.784|   7,681|
| |Teton County|     0|  0.000|  0.000|    82|  6753.418| 282.373|  12,142|
| |Lemhi County|     0|  0.000|  0.000|    23|  2865.330| 195.768|   8,027|
| |Oneida County|     0|  0.000|  0.000|    13|  2869.124| 157.644|   4,531|
| |Madison County|     0|  0.000|  0.000|   162|  4059.438| 107.393|  39,907|
| |Lincoln County|     0|  0.000|  0.000|    56| 10436.079| 159.736|   5,366|
| |Lewis County|     0|  0.000|  0.000|     1|   260.552|  0.000|   3,838|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   146| 165.035| N/A| 9,477| 10712.602| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  3.698| 4,376| 22657.844| 138.320| 193,134|
| |Pennington County|    32| 281.257|  3.767|   881|  7743.353| 79.103| 113,775|
| |Beadle County|     9| 487.726|  0.000|   591| 32027.313| 30.967|  18,453|
| |Todd County|     5| 491.304| 14.037|    69|  6779.994| 42.112|  10,177|
| |Union County|     4| 251.067|  0.000|   213| 13369.320| 161.400|  15,932|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556| 145.624|   1,962|
| |Brown County|     3| 77.242|  0.000|   436| 11225.830| 110.346|  38,839|
| |Yankton County|     2| 87.665|  0.000|   113|  4953.099| 75.142|  22,814|
| |Oglala Lakota County|     2| 141.074| 10.077|   154| 10862.665| 80.613|  14,177|
| |Lyman County|     2| 528.961|  0.000|    89| 23538.746| 37.783|   3,781|
| |Lincoln County|     2| 32.718|  0.000|   621| 10159.011| 140.221|  61,128|
| |Lake County|     2| 156.287|  0.000|    91|  7111.042| 133.960|  12,797|
| |Hughes County|     2| 114.116|  0.000|    92|  5249.344| 73.360|  17,526|
| |Roberts County|     1| 96.209|  0.000|    81|  7792.957| 151.186|  10,394|
| |McCook County|     1| 179.019|  0.000|    27|  4833.512| 76.722|   5,586|
| |Meade County|     1| 35.296|  0.000|    91|  3211.916| 100.845|  28,332|
| |Butte County|     1| 95.886|  0.000|    14|  1342.411| 54.792|  10,429|
| |Codington County|     1| 35.703|  5.100|   129|  4605.662| 56.104|  28,009|
| |Davison County|     1| 50.569|  7.224|    94|  4753.477| 50.569|  19,775|
| |Faulk County|     1| 434.972|  0.000|    26| 11309.265|  0.000|   2,299|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474| 128.161|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |Brookings County|     1| 28.509|  0.000|   133|  3791.658| 61.090|  35,077|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953| 64.466|   2,216|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 120.098|   2,379|
| |Marshall County|     0|  0.000|  0.000|     9|  1823.708| 28.948|   4,935|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Spink County|     0|  0.000|  0.000|    24|  3764.115| 112.027|   6,376|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Turner County|     0|  0.000|  0.000|    51|  6083.015| 119.275|   8,384|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Ziebach County|     0|  0.000|  0.000|    34| 12336.720| 1347.709|   2,756|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Custer County|     0|  0.000|  0.000|    32|  3566.652| 206.993|   8,972|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159| 51.929|   2,751|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061| 42.454|   3,365|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Brule County|     0|  0.000|  0.000|    45|  8495.375| 134.847|   5,297|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233| 103.821|   1,376|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Charles Mix County|     0|  0.000|  0.000|   101| 10869.565| 30.748|   9,292|
| |Clay County|     0|  0.000|  0.000|   124|  8813.077| 101.533|  14,070|
| |Corson County|     0|  0.000|  0.000|    32|  7831.620| 139.850|   4,086|
| |Day County|     0|  0.000|  0.000|    23|  4240.413| 52.676|   5,424|
| |Deuel County|     0|  0.000|  0.000|    10|  2298.322| 65.666|   4,351|
| |Dewey County|     0|  0.000|  0.000|    49|  8316.361|  0.000|   5,892|
| |Douglas County|     0|  0.000|  0.000|    17|  5819.925| 48.907|   2,921|
| |Edmunds County|     0|  0.000|  0.000|    14|  3656.307| 37.309|   3,829|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 148.965|   6,713|
| |Grant County|     0|  0.000|  0.000|    26|  3686.897| 141.804|   7,052|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    18|  2920.182| 92.704|   6,164|
| |Hand County|     0|  0.000|  0.000|     7|  2193.670|  0.000|   3,191|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668| 41.372|   3,453|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Hutchinson County|     0|  0.000|  0.000|    28|  3840.351| 39.187|   7,291|
| |Hyde County|     0|  0.000|  0.000|     3|  2305.919|  0.000|   1,301|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582| 57.849|   4,939|
| |Lawrence County|     0|  0.000|  0.000|    52|  2012.072| 138.192|  25,844|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   131| 73.097| N/A| 7,563|  4220.078| N/A|1,792,147|
| |Kanawha County|    23| 129.124|  2.406|   911|  5114.415| 82.607| 178,124|
| |Jackson County|    19| 664.894|  0.000|   162|  5669.093| 24.996|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   693|  5815.173| 50.348| 119,171|
| |Wayne County|     9| 228.415|  0.000|   203|  5152.023| 76.138|  39,402|
| |Fayette County|     7| 165.071|  6.738|   144|  3395.746| 50.532|  42,406|
| |Wood County|     5| 59.867|  1.710|   245|  2933.499| 18.815|  83,518|
| |Monongalia County|     5| 47.343|  0.000|   938|  8881.566| 39.227| 105,612|
| |Mingo County|     5| 213.456| 18.296|   172|  7342.896| 286.641|  23,424|
| |Preston County|     4| 119.646|  4.273|   124|  3709.021|  4.273|  33,432|
| |Mineral County|     4| 148.876|  0.000|   120|  4466.280| 58.487|  26,868|
| |Ohio County|     4| 96.593|  0.000|   266|  6423.414| 58.646|  41,411|
| |Jefferson County|     4| 69.996|  0.000|   294|  5144.717| 17.499|  57,146|
| |Cabell County|     3| 32.628|  1.554|   389|  4230.790| 99.438|  91,945|
| |Greenbrier County|     3| 86.550|  0.000|    92|  2654.203| 28.850|  34,662|
| |Mercer County|     3| 51.057|  0.000|   182|  3097.451| 104.545|  58,758|
| |Logan County|     3| 93.694|  0.000|   221|  6902.152| 374.777|  32,019|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097| 26.942|  15,907|
| |Marion County|     2| 35.668|  0.000|   186|  3317.164| 35.668|  56,072|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Brooke County|     1| 45.581|  0.000|    62|  2826.018|  6.512|  21,939|
| |Nicholas County|     1| 40.823|  0.000|    37|  1510.451| 29.159|  24,496|
| |Pendleton County|     1| 143.493|  0.000|    39|  5596.212| 40.998|   6,969|
| |Pleasants County|     1| 134.048| 19.150|    12|  1608.579| 76.599|   7,460|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656| 16.791|   8,508|
| |Harrison County|     1| 14.869|  0.000|   219|  3256.215| 67.971|  67,256|
| |Hampshire County|     1| 43.150|  0.000|    76|  3279.396| 12.329|  23,175|
| |Grant County|     1| 86.445| 12.349|   119| 10286.999| 568.070|  11,568|
| |Marshall County|     1| 32.754|  4.679|   131|  4290.721| 32.754|  30,531|
| |Roane County|     1| 73.057|  0.000|    15|  1095.850| 10.437|  13,688|
| |Raleigh County|     1| 13.631|  0.000|   227|  3094.287| 87.629|  73,361|
| |Taylor County|     1| 59.898|  8.557|    56|  3354.298| 34.228|  16,695|
| |Wyoming County|     1| 49.034|  0.000|    31|  1520.055| 70.049|  20,394|
| |Mason County|     1| 37.713|  0.000|    54|  2036.506| 43.101|  26,516|
| |Tyler County|     0|  0.000|  0.000|    13|  1513.212| 16.629|   8,591|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Boone County|     0|  0.000|  0.000|   100|  4660.484| 159.788|  21,457|
| |Randolph County|     0|  0.000|  0.000|   208|  7248.650|  4.978|  28,695|
| |Putnam County|     0|  0.000|  0.000|   193|  3418.955| 75.921|  56,450|
| |Pocahontas County|     0|  0.000|  0.000|    41|  4971.505|  0.000|   8,247|
| |Morgan County|     0|  0.000|  0.000|    26|  1453.813|  0.000|  17,884|
| |Summers County|     0|  0.000|  0.000|    10|   795.355| 34.087|  12,573|
| |Wirt County|     0|  0.000|  0.000|     6|  1030.751|  0.000|   5,821|
| |Wetzel County|     0|  0.000|  0.000|    42|  2787.919|  9.483|  15,065|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 33.820|   8,448|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Upshur County|     0|  0.000|  0.000|    39|  1613.170|  5.909|  24,176|
| |McDowell County|     0|  0.000|  0.000|    58|  3290.967| 210.752|  17,624|
| |Tucker County|     0|  0.000|  0.000|    10|  1462.202|  0.000|   6,839|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |Lincoln County|     0|  0.000|  0.000|    88|  4311.823| 181.993|  20,409|
| |Gilmer County|     0|  0.000|  0.000|    16|  2045.251|  0.000|   7,823|
| |Hardy County|     0|  0.000|  0.000|    58|  4210.221| 41.480|  13,776|
| |Hancock County|     0|  0.000|  0.000|   111|  3852.829| 54.545|  28,810|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   125| 92.991| N/A| 4,026|  2995.063| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.484| 2,082|  7057.555| 16.949| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   670|  3226.723| 13.760| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   170|  1390.002|  3.504| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   558|  5153.449| 10.555| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   152|   999.027|  5.634| 152,148|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Hancock County|     1| 18.186|  0.000|    35|   636.514| 20.784|  54,987|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Knox County|     1| 25.143|  0.000|    28|   704.013|  7.184|  39,772|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Oxford County|     0|  0.000|  0.000|    53|   914.187|  0.000|  57,975|
| |Piscataquis County|     0|  0.000|  0.000|     3|   178.731|  0.000|  16,785|
| |Washington County|     0|  0.000|  0.000|    12|   382.421| 18.211|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    55|  1533.913| 19.921|  35,856|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   112| 146.970| N/A| 7,490|  9828.597| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,028| 16644.405| 87.164| 181,923|
| |Grand Forks County|     6| 86.392|  4.114|   672|  9675.887| 98.734|  69,451|
| |Burleigh County|     6| 62.744|  2.988| 1,142| 11942.359| 295.795|  95,626|
| |Stark County|     3| 95.271|  0.000|   259|  8225.094| 326.645|  31,489|
| |Morton County|     3| 95.651|  0.000|   357| 11382.477| 405.378|  31,364|
| |Williams County|     2| 53.207|  0.000|   269|  7156.349| 152.020|  37,589|
| |Stutsman County|     2| 96.600|  0.000|   127|  6134.080| 124.200|  20,704|
| |Ramsey County|     2| 173.626|  0.000|    69|  5990.103| 359.654|  11,519|
| |McIntosh County|     2| 800.961| 57.212|    30| 12014.417| 629.327|   2,497|
| |Benson County|     2| 292.740| 20.910|   134| 19613.583| 857.310|   6,832|
| |Richland County|     1| 61.816|  8.831|   105|  6490.697| 123.632|  16,177|
| |Sioux County|     1| 236.407| 33.772|    79| 18676.123| 709.220|   4,230|
| |Ward County|     1| 14.784|  0.000|   221|  3267.249| 95.040|  67,641|
| |Mountrail County|     1| 94.832|  0.000|   129| 12233.286| 216.758|  10,545|
| |McKenzie County|     1| 66.560|  0.000|    89|  5923.855| 104.595|  15,024|
| |Emmons County|     1| 308.547|  0.000|    17|  5245.295| 88.156|   3,241|
| |Griggs County|     1| 448.229| 64.033|    34| 15239.803| 320.164|   2,231|
| |McHenry County|     1| 174.064|  0.000|    16|  2785.030| 49.733|   5,745|
| |McLean County|     0|  0.000|  0.000|    59|  6243.386| 332.577|   9,450|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Adams County|     0|  0.000|  0.000|     2|   902.527|  0.000|   2,216|
| |Barnes County|     0|  0.000|  0.000|    37|  3552.568| 68.582|  10,415|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784| 231.660|   1,850|
| |Bowman County|     0|  0.000|  0.000|     6|  1984.127|  0.000|   3,024|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252| 72.924|   1,959|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Pierce County|     0|  0.000|  0.000|    11|  2767.296|  0.000|   3,975|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641|  0.000|   2,327|
| |Rolette County|     0|  0.000|  0.000|    61|  4303.047| 292.244|  14,176|
| |Sargent County|     0|  0.000|  0.000|    11|  2821.960| 109.946|   3,898|
| |Sheridan County|     0|  0.000|  0.000|     8|  6083.650| 325.910|   1,315|
| |Slope County|     0|  0.000|  0.000|     3|  4000.000|  0.000|     750|
| |Steele County|     0|  0.000|  0.000|    14|  7407.407| 302.343|   1,890|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Traill County|     0|  0.000|  0.000|    54|  6719.761| 213.326|   8,036|
| |Wells County|     0|  0.000|  0.000|    21|  5477.308| 223.564|   3,834|
| |Mercer County|     0|  0.000|  0.000|    28|  3420.056| 87.246|   8,187|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704| 270.179|   2,115|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Dickey County|     0|  0.000|  0.000|    12|  2463.054| 29.322|   4,872|
| |Divide County|     0|  0.000|  0.000|     2|   883.392| 63.099|   2,264|
| |Dunn County|     0|  0.000|  0.000|    30|  6781.193| 32.291|   4,424|
| |Eddy County|     0|  0.000|  0.000|    18|  7870.573| 312.324|   2,287|
| |Foster County|     0|  0.000|  0.000|    25|  7788.162| 356.030|   3,210|
| |Golden Valley County|     0|  0.000|  0.000|     4|  2271.437|  0.000|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Kidder County|     0|  0.000|  0.000|    13|  5241.935| 115.207|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 70.616|   4,046|
| |Nelson County|     0|  0.000|  0.000|    25|  8683.571| 396.963|   2,879|
| |Walsh County|     0|  0.000|  0.000|   104|  9773.518| 80.551|  10,641|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    75| 70.174| N/A| 4,889|  4574.383| N/A|1,068,778|
| |Yellowstone County|    30| 185.989|  3.543| 1,261|  7817.731| 188.646| 161,300|
| |Big Horn County|    13| 976.049| 42.903|   421| 31608.980| 1094.033|  13,319|
| |Toole County|     6| 1266.892|  0.000|    45|  9501.689| 422.297|   4,736|
| |Cascade County|     4| 49.161|  3.511|   164|  2015.584| 35.115|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   930|  8126.955| 82.393| 114,434|
| |Lincoln County|     2| 100.100|  0.000|    76|  3803.804| 50.050|  19,980|
| |Richland County|     2| 185.134| 13.224|    47|  4350.643| 13.224|  10,803|
| |Hill County|     2| 121.330| 17.333|    42|  2547.925| 17.333|  16,484|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 112.762|  11,402|
| |Flathead County|     2| 19.267|  0.000|   330|  3179.007| 105.967| 103,806|
| |Missoula County|     1|  8.361|  0.000|   328|  2742.475| 86.001| 119,600|
| |Lake County|     1| 32.832|  0.000|   179|  5876.945| 65.664|  30,458|
| |Madison County|     1| 116.279|  0.000|    87| 10116.279| 215.947|   8,600|
| |Lewis and Clark County|     1| 14.403|  0.000|   156|  2246.803| 55.553|  69,432|
| |Glacier County|     1| 72.711|  0.000|    72|  5235.221| 186.972|  13,753|
| |Ravalli County|     1| 22.828|  0.000|    82|  1871.890| 32.611|  43,806|
| |Rosebud County|     1| 111.894|  0.000|    33|  3692.514| 175.834|   8,937|
| |Stillwater County|     1| 103.713| 14.816|    23|  2385.397| 59.265|   9,642|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972| 38.228|   3,737|
| |Fergus County|     0|  0.000|  0.000|     9|   814.480| 38.785|  11,050|
| |Mineral County|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,397|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |McCone County|     0|  0.000|  0.000|     3|  1802.885| 171.703|   1,664|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Jefferson County|     0|  0.000|  0.000|    28|  2291.138| 35.068|  12,221|
| |Granite County|     0|  0.000|  0.000|    16|  4735.129| 380.501|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Deer Lodge County|     0|  0.000|  0.000|    25|  2735.230| 78.149|   9,140|
| |Dawson County|     0|  0.000|  0.000|    17|  1973.761| 16.586|   8,613|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148| 84.531|   1,690|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    14|  1892.915| 57.946|   7,396|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Park County|     0|  0.000|  0.000|    55|  3312.056| 68.822|  16,606|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Broadwater County|     0|  0.000|  0.000|    11|  1763.668| 22.905|   6,237|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Silver Bow County|     0|  0.000|  0.000|    85|  2434.484| 85.923|  34,915|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 86.345|   3,309|
| |Sanders County|     0|  0.000|  0.000|     9|   743.003|  0.000|  12,113|
| |Roosevelt County|     0|  0.000|  0.000|    23|  2090.149| 51.929|  11,004|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505| 132.644|   1,077|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 48.336|   5,911|
| |Phillips County|     0|  0.000|  0.000|    28|  7081.437| 1011.634|   3,954|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 101.407|   5,635|
| |Carbon County|     0|  0.000|  0.000|    68|  6340.326| 146.520|  10,725|
| |Blaine County|     0|  0.000|  0.000|    10|  1496.782| 42.765|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    62|  6558.764| 226.685|   9,453|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,446|  2317.349| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   728|  4445.150|  9.595| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  2.892|  49,402|
| |Windham County|     3| 71.053|  0.000|   102|  2415.802|  3.383|  42,222|
| |Windsor County|     2| 36.323|  0.000|    72|  1307.617|  2.594|  55,062|
| |Washington County|     2| 34.241|  0.000|    53|   907.394| 14.675|  58,409|
| |Addison County|     2| 54.382|  0.000|    73|  1984.936|  3.884|  36,777|
| |Rutland County|     1| 17.185|  0.000|    99|  1701.294| 24.550|  58,191|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Bennington County|     1| 28.193|  0.000|    85|  2396.391|  4.028|  35,470|
| |Caledonia County|     0|  0.000|  0.000|    26|   866.869|  0.000|  29,993|
| |Orange County|     0|  0.000|  0.000|    14|   484.563|  0.000|  28,892|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    30| 21.188| N/A| 3,323|  2346.964| N/A|1,415,872|
| |Honolulu County|    24| 24.626| N/A| 2,964|  3041.363| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   184|  1099.052| 11.946| 167,417|
| |Kauai County|     0|  0.000|  0.000|    47|   650.132|  0.000|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   128|   635.195|  9.216| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,015|  5209.422| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    23|  2723.505| 16.916|   8,445|
| |Big Horn County|     0|  0.000|  0.000|    36|  3053.435| 12.117|  11,790|
| |Albany County|     0|  0.000|  0.000|    88|  2263.374| 11.023|  38,880|
| |Campbell County|     0|  0.000|  0.000|   123|  2654.237| 21.579|  46,341|
| |Park County|     0|  0.000|  0.000|   132|  4521.477| 73.401|  29,194|
| |Carbon County|     0|  0.000|  0.000|    99|  6689.189| 202.703|  14,800|
| |Laramie County|     0|  0.000|  0.000|   498|  5005.025| 51.687|  99,500|
| |Natrona County|     0|  0.000|  0.000|   229|  2867.590| 25.044|  79,858|
| |Washakie County|     0|  0.000|  0.000|    70|  8968.610| 384.369|   7,805|
| |Uinta County|     0|  0.000|  0.000|   274| 13546.920| 105.946|  20,226|
| |Teton County|     0|  0.000|  0.000|   370| 15768.837| 133.944|  23,464|
| |Sweetwater County|     0|  0.000|  0.000|   257|  6069.480| 50.607|  42,343|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Sublette County|     0|  0.000|  0.000|    38|  3865.324| 29.063|   9,831|
| |Sheridan County|     0|  0.000|  0.000|    72|  2361.817| 56.234|  30,485|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Converse County|     0|  0.000|  0.000|    32|  2315.150| 20.671|  13,822|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 161.859|   4,413|
| |Goshen County|     0|  0.000|  0.000|    26|  1968.057| 129.762|  13,211|
| |Fremont County|     0|  0.000|  0.000|   503| 12811.696| 109.160|  39,261|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565| 18.837|   7,584|
| |Lincoln County|     0|  0.000|  0.000|   100|  5042.864| 79.245|  19,830|
| |Weston County|     0|  0.000|  0.000|     5|   721.813|  0.000|   6,927|


### Rhode Island ###

![Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Rhode%20Island.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|RI|5 counties|     0|  0.000| N/A|17,860| 16859.220| N/A|1,059,361|
| |Bristol County|     0|  0.000|  0.000|   316|  6518.286| 35.361|  48,479|
| |Kent County|     0|  0.000|  0.000| 1,494|  9093.565| 63.476| 164,292|
| |Newport County|     0|  0.000|  0.000|   396|  4824.444| 27.847|  82,082|
| |Providence County|     0|  0.000|  0.000|15,047| 23550.274| 111.347| 638,931|
| |Washington County|     0|  0.000|  0.000|   607|  4833.688| 19.339| 125,577|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|


