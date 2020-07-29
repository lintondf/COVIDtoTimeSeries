# State and Country COVID-19 Analysis #
## Updated: at 2020-07-29 for data as of 2020-07-28 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.8% of deaths and 39.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.3% of deaths and 56.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 119   |   32670|    1679.365|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 119   |   15856|    1785.121|   0.1%/631|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 119   |    8690|     219.923|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 119   |    8559|    1231.581|   0.2%/402|   0.2%/445|   0.2%/456|   0.1%/468 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 119   |    7645|     603.329|   0.2%/340|   0.2%/423|   0.2%/447|   0.1%/474 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 119   |    7170|     560.034|   0.2%/322|   0.2%/377|   0.2%/394|   0.2%/412 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 119   |    6427|     643.566|   0.1%/705|   0.1%/990|   0.1%/ ***|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 119   |    6122|     285.027|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 119   |    5395|     186.068|   3.9%/ 18|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 119   |    4428|    1242.091|   0.1%/901|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 119   |  148708|     451.253|   0.6%/112|   0.7%/106|   0.7%/105|   0.7%/104 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 119   |   89527|     423.474|   1.3%/ 54|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 119   |   45992|     692.281|   0.1%/493|   0.1%/552|   0.1%/569|   0.1%/587 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 119   |   45072|     356.080|   1.5%/ 45|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 119   |   35138|     583.314|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 119   |   34289|      25.190|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 119   |   30249|     450.964|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 119   |   28438|     603.775|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 119   |   18845|     586.506|   1.2%/ 56|   1.1%/ 65|   1.0%/ 68|   1.0%/ 71 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 119   |   16173|     193.979|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 119   |    1520|     310.101|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 119   |      20|      27.852|   1.7%/ 40|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 119   |    3503|     481.278|   2.7%/ 26|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 119   |     419|     138.678|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 119   |    8690|     219.923|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 119   |    1805|     313.420|   0.3%/242|   0.3%/230|   0.3%/227|   0.3%/224 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 119   |    4428|    1242.091|   0.1%/901|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 119   |     570|     585.096|   0.2%/443|   0.2%/447|   0.2%/449|   0.2%/451 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 119   |    6122|     285.027|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 119   |    3531|     332.589|   1.1%/ 63|   1.2%/ 56|   1.3%/ 55|   1.3%/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 119   |      27|      19.045|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 119   |     155|      86.517|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 119   |    7645|     603.329|   0.2%/340|   0.2%/423|   0.2%/447|   0.1%/474 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 119   |    2921|     433.926|   0.4%/195|   0.4%/192|   0.4%/191|   0.4%/190 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 119   |     844|     267.563|   0.7%/106|   0.6%/109|   0.6%/110|   0.6%/111 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 119   |     336|     115.283|   0.8%/ 83|   0.9%/ 75|   1.0%/ 73|   1.0%/ 71 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 119   |     715|     160.060|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 119   |    3795|     816.368|   0.6%/107|   0.7%/ 98|   0.7%/ 95|   0.7%/ 93 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 119   |     121|      89.732|   0.4%/185|   0.3%/230|   0.3%/245|   0.3%/262 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 119   |    3459|     572.091|   0.3%/265|   0.3%/277|   0.2%/279|   0.2%/282 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 119   |    8559|    1231.581|   0.2%/402|   0.2%/445|   0.2%/456|   0.1%/468 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 119   |    6427|     643.566|   0.1%/705|   0.1%/990|   0.1%/ ***|   0.1%/ *** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 119   |    1625|     288.110|   0.3%/226|   0.3%/241|   0.3%/245|   0.3%/250 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 119   |    1532|     514.709|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 119   |    1222|     199.082|   0.8%/ 92|   0.8%/ 82|   0.9%/ 80|   0.9%/ 78 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 119   |      50|      47.015|   3.0%/ 23|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 119   |     323|     166.795|   0.6%/112|   0.6%/109|   0.6%/110|   0.6%/111 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 119   |     758|     246.187|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 119   |     410|     301.843|   0.3%/222|   0.3%/229|   0.3%/230|   0.3%/231 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 119   |   15856|    1785.121|   0.1%/631|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 119   |     622|     296.858|   0.9%/ 77|   0.9%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 119   |   32670|    1679.365|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 119   |    1863|     177.659|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 119   |     101|     132.270|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76|   0.9%/ 77 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 119   |    3359|     287.364|   0.6%/108|   0.7%/101|   0.7%/100|   0.7%/ 98 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 119   |     504|     127.449|   1.2%/ 59|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 119   |     296|      70.179|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 119   |    7170|     560.034|   0.2%/322|   0.2%/377|   0.2%/394|   0.2%/412 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 119   |     203|      63.455|   1.5%/ 47|   1.7%/ 41|   1.7%/ 40|   1.8%/ 38 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 119   |    1008|     951.080|   0.2%/448|   0.1%/568|   0.1%/609|   0.1%/657 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 119   |    1545|     299.997|   3.2%/ 21|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 119   |     126|     142.613|   0.8%/ 85|   0.6%/120|   0.5%/135|   0.5%/153 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 119   |    1003|     146.819|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 119   |    5395|     186.068|   3.9%/ 18|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 119   |  148708|     451.253|   0.6%/112|   0.7%/106|   0.7%/105|   0.7%/104 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 119   |     288|      89.897|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 119   |      56|      89.745|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 119   |    2103|     246.426|   0.4%/179|   0.3%/241|   0.3%/263|   0.2%/289 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 119   |    1517|     199.227|   0.6%/117|   0.6%/120|   0.6%/121|   0.6%/122 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 119   |     105|      58.569|   0.6%/121|   0.6%/108|   0.7%/105|   0.7%/102 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 119   |     898|     154.311|   0.6%/110|   0.7%/ 96|   0.7%/ 93|   0.8%/ 90 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 107   |      26|      45.191|   0.7%/100|   0.5%/129|   0.5%/142|   0.4%/158 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 119   |    1312|      40.715|   1.3%/ 51|   1.0%/ 70|   0.9%/ 77|   0.8%/ 86 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 119   |     145|      51.058|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 119   |    1175|      27.327|   0.9%/ 74|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 119   |      41|       1.316|   4.1%/ 17|   4.7%/ 15|   4.8%/ 14|   5.0%/ 14 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 119   |    3149|      70.081|   3.4%/ 21|   3.5%/ 20|   3.5%/ 19|   3.6%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 119   |     737|     249.056|   1.5%/ 47|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 119   |     140|       5.442|   3.2%/ 21|   4.2%/ 16|   4.4%/ 15|   4.7%/ 15 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 119   |     713|      80.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 119   |     437|      43.364|   2.2%/ 32|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 119   |     145|      94.170|   1.6%/ 43|   1.4%/ 48|   1.4%/ 49|   1.4%/ 51 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 119   |    3021|      17.932|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 119   |     546|      58.002|   1.0%/ 70|   0.9%/ 77|   0.9%/ 79|   0.9%/ 81 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 119   |    9827|     852.690|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 114   |      37|       3.156|   2.0%/ 34|   1.5%/ 45|   1.4%/ 49|   1.3%/ 55 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 119   |    2739|     238.767|   2.6%/ 26|   2.4%/ 28|   2.4%/ 29|   2.3%/ 29 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 119   |     297|      89.934|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 119   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 119   |   89527|     423.474|   1.3%/ 54|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 119   |     353|      50.843|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 119   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 107   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 119   |     393|      14.821|   0.5%/140|   0.5%/128|   0.6%/126|   0.6%/124 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 119   |    8961|     235.816|   0.1%/833|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  67   |      60|      10.920|   1.0%/ 71|   0.8%/ 90|   0.7%/ 99|   0.6%/112 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  92   |      75|       4.620|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 119   |    9591|     501.974|   1.0%/ 68|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 119   |    4651|       3.317|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 119   |    9051|     183.235|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 119   |     123|      24.374|   8.4%/  8|   9.2%/  7|   9.4%/  7|   9.6%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 119   |     130|      31.908|   1.3%/ 55|   1.6%/ 43|   1.7%/ 41|   1.8%/ 38 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 119   |      87|       7.775|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 119   |     613|     105.324|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 119   |    1096|     105.854|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 119   |    5611|     321.186|   0.6%/114|   0.5%/132|   0.5%/137|   0.5%/143 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 119   |    4783|      47.698|   1.2%/ 58|   0.9%/ 77|   0.8%/ 84|   0.8%/ 92 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 119   |     427|      65.880|   2.9%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  98   |      51|      37.548|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 115   |     235|       2.387|   4.0%/ 17|   4.4%/ 16|   4.5%/ 15|   4.5%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 119   |     329|      59.437|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 119   |   30249|     450.964|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 119   |      49|      22.386|   0.5%/149|   0.6%/121|   0.6%/114|   0.6%/108 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 119   |       7|       2.942|   6.8%/ 10|   8.5%/  8|   9.0%/  8|   9.4%/  7 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 116   |      16|       4.336|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 119   |    9132|     109.822|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 119   |     168|       5.555|   1.5%/ 47|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 119   |     202|      18.860|   0.3%/232|   0.4%/180|   0.4%/171|   0.4%/162 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 119   |    1843|     110.974|   2.4%/ 29|   2.0%/ 35|   1.9%/ 37|   1.8%/ 39 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 105   |      45|       3.643|   1.3%/ 52|   1.6%/ 45|   1.6%/ 43|   1.7%/ 41 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  94   |      26|      16.213|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 115   |     162|      13.986|   0.9%/ 75|   0.5%/134|   0.4%/165|   0.3%/212 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 119   |    1182|     129.063|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 119   |     597|      61.090|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 119   |   34289|      25.190|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 119   |    4972|      18.629|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 119   |   16173|     193.979|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 119   |    4639|     118.551|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 119   |    1765|     358.671|   0.1%/985|   0.1%/907|   0.1%/890|   0.1%/875 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 119   |     481|      52.383|   1.9%/ 36|   2.1%/ 33|   2.1%/ 32|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 119   |   35138|     583.314|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 119   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 119   |     998|       7.921|   0.1%/569|   0.2%/458|   0.2%/435|   0.2%/414 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 119   |      11|       1.053|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 119   |     704|      37.694|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 119   |     301|       6.323|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 119   |     191|     106.588|   4.1%/ 17|   3.9%/ 18|   3.8%/ 18|   3.7%/ 18 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 116   |     438|      99.183|   0.8%/ 85|   0.9%/ 80|   0.9%/ 79|   0.9%/ 77 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 117   |     313|      47.876|   3.8%/ 18|   2.9%/ 24|   2.7%/ 26|   2.5%/ 28 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 117   |      31|      16.373|   0.1%/857|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 119   |      45|       6.635|   2.5%/ 28|   3.3%/ 21|   3.5%/ 20|   3.7%/ 19 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 116   |      78|      17.538|   0.8%/ 92|   0.2%/443|   0.0%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 118   |      65|       9.393|   3.3%/ 21|   3.6%/ 19|   3.6%/ 19|   3.7%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 119   |      80|      28.720|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  73   |      94|       3.578|   5.5%/ 12|   5.5%/ 12|   5.6%/ 12|   5.6%/ 12 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 119   |     124|       3.782|   0.1%/512|   0.2%/428|   0.2%/411|   0.2%/395 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 119   |     124|       6.107|   0.2%/397|   0.2%/389|   0.2%/383|   0.2%/377 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 119   |     159|      39.096|   0.4%/189|   0.1%/766|   0.0%/ ***|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 119   |   45072|     356.080|   1.5%/ 45|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 119   |     755|     281.495|   1.0%/ 70|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 119   |     305|       8.516|   1.7%/ 40|   2.0%/ 34|   2.1%/ 33|   2.2%/ 31 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  65   |      11|       0.376|   1.9%/ 36|   0.2%/298|   0.0%/ --|   0.0%/ -- |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  19   |       8|       3.253|  32.6%/  2|   4.6%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  74   |      48|       1.590|   1.6%/ 43|   2.4%/ 28|   2.7%/ 26|   2.9%/ 24 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 119   |    6160|     352.893|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 119   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 119   |     113|      17.477|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 119   |      69|       3.103|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 119   |     879|       4.265|   1.1%/ 63|   0.9%/ 75|   0.9%/ 79|   0.8%/ 82 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 119   |     476|     229.385|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 60 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 119   |     256|      47.660|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 119   |     407|      87.158|   2.8%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 119   |    5967|      27.207|   0.7%/105|   0.4%/167|   0.4%/195|   0.3%/235 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 119   |    1371|     325.046|   2.5%/ 28|   2.3%/ 30|   2.3%/ 31|   2.2%/ 31 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 119   |      45|       6.265|   3.8%/ 18|   4.2%/ 16|   4.3%/ 16|   4.5%/ 15 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 119   |   18845|     586.506|   1.2%/ 56|   1.1%/ 65|   1.0%/ 68|   1.0%/ 71 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 119   |    1995|      18.388|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 119   |    1686|      43.924|   0.4%/165|   0.4%/178|   0.4%/182|   0.4%/185 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 119   |    1728|     168.104|   0.2%/295|   0.2%/368|   0.2%/391|   0.2%/417 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 119   |     170|      61.741|   0.8%/ 91|   0.4%/156|   0.4%/188|   0.3%/235 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 119   |    2235|     115.163|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 119   |   13620|      92.811|   1.1%/ 64|   0.9%/ 74|   0.9%/ 76|   0.9%/ 80 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  60   |       5|       0.409|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 119   |    2834|      82.814|   1.4%/ 48|   1.2%/ 57|   1.2%/ 60|   1.1%/ 63 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 119   |     196|      12.116|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 119   |     568|      81.528|   2.0%/ 34|   1.7%/ 40|   1.6%/ 42|   1.6%/ 45 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  97   |      67|       8.432|   0.2%/296|   0.1%/636|   0.1%/955|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 119   |      27|       4.776|   0.1%/685|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 119   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 119   |     116|      55.544|   0.2%/312|   0.3%/227|   0.3%/213|   0.3%/200 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 112   |      93|       5.863|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 119   |    7239|     123.160|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 119   |   28438|     603.775|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 119   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 119   |     730|      17.210|   0.6%/107|   0.6%/121|   0.6%/126|   0.5%/130 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 119   |    5729|     554.146|   0.2%/378|   0.1%/475|   0.1%/509|   0.1%/550 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 119   |    1978|     229.852|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 119   |      43|       2.465|   8.6%/  8|   2.8%/ 25|   4.6%/ 15|   3.6%/ 19 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 119   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 119   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 119   |      17|       2.291|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 119   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 119   |      50|       4.265|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 119   |    5654|      67.988|   0.3%/216|   0.3%/229|   0.3%/232|   0.3%/236 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 119   |  148708|     451.253|   0.6%/112|   0.7%/106|   0.7%/105|   0.7%/104 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 119   |    1660|      39.639|   1.1%/ 65|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 119   |     347|      35.070|   0.3%/274|   0.2%/334|   0.2%/352|   0.2%/372 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 119   |   45992|     692.281|   0.1%/493|   0.1%/552|   0.1%/569|   0.1%/587 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 119   |      35|      10.036|   0.8%/ 83|   0.7%/ 95|   0.7%/ 99|   0.7%/103 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 119   |     131|       3.835|   4.6%/ 15|   3.8%/ 18|   3.6%/ 19|   3.4%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 119   |     153|       4.746|   3.3%/ 21|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 118   |     180|      10.079|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 119   |      38|       2.503|   5.6%/ 12|   4.3%/ 16|   4.0%/ 17|   3.6%/ 19 |

