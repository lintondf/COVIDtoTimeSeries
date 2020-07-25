# State and Country COVID-19 Analysis #
## Updated: at 2020-07-25 for data as of 2020-07-24 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.3% of deaths and 39.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.5% of deaths and 56.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 115   |   32605|    1676.064|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 115   |   15824|    1781.594|   0.1%/510|   0.1%/928|   0.1%/ ***|   0.0%/ *** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 115   |    8507|    1224.168|   0.2%/373|   0.2%/422|   0.2%/436|   0.2%/451 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 115   |    8279|     209.542|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 115   |    7610|     600.571|   0.2%/284|   0.2%/367|   0.2%/394|   0.2%/426 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 115   |    7117|     555.944|   0.3%/268|   0.2%/284|   0.2%/288|   0.2%/293 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 115   |    6411|     641.972|   0.1%/529|   0.1%/621|   0.1%/651|   0.1%/685 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 115   |    5566|     259.163|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 115   |    4683|     161.499|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 115   |    4419|    1239.316|   0.1%/730|   0.1%/732|   0.1%/737|   0.1%/745 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 115   |  144766|     439.292|   0.6%/116|   0.6%/109|   0.6%/107|   0.7%/106 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 115   |   85411|     404.001|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 115   |   45758|     688.760|   0.2%/442|   0.1%/482|   0.1%/493|   0.1%/505 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 115   |   42694|     337.297|   1.7%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 115   |   35109|     582.833|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 115   |   31146|      22.881|   2.5%/ 27|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 115   |   30226|     450.625|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 115   |   28433|     603.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 115   |   14213|     442.326|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 115   |   15283|     183.300|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 115   |    1411|     287.870|   2.0%/ 35|   2.2%/ 31|   2.3%/ 31|   2.3%/ 30 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 115   |      19|      25.735|   1.4%/ 50|   1.7%/ 40|   1.8%/ 38|   1.9%/ 37 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 115   |    3154|     433.297|   2.9%/ 24|   3.0%/ 23|   3.1%/ 23|   3.1%/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 115   |     391|     129.443|   1.7%/ 41|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 115   |    8279|     209.542|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 115   |    1782|     309.444|   0.3%/237|   0.3%/204|   0.4%/197|   0.4%/191 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 115   |    4419|    1239.316|   0.1%/730|   0.1%/732|   0.1%/737|   0.1%/745 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 115   |     529|     543.417|   0.2%/383|   0.2%/340|   0.2%/330|   0.2%/320 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 115   |    5566|     259.163|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 115   |    3348|     315.342|   1.0%/ 66|   1.3%/ 54|   1.3%/ 52|   1.4%/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 115   |      26|      18.265|   1.4%/ 51|   2.0%/ 35|   2.1%/ 33|   2.3%/ 30 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 115   |     132|      73.645|   3.1%/ 22|   3.9%/ 17|   4.1%/ 17|   4.3%/ 16 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 115   |    7610|     600.571|   0.2%/284|   0.2%/367|   0.2%/394|   0.2%/426 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 115   |    2878|     427.448|   0.4%/186|   0.4%/177|   0.4%/175|   0.4%/172 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 115   |     823|     260.895|   0.7%/ 94|   0.8%/ 83|   0.9%/ 81|   0.9%/ 79 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 115   |     323|     110.886|   0.8%/ 86|   0.9%/ 76|   0.9%/ 74|   1.0%/ 71 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 115   |     693|     155.108|   0.8%/ 88|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 115   |    3597|     773.682|   0.5%/152|   0.4%/161|   0.4%/164|   0.4%/167 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 115   |     119|      88.712|   0.4%/161|   0.3%/206|   0.3%/221|   0.3%/240 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 115   |    3424|     566.371|   0.3%/259|   0.2%/280|   0.2%/286|   0.2%/291 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 115   |    8507|    1224.168|   0.2%/373|   0.2%/422|   0.2%/436|   0.2%/451 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 115   |    6411|     641.972|   0.1%/529|   0.1%/621|   0.1%/651|   0.1%/685 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 115   |    1606|     284.777|   0.3%/210|   0.3%/214|   0.3%/215|   0.3%/216 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 115   |    1454|     488.408|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 115   |    1179|     192.150|   0.7%/102|   0.7%/ 92|   0.8%/ 90|   0.8%/ 88 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 115   |      45|      42.036|   2.9%/ 23|   3.5%/ 20|   3.6%/ 19|   3.8%/ 18 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 115   |     315|     162.638|   0.7%/ 95|   0.9%/ 78|   0.9%/ 75|   1.0%/ 72 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 115   |     711|     230.672|   1.7%/ 41|   1.9%/ 37|   1.9%/ 35|   2.0%/ 34 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 115   |     405|     297.825|   0.3%/206|   0.3%/211|   0.3%/211|   0.3%/210 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 115   |   15824|    1781.594|   0.1%/510|   0.1%/928|   0.1%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 115   |     599|     285.748|   0.8%/ 83|   0.9%/ 80|   0.9%/ 79|   0.9%/ 78 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 115   |   32605|    1676.064|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 115   |    1766|     168.399|   1.3%/ 55|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 115   |      97|     127.325|   1.1%/ 64|   1.2%/ 55|   1.3%/ 53|   1.3%/ 52 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 115   |    3268|     279.571|   0.6%/110|   0.7%/102|   0.7%/100|   0.7%/ 98 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 115   |     477|     120.521|   1.1%/ 60|   1.3%/ 52|   1.4%/ 50|   1.4%/ 48 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 115   |     279|      66.080|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 115   |    7117|     555.944|   0.3%/268|   0.2%/284|   0.2%/288|   0.2%/293 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 115   |     189|      59.063|   1.2%/ 60|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 115   |    1003|     946.662|   0.2%/352|   0.2%/401|   0.2%/415|   0.2%/430 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 115   |    1325|     257.435|   3.0%/ 23|   3.4%/ 20|   3.5%/ 19|   3.6%/ 19 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 115   |     124|     139.777|   1.1%/ 65|   0.9%/ 73|   0.9%/ 76|   0.9%/ 80 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 115   |     929|     135.913|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 115   |    4683|     161.499|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 115   |  144766|     439.292|   0.6%/116|   0.6%/109|   0.6%/107|   0.7%/106 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 115   |     271|      84.378|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 115   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 115   |    2081|     243.850|   0.5%/148|   0.3%/211|   0.3%/236|   0.3%/266 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 115   |    1483|     194.687|   0.6%/117|   0.6%/123|   0.6%/125|   0.5%/127 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 115   |     102|      57.143|   0.5%/143|   0.5%/129|   0.5%/126|   0.6%/124 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 115   |     870|     149.412|   0.6%/121|   0.7%/101|   0.7%/ 97|   0.7%/ 93 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 103   |      26|      44.335|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 115   |    1266|      39.300|   1.6%/ 43|   1.2%/ 58|   1.1%/ 63|   1.0%/ 70 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 115   |     128|      44.938|   2.7%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 115   |    1130|      26.287|   1.0%/ 73|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 115   |      35|       1.110|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 115   |    2718|      60.490|   3.4%/ 20|   3.7%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 115   |     702|     237.430|   1.8%/ 37|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 115   |     129|       5.034|   2.0%/ 34|   2.7%/ 26|   2.8%/ 24|   3.0%/ 23 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 115   |     712|      79.981|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 115   |     403|      40.079|   2.4%/ 29|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 115   |     137|      88.926|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 115   |    2853|      16.936|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.5%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 115   |     527|      55.989|   1.1%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 79 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 115   |    9814|     851.557|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 110   |      35|       2.982|   2.8%/ 25|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 115   |    2489|     217.025|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 115   |     277|      83.818|   1.9%/ 36|   2.1%/ 33|   2.1%/ 33|   2.2%/ 32 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 115   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 115   |   85411|     404.001|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 115   |     331|      47.604|   1.7%/ 40|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 115   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 103   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 115   |     389|      14.661|   0.5%/133|   0.6%/112|   0.6%/108|   0.7%/104 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 115   |    8940|     235.270|   0.1%/725|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  63   |      58|      10.584|   0.6%/108|   1.4%/ 48|   1.6%/ 42|   1.8%/ 38 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  88   |      75|       4.628|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 115   |    9085|     475.456|   1.1%/ 66|   0.8%/ 82|   0.8%/ 87|   0.7%/ 93 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 115   |    4645|       3.313|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 115   |    7986|     161.679|   3.4%/ 20|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 115   |      85|      16.794|  13.5%/  5|  15.2%/  4|  15.7%/  4|  16.1%/  4 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 115   |     126|      30.976|   0.7%/ 96|   0.8%/ 86|   0.8%/ 84|   0.9%/ 81 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 115   |      87|       7.783|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 115   |     612|     105.158|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 115   |    1042|     100.579|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 115   |    5495|     314.576|   0.7%/ 99|   0.6%/108|   0.6%/110|   0.6%/113 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 115   |    4632|      46.194|   1.4%/ 48|   1.1%/ 61|   1.0%/ 66|   1.0%/ 72 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 115   |     385|      59.296|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  94   |      51|      37.548|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 111   |     199|       2.013|   3.7%/ 19|   4.3%/ 16|   4.4%/ 16|   4.6%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 115   |     328|      59.341|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 115   |   30226|     450.625|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 115   |      47|      21.721|   0.3%/225|   0.3%/271|   0.3%/276|   0.3%/276 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 115   |       5|       2.088|   5.5%/ 13|   6.7%/ 10|   7.1%/ 10|   7.5%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 112   |      16|       4.245|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 115   |    9117|     109.649|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 115   |     158|       5.221|   1.3%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 115   |     198|      18.448|   0.3%/213|   0.5%/145|   0.5%/133|   0.6%/123 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 115   |    1709|     102.933|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 101   |      42|       3.442|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  90   |      26|      16.268|   0.1%/584|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 111   |     159|      13.745|   1.3%/ 51|   1.0%/ 71|   0.9%/ 79|   0.8%/ 88 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 115   |    1046|     114.221|   2.7%/ 26|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 115   |     597|      61.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 115   |   31146|      22.881|   2.5%/ 27|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 115   |    4596|      17.220|   2.2%/ 32|   2.3%/ 30|   2.4%/ 29|   2.4%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 115   |   15283|     183.300|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 115   |    4326|     110.561|   2.6%/ 27|   2.1%/ 33|   2.0%/ 35|   1.8%/ 38 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 115   |    1759|     357.413|   0.1%/948|   0.1%/768|   0.1%/733|   0.1%/699 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 115   |     442|      48.133|   1.7%/ 40|   2.0%/ 35|   2.1%/ 33|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 115   |   35109|     582.833|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 115   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 115   |     991|       7.870|   0.1%/817|   0.1%/714|   0.1%/688|   0.1%/662 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 115   |      11|       1.043|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 115   |     622|      33.285|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 115   |     270|       5.684|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.4%/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 115   |     166|      92.305|   4.4%/ 16|   4.2%/ 16|   4.2%/ 16|   4.2%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 112   |     424|      95.827|   0.7%/ 96|   0.7%/ 99|   0.7%/100|   0.7%/100 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 113   |     268|      41.092|   5.0%/ 14|   4.4%/ 16|   4.2%/ 16|   4.1%/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 113   |      31|      16.391|   0.2%/445|   0.1%/614|   0.1%/708|   0.1%/852 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 115   |      43|       6.263|   1.3%/ 52|   1.7%/ 40|   1.8%/ 38|   1.9%/ 36 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 112   |      75|      16.842|   1.2%/ 60|   0.5%/134|   0.3%/201|   0.2%/406 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 114   |      57|       8.278|   3.7%/ 18|   3.4%/ 20|   4.6%/ 15|   4.5%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 115   |      80|      28.656|   0.1%/744|   0.1%/686|   0.1%/668|   0.1%/651 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  69   |      78|       2.956|   5.8%/ 12|   5.4%/ 13|   5.3%/ 13|   5.1%/ 14 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 115   |     123|       3.760|   0.1%/779|   0.1%/706|   0.1%/692|   0.1%/680 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 115   |     123|       6.063|   0.2%/360|   0.2%/410|   0.2%/418|   0.2%/422 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 115   |     159|      39.110|   0.7%/106|   0.4%/164|   0.4%/191|   0.3%/230 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 115   |   42694|     337.297|   1.7%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 115   |     728|     271.360|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 115   |     289|       8.054|   1.4%/ 51|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  61   |      11|       0.380|   2.1%/ 32|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  15   |       7|       2.847|   0.0%/ --|  32.6%/  2|  20.5%/  3|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  70   |      43|       1.431|   1.1%/ 60|   1.6%/ 44|   1.7%/ 40|   1.9%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 115   |    6159|     352.825|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 115   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 115   |     109|      16.802|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 115   |      69|       3.102|   0.1%/853|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 115   |     846|       4.106|   1.3%/ 55|   1.1%/ 64|   1.0%/ 66|   1.0%/ 69 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 115   |     454|     218.363|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 115   |     256|      47.641|   0.1%/863|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 115   |     366|      78.403|   2.9%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 115   |    5878|      26.798|   0.9%/ 76|   0.7%/104|   0.6%/115|   0.5%/128 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 115   |    1252|     296.697|   2.7%/ 26|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 115   |      37|       5.223|   4.8%/ 14|   5.7%/ 12|   6.0%/ 11|   6.2%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 115   |   14213|     442.326|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 115   |    1918|      17.672|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 115   |    1660|      43.256|   0.4%/157|   0.4%/177|   0.4%/183|   0.4%/188 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 115   |    1715|     166.851|   0.3%/248|   0.2%/303|   0.2%/320|   0.2%/339 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 115   |     167|      60.840|   1.1%/ 61|   0.8%/ 86|   0.7%/ 96|   0.6%/107 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 115   |    2143|     110.440|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 63 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 115   |   13125|      89.444|   1.2%/ 56|   1.1%/ 63|   1.1%/ 65|   1.0%/ 67 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  56   |       5|       0.424|   3.3%/ 21|   1.8%/ 38|   1.3%/ 54|   0.7%/106 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 115   |    2705|      79.062|   1.7%/ 42|   1.4%/ 49|   1.3%/ 52|   1.3%/ 54 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 115   |     181|      11.192|   1.7%/ 40|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 115   |     535|      76.839|   2.3%/ 30|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  93   |      66|       8.404|   0.4%/193|   0.4%/194|   0.4%/195|   0.4%/197 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 115   |      27|       4.775|   0.2%/403|   0.2%/434|   0.2%/453|   0.1%/480 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 115   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 115   |     114|      54.383|   0.2%/351|   0.3%/229|   0.3%/210|   0.4%/193 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 108   |      93|       5.872|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 115   |    6152|     104.673|   3.7%/ 18|   3.9%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 115   |   28433|     603.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 115   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 115   |     714|      16.819|   0.8%/ 86|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 115   |    5696|     550.924|   0.2%/288|   0.2%/305|   0.2%/309|   0.2%/313 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 115   |    1974|     229.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 115   |      36|       2.058|   4.4%/ 16|   8.6%/  8|   6.5%/ 11|   4.1%/ 17 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 115   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 115   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 115   |      16|       2.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 115   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 115   |      50|       4.265|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 115   |    5587|      67.183|   0.3%/204|   0.3%/212|   0.3%/215|   0.3%/217 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 115   |  144766|     439.292|   0.6%/116|   0.6%/109|   0.6%/107|   0.7%/106 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 115   |    1597|      38.141|   1.1%/ 61|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 115   |     344|      34.810|   0.3%/235|   0.2%/293|   0.2%/312|   0.2%/333 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 115   |   45758|     688.760|   0.2%/442|   0.1%/482|   0.1%/493|   0.1%/505 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 115   |      34|       9.780|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 115   |     114|       3.348|   5.3%/ 13|   4.4%/ 16|   4.1%/ 17|   3.9%/ 18 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 115   |     136|       4.219|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 114   |     160|       8.940|  10.1%/  7|  11.7%/  6|  12.1%/  6|  12.3%/  5 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 115   |      33|       2.202|   6.2%/ 11|   4.7%/ 15|   4.2%/ 16|   3.8%/ 18 |

