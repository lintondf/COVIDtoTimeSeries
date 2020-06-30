# State and Country COVID-19 Analysis #
## Updated: 2020-06-30 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 108   |   31468|    1617.594|   0.1%/521|   0.1%/639|   0.1%/677|   0.1%/718 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 112   |   14726|    1657.936|   0.3%/251|   0.2%/378|   0.2%/432|   0.1%/502 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 102   |    8104|    1166.176|   0.4%/169|   0.4%/188|   0.4%/192|   0.4%/197 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 105   |    6970|     550.017|   0.6%/116|   0.5%/149|   0.4%/161|   0.4%/174 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 103   |    6652|     519.615|   0.4%/162|   0.4%/196|   0.3%/206|   0.3%/218 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 103   |    6170|     617.775|   0.2%/410|   0.1%/469|   0.1%/485|   0.1%/502 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 118   |    6043|     152.949|   1.1%/ 64|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 103   |    4332|    1215.007|   0.2%/323|   0.2%/432|   0.1%/469|   0.1%/512 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 114   |    3462|     161.185|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 108   |    3214|     691.458|   0.4%/170|   0.4%/176|   0.4%/178|   0.4%/180 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 122   |  126474|     383.786|   0.6%/114|   0.6%/115|   0.6%/115|   0.6%/115 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 105   |   59367|     280.810|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 111   |   43824|     659.650|   0.3%/227|   0.3%/254|   0.3%/261|   0.3%/269 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 130   |   34858|     578.661|   0.1%/881|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   29876|     445.400|   0.1%/883|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 119   |   28607|     607.359|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 103   |   27988|     221.115|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 111   |   17937|      13.177|   2.8%/ 24|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 131   |   10587|     126.974|   1.2%/ 56|   1.3%/ 52|   1.3%/ 52|   1.4%/ 51 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 111   |    9744|     845.521|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)|  97   |     936|     190.895|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)|  97   |      14|      18.686|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 101   |    1614|     221.739|   2.1%/ 32|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)|  98   |     271|      89.887|   2.5%/ 27|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 118   |    6043|     152.949|   1.1%/ 64|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 108   |    1692|     293.839|   0.3%/224|   0.2%/355|   0.2%/417|   0.1%/505 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 103   |    4332|    1215.007|   0.2%/323|   0.2%/432|   0.1%/469|   0.1%/512 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)|  96   |     519|     532.727|   0.3%/248|   0.1%/666|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 114   |    3462|     161.185|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 110   |    2835|     267.048|   0.8%/ 84|   0.6%/124|   0.5%/140|   0.4%/161 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  91   |      17|      12.007|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)|  96   |      91|      50.955|   0.3%/213|   0.3%/239|   0.3%/243|   0.3%/246 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 105   |    6970|     550.017|   0.6%/116|   0.5%/149|   0.4%/161|   0.4%/174 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 106   |    2646|     393.013|   0.5%/130|   0.4%/159|   0.4%/168|   0.4%/180 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)|  97   |     712|     225.826|   0.5%/129|   0.4%/171|   0.4%/185|   0.3%/200 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 109   |     271|      92.901|   0.7%/ 97|   0.8%/ 90|   0.8%/ 88|   0.8%/ 86 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 106   |     562|     125.695|   0.8%/ 90|   0.7%/ 93|   0.7%/ 94|   0.7%/ 94 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 108   |    3214|     691.458|   0.4%/170|   0.4%/176|   0.4%/178|   0.4%/180 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  95   |     104|      77.541|   0.3%/257|   0.3%/216|   0.3%/207|   0.4%/198 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 103   |    3193|     528.168|   0.5%/130|   0.4%/162|   0.4%/172|   0.4%/184 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 102   |    8104|    1166.176|   0.4%/169|   0.4%/188|   0.4%/192|   0.4%/197 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 103   |    6170|     617.775|   0.2%/410|   0.1%/469|   0.1%/485|   0.1%/502 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 101   |    1482|     262.716|   0.7%/102|   0.5%/151|   0.4%/172|   0.3%/198 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 103   |    1056|     354.748|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 103   |    1024|     166.776|   0.8%/ 87|   0.6%/117|   0.5%/129|   0.5%/144 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  95   |      22|      20.879|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  94   |     274|     141.855|   1.4%/ 50|   1.0%/ 71|   0.9%/ 79|   0.8%/ 89 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 106   |     506|     164.235|   0.5%/127|   0.5%/150|   0.4%/156|   0.4%/164 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)|  99   |     370|     272.013|   1.0%/ 66|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 112   |   14726|    1657.936|   0.3%/251|   0.2%/378|   0.2%/432|   0.1%/502 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)|  97   |     500|     238.548|   0.9%/ 81|   0.6%/113|   0.6%/125|   0.5%/140 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 108   |   31468|    1617.594|   0.1%/521|   0.1%/639|   0.1%/677|   0.1%/718 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)|  97   |    1386|     132.158|   1.2%/ 57|   1.1%/ 63|   1.1%/ 65|   1.0%/ 68 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  95   |      79|     104.082|   0.4%/163|   0.4%/171|   0.4%/176|   0.4%/181 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 102   |    2842|     243.166|   0.7%/105|   0.5%/130|   0.5%/138|   0.5%/147 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 103   |     383|      96.871|   0.5%/137|   0.6%/115|   0.6%/110|   0.7%/105 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 107   |     205|      48.691|   1.0%/ 71|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 103   |    6652|     519.615|   0.4%/162|   0.4%/196|   0.3%/206|   0.3%/218 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 101   |     153|      47.761|   0.3%/200|   0.4%/176|   0.4%/170|   0.4%/163 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  94   |     944|     891.316|   0.7%/102|   0.5%/135|   0.5%/147|   0.4%/161 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 106   |     723|     140.515|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 111   |      91|     103.404|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 101   |     598|      87.515|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 105   |    2435|      83.963|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 100   |     172|      53.754|   1.2%/ 59|   0.8%/ 91|   0.7%/105|   0.6%/125 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 102   |      56|      90.144|   0.1%/813|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 108   |    1732|     202.945|   0.8%/ 82|   0.9%/ 73|   1.0%/ 71|   1.0%/ 68 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 122   |    1327|     174.295|   0.5%/127|   0.5%/140|   0.5%/144|   0.5%/149 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  92   |      93|      52.083|   0.5%/149|   0.5%/132|   0.5%/127|   0.6%/124 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 102   |     787|     135.151|   0.8%/ 89|   0.7%/104|   0.6%/109|   0.6%/114 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  78   |      20|      35.213|   0.5%/144|   0.1%/ ***|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 100   |     748|      23.198|   3.1%/ 22|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 111   |      55|      19.294|   3.1%/ 22|   3.9%/ 18|   4.1%/ 17|   4.2%/ 16 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 110   |     917|      21.330|   1.0%/ 69|   0.9%/ 78|   0.9%/ 80|   0.8%/ 83 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  93   |      12|       0.379|   3.6%/ 19|   0.0%/ --|   3.2%/ 21|   3.2%/ 21 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 114   |    1283|      28.555|   2.9%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)|  96   |     448|     151.398|   3.2%/ 21|   2.9%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 121   |     104|       4.044|   0.1%/473|   0.2%/347|   0.2%/324|   0.2%/305 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 110   |     703|      78.966|   0.2%/294|   0.3%/275|   0.3%/271|   0.3%/267 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 109   |     208|      20.645|   3.7%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 106   |      88|      57.172|   4.8%/ 14|   3.9%/ 18|   3.7%/ 19|   3.4%/ 20 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 104   |    1818|      10.789|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  91   |     390|      41.423|   1.5%/ 45|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 111   |    9744|     845.521|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  85   |      18|       1.502|   6.0%/ 11|   3.7%/ 18|   3.2%/ 21|   2.8%/ 25 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  93   |    1054|      91.892|   3.8%/ 18|   3.8%/ 18|   3.9%/ 18|   3.9%/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 101   |     180|      54.522|   0.7%/101|   0.8%/ 86|   0.8%/ 83|   0.9%/ 79 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  91   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 105   |   59367|     280.810|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 111   |     225|      32.403|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 104   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  78   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)|  97   |     333|      12.554|   0.9%/ 79|   0.7%/102|   0.6%/116|   0.5%/137 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 113   |    8682|     228.482|   0.3%/223|   0.2%/351|   0.2%/412|   0.1%/498 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  38   |      47|       8.618|  14.6%/  5|   6.3%/ 11|   4.6%/ 15|   3.1%/ 22 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  63   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 100   |    5769|     301.914|   4.0%/ 17|   3.3%/ 21|   3.1%/ 22|   2.9%/ 23 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 111   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 100   |    3219|      65.176|   5.1%/ 13|   5.5%/ 12|   5.6%/ 12|   5.7%/ 12 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 103   |      12|       2.431|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 103   |     107|      26.272|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 104   |      86|       7.662|   0.2%/399|   0.2%/354|   0.2%/343|   0.2%/332 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 108   |     606|     104.000|   0.1%/773|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 105   |     741|      71.510|   1.4%/ 49|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 108   |    4518|     258.620|   0.9%/ 74|   0.8%/ 82|   0.8%/ 84|   0.8%/ 86 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 114   |    2968|      29.601|   3.9%/ 18|   3.7%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  91   |     158|      24.427|   5.7%/ 12|   6.7%/ 10|   7.0%/ 10|   7.2%/  9 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  69   |      32|      23.559|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  86   |     100|       1.011|   4.5%/ 15|   4.8%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 101   |     328|      59.355|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   29876|     445.400|   0.1%/883|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 102   |      45|      20.500|   2.4%/ 29|   1.7%/ 40|   1.5%/ 45|   1.3%/ 52 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)|  99   |       1|       0.426|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  87   |      14|       3.884|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 113   |    8992|     108.141|   0.1%/535|   0.1%/639|   0.1%/671|   0.1%/706 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 101   |     119|       3.918|   4.8%/ 14|   4.5%/ 15|   4.4%/ 16|   4.2%/ 16 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 111   |     193|      17.959|   0.2%/324|   0.1%/477|   0.1%/552|   0.1%/660 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 106   |     762|      45.886|   4.7%/ 15|   4.5%/ 15|   4.4%/ 15|   4.4%/ 16 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  76   |      31|       2.525|   1.4%/ 48|   1.8%/ 38|   1.9%/ 36|   2.0%/ 34 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  65   |      23|      14.617|   3.6%/ 19|   4.0%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  86   |     104|       8.981|   2.4%/ 29|   1.8%/ 38|   1.7%/ 40|   1.6%/ 42 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)|  96   |     489|      53.427|   3.3%/ 21|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 107   |     583|      59.674|   0.3%/263|   0.2%/295|   0.2%/303|   0.2%/311 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 111   |   17937|      13.177|   2.8%/ 24|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 111   |    2831|      10.606|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 131   |   10587|     126.974|   1.2%/ 56|   1.3%/ 52|   1.3%/ 52|   1.4%/ 51 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 118   |    1970|      50.346|   7.8%/  9|   7.3%/  9|   7.2%/  9|   7.0%/ 10 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 111   |    1735|     352.635|   0.1%/542|   0.1%/579|   0.1%/583|   0.1%/585 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 101   |     317|      34.453|   0.4%/161|   0.6%/118|   0.6%/111|   0.7%/103 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 130   |   34858|     578.661|   0.1%/881|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 103   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 138   |     977|       7.758|   0.3%/239|   0.3%/240|   0.3%/240|   0.3%/241 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  95   |       9|       0.844|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)|  97   |     185|       9.905|   5.9%/ 12|   6.0%/ 11|   6.0%/ 11|   6.1%/ 11 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)|  96   |     147|       3.091|   2.4%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)|  96   |      38|      21.313|   0.1%/470|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  87   |     354|      80.070|   1.2%/ 59|   0.9%/ 73|   0.9%/ 78|   0.8%/ 84 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  88   |      53|       8.149|   4.4%/ 16|   4.8%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  88   |      30|      15.962|   0.4%/169|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 112   |      34|       4.926|   0.5%/134|   0.5%/140|   0.5%/139|   0.5%/138 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  87   |      35|       7.775|   0.5%/150|   0.4%/185|   0.4%/195|   0.3%/206 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  89   |      23|       3.285|  19.3%/  3|   0.0%/ --|   5.3%/ 13|   8.5%/  8 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 101   |      78|      28.074|   0.3%/246|   0.2%/369|   0.2%/412|   0.1%/465 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  44   |      19|       0.711|   3.6%/ 19|   3.7%/ 18|   4.0%/ 17|   4.4%/ 15 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 105   |     121|       3.707|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  93   |     116|       5.707|   0.7%/ 97|   0.5%/154|   0.4%/179|   0.3%/212 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  92   |     130|      31.818|   2.6%/ 26|   1.7%/ 40|   1.5%/ 46|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 103   |   27988|     221.115|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 104   |     545|     203.191|   1.9%/ 37|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 112   |     220|       6.127|   0.4%/182|   0.5%/135|   0.5%/126|   0.6%/118 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  36   |       5|       0.166|   4.4%/ 16|   1.4%/ 51|   2.3%/ 30|   3.3%/ 21 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  45   |      29|       0.977|   2.6%/ 26|   3.3%/ 21|   3.4%/ 20|   3.4%/ 21 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 116   |    6134|     351.385|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  93   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  95   |      77|      11.958|   5.0%/ 14|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)|  97   |      67|       3.016|   0.1%/752|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)|  99   |     592|       2.872|   1.9%/ 36|   1.4%/ 51|   1.2%/ 57|   1.1%/ 65 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 100   |     299|     143.965|   3.0%/ 23|   2.8%/ 25|   2.7%/ 25|   2.6%/ 26 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 108   |     250|      46.615|   0.2%/373|   0.2%/422|   0.2%/439|   0.2%/460 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  91   |     168|      36.070|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 103   |    4472|      20.388|   3.0%/ 23|   2.3%/ 31|   2.1%/ 33|   1.9%/ 37 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 111   |     613|     145.303|   2.3%/ 29|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 101   |      15|       2.074|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 102   |    9644|     300.146|   2.4%/ 28|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 149   |    1260|      11.607|   1.0%/ 68|   1.0%/ 67|   1.0%/ 66|   1.0%/ 66 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 110   |    1464|      38.157|   1.0%/ 71|   0.9%/ 78|   0.9%/ 81|   0.8%/ 83 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 105   |    1564|     152.226|   0.3%/275|   0.3%/257|   0.3%/251|   0.3%/245 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  94   |     117|      42.752|   2.8%/ 25|   2.0%/ 35|   1.8%/ 39|   1.6%/ 44 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 100   |    1628|      83.893|   0.9%/ 73|   0.9%/ 73|   0.9%/ 73|   0.9%/ 73 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 103   |    9303|      63.395|   1.8%/ 37|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  31   |       2|       0.162|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)|  98   |    1631|      47.661|   3.3%/ 21|   2.9%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  90   |     110|       6.763|   3.7%/ 19|   3.2%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 102   |     270|      38.745|   0.4%/157|   0.5%/132|   0.5%/127|   0.6%/122 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  68   |      60|       7.634|   1.3%/ 54|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 101   |      26|       4.577|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  94   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 108   |     110|      52.402|   0.1%/682|   0.2%/388|   0.2%/347|   0.2%/313 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  83   |      91|       5.696|   0.2%/314|   0.1%/932|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  95   |    2594|      44.140|   3.7%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 119   |   28607|     607.359|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  94   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 109   |     598|      14.087|   1.6%/ 43|   1.1%/ 66|   0.9%/ 76|   0.8%/ 90 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 111   |    5338|     516.298|   0.5%/127|   0.5%/141|   0.5%/144|   0.5%/149 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 117   |    1966|     228.543|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  93   |       9|       0.506|   3.0%/ 23|   4.2%/ 16|   4.6%/ 15|   4.9%/ 14 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  91   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 121   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  95   |      14|       1.863|   0.6%/124|   0.8%/ 86|   0.9%/ 80|   0.9%/ 74 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)|  97   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 103   |      50|       4.285|   0.1%/822|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 105   |    5122|      61.598|   0.4%/167|   0.4%/163|   0.4%/163|   0.4%/162 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 122   |  126474|     383.786|   0.6%/114|   0.6%/115|   0.6%/115|   0.6%/115 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 109   |    1158|      27.645|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 102   |     315|      31.835|   0.5%/131|   0.5%/141|   0.5%/144|   0.5%/147 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 111   |   43824|     659.650|   0.3%/227|   0.3%/254|   0.3%/261|   0.3%/269 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  93   |      27|       7.653|   1.0%/ 70|   1.1%/ 63|   1.1%/ 62|   1.1%/ 60 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  95   |      21|       0.601|   1.1%/ 61|   2.0%/ 35|   2.2%/ 32|   2.4%/ 28 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  95   |      46|       1.437|   4.2%/ 16|   4.7%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  89   |      23|       1.289|  17.8%/  4|   5.3%/ 13|   6.9%/ 10|   1.6%/ 44 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)|  99   |       4|       0.264|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |

