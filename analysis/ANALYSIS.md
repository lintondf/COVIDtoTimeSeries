# State and Country COVID-19 Analysis #
## Updated: at 2021-01-12 for data as of 2020-12-31 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 32.9% of deaths and 31.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 58.7% of deaths and 50.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 275   |   36447|    1873.529|   0.4%/195|   0.4%/180|   0.4%/176|   0.4%/173 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 275   |   27965|     964.452|   0.7%/ 96|   0.7%/ 95|   0.7%/ 95|   0.7%/ 95 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 275   |   24328|     615.702|   1.1%/ 64|   1.2%/ 59|   1.2%/ 58|   1.2%/ 57 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 275   |   21610|    1006.135|   0.5%/139|   0.5%/136|   0.5%/136|   0.5%/135 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 275   |   18790|    2115.490|   0.5%/136|   0.5%/126|   0.6%/124|   0.6%/122 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 275   |   18304|    1444.492|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 275   |   15674|    1224.334|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 275   |   13347|    1336.457|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 275   |   12183|    1753.146|   0.5%/136|   0.5%/129|   0.5%/127|   0.6%/126 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 275   |   10902|    1026.762|   0.4%/158|   0.4%/157|   0.4%/157|   0.4%/157 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 275   |  343263|    1041.630|   0.8%/ 82|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 275   |  193863|     916.991|   0.4%/178|   0.4%/173|   0.4%/172|   0.4%/171 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 275   |  150533|     110.587|   0.2%/333|   0.2%/372|   0.2%/384|   0.2%/396 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 275   |  125372|     990.475|   0.5%/127|   0.5%/126|   0.5%/126|   0.6%/126 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 275   |   79068|    1312.576|   0.8%/ 85|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 275   |   73281|    1103.041|   0.7%/100|   0.7%/101|   0.7%/102|   0.7%/102 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 275   |   67839|    1011.374|   0.7%/ 96|   0.7%/ 98|   0.7%/ 99|   0.7%/100 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 275   |   57014|     388.525|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 275   |   58064|     696.398|   0.3%/254|   0.2%/373|   0.2%/422|   0.1%/487 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 275   |   51648|    1096.550|   0.3%/203|   0.3%/215|   0.3%/218|   0.3%/222 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 275   |    4830|     984.988|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 275   |     222|     303.915|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 275   |    8563|    1176.488|   1.0%/ 68|   1.1%/ 63|   1.1%/ 62|   1.1%/ 61 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 275   |    3637|    1205.114|   1.3%/ 52|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 275   |   24328|     615.702|   1.1%/ 64|   1.2%/ 59|   1.2%/ 58|   1.2%/ 57 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 275   |    4999|     868.132|   1.2%/ 60|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 275   |    5938|    1665.565|   0.7%/100|   0.7%/ 95|   0.7%/ 93|   0.8%/ 92 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 275   |     906|     930.296|   0.6%/108|   0.7%/101|   0.7%/ 99|   0.7%/ 98 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 275   |   21610|    1006.135|   0.5%/139|   0.5%/136|   0.5%/136|   0.5%/135 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 275   |   10902|    1026.762|   0.4%/158|   0.4%/157|   0.4%/157|   0.4%/157 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 275   |     297|     210.029|   0.4%/188|   0.3%/207|   0.3%/213|   0.3%/220 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 275   |    1480|     828.366|   1.1%/ 61|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 275   |   18304|    1444.492|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 275   |    8314|    1234.960|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57|   1.2%/ 57 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 275   |    4086|    1295.019|   1.0%/ 70|   1.0%/ 73|   0.9%/ 73|   0.9%/ 74 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 275   |    2794|     959.159|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 275   |    2652|     593.640|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 275   |    7404|    1592.754|   0.6%/123|   0.6%/117|   0.6%/115|   0.6%/114 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 275   |     345|     256.551|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 275   |    5847|     967.148|   0.8%/ 84|   0.9%/ 80|   0.9%/ 79|   0.9%/ 78 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 275   |   12183|    1753.146|   0.5%/136|   0.5%/129|   0.5%/127|   0.6%/126 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 275   |   13347|    1336.457|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 275   |    5619|     996.428|   1.1%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 275   |    4723|    1586.949|   0.8%/ 87|   0.8%/ 83|   0.8%/ 82|   0.8%/ 82 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 275   |    5760|     938.472|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 275   |    1011|     946.225|   0.8%/ 83|   0.7%/ 99|   0.7%/103|   0.6%/109 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 275   |    1804|     932.720|   1.1%/ 64|   1.0%/ 70|   1.0%/ 71|   0.9%/ 73 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 275   |    3085|    1001.486|   1.3%/ 55|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 275   |     710|     522.074|   1.4%/ 49|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 275   |   18790|    2115.490|   0.5%/136|   0.5%/126|   0.6%/124|   0.6%/122 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 275   |    2540|    1211.457|   1.4%/ 50|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 275   |   36447|    1873.529|   0.4%/195|   0.4%/180|   0.4%/176|   0.4%/173 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 275   |    6701|     638.930|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83|   0.8%/ 83 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 275   |    1402|    1839.597|   0.6%/116|   0.4%/155|   0.4%/170|   0.4%/187 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 275   |    8938|     764.628|   1.1%/ 64|   1.1%/ 62|   1.1%/ 62|   1.1%/ 61 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 275   |    2477|     625.890|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63|   1.1%/ 62 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 275   |    1534|     363.676|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 275   |   15674|    1224.334|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 275   |    1521|     476.261|   0.9%/ 76|   0.9%/ 78|   0.9%/ 79|   0.9%/ 79 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 275   |    1773|    1673.498|   0.9%/ 74|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 275   |    5220|    1013.754|   0.6%/109|   0.7%/104|   0.7%/103|   0.7%/102 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 275   |    1764|    1993.881|   1.0%/ 71|   0.8%/ 90|   0.7%/ 96|   0.7%/104 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 275   |    6882|    1007.200|   1.3%/ 52|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 275   |   27965|     964.452|   0.7%/ 96|   0.7%/ 95|   0.7%/ 95|   0.7%/ 95 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 275   |  343263|    1041.630|   0.8%/ 82|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 275   |    1308|     407.853|   1.1%/ 65|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 275   |     131|     210.466|   2.4%/ 29|   2.5%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 275   |    4948|     579.686|   0.7%/ 95|   0.8%/ 91|   0.8%/ 90|   0.8%/ 89 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 275   |    3308|     434.406|   0.6%/107|   0.7%/106|   0.7%/106|   0.7%/106 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 275   |    1362|     760.005|   1.9%/ 37|   1.8%/ 37|   1.8%/ 37|   1.8%/ 37 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 275   |    5543|     952.041|   1.1%/ 65|   1.0%/ 70|   1.0%/ 72|   0.9%/ 73 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 263   |     454|     785.211|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 275   |    2220|      68.891|   0.6%/108|   0.6%/109|   0.6%/109|   0.6%/109 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 275   |    1267|     445.251|   1.0%/ 68|   0.9%/ 75|   0.9%/ 78|   0.9%/ 80 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 275   |    2850|      66.283|   0.3%/211|   0.3%/247|   0.3%/258|   0.3%/270 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 275   |     408|      13.101|   0.5%/148|   0.5%/151|   0.5%/152|   0.5%/153 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 275   |   43898|     976.837|   0.3%/248|   0.2%/287|   0.2%/299|   0.2%/311 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 275   |    2955|     999.238|   0.7%/105|   0.6%/123|   0.5%/129|   0.5%/135 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 275   |     909|      35.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 275   |    7361|     826.843|   1.7%/ 40|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 275   |    2804|     278.483|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 275   |     354|     229.102|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 275   |    7611|      45.175|   0.4%/171|   0.4%/174|   0.4%/175|   0.4%/176 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 275   |    1423|     151.272|   0.7%/102|   0.7%/101|   0.7%/101|   0.7%/101 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 275   |   20053|    1740.033|   0.4%/162|   0.4%/184|   0.4%/190|   0.4%/197 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 270   |      44|       3.775|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 275   |    9126|     795.668|   0.1%/866|   0.1%/838|   0.1%/830|   0.1%/822 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 275   |    4423|    1339.791|   1.0%/ 68|   0.9%/ 80|   0.8%/ 84|   0.8%/ 89 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 275   |      42|      17.937|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 275   |  193863|     916.991|   0.4%/178|   0.4%/173|   0.4%/172|   0.4%/171 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 275   |   10262|    1476.203|   1.5%/ 45|   1.3%/ 55|   1.2%/ 58|   1.1%/ 62 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 275   |      77|       3.705|   0.3%/219|   0.4%/190|   0.4%/184|   0.4%/178 |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 263   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 275   |     450|      16.955|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 275   |   15469|     407.098|   0.9%/ 76|   0.9%/ 73|   1.0%/ 73|   1.0%/ 72 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 223   |      63|      11.464|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 248   |     103|       6.356|   0.1%/991|   0.1%/923|   0.1%/905|   0.1%/886 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 275   |   16588|     868.150|   0.2%/295|   0.2%/299|   0.2%/299|   0.2%/300 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 275   |    4772|       3.403|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 275   |   42905|     868.592|   0.5%/128|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 275   |    2185|     432.040|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89|   0.8%/ 89 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 275   |    4473|    1097.382|   2.2%/ 32|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 275   |     142|      12.624|   0.3%/210|   0.4%/192|   0.4%/187|   0.4%/183 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 275   |    1059|     181.877|   1.7%/ 41|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 275   |    2416|     233.244|   0.1%/656|   0.1%/672|   0.1%/677|   0.1%/681 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 275   |   14206|     813.226|   0.1%/903|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 275   |    7364|      73.445|   0.5%/131|   0.6%/121|   0.6%/118|   0.6%/116 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 275   |    1326|     204.403|   0.6%/119|   0.6%/117|   0.6%/117|   0.6%/116 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 254   |      85|      62.878|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Eritrea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Eritrea.png)|  10   |       3|       0.858|   0.0%/ --|   0.0%/ --|   0.0%/ --|  44.2%/  1 |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 271   |    1943|      19.695|   0.4%/194|   0.3%/204|   0.3%/207|   0.3%/210 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 275   |     517|      93.589|   1.2%/ 56|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 275   |   67839|    1011.374|   0.7%/ 96|   0.7%/ 98|   0.7%/ 99|   0.7%/100 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 275   |      65|      29.984|   0.1%/627|   0.1%/765|   0.1%/811|   0.1%/863 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 275   |     123|      52.604|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 272   |    2876|     772.383|   1.7%/ 42|   1.4%/ 51|   1.3%/ 53|   1.2%/ 57 |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 275   |   33637|     404.539|   2.7%/ 26|   2.8%/ 25|   2.8%/ 25|   2.8%/ 24 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 275   |     334|      11.032|   0.1%/526|   0.1%/489|   0.1%/480|   0.1%/472 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 275   |    6989|     651.725|   1.6%/ 43|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 275   |    4846|     291.852|   0.5%/153|   0.5%/153|   0.5%/152|   0.5%/152 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 261   |      81|       6.652|   0.1%/713|   0.1%/825|   0.1%/860|   0.1%/900 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 250   |      45|      28.064|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 271   |     235|      20.302|   0.1%/ ***|   0.1%/903|   0.1%/879|   0.1%/857 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 275   |    3105|     338.995|   0.2%/292|   0.2%/286|   0.2%/284|   0.2%/282 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 275   |   10728|    1097.711|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 275   |  150533|     110.587|   0.2%/333|   0.2%/372|   0.2%/384|   0.2%/396 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 275   |   21782|      81.606|   0.9%/ 74|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 275   |   58064|     696.398|   0.3%/254|   0.2%/373|   0.2%/422|   0.1%/487 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 275   |   12987|     331.910|   0.1%/822|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 275   |    2225|     452.021|   0.3%/275|   0.3%/275|   0.3%/275|   0.3%/275 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 275   |    3249|     353.601|   0.6%/123|   0.6%/115|   0.6%/113|   0.6%/111 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 275   |   79068|    1312.576|   0.8%/ 85|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89 |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 275   |     304|     111.523|   0.5%/131|   0.5%/134|   0.5%/135|   0.5%/136 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 275   |    3179|      25.243|   1.6%/ 42|   1.7%/ 40|   1.7%/ 39|   1.8%/ 39 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 275   |    4346|     407.604|   0.5%/151|   0.1%/463|   0.1%/942|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 275   |    2746|     146.954|   0.4%/155|   0.5%/149|   0.5%/148|   0.5%/147 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 275   |    1751|      36.803|   0.2%/357|   0.1%/792|   0.1%/ ***|   0.0%/ *** |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 275   |    1406|     782.888|   0.7%/106|   0.6%/123|   0.5%/128|   0.5%/134 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 272   |     944|     213.586|   0.1%/534|   0.1%/662|   0.1%/704|   0.1%/751 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 273   |    1368|     209.446|   0.2%/385|   0.2%/432|   0.2%/446|   0.2%/461 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 273   |     641|     336.384|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 275   |    1488|     217.956|   1.1%/ 63|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 272   |      83|      18.599|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 274   |    1490|     216.868|   0.7%/106|   0.6%/112|   0.6%/114|   0.6%/116 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 275   |    1496|     535.395|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 229   |     262|       9.996|   0.1%/811|   0.1%/887|   0.1%/911|   0.1%/938 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 275   |     479|      14.615|   0.7%/103|   0.6%/112|   0.6%/114|   0.6%/116 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 275   |     258|      12.734|   1.7%/ 42|   1.8%/ 38|   1.8%/ 38|   1.9%/ 37 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 275   |     336|      82.406|   1.6%/ 43|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 275   |  125372|     990.475|   0.5%/127|   0.5%/126|   0.5%/126|   0.6%/126 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 275   |    3008|    1121.485|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 275   |    7721|     215.240|   0.6%/126|   0.5%/153|   0.4%/162|   0.4%/172 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 221   |     163|       5.420|   0.9%/ 80|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)| 175   |     197|      80.303|   1.2%/ 57|   1.4%/ 51|   1.4%/ 50|   1.4%/ 48 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 230   |    1935|      64.515|   0.4%/157|   0.3%/224|   0.3%/250|   0.2%/284 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 275   |   11383|     652.071|   0.6%/122|   0.6%/125|   0.6%/125|   0.5%/126 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 275   |      25|       5.021|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 275   |     165|      25.512|   0.1%/691|   0.1%/675|   0.1%/671|   0.1%/667 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 275   |      87|       3.910|   0.8%/ 89|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 275   |    1251|       6.068|   0.4%/181|   0.4%/162|   0.4%/158|   0.4%/154 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 275   |    2679|    1289.988|   0.9%/ 76|   0.8%/ 88|   0.8%/ 91|   0.7%/ 95 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 275   |     441|      82.112|   0.9%/ 81|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 275   |    1525|     327.006|   0.1%/696|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 275   |   10176|      46.395|   0.8%/ 85|   0.8%/ 82|   0.8%/ 82|   0.9%/ 81 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 275   |    3862|     915.452|   1.0%/ 69|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)| 158   |       9|       1.045|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 275   |    2263|     316.362|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 275   |   37613|    1170.602|   0.2%/447|   0.2%/442|   0.2%/441|   0.2%/439 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 275   |    9300|      85.699|   0.3%/248|   0.3%/266|   0.3%/271|   0.3%/276 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 275   |   49479|    1289.210|   1.1%/ 62|   0.9%/ 80|   0.8%/ 85|   0.7%/ 92 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 275   |    7389|     718.977|   1.2%/ 58|   1.1%/ 62|   1.1%/ 63|   1.1%/ 65 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 275   |     245|      89.234|   0.1%/668|   0.1%/663|   0.1%/661|   0.1%/660 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 275   |   16549|     852.832|   0.9%/ 78|   0.8%/ 87|   0.8%/ 89|   0.8%/ 92 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 275   |   57014|     388.525|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 216   |      75|       6.028|   2.3%/ 31|   2.5%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 275   |    6260|     182.931|   0.1%/464|   0.1%/513|   0.1%/526|   0.1%/540 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 275   |     385|      23.750|   0.8%/ 85|   0.9%/ 76|   0.9%/ 74|   1.0%/ 73 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 275   |    3515|     504.749|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 253   |      76|       9.603|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 275   |      29|       5.130|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 275   |    2136|     391.522|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 32 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 275   |    4499|    2148.416|   1.3%/ 52|   1.0%/ 72|   0.9%/ 79|   0.8%/ 88 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 268   |     130|       8.182|   0.2%/335|   0.2%/296|   0.2%/287|   0.2%/278 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 275   |   26786|     455.740|   1.1%/ 64|   1.2%/ 59|   1.2%/ 58|   1.2%/ 56 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 275   |   51648|    1096.550|   0.3%/203|   0.3%/215|   0.3%/218|   0.3%/222 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 275   |     238|      10.908|   1.0%/ 73|   0.5%/136|   0.4%/173|   0.3%/238 |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 275   |    1512|      35.636|   0.5%/129|   0.5%/129|   0.5%/129|   0.5%/130 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 275   |    8639|     835.579|   0.9%/ 80|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 275   |    8418|     978.360|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 275   |     711|      40.651|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 275   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 275   |      60|       0.903|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 275   |      69|       9.099|   0.1%/612|   0.1%/805|   0.1%/871|   0.1%/947 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 275   |     127|      93.394|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 275   |    4756|     405.736|   0.9%/ 79|   0.7%/ 97|   0.7%/102|   0.6%/108 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 275   |   20827|     250.457|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 275   |  343263|    1041.630|   0.8%/ 82|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)| 161   |     255|       6.320|   0.7%/101|   0.7%/106|   0.6%/107|   0.6%/109 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 275   |   20329|     485.413|   1.1%/ 60|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 275   |     671|      67.880|   0.5%/147|   0.5%/149|   0.5%/149|   0.5%/150 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 275   |   73281|    1103.041|   0.7%/100|   0.7%/101|   0.7%/102|   0.7%/102 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 275   |     115|      32.560|   3.5%/ 20|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 275   |     617|      18.069|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 275   |    1032|      32.032|   0.4%/161|   0.4%/161|   0.4%/161|   0.4%/161 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)| 154   |      35|       0.364|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 274   |     383|      21.435|   0.3%/241|   0.3%/222|   0.3%/218|   0.3%/214 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 275   |     352|      23.215|   0.7%/ 93|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83 |

