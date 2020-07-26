# State and Country COVID-19 Analysis #
## Updated: at 2020-07-26 for data as of 2020-07-25 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.4% of deaths and 39.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.4% of deaths and 56.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 116   |   32622|    1676.914|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 116   |   15837|    1782.999|   0.1%/530|   0.1%/944|   0.1%/ ***|   0.0%/ *** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 116   |    8521|    1226.134|   0.2%/381|   0.2%/430|   0.2%/444|   0.2%/458 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    8393|     212.409|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 116   |    7624|     601.626|   0.2%/294|   0.2%/376|   0.2%/402|   0.2%/430 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 116   |    7133|     557.214|   0.3%/273|   0.2%/290|   0.2%/295|   0.2%/300 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 116   |    6416|     642.484|   0.1%/565|   0.1%/696|   0.1%/741|   0.1%/793 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 116   |    5707|     265.740|   2.4%/ 29|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 116   |    4859|     167.585|   3.4%/ 20|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 116   |    4421|    1240.079|   0.1%/762|   0.1%/803|   0.1%/821|   0.1%/843 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 116   |  145755|     442.294|   0.6%/113|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 116   |   86591|     409.587|   1.4%/ 49|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 116   |   45830|     689.835|   0.2%/440|   0.1%/470|   0.1%/478|   0.1%/486 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 116   |   43262|     341.782|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 116   |   35118|     582.979|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 116   |   31948|      23.470|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26|   2.6%/ 26 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 116   |   30233|     450.732|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 116   |   28434|     603.696|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 116   |   14429|     449.067|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 116   |   15503|     185.942|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 116   |    1441|     293.958|   2.0%/ 34|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 116   |      19|      26.200|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 116   |    3254|     447.115|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 116   |     397|     131.674|   1.7%/ 41|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 116   |    8393|     212.409|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 116   |    1788|     310.511|   0.3%/223|   0.4%/191|   0.4%/185|   0.4%/179 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 116   |    4421|    1240.079|   0.1%/762|   0.1%/803|   0.1%/821|   0.1%/843 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 116   |     534|     547.928|   0.2%/370|   0.2%/326|   0.2%/315|   0.2%/305 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 116   |    5707|     265.740|   2.4%/ 29|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 116   |    3397|     319.939|   1.1%/ 62|   1.4%/ 51|   1.4%/ 48|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 116   |      26|      18.525|   1.2%/ 56|   1.7%/ 40|   1.9%/ 37|   2.0%/ 35 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 116   |     139|      77.600|   2.3%/ 30|   2.8%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 116   |    7624|     601.626|   0.2%/294|   0.2%/376|   0.2%/402|   0.2%/430 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 116   |    2889|     429.156|   0.4%/185|   0.4%/176|   0.4%/173|   0.4%/170 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 116   |     829|     262.596|   0.7%/ 96|   0.8%/ 88|   0.8%/ 86|   0.8%/ 85 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 116   |     326|     111.963|   0.8%/ 85|   0.9%/ 75|   0.9%/ 73|   1.0%/ 71 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 116   |     698|     156.273|   0.8%/ 87|   0.8%/ 91|   0.8%/ 92|   0.7%/ 93 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 116   |    3612|     777.001|   0.4%/160|   0.4%/174|   0.4%/179|   0.4%/184 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 116   |     120|      89.011|   0.4%/171|   0.3%/225|   0.3%/244|   0.3%/268 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 116   |    3433|     567.900|   0.3%/260|   0.2%/278|   0.2%/282|   0.2%/287 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 116   |    8521|    1226.134|   0.2%/381|   0.2%/430|   0.2%/444|   0.2%/458 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 116   |    6416|     642.484|   0.1%/565|   0.1%/696|   0.1%/741|   0.1%/793 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 116   |    1611|     285.724|   0.3%/206|   0.3%/206|   0.3%/206|   0.3%/206 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 116   |    1474|     495.249|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 116   |    1189|     193.774|   0.7%/ 94|   0.8%/ 83|   0.9%/ 80|   0.9%/ 77 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 116   |      46|      43.331|   2.9%/ 23|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 116   |     317|     163.721|   0.7%/ 95|   0.9%/ 80|   0.9%/ 77|   0.9%/ 75 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 116   |     724|     235.036|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 116   |     407|     299.139|   0.4%/193|   0.4%/185|   0.4%/183|   0.4%/179 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 116   |   15837|    1782.999|   0.1%/530|   0.1%/944|   0.1%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 116   |     605|     288.333|   0.8%/ 82|   0.9%/ 79|   0.9%/ 78|   0.9%/ 77 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 116   |   32622|    1676.914|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 116   |    1792|     170.845|   1.3%/ 53|   1.5%/ 48|   1.5%/ 46|   1.5%/ 45 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 116   |      98|     128.824|   1.1%/ 64|   1.2%/ 56|   1.3%/ 54|   1.3%/ 52 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 116   |    3289|     281.397|   0.6%/109|   0.7%/101|   0.7%/ 99|   0.7%/ 97 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 116   |     484|     122.210|   1.2%/ 58|   1.4%/ 49|   1.5%/ 48|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 116   |     282|      66.969|   1.4%/ 50|   1.5%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 116   |    7133|     557.214|   0.3%/273|   0.2%/290|   0.2%/295|   0.2%/300 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 116   |     191|      59.769|   1.3%/ 53|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 116   |    1004|     948.058|   0.2%/359|   0.2%/404|   0.2%/416|   0.2%/429 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 116   |    1362|     264.458|   3.2%/ 21|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 116   |     125|     140.747|   1.0%/ 67|   0.9%/ 78|   0.8%/ 81|   0.8%/ 86 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 116   |     950|     138.998|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 116   |    4859|     167.585|   3.4%/ 20|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 116   |  145755|     442.294|   0.6%/113|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 116   |     275|      85.896|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 116   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 116   |    2089|     244.719|   0.4%/154|   0.3%/215|   0.3%/238|   0.3%/266 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 116   |    1490|     195.656|   0.6%/117|   0.6%/124|   0.6%/126|   0.5%/128 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 116   |     103|      57.429|   0.5%/137|   0.6%/124|   0.6%/121|   0.6%/119 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 116   |     877|     150.683|   0.6%/111|   0.8%/ 91|   0.8%/ 87|   0.8%/ 83 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 104   |      26|      44.566|   0.8%/ 84|   0.8%/ 92|   0.7%/ 95|   0.7%/100 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 116   |    1281|      39.760|   1.6%/ 44|   1.2%/ 57|   1.1%/ 62|   1.0%/ 69 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 116   |     132|      46.354|   2.8%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 116   |    1142|      26.554|   1.0%/ 72|   1.0%/ 68|   1.0%/ 68|   1.0%/ 67 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 116   |      36|       1.158|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 116   |    2826|      62.887|   3.5%/ 20|   3.7%/ 18|   3.8%/ 18|   3.9%/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 116   |     712|     240.903|   1.8%/ 39|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 116   |     131|       5.106|   2.2%/ 31|   2.9%/ 24|   3.1%/ 22|   3.3%/ 21 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 116   |     712|      80.010|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 116   |     412|      40.951|   2.3%/ 30|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 116   |     139|      90.292|   1.8%/ 39|   1.7%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 116   |    2896|      17.188|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 116   |     532|      56.543|   1.0%/ 66|   0.9%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 116   |    9817|     851.848|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 111   |      36|       3.032|   3.5%/ 20|   3.1%/ 22|   3.1%/ 22|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 116   |    2555|     222.732|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 116   |     281|      85.242|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 116   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 116   |   86591|     409.587|   1.4%/ 49|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 116   |     337|      48.425|   1.7%/ 40|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 116   |      53|       2.540|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 104   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 116   |     391|      14.716|   0.5%/141|   0.6%/118|   0.6%/113|   0.6%/109 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 116   |    8946|     235.418|   0.1%/768|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  64   |      59|      10.717|   0.8%/ 88|   1.4%/ 48|   1.6%/ 43|   1.8%/ 39 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  89   |      75|       4.625|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 116   |    9225|     482.780|   1.1%/ 65|   0.9%/ 76|   0.9%/ 79|   0.8%/ 83 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 116   |    4645|       3.313|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 116   |    8260|     167.216|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 116   |      93|      18.430|   8.8%/  8|   9.6%/  7|   9.8%/  7|  10.0%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 116   |     127|      31.264|   0.9%/ 81|   1.0%/ 68|   1.1%/ 65|   1.1%/ 62 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 116   |      87|       7.782|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 116   |     613|     105.215|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 116   |    1056|     101.916|   1.3%/ 54|   1.2%/ 58|   1.2%/ 60|   1.1%/ 61 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 116   |    5529|     316.538|   0.7%/102|   0.6%/111|   0.6%/114|   0.6%/117 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 116   |    4678|      46.649|   1.4%/ 51|   1.0%/ 66|   1.0%/ 72|   0.9%/ 78 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 116   |     396|      60.981|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  95   |      51|      37.548|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 112   |     206|       2.093|   3.7%/ 19|   4.2%/ 16|   4.3%/ 16|   4.4%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 116   |     328|      59.366|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 116   |   30233|     450.732|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 116   |      48|      21.923|   0.4%/160|   0.5%/139|   0.5%/132|   0.6%/124 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 116   |       5|       2.244|   5.6%/ 12|   6.9%/ 10|   7.3%/  9|   7.7%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 113   |      16|       4.276|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 116   |    9122|     109.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 116   |     160|       5.293|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 56 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 116   |     199|      18.562|   0.3%/219|   0.4%/154|   0.5%/143|   0.5%/133 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 116   |    1747|     105.241|   2.7%/ 25|   2.4%/ 29|   2.3%/ 31|   2.2%/ 32 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 102   |      42|       3.469|   1.1%/ 63|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  91   |      26|      16.245|   0.1%/772|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 112   |     160|      13.861|   1.2%/ 56|   0.8%/ 82|   0.7%/ 92|   0.7%/106 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 116   |    1078|     117.728|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 116   |     597|      61.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 116   |   31948|      23.470|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26|   2.6%/ 26 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 116   |    4696|      17.595|   2.2%/ 32|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 116   |   15503|     185.942|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 116   |    4414|     112.811|   2.5%/ 28|   2.0%/ 34|   1.9%/ 36|   1.8%/ 39 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 116   |    1761|     357.793|   0.1%/802|   0.1%/629|   0.1%/595|   0.1%/564 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 116   |     451|      49.092|   1.8%/ 39|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 116   |   35118|     582.979|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 116   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 116   |     993|       7.882|   0.1%/714|   0.1%/589|   0.1%/562|   0.1%/535 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 116   |      11|       1.046|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 116   |     630|      33.712|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 116   |     278|       5.850|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 116   |     172|      95.888|   4.3%/ 16|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 113   |     427|      96.580|   0.7%/ 94|   0.7%/ 94|   0.7%/ 93|   0.7%/ 93 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 114   |     279|      42.678|   4.7%/ 15|   3.9%/ 18|   3.7%/ 18|   3.6%/ 19 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 114   |      31|      16.392|   0.1%/506|   0.1%/928|   0.1%/ ***|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 116   |      43|       6.335|   1.6%/ 43|   2.1%/ 33|   2.2%/ 31|   2.4%/ 29 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 113   |      77|      17.095|   1.0%/ 66|   0.4%/182|   0.2%/335|   0.0%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 115   |      58|       8.491|   3.0%/ 23|   2.6%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 116   |      80|      28.676|   0.1%/815|   0.1%/777|   0.1%/767|   0.1%/758 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  70   |      81|       3.072|   5.8%/ 12|   5.0%/ 14|   4.7%/ 15|   4.4%/ 16 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 116   |     123|       3.762|   0.1%/888|   0.1%/886|   0.1%/891|   0.1%/900 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 116   |     123|       6.073|   0.2%/400|   0.1%/467|   0.1%/478|   0.1%/485 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 116   |     160|      39.202|   0.6%/118|   0.3%/203|   0.3%/250|   0.2%/324 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 116   |   43262|     341.782|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 116   |     735|     274.031|   1.0%/ 66|   1.0%/ 72|   0.9%/ 73|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 116   |     292|       8.149|   1.5%/ 47|   1.7%/ 40|   1.8%/ 38|   1.9%/ 37 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  62   |      11|       0.381|   2.3%/ 30|   1.6%/ 43|   1.3%/ 51|   1.0%/ 68 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  16   |       7|       2.847|  14.5%/  5|  20.5%/  3|   0.0%/ --|   0.0%/ *** |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  71   |      44|       1.466|   1.3%/ 54|   1.8%/ 38|   2.0%/ 35|   2.1%/ 32 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 116   |    6160|     352.843|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 116   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 116   |     110|      16.961|   1.2%/ 57|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 116   |      69|       3.103|   0.1%/949|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 116   |     857|       4.158|   1.3%/ 54|   1.2%/ 59|   1.1%/ 61|   1.1%/ 63 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 116   |     460|     221.621|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.3%/ 51 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 116   |     256|      47.654|   0.1%/967|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 116   |     376|      80.499|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 116   |    5914|      26.964|   0.9%/ 80|   0.6%/110|   0.6%/121|   0.5%/135 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 116   |    1284|     304.252|   2.7%/ 26|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 116   |      39|       5.464|   5.0%/ 14|   6.0%/ 11|   6.2%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 116   |   14429|     449.067|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 116   |    1937|      17.850|   0.9%/ 78|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 116   |    1667|      43.434|   0.4%/158|   0.4%/174|   0.4%/179|   0.4%/183 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 116   |    1719|     167.266|   0.3%/252|   0.2%/302|   0.2%/317|   0.2%/333 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 116   |     168|      61.206|   1.0%/ 68|   0.7%/105|   0.6%/120|   0.5%/139 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 116   |    2166|     111.601|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 116   |   13270|      90.426|   1.2%/ 57|   1.1%/ 63|   1.1%/ 65|   1.0%/ 67 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  57   |       5|       0.404|   3.3%/ 21|   1.1%/ 65|   0.3%/205|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 116   |    2743|      80.151|   1.6%/ 43|   1.4%/ 51|   1.3%/ 53|   1.2%/ 56 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 116   |     185|      11.414|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 116   |     547|      78.483|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  94   |      67|       8.419|   0.3%/210|   0.3%/241|   0.3%/254|   0.3%/271 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 116   |      27|       4.778|   0.2%/450|   0.1%/572|   0.1%/636|   0.1%/725 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 116   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 116   |     115|      54.687|   0.2%/353|   0.3%/237|   0.3%/218|   0.3%/202 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 109   |      93|       5.869|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 116   |    6427|     109.346|   3.8%/ 18|   4.0%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 116   |   28434|     603.696|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 116   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 116   |     719|      16.939|   0.8%/ 90|   0.7%/ 94|   0.7%/ 94|   0.7%/ 95 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 116   |    5707|     552.036|   0.2%/296|   0.2%/315|   0.2%/320|   0.2%/326 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 116   |    1975|     229.508|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 116   |      38|       2.158|   4.4%/ 16|   6.5%/ 11|   4.1%/ 17|   4.0%/ 17 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 116   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 116   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 116   |      16|       2.116|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 116   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 116   |      50|       4.265|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 116   |    5604|      67.392|   0.3%/207|   0.3%/216|   0.3%/219|   0.3%/222 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 116   |  145755|     442.294|   0.6%/113|   0.7%/105|   0.7%/103|   0.7%/101 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 116   |    1615|      38.555|   1.1%/ 61|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 116   |     345|      34.874|   0.3%/256|   0.2%/338|   0.2%/367|   0.2%/400 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 116   |   45830|     689.835|   0.2%/440|   0.1%/470|   0.1%/478|   0.1%/486 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 116   |      35|       9.840|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 116   |     119|       3.483|   5.1%/ 13|   4.1%/ 17|   3.9%/ 18|   3.7%/ 19 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 116   |     140|       4.356|   3.5%/ 19|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 115   |     167|       9.324|   9.7%/  7|  10.0%/  7|  10.0%/  7|   9.8%/  7 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 116   |      35|       2.311|   6.3%/ 11|   4.9%/ 14|   4.5%/ 15|   4.2%/ 17 |

