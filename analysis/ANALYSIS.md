# State and Country COVID-19 Analysis #
## Updated: at 2020-09-05 for data as of 2020-09-04 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.9% of deaths and 57.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 157   |   32988|    1695.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 157   |   15967|    1797.686|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 157   |   13699|     346.694|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 157   |   13818|     476.537|   1.3%/ 55|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 157   |   12003|     558.850|   1.1%/ 63|   0.9%/ 77|   0.9%/ 81|   0.8%/ 86 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 157   |    9110|    1310.875|   0.1%/476|   0.1%/503|   0.1%/511|   0.1%/519 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 157   |    8336|     657.821|   0.3%/267|   0.3%/256|   0.3%/253|   0.3%/251 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 157   |    7743|     604.795|   0.2%/350|   0.2%/363|   0.2%/366|   0.2%/370 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 157   |    6794|     680.245|   0.2%/398|   0.2%/379|   0.2%/375|   0.2%/370 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 157   |    5974|     562.622|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 157   |  188360|     571.578|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/152 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 157   |  126253|     597.188|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 157   |   70377|      51.701|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 157   |   67307|     531.741|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 157   |   41667|     627.184|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 157   |   35545|     590.075|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 157   |   30703|     457.730|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 157   |   29208|     620.113|   0.1%/577|   0.1%/500|   0.1%/484|   0.1%/469 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 157   |   30672|     954.581|   0.6%/121|   0.5%/140|   0.5%/146|   0.5%/152 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 157   |   22251|     266.867|   0.6%/123|   0.5%/144|   0.5%/150|   0.4%/157 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 157   |    2254|     459.723|   0.9%/ 78|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 157   |      41|      55.462|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 157   |    5232|     718.773|   0.7%/105|   0.5%/128|   0.5%/136|   0.5%/144 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 157   |     861|     285.332|   2.0%/ 34|   2.1%/ 33|   2.1%/ 32|   2.2%/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 157   |   13699|     346.694|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 157   |    1960|     340.354|   0.2%/400|   0.2%/421|   0.2%/427|   0.2%/433 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 157   |    4471|    1253.904|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 157   |     608|     624.402|   0.1%/728|   0.1%/809|   0.1%/836|   0.1%/867 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 157   |   12003|     558.850|   1.1%/ 63|   0.9%/ 77|   0.9%/ 81|   0.8%/ 86 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 157   |    5974|     562.622|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 157   |      77|      54.060|   4.2%/ 16|   4.7%/ 15|   4.8%/ 14|   5.0%/ 14 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 157   |     392|     219.367|   1.6%/ 43|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 157   |    8336|     657.821|   0.3%/267|   0.3%/256|   0.3%/253|   0.3%/251 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 157   |    3355|     498.347|   0.3%/208|   0.3%/219|   0.3%/222|   0.3%/225 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 157   |    1156|     366.299|   0.8%/ 86|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 157   |     470|     161.294|   0.8%/ 84|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 157   |     978|     218.880|   1.0%/ 67|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 157   |    5110|    1099.145|   0.6%/124|   0.5%/143|   0.5%/149|   0.4%/155 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 157   |     134|      99.685|   0.2%/280|   0.2%/288|   0.2%/291|   0.2%/294 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 157   |    3787|     626.417|   0.2%/338|   0.2%/347|   0.2%/349|   0.2%/351 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 157   |    9110|    1310.875|   0.1%/476|   0.1%/503|   0.1%/511|   0.1%/519 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 157   |    6794|     680.245|   0.2%/398|   0.2%/379|   0.2%/375|   0.2%/370 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 157   |    1906|     337.965|   0.4%/172|   0.4%/183|   0.4%/186|   0.4%/189 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 157   |    2595|     871.837|   1.0%/ 68|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 157   |    1589|     258.912|   0.8%/ 88|   0.8%/ 83|   0.8%/ 82|   0.9%/ 81 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 157   |     113|     105.301|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 157   |     406|     210.091|   0.5%/127|   0.5%/134|   0.5%/136|   0.5%/139 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 157   |    1403|     455.431|   1.2%/ 58|   1.0%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 157   |     434|     319.366|   0.1%/795|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 157   |   15967|    1797.686|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 157   |     798|     380.586|   0.6%/124|   0.5%/129|   0.5%/130|   0.5%/132 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 157   |   32988|    1695.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 157   |    2837|     270.481|   1.0%/ 72|   0.9%/ 74|   0.9%/ 74|   0.9%/ 75 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 157   |     151|     198.550|   1.0%/ 69|   0.9%/ 73|   0.9%/ 74|   0.9%/ 75 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 157   |    4246|     363.232|   0.5%/128|   0.5%/131|   0.5%/132|   0.5%/133 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 157   |     850|     214.772|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 157   |     480|     113.778|   1.0%/ 68|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 157   |    7743|     604.795|   0.2%/350|   0.2%/363|   0.2%/366|   0.2%/370 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 157   |     478|     149.522|   1.5%/ 46|   1.2%/ 56|   1.2%/ 60|   1.1%/ 64 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 157   |    1054|     995.409|   0.2%/403|   0.2%/374|   0.2%/368|   0.2%/362 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 157   |    2891|     561.421|   1.1%/ 62|   1.0%/ 70|   1.0%/ 72|   0.9%/ 75 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 157   |     172|     194.143|   0.5%/130|   0.5%/151|   0.4%/157|   0.4%/163 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 157   |    1885|     275.887|   1.4%/ 49|   1.3%/ 54|   1.3%/ 55|   1.2%/ 57 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 157   |   13818|     476.537|   1.3%/ 55|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 157   |  188360|     571.578|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/152 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 157   |     424|     132.340|   0.6%/112|   0.5%/138|   0.5%/147|   0.4%/157 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 157   |      58|      93.024|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 157   |    2644|     309.759|   0.6%/111|   0.7%/102|   0.7%/ 99|   0.7%/ 97 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 157   |    1972|     258.904|   0.4%/156|   0.4%/188|   0.3%/198|   0.3%/209 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 157   |     237|     132.513|   2.4%/ 28|   2.6%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 157   |    1155|     198.366|   0.5%/127|   0.5%/132|   0.5%/133|   0.5%/134 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 145   |      41|      71.488|   0.1%/464|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 157   |    1422|      44.126|   0.1%/534|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 157   |     305|     107.249|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 157   |    1550|      36.052|   0.6%/119|   0.5%/129|   0.5%/131|   0.5%/134 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 157   |     118|       3.797|   1.3%/ 51|   1.1%/ 63|   1.0%/ 67|   1.0%/ 71 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 157   |    9825|     218.624|   2.6%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 157   |     896|     303.050|   0.4%/175|   0.3%/199|   0.3%/205|   0.3%/213 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 157   |     763|      29.715|   3.0%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 157   |     736|      82.711|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 157   |     542|      53.867|   0.4%/187|   0.3%/199|   0.3%/202|   0.3%/204 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 157   |     197|     127.454|   0.5%/143|   0.3%/203|   0.3%/228|   0.3%/259 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 157   |    4457|      26.454|   1.0%/ 72|   0.9%/ 75|   0.9%/ 75|   0.9%/ 76 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 157   |     699|      74.306|   0.7%/ 93|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 157   |    9897|     858.790|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 152   |      40|       3.436|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 157   |    5372|     468.375|   1.4%/ 48|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 157   |     657|     199.017|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 157   |       6|       2.391|   6.9%/ 10|   8.4%/  8|   8.8%/  8|   9.2%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 157   |  126253|     597.188|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 157   |     666|      95.792|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 157   |      55|       2.648|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 145   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 157   |     416|      15.682|   0.2%/430|   0.1%/484|   0.1%/499|   0.1%/516 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 157   |    9197|     242.028|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 105   |      62|      11.254|   0.1%/504|   0.2%/331|   0.2%/303|   0.2%/279 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 130   |      77|       4.752|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 157   |   11517|     602.731|   0.5%/146|   0.4%/154|   0.4%/156|   0.4%/159 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 157   |    4730|       3.373|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 157   |   21313|     431.485|   1.6%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 157   |     487|      96.319|   2.3%/ 30|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 157   |     191|      46.911|   1.0%/ 69|   1.1%/ 62|   1.1%/ 60|   1.2%/ 59 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 157   |      94|       8.420|   0.6%/111|   0.8%/ 89|   0.8%/ 85|   0.9%/ 81 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 157   |     626|     107.508|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 157   |    1804|     174.173|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 157   |    6686|     382.765|   0.5%/143|   0.5%/140|   0.5%/139|   0.5%/139 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 157   |    5494|      54.792|   0.3%/201|   0.3%/203|   0.3%/204|   0.3%/204 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 157   |     759|     116.943|   1.0%/ 71|   0.8%/ 86|   0.8%/ 90|   0.7%/ 95 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 136   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 153   |     924|       9.364|   2.4%/ 28|   2.1%/ 33|   2.0%/ 35|   1.9%/ 37 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 157   |     336|      60.843|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 157   |   30703|     457.730|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 157   |      54|      24.642|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 157   |     196|      83.398|   1.1%/ 65|   0.3%/200|   1.0%/ 67|   1.0%/ 67 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 154   |      19|       5.179|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 157   |    9328|     112.182|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 157   |     292|       9.652|   0.7%/ 97|   0.5%/150|   0.4%/174|   0.3%/207 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 157   |     276|      25.779|   1.1%/ 61|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 157   |    2883|     173.645|   0.8%/ 86|   0.7%/102|   0.6%/107|   0.6%/113 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 143   |      61|       5.010|   0.9%/ 78|   0.9%/ 74|   0.9%/ 73|   0.9%/ 73 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 132   |      35|      22.055|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 153   |     208|      17.980|   0.5%/143|   0.5%/153|   0.5%/154|   0.4%/154 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 157   |    1950|     212.874|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 157   |     619|      63.362|   0.1%/585|   0.1%/555|   0.1%/547|   0.1%/538 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 157   |   70377|      51.701|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 157   |    7784|      29.164|   1.3%/ 53|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 157   |   22251|     266.867|   0.6%/123|   0.5%/144|   0.5%/150|   0.4%/157 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 157   |    7410|     189.368|   1.2%/ 60|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 157   |    1778|     361.370|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 157   |    1022|     111.275|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 48 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 157   |   35545|     590.075|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 157   |      22|       8.223|   3.2%/ 22|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 157   |    1346|      10.685|   1.1%/ 64|   1.1%/ 60|   1.2%/ 60|   1.2%/ 59 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 157   |      16|       1.496|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 157   |    1665|      89.096|   1.0%/ 72|   0.8%/ 82|   0.8%/ 85|   0.8%/ 88 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 157   |     617|      12.962|   0.9%/ 81|   0.6%/124|   0.5%/144|   0.4%/172 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 157   |     536|     298.513|   0.7%/101|   0.1%/523|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 154   |     541|     122.487|   0.4%/190|   0.3%/225|   0.3%/236|   0.3%/247 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 155   |     980|     150.052|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 155   |      34|      18.040|   0.3%/215|   0.4%/192|   0.4%/187|   0.4%/183 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 157   |     187|      27.455|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 154   |      83|      18.436|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 156   |     273|      39.703|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 157   |      87|      31.075|   0.2%/293|   0.2%/289|   0.2%/290|   0.2%/292 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 111   |     199|       7.567|   0.9%/ 79|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 157   |     127|       3.865|   0.1%/762|   0.1%/567|   0.1%/531|   0.1%/498 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 157   |     126|       6.227|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 157   |     159|      39.086|   0.1%/582|   0.1%/468|   0.2%/445|   0.2%/424 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 157   |   67307|     531.741|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 157   |    1037|     386.749|   0.8%/ 83|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 157   |    1350|      37.642|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 103   |      25|       0.834|   2.1%/ 33|   2.8%/ 24|   3.0%/ 23|   3.2%/ 21 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  57   |      90|      36.447|   4.9%/ 14|   4.4%/ 16|   4.2%/ 16|   4.0%/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 112   |     276|       9.217|   5.1%/ 13|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 157   |    6271|     359.216|   0.1%/ ***|   0.1%/998|   0.1%/982|   0.1%/967 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 157   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 157   |     142|      21.955|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 157   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 157   |    1041|       5.050|   0.4%/192|   0.3%/199|   0.3%/201|   0.3%/201 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 157   |     613|     295.147|   0.6%/116|   0.6%/117|   0.6%/117|   0.6%/118 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 157   |     266|      49.518|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 157   |     716|     153.453|   1.1%/ 65|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 157   |    6347|      28.938|   0.1%/495|   0.1%/548|   0.1%/562|   0.1%/576 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 157   |    2087|     494.652|   0.7%/ 94|   0.6%/110|   0.6%/115|   0.6%/121 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  40   |       5|       0.562|   4.8%/ 14|   0.7%/101|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 157   |     424|      59.279|   5.7%/ 12|   5.5%/ 12|   5.5%/ 12|   5.5%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 157   |   30672|     954.581|   0.6%/121|   0.5%/140|   0.5%/146|   0.5%/152 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 157   |    3794|      34.965|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 157   |    2099|      54.700|   0.6%/115|   0.6%/113|   0.6%/113|   0.6%/113 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 157   |    1834|     178.470|   0.2%/434|   0.2%/447|   0.2%/450|   0.2%/454 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 157   |     200|      72.954|   0.3%/264|   0.2%/303|   0.2%/311|   0.2%/319 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 157   |    3837|     197.734|   1.3%/ 54|   1.2%/ 57|   1.2%/ 57|   1.2%/ 58 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 157   |   17612|     120.018|   0.6%/113|   0.6%/117|   0.6%/118|   0.6%/119 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  98   |      19|       1.521|   2.2%/ 32|   2.0%/ 34|   4.0%/ 17|   4.0%/ 17 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 157   |    4057|     118.559|   0.8%/ 84|   0.8%/ 91|   0.7%/ 94|   0.7%/ 96 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 157   |     295|      18.206|   0.6%/108|   0.5%/139|   0.5%/150|   0.4%/163 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 157   |     731|     104.912|   0.3%/247|   0.2%/450|   0.1%/563|   0.1%/750 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 135   |      71|       8.949|   0.2%/340|   0.3%/274|   0.3%/261|   0.3%/248 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 157   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 157   |      34|       6.211|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 157   |     135|      64.357|   0.2%/439|   0.1%/597|   0.1%/653|   0.1%/719 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 150   |      98|       6.137|   0.3%/231|   0.4%/188|   0.4%/180|   0.4%/172 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 157   |   15094|     256.810|   1.0%/ 69|   0.7%/ 94|   0.7%/102|   0.6%/112 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 157   |   29208|     620.113|   0.1%/577|   0.1%/500|   0.1%/484|   0.1%/469 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 157   |      12|       0.560|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 157   |     833|      19.630|   0.1%/660|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 157   |    5833|     564.256|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 157   |    2012|     233.851|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 157   |     131|       7.509|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 157   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 157   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 157   |      30|       3.935|   0.0%/ --|   3.6%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 157   |      28|      20.731|   6.8%/ 10|   7.7%/  9|   7.9%/  9|   8.1%/  8 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 157   |      83|       7.118|   1.8%/ 38|   2.1%/ 33|   2.1%/ 32|   2.2%/ 31 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 157   |    6393|      76.880|   0.5%/127|   0.6%/112|   0.6%/109|   0.7%/106 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 157   |  188360|     571.578|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/152 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  43   |      34|       0.855|   4.7%/ 15|   2.6%/ 26|   2.3%/ 29|   2.0%/ 34 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 157   |    2762|      65.944|   1.6%/ 43|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 157   |     388|      39.271|   0.3%/198|   0.4%/194|   0.4%/193|   0.4%/193 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 157   |   41667|     627.184|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 157   |      45|      12.916|   0.6%/111|   0.6%/124|   0.5%/128|   0.5%/134 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 157   |     349|      10.236|   1.8%/ 37|   1.6%/ 43|   1.5%/ 45|   1.5%/ 47 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 157   |     429|      13.307|   1.9%/ 37|   1.6%/ 44|   1.5%/ 46|   1.4%/ 49 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  36   |      35|       0.367|   2.9%/ 23|   1.8%/ 39|   1.3%/ 51|   0.9%/ 79 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 156   |     306|      17.125|   0.5%/134|   0.3%/204|   0.3%/233|   0.3%/273 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 157   |     224|      14.756|   1.4%/ 49|   0.8%/ 83|   0.7%/101|   0.5%/128 |

