# State and Country COVID-19 Analysis #
## Updated: at 2020-09-07 for data as of 2020-09-06 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.9% of deaths and 57.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 159   |   33000|    1696.360|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 159   |   15976|    1798.710|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 159   |   13915|     352.181|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 84 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 159   |   14015|     483.357|   1.2%/ 58|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 159   |   12171|     566.663|   1.0%/ 70|   0.8%/ 86|   0.8%/ 91|   0.7%/ 97 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 159   |    9136|    1314.631|   0.2%/455|   0.1%/469|   0.1%/473|   0.1%/478 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 159   |    8383|     661.552|   0.3%/257|   0.3%/246|   0.3%/243|   0.3%/240 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 159   |    7769|     606.822|   0.2%/368|   0.2%/389|   0.2%/394|   0.2%/400 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 159   |    6815|     682.420|   0.2%/427|   0.2%/420|   0.2%/418|   0.2%/417 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 159   |    6102|     574.724|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 159   |  189984|     576.505|   0.5%/142|   0.5%/152|   0.4%/154|   0.4%/157 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 159   |  127855|     604.770|   0.7%/ 95|   0.7%/103|   0.7%/105|   0.6%/107 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 159   |   72417|      53.200|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 159   |   68230|     539.034|   0.8%/ 87|   0.7%/ 95|   0.7%/ 97|   0.7%/ 99 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 159   |   41384|     622.923|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 159   |   35557|     590.262|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 159   |   30736|     458.233|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 159   |   30734|     956.517|   0.6%/121|   0.5%/137|   0.5%/141|   0.5%/145 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 159   |   29323|     622.566|   0.2%/460|   0.2%/394|   0.2%/380|   0.2%/366 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 159   |   22447|     269.224|   0.5%/126|   0.5%/145|   0.5%/151|   0.4%/157 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 159   |    2291|     467.225|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82|   0.8%/ 82 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 159   |      42|      57.856|   1.7%/ 40|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 159   |    5285|     726.035|   0.7%/105|   0.6%/124|   0.5%/129|   0.5%/135 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 159   |     895|     296.683|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 159   |   13915|     352.181|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 84 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 159   |    1969|     341.867|   0.2%/357|   0.2%/356|   0.2%/355|   0.2%/355 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 159   |    4471|    1254.030|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 159   |     609|     625.686|   0.1%/688|   0.1%/737|   0.1%/752|   0.1%/769 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 159   |   12171|     566.663|   1.0%/ 70|   0.8%/ 86|   0.8%/ 91|   0.7%/ 97 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 159   |    6102|     574.724|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 159   |      84|      59.241|   4.0%/ 17|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 159   |     402|     224.766|   1.5%/ 46|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 159   |    8383|     661.552|   0.3%/257|   0.3%/246|   0.3%/243|   0.3%/240 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 159   |    3375|     501.338|   0.3%/209|   0.3%/219|   0.3%/221|   0.3%/224 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 159   |    1174|     372.169|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84|   0.8%/ 85 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 159   |     479|     164.298|   0.9%/ 79|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 159   |     998|     223.341|   1.0%/ 70|   1.0%/ 67|   1.0%/ 67|   1.0%/ 66 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 159   |    5148|    1107.311|   0.5%/137|   0.4%/163|   0.4%/171|   0.4%/180 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 159   |     135|     100.113|   0.2%/281|   0.2%/291|   0.2%/294|   0.2%/297 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 159   |    3802|     628.925|   0.2%/333|   0.2%/338|   0.2%/339|   0.2%/340 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 159   |    9136|    1314.631|   0.2%/455|   0.1%/469|   0.1%/473|   0.1%/478 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 159   |    6815|     682.420|   0.2%/427|   0.2%/420|   0.2%/418|   0.2%/417 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 159   |    1919|     340.249|   0.4%/178|   0.4%/191|   0.4%/195|   0.3%/199 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 159   |    2635|     885.521|   0.9%/ 75|   0.8%/ 84|   0.8%/ 87|   0.8%/ 90 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 159   |    1621|     264.141|   1.0%/ 72|   1.1%/ 65|   1.1%/ 63|   1.1%/ 62 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 159   |     117|     109.070|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 159   |     409|     211.631|   0.5%/144|   0.4%/161|   0.4%/166|   0.4%/172 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 159   |    1427|     463.175|   1.1%/ 62|   1.0%/ 71|   0.9%/ 73|   0.9%/ 76 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 159   |     435|     319.597|   0.1%/937|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 159   |   15976|    1798.710|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 159   |     806|     384.457|   0.5%/129|   0.5%/135|   0.5%/137|   0.5%/139 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 159   |   33000|    1696.360|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 159   |    2894|     275.932|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 159   |     155|     203.077|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 159   |    4285|     366.539|   0.5%/134|   0.5%/139|   0.5%/140|   0.5%/141 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 159   |     868|     219.288|   1.2%/ 59|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 159   |     488|     115.734|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 159   |    7769|     606.822|   0.2%/368|   0.2%/389|   0.2%/394|   0.2%/400 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 159   |     487|     152.342|   1.5%/ 46|   1.3%/ 54|   1.2%/ 57|   1.2%/ 59 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 159   |    1058|     998.349|   0.2%/446|   0.2%/436|   0.2%/434|   0.2%/433 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 159   |    2941|     571.305|   1.1%/ 64|   1.0%/ 73|   0.9%/ 75|   0.9%/ 78 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 159   |     174|     196.257|   0.6%/122|   0.5%/133|   0.5%/136|   0.5%/139 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 159   |    1928|     282.211|   1.3%/ 52|   1.2%/ 58|   1.1%/ 60|   1.1%/ 62 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 159   |   14015|     483.357|   1.2%/ 58|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 159   |  189984|     576.505|   0.5%/142|   0.5%/152|   0.4%/154|   0.4%/157 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 159   |     428|     133.499|   0.6%/112|   0.5%/133|   0.5%/140|   0.5%/147 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 159   |      58|      92.981|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 159   |    2678|     313.742|   0.6%/116|   0.6%/109|   0.6%/107|   0.7%/106 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 159   |    1981|     260.212|   0.4%/177|   0.3%/225|   0.3%/241|   0.3%/259 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 159   |     249|     138.955|   2.3%/ 30|   2.4%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 159   |    1169|     200.697|   0.6%/121|   0.6%/123|   0.6%/123|   0.6%/123 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 147   |      42|      73.317|   0.3%/243|   0.2%/326|   0.2%/351|   0.2%/376 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 159   |    1422|      44.121|   0.1%/694|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 159   |     315|     110.812|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 159   |    1566|      36.412|   0.6%/120|   0.5%/130|   0.5%/132|   0.5%/135 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 159   |     120|       3.864|   1.3%/ 51|   1.1%/ 61|   1.1%/ 63|   1.0%/ 66 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 159   |   10263|     228.386|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 159   |     902|     305.037|   0.4%/178|   0.3%/199|   0.3%/205|   0.3%/212 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 159   |     798|      31.073|   3.0%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 159   |     737|      82.751|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 159   |     546|      54.282|   0.4%/181|   0.4%/186|   0.4%/186|   0.4%/187 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 159   |     199|     128.752|   0.6%/119|   0.5%/139|   0.5%/144|   0.5%/151 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 159   |    4531|      26.893|   0.9%/ 76|   0.9%/ 80|   0.9%/ 81|   0.8%/ 83 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 159   |     710|      75.462|   0.7%/ 93|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 159   |    9899|     858.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 154   |      40|       3.439|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 159   |    5502|     479.710|   1.3%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 159   |     672|     203.468|   1.4%/ 50|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 159   |       7|       2.853|   7.8%/  9|   9.3%/  7|   9.8%/  7|  10.2%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 159   |  127855|     604.770|   0.7%/ 95|   0.7%/103|   0.7%/105|   0.6%/107 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 159   |     684|      98.360|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 159   |      55|       2.646|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 147   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 159   |     417|      15.706|   0.1%/542|   0.1%/687|   0.1%/735|   0.1%/791 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 159   |    9206|     242.265|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 107   |      62|      11.292|   0.1%/569|   0.2%/428|   0.2%/403|   0.2%/383 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 132   |      77|       4.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 159   |   11622|     608.252|   0.5%/143|   0.5%/148|   0.5%/150|   0.5%/151 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 159   |    4733|       3.375|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 159   |   21849|     442.322|   1.5%/ 46|   1.3%/ 52|   1.3%/ 54|   1.2%/ 56 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 159   |     503|      99.393|   2.1%/ 32|   1.8%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 159   |     196|      48.014|   1.0%/ 69|   1.1%/ 63|   1.1%/ 61|   1.2%/ 60 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 159   |      95|       8.502|   0.6%/119|   0.7%/100|   0.7%/ 96|   0.8%/ 92 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 159   |     627|     107.631|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 159   |    1847|     178.344|   1.2%/ 58|   1.2%/ 60|   1.2%/ 60|   1.2%/ 60 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 159   |    6751|     386.486|   0.5%/144|   0.5%/143|   0.5%/143|   0.5%/142 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 159   |    5531|      55.157|   0.3%/204|   0.3%/207|   0.3%/207|   0.3%/208 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 159   |     770|     118.657|   0.9%/ 74|   0.8%/ 87|   0.8%/ 91|   0.7%/ 95 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 138   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 155   |     957|       9.700|   2.3%/ 30|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 159   |     336|      60.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 159   |   30736|     458.233|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 159   |      53|      24.614|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 159   |     221|      94.081|   0.0%/ --|   1.0%/ 67|   0.7%/101|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 156   |      19|       5.214|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 159   |    9336|     112.275|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 159   |     294|       9.697|   0.6%/107|   0.4%/168|   0.4%/196|   0.3%/234 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 159   |     283|      26.409|   1.1%/ 65|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 159   |    2915|     175.539|   0.7%/ 92|   0.6%/111|   0.6%/117|   0.6%/124 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 145   |      62|       5.081|   0.8%/ 83|   0.8%/ 83|   0.8%/ 84|   0.8%/ 84 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 134   |      36|      22.721|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 155   |     211|      18.189|   0.5%/127|   0.6%/124|   0.6%/122|   0.6%/120 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 159   |    2004|     218.846|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 159   |     621|      63.589|   0.1%/484|   0.2%/437|   0.2%/426|   0.2%/414 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 159   |   72417|      53.200|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 159   |    8000|      29.972|   1.3%/ 53|   1.4%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 159   |   22447|     269.224|   0.5%/126|   0.5%/145|   0.5%/151|   0.4%/157 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 159   |    7565|     193.337|   1.1%/ 61|   1.1%/ 64|   1.1%/ 65|   1.1%/ 66 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 159   |    1778|     361.309|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 159   |    1053|     114.581|   1.5%/ 47|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 159   |   35557|     590.262|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 159   |      24|       8.679|   3.5%/ 20|   4.0%/ 17|   4.2%/ 16|   4.3%/ 16 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 159   |    1374|      10.911|   1.0%/ 66|   1.1%/ 64|   1.1%/ 63|   1.1%/ 63 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 159   |      16|       1.527|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 159   |    1667|      89.215|   0.8%/ 92|   0.6%/118|   0.5%/128|   0.5%/139 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 159   |     621|      13.048|   0.8%/ 89|   0.5%/139|   0.4%/162|   0.4%/193 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 159   |     533|     296.623|   0.5%/148|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 156   |     545|     123.309|   0.4%/192|   0.3%/219|   0.3%/227|   0.3%/235 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 157   |     975|     149.219|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 157   |      35|      18.228|   0.5%/153|   0.5%/131|   0.5%/126|   0.6%/122 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 159   |     198|      29.003|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 156   |      82|      18.408|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 158   |     287|      41.742|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 159   |      87|      31.167|   0.2%/364|   0.2%/401|   0.2%/416|   0.2%/434 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 113   |     202|       7.676|   0.8%/ 86|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 159   |     127|       3.891|   0.1%/ ***|   0.1%/855|   0.1%/809|   0.1%/767 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 159   |     126|       6.238|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 159   |     160|      39.189|   0.1%/666|   0.1%/565|   0.1%/544|   0.1%/524 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 159   |   68230|     539.034|   0.8%/ 87|   0.7%/ 95|   0.7%/ 97|   0.7%/ 99 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 159   |    1057|     394.173|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 159   |    1436|      40.040|   3.2%/ 21|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 105   |      26|       0.878|   2.1%/ 33|   2.5%/ 27|   2.7%/ 26|   2.8%/ 25 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  59   |      92|      37.540|   4.6%/ 15|   3.0%/ 23|   2.5%/ 27|   2.0%/ 34 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 114   |     301|      10.036|   4.9%/ 14|   4.6%/ 15|   4.5%/ 15|   4.4%/ 16 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 159   |    6279|     359.682|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 159   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 159   |     143|      22.073|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 159   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 159   |    1050|       5.094|   0.4%/172|   0.4%/169|   0.4%/168|   0.4%/166 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 159   |     620|     298.568|   0.6%/118|   0.6%/120|   0.6%/121|   0.6%/122 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 159   |     266|      49.471|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 159   |     728|     156.012|   1.0%/ 67|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 159   |    6359|      28.993|   0.1%/559|   0.1%/644|   0.1%/668|   0.1%/694 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 159   |    2110|     500.213|   0.7%/ 97|   0.6%/112|   0.6%/117|   0.6%/122 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  42   |       5|       0.560|   3.0%/ 23|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 159   |     466|      65.094|   5.5%/ 12|   5.3%/ 13|   5.3%/ 13|   5.2%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 159   |   30734|     956.517|   0.6%/121|   0.5%/137|   0.5%/141|   0.5%/145 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 159   |    3925|      36.167|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 159   |    2124|      55.334|   0.6%/118|   0.6%/119|   0.6%/119|   0.6%/119 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 159   |    1840|     179.066|   0.2%/419|   0.2%/423|   0.2%/424|   0.2%/425 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 159   |     202|      73.384|   0.3%/241|   0.3%/252|   0.3%/253|   0.3%/253 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 159   |    3925|     202.287|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 159   |   17816|     121.411|   0.6%/114|   0.6%/117|   0.6%/118|   0.6%/119 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 100   |      19|       1.572|   3.0%/ 23|   1.8%/ 38|   1.5%/ 46|   1.2%/ 57 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 159   |    4115|     120.251|   0.8%/ 86|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 159   |     297|      18.321|   0.6%/122|   0.4%/166|   0.4%/182|   0.3%/202 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 159   |     732|     105.127|   0.3%/262|   0.2%/439|   0.1%/525|   0.1%/652 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 137   |      71|       8.985|   0.2%/386|   0.2%/327|   0.2%/314|   0.2%/303 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 159   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 159   |      34|       6.244|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 159   |     135|      64.570|   0.2%/397|   0.1%/470|   0.1%/491|   0.1%/513 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 152   |      98|       6.156|   0.2%/459|   0.2%/448|   0.2%/449|   0.2%/454 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 159   |   15262|     259.676|   0.9%/ 75|   0.7%/ 99|   0.6%/108|   0.6%/118 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 159   |   29323|     622.566|   0.2%/460|   0.2%/394|   0.2%/380|   0.2%/366 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 159   |      12|       0.562|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 159   |     835|      19.671|   0.1%/503|   0.1%/822|   0.1%/973|   0.1%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 159   |    5837|     564.606|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 159   |    2014|     234.077|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 159   |     139|       7.957|   3.0%/ 23|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 159   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 159   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 159   |      31|       4.049|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 159   |      32|      23.301|   6.8%/ 10|   7.6%/  9|   7.9%/  9|   8.1%/  8 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 159   |      87|       7.381|   2.1%/ 33|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 159   |    6448|      77.538|   0.6%/112|   0.7%/ 99|   0.7%/ 96|   0.7%/ 93 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 159   |  189984|     576.505|   0.5%/142|   0.5%/152|   0.4%/154|   0.4%/157 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  45   |      40|       0.983|   3.2%/ 21|   4.6%/ 15|   5.4%/ 13|   6.2%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 159   |    2861|      68.317|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 159   |     391|      39.484|   0.3%/228|   0.3%/238|   0.3%/241|   0.3%/245 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 159   |   41384|     622.923|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 159   |      46|      13.034|   0.6%/109|   0.6%/121|   0.6%/125|   0.5%/130 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 159   |     359|      10.522|   1.8%/ 39|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 159   |     441|      13.677|   1.8%/ 38|   1.6%/ 44|   1.5%/ 46|   1.4%/ 48 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  38   |      35|       0.366|   2.4%/ 29|   1.0%/ 70|   0.6%/119|   0.2%/377 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 158   |     304|      17.020|   0.4%/163|   0.3%/275|   0.2%/329|   0.2%/411 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 159   |     228|      15.008|   1.3%/ 53|   0.5%/127|   0.4%/195|   0.2%/423 |

