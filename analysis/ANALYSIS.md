# State and Country COVID-19 Analysis #
## Updated: at 2020-09-26 for data as of 2020-09-25 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.4% of deaths and 38.5% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.0% of deaths and 55.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 178   |   33113|    1702.160|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 178   |   16096|    1812.126|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 178   |   15788|     544.488|   0.7%/103|   0.6%/119|   0.6%/123|   0.5%/128 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 178   |   15605|     394.937|   0.6%/112|   0.6%/122|   0.6%/125|   0.5%/127 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 178   |   13931|     648.607|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 178   |    9368|    1348.015|   0.1%/479|   0.1%/474|   0.1%/473|   0.1%/471 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 178   |    8795|     694.056|   0.3%/271|   0.3%/270|   0.3%/270|   0.3%/270 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 178   |    8038|     627.887|   0.2%/309|   0.2%/290|   0.2%/285|   0.2%/280 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 178   |    7038|     704.774|   0.1%/496|   0.1%/509|   0.1%/512|   0.1%/516 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 178   |    6921|     651.861|   0.7%/102|   0.6%/115|   0.6%/119|   0.6%/122 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 178   |  203922|     618.799|   0.4%/177|   0.4%/184|   0.4%/185|   0.4%/187 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 178   |  141048|     667.170|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/149 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 178   |   93240|      68.497|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.2%/ 55 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 178   |   76238|     602.301|   0.6%/118|   0.5%/126|   0.5%/129|   0.5%/131 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 178   |   41941|     631.305|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 178   |   35761|     593.655|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 178   |   32087|     998.633|   0.4%/189|   0.3%/211|   0.3%/217|   0.3%/224 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 178   |   31378|     467.793|   0.2%/437|   0.2%/377|   0.2%/364|   0.2%/352 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 178   |   30931|     656.712|   0.2%/283|   0.3%/258|   0.3%/253|   0.3%/248 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 178   |   25022|     300.109|   0.7%/104|   0.7%/ 99|   0.7%/ 98|   0.7%/ 97 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 178   |    2523|     514.535|   0.5%/133|   0.5%/148|   0.5%/152|   0.4%/157 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 178   |      48|      65.826|   0.4%/162|   0.3%/247|   0.2%/286|   0.2%/338 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 178   |    5600|     769.358|   0.4%/193|   0.3%/218|   0.3%/225|   0.3%/232 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 178   |    1285|     425.667|   1.1%/ 65|   0.9%/ 76|   0.9%/ 79|   0.8%/ 83 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 178   |   15605|     394.937|   0.6%/112|   0.6%/122|   0.6%/125|   0.5%/127 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 178   |    2034|     353.253|   0.2%/374|   0.2%/370|   0.2%/368|   0.2%/367 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 178   |    4499|    1261.841|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 178   |     628|     645.020|   0.2%/338|   0.2%/302|   0.2%/294|   0.2%/286 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 178   |   13931|     648.607|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 178   |    6921|     651.861|   0.7%/102|   0.6%/115|   0.6%/119|   0.6%/122 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 178   |     136|      95.975|   1.6%/ 43|   1.2%/ 58|   1.1%/ 64|   1.0%/ 70 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 178   |     470|     262.981|   0.8%/ 87|   0.7%/104|   0.6%/110|   0.6%/115 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 178   |    8795|     694.056|   0.3%/271|   0.3%/270|   0.3%/270|   0.3%/270 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 178   |    3561|     529.010|   0.3%/239|   0.3%/244|   0.3%/245|   0.3%/246 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 178   |    1320|     418.351|   0.6%/118|   0.5%/127|   0.5%/129|   0.5%/131 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 178   |     632|     216.863|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 178   |    1158|     259.217|   0.7%/100|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 178   |    5476|    1177.955|   0.3%/210|   0.3%/237|   0.3%/245|   0.3%/254 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 178   |     140|     104.402|   0.2%/282|   0.3%/273|   0.3%/271|   0.3%/269 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 178   |    3916|     647.769|   0.2%/427|   0.2%/441|   0.2%/445|   0.2%/448 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 178   |    9368|    1348.015|   0.1%/479|   0.1%/474|   0.1%/473|   0.1%/471 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 178   |    7038|     704.774|   0.1%/496|   0.1%/509|   0.1%/512|   0.1%/516 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 178   |    2052|     363.941|   0.4%/196|   0.3%/200|   0.3%/201|   0.3%/202 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 178   |    2921|     981.341|   0.6%/121|   0.5%/134|   0.5%/138|   0.5%/142 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 178   |    1934|     315.067|   1.0%/ 71|   1.0%/ 67|   1.0%/ 66|   1.1%/ 65 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 178   |     170|     158.951|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 178   |     465|     240.429|   0.6%/107|   0.7%/103|   0.7%/102|   0.7%/101 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 178   |    1593|     517.200|   0.6%/111|   0.5%/127|   0.5%/132|   0.5%/137 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 178   |     439|     323.056|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 178   |   16096|    1812.126|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 178   |     867|     413.306|   0.4%/181|   0.4%/194|   0.4%/197|   0.3%/200 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 178   |   33113|    1702.160|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 178   |    3395|     323.711|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83|   0.8%/ 83 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 178   |     203|     266.340|   1.9%/ 36|   2.2%/ 32|   2.2%/ 31|   2.3%/ 30 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 178   |    4738|     405.297|   0.5%/130|   0.5%/129|   0.5%/129|   0.5%/129 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 178   |     994|     251.140|   0.8%/ 89|   0.7%/ 95|   0.7%/ 97|   0.7%/ 98 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 178   |     550|     130.283|   0.6%/119|   0.5%/137|   0.5%/142|   0.5%/148 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 178   |    8038|     627.887|   0.2%/309|   0.2%/290|   0.2%/285|   0.2%/280 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 178   |     649|     203.252|   1.4%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 178   |    1103|    1041.134|   0.3%/271|   0.3%/249|   0.3%/244|   0.3%/239 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 178   |    3346|     649.955|   0.7%/106|   0.6%/122|   0.5%/126|   0.5%/131 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 178   |     207|     233.815|   1.2%/ 59|   1.3%/ 53|   1.3%/ 52|   1.4%/ 50 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 178   |    2367|     346.330|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 178   |   15788|     544.488|   0.7%/103|   0.6%/119|   0.6%/123|   0.5%/128 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 178   |  203922|     618.799|   0.4%/177|   0.4%/184|   0.4%/185|   0.4%/187 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 178   |     451|     140.583|   0.3%/261|   0.2%/345|   0.2%/374|   0.2%/408 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 178   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 178   |    3090|     362.061|   0.8%/ 85|   0.9%/ 78|   0.9%/ 77|   0.9%/ 75 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 178   |    2086|     273.873|   0.4%/186|   0.4%/182|   0.4%/181|   0.4%/180 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 178   |     340|     189.609|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 178   |    1277|     219.242|   0.4%/155|   0.4%/163|   0.4%/165|   0.4%/167 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 166   |      51|      87.884|   0.2%/399|   0.2%/337|   0.2%/324|   0.2%/310 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 178   |    1449|      44.972|   0.1%/485|   0.1%/464|   0.2%/458|   0.2%/453 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 178   |     383|     134.409|   0.9%/ 75|   0.8%/ 88|   0.8%/ 92|   0.7%/ 96 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 178   |    1717|      39.940|   0.5%/145|   0.5%/152|   0.5%/154|   0.4%/156 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 178   |     164|       5.267|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 178   |   14887|     331.269|   2.2%/ 31|   2.3%/ 31|   2.3%/ 31|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 178   |     948|     320.621|   0.3%/242|   0.3%/256|   0.3%/259|   0.3%/262 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 178   |     939|      36.544|   0.5%/126|   0.2%/335|   0.1%/559|   0.0%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 178   |     772|      86.772|   0.3%/226|   0.4%/192|   0.4%/185|   0.4%/178 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 178   |     586|      58.207|   0.3%/215|   0.3%/231|   0.3%/235|   0.3%/240 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 178   |     232|     150.320|   0.9%/ 75|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 178   |    5146|      30.544|   0.6%/108|   0.6%/118|   0.6%/121|   0.6%/124 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 178   |     811|      86.161|   0.7%/106|   0.6%/110|   0.6%/111|   0.6%/112 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 178   |    9962|     864.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 173   |      40|       3.416|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 178   |    8315|     724.957|   0.5%/129|   0.4%/184|   0.3%/205|   0.3%/232 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 178   |     811|     245.685|   1.1%/ 64|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 178   |      17|       7.425|   3.7%/ 19|   2.9%/ 24|   2.7%/ 25|   2.5%/ 27 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 178   |  141048|     667.170|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/149 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 178   |     806|     115.896|   0.8%/ 91|   0.6%/108|   0.6%/114|   0.6%/120 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 178   |      56|       2.696|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 166   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 178   |     417|      15.727|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 178   |    9296|     244.630|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/986 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 126   |      62|      11.283|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 151   |      82|       5.075|   0.2%/425|   0.2%/356|   0.2%/343|   0.2%/330 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 178   |   12539|     656.251|   0.4%/180|   0.4%/190|   0.4%/192|   0.4%/195 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 178   |    4746|       3.384|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 178   |   25678|     519.845|   0.8%/ 86|   0.7%/105|   0.6%/111|   0.6%/118 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 178   |     816|     161.316|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 178   |     264|      64.883|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 178   |     119|      10.614|   0.8%/ 82|   0.9%/ 79|   0.9%/ 79|   0.9%/ 78 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 178   |     640|     109.898|   0.2%/387|   0.2%/329|   0.2%/316|   0.2%/305 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 178   |    2160|     208.541|   0.6%/120|   0.4%/159|   0.4%/174|   0.4%/191 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 178   |    7365|     421.614|   0.3%/234|   0.3%/274|   0.2%/286|   0.2%/300 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 178   |    5861|      58.452|   0.3%/230|   0.3%/236|   0.3%/237|   0.3%/239 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 178   |     839|     129.299|   0.4%/163|   0.3%/214|   0.3%/231|   0.3%/252 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 157   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 174   |    1195|      12.114|   1.2%/ 59|   1.0%/ 72|   0.9%/ 76|   0.9%/ 80 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 178   |     341|      61.721|   0.1%/550|   0.1%/462|   0.2%/444|   0.2%/426 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 178   |   31378|     467.793|   0.2%/437|   0.2%/377|   0.2%/364|   0.2%/352 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 178   |      54|      24.656|   0.1%/530|   0.2%/413|   0.2%/390|   0.2%/369 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 178   |     111|      47.323|   0.4%/167|   0.3%/245|   0.3%/273|   0.2%/308 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 175   |      19|       5.194|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 178   |    9419|     113.282|   0.1%/ ***|   0.1%/919|   0.1%/895|   0.1%/871 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 178   |     302|       9.978|   0.3%/251|   0.2%/308|   0.2%/326|   0.2%/347 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 178   |     358|      33.395|   1.5%/ 47|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 178   |    3196|     192.475|   0.6%/124|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 164   |      66|       5.371|   0.3%/260|   0.2%/389|   0.2%/439|   0.1%/502 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 153   |      40|      25.031|   0.1%/812|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 174   |     228|      19.683|   0.4%/182|   0.4%/196|   0.3%/200|   0.3%/204 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 178   |    2280|     248.918|   0.7%/106|   0.6%/121|   0.6%/126|   0.5%/130 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 178   |     651|      66.640|   0.8%/ 84|   1.0%/ 70|   1.0%/ 67|   1.1%/ 65 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 178   |   93240|      68.497|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.2%/ 55 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 178   |   10209|      38.247|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 178   |   25022|     300.109|   0.7%/104|   0.7%/ 99|   0.7%/ 98|   0.7%/ 97 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 178   |    8974|     229.343|   0.9%/ 81|   0.8%/ 87|   0.8%/ 88|   0.8%/ 90 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 178   |    1794|     364.594|   0.1%/ ***|   0.1%/998|   0.1%/963|   0.1%/931 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 178   |    1347|     146.608|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 178   |   35761|     593.655|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 178   |      80|      29.424|   5.4%/ 13|   5.5%/ 12|   5.6%/ 12|   5.6%/ 12 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 178   |    1574|      12.495|   0.6%/121|   0.5%/145|   0.5%/153|   0.4%/162 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 178   |      36|       3.383|   4.3%/ 16|   4.7%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 178   |    1722|      92.170|   0.3%/238|   0.2%/315|   0.2%/341|   0.2%/373 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 178   |     673|      14.144|   0.6%/108|   0.6%/107|   0.6%/107|   0.6%/107 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 178   |     492|     273.837|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 175   |     595|     134.627|   0.5%/147|   0.5%/143|   0.5%/143|   0.5%/142 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 176   |    1059|     162.148|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 176   |      36|      19.032|   0.2%/419|   0.1%/513|   0.1%/544|   0.1%/579 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 178   |     342|      50.162|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 175   |      82|      18.323|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 177   |     509|      74.027|   2.6%/ 27|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 178   |      88|      31.441|   0.1%/558|   0.1%/529|   0.1%/520|   0.1%/509 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 132   |     229|       8.734|   0.6%/107|   0.6%/114|   0.6%/115|   0.6%/117 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 178   |     131|       3.989|   0.1%/940|   0.1%/782|   0.1%/748|   0.1%/715 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 178   |     129|       6.391|   0.2%/453|   0.2%/403|   0.2%/392|   0.2%/381 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 178   |     162|      39.647|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 178   |   76238|     602.301|   0.6%/118|   0.5%/126|   0.5%/129|   0.5%/131 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 178   |    1260|     469.772|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 178   |    2068|      57.654|   1.9%/ 36|   1.7%/ 40|   1.6%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 124   |      51|       1.712|   3.7%/ 19|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  78   |     120|      48.872|   1.5%/ 46|   1.3%/ 54|   1.2%/ 57|   1.2%/ 59 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 133   |     469|      15.649|   2.4%/ 29|   2.1%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 178   |    6344|     363.384|   0.1%/956|   0.1%/877|   0.1%/857|   0.1%/838 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 178   |      25|       5.100|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 178   |     150|      23.228|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 178   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 178   |    1117|       5.419|   0.2%/319|   0.2%/404|   0.2%/435|   0.1%/472 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 178   |     716|     344.622|   0.8%/ 87|   0.8%/ 83|   0.8%/ 82|   0.9%/ 81 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 178   |     268|      49.844|   0.1%/627|   0.1%/509|   0.1%/486|   0.1%/464 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 178   |     889|     190.519|   1.1%/ 62|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 178   |    6455|      29.430|   0.1%/836|   0.1%/914|   0.1%/935|   0.1%/956 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 178   |    2323|     550.721|   0.5%/131|   0.5%/140|   0.5%/142|   0.5%/144 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  61   |       7|       0.810|   2.3%/ 30|   1.6%/ 44|   1.4%/ 49|   1.2%/ 57 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 178   |     800|     111.817|   3.1%/ 23|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 178   |   32087|     998.633|   0.4%/189|   0.3%/211|   0.3%/217|   0.3%/224 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 178   |    5364|      49.426|   1.2%/ 56|   1.1%/ 62|   1.1%/ 63|   1.1%/ 65 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 178   |    2361|      61.514|   0.6%/107|   0.7%/102|   0.7%/100|   0.7%/ 99 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 178   |    1927|     187.519|   0.3%/242|   0.3%/220|   0.3%/215|   0.3%/211 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 178   |     213|      77.601|   0.3%/266|   0.2%/281|   0.2%/285|   0.2%/290 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 178   |    4677|     240.998|   0.9%/ 77|   0.8%/ 83|   0.8%/ 84|   0.8%/ 86 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 178   |   19935|     135.845|   0.6%/111|   0.6%/109|   0.6%/109|   0.6%/109 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 119   |      29|       2.304|   1.4%/ 49|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 178   |    4647|     135.813|   0.7%/106|   0.6%/111|   0.6%/112|   0.6%/114 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 178   |     307|      18.955|   0.2%/341|   0.1%/512|   0.1%/582|   0.1%/674 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 178   |     749|     107.512|   0.1%/476|   0.1%/573|   0.1%/602|   0.1%/635 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 156   |      72|       9.170|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 178   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 178   |      41|       7.491|   0.8%/ 82|   1.0%/ 69|   1.0%/ 67|   1.1%/ 64 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 178   |     142|      67.954|   0.2%/305|   0.3%/264|   0.3%/254|   0.3%/245 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 171   |      98|       6.197|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 178   |   16558|     281.717|   0.5%/154|   0.4%/195|   0.3%/208|   0.3%/224 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 178   |   30931|     656.712|   0.2%/283|   0.3%/258|   0.3%/253|   0.3%/248 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 178   |      13|       0.602|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 178   |     840|      19.792|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 178   |    5877|     568.479|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 178   |    2056|     238.980|   0.1%/572|   0.1%/499|   0.1%/483|   0.1%/468 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 178   |     195|      11.126|   1.6%/ 42|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 178   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 178   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 178   |      45|       5.973|   1.2%/ 57|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 178   |      84|      61.351|   3.3%/ 21|   2.5%/ 28|   2.2%/ 31|   2.0%/ 34 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 178   |     141|      11.996|   5.0%/ 14|   5.6%/ 12|   5.8%/ 12|   5.9%/ 12 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 178   |    7798|      93.775|   0.9%/ 77|   0.9%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 178   |  203922|     618.799|   0.4%/177|   0.4%/184|   0.4%/185|   0.4%/187 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  64   |      70|       1.749|   2.3%/ 30|   2.4%/ 29|   2.5%/ 28|   2.6%/ 27 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 178   |    3919|      93.581|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 178   |     410|      41.478|   0.2%/329|   0.2%/372|   0.2%/385|   0.2%/399 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 178   |   41941|     631.305|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 178   |      47|      13.303|   0.3%/244|   0.3%/250|   0.3%/251|   0.3%/250 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 178   |     464|      13.586|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 178   |     597|      18.519|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  57   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 177   |     338|      18.908|   0.3%/211|   0.3%/241|   0.3%/251|   0.3%/261 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 178   |     238|      15.730|   0.2%/409|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

