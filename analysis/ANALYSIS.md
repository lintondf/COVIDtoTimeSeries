# State and Country COVID-19 Analysis #
## Updated: at 2020-07-14 for data as of 2020-07-13 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.7% of deaths and 38.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Florida and California have followed nearly identical trajectories since early April 2020.
 
For confirmed cases, the story is not so different.

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

Why the focus on deaths not cases?  The problem with case statistics is that what is counted has changed nearly continuously since the start of the pandemic and continues to this day.  Early on, only patients sick enough to go to the hospital could be counted.  As tests came online (and eventually actually worked), people visiting a doctor could be tested and counted.  As of mid-2020, in the U.S., drive-up testing is more widely available, but since that involves the choice to undergo the unpleasantness of a deep nasal swab, current testing is by no means a random sample of the U.S. population.

The death statistics are not perfect.  Some claim conflating "dying of COVID-19" vs "dying with COVID-19" overstates death counts or that health care financing incentives favor overcounting.  Others say political incentives or incompetence motivate widespread undercounting.

I can not summarize the poor quality of the data better than [Willis Eschenbach](https://wattsupwiththat.com/daily-coronavirus-covid-19-data-graph-page/#001) when he threw in the towel on his own daily graph series:
> There are four important numbers in the game—positive tests, negative tests, hospitalizations, and deaths. Each has its own problems.

> The positive and negative tests used to refer just to detecting active cases. Now, however, we have test for both active cases and antibody tests to determine if someone has ever had the virus … and unfortunately, there’s no distinction in the data between these totally different tests.

> Hospitalizations were no problem when only corona patients were in the hospitals. But now that elective and other procedures are happening again, say some young guy goes in for a vasectomy. He gets tested, he’s not an active case but he has antibodies. So guess what? His hospitalization is now a COVID hospitalization. So they test his wife and two kids. They had it too, asymptomatic, but they’re now three more positive tests.

> Then there’s the problem of repeat testing of people who have the disease. If someone gets six tests, then it’s reported as six separate cases even though it’s only one case.

> Finally, the deaths. The CDC in its infinite stupidity has said to categorize a death WITH coronavirus the same as a death FROM coronavirus. They’ve also said that if a physician even SUSPECTS, not that corona caused the death but suspects that corona somehow contributed to the death … mark it as a death from coronavirus.

However, since the production of these charts is automatic I will continue to update them nightly.  My keys may be far away but the light is better under this street light.

# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 70.8% of deaths and 52.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 122   |   32564|    1673.915|   0.1%/777|   0.1%/911|   0.1%/952|   0.1%/996 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 126   |   15882|    1788.018|   0.3%/258|   0.3%/247|   0.3%/243|   0.3%/240 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 116   |    8351|    1201.660|   0.2%/279|   0.2%/312|   0.2%/320|   0.2%/329 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 119   |    7418|     585.432|   0.5%/141|   0.5%/138|   0.5%/137|   0.5%/136 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 132   |    7107|     179.862|   1.2%/ 57|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 117   |    6932|     541.474|   0.3%/223|   0.3%/243|   0.3%/249|   0.3%/254 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 117   |    6318|     632.657|   0.2%/376|   0.2%/354|   0.2%/348|   0.2%/342 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 117   |    4363|    1223.737|   0.1%/965|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 128   |    4228|     196.849|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 122   |    3418|     735.294|   0.5%/145|   0.5%/136|   0.5%/134|   0.5%/131 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  136117|     413.047|   0.5%/132|   0.5%/137|   0.5%/139|   0.5%/140 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 119   |   73659|     348.415|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 125   |   45075|     678.478|   0.2%/343|   0.2%/404|   0.2%/422|   0.2%/442 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 117   |   36241|     286.311|   2.0%/ 35|   1.7%/ 41|   1.6%/ 43|   1.5%/ 45 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 144   |   34999|     581.004|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 150   |   30052|     448.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 133   |   28470|     604.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 125   |   23844|      17.517|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 145   |   12943|     155.235|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 116   |   12171|     378.782|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 111   |    1132|     230.784|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 111   |      18|      24.400|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 115   |    2232|     306.645|   2.5%/ 28|   2.6%/ 26|   2.6%/ 26|   2.7%/ 26 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 112   |     328|     108.757|   1.5%/ 46|   1.3%/ 52|   1.3%/ 54|   1.2%/ 56 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 132   |    7107|     179.862|   1.2%/ 57|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 122   |    1726|     299.802|   0.2%/347|   0.2%/362|   0.2%/363|   0.2%/363 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 117   |    4363|    1223.737|   0.1%/965|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 110   |     520|     534.346|   0.1%/540|   0.1%/573|   0.1%/583|   0.1%/595 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 128   |    4228|     196.849|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 124   |    3013|     283.788|   0.6%/117|   0.6%/117|   0.6%/116|   0.6%/115 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 105   |      19|      13.742|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 110   |     102|      56.897|   0.8%/ 89|   1.0%/ 71|   1.0%/ 67|   1.1%/ 64 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 119   |    7418|     585.432|   0.5%/141|   0.5%/138|   0.5%/137|   0.5%/136 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 120   |    2777|     412.566|   0.4%/192|   0.3%/217|   0.3%/224|   0.3%/231 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 111   |     753|     238.541|   0.5%/150|   0.5%/141|   0.5%/138|   0.5%/136 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 123   |     300|     102.970|   0.7%/104|   0.6%/112|   0.6%/114|   0.6%/117 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 120   |     631|     141.299|   0.8%/ 85|   0.8%/ 85|   0.8%/ 85|   0.8%/ 86 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 122   |    3418|     735.294|   0.5%/145|   0.5%/136|   0.5%/134|   0.5%/131 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 109   |     113|      84.404|   0.6%/111|   0.7%/ 92|   0.8%/ 89|   0.8%/ 85 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 117   |    3335|     551.614|   0.3%/206|   0.3%/233|   0.3%/240|   0.3%/248 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 116   |    8351|    1201.660|   0.2%/279|   0.2%/312|   0.2%/320|   0.2%/329 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 117   |    6318|     632.657|   0.2%/376|   0.2%/354|   0.2%/348|   0.2%/342 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 115   |    1551|     275.087|   0.4%/195|   0.3%/247|   0.3%/265|   0.2%/286 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 117   |    1251|     420.467|   1.3%/ 55|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 117   |    1103|     179.742|   0.6%/114|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 109   |      24|      22.882|   0.6%/113|   0.5%/128|   0.5%/132|   0.5%/135 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 108   |     291|     150.374|   0.4%/174|   0.1%/683|   0.0%/ ***|   0.0%/ -- |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 120   |     589|     191.132|   1.2%/ 57|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 113   |     396|     291.297|   0.5%/145|   0.3%/228|   0.3%/264|   0.2%/313 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 126   |   15882|    1788.018|   0.3%/258|   0.3%/247|   0.3%/243|   0.3%/240 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 111   |     547|     260.973|   0.8%/ 91|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 122   |   32564|    1673.915|   0.1%/777|   0.1%/911|   0.1%/952|   0.1%/996 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 111   |    1529|     145.745|   0.8%/ 83|   0.8%/ 87|   0.8%/ 87|   0.8%/ 88 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 109   |      87|     113.846|   0.8%/ 92|   0.9%/ 73|   1.0%/ 69|   1.1%/ 66 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 116   |    3071|     262.754|   0.6%/119|   0.6%/121|   0.6%/121|   0.6%/122 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 117   |     423|     106.795|   0.7%/ 95|   0.8%/ 86|   0.8%/ 83|   0.9%/ 81 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 121   |     236|      55.891|   1.1%/ 65|   1.1%/ 62|   1.1%/ 61|   1.2%/ 60 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 117   |    6932|     541.474|   0.3%/223|   0.3%/243|   0.3%/249|   0.3%/254 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 115   |     164|      51.258|   0.8%/ 91|   1.0%/ 68|   1.1%/ 64|   1.2%/ 60 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 108   |     987|     931.494|   0.3%/226|   0.2%/355|   0.2%/412|   0.1%/492 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 120   |     969|     188.262|   2.1%/ 33|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 125   |     109|     122.884|   1.4%/ 49|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 115   |     748|     109.441|   1.7%/ 40|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 119   |    3190|     110.002|   2.2%/ 32|   2.5%/ 27|   2.6%/ 26|   2.7%/ 25 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 136   |  136117|     413.047|   0.5%/132|   0.5%/137|   0.5%/139|   0.5%/140 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 114   |     215|      67.211|   1.8%/ 39|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 116   |      56|      89.748|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 122   |    1996|     233.871|   0.9%/ 78|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 136   |    1437|     188.649|   0.6%/112|   0.6%/107|   0.7%/105|   0.7%/104 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 106   |      96|      53.759|   0.3%/236|   0.3%/224|   0.3%/220|   0.3%/215 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 116   |     825|     141.650|   0.4%/172|   0.3%/205|   0.3%/214|   0.3%/223 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  92   |      21|      36.506|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 114   |    1048|      32.535|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 125   |      98|      34.542|   3.4%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 124   |    1021|      23.733|   0.8%/ 82|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 107   |      27|       0.855|   5.2%/ 13|   4.8%/ 14|   4.7%/ 15|   4.5%/ 15 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 128   |    1921|      42.741|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 110   |     577|     195.188|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 135   |     108|       4.188|   0.3%/230|   0.4%/192|   0.4%/184|   0.4%/176 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 124   |     710|      79.736|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 123   |     320|      31.806|   3.1%/ 22|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 120   |     113|      73.466|   2.0%/ 35|   1.3%/ 53|   1.1%/ 61|   1.0%/ 71 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 118   |    2434|      14.447|   2.1%/ 33|   1.9%/ 36|   1.8%/ 38|   1.8%/ 39 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 105   |     472|      50.215|   1.4%/ 51|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 125   |    9794|     849.868|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  99   |      26|       2.236|   3.3%/ 21|   2.5%/ 27|   2.4%/ 29|   2.3%/ 30 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 107   |    1923|     167.683|   3.9%/ 18|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 115   |     224|      67.746|   1.5%/ 48|   1.7%/ 42|   1.7%/ 40|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 105   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 119   |   73659|     348.415|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 125   |     276|      39.751|   1.4%/ 49|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 118   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  92   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 111   |     362|      13.618|   0.7%/106|   0.8%/ 92|   0.8%/ 88|   0.8%/ 85 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 127   |    8866|     233.310|   0.2%/416|   0.1%/543|   0.1%/587|   0.1%/639 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  52   |      54|       9.773|   1.4%/ 48|   0.7%/105|   0.4%/183|   0.1%/778 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  77   |      74|       4.586|   0.1%/ ***|   0.2%/395|   0.2%/335|   0.2%/288 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 114   |    7239|     378.867|   1.8%/ 38|   1.3%/ 52|   1.2%/ 57|   1.1%/ 63 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 125   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 114   |    5674|     114.865|   4.1%/ 17|   3.9%/ 18|   3.9%/ 18|   3.8%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 117   |      31|       6.117|   8.5%/  8|   3.8%/ 18|   6.3%/ 11|   9.4%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 117   |     118|      29.028|   0.7%/101|   0.9%/ 78|   0.9%/ 74|   1.0%/ 71 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 118   |      87|       7.736|   0.1%/552|   0.2%/453|   0.2%/430|   0.2%/408 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 122   |     610|     104.780|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 119   |     897|      86.636|   1.5%/ 45|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 122   |    5102|     292.063|   0.9%/ 80|   0.8%/ 83|   0.8%/ 84|   0.8%/ 84 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 128   |    4058|      40.466|   2.3%/ 30|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 105   |     284|      43.841|   3.7%/ 19|   2.5%/ 27|   2.2%/ 31|   1.9%/ 36 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  83   |      55|      40.497|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 100   |     128|       1.300|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 115   |     329|      59.593|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 150   |   30052|     448.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 116   |      48|      21.949|   0.8%/ 90|   0.3%/205|   0.2%/302|   0.1%/576 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 113   |       3|       1.335|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 101   |      15|       4.067|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 127   |    9085|     109.260|   0.1%/870|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 115   |     143|       4.707|   1.8%/ 39|   1.2%/ 56|   1.1%/ 63|   1.0%/ 71 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 125   |     193|      18.040|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 120   |    1276|      76.827|   3.8%/ 18|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  90   |      37|       3.065|   1.3%/ 54|   1.1%/ 64|   1.0%/ 67|   1.0%/ 69 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  79   |      26|      16.299|   0.9%/ 73|   0.5%/151|   0.4%/192|   0.3%/252 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 100   |     139|      12.026|   2.5%/ 28|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 110   |     822|      89.728|   3.2%/ 21|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 121   |     596|      61.030|   0.2%/414|   0.1%/489|   0.1%/512|   0.1%/535 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 125   |   23844|      17.517|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 125   |    3671|      13.753|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 145   |   12943|     155.235|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 132   |    3580|      91.504|   4.2%/ 16|   3.2%/ 21|   3.0%/ 23|   2.7%/ 25 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 125   |    1749|     355.292|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 115   |     360|      39.135|   1.0%/ 72|   1.2%/ 59|   1.2%/ 57|   1.3%/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 144   |   34999|     581.004|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 117   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 152   |     990|       7.860|   0.1%/825|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 109   |      10|       0.960|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 111   |     309|      16.535|   0.4%/166|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 110   |     190|       3.996|   2.1%/ 32|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 110   |     109|      60.834|   4.3%/ 16|   5.7%/ 12|   6.1%/ 11|   6.5%/ 11 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 101   |     394|      89.068|   0.8%/ 85|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 102   |     156|      23.911|   7.1%/ 10|   7.0%/ 10|   6.9%/ 10|   6.8%/ 10 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 102   |      30|      15.836|   0.1%/748|   0.2%/377|   0.2%/333|   0.2%/297 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 126   |      37|       5.387|   0.4%/162|   0.3%/232|   0.3%/265|   0.2%/313 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 101   |      48|      10.726|   2.8%/ 25|   3.8%/ 18|   4.1%/ 17|   4.4%/ 16 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 103   |      43|       6.319|   9.0%/  8|   1.8%/ 38|   0.9%/ 80|   1.7%/ 40 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 115   |      79|      28.412|   0.1%/858|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  58   |      36|       1.389|   4.9%/ 14|   1.6%/ 43|   0.9%/ 77|   0.2%/280 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 119   |     122|       3.710|   0.1%/941|   0.1%/595|   0.1%/542|   0.1%/495 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 107   |     122|       6.031|   0.4%/180|   0.3%/242|   0.3%/265|   0.2%/294 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 106   |     148|      36.374|   1.3%/ 54|   1.2%/ 55|   1.2%/ 55|   1.3%/ 55 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 117   |   36241|     286.311|   2.0%/ 35|   1.7%/ 41|   1.6%/ 43|   1.5%/ 45 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 118   |     658|     245.309|   1.4%/ 49|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 126   |     250|       6.977|   0.9%/ 80|   1.0%/ 70|   1.0%/ 68|   1.0%/ 67 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  50   |       9|       0.309|   5.3%/ 13|   2.0%/ 35|   1.1%/ 61|   0.3%/227 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  59   |      38|       1.269|   2.0%/ 35|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 130   |    6161|     352.945|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 107   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 109   |      94|      14.595|   1.2%/ 59|   0.9%/ 80|   0.8%/ 89|   0.7%/101 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 111   |      68|       3.059|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 113   |     745|       3.615|   1.8%/ 38|   1.9%/ 36|   1.9%/ 36|   2.0%/ 35 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 114   |     396|     190.644|   2.0%/ 35|   1.6%/ 42|   1.6%/ 44|   1.5%/ 47 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 122   |     253|      47.107|   0.1%/856|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 105   |     268|      57.440|   3.1%/ 22|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 117   |    5408|      24.657|   1.6%/ 43|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 125   |     936|     221.893|   2.9%/ 23|   3.1%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 115   |      23|       3.263|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 41 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 116   |   12171|     378.782|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 163   |    1388|      12.795|   0.7%/104|   0.6%/119|   0.6%/123|   0.5%/127 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 124   |    1594|      41.542|   0.6%/116|   0.5%/146|   0.4%/156|   0.4%/167 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 119   |    1666|     162.073|   0.4%/168|   0.4%/158|   0.4%/156|   0.4%/154 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 108   |     152|      55.201|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 114   |    1910|      98.446|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 117   |   11519|      78.497|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  45   |       4|       0.323|   0.5%/141|   6.5%/ 11|   8.6%/  8|  10.8%/  6 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 112   |    2326|      67.989|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 104   |     157|       9.681|   2.3%/ 30|   1.6%/ 42|   1.5%/ 47|   1.3%/ 54 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 116   |     384|      55.130|   2.9%/ 24|   3.7%/ 19|   3.9%/ 18|   4.1%/ 17 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  82   |      64|       8.054|   0.4%/167|   0.2%/462|   0.1%/870|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 115   |      26|       4.559|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 108   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 122   |     111|      53.227|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  97   |      93|       5.846|   0.2%/350|   0.2%/298|   0.2%/291|   0.2%/286 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 109   |    4251|      72.324|   3.6%/ 19|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 133   |   28470|     604.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 108   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 123   |     663|      15.628|   0.9%/ 76|   0.8%/ 92|   0.7%/ 96|   0.7%/101 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 125   |    5577|     539.425|   0.3%/231|   0.2%/316|   0.2%/348|   0.2%/386 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 131   |    1969|     228.837|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 107   |      18|       1.022|  11.9%/  6|   4.6%/ 15|   4.6%/ 15|   5.9%/ 12 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 105   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 135   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 109   |      15|       2.028|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 111   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 117   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 119   |    5381|      64.707|   0.4%/188|   0.4%/192|   0.4%/192|   0.4%/193 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  136117|     413.047|   0.5%/132|   0.5%/137|   0.5%/139|   0.5%/140 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 123   |    1425|      34.036|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 116   |     334|      33.801|   0.5%/153|   0.4%/155|   0.4%/156|   0.4%/156 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 125   |   45075|     678.478|   0.2%/343|   0.2%/404|   0.2%/422|   0.2%/442 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 107   |      31|       8.696|   1.0%/ 66|   1.1%/ 61|   1.2%/ 60|   1.2%/ 58 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 109   |      63|       1.840|   7.6%/  9|   9.2%/  7|   9.6%/  7|   9.9%/  7 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 109   |      95|       2.949|   4.8%/ 14|   4.6%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 103   |      47|       2.631|   4.5%/ 15|   2.9%/ 24|   2.5%/ 28|   2.1%/ 33 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 113   |      10|       0.688|   4.0%/ 17|  26.0%/  3|  26.0%/  3|  13.5%/  5 |

