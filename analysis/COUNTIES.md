# Analysis of US By County #

Updated: at 2020-08-06

For the US counties analysis, the list of all 3,143 counties (or equivalent) is sorted by the absolute number of deaths from highest to lowest.  This sorted list is then divided into two parts: counties with populations of 50,000 or more and smaller counties.

## Larger Population Counties ##

There were 990 larger population counties with a combined population of 288,662,059 (87.94% of the US population).  In these counties there have been 125,814 deaths (435.852 deaths/million) and 4,156,626 confirmed cases (14399.625 confirmed cases/million).  This group accounts for 80.79% of all US deaths and for 87.61% of all US cases.

23.88% of this group's deaths (19.29% of the total US deaths) occured in 12 counties in 9 states with a combined population of 32,573,893 (9.92% of the total US population):



The next 26.10% of this group's deaths (21.09% of the total US deaths) occured in 34 counties in 14 states with a combined population of 41,568,886 (12.66% of the total US population):



The next 24.99% of this group's deaths (20.19% of the total US deaths) occured in 86 counties in 30 states with a combined population of 66,924,527 (20.39% of the total US population)

The remaining 25.03% of this group's deaths (20.22% of the total US deaths) occured in 858 counties in 50 states with a combined population of 147,594,753 (44.97% of the total US population) 

## Smaller Population Counties ##

There were 2152 smaller population counties with a combined population of 39,577,464 (12.06% of the US population).  In these counties there have been 9,476 deaths (239.429 deaths/million) and 420,319 confirmed cases (10620.160 confirmed cases/million).  This group accounts for 6.08% of all US deaths and for 8.86% of all US cases.

24.86% of this group's deaths (1.51% of the total US deaths) occured in 56 counties in 16 states with a combined population of 1,822,576 (0.56% of the total US population):



The next 25.02% of this group's deaths (1.52% of the total US deaths) occured in 108 counties in 26 states with a combined population of 3,253,125 (0.99% of the total US population):



The next 25.12% of this group's deaths (1.53% of the total US deaths) occured in 225 counties in 33 states with a combined population of 5,547,421 (1.69% of the total US population)

The remaining 25.00% of this group's deaths (1.52% of the total US deaths) occured in 1,763 counties in 47 states with a combined population of 28,954,342 (8.82% of the total US population) 

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
|NJ|21 counties|15,842| 1783.569| N/A|182,687| 20567.788| N/A|8,882,190|
| |Essex County| 2,105| 2634.626|  0.936|19,611| 24545.199| 33.167| 798,975|
| |Bergen County| 2,038| 2186.221|  0.000|20,639| 22140.051| 46.664| 932,202|
| |Hudson County| 1,502| 2233.819|  0.000|19,564| 29096.166| 25.283| 672,391|
| |Middlesex County| 1,400| 1696.842|  0.000|17,798| 21571.712| 34.392| 825,062|
| |Union County| 1,347| 2421.177|  0.000|16,605| 29846.803| 15.691| 556,341|
| |Passaic County| 1,239| 2468.983|  0.000|17,550| 34972.281| 42.844| 501,826|
| |Ocean County| 1,016| 1673.293|  0.000|10,520| 17325.828| 37.023| 607,186|
| |Monmouth County|   856| 1383.334|  0.000|10,192| 16470.721| 32.321| 618,795|
| |Morris County|   827| 1681.424|  0.000| 7,195| 14628.592| 27.440| 491,845|
| |Mercer County|   618| 1681.953|  0.000| 8,076| 21979.697| 32.568| 367,430|
| |Camden County|   577| 1139.256|  1.675| 8,442| 16668.279| 61.552| 506,471|
| |Somerset County|   561| 1705.509|  6.558| 5,202| 15814.723| 11.373| 328,934|
| |Burlington County|   470| 1055.352|  0.000| 5,907| 13263.755| 60.627| 445,349|
| |Atlantic County|   252| 955.740|  0.000| 3,436| 13031.441| 53.656| 263,670|
| |Gloucester County|   209| 716.647|  0.000| 3,164| 10849.141| 87.432| 291,636|
| |Sussex County|   197| 1402.255|  7.118| 1,316|  9367.348| 27.206| 140,488|
| |Warren County|   171| 1624.441|  0.000| 1,336| 12691.537| 24.216| 105,267|
| |Cumberland County|   158| 1056.665|  2.857| 3,290| 22002.715| 110.492| 149,527|
| |Hunterdon County|   126| 1013.098|  0.000| 1,144|  9198.286|  8.040| 124,371|
| |Cape May County|    87| 945.251|  0.000|   819|  8898.402| 32.620|  92,039|
| |Salem County|    86| 1378.537| 16.029|   881| 14121.984| 41.858|  62,385|


### New York ###

![New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20York.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NY|62 counties|12,314| 632.988| N/A|250,657| 12884.865| N/A|19,453,561|
| |Nassau County| 2,194| 1616.892|  0.000|43,482| 32044.536| 38.436|1,356,924|
| |Suffolk County| 1,997| 1352.430|  0.000|43,553| 29495.443| 50.285|1,476,601|
| |Westchester County| 1,446| 1494.564|  0.000|36,075| 37286.590| 28.940| 967,506|
| |Queens County|   983| 436.320|  0.978| 7,825|  3471.958| 16.939|2,253,858|
| |Kings County|   929| 363.051|  0.814| 1,343|   524.628|  2.560|2,559,903|
| |Rockland County|   674| 2068.824|  0.000|13,903| 42674.860| 24.299| 325,789|
| |Erie County|   671| 730.378|  0.000| 8,702|  9472.059| 43.581| 918,702|
| |Bronx County|   648| 457.149|  1.025|26,649| 18790.793| 91.678|1,418,207|
| |Orange County|   491| 1275.523|  5.196|11,113| 28869.434| 20.782| 384,940|
| |New York County|   414| 254.117|  0.570|15,370|  9436.737| 46.041|1,628,706|
| |Monroe County|   285| 384.216|  4.486| 4,841|  6526.282| 33.628| 741,770|
| |Onondaga County|   200| 434.284|  0.000| 3,525|  7654.258| 28.131| 460,528|
| |Dutchess County|   153| 520.023|  0.000| 4,568| 15525.903| 48.237| 294,218|
| |Richmond County|   148| 310.566|  0.696| 7,825| 16434.770| 80.183| 476,143|
| |Albany County|   128| 418.977|  0.000| 2,556|  8366.448| 39.549| 305,506|
| |Oneida County|   115| 502.906|  6.952| 2,114|  9244.723| 44.374| 228,671|
| |Niagara County|    98| 468.270|  0.000| 1,466|  7004.936| 33.633| 209,281|
| |Ulster County|    91| 512.465|  0.000| 2,039| 11482.602| 21.655| 177,573|
| |Broome County|    69| 362.228| 10.918| 1,082|  5680.148| 52.497| 190,488|
| |Putnam County|    63| 640.765|  0.000| 1,439| 14635.883| 33.620|  98,320|
| |Orleans County|    54| 1338.224|  0.000|   297|  7360.230| 49.564|  40,352|
| |Sullivan County|    48| 636.335|  0.000| 1,485| 19686.605| 13.257|  75,432|
| |Steuben County|    42| 440.349|  0.000|   297|  3113.893| 22.175|  95,379|
| |Schenectady County|    37| 238.250|  0.000| 1,045|  6728.955| 23.627| 155,299|
| |Columbia County|    37| 622.257|  0.000|   531|  8930.223| 59.733|  59,461|
| |Ontario County|    34| 309.719|  0.000|   352|  3206.500|  6.307| 109,777|
| |Warren County|    33| 516.077|  0.000|   304|  4754.160| 25.629|  63,944|
| |Rensselaer County|    30| 189.019|  0.000|   755|  4756.984| 25.203| 158,714|
| |Tioga County|    25| 518.640|  0.000|   193|  4003.900| 29.330|  48,203|
| |Fulton County|    24| 449.581|  0.000|   287|  5376.243| 21.462|  53,383|
| |Greene County|    18| 381.453|  0.000|   289|  6124.438|  0.000|  47,188|
| |Saratoga County|    17| 73.957|  0.000|   744|  3236.711| 20.887| 229,863|
| |Madison County|    17| 239.636|  0.000|   406|  5723.066| 29.871|  70,941|
| |Washington County|    14| 228.743|  0.000|   255|  4166.394|  0.000|  61,204|
| |Chautauqua County|     9| 70.920| N/A|   241|  1899.088| N/A| 126,903|
| |Livingston County|     8| 127.158| N/A|   171|  2717.996| N/A|  62,914|
| |Yates County|     7| 280.978| N/A|    56|  2247.822| N/A|  24,913|
| |Chenango County|     6| 127.100| N/A|   212|  4490.859| N/A|  47,207|
| |Cattaraugus County|     6| 78.826| N/A|   164|  2154.578| N/A|  76,117|
| |Wyoming County|     5| 125.442| N/A|   114|  2860.082| N/A|  39,859|
| |Otsego County|     5| 84.044| N/A|   115|  1933.001| N/A|  59,493|
| |Genesee County|     5| 87.291| N/A|   274|  4783.520| N/A|  57,280|
| |St. Lawrence County|     4| 37.126| N/A|   262|  2431.780| N/A| 107,740|
| |Delaware County|     4| 90.631| N/A|   104|  2356.406| N/A|  44,135|
| |Clinton County|     4| 49.699| N/A|   127|  1577.934| N/A|  80,485|
| |Herkimer County|     4| 65.233| N/A|   264|  4305.354| N/A|  61,319|
| |Montgomery County|     4| 81.266| N/A|   161|  3270.962| N/A|  49,221|
| |Oswego County|     3| 25.614| N/A|   250|  2134.490| N/A| 117,124|
| |Wayne County|     3| 33.364| N/A|   248|  2758.068| N/A|  89,918|
| |Seneca County|     3| 88.194| N/A|    86|  2528.222| N/A|  34,016|
| |Chemung County|     3| 35.947| N/A|   165|  1977.090| N/A|  83,456|
| |Cayuga County|     2| 26.118| N/A|   150|  1958.838| N/A|  76,576|
| |Allegany County|     1| 21.696| N/A|    76|  1648.912| N/A|  46,091|
| |Lewis County|     0|  0.000| N/A|    37|  1407.058| N/A|  26,296|
| |Schoharie County|     0|  0.000| N/A|    68|  2193.619| N/A|  30,999|
| |Cortland County|     0|  0.000| N/A|    94|  1975.578| N/A|  47,581|
| |Hamilton County|     0|  0.000| N/A|     7|  1585.145| N/A|   4,416|
| |Jefferson County|     0|  0.000| N/A|   140|  1274.651| N/A| 109,834|
| |Franklin County|     0|  0.000| N/A|    52|  1039.543| N/A|  50,022|
| |Essex County|     0|  0.000| N/A|    55|  1491.121| N/A|  36,885|
| |Tompkins County|     0|  0.000| N/A|   231|  2260.716| N/A| 102,180|
| |Schuyler County|     0|  0.000| N/A|    22|  1235.469| N/A|  17,807|


### California ###

![California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/California.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CA|58 counties| 9,808| 248.227| N/A|530,606| 13428.908| N/A|39,512,223|
| |Los Angeles County| 4,827| 480.820|  5.239|198,165| 19739.305| 206.386|10,039,107|
| |Riverside County|   738| 298.719|  0.000|38,487| 15578.338| 252.197|2,470,546|
| |Orange County|   665| 209.403|  1.831|38,131| 12007.147| 63.599|3,175,692|
| |San Diego County|   568| 170.145|  0.384|30,516|  9141.097|  0.000|3,338,330|
| |San Bernardino County|   487| 223.386| 10.700|34,237| 15704.434| 187.976|2,180,085|
| |Imperial County|   232| 1280.247| 25.014| 9,513| 52495.654| 186.794| 181,215|
| |Alameda County|   193| 115.477|  1.002|12,136|  7261.287| 123.792|1,671,329|
| |Tulare County|   193| 413.990|  7.367|10,078| 21617.563| 357.147| 466,195|
| |Santa Clara County|   192| 99.593|  0.220|11,030|  5721.394| 61.208|1,927,852|
| |San Joaquin County|   187| 245.359|  6.367|12,034| 15789.584| 97.750| 762,148|
| |Fresno County|   157| 157.141|  0.000|15,945| 15959.347| 360.901| 999,101|
| |Kern County|   152| 168.851|  3.678|21,433| 23809.101| 434.347| 900,202|
| |Sacramento County|   148| 95.357|  1.933|10,174|  6555.167| 35.437|1,552,058|
| |Stanislaus County|   135| 245.160| 18.287| 9,308| 16903.352| 113.598| 550,660|
| |Contra Costa County|   131| 113.565|  1.734| 8,324|  7216.136| 116.483|1,153,526|
| |San Mateo County|   120| 156.541|  0.557| 5,758|  7511.352| 48.919| 766,573|
| |Ventura County|    77| 91.016|  0.000| 7,877|  9310.809|  0.000| 846,006|
| |Marin County|    76| 293.634|  9.786| 5,180| 20013.445| 201.826| 258,826|
| |Santa Barbara County|    64| 143.337|  3.802| 6,526| 14615.934|  0.000| 446,499|
| |San Francisco County|    62| 70.331| N/A| 7,081|  8032.452| N/A| 881,549|
| |Kings County|    56| 366.157|  0.000| 4,453| 29115.993| 96.686| 152,940|
| |Merced County|    51| 183.665|  1.538| 4,583| 16504.610|  0.000| 277,680|
| |Sonoma County|    42| 84.962|  3.190| 3,208|  6489.513| 96.088| 494,336|
| |Yolo County|    42| 190.476|  0.000| 1,614|  7319.728| 126.984| 220,500|
| |Solano County|    38| 84.889|  1.050| 3,806|  8502.311| 183.890| 447,643|
| |Monterey County|    34| 78.330|  2.918| 4,966| 11440.788| 80.625| 434,061|
| |Madera County|    32| 203.398|  0.000| 2,114| 13436.982| 364.352| 157,327|
| |Placer County|    19| 47.699|  3.189| 1,998|  5015.954| 76.178| 398,329|
| |San Luis Obispo County|    16| 56.515|  0.000| 1,970|  6958.401| 122.115| 283,111|
| |Mendocino County|     9| 103.748| N/A|   341|  3930.881| N/A|  86,749|
| |Napa County|     9| 65.339| N/A| 1,007|  7310.663| N/A| 137,744|
| |Shasta County|     9| 49.978| N/A|   404|  2243.447| N/A| 180,080|
| |Butte County|     8| 36.499| N/A| 1,012|  4617.083| N/A| 219,186|
| |Sutter County|     6| 61.874| N/A|   840|  8662.384| N/A|  96,971|
| |Humboldt County|     4| 29.508| N/A|   245|  1807.344| N/A| 135,558|
| |Yuba County|     4| 50.847| N/A|   533|  6775.309| N/A|  78,668|
| |Santa Cruz County|     4| 14.641| N/A| 1,196|  4377.537| N/A| 273,213|
| |San Benito County|     4| 63.686| N/A|   689| 10969.940| N/A|  62,808|
| |Colusa County|     4| 185.641| N/A|   359| 16661.252| N/A|  21,547|
| |Glenn County|     2| 70.440| N/A|   346| 12186.102| N/A|  28,393|
| |Tuolumne County|     2| 36.712| N/A|   144|  2643.269| N/A|  54,478|
| |Mariposa County|     2| 116.259| N/A|    59|  3429.634| N/A|  17,203|
| |El Dorado County|     1|  5.186| N/A|   668|  3463.958| N/A| 192,843|
| |Lake County|     1| 15.531| N/A|   211|  3277.110| N/A|  64,386|
| |Mono County|     1| 69.233| N/A|   146| 10108.003| N/A|  14,444|
| |Nevada County|     1| 10.025| N/A|   316|  3167.761| N/A|  99,755|
| |Tehama County|     1| 15.365| N/A|   249|  3825.825| N/A|  65,084|
| |Inyo County|     1| 55.435| N/A|    66|  3658.739| N/A|  18,039|
| |Calaveras County|     1| 21.784| N/A|   136|  2962.640| N/A|  45,905|
| |Trinity County|     0|  0.000| N/A|     5|   407.000| N/A|  12,285|
| |Siskiyou County|     0|  0.000| N/A|    88|  2021.176| N/A|  43,539|
| |Sierra County|     0|  0.000| N/A|     3|   998.336| N/A|   3,005|
| |Plumas County|     0|  0.000| N/A|    33|  1754.666| N/A|  18,807|
| |Modoc County|     0|  0.000| N/A|     4|   452.438| N/A|   8,841|
| |Lassen County|     0|  0.000| N/A|   632| 20671.835| N/A|  30,573|
| |Del Norte County|     0|  0.000| N/A|    90|  3236.013| N/A|  27,812|
| |Amador County|     0|  0.000| N/A|   137|  3446.367| N/A|  39,752|
| |Alpine County|     0|  0.000| N/A|     2|  1771.479| N/A|   1,129|


### Massachusetts ###

![Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Massachusetts.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MA|14 counties| 8,652| 1255.277| N/A|119,201| 17294.298| N/A|6,892,503|
| |Middlesex County| 1,989| 1234.101|  0.563|26,109| 16199.675| 45.635|1,611,699|
| |Essex County| 1,186| 1503.104|  0.940|17,571| 22269.002| 86.729| 789,034|
| |Suffolk County| 1,063| 1322.292|  1.244|21,579| 26842.657| 96.156| 803,907|
| |Worcester County|   993| 1195.490|  0.195|13,497| 16249.269| 33.018| 830,622|
| |Norfolk County|   991| 1402.144|  1.702|10,488| 14839.235| 25.468| 706,775|
| |Plymouth County|   714| 1369.910|  1.126| 9,185| 17622.726| 44.446| 521,202|
| |Hampden County|   699| 1498.804|  0.000| 7,518| 16120.179| 43.956| 466,372|
| |Bristol County|   626| 1107.539|  0.277| 9,255| 16374.242| 75.323| 565,217|
| |Barnstable County|   157| 737.124|  0.000| 1,778|  8347.810| 32.833| 212,990|
| |Hampshire County|   127| 789.654|  0.000| 1,150|  7150.407| 18.653| 160,830|
| |Franklin County|    61| 869.194|  0.000|   407|  5799.373| 12.028|  70,180|
| |Berkshire County|    46| 368.165|  0.000|   664|  5314.381| 23.262| 124,944|
| |Nantucket County|     0|  0.000| N/A|     0|     0.000| N/A|  11,399|
| |Dukes County|     0|  0.000| N/A|     0|     0.000| N/A|  17,332|


### Florida ###

![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Florida.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|FL|67 counties| 7,627| 355.112| N/A|502,100| 23377.696| N/A|21,477,737|
| |Miami-Dade County| 1,775| 653.309| 14.039|125,949| 46356.931| 412.425|2,716,940|
| |Palm Beach County|   882| 589.269| 11.712|35,283| 23572.760| 240.169|1,496,770|
| |Broward County|   783| 400.967|  7.465|59,354| 30394.648| 210.443|1,952,778|
| |Pinellas County|   467| 478.976|  9.312|17,202| 17643.149| 154.822| 974,996|
| |Hillsborough County|   377| 256.120|  6.657|31,197| 21194.075| 271.066|1,471,968|
| |Lee County|   317| 411.380|  0.000|15,961| 20713.050| 162.216| 770,577|
| |Polk County|   298| 411.161| 12.929|13,419| 18514.660| 194.543| 724,777|
| |Orange County|   250| 179.411|  3.891|30,425| 21834.265| 176.341|1,393,452|
| |Manatee County|   188| 466.209|  2.480| 8,938| 22164.745| 154.420| 403,253|
| |Duval County|   164| 171.234|  2.088|22,215| 23194.867| 200.991| 957,755|
| |St. Lucie County|   141| 429.489| 21.044| 5,396| 16436.337| 213.222| 328,297|
| |Brevard County|   132| 219.290| 10.101| 5,712|  9489.286| 53.161| 601,942|
| |Sarasota County|   129| 297.412|  7.853| 5,940| 13694.777| 155.161| 433,742|
| |Collier County|   129| 335.150|  5.184|10,050| 26110.542| 291.866| 384,902|
| |Volusia County|   121| 218.694|  4.083| 7,372| 13324.079| 160.317| 553,284|
| |Escambia County|   107| 336.144| 13.107| 8,367| 26285.201| 379.192| 318,316|
| |Seminole County|   105| 222.540|  2.119| 6,826| 14467.198| 140.235| 471,826|
| |Pasco County|   104| 187.744|  4.361| 6,708| 12109.462| 141.300| 553,947|
| |Osceola County|    94| 250.166| 12.691| 9,156| 24367.201| 298.070| 375,751|
| |Charlotte County|    89| 471.124|  0.000| 2,104| 11137.579| 142.041| 188,910|
| |Martin County|    84| 521.739| 17.435| 3,689| 22913.043| 43.478| 161,000|
| |Marion County|    76| 207.889| 15.229| 5,543| 15162.249| 345.123| 365,579|
| |Lake County|    59| 160.711|  0.000| 4,794| 13058.472| 119.511| 367,118|
| |Indian River County|    50| 312.650|  5.294| 2,385| 14913.427| 237.614| 159,923|
| |Clay County|    49| 223.487|  2.144| 3,021| 13778.666| 185.115| 219,252|
| |Bay County|    45| 257.577| 45.791| 3,988| 22827.051| 160.270| 174,705|
| |Sumter County|    40| 302.069| 18.913| 1,180|  8911.041| 142.769| 132,420|
| |Hernando County|    38| 195.957|  8.203| 1,842|  9498.762| 179.416| 193,920|
| |Suwannee County|    38| 855.528| 33.109| 1,224| 27557.016| 388.980|  44,417|
| |Hendry County|    37| 880.491|  0.000| 1,694| 40312.217| 326.830|  42,022|
| |Jackson County|    35| 754.083| 17.973| 1,745| 37596.415| 1368.122|  46,414|
| |Citrus County|    34| 227.186|  0.000| 1,373|  9174.312| 247.232| 149,657|
| |Okaloosa County|    34| 161.338|  7.647| 3,160| 14994.923| 333.482| 210,738|
| |Santa Rosa County|    32| 173.618| 14.053| 3,610| 19586.247| 285.337| 184,313|
| |St. Johns County|    31| 117.126|  3.186| 3,450| 13035.002| 105.791| 264,672|
| |Highlands County|    30| 282.430|  0.000| 1,311| 12342.192| 160.044| 106,221|
| |Alachua County|    25| 92.922|  3.101| 3,862| 14354.583| 229.690| 269,043|
| |Putnam County|    22| 295.219| 16.896| 1,422| 19081.870| 291.141|  74,521|
| |Gadsden County|    21| 459.921|  9.304| 1,614| 35348.226| 416.119|  45,660|
| |Leon County|    21| 71.530|  9.036| 4,537| 15453.945| 151.576| 293,582|
| |DeSoto County|    16| 421.042| 11.241| 1,313| 34551.722| 131.575|  38,001|
| |Washington County|    14| 549.602|  0.439|   716| 28108.193| 1638.985|  25,473|
| |Walton County|    14| 189.008|  6.346| 1,301| 17564.229| 277.741|  74,071|
| |Columbia County|    13| 181.346|  0.000| 2,672| 37273.666| 492.268|  71,686|
| |Flagler County|    13| 112.964|  8.787|   975|  8472.293| 130.432| 115,081|
| |Monroe County|    13| 175.136| 11.509| 1,404| 18914.695| 189.294|  74,228|
| |Nassau County|    11| 124.118|  1.770| 1,155| 13032.440| 191.819|  88,625|
| |Madison County|     8| 432.596| N/A|   663| 35851.403| N/A|  18,493|
| |Calhoun County|     7| 496.278| N/A|   334| 23679.546| N/A|  14,105|
| |Hardee County|     7| 259.866| N/A|   866| 32149.089| N/A|  26,937|
| |Okeechobee County|     6| 142.288| N/A|   975| 23121.799| N/A|  42,168|
| |Jefferson County|     5| 350.976| N/A|   433| 30394.497| N/A|  14,246|
| |Wakulla County|     4| 118.557| N/A|   635| 18820.949| N/A|  33,739|
| |Union County|     4| 262.519| N/A|   259| 16998.097| N/A|  15,237|
| |Taylor County|     4| 185.451| N/A|   768| 35606.658| N/A|  21,569|
| |Dixie County|     4| 237.727| N/A|   289| 17175.799| N/A|  16,826|
| |Baker County|     4| 136.939| N/A|   429| 14686.751| N/A|  29,210|
| |Bradford County|     4| 141.839| N/A|   343| 12162.689| N/A|  28,201|
| |Hamilton County|     4| 277.239| N/A|   595| 41239.257| N/A|  14,428|
| |Levy County|     4| 96.379| N/A|   632| 15227.815| N/A|  41,503|
| |Glades County|     3| 217.218| N/A|   396| 28672.797| N/A|  13,811|
| |Gilchrist County|     3| 161.447| N/A|   330| 17759.122| N/A|  18,582|
| |Gulf County|     2| 146.638| N/A|   436| 31967.153| N/A|  13,639|
| |Liberty County|     2| 239.406| N/A|   393| 47043.333| N/A|   8,354|
| |Holmes County|     2| 101.952| N/A|   460| 23449.049| N/A|  19,617|
| |Franklin County|     2| 164.948| N/A|   197| 16247.423| N/A|  12,125|
| |Lafayette County|     1| 118.737| N/A|   113| 13417.241| N/A|   8,422|


### Illinois ###

![Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Illinois.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IL|102 counties| 7,573| 597.625| N/A|186,401| 14709.883| N/A|12,671,821|
| |Cook County| 4,909| 953.161|  1.075|108,425| 21052.446| 114.364|5,150,233|
| |DuPage County|   515| 558.011|  1.872|11,804| 12789.827| 126.570| 922,921|
| |Lake County|   443| 636.005|  0.000|12,315| 17680.375| 162.232| 696,535|
| |Will County|   341| 493.671|  1.448| 8,821| 12770.307| 117.765| 690,743|
| |Kane County|   301| 565.361|  2.394| 9,417| 17687.729| 137.975| 532,403|
| |St. Clair County|   159| 612.278|  4.877| 3,753| 14452.069| 185.835| 259,686|
| |Winnebago County|   128| 452.982|  5.042| 3,730| 13200.176| 70.745| 282,572|
| |McHenry County|   114| 370.402|  0.000| 3,020|  9812.395| 91.109| 307,774|
| |Madison County|    73| 277.602|  0.000| 2,320|  8822.433| 178.701| 262,966|
| |Kankakee County|    68| 618.958|  0.000| 1,708| 15546.777| 87.446| 109,862|
| |Peoria County|    35| 195.335|  0.529| 1,445|  8064.561| 277.988| 179,179|
| |Sangamon County|    33| 169.516|  0.000| 1,096|  5629.983| 123.284| 194,672|
| |Rock Island County|    33| 232.593|  5.943| 1,649| 11622.580| 155.062| 141,879|
| |DeKalb County|    29| 276.462|  0.000|   884|  8427.314| 143.049| 104,897|
| |Boone County|    23| 429.553|  0.000|   749| 13988.495| 131.072|  53,544|
| |Macon County|    23| 221.135|  0.000|   517|  4970.724| 134.604| 104,009|
| |Kendall County|    23| 178.308|  0.000| 1,310| 10155.826| 54.268| 128,990|
| |Union County|    22| 1321.083| 24.979|   306| 18375.068| 90.074|  16,653|
| |LaSalle County|    21| 193.247|  6.715|   590|  5429.331| 137.013| 108,669|
| |Coles County|    20| 395.093| 19.755|   422|  8336.461| 186.040|  50,621|
| |Jackson County|    19| 334.802|  0.000|   676| 11911.894| 229.075|  56,750|
| |Champaign County|    19| 90.610|  0.000| 1,593|  7596.965| 109.686| 209,689|
| |Jefferson County|    19| 504.193| 22.077|   213|  5652.266| 256.201|  37,684|
| |Clinton County|    17| 452.585|  0.000|   366|  9743.890| 233.510|  37,562|
| |Whiteside County|    16| 289.986|  0.000|   329|  5962.845| 144.993|  55,175|
| |McDonough County|    15| 505.357|  0.000|   134|  4514.521| 64.009|  29,682|
| |McLean County|    15| 87.455|  0.000|   595|  3469.044| 64.134| 171,517|
| |Monroe County|    13| 375.321|  0.000|   292|  8430.291| 174.097|  34,637|
| |Cass County|    11| 905.573|  0.000|   214| 17617.519| 429.198|  12,147|
| |Iroquois County|     9| 331.932| N/A|   250|  9220.329| N/A|  27,114|
| |Tazewell County|     8| 60.697| N/A|   438|  3323.141| N/A| 131,803|
| |Montgomery County|     7| 246.357| N/A|   153|  5384.670| N/A|  28,414|
| |Randolph County|     7| 220.250| N/A|   440| 13844.314| N/A|  31,782|
| |Jasper County|     7| 728.408| N/A|    55|  5723.205| N/A|   9,610|
| |Stephenson County|     6| 134.838| N/A|   324|  7281.226| N/A|  44,498|
| |Morgan County|     6| 178.264| N/A|   213|  6328.362| N/A|  33,658|
| |Williamson County|     5| 75.078| N/A|   349|  5240.476| N/A|  66,597|
| |Ogle County|     5| 98.730| N/A|   392|  7740.458| N/A|  50,643|
| |Adams County|     5| 76.412| N/A|   461|  7045.159| N/A|  65,435|
| |Grundy County|     5| 97.936| N/A|   296|  5797.783| N/A|  51,054|
| |Christian County|     4| 123.824| N/A|   126|  3900.446| N/A|  32,304|
| |Carroll County|     4| 279.623| N/A|    46|  3215.659| N/A|  14,305|
| |Mercer County|     3| 194.338| N/A|    73|  4728.898| N/A|  15,437|
| |Fayette County|     3| 140.607| N/A|    58|  2718.410| N/A|  21,336|
| |Woodford County|     3| 78.005| N/A|   121|  3146.208| N/A|  38,459|
| |Macoupin County|     3| 66.776| N/A|   142|  3160.753| N/A|  44,926|
| |Vermilion County|     2| 26.400| N/A|   218|  2877.584| N/A|  75,758|
| |Livingston County|     2| 56.104| N/A|    99|  2777.154| N/A|  35,648|
| |Bond County|     2| 121.758| N/A|    59|  3591.867| N/A|  16,426|
| |Douglas County|     2| 102.749| N/A|   104|  5342.923| N/A|  19,465|
| |Cumberland County|     2| 185.770| N/A|    47|  4365.595| N/A|  10,766|
| |Bureau County|     2| 61.297| N/A|   161|  4934.412| N/A|  32,628|
| |Ford County|     1| 77.155| N/A|    45|  3471.954| N/A|  12,961|
| |Wayne County|     1| 61.671| N/A|    54|  3330.250| N/A|  16,215|
| |Shelby County|     1| 46.224| N/A|    67|  3096.977| N/A|  21,634|
| |Effingham County|     1| 29.405| N/A|   118|  3469.772| N/A|  34,008|
| |Clark County|     1| 64.763| N/A|    73|  4727.673| N/A|  15,441|
| |Gallatin County|     1| 207.125| N/A|    45|  9320.630| N/A|   4,828|
| |Henry County|     1| 20.444| N/A|   216|  4416.004| N/A|  48,913|
| |Saline County|     1| 42.569| N/A|   117|  4980.631| N/A|  23,491|
| |Hancock County|     1| 56.472| N/A|    39|  2202.394| N/A|  17,708|
| |Perry County|     1| 47.810| N/A|   136|  6502.199| N/A|  20,916|
| |Lee County|     1| 29.329| N/A|   149|  4370.014| N/A|  34,096|
| |Knox County|     1| 20.121| N/A|   279|  5613.795| N/A|  49,699|
| |Jo Daviess County|     1| 47.092| N/A|   119|  5603.956| N/A|  21,235|
| |Jersey County|     1| 45.928| N/A|    74|  3398.705| N/A|  21,773|
| |Washington County|     0|  0.000| N/A|    60|  4320.588| N/A|  13,887|
| |Pope County|     0|  0.000| N/A|     8|  1915.250| N/A|   4,177|
| |Pike County|     0|  0.000| N/A|    17|  1092.475| N/A|  15,561|
| |Piatt County|     0|  0.000| N/A|    52|  3181.596| N/A|  16,344|
| |Moultrie County|     0|  0.000| N/A|    66|  4551.410| N/A|  14,501|
| |Putnam County|     0|  0.000| N/A|     9|  1568.217| N/A|   5,739|
| |Pulaski County|     0|  0.000| N/A|    91| 17057.170| N/A|   5,335|
| |Richland County|     0|  0.000| N/A|    14|   902.469| N/A|  15,513|
| |Menard County|     0|  0.000| N/A|    50|  4099.705| N/A|  12,196|
| |Schuyler County|     0|  0.000| N/A|    17|  2511.820| N/A|   6,768|
| |Stark County|     0|  0.000| N/A|     7|  1310.371| N/A|   5,342|
| |White County|     0|  0.000| N/A|    61|  4506.168| N/A|  13,537|
| |Warren County|     0|  0.000| N/A|   185| 10983.139| N/A|  16,844|
| |Wabash County|     0|  0.000| N/A|    33|  2864.583| N/A|  11,520|
| |Scott County|     0|  0.000| N/A|    12|  2423.753| N/A|   4,951|
| |Massac County|     0|  0.000| N/A|    35|  2541.388| N/A|  13,772|
| |Mason County|     0|  0.000| N/A|    44|  3293.660| N/A|  13,359|
| |Brown County|     0|  0.000| N/A|    13|  1976.285| N/A|   6,578|
| |Hardin County|     0|  0.000| N/A|    17|  4449.097| N/A|   3,821|
| |Hamilton County|     0|  0.000| N/A|    25|  3080.335| N/A|   8,116|
| |Greene County|     0|  0.000| N/A|    28|  2158.995| N/A|  12,969|
| |Fulton County|     0|  0.000| N/A|    32|   931.858| N/A|  34,340|
| |Franklin County|     0|  0.000| N/A|   141|  3665.289| N/A|  38,469|
| |Edwards County|     0|  0.000| N/A|    16|  2501.955| N/A|   6,395|
| |Edgar County|     0|  0.000| N/A|    27|  1573.335| N/A|  17,161|
| |De Witt County|     0|  0.000| N/A|    32|  2046.297| N/A|  15,638|
| |Crawford County|     0|  0.000| N/A|    29|  1553.544| N/A|  18,667|
| |Clay County|     0|  0.000| N/A|    17|  1289.442| N/A|  13,184|
| |Calhoun County|     0|  0.000| N/A|     8|  1688.120| N/A|   4,739|
| |Johnson County|     0|  0.000| N/A|    62|  4993.155| N/A|  12,417|
| |Henderson County|     0|  0.000| N/A|    10|  1504.664| N/A|   6,646|
| |Lawrence County|     0|  0.000| N/A|    44|  2806.480| N/A|  15,678|
| |Marshall County|     0|  0.000| N/A|    21|  1835.985| N/A|  11,438|
| |Logan County|     0|  0.000| N/A|    90|  3144.874| N/A|  28,618|
| |Alexander County|     0|  0.000| N/A|    36|  6248.915| N/A|   5,761|
| |Marion County|     0|  0.000| N/A|   143|  3843.569| N/A|  37,205|


### Texas ###

![Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Texas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TX|254 counties| 7,467| 257.519| N/A|476,999| 16450.578| N/A|28,995,881|
| |Harris County|   805| 170.792|  3.147|80,914| 17167.074| 300.239|4,713,325|
| |Hidalgo County|   743| 855.294| 100.149|18,699| 21525.094| 712.551| 868,707|
| |Dallas County|   726| 275.468|  5.572|52,639| 19972.939| 205.050|2,635,516|
| |Bexar County|   673| 335.903| 13.476|41,614| 20770.092| 104.096|2,003,554|
| |Tarrant County|   410| 195.005|  4.590|30,162| 14345.676| 263.494|2,102,515|
| |Cameron County|   394| 931.083| 25.995|15,564| 36780.153| 2990.100| 423,163|
| |Travis County|   287| 225.283|  2.674|22,024| 17287.908| 317.908|1,273,954|
| |El Paso County|   280| 333.636| 15.159|15,427| 18382.151| 305.634| 839,238|
| |Nueces County|   217| 598.961| 31.101|13,321| 36768.481| 973.555| 362,294|
| |Fort Bend County|   151| 186.032|  6.160| 8,559| 10544.692| 118.272| 811,688|
| |Webb County|   144| 520.510|  3.615| 7,119| 25732.689| 1279.586| 276,652|
| |Galveston County|   106| 309.816|  0.000| 9,168| 26796.127| 500.821| 342,139|
| |Collin County|    85| 82.147|  0.000| 6,857|  6626.850| 26.944|1,034,730|
| |Brazoria County|    84| 224.441|  2.672| 6,887| 18401.449| 207.073| 374,264|
| |Williamson County|    83| 140.547|  5.080| 5,949| 10073.643| 99.060| 590,551|
| |Denton County|    80| 90.171|  2.254| 7,257|  8179.602| 179.778| 887,207|
| |Montgomery County|    76| 125.125|  2.348| 6,459| 10634.007| 138.336| 607,391|
| |Jefferson County|    74| 294.159|  3.975| 5,721| 22741.637| 354.678| 251,565|
| |Comal County|    67| 428.913| 12.803| 1,720| 11010.889| 131.234| 156,209|
| |Lubbock County|    67| 215.733|  3.220| 5,751| 18517.624| 255.814| 310,569|
| |Ector County|    52| 312.833|  0.000| 3,481| 20941.747| 246.657| 166,223|
| |Starr County|    52| 804.543|  7.736| 2,025| 31330.744| 1013.414|  64,633|
| |Val Verde County|    49| 999.490|  0.000| 1,581| 32248.853|  0.000|  49,025|
| |Guadalupe County|    48| 287.689| 17.981| 1,650|  9889.300|  0.000| 166,847|
| |Brazos County|    46| 200.688|  0.000| 3,973| 17333.374| 111.430| 229,211|
| |Midland County|    45| 254.479|  7.007| 2,492| 14092.472|  0.000| 176,832|
| |McLennan County|    43| 167.561|  0.000| 4,694| 18291.424| 501.537| 256,623|
| |Potter County|    43| 366.222|  0.000| 3,607| 30720.095|  0.000| 117,415|
| |Walker County|    40| 548.163| 27.408| 2,838| 38892.163|  0.000|  72,971|
| |Nacogdoches County|    38| 582.786| 12.308| 1,067| 16364.027| 245.384|  65,204|
| |Angelina County|    38| 438.217| 11.532| 1,755| 20238.713| 491.032|  86,715|
| |Washington County|    38| 1059.027|  0.000|   498| 13878.825| 13.935|  35,882|
| |Ellis County|    37| 200.188| 10.821| 2,691| 14559.640| 500.170| 184,826|
| |Hays County|    35| 152.048|  4.344| 4,969| 21586.422| 545.350| 230,191|
| |Victoria County|    34| 369.228| 24.655| 3,331| 36173.494| 574.562|  92,084|
| |Bell County|    33| 90.928|  1.609| 3,680| 10139.864| 175.168| 362,924|
| |Bowie County|    31| 332.458|  5.362|   708|  7592.900|  0.000|  93,245|
| |Liberty County|    30| 340.063| 22.671|   869|  9850.486| 101.563|  88,219|
| |Johnson County|    30| 170.632| 12.849| 1,730|  9839.777| 425.286| 175,817|
| |Maverick County|    29| 493.852|  0.000| 1,852| 31538.435|  0.000|  58,722|
| |Wharton County|    25| 601.598| 40.578|   644| 15497.160| 264.703|  41,556|
| |Hale County|    24| 718.434|  0.000| 1,244| 37238.819| 568.223|  33,406|
| |Caldwell County|    24| 549.652|  0.000| 1,096| 25100.770| 22.902|  43,664|
| |Tom Green County|    24| 201.342|  0.000| 2,513| 21082.215| 387.951| 119,200|
| |Medina County|    24| 465.261|  0.000|   615| 11922.301| 19.386|  51,584|
| |Matagorda County|    23| 627.678|  8.562|   692| 18884.917| 218.323|  36,643|
| |Kaufman County|    22| 161.582|  3.456| 2,007| 14740.661|  0.000| 136,154|
| |Harrison County|    22| 330.564|  0.000|   644|  9676.498| 135.287|  66,553|
| |Gregg County|    22| 177.498|  5.887| 1,348| 10875.792|  0.000| 123,945|
| |Hunt County|    21| 212.995|  5.360| 1,105| 11207.579| 212.747|  98,594|
| |Willacy County|    21| 983.238| 34.690|   644| 30152.636| 1038.299|  21,358|
| |Taylor County|    21| 152.136|  5.808| 1,106|  8012.519| 54.039| 138,034|
| |Grimes County|    20| 692.521|  0.000|   861| 29813.019| 207.756|  28,880|
| |Bastrop County|    20| 225.421| 22.542| 1,313| 14798.868| 79.934|  88,723|
| |San Patricio County|    19| 284.730| 18.869|   867| 12992.657| 390.743|  66,730|
| |Smith County|    18| 77.336|  1.817| 2,416| 10380.192|  0.000| 232,751|
| |Randall County|    18| 130.707|  3.414| 1,646| 11952.394| 147.884| 137,713|
| |Orange County|    18| 215.838|  6.869| 1,369| 16415.655| 1426.927|  83,396|
| |Shelby County|    18| 712.194| 33.359|   390| 15430.878| 161.465|  25,274|
| |Panola County|    17| 732.948|  0.000|   273| 11770.285| 61.155|  23,194|
| |Deaf Smith County|    17| 916.640|  0.000|   629| 33915.669| 705.548|  18,546|
| |Wilson County|    17| 332.876| 19.581|   430|  8419.816| 156.648|  51,070|
| |Atascosa County|    16| 312.787| 19.549|   419|  8191.113| 117.295|  51,153|
| |Lamar County|    16| 320.905|  0.000|   642| 12876.311| 159.942|  49,859|
| |Brown County|    15| 396.155| 11.281|   356|  9402.071| 55.015|  37,864|
| |DeWitt County|    15| 744.048|  0.000|   641| 31795.635| 744.048|  20,160|
| |Parker County|    15| 104.985|  9.870| 1,160|  8118.815| 258.962| 142,878|
| |Titus County|    14| 427.481|  0.000| 1,289| 39358.779|  0.000|  32,750|
| |Lavaca County|    14| 694.651|  0.000|   625| 31011.214| 680.760|  20,154|
| |Fayette County|    14| 552.355| 16.412|   376| 14834.688| 151.456|  25,346|
| |Jim Wells County|    13| 321.130| 49.405|   658| 16254.138| 345.833|  40,482|
| |Rockwall County|    12| 114.378|  0.000|   786|  7491.779| 265.540| 104,915|
| |Aransas County|    12| 510.421|  0.000|   162|  6890.685| 106.240|  23,510|
| |Moore County|    12| 573.066|  0.000| 1,035| 49426.934| 432.759|  20,940|
| |Grayson County|    11| 80.756|  0.000| 1,051|  7715.913| 117.464| 136,212|
| |Polk County|    11| 214.204| 16.636|   693| 13494.830| 136.311|  51,353|
| |Red River County|    11| 914.913|  0.000|   135| 11228.479| 34.448|  12,023|
| |Henderson County|    11| 132.951|  0.000|   609|  7360.673| 146.444|  82,737|
| |Hardin County|    11| 190.966|  0.000|   902| 15659.179| 547.129|  57,602|
| |Wichita County|    11| 83.188|  4.296|   946|  7154.201| 105.876| 132,230|
| |San Augustine County|    11| 1335.438|  0.000|   157| 19060.338| 102.226|   8,237|
| |Anderson County|    10| 173.205|  8.142| 2,355| 40789.816| 450.333|  57,735|
| |Lamb County|    10| 775.615| 155.123|   213| 16520.593| 322.702|  12,893|
| |Bee County|     9| 276.370| N/A|   696| 21372.639| N/A|  32,565|
| |Gonzales County|     9| 431.924| N/A|   646| 31002.544| N/A|  20,837|
| |Lee County|     9| 522.072| N/A|   163|  9455.305| N/A|  17,239|
| |Hood County|     9| 146.002| N/A|   490|  7948.997| N/A|  61,643|
| |San Jacinto County|     8| 277.210| N/A|   175|  6063.966| N/A|  28,859|
| |Navarro County|     8| 159.639| N/A|   810| 16163.471| N/A|  50,113|
| |Fannin County|     8| 225.263| N/A|   237|  6673.425| N/A|  35,514|
| |Marion County|     8| 811.853| N/A|   128| 12989.649| N/A|   9,854|
| |Burnet County|     7| 145.364| N/A|   544| 11296.854| N/A|  48,155|
| |Uvalde County|     7| 261.770| N/A|   506| 18922.254| N/A|  26,741|
| |Cass County|     7| 233.131| N/A|   160|  5328.715| N/A|  30,026|
| |Parmer County|     7| 728.787| N/A|   323| 33628.319| N/A|   9,605|
| |Burleson County|     6| 325.327| N/A|   235| 12741.962| N/A|  18,443|
| |Wise County|     6| 85.734| N/A|   365|  5215.478| N/A|  69,984|
| |Kleberg County|     6| 195.567| N/A|   389| 12679.270| N/A|  30,680|
| |Andrews County|     6| 320.770| N/A|   273| 14595.028| N/A|  18,705|
| |Sabine County|     6| 569.152| N/A|    51|  4837.792| N/A|  10,542|
| |Palo Pinto County|     6| 205.557| N/A|   236|  8085.238| N/A|  29,189|
| |Houston County|     6| 261.233| N/A|   307| 13366.423| N/A|  22,968|
| |Kerr County|     6| 114.068| N/A|   384|  7300.380| N/A|  52,600|
| |Coryell County|     5| 65.832| N/A|   636|  8373.820| N/A|  75,951|
| |Camp County|     5| 381.854| N/A|   219| 16725.218| N/A|  13,094|
| |Cherokee County|     5| 94.974| N/A|   832| 15803.670| N/A|  52,646|
| |Zavala County|     5| 422.297| N/A|   197| 16638.514| N/A|  11,840|
| |Duval County|     5| 448.149| N/A|   161| 14430.402| N/A|  11,157|
| |Wood County|     5| 109.796| N/A|   313|  6873.230| N/A|  45,539|
| |Erath County|     5| 117.102| N/A|   489| 11452.527| N/A|  42,698|
| |Blanco County|     5| 419.076| N/A|    98|  8213.897| N/A|  11,931|
| |Dallam County|     5| 686.153| N/A|   183| 25113.215| N/A|   7,287|
| |Jackson County|     5| 338.753| N/A|   380| 25745.257| N/A|  14,760|
| |Floyd County|     5| 875.350| N/A|    86| 15056.022| N/A|   5,712|
| |Hill County|     5| 136.429| N/A|   313|  8540.479| N/A|  36,649|
| |Jasper County|     5| 140.730| N/A|   302|  8500.099| N/A|  35,529|
| |Karnes County|     5| 320.492| N/A|   391| 25062.496| N/A|  15,601|
| |Frio County|     5| 246.233| N/A|   495| 24377.031| N/A|  20,306|
| |Gillespie County|     5| 185.268| N/A|   174|  6447.310| N/A|  26,988|
| |Goliad County|     4| 522.330| N/A|    77| 10054.845| N/A|   7,658|
| |Young County|     4| 222.099| N/A|   152|  8439.756| N/A|  18,010|
| |Hockley County|     4| 173.754| N/A|   191|  8296.773| N/A|  23,021|
| |Waller County|     4| 72.403| N/A|   417|  7548.058| N/A|  55,246|
| |Reeves County|     4| 250.376| N/A|   143|  8950.926| N/A|  15,976|
| |Lynn County|     4| 672.156| N/A|    66| 11090.573| N/A|   5,951|
| |Kendall County|     4| 84.333| N/A|   155|  3267.905| N/A|  47,431|
| |Newton County|     4| 294.226| N/A|    92|  6767.194| N/A|  13,595|
| |Dawson County|     4| 314.268| N/A|   137| 10763.671| N/A|  12,728|
| |Bailey County|     4| 571.429| N/A|   166| 23714.286| N/A|   7,000|
| |Calhoun County|     4| 187.882| N/A|   511| 24001.879| N/A|  21,290|
| |Castro County|     4| 531.208| N/A|   188| 24966.799| N/A|   7,530|
| |Martin County|     3| 519.841| N/A|    48|  8317.449| N/A|   5,771|
| |Milam County|     3| 120.856| N/A|   327| 13173.267| N/A|  24,823|
| |Cooke County|     3| 72.715| N/A|   206|  4993.092| N/A|  41,257|
| |Van Zandt County|     3| 53.013| N/A|   362|  6396.890| N/A|  56,590|
| |Crockett County|     3| 866.051| N/A|   156| 45034.642| N/A|   3,464|
| |Falls County|     3| 173.440| N/A|   114|  6590.738| N/A|  17,297|
| |Trinity County|     3| 204.764| N/A|   153| 10442.973| N/A|  14,651|
| |Comanche County|     3| 220.022| N/A|   121|  8874.221| N/A|  13,635|
| |Howard County|     3| 81.824| N/A|   162|  4418.503| N/A|  36,664|
| |Reagan County|     3| 779.423| N/A|    61| 15848.272| N/A|   3,849|
| |Callahan County|     3| 215.162| N/A|    46|  3299.147| N/A|  13,943|
| |Bandera County|     3| 129.803| N/A|    89|  3850.813| N/A|  23,112|
| |Austin County|     3| 99.893| N/A|   218|  7258.924| N/A|  30,032|
| |Nolan County|     3| 203.887| N/A|   132|  8971.048| N/A|  14,714|
| |Limestone County|     3| 128.003| N/A|   201|  8576.183| N/A|  23,437|
| |Dimmit County|     3| 296.326| N/A|   138| 13630.976| N/A|  10,124|
| |Tyler County|     2| 92.285| N/A|   115|  5306.386| N/A|  21,672|
| |Terry County|     2| 162.114| N/A|   125| 10132.123| N/A|  12,337|
| |Upshur County|     2| 47.901| N/A|   200|  4790.075| N/A|  41,753|
| |Stephens County|     2| 213.538| N/A|    31|  3309.844| N/A|   9,366|
| |Swisher County|     2| 270.380| N/A|    79| 10680.005| N/A|   7,397|
| |Rusk County|     2| 36.761| N/A|   341|  6267.691| N/A|  54,406|
| |Zapata County|     2| 141.054| N/A|   165| 11636.928| N/A|  14,179|
| |Ochiltree County|     2| 203.335| N/A|    89|  9048.394| N/A|   9,836|
| |Yoakum County|     2| 229.542| N/A|    90| 10329.393| N/A|   8,713|
| |Lampasas County|     2| 93.336| N/A|    86|  4013.440| N/A|  21,428|
| |Robertson County|     2| 117.137| N/A|   220| 12885.088| N/A|  17,074|
| |Madison County|     2| 140.017| N/A|   645| 45155.419| N/A|  14,284|
| |Live Oak County|     2| 163.840| N/A|   222| 18186.287| N/A|  12,207|
| |Leon County|     2| 114.916| N/A|   138|  7929.212| N/A|  17,404|
| |Bosque County|     2| 107.038| N/A|   136|  7278.566| N/A|  18,685|
| |Hudspeth County|     2| 409.333| N/A|    22|  4502.661| N/A|   4,886|
| |Hutchinson County|     2| 95.520| N/A|   120|  5731.206| N/A|  20,938|
| |Garza County|     2| 321.079| N/A|    99| 15893.402| N/A|   6,229|
| |Hamilton County|     2| 236.379| N/A|    55|  6500.414| N/A|   8,461|
| |Culberson County|     2| 921.234| N/A|    16|  7369.876| N/A|   2,171|
| |Hansford County|     2| 370.439| N/A|    58| 10742.730| N/A|   5,399|
| |Cottle County|     2| 1430.615| N/A|    14| 10014.306| N/A|   1,398|
| |Gray County|     2| 91.383| N/A|   205|  9366.718| N/A|  21,886|
| |Brewster County|     2| 217.320| N/A|   186| 20210.801| N/A|   9,203|
| |Chambers County|     2| 45.624| N/A|   924| 21078.085| N/A|  43,837|
| |Crane County|     2| 416.927| N/A|    70| 14592.454| N/A|   4,797|
| |Colorado County|     2| 93.054| N/A|   257| 11957.381| N/A|  21,493|
| |Sutton County|     1| 264.831| N/A|    60| 15889.831| N/A|   3,776|
| |Scurry County|     1| 59.869| N/A|   454| 27180.746| N/A|  16,703|
| |Franklin County|     1| 93.240| N/A|    89|  8298.368| N/A|  10,725|
| |Schleicher County|     1| 358.038| N/A|    35| 12531.328| N/A|   2,793|
| |Wilbarger County|     1| 78.315| N/A|    56|  4385.621| N/A|  12,769|
| |Ward County|     1| 83.347| N/A|    84|  7001.167| N/A|  11,998|
| |Upton County|     1| 273.448| N/A|    16|  4375.171| N/A|   3,657|
| |Winkler County|     1| 124.844| N/A|    70|  8739.076| N/A|   8,010|
| |Runnels County|     1| 97.428| N/A|   116| 11301.637| N/A|  10,264|
| |Refugio County|     1| 143.926| N/A|   216| 31088.083| N/A|   6,948|
| |Rains County|     1| 79.911| N/A|    47|  3755.794| N/A|  12,514|
| |Eastland County|     1| 54.466| N/A|    63|  3431.373| N/A|  18,360|
| |Hall County|     1| 337.382| N/A|    10|  3373.819| N/A|   2,964|
| |Fisher County|     1| 261.097| N/A|    26|  6788.512| N/A|   3,830|
| |Brooks County|     1| 140.984| N/A|    94| 13252.502| N/A|   7,093|
| |Briscoe County|     1| 646.831| N/A|    11|  7115.136| N/A|   1,546|
| |Dickens County|     1| 452.284| N/A|     4|  1809.136| N/A|   2,211|
| |Coke County|     1| 295.247| N/A|    40| 11809.861| N/A|   3,387|
| |Crosby County|     1| 174.307| N/A|    58| 10109.813| N/A|   5,737|
| |Hopkins County|     1| 26.966| N/A|   183|  4934.743| N/A|  37,084|
| |La Salle County|     1| 132.979| N/A|   356| 47340.426| N/A|   7,520|
| |Oldham County|     1| 473.485| N/A|    14|  6628.788| N/A|   2,112|
| |Pecos County|     1| 63.199| N/A|   226| 14283.006| N/A|  15,823|
| |Kenedy County|     1| 2475.248| N/A|     6| 14851.485| N/A|     404|
| |Jim Hogg County|     1| 192.308| N/A|    54| 10384.615| N/A|   5,200|
| |Clay County|     1| 95.502| N/A|    36|  3438.067| N/A|  10,471|
| |Montague County|     1| 50.459| N/A|    61|  3078.010| N/A|  19,818|
| |Morris County|     1| 80.723| N/A|    98|  7910.881| N/A|  12,388|
| |McCulloch County|     1| 125.251| N/A|    45|  5636.273| N/A|   7,984|
| |Llano County|     1| 45.882| N/A|    86|  3945.859| N/A|  21,795|
| |Archer County|     0|  0.000| N/A|    20|  2338.361| N/A|   8,553|
| |Armstrong County|     0|  0.000| N/A|     7|  3709.592| N/A|   1,887|
| |Baylor County|     0|  0.000| N/A|     8|  2279.852| N/A|   3,509|
| |Borden County|     0|  0.000| N/A|     0|     0.000| N/A|     654|
| |Glasscock County|     0|  0.000| N/A|     6|  4258.339| N/A|   1,409|
| |McMullen County|     0|  0.000| N/A|     8| 10767.160| N/A|     743|
| |Kent County|     0|  0.000| N/A|     3|  3937.008| N/A|     762|
| |Kimble County|     0|  0.000| N/A|    13|  2997.464| N/A|   4,337|
| |King County|     0|  0.000| N/A|     0|     0.000| N/A|     272|
| |Carson County|     0|  0.000| N/A|    14|  2362.470| N/A|   5,926|
| |Cochran County|     0|  0.000| N/A|    31| 10865.755| N/A|   2,853|
| |Real County|     0|  0.000| N/A|    86| 24913.094| N/A|   3,452|
| |Presidio County|     0|  0.000| N/A|    45|  6712.411| N/A|   6,704|
| |Donley County|     0|  0.000| N/A|    45| 13727.883| N/A|   3,278|
| |Childress County|     0|  0.000| N/A|    36|  4927.457| N/A|   7,306|
| |Coleman County|     0|  0.000| N/A|    16|  1957.187| N/A|   8,175|
| |Collingsworth County|     0|  0.000| N/A|     7|  2397.260| N/A|   2,920|
| |Concho County|     0|  0.000| N/A|    26|  9537.784| N/A|   2,726|
| |Delta County|     0|  0.000| N/A|    16|  3001.313| N/A|   5,331|
| |Edwards County|     0|  0.000| N/A|    27| 13975.155| N/A|   1,932|
| |Foard County|     0|  0.000| N/A|     2|  1731.602| N/A|   1,155|
| |Freestone County|     0|  0.000| N/A|   142|  7201.907| N/A|  19,717|
| |Gaines County|     0|  0.000| N/A|   145|  6746.696| N/A|  21,492|
| |Kinney County|     0|  0.000| N/A|    18|  4908.645| N/A|   3,667|
| |Knox County|     0|  0.000| N/A|    53| 14465.066| N/A|   3,664|
| |Lipscomb County|     0|  0.000| N/A|    16|  4948.964| N/A|   3,233|
| |Irion County|     0|  0.000| N/A|     9|  5859.375| N/A|   1,536|
| |Loving County|     0|  0.000| N/A|     0|     0.000| N/A|     169|
| |Hemphill County|     0|  0.000| N/A|    42| 10997.643| N/A|   3,819|
| |Haskell County|     0|  0.000| N/A|    39|  6892.895| N/A|   5,658|
| |Hartley County|     0|  0.000| N/A|    82| 14705.882| N/A|   5,576|
| |Hardeman County|     0|  0.000| N/A|    17|  4322.400| N/A|   3,933|
| |Mason County|     0|  0.000| N/A|    45| 10528.779| N/A|   4,274|
| |Menard County|     0|  0.000| N/A|    17|  7951.356| N/A|   2,138|
| |Mills County|     0|  0.000| N/A|    16|  3283.398| N/A|   4,873|
| |Mitchell County|     0|  0.000| N/A|    58|  6787.595| N/A|   8,545|
| |Motley County|     0|  0.000| N/A|     4|  3333.333| N/A|   1,200|
| |Jones County|     0|  0.000| N/A|   631| 31419.609| N/A|  20,083|
| |Jeff Davis County|     0|  0.000| N/A|     8|  3518.030| N/A|   2,274|
| |Jack County|     0|  0.000| N/A|    47|  5260.213| N/A|   8,935|
| |Sterling County|     0|  0.000| N/A|     0|     0.000| N/A|   1,291|
| |Roberts County|     0|  0.000| N/A|     6|  7025.761| N/A|     854|
| |San Saba County|     0|  0.000| N/A|    22|  3633.361| N/A|   6,055|
| |Shackelford County|     0|  0.000| N/A|    17|  5206.738| N/A|   3,265|
| |Sherman County|     0|  0.000| N/A|    39| 12905.361| N/A|   3,022|
| |Somervell County|     0|  0.000| N/A|    65|  7120.947| N/A|   9,128|
| |Stonewall County|     0|  0.000| N/A|     5|  3703.704| N/A|   1,350|
| |Terrell County|     0|  0.000| N/A|     2|  2577.320| N/A|     776|
| |Throckmorton County|     0|  0.000| N/A|     4|  2664.890| N/A|   1,501|
| |Wheeler County|     0|  0.000| N/A|    32|  6329.114| N/A|   5,056|


### Pennsylvania ###

![Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Pennsylvania.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|PA|67 counties| 7,254| 566.631| N/A|120,446|  9408.382| N/A|12,801,989|
| |Philadelphia County| 1,695| 1070.033| N/A|30,877| 19492.268| N/A|1,584,064|
| |Montgomery County|   853| 1026.579|  1.503| 9,952| 11977.158| 42.122| 830,915|
| |Delaware County|   693| 1222.768|  4.500| 9,032| 15936.564| 134.099| 566,747|
| |Bucks County|   580| 923.170|  0.000| 7,085| 11276.999| 49.919| 628,270|
| |Lancaster County|   408| 747.631|  0.776| 5,725| 10490.651| 39.397| 545,724|
| |Berks County|   367| 871.395|  2.028| 5,267| 12505.817| 58.172| 421,164|
| |Chester County|   349| 664.776|  0.494| 5,040|  9600.201| 71.430| 524,989|
| |Lehigh County|   335| 907.077|  0.000| 4,887| 13232.499| 46.031| 369,318|
| |Northampton County|   291| 953.208|  1.356| 3,891| 12745.467| 42.500| 305,285|
| |Allegheny County|   239| 196.539|  1.645| 8,512|  6999.741| 78.506|1,216,045|
| |Lackawanna County|   212| 1011.093|  0.000| 1,912|  9118.918| 22.793| 209,674|
| |Luzerne County|   183| 576.529|  0.000| 3,377| 10639.002| 62.308| 317,417|
| |Dauphin County|   156| 560.548|  1.689| 2,723|  9784.440| 75.458| 278,299|
| |Monroe County|   124| 728.251|  2.761| 1,611|  9461.388| 38.174| 170,271|
| |Beaver County|    89| 542.918|  0.000| 1,269|  7741.156| 86.713| 163,929|
| |York County|    89| 198.193|  0.951| 2,400|  5344.521| 55.475| 449,058|
| |Cumberland County|    70| 276.276|  0.000| 1,259|  4969.018| 50.900| 253,370|
| |Lebanon County|    54| 380.837|  0.000| 1,584| 11171.214| 27.587| 141,793|
| |Schuylkill County|    49| 346.635|  0.000|   905|  6402.139| 32.045| 141,359|
| |Westmoreland County|    46| 131.843|  0.000| 1,475|  4227.584| 34.925| 348,899|
| |Franklin County|    46| 296.723|  0.000| 1,305|  8417.888| 19.351| 155,027|
| |Columbia County|    35| 538.760|  0.000|   468|  7203.990| 41.090|  64,964|
| |Carbon County|    28| 436.259|  0.000|   364|  5671.372| 25.605|  64,182|
| |Susquehanna County|    27| 669.510| 10.592|   212|  5256.893| 20.393|  40,328|
| |Pike County|    21| 376.283|  0.000|   526|  9425.003|  0.000|  55,809|
| |Adams County|    20| 194.158|  0.000|   483|  4688.911| 21.355| 103,009|
| |Lycoming County|    20| 176.524|  0.000|   351|  3097.997| 47.211| 113,299|
| |Erie County|    17| 63.026|  0.000| 1,037|  3844.614| 94.326| 269,728|
| |Butler County|    15| 79.850|  0.000|   624|  3321.746| 39.864| 187,853|
| |Lawrence County|    12| 140.331|  0.000|   359|  4198.241| 58.471|  85,512|
| |Northumberland County|    11| 121.088|  0.000|   421|  4634.369| 64.923|  90,843|
| |Washington County|    11| 53.175|  0.000|   785|  3794.745| 48.781| 206,865|
| |Centre County|    10| 61.582|  0.000|   361|  2223.112|  6.158| 162,385|
| |Mercer County|     9| 82.249| N/A|   376|  3436.175| N/A| 109,424|
| |Wyoming County|     8| 298.574| N/A|    58|  2164.664| N/A|  26,794|
| |Wayne County|     8| 155.760| N/A|   157|  3056.794| N/A|  51,361|
| |Armstrong County|     6| 92.686| N/A|   196|  3027.728| N/A|  64,735|
| |Juniata County|     6| 242.297| N/A|   128|  5169.002| N/A|  24,763|
| |Indiana County|     6| 71.367| N/A|   283|  3366.122| N/A|  84,073|
| |Perry County|     5| 108.057| N/A|   120|  2593.361| N/A|  46,272|
| |Clinton County|     5| 129.426| N/A|   118|  3054.463| N/A|  38,632|
| |Bedford County|     4| 83.528| N/A|   134|  2798.196| N/A|  47,888|
| |Fayette County|     4| 30.942| N/A|   431|  3334.004| N/A| 129,274|
| |Huntingdon County|     4| 88.605| N/A|   295|  6534.645| N/A|  45,144|
| |Cambria County|     3| 23.043| N/A|   312|  2396.461| N/A| 130,192|
| |Bradford County|     3| 49.732| N/A|    85|  1409.081| N/A|  60,323|
| |Montour County|     3| 164.564| N/A|    97|  5320.900| N/A|  18,230|
| |Somerset County|     3| 40.846| N/A|   127|  1729.138| N/A|  73,447|
| |Blair County|     3| 24.625| N/A|   241|  1978.183| N/A| 121,829|
| |Tioga County|     3| 73.908| N/A|    36|   886.896| N/A|  40,591|
| |Snyder County|     2| 49.539| N/A|   100|  2476.964| N/A|  40,372|
| |Elk County|     2| 66.867| N/A|    46|  1537.947| N/A|  29,910|
| |Fulton County|     2| 137.646| N/A|    25|  1720.578| N/A|  14,530|
| |Union County|     2| 44.521| N/A|   201|  4474.323| N/A|  44,923|
| |Clarion County|     2| 52.032| N/A|    77|  2003.226| N/A|  38,438|
| |Greene County|     1| 27.599| N/A|   110|  3035.906| N/A|  36,233|
| |Mifflin County|     1| 21.674| N/A|   113|  2449.174| N/A|  46,138|
| |Jefferson County|     1| 23.028| N/A|    61|  1404.721| N/A|  43,425|
| |McKean County|     1| 24.615| N/A|    33|   812.308| N/A|  40,625|
| |Crawford County|     1| 11.816| N/A|   136|  1607.014| N/A|  84,629|
| |Warren County|     1| 25.516| N/A|    20|   510.321| N/A|  39,191|
| |Forest County|     0|  0.000| N/A|     9|  1241.893| N/A|   7,247|
| |Venango County|     0|  0.000| N/A|    62|  1223.652| N/A|  50,668|
| |Sullivan County|     0|  0.000| N/A|    10|  1648.533| N/A|   6,066|
| |Potter County|     0|  0.000| N/A|    20|  1210.214| N/A|  16,526|
| |Clearfield County|     0|  0.000| N/A|   144|  1816.920| N/A|  79,255|
| |Cameron County|     0|  0.000| N/A|     6|  1349.224| N/A|   4,447|


### Michigan ###

![Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Michigan.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MI|83 counties| 6,403| 641.143| N/A|89,286|  8940.350| N/A|9,986,857|
| |Wayne County| 2,809| 1605.746|  1.223|27,688| 15827.656| 87.938|1,749,343|
| |Oakland County| 1,127| 896.163|  0.421|15,030| 11951.488| 67.130|1,257,584|
| |Macomb County|   937| 1072.117|  0.538| 9,932| 11364.208| 119.688| 873,972|
| |Genesee County|   295| 726.936|  0.000| 3,581|  8824.261| 71.081| 405,813|
| |Kent County|   154| 234.415|  0.000| 7,336| 11166.670| 76.620| 656,955|
| |Saginaw County|   129| 677.027|  0.000| 1,908| 10013.698| 52.483| 190,539|
| |Washtenaw County|   112| 304.678|  0.000| 2,471|  6721.962| 61.661| 367,601|
| |Kalamazoo County|    82| 309.357|  0.588| 1,588|  5990.961| 52.587| 265,066|
| |Berrien County|    66| 430.245|  6.519| 1,315|  8572.304| 64.511| 153,401|
| |Muskegon County|    58| 334.167|  0.000| 1,143|  6585.391| 41.742| 173,566|
| |Ottawa County|    55| 188.466|  1.448| 1,763|  6041.188| 33.866| 291,830|
| |St. Clair County|    53| 333.065|  0.000|   790|  4964.557| 35.641| 159,128|
| |Calhoun County|    41| 305.608|  0.000|   768|  5724.551| 70.811| 134,159|
| |Jackson County|    33| 208.189|  0.000|   701|  4422.434| 35.156| 158,510|
| |Lapeer County|    33| 376.682| 11.415|   452|  5159.405| 160.753|  87,607|
| |Bay County|    31| 300.603|  0.000|   567|  5498.129| 65.617| 103,126|
| |Ingham County|    30| 102.597|  0.000| 1,503|  5140.113| 20.466| 292,406|
| |Tuscola County|    29| 555.077| 11.179|   324|  6201.550| 57.422|  52,245|
| |Shiawassee County|    28| 411.027|  0.000|   335|  4917.648| 44.039|  68,122|
| |Livingston County|    28| 145.837|  0.000|   805|  4192.818| 54.533| 191,995|
| |Hillsdale County|    25| 548.186|  0.000|   253|  5547.637| 18.566|  45,605|
| |Monroe County|    22| 146.179|  0.000|   935|  6212.625| 102.791| 150,500|
| |Gratiot County|    15| 368.451|  0.000|   146|  3586.254|  0.000|  40,711|
| |Clinton County|    13| 163.327|  0.000|   419|  5264.150| 28.275|  79,595|
| |Alpena County|    13| 457.666|  0.000|   127|  4471.044| 37.311|  28,405|
| |Iosco County|    12| 477.574|  0.000|   129|  5133.920|  0.000|  25,127|
| |Cass County|    12| 231.718| 19.310|   302|  5831.579| 83.754|  51,787|
| |Lenawee County|    12| 121.888|  0.000|   409|  4154.351| 50.787|  98,451|
| |Marquette County|    11| 164.920|  0.000|   146|  2188.938| 54.605|  66,699|
| |Van Buren County|    11| 145.355|  0.000|   425|  5615.973| 73.579|  75,677|
| |Otsego County|    10| 405.383|  0.000|   131|  5310.524|  0.000|  24,668|
| |Midland County|    10| 120.256|  0.000|   315|  3788.061| 24.051|  83,156|
| |Isabella County|     9| 128.807| N/A|   204|  2919.624| N/A|  69,872|
| |St. Joseph County|     8| 131.225| N/A|   569|  9333.377| N/A|  60,964|
| |Eaton County|     8| 72.551| N/A|   449|  4071.898| N/A| 110,268|
| |Allegan County|     7| 59.281| N/A|   504|  4268.257| N/A| 118,081|
| |Oceana County|     6| 226.697| N/A|   467| 17644.614| N/A|  26,467|
| |Sanilac County|     6| 145.737| N/A|   101|  2453.243| N/A|  41,170|
| |Crawford County|     5| 356.405| N/A|   103|  7341.935| N/A|  14,029|
| |Grand Traverse County|     5| 53.713| N/A|   199|  2137.762| N/A|  93,088|
| |Ionia County|     5| 77.283| N/A|   272|  4204.213| N/A|  64,697|
| |Huron County|     4| 129.111| N/A|   149|  4809.399| N/A|  30,981|
| |Wexford County|     4| 118.938| N/A|    68|  2021.944| N/A|  33,631|
| |Kalkaska County|     4| 221.754| N/A|    49|  2716.487| N/A|  18,038|
| |Delta County|     3| 83.836| N/A|    85|  2375.363| N/A|  35,784|
| |Clare County|     3| 96.931| N/A|    64|  2067.851| N/A|  30,950|
| |Arenac County|     3| 201.572| N/A|    41|  2754.821| N/A|  14,883|
| |Ogemaw County|     2| 95.252| N/A|    53|  2524.170| N/A|  20,997|
| |Gladwin County|     2| 78.589| N/A|    56|  2200.479| N/A|  25,449|
| |Emmet County|     2| 59.853| N/A|    60|  1795.601| N/A|  33,415|
| |Barry County|     2| 32.494| N/A|   170|  2761.982| N/A|  61,550|
| |Mecosta County|     2| 46.027| N/A|    62|  1426.829| N/A|  43,453|
| |Presque Isle County|     2| 158.831| N/A|    20|  1588.310| N/A|  12,592|
| |Cheboygan County|     2| 79.126| N/A|    41|  1622.092| N/A|  25,276|
| |Dickinson County|     2| 79.242| N/A|    48|  1901.819| N/A|  25,239|
| |Branch County|     2| 45.959| N/A|   348|  7996.875| N/A|  43,517|
| |Charlevoix County|     2| 76.502| N/A|    45|  1721.302| N/A|  26,143|
| |Oscoda County|     1| 121.344| N/A|    24|  2912.268| N/A|   8,241|
| |Montcalm County|     1| 15.652| N/A|   181|  2833.083| N/A|  63,888|
| |Missaukee County|     1| 66.146| N/A|    41|  2711.999| N/A|  15,118|
| |Benzie County|     1| 56.287| N/A|    29|  1632.331| N/A|  17,766|
| |Alcona County|     1| 96.108| N/A|    28|  2691.014| N/A|  10,405|
| |Iron County|     1| 90.367| N/A|    17|  1536.237| N/A|  11,066|
| |Gogebic County|     1| 71.556| N/A|   105|  7513.417| N/A|  13,975|
| |Schoolcraft County|     0|  0.000| N/A|    13|  1606.128| N/A|   8,094|
| |Alger County|     0|  0.000| N/A|     8|   878.349| N/A|   9,108|
| |Antrim County|     0|  0.000| N/A|    40|  1714.972| N/A|  23,324|
| |Baraga County|     0|  0.000| N/A|     5|   609.088| N/A|   8,209|
| |Mackinac County|     0|  0.000| N/A|    25|  2315.029| N/A|  10,799|
| |Roscommon County|     0|  0.000| N/A|    51|  2123.319| N/A|  24,019|
| |Osceola County|     0|  0.000| N/A|    70|  2983.802| N/A|  23,460|
| |Ontonagon County|     0|  0.000| N/A|     7|  1223.776| N/A|   5,720|
| |Newaygo County|     0|  0.000| N/A|   249|  5083.708| N/A|  48,980|
| |Montmorency County|     0|  0.000| N/A|     8|   857.633| N/A|   9,328|
| |Menominee County|     0|  0.000| N/A|   111|  4872.695| N/A|  22,780|
| |Mason County|     0|  0.000| N/A|    99|  3396.926| N/A|  29,144|
| |Manistee County|     0|  0.000| N/A|    34|  1384.478| N/A|  24,558|
| |Luce County|     0|  0.000| N/A|     3|   481.618| N/A|   6,229|
| |Leelanau County|     0|  0.000| N/A|    67|  3078.903| N/A|  21,761|
| |Lake County|     0|  0.000| N/A|    19|  1602.970| N/A|  11,853|
| |Keweenaw County|     0|  0.000| N/A|     3|  1417.769| N/A|   2,116|
| |Houghton County|     0|  0.000| N/A|    49|  1373.164| N/A|  35,684|
| |Chippewa County|     0|  0.000| N/A|    36|   963.881| N/A|  37,349|


### Connecticut ###

![Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Connecticut.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CT|8 counties| 4,437| 1244.500| N/A|49,971| 14015.982| N/A|3,565,287|
| |Hartford County| 1,412| 1583.457|  0.000|12,733| 14279.146| 18.322| 891,720|
| |Fairfield County| 1,408| 1492.582|  0.333|17,912| 18988.013| 38.163| 943,332|
| |New Haven County| 1,104| 1291.595|  0.000|13,118| 15347.052| 23.405| 854,757|
| |Middlesex County|   191| 1175.848|  0.000| 1,396|  8594.154| 31.316| 162,436|
| |Litchfield County|   138| 765.251|  0.000| 1,606|  8905.747| 33.272| 180,333|
| |New London County|   103| 388.377|  0.000| 1,428|  5384.494| 26.395| 265,206|
| |Tolland County|    66| 437.895|  0.000| 1,056|  7006.323| 19.904| 150,721|
| |Windham County|    15| 128.444|  0.000|   722|  6182.460| 43.171| 116,782|


### Louisiana ###

![Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Louisiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|LA|64 counties| 3,978| 855.706| N/A|125,726| 27044.864| N/A|4,648,794|
| |Orleans Parish|   560| 1435.367|  0.000|10,526| 26979.782| 125.211| 390,144|
| |Jefferson Parish|   520| 1202.332|  2.312|14,914| 34483.795| 347.419| 432,493|
| |East Baton Rouge Parish|   332| 754.444|  2.272|11,590| 26337.377| 213.608| 440,059|
| |Caddo Parish|   286| 1190.655|  8.701| 6,516| 27126.942| 402.559| 240,204|
| |St. Tammany Parish|   208| 798.713|  7.044| 4,939| 18965.590| 241.322| 260,419|
| |Calcasieu Parish|   127| 624.275|  0.000| 6,641| 32644.173| 280.186| 203,436|
| |Rapides Parish|   111| 856.164| 18.512| 3,155| 24335.123| 239.109| 129,648|
| |Ouachita Parish|   107| 698.073|  5.361| 4,644| 30297.692| 228.342| 153,279|
| |Lafourche Parish|    96| 983.465|  0.000| 2,684| 27496.056| 437.262|  97,614|
| |Lafayette Parish|    89| 364.172|  4.138| 7,344| 30050.329| 298.703| 244,390|
| |St. John the Baptist Parish|    89| 2077.643|  9.710| 1,386| 32355.207| 163.410|  42,837|
| |St. Landry Parish|    81| 986.313| 32.213| 2,556| 31123.667| 523.598|  82,124|
| |Terrebonne Parish|    80| 724.238|  7.435| 2,899| 26244.557| 172.006| 110,461|
| |Acadia Parish|    77| 1241.035| 40.293| 2,536| 40873.560| 820.363|  62,045|
| |Bossier Parish|    75| 590.370|  7.970| 2,275| 17907.887| 529.233| 127,039|
| |Ascension Parish|    71| 560.804|  3.717| 2,725| 21523.807| 314.906| 126,604|
| |Tangipahoa Parish|    69| 512.029| 18.900| 3,291| 24421.556| 163.256| 134,758|
| |Iberia Parish|    69| 988.114| 28.536| 2,412| 34541.028| 415.294|  69,830|
| |Washington Parish|    58| 1255.574|  0.000| 1,220| 26410.356| 194.830|  46,194|
| |St. Mary Parish|    51| 1033.477| 16.859| 1,511| 30619.275| 594.875|  49,348|
| |St. Charles Parish|    50| 941.620|  0.000| 1,419| 26723.164| 374.025|  53,100|
| |Livingston Parish|    49| 348.039|  0.000| 2,754| 19561.187| 142.057| 140,789|
| |Iberville Parish|    47| 1445.665|  0.000| 1,184| 36418.443| 430.623|  32,511|
| |St. Martin Parish|    43| 804.776|  7.747| 1,590| 29758.006| 336.883|  53,431|
| |West Baton Rouge Parish|    36| 1360.287|  0.000|   678| 25618.742| 226.715|  26,465|
| |East Feliciana Parish|    35| 1829.109|  0.000|   542| 28325.059| 209.041|  19,135|
| |Union Parish|    33| 1492.672|  0.000|   652| 29491.587| 271.395|  22,108|
| |Pointe Coupee Parish|    32| 1472.618|  0.000|   762| 35066.728| 539.090|  21,730|
| |St. James Parish|    32| 1516.875| 22.209|   674| 31949.185| 531.159|  21,096|
| |Bienville Parish|    30| 2265.690|  0.000|   359| 27112.756| 197.218|  13,241|
| |Avoyelles Parish|    29| 722.399| 20.781|   987| 24586.489| 298.924|  40,144|
| |De Soto Parish|    26| 946.728| 72.825|   696| 25343.189| 254.888|  27,463|
| |Allen Parish|    26| 1014.555| 49.568| 1,219| 47567.019| 1521.832|  25,627|
| |Lincoln Parish|    24| 513.457|  0.000|   744| 15917.162| 232.476|  46,742|
| |St. Bernard Parish|    24| 508.001| 21.167| 1,067| 22584.879| 190.500|  47,244|
| |Jefferson Davis Parish|    24| 765.111|  0.000|   983| 31337.669| 286.917|  31,368|
| |Vernon Parish|    23| 484.935|  8.816|   733| 15454.680| 328.122|  47,429|
| |Assumption Parish|    20| 913.617|  7.166|   561| 25626.970| 136.935|  21,891|
| |Vermilion Parish|    20| 336.072|  0.000| 1,493| 25087.799| 890.592|  59,511|
| |Plaquemines Parish|    19| 819.071|  0.000|   430| 18536.880| 86.218|  23,197|
| |Jackson Parish|    18| 1143.293|  0.000|   366| 23246.951| 127.033|  15,744|
| |Franklin Parish|    17| 849.363|  0.000|   860| 42967.774| 579.387|  20,015|
| |Beauregard Parish|    17| 453.370|  0.000|   800| 21335.040| 146.678|  37,497|
| |Natchitoches Parish|    17| 445.516|  0.000|   737| 19314.429| 104.827|  38,158|
| |West Feliciana Parish|    16| 1027.749|  0.000|   332| 21325.797| 128.469|  15,568|
| |Grant Parish|    14| 625.307| 93.895|   288| 12863.460| 89.330|  22,389|
| |Webster Parish|    13| 339.071|  0.000|   855| 22300.469| 330.759|  38,340|
| |Red River Parish|    11| 1303.009|  0.000|   209| 24757.167| 996.289|   8,442|
| |Morehouse Parish|    11| 442.229|  0.000|   467| 18774.624| 405.129|  24,874|
| |Claiborne Parish|    11| 701.978|  0.000|   237| 15124.442| 425.071|  15,670|
| |Sabine Parish|    10| 418.690|  8.945|   605| 25330.765| 41.869|  23,884|
| |Concordia Parish|     8| 415.390| N/A|   298| 15473.285| N/A|  19,259|
| |Winn Parish|     7| 503.452| N/A|   401| 28840.621| N/A|  13,904|
| |Richland Parish|     6| 298.181| N/A|   560| 27830.236| N/A|  20,122|
| |Madison Parish|     6| 547.895| N/A|   596| 54424.253| N/A|  10,951|
| |Catahoula Parish|     5| 526.648| N/A|   273| 28755.003| N/A|   9,494|
| |West Carroll Parish|     5| 461.681| N/A|   275| 25392.428| N/A|  10,830|
| |LaSalle Parish|     2| 134.300| N/A|   259| 17391.888| N/A|  14,892|
| |Caldwell Parish|     2| 201.654| N/A|   203| 20467.836| N/A|   9,918|
| |Evangeline Parish|     2| 59.889| N/A|   817| 24464.740| N/A|  33,395|
| |East Carroll Parish|     1| 145.751| N/A|   511| 74478.939| N/A|   6,861|
| |St. Helena Parish|     1| 98.697| N/A|   251| 24772.996| N/A|  10,132|
| |Tensas Parish|     0|  0.000| N/A|    68| 15689.894| N/A|   4,334|
| |Cameron Parish|     0|  0.000| N/A|   167| 23949.520| N/A|   6,973|


### Arizona ###

![Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arizona.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AZ|15 counties| 3,931| 540.068| N/A|182,203| 25032.296| N/A|7,278,717|
| |Maricopa County| 2,204| 491.370|  8.973|123,082| 27440.499| 151.825|4,485,414|
| |Pima County|   469| 447.827|  0.000|16,964| 16198.167| 82.118|1,047,279|
| |Yuma County|   276| 1291.005| 28.410|11,314| 52921.833| 285.331| 213,787|
| |Navajo County|   197| 1775.991| 34.154| 5,309| 47861.599| 113.393| 110,924|
| |Mohave County|   161| 758.786| 15.787| 3,073| 14482.918| 75.052| 212,181|
| |Pinal County|   145| 313.318|  0.000| 8,297| 17928.257|  0.000| 462,789|
| |Apache County|   137| 1905.769| 13.911| 3,119| 43387.539| 278.214|  71,887|
| |Coconino County|   117| 815.467|  3.545| 3,033| 21139.424| 116.193| 143,476|
| |Yavapai County|    65| 276.479|  4.254| 1,904|  8098.716| 170.141| 235,099|
| |Cochise County|    52| 412.954|  7.870| 1,560| 12388.622| 61.766| 125,922|
| |Santa Cruz County|    51| 1096.821|  8.910| 2,633| 56626.091| 213.065|  46,498|
| |Gila County|    34| 629.420|  0.000|   871| 16124.255| 254.711|  54,018|
| |Graham County|    12| 308.984| 25.749|   511| 13157.556| 229.634|  38,837|
| |La Paz County|    10| 473.754|  0.000|   476| 22550.692| 47.951|  21,108|
| |Greenlee County|     1| 105.285| N/A|    57|  6001.263| N/A|   9,498|


### Georgia ###

![Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Georgia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|GA|159 counties| 3,889| 366.285| N/A|183,850| 17315.878| N/A|10,617,423|
| |Fulton County|   407| 382.541|  3.400|18,996| 17854.441| 316.574|1,063,937|
| |Cobb County|   310| 407.819|  0.000|12,489| 16429.847| 387.649| 760,141|
| |Gwinnett County|   241| 257.410|  0.000|18,550| 19813.084| 304.814| 936,250|
| |DeKalb County|   231| 304.229|  2.634|12,998| 17118.466| 168.577| 759,297|
| |Dougherty County|   169| 1921.415|  1.763| 2,652| 30151.439| 184.592|  87,956|
| |Clayton County|   102| 349.009|  1.453| 4,716| 16136.538| 248.120| 292,256|
| |Muscogee County|    89| 454.617| 30.648| 4,455| 22756.412| 236.873| 195,769|
| |Richmond County|    87| 429.591|  8.227| 3,921| 19361.242| 332.799| 202,518|
| |Hall County|    86| 420.659| 14.454| 5,759| 28169.496| 396.757| 204,441|
| |Chatham County|    73| 252.220|  0.000| 5,360| 18519.158| 496.299| 289,430|
| |Troup County|    66| 943.909| 17.880| 2,213| 31649.552| 241.230|  69,922|
| |Bibb County|    65| 424.396|  0.000| 3,353| 21892.282| 447.256| 153,159|
| |Bartow County|    61| 566.188|  0.000| 1,735| 16103.882| 396.022| 107,738|
| |Cherokee County|    57| 220.270|  1.636| 3,085| 11921.646| 343.790| 258,773|
| |Sumter County|    56| 1896.762|  0.000|   741| 25098.225| 145.775|  29,524|
| |Houston County|    50| 316.730|  0.000| 1,847| 11700.018| 143.563| 157,863|
| |Douglas County|    50| 341.663|  2.919| 2,464| 16837.157| 454.412| 146,343|
| |Habersham County|    48| 1058.948|  0.000| 1,089| 24024.885| 242.676|  45,328|
| |Carroll County|    47| 391.693|  0.000| 1,779| 14825.988| 105.401| 119,992|
| |Upson County|    46| 1747.720|  0.000|   494| 18768.997| 119.269|  26,320|
| |Henry County|    44| 187.584|  0.000| 3,138| 13378.183| 235.414| 234,561|
| |Glynn County|    42| 492.426| 46.898| 2,392| 28044.834| 341.308|  85,292|
| |Mitchell County|    41| 1875.314|  0.000|   633| 28953.026| 200.930|  21,863|
| |Spalding County|    40| 599.673|  0.000|   884| 13252.777| 119.935|  66,703|
| |Thomas County|    40| 899.867| 10.575| 1,035| 23284.066| 346.220|  44,451|
| |Baldwin County|    38| 846.514|  0.000|   988| 22009.356| 178.213|  44,890|
| |Newton County|    37| 331.114|  7.501| 1,688| 15105.956| 294.462| 111,744|
| |Walton County|    37| 391.149| 21.143| 1,020| 10783.039| 251.190|  94,593|
| |Butts County|    37| 1483.799|  0.000|   469| 18808.149| 57.073|  24,936|
| |Tift County|    35| 861.136|  0.000| 1,287| 31665.190| 402.910|  40,644|
| |Hancock County|    34| 4020.338|  0.000|   294| 34764.101| 472.981|   8,457|
| |Lowndes County|    34| 289.593|  7.003| 3,032| 25824.915| 212.936| 117,406|
| |Barrow County|    32| 384.431|  0.000| 1,180| 14175.877| 291.377|  83,240|
| |Early County|    31| 3042.198|  0.000|   352| 34543.670| 294.406|  10,190|
| |Terrell County|    30| 3516.587|  0.000|   296| 34696.987| 196.473|   8,531|
| |Whitfield County|    28| 267.615|  5.065| 3,313| 31664.564| 387.372| 104,628|
| |Randolph County|    26| 3835.940|  0.000|   266| 39244.615| 356.188|   6,778|
| |Fayette County|    25| 218.491|  0.000| 1,028|  8984.365| 190.629| 114,421|
| |Monroe County|    25| 906.520| 72.522|   440| 15954.747| 217.565|  27,578|
| |Coffee County|    25| 577.727|  0.000| 1,394| 32214.083| 476.812|  43,273|
| |Jenkins County|    24| 2766.252| 101.876|   235| 27086.215| 239.383|   8,676|
| |Ware County|    24| 671.629|  0.000| 1,097| 30699.054| 189.453|  35,734|
| |Worth County|    23| 1135.971|  0.000|   436| 21534.054| 210.721|  20,247|
| |Gordon County|    23| 396.805|  0.000| 1,083| 18684.333| 447.420|  57,963|
| |Coweta County|    22| 148.139|  2.876| 1,404|  9453.972| 149.992| 148,509|
| |Colquitt County|    22| 482.456|  0.000| 1,519| 33311.404| 284.179|  45,600|
| |Forsyth County|    22| 90.071|  3.498| 2,035|  8331.559| 168.549| 244,252|
| |Lee County|    22| 733.529|  0.000|   526| 17538.010| 109.877|  29,992|
| |Columbia County|    21| 134.002|  5.451| 2,050| 13081.154| 268.004| 156,714|
| |Paulding County|    21| 124.506| 11.858| 1,538|  9118.559| 226.095| 168,667|
| |Appling County|    19| 1033.395| 83.211|   615| 33449.364| 435.114|  18,386|
| |Turner County|    18| 2254.227|  0.000|   237| 29680.651| 611.189|   7,985|
| |Wilcox County|    18| 2084.540|  0.000|   173| 20034.742| 309.841|   8,635|
| |Clarke County|    17| 132.470|  0.000| 1,863| 14517.147| 424.162| 128,331|
| |Brooks County|    17| 1099.825|  0.000|   387| 25037.200| 194.087|  15,457|
| |Putnam County|    17| 768.570|  0.000|   393| 17767.530| 135.630|  22,119|
| |Floyd County|    16| 162.440|  0.000| 1,353| 13736.320| 327.389|  98,498|
| |Walker County|    16| 229.355|  0.000|   617|  8844.483| 43.004|  69,761|
| |Harris County|    16| 454.081|  0.000|   628| 17822.681| 65.906|  35,236|
| |Rockdale County|    16| 176.025|  0.000| 1,221| 13432.934| 215.614|  90,896|
| |Oconee County|    15| 372.393|  0.000|   413| 10253.227| 211.023|  40,280|
| |Crisp County|    14| 625.782|  0.000|   366| 16359.735| 56.280|  22,372|
| |Bulloch County|    14| 175.862| 10.477| 1,137| 14282.484| 138.177|  79,608|
| |Dooly County|    14| 1045.556|  0.000|   244| 18222.554| 61.807|  13,390|
| |Jackson County|    13| 178.138|  0.000| 1,000| 13702.948| 259.014|  72,977|
| |Peach County|    12| 435.635|  0.000|   351| 12742.322| 290.423|  27,546|
| |Johnson County|    11| 1140.724|  0.000|   232| 24058.903| 259.255|   9,643|
| |Stephens County|    11| 424.301| 20.440|   579| 22333.655| 320.923|  25,925|
| |Polk County|    11| 258.137| 21.348|   714| 16755.450| 164.269|  42,613|
| |Greene County|    11| 600.306|  0.000|   283| 15444.226| 713.356|  18,324|
| |McDuffie County|    10| 469.219| 22.057|   306| 14358.108| 219.888|  21,312|
| |Macon County|    10| 772.380|  0.000|   175| 13516.645|  0.000|  12,947|
| |Wilkinson County|    10| 1116.819|  0.000|   199| 22224.704| 335.046|   8,954|
| |Lamar County|    10| 524.191|  0.000|   252| 13209.624| 681.449|  19,077|
| |Decatur County|    10| 378.730| 75.746|   711| 26927.738| 649.785|  26,404|
| |Catoosa County|     9| 133.175| N/A|   587|  8686.002| N/A|  67,580|
| |Screven County|     9| 644.422| N/A|   182| 13031.648| N/A|  13,966|
| |Emanuel County|     8| 353.263| N/A|   450| 19871.059| N/A|  22,646|
| |Bryan County|     8| 201.883| N/A|   601| 15166.427| N/A|  39,627|
| |Jefferson County|     7| 455.670| N/A|   460| 29944.018| N/A|  15,362|
| |Jeff Davis County|     7| 463.116| N/A|   415| 27456.169| N/A|  15,115|
| |Oglethorpe County|     7| 458.746| N/A|   198| 12975.949| N/A|  15,259|
| |Wayne County|     7| 233.902| N/A|   696| 23256.591| N/A|  29,927|
| |Toombs County|     7| 260.902| N/A|   677| 25232.948| N/A|  26,830|
| |Telfair County|     7| 441.362| N/A|   263| 16582.598| N/A|  15,860|
| |Burke County|     7| 312.737| N/A|   427| 19076.978| N/A|  22,383|
| |Lumpkin County|     6| 178.518| N/A|   316|  9401.964| N/A|  33,610|
| |Laurens County|     6| 126.194| N/A|   785| 16510.327| N/A|  47,546|
| |Meriwether County|     6| 283.460| N/A|   367| 17338.310| N/A|  21,167|
| |Pierce County|     6| 308.246| N/A|   386| 19830.465| N/A|  19,465|
| |Union County|     6| 244.788| N/A|   238|  9709.926| N/A|  24,511|
| |Bacon County|     6| 537.442| N/A|   420| 37620.924| N/A|  11,164|
| |Calhoun County|     6| 969.462| N/A|   199| 32153.821| N/A|   6,189|
| |Haralson County|     6| 201.396| N/A|   201|  6746.778| N/A|  29,792|
| |Cook County|     6| 347.423| N/A|   416| 24088.014| N/A|  17,270|
| |Bleckley County|     5| 388.410| N/A|   162| 12584.479| N/A|  12,873|
| |Stewart County|     5| 755.173| N/A|   253| 38211.750| N/A|   6,621|
| |White County|     5| 162.348| N/A|   314| 10195.467| N/A|  30,798|
| |Grady County|     5| 202.980| N/A|   439| 17821.621| N/A|  24,633|
| |Madison County|     5| 167.336| N/A|   368| 12315.930| N/A|  29,880|
| |Pickens County|     5| 153.417| N/A|   335| 10278.911| N/A|  32,591|
| |Franklin County|     5| 214.142| N/A|   385| 16488.929| N/A|  23,349|
| |Camden County|     4| 73.172| N/A|   708| 12951.377| N/A|  54,666|
| |Gilmer County|     4| 127.514| N/A|   553| 17628.869| N/A|  31,369|
| |Brantley County|     4| 209.325| N/A|   237| 12402.533| N/A|  19,109|
| |Candler County|     4| 370.268| N/A|   233| 21568.083| N/A|  10,803|
| |Clinch County|     4| 604.412| N/A|   180| 27198.549| N/A|   6,618|
| |Marion County|     4| 478.526| N/A|   145| 17346.573| N/A|   8,359|
| |Pike County|     4| 210.948| N/A|   198| 10441.937| N/A|  18,962|
| |Seminole County|     4| 494.438| N/A|   170| 21013.597| N/A|   8,090|
| |Heard County|     4| 335.486| N/A|   136| 11406.525| N/A|  11,923|
| |Hart County|     4| 152.643| N/A|   277| 10570.502| N/A|  26,205|
| |Lanier County|     4| 383.767| N/A|   210| 20147.750| N/A|  10,423|
| |Lincoln County|     4| 504.987| N/A|   130| 16412.069| N/A|   7,921|
| |Dawson County|     3| 114.907| N/A|   329| 12601.501| N/A|  26,108|
| |Liberty County|     3| 48.832| N/A|   659| 10726.784| N/A|  61,435|
| |Fannin County|     3| 114.556| N/A|   300| 11455.629| N/A|  26,188|
| |Jones County|     3| 104.402| N/A|   282|  9813.816| N/A|  28,735|
| |Dodge County|     3| 145.596| N/A|   200|  9706.382| N/A|  20,605|
| |Charlton County|     3| 224.014| N/A|   401| 29943.250| N/A|  13,392|
| |Ben Hill County|     3| 179.641| N/A|   371| 22215.569| N/A|  16,700|
| |Baker County|     3| 987.492| N/A|    62| 20408.163| N/A|   3,038|
| |Banks County|     3| 155.974| N/A|   247| 12841.843| N/A|  19,234|
| |Rabun County|     3| 175.060| N/A|   200| 11670.654| N/A|  17,137|
| |Talbot County|     3| 484.262| N/A|   129| 20823.245| N/A|   6,195|
| |Wilkes County|     3| 306.843| N/A|   182| 18615.117| N/A|   9,777|
| |Treutlen County|     3| 434.720| N/A|   104| 15070.280| N/A|   6,901|
| |Twiggs County|     3| 369.458| N/A|   102| 12561.576| N/A|   8,120|
| |Chattooga County|     2| 80.681| N/A|   212|  8552.180| N/A|  24,789|
| |Washington County|     2| 98.164| N/A|   449| 22037.891| N/A|  20,374|
| |McIntosh County|     2| 139.101| N/A|   164| 11406.315| N/A|  14,378|
| |Webster County|     2| 767.165| N/A|    39| 14959.724| N/A|   2,607|
| |Atkinson County|     2| 244.948| N/A|   301| 36864.666| N/A|   8,165|
| |Taylor County|     2| 249.377| N/A|    78|  9725.686| N/A|   8,020|
| |Clay County|     2| 705.716| N/A|    85| 29992.943| N/A|   2,834|
| |Murray County|     2| 49.880| N/A|   556| 13866.720| N/A|  40,096|
| |Pulaski County|     2| 179.582| N/A|    90|  8081.171| N/A|  11,137|
| |Echols County|     2| 499.251| N/A|   216| 53919.121| N/A|   4,006|
| |Montgomery County|     1| 109.027| N/A|   143| 15590.929| N/A|   9,172|
| |Quitman County|     1| 434.972| N/A|    29| 12614.180| N/A|   2,299|
| |Warren County|     1| 190.331| N/A|    60| 11419.871| N/A|   5,254|
| |Long County|     1| 51.127| N/A|   114|  5828.519| N/A|  19,559|
| |Wheeler County|     1| 127.307| N/A|    85| 10821.133| N/A|   7,855|
| |Towns County|     1| 83.077| N/A|   120|  9969.261| N/A|  12,037|
| |Tattnall County|     1| 39.548| N/A|   458| 18112.790| N/A|  25,286|
| |Schley County|     1| 190.223| N/A|    56| 10652.463| N/A|   5,257|
| |Evans County|     1| 93.861| N/A|   236| 22151.305| N/A|  10,654|
| |Elbert County|     1| 52.100| N/A|   334| 17401.271| N/A|  19,194|
| |Effingham County|     1| 15.553| N/A|   672| 10451.661| N/A|  64,296|
| |Dade County|     1| 62.050| N/A|   119|  7383.966| N/A|  16,116|
| |Chattahoochee County|     1| 91.684| N/A|   696| 63812.231| N/A|  10,907|
| |Irwin County|     1| 106.202| N/A|   157| 16673.747| N/A|   9,416|
| |Jasper County|     1| 70.328| N/A|   135|  9494.339| N/A|  14,219|
| |Taliaferro County|     0|  0.000| N/A|    12|  7807.417| N/A|   1,537|
| |Morgan County|     0|  0.000| N/A|   236| 12243.204| N/A|  19,276|
| |Miller County|     0|  0.000| N/A|   132| 23084.995| N/A|   5,718|
| |Glascock County|     0|  0.000| N/A|    24|  8078.088| N/A|   2,971|
| |Crawford County|     0|  0.000| N/A|    98|  7900.677| N/A|  12,404|
| |Berrien County|     0|  0.000| N/A|   262| 13507.243| N/A|  19,397|


### Ohio ###

![Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Ohio.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OH|88 counties| 3,596| 307.637| N/A|96,305|  8238.872| N/A|11,689,100|
| |Franklin County|   517| 392.632|  0.956|17,619| 13380.611| 133.951|1,316,756|
| |Cuyahoga County|   487| 394.309|  0.000|13,011| 10534.609| 104.447|1,235,072|
| |Lucas County|   320| 747.056|  2.021| 5,114| 11938.891| 200.870| 428,348|
| |Mahoning County|   253| 1106.335|  0.000| 2,470| 10800.978| 120.971| 228,683|
| |Hamilton County|   249| 304.597|  1.223| 9,297| 11372.853| 80.249| 817,473|
| |Summit County|   218| 402.948|  0.000| 3,399|  6282.659| 95.368| 541,013|
| |Stark County|   137| 369.665|  5.695| 1,756|  4738.186| 81.044| 370,606|
| |Trumbull County|   105| 530.373|  4.315| 1,465|  7399.962| 73.697| 197,974|
| |Montgomery County|    85| 159.868|  5.794| 4,114|  7737.635| 53.603| 531,687|
| |Lorain County|    77| 248.521|  0.000| 1,665|  5373.863| 49.317| 309,833|
| |Butler County|    61| 159.213|  2.610| 2,778|  7250.727| 80.912| 383,134|
| |Portage County|    60| 369.308|  0.000|   734|  4517.868| 49.856| 162,466|
| |Columbiana County|    60| 588.911|  0.000| 1,607| 15772.995| 121.968| 101,883|
| |Wayne County|    58| 501.253|  0.000|   517|  4468.067| 77.781| 115,710|
| |Wood County|    58| 443.367|  0.000|   973|  7437.871| 174.125| 130,817|
| |Licking County|    47| 265.744|  5.654| 1,179|  6666.214| 118.737| 176,862|
| |Ashtabula County|    45| 462.768|  0.000|   551|  5666.334| 53.178|  97,241|
| |Marion County|    45| 691.319| 15.363| 2,901| 44567.004| 131.778|  65,093|
| |Geauga County|    44| 469.840|  5.020|   540|  5766.212| 45.442|  93,649|
| |Allen County|    42| 410.353|  0.000|   682|  6663.345| 127.058| 102,351|
| |Pickaway County|    42| 718.477|  0.000| 2,374| 40611.047| 132.073|  58,457|
| |Lake County|    37| 160.765|  2.505| 1,064|  4623.092| 44.625| 230,149|
| |Miami County|    37| 345.836|  0.000|   788|  7365.381| 68.476| 106,987|
| |Medina County|    35| 194.719|  5.896|   869|  4834.600| 94.578| 179,746|
| |Warren County|    35| 149.189|  0.000| 1,689|  7199.427| 121.375| 234,602|
| |Fairfield County|    29| 184.041| 12.692| 1,285|  8154.899| 100.455| 157,574|
| |Erie County|    27| 363.558|  0.000|   546|  7351.951| 135.218|  74,266|
| |Darke County|    27| 528.241|  0.000|   348|  6808.444| 256.512|  51,113|
| |Belmont County|    26| 388.025|  0.000|   591|  8820.106| 12.661|  67,006|
| |Ottawa County|    25| 616.903|  0.000|   365|  9006.786| 105.917|  40,525|
| |Washington County|    22| 367.211|  0.000|   198|  3304.902|  7.195|  59,911|
| |Monroe County|    18| 1318.295|  0.000|    91|  6664.714|  0.000|  13,654|
| |Delaware County|    18| 86.052|  0.000| 1,241|  5932.775| 83.661| 209,177|
| |Putnam County|    17| 502.053|  0.000|   198|  5847.435| 43.804|  33,861|
| |Sandusky County|    16| 273.420|  0.000|   354|  6049.421| 164.072|  58,518|
| |Tuscarawas County|    14| 152.195|  5.110|   759|  8251.166| 54.598|  91,987|
| |Clark County|    14| 104.413|  3.506| 1,104|  8233.706| 68.067| 134,083|
| |Mercer County|    13| 315.749|  0.000|   561| 13625.765| 315.749|  41,172|
| |Hardin County|    12| 382.592|  0.000|   158|  5037.462| 105.724|  31,365|
| |Clermont County|    11| 53.287|  0.760|   874|  4233.922| 72.665| 206,428|
| |Greene County|    11| 65.113|  0.000|   644|  3812.072| 51.559| 168,937|
| |Richland County|    11| 90.794|  0.000|   559|  4613.962| 70.746| 121,154|
| |Madison County|    10| 223.559|  0.000|   343|  7668.060| 107.805|  44,731|
| |Hocking County|     9| 318.426| N/A|   114|  4033.399| N/A|  28,264|
| |Wyandot County|     7| 321.514| N/A|   128|  5879.111| N/A|  21,772|
| |Guernsey County|     7| 180.064| N/A|   113|  2906.752| N/A|  38,875|
| |Knox County|     7| 112.320| N/A|   189|  3032.637| N/A|  62,322|
| |Coshocton County|     6| 163.934| N/A|   186|  5081.967| N/A|  36,600|
| |Clinton County|     6| 142.966| N/A|   154|  3669.462| N/A|  41,968|
| |Holmes County|     6| 136.488| N/A|   326|  7415.833| N/A|  43,960|
| |Huron County|     5| 85.813| N/A|   383|  6573.302| N/A|  58,266|
| |Auglaize County|     5| 109.515| N/A|   233|  5103.382| N/A|  45,656|
| |Crawford County|     5| 120.499| N/A|   168|  4048.778| N/A|  41,494|
| |Carroll County|     5| 185.777| N/A|   110|  4087.092| N/A|  26,914|
| |Shelby County|     4| 82.321| N/A|   168|  3457.502| N/A|  48,590|
| |Ross County|     4| 52.174| N/A|   431|  5621.788| N/A|  76,666|
| |Defiance County|     4| 105.023| N/A|   133|  3492.005| N/A|  38,087|
| |Perry County|     3| 83.024| N/A|   113|  3127.249| N/A|  36,134|
| |Williams County|     3| 81.762| N/A|   129|  3515.753| N/A|  36,692|
| |Ashland County|     3| 56.092| N/A|   135|  2524.119| N/A|  53,484|
| |Seneca County|     3| 54.369| N/A|   177|  3207.800| N/A|  55,178|
| |Hancock County|     3| 39.587| N/A|   344|  4539.277| N/A|  75,783|
| |Morrow County|     2| 56.612| N/A|   163|  4613.904| N/A|  35,328|
| |Champaign County|     2| 51.434| N/A|   151|  3883.245| N/A|  38,885|
| |Logan County|     2| 43.791| N/A|   136|  2977.754| N/A|  45,672|
| |Vinton County|     2| 152.847| N/A|    30|  2292.702| N/A|  13,085|
| |Preble County|     2| 48.921| N/A|   175|  4280.612| N/A|  40,882|
| |Jefferson County|     2| 30.616| N/A|   212|  3245.312| N/A|  65,325|
| |Adams County|     2| 72.207| N/A|    59|  2130.118| N/A|  27,698|
| |Henry County|     2| 74.058| N/A|   110|  4073.169| N/A|  27,006|
| |Union County|     1| 16.953| N/A|   228|  3865.193| N/A|  58,988|
| |Van Wert County|     1| 35.367| N/A|    70|  2475.685| N/A|  28,275|
| |Harrison County|     1| 66.489| N/A|    22|  1462.766| N/A|  15,040|
| |Athens County|     1| 15.308| N/A|   352|  5388.277| N/A|  65,327|
| |Brown County|     1| 23.024| N/A|   120|  2762.940| N/A|  43,432|
| |Scioto County|     1| 13.278| N/A|   204|  2708.660| N/A|  75,314|
| |Highland County|     1| 23.169| N/A|   141|  3266.838| N/A|  43,161|
| |Muskingum County|     1| 11.599| N/A|   207|  2400.974| N/A|  86,215|
| |Fulton County|     1| 23.738| N/A|   143|  3394.578| N/A|  42,126|
| |Gallia County|     1| 33.447| N/A|    62|  2073.717| N/A|  29,898|
| |Jackson County|     0|  0.000| N/A|    70|  2159.627| N/A|  32,413|
| |Fayette County|     0|  0.000| N/A|   104|  3645.925| N/A|  28,525|
| |Lawrence County|     0|  0.000| N/A|   234|  3935.220| N/A|  59,463|
| |Meigs County|     0|  0.000| N/A|    29|  1265.989| N/A|  22,907|
| |Pike County|     0|  0.000| N/A|    73|  2628.547| N/A|  27,772|
| |Paulding County|     0|  0.000| N/A|    64|  3427.592| N/A|  18,672|
| |Noble County|     0|  0.000| N/A|    16|  1109.262| N/A|  14,424|
| |Morgan County|     0|  0.000| N/A|    21|  1447.477| N/A|  14,508|


### Maryland ###

![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maryland.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MD|24 counties| 3,526| 583.226| N/A|92,426| 15287.941| N/A|6,045,680|
| |Baltimore County|   976| 1179.642|  7.252|24,619| 29755.732| 479.834| 827,370|
| |Montgomery County|   794| 755.695|  0.708|17,976| 17108.790| 72.334|1,050,688|
| |Prince George's County|   746| 820.387|  1.419|23,156| 25464.987| 152.147| 909,327|
| |Anne Arundel County|   220| 379.812|  2.144| 7,114| 12281.738| 92.363| 579,234|
| |Frederick County|   121| 466.197|  0.000| 3,020| 11635.658| 23.770| 259,547|
| |Carroll County|   117| 694.580|  0.931| 1,511|  8970.181| 59.481| 168,447|
| |Howard County|   106| 325.463|  0.000| 3,717| 11412.693| 91.992| 325,690|
| |Charles County|    91| 557.403|  0.000| 1,947| 11925.982| 128.086| 163,257|
| |Harford County|    69| 270.121|  1.628| 1,878|  7351.991| 66.476| 255,441|
| |St. Mary's County|    52| 458.109|  0.000|   945|  8325.258| 61.669| 113,510|
| |Wicomico County|    44| 424.674|  0.000| 1,316| 12701.599| 70.378| 103,609|
| |Washington County|    31| 205.231|  6.620|   989|  6547.544| 23.171| 151,049|
| |Cecil County|    30| 291.673|  0.000|   672|  6533.469| 83.383| 102,855|
| |Calvert County|    28| 302.621|  0.000|   660|  7133.207| 141.447|  92,525|
| |Queen Anne's County|    25| 496.219|  0.000|   402|  7979.199| 29.773|  50,381|
| |Kent County|    23| 1184.224|  0.000|   235| 12099.681|  0.000|  19,422|
| |Worcester County|    20| 382.585| 19.129|   656| 12548.780| 439.972|  52,276|
| |Allegany County|    18| 255.624|  0.000|   276|  3919.564| 22.554|  70,416|
| |Dorchester County|     5| 156.597| N/A|   353| 11055.780| N/A|  31,929|
| |Talbot County|     4| 107.582| N/A|   369|  9924.424| N/A|  37,181|
| |Caroline County|     3| 89.804| N/A|   441| 13201.221| N/A|  33,406|
| |Somerset County|     3| 117.114| N/A|   129|  5035.915| N/A|  25,616|
| |Garrett County|     0|  0.000| N/A|    45|  1550.975| N/A|  29,014|
| |Baltimore city|     0|  0.000| N/A|     0|     0.000| N/A| 593,490|


### Indiana ###

![Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Indiana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IN|92 counties| 2,805| 416.653| N/A|69,975| 10394.047| N/A|6,732,219|
| |Marion County|   724| 750.584|  2.201|15,152| 15708.359| 151.419| 964,582|
| |Lake County|   273| 562.315|  2.354| 7,222| 14875.601| 125.393| 485,493|
| |Allen County|   160| 421.831|  2.606| 3,695|  9741.655| 79.535| 379,299|
| |Johnson County|   118| 746.047|  0.000| 1,674| 10583.750| 69.547| 158,167|
| |Hendricks County|   105| 616.519|  0.000| 1,796| 10545.414| 46.973| 170,311|
| |Hamilton County|   104| 307.682|  0.000| 2,572|  7609.220| 87.275| 338,011|
| |St. Joseph County|    79| 290.627|  0.000| 3,224| 11860.528| 132.386| 271,826|
| |Elkhart County|    79| 382.861|  4.846| 4,680| 22680.902| 179.534| 206,341|
| |Howard County|    65| 787.459|  1.888|   829| 10043.129| 108.383|  82,544|
| |Madison County|    65| 501.663|  0.000|   872|  6730.005| 77.179| 129,569|
| |Delaware County|    52| 455.601|  0.000|   665|  5826.434| 43.808| 114,135|
| |Bartholomew County|    47| 561.000|  0.000|   749|  8940.188| 39.595|  83,779|
| |Clark County|    46| 388.835|  3.516| 1,126|  9518.013| 143.700| 118,302|
| |Boone County|    46| 678.036|  0.000|   649|  9566.204| 92.747|  67,843|
| |Floyd County|    45| 573.088|  5.440|   729|  9284.022| 217.915|  78,522|
| |Porter County|    39| 228.888|  0.000| 1,213|  7119.004| 64.124| 170,389|
| |Hancock County|    38| 486.132|  6.014|   634|  8110.736| 76.758|  78,168|
| |Greene County|    34| 1065.096|  0.000|   240|  7518.326| 18.296|  31,922|
| |Morgan County|    34| 482.345| 28.373|   440|  6242.109| 105.293|  70,489|
| |Decatur County|    32| 1204.865|  0.000|   322| 12123.950| 123.345|  26,559|
| |Warrick County|    30| 476.206|  0.000|   540|  8571.701| 222.229|  62,998|
| |Monroe County|    30| 202.114|  0.000|   699|  4709.259| 39.171| 148,431|
| |Noble County|    29| 607.406|  0.000|   638| 13362.936| 11.055|  47,744|
| |LaPorte County|    29| 263.905|  0.000|   850|  7735.149| 59.123| 109,888|
| |Grant County|    29| 440.937|  0.000|   511|  7769.618| 74.188|  65,769|
| |Dearborn County|    28| 566.137|  0.000|   477|  9644.547| 114.061|  49,458|
| |Shelby County|    27| 603.635|  9.300|   530| 11849.136| 159.196|  44,729|
| |Lawrence County|    27| 595.107|  0.000|   332|  7317.611| 44.346|  45,370|
| |Orange County|    24| 1221.623|  0.000|   164|  8347.755|  0.000|  19,646|
| |Harrison County|    22| 543.009|  0.000|   304|  7503.394| 123.411|  40,515|
| |Marshall County|    22| 475.593|  0.000|   752| 16256.647| 90.178|  46,258|
| |Montgomery County|    21| 547.759|  0.000|   343|  8946.737| 26.084|  38,338|
| |Daviess County|    19| 569.698|  0.000|   251|  7526.011| 77.487|  33,351|
| |Henry County|    19| 396.064|  8.671|   365|  7608.605| 35.384|  47,972|
| |Franklin County|    13| 571.228| 55.325|   231| 10150.277| 150.572|  22,758|
| |Vanderburgh County|    13| 71.645|  0.000| 1,800|  9920.034| 193.743| 181,451|
| |Kosciusko County|    12| 151.027|  0.000|   824| 10370.520| 37.757|  79,456|
| |Jennings County|    12| 432.666|  0.000|   214|  7715.882| 70.745|  27,735|
| |Dubois County|    12| 280.794|  0.000|   655| 15326.657| 283.062|  42,736|
| |Perry County|    12| 626.011|  0.000|   172|  8972.821| 52.168|  19,169|
| |Tippecanoe County|    11| 56.199|  0.000| 1,123|  5737.437| 50.532| 195,732|
| |Newton County|    10| 715.103|  0.000|   114|  8152.174| 131.281|  13,984|
| |White County|    10| 414.903|  0.000|   349| 14480.126| 48.733|  24,102|
| |Scott County|    10| 418.883|  0.000|   252| 10555.858| 55.654|  23,873|
| |LaGrange County|    10| 252.436|  0.000|   549| 13858.737| 75.731|  39,614|
| |Vigo County|    10| 93.425|  0.000|   528|  4932.828| 185.688| 107,038|
| |Wayne County|    10| 151.782|  0.000|   337|  5115.051| 110.902|  65,884|
| |Cass County|     9| 238.796| N/A| 1,760| 46697.976| N/A|  37,689|
| |Putnam County|     8| 212.902| N/A|   234|  6227.379| N/A|  37,576|
| |Ripley County|     7| 247.140| N/A|   194|  6849.315| N/A|  28,324|
| |Starke County|     7| 304.414| N/A|   170|  7392.912| N/A|  22,995|
| |Fayette County|     7| 303.004| N/A|   163|  7055.666| N/A|  23,102|
| |Tipton County|     6| 396.092| N/A|   126|  8317.930| N/A|  15,148|
| |Whitley County|     6| 176.658| N/A|   149|  4386.998| N/A|  33,964|
| |Clay County|     5| 190.658| N/A|   102|  3889.418| N/A|  26,225|
| |Jackson County|     4| 90.434| N/A|   556| 12570.369| N/A|  44,231|
| |DeKalb County|     4| 92.007| N/A|   222|  5106.383| N/A|  43,475|
| |Ohio County|     4| 680.851| N/A|    56|  9531.915| N/A|   5,875|
| |Rush County|     4| 241.240| N/A|    80|  4824.799| N/A|  16,581|
| |Gibson County|     4| 118.839| N/A|   204|  6060.786| N/A|  33,659|
| |Randolph County|     4| 162.173| N/A|   109|  4419.218| N/A|  24,665|
| |Huntington County|     3| 82.147| N/A|   119|  3258.488| N/A|  36,520|
| |Wabash County|     3| 96.787| N/A|   161|  5194.219| N/A|  30,996|
| |Steuben County|     3| 86.720| N/A|   203|  5868.070| N/A|  34,594|
| |Spencer County|     3| 147.951| N/A|   116|  5720.767| N/A|  20,277|
| |Clinton County|     3| 92.595| N/A|   388| 11975.678| N/A|  32,399|
| |Fulton County|     2| 100.130| N/A|   150|  7509.763| N/A|  19,974|
| |Carroll County|     2| 98.731| N/A|   152|  7503.579| N/A|  20,257|
| |Blackford County|     2| 170.097| N/A|    56|  4762.715| N/A|  11,758|
| |Miami County|     2| 56.313| N/A|   260|  7320.644| N/A|  35,516|
| |Jefferson County|     2| 61.904| N/A|   153|  4735.669| N/A|  32,308|
| |Jasper County|     2| 59.591| N/A|   216|  6435.850| N/A|  33,562|
| |Adams County|     2| 55.902| N/A|    84|  2347.877| N/A|  35,777|
| |Fountain County|     2| 122.354| N/A|    64|  3915.331| N/A|  16,346|
| |Wells County|     2| 70.681| N/A|   144|  5089.059| N/A|  28,296|
| |Owen County|     1| 48.079| N/A|    82|  3942.497| N/A|  20,799|
| |Parke County|     1| 59.042| N/A|    49|  2893.074| N/A|  16,937|
| |Brown County|     1| 66.260| N/A|    70|  4638.219| N/A|  15,092|
| |Sullivan County|     1| 48.382| N/A|    83|  4015.676| N/A|  20,669|
| |Warren County|     1| 120.992| N/A|    19|  2298.851| N/A|   8,265|
| |Washington County|     1| 35.668| N/A|   117|  4173.206| N/A|  28,036|
| |Pulaski County|     1| 80.952| N/A|    75|  6071.400| N/A|  12,353|
| |Martin County|     0|  0.000| N/A|    42|  4095.563| N/A|  10,255|
| |Pike County|     0|  0.000| N/A|    50|  4035.838| N/A|  12,389|
| |Posey County|     0|  0.000| N/A|   161|  6331.852| N/A|  25,427|
| |Switzerland County|     0|  0.000| N/A|    43|  3999.628| N/A|  10,751|
| |Vermillion County|     0|  0.000| N/A|    47|  3032.649| N/A|  15,498|
| |Knox County|     0|  0.000| N/A|   140|  3825.764| N/A|  36,594|
| |Jay County|     0|  0.000| N/A|    82|  4012.527| N/A|  20,436|
| |Crawford County|     0|  0.000| N/A|    44|  4159.970| N/A|  10,577|
| |Benton County|     0|  0.000| N/A|    60|  6858.711| N/A|   8,748|
| |Union County|     0|  0.000| N/A|    33|  4678.197| N/A|   7,054|


### Virginia ###

![Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VA|133 counties| 2,274| 266.416| N/A|95,049| 11135.702| N/A|8,535,519|
| |Fairfax County|   537| 467.961|  1.997|16,101| 14030.981| 58.240|1,147,532|
| |Henrico County|   182| 550.151|  0.000| 3,714| 11226.717| 98.240| 330,818|
| |Prince William County|   175| 372.075|  2.109| 9,139| 19430.831| 160.524| 470,335|
| |Arlington County|   135| 570.000|  0.000| 2,997| 12654.006| 105.582| 236,842|
| |Loudoun County|   113| 273.252|  1.017| 5,117| 12373.712| 58.036| 413,538|
| |Chesterfield County|    75| 212.584|  0.000| 4,170| 11819.661| 122.274| 352,802|
| |Alexandria city|    60| 376.345|  2.679| 2,872| 18014.401| 87.814| 159,428|
| |Suffolk city|    49| 531.984|  0.000| 1,167| 12669.909| 286.611|  92,108|
| |Virginia Beach city|    49| 108.895|  1.821| 4,583| 10185.033| 170.152| 449,974|
| |Richmond County|    43| 4765.599|  0.000| 3,351| 371384.240| 2314.957|   9,023|
| |Shenandoah County|    42| 962.949|  0.000|   686| 15728.173| 52.236|  43,616|
| |Spotsylvania County|    35| 256.947|  1.896| 1,390| 10204.456| 129.782| 136,215|
| |Chesapeake city|    33| 134.785|  6.842| 2,714| 11085.016| 219.372| 244,835|
| |Mecklenburg County|    32| 1046.196|  0.000|   329| 10756.204| 57.023|  30,587|
| |Hanover County|    32| 296.940|  0.000|   611|  5669.692| 64.956| 107,766|
| |Harrisonburg city|    30| 565.867|  9.995| 1,069| 20163.724| 132.036|  53,016|
| |Northampton County|    29| 2476.516|  0.000|   295| 25192.143| 59.313|  11,710|
| |Norfolk city|    28| 115.349|  0.000| 3,493| 14389.764| 304.850| 242,742|
| |Portsmouth city|    25| 264.836| 10.593| 1,663| 17616.899| 426.887|  94,398|
| |Galax city|    24| 3781.314| 134.602|   342| 53883.725| 315.110|   6,347|
| |Page County|    24| 1004.100|  0.000|   337| 14099.239| 76.484|  23,902|
| |Colonial Heights city|    21| 1208.981|  0.000|   188| 10823.258| 82.443|  17,370|
| |Manassas city|    20| 486.796|  0.000| 1,620| 39430.449| 92.838|  41,085|
| |Petersburg city|    18| 574.236| 67.422|   488| 15568.175| 239.265|  31,346|
| |Roanoke County|    18| 191.111|  0.000| 1,392| 14779.267| 143.333|  94,186|
| |Newport News city|    18| 100.432|  0.000| 1,734|  9674.990| 176.191| 179,225|
| |Rockingham County|    17| 207.449|  0.000|   920| 11226.632| 85.420|  81,948|
| |Albemarle County|    16| 146.346| 15.424|   791|  7234.977| 155.493| 109,330|
| |James City County|    16| 209.087|  0.000|   573|  7487.945| 87.392|  76,523|
| |Accomack County|    15| 464.166|  0.000| 1,085| 33574.700| 69.902|  32,316|
| |Emporia city|    15| 2805.836|  0.000|   171| 31986.532| 376.715|   5,346|
| |Southampton County|    13| 737.338|  0.000|   247| 14009.415| 185.444|  17,631|
| |Charlottesville city|    13| 275.039|  0.000|   504| 10663.056| 133.926|  47,266|
| |Carroll County|    12| 402.806|  0.000|   305| 10237.991| 100.702|  29,791|
| |Culpeper County|    12| 228.115|  0.000|   964| 18325.254| 74.308|  52,605|
| |Greensville County|    10| 882.145| 13.838|   438| 38637.968|  0.000|  11,336|
| |Prince Edward County|    10| 438.558|  0.000|   386| 16928.340| 219.279|  22,802|
| |Isle of Wight County|     9| 242.529| N/A|   365|  9835.889| N/A|  37,109|
| |Sussex County|     9| 806.524| N/A|   281| 25181.468| N/A|  11,159|
| |Nottoway County|     9| 590.861| N/A|   178| 11685.924| N/A|  15,232|
| |Frederick County|     9| 100.769| N/A|   673|  7535.297| N/A|  89,313|
| |Fauquier County|     9| 126.365| N/A|   588|  8255.876| N/A|  71,222|
| |Stafford County|     8| 52.328| N/A| 1,300|  8503.290| N/A| 152,882|
| |Fluvanna County|     8| 293.363| N/A|   176|  6453.979| N/A|  27,270|
| |Buckingham County|     8| 466.527| N/A|   597| 34814.556| N/A|  17,148|
| |Goochland County|     7| 294.700| N/A|   153|  6441.292| N/A|  23,753|
| |Franklin County|     7| 124.906| N/A|   320|  5710.003| N/A|  56,042|
| |Dinwiddie County|     7| 245.235| N/A|   209|  7322.029| N/A|  28,544|
| |Danville city|     7| 174.808| N/A|   354|  8840.276| N/A|  40,044|
| |Botetourt County|     7| 209.462| N/A|   193|  5775.158| N/A|  33,419|
| |Hampton city|     7| 52.041| N/A| 1,129|  8393.428| N/A| 134,510|
| |Manassas Park city|     7| 400.503| N/A|   505| 28893.466| N/A|  17,478|
| |Bedford County|     7| 88.611| N/A|   321|  4063.445| N/A|  78,997|
| |Warren County|     6| 149.388| N/A|   352|  8764.067| N/A|  40,164|
| |Henry County|     6| 118.678| N/A|   530| 10483.217| N/A|  50,557|
| |Williamsburg city|     6| 401.230| N/A|   119|  7957.737| N/A|  14,954|
| |Hopewell city|     5| 221.936| N/A|   259| 11496.294| N/A|  22,529|
| |Caroline County|     5| 162.734| N/A|   193|  6281.530| N/A|  30,725|
| |Charles City County|     5| 718.081| N/A|    51|  7324.429| N/A|   6,963|
| |Grayson County|     5| 321.543| N/A|   145|  9324.759| N/A|  15,550|
| |Washington County|     5| 93.041| N/A|   191|  3554.150| N/A|  53,740|
| |Falls Church city|     5| 342.067| N/A|    59|  4036.396| N/A|  14,617|
| |Patrick County|     4| 227.169| N/A|   119|  6758.292| N/A|  17,608|
| |York County|     4| 58.582| N/A|   335|  4906.268| N/A|  68,280|
| |Augusta County|     4| 52.939| N/A|   262|  3467.535| N/A|  75,558|
| |Alleghany County|     4| 269.179| N/A|    57|  3835.801| N/A|  14,860|
| |Martinsville city|     4| 318.624| N/A|   179| 14258.404| N/A|  12,554|
| |Powhatan County|     4| 134.898| N/A|   135|  4552.813| N/A|  29,652|
| |Lynchburg city|     4| 48.681| N/A|   503|  6121.605| N/A|  82,168|
| |Winchester city|     4| 142.460| N/A|   396| 14103.569| N/A|  28,078|
| |King George County|     4| 149.054| N/A|   124|  4620.659| N/A|  26,836|
| |Waynesboro city|     3| 132.567| N/A|   167|  7379.585| N/A|  22,630|
| |Pulaski County|     3| 88.165| N/A|    79|  2321.686| N/A|  34,027|
| |Salem city|     3| 118.572| N/A|   144|  5691.475| N/A|  25,301|
| |Montgomery County|     3| 30.446| N/A|   291|  2953.265| N/A|  98,535|
| |Smyth County|     3| 99.655| N/A|   126|  4185.490| N/A|  30,104|
| |Scott County|     3| 139.108| N/A|    63|  2921.265| N/A|  21,566|
| |Wise County|     3| 80.250| N/A|   109|  2915.764| N/A|  37,383|
| |Fredericksburg city|     3| 103.320| N/A|   380| 13087.202| N/A|  29,036|
| |Wythe County|     3| 104.588| N/A|   108|  3765.165| N/A|  28,684|
| |Orange County|     3| 80.969| N/A|   221|  5964.751| N/A|  37,051|
| |Westmoreland County|     3| 166.528| N/A|   197| 10935.332| N/A|  18,015|
| |Russell County|     2| 75.228| N/A|    89|  3347.627| N/A|  26,586|
| |Surry County|     2| 311.429| N/A|    42|  6540.019| N/A|   6,422|
| |Northumberland County|     2| 165.358| N/A|    69|  5704.837| N/A|  12,095|
| |Rappahannock County|     2| 271.370| N/A|    41|  5563.094| N/A|   7,370|
| |King William County|     2| 116.632| N/A|    79|  4606.951| N/A|  17,148|
| |Greene County|     2| 100.913| N/A|   152|  7669.408| N/A|  19,819|
| |Brunswick County|     2| 123.221| N/A|   215| 13246.257| N/A|  16,231|
| |Louisa County|     2| 53.204| N/A|   171|  4548.961| N/A|  37,591|
| |Prince George County|     2| 52.147| N/A|   345|  8995.385| N/A|  38,353|
| |Pittsylvania County|     2| 33.138| N/A|   383|  6345.893| N/A|  60,354|
| |Gloucester County|     2| 53.550| N/A|   147|  3935.954| N/A|  37,348|
| |Campbell County|     2| 36.440| N/A|   168|  3060.946| N/A|  54,885|
| |Middlesex County|     1| 94.500| N/A|    32|  3024.003| N/A|  10,582|
| |Lee County|     1| 42.693| N/A|   104|  4440.080| N/A|  23,423|
| |Amelia County|     1| 76.075| N/A|    74|  5629.517| N/A|  13,145|
| |New Kent County|     1| 43.307| N/A|   121|  5240.137| N/A|  23,091|
| |Lunenburg County|     1| 81.994| N/A|    59|  4837.652| N/A|  12,196|
| |Floyd County|     1| 63.496| N/A|    41|  2603.340| N/A|  15,749|
| |Buena Vista city|     1| 154.369| N/A|    50|  7718.432| N/A|   6,478|
| |King and Queen County|     1| 142.349| N/A|    37|  5266.904| N/A|   7,025|
| |Dickenson County|     1| 69.842| N/A|    33|  2304.791| N/A|  14,318|
| |Halifax County|     1| 29.489| N/A|   145|  4275.899| N/A|  33,911|
| |Essex County|     1| 91.299| N/A|    84|  7669.132| N/A|  10,953|
| |Madison County|     1| 75.409| N/A|    64|  4826.182| N/A|  13,261|
| |Lancaster County|     0|  0.000| N/A|    32|  3018.014| N/A|  10,603|
| |Amherst County|     0|  0.000| N/A|   130|  4113.273| N/A|  31,605|
| |Appomattox County|     0|  0.000| N/A|    75|  4713.720| N/A|  15,911|
| |Bath County|     0|  0.000| N/A|     4|   964.553| N/A|   4,147|
| |Bland County|     0|  0.000| N/A|     8|  1273.885| N/A|   6,280|
| |Staunton city|     0|  0.000| N/A|   144|  5775.710| N/A|  24,932|
| |Charlotte County|     0|  0.000| N/A|    50|  4208.754| N/A|  11,880|
| |Highland County|     0|  0.000| N/A|     4|  1826.484| N/A|   2,190|
| |Buchanan County|     0|  0.000| N/A|    73|  3475.528| N/A|  21,004|
| |Mathews County|     0|  0.000| N/A|    15|  1697.985| N/A|   8,834|
| |Lexington city|     0|  0.000| N/A|    33|  4431.910| N/A|   7,446|
| |Franklin city|     0|  0.000| N/A|     0|     0.000| N/A|   7,967|
| |Fairfax city|     0|  0.000| N/A|     0|     0.000| N/A|  24,019|
| |Covington city|     0|  0.000| N/A|    12|  2166.847| N/A|   5,538|
| |Bristol city|     0|  0.000| N/A|    70|  4176.113| N/A|  16,762|
| |Tazewell County|     0|  0.000| N/A|   103|  2537.258| N/A|  40,595|
| |Richmond city|     0|  0.000| N/A|     0|     0.000| N/A| 230,436|
| |Craig County|     0|  0.000| N/A|    16|  3118.301| N/A|   5,131|
| |Rockbridge County|     0|  0.000| N/A|    66|  2923.847| N/A|  22,573|
| |Cumberland County|     0|  0.000| N/A|    71|  7148.611| N/A|   9,932|
| |Nelson County|     0|  0.000| N/A|    34|  2277.294| N/A|  14,930|
| |Giles County|     0|  0.000| N/A|    23|  1375.598| N/A|  16,720|
| |Radford city|     0|  0.000| N/A|    34|  1863.116| N/A|  18,249|
| |Roanoke city|     0|  0.000| N/A|     0|     0.000| N/A|  99,143|
| |Norton city|     0|  0.000| N/A|    15|  3767.898| N/A|   3,981|
| |Poquoson city|     0|  0.000| N/A|    41|  3341.211| N/A|  12,271|
| |Clarke County|     0|  0.000| N/A|    69|  4719.885| N/A|  14,619|


### North Carolina ###

![North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NC|100 counties| 2,085| 198.797| N/A|129,733| 12369.561| N/A|10,488,084|
| |Mecklenburg County|   222| 199.936|  5.404|21,517| 19378.470| 202.761|1,110,356|
| |Guilford County|   153| 284.824|  4.198| 5,335|  9931.605| 77.073| 537,174|
| |Wake County|   137| 123.228|  1.503|11,425| 10276.489| 79.154|1,111,761|
| |Durham County|    79| 245.732|  0.976| 5,989| 18629.000| 117.876| 321,488|
| |Henderson County|    54| 459.899|  0.000| 1,429| 12170.299| 141.629| 117,417|
| |Chatham County|    51| 684.840| 13.428| 1,261| 16932.993| 113.510|  74,470|
| |Forsyth County|    51| 133.405|  5.232| 5,028| 13152.147| 95.476| 382,295|
| |Robeson County|    51| 390.431|  0.000| 2,714| 20777.033| 176.077| 130,625|
| |Cumberland County|    50| 149.027|  0.000| 2,880|  8583.972| 144.423| 335,509|
| |Cabarrus County|    49| 226.377|  3.366| 2,504| 11568.331|  0.000| 216,453|
| |Rowan County|    48| 337.819|  0.000| 2,072| 14582.512| 140.758| 142,088|
| |Duplin County|    48| 817.146| 38.840| 1,961| 33383.838| 163.609|  58,741|
| |Buncombe County|    46| 176.116|  0.000| 1,757|  6726.878| 80.401| 261,191|
| |Columbus County|    46| 828.709|  0.000|   851| 15331.123| 126.108|  55,508|
| |Orange County|    45| 303.079|  0.000| 1,308|  8809.505| 49.859| 148,476|
| |Johnston County|    44| 210.185|  0.000| 3,135| 14975.709| 120.997| 209,339|
| |Union County|    42| 175.103|  4.169| 2,930| 12215.510| 204.287| 239,859|
| |Gaston County|    41| 182.604|  0.000| 3,124| 13913.570| 97.983| 224,529|
| |Alamance County|    41| 241.875|  0.000| 2,298| 13556.802| 170.845| 169,509|
| |Wayne County|    40| 324.857|  0.000| 2,335| 18963.543| 44.141| 123,131|
| |Vance County|    40| 898.170|  0.000|   746| 16750.870| 100.062|  44,535|
| |Harnett County|    38| 279.461| 14.708| 1,189|  8744.190| 125.022| 135,976|
| |Randolph County|    36| 250.579|  0.000| 2,085| 14512.727| 59.547| 143,667|
| |Wilson County|    35| 427.868|  2.464| 1,447| 17689.270| 452.317|  81,801|
| |Catawba County|    29| 181.760|  0.000| 1,986| 12447.431| 172.944| 159,551|
| |Burke County|    28| 309.444|  0.000| 1,637| 18091.396|  0.000|  90,485|
| |Granville County|    27| 446.702|  8.272| 1,194| 19754.149| 86.234|  60,443|
| |Franklin County|    25| 358.757|  0.000|   811| 11638.086| 116.442|  69,685|
| |Stanly County|    24| 382.129| 48.972|   938| 14934.879| 212.504|  62,806|
| |Moore County|    20| 198.255|  0.000|   947|  9387.391| 188.343| 100,880|
| |New Hanover County|    20| 85.298|  0.664| 2,449| 10444.699|  0.000| 234,473|
| |Iredell County|    18| 99.007|  0.000| 1,771|  9741.153|  0.000| 181,806|
| |Davidson County|    18| 107.393|  0.936| 1,690| 10082.991| 101.706| 167,609|
| |Cleveland County|    17| 173.563|  4.805| 1,097| 11199.935| 287.258|  97,947|
| |Pasquotank County|    17| 426.878|  0.000|   360|  9039.775| 40.011|  39,824|
| |Brunswick County|    17| 119.031|  0.000| 1,213|  8493.208| 55.048| 142,820|
| |Northampton County|    16| 821.229|  0.000|   329| 16886.516| 177.138|  19,483|
| |Montgomery County|    14| 515.217|  0.000|   644| 23699.996|  0.000|  27,173|
| |Caldwell County|    14| 170.362|  0.000| 1,159| 14103.531| 60.844|  82,178|
| |Rutherford County|    14| 208.865|  0.000|   689| 10279.133| 109.997|  67,029|
| |Sampson County|    13| 204.625|  6.724| 1,439| 22650.360| 94.162|  63,531|
| |McDowell County|    13| 284.116| 27.007|   621| 13571.991| 109.275|  45,756|
| |Lenoir County|    12| 214.481|  0.000|   540|  9651.647| 33.023|  55,949|
| |Edgecombe County|    12| 233.136|  0.000|   605| 11753.963| 161.161|  51,472|
| |Nash County|    12| 127.256|  4.985| 1,086| 11516.681| 190.884|  94,298|
| |Hertford County|    11| 464.586|  0.000|   310| 13092.875| 316.763|  23,677|
| |Lee County|    11| 178.054|  6.914| 1,240| 20071.545| 208.174|  61,779|
| |Pitt County|    11| 60.860|  0.000| 1,833| 10141.528| 111.291| 180,742|
| |Craven County|    10| 97.906|  0.000|   673|  6589.060|  0.000| 102,139|
| |Wilkes County|    10| 146.173|  0.000|   744| 10875.285| 53.905|  68,412|
| |Onslow County|    10| 50.521|  0.000|   987|  4986.410| 113.736| 197,938|
| |Surry County|     9| 125.378| N/A|   878| 12231.308| N/A|  71,783|
| |Richmond County|     9| 200.763| N/A|   490| 10930.425| N/A|  44,829|
| |Hoke County|     9| 162.943| N/A|   693| 12546.620| N/A|  55,234|
| |Haywood County|     8| 128.376| N/A|   362|  5809.009| N/A|  62,317|
| |Rockingham County|     7| 76.915| N/A|   494|  5427.975| N/A|  91,010|
| |Bladen County|     7| 213.923| N/A|   596| 18214.046| N/A|  32,722|
| |Warren County|     7| 354.772| N/A|   252| 12771.780| N/A|  19,731|
| |Halifax County|     6| 119.976| N/A|   657| 13137.373| N/A|  50,010|
| |Davie County|     6| 140.036| N/A|   391|  9125.706| N/A|  42,846|
| |Carteret County|     6| 86.364| N/A|   332|  4778.835| N/A|  69,473|
| |Yadkin County|     6| 159.291| N/A|   513| 13619.349| N/A|  37,667|
| |Martin County|     6| 267.380| N/A|   245| 10918.004| N/A|  22,440|
| |Polk County|     5| 241.266| N/A|   146|  7044.972| N/A|  20,724|
| |Bertie County|     5| 263.894| N/A|   254| 13405.816| N/A|  18,947|
| |Washington County|     4| 345.423| N/A|   124| 10708.117| N/A|  11,580|
| |Jackson County|     4| 91.037| N/A|   415|  9445.127| N/A|  43,938|
| |Jones County|     4| 424.674| N/A|    79|  8387.302| N/A|   9,419|
| |Macon County|     3| 83.663| N/A|   460| 12828.379| N/A|  35,858|
| |Greene County|     3| 142.389| N/A|   318| 15093.265| N/A|  21,069|
| |Stokes County|     3| 65.802| N/A|   277|  6075.761| N/A|  45,591|
| |Pender County|     3| 47.574| N/A|   633| 10038.059| N/A|  63,060|
| |Lincoln County|     3| 34.839| N/A|   781|  9069.689| N/A|  86,111|
| |Cherokee County|     3| 104.851| N/A|   265|  9261.848| N/A|  28,612|
| |Caswell County|     2| 88.480| N/A|   189|  8361.352| N/A|  22,604|
| |Swain County|     2| 140.144| N/A|   106|  7427.650| N/A|  14,271|
| |Gates County|     2| 172.980| N/A|    46|  3978.550| N/A|  11,562|
| |Scotland County|     2| 57.433| N/A|   312|  8959.596| N/A|  34,823|
| |Perquimans County|     2| 148.555| N/A|    74|  5496.546| N/A|  13,463|
| |Person County|     2| 50.646| N/A|   202|  5115.219| N/A|  39,490|
| |Camden County|     2| 184.043| N/A|    64|  5889.390| N/A|  10,867|
| |Beaufort County|     2| 42.559| N/A|   373|  7937.183| N/A|  46,994|
| |Dare County|     2| 54.041| N/A|   203|  5485.152| N/A|  37,009|
| |Anson County|     2| 81.813| N/A|   311| 12721.918| N/A|  24,446|
| |Alexander County|     2| 53.338| N/A|   295|  7867.296| N/A|  37,497|
| |Mitchell County|     2| 133.654| N/A|   116|  7751.938| N/A|  14,964|
| |Chowan County|     1| 71.721| N/A|   145| 10399.484| N/A|  13,943|
| |Ashe County|     1| 36.761| N/A|   139|  5109.731| N/A|  27,203|
| |Pamlico County|     1| 78.579| N/A|    65|  5107.654| N/A|  12,726|
| |Transylvania County|     1| 29.082| N/A|   132|  3838.883| N/A|  34,385|
| |Tyrrell County|     1| 249.004| N/A|    92| 22908.367| N/A|   4,016|
| |Alleghany County|     0|  0.000| N/A|   165| 14815.480| N/A|  11,137|
| |Hyde County|     0|  0.000| N/A|    37|  7494.430| N/A|   4,937|
| |Yancey County|     0|  0.000| N/A|   101|  5589.684| N/A|  18,069|
| |Watauga County|     0|  0.000| N/A|   283|  5037.649| N/A|  56,177|
| |Madison County|     0|  0.000| N/A|    41|  1884.624| N/A|  21,755|
| |Graham County|     0|  0.000| N/A|    29|  3435.612| N/A|   8,441|
| |Currituck County|     0|  0.000| N/A|    71|  2557.361| N/A|  27,763|
| |Clay County|     0|  0.000| N/A|    76|  6766.984| N/A|  11,231|
| |Avery County|     0|  0.000| N/A|    99|  5638.777| N/A|  17,557|


### South Carolina ###

![South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Carolina.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SC|46 counties| 1,894| 367.859| N/A|95,472| 18542.883| N/A|5,148,714|
| |Greenville County|   198| 378.193|  6.360|10,495| 20046.147| 180.794| 523,542|
| |Charleston County|   182| 442.385|  7.292|11,926| 28988.396| 272.237| 411,406|
| |Richland County|   148| 355.975|  8.424| 8,344| 20069.319| 331.392| 415,759|
| |Horry County|   141| 398.214| 13.184| 8,317| 23488.976| 195.530| 354,081|
| |Lexington County|   107| 358.159|  5.021| 4,805| 16083.682| 186.141| 298,750|
| |Florence County|   105| 759.258| 19.520| 3,186| 23038.042| 345.853| 138,293|
| |Spartanburg County|    94| 293.947| 10.262| 3,898| 12189.440| 164.173| 319,785|
| |Berkeley County|    61| 267.653|  3.619| 4,016| 17621.223| 114.082| 227,907|
| |Orangeburg County|    60| 696.258| 11.702| 2,277| 26422.977| 301.101|  86,175|
| |Beaufort County|    53| 275.866|  8.045| 3,850| 20039.350| 409.770| 192,122|
| |Anderson County|    51| 251.780|  7.015| 2,179| 10757.413| 187.609| 202,558|
| |Clarendon County|    50| 1481.701|  0.000|   804| 23825.752| 207.438|  33,745|
| |Sumter County|    46| 431.030|  3.880| 2,395| 22441.694| 309.561| 106,721|
| |Dorchester County|    43| 264.113|  9.213| 2,910| 17873.705| 240.458| 162,809|
| |Laurens County|    41| 607.470| 40.036| 1,255| 18594.521| 162.980|  67,493|
| |Darlington County|    35| 525.384| 15.909| 1,174| 17622.865| 307.725|  66,618|
| |Aiken County|    33| 193.127| 11.705| 1,706|  9984.082| 291.900| 170,872|
| |Colleton County|    32| 849.325| 26.541|   779| 20675.744| 185.790|  37,677|
| |Williamsburg County|    29| 954.953| 28.132|   957| 31513.435| 427.042|  30,368|
| |York County|    28| 99.652|  0.000| 3,341| 11890.568| 182.310| 280,979|
| |Cherokee County|    28| 488.656| 19.834|   576| 10052.356| 209.424|  57,300|
| |Lee County|    27| 1604.469|  0.000|   537| 31911.101| 297.124|  16,828|
| |Pickens County|    24| 189.149|  0.000| 1,777| 14004.918| 173.387| 126,884|
| |Lancaster County|    23| 234.665| 10.203| 1,109| 11314.941| 139.747|  98,012|
| |Fairfield County|    23| 1029.221|  0.000|   548| 24522.307| 192.792|  22,347|
| |Dillon County|    23| 754.618|  0.000|   593| 19456.019| 282.011|  30,479|
| |Kershaw County|    23| 345.600|  0.000| 1,339| 20119.908| 303.268|  66,551|
| |Bamberg County|    20| 1421.868| 213.280|   452| 32134.224| 235.220|  14,066|
| |Chesterfield County|    20| 438.116|  9.060|   723| 15837.897| 185.501|  45,650|
| |Georgetown County|    19| 303.127|  0.000| 1,334| 21282.706| 231.380|  62,680|
| |Greenwood County|    16| 225.954|  5.914| 1,314| 18556.439| 269.884|  70,811|
| |Jasper County|    13| 432.281|  0.000|   550| 18288.831| 490.498|  30,073|
| |Chester County|    13| 403.176| 18.042|   599| 18577.100| 332.262|  32,244|
| |Marion County|    13| 424.047|  0.000|   531| 17320.677| 130.476|  30,657|
| |Calhoun County|    10| 687.144|  0.000|   369| 25355.597| 1099.430|  14,553|
| |Newberry County|     9| 234.131| N/A|   816| 21227.888| N/A|  38,440|
| |Saluda County|     8| 390.759| N/A|   431| 21052.117| N/A|  20,473|
| |Abbeville County|     8| 326.171| N/A|   304| 12394.504| N/A|  24,527|
| |Oconee County|     7| 87.999| N/A|   771|  9692.505| N/A|  79,546|
| |Hampton County|     7| 364.166| N/A|   401| 20861.513| N/A|  19,222|
| |Edgefield County|     6| 220.103| N/A|   297| 10895.084| N/A|  27,260|
| |Barnwell County|     5| 239.624| N/A|   379| 18163.520| N/A|  20,866|
| |Marlboro County|     4| 153.151| N/A|   460| 17612.375| N/A|  26,118|
| |Allendale County|     3| 345.304| N/A|   196| 22559.853| N/A|   8,688|
| |Union County|     3| 109.826| N/A|   344| 12593.352| N/A|  27,316|
| |McCormick County|     2| 211.349| N/A|   108| 11412.871| N/A|   9,463|


### Colorado ###

![Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Colorado.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|CO|64 counties| 1,851| 321.425| N/A|48,970|  8503.602| N/A|5,758,736|
| |Denver County|   412| 566.548| N/A| 9,968| 13707.163| N/A| 727,211|
| |Arapahoe County|   364| 554.379|  0.000| 7,156| 10898.734| 101.281| 656,590|
| |Jefferson County|   227| 389.445|  0.000| 4,051|  6949.961| 64.072| 582,881|
| |Adams County|   175| 338.216|  3.040| 6,248| 12075.273| 128.573| 517,421|
| |Weld County|   142| 437.607|  0.000| 3,617| 11146.654| 86.497| 324,492|
| |El Paso County|   137| 190.171|  0.590| 4,754|  6599.084| 56.913| 720,403|
| |Boulder County|    75| 229.923|  0.000| 1,982|  6076.101| 77.992| 326,196|
| |Douglas County|    59| 168.017|  0.000| 1,689|  4809.856| 46.304| 351,154|
| |Morgan County|    46| 1582.496|  0.000|   681| 23427.824| 57.680|  29,068|
| |Larimer County|    35| 98.067|  0.000| 1,456|  4079.586| 53.195| 356,899|
| |Pueblo County|    34| 201.871|  0.000|   645|  3829.620| 77.043| 168,424|
| |Broomfield County|    32| 454.126| N/A|   436|  6187.469| N/A|  70,465|
| |Chaffee County|    19| 933.386|  0.000|   292| 14344.665| 98.241|  20,356|
| |Montrose County|    13| 304.037|  0.000|   287|  6712.194| 48.696|  42,758|
| |Alamosa County|     9| 554.426| N/A|   224| 13799.051| N/A|  16,233|
| |Eagle County|     9| 163.259| N/A| 1,096| 19881.365| N/A|  55,127|
| |Otero County|     6| 328.263| N/A|    65|  3556.188| N/A|  18,278|
| |Gunnison County|     6| 343.603| N/A|   266| 15233.078| N/A|  17,462|
| |Routt County|     6| 234.028| N/A|   110|  4290.506| N/A|  25,638|
| |Logan County|     5| 223.125| N/A|   649| 28961.578| N/A|  22,409|
| |Montezuma County|     4| 152.771| N/A|   108|  4124.814| N/A|  26,183|
| |Summit County|     4| 128.986| N/A|   327| 10544.645| N/A|  31,011|
| |Garfield County|     4| 66.599| N/A|   742| 12354.107| N/A|  60,061|
| |Mesa County|     3| 19.454| N/A|   280|  1815.706| N/A| 154,210|
| |Kit Carson County|     3| 422.714| N/A|    43|  6058.898| N/A|   7,097|
| |Teller County|     3| 118.166| N/A|   121|  4766.031| N/A|  25,388|
| |Elbert County|     2| 74.825| N/A|    97|  3629.017| N/A|  26,729|
| |Saguache County|     2| 293.083| N/A|   106| 15533.411| N/A|   6,824|
| |Rio Grande County|     2| 177.510| N/A|    88|  7810.420| N/A|  11,267|
| |Pitkin County|     2| 112.568| N/A|   180| 10131.142| N/A|  17,767|
| |La Plata County|     2| 35.574| N/A|   201|  3575.177| N/A|  56,221|
| |Huerfano County|     1| 144.991| N/A|     7|  1014.934| N/A|   6,897|
| |Moffat County|     1| 75.284| N/A|    26|  1957.389| N/A|  13,283|
| |Sedgwick County|     1| 444.840| N/A|    11|  4893.238| N/A|   2,248|
| |Delta County|     1| 32.090| N/A|   115|  3690.392| N/A|  31,162|
| |Ouray County|     1| 201.939| N/A|    12|  2423.263| N/A|   4,952|
| |Grand County|     1| 63.557| N/A|    44|  2796.492| N/A|  15,734|
| |Park County|     1| 53.064| N/A|    42|  2228.708| N/A|  18,845|
| |Clear Creek County|     1| 103.093| N/A|    28|  2886.598| N/A|   9,700|
| |Crowley County|     1| 164.989| N/A|    72| 11879.228| N/A|   6,061|
| |Fremont County|     0|  0.000| N/A|   117|  2445.703| N/A|  47,839|
| |Archuleta County|     0|  0.000| N/A|    34|  2423.551| N/A|  14,029|
| |Dolores County|     0|  0.000| N/A|     1|   486.618| N/A|   2,055|
| |Custer County|     0|  0.000| N/A|    11|  2170.481| N/A|   5,068|
| |Costilla County|     0|  0.000| N/A|    22|  5659.892| N/A|   3,887|
| |Conejos County|     0|  0.000| N/A|    23|  2803.169| N/A|   8,205|
| |Cheyenne County|     0|  0.000| N/A|     8|  4369.197| N/A|   1,831|
| |Bent County|     0|  0.000| N/A|     8|  1434.463| N/A|   5,577|
| |Baca County|     0|  0.000| N/A|    14|  3909.522| N/A|   3,581|
| |Gilpin County|     0|  0.000| N/A|    16|  2562.870| N/A|   6,243|
| |Hinsdale County|     0|  0.000| N/A|     3|  3658.537| N/A|     820|
| |Jackson County|     0|  0.000| N/A|     8|  5747.126| N/A|   1,392|
| |Kiowa County|     0|  0.000| N/A|     0|     0.000| N/A|   1,406|
| |Yuma County|     0|  0.000| N/A|    63|  6288.053| N/A|  10,019|
| |Washington County|     0|  0.000| N/A|    47|  9576.202| N/A|   4,908|
| |San Miguel County|     0|  0.000| N/A|    80|  9781.147| N/A|   8,179|
| |San Juan County|     0|  0.000| N/A|     2|  2747.253| N/A|     728|
| |Rio Blanco County|     0|  0.000| N/A|     8|  1265.022| N/A|   6,324|
| |Prowers County|     0|  0.000| N/A|    50|  4107.788| N/A|  12,172|
| |Phillips County|     0|  0.000| N/A|    19|  4454.865| N/A|   4,265|
| |Mineral County|     0|  0.000| N/A|    18| 23407.022| N/A|     769|
| |Lincoln County|     0|  0.000| N/A|     7|  1227.855| N/A|   5,701|
| |Las Animas County|     0|  0.000| N/A|    15|  1034.055| N/A|  14,506|
| |Lake County|     0|  0.000| N/A|    74|  9105.451| N/A|   8,127|


### Mississippi ###

![Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Mississippi.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MS|82 counties| 1,804| 606.152| N/A|63,444| 21317.481| N/A|2,976,149|
| |Hinds County|   112| 483.092|  8.627| 5,416| 23360.939| 307.376| 231,840|
| |Neshoba County|    90| 3090.872| 68.686| 1,264| 43409.575| 828.784|  29,118|
| |Lauderdale County|    90| 1214.165| 11.223| 1,379| 18603.710| 294.535|  74,125|
| |Leflore County|    61| 2164.425| 17.741|   882| 31295.462| 283.859|  28,183|
| |Madison County|    60| 564.589| 19.030| 2,363| 22235.396| 284.219| 106,272|
| |Jones County|    57| 837.029|  0.000| 1,828| 26843.666| 353.714|  68,098|
| |Forrest County|    55| 734.342| 11.606| 1,701| 22711.190| 358.138|  74,897|
| |Monroe County|    51| 1446.726| 11.738|   731| 20736.412| 347.960|  35,252|
| |Holmes County|    48| 2821.869| 24.977|   859| 50499.706| 333.166|  17,010|
| |Jackson County|    41| 285.482| 16.777| 2,156| 15012.150| 545.287| 143,617|
| |Lincoln County|    41| 1200.480| 16.995|   787| 23043.364| 530.586|  34,153|
| |Pearl River County|    37| 666.247|  0.000|   515|  9273.431| 232.542|  55,535|
| |Oktibbeha County|    37| 746.163| 17.003| 1,077| 21719.402| 231.916|  49,587|
| |Harrison County|    35| 168.205|  6.007| 2,287| 10990.965| 314.501| 208,080|
| |Washington County|    35| 797.103| 28.468| 1,548| 35254.731| 579.451|  43,909|
| |Lowndes County|    33| 563.188| 17.066| 1,023| 17458.828| 285.921|  58,595|
| |Pike County|    33| 839.951| 10.529|   861| 21915.089| 332.783|  39,288|
| |Bolivar County|    32| 1044.796|  0.000| 1,010| 32976.361| 804.516|  30,628|
| |Lee County|    32| 374.549|  9.738| 1,297| 15180.954| 311.659|  85,436|
| |Warren County|    31| 683.105| 40.861|   995| 21925.475| 285.526|  45,381|
| |Rankin County|    31| 199.651|  0.000| 2,202| 14181.657| 180.330| 155,271|
| |Simpson County|    30| 1125.366| 53.186|   767| 28771.851| 877.884|  26,658|
| |Copiah County|    28| 997.684| 60.084|   929| 33101.728| 225.123|  28,065|
| |Tate County|    27| 953.356| 59.146|   683| 24116.380| 176.547|  28,321|
| |DeSoto County|    27| 145.989|  0.000| 3,472| 18773.149| 371.084| 184,945|
| |Clarke County|    25| 1608.648|  0.000|   322| 20719.387| 602.088|  15,541|
| |Leake County|    25| 1097.165|  0.000|   776| 34055.999| 155.567|  22,786|
| |Adams County|    25| 814.518|  0.000|   596| 19418.108| 183.738|  30,693|
| |Attala County|    24| 1320.568|  0.000|   510| 28062.067| 303.015|  18,174|
| |Sunflower County|    23| 915.970| 16.780|   942| 37514.934| 576.341|  25,110|
| |Grenada County|    21| 1011.658| 20.397|   819| 39454.668| 144.523|  20,758|
| |Wayne County|    21| 1040.480|  0.000|   749| 37110.439| 49.547|  20,183|
| |Scott County|    20| 711.136| 35.557|   978| 34774.570| 356.272|  28,124|
| |Marion County|    19| 773.206| 17.383|   634| 25800.676| 465.303|  24,573|
| |Chickasaw County|    19| 1110.916|  0.000|   438| 25609.542| 31.077|  17,103|
| |Walthall County|    19| 1329.973|  0.000|   482| 33739.325| 974.851|  14,286|
| |Winston County|    15| 835.422|  0.000|   593| 33027.012| 501.253|  17,955|
| |Kemper County|    15| 1539.725|  0.000|   227| 23301.170|  0.000|   9,742|
| |Union County|    15| 520.562| 34.704|   552| 19156.689| 371.622|  28,815|
| |Lafayette County|    14| 259.168| 37.024|   907| 16790.389| 222.144|  54,019|
| |Clay County|    14| 724.788| 13.414|   380| 19672.810| 233.875|  19,316|
| |Hancock County|    14| 293.920|  0.000|   349|  7327.007| 136.463|  47,632|
| |Covington County|    13| 697.575| 53.660|   603| 32356.729| 384.790|  18,636|
| |Smith County|    13| 816.788|  0.000|   389| 24440.814| 251.319|  15,916|
| |Claiborne County|    13| 1446.373|  0.000|   399| 44392.523|  0.000|   8,988|
| |Tippah County|    13| 590.506| 24.071|   320| 14535.544| 210.721|  22,015|
| |Wilkinson County|    13| 1506.373|  0.000|   193| 22363.847| 347.625|   8,630|
| |Lamar County|    13| 205.232|  0.000| 1,177| 18581.374| 381.323|  63,343|
| |Yazoo County|    12| 404.176|  0.000|   803| 27046.143| 336.814|  29,690|
| |Webster County|    12| 1238.518|  0.000|   211| 21777.273| 554.980|   9,689|
| |Panola County|    12| 350.959| 12.102|   960| 28076.743| 146.233|  34,192|
| |Newton County|    11| 523.361|  0.000|   530| 25216.481| 266.162|  21,018|
| |Carroll County|    11| 1105.861|  0.000|   248| 24932.140| 116.386|   9,947|
| |Humphreys County|    11| 1364.087|  0.000|   281| 34846.230| 620.040|   8,064|
| |Greene County|    11| 809.657|  0.000|   230| 16929.192|  0.000|  13,586|
| |Noxubee County|    11| 1055.966| 41.006|   438| 42046.655| 791.007|  10,417|
| |Coahoma County|    10| 451.998|  0.000|   684| 30916.652| 426.345|  22,124|
| |Tallahatchie County|    10| 724.165|  0.000|   512| 37077.268| 711.046|  13,809|
| |Itawamba County|    10| 427.533|  0.000|   323| 13809.320|  0.000|  23,390|
| |Yalobusha County|    10| 825.900|  0.000|   304| 25107.367|  0.000|  12,108|
| |Marshall County|     9| 255.001| N/A|   616| 17453.392| N/A|  35,294|
| |Calhoun County|     9| 626.697| N/A|   392| 27296.149| N/A|  14,361|
| |Jasper County|     9| 549.350| N/A|   379| 23133.736| N/A|  16,383|
| |Prentiss County|     9| 358.195| N/A|   369| 14685.983| N/A|  25,126|
| |Pontotoc County|     8| 248.648| N/A|   780| 24243.178| N/A|  32,174|
| |Lawrence County|     7| 556.174| N/A|   302| 23994.915| N/A|  12,586|
| |Perry County|     7| 584.649| N/A|   220| 18374.676| N/A|  11,973|
| |Tunica County|     6| 622.924| N/A|   307| 31872.924| N/A|   9,632|
| |Jefferson County|     6| 858.369| N/A|   193| 27610.873| N/A|   6,990|
| |Jefferson Davis County|     6| 539.180| N/A|   225| 20219.267| N/A|  11,128|
| |Amite County|     6| 487.924| N/A|   217| 17646.580| N/A|  12,297|
| |Tishomingo County|     5| 257.958| N/A|   344| 17747.511| N/A|  19,383|
| |Alcorn County|     5| 135.307| N/A|   377| 10202.149| N/A|  36,953|
| |George County|     4| 163.265| N/A|   545| 22244.898| N/A|  24,500|
| |Choctaw County|     4| 487.211| N/A|   129| 15712.546| N/A|   8,210|
| |Sharkey County|     3| 694.284| N/A|   191| 44202.731| N/A|   4,321|
| |Stone County|     3| 163.613| N/A|   160|  8726.003| N/A|  18,336|
| |Montgomery County|     3| 306.905| N/A|   302| 30895.141| N/A|   9,775|
| |Franklin County|     2| 259.302| N/A|   115| 14909.892| N/A|   7,713|
| |Quitman County|     1| 147.232| N/A|   238| 35041.225| N/A|   6,792|
| |Issaquena County|     1| 753.580| N/A|    24| 18085.908| N/A|   1,327|
| |Benton County|     0|  0.000| N/A|   128| 15498.244| N/A|   8,259|


### Alabama ###

![Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Alabama.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AL|67 counties| 1,639| 334.273| N/A|91,776| 18717.629| N/A|4,903,185|
| |Jefferson County|   230| 349.240|  2.626|12,186| 18503.643| 317.353| 658,573|
| |Mobile County|   204| 493.696| 10.607| 9,269| 22431.693| 222.523| 413,210|
| |Montgomery County|   148| 653.462|  7.017| 6,350| 28037.053| 223.617| 226,486|
| |Tallapoosa County|    78| 1932.271|  0.000|   827| 20487.031| 172.150|  40,367|
| |Tuscaloosa County|    69| 329.584| 10.839| 4,002| 19115.856| 296.148| 209,355|
| |Walker County|    64| 1007.541|  6.669| 1,479| 23283.638| 91.968|  63,521|
| |Lee County|    42| 255.254|  0.000| 2,554| 15521.873| 139.077| 164,542|
| |Chambers County|    38| 1142.720|  0.000|   832| 25019.547| 173.098|  33,254|
| |Elmore County|    37| 455.615|  0.000| 1,633| 20108.609| 184.604|  81,209|
| |Butler County|    35| 1799.671|  0.000|   754| 38770.053| 51.419|  19,448|
| |Marshall County|    34| 351.334| 10.333| 3,001| 31010.395| 182.849|  96,774|
| |Shelby County|    32| 146.990|  0.000| 3,119| 14326.924| 220.485| 217,702|
| |Etowah County|    28| 273.790|  0.000| 1,967| 19233.778| 180.897| 102,268|
| |Madison County|    27| 72.404|  0.000| 5,122| 13735.254| 155.937| 372,909|
| |Hale County|    26| 1774.623|  0.000|   459| 31328.920| 217.067|  14,651|
| |Lowndes County|    24| 2467.613|  0.000|   561| 57680.444| 485.384|   9,726|
| |Marion County|    24| 807.836|  0.000|   547| 18411.929| 109.746|  29,709|
| |Baldwin County|    23| 103.031|  0.722| 3,322| 14881.246| 242.772| 223,234|
| |Dale County|    23| 467.746| 20.337|   798| 16228.748| 140.543|  49,172|
| |Dallas County|    23| 618.346|  0.000| 1,298| 34896.225| 147.149|  37,196|
| |Autauga County|    21| 375.879|  0.000| 1,030| 18435.984| 84.801|  55,869|
| |Franklin County|    20| 637.714|  0.000| 1,215| 38741.152| 315.598|  31,362|
| |Covington County|    20| 539.826|  0.000|   716| 19325.758| 91.233|  37,049|
| |Sumter County|    18| 1448.459|  0.000|   360| 28969.180|  0.000|  12,427|
| |Morgan County|    15| 125.335|  0.000| 2,270| 18967.404| 189.890| 119,679|
| |Escambia County|    15| 409.467|  0.000|   981| 26779.134| 86.929|  36,633|
| |St. Clair County|    14| 156.404|  9.360| 1,252| 13986.951| 194.643|  89,512|
| |Marengo County|    14| 742.194|  0.000|   529| 28044.320| 243.610|  18,863|
| |Macon County|    13| 719.504|  0.000|   316| 17489.484| 172.598|  18,068|
| |Lauderdale County|    13| 140.193| 10.784| 1,111| 11981.149| 212.719|  92,729|
| |Talladega County|    13| 162.545|  0.000|   946| 11828.253| 209.299|  79,978|
| |Limestone County|    13| 131.426|  0.000| 1,227| 12404.590| 152.926|  98,915|
| |Colbert County|    13| 235.332|  7.530| 1,122| 20311.001| 262.486|  55,241|
| |Calhoun County|    13| 114.432| 14.942| 1,627| 14321.553| 296.725| 113,605|
| |DeKalb County|    13| 181.785|  0.000| 1,721| 24065.555| 172.417|  71,513|
| |Cullman County|    12| 143.253|  4.940| 1,171| 13979.085| 205.257|  83,768|
| |Houston County|    12| 113.334|  0.000| 1,334| 12598.931| 70.834| 105,882|
| |Washington County|    12| 735.024| 26.164|   315| 19294.377| 131.266|  16,326|
| |Choctaw County|    12| 953.213|  0.000|   276| 21923.902| 80.336|  12,589|
| |Winston County|    11| 465.530|  0.000|   435| 18409.581| 42.321|  23,629|
| |Greene County|    11| 1356.183|  0.000|   247| 30452.472| 298.960|   8,111|
| |Bullock County|    11| 1089.001|  0.000|   444| 43956.044| 256.413|  10,101|
| |Conecuh County|    10| 828.706|  0.000|   373| 30910.748| 82.871|  12,067|
| |Randolph County|    10| 440.102|  0.000|   392| 17252.002| 72.698|  22,722|
| |Wilcox County|    10| 964.041|  0.000|   411| 39622.096| 289.212|  10,373|
| |Pickens County|     9| 451.581| N/A|   376| 18866.031| N/A|  19,930|
| |Clarke County|     9| 381.001| N/A|   491| 20785.708| N/A|  23,622|
| |Pike County|     7| 211.391| N/A|   672| 20293.531| N/A|  33,114|
| |Cherokee County|     7| 267.216| N/A|   249|  9505.268| N/A|  26,196|
| |Chilton County|     6| 135.050| N/A|   738| 16611.146| N/A|  44,428|
| |Fayette County|     5| 306.711| N/A|   178| 10918.906| N/A|  16,302|
| |Clay County|     5| 377.786| N/A|   225| 17000.378| N/A|  13,235|
| |Barbour County|     5| 202.544| N/A|   564| 22846.958| N/A|  24,686|
| |Coffee County|     5| 95.526| N/A|   725| 13851.209| N/A|  52,342|
| |Bibb County|     4| 178.619| N/A|   384| 17147.450| N/A|  22,394|
| |Jackson County|     4| 77.480| N/A|   890| 17239.376| N/A|  51,626|
| |Monroe County|     4| 192.929| N/A|   396| 19099.986| N/A|  20,733|
| |Perry County|     4| 448.280| N/A|   432| 48414.210| N/A|   8,923|
| |Henry County|     3| 174.368| N/A|   247| 14356.292| N/A|  17,205|
| |Blount County|     3| 51.880| N/A|   745| 12883.478| N/A|  57,826|
| |Crenshaw County|     3| 217.833| N/A|   307| 22291.606| N/A|  13,772|
| |Lamar County|     2| 144.875| N/A|   205| 14849.692| N/A|  13,805|
| |Russell County|     2| 34.506| N/A| 1,267| 21859.526| N/A|  57,961|
| |Coosa County|     2| 187.564| N/A|    95|  8909.313| N/A|  10,663|
| |Cleburne County|     1| 67.069| N/A|   121|  8115.359| N/A|  14,910|
| |Lawrence County|     1| 30.373| N/A|   325|  9871.219| N/A|  32,924|
| |Geneva County|     0|  0.000| N/A|   243|  9249.743| N/A|  26,271|


### Minnesota ###

![Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Minnesota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MN|87 counties| 1,629| 288.849| N/A|57,670| 10225.845| N/A|5,639,632|
| |Hennepin County|   825| 651.740|  3.950|18,393| 14530.238| 158.555|1,265,843|
| |Ramsey County|   261| 474.269|  0.000| 7,130| 12956.075| 166.043| 550,321|
| |Anoka County|   113| 316.597|  0.440| 3,456|  9682.815| 124.286| 356,921|
| |Dakota County|   104| 242.412|  1.335| 4,112|  9584.612| 137.010| 429,021|
| |Washington County|    43| 163.847|  0.000| 1,978|  7536.961| 116.405| 262,440|
| |Clay County|    40| 622.840|  0.000|   758| 11802.809| 79.428|  64,222|
| |Olmsted County|    23| 145.300|  0.000| 1,649| 10417.391| 62.188| 158,293|
| |Stearns County|    20| 124.166|  0.000| 2,847| 17674.996| 55.732| 161,075|
| |St. Louis County|    19| 95.444|  0.000|   475|  2386.095| 89.902| 199,070|
| |Scott County|    18| 120.795| 11.391| 1,439|  9656.876| 187.903| 149,013|
| |Winona County|    16| 316.932|  0.000|   252|  4991.681| 47.853|  50,484|
| |Crow Wing County|    14| 215.203|  8.146|   221|  3397.126| 122.973|  65,055|
| |Nicollet County|    13| 379.296|  0.000|   322|  9394.877| 145.883|  34,274|
| |Itasca County|    12| 265.899|  0.000|   135|  2991.358| 66.475|  45,130|
| |Pipestone County|     9| 986.193| N/A|   144| 15779.093| N/A|   9,126|
| |Rice County|     8| 119.453| N/A| 1,006| 15021.203| N/A|  66,972|
| |Goodhue County|     8| 172.637| N/A|   183|  3949.072| N/A|  46,340|
| |Sherburne County|     7| 71.988| N/A|   667|  6859.458| N/A|  97,238|
| |Nobles County|     6| 277.405| N/A| 1,751| 80956.124| N/A|  21,629|
| |Renville County|     5| 343.690| N/A|    60|  4124.278| N/A|  14,548|
| |Wright County|     5| 36.133| N/A|   827|  5976.427| N/A| 138,377|
| |Blue Earth County|     5| 73.907| N/A|   865| 12785.834| N/A|  67,653|
| |Martin County|     5| 254.026| N/A|   204| 10364.274| N/A|  19,683|
| |Benton County|     3| 73.369| N/A|   313|  7654.871| N/A|  40,889|
| |Lyon County|     3| 117.767| N/A|   420| 16487.399| N/A|  25,474|
| |Koochiching County|     3| 245.319| N/A|    74|  6051.190| N/A|  12,229|
| |Otter Tail County|     3| 51.067| N/A|   182|  3098.083| N/A|  58,746|
| |Polk County|     3| 95.651| N/A|   139|  4431.833| N/A|  31,364|
| |Mille Lacs County|     3| 114.168| N/A|    69|  2625.871| N/A|  26,277|
| |Wilkin County|     3| 483.325| N/A|    31|  4994.361| N/A|   6,207|
| |Todd County|     2| 81.090| N/A|   421| 17069.413| N/A|  24,664|
| |Sibley County|     2| 134.544| N/A|    80|  5381.769| N/A|  14,865|
| |Meeker County|     2| 86.125| N/A|    85|  3660.322| N/A|  23,222|
| |Mower County|     2| 49.923| N/A| 1,088| 27157.905| N/A|  40,062|
| |Carver County|     2| 19.031| N/A|   805|  7660.174| N/A| 105,089|
| |Cass County|     2| 67.161| N/A|    66|  2216.327| N/A|  29,779|
| |Brown County|     2| 79.974| N/A|    85|  3398.912| N/A|  25,008|
| |Chisago County|     1| 17.674| N/A|   184|  3252.090| N/A|  56,579|
| |Chippewa County|     1| 84.746| N/A|   101|  8559.322| N/A|  11,800|
| |Becker County|     1| 29.050| N/A|   148|  4299.451| N/A|  34,423|
| |Grant County|     1| 167.448| N/A|    52|  8707.301| N/A|   5,972|
| |Aitkin County|     1| 62.949| N/A|    29|  1825.507| N/A|  15,886|
| |Kandiyohi County|     1| 23.149| N/A|   681| 15764.254| N/A|  43,199|
| |Kanabec County|     1| 61.211| N/A|    30|  1836.322| N/A|  16,337|
| |Murray County|     1| 122.041| N/A|   122| 14888.943| N/A|   8,194|
| |Le Sueur County|     1| 34.618| N/A|   203|  7027.383| N/A|  28,887|
| |Morrison County|     1| 29.953| N/A|    82|  2456.119| N/A|  33,386|
| |Mahnomen County|     1| 180.930| N/A|    25|  4523.250| N/A|   5,527|
| |Pennington County|     1| 70.827| N/A|    73|  5170.338| N/A|  14,119|
| |Steele County|     1| 27.286| N/A|   334|  9113.482| N/A|  36,649|
| |Swift County|     1| 107.921| N/A|    52|  5611.915| N/A|   9,266|
| |Freeborn County|     1| 33.024| N/A|   356| 11756.547| N/A|  30,281|
| |Pope County|     0|  0.000| N/A|    46|  4089.252| N/A|  11,249|
| |Marshall County|     0|  0.000| N/A|    29|  3106.255| N/A|   9,336|
| |Pine County|     0|  0.000| N/A|   128|  4327.394| N/A|  29,579|
| |Red Lake County|     0|  0.000| N/A|    21|  5178.792| N/A|   4,055|
| |Redwood County|     0|  0.000| N/A|    32|  2109.426| N/A|  15,170|
| |Rock County|     0|  0.000| N/A|    75|  8051.530| N/A|   9,315|
| |Watonwan County|     0|  0.000| N/A|   300| 27530.513| N/A|  10,897|
| |Yellow Medicine County|     0|  0.000| N/A|    50|  5149.861| N/A|   9,709|
| |Waseca County|     0|  0.000| N/A|   133|  7145.927| N/A|  18,612|
| |Wadena County|     0|  0.000| N/A|    24|  1754.130| N/A|  13,682|
| |Wabasha County|     0|  0.000| N/A|    84|  3884.034| N/A|  21,627|
| |Traverse County|     0|  0.000| N/A|    10|  3068.426| N/A|   3,259|
| |Stevens County|     0|  0.000| N/A|    16|  1631.820| N/A|   9,805|
| |Roseau County|     0|  0.000| N/A|    46|  3033.300| N/A|  15,165|
| |Norman County|     0|  0.000| N/A|    37|  5803.922| N/A|   6,375|
| |Hubbard County|     0|  0.000| N/A|    30|  1395.933| N/A|  21,491|
| |Beltrami County|     0|  0.000| N/A|   207|  4386.708| N/A|  47,188|
| |Big Stone County|     0|  0.000| N/A|    22|  4407.934| N/A|   4,991|
| |Carlton County|     0|  0.000| N/A|   130|  3624.097| N/A|  35,871|
| |McLeod County|     0|  0.000| N/A|   145|  4039.785| N/A|  35,893|
| |Lincoln County|     0|  0.000| N/A|    54|  9576.166| N/A|   5,639|
| |Lake of the Woods County|     0|  0.000| N/A|     1|   267.380| N/A|   3,740|
| |Lake County|     0|  0.000| N/A|    18|  1691.570| N/A|  10,641|
| |Lac qui Parle County|     0|  0.000| N/A|     6|   905.934| N/A|   6,623|
| |Kittson County|     0|  0.000| N/A|     3|   697.999| N/A|   4,298|
| |Jackson County|     0|  0.000| N/A|    71|  7211.050| N/A|   9,846|
| |Isanti County|     0|  0.000| N/A|   114|  2808.158| N/A|  40,596|
| |Houston County|     0|  0.000| N/A|    40|  2150.538| N/A|  18,600|
| |Fillmore County|     0|  0.000| N/A|    61|  2895.524| N/A|  21,067|
| |Faribault County|     0|  0.000| N/A|    83|  6079.250| N/A|  13,653|
| |Douglas County|     0|  0.000| N/A|   136|  3565.717| N/A|  38,141|
| |Dodge County|     0|  0.000| N/A|   125|  5971.147| N/A|  20,934|
| |Cottonwood County|     0|  0.000| N/A|   173| 15451.947| N/A|  11,196|
| |Cook County|     0|  0.000| N/A|     2|   366.099| N/A|   5,463|
| |Clearwater County|     0|  0.000| N/A|    14|  1587.662| N/A|   8,818|


### Washington ###

![Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Washington.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WA|39 counties| 1,621| 212.872| N/A|59,894|  7865.376| N/A|7,614,893|
| |King County|   659| 292.527|  0.257|15,865|  7042.404| 56.024|2,252,782|
| |Yakima County|   210| 837.077|  9.965|10,142| 40426.830| 179.007| 250,873|
| |Snohomish County|   190| 231.120|  0.207| 5,261|  6399.597| 51.090| 822,083|
| |Pierce County|   129| 142.545|  0.345| 5,348|  5909.523| 75.140| 904,980|
| |Benton County|   111| 543.079|  2.078| 3,613| 17676.990| 186.333| 204,390|
| |Spokane County|    72| 137.720|  7.844| 4,088|  7819.464| 158.761| 522,798|
| |Franklin County|    47| 493.583|  0.000| 3,390| 35601.017| 275.075|  95,222|
| |Clark County|    42| 86.023|  0.000| 1,705|  3492.128| 77.830| 488,241|
| |Whatcom County|    38| 165.760|  0.000|   957|  4174.537| 48.223| 229,247|
| |Skagit County|    21| 162.532|  0.000|   849|  6570.953| 88.257| 129,205|
| |Kittitas County|    18| 375.509|  0.000|   354|  7385.001| 49.360|  47,935|
| |Grant County|    12| 122.784|  0.000| 1,333| 13639.201| 199.523|  97,733|
| |Island County|    11| 129.197|  0.000|   241|  2830.599|  9.851|  85,141|
| |Thurston County|    10| 34.419|  2.940|   659|  2268.221| 27.817| 290,536|
| |Chelan County|    10| 129.534|  0.000| 1,224| 15854.922| 350.249|  77,200|
| |Douglas County|     7| 161.183| N/A|   868| 19986.645| N/A|  43,429|
| |Cowlitz County|     5| 45.211| N/A|   454|  4105.142| N/A| 110,593|
| |Adams County|     4| 200.170| N/A|   407| 20367.312| N/A|  19,983|
| |Kitsap County|     4| 14.734| N/A|   690|  2541.689| N/A| 271,473|
| |Walla Walla County|     3| 49.375| N/A|   470|  7735.352| N/A|  60,760|
| |Lewis County|     3| 37.171| N/A|   194|  2403.757| N/A|  80,707|
| |Klickitat County|     3| 133.779| N/A|   108|  4816.054| N/A|  22,425|
| |Okanogan County|     2| 47.345| N/A|   795| 18819.686| N/A|  42,243|
| |Pacific County|     2| 89.004| N/A|    44|  1958.079| N/A|  22,471|
| |Grays Harbor County|     2| 26.645| N/A|   109|  1452.152| N/A|  75,061|
| |Asotin County|     2| 88.566| N/A|    24|  1062.793| N/A|  22,582|
| |Columbia County|     1| 250.941| N/A|    13|  3262.233| N/A|   3,985|
| |Mason County|     1| 14.977| N/A|   181|  2710.879| N/A|  66,768|
| |Skamania County|     1| 82.761| N/A|    56|  4634.611| N/A|  12,083|
| |Stevens County|     1| 21.871| N/A|    96|  2099.600| N/A|  45,723|
| |Clallam County|     0|  0.000| N/A|    98|  1267.280| N/A|  77,331|
| |Whitman County|     0|  0.000| N/A|    87|  1736.388| N/A|  50,104|
| |Wahkiakum County|     0|  0.000| N/A|     5|  1114.082| N/A|   4,488|
| |San Juan County|     0|  0.000| N/A|    28|  1592.538| N/A|  17,582|
| |Pend Oreille County|     0|  0.000| N/A|    39|  2841.737| N/A|  13,724|
| |Lincoln County|     0|  0.000| N/A|    19|  1736.905| N/A|  10,939|
| |Jefferson County|     0|  0.000| N/A|    54|  1675.926| N/A|  32,221|
| |Garfield County|     0|  0.000| N/A|     2|   898.876| N/A|   2,225|
| |Ferry County|     0|  0.000| N/A|    24|  3146.716| N/A|   7,627|


### Missouri ###

![Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Missouri.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MO|115 counties| 1,240| 202.039| N/A|49,346|  8040.176| N/A|6,137,428|
| |St. Louis County|   823| 827.797|  1.006|18,931| 19041.345| 364.309| 994,205|
| |St. Charles County|    87| 216.406|  0.000| 3,842|  9556.691| 248.797| 402,022|
| |Jackson County|    61| 86.770|  1.180| 3,713|  5281.567| 125.079| 703,011|
| |Jasper County|    27| 222.537|  0.000| 1,694| 13962.152| 57.695| 121,328|
| |Jefferson County|    24| 106.628|  0.000| 1,486|  6602.068| 202.067| 225,081|
| |Clay County|    20| 80.017|  0.000|   974|  3896.811| 106.889| 249,948|
| |Franklin County|    18| 173.132|  0.000|   566|  5444.035| 132.019| 103,967|
| |Scott County|    13| 339.603|  0.000|   358|  9352.142| 85.493|  38,280|
| |Platte County|    11| 105.346|  9.577|   332|  3179.528| 65.691| 104,418|
| |Buchanan County|    10| 114.464|  0.000| 1,069| 12236.161| 44.231|  87,364|
| |Greene County|    10| 34.120|  0.000| 1,350|  4606.157| 160.771| 293,086|
| |Pemiscot County|     9| 569.440| N/A|   226| 14299.272| N/A|  15,805|
| |Gentry County|     9| 1369.655| N/A|    82| 12479.075| N/A|   6,571|
| |Stoddard County|     9| 310.078| N/A|   215|  7407.407| N/A|  29,025|
| |Cass County|     9| 85.082| N/A|   679|  6418.983| N/A| 105,780|
| |Saline County|     7| 307.544| N/A|   421| 18496.551| N/A|  22,761|
| |McDonald County|     7| 306.520| N/A|   942| 41248.851| N/A|  22,837|
| |Newton County|     6| 103.029| N/A|   833| 14303.867| N/A|  58,236|
| |Cape Girardeau County|     5| 63.395| N/A|   614|  7784.864| N/A|  78,871|
| |Camden County|     5| 107.980| N/A|   326|  7040.276| N/A|  46,305|
| |Dunklin County|     4| 137.311| N/A|   276|  9474.443| N/A|  29,131|
| |Perry County|     4| 209.030| N/A|   214| 11183.110| N/A|  19,136|
| |Henry County|     3| 137.463| N/A|    73|  3344.941| N/A|  21,824|
| |Cole County|     3| 39.090| N/A|   354|  4612.678| N/A|  76,745|
| |Pettis County|     3| 70.857| N/A|   454| 10722.974| N/A|  42,339|
| |Boone County|     3| 16.624| N/A| 1,283|  7109.491| N/A| 180,463|
| |Taney County|     3| 53.640| N/A|   507|  9065.227| N/A|  55,928|
| |St. Francois County|     2| 29.755| N/A|   334|  4969.129| N/A|  67,215|
| |Lafayette County|     2| 61.147| N/A|   166|  5075.211| N/A|  32,708|
| |Lawrence County|     2| 52.144| N/A|   202|  5266.588| N/A|  38,355|
| |Johnson County|     2| 36.995| N/A|   474|  8767.711| N/A|  54,062|
| |Howell County|     2| 49.854| N/A|   143|  3564.574| N/A|  40,117|
| |Moniteau County|     2| 123.977| N/A|   136|  8430.449| N/A|  16,132|
| |Douglas County|     2| 151.688| N/A|    83|  6295.032| N/A|  13,185|
| |Butler County|     2| 47.083| N/A|   253|  5956.024| N/A|  42,478|
| |Barry County|     2| 55.883| N/A|   242|  6761.854| N/A|  35,789|
| |Washington County|     1| 40.437| N/A|    66|  2668.823| N/A|  24,730|
| |Stone County|     1| 31.297| N/A|   106|  3317.476| N/A|  31,952|
| |Webster County|     1| 25.258| N/A|   125|  3157.203| N/A|  39,592|
| |Laclede County|     1| 27.993| N/A|   197|  5514.654| N/A|  35,723|
| |Harrison County|     1| 119.732| N/A|    60|  7183.908| N/A|   8,352|
| |Lewis County|     1| 102.291| N/A|    35|  3580.196| N/A|   9,776|
| |Lincoln County|     1| 16.945| N/A|   343|  5812.279| N/A|  59,013|
| |Linn County|     1| 83.893| N/A|    31|  2600.671| N/A|  11,920|
| |Ste. Genevieve County|     1| 55.885| N/A|    51|  2850.117| N/A|  17,894|
| |Marion County|     1| 35.051| N/A|   164|  5748.335| N/A|  28,530|
| |New Madrid County|     1| 58.562| N/A|   205| 12005.153| N/A|  17,076|
| |Osage County|     1| 73.448| N/A|    46|  3378.627| N/A|  13,615|
| |Pike County|     1| 54.639| N/A|    79|  4316.468| N/A|  18,302|
| |Grundy County|     1| 101.523| N/A|    25|  2538.071| N/A|   9,850|
| |Shannon County|     1| 122.459| N/A|    44|  5388.195| N/A|   8,166|
| |DeKalb County|     1| 79.700| N/A|    35|  2789.511| N/A|  12,547|
| |Scotland County|     1| 203.998| N/A|    14|  2855.977| N/A|   4,902|
| |Benton County|     1| 51.432| N/A|    78|  4011.727| N/A|  19,443|
| |Bates County|     1| 61.835| N/A|    42|  2597.081| N/A|  16,172|
| |Audrain County|     1| 39.389| N/A|   198|  7798.960| N/A|  25,388|
| |Andrew County|     1| 56.459| N/A|    87|  4911.924| N/A|  17,712|
| |Pulaski County|     1| 19.009| N/A|   192|  3649.704| N/A|  52,607|
| |Putnam County|     1| 212.947| N/A|    13|  2768.313| N/A|   4,696|
| |Randolph County|     1| 40.407| N/A|    60|  2424.438| N/A|  24,748|
| |Callaway County|     1| 22.350| N/A|   133|  2972.532| N/A|  44,743|
| |Caldwell County|     1| 110.865| N/A|    36|  3991.131| N/A|   9,020|
| |Dallas County|     1| 59.249| N/A|    53|  3140.182| N/A|  16,878|
| |Christian County|     1| 11.287| N/A|   311|  3510.356| N/A|  88,595|
| |Carter County|     1| 167.168| N/A|    20|  3343.363| N/A|   5,982|
| |Nodaway County|     0|  0.000| N/A|   168|  7604.563| N/A|  22,092|
| |Iron County|     0|  0.000| N/A|    22|  2172.840| N/A|  10,125|
| |Clark County|     0|  0.000| N/A|    15|  2206.856| N/A|   6,797|
| |Clinton County|     0|  0.000| N/A|    68|  3335.459| N/A|  20,387|
| |Cooper County|     0|  0.000| N/A|   107|  6042.125| N/A|  17,709|
| |Mississippi County|     0|  0.000| N/A|   133| 10091.047| N/A|  13,180|
| |Miller County|     0|  0.000| N/A|   109|  4254.655| N/A|  25,619|
| |Mercer County|     0|  0.000| N/A|    11|  3041.194| N/A|   3,617|
| |Maries County|     0|  0.000| N/A|    18|  2069.679| N/A|   8,697|
| |Madison County|     0|  0.000| N/A|    18|  1489.080| N/A|  12,088|
| |Macon County|     0|  0.000| N/A|    55|  3638.288| N/A|  15,117|
| |Livingston County|     0|  0.000| N/A|    53|  3480.659| N/A|  15,227|
| |Knox County|     0|  0.000| N/A|    24|  6062.137| N/A|   3,959|
| |Howard County|     0|  0.000| N/A|    47|  4699.530| N/A|  10,001|
| |Holt County|     0|  0.000| N/A|     6|  1362.707| N/A|   4,403|
| |Hickory County|     0|  0.000| N/A|    21|  2200.335| N/A|   9,544|
| |Gasconade County|     0|  0.000| N/A|    20|  1359.989| N/A|  14,706|
| |Dent County|     0|  0.000| N/A|     9|   577.923| N/A|  15,573|
| |Daviess County|     0|  0.000| N/A|    17|  2053.636| N/A|   8,278|
| |Dade County|     0|  0.000| N/A|    15|  1983.865| N/A|   7,561|
| |Crawford County|     0|  0.000| N/A|    62|  2591.973| N/A|  23,920|
| |Chariton County|     0|  0.000| N/A|    16|  2154.592| N/A|   7,426|
| |Shelby County|     0|  0.000| N/A|    29|  4890.388| N/A|   5,930|
| |St. Louis city|     0|  0.000| N/A|     0|     0.000| N/A| 300,576|
| |Wright County|     0|  0.000| N/A|    58|  3171.305| N/A|  18,289|
| |Worth County|     0|  0.000| N/A|     9|  4470.939| N/A|   2,013|
| |Wayne County|     0|  0.000| N/A|    45|  3495.689| N/A|  12,873|
| |Warren County|     0|  0.000| N/A|   185|  5189.486| N/A|  35,649|
| |Bollinger County|     0|  0.000| N/A|    59|  4862.771| N/A|  12,133|
| |Montgomery County|     0|  0.000| N/A|    41|  3549.476| N/A|  11,551|
| |Cedar County|     0|  0.000| N/A|    36|  2508.886| N/A|  14,349|
| |Carroll County|     0|  0.000| N/A|    99| 11406.844| N/A|   8,679|
| |Barton County|     0|  0.000| N/A|    66|  5615.110| N/A|  11,754|
| |Vernon County|     0|  0.000| N/A|    47|  2285.659| N/A|  20,563|
| |Atchison County|     0|  0.000| N/A|    14|  2722.147| N/A|   5,143|
| |Adair County|     0|  0.000| N/A|   143|  5642.584| N/A|  25,343|
| |Monroe County|     0|  0.000| N/A|    24|  2776.492| N/A|   8,644|
| |Texas County|     0|  0.000| N/A|    45|  1771.793| N/A|  25,398|
| |Sullivan County|     0|  0.000| N/A|   139| 22828.051| N/A|   6,089|
| |Schuyler County|     0|  0.000| N/A|     9|  1931.330| N/A|   4,660|
| |Morgan County|     0|  0.000| N/A|    74|  3587.531| N/A|  20,627|
| |St. Clair County|     0|  0.000| N/A|    19|  2021.922| N/A|   9,397|
| |Ripley County|     0|  0.000| N/A|    47|  3537.026| N/A|  13,288|
| |Reynolds County|     0|  0.000| N/A|    16|  2551.834| N/A|   6,270|
| |Ralls County|     0|  0.000| N/A|    25|  2425.065| N/A|  10,309|
| |Polk County|     0|  0.000| N/A|   196|  6096.613| N/A|  32,149|
| |Phelps County|     0|  0.000| N/A|    79|  1772.373| N/A|  44,573|
| |Ozark County|     0|  0.000| N/A|     8|   872.030| N/A|   9,174|
| |Oregon County|     0|  0.000| N/A|    14|  1329.661| N/A|  10,529|
| |Ray County|     0|  0.000| N/A|   110|  4778.869| N/A|  23,018|


### Tennessee ###

![Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Tennessee.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|TN|95 counties| 1,125| 164.734| N/A|108,377| 15869.708| N/A|6,829,174|
| |Shelby County|   298| 317.980|  5.001|21,924| 23393.934| 226.918| 937,166|
| |Davidson County|   208| 299.650|  4.322|19,812| 28541.628| 267.070| 694,144|
| |Sumner County|    71| 371.178|  3.006| 3,264| 17063.722| 201.749| 191,283|
| |Rutherford County|    53| 159.502|  0.913| 6,254| 18821.193| 243.515| 332,285|
| |Hamilton County|    47| 127.785|  0.000| 5,803| 15777.425| 180.177| 367,804|
| |Knox County|    38| 80.797|  2.459| 4,186|  8900.456| 174.396| 470,313|
| |Wilson County|    23| 158.997|  6.913| 2,152| 14876.570| 239.585| 144,657|
| |Williamson County|    22| 92.277|  0.000| 3,363| 14105.834| 163.582| 238,412|
| |McMinn County|    20| 371.789|  0.000|   498|  9257.538| 185.894|  53,794|
| |Robertson County|    19| 264.576| 14.081| 1,475| 20539.457| 174.063|  71,813|
| |Madison County|    14| 142.880| 10.206|   957|  9766.901| 229.785|  97,984|
| |Putnam County|    13| 162.004|  0.000| 1,646| 20512.181| 475.033|  80,245|
| |Montgomery County|    13| 62.203|  2.392| 1,781|  8521.817| 112.444| 208,993|
| |Macon County|    13| 528.412|  0.000|   847| 34428.095| 184.034|  24,602|
| |Hamblen County|    13| 200.203|  0.000| 1,311| 20189.731| 458.366|  64,934|
| |Giles County|    12| 407.277| 42.426|   360| 12218.300| 166.225|  29,464|
| |Bradley County|    12| 110.998|  0.000| 1,771| 16381.463| 237.542| 108,110|
| |Hardeman County|    12| 479.042|  0.000|   843| 33652.695| 739.985|  25,050|
| |Sullivan County|    11| 69.467|  5.254|   859|  5424.761| 166.894| 158,348|
| |Bedford County|    11| 221.270|  0.000|   890| 17902.762| 181.039|  49,713|
| |Tipton County|     9| 146.106| N/A| 1,137| 18458.092| N/A|  61,599|
| |Monroe County|     9| 193.361| N/A|   380|  8164.142| N/A|  46,545|
| |Fayette County|     8| 194.491| N/A|   646| 15705.152| N/A|  41,133|
| |Blount County|     8| 60.111| N/A| 1,186|  8911.397| N/A| 133,088|
| |Maury County|     7| 72.624| N/A| 1,107| 11484.951| N/A|  96,387|
| |Dyer County|     7| 188.380| N/A|   579| 15581.689| N/A|  37,159|
| |Hardin County|     7| 272.883| N/A|   426| 16606.892| N/A|  25,652|
| |Lauderdale County|     7| 273.085| N/A|   445| 17360.434| N/A|  25,633|
| |Sevier County|     6| 61.069| N/A| 1,763| 17944.020| N/A|  98,250|
| |Lawrence County|     6| 135.925| N/A|   497| 11259.118| N/A|  44,142|
| |Cumberland County|     6| 99.141| N/A|   397|  6559.815| N/A|  60,520|
| |Trousdale County|     6| 531.726| N/A| 1,576| 139666.785| N/A|  11,284|
| |Cheatham County|     6| 147.540| N/A|   554| 13622.839| N/A|  40,667|
| |Greene County|     6| 86.870| N/A|   398|  5762.354| N/A|  69,069|
| |Anderson County|     6| 77.944| N/A|   637|  8275.092| N/A|  76,978|
| |Carter County|     5| 88.667| N/A|   452|  8015.463| N/A|  56,391|
| |McNairy County|     5| 194.598| N/A|   335| 13038.063| N/A|  25,694|
| |Hawkins County|     5| 88.050| N/A|   391|  6885.500| N/A|  56,786|
| |Haywood County|     5| 288.951| N/A|   414| 23925.104| N/A|  17,304|
| |Franklin County|     4| 94.769| N/A|   296|  7012.889| N/A|  42,208|
| |Crockett County|     4| 281.096| N/A|   246| 17287.421| N/A|  14,230|
| |Obion County|     4| 133.027| N/A|   464| 15431.175| N/A|  30,069|
| |Marion County|     4| 138.375| N/A|   210|  7264.676| N/A|  28,907|
| |Warren County|     4| 96.906| N/A|   454| 10998.861| N/A|  41,277|
| |Jefferson County|     3| 55.051| N/A|   513|  9413.708| N/A|  54,495|
| |Polk County|     3| 178.232| N/A|   181| 10753.327| N/A|  16,832|
| |Smith County|     3| 148.832| N/A|   393| 19496.949| N/A|  20,157|
| |Loudon County|     3| 55.486| N/A|   686| 12687.727| N/A|  54,068|
| |Marshall County|     3| 87.273| N/A|   271|  7883.636| N/A|  34,375|
| |Carroll County|     3| 108.042| N/A|   251|  9039.507| N/A|  27,767|
| |White County|     3| 109.709| N/A|   232|  8484.184| N/A|  27,345|
| |Weakley County|     3| 90.014| N/A|   329|  9871.579| N/A|  33,328|
| |Humphreys County|     3| 161.447| N/A|   113|  6081.154| N/A|  18,582|
| |Wayne County|     2| 119.954| N/A|   222| 13314.940| N/A|  16,673|
| |Washington County|     2| 15.459| N/A| 1,114|  8610.628| N/A| 129,375|
| |Decatur County|     2| 171.482| N/A|   174| 14918.975| N/A|  11,663|
| |Coffee County|     2| 35.386| N/A|   448|  7926.398| N/A|  56,520|
| |Gibson County|     2| 40.706| N/A|   615| 12517.046| N/A|  49,133|
| |Cocke County|     2| 55.549| N/A|   421| 11693.145| N/A|  36,004|
| |Chester County|     2| 115.627| N/A|   201| 11620.512| N/A|  17,297|
| |Roane County|     2| 37.466| N/A|   398|  7455.697| N/A|  53,382|
| |Grundy County|     2| 148.954| N/A|   104|  7745.587| N/A|  13,427|
| |Hancock County|     1| 151.057| N/A|    76| 11480.363| N/A|   6,620|
| |Morgan County|     1| 46.722| N/A|    94|  4391.908| N/A|  21,403|
| |DeKalb County|     1| 48.804| N/A|   326| 15910.200| N/A|  20,490|
| |Overton County|     1| 44.962| N/A|   141|  6339.643| N/A|  22,241|
| |Dickson County|     1| 18.536| N/A|   630| 11677.912| N/A|  53,948|
| |Benton County|     1| 61.881| N/A|   111|  6868.812| N/A|  16,160|
| |Bledsoe County|     1| 66.383| N/A|   674| 44742.432| N/A|  15,064|
| |Campbell County|     1| 25.099| N/A|   224|  5622.208| N/A|  39,842|
| |Lewis County|     1| 81.513| N/A|    62|  5053.799| N/A|  12,268|
| |Lincoln County|     1| 29.099| N/A|   259|  7536.519| N/A|  34,366|
| |Jackson County|     1| 84.846| N/A|   109|  9248.261| N/A|  11,786|
| |Pickett County|     1| 198.098| N/A|    27|  5348.653| N/A|   5,048|
| |Rhea County|     1| 30.150| N/A|   514| 15497.332| N/A|  33,167|
| |Claiborne County|     0|  0.000| N/A|   235|  7353.171| N/A|  31,959|
| |Cannon County|     0|  0.000| N/A|   131|  8924.922| N/A|  14,678|
| |Clay County|     0|  0.000| N/A|    66|  8667.104| N/A|   7,615|
| |Unicoi County|     0|  0.000| N/A|   141|  7884.583| N/A|  17,883|
| |Union County|     0|  0.000| N/A|   133|  6659.323| N/A|  19,972|
| |Van Buren County|     0|  0.000| N/A|    33|  5619.891| N/A|   5,872|
| |Fentress County|     0|  0.000| N/A|    76|  4103.007| N/A|  18,523|
| |Stewart County|     0|  0.000| N/A|    72|  5249.727| N/A|  13,715|
| |Henry County|     0|  0.000| N/A|   231|  7141.753| N/A|  32,345|
| |Houston County|     0|  0.000| N/A|    54|  6584.563| N/A|   8,201|
| |Hickman County|     0|  0.000| N/A|   240|  9532.131| N/A|  25,178|
| |Scott County|     0|  0.000| N/A|   105|  4758.021| N/A|  22,068|
| |Sequatchie County|     0|  0.000| N/A|    96|  6388.926| N/A|  15,026|
| |Perry County|     0|  0.000| N/A|    77|  9534.423| N/A|   8,076|
| |Lake County|     0|  0.000| N/A|   758| 108038.769| N/A|   7,016|
| |Johnson County|     0|  0.000| N/A|   214| 12030.582| N/A|  17,788|
| |Henderson County|     0|  0.000| N/A|   483| 17178.220| N/A|  28,117|
| |Grainger County|     0|  0.000| N/A|   181|  7761.578| N/A|  23,320|
| |Meigs County|     0|  0.000| N/A|    99|  7969.731| N/A|  12,422|
| |Moore County|     0|  0.000| N/A|    53|  8168.927| N/A|   6,488|


### Wisconsin ###

![Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wisconsin.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WI|72 counties|   970| 166.597| N/A|56,940|  9779.415| N/A|5,822,434|
| |Milwaukee County|   450| 475.825|  1.766|20,175| 21332.817| 164.109| 945,726|
| |Racine County|    78| 397.329|  5.094| 3,343| 17029.102| 165.971| 196,311|
| |Kenosha County|    58| 342.060| 12.596| 2,561| 15103.709| 176.188| 169,561|
| |Waukesha County|    57| 141.020|  2.114| 3,841|  9502.768| 188.027| 404,198|
| |Brown County|    52| 196.566|  1.590| 4,100| 15498.484| 118.734| 264,542|
| |Dane County|    37| 67.679|  0.000| 4,340|  7938.613| 58.534| 546,695|
| |Rock County|    26| 159.164|  0.000| 1,382|  8460.154| 33.185| 163,354|
| |Washington County|    22| 161.724|  0.000|   945|  6946.793| 196.231| 136,034|
| |Walworth County|    21| 202.180|  0.000| 1,291| 12429.237| 202.180| 103,868|
| |Winnebago County|    18| 104.708|  0.913| 1,094|  6363.906| 79.386| 171,907|
| |Ozaukee County|    17| 190.538|  0.000|   605|  6780.915| 161.713|  89,221|
| |Waupaca County|    15| 294.175|  0.000|   408|  8001.569| 266.651|  50,990|
| |Grant County|    14| 272.167|  0.000|   332|  6454.247| 28.623|  51,439|
| |Outagamie County|    13| 69.191|  0.000| 1,158|  6163.345| 110.948| 187,885|
| |Sheboygan County|     8| 69.360| N/A|   682|  5912.953| N/A| 115,340|
| |Clark County|     7| 201.300| N/A|   179|  5147.524| N/A|  34,774|
| |Marathon County|     7| 51.587| N/A|   605|  4458.627| N/A| 135,692|
| |Fond du Lac County|     6| 58.025| N/A|   584|  5647.805| N/A| 103,403|
| |Jefferson County|     5| 58.984| N/A|   581|  6853.921| N/A|  84,769|
| |Dodge County|     5| 56.922| N/A|   743|  8458.657| N/A|  87,839|
| |Eau Claire County|     4| 38.224| N/A|   531|  5074.250| N/A| 104,646|
| |Richland County|     4| 231.857| N/A|    34|  1970.786| N/A|  17,252|
| |Forest County|     4| 444.247| N/A|    59|  6552.643| N/A|   9,004|
| |Sauk County|     3| 46.553| N/A|   411|  6377.828| N/A|  64,442|
| |Door County|     3| 108.429| N/A|    98|  3541.998| N/A|  27,668|
| |Marinette County|     3| 74.349| N/A|   350|  8674.102| N/A|  40,350|
| |Barron County|     3| 66.307| N/A|   273|  6033.949| N/A|  45,244|
| |Polk County|     2| 45.680| N/A|   126|  2877.829| N/A|  43,783|
| |Trempealeau County|     2| 67.456| N/A|   322| 10860.400| N/A|  29,649|
| |Monroe County|     2| 43.240| N/A|   234|  5059.131| N/A|  46,253|
| |St. Croix County|     2| 22.054| N/A|   470|  5182.661| N/A|  90,687|
| |Kewaunee County|     2| 97.876| N/A|   115|  5627.875| N/A|  20,434|
| |Buffalo County|     2| 153.480| N/A|    42|  3223.083| N/A|  13,031|
| |Calumet County|     2| 39.929| N/A|   276|  5510.192| N/A|  50,089|
| |Adams County|     2| 98.912| N/A|    79|  3907.023| N/A|  20,220|
| |Columbia County|     1| 17.382| N/A|   233|  4049.920| N/A|  57,532|
| |Burnett County|     1| 64.876| N/A|    21|  1362.398| N/A|  15,414|
| |Wood County|     1| 13.699| N/A|   263|  3602.789| N/A|  72,999|
| |Bayfield County|     1| 66.507| N/A|    21|  1396.648| N/A|  15,036|
| |Ashland County|     1| 64.259| N/A|    21|  1349.441| N/A|  15,562|
| |Manitowoc County|     1| 12.661| N/A|   318|  4026.285| N/A|  78,981|
| |Juneau County|     1| 37.471| N/A|   133|  4983.700| N/A|  26,687|
| |Green County|     1| 27.056| N/A|   135|  3652.597| N/A|  36,960|
| |Marquette County|     1| 64.210| N/A|    75|  4815.719| N/A|  15,574|
| |Iron County|     1| 175.840| N/A|    73| 12836.293| N/A|   5,687|
| |Jackson County|     1| 48.443| N/A|    50|  2422.129| N/A|  20,643|
| |Langlade County|     1| 52.113| N/A|    51|  2657.773| N/A|  19,189|
| |La Crosse County|     1|  8.473| N/A|   854|  7236.307| N/A| 118,016|
| |Rusk County|     1| 70.532| N/A|    16|  1128.509| N/A|  14,178|
| |Oneida County|     0|  0.000| N/A|    96|  2697.008| N/A|  35,595|
| |Pepin County|     0|  0.000| N/A|    42|  5763.689| N/A|   7,287|
| |Sawyer County|     0|  0.000| N/A|    50|  3019.688| N/A|  16,558|
| |Price County|     0|  0.000| N/A|    25|  1872.519| N/A|  13,351|
| |Portage County|     0|  0.000| N/A|   367|  5185.667| N/A|  70,772|
| |Pierce County|     0|  0.000| N/A|   183|  4280.301| N/A|  42,754|
| |Lafayette County|     0|  0.000| N/A|   114|  6840.684| N/A|  16,665|
| |Oconto County|     0|  0.000| N/A|   200|  5272.871| N/A|  37,930|
| |Iowa County|     0|  0.000| N/A|    68|  2871.864| N/A|  23,678|
| |Menominee County|     0|  0.000| N/A|    20|  4389.816| N/A|   4,556|
| |Lincoln County|     0|  0.000| N/A|    66|  2391.911| N/A|  27,593|
| |Florence County|     0|  0.000| N/A|     6|  1396.973| N/A|   4,295|
| |Chippewa County|     0|  0.000| N/A|   213|  3294.256| N/A|  64,658|
| |Green Lake County|     0|  0.000| N/A|    54|  2855.179| N/A|  18,913|
| |Dunn County|     0|  0.000| N/A|   112|  2468.700| N/A|  45,368|
| |Douglas County|     0|  0.000| N/A|   145|  3360.371| N/A|  43,150|
| |Crawford County|     0|  0.000| N/A|    69|  4277.478| N/A|  16,131|
| |Taylor County|     0|  0.000| N/A|    59|  2900.261| N/A|  20,343|
| |Vernon County|     0|  0.000| N/A|    59|  1914.217| N/A|  30,822|
| |Waushara County|     0|  0.000| N/A|   112|  4582.089| N/A|  24,443|
| |Washburn County|     0|  0.000| N/A|    39|  2480.916| N/A|  15,720|
| |Vilas County|     0|  0.000| N/A|    40|  1802.208| N/A|  22,195|
| |Shawano County|     0|  0.000| N/A|   168|  4107.680| N/A|  40,899|


### Iowa ###

![Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Iowa.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|IA|99 counties|   900| 285.255| N/A|46,832| 14843.411| N/A|3,155,070|
| |Polk County|   204| 416.190|  2.040| 9,874| 20144.402| 141.220| 490,161|
| |Linn County|    87| 383.757|  0.000| 2,198|  9695.376| 178.893| 226,706|
| |Black Hawk County|    62| 472.460|  0.000| 3,054| 23272.472| 243.850| 131,228|
| |Woodbury County|    51| 494.632|  1.521| 3,673| 35623.188| 106.685| 103,107|
| |Muscatine County|    48| 1125.070|  0.000|   839| 19665.292| 137.145|  42,664|
| |Dallas County|    35| 374.520|  0.000| 1,807| 19335.923| 96.305|  93,453|
| |Wapello County|    33| 943.693| 16.381|   866| 24764.792| 114.387|  34,969|
| |Dubuque County|    31| 318.566|  8.549| 1,594| 16380.471| 292.875|  97,311|
| |Tama County|    29| 1720.660|  0.000|   543| 32217.871| 152.007|  16,854|
| |Marshall County|    25| 635.017| 10.495| 1,407| 35738.779| 216.716|  39,369|
| |Jasper County|    25| 672.314|  0.000|   458| 12316.794| 38.553|  37,185|
| |Pottawattamie County|    24| 257.494|  4.631| 1,257| 13486.256| 53.645|  93,206|
| |Mahaska County|    17| 769.405|  0.000|   137|  6200.498| 18.933|  22,095|
| |Cerro Gordo County|    17| 400.471|  0.000|   586| 13804.476| 81.046|  42,450|
| |Johnson County|    16| 105.862|  2.734| 2,002| 13245.997| 208.253| 151,140|
| |Story County|    14| 144.156|  1.615| 1,126| 11594.263| 72.477|  97,117|
| |Louisa County|    14| 1268.691|  0.000|   379| 34345.265| 13.202|  11,035|
| |Scott County|    13| 75.169|  0.000| 1,636|  9459.764| 106.323| 172,943|
| |Buena Vista County|    12| 611.621|  0.000| 1,790| 91233.435| 131.995|  19,620|
| |Washington County|    10| 455.270|  0.000|   288| 13111.769| 19.618|  21,965|
| |Plymouth County|     8| 317.750| N/A|   448| 17794.018| N/A|  25,177|
| |Poweshiek County|     8| 432.339| N/A|   151|  8160.398| N/A|  18,504|
| |Franklin County|     8| 794.439| N/A|   227| 22542.205| N/A|  10,070|
| |Webster County|     7| 194.964| N/A|   763| 21251.114| N/A|  35,904|
| |Monroe County|     7| 908.265| N/A|    70|  9082.652| N/A|   7,707|
| |Bremer County|     7| 279.307| N/A|   196|  7820.605| N/A|  25,062|
| |Guthrie County|     5| 467.771| N/A|   128| 11974.927| N/A|  10,689|
| |Montgomery County|     4| 403.348| N/A|    45|  4537.663| N/A|   9,917|
| |Lucas County|     4| 465.116| N/A|    53|  6162.791| N/A|   8,600|
| |Dickinson County|     4| 231.777| N/A|   378| 21902.886| N/A|  17,258|
| |Allamakee County|     4| 292.248| N/A|   152| 11105.429| N/A|  13,687|
| |Clinton County|     3| 64.615| N/A|   338|  7279.933| N/A|  46,429|
| |Clayton County|     3| 170.950| N/A|   101|  5755.314| N/A|  17,549|
| |Clarke County|     3| 319.319| N/A|   190| 20223.523| N/A|   9,395|
| |Appanoose County|     3| 241.429| N/A|    43|  3460.486| N/A|  12,426|
| |Crawford County|     3| 178.359| N/A|   726| 43162.901| N/A|  16,820|
| |Henry County|     3| 150.346| N/A|   114|  5713.140| N/A|  19,954|
| |Lee County|     3| 89.135| N/A|    99|  2941.439| N/A|  33,657|
| |Jones County|     2| 96.707| N/A|   126|  6092.549| N/A|  20,681|
| |Hancock County|     2| 188.147| N/A|   117| 11006.585| N/A|  10,630|
| |Emmet County|     2| 217.202| N/A|   185| 20091.225| N/A|   9,208|
| |Floyd County|     2| 127.861| N/A|   132|  8438.819| N/A|  15,642|
| |Madison County|     2| 122.414| N/A|   107|  6549.149| N/A|  16,338|
| |Calhoun County|     2| 206.868| N/A|    82|  8481.589| N/A|   9,668|
| |Sioux County|     2| 57.381| N/A|   607| 17415.005| N/A|  34,855|
| |Des Moines County|     2| 51.325| N/A|   143|  3669.772| N/A|  38,967|
| |Butler County|     2| 138.514| N/A|   118|  8172.311| N/A|  14,439|
| |Boone County|     2| 76.237| N/A|   234|  8919.722| N/A|  26,234|
| |Cass County|     1| 77.906| N/A|    48|  3739.483| N/A|  12,836|
| |Van Buren County|     1| 141.965| N/A|    34|  4826.803| N/A|   7,044|
| |Davis County|     1| 111.111| N/A|    51|  5666.667| N/A|   9,000|
| |Grundy County|     1| 81.753| N/A|    76|  6213.211| N/A|  12,232|
| |Carroll County|     1| 49.591| N/A|   183|  9075.130| N/A|  20,165|
| |Cherokee County|     1| 89.008| N/A|    99|  8811.749| N/A|  11,235|
| |Hamilton County|     1| 67.691| N/A|   243| 16448.927| N/A|  14,773|
| |Humboldt County|     1| 104.624| N/A|    94|  9834.693| N/A|   9,558|
| |Iowa County|     1| 61.789| N/A|    94|  5808.206| N/A|  16,184|
| |Jackson County|     1| 51.443| N/A|   146|  7510.674| N/A|  19,439|
| |Keokuk County|     1| 97.599| N/A|    31|  3025.571| N/A|  10,246|
| |Winneshiek County|     1| 50.023| N/A|    90|  4502.026| N/A|  19,991|
| |Warren County|     1| 19.430| N/A|   542| 10531.224| N/A|  51,466|
| |Audubon County|     1| 181.951| N/A|    28|  5094.614| N/A|   5,496|
| |Benton County|     1| 38.994| N/A|   145|  5654.124| N/A|  25,645|
| |Cedar County|     1| 53.686| N/A|   123|  6603.318| N/A|  18,627|
| |Wayne County|     1| 155.255| N/A|    19|  2949.853| N/A|   6,441|
| |Clay County|     1| 62.438| N/A|   174| 10864.136| N/A|  16,016|
| |Buchanan County|     1| 47.226| N/A|   118|  5572.609| N/A|  21,175|
| |Wright County|     1| 79.605| N/A|   451| 35901.926| N/A|  12,562|
| |Union County|     1| 81.693| N/A|    74|  6045.258| N/A|  12,241|
| |Shelby County|     1| 87.306| N/A|   176| 15365.811| N/A|  11,454|
| |Delaware County|     1| 58.785| N/A|    94|  5525.836| N/A|  17,011|
| |Ringgold County|     1| 204.332| N/A|    21|  4290.969| N/A|   4,894|
| |Pocahontas County|     1| 151.080| N/A|   114| 17223.145| N/A|   6,619|
| |O'Brien County|     1| 72.711| N/A|   132|  9597.906| N/A|  13,753|
| |Jefferson County|     0|  0.000| N/A|    77|  4208.800| N/A|  18,295|
| |Marion County|     0|  0.000| N/A|   159|  4781.523| N/A|  33,253|
| |Lyon County|     0|  0.000| N/A|   108|  9187.580| N/A|  11,755|
| |Kossuth County|     0|  0.000| N/A|    82|  5535.678| N/A|  14,813|
| |Ida County|     0|  0.000| N/A|    29|  4227.405| N/A|   6,860|
| |Howard County|     0|  0.000| N/A|    49|  5350.513| N/A|   9,158|
| |Harrison County|     0|  0.000| N/A|    99|  7046.765| N/A|  14,049|
| |Hardin County|     0|  0.000| N/A|   171| 10150.778| N/A|  16,846|
| |Greene County|     0|  0.000| N/A|    38|  4275.428| N/A|   8,888|
| |Fremont County|     0|  0.000| N/A|    34|  4885.057| N/A|   6,960|
| |Fayette County|     0|  0.000| N/A|    81|  4122.137| N/A|  19,650|
| |Decatur County|     0|  0.000| N/A|    23|  2922.490| N/A|   7,870|
| |Chickasaw County|     0|  0.000| N/A|    52|  4357.664| N/A|  11,933|
| |Adams County|     0|  0.000| N/A|    16|  4441.977| N/A|   3,602|
| |Adair County|     0|  0.000| N/A|    23|  3215.884| N/A|   7,152|
| |Mills County|     0|  0.000| N/A|    85|  5625.786| N/A|  15,109|
| |Osceola County|     0|  0.000| N/A|    78| 13091.641| N/A|   5,958|
| |Monona County|     0|  0.000| N/A|    91| 10562.972| N/A|   8,615|
| |Mitchell County|     0|  0.000| N/A|    78|  7368.222| N/A|  10,586|
| |Worth County|     0|  0.000| N/A|    64|  8670.912| N/A|   7,381|
| |Winnebago County|     0|  0.000| N/A|    76|  7340.158| N/A|  10,354|
| |Taylor County|     0|  0.000| N/A|    94| 15356.968| N/A|   6,121|
| |Sac County|     0|  0.000| N/A|    81|  8332.476| N/A|   9,721|
| |Palo Alto County|     0|  0.000| N/A|    80|  9002.926| N/A|   8,886|
| |Page County|     0|  0.000| N/A|    77|  5096.975| N/A|  15,107|


### Nevada ###

![Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nevada.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NV|17 counties|   882| 286.349| N/A|52,503| 17045.565| N/A|3,080,156|
| |Clark County|   744| 328.228|  9.265|45,563| 20100.895| 341.763|2,266,715|
| |Washoe County|   115| 243.893|  0.331| 5,426| 11507.490| 89.431| 471,519|
| |Nye County|     9| 193.453| N/A|   362|  7781.098| N/A|  46,523|
| |Lyon County|     5| 86.941| N/A|   215|  3738.480| N/A|  57,510|
| |Humboldt County|     4| 237.657| N/A|    96|  5703.761| N/A|  16,831|
| |Elko County|     2| 37.895| N/A|   505|  9568.381| N/A|  52,778|
| |Lander County|     1| 180.766| N/A|    50|  9038.322| N/A|   5,532|
| |White Pine County|     1| 104.384| N/A|    14|  1461.378| N/A|   9,580|
| |Churchill County|     1| 40.146| N/A|    49|  1967.160| N/A|  24,909|
| |Mineral County|     0|  0.000| N/A|    11|  2441.731| N/A|   4,505|
| |Lincoln County|     0|  0.000| N/A|     4|   771.754| N/A|   5,183|
| |Eureka County|     0|  0.000| N/A|     2|   985.707| N/A|   2,029|
| |Esmeralda County|     0|  0.000| N/A|     0|     0.000| N/A|     873|
| |Douglas County|     0|  0.000| N/A|   189|  3864.636| N/A|  48,905|
| |Pershing County|     0|  0.000| N/A|    13|  1933.086| N/A|   6,725|
| |Carson City|     0|  0.000| N/A|     0|     0.000| N/A|  55,916|
| |Storey County|     0|  0.000| N/A|     4|   970.167| N/A|   4,123|


### Kentucky ###

![Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kentucky.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KY|120 counties|   752| 168.320| N/A|32,741|  7328.424| N/A|4,467,673|
| |Jefferson County|   236| 307.790|  1.234| 7,518|  9804.932| 180.674| 766,757|
| |Fayette County|    46| 142.348|  0.000| 2,910|  9005.050| 159.368| 323,152|
| |Kenton County|    38| 227.548|  0.000| 1,362|  8155.786| 65.869| 166,998|
| |Hopkins County|    33| 738.486|  0.000|   414|  9264.647| 104.650|  44,686|
| |Boone County|    24| 179.666|  0.000| 1,054|  7890.344| 98.322| 133,581|
| |Logan County|    23| 848.646| 36.898|   310| 11438.270| 130.355|  27,102|
| |Graves County|    22| 590.350|  0.000|   525| 14087.909| 171.226|  37,266|
| |Warren County|    22| 165.543|  0.000| 2,537| 19090.116| 180.592| 132,896|
| |Shelby County|    22| 448.760|  0.000|   725| 14788.675| 115.581|  49,024|
| |Adair County|    19| 989.480|  0.000|   204| 10623.893| 52.078|  19,202|
| |Butler County|    15| 1164.687|  0.000|   297| 23060.797| 101.160|  12,879|
| |Jackson County|    14| 1050.341|  0.000|   143| 10728.487|  0.000|  13,329|
| |Oldham County|    14| 209.584|  0.000|   586|  8772.586| 117.052|  66,799|
| |Campbell County|    13| 138.913|  0.000|   548|  5855.702| 86.801|  93,584|
| |Edmonson County|    12| 987.654|  0.000|    96|  7901.235| 54.030|  12,150|
| |Grayson County|    11| 416.241|  0.000|   187|  7076.096| 107.808|  26,427|
| |Muhlenberg County|    10| 326.563|  0.000|   622| 20312.194| 135.211|  30,622|
| |Casey County|    10| 618.850|  0.000|   157|  9715.948| 80.098|  16,159|
| |Knox County|     8| 256.863| N/A|   222|  7127.950| N/A|  31,145|
| |Hardin County|     8| 72.099| N/A|   553|  4983.868| N/A| 110,958|
| |Gallatin County|     8| 902.018| N/A|    79|  8907.430| N/A|   8,869|
| |Allen County|     8| 375.323| N/A|   220| 10321.370| N/A|  21,315|
| |Daviess County|     8| 78.809| N/A|   735|  7240.595| N/A| 101,511|
| |Ohio County|     7| 291.740| N/A|   344| 14336.918| N/A|  23,994|
| |Clark County|     7| 193.034| N/A|   168|  4632.821| N/A|  36,263|
| |Simpson County|     7| 376.911| N/A|   145|  7807.452| N/A|  18,572|
| |Christian County|     6| 85.153| N/A|   481|  6826.471| N/A|  70,461|
| |Clay County|     5| 251.244| N/A|   145|  7286.066| N/A|  19,901|
| |Russell County|     5| 278.971| N/A|   100|  5579.423| N/A|  17,923|
| |Franklin County|     5| 98.057| N/A|   269|  5275.441| N/A|  50,991|
| |Grant County|     5| 199.450| N/A|   107|  4268.220| N/A|  25,069|
| |Henderson County|     4| 88.476| N/A|   330|  7299.270| N/A|  45,210|
| |McCracken County|     4| 61.145| N/A|   348|  5319.637| N/A|  65,418|
| |Lyon County|     4| 487.211| N/A|    32|  3897.686| N/A|   8,210|
| |Calloway County|     4| 102.561| N/A|   202|  5179.354| N/A|  39,001|
| |Laurel County|     4| 65.775| N/A|   397|  6528.209| N/A|  60,813|
| |Bullitt County|     4| 48.974| N/A|   329|  4028.111| N/A|  81,676|
| |Pike County|     3| 51.835| N/A|   233|  4025.848| N/A|  57,876|
| |Perry County|     3| 116.469| N/A|   200|  7764.578| N/A|  25,758|
| |Boyd County|     3| 64.215| N/A|   182|  3895.715| N/A|  46,718|
| |Harlan County|     3| 115.340| N/A|   214|  8227.605| N/A|  26,010|
| |Nelson County|     2| 43.259| N/A|   203|  4390.803| N/A|  46,233|
| |Carroll County|     2| 188.129| N/A|   148| 13921.550| N/A|  10,631|
| |Pulaski County|     2| 30.779| N/A|   263|  4047.461| N/A|  64,979|
| |Barren County|     2| 45.199| N/A|   352|  7954.982| N/A|  44,249|
| |Breckinridge County|     2| 97.671| N/A|    55|  2685.940| N/A|  20,477|
| |Henry County|     2| 124.023| N/A|   105|  6511.224| N/A|  16,126|
| |Bell County|     2| 76.829| N/A|   287| 11024.892| N/A|  26,032|
| |Monroe County|     2| 187.793| N/A|    90|  8450.704| N/A|  10,650|
| |Green County|     2| 182.799| N/A|    31|  2833.379| N/A|  10,941|
| |Floyd County|     2| 56.197| N/A|    89|  2500.773| N/A|  35,589|
| |Metcalfe County|     2| 198.590| N/A|    56|  5560.520| N/A|  10,071|
| |Taylor County|     2| 77.613| N/A|   105|  4074.663| N/A|  25,769|
| |Marshall County|     2| 64.309| N/A|   128|  4115.756| N/A|  31,100|
| |Meade County|     2| 69.999| N/A|    91|  3184.936| N/A|  28,572|
| |Mason County|     1| 58.582| N/A|    53|  3104.862| N/A|  17,070|
| |Fulton County|     1| 167.532| N/A|    69| 11559.725| N/A|   5,969|
| |McLean County|     1| 108.613| N/A|    41|  4453.133| N/A|   9,207|
| |Madison County|     1| 10.754| N/A|   426|  4581.286| N/A|  92,987|
| |Larue County|     1| 69.454| N/A|    52|  3611.613| N/A|  14,398|
| |Whitley County|     1| 27.576| N/A|   155|  4274.211| N/A|  36,264|
| |Webster County|     1| 77.268| N/A|    83|  6413.228| N/A|  12,942|
| |Crittenden County|     1| 113.559| N/A|    26|  2952.532| N/A|   8,806|
| |Carlisle County|     1| 210.084| N/A|    33|  6932.773| N/A|   4,760|
| |Bath County|     1| 80.000| N/A|    36|  2880.000| N/A|  12,500|
| |Bourbon County|     1| 50.536| N/A|    73|  3689.105| N/A|  19,788|
| |Greenup County|     1| 28.492| N/A|   102|  2906.148| N/A|  35,098|
| |Livingston County|     1| 108.767| N/A|    33|  3589.297| N/A|   9,194|
| |Knott County|     1| 67.540| N/A|    48|  3241.929| N/A|  14,806|
| |Carter County|     1| 37.318| N/A|    99|  3694.443| N/A|  26,797|
| |Anderson County|     1| 43.962| N/A|    80|  3516.947| N/A|  22,747|
| |Lincoln County|     1| 40.735| N/A|    99|  4032.751| N/A|  24,549|
| |Bracken County|     0|  0.000| N/A|    30|  3613.152| N/A|   8,303|
| |Union County|     0|  0.000| N/A|    58|  4033.099| N/A|  14,381|
| |Trimble County|     0|  0.000| N/A|    32|  3777.594| N/A|   8,471|
| |Trigg County|     0|  0.000| N/A|    53|  3617.501| N/A|  14,651|
| |Todd County|     0|  0.000| N/A|    34|  2765.577| N/A|  12,294|
| |Spencer County|     0|  0.000| N/A|   110|  5684.461| N/A|  19,351|
| |Scott County|     0|  0.000| N/A|   356|  6245.176| N/A|  57,004|
| |Rowan County|     0|  0.000| N/A|    69|  2820.932| N/A|  24,460|
| |Wayne County|     0|  0.000| N/A|    53|  2606.600| N/A|  20,333|
| |Washington County|     0|  0.000| N/A|    66|  5456.800| N/A|  12,095|
| |Wolfe County|     0|  0.000| N/A|    11|  1536.957| N/A|   7,157|
| |Nicholas County|     0|  0.000| N/A|    20|  2751.410| N/A|   7,269|
| |Lawrence County|     0|  0.000| N/A|    36|  2350.330| N/A|  15,317|
| |Montgomery County|     0|  0.000| N/A|   115|  4084.242| N/A|  28,157|
| |Mercer County|     0|  0.000| N/A|    80|  3647.472| N/A|  21,933|
| |Menifee County|     0|  0.000| N/A|    29|  4469.102| N/A|   6,489|
| |Martin County|     0|  0.000| N/A|    33|  2947.745| N/A|  11,195|
| |Magoffin County|     0|  0.000| N/A|    31|  2549.132| N/A|  12,161|
| |McCreary County|     0|  0.000| N/A|    37|  2147.293| N/A|  17,231|
| |Lewis County|     0|  0.000| N/A|    37|  2787.194| N/A|  13,275|
| |Letcher County|     0|  0.000| N/A|    53|  2459.054| N/A|  21,553|
| |Leslie County|     0|  0.000| N/A|    28|  2834.869| N/A|   9,877|
| |Lee County|     0|  0.000| N/A|     5|   675.402| N/A|   7,403|
| |Johnson County|     0|  0.000| N/A|    43|  1937.984| N/A|  22,188|
| |Woodford County|     0|  0.000| N/A|   142|  5311.588| N/A|  26,734|
| |Jessamine County|     0|  0.000| N/A|   318|  5876.374| N/A|  54,115|
| |Pendleton County|     0|  0.000| N/A|    41|  2810.144| N/A|  14,590|
| |Powell County|     0|  0.000| N/A|    50|  4045.635| N/A|  12,359|
| |Robertson County|     0|  0.000| N/A|     3|  1423.150| N/A|   2,108|
| |Rockcastle County|     0|  0.000| N/A|    61|  3653.789| N/A|  16,695|
| |Morgan County|     0|  0.000| N/A|    30|  2254.114| N/A|  13,309|
| |Owen County|     0|  0.000| N/A|    43|  3944.592| N/A|  10,901|
| |Garrard County|     0|  0.000| N/A|    71|  4019.020| N/A|  17,666|
| |Owsley County|     0|  0.000| N/A|    12|  2718.007| N/A|   4,415|
| |Fleming County|     0|  0.000| N/A|    57|  3909.197| N/A|  14,581|
| |Estill County|     0|  0.000| N/A|    18|  1276.053| N/A|  14,106|
| |Elliott County|     0|  0.000| N/A|     8|  1064.254| N/A|   7,517|
| |Cumberland County|     0|  0.000| N/A|    40|  6047.777| N/A|   6,614|
| |Clinton County|     0|  0.000| N/A|    27|  2642.396| N/A|  10,218|
| |Caldwell County|     0|  0.000| N/A|    49|  3844.042| N/A|  12,747|
| |Breathitt County|     0|  0.000| N/A|    28|  2216.944| N/A|  12,630|
| |Boyle County|     0|  0.000| N/A|   144|  4790.419| N/A|  30,060|
| |Ballard County|     0|  0.000| N/A|    31|  3930.020| N/A|   7,888|
| |Hickman County|     0|  0.000| N/A|    37|  8447.489| N/A|   4,380|
| |Marion County|     0|  0.000| N/A|   117|  6070.669| N/A|  19,273|
| |Hancock County|     0|  0.000| N/A|    49|  5617.978| N/A|   8,722|
| |Harrison County|     0|  0.000| N/A|   117|  6195.065| N/A|  18,886|
| |Hart County|     0|  0.000| N/A|    88|  4623.063| N/A|  19,035|


### New Mexico ###

![New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Mexico.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NM|33 counties|   667| 318.099| N/A|20,288|  9675.562| N/A|2,096,829|
| |McKinley County|   222| 3110.681|  5.950| 4,025| 56398.616| 28.024|  71,367|
| |San Juan County|   182| 1468.239|  0.000| 3,017| 24338.889| 48.470| 123,958|
| |Bernalillo County|   128| 188.479|  3.108| 4,989|  7346.261| 61.845| 679,121|
| |Sandoval County|    33| 224.875|  0.000| 1,111|  7570.802| 50.597| 146,748|
| |Dona Ana County|    27| 123.743|  6.525| 2,315| 10609.776| 163.260| 218,195|
| |Cibola County|    17| 637.301|  0.000|   345| 12933.458| 102.208|  26,675|
| |Otero County|    10| 148.170|  0.000|   195|  2889.317| 53.082|  67,490|
| |Chaves County|     6| 92.858| N/A|   395|  6113.132| N/A|  64,615|
| |Socorro County|     6| 360.642| N/A|    73|  4387.810| N/A|  16,637|
| |Rio Arriba County|     5| 128.465| N/A|   306|  7862.080| N/A|  38,921|
| |Eddy County|     4| 68.423| N/A|   269|  4601.437| N/A|  58,460|
| |Valencia County|     4| 52.159| N/A|   389|  5072.502| N/A|  76,688|
| |Lea County|     4| 56.283| N/A|   706|  9933.868| N/A|  71,070|
| |Santa Fe County|     3| 19.952| N/A|   610|  4056.984| N/A| 150,358|
| |Luna County|     3| 126.534| N/A|   240| 10122.738| N/A|  23,709|
| |Curry County|     2| 40.855| N/A|   506| 10336.234| N/A|  48,954|
| |Grant County|     2| 74.080| N/A|    70|  2592.785| N/A|  26,998|
| |Union County|     2| 492.732| N/A|    28|  6898.251| N/A|   4,059|
| |Colfax County|     1| 83.745| N/A|    15|  1256.176| N/A|  11,941|
| |Catron County|     1| 283.527| N/A|     4|  1134.108| N/A|   3,527|
| |Lincoln County|     1| 51.093| N/A|   113|  5773.554| N/A|  19,572|
| |Quay County|     1| 121.168| N/A|    34|  4119.714| N/A|   8,253|
| |Roosevelt County|     1| 54.054| N/A|   152|  8216.216| N/A|  18,500|
| |Taos County|     1| 30.560| N/A|   102|  3117.074| N/A|  32,723|
| |Torrance County|     1| 64.679| N/A|    60|  3880.732| N/A|  15,461|
| |Sierra County|     0|  0.000| N/A|    31|  2872.764| N/A|  10,791|
| |Guadalupe County|     0|  0.000| N/A|    31|  7209.302| N/A|   4,300|
| |San Miguel County|     0|  0.000| N/A|    42|  1539.759| N/A|  27,277|
| |Mora County|     0|  0.000| N/A|     6|  1327.140| N/A|   4,521|
| |Los Alamos County|     0|  0.000| N/A|    20|  1032.578| N/A|  19,369|
| |Hidalgo County|     0|  0.000| N/A|    88| 20962.363| N/A|   4,198|
| |Harding County|     0|  0.000| N/A|     1|  1600.000| N/A|     625|
| |De Baca County|     0|  0.000| N/A|     0|     0.000| N/A|   1,748|


### District of Columbia ###

![District of Columbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/District%20of%20Columbia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DC|1 counties|   587| 831.740| N/A|12,443| 17630.914| N/A| 705,749|
| |District of Columbia|   587| 831.740|  0.979|12,443| 17630.914| 134.873| 705,749|


### Delaware ###

![Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Delaware.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|DE|3 counties|   587| 602.815| N/A|15,058| 15463.706| N/A| 973,764|
| |New Castle County|   289| 517.223|  0.000| 7,042| 12603.064| 93.064| 558,753|
| |Sussex County|   191| 815.455|  0.000| 5,778| 24668.588| 224.143| 234,225|
| |Kent County|   107| 591.860|  0.000| 2,238| 12379.277| 66.893| 180,786|


### Oklahoma ###

![Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oklahoma.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OK|77 counties|   583| 147.335| N/A|40,555| 10249.001| N/A|3,956,971|
| |Oklahoma County|   107| 134.180|  0.000| 9,950| 12477.522| 286.514| 797,434|
| |Tulsa County|   103| 158.084|  1.270| 9,742| 14951.992| 400.074| 651,552|
| |Cleveland County|    54| 190.131|  7.042| 2,871| 10108.657| 227.727| 284,014|
| |Washington County|    39| 756.885|  0.000|   593| 11508.530| 77.629|  51,527|
| |McCurtain County|    28| 852.827| 38.036|   838| 25523.879| 130.418|  32,832|
| |Wagoner County|    22| 270.639|  0.000|   787|  9681.507| 260.782|  81,289|
| |Delaware County|    19| 441.768|  0.000|   405|  9416.634| 26.905|  43,009|
| |Rogers County|    16| 173.050|  8.628|   874|  9452.839| 205.496|  92,459|
| |Caddo County|    16| 556.290| 36.848|   384| 13350.949| 191.225|  28,762|
| |Muskogee County|    16| 235.304|  0.000|   480|  7059.135| 221.300|  67,997|
| |Creek County|    13| 181.762|  0.000|   536|  7494.198| 226.059|  71,522|
| |Kay County|    11| 252.653| 22.968|   231|  5305.710| 146.116|  43,538|
| |Osage County|    11| 234.227|  0.000|   385|  8197.943| 157.390|  46,963|
| |Comanche County|    10| 82.816|  0.000|   792|  6559.061| 57.971| 120,749|
| |Greer County|     8| 1400.560| N/A|    81| 14180.672| N/A|   5,712|
| |Pottawatomie County|     8| 110.205| N/A|   416|  5730.659| N/A|  72,592|
| |Texas County|     7| 350.298| N/A| 1,044| 52244.408| N/A|  19,983|
| |Grady County|     7| 125.372| N/A|   421|  7540.208| N/A|  55,834|
| |Canadian County|     6| 40.457| N/A| 1,128|  7605.896| N/A| 148,306|
| |Mayes County|     6| 145.985| N/A|   294|  7153.285| N/A|  41,100|
| |Adair County|     6| 270.343| N/A|   314| 14147.968| N/A|  22,194|
| |Jackson County|     5| 203.832| N/A|   497| 20260.905| N/A|  24,530|
| |Seminole County|     5| 206.118| N/A|   214|  8821.832| N/A|  24,258|
| |McClain County|     4| 98.829| N/A|   420| 10377.032| N/A|  40,474|
| |Payne County|     4| 48.909| N/A|   687|  8400.176| N/A|  81,784|
| |Garvin County|     4| 144.347| N/A|   215|  7758.652| N/A|  27,711|
| |Sequoyah County|     4| 96.226| N/A|   290|  6976.353| N/A|  41,569|
| |Garfield County|     4| 65.514| N/A|   389|  6371.200| N/A|  61,056|
| |Carter County|     4| 83.141| N/A|   315|  6547.359| N/A|  48,111|
| |Pittsburg County|     3| 68.722| N/A|   227|  5199.982| N/A|  43,654|
| |Pawnee County|     3| 183.195| N/A|   127|  7755.252| N/A|  16,376|
| |Okmulgee County|     3| 77.993| N/A|   411| 10685.038| N/A|  38,465|
| |Stephens County|     2| 46.357| N/A|   190|  4403.959| N/A|  43,143|
| |Ottawa County|     2| 64.253| N/A|   352| 11308.510| N/A|  31,127|
| |Pontotoc County|     2| 52.241| N/A|   186|  4858.426| N/A|  38,284|
| |Logan County|     2| 41.657| N/A|   196|  4082.398| N/A|  48,011|
| |Lincoln County|     2| 57.344| N/A|   147|  4214.812| N/A|  34,877|
| |Cotton County|     2| 352.983| N/A|    19|  3353.336| N/A|   5,666|
| |Cherokee County|     2| 41.104| N/A|   385|  7912.531| N/A|  48,657|
| |Noble County|     2| 179.678| N/A|    83|  7456.653| N/A|  11,131|
| |Beckham County|     1| 45.748| N/A|    45|  2058.649| N/A|  21,859|
| |Le Flore County|     1| 20.059| N/A|   277|  5556.336| N/A|  49,853|
| |Latimer County|     1| 99.275| N/A|    77|  7644.197| N/A|  10,073|
| |Kiowa County|     1| 114.837| N/A|    27|  3100.597| N/A|   8,708|
| |Hughes County|     1| 75.307| N/A|   118|  8886.211| N/A|  13,279|
| |Choctaw County|     1| 68.157| N/A|   171| 11654.853| N/A|  14,672|
| |Bryan County|     1| 20.836| N/A|   402|  8375.872| N/A|  47,995|
| |Tillman County|     1| 137.931| N/A|    57|  7862.069| N/A|   7,250|
| |Nowata County|     1| 99.246| N/A|    56|  5557.761| N/A|  10,076|
| |Major County|     1| 131.079| N/A|    26|  3408.048| N/A|   7,629|
| |McIntosh County|     1| 51.031| N/A|   160|  8164.932| N/A|  19,596|
| |Alfalfa County|     0|  0.000| N/A|     3|   526.131| N/A|   5,702|
| |Dewey County|     0|  0.000| N/A|     8|  1635.657| N/A|   4,891|
| |Custer County|     0|  0.000| N/A|   193|  6654.484| N/A|  29,003|
| |Craig County|     0|  0.000| N/A|    77|  5444.774| N/A|  14,142|
| |Coal County|     0|  0.000| N/A|    31|  5641.492| N/A|   5,495|
| |Cimarron County|     0|  0.000| N/A|     1|   467.946| N/A|   2,137|
| |Blaine County|     0|  0.000| N/A|    39|  4136.176| N/A|   9,429|
| |Beaver County|     0|  0.000| N/A|    36|  6778.384| N/A|   5,311|
| |Atoka County|     0|  0.000| N/A|    67|  4869.894| N/A|  13,758|
| |Ellis County|     0|  0.000| N/A|     3|   777.403| N/A|   3,859|
| |Grant County|     0|  0.000| N/A|    12|  2769.444| N/A|   4,333|
| |Harmon County|     0|  0.000| N/A|    27| 10177.158| N/A|   2,653|
| |Harper County|     0|  0.000| N/A|     9|  2440.347| N/A|   3,688|
| |Roger Mills County|     0|  0.000| N/A|     8|  2232.766| N/A|   3,583|
| |Woodward County|     0|  0.000| N/A|    35|  1731.730| N/A|  20,211|
| |Haskell County|     0|  0.000| N/A|    48|  3801.378| N/A|  12,627|
| |Woods County|     0|  0.000| N/A|    19|  2160.810| N/A|   8,793|
| |Washita County|     0|  0.000| N/A|    25|  2290.216| N/A|  10,916|
| |Pushmataha County|     0|  0.000| N/A|   101|  9102.379| N/A|  11,096|
| |Okfuskee County|     0|  0.000| N/A|    58|  4836.154| N/A|  11,993|
| |Murray County|     0|  0.000| N/A|    68|  4831.948| N/A|  14,073|
| |Marshall County|     0|  0.000| N/A|    99|  5847.262| N/A|  16,931|
| |Love County|     0|  0.000| N/A|    65|  6339.608| N/A|  10,253|
| |Kingfisher County|     0|  0.000| N/A|   114|  7231.208| N/A|  15,765|
| |Johnston County|     0|  0.000| N/A|    45|  4059.540| N/A|  11,085|
| |Jefferson County|     0|  0.000| N/A|    32|  5331.556| N/A|   6,002|


### Arkansas ###

![Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Arkansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|AR|75 counties|   508| 168.334| N/A|44,607| 14781.278| N/A|3,017,804|
| |Pulaski County|    81| 206.680|  2.552| 5,151| 13143.290| 140.338| 391,911|
| |Washington County|    50| 209.041|  5.930| 6,168| 25787.355| 213.431| 239,187|
| |Benton County|    40| 143.297|  1.509| 4,634| 16600.929| 111.055| 279,141|
| |Jefferson County|    40| 598.587|  8.607| 1,412| 21130.133| 247.200|  66,824|
| |Crittenden County|    20| 417.058|  0.000| 1,291| 26921.072| 526.200|  47,955|
| |Sebastian County|    17| 132.992|  6.508| 1,977| 15466.216| 473.296| 127,827|
| |Union County|    17| 439.481|  0.000|   458| 11840.132| 209.362|  38,682|
| |Yell County|    14| 656.014|  0.000| 1,052| 49294.785| 463.932|  21,341|
| |Hot Spring County|    12| 355.334| 59.222| 1,479| 43794.972| 211.889|  33,771|
| |Craighead County|    12| 108.763|  1.422| 1,196| 10840.010| 254.943| 110,332|
| |Mississippi County|    12| 295.196| 14.148|   891| 21918.280| 949.109|  40,651|
| |Lincoln County|    11| 844.595|  0.000| 1,196| 91830.467| 307.125|  13,024|
| |Pope County|    10| 156.074|  0.000| 1,266| 19759.021| 363.921|  64,072|
| |Sevier County|    10| 587.993|  0.000|   958| 56329.747| 510.918|  17,007|
| |Lawrence County|     9| 548.580| N/A|   191| 11642.082| N/A|  16,406|
| |Nevada County|     9| 1090.645| N/A|   134| 16238.488| N/A|   8,252|
| |Lee County|     8| 903.240| N/A|   890| 100485.492| N/A|   8,857|
| |Garland County|     8| 80.494| N/A|   910|  9156.219| N/A|  99,386|
| |Chicot County|     8| 790.670| N/A|   700| 69183.633| N/A|  10,118|
| |Phillips County|     7| 393.657| N/A|   298| 16758.520| N/A|  17,782|
| |Columbia County|     7| 298.418| N/A|   209|  8909.920| N/A|  23,457|
| |Carroll County|     7| 246.653| N/A|   346| 12191.684| N/A|  28,380|
| |Saline County|     6| 49.005| N/A|   949|  7750.925| N/A| 122,437|
| |Cleburne County|     5| 200.650| N/A|   187|  7504.314| N/A|  24,919|
| |Ashley County|     5| 254.362| N/A|   284| 14447.779| N/A|  19,657|
| |Faulkner County|     5| 39.680| N/A| 1,239|  9832.787| N/A| 126,007|
| |Sharp County|     5| 286.664| N/A|   106|  6077.285| N/A|  17,442|
| |Miller County|     5| 115.588| N/A|   489| 11304.529| N/A|  43,257|
| |Newton County|     5| 644.912| N/A|   100| 12898.233| N/A|   7,753|
| |Clay County|     4| 274.895| N/A|   114|  7834.513| N/A|  14,551|
| |Poinsett County|     3| 127.508| N/A|   190|  8075.485| N/A|  23,528|
| |St. Francis County|     3| 120.029| N/A| 1,148| 45931.023| N/A|  24,994|
| |Randolph County|     3| 167.056| N/A|   198| 11025.727| N/A|  17,958|
| |Bradley County|     3| 278.733| N/A|   167| 15516.120| N/A|  10,763|
| |Drew County|     3| 164.663| N/A|   175|  9605.357| N/A|  18,219|
| |Conway County|     3| 143.913| N/A|   143|  6859.829| N/A|  20,846|
| |Cross County|     3| 182.715| N/A|   173| 10536.573| N/A|  16,419|
| |Crawford County|     3| 47.426| N/A|   569|  8995.052| N/A|  63,257|
| |Van Buren County|     2| 120.882| N/A|    52|  3142.943| N/A|  16,545|
| |Franklin County|     2| 112.899| N/A|   113|  6378.775| N/A|  17,715|
| |White County|     2| 25.396| N/A|   284|  3606.212| N/A|  78,753|
| |Desha County|     2| 176.041| N/A|   174| 15315.553| N/A|  11,361|
| |Hempstead County|     2| 92.885| N/A|   227| 10542.448| N/A|  21,532|
| |Lonoke County|     2| 27.282| N/A|   474|  6465.782| N/A|  73,309|
| |Howard County|     2| 151.492| N/A|   308| 23329.799| N/A|  13,202|
| |Lafayette County|     2| 301.932| N/A|    52|  7850.242| N/A|   6,624|
| |Johnson County|     2| 75.250| N/A|   646| 24305.817| N/A|  26,578|
| |Cleveland County|     2| 251.383| N/A|    83| 10432.378| N/A|   7,956|
| |Ouachita County|     2| 85.536| N/A|    84|  3592.507| N/A|  23,382|
| |Arkansas County|     1| 57.189| N/A|   209| 11952.419| N/A|  17,486|
| |Boone County|     1| 26.715| N/A|   184|  4915.580| N/A|  37,432|
| |Greene County|     1| 22.063| N/A|   422|  9310.535| N/A|  45,325|
| |Izard County|     1| 73.373| N/A|    45|  3301.783| N/A|  13,629|
| |Independence County|     1| 26.438| N/A|   433| 11447.455| N/A|  37,825|
| |Madison County|     1| 60.328| N/A|   267| 16107.625| N/A|  16,576|
| |Stone County|     1| 79.962| N/A|    59|  4717.735| N/A|  12,506|
| |Clark County|     1| 44.803| N/A|   170|  7616.487| N/A|  22,320|
| |Polk County|     1| 50.090| N/A|   134|  6712.082| N/A|  19,964|
| |Pike County|     1| 93.301| N/A|    88|  8210.487| N/A|  10,718|
| |Jackson County|     1| 59.812| N/A|    62|  3708.356| N/A|  16,719|
| |Little River County|     1| 81.573| N/A|   160| 13051.636| N/A|  12,259|
| |Logan County|     1| 46.585| N/A|   208|  9689.742| N/A|  21,466|
| |Calhoun County|     0|  0.000| N/A|    13|  2505.300| N/A|   5,189|
| |Baxter County|     0|  0.000| N/A|    68|  1621.673| N/A|  41,932|
| |Fulton County|     0|  0.000| N/A|    30|  2404.424| N/A|  12,477|
| |Dallas County|     0|  0.000| N/A|    59|  8417.749| N/A|   7,009|
| |Grant County|     0|  0.000| N/A|   130|  7117.438| N/A|  18,265|
| |Marion County|     0|  0.000| N/A|    26|  1557.446| N/A|  16,694|
| |Searcy County|     0|  0.000| N/A|    28|  3552.849| N/A|   7,881|
| |Prairie County|     0|  0.000| N/A|    78|  9675.019| N/A|   8,062|
| |Perry County|     0|  0.000| N/A|    50|  4782.401| N/A|  10,455|
| |Montgomery County|     0|  0.000| N/A|    31|  3449.811| N/A|   8,986|
| |Monroe County|     0|  0.000| N/A|    52|  7760.036| N/A|   6,701|
| |Scott County|     0|  0.000| N/A|    46|  4474.273| N/A|  10,281|
| |Woodruff County|     0|  0.000| N/A|    20|  3164.557| N/A|   6,320|


### New Hampshire ###

![New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/New%20Hampshire.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NH|10 counties|   418| 307.418| N/A| 6,716|  4939.285| N/A|1,359,711|
| |Hillsborough County|   279| 669.025|  0.000| 3,801|  9114.561| 29.286| 417,025|
| |Rockingham County|    95| 306.680|  0.000| 1,660|  5358.832| 29.532| 309,769|
| |Merrimack County|    21| 138.714|  0.000|   459|  3031.884|  0.000| 151,391|
| |Strafford County|    13| 99.515|  0.000|   338|  2587.401| 12.578| 130,633|
| |Belknap County|     4| 65.250| N/A|   113|  1843.303| N/A|  61,303|
| |Cheshire County|     3| 39.430| N/A|    95|  1248.604| N/A|  76,085|
| |Carroll County|     1| 20.446| N/A|    91|  1860.560| N/A|  48,910|
| |Grafton County|     1| 11.125| N/A|   103|  1145.896| N/A|  89,886|
| |Sullivan County|     1| 23.177| N/A|    40|   927.085| N/A|  43,146|
| |Coos County|     0|  0.000| N/A|    16|   506.923| N/A|  31,563|


### Kansas ###

![Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Kansas.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|KS|105 counties|   371| 127.346| N/A|29,256| 10042.172| N/A|2,913,314|
| |Wyandotte County|    98| 592.399|  5.991| 4,674| 28253.813| 363.437| 165,429|
| |Johnson County|    98| 162.682|  0.000| 5,320|  8831.327| 141.102| 602,401|
| |Sedgwick County|    43| 83.327|  0.000| 4,540|  8797.734| 186.140| 516,042|
| |Shawnee County|    19| 107.420|  0.000| 1,473|  8327.915| 104.804| 176,875|
| |Lyon County|    13| 391.625|  9.452|   680| 20485.013| 56.914|  33,195|
| |Finney County|    10| 274.221|  0.000| 1,758| 48207.969| 219.949|  36,467|
| |Ford County|     8| 237.961| N/A| 2,055| 61126.149| N/A|  33,619|
| |Coffey County|     8| 978.115| N/A|    67|  8191.710| N/A|   8,179|
| |Phillips County|     8| 1528.468| N/A|    50|  9552.923| N/A|   5,234|
| |Leavenworth County|     8| 97.850| N/A| 1,444| 17661.880| N/A|  81,758|
| |Riley County|     5| 67.356| N/A|   465|  6264.145| N/A|  74,232|
| |Douglas County|     5| 40.897| N/A|   686|  5611.039| N/A| 122,259|
| |Saline County|     5| 92.210| N/A|   362|  6676.011| N/A|  54,224|
| |Montgomery County|     5| 157.089| N/A|   162|  5089.698| N/A|  31,829|
| |Seward County|     4| 186.672| N/A| 1,215| 56701.512| N/A|  21,428|
| |Barton County|     3| 116.374| N/A|   126|  4887.699| N/A|  25,779|
| |Sumner County|     3| 131.372| N/A|    98|  4291.470| N/A|  22,836|
| |Grant County|     2| 279.720| N/A|    97| 13566.434| N/A|   7,150|
| |Bourbon County|     2| 137.608| N/A|    73|  5022.705| N/A|  14,534|
| |Geary County|     2| 63.151| N/A|   130|  4104.831| N/A|  31,670|
| |Morton County|     2| 773.096| N/A|     9|  3478.933| N/A|   2,587|
| |Cowley County|     2| 57.293| N/A|   160|  4583.477| N/A|  34,908|
| |Clay County|     2| 249.938| N/A|    18|  2249.438| N/A|   8,002|
| |Clark County|     1| 501.505| N/A|    45| 22567.703| N/A|   1,994|
| |Crawford County|     1| 25.761| N/A|   377|  9711.989| N/A|  38,818|
| |Dickinson County|     1| 54.154| N/A|    44|  2382.758| N/A|  18,466|
| |Ellis County|     1| 35.023| N/A|   135|  4728.050| N/A|  28,553|
| |Cherokee County|     1| 50.153| N/A|    91|  4563.920| N/A|  19,939|
| |Butler County|     1| 14.945| N/A|   228|  3407.511| N/A|  66,911|
| |Reno County|     1| 16.130| N/A|   241|  3887.222| N/A|  61,998|
| |Marion County|     1| 84.147| N/A|    46|  3870.751| N/A|  11,884|
| |Nemaha County|     1| 97.742| N/A|    48|  4691.623| N/A|  10,231|
| |Harvey County|     1| 29.045| N/A|   169|  4908.653| N/A|  34,429|
| |Jackson County|     1| 75.924| N/A|   146| 11084.959| N/A|  13,171|
| |McPherson County|     1| 35.036| N/A|   137|  4799.944| N/A|  28,542|
| |Franklin County|     1| 39.148| N/A|   172|  6733.479| N/A|  25,544|
| |Trego County|     1| 356.761| N/A|     5|  1783.803| N/A|   2,803|
| |Stanton County|     1| 498.504| N/A|    16|  7976.072| N/A|   2,006|
| |Kearny County|     1| 260.552| N/A|    57| 14851.485| N/A|   3,838|
| |Republic County|     0|  0.000| N/A|    32|  6902.502| N/A|   4,636|
| |Pratt County|     0|  0.000| N/A|    33|  3601.048| N/A|   9,164|
| |Sheridan County|     0|  0.000| N/A|     7|  2776.676| N/A|   2,521|
| |Scott County|     0|  0.000| N/A|    34|  7049.554| N/A|   4,823|
| |Russell County|     0|  0.000| N/A|    13|  1896.149| N/A|   6,856|
| |Rush County|     0|  0.000| N/A|     6|  1976.285| N/A|   3,036|
| |Rooks County|     0|  0.000| N/A|    16|  3252.033| N/A|   4,920|
| |Rice County|     0|  0.000| N/A|    35|  3669.917| N/A|   9,537|
| |Rawlins County|     0|  0.000| N/A|     0|     0.000| N/A|   2,530|
| |Pottawatomie County|     0|  0.000| N/A|   106|  4347.291| N/A|  24,383|
| |Smith County|     0|  0.000| N/A|     3|   837.287| N/A|   3,583|
| |Pawnee County|     0|  0.000| N/A|     7|  1091.363| N/A|   6,414|
| |Ottawa County|     0|  0.000| N/A|    32|  5610.098| N/A|   5,704|
| |Osborne County|     0|  0.000| N/A|     4|  1169.249| N/A|   3,421|
| |Osage County|     0|  0.000| N/A|    38|  2382.595| N/A|  15,949|
| |Norton County|     0|  0.000| N/A|    23|  4290.244| N/A|   5,361|
| |Ness County|     0|  0.000| N/A|     6|  2181.818| N/A|   2,750|
| |Neosho County|     0|  0.000| N/A|    56|  3498.469| N/A|  16,007|
| |Morris County|     0|  0.000| N/A|    11|  1957.295| N/A|   5,620|
| |Sherman County|     0|  0.000| N/A|    15|  2535.068| N/A|   5,917|
| |Stafford County|     0|  0.000| N/A|     3|   721.848| N/A|   4,156|
| |Edwards County|     0|  0.000| N/A|    10|  3573.981| N/A|   2,798|
| |Brown County|     0|  0.000| N/A|    35|  3659.557| N/A|   9,564|
| |Atchison County|     0|  0.000| N/A|    62|  3857.401| N/A|  16,073|
| |Marshall County|     0|  0.000| N/A|     9|   927.166| N/A|   9,707|
| |Anderson County|     0|  0.000| N/A|    29|  3690.506| N/A|   7,858|
| |Allen County|     0|  0.000| N/A|    15|  1212.709| N/A|  12,369|
| |Elk County|     0|  0.000| N/A|     1|   395.257| N/A|   2,530|
| |Chautauqua County|     0|  0.000| N/A|     5|  1538.462| N/A|   3,250|
| |Ellsworth County|     0|  0.000| N/A|    21|  3441.495| N/A|   6,102|
| |Gove County|     0|  0.000| N/A|     6|  2276.176| N/A|   2,636|
| |Logan County|     0|  0.000| N/A|     2|   715.820| N/A|   2,794|
| |Linn County|     0|  0.000| N/A|    36|  3710.193| N/A|   9,703|
| |Lincoln County|     0|  0.000| N/A|     6|  2025.658| N/A|   2,962|
| |Lane County|     0|  0.000| N/A|     5|  3257.329| N/A|   1,535|
| |Labette County|     0|  0.000| N/A|   118|  6014.884| N/A|  19,618|
| |Kiowa County|     0|  0.000| N/A|     7|  2828.283| N/A|   2,475|
| |Kingman County|     0|  0.000| N/A|    12|  1677.852| N/A|   7,152|
| |Jewell County|     0|  0.000| N/A|    10|  3473.428| N/A|   2,879|
| |Jefferson County|     0|  0.000| N/A|    75|  3938.455| N/A|  19,043|
| |Chase County|     0|  0.000| N/A|    42| 15861.027| N/A|   2,648|
| |Cheyenne County|     0|  0.000| N/A|     2|   752.729| N/A|   2,657|
| |Wilson County|     0|  0.000| N/A|    10|  1173.021| N/A|   8,525|
| |Stevens County|     0|  0.000| N/A|    45|  8204.193| N/A|   5,485|
| |Woodson County|     0|  0.000| N/A|    11|  3505.417| N/A|   3,138|
| |Wichita County|     0|  0.000| N/A|     4|  1887.683| N/A|   2,119|
| |Cloud County|     0|  0.000| N/A|    30|  3414.523| N/A|   8,786|
| |Washington County|     0|  0.000| N/A|     3|   554.939| N/A|   5,406|
| |Wallace County|     0|  0.000| N/A|     0|     0.000| N/A|   1,518|
| |Wabaunsee County|     0|  0.000| N/A|    42|  6059.732| N/A|   6,931|
| |Thomas County|     0|  0.000| N/A|    35|  4500.450| N/A|   7,777|
| |Mitchell County|     0|  0.000| N/A|    27|  4515.805| N/A|   5,979|
| |Miami County|     0|  0.000| N/A|   123|  3592.604| N/A|  34,237|
| |Meade County|     0|  0.000| N/A|    42| 10414.084| N/A|   4,033|
| |Barber County|     0|  0.000| N/A|     4|   903.546| N/A|   4,427|
| |Doniphan County|     0|  0.000| N/A|    47|  6184.211| N/A|   7,600|
| |Decatur County|     0|  0.000| N/A|     5|  1768.659| N/A|   2,827|
| |Comanche County|     0|  0.000| N/A|     3|  1764.706| N/A|   1,700|
| |Hodgeman County|     0|  0.000| N/A|    11|  6131.550| N/A|   1,794|
| |Haskell County|     0|  0.000| N/A|    44| 11088.710| N/A|   3,968|
| |Harper County|     0|  0.000| N/A|    10|  1839.588| N/A|   5,436|
| |Hamilton County|     0|  0.000| N/A|    37| 14572.666| N/A|   2,539|
| |Greenwood County|     0|  0.000| N/A|    20|  3343.363| N/A|   5,982|
| |Greeley County|     0|  0.000| N/A|     3|  2435.065| N/A|   1,232|
| |Gray County|     0|  0.000| N/A|    77| 12859.051| N/A|   5,988|
| |Graham County|     0|  0.000| N/A|    16|  6446.414| N/A|   2,482|


### Oregon ###

![Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Oregon.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|OR|36 counties|   338| 80.138| N/A|19,978|  4736.663| N/A|4,217,737|
| |Multnomah County|    93| 114.412|  0.192| 4,608|  5668.908| 66.644| 812,855|
| |Marion County|    68| 195.505|  0.446| 2,755|  7920.809| 88.106| 347,818|
| |Clackamas County|    38| 90.868|  1.196| 1,464|  3500.826| 50.217| 418,187|
| |Umatilla County|    26| 333.547| 10.620| 2,141| 27466.325| 519.564|  77,950|
| |Washington County|    24| 39.894|  0.691| 2,921|  4855.450| 56.796| 601,592|
| |Malheur County|    12| 392.529| 26.960|   715| 23388.178| 435.187|  30,571|
| |Yamhill County|    12| 112.045|  3.988|   404|  3772.176| 84.034| 107,100|
| |Polk County|    12| 139.397|  0.000|   301|  3496.544| 38.450|  86,085|
| |Linn County|    10| 77.072|  0.000|   263|  2026.991| 36.441| 129,749|
| |Lincoln County|     9| 180.137| N/A|   414|  8286.298| N/A|  49,962|
| |Deschutes County|     8| 40.467| N/A|   555|  2807.397| N/A| 197,692|
| |Benton County|     6| 64.479| N/A|   162|  1740.943| N/A|  93,053|
| |Wasco County|     3| 112.435| N/A|   172|  6446.293| N/A|  26,682|
| |Lane County|     3|  7.852| N/A|   540|  1413.365| N/A| 382,067|
| |Jefferson County|     3| 121.664| N/A|   332| 13464.190| N/A|  24,658|
| |Morrow County|     2| 172.369| N/A|   327| 28182.367| N/A|  11,603|
| |Union County|     2| 74.530| N/A|   392| 14607.788| N/A|  26,835|
| |Josephine County|     2| 22.861| N/A|   108|  1234.469| N/A|  87,487|
| |Jackson County|     1|  4.526| N/A|   421|  1905.460| N/A| 220,944|
| |Douglas County|     1|  9.011| N/A|   140|  1261.489| N/A| 110,980|
| |Wallowa County|     1| 138.735| N/A|    19|  2635.960| N/A|   7,208|
| |Crook County|     1| 40.977| N/A|    42|  1721.029| N/A|  24,404|
| |Klamath County|     1| 14.655| N/A|   200|  2930.918| N/A|  68,238|
| |Hood River County|     0|  0.000| N/A|   178|  7612.694| N/A|  23,382|
| |Grant County|     0|  0.000| N/A|     2|   277.816| N/A|   7,199|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|   1,332|
| |Tillamook County|     0|  0.000| N/A|    34|  1257.582| N/A|  27,036|
| |Sherman County|     0|  0.000| N/A|    14|  7865.169| N/A|   1,780|
| |Lake County|     0|  0.000| N/A|    32|  4066.590| N/A|   7,869|
| |Harney County|     0|  0.000| N/A|    10|  1352.631| N/A|   7,393|
| |Gilliam County|     0|  0.000| N/A|     4|  2092.050| N/A|   1,912|
| |Baker County|     0|  0.000| N/A|    36|  2232.697| N/A|  16,124|
| |Curry County|     0|  0.000| N/A|    14|   610.687| N/A|  22,925|
| |Coos County|     0|  0.000| N/A|    89|  1380.123| N/A|  64,487|
| |Columbia County|     0|  0.000| N/A|    86|  1642.663| N/A|  52,354|
| |Clatsop County|     0|  0.000| N/A|    83|  2063.445| N/A|  40,224|


### Nebraska ###

![Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Nebraska.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|NE|93 counties|   335| 173.180| N/A|27,339| 14133.006| N/A|1,934,408|
| |Douglas County|   131| 229.291|  0.000|10,875| 19034.633| 230.261| 571,327|
| |Hall County|    45| 733.460|  0.000| 1,727| 28148.583| 78.739|  61,353|
| |Dakota County|    41| 2047.338|  0.000| 1,908| 95276.141| 144.687|  20,026|
| |Lancaster County|    17| 53.277|  6.268| 3,180|  9965.840| 73.647| 319,090|
| |Hamilton County|    12| 1287.001|  0.000|    97| 10403.260| 44.857|   9,324|
| |Adams County|    11| 350.732|  0.000|   346| 11032.108| 40.733|  31,363|
| |Dawson County|     9| 381.437| N/A|   951| 40305.149| N/A|  23,595|
| |Sarpy County|     9| 48.078| N/A| 2,139| 11426.526| N/A| 187,196|
| |Dodge County|     8| 218.788| N/A|   784| 21441.269| N/A|  36,565|
| |Scotts Bluff County|     6| 168.454| N/A|   297|  8338.481| N/A|  35,618|
| |Madison County|     5| 142.454| N/A|   427| 12165.589| N/A|  35,099|
| |Howard County|     4| 620.636| N/A|    55|  8533.747| N/A|   6,445|
| |Thurston County|     4| 553.710| N/A|   203| 28100.775| N/A|   7,224|
| |Colfax County|     4| 373.518| N/A|   696| 64992.063| N/A|  10,709|
| |Custer County|     4| 371.161| N/A|    43|  3989.979| N/A|  10,777|
| |Gage County|     4| 185.934| N/A|    83|  3858.132| N/A|  21,513|
| |Platte County|     3| 89.633| N/A|   778| 23244.697| N/A|  33,470|
| |Dixon County|     2| 354.862| N/A|    57| 10113.556| N/A|   5,636|
| |Cass County|     2| 76.196| N/A|   163|  6209.997| N/A|  26,248|
| |Lincoln County|     2| 57.284| N/A|    94|  2692.330| N/A|  34,914|
| |Saline County|     2| 140.607| N/A|   592| 41619.798| N/A|  14,224|
| |Saunders County|     2| 92.687| N/A|   143|  6627.120| N/A|  21,578|
| |Richardson County|     1| 127.146| N/A|    20|  2542.912| N/A|   7,865|
| |Washington County|     1| 48.242| N/A|   113|  5451.300| N/A|  20,729|
| |Seward County|     1| 57.857| N/A|   107|  6190.697| N/A|  17,284|
| |Perkins County|     1| 345.901| N/A|    17|  5880.318| N/A|   2,891|
| |Antelope County|     1| 158.781| N/A|    19|  3016.831| N/A|   6,298|
| |Fillmore County|     1| 183.083| N/A|    24|  4393.995| N/A|   5,462|
| |Furnas County|     1| 213.858| N/A|    15|  3207.870| N/A|   4,676|
| |Buffalo County|     1| 20.137| N/A|   376|  7571.639| N/A|  49,659|
| |Johnson County|     0|  0.000| N/A|    13|  2563.597| N/A|   5,071|
| |Nance County|     0|  0.000| N/A|     8|  2273.373| N/A|   3,519|
| |Morrill County|     0|  0.000| N/A|    58| 12494.614| N/A|   4,642|
| |Merrick County|     0|  0.000| N/A|    57|  7350.097| N/A|   7,755|
| |McPherson County|     0|  0.000| N/A|     4|  8097.166| N/A|     494|
| |Logan County|     0|  0.000| N/A|     0|     0.000| N/A|     748|
| |Hitchcock County|     0|  0.000| N/A|     1|   362.056| N/A|   2,762|
| |Knox County|     0|  0.000| N/A|    33|  3960.634| N/A|   8,332|
| |Kimball County|     0|  0.000| N/A|    15|  4129.956| N/A|   3,632|
| |Keya Paha County|     0|  0.000| N/A|     0|     0.000| N/A|     806|
| |Keith County|     0|  0.000| N/A|    19|  2364.949| N/A|   8,034|
| |Kearney County|     0|  0.000| N/A|    43|  6620.477| N/A|   6,495|
| |Jefferson County|     0|  0.000| N/A|    14|  1986.943| N/A|   7,046|
| |Nuckolls County|     0|  0.000| N/A|     5|  1205.400| N/A|   4,148|
| |Hooker County|     0|  0.000| N/A|     4|  5865.103| N/A|     682|
| |Phelps County|     0|  0.000| N/A|    37|  4095.639| N/A|   9,034|
| |Pierce County|     0|  0.000| N/A|    18|  2518.187| N/A|   7,148|
| |Polk County|     0|  0.000| N/A|    26|  4987.531| N/A|   5,213|
| |Red Willow County|     0|  0.000| N/A|    16|  1491.981| N/A|  10,724|
| |York County|     0|  0.000| N/A|    77|  5629.066| N/A|  13,679|
| |Nemaha County|     0|  0.000| N/A|    23|  3298.910| N/A|   6,972|
| |Otoe County|     0|  0.000| N/A|    43|  2685.486| N/A|  16,012|
| |Pawnee County|     0|  0.000| N/A|     9|  3444.317| N/A|   2,613|
| |Loup County|     0|  0.000| N/A|     0|     0.000| N/A|     664|
| |Wheeler County|     0|  0.000| N/A|     0|     0.000| N/A|     783|
| |Webster County|     0|  0.000| N/A|     9|  2581.015| N/A|   3,487|
| |Wayne County|     0|  0.000| N/A|    37|  3942.461| N/A|   9,385|
| |Frontier County|     0|  0.000| N/A|     3|  1141.987| N/A|   2,627|
| |Box Butte County|     0|  0.000| N/A|    11|  1020.124| N/A|  10,783|
| |Boyd County|     0|  0.000| N/A|     1|   521.105| N/A|   1,919|
| |Brown County|     0|  0.000| N/A|     0|     0.000| N/A|   2,955|
| |Burt County|     0|  0.000| N/A|    26|  4025.391| N/A|   6,459|
| |Greeley County|     0|  0.000| N/A|     9|  3820.034| N/A|   2,356|
| |Grant County|     0|  0.000| N/A|     0|     0.000| N/A|     623|
| |Gosper County|     0|  0.000| N/A|    19|  9547.739| N/A|   1,990|
| |Garfield County|     0|  0.000| N/A|     3|  1523.616| N/A|   1,969|
| |Garden County|     0|  0.000| N/A|     4|  2177.463| N/A|   1,837|
| |Franklin County|     0|  0.000| N/A|    10|  3356.831| N/A|   2,979|
| |Valley County|     0|  0.000| N/A|    10|  2405.002| N/A|   4,158|
| |Dundy County|     0|  0.000| N/A|     1|   590.667| N/A|   1,693|
| |Deuel County|     0|  0.000| N/A|     2|  1114.827| N/A|   1,794|
| |Dawes County|     0|  0.000| N/A|     9|  1047.852| N/A|   8,589|
| |Cuming County|     0|  0.000| N/A|    65|  7347.954| N/A|   8,846|
| |Clay County|     0|  0.000| N/A|    49|  7899.404| N/A|   6,203|
| |Cheyenne County|     0|  0.000| N/A|    26|  2918.070| N/A|   8,910|
| |Cherry County|     0|  0.000| N/A|     4|   703.111| N/A|   5,689|
| |Chase County|     0|  0.000| N/A|     6|  1529.052| N/A|   3,924|
| |Cedar County|     0|  0.000| N/A|    22|  2618.424| N/A|   8,402|
| |Butler County|     0|  0.000| N/A|    57|  7110.778| N/A|   8,016|
| |Thomas County|     0|  0.000| N/A|     1|  1385.042| N/A|     722|
| |Thayer County|     0|  0.000| N/A|    26|  5196.882| N/A|   5,003|
| |Stanton County|     0|  0.000| N/A|    28|  4729.730| N/A|   5,920|
| |Sioux County|     0|  0.000| N/A|     5|  4288.165| N/A|   1,166|
| |Sherman County|     0|  0.000| N/A|    10|  3332.223| N/A|   3,001|
| |Sheridan County|     0|  0.000| N/A|     9|  1715.593| N/A|   5,246|
| |Rock County|     0|  0.000| N/A|     3|  2210.759| N/A|   1,357|
| |Holt County|     0|  0.000| N/A|    12|  1192.014| N/A|  10,067|
| |Hayes County|     0|  0.000| N/A|     0|     0.000| N/A|     922|
| |Boone County|     0|  0.000| N/A|     7|  1348.228| N/A|   5,192|
| |Blaine County|     0|  0.000| N/A|     0|     0.000| N/A|     465|
| |Banner County|     0|  0.000| N/A|     2|  2684.564| N/A|     745|
| |Arthur County|     0|  0.000| N/A|     0|     0.000| N/A|     463|
| |Harlan County|     0|  0.000| N/A|     1|   295.858| N/A|   3,380|


### Utah ###

![Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Utah.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|UT|29 counties|   269| 83.906| N/A|33,675| 10503.881| N/A|3,205,958|
| |Salt Lake County|   185| 159.423|  2.800|19,875| 17127.168| 127.538|1,160,437|
| |Utah County|    36| 56.583|  1.572| 8,271| 12999.914| 176.036| 636,235|
| |San Juan County|    25| 1633.133| 27.173|   632| 41285.602| 161.051|  15,308|
| |Davis County|    18| 50.636|  5.626| 3,094|  8703.700| 95.645| 355,481|
| |Wasatch County|     4| 117.333| N/A|   538| 15781.291| N/A|  34,091|
| |Summit County|     1| 23.728| N/A|   701| 16633.053| N/A|  42,145|
| |Garfield County|     0|  0.000| N/A|     0|     0.000| N/A|   5,051|
| |Emery County|     0|  0.000| N/A|     0|     0.000| N/A|  10,012|
| |Grand County|     0|  0.000| N/A|     0|     0.000| N/A|   9,754|
| |Daggett County|     0|  0.000| N/A|     0|     0.000| N/A|     950|
| |Iron County|     0|  0.000| N/A|     0|     0.000| N/A|  54,839|
| |Juab County|     0|  0.000| N/A|     0|     0.000| N/A|  12,017|
| |Kane County|     0|  0.000| N/A|     0|     0.000| N/A|   7,886|
| |Millard County|     0|  0.000| N/A|     0|     0.000| N/A|  13,188|
| |Morgan County|     0|  0.000| N/A|     0|     0.000| N/A|  12,124|
| |Piute County|     0|  0.000| N/A|     0|     0.000| N/A|   1,479|
| |Uintah County|     0|  0.000| N/A|     0|     0.000| N/A|  35,734|
| |Washington County|     0|  0.000| N/A|     0|     0.000| N/A| 177,556|
| |Wayne County|     0|  0.000| N/A|     0|     0.000| N/A|   2,711|
| |Weber County|     0|  0.000| N/A|     0|     0.000| N/A| 260,213|
| |Rich County|     0|  0.000| N/A|     0|     0.000| N/A|   2,483|
| |Duchesne County|     0|  0.000| N/A|     0|     0.000| N/A|  19,938|
| |Carbon County|     0|  0.000| N/A|     0|     0.000| N/A|  20,463|
| |Sevier County|     0|  0.000| N/A|     0|     0.000| N/A|  21,620|
| |Cache County|     0|  0.000| N/A|     0|     0.000| N/A| 128,289|
| |Beaver County|     0|  0.000| N/A|     0|     0.000| N/A|   6,710|
| |Box Elder County|     0|  0.000| N/A|     0|     0.000| N/A|  56,046|
| |Sanpete County|     0|  0.000| N/A|     0|     0.000| N/A|  30,939|
| |Tooele County|     0|  0.000| N/A|   564|  7805.256| N/A|  72,259|


### Idaho ###

![Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Idaho.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ID|44 counties|   217| 121.428| N/A|22,703| 12704.071| N/A|1,787,065|
| |Ada County|    71| 147.429|  6.851| 8,415| 17473.478| 134.970| 481,587|
| |Canyon County|    43| 187.079|  8.260| 5,199| 22619.198| 516.368| 229,849|
| |Twin Falls County|    32| 368.333|  0.000| 1,283| 14767.835| 261.057|  86,878|
| |Nez Perce County|    19| 470.204|  0.000|   138|  3415.165|  0.000|  40,408|
| |Kootenai County|    14| 84.492|  2.578| 1,668| 10066.567| 164.372| 165,697|
| |Blaine County|     6| 260.632| N/A|   573| 24890.318| N/A|  23,021|
| |Jerome County|     6| 245.781| N/A|   449| 18392.594| N/A|  24,412|
| |Elmore County|     3| 109.047| N/A|   202|  7342.518| N/A|  27,511|
| |Washington County|     3| 294.291| N/A|   196| 19226.996| N/A|  10,194|
| |Owyhee County|     2| 169.162| N/A|   241| 20383.997| N/A|  11,823|
| |Minidoka County|     2| 95.062| N/A|   459| 21816.626| N/A|  21,039|
| |Shoshone County|     2| 155.255| N/A|    81|  6287.844| N/A|  12,882|
| |Payette County|     2| 83.504| N/A|   354| 14780.176| N/A|  23,951|
| |Bonneville County|     2| 16.798| N/A|   858|  7206.329| N/A| 119,062|
| |Bingham County|     2| 42.725| N/A|   223|  4763.838| N/A|  46,811|
| |Bannock County|     2| 22.777| N/A|   359|  4088.466| N/A|  87,808|
| |Boise County|     1| 127.698| N/A|    43|  5490.997| N/A|   7,831|
| |Jefferson County|     1| 33.477| N/A|   164|  5490.275| N/A|  29,871|
| |Gooding County|     1| 65.880| N/A|   149|  9816.193| N/A|  15,179|
| |Gem County|     1| 55.212| N/A|   165|  9109.982| N/A|  18,112|
| |Cassia County|     1| 41.615| N/A|   498| 20724.095| N/A|  24,030|
| |Valley County|     1| 87.781| N/A|    54|  4740.169| N/A|  11,392|
| |Adams County|     0|  0.000| N/A|    18|  4191.896| N/A|   4,294|
| |Clark County|     0|  0.000| N/A|     7|  8284.024| N/A|     845|
| |Custer County|     0|  0.000| N/A|     7|  1622.248| N/A|   4,315|
| |Madison County|     0|  0.000| N/A|   144|  3608.390| N/A|  39,907|
| |Lincoln County|     0|  0.000| N/A|    54| 10063.362| N/A|   5,366|
| |Lewis County|     0|  0.000| N/A|     1|   260.552| N/A|   3,838|
| |Lemhi County|     0|  0.000| N/A|    13|  1619.534| N/A|   8,027|
| |Latah County|     0|  0.000| N/A|    93|  2318.739| N/A|  40,108|
| |Idaho County|     0|  0.000| N/A|    30|  1799.964| N/A|  16,667|
| |Fremont County|     0|  0.000| N/A|    69|  5267.578| N/A|  13,099|
| |Franklin County|     0|  0.000| N/A|    50|  3603.344| N/A|  13,876|
| |Clearwater County|     0|  0.000| N/A|    16|  1827.318| N/A|   8,756|
| |Caribou County|     0|  0.000| N/A|    28|  3913.347| N/A|   7,155|
| |Camas County|     0|  0.000| N/A|     1|   904.159| N/A|   1,106|
| |Butte County|     0|  0.000| N/A|     0|     0.000| N/A|   2,597|
| |Boundary County|     0|  0.000| N/A|    34|  2776.644| N/A|  12,245|
| |Bonner County|     0|  0.000| N/A|   164|  3585.562| N/A|  45,739|
| |Benewah County|     0|  0.000| N/A|    59|  6345.451| N/A|   9,298|
| |Bear Lake County|     0|  0.000| N/A|    11|  1795.918| N/A|   6,125|
| |Oneida County|     0|  0.000| N/A|    13|  2869.124| N/A|   4,531|
| |Power County|     0|  0.000| N/A|    54|  7030.335| N/A|   7,681|
| |Teton County|     0|  0.000| N/A|    66|  5435.678| N/A|  12,142|


### South Dakota ###

![South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/South%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|SD|66 counties|   137| 154.862| N/A| 9,168| 10363.315| N/A| 884,659|
| |Minnehaha County|    64| 331.376|  0.000| 4,285| 22186.668| 134.622| 193,134|
| |Pennington County|    29| 254.889|  0.000|   858|  7541.200| 166.996| 113,775|
| |Beadle County|     9| 487.726| N/A|   587| 31810.546| N/A|  18,453|
| |Union County|     4| 251.067| N/A|   204| 12804.419| N/A|  15,932|
| |Todd County|     4| 393.043| N/A|    67|  6583.473| N/A|  10,177|
| |Brown County|     3| 77.242| N/A|   419| 10788.125| N/A|  38,839|
| |Buffalo County|     3| 1529.052| N/A|   109| 55555.556| N/A|   1,962|
| |Lincoln County|     2| 32.718| N/A|   588|  9619.160| N/A|  61,128|
| |Lyman County|     2| 528.961| N/A|    88| 23274.266| N/A|   3,781|
| |Lake County|     2| 156.287| N/A|    86|  6720.325| N/A|  12,797|
| |Hughes County|     2| 114.116| N/A|    84|  4792.879| N/A|  17,526|
| |Yankton County|     2| 87.665| N/A|   104|  4558.604| N/A|  22,814|
| |Davison County|     1| 50.569| N/A|    93|  4702.908| N/A|  19,775|
| |Jerauld County|     1| 496.771| N/A|    40| 19870.840| N/A|   2,013|
| |Codington County|     1| 35.703| N/A|   123|  4391.446| N/A|  28,009|
| |Roberts County|     1| 96.209| N/A|    71|  6830.864| N/A|  10,394|
| |Jackson County|     1| 299.043| N/A|    11|  3289.474| N/A|   3,344|
| |Oglala Lakota County|     1| 70.537| N/A|   152| 10721.591| N/A|  14,177|
| |Faulk County|     1| 434.972| N/A|    26| 11309.265| N/A|   2,299|
| |Meade County|     1| 35.296| N/A|    82|  2894.254| N/A|  28,332|
| |McCook County|     1| 179.019| N/A|    26|  4654.493| N/A|   5,586|
| |Butte County|     1| 95.886| N/A|    12|  1150.638| N/A|  10,429|
| |Brookings County|     1| 28.509| N/A|   122|  3478.063| N/A|  35,077|
| |Kingsbury County|     0|  0.000| N/A|    14|  2834.582| N/A|   4,939|
| |Jones County|     0|  0.000| N/A|     2|  2214.839| N/A|     903|
| |Edmunds County|     0|  0.000| N/A|    13|  3395.142| N/A|   3,829|
| |Campbell County|     0|  0.000| N/A|     3|  2180.233| N/A|   1,376|
| |Douglas County|     0|  0.000| N/A|    16|  5477.576| N/A|   2,921|
| |Dewey County|     0|  0.000| N/A|    64| 10862.186| N/A|   5,892|
| |Deuel County|     0|  0.000| N/A|     9|  2068.490| N/A|   4,351|
| |Day County|     0|  0.000| N/A|    21|  3871.681| N/A|   5,424|
| |Custer County|     0|  0.000| N/A|    23|  2563.531| N/A|   8,972|
| |Corson County|     0|  0.000| N/A|    30|  7342.144| N/A|   4,086|
| |Clay County|     0|  0.000| N/A|   120|  8528.785| N/A|  14,070|
| |Clark County|     0|  0.000| N/A|    16|  4282.655| N/A|   3,736|
| |Hyde County|     0|  0.000| N/A|     3|  2305.919| N/A|   1,301|
| |Lawrence County|     0|  0.000| N/A|    35|  1354.280| N/A|  25,844|
| |Gregory County|     0|  0.000| N/A|     7|  1672.640| N/A|   4,185|
| |Ziebach County|     0|  0.000| N/A|     9|  3265.602| N/A|   2,756|
| |Walworth County|     0|  0.000| N/A|    18|  3311.868| N/A|   5,435|
| |Turner County|     0|  0.000| N/A|    49|  5844.466| N/A|   8,384|
| |Tripp County|     0|  0.000| N/A|    20|  3675.795| N/A|   5,441|
| |Sully County|     0|  0.000| N/A|     1|   718.907| N/A|   1,391|
| |Stanley County|     0|  0.000| N/A|    14|  4519.045| N/A|   3,098|
| |Spink County|     0|  0.000| N/A|    22|  3450.439| N/A|   6,376|
| |Sanborn County|     0|  0.000| N/A|    13|  5546.075| N/A|   2,344|
| |Grant County|     0|  0.000| N/A|    23|  3261.486| N/A|   7,052|
| |Haakon County|     0|  0.000| N/A|     2|  1053.186| N/A|   1,899|
| |Hamlin County|     0|  0.000| N/A|    16|  2595.717| N/A|   6,164|
| |Fall River County|     0|  0.000| N/A|    20|  2979.294| N/A|   6,713|
| |Hutchinson County|     0|  0.000| N/A|    27|  3703.196| N/A|   7,291|
| |Harding County|     0|  0.000| N/A|     0|     0.000| N/A|   1,298|
| |Hanson County|     0|  0.000| N/A|    21|  6081.668| N/A|   3,453|
| |Hand County|     0|  0.000| N/A|     7|  2193.670| N/A|   3,191|
| |Perkins County|     0|  0.000| N/A|     6|  2094.241| N/A|   2,865|
| |Potter County|     0|  0.000| N/A|     1|   464.468| N/A|   2,153|
| |Moody County|     0|  0.000| N/A|    30|  4562.044| N/A|   6,576|
| |Miner County|     0|  0.000| N/A|    15|  6768.953| N/A|   2,216|
| |Bennett County|     0|  0.000| N/A|     6|  1783.061| N/A|   3,365|
| |Aurora County|     0|  0.000| N/A|    38| 13813.159| N/A|   2,751|
| |Mellette County|     0|  0.000| N/A|    24| 11644.833| N/A|   2,061|
| |Marshall County|     0|  0.000| N/A|     8|  1621.074| N/A|   4,935|
| |McPherson County|     0|  0.000| N/A|     7|  2942.413| N/A|   2,379|
| |Charles Mix County|     0|  0.000| N/A|   100| 10761.946| N/A|   9,292|
| |Brule County|     0|  0.000| N/A|    45|  8495.375| N/A|   5,297|
| |Bon Homme County|     0|  0.000| N/A|    13|  1883.785| N/A|   6,901|


### Maine ###

![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Maine.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ME|16 counties|   124| 92.247| N/A| 3,992|  2969.770| N/A|1,344,212|
| |Cumberland County|    69| 233.896|  0.494| 2,066|  7003.319| 14.691| 295,003|
| |Waldo County|    14| 352.512|  0.000|    62|  1561.123|  0.000|  39,715|
| |York County|    12| 57.792|  0.000|   666|  3207.459| 19.264| 207,641|
| |Kennebec County|    11| 89.941|  0.000|   169|  1381.825|  3.418| 122,302|
| |Androscoggin County|     7| 64.649| N/A|   549|  5070.329| N/A| 108,277|
| |Penobscot County|     5| 32.863| N/A|   150|   985.882| N/A| 152,148|
| |Lincoln County|     1| 28.873| N/A|    33|   952.821| N/A|  34,634|
| |Somerset County|     1| 19.808| N/A|    34|   673.481| N/A|  50,484|
| |Aroostook County|     1| 14.913| N/A|    32|   477.220| N/A|  67,055|
| |Hancock County|     1| 18.186| N/A|    36|   654.700| N/A|  54,987|
| |Knox County|     1| 25.143| N/A|    27|   678.870| N/A|  39,772|
| |Franklin County|     1| 33.114| N/A|    45|  1490.116| N/A|  30,199|
| |Washington County|     0|  0.000| N/A|    12|   382.421| N/A|  31,379|
| |Sagadahoc County|     0|  0.000| N/A|    54|  1506.024| N/A|  35,856|
| |Piscataquis County|     0|  0.000| N/A|     3|   178.731| N/A|  16,785|
| |Oxford County|     0|  0.000| N/A|    54|   931.436| N/A|  57,975|


### West Virginia ###

![West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/West%20Virginia.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WV|55 counties|   124| 69.191| N/A| 7,162|  3996.324| N/A|1,792,147|
| |Kanawha County|    22| 123.509|  2.639|   856|  4805.641| 60.086| 178,124|
| |Jackson County|    19| 664.894|  0.000|   158|  5529.115| 16.450|  28,576|
| |Berkeley County|    11| 92.304|  0.000|   670|  5622.173| 48.247| 119,171|
| |Wayne County|     9| 228.415| N/A|   194|  4923.608| N/A|  39,402|
| |Fayette County|     5| 117.908| N/A|   134|  3159.930| N/A|  42,406|
| |Wood County|     5| 59.867| N/A|   240|  2873.632| N/A|  83,518|
| |Monongalia County|     5| 47.343| N/A|   929|  8796.349| N/A| 105,612|
| |Ohio County|     4| 96.593| N/A|   263|  6350.970| N/A|  41,411|
| |Preston County|     4| 119.646| N/A|   125|  3738.933| N/A|  33,432|
| |Mineral County|     4| 148.876| N/A|   116|  4317.404| N/A|  26,868|
| |Jefferson County|     4| 69.996| N/A|   292|  5109.719| N/A|  57,146|
| |Logan County|     3| 93.694| N/A|   162|  5059.496| N/A|  32,019|
| |Greenbrier County|     3| 86.550| N/A|    88|  2538.803| N/A|  34,662|
| |Mingo County|     3| 128.074| N/A|   153|  6531.762| N/A|  23,424|
| |Mercer County|     3| 51.057| N/A|   173|  2944.280| N/A|  58,758|
| |Cabell County|     2| 21.752| N/A|   362|  3937.136| N/A|  91,945|
| |Marion County|     2| 35.668| N/A|   179|  3192.324| N/A|  56,072|
| |Lewis County|     2| 125.731| N/A|    28|  1760.231| N/A|  15,907|
| |Clay County|     1| 117.536| N/A|    18|  2115.656| N/A|   8,508|
| |Pendleton County|     1| 143.493| N/A|    42|  6026.690| N/A|   6,969|
| |Barbour County|     1| 60.824| N/A|    30|  1824.707| N/A|  16,441|
| |Wyoming County|     1| 49.034| N/A|    24|  1176.817| N/A|  20,394|
| |Raleigh County|     1| 13.631| N/A|   207|  2821.663| N/A|  73,361|
| |Roane County|     1| 73.057| N/A|    14|  1022.794| N/A|  13,688|
| |Taylor County|     1| 59.898| N/A|    55|  3294.400| N/A|  16,695|
| |Brooke County|     1| 45.581| N/A|    62|  2826.018| N/A|  21,939|
| |Nicholas County|     1| 40.823| N/A|    33|  1347.159| N/A|  24,496|
| |Hampshire County|     1| 43.150| N/A|    75|  3236.246| N/A|  23,175|
| |Harrison County|     1| 14.869| N/A|   204|  3033.187| N/A|  67,256|
| |Grant County|     1| 86.445| N/A|    89|  7693.638| N/A|  11,568|
| |Marshall County|     1| 32.754| N/A|   129|  4225.214| N/A|  30,531|
| |Mason County|     1| 37.713| N/A|    51|  1923.367| N/A|  26,516|
| |Wirt County|     0|  0.000| N/A|     6|  1030.751| N/A|   5,821|
| |Wetzel County|     0|  0.000| N/A|    41|  2721.540| N/A|  15,065|
| |Hancock County|     0|  0.000| N/A|   106|  3679.278| N/A|  28,810|
| |Gilmer County|     0|  0.000| N/A|    16|  2045.251| N/A|   7,823|
| |Morgan County|     0|  0.000| N/A|    26|  1453.813| N/A|  17,884|
| |McDowell County|     0|  0.000| N/A|    48|  2723.559| N/A|  17,624|
| |Lincoln County|     0|  0.000| N/A|    75|  3674.849| N/A|  20,409|
| |Hardy County|     0|  0.000| N/A|    54|  3919.861| N/A|  13,776|
| |Monroe County|     0|  0.000| N/A|    19|  1431.262| N/A|  13,275|
| |Webster County|     0|  0.000| N/A|     3|   369.731| N/A|   8,114|
| |Upshur County|     0|  0.000| N/A|    39|  1613.170| N/A|  24,176|
| |Tyler County|     0|  0.000| N/A|    12|  1396.811| N/A|   8,591|
| |Tucker County|     0|  0.000| N/A|    11|  1608.422| N/A|   6,839|
| |Summers County|     0|  0.000| N/A|     7|   556.749| N/A|  12,573|
| |Ritchie County|     0|  0.000| N/A|     3|   314.005| N/A|   9,554|
| |Randolph County|     0|  0.000| N/A|   207|  7213.800| N/A|  28,695|
| |Putnam County|     0|  0.000| N/A|   174|  3082.374| N/A|  56,450|
| |Pocahontas County|     0|  0.000| N/A|    41|  4971.505| N/A|   8,247|
| |Pleasants County|     0|  0.000| N/A|     9|  1206.434| N/A|   7,460|
| |Doddridge County|     0|  0.000| N/A|     4|   473.485| N/A|   8,448|
| |Calhoun County|     0|  0.000| N/A|     6|   844.001| N/A|   7,109|
| |Braxton County|     0|  0.000| N/A|     8|   573.189| N/A|  13,957|
| |Boone County|     0|  0.000| N/A|    92|  4287.645| N/A|  21,457|


### North Dakota ###

![North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/North%20Dakota.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|ND|53 counties|   108| 141.721| N/A| 7,039|  9236.781| N/A| 762,062|
| |Cass County|    76| 417.759|  0.000| 2,958| 16259.626| 54.968| 181,923|
| |Grand Forks County|     6| 86.392| N/A|   650|  9359.116| N/A|  69,451|
| |Burleigh County|     5| 52.287| N/A| 1,049| 10969.820| N/A|  95,626|
| |Morton County|     3| 95.651| N/A|   297|  9469.455| N/A|  31,364|
| |Stark County|     3| 95.271| N/A|   227|  7208.867| N/A|  31,489|
| |Ramsey County|     2| 173.626| N/A|    65|  5642.851| N/A|  11,519|
| |Williams County|     2| 53.207| N/A|   247|  6571.071| N/A|  37,589|
| |Stutsman County|     2| 96.600| N/A|   121|  5844.281| N/A|  20,704|
| |Benson County|     1| 146.370| N/A|   130| 19028.103| N/A|   6,832|
| |Emmons County|     1| 308.547| N/A|    17|  5245.295| N/A|   3,241|
| |McKenzie County|     1| 66.560| N/A|    84|  5591.054| N/A|  15,024|
| |Sioux County|     1| 236.407| N/A|    59| 13947.991| N/A|   4,230|
| |McHenry County|     1| 174.064| N/A|    15|  2610.966| N/A|   5,745|
| |Mountrail County|     1| 94.832| N/A|   122| 11569.464| N/A|  10,545|
| |Griggs County|     1| 448.229| N/A|    30| 13446.885| N/A|   2,231|
| |McIntosh County|     1| 400.481| N/A|    27| 10812.976| N/A|   2,497|
| |Ward County|     1| 14.784| N/A|   197|  2912.435| N/A|  67,641|
| |Golden Valley County|     0|  0.000| N/A|     4|  2271.437| N/A|   1,761|
| |Eddy County|     0|  0.000| N/A|    17|  7433.319| N/A|   2,287|
| |Foster County|     0|  0.000| N/A|    23|  7165.109| N/A|   3,210|
| |Wells County|     0|  0.000| N/A|    20|  5216.484| N/A|   3,834|
| |Dunn County|     0|  0.000| N/A|    30|  6781.193| N/A|   4,424|
| |Logan County|     0|  0.000| N/A|     7|  3783.784| N/A|   1,850|
| |McLean County|     0|  0.000| N/A|    42|  4444.444| N/A|   9,450|
| |LaMoure County|     0|  0.000| N/A|    15|  3707.365| N/A|   4,046|
| |Kidder County|     0|  0.000| N/A|    12|  4838.710| N/A|   2,480|
| |Hettinger County|     0|  0.000| N/A|     6|  2400.960| N/A|   2,499|
| |Grant County|     0|  0.000| N/A|     4|  1759.015| N/A|   2,274|
| |Steele County|     0|  0.000| N/A|    13|  6878.307| N/A|   1,890|
| |Traill County|     0|  0.000| N/A|    49|  6097.561| N/A|   8,036|
| |Walsh County|     0|  0.000| N/A|   101|  9491.589| N/A|  10,641|
| |Nelson County|     0|  0.000| N/A|    22|  7641.542| N/A|   2,879|
| |Divide County|     0|  0.000| N/A|     1|   441.696| N/A|   2,264|
| |Dickey County|     0|  0.000| N/A|    12|  2463.054| N/A|   4,872|
| |Cavalier County|     0|  0.000| N/A|    31|  8240.298| N/A|   3,762|
| |Burke County|     0|  0.000| N/A|    23| 10874.704| N/A|   2,115|
| |Bowman County|     0|  0.000| N/A|     6|  1984.127| N/A|   3,024|
| |Bottineau County|     0|  0.000| N/A|     0|     0.000| N/A|   6,282|
| |Billings County|     0|  0.000| N/A|     2|  2155.172| N/A|     928|
| |Barnes County|     0|  0.000| N/A|    36|  3456.553| N/A|  10,415|
| |Adams County|     0|  0.000| N/A|     2|   902.527| N/A|   2,216|
| |Mercer County|     0|  0.000| N/A|    24|  2931.477| N/A|   8,187|
| |Towner County|     0|  0.000| N/A|     5|  2284.148| N/A|   2,189|
| |Oliver County|     0|  0.000| N/A|     7|  3573.252| N/A|   1,959|
| |Pembina County|     0|  0.000| N/A|    27|  3970.004| N/A|   6,801|
| |Slope County|     0|  0.000| N/A|     3|  4000.000| N/A|     750|
| |Sheridan County|     0|  0.000| N/A|     6|  4562.738| N/A|   1,315|
| |Sargent County|     0|  0.000| N/A|    10|  2565.418| N/A|   3,898|
| |Rolette County|     0|  0.000| N/A|    38|  2680.587| N/A|  14,176|
| |Richland County|     0|  0.000| N/A|   101|  6243.432| N/A|  16,177|
| |Renville County|     0|  0.000| N/A|     8|  3437.903| N/A|   2,327|
| |Ransom County|     0|  0.000| N/A|    26|  4982.752| N/A|   5,218|
| |Pierce County|     0|  0.000| N/A|    11|  2767.296| N/A|   3,975|


### Montana ###

![Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Montana.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|MT|56 counties|    65| 60.817| N/A| 4,429|  4143.985| N/A|1,068,778|
| |Yellowstone County|    27| 167.390|  0.000| 1,144|  7092.374| 105.394| 161,300|
| |Big Horn County|    11| 825.888| 23.556|   375| 28155.267| 964.310|  13,319|
| |Toole County|     6| 1266.892| N/A|    36|  7601.351| N/A|   4,736|
| |Gallatin County|     3| 26.216| N/A|   887|  7751.193| N/A| 114,434|
| |Flathead County|     2| 19.267| N/A|   276|  2658.806| N/A| 103,806|
| |Custer County|     2| 175.408| N/A|    58|  5086.827| N/A|  11,402|
| |Richland County|     2| 185.134| N/A|    47|  4350.643| N/A|  10,803|
| |Cascade County|     2| 24.580| N/A|   159|  1954.133| N/A|  81,366|
| |Lincoln County|     2| 100.100| N/A|    73|  3653.654| N/A|  19,980|
| |Glacier County|     1| 72.711| N/A|    60|  4362.685| N/A|  13,753|
| |Lake County|     1| 32.832| N/A|   170|  5581.456| N/A|  30,458|
| |Lewis and Clark County|     1| 14.403| N/A|   147|  2117.179| N/A|  69,432|
| |Madison County|     1| 116.279| N/A|    78|  9069.767| N/A|   8,600|
| |Missoula County|     1|  8.361| N/A|   267|  2232.441| N/A| 119,600|
| |Ravalli County|     1| 22.828| N/A|    74|  1689.266| N/A|  43,806|
| |Rosebud County|     1| 111.894| N/A|    31|  3468.726| N/A|   8,937|
| |Sweet Grass County|     1| 267.594| N/A|     5|  1337.972| N/A|   3,737|
| |Musselshell County|     0|  0.000| N/A|     2|   431.686| N/A|   4,633|
| |Petroleum County|     0|  0.000| N/A|     0|     0.000| N/A|     487|
| |Powder River County|     0|  0.000| N/A|     1|   594.530| N/A|   1,682|
| |Pondera County|     0|  0.000| N/A|    10|  1691.761| N/A|   5,911|
| |Powell County|     0|  0.000| N/A|     2|   290.276| N/A|   6,890|
| |Prairie County|     0|  0.000| N/A|     1|   928.505| N/A|   1,077|
| |Roosevelt County|     0|  0.000| N/A|    20|  1817.521| N/A|  11,004|
| |Sanders County|     0|  0.000| N/A|     9|   743.003| N/A|  12,113|
| |Phillips County|     0|  0.000| N/A|     5|  1264.542| N/A|   3,954|
| |Teton County|     0|  0.000| N/A|    15|  2440.215| N/A|   6,147|
| |Wibaux County|     0|  0.000| N/A|     3|  3095.975| N/A|     969|
| |Wheatland County|     0|  0.000| N/A|     3|  1411.101| N/A|   2,126|
| |Valley County|     0|  0.000| N/A|    13|  1757.707| N/A|   7,396|
| |Treasure County|     0|  0.000| N/A|     2|  2873.563| N/A|     696|
| |Stillwater County|     0|  0.000| N/A|    20|  2074.258| N/A|   9,642|
| |Silver Bow County|     0|  0.000| N/A|    75|  2148.074| N/A|  34,915|
| |Sheridan County|     0|  0.000| N/A|     4|  1208.824| N/A|   3,309|
| |Fallon County|     0|  0.000| N/A|     2|   702.741| N/A|   2,846|
| |Deer Lodge County|     0|  0.000| N/A|    23|  2516.411| N/A|   9,140|
| |Dawson County|     0|  0.000| N/A|    16|  1857.657| N/A|   8,613|
| |Daniels County|     0|  0.000| N/A|     3|  1775.148| N/A|   1,690|
| |Chouteau County|     0|  0.000| N/A|     7|  1242.236| N/A|   5,635|
| |Carter County|     0|  0.000| N/A|     0|     0.000| N/A|   1,252|
| |Park County|     0|  0.000| N/A|    54|  3251.837| N/A|  16,606|
| |Fergus County|     0|  0.000| N/A|     8|   723.982| N/A|  11,050|
| |Garfield County|     0|  0.000| N/A|    12|  9538.951| N/A|   1,258|
| |Golden Valley County|     0|  0.000| N/A|     3|  3654.080| N/A|     821|
| |Granite County|     0|  0.000| N/A|    13|  3847.292| N/A|   3,379|
| |Beaverhead County|     0|  0.000| N/A|    57|  6029.832| N/A|   9,453|
| |Blaine County|     0|  0.000| N/A|    10|  1496.782| N/A|   6,681|
| |Broadwater County|     0|  0.000| N/A|    11|  1763.668| N/A|   6,237|
| |Carbon County|     0|  0.000| N/A|    60|  5594.406| N/A|  10,725|
| |Mineral County|     0|  0.000| N/A|     0|     0.000| N/A|   4,397|
| |Meagher County|     0|  0.000| N/A|     4|  2148.228| N/A|   1,862|
| |McCone County|     0|  0.000| N/A|     2|  1201.923| N/A|   1,664|
| |Liberty County|     0|  0.000| N/A|     1|   427.899| N/A|   2,337|
| |Judith Basin County|     0|  0.000| N/A|     3|  1494.768| N/A|   2,007|
| |Jefferson County|     0|  0.000| N/A|    27|  2209.312| N/A|  12,221|
| |Hill County|     0|  0.000| N/A|    41|  2487.260| N/A|  16,484|


### Vermont ###

![Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Vermont.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|VT|14 counties|    57| 91.348| N/A| 1,428|  2288.502| N/A| 623,989|
| |Chittenden County|    39| 238.133|  0.000|   723|  4414.620|  6.165| 163,774|
| |Franklin County|     6| 121.453| N/A|   118|  2388.567| N/A|  49,402|
| |Windham County|     3| 71.053| N/A|   102|  2415.802| N/A|  42,222|
| |Windsor County|     2| 36.323| N/A|    71|  1289.456| N/A|  55,062|
| |Addison County|     2| 54.382| N/A|    73|  1984.936| N/A|  36,777|
| |Washington County|     2| 34.241| N/A|    52|   890.274| N/A|  58,409|
| |Rutland County|     1| 17.185| N/A|    92|  1581.000| N/A|  58,191|
| |Lamoille County|     1| 39.429| N/A|    42|  1656.021| N/A|  25,362|
| |Bennington County|     1| 28.193| N/A|    84|  2368.198| N/A|  35,470|
| |Orleans County|     0|  0.000| N/A|    14|   517.809| N/A|  27,037|
| |Orange County|     0|  0.000| N/A|    14|   484.563| N/A|  28,892|
| |Grand Isle County|     0|  0.000| N/A|    13|  1796.821| N/A|   7,235|
| |Caledonia County|     0|  0.000| N/A|    26|   866.869| N/A|  29,993|
| |Essex County|     0|  0.000| N/A|     4|   649.035| N/A|   6,163|


### Hawaii ###

![Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Hawaii.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|HI|5 counties|    26| 18.363| N/A| 2,740|  1935.203| N/A|1,415,872|
| |Honolulu County|    20| 20.522| N/A| 2,394|  2456.486| N/A| 974,563|
| |Maui County|     6| 35.839| N/A|   177|  1057.240| N/A| 167,417|
| |Kauai County|     0|  0.000| N/A|    47|   650.132| N/A|  72,293|
| |Hawaii County|     0|  0.000| N/A|   122|   605.420| N/A| 201,513|
| |Kalawao County|     0|  0.000| N/A|     0|     0.000| N/A|      86|


### Wyoming ###

![Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/counties/Wyoming.png)

|State|County|Deaths|Deaths/1M|Deaths/day/1M|Cases|Cases/1M|Cases/day/1M|Population|
|:--|:--|--:|--:|--:|--:|--:|--:|--:|
|WY|23 counties|     1|  1.728| N/A| 2,923|  5050.461| N/A| 578,759|
| |Johnson County|     1| 118.413| N/A|    22|  2605.092| N/A|   8,445|
| |Sweetwater County|     0|  0.000| N/A|   252|  5951.397| N/A|  42,343|
| |Sheridan County|     0|  0.000| N/A|    64|  2099.393| N/A|  30,485|
| |Platte County|     0|  0.000| N/A|     5|   595.735| N/A|   8,393|
| |Park County|     0|  0.000| N/A|   124|  4247.448| N/A|  29,194|
| |Niobrara County|     0|  0.000| N/A|     2|   848.896| N/A|   2,356|
| |Uinta County|     0|  0.000| N/A|   268| 13250.272| N/A|  20,226|
| |Teton County|     0|  0.000| N/A|   363| 15470.508| N/A|  23,464|
| |Big Horn County|     0|  0.000| N/A|    36|  3053.435| N/A|  11,790|
| |Washakie County|     0|  0.000| N/A|    58|  7431.134| N/A|   7,805|
| |Campbell County|     0|  0.000| N/A|   118|  2546.341| N/A|  46,341|
| |Hot Springs County|     0|  0.000| N/A|    19|  4305.461| N/A|   4,413|
| |Goshen County|     0|  0.000| N/A|    22|  1665.279| N/A|  13,211|
| |Fremont County|     0|  0.000| N/A|   496| 12633.402| N/A|  39,261|
| |Crook County|     0|  0.000| N/A|    10|  1318.565| N/A|   7,584|
| |Converse County|     0|  0.000| N/A|    32|  2315.150| N/A|  13,822|
| |Carbon County|     0|  0.000| N/A|    88|  5945.946| N/A|  14,800|
| |Lincoln County|     0|  0.000| N/A|    97|  4891.578| N/A|  19,830|
| |Albany County|     0|  0.000| N/A|    88|  2263.374| N/A|  38,880|
| |Laramie County|     0|  0.000| N/A|   489|  4914.573| N/A|  99,500|
| |Natrona County|     0|  0.000| N/A|   226|  2830.023| N/A|  79,858|
| |Sublette County|     0|  0.000| N/A|    39|  3967.043| N/A|   9,831|
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
| |Bristol Bay Borough|     0|  0.000| N/A|     0|     0.000| N/A|     836|
| |Lake and Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|   1,592|
| |Kusilvak Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   8,314|
| |Kodiak Island Borough|     0|  0.000| N/A|     0|     0.000| N/A|  12,998|
| |Ketchikan Gateway Borough|     0|  0.000| N/A|     0|     0.000| N/A|  13,901|
| |Kenai Peninsula Borough|     0|  0.000| N/A|     0|     0.000| N/A|  58,708|
| |Juneau Borough|     0|  0.000| N/A|     0|     0.000| N/A|  31,974|
| |Hoonah-Angoon Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   2,148|
| |Fairbanks North Star Borough|     0|  0.000| N/A|     0|     0.000| N/A|  96,849|
| |Dillingham Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   4,916|
| |Denali Borough|     0|  0.000| N/A|     0|     0.000| N/A|   2,097|
| |Bethel Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  18,386|
| |Anchorage Borough|     0|  0.000| N/A|     0|     0.000| N/A| 288,000|
| |Aleutians West Census Area|     0|  0.000| N/A|     0|     0.000| N/A|   5,634|
| |Aleutians East Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,337|
| |Nome Census Area|     0|  0.000| N/A|     0|     0.000| N/A|  10,004|
| |North Slope Borough|     0|  0.000| N/A|     0|     0.000| N/A|   9,832|
| |Northwest Arctic Borough|     0|  0.000| N/A|     0|     0.000| N/A|   7,621|
| |Petersburg Borough|     0|  0.000| N/A|     0|     0.000| N/A|   3,266|
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


