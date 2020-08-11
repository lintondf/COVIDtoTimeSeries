# State and Country COVID-19 Analysis #
## Updated: at 2020-08-11 for data as of 2020-08-10 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.2% of deaths and 40.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.2% of deaths and 55.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 132   |   32806|    1686.359|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 132   |   15892|    1789.168|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 132   |   10534|     266.612|   1.4%/ 48|   1.4%/ 48|   1.5%/ 48|   1.5%/ 47 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 132   |    9604|     331.222|   2.7%/ 25|   2.4%/ 28|   2.3%/ 29|   2.3%/ 31 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 132   |    8749|    1258.935|   0.2%/410|   0.2%/416|   0.2%/418|   0.2%/419 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 132   |    8506|     396.033|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 132   |    7857|     620.027|   0.2%/307|   0.2%/300|   0.2%/299|   0.2%/297 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 132   |    7332|     572.706|   0.2%/391|   0.2%/424|   0.2%/433|   0.2%/442 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 132   |    6526|     653.453|   0.1%/562|   0.1%/533|   0.1%/526|   0.1%/519 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 132   |    4448|    1247.585|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 132   |  164097|     497.950|   0.7%/ 96|   0.7%/ 94|   0.7%/ 94|   0.7%/ 93 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 132   |  102845|     486.467|   1.1%/ 65|   1.0%/ 70|   1.0%/ 71|   1.0%/ 73 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 132   |   53273|     420.870|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 132   |   46745|     703.607|   0.1%/575|   0.1%/627|   0.1%/642|   0.1%/658 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 132   |   45555|      33.466|   2.2%/ 31|   2.1%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 132   |   35215|     584.597|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 132   |   30340|     452.320|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 132   |   28516|     605.430|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 132   |   22423|     697.845|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 132   |   19103|     229.115|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 132   |    1820|     371.147|   1.4%/ 51|   1.2%/ 57|   1.2%/ 59|   1.1%/ 60 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 132   |      27|      37.147|   1.2%/ 58|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 132   |    4343|     596.644|   1.6%/ 42|   1.3%/ 54|   1.2%/ 58|   1.1%/ 62 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 132   |     553|     183.139|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 132   |   10534|     266.612|   1.4%/ 48|   1.4%/ 48|   1.5%/ 48|   1.5%/ 47 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 132   |    1875|     325.519|   0.2%/319|   0.2%/407|   0.2%/440|   0.1%/482 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 132   |    4448|    1247.585|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 132   |     603|     619.511|   0.1%/477|   0.1%/498|   0.1%/504|   0.1%/509 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 132   |    8506|     396.033|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 132   |    4251|     400.421|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 132   |      28|      19.885|   1.0%/ 69|   1.2%/ 58|   1.3%/ 55|   1.3%/ 52 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 132   |     252|     141.205|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 132   |    7857|     620.027|   0.2%/307|   0.2%/300|   0.2%/299|   0.2%/297 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 132   |    3056|     453.994|   0.3%/212|   0.3%/225|   0.3%/229|   0.3%/232 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 132   |     935|     296.481|   0.8%/ 88|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 132   |     390|     133.963|   0.8%/ 82|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 132   |     783|     175.164|   0.7%/105|   0.6%/115|   0.6%/118|   0.6%/122 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 132   |    4286|     921.992|   0.9%/ 80|   0.9%/ 76|   0.9%/ 75|   0.9%/ 75 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 132   |     126|      93.674|   0.3%/232|   0.3%/270|   0.2%/282|   0.2%/296 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 132   |    3593|     594.355|   0.3%/240|   0.3%/236|   0.3%/235|   0.3%/234 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 132   |    8749|    1258.935|   0.2%/410|   0.2%/416|   0.2%/418|   0.2%/419 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 132   |    6526|     653.453|   0.1%/562|   0.1%/533|   0.1%/526|   0.1%/519 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 132   |    1698|     301.140|   0.4%/193|   0.4%/184|   0.4%/181|   0.4%/179 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 132   |    1932|     649.220|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 132   |    1349|     219.852|   0.7%/ 99|   0.7%/104|   0.7%/106|   0.6%/107 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 132   |      78|      72.672|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 132   |     348|     180.136|   0.6%/117|   0.6%/124|   0.6%/125|   0.5%/127 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 132   |     969|     314.547|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 132   |     423|     310.988|   0.2%/407|   0.1%/677|   0.1%/821|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 132   |   15892|    1789.168|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 132   |     694|     330.959|   0.8%/ 87|   0.7%/ 92|   0.7%/ 94|   0.7%/ 95 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 132   |   32806|    1686.359|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 132   |    2227|     212.333|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 132   |     113|     148.372|   0.9%/ 74|   0.9%/ 75|   0.9%/ 75|   0.9%/ 75 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 132   |    3720|     318.232|   0.7%/103|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 132   |     618|     156.149|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55|   1.2%/ 55 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 132   |     365|      86.423|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 132   |    7332|     572.706|   0.2%/391|   0.2%/424|   0.2%/433|   0.2%/442 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 132   |     275|      86.054|   2.4%/ 29|   2.7%/ 26|   2.8%/ 25|   2.8%/ 24 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 132   |    1017|     959.835|   0.1%/858|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 132   |    2159|     419.254|   2.3%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 132   |     147|     165.636|   1.2%/ 58|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 132   |    1252|     183.240|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 132   |    9604|     331.222|   2.7%/ 25|   2.4%/ 28|   2.3%/ 29|   2.3%/ 31 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 132   |  164097|     497.950|   0.7%/ 96|   0.7%/ 94|   0.7%/ 94|   0.7%/ 93 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 132   |     350|     109.250|   1.4%/ 50|   1.2%/ 57|   1.2%/ 60|   1.1%/ 62 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 132   |      58|      92.834|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 132   |    2341|     274.242|   0.7%/ 93|   0.8%/ 85|   0.8%/ 83|   0.8%/ 82 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 132   |    1697|     222.895|   0.8%/ 87|   0.8%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 132   |     132|      73.813|   2.0%/ 35|   2.4%/ 29|   2.5%/ 27|   2.6%/ 26 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 132   |    1007|     173.019|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 120   |      28|      48.520|   0.7%/ 93|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 132   |    1336|      41.472|   0.4%/180|   0.2%/399|   0.1%/556|   0.1%/897 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 132   |     206|      72.494|   2.6%/ 27|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 132   |    1318|      30.659|   0.9%/ 81|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 132   |      78|       2.491|   4.5%/ 15|   4.1%/ 17|   4.0%/ 17|   3.9%/ 18 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 132   |    4826|     107.399|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 132   |     808|     273.214|   0.8%/ 86|   0.6%/114|   0.6%/123|   0.5%/134 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 132   |     323|      12.587|   4.9%/ 14|   5.4%/ 13|   5.5%/ 12|   5.7%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 132   |     722|      81.106|   0.1%/861|   0.1%/787|   0.1%/772|   0.1%/759 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 132   |     512|      50.879|   1.2%/ 60|   0.8%/ 84|   0.7%/ 93|   0.7%/106 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 132   |     164|     106.227|   1.1%/ 61|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 132   |    3473|      20.614|   1.1%/ 63|   1.0%/ 71|   0.9%/ 74|   0.9%/ 76 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 132   |     599|      63.648|   0.7%/106|   0.5%/132|   0.5%/140|   0.5%/151 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 132   |    9876|     856.926|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 127   |      39|       3.330|   0.4%/182|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 132   |    3810|     332.137|   2.4%/ 29|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 132   |     422|     127.808|   2.1%/ 33|   2.1%/ 32|   2.1%/ 32|   2.2%/ 32 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 132   |       1|       0.428|   3.0%/ 23|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 132   |  102845|     486.467|   1.1%/ 65|   1.0%/ 70|   1.0%/ 71|   1.0%/ 73 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 132   |     461|      66.377|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 132   |      54|       2.584|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 120   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 132   |     397|      14.955|   0.2%/439|   0.1%/966|   0.1%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 132   |    9040|     237.901|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  80   |      59|      10.825|   0.1%/751|   0.2%/340|   0.2%/294|   0.3%/256 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 105   |      76|       4.670|   0.1%/693|   0.2%/452|   0.2%/412|   0.2%/379 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 132   |   10273|     537.646|   0.7%/ 93|   0.7%/103|   0.7%/106|   0.6%/109 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 132   |    4687|       3.342|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 132   |   13510|     273.502|   2.9%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 132   |     268|      53.048|   5.9%/ 12|   5.2%/ 13|   5.0%/ 14|   4.8%/ 14 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 132   |     162|      39.826|   1.0%/ 68|   0.9%/ 76|   0.9%/ 79|   0.8%/ 82 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 132   |      88|       7.844|   0.1%/958|   0.1%/730|   0.1%/688|   0.1%/651 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 132   |     618|     106.156|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 132   |    1320|     127.463|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 132   |    5987|     342.749|   0.5%/145|   0.4%/164|   0.4%/170|   0.4%/176 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 132   |    5113|      50.989|   0.6%/122|   0.4%/176|   0.3%/199|   0.3%/227 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 132   |     564|      87.004|   2.3%/ 30|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 111   |      93|      68.474|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 128   |     431|       4.373|   4.3%/ 16|   4.2%/ 16|   4.2%/ 16|   4.1%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 132   |     331|      59.944|   0.1%/ ***|   0.1%/803|   0.1%/760|   0.1%/721 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 132   |   30340|     452.320|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 132   |      52|      23.848|   0.3%/216|   0.3%/266|   0.2%/286|   0.2%/310 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 132   |      23|       9.797|  15.9%/  4|   5.9%/ 12|  12.9%/  5|   6.6%/ 10 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 129   |      17|       4.663|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 132   |    9202|     110.665|   0.1%/ ***|   0.1%/993|   0.1%/969|   0.1%/945 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 132   |     214|       7.079|   1.8%/ 38|   1.9%/ 36|   1.9%/ 35|   2.0%/ 35 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 132   |     213|      19.885|   0.3%/201|   0.4%/197|   0.4%/197|   0.4%/197 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 132   |    2288|     137.778|   1.7%/ 40|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 118   |      51|       4.170|   1.0%/ 71|   0.8%/ 82|   0.8%/ 85|   0.8%/ 89 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 107   |      28|      17.668|   0.9%/ 77|   1.4%/ 51|   1.5%/ 47|   1.6%/ 43 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 128   |     180|      15.581|   1.2%/ 58|   1.4%/ 51|   1.4%/ 49|   1.5%/ 47 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 132   |    1603|     175.050|   1.8%/ 37|   1.4%/ 50|   1.3%/ 55|   1.1%/ 61 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 132   |     601|      61.525|   0.1%/748|   0.1%/548|   0.1%/512|   0.1%/479 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 132   |   45555|      33.466|   2.2%/ 31|   2.1%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 132   |    5885|      22.048|   1.3%/ 53|   1.1%/ 62|   1.1%/ 65|   1.0%/ 68 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 132   |   19103|     229.115|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 132   |    5538|     141.532|   1.5%/ 46|   1.3%/ 52|   1.3%/ 54|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 132   |    1771|     359.917|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 132   |     618|      67.264|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 132   |   35215|     584.597|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 132   |      13|       4.840|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 132   |    1044|       8.286|   0.4%/191|   0.4%/157|   0.5%/150|   0.5%/144 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 132   |      11|       1.037|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 132   |    1176|      62.919|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 132   |     449|       9.433|   2.6%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 132   |     341|     189.719|   3.6%/ 19|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 129   |     484|     109.425|   0.7%/ 97|   0.7%/102|   0.7%/104|   0.7%/106 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 130   |    1785|     273.139|   1.0%/ 70|   0.2%/347|   0.0%/ ***|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 130   |      32|      16.885|   0.2%/448|   0.2%/452|   0.2%/459|   0.1%/470 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 132   |      79|      11.639|   3.3%/ 21|   3.6%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 129   |      81|      18.070|   0.6%/110|   0.6%/109|   0.6%/110|   0.6%/110 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 131   |     123|      17.896|   4.6%/ 15|   4.9%/ 14|   5.0%/ 14|   5.1%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 132   |      81|      28.959|   0.1%/756|   0.1%/651|   0.1%/623|   0.1%/597 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  86   |     153|       5.827|   4.0%/ 17|   3.5%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 132   |     126|       3.832|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 132   |     125|       6.182|   0.1%/641|   0.1%/756|   0.1%/789|   0.1%/823 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 132   |     158|      38.721|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 132   |   53273|     420.870|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 132   |     858|     319.946|   0.9%/ 73|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 132   |     502|      13.999|   3.2%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  78   |      17|       0.559|   2.7%/ 26|   2.8%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  32   |      20|       7.933|   4.3%/ 16|   8.4%/  8|   7.9%/  9|   7.2%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  87   |      77|       2.554|   3.8%/ 18|   4.5%/ 15|   4.7%/ 15|   4.9%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 132   |    6178|     353.875|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 132   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 132   |     126|      19.561|   0.7%/ 96|   0.5%/126|   0.5%/138|   0.5%/152 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 132   |      69|       3.093|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 132   |     957|       4.644|   0.8%/ 92|   0.7%/102|   0.7%/105|   0.6%/108 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 132   |     537|     258.649|   0.9%/ 75|   0.8%/ 89|   0.7%/ 93|   0.7%/ 97 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 132   |     256|      47.711|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 132   |     527|     112.910|   2.0%/ 34|   1.8%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 132   |    6140|      27.993|   0.3%/232|   0.2%/346|   0.2%/392|   0.2%/451 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 132   |    1700|     402.892|   1.7%/ 41|   1.4%/ 48|   1.4%/ 51|   1.3%/ 53 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  15   |       3|       0.336|   0.0%/ --|  14.5%/  5|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 132   |      77|      10.757|   4.6%/ 15|   5.0%/ 14|   5.1%/ 14|   5.1%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 132   |   22423|     697.845|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 132   |    2269|      20.909|   1.2%/ 58|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 132   |    1806|      47.055|   0.6%/124|   0.6%/114|   0.6%/111|   0.6%/109 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 132   |    1759|     171.153|   0.2%/427|   0.1%/478|   0.1%/491|   0.1%/505 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 132   |     186|      67.584|   0.8%/ 89|   0.8%/ 89|   0.8%/ 89|   0.8%/ 89 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 132   |    2700|     139.157|   1.5%/ 46|   1.7%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 132   |   15122|     103.047|   0.8%/ 83|   0.7%/ 93|   0.7%/ 95|   0.7%/ 98 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  73   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 132   |    3203|      93.608|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 132   |     237|      14.629|   1.5%/ 47|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 132   |     658|      94.473|   1.3%/ 54|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 110   |      68|       8.627|   0.2%/286|   0.3%/232|   0.3%/221|   0.3%/209 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 132   |      27|       4.735|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 132   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 132   |     127|      60.686|   0.6%/108|   0.7%/ 93|   0.8%/ 90|   0.8%/ 87 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 125   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 132   |   10921|     185.808|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 132   |   28516|     605.430|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 132   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 132   |     786|      18.511|   0.6%/124|   0.5%/133|   0.5%/136|   0.5%/139 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 132   |    5788|     559.840|   0.1%/944|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 132   |    1987|     230.980|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 132   |      55|       3.136|   2.3%/ 30|   1.4%/ 50|   2.7%/ 25|   2.7%/ 25 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 132   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 132   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 132   |      23|       3.074|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 132   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 132   |      51|       4.362|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 132   |    5865|      70.531|   0.3%/241|   0.3%/248|   0.3%/250|   0.3%/252 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 132   |  164097|     497.950|   0.7%/ 96|   0.7%/ 94|   0.7%/ 94|   0.7%/ 93 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  18   |       9|       0.223|   7.7%/  9|   6.3%/ 11|  11.9%/  6|  14.5%/  5 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 132   |    1932|      46.143|   1.3%/ 55|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 132   |     358|      36.168|   0.2%/287|   0.2%/295|   0.2%/297|   0.2%/299 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 132   |   46745|     703.607|   0.1%/575|   0.1%/627|   0.1%/642|   0.1%/658 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 132   |      38|      10.683|   0.5%/150|   0.4%/197|   0.3%/214|   0.3%/235 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 132   |     205|       6.001|   3.7%/ 19|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 132   |     228|       7.076|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  11   |      15|       0.156|  38.7%/  2|   3.6%/ 19|   9.1%/  7|  14.5%/  5 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 131   |     220|      12.300|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 132   |     117|       7.727|   5.5%/ 12|   8.0%/  9|   7.4%/  9|   0.6%/107 |

