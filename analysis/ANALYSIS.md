# State and Country COVID-19 Analysis #
## Updated: at 2020-07-27 for data as of 2020-07-26 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.4% of deaths and 39.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.3% of deaths and 56.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 117   |   32639|    1677.766|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 117   |   15843|    1783.667|   0.1%/558|   0.1%/985|   0.1%/ ***|   0.0%/ *** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 117   |    8534|    1228.057|   0.2%/386|   0.2%/430|   0.2%/442|   0.2%/455 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 117   |    8493|     214.948|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 117   |    7629|     602.018|   0.2%/314|   0.2%/409|   0.2%/439|   0.1%/472 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 117   |    7146|     558.227|   0.2%/284|   0.2%/309|   0.2%/316|   0.2%/323 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 117   |    6420|     642.806|   0.1%/623|   0.1%/834|   0.1%/915|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 117   |    5849|     272.307|   2.3%/ 29|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 117   |    5040|     173.809|   3.4%/ 20|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 117   |    4423|    1240.704|   0.1%/824|   0.1%/944|   0.1%/991|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 117   |  146694|     445.142|   0.6%/112|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 117   |   87631|     414.503|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 117   |   45887|     690.698|   0.2%/445|   0.1%/474|   0.1%/481|   0.1%/488 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 117   |   43881|     346.676|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 117   |   35125|     583.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 117   |   32757|      24.064|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 117   |   30238|     450.799|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   28435|     603.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 117   |   14638|     455.565|   1.3%/ 54|   1.1%/ 63|   1.1%/ 66|   1.0%/ 69 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 117   |   15726|     188.607|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 117   |    1471|     299.936|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 117   |      19|      26.623|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 117   |    3346|     459.659|   2.9%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 117   |     403|     133.698|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 117   |    8493|     214.948|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 117   |    1794|     311.466|   0.3%/231|   0.3%/207|   0.3%/201|   0.4%/196 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 117   |    4423|    1240.704|   0.1%/824|   0.1%/944|   0.1%/991|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 117   |     549|     563.481|   0.2%/356|   0.2%/310|   0.2%/299|   0.2%/289 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 117   |    5849|     272.307|   2.3%/ 29|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 117   |    3452|     325.105|   1.2%/ 59|   1.4%/ 49|   1.5%/ 47|   1.5%/ 45 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 117   |      27|      18.732|   1.4%/ 49|   1.9%/ 35|   2.1%/ 33|   2.2%/ 31 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 117   |     144|      80.858|   1.7%/ 40|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 117   |    7629|     602.018|   0.2%/314|   0.2%/409|   0.2%/439|   0.1%/472 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 117   |    2900|     430.797|   0.4%/189|   0.4%/182|   0.4%/180|   0.4%/178 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 117   |     834|     264.275|   0.7%/100|   0.7%/ 96|   0.7%/ 95|   0.7%/ 95 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 117   |     329|     113.015|   0.8%/ 83|   0.9%/ 73|   1.0%/ 71|   1.0%/ 69 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 117   |     703|     157.368|   0.8%/ 87|   0.8%/ 92|   0.7%/ 93|   0.7%/ 94 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 117   |    3626|     780.072|   0.9%/ 78|   1.1%/ 63|   1.2%/ 60|   1.2%/ 57 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 117   |     120|      89.207|   0.4%/180|   0.3%/242|   0.3%/265|   0.2%/293 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 117   |    3442|     569.303|   0.3%/258|   0.3%/271|   0.3%/273|   0.3%/276 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 117   |    8534|    1228.057|   0.2%/386|   0.2%/430|   0.2%/442|   0.2%/455 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 117   |    6420|     642.806|   0.1%/623|   0.1%/834|   0.1%/915|   0.1%/ *** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 117   |    1616|     286.599|   0.3%/209|   0.3%/211|   0.3%/212|   0.3%/213 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 117   |    1493|     501.794|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 117   |    1200|     195.447|   0.7%/ 95|   0.8%/ 85|   0.8%/ 83|   0.9%/ 80 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 117   |      47|      44.422|   2.9%/ 24|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 117   |     319|     164.766|   0.7%/102|   0.8%/ 92|   0.8%/ 90|   0.8%/ 88 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 117   |     736|     238.839|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 117   |     408|     300.201|   0.4%/193|   0.4%/184|   0.4%/180|   0.4%/177 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 117   |   15843|    1783.667|   0.1%/558|   0.1%/985|   0.1%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 117   |     610|     291.128|   0.9%/ 81|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 117   |   32639|    1677.766|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 117   |    1816|     173.146|   1.3%/ 53|   1.4%/ 49|   1.5%/ 48|   1.5%/ 47 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 117   |      99|     130.124|   1.1%/ 65|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 117   |    3309|     283.100|   0.6%/110|   0.7%/104|   0.7%/102|   0.7%/100 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 117   |     491|     124.122|   1.2%/ 57|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 117   |     287|      68.037|   1.4%/ 48|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 117   |    7146|     558.227|   0.2%/284|   0.2%/309|   0.2%/316|   0.2%/323 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 117   |     194|      60.884|   1.4%/ 48|   1.7%/ 40|   1.8%/ 39|   1.9%/ 37 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 117   |    1005|     949.043|   0.2%/392|   0.1%/467|   0.1%/490|   0.1%/515 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 117   |    1430|     277.730|   3.3%/ 21|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 117   |     125|     141.604|   1.0%/ 71|   0.8%/ 87|   0.7%/ 92|   0.7%/ 99 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 117   |     968|     141.692|   2.0%/ 35|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 117   |    5040|     173.809|   3.4%/ 20|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 117   |  146694|     445.142|   0.6%/112|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 117   |     279|      87.130|   1.9%/ 37|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 117   |      56|      89.745|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 117   |    2094|     245.276|   0.4%/160|   0.3%/217|   0.3%/237|   0.3%/261 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 117   |    1497|     196.618|   0.6%/120|   0.5%/131|   0.5%/133|   0.5%/136 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 117   |     103|      57.680|   0.5%/141|   0.5%/132|   0.5%/130|   0.5%/129 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 117   |     885|     151.924|   0.6%/110|   0.7%/ 93|   0.8%/ 89|   0.8%/ 85 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 105   |      26|      44.755|   0.7%/ 96|   0.6%/122|   0.5%/134|   0.5%/149 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 117   |    1293|      40.119|   1.5%/ 46|   1.2%/ 59|   1.1%/ 64|   1.0%/ 71 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 117   |     136|      47.790|   2.9%/ 24|   2.9%/ 23|   2.9%/ 23|   3.0%/ 23 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 117   |    1153|      26.819|   1.0%/ 72|   1.0%/ 69|   1.0%/ 68|   1.0%/ 68 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 117   |      38|       1.211|   3.6%/ 19|   3.9%/ 18|   4.0%/ 17|   4.1%/ 17 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 117   |    2928|      65.148|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 117   |     721|     243.881|   1.7%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 117   |     134|       5.206|   2.6%/ 26|   3.5%/ 20|   3.7%/ 19|   3.9%/ 17 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 117   |     712|      80.033|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 117   |     421|      41.782|   2.3%/ 30|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 117   |     142|      91.795|   1.8%/ 39|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 117   |    2938|      17.440|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 117   |     537|      57.036|   1.0%/ 67|   0.9%/ 74|   0.9%/ 75|   0.9%/ 77 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 117   |    9820|     852.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 112   |      36|       3.086|   0.0%/ --|   3.1%/ 22|   0.0%/ --|   1.0%/ 71 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 117   |    2614|     227.865|   2.7%/ 25|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 117   |     285|      86.482|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 117   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 117   |   87631|     414.503|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 117   |     342|      49.164|   1.7%/ 41|   1.7%/ 40|   1.7%/ 39|   1.8%/ 39 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 117   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 105   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 117   |     391|      14.732|   0.5%/145|   0.5%/128|   0.6%/125|   0.6%/122 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 117   |    8950|     235.526|   0.1%/814|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  65   |      59|      10.826|   0.9%/ 74|   1.3%/ 53|   1.4%/ 50|   1.5%/ 47 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  90   |      75|       4.623|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 117   |    9362|     489.991|   1.1%/ 65|   0.9%/ 75|   0.9%/ 78|   0.9%/ 80 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 117   |    4645|       3.313|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 117   |    8490|     171.873|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 117   |     102|      20.219|   7.9%/  9|   8.7%/  8|   8.9%/  8|   9.1%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 117   |     128|      31.465|   1.0%/ 69|   1.3%/ 55|   1.3%/ 52|   1.4%/ 50 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 117   |      87|       7.781|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 117   |     613|     105.259|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 117   |    1068|     103.096|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 117   |    5557|     318.134|   0.7%/105|   0.6%/117|   0.6%/121|   0.6%/124 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 117   |    4714|      47.009|   1.3%/ 53|   1.0%/ 70|   0.9%/ 77|   0.8%/ 84 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 117   |     406|      62.661|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  96   |      51|      37.548|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 113   |     216|       2.192|   3.8%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 117   |     328|      59.389|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 117   |   30238|     450.799|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 117   |      48|      22.089|   0.5%/128|   0.7%/ 98|   0.8%/ 91|   0.8%/ 85 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 117   |       6|       2.394|   5.8%/ 12|   7.1%/ 10|   7.5%/  9|   7.9%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 114   |      16|       4.303|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 117   |    9125|     109.746|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 117   |     163|       5.393|   1.5%/ 47|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 117   |     200|      18.675|   0.3%/226|   0.4%/165|   0.5%/154|   0.5%/144 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 117   |    1781|     107.285|   2.6%/ 26|   2.2%/ 31|   2.1%/ 32|   2.0%/ 34 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 103   |      43|       3.508|   1.1%/ 65|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  92   |      26|      16.240|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 113   |     161|      13.914|   1.1%/ 60|   0.7%/ 93|   0.6%/107|   0.6%/125 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 117   |    1108|     121.013|   2.8%/ 25|   2.8%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 117   |     597|      61.123|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 117   |   32757|      24.064|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 117   |    4794|      17.959|   2.1%/ 32|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 117   |   15726|     188.607|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 117   |    4487|     114.686|   2.4%/ 29|   2.0%/ 35|   1.8%/ 37|   1.7%/ 40 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 117   |    1763|     358.143|   0.1%/844|   0.1%/694|   0.1%/663|   0.1%/634 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 117   |     461|      50.196|   1.8%/ 38|   2.1%/ 33|   2.1%/ 32|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 117   |   35125|     583.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 117   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 117   |     994|       7.895|   0.1%/635|   0.1%/508|   0.1%/481|   0.2%/455 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 117   |      11|       1.049|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 117   |     636|      34.015|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 117   |     286|       6.005|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 117   |     177|      98.661|   4.1%/ 17|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 114   |     430|      97.380|   0.8%/ 91|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 115   |    1212|     185.452|   4.3%/ 16|   3.4%/ 20|   3.2%/ 21|   3.0%/ 23 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 115   |      31|      16.388|   0.1%/587|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 117   |      44|       6.426|   1.8%/ 39|   2.3%/ 30|   2.4%/ 28|   2.6%/ 27 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 114   |      77|      17.248|   0.9%/ 74|   0.3%/256|   0.1%/683|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 116   |      60|       8.744|   1.4%/ 49|   4.5%/ 15|   3.1%/ 23|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 117   |      80|      28.695|   0.1%/891|   0.1%/886|   0.1%/890|   0.1%/898 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  71   |      85|       3.226|   5.7%/ 12|   5.2%/ 13|   5.1%/ 14|   4.9%/ 14 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 117   |     123|       3.770|   0.1%/708|   0.1%/641|   0.1%/628|   0.1%/617 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 117   |     123|       6.079|   0.2%/447|   0.1%/530|   0.1%/545|   0.1%/557 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 117   |     160|      39.199|   0.5%/137|   0.2%/292|   0.2%/411|   0.1%/691 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 117   |   43881|     346.676|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 117   |     741|     276.238|   1.0%/ 68|   0.9%/ 75|   0.9%/ 76|   0.9%/ 78 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 117   |     297|       8.265|   1.6%/ 44|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  63   |      11|       0.380|   2.1%/ 33|   1.1%/ 61|   0.8%/ 87|   0.4%/168 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  17   |       8|       3.253|  26.0%/  2|   0.0%/ --|   0.0%/ --|   4.6%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  72   |      45|       1.492|   1.3%/ 52|   1.8%/ 37|   2.0%/ 34|   2.2%/ 32 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 117   |    6159|     352.836|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 117   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 117   |     110|      17.086|   1.1%/ 64|   1.0%/ 71|   0.9%/ 74|   0.9%/ 76 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 117   |      69|       3.104|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 117   |     865|       4.197|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 117   |     466|     224.197|   1.4%/ 48|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 117   |     256|      47.663|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 117   |     386|      82.730|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26|   2.6%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 117   |    5935|      27.058|   0.8%/ 87|   0.6%/125|   0.5%/140|   0.4%/159 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 117   |    1313|     311.235|   2.6%/ 26|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 117   |      41|       5.716|   3.9%/ 17|   4.6%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 117   |   14638|     455.565|   1.3%/ 54|   1.1%/ 63|   1.1%/ 66|   1.0%/ 69 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 117   |    1958|      18.042|   0.9%/ 76|   0.9%/ 75|   0.9%/ 75|   0.9%/ 75 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 117   |    1673|      43.603|   0.4%/160|   0.4%/175|   0.4%/179|   0.4%/183 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 117   |    1722|     167.568|   0.3%/259|   0.2%/307|   0.2%/321|   0.2%/335 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 117   |     169|      61.401|   0.9%/ 77|   0.6%/126|   0.5%/148|   0.4%/179 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 117   |    2188|     112.763|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 117   |   13392|      91.257|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  58   |       5|       0.415|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 117   |    2774|      81.067|   1.5%/ 45|   1.3%/ 52|   1.3%/ 55|   1.2%/ 57 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 117   |     189|      11.641|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 117   |     554|      79.556|   2.1%/ 32|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  95   |      67|       8.428|   0.3%/235|   0.2%/306|   0.2%/339|   0.2%/385 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 117   |      27|       4.779|   0.1%/509|   0.1%/816|   0.1%/ ***|   0.1%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 117   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 117   |     115|      55.001|   0.2%/334|   0.3%/231|   0.3%/213|   0.3%/198 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 110   |      93|       5.866|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 117   |    6687|     113.772|   3.7%/ 18|   3.9%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   28435|     603.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 117   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 117   |     723|      17.033|   0.7%/ 95|   0.7%/100|   0.7%/101|   0.7%/103 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 117   |    5716|     552.887|   0.2%/311|   0.2%/340|   0.2%/348|   0.2%/356 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 117   |    1976|     229.625|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 117   |      40|       2.263|   5.1%/ 14|   4.1%/ 17|   4.0%/ 17|   2.8%/ 25 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 117   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 117   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 117   |      16|       2.156|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 117   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 117   |      50|       4.265|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 117   |    5621|      67.594|   0.3%/210|   0.3%/221|   0.3%/224|   0.3%/227 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 117   |  146694|     445.142|   0.6%/112|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 117   |    1630|      38.932|   1.1%/ 62|   1.0%/ 67|   1.0%/ 68|   1.0%/ 70 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 117   |     345|      34.928|   0.3%/269|   0.2%/357|   0.2%/388|   0.2%/425 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 117   |   45887|     690.698|   0.2%/445|   0.1%/474|   0.1%/481|   0.1%/488 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 117   |      35|       9.888|   0.8%/ 84|   0.7%/100|   0.7%/105|   0.6%/112 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 117   |     123|       3.600|   4.9%/ 14|   4.0%/ 17|   3.7%/ 18|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 117   |     144|       4.483|   3.5%/ 20|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 116   |     172|       9.625|   9.0%/  8|   8.2%/  8|   7.9%/  9|   7.5%/  9 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 117   |      36|       2.377|   6.2%/ 11|   4.8%/ 14|   4.4%/ 16|   4.1%/ 17 |

