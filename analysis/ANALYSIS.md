# State and Country COVID-19 Analysis #
## Updated: at 2020-08-18 for data as of 2020-08-17 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.6% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.8% of deaths and 58.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 139   |   32855|    1688.890|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 139   |   15921|    1792.503|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 139   |   11502|     291.089|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 139   |   11219|     386.928|   2.1%/ 33|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 139   |    9781|     455.403|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 139   |    8849|    1273.368|   0.2%/412|   0.2%/415|   0.2%/415|   0.2%/416 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 139   |    7974|     629.302|   0.2%/326|   0.2%/330|   0.2%/332|   0.2%/333 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 139   |    7454|     582.252|   0.2%/305|   0.2%/288|   0.2%/284|   0.2%/279 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 139   |    6592|     660.042|   0.1%/484|   0.2%/451|   0.2%/444|   0.2%/436 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 139   |    4747|     447.102|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 139   |  171725|     521.097|   0.7%/106|   0.6%/110|   0.6%/112|   0.6%/113 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 139   |  109516|     518.022|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 139   |   57946|     457.793|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 139   |   52323|      38.438|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 35 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 139   |   46979|     707.139|   0.1%/883|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 139   |   35317|     586.291|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 139   |   30420|     453.522|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 139   |   28625|     607.749|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 139   |   25509|     793.881|   0.9%/ 74|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 139   |   20053|     240.511|   1.0%/ 72|   0.9%/ 81|   0.8%/ 84|   0.8%/ 86 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 139   |    1969|     401.490|   1.1%/ 64|   0.9%/ 76|   0.9%/ 80|   0.8%/ 84 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 139   |      29|      39.364|   1.3%/ 53|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 139   |    4650|     638.803|   1.3%/ 54|   1.0%/ 68|   1.0%/ 72|   0.9%/ 77 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 139   |     625|     207.206|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 139   |   11502|     291.089|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 139   |    1901|     330.057|   0.2%/305|   0.2%/334|   0.2%/341|   0.2%/349 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 139   |    4457|    1250.080|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 139   |     598|     614.307|   0.1%/754|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 139   |    9781|     455.403|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 139   |    4747|     447.102|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 139   |      40|      28.216|   3.6%/ 19|   4.6%/ 15|   4.8%/ 14|   5.1%/ 13 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 139   |     288|     161.436|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 139   |    7974|     629.302|   0.2%/326|   0.2%/330|   0.2%/332|   0.2%/333 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 139   |    3140|     466.361|   0.4%/189|   0.4%/187|   0.4%/186|   0.4%/185 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 139   |     989|     313.434|   0.8%/ 91|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 139   |     414|     142.165|   0.8%/ 86|   0.7%/ 95|   0.7%/ 98|   0.7%/100 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 139   |     818|     183.084|   0.7%/104|   0.6%/107|   0.6%/108|   0.6%/108 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 139   |    4541|     976.753|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 139   |     128|      94.963|   0.2%/287|   0.2%/342|   0.2%/359|   0.2%/377 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 139   |    3657|     604.910|   0.2%/282|   0.2%/304|   0.2%/310|   0.2%/317 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 139   |    8849|    1273.368|   0.2%/412|   0.2%/415|   0.2%/415|   0.2%/416 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 139   |    6592|     660.042|   0.1%/484|   0.2%/451|   0.2%/444|   0.2%/436 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 139   |    1749|     310.170|   0.4%/173|   0.4%/164|   0.4%/162|   0.4%/160 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 139   |    2141|     719.464|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 139   |    1401|     228.308|   0.6%/111|   0.6%/117|   0.6%/119|   0.6%/120 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 139   |      90|      84.237|   1.9%/ 37|   1.4%/ 50|   1.2%/ 55|   1.1%/ 62 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 139   |     365|     188.650|   0.6%/116|   0.6%/119|   0.6%/120|   0.6%/121 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 139   |    1096|     355.756|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 139   |     425|     312.269|   0.1%/575|   0.1%/922|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 139   |   15921|    1792.503|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 139   |     722|     344.321|   0.7%/104|   0.6%/115|   0.6%/118|   0.6%/121 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 139   |   32855|    1688.890|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 139   |    2404|     229.245|   1.1%/ 62|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 139   |     124|     163.266|   1.2%/ 58|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 139   |    3863|     330.487|   0.6%/114|   0.6%/123|   0.6%/126|   0.5%/128 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 139   |     672|     169.875|   1.3%/ 54|   1.2%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 139   |     399|      94.510|   1.2%/ 58|   1.1%/ 64|   1.0%/ 66|   1.0%/ 68 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 139   |    7454|     582.252|   0.2%/305|   0.2%/288|   0.2%/284|   0.2%/279 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 139   |     336|     105.360|   2.7%/ 26|   2.9%/ 24|   2.9%/ 23|   3.0%/ 23 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 139   |    1023|     965.242|   0.1%/793|   0.1%/830|   0.1%/837|   0.1%/844 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 139   |    2374|     461.030|   1.8%/ 39|   1.4%/ 48|   1.4%/ 51|   1.3%/ 54 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 139   |     156|     175.806|   0.9%/ 74|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 139   |    1398|     204.527|   1.6%/ 43|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 139   |   11219|     386.928|   2.1%/ 33|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 139   |  171725|     521.097|   0.7%/106|   0.6%/110|   0.6%/112|   0.6%/113 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 139   |     374|     116.701|   1.1%/ 64|   0.9%/ 77|   0.8%/ 82|   0.8%/ 87 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 139   |      58|      93.608|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 139   |    2427|     284.301|   0.5%/137|   0.4%/161|   0.4%/169|   0.4%/179 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 139   |    1793|     235.499|   0.8%/ 92|   0.8%/ 91|   0.8%/ 91|   0.8%/ 91 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 139   |     163|      90.948|   2.2%/ 31|   2.4%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 139   |    1051|     180.494|   0.7%/104|   0.6%/112|   0.6%/115|   0.6%/117 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 127   |      30|      52.418|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 139   |    1378|      42.765|   0.5%/151|   0.4%/159|   0.4%/161|   0.4%/162 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 139   |     237|      83.186|   2.2%/ 31|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 139   |    1387|      32.255|   0.8%/ 90|   0.7%/ 97|   0.7%/ 98|   0.7%/100 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 139   |      96|       3.081|   2.7%/ 26|   2.3%/ 30|   2.2%/ 31|   2.1%/ 32 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 139   |    6009|     133.711|   3.1%/ 23|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 139   |     834|     282.062|   0.6%/117|   0.5%/153|   0.4%/165|   0.4%/179 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 139   |     443|      17.260|   5.0%/ 14|   5.1%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 139   |     728|      81.750|   0.1%/620|   0.1%/549|   0.1%/533|   0.1%/518 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 139   |     523|      51.967|   0.7%/106|   0.4%/196|   0.3%/248|   0.2%/338 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 139   |     174|     112.842|   0.9%/ 74|   0.8%/ 81|   0.8%/ 84|   0.8%/ 86 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 139   |    3709|      22.015|   1.0%/ 67|   1.0%/ 72|   0.9%/ 73|   0.9%/ 74 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 139   |     616|      65.445|   0.5%/130|   0.4%/158|   0.4%/166|   0.4%/175 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 139   |    9930|     861.634|   0.1%/ ***|   0.1%/846|   0.1%/812|   0.1%/780 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 134   |      39|       3.354|   0.4%/196|   0.2%/329|   0.2%/388|   0.1%/467 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 139   |    4260|     371.389|   1.8%/ 38|   1.6%/ 44|   1.5%/ 47|   1.4%/ 49 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 139   |     498|     150.929|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 139   |       3|       1.250|   3.6%/ 19|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 139   |  109516|     518.022|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 139   |     520|      74.785|   1.7%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 139   |      55|       2.613|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 127   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 139   |     402|      15.149|   0.2%/384|   0.2%/406|   0.2%/409|   0.2%/411 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 139   |    9082|     239.016|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  87   |      61|      11.174|   0.2%/278|   0.3%/258|   0.3%/259|   0.3%/264 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 112   |      76|       4.694|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 139   |   10585|     554.003|   0.6%/116|   0.5%/134|   0.5%/139|   0.5%/145 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 139   |    4708|       3.358|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 139   |   15851|     320.904|   2.5%/ 28|   2.3%/ 31|   2.2%/ 31|   2.1%/ 32 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 139   |     337|      66.681|   3.7%/ 18|   3.2%/ 21|   3.1%/ 22|   3.0%/ 23 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 139   |     169|      41.389|   0.8%/ 89|   0.6%/112|   0.6%/119|   0.5%/128 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 139   |      88|       7.881|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 139   |     622|     106.793|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 139   |    1473|     142.178|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 139   |    6125|     350.620|   0.4%/177|   0.3%/205|   0.3%/213|   0.3%/222 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 139   |    5221|      52.071|   0.4%/162|   0.3%/217|   0.3%/237|   0.3%/260 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 139   |     636|      98.112|   1.9%/ 37|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 118   |      89|      65.819|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 135   |     562|       5.700|   3.8%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 139   |     334|      60.369|   0.1%/987|   0.1%/904|   0.1%/888|   0.1%/875 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 139   |   30420|     453.522|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 139   |      52|      23.939|   0.2%/394|   0.1%/705|   0.1%/878|   0.1%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 139   |      63|      26.835|  19.0%/  3|  17.8%/  4|  13.6%/  5|   8.0%/  8 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 136   |      17|       4.622|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 139   |    9242|     111.146|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 139   |     239|       7.897|   1.6%/ 43|   1.6%/ 44|   1.6%/ 45|   1.5%/ 45 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 139   |     224|      20.874|   0.7%/ 96|   0.9%/ 80|   0.9%/ 76|   0.9%/ 73 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 139   |    2458|     148.019|   1.3%/ 54|   1.0%/ 66|   1.0%/ 71|   0.9%/ 75 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 125   |      52|       4.237|   0.5%/144|   0.3%/264|   0.2%/336|   0.2%/461 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 114   |      32|      19.744|   1.8%/ 39|   2.4%/ 28|   2.6%/ 26|   2.8%/ 25 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 135   |     198|      17.076|   1.2%/ 59|   1.3%/ 55|   1.3%/ 54|   1.3%/ 53 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 139   |    1660|     181.280|   1.0%/ 67|   0.5%/131|   0.4%/170|   0.3%/243 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 139   |     608|      62.208|   0.1%/600|   0.1%/509|   0.1%/491|   0.1%/476 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 139   |   52323|      38.438|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 35 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 139   |    6266|      23.478|   1.1%/ 63|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 139   |   20053|     240.511|   1.0%/ 72|   0.9%/ 81|   0.8%/ 84|   0.8%/ 86 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 139   |    5997|     153.255|   1.3%/ 53|   1.2%/ 59|   1.1%/ 60|   1.1%/ 62 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 139   |    1776|     360.813|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 139   |     698|      76.026|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 139   |   35317|     586.291|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 139   |      15|       5.406|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 139   |    1093|       8.678|   0.6%/113|   0.7%/ 93|   0.8%/ 89|   0.8%/ 86 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 139   |      11|       1.032|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 139   |    1414|      75.684|   0.6%/124|   0.7%/ 98|   0.7%/ 93|   0.8%/ 88 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 139   |     507|      10.660|   2.0%/ 35|   1.6%/ 44|   1.5%/ 46|   1.4%/ 50 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 139   |     425|     236.624|   3.2%/ 21|   2.9%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 136   |     505|     114.271|   0.7%/106|   0.6%/113|   0.6%/115|   0.6%/117 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 137   |    1521|     232.727|   0.4%/183|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 137   |      32|      16.907|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 139   |     104|      15.283|   3.6%/ 19|   3.8%/ 18|   3.8%/ 18|   3.9%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 136   |      84|      18.661|   0.5%/129|   0.5%/153|   0.4%/161|   0.4%/170 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 138   |     163|      23.737|   4.1%/ 17|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 139   |      81|      29.080|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  93   |     178|       6.774|   2.7%/ 25|   2.0%/ 34|   1.9%/ 37|   1.7%/ 41 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 139   |     125|       3.827|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 139   |     125|       6.190|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 139   |     157|      38.571|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 139   |   57946|     457.793|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 139   |     910|     339.284|   0.9%/ 77|   0.9%/ 80|   0.9%/ 81|   0.8%/ 81 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 139   |     667|      18.593|   3.8%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  85   |      20|       0.666|   2.6%/ 27|   1.6%/ 43|   1.4%/ 51|   1.1%/ 61 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  39   |      39|      15.743|   7.5%/  9|   9.0%/  8|   8.7%/  8|   8.3%/  8 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  94   |     110|       3.673|   4.5%/ 15|   4.7%/ 14|   4.8%/ 14|   4.8%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 139   |    6192|     354.679|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 139   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 139   |     131|      20.294|   0.5%/132|   0.4%/188|   0.3%/210|   0.3%/240 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 139   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 139   |     991|       4.808|   0.6%/125|   0.5%/151|   0.4%/160|   0.4%/169 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 139   |     553|     266.463|   0.6%/110|   0.5%/143|   0.4%/154|   0.4%/168 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 139   |     259|      48.212|   0.1%/690|   0.1%/525|   0.1%/494|   0.1%/465 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 139   |     595|     127.599|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 139   |    6210|      28.315|   0.2%/312|   0.2%/416|   0.2%/452|   0.1%/495 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 139   |    1830|     433.732|   1.3%/ 55|   1.0%/ 67|   1.0%/ 71|   0.9%/ 76 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  22   |       3|       0.336|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 139   |     113|      15.820|   6.2%/ 11|   7.0%/ 10|   7.2%/ 10|   7.4%/  9 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 139   |   25509|     793.881|   0.9%/ 74|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 139   |    2510|      23.127|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 28 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 139   |    1885|      49.114|   0.6%/119|   0.6%/114|   0.6%/113|   0.6%/112 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 139   |    1779|     173.145|   0.2%/408|   0.2%/411|   0.2%/410|   0.2%/410 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 139   |     195|      70.987|   0.7%/102|   0.6%/108|   0.6%/110|   0.6%/112 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 139   |    3029|     156.077|   1.5%/ 45|   1.6%/ 43|   1.6%/ 43|   1.6%/ 42 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 139   |   15846|     107.980|   0.7%/ 95|   0.7%/104|   0.7%/106|   0.6%/109 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  80   |       9|       0.698|   5.3%/ 13|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 139   |    3444|     100.646|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 139   |     258|      15.943|   1.3%/ 53|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 139   |     694|      99.593|   0.9%/ 75|   0.7%/ 97|   0.7%/105|   0.6%/114 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 117   |      69|       8.784|   0.2%/361|   0.2%/401|   0.2%/416|   0.2%/435 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 139   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 139   |      31|       5.744|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 139   |     132|      62.902|   0.4%/178|   0.3%/207|   0.3%/217|   0.3%/229 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 132   |      93|       5.852|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 139   |   12609|     214.536|   2.3%/ 30|   2.0%/ 35|   1.9%/ 37|   1.8%/ 39 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 139   |   28625|     607.749|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 139   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 139   |     808|      19.034|   0.4%/156|   0.4%/180|   0.4%/187|   0.4%/195 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 139   |    5795|     560.578|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 139   |    1993|     231.598|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 139   |      63|       3.600|   2.2%/ 31|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 139   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 139   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 139   |      28|       3.713|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 139   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 139   |      53|       4.516|   0.5%/154|   0.6%/119|   0.6%/112|   0.7%/106 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 139   |    5987|      71.994|   0.3%/227|   0.3%/223|   0.3%/222|   0.3%/221 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 139   |  171725|     521.097|   0.7%/106|   0.6%/110|   0.6%/112|   0.6%/113 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  25   |      15|       0.363|  12.8%/  5|   9.9%/  7|   8.4%/  8|   6.8%/ 10 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 139   |    2123|      50.689|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 139   |     363|      36.710|   0.2%/279|   0.3%/272|   0.3%/270|   0.3%/268 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 139   |   46979|     707.139|   0.1%/883|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 139   |      39|      10.960|   0.5%/127|   0.6%/125|   0.6%/125|   0.6%/124 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 139   |     247|       7.237|   3.0%/ 23|   2.6%/ 26|   2.5%/ 27|   2.4%/ 29 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 139   |     291|       9.027|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  18   |      25|       0.260|  17.0%/  4|  10.1%/  7|   4.6%/ 15|   4.4%/ 16 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 138   |     279|      15.597|   3.0%/ 23|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 139   |     160|      10.538|   0.6%/107|   2.1%/ 32|   1.0%/ 67|   1.8%/ 39 |

