# State and Country COVID-19 Analysis #
## Updated: 2020-06-29 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 107   |   31439|    1616.088|   0.1%/487|   0.1%/579|   0.1%/606|   0.1%/635 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 111   |   14451|    1626.933|   0.3%/236|   0.2%/353|   0.2%/402|   0.1%/467 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 101   |    8076|    1162.136|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/192 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 104   |    6947|     548.212|   0.6%/107|   0.5%/133|   0.5%/141|   0.5%/150 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 102   |    6635|     518.295|   0.5%/151|   0.4%/174|   0.4%/180|   0.4%/187 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 102   |    6162|     617.021|   0.2%/399|   0.2%/460|   0.1%/477|   0.1%/493 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 117   |    5991|     151.613|   1.1%/ 61|   1.1%/ 65|   1.0%/ 67|   1.0%/ 68 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 102   |    4327|    1213.548|   0.2%/299|   0.2%/387|   0.2%/414|   0.2%/444 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 113   |    3427|     159.552|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 107   |    3204|     689.305|   0.4%/159|   0.4%/155|   0.4%/154|   0.5%/153 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 121   |  125795|     381.723|   0.6%/109|   0.6%/107|   0.7%/106|   0.7%/105 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 104   |   58457|     276.507|   2.1%/ 33|   1.9%/ 36|   1.9%/ 37|   1.8%/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 110   |   43731|     658.241|   0.3%/212|   0.3%/228|   0.3%/231|   0.3%/235 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 129   |   34851|     578.555|   0.1%/799|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 135   |   29857|     445.125|   0.1%/822|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 118   |   28563|     606.435|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 102   |   27316|     215.808|   3.3%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 110   |   17487|      12.847|   2.9%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 130   |   10441|     125.227|   1.2%/ 57|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 110   |    9742|     845.311|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  96   |     925|     188.681|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  96   |      12|      16.687|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 100   |    1584|     217.557|   2.2%/ 31|   2.4%/ 28|   2.5%/ 28|   2.6%/ 27 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  97   |     266|      88.179|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 117   |    5991|     151.613|   1.1%/ 61|   1.1%/ 65|   1.0%/ 67|   1.0%/ 68 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 107   |    1689|     293.279|   0.3%/206|   0.2%/312|   0.2%/359|   0.2%/422 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 102   |    4327|    1213.548|   0.2%/299|   0.2%/387|   0.2%/414|   0.2%/444 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  95   |     514|     528.307|   0.3%/214|   0.1%/471|   0.1%/672|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 113   |    3427|     159.552|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 109   |    2826|     266.165|   0.9%/ 75|   0.7%/101|   0.6%/110|   0.6%/121 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  90   |      17|      12.007|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  95   |      91|      50.819|   0.3%/212|   0.3%/260|   0.3%/272|   0.2%/283 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 104   |    6947|     548.212|   0.6%/107|   0.5%/133|   0.5%/141|   0.5%/150 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 105   |    2637|     391.765|   0.6%/124|   0.5%/149|   0.4%/157|   0.4%/166 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  96   |     710|     224.979|   0.6%/121|   0.4%/161|   0.4%/174|   0.4%/189 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 108   |     268|      92.084|   0.7%/103|   0.7%/ 97|   0.7%/ 96|   0.7%/ 95 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 105   |     558|     124.850|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86|   0.8%/ 86 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 107   |    3204|     689.305|   0.4%/159|   0.4%/155|   0.4%/154|   0.5%/153 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  94   |     104|      77.201|   0.2%/299|   0.2%/281|   0.3%/276|   0.3%/271 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 102   |    3182|     526.390|   0.6%/123|   0.5%/152|   0.4%/160|   0.4%/170 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 101   |    8076|    1162.136|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/192 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 102   |    6162|     617.021|   0.2%/399|   0.2%/460|   0.1%/477|   0.1%/493 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 100   |    1476|     261.763|   0.7%/ 96|   0.5%/149|   0.4%/172|   0.3%/203 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 102   |    1043|     350.427|   1.1%/ 63|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 102   |    1020|     166.231|   0.9%/ 79|   0.7%/ 99|   0.6%/107|   0.6%/116 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  94   |      22|      20.731|   1.3%/ 54|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  93   |     273|     140.956|   1.5%/ 45|   1.2%/ 60|   1.1%/ 65|   1.0%/ 71 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 105   |     504|     163.535|   0.6%/123|   0.5%/142|   0.5%/148|   0.4%/154 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  98   |     367|     269.970|   1.1%/ 61|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 111   |   14451|    1626.933|   0.3%/236|   0.2%/353|   0.2%/402|   0.1%/467 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  96   |     498|     237.632|   0.9%/ 74|   0.7%/ 95|   0.7%/103|   0.6%/111 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 107   |   31439|    1616.088|   0.1%/487|   0.1%/579|   0.1%/606|   0.1%/635 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  96   |    1375|     131.070|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  94   |      79|     103.698|   0.4%/162|   0.4%/171|   0.4%/175|   0.4%/180 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 101   |    2831|     242.179|   0.7%/ 99|   0.6%/117|   0.6%/123|   0.5%/130 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 102   |     381|      96.307|   0.5%/146|   0.6%/123|   0.6%/117|   0.6%/112 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 106   |     204|      48.308|   1.0%/ 66|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 102   |    6635|     518.295|   0.5%/151|   0.4%/174|   0.4%/180|   0.4%/187 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 100   |     152|      47.575|   0.3%/207|   0.4%/189|   0.4%/183|   0.4%/177 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  93   |     938|     885.775|   0.7%/ 99|   0.5%/137|   0.5%/152|   0.4%/170 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 105   |     715|     138.845|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 110   |      90|     102.181|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 100   |     591|      86.458|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 104   |    2407|      83.015|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  99   |     171|      53.427|   1.3%/ 54|   0.9%/ 75|   0.8%/ 84|   0.7%/ 96 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 101   |      56|      90.146|   0.1%/726|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 107   |    1717|     201.146|   0.8%/ 82|   1.0%/ 73|   1.0%/ 70|   1.0%/ 68 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 121   |    1321|     173.498|   0.6%/123|   0.5%/132|   0.5%/135|   0.5%/139 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  91   |      93|      51.876|   0.5%/146|   0.5%/130|   0.6%/125|   0.6%/120 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 101   |     783|     134.534|   0.8%/ 85|   0.7%/ 96|   0.7%/ 99|   0.7%/103 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  77   |      20|      35.350|   0.5%/137|   0.2%/395|   0.1%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  99   |     728|      22.595|   3.2%/ 21|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 110   |      53|      18.488|   2.9%/ 24|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 109   |     910|      21.153|   1.0%/ 66|   1.0%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  92   |      11|       0.353|   7.7%/  9|   0.0%/ --|   0.0%/ --|   3.2%/ 21 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 113   |    1248|      27.782|   2.9%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  95   |     437|     147.766|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 120   |     104|       4.036|   0.2%/443|   0.2%/310|   0.2%/287|   0.3%/267 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 109   |     701|      78.771|   0.2%/296|   0.3%/271|   0.3%/266|   0.3%/261 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 108   |     201|      19.946|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 105   |      86|      55.445|   4.9%/ 14|   3.9%/ 18|   3.6%/ 19|   3.4%/ 20 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 103   |    1775|      10.539|   2.9%/ 24|   2.4%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  90   |     385|      40.905|   1.6%/ 44|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 110   |    9742|     845.311|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  84   |      16|       1.401|   6.1%/ 11|   2.5%/ 28|   1.6%/ 43|   0.7%/ 95 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  92   |    1011|      88.175|   3.7%/ 18|   3.7%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 100   |     178|      53.914|   0.6%/110|   0.7%/ 96|   0.7%/ 93|   0.8%/ 89 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  90   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 104   |   58457|     276.507|   2.1%/ 33|   1.9%/ 36|   1.9%/ 37|   1.8%/ 37 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 110   |     222|      31.955|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 103   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  77   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  96   |     335|      12.630|   1.0%/ 73|   0.9%/ 75|   0.9%/ 78|   0.8%/ 82 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 112   |    8668|     228.109|   0.3%/210|   0.2%/330|   0.2%/386|   0.1%/466 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  37   |      46|       8.391|  13.5%/  5|   8.3%/  8|   4.9%/ 14|   1.7%/ 40 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  62   |      74|       4.556|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  99   |    5605|     293.319|   4.2%/ 17|   3.4%/ 20|   3.2%/ 22|   3.0%/ 23 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 110   |    4641|       3.309|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  99   |    3066|      62.078|   5.2%/ 13|   5.9%/ 12|   6.1%/ 11|   6.2%/ 11 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 102   |      12|       2.423|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 102   |     107|      26.287|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 103   |      86|       7.648|   0.2%/459|   0.2%/449|   0.2%/447|   0.2%/444 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 107   |     605|     103.921|   0.1%/725|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 104   |     732|      70.690|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 107   |    4478|     256.354|   1.0%/ 72|   0.9%/ 77|   0.9%/ 79|   0.9%/ 81 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 113   |    2870|      28.619|   4.0%/ 17|   3.9%/ 18|   3.9%/ 18|   3.8%/ 18 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  90   |     147|      22.721|   5.4%/ 13|   6.5%/ 11|   6.7%/ 10|   7.0%/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  68   |      32|      23.559|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  85   |      95|       0.966|   4.4%/ 16|   4.4%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 100   |     328|      59.329|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 135   |   29857|     445.125|   0.1%/822|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 101   |      44|      20.351|   2.5%/ 28|   2.0%/ 35|   1.8%/ 38|   1.6%/ 42 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  98   |       1|       0.426|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  86   |      14|       3.826|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 112   |    8984|     108.048|   0.1%/494|   0.1%/564|   0.1%/584|   0.1%/604 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 100   |     114|       3.771|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14|   4.9%/ 14 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 110   |     192|      17.949|   0.2%/287|   0.2%/374|   0.2%/411|   0.2%/460 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 105   |     732|      44.105|   4.9%/ 14|   4.7%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  75   |      30|       2.482|   1.4%/ 49|   1.6%/ 43|   1.7%/ 41|   1.7%/ 40 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  64   |      22|      13.949|   3.3%/ 21|   4.3%/ 16|   4.5%/ 15|   4.7%/ 15 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  85   |     102|       8.804|   2.5%/ 27|   1.7%/ 40|   1.6%/ 44|   1.4%/ 49 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  95   |     476|      51.948|   3.4%/ 20|   4.0%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 106   |     581|      59.491|   0.3%/272|   0.2%/333|   0.2%/351|   0.2%/372 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 110   |   17487|      12.847|   2.9%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 110   |    2788|      10.445|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 130   |   10441|     125.227|   1.2%/ 57|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 117   |    1844|      47.128|   8.0%/  8|   7.7%/  9|   7.6%/  9|   7.5%/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 110   |    1734|     352.269|   0.1%/526|   0.1%/559|   0.1%/562|   0.1%/561 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 100   |     315|      34.231|   0.4%/172|   0.6%/124|   0.6%/115|   0.6%/107 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 129   |   34851|     578.555|   0.1%/799|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 102   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 137   |     975|       7.739|   0.3%/222|   0.3%/214|   0.3%/212|   0.3%/211 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  94   |       9|       0.844|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  96   |     174|       9.334|   5.7%/ 12|   5.6%/ 12|   5.6%/ 12|   5.5%/ 12 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  95   |     144|       3.036|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  95   |      38|      21.052|   0.2%/399|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  86   |     351|      79.480|   1.2%/ 56|   1.0%/ 69|   0.9%/ 74|   0.9%/ 79 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  87   |      50|       7.651|   4.1%/ 17|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  87   |      30|      15.981|   0.5%/135|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 111   |      33|       4.891|   0.5%/147|   0.4%/190|   0.3%/200|   0.3%/209 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  86   |      34|       7.677|   0.4%/172|   0.1%/521|   0.1%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  88   |      21|       3.040|   0.0%/ --|   1.9%/ 36|   0.0%/ --|   5.3%/ 13 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 100   |      78|      28.045|   0.3%/215|   0.2%/301|   0.2%/327|   0.2%/356 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  43   |      17|       0.657|   3.7%/ 18|   2.6%/ 26|   2.3%/ 30|   1.9%/ 37 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 104   |     122|       3.712|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  92   |     115|       5.683|   0.8%/ 90|   0.4%/157|   0.4%/190|   0.3%/240 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  91   |     127|      31.246|   2.8%/ 25|   1.7%/ 40|   1.5%/ 46|   1.2%/ 56 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 102   |   27316|     215.808|   3.3%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 103   |     537|     200.106|   2.0%/ 35|   1.7%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 111   |     219|       6.092|   0.3%/226|   0.4%/177|   0.4%/167|   0.4%/157 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  35   |       5|       0.166|   5.0%/ 14|   0.5%/127|   0.0%/ --|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  44   |      28|       0.949|   2.6%/ 26|   3.5%/ 19|   3.9%/ 18|   4.2%/ 17 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 115   |    6132|     351.277|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  92   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  94   |      77|      11.880|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  96   |      67|       3.019|   0.1%/622|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  98   |     587|       2.846|   2.1%/ 33|   1.5%/ 46|   1.4%/ 51|   1.2%/ 58 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  99   |     290|     139.851|   3.0%/ 23|   2.7%/ 25|   2.6%/ 26|   2.5%/ 27 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 107   |     250|      46.561|   0.2%/332|   0.2%/340|   0.2%/342|   0.2%/345 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  90   |     163|      34.996|   3.3%/ 21|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 102   |    4398|      20.051|   3.1%/ 22|   2.4%/ 29|   2.2%/ 31|   2.0%/ 35 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 110   |     597|     141.487|   2.3%/ 30|   2.5%/ 27|   2.6%/ 27|   2.7%/ 26 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 100   |      14|       2.000|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 101   |    9456|     294.293|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31|   2.1%/ 32 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 148   |    1247|      11.490|   1.0%/ 67|   1.1%/ 65|   1.1%/ 64|   1.1%/ 64 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 109   |    1454|      37.885|   1.0%/ 66|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 104   |    1560|     151.798|   0.2%/279|   0.3%/271|   0.3%/266|   0.3%/261 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  93   |     116|      42.140|   3.0%/ 23|   2.3%/ 30|   2.1%/ 33|   1.9%/ 36 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  99   |    1611|      83.030|   0.9%/ 75|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 102   |    9181|      62.567|   1.9%/ 36|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  30   |       2|       0.162|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  97   |    1590|      46.462|   3.4%/ 20|   3.0%/ 23|   2.9%/ 24|   2.7%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  89   |     107|       6.580|   3.7%/ 18|   3.2%/ 21|   3.1%/ 22|   3.0%/ 23 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 101   |     268|      38.467|   0.4%/180|   0.4%/164|   0.4%/161|   0.4%/157 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  67   |      60|       7.542|   1.2%/ 58|   1.8%/ 38|   2.0%/ 35|   2.1%/ 32 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 100   |      26|       4.584|   0.1%/778|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  93   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 107   |     109|      52.231|   0.0%/ ***|   0.1%/842|   0.1%/752|   0.1%/676 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  82   |      91|       5.698|   0.3%/267|   0.1%/619|   0.1%/929|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  94   |    2525|      42.956|   3.8%/ 18|   3.3%/ 21|   3.2%/ 21|   3.1%/ 22 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 118   |   28563|     606.435|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  93   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 108   |     595|      14.016|   1.8%/ 38|   1.3%/ 52|   1.2%/ 57|   1.1%/ 63 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 110   |    5315|     514.058|   0.6%/118|   0.6%/125|   0.5%/126|   0.5%/128 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 116   |    1966|     228.511|   0.1%/946|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  92   |       8|       0.439|   2.7%/ 25|   4.1%/ 17|   4.4%/ 16|   4.8%/ 14 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  90   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 120   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  94   |      14|       1.847|   0.6%/114|   1.0%/ 71|   1.1%/ 64|   1.2%/ 59 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  96   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 102   |      50|       4.287|   0.1%/709|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 104   |    5101|      61.348|   0.4%/164|   0.4%/157|   0.4%/155|   0.5%/154 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 121   |  125795|     381.723|   0.6%/109|   0.6%/107|   0.7%/106|   0.7%/105 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 108   |    1138|      27.182|   1.7%/ 41|   1.7%/ 42|   1.7%/ 42|   1.6%/ 42 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 101   |     313|      31.691|   0.5%/128|   0.5%/136|   0.5%/138|   0.5%/141 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 110   |   43731|     658.241|   0.3%/212|   0.3%/228|   0.3%/231|   0.3%/235 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  92   |      27|       7.565|   0.9%/ 74|   1.1%/ 65|   1.1%/ 63|   1.1%/ 62 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  94   |      20|       0.587|   0.7%/ 92|   1.3%/ 54|   1.4%/ 48|   1.6%/ 43 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  94   |      44|       1.363|   4.1%/ 17|   4.4%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  88   |      22|       1.220|   0.0%/ --|   5.3%/ 13|   5.3%/ 13|   6.9%/ 10 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  98   |       4|       0.264|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |

