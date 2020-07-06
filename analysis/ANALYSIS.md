# State and Country COVID-19 Analysis #
## Updated: at 2020-07-06 for data as of 2020-07-05 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 36.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Florida and California have followed nearly identical trajectories since early April 2020.
 
For confirmed cases, the story is not so different.

![Cases](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20Cases.png)

![Daily Case Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestConfirmed%20CasesPerDay.png)

The next two plots show the latest 21-day trajectory of deaths/day/million vs confirmed cases/day/million for the four largest population states and for all states with non-trival death rates.

![Four State Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/FourDailyCasesVsDeaths.png)

![All States Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/AllDailyCasesVsDeaths.png)

The next plots shows the total US deaths to date from COVID-19 compared to historical seasonal flus and 20th century pandemics.

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.8% of deaths and 54.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 114   |   32173|    1653.831|   0.2%/367|   0.2%/333|   0.2%/325|   0.2%/317 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 118   |   15664|    1763.581|   0.2%/282|   0.2%/329|   0.2%/342|   0.2%/355 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 108   |    8208|    1181.080|   0.3%/227|   0.3%/271|   0.2%/285|   0.2%/300 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 111   |    7078|     558.569|   0.4%/168|   0.3%/237|   0.3%/265|   0.2%/299 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 109   |    6784|     529.942|   0.4%/186|   0.3%/208|   0.3%/214|   0.3%/221 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 124   |    6430|     162.738|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 109   |    6233|     624.080|   0.2%/434|   0.1%/469|   0.1%/479|   0.1%/489 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 109   |    4352|    1220.571|   0.1%/527|   0.1%/840|   0.1%/992|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 120   |    3731|     173.711|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 114   |    3294|     708.550|   0.4%/165|   0.4%/167|   0.4%/167|   0.4%/168 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 128   |  130842|     397.038|   0.6%/125|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 111   |   65295|     308.853|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 117   |   44459|     669.207|   0.3%/260|   0.2%/290|   0.2%/299|   0.2%/308 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   34919|     579.684|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 109   |   31747|     250.813|   2.5%/ 27|   2.1%/ 33|   2.0%/ 35|   1.9%/ 37 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 142   |   29959|     446.638|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 125   |   28640|     608.070|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 117   |   20258|      14.882|   2.6%/ 26|   2.5%/ 27|   2.5%/ 28|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 137   |   11507|     138.008|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 108   |   10740|     334.240|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 41 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 103   |    1020|     208.114|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 103   |      16|      21.215|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 107   |    1858|     255.238|   2.2%/ 31|   2.3%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 104   |     297|      98.329|   1.9%/ 37|   1.4%/ 50|   1.3%/ 55|   1.1%/ 60 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 124   |    6430|     162.738|   1.1%/ 65|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 114   |    1711|     297.046|   0.2%/293|   0.2%/413|   0.2%/457|   0.1%/510 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 109   |    4352|    1220.571|   0.1%/527|   0.1%/840|   0.1%/992|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 102   |     530|     544.724|   0.2%/386|   0.1%/681|   0.1%/817|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 120   |    3731|     173.711|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 116   |    2902|     273.305|   0.6%/121|   0.4%/179|   0.3%/202|   0.3%/231 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  97   |      19|      13.309|   1.0%/ 67|   1.6%/ 44|   1.7%/ 40|   1.9%/ 37 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 102   |      93|      52.121|   0.3%/203|   0.4%/181|   0.4%/177|   0.4%/172 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 111   |    7078|     558.569|   0.4%/168|   0.3%/237|   0.3%/265|   0.2%/299 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 112   |    2704|     401.686|   0.5%/154|   0.4%/179|   0.4%/186|   0.4%/194 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 103   |     727|     230.385|   0.4%/177|   0.3%/230|   0.3%/249|   0.3%/271 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 115   |     285|      97.724|   0.8%/ 90|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 112   |     590|     131.978|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 114   |    3294|     708.550|   0.4%/165|   0.4%/167|   0.4%/167|   0.4%/168 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 101   |     107|      79.449|   0.4%/191|   0.5%/145|   0.5%/136|   0.5%/129 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 109   |    3259|     539.031|   0.4%/166|   0.3%/202|   0.3%/214|   0.3%/226 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 108   |    8208|    1181.080|   0.3%/227|   0.3%/271|   0.2%/285|   0.2%/300 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 109   |    6233|     624.080|   0.2%/434|   0.1%/469|   0.1%/479|   0.1%/489 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 107   |    1517|     268.977|   0.5%/130|   0.4%/163|   0.4%/173|   0.4%/185 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 109   |    1126|     378.222|   1.0%/ 66|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 109   |    1057|     172.187|   0.7%/ 98|   0.6%/113|   0.6%/116|   0.6%/120 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 101   |      23|      21.633|   0.9%/ 74|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 100   |     289|     149.382|   1.1%/ 64|   0.9%/ 81|   0.8%/ 86|   0.7%/ 92 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 112   |     530|     171.932|   0.7%/ 94|   0.8%/ 83|   0.9%/ 81|   0.9%/ 78 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 105   |     385|     283.338|   0.8%/ 89|   0.6%/107|   0.6%/113|   0.6%/121 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 118   |   15664|    1763.581|   0.2%/282|   0.2%/329|   0.2%/342|   0.2%/355 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 103   |     516|     245.957|   0.7%/ 98|   0.6%/113|   0.6%/117|   0.6%/121 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 114   |   32173|    1653.831|   0.2%/367|   0.2%/333|   0.2%/325|   0.2%/317 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 103   |    1451|     138.386|   1.0%/ 72|   0.7%/ 95|   0.7%/104|   0.6%/114 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 101   |      81|     105.822|   0.3%/205|   0.2%/305|   0.2%/346|   0.2%/402 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 108   |    2934|     250.976|   0.6%/120|   0.5%/138|   0.5%/144|   0.5%/149 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 109   |     399|     100.821|   0.6%/119|   0.7%/104|   0.7%/101|   0.7%/ 99 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 113   |     215|      51.033|   0.8%/ 82|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 109   |    6784|     529.942|   0.4%/186|   0.3%/208|   0.3%/214|   0.3%/221 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 107   |     155|      48.601|   0.3%/227|   0.3%/217|   0.3%/216|   0.3%/216 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 100   |     971|     916.275|   0.5%/135|   0.4%/180|   0.4%/196|   0.3%/216 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 112   |     811|     157.510|   1.7%/ 41|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 117   |      99|     111.581|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 107   |     648|      94.856|   1.4%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 111   |    2638|      90.964|   1.3%/ 51|   1.4%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 128   |  130842|     397.038|   0.6%/125|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 106   |     183|      56.983|   1.2%/ 58|   1.2%/ 59|   1.2%/ 59|   1.2%/ 58 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 108   |      56|      89.932|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 114   |    1856|     217.399|   1.0%/ 68|   1.1%/ 60|   1.2%/ 59|   1.2%/ 57 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 128   |    1366|     179.394|   0.5%/136|   0.5%/148|   0.5%/151|   0.4%/155 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  98   |      94|      52.720|   0.3%/219|   0.2%/337|   0.2%/400|   0.1%/495 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 108   |     807|     138.557|   0.6%/125|   0.4%/176|   0.4%/196|   0.3%/221 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  84   |      20|      34.616|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 106   |     869|      26.964|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 117   |      75|      26.189|   4.3%/ 16|   5.1%/ 14|   5.2%/ 13|   5.4%/ 13 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 116   |     959|      22.300|   0.9%/ 76|   0.8%/ 87|   0.8%/ 90|   0.7%/ 94 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  99   |      20|       0.629|   3.2%/ 21|  11.5%/  6|   8.2%/  8|   3.8%/ 18 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 120   |    1514|      33.691|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 102   |     500|     168.936|   2.4%/ 28|   1.9%/ 37|   1.7%/ 40|   1.6%/ 44 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 127   |     105|       4.082|   0.1%/482|   0.2%/420|   0.2%/409|   0.2%/400 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 116   |     709|      79.671|   0.2%/442|   0.1%/607|   0.1%/676|   0.1%/765 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 115   |     253|      25.156|   3.5%/ 20|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 112   |     104|      67.629|   3.5%/ 20|   2.6%/ 27|   2.3%/ 29|   2.1%/ 32 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 110   |    2076|      12.324|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  97   |     423|      44.964|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 117   |    9775|     848.200|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  91   |      23|       1.961|   4.6%/ 15|   3.7%/ 19|   3.5%/ 20|   3.2%/ 21 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  99   |    1418|     123.671|   4.5%/ 15|   4.9%/ 14|   5.1%/ 14|   5.2%/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 107   |     193|      58.324|   0.9%/ 81|   0.9%/ 73|   1.0%/ 71|   1.0%/ 70 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  97   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 111   |   65295|     308.853|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 117   |     246|      35.380|   1.5%/ 45|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 110   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  84   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 103   |     319|      12.028|   0.4%/197|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 119   |    8774|     230.892|   0.3%/275|   0.2%/367|   0.2%/398|   0.2%/435 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  44   |      48|       8.792|   3.4%/ 20|   0.9%/ 79|   0.4%/172|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  69   |      74|       4.555|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 106   |    6505|     340.433|   2.8%/ 24|   2.2%/ 32|   2.0%/ 34|   1.8%/ 37 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 117   |    4642|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 106   |    4187|      84.762|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 109   |      18|       3.634|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 109   |     111|      27.129|   0.4%/163|   0.7%/100|   0.8%/ 91|   0.8%/ 82 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 110   |      86|       7.698|   0.1%/770|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 114   |     607|     104.276|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 111   |     797|      76.908|   1.3%/ 52|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 114   |    4775|     273.341|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68|   1.0%/ 68 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 120   |    3497|      34.876|   3.2%/ 22|   2.7%/ 26|   2.6%/ 27|   2.4%/ 28 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  97   |     226|      34.865|   5.8%/ 12|   5.6%/ 12|   5.6%/ 12|   5.5%/ 12 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  75   |      50|      36.659|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  92   |     112|       1.133|   2.0%/ 34|   1.0%/ 70|   0.7%/ 99|   0.4%/172 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 107   |     329|      59.525|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 142   |   29959|     446.638|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 108   |      46|      21.192|   1.8%/ 39|   1.0%/ 70|   0.8%/ 87|   0.6%/112 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 105   |       2|       0.953|   1.9%/ 37|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  93   |      15|       4.080|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 119   |    9037|     108.686|   0.1%/677|   0.1%/826|   0.1%/875|   0.1%/929 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 107   |     131|       4.319|   2.8%/ 24|   1.4%/ 49|   1.0%/ 66|   0.7%/103 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 117   |     193|      18.010|   0.1%/591|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 112   |     967|      58.227|   4.3%/ 16|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  82   |      35|       2.833|   1.7%/ 42|   1.5%/ 46|   1.5%/ 48|   1.4%/ 50 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  71   |      26|      16.178|   2.8%/ 24|   1.7%/ 40|   1.4%/ 49|   1.1%/ 63 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  92   |     115|       9.939|   1.9%/ 37|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 102   |     638|      69.656|   4.1%/ 17|   4.6%/ 15|   4.8%/ 14|   4.9%/ 14 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 113   |     591|      60.467|   0.2%/306|   0.2%/338|   0.2%/348|   0.2%/358 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 117   |   20258|      14.882|   2.6%/ 26|   2.5%/ 27|   2.5%/ 28|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 117   |    3149|      11.799|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 137   |   11507|     138.008|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 124   |    2725|      69.647|   6.2%/ 11|   5.3%/ 13|   5.0%/ 14|   4.8%/ 14 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 117   |    1745|     354.474|   0.1%/725|   0.1%/823|   0.1%/857|   0.1%/896 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 107   |     329|      35.850|   0.5%/126|   0.7%/104|   0.7%/100|   0.7%/ 96 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   34919|     579.684|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 109   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 144   |     987|       7.833|   0.2%/365|   0.1%/488|   0.1%/538|   0.1%/602 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 101   |       9|       0.844|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 103   |     215|      11.480|   2.9%/ 24|   1.3%/ 54|   0.9%/ 79|   0.4%/154 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 102   |     162|       3.408|   2.0%/ 35|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 102   |      61|      33.742|   0.2%/438|   0.2%/284|   0.3%/254|   0.3%/228 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  93   |     369|      83.591|   0.9%/ 76|   0.7%/ 97|   0.7%/103|   0.6%/111 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  94   |      84|      12.828|   6.3%/ 11|   7.2%/  9|   7.5%/  9|   7.7%/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  94   |      30|      15.748|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 118   |      35|       5.161|   0.7%/ 97|   0.9%/ 79|   0.9%/ 76|   1.0%/ 72 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  93   |      37|       8.343|   0.7%/ 94|   0.8%/ 83|   0.9%/ 80|   0.9%/ 78 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  95   |      31|       4.569|   8.5%/  8|   4.0%/ 17|   2.6%/ 27|   7.2%/ 10 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 107   |      79|      28.315|   0.2%/292|   0.2%/304|   0.2%/308|   0.2%/311 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  50   |      31|       1.186|   5.3%/ 13|   8.7%/  8|   9.4%/  7|  10.1%/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 111   |     121|       3.695|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  99   |     119|       5.873|   0.6%/119|   0.5%/139|   0.5%/144|   0.5%/150 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  98   |     136|      33.318|   1.4%/ 51|   0.2%/295|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 109   |   31747|     250.813|   2.5%/ 27|   2.1%/ 33|   2.0%/ 35|   1.9%/ 37 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 110   |     591|     220.528|   1.6%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 118   |     232|       6.461|   0.6%/112|   0.8%/ 88|   0.8%/ 83|   0.9%/ 79 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  42   |       7|       0.245|   3.6%/ 19|   4.8%/ 14|   5.4%/ 13|   6.1%/ 11 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  51   |      34|       1.136|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22|   3.3%/ 21 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 122   |    6143|     351.882|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  99   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 101   |      86|      13.318|   1.6%/ 42|   1.4%/ 48|   1.4%/ 51|   1.3%/ 53 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 103   |      68|       3.038|   0.1%/498|   0.2%/405|   0.2%/379|   0.2%/354 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 105   |     647|       3.137|   1.8%/ 39|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 106   |     345|     166.228|   2.7%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 114   |     252|      46.994|   0.1%/473|   0.1%/656|   0.1%/732|   0.1%/831 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  97   |     209|      44.702|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 109   |    4882|      22.259|   2.1%/ 33|   1.4%/ 48|   1.3%/ 54|   1.1%/ 62 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 117   |     725|     171.752|   2.8%/ 25|   3.1%/ 23|   3.1%/ 22|   3.2%/ 21 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 107   |      20|       2.776|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 108   |   10740|     334.240|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 41 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 155   |    1320|      12.164|   0.8%/ 86|   0.7%/ 95|   0.7%/ 98|   0.7%/101 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 116   |    1533|      39.947|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 111   |    1603|     156.022|   0.4%/192|   0.4%/157|   0.5%/150|   0.5%/144 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 100   |     127|      46.261|   2.1%/ 33|   1.6%/ 42|   1.5%/ 45|   1.5%/ 48 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 106   |    1740|      89.647|   1.1%/ 65|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 109   |   10183|      69.395|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  37   |       3|       0.255|   1.6%/ 44|   7.4%/  9|   4.8%/ 14|   1.7%/ 41 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 104   |    1922|      56.164|   3.1%/ 22|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  96   |     133|       8.202|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 108   |     286|      41.016|   1.0%/ 73|   1.3%/ 54|   1.4%/ 51|   1.4%/ 48 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  74   |      63|       7.923|   1.0%/ 68|   0.8%/ 85|   0.8%/ 91|   0.7%/ 99 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 107   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 100   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 114   |     111|      53.100|   0.1%/671|   0.1%/539|   0.1%/517|   0.1%/499 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  89   |      91|       5.733|   0.2%/370|   0.2%/307|   0.2%/289|   0.3%/269 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 101   |    3164|      53.827|   3.5%/ 19|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 125   |   28640|     608.070|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 100   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 115   |     624|      14.693|   1.1%/ 61|   0.8%/ 90|   0.7%/102|   0.6%/117 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 117   |    5472|     529.323|   0.5%/152|   0.4%/179|   0.4%/188|   0.4%/198 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 123   |    1968|     228.721|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  99   |      10|       0.586|   4.0%/ 17|   3.6%/ 19|   3.6%/ 19|  13.0%/  5 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  97   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 127   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 101   |      15|       1.946|   0.7%/ 95|   0.9%/ 75|   1.0%/ 72|   1.0%/ 69 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 103   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 109   |      50|       4.273|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 111   |    5233|      62.936|   0.4%/182|   0.4%/193|   0.4%/196|   0.3%/199 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 128   |  130842|     397.038|   0.6%/125|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 115   |    1267|      30.255|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 108   |     323|      32.615|   0.5%/149|   0.4%/162|   0.4%/166|   0.4%/169 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 117   |   44459|     669.207|   0.3%/260|   0.2%/290|   0.2%/299|   0.2%/308 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  99   |      28|       8.097|   0.9%/ 76|   0.8%/ 87|   0.8%/ 91|   0.7%/ 96 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 101   |      30|       0.867|   3.9%/ 18|   5.9%/ 12|   6.4%/ 11|   6.9%/ 10 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 101   |      64|       2.001|   5.0%/ 14|   5.3%/ 13|   5.4%/ 13|   5.5%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  95   |      33|       1.867|   1.6%/ 44|   7.7%/  9|   0.0%/ --|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 105   |       8|       0.512|   5.3%/ 13|   0.0%/ --|   4.6%/ 15|   4.6%/ 15 |

