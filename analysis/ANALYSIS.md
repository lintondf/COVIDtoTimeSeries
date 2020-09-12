# State and Country COVID-19 Analysis #
## Updated: at 2020-09-12 for data as of 2020-09-11 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Deaths in Florida and California have followed nearly identical trajectories since early April 2020 with Florida somewhat higher, but both falling well below New York and above Texas.


![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to date from COVID-19 compared to historical seasonal flus and 20th century pandemics.  The number of deaths in each flu/pandemic is divided by the US population in millions at the time of the flu/pandemic.   In all cases the midpoint CDC estimate for fatalities is used.  In all cases except the Spanish Flu (1918) these are for a full year.  The vertical axis is limited for readability; the Spanish Flu was nearly 10 times more deadly than the 1957 Asian flu on a _per capita_ basis.

![Compared To Flus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/ComparedToFlus.png)


Daily Death Growth Rate (DDGR)  is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously; yes, technically this is a factor not a rate, but we must grant Professor Kling the author's naming rights.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate local-error minimizing non-parametric trend lines.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

Up until June 29, 2020, this page reported the DDGR directly, but as the high growth phase of the pandemic has passed, the DDGR values have  declined toward one, required progressively more digits of precision to show differences.  Accordingly, henceforth this page will report DDGR as a true growth percentage rate (100*(DDGR-1)) which will be termed the Daily Death Rate of Growth (DDRG).  A DDRG of 100% means the number of deaths doubles every day, 0% means no new deaths.


# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.7% of deaths and 57.0% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 164   |   33034|    1698.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 164   |   16004|    1801.863|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 164   |   14381|     363.974|   0.8%/ 90|   0.7%/100|   0.7%/104|   0.6%/107 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 164   |   14519|     500.714|   0.9%/ 74|   0.7%/ 93|   0.7%/ 99|   0.6%/106 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 164   |   12587|     586.063|   0.9%/ 80|   0.7%/ 96|   0.7%/101|   0.7%/106 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 164   |    9192|    1322.710|   0.1%/522|   0.1%/564|   0.1%/576|   0.1%/589 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 164   |    8486|     669.702|   0.3%/275|   0.3%/271|   0.3%/270|   0.3%/269 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 164   |    7833|     611.839|   0.2%/395|   0.2%/418|   0.2%/424|   0.2%/430 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 164   |    6880|     688.857|   0.2%/346|   0.2%/321|   0.2%/316|   0.2%/310 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 164   |    6370|     599.959|   1.0%/ 71|   0.9%/ 80|   0.8%/ 82|   0.8%/ 85 |


- Days - Number of days since first death
- Deaths - Total deaths to date
- Deaths/1M - Deaths per million in population
- DDRG - **LOWESS Smoothed** Daily Deaths Rate of Growth. [n:m] total deaths n days ago over m days ago followed by the DDRG expressed as the number of days to double the total deaths count if that rate holds

# Ten Countries with Highest Death Tolls #

Deaths in the 10 countries with the highest death tolls expressed as deaths per 1 million population. 

![Countries with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDeathRates.png)

Daily Death Rate of Growth (DDRG) in the 10 countries with the highest death tolls.

![Countries with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/Countries10WorstDDGR.png)

|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 164   |  193632|     587.576|   0.4%/161|   0.4%/174|   0.4%/178|   0.4%/182 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 164   |  131444|     621.744|   0.6%/109|   0.6%/121|   0.6%/124|   0.5%/127 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 164   |   77915|      57.239|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 164   |   70558|     557.425|   0.7%/ 93|   0.7%/ 99|   0.7%/101|   0.7%/103 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 164   |   41059|     618.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 164   |   35594|     590.885|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 164   |   30830|     459.624|   0.1%/ ***|   0.1%/ ***|   0.1%/991|   0.1%/972 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 164   |   31014|     965.230|   0.5%/136|   0.5%/152|   0.4%/157|   0.4%/161 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 164   |   29635|     629.179|   0.2%/397|   0.2%/348|   0.2%/338|   0.2%/328 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 164   |   23002|     275.878|   0.5%/129|   0.5%/140|   0.5%/143|   0.5%/146 |


# US and Selected States #

For each country and each US state, deaths per million in population is plotted on the left logarithmic axis and the raw and smoothed DDRG is plotted on the linear right axis.


## United States ##
![United States](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)

## Florida ##
![Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)

## Maryland ##
![Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)

## Maine ##
![Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)

# US States #

Click on the link in the first column to view the deaths and DDRG charts for a specific state.

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 164   |    2358|     480.887|   0.7%/106|   0.6%/118|   0.6%/122|   0.6%/126 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 164   |      45|      61.562|   0.8%/ 84|   0.7%/ 96|   0.7%/100|   0.7%/104 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 164   |    5383|     739.565|   0.5%/145|   0.4%/189|   0.3%/204|   0.3%/223 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 164   |     973|     322.472|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 164   |   14381|     363.974|   0.8%/ 90|   0.7%/100|   0.7%/104|   0.6%/107 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 164   |    1986|     344.810|   0.2%/399|   0.2%/412|   0.2%/416|   0.2%/419 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 164   |    4476|    1255.331|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 164   |     612|     628.770|   0.1%/631|   0.1%/641|   0.1%/644|   0.1%/646 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 164   |   12587|     586.063|   0.9%/ 80|   0.7%/ 96|   0.7%/101|   0.7%/106 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 164   |    6370|     599.959|   1.0%/ 71|   0.9%/ 80|   0.8%/ 82|   0.8%/ 85 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 164   |      99|      70.113|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 164   |     425|     238.065|   1.4%/ 50|   1.2%/ 57|   1.2%/ 59|   1.1%/ 61 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 164   |    8486|     669.702|   0.3%/275|   0.3%/271|   0.3%/270|   0.3%/269 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 164   |    3423|     508.484|   0.3%/222|   0.3%/231|   0.3%/234|   0.3%/236 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 164   |    1220|     386.643|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 164   |     502|     172.291|   1.0%/ 71|   1.0%/ 66|   1.1%/ 65|   1.1%/ 64 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 164   |    1041|     233.034|   0.9%/ 75|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 164   |    5240|    1127.247|   0.4%/154|   0.4%/182|   0.4%/191|   0.3%/201 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 164   |     135|     100.664|   0.1%/507|   0.1%/739|   0.1%/839|   0.1%/974 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 164   |    3836|     634.459|   0.2%/374|   0.2%/391|   0.2%/396|   0.2%/401 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 164   |    9192|    1322.710|   0.1%/522|   0.1%/564|   0.1%/576|   0.1%/589 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 164   |    6880|     688.857|   0.2%/346|   0.2%/321|   0.2%/316|   0.2%/310 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 164   |    1948|     345.451|   0.3%/198|   0.3%/216|   0.3%/221|   0.3%/226 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 164   |    2719|     913.696|   0.8%/ 90|   0.7%/105|   0.6%/110|   0.6%/115 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 164   |    1717|     279.717|   0.9%/ 80|   0.9%/ 76|   0.9%/ 75|   0.9%/ 75 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 164   |     127|     118.611|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 164   |     423|     218.621|   0.7%/ 96|   0.8%/ 89|   0.8%/ 87|   0.8%/ 85 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 164   |    1476|     479.105|   0.9%/ 80|   0.7%/ 98|   0.7%/104|   0.6%/111 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 164   |     435|     320.079|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 164   |   16004|    1801.863|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 164   |     824|     393.116|   0.5%/145|   0.4%/157|   0.4%/160|   0.4%/164 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 164   |   33034|    1698.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 164   |    3023|     288.222|   0.9%/ 73|   0.9%/ 74|   0.9%/ 75|   0.9%/ 75 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 164   |     162|     212.758|   1.0%/ 70|   1.0%/ 72|   1.0%/ 72|   1.0%/ 73 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 164   |    4385|     375.158|   0.5%/137|   0.5%/141|   0.5%/142|   0.5%/143 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 164   |     903|     228.099|   0.9%/ 75|   0.8%/ 86|   0.8%/ 89|   0.8%/ 92 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 164   |     507|     120.110|   0.9%/ 81|   0.8%/ 88|   0.8%/ 90|   0.7%/ 93 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 164   |    7833|     611.839|   0.2%/395|   0.2%/418|   0.2%/424|   0.2%/430 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 164   |     520|     162.848|   1.6%/ 44|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 164   |    1067|    1006.760|   0.2%/378|   0.2%/358|   0.2%/354|   0.2%/349 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 164   |    3058|     593.896|   0.9%/ 76|   0.8%/ 87|   0.8%/ 90|   0.7%/ 94 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 164   |     177|     200.630|   0.5%/137|   0.5%/149|   0.5%/152|   0.4%/155 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 164   |    2031|     297.283|   1.2%/ 55|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 164   |   14519|     500.714|   0.9%/ 74|   0.7%/ 93|   0.7%/ 99|   0.6%/106 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 164   |  193632|     587.576|   0.4%/161|   0.4%/174|   0.4%/178|   0.4%/182 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 164   |     437|     136.198|   0.5%/136|   0.4%/166|   0.4%/176|   0.4%/187 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 164   |      58|      92.953|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 164   |    2740|     321.045|   0.5%/147|   0.5%/154|   0.4%/156|   0.4%/159 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 164   |    2004|     263.204|   0.3%/207|   0.3%/255|   0.3%/270|   0.2%/287 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 164   |     271|     151.426|   1.7%/ 39|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 164   |    1198|     205.712|   0.5%/126|   0.5%/128|   0.5%/128|   0.5%/129 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 152   |      44|      75.691|   0.1%/494|   0.1%/871|   0.1%/ ***|   0.1%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 164   |    1426|      44.250|   0.1%/725|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 164   |     337|     118.321|   1.3%/ 52|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 164   |    1605|      37.330|   0.5%/126|   0.5%/134|   0.5%/136|   0.5%/138 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 164   |     129|       4.158|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 164   |   11379|     253.220|   2.3%/ 30|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 164   |     916|     309.577|   0.3%/210|   0.3%/242|   0.3%/252|   0.3%/262 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 164   |     899|      35.007|   1.7%/ 40|   1.3%/ 54|   1.2%/ 60|   1.0%/ 66 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 164   |     744|      83.586|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 164   |     558|      55.409|   0.4%/175|   0.4%/173|   0.4%/172|   0.4%/172 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 164   |     206|     133.327|   0.7%/ 96|   0.7%/ 96|   0.7%/ 95|   0.7%/ 95 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 164   |    4712|      27.969|   0.9%/ 81|   0.8%/ 87|   0.8%/ 88|   0.8%/ 90 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 164   |     737|      78.344|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 91 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 164   |    9910|     859.873|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 159   |      40|       3.439|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 164   |    5900|     514.368|   1.2%/ 60|   1.0%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 164   |     706|     214.022|   1.2%/ 59|   1.0%/ 67|   1.0%/ 69|   1.0%/ 72 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 164   |      10|       4.179|   6.9%/ 10|   7.7%/  9|   7.8%/  9|   8.0%/  8 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 164   |  131444|     621.744|   0.6%/109|   0.6%/121|   0.6%/124|   0.5%/127 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 164   |     725|     104.349|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 164   |      56|       2.671|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 152   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 164   |     418|      15.732|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 164   |    9225|     242.769|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 112   |      62|      11.327|   0.1%/887|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 137   |      79|       4.855|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 164   |   11874|     621.430|   0.4%/155|   0.4%/163|   0.4%/165|   0.4%/168 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 164   |    4738|       3.379|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 164   |   23116|     467.971|   1.3%/ 52|   1.2%/ 59|   1.1%/ 61|   1.1%/ 63 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 164   |     570|     112.649|   2.6%/ 27|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 164   |     208|      50.980|   1.1%/ 62|   1.2%/ 57|   1.2%/ 56|   1.3%/ 55 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 164   |     105|       9.357|   0.8%/ 84|   1.0%/ 72|   1.0%/ 70|   1.0%/ 68 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 164   |     629|     107.975|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 164   |    1954|     188.652|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63|   1.1%/ 63 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 164   |    6922|     396.270|   0.5%/137|   0.5%/135|   0.5%/135|   0.5%/135 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 164   |    5618|      56.030|   0.3%/216|   0.3%/221|   0.3%/223|   0.3%/224 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 164   |     795|     122.576|   0.8%/ 91|   0.6%/110|   0.6%/116|   0.6%/123 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 143   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 160   |    1038|      10.519|   1.9%/ 36|   1.6%/ 43|   1.5%/ 46|   1.4%/ 48 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 164   |     337|      60.963|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 164   |   30830|     459.624|   0.1%/ ***|   0.1%/ ***|   0.1%/991|   0.1%/972 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 164   |      53|      24.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 164   |     119|      50.687|   0.7%/101|   0.0%/ --|   0.3%/206|   0.3%/206 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 161   |      20|       5.249|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 164   |    9353|     112.485|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 164   |     295|       9.736|   0.3%/219|   0.1%/881|   0.0%/ ***|   0.0%/ -- |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 164   |     300|      27.970|   1.1%/ 64|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 164   |    2985|     179.785|   0.6%/114|   0.5%/144|   0.5%/154|   0.4%/165 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 150   |      64|       5.262|   0.7%/ 96|   0.6%/108|   0.6%/112|   0.6%/116 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 139   |      39|      24.099|   0.6%/125|   0.7%/106|   0.7%/102|   0.7%/ 98 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 160   |     216|      18.660|   0.5%/151|   0.5%/149|   0.5%/148|   0.5%/147 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 164   |    2109|     230.228|   1.0%/ 69|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 164   |     628|      64.233|   0.2%/378|   0.2%/331|   0.2%/321|   0.2%/311 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 164   |   77915|      57.239|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 164   |    8547|      32.021|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 164   |   23002|     275.878|   0.5%/129|   0.5%/140|   0.5%/143|   0.5%/146 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 164   |    7954|     203.289|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 164   |    1779|     361.556|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 164   |    1118|     121.729|   1.4%/ 50|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 164   |   35594|     590.885|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 164   |      40|      14.641|  10.1%/  7|   4.8%/ 14|   5.6%/ 12|   3.6%/ 19 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 164   |    1440|      11.434|   1.0%/ 72|   1.0%/ 73|   0.9%/ 73|   0.9%/ 73 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 164   |      17|       1.640|   2.2%/ 32|   5.9%/ 12|   5.6%/ 12|   3.4%/ 20 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 164   |    1690|      90.423|   0.6%/116|   0.4%/159|   0.4%/175|   0.4%/194 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 164   |     631|      13.272|   0.6%/115|   0.4%/181|   0.3%/210|   0.3%/250 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 164   |     523|     291.192|   0.1%/707|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 161   |     556|     125.755|   0.4%/164|   0.4%/165|   0.4%/164|   0.4%/164 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 162   |     986|     150.925|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 162   |      35|      18.520|   0.3%/258|   0.3%/272|   0.3%/276|   0.2%/282 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 164   |     229|      33.552|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 161   |      82|      18.345|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 163   |     338|      49.254|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 164   |      87|      31.218|   0.1%/737|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 118   |     210|       7.997|   0.8%/ 84|   0.8%/ 86|   0.8%/ 86|   0.8%/ 87 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 164   |     128|       3.919|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 164   |     127|       6.288|   0.1%/473|   0.2%/385|   0.2%/367|   0.2%/350 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 164   |     161|      39.427|   0.1%/572|   0.1%/499|   0.1%/483|   0.1%/469 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 164   |   70558|     557.425|   0.7%/ 93|   0.7%/ 99|   0.7%/101|   0.7%/103 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 164   |    1109|     413.439|   0.9%/ 76|   0.9%/ 73|   1.0%/ 72|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 164   |    1690|      47.100|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 110   |      30|       1.006|   2.5%/ 28|   2.8%/ 24|   2.9%/ 23|   3.0%/ 23 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  64   |      98|      39.832|   2.8%/ 25|   1.6%/ 42|   1.4%/ 50|   1.2%/ 59 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 119   |     354|      11.817|   3.7%/ 19|   2.9%/ 23|   2.7%/ 25|   2.5%/ 27 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 164   |    6294|     360.537|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 164   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 164   |     145|      22.454|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 164   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 164   |    1074|       5.210|   0.4%/170|   0.4%/162|   0.4%/161|   0.4%/159 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 164   |     641|     308.655|   0.7%/104|   0.7%/103|   0.7%/102|   0.7%/102 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 164   |     265|      49.410|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 164   |     767|     164.399|   1.1%/ 64|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 164   |    6388|      29.126|   0.1%/655|   0.1%/757|   0.1%/787|   0.1%/820 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 164   |    2167|     513.606|   0.6%/114|   0.5%/134|   0.5%/140|   0.5%/146 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  47   |       5|       0.560|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 164   |     572|      79.903|   4.5%/ 15|   3.9%/ 17|   3.8%/ 18|   3.7%/ 19 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 164   |   31014|     965.230|   0.5%/136|   0.5%/152|   0.4%/157|   0.4%/161 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 164   |    4211|      38.810|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 164   |    2178|      56.744|   0.5%/131|   0.5%/136|   0.5%/138|   0.5%/139 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 164   |    1855|     180.525|   0.2%/424|   0.2%/427|   0.2%/428|   0.2%/429 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 164   |     205|      74.711|   0.3%/229|   0.3%/222|   0.3%/220|   0.3%/218 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 164   |    4144|     213.548|   1.2%/ 60|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 164   |   18323|     124.864|   0.6%/117|   0.6%/119|   0.6%/120|   0.6%/120 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 105   |      22|       1.771|   1.9%/ 36|   3.4%/ 20|   5.0%/ 14|   3.2%/ 21 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 164   |    4256|     124.391|   0.7%/ 94|   0.7%/103|   0.7%/105|   0.6%/108 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 164   |     301|      18.544|   0.4%/182|   0.2%/297|   0.2%/352|   0.2%/434 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 164   |     737|     105.814|   0.2%/337|   0.1%/535|   0.1%/623|   0.1%/745 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 142   |      72|       9.111|   0.2%/289|   0.3%/250|   0.3%/242|   0.3%/235 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 164   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 164   |      38|       6.897|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 164   |     136|      64.914|   0.1%/577|   0.1%/761|   0.1%/828|   0.1%/909 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 157   |      98|       6.187|   0.1%/717|   0.1%/963|   0.1%/ ***|   0.1%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 164   |   15723|     267.510|   0.8%/ 90|   0.6%/117|   0.5%/126|   0.5%/137 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 164   |   29635|     629.179|   0.2%/397|   0.2%/348|   0.2%/338|   0.2%/328 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 164   |      12|       0.562|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 164   |     838|      19.745|   0.1%/676|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 164   |    5846|     565.475|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 164   |    2020|     234.761|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 164   |     158|       9.002|   2.7%/ 26|   2.6%/ 27|   2.6%/ 27|   2.5%/ 27 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 164   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 164   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 164   |      34|       4.521|   1.5%/ 45|   1.9%/ 36|   2.0%/ 34|   2.1%/ 32 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 164   |      45|      33.282|   6.7%/ 10|   7.1%/ 10|   7.2%/  9|   7.3%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 164   |     101|       8.636|   2.0%/ 35|   2.1%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 164   |    6668|      80.184|   0.7%/ 94|   0.8%/ 84|   0.9%/ 81|   0.9%/ 79 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 164   |  193632|     587.576|   0.4%/161|   0.4%/174|   0.4%/178|   0.4%/182 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  50   |      51|       1.256|   5.0%/ 14|   4.3%/ 16|   3.7%/ 19|   3.0%/ 23 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 164   |    3114|      74.351|   1.6%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 164   |     397|      40.122|   0.3%/199|   0.4%/197|   0.4%/196|   0.4%/196 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 164   |   41059|     618.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 164   |      46|      13.165|   0.3%/217|   0.2%/420|   0.1%/552|   0.1%/808 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 164   |     385|      11.286|   1.6%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 164   |     476|      14.776|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  43   |      35|       0.364|   0.7%/101|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 163   |     305|      17.081|   0.4%/162|   0.3%/206|   0.3%/220|   0.3%/235 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 164   |     239|      15.738|   0.3%/200|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

