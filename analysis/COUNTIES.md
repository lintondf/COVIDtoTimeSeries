# Analysis of US By County #

Updated: at 2020-08-10

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 129,898 deaths (450.001 deaths/million) and 4,339,528 confirmed cases (15033.248 confirmed cases/million).  This group accounts for 81.01% of all US deaths and for 87.51% of all US cases.

24.69% of this group's deaths (20.00% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.05% of this group's deaths (20.30% of the total US deaths) occured in 33 counties in 14 states with a combined population of 41,047,233 (12.51% of the total US population):



The next 25.26% of this group's deaths (20.46% of the total US deaths) occured in 89 counties in 30 states with a combined population of 65,834,261 (20.06% of the total US population)

The remaining 25.00% of this group's deaths (20.26% of the total US deaths) occured in 855 counties in 50 states with a combined population of 144,493,347 (44.02% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,986 deaths (252.315 deaths/million) and 450,812 confirmed cases (11390.624 confirmed cases/million).  This group accounts for 6.23% of all US deaths and for 9.09% of all US cases.

24.86% of this group's deaths (1.55% of the total US deaths) occured in 58 counties in 16 states with a combined population of 1,922,976 (0.59% of the total US population):



The next 25.09% of this group's deaths (1.56% of the total US deaths) occured in 112 counties in 27 states with a combined population of 3,323,269 (1.01% of the total US population):



The next 25.03% of this group's deaths (1.56% of the total US deaths) occured in 232 counties in 34 states with a combined population of 5,675,872 (1.73% of the total US population)

The remaining 25.03% of this group's deaths (1.56% of the total US deaths) occured in 1,750 counties in 47 states with a combined population of 28,655,347 (8.73% of the total US population) 

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
|NJ|21 counties|15,874| 1787.172| N/A|184,127| 20729.910| N/A|8,882,190|
| |Essex County| 2,111| 2642.135|  1.609|19,728| 24691.636| 36.118| 798,975|
| |Bergen County| 2,038| 2186.221|  0.000|20,794| 22306.324| 41.836| 932,202|
| |Hudson County| 1,504| 2236.794|  0.637|19,671| 29255.299| 33.994| 672,391|
| |Middlesex County| 1,403| 1700.478|  0.000|17,919| 21718.368| 35.668| 825,062|
| |Union County| 1,350| 2426.569|  0.514|16,695| 30008.574| 30.814| 556,341|
| |Passaic County| 1,240| 2470.976|  0.000|17,642| 35155.612| 42.417| 501,826|
| |Ocean County| 1,018| 1676.587|  0.471|10,596| 17450.995| 32.233| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,302| 16648.486| 42.710| 618,795|
| |Morris County|   829| 1685.490|  0.000| 7,248| 14736.350| 26.722| 491,845|
| |Mercer County|   619| 1684.675|  1.166| 8,119| 22096.726| 29.938| 367,430|
| |Camden County|   580| 1145.179|  1.410| 8,562| 16905.213| 57.823| 506,471|
| |Somerset County|   561| 1705.509|  2.606| 5,245| 15945.448| 23.887| 328,934|
| |Burlington County|   473| 1062.088|  0.962| 6,007| 13488.298| 56.457| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,463| 13133.842| 37.926| 263,670|
| |Gloucester County|   212| 726.934|  1.470| 3,248| 11137.171| 73.967| 291,636|
| |Sussex County|   198| 1409.373|  3.051| 1,330|  9467.001| 23.388| 140,488|
| |Warren County|   172| 1633.940|  1.357| 1,345| 12777.034| 20.356| 105,267|
| |Cumberland County|   158| 1056.665|  0.955| 3,338| 22323.727| 93.629| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,149|  9238.488| 13.784| 124,371|
| |Salem County|    87| 1394.566|  9.160|   894| 14330.368| 52.668|  62,385|
| |Cape May County|    87| 945.251|  0.000|   832|  9039.646| 34.147|  92,039|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,319| 633.258| N/A|252,366| 12972.757| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,655| 32172.030| 35.058|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.097|43,786| 29653.237| 42.666|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.148|36,205| 37420.957| 30.565| 967,506|
| |Queens County|   984| 436.635|  0.778| 7,869|  3491.127| 17.726|2,253,858|
| |Kings County|   930| 363.313|  0.648| 1,350|   527.524|  2.678|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,942| 42794.569| 26.310| 325,789|
| |Erie County|   671| 730.378|  0.311| 8,904|  9691.935| 51.626| 918,702|
| |Bronx County|   649| 457.479|  0.816|26,796| 18894.540| 95.936|1,418,207|
| |Orange County|   491| 1275.523|  0.742|11,159| 28988.933| 24.494| 384,940|
| |New York County|   414| 254.300|  0.453|15,455|  9488.840| 48.179|1,628,706|
| |Monroe County|   285| 384.216|  1.541| 4,956|  6681.316| 36.207| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,576|  7765.000| 28.228| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,607| 15658.457| 42.243| 294,218|
| |Richmond County|   148| 310.790|  0.554| 7,869| 16525.509| 83.907| 476,143|
| |Albany County|   128| 418.977|  0.935| 2,595|  8494.105| 34.603| 305,506|
| |Oneida County|   115| 502.906|  1.874| 2,146|  9384.662| 36.859| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,498|  7157.840| 35.496| 209,281|
| |Ulster County|    92| 518.097|  0.804| 2,062| 11612.126| 27.353| 177,573|
| |Broome County|    69| 362.228|  3.750| 1,126|  5911.134| 53.997| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,449| 14737.592| 30.513|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   298|  7385.012| 10.621|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,489| 19739.633| 11.363|  75,432|
| |Steuben County|    42| 440.349|  0.000|   298|  3124.377|  8.987|  95,379|
| |Columbia County|    37| 622.257|  0.000|   540|  9081.583| 43.246|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,058|  6812.665| 21.157| 155,299|
| |Ontario County|    34| 309.719|  0.000|   360|  3279.375| 14.315| 109,777|
| |Warren County|    33| 516.077|  0.000|   308|  4816.715| 17.873|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   765|  4819.991| 26.103| 158,714|
| |Tioga County|    25| 518.640|  0.000|   193|  4003.900| 11.855|  48,203|
| |Fulton County|    24| 449.581|  0.000|   296|  5544.836| 34.789|  53,383|
| |Greene County|    18| 381.453|  0.000|   292|  6188.014|  9.082|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   757|  3293.266| 15.537| 229,863|
| |Madison County|    17| 239.636|  0.000|   412|  5807.643| 24.165|  70,941|
| |Washington County|    14| 228.743|  0.000|   259|  4231.750|  9.336|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   253|  1993.649| 23.640| 126,903|
| |Livingston County|     8| 127.158|  0.000|   176|  2797.470| 20.436|  62,914|
| |Yates County|     7| 280.978|  0.000|    57|  2287.962| 11.468|  24,913|
| |Cattaraugus County|     6| 78.826|  0.000|   165|  2167.715| 11.261|  76,117|
| |Chenango County|     6| 127.100|  0.000|   216|  4575.593| 15.131|  47,207|
| |Genesee County|     5| 87.291|  0.000|   277|  4835.894| 12.470|  57,280|
| |Otsego County|     5| 84.044|  0.000|   116|  1949.809|  9.605|  59,493|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436| 21.504|  39,859|
| |Montgomery County|     4| 81.266|  0.000|   176|  3575.710| 55.145|  49,221|
| |Herkimer County|     4| 65.233|  0.000|   274|  4468.436| 76.881|  61,319|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  1.326| 107,740|
| |Delaware County|     4| 90.631|  0.000|   105|  2379.064|  6.474|  44,135|
| |Clinton County|     4| 49.699|  0.000|   127|  1577.934|  0.000|  80,485|
| |Oswego County|     3| 25.614|  0.000|   253|  2160.104|  8.538| 117,124|
| |Seneca County|     3| 88.194|  0.000|    89|  2616.416| 12.599|  34,016|
| |Wayne County|     3| 33.364|  0.000|   250|  2780.311|  6.355|  89,918|
| |Chemung County|     3| 35.947|  0.000|   171|  2048.984| 13.694|  83,456|
| |Cayuga County|     2| 26.118|  0.000|   152|  1984.956|  7.462|  76,576|
| |Allegany County|     1| 21.696|  0.000|    79|  1714.001| 15.497|  46,091|
| |Hamilton County|     0|  0.000|  0.000|     8|  1811.594| 32.350|   4,416|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  4.608|  30,999|
| |Schuyler County|     0|  0.000|  0.000|    22|  1235.469|  0.000|  17,807|
| |Lewis County|     0|  0.000|  0.000|    41|  1559.172| 32.596|  26,296|
| |Jefferson County|     0|  0.000|  0.000|   142|  1292.860| 10.405| 109,834|
| |Cortland County|     0|  0.000|  0.000|    95|  1996.595|  9.007|  47,581|
| |Tompkins County|     0|  0.000|  0.000|   234|  2290.076|  5.592| 102,180|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525| 11.424|  50,022|
| |Essex County|     0|  0.000|  0.000|    55|  1491.121|  0.000|  36,885|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|10,377| 262.628| N/A|559,746| 14166.401| N/A|39,512,223|
| |Los Angeles County| 4,977| 495.761|  4.041|208,563| 20775.055| 233.174|10,039,107|
| |Riverside County|   799| 323.410|  6.014|40,452| 16373.708| 198.973|2,470,546|
| |Orange County|   726| 228.612|  3.374|39,641| 12482.634| 101.215|3,175,692|
| |San Diego County|   593| 177.634|  1.198|32,330|  9684.483| 104.714|3,338,330|
| |San Bernardino County|   546| 250.449|  8.453|35,712| 16381.013| 179.023|2,180,085|
| |Imperial County|   244| 1346.467| 18.920| 9,693| 53488.950| 223.886| 181,215|
| |San Joaquin County|   211| 276.849|  8.060|12,303| 16142.534| 153.701| 762,148|
| |Alameda County|   208| 124.452|  1.624|13,213|  7905.685| 144.368|1,671,329|
| |Santa Clara County|   204| 105.817|  0.963|11,687|  6062.187| 78.622|1,927,852|
| |Tulare County|   196| 420.425|  5.516|10,475| 22469.138| 312.867| 466,195|
| |Fresno County|   171| 171.154|  4.719|17,290| 17305.558| 315.569| 999,101|
| |Kern County|   171| 189.957|  4.285|23,583| 26197.453| 482.114| 900,202|
| |Stanislaus County|   162| 294.192| 13.490| 9,665| 17551.665| 156.695| 550,660|
| |Sacramento County|   161| 103.733|  1.749|10,795|  6955.281| 67.008|1,552,058|
| |Contra Costa County|   139| 120.500|  1.734| 9,182|  7959.942| 150.594|1,153,526|
| |San Mateo County|   120| 156.541|  0.186| 6,110|  7970.539| 105.479| 766,573|
| |Ventura County|    89| 105.200|  2.195| 8,146|  9628.773| 135.426| 846,006|
| |Marin County|    79| 305.224|  4.967| 5,327| 20581.394| 183.797| 258,826|
| |Santa Barbara County|    69| 154.536|  2.880| 6,704| 15014.591| 171.813| 446,499|
| |San Francisco County|    67| 76.003| N/A| 7,548|  8562.201| N/A| 881,549|
| |Merced County|    64| 230.481|  7.203| 5,012| 18049.553| 374.017| 277,680|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993| 68.187| 152,940|
| |Sonoma County|    47| 95.077|  2.890| 3,556|  7193.488| 144.783| 494,336|
| |Yolo County|    43| 195.011|  0.648| 1,721|  7804.989| 114.674| 220,500|
| |Solano County|    40| 89.357|  0.957| 4,029|  9000.476| 133.397| 447,643|
| |Madera County|    39| 247.891|  8.172| 2,302| 14631.945| 325.982| 157,327|
| |Monterey County|    35| 80.634|  1.646| 5,293| 12194.139| 155.014| 434,061|
| |Placer County|    20| 50.210|  1.435| 2,186|  5487.926| 93.605| 398,329|
| |San Luis Obispo County|    15| 52.983|  0.000| 2,093|  7392.860| 156.425| 283,111|
| |Shasta County|    10| 55.531|  0.793|   418|  2321.191| 38.872| 180,080|
| |Napa County|    10| 72.598|  2.074| 1,046|  7593.797| 163.865| 137,744|
| |Mendocino County|    10| 115.275|  1.647|   431|  4968.357| 187.734|  86,749|
| |Butte County|     8| 36.499|  0.652| 1,095|  4995.757| 100.371| 219,186|
| |Sutter County|     7| 72.187|  1.473|   942|  9714.244| 229.818|  96,971|
| |Santa Cruz County|     6| 21.961|  1.046| 1,238|  4531.263| 44.968| 273,213|
| |Humboldt County|     4| 29.508|  0.000|   282|  2080.290| 51.638| 135,558|
| |Yuba County|     4| 50.847|  0.000|   600|  7626.989| 208.834|  78,668|
| |Colusa County|     4| 185.641|  0.000|   362| 16800.483| 258.571|  21,547|
| |San Benito County|     4| 63.686|  0.000|   715| 11383.900| 163.764|  62,808|
| |Inyo County|     3| 166.306| 15.839|    89|  4933.755| 300.935|  18,039|
| |Glenn County|     3| 105.660| 10.063|   360| 12679.181| 176.100|  28,393|
| |Amador County|     2| 50.312|  7.187|   164|  4125.579| 136.561|  39,752|
| |Lake County|     2| 31.063|  2.219|   220|  3416.892| 55.469|  64,386|
| |Mariposa County|     2| 116.259|  0.000|    61|  3545.893| 41.521|  17,203|
| |Tuolumne County|     2| 36.712|  0.000|   152|  2790.117| 28.845|  54,478|
| |Nevada County|     1| 10.025|  0.000|   322|  3227.908| 32.938|  99,755|
| |Mono County|     1| 69.233|  0.000|   154| 10661.867| 89.014|  14,444|
| |Calaveras County|     1| 21.784|  0.000|   147|  3202.266| 68.464|  45,905|
| |Tehama County|     1| 15.365|  0.000|   276|  4240.674| 92.189|  65,084|
| |El Dorado County|     1|  5.186|  0.000|   729|  3780.277| 68.153| 192,843|
| |Del Norte County|     0|  0.000|  0.000|    99|  3559.615| 56.502|  27,812|
| |Lassen County|     0|  0.000|  0.000|   638| 20868.086| 32.709|  30,573|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547| 48.475|   8,841|
| |Plumas County|     0|  0.000|  0.000|    34|  1807.838|  7.596|  18,807|
| |Sierra County|     0|  0.000|  0.000|     3|   998.336| 47.540|   3,005|
| |Siskiyou County|     0|  0.000|  0.000|    93|  2136.016| 65.623|  43,539|
| |Trinity County|     0|  0.000|  0.000|     5|   407.000|  0.000|  12,285|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 8,918| 307.561| N/A|503,328| 17358.603| N/A|28,995,881|
| |Harris County| 1,575| 334.159| 24.672|85,757| 18194.587| 276.359|4,713,325|
| |Hidalgo County|   807| 928.967| 26.805|19,741| 22724.578| 449.765| 868,707|
| |Bexar County|   782| 390.306| 12.193|42,783| 21353.555| 121.284|2,003,554|
| |Dallas County|   755| 286.471|  3.632|54,674| 20745.084| 193.294|2,635,516|
| |Tarrant County|   447| 212.603|  3.805|31,687| 15070.998| 178.901|2,102,515|
| |Cameron County|   430| 1016.157| 28.358|16,290| 38495.804| 1795.661| 423,163|
| |Travis County|   298| 233.917|  7.177|22,724| 17837.379| 221.919|1,273,954|
| |El Paso County|   293| 349.126|  7.660|16,308| 19431.913| 323.082| 839,238|
| |Nueces County|   236| 651.405| 21.293|15,244| 42076.325| 1090.669| 362,294|
| |Webb County|   169| 610.876| 47.507| 7,888| 28512.355| 907.277| 276,652|
| |Fort Bend County|   162| 199.584|  2.992| 9,533| 11744.661| 431.376| 811,688|
| |Galveston County|   113| 330.275|  6.681| 9,376| 27404.067| 273.490| 342,139|
| |Williamson County|    93| 157.480|  3.387| 6,245| 10574.870| 128.210| 590,551|
| |Brazoria County|    93| 248.488|  8.016| 7,357| 19657.247| 314.140| 374,264|
| |Collin County|    89| 86.013|  2.347| 7,654|  7397.099| 179.619|1,034,730|
| |Denton County|    87| 98.061|  2.093| 7,644|  8615.802| 135.417| 887,207|
| |Montgomery County|    85| 139.943|  3.058| 6,577| 10828.280| 89.610| 607,391|
| |Jefferson County|    84| 333.910|  9.654| 5,880| 23373.681| 220.903| 251,565|
| |Lubbock County|    73| 235.052|  4.140| 6,018| 19377.336| 232.753| 310,569|
| |Comal County|    69| 441.716|  7.316| 1,839| 11772.689| 155.469| 156,209|
| |Starr County|    68| 1052.094| 39.785| 2,161| 33434.933| 784.650|  64,633|
| |Ector County|    56| 336.897|  6.016| 3,531| 21242.548| 209.701| 166,223|
| |Guadalupe County|    55| 329.643| 10.275| 1,679| 10063.112| 70.210| 166,847|
| |McLennan County|    55| 214.322|  8.907| 4,946| 19273.409| 345.142| 256,623|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401| 541.998|  49,025|
| |Midland County|    48| 271.444|  4.847| 2,592| 14657.980| 333.650| 176,832|
| |Brazos County|    48| 209.414|  3.740| 4,055| 17691.123| 110.940| 229,211|
| |Angelina County|    45| 518.941| 16.474| 1,796| 20711.526| 245.468|  86,715|
| |Potter County|    44| 374.739|  6.083| 3,661| 31180.003| 189.803| 117,415|
| |Maverick County|    43| 732.264|  9.731| 2,321| 39525.221| 807.680|  58,722|
| |Victoria County|    42| 456.105| 21.719| 3,448| 37444.073| 380.088|  92,084|
| |Nacogdoches County|    42| 644.132| 13.146| 1,147| 17590.945| 271.675|  65,204|
| |Ellis County|    41| 221.830|  5.410| 2,855| 15446.961| 296.031| 184,826|
| |Walker County|    41| 561.867|  5.873| 3,005| 41180.743| 373.925|  72,971|
| |Washington County|    39| 1086.896|  3.981|   515| 14352.600| 151.290|  35,882|
| |Hays County|    38| 165.080|  3.724| 5,012| 21773.223| 443.731| 230,191|
| |Bell County|    38| 104.705|  2.755| 3,831| 10555.929| 131.865| 362,924|
| |Liberty County|    34| 385.405| 14.574|   978| 11086.047| 220.231|  88,219|
| |Bowie County|    32| 343.182|  3.064|   764|  8193.469| 85.795|  93,245|
| |Johnson County|    30| 170.632|  4.875| 1,861| 10584.869| 260.011| 175,817|
| |Willacy County|    29| 1357.805| 73.576|   693| 32446.858| 715.690|  21,358|
| |Matagorda County|    27| 736.839| 23.392|   740| 20194.853| 261.208|  36,643|
| |Caldwell County|    26| 595.456|  9.815| 1,145| 26222.975| 245.380|  43,664|
| |Tom Green County|    26| 218.121|  2.397| 2,632| 22080.537| 309.204| 119,200|
| |Hale County|    26| 778.303| 17.106| 1,285| 38466.144| 427.639|  33,406|
| |Gregg County|    26| 209.770|  8.068| 1,416| 11424.422| 118.716| 123,945|
| |San Patricio County|    26| 389.630| 21.408|   935| 14011.689| 295.434|  66,730|
| |Medina County|    26| 504.032|  5.539|   811| 15721.929| 600.962|  51,584|
| |Wharton County|    25| 601.598| 13.751|   711| 17109.443| 299.080|  41,556|
| |Kaufman County|    25| 183.616|  6.295| 2,158| 15849.700| 358.837| 136,154|
| |Smith County|    23| 98.818|  3.683| 2,524| 10844.207| 131.962| 232,751|
| |Taylor County|    23| 166.626|  4.140| 1,126|  8157.410| 45.537| 138,034|
| |Harrison County|    23| 345.589|  2.147|   693| 10412.754| 156.696|  66,553|
| |Grimes County|    23| 796.399| 14.840|   876| 30332.410| 183.023|  28,880|
| |Randall County|    21| 152.491|  4.149| 1,725| 12526.051| 144.192| 137,713|
| |Bastrop County|    21| 236.692|  4.830| 1,363| 15362.420| 107.880|  88,723|
| |Hunt County|    21| 212.995|  1.449| 1,182| 11988.559| 192.709|  98,594|
| |Orange County|    20| 239.820|  6.852| 1,477| 17710.682| 781.127|  83,396|
| |Parker County|    19| 132.981|  6.999| 1,225|  8573.748| 154.977| 142,878|
| |Wilson County|    19| 372.038|  8.392|   439|  8596.045| 69.932|  51,070|
| |DeWitt County|    19| 942.460| 28.345|   693| 34375.000| 1147.959|  20,160|
| |Shelby County|    18| 712.194| 11.305|   401| 15866.107| 124.351|  25,274|
| |Panola County|    18| 776.063|  6.159|   291| 12546.348| 135.503|  23,194|
| |Lamar County|    18| 361.018|  5.730|   644| 12916.424| 68.765|  49,859|
| |Atascosa County|    18| 351.886|  8.378|   437|  8542.998| 89.368|  51,153|
| |Lavaca County|    17| 843.505| 21.265|   627| 31110.450| 241.001|  20,154|
| |Deaf Smith County|    17| 916.640|  0.000|   667| 35964.628| 539.200|  18,546|
| |Brown County|    16| 422.565|  7.546|   391| 10326.431| 150.916|  37,864|
| |Hardin County|    15| 260.408|  9.920|   973| 16891.775| 401.772|  57,602|
| |Titus County|    15| 458.015|  4.362| 1,289| 39358.779|  0.000|  32,750|
| |Jim Wells County|    15| 370.535| 31.760|   724| 17884.492| 469.344|  40,482|
| |Aransas County|    15| 638.026| 18.229|   173|  7358.571| 121.529|  23,510|
| |Fayette County|    14| 552.355|  5.636|   378| 14913.596| 61.999|  25,346|
| |Anderson County|    14| 242.487| 14.846| 2,402| 41603.880| 477.551|  57,735|
| |Grayson County|    13| 95.439|  2.098| 1,118|  8207.794| 118.513| 136,212|
| |Moore County|    13| 620.821|  6.822| 1,050| 50143.266| 252.422|  20,940|
| |Rockwall County|    13| 123.910|  0.000|   896|  8540.247| 239.650| 104,915|
| |Polk County|    12| 233.677|  8.346|   748| 14565.848| 247.586|  51,353|
| |Henderson County|    12| 145.038|  5.180|   641|  7747.441| 110.505|  82,737|
| |Red River County|    11| 914.913|  0.000|   136| 11311.653| 23.764|  12,023|
| |Lamb County|    11| 853.176| 44.321|   226| 17528.892| 254.845|  12,893|
| |San Augustine County|    11| 1335.438|  0.000|   162| 19667.355| 121.403|   8,237|
| |Bee County|    11| 337.786|  8.774| 1,089| 33440.811| 2535.588|  32,565|
| |Jasper County|    11| 309.606| 24.125|   304|  8556.391| 52.271|  35,529|
| |Wichita County|    11| 83.188|  2.161| 1,001|  7570.143| 106.956| 132,230|
| |Lee County|    10| 580.080| 16.574|   173| 10035.385| 174.024|  17,239|
| |Hood County|    10| 162.224|  4.635|   528|  8565.449| 210.892|  61,643|
| |Uvalde County|    10| 373.958| 16.027|   543| 20305.897| 325.877|  26,741|
| |Burnet County|     9| 186.896|  5.933|   557| 11566.815| 44.499|  48,155|
| |Gonzales County|     9| 431.924| 13.712|   683| 32778.231| 452.492|  20,837|
| |Fannin County|     8| 225.263|  0.000|   246|  6926.846| 128.722|  35,514|
| |San Jacinto County|     8| 277.210|  0.000|   177|  6133.269| 158.406|  28,859|
| |Marion County|     8| 811.853| 14.497|   133| 13497.057| 144.974|   9,854|
| |Kleberg County|     8| 260.756| 13.969|   434| 14146.023| 409.760|  30,680|
| |Navarro County|     8| 159.639|  0.000|   856| 17081.396| 253.712|  50,113|
| |Cass County|     8| 266.436|  4.758|   176|  5861.587| 109.429|  30,026|
| |Houston County|     7| 304.772|  6.220|   314| 13671.195| 410.509|  22,968|
| |Jackson County|     7| 474.255| 29.036|   406| 27506.775| 832.365|  14,760|
| |Hill County|     7| 191.001| 15.592|   321|  8758.766| 50.674|  36,649|
| |Wise County|     7| 100.023|  4.083|   409|  5844.193| 200.046|  69,984|
| |Cherokee County|     7| 132.964|  8.141| 1,110| 21084.223| 887.328|  52,646|
| |Andrews County|     7| 374.231|  7.637|   297| 15878.107| 320.770|  18,705|
| |Palo Pinto County|     7| 239.816|  4.894|   265|  9078.763| 347.489|  29,189|
| |Parmer County|     7| 728.787|  0.000|   340| 35398.230| 431.323|   9,605|
| |Wood County|     7| 153.714|  6.274|   316|  6939.107| 78.426|  45,539|
| |Burleson County|     6| 325.327|  7.746|   242| 13121.510| 85.205|  18,443|
| |Sabine County|     6| 569.152|  0.000|    51|  4837.792| 94.859|  10,542|
| |Howard County|     6| 163.648| 11.689|   171|  4663.976| 54.549|  36,664|
| |Camp County|     6| 458.225| 21.820|   233| 17794.410| 207.292|  13,094|
| |Gillespie County|     6| 222.321| 10.587|   175|  6484.363| 21.173|  26,988|
| |Karnes County|     6| 384.591| 18.314|   632| 40510.224| 3058.412|  15,601|
| |Duval County|     6| 537.779| 38.413|   176| 15774.850| 332.911|  11,157|
| |Floyd County|     6| 1050.420| 25.010|    89| 15581.232| 150.060|   5,712|
| |Kerr County|     6| 114.068|  0.000|   398|  7566.540| 135.796|  52,600|
| |Dallam County|     5| 686.153|  0.000|   190| 26073.830| 215.648|   7,287|
| |Erath County|     5| 117.102|  0.000|   527| 12342.498| 217.474|  42,698|
| |Coryell County|     5| 65.832|  0.000|   668|  8795.144| 105.331|  75,951|
| |Zavala County|     5| 422.297|  0.000|   210| 17736.486| 422.297|  11,840|
| |Young County|     5| 277.624|  7.932|   169|  9383.676| 237.963|  18,010|
| |Blanco County|     5| 419.076| 11.974|    98|  8213.897|  0.000|  11,931|
| |Frio County|     5| 246.233|  0.000|   512| 25214.222| 260.303|  20,306|
| |Martin County|     5| 866.401| 49.509|    55|  9530.411| 247.543|   5,771|
| |Calhoun County|     5| 234.852| 13.420|   544| 25551.902| 610.615|  21,290|
| |Waller County|     5| 90.504|  5.172|   444|  8036.781| 116.363|  55,246|
| |Reeves County|     5| 312.969| 17.884|   146|  9138.708| 98.362|  15,976|
| |Kendall County|     4| 84.333|  6.024|   158|  3331.155| 39.155|  47,431|
| |Lynn County|     4| 672.156|  0.000|    67| 11258.612| 48.011|   5,951|
| |Goliad County|     4| 522.330| 18.655|    89| 11621.833| 223.856|   7,658|
| |Refugio County|     4| 575.705| 82.244|   223| 32095.567| 575.705|   6,948|
| |Dawson County|     4| 314.268|  0.000|   145| 11392.206| 89.791|  12,728|
| |Austin County|     4| 133.191|  4.757|   242|  8058.071| 137.948|  30,032|
| |Bailey County|     4| 571.429|  0.000|   171| 24428.571| 265.306|   7,000|
| |Trinity County|     4| 273.019| 19.501|   156| 10647.737| 204.764|  14,651|
| |Hockley County|     4| 173.754|  0.000|   206|  8948.352| 155.138|  23,021|
| |Newton County|     4| 294.226|  0.000|    93|  6840.750| 73.556|  13,595|
| |Castro County|     4| 531.208| 18.972|   200| 26560.425| 569.152|   7,530|
| |Stephens County|     3| 320.307| 15.253|    42|  4484.305| 198.286|   9,366|
| |Van Zandt County|     3| 53.013|  0.000|   375|  6626.612| 108.550|  56,590|
| |Bandera County|     3| 129.803|  0.000|    91|  3937.349| 49.449|  23,112|
| |Reagan County|     3| 779.423|  0.000|    63| 16367.888| 185.577|   3,849|
| |Chambers County|     3| 68.435|  3.259|   951| 21694.003| 208.565|  43,837|
| |Callahan County|     3| 215.162|  0.000|    46|  3299.147| 51.229|  13,943|
| |Crockett County|     3| 866.051|  0.000|   155| 44745.958| 82.481|   3,464|
| |Comanche County|     3| 220.022|  0.000|   142| 10414.375|  0.000|  13,635|
| |Cooke County|     3| 72.715|  3.463|   223|  5405.143| 79.640|  41,257|
| |Gaines County|     3| 139.587| 19.941|   161|  7491.160| 192.763|  21,492|
| |Nolan County|     3| 203.887|  0.000|   134|  9106.973| 29.127|  14,714|
| |Hamilton County|     3| 354.568| 16.884|    83|  9809.715| 472.757|   8,461|
| |Falls County|     3| 173.440|  8.259|   127|  7342.314| 140.404|  17,297|
| |Milam County|     3| 120.856|  0.000|   333| 13414.978| 155.386|  24,823|
| |Dimmit County|     3| 296.326| 28.221|   150| 14816.278| 366.879|  10,124|
| |Morris County|     3| 242.170| 23.064|   116|  9363.901| 230.638|  12,388|
| |Lampasas County|     3| 140.004| 13.334|   104|  4853.463| 133.337|  21,428|
| |Yoakum County|     3| 344.313| 32.792|   102| 11706.645| 278.730|   8,713|
| |Brooks County|     3| 422.952| 40.281|   113| 15931.200| 563.936|   7,093|
| |Hutchinson County|     3| 143.280|  6.823|   126|  6017.767| 81.874|  20,938|
| |Limestone County|     3| 128.003|  0.000|   235| 10026.881| 219.433|  23,437|
| |Garza County|     3| 481.618| 22.934|    99| 15893.402| 45.868|   6,229|
| |Upshur County|     2| 47.901|  0.000|   221|  5293.033| 102.644|  41,753|
| |Leon County|     2| 114.916|  8.208|   143|  8216.502| 41.041|  17,404|
| |Ochiltree County|     2| 203.335|  0.000|    95|  9658.398| 159.763|   9,836|
| |Throckmorton County|     2| 1332.445| 190.349|     4|  2664.890|  0.000|   1,501|
| |Terry County|     2| 162.114| 11.580|   143| 11591.149| 312.648|  12,337|
| |Zapata County|     2| 141.054|  0.000|   172| 12130.616| 161.204|  14,179|
| |Swisher County|     2| 270.380|  0.000|    80| 10815.195| 96.564|   7,397|
| |Hudspeth County|     2| 409.333|  0.000|    23|  4707.327| 29.238|   4,886|
| |Rusk County|     2| 36.761|  0.000|   369|  6782.340| 97.153|  54,406|
| |Culberson County|     2| 921.234|  0.000|    17|  7830.493| 131.605|   2,171|
| |La Salle County|     2| 265.957| 18.997|   362| 48138.298| 94.985|   7,520|
| |Live Oak County|     2| 163.840| 11.703|   230| 18841.648| 269.166|  12,207|
| |Tyler County|     2| 92.285|  6.592|   116|  5352.529|  6.592|  21,672|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Madison County|     2| 140.017|  0.000|   666| 46625.595| 210.025|  14,284|
| |Colorado County|     2| 93.054|  0.000|   281| 13074.024| 259.221|  21,493|
| |Coke County|     2| 590.493| 42.178|    42| 12400.354| 126.534|   3,387|
| |Hansford County|     2| 370.439|  0.000|    73| 13521.022| 370.439|   5,399|
| |Hopkins County|     2| 53.932|  3.852|   199|  5366.196| 115.568|  37,084|
| |Robertson County|     2| 117.137|  8.367|   234| 13705.049| 167.339|  17,074|
| |Presidio County|     2| 298.329| 42.618|    46|  6861.575| 42.618|   6,704|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536| 408.747|   1,398|
| |Franklin County|     2| 186.480| 13.320|    92|  8578.089| 106.560|  10,725|
| |Brewster County|     2| 217.320|  0.000|   188| 20428.121| 108.660|   9,203|
| |Gray County|     2| 91.383|  0.000|   215|  9823.632| 208.875|  21,886|
| |Bosque County|     2| 107.038|  0.000|   161|  8616.537| 275.240|  18,685|
| |Runnels County|     1| 97.428|  0.000|   124| 12081.060| 236.611|  10,264|
| |Real County|     1| 289.687| 41.384|    87| 25202.781| 455.223|   3,452|
| |Rains County|     1| 79.911|  0.000|    51|  4075.436| 68.495|  12,514|
| |Pecos County|     1| 63.199|  0.000|   243| 15357.391| 306.967|  15,823|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788| 67.641|   2,112|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366| 51.148|   2,793|
| |Scurry County|     1| 59.869|  0.000|   481| 28797.222| 410.534|  16,703|
| |Jim Hogg County|     1| 192.308|  0.000|    62| 11923.077| 247.253|   5,200|
| |Wilbarger County|     1| 78.315|  0.000|    69|  5403.712| 212.568|  12,769|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Ward County|     1| 83.347|  0.000|    89|  7417.903| 71.440|  11,998|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Mitchell County|     1| 117.028| 16.718|    61|  7138.678| 150.464|   8,545|
| |Winkler County|     1| 124.844|  0.000|    84| 10486.891| 285.358|   8,010|
| |Sutton County|     1| 264.831|  0.000|    62| 16419.492| 151.332|   3,776|
| |Kimble County|     1| 230.574| 32.939|    13|  2997.464|  0.000|   4,337|
| |Montague County|     1| 50.459|  0.000|    70|  3532.142| 93.710|  19,818|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966| 92.404|   1,546|
| |McCulloch County|     1| 125.251|  0.000|    48|  6012.024| 125.251|   7,984|
| |Fisher County|     1| 261.097|  0.000|    28|  7310.705| 149.198|   3,830|
| |Llano County|     1| 45.882|  0.000|    89|  4083.505| 19.664|  21,795|
| |Clay County|     1| 95.502|  0.000|    40|  3820.074| 81.859|  10,471|
| |Knox County|     1| 272.926| 38.989|    60| 16375.546| 545.852|   3,664|
| |Crosby County|     1| 174.307|  0.000|    63| 10981.349| 273.911|   5,737|
| |Hall County|     1| 337.382|  0.000|    11|  3711.201| 144.592|   2,964|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420| 64.612|   2,211|
| |Eastland County|     1| 54.466|  0.000|    73|  3976.035| 171.180|  18,360|
| |Foard County|     0|  0.000|  0.000|     2|  1731.602|  0.000|   1,155|
| |Concho County|     0|  0.000|  0.000|    28| 10271.460| 104.811|   2,726|
| |Delta County|     0|  0.000|  0.000|    16|  3001.313| 53.595|   5,331|
| |Donley County|     0|  0.000|  0.000|    48| 14643.075| 217.903|   3,278|
| |Edwards County|     0|  0.000|  0.000|    28| 14492.754| 295.770|   1,932|
| |Collingsworth County|     0|  0.000|  0.000|    11|  3767.123| 195.695|   2,920|
| |Carson County|     0|  0.000|  0.000|    15|  2531.218| 48.214|   5,926|
| |Childress County|     0|  0.000|  0.000|    40|  5474.952| 117.320|   7,306|
| |Cochran County|     0|  0.000|  0.000|    32| 11216.264| 550.799|   2,853|
| |Coleman County|     0|  0.000|  0.000|    19|  2324.159| 139.799|   8,175|
| |Archer County|     0|  0.000|  0.000|    21|  2455.279| 16.703|   8,553|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Baylor County|     0|  0.000|  0.000|    11|  3134.796| 162.847|   3,509|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |McMullen County|     0|  0.000|  0.000|     9| 12113.055| 192.271|     743|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Jones County|     0|  0.000|  0.000|   596| 29676.841|  0.000|  20,083|
| |Kinney County|     0|  0.000|  0.000|    19|  5181.347| 77.915|   3,667|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008| 187.477|     762|
| |Freestone County|     0|  0.000|  0.000|   156|  7911.954| 130.417|  19,717|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000| 238.095|   1,200|
| |Mason County|     0|  0.000|  0.000|    53| 12400.562| 434.521|   4,274|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Mills County|     0|  0.000|  0.000|    22|  4514.673| 205.212|   4,873|
| |Menard County|     0|  0.000|  0.000|    17|  7951.356| 66.818|   2,138|
| |Hartley County|     0|  0.000|  0.000|    85| 15243.902| 76.860|   5,576|
| |Haskell County|     0|  0.000|  0.000|    42|  7423.118| 176.741|   5,658|
| |Jack County|     0|  0.000|  0.000|    59|  6603.246| 303.781|   8,935|
| |Lipscomb County|     0|  0.000|  0.000|    18|  5567.584| 132.562|   3,233|
| |Hemphill County|     0|  0.000|  0.000|    42| 10997.643| 37.407|   3,819|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Hardeman County|     0|  0.000|  0.000|    18|  4576.659| 108.968|   3,933|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Somervell County|     0|  0.000|  0.000|    74|  8106.924| 250.407|   9,128|
| |San Saba County|     0|  0.000|  0.000|    24|  3963.666| 47.187|   6,055|
| |Shackelford County|     0|  0.000|  0.000|    18|  5513.017| 43.754|   3,265|
| |Sherman County|     0|  0.000|  0.000|    40| 13236.267| 141.817|   3,022|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |Sterling County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,291|
| |Wheeler County|     0|  0.000|  0.000|    33|  6526.899| 56.510|   5,056|
| |Stonewall County|     0|  0.000|  0.000|     5|  3703.704| 105.820|   1,350|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,728| 1266.303| N/A|120,612| 17499.013| N/A|6,892,503|
| |Middlesex County| 2,003| 1242.788|  1.595|26,420| 16392.639| 46.623|1,611,699|
| |Essex County| 1,193| 1511.975|  1.811|17,846| 22617.530| 83.284| 789,034|
| |Suffolk County| 1,074| 1335.975|  2.843|21,849| 27178.517| 87.786| 803,907|
| |Worcester County| 1,005| 1209.937|  2.236|13,630| 16409.390| 36.977| 830,622|
| |Norfolk County|   997| 1410.633|  1.819|10,614| 15017.509| 54.776| 706,775|
| |Plymouth County|   721| 1383.341|  2.467| 9,245| 17737.844| 35.632| 521,202|
| |Hampden County|   707| 1515.957|  2.757| 7,600| 16296.004| 40.740| 466,372|
| |Bristol County|   634| 1121.693|  2.275| 9,355| 16551.165| 58.385| 565,217|
| |Barnstable County|   158| 741.819|  0.671| 1,800|  8451.101| 28.841| 212,990|
| |Hampshire County|   129| 802.089|  1.776| 1,174|  7299.633| 33.753| 160,830|
| |Franklin County|    61| 869.194|  2.036|   411|  5856.369| 12.213|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   668|  5346.395| 12.577| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 8,186| 381.139| N/A|532,111| 24775.003| N/A|21,477,737|
| |Miami-Dade County| 1,865| 686.434| 10.306|132,461| 48753.745| 513.761|2,716,940|
| |Palm Beach County|   931| 622.006|  9.353|37,020| 24733.259| 266.669|1,496,770|
| |Broward County|   803| 411.209|  4.243|62,268| 31886.881| 314.058|1,952,778|
| |Pinellas County|   500| 512.823|  8.938|17,879| 18337.511| 161.905| 974,996|
| |Hillsborough County|   388| 263.593|  3.979|32,587| 22138.389| 239.621|1,471,968|
| |Lee County|   334| 433.441|  6.303|16,529| 21450.160| 158.508| 770,577|
| |Polk County|   312| 430.477|  8.081|14,301| 19731.586| 258.207| 724,777|
| |Orange County|   298| 213.857|  6.561|31,719| 22762.894| 207.091|1,393,452|
| |Manatee County|   192| 476.128|  2.126| 9,288| 23032.687| 196.615| 403,253|
| |Duval County|   188| 196.292|  4.475|23,437| 24470.768| 264.309| 957,755|
| |St. Lucie County|   166| 505.640| 18.276| 5,772| 17581.641| 244.552| 328,297|
| |Brevard County|   151| 250.855|  8.069| 6,064| 10074.060| 113.205| 601,942|
| |Sarasota County|   139| 320.467|  5.928| 6,231| 14365.683| 166.985| 433,742|
| |Collier County|   136| 353.337|  4.454|10,334| 26848.393| 222.691| 384,902|
| |Volusia County|   135| 243.998|  5.164| 7,876| 14235.004| 201.137| 553,284|
| |Pasco County|   128| 231.069|  7.995| 7,080| 12781.006| 154.992| 553,947|
| |Escambia County|   120| 376.984| 10.322| 9,508| 29869.689| 673.634| 318,316|
| |Seminole County|   119| 252.212|  9.689| 7,118| 15086.070| 145.029| 471,826|
| |Osceola County|   104| 276.779|  9.125| 9,696| 25804.323| 347.495| 375,751|
| |Martin County|    94| 583.851| 14.197| 3,825| 23757.764| 166.815| 161,000|
| |Charlotte County|    91| 481.711|  1.512| 2,238| 11846.911| 161.831| 188,910|
| |Marion County|    89| 243.449| 10.942| 6,511| 17810.104| 522.850| 365,579|
| |Lake County|    68| 185.227|  6.615| 5,161| 14058.150| 194.566| 367,118|
| |Indian River County|    56| 350.169|  7.146| 2,523| 15776.342| 197.416| 159,923|
| |Bay County|    51| 291.921| 24.531| 4,440| 25414.270| 627.180| 174,705|
| |Clay County|    51| 232.609|  1.955| 3,282| 14969.077| 243.686| 219,252|
| |Hernando County|    47| 242.368| 10.314| 2,022| 10426.980| 201.114| 193,920|
| |Suwannee County|    43| 968.098| 35.379| 1,454| 32735.214| 910.205|  44,417|
| |Okaloosa County|    41| 194.554|  7.457| 3,502| 16617.791| 387.075| 210,738|
| |Sumter County|    41| 309.621|  9.709| 1,303|  9839.903| 185.557| 132,420|
| |Jackson County|    38| 818.718| 15.389| 1,821| 39233.852| 640.201|  46,414|
| |Hendry County|    38| 904.288|  3.400| 1,762| 41930.417| 373.954|  42,022|
| |Highlands County|    37| 348.330| 10.759| 1,435| 13509.570| 246.118| 106,221|
| |Santa Rosa County|    37| 200.745| 10.076| 3,939| 21371.254| 375.913| 184,313|
| |Citrus County|    36| 240.550|  5.727| 1,539| 10283.515| 236.732| 149,657|
| |St. Johns County|    34| 128.461|  2.699| 3,635| 13733.980| 168.403| 264,672|
| |Alachua County|    26| 96.639|  1.593| 4,142| 15395.309| 254.872| 269,043|
| |Putnam County|    26| 348.895| 13.419| 1,508| 20235.907| 268.381|  74,521|
| |Leon County|    24| 81.749|  4.866| 4,965| 16911.800| 281.255| 293,582|
| |Gadsden County|    21| 459.921|  3.129| 1,884| 41261.498| 1038.733|  45,660|
| |DeSoto County|    16| 421.042|  3.759| 1,351| 35551.696| 221.799|  38,001|
| |Walton County|    15| 202.508|  3.857| 1,408| 19008.789| 314.370|  74,071|
| |Columbia County|    15| 209.246|  9.964| 2,873| 40077.560| 599.838|  71,686|
| |Washington County|    14| 549.602|  0.000|   867| 34036.038| 1553.466|  25,473|
| |Monroe County|    13| 175.136|  3.849| 1,526| 20558.280| 325.253|  74,228|
| |Flagler County|    13| 112.964|  3.724| 1,070|  9297.799| 173.791| 115,081|
| |Okeechobee County|    12| 284.576| 20.327| 1,039| 24639.537| 318.454|  42,168|
| |Nassau County|    11| 124.118|  1.612| 1,233| 13912.553| 207.939|  88,625|
| |Madison County|     8| 432.596|  7.725|   700| 37852.160| 440.321|  18,493|
| |Calhoun County|     7| 496.278|  0.000|   475| 33676.001| 1579.987|  14,105|
| |Hardee County|     7| 259.866|  0.000|   963| 35750.084| 562.158|  26,937|
| |Liberty County|     6| 718.219| 68.402|   400| 47881.254|  0.000|   8,354|
| |Union County|     5| 328.149|  9.376|   310| 20345.212| 796.932|  15,237|
| |Jefferson County|     5| 350.976|  0.000|   453| 31798.400| 1093.039|  14,246|
| |Bradford County|     4| 141.839|  0.000|   494| 17517.109| 795.311|  28,201|
| |Baker County|     4| 136.939|  0.000|   907| 31051.010| 2548.051|  29,210|
| |Levy County|     4| 96.379|  3.442|   684| 16480.736| 306.346|  41,503|
| |Dixie County|     4| 237.727|  0.000|   547| 32509.212| 2334.822|  16,826|
| |Taylor County|     4| 185.451|  6.623|   961| 44554.685| 3901.101|  21,569|
| |Wakulla County|     4| 118.557|  0.000|   692| 20510.389| 342.969|  33,739|
| |Hamilton County|     4| 277.239|  9.901|   618| 42833.380| 306.943|  14,428|
| |Glades County|     3| 217.218|  0.000|   401| 29034.827| 103.437|  13,811|
| |Gilchrist County|     3| 161.447|  0.000|   363| 19535.034| 222.950|  18,582|
| |Holmes County|     2| 101.952|  0.000|   505| 25742.978| 436.939|  19,617|
| |Gulf County|     2| 146.638|  0.000|   648| 47510.815| 2817.551|  13,639|
| |Franklin County|     2| 164.948|  0.000|   418| 34474.227| 3393.225|  12,125|
| |Lafayette County|     1| 118.737|  0.000|   146| 17335.550| 610.646|   8,422|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,636| 602.597| N/A|194,012| 15310.507| N/A|12,671,821|
| |Cook County| 4,928| 956.850|  0.943|111,447| 21639.215| 131.312|5,150,233|
| |DuPage County|   520| 563.429|  1.548|12,233| 13254.656| 118.103| 922,921|
| |Lake County|   446| 640.312|  1.231|12,670| 18190.041| 141.107| 696,535|
| |Will County|   344| 498.014|  1.034| 9,236| 13371.109| 133.190| 690,743|
| |Kane County|   305| 572.874|  1.878| 9,759| 18330.100| 149.994| 532,403|
| |St. Clair County|   161| 619.980|  2.751| 4,006| 15426.323| 217.846| 259,686|
| |Winnebago County|   131| 463.599|  3.539| 3,779| 13373.583| 53.589| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,189| 10361.499| 115.112| 307,774|
| |Madison County|    76| 289.011|  1.630| 2,591|  9852.985| 220.018| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,782| 16220.349| 127.433| 109,862|
| |Rock Island County|    36| 253.737|  5.034| 1,745| 12299.213| 163.117| 141,879|
| |Peoria County|    35| 195.335|  0.797| 1,607|  8968.685| 243.173| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,247|  6405.646| 171.717| 194,672|
| |DeKalb County|    30| 285.995|  1.362|   936|  8923.039| 122.569| 104,897|
| |LaSalle County|    24| 220.854|  7.888|   766|  7048.928| 329.967| 108,669|
| |Boone County|    23| 429.553|  0.000|   765| 14287.315| 98.717|  53,544|
| |Kendall County|    23| 178.308|  0.000| 1,377| 10675.246| 102.998| 128,990|
| |Macon County|    23| 221.135|  0.000|   624|  5999.481| 207.400| 104,009|
| |Union County|    23| 1381.133| 17.157|   321| 19275.806| 154.412|  16,653|
| |Coles County|    20| 395.093|  2.822|   472|  9324.194| 206.013|  50,621|
| |Jefferson County|    19| 504.193|  7.582|   286|  7589.428| 375.301|  37,684|
| |Champaign County|    19| 90.610|  0.000| 1,669|  7959.407| 85.160| 209,689|
| |Jackson County|    19| 334.802|  0.000|   717| 12634.361| 183.763|  56,750|
| |Clinton County|    17| 452.585|  0.000|   407| 10835.419| 262.423|  37,562|
| |Whiteside County|    17| 308.111|  2.589|   355|  6434.073| 121.691|  55,175|
| |McDonough County|    15| 505.357|  0.000|   143|  4817.735| 72.194|  29,682|
| |McLean County|    15| 87.455|  0.000|   651|  3795.542| 74.128| 171,517|
| |Monroe County|    13| 375.321|  0.000|   318|  9180.934| 164.976|  34,637|
| |Iroquois County|    11| 405.694| 21.075|   263|  9699.786| 42.150|  27,114|
| |Cass County|    11| 905.573|  0.000|   231| 19017.041| 341.060|  12,147|
| |Tazewell County|     8| 60.697|  0.000|   518|  3930.108| 161.496| 131,803|
| |Montgomery County|     7| 246.357|  0.000|   170|  5982.966| 135.748|  28,414|
| |Randolph County|     7| 220.250|  0.000|   464| 14599.459| 143.837|  31,782|
| |Jasper County|     7| 728.408|  0.000|    59|  6139.438| 74.327|   9,610|
| |Morgan County|     6| 178.264|  4.244|   249|  7397.944| 224.952|  33,658|
| |Stephenson County|     6| 134.838|  0.000|   327|  7348.645| 32.104|  44,498|
| |Williamson County|     6| 90.094|  2.145|   399|  5991.261| 150.157|  66,597|
| |Adams County|     5| 76.412|  6.550|   519|  7931.535| 207.403|  65,435|
| |Grundy County|     5| 97.936|  0.000|   323|  6326.635| 117.523|  51,054|
| |Ogle County|     5| 98.730|  0.000|   410|  8095.887| 110.014|  50,643|
| |Carroll County|     4| 279.623|  9.987|    56|  3914.715| 109.852|  14,305|
| |Christian County|     4| 123.824|  0.000|   142|  4395.740| 128.246|  32,304|
| |Mercer County|     4| 259.118| 37.017|    75|  4858.457| 46.271|  15,437|
| |Fayette County|     3| 140.607|  0.000|    66|  3093.363| 73.652|  21,336|
| |Macoupin County|     3| 66.776|  0.000|   179|  3984.330| 139.913|  44,926|
| |Bureau County|     3| 91.946|  4.378|   205|  6282.947| 280.215|  32,628|
| |Bond County|     3| 182.637|  8.697|    60|  3652.746| 52.182|  16,426|
| |Woodford County|     3| 78.005|  0.000|   151|  3926.259| 208.014|  38,459|
| |Jersey County|     2| 91.857|  6.561|   105|  4822.487| 236.203|  21,773|
| |Gallatin County|     2| 414.250| 59.179|    51| 10563.380| 177.536|   4,828|
| |Ford County|     2| 154.309| 11.022|    49|  3780.572| 88.177|  12,961|
| |Livingston County|     2| 56.104|  0.000|   115|  3225.987| 92.171|  35,648|
| |Douglas County|     2| 102.749|  0.000|   116|  5959.414| 102.749|  19,465|
| |Clark County|     2| 129.525| 18.504|    82|  5310.537| 148.029|  15,441|
| |Saline County|     2| 85.139|  6.081|   132|  5619.173| 127.708|  23,491|
| |Vermilion County|     2| 26.400|  0.000|   234|  3088.783| 41.485|  75,758|
| |Cumberland County|     2| 185.770|  0.000|    55|  5108.675| 119.424|  10,766|
| |Lee County|     1| 29.329|  0.000|   171|  5015.251| 104.746|  34,096|
| |Perry County|     1| 47.810|  0.000|   184|  8797.093| 396.142|  20,916|
| |Pulaski County|     1| 187.441| 26.777|    93| 17432.052| 53.555|   5,335|
| |Knox County|     1| 20.121|  0.000|   299|  6016.218| 114.978|  49,699|
| |Jo Daviess County|     1| 47.092|  0.000|   125|  5886.508| 87.457|  21,235|
| |Shelby County|     1| 46.224|  0.000|    79|  3651.659| 125.464|  21,634|
| |Wayne County|     1| 61.671|  0.000|    61|  3761.949| 149.773|  16,215|
| |Effingham County|     1| 29.405|  0.000|   155|  4557.751| 176.429|  34,008|
| |Hancock County|     1| 56.472|  0.000|    53|  2992.998| 169.415|  17,708|
| |Henry County|     1| 20.444|  0.000|   234|  4784.004| 84.698|  48,913|
| |Marion County|     0|  0.000|  0.000|   156|  4192.985| 76.795|  37,205|
| |Brown County|     0|  0.000|  0.000|    14|  2128.306| 21.717|   6,578|
| |Logan County|     0|  0.000|  0.000|   112|  3913.621| 134.780|  28,618|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203| 149.354|   5,739|
| |Richland County|     0|  0.000|  0.000|    19|  1224.779| 64.462|  15,513|
| |Mason County|     0|  0.000|  0.000|    47|  3518.227| 53.469|  13,359|
| |Schuyler County|     0|  0.000|  0.000|    18|  2659.574| 42.215|   6,768|
| |Scott County|     0|  0.000|  0.000|    21|  4241.567| 317.396|   4,951|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Wabash County|     0|  0.000|  0.000|    35|  3038.194| 37.202|  11,520|
| |Warren County|     0|  0.000|  0.000|   190| 11279.981| 84.812|  16,844|
| |Washington County|     0|  0.000|  0.000|    66|  4752.646| 92.584|  13,887|
| |Massac County|     0|  0.000|  0.000|    39|  2831.833| 51.865|  13,772|
| |Pope County|     0|  0.000|  0.000|     9|  2154.656| 34.201|   4,177|
| |Menard County|     0|  0.000|  0.000|    56|  4591.669| 117.134|  12,196|
| |White County|     0|  0.000|  0.000|    68|  5023.270| 116.084|  13,537|
| |Marshall County|     0|  0.000|  0.000|    26|  2273.125| 62.448|  11,438|
| |Piatt County|     0|  0.000|  0.000|    61|  3732.256| 148.591|  16,344|
| |Moultrie County|     0|  0.000|  0.000|    73|  5034.136| 197.031|  14,501|
| |Pike County|     0|  0.000|  0.000|    21|  1349.528| 73.444|  15,561|
| |Franklin County|     0|  0.000|  0.000|   178|  4627.102| 181.965|  38,469|
| |Fulton County|     0|  0.000|  0.000|    33|   960.978| 29.121|  34,340|
| |Greene County|     0|  0.000|  0.000|    43|  3315.599| 264.367|  12,969|
| |Lawrence County|     0|  0.000|  0.000|    47|  2997.831| 45.560|  15,678|
| |Johnson County|     0|  0.000|  0.000|    67|  5395.828| 115.050|  12,417|
| |Henderson County|     0|  0.000|  0.000|    12|  1805.597| 64.486|   6,646|
| |Alexander County|     0|  0.000|  0.000|    37|  6422.496| 24.797|   5,761|
| |Edwards County|     0|  0.000|  0.000|    18|  2814.699| 111.694|   6,395|
| |Edgar County|     0|  0.000|  0.000|    28|  1631.607| 16.649|  17,161|
| |De Witt County|     0|  0.000|  0.000|    33|  2110.244| 36.541|  15,638|
| |Crawford County|     0|  0.000|  0.000|    29|  1553.544|  0.000|  18,667|
| |Clay County|     0|  0.000|  0.000|    23|  1744.539| 97.521|  13,184|
| |Calhoun County|     0|  0.000|  0.000|     9|  1899.135| 60.290|   4,739|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809| 37.387|   3,821|
| |Hamilton County|     0|  0.000|  0.000|    29|  3573.189| 123.213|   8,116|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,311| 571.083| N/A|123,312|  9632.253| N/A|12,801,989|
| |Philadelphia County| 1,698| 1071.926| N/A|31,120| 19645.671| N/A|1,584,064|
| |Montgomery County|   857| 1031.393|  1.203|10,121| 12180.548| 49.171| 830,915|
| |Delaware County|   698| 1231.590|  2.773| 9,226| 16278.869| 106.371| 566,747|
| |Bucks County|   582| 926.353|  0.682| 7,197| 11455.266| 45.931| 628,270|
| |Lancaster County|   411| 753.128|  1.047| 5,923| 10853.472| 70.418| 545,724|
| |Berks County|   368| 873.769|  1.018| 5,382| 12778.870| 65.126| 421,164|
| |Chester County|   349| 664.776|  0.000| 5,102|  9718.299| 59.049| 524,989|
| |Lehigh County|   337| 912.493|  0.774| 4,968| 13451.822| 46.031| 369,318|
| |Northampton County|   292| 956.483|  0.936| 3,928| 12866.666| 31.820| 305,285|
| |Allegheny County|   247| 203.117|  1.527| 8,857|  7283.448| 72.248|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,932|  9214.304| 21.803| 209,674|
| |Luzerne County|   184| 579.679|  0.450| 3,448| 10862.682| 55.808| 317,417|
| |Dauphin County|   159| 571.328|  2.053| 2,801| 10064.715| 73.918| 278,299|
| |Monroe County|   124| 728.251|  0.839| 1,634|  9596.467| 36.077| 170,271|
| |York County|    93| 207.100|  1.591| 2,572|  5727.545| 78.577| 449,058|
| |Beaver County|    92| 561.219|  2.614| 1,316|  8027.866| 73.202| 163,929|
| |Cumberland County|    71| 280.223|  0.564| 1,286|  5075.581| 34.394| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,610| 11354.580| 39.293| 141,793|
| |Schuylkill County|    51| 360.784|  2.021|   916|  6479.955| 24.254| 141,359|
| |Franklin County|    46| 296.723|  0.000| 1,350|  8708.161| 63.583| 155,027|
| |Westmoreland County|    46| 131.843|  0.000| 1,537|  4405.286| 40.536| 348,899|
| |Columbia County|    35| 538.760|  0.000|   471|  7250.169| 21.990|  64,964|
| |Carbon County|    28| 436.259|  0.000|   372|  5796.018| 26.710|  64,182|
| |Susquehanna County|    27| 669.510|  3.542|   214|  5306.487| 14.170|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  2.560|  55,809|
| |Adams County|    20| 194.158|  0.000|   518|  5028.687| 61.021| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   391|  3451.045| 68.088| 113,299|
| |Erie County|    19| 70.441|  1.589| 1,102|  4085.597| 71.501| 269,728|
| |Lawrence County|    16| 187.108|  6.682|   391|  4572.458| 80.189|  85,512|
| |Butler County|    15| 79.850|  0.000|   661|  3518.709| 44.868| 187,853|
| |Northumberland County|    13| 143.104|  3.145|   466|  5129.729| 99.072|  90,843|
| |Washington County|    12| 58.009|  0.691|   840|  4060.619| 58.009| 206,865|
| |Centre County|    10| 61.582|  0.000|   372|  2290.852| 13.196| 162,385|
| |Wayne County|     9| 175.230|  2.781|   160|  3115.204|  5.563|  51,361|
| |Mercer County|     9| 82.249|  0.000|   437|  3993.639| 116.193| 109,424|
| |Wyoming County|     8| 298.574|  0.000|    60|  2239.307| 15.995|  26,794|
| |Armstrong County|     7| 108.133|  2.207|   212|  3274.890| 55.170|  64,735|
| |Indiana County|     6| 71.367|  0.000|   320|  3806.216| 81.562|  84,073|
| |Juniata County|     6| 242.297|  0.000|   132|  5330.533| 34.614|  24,763|
| |Blair County|     5| 41.041|  2.345|   284|  2331.136| 70.356| 121,829|
| |Clinton County|     5| 129.426|  0.000|   120|  3106.233| 18.489|  38,632|
| |Perry County|     5| 108.057|  0.000|   124|  2679.806| 12.349|  46,272|
| |Fayette County|     5| 38.678|  1.105|   494|  3821.341| 95.036| 129,274|
| |Bedford County|     4| 83.528|  0.000|   142|  2965.252| 35.798|  47,888|
| |Huntingdon County|     4| 88.605|  0.000|   308|  6822.612| 63.290|  45,144|
| |Bradford County|     3| 49.732|  0.000|    85|  1409.081|  9.473|  60,323|
| |Cambria County|     3| 23.043|  0.000|   336|  2580.804| 75.712| 130,192|
| |Montour County|     3| 164.564|  0.000|   102|  5595.173| 70.527|  18,230|
| |Tioga County|     3| 73.908|  3.519|    38|   936.168| 10.558|  40,591|
| |Somerset County|     3| 40.846|  1.945|   134|  1824.445| 19.450|  73,447|
| |Snyder County|     2| 49.539|  0.000|   104|  2576.043| 24.770|  40,372|
| |Union County|     2| 44.521|  0.000|   225|  5008.570| 168.542|  44,923|
| |Elk County|     2| 66.867|  0.000|    48|  1604.814| 19.105|  29,910|
| |Clarion County|     2| 52.032|  0.000|    80|  2081.274| 14.866|  38,438|
| |Fulton County|     2| 137.646|  0.000|    27|  1858.224| 29.496|  14,530|
| |Greene County|     1| 27.599|  0.000|   116|  3201.501| 31.542|  36,233|
| |McKean County|     1| 24.615|  0.000|    34|   836.923| 21.099|  40,625|
| |Mifflin County|     1| 21.674|  0.000|   120|  2600.893| 43.348|  46,138|
| |Jefferson County|     1| 23.028|  0.000|    71|  1635.003| 42.767|  43,425|
| |Crawford County|     1| 11.816|  0.000|   144|  1701.544| 28.697|  84,629|
| |Warren County|     1| 25.516|  0.000|    23|   586.869| 18.226|  39,191|
| |Venango County|     0|  0.000|  0.000|    63|  1243.388|  2.819|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Potter County|     0|  0.000|  0.000|    20|  1210.214|  0.000|  16,526|
| |Cameron County|     0|  0.000|  0.000|     7|  1574.095| 32.124|   4,447|
| |Clearfield County|     0|  0.000|  0.000|   172|  2170.210| 64.890|  79,255|
| |Forest County|     0|  0.000|  0.000|    10|  1379.881| 19.713|   7,247|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,443| 645.148| N/A|92,022|  9214.310| N/A|9,986,857|
| |Wayne County| 2,824| 1614.320|  1.797|28,163| 16099.187| 75.865|1,749,343|
| |Oakland County| 1,129| 897.753|  0.341|15,501| 12326.016| 82.244|1,257,584|
| |Macomb County|   946| 1082.415|  1.635|10,433| 11937.453| 135.833| 873,972|
| |Genesee County|   296| 729.400|  0.704| 3,648|  8989.362| 53.156| 405,813|
| |Kent County|   157| 238.981|  0.652| 7,523| 11451.317| 70.672| 656,955|
| |Saginaw County|   131| 687.523|  1.500| 2,010| 10549.021| 123.709| 190,539|
| |Washtenaw County|   113| 307.399|  0.389| 2,542|  6915.106| 54.018| 367,601|
| |Kalamazoo County|    83| 313.130|  1.078| 1,639|  6183.366| 50.122| 265,066|
| |Berrien County|    66| 430.245|  0.931| 1,363|  8885.209| 67.051| 153,401|
| |Muskegon County|    59| 339.928|  0.823| 1,178|  6787.044| 44.446| 173,566|
| |Ottawa County|    56| 191.893|  0.979| 1,827|  6260.494| 47.973| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   812|  5102.810| 34.114| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   789|  5881.081| 44.723| 134,159|
| |Jackson County|    34| 214.498|  0.901|   709|  4472.904| 22.531| 158,510|
| |Lapeer County|    33| 376.682|  1.631|   466|  5319.210| 83.164|  87,607|
| |Bay County|    31| 300.603|  0.000|   628|  6089.638| 112.207| 103,126|
| |Ingham County|    30| 102.597|  0.000| 1,551|  5304.269| 33.710| 292,406|
| |Tuscola County|    29| 555.077|  5.469|   350|  6699.206| 117.578|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   341|  5005.725| 37.747|  68,122|
| |Livingston County|    28| 145.837|  0.000|   829|  4317.821| 37.947| 191,995|
| |Hillsdale County|    25| 548.186|  0.000|   267|  5854.621| 50.120|  45,605|
| |Monroe County|    24| 159.468|  1.898|   984|  6538.206| 93.972| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   156|  3831.888| 42.109|  40,711|
| |Cass County|    14| 270.338| 11.034|   321|  6198.467| 82.757|  51,787|
| |Alpena County|    13| 457.666|  0.000|   128|  4506.249| 15.088|  28,405|
| |Clinton County|    13| 163.327|  0.000|   423|  5314.404| 17.948|  79,595|
| |Lenawee County|    12| 121.888|  0.000|   430|  4367.655| 55.140|  98,451|
| |Iosco County|    12| 477.574|  0.000|   131|  5213.515| 11.371|  25,127|
| |Marquette County|    11| 164.920|  0.000|   159|  2383.844| 49.262|  66,699|
| |Otsego County|    10| 405.383|  0.000|   135|  5472.677| 23.165|  24,668|
| |Midland County|    10| 120.256|  0.000|   335|  4028.573| 41.231|  83,156|
| |Van Buren County|     9| 118.926|  0.000|   445|  5880.254| 69.846|  75,677|
| |Isabella County|     9| 128.807|  0.000|   207|  2962.560| 14.312|  69,872|
| |St. Joseph County|     8| 131.225|  2.343|   588|  9645.036| 72.642|  60,964|
| |Eaton County|     8| 72.551|  1.296|   462|  4189.792| 10.364| 110,268|
| |Ionia County|     7| 108.197|  4.416|   273|  4219.670| 17.665|  64,697|
| |Allegan County|     6| 50.813|  0.000|   529|  4479.976| 26.616| 118,081|
| |Oceana County|     6| 226.697|  0.000|   475| 17946.877| 53.976|  26,467|
| |Sanilac County|     6| 145.737|  0.000|   106|  2574.690| 38.169|  41,170|
| |Grand Traverse County|     5| 53.713|  0.000|   209|  2245.187| 13.812|  93,088|
| |Crawford County|     5| 356.405|  0.000|   106|  7555.777| 91.647|  14,029|
| |Kalkaska County|     4| 221.754|  0.000|    52|  2882.803| 31.679|  18,038|
| |Huron County|     4| 129.111|  0.000|   156|  5035.344| 46.111|  30,981|
| |Wexford County|     4| 118.938|  0.000|    69|  2051.679| 21.239|  33,631|
| |Clare County|     3| 96.931|  0.000|    71|  2294.023| 50.773|  30,950|
| |Delta County|     3| 83.836|  0.000|    96|  2682.763| 63.875|  35,784|
| |Arenac County|     3| 201.572|  0.000|    42|  2822.012| 19.197|  14,883|
| |Ogemaw County|     2| 95.252|  0.000|    54|  2571.796| 20.411|  20,997|
| |Charlevoix County|     2| 76.502|  0.000|    49|  1874.307| 38.251|  26,143|
| |Cheboygan County|     2| 79.126|  0.000|    49|  1938.598| 62.171|  25,276|
| |Emmet County|     2| 59.853|  0.000|    62|  1855.454| 25.651|  33,415|
| |Gladwin County|     2| 78.589|  0.000|    58|  2279.068| 33.681|  25,449|
| |Mecosta County|     2| 46.027|  0.000|    69|  1587.923| 42.739|  43,453|
| |Barry County|     2| 32.494|  0.000|   181|  2940.699| 23.210|  61,550|
| |Branch County|     2| 45.959|  0.000|   365|  8387.527| 124.746|  43,517|
| |Dickinson County|     2| 79.242|  0.000|    55|  2179.167| 56.602|  25,239|
| |Presque Isle County|     1| 79.416|  0.000|    20|  1588.310| 34.035|  12,592|
| |Oscoda County|     1| 121.344|  0.000|    24|  2912.268|  0.000|   8,241|
| |Montmorency County|     1| 107.204| 15.315|     9|   964.837| 15.315|   9,328|
| |Montcalm County|     1| 15.652|  0.000|   191|  2989.607| 24.597|  63,888|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122| 13.730|  10,405|
| |Benzie County|     1| 56.287|  0.000|    28|  1576.044|  0.000|  17,766|
| |Gogebic County|     1| 71.556|  0.000|   119|  8515.206| 235.114|  13,975|
| |Iron County|     1| 90.367|  0.000|    19|  1716.971| 25.819|  11,066|
| |Missaukee County|     1| 66.146|  0.000|    41|  2711.999|  9.449|  15,118|
| |Luce County|     0|  0.000|  0.000|     3|   481.618|  0.000|   6,229|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128| 17.650|   8,094|
| |Ontonagon County|     0|  0.000|  0.000|    12|  2097.902| 199.800|   5,720|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  6.089|  23,460|
| |Roscommon County|     0|  0.000|  0.000|    53|  2206.586| 29.738|  24,019|
| |Newaygo County|     0|  0.000|  0.000|   250|  5104.124| 11.667|  48,980|
| |Menominee County|     0|  0.000|  0.000|   134|  5882.353| 250.847|  22,780|
| |Mason County|     0|  0.000|  0.000|   101|  3465.550| 19.607|  29,144|
| |Manistee County|     0|  0.000|  0.000|    35|  1425.197|  5.817|  24,558|
| |Mackinac County|     0|  0.000|  0.000|    27|  2500.232| 105.830|  10,799|
| |Leelanau County|     0|  0.000|  0.000|    72|  3308.671| 52.519|  21,761|
| |Lake County|     0|  0.000|  0.000|    22|  1856.070| 60.262|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     3|  1417.769|  0.000|   2,116|
| |Houghton County|     0|  0.000|  0.000|    50|  1401.188| 12.010|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    40|  1070.979| 30.599|  37,349|
| |Antrim County|     0|  0.000|  0.000|    41|  1757.846| 18.375|  23,324|
| |Alger County|     0|  0.000|  0.000|    11|  1207.729| 47.054|   9,108|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|


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
|AZ|15 counties| 4,149| 570.018| N/A|186,923| 25680.762| N/A|7,278,717|
| |Maricopa County| 2,353| 524.589|  8.026|126,053| 28102.869| 183.898|4,485,414|
| |Pima County|   489| 466.924|  3.683|17,880| 17072.814| 167.100|1,047,279|
| |Yuma County|   288| 1347.135| 19.378|11,510| 53838.634| 245.906| 213,787|
| |Navajo County|   200| 1803.036| 15.455| 5,374| 48447.586| 132.652| 110,924|
| |Mohave County|   168| 791.777| 10.099| 3,186| 15015.482| 107.051| 212,181|
| |Pinal County|   156| 337.087|  4.630| 8,378| 18103.282| 46.612| 462,789|
| |Apache County|   139| 1933.590|  5.962| 3,193| 44416.932| 256.355|  71,887|
| |Coconino County|   117| 815.467|  1.991| 3,090| 21536.703| 99.569| 143,476|
| |Yavapai County|    67| 284.986|  3.646| 2,004|  8524.069| 113.022| 235,099|
| |Santa Cruz County|    53| 1139.834|  9.217| 2,662| 57249.774| 165.906|  46,498|
| |Cochise County|    52| 412.954|  3.403| 1,603| 12730.103| 76.011| 125,922|
| |Gila County|    38| 703.469| 23.802|   912| 16883.261| 208.925|  54,018|
| |Graham County|    16| 411.978| 25.749|   545| 14033.010| 205.989|  38,837|
| |La Paz County|    12| 568.505| 13.536|   476| 22550.692| 20.304|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263| 30.082|   9,498|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,145| 891.629| N/A|131,146| 28210.757| N/A|4,648,794|
| |Orleans Parish|   562| 1440.494|  0.732|10,735| 27515.481| 128.524| 390,144|
| |Jefferson Parish|   529| 1223.141|  3.633|15,279| 35327.739| 272.837| 432,493|
| |East Baton Rouge Parish|   347| 788.531|  6.493|12,187| 27694.014| 330.475| 440,059|
| |Caddo Parish|   295| 1228.123|  8.326| 6,668| 27759.738| 242.056| 240,204|
| |St. Tammany Parish|   214| 821.753|  6.034| 5,229| 20079.180| 257.826| 260,419|
| |Calcasieu Parish|   146| 717.670| 13.342| 6,815| 33499.479| 263.333| 203,436|
| |Rapides Parish|   114| 879.304| 11.019| 3,290| 25376.404| 278.777| 129,648|
| |Ouachita Parish|   113| 737.218|  7.456| 4,870| 31772.128| 369.075| 153,279|
| |Lafourche Parish|    99| 1014.199|  4.390| 2,800| 28684.410| 333.676|  97,614|
| |Lafayette Parish|    93| 380.539|  4.092| 7,628| 31212.406| 747.050| 244,390|
| |St. John the Baptist Parish|    92| 2147.676| 13.340| 1,424| 33242.291| 253.452|  42,837|
| |St. Landry Parish|    86| 1047.197| 20.874| 2,727| 33205.884| 946.304|  82,124|
| |Terrebonne Parish|    85| 769.502|  9.053| 3,035| 27475.761| 328.493| 110,461|
| |Acadia Parish|    83| 1337.739| 25.327| 2,598| 41872.834| 501.940|  62,045|
| |Bossier Parish|    81| 637.599|  8.996| 2,333| 18364.439| 249.642| 127,039|
| |Tangipahoa Parish|    75| 556.553| 12.721| 3,477| 25801.808| 360.434| 134,758|
| |Ascension Parish|    74| 584.500|  6.770| 2,871| 22677.009| 295.635| 126,604|
| |Iberia Parish|    72| 1031.075| 18.412| 2,532| 36259.487| 642.376|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,265| 27384.509| 222.663|  46,194|
| |St. Mary Parish|    54| 1094.269| 14.474| 1,597| 32362.000| 471.867|  49,348|
| |St. Charles Parish|    52| 979.284|  5.381| 1,474| 27758.945| 287.867|  53,100|
| |Livingston Parish|    51| 362.244|  2.029| 2,924| 20768.668| 267.878| 140,789|
| |Iberville Parish|    48| 1476.423|  4.394| 1,237| 38048.660| 435.018|  32,511|
| |St. Martin Parish|    45| 842.208|  8.021| 1,711| 32022.609| 561.472|  53,431|
| |West Baton Rouge Parish|    37| 1398.073|  5.398|   720| 27205.743| 350.868|  26,465|
| |East Feliciana Parish|    36| 1881.369|  7.466|   587| 30676.770| 515.137|  19,135|
| |Union Parish|    33| 1492.672|  0.000|   706| 31934.141| 562.175|  22,108|
| |St. James Parish|    32| 1516.875|  6.772|   716| 33940.083| 480.795|  21,096|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   791| 36401.289| 427.322|  21,730|
| |Avoyelles Parish|    32| 797.130| 17.793| 1,070| 26654.045| 466.179|  40,144|
| |Lincoln Parish|    31| 663.215| 21.394|   797| 17051.046| 247.560|  46,742|
| |Bienville Parish|    30| 2265.690|  0.000|   381| 28774.262| 302.092|  13,241|
| |Allen Parish|    29| 1131.619| 33.447| 1,276| 49791.236| 886.342|  25,627|
| |Jefferson Davis Parish|    28| 892.629| 18.217| 1,024| 32644.733| 318.796|  31,368|
| |Vernon Parish|    28| 590.356| 18.072|   768| 16192.625| 253.010|  47,429|
| |De Soto Parish|    26| 946.728| 10.404|   722| 26289.917| 348.521|  27,463|
| |Vermilion Parish|    24| 403.287| 16.804| 1,582| 26583.321| 616.933|  59,511|
| |St. Bernard Parish|    24| 508.001|  3.024| 1,103| 23346.880| 226.786|  47,244|
| |Assumption Parish|    20| 913.617|  6.526|   584| 26677.630| 208.827|  21,891|
| |Plaquemines Parish|    19| 819.071|  0.000|   458| 19743.932| 203.228|  23,197|
| |Grant Parish|    18| 803.966| 57.426|   306| 13667.426| 165.898|  22,389|
| |Jackson Parish|    18| 1143.293|  0.000|   376| 23882.114| 172.401|  15,744|
| |Beauregard Parish|    18| 480.038|  3.810|   833| 22215.111| 228.590|  37,497|
| |Franklin Parish|    17| 849.363|  0.000|   934| 46665.001| 770.850|  20,015|
| |Natchitoches Parish|    17| 445.516|  0.000|   773| 20257.875| 321.970|  38,158|
| |West Feliciana Parish|    16| 1027.749|  0.000|   347| 22289.311| 211.056|  15,568|
| |Webster Parish|    14| 365.154|  3.726|   893| 23291.601| 260.824|  38,340|
| |Red River Parish|    12| 1421.464| 16.922|   238| 28192.371| 829.187|   8,442|
| |Morehouse Parish|    11| 442.229|  0.000|   529| 21267.187| 505.404|  24,874|
| |Claiborne Parish|    11| 701.978|  0.000|   274| 17485.641| 474.063|  15,670|
| |Sabine Parish|    10| 418.690|  5.981|   645| 27005.527| 663.923|  23,884|
| |Concordia Parish|     9| 467.314|  7.418|   327| 16979.075| 363.466|  19,259|
| |Evangeline Parish|     7| 209.612| 21.389|   895| 26800.419| 748.615|  33,395|
| |Richland Parish|     7| 347.878|  7.100|   601| 29867.806| 447.272|  20,122|
| |Winn Parish|     7| 503.452|  0.000|   423| 30422.900| 380.158|  13,904|
| |Madison Parish|     6| 547.895|  0.000|   613| 55976.623| 639.211|  10,951|
| |West Carroll Parish|     6| 554.017| 13.191|   293| 27054.478| 461.681|  10,830|
| |Catahoula Parish|     5| 526.648| 15.047|   293| 30861.597| 556.743|   9,494|
| |St. Helena Parish|     2| 197.394| 14.100|   264| 26056.060| 253.793|  10,132|
| |LaSalle Parish|     2| 134.300|  0.000|   305| 20480.795| 661.909|  14,892|
| |Caldwell Parish|     2| 201.654|  0.000|   218| 21980.238| 302.480|   9,918|
| |East Carroll Parish|     1| 145.751|  0.000|   519| 75644.950| 374.789|   6,861|
| |Tensas Parish|     0|  0.000|  0.000|    88| 20304.569| 824.049|   4,334|
| |Cameron Parish|     0|  0.000|  0.000|   168| 24092.930| 20.487|   6,973|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,099| 386.064| N/A|197,384| 18590.575| N/A|10,617,423|
| |Fulton County|   430| 404.159|  4.297|20,276| 19057.519| 294.996|1,063,937|
| |Cobb County|   319| 419.659|  3.947|13,564| 17844.058| 352.190| 760,141|
| |Gwinnett County|   260| 277.704|  3.052|19,808| 21156.742| 309.289| 936,250|
| |DeKalb County|   237| 312.131|  2.258|13,923| 18336.698| 272.244| 759,297|
| |Dougherty County|   170| 1932.785|  3.248| 2,694| 30628.951| 149.425|  87,956|
| |Clayton County|   110| 376.382|  4.399| 5,006| 17128.819| 238.538| 292,256|
| |Muscogee County|    96| 490.374| 10.216| 4,748| 24253.074| 321.808| 195,769|
| |Hall County|    91| 445.116|  8.385| 6,080| 29739.631| 389.215| 204,441|
| |Richmond County|    90| 444.405|  4.938| 4,355| 21504.261| 448.637| 202,518|
| |Chatham County|    75| 259.130|  3.949| 5,703| 19704.246| 366.731| 289,430|
| |Troup County|    69| 986.814| 12.259| 2,290| 32750.779| 247.214|  69,922|
| |Bibb County|    68| 443.983|  6.529| 3,616| 23609.452| 434.656| 153,159|
| |Cherokee County|    63| 243.457|  3.864| 3,462| 13378.521| 336.202| 258,773|
| |Bartow County|    62| 575.470|  2.652| 1,868| 17338.358| 346.078| 107,738|
| |Houston County|    59| 373.742|  9.049| 1,976| 12517.183| 172.844| 157,863|
| |Sumter County|    56| 1896.762|  0.000|   762| 25809.511| 159.676|  29,524|
| |Douglas County|    51| 348.496|  1.952| 2,635| 18005.644| 310.425| 146,343|
| |Habersham County|    49| 1081.010|  3.152| 1,141| 25172.079| 327.770|  45,328|
| |Carroll County|    49| 408.361|  2.381| 1,881| 15676.045| 171.440| 119,992|
| |Henry County|    47| 200.374|  3.045| 3,364| 14341.685| 229.608| 234,561|
| |Glynn County|    47| 551.048| 21.774| 2,533| 29697.979| 371.832|  85,292|
| |Upson County|    46| 1747.720|  0.000|   535| 20326.748| 276.813|  26,320|
| |Lowndes County|    44| 374.768| 14.601| 3,178| 27068.463| 251.873| 117,406|
| |Thomas County|    42| 944.861|  9.641| 1,123| 25263.774| 404.940|  44,451|
| |Mitchell County|    41| 1875.314|  0.000|   650| 29730.595| 202.560|  21,863|
| |Spalding County|    41| 614.665|  4.283|   937| 14047.344| 162.768|  66,703|
| |Newton County|    40| 357.961|  6.392| 1,787| 15991.910| 244.181| 111,744|
| |Baldwin County|    39| 868.790|  3.182| 1,048| 23345.957| 264.138|  44,890|
| |Walton County|    39| 412.293|  7.551| 1,113| 11766.198| 238.616|  94,593|
| |Butts County|    37| 1483.799|  0.000|   490| 19650.305| 143.224|  24,936|
| |Tift County|    36| 885.740|  3.515| 1,333| 32796.969| 305.791|  40,644|
| |Hancock County|    35| 4138.583| 16.892|   318| 37601.987| 608.118|   8,457|
| |Barrow County|    32| 384.431|  0.000| 1,289| 15485.344| 303.769|  83,240|
| |Early County|    32| 3140.334| 14.019|   360| 35328.754| 196.271|  10,190|
| |Whitfield County|    30| 286.730|  4.096| 3,527| 33709.906| 441.018| 104,628|
| |Terrell County|    30| 3516.587|  0.000|   302| 35400.305| 167.457|   8,531|
| |Ware County|    29| 811.552| 23.987| 1,144| 32014.328| 267.852|  35,734|
| |Coffee County|    28| 647.055|  9.904| 1,462| 33785.501| 399.457|  43,273|
| |Fayette County|    28| 244.710|  3.746| 1,120|  9788.413| 187.278| 114,421|
| |Monroe County|    26| 942.780| 15.540|   461| 16716.223| 196.844|  27,578|
| |Randolph County|    26| 3835.940|  0.000|   271| 39982.296| 252.919|   6,778|
| |Jenkins County|    24| 2766.252| 32.932|   244| 28123.559| 230.521|   8,676|
| |Worth County|    23| 1135.971|  0.000|   447| 22077.345| 162.282|  20,247|
| |Colquitt County|    23| 504.386|  3.133| 1,546| 33903.509| 203.634|  45,600|
| |Columbia County|    23| 146.764|  3.646| 2,241| 14299.935| 293.528| 156,714|
| |Gordon County|    23| 396.805|  0.000| 1,183| 20409.572| 416.522|  57,963|
| |Paulding County|    22| 130.435|  2.541| 1,678|  9948.597| 210.050| 168,667|
| |Forsyth County|    22| 90.071|  1.170| 2,270|  9293.680| 201.197| 244,252|
| |Coweta County|    22| 148.139|  0.962| 1,503| 10120.599| 158.721| 148,509|
| |Lee County|    22| 733.529|  0.000|   539| 17971.459| 114.316|  29,992|
| |Appling County|    19| 1033.395| 23.310|   671| 36495.159| 598.281|  18,386|
| |Wilcox County|    19| 2200.347| 16.544|   181| 20961.204| 248.159|   8,635|
| |Putnam County|    18| 813.780|  6.459|   428| 19349.880| 303.553|  22,119|
| |Clarke County|    18| 140.262|  1.113| 2,047| 15950.939| 367.354| 128,331|
| |Turner County|    18| 2254.227|  0.000|   246| 30807.765| 375.704|   7,985|
| |Brooks County|    18| 1164.521| 27.727|   412| 26654.590| 378.931|  15,457|
| |Walker County|    17| 243.689|  2.048|   705| 10105.933| 311.267|  69,761|
| |Floyd County|    17| 172.592|  2.901| 1,504| 15269.346| 345.185|  98,498|
| |Harris County|    17| 482.461|  4.054|   656| 18617.323| 145.955|  35,236|
| |Rockdale County|    17| 187.027|  1.572| 1,318| 14500.088| 234.177|  90,896|
| |Jackson County|    16| 219.247|  5.873| 1,063| 14566.233| 221.205|  72,977|
| |Oconee County|    15| 372.393|  0.000|   437| 10849.057| 152.504|  40,280|
| |Peach County|    14| 508.241| 10.372|   385| 13976.621| 305.982|  27,546|
| |Crisp County|    14| 625.782|  0.000|   374| 16717.325| 70.241|  22,372|
| |Dooly County|    14| 1045.556|  0.000|   252| 18820.015| 106.689|  13,390|
| |Bulloch County|    14| 175.862|  3.589| 1,262| 15852.678| 288.916|  79,608|
| |Stephens County|    12| 462.874| 11.021|   621| 23953.713| 358.176|  25,925|
| |Lamar County|    12| 629.030| 22.465|   274| 14362.845| 381.911|  19,077|
| |Greene County|    12| 654.879|  7.796|   308| 16808.557| 467.771|  18,324|
| |Decatur County|    11| 416.604| 16.231|   793| 30033.328| 687.125|  26,404|
| |Wilkinson County|    11| 1228.501| 15.955|   215| 24011.615| 526.501|   8,954|
| |Johnson County|    11| 1140.724| 14.815|   241| 24992.222| 207.404|   9,643|
| |Polk County|    11| 258.137|  6.705|   802| 18820.548| 425.759|  42,613|
| |McDuffie County|    10| 469.219|  6.703|   352| 16516.517| 395.485|  21,312|
| |Macon County|    10| 772.380|  0.000|   177| 13671.121| 22.068|  12,947|
| |Bleckley County|     9| 699.138| 66.585|   227| 17633.807| 1054.255|  12,873|
| |Emanuel County|     9| 397.421| 12.617|   511| 22564.691| 536.203|  22,646|
| |Catoosa County|     9| 133.175|  0.000|   637|  9425.866| 205.048|  67,580|
| |Telfair County|     9| 567.465| 18.015|   278| 17528.373| 225.185|  15,860|
| |Screven County|     9| 644.422|  0.000|   198| 14177.288| 255.723|  13,966|
| |Pierce County|     8| 410.994| 14.678|   400| 20549.705| 161.462|  19,465|
| |Wayne County|     8| 267.317| 19.094|   773| 25829.518| 720.802|  29,927|
| |Laurens County|     8| 168.258| 12.018|   910| 19139.360| 483.742|  47,546|
| |Bryan County|     8| 201.883|  3.605|   657| 16579.605| 382.135|  39,627|
| |Toombs County|     8| 298.174| 10.649|   755| 28140.142| 654.917|  26,830|
| |Bacon County|     8| 716.589| 25.592|   437| 39143.676| 281.517|  11,164|
| |Jeff Davis County|     8| 529.276| 18.903|   451| 29837.909| 538.727|  15,115|
| |Stewart County|     7| 1057.242| 43.153|   255| 38513.820| 151.035|   6,621|
| |Union County|     7| 285.586|  5.828|   263| 10729.876| 262.273|  24,511|
| |Oglethorpe County|     7| 458.746|  0.000|   214| 14024.510| 252.778|  15,259|
| |Jefferson County|     7| 455.670|  9.299|   497| 32352.558| 585.861|  15,362|
| |Hart County|     7| 267.125| 27.258|   305| 11639.000| 212.609|  26,205|
| |Burke County|     7| 312.737|  0.000|   467| 20864.049| 376.561|  22,383|
| |Calhoun County|     6| 969.462|  0.000|   203| 32800.129| 207.742|   6,189|
| |Madison County|     6| 200.803|  9.562|   394| 13186.078| 282.081|  29,880|
| |Franklin County|     6| 256.970| 12.237|   401| 17174.183| 220.260|  23,349|
| |Meriwether County|     6| 283.460|  6.749|   390| 18424.907| 236.217|  21,167|
| |Haralson County|     6| 201.396|  0.000|   213|  7149.570| 100.698|  29,792|
| |Lumpkin County|     6| 178.518|  0.000|   342| 10175.543| 174.268|  33,610|
| |Cook County|     6| 347.423|  0.000|   438| 25361.899| 297.791|  17,270|
| |Pickens County|     5| 153.417|  0.000|   380| 11659.661| 394.500|  32,591|
| |White County|     5| 162.348|  0.000|   353| 11461.783| 241.203|  30,798|
| |Camden County|     5| 91.465|  2.613|   737| 13481.872| 175.089|  54,666|
| |Marion County|     5| 598.158| 17.090|   150| 17944.730| 119.632|   8,359|
| |Brantley County|     5| 261.657|  7.476|   249| 13030.509| 186.898|  19,109|
| |Grady County|     5| 202.980|  0.000|   480| 19486.055| 423.358|  24,633|
| |Candler County|     4| 370.268|  0.000|   254| 23511.987| 330.596|  10,803|
| |Wilkes County|     4| 409.123| 14.612|   193| 19740.207| 233.785|   9,777|
| |Ben Hill County|     4| 239.521|  8.554|   436| 26107.784| 769.889|  16,700|
| |Seminole County|     4| 494.438| 35.317|   196| 24227.441| 900.583|   8,090|
| |Banks County|     4| 207.965|  7.427|   271| 14089.633| 215.392|  19,234|
| |Clinch County|     4| 604.412|  0.000|   196| 29616.198| 474.895|   6,618|
| |Pike County|     4| 210.948|  0.000|   215| 11338.466| 173.279|  18,962|
| |Heard County|     4| 335.486| 11.982|   143| 11993.626| 155.761|  11,923|
| |Lanier County|     4| 383.767|  0.000|   219| 21011.225| 54.824|  10,423|
| |Lincoln County|     4| 504.987|  0.000|   141| 17800.783| 216.423|   7,921|
| |Gilmer County|     4| 127.514|  4.554|   620| 19764.736| 491.841|  31,369|
| |Dodge County|     3| 145.596|  0.000|   221| 10725.552| 221.860|  20,605|
| |Fannin County|     3| 114.556|  5.455|   334| 12753.933| 289.118|  26,188|
| |Liberty County|     3| 48.832|  2.325|   720| 11719.704| 267.414|  61,435|
| |Jones County|     3| 104.402|  0.000|   306| 10649.034| 223.719|  28,735|
| |Dawson County|     3| 114.907|  0.000|   377| 14440.018| 432.270|  26,108|
| |Rabun County|     3| 175.060|  0.000|   215| 12545.953| 200.068|  17,137|
| |Talbot County|     3| 484.262|  0.000|   138| 22276.029| 276.721|   6,195|
| |Baker County|     3| 987.492|  0.000|    63| 20737.327| 235.117|   3,038|
| |Charlton County|     3| 224.014|  0.000|   425| 31735.364| 480.031|  13,392|
| |Chattooga County|     3| 121.021|  5.763|   266| 10730.566| 391.879|  24,789|
| |Twiggs County|     3| 369.458|  0.000|   118| 14532.020| 439.831|   8,120|
| |Treutlen County|     3| 434.720|  0.000|   124| 17968.410| 517.523|   6,901|
| |Washington County|     2| 98.164|  0.000|   475| 23314.028| 378.634|  20,374|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724| 164.393|   2,607|
| |Taylor County|     2| 249.377|  0.000|    87| 10847.880| 302.814|   8,020|
| |Murray County|     2| 49.880|  0.000|   604| 15063.847| 245.839|  40,096|
| |Pulaski County|     2| 179.582|  0.000|   115| 10325.941| 371.990|  11,137|
| |Effingham County|     2| 31.106|  2.222|   727| 11307.080| 213.299|  64,296|
| |Montgomery County|     2| 218.055| 15.575|   153| 16681.204| 373.808|   9,172|
| |Echols County|     2| 499.251|  0.000|   222| 55416.875| 142.643|   4,006|
| |Clay County|     2| 705.716|  0.000|    86| 30345.801| 302.450|   2,834|
| |Chattahoochee County|     2| 183.368| 13.098|   761| 69771.706| 1322.873|  10,907|
| |Atkinson County|     2| 244.948|  0.000|   319| 39069.198| 454.903|   8,165|
| |McIntosh County|     2| 139.101|  0.000|   184| 12797.329| 337.818|  14,378|
| |Wheeler County|     1| 127.307|  0.000|    91| 11584.978| 145.494|   7,855|
| |Schley County|     1| 190.223|  0.000|    66| 12554.689| 407.620|   5,257|
| |Tattnall County|     1| 39.548|  0.000|   502| 19852.883| 485.870|  25,286|
| |Warren County|     1| 190.331| 27.190|    77| 14655.501| 598.184|   5,254|
| |Towns County|     1| 83.077|  0.000|   143| 11880.037| 332.309|  12,037|
| |Quitman County|     1| 434.972|  0.000|    29| 12614.180|  0.000|   2,299|
| |Irwin County|     1| 106.202|  0.000|   167| 17735.769| 166.889|   9,416|
| |Jasper County|     1| 70.328|  0.000|   162| 11393.206| 381.783|  14,219|
| |Long County|     1| 51.127|  0.000|   126|  6442.047| 21.912|  19,559|
| |Evans County|     1| 93.861|  0.000|   250| 23465.365| 402.263|  10,654|
| |Elbert County|     1| 52.100|  0.000|   358| 18651.662| 260.498|  19,194|
| |Dade County|     1| 62.050|  0.000|   126|  7818.317| 141.829|  16,116|
| |Taliaferro County|     0|  0.000|  0.000|    13|  8458.035|  0.000|   1,537|
| |Crawford County|     0|  0.000|  0.000|   102|  8223.154| 149.721|  12,404|
| |Berrien County|     0|  0.000|  0.000|   295| 15208.537| 250.407|  19,397|
| |Morgan County|     0|  0.000|  0.000|   274| 14214.567| 407.613|  19,276|
| |Miller County|     0|  0.000|  0.000|   143| 25008.744| 324.789|   5,718|
| |Glascock County|     0|  0.000|  0.000|    24|  8078.088| 96.168|   2,971|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,669| 313.882| N/A|100,848|  8627.525| N/A|11,689,100|
| |Franklin County|   524| 397.948|  1.085|18,317| 13910.702| 131.275|1,316,756|
| |Cuyahoga County|   499| 404.025|  2.545|13,514| 10941.872| 100.399|1,235,072|
| |Lucas County|   323| 754.060|  1.668| 5,348| 12485.176| 165.420| 428,348|
| |Hamilton County|   255| 311.937|  1.398| 9,643| 11796.108| 93.144| 817,473|
| |Mahoning County|   255| 1115.081|  1.249| 2,554| 11168.298| 100.576| 228,683|
| |Summit County|   222| 410.341|  1.320| 3,555|  6571.007| 81.065| 541,013|
| |Stark County|   139| 375.061|  2.698| 1,827|  4929.764| 57.049| 370,606|
| |Trumbull County|   106| 535.424|  2.165| 1,524|  7697.981| 74.324| 197,974|
| |Montgomery County|    94| 176.796|  4.568| 4,362|  8204.075| 90.816| 531,687|
| |Lorain County|    78| 251.749|  0.922| 1,770|  5712.755| 69.162| 309,833|
| |Butler County|    63| 164.433|  1.491| 2,929|  7644.845| 91.725| 383,134|
| |Portage County|    61| 375.463|  0.879|   758|  4665.592| 41.327| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,658| 16273.569| 123.391| 101,883|
| |Wood County|    58| 443.367|  0.000| 1,043|  7972.970| 145.241| 130,817|
| |Wayne County|    58| 501.253|  0.000|   539|  4658.197| 58.027| 115,710|
| |Licking County|    49| 277.052|  5.654| 1,281|  7242.935| 133.276| 176,862|
| |Ashtabula County|    46| 473.051|  1.469|   569|  5851.441| 45.542|  97,241|
| |Marion County|    45| 691.319|  2.195| 2,925| 44935.707| 109.733|  65,093|
| |Allen County|    44| 429.893|  2.792|   740|  7230.022| 131.201| 102,351|
| |Geauga County|    44| 469.840|  1.525|   556|  5937.063| 42.713|  93,649|
| |Pickaway County|    42| 718.477|  0.000| 2,387| 40833.433| 85.533|  58,457|
| |Warren County|    39| 166.239|  2.436| 1,789|  7625.681| 115.089| 234,602|
| |Miami County|    38| 355.183|  1.335|   839|  7842.074| 94.805| 106,987|
| |Lake County|    38| 165.110|  1.862| 1,114|  4840.343| 49.657| 230,149|
| |Medina County|    35| 194.719|  1.590|   923|  5135.024| 73.119| 179,746|
| |Fairfield County|    32| 203.079|  6.346| 1,387|  8802.214| 135.084| 157,574|
| |Darke County|    29| 567.370|  5.590|   395|  7727.975| 220.799|  51,113|
| |Erie County|    27| 363.558|  0.000|   575|  7742.439| 113.492|  74,266|
| |Belmont County|    26| 388.025|  0.000|   621|  9267.827| 68.224|  67,006|
| |Ottawa County|    26| 641.579|  3.525|   386|  9524.985| 119.855|  40,525|
| |Washington County|    22| 367.211|  0.000|   203|  3388.359| 14.307|  59,911|
| |Delaware County|    19| 90.832|  0.683| 1,301|  6219.613| 73.076| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    93|  6811.191| 31.388|  13,654|
| |Putnam County|    17| 502.053|  0.000|   205|  6054.163| 50.627|  33,861|
| |Sandusky County|    16| 273.420|  0.000|   377|  6442.462| 117.180|  58,518|
| |Tuscarawas County|    14| 152.195|  1.553|   782|  8501.201| 55.909|  91,987|
| |Clark County|    14| 104.413|  1.065| 1,146|  8546.945| 74.581| 134,083|
| |Mercer County|    13| 315.749|  0.000|   612| 14864.471| 312.279|  41,172|
| |Richland County|    12| 99.047|  2.358|   604|  4985.390| 80.181| 121,154|
| |Hardin County|    12| 382.592|  0.000|   165|  5260.641| 68.320|  31,365|
| |Greene County|    12| 71.032|  0.846|   690|  4084.363| 60.039| 168,937|
| |Clermont County|    11| 53.287|  0.692|   933|  4519.736| 67.820| 206,428|
| |Madison County|    10| 223.559|  0.000|   374|  8361.092| 143.716|  44,731|
| |Hocking County|     9| 318.426|  0.000|   118|  4174.922| 50.544|  28,264|
| |Wyandot County|     8| 367.444| 19.685|   146|  6705.861| 177.161|  21,772|
| |Guernsey County|     7| 180.064|  3.675|   117|  3009.646| 25.723|  38,875|
| |Knox County|     7| 112.320| 11.461|   205|  3289.368| 91.690|  62,322|
| |Holmes County|     6| 136.488|  0.000|   328|  7461.328| 25.998|  43,960|
| |Auglaize County|     6| 131.418|  3.129|   254|  5563.343| 128.289|  45,656|
| |Clinton County|     6| 142.966|  0.000|   164|  3907.739| 61.271|  41,968|
| |Coshocton County|     6| 163.934|  0.000|   193|  5273.224| 31.226|  36,600|
| |Carroll County|     5| 185.777|  0.000|   111|  4124.248| 21.232|  26,914|
| |Crawford County|     5| 120.499|  0.000|   174|  4193.377| 34.428|  41,494|
| |Huron County|     5| 85.813|  2.452|   396|  6796.416| 61.295|  58,266|
| |Ross County|     4| 52.174|  0.000|   484|  6313.098| 180.747|  76,666|
| |Shelby County|     4| 82.321|  0.000|   194|  3992.591| 108.782|  48,590|
| |Defiance County|     4| 105.023|  0.000|   144|  3780.818| 56.262|  38,087|
| |Williams County|     3| 81.762|  0.000|   135|  3679.276| 46.721|  36,692|
| |Perry County|     3| 83.024|  3.954|   130|  3597.720| 98.838|  36,134|
| |Hancock County|     3| 39.587|  1.885|   378|  4987.926| 118.760|  75,783|
| |Seneca County|     3| 54.369|  0.000|   214|  3878.357| 157.930|  55,178|
| |Ashland County|     3| 56.092|  0.000|   144|  2692.394| 37.394|  53,484|
| |Adams County|     2| 72.207|  0.000|    61|  2202.325| 41.261|  27,698|
| |Brown County|     2| 46.049|  3.289|   129|  2970.160| 55.917|  43,432|
| |Champaign County|     2| 51.434|  3.674|   176|  4526.167| 260.842|  38,885|
| |Henry County|     2| 74.058|  5.290|   117|  4332.371| 58.188|  27,006|
| |Logan County|     2| 43.791|  3.128|   155|  3393.764| 109.476|  45,672|
| |Jefferson County|     2| 30.616|  0.000|   229|  3505.549| 54.672|  65,325|
| |Preble County|     2| 48.921|  0.000|   203|  4965.510| 136.281|  40,882|
| |Morrow County|     2| 56.612|  0.000|   170|  4812.047| 48.525|  35,328|
| |Vinton County|     2| 152.847|  0.000|    31|  2369.125| 10.918|  13,085|
| |Athens County|     1| 15.308|  0.000|   357|  5464.815| 28.428|  65,327|
| |Gallia County|     1| 33.447|  0.000|    65|  2174.058| 38.225|  29,898|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723| 66.489|  15,040|
| |Highland County|     1| 23.169|  0.000|   158|  3660.712| 102.606|  43,161|
| |Fulton County|     1| 23.738|  0.000|   148|  3513.270| 30.521|  42,126|
| |Van Wert County|     1| 35.367|  0.000|    71|  2511.052| 15.157|  28,275|
| |Union County|     1| 16.953|  0.000|   251|  4255.103| 89.607|  58,988|
| |Scioto County|     1| 13.278|  0.000|   226|  3000.770| 77.770|  75,314|
| |Muskingum County|     1| 11.599|  0.000|   236|  2737.343| 96.105|  86,215|
| |Pike County|     0|  0.000|  0.000|    76|  2736.569| 51.439|  27,772|
| |Meigs County|     0|  0.000|  0.000|    40|  1746.191| 99.782|  22,907|
| |Morgan County|     0|  0.000|  0.000|    26|  1792.115| 59.081|  14,508|
| |Noble County|     0|  0.000|  0.000|    16|  1109.262|  0.000|  14,424|
| |Paulding County|     0|  0.000|  0.000|    69|  3695.373| 76.509|  18,672|
| |Fayette County|     0|  0.000|  0.000|   113|  3961.437| 95.155|  28,525|
| |Jackson County|     0|  0.000|  0.000|    74|  2283.035| 39.667|  32,413|
| |Lawrence County|     0|  0.000|  0.000|   283|  4759.262| 160.964|  59,463|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,567| 590.008| N/A|95,503| 15796.900| N/A|6,045,680|
| |Baltimore County|   991| 1197.771|  4.662|25,804| 31187.981| 354.307| 827,370|
| |Montgomery County|   803| 764.261|  1.632|18,392| 17504.721| 86.202|1,050,688|
| |Prince George's County|   753| 828.085|  1.571|23,697| 26059.932| 149.875| 909,327|
| |Anne Arundel County|   225| 388.444|  1.973| 7,361| 12708.163| 99.392| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,067| 11816.742| 37.978| 259,547|
| |Carroll County|   117| 694.580|  0.848| 1,546|  9177.961| 55.125| 168,447|
| |Howard County|   110| 337.744|  1.755| 3,846| 11808.775| 98.253| 325,690|
| |Charles County|    91| 557.403|  0.000| 2,024| 12397.631| 127.756| 163,257|
| |Harford County|    69| 270.121|  0.559| 1,968|  7704.323| 83.889| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   983|  8660.030| 76.771| 113,510|
| |Wicomico County|    45| 434.325|  1.379| 1,338| 12913.936| 60.668| 103,609|
| |Washington County|    31| 205.231|  0.946| 1,012|  6699.813| 32.156| 151,049|
| |Cecil County|    30| 291.673|  0.000|   702|  6825.142| 76.390| 102,855|
| |Calvert County|    28| 302.621|  0.000|   697|  7533.099| 120.431|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   431|  8554.812| 96.408|  50,381|
| |Kent County|    23| 1184.224|  0.000|   243| 12511.585| 58.843|  19,422|
| |Worcester County|    20| 382.585|  2.733|   694| 13275.691| 289.671|  52,276|
| |Allegany County|    18| 255.624|  0.000|   291|  4132.584| 40.575|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   371| 11619.531| 89.484|  31,929|
| |Talbot County|     4| 107.582|  0.000|   400| 10758.183| 130.635|  37,181|
| |Caroline County|     3| 89.804|  0.000|   451| 13500.569| 81.251|  33,406|
| |Somerset County|     3| 117.114|  0.000|   136|  5309.182| 72.499|  25,616|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    49|  1688.840| 29.542|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,835| 421.109| N/A|74,328| 11040.639| N/A|6,732,219|
| |Marion County|   725| 751.621|  0.889|15,860| 16442.355| 170.318| 964,582|
| |Lake County|   275| 566.435|  1.766| 7,570| 15592.398| 156.836| 485,493|
| |Allen County|   163| 429.740|  2.260| 3,902| 10287.399| 109.601| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,757| 11108.512| 98.449| 158,167|
| |Hendricks County|   108| 634.134|  2.516| 1,887| 11079.731| 121.626| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,763|  8174.290| 115.804| 338,011|
| |Elkhart County|    84| 407.093|  5.539| 4,843| 23470.856| 180.699| 206,341|
| |St. Joseph County|    81| 297.985|  1.051| 3,500| 12875.884| 202.861| 271,826|
| |Howard County|    65| 787.459|  1.731|   890| 10782.128| 148.838|  82,544|
| |Madison County|    65| 501.663|  0.000|   979|  7555.820| 151.050| 129,569|
| |Delaware County|    52| 455.601|  0.000|   730|  6395.935| 121.410| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   793|  9465.379| 93.784|  83,779|
| |Clark County|    47| 397.288|  2.415| 1,233| 10422.478| 190.795| 118,302|
| |Boone County|    46| 678.036|  0.000|   678|  9993.662| 96.862|  67,843|
| |Floyd County|    46| 585.823|  3.639|   779|  9920.787| 172.836|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,316|  7723.503| 119.055| 170,389|
| |Hancock County|    38| 486.132|  1.828|   660|  8443.353| 80.413|  78,168|
| |Greene County|    34| 1065.096|  0.000|   250|  7831.589| 53.702|  31,922|
| |Morgan County|    34| 482.345|  4.053|   476|  6752.827| 117.546|  70,489|
| |Decatur County|    32| 1204.865|  0.000|   337| 12688.731| 129.093|  26,559|
| |Monroe County|    30| 202.114|  0.000|   756|  5093.276| 69.296| 148,431|
| |Warrick County|    30| 476.206|  0.000|   581|  9222.515| 179.144|  62,998|
| |Grant County|    30| 456.142|  2.172|   526|  7997.689| 65.163|  65,769|
| |LaPorte County|    30| 273.005|  1.300|   911|  8290.259| 106.602| 109,888|
| |Noble County|    29| 607.406|  2.992|   678| 14200.737| 128.662|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   508| 10271.341| 135.757|  49,458|
| |Lawrence County|    27| 595.107|  0.000|   346|  7626.185| 62.974|  45,370|
| |Shelby County|    27| 603.635|  3.194|   553| 12363.344| 140.529|  44,729|
| |Orange County|    24| 1221.623|  0.000|   171|  8704.062| 58.173|  19,646|
| |Harrison County|    23| 567.691|  3.526|   338|  8342.589| 172.776|  40,515|
| |Marshall County|    22| 475.593|  0.000|   784| 16948.420| 129.707|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   354|  9233.659| 59.620|  38,338|
| |Daviess County|    20| 599.682|  4.283|   273|  8185.662| 128.503|  33,351|
| |Henry County|    20| 416.910|  5.956|   383|  7983.824| 65.514|  47,972|
| |Franklin County|    14| 615.168| 25.109|   242| 10633.623| 232.257|  22,758|
| |Vanderburgh County|    13| 71.645|  0.787| 1,963| 10818.348| 207.061| 181,451|
| |Perry County|    12| 626.011|  0.000|   186|  9703.167| 111.788|  19,169|
| |Kosciusko County|    12| 151.027|  0.000|   852| 10722.916| 64.726|  79,456|
| |Jennings County|    12| 432.666|  0.000|   225|  8112.493| 92.714|  27,735|
| |Dubois County|    12| 280.794|  0.000|   696| 16286.035| 240.680|  42,736|
| |Tippecanoe County|    11| 56.199|  0.000| 1,211|  6187.031| 85.394| 195,732|
| |LaGrange County|    10| 252.436|  0.000|   559| 14111.173| 61.306|  39,614|
| |Tipton County|    10| 660.153| 47.154|   138|  9110.114| 301.784|  15,148|
| |Vigo County|    10| 93.425|  0.000|   651|  6081.952| 244.239| 107,038|
| |Scott County|    10| 418.883|  0.000|   268| 11226.071| 125.665|  23,873|
| |Wayne County|    10| 151.782|  2.168|   377|  5722.178| 134.435|  65,884|
| |White County|    10| 414.903|  0.000|   369| 15309.933| 142.253|  24,102|
| |Newton County|    10| 715.103|  0.000|   118|  8438.215| 91.942|  13,984|
| |Cass County|     9| 238.796|  0.000| 1,795| 47626.628| 170.569|  37,689|
| |Putnam County|     8| 212.902|  0.000|   288|  7664.467| 254.722|  37,576|
| |Fayette County|     7| 303.004|  0.000|   189|  8181.110| 216.431|  23,102|
| |Ripley County|     7| 247.140|  0.000|   208|  7343.596| 100.874|  28,324|
| |Starke County|     7| 304.414|  0.000|   178|  7740.813| 86.975|  22,995|
| |Whitley County|     6| 176.658|  0.000|   152|  4475.327| 16.825|  33,964|
| |Ohio County|     5| 851.064| 24.316|    65| 11063.830| 364.742|   5,875|
| |Jackson County|     5| 113.043|  3.230|   586| 13248.627| 113.043|  44,231|
| |Clay County|     5| 190.658|  0.000|   121|  4613.918| 130.737|  26,225|
| |Randolph County|     4| 162.173|  0.000|   122|  4946.280| 115.838|  24,665|
| |Gibson County|     4| 118.839|  0.000|   225|  6684.691| 114.595|  33,659|
| |Rush County|     4| 241.240|  0.000|    80|  4824.799|  8.616|  16,581|
| |DeKalb County|     4| 92.007|  0.000|   232|  5336.400| 36.146|  43,475|
| |Clinton County|     3| 92.595|  0.000|   434| 13395.475| 361.563|  32,399|
| |Huntington County|     3| 82.147|  0.000|   122|  3340.635| 15.647|  36,520|
| |Wabash County|     3| 96.787|  0.000|   169|  5452.316| 50.698|  30,996|
| |Steuben County|     3| 86.720|  0.000|   210|  6070.417| 45.425|  34,594|
| |Spencer County|     3| 147.951|  0.000|   136|  6707.107| 162.041|  20,277|
| |Blackford County|     2| 170.097|  0.000|    64|  5443.103| 133.648|  11,758|
| |Carroll County|     2| 98.731|  0.000|   191|  9428.839| 345.560|  20,257|
| |Miami County|     2| 56.313|  0.000|   274|  7714.833| 64.357|  35,516|
| |Jefferson County|     2| 61.904|  0.000|   163|  5045.190| 61.904|  32,308|
| |Fountain County|     2| 122.354|  0.000|    74|  4527.101| 96.135|  16,346|
| |Jasper County|     2| 59.591|  0.000|   243|  7240.331| 170.261|  33,562|
| |Fulton County|     2| 100.130|  0.000|   168|  8410.934| 171.652|  19,974|
| |Wells County|     2| 70.681|  0.000|   168|  5937.235| 186.801|  28,296|
| |Adams County|     2| 55.902|  0.000|   101|  2823.043| 79.860|  35,777|
| |Warren County|     1| 120.992|  0.000|    22|  2661.827| 51.854|   8,265|
| |Washington County|     1| 35.668|  0.000|   140|  4993.580| 127.387|  28,036|
| |Sullivan County|     1| 48.382|  0.000|   126|  6096.086| 352.495|  20,669|
| |Owen County|     1| 48.079|  0.000|    90|  4327.131| 82.422|  20,799|
| |Pulaski County|     1| 80.952|  0.000|    83|  6719.016| 138.775|  12,353|
| |Parke County|     1| 59.042|  0.000|    51|  3011.159| 50.608|  16,937|
| |Brown County|     1| 66.260|  0.000|    73|  4837.000| 28.397|  15,092|
| |Jay County|     0|  0.000|  0.000|    91|  4452.926| 62.914|  20,436|
| |Crawford County|     0|  0.000|  0.000|    45|  4254.515| 40.519|  10,577|
| |Switzerland County|     0|  0.000|  0.000|    52|  4836.759| 119.590|  10,751|
| |Vermillion County|     0|  0.000|  0.000|    52|  3355.272| 129.049|  15,498|
| |Union County|     0|  0.000|  0.000|    41|  5812.305| 182.267|   7,054|
| |Benton County|     0|  0.000|  0.000|    61|  6973.022| 16.330|   8,748|
| |Posey County|     0|  0.000|  0.000|   171|  6725.135| 78.657|  25,427|
| |Pike County|     0|  0.000|  0.000|    53|  4277.989| 92.248|  12,389|
| |Martin County|     0|  0.000|  0.000|    45|  4388.103| 41.791|  10,255|
| |Knox County|     0|  0.000|  0.000|   154|  4208.340| 97.596|  36,594|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,326| 272.508| N/A|100,086| 11725.825| N/A|8,535,519|
| |Fairfax County|   536| 467.089|  0.747|16,464| 14347.312| 76.562|1,147,532|
| |Henrico County|   185| 559.220|  1.295| 3,871| 11701.298| 113.139| 330,818|
| |Prince William County|   176| 374.201|  1.215| 9,488| 20172.856| 176.470| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,077| 12991.784| 91.683| 236,842|
| |Loudoun County|   115| 278.088|  1.036| 5,280| 12767.871| 84.981| 413,538|
| |Chesterfield County|    80| 226.756|  2.025| 4,362| 12363.875| 138.483| 352,802|
| |Alexandria city|    60| 376.345|  0.896| 2,964| 18591.464| 129.033| 159,428|
| |Virginia Beach city|    54| 120.007|  2.222| 4,973| 11051.750| 213.981| 449,974|
| |Suffolk city|    50| 542.841|  1.551| 1,282| 13918.444| 294.685|  92,108|
| |Richmond County|    45| 4987.255| 31.665| 3,482| 385902.693| 3467.330|   9,023|
| |Shenandoah County|    44| 1008.804|  6.551|   717| 16438.921| 121.188|  43,616|
| |Chesapeake city|    37| 151.122|  4.668| 2,912| 11893.724| 218.223| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,486| 10909.224| 161.509| 136,215|
| |Hanover County|    32| 296.940|  1.326|   644|  5975.911| 71.584| 107,766|
| |Mecklenburg County|    32| 1046.196|  0.000|   444| 14515.971| 635.190|  30,587|
| |Harrisonburg city|    31| 584.729|  5.389| 1,077| 20314.622| 78.144|  53,016|
| |Norfolk city|    31| 127.708|  2.943| 3,703| 15254.880| 290.138| 242,742|
| |Northampton County|    29| 2476.516| 12.200|   296| 25277.541| 48.798|  11,710|
| |Page County|    25| 1045.938|  5.977|   345| 14433.939| 77.698|  23,902|
| |Portsmouth city|    25| 264.836|  1.513| 1,759| 18633.869| 332.937|  94,398|
| |Galax city|    24| 3781.314| 45.016|   347| 54671.498| 360.125|   6,347|
| |Manassas city|    22| 535.475|  6.954| 1,653| 40233.662| 152.993|  41,085|
| |Colonial Heights city|    21| 1208.981|  0.000|   197| 11341.393| 106.917|  17,370|
| |Petersburg city|    19| 606.138| 27.345|   515| 16429.528| 227.871|  31,346|
| |Rockingham County|    19| 231.854|  3.487|   938| 11446.283| 64.501|  81,948|
| |Roanoke County|    19| 201.728|  1.517| 1,513| 16063.959| 247.231|  94,186|
| |Newport News city|    18| 100.432|  1.594| 1,827| 10193.890| 149.852| 179,225|
| |Albemarle County|    16| 146.346|  5.227|   838|  7664.868| 104.533| 109,330|
| |Accomack County|    16| 495.111|  4.421| 1,100| 34038.866| 92.833|  32,316|
| |James City County|    16| 209.087|  0.000|   608|  7945.324| 110.144|  76,523|
| |Charlottesville city|    15| 317.353|  6.045|   542| 11467.016| 190.412|  47,266|
| |Emporia city|    15| 2805.836|  0.000|   175| 32734.755| 267.222|   5,346|
| |Nottoway County|    13| 853.466| 37.515|   182| 11948.529| 56.273|  15,232|
| |Southampton County|    13| 737.338|  0.000|   267| 15143.781| 234.976|  17,631|
| |Carroll County|    13| 436.373|  0.000|   334| 11211.440| 110.292|  29,791|
| |Culpeper County|    12| 228.115|  0.000| 1,005| 19104.648| 146.645|  52,605|
| |Greensville County|    11| 970.360| 25.204|   482| 42519.407| 718.318|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   410| 17980.879| 369.642|  22,802|
| |Stafford County|     9| 58.869|  1.869| 1,374|  8987.324| 100.918| 152,882|
| |Sussex County|     9| 806.524|  0.000|   302| 27063.357| 320.049|  11,159|
| |Fluvanna County|     9| 330.033|  5.239|   192|  7040.704| 94.295|  27,270|
| |Fauquier County|     9| 126.365|  2.006|   616|  8649.013| 84.244|  71,222|
| |Isle of Wight County|     9| 242.529|  0.000|   387| 10428.737| 188.633|  37,109|
| |Frederick County|     9| 100.769|  0.000|   681|  7624.870| 28.791|  89,313|
| |Buckingham County|     8| 466.527| 16.662|   605| 35281.082| 74.978|  17,148|
| |Bedford County|     7| 88.611|  1.808|   359|  4544.476| 108.503|  78,997|
| |Franklin County|     7| 124.906|  0.000|   353|  6298.847| 170.790|  56,042|
| |Botetourt County|     7| 209.462|  0.000|   214|  6403.543| 111.143|  33,419|
| |Dinwiddie County|     7| 245.235|  5.005|   219|  7672.365| 95.091|  28,544|
| |Goochland County|     7| 294.700|  0.000|   163|  6862.291| 72.171|  23,753|
| |Danville city|     7| 174.808|  0.000|   405| 10113.875| 267.563|  40,044|
| |Henry County|     7| 138.458|  2.826|   588| 11630.437| 217.576|  50,557|
| |Manassas Park city|     7| 400.503|  0.000|   516| 29522.829| 130.777|  17,478|
| |Hampton city|     7| 52.041|  2.124| 1,228|  9129.433| 191.170| 134,510|
| |Williamsburg city|     6| 401.230|  0.000|   126|  8425.839| 143.297|  14,954|
| |Falls Church city|     6| 410.481|  0.000|    60|  4104.809|  9.773|  14,617|
| |Warren County|     6| 149.388|  0.000|   355|  8838.761| 24.898|  40,164|
| |Charles City County|     5| 718.081|  0.000|    52|  7468.045| 41.033|   6,963|
| |Grayson County|     5| 321.543|  9.187|   157| 10096.463| 248.048|  15,550|
| |Caroline County|     5| 162.734|  4.650|   208|  6769.731| 79.042|  30,725|
| |Washington County|     5| 93.041|  2.658|   229|  4261.258| 127.598|  53,740|
| |Hopewell city|     5| 221.936|  0.000|   272| 12073.328| 114.139|  22,529|
| |Lynchburg city|     5| 60.851|  5.216|   617|  7509.006| 274.699|  82,168|
| |Augusta County|     4| 52.939|  0.000|   276|  3652.823| 45.377|  75,558|
| |York County|     4| 58.582|  2.092|   366|  5360.281| 117.165|  68,280|
| |Patrick County|     4| 227.169|  8.113|   157|  8916.402| 340.754|  17,608|
| |Fredericksburg city|     4| 137.760|  9.840|   403| 13879.322| 221.400|  29,036|
| |Alleghany County|     4| 269.179|  9.614|    62|  4172.275| 57.681|  14,860|
| |Powhatan County|     4| 134.898|  0.000|   147|  4957.507| 96.356|  29,652|
| |King George County|     4| 149.054|  0.000|   144|  5365.926| 106.467|  26,836|
| |Winchester city|     4| 142.460|  0.000|   399| 14210.414| 35.615|  28,078|
| |Salem city|     3| 118.572|  0.000|   161|  6363.385| 129.865|  25,301|
| |Montgomery County|     3| 30.446|  0.000|   305|  3095.347| 36.245|  98,535|
| |Martinsville city|     3| 238.968|  0.000|   209| 16648.080| 455.176|  12,554|
| |Waynesboro city|     3| 132.567|  0.000|   173|  7644.719| 44.189|  22,630|
| |Smyth County|     3| 99.655|  0.000|   148|  4916.290| 132.873|  30,104|
| |Scott County|     3| 139.108|  0.000|    91|  4219.605| 245.095|  21,566|
| |Pulaski County|     3| 88.165|  0.000|    89|  2615.570| 62.975|  34,027|
| |Wythe County|     3| 104.588|  0.000|   115|  4009.204| 49.804|  28,684|
| |Orange County|     3| 80.969|  0.000|   231|  6234.650| 73.258|  37,051|
| |Westmoreland County|     3| 166.528|  7.930|   211| 11712.462| 142.738|  18,015|
| |Wise County|     3| 80.250|  0.000|   130|  3477.517| 175.787|  37,383|
| |Prince George County|     2| 52.147|  0.000|   384| 10012.255| 186.240|  38,353|
| |Pittsylvania County|     2| 33.138|  0.000|   487|  8069.059| 314.809|  60,354|
| |Northumberland County|     2| 165.358|  0.000|    72|  5952.873| 70.868|  12,095|
| |Amelia County|     2| 152.149| 10.868|    79|  6009.890| 65.207|  13,145|
| |Campbell County|     2| 36.440|  0.000|   213|  3880.842| 161.376|  54,885|
| |Brunswick County|     2| 123.221|  8.801|   228| 14047.194| 202.434|  16,231|
| |Floyd County|     2| 126.992|  9.071|    75|  4762.207| 344.693|  15,749|
| |Rappahannock County|     2| 271.370|  0.000|    43|  5834.464| 58.151|   7,370|
| |Russell County|     2| 75.228|  5.373|   115|  4325.585| 284.790|  26,586|
| |Surry County|     2| 311.429|  0.000|    52|  8097.166| 333.674|   6,422|
| |Greene County|     2| 100.913|  0.000|   163|  8224.431| 180.202|  19,819|
| |Louisa County|     2| 53.204|  0.000|   182|  4841.584| 60.805|  37,591|
| |Gloucester County|     2| 53.550|  0.000|   160|  4284.031| 57.375|  37,348|
| |King William County|     2| 116.632|  0.000|    87|  5073.478| 83.308|  17,148|
| |Buena Vista city|     1| 154.369| 22.053|    50|  7718.432| 44.105|   6,478|
| |Essex County|     1| 91.299|  0.000|   102|  9312.517| 326.069|  10,953|
| |Dickenson County|     1| 69.842|  9.977|    41|  2863.528| 169.617|  14,318|
| |Lee County|     1| 42.693|  0.000|   115|  4909.704| 121.980|  23,423|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648| 142.349|   7,025|
| |Halifax County|     1| 29.489|  0.000|   155|  4570.788| 75.829|  33,911|
| |Rockbridge County|     1| 44.301|  6.329|    67|  2968.148|  0.000|  22,573|
| |New Kent County|     1| 43.307|  0.000|   128|  5543.285| 68.054|  23,091|
| |Middlesex County|     1| 94.500|  0.000|    41|  3874.504| 189.000|  10,582|
| |Madison County|     1| 75.409|  0.000|    69|  5203.228| 86.182|  13,261|
| |Lunenburg County|     1| 81.994|  0.000|    62|  5083.634| 81.994|  12,196|
| |Buchanan County|     0|  0.000|  0.000|    80|  3808.798| 61.213|  21,004|
| |Charlotte County|     0|  0.000|  0.000|    53|  4461.279| 48.100|  11,880|
| |Clarke County|     0|  0.000|  0.000|    71|  4856.693| 19.544|  14,619|
| |Craig County|     0|  0.000|  0.000|    17|  3313.194| 27.842|   5,131|
| |Cumberland County|     0|  0.000|  0.000|    76|  7652.034| 115.068|   9,932|
| |Staunton city|     0|  0.000|  0.000|   151|  6056.474| 51.569|  24,932|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Bland County|     0|  0.000|  0.000|    19|  3025.478| 272.975|   6,280|
| |Tazewell County|     0|  0.000|  0.000|   117|  2882.128| 77.420|  40,595|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418| 25.796|   5,538|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|
| |Poquoson city|     0|  0.000|  0.000|    44|  3585.690| 93.135|  12,271|
| |Norton city|     0|  0.000|  0.000|    18|  4521.477| 179.424|   3,981|
| |Bristol city|     0|  0.000|  0.000|    78|  4653.383| 127.840|  16,762|
| |Nelson County|     0|  0.000|  0.000|    48|  3215.003| 133.958|  14,930|
| |Amherst County|     0|  0.000|  0.000|   175|  5537.099| 275.725|  31,605|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Appomattox County|     0|  0.000|  0.000|    85|  5342.216| 134.678|  15,911|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Giles County|     0|  0.000|  0.000|    24|  1435.407|  8.544|  16,720|
| |Radford city|     0|  0.000|  0.000|    53|  2904.269| 211.362|  18,249|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726| 195.695|   2,190|
| |Lancaster County|     0|  0.000|  0.000|    37|  3489.578| 80.840|  10,603|
| |Lexington city|     0|  0.000|  0.000|    33|  4431.910| 19.186|   7,446|
| |Mathews County|     0|  0.000|  0.000|    18|  2037.582| 64.685|   8,834|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,192| 208.999| N/A|136,346| 13000.087| N/A|10,488,084|
| |Mecklenburg County|   228| 205.340|  2.316|22,255| 20043.121| 178.964|1,110,356|
| |Wake County|   170| 152.911|  4.754|12,028| 10818.872| 117.574|1,111,761|
| |Guilford County|   156| 290.409|  2.393| 5,651| 10519.869| 117.546| 537,174|
| |Durham County|    80| 248.843|  1.333| 6,171| 19195.118| 133.309| 321,488|
| |Henderson County|    54| 459.899|  1.217| 1,482| 12621.682| 144.783| 117,417|
| |Robeson County|    53| 405.742|  2.187| 2,804| 21466.029| 184.826| 130,625|
| |Chatham County|    52| 698.268|  3.837| 1,300| 17456.694| 126.609|  74,470|
| |Gaston County|    52| 231.596|  9.544| 3,322| 14795.416| 196.602| 224,529|
| |Forsyth County|    52| 136.021|  1.121| 5,273| 13793.013| 130.042| 382,295|
| |Cumberland County|    51| 152.008|  0.426| 3,081|  9183.062| 147.750| 335,509|
| |Cabarrus County|    50| 230.997|  2.640| 2,630| 12150.444| 147.838| 216,453|
| |Rowan County|    48| 337.819|  0.000| 2,197| 15462.249| 191.028| 142,088|
| |Duplin County|    48| 817.146| 14.592| 2,013| 34269.080| 184.831|  58,741|
| |Columbus County|    48| 864.740|  5.147|   903| 16267.925| 198.170|  55,508|
| |Orange County|    47| 316.549|  1.924| 1,348|  9078.908| 59.654| 148,476|
| |Buncombe County|    47| 179.945|  0.547| 1,884|  7213.112| 106.654| 261,191|
| |Johnston County|    46| 219.739|  1.365| 3,304| 15783.012| 168.558| 209,339|
| |Union County|    43| 179.272|  1.787| 3,096| 12907.583| 175.103| 239,859|
| |Wayne County|    42| 341.100|  5.801| 2,412| 19588.893| 116.020| 123,131|
| |Alamance County|    41| 241.875|  0.000| 2,448| 14441.711| 203.108| 169,509|
| |Vance County|    41| 920.624|  3.208|   773| 17357.135| 134.725|  44,535|
| |Harnett County|    39| 286.815|  3.152| 1,288|  9472.260| 154.439| 135,976|
| |Randolph County|    37| 257.540|  0.994| 2,174| 15132.215| 119.324| 143,667|
| |Wilson County|    35| 427.868|  1.746| 1,490| 18214.936| 158.922|  81,801|
| |Catawba County|    29| 181.760|  4.477| 2,120| 13287.287| 198.772| 159,551|
| |Burke County|    28| 309.444|  3.158| 1,655| 18290.324| 156.301|  90,485|
| |Granville County|    27| 446.702|  4.727| 1,245| 20597.919| 163.082|  60,443|
| |Franklin County|    26| 373.108|  2.050|   866| 12427.352| 170.153|  69,685|
| |Stanly County|    26| 413.973| 34.119| 1,064| 16941.057| 379.855|  62,806|
| |Brunswick County|    21| 147.038|  4.001| 1,249|  8745.274| 61.016| 142,820|
| |Cleveland County|    20| 204.192|  8.751| 1,178| 12026.913| 231.904|  97,947|
| |Moore County|    20| 198.255|  0.000| 1,009| 10001.983| 168.517| 100,880|
| |Pasquotank County|    20| 502.210| 10.762|   401| 10069.305| 179.361|  39,824|
| |New Hanover County|    20| 85.298|  0.609| 2,566| 10943.691| 139.523| 234,473|
| |Davidson County|    18| 107.393|  0.852| 1,781| 10625.921| 117.621| 167,609|
| |Iredell County|    18| 99.007|  0.000| 1,820| 10010.671| 101.364| 181,806|
| |Northampton County|    16| 821.229|  0.000|   350| 17964.379| 315.293|  19,483|
| |McDowell County|    14| 305.971| 15.611|   683| 14927.004| 246.650|  45,756|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996| 299.667|  27,173|
| |Caldwell County|    14| 170.362|  3.477| 1,215| 14784.979| 163.408|  82,178|
| |Rutherford County|    14| 208.865|  2.131|   746| 11129.511| 221.652|  67,029|
| |Sampson County|    14| 220.365|  4.497| 1,508| 23736.444| 195.630|  63,531|
| |Edgecombe County|    13| 252.565|  5.551|   646| 12550.513| 185.954|  51,472|
| |Lenoir County|    12| 214.481|  0.000|   573| 10241.470| 97.027|  55,949|
| |Craven County|    12| 117.487|  2.797|   699|  6843.615| 95.108| 102,139|
| |Haywood County|    12| 192.564| 13.755|   432|  6932.298| 307.185|  62,317|
| |Nash County|    12| 127.256|  1.515| 1,180| 12513.521| 215.123|  94,298|
| |Wilkes County|    11| 160.791|  2.088|   834| 12190.844| 208.819|  68,412|
| |Hertford County|    11| 464.586|  0.000|   344| 14528.868| 368.049|  23,677|
| |Pitt County|    11| 60.860|  0.000| 2,020| 11176.152| 200.760| 180,742|
| |Lee County|    11| 178.054|  2.312| 1,289| 20864.695| 208.115|  61,779|
| |Onslow County|    10| 50.521|  0.000| 1,065|  5380.473| 97.433| 197,938|
| |Surry County|    10| 139.309|  5.970|   954| 13290.055| 169.161|  71,783|
| |Hoke County|     9| 162.943|  2.586|   717| 12981.135| 121.561|  55,234|
| |Lincoln County|     9| 104.516|  9.954|   848|  9847.755| 169.217|  86,111|
| |Richmond County|     9| 200.763|  3.187|   506| 11287.336| 89.228|  44,829|
| |Rockingham County|     8| 87.902|  1.570|   549|  6032.304| 124.005|  91,010|
| |Bladen County|     7| 213.923|  0.000|   623| 19039.179| 170.266|  32,722|
| |Warren County|     7| 354.772|  7.240|   256| 12974.507| 115.844|  19,731|
| |Carteret County|     6| 86.364|  2.056|   344|  4951.564| 100.759|  69,473|
| |Yadkin County|     6| 159.291|  0.000|   541| 14362.705| 193.424|  37,667|
| |Davie County|     6| 140.036|  6.668|   422|  9849.227| 170.044|  42,846|
| |Halifax County|     6| 119.976|  0.000|   700| 13997.201| 174.251|  50,010|
| |Martin County|     6| 267.380|  0.000|   258| 11497.326| 120.957|  22,440|
| |Polk County|     5| 241.266|  0.000|   163|  7865.277| 179.226|  20,724|
| |Jackson County|     5| 113.797|  6.503|   447| 10173.426| 172.321|  43,938|
| |Bertie County|     5| 263.894|  0.000|   272| 14355.835| 188.496|  18,947|
| |Jones County|     4| 424.674| 15.167|    93|  9873.660| 515.675|   9,419|
| |Cherokee County|     4| 139.801|  4.993|   273|  9541.451| 184.738|  28,612|
| |Washington County|     4| 345.423| 12.337|   133| 11485.320| 160.375|  11,580|
| |Pender County|     3| 47.574|  0.000|   658| 10434.507| 88.351|  63,060|
| |Stokes County|     3| 65.802|  0.000|   291|  6382.839| 81.470|  45,591|
| |Anson County|     3| 122.719|  5.844|   328| 13417.328| 151.938|  24,446|
| |Greene County|     3| 142.389|  0.000|   331| 15710.285| 155.950|  21,069|
| |Macon County|     3| 83.663|  3.984|   463| 12912.042| 67.727|  35,858|
| |Alexander County|     2| 53.338|  0.000|   299|  7973.971| 15.239|  37,497|
| |Beaufort County|     2| 42.559|  0.000|   406|  8639.401| 176.314|  46,994|
| |Scotland County|     2| 57.433|  0.000|   343|  9849.812| 254.347|  34,823|
| |Swain County|     2| 140.144|  0.000|   119|  8338.589| 140.144|  14,271|
| |Gates County|     2| 172.980|  0.000|    46|  3978.550| 37.067|  11,562|
| |Person County|     2| 50.646|  0.000|   223|  5646.999| 108.527|  39,490|
| |Perquimans County|     2| 148.555|  0.000|    86|  6387.878| 201.611|  13,463|
| |Mitchell County|     2| 133.654|  0.000|   116|  7751.938| 76.374|  14,964|
| |Camden County|     2| 184.043|  0.000|    72|  6625.564| 118.314|  10,867|
| |Caswell County|     2| 88.480|  0.000|   195|  8626.792| 69.520|  22,604|
| |Dare County|     2| 54.041|  3.860|   209|  5647.275| 38.601|  37,009|
| |Ashe County|     1| 36.761|  0.000|   157|  5771.422| 199.558|  27,203|
| |Pamlico County|     1| 78.579|  0.000|    68|  5343.391| 112.256|  12,726|
| |Chowan County|     1| 71.721|  0.000|   157| 11260.131| 194.670|  13,943|
| |Transylvania County|     1| 29.082|  0.000|   137|  3984.295| 41.546|  34,385|
| |Tyrrell County|     1| 249.004|  0.000|    98| 24402.390| 249.004|   4,016|
| |Clay County|     0|  0.000|  0.000|    76|  6766.984| 139.919|  11,231|
| |Currituck County|     0|  0.000|  0.000|    73|  2629.399| 15.437|  27,763|
| |Avery County|     0|  0.000|  0.000|    99|  5638.777| 130.188|  17,557|
| |Alleghany County|     0|  0.000|  0.000|   167| 14995.062| 885.081|  11,137|
| |Madison County|     0|  0.000|  0.000|    45|  2068.490| 45.966|  21,755|
| |Graham County|     0|  0.000|  0.000|    39|  4620.306| 203.090|   8,441|
| |Hyde County|     0|  0.000|  0.000|    44|  8912.295| 202.552|   4,937|
| |Watauga County|     0|  0.000|  0.000|   292|  5197.857| 91.547|  56,177|
| |Yancey County|     0|  0.000|  0.000|   101|  5589.684| 55.343|  18,069|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,031| 394.467| N/A|100,435| 19506.813| N/A|5,148,714|
| |Greenville County|   208| 397.294|  5.457|10,916| 20850.285| 192.371| 523,542|
| |Charleston County|   194| 471.554|  9.028|12,324| 29955.810| 253.486| 411,406|
| |Horry County|   153| 432.105|  9.280| 8,594| 24271.283| 192.853| 354,081|
| |Richland County|   152| 365.596|  4.123| 8,774| 21103.572| 274.541| 415,759|
| |Florence County|   115| 831.568| 17.561| 3,436| 24845.798| 416.300| 138,293|
| |Lexington County|   110| 368.201|  2.869| 4,955| 16585.774| 143.933| 298,750|
| |Spartanburg County|   103| 322.091|  8.041| 4,080| 12758.572| 151.441| 319,785|
| |Berkeley County|    66| 289.592|  4.388| 4,158| 18244.284| 190.554| 227,907|
| |Orangeburg County|    64| 742.675| 11.604| 2,420| 28082.390| 381.284|  86,175|
| |Anderson County|    63| 311.022| 11.284| 2,335| 11527.562| 189.716| 202,558|
| |Beaufort County|    56| 291.481|  4.461| 4,105| 21366.632| 351.711| 192,122|
| |Clarendon County|    52| 1540.969|  8.467|   838| 24833.309| 249.772|  33,745|
| |Sumter County|    51| 477.882|  8.032| 2,517| 23584.861| 274.414| 106,721|
| |Dorchester County|    47| 288.682|  7.020| 3,113| 19120.565| 292.192| 162,809|
| |Laurens County|    46| 681.552| 25.399| 1,330| 19705.747| 228.595|  67,493|
| |Aiken County|    38| 222.389| 10.033| 1,868| 10932.160| 244.962| 170,872|
| |Darlington County|    35| 525.384|  4.289| 1,295| 19439.191| 441.751|  66,618|
| |Colleton County|    34| 902.407| 11.375|   814| 21604.693| 193.373|  37,677|
| |Williamsburg County|    31| 1020.811| 18.817| 1,016| 33456.270| 465.716|  30,368|
| |Lee County|    29| 1723.318| 16.979|   562| 33396.720| 339.570|  16,828|
| |York County|    29| 103.211|  0.508| 3,568| 12698.458| 202.354| 280,979|
| |Cherokee County|    28| 488.656|  7.479|   638| 11134.380| 221.890|  57,300|
| |Pickens County|    27| 212.793|  4.504| 1,850| 14580.247| 140.736| 126,884|
| |Lancaster County|    25| 255.071|  5.830| 1,209| 12335.224| 212.802|  98,012|
| |Kershaw County|    25| 375.652|  4.293| 1,394| 20946.342| 236.124|  66,551|
| |Dillon County|    24| 787.427|  4.687|   642| 21063.683| 365.591|  30,479|
| |Fairfield County|    23| 1029.221|  0.000|   567| 25372.533| 198.173|  22,347|
| |Bamberg County|    22| 1564.055| 60.937|   473| 33627.186| 324.998|  14,066|
| |Chesterfield County|    21| 460.022|  6.259|   769| 16845.564| 228.446|  45,650|
| |Georgetown County|    19| 303.127|  0.000| 1,454| 23197.192| 380.618|  62,680|
| |Greenwood County|    18| 254.198|  6.052| 1,390| 19629.719| 266.302|  70,811|
| |Jasper County|    15| 498.786|  9.501|   594| 19751.937| 422.781|  30,073|
| |Chester County|    14| 434.189| 13.292|   665| 20623.992| 438.620|  32,244|
| |Marion County|    13| 424.047|  4.660|   554| 18070.914| 149.115|  30,657|
| |Calhoun County|    11| 755.858|  9.816|   380| 26111.455| 647.878|  14,553|
| |Newberry County|    10| 260.146|  7.433|   845| 21982.310| 260.146|  38,440|
| |Abbeville County|     9| 366.943| 11.649|   335| 13658.417| 262.102|  24,527|
| |Oconee County|     9| 113.142|  3.592|   827| 10396.500| 145.468|  79,546|
| |Hampton County|     9| 468.214| 14.864|   432| 22474.248| 505.373|  19,222|
| |Saluda County|     8| 390.759|  0.000|   458| 22370.928| 293.069|  20,473|
| |Edgefield County|     7| 256.787|  5.241|   330| 12105.649| 225.343|  27,260|
| |Barnwell County|     5| 239.624|  6.846|   413| 19792.965| 499.788|  20,866|
| |Union County|     4| 146.434| 10.460|   362| 13252.306| 146.434|  27,316|
| |Marlboro County|     4| 153.151|  0.000|   497| 19029.022| 333.651|  26,118|
| |Allendale County|     3| 345.304|  0.000|   221| 25437.385| 526.177|   8,688|
| |McCormick County|     2| 211.349|  0.000|   118| 12469.619| 181.157|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,896| 637.065| N/A|67,173| 22570.443| N/A|2,976,149|
| |Hinds County|   118| 508.972|  7.394| 5,613| 24210.663| 248.940| 231,840|
| |Lauderdale County|    92| 1241.147|  7.709| 1,412| 19048.904| 171.525|  74,125|
| |Neshoba County|    92| 3159.558| 24.531| 1,286| 44165.121| 451.365|  29,118|
| |Madison County|    66| 621.048| 16.131| 2,422| 22790.575| 189.541| 106,272|
| |Leflore County|    63| 2235.390| 20.276|   933| 33105.063| 511.960|  28,183|
| |Jones County|    58| 851.714|  2.098| 1,899| 27886.282| 281.107|  68,098|
| |Forrest County|    56| 747.693|  5.722| 1,806| 24113.115| 333.792|  74,897|
| |Monroe County|    55| 1560.195| 20.262|   796| 22580.279| 401.193|  35,252|
| |Holmes County|    48| 2821.869|  8.398|   892| 52439.741| 411.523|  17,010|
| |Jackson County|    42| 292.444|  7.958| 2,276| 15847.706| 345.164| 143,617|
| |Washington County|    41| 933.749| 29.281| 1,663| 37873.784| 595.387|  43,909|
| |Lincoln County|    41| 1200.480|  8.366|   817| 23921.764| 309.531|  34,153|
| |Lee County|    41| 479.891| 18.393| 1,462| 17112.224| 384.582|  85,436|
| |Oktibbeha County|    39| 786.496| 11.524| 1,122| 22626.898| 201.666|  49,587|
| |Pearl River County|    39| 702.260|  7.717|   550|  9903.664| 174.922|  55,535|
| |Lowndes County|    37| 631.453| 12.190| 1,077| 18380.408| 253.556|  58,595|
| |Pike County|    36| 916.310| 14.545|   936| 23824.068| 399.977|  39,288|
| |Harrison County|    36| 173.010|  2.746| 2,520| 12110.727| 289.724| 208,080|
| |Bolivar County|    34| 1110.095|  9.329| 1,113| 36339.297| 811.582|  30,628|
| |Rankin County|    34| 218.972|  5.520| 2,283| 14703.325| 146.288| 155,271|
| |Warren County|    33| 727.177| 22.036| 1,093| 24084.969| 406.086|  45,381|
| |DeSoto County|    31| 167.617|  3.090| 3,658| 19778.853| 291.979| 184,945|
| |Simpson County|    30| 1125.366| 21.436|   796| 29859.704| 455.505|  26,658|
| |Tate County|    29| 1023.975| 30.265|   734| 25917.164| 448.935|  28,321|
| |Copiah County|    28| 997.684| 20.361|   954| 33992.517| 229.060|  28,065|
| |Clarke County|    26| 1672.994|  9.192|   327| 21041.117| 266.576|  15,541|
| |Adams County|    25| 814.518|  0.000|   623| 20297.788| 200.139|  30,693|
| |Sunflower County|    25| 995.619| 17.068| 1,039| 41377.937| 756.671|  25,110|
| |Leake County|    25| 1097.165|  0.000|   788| 34582.638| 131.660|  22,786|
| |Attala County|    25| 1375.592|  7.861|   522| 28722.351| 212.234|  18,174|
| |Grenada County|    21| 1011.658|  6.882|   847| 40803.546| 240.871|  20,758|
| |Wayne County|    21| 1040.480|  0.000|   767| 38002.279| 247.733|  20,183|
| |Scott County|    20| 711.136| 15.239| 1,003| 35663.490| 253.977|  28,124|
| |Marion County|    20| 813.901| 11.627|   677| 27550.564| 453.459|  24,573|
| |Walthall County|    20| 1399.972| 20.000|   502| 35139.297| 599.988|  14,286|
| |Chickasaw County|    19| 1110.916|  0.000|   462| 27012.805| 225.524|  17,103|
| |Lafayette County|    16| 296.192| 18.512|   973| 18012.181| 275.036|  54,019|
| |Union County|    16| 555.266| 14.873|   636| 22071.838| 580.055|  28,815|
| |Winston County|    16| 891.117|  7.956|   620| 34530.771| 389.864|  17,955|
| |Hancock County|    14| 293.920|  0.000|   390|  8187.773| 191.948|  47,632|
| |Kemper County|    14| 1437.077|  0.000|   233| 23917.060| 146.640|   9,742|
| |Lamar County|    14| 221.019|  4.511| 1,220| 19260.218| 236.806|  63,343|
| |Clay County|    14| 724.788|  0.000|   396| 20501.139| 207.082|  19,316|
| |Covington County|    13| 697.575| 15.331|   612| 32839.665| 260.632|  18,636|
| |Claiborne County|    13| 1446.373|  0.000|   407| 45282.599| 111.259|   8,988|
| |Tippah County|    13| 590.506|  6.489|   366| 16625.028| 402.323|  22,015|
| |Smith County|    13| 816.788|  0.000|   405| 25446.092| 251.319|  15,916|
| |Panola County|    13| 380.206|  8.356| 1,059| 30972.157| 635.069|  34,192|
| |Wilkinson County|    13| 1506.373| 16.554|   212| 24565.469| 413.839|   8,630|
| |Coahoma County|    13| 587.597| 19.371|   760| 34351.835| 652.168|  22,124|
| |Yazoo County|    12| 404.176|  4.812|   831| 27989.222| 279.074|  29,690|
| |Webster County|    12| 1238.518|  0.000|   234| 24151.099| 545.538|   9,689|
| |Greene County|    12| 883.262| 10.515|   250| 18401.295| 252.361|  13,586|
| |Noxubee County|    11| 1055.966| 13.714|   457| 43870.596| 548.554|  10,417|
| |Humphreys County|    11| 1364.087|  0.000|   293| 36334.325| 425.170|   8,064|
| |Carroll County|    11| 1105.861|  0.000|   261| 26239.067| 229.789|   9,947|
| |Newton County|    11| 523.361|  0.000|   542| 25787.420| 176.719|  21,018|
| |Yalobusha County|    10| 825.900|  0.000|   315| 26015.857|  0.000|  12,108|
| |Prentiss County|    10| 397.994| 22.743|   412| 16397.357| 426.422|  25,126|
| |Tallahatchie County|    10| 724.165|  0.000|   531| 38453.183| 393.118|  13,809|
| |Itawamba County|    10| 427.533|  0.000|   359| 15348.440| 317.596|  23,390|
| |Jasper County|     9| 549.350|  8.720|   386| 23561.008| 95.918|  16,383|
| |Marshall County|     9| 255.001|  4.048|   695| 19691.732| 522.145|  35,294|
| |Calhoun County|     9| 626.697|  9.948|   418| 29106.608| 437.693|  14,361|
| |Lawrence County|     8| 635.627| 34.051|   323| 25663.436| 113.505|  12,586|
| |Pontotoc County|     8| 248.648|  4.440|   827| 25703.985| 457.335|  32,174|
| |Perry County|     7| 584.649|  0.000|   236| 19711.016| 178.974|  11,973|
| |Tunica County|     7| 726.744| 14.832|   337| 34987.542| 1067.869|   9,632|
| |Jefferson County|     7| 1001.431| 20.437|   196| 28040.057| 102.187|   6,990|
| |Jefferson Davis County|     6| 539.180|  0.000|   231| 20758.447| 423.642|  11,128|
| |Amite County|     6| 487.924| 11.617|   232| 18866.390| 255.579|  12,297|
| |Tishomingo County|     5| 257.958| 14.740|   417| 21513.698| 744.393|  19,383|
| |Alcorn County|     5| 135.307|  3.866|   428| 11582.280| 286.078|  36,953|
| |Stone County|     5| 272.688| 15.582|   199| 10852.967| 397.345|  18,336|
| |George County|     5| 204.082|  0.000|   581| 23714.286| 233.236|  24,500|
| |Sharkey County|     5| 1157.140| 132.245|   197| 45591.298| 562.039|   4,321|
| |Montgomery County|     5| 511.509| 29.229|   326| 33350.384| 511.509|   9,775|
| |Choctaw County|     4| 487.211|  0.000|   134| 16321.559| 139.203|   8,210|
| |Franklin County|     2| 259.302|  0.000|   127| 16465.707| 240.781|   7,713|
| |Issaquena County|     1| 753.580|  0.000|    26| 19593.067| 538.271|   1,327|
| |Benton County|     1| 121.080| 17.297|   144| 17435.525| 345.943|   8,259|
| |Quitman County|     1| 147.232|  0.000|   269| 39605.418| 1009.591|   6,792|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,858| 322.640| N/A|50,642|  8793.944| N/A|5,758,736|
| |Denver County|   414| 569.298| N/A|10,224| 14059.193| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.218| 7,311| 11134.803| 66.360| 656,590|
| |Jefferson County|   228| 391.160|  0.245| 4,177|  7166.128| 55.880| 582,881|
| |Adams County|   176| 340.149|  1.380| 6,491| 12544.910| 110.714| 517,421|
| |Weld County|   143| 440.689|  0.880| 3,709| 11430.174| 71.761| 324,492|
| |El Paso County|   137| 190.171|  0.198| 5,006|  6948.888| 83.683| 720,403|
| |Boulder County|    75| 229.923|  0.000| 2,046|  6272.303| 58.685| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,734|  4938.004| 35.394| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   685| 23565.433| 39.317|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,554|  4354.173| 61.242| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   693|  4114.615| 67.856| 168,424|
| |Broomfield County|    32| 454.126| N/A|   473|  6712.552| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   303| 14885.046| 112.287|  20,356|
| |Montrose County|    13| 304.037|  0.000|   305|  7133.168| 86.868|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,123| 20371.143| 189.174|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   230| 14168.669| 52.802|  16,233|
| |Routt County|     7| 273.032|  5.572|   125|  4875.575| 100.298|  25,638|
| |Gunnison County|     6| 343.603|  0.000|   272| 15576.681| 147.259|  17,462|
| |Otero County|     6| 328.263|  0.000|    71|  3884.451| 117.237|  18,278|
| |Logan County|     5| 223.125|  0.000|   651| 29050.828| 19.125|  22,409|
| |Montezuma County|     4| 152.771|  0.000|   112|  4277.585| 21.824|  26,183|
| |Garfield County|     4| 66.599|  0.000|   767| 12770.350| 128.441|  60,061|
| |Summit County|     4| 128.986|  0.000|   328| 10576.892| 23.033|  31,011|
| |Mesa County|     4| 25.939|  0.926|   306|  1984.307| 36.129| 154,210|
| |Teller County|     3| 118.166|  0.000|   132|  5199.307| 106.912|  25,388|
| |Kit Carson County|     3| 422.714|  0.000|    51|  7186.135| 161.034|   7,097|
| |Elbert County|     2| 74.825|  0.000|   105|  3928.318| 101.548|  26,729|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Pitkin County|     2| 112.568|  0.000|   187| 10525.131| 144.731|  17,767|
| |La Plata County|     2| 35.574|  0.000|   212|  3770.833| 30.492|  56,221|
| |Rio Grande County|     2| 177.510|  0.000|    89|  7899.175| 25.359|  11,267|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202| 28.848|   4,952|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925| 41.426|   6,897|
| |Clear Creek County|     1| 103.093|  0.000|    30|  3092.784| 44.183|   9,700|
| |Crowley County|     1| 164.989|  0.000|    72| 11879.228|  0.000|   6,061|
| |Grand County|     1| 63.557|  0.000|    46|  2923.605| 27.239|  15,734|
| |Delta County|     1| 32.090|  0.000|   121|  3882.934| 55.012|  31,162|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  7.581|  18,845|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Moffat County|     1| 75.284|  0.000|    31|  2333.810| 64.529|  13,283|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517| 102.627|   1,392|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053| 14.259|  10,019|
| |Washington County|     0|  0.000|  0.000|    48|  9779.951| 29.107|   4,908|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|
| |San Miguel County|     0|  0.000|  0.000|    89| 10881.526| 227.062|   8,179|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Lake County|     0|  0.000|  0.000|    77|  9474.591| 105.469|   8,127|
| |Las Animas County|     0|  0.000|  0.000|    17|  1171.929| 19.696|  14,506|
| |Rio Blanco County|     0|  0.000|  0.000|    16|  2530.044| 203.307|   6,324|
| |Prowers County|     0|  0.000|  0.000|    53|  4354.256| 58.683|  12,172|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263| 50.117|   5,701|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Fremont County|     0|  0.000|  0.000|   125|  2612.931| 41.807|  47,839|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |Gilpin County|     0|  0.000|  0.000|    16|  2562.870|  0.000|   6,243|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Archuleta County|     0|  0.000|  0.000|    36|  2566.113| 30.549|  14,029|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774| 39.893|   3,581|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Bent County|     0|  0.000|  0.000|     9|  1613.771| 102.462|   5,577|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347| 78.021|   1,831|
| |Conejos County|     0|  0.000|  0.000|    23|  2803.169|  0.000|   8,205|
| |Costilla County|     0|  0.000|  0.000|    23|  5917.160| 36.753|   3,887|
| |Custer County|     0|  0.000|  0.000|    11|  2170.481| 28.188|   5,068|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,707| 348.141| N/A|97,735| 19932.962| N/A|4,903,185|
| |Jefferson County|   243| 368.980|  3.905|13,109| 19905.159| 316.485| 658,573|
| |Mobile County|   207| 500.956|  5.532| 9,947| 24072.506| 328.093| 413,210|
| |Montgomery County|   148| 653.462|  3.154| 6,835| 30178.466| 401.791| 226,486|
| |Tallapoosa County|    79| 1957.044|  3.539|   855| 21180.667| 180.487|  40,367|
| |Tuscaloosa County|    73| 348.690|  6.824| 4,213| 20123.713| 205.393| 209,355|
| |Walker County|    64| 1007.541|  2.249| 1,526| 24023.551| 155.179|  63,521|
| |Lee County|    45| 273.486|  4.341| 2,678| 16275.480| 162.355| 164,542|
| |Chambers County|    38| 1142.720|  0.000|   841| 25290.191| 115.990|  33,254|
| |Elmore County|    38| 467.928|  1.759| 1,723| 21216.860| 244.519|  81,209|
| |Butler County|    36| 1851.090|  7.346|   764| 39284.245| 95.493|  19,448|
| |Marshall County|    36| 372.001|  8.857| 3,167| 32725.732| 324.763|  96,774|
| |Shelby County|    35| 160.770|  1.969| 3,283| 15080.247| 184.394| 217,702|
| |Madison County|    34| 91.175|  3.448| 5,378| 14421.749| 170.857| 372,909|
| |Etowah County|    31| 303.125|  8.381| 2,121| 20739.625| 289.156| 102,268|
| |Hale County|    26| 1774.623|  9.751|   476| 32489.250| 263.268|  14,651|
| |Baldwin County|    25| 111.990|  1.920| 3,544| 15875.718| 236.139| 223,234|
| |Dale County|    24| 488.083| 14.526|   834| 16960.872| 168.505|  49,172|
| |Lowndes County|    24| 2467.613|  0.000|   572| 58811.433| 381.892|   9,726|
| |Marion County|    24| 807.836|  0.000|   574| 19320.745| 187.533|  29,709|
| |Dallas County|    23| 618.346|  0.000| 1,323| 35568.341| 165.148|  37,196|
| |Autauga County|    21| 375.879|  2.557| 1,169| 20923.947| 406.563|  55,869|
| |Covington County|    20| 539.826|  0.000|   735| 19838.592| 119.533|  37,049|
| |Franklin County|    20| 637.714|  0.000| 1,274| 40622.409| 409.959|  31,362|
| |Lauderdale County|    19| 204.898| 10.784| 1,167| 12585.060| 175.627|  92,729|
| |Sumter County|    18| 1448.459|  0.000|   360| 28969.180|  0.000|  12,427|
| |Morgan County|    18| 150.402|  3.581| 2,393| 19995.154| 223.216| 119,679|
| |Escambia County|    17| 464.062|  7.799| 1,082| 29536.211| 456.263|  36,633|
| |St. Clair County|    17| 189.919|  7.980| 1,338| 14947.717| 248.969|  89,512|
| |Marengo County|    15| 795.208|  7.573|   552| 29263.638| 280.216|  18,863|
| |Calhoun County|    14| 123.234|  6.287| 1,784| 15703.534| 313.115| 113,605|
| |Talladega County|    14| 175.048|  1.786| 1,026| 12828.528| 242.924|  79,978|
| |Macon County|    14| 774.851|  7.907|   335| 18541.067| 213.479|  18,068|
| |Limestone County|    13| 131.426|  0.000| 1,333| 13476.217| 216.636|  98,915|
| |DeKalb County|    13| 181.785|  0.000| 1,819| 25435.935| 283.665|  71,513|
| |Colbert County|    13| 235.332|  2.586| 1,181| 21379.048| 271.537|  55,241|
| |Houston County|    12| 113.334|  0.000| 1,398| 13203.377| 120.080| 105,882|
| |Cullman County|    12| 143.253|  1.705| 1,225| 14623.723| 191.004|  83,768|
| |Washington County|    12| 735.024|  8.750|   391| 23949.528| 708.773|  16,326|
| |Choctaw County|    12| 953.213|  0.000|   283| 22479.943| 113.478|  12,589|
| |Greene County|    11| 1356.183|  0.000|   251| 30945.629| 193.740|   8,111|
| |Winston County|    11| 465.530|  0.000|   453| 19171.357| 151.146|  23,629|
| |Bullock County|    11| 1089.001|  0.000|   464| 45936.046| 381.858|  10,101|
| |Conecuh County|    10| 828.706|  0.000|   393| 32568.161| 260.451|  12,067|
| |Wilcox County|    10| 964.041| 13.772|   429| 41357.370| 371.844|  10,373|
| |Randolph County|    10| 440.102|  0.000|   401| 17648.094| 81.733|  22,722|
| |Clarke County|     9| 381.001|  0.000|   662| 28024.723| 1076.478|  23,622|
| |Pickens County|     9| 451.581|  0.000|   400| 20070.246| 265.214|  19,930|
| |Pike County|     7| 211.391|  0.000|   709| 21410.884| 237.276|  33,114|
| |Cherokee County|     7| 267.216|  0.000|   273| 10421.438| 218.136|  26,196|
| |Coffee County|     6| 114.631|  2.729|   761| 14538.994| 158.300|  52,342|
| |Chilton County|     6| 135.050|  0.000|   792| 17826.596| 305.470|  44,428|
| |Fayette County|     5| 306.711|  0.000|   207| 12697.828| 333.000|  16,302|
| |Clay County|     5| 377.786|  0.000|   258| 19493.767| 453.343|  13,235|
| |Bibb County|     5| 223.274| 12.759|   438| 19558.810| 472.065|  22,394|
| |Crenshaw County|     5| 363.055| 20.746|   318| 23090.328| 352.682|  13,772|
| |Barbour County|     5| 202.544|  0.000|   575| 23292.554| 75.231|  24,686|
| |Monroe County|     4| 192.929|  0.000|   421| 20305.793| 227.381|  20,733|
| |Jackson County|     4| 77.480|  2.767|   989| 19157.014| 478.718|  51,626|
| |Perry County|     4| 448.280|  0.000|   442| 49534.910| 224.140|   8,923|
| |Blount County|     4| 69.173|  2.470|   800| 13834.607| 192.696|  57,826|
| |Henry County|     3| 174.368|  0.000|   263| 15286.254| 166.065|  17,205|
| |Russell County|     2| 34.506|  2.465| 1,368| 23602.077| 364.777|  57,961|
| |Lamar County|     2| 144.875|  0.000|   222| 16081.130| 289.750|  13,805|
| |Coosa County|     2| 187.564|  0.000|   101|  9472.006| 147.372|  10,663|
| |Geneva County|     1| 38.065|  5.438|   261|  9934.909| 190.324|  26,271|
| |Lawrence County|     1| 30.373|  4.339|   349| 10600.170| 186.577|  32,924|
| |Cleburne County|     1| 67.069|  0.000|   127|  8517.773| 124.557|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,686| 221.408| N/A|62,864|  8255.402| N/A|7,614,893|
| |King County|   675| 299.630|  1.141|16,570|  7355.350| 67.789|2,252,782|
| |Yakima County|   211| 841.063|  3.986|10,325| 41156.282| 175.388| 250,873|
| |Snohomish County|   193| 234.769|  0.695| 5,465|  6647.747| 55.955| 822,083|
| |Pierce County|   140| 154.700|  2.052| 5,682|  6278.592| 87.610| 904,980|
| |Benton County|   115| 562.650|  3.495| 3,723| 18215.177| 155.166| 204,390|
| |Spokane County|    89| 170.238|  7.924| 4,442|  8496.590| 158.215| 522,798|
| |Franklin County|    49| 514.587|  3.001| 3,507| 36829.724| 297.050|  95,222|
| |Clark County|    43| 88.071|  0.293| 1,777|  3639.596| 48.863| 488,241|
| |Whatcom County|    39| 170.122|  0.623|   989|  4314.124| 41.752| 229,247|
| |Skagit County|    21| 162.532|  0.000|   880|  6810.882| 71.868| 129,205|
| |Kittitas County|    19| 396.370|  5.960|   373|  7781.371| 74.506|  47,935|
| |Grant County|    13| 133.015|  0.000| 1,491| 15255.850| 314.267|  97,733|
| |Thurston County|    11| 37.861|  1.475|   717|  2467.853| 38.844| 290,536|
| |Island County|    11| 129.197|  0.000|   250|  2936.306| 18.457|  85,141|
| |Chelan County|    10| 129.534|  0.000| 1,334| 17279.793| 371.947|  77,200|
| |Kitsap County|     7| 25.785|  1.579|   739|  2722.186| 49.466| 271,473|
| |Douglas County|     7| 161.183|  0.000|   948| 21828.732| 460.522|  43,429|
| |Cowlitz County|     5| 45.211|  0.000|   482|  4358.323| 46.503| 110,593|
| |Adams County|     5| 250.213|  7.149|   440| 22018.716| 314.553|  19,983|
| |Okanogan County|     4| 94.690|  6.764|   864| 20453.093| 368.616|  42,243|
| |Klickitat County|     3| 133.779|  0.000|   113|  5039.019| 44.593|  22,425|
| |Lewis County|     3| 37.171|  0.000|   220|  2725.910| 60.182|  80,707|
| |Walla Walla County|     3| 49.375|  0.000|   533|  8772.219| 265.682|  60,760|
| |Pacific County|     2| 89.004|  0.000|    51|  2269.592| 69.931|  22,471|
| |Grays Harbor County|     2| 26.645|  1.903|   120|  1598.700| 43.774|  75,061|
| |Asotin County|     2| 88.566|  0.000|    27|  1195.643| 18.978|  22,582|
| |Stevens County|     1| 21.871|  0.000|   110|  2405.791| 65.612|  45,723|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Skamania County|     1| 82.761|  0.000|    57|  4717.372| 47.292|  12,083|
| |Mason County|     1| 14.977|  0.000|   217|  3250.060| 128.376|  66,768|
| |Clallam County|     0|  0.000|  0.000|   120|  1551.771| 48.031|  77,331|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489| 74.922|   7,627|
| |Lincoln County|     0|  0.000|  0.000|    27|  2468.233| 182.832|  10,939|
| |Jefferson County|     0|  0.000|  0.000|    54|  1675.926|  4.434|  32,221|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753| 128.411|   2,225|
| |Pend Oreille County|     0|  0.000|  0.000|    41|  2987.467| 52.046|  13,724|
| |Whitman County|     0|  0.000|  0.000|   104|  2075.683| 45.619|  50,104|
| |San Juan County|     0|  0.000|  0.000|    28|  1592.538|  0.000|  17,582|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,657| 293.813| N/A|60,764| 10774.462| N/A|5,639,632|
| |Hennepin County|   835| 659.639|  1.806|19,271| 15223.847| 167.252|1,265,843|
| |Ramsey County|   265| 481.537|  1.038| 7,572| 13759.242| 184.568| 550,321|
| |Anoka County|   114| 319.398|  0.800| 3,683| 10318.810| 142.489| 356,921|
| |Dakota County|   106| 247.074|  1.332| 4,414| 10288.541| 157.168| 429,021|
| |Washington County|    45| 171.468|  1.089| 2,128|  8108.520| 131.731| 262,440|
| |Clay County|    40| 622.840|  0.000|   784| 12207.655| 91.202|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,732| 10941.735| 101.078| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,893| 17960.577| 67.404| 161,075|
| |Scott County|    19| 127.506|  4.793| 1,559| 10462.174| 188.862| 149,013|
| |St. Louis County|    19| 95.444|  0.000|   553|  2777.917| 90.420| 199,070|
| |Winona County|    16| 316.932|  0.000|   261|  5169.955| 45.276|  50,484|
| |Crow Wing County|    14| 215.203|  2.196|   235|  3612.328| 63.682|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   337|  9832.526| 125.043|  34,274|
| |Itasca County|    12| 265.899|  0.000|   147|  3257.257| 56.978|  45,130|
| |Pipestone County|     9| 986.193|  0.000|   157| 17203.594| 219.154|   9,126|
| |Goodhue County|     9| 194.217|  3.083|   196|  4229.607| 64.739|  46,340|
| |Sherburne County|     8| 82.272|  1.469|   723|  7435.365| 124.878|  97,238|
| |Rice County|     8| 119.453|  0.000| 1,032| 15409.425| 91.723|  66,972|
| |Nobles County|     6| 277.405|  0.000| 1,764| 81557.169| 125.493|  21,629|
| |Blue Earth County|     5| 73.907|  0.000|   918| 13569.243| 147.813|  67,653|
| |Martin County|     5| 254.026|  0.000|   207| 10516.690| 29.032|  19,683|
| |Wright County|     5| 36.133|  0.000|   884|  6388.345| 85.687| 138,377|
| |Renville County|     5| 343.690|  0.000|    64|  4399.230| 58.918|  14,548|
| |Polk County|     4| 127.535|  4.555|   153|  4878.204| 109.316|  31,364|
| |Benton County|     3| 73.369|  0.000|   320|  7826.066| 55.900|  40,889|
| |Carver County|     3| 28.547|  1.359|   861|  8193.055| 125.064| 105,089|
| |Grant County|     3| 502.344| 47.842|    55|  9209.645| 143.527|   5,972|
| |Koochiching County|     3| 245.319|  0.000|    77|  6296.508| 46.727|  12,229|
| |Lyon County|     3| 117.767|  0.000|   425| 16683.677| 56.080|  25,474|
| |Mille Lacs County|     3| 114.168|  0.000|    71|  2701.983| 38.056|  26,277|
| |Otter Tail County|     3| 51.067|  0.000|   194|  3302.353| 46.204|  58,746|
| |Wilkin County|     3| 483.325|  0.000|    34|  5477.686| 138.093|   6,207|
| |Brown County|     2| 79.974|  0.000|    89|  3558.861| 34.275|  25,008|
| |Cass County|     2| 67.161|  0.000|    72|  2417.811| 67.161|  29,779|
| |Meeker County|     2| 86.125|  0.000|    85|  3660.322| 12.304|  23,222|
| |Mower County|     2| 49.923|  0.000| 1,101| 27482.402| 82.016|  40,062|
| |Todd County|     2| 81.090|  0.000|   426| 17272.138| 46.337|  24,664|
| |Sibley County|     2| 134.544|  0.000|    83|  5583.586| 48.052|  14,865|
| |Steele County|     2| 54.572|  3.898|   348|  9495.484| 81.858|  36,649|
| |Kanabec County|     1| 61.211|  0.000|    36|  2203.587| 69.955|  16,337|
| |Chisago County|     1| 17.674|  0.000|   201|  3552.555| 63.123|  56,579|
| |Chippewa County|     1| 84.746|  0.000|   104|  8813.559| 84.746|  11,800|
| |Becker County|     1| 29.050|  0.000|   157|  4560.904| 62.251|  34,423|
| |Aitkin County|     1| 62.949|  8.993|    40|  2517.940| 107.912|  15,886|
| |Kandiyohi County|     1| 23.149|  0.000|   696| 16111.484| 85.981|  43,199|
| |Douglas County|     1| 26.219|  3.746|   144|  3775.465| 56.183|  38,141|
| |Freeborn County|     1| 33.024|  0.000|   359| 11855.619| 23.589|  30,281|
| |Swift County|     1| 107.921|  0.000|    53|  5719.836| 15.417|   9,266|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991| 50.590|  14,119|
| |Murray County|     1| 122.041|  0.000|   122| 14888.943|  0.000|   8,194|
| |Morrison County|     1| 29.953|  0.000|    92|  2755.646| 38.511|  33,386|
| |Mahnomen County|     1| 180.930|  0.000|    27|  4885.109| 103.389|   5,527|
| |Le Sueur County|     1| 34.618|  0.000|   220|  7615.883| 103.853|  28,887|
| |Lake County|     0|  0.000|  0.000|    21|  1973.499| 53.701|  10,641|
| |Lac qui Parle County|     0|  0.000|  0.000|     7|  1056.923| 21.570|   6,623|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Cottonwood County|     0|  0.000|  0.000|   178| 15898.535| 89.318|  11,196|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Carlton County|     0|  0.000|  0.000|   137|  3819.241| 51.773|  35,871|
| |Big Stone County|     0|  0.000|  0.000|    22|  4407.934|  0.000|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   240|  5086.039| 148.343|  47,188|
| |Cook County|     0|  0.000|  0.000|     5|   915.248| 78.450|   5,463|
| |Dodge County|     0|  0.000|  0.000|   127|  6066.686| 34.121|  20,934|
| |Jackson County|     0|  0.000|  0.000|    86|  8734.511| 232.146|   9,846|
| |Isanti County|     0|  0.000|  0.000|   125|  3079.121| 59.823|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    33|  1535.526| 33.237|  21,491|
| |Houston County|     0|  0.000|  0.000|    42|  2258.065| 15.361|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    63|  2990.459| 13.562|  21,067|
| |Faribault County|     0|  0.000|  0.000|    87|  6372.226| 52.317|  13,653|
| |Redwood County|     0|  0.000|  0.000|    36|  2373.105| 56.502|  15,170|
| |Red Lake County|     0|  0.000|  0.000|    24|  5918.619| 176.149|   4,055|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046| 114.296|  11,249|
| |Pine County|     0|  0.000|  0.000|   129|  4361.202| 14.489|  29,579|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510| 134.454|   6,375|
| |Marshall County|     0|  0.000|  0.000|    29|  3106.255| 15.302|   9,336|
| |McLeod County|     0|  0.000|  0.000|   181|  5042.766| 183.084|  35,893|
| |Lincoln County|     0|  0.000|  0.000|    58| 10285.512| 101.335|   5,639|
| |Lake of the Woods County|     0|  0.000|  0.000|     2|   534.759| 38.197|   3,740|
| |Waseca County|     0|  0.000|  0.000|   148|  7951.859| 153.511|  18,612|
| |Watonwan County|     0|  0.000|  0.000|   308| 28264.660| 131.098|  10,897|
| |Yellow Medicine County|     0|  0.000|  0.000|    52|  5355.855| 44.142|   9,709|
| |Wadena County|     0|  0.000|  0.000|    27|  1973.396| 41.765|  13,682|
| |Rock County|     0|  0.000|  0.000|    85|  9125.067| 184.035|   9,315|
| |Wabasha County|     0|  0.000|  0.000|    92|  4253.942| 92.477|  21,627|
| |Traverse County|     0|  0.000|  0.000|    11|  3375.268| 43.835|   3,259|
| |Stevens County|     0|  0.000|  0.000|    18|  1835.798| 43.709|   9,805|
| |Roseau County|     0|  0.000|  0.000|    52|  3428.948| 65.941|  15,165|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,271| 207.090| N/A|52,735|  8592.361| N/A|6,137,428|
| |St. Louis County|   841| 845.902|  3.161|19,985| 20101.488| 300.743| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 4,052| 10079.050| 177.318| 402,022|
| |Jackson County|    64| 91.037|  1.016| 4,014|  5709.726| 114.609| 703,011|
| |Jasper County|    31| 255.506|  7.065| 1,761| 14514.374| 128.342| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,593|  7077.452| 154.865| 225,081|
| |Clay County|    20| 80.017|  0.000| 1,037|  4148.863| 78.302| 249,948|
| |Franklin County|    18| 173.132|  0.000|   618|  5944.194| 136.032| 103,967|
| |Scott County|    13| 339.603|  0.000|   395| 10318.704| 186.595|  38,280|
| |Buchanan County|    10| 114.464|  0.000| 1,084| 12407.857| 45.785|  87,364|
| |Platte County|    10| 95.769|  0.000|   363|  3476.412| 69.775| 104,418|
| |Greene County|    10| 34.120|  0.000| 1,515|  5169.131| 143.790| 293,086|
| |Gentry County|     9| 1369.655|  0.000|    83| 12631.259| 86.962|   6,571|
| |Stoddard County|     9| 310.078|  0.000|   231|  7958.656| 103.359|  29,025|
| |Cass County|     9| 85.082|  0.000|   742|  7014.559| 143.154| 105,780|
| |Pemiscot County|     9| 569.440|  9.039|   234| 14805.441| 262.123|  15,805|
| |McDonald County|     7| 306.520|  0.000|   950| 41599.159| 150.132|  22,837|
| |Saline County|     7| 307.544|  0.000|   428| 18804.095| 112.975|  22,761|
| |Newton County|     6| 103.029|  0.000|   869| 14922.041| 166.809|  58,236|
| |Cape Girardeau County|     5| 63.395|  3.623|   651|  8253.984| 97.809|  78,871|
| |Camden County|     5| 107.980|  3.085|   350|  7558.579| 154.257|  46,305|
| |Barry County|     4| 111.766| 15.967|   254|  7097.153| 103.783|  35,789|
| |Dunklin County|     4| 137.311|  0.000|   310| 10641.585| 308.949|  29,131|
| |Pettis County|     4| 94.476|  3.374|   505| 11927.537| 320.542|  42,339|
| |Perry County|     4| 209.030|  0.000|   225| 11757.943| 141.842|  19,136|
| |Cole County|     3| 39.090|  1.861|   410|  5342.368| 176.838|  76,745|
| |Boone County|     3| 16.624|  0.000| 1,375|  7619.290| 124.283| 180,463|
| |Henry County|     3| 137.463|  0.000|    79|  3619.868| 65.459|  21,824|
| |Taney County|     3| 53.640|  0.000|   589| 10531.398| 411.243|  55,928|
| |St. Francois County|     2| 29.755|  0.000|   368|  5474.968| 146.651|  67,215|
| |Moniteau County|     2| 123.977|  0.000|   146|  9050.335| 203.677|  16,132|
| |Howell County|     2| 49.854|  0.000|   153|  3813.845| 56.976|  40,117|
| |Johnson County|     2| 36.995|  0.000|   487|  9008.176| 60.777|  54,062|
| |Lafayette County|     2| 61.147|  0.000|   178|  5442.094| 113.559|  32,708|
| |Douglas County|     2| 151.688|  0.000|    82|  6219.188| 97.513|  13,185|
| |Butler County|     2| 47.083|  0.000|   281|  6615.189| 141.250|  42,478|
| |Ray County|     2| 86.889| 12.413|   116|  5039.534| 161.364|  23,018|
| |Lawrence County|     2| 52.144|  0.000|   228|  5944.466| 156.433|  38,355|
| |Putnam County|     1| 212.947|  0.000|    13|  2768.313| 91.263|   4,696|
| |Pike County|     1| 54.639|  0.000|    99|  5409.245| 234.166|  18,302|
| |Osage County|     1| 73.448| 10.493|    48|  3525.523| 94.434|  13,615|
| |New Madrid County|     1| 58.562|  0.000|   250| 14640.431| 552.153|  17,076|
| |Randolph County|     1| 40.407|  0.000|    69|  2788.104| 80.815|  24,748|
| |Webster County|     1| 25.258|  0.000|   135|  3409.780| 68.556|  39,592|
| |Scotland County|     1| 203.998|  0.000|    15|  3059.976| 87.428|   4,902|
| |Washington County|     1| 40.437|  0.000|    77|  3113.627| 121.310|  24,730|
| |Stone County|     1| 31.297|  0.000|   129|  4037.306| 192.253|  31,952|
| |Miller County|     1| 39.034|  5.576|   127|  4957.258| 172.863|  25,619|
| |Ste. Genevieve County|     1| 55.885|  0.000|    56|  3129.541| 95.802|  17,894|
| |Pulaski County|     1| 19.009|  0.000|   224|  4257.988| 119.484|  52,607|
| |Linn County|     1| 83.893|  0.000|    32|  2684.564| 11.985|  11,920|
| |Lincoln County|     1| 16.945|  0.000|   374|  6337.587| 176.717|  59,013|
| |Lewis County|     1| 102.291|  0.000|    46|  4705.401| 189.970|   9,776|
| |Grundy County|     1| 101.523|  0.000|    27|  2741.117| 43.510|   9,850|
| |Laclede County|     1| 27.993|  0.000|   200|  5598.634| 11.997|  35,723|
| |Audrain County|     1| 39.389|  0.000|   200|  7877.738| 39.389|  25,388|
| |Carter County|     1| 167.168|  0.000|    20|  3343.363|  0.000|   5,982|
| |Callaway County|     1| 22.350|  0.000|   157|  3508.929| 102.171|  44,743|
| |Christian County|     1| 11.287|  0.000|   351|  3961.849| 112.873|  88,595|
| |Benton County|     1| 51.432|  0.000|    94|  4834.645| 168.992|  19,443|
| |Harrison County|     1| 119.732|  0.000|    60|  7183.908|  0.000|   8,352|
| |Marion County|     1| 35.051|  0.000|   193|  6764.809| 215.312|  28,530|
| |Caldwell County|     1| 110.865|  0.000|    35|  3880.266| 79.189|   9,020|
| |Shannon County|     1| 122.459|  0.000|    43|  5265.736|  0.000|   8,166|
| |Bollinger County|     1| 82.420| 11.774|    68|  5604.550| 141.291|  12,133|
| |DeKalb County|     1| 79.700|  0.000|    35|  2789.511| 34.157|  12,547|
| |Bates County|     1| 61.835|  0.000|    47|  2906.258| 70.669|  16,172|
| |Dallas County|     1| 59.249|  0.000|    67|  3969.665| 152.354|  16,878|
| |Andrew County|     1| 56.459|  0.000|    87|  4911.924| 24.197|  17,712|
| |Daviess County|     0|  0.000|  0.000|    17|  2053.636|  0.000|   8,278|
| |Dade County|     0|  0.000|  0.000|    15|  1983.865|  0.000|   7,561|
| |Crawford County|     0|  0.000|  0.000|    73|  3051.839| 101.529|  23,920|
| |Cooper County|     0|  0.000|  0.000|   125|  7058.558| 250.075|  17,709|
| |Clinton County|     0|  0.000|  0.000|    82|  4022.171| 147.153|  20,387|
| |Clark County|     0|  0.000|  0.000|    20|  2942.475| 126.106|   6,797|
| |Chariton County|     0|  0.000|  0.000|    17|  2289.254| 57.712|   7,426|
| |Cedar County|     0|  0.000|  0.000|    40|  2787.651| 59.735|  14,349|
| |Carroll County|     0|  0.000|  0.000|   101| 11637.285| 49.380|   8,679|
| |Barton County|     0|  0.000|  0.000|    68|  5785.265| 36.462|  11,754|
| |Atchison County|     0|  0.000|  0.000|    18|  3499.903| 166.662|   5,143|
| |Adair County|     0|  0.000|  0.000|   159|  6273.922| 140.924|  25,343|
| |Gasconade County|     0|  0.000|  0.000|    24|  1631.987| 38.857|  14,706|
| |Dent County|     0|  0.000|  0.000|    11|   706.351| 18.347|  15,573|
| |Hickory County|     0|  0.000|  0.000|    31|  3248.114| 209.556|   9,544|
| |Holt County|     0|  0.000|  0.000|     8|  1816.943| 64.891|   4,403|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Wright County|     0|  0.000|  0.000|    62|  3390.016| 31.244|  18,289|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939| 70.967|   2,013|
| |Wayne County|     0|  0.000|  0.000|    55|  4272.508| 221.948|  12,873|
| |Warren County|     0|  0.000|  0.000|   196|  5498.050| 140.256|  35,649|
| |Vernon County|     0|  0.000|  0.000|    53|  2577.445| 55.578|  20,563|
| |Texas County|     0|  0.000|  0.000|    52|  2047.405| 89.996|  25,398|
| |Sullivan County|     0|  0.000|  0.000|   144| 23649.203| 211.154|   6,089|
| |Mercer County|     0|  0.000|  0.000|    11|  3041.194| 78.992|   3,617|
| |Mississippi County|     0|  0.000|  0.000|   135| 10242.792| 54.195|  13,180|
| |St. Clair County|     0|  0.000|  0.000|    19|  2021.922| 15.202|   9,397|
| |Ripley County|     0|  0.000|  0.000|    52|  3913.305| 129.010|  13,288|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    32|  3104.084| 152.433|  10,309|
| |Polk County|     0|  0.000|  0.000|   208|  6469.875| 75.541|  32,149|
| |Phelps County|     0|  0.000|  0.000|    88|  1974.289| 41.665|  44,573|
| |Ozark County|     0|  0.000|  0.000|    12|  1308.044| 77.860|   9,174|
| |Oregon County|     0|  0.000|  0.000|    16|  1519.612| 27.136|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   179|  8102.481| 142.262|  22,092|
| |Morgan County|     0|  0.000|  0.000|    81|  3926.892| 96.960|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    41|  3549.476| 61.838|  11,551|
| |Monroe County|     0|  0.000|  0.000|    29|  3354.928| 198.321|   8,644|
| |Knox County|     0|  0.000|  0.000|    27|  6819.904| 433.010|   3,959|
| |Iron County|     0|  0.000|  0.000|    22|  2172.840| 84.656|  10,125|
| |Howard County|     0|  0.000|  0.000|    52|  5199.480| 85.706|  10,001|
| |Livingston County|     0|  0.000|  0.000|    61|  4006.042| 75.055|  15,227|
| |Shelby County|     0|  0.000|  0.000|    38|  6408.094| 240.906|   5,930|
| |Maries County|     0|  0.000|  0.000|    23|  2644.590| 147.834|   8,697|
| |Madison County|     0|  0.000|  0.000|    25|  2068.167| 94.545|  12,088|
| |Macon County|     0|  0.000|  0.000|    58|  3836.740| 47.250|  15,117|
| |Schuyler County|     0|  0.000|  0.000|    11|  2360.515| 61.312|   4,660|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,199| 175.570| N/A|116,627| 17077.761| N/A|6,829,174|
| |Shelby County|   304| 324.382|  2.896|23,238| 24796.034| 296.029| 937,166|
| |Davidson County|   213| 306.853|  2.881|20,620| 29705.652| 267.544| 694,144|
| |Sumner County|    73| 381.633|  2.987| 3,433| 17947.230| 203.886| 191,283|
| |Rutherford County|    54| 162.511|  1.290| 6,553| 19721.023| 219.691| 332,285|
| |Hamilton County|    53| 144.098|  2.330| 6,132| 16671.923| 198.475| 367,804|
| |Knox County|    39| 82.923|  1.519| 4,600|  9780.720| 204.727| 470,313|
| |Williamson County|    25| 104.860|  1.798| 3,551| 14894.385| 192.344| 238,412|
| |Wilson County|    23| 158.997|  2.963| 2,290| 15830.551| 223.188| 144,657|
| |McMinn County|    20| 371.789|  0.000|   547| 10168.420| 180.583|  53,794|
| |Robertson County|    19| 264.576|  5.968| 1,558| 21695.236| 250.651|  71,813|
| |Putnam County|    18| 224.313|  8.901| 1,767| 22020.064| 391.658|  80,245|
| |Hardeman County|    17| 678.643| 34.217|   917| 36606.786| 701.454|  25,050|
| |Madison County|    17| 173.498|  7.290| 1,102| 11246.734| 310.546|  97,984|
| |Sullivan County|    14| 88.413|  4.511|   994|  6277.313| 193.065| 158,348|
| |Hamblen County|    14| 215.604|  2.200| 1,396| 21498.753| 393.806|  64,934|
| |Giles County|    13| 441.216| 19.394|   381| 12931.034| 179.396|  29,464|
| |Macon County|    13| 528.412|  0.000|   860| 34956.508| 150.975|  24,602|
| |Montgomery County|    13| 62.203|  1.367| 1,939|  9277.823| 155.849| 208,993|
| |Bradley County|    12| 110.998|  2.643| 1,943| 17972.435| 314.494| 108,110|
| |Bedford County|    11| 221.270|  2.874|   928| 18667.149| 189.660|  49,713|
| |Blount County|    11| 82.652|  4.294| 1,303|  9790.515| 220.048| 133,088|
| |Tipton County|    10| 162.340|  2.319| 1,208| 19610.708| 241.191|  61,599|
| |Monroe County|     9| 193.361|  0.000|   444|  9539.156| 270.092|  46,545|
| |Lauderdale County|     8| 312.098| 11.146|   508| 19818.203| 484.866|  25,633|
| |Greene County|     8| 115.826|  6.205|   492|  7123.311| 254.404|  69,069|
| |Fayette County|     8| 194.491|  0.000|   698| 16969.343| 281.317|  41,133|
| |Hardin County|     8| 311.867|  5.569|   471| 18361.141| 406.540|  25,652|
| |Dyer County|     8| 215.291|  3.844|   650| 17492.398| 415.204|  37,159|
| |Cheatham County|     7| 172.130|  7.026|   595| 14631.028| 179.155|  40,667|
| |Sevier County|     7| 71.247|  2.908| 1,886| 19195.929| 267.539|  98,250|
| |Maury County|     7| 72.624|  2.964| 1,257| 13041.178| 283.085|  96,387|
| |Hawkins County|     7| 123.270|  7.547|   472|  8311.908| 372.325|  56,786|
| |Trousdale County|     6| 531.726|  0.000| 1,583| 140287.132| 139.262|  11,284|
| |Lawrence County|     6| 135.925|  0.000|   562| 12731.639| 284.795|  44,142|
| |Carter County|     6| 106.400|  2.533|   522|  9256.796| 248.267|  56,391|
| |Haywood County|     6| 346.741|  8.256|   500| 28895.053| 1081.501|  17,304|
| |Cumberland County|     6| 99.141|  0.000|   457|  7551.223| 193.561|  60,520|
| |Anderson County|     6| 77.944|  1.856|   684|  8885.656| 157.745|  76,978|
| |Crockett County|     5| 351.370| 20.078|   269| 18903.725| 461.801|  14,230|
| |Gibson County|     5| 101.765|  8.723|   717| 14593.043| 462.302|  49,133|
| |White County|     5| 182.849| 10.449|   293| 10714.939| 532.874|  27,345|
| |McNairy County|     5| 194.598|  0.000|   378| 14711.606| 378.076|  25,694|
| |Franklin County|     4| 94.769|  0.000|   330|  7818.423| 152.307|  42,208|
| |Jefferson County|     4| 73.401|  5.243|   568| 10422.975| 207.096|  54,495|
| |Smith County|     4| 198.442|  7.087|   452| 22423.972| 644.937|  20,157|
| |Obion County|     4| 133.027|  0.000|   565| 18790.116| 655.635|  30,069|
| |Marion County|     4| 138.375|  0.000|   224|  7748.988| 88.955|  28,907|
| |Weakley County|     4| 120.019|  4.286|   451| 13532.165| 818.702|  33,328|
| |Warren County|     4| 96.906|  0.000|   530| 12840.080| 449.922|  41,277|
| |Decatur County|     3| 257.224| 24.497|   213| 18262.883| 661.432|  11,663|
| |Coffee County|     3| 53.079|  2.528|   545|  9642.604| 338.692|  56,520|
| |Carroll County|     3| 108.042|  0.000|   314| 11308.388| 452.747|  27,767|
| |Humphreys County|     3| 161.447|  0.000|   124|  6673.125| 176.822|  18,582|
| |Loudon County|     3| 55.486|  0.000|   742| 13723.459| 245.722|  54,068|
| |Polk County|     3| 178.232| 16.974|   206| 12238.593| 339.489|  16,832|
| |Marshall County|     3| 87.273|  4.156|   301|  8756.364| 157.922|  34,375|
| |Cocke County|     2| 55.549|  3.968|   475| 13192.979| 333.296|  36,004|
| |DeKalb County|     2| 97.609|  6.972|   360| 17569.546| 390.434|  20,490|
| |Chester County|     2| 115.627|  8.259|   221| 12776.782| 239.513|  17,297|
| |Grundy County|     2| 148.954|  0.000|   114|  8490.355| 138.314|  13,427|
| |Dickson County|     2| 37.073|  2.648|   691| 12808.631| 275.397|  53,948|
| |Rhea County|     2| 60.301|  4.307|   536| 16160.642| 167.981|  33,167|
| |Henderson County|     2| 71.131| 10.162|   593| 21090.444| 848.495|  28,117|
| |Hancock County|     2| 302.115| 21.580|    80| 12084.592| 129.478|   6,620|
| |Washington County|     2| 15.459|  0.000| 1,252|  9677.295| 236.301| 129,375|
| |Wayne County|     2| 119.954|  8.568|   226| 13554.849| 102.818|  16,673|
| |Roane County|     2| 37.466|  2.676|   475|  8898.130| 318.459|  53,382|
| |Bledsoe County|     1| 66.383|  0.000|   705| 46800.319| 350.884|  15,064|
| |Benton County|     1| 61.881|  0.000|   155|  9591.584| 556.931|  16,160|
| |Campbell County|     1| 25.099|  0.000|   248|  6224.587| 147.009|  39,842|
| |Jackson County|     1| 84.846|  0.000|   127| 10775.496| 242.418|  11,786|
| |Overton County|     1| 44.962|  0.000|   195|  8767.591| 391.812|  22,241|
| |Lewis County|     1| 81.513|  0.000|    75|  6113.466| 221.249|  12,268|
| |Lincoln County|     1| 29.099|  0.000|   302|  8787.755| 212.004|  34,366|
| |Morgan County|     1| 46.722|  0.000|   122|  5700.135| 287.009|  21,403|
| |Pickett County|     1| 198.098|  0.000|    35|  6933.439| 367.897|   5,048|
| |Lake County|     0|  0.000|  0.000|   787| 112172.178| 875.550|   7,016|
| |Perry County|     0|  0.000|  0.000|    81| 10029.718| 123.824|   8,076|
| |Fentress County|     0|  0.000|  0.000|    93|  5020.785| 146.536|  18,523|
| |Moore County|     0|  0.000|  0.000|    63|  9710.234| 462.392|   6,488|
| |Grainger County|     0|  0.000|  0.000|   197|  8447.684| 177.653|  23,320|
| |Meigs County|     0|  0.000|  0.000|   106|  8533.247| 115.003|  12,422|
| |Henry County|     0|  0.000|  0.000|   288|  8904.004| 340.083|  32,345|
| |Hickman County|     0|  0.000|  0.000|   268| 10644.213| 238.303|  25,178|
| |Houston County|     0|  0.000|  0.000|    59|  7194.245| 69.678|   8,201|
| |Johnson County|     0|  0.000|  0.000|   280| 15740.949| 963.732|  17,788|
| |Cannon County|     0|  0.000|  0.000|   147| 10014.988| 291.982|  14,678|
| |Scott County|     0|  0.000|  0.000|   119|  5392.423| 116.523|  22,068|
| |Sequatchie County|     0|  0.000|  0.000|   105|  6987.888| 104.581|  15,026|
| |Claiborne County|     0|  0.000|  0.000|   272|  8510.905| 268.201|  31,959|
| |Clay County|     0|  0.000|  0.000|    76|  9980.302| 262.640|   7,615|
| |Stewart County|     0|  0.000|  0.000|    74|  5395.552| 41.664|  13,715|
| |Unicoi County|     0|  0.000|  0.000|   166|  9282.559| 239.653|  17,883|
| |Union County|     0|  0.000|  0.000|   160|  8011.216| 300.421|  19,972|
| |Van Buren County|     0|  0.000|  0.000|    36|  6130.790| 97.314|   5,872|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   998| 171.406| N/A|60,554| 10400.118| N/A|5,822,434|
| |Milwaukee County|   456| 482.169|  1.511|21,062| 22270.721| 201.659| 945,726|
| |Racine County|    78| 397.329|  1.455| 3,514| 17900.169| 195.754| 196,311|
| |Kenosha County|    60| 353.855|  5.898| 2,667| 15728.853| 162.605| 169,561|
| |Waukesha County|    58| 143.494|  1.060| 4,234| 10475.064| 201.811| 404,198|
| |Brown County|    54| 204.126|  1.620| 4,264| 16118.424| 138.244| 264,542|
| |Dane County|    39| 71.338|  0.523| 4,536|  8297.131| 88.323| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,432|  8766.238| 57.719| 163,354|
| |Walworth County|    23| 221.435|  2.751| 1,335| 12852.852| 134.786| 103,868|
| |Washington County|    22| 161.724|  0.000| 1,066|  7836.276| 195.329| 136,034|
| |Winnebago County|    18| 104.708|  0.831| 1,176|  6840.908| 100.553| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   692|  7756.022| 198.544|  89,221|
| |Grant County|    15| 291.608|  2.777|   356|  6920.819| 77.762|  51,439|
| |Waupaca County|    15| 294.175|  0.000|   453|  8884.095| 232.539|  50,990|
| |Outagamie County|    14| 74.514|  0.760| 1,252|  6663.651| 114.052| 187,885|
| |Sheboygan County|     9| 78.030|  4.954|   746|  6467.834| 169.685| 115,340|
| |Marathon County|     9| 66.327|  3.158|   646|  4760.782| 71.591| 135,692|
| |Fond du Lac County|     7| 67.696|  1.382|   657|  6353.781| 134.011| 103,403|
| |Clark County|     7| 201.300|  0.000|   184|  5291.310| 41.082|  34,774|
| |St. Croix County|     5| 55.135|  4.726|   493|  5436.281| 72.463|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   631|  7443.759| 126.394|  84,769|
| |Dodge County|     5| 56.922|  0.000|   819|  9323.877| 190.283|  87,839|
| |Richland County|     4| 231.857|  0.000|    37|  2144.679| 41.403|  17,252|
| |Eau Claire County|     4| 38.224|  1.365|   588|  5618.944| 116.037| 104,646|
| |Forest County|     4| 444.247|  0.000|    59|  6552.643|  0.000|   9,004|
| |Marinette County|     3| 74.349|  0.000|   395|  9789.343| 283.236|  40,350|
| |Sauk County|     3| 46.553|  0.000|   444|  6889.917| 128.576|  64,442|
| |Door County|     3| 108.429|  0.000|   106|  3831.141| 108.429|  27,668|
| |Barron County|     3| 66.307|  0.000|   293|  6475.997| 119.984|  45,244|
| |Trempealeau County|     2| 67.456|  0.000|   336| 11332.591| 139.730|  29,649|
| |Calumet County|     2| 39.929|  0.000|   320|  6388.628| 182.532|  50,089|
| |Buffalo County|     2| 153.480|  0.000|    43|  3299.823| 21.926|  13,031|
| |Polk County|     2| 45.680|  0.000|   132|  3014.869| 39.154|  43,783|
| |Pierce County|     2| 46.779|  6.683|   222|  5192.497| 173.751|  42,754|
| |Monroe County|     2| 43.240|  3.089|   243|  5253.713| 64.861|  46,253|
| |Kewaunee County|     2| 97.876|  0.000|   131|  6410.884| 146.814|  20,434|
| |Adams County|     2| 98.912|  0.000|    85|  4203.759| 84.782|  20,220|
| |Waushara County|     1| 40.912|  5.845|   116|  4745.735| 58.445|  24,443|
| |Wood County|     1| 13.699|  0.000|   291|  3986.356| 103.720|  72,999|
| |Burnett County|     1| 64.876|  0.000|    22|  1427.274| 74.144|  15,414|
| |Columbia County|     1| 17.382|  0.000|   248|  4310.645| 59.594|  57,532|
| |Taylor County|     1| 49.157|  7.022|    69|  3391.830| 119.381|  20,343|
| |Iron County|     1| 175.840|  0.000|    75| 13187.973| 75.360|   5,687|
| |Jackson County|     1| 48.443|  0.000|    58|  2809.669| 69.204|  20,643|
| |Juneau County|     1| 37.471|  0.000|   137|  5133.586| 42.824|  26,687|
| |La Crosse County|     1|  8.473|  0.000|   908|  7693.872| 105.313| 118,016|
| |Langlade County|     1| 52.113|  0.000|    65|  3387.357| 126.561|  19,189|
| |Rusk County|     1| 70.532|  0.000|    20|  1410.636| 40.304|  14,178|
| |Manitowoc County|     1| 12.661|  0.000|   337|  4266.849| 65.115|  78,981|
| |Ashland County|     1| 64.259|  9.180|    25|  1606.477| 45.899|  15,562|
| |Bayfield County|     1| 66.507|  0.000|    27|  1795.690| 66.507|  15,036|
| |Green County|     1| 27.056|  0.000|   162|  4383.117| 123.686|  36,960|
| |Marquette County|     1| 64.210|  0.000|    80|  5136.766| 82.555|  15,574|
| |Oneida County|     0|  0.000|  0.000|   131|  3680.292| 172.576|  35,595|
| |Iowa County|     0|  0.000|  0.000|    80|  3378.664| 102.567|  23,678|
| |Oconto County|     0|  0.000|  0.000|   248|  6538.360| 244.812|  37,930|
| |Price County|     0|  0.000|  0.000|    32|  2396.824| 107.001|  13,351|
| |Portage County|     0|  0.000|  0.000|   411|  5807.381| 115.058|  70,772|
| |Pepin County|     0|  0.000|  0.000|    42|  5763.689| 39.209|   7,287|
| |Lafayette County|     0|  0.000|  0.000|   139|  8340.834| 265.741|  16,665|
| |Chippewa County|     0|  0.000|  0.000|   230|  3557.178| 46.398|  64,658|
| |Crawford County|     0|  0.000|  0.000|    75|  4649.433| 115.129|  16,131|
| |Florence County|     0|  0.000|  0.000|     8|  1862.631| 33.261|   4,295|
| |Dunn County|     0|  0.000|  0.000|   123|  2711.162| 56.679|  45,368|
| |Douglas County|     0|  0.000|  0.000|   173|  4009.270| 132.428|  43,150|
| |Menominee County|     0|  0.000|  0.000|    22|  4828.797| 94.067|   4,556|
| |Lincoln County|     0|  0.000|  0.000|    68|  2464.393| 25.886|  27,593|
| |Shawano County|     0|  0.000|  0.000|   196|  4792.293| 132.731|  40,899|
| |Washburn County|     0|  0.000|  0.000|    47|  2989.822| 118.139|  15,720|
| |Vilas County|     0|  0.000|  0.000|    53|  2387.925| 96.547|  22,195|
| |Vernon County|     0|  0.000|  0.000|    64|  2076.439| 27.809|  30,822|
| |Sawyer County|     0|  0.000|  0.000|    67|  4046.382| 258.830|  16,558|
| |Green Lake County|     0|  0.000|  0.000|    56|  2960.926| 30.214|  18,913|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   949| 308.101| N/A|55,878| 18141.289| N/A|3,080,156|
| |Clark County|   807| 356.022|  7.500|48,466| 21381.603| 335.224|2,266,715|
| |Washoe County|   118| 250.255|  1.212| 5,756| 12207.355| 140.276| 471,519|
| |Nye County|     9| 193.453|  0.000|   408|  8769.856| 175.029|  46,523|
| |Lyon County|     6| 104.330|  2.484|   224|  3894.975| 49.681|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074| 67.902|  16,831|
| |Elko County|     2| 37.895|  0.000|   544| 10307.325| 167.819|  52,778|
| |Churchill County|     1| 40.146|  0.000|    69|  2770.083| 126.174|  24,909|
| |White Pine County|     1| 104.384|  0.000|    16|  1670.146| 29.824|   9,580|
| |Lander County|     1| 180.766|  0.000|    51|  9219.089| 25.824|   5,532|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784| 21.243|   6,725|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|
| |Storey County|     0|  0.000|  0.000|     4|   970.167|  0.000|   4,123|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692| 27.563|   5,183|
| |Eureka County|     0|  0.000|  0.000|     3|  1478.561| 70.408|   2,029|
| |Douglas County|     0|  0.000|  0.000|   203|  4150.905| 84.712|  48,905|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   931| 295.081| N/A|48,913| 15502.984| N/A|3,155,070|
| |Polk County|   207| 422.310|  1.457|10,309| 21031.865| 174.870| 490,161|
| |Linn County|    88| 388.168|  0.630| 2,375| 10476.123| 180.221| 226,706|
| |Black Hawk County|    66| 502.941|  4.354| 3,127| 23828.756| 141.520| 131,228|
| |Woodbury County|    52| 504.330|  2.771| 3,719| 36069.326| 106.685| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   847| 19852.803| 77.014|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,885| 20170.567| 149.808|  93,453|
| |Wapello County|    33| 943.693|  8.171|   900| 25737.081| 224.689|  34,969|
| |Dubuque County|    31| 318.566|  2.936| 1,676| 17223.130| 218.739|  97,311|
| |Tama County|    29| 1720.660|  0.000|   551| 32692.536| 118.666|  16,854|
| |Pottawattamie County|    26| 278.952|  4.598| 1,325| 14215.823| 173.195|  93,206|
| |Jasper County|    26| 699.207|  7.684|   478| 12854.646| 92.203|  37,185|
| |Marshall County|    26| 660.418|  7.257| 1,444| 36678.605| 221.349|  39,369|
| |Johnson County|    19| 125.711|  3.781| 2,096| 13867.937| 168.245| 151,140|
| |Cerro Gordo County|    17| 400.471|  0.000|   625| 14723.204| 148.073|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   139|  6291.016| 19.397|  22,095|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Scott County|    14| 80.952|  1.652| 1,718|  9933.909| 105.733| 172,943|
| |Story County|    14| 144.156|  1.471| 1,166| 12006.137| 82.375|  97,117|
| |Buena Vista County|    12| 611.621|  0.000| 1,794| 91437.309| 72.812|  19,620|
| |Washington County|    10| 455.270|  0.000|   298| 13567.038| 71.542|  21,965|
| |Franklin County|    10| 993.049| 85.118|   241| 23932.473| 397.219|  10,070|
| |Plymouth County|     9| 357.469|  5.674|   462| 18350.081| 107.808|  25,177|
| |Poweshiek County|     8| 432.339|  0.000|   159|  8592.737| 100.364|  18,504|
| |Monroe County|     7| 908.265|  0.000|    73|  9471.909| 129.752|   7,707|
| |Bremer County|     7| 279.307|  0.000|   226|  9017.636| 222.306|  25,062|
| |Webster County|     7| 194.964|  7.958|   801| 22309.492| 354.119|  35,904|
| |Guthrie County|     5| 467.771|  0.000|   132| 12349.144| 80.189|  10,689|
| |Allamakee County|     4| 292.248|  0.000|   155| 11324.615| 62.625|  13,687|
| |Emmet County|     4| 434.405| 46.543|   192| 20851.434| 201.688|   9,208|
| |Dickinson County|     4| 231.777|  0.000|   381| 22076.718| 49.666|  17,258|
| |Lucas County|     4| 465.116|  0.000|    68|  7906.977| 415.282|   8,600|
| |Montgomery County|     4| 403.348| 14.405|    59|  5949.380| 230.484|   9,917|
| |Henry County|     4| 200.461|  7.159|   125|  6264.408| 93.071|  19,954|
| |Sioux County|     3| 86.071|  4.099|   634| 18189.643| 168.043|  34,855|
| |Clayton County|     3| 170.950|  0.000|   104|  5926.264| 56.983|  17,549|
| |Clinton County|     3| 64.615|  0.000|   397|  8550.690| 261.536|  46,429|
| |Crawford County|     3| 178.359|  0.000|   728| 43281.807| 110.413|  16,820|
| |Clarke County|     3| 319.319|  0.000|   201| 21394.359| 243.291|   9,395|
| |Lee County|     3| 89.135|  0.000|   114|  3387.111| 93.379|  33,657|
| |Appanoose County|     3| 241.429|  0.000|    49|  3943.345| 68.980|  12,426|
| |Boone County|     3| 114.355|  5.445|   258|  9834.566| 163.365|  26,234|
| |Lyon County|     2| 170.140| 24.306|   113|  9612.931| 157.987|  11,755|
| |Jones County|     2| 96.707|  6.908|   130|  6285.963| 48.354|  20,681|
| |Butler County|     2| 138.514|  0.000|   121|  8380.082| 79.151|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    83|  8585.023| 29.553|   9,668|
| |Madison County|     2| 122.414|  0.000|   121|  7406.047| 183.621|  16,338|
| |Davis County|     2| 222.222| 15.873|    57|  6333.333| 126.984|   9,000|
| |Floyd County|     2| 127.861|  0.000|   155|  9909.219| 283.121|  15,642|
| |O'Brien County|     2| 145.423| 10.387|   138| 10034.174| 72.711|  13,753|
| |Des Moines County|     2| 51.325|  0.000|   179|  4593.631| 146.644|  38,967|
| |Hancock County|     2| 188.147|  0.000|   122| 11476.952| 80.634|  10,630|
| |Pocahontas County|     2| 302.160| 21.583|   115| 17374.226| 43.166|   6,619|
| |Keokuk County|     1| 97.599|  0.000|    35|  3415.967| 69.714|  10,246|
| |Audubon County|     1| 181.951|  0.000|    28|  5094.614|  0.000|   5,496|
| |Benton County|     1| 38.994|  0.000|   156|  6083.057| 77.988|  25,645|
| |Cass County|     1| 77.906|  0.000|    74|  5765.036| 300.494|  12,836|
| |Cedar County|     1| 53.686|  0.000|   133|  7140.173| 99.702|  18,627|
| |Cherokee County|     1| 89.008|  0.000|   108|  9612.817| 139.869|  11,235|
| |Clay County|     1| 62.438|  0.000|   190| 11863.137| 169.473|  16,016|
| |Buchanan County|     1| 47.226|  0.000|   127|  5997.639| 114.691|  21,175|
| |Carroll County|     1| 49.591|  0.000|   192|  9521.448| 77.929|  20,165|
| |Warren County|     1| 19.430|  0.000|   564| 10958.691| 105.479|  51,466|
| |Wayne County|     1| 155.255|  0.000|    19|  2949.853| 88.717|   6,441|
| |Delaware County|     1| 58.785|  0.000|   112|  6583.975| 184.754|  17,011|
| |Winneshiek County|     1| 50.023|  0.000|    97|  4852.183| 107.191|  19,991|
| |Wright County|     1| 79.605|  0.000|   472| 37573.635| 352.537|  12,562|
| |Van Buren County|     1| 141.965|  0.000|    37|  5252.697| 121.684|   7,044|
| |Union County|     1| 81.693|  0.000|    77|  6290.336| 81.693|  12,241|
| |Grundy County|     1| 81.753|  0.000|    79|  6458.470| 81.753|  12,232|
| |Shelby County|     1| 87.306|  0.000|   184| 16064.257| 311.806|  11,454|
| |Hamilton County|     1| 67.691|  0.000|   246| 16652.000| 67.691|  14,773|
| |Ringgold County|     1| 204.332|  0.000|    22|  4495.300| 29.190|   4,894|
| |Harrison County|     1| 71.179| 10.168|   107|  7616.200| 111.853|  14,049|
| |Humboldt County|     1| 104.624|  0.000|   111| 11613.308| 328.820|   9,558|
| |Iowa County|     1| 61.789|  0.000|    97|  5993.574| 79.444|  16,184|
| |Jackson County|     1| 51.443|  0.000|   156|  8025.104| 124.933|  19,439|
| |Worth County|     0|  0.000|  0.000|    66|  8941.878| 96.774|   7,381|
| |Winnebago County|     0|  0.000|  0.000|    84|  8112.807| 151.770|  10,354|
| |Taylor County|     0|  0.000|  0.000|    98| 16010.456| 116.694|   6,121|
| |Sac County|     0|  0.000|  0.000|    85|  8743.956| 58.783|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|    84|  9453.072| 96.460|   8,886|
| |Page County|     0|  0.000|  0.000|    94|  6222.281| 189.127|  15,107|
| |Osceola County|     0|  0.000|  0.000|    83| 13930.849| 143.864|   5,958|
| |Monona County|     0|  0.000|  0.000|    91| 10562.972| 16.582|   8,615|
| |Mitchell County|     0|  0.000|  0.000|    78|  7368.222| 26.990|  10,586|
| |Mills County|     0|  0.000|  0.000|    89|  5890.529| 75.641|  15,109|
| |Marion County|     0|  0.000|  0.000|   173|  5202.538| 90.217|  33,253|
| |Adams County|     0|  0.000|  0.000|    16|  4441.977|  0.000|   3,602|
| |Adair County|     0|  0.000|  0.000|    30|  4194.631| 199.744|   7,152|
| |Fremont County|     0|  0.000|  0.000|    42|  6034.483| 123.153|   6,960|
| |Fayette County|     0|  0.000|  0.000|    82|  4173.028| 21.810|  19,650|
| |Hardin County|     0|  0.000|  0.000|   181| 10744.390| 127.203|  16,846|
| |Howard County|     0|  0.000|  0.000|    49|  5350.513| 15.599|   9,158|
| |Ida County|     0|  0.000|  0.000|    29|  4227.405|  0.000|   6,860|
| |Decatur County|     0|  0.000|  0.000|    23|  2922.490| 36.304|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    54|  4525.266| 47.886|  11,933|
| |Greene County|     0|  0.000|  0.000|    41|  4612.961| 48.219|   8,888|
| |Jefferson County|     0|  0.000|  0.000|    84|  4591.418| 46.851|  18,295|
| |Kossuth County|     0|  0.000|  0.000|    91|  6143.253| 135.017|  14,813|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   773| 173.021| N/A|34,982|  7830.027| N/A|4,467,673|
| |Jefferson County|   237| 309.094|  0.745| 8,084| 10543.106| 177.557| 766,757|
| |Fayette County|    47| 145.442|  0.442| 3,120|  9654.899| 151.631| 323,152|
| |Kenton County|    41| 245.512|  3.422| 1,410|  8443.215| 79.556| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   421|  9421.295| 57.544|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,104|  8264.648| 91.972| 133,581|
| |Graves County|    24| 644.019|  7.667|   558| 14973.434| 191.672|  37,266|
| |Logan County|    23| 848.646|  5.271|   328| 12102.428| 142.319|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,630| 19789.911| 218.216| 132,896|
| |Shelby County|    21| 428.362|  0.000|   773| 15767.787| 189.412|  49,024|
| |Adair County|    19| 989.480|  0.000|   201| 10467.660|  0.000|  19,202|
| |Butler County|    15| 1164.687|  0.000|   293| 22750.214| 11.092|  12,879|
| |Oldham County|    15| 224.554|  2.139|   632|  9461.219| 164.673|  66,799|
| |Jackson County|    14| 1050.341|  0.000|   150| 11253.657| 85.742|  13,329|
| |Campbell County|    13| 138.913|  0.000|   569|  6080.099| 70.220|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   106|  8724.280| 152.851|  12,150|
| |Grayson County|    11| 416.241|  0.000|   201|  7605.858| 118.926|  26,427|
| |Muhlenberg County|    11| 359.219|  4.665|   626| 20442.819| 69.978|  30,622|
| |Casey County|    10| 618.850|  0.000|   188| 11634.383| 300.584|  16,159|
| |Daviess County|     9| 88.660|  2.815|   765|  7536.129| 74.587| 101,511|
| |Ohio County|     8| 333.417| 11.908|   356| 14837.043| 95.262|  23,994|
| |Hardin County|     8| 72.099|  0.000|   619|  5578.687| 126.174| 110,958|
| |Christian County|     8| 113.538|  4.055|   501|  7110.316| 52.714|  70,461|
| |Allen County|     8| 375.323|  0.000|   226| 10602.862| 60.320|  21,315|
| |Knox County|     8| 256.863|  0.000|   235|  7545.352| 155.953|  31,145|
| |Simpson County|     7| 376.911|  0.000|   150|  8076.675| 92.305|  18,572|
| |Clark County|     7| 193.034|  0.000|   166|  4577.669| 39.395|  36,263|
| |Franklin County|     7| 137.279|  5.603|   302|  5922.614| 131.676|  50,991|
| |Gallatin County|     7| 789.266|  0.000|    80|  9020.183| 16.107|   8,869|
| |Bullitt County|     5| 61.217|  1.749|   374|  4579.069| 103.195|  81,676|
| |Grant County|     5| 199.450|  0.000|   117|  4667.119| 96.875|  25,069|
| |Laurel County|     5| 82.219|  2.349|   433|  7120.188| 138.598|  60,813|
| |Clay County|     5| 251.244|  0.000|   152|  7637.807| 64.606|  19,901|
| |Russell County|     5| 278.971|  0.000|   108|  6025.777| 63.765|  17,923|
| |Pulaski County|     5| 76.948|  6.596|   298|  4586.097| 87.940|  64,979|
| |Bell County|     4| 153.657| 10.976|   312| 11985.249| 208.535|  26,032|
| |Calloway County|     4| 102.561|  7.326|   242|  6204.969| 183.145|  39,001|
| |McCracken County|     4| 61.145|  0.000|   366|  5594.790| 78.615|  65,418|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686| 34.801|   8,210|
| |Boyd County|     3| 64.215|  0.000|   190|  4066.955| 58.099|  46,718|
| |Henderson County|     3| 66.357|  0.000|   344|  7608.936| 66.357|  45,210|
| |Perry County|     3| 116.469|  0.000|   224|  8696.327| 205.207|  25,758|
| |Pike County|     3| 51.835|  0.000|   249|  4302.301| 74.050|  57,876|
| |Harlan County|     3| 115.340|  0.000|   232|  8919.646| 175.757|  26,010|
| |Green County|     2| 182.799|  0.000|    36|  3290.376| 78.342|  10,941|
| |Fulton County|     2| 335.064| 23.933|    84| 14072.709| 598.329|   5,969|
| |Floyd County|     2| 56.197|  4.014|    95|  2669.364| 56.197|  35,589|
| |Carroll County|     2| 188.129|  0.000|   158| 14862.195| 228.442|  10,631|
| |Breckinridge County|     2| 97.671|  0.000|    70|  3418.470| 125.576|  20,477|
| |Barren County|     2| 45.199|  0.000|   364|  8226.175| 116.225|  44,249|
| |Meade County|     2| 69.999|  0.000|    94|  3289.934| 44.999|  28,572|
| |Marshall County|     2| 64.309|  0.000|   137|  4405.145| 59.715|  31,100|
| |Metcalfe County|     2| 198.590|  0.000|    60|  5957.700| 141.850|  10,071|
| |Monroe County|     2| 187.793|  0.000|    94|  8826.291| 80.483|  10,650|
| |Nelson County|     2| 43.259|  0.000|   216|  4671.988| 83.428|  46,233|
| |Taylor County|     2| 77.613|  0.000|   131|  5083.628| 166.313|  25,769|
| |Henry County|     2| 124.023|  0.000|   120|  7441.399| 256.905|  16,126|
| |Crittenden County|     1| 113.559|  0.000|    31|  3520.327| 81.114|   8,806|
| |Clinton County|     1| 97.867| 13.981|    32|  3131.728| 83.886|  10,218|
| |Carter County|     1| 37.318|  0.000|   101|  3769.079| 31.987|  26,797|
| |Carlisle County|     1| 210.084|  0.000|    43|  9033.613| 510.204|   4,760|
| |Bourbon County|     1| 50.536|  0.000|    81|  4093.390| 86.633|  19,788|
| |Bath County|     1| 80.000|  0.000|    37|  2960.000| 22.857|  12,500|
| |Anderson County|     1| 43.962|  0.000|    84|  3692.795| 56.522|  22,747|
| |Greenup County|     1| 28.492|  0.000|   110|  3134.082| 85.475|  35,098|
| |Knott County|     1| 67.540|  0.000|    57|  3849.791| 164.026|  14,806|
| |Whitley County|     1| 27.576|  0.000|   163|  4494.816| 106.363|  36,264|
| |Webster County|     1| 77.268|  0.000|    88|  6799.567| 77.268|  12,942|
| |Mason County|     1| 58.582|  0.000|    54|  3163.445|  8.369|  17,070|
| |Madison County|     1| 10.754|  0.000|   505|  5430.867| 187.430|  92,987|
| |McLean County|     1| 108.613|  0.000|    42|  4561.746| 62.065|   9,207|
| |Livingston County|     1| 108.767|  0.000|    35|  3806.831| 46.614|   9,194|
| |Lincoln County|     1| 40.735|  0.000|   105|  4277.160| 34.916|  24,549|
| |Larue County|     1| 69.454|  0.000|    54|  3750.521| 49.610|  14,398|
| |Fleming County|     0|  0.000|  0.000|    59|  4046.362| 39.190|  14,581|
| |Estill County|     0|  0.000|  0.000|    22|  1559.620| 101.274|  14,106|
| |Elliott County|     0|  0.000|  0.000|    11|  1463.350| 76.018|   7,517|
| |Cumberland County|     0|  0.000|  0.000|    57|  8618.083| 367.186|   6,614|
| |Woodford County|     0|  0.000|  0.000|   155|  5797.860| 138.935|  26,734|
| |Jessamine County|     0|  0.000|  0.000|   340|  6282.916| 131.994|  54,115|
| |Hickman County|     0|  0.000|  0.000|    48| 10958.904| 489.237|   4,380|
| |Hart County|     0|  0.000|  0.000|    99|  5200.946| 165.109|  19,035|
| |Harrison County|     0|  0.000|  0.000|   121|  6406.862| 37.821|  18,886|
| |Trigg County|     0|  0.000|  0.000|    54|  3685.755| 48.753|  14,651|
| |Todd County|     0|  0.000|  0.000|    35|  2846.917| 23.240|  12,294|
| |Spencer County|     0|  0.000|  0.000|   120|  6201.230| 169.796|  19,351|
| |Scott County|     0|  0.000|  0.000|   377|  6613.571| 135.329|  57,004|
| |Rowan County|     0|  0.000|  0.000|    70|  2861.815| 11.681|  24,460|
| |Rockcastle County|     0|  0.000|  0.000|    71|  4252.770| 85.569|  16,695|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    53|  4288.373| 57.795|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    44|  3015.764| 78.332|  14,590|
| |Owsley County|     0|  0.000|  0.000|    12|  2718.007| 64.714|   4,415|
| |Owen County|     0|  0.000|  0.000|    48|  4403.266| 78.630|  10,901|
| |Nicholas County|     0|  0.000|  0.000|    20|  2751.410|  0.000|   7,269|
| |Morgan County|     0|  0.000|  0.000|    31|  2329.251| 21.468|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   121|  4297.333| 40.589|  28,157|
| |Mercer County|     0|  0.000|  0.000|    83|  3784.252| 58.620|  21,933|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Martin County|     0|  0.000|  0.000|    36|  3215.721| 76.565|  11,195|
| |Marion County|     0|  0.000|  0.000|   119|  6174.441| 103.772|  19,273|
| |Magoffin County|     0|  0.000|  0.000|    39|  3206.973| 223.196|  12,161|
| |McCreary County|     0|  0.000|  0.000|    40|  2321.397| 33.163|  17,231|
| |Lewis County|     0|  0.000|  0.000|    41|  3088.512| 64.568|  13,275|
| |Letcher County|     0|  0.000|  0.000|    59|  2737.438| 66.282|  21,553|
| |Trimble County|     0|  0.000|  0.000|    32|  3777.594|  0.000|   8,471|
| |Union County|     0|  0.000|  0.000|    65|  4519.853| 119.205|  14,381|
| |Washington County|     0|  0.000|  0.000|    85|  7027.697| 271.659|  12,095|
| |Wayne County|     0|  0.000|  0.000|    66|  3245.955| 98.362|  20,333|
| |Hancock County|     0|  0.000|  0.000|    50|  5732.630| 49.137|   8,722|
| |Johnson County|     0|  0.000|  0.000|    49|  2208.401| 64.385|  22,188|
| |Lawrence County|     0|  0.000|  0.000|    36|  2350.330| 27.980|  15,317|
| |Lee County|     0|  0.000|  0.000|     6|   810.482| 38.594|   7,403|
| |Leslie County|     0|  0.000|  0.000|    30|  3037.360| 57.854|   9,877|
| |Caldwell County|     0|  0.000|  0.000|    53|  4157.841| 44.828|  12,747|
| |Breathitt County|     0|  0.000|  0.000|    31|  2454.473| 56.555|  12,630|
| |Bracken County|     0|  0.000|  0.000|    34|  4094.905| 86.027|   8,303|
| |Boyle County|     0|  0.000|  0.000|   154|  5123.087| 95.048|  30,060|
| |Ballard County|     0|  0.000|  0.000|    35|  4437.120| 90.553|   7,888|
| |Wolfe County|     0|  0.000|  0.000|    14|  1956.127| 99.802|   7,157|
| |Garrard County|     0|  0.000|  0.000|    78|  4415.261| 80.866|  17,666|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   685| 326.684| N/A|21,013| 10021.323| N/A|2,096,829|
| |McKinley County|   225| 3152.718|  8.007| 4,046| 56692.869| 88.076|  71,367|
| |San Juan County|   184| 1484.374|  3.457| 3,044| 24556.705| 48.403| 123,958|
| |Bernalillo County|   134| 197.314|  2.314| 5,136|  7562.717| 58.058| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,133|  7720.719| 36.992| 146,748|
| |Dona Ana County|    30| 137.492|  4.583| 2,447| 11214.739| 152.550| 218,195|
| |Cibola County|    18| 674.789|  5.355|   366| 13720.712| 160.664|  26,675|
| |Otero County|    10| 148.170|  0.000|   201|  2978.219| 35.984|  67,490|
| |Rio Arriba County|     7| 179.851|  7.341|   318|  8170.396| 88.091|  38,921|
| |Chaves County|     6| 92.858|  0.000|   457|  7072.661| 210.035|  64,615|
| |Socorro County|     6| 360.642|  0.000|    74|  4447.917|  8.587|  16,637|
| |Eddy County|     4| 68.423|  0.000|   301|  5148.820| 117.296|  58,460|
| |Lea County|     4| 56.283|  0.000|   776| 10918.812| 271.362|  71,070|
| |Valencia County|     4| 52.159|  0.000|   414|  5398.498| 83.828|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   650|  4323.016| 52.256| 150,358|
| |Luna County|     3| 126.534|  0.000|   254| 10713.231| 168.712|  23,709|
| |Curry County|     2| 40.855|  0.000|   552| 11275.892| 210.110|  48,954|
| |Grant County|     2| 74.080|  0.000|    71|  2629.824| 21.166|  26,998|
| |Lincoln County|     2| 102.187|  7.299|   128|  6539.955| 167.878|  19,572|
| |Union County|     2| 492.732| 70.390|    30|  7390.983| 105.585|   4,059|
| |Torrance County|     1| 64.679|  0.000|    61|  3945.411|  9.240|  15,461|
| |Taos County|     1| 30.560|  0.000|   108|  3300.431| 43.656|  32,723|
| |Roosevelt County|     1| 54.054|  0.000|   164|  8864.865| 177.606|  18,500|
| |Quay County|     1| 121.168|  0.000|    34|  4119.714| 34.619|   8,253|
| |Catron County|     1| 283.527|  0.000|     5|  1417.635| 40.504|   3,527|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411| 47.854|  11,941|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Guadalupe County|     0|  0.000|  0.000|    31|  7209.302|  0.000|   4,300|
| |Harding County|     0|  0.000|  0.000|     1|  1600.000|  0.000|     625|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780| 68.060|   4,198|
| |Los Alamos County|     0|  0.000|  0.000|    22|  1135.836| 14.751|  19,369|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |San Miguel County|     0|  0.000|  0.000|    43|  1576.420|  5.237|  27,277|
| |Sierra County|     0|  0.000|  0.000|    32|  2965.434| 39.716|  10,791|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   603| 152.389| N/A|43,561| 11008.673| N/A|3,956,971|
| |Oklahoma County|   112| 140.450|  2.508|10,560| 13242.475| 215.513| 797,434|
| |Tulsa County|   107| 164.223|  1.316|10,465| 16061.650| 310.029| 651,552|
| |Cleveland County|    55| 193.652|  3.018| 2,994| 10541.734| 146.371| 284,014|
| |Washington County|    39| 756.885|  0.000|   632| 12265.414| 169.121|  51,527|
| |McCurtain County|    28| 852.827| 13.053|   854| 26011.209| 121.832|  32,832|
| |Wagoner County|    23| 282.941|  1.757|   860| 10579.537| 223.190|  81,289|
| |Delaware County|    19| 441.768|  0.000|   426|  9904.904| 83.039|  43,009|
| |Muskogee County|    16| 235.304|  0.000|   506|  7441.505| 142.863|  67,997|
| |Caddo County|    16| 556.290|  9.934|   417| 14498.296| 293.045|  28,762|
| |Rogers County|    16| 173.050|  3.090|   976| 10556.030| 271.935|  92,459|
| |Creek County|    14| 195.744|  1.997|   596|  8333.100| 205.731|  71,522|
| |Osage County|    11| 234.227|  0.000|   417|  8879.331| 155.137|  46,963|
| |Kay County|    11| 252.653|  3.281|   244|  5604.300| 98.436|  43,538|
| |Comanche County|    10| 82.816|  0.000|   831|  6882.045| 70.986| 120,749|
| |Pottawatomie County|     9| 123.981|  3.936|   447|  6157.703| 106.269|  72,592|
| |Greer County|     8| 1400.560|  0.000|    83| 14530.812| 75.030|   5,712|
| |Grady County|     7| 125.372|  2.559|   441|  7898.413| 81.875|  55,834|
| |Canadian County|     7| 47.200|  1.927| 1,208|  8145.321| 125.224| 148,306|
| |Texas County|     7| 350.298|  0.000| 1,056| 52844.918| 150.128|  19,983|
| |Adair County|     6| 270.343|  6.437|   340| 15319.456| 238.160|  22,194|
| |Mayes County|     6| 145.985|  0.000|   316|  7688.564| 107.751|  41,100|
| |Seminole County|     5| 206.118|  0.000|   235|  9687.526| 247.341|  24,258|
| |Garfield County|     5| 81.892|  2.340|   452|  7403.040| 203.560|  61,056|
| |Jackson County|     5| 203.832|  5.824|   523| 21320.832| 215.480|  24,530|
| |Sequoyah County|     4| 96.226|  0.000|   340|  8179.172| 281.803|  41,569|
| |Payne County|     4| 48.909|  1.747|   730|  8925.951| 117.033|  81,784|
| |Garvin County|     4| 144.347|  0.000|   226|  8155.606| 103.105|  27,711|
| |Carter County|     4| 83.141|  2.969|   338|  7025.420| 100.957|  48,111|
| |McClain County|     4| 98.829|  0.000|   440| 10871.177| 155.303|  40,474|
| |Pawnee County|     3| 183.195|  0.000|   137|  8365.901| 148.301|  16,376|
| |Stephens County|     3| 69.536|  3.311|   200|  4635.746| 86.092|  43,143|
| |Pittsburg County|     3| 68.722|  0.000|   350|  8017.593| 513.780|  43,654|
| |Okmulgee County|     3| 77.993|  0.000|   467| 12140.907| 252.549|  38,465|
| |Ottawa County|     3| 96.379|  4.589|   369| 11854.660| 110.148|  31,127|
| |Lincoln County|     2| 57.344|  0.000|   164|  4702.239| 139.265|  34,877|
| |Pontotoc County|     2| 52.241|  0.000|   199|  5197.994| 85.825|  38,284|
| |Noble County|     2| 179.678|  0.000|    83|  7456.653| 77.005|  11,131|
| |Cotton County|     2| 352.983|  0.000|    18|  3176.844| 25.213|   5,666|
| |Cherokee County|     2| 41.104|  2.936|   440|  9042.892| 275.984|  48,657|
| |Hughes County|     2| 150.614| 10.758|   137| 10317.042| 279.711|  13,279|
| |Bryan County|     1| 20.836|  0.000|   452|  9417.648| 196.449|  47,995|
| |Beckham County|     1| 45.748|  0.000|    60|  2744.865| 98.031|  21,859|
| |Roger Mills County|     1| 279.096| 39.871|     8|  2232.766|  0.000|   3,583|
| |Tillman County|     1| 137.931|  0.000|    58|  8000.000| 59.113|   7,250|
| |Choctaw County|     1| 68.157|  0.000|   185| 12609.051| 184.998|  14,672|
| |Latimer County|     1| 99.275|  0.000|    88|  8736.226| 269.462|  10,073|
| |Le Flore County|     1| 20.059|  0.000|   340|  6820.051| 298.019|  49,853|
| |Logan County|     1| 20.829|  0.000|   220|  4582.283| 104.143|  48,011|
| |McIntosh County|     1| 51.031|  0.000|   180|  9185.548| 211.413|  19,596|
| |Major County|     1| 131.079|  0.000|    34|  4456.678| 168.530|   7,629|
| |Marshall County|     1| 59.063|  8.438|   107|  6319.768| 92.814|  16,931|
| |Nowata County|     1| 99.246|  0.000|    57|  5657.007| 28.356|  10,076|
| |Okfuskee County|     1| 83.382| 11.912|    66|  5503.210| 119.117|  11,993|
| |Kiowa County|     1| 114.837|  0.000|    28|  3215.434| 16.405|   8,708|
| |Pushmataha County|     0|  0.000|  0.000|   108|  9733.237| 77.248|  11,096|
| |Atoka County|     0|  0.000|  0.000|    70|  5087.949| 72.685|  13,758|
| |Alfalfa County|     0|  0.000|  0.000|     3|   526.131|  0.000|   5,702|
| |Beaver County|     0|  0.000|  0.000|    36|  6778.384|  0.000|   5,311|
| |Washita County|     0|  0.000|  0.000|    27|  2473.433| 26.174|  10,916|
| |Woods County|     0|  0.000|  0.000|    20|  2274.537| 81.233|   8,793|
| |Woodward County|     0|  0.000|  0.000|    37|  1830.686| 35.341|  20,211|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167| 47.603|   6,002|
| |Johnston County|     0|  0.000|  0.000|    47|  4239.964| 90.212|  11,085|
| |Kingfisher County|     0|  0.000|  0.000|   136|  8626.705| 244.665|  15,765|
| |Love County|     0|  0.000|  0.000|    75|  7314.932| 139.332|  10,253|
| |Murray County|     0|  0.000|  0.000|    73|  5187.238| 142.116|  14,073|
| |Blaine County|     0|  0.000|  0.000|    42|  4454.343|  0.000|   9,429|
| |Haskell County|     0|  0.000|  0.000|    58|  4593.332| 192.332|  12,627|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817| 430.779|   2,653|
| |Harper County|     0|  0.000|  0.000|    10|  2711.497| 38.736|   3,688|
| |Cimarron County|     0|  0.000|  0.000|     1|   467.946|  0.000|   2,137|
| |Coal County|     0|  0.000|  0.000|    35|  6369.427| 207.981|   5,495|
| |Craig County|     0|  0.000|  0.000|    82|  5798.331| 50.508|  14,142|
| |Custer County|     0|  0.000|  0.000|   206|  7102.714| 78.810|  29,003|
| |Dewey County|     0|  0.000|  0.000|    10|  2044.572| 87.624|   4,891|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672| 74.038|   3,859|
| |Grant County|     0|  0.000|  0.000|    15|  3461.805| 131.878|   4,333|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   591| 837.408| N/A|12,753| 18070.164| N/A| 705,749|
| |District of Columbia|   591| 837.408|  1.417|12,753| 18070.164| 140.884| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   591| 606.923| N/A|15,332| 15745.088| N/A| 973,764|
| |New Castle County|   291| 520.803|  1.023| 7,206| 12896.575| 86.417| 558,753|
| |Sussex County|   192| 819.725|  0.610| 5,839| 24929.021| 111.614| 234,225|
| |Kent County|   108| 597.391|  0.790| 2,287| 12650.316| 69.538| 180,786|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   544| 180.264| N/A|47,587| 15768.751| N/A|3,017,804|
| |Pulaski County|    85| 216.886|  2.552| 5,582| 14243.030| 271.199| 391,911|
| |Washington County|    52| 217.403|  3.584| 6,298| 26330.862| 174.998| 239,187|
| |Benton County|    43| 154.044|  2.047| 4,774| 17102.468| 125.896| 279,141|
| |Jefferson County|    40| 598.587|  4.276| 1,534| 22955.824| 378.393|  66,824|
| |Crittenden County|    23| 479.616|  8.937| 1,356| 28276.509| 425.995|  47,955|
| |Sebastian County|    20| 156.461|  5.588| 2,176| 17023.008| 455.973| 127,827|
| |Union County|    17| 439.481|  3.693|   499| 12900.057| 243.746|  38,682|
| |Yell County|    14| 656.014|  0.000| 1,066| 49950.799| 294.537|  21,341|
| |Garland County|    14| 140.865| 10.062| 1,008| 10142.274| 237.171|  99,386|
| |Mississippi County|    14| 344.395| 14.057| 1,014| 24944.036| 839.902|  40,651|
| |Lincoln County|    12| 921.376| 10.969| 1,219| 93596.437| 405.844|  13,024|
| |Craighead County|    12| 108.763|  1.295| 1,344| 12181.416| 290.034| 110,332|
| |Columbia County|    11| 468.943| 30.451|   215|  9165.707| 133.984|  23,457|
| |Hot Spring County|    11| 325.723| 12.691| 1,546| 45778.923| 376.485|  33,771|
| |Sevier County|    10| 587.993|  0.000|   989| 58152.525| 453.595|  17,007|
| |Pope County|    10| 156.074|  2.230| 1,313| 20492.571| 247.489|  64,072|
| |Nevada County|     9| 1090.645|  0.000|   142| 17207.950| 207.742|   8,252|
| |Lawrence County|     9| 548.580|  0.000|   212| 12922.102| 235.106|  16,406|
| |Phillips County|     8| 449.893| 16.068|   318| 17883.253| 289.217|  17,782|
| |Chicot County|     8| 790.670| 28.238|   733| 72445.147| 2880.298|  10,118|
| |Lee County|     8| 903.240| 32.259|   894| 100937.112| 145.164|   8,857|
| |Carroll County|     7| 246.653|  5.034|   354| 12473.573| 70.472|  28,380|
| |Newton County|     6| 773.894| 55.278|   103| 13285.180| 165.834|   7,753|
| |Faulkner County|     6| 47.616|  1.134| 1,304| 10348.631| 114.506| 126,007|
| |Saline County|     6| 49.005|  2.334| 1,046|  8543.169| 194.852| 122,437|
| |Sharp County|     5| 286.664|  0.000|   113|  6478.615| 73.714|  17,442|
| |Miller County|     5| 115.588|  3.303|   512| 11836.235| 165.126|  43,257|
| |Cleburne County|     5| 200.650|  0.000|   200|  8026.004| 108.924|  24,919|
| |Ashley County|     5| 254.362|  7.267|   326| 16584.423| 559.597|  19,657|
| |Cross County|     4| 243.620| 26.102|   195| 11876.485| 252.321|  16,419|
| |Crawford County|     4| 63.234|  2.258|   627|  9911.947| 205.511|  63,257|
| |Howard County|     4| 302.984| 21.642|   340| 25753.674| 476.118|  13,202|
| |Clay County|     4| 274.895|  0.000|   136|  9346.437| 284.713|  14,551|
| |Poinsett County|     3| 127.508|  0.000|   272| 11560.694| 686.113|  23,528|
| |Randolph County|     3| 167.056|  7.955|   213| 11861.009| 318.203|  17,958|
| |St. Francis County|     3| 120.029|  0.000| 1,209| 48371.609| 445.821|  24,994|
| |Bradley County|     3| 278.733|  0.000|   190| 17653.071| 637.103|  10,763|
| |Conway County|     3| 143.913|  0.000|   152|  7291.567| 109.648|  20,846|
| |Drew County|     3| 164.663|  7.841|   203| 11142.214| 321.485|  18,219|
| |Desha County|     2| 176.041|  0.000|   194| 17075.962| 540.697|  11,361|
| |Cleveland County|     2| 251.383|  0.000|    97| 12192.056| 520.721|   7,956|
| |Hempstead County|     2| 92.885|  0.000|   239| 11099.758| 192.405|  21,532|
| |White County|     2| 25.396|  0.000|   322|  4088.733| 108.839|  78,753|
| |Franklin County|     2| 112.899|  0.000|   126|  7112.616| 145.155|  17,715|
| |Lafayette County|     2| 301.932|  0.000|    54|  8152.174| 107.833|   6,624|
| |Johnson County|     2| 75.250| 10.750|   668| 25133.569| 198.876|  26,578|
| |Lonoke County|     2| 27.282|  0.000|   512|  6984.136| 153.947|  73,309|
| |Madison County|     2| 120.656|  8.618|   270| 16288.610| 94.801|  16,576|
| |Ouachita County|     2| 85.536|  6.110|   100|  4276.794| 140.523|  23,382|
| |Van Buren County|     2| 120.882|  0.000|    53|  3203.385| 25.903|  16,545|
| |Clark County|     1| 44.803|  6.400|   177|  7930.108| 147.209|  22,320|
| |Stone County|     1| 79.962|  0.000|    69|  5517.352| 182.769|  12,506|
| |Jackson County|     1| 59.812|  0.000|   112|  6698.965| 461.408|  16,719|
| |Little River County|     1| 81.573|  0.000|   181| 14764.663| 326.291|  12,259|
| |Logan County|     1| 46.585|  0.000|   261| 12158.763| 685.469|  21,466|
| |Polk County|     1| 50.090|  0.000|   142|  7112.803| 100.180|  19,964|
| |Pike County|     1| 93.301|  0.000|   101|  9423.400| 306.560|  10,718|
| |Boone County|     1| 26.715|  0.000|   211|  5636.888| 156.474|  37,432|
| |Montgomery County|     1| 111.284| 15.898|    35|  3894.948| 158.977|   8,986|
| |Izard County|     1| 73.373|  0.000|    53|  3888.767| 94.337|  13,629|
| |Independence County|     1| 26.438|  3.777|   517| 13668.209| 566.519|  37,825|
| |Greene County|     1| 22.063|  0.000|   476| 10501.931| 293.121|  45,325|
| |Arkansas County|     1| 57.189|  8.170|   217| 12409.928| 147.056|  17,486|
| |Scott County|     0|  0.000|  0.000|    61|  5933.275| 264.010|  10,281|
| |Prairie County|     0|  0.000|  0.000|    91| 11287.522| 442.995|   8,062|
| |Searcy County|     0|  0.000|  0.000|    30|  3806.624| 90.634|   7,881|
| |Woodruff County|     0|  0.000|  0.000|    21|  3322.785| 45.208|   6,320|
| |Baxter County|     0|  0.000|  0.000|    71|  1693.218| 34.069|  41,932|
| |Fulton County|     0|  0.000|  0.000|    42|  3366.194| 148.845|  12,477|
| |Grant County|     0|  0.000|  0.000|   136|  7445.935| 86.035|  18,265|
| |Perry County|     0|  0.000|  0.000|    54|  5164.993| 68.320|  10,455|
| |Dallas County|     0|  0.000|  0.000|    63|  8988.443| 101.910|   7,009|
| |Calhoun County|     0|  0.000|  0.000|    16|  3083.446| 82.592|   5,189|
| |Marion County|     0|  0.000|  0.000|    28|  1677.249| 42.787|  16,694|
| |Monroe County|     0|  0.000|  0.000|    60|  8953.887| 170.550|   6,701|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   419| 308.154| N/A| 6,829|  5022.391| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.000| 3,850|  9232.060| 28.433| 417,025|
| |Rockingham County|    96| 309.908|  0.461| 1,691|  5458.906| 27.209| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   464|  3064.911|  5.662| 151,391|
| |Strafford County|    13| 99.515|  0.000|   358|  2740.502| 30.620| 130,633|
| |Belknap County|     4| 65.250|  0.000|   115|  1875.928| 13.982|  61,303|
| |Cheshire County|     3| 39.430|  1.878|    97|  1274.890| 13.143|  76,085|
| |Grafton County|     1| 11.125|  0.000|   103|  1145.896|  0.000|  89,886|
| |Sullivan County|     1| 23.177|  0.000|    40|   927.085|  0.000|  43,146|
| |Carroll County|     1| 20.446|  0.000|    94|  1921.897| 14.604|  48,910|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  4.526|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   379| 130.092| N/A|30,662| 10524.784| N/A|2,913,314|
| |Johnson County|   103| 170.982|  1.186| 5,703|  9467.116| 163.394| 602,401|
| |Wyandotte County|    99| 598.444|  3.454| 4,896| 29595.778| 348.876| 165,429|
| |Sedgwick County|    44| 85.264|  0.554| 4,878|  9452.719| 163.608| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,550|  8763.251| 104.997| 176,875|
| |Lyon County|    13| 391.625|  8.607|   697| 20997.138| 228.089|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,783| 48893.520| 180.202|  36,467|
| |Phillips County|     8| 1528.468|  0.000|    51|  9743.982| 109.176|   5,234|
| |Ford County|     8| 237.961|  0.000| 2,069| 61542.580| 182.720|  33,619|
| |Leavenworth County|     8| 97.850|  0.000| 1,459| 17845.348| 117.070|  81,758|
| |Coffey County|     8| 978.115|  0.000|    67|  8191.710| 34.933|   8,179|
| |Riley County|     5| 67.356|  0.000|   477|  6425.800| 53.885|  74,232|
| |Saline County|     5| 92.210|  0.000|   372|  6860.431| 84.306|  54,224|
| |Douglas County|     5| 40.897|  2.337|   714|  5840.061| 74.783| 122,259|
| |Montgomery County|     5| 157.089|  0.000|   167|  5246.788| 67.324|  31,829|
| |Seward County|     4| 186.672|  0.000| 1,220| 56934.852| 213.339|  21,428|
| |Sumner County|     3| 131.372|  0.000|    99|  4335.260| 12.512|  22,836|
| |Barton County|     3| 116.374|  0.000|   139|  5391.986| 138.540|  25,779|
| |Morton County|     2| 773.096|  0.000|     9|  3478.933|  0.000|   2,587|
| |Grant County|     2| 279.720|  0.000|   110| 15384.615| 319.680|   7,150|
| |Geary County|     2| 63.151|  0.000|   140|  4420.587| 54.130|  31,670|
| |Cowley County|     2| 57.293|  0.000|   165|  4726.710| 57.293|  34,908|
| |Clay County|     2| 249.938|  0.000|    20|  2499.375| 53.558|   8,002|
| |Bourbon County|     2| 137.608|  9.829|    73|  5022.705| 78.633|  14,534|
| |Trego County|     1| 356.761|  0.000|     6|  2140.564| 50.966|   2,803|
| |Stafford County|     1| 240.616| 34.374|     3|   721.848|  0.000|   4,156|
| |Stanton County|     1| 498.504|  0.000|    18|  8973.081| 142.430|   2,006|
| |Jackson County|     1| 75.924|  0.000|   146| 11084.959| 21.693|  13,171|
| |Harvey County|     1| 29.045|  0.000|   194|  5634.785| 153.525|  34,429|
| |Franklin County|     1| 39.148|  0.000|   178|  6968.368| 162.185|  25,544|
| |Ellis County|     1| 35.023|  0.000|   141|  4938.185| 65.042|  28,553|
| |Dickinson County|     1| 54.154|  0.000|    47|  2545.218| 54.154|  18,466|
| |Kearny County|     1| 260.552|  0.000|    59| 15372.590| 74.444|   3,838|
| |Crawford County|     1| 25.761|  0.000|   380|  9789.273| 44.162|  38,818|
| |Clark County|     1| 501.505|  0.000|    44| 22066.199| 71.644|   1,994|
| |Cherokee County|     1| 50.153|  0.000|   118|  5918.050| 322.412|  19,939|
| |Butler County|     1| 14.945|  2.135|   255|  3811.033| 117.427|  66,911|
| |Reno County|     1| 16.130|  0.000|   273|  4403.368| 124.428|  61,998|
| |Nemaha County|     1| 97.742| 13.963|    49|  4789.366| 27.926|  10,231|
| |Marion County|     1| 84.147|  0.000|    48|  4039.044| 72.126|  11,884|
| |McPherson County|     1| 35.036|  0.000|   142|  4975.124| 65.067|  28,542|
| |Neosho County|     0|  0.000|  0.000|    58|  3623.415| 71.397|  16,007|
| |Morris County|     0|  0.000|  0.000|    11|  1957.295| 50.839|   5,620|
| |Wabaunsee County|     0|  0.000|  0.000|    42|  6059.732| 61.834|   6,931|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Ness County|     0|  0.000|  0.000|     6|  2181.818| 51.948|   2,750|
| |Thomas County|     0|  0.000|  0.000|    38|  4886.203| 110.215|   7,777|
| |Stevens County|     0|  0.000|  0.000|    45|  8204.193| 52.090|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    15|  2535.068| 24.144|   5,917|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Scott County|     0|  0.000|  0.000|    47|  9744.972| 562.780|   4,823|
| |Russell County|     0|  0.000|  0.000|    13|  1896.149| 62.510|   6,856|
| |Rooks County|     0|  0.000|  0.000|    17|  3455.285| 58.072|   4,920|
| |Rice County|     0|  0.000|  0.000|    37|  3879.627| 149.793|   9,537|
| |Republic County|     0|  0.000|  0.000|    32|  6902.502| 154.074|   4,636|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    33|  3601.048|  0.000|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   107|  4388.303| 29.294|  24,383|
| |Pawnee County|     0|  0.000|  0.000|     7|  1091.363|  0.000|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    34|  5960.729| 100.180|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Osage County|     0|  0.000|  0.000|    40|  2507.994| 17.914|  15,949|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Atchison County|     0|  0.000|  0.000|    64|  3981.833| 26.664|  16,073|
| |Marshall County|     0|  0.000|  0.000|     9|   927.166|  0.000|   9,707|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Doniphan County|     0|  0.000|  0.000|    48|  6315.789| 75.188|   7,600|
| |Edwards County|     0|  0.000|  0.000|    10|  3573.981|  0.000|   2,798|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Anderson County|     0|  0.000|  0.000|    29|  3690.506| 36.360|   7,858|
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
| |Linn County|     0|  0.000|  0.000|    35|  3607.132| 73.615|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Lane County|     0|  0.000|  0.000|     5|  3257.329|  0.000|   1,535|
| |Harper County|     0|  0.000|  0.000|    10|  1839.588| 52.560|   5,436|
| |Labette County|     0|  0.000|  0.000|   133|  6779.488| 189.330|  19,618|
| |Kiowa County|     0|  0.000|  0.000|     7|  2828.283| 57.720|   2,475|
| |Kingman County|     0|  0.000|  0.000|    17|  2376.957| 159.795|   7,152|
| |Jewell County|     0|  0.000|  0.000|    11|  3820.771| 99.241|   2,879|
| |Jefferson County|     0|  0.000|  0.000|    76|  3990.968| 127.531|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    44| 11088.710|  0.000|   3,968|
| |Hamilton County|     0|  0.000|  0.000|    37| 14572.666|  0.000|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    20|  3343.363| 23.881|   5,982|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753| 115.955|   1,232|
| |Gray County|     0|  0.000|  0.000|    77| 12859.051| 143.143|   5,988|
| |Graham County|     0|  0.000|  0.000|    16|  6446.414|  0.000|   2,482|
| |Gove County|     0|  0.000|  0.000|     6|  2276.176| 162.584|   2,636|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495| 70.235|   6,102|
| |Rush County|     0|  0.000|  0.000|     6|  1976.285| 47.054|   3,036|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   356| 84.405| N/A|21,272|  5043.463| N/A|4,217,737|
| |Multnomah County|    95| 116.872|  0.527| 4,917|  6049.049| 82.074| 812,855|
| |Marion County|    70| 201.255|  1.232| 2,911|  8369.320| 100.217| 347,818|
| |Clackamas County|    40| 95.651|  1.366| 1,538|  3677.781| 46.801| 418,187|
| |Umatilla County|    28| 359.205|  7.331| 2,290| 29377.806| 538.807|  77,950|
| |Washington County|    25| 41.556|  0.475| 3,088|  5133.047| 61.266| 601,592|
| |Malheur County|    14| 457.950| 18.692|   783| 25612.509| 514.026|  30,571|
| |Yamhill County|    13| 121.382|  2.668|   460|  4295.051| 134.721| 107,100|
| |Polk County|    12| 139.397|  0.000|   313|  3635.941| 41.487|  86,085|
| |Deschutes County|    10| 50.584|  1.445|   604|  3055.258| 48.416| 197,692|
| |Linn County|    10| 77.072|  0.000|   281|  2165.720| 36.334| 129,749|
| |Lincoln County|     9| 180.137|  0.000|   416|  8326.328| 71.483|  49,962|
| |Benton County|     6| 64.479|  0.000|   169|  1816.169| 21.493|  93,053|
| |Jefferson County|     4| 162.219|  5.794|   360| 14599.724| 289.677|  24,658|
| |Morrow County|     3| 258.554| 24.624|   357| 30767.905| 652.541|  11,603|
| |Wasco County|     3| 112.435|  0.000|   192|  7195.862| 165.976|  26,682|
| |Lane County|     3|  7.852|  0.000|   585|  1531.145| 25.052| 382,067|
| |Klamath County|     2| 29.309|  2.094|   201|  2945.573| 14.655|  68,238|
| |Josephine County|     2| 22.861|  1.633|   115|  1314.481| 16.329|  87,487|
| |Jackson County|     2|  9.052|  0.647|   465|  2104.606| 51.726| 220,944|
| |Union County|     2| 74.530|  0.000|   394| 14682.318| 31.941|  26,835|
| |Wallowa County|     1| 138.735|  0.000|    19|  2635.960|  0.000|   7,208|
| |Douglas County|     1|  9.011|  0.000|   151|  1360.606| 24.457| 110,980|
| |Crook County|     1| 40.977|  0.000|    47|  1925.914| 23.415|  24,404|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764| 160.514|   1,780|
| |Tillamook County|     0|  0.000|  0.000|    34|  1257.582| 31.704|  27,036|
| |Hood River County|     0|  0.000|  0.000|   191|  8168.677| 134.414|  23,382|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|
| |Baker County|     0|  0.000|  0.000|    38|  2356.735| 70.879|  16,124|
| |Clatsop County|     0|  0.000|  0.000|    85|  2113.166| 17.758|  40,224|
| |Columbia County|     0|  0.000|  0.000|    96|  1833.671| 49.116|  52,354|
| |Coos County|     0|  0.000|  0.000|    91|  1411.137| 15.507|  64,487|
| |Curry County|     0|  0.000|  0.000|    15|   654.308|  6.232|  22,925|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Grant County|     0|  0.000|  0.000|     4|   555.633| 39.688|   7,199|
| |Harney County|     0|  0.000|  0.000|    10|  1352.631| 38.647|   7,393|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   345| 178.349| N/A|28,296| 14627.731| N/A|1,934,408|
| |Douglas County|   132| 231.041|  0.250|11,270| 19726.006| 197.535| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,741| 28376.770| 65.196|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,924| 96075.102| 164.072|  20,026|
| |Lancaster County|    17| 53.277|  0.895| 3,292| 10316.839| 85.063| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   100| 10725.011| 61.286|   9,324|
| |Adams County|    11| 350.732|  0.000|   353| 11255.301| 54.659|  31,363|
| |Sarpy County|    11| 58.762|  1.526| 2,258| 12062.224| 175.523| 187,196|
| |Dawson County|     9| 381.437|  0.000|   959| 40644.204| 60.546|  23,595|
| |Dodge County|     9| 246.137|  3.907|   806| 22042.937| 132.836|  36,565|
| |Perkins County|     7| 2421.308| 296.487|    18|  6226.219| 49.414|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   301|  8450.783| 48.130|  35,618|
| |Madison County|     5| 142.454|  0.000|   453| 12906.351| 138.384|  35,099|
| |Howard County|     4| 620.636|  0.000|    55|  8533.747|  0.000|   6,445|
| |Gage County|     4| 185.934|  0.000|    89|  4137.033| 46.484|  21,513|
| |Colfax County|     4| 373.518|  0.000|   701| 65458.960| 93.379|  10,709|
| |Thurston County|     4| 553.710|  0.000|   205| 28377.630| 79.101|   7,224|
| |Custer County|     4| 371.161|  0.000|    46|  4268.349| 39.767|  10,777|
| |Platte County|     3| 89.633|  0.000|   792| 23662.982| 110.974|  33,470|
| |Cass County|     2| 76.196|  5.443|   178|  6781.469| 114.294|  26,248|
| |Lincoln County|     2| 57.284|  0.000|   123|  3522.942| 114.567|  34,914|
| |Dixon County|     2| 354.862|  0.000|    58| 10290.987| 50.695|   5,636|
| |Saline County|     2| 140.607|  0.000|   595| 41830.709| 120.521|  14,224|
| |Saunders County|     2| 92.687|  0.000|   160|  7414.960| 145.651|  21,578|
| |Washington County|     1| 48.242|  0.000|   125|  6030.199| 130.941|  20,729|
| |Seward County|     1| 57.857|  0.000|   119|  6884.980| 190.101|  17,284|
| |Furnas County|     1| 213.858|  0.000|    15|  3207.870|  0.000|   4,676|
| |Richardson County|     1| 127.146|  0.000|    22|  2797.203| 36.327|   7,865|
| |Fillmore County|     1| 183.083|  0.000|    24|  4393.995|  0.000|   5,462|
| |Antelope County|     1| 158.781|  0.000|    19|  3016.831| 22.683|   6,298|
| |Buffalo County|     1| 20.137|  0.000|   415|  8356.995| 195.620|  49,659|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Banner County|     0|  0.000|  0.000|     3|  4026.846| 191.755|     745|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616| 46.061|   6,203|
| |Cuming County|     0|  0.000|  0.000|    67|  7574.045| 145.344|   8,846|
| |Dawes County|     0|  0.000|  0.000|    10|  1164.280| 33.265|   8,589|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827| 308.547|     463|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827| 79.631|   1,794|
| |Chase County|     0|  0.000|  0.000|     6|  1529.052|  0.000|   3,924|
| |Brown County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,955|
| |Cedar County|     0|  0.000|  0.000|    22|  2618.424| 17.003|   8,402|
| |Butler County|     0|  0.000|  0.000|    60|  7485.030| 71.286|   8,016|
| |Burt County|     0|  0.000|  0.000|    33|  5109.150| 176.940|   6,459|
| |Boyd County|     0|  0.000|  0.000|     4|  2084.419| 223.331|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    12|  1112.863| 13.248|  10,783|
| |Boone County|     0|  0.000|  0.000|     8|  1540.832| 27.515|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Franklin County|     0|  0.000|  0.000|    12|  4028.197| 143.864|   2,979|
| |Dundy County|     0|  0.000|  0.000|     1|   590.667|  0.000|   1,693|
| |Frontier County|     0|  0.000|  0.000|     3|  1141.987|  0.000|   2,627|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482| 121.271|   2,356|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Gosper County|     0|  0.000|  0.000|    19|  9547.739| 143.575|   1,990|
| |Garfield County|     0|  0.000|  0.000|     3|  1523.616|  0.000|   1,969|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Harlan County|     0|  0.000|  0.000|     1|   295.858|  0.000|   3,380|
| |Red Willow County|     0|  0.000|  0.000|    16|  1491.981|  0.000|  10,724|
| |Polk County|     0|  0.000|  0.000|    26|  4987.531| 54.808|   5,213|
| |Pierce County|     0|  0.000|  0.000|    21|  2937.885| 79.942|   7,148|
| |Phelps County|     0|  0.000|  0.000|    37|  4095.639| 15.813|   9,034|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317| 109.343|   2,613|
| |Otoe County|     0|  0.000|  0.000|    52|  3247.564| 89.219|  16,012|
| |Nuckolls County|     0|  0.000|  0.000|     5|  1205.400|  0.000|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    28|  4016.064| 143.431|   6,972|
| |Nance County|     0|  0.000|  0.000|     8|  2273.373|  0.000|   3,519|
| |Morrill County|     0|  0.000|  0.000|    58| 12494.614|  0.000|   4,642|
| |Merrick County|     0|  0.000|  0.000|    62|  7994.842| 147.370|   7,755|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    34|  4080.653| 51.437|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Keith County|     0|  0.000|  0.000|    22|  2738.362| 53.345|   8,034|
| |Kearney County|     0|  0.000|  0.000|    52|  8006.159| 395.909|   6,495|
| |Johnson County|     0|  0.000|  0.000|    13|  2563.597| 28.171|   5,071|
| |Jefferson County|     0|  0.000|  0.000|    17|  2412.716| 60.825|   7,046|
| |McPherson County|     0|  0.000|  0.000|     5| 10121.457| 289.184|     494|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Holt County|     0|  0.000|  0.000|    13|  1291.348| 70.953|  10,067|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759| 105.274|   1,357|
| |Stanton County|     0|  0.000|  0.000|    29|  4898.649| 24.131|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Sherman County|     0|  0.000|  0.000|    11|  3665.445| 142.810|   3,001|
| |Sheridan County|     0|  0.000|  0.000|     9|  1715.593|  0.000|   5,246|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Thomas County|     0|  0.000|  0.000|     1|  1385.042|  0.000|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762| 57.109|   5,003|
| |Valley County|     0|  0.000|  0.000|    10|  2405.002|  0.000|   4,158|
| |Wayne County|     0|  0.000|  0.000|    37|  3942.461| 30.444|   9,385|
| |York County|     0|  0.000|  0.000|    79|  5775.276| 52.218|  13,679|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139| 182.448|     783|
| |Webster County|     0|  0.000|  0.000|     9|  2581.015|  0.000|   3,487|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   277| 86.402| N/A|35,073| 10939.944| N/A|3,205,958|
| |Salt Lake County|   189| 162.870|  1.600|20,628| 17776.062| 150.190|1,160,437|
| |Utah County|    37| 58.155|  0.449| 8,719| 13704.056| 172.892| 636,235|
| |San Juan County|    25| 1633.133|  9.332|   648| 42330.807| 233.305|  15,308|
| |Davis County|    21| 59.075|  2.813| 3,224|  9069.402| 86.804| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   563| 16514.623| 134.095|  34,091|
| |Summit County|     1| 23.728|  0.000|   710| 16846.601| 50.845|  42,145|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Tooele County|     0|  0.000|  0.000|   581|  8040.521| 86.989|  72,259|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   237| 132.620| N/A|24,670| 13804.758| N/A|1,787,065|
| |Ada County|    81| 168.194|  5.636| 8,949| 18582.312| 280.323| 481,587|
| |Canyon County|    48| 208.833|  6.837| 5,772| 25112.139| 617.797| 229,849|
| |Twin Falls County|    32| 368.333|  1.644| 1,412| 16252.676| 338.734|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   159|  3934.864| 102.526|  40,408|
| |Kootenai County|    16| 96.562|  2.586| 1,791| 10808.886| 187.088| 165,697|
| |Jerome County|     6| 245.781|  0.000|   474| 19416.680| 316.004|  24,412|
| |Blaine County|     6| 260.632|  0.000|   576| 25020.633| 43.439|  23,021|
| |Bonneville County|     4| 33.596|  2.400| 1,052|  8835.733| 411.550| 119,062|
| |Washington County|     3| 294.291| 14.014|   205| 20109.869| 224.222|  10,194|
| |Elmore County|     3| 109.047|  0.000|   212|  7706.009| 62.313|  27,511|
| |Owyhee County|     3| 253.743| 24.166|   263| 22244.777| 374.573|  11,823|
| |Bingham County|     2| 42.725|  0.000|   244|  5212.450| 198.366|  46,811|
| |Bannock County|     2| 22.777|  0.000|   391|  4452.897| 144.796|  87,808|
| |Minidoka County|     2| 95.062|  0.000|   478| 22719.711| 339.506|  21,039|
| |Payette County|     2| 83.504|  0.000|   384| 16032.733| 345.944|  23,951|
| |Shoshone County|     2| 155.255|  0.000|   100|  7762.770| 299.421|  12,882|
| |Cassia County|     1| 41.615|  0.000|   518| 21556.388| 273.468|  24,030|
| |Boise County|     1| 127.698|  0.000|    48|  6129.485| 182.425|   7,831|
| |Valley County|     1| 87.781|  0.000|    59|  5179.073| 163.022|  11,392|
| |Gem County|     1| 55.212|  7.887|   179|  9882.951| 220.848|  18,112|
| |Gooding County|     1| 65.880|  0.000|   162| 10672.640| 263.522|  15,179|
| |Jefferson County|     1| 33.477|  0.000|   198|  6628.503| 301.296|  29,871|
| |Bear Lake County|     0|  0.000|  0.000|    15|  2448.980| 209.913|   6,125|
| |Adams County|     0|  0.000|  0.000|    19|  4424.779| 33.269|   4,294|
| |Benewah County|     0|  0.000|  0.000|    64|  6883.201| 199.736|   9,298|
| |Custer County|     0|  0.000|  0.000|    10|  2317.497| 99.321|   4,315|
| |Clearwater County|     0|  0.000|  0.000|    16|  1827.318| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|     8|  9467.456| 1183.432|     845|
| |Caribou County|     0|  0.000|  0.000|    31|  4332.635| 159.728|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,597|
| |Boundary County|     0|  0.000|  0.000|    35|  2858.310| 23.333|  12,245|
| |Bonner County|     0|  0.000|  0.000|   183|  4000.962| 96.823|  45,739|
| |Teton County|     0|  0.000|  0.000|    82|  6753.418| 282.373|  12,142|
| |Power County|     0|  0.000|  0.000|    55|  7160.526| 241.784|   7,681|
| |Oneida County|     0|  0.000|  0.000|    13|  2869.124| 157.644|   4,531|
| |Lemhi County|     0|  0.000|  0.000|    25|  3114.489| 231.362|   8,027|
| |Latah County|     0|  0.000|  0.000|    99|  2468.335| 71.236|  40,108|
| |Madison County|     0|  0.000|  0.000|   165|  4134.613| 118.132|  39,907|
| |Lincoln County|     0|  0.000|  0.000|    56| 10436.079| 159.736|   5,366|
| |Lewis County|     0|  0.000|  0.000|     1|   260.552|  0.000|   3,838|
| |Idaho County|     0|  0.000|  0.000|    31|  1859.963| 17.143|  16,667|
| |Fremont County|     0|  0.000|  0.000|    84|  6412.703| 370.803|  13,099|
| |Franklin County|     0|  0.000|  0.000|    51|  3675.411| 41.181|  13,876|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   146| 165.035| N/A| 9,605| 10857.291| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  2.959| 4,422| 22896.020| 147.196| 193,134|
| |Pennington County|    32| 281.257|  3.767|   891|  7831.246| 81.615| 113,775|
| |Beadle County|     9| 487.726|  0.000|   593| 32135.696| 46.450|  18,453|
| |Todd County|     5| 491.304| 14.037|    69|  6779.994| 42.112|  10,177|
| |Union County|     4| 251.067|  0.000|   214| 13432.086| 161.400|  15,932|
| |Brown County|     3| 77.242|  0.000|   442| 11380.314| 128.737|  38,839|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556| 145.624|   1,962|
| |Oglala Lakota County|     2| 141.074| 10.077|   155| 10933.202| 70.537|  14,177|
| |Lyman County|     2| 528.961|  0.000|    90| 23803.227| 75.566|   3,781|
| |Lake County|     2| 156.287|  0.000|    94|  7345.472| 145.123|  12,797|
| |Yankton County|     2| 87.665|  0.000|   114|  4996.932| 75.142|  22,814|
| |Lincoln County|     2| 32.718|  0.000|   638| 10437.116| 156.580|  61,128|
| |Hughes County|     2| 114.116|  0.000|    93|  5306.402| 73.360|  17,526|
| |Roberts County|     1| 96.209|  0.000|    80|  7696.748| 137.442|  10,394|
| |Meade County|     1| 35.296|  0.000|    94|  3317.803| 100.845|  28,332|
| |Butte County|     1| 95.886|  0.000|    17|  1630.070| 82.188|  10,429|
| |Codington County|     1| 35.703|  5.100|   133|  4748.474| 76.506|  28,009|
| |Davison County|     1| 50.569|  7.224|    97|  4905.183| 65.017|  19,775|
| |Faulk County|     1| 434.972|  0.000|    26| 11309.265|  0.000|   2,299|
| |Jackson County|     1| 299.043|  0.000|    11|  3289.474| 85.441|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |McCook County|     1| 179.019|  0.000|    28|  5012.531| 102.297|   5,586|
| |Brookings County|     1| 28.509|  0.000|   137|  3905.693| 73.308|  35,077|
| |Moody County|     0|  0.000|  0.000|    32|  4866.180| 43.448|   6,576|
| |Turner County|     0|  0.000|  0.000|    51|  6083.015| 119.275|   8,384|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757| 120.098|   2,379|
| |Marshall County|     0|  0.000|  0.000|     9|  1823.708| 28.948|   4,935|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Potter County|     0|  0.000|  0.000|     1|   464.468|  0.000|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Spink County|     0|  0.000|  0.000|    25|  3920.954| 112.027|   6,376|
| |Stanley County|     0|  0.000|  0.000|    14|  4519.045|  0.000|   3,098|
| |Sully County|     0|  0.000|  0.000|     3|  2156.722| 205.402|   1,391|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565| 1399.544|   2,756|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Day County|     0|  0.000|  0.000|    23|  4240.413| 52.676|   5,424|
| |Aurora County|     0|  0.000|  0.000|    38| 13813.159|  0.000|   2,751|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Bon Homme County|     0|  0.000|  0.000|    13|  1883.785|  0.000|   6,901|
| |Brule County|     0|  0.000|  0.000|    45|  8495.375| 134.847|   5,297|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233| 103.821|   1,376|
| |Charles Mix County|     0|  0.000|  0.000|   105| 11300.043| 92.245|   9,292|
| |Clark County|     0|  0.000|  0.000|    16|  4282.655|  0.000|   3,736|
| |Clay County|     0|  0.000|  0.000|   128|  9097.370| 111.686|  14,070|
| |Corson County|     0|  0.000|  0.000|    33|  8076.358| 174.813|   4,086|
| |Custer County|     0|  0.000|  0.000|    35|  3901.025| 191.071|   8,972|
| |Deuel County|     0|  0.000|  0.000|    11|  2528.154| 98.500|   4,351|
| |Hanson County|     0|  0.000|  0.000|    21|  6081.668|  0.000|   3,453|
| |Dewey County|     0|  0.000|  0.000|    48|  8146.640|  0.000|   5,892|
| |Douglas County|     0|  0.000|  0.000|    17|  5819.925| 48.907|   2,921|
| |Edmunds County|     0|  0.000|  0.000|    15|  3917.472| 74.619|   3,829|
| |Fall River County|     0|  0.000|  0.000|    22|  3277.223| 127.684|   6,713|
| |Grant County|     0|  0.000|  0.000|    26|  3686.897| 60.773|   7,052|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Hamlin County|     0|  0.000|  0.000|    21|  3406.879| 162.232|   6,164|
| |Hand County|     0|  0.000|  0.000|     7|  2193.670|  0.000|   3,191|
| |Harding County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,298|
| |Hutchinson County|     0|  0.000|  0.000|    29|  3977.507| 58.781|   7,291|
| |Hyde County|     0|  0.000|  0.000|     3|  2305.919|  0.000|   1,301|
| |Kingsbury County|     0|  0.000|  0.000|    14|  2834.582| 57.849|   4,939|
| |Lawrence County|     0|  0.000|  0.000|    55|  2128.154| 138.192|  25,844|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   139| 77.561| N/A| 7,695|  4293.733| N/A|1,792,147|
| |Kanawha County|    23| 129.124|  1.604|   935|  5249.152| 90.627| 178,124|
| |Jackson County|    19| 664.894|  0.000|   162|  5669.093| 24.996|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   696|  5840.347| 49.149| 119,171|
| |Mercer County|    11| 187.209| 19.450|   196|  3335.716| 77.801|  58,758|
| |Wayne County|     9| 228.415|  0.000|   208|  5278.920| 87.015|  39,402|
| |Fayette County|     7| 165.071|  6.738|   148|  3490.072| 64.007|  42,406|
| |Mingo County|     5| 213.456| 18.296|   173|  7385.587| 280.543|  23,424|
| |Wood County|     5| 59.867|  1.710|   247|  2957.446| 20.526|  83,518|
| |Monongalia County|     5| 47.343|  0.000|   939|  8891.035| 31.111| 105,612|
| |Mineral County|     4| 148.876|  0.000|   121|  4503.499| 58.487|  26,868|
| |Preston County|     4| 119.646|  4.273|   125|  3738.933|  8.546|  33,432|
| |Ohio County|     4| 96.593|  0.000|   268|  6471.710| 55.196|  41,411|
| |Jefferson County|     4| 69.996|  0.000|   294|  5144.717| 12.499|  57,146|
| |Logan County|     3| 93.694|  0.000|   228|  7120.772| 356.931|  32,019|
| |Greenbrier County|     3| 86.550|  0.000|    93|  2683.053| 24.729|  34,662|
| |Cabell County|     3| 32.628|  1.554|   400|  4350.427| 111.868|  91,945|
| |Lewis County|     2| 125.731|  0.000|    29|  1823.097| 17.962|  15,907|
| |Marion County|     2| 35.668|  0.000|   191|  3406.335| 38.216|  56,072|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656| 16.791|   8,508|
| |Brooke County|     1| 45.581|  0.000|    64|  2917.179| 13.023|  21,939|
| |Barbour County|     1| 60.824|  0.000|    29|  1763.883|  0.000|  16,441|
| |Grant County|     1| 86.445| 12.349|   121| 10459.889| 543.371|  11,568|
| |Marshall County|     1| 32.754|  4.679|   131|  4290.721| 28.075|  30,531|
| |Mason County|     1| 37.713|  0.000|    56|  2111.932| 53.876|  26,516|
| |Wyoming County|     1| 49.034|  0.000|    31|  1520.055| 56.039|  20,394|
| |Roane County|     1| 73.057|  0.000|    15|  1095.850| 10.437|  13,688|
| |Nicholas County|     1| 40.823|  0.000|    37|  1510.451| 29.159|  24,496|
| |Pleasants County|     1| 134.048| 19.150|    13|  1742.627| 95.749|   7,460|
| |Pendleton County|     1| 143.493|  0.000|    40|  5739.704| 61.497|   6,969|
| |Hampshire County|     1| 43.150|  0.000|    76|  3279.396| 12.329|  23,175|
| |Harrison County|     1| 14.869|  0.000|   221|  3285.952| 59.474|  67,256|
| |Taylor County|     1| 59.898|  8.557|    56|  3354.298| 25.671|  16,695|
| |Raleigh County|     1| 13.631|  0.000|   253|  3448.699| 124.628|  73,361|
| |Tyler County|     0|  0.000|  0.000|    13|  1513.212| 16.629|   8,591|
| |Tucker County|     0|  0.000|  0.000|    10|  1462.202|  0.000|   6,839|
| |Wirt County|     0|  0.000|  0.000|     6|  1030.751|  0.000|   5,821|
| |Webster County|     0|  0.000|  0.000|     4|   492.975| 17.606|   8,114|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533| 11.818|  24,176|
| |Wetzel County|     0|  0.000|  0.000|    42|  2787.919|  9.483|  15,065|
| |Hardy County|     0|  0.000|  0.000|    58|  4210.221| 41.480|  13,776|
| |Hancock County|     0|  0.000|  0.000|   112|  3887.539| 59.503|  28,810|
| |Summers County|     0|  0.000|  0.000|    11|   874.891| 45.449|  12,573|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Randolph County|     0|  0.000|  0.000|   210|  7318.348| 14.935|  28,695|
| |Putnam County|     0|  0.000|  0.000|   195|  3454.384| 70.859|  56,450|
| |Pocahontas County|     0|  0.000|  0.000|    41|  4971.505|  0.000|   8,247|
| |Lincoln County|     0|  0.000|  0.000|    88|  4311.823| 139.994|  20,409|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921| 21.523|  13,275|
| |McDowell County|     0|  0.000|  0.000|    62|  3517.930| 202.646|  17,624|
| |Morgan County|     0|  0.000|  0.000|    28|  1565.645| 15.976|  17,884|
| |Gilmer County|     0|  0.000|  0.000|    16|  2045.251|  0.000|   7,823|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227| 33.820|   8,448|
| |Calhoun County|     0|  0.000|  0.000|     6|   844.001|  0.000|   7,109|
| |Boone County|     0|  0.000|  0.000|   101|  4707.089| 159.788|  21,457|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   125| 92.991| N/A| 4,042|  3006.966| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.484| 2,088|  7077.894| 17.433| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   673|  3241.171| 12.384| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   170|  1390.002|  3.504| 122,302|
| |Androscoggin County|     8| 73.885|  1.319|   563|  5199.627| 17.152| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   152|   999.027|  3.756| 152,148|
| |Franklin County|     1| 33.114|  0.000|    45|  1490.116|  0.000|  30,199|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  2.130|  67,055|
| |Hancock County|     1| 18.186|  0.000|    35|   636.514|  2.598|  54,987|
| |Somerset County|     1| 19.808|  0.000|    33|   653.672|  0.000|  50,484|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  4.125|  34,634|
| |Knox County|     1| 25.143|  0.000|    27|   678.870|  3.592|  39,772|
| |Oxford County|     0|  0.000|  0.000|    53|   914.187|  0.000|  57,975|
| |Washington County|     0|  0.000|  0.000|    13|   414.290| 18.211|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    56|  1561.803| 23.905|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|     4|   238.308|  8.511|  16,785|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   112| 146.970| N/A| 7,577|  9942.761| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,039| 16704.870| 91.876| 181,923|
| |Grand Forks County|     6| 86.392|  2.057|   677|  9747.880| 104.904|  69,451|
| |Burleigh County|     6| 62.744|  1.494| 1,171| 12245.624| 313.722|  95,626|
| |Morton County|     3| 95.651|  0.000|   367| 11701.314| 432.707|  31,364|
| |Stark County|     3| 95.271|  0.000|   261|  8288.609| 313.034|  31,489|
| |Williams County|     2| 53.207|  0.000|   270|  7182.952| 152.020|  37,589|
| |Stutsman County|     2| 96.600|  0.000|   127|  6134.080| 82.800|  20,704|
| |Ramsey County|     2| 173.626|  0.000|    69|  5990.103| 322.449|  11,519|
| |Benson County|     2| 292.740| 20.910|   136| 19906.323| 878.220|   6,832|
| |McIntosh County|     2| 800.961| 57.212|    30| 12014.417| 343.269|   2,497|
| |Richland County|     1| 61.816|  8.831|   109|  6737.961| 150.125|  16,177|
| |Sioux County|     1| 236.407| 33.772|    83| 19621.749| 844.309|   4,230|
| |Ward County|     1| 14.784|  0.000|   222|  3282.033| 95.040|  67,641|
| |Mountrail County|     1| 94.832|  0.000|   130| 12328.118| 203.211|  10,545|
| |Emmons County|     1| 308.547|  0.000|    17|  5245.295| 88.156|   3,241|
| |Griggs County|     1| 448.229| 64.033|    34| 15239.803| 256.131|   2,231|
| |McHenry County|     1| 174.064|  0.000|    16|  2785.030| 49.733|   5,745|
| |McKenzie County|     1| 66.560|  0.000|    89|  5923.855| 95.086|  15,024|
| |McLean County|     0|  0.000|  0.000|    61|  6455.026| 362.812|   9,450|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Adams County|     0|  0.000|  0.000|     2|   902.527|  0.000|   2,216|
| |Barnes County|     0|  0.000|  0.000|    37|  3552.568| 54.866|  10,415|
| |Billings County|     0|  0.000|  0.000|     2|  2155.172|  0.000|     928|
| |Bowman County|     0|  0.000|  0.000|     6|  1984.127|  0.000|   3,024|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784| 154.440|   1,850|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704| 270.179|   2,115|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Dickey County|     0|  0.000|  0.000|    13|  2668.309| 58.644|   4,872|
| |Nelson County|     0|  0.000|  0.000|    25|  8683.571| 396.963|   2,879|
| |Pierce County|     0|  0.000|  0.000|    12|  3018.868| 35.939|   3,975|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041| 54.756|   5,218|
| |Renville County|     0|  0.000|  0.000|     9|  3867.641|  0.000|   2,327|
| |Rolette County|     0|  0.000|  0.000|    72|  5079.007| 393.018|  14,176|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418| 73.298|   3,898|
| |Sheridan County|     0|  0.000|  0.000|     8|  6083.650| 325.910|   1,315|
| |Slope County|     0|  0.000|  0.000|     3|  4000.000|  0.000|     750|
| |Steele County|     0|  0.000|  0.000|    14|  7407.407| 302.343|   1,890|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Traill County|     0|  0.000|  0.000|    55|  6844.201| 231.103|   8,036|
| |Walsh County|     0|  0.000|  0.000|   104|  9773.518| 80.551|  10,641|
| |Mercer County|     0|  0.000|  0.000|    29|  3542.201| 104.696|   8,187|
| |Divide County|     0|  0.000|  0.000|     2|   883.392| 63.099|   2,264|
| |Dunn County|     0|  0.000|  0.000|    30|  6781.193| 32.291|   4,424|
| |Eddy County|     0|  0.000|  0.000|    18|  7870.573| 312.324|   2,287|
| |Foster County|     0|  0.000|  0.000|    25|  7788.162| 356.030|   3,210|
| |Golden Valley County|     0|  0.000|  0.000|     4|  2271.437|  0.000|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Hettinger County|     0|  0.000|  0.000|     6|  2400.960|  0.000|   2,499|
| |Kidder County|     0|  0.000|  0.000|    14|  5645.161| 172.811|   2,480|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523| 70.616|   4,046|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Wells County|     0|  0.000|  0.000|    21|  5477.308| 223.564|   3,834|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    75| 70.174| N/A| 4,952|  4633.329| N/A|1,068,778|
| |Yellowstone County|    30| 185.989|  3.543| 1,285|  7966.522| 165.619| 161,300|
| |Big Horn County|    13| 976.049| 42.903|   428| 32134.545| 965.323|  13,319|
| |Toole County|     6| 1266.892|  0.000|    45|  9501.689| 422.297|   4,736|
| |Cascade County|     4| 49.161|  3.511|   166|  2040.164| 35.115|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   939|  8205.603| 86.138| 114,434|
| |Lincoln County|     2| 100.100|  0.000|    77|  3853.854| 50.050|  19,980|
| |Hill County|     2| 121.330| 17.333|    42|  2547.925| 17.333|  16,484|
| |Richland County|     2| 185.134| 13.224|    47|  4350.643| 13.224|  10,803|
| |Flathead County|     2| 19.267|  0.000|   330|  3179.007| 92.205| 103,806|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939| 112.762|  11,402|
| |Madison County|     1| 116.279|  0.000|    84|  9767.442| 149.502|   8,600|
| |Glacier County|     1| 72.711|  0.000|    74|  5380.644| 186.972|  13,753|
| |Lake County|     1| 32.832|  0.000|   180|  5909.777| 65.664|  30,458|
| |Lewis and Clark County|     1| 14.403|  0.000|   158|  2275.608| 55.553|  69,432|
| |Rosebud County|     1| 111.894|  0.000|    34|  3804.409| 191.819|   8,937|
| |Sweet Grass County|     1| 267.594|  0.000|     5|  1337.972| 38.228|   3,737|
| |Missoula County|     1|  8.361|  0.000|   329|  2750.836| 75.251| 119,600|
| |Ravalli County|     1| 22.828|  0.000|    83|  1894.718| 35.872|  43,806|
| |Stillwater County|     1| 103.713| 14.816|    26|  2696.536| 103.713|   9,642|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |McCone County|     0|  0.000|  0.000|     3|  1802.885| 171.703|   1,664|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Jefferson County|     0|  0.000|  0.000|    28|  2291.138| 35.068|  12,221|
| |Granite County|     0|  0.000|  0.000|    16|  4735.129| 380.501|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Fergus County|     0|  0.000|  0.000|    13|  1176.471| 90.498|  11,050|
| |Deer Lodge County|     0|  0.000|  0.000|    25|  2735.230| 78.149|   9,140|
| |Dawson County|     0|  0.000|  0.000|    17|  1973.761| 16.586|   8,613|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148| 84.531|   1,690|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    15|  2028.123| 38.631|   7,396|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Mineral County|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,397|
| |Park County|     0|  0.000|  0.000|    55|  3312.056| 60.219|  16,606|
| |Broadwater County|     0|  0.000|  0.000|    12|  1924.002| 45.810|   6,237|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Musselshell County|     0|  0.000|  0.000|     3|   647.529| 30.835|   4,633|
| |Silver Bow County|     0|  0.000|  0.000|    88|  2520.407| 90.015|  34,915|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031| 86.345|   3,309|
| |Sanders County|     0|  0.000|  0.000|     9|   743.003|  0.000|  12,113|
| |Roosevelt County|     0|  0.000|  0.000|    23|  2090.149| 51.929|  11,004|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505| 132.644|   1,077|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937| 48.336|   5,911|
| |Phillips County|     0|  0.000|  0.000|    28|  7081.437| 1011.634|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623| 76.055|   5,635|
| |Carbon County|     0|  0.000|  0.000|    69|  6433.566| 146.520|  10,725|
| |Blaine County|     0|  0.000|  0.000|    10|  1496.782| 21.383|   6,681|
| |Beaverhead County|     0|  0.000|  0.000|    64|  6770.337| 256.910|   9,453|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,451|  2325.362| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   729|  4451.256|  7.851| 163,774|
| |Franklin County|     7| 141.695|  2.892|   118|  2388.567|  2.892|  49,402|
| |Windham County|     3| 71.053|  0.000|   102|  2415.802|  3.383|  42,222|
| |Addison County|     2| 54.382|  0.000|    73|  1984.936|  3.884|  36,777|
| |Windsor County|     2| 36.323|  0.000|    72|  1307.617|  2.594|  55,062|
| |Washington County|     2| 34.241|  0.000|    53|   907.394|  9.783|  58,409|
| |Rutland County|     1| 17.185|  0.000|    99|  1701.294| 24.550|  58,191|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  5.633|  25,362|
| |Bennington County|     1| 28.193|  0.000|    87|  2452.777| 12.083|  35,470|
| |Orleans County|     0|  0.000|  0.000|    14|   517.809|  0.000|  27,037|
| |Orange County|     0|  0.000|  0.000|    14|   484.563|  0.000|  28,892|
| |Caledonia County|     0|  0.000|  0.000|    28|   933.551|  9.526|  29,993|
| |Essex County|     0|  0.000|  0.000|     6|   973.552| 46.360|   6,163|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    30| 21.188| N/A| 3,475|  2454.318| N/A|1,415,872|
| |Honolulu County|    24| 24.626| N/A| 3,111|  3192.200| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   185|  1105.025| 11.946| 167,417|
| |Kauai County|     0|  0.000|  0.000|    48|   663.965|  1.976|  72,293|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Hawaii County|     0|  0.000|  0.000|   131|   650.082| 11.343| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,050|  5269.896| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    23|  2723.505| 16.916|   8,445|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Crook County|     0|  0.000|  0.000|    10|  1318.565| 18.837|   7,584|
| |Converse County|     0|  0.000|  0.000|    32|  2315.150| 10.335|  13,822|
| |Carbon County|     0|  0.000|  0.000|    99|  6689.189| 202.703|  14,800|
| |Sheridan County|     0|  0.000|  0.000|    74|  2427.423| 65.606|  30,485|
| |Platte County|     0|  0.000|  0.000|     5|   595.735|  0.000|   8,393|
| |Park County|     0|  0.000|  0.000|   134|  4589.984| 83.187|  29,194|
| |Natrona County|     0|  0.000|  0.000|   231|  2892.634| 26.833|  79,858|
| |Lincoln County|     0|  0.000|  0.000|   103|  5194.150| 79.245|  19,830|
| |Laramie County|     0|  0.000|  0.000|   502|  5045.226| 41.637|  99,500|
| |Hot Springs County|     0|  0.000|  0.000|    22|  4985.271| 129.488|   4,413|
| |Goshen County|     0|  0.000|  0.000|    28|  2119.446| 140.575|  13,211|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762| 43.594|   9,831|
| |Campbell County|     0|  0.000|  0.000|   123|  2654.237| 15.414|  46,341|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253| 12.117|  11,790|
| |Albany County|     0|  0.000|  0.000|    88|  2263.374|  3.674|  38,880|
| |Sweetwater County|     0|  0.000|  0.000|   259|  6116.714| 40.486|  42,343|
| |Fremont County|     0|  0.000|  0.000|   504| 12837.167| 105.521|  39,261|
| |Washakie County|     0|  0.000|  0.000|    77|  9865.471| 512.492|   7,805|
| |Uinta County|     0|  0.000|  0.000|   278| 13744.685| 113.009|  20,226|
| |Teton County|     0|  0.000|  0.000|   374| 15939.311| 121.767|  23,464|
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
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Lake and Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,592|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Kusilvak Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   8,314|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Ketchikan Gateway Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,901|
| |Kodiak Island Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,998|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|


