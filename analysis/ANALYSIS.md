# State and Country COVID-19 Analysis #
## Updated: at 2020-07-03 for data as of 2020-07-02 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 111   |   31849|    1637.181|   0.3%/253|   0.4%/195|   0.4%/184|   0.4%/173 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 115   |   15336|    1726.559|   0.3%/274|   0.2%/367|   0.2%/399|   0.2%/436 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 105   |    8149|    1172.644|   0.3%/225|   0.2%/316|   0.2%/352|   0.2%/399 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 108   |    7029|     554.706|   0.5%/144|   0.3%/208|   0.3%/234|   0.3%/267 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 106   |    6719|     524.870|   0.4%/174|   0.4%/198|   0.3%/204|   0.3%/211 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 121   |    6243|     158.000|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 106   |    6206|     621.420|   0.2%/376|   0.2%/363|   0.2%/359|   0.2%/354 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 106   |    4343|    1218.194|   0.2%/424|   0.1%/643|   0.1%/739|   0.1%/871 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 117   |    3589|     167.098|   1.2%/ 59|   1.2%/ 58|   1.2%/ 58|   1.2%/ 57 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 111   |    3253|     699.824|   0.4%/168|   0.4%/170|   0.4%/171|   0.4%/172 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 125   |  128811|     390.877|   0.6%/115|   0.6%/114|   0.6%/114|   0.6%/114 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 108   |   62363|     294.983|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 114   |   44154|     664.617|   0.3%/243|   0.3%/267|   0.3%/274|   0.2%/281 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 133   |   34888|     579.158|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 139   |   29921|     446.082|   0.1%/934|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 106   |   29949|     236.605|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 31 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 122   |   28660|     608.488|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 114   |   19096|      14.029|   2.7%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 134   |   11035|     132.347|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 105   |   10197|     317.367|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 100   |     979|     199.697|   1.4%/ 50|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 100   |      14|      19.488|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 104   |    1737|     238.691|   2.3%/ 31|   2.4%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 101   |     286|      94.775|   2.3%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 121   |    6243|     158.000|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 111   |    1703|     295.721|   0.3%/228|   0.2%/287|   0.2%/305|   0.2%/325 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 106   |    4343|    1218.194|   0.2%/424|   0.1%/643|   0.1%/739|   0.1%/871 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  99   |     529|     543.322|   0.2%/319|   0.1%/758|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 117   |    3589|     167.098|   1.2%/ 59|   1.2%/ 58|   1.2%/ 58|   1.2%/ 57 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 113   |    2872|     270.537|   0.7%/ 99|   0.5%/140|   0.4%/156|   0.4%/176 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  94   |      17|      12.007|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  99   |      92|      51.507|   0.3%/211|   0.3%/202|   0.4%/198|   0.4%/193 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 108   |    7029|     554.706|   0.5%/144|   0.3%/208|   0.3%/234|   0.3%/267 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 109   |    2674|     397.229|   0.5%/146|   0.4%/180|   0.4%/191|   0.3%/204 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 100   |     721|     228.624|   0.5%/140|   0.4%/163|   0.4%/169|   0.4%/175 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 112   |     278|      95.295|   0.8%/ 92|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 109   |     576|     128.907|   0.8%/ 86|   0.8%/ 83|   0.8%/ 82|   0.8%/ 82 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 111   |    3253|     699.824|   0.4%/168|   0.4%/170|   0.4%/171|   0.4%/172 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  98   |     105|      78.239|   0.3%/262|   0.3%/240|   0.3%/234|   0.3%/228 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 106   |    3228|     533.903|   0.5%/147|   0.4%/179|   0.4%/189|   0.3%/199 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 105   |    8149|    1172.644|   0.3%/225|   0.2%/316|   0.2%/352|   0.2%/399 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 106   |    6206|     621.420|   0.2%/376|   0.2%/363|   0.2%/359|   0.2%/354 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 104   |    1500|     265.958|   0.6%/116|   0.5%/154|   0.4%/166|   0.4%/181 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 106   |    1094|     367.599|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58|   1.2%/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 106   |    1038|     169.127|   0.7%/ 99|   0.5%/134|   0.5%/147|   0.4%/162 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  98   |      23|      21.088|   0.8%/ 85|   0.5%/151|   0.4%/190|   0.3%/259 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  97   |     282|     145.900|   1.2%/ 56|   1.0%/ 69|   1.0%/ 73|   0.9%/ 77 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 109   |     516|     167.416|   0.6%/114|   0.6%/111|   0.6%/110|   0.6%/109 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 102   |     379|     278.389|   0.9%/ 77|   0.8%/ 85|   0.8%/ 87|   0.8%/ 90 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 115   |   15336|    1726.559|   0.3%/274|   0.2%/367|   0.2%/399|   0.2%/436 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 100   |     507|     241.790|   0.7%/ 96|   0.5%/133|   0.5%/147|   0.4%/164 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 111   |   31849|    1637.181|   0.3%/253|   0.4%/195|   0.4%/184|   0.4%/173 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 100   |    1425|     135.873|   1.1%/ 61|   1.0%/ 69|   1.0%/ 72|   0.9%/ 75 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  98   |      80|     105.218|   0.4%/163|   0.4%/181|   0.4%/188|   0.4%/195 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 105   |    2892|     247.423|   0.7%/106|   0.6%/116|   0.6%/119|   0.6%/122 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 106   |     391|      98.786|   0.5%/132|   0.6%/112|   0.6%/107|   0.7%/104 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 110   |     211|      49.912|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 106   |    6719|     524.870|   0.4%/174|   0.4%/198|   0.3%/204|   0.3%/211 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 104   |     154|      48.138|   0.3%/245|   0.3%/253|   0.3%/255|   0.3%/258 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  97   |     961|     906.981|   0.7%/104|   0.6%/117|   0.6%/120|   0.6%/123 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 109   |     764|     148.301|   1.5%/ 45|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 114   |      95|     107.540|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 104   |     622|      91.055|   1.4%/ 48|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 108   |    2532|      87.330|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 103   |     176|      54.967|   1.1%/ 63|   0.9%/ 80|   0.8%/ 86|   0.8%/ 92 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 105   |      56|      90.058|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 111   |    1792|     209.917|   0.9%/ 74|   1.1%/ 65|   1.1%/ 63|   1.1%/ 61 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 125   |    1348|     176.963|   0.6%/126|   0.5%/134|   0.5%/136|   0.5%/138 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  95   |      94|      52.474|   0.4%/195|   0.3%/235|   0.3%/253|   0.2%/279 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 105   |     798|     137.116|   0.7%/103|   0.5%/130|   0.5%/139|   0.5%/150 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  81   |      20|      34.840|   0.3%/255|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 103   |     807|      25.057|   2.9%/ 24|   2.7%/ 25|   2.7%/ 26|   2.6%/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 114   |      63|      22.199|   4.0%/ 17|   4.9%/ 14|   5.2%/ 13|   5.4%/ 13 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 113   |     938|      21.809|   0.9%/ 74|   0.8%/ 85|   0.8%/ 89|   0.7%/ 93 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  96   |      13|       0.406|   0.0%/ --|   9.1%/  7|  10.9%/  6|  15.6%/  4 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 117   |    1391|      30.953|   2.8%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  99   |     475|     160.770|   2.8%/ 25|   2.3%/ 30|   2.2%/ 32|   2.0%/ 34 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 124   |     104|       4.060|   0.1%/600|   0.1%/524|   0.1%/513|   0.1%/504 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 113   |     707|      79.443|   0.2%/322|   0.2%/335|   0.2%/340|   0.2%/344 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 112   |     230|      22.861|   3.6%/ 19|   3.5%/ 20|   3.5%/ 20|   3.4%/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 109   |      97|      63.075|   4.3%/ 16|   3.5%/ 19|   3.4%/ 21|   3.2%/ 22 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 107   |    1947|      11.556|   2.7%/ 26|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  94   |     405|      43.069|   1.5%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 114   |    9760|     846.879|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  88   |      21|       1.820|   6.2%/ 11|   6.3%/ 11|   6.4%/ 11|   6.6%/ 10 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  96   |    1217|     106.086|   4.3%/ 16|   4.8%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 104   |     187|      56.585|   0.9%/ 77|   1.1%/ 62|   1.2%/ 59|   1.2%/ 56 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  94   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 108   |   62363|     294.983|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 114   |     235|      33.873|   1.6%/ 44|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 107   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  81   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 100   |     327|      12.304|   0.6%/109|   0.1%/562|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 116   |    8732|     229.792|   0.3%/240|   0.2%/329|   0.2%/362|   0.2%/400 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  41   |      48|       8.771|   8.3%/  8|   2.4%/ 29|   1.4%/ 50|   0.3%/216 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  66   |      74|       4.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 103   |    6138|     321.217|   3.3%/ 21|   2.4%/ 28|   2.2%/ 31|   2.0%/ 34 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 114   |    4642|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 103   |    3670|      74.292|   4.3%/ 16|   4.3%/ 16|   4.3%/ 16|   4.3%/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 106   |      16|       3.143|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 106   |     108|      26.433|   0.1%/689|   0.2%/417|   0.2%/374|   0.2%/337 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 107   |      86|       7.688|   0.1%/536|   0.1%/605|   0.1%/621|   0.1%/639 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 111   |     607|     104.175|   0.1%/856|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 108   |     768|      74.183|   1.4%/ 50|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 111   |    4631|     265.114|   0.9%/ 75|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 117   |    3245|      32.360|   3.6%/ 19|   3.2%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  94   |     192|      29.674|   6.0%/ 11|   6.6%/ 10|   6.7%/ 10|   6.8%/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  72   |      32|      23.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  89   |     109|       1.101|   3.4%/ 20|   3.0%/ 23|   2.8%/ 24|   2.7%/ 25 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 104   |     328|      59.408|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 139   |   29921|     446.082|   0.1%/934|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 105   |      45|      20.832|   2.0%/ 35|   1.1%/ 66|   0.8%/ 87|   0.5%/127 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 102   |       2|       1.000|   3.6%/ 19|   0.1%/513|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  90   |      15|       4.017|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 116   |    9017|     108.443|   0.1%/593|   0.1%/702|   0.1%/736|   0.1%/774 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 104   |     128|       4.224|   3.9%/ 17|   2.8%/ 24|   2.5%/ 27|   2.2%/ 31 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 114   |     193|      18.007|   0.2%/372|   0.1%/607|   0.1%/729|   0.1%/912 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 109   |     859|      51.745|   4.4%/ 16|   4.2%/ 16|   4.1%/ 17|   4.0%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  79   |      33|       2.719|   1.8%/ 39|   2.3%/ 31|   2.4%/ 29|   2.5%/ 28 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  68   |      25|      15.651|   3.6%/ 19|   2.8%/ 25|   2.5%/ 27|   2.3%/ 30 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  89   |     110|       9.477|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  99   |     553|      60.331|   3.7%/ 19|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 110   |     587|      60.112|   0.3%/268|   0.2%/284|   0.2%/287|   0.2%/289 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 114   |   19096|      14.029|   2.7%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 114   |    2984|      11.179|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 134   |   11035|     132.347|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 121   |    2349|      60.036|   7.0%/ 10|   6.2%/ 11|   6.0%/ 11|   5.8%/ 12 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 114   |    1740|     353.649|   0.1%/642|   0.1%/695|   0.1%/709|   0.1%/724 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 104   |     322|      35.085|   0.5%/151|   0.6%/123|   0.6%/117|   0.6%/112 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 133   |   34888|     579.158|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 106   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 141   |     983|       7.805|   0.2%/283|   0.2%/314|   0.2%/325|   0.2%/338 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  98   |       9|       0.844|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 100   |     207|      11.089|   4.8%/ 14|   3.9%/ 18|   3.7%/ 19|   3.4%/ 20 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  99   |     154|       3.247|   2.1%/ 32|   1.8%/ 38|   1.7%/ 40|   1.7%/ 42 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  99   |      54|      30.076|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  90   |     362|      81.968|   1.1%/ 65|   0.9%/ 81|   0.8%/ 86|   0.8%/ 92 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  91   |      67|      10.254|   6.0%/ 11|   7.4%/  9|   7.8%/  9|   8.2%/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  91   |      30|      15.805|   0.2%/408|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 115   |      34|       5.024|   0.6%/122|   0.6%/109|   0.7%/106|   0.7%/102 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  90   |      36|       8.120|   0.8%/ 84|   1.2%/ 58|   1.3%/ 54|   1.4%/ 49 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  92   |      27|       3.922|   1.9%/ 36|  10.1%/  7|   6.0%/ 11|   4.2%/ 16 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 104   |      79|      28.125|   0.2%/372|   0.1%/726|   0.1%/962|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  47   |      23|       0.891|   3.3%/ 21|   6.1%/ 11|   6.9%/ 10|   7.7%/  9 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 108   |     121|       3.700|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  96   |     117|       5.792|   0.6%/107|   0.5%/131|   0.5%/138|   0.5%/146 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  95   |     137|      33.670|   2.1%/ 33|   0.9%/ 81|   0.6%/126|   0.3%/276 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 106   |   29949|     236.605|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 31 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 107   |     567|     211.426|   1.7%/ 41|   1.5%/ 47|   1.4%/ 50|   1.3%/ 52 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 115   |     226|       6.299|   0.6%/123|   0.8%/ 91|   0.8%/ 85|   0.9%/ 79 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  39   |       6|       0.207|   0.6%/125|   3.7%/ 19|   4.2%/ 16|   4.5%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  48   |      31|       1.032|   3.3%/ 21|   2.4%/ 29|   2.1%/ 33|   1.7%/ 40 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 119   |    6138|     351.633|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  96   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  98   |      83|      12.876|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 100   |      67|       3.019|   0.1%/848|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 102   |     618|       2.996|   1.9%/ 37|   1.5%/ 46|   1.4%/ 49|   1.3%/ 52 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 103   |     321|     154.671|   2.8%/ 24|   2.5%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 111   |     252|      46.864|   0.2%/362|   0.2%/385|   0.2%/394|   0.2%/404 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  94   |     187|      40.079|   3.4%/ 20|   3.5%/ 20|   3.5%/ 19|   3.6%/ 19 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 106   |    4703|      21.440|   2.6%/ 27|   1.9%/ 36|   1.8%/ 39|   1.6%/ 43 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 114   |     661|     156.664|   2.4%/ 29|   2.5%/ 27|   2.5%/ 27|   2.6%/ 27 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 104   |      17|       2.309|   3.2%/ 22|   4.7%/ 14|   5.2%/ 13|   5.6%/ 12 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 105   |   10197|     317.367|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 152   |    1293|      11.916|   0.9%/ 74|   0.9%/ 77|   0.9%/ 77|   0.9%/ 78 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 113   |    1500|      39.075|   0.9%/ 75|   0.8%/ 82|   0.8%/ 84|   0.8%/ 87 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 108   |    1581|     153.803|   0.3%/245|   0.3%/212|   0.3%/205|   0.4%/198 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  97   |     121|      44.163|   2.2%/ 31|   1.4%/ 51|   1.2%/ 60|   0.9%/ 73 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 103   |    1680|      86.575|   1.0%/ 69|   1.0%/ 67|   1.0%/ 66|   1.1%/ 66 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 106   |    9721|      66.241|   1.7%/ 40|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  34   |       3|       0.253|   0.0%/ --|   0.0%/ --|  14.5%/  5|  14.5%/  5 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 101   |    1768|      51.667|   3.2%/ 22|   2.8%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  93   |     120|       7.426|   3.5%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 105   |     278|      39.934|   0.7%/ 94|   1.0%/ 70|   1.1%/ 66|   1.1%/ 61 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  71   |      61|       7.754|   1.1%/ 62|   0.7%/101|   0.6%/122|   0.4%/156 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 104   |      26|       4.566|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  97   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 111   |     111|      52.845|   0.1%/490|   0.2%/328|   0.2%/301|   0.2%/278 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  86   |      90|       5.687|   0.1%/526|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  98   |    2858|      48.620|   3.6%/ 19|   3.4%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 122   |   28660|     608.488|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  97   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 112   |     613|      14.434|   1.4%/ 50|   0.9%/ 73|   0.8%/ 83|   0.7%/ 94 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 114   |    5413|     523.622|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/149 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 120   |    1968|     228.697|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  96   |       9|       0.532|   2.5%/ 28|   2.6%/ 27|   2.6%/ 26|   2.6%/ 26 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  94   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 124   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  98   |      14|       1.887|   0.4%/194|   0.4%/194|   0.3%/200|   0.3%/209 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 100   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 106   |      50|       4.279|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 108   |    5179|      62.284|   0.4%/176|   0.4%/182|   0.4%/185|   0.4%/187 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 125   |  128811|     390.877|   0.6%/115|   0.6%/114|   0.6%/114|   0.6%/114 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 112   |    1211|      28.912|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 105   |     319|      32.208|   0.5%/146|   0.4%/168|   0.4%/175|   0.4%/182 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 114   |   44154|     664.617|   0.3%/243|   0.3%/267|   0.3%/274|   0.2%/281 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  96   |      28|       7.927|   1.1%/ 64|   1.2%/ 60|   1.2%/ 59|   1.2%/ 58 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  98   |      24|       0.703|   2.6%/ 26|   4.4%/ 16|   4.9%/ 14|   5.4%/ 13 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  98   |      55|       1.705|   5.0%/ 14|   5.6%/ 12|   5.8%/ 12|   5.9%/ 12 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  92   |      29|       1.633|   5.3%/ 13|   4.6%/ 15|  10.9%/  6|  10.9%/  6 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 102   |       4|       0.264|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |

