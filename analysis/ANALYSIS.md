# State and Country COVID-19 Analysis #
## Updated: at 2020-07-05 for data as of 2020-07-04 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.5% of deaths and 36.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 113   |   32075|    1648.785|   0.2%/283|   0.3%/237|   0.3%/226|   0.3%/216 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 117   |   15571|    1753.112|   0.2%/277|   0.2%/334|   0.2%/350|   0.2%/367 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 107   |    8188|    1178.240|   0.3%/217|   0.3%/256|   0.3%/268|   0.2%/281 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 110   |    7065|     557.560|   0.4%/160|   0.3%/228|   0.3%/255|   0.2%/289 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 108   |    6767|     528.605|   0.4%/177|   0.4%/193|   0.4%/197|   0.3%/201 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 123   |    6372|     161.262|   1.1%/ 62|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 108   |    6226|     623.374|   0.2%/401|   0.2%/408|   0.2%/409|   0.2%/409 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 108   |    4350|    1220.143|   0.1%/488|   0.1%/755|   0.1%/878|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 119   |    3687|     171.675|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 113   |    3282|     705.937|   0.4%/162|   0.4%/161|   0.4%/161|   0.4%/160 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 127   |  130244|     395.224|   0.6%/119|   0.6%/121|   0.6%/122|   0.6%/122 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 110   |   64287|     304.086|   1.8%/ 38|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 116   |   44374|     667.923|   0.3%/249|   0.3%/272|   0.2%/278|   0.2%/285 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 135   |   34905|     579.444|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 108   |   31225|     246.683|   2.7%/ 26|   2.3%/ 30|   2.2%/ 32|   2.1%/ 33 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 141   |   29950|     446.512|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 124   |   28657|     608.430|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 116   |   19872|      14.599|   2.7%/ 26|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   11345|     136.063|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 107   |   10550|     328.342|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 102   |    1010|     205.915|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 102   |      15|      20.556|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 106   |    1823|     250.490|   2.3%/ 30|   2.5%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 103   |     293|      97.154|   2.0%/ 34|   1.6%/ 44|   1.5%/ 47|   1.3%/ 51 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 123   |    6372|     161.262|   1.1%/ 62|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 113   |    1709|     296.762|   0.3%/260|   0.2%/337|   0.2%/362|   0.2%/389 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 108   |    4350|    1220.143|   0.1%/488|   0.1%/755|   0.1%/878|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 101   |     531|     545.368|   0.2%/355|   0.1%/670|   0.1%/841|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 119   |    3687|     171.675|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 115   |    2892|     272.372|   0.6%/110|   0.5%/153|   0.4%/169|   0.4%/189 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  96   |      18|      13.020|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 101   |      93|      51.953|   0.3%/206|   0.4%/186|   0.4%/181|   0.4%/176 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 110   |    7065|     557.560|   0.4%/160|   0.3%/228|   0.3%/255|   0.2%/289 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 111   |    2694|     400.222|   0.5%/149|   0.4%/175|   0.4%/183|   0.4%/191 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 102   |     726|     229.959|   0.4%/161|   0.4%/196|   0.3%/206|   0.3%/218 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 114   |     283|      96.994|   0.8%/ 87|   0.9%/ 79|   0.9%/ 78|   0.9%/ 76 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 111   |     586|     131.168|   0.8%/ 83|   0.9%/ 78|   0.9%/ 77|   0.9%/ 76 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 113   |    3282|     705.937|   0.4%/162|   0.4%/161|   0.4%/161|   0.4%/160 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 100   |     106|      78.799|   0.3%/251|   0.3%/223|   0.3%/217|   0.3%/211 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 108   |    3250|     537.495|   0.4%/160|   0.4%/195|   0.3%/206|   0.3%/218 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 107   |    8188|    1178.240|   0.3%/217|   0.3%/256|   0.3%/268|   0.2%/281 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 108   |    6226|     623.374|   0.2%/401|   0.2%/408|   0.2%/409|   0.2%/409 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 106   |    1512|     268.087|   0.6%/122|   0.5%/149|   0.4%/157|   0.4%/165 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 108   |    1117|     375.161|   1.1%/ 63|   1.1%/ 65|   1.1%/ 65|   1.1%/ 66 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 108   |    1052|     171.390|   0.8%/ 90|   0.7%/ 99|   0.7%/101|   0.7%/103 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 100   |      23|      21.499|   0.9%/ 78|   0.7%/ 95|   0.7%/101|   0.6%/107 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)|  99   |     287|     148.404|   1.2%/ 59|   1.0%/ 69|   1.0%/ 72|   0.9%/ 76 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 111   |     525|     170.460|   0.7%/ 93|   0.9%/ 81|   0.9%/ 79|   0.9%/ 76 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 104   |     383|     281.780|   0.8%/ 85|   0.7%/100|   0.7%/104|   0.6%/110 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 117   |   15571|    1753.112|   0.2%/277|   0.2%/334|   0.2%/350|   0.2%/367 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 102   |     513|     244.802|   0.7%/ 96|   0.6%/113|   0.6%/117|   0.6%/122 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 113   |   32075|    1648.785|   0.2%/283|   0.3%/237|   0.3%/226|   0.3%/216 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 102   |    1445|     137.797|   1.0%/ 66|   0.8%/ 82|   0.8%/ 87|   0.7%/ 94 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 100   |      81|     105.707|   0.4%/182|   0.3%/231|   0.3%/248|   0.3%/267 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 107   |    2921|     249.929|   0.6%/115|   0.5%/131|   0.5%/136|   0.5%/141 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 108   |     397|     100.251|   0.6%/115|   0.7%/ 96|   0.8%/ 92|   0.8%/ 89 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 112   |     214|      50.624|   0.8%/ 82|   0.7%/ 93|   0.7%/ 96|   0.7%/ 99 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 108   |    6767|     528.605|   0.4%/177|   0.4%/193|   0.4%/197|   0.3%/201 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 106   |     155|      48.457|   0.3%/238|   0.3%/234|   0.3%/235|   0.3%/236 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)|  99   |     968|     913.728|   0.6%/121|   0.5%/148|   0.4%/156|   0.4%/165 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 111   |     796|     154.612|   1.7%/ 41|   1.9%/ 36|   2.0%/ 34|   2.1%/ 33 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 116   |      98|     110.482|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 106   |     640|      93.638|   1.5%/ 47|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 110   |    2605|      89.848|   1.4%/ 51|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 127   |  130244|     395.224|   0.6%/119|   0.6%/121|   0.6%/122|   0.6%/122 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 105   |     181|      56.316|   1.2%/ 59|   1.1%/ 64|   1.1%/ 64|   1.1%/ 65 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 107   |      56|      89.949|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 113   |    1837|     215.178|   1.0%/ 67|   1.2%/ 58|   1.2%/ 56|   1.3%/ 54 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 127   |    1360|     178.612|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/149 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  97   |      94|      52.639|   0.3%/217|   0.2%/323|   0.2%/382|   0.1%/475 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 107   |     804|     138.142|   0.6%/113|   0.5%/146|   0.4%/157|   0.4%/171 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  83   |      20|      34.626|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 105   |     847|      26.286|   2.9%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 116   |      71|      24.887|   4.3%/ 16|   5.1%/ 13|   5.3%/ 13|   5.5%/ 12 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 115   |     951|      22.124|   0.9%/ 75|   0.8%/ 86|   0.8%/ 90|   0.7%/ 93 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)|  98   |      19|       0.609|   3.2%/ 21|  15.6%/  4|  11.5%/  6|   8.2%/  8 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 119   |    1473|      32.787|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 101   |     492|     166.525|   2.6%/ 27|   2.0%/ 35|   1.9%/ 37|   1.7%/ 41 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 126   |     104|       4.067|   0.1%/728|   0.1%/770|   0.1%/797|   0.1%/833 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 115   |     709|      79.598|   0.2%/401|   0.1%/503|   0.1%/541|   0.1%/587 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 114   |     245|      24.374|   3.5%/ 19|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 111   |     102|      66.115|   3.8%/ 18|   3.0%/ 23|   2.8%/ 25|   2.6%/ 27 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 109   |    2033|      12.069|   2.5%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  96   |     417|      44.343|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 116   |    9771|     847.820|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  90   |      23|       1.927|   5.1%/ 13|   4.6%/ 15|   4.5%/ 15|   4.4%/ 16 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)|  98   |    1350|     117.687|   4.5%/ 15|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 106   |     191|      57.862|   0.9%/ 77|   1.1%/ 66|   1.1%/ 63|   1.1%/ 61 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  96   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 110   |   64287|     304.086|   1.8%/ 38|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 116   |     242|      34.866|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 109   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  83   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 102   |     321|      12.102|   0.4%/156|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 118   |    8762|     230.576|   0.3%/258|   0.2%/338|   0.2%/365|   0.2%/394 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  43   |      48|       8.769|   4.6%/ 15|   1.2%/ 58|   0.5%/143|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  68   |      74|       4.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 105   |    6387|     334.295|   3.0%/ 23|   2.3%/ 31|   2.1%/ 33|   1.9%/ 36 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 116   |    4642|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 105   |    4008|      81.146|   4.4%/ 16|   4.4%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 108   |      18|       3.466|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 108   |     109|      26.847|   0.3%/205|   0.6%/122|   0.6%/110|   0.7%/100 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 109   |      86|       7.696|   0.1%/680|   0.1%/920|   0.1%/ ***|   0.1%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 113   |     607|     104.256|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 110   |     787|      76.002|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 113   |    4730|     270.765|   1.0%/ 70|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 119   |    3410|      34.010|   3.3%/ 21|   2.9%/ 24|   2.7%/ 25|   2.6%/ 26 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  96   |     215|      33.203|   6.0%/ 11|   6.0%/ 11|   6.0%/ 11|   6.0%/ 11 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  74   |      46|      33.539|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  91   |     111|       1.127|   2.4%/ 29|   1.5%/ 48|   1.2%/ 58|   0.9%/ 74 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 106   |     329|      59.493|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 141   |   29950|     446.512|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 107   |      46|      21.026|   1.8%/ 38|   1.0%/ 70|   0.8%/ 88|   0.6%/120 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 104   |       2|       0.975|   2.4%/ 29|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  92   |      15|       4.063|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 118   |    9031|     108.613|   0.1%/641|   0.1%/766|   0.1%/805|   0.1%/848 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 106   |     130|       4.295|   3.1%/ 22|   1.6%/ 42|   1.3%/ 55|   0.9%/ 80 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 116   |     193|      18.015|   0.1%/498|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 111   |     930|      56.035|   4.4%/ 16|   4.1%/ 17|   4.1%/ 17|   4.0%/ 17 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  81   |      34|       2.799|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  70   |      26|      16.108|   3.1%/ 22|   2.0%/ 35|   1.7%/ 42|   1.3%/ 52 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  91   |     113|       9.801|   2.0%/ 35|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 101   |     612|      66.778|   4.3%/ 16|   5.0%/ 14|   5.2%/ 13|   5.4%/ 13 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 112   |     590|      60.369|   0.2%/289|   0.2%/312|   0.2%/318|   0.2%/324 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 116   |   19872|      14.599|   2.7%/ 26|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 116   |    3090|      11.578|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   11345|     136.063|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 123   |    2589|      66.179|   6.5%/ 11|   5.6%/ 12|   5.4%/ 13|   5.1%/ 13 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 116   |    1743|     354.249|   0.1%/694|   0.1%/771|   0.1%/796|   0.1%/824 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 106   |     327|      35.593|   0.5%/133|   0.6%/108|   0.7%/103|   0.7%/ 99 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 135   |   34905|     579.444|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 108   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 143   |     986|       7.826|   0.2%/324|   0.2%/391|   0.2%/416|   0.2%/446 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 100   |       9|       0.844|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 102   |     214|      11.451|   3.5%/ 19|   2.0%/ 34|   1.6%/ 42|   1.2%/ 56 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 101   |     160|       3.357|   2.0%/ 34|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 101   |      57|      31.682|   0.1%/522|   0.2%/390|   0.2%/357|   0.2%/324 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  92   |     367|      83.031|   0.9%/ 73|   0.7%/ 96|   0.7%/103|   0.6%/112 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  93   |      77|      11.836|   6.3%/ 11|   7.5%/  9|   7.8%/  9|   8.2%/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  93   |      30|      15.768|   0.1%/979|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 117   |      35|       5.103|   0.7%/104|   0.8%/ 86|   0.8%/ 82|   0.9%/ 78 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  92   |      37|       8.284|   0.8%/ 86|   1.0%/ 68|   1.1%/ 65|   1.1%/ 61 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  94   |      30|       4.306|   5.3%/ 13|   4.2%/ 16|   4.0%/ 17|   2.6%/ 27 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 106   |      79|      28.264|   0.2%/316|   0.2%/361|   0.2%/376|   0.2%/393 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  49   |      28|       1.069|   4.5%/ 15|   8.0%/  9|   8.8%/  8|   9.6%/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 110   |     121|       3.696|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)|  98   |     118|       5.841|   0.6%/117|   0.5%/140|   0.5%/146|   0.5%/153 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  97   |     136|      33.243|   1.7%/ 40|   0.4%/191|   0.0%/ ***|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 108   |   31225|     246.683|   2.7%/ 26|   2.3%/ 30|   2.2%/ 32|   2.1%/ 33 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 109   |     584|     217.752|   1.7%/ 41|   1.5%/ 47|   1.4%/ 48|   1.4%/ 50 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 117   |     230|       6.401|   0.6%/120|   0.7%/ 94|   0.8%/ 89|   0.8%/ 84 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  41   |       7|       0.221|   2.5%/ 28|   3.3%/ 21|   3.0%/ 23|   2.5%/ 27 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  50   |      33|       1.103|   3.1%/ 23|   2.9%/ 24|   3.0%/ 23|   3.2%/ 22 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 121   |    6140|     351.728|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)|  98   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 100   |      85|      13.217|   0.0%/ --|   3.9%/ 18|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 102   |      68|       3.032|   0.1%/467|   0.2%/351|   0.2%/323|   0.2%/298 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 104   |     637|       3.092|   1.8%/ 38|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 105   |     338|     162.542|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 113   |     252|      46.966|   0.2%/419|   0.1%/511|   0.1%/545|   0.1%/584 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  96   |     200|      42.949|   3.4%/ 21|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 108   |    4825|      22.000|   2.2%/ 31|   1.5%/ 46|   1.3%/ 51|   1.2%/ 59 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 116   |     701|     166.266|   2.6%/ 26|   2.9%/ 24|   2.9%/ 24|   3.0%/ 23 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 106   |      19|       2.671|   3.4%/ 20|   4.7%/ 15|   5.0%/ 14|   5.4%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 107   |   10550|     328.342|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 154   |    1312|      12.086|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 96 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 115   |    1523|      39.677|   0.9%/ 76|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 110   |    1595|     155.232|   0.3%/208|   0.4%/171|   0.4%/164|   0.4%/157 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)|  99   |     124|      45.277|   2.1%/ 33|   1.5%/ 47|   1.3%/ 52|   1.2%/ 58 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 105   |    1719|      88.586|   1.0%/ 66|   1.1%/ 63|   1.1%/ 62|   1.1%/ 61 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 108   |   10033|      68.369|   1.7%/ 40|   1.6%/ 44|   1.6%/ 45|   1.5%/ 45 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  36   |       3|       0.263|   1.4%/ 50|   9.3%/  7|   8.7%/  8|   7.5%/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 103   |    1866|      54.542|   3.1%/ 22|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  95   |     129|       7.932|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 107   |     283|      40.572|   0.9%/ 80|   1.2%/ 60|   1.2%/ 56|   1.3%/ 53 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  73   |      62|       7.889|   1.1%/ 66|   0.8%/ 89|   0.7%/ 99|   0.6%/113 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 106   |      26|       4.560|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)|  99   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 113   |     111|      53.025|   0.1%/602|   0.2%/451|   0.2%/425|   0.2%/402 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  88   |      91|       5.710|   0.1%/482|   0.1%/651|   0.1%/702|   0.1%/748 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 100   |    3051|      51.908|   3.5%/ 20|   3.4%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 124   |   28657|     608.430|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)|  99   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 114   |     621|      14.624|   1.3%/ 55|   0.9%/ 76|   0.8%/ 83|   0.7%/ 93 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 116   |    5458|     527.895|   0.5%/138|   0.5%/152|   0.4%/156|   0.4%/160 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 122   |    1968|     228.723|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)|  98   |      10|       0.570|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  96   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 126   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 100   |      14|       1.919|   0.5%/130|   0.6%/113|   0.6%/112|   0.6%/110 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 102   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 108   |      50|       4.275|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 110   |    5216|      62.721|   0.4%/181|   0.4%/192|   0.4%/195|   0.3%/199 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 127   |  130244|     395.224|   0.6%/119|   0.6%/121|   0.6%/122|   0.6%/122 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 114   |    1248|      29.796|   1.6%/ 44|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 107   |     321|      32.453|   0.5%/153|   0.4%/174|   0.4%/180|   0.4%/187 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 116   |   44374|     667.923|   0.3%/249|   0.3%/272|   0.2%/278|   0.2%/285 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)|  98   |      28|       8.057|   1.0%/ 68|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 100   |      28|       0.811|   3.3%/ 21|   5.0%/ 14|   5.5%/ 12|   6.0%/ 11 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 100   |      61|       1.898|   5.0%/ 14|   5.4%/ 13|   5.6%/ 12|   5.7%/ 12 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  94   |      33|       1.818|   6.9%/ 10|  10.9%/  6|   7.7%/  9|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 104   |       7|       0.494|   3.3%/ 21|   2.5%/ 27|   2.3%/ 30|   2.1%/ 33 |

