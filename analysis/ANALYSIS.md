# State and Country COVID-19 Analysis #
## Updated: at 2020-09-04 for data as of 2020-09-03 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.0% of deaths and 57.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 156   |   32981|    1695.356|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 156   |   15963|    1797.241|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 156   |   13578|     343.648|   0.9%/ 73|   0.9%/ 80|   0.8%/ 82|   0.8%/ 84 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 156   |   13723|     473.274|   1.3%/ 54|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 156   |   11911|     554.570|   1.1%/ 62|   0.9%/ 76|   0.9%/ 81|   0.8%/ 86 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 156   |    9097|    1308.981|   0.1%/468|   0.1%/492|   0.1%/499|   0.1%/506 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 156   |    8311|     655.880|   0.2%/278|   0.3%/271|   0.3%/269|   0.3%/267 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 156   |    7728|     603.692|   0.2%/355|   0.2%/373|   0.2%/377|   0.2%/383 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 156   |    6781|     679.023|   0.2%/396|   0.2%/374|   0.2%/369|   0.2%/364 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 156   |    5906|     556.249|   1.2%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 156   |  187505|     568.983|   0.5%/138|   0.5%/149|   0.5%/152|   0.4%/155 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 156   |  125396|     593.137|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 156   |   69369|      50.961|   1.6%/ 43|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 156   |   66823|     527.923|   0.8%/ 82|   0.8%/ 90|   0.7%/ 92|   0.7%/ 95 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 156   |   41391|     623.030|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 156   |   35540|     589.993|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 156   |   30682|     457.424|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 156   |   29170|     619.308|   0.1%/623|   0.1%/543|   0.1%/526|   0.1%/510 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 156   |   30610|     952.655|   0.6%/118|   0.5%/138|   0.5%/144|   0.5%/150 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 156   |   22155|     265.723|   0.6%/121|   0.5%/142|   0.5%/149|   0.4%/156 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 156   |    2233|     455.482|   0.9%/ 79|   0.8%/ 82|   0.8%/ 82|   0.8%/ 83 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 156   |      40|      54.472|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 156   |    5205|     715.069|   0.7%/106|   0.5%/134|   0.5%/143|   0.4%/154 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 156   |     843|     279.374|   2.0%/ 35|   2.1%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 156   |   13578|     343.648|   0.9%/ 73|   0.9%/ 80|   0.8%/ 82|   0.8%/ 84 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 156   |    1957|     339.871|   0.2%/393|   0.2%/412|   0.2%/417|   0.2%/423 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 156   |    4470|    1253.802|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 156   |     608|     623.984|   0.1%/692|   0.1%/750|   0.1%/768|   0.1%/789 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 156   |   11911|     554.570|   1.1%/ 62|   0.9%/ 76|   0.9%/ 81|   0.8%/ 86 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 156   |    5906|     556.249|   1.2%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 156   |      72|      51.101|   4.3%/ 16|   4.8%/ 14|   5.0%/ 14|   5.1%/ 13 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 156   |     387|     216.319|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 156   |    8311|     655.880|   0.2%/278|   0.3%/271|   0.3%/269|   0.3%/267 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 156   |    3344|     496.764|   0.3%/209|   0.3%/221|   0.3%/225|   0.3%/228 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 156   |    1146|     363.071|   0.8%/ 88|   0.8%/ 89|   0.8%/ 90|   0.8%/ 90 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 156   |     465|     159.709|   0.8%/ 92|   0.7%/ 92|   0.7%/ 93|   0.7%/ 93 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 156   |     967|     216.436|   1.0%/ 70|   1.0%/ 66|   1.1%/ 66|   1.1%/ 65 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 156   |    5088|    1094.448|   0.6%/117|   0.5%/133|   0.5%/137|   0.5%/142 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 156   |     134|      99.411|   0.2%/309|   0.2%/332|   0.2%/340|   0.2%/349 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 156   |    3779|     625.099|   0.2%/345|   0.2%/360|   0.2%/363|   0.2%/367 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 156   |    9097|    1308.981|   0.1%/468|   0.1%/492|   0.1%/499|   0.1%/506 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 156   |    6781|     679.023|   0.2%/396|   0.2%/374|   0.2%/369|   0.2%/364 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 156   |    1899|     336.702|   0.4%/175|   0.4%/187|   0.4%/190|   0.4%/194 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 156   |    2572|     864.226|   1.0%/ 66|   1.0%/ 72|   0.9%/ 74|   0.9%/ 75 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 156   |    1575|     256.623|   0.8%/ 91|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 156   |     111|     103.433|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 156   |     404|     209.091|   0.6%/123|   0.5%/129|   0.5%/130|   0.5%/132 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 156   |    1391|     451.465|   1.2%/ 59|   1.0%/ 69|   1.0%/ 72|   0.9%/ 75 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 156   |     434|     319.233|   0.1%/706|   0.1%/858|   0.1%/912|   0.1%/977 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 156   |   15963|    1797.241|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 156   |     794|     378.732|   0.6%/118|   0.6%/121|   0.6%/121|   0.6%/122 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 156   |   32981|    1695.356|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 156   |    2810|     267.934|   0.9%/ 74|   0.9%/ 77|   0.9%/ 78|   0.9%/ 79 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 156   |     150|     196.927|   1.0%/ 69|   0.9%/ 74|   0.9%/ 75|   0.9%/ 76 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 156   |    4223|     361.280|   0.5%/133|   0.5%/138|   0.5%/140|   0.5%/141 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 156   |     840|     212.204|   1.2%/ 58|   1.2%/ 60|   1.1%/ 61|   1.1%/ 61 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 156   |     476|     112.757|   1.0%/ 66|   1.0%/ 70|   1.0%/ 70|   1.0%/ 71 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 156   |    7728|     603.692|   0.2%/355|   0.2%/373|   0.2%/377|   0.2%/383 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 156   |     474|     148.333|   1.5%/ 45|   1.2%/ 55|   1.2%/ 59|   1.1%/ 63 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 156   |    1053|     993.571|   0.2%/403|   0.2%/370|   0.2%/363|   0.2%/357 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 156   |    2864|     556.313|   1.1%/ 61|   1.0%/ 69|   1.0%/ 72|   0.9%/ 74 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 156   |     171|     193.369|   0.5%/130|   0.4%/154|   0.4%/161|   0.4%/169 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 156   |    1863|     272.595|   1.5%/ 47|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 156   |   13723|     473.274|   1.3%/ 54|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 156   |  187505|     568.983|   0.5%/138|   0.5%/149|   0.5%/152|   0.4%/155 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 156   |     422|     131.688|   0.6%/113|   0.5%/144|   0.4%/154|   0.4%/167 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 156   |      58|      93.053|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 156   |    2626|     307.673|   0.6%/113|   0.7%/104|   0.7%/102|   0.7%/ 99 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 156   |    1965|     258.094|   0.5%/151|   0.4%/180|   0.4%/190|   0.3%/201 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 156   |     231|     128.926|   2.4%/ 29|   2.5%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 156   |    1149|     197.349|   0.5%/130|   0.5%/137|   0.5%/139|   0.5%/141 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 144   |      41|      70.285|   0.1%/745|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 156   |    1422|      44.125|   0.1%/476|   0.1%/939|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 156   |     300|     105.563|   1.6%/ 42|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 156   |    1542|      35.869|   0.6%/115|   0.6%/124|   0.5%/126|   0.5%/129 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 156   |     117|       3.765|   1.3%/ 53|   1.0%/ 69|   0.9%/ 74|   0.9%/ 80 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 156   |    9606|     213.748|   2.6%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 156   |     893|     302.058|   0.4%/172|   0.4%/197|   0.3%/204|   0.3%/212 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 156   |     746|      29.054|   2.9%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 156   |     736|      82.691|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 156   |     540|      53.677|   0.4%/192|   0.3%/212|   0.3%/217|   0.3%/221 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 156   |     196|     126.890|   0.5%/148|   0.3%/226|   0.3%/261|   0.2%/311 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 156   |    4418|      26.226|   1.0%/ 70|   1.0%/ 72|   1.0%/ 72|   0.9%/ 73 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 156   |     694|      73.719|   0.7%/ 93|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 156   |    9897|     858.795|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 151   |      40|       3.433|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 156   |    5302|     462.244|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 156   |     650|     196.769|   1.5%/ 45|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 156   |       5|       2.160|   6.5%/ 11|   7.8%/  9|   8.2%/  8|   8.6%/  8 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 156   |  125396|     593.137|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 156   |     656|      94.426|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 156   |      55|       2.649|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 144   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 156   |     416|      15.664|   0.2%/401|   0.2%/437|   0.2%/447|   0.2%/457 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 156   |    9191|     241.886|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 104   |      62|      11.230|   0.1%/485|   0.2%/302|   0.3%/273|   0.3%/248 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 129   |      77|       4.749|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 156   |   11464|     599.962|   0.5%/147|   0.4%/156|   0.4%/159|   0.4%/161 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 156   |    4728|       3.372|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 156   |   21044|     426.023|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 156   |     479|      94.682|   2.4%/ 29|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 156   |     189|      46.360|   0.9%/ 74|   1.0%/ 67|   1.1%/ 65|   1.1%/ 63 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 156   |      94|       8.384|   0.5%/130|   0.7%/105|   0.7%/100|   0.7%/ 95 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 156   |     626|     107.437|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 156   |    1784|     172.267|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 156   |    6654|     380.920|   0.5%/144|   0.5%/141|   0.5%/141|   0.5%/140 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 156   |    5476|      54.610|   0.3%/201|   0.3%/205|   0.3%/205|   0.3%/206 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 156   |     753|     116.132|   1.0%/ 70|   0.8%/ 85|   0.8%/ 90|   0.7%/ 95 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 135   |      83|      61.107|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 152   |     907|       9.195|   2.5%/ 27|   2.2%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 156   |     336|      60.828|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 156   |   30682|     457.424|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 156   |      54|      24.652|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 156   |     184|      78.194|   2.2%/ 32|   0.0%/ --|   0.3%/200|   1.0%/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 153   |      19|       5.152|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 156   |    9323|     112.128|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 156   |     291|       9.616|   0.7%/ 94|   0.5%/148|   0.4%/173|   0.3%/209 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 156   |     273|      25.429|   1.2%/ 60|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 156   |    2866|     172.620|   0.8%/ 82|   0.7%/ 97|   0.7%/101|   0.7%/106 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 142   |      61|       4.962|   0.9%/ 80|   0.9%/ 77|   0.9%/ 76|   0.9%/ 76 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 131   |      35|      21.710|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 152   |     207|      17.876|   0.4%/177|   0.3%/227|   0.3%/241|   0.3%/256 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 156   |    1921|     209.731|   1.2%/ 57|   1.3%/ 53|   1.3%/ 52|   1.4%/ 51 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 156   |     618|      63.274|   0.1%/677|   0.1%/679|   0.1%/679|   0.1%/677 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 156   |   69369|      50.961|   1.6%/ 43|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 156   |    7678|      28.767|   1.3%/ 54|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 156   |   22155|     265.723|   0.6%/121|   0.5%/142|   0.5%/149|   0.4%/156 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 156   |    7331|     187.348|   1.2%/ 59|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 156   |    1779|     361.402|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 156   |    1007|     109.570|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 156   |   35540|     589.993|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 156   |      22|       8.019|   0.0%/ --|   1.6%/ 42|   4.6%/ 15|  11.4%/  6 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 156   |    1330|      10.561|   1.1%/ 64|   1.2%/ 60|   1.2%/ 59|   1.2%/ 58 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 156   |      16|       1.473|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 156   |    1662|      88.943|   1.1%/ 65|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 156   |     614|      12.918|   0.9%/ 77|   0.6%/116|   0.5%/134|   0.4%/158 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 156   |     537|     299.063|   0.8%/ 84|   0.3%/258|   0.1%/545|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 153   |     540|     122.174|   0.4%/179|   0.3%/208|   0.3%/216|   0.3%/225 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 154   |     986|     150.976|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 154   |      34|      17.929|   0.3%/272|   0.3%/257|   0.3%/255|   0.3%/253 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 156   |     182|      26.662|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 153   |      83|      18.460|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 155   |     266|      38.751|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 156   |      87|      31.010|   0.3%/265|   0.3%/249|   0.3%/246|   0.3%/244 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 110   |     197|       7.509|   0.9%/ 75|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 156   |     126|       3.832|   0.1%/662|   0.1%/483|   0.2%/450|   0.2%/421 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 156   |     126|       6.225|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 156   |     159|      39.033|   0.1%/650|   0.1%/523|   0.1%/497|   0.1%/474 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 156   |   66823|     527.923|   0.8%/ 82|   0.8%/ 90|   0.7%/ 92|   0.7%/ 95 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 156   |    1028|     383.242|   0.8%/ 88|   0.8%/ 88|   0.8%/ 88|   0.8%/ 87 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 156   |    1314|      36.631|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 102   |      24|       0.809|   1.8%/ 37|   2.5%/ 28|   2.6%/ 26|   2.8%/ 25 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  56   |      87|      35.302|   5.2%/ 13|   4.9%/ 14|   4.9%/ 14|   4.9%/ 14 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 111   |     264|       8.799|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 156   |    6267|     358.978|   0.1%/ ***|   0.1%/969|   0.1%/950|   0.1%/933 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 156   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 156   |     141|      21.878|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 156   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 156   |    1036|       5.028|   0.3%/226|   0.3%/263|   0.3%/273|   0.2%/283 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 156   |     610|     293.535|   0.6%/110|   0.6%/109|   0.6%/109|   0.6%/109 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 156   |     266|      49.534|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 156   |     710|     152.295|   1.1%/ 62|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 156   |    6340|      28.906|   0.1%/519|   0.1%/603|   0.1%/628|   0.1%/654 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 156   |    2075|     491.799|   0.7%/ 93|   0.6%/110|   0.6%/116|   0.6%/122 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  39   |       5|       0.562|   4.4%/ 16|   1.5%/ 45|   0.1%/ ***|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 156   |     403|      56.356|   5.8%/ 12|   5.7%/ 12|   5.7%/ 12|   5.7%/ 12 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 156   |   30610|     952.655|   0.6%/118|   0.5%/138|   0.5%/144|   0.5%/150 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 156   |    3728|      34.354|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 156   |    2087|      54.377|   0.6%/116|   0.6%/116|   0.6%/115|   0.6%/115 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 156   |    1831|     178.192|   0.2%/433|   0.2%/446|   0.2%/449|   0.2%/453 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 156   |     200|      72.788|   0.2%/286|   0.2%/365|   0.2%/388|   0.2%/412 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 156   |    3792|     195.419|   1.3%/ 54|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 156   |   17508|     119.311|   0.6%/114|   0.6%/119|   0.6%/120|   0.6%/121 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  97   |      19|       1.497|   2.7%/ 25|   2.2%/ 32|   2.0%/ 34|   1.9%/ 36 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 156   |    4028|     117.720|   0.8%/ 82|   0.8%/ 89|   0.8%/ 91|   0.7%/ 93 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 156   |     294|      18.134|   0.7%/104|   0.5%/135|   0.5%/145|   0.4%/158 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 156   |     730|     104.811|   0.3%/237|   0.2%/444|   0.1%/566|   0.1%/778 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 134   |      71|       8.926|   0.2%/317|   0.3%/246|   0.3%/231|   0.3%/218 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 156   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 156   |      34|       6.192|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 156   |     135|      64.307|   0.1%/470|   0.1%/728|   0.1%/840|   0.1%/989 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 149   |      97|       6.121|   0.4%/196|   0.5%/153|   0.5%/145|   0.5%/138 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 156   |   15008|     255.346|   1.0%/ 68|   0.7%/ 93|   0.7%/102|   0.6%/113 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 156   |   29170|     619.308|   0.1%/623|   0.1%/543|   0.1%/526|   0.1%/510 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 156   |      12|       0.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 156   |     833|      19.636|   0.1%/561|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 156   |    5831|     564.031|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 156   |    2011|     233.709|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 156   |     127|       7.277|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 156   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 156   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 156   |      29|       3.891|   0.0%/ --|   1.2%/ 57|   3.6%/ 19|   3.5%/ 20 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 156   |      26|      19.242|   6.9%/ 10|   8.1%/  8|   8.4%/  8|   8.7%/  8 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 156   |      82|       6.995|   1.6%/ 43|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 156   |    6368|      76.578|   0.5%/137|   0.6%/122|   0.6%/119|   0.6%/115 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 156   |  187505|     568.983|   0.5%/138|   0.5%/149|   0.5%/152|   0.4%/155 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  42   |      33|       0.826|   5.5%/ 13|   2.7%/ 26|   2.2%/ 32|   1.7%/ 41 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 156   |    2714|      64.812|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 156   |     387|      39.152|   0.4%/194|   0.4%/186|   0.4%/185|   0.4%/183 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 156   |   41391|     623.030|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 156   |      45|      12.838|   0.6%/111|   0.6%/124|   0.5%/129|   0.5%/134 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 156   |     344|      10.088|   1.9%/ 36|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 156   |     423|      13.126|   1.9%/ 36|   1.6%/ 43|   1.5%/ 45|   1.4%/ 48 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  35   |      35|       0.364|   3.0%/ 23|   2.2%/ 32|   1.8%/ 38|   1.4%/ 49 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 155   |     306|      17.095|   0.6%/122|   0.4%/178|   0.3%/201|   0.3%/231 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 156   |     221|      14.579|   2.0%/ 35|   1.3%/ 53|   1.1%/ 61|   1.0%/ 71 |

