# State and Country COVID-19 Analysis #
## Updated: at 2020-07-09 for data as of 2020-07-08 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 37.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Florida and California have followed nearly identical trajectories since early April 2020.
 
For confirmed cases, the story is not so different.

![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to date from COVID-19 compared to historical seasonal flus and 20th century pandemics.  The number of deaths is scaled by the ratio of the current US population to the size of the population at the time of the flu/pandemic.   In all cases the midpoint CDC estimate for fatalities is used.  In all cases except the Spanish Flu (1918) these are for a full year.

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.4% of deaths and 53.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 117   |   32378|    1664.368|   0.1%/554|   0.1%/605|   0.1%/621|   0.1%/637 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 121   |   15823|    1781.430|   0.2%/302|   0.2%/335|   0.2%/343|   0.2%/351 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 111   |    8256|    1188.035|   0.3%/258|   0.2%/315|   0.2%/333|   0.2%/352 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 114   |    7198|     568.070|   0.5%/136|   0.5%/133|   0.5%/131|   0.5%/129 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 112   |    6832|     533.666|   0.3%/223|   0.3%/272|   0.2%/289|   0.2%/308 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 127   |    6643|     168.122|   1.1%/ 63|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 112   |    6259|     626.744|   0.2%/449|   0.1%/475|   0.1%/483|   0.1%/492 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 112   |    4356|    1221.678|   0.1%/724|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 123   |    3876|     180.463|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 117   |    3333|     716.983|   0.4%/171|   0.4%/174|   0.4%/175|   0.4%/176 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 131   |  132668|     402.579|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/150 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 114   |   68296|     323.046|   1.7%/ 41|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 120   |   44700|     672.826|   0.2%/303|   0.2%/360|   0.2%/378|   0.2%/399 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 139   |   34945|     580.109|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 112   |   33389|     263.784|   2.2%/ 31|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 145   |   29990|     447.099|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 128   |   28581|     606.806|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 120   |   21480|      15.780|   2.6%/ 27|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 140   |   12012|     144.067|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 111   |   11264|     350.562|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 106   |    1054|     214.964|   1.2%/ 56|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 106   |      17|      22.980|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 110   |    1967|     270.293|   2.1%/ 33|   2.0%/ 35|   2.0%/ 35|   1.9%/ 36 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 107   |     308|     101.914|   1.7%/ 40|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 127   |    6643|     168.122|   1.1%/ 63|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 117   |    1711|     297.171|   0.1%/505|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 112   |    4356|    1221.678|   0.1%/724|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 105   |     527|     540.847|   0.1%/489|   0.1%/676|   0.1%/729|   0.1%/784 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 123   |    3876|     180.463|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 119   |    2931|     276.018|   0.5%/134|   0.4%/177|   0.4%/192|   0.3%/209 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 100   |      19|      13.560|   0.7%/ 92|   0.7%/ 93|   0.7%/ 94|   0.7%/ 96 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 105   |      95|      52.965|   0.4%/158|   0.5%/128|   0.6%/122|   0.6%/116 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 114   |    7198|     568.070|   0.5%/136|   0.5%/133|   0.5%/131|   0.5%/129 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 115   |    2732|     405.772|   0.4%/168|   0.4%/192|   0.3%/198|   0.3%/205 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 106   |     734|     232.736|   0.4%/179|   0.4%/197|   0.3%/203|   0.3%/209 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 118   |     291|      99.776|   0.7%/ 96|   0.7%/ 98|   0.7%/ 98|   0.7%/ 99 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 115   |     605|     135.429|   0.8%/ 84|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 117   |    3333|     716.983|   0.4%/171|   0.4%/174|   0.4%/175|   0.4%/176 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 104   |     109|      81.275|   0.5%/134|   0.7%/102|   0.7%/ 96|   0.8%/ 90 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 112   |    3286|     543.570|   0.4%/188|   0.3%/231|   0.3%/244|   0.3%/259 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 111   |    8256|    1188.035|   0.3%/258|   0.2%/315|   0.2%/333|   0.2%/352 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 112   |    6259|     626.744|   0.2%/449|   0.1%/475|   0.1%/483|   0.1%/492 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 110   |    1531|     271.392|   0.4%/159|   0.3%/209|   0.3%/226|   0.3%/247 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 112   |    1165|     391.435|   1.1%/ 63|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 112   |    1073|     174.762|   0.6%/114|   0.5%/133|   0.5%/138|   0.5%/143 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 104   |      23|      21.878|   0.7%/106|   0.4%/161|   0.4%/185|   0.3%/217 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 103   |     290|     149.946|   0.7%/101|   0.3%/222|   0.2%/322|   0.1%/598 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 115   |     546|     177.209|   0.8%/ 84|   0.9%/ 73|   1.0%/ 71|   1.0%/ 68 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 108   |     390|     287.103|   0.7%/104|   0.5%/138|   0.5%/152|   0.4%/168 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 121   |   15823|    1781.430|   0.2%/302|   0.2%/335|   0.2%/343|   0.2%/351 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 106   |     525|     250.160|   0.6%/109|   0.6%/120|   0.6%/122|   0.6%/125 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 117   |   32378|    1664.368|   0.1%/554|   0.1%/605|   0.1%/621|   0.1%/637 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 106   |    1472|     140.392|   0.8%/ 86|   0.6%/122|   0.5%/136|   0.5%/154 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 104   |      82|     108.190|   0.5%/129|   0.7%/105|   0.7%/ 99|   0.7%/ 94 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 111   |    2981|     255.017|   0.6%/120|   0.5%/127|   0.5%/128|   0.5%/130 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 112   |     406|     102.613|   0.6%/123|   0.6%/116|   0.6%/115|   0.6%/114 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 116   |     221|      52.454|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76|   0.9%/ 76 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 112   |    6832|     533.666|   0.3%/223|   0.3%/272|   0.2%/289|   0.2%/308 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 110   |     157|      49.209|   0.4%/191|   0.4%/173|   0.4%/169|   0.4%/165 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 103   |     977|     922.396|   0.4%/168|   0.3%/239|   0.3%/270|   0.2%/310 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 115   |     861|     167.191|   1.7%/ 39|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 120   |     101|     113.985|   1.0%/ 69|   0.8%/ 87|   0.7%/ 93|   0.7%/101 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 110   |     677|      99.017|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 114   |    2773|      95.625|   1.5%/ 45|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 131   |  132668|     402.579|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/150 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 109   |     193|      60.218|   1.5%/ 46|   1.8%/ 39|   1.8%/ 38|   1.9%/ 36 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 111   |      56|      89.800|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 117   |    1906|     223.340|   0.9%/ 75|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 131   |    1388|     182.291|   0.5%/127|   0.5%/129|   0.5%/129|   0.5%/130 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 101   |      95|      53.136|   0.3%/209|   0.3%/257|   0.3%/270|   0.2%/282 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 111   |     812|     139.446|   0.4%/156|   0.3%/237|   0.3%/272|   0.2%/319 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  87   |      20|      35.351|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 109   |     942|      29.244|   2.8%/ 24|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 120   |      85|      29.703|   4.0%/ 17|   4.2%/ 16|   4.3%/ 16|   4.3%/ 16 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 119   |     980|      22.786|   0.9%/ 81|   0.8%/ 90|   0.8%/ 92|   0.7%/ 95 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 102   |      22|       0.708|   5.7%/ 12|   6.2%/ 11|   6.3%/ 11|   6.3%/ 11 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 123   |    1666|      37.074|   3.1%/ 22|   3.2%/ 22|   3.2%/ 21|   3.2%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 105   |     524|     177.124|   2.2%/ 32|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 130   |     106|       4.117|   0.2%/314|   0.3%/264|   0.3%/253|   0.3%/243 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 119   |     710|      79.735|   0.1%/619|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 118   |     278|      27.579|   3.4%/ 20|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 115   |     108|      69.691|   2.5%/ 27|   1.5%/ 47|   1.2%/ 57|   0.9%/ 73 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 113   |    2214|      13.144|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 100   |     442|      46.968|   1.5%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 120   |    9785|     849.088|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  94   |      23|       1.996|   3.4%/ 20|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 102   |    1610|     140.387|   4.3%/ 16|   4.4%/ 16|   4.4%/ 16|   4.4%/ 16 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 110   |     202|      61.269|   1.3%/ 54|   1.6%/ 43|   1.7%/ 41|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 100   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 114   |   68296|     323.046|   1.7%/ 41|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 120   |     258|      37.046|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 113   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  87   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 106   |     333|      12.531|   0.7%/ 99|   0.8%/ 84|   0.9%/ 79|   0.9%/ 73 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 122   |    8811|     231.875|   0.2%/332|   0.2%/447|   0.1%/487|   0.1%/534 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  47   |      52|       9.521|   1.3%/ 52|   2.0%/ 35|   2.3%/ 30|   2.7%/ 26 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  72   |      74|       4.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 109   |    6811|     356.436|   2.3%/ 30|   1.7%/ 41|   1.5%/ 45|   1.4%/ 51 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 120   |    4642|       3.310|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 109   |    4706|      95.262|   4.2%/ 17|   4.0%/ 17|   3.9%/ 17|   3.9%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 112   |      22|       4.414|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 112   |     113|      27.724|   0.4%/188|   0.5%/134|   0.6%/124|   0.6%/116 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 113   |      86|       7.699|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 117   |     609|     104.509|   0.1%/923|   0.1%/952|   0.1%/956|   0.1%/958 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 114   |     828|      79.973|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 117   |    4905|     280.824|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 123   |    3711|      37.008|   2.8%/ 25|   2.3%/ 31|   2.1%/ 32|   2.0%/ 35 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 100   |     253|      39.052|   5.0%/ 14|   4.1%/ 17|   3.9%/ 18|   3.6%/ 19 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  78   |      56|      41.112|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  95   |     114|       1.159|   1.3%/ 54|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 110   |     329|      59.582|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 145   |   29990|     447.099|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 111   |      47|      21.660|   1.6%/ 44|   1.1%/ 62|   1.0%/ 69|   0.9%/ 76 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 108   |       3|       1.130|   4.6%/ 15|   5.0%/ 14|   5.3%/ 13|   5.5%/ 12 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  96   |      15|       4.098|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 122   |    9054|     108.885|   0.1%/801|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 110   |     136|       4.483|   2.5%/ 28|   1.5%/ 45|   1.3%/ 53|   1.1%/ 64 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 120   |     193|      18.024|   0.1%/720|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 115   |    1074|      64.655|   4.0%/ 17|   3.7%/ 19|   3.6%/ 19|   3.5%/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  85   |      35|       2.875|   1.3%/ 53|   0.7%/ 95|   0.6%/122|   0.4%/174 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  74   |      26|      16.106|   2.0%/ 35|   0.4%/168|   0.0%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  95   |     121|      10.419|   1.8%/ 39|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 105   |     709|      77.408|   3.6%/ 19|   3.5%/ 19|   3.5%/ 20|   3.5%/ 20 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 116   |     593|      60.642|   0.2%/416|   0.1%/589|   0.1%/664|   0.1%/764 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 120   |   21480|      15.780|   2.6%/ 27|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 120   |    3342|      12.522|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 140   |   12012|     144.067|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 127   |    3058|      78.159|   5.4%/ 13|   4.4%/ 16|   4.2%/ 16|   3.9%/ 18 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 120   |    1746|     354.762|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 110   |     339|      36.852|   0.7%/ 95|   0.9%/ 77|   0.9%/ 73|   1.0%/ 70 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 139   |   34945|     580.109|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 112   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 147   |     989|       7.850|   0.2%/450|   0.1%/692|   0.1%/806|   0.1%/969 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 104   |      10|       0.949|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 106   |     269|      14.372|   1.8%/ 39|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 105   |     170|       3.583|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.7%/ 42 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 105   |      77|      43.062|   4.1%/ 17|   5.9%/ 12|   6.4%/ 11|   6.9%/ 10 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  96   |     379|      85.758|   0.9%/ 76|   0.9%/ 81|   0.8%/ 82|   0.8%/ 82 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  97   |     110|      16.775|   7.5%/  9|   8.9%/  8|   9.3%/  7|   9.6%/  7 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  97   |      30|      15.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 121   |      36|       5.293|   0.7%/ 94|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  96   |      40|       8.881|   1.4%/ 50|   2.0%/ 35|   2.1%/ 33|   2.3%/ 30 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  98   |      37|       5.383|   4.2%/ 16|   8.0%/  9|   9.0%/  8|   4.0%/ 17 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 110   |      79|      28.406|   0.2%/400|   0.1%/556|   0.1%/616|   0.1%/691 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  53   |      36|       1.381|   7.8%/  9|   6.2%/ 11|   5.5%/ 12|   4.8%/ 14 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 114   |     121|       3.694|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 102   |     120|       5.943|   0.5%/136|   0.4%/163|   0.4%/171|   0.4%/180 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 101   |     138|      33.874|   1.2%/ 59|   0.7%/ 95|   0.6%/111|   0.5%/133 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 112   |   33389|     263.784|   2.2%/ 31|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 113   |     616|     229.571|   1.5%/ 45|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 121   |     239|       6.659|   0.8%/ 89|   1.0%/ 72|   1.0%/ 69|   1.0%/ 66 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  45   |       8|       0.281|   4.3%/ 16|   4.9%/ 14|   4.9%/ 14|   4.8%/ 14 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  54   |      36|       1.202|   2.7%/ 26|   2.2%/ 31|   2.1%/ 34|   1.8%/ 38 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 125   |    6151|     352.367|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 102   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 104   |      90|      13.952|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 106   |      68|       3.050|   0.1%/640|   0.1%/541|   0.1%/519|   0.1%/499 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 108   |     679|       3.296|   1.7%/ 40|   1.7%/ 42|   1.7%/ 42|   1.6%/ 42 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 109   |     366|     176.434|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 117   |     252|      47.017|   0.1%/727|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 100   |     232|      49.810|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 112   |    5082|      23.168|   1.9%/ 36|   1.5%/ 47|   1.4%/ 50|   1.3%/ 54 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 120   |     801|     189.901|   3.0%/ 23|   3.3%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 110   |      21|       2.973|   2.1%/ 33|   2.2%/ 31|   2.3%/ 31|   2.3%/ 31 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 111   |   11264|     350.562|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 158   |    1342|      12.364|   0.7%/100|   0.6%/119|   0.6%/125|   0.5%/132 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 119   |    1556|      40.556|   0.7%/ 97|   0.6%/120|   0.5%/128|   0.5%/137 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 114   |    1627|     158.351|   0.4%/173|   0.5%/147|   0.5%/141|   0.5%/137 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 103   |     136|      49.414|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 109   |    1806|      93.056|   1.1%/ 61|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 112   |   10662|      72.659|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  40   |       3|       0.244|   9.6%/  7|   1.3%/ 54|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 107   |    2082|      60.858|   2.9%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  99   |     144|       8.903|   3.1%/ 22|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 111   |     318|      45.718|   1.7%/ 40|   2.4%/ 29|   2.5%/ 27|   2.7%/ 26 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  77   |      63|       8.019|   0.8%/ 84|   0.5%/133|   0.4%/154|   0.4%/181 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 110   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 103   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 117   |     111|      53.223|   0.1%/954|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  92   |      92|       5.783|   0.2%/334|   0.3%/269|   0.3%/252|   0.3%/235 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 104   |    3553|      60.451|   3.7%/ 18|   3.9%/ 18|   3.9%/ 18|   3.9%/ 17 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 128   |   28581|     606.806|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 103   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 118   |     637|      15.022|   1.0%/ 66|   0.8%/ 86|   0.7%/ 93|   0.7%/101 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 120   |    5514|     533.341|   0.4%/186|   0.3%/243|   0.3%/265|   0.2%/291 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 126   |    1968|     228.750|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 102   |      14|       0.774|   0.0%/ --|  11.9%/  6|  11.9%/  6|   2.5%/ 28 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 100   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 130   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 104   |      15|       1.999|   0.8%/ 92|   0.8%/ 85|   0.8%/ 82|   0.9%/ 80 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 106   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 112   |      50|       4.268|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 114   |    5286|      63.571|   0.4%/189|   0.3%/202|   0.3%/206|   0.3%/210 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 131   |  132668|     402.579|   0.5%/134|   0.5%/144|   0.5%/147|   0.5%/150 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 118   |    1324|      31.618|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 111   |     327|      33.059|   0.5%/147|   0.5%/152|   0.5%/152|   0.5%/153 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 120   |   44700|     672.826|   0.2%/303|   0.2%/360|   0.2%/378|   0.2%/399 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 102   |      29|       8.317|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 104   |      36|       1.061|   5.8%/ 12|   8.2%/  8|   8.8%/  8|   9.4%/  7 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 104   |      75|       2.327|   5.0%/ 14|   5.1%/ 13|   5.1%/ 13|   5.1%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  98   |      40|       2.249|   6.8%/ 10|   5.6%/ 12|   5.4%/ 13|   5.2%/ 13 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 108   |       9|       0.586|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |

