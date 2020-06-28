# State and Country COVID-19 Analysis #
## Updated: 2020-06-28 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 106   |   31407|    1614.459|   0.1%/466|   0.1%/549|   0.1%/572|   0.1%/598 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 110   |   13280|    1495.079|   0.3%/229|   0.2%/364|   0.2%/428|   0.1%/520 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 100   |    8049|    1158.279|   0.4%/162|   0.4%/182|   0.4%/188|   0.4%/194 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 103   |    6915|     545.685|   0.7%/101|   0.6%/122|   0.5%/129|   0.5%/136 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 101   |    6615|     516.694|   0.5%/142|   0.4%/159|   0.4%/163|   0.4%/168 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 101   |    6154|     616.174|   0.2%/384|   0.2%/453|   0.1%/472|   0.1%/491 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    5936|     150.237|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 101   |    4321|    1211.899|   0.2%/281|   0.2%/360|   0.2%/385|   0.2%/413 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 112   |    3390|     157.855|   1.2%/ 60|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 106   |    3192|     686.547|   0.4%/157|   0.5%/151|   0.5%/149|   0.5%/147 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  125050|     379.464|   0.7%/105|   0.7%/101|   0.7%/100|   0.7%/ 98 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 103   |   57437|     271.683|   2.2%/ 32|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 109   |   43618|     656.546|   0.3%/206|   0.3%/220|   0.3%/223|   0.3%/226 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   34841|     578.391|   0.1%/742|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   29845|     444.944|   0.1%/755|   0.1%/949|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   28502|     605.143|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 101   |   26587|     210.047|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 109   |   16955|      12.455|   3.0%/ 23|   2.7%/ 25|   2.6%/ 26|   2.6%/ 27 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   10302|     123.558|   1.2%/ 58|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 109   |    9739|     845.031|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |


# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, policital, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.
 
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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  95   |     915|     186.533|   1.3%/ 51|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  95   |      12|      16.654|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)|  99   |    1548|     212.633|   2.2%/ 32|   2.4%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  96   |     260|      86.073|   2.5%/ 27|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    5936|     150.237|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 106   |    1687|     292.920|   0.4%/189|   0.3%/271|   0.2%/305|   0.2%/348 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 101   |    4321|    1211.899|   0.2%/281|   0.2%/360|   0.2%/385|   0.2%/413 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  94   |     507|     520.938|   0.4%/185|   0.2%/331|   0.2%/411|   0.1%/544 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 112   |    3390|     157.855|   1.2%/ 60|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 108   |    2814|     265.010|   1.0%/ 69|   0.8%/ 87|   0.7%/ 94|   0.7%/101 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  89   |      17|      12.007|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  94   |      91|      50.675|   0.3%/212|   0.2%/278|   0.2%/298|   0.2%/319 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 103   |    6915|     545.685|   0.7%/101|   0.6%/122|   0.5%/129|   0.5%/136 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 104   |    2627|     390.282|   0.6%/119|   0.5%/142|   0.5%/149|   0.4%/158 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  95   |     707|     224.091|   0.6%/116|   0.4%/160|   0.4%/176|   0.4%/195 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 107   |     266|      91.427|   0.7%/106|   0.7%/105|   0.7%/104|   0.7%/103 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 104   |     554|     123.913|   0.8%/ 86|   0.8%/ 86|   0.8%/ 85|   0.8%/ 85 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 106   |    3192|     686.547|   0.4%/157|   0.5%/151|   0.5%/149|   0.5%/147 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  93   |     103|      76.989|   0.2%/311|   0.2%/308|   0.2%/306|   0.2%/304 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 101   |    3170|     524.375|   0.6%/118|   0.5%/145|   0.4%/154|   0.4%/163 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 100   |    8049|    1158.279|   0.4%/162|   0.4%/182|   0.4%/188|   0.4%/194 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 101   |    6154|     616.174|   0.2%/384|   0.2%/453|   0.1%/472|   0.1%/491 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)|  99   |    1469|     260.555|   0.8%/ 89|   0.5%/138|   0.4%/159|   0.4%/188 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 101   |    1032|     346.822|   1.1%/ 60|   1.2%/ 59|   1.2%/ 58|   1.2%/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 101   |    1015|     165.421|   0.9%/ 75|   0.8%/ 91|   0.7%/ 96|   0.7%/103 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  93   |      22|      20.527|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  92   |     271|     139.958|   1.6%/ 42|   1.3%/ 54|   1.2%/ 58|   1.1%/ 62 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 104   |     502|     162.942|   0.6%/117|   0.5%/130|   0.5%/134|   0.5%/139 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  97   |     364|     267.428|   1.2%/ 60|   1.2%/ 60|   1.2%/ 59|   1.2%/ 59 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 110   |   13280|    1495.079|   0.3%/229|   0.2%/364|   0.2%/428|   0.1%/520 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  95   |     495|     236.209|   1.0%/ 69|   0.8%/ 85|   0.8%/ 90|   0.7%/ 96 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 106   |   31407|    1614.459|   0.1%/466|   0.1%/549|   0.1%/572|   0.1%/598 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  95   |    1362|     129.823|   1.4%/ 49|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  93   |      79|     103.195|   0.4%/161|   0.4%/170|   0.4%/174|   0.4%/179 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 100   |    2818|     241.093|   0.7%/ 93|   0.6%/108|   0.6%/112|   0.6%/116 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 101   |     378|      95.647|   0.4%/163|   0.5%/146|   0.5%/142|   0.5%/137 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 105   |     202|      47.934|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 101   |    6615|     516.694|   0.5%/142|   0.4%/159|   0.4%/163|   0.4%/168 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)|  99   |     151|      47.348|   0.3%/214|   0.3%/204|   0.3%/200|   0.4%/195 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  92   |     936|     883.333|   0.8%/ 92|   0.6%/118|   0.5%/127|   0.5%/138 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 104   |     705|     137.004|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 109   |      89|     100.699|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)|  99   |     583|      85.360|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 103   |    2377|      81.968|   1.4%/ 51|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)|  98   |     170|      53.157|   1.4%/ 49|   1.0%/ 67|   0.9%/ 73|   0.9%/ 81 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 100   |      56|      90.124|   0.1%/661|   0.1%/753|   0.1%/809|   0.1%/889 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 106   |    1700|     199.135|   0.8%/ 87|   0.9%/ 77|   0.9%/ 75|   1.0%/ 72 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 120   |    1316|     172.761|   0.6%/115|   0.6%/119|   0.6%/120|   0.6%/122 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  90   |      92|      51.587|   0.5%/144|   0.6%/125|   0.6%/119|   0.6%/113 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 100   |     779|     133.719|   0.9%/ 81|   0.8%/ 88|   0.8%/ 90|   0.8%/ 92 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  76   |      21|      35.422|   0.5%/129|   0.3%/229|   0.2%/319|   0.1%/569 |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)|  98   |     708|      21.967|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 109   |      51|      17.751|   2.8%/ 25|   3.5%/ 20|   3.7%/ 19|   3.9%/ 18 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 108   |     901|      20.964|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  91   |      10|       0.321|   4.0%/ 17|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 112   |    1217|      27.085|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  94   |     426|     143.990|   3.5%/ 19|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 119   |     103|       4.028|   0.2%/418|   0.2%/279|   0.3%/256|   0.3%/236 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 108   |     699|      78.557|   0.2%/294|   0.3%/259|   0.3%/252|   0.3%/246 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 107   |     194|      19.272|   3.9%/ 18|   3.7%/ 18|   3.7%/ 18|   3.7%/ 19 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 104   |      83|      53.460|   5.0%/ 14|   3.9%/ 18|   3.6%/ 19|   3.3%/ 21 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 102   |    1738|      10.319|   3.0%/ 23|   2.5%/ 27|   2.4%/ 29|   2.3%/ 30 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  89   |     380|      40.355|   1.6%/ 43|   1.5%/ 47|   1.4%/ 48|   1.4%/ 50 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 109   |    9739|     845.031|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  83   |      16|       1.355|   5.7%/ 12|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  91   |     974|      84.922|   3.8%/ 18|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)|  99   |     177|      53.595|   0.6%/110|   0.7%/ 94|   0.8%/ 90|   0.8%/ 87 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  89   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 103   |   57437|     271.683|   2.2%/ 32|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 109   |     219|      31.529|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 102   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  76   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  95   |     335|      12.611|   1.1%/ 61|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 111   |    8654|     227.736|   0.4%/188|   0.3%/273|   0.2%/308|   0.2%/354 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  36   |      46|       8.298|  11.6%/  6|  10.9%/  6|   7.4%/  9|   3.6%/ 19 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  61   |      74|       4.557|   0.1%/658|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)|  98   |    5448|     285.120|   4.2%/ 16|   3.3%/ 21|   3.1%/ 22|   2.8%/ 24 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 109   |    4640|       3.309|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)|  98   |    2912|      58.952|   4.8%/ 14|   5.2%/ 13|   5.3%/ 13|   5.4%/ 13 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 101   |      12|       2.425|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 101   |     107|      26.307|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 102   |      86|       7.633|   0.1%/546|   0.1%/644|   0.1%/680|   0.1%/722 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 106   |     605|     103.880|   0.1%/674|   0.1%/964|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 103   |     723|      69.795|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 106   |    4448|     254.606|   1.0%/ 69|   1.0%/ 73|   0.9%/ 74|   0.9%/ 75 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 112   |    2768|      27.608|   4.1%/ 17|   4.1%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  89   |     138|      21.207|   5.2%/ 13|   6.3%/ 11|   6.5%/ 10|   6.8%/ 10 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  67   |      12|       8.835|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  84   |      92|       0.930|   3.4%/ 20|   1.5%/ 46|   1.0%/ 67|   0.6%/120 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)|  99   |     328|      59.292|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 134   |   29845|     444.944|   0.1%/755|   0.1%/949|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 100   |      44|      20.053|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  97   |       1|       0.426|   5.8%/ 12|   6.4%/ 11|   6.4%/ 11|   6.4%/ 11 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  85   |      14|       3.779|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 111   |    8975|     107.936|   0.1%/477|   0.1%/544|   0.1%/562|   0.1%/582 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)|  99   |     109|       3.602|   4.9%/ 14|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 109   |     192|      17.929|   0.3%/258|   0.2%/293|   0.2%/307|   0.2%/325 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 104   |     702|      42.272|   4.9%/ 14|   4.5%/ 15|   4.4%/ 16|   4.3%/ 16 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  74   |      30|       2.425|   1.3%/ 52|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  63   |      22|      13.568|   3.0%/ 23|   4.0%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  84   |     101|       8.708|   2.7%/ 25|   1.9%/ 36|   1.7%/ 41|   1.5%/ 45 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  94   |     458|      49.991|   3.2%/ 21|   3.9%/ 18|   4.1%/ 17|   4.3%/ 16 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 105   |     580|      59.365|   0.3%/264|   0.2%/329|   0.2%/349|   0.2%/372 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 109   |   16955|      12.455|   3.0%/ 23|   2.7%/ 25|   2.6%/ 26|   2.6%/ 27 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 109   |    2746|      10.287|   1.9%/ 37|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   10302|     123.558|   1.2%/ 58|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 116   |    1720|      43.955|   8.2%/  8|   8.0%/  9|   7.9%/  9|   7.8%/  9 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 109   |    1732|     351.841|   0.1%/529|   0.1%/606|   0.1%/621|   0.1%/633 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)|  99   |     313|      34.015|   0.3%/206|   0.4%/157|   0.5%/148|   0.5%/139 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 128   |   34841|     578.391|   0.1%/742|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 101   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 136   |     972|       7.717|   0.3%/208|   0.4%/195|   0.4%/191|   0.4%/188 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  93   |       9|       0.844|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  95   |     164|       8.783|   5.4%/ 13|   5.1%/ 13|   5.1%/ 14|   4.9%/ 14 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  94   |     141|       2.974|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  94   |      38|      20.914|   0.3%/271|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  85   |     348|      78.796|   1.3%/ 54|   1.1%/ 65|   1.0%/ 68|   1.0%/ 73 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  86   |      48|       7.314|   3.9%/ 17|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  86   |      31|      16.047|   0.6%/110|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 110   |      33|       4.857|   0.4%/162|   0.2%/278|   0.2%/325|   0.2%/384 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  85   |      34|       7.681|   0.5%/146|   0.2%/350|   0.1%/530|   0.1%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  87   |      20|       2.848|   7.9%/  9|   7.7%/  9|   7.8%/  9|   7.9%/  9 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)|  99   |      78|      27.987|   0.4%/189|   0.3%/243|   0.3%/257|   0.3%/271 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  42   |      16|       0.626|   3.7%/ 19|   2.5%/ 27|   1.7%/ 40|   0.9%/ 79 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 103   |     122|       3.713|   0.1%/830|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  91   |     115|       5.657|   0.9%/ 81|   0.5%/137|   0.4%/164|   0.3%/203 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  90   |     125|      30.693|   3.0%/ 23|   1.8%/ 38|   1.5%/ 46|   1.2%/ 56 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 101   |   26587|     210.047|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 102   |     528|     197.012|   2.0%/ 35|   1.8%/ 39|   1.7%/ 40|   1.7%/ 42 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 110   |     217|       6.062|   0.3%/259|   0.3%/208|   0.4%/197|   0.4%/186 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  34   |       5|       0.166|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  43   |      28|       0.927|   2.8%/ 24|   3.6%/ 19|   4.2%/ 17|   4.7%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 114   |    6131|     351.205|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  91   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  93   |      76|      11.760|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  95   |      67|       3.019|   0.1%/530|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  97   |     581|       2.818|   2.2%/ 31|   1.8%/ 39|   1.6%/ 43|   1.5%/ 46 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)|  98   |     283|     136.388|   3.1%/ 23|   2.8%/ 25|   2.7%/ 25|   2.6%/ 26 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 106   |     250|      46.485|   0.2%/297|   0.2%/280|   0.3%/275|   0.3%/270 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  89   |     159|      34.021|   3.3%/ 21|   2.8%/ 24|   2.7%/ 26|   2.6%/ 27 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 101   |    4320|      19.694|   3.3%/ 21|   2.7%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 109   |     581|     137.830|   2.3%/ 30|   2.5%/ 27|   2.6%/ 27|   2.7%/ 26 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)|  99   |      14|       1.939|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 100   |    9264|     288.320|   2.5%/ 27|   2.4%/ 29|   2.3%/ 30|   2.3%/ 31 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 147   |    1235|      11.377|   1.0%/ 66|   1.1%/ 64|   1.1%/ 63|   1.1%/ 63 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 108   |    1442|      37.573|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 103   |    1555|     151.360|   0.2%/288|   0.2%/299|   0.2%/299|   0.2%/297 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  92   |     114|      41.541|   3.2%/ 22|   2.6%/ 27|   2.4%/ 28|   2.3%/ 30 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)|  98   |    1596|      82.247|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 101   |    9049|      61.667|   2.0%/ 35|   1.7%/ 41|   1.6%/ 43|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  29   |       2|       0.162|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  96   |    1549|      45.275|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  88   |     104|       6.393|   3.8%/ 18|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 100   |     266|      38.249|   0.4%/197|   0.4%/192|   0.4%/191|   0.4%/191 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  66   |      59|       7.404|   1.0%/ 68|   1.6%/ 43|   1.7%/ 40|   1.9%/ 37 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)|  99   |      26|       4.586|   0.1%/596|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  92   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 106   |     109|      52.052|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  81   |      91|       5.698|   0.3%/228|   0.2%/449|   0.1%/584|   0.1%/840 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  93   |    2455|      41.767|   4.0%/ 17|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 117   |   28502|     605.143|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  92   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 107   |     589|      13.871|   2.0%/ 35|   1.5%/ 47|   1.4%/ 51|   1.2%/ 55 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 109   |    5292|     511.881|   0.6%/113|   0.6%/115|   0.6%/116|   0.6%/116 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 115   |    1965|     228.423|   0.1%/907|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  91   |       8|       0.433|   2.1%/ 34|   2.9%/ 24|   3.1%/ 22|   3.3%/ 21 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  89   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 119   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  93   |      14|       1.828|   0.6%/109|   1.1%/ 61|   1.3%/ 55|   1.4%/ 49 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  95   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 101   |      50|       4.287|   0.1%/634|   0.1%/920|   0.1%/ ***|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 103   |    5081|      61.101|   0.4%/162|   0.5%/152|   0.5%/150|   0.5%/148 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 120   |  125050|     379.464|   0.7%/105|   0.7%/101|   0.7%/100|   0.7%/ 98 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 107   |    1119|      26.717|   1.7%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 100   |     312|      31.535|   0.5%/128|   0.5%/137|   0.5%/139|   0.5%/142 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 109   |   43618|     656.546|   0.3%/206|   0.3%/220|   0.3%/223|   0.3%/226 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  91   |      26|       7.463|   0.9%/ 78|   1.0%/ 67|   1.1%/ 65|   1.1%/ 63 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  93   |      20|       0.576|   0.5%/135|   0.7%/ 95|   0.8%/ 86|   0.9%/ 78 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  93   |      42|       1.304|   4.0%/ 17|   4.6%/ 15|   4.7%/ 15|   4.8%/ 14 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  87   |      21|       1.159|   0.0%/ --|  17.8%/  4|   5.3%/ 13|   5.3%/ 13 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  97   |       4|       0.264|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |

