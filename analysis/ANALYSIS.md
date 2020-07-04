# State and Country COVID-19 Analysis #
## Updated: at 2020-07-04 for data as of 2020-07-03 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.
 
For confirmed cases, the story is not so different.

![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to date from COVID-19 compared to historical seasonal flus and 20th century pandemics.

![Compared To Flus](https:f//github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/ComparedToFlus.png)


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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. One per million is 0.0001%.  1% is 10,000 per million.

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDeathRates.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDRG.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 112   |   31968|    1643.307|   0.3%/265|   0.3%/212|   0.3%/201|   0.4%/191 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 116   |   15453|    1739.757|   0.3%/273|   0.2%/343|   0.2%/364|   0.2%/388 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 106   |    8169|    1175.438|   0.3%/225|   0.2%/291|   0.2%/316|   0.2%/345 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 109   |    7049|     556.271|   0.5%/151|   0.3%/213|   0.3%/238|   0.3%/270 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 107   |    6745|     526.854|   0.4%/173|   0.4%/189|   0.4%/193|   0.4%/197 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 122   |    6312|     159.736|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 107   |    6217|     622.471|   0.2%/387|   0.2%/385|   0.2%/383|   0.2%/381 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 107   |    4347|    1219.175|   0.2%/454|   0.1%/696|   0.1%/805|   0.1%/956 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 118   |    3640|     169.484|   1.2%/ 57|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 112   |    3269|     703.188|   0.4%/162|   0.4%/159|   0.4%/159|   0.4%/159 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 126   |  129571|     393.182|   0.6%/116|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 109   |   63188|     298.887|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 115   |   44266|     666.299|   0.3%/243|   0.3%/263|   0.3%/269|   0.3%/275 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 134   |   34896|     579.293|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 140   |   29939|     446.345|   0.1%/971|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 107   |   30578|     241.576|   2.7%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 123   |   28658|     608.448|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 115   |   19425|      14.270|   2.7%/ 26|   2.5%/ 28|   2.5%/ 28|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 135   |   11192|     134.233|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 106   |   10374|     322.855|   2.2%/ 32|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 101   |     996|     203.110|   1.4%/ 48|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 101   |      15|      19.953|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 105   |    1782|     244.883|   2.4%/ 29|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 102   |     290|      95.982|   2.1%/ 32|   1.7%/ 40|   1.6%/ 42|   1.5%/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 122   |    6312|     159.736|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 112   |    1707|     296.371|   0.3%/238|   0.2%/297|   0.2%/314|   0.2%/333 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 107   |    4347|    1219.175|   0.2%/454|   0.1%/696|   0.1%/805|   0.1%/956 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 100   |     531|     544.877|   0.2%/337|   0.1%/718|   0.1%/987|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 118   |    3640|     169.484|   1.2%/ 57|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 114   |    2883|     271.572|   0.7%/102|   0.5%/140|   0.5%/153|   0.4%/168 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  95   |      17|      12.007|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 100   |      92|      51.748|   0.3%/209|   0.4%/192|   0.4%/188|   0.4%/183 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 109   |    7049|     556.271|   0.5%/151|   0.3%/213|   0.3%/238|   0.3%/270 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 110   |    2685|     398.805|   0.5%/147|   0.4%/176|   0.4%/185|   0.4%/194 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 101   |     724|     229.378|   0.5%/150|   0.4%/177|   0.4%/185|   0.4%/192 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 113   |     280|      96.184|   0.8%/ 87|   0.9%/ 78|   0.9%/ 76|   0.9%/ 74 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 110   |     581|     130.142|   0.8%/ 83|   0.9%/ 77|   0.9%/ 76|   0.9%/ 74 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 112   |    3269|     703.188|   0.4%/162|   0.4%/159|   0.4%/159|   0.4%/159 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)|  99   |     105|      78.383|   0.2%/286|   0.2%/288|   0.2%/287|   0.2%/288 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 107   |    3238|     535.577|   0.5%/154|   0.4%/187|   0.4%/198|   0.3%/209 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 106   |    8169|    1175.438|   0.3%/225|   0.2%/291|   0.2%/316|   0.2%/345 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 107   |    6217|     622.471|   0.2%/387|   0.2%/385|   0.2%/383|   0.2%/381 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 105   |    1507|     267.147|   0.6%/118|   0.5%/148|   0.4%/157|   0.4%/166 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 107   |    1106|     371.695|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 107   |    1045|     170.242|   0.7%/ 93|   0.6%/108|   0.6%/113|   0.6%/117 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)|  99   |      23|      21.306|   0.8%/ 82|   0.6%/117|   0.5%/131|   0.5%/150 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  98   |     285|     147.313|   1.2%/ 57|   1.0%/ 67|   1.0%/ 70|   0.9%/ 73 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 110   |     520|     168.979|   0.7%/101|   0.8%/ 91|   0.8%/ 89|   0.8%/ 86 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 103   |     381|     280.046|   0.8%/ 82|   0.7%/ 93|   0.7%/ 97|   0.7%/102 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 116   |   15453|    1739.757|   0.3%/273|   0.2%/343|   0.2%/364|   0.2%/388 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 101   |     510|     243.351|   0.7%/ 97|   0.6%/122|   0.5%/130|   0.5%/138 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 112   |   31968|    1643.307|   0.3%/265|   0.3%/212|   0.3%/201|   0.4%/191 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 101   |    1436|     136.956|   1.1%/ 63|   1.0%/ 72|   0.9%/ 76|   0.9%/ 80 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)|  99   |      80|     105.485|   0.4%/164|   0.4%/181|   0.4%/187|   0.4%/193 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 106   |    2908|     248.782|   0.6%/110|   0.6%/121|   0.6%/125|   0.5%/128 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 107   |     394|      99.612|   0.6%/121|   0.7%/101|   0.7%/ 97|   0.7%/ 93 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 111   |     212|      50.200|   0.9%/ 80|   0.8%/ 91|   0.7%/ 95|   0.7%/ 98 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 107   |    6745|     526.854|   0.4%/173|   0.4%/189|   0.4%/193|   0.4%/197 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 105   |     154|      48.279|   0.3%/251|   0.3%/259|   0.3%/263|   0.3%/268 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  98   |     965|     910.817|   0.6%/111|   0.5%/127|   0.5%/131|   0.5%/134 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 110   |     779|     151.316|   1.6%/ 42|   1.9%/ 37|   2.0%/ 35|   2.0%/ 34 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 115   |      97|     109.152|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 105   |     631|      92.415|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 109   |    2571|      88.652|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 126   |  129571|     393.182|   0.6%/116|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 104   |     179|      55.741|   1.1%/ 61|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 106   |      56|      90.006|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 112   |    1815|     212.633|   1.0%/ 69|   1.2%/ 59|   1.2%/ 57|   1.3%/ 55 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 126   |    1354|     177.845|   0.5%/128|   0.5%/136|   0.5%/138|   0.5%/141 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  96   |      94|      52.511|   0.3%/215|   0.2%/311|   0.2%/366|   0.2%/451 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 106   |     802|     137.707|   0.6%/108|   0.5%/137|   0.5%/147|   0.4%/159 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  82   |      20|      34.713|   0.2%/359|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 104   |     829|      25.723|   2.9%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 115   |      67|      23.632|   4.2%/ 16|   5.1%/ 13|   5.3%/ 13|   5.5%/ 12 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 114   |     944|      21.961|   0.9%/ 75|   0.8%/ 86|   0.8%/ 89|   0.7%/ 93 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  97   |      13|       0.419|   0.0%/ --|  10.9%/  6|  15.6%/  4|  11.5%/  6 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 118   |    1431|      31.850|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 100   |     485|     163.886|   2.7%/ 26|   2.2%/ 32|   2.0%/ 34|   1.9%/ 37 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 125   |     104|       4.064|   0.1%/658|   0.1%/625|   0.1%/627|   0.1%/632 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 114   |     708|      79.535|   0.2%/357|   0.2%/411|   0.2%/428|   0.2%/448 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 113   |     238|      23.626|   3.6%/ 19|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 110   |     100|      64.705|   4.1%/ 17|   3.4%/ 20|   3.2%/ 22|   3.0%/ 23 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 108   |    1993|      11.829|   2.6%/ 26|   2.4%/ 29|   2.3%/ 30|   2.3%/ 31 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  95   |     411|      43.690|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 115   |    9765|     847.332|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  89   |      22|       1.878|   5.6%/ 12|   5.4%/ 13|   5.4%/ 13|   5.5%/ 12 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  97   |    1282|     111.783|   4.4%/ 15|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 105   |     189|      57.286|   0.9%/ 76|   1.1%/ 62|   1.2%/ 59|   1.2%/ 56 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  95   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 109   |   63188|     298.887|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 115   |     239|      34.383|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 108   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  82   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 101   |     324|      12.191|   0.5%/128|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 117   |    8748|     230.207|   0.3%/247|   0.2%/326|   0.2%/353|   0.2%/385 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  42   |      48|       8.777|   5.8%/ 12|   1.7%/ 41|   0.8%/ 89|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  67   |      74|       4.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 104   |    6266|     327.931|   3.1%/ 22|   2.3%/ 30|   2.1%/ 33|   1.9%/ 36 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 115   |    4642|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 104   |    3836|      77.664|   4.4%/ 16|   4.4%/ 16|   4.4%/ 16|   4.4%/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 107   |      17|       3.341|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 107   |     108|      26.614|   0.2%/450|   0.3%/272|   0.3%/245|   0.3%/221 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 108   |      86|       7.693|   0.1%/602|   0.1%/739|   0.1%/782|   0.1%/833 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 112   |     607|     104.227|   0.1%/896|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 109   |     778|      75.074|   1.3%/ 51|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 112   |    4679|     267.848|   0.9%/ 73|   0.9%/ 75|   0.9%/ 76|   0.9%/ 76 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 118   |    3329|      33.202|   3.4%/ 20|   3.0%/ 23|   2.9%/ 24|   2.7%/ 25 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  95   |     204|      31.504|   6.0%/ 11|   6.4%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  73   |      38|      27.614|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  90   |     110|       1.118|   2.8%/ 24|   2.0%/ 34|   1.8%/ 38|   1.6%/ 43 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 105   |     329|      59.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 140   |   29939|     446.345|   0.1%/971|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 106   |      46|      20.944|   1.9%/ 36|   1.0%/ 70|   0.7%/ 93|   0.5%/138 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 103   |       2|       0.983|   3.7%/ 19|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  91   |      15|       4.047|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 117   |    9024|     108.527|   0.1%/622|   0.1%/747|   0.1%/787|   0.1%/831 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 105   |     129|       4.274|   3.6%/ 19|   2.3%/ 30|   2.0%/ 35|   1.6%/ 42 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 115   |     193|      18.009|   0.2%/426|   0.1%/811|   0.1%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 110   |     894|      53.832|   4.4%/ 16|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  80   |      34|       2.752|   1.7%/ 39|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  69   |      26|      15.937|   3.4%/ 20|   2.3%/ 29|   2.1%/ 34|   1.8%/ 39 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  90   |     111|       9.624|   2.0%/ 34|   1.8%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 100   |     581|      63.433|   4.1%/ 17|   4.9%/ 14|   5.1%/ 13|   5.3%/ 13 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 111   |     589|      60.240|   0.2%/279|   0.2%/300|   0.2%/304|   0.2%/309 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 115   |   19425|      14.270|   2.7%/ 26|   2.5%/ 28|   2.5%/ 28|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 115   |    3036|      11.373|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 135   |   11192|     134.233|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 122   |    2470|      63.128|   6.7%/ 10|   5.9%/ 12|   5.6%/ 12|   5.4%/ 13 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 115   |    1742|     353.961|   0.1%/665|   0.1%/728|   0.1%/747|   0.1%/767 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 105   |     324|      35.317|   0.5%/144|   0.6%/118|   0.6%/113|   0.6%/108 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 134   |   34896|     579.293|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 107   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 142   |     985|       7.817|   0.2%/294|   0.2%/336|   0.2%/351|   0.2%/369 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)|  99   |       9|       0.844|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 101   |     212|      11.370|   4.1%/ 17|   2.8%/ 24|   2.5%/ 27|   2.2%/ 31 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 100   |     157|       3.299|   2.0%/ 34|   1.7%/ 41|   1.6%/ 43|   1.5%/ 46 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 100   |      56|      31.035|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  91   |     364|      82.394|   1.0%/ 69|   0.8%/ 89|   0.7%/ 96|   0.7%/104 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  92   |      72|      11.068|   6.3%/ 11|   7.7%/  9|   8.0%/  8|   8.4%/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  92   |      30|      15.797|   0.1%/601|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 116   |      35|       5.066|   0.6%/112|   0.7%/ 95|   0.8%/ 91|   0.8%/ 87 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  91   |      37|       8.217|   0.9%/ 80|   1.2%/ 59|   1.3%/ 55|   1.4%/ 51 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  93   |      28|       4.144|   0.0%/ --|   6.0%/ 11|   4.2%/ 16|   4.0%/ 17 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 105   |      79|      28.201|   0.2%/344|   0.1%/473|   0.1%/526|   0.1%/595 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  48   |      25|       0.966|   3.8%/ 18|   7.1%/ 10|   8.0%/  9|   8.9%/  8 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 109   |     121|       3.698|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  97   |     118|       5.814|   0.6%/114|   0.5%/142|   0.5%/151|   0.4%/161 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  96   |     136|      33.302|   1.4%/ 51|   0.5%/148|   0.2%/281|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 107   |   30578|     241.576|   2.7%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 108   |     576|     214.737|   1.7%/ 41|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 116   |     228|       6.346|   0.6%/123|   0.7%/ 94|   0.8%/ 88|   0.8%/ 83 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  40   |       6|       0.207|   1.2%/ 60|   2.8%/ 24|   2.3%/ 29|   1.6%/ 42 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  49   |      32|       1.058|   3.2%/ 21|   2.5%/ 28|   2.3%/ 29|   2.2%/ 31 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 120   |    6140|     351.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  97   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)|  99   |      84|      13.064|   0.0%/ --|   3.9%/ 18|   3.9%/ 18|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 101   |      68|       3.026|   0.1%/610|   0.1%/594|   0.1%/574|   0.1%/546 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 103   |     627|       3.042|   1.9%/ 37|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 104   |     330|     158.810|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 112   |     252|      46.924|   0.2%/375|   0.2%/412|   0.2%/425|   0.2%/439 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  95   |     193|      41.409|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 107   |    4758|      21.692|   2.4%/ 29|   1.7%/ 40|   1.5%/ 45|   1.4%/ 50 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 115   |     681|     161.411|   2.5%/ 28|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 105   |      18|       2.533|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 106   |   10374|     322.855|   2.2%/ 32|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 153   |    1302|      12.003|   0.9%/ 79|   0.8%/ 84|   0.8%/ 86|   0.8%/ 87 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 114   |    1512|      39.396|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 109   |    1588|     154.493|   0.3%/228|   0.4%/192|   0.4%/184|   0.4%/177 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  98   |     123|      44.714|   2.1%/ 32|   1.4%/ 49|   1.2%/ 56|   1.1%/ 65 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 104   |    1699|      87.547|   1.0%/ 68|   1.1%/ 65|   1.1%/ 65|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 107   |    9869|      67.255|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  35   |       3|       0.261|   0.0%/ --|   9.0%/  8|  13.0%/  5|  17.0%/  4 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 102   |    1816|      53.069|   3.1%/ 22|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  94   |     124|       7.674|   3.5%/ 20|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 106   |     280|      40.244|   0.8%/ 83|   1.1%/ 61|   1.2%/ 57|   1.3%/ 53 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  72   |      62|       7.837|   1.1%/ 64|   0.7%/ 94|   0.6%/109|   0.5%/131 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 105   |      26|       4.562|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  98   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 112   |     111|      52.933|   0.1%/541|   0.2%/382|   0.2%/354|   0.2%/331 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  87   |      90|       5.682|   0.1%/640|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)|  99   |    2954|      50.261|   3.6%/ 19|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 123   |   28658|     608.448|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  98   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 113   |     617|      14.533|   1.4%/ 50|   1.1%/ 65|   1.0%/ 70|   0.9%/ 76 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 115   |    5437|     525.934|   0.5%/132|   0.5%/142|   0.5%/144|   0.5%/147 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 121   |    1968|     228.715|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  97   |      10|       0.553|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  95   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 125   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)|  99   |      14|       1.890|   0.3%/212|   0.3%/241|   0.3%/259|   0.2%/285 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 101   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 107   |      50|       4.276|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 109   |    5197|      62.504|   0.4%/179|   0.4%/188|   0.4%/191|   0.4%/194 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 126   |  129571|     393.182|   0.6%/116|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 113   |    1230|      29.358|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 106   |     320|      32.313|   0.5%/153|   0.4%/180|   0.4%/189|   0.3%/199 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 115   |   44266|     666.299|   0.3%/243|   0.3%/263|   0.3%/269|   0.3%/275 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  97   |      28|       8.001|   1.1%/ 63|   1.2%/ 59|   1.2%/ 58|   1.2%/ 57 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)|  99   |      26|       0.765|   2.9%/ 24|   4.5%/ 15|   4.9%/ 14|   5.4%/ 13 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)|  99   |      58|       1.801|   5.0%/ 14|   5.6%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  93   |      31|       1.735|   5.3%/ 13|  10.9%/  6|  10.9%/  6|   7.7%/  9 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 103   |       4|       0.264|   0.0%/ --|   5.3%/ 13|   0.0%/ --|   0.0%/ -- |

