# State and Country COVID-19 Analysis #
## Updated: at 2020-09-03 for data as of 2020-09-02 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.0% of deaths and 57.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 155   |   32973|    1694.972|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 155   |   15959|    1796.773|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 155   |   13453|     340.474|   0.9%/ 74|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 155   |   13581|     468.372|   1.3%/ 54|   1.1%/ 64|   1.0%/ 68|   1.0%/ 71 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 155   |   11796|     549.200|   1.1%/ 62|   0.9%/ 78|   0.8%/ 83|   0.8%/ 89 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 155   |    9085|    1307.283|   0.2%/441|   0.2%/451|   0.2%/454|   0.2%/457 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 155   |    8289|     654.162|   0.2%/292|   0.2%/288|   0.2%/287|   0.2%/287 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 155   |    7713|     602.506|   0.2%/368|   0.2%/393|   0.2%/400|   0.2%/408 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 155   |    6769|     677.776|   0.2%/401|   0.2%/379|   0.2%/374|   0.2%/369 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 155   |    5836|     549.619|   1.2%/ 56|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 155   |  186602|     566.242|   0.5%/139|   0.5%/152|   0.4%/155|   0.4%/159 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 155   |  124486|     588.830|   0.8%/ 91|   0.7%/ 98|   0.7%/100|   0.7%/103 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 155   |   68314|      50.186|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 155   |   66289|     523.700|   0.8%/ 83|   0.8%/ 92|   0.7%/ 95|   0.7%/ 98 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 155   |   41344|     622.319|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 155   |   35535|     589.898|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 155   |   30663|     457.136|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 155   |   29132|     618.509|   0.1%/668|   0.1%/586|   0.1%/568|   0.1%/551 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 155   |   30490|     948.930|   0.6%/112|   0.5%/128|   0.5%/133|   0.5%/138 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 155   |   22043|     264.372|   0.6%/118|   0.5%/140|   0.5%/147|   0.4%/154 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 155   |    2213|     451.409|   0.9%/ 78|   0.9%/ 81|   0.8%/ 82|   0.8%/ 82 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 155   |      39|      53.413|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 155   |    5174|     710.775|   0.7%/104|   0.5%/133|   0.5%/144|   0.4%/155 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 155   |     825|     273.430|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 155   |   13453|     340.474|   0.9%/ 74|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 155   |    1954|     339.291|   0.2%/390|   0.2%/409|   0.2%/414|   0.2%/420 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 155   |    4470|    1253.631|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 155   |     607|     623.490|   0.1%/660|   0.1%/697|   0.1%/709|   0.1%/723 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 155   |   11796|     549.200|   1.1%/ 62|   0.9%/ 78|   0.8%/ 83|   0.8%/ 89 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 155   |    5836|     549.619|   1.2%/ 56|   1.2%/ 58|   1.2%/ 58|   1.2%/ 59 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 155   |      68|      48.004|   4.3%/ 16|   4.9%/ 14|   5.1%/ 14|   5.2%/ 13 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 155   |     381|     213.274|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 155   |    8289|     654.162|   0.2%/292|   0.2%/288|   0.2%/287|   0.2%/287 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 155   |    3334|     495.288|   0.3%/210|   0.3%/222|   0.3%/226|   0.3%/230 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 155   |    1137|     360.485|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 155   |     461|     158.229|   0.7%/100|   0.7%/104|   0.7%/106|   0.6%/107 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 155   |     957|     214.163|   0.9%/ 74|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 155   |    5062|    1088.897|   0.6%/114|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 155   |     133|      99.219|   0.2%/311|   0.2%/335|   0.2%/343|   0.2%/352 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 155   |    3771|     623.808|   0.2%/344|   0.2%/361|   0.2%/366|   0.2%/370 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 155   |    9085|    1307.283|   0.2%/441|   0.2%/451|   0.2%/454|   0.2%/457 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 155   |    6769|     677.776|   0.2%/401|   0.2%/379|   0.2%/374|   0.2%/369 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 155   |    1892|     335.497|   0.4%/173|   0.4%/185|   0.4%/188|   0.4%/192 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 155   |    2547|     855.939|   1.1%/ 64|   1.0%/ 70|   1.0%/ 71|   0.9%/ 73 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 155   |    1562|     254.582|   0.7%/ 93|   0.8%/ 88|   0.8%/ 87|   0.8%/ 85 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 155   |     109|     101.662|   1.5%/ 45|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 155   |     402|     207.887|   0.6%/123|   0.5%/129|   0.5%/130|   0.5%/132 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 155   |    1377|     446.922|   1.2%/ 60|   1.0%/ 71|   0.9%/ 75|   0.9%/ 79 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 155   |     434|     319.054|   0.1%/634|   0.1%/722|   0.1%/751|   0.1%/784 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 155   |   15959|    1796.773|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 155   |     790|     376.738|   0.6%/117|   0.6%/119|   0.6%/119|   0.6%/120 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 155   |   32973|    1694.972|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 155   |    2784|     265.433|   0.9%/ 76|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 155   |     149|     194.900|   1.0%/ 72|   0.9%/ 79|   0.8%/ 82|   0.8%/ 84 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 155   |    4200|     359.273|   0.5%/141|   0.5%/152|   0.4%/155|   0.4%/158 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 155   |     830|     209.685|   1.2%/ 59|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 155   |     471|     111.706|   1.1%/ 64|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 155   |    7713|     602.506|   0.2%/368|   0.2%/393|   0.2%/400|   0.2%/408 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 155   |     468|     146.469|   1.6%/ 43|   1.4%/ 51|   1.3%/ 54|   1.2%/ 57 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 155   |    1051|     991.640|   0.2%/419|   0.2%/386|   0.2%/379|   0.2%/372 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 155   |    2836|     550.818|   1.2%/ 60|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 155   |     170|     192.493|   0.6%/126|   0.5%/148|   0.4%/155|   0.4%/163 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 155   |    1839|     269.069|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 155   |   13581|     468.372|   1.3%/ 54|   1.1%/ 64|   1.0%/ 68|   1.0%/ 71 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 155   |  186602|     566.242|   0.5%/139|   0.5%/152|   0.4%/155|   0.4%/159 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 155   |     420|     131.034|   0.6%/110|   0.5%/140|   0.5%/151|   0.4%/164 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 155   |      58|      93.061|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 155   |    2608|     305.558|   0.6%/121|   0.6%/114|   0.6%/112|   0.6%/110 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 155   |    1958|     257.115|   0.5%/149|   0.4%/181|   0.4%/192|   0.3%/203 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 155   |     225|     125.457|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 29 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 155   |    1143|     196.321|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/150 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 143   |      40|      69.192|   0.1%/476|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 155   |    1421|      44.087|   0.2%/449|   0.1%/871|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 155   |     295|     103.807|   1.6%/ 43|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 155   |    1534|      35.667|   0.6%/111|   0.6%/119|   0.6%/121|   0.6%/123 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 155   |     116|       3.723|   1.3%/ 53|   1.0%/ 72|   0.9%/ 79|   0.8%/ 88 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 155   |    9383|     208.790|   2.6%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 155   |     890|     300.978|   0.4%/167|   0.4%/190|   0.4%/197|   0.3%/204 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 155   |     725|      28.214|   2.9%/ 24|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 155   |     736|      82.657|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 155   |     538|      53.460|   0.4%/197|   0.3%/228|   0.3%/236|   0.3%/244 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 155   |     195|     126.580|   0.5%/130|   0.4%/179|   0.3%/198|   0.3%/223 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 155   |    4378|      25.987|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 155   |     688|      73.165|   0.7%/ 94|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 155   |    9916|     860.420|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 150   |      40|       3.429|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 155   |    5226|     455.618|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 155   |     641|     194.063|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 155   |       5|       2.026|   6.9%/ 10|   8.5%/  8|   9.0%/  8|   9.4%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 155   |  124486|     588.830|   0.8%/ 91|   0.7%/ 98|   0.7%/100|   0.7%/103 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 155   |     646|      92.987|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 155   |      55|       2.649|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 143   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 155   |     415|      15.641|   0.2%/427|   0.1%/483|   0.1%/501|   0.1%/521 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 155   |    9185|     241.727|   0.1%/993|   0.1%/995|   0.1%/996|   0.1%/997 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 103   |      62|      11.205|   0.1%/474|   0.2%/281|   0.3%/253|   0.3%/228 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 128   |      77|       4.746|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 155   |   11411|     597.218|   0.5%/144|   0.5%/153|   0.4%/155|   0.4%/157 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 155   |    4727|       3.371|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 155   |   20715|     419.361|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 155   |     469|      92.713|   2.4%/ 28|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 155   |     187|      45.838|   0.9%/ 79|   1.0%/ 73|   1.0%/ 71|   1.0%/ 70 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 155   |      94|       8.358|   0.5%/140|   0.6%/112|   0.6%/107|   0.7%/102 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 155   |     625|     107.378|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 155   |    1761|     169.969|   1.2%/ 59|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 155   |    6623|     379.118|   0.5%/144|   0.5%/141|   0.5%/140|   0.5%/140 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 155   |    5456|      54.416|   0.3%/202|   0.3%/208|   0.3%/209|   0.3%/210 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 155   |     746|     115.085|   1.0%/ 69|   0.8%/ 85|   0.8%/ 90|   0.7%/ 96 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 134   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 151   |     889|       9.009|   2.6%/ 26|   2.3%/ 30|   2.2%/ 32|   2.1%/ 33 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 155   |     336|      60.805|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 155   |   30663|     457.136|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 155   |      54|      24.653|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 155   |     169|      71.805|   2.2%/ 31|   0.0%/ --|   0.0%/ --|   0.3%/200 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 152   |      19|       5.121|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 155   |    9319|     112.073|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 155   |     290|       9.567|   0.8%/ 88|   0.5%/131|   0.5%/150|   0.4%/177 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 155   |     269|      25.095|   1.1%/ 63|   1.2%/ 57|   1.2%/ 55|   1.3%/ 54 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 155   |    2847|     171.451|   0.9%/ 79|   0.8%/ 91|   0.7%/ 95|   0.7%/ 99 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 141   |      60|       4.905|   0.8%/ 84|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 130   |      35|      21.758|   0.2%/324|   0.2%/450|   0.1%/492|   0.1%/542 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 151   |     206|      17.758|   0.3%/225|   0.2%/424|   0.1%/533|   0.1%/708 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 155   |    1894|     206.818|   1.2%/ 59|   1.2%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 155   |     618|      63.186|   0.1%/795|   0.1%/866|   0.1%/886|   0.1%/907 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 155   |   68314|      50.186|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 155   |    7574|      28.376|   1.3%/ 55|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 155   |   22043|     264.372|   0.6%/118|   0.5%/140|   0.5%/147|   0.4%/154 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 155   |    7250|     185.292|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 155   |    1779|     361.407|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 155   |     991|     107.857|   1.6%/ 44|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 155   |   35535|     589.898|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 155   |      21|       7.843|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 155   |    1316|      10.452|   1.1%/ 64|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 155   |      16|       1.464|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 155   |    1651|      88.353|   1.1%/ 66|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 155   |     611|      12.846|   1.0%/ 71|   0.7%/103|   0.6%/117|   0.5%/134 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 155   |     535|     297.948|   1.0%/ 71|   0.4%/164|   0.3%/246|   0.1%/490 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 152   |     539|     121.832|   0.4%/173|   0.3%/200|   0.3%/208|   0.3%/217 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 153   |     994|     152.183|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 153   |      34|      17.883|   0.3%/247|   0.3%/224|   0.3%/219|   0.3%/215 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 155   |     176|      25.856|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 152   |      83|      18.488|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 154   |     261|      37.936|   2.9%/ 24|   2.5%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 155   |      86|      30.950|   0.3%/238|   0.3%/215|   0.3%/210|   0.3%/206 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 109   |     196|       7.449|   0.9%/ 74|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 155   |     125|       3.828|   0.1%/ ***|   0.1%/763|   0.1%/709|   0.1%/660 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 155   |     126|       6.222|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 155   |     159|      38.976|   0.1%/744|   0.1%/600|   0.1%/572|   0.1%/546 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 155   |   66289|     523.700|   0.8%/ 83|   0.8%/ 92|   0.7%/ 95|   0.7%/ 98 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 155   |    1019|     379.824|   0.7%/ 94|   0.7%/ 97|   0.7%/ 97|   0.7%/ 98 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 155   |    1286|      35.854|   3.5%/ 20|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 101   |      24|       0.782|   1.6%/ 44|   2.0%/ 35|   2.1%/ 33|   2.2%/ 31 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  55   |      83|      33.798|   5.6%/ 12|   4.9%/ 14|   4.9%/ 14|   4.8%/ 14 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 110   |     252|       8.396|   5.3%/ 13|   5.4%/ 13|   5.4%/ 13|   5.5%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 155   |    6263|     358.747|   0.1%/ ***|   0.1%/ ***|   0.1%/988|   0.1%/970 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 155   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 155   |     141|      21.779|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 155   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 155   |    1031|       5.002|   0.3%/276|   0.2%/391|   0.2%/436|   0.1%/491 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 155   |     606|     291.931|   0.7%/104|   0.7%/101|   0.7%/100|   0.7%/100 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 155   |     266|      49.536|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 155   |     703|     150.649|   1.1%/ 61|   1.0%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 155   |    6331|      28.865|   0.1%/544|   0.1%/669|   0.1%/710|   0.1%/755 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 155   |    2061|     488.501|   0.8%/ 91|   0.6%/110|   0.6%/116|   0.6%/122 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  38   |       5|       0.568|   3.0%/ 23|   2.7%/ 25|   0.9%/ 76|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 155   |     383|      53.479|   5.9%/ 12|   5.9%/ 12|   5.9%/ 12|   5.9%/ 12 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 155   |   30490|     948.930|   0.6%/112|   0.5%/128|   0.5%/133|   0.5%/138 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 155   |    3662|      33.746|   2.1%/ 33|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 155   |    2074|      54.039|   0.6%/121|   0.6%/123|   0.6%/123|   0.6%/123 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 155   |    1828|     177.927|   0.2%/422|   0.2%/430|   0.2%/433|   0.2%/435 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 155   |     199|      72.531|   0.2%/334|   0.1%/535|   0.1%/621|   0.1%/734 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 155   |    3746|     193.034|   1.3%/ 54|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 155   |   17403|     118.591|   0.6%/115|   0.6%/121|   0.6%/122|   0.6%/124 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  96   |      18|       1.469|   2.3%/ 30|   0.0%/ --|   0.0%/ --|   2.0%/ 34 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 155   |    3998|     116.833|   0.9%/ 80|   0.8%/ 86|   0.8%/ 88|   0.8%/ 90 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 155   |     292|      18.042|   0.7%/ 97|   0.6%/122|   0.5%/130|   0.5%/140 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 155   |     728|     104.598|   0.3%/222|   0.2%/417|   0.1%/531|   0.1%/731 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 133   |      70|       8.900|   0.2%/377|   0.2%/304|   0.2%/288|   0.3%/272 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 155   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 155   |      34|       6.168|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 155   |     134|      64.208|   0.1%/506|   0.1%/946|   0.1%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 148   |      97|       6.090|   0.4%/181|   0.5%/138|   0.5%/130|   0.6%/123 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 155   |   14877|     253.124|   1.1%/ 65|   0.8%/ 91|   0.7%/101|   0.6%/113 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 155   |   29132|     618.509|   0.1%/668|   0.1%/586|   0.1%/568|   0.1%/551 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 155   |      12|       0.558|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 155   |     833|      19.628|   0.1%/483|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 155   |    5829|     563.792|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 155   |    2009|     233.554|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 155   |     123|       7.050|   3.0%/ 23|   3.1%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 155   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 155   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 155   |      29|       3.831|   0.5%/146|   0.2%/425|   0.1%/729|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 155   |      24|      17.860|   6.6%/ 10|   7.6%/  9|   7.9%/  9|   8.2%/  8 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 155   |      80|       6.864|   1.5%/ 47|   1.7%/ 41|   1.7%/ 39|   1.8%/ 38 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 155   |    6346|      76.314|   0.5%/152|   0.5%/137|   0.5%/134|   0.5%/130 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 155   |  186602|     566.242|   0.5%/139|   0.5%/152|   0.4%/155|   0.4%/159 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  41   |      33|       0.813|   6.4%/ 11|   3.3%/ 21|   2.9%/ 24|   2.5%/ 28 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 155   |    2670|      63.758|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 155   |     386|      39.021|   0.4%/189|   0.4%/179|   0.4%/177|   0.4%/175 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 155   |   41344|     622.319|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 155   |      45|      12.788|   0.7%/ 99|   0.7%/104|   0.7%/106|   0.6%/108 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 155   |     339|       9.925|   2.0%/ 35|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 155   |     416|      12.907|   2.0%/ 34|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  34   |      35|       0.359|   3.3%/ 21|   2.4%/ 29|   2.3%/ 31|   2.1%/ 33 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 154   |     307|      17.152|   0.6%/116|   0.4%/180|   0.3%/209|   0.3%/249 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 155   |     217|      14.318|   2.2%/ 31|   1.6%/ 44|   1.4%/ 49|   1.3%/ 55 |

