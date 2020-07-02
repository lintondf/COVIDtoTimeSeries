# State and Country COVID-19 Analysis #
## Updated: at 2020-07-02 for data as of 2020-07-01 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 110   |   31715|    1630.296|   0.2%/347|   0.2%/292|   0.2%/279|   0.3%/267 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 114   |   15173|    1708.247|   0.3%/271|   0.2%/382|   0.2%/423|   0.1%/472 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 104   |    8129|    1169.659|   0.3%/208|   0.2%/281|   0.2%/308|   0.2%/341 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 107   |    7010|     553.199|   0.5%/134|   0.4%/185|   0.3%/205|   0.3%/230 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 105   |    6696|     523.064|   0.4%/176|   0.3%/211|   0.3%/222|   0.3%/235 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 105   |    6194|     620.210|   0.2%/395|   0.2%/405|   0.2%/406|   0.2%/407 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 120   |    6172|     156.197|   1.1%/ 64|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 105   |    4341|    1217.457|   0.2%/384|   0.1%/551|   0.1%/617|   0.1%/701 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 116   |    3542|     164.938|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 110   |    3240|     696.870|   0.4%/175|   0.4%/184|   0.4%/187|   0.4%/190 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 124   |  128046|     388.554|   0.6%/117|   0.6%/117|   0.6%/118|   0.6%/118 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 107   |   61290|     289.907|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 113   |   44047|     662.997|   0.3%/243|   0.3%/275|   0.2%/284|   0.2%/295 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 132   |   34879|     579.016|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 138   |   29907|     445.867|   0.1%/909|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 105   |   29307|     231.530|   2.9%/ 24|   2.5%/ 27|   2.4%/ 28|   2.3%/ 29 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 121   |   28652|     608.322|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 113   |   18755|      13.778|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 133   |   10881|     130.497|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 104   |   10019|     311.820|   2.3%/ 30|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  99   |     964|     196.701|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  99   |      14|      19.338|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 103   |    1693|     232.629|   2.1%/ 32|   2.2%/ 31|   2.3%/ 31|   2.3%/ 30 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 100   |     282|      93.322|   2.3%/ 29|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 120   |    6172|     156.197|   1.1%/ 64|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 110   |    1699|     295.062|   0.3%/230|   0.2%/311|   0.2%/340|   0.2%/374 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 105   |    4341|    1217.457|   0.2%/384|   0.1%/551|   0.1%/617|   0.1%/701 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  98   |     527|     541.056|   0.2%/300|   0.1%/801|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 116   |    3542|     164.938|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 112   |    2860|     269.393|   0.7%/ 97|   0.5%/147|   0.4%/168|   0.4%/196 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  93   |      17|      12.007|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  98   |      92|      51.354|   0.3%/213|   0.3%/207|   0.3%/204|   0.3%/199 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 107   |    7010|     553.199|   0.5%/134|   0.4%/185|   0.3%/205|   0.3%/230 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 108   |    2665|     395.891|   0.5%/143|   0.4%/180|   0.4%/193|   0.3%/208 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  99   |     718|     227.703|   0.5%/134|   0.4%/159|   0.4%/166|   0.4%/172 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 111   |     275|      94.428|   0.7%/ 94|   0.8%/ 86|   0.8%/ 84|   0.8%/ 82 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 108   |     570|     127.654|   0.8%/ 91|   0.7%/ 93|   0.7%/ 93|   0.7%/ 93 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 110   |    3240|     696.870|   0.4%/175|   0.4%/184|   0.4%/187|   0.4%/190 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  97   |     105|      78.053|   0.3%/242|   0.3%/205|   0.4%/195|   0.4%/187 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 105   |    3217|     532.193|   0.5%/142|   0.4%/175|   0.4%/186|   0.4%/197 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 104   |    8129|    1169.659|   0.3%/208|   0.2%/281|   0.2%/308|   0.2%/341 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 105   |    6194|     620.210|   0.2%/395|   0.2%/405|   0.2%/406|   0.2%/407 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 103   |    1492|     264.562|   0.6%/112|   0.4%/157|   0.4%/174|   0.4%/194 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 105   |    1082|     363.429|   1.1%/ 60|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 105   |    1030|     167.856|   0.7%/104|   0.4%/167|   0.3%/199|   0.3%/246 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  97   |      23|      21.057|   0.9%/ 75|   0.6%/109|   0.6%/124|   0.5%/145 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  96   |     279|     144.388|   1.2%/ 55|   0.9%/ 76|   0.8%/ 83|   0.7%/ 92 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 108   |     511|     165.879|   0.5%/128|   0.5%/141|   0.5%/145|   0.5%/149 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 101   |     376|     276.437|   0.9%/ 75|   0.8%/ 83|   0.8%/ 86|   0.8%/ 88 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 114   |   15173|    1708.247|   0.3%/271|   0.2%/382|   0.2%/423|   0.1%/472 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  99   |     504|     240.530|   0.7%/ 93|   0.5%/134|   0.5%/150|   0.4%/171 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 110   |   31715|    1630.296|   0.2%/347|   0.2%/292|   0.2%/279|   0.3%/267 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  99   |    1412|     134.654|   1.1%/ 61|   1.0%/ 70|   0.9%/ 74|   0.9%/ 78 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  97   |      80|     104.845|   0.4%/163|   0.4%/177|   0.4%/183|   0.4%/189 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 104   |    2879|     246.275|   0.7%/105|   0.6%/119|   0.6%/123|   0.5%/127 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 105   |     388|      98.000|   0.5%/143|   0.5%/126|   0.6%/122|   0.6%/118 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 109   |     209|      49.548|   0.9%/ 73|   0.9%/ 79|   0.9%/ 81|   0.8%/ 82 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 105   |    6696|     523.064|   0.4%/176|   0.3%/211|   0.3%/222|   0.3%/235 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 103   |     153|      48.044|   0.3%/223|   0.3%/216|   0.3%/213|   0.3%/210 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  96   |     956|     902.306|   0.7%/100|   0.6%/111|   0.6%/114|   0.6%/116 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 108   |     748|     145.276|   1.4%/ 50|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 113   |      93|     105.670|   1.3%/ 55|   1.2%/ 59|   1.1%/ 60|   1.1%/ 61 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 103   |     614|      89.809|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 107   |    2497|      86.123|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 102   |     175|      54.498|   1.1%/ 63|   0.8%/ 90|   0.7%/100|   0.6%/113 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 104   |      56|      90.104|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 110   |    1770|     207.312|   0.9%/ 80|   1.0%/ 71|   1.0%/ 69|   1.0%/ 67 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 124   |    1341|     176.154|   0.6%/125|   0.5%/133|   0.5%/136|   0.5%/138 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  94   |      94|      52.393|   0.4%/176|   0.4%/187|   0.4%/193|   0.3%/202 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 104   |     795|     136.467|   0.7%/101|   0.5%/130|   0.5%/141|   0.5%/154 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  80   |      20|      34.999|   0.4%/196|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 102   |     785|      24.353|   2.9%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 113   |      60|      21.057|   3.7%/ 18|   4.6%/ 15|   4.8%/ 14|   5.0%/ 14 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 112   |     931|      21.650|   0.9%/ 73|   0.8%/ 84|   0.8%/ 87|   0.8%/ 90 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  95   |      13|       0.424|   0.0%/ --|   3.2%/ 21|   9.1%/  7|  10.9%/  6 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 116   |    1354|      30.137|   2.9%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  98   |     467|     157.908|   2.9%/ 23|   2.5%/ 28|   2.3%/ 30|   2.2%/ 32 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 123   |     104|       4.057|   0.1%/552|   0.2%/450|   0.2%/432|   0.2%/417 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 112   |     706|      79.319|   0.2%/303|   0.2%/299|   0.2%/298|   0.2%/298 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 111   |     222|      22.092|   3.7%/ 19|   3.5%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 108   |      94|      61.210|   4.5%/ 15|   3.6%/ 19|   3.4%/ 20|   3.2%/ 22 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 106   |    1904|      11.302|   2.7%/ 25|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  93   |     400|      42.491|   1.5%/ 47|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 113   |    9754|     846.407|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  87   |      20|       1.740|   6.6%/ 10|   6.5%/ 10|   6.6%/ 10|   6.8%/ 10 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  95   |    1156|     100.804|   4.1%/ 17|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 103   |     185|      55.942|   0.9%/ 79|   1.1%/ 62|   1.2%/ 58|   1.2%/ 55 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  93   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 107   |   61290|     289.907|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 113   |     233|      33.463|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44|   1.6%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 106   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  80   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  99   |     327|      12.333|   0.7%/ 96|   0.3%/227|   0.2%/390|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 115   |    8712|     229.260|   0.3%/233|   0.2%/329|   0.2%/367|   0.2%/414 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  40   |      48|       8.814|  11.6%/  6|   3.5%/ 20|   2.4%/ 28|   1.5%/ 47 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  65   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 102   |    6018|     314.972|   3.5%/ 20|   2.6%/ 26|   2.4%/ 28|   2.2%/ 31 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 113   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 102   |    3516|      71.188|   4.6%/ 15|   4.8%/ 14|   4.8%/ 14|   4.9%/ 14 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 105   |      15|       2.945|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 105   |     107|      26.311|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 106   |      86|       7.681|   0.1%/480|   0.1%/499|   0.1%/501|   0.1%/501 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 110   |     606|     104.119|   0.1%/814|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 107   |     759|      73.250|   1.4%/ 50|   1.3%/ 55|   1.2%/ 56|   1.2%/ 58 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 110   |    4589|     262.726|   0.9%/ 75|   0.8%/ 82|   0.8%/ 84|   0.8%/ 86 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 116   |    3157|      31.480|   3.7%/ 19|   3.3%/ 21|   3.3%/ 21|   3.2%/ 22 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  93   |     181|      27.888|   6.0%/ 11|   6.8%/ 10|   7.0%/ 10|   7.2%/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  71   |      32|      23.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  88   |     106|       1.079|   3.9%/ 18|   3.8%/ 18|   3.7%/ 18|   3.7%/ 18 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 103   |     328|      59.395|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 138   |   29907|     445.867|   0.1%/909|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 104   |      45|      20.845|   2.2%/ 31|   1.5%/ 46|   1.3%/ 53|   1.1%/ 63 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 101   |       2|       1.011|   4.2%/ 16|   0.9%/ 79|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  89   |      15|       3.980|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 115   |    9008|     108.336|   0.1%/581|   0.1%/700|   0.1%/737|   0.1%/779 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 103   |     125|       4.134|   4.3%/ 16|   3.4%/ 20|   3.2%/ 22|   2.9%/ 23 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 113   |     193|      17.999|   0.2%/355|   0.1%/567|   0.1%/677|   0.1%/843 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 108   |     826|      49.756|   4.5%/ 15|   4.2%/ 16|   4.1%/ 17|   4.0%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  78   |      33|       2.669|   1.7%/ 41|   2.2%/ 31|   2.4%/ 29|   2.5%/ 27 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  67   |      25|      15.434|   3.8%/ 18|   3.6%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  88   |     108|       9.296|   2.2%/ 31|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  98   |     526|      57.458|   3.3%/ 21|   3.6%/ 19|   3.6%/ 19|   3.7%/ 19 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 109   |     586|      59.977|   0.3%/253|   0.3%/260|   0.3%/260|   0.3%/260 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 113   |   18755|      13.778|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 113   |    2932|      10.985|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 133   |   10881|     130.497|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 120   |    2224|      56.851|   7.2%/  9|   6.5%/ 10|   6.3%/ 11|   6.1%/ 11 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 113   |    1739|     353.357|   0.1%/612|   0.1%/660|   0.1%/670|   0.1%/679 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 103   |     321|      34.885|   0.4%/157|   0.6%/125|   0.6%/119|   0.6%/113 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 132   |   34879|     579.016|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 105   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 140   |     981|       7.790|   0.3%/273|   0.2%/295|   0.2%/303|   0.2%/312 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  97   |       9|       0.844|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  99   |     201|      10.744|   5.3%/ 13|   4.9%/ 14|   4.8%/ 14|   4.7%/ 15 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  98   |     152|       3.197|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  98   |      39|      21.877|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  89   |     360|      81.430|   1.1%/ 63|   0.9%/ 78|   0.8%/ 83|   0.8%/ 89 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  90   |      61|       9.408|   5.4%/ 13|   6.6%/ 10|   6.9%/ 10|   7.3%/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  90   |      30|      15.848|   0.2%/299|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 114   |      34|       4.976|   0.5%/133|   0.6%/126|   0.6%/122|   0.6%/119 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  89   |      36|       8.001|   0.8%/ 88|   1.2%/ 59|   1.3%/ 54|   1.4%/ 50 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  91   |      26|       3.737|  21.6%/  3|   8.5%/  8|  10.1%/  7|   6.0%/ 11 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 103   |      79|      28.110|   0.2%/325|   0.1%/583|   0.1%/723|   0.1%/955 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  46   |      21|       0.817|   3.2%/ 22|   5.6%/ 12|   6.7%/ 10|   7.8%/  9 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 107   |     121|       3.701|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  95   |     117|       5.759|   0.7%/103|   0.5%/135|   0.5%/145|   0.4%/156 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  94   |     135|      33.034|   2.6%/ 26|   1.4%/ 50|   1.1%/ 65|   0.8%/ 91 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 105   |   29307|     231.530|   2.9%/ 24|   2.5%/ 27|   2.4%/ 28|   2.3%/ 29 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 106   |     560|     208.671|   1.7%/ 39|   1.5%/ 46|   1.4%/ 48|   1.4%/ 51 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 114   |     224|       6.238|   0.5%/128|   0.8%/ 91|   0.8%/ 84|   0.9%/ 79 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  38   |       6|       0.204|   1.4%/ 48|   4.0%/ 17|   5.6%/ 12|   7.2%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  47   |      30|       1.006|   3.2%/ 22|   2.6%/ 27|   2.3%/ 30|   2.0%/ 35 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 118   |    6137|     351.574|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  95   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  97   |      82|      12.633|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  99   |      67|       3.011|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 101   |     609|       2.953|   1.9%/ 37|   1.4%/ 50|   1.3%/ 54|   1.2%/ 60 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 102   |     313|     150.704|   2.9%/ 24|   2.6%/ 27|   2.5%/ 27|   2.4%/ 28 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 110   |     251|      46.789|   0.2%/375|   0.2%/415|   0.2%/431|   0.2%/449 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  93   |     181|      38.749|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.5%/ 20 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 105   |    4633|      21.125|   2.7%/ 25|   2.1%/ 34|   1.9%/ 37|   1.7%/ 40 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 113   |     644|     152.560|   2.3%/ 29|   2.5%/ 27|   2.5%/ 27|   2.6%/ 27 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 103   |      16|       2.205|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 104   |   10019|     311.820|   2.3%/ 30|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 151   |    1283|      11.825|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 112   |    1488|      38.764|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 107   |    1575|     153.252|   0.3%/259|   0.3%/232|   0.3%/225|   0.3%/218 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  96   |     120|      43.697|   2.4%/ 29|   1.5%/ 46|   1.3%/ 53|   1.1%/ 65 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 102   |    1662|      85.650|   1.0%/ 70|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 105   |    9579|      65.279|   1.7%/ 40|   1.5%/ 46|   1.4%/ 48|   1.4%/ 50 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  33   |       2|       0.162|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 100   |    1721|      50.306|   3.2%/ 21|   2.8%/ 24|   2.7%/ 25|   2.6%/ 26 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  92   |     117|       7.189|   3.5%/ 20|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 104   |     275|      39.483|   0.6%/111|   0.8%/ 84|   0.9%/ 79|   0.9%/ 75 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  70   |      61|       7.738|   1.3%/ 54|   1.0%/ 70|   0.9%/ 76|   0.8%/ 84 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 103   |      26|       4.566|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  96   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 110   |     110|      52.715|   0.2%/450|   0.2%/281|   0.3%/255|   0.3%/232 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  85   |      90|       5.692|   0.2%/443|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  97   |    2767|      47.085|   3.6%/ 19|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 121   |   28652|     608.322|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  96   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 111   |     606|      14.277|   1.4%/ 50|   0.9%/ 80|   0.7%/ 95|   0.6%/115 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 113   |    5386|     520.964|   0.5%/133|   0.5%/148|   0.5%/153|   0.4%/158 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 119   |    1967|     228.623|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  95   |       9|       0.527|   2.7%/ 26|   3.1%/ 22|   3.2%/ 22|   3.3%/ 21 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  93   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 123   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  97   |      14|       1.881|   0.4%/155|   0.5%/133|   0.5%/131|   0.5%/129 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  99   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 105   |      50|       4.282|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 107   |    5161|      62.065|   0.4%/173|   0.4%/176|   0.4%/177|   0.4%/179 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 124   |  128046|     388.554|   0.6%/117|   0.6%/117|   0.6%/118|   0.6%/118 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 111   |    1194|      28.504|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 104   |     317|      32.095|   0.5%/140|   0.4%/156|   0.4%/161|   0.4%/167 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 113   |   44047|     662.997|   0.3%/243|   0.3%/275|   0.2%/284|   0.2%/295 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  95   |      28|       7.836|   1.1%/ 66|   1.2%/ 60|   1.2%/ 59|   1.2%/ 58 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  97   |      21|       0.622|   2.1%/ 32|   3.7%/ 18|   4.2%/ 17|   4.6%/ 15 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  97   |      52|       1.608|   4.8%/ 14|   5.5%/ 13|   5.6%/ 12|   5.8%/ 12 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  91   |      27|       1.514|  17.8%/  4|   1.6%/ 44|   4.6%/ 15|  10.9%/  6 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 101   |       4|       0.264|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |

