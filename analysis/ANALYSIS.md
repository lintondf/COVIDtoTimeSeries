# State and Country COVID-19 Analysis #
## Updated: at 2020-08-10 for data as of 2020-08-09 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.1% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.3% of deaths and 55.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 131   |   32798|    1685.951|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 131   |   15887|    1788.596|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 131   |   10397|     263.129|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 131   |    9310|     321.083|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 131   |    8736|    1257.000|   0.2%/399|   0.2%/399|   0.2%/399|   0.2%/398 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 131   |    8336|     388.134|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 131   |    7842|     618.819|   0.2%/293|   0.2%/279|   0.3%/275|   0.3%/271 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 131   |    7321|     571.892|   0.2%/369|   0.2%/389|   0.2%/394|   0.2%/399 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 131   |    6518|     652.704|   0.1%/520|   0.1%/475|   0.1%/464|   0.2%/453 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 131   |    4447|    1247.220|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 131   |  163049|     494.771|   0.7%/ 92|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 131   |  101890|     481.950|   1.1%/ 62|   1.0%/ 66|   1.0%/ 67|   1.0%/ 68 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 131   |   52610|     415.633|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 131   |   46707|     703.050|   0.1%/526|   0.1%/545|   0.1%/550|   0.1%/555 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 131   |   44600|      32.765|   2.2%/ 31|   2.2%/ 32|   2.2%/ 32|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 131   |   35209|     584.495|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 131   |   30333|     452.225|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 131   |   28501|     605.101|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 131   |   22183|     690.377|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 131   |   18855|     226.136|   1.2%/ 58|   1.1%/ 64|   1.1%/ 65|   1.0%/ 67 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 131   |    1798|     366.610|   1.4%/ 50|   1.3%/ 55|   1.2%/ 57|   1.2%/ 59 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 131   |      27|      36.773|   1.2%/ 58|   1.4%/ 48|   1.5%/ 46|   1.6%/ 45 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 131   |    4288|     589.124|   1.8%/ 39|   1.5%/ 47|   1.4%/ 50|   1.3%/ 53 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 131   |     541|     179.332|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 131   |   10397|     263.129|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 131   |    1872|     325.049|   0.2%/294|   0.2%/352|   0.2%/372|   0.2%/397 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 131   |    4447|    1247.220|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 131   |     603|     619.156|   0.1%/483|   0.1%/510|   0.1%/517|   0.1%/525 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 131   |    8336|     388.134|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 131   |    4201|     395.664|   1.4%/ 50|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 131   |      28|      19.746|   0.5%/135|   0.5%/147|   0.5%/148|   0.5%/147 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 131   |     245|     137.309|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 131   |    7842|     618.819|   0.2%/293|   0.2%/279|   0.3%/275|   0.3%/271 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 131   |    3048|     452.771|   0.3%/204|   0.3%/212|   0.3%/215|   0.3%/217 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 131   |     929|     294.315|   0.8%/ 87|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 131   |     387|     132.911|   0.9%/ 78|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 131   |     778|     174.236|   0.7%/101|   0.6%/109|   0.6%/112|   0.6%/114 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 131   |    4249|     914.033|   0.9%/ 78|   1.0%/ 73|   1.0%/ 72|   1.0%/ 70 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 131   |     126|      93.486|   0.3%/227|   0.3%/263|   0.3%/275|   0.2%/289 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 131   |    3583|     592.734|   0.3%/236|   0.3%/230|   0.3%/228|   0.3%/227 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 131   |    8736|    1257.000|   0.2%/399|   0.2%/399|   0.2%/399|   0.2%/398 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 131   |    6518|     652.704|   0.1%/520|   0.1%/475|   0.1%/464|   0.2%/453 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 131   |    1692|     300.028|   0.4%/196|   0.4%/188|   0.4%/186|   0.4%/183 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 131   |    1904|     639.843|   1.7%/ 42|   1.7%/ 40|   1.7%/ 40|   1.7%/ 39 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 131   |    1341|     218.515|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97|   0.7%/ 98 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 131   |      76|      70.879|   3.5%/ 19|   3.7%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 131   |     346|     179.096|   0.6%/111|   0.6%/114|   0.6%/115|   0.6%/116 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 131   |     953|     309.383|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 131   |     423|     310.785|   0.2%/354|   0.1%/506|   0.1%/572|   0.1%/659 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 131   |   15887|    1788.596|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 131   |     689|     328.605|   0.8%/ 86|   0.8%/ 90|   0.8%/ 92|   0.7%/ 93 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 131   |   32798|    1685.951|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 131   |    2202|     209.990|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 131   |     112|     147.055|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 131   |    3701|     316.620|   0.7%/ 96|   0.7%/ 97|   0.7%/ 98|   0.7%/ 98 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 131   |     611|     154.486|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 131   |     360|      85.439|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 131   |    7321|     571.892|   0.2%/369|   0.2%/389|   0.2%/394|   0.2%/399 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 131   |     267|      83.660|   2.4%/ 28|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 131   |    1016|     959.224|   0.1%/791|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 131   |    2118|     411.335|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 131   |     145|     163.905|   1.3%/ 55|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 131   |    1234|     180.578|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 131   |    9310|     321.083|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 131   |  163049|     494.771|   0.7%/ 92|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 131   |     346|     107.908|   1.4%/ 48|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 131   |      58|      92.625|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 131   |    2326|     272.552|   0.8%/ 88|   0.9%/ 78|   0.9%/ 76|   0.9%/ 73 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 131   |    1685|     221.220|   0.8%/ 84|   0.9%/ 77|   0.9%/ 75|   0.9%/ 74 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 131   |     130|      72.299|   1.7%/ 40|   2.1%/ 33|   2.2%/ 32|   2.3%/ 30 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 131   |    1001|     171.928|   0.8%/ 83|   0.9%/ 78|   0.9%/ 78|   0.9%/ 77 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 119   |      28|      48.205|   0.8%/ 85|   0.9%/ 76|   0.9%/ 74|   1.0%/ 71 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 131   |    1331|      41.317|   0.4%/179|   0.1%/517|   0.1%/933|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 131   |     202|      70.902|   2.7%/ 26|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 131   |    1308|      30.414|   0.9%/ 79|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 131   |      74|       2.384|   3.7%/ 19|   4.3%/ 16|   4.1%/ 17|   5.4%/ 13 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 131   |    4684|     104.225|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 131   |     803|     271.432|   0.8%/ 84|   0.6%/114|   0.6%/125|   0.5%/138 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 131   |     307|      11.951|   4.7%/ 15|   5.2%/ 13|   5.3%/ 13|   5.5%/ 13 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 131   |     721|      81.023|   0.1%/944|   0.1%/883|   0.1%/872|   0.1%/863 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 131   |     508|      50.482|   1.2%/ 55|   0.9%/ 75|   0.8%/ 82|   0.8%/ 91 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 131   |     162|     105.126|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 131   |    3438|      20.410|   1.1%/ 62|   1.0%/ 70|   1.0%/ 73|   0.9%/ 76 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 131   |     596|      63.343|   0.7%/100|   0.6%/119|   0.6%/126|   0.5%/133 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 131   |    9872|     856.570|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 126   |      39|       3.329|   0.5%/151|   0.1%/703|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 131   |    3731|     325.301|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 131   |     411|     124.476|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 131   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 131   |  101890|     481.950|   1.1%/ 62|   1.0%/ 66|   1.0%/ 67|   1.0%/ 68 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 131   |     453|      65.182|   2.0%/ 35|   2.0%/ 34|   2.1%/ 34|   2.1%/ 33 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 131   |      54|       2.580|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 119   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 131   |     397|      14.940|   0.2%/459|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 131   |    9035|     237.757|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  79   |      59|      10.785|   0.1%/ ***|   0.1%/862|   0.1%/775|   0.1%/687 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 104   |      76|       4.661|   0.1%/639|   0.2%/389|   0.2%/351|   0.2%/319 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 131   |   10212|     534.461|   0.8%/ 91|   0.7%/100|   0.7%/102|   0.7%/105 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 131   |    4685|       3.341|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 131   |   13160|     266.423|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 131   |     256|      50.561|   5.4%/ 13|   5.7%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 131   |     161|      39.545|   1.1%/ 64|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 131   |      88|       7.836|   0.1%/887|   0.1%/657|   0.1%/614|   0.1%/576 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 131   |     617|     106.044|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 131   |    1301|     125.554|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 131   |    5965|     341.453|   0.5%/136|   0.5%/149|   0.5%/152|   0.4%/156 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 131   |    5091|      50.777|   0.6%/115|   0.4%/168|   0.4%/190|   0.3%/218 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 131   |     552|      85.031|   2.3%/ 30|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 110   |      92|      67.662|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 127   |     415|       4.206|   4.4%/ 16|   4.4%/ 16|   4.4%/ 16|   4.4%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 131   |     331|      59.864|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 131   |   30333|     452.225|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 131   |      52|      23.811|   0.4%/186|   0.3%/208|   0.3%/216|   0.3%/225 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 131   |      20|       8.370|   9.9%/  7|  11.2%/  6|  11.5%/  6|  11.9%/  6 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 128   |      17|       4.666|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 131   |    9196|     110.598|   0.1%/ ***|   0.1%/929|   0.1%/900|   0.1%/873 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 131   |     211|       6.952|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 131   |     213|      19.816|   0.3%/211|   0.3%/207|   0.3%/206|   0.3%/206 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 131   |    2257|     135.916|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 117   |      51|       4.144|   1.1%/ 63|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 106   |      28|      17.422|   0.7%/101|   1.1%/ 66|   1.1%/ 60|   1.2%/ 56 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 127   |     178|      15.386|   1.2%/ 59|   1.4%/ 51|   1.4%/ 49|   1.5%/ 47 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 131   |    1583|     172.875|   2.0%/ 34|   1.6%/ 43|   1.5%/ 47|   1.4%/ 50 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 131   |     600|      61.424|   0.1%/854|   0.1%/625|   0.1%/583|   0.1%/545 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 131   |   44600|      32.765|   2.2%/ 31|   2.2%/ 32|   2.2%/ 32|   2.1%/ 32 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 131   |    5818|      21.797|   1.4%/ 51|   1.2%/ 60|   1.1%/ 62|   1.1%/ 65 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 131   |   18855|     226.136|   1.2%/ 58|   1.1%/ 64|   1.1%/ 65|   1.0%/ 67 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 131   |    5463|     139.607|   1.5%/ 45|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 131   |    1770|     359.744|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 131   |     608|      66.129|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 131   |   35209|     584.495|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 131   |      13|       4.724|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 131   |    1039|       8.249|   0.4%/193|   0.4%/156|   0.5%/149|   0.5%/142 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 131   |      11|       1.037|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 131   |    1153|      61.719|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 131   |     439|       9.239|   2.8%/ 25|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 131   |     326|     181.630|   3.6%/ 19|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 128   |     480|     108.689|   0.7%/ 97|   0.7%/103|   0.7%/104|   0.7%/106 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 129   |    1773|     271.372|   1.1%/ 62|   0.3%/259|   0.1%/ ***|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 129   |      32|      16.864|   0.2%/413|   0.2%/391|   0.2%/389|   0.2%/389 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 131   |      77|      11.273|   3.1%/ 22|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 128   |      81|      18.109|   0.6%/107|   0.7%/104|   0.7%/104|   0.7%/103 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 130   |     117|      16.993|   4.5%/ 15|   4.6%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 131   |      81|      28.928|   0.1%/695|   0.1%/588|   0.1%/560|   0.1%/533 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  85   |     148|       5.651|   4.1%/ 17|   3.5%/ 20|   3.3%/ 21|   3.2%/ 22 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 131   |     126|       3.832|   0.1%/963|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 131   |     125|       6.177|   0.1%/570|   0.1%/619|   0.1%/632|   0.1%/645 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 131   |     158|      38.728|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 131   |   52610|     415.633|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 131   |     851|     317.329|   1.0%/ 70|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 131   |     486|      13.541|   3.2%/ 22|   3.6%/ 19|   3.7%/ 18|   3.9%/ 18 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  77   |      16|       0.548|   2.6%/ 27|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  31   |      19|       7.568|   4.4%/ 16|   8.1%/  8|   9.1%/  7|  10.0%/  7 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  86   |      73|       2.429|   3.7%/ 19|   4.5%/ 15|   4.7%/ 15|   5.0%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 131   |    6176|     353.807|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 131   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 131   |     126|      19.480|   0.8%/ 85|   0.7%/103|   0.6%/108|   0.6%/115 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 131   |      69|       3.093|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 131   |     951|       4.613|   0.8%/ 88|   0.7%/ 97|   0.7%/ 99|   0.7%/101 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 131   |     533|     256.789|   1.0%/ 71|   0.8%/ 82|   0.8%/ 86|   0.8%/ 89 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 131   |     256|      47.701|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 131   |     516|     110.676|   2.1%/ 32|   2.0%/ 34|   2.0%/ 35|   1.9%/ 35 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 131   |    6126|      27.929|   0.3%/222|   0.2%/340|   0.2%/390|   0.2%/456 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 131   |    1675|     397.079|   1.7%/ 40|   1.5%/ 47|   1.4%/ 49|   1.3%/ 52 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  14   |       3|       0.336|   0.0%/ --|  14.5%/  5|  14.5%/  5|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 131   |      73|      10.213|   4.5%/ 15|   4.7%/ 15|   4.8%/ 14|   4.8%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 131   |   22183|     690.377|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 131   |    2239|      20.632|   1.1%/ 62|   1.2%/ 57|   1.2%/ 56|   1.3%/ 55 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 131   |    1796|      46.796|   0.6%/121|   0.6%/110|   0.6%/107|   0.7%/105 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 131   |    1756|     170.865|   0.2%/448|   0.1%/531|   0.1%/557|   0.1%/585 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 131   |     184|      66.924|   0.7%/ 98|   0.7%/104|   0.7%/106|   0.6%/107 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 131   |    2656|     136.857|   1.5%/ 46|   1.7%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 131   |   15014|     102.316|   0.9%/ 81|   0.8%/ 89|   0.8%/ 91|   0.7%/ 93 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  72   |       5|       0.404|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 131   |    3169|      92.603|   1.1%/ 63|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 131   |     234|      14.423|   1.5%/ 47|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 131   |     651|      93.453|   1.3%/ 52|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 109   |      68|       8.587|   0.2%/328|   0.2%/285|   0.3%/274|   0.3%/263 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 131   |      27|       4.736|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 131   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 131   |     126|      60.231|   0.6%/112|   0.7%/ 96|   0.7%/ 93|   0.8%/ 90 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 124   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 131   |   10624|     180.754|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 131   |   28501|     605.101|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 131   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 131   |     782|      18.420|   0.6%/118|   0.6%/125|   0.5%/126|   0.5%/128 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 131   |    5786|     559.643|   0.1%/831|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 131   |    1987|     230.903|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 131   |      54|       3.083|   2.4%/ 29|   1.5%/ 45|   1.3%/ 52|   1.1%/ 62 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 131   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 131   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 131   |      22|       2.980|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 131   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 131   |      51|       4.359|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 131   |    5849|      70.338|   0.3%/238|   0.3%/244|   0.3%/246|   0.3%/248 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 131   |  163049|     494.771|   0.7%/ 92|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  17   |       7|       0.171|  18.6%/  4|   6.3%/ 11|   6.3%/ 11|  11.9%/  6 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 131   |    1907|      45.523|   1.3%/ 55|   1.3%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 131   |     357|      36.093|   0.3%/270|   0.3%/268|   0.3%/268|   0.3%/267 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 131   |   46707|     703.050|   0.1%/526|   0.1%/545|   0.1%/550|   0.1%/555 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 131   |      37|      10.650|   0.5%/132|   0.4%/161|   0.4%/170|   0.4%/180 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 131   |     198|       5.802|   3.7%/ 18|   3.5%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 131   |     221|       6.847|   3.3%/ 21|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  10   |      13|       0.135|  32.6%/  2|   7.7%/  9|   3.6%/ 19|   9.1%/  7 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 130   |     209|      11.712|   3.9%/ 17|   4.7%/ 15|   4.9%/ 14|   5.1%/ 14 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 131   |     111|       7.329|   6.1%/ 11|   8.0%/  9|   8.0%/  9|   7.4%/  9 |

