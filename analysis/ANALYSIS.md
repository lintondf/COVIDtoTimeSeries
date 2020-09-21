# State and Country COVID-19 Analysis #
## Updated: at 2020-09-21 for data as of 2020-09-20 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.2% of deaths and 56.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 173   |   33085|    1700.692|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 173   |   16065|    1808.713|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 173   |   15369|     530.044|   0.7%/ 93|   0.6%/110|   0.6%/115|   0.6%/121 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 173   |   15192|     384.481|   0.7%/103|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 173   |   13447|     626.098|   0.8%/ 83|   0.8%/ 89|   0.8%/ 91|   0.7%/ 92 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 173   |    9301|    1338.372|   0.1%/492|   0.1%/497|   0.1%/498|   0.1%/498 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 173   |    8686|     685.481|   0.3%/268|   0.3%/265|   0.3%/265|   0.3%/264 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 173   |    7945|     620.640|   0.2%/378|   0.2%/376|   0.2%/375|   0.2%/373 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 173   |    6988|     699.723|   0.1%/522|   0.1%/556|   0.1%/566|   0.1%/576 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 173   |    6738|     634.659|   0.7%/ 96|   0.6%/113|   0.6%/118|   0.6%/124 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 173   |  200315|     607.855|   0.4%/170|   0.4%/178|   0.4%/180|   0.4%/182 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 173   |  137773|     651.682|   0.6%/120|   0.5%/128|   0.5%/131|   0.5%/133 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 173   |   87672|      64.407|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 173   |   74297|     586.967|   0.6%/114|   0.6%/125|   0.5%/128|   0.5%/131 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 173   |   41820|     629.476|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 173   |   35682|     592.353|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 173   |   31614|     983.890|   0.4%/172|   0.4%/195|   0.3%/202|   0.3%/210 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 173   |   31107|     463.759|   0.1%/574|   0.1%/495|   0.1%/477|   0.2%/461 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 173   |   30308|     643.485|   0.2%/352|   0.2%/326|   0.2%/320|   0.2%/314 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 173   |   24178|     289.982|   0.6%/116|   0.6%/115|   0.6%/114|   0.6%/114 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 173   |    2470|     503.730|   0.6%/120|   0.5%/134|   0.5%/138|   0.5%/142 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 173   |      47|      64.706|   0.7%/101|   0.6%/122|   0.5%/129|   0.5%/137 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 173   |    5520|     758.358|   0.4%/176|   0.3%/208|   0.3%/217|   0.3%/227 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 173   |    1180|     391.054|   1.2%/ 60|   0.9%/ 73|   0.9%/ 77|   0.8%/ 82 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 173   |   15192|     384.481|   0.7%/103|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 173   |    2016|     350.008|   0.2%/395|   0.2%/399|   0.2%/400|   0.2%/400 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 173   |    4490|    1259.330|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 173   |     621|     637.253|   0.1%/495|   0.1%/468|   0.2%/461|   0.2%/454 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 173   |   13447|     626.098|   0.8%/ 83|   0.8%/ 89|   0.8%/ 91|   0.7%/ 92 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 173   |    6738|     634.659|   0.7%/ 96|   0.6%/113|   0.6%/118|   0.6%/124 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 173   |     125|      88.359|   2.8%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 173   |     455|     254.830|   0.9%/ 75|   0.8%/ 91|   0.7%/ 96|   0.7%/101 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 173   |    8686|     685.481|   0.3%/268|   0.3%/265|   0.3%/265|   0.3%/264 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 173   |    3514|     521.898|   0.3%/230|   0.3%/234|   0.3%/235|   0.3%/236 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 173   |    1285|     407.205|   0.6%/114|   0.6%/125|   0.5%/128|   0.5%/132 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 173   |     559|     191.751|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 173   |    1123|     251.271|   0.8%/ 85|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 173   |    5400|    1161.569|   0.4%/182|   0.3%/206|   0.3%/212|   0.3%/219 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 173   |     138|     102.938|   0.3%/263|   0.3%/248|   0.3%/244|   0.3%/239 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 173   |    3887|     642.925|   0.2%/436|   0.1%/467|   0.1%/476|   0.1%/485 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 173   |    9301|    1338.372|   0.1%/492|   0.1%/497|   0.1%/498|   0.1%/498 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 173   |    6988|     699.723|   0.1%/522|   0.1%/556|   0.1%/566|   0.1%/576 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 173   |    2017|     357.579|   0.4%/180|   0.4%/180|   0.4%/179|   0.4%/179 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 173   |    2854|     959.078|   0.6%/110|   0.6%/125|   0.5%/130|   0.5%/135 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 173   |    1840|     299.819|   0.8%/ 91|   0.8%/ 92|   0.8%/ 92|   0.7%/ 92 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 173   |     153|     143.024|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 173   |     448|     231.836|   0.4%/155|   0.4%/168|   0.4%/172|   0.4%/177 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 173   |    1554|     504.365|   0.7%/ 93|   0.7%/106|   0.6%/109|   0.6%/113 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 173   |     438|     322.365|   0.1%/913|   0.1%/946|   0.1%/951|   0.1%/956 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 173   |   16065|    1808.713|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 173   |     851|     406.078|   0.4%/166|   0.4%/177|   0.4%/180|   0.4%/183 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 173   |   33085|    1700.692|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 173   |    3263|     311.135|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80|   0.9%/ 80 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 173   |     184|     242.089|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 173   |    4616|     394.925|   0.6%/121|   0.6%/118|   0.6%/117|   0.6%/117 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 173   |     962|     243.044|   0.8%/ 88|   0.7%/ 99|   0.7%/102|   0.7%/105 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 173   |     537|     127.338|   0.6%/108|   0.5%/127|   0.5%/133|   0.5%/140 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 173   |    7945|     620.640|   0.2%/378|   0.2%/376|   0.2%/375|   0.2%/373 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 173   |     606|     189.808|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 173   |    1087|    1026.555|   0.2%/329|   0.2%/310|   0.2%/306|   0.2%/301 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 173   |    3256|     632.361|   0.8%/ 92|   0.7%/104|   0.6%/108|   0.6%/112 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 173   |     194|     219.682|   1.1%/ 64|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 173   |    2256|     330.210|   1.1%/ 60|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 173   |   15369|     530.044|   0.7%/ 93|   0.6%/110|   0.6%/115|   0.6%/121 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 173   |  200315|     607.855|   0.4%/170|   0.4%/178|   0.4%/180|   0.4%/182 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 173   |     447|     139.369|   0.3%/233|   0.2%/334|   0.2%/375|   0.2%/426 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 173   |      58|      92.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 173   |    2929|     343.208|   0.8%/ 90|   0.8%/ 82|   0.9%/ 80|   0.9%/ 78 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 173   |    2049|     269.038|   0.3%/234|   0.3%/258|   0.3%/265|   0.3%/272 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 173   |     316|     176.078|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 173   |    1251|     214.834|   0.5%/147|   0.4%/154|   0.4%/157|   0.4%/159 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 161   |      48|      83.195|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 173   |    1438|      44.634|   0.1%/539|   0.1%/538|   0.1%/536|   0.1%/534 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 173   |     367|     128.987|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 173   |    1678|      39.031|   0.5%/137|   0.5%/143|   0.5%/144|   0.5%/146 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 173   |     150|       4.823|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 173   |   13381|     297.771|   1.9%/ 35|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 173   |     936|     316.461|   0.3%/265|   0.2%/309|   0.2%/322|   0.2%/336 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 173   |    1048|      40.820|   0.9%/ 80|   0.5%/153|   0.3%/198|   0.2%/280 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 173   |     763|      85.668|   0.2%/345|   0.2%/292|   0.2%/281|   0.3%/270 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 173   |     577|      57.342|   0.4%/187|   0.4%/191|   0.4%/192|   0.4%/194 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 173   |     221|     143.410|   0.8%/ 89|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 173   |    5000|      29.681|   0.7%/101|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 173   |     786|      83.584|   0.7%/103|   0.7%/106|   0.6%/107|   0.6%/108 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 173   |    9944|     862.820|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 168   |      40|       3.424|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 173   |    7954|     693.451|   0.7%/100|   0.5%/133|   0.5%/145|   0.4%/159 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 173   |     771|     233.561|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 173   |      15|       6.509|   4.9%/ 14|   4.5%/ 15|   4.3%/ 16|   4.2%/ 16 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 173   |  137773|     651.682|   0.6%/120|   0.5%/128|   0.5%/131|   0.5%/133 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 173   |     783|     112.612|   0.9%/ 78|   0.8%/ 92|   0.7%/ 97|   0.7%/102 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 173   |      56|       2.692|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 161   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 173   |     417|      15.717|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 173   |    9264|     243.797|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 121   |      62|      11.297|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 146   |      81|       5.014|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 173   |   12321|     644.860|   0.4%/163|   0.4%/169|   0.4%/170|   0.4%/171 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 173   |    4741|       3.381|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 173   |   24916|     504.426|   0.9%/ 75|   0.7%/ 93|   0.7%/ 98|   0.7%/105 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 173   |     715|     141.411|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27|   2.6%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 173   |     243|      59.685|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 173   |     113|      10.112|   0.9%/ 81|   0.9%/ 75|   0.9%/ 74|   1.0%/ 73 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 173   |     635|     109.038|   0.1%/661|   0.1%/582|   0.1%/565|   0.1%/548 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 173   |    2108|     203.483|   0.8%/ 86|   0.7%/ 99|   0.7%/103|   0.6%/107 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 173   |    7223|     413.499|   0.4%/194|   0.3%/217|   0.3%/223|   0.3%/231 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 173   |    5775|      57.593|   0.3%/222|   0.3%/226|   0.3%/228|   0.3%/229 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 173   |     826|     127.413|   0.5%/131|   0.4%/168|   0.4%/181|   0.4%/195 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 152   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 169   |    1142|      11.578|   1.3%/ 52|   1.1%/ 65|   1.0%/ 69|   0.9%/ 74 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 173   |     339|      61.303|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 173   |   31107|     463.759|   0.1%/574|   0.1%/495|   0.1%/477|   0.2%/461 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 173   |      53|      24.415|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 173   |     108|      45.954|   1.0%/ 70|   0.9%/ 73|   0.3%/223|   0.3%/223 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 170   |      19|       5.175|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 173   |    9389|     112.912|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 173   |     299|       9.883|   0.3%/211|   0.3%/272|   0.2%/292|   0.2%/313 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 173   |     333|      31.058|   1.2%/ 57|   1.3%/ 54|   1.3%/ 54|   1.3%/ 53 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 173   |    3113|     187.463|   0.6%/113|   0.6%/119|   0.6%/120|   0.6%/122 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 159   |      65|       5.311|   0.2%/311|   0.1%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 148   |      40|      25.168|   0.2%/330|   0.1%/475|   0.1%/542|   0.1%/635 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 169   |     224|      19.391|   0.4%/189|   0.3%/211|   0.3%/219|   0.3%/228 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 173   |    2219|     242.300|   0.7%/ 99|   0.6%/119|   0.6%/126|   0.5%/133 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 173   |     641|      65.622|   0.6%/120|   0.7%/ 98|   0.7%/ 93|   0.8%/ 89 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 173   |   87672|      64.407|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 173   |    9575|      35.872|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 173   |   24178|     289.982|   0.6%/116|   0.6%/115|   0.6%/114|   0.6%/114 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 173   |    8622|     220.349|   0.9%/ 73|   0.9%/ 77|   0.9%/ 78|   0.9%/ 79 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 173   |    1788|     363.381|   0.1%/ ***|   0.1%/ ***|   0.1%/969|   0.1%/926 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 173   |    1241|     135.113|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 173   |   35682|     592.353|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 173   |      59|      21.669|   5.5%/ 12|   5.8%/ 12|   5.9%/ 12|   6.0%/ 11 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 173   |    1537|      12.199|   0.7%/ 95|   0.6%/107|   0.6%/110|   0.6%/113 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 173   |      29|       2.750|   4.0%/ 17|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 173   |    1709|      91.487|   0.3%/216|   0.2%/325|   0.2%/371|   0.2%/433 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 173   |     654|      13.753|   0.5%/128|   0.5%/148|   0.5%/154|   0.4%/159 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 173   |     499|     278.157|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 170   |     581|     131.340|   0.5%/135|   0.5%/127|   0.6%/125|   0.6%/123 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 171   |    1046|     160.075|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 171   |      36|      18.866|   0.3%/246|   0.3%/246|   0.3%/245|   0.3%/244 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 173   |     297|      43.445|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 170   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 172   |     447|      65.026|   3.1%/ 22|   3.1%/ 23|   3.1%/ 23|   3.0%/ 23 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 173   |      87|      31.293|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 127   |     222|       8.447|   0.7%/103|   0.6%/113|   0.6%/115|   0.6%/118 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 173   |     129|       3.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 173   |     128|       6.345|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 173   |     162|      39.647|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 173   |   74297|     586.967|   0.6%/114|   0.6%/125|   0.5%/128|   0.5%/131 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 173   |    1201|     447.913|   0.9%/ 74|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 173   |    1913|      53.335|   2.2%/ 32|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 119   |      43|       1.423|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  73   |     113|      46.034|   1.7%/ 40|   1.4%/ 49|   1.3%/ 52|   1.2%/ 56 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 128   |     426|      14.203|   2.6%/ 26|   2.1%/ 33|   2.0%/ 35|   1.8%/ 38 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 173   |    6321|     362.066|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 173   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 173   |     148|      22.975|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 173   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 173   |    1107|       5.370|   0.3%/227|   0.3%/244|   0.3%/250|   0.3%/256 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 173   |     686|     330.149|   0.8%/ 87|   0.8%/ 82|   0.9%/ 81|   0.9%/ 80 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 173   |     266|      49.567|   0.1%/949|   0.1%/771|   0.1%/733|   0.1%/698 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 173   |     840|     180.026|   1.0%/ 67|   1.0%/ 69|   1.0%/ 69|   1.0%/ 70 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 173   |    6432|      29.325|   0.1%/796|   0.1%/902|   0.1%/932|   0.1%/965 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 173   |    2265|     536.913|   0.6%/121|   0.5%/130|   0.5%/133|   0.5%/135 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  56   |       7|       0.733|   2.4%/ 28|   1.9%/ 36|   1.7%/ 40|   1.5%/ 46 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 173   |     705|      98.594|   3.2%/ 22|   2.6%/ 26|   2.5%/ 28|   2.4%/ 29 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 173   |   31614|     983.890|   0.4%/172|   0.4%/195|   0.3%/202|   0.3%/210 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 173   |    5004|      46.112|   1.6%/ 43|   1.6%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 173   |    2288|      59.612|   0.6%/119|   0.6%/118|   0.6%/117|   0.6%/117 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 173   |    1894|     184.283|   0.3%/275|   0.3%/249|   0.3%/243|   0.3%/237 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 173   |     210|      76.614|   0.3%/244|   0.3%/247|   0.3%/249|   0.3%/250 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 173   |    4493|     231.557|   1.0%/ 71|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 173   |   19327|     131.704|   0.6%/112|   0.6%/111|   0.6%/111|   0.6%/111 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 114   |      26|       2.074|   2.4%/ 28|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 173   |    4506|     131.690|   0.7%/101|   0.6%/107|   0.6%/108|   0.6%/109 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 173   |     305|      18.846|   0.3%/246|   0.2%/347|   0.2%/385|   0.2%/431 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 173   |     744|     106.879|   0.2%/427|   0.1%/547|   0.1%/586|   0.1%/631 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 151   |      73|       9.183|   0.1%/878|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 173   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 173   |      40|       7.253|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 173   |     137|      65.572|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 166   |      99|       6.210|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 173   |   16294|     277.229|   0.5%/133|   0.4%/176|   0.4%/191|   0.3%/209 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 173   |   30308|     643.485|   0.2%/352|   0.2%/326|   0.2%/320|   0.2%/314 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 173   |      13|       0.591|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 173   |     840|      19.799|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 173   |    5865|     567.267|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 173   |    2031|     236.001|   0.1%/ ***|   0.1%/947|   0.1%/931|   0.1%/914 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 173   |     183|      10.454|   1.9%/ 36|   1.6%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 173   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 173   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 173   |      42|       5.588|   1.7%/ 41|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 173   |      74|      54.170|   4.9%/ 14|   4.4%/ 16|   4.3%/ 16|   4.2%/ 17 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 173   |     125|      10.666|   2.5%/ 27|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 173   |    7422|      89.250|   0.9%/ 81|   0.9%/ 74|   0.9%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 173   |  200315|     607.855|   0.4%/170|   0.4%/178|   0.4%/180|   0.4%/182 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  59   |      65|       1.602|   3.4%/ 20|   2.2%/ 31|   1.9%/ 36|   1.6%/ 44 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 173   |    3627|      86.606|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 173   |     406|      41.097|   0.2%/284|   0.2%/315|   0.2%/323|   0.2%/333 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 173   |   41820|     629.476|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 173   |      46|      13.172|   0.2%/369|   0.1%/669|   0.1%/823|   0.1%/ *** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 173   |     437|      12.807|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 173   |     551|      17.091|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  52   |      35|       0.364|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 172   |     329|      18.370|   0.7%/103|   0.7%/ 98|   0.7%/ 97|   0.7%/ 95 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 173   |     242|      15.962|   0.2%/324|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

