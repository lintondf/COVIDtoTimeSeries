# State and Country COVID-19 Analysis #
## Updated: at 2020-07-15 for data as of 2020-07-14 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.8% of deaths and 38.5% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 70.7% of deaths and 52.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 123   |   32580|    1674.761|   0.1%/806|   0.1%/950|   0.1%/994|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 127   |   15859|    1785.454|   0.3%/271|   0.3%/267|   0.3%/266|   0.3%/265 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 117   |    8365|    1203.679|   0.2%/296|   0.2%/339|   0.2%/351|   0.2%/364 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 120   |    7450|     587.952|   0.5%/149|   0.5%/150|   0.5%/150|   0.5%/150 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 133   |    7203|     182.306|   1.2%/ 57|   1.2%/ 56|   1.2%/ 55|   1.3%/ 55 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 118   |    6948|     542.763|   0.3%/235|   0.3%/263|   0.3%/271|   0.2%/279 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 118   |    6329|     633.698|   0.2%/397|   0.2%/388|   0.2%/385|   0.2%/382 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 129   |    4312|     200.755|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 118   |    4367|    1224.755|   0.1%/865|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 123   |    3436|     739.134|   0.5%/146|   0.5%/139|   0.5%/137|   0.5%/135 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 137   |  136757|     414.989|   0.5%/135|   0.5%/143|   0.5%/145|   0.5%/146 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 120   |   74734|     353.499|   1.6%/ 44|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 126   |   45143|     679.501|   0.2%/360|   0.2%/431|   0.2%/453|   0.1%/477 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 118   |   36796|     290.698|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 145   |   35009|     581.166|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 151   |   30061|     448.165|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 134   |   28452|     604.079|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 126   |   24395|      17.921|   2.4%/ 28|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 146   |   13140|     157.600|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 117   |   12348|     384.282|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 112   |    1150|     234.578|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48|   1.5%/ 48 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 112   |      18|      24.498|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 116   |    2294|     315.156|   2.5%/ 27|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 113   |     332|     110.178|   1.5%/ 47|   1.3%/ 54|   1.3%/ 55|   1.2%/ 57 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 133   |    7203|     182.306|   1.2%/ 57|   1.2%/ 56|   1.2%/ 55|   1.3%/ 55 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 123   |    1731|     300.576|   0.2%/340|   0.2%/345|   0.2%/344|   0.2%/343 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 118   |    4367|    1224.755|   0.1%/865|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 111   |     520|     533.767|   0.1%/571|   0.1%/630|   0.1%/649|   0.1%/671 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 129   |    4312|     200.755|   1.6%/ 44|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 125   |    3034|     285.712|   0.6%/115|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 106   |      20|      13.800|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 111   |     103|      57.514|   0.7%/ 99|   0.8%/ 84|   0.9%/ 81|   0.9%/ 78 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 120   |    7450|     587.952|   0.5%/149|   0.5%/150|   0.5%/150|   0.5%/150 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 121   |    2785|     413.732|   0.3%/201|   0.3%/229|   0.3%/237|   0.3%/247 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 112   |     756|     239.650|   0.5%/151|   0.5%/143|   0.5%/141|   0.5%/139 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 124   |     302|     103.501|   0.6%/108|   0.6%/119|   0.6%/122|   0.5%/126 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 121   |     636|     142.415|   0.8%/ 86|   0.8%/ 88|   0.8%/ 88|   0.8%/ 89 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 123   |    3436|     739.134|   0.5%/146|   0.5%/139|   0.5%/137|   0.5%/135 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 110   |     114|      84.946|   0.6%/109|   0.7%/ 94|   0.8%/ 91|   0.8%/ 88 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 118   |    3343|     553.020|   0.3%/213|   0.3%/242|   0.3%/250|   0.3%/259 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 117   |    8365|    1203.679|   0.2%/296|   0.2%/339|   0.2%/351|   0.2%/364 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 118   |    6329|     633.698|   0.2%/397|   0.2%/388|   0.2%/385|   0.2%/382 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 116   |    1556|     275.825|   0.3%/204|   0.3%/261|   0.2%/280|   0.2%/303 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 118   |    1268|     426.158|   1.2%/ 55|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 118   |    1111|     180.971|   0.6%/112|   0.6%/112|   0.6%/111|   0.6%/111 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 110   |      25|      23.057|   2.8%/ 25|   3.9%/ 18|   4.1%/ 17|   4.4%/ 15 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 109   |     290|     150.168|   0.3%/201|   0.1%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 121   |     599|     194.489|   1.2%/ 57|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 114   |     397|     291.644|   0.4%/164|   0.2%/283|   0.2%/343|   0.2%/435 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 127   |   15859|    1785.454|   0.3%/271|   0.3%/267|   0.3%/266|   0.3%/265 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 112   |     551|     262.877|   0.7%/ 94|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 123   |   32580|    1674.761|   0.1%/806|   0.1%/950|   0.1%/994|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 112   |    1547|     147.457|   0.9%/ 79|   0.9%/ 78|   0.9%/ 77|   0.9%/ 76 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 110   |      88|     114.953|   0.7%/ 94|   0.9%/ 78|   0.9%/ 75|   1.0%/ 72 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 117   |    3085|     263.962|   0.6%/124|   0.5%/128|   0.5%/129|   0.5%/130 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 118   |     426|     107.667|   0.7%/ 97|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 122   |     239|      56.737|   1.1%/ 61|   1.2%/ 56|   1.3%/ 55|   1.3%/ 53 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 118   |    6948|     542.763|   0.3%/235|   0.3%/263|   0.3%/271|   0.2%/279 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 116   |     166|      51.899|   0.7%/ 93|   1.0%/ 72|   1.0%/ 68|   1.1%/ 64 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 109   |     988|     933.045|   0.3%/235|   0.2%/351|   0.2%/399|   0.2%/460 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 121   |     991|     192.432|   2.0%/ 34|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 126   |     110|     124.234|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 116   |     762|     111.485|   1.7%/ 41|   1.8%/ 39|   1.8%/ 38|   1.8%/ 37 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 120   |    3275|     112.960|   2.2%/ 31|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 137   |  136757|     414.989|   0.5%/135|   0.5%/143|   0.5%/145|   0.5%/146 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 115   |     221|      68.890|   1.8%/ 38|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 117   |      56|      89.746|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 123   |    2008|     235.224|   0.8%/ 85|   0.7%/ 95|   0.7%/ 99|   0.7%/102 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 137   |    1434|     188.256|   0.5%/137|   0.5%/145|   0.5%/147|   0.5%/149 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 107   |      97|      53.952|   0.3%/230|   0.3%/216|   0.3%/212|   0.3%/207 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 117   |     827|     142.096|   0.4%/182|   0.3%/219|   0.3%/229|   0.3%/241 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  93   |      21|      37.005|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 115   |    1068|      33.152|   2.3%/ 30|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 126   |     101|      35.466|   3.4%/ 21|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 125   |    1029|      23.925|   0.8%/ 83|   0.8%/ 85|   0.8%/ 85|   0.8%/ 86 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 108   |      27|       0.883|   5.1%/ 13|   4.5%/ 15|   4.3%/ 16|   4.1%/ 17 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 129   |    1976|      43.964|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 111   |     587|     198.553|   2.0%/ 34|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 136   |     108|       4.213|   0.4%/190|   0.4%/154|   0.5%/146|   0.5%/140 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 125   |     710|      79.749|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 124   |     329|      32.635|   3.0%/ 23|   2.7%/ 25|   2.7%/ 26|   2.6%/ 27 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 121   |     115|      74.193|   1.9%/ 36|   1.3%/ 53|   1.2%/ 60|   1.0%/ 69 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 119   |    2474|      14.684|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 106   |     478|      50.800|   1.3%/ 52|   1.2%/ 55|   1.2%/ 56|   1.2%/ 58 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 126   |    9795|     849.973|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 100   |      27|       2.280|   2.4%/ 29|   2.7%/ 26|   2.8%/ 25|   2.9%/ 24 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 108   |    1982|     172.816|   3.8%/ 18|   3.4%/ 20|   3.2%/ 21|   3.1%/ 22 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 116   |     227|      68.689|   1.4%/ 49|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 106   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 120   |   74734|     353.499|   1.6%/ 44|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 126   |     281|      40.406|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 119   |      53|       2.540|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  93   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 112   |     364|      13.721|   0.6%/120|   0.6%/108|   0.7%/105|   0.7%/103 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 128   |    8876|     233.586|   0.2%/438|   0.1%/574|   0.1%/621|   0.1%/677 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  53   |      54|       9.740|   1.4%/ 50|   0.4%/178|   0.1%/716|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  78   |      75|       4.600|   0.1%/716|   0.3%/275|   0.3%/235|   0.3%/204 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 115   |    7301|     382.096|   1.7%/ 41|   1.2%/ 57|   1.1%/ 63|   1.0%/ 71 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 126   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 115   |    5878|     118.997|   4.0%/ 17|   3.9%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 118   |      33|       6.619|   9.6%/  7|   6.3%/ 11|   9.4%/  7|   9.7%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 118   |     119|      29.292|   0.7%/101|   0.9%/ 81|   0.9%/ 78|   0.9%/ 74 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 119   |      87|       7.746|   0.1%/599|   0.1%/522|   0.1%/501|   0.1%/480 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 123   |     610|     104.827|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 120   |     910|      87.889|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 123   |    5143|     294.427|   0.8%/ 82|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 129   |    4123|      41.119|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 106   |     290|      44.688|   3.5%/ 20|   2.4%/ 28|   2.2%/ 32|   1.9%/ 37 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  84   |      55|      40.201|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 101   |     133|       1.343|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 116   |     329|      59.593|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 151   |   30061|     448.165|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 117   |      48|      21.922|   0.7%/104|   0.2%/286|   0.1%/516|   0.0%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 114   |       3|       1.364|   2.8%/ 25|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 102   |      15|       4.057|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 128   |    9090|     109.324|   0.1%/936|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 116   |     144|       4.757|   1.7%/ 41|   1.2%/ 59|   1.1%/ 65|   0.9%/ 73 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 126   |     193|      18.040|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 121   |    1319|      79.428|   3.7%/ 18|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  91   |      38|       3.103|   1.2%/ 56|   1.0%/ 67|   1.0%/ 69|   1.0%/ 72 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  80   |      26|      16.352|   0.8%/ 88|   0.4%/181|   0.3%/228|   0.2%/301 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 101   |     142|      12.292|   2.3%/ 30|   2.5%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 111   |     839|      91.593|   3.0%/ 23|   2.5%/ 27|   2.4%/ 29|   2.3%/ 31 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 122   |     597|      61.076|   0.1%/466|   0.1%/603|   0.1%/648|   0.1%/700 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 126   |   24395|      17.921|   2.4%/ 28|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 126   |    3736|      13.996|   1.8%/ 37|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 146   |   13140|     157.600|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 133   |    3661|      93.569|   4.0%/ 17|   3.1%/ 22|   2.8%/ 24|   2.6%/ 26 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 126   |    1749|     355.325|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 116   |     364|      39.638|   1.0%/ 66|   1.3%/ 55|   1.3%/ 53|   1.4%/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 145   |   35009|     581.166|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 118   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 153   |     990|       7.859|   0.1%/920|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 110   |      10|       0.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 112   |     362|      19.353|  10.0%/  7|  12.0%/  6|  12.5%/  5|  13.0%/  5 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 111   |     196|       4.112|   2.2%/ 31|   2.4%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 111   |     115|      63.832|   4.6%/ 15|   6.1%/ 11|   6.5%/ 11|   6.9%/ 10 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 102   |     397|      89.753|   0.8%/ 85|   0.8%/ 88|   0.8%/ 88|   0.8%/ 89 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 103   |     164|      25.121|   6.9%/ 10|   6.6%/ 10|   6.4%/ 11|   6.3%/ 11 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 103   |      30|      15.940|   0.2%/353|   0.4%/194|   0.4%/173|   0.4%/155 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 127   |      37|       5.417|   0.5%/150|   0.4%/189|   0.3%/204|   0.3%/224 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 102   |      50|      11.191|   2.8%/ 24|   3.8%/ 18|   4.0%/ 17|   4.3%/ 16 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 104   |      45|       6.497|   4.0%/ 17|   0.9%/ 80|   1.7%/ 40|   3.4%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 116   |      79|      28.412|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  59   |      38|       1.434|   4.1%/ 17|   2.1%/ 33|   1.7%/ 40|   1.4%/ 49 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 120   |     122|       3.714|   0.1%/983|   0.1%/649|   0.1%/594|   0.1%/546 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 108   |     122|       6.039|   0.3%/203|   0.2%/309|   0.2%/358|   0.2%/427 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 107   |     149|      36.666|   1.1%/ 61|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 118   |   36796|     290.698|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 119   |     665|     247.915|   1.3%/ 52|   1.2%/ 58|   1.2%/ 60|   1.1%/ 62 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 127   |     253|       7.062|   1.0%/ 72|   1.1%/ 62|   1.1%/ 60|   1.2%/ 58 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  51   |       9|       0.307|   4.6%/ 15|   1.3%/ 54|   0.5%/140|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  60   |      38|       1.281|   1.8%/ 38|   1.4%/ 48|   1.4%/ 51|   1.3%/ 52 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 131   |    6162|     352.983|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 108   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 110   |      96|      14.876|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 112   |      68|       3.059|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 114   |     758|       3.677|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 115   |     401|     192.920|   1.9%/ 37|   1.5%/ 45|   1.4%/ 48|   1.3%/ 52 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 123   |     253|      47.135|   0.1%/830|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 106   |     276|      59.074|   3.1%/ 22|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 118   |    5470|      24.941|   1.5%/ 45|   1.3%/ 53|   1.2%/ 55|   1.2%/ 58 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 126   |     964|     228.474|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 116   |      24|       3.383|   2.5%/ 28|   2.5%/ 27|   2.5%/ 28|   2.5%/ 28 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 117   |   12348|     384.282|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 164   |    1399|      12.895|   0.6%/108|   0.6%/124|   0.5%/128|   0.5%/133 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 125   |    1601|      41.710|   0.6%/122|   0.5%/153|   0.4%/164|   0.4%/176 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 120   |    1672|     162.663|   0.4%/173|   0.4%/168|   0.4%/167|   0.4%/166 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 109   |     154|      56.062|   1.9%/ 36|   1.8%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 115   |    1932|      99.558|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 118   |   11683|      79.616|   1.6%/ 45|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  46   |       4|       0.344|   0.0%/ ***|  10.1%/  7|  10.1%/  7|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 113   |    2366|      69.151|   2.3%/ 29|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 105   |     158|       9.758|   2.1%/ 33|   1.4%/ 48|   1.2%/ 56|   1.1%/ 66 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 117   |     401|      57.550|   3.0%/ 23|   3.8%/ 18|   4.0%/ 17|   4.2%/ 16 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  83   |      64|       8.081|   0.4%/177|   0.2%/357|   0.1%/488|   0.1%/771 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 116   |      26|       4.586|   0.1%/702|   0.2%/412|   0.2%/371|   0.2%/337 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 109   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 123   |     111|      53.204|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  98   |      93|       5.859|   0.2%/318|   0.3%/272|   0.3%/265|   0.3%/259 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 110   |    4395|      74.778|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 134   |   28452|     604.079|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 109   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 124   |     668|      15.736|   0.9%/ 81|   0.7%/ 99|   0.7%/105|   0.6%/111 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 126   |    5584|     540.164|   0.3%/252|   0.2%/361|   0.2%/405|   0.2%/460 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 132   |    1969|     228.866|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 108   |      19|       1.099|   2.5%/ 28|   4.6%/ 15|   5.9%/ 12|   9.5%/  7 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 106   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 136   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 110   |      15|       2.028|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 112   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 118   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 120   |    5401|      64.948|   0.4%/189|   0.4%/191|   0.4%/191|   0.4%/192 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 137   |  136757|     414.989|   0.5%/135|   0.5%/143|   0.5%/145|   0.5%/146 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 124   |    1444|      34.481|   1.5%/ 47|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 117   |     336|      33.939|   0.4%/155|   0.4%/157|   0.4%/158|   0.4%/159 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 126   |   45143|     679.501|   0.2%/360|   0.2%/431|   0.2%/453|   0.1%/477 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 108   |      31|       8.785|   1.1%/ 65|   1.1%/ 60|   1.2%/ 59|   1.2%/ 57 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 110   |      68|       1.989|   7.4%/  9|   8.5%/  8|   8.7%/  8|   8.9%/  8 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 110   |      99|       3.071|   4.7%/ 15|   4.5%/ 15|   4.4%/ 16|   4.3%/ 16 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 104   |      48|       2.666|  11.9%/  6|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 114   |      11|       0.714|   9.0%/  8|  12.1%/  6|  12.9%/  5|  13.8%/  5 |

