# State and Country COVID-19 Analysis #
## Updated: at 2020-09-10 for data as of 2020-09-09 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.8% of deaths and 57.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 162   |   33022|    1697.486|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 162   |   15992|    1800.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 162   |   14194|     359.224|   0.8%/ 90|   0.7%/103|   0.6%/108|   0.6%/112 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 162   |   14316|     493.718|   1.0%/ 69|   0.8%/ 86|   0.8%/ 92|   0.7%/ 98 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 162   |   12388|     576.806|   0.8%/ 85|   0.6%/112|   0.6%/121|   0.5%/132 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 162   |    9169|    1319.435|   0.1%/511|   0.1%/553|   0.1%/565|   0.1%/578 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 162   |    8442|     666.178|   0.2%/291|   0.2%/293|   0.2%/294|   0.2%/295 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 162   |    7806|     609.787|   0.2%/393|   0.2%/419|   0.2%/427|   0.2%/434 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 162   |    6848|     685.672|   0.2%/448|   0.2%/450|   0.2%/452|   0.2%/453 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 162   |    6266|     590.197|   1.0%/ 69|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 162   |  192111|     582.960|   0.4%/164|   0.4%/183|   0.4%/189|   0.4%/195 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 162   |  129960|     614.723|   0.6%/110|   0.6%/124|   0.5%/128|   0.5%/133 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 162   |   75639|      55.567|   1.6%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 162   |   69573|     549.649|   0.7%/ 94|   0.7%/104|   0.6%/107|   0.6%/109 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 162   |   41084|     618.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 162   |   35577|     590.606|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 162   |   30786|     458.965|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 162   |   30889|     961.322|   0.5%/129|   0.5%/144|   0.5%/148|   0.5%/152 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 162   |   29508|     626.495|   0.2%/415|   0.2%/359|   0.2%/347|   0.2%/335 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 162   |   22772|     273.122|   0.5%/128|   0.5%/142|   0.5%/146|   0.5%/150 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 162   |    2331|     475.501|   0.7%/102|   0.6%/113|   0.6%/117|   0.6%/121 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 162   |      44|      60.333|   1.3%/ 55|   1.2%/ 55|   1.2%/ 55|   1.2%/ 55 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 162   |    5345|     734.399|   0.5%/133|   0.4%/172|   0.4%/185|   0.3%/201 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 162   |     943|     312.604|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 162   |   14194|     359.224|   0.8%/ 90|   0.7%/103|   0.6%/108|   0.6%/112 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 162   |    1979|     343.658|   0.2%/386|   0.2%/397|   0.2%/399|   0.2%/402 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 162   |    4473|    1254.570|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 162   |     611|     627.112|   0.1%/767|   0.1%/868|   0.1%/898|   0.1%/932 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 162   |   12388|     576.806|   0.8%/ 85|   0.6%/112|   0.6%/121|   0.5%/132 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 162   |    6266|     590.197|   1.0%/ 69|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 162   |      93|      65.724|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 162   |     417|     233.378|   1.2%/ 55|   1.0%/ 68|   1.0%/ 73|   0.9%/ 78 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 162   |    8442|     666.178|   0.2%/291|   0.2%/293|   0.2%/294|   0.2%/295 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 162   |    3403|     505.418|   0.3%/232|   0.3%/250|   0.3%/255|   0.3%/261 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 162   |    1201|     380.746|   0.8%/ 88|   0.8%/ 91|   0.8%/ 91|   0.8%/ 92 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 162   |     491|     168.579|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81|   0.9%/ 81 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 162   |    1021|     228.547|   0.8%/ 84|   0.8%/ 87|   0.8%/ 88|   0.8%/ 90 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 162   |    5202|    1119.048|   0.5%/149|   0.4%/178|   0.4%/188|   0.3%/198 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 162   |     135|     100.515|   0.2%/393|   0.1%/486|   0.1%/518|   0.1%/556 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 162   |    3822|     632.257|   0.2%/369|   0.2%/387|   0.2%/392|   0.2%/397 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 162   |    9169|    1319.435|   0.1%/511|   0.1%/553|   0.1%/565|   0.1%/578 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 162   |    6848|     685.672|   0.2%/448|   0.2%/450|   0.2%/452|   0.2%/453 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 162   |    1935|     343.111|   0.3%/210|   0.3%/242|   0.3%/252|   0.3%/263 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 162   |    2685|     902.036|   0.8%/ 92|   0.6%/113|   0.6%/120|   0.5%/128 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 162   |    1683|     274.274|   0.9%/ 73|   1.0%/ 67|   1.1%/ 66|   1.1%/ 64 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 162   |     122|     114.363|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 162   |     415|     214.445|   0.5%/146|   0.4%/159|   0.4%/163|   0.4%/166 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 162   |    1457|     473.177|   0.9%/ 79|   0.7%/100|   0.6%/108|   0.6%/117 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 162   |     435|     319.840|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 162   |   15992|    1800.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 162   |     817|     389.783|   0.5%/139|   0.5%/149|   0.5%/152|   0.4%/155 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 162   |   33022|    1697.486|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 162   |    2967|     282.935|   0.9%/ 77|   0.9%/ 81|   0.8%/ 81|   0.8%/ 82 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 162   |     159|     208.360|   0.9%/ 74|   0.9%/ 79|   0.9%/ 80|   0.9%/ 81 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 162   |    4340|     371.276|   0.5%/149|   0.4%/160|   0.4%/163|   0.4%/166 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 162   |     890|     224.833|   0.9%/ 76|   0.8%/ 90|   0.7%/ 94|   0.7%/ 99 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 162   |     499|     118.345|   0.9%/ 81|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 162   |    7806|     609.787|   0.2%/393|   0.2%/419|   0.2%/427|   0.2%/434 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 162   |     504|     157.739|   1.5%/ 47|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 162   |    1062|    1002.474|   0.1%/478|   0.1%/487|   0.1%/491|   0.1%/495 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 162   |    3008|     584.316|   0.9%/ 75|   0.8%/ 89|   0.7%/ 93|   0.7%/ 98 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 162   |     176|     198.494|   0.5%/149|   0.4%/175|   0.4%/182|   0.4%/191 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 162   |    1982|     290.087|   1.1%/ 61|   1.0%/ 72|   0.9%/ 75|   0.9%/ 79 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 162   |   14316|     493.718|   1.0%/ 69|   0.8%/ 86|   0.8%/ 92|   0.7%/ 98 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 162   |  192111|     582.960|   0.4%/164|   0.4%/183|   0.4%/189|   0.4%/195 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 162   |     433|     135.077|   0.5%/132|   0.4%/166|   0.4%/177|   0.4%/190 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 162   |      58|      92.958|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 162   |    2718|     318.393|   0.5%/135|   0.5%/136|   0.5%/137|   0.5%/137 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 162   |    1994|     261.814|   0.3%/228|   0.2%/323|   0.2%/360|   0.2%/407 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 162   |     263|     146.614|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 162   |    1185|     203.493|   0.5%/137|   0.5%/145|   0.5%/147|   0.5%/149 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 150   |      43|      75.033|   0.2%/378|   0.1%/589|   0.1%/668|   0.1%/764 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 162   |    1424|      44.197|   0.1%/661|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 162   |     329|     115.619|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 162   |    1589|      36.950|   0.5%/127|   0.5%/137|   0.5%/139|   0.5%/142 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 162   |     125|       4.020|   1.5%/ 48|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 162   |   10911|     242.797|   2.4%/ 29|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 162   |     911|     307.904|   0.4%/192|   0.3%/216|   0.3%/223|   0.3%/230 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 162   |     855|      33.275|   2.0%/ 35|   1.5%/ 45|   1.4%/ 49|   1.3%/ 53 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 162   |     738|      82.878|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 162   |     553|      54.980|   0.4%/169|   0.4%/165|   0.4%/164|   0.4%/163 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 162   |     202|     131.187|   0.6%/108|   0.6%/114|   0.6%/115|   0.6%/116 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 162   |    4639|      27.535|   0.9%/ 80|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 162   |     726|      77.177|   0.7%/ 94|   0.8%/ 92|   0.8%/ 92|   0.8%/ 91 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 162   |    9905|     859.444|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 157   |      40|       3.441|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 162   |    5738|     500.235|   1.3%/ 53|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 162   |     693|     209.993|   1.3%/ 54|   1.2%/ 60|   1.1%/ 61|   1.1%/ 63 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 162   |       8|       3.627|   7.3%/  9|   8.4%/  8|   8.7%/  8|   9.0%/  8 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 162   |  129960|     614.723|   0.6%/110|   0.6%/124|   0.5%/128|   0.5%/133 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 162   |     709|     102.000|   1.3%/ 53|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 162   |      56|       2.661|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 150   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 162   |     417|      15.726|   0.1%/814|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 162   |    9217|     242.565|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 110   |      62|      11.320|   0.1%/717|   0.1%/733|   0.1%/755|   0.1%/787 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 135   |      78|       4.827|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 162   |   11771|     616.068|   0.5%/152|   0.4%/160|   0.4%/162|   0.4%/164 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 162   |    4736|       3.377|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 162   |   22606|     457.645|   1.4%/ 50|   1.2%/ 58|   1.1%/ 61|   1.1%/ 63 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 162   |     539|     106.625|   2.1%/ 33|   1.9%/ 36|   1.8%/ 38|   1.8%/ 39 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 162   |     203|      49.758|   1.1%/ 65|   1.2%/ 59|   1.2%/ 58|   1.2%/ 57 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 162   |      97|       8.633|   0.7%/ 94|   0.9%/ 79|   0.9%/ 76|   0.9%/ 73 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 162   |     628|     107.833|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 162   |    1912|     184.602|   1.2%/ 59|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 162   |    6854|     392.346|   0.5%/144|   0.5%/145|   0.5%/146|   0.5%/147 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 162   |    5584|      55.688|   0.3%/211|   0.3%/215|   0.3%/216|   0.3%/217 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 162   |     786|     121.118|   0.8%/ 82|   0.7%/ 97|   0.7%/102|   0.6%/107 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 141   |      83|      61.107|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 158   |    1007|      10.209|   2.1%/ 33|   1.8%/ 39|   1.7%/ 41|   1.6%/ 43 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 162   |     337|      60.912|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 162   |   30786|     458.965|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 162   |      53|      24.569|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 162   |     121|      51.687|   1.0%/ 67|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 159   |      20|       5.246|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 162   |    9346|     112.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 162   |     295|       9.728|   0.4%/167|   0.2%/426|   0.1%/691|   0.0%/ *** |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 162   |     293|      27.347|   1.1%/ 64|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 162   |    2957|     178.112|   0.7%/106|   0.5%/133|   0.5%/143|   0.5%/153 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 148   |      64|       5.204|   0.8%/ 82|   0.8%/ 84|   0.8%/ 84|   0.8%/ 85 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 137   |      38|      23.520|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 158   |     214|      18.481|   0.5%/141|   0.5%/137|   0.5%/135|   0.5%/133 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 162   |    2073|     226.299|   1.1%/ 61|   1.1%/ 60|   1.1%/ 60|   1.2%/ 60 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 162   |     625|      63.949|   0.2%/435|   0.2%/387|   0.2%/376|   0.2%/365 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 162   |   75639|      55.567|   1.6%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 162   |    8325|      31.191|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51|   1.3%/ 51 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 162   |   22772|     273.122|   0.5%/128|   0.5%/142|   0.5%/146|   0.5%/150 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 162   |    7799|     199.319|   1.1%/ 64|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 162   |    1779|     361.388|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 162   |    1094|     119.064|   1.3%/ 51|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 162   |   35577|     590.606|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 162   |      26|       9.480|   3.8%/ 18|   4.3%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 162   |    1415|      11.235|   1.0%/ 69|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 162   |      17|       1.599|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 162   |    1681|      89.944|   0.7%/104|   0.5%/136|   0.5%/148|   0.4%/162 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 162   |     626|      13.168|   0.6%/112|   0.4%/195|   0.3%/240|   0.2%/309 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 162   |     527|     293.437|   0.2%/318|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 159   |     551|     124.646|   0.4%/177|   0.4%/187|   0.4%/190|   0.4%/192 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 160   |     976|     149.441|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 160   |      35|      18.429|   0.3%/204|   0.4%/195|   0.4%/193|   0.4%/191 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 162   |     216|      31.603|   3.1%/ 23|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 159   |      82|      18.359|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 161   |     315|      45.899|   2.6%/ 27|   2.3%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 162   |      87|      31.220|   0.1%/536|   0.1%/840|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 116   |     207|       7.871|   0.8%/ 82|   0.8%/ 82|   0.8%/ 82|   0.8%/ 82 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 162   |     128|       3.911|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 162   |     127|       6.265|   0.1%/606|   0.1%/494|   0.1%/471|   0.2%/450 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 162   |     160|      39.323|   0.1%/693|   0.1%/613|   0.1%/597|   0.1%/581 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 162   |   69573|     549.649|   0.7%/ 94|   0.7%/104|   0.6%/107|   0.6%/109 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 162   |    1088|     405.642|   0.9%/ 77|   0.9%/ 74|   0.9%/ 73|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 162   |    1582|      44.102|   2.9%/ 23|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 108   |      28|       0.940|   2.0%/ 34|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  62   |      95|      38.560|   3.6%/ 19|   1.7%/ 41|   1.2%/ 59|   0.7%/ 99 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 117   |     335|      11.179|   4.3%/ 16|   3.7%/ 19|   3.5%/ 19|   3.4%/ 20 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 162   |    6288|     360.204|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 162   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 162   |     144|      22.310|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 162   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 162   |    1065|       5.164|   0.4%/169|   0.4%/161|   0.4%/159|   0.4%/157 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 162   |     633|     304.616|   0.7%/105|   0.7%/103|   0.7%/102|   0.7%/102 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 162   |     265|      49.400|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 162   |     751|     160.957|   1.1%/ 63|   1.1%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 162   |    6377|      29.075|   0.1%/619|   0.1%/716|   0.1%/744|   0.1%/774 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 162   |    2145|     508.398|   0.6%/107|   0.6%/124|   0.5%/129|   0.5%/135 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  45   |       5|       0.560|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 162   |     529|      73.929|   5.0%/ 14|   4.6%/ 15|   4.5%/ 15|   4.4%/ 16 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 162   |   30889|     961.322|   0.5%/129|   0.5%/144|   0.5%/148|   0.5%/152 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 162   |    4098|      37.761|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 162   |    2156|      56.179|   0.5%/130|   0.5%/135|   0.5%/137|   0.5%/138 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 162   |    1849|     179.940|   0.2%/422|   0.2%/427|   0.2%/428|   0.2%/428 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 162   |     204|      74.263|   0.4%/198|   0.4%/184|   0.4%/180|   0.4%/175 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 162   |    4056|     209.011|   1.2%/ 59|   1.1%/ 63|   1.1%/ 63|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 162   |   18110|     123.408|   0.6%/121|   0.6%/126|   0.5%/127|   0.5%/128 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 103   |      21|       1.669|   4.0%/ 17|   1.8%/ 38|   3.6%/ 19|   3.4%/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 162   |    4201|     122.772|   0.8%/ 90|   0.7%/ 98|   0.7%/100|   0.7%/102 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 162   |     299|      18.472|   0.5%/152|   0.3%/225|   0.3%/255|   0.2%/296 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 162   |     735|     105.539|   0.2%/302|   0.1%/481|   0.1%/561|   0.1%/671 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 140   |      72|       9.061|   0.2%/301|   0.3%/251|   0.3%/242|   0.3%/233 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 162   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 162   |      37|       6.853|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 162   |     136|      64.810|   0.2%/460|   0.1%/548|   0.1%/574|   0.1%/603 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 155   |      98|       6.176|   0.1%/803|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 162   |   15540|     264.390|   0.8%/ 83|   0.6%/108|   0.6%/117|   0.5%/126 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 162   |   29508|     626.495|   0.2%/415|   0.2%/359|   0.2%/347|   0.2%/335 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 162   |      12|       0.562|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 162   |     837|      19.720|   0.1%/544|   0.1%/804|   0.1%/906|   0.1%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 162   |    5842|     565.112|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 162   |    2017|     234.485|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 162   |     150|       8.589|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 162   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 162   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 162   |      32|       4.296|   1.0%/ 69|   1.3%/ 54|   1.3%/ 51|   1.4%/ 49 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 162   |      40|      29.083|   6.6%/ 10|   7.0%/ 10|   7.2%/ 10|   7.3%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 162   |      96|       8.175|   2.2%/ 32|   2.5%/ 28|   2.5%/ 27|   2.6%/ 26 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 162   |    6576|      79.076|   0.7%/ 99|   0.8%/ 88|   0.8%/ 85|   0.8%/ 83 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 162   |  192111|     582.960|   0.4%/164|   0.4%/183|   0.4%/189|   0.4%/195 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  48   |      48|       1.182|   3.7%/ 18|   5.7%/ 12|   6.1%/ 11|   6.5%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 162   |    3011|      71.904|   1.6%/ 43|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 162   |     394|      39.807|   0.3%/233|   0.3%/246|   0.3%/249|   0.3%/254 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 162   |   41084|     618.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 162   |      46|      13.135|   0.4%/161|   0.3%/234|   0.3%/266|   0.2%/308 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 162   |     374|      10.970|   1.7%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 162   |     461|      14.315|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  41   |      35|       0.364|   1.4%/ 49|   0.2%/346|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 161   |     305|      17.027|   0.4%/167|   0.3%/214|   0.3%/229|   0.3%/246 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 162   |     234|      15.445|   0.8%/ 83|   0.1%/649|   0.0%/ --|   0.0%/ -- |

