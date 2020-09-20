# State and Country COVID-19 Analysis #
## Updated: at 2020-09-20 for data as of 2020-09-19 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.4% of deaths and 38.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.2% of deaths and 56.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 172   |   33078|    1700.351|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 172   |   16059|    1807.990|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 172   |   15286|     527.190|   0.8%/ 90|   0.7%/106|   0.6%/111|   0.6%/117 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 172   |   15110|     382.401|   0.7%/ 99|   0.6%/108|   0.6%/110|   0.6%/112 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 172   |   13357|     621.877|   0.9%/ 81|   0.8%/ 86|   0.8%/ 87|   0.8%/ 88 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 172   |    9287|    1336.409|   0.1%/504|   0.1%/516|   0.1%/518|   0.1%/521 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 172   |    8664|     683.741|   0.3%/266|   0.3%/263|   0.3%/262|   0.3%/261 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 172   |    7930|     619.434|   0.2%/399|   0.2%/405|   0.2%/406|   0.2%/408 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 172   |    6979|     698.772|   0.1%/487|   0.1%/507|   0.1%/512|   0.1%/518 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 172   |    6704|     631.430|   0.7%/ 93|   0.6%/109|   0.6%/115|   0.6%/120 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 172   |  199610|     605.714|   0.4%/166|   0.4%/173|   0.4%/175|   0.4%/177 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 172   |  137098|     648.490|   0.6%/118|   0.6%/126|   0.5%/128|   0.5%/130 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 172   |   86584|      63.607|   1.4%/ 49|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 172   |   73926|     584.035|   0.6%/112|   0.6%/124|   0.5%/127|   0.5%/131 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 172   |   41801|     629.194|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 172   |   35669|     592.135|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 172   |   31529|     981.245|   0.4%/168|   0.4%/190|   0.4%/196|   0.3%/203 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 172   |   31057|     463.012|   0.1%/612|   0.1%/529|   0.1%/511|   0.1%/493 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 172   |   30090|     638.850|   0.2%/329|   0.2%/298|   0.2%/291|   0.2%/285 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 172   |   24026|     288.159|   0.6%/119|   0.6%/118|   0.6%/118|   0.6%/118 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 172   |    2459|     501.593|   0.6%/117|   0.5%/129|   0.5%/133|   0.5%/137 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 172   |      47|      64.616|   0.7%/100|   0.6%/123|   0.5%/130|   0.5%/139 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 172   |    5502|     755.942|   0.4%/178|   0.3%/217|   0.3%/229|   0.3%/242 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 172   |    1156|     382.929|   1.3%/ 54|   1.1%/ 63|   1.1%/ 66|   1.0%/ 69 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 172   |   15110|     382.401|   0.7%/ 99|   0.6%/108|   0.6%/110|   0.6%/112 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 172   |    2012|     349.438|   0.2%/387|   0.2%/387|   0.2%/388|   0.2%/388 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 172   |    4488|    1258.868|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 172   |     620|     636.357|   0.1%/489|   0.2%/460|   0.2%/452|   0.2%/445 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 172   |   13357|     621.877|   0.9%/ 81|   0.8%/ 86|   0.8%/ 87|   0.8%/ 88 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 172   |    6704|     631.430|   0.7%/ 93|   0.6%/109|   0.6%/115|   0.6%/120 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 172   |     122|      86.419|   2.7%/ 26|   2.5%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 172   |     453|     253.242|   1.0%/ 72|   0.8%/ 87|   0.8%/ 92|   0.7%/ 97 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 172   |    8664|     683.741|   0.3%/266|   0.3%/263|   0.3%/262|   0.3%/261 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 172   |    3504|     520.493|   0.3%/227|   0.3%/232|   0.3%/233|   0.3%/234 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 172   |    1279|     405.341|   0.6%/109|   0.6%/118|   0.6%/121|   0.6%/123 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 172   |     551|     189.272|   1.6%/ 42|   1.8%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 172   |    1115|     249.478|   0.8%/ 82|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 172   |    5383|    1158.028|   0.4%/179|   0.3%/203|   0.3%/210|   0.3%/217 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 172   |     138|     102.645|   0.3%/263|   0.3%/249|   0.3%/245|   0.3%/241 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 172   |    3882|     642.051|   0.2%/430|   0.2%/462|   0.1%/471|   0.1%/480 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 172   |    9287|    1336.409|   0.1%/504|   0.1%/516|   0.1%/518|   0.1%/521 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 172   |    6979|     698.772|   0.1%/487|   0.1%/507|   0.1%/512|   0.1%/518 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 172   |    2009|     356.240|   0.4%/180|   0.4%/181|   0.4%/181|   0.4%/181 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 172   |    2842|     954.765|   0.7%/104|   0.6%/118|   0.6%/121|   0.6%/125 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 172   |    1827|     297.646|   0.8%/ 92|   0.7%/ 92|   0.7%/ 93|   0.7%/ 93 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 172   |     149|     139.740|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.1%/ 34 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 172   |     447|     230.855|   0.5%/138|   0.5%/144|   0.5%/146|   0.5%/147 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 172   |    1545|     501.699|   0.8%/ 90|   0.7%/102|   0.7%/105|   0.6%/109 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 172   |     438|     322.165|   0.1%/843|   0.1%/857|   0.1%/857|   0.1%/856 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 172   |   16059|    1807.990|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 172   |     848|     404.563|   0.4%/168|   0.4%/182|   0.4%/186|   0.4%/190 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 172   |   33078|    1700.351|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 172   |    3237|     308.664|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 172   |     181|     237.576|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 172   |    4591|     392.759|   0.6%/115|   0.6%/111|   0.6%/109|   0.6%/108 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 172   |     956|     241.588|   0.8%/ 85|   0.7%/ 94|   0.7%/ 97|   0.7%/100 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 172   |     534|     126.673|   0.7%/104|   0.6%/122|   0.5%/127|   0.5%/133 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 172   |    7930|     619.434|   0.2%/399|   0.2%/405|   0.2%/406|   0.2%/408 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 172   |     596|     186.585|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 172   |    1085|    1024.481|   0.2%/315|   0.2%/293|   0.2%/287|   0.2%/282 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 172   |    3237|     628.762|   0.8%/ 87|   0.7%/ 98|   0.7%/101|   0.7%/104 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 172   |     192|     216.775|   1.0%/ 68|   1.1%/ 60|   1.2%/ 58|   1.2%/ 57 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 172   |    2234|     327.002|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 172   |   15286|     527.190|   0.8%/ 90|   0.7%/106|   0.6%/111|   0.6%/117 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 172   |  199610|     605.714|   0.4%/166|   0.4%/173|   0.4%/175|   0.4%/177 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 172   |     446|     139.163|   0.3%/221|   0.2%/314|   0.2%/351|   0.2%/397 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 172   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 172   |    2897|     339.407|   0.7%/ 97|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 172   |    2044|     268.467|   0.3%/219|   0.3%/238|   0.3%/243|   0.3%/248 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 172   |     310|     173.017|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 172   |    1246|     213.973|   0.5%/142|   0.5%/148|   0.5%/149|   0.5%/151 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 160   |      47|      81.983|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 172   |    1436|      44.572|   0.1%/543|   0.1%/548|   0.1%/548|   0.1%/546 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 172   |     364|     127.754|   1.1%/ 62|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 172   |    1670|      38.848|   0.5%/132|   0.5%/137|   0.5%/138|   0.5%/139 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 172   |     147|       4.737|   1.6%/ 42|   1.7%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 172   |   13163|     292.904|   2.0%/ 34|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 172   |     934|     315.831|   0.3%/254|   0.2%/292|   0.2%/304|   0.2%/316 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 172   |    1038|      40.429|   0.9%/ 74|   0.5%/134|   0.4%/169|   0.3%/227 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 172   |     761|      85.440|   0.2%/391|   0.2%/333|   0.2%/320|   0.2%/309 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 172   |     575|      57.148|   0.4%/180|   0.4%/181|   0.4%/182|   0.4%/182 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 172   |     220|     142.354|   0.8%/ 88|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 172   |    4972|      29.513|   0.7%/ 98|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 172   |     782|      83.079|   0.7%/ 98|   0.7%/100|   0.7%/100|   0.7%/101 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 172   |    9940|     862.487|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 167   |      40|       3.425|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 172   |    7854|     684.743|   0.7%/ 94|   0.6%/122|   0.5%/132|   0.5%/144 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 172   |     764|     231.324|   1.1%/ 60|   1.1%/ 64|   1.1%/ 65|   1.0%/ 66 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 172   |      15|       6.285|   5.5%/ 13|   5.2%/ 13|   5.2%/ 13|   5.1%/ 13 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 172   |  137098|     648.490|   0.6%/118|   0.6%/126|   0.5%/128|   0.5%/130 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 172   |     778|     111.886|   0.9%/ 73|   0.8%/ 85|   0.8%/ 89|   0.7%/ 93 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 172   |      56|       2.691|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 160   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 172   |     417|      15.719|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 172   |    9259|     243.666|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 120   |      62|      11.303|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 145   |      81|       5.004|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 172   |   12274|     642.355|   0.4%/161|   0.4%/167|   0.4%/168|   0.4%/169 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 172   |    4740|       3.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 172   |   24757|     501.193|   1.0%/ 72|   0.8%/ 89|   0.7%/ 94|   0.7%/100 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 172   |     699|     138.122|   2.6%/ 27|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 172   |     239|      58.571|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 172   |     112|       9.995|   0.8%/ 88|   0.8%/ 82|   0.9%/ 81|   0.9%/ 80 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 172   |     634|     108.887|   0.1%/705|   0.1%/623|   0.1%/605|   0.1%/588 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 172   |    2094|     202.136|   0.9%/ 81|   0.8%/ 91|   0.7%/ 94|   0.7%/ 97 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 172   |    7193|     411.749|   0.4%/182|   0.3%/199|   0.3%/204|   0.3%/209 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 172   |    5757|      57.418|   0.3%/221|   0.3%/226|   0.3%/228|   0.3%/229 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 172   |     824|     126.985|   0.6%/126|   0.4%/160|   0.4%/171|   0.4%/185 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 151   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 168   |    1133|      11.479|   1.4%/ 50|   1.1%/ 63|   1.0%/ 67|   1.0%/ 72 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 172   |     339|      61.265|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 172   |   31057|     463.012|   0.1%/612|   0.1%/529|   0.1%/511|   0.1%/493 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 172   |      53|      24.425|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 172   |     107|      45.681|   1.0%/ 70|   1.3%/ 54|   0.9%/ 73|   0.3%/223 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 169   |      19|       5.188|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 172   |    9384|     112.861|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 172   |     299|       9.865|   0.3%/211|   0.2%/288|   0.2%/314|   0.2%/344 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 172   |     329|      30.644|   1.2%/ 57|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 172   |    3095|     186.395|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/134 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 158   |      65|       5.309|   0.2%/323|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 147   |      40|      25.145|   0.2%/287|   0.2%/366|   0.2%/398|   0.2%/437 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 168   |     224|      19.341|   0.4%/177|   0.4%/190|   0.4%/195|   0.3%/200 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 172   |    2208|     241.045|   0.7%/100|   0.6%/121|   0.5%/129|   0.5%/137 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 172   |     640|      65.450|   0.4%/160|   0.5%/132|   0.5%/126|   0.6%/121 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 172   |   86584|      63.607|   1.4%/ 49|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 172   |    9457|      35.430|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 172   |   24026|     288.159|   0.6%/119|   0.6%/118|   0.6%/118|   0.6%/118 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 172   |    8548|     218.469|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 172   |    1787|     363.126|   0.1%/ ***|   0.1%/ ***|   0.1%/997|   0.1%/951 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 172   |    1224|     133.178|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 172   |   35669|     592.135|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 172   |      56|      20.418|   5.1%/ 13|   5.3%/ 13|   5.4%/ 13|   5.4%/ 13 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 172   |    1528|      12.130|   0.8%/ 90|   0.7%/ 99|   0.7%/101|   0.7%/104 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 172   |      28|       2.643|   3.8%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 172   |    1709|      91.447|   0.4%/191|   0.3%/271|   0.2%/301|   0.2%/340 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 172   |     652|      13.701|   0.6%/123|   0.5%/143|   0.5%/149|   0.4%/154 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 172   |     502|     279.552|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 169   |     577|     130.618|   0.5%/137|   0.5%/128|   0.5%/126|   0.6%/124 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 170   |    1040|     159.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 170   |      36|      18.816|   0.3%/221|   0.3%/214|   0.3%/211|   0.3%/209 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 172   |     288|      42.179|   2.9%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 169   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 171   |     434|      63.102|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 172   |      87|      31.298|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 126   |     220|       8.384|   0.6%/108|   0.6%/125|   0.5%/131|   0.5%/136 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 172   |     129|       3.943|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 172   |     128|       6.342|   0.1%/909|   0.1%/949|   0.1%/965|   0.1%/984 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 172   |     162|      39.638|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 172   |   73926|     584.035|   0.6%/112|   0.6%/124|   0.5%/127|   0.5%/131 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 172   |    1190|     443.799|   0.9%/ 74|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 172   |    1887|      52.595|   2.2%/ 31|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 118   |      41|       1.374|   3.1%/ 22|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  72   |     112|      45.477|   1.8%/ 39|   1.5%/ 45|   1.5%/ 47|   1.4%/ 50 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 127   |     417|      13.889|   2.7%/ 25|   2.1%/ 32|   2.0%/ 35|   1.8%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 172   |    6317|     361.861|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 172   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 172   |     148|      22.935|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 172   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 172   |    1104|       5.356|   0.3%/215|   0.3%/227|   0.3%/230|   0.3%/234 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 172   |     680|     327.345|   0.8%/ 88|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 172   |     266|      49.524|   0.1%/ ***|   0.1%/886|   0.1%/844|   0.1%/805 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 172   |     830|     177.959|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71|   1.0%/ 71 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 172   |    6428|      29.305|   0.1%/768|   0.1%/864|   0.1%/891|   0.1%/920 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 172   |    2254|     534.168|   0.6%/123|   0.5%/134|   0.5%/136|   0.5%/139 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  55   |       6|       0.695|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 172   |     690|      96.422|   3.2%/ 21|   2.6%/ 27|   2.4%/ 28|   2.3%/ 30 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 172   |   31529|     981.245|   0.4%/168|   0.4%/190|   0.4%/196|   0.3%/203 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 172   |    4917|      45.315|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 172   |    2275|      59.267|   0.6%/120|   0.6%/119|   0.6%/118|   0.6%/118 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 172   |    1888|     183.761|   0.2%/296|   0.3%/272|   0.3%/266|   0.3%/261 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 172   |     210|      76.399|   0.3%/246|   0.3%/249|   0.3%/251|   0.3%/252 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 172   |    4457|     229.664|   1.0%/ 71|   0.9%/ 76|   0.9%/ 78|   0.9%/ 80 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 172   |   19209|     130.901|   0.6%/112|   0.6%/111|   0.6%/111|   0.6%/111 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 113   |      25|       2.024|   0.0%/ --|   1.5%/ 46|   4.4%/ 16|   5.7%/ 12 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 172   |    4478|     130.875|   0.7%/100|   0.7%/106|   0.6%/107|   0.6%/109 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 172   |     305|      18.820|   0.3%/235|   0.2%/333|   0.2%/370|   0.2%/416 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 172   |     743|     106.764|   0.2%/416|   0.1%/541|   0.1%/583|   0.1%/631 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 150   |      73|       9.184|   0.1%/757|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 172   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 172   |      39|       7.221|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 172   |     137|      65.413|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 165   |      99|       6.212|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 172   |   16246|     276.410|   0.5%/128|   0.4%/168|   0.4%/182|   0.3%/199 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 172   |   30090|     638.850|   0.2%/329|   0.2%/298|   0.2%/291|   0.2%/285 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 172   |      13|       0.588|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 172   |     840|      19.799|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 172   |    5862|     567.060|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 172   |    2029|     235.866|   0.1%/942|   0.1%/860|   0.1%/840|   0.1%/821 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 172   |     181|      10.325|   2.0%/ 35|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 172   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 172   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 172   |      41|       5.497|   1.8%/ 37|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 172   |      71|      52.043|   5.2%/ 13|   4.8%/ 14|   4.7%/ 15|   4.6%/ 15 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 172   |     122|      10.421|   2.5%/ 28|   2.6%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 172   |    7337|      88.233|   0.9%/ 81|   0.9%/ 75|   0.9%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 172   |  199610|     605.714|   0.4%/166|   0.4%/173|   0.4%/175|   0.4%/177 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  58   |      64|       1.586|   3.6%/ 19|   2.6%/ 27|   2.2%/ 31|   1.9%/ 36 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 172   |    3567|      85.182|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 172   |     406|      41.015|   0.3%/271|   0.2%/296|   0.2%/304|   0.2%/311 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 172   |   41801|     629.194|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 172   |      46|      13.166|   0.2%/327|   0.1%/555|   0.1%/662|   0.1%/813 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 172   |     431|      12.631|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 172   |     542|      16.815|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  51   |      35|       0.364|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 171   |     326|      18.234|   0.7%/ 98|   0.8%/ 92|   0.8%/ 91|   0.8%/ 89 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 172   |     243|      16.011|   0.3%/273|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

