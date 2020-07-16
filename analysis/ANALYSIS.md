# State and Country COVID-19 Analysis #
## Updated: at 2020-07-16 for data as of 2020-07-15 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.8% of deaths and 38.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.5% of deaths and 57.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 124   |   32599|    1675.746|   0.1%/822|   0.1%/959|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 128   |   15880|    1787.858|   0.3%/273|   0.3%/269|   0.3%/269|   0.3%/268 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 118   |    8381|    1206.003|   0.2%/307|   0.2%/352|   0.2%/366|   0.2%/380 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 121   |    7479|     590.217|   0.4%/159|   0.4%/166|   0.4%/169|   0.4%/171 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 134   |    7307|     184.925|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 119   |    6966|     544.160|   0.3%/241|   0.3%/269|   0.3%/276|   0.2%/284 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 119   |    6338|     634.619|   0.2%/417|   0.2%/421|   0.2%/421|   0.2%/422 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 130   |    4402|     204.969|   1.7%/ 42|   1.8%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 119   |    4371|    1226.062|   0.1%/734|   0.1%/756|   0.1%/754|   0.1%/749 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 121   |    3376|     116.443|   2.3%/ 30|   2.7%/ 26|   2.8%/ 25|   2.9%/ 24 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 138   |  137445|     417.077|   0.5%/136|   0.5%/142|   0.5%/143|   0.5%/145 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 121   |   75806|     358.572|   1.5%/ 45|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 127   |   45212|     680.540|   0.2%/369|   0.2%/437|   0.2%/458|   0.1%/481 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 119   |   37358|     295.135|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 146   |   35019|     581.334|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 152   |   30084|     448.512|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 135   |   28440|     603.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 127   |   24973|      18.346|   2.4%/ 28|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 147   |   13341|     160.012|   1.5%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 118   |   12526|     389.838|   1.7%/ 41|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 113   |    1173|     239.319|   1.5%/ 46|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 113   |      18|      24.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 117   |    2364|     324.782|   2.6%/ 27|   2.7%/ 25|   2.8%/ 25|   2.8%/ 24 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 114   |     337|     111.587|   1.4%/ 48|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 134   |    7307|     184.925|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 124   |    1736|     301.453|   0.2%/315|   0.2%/301|   0.2%/296|   0.2%/290 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 119   |    4371|    1226.062|   0.1%/734|   0.1%/756|   0.1%/754|   0.1%/749 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 112   |     521|     534.745|   0.1%/519|   0.1%/518|   0.1%/520|   0.1%/522 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 130   |    4402|     204.969|   1.7%/ 42|   1.8%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 126   |    3057|     287.969|   0.6%/109|   0.7%/102|   0.7%/100|   0.7%/ 98 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 107   |      20|      13.843|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 112   |     104|      58.102|   0.9%/ 78|   1.1%/ 62|   1.2%/ 59|   1.2%/ 56 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 121   |    7479|     590.217|   0.4%/159|   0.4%/166|   0.4%/169|   0.4%/171 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 122   |    2793|     414.931|   0.3%/205|   0.3%/232|   0.3%/241|   0.3%/250 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 113   |     763|     241.732|   0.5%/134|   0.6%/118|   0.6%/115|   0.6%/111 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 125   |     304|     104.205|   0.6%/107|   0.6%/116|   0.6%/118|   0.6%/121 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 122   |     642|     143.732|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 124   |    3453|     742.863|   0.5%/147|   0.5%/139|   0.5%/138|   0.5%/136 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 111   |     115|      85.376|   0.6%/118|   0.6%/109|   0.6%/107|   0.7%/106 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 119   |    3351|     554.351|   0.3%/222|   0.3%/256|   0.3%/265|   0.3%/276 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 118   |    8381|    1206.003|   0.2%/307|   0.2%/352|   0.2%/366|   0.2%/380 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 119   |    6338|     634.619|   0.2%/417|   0.2%/421|   0.2%/421|   0.2%/422 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 117   |    1560|     276.636|   0.3%/205|   0.3%/251|   0.3%/266|   0.2%/282 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 119   |    1286|     432.035|   1.2%/ 56|   1.3%/ 54|   1.3%/ 54|   1.3%/ 53 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 119   |    1118|     182.147|   0.6%/109|   0.7%/106|   0.7%/106|   0.7%/105 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 111   |      32|      29.969|   3.2%/ 21|   4.4%/ 16|   4.7%/ 15|   5.0%/ 14 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 110   |     291|     150.447|   0.4%/197|   0.1%/510|   0.1%/813|   0.0%/ *** |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 122   |     609|     197.787|   1.3%/ 55|   1.5%/ 47|   1.5%/ 46|   1.6%/ 44 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 115   |     397|     292.111|   0.4%/177|   0.2%/309|   0.2%/377|   0.1%/483 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 128   |   15880|    1787.858|   0.3%/273|   0.3%/269|   0.3%/269|   0.3%/268 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 113   |     556|     265.035|   0.7%/ 94|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 124   |   32599|    1675.746|   0.1%/822|   0.1%/959|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 113   |    1565|     149.204|   0.9%/ 74|   1.0%/ 69|   1.0%/ 67|   1.1%/ 66 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 111   |      88|     115.866|   0.7%/ 98|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 118   |    3098|     265.019|   0.5%/133|   0.5%/143|   0.5%/146|   0.5%/150 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 119   |     430|     108.580|   0.7%/ 95|   0.8%/ 88|   0.8%/ 87|   0.8%/ 85 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 123   |     243|      57.610|   1.2%/ 57|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 119   |    6966|     544.160|   0.3%/241|   0.3%/269|   0.3%/276|   0.2%/284 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 117   |     168|      52.547|   0.8%/ 91|   1.0%/ 72|   1.0%/ 68|   1.1%/ 64 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 110   |     990|     934.540|   0.3%/236|   0.2%/323|   0.2%/352|   0.2%/386 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 122   |    1010|     196.082|   2.0%/ 35|   2.0%/ 34|   2.1%/ 34|   2.1%/ 33 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 127   |     111|     125.747|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 117   |     777|     113.702|   1.7%/ 40|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 121   |    3376|     116.443|   2.3%/ 30|   2.7%/ 26|   2.8%/ 25|   2.9%/ 24 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 138   |  137445|     417.077|   0.5%/136|   0.5%/142|   0.5%/143|   0.5%/145 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 116   |     226|      70.583|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 118   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 124   |    2020|     236.628|   0.8%/ 90|   0.7%/106|   0.6%/111|   0.6%/117 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 138   |    1437|     188.722|   0.4%/177|   0.3%/222|   0.3%/239|   0.3%/259 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 108   |      97|      54.222|   0.3%/203|   0.4%/174|   0.4%/167|   0.4%/160 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 118   |     830|     142.493|   0.4%/189|   0.3%/224|   0.3%/234|   0.3%/245 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  94   |      22|      37.446|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 116   |    1094|      33.961|   2.3%/ 30|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 127   |     104|      36.441|   3.3%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 126   |    1038|      24.136|   0.8%/ 81|   0.8%/ 82|   0.8%/ 83|   0.8%/ 83 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 109   |      28|       0.905|   4.7%/ 15|   3.7%/ 19|   3.4%/ 20|   3.1%/ 22 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 130   |    2037|      45.323|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 112   |     598|     202.168|   2.0%/ 35|   1.8%/ 38|   1.8%/ 39|   1.7%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 137   |     109|       4.246|   0.5%/149|   0.6%/116|   0.6%/110|   0.7%/104 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 126   |     710|      79.776|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 125   |     336|      33.402|   2.9%/ 24|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 122   |     116|      75.465|   1.9%/ 36|   1.4%/ 48|   1.3%/ 52|   1.2%/ 57 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 120   |    2514|      14.924|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 107   |     483|      51.383|   1.3%/ 53|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 127   |    9796|     850.056|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 101   |      27|       2.303|   1.7%/ 40|   2.7%/ 26|   2.9%/ 24|   3.1%/ 22 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 109   |    2034|     177.355|   3.6%/ 19|   3.1%/ 22|   3.0%/ 23|   2.8%/ 24 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 117   |     231|      70.053|   1.5%/ 46|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 107   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 121   |   75806|     358.572|   1.5%/ 45|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 127   |     286|      41.117|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 120   |      53|       2.540|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  94   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 113   |     367|      13.826|   0.5%/140|   0.5%/133|   0.5%/132|   0.5%/133 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 129   |    8884|     233.809|   0.2%/459|   0.1%/600|   0.1%/649|   0.1%/708 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  54   |      53|       9.706|   1.3%/ 55|   0.2%/338|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  79   |      75|       4.611|   0.1%/625|   0.2%/317|   0.2%/279|   0.3%/248 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 116   |    7387|     386.617|   1.6%/ 44|   1.1%/ 62|   1.0%/ 69|   0.9%/ 77 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 127   |    4641|       3.310|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 116   |    6088|     123.256|   3.9%/ 18|   3.7%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 119   |      36|       7.188|   6.6%/ 10|   7.5%/  9|   7.7%/  9|   7.9%/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 119   |     120|      29.507|   0.7%/104|   0.8%/ 88|   0.8%/ 85|   0.8%/ 82 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 120   |      87|       7.754|   0.1%/655|   0.1%/593|   0.1%/574|   0.1%/554 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 124   |     611|     104.869|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 121   |     925|      89.297|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 124   |    5183|     296.688|   0.8%/ 83|   0.8%/ 88|   0.8%/ 90|   0.8%/ 91 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 130   |    4187|      41.755|   2.2%/ 32|   1.8%/ 38|   1.7%/ 40|   1.6%/ 42 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 107   |     296|      45.583|   3.4%/ 20|   2.4%/ 28|   2.2%/ 32|   1.9%/ 35 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  85   |      54|      39.406|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 102   |     138|       1.395|   2.5%/ 28|   2.9%/ 24|   3.0%/ 23|   3.2%/ 22 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 117   |     329|      59.553|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 152   |   30084|     448.512|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 118   |      48|      21.887|   0.6%/122|   0.2%/442|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 115   |       3|       1.388|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 103   |      15|       4.048|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 129   |    9094|     109.370|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 117   |     145|       4.781|   1.5%/ 46|   1.0%/ 71|   0.9%/ 81|   0.7%/ 94 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 127   |     193|      18.041|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 122   |    1364|      82.137|   3.7%/ 19|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  92   |      38|       3.134|   1.2%/ 59|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  81   |      26|      16.369|   0.7%/106|   0.3%/219|   0.2%/281|   0.2%/388 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 102   |     145|      12.544|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 112   |     860|      93.861|   2.9%/ 24|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 123   |     597|      61.107|   0.1%/528|   0.1%/746|   0.1%/829|   0.1%/933 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 127   |   24973|      18.346|   2.4%/ 28|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 127   |    3805|      14.255|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 147   |   13341|     160.012|   1.5%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 134   |    3741|      95.597|   3.8%/ 18|   2.9%/ 24|   2.7%/ 26|   2.5%/ 28 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 127   |    1749|     355.407|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 117   |     370|      40.221|   1.1%/ 64|   1.3%/ 53|   1.3%/ 51|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 146   |   35019|     581.334|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 119   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 154   |     990|       7.858|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 111   |      10|       0.960|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 113   |     379|      20.307|   0.2%/440|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 112   |     201|       4.236|   2.4%/ 28|   2.8%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 112   |     119|      66.540|   5.0%/ 14|   6.5%/ 10|   6.9%/ 10|   7.2%/  9 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 103   |     400|      90.435|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89|   0.8%/ 90 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 104   |     173|      26.492|   6.6%/ 10|   5.9%/ 12|   5.7%/ 12|   5.5%/ 12 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 104   |      31|      16.025|   0.3%/234|   0.5%/134|   0.6%/120|   0.6%/108 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 128   |      37|       5.467|   0.6%/126|   0.5%/138|   0.5%/142|   0.5%/146 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 103   |      52|      11.511|   2.8%/ 24|   3.6%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 105   |      46|       6.648|   3.8%/ 18|   1.7%/ 40|   3.4%/ 20|   3.3%/ 21 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 117   |      79|      28.399|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  60   |      40|       1.517|   3.3%/ 21|   3.2%/ 21|   3.4%/ 20|   3.6%/ 19 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 121   |     122|       3.718|   0.1%/ ***|   0.1%/716|   0.1%/660|   0.1%/612 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 109   |     122|       6.042|   0.3%/232|   0.2%/414|   0.1%/520|   0.1%/706 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 108   |     151|      36.988|   1.0%/ 66|   0.9%/ 76|   0.9%/ 79|   0.8%/ 83 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 119   |   37358|     295.135|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 120   |     672|     250.417|   1.3%/ 54|   1.1%/ 62|   1.1%/ 64|   1.0%/ 66 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 128   |     256|       7.140|   1.0%/ 70|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  52   |       9|       0.306|   3.8%/ 18|   0.8%/ 88|   0.1%/581|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  61   |      39|       1.300|   1.7%/ 41|   1.3%/ 52|   1.3%/ 54|   1.2%/ 55 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 132   |    6163|     353.025|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 109   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 111   |      98|      15.118|   1.4%/ 49|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 113   |      68|       3.067|   0.1%/728|   0.1%/748|   0.1%/761|   0.1%/775 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 115   |     770|       3.734|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 116   |     406|     195.378|   1.8%/ 39|   1.4%/ 50|   1.3%/ 54|   1.2%/ 59 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 124   |     253|      47.169|   0.1%/800|   0.1%/972|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 107   |     283|      60.729|   3.1%/ 22|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 119   |    5528|      25.204|   1.5%/ 47|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 127   |     991|     234.949|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 117   |      25|       3.471|   2.7%/ 25|   2.9%/ 24|   2.9%/ 23|   3.0%/ 23 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 118   |   12526|     389.838|   1.7%/ 41|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 165   |    1409|      12.982|   0.8%/ 92|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 126   |    1607|      41.871|   0.6%/125|   0.4%/156|   0.4%/166|   0.4%/178 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 121   |    1678|     163.313|   0.4%/176|   0.4%/176|   0.4%/176|   0.4%/177 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 110   |     156|      56.799|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 116   |    1953|     100.654|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 119   |   11846|      80.724|   1.5%/ 45|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  47   |       4|       0.344|   0.0%/ --|   4.5%/ 15|   4.1%/ 17|   3.5%/ 20 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 114   |    2402|      70.208|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.6%/ 42 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 106   |     159|       9.833|   2.0%/ 35|   1.2%/ 55|   1.1%/ 65|   0.9%/ 79 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 118   |     417|      59.858|   3.2%/ 21|   4.0%/ 17|   4.2%/ 16|   4.4%/ 15 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  84   |      64|       8.106|   0.4%/183|   0.2%/286|   0.2%/336|   0.2%/403 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 117   |      26|       4.616|   0.2%/321|   0.4%/194|   0.4%/175|   0.4%/159 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 110   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 124   |     111|      53.194|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  99   |      93|       5.867|   0.2%/342|   0.2%/327|   0.2%/327|   0.2%/327 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 111   |    4535|      77.155|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 135   |   28440|     603.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 110   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 125   |     673|      15.848|   0.9%/ 81|   0.7%/ 96|   0.7%/100|   0.7%/105 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 127   |    5594|     541.135|   0.3%/259|   0.2%/359|   0.2%/397|   0.2%/444 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 133   |    1969|     228.878|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 109   |      21|       1.185|   0.0%/ --|   5.9%/ 12|   9.5%/  7|  11.2%/  6 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 107   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 137   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 111   |      15|       2.027|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 113   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 119   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 121   |    5420|      65.178|   0.4%/190|   0.4%/191|   0.4%/192|   0.4%/192 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 138   |  137445|     417.077|   0.5%/136|   0.5%/142|   0.5%/143|   0.5%/145 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 125   |    1462|      34.903|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 118   |     337|      34.051|   0.4%/163|   0.4%/172|   0.4%/175|   0.4%/177 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 127   |   45212|     680.540|   0.2%/369|   0.2%/437|   0.2%/458|   0.1%/481 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 109   |      31|       8.854|   1.0%/ 72|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 111   |      73|       2.140|   7.2%/  9|   8.0%/  9|   8.1%/  8|   8.3%/  8 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 111   |     103|       3.193|   4.6%/ 15|   4.3%/ 16|   4.3%/ 16|   4.2%/ 16 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 105   |      48|       2.675|   3.4%/ 20|   1.7%/ 42|   1.2%/ 59|   0.7%/100 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 115   |      21|       1.396|   8.8%/  8|  11.2%/  6|  11.8%/  6|  12.5%/  5 |

