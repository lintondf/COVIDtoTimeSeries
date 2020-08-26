# State and Country COVID-19 Analysis #
## Updated: at 2020-08-26 for data as of 2020-08-25 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.0% of deaths and 40.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.4% of deaths and 58.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 147   |   32908|    1691.640|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 147   |   15959|    1796.690|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 147   |   12530|     317.105|   1.1%/ 63|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 147   |   12636|     435.787|   1.7%/ 41|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 147   |   10993|     511.843|   1.5%/ 46|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 147   |    8960|    1289.366|   0.2%/435|   0.2%/442|   0.2%/443|   0.2%/445 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 147   |    8125|     641.169|   0.2%/313|   0.2%/313|   0.2%/313|   0.2%/314 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 147   |    7593|     593.110|   0.2%/332|   0.2%/336|   0.2%/337|   0.2%/339 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 147   |    6676|     668.463|   0.1%/464|   0.2%/447|   0.2%/443|   0.2%/440 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 147   |    5284|     497.647|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 147   |  179528|     544.778|   0.6%/123|   0.5%/133|   0.5%/136|   0.5%/139 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 147   |  117387|     555.255|   0.9%/ 80|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 147   |   62381|     492.828|   1.0%/ 71|   0.9%/ 81|   0.8%/ 83|   0.8%/ 86 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 147   |   60375|      44.354|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41|   1.7%/ 42 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 147   |   40960|     616.530|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 147   |   35470|     588.833|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 147   |   30530|     455.160|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 147   |   28864|     612.828|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 147   |   28872|     898.553|   0.8%/ 89|   0.7%/ 99|   0.7%/103|   0.7%/106 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 147   |   21178|     253.998|   0.8%/ 91|   0.7%/106|   0.6%/110|   0.6%/115 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 147   |    2078|     423.866|   0.8%/ 85|   0.6%/107|   0.6%/114|   0.6%/122 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 147   |      32|      43.489|   1.2%/ 59|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 147   |    4926|     676.706|   0.9%/ 79|   0.7%/104|   0.6%/112|   0.6%/123 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 147   |     709|     234.935|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 147   |   12530|     317.105|   1.1%/ 63|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 147   |    1927|     334.536|   0.2%/366|   0.2%/391|   0.2%/397|   0.2%/404 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 147   |    4465|    1252.251|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 147   |     601|     617.534|   0.2%/457|   0.2%/416|   0.2%/405|   0.2%/395 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 147   |   10993|     511.843|   1.5%/ 46|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 147   |    5284|     497.647|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 147   |      50|      35.286|   2.3%/ 31|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 147   |     329|     183.860|   1.9%/ 35|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 147   |    8125|     641.169|   0.2%/313|   0.2%/313|   0.2%/313|   0.2%/314 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 147   |    3246|     482.171|   0.4%/186|   0.4%/185|   0.4%/185|   0.4%/185 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 147   |    1057|     334.980|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 147   |     436|     149.489|   0.7%/102|   0.6%/116|   0.6%/120|   0.6%/124 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 147   |     884|     197.921|   0.9%/ 78|   1.0%/ 72|   1.0%/ 71|   1.0%/ 69 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 147   |    4822|    1037.281|   0.8%/ 91|   0.7%/ 94|   0.7%/ 95|   0.7%/ 96 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 147   |     130|      97.053|   0.3%/210|   0.4%/194|   0.4%/189|   0.4%/184 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 147   |    3712|     614.064|   0.2%/332|   0.2%/368|   0.2%/378|   0.2%/388 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 147   |    8960|    1289.366|   0.2%/435|   0.2%/442|   0.2%/443|   0.2%/445 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 147   |    6676|     668.463|   0.1%/464|   0.2%/447|   0.2%/443|   0.2%/440 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 147   |    1825|     323.550|   0.5%/148|   0.5%/142|   0.5%/140|   0.5%/139 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 147   |    2335|     784.461|   1.2%/ 60|   1.0%/ 68|   1.0%/ 71|   0.9%/ 73 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 147   |    1476|     240.504|   0.6%/122|   0.5%/129|   0.5%/131|   0.5%/134 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 147   |      97|      90.550|   1.4%/ 48|   1.1%/ 61|   1.1%/ 66|   1.0%/ 71 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 147   |     384|     198.708|   0.6%/111|   0.6%/112|   0.6%/112|   0.6%/113 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 147   |    1250|     405.816|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 147   |     430|     316.008|   0.1%/494|   0.1%/513|   0.1%/516|   0.1%/519 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 147   |   15959|    1796.690|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 147   |     756|     360.656|   0.6%/117|   0.6%/125|   0.5%/128|   0.5%/130 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 147   |   32908|    1691.640|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 147   |    2595|     247.400|   1.0%/ 70|   0.9%/ 77|   0.9%/ 79|   0.9%/ 81 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 147   |     139|     182.161|   1.3%/ 55|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 147   |    4030|     344.789|   0.5%/133|   0.5%/147|   0.5%/150|   0.4%/154 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 147   |     747|     188.867|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 147   |     433|     102.624|   1.0%/ 68|   0.9%/ 76|   0.9%/ 79|   0.8%/ 81 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 147   |    7593|     593.110|   0.2%/332|   0.2%/336|   0.2%/337|   0.2%/339 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 147   |     410|     128.285|   2.3%/ 31|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 147   |    1034|     975.846|   0.1%/516|   0.2%/458|   0.2%/445|   0.2%/433 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 147   |    2609|     506.694|   1.4%/ 51|   1.1%/ 62|   1.1%/ 65|   1.0%/ 68 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 147   |     164|     185.114|   0.7%/ 97|   0.6%/114|   0.6%/119|   0.6%/125 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 147   |    1620|     237.122|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 147   |   12636|     435.787|   1.7%/ 41|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 147   |  179528|     544.778|   0.6%/123|   0.5%/133|   0.5%/136|   0.5%/139 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 147   |     399|     124.403|   0.9%/ 77|   0.8%/ 90|   0.7%/ 93|   0.7%/ 97 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 147   |      58|      93.385|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 147   |    2492|     291.988|   0.4%/155|   0.4%/175|   0.4%/180|   0.4%/185 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 147   |    1897|     249.063|   0.7%/106|   0.6%/113|   0.6%/115|   0.6%/118 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 147   |     187|     104.581|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 147   |    1097|     188.371|   0.6%/121|   0.5%/132|   0.5%/135|   0.5%/139 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 135   |      37|      63.659|   1.1%/ 61|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 147   |    1408|      43.696|   0.3%/236|   0.2%/292|   0.2%/312|   0.2%/335 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 147   |     264|      92.669|   1.7%/ 42|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 147   |    1462|      33.999|   0.7%/100|   0.6%/107|   0.6%/108|   0.6%/110 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 147   |     107|       3.435|   1.6%/ 43|   1.1%/ 62|   1.0%/ 69|   0.9%/ 79 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 147   |    7569|     168.439|   3.1%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 147   |     864|     292.089|   0.5%/136|   0.4%/158|   0.4%/164|   0.4%/171 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 147   |     624|      24.306|   3.4%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 147   |     733|      82.382|   0.1%/720|   0.1%/706|   0.1%/703|   0.1%/701 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 147   |     528|      52.423|   0.4%/194|   0.2%/384|   0.1%/502|   0.1%/720 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 147   |     188|     121.578|   0.9%/ 75|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 147   |    4026|      23.899|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 147   |     647|      68.735|   0.7%/106|   0.7%/102|   0.7%/101|   0.7%/100 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 147   |   10003|     868.023|   0.1%/938|   0.1%/872|   0.1%/858|   0.1%/846 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 142   |      40|       3.368|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 147   |    4713|     410.881|   1.5%/ 45|   1.3%/ 52|   1.3%/ 53|   1.2%/ 55 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 147   |     569|     172.516|   1.7%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 147   |       3|       1.413|   1.6%/ 43|   1.1%/ 64|   0.9%/ 74|   0.8%/ 88 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 147   |  117387|     555.255|   0.9%/ 80|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 147   |     576|      82.850|   1.4%/ 49|   1.3%/ 55|   1.2%/ 56|   1.2%/ 58 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 147   |      55|       2.648|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 135   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 147   |     410|      15.460|   0.2%/336|   0.2%/331|   0.2%/331|   0.2%/332 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 147   |    9133|     240.360|   0.1%/983|   0.1%/979|   0.1%/977|   0.1%/975 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  95   |      61|      11.133|   0.1%/889|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 120   |      76|       4.695|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 147   |   10992|     575.256|   0.5%/129|   0.5%/139|   0.5%/142|   0.5%/145 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 147   |    4719|       3.365|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 147   |   18264|     369.748|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 147   |     400|      79.041|   2.9%/ 24|   2.4%/ 29|   2.2%/ 31|   2.1%/ 33 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 147   |     175|      42.889|   0.6%/116|   0.5%/134|   0.5%/139|   0.5%/145 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 147   |      89|       7.922|   0.2%/297|   0.3%/230|   0.3%/217|   0.3%/204 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 147   |     623|     107.051|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 147   |    1620|     156.443|   1.2%/ 57|   1.1%/ 63|   1.1%/ 64|   1.0%/ 66 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 147   |    6338|     362.856|   0.5%/151|   0.5%/148|   0.5%/147|   0.5%/146 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 147   |    5323|      53.081|   0.3%/217|   0.3%/269|   0.2%/286|   0.2%/304 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 147   |     697|     107.386|   1.3%/ 52|   1.1%/ 64|   1.0%/ 68|   1.0%/ 72 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 126   |      83|      61.379|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 143   |     737|       7.474|   3.5%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 147   |     335|      60.638|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 147   |   30530|     455.160|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 147   |      53|      24.538|   0.2%/374|   0.2%/440|   0.2%/459|   0.1%/480 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 147   |     122|      52.005|   6.9%/ 10|   2.4%/ 29|   1.2%/ 59|   2.3%/ 30 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 144   |      17|       4.635|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 147   |    9285|     111.666|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 147   |     274|       9.053|   1.5%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 147   |     244|      22.714|   0.8%/ 87|   0.9%/ 78|   0.9%/ 76|   0.9%/ 75 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 147   |    2664|     160.430|   1.1%/ 61|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 133   |      55|       4.471|   0.8%/ 92|   0.8%/ 83|   0.9%/ 81|   0.9%/ 79 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 122   |      34|      21.411|   0.2%/306|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 143   |     204|      17.613|   0.5%/154|   0.2%/347|   0.1%/525|   0.1%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 147   |    1707|     186.427|   0.8%/ 92|   0.5%/126|   0.5%/138|   0.5%/151 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 147   |     614|      62.806|   0.1%/571|   0.1%/545|   0.1%/540|   0.1%/535 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 147   |   60375|      44.354|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41|   1.7%/ 42 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 147   |    6821|      25.553|   1.2%/ 60|   1.1%/ 60|   1.1%/ 60|   1.1%/ 60 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 147   |   21178|     253.998|   0.8%/ 91|   0.7%/106|   0.6%/110|   0.6%/115 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 147   |    6617|     169.100|   1.3%/ 54|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 147   |    1779|     361.426|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 147   |     857|      93.279|   1.7%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 147   |   35470|     588.833|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 147   |      16|       5.962|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 147   |    1197|       9.503|   0.9%/ 73|   1.1%/ 63|   1.1%/ 61|   1.2%/ 59 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 147   |      11|       1.032|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 147   |    1579|      84.500|   1.3%/ 55|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 147   |     571|      11.997|   1.7%/ 39|   1.6%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 147   |     496|     275.945|   2.6%/ 26|   2.3%/ 30|   2.3%/ 30|   2.2%/ 31 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 144   |     524|     118.522|   0.5%/140|   0.4%/161|   0.4%/168|   0.4%/175 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 145   |    1548|     236.907|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 145   |      33|      17.323|   0.2%/413|   0.2%/387|   0.2%/379|   0.2%/372 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 147   |     134|      19.660|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 144   |      84|      18.698|   0.1%/492|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 146   |     211|      30.652|   3.4%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 147   |      83|      29.849|   0.4%/195|   0.5%/150|   0.5%/141|   0.5%/133 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 101   |     186|       7.077|   1.2%/ 60|   0.3%/201|   0.1%/481|   0.0%/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 147   |     125|       3.819|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 147   |     125|       6.185|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 147   |     158|      38.731|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 147   |   62381|     492.828|   1.0%/ 71|   0.9%/ 81|   0.8%/ 83|   0.8%/ 86 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 147   |     961|     358.393|   0.7%/ 93|   0.7%/101|   0.7%/103|   0.7%/105 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 147   |     951|      26.520|   4.3%/ 16|   4.5%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  93   |      21|       0.701|   1.4%/ 51|   0.9%/ 76|   0.8%/ 84|   0.7%/ 95 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  47   |      58|      23.538|   4.7%/ 15|   7.2%/ 10|   8.0%/  8|   8.9%/  8 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 102   |     164|       5.453|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14|   5.0%/ 14 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 147   |    6224|     356.550|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/989 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 147   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 147   |     136|      21.099|   0.5%/143|   0.4%/171|   0.4%/179|   0.4%/189 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 147   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 147   |    1017|       4.935|   0.4%/170|   0.3%/214|   0.3%/229|   0.3%/247 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 147   |     573|     275.940|   0.5%/126|   0.5%/144|   0.5%/149|   0.5%/154 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 147   |     265|      49.306|   0.1%/523|   0.2%/453|   0.2%/439|   0.2%/426 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 147   |     657|     140.923|   1.3%/ 53|   1.2%/ 59|   1.1%/ 60|   1.1%/ 62 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 147   |    6278|      28.621|   0.2%/410|   0.1%/511|   0.1%/544|   0.1%/581 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 147   |    1956|     463.710|   1.0%/ 70|   0.8%/ 85|   0.8%/ 89|   0.7%/ 94 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  30   |       4|       0.448|   3.6%/ 19|   3.6%/ 19|   1.0%/ 72|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 147   |     233|      32.604|   6.1%/ 11|   6.4%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 147   |   28872|     898.553|   0.8%/ 89|   0.7%/ 99|   0.7%/103|   0.7%/106 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 147   |    3080|      28.383|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 147   |    1978|      51.548|   0.6%/121|   0.6%/121|   0.6%/121|   0.6%/121 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 147   |    1804|     175.534|   0.2%/408|   0.2%/405|   0.2%/405|   0.2%/404 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 147   |     198|      72.088|   0.3%/250|   0.1%/560|   0.1%/827|   0.0%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 147   |    3388|     174.582|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 147   |   16618|     113.243|   0.6%/109|   0.6%/119|   0.6%/122|   0.6%/125 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  88   |      14|       1.103|   5.4%/ 13|   6.4%/ 11|   6.7%/ 10|   7.0%/ 10 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 147   |    3736|     109.177|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 147   |     278|      17.123|   1.0%/ 67|   0.9%/ 74|   0.9%/ 77|   0.9%/ 79 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 147   |     718|     103.052|   0.6%/118|   0.4%/168|   0.4%/189|   0.3%/214 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 125   |      69|       8.785|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 147   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 147   |      33|       6.117|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 147   |     133|      63.562|   0.3%/222|   0.2%/278|   0.2%/297|   0.2%/317 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 140   |      93|       5.865|   0.0%/ ***|   0.1%/ ***|   0.1%/928|   0.1%/857 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 147   |   14011|     238.380|   1.6%/ 44|   1.2%/ 59|   1.1%/ 65|   1.0%/ 71 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 147   |   28864|     612.828|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 147   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 147   |     826|      19.468|   0.3%/220|   0.2%/281|   0.2%/302|   0.2%/326 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 147   |    5817|     562.696|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 147   |    2001|     232.617|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 147   |      92|       5.241|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 147   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 147   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 147   |      29|       3.907|   0.8%/ 92|   0.1%/653|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 147   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 147   |      55|       4.706|   1.2%/ 58|   1.5%/ 47|   1.5%/ 45|   1.6%/ 43 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 147   |    6153|      73.997|   0.3%/208|   0.3%/201|   0.3%/199|   0.4%/198 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 147   |  179528|     544.778|   0.6%/123|   0.5%/133|   0.5%/136|   0.5%/139 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  33   |      24|       0.593|   7.0%/ 10|   6.1%/ 11|   5.9%/ 12|   5.8%/ 12 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 147   |    2365|      56.479|   1.3%/ 52|   1.3%/ 51|   1.3%/ 51|   1.4%/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 147   |     375|      37.870|   0.4%/182|   0.4%/160|   0.4%/155|   0.5%/151 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 147   |   40960|     616.530|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 147   |      42|      12.001|   0.9%/ 75|   1.0%/ 66|   1.1%/ 64|   1.1%/ 62 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 147   |     293|       8.578|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 147   |     359|      11.157|   2.7%/ 26|   2.4%/ 29|   2.3%/ 30|   2.3%/ 31 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  26   |      27|       0.283|   1.4%/ 50|   2.6%/ 27|   2.6%/ 27|   1.3%/ 55 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 146   |     309|      17.286|   0.8%/ 87|   0.7%/100|   0.7%/104|   0.6%/109 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 147   |     182|      11.978|   2.6%/ 27|   1.3%/ 54|   1.0%/ 71|   0.7%/104 |

