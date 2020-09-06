# State and Country COVID-19 Analysis #
## Updated: at 2020-09-06 for data as of 2020-09-05 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.9% of deaths and 57.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 158   |   32995|    1696.066|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 158   |   15972|    1798.192|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 158   |   13813|     349.576|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 79 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 158   |   13918|     480.013|   1.2%/ 56|   1.1%/ 65|   1.0%/ 67|   1.0%/ 70 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 158   |   12090|     562.931|   1.1%/ 65|   0.9%/ 79|   0.8%/ 83|   0.8%/ 88 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 158   |    9123|    1312.807|   0.2%/461|   0.1%/479|   0.1%/485|   0.1%/490 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 158   |    8361|     659.780|   0.3%/258|   0.3%/246|   0.3%/243|   0.3%/240 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 158   |    7757|     605.892|   0.2%/353|   0.2%/366|   0.2%/370|   0.2%/374 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 158   |    6805|     681.417|   0.2%/407|   0.2%/393|   0.2%/389|   0.2%/386 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 158   |    6038|     568.721|   1.2%/ 57|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 158   |  189202|     574.133|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/151 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 158   |  127083|     601.114|   0.8%/ 92|   0.7%/ 99|   0.7%/100|   0.7%/102 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 158   |   71395|      52.449|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 158   |   67786|     535.529|   0.8%/ 84|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 158   |   41291|     621.521|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 158   |   35551|     590.172|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 158   |   30721|     458.000|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 158   |   30706|     955.647|   0.6%/123|   0.5%/141|   0.5%/146|   0.5%/152 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 158   |   29250|     621.010|   0.1%/494|   0.2%/423|   0.2%/408|   0.2%/394 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 158   |   22347|     268.024|   0.6%/125|   0.5%/144|   0.5%/150|   0.4%/157 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 158   |    2274|     463.713|   0.9%/ 78|   0.9%/ 79|   0.9%/ 79|   0.9%/ 78 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 158   |      42|      56.744|   1.8%/ 39|   1.9%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 158   |    5259|     722.569|   0.7%/103|   0.6%/121|   0.5%/126|   0.5%/132 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 158   |     878|     291.063|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33|   2.1%/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 158   |   13813|     349.576|   1.0%/ 72|   0.9%/ 77|   0.9%/ 78|   0.9%/ 79 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 158   |    1965|     341.147|   0.2%/374|   0.2%/381|   0.2%/383|   0.2%/385 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 158   |    4471|    1253.979|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 158   |     609|     625.022|   0.1%/726|   0.1%/805|   0.1%/831|   0.1%/860 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 158   |   12090|     562.931|   1.1%/ 65|   0.9%/ 79|   0.8%/ 83|   0.8%/ 88 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 158   |    6038|     568.721|   1.2%/ 57|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 158   |      80|      56.798|   4.2%/ 16|   4.6%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 158   |     397|     222.190|   1.5%/ 45|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 158   |    8361|     659.780|   0.3%/258|   0.3%/246|   0.3%/243|   0.3%/240 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 158   |    3366|     499.940|   0.3%/208|   0.3%/217|   0.3%/220|   0.3%/223 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 158   |    1165|     369.402|   0.8%/ 85|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 158   |     474|     162.860|   0.9%/ 78|   0.9%/ 74|   1.0%/ 73|   1.0%/ 71 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 158   |     988|     221.224|   1.0%/ 68|   1.1%/ 64|   1.1%/ 64|   1.1%/ 63 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 158   |    5131|    1103.620|   0.5%/134|   0.4%/160|   0.4%/168|   0.4%/178 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 158   |     134|      99.918|   0.2%/280|   0.2%/290|   0.2%/294|   0.2%/297 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 158   |    3795|     627.723|   0.2%/329|   0.2%/333|   0.2%/333|   0.2%/334 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 158   |    9123|    1312.807|   0.2%/461|   0.1%/479|   0.1%/485|   0.1%/490 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 158   |    6805|     681.417|   0.2%/407|   0.2%/393|   0.2%/389|   0.2%/386 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 158   |    1913|     339.123|   0.4%/175|   0.4%/187|   0.4%/191|   0.4%/195 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 158   |    2616|     878.904|   1.0%/ 71|   0.9%/ 79|   0.8%/ 82|   0.8%/ 84 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 158   |    1604|     261.269|   0.9%/ 80|   0.9%/ 73|   1.0%/ 72|   1.0%/ 70 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 158   |     115|     107.228|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 158   |     408|     210.934|   0.5%/130|   0.5%/140|   0.5%/142|   0.5%/145 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 158   |    1415|     459.478|   1.2%/ 58|   1.1%/ 65|   1.0%/ 68|   1.0%/ 70 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 158   |     434|     319.452|   0.1%/907|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 158   |   15972|    1798.192|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 158   |     802|     382.563|   0.5%/127|   0.5%/134|   0.5%/136|   0.5%/137 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 158   |   32995|    1696.066|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 158   |    2867|     273.375|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70|   1.0%/ 71 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 158   |     153|     200.863|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 158   |    4266|     364.994|   0.6%/125|   0.5%/127|   0.5%/127|   0.5%/128 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 158   |     859|     217.128|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 158   |     484|     114.809|   1.0%/ 70|   0.9%/ 74|   0.9%/ 76|   0.9%/ 77 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 158   |    7757|     605.892|   0.2%/353|   0.2%/366|   0.2%/370|   0.2%/374 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 158   |     481|     150.753|   1.5%/ 47|   1.2%/ 57|   1.1%/ 60|   1.1%/ 64 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 158   |    1056|     996.998|   0.2%/410|   0.2%/386|   0.2%/381|   0.2%/377 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 158   |    2917|     566.596|   1.1%/ 63|   1.0%/ 71|   0.9%/ 73|   0.9%/ 76 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 158   |     173|     195.275|   0.6%/126|   0.5%/140|   0.5%/144|   0.5%/149 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 158   |    1907|     279.079|   1.4%/ 50|   1.2%/ 55|   1.2%/ 57|   1.2%/ 59 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 158   |   13918|     480.013|   1.2%/ 56|   1.1%/ 65|   1.0%/ 67|   1.0%/ 70 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 158   |  189202|     574.133|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/151 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 158   |     426|     132.928|   0.6%/110|   0.5%/133|   0.5%/140|   0.5%/148 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 158   |      58|      93.000|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 158   |    2662|     311.866|   0.6%/112|   0.7%/103|   0.7%/101|   0.7%/ 99 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 158   |    1977|     259.611|   0.4%/163|   0.3%/200|   0.3%/211|   0.3%/224 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 158   |     243|     135.820|   2.4%/ 29|   2.6%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 158   |    1162|     199.609|   0.6%/123|   0.6%/125|   0.6%/125|   0.6%/126 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 146   |      42|      72.493|   0.3%/210|   0.2%/312|   0.2%/352|   0.2%/400 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 158   |    1422|      44.120|   0.1%/630|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 158   |     310|     109.034|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 158   |    1558|      36.232|   0.6%/120|   0.5%/129|   0.5%/132|   0.5%/135 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 158   |     119|       3.833|   1.4%/ 50|   1.2%/ 60|   1.1%/ 62|   1.1%/ 65 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 158   |   10042|     223.461|   2.6%/ 27|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 158   |     899|     304.075|   0.4%/176|   0.4%/197|   0.3%/203|   0.3%/210 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 158   |     781|      30.398|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 158   |     736|      82.726|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 158   |     544|      54.064|   0.4%/183|   0.4%/189|   0.4%/190|   0.4%/191 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 158   |     198|     128.010|   0.5%/135|   0.4%/175|   0.4%/189|   0.3%/206 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 158   |    4494|      26.677|   0.9%/ 74|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 158   |     704|      74.877|   0.7%/ 93|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 158   |    9898|     858.867|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 153   |      40|       3.438|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 158   |    5441|     474.405|   1.4%/ 49|   1.4%/ 51|   1.4%/ 51|   1.3%/ 52 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 158   |     665|     201.309|   1.4%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 158   |       6|       2.624|   7.4%/  9|   8.9%/  8|   9.4%/  7|   9.8%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 158   |  127083|     601.114|   0.8%/ 92|   0.7%/ 99|   0.7%/100|   0.7%/102 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 158   |     675|      97.108|   1.5%/ 47|   1.5%/ 47|   1.5%/ 48|   1.5%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 158   |      55|       2.647|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 146   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 158   |     417|      15.695|   0.1%/484|   0.1%/580|   0.1%/610|   0.1%/642 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 158   |    9202|     242.154|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 106   |      62|      11.275|   0.1%/531|   0.2%/372|   0.2%/345|   0.2%/322 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 131   |      77|       4.754|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 158   |   11570|     605.536|   0.5%/143|   0.5%/149|   0.5%/150|   0.5%/151 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 158   |    4732|       3.374|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 158   |   21572|     436.718|   1.6%/ 44|   1.4%/ 51|   1.3%/ 52|   1.3%/ 54 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 158   |     496|      97.969|   2.3%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 158   |     194|      47.472|   1.0%/ 68|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 158   |      95|       8.459|   0.6%/117|   0.7%/ 95|   0.8%/ 91|   0.8%/ 87 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 158   |     626|     107.573|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 158   |    1827|     176.365|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 158   |    6721|     384.763|   0.5%/141|   0.5%/138|   0.5%/138|   0.5%/137 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 158   |    5512|      54.974|   0.3%/202|   0.3%/205|   0.3%/205|   0.3%/205 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 158   |     764|     117.790|   1.0%/ 72|   0.8%/ 86|   0.8%/ 90|   0.7%/ 94 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 137   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 154   |     940|       9.531|   2.4%/ 29|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 158   |     336|      60.856|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 158   |   30721|     458.000|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 158   |      54|      24.630|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 158   |     207|      88.342|   1.1%/ 65|   1.0%/ 67|   1.0%/ 67|   0.7%/101 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 155   |      19|       5.201|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 158   |    9332|     112.231|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 158   |     293|       9.679|   0.7%/ 99|   0.5%/150|   0.4%/172|   0.3%/201 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 158   |     280|      26.087|   1.1%/ 62|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 158   |    2900|     174.652|   0.8%/ 89|   0.7%/106|   0.6%/111|   0.6%/118 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 144   |      62|       5.047|   0.9%/ 75|   1.0%/ 72|   1.0%/ 71|   1.0%/ 71 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 133   |      36|      22.388|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 154   |     209|      18.076|   0.5%/130|   0.5%/128|   0.5%/127|   0.6%/125 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 158   |    1978|     216.028|   1.3%/ 53|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 158   |     620|      63.478|   0.1%/517|   0.1%/472|   0.2%/461|   0.2%/449 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 158   |   71395|      52.449|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 158   |    7893|      29.570|   1.3%/ 52|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 158   |   22347|     268.024|   0.6%/125|   0.5%/144|   0.5%/150|   0.4%/157 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 158   |    7486|     191.332|   1.1%/ 61|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 158   |    1778|     361.339|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 158   |    1038|     112.948|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 158   |   35551|     590.172|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 158   |      23|       8.442|   3.3%/ 21|   3.8%/ 18|   4.0%/ 17|   4.1%/ 17 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 158   |    1361|      10.803|   1.1%/ 65|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 158   |      16|       1.513|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 158   |    1666|      89.183|   0.8%/ 82|   0.7%/100|   0.7%/106|   0.6%/113 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 158   |     619|      13.007|   0.8%/ 85|   0.5%/132|   0.5%/153|   0.4%/183 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 158   |     535|     297.704|   0.6%/121|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 155   |     543|     122.835|   0.4%/196|   0.3%/231|   0.3%/242|   0.3%/254 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 156   |     978|     149.637|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 156   |      35|      18.135|   0.4%/178|   0.4%/154|   0.5%/149|   0.5%/145 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 158   |     193|      28.236|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 155   |      82|      18.414|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 157   |     279|      40.648|   2.8%/ 24|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 158   |      87|      31.127|   0.2%/326|   0.2%/342|   0.2%/349|   0.2%/358 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 112   |     200|       7.624|   0.8%/ 82|   0.8%/ 88|   0.8%/ 89|   0.8%/ 90 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 158   |     127|       3.880|   0.1%/890|   0.1%/677|   0.1%/636|   0.1%/599 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 158   |     126|       6.229|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 158   |     160|      39.143|   0.1%/620|   0.1%/511|   0.1%/489|   0.1%/468 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 158   |   67786|     535.529|   0.8%/ 84|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 158   |    1048|     390.640|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 158   |    1389|      38.732|   3.3%/ 21|   3.1%/ 22|   3.1%/ 23|   3.0%/ 23 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 104   |      26|       0.853|   2.1%/ 33|   2.7%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  58   |      91|      37.083|   4.9%/ 14|   3.7%/ 18|   3.4%/ 20|   3.0%/ 23 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 113   |     289|       9.633|   5.0%/ 14|   4.8%/ 14|   4.7%/ 15|   4.7%/ 15 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 158   |    6275|     359.459|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 158   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 158   |     142|      22.020|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 158   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 158   |    1046|       5.072|   0.4%/168|   0.4%/163|   0.4%/161|   0.4%/159 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 158   |     617|     296.875|   0.6%/118|   0.6%/121|   0.6%/121|   0.6%/122 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 158   |     266|      49.497|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 158   |     721|     154.463|   1.0%/ 67|   0.9%/ 75|   0.9%/ 77|   0.9%/ 79 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 158   |    6353|      28.966|   0.1%/523|   0.1%/588|   0.1%/606|   0.1%/624 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 158   |    2099|     497.467|   0.7%/ 95|   0.6%/110|   0.6%/115|   0.6%/119 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  41   |       5|       0.560|   4.4%/ 16|   0.2%/367|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 158   |     445|      62.168|   5.5%/ 12|   5.4%/ 13|   5.3%/ 13|   5.3%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 158   |   30706|     955.647|   0.6%/123|   0.5%/141|   0.5%/146|   0.5%/152 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 158   |    3858|      35.556|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 158   |    2112|      55.027|   0.6%/115|   0.6%/115|   0.6%/114|   0.6%/114 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 158   |    1837|     178.776|   0.2%/427|   0.2%/435|   0.2%/437|   0.2%/439 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 158   |     201|      73.153|   0.3%/244|   0.3%/259|   0.3%/261|   0.3%/262 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 158   |    3881|     200.014|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 158   |   17717|     120.734|   0.6%/113|   0.6%/116|   0.6%/116|   0.6%/117 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  99   |      19|       1.537|   2.2%/ 32|   4.0%/ 17|   4.0%/ 17|   1.9%/ 36 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 158   |    4086|     119.405|   0.8%/ 85|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 158   |     296|      18.271|   0.6%/115|   0.5%/153|   0.4%/166|   0.4%/183 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 158   |     731|     105.022|   0.3%/253|   0.2%/434|   0.1%/525|   0.1%/663 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 136   |      71|       8.967|   0.2%/361|   0.2%/298|   0.2%/284|   0.3%/272 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 158   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 158   |      34|       6.228|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 158   |     135|      64.471|   0.2%/412|   0.1%/510|   0.1%/541|   0.1%/574 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 151   |      98|       6.149|   0.2%/309|   0.3%/267|   0.3%/259|   0.3%/252 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 158   |   15178|     258.243|   1.0%/ 71|   0.7%/ 95|   0.7%/103|   0.6%/112 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 158   |   29250|     621.010|   0.1%/494|   0.2%/423|   0.2%/408|   0.2%/394 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 158   |      12|       0.561|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 158   |     834|      19.651|   0.1%/580|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 158   |    5835|     564.447|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 158   |    2013|     233.973|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 158   |     135|       7.734|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 158   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 158   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 158   |      30|       3.991|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 158   |      30|      22.139|   6.8%/ 10|   7.5%/  9|   7.7%/  9|   7.9%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 158   |      85|       7.245|   1.9%/ 37|   2.1%/ 32|   2.2%/ 31|   2.3%/ 30 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 158   |    6427|      77.294|   0.6%/119|   0.7%/104|   0.7%/101|   0.7%/ 98 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 158   |  189202|     574.133|   0.5%/138|   0.5%/147|   0.5%/149|   0.5%/151 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  44   |      37|       0.915|   3.9%/ 18|   3.5%/ 20|   3.8%/ 18|   4.1%/ 17 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 158   |    2811|      67.110|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 158   |     390|      39.386|   0.3%/213|   0.3%/215|   0.3%/216|   0.3%/217 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 158   |   41291|     621.521|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 158   |      46|      12.981|   0.6%/110|   0.6%/124|   0.5%/129|   0.5%/134 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 158   |     354|      10.382|   1.8%/ 38|   1.6%/ 44|   1.5%/ 46|   1.5%/ 48 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 158   |     435|      13.489|   1.8%/ 37|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  37   |      35|       0.367|   2.7%/ 26|   1.5%/ 48|   1.1%/ 65|   0.7%/100 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 157   |     305|      17.060|   0.5%/154|   0.2%/277|   0.2%/346|   0.2%/457 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 158   |     226|      14.899|   1.5%/ 45|   0.8%/ 89|   0.6%/117|   0.4%/171 |

