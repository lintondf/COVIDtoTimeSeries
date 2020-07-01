# State and Country COVID-19 Analysis #
## Updated: at 2020-07-01 for data as of 2020-06-30 00:00:00 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

Daily Death Growth Rate (DDGR)  is the cube root of Arnold Kling's [Three Day Death Reproduction Rate (3DDRR)](http://www.arnoldkling.com/blog/the-3ddrr/).  The 3DDRR is calculated by dividing the cumulative total number of deaths on a given day by the  cumulative total number of deaths three days previously; yes, technically this is a factor not a rate, but we must grant Professor Kling the author's naming rights.  Taking the cube root converts this to the geometric mean for the three days.  These values are LOWESS filtered to generate local-error minimizing non-parametric trend lines.

If deaths remain constant over the three days, the DDGR equals one.  A value of 2 would indicate that the number of deaths doubles every day.

Up until June 29, 2020, this page reported the DDGR directly, but as the high growth phase of the pandemic has passed, the DDGR values have  declined toward one, required progressively more digits of precision to show differences.  Accordingly, henceforth this page will report DDGR as a true growth percentage rate (100*(DDGR-1)) which will be termed the Daily Death Rate of Growth (DDRG).  A DDRG of 100% means the number of deaths doubles every day, 0% means no new deaths.

Why the focus on deaths not cases?  The problem with case statistics is that what is counted has changed nearly continuously since the start of the pandemic and continues to this day.  Early on, only patients sick enough to go to the hospital could be counted.  As tests came online (and eventually actually worked), people visiting a doctor could be tested and counted.  As of mid-2020, in the U.S., drive-up testing is more widely available, but since that involves the choice to undergo the unpleasantness of a deep nasal swab, current testing is by no means a random sample of the U.S. population.

The death statistics are not perfect.  Some claim conflating "dying of COVID-19" vs "dying with COVID-19" overstates death counts.  Others say political incentives motivate widespread undercounting.


# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDRG.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 109   |   31576|    1623.171|   0.1%/484|   0.1%/519|   0.1%/528|   0.1%/536 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 113   |   14972|    1685.614|   0.3%/264|   0.2%/390|   0.2%/441|   0.1%/505 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 103   |    8117|    1168.065|   0.4%/185|   0.3%/222|   0.3%/234|   0.3%/247 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 106   |    6990|     551.640|   0.6%/125|   0.4%/169|   0.4%/185|   0.3%/205 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 104   |    6674|     521.340|   0.4%/172|   0.3%/214|   0.3%/227|   0.3%/242 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 104   |    6183|     619.081|   0.2%/404|   0.2%/435|   0.2%/442|   0.2%/449 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 119   |    6104|     154.476|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 104   |    4337|    1216.528|   0.2%/351|   0.1%/483|   0.1%/530|   0.1%/588 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 115   |    3501|     163.027|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 109   |    3227|     694.079|   0.4%/174|   0.4%/183|   0.4%/186|   0.4%/189 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 123   |  127267|     386.191|   0.6%/116|   0.6%/118|   0.6%/119|   0.6%/119 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 106   |   60325|     285.343|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 112   |   43933|     661.289|   0.3%/239|   0.3%/274|   0.2%/284|   0.2%/296 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 131   |   34864|     578.771|   0.1%/951|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 137   |   29892|     445.637|   0.1%/909|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 120   |   28631|     607.869|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 104   |   28654|     226.377|   3.0%/ 23|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 112   |   18382|      13.504|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 132   |   10729|     128.679|   1.3%/ 55|   1.3%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 112   |    9749|     845.971|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.
 
For confirmed cases, the story is not so different.

![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to day from COVID-19 compared to historical seasonal flus and 20th century pandemics.

![Compared To Flus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/ComparedToFlus.png)


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

Click on the link in the first column to view the DDRG and IHME charts for a specific state.

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  98   |     949|     193.578|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  98   |      14|      19.101|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 102   |    1648|     226.471|   2.1%/ 33|   2.1%/ 32|   2.1%/ 32|   2.2%/ 32 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  99   |     276|      91.505|   2.4%/ 28|   2.2%/ 31|   2.1%/ 33|   2.1%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 119   |    6104|     154.476|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 109   |    1695|     294.400|   0.3%/231|   0.2%/348|   0.2%/398|   0.1%/464 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 104   |    4337|    1216.528|   0.2%/351|   0.1%/483|   0.1%/530|   0.1%/588 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  97   |     524|     537.622|   0.3%/273|   0.1%/726|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 115   |    3501|     163.027|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 111   |    2845|     267.966|   0.8%/ 91|   0.5%/141|   0.4%/162|   0.4%/191 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  92   |      17|      12.007|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  97   |      91|      51.170|   0.3%/214|   0.3%/222|   0.3%/221|   0.3%/219 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 106   |    6990|     551.640|   0.6%/125|   0.4%/169|   0.4%/185|   0.3%/205 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 107   |    2655|     394.382|   0.5%/138|   0.4%/173|   0.4%/185|   0.3%/199 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  98   |     716|     226.833|   0.5%/132|   0.4%/162|   0.4%/171|   0.4%/179 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 110   |     273|      93.590|   0.7%/ 98|   0.8%/ 91|   0.8%/ 89|   0.8%/ 88 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 107   |     566|     126.597|   0.8%/ 92|   0.7%/ 95|   0.7%/ 96|   0.7%/ 96 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 109   |    3227|     694.079|   0.4%/174|   0.4%/183|   0.4%/186|   0.4%/189 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  96   |     105|      77.820|   0.3%/249|   0.3%/210|   0.3%/200|   0.4%/191 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 104   |    3206|     530.297|   0.5%/137|   0.4%/171|   0.4%/182|   0.4%/194 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 103   |    8117|    1168.065|   0.4%/185|   0.3%/222|   0.3%/234|   0.3%/247 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 104   |    6183|     619.081|   0.2%/404|   0.2%/435|   0.2%/442|   0.2%/449 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 102   |    1487|     263.645|   0.6%/107|   0.5%/152|   0.4%/169|   0.4%/191 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 104   |    1069|     359.125|   1.1%/ 62|   1.2%/ 60|   1.2%/ 60|   1.2%/ 59 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 104   |    1027|     167.287|   0.7%/ 97|   0.5%/151|   0.4%/177|   0.3%/215 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  96   |      22|      20.992|   1.0%/ 66|   0.9%/ 81|   0.8%/ 87|   0.7%/ 93 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  95   |     277|     143.051|   1.3%/ 53|   0.9%/ 76|   0.8%/ 85|   0.7%/ 96 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 107   |     508|     164.975|   0.5%/131|   0.5%/153|   0.4%/160|   0.4%/167 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 100   |     373|     274.364|   1.0%/ 71|   0.9%/ 79|   0.9%/ 80|   0.8%/ 82 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 113   |   14972|    1685.614|   0.3%/264|   0.2%/390|   0.2%/441|   0.1%/505 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  98   |     502|     239.544|   0.8%/ 87|   0.5%/127|   0.5%/142|   0.4%/163 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 109   |   31576|    1623.171|   0.1%/484|   0.1%/519|   0.1%/528|   0.1%/536 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  98   |    1399|     133.382|   1.1%/ 60|   1.0%/ 70|   0.9%/ 74|   0.9%/ 79 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  96   |      80|     104.358|   0.4%/163|   0.4%/174|   0.4%/179|   0.4%/185 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 103   |    2860|     244.702|   0.7%/106|   0.5%/127|   0.5%/133|   0.5%/140 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 104   |     385|      97.421|   0.5%/141|   0.6%/122|   0.6%/117|   0.6%/113 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 108   |     207|      49.149|   1.0%/ 73|   0.9%/ 80|   0.8%/ 82|   0.8%/ 84 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 104   |    6674|     521.340|   0.4%/172|   0.3%/214|   0.3%/227|   0.3%/242 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 102   |     153|      47.917|   0.3%/205|   0.4%/183|   0.4%/177|   0.4%/171 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  95   |     950|     896.440|   0.7%/103|   0.5%/126|   0.5%/133|   0.5%/141 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 107   |     734|     142.623|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 112   |      92|     104.455|   1.3%/ 52|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 102   |     606|      88.709|   1.5%/ 47|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 106   |    2464|      84.977|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 101   |     174|      54.141|   1.1%/ 62|   0.7%/ 93|   0.6%/107|   0.6%/126 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 103   |      56|      90.119|   0.1%/941|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 109   |    1750|     205.029|   0.8%/ 82|   0.9%/ 74|   1.0%/ 72|   1.0%/ 70 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 123   |    1334|     175.209|   0.5%/128|   0.5%/140|   0.5%/143|   0.5%/147 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  93   |      94|      52.263|   0.4%/162|   0.4%/154|   0.5%/153|   0.5%/153 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 103   |     791|     135.824|   0.7%/ 95|   0.6%/118|   0.6%/125|   0.5%/134 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  79   |      20|      35.041|   0.4%/169|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 101   |     765|      23.745|   3.0%/ 23|   2.7%/ 25|   2.7%/ 26|   2.6%/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 112   |      57|      20.048|   3.4%/ 20|   4.2%/ 16|   4.4%/ 16|   4.6%/ 15 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 111   |     924|      21.491|   1.0%/ 72|   0.8%/ 82|   0.8%/ 85|   0.8%/ 88 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  94   |      12|       0.396|   3.6%/ 19|   3.2%/ 21|   3.2%/ 21|   9.1%/  7 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 115   |    1317|      29.310|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  97   |     458|     154.705|   3.1%/ 22|   2.6%/ 26|   2.5%/ 28|   2.4%/ 29 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 122   |     104|       4.051|   0.1%/508|   0.2%/393|   0.2%/372|   0.2%/354 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 111   |     705|      79.164|   0.2%/292|   0.3%/276|   0.3%/272|   0.3%/269 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 110   |     215|      21.362|   3.7%/ 19|   3.5%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 107   |      91|      58.895|   4.6%/ 15|   3.8%/ 18|   3.5%/ 19|   3.3%/ 21 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 105   |    1861|      11.045|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  92   |     395|      41.960|   1.5%/ 46|   1.4%/ 51|   1.3%/ 52|   1.3%/ 54 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 112   |    9749|     845.971|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  86   |      19|       1.629|   6.3%/ 11|   5.8%/ 12|   5.8%/ 12|   5.8%/ 12 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  94   |    1101|      95.979|   3.9%/ 18|   4.1%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 102   |     182|      55.205|   0.8%/ 91|   0.9%/ 73|   1.0%/ 70|   1.0%/ 66 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  92   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 106   |   60325|     285.343|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 112   |     229|      32.952|   1.6%/ 45|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 105   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  79   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  98   |     331|      12.455|   0.8%/ 85|   0.4%/154|   0.3%/211|   0.2%/351 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 114   |    8696|     228.855|   0.3%/232|   0.2%/352|   0.2%/406|   0.1%/479 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  39   |      48|       8.755|  14.0%/  5|   4.7%/ 15|   3.1%/ 22|   1.7%/ 40 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  64   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 101   |    5902|     308.863|   3.8%/ 18|   3.0%/ 23|   2.8%/ 25|   2.6%/ 26 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 112   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 101   |    3370|      68.233|   4.8%/ 14|   5.0%/ 14|   5.1%/ 14|   5.1%/ 13 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 104   |      14|       2.768|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 104   |     107|      26.270|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 105   |      86|       7.672|   0.2%/435|   0.2%/419|   0.2%/412|   0.2%/405 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 109   |     606|     104.049|   0.1%/820|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 106   |     750|      72.408|   1.4%/ 49|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 109   |    4552|     260.615|   0.9%/ 76|   0.8%/ 85|   0.8%/ 87|   0.8%/ 90 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 115   |    3062|      30.540|   3.8%/ 18|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  92   |     169|      26.093|   5.9%/ 12|   6.9%/ 10|   7.1%/ 10|   7.3%/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  70   |      32|      23.600|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  87   |     103|       1.049|   4.3%/ 16|   4.3%/ 16|   4.4%/ 16|   4.4%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 102   |     328|      59.377|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 137   |   29892|     445.637|   0.1%/909|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 103   |      45|      20.633|   2.2%/ 31|   1.6%/ 43|   1.4%/ 48|   1.2%/ 55 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 100   |       1|       0.426|   4.5%/ 15|   2.5%/ 28|   1.8%/ 38|   1.1%/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  88   |      15|       3.936|   0.6%/126|   1.2%/ 57|   1.4%/ 49|   1.6%/ 43 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 114   |    9000|     108.244|   0.1%/562|   0.1%/679|   0.1%/716|   0.1%/757 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 102   |     122|       4.030|   4.6%/ 15|   4.0%/ 17|   3.8%/ 18|   3.6%/ 19 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 112   |     193|      17.984|   0.2%/340|   0.1%/522|   0.1%/615|   0.1%/754 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 107   |     792|      47.689|   4.6%/ 15|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  77   |      32|       2.602|   1.6%/ 44|   2.2%/ 32|   2.3%/ 30|   2.5%/ 28 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  66   |      24|      15.104|   3.7%/ 18|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  87   |     106|       9.125|   2.3%/ 30|   1.8%/ 39|   1.7%/ 42|   1.6%/ 44 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  97   |     504|      55.012|   3.1%/ 22|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 108   |     585|      59.836|   0.3%/253|   0.3%/265|   0.3%/267|   0.3%/269 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 112   |   18382|      13.504|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 112   |    2881|      10.796|   1.8%/ 38|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 132   |   10729|     128.679|   1.3%/ 55|   1.3%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 119   |    2097|      53.588|   7.5%/  9|   6.9%/ 10|   6.8%/ 10|   6.6%/ 10 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 112   |    1737|     353.004|   0.1%/581|   0.1%/628|   0.1%/635|   0.1%/641 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 102   |     318|      34.665|   0.4%/160|   0.6%/123|   0.6%/116|   0.6%/109 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 131   |   34864|     578.771|   0.1%/951|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 104   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 139   |     979|       7.773|   0.3%/261|   0.3%/274|   0.2%/278|   0.2%/283 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  96   |       9|       0.844|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  98   |     194|      10.367|   5.7%/ 12|   5.6%/ 12|   5.6%/ 12|   5.6%/ 12 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  97   |     150|       3.149|   2.3%/ 30|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  97   |      39|      21.594|   0.1%/889|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  88   |     357|      80.765|   1.1%/ 61|   0.9%/ 76|   0.9%/ 81|   0.8%/ 87 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  89   |      57|       8.734|   4.9%/ 14|   5.8%/ 12|   6.0%/ 11|   6.2%/ 11 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  89   |      30|      15.900|   0.3%/219|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 113   |      34|       4.953|   0.6%/122|   0.6%/113|   0.6%/109|   0.7%/105 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  88   |      35|       7.871|   0.6%/119|   0.7%/ 99|   0.7%/ 94|   0.8%/ 89 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  90   |      24|       3.518|   7.6%/  9|   8.6%/  8|   8.8%/  8|   9.1%/  7 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 102   |      78|      28.095|   0.2%/282|   0.2%/447|   0.1%/516|   0.1%/609 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  45   |      20|       0.757|   3.4%/ 20|   4.9%/ 14|   5.8%/ 12|   6.7%/ 10 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 106   |     121|       3.704|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  94   |     116|       5.736|   0.7%/ 99|   0.5%/133|   0.5%/144|   0.4%/157 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  93   |     132|      32.323|   1.5%/ 47|   1.9%/ 36|   2.2%/ 32|   2.2%/ 32 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 104   |   28654|     226.377|   3.0%/ 23|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 105   |     553|     206.100|   1.8%/ 38|   1.6%/ 43|   1.5%/ 45|   1.5%/ 47 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 113   |     222|       6.178|   0.5%/148|   0.7%/106|   0.7%/ 99|   0.8%/ 92 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  37   |       6|       0.198|   3.0%/ 23|   2.7%/ 25|   4.3%/ 16|   6.0%/ 11 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  46   |      30|       0.990|   2.9%/ 24|   2.8%/ 25|   2.5%/ 28|   2.1%/ 33 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 117   |    6136|     351.492|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  94   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  96   |      80|      12.329|   1.9%/ 36|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  98   |      67|       3.013|   0.1%/946|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 100   |     601|       2.914|   1.9%/ 37|   1.3%/ 51|   1.2%/ 57|   1.1%/ 65 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 101   |     306|     147.517|   3.0%/ 23|   2.7%/ 25|   2.7%/ 26|   2.6%/ 27 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 109   |     251|      46.692|   0.2%/389|   0.2%/453|   0.1%/478|   0.1%/507 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  92   |     174|      37.333|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 104   |    4561|      20.794|   2.8%/ 24|   2.1%/ 32|   1.9%/ 36|   1.8%/ 39 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 112   |     628|     148.824|   2.3%/ 29|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 102   |      15|       2.162|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 103   |    9826|     305.813|   2.4%/ 29|   2.1%/ 33|   2.1%/ 34|   2.0%/ 35 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 150   |    1272|      11.721|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 111   |    1476|      38.451|   0.9%/ 74|   0.8%/ 84|   0.8%/ 87|   0.8%/ 90 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 106   |    1570|     152.747|   0.3%/267|   0.3%/240|   0.3%/233|   0.3%/226 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  95   |     119|      43.162|   2.5%/ 27|   1.7%/ 41|   1.5%/ 47|   1.2%/ 56 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 101   |    1645|      84.771|   1.0%/ 71|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 104   |    9440|      64.327|   1.8%/ 39|   1.5%/ 46|   1.4%/ 48|   1.4%/ 51 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  32   |       2|       0.162|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  99   |    1674|      48.909|   3.3%/ 21|   2.8%/ 24|   2.7%/ 25|   2.6%/ 26 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  91   |     113|       6.960|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 103   |     272|      39.102|   0.5%/131|   0.7%/104|   0.7%/ 98|   0.7%/ 93 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  69   |      61|       7.700|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 102   |      26|       4.571|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  95   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 109   |     110|      52.566|   0.2%/431|   0.3%/253|   0.3%/227|   0.3%/206 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  84   |      91|       5.696|   0.2%/372|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  96   |    2681|      45.621|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 120   |   28631|     607.869|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  95   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 110   |     599|      14.124|   1.4%/ 49|   0.8%/ 86|   0.6%/107|   0.5%/141 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 112   |    5361|     518.579|   0.5%/133|   0.5%/151|   0.4%/156|   0.4%/162 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 118   |    1967|     228.571|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  94   |       9|       0.519|   2.9%/ 24|   3.6%/ 19|   3.9%/ 18|   4.1%/ 17 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  92   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 122   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  96   |      14|       1.872|   0.5%/137|   0.7%/104|   0.7%/ 99|   0.7%/ 95 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  98   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 104   |      50|       4.285|   0.1%/964|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 106   |    5142|      61.834|   0.4%/171|   0.4%/171|   0.4%/172|   0.4%/172 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 123   |  127267|     386.191|   0.6%/116|   0.6%/118|   0.6%/119|   0.6%/119 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 110   |    1176|      28.080|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 103   |     316|      31.967|   0.5%/134|   0.5%/146|   0.5%/149|   0.5%/152 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 112   |   43933|     661.289|   0.3%/239|   0.3%/274|   0.2%/284|   0.2%/296 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  94   |      27|       7.720|   1.0%/ 67|   1.1%/ 61|   1.1%/ 60|   1.2%/ 59 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  96   |      21|       0.612|   1.5%/ 45|   2.7%/ 25|   3.0%/ 23|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  96   |      49|       1.516|   4.5%/ 15|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  90   |      25|       1.371|  17.8%/  4|   6.9%/ 10|   1.6%/ 44|   4.6%/ 15 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 100   |       4|       0.264|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |

