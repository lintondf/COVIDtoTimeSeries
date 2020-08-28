# State and Country COVID-19 Analysis #
## Updated: at 2020-08-28 for data as of 2020-08-27 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.1% of deaths and 40.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.3% of deaths and 58.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 149   |   32925|    1692.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 149   |   15955|    1796.297|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 149   |   12780|     323.444|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 149   |   12935|     446.100|   1.6%/ 43|   1.4%/ 49|   1.4%/ 50|   1.3%/ 52 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 149   |   11216|     522.196|   1.4%/ 48|   1.2%/ 58|   1.1%/ 61|   1.1%/ 64 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 149   |    8994|    1294.168|   0.2%/403|   0.2%/394|   0.2%/392|   0.2%/390 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 149   |    8168|     644.573|   0.2%/287|   0.2%/277|   0.3%/275|   0.3%/272 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 149   |    7627|     595.747|   0.2%/318|   0.2%/316|   0.2%/317|   0.2%/317 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 149   |    6698|     670.657|   0.2%/443|   0.2%/423|   0.2%/418|   0.2%/414 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 149   |    5419|     510.374|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 149   |  181421|     550.521|   0.6%/123|   0.5%/131|   0.5%/133|   0.5%/136 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 149   |  119298|     564.294|   0.9%/ 80|   0.8%/ 85|   0.8%/ 86|   0.8%/ 88 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 149   |   63400|     500.878|   0.9%/ 74|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 149   |   62374|      45.822|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 149   |   40953|     616.438|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 149   |   35492|     589.199|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 149   |   30560|     455.608|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 149   |   28934|     614.310|   0.1%/804|   0.1%/681|   0.1%/656|   0.1%/633 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 149   |   29433|     916.016|   0.7%/ 95|   0.6%/107|   0.6%/111|   0.6%/115 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 149   |   21423|     256.940|   0.7%/ 97|   0.6%/113|   0.6%/118|   0.6%/123 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 149   |    2103|     428.943|   0.8%/ 91|   0.6%/114|   0.6%/121|   0.5%/130 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 149   |      33|      45.144|   1.2%/ 60|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 149   |    4998|     686.665|   0.9%/ 80|   0.7%/ 99|   0.7%/105|   0.6%/112 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 149   |     736|     243.787|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 149   |   12780|     323.444|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 149   |    1933|     335.695|   0.2%/368|   0.2%/386|   0.2%/390|   0.2%/395 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 149   |    4466|    1252.749|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 149   |     603|     619.532|   0.1%/470|   0.2%/434|   0.2%/424|   0.2%/415 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 149   |   11216|     522.196|   1.4%/ 48|   1.2%/ 58|   1.1%/ 61|   1.1%/ 64 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 149   |    5419|     510.374|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 149   |      53|      37.436|   2.5%/ 27|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 149   |     342|     191.603|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 149   |    8168|     644.573|   0.2%/287|   0.2%/277|   0.3%/275|   0.3%/272 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 149   |    3271|     485.857|   0.4%/182|   0.4%/181|   0.4%/181|   0.4%/181 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 149   |    1077|     341.406|   0.9%/ 79|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 149   |     443|     151.994|   0.8%/ 91|   0.7%/ 94|   0.7%/ 95|   0.7%/ 96 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 149   |     903|     202.069|   0.9%/ 74|   1.0%/ 68|   1.0%/ 67|   1.1%/ 65 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 149   |    4893|    1052.554|   0.8%/ 91|   0.7%/ 95|   0.7%/ 95|   0.7%/ 96 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 149   |     131|      97.812|   0.3%/213|   0.4%/196|   0.4%/192|   0.4%/188 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 149   |    3727|     616.487|   0.2%/329|   0.2%/353|   0.2%/360|   0.2%/366 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 149   |    8994|    1294.168|   0.2%/403|   0.2%/394|   0.2%/392|   0.2%/390 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 149   |    6698|     670.657|   0.2%/443|   0.2%/423|   0.2%/418|   0.2%/414 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 149   |    1845|     327.136|   0.5%/140|   0.5%/133|   0.5%/132|   0.5%/130 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 149   |    2396|     804.984|   1.3%/ 55|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 149   |    1493|     243.307|   0.6%/116|   0.6%/120|   0.6%/121|   0.6%/122 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 149   |     100|      93.207|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 149   |     389|     201.316|   0.6%/109|   0.6%/110|   0.6%/110|   0.6%/110 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 149   |    1285|     417.295|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 149   |     431|     316.818|   0.1%/528|   0.1%/550|   0.1%/556|   0.1%/563 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 149   |   15955|    1796.297|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 149   |     765|     364.647|   0.6%/119|   0.5%/127|   0.5%/129|   0.5%/131 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 149   |   32925|    1692.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 149   |    2644|     252.083|   1.0%/ 70|   0.9%/ 75|   0.9%/ 76|   0.9%/ 78 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 149   |     142|     185.742|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 149   |    4074|     348.572|   0.5%/129|   0.5%/136|   0.5%/138|   0.5%/140 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 149   |     770|     194.505|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 149   |     441|     104.655|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 149   |    7627|     595.747|   0.2%/318|   0.2%/316|   0.2%/317|   0.2%/317 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 149   |     425|     133.120|   2.1%/ 33|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 149   |    1038|     980.067|   0.2%/404|   0.2%/344|   0.2%/331|   0.2%/318 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 149   |    2667|     517.995|   1.3%/ 53|   1.1%/ 63|   1.1%/ 66|   1.0%/ 69 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 149   |     165|     186.751|   0.6%/116|   0.5%/148|   0.4%/159|   0.4%/171 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 149   |    1677|     245.464|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 149   |   12935|     446.100|   1.6%/ 43|   1.4%/ 49|   1.4%/ 50|   1.3%/ 52 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 149   |  181421|     550.521|   0.6%/123|   0.5%/131|   0.5%/133|   0.5%/136 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 149   |     406|     126.571|   0.9%/ 73|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 149   |      58|      93.306|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 149   |    2518|     294.947|   0.5%/143|   0.5%/149|   0.5%/150|   0.5%/151 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 149   |    1915|     251.512|   0.6%/118|   0.5%/133|   0.5%/137|   0.5%/142 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 149   |     195|     108.846|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 149   |    1110|     190.566|   0.6%/116|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 137   |      38|      65.503|   0.7%/105|   0.5%/128|   0.5%/135|   0.5%/145 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 149   |    1414|      43.879|   0.3%/241|   0.2%/294|   0.2%/313|   0.2%/335 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 149   |     271|      95.279|   1.6%/ 42|   1.4%/ 48|   1.4%/ 50|   1.3%/ 51 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 149   |    1481|      34.432|   0.7%/101|   0.6%/107|   0.6%/108|   0.6%/110 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 149   |     110|       3.527|   1.8%/ 38|   1.5%/ 47|   1.4%/ 50|   1.3%/ 53 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 149   |    8047|     179.069|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 149   |     871|     294.418|   0.5%/146|   0.4%/170|   0.4%/176|   0.4%/184 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 149   |     619|      24.116|   3.4%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 149   |     734|      82.494|   0.1%/833|   0.1%/879|   0.1%/893|   0.1%/909 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 149   |     530|      52.623|   0.3%/211|   0.2%/376|   0.2%/461|   0.1%/591 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 149   |     190|     123.294|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 96 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 149   |    4116|      24.430|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 149   |     657|      69.790|   0.7%/100|   0.7%/ 94|   0.7%/ 93|   0.8%/ 91 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 149   |   10019|     869.393|   0.1%/906|   0.1%/857|   0.1%/848|   0.1%/841 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 144   |      40|       3.392|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 149   |    4843|     422.199|   1.5%/ 46|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 149   |     589|     178.396|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 149   |       3|       1.425|   1.3%/ 51|   0.8%/ 88|   0.6%/110|   0.5%/147 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 149   |  119298|     564.294|   0.9%/ 80|   0.8%/ 85|   0.8%/ 86|   0.8%/ 88 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 149   |     593|      85.368|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 149   |      55|       2.650|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 137   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 149   |     412|      15.517|   0.2%/335|   0.2%/334|   0.2%/336|   0.2%/337 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 149   |    9147|     240.708|   0.1%/968|   0.1%/955|   0.1%/951|   0.1%/948 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  97   |      61|      11.119|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 122   |      77|       4.713|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 149   |   11097|     580.772|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/149 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 149   |    4723|       3.368|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 149   |   18895|     382.525|   2.0%/ 35|   1.8%/ 39|   1.7%/ 41|   1.7%/ 42 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 149   |     418|      82.544|   2.8%/ 25|   2.3%/ 31|   2.1%/ 32|   2.0%/ 34 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 149   |     177|      43.389|   0.6%/110|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 149   |      89|       7.929|   0.3%/257|   0.3%/201|   0.4%/190|   0.4%/180 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 149   |     624|     107.138|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 149   |    1653|     159.616|   1.2%/ 59|   1.1%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 149   |    6410|     366.970|   0.5%/139|   0.5%/131|   0.5%/129|   0.5%/127 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 149   |    5354|      53.390|   0.3%/215|   0.3%/249|   0.3%/258|   0.3%/269 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 149   |     711|     109.594|   1.3%/ 54|   1.0%/ 66|   1.0%/ 70|   0.9%/ 74 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 128   |      83|      61.208|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 145   |     779|       7.897|   3.2%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 149   |     335|      60.687|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 149   |   30560|     455.608|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 149   |      53|      24.603|   0.1%/484|   0.1%/645|   0.1%/705|   0.1%/779 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 149   |     131|      55.997|  10.1%/  7|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 146   |      18|       4.767|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 149   |    9294|     111.776|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 149   |     280|       9.248|   1.3%/ 52|   1.2%/ 58|   1.2%/ 60|   1.1%/ 62 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 149   |     248|      23.169|   0.9%/ 79|   1.0%/ 71|   1.0%/ 69|   1.0%/ 68 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 149   |    2716|     163.577|   1.1%/ 64|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 135   |      56|       4.592|   1.0%/ 67|   1.2%/ 56|   1.3%/ 53|   1.4%/ 51 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 124   |      35|      21.654|   0.4%/176|   0.3%/247|   0.3%/274|   0.2%/307 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 145   |     204|      17.645|   0.4%/182|   0.1%/524|   0.1%/ ***|   0.0%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 149   |    1747|     190.789|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 76 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 149   |     615|      62.924|   0.1%/640|   0.1%/654|   0.1%/658|   0.1%/663 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 149   |   62374|      45.822|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 149   |    6994|      26.204|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 149   |   21423|     256.940|   0.7%/ 97|   0.6%/113|   0.6%/118|   0.6%/123 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 149   |    6777|     173.210|   1.3%/ 55|   1.2%/ 57|   1.2%/ 57|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 149   |    1779|     361.478|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 149   |     894|      97.253|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 149   |   35492|     589.199|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 149   |      17|       6.123|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 149   |    1225|       9.726|   1.0%/ 69|   1.1%/ 61|   1.2%/ 59|   1.2%/ 57 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 149   |      11|       1.032|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 149   |    1611|      86.217|   1.6%/ 44|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 149   |     585|      12.307|   1.6%/ 44|   1.3%/ 51|   1.3%/ 53|   1.2%/ 55 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 149   |     514|     286.044|   2.3%/ 30|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 146   |     527|     119.316|   0.5%/153|   0.4%/182|   0.4%/191|   0.3%/201 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 147   |    1093|     167.255|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 147   |      33|      17.448|   0.2%/301|   0.3%/258|   0.3%/249|   0.3%/240 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 149   |     144|      21.071|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 146   |      83|      18.636|   0.1%/851|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 148   |     224|      32.568|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 149   |      84|      30.164|   0.3%/201|   0.4%/160|   0.5%/152|   0.5%/144 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 103   |     186|       7.097|   1.0%/ 72|   0.3%/206|   0.2%/378|   0.0%/ *** |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 149   |     125|       3.818|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 149   |     126|       6.198|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 149   |     158|      38.761|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 149   |   63400|     500.878|   0.9%/ 74|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 149   |     976|     363.946|   0.8%/ 88|   0.8%/ 91|   0.8%/ 92|   0.7%/ 93 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 149   |    1027|      28.627|   4.3%/ 16|   4.6%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  95   |      21|       0.708|   1.2%/ 58|   0.8%/ 85|   0.7%/ 94|   0.7%/104 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  49   |      63|      25.575|   5.4%/ 13|   5.7%/ 12|   5.5%/ 12|   5.1%/ 13 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 104   |     181|       6.048|   5.1%/ 14|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 149   |    6235|     357.136|   0.1%/ ***|   0.1%/921|   0.1%/886|   0.1%/853 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 149   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 149   |     138|      21.311|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 149   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 149   |    1023|       4.960|   0.4%/191|   0.3%/251|   0.3%/272|   0.2%/297 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 149   |     581|     279.501|   0.6%/115|   0.6%/119|   0.6%/120|   0.6%/120 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 149   |     265|      49.415|   0.1%/709|   0.1%/666|   0.1%/659|   0.1%/654 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 149   |     670|     143.628|   1.3%/ 54|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 149   |    6294|      28.695|   0.2%/434|   0.1%/532|   0.1%/564|   0.1%/599 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 149   |    1985|     470.477|   0.9%/ 76|   0.7%/ 92|   0.7%/ 98|   0.7%/103 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  32   |       4|       0.448|   8.2%/  8|   0.3%/204|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 149   |     267|      37.272|   6.1%/ 11|   6.4%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 149   |   29433|     916.016|   0.7%/ 95|   0.6%/107|   0.6%/111|   0.6%/115 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 149   |    3206|      29.547|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 149   |    2003|      52.202|   0.6%/115|   0.6%/113|   0.6%/112|   0.6%/112 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 149   |    1810|     176.123|   0.2%/404|   0.2%/402|   0.2%/401|   0.2%/401 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 149   |     198|      72.147|   0.2%/308|   0.1%/929|   0.0%/ ***|   0.0%/ -- |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 149   |    3479|     179.300|   1.4%/ 50|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 149   |   16815|     114.586|   0.6%/110|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  90   |      15|       1.239|   5.5%/ 13|   6.3%/ 11|   6.6%/ 10|   6.8%/ 10 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 149   |    3807|     111.264|   1.0%/ 69|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 149   |     282|      17.390|   1.0%/ 72|   0.8%/ 83|   0.8%/ 87|   0.8%/ 90 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 149   |     722|     103.717|   0.5%/134|   0.4%/197|   0.3%/224|   0.3%/257 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 127   |      69|       8.794|   0.1%/951|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 149   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 149   |      34|       6.142|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 149   |     134|      63.844|   0.3%/243|   0.2%/311|   0.2%/331|   0.2%/354 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 142   |      94|       5.903|   0.2%/400|   0.3%/275|   0.3%/254|   0.3%/235 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 149   |   14277|     242.916|   1.4%/ 49|   1.0%/ 66|   0.9%/ 73|   0.9%/ 81 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 149   |   28934|     614.310|   0.1%/804|   0.1%/681|   0.1%/656|   0.1%/633 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 149   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 149   |     829|      19.542|   0.3%/250|   0.2%/334|   0.2%/364|   0.2%/401 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 149   |    5823|     563.201|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 149   |    2003|     232.844|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 149   |     100|       5.688|   3.0%/ 23|   3.2%/ 21|   3.2%/ 21|   3.3%/ 21 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 149   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 149   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 149   |      29|       3.881|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 149   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 149   |      67|       5.727|   1.1%/ 62|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 149   |    6197|      74.524|   0.3%/204|   0.4%/197|   0.4%/195|   0.4%/193 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 149   |  181421|     550.521|   0.6%/123|   0.5%/131|   0.5%/133|   0.5%/136 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  35   |      28|       0.698|   7.0%/ 10|   7.1%/ 10|   8.0%/  9|   8.9%/  8 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 149   |    2432|      58.062|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 149   |     378|      38.170|   0.4%/190|   0.4%/172|   0.4%/168|   0.4%/164 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 149   |   40953|     616.438|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 149   |      43|      12.230|   0.9%/ 75|   1.0%/ 67|   1.1%/ 66|   1.1%/ 64 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 149   |     305|       8.941|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 149   |     375|      11.627|   2.5%/ 28|   2.2%/ 31|   2.1%/ 33|   2.0%/ 34 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  28   |      30|       0.313|   0.9%/ 77|   2.7%/ 25|   3.1%/ 22|   3.6%/ 19 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 148   |     311|      17.372|   0.8%/ 88|   0.6%/119|   0.5%/132|   0.5%/147 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 149   |     191|      12.596|   2.5%/ 27|   2.8%/ 25|   4.9%/ 14|   6.8%/ 10 |

