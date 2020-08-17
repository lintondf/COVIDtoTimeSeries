# Analysis of US By County #

Updated: at 2020-08-17

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 136,033 deaths (471.255 deaths/million) and 4,642,134 confirmed cases (16081.552 confirmed cases/million).  This group accounts for 81.21% of all US deaths and for 87.45% of all US cases.

24.34% of this group's deaths (19.76% of the total US deaths) occured in 13 counties in 10 states with a combined population of 37,287,218 (11.36% of the total US population):



The next 25.18% of this group's deaths (20.45% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,435 (12.66% of the total US population):



The next 25.45% of this group's deaths (20.67% of the total US deaths) occured in 93 counties in 31 states with a combined population of 70,415,402 (21.45% of the total US population)

The remaining 25.03% of this group's deaths (20.33% of the total US deaths) occured in 850 counties in 50 states with a combined population of 139,391,004 (42.47% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 10,978 deaths (277.380 deaths/million) and 496,064 confirmed cases (12534.002 confirmed cases/million).  This group accounts for 6.55% of all US deaths and for 9.34% of all US cases.

24.80% of this group's deaths (1.63% of the total US deaths) occured in 61 counties in 16 states with a combined population of 2,075,887 (0.63% of the total US population):



The next 25.12% of this group's deaths (1.65% of the total US deaths) occured in 119 counties in 28 states with a combined population of 3,500,866 (1.07% of the total US population):



The next 25.06% of this group's deaths (1.64% of the total US deaths) occured in 239 counties in 34 states with a combined population of 5,850,985 (1.78% of the total US population)

The remaining 25.01% of this group's deaths (1.64% of the total US deaths) occured in 1,733 counties in 47 states with a combined population of 28,149,726 (8.58% of the total US population) 

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
|NJ|21 counties|15,912| 1791.450| N/A|187,013| 21054.830| N/A|8,882,190|
| |Essex County| 2,110| 2640.884|  0.000|19,927| 24940.705| 35.581| 798,975|
| |Bergen County| 2,036| 2184.076|  0.000|21,195| 22736.488| 61.452| 932,202|
| |Hudson County| 1,508| 2242.743|  0.850|19,892| 29583.977| 46.954| 672,391|
| |Middlesex County| 1,415| 1715.023|  2.078|18,099| 21936.533| 31.166| 825,062|
| |Union County| 1,349| 2424.772|  0.000|16,869| 30321.332| 44.680| 556,341|
| |Passaic County| 1,244| 2478.947|  1.139|17,950| 35769.370| 87.680| 501,826|
| |Ocean County| 1,020| 1679.881|  0.471|10,752| 17707.918| 36.703| 607,186|
| |Monmouth County|   858| 1386.566|  0.462|10,474| 16926.446| 39.709| 618,795|
| |Morris County|   830| 1687.524|  0.290| 7,341| 14925.434| 27.012| 491,845|
| |Mercer County|   622| 1692.839|  1.166| 8,190| 22289.960| 27.605| 367,430|
| |Camden County|   582| 1149.128|  0.564| 8,793| 17361.310| 65.157| 506,471|
| |Somerset County|   565| 1717.670|  1.737| 5,307| 16133.936| 26.927| 328,934|
| |Burlington County|   477| 1071.070|  1.283| 6,145| 13798.167| 44.267| 445,349|
| |Atlantic County|   253| 959.533|  0.542| 3,585| 13596.541| 66.100| 263,670|
| |Gloucester County|   215| 737.220|  1.470| 3,413| 11702.945| 80.825| 291,636|
| |Sussex County|   198| 1409.373|  0.000| 1,351|  9616.480| 21.354| 140,488|
| |Warren County|   172| 1633.940|  0.000| 1,365| 12967.027| 27.142| 105,267|
| |Cumberland County|   158| 1056.665|  0.000| 3,427| 22918.938| 85.030| 149,527|
| |Hunterdon County|   124| 997.017|  0.000| 1,161|  9334.974| 13.784| 124,371|
| |Cape May County|    89| 966.981|  3.104|   847|  9202.621| 23.282|  92,039|
| |Salem County|    87| 1394.566|  0.000|   930| 14907.430| 82.437|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,343| 634.510| N/A|255,246| 13120.788| N/A|19,453,561|
| |Nassau County| 2,195| 1617.629|  0.105|43,929| 32373.958| 28.847|1,356,924|
| |Suffolk County| 1,998| 1353.108|  0.000|44,159| 29905.845| 36.087|1,476,601|
| |Westchester County| 1,447| 1495.598|  0.000|36,453| 37677.286| 36.618| 967,506|
| |Queens County|   986| 437.524|  0.958| 7,951|  3527.765| 20.096|2,253,858|
| |Kings County|   932| 364.053|  0.797| 1,365|   533.061|  3.037|2,559,903|
| |Erie County|   674| 733.644|  0.466| 9,147|  9956.439| 37.786| 918,702|
| |Rockland County|   674| 2068.824|  0.000|14,007| 42994.085| 28.502| 325,789|
| |Bronx County|   650| 458.410|  1.004|27,078| 19092.831| 108.763|1,418,207|
| |Orange County|   491| 1275.523|  0.000|11,254| 29235.725| 35.256| 384,940|
| |New York County|   415| 254.818|  0.558|15,617|  9588.421| 54.621|1,628,706|
| |Monroe County|   285| 384.216|  0.000| 5,165|  6963.075| 40.251| 741,770|
| |Onondaga County|   203| 440.798|  0.931| 3,674|  7977.799| 30.400| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,686| 15926.966| 38.358| 294,218|
| |Richmond County|   148| 311.423|  0.682| 7,951| 16698.938| 95.126| 476,143|
| |Albany County|   129| 422.250|  0.468| 2,654|  8687.227| 27.589| 305,506|
| |Oneida County|   117| 511.652|  1.249| 2,198|  9612.063| 32.486| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,532|  7320.301| 23.209| 209,281|
| |Ulster County|    92| 518.097|  0.000| 2,095| 11797.965| 26.548| 177,573|
| |Broome County|    69| 362.228|  0.000| 1,166|  6121.120| 29.998| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,461| 14859.642| 17.436|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   301|  7459.358| 10.621|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,493| 19792.661|  7.575|  75,432|
| |Steuben County|    42| 440.349|  0.000|   306|  3208.253| 11.982|  95,379|
| |Rensselaer County|    38| 239.424|  7.201|   795|  5009.010| 27.003| 158,714|
| |Columbia County|    37| 622.257|  0.000|   552|  9283.396| 28.830|  59,461|
| |Schenectady County|    37| 238.250|  0.000| 1,119|  7205.455| 56.113| 155,299|
| |Ontario County|    34| 309.719|  0.000|   368|  3352.250| 10.411| 109,777|
| |Warren County|    33| 516.077|  0.000|   312|  4879.269|  8.936|  63,944|
| |Tioga County|    25| 518.640|  0.000|   195|  4045.391|  5.927|  48,203|
| |Fulton County|    24| 449.581|  0.000|   303|  5675.964| 18.733|  53,383|
| |Greene County|    18| 381.453|  0.000|   298|  6315.165| 18.164|  47,188|
| |Madison County|    17| 239.636|  0.000|   421|  5934.509| 18.124|  70,941|
| |Saratoga County|    17| 73.957|  0.000|   792|  3445.531| 21.752| 229,863|
| |Washington County|    14| 228.743|  0.000|   261|  4264.427|  4.668|  61,204|
| |Chautauqua County|     9| 70.920|  0.000|   263|  2072.449| 11.257| 126,903|
| |Livingston County|     8| 127.158|  0.000|   178|  2829.259|  4.541|  62,914|
| |Yates County|     7| 280.978|  0.000|    59|  2368.241| 11.468|  24,913|
| |Cattaraugus County|     6| 78.826|  0.000|   171|  2246.542| 11.261|  76,117|
| |Chenango County|     6| 127.100|  0.000|   218|  4617.959|  6.052|  47,207|
| |Wyoming County|     5| 125.442|  0.000|   118|  2960.436|  0.000|  39,859|
| |Genesee County|     5| 87.291|  0.000|   285|  4975.559| 19.952|  57,280|
| |Otsego County|     5| 84.044|  0.000|   118|  1983.427|  4.802|  59,493|
| |St. Lawrence County|     4| 37.126|  0.000|   263|  2441.062|  0.000| 107,740|
| |Herkimer County|     4| 65.233|  0.000|   283|  4615.209| 20.968|  61,319|
| |Delaware County|     4| 90.631|  0.000|   107|  2424.380|  6.474|  44,135|
| |Clinton County|     4| 49.699|  0.000|   132|  1640.057|  8.875|  80,485|
| |Montgomery County|     4| 81.266|  0.000|   187|  3799.191| 31.926|  49,221|
| |Seneca County|     3| 88.194|  0.000|    93|  2734.008| 16.799|  34,016|
| |Wayne County|     3| 33.364|  0.000|   269|  2991.615| 30.186|  89,918|
| |Chemung County|     3| 35.947|  0.000|   189|  2264.666| 30.812|  83,456|
| |Oswego County|     3| 25.614|  0.000|   271|  2313.787| 21.955| 117,124|
| |Cayuga County|     2| 26.118|  0.000|   164|  2141.663| 22.387|  76,576|
| |Allegany County|     1| 21.696|  0.000|    80|  1735.697|  3.099|  46,091|
| |Hamilton County|     0|  0.000|  0.000|    11|  2490.942| 97.050|   4,416|
| |Jefferson County|     0|  0.000|  0.000|   143|  1301.965|  1.301| 109,834|
| |Lewis County|     0|  0.000|  0.000|    47|  1787.344| 32.596|  26,296|
| |Tompkins County|     0|  0.000|  0.000|   238|  2329.223|  5.592| 102,180|
| |Schoharie County|     0|  0.000|  0.000|    69|  2225.878|  0.000|  30,999|
| |Essex County|     0|  0.000|  0.000|    59|  1599.566| 15.492|  36,885|
| |Cortland County|     0|  0.000|  0.000|    97|  2038.629|  6.005|  47,581|
| |Schuyler County|     0|  0.000|  0.000|    23|  1291.627|  8.023|  17,807|
| |Franklin County|     0|  0.000|  0.000|    54|  1079.525|  0.000|  50,022|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties|11,243| 284.545| N/A|623,873| 15789.367| N/A|39,512,223|
| |Los Angeles County| 5,254| 523.353|  3.942|221,971| 22110.632| 190.797|10,039,107|
| |Riverside County|   881| 356.601|  4.742|45,662| 18482.554| 301.264|2,470,546|
| |Orange County|   810| 255.063|  3.779|43,709| 13763.614| 182.997|3,175,692|
| |San Diego County|   626| 187.519|  1.412|34,344| 10287.779| 86.185|3,338,330|
| |San Bernardino County|   568| 260.540|  1.442|41,124| 18863.485| 354.639|2,180,085|
| |San Joaquin County|   261| 342.453|  9.372|14,651| 19223.300| 440.109| 762,148|
| |Imperial County|   257| 1418.205| 10.248|10,058| 55503.132| 287.740| 181,215|
| |Alameda County|   221| 132.230|  1.111|14,973|  8958.739| 150.436|1,671,329|
| |Santa Clara County|   209| 108.411|  0.371|14,207|  7369.342| 186.736|1,927,852|
| |Tulare County|   205| 439.730|  2.758|12,105| 25965.529| 499.484| 466,195|
| |Kern County|   204| 226.616|  5.237|26,570| 29515.598| 474.021| 900,202|
| |Fresno County|   203| 203.183|  4.576|19,900| 19917.906| 373.193| 999,101|
| |Sacramento County|   199| 128.217|  3.498|13,615|  8772.224| 259.563|1,552,058|
| |Stanislaus County|   198| 359.569|  9.339|12,379| 22480.296| 704.090| 550,660|
| |Contra Costa County|   157| 136.104|  2.229|11,228|  9733.634| 253.385|1,153,526|
| |San Mateo County|   126| 164.368|  1.118| 6,952|  9068.934| 156.914| 766,573|
| |Ventura County|    95| 112.292|  1.013| 9,090| 10744.605| 159.404| 846,006|
| |Merced County|    89| 320.513| 12.862| 6,777| 24405.791| 908.034| 277,680|
| |Marin County|    82| 316.815|  1.656| 5,750| 22215.697| 233.472| 258,826|
| |Santa Barbara County|    77| 172.453|  2.560| 7,274| 16291.190| 182.371| 446,499|
| |San Francisco County|    69| 78.271| N/A| 8,292|  9406.170| N/A| 881,549|
| |Kings County|    66| 431.542|  9.341| 5,409| 35366.811| 892.974| 152,940|
| |Sonoma County|    54| 109.237|  2.023| 4,293|  8684.377| 212.984| 494,336|
| |Madera County|    47| 298.741|  7.264| 2,924| 18585.494| 564.793| 157,327|
| |Yolo County|    46| 208.617|  1.944| 2,019|  9156.463| 193.068| 220,500|
| |Monterey County|    46| 105.976|  3.620| 6,461| 14885.005| 384.409| 434,061|
| |Solano County|    41| 91.591|  0.319| 4,596| 10267.110| 180.948| 447,643|
| |Placer County|    28| 70.294|  2.869| 2,582|  6482.079| 142.022| 398,329|
| |San Luis Obispo County|    18| 63.579|  1.514| 2,439|  8614.996| 174.591| 283,111|
| |Butte County|    12| 54.748|  2.607| 1,370|  6250.399| 179.235| 219,186|
| |Amador County|    11| 276.716| 32.343|   208|  5232.441| 158.123|  39,752|
| |Napa County|    11| 79.858|  1.037| 1,206|  8755.372| 165.939| 137,744|
| |Shasta County|    10| 55.531|  0.000|   488|  2709.907| 55.531| 180,080|
| |Mendocino County|    10| 115.275|  0.000|   537|  6190.273| 174.559|  86,749|
| |Santa Cruz County|     7| 25.621|  0.523| 1,454|  5321.855| 112.942| 273,213|
| |Sutter County|     7| 72.187|  0.000| 1,094| 11281.723| 223.926|  96,971|
| |Colusa County|     5| 232.051|  6.630|   409| 18981.761| 311.611|  21,547|
| |Inyo County|     5| 277.177| 15.839|   127|  7040.302| 300.935|  18,039|
| |San Benito County|     4| 63.686|  0.000|   828| 13183.034| 257.019|  62,808|
| |Yuba County|     4| 50.847|  0.000|   758|  9635.430| 286.920|  78,668|
| |Humboldt County|     4| 29.508|  0.000|   309|  2279.467| 28.454| 135,558|
| |Glenn County|     3| 105.660|  0.000|   407| 14334.519| 236.477|  28,393|
| |Nevada County|     2| 20.049|  1.432|   373|  3739.161| 73.036|  99,755|
| |Mariposa County|     2| 116.259|  0.000|    64|  3720.281| 24.913|  17,203|
| |Tuolumne County|     2| 36.712|  0.000|   160|  2936.965| 20.978|  54,478|
| |El Dorado County|     2| 10.371|  0.741|   827|  4288.463| 72.598| 192,843|
| |Lake County|     2| 31.063|  0.000|   268|  4162.396| 106.501|  64,386|
| |Mono County|     1| 69.233|  0.000|   160| 11077.264| 59.342|  14,444|
| |Calaveras County|     1| 21.784|  0.000|   174|  3790.437| 84.024|  45,905|
| |Tehama County|     1| 15.365|  0.000|   318|  4885.993| 92.189|  65,084|
| |Trinity County|     0|  0.000|  0.000|     8|   651.201| 34.886|  12,285|
| |Siskiyou County|     0|  0.000|  0.000|   111|  2549.438| 59.060|  43,539|
| |Sierra County|     0|  0.000|  0.000|     6|  1996.672| 142.619|   3,005|
| |Plumas County|     0|  0.000|  0.000|    39|  2073.696| 37.980|  18,807|
| |Modoc County|     0|  0.000|  0.000|     5|   565.547|  0.000|   8,841|
| |Lassen County|     0|  0.000|  0.000|   703| 22994.145| 303.723|  30,573|
| |Del Norte County|     0|  0.000|  0.000|   106|  3811.304| 35.956|  27,812|
| |Alpine County|     0|  0.000|  0.000|     2|  1771.479|  0.000|   1,129|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties|10,396| 358.534| N/A|555,394| 19154.238| N/A|28,995,881|
| |Harris County| 1,829| 388.049|  7.699|92,253| 19572.807| 196.889|4,713,325|
| |Hidalgo County|   955| 1099.335| 24.338|22,013| 25339.959| 373.626| 868,707|
| |Bexar County|   892| 445.209|  7.843|44,052| 21986.929| 90.482|2,003,554|
| |Dallas County|   825| 313.032|  3.794|63,428| 24066.634| 474.507|2,635,516|
| |Cameron County|   560| 1323.367| 43.887|17,816| 42101.980| 515.168| 423,163|
| |Tarrant County|   504| 239.713|  3.873|35,310| 16794.173| 246.168|2,102,515|
| |El Paso County|   358| 426.577| 11.064|18,350| 21865.073| 347.594| 839,238|
| |Travis County|   335| 262.961|  4.149|24,144| 18952.019| 159.234|1,273,954|
| |Nueces County|   287| 792.174| 20.110|17,044| 47044.665| 709.763| 362,294|
| |Fort Bend County|   194| 239.008|  5.632|12,228| 15064.902| 474.320| 811,688|
| |Webb County|   193| 697.627| 12.393| 9,552| 34527.132| 859.254| 276,652|
| |Galveston County|   125| 365.349|  5.010| 9,937| 29043.751| 234.241| 342,139|
| |Brazoria County|   111| 296.582|  6.871| 8,148| 21770.729| 301.926| 374,264|
| |Denton County|   104| 117.222|  2.737| 8,300|  9355.201| 105.628| 887,207|
| |Williamson County|   103| 174.413|  2.419| 7,330| 12412.137| 262.467| 590,551|
| |Montgomery County|   103| 169.578|  4.234| 6,957| 11453.907| 89.375| 607,391|
| |Collin County|    98| 94.711|  1.243|10,007|  9671.122| 324.860|1,034,730|
| |Jefferson County|    94| 373.661|  5.679| 6,247| 24832.548| 208.410| 251,565|
| |Starr County|    93| 1438.893| 55.257| 2,422| 37473.117| 576.884|  64,633|
| |Lubbock County|    80| 257.592|  3.220| 6,528| 21019.484| 234.592| 310,569|
| |Comal County|    80| 512.134| 10.060| 2,132| 13648.381| 267.956| 156,209|
| |McLennan County|    62| 241.600|  3.897| 5,322| 20738.593| 209.312| 256,623|
| |Guadalupe County|    59| 353.617|  3.425| 1,799| 10782.334| 102.746| 166,847|
| |Ector County|    59| 354.945|  2.578| 3,771| 22686.391| 206.263| 166,223|
| |Victoria County|    57| 619.000| 23.271| 3,584| 38920.985| 210.987|  92,084|
| |Angelina County|    54| 622.730| 14.827| 1,906| 21980.050| 181.218|  86,715|
| |Maverick County|    54| 919.587| 26.760| 2,596| 44208.304| 669.012|  58,722|
| |Midland County|    53| 299.720|  4.039| 2,888| 16331.886| 239.129| 176,832|
| |Ellis County|    51| 275.935|  7.729| 3,255| 17611.159| 309.171| 184,826|
| |Brazos County|    51| 222.502|  1.870| 4,185| 18258.286| 81.023| 229,211|
| |Val Verde County|    49| 999.490|  0.000| 1,693| 34533.401|  0.000|  49,025|
| |Bell County|    49| 135.014|  4.330| 4,281| 11795.858| 177.133| 362,924|
| |Potter County|    46| 391.773|  2.433| 3,802| 32380.871| 171.553| 117,415|
| |Hays County|    46| 199.834|  4.965| 5,111| 22203.301| 61.440| 230,191|
| |Walker County|    43| 589.275|  3.915| 3,189| 43702.293| 360.221|  72,971|
| |Nacogdoches County|    43| 659.469|  2.191| 1,202| 18434.452| 120.501|  65,204|
| |Washington County|    41| 1142.634|  7.963|   526| 14659.161| 43.794|  35,882|
| |Bowie County|    39| 418.253| 10.724|   790|  8472.304| 39.834|  93,245|
| |Liberty County|    36| 408.075|  3.239| 1,115| 12639.001| 221.850|  88,219|
| |Matagorda County|    35| 955.162| 31.189|   831| 22678.274| 354.774|  36,643|
| |San Patricio County|    34| 509.516| 17.127| 1,114| 16694.141| 383.207|  66,730|
| |Smith County|    34| 146.079|  6.752| 2,750| 11815.202| 138.714| 232,751|
| |Johnson County|    34| 193.383|  3.250| 2,159| 12279.814| 242.135| 175,817|
| |Tom Green County|    34| 285.235|  9.588| 2,903| 24354.027| 324.784| 119,200|
| |Gregg County|    32| 258.179|  6.916| 1,646| 13280.084| 265.095| 123,945|
| |Kaufman County|    32| 235.028|  7.345| 2,446| 17964.951| 302.179| 136,154|
| |Medina County|    32| 620.347| 16.616|   987| 19133.840| 487.416|  51,584|
| |Hale County|    31| 927.977| 21.382| 1,478| 44243.549| 825.344|  33,406|
| |Willacy County|    30| 1404.626|  6.689|   767| 35911.602| 494.963|  21,358|
| |Wharton County|    30| 721.917| 17.189| 1,019| 24521.128| 1058.812|  41,556|
| |Caldwell County|    29| 664.163|  9.815| 1,179| 27001.649| 111.239|  43,664|
| |Orange County|    29| 347.739| 15.417| 1,579| 18933.762| 174.726|  83,396|
| |Taylor County|    29| 210.093|  6.210| 1,156|  8374.748| 31.048| 138,034|
| |Grimes County|    27| 934.903| 19.786|   932| 32271.468| 277.008|  28,880|
| |Lavaca County|    25| 1240.449| 56.706|   641| 31805.101| 99.236|  20,154|
| |Randall County|    25| 181.537|  4.149| 1,899| 13789.548| 180.500| 137,713|
| |Harrison County|    24| 360.615|  2.147|   735| 11043.830| 90.154|  66,553|
| |Bastrop County|    23| 259.234|  3.220| 1,448| 16320.458| 136.863|  88,723|
| |Hunt County|    21| 212.995|  0.000| 1,284| 13023.105| 147.792|  98,594|
| |DeWitt County|    21| 1041.667| 14.172|   745| 36954.365| 368.481|  20,160|
| |Wilson County|    20| 391.619|  2.797|   499|  9770.903| 167.837|  51,070|
| |Parker County|    20| 139.980|  1.000| 1,401|  9805.568| 175.974| 142,878|
| |Atascosa County|    19| 371.435|  2.793|   517| 10106.934| 223.419|  51,153|
| |Jim Wells County|    19| 469.344| 14.116|   824| 20354.726| 352.891|  40,482|
| |Lamar County|    19| 381.075|  2.865|   705| 14139.874| 174.779|  49,859|
| |Kleberg County|    18| 586.701| 46.564|   489| 15938.722| 256.100|  30,680|
| |Shelby County|    18| 712.194|  0.000|   411| 16261.771| 56.523|  25,274|
| |Panola County|    18| 776.063|  0.000|   301| 12977.494| 61.592|  23,194|
| |Brown County|    18| 475.386|  7.546|   408| 10775.407| 64.139|  37,864|
| |Deaf Smith County|    18| 970.560|  7.703|   726| 39145.907| 454.468|  18,546|
| |Hardin County|    18| 312.489|  7.440| 1,124| 19513.211| 374.491|  57,602|
| |Anderson County|    17| 294.449|  7.423| 2,434| 42158.136| 79.180|  57,735|
| |Lamb County|    17| 1318.545| 66.481|   246| 19080.121| 221.604|  12,893|
| |Bee County|    17| 522.033| 26.321| 1,382| 42438.201| 1285.341|  32,565|
| |Titus County|    17| 519.084|  8.724| 1,397| 42656.489| 471.101|  32,750|
| |Aransas County|    16| 680.561|  6.076|   187|  7954.062| 85.070|  23,510|
| |Grayson County|    16| 117.464|  3.146| 1,260|  9250.286| 148.928| 136,212|
| |Jasper County|    15| 422.190| 16.083|   359| 10104.422| 221.147|  35,529|
| |Rockwall County|    15| 142.973|  2.723| 1,105| 10532.336| 284.584| 104,915|
| |Fayette County|    14| 552.355|  0.000|   405| 15978.853| 152.180|  25,346|
| |Polk County|    14| 272.623|  5.564|   769| 14974.782| 58.419|  51,353|
| |Moore County|    14| 668.577|  6.822| 1,082| 51671.442| 218.311|  20,940|
| |Hood County|    13| 210.892|  6.952|   657| 10658.144| 298.956|  61,643|
| |Henderson County|    12| 145.038|  0.000|   697|  8424.284| 96.692|  82,737|
| |Red River County|    12| 998.087| 11.882|   141| 11727.522| 59.410|  12,023|
| |Wichita County|    12| 90.751|  1.080| 1,117|  8447.402| 125.323| 132,230|
| |Uvalde County|    12| 448.749| 10.685|   595| 22250.477| 277.797|  26,741|
| |Lee County|    12| 696.096| 16.574|   180| 10441.441| 58.008|  17,239|
| |Gonzales County|    11| 527.907| 13.712|   721| 34601.910| 260.526|  20,837|
| |Navarro County|    11| 219.504|  8.552|   942| 18797.518| 245.160|  50,113|
| |Jackson County|    11| 745.257| 38.715|   418| 28319.783| 116.144|  14,760|
| |Cherokee County|    11| 208.943| 10.854| 1,232| 23401.588| 331.052|  52,646|
| |San Augustine County|    11| 1335.438|  0.000|   178| 21609.809| 277.494|   8,237|
| |Burnet County|    11| 228.429|  5.933|   576| 11961.375| 56.366|  48,155|
| |Karnes County|    10| 640.985| 36.628|   672| 43074.162| 366.277|  15,601|
| |Palo Pinto County|    10| 342.595| 14.683|   347| 11888.040| 401.325|  29,189|
| |Wise County|    10| 142.890|  6.124|   536|  7658.893| 259.243|  69,984|
| |Marion County|     9| 913.335| 14.497|   136| 13801.502| 43.492|   9,854|
| |Wood County|     9| 197.633|  6.274|   360|  7905.312| 138.029|  45,539|
| |Cass County|     9| 299.740|  4.758|   199|  6627.589| 109.429|  30,026|
| |Refugio County|     9| 1295.337| 102.805|   243| 34974.093| 411.218|   6,948|
| |Fannin County|     9| 253.421|  4.023|   321|  9038.689| 301.692|  35,514|
| |Houston County|     8| 348.311|  6.220|   323| 14063.044| 55.979|  22,968|
| |San Jacinto County|     8| 277.210|  0.000|   187|  6479.781| 49.502|  28,859|
| |Van Zandt County|     8| 141.368| 12.622|   446|  7881.251| 179.234|  56,590|
| |Parmer County|     7| 728.787|  0.000|   360| 37480.479| 297.464|   9,605|
| |Andrews County|     7| 374.231|  0.000|   338| 18070.035| 313.132|  18,705|
| |Duval County|     7| 627.409| 12.804|   195| 17477.817| 243.281|  11,157|
| |Hill County|     7| 191.001|  0.000|   340|  9277.197| 74.062|  36,649|
| |Calhoun County|     7| 328.793| 13.420|   555| 26068.577| 73.811|  21,290|
| |Erath County|     7| 163.942|  6.692|   580| 13583.774| 177.325|  42,698|
| |Howard County|     7| 190.923|  3.896|   201|  5482.217| 116.892|  36,664|
| |Camp County|     6| 458.225|  0.000|   256| 19550.939| 250.933|  13,094|
| |Burleson County|     6| 325.327|  0.000|   250| 13555.278| 61.967|  18,443|
| |Brooks County|     6| 845.904| 60.422|   147| 20724.658| 684.780|   7,093|
| |Gillespie County|     6| 222.321|  0.000|   188|  6966.059| 68.814|  26,988|
| |Goliad County|     6| 783.494| 37.309|   119| 15539.305| 559.639|   7,658|
| |Zavala County|     6| 506.757| 12.066|   243| 20523.649| 398.166|  11,840|
| |Sabine County|     6| 569.152|  0.000|    65|  6165.813| 189.717|  10,542|
| |Dallam County|     6| 823.384| 19.604|   196| 26897.214| 117.626|   7,287|
| |Coryell County|     6| 78.998|  1.881|   717|  9440.297| 92.165|  75,951|
| |Young County|     6| 333.148|  7.932|   200| 11104.942| 245.895|  18,010|
| |Frio County|     6| 295.479|  7.035|   571| 28119.768| 415.078|  20,306|
| |Floyd County|     6| 1050.420|  0.000|    94| 16456.583| 125.050|   5,712|
| |Kerr County|     6| 114.068|  0.000|   416|  7908.745| 48.886|  52,600|
| |Chambers County|     5| 114.059|  6.518| 1,028| 23450.510| 250.930|  43,837|
| |Live Oak County|     5| 409.601| 35.109|   240| 19660.850| 117.029|  12,207|
| |Martin County|     5| 866.401|  0.000|    67| 11609.773| 297.052|   5,771|
| |Reeves County|     5| 312.969|  0.000|   152|  9514.271| 53.652|  15,976|
| |Dawson County|     5| 392.835| 11.224|   172| 13513.514| 303.044|  12,728|
| |Lampasas County|     5| 233.340| 13.334|   128|  5973.493| 160.004|  21,428|
| |Blanco County|     5| 419.076|  0.000|   116|  9722.571| 215.525|  11,931|
| |Knox County|     5| 1364.629| 155.958|    62| 16921.397| 77.979|   3,664|
| |Waller County|     5| 90.504|  0.000|   526|  9521.051| 212.039|  55,246|
| |Hockley County|     5| 217.193|  6.206|   223|  9686.808| 105.494|  23,021|
| |Bailey County|     4| 571.429|  0.000|   187| 26714.286| 326.531|   7,000|
| |Dimmit County|     4| 395.101| 14.111|   164| 16199.131| 197.550|  10,124|
| |Austin County|     4| 133.191|  0.000|   331| 11021.577| 423.358|  30,032|
| |Kendall County|     4| 84.333|  0.000|   180|  3794.986| 66.262|  47,431|
| |Gaines County|     4| 186.116|  6.647|   199|  9259.259| 252.586|  21,492|
| |Castro County|     4| 531.208|  0.000|   209| 27755.644| 170.746|   7,530|
| |Lynn County|     4| 672.156|  0.000|    74| 12434.885| 168.039|   5,951|
| |Presidio County|     4| 596.659| 42.618|    49|  7309.069| 63.928|   6,704|
| |Reagan County|     4| 1039.231| 37.115|    66| 17147.311| 111.346|   3,849|
| |Newton County|     4| 294.226|  0.000|   124|  9121.000| 325.750|  13,595|
| |Trinity County|     4| 273.019|  0.000|   163| 11125.520| 68.255|  14,651|
| |Crockett County|     4| 1154.734| 41.241|   157| 45323.326| 82.481|   3,464|
| |Zapata County|     3| 211.581| 10.075|   203| 14316.948| 312.333|  14,179|
| |Yoakum County|     3| 344.313|  0.000|   124| 14231.608| 360.709|   8,713|
| |Swisher County|     3| 405.570| 19.313|    83| 11220.765| 57.939|   7,397|
| |Tyler County|     3| 138.427|  6.592|   146|  6736.803| 197.754|  21,672|
| |Morris County|     3| 242.170|  0.000|   134| 10816.920| 207.574|  12,388|
| |Hopkins County|     3| 80.897|  3.852|   217|  5851.580| 69.341|  37,084|
| |Milam County|     3| 120.856|  0.000|   366| 14744.390| 189.916|  24,823|
| |Hutchinson County|     3| 143.280|  0.000|   133|  6352.087| 47.760|  20,938|
| |Leon County|     3| 172.374|  8.208|   158|  9078.373| 123.124|  17,404|
| |Madison County|     3| 210.025| 10.001|   684| 47885.746| 180.022|  14,284|
| |Limestone County|     3| 128.003|  0.000|   298| 12714.938| 384.008|  23,437|
| |Callahan County|     3| 215.162|  0.000|    52|  3729.470| 61.475|  13,943|
| |Stephens County|     3| 320.307|  0.000|   131| 13986.761| 1357.494|   9,366|
| |Robertson County|     3| 175.706|  8.367|   239| 13997.892| 41.835|  17,074|
| |Comanche County|     3| 220.022|  0.000|   172| 12614.595| 314.317|  13,635|
| |Cooke County|     3| 72.715|  0.000|   265|  6423.152| 145.430|  41,257|
| |Falls County|     3| 173.440|  0.000|   145|  8382.957| 148.663|  17,297|
| |Bandera County|     3| 129.803|  0.000|   100|  4326.757| 55.630|  23,112|
| |Franklin County|     3| 279.720| 13.320|    95|  8857.809| 39.960|  10,725|
| |Garza County|     3| 481.618|  0.000|   101| 16214.481| 45.868|   6,229|
| |Hamilton County|     3| 354.568|  0.000|    92| 10873.419| 151.958|   8,461|
| |Nolan County|     3| 203.887|  0.000|   140|  9514.748| 58.254|  14,714|
| |La Salle County|     2| 265.957|  0.000|   364| 48404.255| 37.994|   7,520|
| |Upshur County|     2| 47.901|  0.000|   267|  6394.750| 157.388|  41,753|
| |Montague County|     2| 100.918|  7.208|    86|  4339.489| 115.335|  19,818|
| |Brewster County|     2| 217.320|  0.000|   187| 20319.461|  0.000|   9,203|
| |Runnels County|     2| 194.856| 13.918|   152| 14809.041| 389.712|  10,264|
| |Pecos County|     2| 126.398|  9.028|   258| 16305.378| 135.427|  15,823|
| |Bosque County|     2| 107.038|  0.000|   180|  9633.396| 145.265|  18,685|
| |Real County|     2| 579.374| 41.384|    91| 26361.530| 165.536|   3,452|
| |Throckmorton County|     2| 1332.445|  0.000|     4|  2664.890|  0.000|   1,501|
| |Jim Hogg County|     2| 384.615| 27.473|    65| 12500.000| 82.418|   5,200|
| |Scurry County|     2| 119.739|  8.553|   505| 30234.090| 205.267|  16,703|
| |Terry County|     2| 162.114|  0.000|   173| 14022.858| 347.387|  12,337|
| |Rusk County|     2| 36.761|  0.000|   398|  7315.370| 76.147|  54,406|
| |Ochiltree County|     2| 203.335|  0.000|   100| 10166.734| 72.620|   9,836|
| |Gray County|     2| 91.383|  0.000|   226| 10326.236| 71.801|  21,886|
| |Culberson County|     2| 921.234|  0.000|    21|  9672.962| 263.210|   2,171|
| |Cottle County|     2| 1430.615|  0.000|    18| 12875.536|  0.000|   1,398|
| |Hudspeth County|     2| 409.333|  0.000|    35|  7163.324| 350.857|   4,886|
| |Colorado County|     2| 93.054|  0.000|   360| 16749.639| 525.088|  21,493|
| |Hansford County|     2| 370.439|  0.000|    93| 17225.412| 529.199|   5,399|
| |Coke County|     2| 590.493|  0.000|    42| 12400.354|  0.000|   3,387|
| |Crane County|     2| 416.927|  0.000|    70| 14592.454|  0.000|   4,797|
| |Mitchell County|     1| 117.028|  0.000|    70|  8191.925| 150.464|   8,545|
| |Sutton County|     1| 264.831|  0.000|    68| 18008.475| 226.998|   3,776|
| |Upton County|     1| 273.448|  0.000|    16|  4375.171|  0.000|   3,657|
| |Schleicher County|     1| 358.038|  0.000|    36| 12889.366|  0.000|   2,793|
| |Wilbarger County|     1| 78.315|  0.000|    78|  6108.544| 100.690|  12,769|
| |Ward County|     1| 83.347|  0.000|    99|  8251.375| 119.067|  11,998|
| |Rains County|     1| 79.911|  0.000|    54|  4315.167| 34.247|  12,514|
| |Llano County|     1| 45.882|  0.000|    92|  4221.152| 19.664|  21,795|
| |Oldham County|     1| 473.485|  0.000|    14|  6628.788|  0.000|   2,112|
| |Winkler County|     1| 124.844|  0.000|    88| 10986.267| 71.339|   8,010|
| |Fisher County|     1| 261.097|  0.000|    31|  8093.995| 111.899|   3,830|
| |Hall County|     1| 337.382|  0.000|    15|  5060.729| 192.790|   2,964|
| |McCulloch County|     1| 125.251|  0.000|    57|  7139.279| 161.036|   7,984|
| |Crosby County|     1| 174.307|  0.000|    65| 11329.963| 49.802|   5,737|
| |Dickens County|     1| 452.284|  0.000|     5|  2261.420|  0.000|   2,211|
| |Eastland County|     1| 54.466|  0.000|    92|  5010.893| 147.837|  18,360|
| |Kimble County|     1| 230.574|  0.000|    16|  3689.186| 98.817|   4,337|
| |Kenedy County|     1| 2475.248|  0.000|     6| 14851.485|  0.000|     404|
| |Clay County|     1| 95.502|  0.000|    47|  4488.588| 95.502|  10,471|
| |Briscoe County|     1| 646.831|  0.000|    12|  7761.966|  0.000|   1,546|
| |Menard County|     0|  0.000|  0.000|    18|  8419.083| 66.818|   2,138|
| |Baylor County|     0|  0.000|  0.000|    13|  3704.759| 81.423|   3,509|
| |Armstrong County|     0|  0.000|  0.000|     8|  4239.534|  0.000|   1,887|
| |Archer County|     0|  0.000|  0.000|    33|  3858.295| 200.431|   8,553|
| |Lipscomb County|     0|  0.000|  0.000|    22|  6804.825| 176.749|   3,233|
| |Freestone County|     0|  0.000|  0.000|   182|  9230.613| 188.380|  19,717|
| |Foard County|     0|  0.000|  0.000|     3|  2597.403| 123.686|   1,155|
| |Childress County|     0|  0.000|  0.000|    53|  7254.312| 254.194|   7,306|
| |Irion County|     0|  0.000|  0.000|     9|  5859.375|  0.000|   1,536|
| |Jack County|     0|  0.000|  0.000|    99| 11080.022| 639.540|   8,935|
| |Hardeman County|     0|  0.000|  0.000|    22|  5593.694| 145.291|   3,933|
| |Concho County|     0|  0.000|  0.000|    34| 12472.487| 314.432|   2,726|
| |Kent County|     0|  0.000|  0.000|     3|  3937.008|  0.000|     762|
| |King County|     0|  0.000|  0.000|     0|     0.000|  0.000|     272|
| |Kinney County|     0|  0.000|  0.000|    21|  5726.752| 77.915|   3,667|
| |Glasscock County|     0|  0.000|  0.000|     6|  4258.339|  0.000|   1,409|
| |Stonewall County|     0|  0.000|  0.000|     7|  5185.185| 211.640|   1,350|
| |Wheeler County|     0|  0.000|  0.000|    36|  7120.253| 84.765|   5,056|
| |Roberts County|     0|  0.000|  0.000|     6|  7025.761|  0.000|     854|
| |Edwards County|     0|  0.000|  0.000|    30| 15527.950| 147.885|   1,932|
| |Mason County|     0|  0.000|  0.000|    60| 14038.372| 233.973|   4,274|
| |Shackelford County|     0|  0.000|  0.000|    19|  5819.296| 43.754|   3,265|
| |Mills County|     0|  0.000|  0.000|    26|  5335.522| 117.264|   4,873|
| |Donley County|     0|  0.000|  0.000|    49| 14948.139| 43.581|   3,278|
| |Sterling County|     0|  0.000|  0.000|     1|   774.593| 110.656|   1,291|
| |Somervell County|     0|  0.000|  0.000|    85|  9312.007| 172.155|   9,128|
| |Sherman County|     0|  0.000|  0.000|    44| 14559.894| 189.090|   3,022|
| |Terrell County|     0|  0.000|  0.000|     2|  2577.320|  0.000|     776|
| |McMullen County|     0|  0.000|  0.000|    10| 13458.950| 192.271|     743|
| |Hemphill County|     0|  0.000|  0.000|    45| 11783.189| 112.221|   3,819|
| |Haskell County|     0|  0.000|  0.000|    52|  9190.527| 252.487|   5,658|
| |Jeff Davis County|     0|  0.000|  0.000|     8|  3518.030|  0.000|   2,274|
| |Cochran County|     0|  0.000|  0.000|    33| 11566.772| 50.073|   2,853|
| |Coleman County|     0|  0.000|  0.000|    33|  4036.697| 244.648|   8,175|
| |Jones County|     0|  0.000|  0.000|   600| 29876.015| 28.453|  20,083|
| |Hartley County|     0|  0.000|  0.000|    94| 16857.963| 230.580|   5,576|
| |Carson County|     0|  0.000|  0.000|    17|  2868.714| 48.214|   5,926|
| |Collingsworth County|     0|  0.000|  0.000|    13|  4452.055| 97.847|   2,920|
| |Motley County|     0|  0.000|  0.000|     6|  5000.000|  0.000|   1,200|
| |San Saba County|     0|  0.000|  0.000|    27|  4459.125| 70.780|   6,055|
| |Delta County|     0|  0.000|  0.000|    17|  3188.895| 26.797|   5,331|
| |Borden County|     0|  0.000|  0.000|     0|     0.000|  0.000|     654|
| |Loving County|     0|  0.000|  0.000|     0|     0.000|  0.000|     169|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 9,452| 440.084| N/A|572,646| 26662.306| N/A|21,477,737|
| |Miami-Dade County| 2,057| 757.102| 10.095|145,307| 53481.858| 675.445|2,716,940|
| |Palm Beach County|   992| 662.760|  5.822|39,129| 26142.293| 201.291|1,496,770|
| |Broward County|   980| 501.849| 12.949|66,447| 34026.909| 305.718|1,952,778|
| |Pinellas County|   548| 562.054|  7.033|18,730| 19210.335| 124.689| 974,996|
| |Hillsborough County|   483| 328.132|  9.220|34,238| 23260.017| 160.233|1,471,968|
| |Lee County|   375| 486.648|  7.601|17,401| 22581.780| 161.660| 770,577|
| |Polk County|   358| 493.945|  9.067|15,429| 21287.927| 222.334| 724,777|
| |Orange County|   351| 251.892|  5.434|33,382| 23956.333| 170.491|1,393,452|
| |Manatee County|   245| 607.559| 18.776| 9,781| 24255.244| 174.651| 403,253|
| |Duval County|   222| 231.792|  5.071|24,629| 25715.345| 177.797| 957,755|
| |St. Lucie County|   197| 600.066| 13.490| 6,254| 19049.824| 209.740| 328,297|
| |Brevard County|   178| 295.710|  6.408| 6,511| 10816.657| 106.085| 601,942|
| |Sarasota County|   173| 398.855| 11.198| 6,689| 15421.610| 150.847| 433,742|
| |Volusia County|   169| 305.449|  8.779| 8,452| 15276.061| 148.722| 553,284|
| |Collier County|   152| 394.906|  5.938|10,891| 28295.514| 206.732| 384,902|
| |Escambia County|   152| 477.513| 14.361|10,265| 32247.829| 339.734| 318,316|
| |Pasco County|   149| 268.979|  5.416| 7,453| 13454.356| 96.193| 553,947|
| |Seminole County|   145| 307.317|  7.872| 7,471| 15834.227| 106.880| 471,826|
| |Osceola County|   119| 316.699|  5.703|10,314| 27449.029| 234.958| 375,751|
| |Marion County|   113| 309.099|  9.378| 7,247| 19823.349| 287.606| 365,579|
| |Martin County|   104| 645.963|  8.873| 3,923| 24366.460| 86.957| 161,000|
| |Charlotte County|   100| 529.353|  6.806| 2,378| 12588.005| 105.871| 188,910|
| |Lake County|    83| 226.085|  5.837| 5,619| 15305.706| 178.222| 367,118|
| |Indian River County|    67| 418.952|  9.826| 2,652| 16582.981| 115.234| 159,923|
| |Clay County|    65| 296.463|  9.122| 3,461| 15785.489| 116.630| 219,252|
| |Bay County|    64| 366.332| 10.630| 4,821| 27595.089| 311.546| 174,705|
| |Hernando County|    60| 309.406|  9.577| 2,225| 11473.804| 149.546| 193,920|
| |Jackson County|    52| 1120.352| 43.090| 2,030| 43736.804| 643.279|  46,414|
| |Okaloosa County|    50| 237.261|  6.101| 3,728| 17690.212| 153.203| 210,738|
| |Suwannee County|    47| 1058.153| 12.865| 2,253| 50723.822| 2569.801|  44,417|
| |Santa Rosa County|    47| 255.001|  7.751| 4,223| 22912.111| 220.122| 184,313|
| |St. Johns County|    46| 173.800|  6.477| 3,971| 15003.476| 181.357| 264,672|
| |Sumter County|    44| 332.276|  3.236| 1,540| 11629.663| 255.680| 132,420|
| |Highlands County|    41| 385.988|  5.380| 1,608| 15138.249| 232.669| 106,221|
| |Citrus County|    40| 267.278|  3.818| 1,778| 11880.500| 228.141| 149,657|
| |Hendry County|    39| 928.085|  3.400| 1,879| 44714.673| 397.751|  42,022|
| |Putnam County|    33| 442.828| 13.419| 1,611| 21618.067| 197.452|  74,521|
| |Alachua County|    28| 104.073|  1.062| 4,629| 17205.428| 258.589| 269,043|
| |Gadsden County|    28| 613.228| 21.901| 2,037| 44612.352| 478.693|  45,660|
| |Leon County|    27| 91.967|  1.460| 5,402| 18400.311| 212.644| 293,582|
| |Columbia County|    26| 362.693| 21.921| 3,038| 42379.265| 328.815|  71,686|
| |DeSoto County|    20| 526.302| 15.037| 1,420| 37367.438| 259.392|  38,001|
| |Walton County|    18| 243.010|  5.786| 1,486| 20061.833| 150.435|  74,071|
| |Washington County|    14| 549.602|  0.000|   929| 36469.988| 347.707|  25,473|
| |Flagler County|    14| 121.653|  1.241| 1,160| 10079.857| 111.723| 115,081|
| |Monroe County|    13| 175.136|  0.000| 1,633| 21999.784| 205.929|  74,228|
| |Nassau County|    13| 146.685|  3.224| 1,334| 15052.186| 162.805|  88,625|
| |Okeechobee County|    12| 284.576|  0.000| 1,142| 27082.148| 348.944|  42,168|
| |Madison County|    11| 594.820| 23.175|   763| 41258.855| 486.671|  18,493|
| |Hardee County|     8| 296.989|  5.303| 1,011| 37532.019| 254.562|  26,937|
| |Calhoun County|     8| 567.175| 10.128|   503| 35661.113| 283.587|  14,105|
| |Gilchrist County|     7| 376.709| 30.752|   402| 21633.839| 299.829|  18,582|
| |Liberty County|     7| 837.922| 17.100|   411| 49197.989| 188.105|   8,354|
| |Levy County|     6| 144.568|  6.884|   767| 18480.592| 285.694|  41,503|
| |Wakulla County|     5| 148.196|  4.234|   773| 22911.171| 342.969|  33,739|
| |Jefferson County|     5| 350.976|  0.000|   467| 32781.132| 140.390|  14,246|
| |Taylor County|     5| 231.814|  6.623| 1,100| 50999.119| 920.633|  21,569|
| |Union County|     5| 328.149|  0.000|   488| 32027.302| 1668.870|  15,237|
| |Gulf County|     4| 293.277| 20.948|   743| 54476.135| 995.046|  13,639|
| |Baker County|     4| 136.939|  0.000| 1,077| 36870.935| 831.418|  29,210|
| |Bradford County|     4| 141.839|  0.000|   569| 20176.589| 379.926|  28,201|
| |Dixie County|     4| 237.727|  0.000|   591| 35124.213| 373.572|  16,826|
| |Hamilton County|     4| 277.239|  0.000|   635| 44011.644| 168.323|  14,428|
| |Holmes County|     4| 203.905| 14.565|   533| 27170.311| 203.905|  19,617|
| |Franklin County|     3| 247.423| 11.782|   473| 39010.309| 648.012|  12,125|
| |Glades County|     3| 217.218|  0.000|   421| 30482.948| 206.874|  13,811|
| |Lafayette County|     2| 237.473| 16.962|   989| 117430.539| 14299.284|   8,422|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,744| 1268.625| N/A|121,278| 17595.640| N/A|6,892,503|
| |Middlesex County| 2,006| 1244.649|  0.266|26,565| 16482.606| 12.852|1,611,699|
| |Essex County| 1,194| 1513.243|  0.181|17,930| 22723.989| 15.208| 789,034|
| |Suffolk County| 1,076| 1338.463|  0.355|22,017| 27387.496| 29.854| 803,907|
| |Worcester County| 1,007| 1212.344|  0.344|13,686| 16476.809|  9.631| 830,622|
| |Norfolk County|   997| 1410.633|  0.000|10,682| 15113.721| 13.745| 706,775|
| |Plymouth County|   723| 1387.178|  0.548| 9,288| 17820.346| 11.786| 521,202|
| |Hampden County|   709| 1520.246|  0.613| 7,637| 16375.340| 11.334| 466,372|
| |Bristol County|   637| 1127.001|  0.758| 9,408| 16644.935| 13.396| 565,217|
| |Barnstable County|   158| 741.819|  0.000| 1,803|  8465.186|  2.012| 212,990|
| |Hampshire County|   130| 808.307|  0.888| 1,184|  7361.811|  8.882| 160,830|
| |Franklin County|    61| 869.194|  0.000|   411|  5856.369|  0.000|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   667|  5338.392|  0.000| 124,944|
| |Dukes County|     0|  0.000|  0.000|     0|     0.000|  0.000|  17,332|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,744| 611.120| N/A|206,040| 16259.699| N/A|12,671,821|
| |Cook County| 4,962| 963.452|  0.943|115,960| 22515.486| 125.182|5,150,233|
| |DuPage County|   526| 569.930|  0.929|12,892| 13968.693| 102.005| 922,921|
| |Lake County|   450| 646.055|  0.820|13,282| 19068.676| 125.519| 696,535|
| |Will County|   351| 508.148|  1.448| 9,874| 14294.752| 131.949| 690,743|
| |Kane County|   304| 570.996|  0.000|10,184| 19128.367| 114.038| 532,403|
| |St. Clair County|   162| 623.830|  0.550| 4,425| 17039.810| 230.498| 259,686|
| |Winnebago County|   134| 474.215|  1.517| 3,861| 13663.774| 41.456| 282,572|
| |McHenry County|   115| 373.651|  0.464| 3,389| 11011.326| 92.832| 307,774|
| |Madison County|    85| 323.236|  4.889| 3,111| 11830.427| 282.492| 262,966|
| |Kankakee County|    70| 637.163|  2.601| 1,886| 17166.991| 135.235| 109,862|
| |Rock Island County|    40| 281.930|  4.028| 1,869| 13173.197| 124.855| 141,879|
| |Peoria County|    37| 206.497|  1.595| 1,890| 10548.111| 225.632| 179,179|
| |Sangamon County|    35| 179.790|  1.468| 1,447|  7433.016| 146.767| 194,672|
| |DeKalb County|    32| 305.061|  2.724|   985|  9390.164| 66.732| 104,897|
| |LaSalle County|    30| 276.068|  7.888|   953|  8769.750| 245.832| 108,669|
| |Kendall County|    23| 178.308|  0.000| 1,461| 11326.459| 93.030| 128,990|
| |Macon County|    23| 221.135|  0.000|   755|  7258.987| 179.929| 104,009|
| |Union County|    23| 1381.133|  0.000|   361| 21677.776| 343.139|  16,653|
| |Boone County|    23| 429.553|  0.000|   769| 14362.020| 10.672|  53,544|
| |Coles County|    21| 414.848|  2.822|   612| 12089.844| 395.093|  50,621|
| |Jefferson County|    20| 530.729|  3.791|   353|  9367.371| 253.992|  37,684|
| |Jackson County|    20| 352.423|  2.517|   772| 13603.524| 138.452|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,766|  8421.996| 66.084| 209,689|
| |Clinton County|    17| 452.585|  0.000|   485| 12911.986| 296.652|  37,562|
| |Whiteside County|    17| 308.111|  0.000|   391|  7086.543| 93.210|  55,175|
| |McDonough County|    15| 505.357|  0.000|   158|  5323.091| 72.194|  29,682|
| |McLean County|    15| 87.455|  0.000|   773|  4506.842| 101.614| 171,517|
| |Iroquois County|    14| 516.338| 15.806|   280| 10326.768| 89.569|  27,114|
| |Monroe County|    13| 375.321|  0.000|   354| 10220.285| 148.479|  34,637|
| |Cass County|    11| 905.573|  0.000|   257| 21157.487| 305.778|  12,147|
| |Morgan County|    11| 326.817| 21.222|   392| 11646.562| 606.945|  33,658|
| |Tazewell County|     9| 68.284|  1.084|   700|  5310.957| 197.264| 131,803|
| |Williamson County|     7| 105.110|  2.145|   534|  8018.379| 289.588|  66,597|
| |Adams County|     7| 106.976|  4.366|   643|  9826.545| 270.716|  65,435|
| |Jasper County|     7| 728.408|  0.000|    66|  6867.846| 104.058|   9,610|
| |Randolph County|     7| 220.250|  0.000|   523| 16455.856| 265.200|  31,782|
| |Montgomery County|     7| 246.357|  0.000|   190|  6686.845| 100.554|  28,414|
| |Stephenson County|     6| 134.838|  0.000|   345|  7753.157| 57.788|  44,498|
| |Ogle County|     5| 98.730|  0.000|   433|  8550.046| 64.880|  50,643|
| |Grundy County|     5| 97.936|  0.000|   384|  7521.448| 170.688|  51,054|
| |Bureau County|     4| 122.594|  4.378|   277|  8489.641| 315.242|  32,628|
| |Christian County|     4| 123.824|  0.000|   153|  4736.256| 48.645|  32,304|
| |Carroll County|     4| 279.623|  0.000|    84|  5872.073| 279.623|  14,305|
| |Mercer County|     4| 259.118|  0.000|    79|  5117.575| 37.017|  15,437|
| |Livingston County|     3| 84.156|  4.007|   150|  4207.810| 140.260|  35,648|
| |Macoupin County|     3| 66.776|  0.000|   241|  5364.377| 197.150|  44,926|
| |Perry County|     3| 143.431| 13.660|   210| 10040.161| 177.581|  20,916|
| |Bond County|     3| 182.637|  0.000|    80|  4870.328| 173.940|  16,426|
| |Douglas County|     3| 154.123|  7.339|   146|  7500.642| 220.175|  19,465|
| |Cumberland County|     3| 278.655| 13.269|    66|  6130.411| 145.962|  10,766|
| |Fayette County|     3| 140.607|  0.000|    78|  3655.793| 80.347|  21,336|
| |Woodford County|     3| 78.005|  0.000|   186|  4836.319| 130.009|  38,459|
| |Gallatin County|     2| 414.250|  0.000|    53| 10977.630| 59.179|   4,828|
| |Clark County|     2| 129.525|  0.000|    95|  6152.451| 120.273|  15,441|
| |Wayne County|     2| 123.343|  8.810|    72|  4440.333| 96.912|  16,215|
| |Vermilion County|     2| 26.400|  0.000|   267|  3524.380| 62.228|  75,758|
| |Shelby County|     2| 92.447|  6.603|   108|  4992.142| 191.498|  21,634|
| |Saline County|     2| 85.139|  0.000|   138|  5874.590| 36.488|  23,491|
| |Ford County|     2| 154.309|  0.000|    60|  4629.272| 121.243|  12,961|
| |Jersey County|     2| 91.857|  0.000|   151|  6935.195| 301.815|  21,773|
| |Washington County|     1| 72.010| 10.287|    73|  5256.715| 72.010|  13,887|
| |Jo Daviess County|     1| 47.092|  0.000|   141|  6639.981| 107.639|  21,235|
| |Knox County|     1| 20.121|  0.000|   361|  7263.728| 178.216|  49,699|
| |Henry County|     1| 20.444|  0.000|   297|  6072.005| 184.000|  48,913|
| |Effingham County|     1| 29.405|  0.000|   241|  7086.568| 361.260|  34,008|
| |Logan County|     1| 34.943|  4.992|   196|  6848.836| 419.317|  28,618|
| |Pulaski County|     1| 187.441|  0.000|   101| 18931.584| 214.219|   5,335|
| |Franklin County|     1| 25.995|  3.714|   242|  6290.780| 237.668|  38,469|
| |Hancock County|     1| 56.472|  0.000|    92|  5195.392| 314.628|  17,708|
| |Lee County|     1| 29.329|  0.000|   194|  5689.817| 96.367|  34,096|
| |Pike County|     0|  0.000|  0.000|    34|  2184.950| 119.346|  15,561|
| |Moultrie County|     0|  0.000|  0.000|   111|  7654.645| 374.358|  14,501|
| |Massac County|     0|  0.000|  0.000|    43|  3122.277| 41.492|  13,772|
| |Menard County|     0|  0.000|  0.000|    61|  5001.640| 58.567|  12,196|
| |Piatt County|     0|  0.000|  0.000|    69|  4221.733| 69.925|  16,344|
| |Wabash County|     0|  0.000|  0.000|    63|  5468.750| 347.222|  11,520|
| |White County|     0|  0.000|  0.000|    84|  6205.215| 168.849|  13,537|
| |Warren County|     0|  0.000|  0.000|   203| 12051.769| 110.255|  16,844|
| |Stark County|     0|  0.000|  0.000|     7|  1310.371|  0.000|   5,342|
| |Scott County|     0|  0.000|  0.000|    35|  7069.279| 403.959|   4,951|
| |Schuyler County|     0|  0.000|  0.000|    19|  2807.329| 21.108|   6,768|
| |Richland County|     0|  0.000|  0.000|    41|  2642.945| 202.595|  15,513|
| |Putnam County|     0|  0.000|  0.000|    13|  2265.203|  0.000|   5,739|
| |Pope County|     0|  0.000|  0.000|    11|  2633.469| 68.402|   4,177|
| |Edgar County|     0|  0.000|  0.000|    35|  2039.508| 58.272|  17,161|
| |De Witt County|     0|  0.000|  0.000|    36|  2302.085| 27.406|  15,638|
| |Crawford County|     0|  0.000|  0.000|    35|  1874.967| 45.918|  18,667|
| |Clay County|     0|  0.000|  0.000|    36|  2730.583| 140.863|  13,184|
| |Calhoun County|     0|  0.000|  0.000|    14|  2954.210| 150.725|   4,739|
| |Brown County|     0|  0.000|  0.000|    15|  2280.328| 21.717|   6,578|
| |Edwards County|     0|  0.000|  0.000|    25|  3909.304| 156.372|   6,395|
| |Alexander County|     0|  0.000|  0.000|    40|  6943.239| 74.392|   5,761|
| |Fulton County|     0|  0.000|  0.000|    45|  1310.425| 49.921|  34,340|
| |Hamilton County|     0|  0.000|  0.000|    37|  4558.896| 140.815|   8,116|
| |Mason County|     0|  0.000|  0.000|    61|  4566.210| 149.712|  13,359|
| |Greene County|     0|  0.000|  0.000|    72|  5551.700| 319.443|  12,969|
| |Marshall County|     0|  0.000|  0.000|    35|  3059.976| 112.407|  11,438|
| |Marion County|     0|  0.000|  0.000|   182|  4891.816| 99.833|  37,205|
| |Lawrence County|     0|  0.000|  0.000|    62|  3954.586| 136.679|  15,678|
| |Johnson County|     0|  0.000|  0.000|    78|  6281.711| 126.555|  12,417|
| |Henderson County|     0|  0.000|  0.000|    23|  3460.728| 236.447|   6,646|
| |Hardin County|     0|  0.000|  0.000|    18|  4710.809|  0.000|   3,821|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,453| 582.175| N/A|129,070| 10082.027| N/A|12,801,989|
| |Philadelphia County| 1,717| 1083.921| N/A|32,186| 20318.623| N/A|1,584,064|
| |Montgomery County|   859| 1033.800|  0.344|10,405| 12522.340| 48.827| 830,915|
| |Delaware County|   713| 1258.057|  3.781| 9,691| 17099.341| 117.210| 566,747|
| |Bucks County|   583| 927.945|  0.227| 7,419| 11808.617| 50.479| 628,270|
| |Lancaster County|   421| 771.452|  2.618| 6,212| 11383.043| 75.653| 545,724|
| |Berks County|   375| 890.389|  2.374| 5,589| 13270.365| 70.214| 421,164|
| |Chester County|   350| 666.681|  0.272| 5,293| 10082.116| 51.974| 524,989|
| |Lehigh County|   341| 923.324|  1.547| 5,070| 13728.007| 39.455| 369,318|
| |Northampton County|   295| 966.310|  1.404| 4,008| 13128.716| 37.436| 305,285|
| |Allegheny County|   270| 222.031|  2.702| 9,433|  7757.114| 67.667|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,963|  9362.153| 21.121| 209,674|
| |Luzerne County|   185| 582.830|  0.450| 3,607| 11363.601| 71.560| 317,417|
| |Dauphin County|   160| 574.921|  0.513| 2,982| 10715.094| 92.911| 278,299|
| |Monroe County|   125| 734.124|  0.839| 1,667|  9790.276| 27.687| 170,271|
| |York County|   105| 233.823|  3.818| 2,884|  6422.333| 99.255| 449,058|
| |Beaver County|    94| 573.419|  1.743| 1,407|  8582.984| 79.303| 163,929|
| |Cumberland County|    71| 280.223|  0.000| 1,369|  5403.165| 46.798| 253,370|
| |Lebanon County|    55| 387.889|  1.008| 1,650| 11636.682| 40.300| 141,793|
| |Schuylkill County|    51| 360.784|  0.000|   947|  6699.255| 31.329| 141,359|
| |Westmoreland County|    48| 137.576|  0.819| 1,620|  4643.178| 33.984| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,416|  9133.893| 60.819| 155,027|
| |Columbia County|    35| 538.760|  0.000|   491|  7558.032| 43.980|  64,964|
| |Carbon County|    28| 436.259|  0.000|   390|  6076.470| 40.065|  64,182|
| |Erie County|    27| 100.101|  4.237| 1,211|  4489.708| 57.730| 269,728|
| |Susquehanna County|    27| 669.510|  0.000|   221|  5480.063| 24.797|  40,328|
| |Adams County|    22| 213.574|  2.774|   548|  5319.924| 41.605| 103,009|
| |Pike County|    21| 376.283|  0.000|   528|  9460.840|  5.120|  55,809|
| |Lycoming County|    20| 176.524|  0.000|   442|  3901.182| 64.305| 113,299|
| |Northumberland County|    18| 198.144|  7.863|   563|  6197.506| 152.539|  90,843|
| |Washington County|    17| 82.179|  3.453|   903|  4365.166| 43.507| 206,865|
| |Butler County|    17| 90.496|  1.521|   718|  3822.138| 43.347| 187,853|
| |Lawrence County|    16| 187.108|  0.000|   423|  4946.674| 53.459|  85,512|
| |Mercer County|    12| 109.665|  3.917|   493|  4505.410| 73.110| 109,424|
| |Centre County|    11| 67.740|  0.880|   392|  2414.016| 17.595| 162,385|
| |Wayne County|    10| 194.700|  2.781|   164|  3193.084| 11.126|  51,361|
| |Armstrong County|     9| 139.028|  4.414|   242|  3738.318| 66.204|  64,735|
| |Blair County|     8| 65.666|  3.518|   351|  2881.087| 78.564| 121,829|
| |Wyoming County|     8| 298.574|  0.000|    63|  2351.273| 15.995|  26,794|
| |Indiana County|     8| 95.155|  3.398|   358|  4258.204| 64.570|  84,073|
| |Fayette County|     6| 46.413|  1.105|   624|  4826.957| 143.659| 129,274|
| |Juniata County|     6| 242.297|  0.000|   139|  5613.213| 40.383|  24,763|
| |Clinton County|     5| 129.426|  0.000|   128|  3313.315| 29.583|  38,632|
| |Huntingdon County|     5| 110.757|  3.164|   333|  7376.396| 79.112|  45,144|
| |Perry County|     5| 108.057|  0.000|   140|  3025.588| 49.397|  46,272|
| |Bedford County|     4| 83.528|  0.000|   153|  3194.955| 32.815|  47,888|
| |Tioga County|     3| 73.908|  0.000|    41|  1010.076| 10.558|  40,591|
| |Cambria County|     3| 23.043|  0.000|   383|  2941.809| 51.572| 130,192|
| |Montour County|     3| 164.564|  0.000|   112|  6143.719| 78.364|  18,230|
| |Somerset County|     3| 40.846|  0.000|   142|  1933.367| 15.560|  73,447|
| |Bradford County|     3| 49.732|  0.000|    92|  1525.123| 16.577|  60,323|
| |Snyder County|     2| 49.539|  0.000|   122|  3021.896| 63.693|  40,372|
| |Union County|     2| 44.521|  0.000|   306|  6811.655| 257.584|  44,923|
| |Elk County|     2| 66.867|  0.000|    56|  1872.284| 38.210|  29,910|
| |Clarion County|     2| 52.032|  0.000|    89|  2315.417| 33.449|  38,438|
| |Fulton County|     2| 137.646|  0.000|    28|  1927.047|  9.832|  14,530|
| |Greene County|     1| 27.599|  0.000|   126|  3477.493| 39.427|  36,233|
| |Clearfield County|     1| 12.618|  1.803|   194|  2447.795| 39.655|  79,255|
| |Crawford County|     1| 11.816|  0.000|   168|  1985.135| 40.513|  84,629|
| |Jefferson County|     1| 23.028|  0.000|    75|  1727.116| 13.159|  43,425|
| |Warren County|     1| 25.516|  0.000|    23|   586.869|  0.000|  39,191|
| |McKean County|     1| 24.615|  0.000|    34|   836.923|  0.000|  40,625|
| |Mifflin County|     1| 21.674|  0.000|   125|  2709.264| 15.482|  46,138|
| |Forest County|     0|  0.000|  0.000|    12|  1655.858| 39.425|   7,247|
| |Venango County|     0|  0.000|  0.000|    67|  1322.334| 11.278|  50,668|
| |Sullivan County|     0|  0.000|  0.000|    10|  1648.533|  0.000|   6,066|
| |Potter County|     0|  0.000|  0.000|    21|  1270.725|  8.644|  16,526|
| |Cameron County|     0|  0.000|  0.000|     8|  1798.966| 32.124|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,516| 652.458| N/A|97,028|  9715.569| N/A|9,986,857|
| |Wayne County| 2,839| 1622.895|  1.225|29,111| 16641.105| 77.417|1,749,343|
| |Oakland County| 1,141| 907.295|  1.363|16,469| 13095.745| 109.961|1,257,584|
| |Macomb County|   955| 1092.712|  1.471|11,316| 12947.783| 144.333| 873,972|
| |Genesee County|   298| 734.328|  0.704| 3,741|  9218.532| 32.739| 405,813|
| |Kent County|   158| 240.504|  0.217| 7,777| 11837.949| 55.233| 656,955|
| |Saginaw County|   128| 671.778|  0.000| 2,178| 11430.731| 125.958| 190,539|
| |Washtenaw County|   114| 310.119|  0.389| 2,651|  7211.623| 42.360| 367,601|
| |Kalamazoo County|    85| 320.675|  1.078| 1,746|  6587.039| 57.668| 265,066|
| |Berrien County|    69| 449.802|  2.794| 1,462|  9530.577| 92.195| 153,401|
| |Muskegon County|    63| 362.974|  3.292| 1,222|  7040.549| 36.215| 173,566|
| |Ottawa County|    59| 202.172|  1.469| 1,926|  6599.733| 48.463| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   841|  5285.054| 26.035| 159,128|
| |Calhoun County|    43| 320.515|  2.130|   839|  6253.774| 53.242| 134,159|
| |Bay County|    35| 339.391|  5.541|   707|  6855.691| 109.436| 103,126|
| |Jackson County|    35| 220.806|  0.901|   742|  4681.093| 29.741| 158,510|
| |Lapeer County|    33| 376.682|  0.000|   498|  5684.477| 52.181|  87,607|
| |Ingham County|    33| 112.857|  1.466| 1,624|  5553.922| 35.665| 292,406|
| |Tuscola County|    29| 555.077|  0.000|   385|  7369.126| 95.703|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   354|  5196.559| 27.262|  68,122|
| |Livingston County|    28| 145.837|  0.000|   917|  4776.166| 65.478| 191,995|
| |Monroe County|    25| 166.113|  0.949| 1,064|  7069.767| 75.937| 150,500|
| |Hillsdale County|    25| 548.186|  0.000|   283|  6205.460| 50.120|  45,605|
| |Gratiot County|    15| 368.451|  0.000|   166|  4077.522| 35.091|  40,711|
| |Cass County|    15| 289.648|  2.759|   361|  6970.861| 110.342|  51,787|
| |Alpena County|    13| 457.666|  0.000|   129|  4541.454|  5.029|  28,405|
| |Van Buren County|    13| 171.783|  7.551|   508|  6712.740| 118.926|  75,677|
| |Clinton County|    13| 163.327|  0.000|   439|  5515.422| 28.717|  79,595|
| |Lenawee County|    13| 132.045|  1.451|   476|  4834.892| 66.748|  98,451|
| |Iosco County|    12| 477.574|  0.000|   136|  5412.504| 28.427|  25,127|
| |Marquette County|    11| 164.920|  0.000|   196|  2938.575| 79.247|  66,699|
| |Otsego County|    11| 445.922|  5.791|   136|  5513.216|  5.791|  24,668|
| |Midland County|    10| 120.256|  0.000|   358|  4305.161| 39.513|  83,156|
| |St. Joseph County|    10| 164.031|  4.687|   622| 10202.743| 79.672|  60,964|
| |Isabella County|     9| 128.807|  0.000|   225|  3220.174| 36.802|  69,872|
| |Eaton County|     8| 72.551|  0.000|   473|  4289.549| 14.251| 110,268|
| |Ionia County|     7| 108.197|  0.000|   277|  4281.497|  8.832|  64,697|
| |Oceana County|     6| 226.697|  0.000|   485| 18324.706| 53.976|  26,467|
| |Allegan County|     6| 50.813|  0.000|   571|  4835.664| 50.813| 118,081|
| |Sanilac County|     6| 145.737|  0.000|   115|  2793.296| 31.229|  41,170|
| |Crawford County|     5| 356.405|  0.000|   110|  7840.901| 40.732|  14,029|
| |Grand Traverse County|     5| 53.713|  0.000|   240|  2578.206| 47.574|  93,088|
| |Kalkaska County|     4| 221.754|  0.000|    56|  3104.557| 31.679|  18,038|
| |Huron County|     4| 129.111|  0.000|   173|  5584.068| 78.389|  30,981|
| |Wexford County|     4| 118.938|  0.000|    72|  2140.882| 12.743|  33,631|
| |Arenac County|     3| 201.572|  0.000|    49|  3292.347| 67.191|  14,883|
| |Delta County|     3| 83.836|  0.000|   114|  3185.781| 71.860|  35,784|
| |Ogemaw County|     3| 142.878|  6.804|    54|  2571.796|  0.000|  20,997|
| |Clare County|     3| 96.931|  0.000|    81|  2617.124| 46.157|  30,950|
| |Dickinson County|     2| 79.242|  0.000|    60|  2377.273| 28.301|  25,239|
| |Charlevoix County|     2| 76.502|  0.000|    54|  2065.562| 27.322|  26,143|
| |Gladwin County|     2| 78.589|  0.000|    68|  2672.011| 56.135|  25,449|
| |Montcalm County|     2| 31.305|  2.236|   204|  3193.088| 29.069|  63,888|
| |Mecosta County|     2| 46.027|  0.000|    74|  1702.989| 16.438|  43,453|
| |Roscommon County|     2| 83.267| 11.895|    57|  2373.121| 23.791|  24,019|
| |Barry County|     2| 32.494|  0.000|   198|  3216.897| 39.457|  61,550|
| |Cheboygan County|     2| 79.126|  0.000|    56|  2215.540| 39.563|  25,276|
| |Branch County|     2| 45.959|  0.000|   382|  8778.179| 55.807|  43,517|
| |Emmet County|     2| 59.853|  0.000|    74|  2214.574| 51.303|  33,415|
| |Benzie County|     1| 56.287|  0.000|    36|  2026.342| 64.328|  17,766|
| |Alcona County|     1| 96.108|  0.000|    29|  2787.122|  0.000|  10,405|
| |Gogebic County|     1| 71.556|  0.000|   135|  9660.107| 163.557|  13,975|
| |Iron County|     1| 90.367|  0.000|    23|  2078.438| 51.638|  11,066|
| |Manistee County|     1| 40.720|  5.817|    42|  1710.237| 40.720|  24,558|
| |Missaukee County|     1| 66.146|  0.000|    42|  2778.145|  9.449|  15,118|
| |Presque Isle County|     1| 79.416|  0.000|    21|  1667.726| 11.345|  12,592|
| |Oscoda County|     1| 121.344|  0.000|    26|  3154.957| 34.670|   8,241|
| |Alger County|     0|  0.000|  0.000|    17|  1866.491| 94.109|   9,108|
| |Antrim County|     0|  0.000|  0.000|    43|  1843.595| 12.250|  23,324|
| |Schoolcraft County|     0|  0.000|  0.000|    13|  1606.128|  0.000|   8,094|
| |Osceola County|     0|  0.000|  0.000|    71|  3026.428|  0.000|  23,460|
| |Ontonagon County|     0|  0.000|  0.000|    26|  4545.455| 349.650|   5,720|
| |Newaygo County|     0|  0.000|  0.000|   266|  5430.788| 46.666|  48,980|
| |Montmorency County|     0|  0.000|  0.000|     8|   857.633|  0.000|   9,328|
| |Menominee County|     0|  0.000|  0.000|   181|  7945.566| 294.745|  22,780|
| |Mason County|     0|  0.000|  0.000|   107|  3671.425| 29.411|  29,144|
| |Mackinac County|     0|  0.000|  0.000|    27|  2500.232|  0.000|  10,799|
| |Luce County|     0|  0.000|  0.000|     4|   642.158| 22.934|   6,229|
| |Leelanau County|     0|  0.000|  0.000|    75|  3446.533| 19.694|  21,761|
| |Lake County|     0|  0.000|  0.000|    27|  2277.904| 60.262|  11,853|
| |Keweenaw County|     0|  0.000|  0.000|     4|  1890.359| 67.513|   2,116|
| |Houghton County|     0|  0.000|  0.000|    54|  1513.283| 16.014|  35,684|
| |Chippewa County|     0|  0.000|  0.000|    44|  1178.077| 15.300|  37,349|
| |Baraga County|     0|  0.000|  0.000|     5|   609.088|  0.000|   8,209|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 4,595| 432.779| N/A|217,434| 20478.981| N/A|10,617,423|
| |Fulton County|   474| 445.515|  5.908|21,993| 20671.337| 230.545|1,063,937|
| |Cobb County|   339| 445.970|  3.759|14,893| 19592.418| 249.766| 760,141|
| |Gwinnett County|   289| 308.678|  4.425|21,534| 23000.267| 263.361| 936,250|
| |DeKalb County|   264| 347.690|  5.080|15,030| 19794.626| 208.275| 759,297|
| |Dougherty County|   173| 1966.893|  4.873| 2,826| 32129.701| 214.393|  87,956|
| |Clayton County|   116| 396.912|  2.933| 5,522| 18894.394| 252.225| 292,256|
| |Muscogee County|   109| 556.779|  9.486| 5,066| 25877.437| 232.052| 195,769|
| |Hall County|   105| 513.596|  9.783| 6,552| 32048.366| 329.819| 204,441|
| |Richmond County|    97| 478.970|  4.938| 5,064| 25005.185| 500.132| 202,518|
| |Chatham County|    96| 331.686| 10.365| 6,247| 21583.803| 268.508| 289,430|
| |Bibb County|    83| 541.920| 13.991| 4,061| 26514.929| 415.068| 153,159|
| |Troup County|    77| 1101.227| 16.345| 2,413| 34509.882| 251.300|  69,922|
| |Cherokee County|    67| 258.914|  2.208| 3,981| 15384.140| 286.517| 258,773|
| |Bartow County|    64| 594.034|  2.652| 2,057| 19092.614| 250.608| 107,738|
| |Houston County|    62| 392.746|  2.715| 2,218| 14050.157| 218.996| 157,863|
| |Henry County|    59| 251.534|  7.308| 3,735| 15923.363| 225.954| 234,561|
| |Douglas County|    58| 396.329|  6.833| 2,874| 19638.794| 233.307| 146,343|
| |Glynn County|    56| 656.568| 15.074| 2,750| 32242.180| 363.457|  85,292|
| |Sumter County|    56| 1896.762|  0.000|   783| 26520.797| 101.612|  29,524|
| |Carroll County|    54| 450.030|  5.953| 2,043| 17026.135| 192.870| 119,992|
| |Habersham County|    52| 1147.194|  9.455| 1,212| 26738.440| 223.766|  45,328|
| |Lowndes County|    50| 425.873|  7.301| 3,256| 27732.825| 94.909| 117,406|
| |Upson County|    49| 1861.702| 16.283|   626| 23784.195| 493.921|  26,320|
| |Newton County|    49| 438.502| 11.506| 2,012| 18005.441| 287.647| 111,744|
| |Tift County|    45| 1107.174| 31.634| 1,399| 34420.825| 231.979|  40,644|
| |Baldwin County|    44| 980.174| 15.912| 1,168| 26019.158| 381.886|  44,890|
| |Thomas County|    44| 989.854|  6.428| 1,248| 28075.859| 401.726|  44,451|
| |Spalding County|    43| 644.649|  4.283| 1,036| 15531.535| 212.027|  66,703|
| |Walton County|    42| 444.007|  4.531| 1,268| 13404.797| 234.086|  94,593|
| |Mitchell County|    41| 1875.314|  0.000|   673| 30782.601| 150.287|  21,863|
| |Butts County|    40| 1604.107| 17.187|   511| 20492.461| 120.308|  24,936|
| |Whitfield County|    38| 363.191| 10.923| 3,720| 35554.536| 263.519| 104,628|
| |Hancock County|    35| 4138.583|  0.000|   338| 39966.891| 337.844|   8,457|
| |Fayette County|    34| 297.148|  7.491| 1,277| 11160.539| 196.018| 114,421|
| |Columbia County|    34| 216.956| 10.027| 2,635| 16814.069| 359.162| 156,714|
| |Ware County|    34| 951.475| 19.989| 1,229| 34393.015| 339.812|  35,734|
| |Barrow County|    33| 396.444|  1.716| 1,433| 17215.281| 247.134|  83,240|
| |Early County|    32| 3140.334|  0.000|   383| 37585.868| 322.445|  10,190|
| |Coffee County|    32| 739.491| 13.205| 1,591| 36766.575| 425.868|  43,273|
| |Terrell County|    30| 3516.587|  0.000|   307| 35986.403| 83.728|   8,531|
| |Monroe County|    30| 1087.824| 20.720|   501| 18166.655| 207.205|  27,578|
| |Forsyth County|    27| 110.542|  2.924| 2,569| 10517.826| 174.878| 244,252|
| |Paulding County|    26| 154.150|  3.388| 1,886| 11181.796| 176.171| 168,667|
| |Coweta County|    26| 175.074|  3.848| 1,768| 11905.002| 254.915| 148,509|
| |Rockdale County|    26| 286.041| 14.145| 1,471| 16183.330| 240.463|  90,896|
| |Randolph County|    26| 3835.940|  0.000|   287| 42342.874| 337.225|   6,778|
| |Jenkins County|    24| 2766.252|  0.000|   263| 30313.509| 312.850|   8,676|
| |Colquitt County|    24| 526.316|  3.133| 1,623| 35592.105| 241.228|  45,600|
| |Gordon County|    24| 414.057|  2.465| 1,335| 23031.934| 374.623|  57,963|
| |Worth County|    23| 1135.971|  0.000|   471| 23262.706| 169.337|  20,247|
| |Lee County|    23| 766.871|  4.763|   607| 20238.730| 323.896|  29,992|
| |Clarke County|    21| 163.639|  3.340| 2,250| 17532.786| 225.978| 128,331|
| |Floyd County|    20| 203.050|  4.351| 1,805| 18325.245| 436.557|  98,498|
| |Wilcox County|    19| 2200.347|  0.000|   198| 22929.936| 281.247|   8,635|
| |Laurens County|    19| 399.613| 33.051| 1,128| 23724.393| 655.005|  47,546|
| |Appling County|    19| 1033.395|  0.000|   789| 42913.086| 916.847|  18,386|
| |Brooks County|    18| 1164.521|  0.000|   432| 27948.502| 184.845|  15,457|
| |Turner County|    18| 2254.227|  0.000|   262| 32811.522| 286.251|   7,985|
| |Putnam County|    18| 813.780|  0.000|   476| 21519.960| 310.011|  22,119|
| |Bulloch County|    17| 213.546|  5.384| 1,395| 17523.364| 238.669|  79,608|
| |Harris County|    17| 482.461|  0.000|   685| 19440.345| 117.575|  35,236|
| |Jackson County|    17| 232.950|  1.958| 1,188| 16279.102| 244.695|  72,977|
| |Walker County|    17| 243.689|  0.000|   814| 11668.411| 223.211|  69,761|
| |Stephens County|    17| 655.738| 27.552|   696| 26846.673| 413.280|  25,925|
| |Decatur County|    17| 643.842| 32.463|   846| 32040.600| 286.753|  26,404|
| |Catoosa County|    16| 236.756| 14.797|   709| 10491.270| 152.201|  67,580|
| |Oconee County|    16| 397.219|  3.547|   472| 11717.974| 124.131|  40,280|
| |Peach County|    16| 580.847| 10.372|   451| 16372.613| 342.285|  27,546|
| |Crisp County|    15| 670.481|  6.386|   415| 18549.973| 261.807|  22,372|
| |Emanuel County|    14| 618.211| 31.541|   591| 26097.324| 504.662|  22,646|
| |Lamar County|    14| 733.868| 14.977|   294| 15411.228| 149.769|  19,077|
| |Dooly County|    14| 1045.556|  0.000|   264| 19716.206| 128.027|  13,390|
| |Greene County|    13| 709.452|  7.796|   361| 19700.939| 413.197|  18,324|
| |Wayne County|    13| 434.390| 23.868|   871| 29104.153| 467.805|  29,927|
| |Wilkinson County|    12| 1340.183| 15.955|   238| 26580.299| 366.955|   8,954|
| |Telfair County|    12| 756.620| 27.022|   309| 19482.976| 279.229|  15,860|
| |Johnson County|    12| 1244.426| 14.815|   264| 27377.372| 340.736|   9,643|
| |Polk County|    11| 258.137|  0.000|   958| 22481.402| 522.979|  42,613|
| |Jefferson County|    11| 716.053| 37.198|   567| 36909.257| 650.957|  15,362|
| |Stewart County|    10| 1510.346| 64.729|   275| 41534.511| 431.527|   6,621|
| |Macon County|    10| 772.380|  0.000|   189| 14597.976| 132.408|  12,947|
| |Bleckley County|    10| 776.820| 11.097|   279| 21673.270| 577.066|  12,873|
| |McDuffie County|    10| 469.219|  0.000|   415| 19472.598| 422.297|  21,312|
| |Pierce County|     9| 462.368|  7.339|   442| 22707.424| 308.246|  19,465|
| |Candler County|     9| 833.102| 66.119|   280| 25918.726| 343.820|  10,803|
| |Cook County|     9| 521.135| 24.816|   472| 27330.631| 281.247|  17,270|
| |Screven County|     9| 644.422|  0.000|   228| 16325.362| 306.868|  13,966|
| |Toombs County|     9| 335.445|  5.325|   871| 32463.660| 617.645|  26,830|
| |Lumpkin County|     9| 267.777| 12.751|   417| 12407.022| 318.783|  33,610|
| |Bryan County|     8| 201.883|  0.000|   732| 18472.254| 270.378|  39,627|
| |Bacon County|     8| 716.589|  0.000|   472| 42278.753| 447.868|  11,164|
| |Brantley County|     8| 418.651| 22.428|   272| 14234.131| 171.946|  19,109|
| |Hart County|     8| 305.285|  5.452|   350| 13356.230| 245.319|  26,205|
| |Grady County|     8| 324.768| 17.398|   560| 22733.731| 463.954|  24,633|
| |Jeff Davis County|     8| 529.276|  0.000|   532| 35196.824| 765.559|  15,115|
| |Camden County|     7| 128.050|  5.227|   860| 15731.899| 321.432|  54,666|
| |Burke County|     7| 312.737|  0.000|   546| 24393.513| 504.209|  22,383|
| |Ben Hill County|     7| 419.162| 25.663|   535| 32035.928| 846.878|  16,700|
| |Madison County|     7| 234.270|  4.781|   447| 14959.839| 253.395|  29,880|
| |Haralson County|     7| 234.962|  4.795|   251|  8425.081| 182.216|  29,792|
| |Liberty County|     7| 113.942|  9.301|   803| 13070.725| 193.003|  61,435|
| |Oglethorpe County|     7| 458.746|  0.000|   252| 16514.844| 355.762|  15,259|
| |Union County|     7| 285.586|  0.000|   331| 13504.141| 396.324|  24,511|
| |Meriwether County|     7| 330.703|  6.749|   436| 20598.101| 310.456|  21,167|
| |White County|     6| 194.818|  4.639|   394| 12793.039| 190.179|  30,798|
| |Banks County|     6| 311.948| 14.855|   301| 15649.371| 222.820|  19,234|
| |Pike County|     6| 316.422| 15.068|   241| 12709.630| 195.880|  18,962|
| |Calhoun County|     6| 969.462|  0.000|   214| 34577.476| 253.907|   6,189|
| |Pickens County|     6| 184.100|  4.383|   444| 13623.393| 280.533|  32,591|
| |Franklin County|     6| 256.970|  0.000|   456| 19529.744| 336.509|  23,349|
| |Dawson County|     5| 191.512| 10.944|   484| 18538.379| 585.480|  26,108|
| |Effingham County|     5| 77.765|  6.666|   823| 12800.174| 213.299|  64,296|
| |Fannin County|     5| 190.927| 10.910|   368| 14052.238| 185.472|  26,188|
| |Heard County|     5| 419.358| 11.982|   152| 12748.469| 107.835|  11,923|
| |Lanier County|     5| 479.708| 13.706|   231| 22162.525| 164.471|  10,423|
| |Lincoln County|     5| 631.233| 18.035|   168| 21209.443| 486.952|   7,921|
| |Marion County|     5| 598.158|  0.000|   162| 19380.309| 205.083|   8,359|
| |Seminole County|     5| 618.047| 17.658|   242| 29913.473| 812.290|   8,090|
| |Talbot County|     5| 807.103| 46.120|   147| 23728.814| 207.541|   6,195|
| |Chattooga County|     4| 161.362|  5.763|   360| 14522.570| 541.715|  24,789|
| |Twiggs County|     4| 492.611| 17.593|   135| 16625.616| 299.085|   8,120|
| |Clinch County|     4| 604.412|  0.000|   216| 32638.259| 431.723|   6,618|
| |Jones County|     4| 139.203|  4.972|   348| 12110.666| 208.805|  28,735|
| |Gilmer County|     4| 127.514|  0.000|   684| 21804.967| 291.462|  31,369|
| |Pulaski County|     3| 269.372| 12.827|   139| 12480.919| 307.854|  11,137|
| |Charlton County|     3| 224.014|  0.000|   490| 36589.008| 693.378|  13,392|
| |Washington County|     3| 147.246|  7.012|   536| 26308.040| 427.716|  20,374|
| |Atkinson County|     3| 367.422| 17.496|   352| 43110.839| 577.377|   8,165|
| |Baker County|     3| 987.492|  0.000|    72| 23699.803| 423.211|   3,038|
| |Treutlen County|     3| 434.720|  0.000|   143| 20721.635| 393.318|   6,901|
| |Taylor County|     3| 374.065| 17.813|   105| 13092.269| 320.627|   8,020|
| |Wilkes County|     3| 306.843|  0.000|   201| 20558.454| 116.892|   9,777|
| |Rabun County|     3| 175.060|  0.000|   234| 13654.665| 158.387|  17,137|
| |Murray County|     3| 74.820|  3.563|   655| 16335.794| 181.707|  40,096|
| |Evans County|     3| 281.584| 26.818|   313| 29378.637| 844.753|  10,654|
| |McIntosh County|     3| 208.652|  9.936|   211| 14675.198| 268.267|  14,378|
| |Dodge County|     3| 145.596|  0.000|   253| 12278.573| 221.860|  20,605|
| |Chattahoochee County|     2| 183.368|  0.000|   810| 74264.234| 641.790|  10,907|
| |Clay County|     2| 705.716|  0.000|   103| 36344.390| 856.941|   2,834|
| |Tattnall County|     2| 79.095|  5.650|   597| 23609.903| 536.717|  25,286|
| |Webster County|     2| 767.165|  0.000|    39| 14959.724|  0.000|   2,607|
| |Montgomery County|     2| 218.055|  0.000|   178| 19406.891| 389.384|   9,172|
| |Long County|     2| 102.255|  7.304|   145|  7413.467| 138.774|  19,559|
| |Dade County|     2| 124.100|  8.864|   154|  9555.721| 248.201|  16,116|
| |Echols County|     2| 499.251|  0.000|   226| 56415.377| 142.643|   4,006|
| |Towns County|     2| 166.154| 11.868|   158| 13126.194| 178.023|  12,037|
| |Jasper County|     2| 140.657| 10.047|   176| 12377.804| 140.657|  14,219|
| |Berrien County|     1| 51.554|  7.365|   337| 17373.821| 309.326|  19,397|
| |Morgan County|     1| 51.878|  7.411|   320| 16600.955| 340.912|  19,276|
| |Quitman County|     1| 434.972|  0.000|    32| 13919.095| 186.416|   2,299|
| |Schley County|     1| 190.223|  0.000|    79| 15027.582| 353.270|   5,257|
| |Glascock County|     1| 336.587| 48.084|    27|  9087.849| 144.252|   2,971|
| |Warren County|     1| 190.331|  0.000|    92| 17510.468| 407.853|   5,254|
| |Wheeler County|     1| 127.307|  0.000|   106| 13494.589| 272.802|   7,855|
| |Elbert County|     1| 52.100|  0.000|   385| 20058.352| 200.956|  19,194|
| |Irwin County|     1| 106.202|  0.000|   178| 18903.993| 166.889|   9,416|
| |Taliaferro County|     0|  0.000|  0.000|    17| 11060.507| 371.782|   1,537|
| |Miller County|     0|  0.000|  0.000|   164| 28681.357| 524.659|   5,718|
| |Crawford County|     0|  0.000|  0.000|   117|  9432.441| 172.755|  12,404|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 4,505| 618.928| N/A|193,537| 26589.439| N/A|7,278,717|
| |Maricopa County| 2,596| 578.765|  7.739|129,385| 28845.721| 106.122|4,485,414|
| |Pima County|   531| 507.028|  5.729|19,581| 18697.023| 232.030|1,047,279|
| |Yuma County|   294| 1375.201|  4.009|11,861| 55480.455| 234.546| 213,787|
| |Navajo County|   208| 1875.158| 10.303| 5,452| 49150.770| 100.455| 110,924|
| |Mohave County|   184| 867.184| 10.772| 3,363| 15849.676| 119.170| 212,181|
| |Pinal County|   169| 365.177|  4.013| 8,710| 18820.672| 102.484| 462,789|
| |Apache County|   142| 1975.322|  5.962| 3,241| 45084.647| 95.388|  71,887|
| |Coconino County|   120| 836.377|  2.987| 3,180| 22163.986| 89.612| 143,476|
| |Yavapai County|    73| 310.507|  3.646| 2,146|  9128.069| 86.286| 235,099|
| |Cochise County|    57| 452.661|  5.672| 1,761| 13984.848| 179.249| 125,922|
| |Santa Cruz County|    55| 1182.847|  6.145| 2,704| 58153.039| 129.038|  46,498|
| |Gila County|    42| 777.519| 10.578| 1,002| 18549.372| 238.016|  54,018|
| |Graham County|    21| 540.721| 18.392|   604| 15552.180| 217.024|  38,837|
| |La Paz County|    12| 568.505|  0.000|   490| 23213.947| 94.751|  21,108|
| |Greenlee County|     1| 105.285|  0.000|    57|  6001.263|  0.000|   9,498|


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


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 4,384| 943.040| N/A|137,683| 29616.929| N/A|4,648,794|
| |Orleans Parish|   568| 1455.873|  2.197|10,992| 28174.213| 94.104| 390,144|
| |Jefferson Parish|   531| 1227.766|  0.661|15,789| 36506.949| 168.459| 432,493|
| |East Baton Rouge Parish|   383| 870.338| 11.687|12,824| 29141.547| 206.790| 440,059|
| |Caddo Parish|   299| 1244.775|  2.379| 6,936| 28875.456| 159.388| 240,204|
| |St. Tammany Parish|   220| 844.792|  3.291| 5,552| 21319.489| 177.187| 260,419|
| |Calcasieu Parish|   156| 766.826|  7.022| 7,044| 34625.140| 160.809| 203,436|
| |Rapides Parish|   127| 979.575| 14.325| 3,472| 26780.205| 200.543| 129,648|
| |Ouachita Parish|   117| 763.314|  3.728| 5,144| 33559.718| 255.370| 153,279|
| |Lafourche Parish|   104| 1065.421|  7.317| 2,985| 30579.630| 270.746|  97,614|
| |Lafayette Parish|   101| 413.274|  4.676| 7,947| 32517.697| 186.470| 244,390|
| |St. Landry Parish|    96| 1168.964| 17.395| 2,895| 35251.571| 292.241|  82,124|
| |St. John the Baptist Parish|    93| 2171.020|  3.335| 1,462| 34129.374| 126.726|  42,837|
| |Acadia Parish|    90| 1450.560| 16.117| 2,696| 43452.333| 225.643|  62,045|
| |Terrebonne Parish|    90| 814.767|  6.466| 3,196| 28933.289| 208.218| 110,461|
| |Bossier Parish|    84| 661.214|  3.374| 2,464| 19395.619| 147.311| 127,039|
| |Tangipahoa Parish|    83| 615.919|  8.481| 3,710| 27530.833| 247.004| 134,758|
| |Ascension Parish|    81| 639.790|  7.899| 3,064| 24201.447| 217.777| 126,604|
| |Iberia Parish|    78| 1116.998| 12.275| 2,616| 37462.409| 171.846|  69,830|
| |St. Mary Parish|    61| 1236.119| 20.264| 1,677| 33983.140| 231.591|  49,348|
| |Washington Parish|    59| 1277.222|  3.093| 1,335| 28899.857| 216.478|  46,194|
| |Livingston Parish|    56| 397.758|  5.073| 3,100| 22018.766| 178.585| 140,789|
| |St. Charles Parish|    54| 1016.949|  5.381| 1,542| 29039.548| 182.943|  53,100|
| |Iberville Parish|    50| 1537.941|  8.788| 1,290| 39678.878| 232.888|  32,511|
| |St. Martin Parish|    47| 879.639|  5.347| 1,783| 33370.141| 192.505|  53,431|
| |East Feliciana Parish|    40| 2090.410| 29.863|   626| 32714.920| 291.164|  19,135|
| |Avoyelles Parish|    37| 921.682| 17.793| 1,143| 28472.499| 259.779|  40,144|
| |West Baton Rouge Parish|    37| 1398.073|  0.000|   756| 28566.031| 194.327|  26,465|
| |Union Parish|    35| 1583.137| 12.924|   752| 34014.836| 297.242|  22,108|
| |Lincoln Parish|    35| 748.791| 12.225|   857| 18334.688| 183.377|  46,742|
| |Pointe Coupee Parish|    33| 1518.638|  6.574|   844| 38840.313| 348.432|  21,730|
| |St. James Parish|    32| 1516.875|  0.000|   737| 34935.533| 142.207|  21,096|
| |Allen Parish|    32| 1248.683| 16.723| 1,378| 53771.413| 568.597|  25,627|
| |Vernon Parish|    31| 653.609|  9.036|   810| 17078.159| 126.505|  47,429|
| |Bienville Parish|    30| 2265.690|  0.000|   395| 29831.584| 151.046|  13,241|
| |Vermilion Parish|    30| 504.108| 14.403| 1,724| 28969.434| 340.873|  59,511|
| |Jefferson Davis Parish|    30| 956.389|  9.108| 1,078| 34366.233| 245.929|  31,368|
| |De Soto Parish|    28| 1019.554| 10.404|   775| 28219.787| 275.696|  27,463|
| |Beauregard Parish|    25| 666.720| 26.669|   884| 23575.219| 194.301|  37,497|
| |St. Bernard Parish|    24| 508.001|  0.000| 1,136| 24045.381| 99.786|  47,244|
| |Franklin Parish|    22| 1099.176| 35.688|   993| 49612.790| 421.113|  20,015|
| |Grant Parish|    22| 982.625| 25.523|   357| 15945.330| 325.415|  22,389|
| |Assumption Parish|    20| 913.617|  0.000|   613| 28002.375| 189.249|  21,891|
| |Jackson Parish|    19| 1206.809|  9.074|   402| 25533.537| 235.918|  15,744|
| |Plaquemines Parish|    19| 819.071|  0.000|   472| 20347.459| 86.218|  23,197|
| |Natchitoches Parish|    18| 471.723|  3.744|   825| 21620.630| 194.679|  38,158|
| |West Feliciana Parish|    18| 1156.218| 18.353|   406| 26079.137| 541.404|  15,568|
| |Webster Parish|    17| 443.401| 11.178|   949| 24752.217| 208.659|  38,340|
| |Red River Parish|    16| 1895.285| 67.689|   291| 34470.505| 896.876|   8,442|
| |Morehouse Parish|    14| 562.837| 17.230|   554| 22272.252| 143.581|  24,874|
| |Evangeline Parish|    13| 389.280| 25.667|   967| 28956.431| 308.002|  33,395|
| |Claiborne Parish|    12| 765.795|  9.117|   299| 19081.047| 227.915|  15,670|
| |Sabine Parish|    11| 460.559|  5.981|   699| 29266.455| 322.990|  23,884|
| |Concordia Parish|     9| 467.314|  0.000|   367| 19056.026| 296.707|  19,259|
| |Winn Parish|     9| 647.296| 20.549|   479| 34450.518| 575.374|  13,904|
| |Richland Parish|     8| 397.575|  7.100|   641| 31855.680| 283.982|  20,122|
| |West Carroll Parish|     8| 738.689| 26.382|   307| 28347.184| 184.672|  10,830|
| |Madison Parish|     6| 547.895|  0.000|   640| 58442.151| 352.218|  10,951|
| |Catahoula Parish|     5| 526.648|  0.000|   319| 33600.169| 391.225|   9,494|
| |LaSalle Parish|     4| 268.601| 19.186|   349| 23435.402| 422.087|  14,892|
| |Caldwell Parish|     3| 302.480| 14.404|   242| 24400.081| 345.692|   9,918|
| |St. Helena Parish|     2| 197.394|  0.000|   288| 28424.793| 338.390|  10,132|
| |East Carroll Parish|     2| 291.503| 20.822|   524| 76373.706| 104.108|   6,861|
| |Cameron Parish|     0|  0.000|  0.000|   174| 24953.392| 122.923|   6,973|
| |Tensas Parish|     0|  0.000|  0.000|   116| 26765.113| 922.935|   4,334|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,826| 327.313| N/A|108,287|  9263.930| N/A|11,689,100|
| |Franklin County|   537| 407.820|  1.410|19,553| 14849.372| 134.096|1,316,756|
| |Cuyahoga County|   528| 427.505|  3.354|14,335| 11606.611| 94.963|1,235,072|
| |Lucas County|   329| 768.067|  2.001| 5,704| 13316.276| 118.729| 428,348|
| |Hamilton County|   269| 329.063|  2.447|10,142| 12406.526| 87.203| 817,473|
| |Mahoning County|   260| 1136.945|  3.123| 2,681| 11723.652| 79.336| 228,683|
| |Summit County|   228| 421.432|  1.584| 3,788|  7001.680| 61.525| 541,013|
| |Stark County|   143| 385.855|  1.542| 2,008|  5418.153| 69.770| 370,606|
| |Trumbull County|   112| 565.731|  4.330| 1,629|  8228.353| 75.768| 197,974|
| |Montgomery County|   105| 197.485|  2.956| 4,693|  8826.622| 88.935| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,915|  6180.749| 66.856| 309,833|
| |Butler County|    69| 180.094|  2.237| 3,197|  8344.339| 99.928| 383,134|
| |Portage County|    65| 400.084|  3.517|   789|  4856.401| 27.258| 162,466|
| |Columbiana County|    62| 608.541|  2.804| 1,721| 16891.925| 88.337| 101,883|
| |Wayne County|    60| 518.538|  2.469|   593|  5124.881| 66.669| 115,710|
| |Wood County|    58| 443.367|  0.000| 1,146|  8760.329| 112.480| 130,817|
| |Licking County|    55| 310.977|  4.846| 1,419|  8023.205| 111.467| 176,862|
| |Allen County|    46| 449.434|  2.792|   875|  8549.013| 188.427| 102,351|
| |Ashtabula County|    46| 473.051|  0.000|   588|  6046.832| 27.913|  97,241|
| |Geauga County|    45| 480.518|  1.525|   570|  6086.557| 21.356|  93,649|
| |Marion County|    45| 691.319|  0.000| 2,964| 45534.850| 85.592|  65,093|
| |Lake County|    43| 186.835|  3.104| 1,176|  5109.733| 38.484| 230,149|
| |Pickaway County|    42| 718.477|  0.000| 2,418| 41363.737| 75.758|  58,457|
| |Warren County|    40| 170.502|  0.609| 1,946|  8294.899| 95.603| 234,602|
| |Miami County|    39| 364.530|  1.335|   911|  8515.053| 96.140| 106,987|
| |Medina County|    36| 200.283|  0.795|   996|  5541.153| 58.018| 179,746|
| |Fairfield County|    35| 222.118|  2.720| 1,498|  9506.644| 100.633| 157,574|
| |Darke County|    30| 586.935|  2.795|   459|  8980.103| 178.875|  51,113|
| |Erie County|    30| 403.953|  5.771|   632|  8509.951| 109.644|  74,266|
| |Ottawa County|    27| 666.255|  3.525|   411| 10141.888| 88.129|  40,525|
| |Belmont County|    26| 388.025|  0.000|   638|  9521.535| 36.244|  67,006|
| |Washington County|    22| 367.211|  0.000|   213|  3555.274| 23.845|  59,911|
| |Delaware County|    19| 90.832|  0.000| 1,412|  6750.264| 75.807| 209,177|
| |Monroe County|    18| 1318.295|  0.000|    96|  7030.907| 31.388|  13,654|
| |Putnam County|    17| 502.053|  0.000|   225|  6644.813| 84.379|  33,861|
| |Sandusky County|    17| 290.509|  2.441|   442|  7553.231| 158.681|  58,518|
| |Clark County|    16| 119.329|  2.131| 1,244|  9277.835| 104.413| 134,083|
| |Mercer County|    14| 340.037|  3.470|   694| 16856.116| 284.521|  41,172|
| |Tuscarawas County|    14| 152.195|  0.000|   812|  8827.334| 46.590|  91,987|
| |Greene County|    13| 76.952|  0.846|   799|  4729.574| 92.173| 168,937|
| |Hardin County|    12| 382.592|  0.000|   187|  5962.060| 100.203|  31,365|
| |Richland County|    12| 99.047|  0.000|   644|  5315.549| 47.165| 121,154|
| |Clermont County|    11| 53.287|  0.000| 1,034|  5009.010| 69.896| 206,428|
| |Madison County|    10| 223.559|  0.000|   592| 13234.669| 696.225|  44,731|
| |Coshocton County|     9| 245.902| 11.710|   202|  5519.126| 35.129|  36,600|
| |Hocking County|     9| 318.426|  0.000|   125|  4422.587| 35.381|  28,264|
| |Wyandot County|     9| 413.375|  6.562|   159|  7302.958| 85.300|  21,772|
| |Knox County|     9| 144.411|  4.584|   226|  3626.328| 48.137|  62,322|
| |Auglaize County|     8| 175.223|  6.258|   291|  6373.752| 115.773|  45,656|
| |Guernsey County|     7| 180.064|  0.000|   121|  3112.540| 14.699|  38,875|
| |Holmes County|     6| 136.488|  0.000|   335|  7620.564| 22.748|  43,960|
| |Ross County|     6| 78.262|  3.727|   547|  7134.845| 117.392|  76,666|
| |Clinton County|     6| 142.966|  0.000|   185|  4408.120| 71.483|  41,968|
| |Huron County|     5| 85.813|  0.000|   418|  7173.995| 53.940|  58,266|
| |Crawford County|     5| 120.499|  0.000|   183|  4410.276| 30.986|  41,494|
| |Carroll County|     5| 185.777|  0.000|   116|  4310.025| 26.540|  26,914|
| |Lawrence County|     4| 67.269|  9.610|   344|  5785.110| 146.550|  59,463|
| |Seneca County|     4| 72.493|  2.589|   250|  4530.791| 93.205|  55,178|
| |Shelby County|     4| 82.321|  0.000|   242|  4980.449| 141.123|  48,590|
| |Defiance County|     4| 105.023|  0.000|   169|  4437.210| 93.770|  38,087|
| |Jefferson County|     3| 45.924|  2.187|   250|  3827.019| 45.924|  65,325|
| |Perry County|     3| 83.024|  0.000|   179|  4953.783| 193.723|  36,134|
| |Williams County|     3| 81.762|  0.000|   141|  3842.800| 23.360|  36,692|
| |Hancock County|     3| 39.587|  0.000|   428|  5647.705| 94.254|  75,783|
| |Ashland County|     3| 56.092|  0.000|   161|  3010.246| 45.407|  53,484|
| |Highland County|     2| 46.338|  3.310|   171|  3961.910| 43.028|  43,161|
| |Henry County|     2| 74.058|  0.000|   128|  4739.687| 58.188|  27,006|
| |Gallia County|     2| 66.894|  4.778|    89|  2976.788| 114.676|  29,898|
| |Champaign County|     2| 51.434|  0.000|   202|  5194.805| 95.520|  38,885|
| |Adams County|     2| 72.207|  0.000|    70|  2527.258| 46.419|  27,698|
| |Vinton County|     2| 152.847|  0.000|    32|  2445.548| 10.918|  13,085|
| |Van Wert County|     2| 70.734|  5.052|    74|  2617.153| 15.157|  28,275|
| |Preble County|     2| 48.921|  0.000|   256|  6261.925| 185.202|  40,882|
| |Morrow County|     2| 56.612|  0.000|   190|  5378.170| 80.875|  35,328|
| |Athens County|     2| 30.615|  2.187|   367|  5617.892| 21.868|  65,327|
| |Brown County|     2| 46.049|  0.000|   158|  3637.871| 95.387|  43,432|
| |Logan County|     2| 43.791|  0.000|   184|  4028.727| 90.709|  45,672|
| |Scioto County|     1| 13.278|  0.000|   269|  3571.713| 81.563|  75,314|
| |Fulton County|     1| 23.738|  0.000|   163|  3869.344| 50.868|  42,126|
| |Union County|     1| 16.953|  0.000|   289|  4899.302| 92.028|  58,988|
| |Harrison County|     1| 66.489|  0.000|    26|  1728.723|  0.000|  15,040|
| |Muskingum County|     1| 11.599|  0.000|   267|  3096.909| 51.367|  86,215|
| |Fayette County|     0|  0.000|  0.000|   130|  4557.406| 85.138|  28,525|
| |Pike County|     0|  0.000|  0.000|    84|  3024.629| 41.151|  27,772|
| |Paulding County|     0|  0.000|  0.000|    75|  4016.710| 45.905|  18,672|
| |Noble County|     0|  0.000|  0.000|    19|  1317.249| 29.712|  14,424|
| |Morgan County|     0|  0.000|  0.000|    33|  2274.607| 68.927|  14,508|
| |Meigs County|     0|  0.000|  0.000|    67|  2924.870| 168.383|  22,907|
| |Jackson County|     0|  0.000|  0.000|    83|  2560.701| 39.667|  32,413|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,631| 600.594| N/A|100,212| 16575.803| N/A|6,045,680|
| |Baltimore County| 1,018| 1230.405|  4.662|27,366| 33075.891| 269.701| 827,370|
| |Montgomery County|   810| 770.923|  0.952|19,003| 18086.244| 83.075|1,050,688|
| |Prince George's County|   768| 844.581|  2.357|24,654| 27112.359| 150.347| 909,327|
| |Anne Arundel County|   229| 395.350|  0.987| 7,648| 13203.645| 70.783| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,216| 12390.819| 82.011| 259,547|
| |Carroll County|   118| 700.517|  0.848| 1,608|  9546.029| 52.581| 168,447|
| |Howard County|   116| 356.167|  2.632| 4,071| 12499.616| 98.692| 325,690|
| |Charles County|    93| 569.654|  1.750| 2,165| 13261.300| 123.381| 163,257|
| |Harford County|    69| 270.121|  0.000| 2,150|  8416.816| 101.785| 255,441|
| |St. Mary's County|    52| 458.109|  0.000| 1,048|  9232.667| 81.805| 113,510|
| |Wicomico County|    45| 434.325|  0.000| 1,401| 13521.991| 86.865| 103,609|
| |Washington County|    31| 205.231|  0.000| 1,125|  7447.914| 106.872| 151,049|
| |Cecil County|    30| 291.673|  0.000|   726|  7058.480| 33.334| 102,855|
| |Calvert County|    28| 302.621|  0.000|   737|  7965.415| 61.759|  92,525|
| |Queen Anne's County|    26| 516.068|  2.836|   482|  9567.099| 144.612|  50,381|
| |Kent County|    23| 1184.224|  0.000|   244| 12563.073|  7.355|  19,422|
| |Worcester County|    20| 382.585|  0.000|   729| 13945.214| 95.646|  52,276|
| |Allegany County|    19| 269.825|  2.029|   341|  4842.649| 101.438|  70,416|
| |Dorchester County|     5| 156.597|  0.000|   408| 12778.352| 165.546|  31,929|
| |Talbot County|     4| 107.582|  0.000|   420| 11296.092| 76.844|  37,181|
| |Somerset County|     3| 117.114|  0.000|   151|  5894.753| 83.653|  25,616|
| |Caroline County|     3| 89.804|  0.000|   461| 13799.916| 42.764|  33,406|
| |Baltimore city|     0|  0.000|  0.000|     0|     0.000|  0.000| 593,490|
| |Garrett County|     0|  0.000|  0.000|    58|  1999.035| 44.314|  29,014|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,924| 434.329| N/A|80,415| 11944.799| N/A|6,732,219|
| |Marion County|   735| 761.988|  1.481|16,640| 17250.996| 115.520| 964,582|
| |Lake County|   283| 582.913|  2.354| 8,095| 16673.773| 154.482| 485,493|
| |Allen County|   166| 437.649|  1.130| 4,277| 11276.065| 141.238| 379,299|
| |Johnson County|   119| 752.369|  0.903| 1,845| 11664.886| 79.482| 158,167|
| |Hendricks County|   109| 640.006|  0.839| 2,015| 11831.297| 107.367| 170,311|
| |Hamilton County|   105| 310.641|  0.423| 3,144|  9301.472| 161.026| 338,011|
| |Elkhart County|    92| 445.864|  5.539| 5,120| 24813.294| 191.777| 206,341|
| |St. Joseph County|    83| 305.342|  1.051| 3,844| 14141.399| 180.788| 271,826|
| |Madison County|    66| 509.381|  1.103| 1,100|  8489.685| 133.409| 129,569|
| |Howard County|    65| 787.459|  0.000|   979| 11860.341| 154.030|  82,544|
| |Delaware County|    53| 464.362|  1.252|   802|  7026.767| 90.119| 114,135|
| |Floyd County|    50| 636.764|  7.277|   890| 11334.403| 201.945|  78,522|
| |Clark County|    50| 422.647|  3.623| 1,410| 11918.649| 213.739| 118,302|
| |Bartholomew County|    47| 561.000|  0.000|   910| 10861.911| 199.504|  83,779|
| |Boone County|    46| 678.036|  0.000|   734| 10819.097| 117.919|  67,843|
| |Hancock County|    40| 511.718|  3.655|   719|  9198.137| 107.826|  78,168|
| |Porter County|    39| 228.888|  0.000| 1,450|  8509.939| 112.348| 170,389|
| |Morgan County|    35| 496.531|  2.027|   507|  7192.612| 62.826|  70,489|
| |Greene County|    34| 1065.096|  0.000|   266|  8332.811| 71.603|  31,922|
| |Monroe County|    33| 222.326|  2.887|   802|  5403.184| 44.273| 148,431|
| |Decatur County|    32| 1204.865|  0.000|   358| 13479.423| 112.956|  26,559|
| |Warrick County|    30| 476.206|  0.000|   630| 10000.317| 111.115|  62,998|
| |LaPorte County|    30| 273.005|  0.000| 1,000|  9100.175| 115.702| 109,888|
| |Grant County|    30| 456.142|  0.000|   540|  8210.555| 30.409|  65,769|
| |Noble County|    29| 607.406|  0.000|   737| 15436.495| 176.537|  47,744|
| |Dearborn County|    28| 566.137|  0.000|   535| 10817.259| 77.988|  49,458|
| |Shelby County|    28| 625.992|  3.194|   582| 13011.693| 92.621|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   364|  8022.923| 56.677|  45,370|
| |Orange County|    24| 1221.623|  0.000|   190|  9671.180| 138.160|  19,646|
| |Harrison County|    24| 592.373|  3.526|   381|  9403.924| 151.619|  40,515|
| |Marshall County|    23| 497.211|  3.088|   808| 17467.249| 74.118|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   369|  9624.915| 55.894|  38,338|
| |Henry County|    21| 437.755|  2.978|   504| 10506.129| 360.329|  47,972|
| |Daviess County|    20| 599.682|  0.000|   314|  9415.010| 175.621|  33,351|
| |Franklin County|    19| 834.871| 31.386|   253| 11116.970| 69.050|  22,758|
| |Tipton County|    17| 1122.260| 66.015|   162| 10694.481| 226.338|  15,148|
| |Vanderburgh County|    15| 82.667|  1.575| 2,181| 12019.774| 171.632| 181,451|
| |Vigo County|    13| 121.452|  4.004|   840|  7847.680| 252.247| 107,038|
| |Perry County|    13| 678.178|  7.453|   192| 10016.172| 44.715|  19,169|
| |Dubois County|    13| 304.193|  3.343|   743| 17385.811| 157.111|  42,736|
| |Jennings County|    12| 432.666|  0.000|   235|  8473.048| 51.508|  27,735|
| |Kosciusko County|    12| 151.027|  0.000|   882| 11100.483| 53.938|  79,456|
| |Tippecanoe County|    12| 61.308|  0.730| 1,337|  6830.769| 91.962| 195,732|
| |White County|    11| 456.394|  5.927|   394| 16347.191| 148.180|  24,102|
| |Wayne County|    10| 151.782|  0.000|   430|  6526.623| 114.921|  65,884|
| |LaGrange County|    10| 252.436|  0.000|   573| 14464.583| 50.487|  39,614|
| |Scott County|    10| 418.883|  0.000|   289| 12105.726| 125.665|  23,873|
| |Newton County|    10| 715.103|  0.000|   122|  8724.256| 40.863|  13,984|
| |Cass County|     9| 238.796|  0.000| 1,821| 48316.485| 98.551|  37,689|
| |Putnam County|     8| 212.902|  0.000|   341|  9074.941| 201.496|  37,576|
| |Ripley County|     8| 282.446|  5.044|   225|  7943.793| 85.743|  28,324|
| |Ohio County|     7| 1191.489| 48.632|    68| 11574.468| 72.948|   5,875|
| |Starke County|     7| 304.414|  0.000|   185|  8045.227| 43.488|  22,995|
| |Fayette County|     7| 303.004|  0.000|   220|  9522.985| 191.696|  23,102|
| |Carroll County|     6| 296.194| 28.209|   227| 11206.003| 253.880|  20,257|
| |Whitley County|     6| 176.658|  0.000|   167|  4916.971| 63.092|  33,964|
| |Wabash County|     5| 161.311|  9.218|   183|  5903.988| 64.524|  30,996|
| |Randolph County|     5| 202.716|  5.792|   135|  5473.343| 75.295|  24,665|
| |Jackson County|     5| 113.043|  0.000|   628| 14198.187| 135.651|  44,231|
| |Clay County|     5| 190.658|  0.000|   169|  6444.233| 261.474|  26,225|
| |Rush County|     4| 241.240|  0.000|   103|  6211.929| 198.161|  16,581|
| |Gibson County|     4| 118.839|  0.000|   247|  7338.305| 93.373|  33,659|
| |DeKalb County|     4| 92.007|  0.000|   252|  5796.435| 65.719|  43,475|
| |Clinton County|     4| 123.461|  4.409|   474| 14630.081| 176.372|  32,399|
| |Huntington County|     3| 82.147|  0.000|   136|  3723.987| 54.765|  36,520|
| |Knox County|     3| 81.981| 11.712|   184|  5028.147| 117.115|  36,594|
| |Steuben County|     3| 86.720|  0.000|   222|  6417.298| 49.554|  34,594|
| |Spencer County|     3| 147.951|  0.000|   141|  6953.691| 35.226|  20,277|
| |Jasper County|     2| 59.591|  0.000|   271|  8074.608| 119.182|  33,562|
| |Fulton County|     2| 100.130|  0.000|   178|  8911.585| 71.522|  19,974|
| |Fountain County|     2| 122.354|  0.000|    76|  4649.456| 17.479|  16,346|
| |Brown County|     2| 132.521|  9.466|    79|  5234.561| 56.795|  15,092|
| |Blackford County|     2| 170.097|  0.000|    67|  5698.248| 36.449|  11,758|
| |Adams County|     2| 55.902|  0.000|   135|  3773.374| 135.762|  35,777|
| |Jefferson County|     2| 61.904|  0.000|   184|  5695.184| 92.856|  32,308|
| |Wells County|     2| 70.681|  0.000|   181|  6396.664| 65.633|  28,296|
| |Miami County|     2| 56.313|  0.000|   286|  8052.709| 48.268|  35,516|
| |Parke County|     1| 59.042|  0.000|    61|  3601.582| 84.346|  16,937|
| |Washington County|     1| 35.668|  0.000|   159|  5671.280| 96.814|  28,036|
| |Pulaski County|     1| 80.952|  0.000|    87|  7042.824| 46.258|  12,353|
| |Owen County|     1| 48.079|  0.000|   115|  5529.112| 171.712|  20,799|
| |Warren County|     1| 120.992|  0.000|    27|  3266.788| 86.423|   8,265|
| |Sullivan County|     1| 48.382|  0.000|   180|  8708.694| 373.230|  20,669|
| |Vermillion County|     0|  0.000|  0.000|    65|  4194.090| 119.831|  15,498|
| |Union County|     0|  0.000|  0.000|    47|  6662.886| 121.512|   7,054|
| |Posey County|     0|  0.000|  0.000|   188|  7393.715| 95.512|  25,427|
| |Pike County|     0|  0.000|  0.000|    73|  5892.324| 230.619|  12,389|
| |Martin County|     0|  0.000|  0.000|    54|  5265.724| 125.374|  10,255|
| |Jay County|     0|  0.000|  0.000|   100|  4893.326| 62.914|  20,436|
| |Crawford County|     0|  0.000|  0.000|    52|  4916.328| 94.545|  10,577|
| |Benton County|     0|  0.000|  0.000|    69|  7887.517| 130.642|   8,748|
| |Switzerland County|     0|  0.000|  0.000|    59|  5487.862| 93.015|  10,751|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,381| 278.952| N/A|106,687| 12499.181| N/A|8,535,519|
| |Fairfax County|   540| 470.575|  0.498|17,098| 14899.802| 78.927|1,147,532|
| |Henrico County|   187| 565.265|  0.864| 4,109| 12420.727| 102.776| 330,818|
| |Prince William County|   178| 378.454|  0.607| 9,890| 21027.565| 122.101| 470,335|
| |Arlington County|   135| 570.000|  0.000| 3,229| 13633.562| 91.683| 236,842|
| |Loudoun County|   115| 278.088|  0.000| 5,511| 13326.466| 79.799| 413,538|
| |Chesterfield County|    80| 226.756|  0.000| 4,621| 13097.998| 104.875| 352,802|
| |Alexandria city|    61| 382.618|  0.896| 3,104| 19469.604| 125.448| 159,428|
| |Virginia Beach city|    55| 122.229|  0.317| 5,394| 11987.359| 133.659| 449,974|
| |Suffolk city|    53| 575.411|  4.653| 1,425| 15470.969| 221.789|  92,108|
| |Shenandoah County|    47| 1077.586|  9.826|   742| 17012.106| 81.883|  43,616|
| |Richmond County|    46| 5098.083| 15.833| 3,678| 407624.958| 3103.181|   9,023|
| |Chesapeake city|    41| 167.460|  2.334| 3,258| 13306.921| 201.885| 244,835|
| |Spotsylvania County|    35| 256.947|  0.000| 1,607| 11797.526| 126.900| 136,215|
| |Norfolk city|    34| 140.066|  1.766| 3,982| 16404.248| 164.195| 242,742|
| |Hanover County|    33| 306.219|  1.326|   700|  6495.555| 74.235| 107,766|
| |Mecklenburg County|    32| 1046.196|  0.000|   459| 15006.375| 70.058|  30,587|
| |Harrisonburg city|    31| 584.729|  0.000| 1,099| 20729.591| 59.281|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   299| 25533.732| 36.599|  11,710|
| |Galax city|    27| 4253.978| 67.523|   353| 55616.827| 135.047|   6,347|
| |Page County|    25| 1045.938|  0.000|   353| 14768.639| 47.814|  23,902|
| |Portsmouth city|    25| 264.836|  0.000| 1,965| 20816.119| 311.750|  94,398|
| |Manassas city|    22| 535.475|  0.000| 1,710| 41621.030| 198.195|  41,085|
| |Colonial Heights city|    22| 1266.552|  8.224|   206| 11859.528| 74.019|  17,370|
| |Newport News city|    20| 111.592|  1.594| 1,980| 11047.566| 121.954| 179,225|
| |Rockingham County|    20| 244.057|  1.743|   975| 11897.789| 64.501|  81,948|
| |Petersburg city|    19| 606.138|  0.000|   541| 17258.980| 118.493|  31,346|
| |Roanoke County|    19| 201.728|  0.000| 1,578| 16754.082| 98.589|  94,186|
| |Accomack County|    17| 526.055|  4.421| 1,123| 34750.588| 101.675|  32,316|
| |James City County|    17| 222.155|  1.867|   641|  8376.567| 61.606|  76,523|
| |Albemarle County|    16| 146.346|  0.000|   906|  8286.838| 88.853| 109,330|
| |Emporia city|    15| 2805.836|  0.000|   188| 35166.480| 347.389|   5,346|
| |Charlottesville city|    15| 317.353|  0.000|   560| 11847.840| 54.403|  47,266|
| |Carroll County|    14| 469.941|  4.795|   341| 11446.410| 33.567|  29,791|
| |Nottoway County|    14| 919.118|  9.379|   183| 12014.181|  9.379|  15,232|
| |Southampton County|    13| 737.338|  0.000|   303| 17185.639| 291.694|  17,631|
| |Culpeper County|    12| 228.115|  0.000| 1,039| 19750.974| 92.332|  52,605|
| |Greensville County|    11| 970.360|  0.000|   570| 50282.287| 1108.983|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   447| 19603.544| 231.809|  22,802|
| |Stafford County|    10| 65.410|  0.934| 1,496|  9785.325| 114.000| 152,882|
| |Frederick County|    10| 111.966|  1.600|   698|  7815.212| 27.192|  89,313|
| |Hampton city|     9| 66.910|  2.124| 1,337|  9939.781| 115.764| 134,510|
| |Henry County|     9| 178.017|  5.651|   672| 13291.928| 237.356|  50,557|
| |Fluvanna County|     9| 330.033|  0.000|   202|  7407.407| 52.386|  27,270|
| |Isle of Wight County|     9| 242.529|  0.000|   431| 11614.433| 169.385|  37,109|
| |Fauquier County|     9| 126.365|  0.000|   638|  8957.906| 44.128|  71,222|
| |Sussex County|     9| 806.524|  0.000|   316| 28317.950| 179.228|  11,159|
| |Danville city|     8| 199.780|  3.568|   465| 11612.227| 214.050|  40,044|
| |Buckingham County|     8| 466.527|  0.000|   617| 35980.872| 99.970|  17,148|
| |Bedford County|     8| 101.270|  1.808|   414|  5240.705| 99.461|  78,997|
| |Manassas Park city|     7| 400.503|  0.000|   535| 30609.910| 155.297|  17,478|
| |Botetourt County|     7| 209.462|  0.000|   220|  6583.081| 25.648|  33,419|
| |Franklin County|     7| 124.906|  0.000|   392|  6994.754| 99.415|  56,042|
| |Goochland County|     7| 294.700|  0.000|   172|  7241.191| 54.129|  23,753|
| |Dinwiddie County|     7| 245.235|  0.000|   238|  8338.004| 95.091|  28,544|
| |Washington County|     6| 111.649|  2.658|   283|  5266.096| 143.548|  53,740|
| |Warren County|     6| 149.388|  0.000|   367|  9137.536| 42.682|  40,164|
| |Williamsburg city|     6| 401.230|  0.000|   135|  9027.685| 85.978|  14,954|
| |Falls Church city|     6| 410.481|  0.000|    62|  4241.636| 19.547|  14,617|
| |Caroline County|     5| 162.734|  0.000|   228|  7420.667| 92.991|  30,725|
| |Charles City County|     5| 718.081|  0.000|    55|  7898.894| 61.550|   6,963|
| |Grayson County|     5| 321.543|  0.000|   165| 10610.932| 73.496|  15,550|
| |Patrick County|     5| 283.962|  8.113|   176|  9995.457| 154.151|  17,608|
| |Wise County|     5| 133.751|  7.643|   238|  6366.530| 412.716|  37,383|
| |Lynchburg city|     5| 60.851|  0.000|   736|  8957.258| 206.893|  82,168|
| |Hopewell city|     5| 221.936|  0.000|   291| 12916.685| 120.480|  22,529|
| |Alleghany County|     4| 269.179|  0.000|    60|  4037.685|  0.000|  14,860|
| |Augusta County|     4| 52.939|  0.000|   310|  4102.808| 64.284|  75,558|
| |Winchester city|     4| 142.460|  0.000|   421| 14993.945| 111.933|  28,078|
| |Fredericksburg city|     4| 137.760|  0.000|   428| 14740.322| 123.000|  29,036|
| |King George County|     4| 149.054|  0.000|   167|  6222.984| 122.437|  26,836|
| |York County|     4| 58.582|  0.000|   406|  5946.104| 83.689|  68,280|
| |Powhatan County|     4| 134.898|  0.000|   167|  5631.998| 96.356|  29,652|
| |Northumberland County|     3| 248.036| 11.811|    79|  6531.625| 82.679|  12,095|
| |Smyth County|     3| 99.655|  0.000|   169|  5613.872| 99.655|  30,104|
| |Scott County|     3| 139.108|  0.000|   118|  5471.576| 178.853|  21,566|
| |Orange County|     3| 80.969|  0.000|   235|  6342.609| 15.423|  37,051|
| |Martinsville city|     3| 238.968|  0.000|   240| 19117.413| 352.762|  12,554|
| |Salem city|     3| 118.572|  0.000|   165|  6521.481| 22.585|  25,301|
| |Pulaski County|     3| 88.165|  0.000|    91|  2674.347|  8.397|  34,027|
| |Waynesboro city|     3| 132.567|  0.000|   188|  8307.556| 94.691|  22,630|
| |Russell County|     3| 112.841|  5.373|   150|  5642.067| 188.069|  26,586|
| |Westmoreland County|     3| 166.528|  0.000|   216| 11990.008| 39.649|  18,015|
| |Wythe County|     3| 104.588|  0.000|   125|  4357.830| 49.804|  28,684|
| |Montgomery County|     3| 30.446|  0.000|   327|  3318.618| 31.896|  98,535|
| |Campbell County|     3| 54.660|  2.603|   251|  4573.199| 98.908|  54,885|
| |Gloucester County|     2| 53.550|  0.000|   175|  4685.659| 57.375|  37,348|
| |Floyd County|     2| 126.992|  0.000|   112|  7111.563| 335.622|  15,749|
| |Amelia County|     2| 152.149|  0.000|    85|  6466.337| 65.207|  13,145|
| |Brunswick County|     2| 123.221|  0.000|   247| 15217.793| 167.228|  16,231|
| |Pittsylvania County|     2| 33.138|  0.000|   567|  9394.572| 189.359|  60,354|
| |Louisa County|     2| 53.204|  0.000|   204|  5426.831| 83.607|  37,591|
| |Rappahannock County|     2| 271.370|  0.000|    46|  6241.520| 58.151|   7,370|
| |Prince George County|     2| 52.147|  0.000|   456| 11889.552| 268.185|  38,353|
| |King William County|     2| 116.632|  0.000|   102|  5948.216| 124.963|  17,148|
| |Greene County|     2| 100.913|  0.000|   177|  8930.824| 100.913|  19,819|
| |Halifax County|     2| 58.978|  4.213|   169|  4983.634| 58.978|  33,911|
| |Lee County|     2| 85.386|  6.099|   148|  6318.576| 201.267|  23,423|
| |Surry County|     2| 311.429|  0.000|    51|  7941.451|  0.000|   6,422|
| |King and Queen County|     1| 142.349|  0.000|    42|  5978.648|  0.000|   7,025|
| |Lunenburg County|     1| 81.994|  0.000|    68|  5575.599| 70.281|  12,196|
| |Madison County|     1| 75.409|  0.000|    72|  5429.455| 32.318|  13,261|
| |Middlesex County|     1| 94.500|  0.000|    51|  4819.505| 135.000|  10,582|
| |New Kent County|     1| 43.307|  0.000|   135|  5846.434| 43.307|  23,091|
| |Dickenson County|     1| 69.842|  0.000|    52|  3631.792| 109.752|  14,318|
| |Essex County|     1| 91.299|  0.000|   108|  9860.312| 78.256|  10,953|
| |Rockbridge County|     1| 44.301|  0.000|    80|  3544.057| 82.273|  22,573|
| |Buena Vista city|     1| 154.369|  0.000|    65| 10033.961| 330.790|   6,478|
| |Amherst County|     1| 31.641|  4.520|   219|  6929.283| 198.884|  31,605|
| |Buchanan County|     1| 47.610|  6.801|    84|  3999.238| 27.206|  21,004|
| |Roanoke city|     0|  0.000|  0.000|     0|     0.000|  0.000|  99,143|
| |Radford city|     0|  0.000|  0.000|    67|  3671.434| 109.595|  18,249|
| |Richmond city|     0|  0.000|  0.000|     0|     0.000|  0.000| 230,436|
| |Nelson County|     0|  0.000|  0.000|    67|  4487.609| 181.801|  14,930|
| |Mathews County|     0|  0.000|  0.000|    23|  2603.577| 80.856|   8,834|
| |Tazewell County|     0|  0.000|  0.000|   131|  3226.998| 49.267|  40,595|
| |Highland County|     0|  0.000|  0.000|     6|  2739.726|  0.000|   2,190|
| |Bristol city|     0|  0.000|  0.000|    92|  5488.605| 119.318|  16,762|
| |Covington city|     0|  0.000|  0.000|    13|  2347.418|  0.000|   5,538|
| |Poquoson city|     0|  0.000|  0.000|    46|  3748.676| 23.284|  12,271|
| |Appomattox County|     0|  0.000|  0.000|   103|  6473.509| 161.613|  15,911|
| |Staunton city|     0|  0.000|  0.000|   158|  6337.237| 40.109|  24,932|
| |Charlotte County|     0|  0.000|  0.000|    58|  4882.155| 60.125|  11,880|
| |Franklin city|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,967|
| |Cumberland County|     0|  0.000|  0.000|    81|  8155.457| 71.918|   9,932|
| |Lexington city|     0|  0.000|  0.000|    36|  4834.811| 57.557|   7,446|
| |Craig County|     0|  0.000|  0.000|    19|  3702.982| 55.684|   5,131|
| |Clarke County|     0|  0.000|  0.000|    74|  5061.906| 29.316|  14,619|
| |Norton city|     0|  0.000|  0.000|    23|  5777.443| 179.424|   3,981|
| |Bland County|     0|  0.000|  0.000|    31|  4936.306| 272.975|   6,280|
| |Bath County|     0|  0.000|  0.000|     4|   964.553|  0.000|   4,147|
| |Giles County|     0|  0.000|  0.000|    32|  1913.876| 68.353|  16,720|
| |Lancaster County|     0|  0.000|  0.000|    49|  4621.334| 161.679|  10,603|
| |Fairfax city|     0|  0.000|  0.000|     0|     0.000|  0.000|  24,019|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,347| 223.778| N/A|144,952| 13820.637| N/A|10,488,084|
| |Mecklenburg County|   257| 231.457|  3.731|23,110| 20813.145| 110.003|1,110,356|
| |Wake County|   182| 163.704|  1.542|12,714| 11435.911| 88.148|1,111,761|
| |Guilford County|   158| 294.132|  0.532| 5,959| 11093.240| 81.910| 537,174|
| |Durham County|    80| 248.843|  0.000| 6,409| 19935.425| 105.758| 321,488|
| |Gaston County|    57| 253.865|  3.181| 3,570| 15899.951| 157.791| 224,529|
| |Henderson County|    56| 476.933|  2.433| 1,558| 13268.947| 92.467| 117,417|
| |Forsyth County|    56| 146.484|  1.495| 5,552| 14522.816| 104.258| 382,295|
| |Cumberland County|    56| 166.911|  2.129| 3,425| 10208.370| 146.473| 335,509|
| |Robeson County|    56| 428.708|  3.281| 3,023| 23142.584| 239.508| 130,625|
| |Chatham County|    55| 738.552|  5.755| 1,353| 18168.390| 101.671|  74,470|
| |Buncombe County|    54| 206.745|  3.829| 2,079|  7959.692| 106.654| 261,191|
| |Rowan County|    51| 358.932|  3.016| 2,359| 16602.387| 162.877| 142,088|
| |Cabarrus County|    50| 230.997|  0.000| 2,803| 12949.693| 114.179| 216,453|
| |Duplin County|    49| 834.170|  2.432| 2,027| 34507.414| 34.048|  58,741|
| |Columbus County|    48| 864.740|  0.000|   973| 17529.005| 180.154|  55,508|
| |Orange County|    48| 323.285|  0.962| 1,447|  9745.683| 95.253| 148,476|
| |Johnston County|    45| 214.962|  0.000| 3,435| 16408.791| 89.397| 209,339|
| |Union County|    44| 183.441|  0.596| 3,375| 14070.767| 166.169| 239,859|
| |Alamance County|    42| 247.774|  0.843| 2,639| 15568.495| 160.969| 169,509|
| |Wayne County|    42| 341.100|  0.000| 2,527| 20522.858| 133.424| 123,131|
| |Vance County|    41| 920.624|  0.000|   816| 18322.668| 137.933|  44,535|
| |Harnett County|    40| 294.170|  1.051| 1,412| 10384.185| 130.275| 135,976|
| |Randolph County|    39| 271.461|  1.989| 2,250| 15661.217| 75.572| 143,667|
| |Wilson County|    36| 440.092|  1.746| 1,562| 19095.121| 125.741|  81,801|
| |Catawba County|    33| 206.830|  3.581| 2,265| 14196.088| 129.829| 159,551|
| |Stanly County|    31| 493.583| 11.373| 1,235| 19663.726| 388.953|  62,806|
| |Granville County|    29| 479.791|  4.727| 1,353| 22384.726| 255.258|  60,443|
| |Burke County|    27| 298.392|  0.000| 1,710| 18898.160| 86.834|  90,485|
| |Franklin County|    26| 373.108|  0.000|   929| 13331.420| 129.153|  69,685|
| |Cleveland County|    24| 245.030|  5.834| 1,322| 13497.095| 210.026|  97,947|
| |Haywood County|    24| 385.128| 27.509|   460|  7381.613| 64.188|  62,317|
| |Davidson County|    23| 137.224|  4.262| 1,879| 11210.615| 83.528| 167,609|
| |Brunswick County|    22| 154.040|  1.000| 1,310|  9172.385| 61.016| 142,820|
| |New Hanover County|    21| 89.563|  0.609| 2,704| 11532.245| 84.079| 234,473|
| |Moore County|    20| 198.255|  0.000| 1,093| 10834.655| 118.953| 100,880|
| |McDowell County|    20| 437.101| 18.733|   713| 15582.656| 93.665|  45,756|
| |Pasquotank County|    20| 502.210|  0.000|   447| 11224.387| 165.012|  39,824|
| |Sampson County|    19| 299.067| 11.243| 1,513| 23815.145| 11.243|  63,531|
| |Craven County|    18| 176.230|  8.392|   784|  7675.814| 118.886| 102,139|
| |Wilkes County|    18| 263.112| 14.617|   910| 13301.760| 158.702|  68,412|
| |Iredell County|    17| 93.506|  0.000| 2,010| 11055.741| 149.296| 181,806|
| |Montgomery County|    16| 588.820| 10.515|   701| 25797.667| 299.667|  27,173|
| |Northampton County|    16| 821.229|  0.000|   319| 16373.248|  0.000|  19,483|
| |Pitt County|    14| 77.458|  2.371| 2,278| 12603.601| 203.921| 180,742|
| |Rutherford County|    14| 208.865|  0.000|   820| 12233.511| 157.714|  67,029|
| |Nash County|    14| 148.466|  3.030| 1,333| 14136.037| 231.788|  94,298|
| |Edgecombe County|    13| 252.565|  0.000|   736| 14299.036| 249.789|  51,472|
| |Caldwell County|    13| 158.193|  0.000| 1,277| 15539.439| 107.780|  82,178|
| |Onslow County|    12| 60.625|  1.443| 1,200|  6062.504| 97.433| 197,938|
| |Lee County|    11| 178.054|  0.000| 1,335| 21609.285| 106.370|  61,779|
| |Hertford County|    11| 464.586|  0.000|   401| 16936.267| 343.914|  23,677|
| |Hoke County|    11| 199.153|  5.173|   780| 14121.737| 162.943|  55,234|
| |Lenoir County|    11| 196.608|  0.000|   642| 11474.736| 176.181|  55,949|
| |Lincoln County|    10| 116.129|  1.659|   930| 10800.014| 136.037|  86,111|
| |Surry County|    10| 139.309|  0.000| 1,005| 14000.529| 101.496|  71,783|
| |Richmond County|     9| 200.763|  0.000|   562| 12536.528| 178.456|  44,829|
| |Halifax County|     8| 159.968|  5.713|   754| 15076.985| 154.255|  50,010|
| |Jackson County|     7| 159.315|  6.503|   460| 10469.298| 42.267|  43,938|
| |Bladen County|     7| 213.923|  0.000|   652| 19925.432| 126.608|  32,722|
| |Rockingham County|     6| 65.927|  0.000|   592|  6504.780| 67.497|  91,010|
| |Warren County|     6| 304.090|  0.000|   271| 13734.732| 108.604|  19,731|
| |Yadkin County|     6| 159.291|  0.000|   563| 14946.770| 83.438|  37,667|
| |Martin County|     6| 267.380|  0.000|   282| 12566.845| 152.788|  22,440|
| |Polk County|     6| 289.519|  6.893|   177|  8540.822| 96.506|  20,724|
| |Bertie County|     5| 263.894|  0.000|   317| 16730.881| 339.292|  18,947|
| |Carteret County|     5| 71.970|  0.000|   377|  5426.569| 67.858|  69,473|
| |Davie County|     5| 116.697|  0.000|   437| 10199.318| 50.013|  42,846|
| |Scotland County|     5| 143.583| 12.307|   432| 12405.594| 365.112|  34,823|
| |Jones County|     4| 424.674|  0.000|   113| 11997.027| 303.338|   9,419|
| |Washington County|     4| 345.423|  0.000|   142| 12262.522| 111.029|  11,580|
| |Cherokee County|     4| 139.801|  0.000|   294| 10275.409| 104.851|  28,612|
| |Pender County|     3| 47.574|  0.000|   696| 11037.108| 86.086|  63,060|
| |Mitchell County|     3| 200.481|  9.547|    80|  5346.164|  0.000|  14,964|
| |Greene County|     3| 142.389|  0.000|   342| 16232.379| 74.585|  21,069|
| |Stokes County|     3| 65.802|  0.000|   304|  6667.983| 40.735|  45,591|
| |Anson County|     3| 122.719|  0.000|   374| 15299.026| 268.814|  24,446|
| |Gates County|     2| 172.980|  0.000|    55|  4756.962| 111.202|  11,562|
| |Perquimans County|     2| 148.555|  0.000|    93|  6907.821| 74.278|  13,463|
| |Person County|     2| 50.646|  0.000|   247|  6254.748| 86.821|  39,490|
| |Dare County|     2| 54.041|  0.000|   212|  5728.336| 11.580|  37,009|
| |Macon County|     2| 55.776|  0.000|   478| 13330.359| 59.760|  35,858|
| |Alexander County|     2| 53.338|  0.000|   338|  9014.054| 148.583|  37,497|
| |Beaufort County|     2| 42.559|  0.000|   448|  9533.132| 127.676|  46,994|
| |Camden County|     2| 184.043|  0.000|    76|  6993.651| 52.584|  10,867|
| |Caswell County|     2| 88.480|  0.000|   201|  8892.231| 37.920|  22,604|
| |Chowan County|     2| 143.441| 10.246|   166| 11905.616| 92.212|  13,943|
| |Tyrrell County|     2| 498.008| 35.572|   101| 25149.402| 106.716|   4,016|
| |Swain County|     2| 140.144|  0.000|   120|  8408.661| 10.010|  14,271|
| |Ashe County|     1| 36.761|  0.000|   174|  6396.353| 89.276|  27,203|
| |Clay County|     1| 89.039| 12.720|    76|  6766.984|  0.000|  11,231|
| |Madison County|     1| 45.966|  6.567|    49|  2252.356| 26.267|  21,755|
| |Pamlico County|     1| 78.579|  0.000|    74|  5814.867| 67.354|  12,726|
| |Transylvania County|     1| 29.082|  0.000|   161|  4682.274| 99.711|  34,385|
| |Alleghany County|     0|  0.000|  0.000|   179| 16072.551| 153.927|  11,137|
| |Avery County|     0|  0.000|  0.000|   107|  6094.435| 65.094|  17,557|
| |Yancey County|     0|  0.000|  0.000|    80|  4427.472|  0.000|  18,069|
| |Watauga County|     0|  0.000|  0.000|   339|  6034.498| 119.520|  56,177|
| |Hyde County|     0|  0.000|  0.000|    57| 11545.473| 376.168|   4,937|
| |Graham County|     0|  0.000|  0.000|    46|  5449.591| 118.469|   8,441|
| |Currituck County|     0|  0.000|  0.000|    83|  2989.590| 51.456|  27,763|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 2,269| 440.693| N/A|106,497| 20684.194| N/A|5,148,714|
| |Greenville County|   227| 433.585|  5.184|11,252| 21492.067| 91.683| 523,542|
| |Charleston County|   214| 520.167|  6.945|12,879| 31304.842| 192.719| 411,406|
| |Horry County|   169| 477.292|  6.455| 8,865| 25036.644| 109.337| 354,081|
| |Richland County|   168| 404.080|  5.498| 9,365| 22525.069| 203.071| 415,759|
| |Florence County|   130| 940.033| 15.495| 3,753| 27138.033| 327.462| 138,293|
| |Lexington County|   120| 401.674|  4.782| 5,216| 17459.414| 124.806| 298,750|
| |Spartanburg County|   114| 356.490|  4.914| 4,389| 13724.846| 138.039| 319,785|
| |Orangeburg County|    77| 893.531| 21.551| 2,578| 29915.869| 261.925|  86,175|
| |Anderson County|    76| 375.201|  9.168| 2,599| 12830.893| 186.190| 202,558|
| |Berkeley County|    73| 320.306|  4.388| 4,449| 19521.120| 182.405| 227,907|
| |Beaufort County|    60| 312.302|  2.974| 4,359| 22688.708| 188.868| 192,122|
| |Dorchester County|    58| 356.246|  9.652| 3,271| 20091.027| 138.637| 162,809|
| |Clarendon County|    57| 1689.139| 21.167|   902| 26729.886| 270.940|  33,745|
| |Sumter County|    56| 524.733|  6.693| 2,632| 24662.438| 153.939| 106,721|
| |Laurens County|    49| 726.001|  6.350| 1,377| 20402.116| 99.481|  67,493|
| |Aiken County|    46| 269.207|  6.688| 2,121| 12412.800| 211.520| 170,872|
| |Darlington County|    38| 570.416|  6.433| 1,445| 21690.834| 321.663|  66,618|
| |Colleton County|    36| 955.490|  7.583|   850| 22560.183| 136.499|  37,677|
| |York County|    32| 113.888|  1.525| 3,774| 13431.609| 104.736| 280,979|
| |Williamsburg County|    31| 1020.811|  0.000| 1,086| 35761.328| 329.294|  30,368|
| |Cherokee County|    31| 541.012|  7.479|   717| 12513.089| 196.958|  57,300|
| |Lee County|    30| 1782.743|  8.489|   586| 34822.914| 203.742|  16,828|
| |Pickens County|    29| 228.555|  2.252| 1,929| 15202.862| 88.945| 126,884|
| |Lancaster County|    27| 275.476|  2.915| 1,375| 14028.894| 241.953|  98,012|
| |Bamberg County|    27| 1919.522| 50.781|   490| 34835.774| 172.655|  14,066|
| |Kershaw County|    27| 405.704|  4.293| 1,455| 21862.932| 130.941|  66,551|
| |Dillon County|    26| 853.046|  9.374|   679| 22277.634| 173.422|  30,479|
| |Georgetown County|    25| 398.851| 13.675| 1,535| 24489.470| 184.611|  62,680|
| |Fairfield County|    24| 1073.970|  6.393|   585| 26178.010| 115.068|  22,347|
| |Chesterfield County|    22| 481.928|  3.129|   826| 18094.195| 178.376|  45,650|
| |Greenwood County|    20| 282.442|  4.035| 1,544| 21804.522| 310.686|  70,811|
| |Jasper County|    19| 631.796| 19.001|   632| 21015.529| 180.513|  30,073|
| |Marion County|    14| 456.666|  4.660|   586| 19114.721| 149.115|  30,657|
| |Chester County|    14| 434.189|  0.000|   744| 23074.060| 350.010|  32,244|
| |Calhoun County|    14| 962.001| 29.449|   396| 27210.884| 157.061|  14,553|
| |Oconee County|    13| 163.427|  7.184|   877| 11025.067| 89.795|  79,546|
| |Hampton County|    13| 676.308| 29.728|   473| 24607.221| 304.710|  19,222|
| |Newberry County|    12| 312.175|  7.433|   892| 23204.995| 174.669|  38,440|
| |Saluda County|    10| 488.448| 13.956|   485| 23689.738| 188.401|  20,473|
| |Barnwell County|     9| 431.324| 27.386|   459| 21997.508| 314.935|  20,866|
| |Abbeville County|     8| 326.171|  0.000|   362| 14759.245| 157.261|  24,527|
| |Edgefield County|     7| 256.787|  0.000|   366| 13426.266| 188.659|  27,260|
| |Allendale County|     6| 690.608| 49.329|   250| 28775.322| 476.848|   8,688|
| |Marlboro County|     5| 191.439|  5.470|   552| 21134.850| 300.832|  26,118|
| |Union County|     4| 146.434|  0.000|   400| 14643.432| 198.732|  27,316|
| |McCormick County|     2| 211.349|  0.000|   140| 14794.463| 332.121|   9,463|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 2,084| 700.234| N/A|72,136| 24238.034| N/A|2,976,149|
| |Hinds County|   128| 552.105|  6.162| 5,902| 25457.212| 178.078| 231,840|
| |Lauderdale County|    98| 1322.091| 11.563| 1,493| 20141.653| 156.107|  74,125|
| |Neshoba County|    96| 3296.930| 19.625| 1,328| 45607.528| 206.058|  29,118|
| |Madison County|    74| 696.326| 10.754| 2,556| 24051.491| 180.131| 106,272|
| |Leflore County|    70| 2483.767| 35.482|   990| 35127.559| 288.928|  28,183|
| |Jones County|    65| 954.507| 14.685| 1,987| 29178.537| 184.608|  68,098|
| |Forrest County|    57| 761.045|  1.907| 1,914| 25555.096| 205.997|  74,897|
| |Monroe County|    55| 1560.195|  0.000|   873| 24764.552| 312.039|  35,252|
| |Holmes County|    50| 2939.447| 16.797|   951| 55908.289| 495.507|  17,010|
| |Jackson County|    47| 327.259|  4.974| 2,462| 17142.817| 185.016| 143,617|
| |Washington County|    46| 1047.621| 16.267| 1,817| 41381.038| 501.036|  43,909|
| |Lincoln County|    45| 1317.600| 16.731|   876| 25649.284| 246.789|  34,153|
| |Lee County|    43| 503.301|  3.344| 1,724| 20178.847| 438.089|  85,436|
| |Lowndes County|    42| 716.785| 12.190| 1,140| 19455.585| 153.597|  58,595|
| |Rankin County|    42| 270.495|  7.360| 2,429| 15643.617| 134.327| 155,271|
| |Pearl River County|    41| 738.273|  5.145|   601| 10822.004| 131.191|  55,535|
| |Oktibbeha County|    41| 826.830|  5.762| 1,178| 23756.226| 161.333|  49,587|
| |Bolivar County|    40| 1305.995| 27.986| 1,221| 39865.483| 503.741|  30,628|
| |Pike County|    38| 967.216|  7.272|   982| 24994.909| 167.263|  39,288|
| |Harrison County|    37| 177.816|  0.687| 2,788| 13398.693| 183.995| 208,080|
| |Warren County|    37| 815.319| 12.592| 1,179| 25980.036| 270.724|  45,381|
| |Simpson County|    36| 1350.439| 32.153|   858| 32185.460| 332.251|  26,658|
| |DeSoto County|    34| 183.838|  2.317| 3,911| 21146.827| 195.425| 184,945|
| |Copiah County|    30| 1068.947| 10.180|   985| 35097.096| 157.797|  28,065|
| |Tate County|    30| 1059.285|  5.044|   773| 27294.234| 196.724|  28,321|
| |Sunflower County|    29| 1154.918| 22.757| 1,115| 44404.620| 432.383|  25,110|
| |Adams County|    28| 912.260| 13.963|   668| 21763.920| 209.447|  30,693|
| |Clarke County|    28| 1801.686| 18.385|   369| 23743.646| 386.076|  15,541|
| |Grenada County|    27| 1300.703| 41.292|   869| 41863.378| 151.405|  20,758|
| |Leake County|    27| 1184.938| 12.539|   811| 35592.030| 144.199|  22,786|
| |Attala County|    25| 1375.592|  0.000|   551| 30318.037| 227.955|  18,174|
| |Walthall County|    22| 1539.969| 20.000|   525| 36749.265| 229.995|  14,286|
| |Scott County|    21| 746.693|  5.080| 1,032| 36694.638| 147.307|  28,124|
| |Marion County|    21| 854.597|  5.814|   708| 28812.111| 180.221|  24,573|
| |Lafayette County|    21| 388.752| 13.223| 1,065| 19715.285| 243.301|  54,019|
| |Wayne County|    21| 1040.480|  0.000|   809| 40083.238| 297.280|  20,183|
| |Lamar County|    20| 315.741| 13.532| 1,291| 20381.100| 160.126|  63,343|
| |Union County|    19| 659.379| 14.873|   763| 26479.264| 629.632|  28,815|
| |Chickasaw County|    19| 1110.916|  0.000|   513| 29994.738| 425.990|  17,103|
| |Panola County|    18| 526.439| 20.890| 1,140| 33341.132| 338.425|  34,192|
| |Winston County|    18| 1002.506| 15.913|   652| 36313.005| 254.605|  17,955|
| |Covington County|    16| 858.553| 22.997|   664| 35629.964| 398.614|  18,636|
| |Hancock County|    15| 314.914|  2.999|   425|  8922.573| 104.971|  47,632|
| |Yazoo County|    14| 471.539|  9.623|   890| 29976.423| 283.886|  29,690|
| |Kemper County|    14| 1437.077|  0.000|   250| 25662.082| 249.289|   9,742|
| |Tippah County|    14| 635.930|  6.489|   438| 19895.526| 467.214|  22,015|
| |Wilkinson County|    14| 1622.248| 16.554|   234| 27114.716| 364.178|   8,630|
| |Clay County|    14| 724.788|  0.000|   417| 21588.321| 155.312|  19,316|
| |Claiborne County|    14| 1557.632| 15.894|   414| 46061.415| 111.259|   8,988|
| |Webster County|    13| 1341.728| 14.744|   257| 26524.925| 339.118|   9,689|
| |Smith County|    13| 816.788|  0.000|   421| 26451.370| 143.611|  15,916|
| |Coahoma County|    13| 587.597|  0.000|   817| 36928.223| 368.055|  22,124|
| |Greene County|    13| 956.867| 10.515|   276| 20315.030| 273.391|  13,586|
| |Tishomingo County|    12| 619.099| 51.592|   469| 24196.461| 383.252|  19,383|
| |Noxubee County|    12| 1151.963| 13.714|   484| 46462.513| 370.274|  10,417|
| |Newton County|    12| 570.939|  6.797|   587| 27928.442| 305.860|  21,018|
| |Humphreys County|    12| 1488.095| 17.715|   312| 38690.476| 336.593|   8,064|
| |Tallahatchie County|    11| 796.582| 10.345|   568| 41132.595| 382.773|  13,809|
| |Prentiss County|    11| 437.794|  5.686|   497| 19780.307| 483.279|  25,126|
| |Carroll County|    11| 1105.861|  0.000|   267| 26842.264| 86.171|   9,947|
| |Jasper County|    11| 671.428| 17.440|   429| 26185.680| 374.953|  16,383|
| |Itawamba County|    10| 427.533|  0.000|   424| 18127.405| 396.995|  23,390|
| |Yalobusha County|    10| 825.900|  0.000|   326| 26924.348| 129.784|  12,108|
| |Montgomery County|    10| 1023.018| 73.073|   366| 37442.455| 584.582|   9,775|
| |Marshall County|    10| 283.334|  4.048|   768| 21760.073| 295.477|  35,294|
| |Calhoun County|     9| 626.697|  0.000|   433| 30151.104| 149.214|  14,361|
| |George County|     9| 367.347| 23.324|   638| 26040.816| 332.362|  24,500|
| |Pontotoc County|     9| 279.729|  4.440|   888| 27599.925| 270.849|  32,174|
| |Lawrence County|     8| 635.627|  0.000|   342| 27173.049| 215.659|  12,586|
| |Jefferson County|     8| 1144.492| 20.437|   198| 28326.180| 40.875|   6,990|
| |Perry County|     8| 668.170| 11.932|   260| 21715.527| 286.359|  11,973|
| |Tunica County|     8| 830.565| 14.832|   381| 39555.648| 652.587|   9,632|
| |Sharkey County|     7| 1619.995| 66.122|   218| 50451.284| 694.284|   4,321|
| |Jefferson Davis County|     6| 539.180|  0.000|   254| 22825.306| 295.265|  11,128|
| |Amite County|     6| 487.924|  0.000|   248| 20167.521| 185.876|  12,297|
| |Stone County|     6| 327.225|  7.791|   255| 13907.068| 436.300|  18,336|
| |Alcorn County|     5| 135.307|  0.000|   457| 12367.061| 112.112|  36,953|
| |Choctaw County|     4| 487.211|  0.000|   141| 17174.178| 121.803|   8,210|
| |Franklin County|     2| 259.302|  0.000|   152| 19706.988| 463.040|   7,713|
| |Issaquena County|     2| 1507.159| 107.654|    28| 21100.226| 215.308|   1,327|
| |Quitman County|     1| 147.232|  0.000|   278| 40930.506| 189.298|   6,792|
| |Benton County|     1| 121.080|  0.000|   166| 20099.286| 380.537|   8,259|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,896| 329.239| N/A|53,157|  9230.671| N/A|5,758,736|
| |Denver County|   420| 577.549| N/A|10,572| 14537.734| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.000| 7,594| 11565.817| 61.574| 656,590|
| |Jefferson County|   235| 403.170|  1.716| 4,414|  7572.729| 58.086| 582,881|
| |Adams County|   184| 355.610|  2.209| 6,816| 13173.025| 89.731| 517,421|
| |Weld County|   145| 446.852|  0.880| 3,825| 11787.656| 51.069| 324,492|
| |El Paso County|   144| 199.888|  1.388| 5,478|  7604.077| 93.598| 720,403|
| |Boulder County|    77| 236.054|  0.876| 2,136|  6548.210| 39.415| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,833|  5219.932| 40.275| 351,154|
| |Morgan County|    47| 1616.898|  4.915|   698| 24012.660| 63.890|  29,068|
| |Larimer County|    36| 100.869|  0.400| 1,687|  4726.827| 53.236| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   754|  4476.797| 51.740| 168,424|
| |Broomfield County|    32| 454.126| N/A|   489|  6939.615| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   304| 14934.172|  7.018|  20,356|
| |Montrose County|    13| 304.037|  0.000|   321|  7507.367| 53.457|  42,758|
| |Eagle County|     9| 163.259|  0.000| 1,152| 20897.201| 75.151|  55,127|
| |Alamosa County|     9| 554.426|  0.000|   233| 14353.477| 26.401|  16,233|
| |Routt County|     8| 312.037|  5.572|   127|  4953.585| 11.144|  25,638|
| |Gunnison County|     7| 400.870|  8.181|   279| 15977.551| 57.267|  17,462|
| |Otero County|     6| 328.263|  0.000|    78|  4267.425| 54.711|  18,278|
| |Mesa County|     5| 32.423|  0.926|   367|  2379.872| 56.509| 154,210|
| |Montezuma County|     5| 190.964|  5.456|   115|  4392.163| 16.368|  26,183|
| |Logan County|     5| 223.125|  0.000|   658| 29363.202| 44.625|  22,409|
| |Garfield County|     4| 66.599|  0.000|   797| 13269.842| 71.356|  60,061|
| |Summit County|     4| 128.986|  0.000|   344| 11092.838| 73.707|  31,011|
| |Teller County|     3| 118.166|  0.000|   146|  5750.748| 78.777|  25,388|
| |Kit Carson County|     3| 422.714|  0.000|    70|  9863.323| 382.455|   7,097|
| |La Plata County|     2| 35.574|  0.000|   228|  4055.424| 40.656|  56,221|
| |Elbert County|     2| 74.825|  0.000|   110|  4115.380| 26.723|  26,729|
| |Saguache County|     2| 293.083|  0.000|   106| 15533.411|  0.000|   6,824|
| |Rio Grande County|     2| 177.510|  0.000|    92|  8165.439| 38.038|  11,267|
| |Pitkin County|     2| 112.568|  0.000|   191| 10750.267| 32.162|  17,767|
| |Park County|     1| 53.064|  0.000|    42|  2228.708|  0.000|  18,845|
| |Huerfano County|     1| 144.991|  0.000|     8|  1159.925|  0.000|   6,897|
| |Moffat County|     1| 75.284|  0.000|    32|  2409.094| 10.755|  13,283|
| |Ouray County|     1| 201.939|  0.000|    13|  2625.202|  0.000|   4,952|
| |Sedgwick County|     1| 444.840|  0.000|    11|  4893.238|  0.000|   2,248|
| |Grand County|     1| 63.557|  0.000|    54|  3432.058| 72.636|  15,734|
| |Delta County|     1| 32.090|  0.000|   133|  4268.019| 55.012|  31,162|
| |Clear Creek County|     1| 103.093|  0.000|    31|  3195.876| 14.728|   9,700|
| |Crowley County|     1| 164.989|  0.000|    73| 12044.217| 23.570|   6,061|
| |Dolores County|     0|  0.000|  0.000|     1|   486.618|  0.000|   2,055|
| |Custer County|     0|  0.000|  0.000|    13|  2565.114| 56.376|   5,068|
| |Costilla County|     0|  0.000|  0.000|    24|  6174.428| 36.753|   3,887|
| |Conejos County|     0|  0.000|  0.000|    27|  3290.676| 69.644|   8,205|
| |Cheyenne County|     0|  0.000|  0.000|     9|  4915.347|  0.000|   1,831|
| |Bent County|     0|  0.000|  0.000|    11|  1972.387| 51.231|   5,577|
| |Baca County|     0|  0.000|  0.000|    15|  4188.774|  0.000|   3,581|
| |Archuleta County|     0|  0.000|  0.000|    40|  2851.237| 40.732|  14,029|
| |Fremont County|     0|  0.000|  0.000|   137|  2863.772| 35.834|  47,839|
| |Gilpin County|     0|  0.000|  0.000|    17|  2723.050| 22.883|   6,243|
| |Hinsdale County|     0|  0.000|  0.000|     3|  3658.537|  0.000|     820|
| |San Juan County|     0|  0.000|  0.000|     2|  2747.253|  0.000|     728|
| |Yuma County|     0|  0.000|  0.000|    63|  6288.053|  0.000|  10,019|
| |Washington County|     0|  0.000|  0.000|    51| 10391.198| 87.321|   4,908|
| |San Miguel County|     0|  0.000|  0.000|    93| 11370.583| 69.865|   8,179|
| |Rio Blanco County|     0|  0.000|  0.000|    20|  3162.555| 90.359|   6,324|
| |Jackson County|     0|  0.000|  0.000|     9|  6465.517|  0.000|   1,392|
| |Prowers County|     0|  0.000|  0.000|    69|  5668.748| 187.785|  12,172|
| |Phillips County|     0|  0.000|  0.000|    19|  4454.865|  0.000|   4,265|
| |Mineral County|     0|  0.000|  0.000|    18| 23407.022|  0.000|     769|
| |Lincoln County|     0|  0.000|  0.000|     8|  1403.263|  0.000|   5,701|
| |Las Animas County|     0|  0.000|  0.000|    18|  1240.866|  9.848|  14,506|
| |Lake County|     0|  0.000|  0.000|    79|  9720.684| 35.156|   8,127|
| |Kiowa County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,406|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,830| 373.227| N/A|104,079| 21226.815| N/A|4,903,185|
| |Jefferson County|   262| 397.830|  4.121|13,988| 21239.863| 190.672| 658,573|
| |Mobile County|   227| 549.357|  6.915|11,022| 26674.088| 371.655| 413,210|
| |Montgomery County|   153| 675.538|  3.154| 7,152| 31578.111| 199.949| 226,486|
| |Tuscaloosa County|    80| 382.126|  4.777| 4,449| 21250.985| 161.039| 209,355|
| |Tallapoosa County|    79| 1957.044|  0.000|   887| 21973.394| 113.247|  40,367|
| |Walker County|    66| 1039.026|  4.498| 1,618| 25471.891| 206.906|  63,521|
| |Lee County|    47| 285.641|  1.736| 2,776| 16871.072| 85.085| 164,542|
| |Elmore County|    39| 480.242|  1.759| 1,826| 22485.193| 181.190|  81,209|
| |Marshall County|    38| 392.667|  2.952| 3,233| 33407.733| 97.429|  96,774|
| |Chambers County|    38| 1142.720|  0.000|   854| 25681.121| 55.847|  33,254|
| |Shelby County|    37| 169.957|  1.312| 3,495| 16054.056| 139.115| 217,702|
| |Butler County|    36| 1851.090|  0.000|   792| 40723.982| 205.677|  19,448|
| |Madison County|    35| 93.857|  0.383| 5,687| 15250.369| 118.374| 372,909|
| |Etowah County|    34| 332.460|  4.191| 2,263| 22128.134| 198.358| 102,268|
| |Baldwin County|    29| 129.909|  2.560| 3,877| 17367.426| 213.101| 223,234|
| |Dale County|    29| 589.767| 14.526|   879| 17876.027| 130.736|  49,172|
| |Marion County|    26| 875.156|  9.617|   606| 20397.859| 153.874|  29,709|
| |Hale County|    26| 1774.623|  0.000|   495| 33786.090| 185.263|  14,651|
| |Dallas County|    25| 672.115|  7.681| 1,363| 36643.725| 153.626|  37,196|
| |Lowndes County|    24| 2467.613|  0.000|   578| 59428.336| 88.129|   9,726|
| |Autauga County|    22| 393.778|  2.557| 1,218| 21800.999| 125.293|  55,869|
| |Franklin County|    22| 701.486|  9.110| 1,351| 43077.610| 350.743|  31,362|
| |Covington County|    21| 566.817|  3.856|   773| 20864.261| 146.524|  37,049|
| |Morgan County|    20| 167.114|  2.387| 2,502| 20905.923| 130.110| 119,679|
| |Lauderdale County|    20| 215.682|  1.541| 1,238| 13350.732| 109.382|  92,729|
| |St. Clair County|    20| 223.434|  4.788| 1,412| 15774.421| 118.101|  89,512|
| |Calhoun County|    19| 167.246|  6.287| 1,919| 16891.862| 169.761| 113,605|
| |Sumter County|    19| 1528.929| 11.496|   374| 30095.759| 160.940|  12,427|
| |Colbert County|    18| 325.845| 12.930| 1,272| 23026.375| 235.332|  55,241|
| |Marengo County|    17| 901.235| 15.147|   585| 31013.094| 249.922|  18,863|
| |Escambia County|    17| 464.062|  0.000| 1,113| 30382.442| 120.890|  36,633|
| |Macon County|    15| 830.197|  7.907|   346| 19149.878| 86.973|  18,068|
| |DeKalb County|    14| 195.769|  1.998| 1,896| 26512.662| 153.818|  71,513|
| |Talladega County|    14| 175.048|  0.000| 1,133| 14166.396| 191.124|  79,978|
| |Limestone County|    13| 131.426|  0.000| 1,449| 14648.941| 167.532|  98,915|
| |Washington County|    13| 796.276|  8.750|   465| 28482.176| 647.521|  16,326|
| |Houston County|    13| 122.778|  1.349| 1,519| 14346.159| 163.255| 105,882|
| |Cullman County|    12| 143.253|  0.000| 1,274| 15208.672| 83.564|  83,768|
| |Choctaw County|    12| 953.213|  0.000|   293| 23274.287| 113.478|  12,589|
| |Bullock County|    11| 1089.001|  0.000|   496| 49104.049| 452.572|  10,101|
| |Greene County|    11| 1356.183|  0.000|   258| 31808.655| 123.289|   8,111|
| |Randolph County|    11| 484.112|  6.287|   409| 18000.176| 50.297|  22,722|
| |Winston County|    11| 465.530|  0.000|   477| 20187.058| 145.100|  23,629|
| |Conecuh County|    10| 828.706|  0.000|   403| 33396.867| 118.387|  12,067|
| |Pickens County|    10| 501.756|  7.168|   436| 21876.568| 258.046|  19,930|
| |Wilcox County|    10| 964.041|  0.000|   449| 43285.453| 275.440|  10,373|
| |Clarke County|    10| 423.334|  6.048|   833| 35263.737| 1034.145|  23,622|
| |Chilton County|     9| 202.575|  9.646|   859| 19334.654| 215.437|  44,428|
| |Cherokee County|     8| 305.390|  5.453|   302| 11528.478| 158.148|  26,196|
| |Crenshaw County|     8| 580.889| 31.119|   349| 25341.272| 321.563|  13,772|
| |Pike County|     7| 211.391|  0.000|   723| 21833.666| 60.397|  33,114|
| |Coffee County|     6| 114.631|  0.000|   812| 15513.354| 139.194|  52,342|
| |Monroe County|     6| 289.394| 13.781|   432| 20836.348| 75.794|  20,733|
| |Barbour County|     6| 243.053|  5.787|   604| 24467.309| 167.822|  24,686|
| |Jackson County|     5| 96.850|  2.767| 1,124| 21771.975| 373.566|  51,626|
| |Fayette County|     5| 306.711|  0.000|   241| 14783.462| 297.948|  16,302|
| |Clay County|     5| 377.786|  0.000|   301| 22742.728| 464.137|  13,235|
| |Bibb County|     5| 223.274|  0.000|   469| 20943.110| 197.757|  22,394|
| |Blount County|     5| 86.466|  2.470|   860| 14872.203| 148.228|  57,826|
| |Perry County|     4| 448.280|  0.000|   456| 51103.889| 224.140|   8,923|
| |Lawrence County|     3| 91.119|  8.678|   370| 11238.003| 91.119|  32,924|
| |Coosa County|     3| 281.347| 13.397|   106|  9940.917| 66.987|  10,663|
| |Henry County|     3| 174.368|  0.000|   275| 15983.726| 99.639|  17,205|
| |Lamar County|     2| 144.875|  0.000|   240| 17385.005| 186.268|  13,805|
| |Russell County|     2| 34.506|  0.000| 1,407| 24274.943| 96.124|  57,961|
| |Geneva County|     2| 76.130|  5.438|   283| 10772.335| 119.632|  26,271|
| |Cleburne County|     1| 67.069|  0.000|   133|  8920.188| 57.488|  14,910|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,776| 233.227| N/A|67,208|  8825.863| N/A|7,614,893|
| |King County|   694| 308.064|  1.205|17,623|  7822.772| 66.775|2,252,782|
| |Yakima County|   221| 880.924|  5.694|10,625| 42352.106| 170.832| 250,873|
| |Snohomish County|   204| 248.150|  1.912| 5,730|  6970.099| 46.050| 822,083|
| |Pierce County|   146| 161.330|  0.947| 6,150|  6795.730| 73.877| 904,980|
| |Benton County|   121| 592.005|  4.194| 3,851| 18841.431| 89.465| 204,390|
| |Spokane County|   106| 202.755|  4.645| 4,791|  9164.151| 95.366| 522,798|
| |Franklin County|    53| 556.594|  6.001| 3,713| 38993.090| 309.052|  95,222|
| |Clark County|    49| 100.360|  1.756| 1,933|  3959.110| 45.645| 488,241|
| |Whatcom County|    39| 170.122|  0.000| 1,024|  4466.798| 21.811| 229,247|
| |Skagit County|    23| 178.012|  2.211|   932|  7213.343| 57.494| 129,205|
| |Kittitas County|    20| 417.232|  2.980|   446|  9304.266| 217.557|  47,935|
| |Grant County|    13| 133.015|  0.000| 1,821| 18632.396| 482.364|  97,733|
| |Island County|    12| 140.943|  1.678|   253|  2971.541|  5.034|  85,141|
| |Thurston County|    11| 37.861|  0.000|   790|  2719.112| 35.894| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,544| 20000.000| 388.601|  77,200|
| |Kitsap County|     7| 25.785|  0.000|   806|  2968.988| 35.257| 271,473|
| |Douglas County|     7| 161.183|  0.000| 1,031| 23739.897| 273.024|  43,429|
| |Adams County|     6| 300.255|  7.149|   504| 25221.438| 457.532|  19,983|
| |Okanogan County|     6| 142.035|  6.764|   924| 21873.446| 202.908|  42,243|
| |Cowlitz County|     5| 45.211|  0.000|   505|  4566.293| 29.710| 110,593|
| |Walla Walla County|     4| 65.833|  2.351|   638| 10500.329| 246.873|  60,760|
| |Lewis County|     4| 49.562|  1.770|   261|  3233.920| 72.573|  80,707|
| |Grays Harbor County|     3| 39.967|  1.903|   142|  1891.795| 41.871|  75,061|
| |Klickitat County|     3| 133.779|  0.000|   134|  5975.474| 133.779|  22,425|
| |Pacific County|     2| 89.004|  0.000|    58|  2581.105| 44.502|  22,471|
| |Asotin County|     2| 88.566|  0.000|    41|  1815.605| 88.566|  22,582|
| |Stevens County|     1| 21.871|  0.000|   117|  2558.887| 21.871|  45,723|
| |Clallam County|     1| 12.931|  1.847|   163|  2107.822| 79.436|  77,331|
| |Columbia County|     1| 250.941|  0.000|    13|  3262.233|  0.000|   3,985|
| |Skamania County|     1| 82.761|  0.000|    58|  4800.132| 11.823|  12,083|
| |Mason County|     1| 14.977|  0.000|   262|  3924.035| 96.282|  66,768|
| |Garfield County|     0|  0.000|  0.000|     4|  1797.753|  0.000|   2,225|
| |Jefferson County|     0|  0.000|  0.000|    59|  1831.104| 22.168|  32,221|
| |Lincoln County|     0|  0.000|  0.000|    31|  2833.897| 52.238|  10,939|
| |Ferry County|     0|  0.000|  0.000|    22|  2884.489|  0.000|   7,627|
| |Pend Oreille County|     0|  0.000|  0.000|    50|  3643.253| 93.684|  13,724|
| |San Juan County|     0|  0.000|  0.000|    30|  1706.291| 16.250|  17,582|
| |Wahkiakum County|     0|  0.000|  0.000|     5|  1114.082|  0.000|   4,488|
| |Whitman County|     0|  0.000|  0.000|   124|  2474.852| 57.024|  50,104|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,706| 302.502| N/A|65,006| 11526.639| N/A|5,639,632|
| |Hennepin County|   848| 669.909|  1.467|20,469| 16170.252| 135.201|1,265,843|
| |Ramsey County|   274| 497.891|  2.336| 8,054| 14635.095| 125.122| 550,321|
| |Anoka County|   115| 322.200|  0.400| 4,013| 11243.384| 132.082| 356,921|
| |Dakota County|   106| 247.074|  0.000| 4,810| 11211.572| 131.862| 429,021|
| |Washington County|    48| 182.899|  1.633| 2,354|  8969.669| 123.021| 262,440|
| |Clay County|    40| 622.840|  0.000|   797| 12410.078| 28.918|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,835| 11592.427| 92.956| 158,293|
| |Scott County|    23| 154.349|  3.835| 1,717| 11522.485| 151.473| 149,013|
| |St. Louis County|    21| 105.491|  1.435|   670|  3365.650| 83.962| 199,070|
| |Stearns County|    20| 124.166|  0.000| 2,957| 18357.908| 56.761| 161,075|
| |Winona County|    17| 336.740|  2.830|   279|  5526.503| 50.936|  50,484|
| |Crow Wing County|    14| 215.203|  0.000|   268|  4119.591| 72.466|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   375| 10941.238| 158.387|  34,274|
| |Itasca County|    12| 265.899|  0.000|   147|  3257.257|  0.000|  45,130|
| |Sherburne County|    10| 102.840|  2.938|   780|  8021.555| 83.742|  97,238|
| |Goodhue County|     9| 194.217|  0.000|   213|  4596.461| 52.408|  46,340|
| |Pipestone County|     9| 986.193|  0.000|   163| 17861.056| 93.923|   9,126|
| |Nobles County|     9| 416.108| 19.815| 1,792| 82851.727| 184.937|  21,629|
| |Rice County|     8| 119.453|  0.000| 1,065| 15902.168| 70.392|  66,972|
| |Martin County|     6| 304.832|  7.258|   211| 10719.911| 29.032|  19,683|
| |Blue Earth County|     6| 88.688|  2.112|   982| 14515.247| 135.143|  67,653|
| |Renville County|     5| 343.690|  0.000|    69|  4742.920| 49.099|  14,548|
| |Wright County|     5| 36.133|  0.000|   976|  7053.195| 94.979| 138,377|
| |Grant County|     4| 669.792| 23.921|    57|  9544.541| 47.842|   5,972|
| |Otter Tail County|     4| 68.090|  2.432|   217|  3693.869| 55.931|  58,746|
| |Polk County|     4| 127.535|  0.000|   161|  5133.274| 36.439|  31,364|
| |Benton County|     3| 73.369|  0.000|   332|  8119.543| 41.925|  40,889|
| |Wilkin County|     3| 483.325|  0.000|    39|  6283.229| 115.077|   6,207|
| |Cass County|     3| 100.742|  4.797|    80|  2686.457| 38.378|  29,779|
| |Carver County|     3| 28.547|  0.000|   954|  9078.020| 126.423| 105,089|
| |Mille Lacs County|     3| 114.168|  0.000|    78|  2968.375| 38.056|  26,277|
| |Koochiching County|     3| 245.319|  0.000|    84|  6868.918| 81.773|  12,229|
| |Kanabec County|     3| 183.632| 17.489|    41|  2509.641| 43.722|  16,337|
| |Lyon County|     3| 117.767|  0.000|   430| 16879.956| 28.040|  25,474|
| |Watonwan County|     2| 183.537| 26.220|   391| 35881.435| 1088.111|  10,897|
| |Mower County|     2| 49.923|  0.000| 1,126| 28106.435| 89.148|  40,062|
| |Todd County|     2| 81.090|  0.000|   435| 17637.042| 52.129|  24,664|
| |Steele County|     2| 54.572|  0.000|   367| 10013.916| 74.062|  36,649|
| |Sibley County|     2| 134.544|  0.000|    89|  5987.218| 57.662|  14,865|
| |Brown County|     2| 79.974|  0.000|    99|  3958.733| 57.125|  25,008|
| |Meeker County|     2| 86.125|  0.000|    90|  3875.635| 30.759|  23,222|
| |Douglas County|     1| 26.219|  0.000|   147|  3854.120| 11.237|  38,141|
| |Mahnomen County|     1| 180.930|  0.000|    28|  5066.039| 25.847|   5,527|
| |Le Sueur County|     1| 34.618|  0.000|   248|  8585.177| 138.471|  28,887|
| |Kandiyohi County|     1| 23.149|  0.000|   739| 17106.877| 142.199|  43,199|
| |Freeborn County|     1| 33.024|  0.000|   367| 12119.811| 37.742|  30,281|
| |Chisago County|     1| 17.674|  0.000|   214|  3782.322| 32.824|  56,579|
| |Chippewa County|     1| 84.746|  0.000|   124| 10508.475| 242.131|  11,800|
| |Carlton County|     1| 27.878|  3.983|   156|  4348.917| 75.668|  35,871|
| |Murray County|     1| 122.041|  0.000|   129| 15743.227| 122.041|   8,194|
| |Morrison County|     1| 29.953|  0.000|   103|  3085.126| 47.068|  33,386|
| |Pennington County|     1| 70.827|  0.000|    75|  5311.991|  0.000|  14,119|
| |Becker County|     1| 29.050|  0.000|   165|  4793.307| 33.200|  34,423|
| |Aitkin County|     1| 62.949|  0.000|    42|  2643.837| 17.985|  15,886|
| |Waseca County|     1| 53.729|  7.676|   169|  9080.163| 161.186|  18,612|
| |Swift County|     1| 107.921|  0.000|    58|  6259.443| 77.087|   9,266|
| |Red Lake County|     0|  0.000|  0.000|    26|  6411.837| 70.460|   4,055|
| |Redwood County|     0|  0.000|  0.000|    38|  2504.944| 18.834|  15,170|
| |Rock County|     0|  0.000|  0.000|    90|  9661.836| 76.681|   9,315|
| |Roseau County|     0|  0.000|  0.000|    56|  3692.713| 37.681|  15,165|
| |Stevens County|     0|  0.000|  0.000|    22|  2243.753| 58.279|   9,805|
| |Yellow Medicine County|     0|  0.000|  0.000|    54|  5561.850| 29.428|   9,709|
| |Wadena County|     0|  0.000|  0.000|    29|  2119.573| 20.882|  13,682|
| |Wabasha County|     0|  0.000|  0.000|   101|  4670.088| 59.449|  21,627|
| |Traverse County|     0|  0.000|  0.000|    16|  4909.481| 219.173|   3,259|
| |Big Stone County|     0|  0.000|  0.000|    25|  5009.016| 85.869|   4,991|
| |Beltrami County|     0|  0.000|  0.000|   271|  5742.986| 93.850|  47,188|
| |Lac qui Parle County|     0|  0.000|  0.000|    10|  1509.890| 64.710|   6,623|
| |Dodge County|     0|  0.000|  0.000|   137|  6544.378| 68.242|  20,934|
| |Kittson County|     0|  0.000|  0.000|     3|   697.999|  0.000|   4,298|
| |Jackson County|     0|  0.000|  0.000|    83|  8429.819|  0.000|   9,846|
| |Isanti County|     0|  0.000|  0.000|   147|  3621.046| 77.418|  40,596|
| |Hubbard County|     0|  0.000|  0.000|    37|  1721.651| 26.589|  21,491|
| |Houston County|     0|  0.000|  0.000|    57|  3064.516| 115.207|  18,600|
| |Fillmore County|     0|  0.000|  0.000|    74|  3512.603| 74.592|  21,067|
| |Faribault County|     0|  0.000|  0.000|    95|  6958.178| 83.707|  13,653|
| |Lake of the Woods County|     0|  0.000|  0.000|     7|  1871.658| 190.985|   3,740|
| |Lincoln County|     0|  0.000|  0.000|    61| 10817.521| 76.001|   5,639|
| |McLeod County|     0|  0.000|  0.000|   260|  7243.752| 314.427|  35,893|
| |Marshall County|     0|  0.000|  0.000|    30|  3213.368| 15.302|   9,336|
| |Clearwater County|     0|  0.000|  0.000|    14|  1587.662|  0.000|   8,818|
| |Cook County|     0|  0.000|  0.000|     6|  1098.298| 26.150|   5,463|
| |Cottonwood County|     0|  0.000|  0.000|   182| 16255.806| 51.039|  11,196|
| |Lake County|     0|  0.000|  0.000|    25|  2349.403| 53.701|  10,641|
| |Pope County|     0|  0.000|  0.000|    48|  4267.046|  0.000|  11,249|
| |Pine County|     0|  0.000|  0.000|   132|  4462.626| 14.489|  29,579|
| |Norman County|     0|  0.000|  0.000|    40|  6274.510|  0.000|   6,375|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,340| 196.217| N/A|127,438| 18660.822| N/A|6,829,174|
| |Shelby County|   327| 348.924|  3.506|24,692| 26347.520| 221.641| 937,166|
| |Davidson County|   227| 327.021|  2.881|21,893| 31539.565| 261.988| 694,144|
| |Sumner County|    75| 392.089|  1.494| 3,636| 19008.485| 151.608| 191,283|
| |Rutherford County|    59| 177.558|  2.150| 7,080| 21307.011| 226.570| 332,285|
| |Hamilton County|    59| 160.412|  2.330| 6,801| 18490.827| 259.843| 367,804|
| |Knox County|    42| 89.302|  0.911| 5,231| 11122.380| 191.666| 470,313|
| |Madison County|    26| 265.349| 13.122| 1,330| 13573.645| 332.416|  97,984|
| |Williamson County|    26| 109.055|  0.599| 3,861| 16194.655| 185.753| 238,412|
| |Wilson County|    24| 165.910|  0.988| 2,484| 17171.654| 191.586| 144,657|
| |Robertson County|    21| 292.426|  3.979| 1,638| 22809.241| 159.143|  71,813|
| |Putnam County|    20| 249.237|  3.561| 1,931| 24063.805| 291.963|  80,245|
| |McMinn County|    20| 371.789|  0.000|   609| 11320.965| 164.649|  53,794|
| |Hardeman County|    18| 718.563|  5.703| 1,056| 42155.689| 792.700|  25,050|
| |Sullivan County|    16| 101.043|  1.804| 1,197|  7559.300| 183.141| 158,348|
| |Montgomery County|    16| 76.558|  2.051| 2,150| 10287.426| 144.229| 208,993|
| |Bradley County|    16| 147.997|  5.286| 2,166| 20035.149| 294.673| 108,110|
| |Hamblen County|    15| 231.004|  2.200| 1,494| 23007.977| 215.604|  64,934|
| |Blount County|    15| 112.707|  4.294| 1,477| 11097.920| 186.772| 133,088|
| |Macon County|    13| 528.412|  0.000|   864| 35119.096| 23.227|  24,602|
| |Giles County|    13| 441.216|  0.000|   415| 14084.985| 164.850|  29,464|
| |Tipton County|    12| 194.808|  4.638| 1,256| 20389.941| 111.319|  61,599|
| |Bedford County|    12| 241.386|  2.874|   984| 19793.615| 160.924|  49,713|
| |Monroe County|    10| 214.846|  3.069|   511| 10978.623| 205.638|  46,545|
| |Hawkins County|    10| 176.100|  7.547|   572| 10072.905| 251.571|  56,786|
| |Maury County|    10| 103.748|  4.446| 1,433| 14867.150| 260.853|  96,387|
| |Cheatham County|     9| 221.310|  7.026|   637| 15663.806| 147.540|  40,667|
| |Sevier County|     9| 91.603|  2.908| 2,038| 20743.003| 221.011|  98,250|
| |Dyer County|     9| 242.202|  3.844|   737| 19833.688| 334.470|  37,159|
| |Lauderdale County|     9| 351.110|  5.573|   565| 22041.899| 317.671|  25,633|
| |Greene County|     9| 130.304|  2.068|   605|  8759.357| 233.721|  69,069|
| |Gibson County|     9| 183.176| 11.630|   819| 16669.041| 296.571|  49,133|
| |Fayette County|     8| 194.491|  0.000|   755| 18355.092| 197.964|  41,133|
| |Hardin County|     8| 311.867|  0.000|   510| 19881.491| 217.193|  25,652|
| |Polk County|     8| 475.285| 42.436|   268| 15922.053| 526.209|  16,832|
| |Lawrence County|     7| 158.579|  3.236|   639| 14476.009| 249.196|  44,142|
| |Cumberland County|     7| 115.664|  2.360|   567|  9368.804| 259.654|  60,520|
| |Crockett County|     7| 491.918| 20.078|   303| 21293.043| 341.331|  14,230|
| |Haywood County|     7| 404.531|  8.256|   608| 35136.385| 891.619|  17,304|
| |Warren County|     6| 145.359|  6.922|   592| 14342.128| 214.578|  41,277|
| |Trousdale County|     6| 531.726|  0.000| 1,585| 140464.374| 25.320|  11,284|
| |Anderson County|     6| 77.944|  0.000|   759|  9859.960| 139.186|  76,978|
| |McNairy County|     6| 233.518|  5.560|   419| 16307.309| 227.958|  25,694|
| |Carter County|     6| 106.400|  0.000|   634| 11242.929| 283.733|  56,391|
| |Carroll County|     6| 216.084| 15.435|   394| 14189.506| 411.588|  27,767|
| |White County|     6| 219.419|  5.224|   336| 12287.438| 224.643|  27,345|
| |Weakley County|     5| 150.024|  4.286|   603| 18092.895| 651.533|  33,328|
| |Marion County|     5| 172.968|  4.942|   256|  8855.986| 158.143|  28,907|
| |Cocke County|     5| 138.873| 11.903|   547| 15192.756| 285.683|  36,004|
| |Smith County|     4| 198.442|  0.000|   479| 23763.457| 191.355|  20,157|
| |Coffee County|     4| 70.771|  2.528|   608| 10757.254| 159.236|  56,520|
| |Franklin County|     4| 94.769|  0.000|   380|  9003.033| 169.230|  42,208|
| |Jefferson County|     4| 73.401|  0.000|   650| 11927.700| 214.961|  54,495|
| |Marshall County|     4| 116.364|  4.156|   369| 10734.545| 282.597|  34,375|
| |Obion County|     4| 133.027|  0.000|   665| 22115.800| 475.098|  30,069|
| |Dickson County|     4| 74.145|  5.296|   777| 14402.758| 227.733|  53,948|
| |Loudon County|     3| 55.486|  0.000|   809| 14962.640| 177.026|  54,068|
| |Decatur County|     3| 257.224|  0.000|   239| 20492.155| 318.467|  11,663|
| |Humphreys County|     3| 161.447|  0.000|   140|  7534.173| 123.007|  18,582|
| |Henderson County|     3| 106.697|  5.081|   684| 24326.920| 462.354|  28,117|
| |Wayne County|     2| 119.954|  0.000|   236| 14154.621| 85.682|  16,673|
| |Washington County|     2| 15.459|  0.000| 1,455| 11246.377| 224.155| 129,375|
| |Benton County|     2| 123.762|  8.840|   183| 11324.257| 247.525|  16,160|
| |Bledsoe County|     2| 132.767|  9.483|   749| 49721.190| 417.267|  15,064|
| |Scott County|     2| 90.629| 12.947|   142|  6434.657| 148.890|  22,068|
| |DeKalb County|     2| 97.609|  0.000|   387| 18887.262| 188.245|  20,490|
| |Grundy County|     2| 148.954|  0.000|   130|  9681.984| 170.233|  13,427|
| |Hancock County|     2| 302.115|  0.000|    84| 12688.822| 86.319|   6,620|
| |Chester County|     2| 115.627|  0.000|   274| 15840.897| 437.731|  17,297|
| |Rhea County|     2| 60.301|  0.000|   581| 17517.412| 193.824|  33,167|
| |Roane County|     2| 37.466|  0.000|   533|  9984.639| 155.216|  53,382|
| |Henry County|     1| 30.917|  4.417|   328| 10140.671| 176.667|  32,345|
| |Hickman County|     1| 39.717|  5.674|   305| 12113.750| 209.934|  25,178|
| |Lewis County|     1| 81.513|  0.000|    88|  7173.133| 151.381|  12,268|
| |Overton County|     1| 44.962|  0.000|   272| 12229.666| 494.582|  22,241|
| |Morgan County|     1| 46.722|  0.000|   141|  6587.862| 126.818|  21,403|
| |Campbell County|     1| 25.099|  0.000|   271|  6801.867| 82.469|  39,842|
| |Claiborne County|     1| 31.290|  4.470|   306|  9574.768| 151.980|  31,959|
| |Lincoln County|     1| 29.099|  0.000|   344| 10009.893| 174.591|  34,366|
| |Sequatchie County|     1| 66.551|  9.507|   122|  8119.260| 161.625|  15,026|
| |Lake County|     1| 142.531| 20.362|   801| 114167.617| 285.063|   7,016|
| |Grainger County|     1| 42.882|  6.126|   219|  9391.081| 134.771|  23,320|
| |Jackson County|     1| 84.846|  0.000|   149| 12642.118| 266.660|  11,786|
| |Pickett County|     1| 198.098|  0.000|    38|  7527.734| 84.899|   5,048|
| |Johnson County|     0|  0.000|  0.000|   349| 19619.969| 554.146|  17,788|
| |Houston County|     0|  0.000|  0.000|    66|  8047.799| 121.936|   8,201|
| |Meigs County|     0|  0.000|  0.000|   121|  9740.782| 172.505|  12,422|
| |Fentress County|     0|  0.000|  0.000|   122|  6586.406| 223.660|  18,523|
| |Clay County|     0|  0.000|  0.000|    89| 11687.459| 243.880|   7,615|
| |Cannon County|     0|  0.000|  0.000|   163| 11105.055| 155.724|  14,678|
| |Perry County|     0|  0.000|  0.000|    90| 11144.131| 159.202|   8,076|
| |Van Buren County|     0|  0.000|  0.000|    45|  7663.488| 218.957|   5,872|
| |Stewart County|     0|  0.000|  0.000|    82|  5978.855| 83.329|  13,715|
| |Unicoi County|     0|  0.000|  0.000|   184| 10289.101| 143.792|  17,883|
| |Union County|     0|  0.000|  0.000|   177|  8862.407| 121.599|  19,972|
| |Moore County|     0|  0.000|  0.000|    75| 11559.803| 264.224|   6,488|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,317| 214.585| N/A|60,547|  9865.207| N/A|6,137,428|
| |St. Louis County|   859| 864.007|  2.586|22,228| 22357.562| 322.296| 994,205|
| |St. Charles County|    91| 226.356|  1.421| 4,649| 11564.044| 212.142| 402,022|
| |Jackson County|    66| 93.882|  0.406| 4,560|  6486.385| 110.951| 703,011|
| |Jasper County|    32| 263.748|  1.177| 1,947| 16047.409| 219.005| 121,328|
| |Clay County|    30| 120.025|  5.715| 1,143|  4572.951| 60.584| 249,948|
| |Jefferson County|    27| 119.957|  1.904| 1,944|  8636.891| 222.777| 225,081|
| |Franklin County|    19| 182.750|  1.374|   742|  7136.880| 170.384| 103,967|
| |Scott County|    13| 339.603|  0.000|   476| 12434.692| 302.284|  38,280|
| |Buchanan County|    10| 114.464|  0.000| 1,129| 12922.943| 73.584|  87,364|
| |Greene County|    10| 34.120|  0.000| 1,902|  6489.563| 188.633| 293,086|
| |Platte County|    10| 95.769|  0.000|   407|  3897.795| 60.198| 104,418|
| |Pemiscot County|     9| 569.440|  0.000|   263| 16640.304| 262.123|  15,805|
| |Gentry County|     9| 1369.655|  0.000|    87| 13239.994| 86.962|   6,571|
| |Cass County|     9| 85.082|  0.000|   863|  8158.442| 163.412| 105,780|
| |Stoddard County|     9| 310.078|  0.000|   242|  8337.640| 54.141|  29,025|
| |McDonald County|     8| 350.309|  6.256|   959| 41993.257| 56.300|  22,837|
| |Camden County|     7| 151.172|  6.170|   408|  8811.144| 178.938|  46,305|
| |Saline County|     7| 307.544|  0.000|   483| 21220.509| 345.202|  22,761|
| |Newton County|     6| 103.029|  0.000|   946| 16244.248| 188.887|  58,236|
| |Cape Girardeau County|     5| 63.395|  0.000|   742|  9407.767| 164.826|  78,871|
| |Pettis County|     5| 118.094|  3.374|   651| 15375.895| 492.622|  42,339|
| |Perry County|     4| 209.030|  0.000|   256| 13377.926| 231.426|  19,136|
| |Dunklin County|     4| 137.311|  0.000|   388| 13319.145| 382.509|  29,131|
| |Barry County|     4| 111.766|  0.000|   293|  8186.873| 155.674|  35,789|
| |Henry County|     3| 137.463|  0.000|    95|  4353.006| 104.734|  21,824|
| |Boone County|     3| 16.624|  0.000| 1,594|  8832.836| 173.364| 180,463|
| |Johnson County|     3| 55.492|  2.642|   513|  9489.105| 68.704|  54,062|
| |Taney County|     3| 53.640|  0.000|   739| 13213.417| 383.146|  55,928|
| |Cole County|     3| 39.090|  0.000|   589|  7674.767| 333.200|  76,745|
| |New Madrid County|     3| 175.685| 16.732|   299| 17509.955| 409.932|  17,076|
| |St. Francois County|     2| 29.755|  0.000|   571|  8495.128| 431.451|  67,215|
| |Lawrence County|     2| 52.144|  0.000|   264|  6883.066| 134.086|  38,355|
| |Benton County|     2| 102.865|  7.347|   117|  6017.590| 168.992|  19,443|
| |Lafayette County|     2| 61.147|  0.000|   198|  6053.565| 87.353|  32,708|
| |Douglas County|     2| 151.688|  0.000|    94|  7129.314| 130.018|  13,185|
| |Butler County|     2| 47.083|  0.000|   317|  7462.687| 121.071|  42,478|
| |Howell County|     2| 49.854|  0.000|   176|  4387.168| 81.903|  40,117|
| |Moniteau County|     2| 123.977|  0.000|   163| 10104.141| 150.544|  16,132|
| |Osage County|     1| 73.448|  0.000|    62|  4553.801| 146.897|  13,615|
| |Pike County|     1| 54.639|  0.000|   144|  7867.993| 351.250|  18,302|
| |Bollinger County|     1| 82.420|  0.000|    81|  6676.008| 153.065|  12,133|
| |Caldwell County|     1| 110.865|  0.000|    36|  3991.131| 15.838|   9,020|
| |Miller County|     1| 39.034|  0.000|   157|  6128.264| 167.287|  25,619|
| |Callaway County|     1| 22.350|  0.000|   198|  4425.273| 130.906|  44,743|
| |Grundy County|     1| 101.523|  0.000|    30|  3045.685| 43.510|   9,850|
| |Laclede County|     1| 27.993|  0.000|   235|  6578.395| 139.966|  35,723|
| |Harrison County|     1| 119.732|  0.000|    62|  7423.372| 34.209|   8,352|
| |DeKalb County|     1| 79.700|  0.000|    41|  3267.713| 68.315|  12,547|
| |Carter County|     1| 167.168|  0.000|    23|  3844.868| 71.644|   5,982|
| |Dallas County|     1| 59.249|  0.000|    76|  4502.903| 76.177|  16,878|
| |Christian County|     1| 11.287|  0.000|   441|  4977.708| 145.123|  88,595|
| |Webster County|     1| 25.258|  0.000|   154|  3889.675| 68.556|  39,592|
| |Washington County|     1| 40.437|  0.000|   133|  5378.083| 323.494|  24,730|
| |Randolph County|     1| 40.407|  0.000|    82|  3313.399| 75.042|  24,748|
| |Texas County|     1| 39.373|  5.625|    67|  2638.003| 84.371|  25,398|
| |Stone County|     1| 31.297|  0.000|   191|  5977.717| 277.202|  31,952|
| |Shannon County|     1| 122.459|  0.000|    44|  5388.195| 17.494|   8,166|
| |Scotland County|     1| 203.998|  0.000|    19|  3875.969| 116.570|   4,902|
| |Ste. Genevieve County|     1| 55.885|  0.000|    69|  3856.041| 103.786|  17,894|
| |Putnam County|     1| 212.947|  0.000|    14|  2981.261| 30.421|   4,696|
| |Pulaski County|     1| 19.009|  0.000|   273|  5189.423| 133.062|  52,607|
| |Bates County|     1| 61.835|  0.000|    54|  3339.105| 61.835|  16,172|
| |Andrew County|     1| 56.459|  0.000|    98|  5532.972| 88.721|  17,712|
| |Lewis County|     1| 102.291|  0.000|    54|  5523.732| 116.904|   9,776|
| |Lincoln County|     1| 16.945|  0.000|   439|  7439.039| 157.350|  59,013|
| |Linn County|     1| 83.893|  0.000|    41|  3439.597| 107.862|  11,920|
| |Marion County|     1| 35.051|  0.000|   269|  9428.672| 380.552|  28,530|
| |Audrain County|     1| 39.389|  0.000|   227|  8941.232| 151.928|  25,388|
| |Mercer County|     0|  0.000|  0.000|    15|  4147.083| 157.984|   3,617|
| |Ozark County|     0|  0.000|  0.000|    16|  1744.059| 62.288|   9,174|
| |Oregon County|     0|  0.000|  0.000|    21|  1994.491| 67.840|  10,529|
| |Nodaway County|     0|  0.000|  0.000|   226| 10229.947| 303.924|  22,092|
| |Morgan County|     0|  0.000|  0.000|    95|  4605.614| 96.960|  20,627|
| |Montgomery County|     0|  0.000|  0.000|    44|  3809.194| 37.103|  11,551|
| |Monroe County|     0|  0.000|  0.000|    37|  4280.426| 132.214|   8,644|
| |Mississippi County|     0|  0.000|  0.000|   172| 13050.076| 401.041|  13,180|
| |Maries County|     0|  0.000|  0.000|    28|  3219.501| 82.130|   8,697|
| |Hickory County|     0|  0.000|  0.000|    40|  4191.115| 134.714|   9,544|
| |Madison County|     0|  0.000|  0.000|    35|  2895.433| 118.181|  12,088|
| |Macon County|     0|  0.000|  0.000|    69|  4564.398| 103.951|  15,117|
| |Livingston County|     0|  0.000|  0.000|    64|  4203.060| 28.145|  15,227|
| |Knox County|     0|  0.000|  0.000|    36|  9093.205| 324.757|   3,959|
| |Iron County|     0|  0.000|  0.000|    25|  2469.136| 42.328|  10,125|
| |Howard County|     0|  0.000|  0.000|    69|  6899.310| 242.833|  10,001|
| |Holt County|     0|  0.000|  0.000|    46| 10447.422| 1232.926|   4,403|
| |Gasconade County|     0|  0.000|  0.000|    37|  2515.980| 126.285|  14,706|
| |Phelps County|     0|  0.000|  0.000|   123|  2759.518| 112.176|  44,573|
| |Daviess County|     0|  0.000|  0.000|    19|  2295.240| 34.515|   8,278|
| |St. Louis city|     0|  0.000|  0.000|     0|     0.000|  0.000| 300,576|
| |Clinton County|     0|  0.000|  0.000|    97|  4757.934| 105.109|  20,387|
| |Reynolds County|     0|  0.000|  0.000|    16|  2551.834|  0.000|   6,270|
| |Ralls County|     0|  0.000|  0.000|    57|  5529.149| 346.438|  10,309|
| |Polk County|     0|  0.000|  0.000|   238|  7403.030| 133.308|  32,149|
| |Carroll County|     0|  0.000|  0.000|   104| 11982.947| 49.380|   8,679|
| |Dade County|     0|  0.000|  0.000|    17|  2248.380| 37.788|   7,561|
| |Crawford County|     0|  0.000|  0.000|   111|  4640.468| 226.947|  23,920|
| |Cooper County|     0|  0.000|  0.000|   159|  8978.486| 274.275|  17,709|
| |Clark County|     0|  0.000|  0.000|    29|  4266.588| 189.159|   6,797|
| |Wright County|     0|  0.000|  0.000|    74|  4046.148| 93.733|  18,289|
| |Chariton County|     0|  0.000|  0.000|    21|  2827.902| 76.950|   7,426|
| |Cedar County|     0|  0.000|  0.000|    45|  3136.107| 49.779|  14,349|
| |Barton County|     0|  0.000|  0.000|    72|  6125.574| 48.616|  11,754|
| |Dent County|     0|  0.000|  0.000|    23|  1476.915| 110.081|  15,573|
| |Atchison County|     0|  0.000|  0.000|    20|  3888.781| 55.554|   5,143|
| |Adair County|     0|  0.000|  0.000|   183|  7220.929| 135.287|  25,343|
| |Worth County|     0|  0.000|  0.000|     9|  4470.939|  0.000|   2,013|
| |Wayne County|     0|  0.000|  0.000|    66|  5127.010| 122.072|  12,873|
| |Warren County|     0|  0.000|  0.000|   248|  6956.717| 208.381|  35,649|
| |Vernon County|     0|  0.000|  0.000|    63|  3063.755| 69.473|  20,563|
| |Sullivan County|     0|  0.000|  0.000|   155| 25455.740| 258.077|   6,089|
| |Shelby County|     0|  0.000|  0.000|    42|  7082.631| 96.362|   5,930|
| |Schuyler County|     0|  0.000|  0.000|    13|  2789.700| 61.312|   4,660|
| |St. Clair County|     0|  0.000|  0.000|    23|  2447.590| 60.810|   9,397|
| |Ripley County|     0|  0.000|  0.000|    75|  5644.190| 247.269|  13,288|
| |Ray County|     0|  0.000|  0.000|   119|  5169.867| 18.619|  23,018|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties| 1,064| 345.437| N/A|60,917| 19777.245| N/A|3,080,156|
| |Clark County|   910| 401.462|  6.491|52,867| 23323.179| 277.368|2,266,715|
| |Washoe County|   125| 265.101|  2.121| 6,191| 13129.906| 131.793| 471,519|
| |Nye County|    12| 257.937|  9.212|   439|  9436.193| 95.191|  46,523|
| |Lyon County|     6| 104.330|  0.000|   269|  4677.447| 111.782|  57,510|
| |Humboldt County|     4| 237.657|  0.000|   104|  6179.074|  0.000|  16,831|
| |Elko County|     3| 56.842|  2.707|   640| 12126.265| 259.849|  52,778|
| |Lander County|     1| 180.766|  0.000|    52|  9399.855| 25.824|   5,532|
| |Churchill County|     1| 40.146|  0.000|    82|  3291.983| 74.557|  24,909|
| |Douglas County|     1| 20.448|  2.921|   216|  4416.726| 37.974|  48,905|
| |White Pine County|     1| 104.384|  0.000|    16|  1670.146|  0.000|   9,580|
| |Storey County|     0|  0.000|  0.000|     6|  1455.251| 69.298|   4,123|
| |Pershing County|     0|  0.000|  0.000|    14|  2081.784|  0.000|   6,725|
| |Mineral County|     0|  0.000|  0.000|    11|  2441.731|  0.000|   4,505|
| |Lincoln County|     0|  0.000|  0.000|     5|   964.692|  0.000|   5,183|
| |Eureka County|     0|  0.000|  0.000|     5|  2464.268| 140.815|   2,029|
| |Esmeralda County|     0|  0.000|  0.000|     0|     0.000|  0.000|     873|
| |Carson City|     0|  0.000|  0.000|     0|     0.000|  0.000|  55,916|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties| 1,039| 178.448| N/A|65,741| 11290.982| N/A|5,822,434|
| |Milwaukee County|   466| 492.743|  1.511|22,212| 23486.718| 173.714| 945,726|
| |Racine County|    81| 412.611|  2.183| 3,676| 18725.390| 117.889| 196,311|
| |Waukesha County|    65| 160.812|  2.474| 4,810| 11900.108| 203.578| 404,198|
| |Kenosha County|    60| 353.855|  0.000| 2,780| 16395.280| 95.204| 169,561|
| |Brown County|    55| 207.906|  0.540| 4,505| 17029.432| 130.144| 264,542|
| |Dane County|    39| 71.338|  0.000| 4,849|  8869.662| 81.790| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,484|  9084.565| 45.475| 163,354|
| |Walworth County|    25| 240.690|  2.751| 1,499| 14431.779| 225.561| 103,868|
| |Washington County|    23| 169.075|  1.050| 1,259|  9255.039| 202.680| 136,034|
| |Winnebago County|    19| 110.525|  0.831| 1,280|  7445.886| 86.425| 171,907|
| |Ozaukee County|    18| 201.746|  1.601|   783|  8775.961| 145.706|  89,221|
| |Waupaca County|    16| 313.787|  2.802|   526| 10315.748| 204.522|  50,990|
| |Grant County|    16| 311.048|  2.777|   396|  7698.439| 111.089|  51,439|
| |Outagamie County|    14| 74.514|  0.000| 1,388|  7387.498| 103.407| 187,885|
| |Marathon County|    12| 88.436|  3.158|   697|  5136.633| 53.693| 135,692|
| |Sheboygan County|     8| 69.360|  0.000|   842|  7300.156| 118.903| 115,340|
| |Clark County|     8| 230.057|  4.108|   197|  5665.152| 53.406|  34,774|
| |Fond du Lac County|     8| 77.367|  1.382|   763|  7378.896| 146.445| 103,403|
| |St. Croix County|     6| 66.162|  1.575|   536|  5910.439| 67.737|  90,687|
| |Jefferson County|     5| 58.984|  0.000|   718|  8470.078| 146.617|  84,769|
| |Marinette County|     5| 123.916|  7.081|   495| 12267.658| 354.045|  40,350|
| |Dodge County|     5| 56.922|  0.000|   930| 10587.552| 180.525|  87,839|
| |Pierce County|     4| 93.558|  6.683|   244|  5707.068| 73.510|  42,754|
| |Richland County|     4| 231.857|  0.000|    38|  2202.643|  8.281|  17,252|
| |Eau Claire County|     4| 38.224|  0.000|   658|  6287.866| 95.560| 104,646|
| |Forest County|     4| 444.247|  0.000|    61|  6774.767| 31.732|   9,004|
| |Sauk County|     3| 46.553|  0.000|   512|  7945.129| 150.745|  64,442|
| |Door County|     3| 108.429|  0.000|   114|  4120.283| 41.306|  27,668|
| |Barron County|     3| 66.307|  0.000|   326|  7205.375| 104.197|  45,244|
| |Taylor County|     2| 98.314|  7.022|    78|  3834.243| 63.202|  20,343|
| |Kewaunee County|     2| 97.876|  0.000|   143|  6998.140| 83.894|  20,434|
| |Monroe County|     2| 43.240|  0.000|   254|  5491.536| 33.975|  46,253|
| |Polk County|     2| 45.680|  0.000|   143|  3266.108| 35.891|  43,783|
| |Wood County|     2| 27.398|  1.957|   379|  5191.852| 172.214|  72,999|
| |Trempealeau County|     2| 67.456|  0.000|   371| 12513.070| 168.640|  29,649|
| |Adams County|     2| 98.912|  0.000|    94|  4648.863| 63.586|  20,220|
| |Columbia County|     2| 34.763|  2.483|   288|  5005.910| 99.324|  57,532|
| |Calumet County|     2| 39.929|  0.000|   403|  8045.679| 236.721|  50,089|
| |Buffalo County|     2| 153.480|  0.000|    47|  3606.784| 43.851|  13,031|
| |Langlade County|     1| 52.113|  0.000|    74|  3856.376| 67.003|  19,189|
| |La Crosse County|     1|  8.473|  0.000|   967|  8193.804| 71.419| 118,016|
| |Juneau County|     1| 37.471|  0.000|   152|  5695.657| 80.296|  26,687|
| |Jackson County|     1| 48.443|  0.000|    62|  3003.439| 27.681|  20,643|
| |Iron County|     1| 175.840|  0.000|    80| 14067.171| 125.600|   5,687|
| |Green County|     1| 27.056|  0.000|   214|  5790.043| 200.989|  36,960|
| |Manitowoc County|     1| 12.661|  0.000|   399|  5051.848| 112.143|  78,981|
| |Ashland County|     1| 64.259|  0.000|    30|  1927.773| 45.899|  15,562|
| |Bayfield County|     1| 66.507|  0.000|    34|  2261.240| 66.507|  15,036|
| |Burnett County|     1| 64.876|  0.000|    27|  1751.654| 46.340|  15,414|
| |Waushara County|     1| 40.912|  0.000|   128|  5236.673| 70.134|  24,443|
| |Rusk County|     1| 70.532|  0.000|    22|  1551.700| 20.152|  14,178|
| |Marquette County|     1| 64.210|  0.000|    81|  5200.976|  9.173|  15,574|
| |Oconto County|     1| 26.364|  3.766|   276|  7276.562| 105.457|  37,930|
| |Oneida County|     0|  0.000|  0.000|   176|  4944.515| 180.603|  35,595|
| |Pepin County|     0|  0.000|  0.000|    46|  6312.611| 78.418|   7,287|
| |Portage County|     0|  0.000|  0.000|   467|  6598.655| 113.039|  70,772|
| |Price County|     0|  0.000|  0.000|    33|  2471.725| 10.700|  13,351|
| |Green Lake County|     0|  0.000|  0.000|    62|  3278.168| 45.320|  18,913|
| |Chippewa County|     0|  0.000|  0.000|   274|  4237.681| 97.215|  64,658|
| |Crawford County|     0|  0.000|  0.000|    86|  5331.350| 97.417|  16,131|
| |Menominee County|     0|  0.000|  0.000|    26|  5706.760| 125.423|   4,556|
| |Iowa County|     0|  0.000|  0.000|   100|  4223.330| 120.667|  23,678|
| |Lafayette County|     0|  0.000|  0.000|   171| 10261.026| 274.313|  16,665|
| |Lincoln County|     0|  0.000|  0.000|    73|  2645.599| 25.886|  27,593|
| |Shawano County|     0|  0.000|  0.000|   217|  5305.753| 73.351|  40,899|
| |Vilas County|     0|  0.000|  0.000|    74|  3334.084| 135.166|  22,195|
| |Washburn County|     0|  0.000|  0.000|    50|  3180.662| 27.263|  15,720|
| |Sawyer County|     0|  0.000|  0.000|   110|  6643.314| 370.990|  16,558|
| |Florence County|     0|  0.000|  0.000|    16|  3725.262| 266.090|   4,295|
| |Dunn County|     0|  0.000|  0.000|   139|  3063.834| 50.382|  45,368|
| |Douglas County|     0|  0.000|  0.000|   223|  5168.019| 165.536|  43,150|
| |Vernon County|     0|  0.000|  0.000|    74|  2400.882| 46.349|  30,822|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   975| 309.026| N/A|52,447| 16623.086| N/A|3,155,070|
| |Polk County|   211| 430.471|  1.166|10,983| 22406.923| 196.437| 490,161|
| |Linn County|    89| 392.579|  0.630| 2,549| 11243.637| 109.645| 226,706|
| |Black Hawk County|    66| 502.941|  0.000| 3,297| 25124.211| 185.065| 131,228|
| |Woodbury County|    54| 523.728|  2.771| 3,807| 36922.808| 121.926| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   891| 20884.118| 147.331|  42,664|
| |Wapello County|    37| 1058.080| 16.341|   955| 27309.903| 224.689|  34,969|
| |Dallas County|    35| 374.520|  0.000| 1,990| 21294.126| 160.508|  93,453|
| |Dubuque County|    31| 318.566|  0.000| 1,797| 18466.566| 177.634|  97,311|
| |Pottawattamie County|    29| 311.139|  4.598| 1,426| 15299.444| 154.803|  93,206|
| |Tama County|    29| 1720.660|  0.000|   562| 33345.200| 93.238|  16,854|
| |Jasper County|    28| 752.992|  7.684|   498| 13392.497| 76.836|  37,185|
| |Marshall County|    27| 685.819|  3.629| 1,509| 38329.650| 235.864|  39,369|
| |Johnson County|    21| 138.944|  1.890| 2,191| 14496.493| 89.794| 151,140|
| |Cerro Gordo County|    19| 447.585|  6.731|   686| 16160.188| 205.284|  42,450|
| |Mahaska County|    17| 769.405|  0.000|   146|  6607.830| 45.259|  22,095|
| |Story County|    15| 154.453|  1.471| 1,398| 14395.008| 341.267|  97,117|
| |Scott County|    15| 86.734|  0.826| 1,853| 10714.513| 111.515| 172,943|
| |Louisa County|    14| 1268.691|  0.000|   378| 34254.644|  0.000|  11,035|
| |Franklin County|    13| 1290.963| 42.559|   265| 26315.789| 340.474|  10,070|
| |Buena Vista County|    12| 611.621|  0.000| 1,804| 91946.993| 72.812|  19,620|
| |Plymouth County|    12| 476.625| 17.022|   509| 20216.865| 266.683|  25,177|
| |Washington County|    10| 455.270|  0.000|   309| 14067.835| 71.542|  21,965|
| |Monroe County|     8| 1038.017| 18.536|    78| 10120.670| 92.680|   7,707|
| |Webster County|     8| 222.816|  3.979|   884| 24621.212| 330.246|  35,904|
| |Poweshiek County|     8| 432.339|  0.000|   163|  8808.906| 30.881|  18,504|
| |Bremer County|     7| 279.307|  0.000|   243|  9695.954| 96.903|  25,062|
| |O'Brien County|     5| 363.557| 31.162|   149| 10834.000| 114.261|  13,753|
| |Lee County|     5| 148.558|  8.489|   154|  4575.571| 169.780|  33,657|
| |Guthrie County|     5| 467.771|  0.000|   147| 13752.456| 200.473|  10,689|
| |Dickinson County|     4| 231.777|  0.000|   390| 22598.215| 74.500|  17,258|
| |Lucas County|     4| 465.116|  0.000|    75|  8720.930| 116.279|   8,600|
| |Henry County|     4| 200.461|  0.000|   166|  8319.134| 293.532|  19,954|
| |Emmet County|     4| 434.405|  0.000|   199| 21611.642| 108.601|   9,208|
| |Clinton County|     4| 86.153|  3.077|   508| 10941.437| 341.535|  46,429|
| |Allamakee County|     4| 292.248|  0.000|   163| 11909.111| 83.499|  13,687|
| |Montgomery County|     4| 403.348|  0.000|    64|  6453.565| 72.026|   9,917|
| |Floyd County|     3| 191.791|  9.133|   178| 11379.619| 210.057|  15,642|
| |Crawford County|     3| 178.359|  0.000|   754| 44827.586| 220.826|  16,820|
| |Clayton County|     3| 170.950|  0.000|   120|  6837.996| 130.248|  17,549|
| |Clarke County|     3| 319.319|  0.000|   212| 22565.194| 167.262|   9,395|
| |Sioux County|     3| 86.071|  0.000|   693| 19882.370| 241.818|  34,855|
| |Appanoose County|     3| 241.429|  0.000|    56|  4506.680| 80.476|  12,426|
| |Boone County|     3| 114.355|  0.000|   293| 11168.712| 190.592|  26,234|
| |Pocahontas County|     2| 302.160|  0.000|   122| 18431.787| 151.080|   6,619|
| |Union County|     2| 163.385| 11.670|    88|  7188.955| 128.374|  12,241|
| |Warren County|     2| 38.861|  2.776|   603| 11716.473| 108.255|  51,466|
| |Hancock County|     2| 188.147|  0.000|   127| 11947.319| 67.195|  10,630|
| |Madison County|     2| 122.414|  0.000|   134|  8201.738| 113.670|  16,338|
| |Butler County|     2| 138.514|  0.000|   140|  9695.962| 187.983|  14,439|
| |Calhoun County|     2| 206.868|  0.000|    95|  9826.231| 177.315|   9,668|
| |Carroll County|     2| 99.182|  7.084|   223| 11058.765| 219.617|  20,165|
| |Cass County|     2| 155.812| 11.129|    94|  7323.154| 222.588|  12,836|
| |Davis County|     2| 222.222|  0.000|    65|  7222.222| 126.984|   9,000|
| |Des Moines County|     2| 51.325|  0.000|   250|  6415.685| 260.294|  38,967|
| |Lyon County|     2| 170.140|  0.000|   128| 10888.983| 182.293|  11,755|
| |Jones County|     2| 96.707|  0.000|   139|  6721.145| 62.169|  20,681|
| |Monona County|     1| 116.077| 16.582|    93| 10795.125| 33.165|   8,615|
| |Clay County|     1| 62.438|  0.000|   215| 13424.076| 222.991|  16,016|
| |Cedar County|     1| 53.686|  0.000|   137|  7354.915| 30.677|  18,627|
| |Benton County|     1| 38.994|  0.000|   171|  6667.966| 83.558|  25,645|
| |Buchanan County|     1| 47.226|  0.000|   150|  7083.825| 155.170|  21,175|
| |Cherokee County|     1| 89.008|  0.000|   113| 10057.855| 63.577|  11,235|
| |Ringgold County|     1| 204.332|  0.000|    24|  4903.964| 58.381|   4,894|
| |Jackson County|     1| 51.443|  0.000|   169|  8693.863| 95.537|  19,439|
| |Keokuk County|     1| 97.599|  0.000|    43|  4196.760| 111.542|  10,246|
| |Mills County|     1| 66.186|  9.455|    98|  6486.200| 85.096|  15,109|
| |Iowa County|     1| 61.789|  0.000|    99|  6117.153| 17.654|  16,184|
| |Humboldt County|     1| 104.624|  0.000|   133| 13915.045| 328.820|   9,558|
| |Harrison County|     1| 71.179|  0.000|   117|  8327.995| 101.685|  14,049|
| |Shelby County|     1| 87.306|  0.000|   194| 16937.314| 124.722|  11,454|
| |Wright County|     1| 79.605|  0.000|   496| 39484.159| 272.932|  12,562|
| |Winneshiek County|     1| 50.023|  0.000|   109|  5452.454| 85.753|  19,991|
| |Van Buren County|     1| 141.965|  0.000|    42|  5962.521| 101.403|   7,044|
| |Delaware County|     1| 58.785|  0.000|   136|  7994.827| 201.550|  17,011|
| |Grundy County|     1| 81.753|  0.000|    91|  7439.503| 140.148|  12,232|
| |Hamilton County|     1| 67.691|  0.000|   262| 17735.057| 154.722|  14,773|
| |Wayne County|     1| 155.255|  0.000|    25|  3881.385| 133.076|   6,441|
| |Audubon County|     1| 181.951|  0.000|    30|  5458.515| 51.986|   5,496|
| |Greene County|     0|  0.000|  0.000|    42|  4725.473| 16.073|   8,888|
| |Howard County|     0|  0.000|  0.000|    65|  7097.620| 249.587|   9,158|
| |Page County|     0|  0.000|  0.000|   101|  6685.642| 66.194|  15,107|
| |Osceola County|     0|  0.000|  0.000|    89| 14937.899| 143.864|   5,958|
| |Mitchell County|     0|  0.000|  0.000|    83|  7840.544| 67.475|  10,586|
| |Marion County|     0|  0.000|  0.000|   209|  6285.147| 154.658|  33,253|
| |Kossuth County|     0|  0.000|  0.000|   106|  7155.877| 144.661|  14,813|
| |Jefferson County|     0|  0.000|  0.000|    91|  4974.037| 54.660|  18,295|
| |Ida County|     0|  0.000|  0.000|    34|  4956.268| 104.123|   6,860|
| |Hardin County|     0|  0.000|  0.000|   194| 11516.087| 110.242|  16,846|
| |Fremont County|     0|  0.000|  0.000|    46|  6609.195| 82.102|   6,960|
| |Fayette County|     0|  0.000|  0.000|   102|  5190.840| 145.402|  19,650|
| |Decatur County|     0|  0.000|  0.000|    29|  3684.879| 108.913|   7,870|
| |Chickasaw County|     0|  0.000|  0.000|    68|  5698.483| 167.602|  11,933|
| |Adams County|     0|  0.000|  0.000|    17|  4719.600| 39.661|   3,602|
| |Adair County|     0|  0.000|  0.000|    38|  5313.199| 159.795|   7,152|
| |Sac County|     0|  0.000|  0.000|    90|  9258.307| 73.479|   9,721|
| |Palo Alto County|     0|  0.000|  0.000|   102| 11478.731| 289.380|   8,886|
| |Taylor County|     0|  0.000|  0.000|   104| 16990.688| 140.033|   6,121|
| |Winnebago County|     0|  0.000|  0.000|   119| 11493.143| 482.905|  10,354|
| |Worth County|     0|  0.000|  0.000|    71|  9619.293| 96.774|   7,381|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   810| 181.302| N/A|38,930|  8713.708| N/A|4,467,673|
| |Jefferson County|   251| 327.353|  2.608| 9,350| 12194.215| 235.873| 766,757|
| |Fayette County|    49| 151.631|  0.884| 3,385| 10474.947| 117.150| 323,152|
| |Kenton County|    41| 245.512|  0.000| 1,507|  9024.060| 82.978| 166,998|
| |Hopkins County|    35| 783.243|  6.394|   439|  9824.106| 57.544|  44,686|
| |Graves County|    26| 697.687|  7.667|   580| 15563.785| 84.336|  37,266|
| |Boone County|    24| 179.666|  0.000| 1,149|  8601.523| 48.125| 133,581|
| |Logan County|    23| 848.646|  0.000|   354| 13061.767| 137.048|  27,102|
| |Warren County|    22| 165.543|  0.000| 2,773| 20865.940| 153.718| 132,896|
| |Shelby County|    21| 428.362|  0.000|   817| 16665.307| 128.217|  49,024|
| |Adair County|    19| 989.480|  0.000|   224| 11665.452| 171.113|  19,202|
| |Oldham County|    16| 239.525|  2.139|   663|  9925.298| 66.297|  66,799|
| |Butler County|    15| 1164.687|  0.000|   303| 23526.671| 110.923|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   155| 11628.779| 53.589|  13,329|
| |Campbell County|    13| 138.913|  0.000|   612|  6539.579| 65.640|  93,584|
| |Edmonson County|    12| 987.654|  0.000|   115|  9465.021| 105.820|  12,150|
| |Grayson County|    11| 416.241|  0.000|   219|  8286.979| 97.303|  26,427|
| |Casey County|    11| 680.735|  8.841|   213| 13181.509| 221.018|  16,159|
| |Muhlenberg County|    11| 359.219|  0.000|   633| 20671.413| 32.656|  30,622|
| |Christian County|    10| 141.922|  4.055|   532|  7550.276| 62.851|  70,461|
| |Daviess County|     9| 88.660|  0.000|   824|  8117.347| 83.031| 101,511|
| |Ohio County|     9| 375.094|  5.954|   365| 15212.136| 53.585|  23,994|
| |Franklin County|     9| 176.502|  5.603|   349|  6844.345| 131.676|  50,991|
| |Knox County|     8| 256.863|  0.000|   268|  8604.913| 151.366|  31,145|
| |Hardin County|     8| 72.099|  0.000|   744|  6705.240| 160.936| 110,958|
| |Allen County|     8| 375.323|  0.000|   234| 10978.184| 53.618|  21,315|
| |Clark County|     7| 193.034|  0.000|   186|  5129.195| 78.789|  36,263|
| |Gallatin County|     7| 789.266|  0.000|    82|  9245.687| 32.215|   8,869|
| |Simpson County|     7| 376.911|  0.000|   167|  8992.031| 130.765|  18,572|
| |Grant County|     6| 239.339|  5.699|   127|  5066.018| 56.986|  25,069|
| |Russell County|     5| 278.971|  0.000|   139|  7755.398| 247.089|  17,923|
| |Pulaski County|     5| 76.948|  0.000|   376|  5786.485| 171.484|  64,979|
| |Laurel County|     5| 82.219|  0.000|   480|  7893.049| 110.409|  60,813|
| |McCracken County|     5| 76.432|  2.184|   401|  6129.811| 76.432|  65,418|
| |Clay County|     5| 251.244|  0.000|   185|  9296.015| 236.887|  19,901|
| |Bullitt County|     5| 61.217|  0.000|   440|  5387.139| 115.439|  81,676|
| |Bell County|     5| 192.071|  5.488|   338| 12984.020| 142.682|  26,032|
| |Lyon County|     4| 487.211|  0.000|    32|  3897.686|  0.000|   8,210|
| |Calloway County|     4| 102.561|  0.000|   289|  7410.066| 172.157|  39,001|
| |Pike County|     3| 51.835|  0.000|   270|  4665.146| 51.835|  57,876|
| |Perry County|     3| 116.469|  0.000|   254|  9861.014| 166.384|  25,758|
| |Henderson County|     3| 66.357|  0.000|   371|  8206.149| 85.316|  45,210|
| |Meade County|     3| 104.998|  5.000|   103|  3604.928| 44.999|  28,572|
| |Harlan County|     3| 115.340|  0.000|   253|  9727.028| 115.340|  26,010|
| |Barren County|     3| 67.798|  3.228|   429|  9695.134| 209.851|  44,249|
| |Boyd County|     3| 64.215|  0.000|   201|  4302.410| 33.636|  46,718|
| |Taylor County|     3| 116.419|  5.544|   153|  5937.367| 121.963|  25,769|
| |Nelson County|     2| 43.259|  0.000|   253|  5472.282| 114.328|  46,233|
| |Monroe County|     2| 187.793|  0.000|   104|  9765.258| 134.138|  10,650|
| |Marshall County|     2| 64.309|  0.000|   155|  4983.923| 82.683|  31,100|
| |Henry County|     2| 124.023|  0.000|   142|  8805.655| 194.894|  16,126|
| |Lincoln County|     2| 81.470|  5.819|   119|  4847.448| 81.470|  24,549|
| |Metcalfe County|     2| 198.590|  0.000|    65|  6454.175| 70.925|  10,071|
| |Breckinridge County|     2| 97.671|  0.000|    84|  4102.163| 97.671|  20,477|
| |Carroll County|     2| 188.129|  0.000|   170| 15990.970| 161.253|  10,631|
| |Carter County|     2| 74.635|  5.331|   105|  3918.349| 21.324|  26,797|
| |Floyd County|     2| 56.197|  0.000|   119|  3343.730| 96.338|  35,589|
| |Fulton County|     2| 335.064|  0.000|    98| 16418.160| 335.064|   5,969|
| |Green County|     2| 182.799|  0.000|    57|  5209.761| 274.198|  10,941|
| |Whitley County|     1| 27.576|  0.000|   170|  4687.845| 27.576|  36,264|
| |Webster County|     1| 77.268|  0.000|    92|  7108.639| 44.153|  12,942|
| |Greenup County|     1| 28.492|  0.000|   139|  3960.340| 118.037|  35,098|
| |Anderson County|     1| 43.962|  0.000|    90|  3956.566| 37.682|  22,747|
| |Lewis County|     1| 75.330| 10.761|    84|  6327.684| 462.739|  13,275|
| |Mason County|     1| 58.582|  0.000|    56|  3280.609| 16.738|  17,070|
| |Larue County|     1| 69.454|  0.000|    66|  4583.970| 119.064|  14,398|
| |Knott County|     1| 67.540|  0.000|    75|  5065.514| 173.675|  14,806|
| |Crittenden County|     1| 113.559|  0.000|    34|  3861.004| 48.668|   8,806|
| |Bourbon County|     1| 50.536|  0.000|    97|  4901.961| 115.510|  19,788|
| |Carlisle County|     1| 210.084|  0.000|    50| 10504.202| 210.084|   4,760|
| |Bath County|     1| 80.000|  0.000|    41|  3280.000| 45.714|  12,500|
| |Clinton County|     1| 97.867|  0.000|    42|  4110.393| 139.809|  10,218|
| |Livingston County|     1| 108.767|  0.000|    36|  3915.597| 15.538|   9,194|
| |Nicholas County|     1| 137.571| 19.653|    21|  2888.981| 19.653|   7,269|
| |Madison County|     1| 10.754|  0.000|   630|  6775.141| 192.039|  92,987|
| |McLean County|     1| 108.613|  0.000|    44|  4778.973| 31.032|   9,207|
| |Cumberland County|     0|  0.000|  0.000|    66|  9978.833| 194.393|   6,614|
| |Hart County|     0|  0.000|  0.000|   109|  5726.294| 75.050|  19,035|
| |Harrison County|     0|  0.000|  0.000|   123|  6512.761| 15.128|  18,886|
| |Hancock County|     0|  0.000|  0.000|    52|  5961.935| 32.758|   8,722|
| |Garrard County|     0|  0.000|  0.000|    91|  5151.138| 105.125|  17,666|
| |Fleming County|     0|  0.000|  0.000|    64|  4389.274| 48.987|  14,581|
| |Estill County|     0|  0.000|  0.000|    27|  1914.079| 50.637|  14,106|
| |Elliott County|     0|  0.000|  0.000|    15|  1995.477| 76.018|   7,517|
| |Caldwell County|     0|  0.000|  0.000|    55|  4314.741| 22.414|  12,747|
| |Jessamine County|     0|  0.000|  0.000|   372|  6874.249| 84.476|  54,115|
| |Breathitt County|     0|  0.000|  0.000|    33|  2612.827| 22.622|  12,630|
| |Bracken County|     0|  0.000|  0.000|    37|  4456.221| 51.616|   8,303|
| |Todd County|     0|  0.000|  0.000|    35|  2846.917|  0.000|  12,294|
| |Trigg County|     0|  0.000|  0.000|    59|  4027.029| 48.753|  14,651|
| |Letcher County|     0|  0.000|  0.000|    65|  3015.821| 39.769|  21,553|
| |Leslie County|     0|  0.000|  0.000|    34|  3442.341| 57.854|   9,877|
| |Lee County|     0|  0.000|  0.000|     5|   675.402|  0.000|   7,403|
| |Rockcastle County|     0|  0.000|  0.000|    86|  5151.243| 128.353|  16,695|
| |Scott County|     0|  0.000|  0.000|   426|  7473.160| 122.798|  57,004|
| |Woodford County|     0|  0.000|  0.000|   177|  6620.783| 117.560|  26,734|
| |Spencer County|     0|  0.000|  0.000|   138|  7131.414| 132.883|  19,351|
| |Wolfe County|     0|  0.000|  0.000|    16|  2235.574| 39.921|   7,157|
| |Wayne County|     0|  0.000|  0.000|    77|  3786.947| 77.285|  20,333|
| |Washington County|     0|  0.000|  0.000|   101|  8350.558| 188.980|  12,095|
| |Union County|     0|  0.000|  0.000|    73|  5076.142| 79.470|  14,381|
| |Trimble County|     0|  0.000|  0.000|    35|  4131.744| 50.593|   8,471|
| |Magoffin County|     0|  0.000|  0.000|    49|  4029.274| 117.472|  12,161|
| |McCreary County|     0|  0.000|  0.000|    52|  3017.817| 99.488|  17,231|
| |Marion County|     0|  0.000|  0.000|   129|  6693.302| 74.123|  19,273|
| |Boyle County|     0|  0.000|  0.000|   168|  5588.822| 66.534|  30,060|
| |Hickman County|     0|  0.000|  0.000|    58| 13242.009| 326.158|   4,380|
| |Johnson County|     0|  0.000|  0.000|    83|  3740.761| 218.909|  22,188|
| |Ballard County|     0|  0.000|  0.000|    37|  4690.669| 36.221|   7,888|
| |Lawrence County|     0|  0.000|  0.000|    38|  2480.904| 18.653|  15,317|
| |Martin County|     0|  0.000|  0.000|    41|  3662.349| 63.804|  11,195|
| |Mercer County|     0|  0.000|  0.000|    91|  4148.999| 52.107|  21,933|
| |Robertson County|     0|  0.000|  0.000|     3|  1423.150|  0.000|   2,108|
| |Powell County|     0|  0.000|  0.000|    68|  5502.063| 173.384|  12,359|
| |Pendleton County|     0|  0.000|  0.000|    51|  3495.545| 68.540|  14,590|
| |Owsley County|     0|  0.000|  0.000|    15|  3397.508| 97.072|   4,415|
| |Owen County|     0|  0.000|  0.000|    65|  5962.756| 222.784|  10,901|
| |Morgan County|     0|  0.000|  0.000|    35|  2629.799| 42.936|  13,309|
| |Montgomery County|     0|  0.000|  0.000|   139|  4936.605| 91.325|  28,157|
| |Menifee County|     0|  0.000|  0.000|    28|  4314.995|  0.000|   6,489|
| |Rowan County|     0|  0.000|  0.000|    88|  3597.711| 105.128|  24,460|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   714| 340.514| N/A|22,103| 10541.155| N/A|2,096,829|
| |McKinley County|   233| 3264.814| 16.014| 4,121| 57743.775| 150.129|  71,367|
| |San Juan County|   187| 1508.575|  3.457| 3,102| 25024.605| 66.843| 123,958|
| |Bernalillo County|   137| 201.731|  0.631| 5,337|  7858.688| 42.282| 679,121|
| |Dona Ana County|    35| 160.407|  3.274| 2,630| 12053.438| 119.814| 218,195|
| |Sandoval County|    33| 224.875|  0.000| 1,158|  7891.079| 24.337| 146,748|
| |Cibola County|    19| 712.277|  5.355|   381| 14283.037| 80.332|  26,675|
| |Rio Arriba County|    10| 256.931| 11.011|   326|  8375.941| 29.364|  38,921|
| |Otero County|    10| 148.170|  0.000|   209|  3096.755| 16.934|  67,490|
| |Socorro County|     6| 360.642|  0.000|    75|  4508.024|  8.587|  16,637|
| |Chaves County|     6| 92.858|  0.000|   538|  8326.240| 179.083|  64,615|
| |Lea County|     6| 84.424|  4.020|   922| 12973.125| 293.473|  71,070|
| |Luna County|     5| 210.890| 12.051|   257| 10839.765| 18.076|  23,709|
| |Eddy County|     5| 85.529|  2.444|   373|  6380.431| 175.944|  58,460|
| |Valencia County|     4| 52.159|  0.000|   460|  5998.331| 85.690|  76,688|
| |Santa Fe County|     3| 19.952|  0.000|   695|  4622.301| 42.755| 150,358|
| |Curry County|     2| 40.855|  0.000|   594| 12133.840| 122.564|  48,954|
| |Lincoln County|     2| 102.187|  0.000|   155|  7919.477| 197.075|  19,572|
| |Grant County|     2| 74.080|  0.000|    72|  2666.864|  5.291|  26,998|
| |Union County|     2| 492.732|  0.000|    30|  7390.983|  0.000|   4,059|
| |Taos County|     1| 30.560|  0.000|   115|  3514.348| 30.560|  32,723|
| |Torrance County|     1| 64.679|  0.000|    63|  4074.769| 18.480|  15,461|
| |Catron County|     1| 283.527|  0.000|     6|  1701.162| 40.504|   3,527|
| |Colfax County|     1| 83.745|  0.000|    18|  1507.411|  0.000|  11,941|
| |Quay County|     1| 121.168|  0.000|    50|  6058.403| 276.956|   8,253|
| |Roosevelt County|     1| 54.054|  0.000|   175|  9459.459| 84.942|  18,500|
| |Sierra County|     1| 92.670| 13.239|    34|  3150.774| 26.477|  10,791|
| |Hidalgo County|     0|  0.000|  0.000|    90| 21438.780|  0.000|   4,198|
| |San Miguel County|     0|  0.000|  0.000|    53|  1943.029| 52.373|  27,277|
| |Mora County|     0|  0.000|  0.000|     6|  1327.140|  0.000|   4,521|
| |Los Alamos County|     0|  0.000|  0.000|    24|  1239.093| 14.751|  19,369|
| |Harding County|     0|  0.000|  0.000|     2|  3200.000| 228.571|     625|
| |De Baca County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,748|
| |Guadalupe County|     0|  0.000|  0.000|    32|  7441.860| 33.223|   4,300|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   661| 167.047| N/A|48,335| 12215.151| N/A|3,956,971|
| |Oklahoma County|   131| 164.277|  3.404|11,600| 14546.658| 186.312| 797,434|
| |Tulsa County|   114| 174.967|  1.535|11,375| 17458.315| 199.524| 651,552|
| |Cleveland County|    57| 200.694|  1.006| 3,192| 11238.883| 99.593| 284,014|
| |Washington County|    39| 756.885|  0.000|   696| 13507.482| 177.438|  51,527|
| |McCurtain County|    28| 852.827|  0.000|   895| 27259.990| 178.397|  32,832|
| |Wagoner County|    23| 282.941|  0.000|   960| 11809.716| 175.740|  81,289|
| |Rogers County|    21| 227.128|  7.725| 1,131| 12232.449| 239.488|  92,459|
| |Delaware County|    20| 465.019|  3.322|   469| 10904.694| 142.827|  43,009|
| |Caddo County|    19| 660.594| 14.901|   464| 16132.397| 233.443|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   578|  8500.375| 151.267|  67,997|
| |Creek County|    15| 209.726|  1.997|   681|  9521.546| 169.778|  71,522|
| |Osage County|    12| 255.520|  3.042|   558| 11881.694| 428.909|  46,963|
| |Comanche County|    11| 91.098|  1.183|   884|  7320.972| 62.704| 120,749|
| |Kay County|    11| 252.653|  0.000|   266|  6109.605| 72.187|  43,538|
| |Canadian County|     9| 60.685|  1.927| 1,331|  8974.687| 118.481| 148,306|
| |Pottawatomie County|     9| 123.981|  0.000|   590|  8127.617| 281.416|  72,592|
| |Garfield County|     8| 131.027|  7.019|   609|  9974.450| 367.344|  61,056|
| |Mayes County|     8| 194.647|  6.952|   366|  8905.109| 173.792|  41,100|
| |Greer County|     8| 1400.560|  0.000|    85| 14880.952| 50.020|   5,712|
| |Grady County|     7| 125.372|  0.000|   469|  8399.900| 71.641|  55,834|
| |Texas County|     7| 350.298|  0.000| 1,078| 53945.854| 157.277|  19,983|
| |Jackson County|     7| 285.365| 11.648|   537| 21891.561| 81.533|  24,530|
| |Adair County|     6| 270.343|  0.000|   378| 17031.630| 244.596|  22,194|
| |Carter County|     5| 103.926|  2.969|   367|  7628.193| 86.110|  48,111|
| |Seminole County|     5| 206.118|  0.000|   257| 10594.443| 129.560|  24,258|
| |Garvin County|     4| 144.347|  0.000|   242|  8732.994| 82.484|  27,711|
| |Sequoyah County|     4| 96.226|  0.000|   433| 10416.416| 319.606|  41,569|
| |McClain County|     4| 98.829|  0.000|   480| 11859.465| 141.184|  40,474|
| |Pittsburg County|     4| 91.630|  3.272|   433|  9918.908| 271.616|  43,654|
| |Payne County|     4| 48.909|  0.000|   794|  9708.500| 111.793|  81,784|
| |Lincoln County|     3| 86.017|  4.096|   243|  6967.342| 323.586|  34,877|
| |Okmulgee County|     3| 77.993|  0.000|   505| 13128.818| 141.130|  38,465|
| |Ottawa County|     3| 96.379|  0.000|   417| 13396.730| 220.296|  31,127|
| |Pawnee County|     3| 183.195|  0.000|   166| 10136.786| 252.983|  16,376|
| |Stephens County|     3| 69.536|  0.000|   217|  5029.785| 56.291|  43,143|
| |Latimer County|     2| 198.551| 14.182|   101| 10026.804| 184.368|  10,073|
| |McIntosh County|     2| 102.062|  7.290|   207| 10563.380| 196.833|  19,596|
| |Hughes County|     2| 150.614|  0.000|   178| 13404.624| 441.083|  13,279|
| |Pontotoc County|     2| 52.241|  0.000|   211|  5511.441| 44.778|  38,284|
| |Noble County|     2| 179.678|  0.000|    91|  8175.366| 102.673|  11,131|
| |Bryan County|     2| 41.671|  2.977|   512| 10667.778| 178.590|  47,995|
| |Cherokee County|     2| 41.104|  0.000|   521| 10707.606| 237.816|  48,657|
| |Cotton County|     2| 352.983|  0.000|    21|  3706.318| 75.639|   5,666|
| |Logan County|     1| 20.829|  0.000|   244|  5082.169| 71.412|  48,011|
| |Beckham County|     1| 45.748|  0.000|   102|  4666.270| 274.486|  21,859|
| |Major County|     1| 131.079|  0.000|    40|  5243.151| 112.353|   7,629|
| |Marshall County|     1| 59.063|  0.000|   121|  7146.654| 118.127|  16,931|
| |Atoka County|     1| 72.685| 10.384|    84|  6105.539| 145.370|  13,758|
| |Nowata County|     1| 99.246|  0.000|    62|  6153.235| 70.890|  10,076|
| |Okfuskee County|     1| 83.382|  0.000|    83|  6920.704| 202.499|  11,993|
| |Le Flore County|     1| 20.059|  0.000|   430|  8625.359| 257.901|  49,853|
| |Kiowa County|     1| 114.837|  0.000|    32|  3674.782| 65.621|   8,708|
| |Choctaw County|     1| 68.157|  0.000|   209| 14244.820| 233.681|  14,672|
| |Haskell County|     1| 79.195| 11.314|    88|  6969.193| 339.409|  12,627|
| |Craig County|     1| 70.711| 10.102|    94|  6646.867| 121.219|  14,142|
| |Tillman County|     1| 137.931|  0.000|    59|  8137.931| 19.704|   7,250|
| |Roger Mills County|     1| 279.096|  0.000|     9|  2511.862| 39.871|   3,583|
| |Dewey County|     0|  0.000|  0.000|    13|  2657.943| 87.624|   4,891|
| |Blaine County|     0|  0.000|  0.000|    46|  4878.566| 60.603|   9,429|
| |Harmon County|     0|  0.000|  0.000|    32| 12061.817|  0.000|   2,653|
| |Grant County|     0|  0.000|  0.000|    17|  3923.379| 65.939|   4,333|
| |Ellis County|     0|  0.000|  0.000|     5|  1295.672|  0.000|   3,859|
| |Custer County|     0|  0.000|  0.000|   232|  7999.172| 128.066|  29,003|
| |Coal County|     0|  0.000|  0.000|    46|  8371.247| 285.974|   5,495|
| |Cimarron County|     0|  0.000|  0.000|    11|  5147.403| 668.494|   2,137|
| |Beaver County|     0|  0.000|  0.000|    39|  7343.250| 80.695|   5,311|
| |Alfalfa County|     0|  0.000|  0.000|     6|  1052.262| 75.162|   5,702|
| |Harper County|     0|  0.000|  0.000|    11|  2982.646| 38.736|   3,688|
| |Jefferson County|     0|  0.000|  0.000|    33|  5498.167|  0.000|   6,002|
| |Johnston County|     0|  0.000|  0.000|    54|  4871.448| 90.212|  11,085|
| |Kingfisher County|     0|  0.000|  0.000|   157|  9958.769| 190.295|  15,765|
| |Woodward County|     0|  0.000|  0.000|    52|  2572.856| 106.024|  20,211|
| |Woods County|     0|  0.000|  0.000|    21|  2388.263| 16.247|   8,793|
| |Washita County|     0|  0.000|  0.000|    35|  3206.303| 104.696|  10,916|
| |Pushmataha County|     0|  0.000|  0.000|   117| 10544.340| 115.872|  11,096|
| |Murray County|     0|  0.000|  0.000|    81|  5755.702| 81.209|  14,073|
| |Love County|     0|  0.000|  0.000|    82|  7997.659| 97.532|  10,253|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   599| 198.489| N/A|51,910| 17201.250| N/A|3,017,804|
| |Pulaski County|    88| 224.541|  1.094| 6,085| 15526.484| 183.351| 391,911|
| |Washington County|    53| 221.584|  0.597| 6,430| 26882.732| 78.838| 239,187|
| |Benton County|    43| 154.044|  0.000| 4,917| 17614.754| 73.184| 279,141|
| |Jefferson County|    41| 613.552|  2.138| 1,696| 25380.103| 346.326|  66,824|
| |Crittenden County|    24| 500.469|  2.979| 1,482| 30903.972| 375.352|  47,955|
| |Sebastian County|    22| 172.108|  2.235| 2,435| 19049.184| 289.454| 127,827|
| |Union County|    20| 517.036| 11.079|   556| 14373.610| 210.508|  38,682|
| |Yell County|    17| 796.589| 20.082| 1,088| 50981.678| 147.269|  21,341|
| |Garland County|    17| 171.050|  4.312| 1,182| 11893.023| 250.107|  99,386|
| |Mississippi County|    14| 344.395|  0.000| 1,154| 28387.986| 491.993|  40,651|
| |Hot Spring County|    13| 384.946|  8.460| 1,643| 48651.210| 410.327|  33,771|
| |Craighead County|    13| 117.826|  1.295| 1,482| 13432.186| 178.681| 110,332|
| |Columbia County|    12| 511.574|  6.090|   242| 10316.750| 164.435|  23,457|
| |Lincoln County|    12| 921.376|  0.000| 1,346| 103347.666| 1393.033|  13,024|
| |Pope County|    12| 187.289|  4.459| 1,449| 22615.183| 303.230|  64,072|
| |Sevier County|    11| 646.792|  8.400| 1,058| 62209.678| 579.593|  17,007|
| |Newton County|    11| 1418.806| 92.130|   107| 13801.109| 73.704|   7,753|
| |Randolph County|    11| 612.540| 63.641|   260| 14478.227| 373.888|  17,958|
| |Phillips County|     9| 506.130|  8.034|   349| 19626.589| 249.048|  17,782|
| |Lawrence County|     9| 548.580|  0.000|   230| 14019.261| 156.737|  16,406|
| |Chicot County|     9| 889.504| 14.119|   921| 91025.894| 2654.392|  10,118|
| |Nevada County|     9| 1090.645|  0.000|   147| 17813.863| 86.559|   8,252|
| |Saline County|     8| 65.340|  2.334| 1,267| 10348.179| 257.859| 122,437|
| |Lee County|     8| 903.240|  0.000|   977| 110308.231| 1338.731|   8,857|
| |Carroll County|     7| 246.653|  0.000|   392| 13812.544| 191.282|  28,380|
| |Faulkner County|     6| 47.616|  0.000| 1,397| 11086.686| 105.436| 126,007|
| |Miller County|     5| 115.588|  0.000|   535| 12367.940| 75.958|  43,257|
| |Crawford County|     5| 79.043|  2.258|   736| 11635.076| 246.161|  63,257|
| |Cleburne County|     5| 200.650|  0.000|   225|  9029.255| 143.322|  24,919|
| |Sharp County|     5| 286.664|  0.000|   128|  7338.608| 122.856|  17,442|
| |Ashley County|     5| 254.362|  0.000|   362| 18415.832| 261.630|  19,657|
| |Poinsett County|     4| 170.010|  6.072|   340| 14450.867| 412.882|  23,528|
| |Howard County|     4| 302.984|  0.000|   374| 28329.041| 367.910|  13,202|
| |Bradley County|     4| 371.644| 13.273|   221| 20533.309| 411.463|  10,763|
| |Cross County|     4| 243.620|  0.000|   225| 13703.636| 261.022|  16,419|
| |Clay County|     4| 274.895|  0.000|   146| 10033.675| 98.177|  14,551|
| |White County|     3| 38.094|  1.814|   394|  5002.984| 130.607|  78,753|
| |Ouachita County|     3| 128.304|  6.110|   118|  5046.617| 109.975|  23,382|
| |St. Francis County|     3| 120.029|  0.000| 1,238| 49531.888| 165.754|  24,994|
| |Conway County|     3| 143.913|  0.000|   162|  7771.275| 68.530|  20,846|
| |Greene County|     3| 66.189|  6.304|   534| 11781.577| 182.807|  45,325|
| |Little River County|     3| 244.718| 23.306|   218| 17782.853| 431.170|  12,259|
| |Drew County|     3| 164.663|  0.000|   260| 14270.816| 446.943|  18,219|
| |Lonoke County|     2| 27.282|  0.000|   573|  7816.230| 118.871|  73,309|
| |Madison County|     2| 120.656|  0.000|   278| 16771.236| 68.946|  16,576|
| |Hempstead County|     2| 92.885|  0.000|   267| 12400.149| 185.770|  21,532|
| |Lafayette County|     2| 301.932|  0.000|    59|  8907.005| 107.833|   6,624|
| |Johnson County|     2| 75.250|  0.000|   691| 25998.946| 123.625|  26,578|
| |Independence County|     2| 52.875|  3.777|   614| 16232.650| 366.349|  37,825|
| |Van Buren County|     2| 120.882|  0.000|    55|  3324.267| 17.269|  16,545|
| |Arkansas County|     2| 114.377|  8.170|   247| 14125.586| 245.094|  17,486|
| |Boone County|     2| 53.430|  3.816|   230|  6144.475| 72.512|  37,432|
| |Clark County|     2| 89.606|  6.400|   189|  8467.742| 76.805|  22,320|
| |Cleveland County|     2| 251.383|  0.000|   120| 15082.956| 412.986|   7,956|
| |Franklin County|     2| 112.899|  0.000|   140|  7902.907| 112.899|  17,715|
| |Desha County|     2| 176.041|  0.000|   210| 18484.288| 201.190|  11,361|
| |Dallas County|     2| 285.347| 40.764|    68|  9701.812| 101.910|   7,009|
| |Logan County|     1| 46.585|  0.000|   337| 15699.245| 505.783|  21,466|
| |Jackson County|     1| 59.812|  0.000|   124|  7416.712| 102.535|  16,719|
| |Polk County|     1| 50.090|  0.000|   161|  8064.516| 135.959|  19,964|
| |Stone County|     1| 79.962|  0.000|    86|  6876.699| 194.193|  12,506|
| |Pike County|     1| 93.301|  0.000|   140| 13062.138| 519.820|  10,718|
| |Montgomery County|     1| 111.284|  0.000|    43|  4785.221| 127.182|   8,986|
| |Woodruff County|     0|  0.000|  0.000|    24|  3797.468| 67.812|   6,320|
| |Perry County|     0|  0.000|  0.000|    55|  5260.641| 13.664|  10,455|
| |Monroe County|     0|  0.000|  0.000|    76| 11341.591| 341.100|   6,701|
| |Marion County|     0|  0.000|  0.000|    33|  1976.758| 42.787|  16,694|
| |Izard County|     0|  0.000|  0.000|    61|  4475.750| 83.855|  13,629|
| |Grant County|     0|  0.000|  0.000|   150|  8212.428| 109.499|  18,265|
| |Fulton County|     0|  0.000|  0.000|    48|  3847.079| 68.698|  12,477|
| |Calhoun County|     0|  0.000|  0.000|    16|  3083.446|  0.000|   5,189|
| |Baxter County|     0|  0.000|  0.000|    86|  2050.940| 51.103|  41,932|
| |Searcy County|     0|  0.000|  0.000|    34|  4314.173| 72.507|   7,881|
| |Scott County|     0|  0.000|  0.000|    78|  7586.811| 236.219|  10,281|
| |Prairie County|     0|  0.000|  0.000|   109| 13520.218| 318.957|   8,062|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   597| 845.910| N/A|13,220| 18731.872| N/A| 705,749|
| |District of Columbia|   597| 845.910|  1.215|13,220| 18731.872| 94.530| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   593| 608.977| N/A|16,190| 16626.205| N/A| 973,764|
| |New Castle County|   293| 524.382|  0.511| 7,524| 13465.700| 81.303| 558,753|
| |Sussex County|   192| 819.725|  0.000| 6,181| 26389.156| 208.591| 234,225|
| |Kent County|   108| 597.391|  0.000| 2,485| 13745.533| 156.460| 180,786|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   423| 311.096| N/A| 6,988|  5139.327| N/A|1,359,711|
| |Hillsborough County|   281| 673.821|  0.685| 3,935|  9435.885| 29.118| 417,025|
| |Rockingham County|    96| 309.908|  0.000| 1,723|  5562.209| 14.758| 309,769|
| |Merrimack County|    23| 151.924|  1.887|   472|  3117.755|  7.549| 151,391|
| |Strafford County|    13| 99.515|  0.000|   367|  2809.397|  9.842| 130,633|
| |Belknap County|     4| 65.250|  0.000|   121|  1973.802| 13.982|  61,303|
| |Cheshire County|     3| 39.430|  0.000|   106|  1393.179| 16.898|  76,085|
| |Carroll County|     1| 20.446|  0.000|    96|  1962.789|  5.842|  48,910|
| |Grafton County|     1| 11.125|  0.000|   107|  1190.397|  6.357|  89,886|
| |Sullivan County|     1| 23.177|  0.000|    44|  1019.793| 13.244|  43,146|
| |Coos County|     0|  0.000|  0.000|    17|   538.605|  0.000|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   405| 139.017| N/A|33,885| 11631.084| N/A|2,913,314|
| |Johnson County|   108| 179.283|  1.186| 6,357| 10552.771| 155.094| 602,401|
| |Wyandotte County|   107| 646.803|  6.908| 5,329| 32213.215| 373.920| 165,429|
| |Sedgwick County|    47| 91.078|  0.830| 5,718| 11080.493| 232.539| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,720|  9724.382| 137.304| 176,875|
| |Lyon County|    14| 421.750|  4.304|   703| 21177.888| 25.821|  33,195|
| |Finney County|    11| 301.643|  3.917| 1,730| 47440.151|  0.000|  36,467|
| |Ford County|    10| 297.451|  8.499| 2,206| 65617.657| 582.154|  33,619|
| |Leavenworth County|     9| 110.081|  1.747| 1,549| 18946.158| 157.259|  81,758|
| |Coffey County|     8| 978.115|  0.000|    70|  8558.503| 52.399|   8,179|
| |Phillips County|     8| 1528.468|  0.000|    48|  9170.806|  0.000|   5,234|
| |Saline County|     7| 129.094|  5.269|   385|  7100.177| 34.249|  54,224|
| |Douglas County|     5| 40.897|  0.000|   805|  6584.382| 106.332| 122,259|
| |Montgomery County|     5| 157.089|  0.000|   168|  5278.205|  4.488|  31,829|
| |Riley County|     5| 67.356|  0.000|   451|  6075.547|  0.000|  74,232|
| |Seward County|     4| 186.672|  0.000| 1,189| 55488.146|  0.000|  21,428|
| |Sumner County|     3| 131.372|  0.000|   104|  4554.213| 31.279|  22,836|
| |Barton County|     3| 116.374|  0.000|   149|  5779.898| 55.416|  25,779|
| |Bourbon County|     2| 137.608|  0.000|    78|  5366.726| 49.146|  14,534|
| |Butler County|     2| 29.890|  2.135|   333|  4976.760| 166.533|  66,911|
| |Clay County|     2| 249.938|  0.000|    22|  2749.313| 35.705|   8,002|
| |Cowley County|     2| 57.293|  0.000|   182|  5213.705| 69.571|  34,908|
| |Morton County|     2| 773.096|  0.000|    10|  3865.481| 55.221|   2,587|
| |Geary County|     2| 63.151|  0.000|   223|  7041.364| 374.397|  31,670|
| |Grant County|     2| 279.720|  0.000|   102| 14265.734|  0.000|   7,150|
| |Cherokee County|     1| 50.153|  0.000|   157|  7874.016| 279.424|  19,939|
| |Stanton County|     1| 498.504|  0.000|    40| 19940.179| 1566.728|   2,006|
| |Reno County|     1| 16.130|  0.000|   418|  6742.153| 334.112|  61,998|
| |Franklin County|     1| 39.148|  0.000|   222|  8690.886| 246.074|  25,544|
| |Ellis County|     1| 35.023|  0.000|   153|  5358.456| 60.039|  28,553|
| |Dickinson County|     1| 54.154|  0.000|    47|  2545.218|  0.000|  18,466|
| |Crawford County|     1| 25.761|  0.000|   415| 10690.917| 128.806|  38,818|
| |Trego County|     1| 356.761|  0.000|     7|  2497.324| 50.966|   2,803|
| |Stafford County|     1| 240.616|  0.000|     7|  1684.312| 137.495|   4,156|
| |Marion County|     1| 84.147|  0.000|    59|  4964.658| 132.231|  11,884|
| |McPherson County|     1| 35.036|  0.000|   164|  5745.918| 110.113|  28,542|
| |Labette County|     1| 50.974|  7.282|   153|  7798.960| 145.639|  19,618|
| |Kearny County|     1| 260.552|  0.000|    66| 17196.456| 260.552|   3,838|
| |Jackson County|     1| 75.924|  0.000|   164| 12451.598| 195.234|  13,171|
| |Harvey County|     1| 29.045|  0.000|   224|  6506.143| 124.480|  34,429|
| |Clark County|     1| 501.505|  0.000|    45| 22567.703| 71.644|   1,994|
| |Jewell County|     1| 347.343| 49.620|    13|  4515.457| 99.241|   2,879|
| |Nemaha County|     1| 97.742|  0.000|    50|  4887.108| 13.963|  10,231|
| |Thomas County|     0|  0.000|  0.000|    45|  5786.293| 128.584|   7,777|
| |Rooks County|     0|  0.000|  0.000|    18|  3658.537| 29.036|   4,920|
| |Rice County|     0|  0.000|  0.000|    39|  4089.336| 29.959|   9,537|
| |Republic County|     0|  0.000|  0.000|    31|  6686.799|  0.000|   4,636|
| |Rawlins County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
| |Pratt County|     0|  0.000|  0.000|    35|  3819.293| 31.178|   9,164|
| |Pottawatomie County|     0|  0.000|  0.000|   119|  4880.449| 70.307|  24,383|
| |Pawnee County|     0|  0.000|  0.000|    63|  9822.264| 1247.272|   6,414|
| |Ottawa County|     0|  0.000|  0.000|    37|  6486.676| 75.135|   5,704|
| |Osborne County|     0|  0.000|  0.000|     4|  1169.249|  0.000|   3,421|
| |Osage County|     0|  0.000|  0.000|    47|  2946.893| 62.700|  15,949|
| |Wabaunsee County|     0|  0.000|  0.000|    43|  6204.011| 20.611|   6,931|
| |Wallace County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,518|
| |Rush County|     0|  0.000|  0.000|    10|  3293.808| 188.218|   3,036|
| |Russell County|     0|  0.000|  0.000|    19|  2771.295| 125.021|   6,856|
| |Scott County|     0|  0.000|  0.000|    54| 11196.351| 207.340|   4,823|
| |Sheridan County|     0|  0.000|  0.000|     7|  2776.676|  0.000|   2,521|
| |Stevens County|     0|  0.000|  0.000|    46|  8386.509| 26.045|   5,485|
| |Smith County|     0|  0.000|  0.000|     3|   837.287|  0.000|   3,583|
| |Sherman County|     0|  0.000|  0.000|    17|  2873.078| 48.287|   5,917|
| |Washington County|     0|  0.000|  0.000|     1|   184.980|  0.000|   5,406|
| |Kiowa County|     0|  0.000|  0.000|     8|  3232.323| 57.720|   2,475|
| |Gray County|     0|  0.000|  0.000|    77| 12859.051|  0.000|   5,988|
| |Morris County|     0|  0.000|  0.000|    13|  2313.167| 50.839|   5,620|
| |Lane County|     0|  0.000|  0.000|     6|  3908.795| 93.067|   1,535|
| |Mitchell County|     0|  0.000|  0.000|    28|  4683.057| 23.893|   5,979|
| |Miami County|     0|  0.000|  0.000|   152|  4439.641| 79.279|  34,237|
| |Meade County|     0|  0.000|  0.000|    59| 14629.308| 531.331|   4,033|
| |Marshall County|     0|  0.000|  0.000|    14|  1442.258| 73.585|   9,707|
| |Logan County|     0|  0.000|  0.000|     2|   715.820|  0.000|   2,794|
| |Linn County|     0|  0.000|  0.000|    50|  5153.045| 220.845|   9,703|
| |Lincoln County|     0|  0.000|  0.000|     6|  2025.658|  0.000|   2,962|
| |Greeley County|     0|  0.000|  0.000|     4|  3246.753|  0.000|   1,232|
| |Kingman County|     0|  0.000|  0.000|    25|  3495.526| 159.795|   7,152|
| |Jefferson County|     0|  0.000|  0.000|    89|  4673.633| 97.524|  19,043|
| |Hodgeman County|     0|  0.000|  0.000|    11|  6131.550|  0.000|   1,794|
| |Haskell County|     0|  0.000|  0.000|    49| 12348.790| 180.012|   3,968|
| |Harper County|     0|  0.000|  0.000|    21|  3863.135| 289.078|   5,436|
| |Hamilton County|     0|  0.000|  0.000|    43| 16935.801| 337.591|   2,539|
| |Greenwood County|     0|  0.000|  0.000|    23|  3844.868| 71.644|   5,982|
| |Gove County|     0|  0.000|  0.000|     5|  1896.813|  0.000|   2,636|
| |Allen County|     0|  0.000|  0.000|    22|  1778.640| 80.847|  12,369|
| |Anderson County|     0|  0.000|  0.000|    30|  3817.765| 18.180|   7,858|
| |Woodson County|     0|  0.000|  0.000|    12|  3824.092| 45.525|   3,138|
| |Wilson County|     0|  0.000|  0.000|    14|  1642.229| 50.272|   8,525|
| |Wichita County|     0|  0.000|  0.000|     4|  1887.683|  0.000|   2,119|
| |Norton County|     0|  0.000|  0.000|    23|  4290.244|  0.000|   5,361|
| |Ness County|     0|  0.000|  0.000|     7|  2545.455| 51.948|   2,750|
| |Neosho County|     0|  0.000|  0.000|    67|  4185.669| 80.322|  16,007|
| |Cheyenne County|     0|  0.000|  0.000|     5|  1881.822| 107.533|   2,657|
| |Ellsworth County|     0|  0.000|  0.000|    21|  3441.495|  0.000|   6,102|
| |Elk County|     0|  0.000|  0.000|     1|   395.257|  0.000|   2,530|
| |Edwards County|     0|  0.000|  0.000|    16|  5718.370| 306.341|   2,798|
| |Doniphan County|     0|  0.000|  0.000|    46|  6052.632|  0.000|   7,600|
| |Decatur County|     0|  0.000|  0.000|     5|  1768.659|  0.000|   2,827|
| |Comanche County|     0|  0.000|  0.000|     9|  5294.118| 336.134|   1,700|
| |Cloud County|     0|  0.000|  0.000|    41|  4666.515| 146.337|   8,786|
| |Chautauqua County|     0|  0.000|  0.000|     6|  1846.154| 43.956|   3,250|
| |Graham County|     0|  0.000|  0.000|    18|  7252.216| 115.115|   2,482|
| |Chase County|     0|  0.000|  0.000|    46| 17371.601| 215.796|   2,648|
| |Brown County|     0|  0.000|  0.000|    47|  4914.262| 149.370|   9,564|
| |Barber County|     0|  0.000|  0.000|     4|   903.546|  0.000|   4,427|
| |Atchison County|     0|  0.000|  0.000|    83|  5163.940| 168.872|  16,073|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   388| 91.992| N/A|23,262|  5515.280| N/A|4,217,737|
| |Multnomah County|   102| 125.484|  1.230| 5,330|  6557.135| 72.584| 812,855|
| |Marion County|    73| 209.880|  1.232| 3,204|  9211.714| 120.342| 347,818|
| |Clackamas County|    50| 119.564|  3.416| 1,689|  4038.863| 51.583| 418,187|
| |Umatilla County|    32| 410.520|  7.331| 2,450| 31430.404| 293.228|  77,950|
| |Washington County|    27| 44.881|  0.475| 3,337|  5546.949| 59.129| 601,592|
| |Malheur County|    15| 490.661|  4.673|   905| 29603.219| 570.101|  30,571|
| |Yamhill County|    13| 121.382|  0.000|   517|  4827.264| 76.030| 107,100|
| |Polk County|    12| 139.397|  0.000|   364|  4228.379| 84.634|  86,085|
| |Linn County|    11| 84.779|  1.101|   333|  2566.494| 57.253| 129,749|
| |Deschutes County|    11| 55.642|  0.723|   639|  3232.301| 25.292| 197,692|
| |Lincoln County|     9| 180.137|  0.000|   438|  8766.663| 62.905|  49,962|
| |Benton County|     6| 64.479|  0.000|   186|  1998.861| 26.099|  93,053|
| |Jefferson County|     5| 202.774|  5.794|   411| 16668.018| 295.471|  24,658|
| |Lane County|     4| 10.469|  0.374|   625|  1635.839| 14.956| 382,067|
| |Morrow County|     3| 258.554|  0.000|   407| 35077.135| 615.604|  11,603|
| |Wasco County|     3| 112.435|  0.000|   202|  7570.647| 53.541|  26,682|
| |Klamath County|     2| 29.309|  0.000|   210|  3077.464| 18.842|  68,238|
| |Union County|     2| 74.530|  0.000|   398| 14831.377| 21.294|  26,835|
| |Jackson County|     2|  9.052|  0.000|   559|  2530.053| 60.778| 220,944|
| |Josephine County|     2| 22.861|  0.000|   139|  1588.807| 39.189|  87,487|
| |Columbia County|     1| 19.101|  2.729|   110|  2101.081| 38.201|  52,354|
| |Douglas County|     1|  9.011|  0.000|   160|  1441.701| 11.585| 110,980|
| |Crook County|     1| 40.977|  0.000|    52|  2130.798| 29.269|  24,404|
| |Wallowa County|     1| 138.735|  0.000|    21|  2913.430| 39.638|   7,208|
| |Coos County|     0|  0.000|  0.000|    93|  1442.151|  4.431|  64,487|
| |Sherman County|     0|  0.000|  0.000|    16|  8988.764|  0.000|   1,780|
| |Lake County|     0|  0.000|  0.000|    32|  4066.590|  0.000|   7,869|
| |Hood River County|     0|  0.000|  0.000|   218|  9323.411| 164.962|  23,382|
| |Harney County|     0|  0.000|  0.000|    11|  1487.894| 19.323|   7,393|
| |Grant County|     0|  0.000|  0.000|     4|   555.633|  0.000|   7,199|
| |Gilliam County|     0|  0.000|  0.000|     4|  2092.050|  0.000|   1,912|
| |Curry County|     0|  0.000|  0.000|    19|   828.790| 24.926|  22,925|
| |Clatsop County|     0|  0.000|  0.000|    91|  2262.331| 21.309|  40,224|
| |Wheeler County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,332|
| |Baker County|     0|  0.000|  0.000|    53|  3287.026| 132.899|  16,124|
| |Tillamook County|     0|  0.000|  0.000|    35|  1294.570|  5.284|  27,036|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   361| 186.620| N/A|30,218| 15621.317| N/A|1,934,408|
| |Douglas County|   143| 250.294|  2.750|12,065| 21117.504| 198.785| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,770| 28849.445| 67.525|  61,353|
| |Dakota County|    42| 2097.274|  7.134| 1,943| 97023.869| 135.538|  20,026|
| |Lancaster County|    19| 59.544|  0.895| 3,446| 10799.461| 68.946| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|   103| 11046.761| 45.964|   9,324|
| |Sarpy County|    11| 58.762|  0.000| 2,488| 13290.882| 175.523| 187,196|
| |Adams County|    11| 350.732|  0.000|   365| 11637.917| 54.659|  31,363|
| |Dodge County|    10| 273.486|  3.907|   843| 23054.834| 144.557|  36,565|
| |Dawson County|     9| 381.437|  0.000|   977| 41407.078| 108.982|  23,595|
| |Perkins County|     7| 2421.308|  0.000|    24|  8301.626| 296.487|   2,891|
| |Scotts Bluff County|     6| 168.454|  0.000|   313|  8787.692| 48.130|  35,618|
| |Madison County|     5| 142.454|  0.000|   490| 13960.512| 150.594|  35,099|
| |Howard County|     5| 775.795| 22.166|    57|  8844.065| 44.331|   6,445|
| |Gage County|     4| 185.934|  0.000|    97|  4508.902| 53.124|  21,513|
| |Colfax County|     4| 373.518|  0.000|   708| 66112.616| 93.379|  10,709|
| |Thurston County|     4| 553.710|  0.000|   211| 29208.195| 118.652|   7,224|
| |Custer County|     4| 371.161|  0.000|    57|  5289.041| 145.813|  10,777|
| |Platte County|     3| 89.633|  0.000|   817| 24409.919| 106.705|  33,470|
| |Lincoln County|     2| 57.284|  0.000|   194|  5556.510| 290.510|  34,914|
| |Saline County|     2| 140.607|  0.000|   603| 42393.138| 80.347|  14,224|
| |Saunders County|     2| 92.687|  0.000|   177|  8202.799| 112.548|  21,578|
| |Dixon County|     2| 354.862|  0.000|    57| 10113.556|  0.000|   5,636|
| |Cass County|     2| 76.196|  0.000|   214|  8153.002| 195.933|  26,248|
| |Antelope County|     1| 158.781|  0.000|    21|  3334.392| 45.366|   6,298|
| |Buffalo County|     1| 20.137|  0.000|   500| 10068.668| 244.525|  49,659|
| |Washington County|     1| 48.242|  0.000|   147|  7091.514| 151.616|  20,729|
| |Fillmore County|     1| 183.083|  0.000|    29|  5309.410| 130.774|   5,462|
| |Furnas County|     1| 213.858|  0.000|    17|  3635.586| 61.102|   4,676|
| |Richardson County|     1| 127.146|  0.000|    27|  3432.931| 90.818|   7,865|
| |Seward County|     1| 57.857|  0.000|   133|  7694.978| 115.714|  17,284|
| |Keya Paha County|     0|  0.000|  0.000|     0|     0.000|  0.000|     806|
| |Nuckolls County|     0|  0.000|  0.000|     6|  1446.480| 34.440|   4,148|
| |Nemaha County|     0|  0.000|  0.000|    50|  7171.543| 450.783|   6,972|
| |Nance County|     0|  0.000|  0.000|    10|  2841.716| 81.192|   3,519|
| |Merrick County|     0|  0.000|  0.000|    63|  8123.791| 18.421|   7,755|
| |Red Willow County|     0|  0.000|  0.000|    18|  1678.478| 26.643|  10,724|
| |McPherson County|     0|  0.000|  0.000|     6| 12145.749| 289.184|     494|
| |Loup County|     0|  0.000|  0.000|     0|     0.000|  0.000|     664|
| |Logan County|     0|  0.000|  0.000|     0|     0.000|  0.000|     748|
| |Knox County|     0|  0.000|  0.000|    42|  5040.807| 137.165|   8,332|
| |Kimball County|     0|  0.000|  0.000|    15|  4129.956|  0.000|   3,632|
| |Keith County|     0|  0.000|  0.000|    38|  4729.898| 284.505|   8,034|
| |Webster County|     0|  0.000|  0.000|    10|  2867.795| 40.968|   3,487|
| |Polk County|     0|  0.000|  0.000|    28|  5371.187| 54.808|   5,213|
| |Rock County|     0|  0.000|  0.000|     3|  2210.759|  0.000|   1,357|
| |Johnson County|     0|  0.000|  0.000|    17|  3352.396| 112.686|   5,071|
| |Wheeler County|     0|  0.000|  0.000|     1|  1277.139|  0.000|     783|
| |Otoe County|     0|  0.000|  0.000|    64|  3997.002| 107.063|  16,012|
| |Pawnee County|     0|  0.000|  0.000|     9|  3444.317|  0.000|   2,613|
| |Phelps County|     0|  0.000|  0.000|    45|  4981.182| 126.506|   9,034|
| |Pierce County|     0|  0.000|  0.000|    45|  6295.467| 479.655|   7,148|
| |Morrill County|     0|  0.000|  0.000|    63| 13571.736| 153.875|   4,642|
| |York County|     0|  0.000|  0.000|    94|  6871.847| 156.653|  13,679|
| |Sheridan County|     0|  0.000|  0.000|    12|  2287.457| 81.695|   5,246|
| |Grant County|     0|  0.000|  0.000|     0|     0.000|  0.000|     623|
| |Cedar County|     0|  0.000|  0.000|    28|  3332.540| 102.017|   8,402|
| |Cherry County|     0|  0.000|  0.000|     4|   703.111|  0.000|   5,689|
| |Hooker County|     0|  0.000|  0.000|     4|  5865.103|  0.000|     682|
| |Garfield County|     0|  0.000|  0.000|     6|  3047.232| 217.659|   1,969|
| |Holt County|     0|  0.000|  0.000|    14|  1390.682| 14.191|  10,067|
| |Hitchcock County|     0|  0.000|  0.000|     1|   362.056|  0.000|   2,762|
| |Hayes County|     0|  0.000|  0.000|     0|     0.000|  0.000|     922|
| |Harlan County|     0|  0.000|  0.000|     2|   591.716| 42.265|   3,380|
| |Greeley County|     0|  0.000|  0.000|    10|  4244.482|  0.000|   2,356|
| |Gosper County|     0|  0.000|  0.000|    22| 11055.276| 215.363|   1,990|
| |Wayne County|     0|  0.000|  0.000|    40|  4262.120| 45.666|   9,385|
| |Garden County|     0|  0.000|  0.000|     4|  2177.463|  0.000|   1,837|
| |Cheyenne County|     0|  0.000|  0.000|    26|  2918.070|  0.000|   8,910|
| |Frontier County|     0|  0.000|  0.000|     4|  1522.649| 54.380|   2,627|
| |Franklin County|     0|  0.000|  0.000|    15|  5035.247| 143.864|   2,979|
| |Dundy County|     0|  0.000|  0.000|     2|  1181.335| 84.381|   1,693|
| |Deuel County|     0|  0.000|  0.000|     2|  1114.827|  0.000|   1,794|
| |Dawes County|     0|  0.000|  0.000|    16|  1862.848| 99.795|   8,589|
| |Cuming County|     0|  0.000|  0.000|    72|  8139.272| 80.747|   8,846|
| |Clay County|     0|  0.000|  0.000|    50|  8060.616|  0.000|   6,203|
| |Valley County|     0|  0.000|  0.000|    13|  3126.503| 103.072|   4,158|
| |Thomas County|     0|  0.000|  0.000|     2|  2770.083| 197.863|     722|
| |Thayer County|     0|  0.000|  0.000|    27|  5396.762|  0.000|   5,003|
| |Stanton County|     0|  0.000|  0.000|    33|  5574.324| 96.525|   5,920|
| |Sioux County|     0|  0.000|  0.000|     5|  4288.165|  0.000|   1,166|
| |Sherman County|     0|  0.000|  0.000|    14|  4665.112| 142.810|   3,001|
| |Kearney County|     0|  0.000|  0.000|    83| 12779.061| 681.843|   6,495|
| |Jefferson County|     0|  0.000|  0.000|    19|  2696.565| 40.550|   7,046|
| |Banner County|     0|  0.000|  0.000|     2|  2684.564|  0.000|     745|
| |Butler County|     0|  0.000|  0.000|    66|  8233.533| 106.929|   8,016|
| |Burt County|     0|  0.000|  0.000|    53|  8205.605| 442.351|   6,459|
| |Brown County|     0|  0.000|  0.000|     2|   676.819| 96.688|   2,955|
| |Boyd County|     0|  0.000|  0.000|     8|  4168.838| 297.774|   1,919|
| |Box Butte County|     0|  0.000|  0.000|    16|  1483.817| 52.993|  10,783|
| |Boone County|     0|  0.000|  0.000|    11|  2118.644| 82.545|   5,192|
| |Blaine County|     0|  0.000|  0.000|     0|     0.000|  0.000|     465|
| |Arthur County|     0|  0.000|  0.000|     1|  2159.827|  0.000|     463|
| |Chase County|     0|  0.000|  0.000|     9|  2293.578| 109.218|   3,924|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   301| 93.888| N/A|37,185| 11598.717| N/A|3,205,958|
| |Salt Lake County|   211| 181.828|  2.708|21,771| 18761.036| 140.711|1,160,437|
| |Utah County|    38| 59.726|  0.225| 9,398| 14771.272| 152.459| 636,235|
| |San Juan County|    26| 1698.458|  9.332|   653| 42657.434| 46.661|  15,308|
| |Davis County|    21| 59.075|  0.000| 3,414|  9603.889| 76.355| 355,481|
| |Wasatch County|     4| 117.333|  0.000|   598| 17541.287| 146.666|  34,091|
| |Summit County|     1| 23.728|  0.000|   733| 17392.336| 77.962|  42,145|
| |Sanpete County|     0|  0.000|  0.000|     0|     0.000|  0.000|  30,939|
| |Uintah County|     0|  0.000|  0.000|     0|     0.000|  0.000|  35,734|
| |Tooele County|     0|  0.000|  0.000|   618|  8552.568| 73.150|  72,259|
| |Sevier County|     0|  0.000|  0.000|     0|     0.000|  0.000|  21,620|
| |Washington County|     0|  0.000|  0.000|     0|     0.000|  0.000| 177,556|
| |Wayne County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,711|
| |Weber County|     0|  0.000|  0.000|     0|     0.000|  0.000| 260,213|
| |Millard County|     0|  0.000|  0.000|     0|     0.000|  0.000|  13,188|
| |Daggett County|     0|  0.000|  0.000|     0|     0.000|  0.000|     950|
| |Duchesne County|     0|  0.000|  0.000|     0|     0.000|  0.000|  19,938|
| |Garfield County|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,051|
| |Grand County|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,754|
| |Rich County|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,483|
| |Kane County|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,886|
| |Piute County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,479|
| |Emery County|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,012|
| |Iron County|     0|  0.000|  0.000|     0|     0.000|  0.000|  54,839|
| |Juab County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,017|
| |Morgan County|     0|  0.000|  0.000|     0|     0.000|  0.000|  12,124|
| |Carbon County|     0|  0.000|  0.000|     0|     0.000|  0.000|  20,463|
| |Cache County|     0|  0.000|  0.000|     0|     0.000|  0.000| 128,289|
| |Box Elder County|     0|  0.000|  0.000|     0|     0.000|  0.000|  56,046|
| |Beaver County|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,710|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   269| 150.526| N/A|27,653| 15473.975| N/A|1,787,065|
| |Ada County|    95| 197.264|  4.153| 9,968| 20698.233| 302.274| 481,587|
| |Canyon County|    56| 243.638|  4.972| 6,362| 27679.041| 366.700| 229,849|
| |Twin Falls County|    33| 379.843|  1.644| 1,521| 17507.309| 179.233|  86,878|
| |Kootenai County|    20| 120.702|  3.449| 1,989| 12003.838| 170.707| 165,697|
| |Nez Perce County|    19| 470.204|  0.000|   174|  4306.078| 53.031|  40,408|
| |Blaine County|     6| 260.632|  0.000|   585| 25411.581| 55.850|  23,021|
| |Jerome County|     6| 245.781|  0.000|   525| 21505.817| 298.448|  24,412|
| |Bonneville County|     6| 50.394|  2.400| 1,317| 11061.464| 317.962| 119,062|
| |Shoshone County|     3| 232.883| 11.090|   166| 12886.198| 731.918|  12,882|
| |Elmore County|     3| 109.047|  0.000|   234|  8505.689| 114.240|  27,511|
| |Owyhee County|     3| 253.743|  0.000|   279| 23598.072| 193.328|  11,823|
| |Washington County|     3| 294.291|  0.000|   238| 23347.067| 462.457|  10,194|
| |Payette County|     3| 125.256|  5.965|   447| 18663.104| 375.767|  23,951|
| |Bannock County|     2| 22.777|  0.000|   487|  5546.192| 156.185|  87,808|
| |Bingham County|     2| 42.725|  0.000|   339|  7241.888| 289.920|  46,811|
| |Minidoka County|     2| 95.062|  0.000|   504| 23955.511| 176.543|  21,039|
| |Valley County|     1| 87.781|  0.000|    76|  6671.348| 213.182|  11,392|
| |Cassia County|     1| 41.615|  0.000|   547| 22763.213| 172.404|  24,030|
| |Boise County|     1| 127.698|  0.000|    53|  6767.973| 91.213|   7,831|
| |Benewah County|     1| 107.550| 15.364|    80|  8604.001| 245.829|   9,298|
| |Jefferson County|     1| 33.477|  0.000|   252|  8436.276| 258.253|  29,871|
| |Gem County|     1| 55.212|  0.000|   189| 10435.071| 78.874|  18,112|
| |Gooding County|     1| 65.880|  0.000|   181| 11924.369| 178.818|  15,179|
| |Lewis County|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,838|
| |Bear Lake County|     0|  0.000|  0.000|    21|  3428.571| 139.942|   6,125|
| |Franklin County|     0|  0.000|  0.000|    52|  3747.478| 10.295|  13,876|
| |Madison County|     0|  0.000|  0.000|   190|  4761.069| 89.494|  39,907|
| |Adams County|     0|  0.000|  0.000|    22|  5123.428| 99.807|   4,294|
| |Lincoln County|     0|  0.000|  0.000|    62| 11554.230| 159.736|   5,366|
| |Lemhi County|     0|  0.000|  0.000|    48|  5979.818| 409.333|   8,027|
| |Latah County|     0|  0.000|  0.000|   133|  3316.047| 121.102|  40,108|
| |Idaho County|     0|  0.000|  0.000|    34|  2039.959| 25.714|  16,667|
| |Fremont County|     0|  0.000|  0.000|    94|  7176.120| 109.060|  13,099|
| |Custer County|     0|  0.000|  0.000|    11|  2549.247| 33.107|   4,315|
| |Power County|     0|  0.000|  0.000|    66|  8592.631| 204.586|   7,681|
| |Clearwater County|     0|  0.000|  0.000|    17|  1941.526| 16.315|   8,756|
| |Clark County|     0|  0.000|  0.000|    12| 14201.183| 676.247|     845|
| |Caribou County|     0|  0.000|  0.000|    34|  4751.922| 59.898|   7,155|
| |Camas County|     0|  0.000|  0.000|     1|   904.159|  0.000|   1,106|
| |Butte County|     0|  0.000|  0.000|     1|   385.060| 55.009|   2,597|
| |Boundary County|     0|  0.000|  0.000|    38|  3103.307| 35.000|  12,245|
| |Bonner County|     0|  0.000|  0.000|   191|  4175.867| 24.986|  45,739|
| |Oneida County|     0|  0.000|  0.000|    16|  3531.229| 94.586|   4,531|
| |Teton County|     0|  0.000|  0.000|    97|  7988.799| 176.483|  12,142|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   160| 89.278| N/A| 8,567|  4780.300| N/A|1,792,147|
| |Kanawha County|    24| 134.738|  0.802| 1,080|  6063.192| 116.291| 178,124|
| |Jackson County|    19| 664.894|  0.000|   168|  5879.059| 29.995|  28,576|
| |Mercer County|    18| 306.341| 17.019|   240|  4084.550| 106.976|  58,758|
| |Berkeley County|    11| 92.304|  0.000|   734|  6159.217| 45.553| 119,171|
| |Logan County|    11| 343.546| 35.693|   356| 11118.398| 571.089|  32,019|
| |Wayne County|     9| 228.415|  0.000|   221|  5608.852| 47.133|  39,402|
| |Fayette County|     7| 165.071|  0.000|   170|  4008.867| 74.114|  42,406|
| |Mingo County|     5| 213.456|  0.000|   201|  8580.943| 170.765|  23,424|
| |Wood County|     5| 59.867|  0.000|   283|  3388.491| 61.578|  83,518|
| |Monongalia County|     5| 47.343|  0.000|   989|  9364.466| 67.633| 105,612|
| |Preston County|     4| 119.646|  0.000|   130|  3888.490| 21.365|  33,432|
| |Ohio County|     4| 96.593|  0.000|   279|  6737.340| 37.947|  41,411|
| |Grant County|     4| 345.781| 37.048|   131| 11324.343| 123.493|  11,568|
| |Mineral County|     4| 148.876|  0.000|   127|  4726.813| 31.902|  26,868|
| |Jefferson County|     4| 69.996|  0.000|   305|  5337.206| 27.498|  57,146|
| |Cabell County|     3| 32.628|  0.000|   450|  4894.230| 77.686|  91,945|
| |Greenbrier County|     3| 86.550|  0.000|    96|  2769.604| 12.364|  34,662|
| |Marion County|     2| 35.668|  0.000|   199|  3549.008| 20.382|  56,072|
| |Wyoming County|     2| 98.068|  7.005|    47|  2304.599| 112.078|  20,394|
| |Pleasants County|     2| 268.097| 19.150|    14|  1876.676| 19.150|   7,460|
| |Lewis County|     2| 125.731|  0.000|    28|  1760.231|  0.000|  15,907|
| |Brooke County|     1| 45.581|  0.000|    76|  3464.151| 78.139|  21,939|
| |Barbour County|     1| 60.824|  0.000|    33|  2007.177| 34.756|  16,441|
| |Pendleton County|     1| 143.493|  0.000|    43|  6170.182| 61.497|   6,969|
| |Taylor County|     1| 59.898|  0.000|    74|  4432.465| 154.024|  16,695|
| |Roane County|     1| 73.057|  0.000|    19|  1388.077| 41.747|  13,688|
| |Harrison County|     1| 14.869|  0.000|   248|  3687.403| 57.350|  67,256|
| |Clay County|     1| 117.536|  0.000|    18|  2115.656|  0.000|   8,508|
| |Hampshire County|     1| 43.150|  0.000|    88|  3797.195| 73.971|  23,175|
| |Marshall County|     1| 32.754|  0.000|   130|  4257.967|  0.000|  30,531|
| |Mason County|     1| 37.713|  0.000|    73|  2753.055| 91.589|  26,516|
| |Nicholas County|     1| 40.823|  0.000|    40|  1632.920| 17.496|  24,496|
| |Raleigh County|     1| 13.631|  0.000|   297|  4048.473| 85.682|  73,361|
| |Hardy County|     0|  0.000|  0.000|    63|  4573.171| 51.850|  13,776|
| |Tucker County|     0|  0.000|  0.000|    11|  1608.422| 20.889|   6,839|
| |Summers County|     0|  0.000|  0.000|    19|  1511.175| 90.898|  12,573|
| |Ritchie County|     0|  0.000|  0.000|     3|   314.005|  0.000|   9,554|
| |Putnam County|     0|  0.000|  0.000|   218|  3861.825| 58.206|  56,450|
| |Randolph County|     0|  0.000|  0.000|   214|  7457.745| 19.914|  28,695|
| |Tyler County|     0|  0.000|  0.000|    15|  1746.013| 33.257|   8,591|
| |Morgan County|     0|  0.000|  0.000|    33|  1845.225| 39.940|  17,884|
| |Monroe County|     0|  0.000|  0.000|    21|  1581.921|  0.000|  13,275|
| |Lincoln County|     0|  0.000|  0.000|   108|  5291.783| 139.994|  20,409|
| |McDowell County|     0|  0.000|  0.000|    67|  3801.634| 40.529|  17,624|
| |Wirt County|     0|  0.000|  0.000|     7|  1202.543| 24.542|   5,821|
| |Wetzel County|     0|  0.000|  0.000|    45|  2987.056| 28.448|  15,065|
| |Braxton County|     0|  0.000|  0.000|     8|   573.189|  0.000|  13,957|
| |Boone County|     0|  0.000|  0.000|   118|  5499.371| 113.183|  21,457|
| |Gilmer County|     0|  0.000|  0.000|    18|  2300.908| 36.522|   7,823|
| |Doddridge County|     0|  0.000|  0.000|     6|   710.227|  0.000|   8,448|
| |Upshur County|     0|  0.000|  0.000|    40|  1654.533|  0.000|  24,176|
| |Calhoun County|     0|  0.000|  0.000|     7|   984.667| 20.095|   7,109|
| |Hancock County|     0|  0.000|  0.000|   113|  3922.249|  4.959|  28,810|
| |Pocahontas County|     0|  0.000|  0.000|    42|  5092.761| 17.322|   8,247|
| |Webster County|     0|  0.000|  0.000|     4|   492.975|  0.000|   8,114|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   153| 172.948| N/A|10,274| 11613.514| N/A| 884,659|
| |Minnehaha County|    68| 352.087|  0.000| 4,629| 23967.815| 153.114| 193,134|
| |Pennington County|    33| 290.046|  1.256|   942|  8279.499| 64.036| 113,775|
| |Beadle County|     9| 487.726|  0.000|   598| 32406.655| 38.708|  18,453|
| |Todd County|     5| 491.304|  0.000|    75|  7369.559| 84.224|  10,177|
| |Union County|     4| 251.067|  0.000|   223| 13996.987| 80.700|  15,932|
| |Lake County|     4| 312.573| 22.327|   101|  7892.475| 78.143|  12,797|
| |Buffalo County|     3| 1529.052|  0.000|   109| 55555.556|  0.000|   1,962|
| |Brown County|     3| 77.242|  0.000|   473| 12178.480| 114.024|  38,839|
| |Lyman County|     3| 793.441| 37.783|    91| 24067.707| 37.783|   3,781|
| |Yankton County|     3| 131.498|  6.262|   153|  6706.408| 244.211|  22,814|
| |Hughes County|     3| 171.174|  8.151|    98|  5591.692| 40.756|  17,526|
| |Oglala Lakota County|     2| 141.074|  0.000|   158| 11144.812| 30.230|  14,177|
| |Lincoln County|     2| 32.718|  0.000|   708| 11582.254| 163.591|  61,128|
| |Roberts County|     1| 96.209|  0.000|    87|  8370.214| 96.209|  10,394|
| |Davison County|     1| 50.569|  0.000|   100|  5056.890| 21.672|  19,775|
| |Lawrence County|     1| 38.694|  5.528|    73|  2824.640| 99.498|  25,844|
| |Jackson County|     1| 299.043|  0.000|    12|  3588.517| 42.720|   3,344|
| |Jerauld County|     1| 496.771|  0.000|    39| 19374.069|  0.000|   2,013|
| |McCook County|     1| 179.019|  0.000|    36|  6444.683| 204.593|   5,586|
| |Codington County|     1| 35.703|  0.000|   163|  5819.558| 153.012|  28,009|
| |Butte County|     1| 95.886|  0.000|    20|  1917.729| 41.094|  10,429|
| |Brookings County|     1| 28.509|  0.000|   154|  4390.341| 69.235|  35,077|
| |Faulk County|     1| 434.972|  0.000|    29| 12614.180| 186.416|   2,299|
| |Meade County|     1| 35.296|  0.000|   104|  3670.761| 50.423|  28,332|
| |Grant County|     0|  0.000|  0.000|    33|  4679.524| 141.804|   7,052|
| |Fall River County|     0|  0.000|  0.000|    23|  3426.188| 21.281|   6,713|
| |Edmunds County|     0|  0.000|  0.000|    19|  4962.131| 149.237|   3,829|
| |Douglas County|     0|  0.000|  0.000|    19|  6504.622| 97.814|   2,921|
| |Dewey County|     0|  0.000|  0.000|    58|  9843.856| 242.460|   5,892|
| |Marshall County|     0|  0.000|  0.000|    12|  2431.611| 86.843|   4,935|
| |Miner County|     0|  0.000|  0.000|    15|  6768.953|  0.000|   2,216|
| |Day County|     0|  0.000|  0.000|    26|  4793.510| 79.014|   5,424|
| |Walworth County|     0|  0.000|  0.000|    18|  3311.868|  0.000|   5,435|
| |Ziebach County|     0|  0.000|  0.000|    35| 12699.565|  0.000|   2,756|
| |Turner County|     0|  0.000|  0.000|    59|  7037.214| 136.314|   8,384|
| |Moody County|     0|  0.000|  0.000|    33|  5018.248| 21.724|   6,576|
| |Tripp County|     0|  0.000|  0.000|    20|  3675.795|  0.000|   5,441|
| |Sully County|     0|  0.000|  0.000|     4|  2875.629| 102.701|   1,391|
| |Stanley County|     0|  0.000|  0.000|    15|  4841.833| 46.113|   3,098|
| |Spink County|     0|  0.000|  0.000|    27|  4234.630| 44.811|   6,376|
| |Gregory County|     0|  0.000|  0.000|     7|  1672.640|  0.000|   4,185|
| |Haakon County|     0|  0.000|  0.000|     2|  1053.186|  0.000|   1,899|
| |Mellette County|     0|  0.000|  0.000|    24| 11644.833|  0.000|   2,061|
| |Hamlin County|     0|  0.000|  0.000|    30|  4866.970| 208.584|   6,164|
| |Hand County|     0|  0.000|  0.000|    12|  3760.577| 223.844|   3,191|
| |McPherson County|     0|  0.000|  0.000|     8|  3362.757|  0.000|   2,379|
| |Kingsbury County|     0|  0.000|  0.000|    15|  3037.052| 28.924|   4,939|
| |Jones County|     0|  0.000|  0.000|     2|  2214.839|  0.000|     903|
| |Hyde County|     0|  0.000|  0.000|     4|  3074.558| 109.806|   1,301|
| |Hutchinson County|     0|  0.000|  0.000|    31|  4251.817| 39.187|   7,291|
| |Harding County|     0|  0.000|  0.000|     2|  1540.832| 220.119|   1,298|
| |Hanson County|     0|  0.000|  0.000|    22|  6371.271| 41.372|   3,453|
| |Potter County|     0|  0.000|  0.000|     2|   928.936| 66.353|   2,153|
| |Sanborn County|     0|  0.000|  0.000|    13|  5546.075|  0.000|   2,344|
| |Perkins County|     0|  0.000|  0.000|     6|  2094.241|  0.000|   2,865|
| |Deuel County|     0|  0.000|  0.000|    19|  4366.812| 262.665|   4,351|
| |Charles Mix County|     0|  0.000|  0.000|   113| 12160.999| 122.994|   9,292|
| |Campbell County|     0|  0.000|  0.000|     3|  2180.233|  0.000|   1,376|
| |Brule County|     0|  0.000|  0.000|    47|  8872.947| 53.939|   5,297|
| |Bon Homme County|     0|  0.000|  0.000|    24|  3477.757| 227.710|   6,901|
| |Bennett County|     0|  0.000|  0.000|     6|  1783.061|  0.000|   3,365|
| |Clark County|     0|  0.000|  0.000|    17|  4550.321| 38.238|   3,736|
| |Clay County|     0|  0.000|  0.000|   142| 10092.395| 142.146|  14,070|
| |Aurora County|     0|  0.000|  0.000|    40| 14540.167| 103.858|   2,751|
| |Corson County|     0|  0.000|  0.000|    47| 11502.692| 489.476|   4,086|
| |Custer County|     0|  0.000|  0.000|    45|  5015.604| 159.226|   8,972|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   127| 94.479| N/A| 4,166|  3099.214| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.000| 2,126|  7206.706| 18.402| 295,003|
| |Waldo County|    14| 352.512|  0.000|    63|  1586.302|  3.597|  39,715|
| |York County|    13| 62.608|  0.688|   689|  3318.227| 11.008| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   172|  1406.355|  2.336| 122,302|
| |Androscoggin County|     9| 83.120|  1.319|   577|  5328.925| 18.471| 108,277|
| |Penobscot County|     5| 32.863|  0.000|   178|  1169.914| 24.412| 152,148|
| |Hancock County|     1| 18.186|  0.000|    40|   727.445| 12.990|  54,987|
| |Somerset County|     1| 19.808|  0.000|    37|   732.905| 11.319|  50,484|
| |Lincoln County|     1| 28.873|  0.000|    35|  1010.568|  0.000|  34,634|
| |Knox County|     1| 25.143|  0.000|    28|   704.013|  3.592|  39,772|
| |Franklin County|     1| 33.114|  0.000|    47|  1556.343|  9.461|  30,199|
| |Aroostook County|     1| 14.913|  0.000|    33|   492.133|  0.000|  67,055|
| |Washington County|     0|  0.000|  0.000|    14|   446.158|  4.553|  31,379|
| |Sagadahoc County|     0|  0.000|  0.000|    58|  1617.581|  7.968|  35,856|
| |Piscataquis County|     0|  0.000|  0.000|    11|   655.347| 59.577|  16,785|
| |Oxford County|     0|  0.000|  0.000|    58|  1000.431| 12.321|  57,975|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   125| 164.029| N/A| 8,565| 11239.243| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 3,128| 17194.088| 69.888| 181,923|
| |Burleigh County|     9| 94.117|  4.482| 1,388| 14514.881| 324.180|  95,626|
| |Grand Forks County|     8| 115.189|  4.114|   789| 11360.528| 230.378|  69,451|
| |Stark County|     6| 190.543| 13.610|   391| 12417.035| 589.775|  31,489|
| |Morton County|     4| 127.535|  4.555|   452| 14411.427| 387.159|  31,364|
| |Stutsman County|     3| 144.900|  6.900|   130|  6278.980| 20.700|  20,704|
| |McKenzie County|     2| 133.120|  9.509|    93|  6190.096| 38.034|  15,024|
| |Ramsey County|     2| 173.626|  0.000|    87|  7552.739| 223.234|  11,519|
| |McIntosh County|     2| 800.961|  0.000|    41| 16419.704| 629.327|   2,497|
| |Williams County|     2| 53.207|  0.000|   302|  8034.265| 121.616|  37,589|
| |Sioux County|     2| 472.813| 33.772|    97| 22931.442| 472.813|   4,230|
| |Richland County|     2| 123.632|  8.831|   117|  7232.491| 70.647|  16,177|
| |Benson County|     2| 292.740|  0.000|   168| 24590.164| 669.120|   6,832|
| |Ward County|     1| 14.784|  0.000|   276|  4080.365| 114.047|  67,641|
| |McHenry County|     1| 174.064|  0.000|    24|  4177.546| 198.931|   5,745|
| |Mountrail County|     1| 94.832|  0.000|   155| 14698.909| 338.685|  10,545|
| |Griggs County|     1| 448.229|  0.000|    37| 16584.491| 192.098|   2,231|
| |Emmons County|     1| 308.547|  0.000|    23|  7096.575| 264.469|   3,241|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Eddy County|     0|  0.000|  0.000|    20|  8745.081| 124.930|   2,287|
| |Dunn County|     0|  0.000|  0.000|    32|  7233.273| 64.583|   4,424|
| |Foster County|     0|  0.000|  0.000|    26|  8099.688| 44.504|   3,210|
| |Golden Valley County|     0|  0.000|  0.000|    12|  6814.310| 648.982|   1,761|
| |Grant County|     0|  0.000|  0.000|     4|  1759.015|  0.000|   2,274|
| |Hettinger County|     0|  0.000|  0.000|     7|  2801.120| 57.166|   2,499|
| |Kidder County|     0|  0.000|  0.000|    22|  8870.968| 460.829|   2,480|
| |Traill County|     0|  0.000|  0.000|    64|  7964.161| 159.994|   8,036|
| |Dickey County|     0|  0.000|  0.000|    14|  2873.563| 29.322|   4,872|
| |Walsh County|     0|  0.000|  0.000|   116| 10901.231| 161.102|  10,641|
| |Wells County|     0|  0.000|  0.000|    24|  6259.781| 111.782|   3,834|
| |Divide County|     0|  0.000|  0.000|     4|  1766.784| 126.199|   2,264|
| |Cavalier County|     0|  0.000|  0.000|    31|  8240.298|  0.000|   3,762|
| |Burke County|     0|  0.000|  0.000|    23| 10874.704|  0.000|   2,115|
| |Logan County|     0|  0.000|  0.000|     7|  3783.784|  0.000|   1,850|
| |Bowman County|     0|  0.000|  0.000|    11|  3637.566| 236.206|   3,024|
| |Billings County|     0|  0.000|  0.000|     3|  3232.759| 153.941|     928|
| |Barnes County|     0|  0.000|  0.000|    45|  4320.691| 109.732|  10,415|
| |Adams County|     0|  0.000|  0.000|     3|  1353.791| 64.466|   2,216|
| |LaMoure County|     0|  0.000|  0.000|    16|  3954.523|  0.000|   4,046|
| |McLean County|     0|  0.000|  0.000|   102| 10793.651| 619.803|   9,450|
| |Mercer County|     0|  0.000|  0.000|    34|  4152.925| 87.246|   8,187|
| |Towner County|     0|  0.000|  0.000|     5|  2284.148|  0.000|   2,189|
| |Steele County|     0|  0.000|  0.000|    16|  8465.608| 151.172|   1,890|
| |Slope County|     0|  0.000|  0.000|     4|  5333.333| 190.476|     750|
| |Sheridan County|     0|  0.000|  0.000|     9|  6844.106| 108.637|   1,315|
| |Sargent County|     0|  0.000|  0.000|    10|  2565.418|  0.000|   3,898|
| |Rolette County|     0|  0.000|  0.000|    88|  6207.675| 161.238|  14,176|
| |Renville County|     0|  0.000|  0.000|    10|  4297.379| 61.391|   2,327|
| |Ransom County|     0|  0.000|  0.000|    28|  5366.041|  0.000|   5,218|
| |Pierce County|     0|  0.000|  0.000|    16|  4025.157| 143.756|   3,975|
| |Pembina County|     0|  0.000|  0.000|    27|  3970.004|  0.000|   6,801|
| |Oliver County|     0|  0.000|  0.000|     7|  3573.252|  0.000|   1,959|
| |Nelson County|     0|  0.000|  0.000|    27|  9378.256| 99.241|   2,879|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    82| 76.723| N/A| 5,750|  5379.976| N/A|1,068,778|
| |Yellowstone County|    32| 198.388|  1.771| 1,522|  9435.834| 209.902| 161,300|
| |Big Horn County|    14| 1051.130| 10.726|   519| 38966.889| 976.049|  13,319|
| |Toole County|     6| 1266.892|  0.000|    46|  9712.838| 30.164|   4,736|
| |Cascade County|     4| 49.161|  0.000|   182|  2236.807| 28.092|  81,366|
| |Gallatin County|     3| 26.216|  0.000|   991|  8660.014| 64.916| 114,434|
| |Flathead County|     3| 28.900|  1.376|   392|  3776.275| 85.324| 103,806|
| |Hill County|     2| 121.330|  0.000|    48|  2911.915| 51.998|  16,484|
| |Custer County|     2| 175.408|  0.000|    61|  5349.939|  0.000|  11,402|
| |Missoula County|     2| 16.722|  1.194|   384|  3210.702| 65.695| 119,600|
| |Lewis and Clark County|     2| 28.805|  2.058|   178|  2563.659| 41.150|  69,432|
| |Lincoln County|     2| 100.100|  0.000|    78|  3903.904|  7.150|  19,980|
| |Richland County|     2| 185.134|  0.000|    50|  4628.344| 39.672|  10,803|
| |Ravalli County|     2| 45.656|  3.261|    85|  1940.373|  6.522|  43,806|
| |Rosebud County|     1| 111.894|  0.000|    78|  8727.761| 703.336|   8,937|
| |Stillwater County|     1| 103.713|  0.000|    31|  3215.101| 74.081|   9,642|
| |Sweet Grass County|     1| 267.594|  0.000|     6|  1605.566| 38.228|   3,737|
| |Madison County|     1| 116.279|  0.000|    85|  9883.721| 16.611|   8,600|
| |Lake County|     1| 32.832|  0.000|   187|  6139.602| 32.832|  30,458|
| |Glacier County|     1| 72.711|  0.000|    88|  6398.604| 145.423|  13,753|
| |Garfield County|     0|  0.000|  0.000|    12|  9538.951|  0.000|   1,258|
| |Powell County|     0|  0.000|  0.000|     2|   290.276|  0.000|   6,890|
| |Prairie County|     0|  0.000|  0.000|     1|   928.505|  0.000|   1,077|
| |Roosevelt County|     0|  0.000|  0.000|    35|  3180.662| 155.788|  11,004|
| |Sheridan County|     0|  0.000|  0.000|     5|  1511.031|  0.000|   3,309|
| |Silver Bow County|     0|  0.000|  0.000|   105|  3007.303| 69.557|  34,915|
| |Teton County|     0|  0.000|  0.000|    15|  2440.215|  0.000|   6,147|
| |Treasure County|     0|  0.000|  0.000|     2|  2873.563|  0.000|     696|
| |Valley County|     0|  0.000|  0.000|    30|  4056.247| 289.732|   7,396|
| |Sanders County|     0|  0.000|  0.000|    18|  1486.007| 106.143|  12,113|
| |Wibaux County|     0|  0.000|  0.000|     3|  3095.975|  0.000|     969|
| |Wheatland County|     0|  0.000|  0.000|     3|  1411.101|  0.000|   2,126|
| |Beaverhead County|     0|  0.000|  0.000|    68|  7193.484| 60.449|   9,453|
| |Chouteau County|     0|  0.000|  0.000|    10|  1774.623|  0.000|   5,635|
| |Carter County|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,252|
| |Carbon County|     0|  0.000|  0.000|    75|  6993.007| 79.920|  10,725|
| |Broadwater County|     0|  0.000|  0.000|    14|  2244.669| 45.810|   6,237|
| |Blaine County|     0|  0.000|  0.000|    15|  2245.173| 106.913|   6,681|
| |Granite County|     0|  0.000|  0.000|    18|  5327.020| 84.556|   3,379|
| |Golden Valley County|     0|  0.000|  0.000|     3|  3654.080|  0.000|     821|
| |Fergus County|     0|  0.000|  0.000|    23|  2081.448| 129.282|  11,050|
| |Jefferson County|     0|  0.000|  0.000|    31|  2536.617| 35.068|  12,221|
| |Judith Basin County|     0|  0.000|  0.000|     3|  1494.768|  0.000|   2,007|
| |Liberty County|     0|  0.000|  0.000|     1|   427.899|  0.000|   2,337|
| |Fallon County|     0|  0.000|  0.000|     2|   702.741|  0.000|   2,846|
| |Daniels County|     0|  0.000|  0.000|     3|  1775.148|  0.000|   1,690|
| |Dawson County|     0|  0.000|  0.000|    30|  3483.107| 215.621|   8,613|
| |Deer Lodge County|     0|  0.000|  0.000|    30|  3282.276| 78.149|   9,140|
| |Meagher County|     0|  0.000|  0.000|     4|  2148.228|  0.000|   1,862|
| |Powder River County|     0|  0.000|  0.000|     1|   594.530|  0.000|   1,682|
| |Pondera County|     0|  0.000|  0.000|    11|  1860.937|  0.000|   5,911|
| |Phillips County|     0|  0.000|  0.000|    92| 23267.577| 2312.306|   3,954|
| |Petroleum County|     0|  0.000|  0.000|     0|     0.000|  0.000|     487|
| |Park County|     0|  0.000|  0.000|    63|  3793.809| 68.822|  16,606|
| |Musselshell County|     0|  0.000|  0.000|     4|   863.371| 30.835|   4,633|
| |Mineral County|     0|  0.000|  0.000|     2|   454.856| 64.979|   4,397|
| |McCone County|     0|  0.000|  0.000|     5|  3004.808| 171.703|   1,664|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    58| 92.950| N/A| 1,507|  2415.107| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   756|  4616.117| 23.552| 163,774|
| |Franklin County|     7| 141.695|  0.000|   121|  2449.294|  8.675|  49,402|
| |Windham County|     3| 71.053|  0.000|   105|  2486.855| 10.150|  42,222|
| |Addison County|     2| 54.382|  0.000|    76|  2066.509| 11.653|  36,777|
| |Washington County|     2| 34.241|  0.000|    58|   992.998| 12.229|  58,409|
| |Windsor County|     2| 36.323|  0.000|    75|  1362.101|  7.783|  55,062|
| |Bennington County|     1| 28.193|  0.000|    92|  2593.741| 20.138|  35,470|
| |Lamoille County|     1| 39.429|  0.000|    43|  1695.450|  0.000|  25,362|
| |Rutland County|     1| 17.185|  0.000|   101|  1735.664|  4.910|  58,191|
| |Caledonia County|     0|  0.000|  0.000|    29|   966.892|  4.763|  29,993|
| |Orleans County|     0|  0.000|  0.000|    15|   554.795|  5.284|  27,037|
| |Orange County|     0|  0.000|  0.000|    17|   588.398| 14.834|  28,892|
| |Grand Isle County|     0|  0.000|  0.000|    13|  1796.821|  0.000|   7,235|
| |Essex County|     0|  0.000|  0.000|     6|   973.552|  0.000|   6,163|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    39| 27.545| N/A| 5,019|  3544.812| N/A|1,415,872|
| |Honolulu County|    33| 33.861| N/A| 4,591|  4710.829| N/A| 974,563|
| |Maui County|     6| 35.839|  0.000|   226|  1349.923| 34.985| 167,417|
| |Kalawao County|     0|  0.000|  0.000|     0|     0.000|  0.000|      86|
| |Kauai County|     0|  0.000|  0.000|    54|   746.960| 11.857|  72,293|
| |Hawaii County|     0|  0.000|  0.000|   148|   734.444| 12.052| 201,513|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 3,286|  5677.665| N/A| 578,759|
| |Johnson County|     1| 118.413|  0.000|    25|  2960.332| 33.832|   8,445|
| |Hot Springs County|     0|  0.000|  0.000|    23|  5211.874| 32.372|   4,413|
| |Lincoln County|     0|  0.000|  0.000|   102|  5143.722|  0.000|  19,830|
| |Laramie County|     0|  0.000|  0.000|   517|  5195.980| 21.536|  99,500|
| |Natrona County|     0|  0.000|  0.000|   248|  3105.512| 30.411|  79,858|
| |Albany County|     0|  0.000|  0.000|    95|  2443.416| 25.720|  38,880|
| |Big Horn County|     0|  0.000|  0.000|    37|  3138.253|  0.000|  11,790|
| |Campbell County|     0|  0.000|  0.000|   148|  3193.716| 77.068|  46,341|
| |Carbon County|     0|  0.000|  0.000|   167| 11283.784| 656.371|  14,800|
| |Converse County|     0|  0.000|  0.000|    31|  2242.801|  0.000|  13,822|
| |Crook County|     0|  0.000|  0.000|    11|  1450.422| 18.837|   7,584|
| |Washakie County|     0|  0.000|  0.000|    97| 12427.931| 366.066|   7,805|
| |Fremont County|     0|  0.000|  0.000|   523| 13321.107| 69.134|  39,261|
| |Niobrara County|     0|  0.000|  0.000|     2|   848.896|  0.000|   2,356|
| |Park County|     0|  0.000|  0.000|   144|  4932.520| 48.934|  29,194|
| |Goshen County|     0|  0.000|  0.000|    39|  2952.085| 118.948|  13,211|
| |Uinta County|     0|  0.000|  0.000|   276| 13645.802|  0.000|  20,226|
| |Teton County|     0|  0.000|  0.000|   389| 16578.588| 91.325|  23,464|
| |Sweetwater County|     0|  0.000|  0.000|   276|  6518.197| 57.355|  42,343|
| |Sublette County|     0|  0.000|  0.000|    40|  4068.762|  0.000|   9,831|
| |Sheridan County|     0|  0.000|  0.000|    83|  2722.650| 42.175|  30,485|
| |Platte County|     0|  0.000|  0.000|     6|   714.881| 17.021|   8,393|
| |Weston County|     0|  0.000|  0.000|     7|  1010.538| 41.246|   6,927|


### Alaska ###

![Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alaska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AK|29 counties|     0|  0.000| N/A|     0|     0.000| N/A| 731,545|
| |Prince of Wales-Hyder Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,203|
| |Petersburg Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,266|
| |Skagway Municipality|     0|  0.000|  0.000|     0|     0.000|  0.000|   1,183|
| |Sitka Borough|     0|  0.000| N/A|     0|     0.000| N/A|   8,493|
| |Southeast Fairbanks Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   6,893|
| |Valdez-Cordova Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,202|
| |Nome Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  10,004|
| |Dillingham Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   4,916|
| |Denali Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,097|
| |Bristol Bay Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|     836|
| |Bethel Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,634|
| |Aleutians East Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   3,337|
| |Matanuska-Susitna Borough|     0|  0.000|  0.000|     0|     0.000|  0.000| 108,317|
| |North Slope Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   9,832|
| |Yukon-Koyukuk Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   5,230|
| |Yakutat Borough|     0|  0.000| N/A|     0|     0.000| N/A|     579|
| |Northwest Arctic Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   7,621|
| |Wrangell Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,502|
| |Fairbanks North Star Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  96,849|
| |Hoonah-Angoon Census Area|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,148|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Kenai Peninsula Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|  58,708|
| |Haines Borough|     0|  0.000|  0.000|     0|     0.000|  0.000|   2,530|
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


