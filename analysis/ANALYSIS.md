# State and Country COVID-19 Analysis #
## Updated: at 2020-07-11 for data as of 2020-07-10 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 37.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.1% of deaths and 53.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 119   |   32476|    1669.393|   0.1%/694|   0.1%/805|   0.1%/838|   0.1%/875 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 123   |   15872|    1786.987|   0.3%/258|   0.3%/250|   0.3%/247|   0.3%/244 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 113   |    8297|    1193.887|   0.3%/257|   0.2%/289|   0.2%/297|   0.2%/305 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 116   |    7298|     575.948|   0.6%/120|   0.6%/109|   0.7%/106|   0.7%/103 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 129   |    6838|     173.063|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 114   |    6874|     536.973|   0.3%/210|   0.3%/228|   0.3%/233|   0.3%/238 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 114   |    6280|     628.848|   0.2%/417|   0.2%/414|   0.2%/414|   0.2%/412 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 114   |    4358|    1222.244|   0.1%/825|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 125   |    4005|     186.470|   1.4%/ 50|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 119   |    3365|     723.870|   0.4%/157|   0.5%/151|   0.5%/150|   0.5%/148 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 133   |  134105|     406.941|   0.5%/127|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 116   |   70524|     333.588|   1.7%/ 41|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 122   |   44854|     675.157|   0.2%/310|   0.2%/358|   0.2%/373|   0.2%/389 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 141   |   34969|     580.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 114   |   34555|     272.996|   2.2%/ 32|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 147   |   30016|     447.494|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 130   |   28522|     605.568|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 122   |   22329|      16.404|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 142   |   12377|     148.440|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 113   |   11628|     361.877|   1.8%/ 38|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 108   |    1086|     221.394|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 108   |      17|      23.778|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 112   |    2064|     283.530|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 109   |     316|     104.720|   1.6%/ 42|   1.4%/ 49|   1.4%/ 51|   1.3%/ 53 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 129   |    6838|     173.063|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 119   |    1716|     298.045|   0.2%/394|   0.1%/512|   0.1%/552|   0.1%/598 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 114   |    4358|    1222.244|   0.1%/825|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 107   |     523|     537.163|   0.2%/445|   0.2%/445|   0.2%/439|   0.2%/432 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 125   |    4005|     186.470|   1.4%/ 50|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 121   |    2959|     278.666|   0.5%/130|   0.5%/150|   0.4%/155|   0.4%/160 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 102   |      19|      13.629|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 107   |      97|      54.300|   0.8%/ 89|   1.1%/ 63|   1.2%/ 58|   1.3%/ 54 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 116   |    7298|     575.948|   0.6%/120|   0.6%/109|   0.7%/106|   0.7%/103 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 117   |    2752|     408.802|   0.4%/169|   0.4%/182|   0.4%/185|   0.4%/188 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 108   |     741|     234.937|   0.4%/159|   0.4%/156|   0.4%/155|   0.5%/153 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 120   |     295|     101.160|   0.7%/ 97|   0.7%/100|   0.7%/101|   0.7%/102 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 117   |     616|     137.944|   0.9%/ 80|   0.9%/ 76|   0.9%/ 75|   0.9%/ 74 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 119   |    3365|     723.870|   0.4%/157|   0.5%/151|   0.5%/150|   0.5%/148 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 106   |     111|      82.444|   0.5%/131|   0.6%/107|   0.7%/102|   0.7%/ 98 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 114   |    3306|     546.866|   0.4%/190|   0.3%/218|   0.3%/226|   0.3%/234 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 113   |    8297|    1193.887|   0.3%/257|   0.2%/289|   0.2%/297|   0.2%/305 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 114   |    6280|     628.848|   0.2%/417|   0.2%/414|   0.2%/414|   0.2%/412 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 112   |    1540|     273.096|   0.4%/168|   0.3%/208|   0.3%/222|   0.3%/236 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 114   |    1200|     403.344|   1.3%/ 53|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 114   |    1084|     176.586|   0.6%/116|   0.6%/125|   0.5%/128|   0.5%/130 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 106   |      24|      22.373|   0.7%/ 92|   0.7%/100|   0.7%/102|   0.7%/104 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 105   |     291|     150.321|   0.6%/124|   0.2%/325|   0.1%/565|   0.0%/ *** |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 117   |     562|     182.407|   1.1%/ 66|   1.3%/ 53|   1.4%/ 51|   1.4%/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 110   |     393|     289.078|   0.6%/115|   0.4%/159|   0.4%/176|   0.4%/197 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 123   |   15872|    1786.987|   0.3%/258|   0.3%/250|   0.3%/247|   0.3%/244 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 108   |     534|     254.501|   0.7%/ 94|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 119   |   32476|    1669.393|   0.1%/694|   0.1%/805|   0.1%/838|   0.1%/875 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 108   |    1494|     142.430|   0.8%/ 84|   0.7%/101|   0.7%/105|   0.6%/110 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 106   |      84|     110.340|   0.7%/101|   0.9%/ 77|   1.0%/ 72|   1.0%/ 68 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 113   |    3019|     258.309|   0.6%/113|   0.6%/111|   0.6%/110|   0.6%/110 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 114   |     412|     104.174|   0.6%/108|   0.7%/ 98|   0.7%/ 96|   0.7%/ 94 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 118   |     227|      53.926|   1.1%/ 62|   1.2%/ 55|   1.3%/ 54|   1.3%/ 52 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 114   |    6874|     536.973|   0.3%/210|   0.3%/228|   0.3%/233|   0.3%/238 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 112   |     159|      49.672|   0.4%/166|   0.5%/144|   0.5%/140|   0.5%/135 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 105   |     982|     926.934|   0.4%/179|   0.3%/245|   0.3%/270|   0.2%/303 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 117   |     903|     175.472|   2.0%/ 34|   2.3%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 122   |     104|     117.126|   1.2%/ 60|   1.1%/ 63|   1.1%/ 65|   1.1%/ 66 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 112   |     705|     103.135|   1.7%/ 41|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 116   |    2871|      99.030|   1.9%/ 36|   2.3%/ 30|   2.4%/ 29|   2.5%/ 28 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 133   |  134105|     406.941|   0.5%/127|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 111   |     202|      63.041|   1.7%/ 40|   2.1%/ 33|   2.2%/ 32|   2.3%/ 31 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 113   |      56|      89.771|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 119   |    1949|     228.371|   1.0%/ 68|   1.1%/ 64|   1.1%/ 64|   1.1%/ 63 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 133   |    1408|     184.935|   0.6%/111|   0.7%/105|   0.7%/103|   0.7%/102 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 103   |      95|      53.244|   0.3%/268|   0.2%/411|   0.1%/464|   0.1%/530 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 113   |     817|     140.276|   0.4%/164|   0.3%/222|   0.3%/243|   0.3%/267 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  89   |      21|      35.960|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 111   |     987|      30.637|   2.7%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 122   |      90|      31.645|   3.5%/ 20|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 121   |     996|      23.170|   0.9%/ 80|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 104   |      24|       0.764|   5.5%/ 12|   5.6%/ 12|   5.5%/ 12|   5.5%/ 13 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 125   |    1769|      39.363|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 107   |     544|     184.090|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 132   |     106|       4.139|   0.2%/324|   0.2%/284|   0.3%/275|   0.3%/267 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 121   |     710|      79.730|   0.1%/848|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 120   |     295|      29.330|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 117   |     110|      71.314|   2.2%/ 31|   1.3%/ 51|   1.1%/ 62|   0.9%/ 78 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 115   |    2305|      13.683|   2.3%/ 30|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 102   |     455|      48.343|   1.5%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 122   |    9790|     849.494|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  96   |      24|       2.061|   0.0%/ --|   0.0%/ --|   3.1%/ 22|   3.1%/ 22 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 104   |    1738|     151.533|   4.2%/ 16|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 112   |     211|      63.964|   1.5%/ 47|   1.8%/ 38|   1.9%/ 37|   2.0%/ 35 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 102   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 116   |   70524|     333.588|   1.7%/ 41|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 122   |     266|      38.215|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 115   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  89   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 108   |     347|      13.064|   1.1%/ 65|   1.4%/ 48|   1.6%/ 44|   1.7%/ 41 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 124   |    8837|     232.552|   0.2%/354|   0.2%/453|   0.1%/486|   0.1%/523 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  49   |      53|       9.717|   1.2%/ 59|   1.4%/ 49|   1.4%/ 50|   1.3%/ 53 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  74   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 111   |    6983|     365.451|   2.1%/ 33|   1.5%/ 45|   1.4%/ 50|   1.3%/ 55 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 122   |    4641|       3.310|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 111   |    5064|     102.527|   4.1%/ 17|   3.9%/ 18|   3.8%/ 18|   3.7%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 114   |      25|       5.024|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 114   |     115|      28.223|   0.5%/138|   0.7%/ 99|   0.7%/ 93|   0.8%/ 87 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 115   |      86|       7.695|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 119   |     609|     104.636|   0.1%/972|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 116   |     853|      82.375|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 119   |    4978|     284.972|   0.8%/ 82|   0.8%/ 88|   0.8%/ 90|   0.8%/ 92 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 125   |    3853|      38.425|   2.5%/ 27|   2.0%/ 34|   1.9%/ 36|   1.8%/ 39 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 102   |     267|      41.163|   4.5%/ 15|   3.4%/ 20|   3.1%/ 22|   2.8%/ 25 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  80   |      57|      41.925|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  97   |     121|       1.222|   2.6%/ 27|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 112   |     329|      59.598|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 147   |   30016|     447.494|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 113   |      48|      21.873|   1.2%/ 58|   0.7%/ 98|   0.6%/116|   0.5%/142 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 110   |       3|       1.222|   3.9%/ 18|   4.2%/ 16|   4.4%/ 15|   4.7%/ 15 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  98   |      15|       4.089|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 124   |    9068|     109.058|   0.1%/770|   0.1%/889|   0.1%/923|   0.1%/959 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 112   |     139|       4.577|   2.0%/ 34|   1.1%/ 61|   0.9%/ 74|   0.7%/ 95 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 122   |     193|      18.030|   0.1%/804|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 117   |    1153|      69.450|   4.0%/ 17|   3.7%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  87   |      36|       2.966|   1.4%/ 50|   1.1%/ 61|   1.1%/ 64|   1.0%/ 68 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  76   |      26|      16.156|   1.4%/ 49|   0.3%/261|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  97   |     127|      10.968|   2.1%/ 33|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 107   |     755|      82.469|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.1%/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 118   |     594|      60.780|   0.2%/434|   0.1%/590|   0.1%/654|   0.1%/736 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 122   |   22329|      16.404|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 122   |    3472|      13.007|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 142   |   12377|     148.440|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 129   |    3281|      83.865|   4.9%/ 14|   3.9%/ 18|   3.7%/ 19|   3.4%/ 20 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 122   |    1747|     354.957|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 112   |     346|      37.691|   0.8%/ 84|   1.0%/ 68|   1.1%/ 65|   1.1%/ 63 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 141   |   34969|     580.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 114   |      10|       3.667|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 149   |     990|       7.857|   0.1%/547|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 106   |      10|       0.955|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 108   |     279|      14.907|   1.3%/ 51|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 107   |     177|       3.728|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 107   |      90|      50.188|   3.2%/ 22|   4.6%/ 15|   5.0%/ 14|   5.3%/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  98   |     385|      87.063|   0.9%/ 81|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  99   |     128|      19.639|   7.5%/  9|   8.3%/  8|   8.5%/  8|   8.7%/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  99   |      30|      15.733|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 123   |      37|       5.349|   0.6%/112|   0.6%/111|   0.6%/112|   0.6%/112 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  98   |      41|       9.264|   1.9%/ 36|   2.7%/ 25|   2.9%/ 23|   3.2%/ 22 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 100   |      40|       5.863|   5.7%/ 12|   4.0%/ 17|   3.6%/ 19|   3.2%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 112   |      79|      28.429|   0.1%/526|   0.1%/973|   0.1%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  55   |      36|       1.362|   7.4%/  9|   3.1%/ 22|   1.9%/ 36|   0.7%/106 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 116   |     121|       3.694|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 104   |     121|       5.988|   0.5%/145|   0.4%/169|   0.4%/176|   0.4%/184 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 103   |     143|      34.974|   1.5%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 114   |   34555|     272.996|   2.2%/ 32|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 115   |     634|     236.371|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 123   |     243|       6.776|   0.8%/ 90|   0.9%/ 78|   0.9%/ 75|   0.9%/ 73 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  47   |       9|       0.304|   5.0%/ 14|   4.4%/ 16|   4.0%/ 17|   3.5%/ 19 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  56   |      36|       1.203|   2.6%/ 26|   1.1%/ 63|   0.6%/109|   0.2%/455 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 127   |    6156|     352.654|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 104   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 106   |      92|      14.317|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 108   |      68|       3.055|   0.1%/762|   0.1%/734|   0.1%/736|   0.1%/744 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 110   |     703|       3.412|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 111   |     378|     182.157|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 119   |     253|      47.050|   0.1%/753|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 102   |     247|      53.042|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 114   |    5207|      23.738|   1.8%/ 39|   1.4%/ 48|   1.3%/ 51|   1.3%/ 54 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 122   |     855|     202.628|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 112   |      22|       3.045|   1.6%/ 44|   1.4%/ 51|   1.3%/ 55|   1.2%/ 59 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 113   |   11628|     361.877|   1.8%/ 38|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 160   |    1358|      12.516|   0.7%/104|   0.6%/123|   0.5%/128|   0.5%/135 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 121   |    1573|      40.997|   0.7%/100|   0.6%/121|   0.5%/127|   0.5%/134 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 116   |    1643|     159.905|   0.4%/167|   0.5%/147|   0.5%/143|   0.5%/139 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 105   |     143|      52.059|   2.3%/ 30|   2.4%/ 28|   2.5%/ 28|   2.6%/ 27 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 111   |    1849|      95.295|   1.1%/ 61|   1.2%/ 57|   1.2%/ 56|   1.2%/ 55 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 114   |   11004|      74.987|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  42   |       3|       0.242|   5.7%/ 12|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 109   |    2187|      63.909|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 101   |     151|       9.289|   2.8%/ 24|   2.5%/ 28|   2.4%/ 29|   2.2%/ 31 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 113   |     332|      47.695|   2.3%/ 31|   3.1%/ 23|   3.3%/ 21|   3.5%/ 20 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  79   |      64|       8.047|   0.7%/103|   0.4%/183|   0.3%/222|   0.2%/281 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 112   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 105   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 119   |     112|      53.251|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  94   |      92|       5.805|   0.2%/399|   0.2%/349|   0.2%/338|   0.2%/330 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 106   |    3835|      65.252|   3.7%/ 18|   3.9%/ 18|   3.9%/ 18|   3.9%/ 17 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 130   |   28522|     605.568|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 105   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 120   |     650|      15.309|   1.1%/ 64|   0.9%/ 73|   0.9%/ 76|   0.9%/ 78 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 122   |    5544|     536.240|   0.4%/186|   0.3%/228|   0.3%/241|   0.3%/256 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 128   |    1968|     228.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 104   |      15|       0.869|   3.6%/ 19|   2.5%/ 28|   0.0%/ --|   4.6%/ 15 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 102   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 132   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 106   |      15|       2.017|   0.5%/128|   0.5%/146|   0.5%/151|   0.4%/156 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 108   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 114   |      50|       4.266|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 116   |    5323|      64.017|   0.4%/189|   0.3%/199|   0.3%/201|   0.3%/203 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 133   |  134105|     406.941|   0.5%/127|   0.5%/130|   0.5%/132|   0.5%/133 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 120   |    1365|      32.588|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 113   |     330|      33.354|   0.5%/151|   0.4%/155|   0.4%/156|   0.4%/156 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 122   |   44854|     675.157|   0.2%/310|   0.2%/358|   0.2%/373|   0.2%/389 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 104   |      30|       8.392|   0.8%/ 89|   0.6%/115|   0.6%/125|   0.5%/137 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 106   |      46|       1.358|   7.1%/ 10|   9.5%/  7|  10.1%/  7|  10.8%/  6 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 106   |      83|       2.583|   5.1%/ 14|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 100   |      44|       2.466|   6.4%/ 11|   5.7%/ 12|   5.6%/ 12|   5.4%/ 13 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 110   |       9|       0.621|   4.3%/ 16|   4.8%/ 14|   5.0%/ 14|   5.1%/ 13 |

