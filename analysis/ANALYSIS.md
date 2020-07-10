# State and Country COVID-19 Analysis #
## Updated: at 2020-07-10 for data as of 2020-07-09 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 37.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.3% of deaths and 53.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 118   |   32429|    1667.000|   0.1%/668|   0.1%/777|   0.1%/810|   0.1%/847 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 122   |   15857|    1785.213|   0.3%/276|   0.2%/278|   0.2%/277|   0.3%/277 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 112   |    8277|    1191.009|   0.3%/261|   0.2%/307|   0.2%/321|   0.2%/335 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 115   |    7250|     572.163|   0.6%/116|   0.7%/103|   0.7%/100|   0.7%/ 96 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 128   |    6739|     170.555|   1.2%/ 58|   1.2%/ 56|   1.3%/ 55|   1.3%/ 55 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 113   |    6852|     535.233|   0.3%/217|   0.3%/247|   0.3%/257|   0.3%/267 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 113   |    6269|     627.756|   0.2%/422|   0.2%/422|   0.2%/422|   0.2%/423 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 113   |    4357|    1222.041|   0.1%/775|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 124   |    3937|     183.291|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 118   |    3348|     720.203|   0.4%/164|   0.4%/162|   0.4%/161|   0.4%/161 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 132   |  133386|     404.759|   0.5%/129|   0.5%/135|   0.5%/136|   0.5%/138 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 115   |   69366|     328.107|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 121   |   44781|     674.058|   0.2%/301|   0.2%/348|   0.2%/362|   0.2%/378 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 140   |   34960|     580.354|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 113   |   33965|     268.336|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 146   |   30002|     447.285|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 129   |   28551|     606.179|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 121   |   21904|      16.091|   2.5%/ 27|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 141   |   12195|     146.263|   1.4%/ 50|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 112   |   11452|     356.413|   1.9%/ 37|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 107   |    1067|     217.677|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 107   |      17|      23.447|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 111   |    2015|     276.881|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31|   2.3%/ 31 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 108   |     312|     103.420|   1.7%/ 41|   1.4%/ 48|   1.4%/ 50|   1.3%/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 128   |    6739|     170.555|   1.2%/ 58|   1.2%/ 56|   1.3%/ 55|   1.3%/ 55 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 118   |    1712|     297.342|   0.1%/480|   0.1%/946|   0.1%/ ***|   0.0%/ *** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 113   |    4357|    1222.041|   0.1%/775|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 106   |     525|     539.003|   0.2%/455|   0.1%/474|   0.1%/471|   0.1%/466 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 124   |    3937|     183.291|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 120   |    2944|     277.257|   0.5%/134|   0.4%/167|   0.4%/177|   0.4%/188 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 101   |      19|      13.603|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 106   |      95|      53.330|   0.6%/121|   0.8%/ 89|   0.8%/ 83|   0.9%/ 78 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 115   |    7250|     572.163|   0.6%/116|   0.7%/103|   0.7%/100|   0.7%/ 96 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 116   |    2743|     407.373|   0.4%/166|   0.4%/182|   0.4%/186|   0.4%/189 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 107   |     738|     233.860|   0.4%/163|   0.4%/163|   0.4%/163|   0.4%/162 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 119   |     293|     100.540|   0.7%/ 94|   0.7%/ 93|   0.7%/ 94|   0.7%/ 94 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 116   |     610|     136.613|   0.8%/ 82|   0.9%/ 78|   0.9%/ 77|   0.9%/ 76 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 118   |    3348|     720.203|   0.4%/164|   0.4%/162|   0.4%/161|   0.4%/161 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 105   |     110|      81.913|   0.5%/128|   0.7%/100|   0.7%/ 94|   0.8%/ 89 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 113   |    3296|     545.145|   0.4%/188|   0.3%/221|   0.3%/231|   0.3%/242 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 112   |    8277|    1191.009|   0.3%/261|   0.2%/307|   0.2%/321|   0.2%/335 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 113   |    6269|     627.756|   0.2%/422|   0.2%/422|   0.2%/422|   0.2%/423 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 111   |    1535|     272.183|   0.4%/165|   0.3%/213|   0.3%/229|   0.3%/248 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 113   |    1183|     397.482|   1.2%/ 55|   1.4%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 113   |    1078|     175.574|   0.6%/114|   0.5%/126|   0.5%/129|   0.5%/132 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 105   |      24|      22.211|   0.8%/ 90|   0.7%/100|   0.7%/102|   0.7%/104 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 104   |     291|     150.198|   0.6%/115|   0.2%/305|   0.1%/538|   0.0%/ *** |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 116   |     553|     179.609|   0.9%/ 73|   1.1%/ 61|   1.2%/ 58|   1.2%/ 56 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 109   |     392|     288.030|   0.6%/110|   0.5%/152|   0.4%/168|   0.4%/188 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 122   |   15857|    1785.213|   0.3%/276|   0.2%/278|   0.2%/277|   0.3%/277 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 107   |     529|     252.197|   0.7%/102|   0.7%/104|   0.7%/104|   0.7%/104 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 118   |   32429|    1667.000|   0.1%/668|   0.1%/777|   0.1%/810|   0.1%/847 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 107   |    1481|     141.213|   0.8%/ 86|   0.6%/112|   0.6%/121|   0.5%/131 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 105   |      83|     109.335|   0.7%/ 99|   0.9%/ 73|   1.0%/ 68|   1.1%/ 63 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 112   |    3000|     256.618|   0.6%/114|   0.6%/115|   0.6%/115|   0.6%/114 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 113   |     409|     103.314|   0.6%/116|   0.6%/107|   0.7%/105|   0.7%/104 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 117   |     224|      53.164|   1.0%/ 68|   1.1%/ 63|   1.1%/ 61|   1.2%/ 60 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 113   |    6852|     535.233|   0.3%/217|   0.3%/247|   0.3%/257|   0.3%/267 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 111   |     158|      49.465|   0.4%/168|   0.5%/144|   0.5%/139|   0.5%/134 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 104   |     980|     924.996|   0.4%/169|   0.3%/224|   0.3%/246|   0.3%/272 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 116   |     881|     171.092|   1.9%/ 37|   2.1%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 121   |     102|     115.060|   1.0%/ 68|   0.8%/ 82|   0.8%/ 87|   0.7%/ 93 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 111   |     690|     100.968|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 115   |    2824|      97.378|   1.7%/ 41|   1.9%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 132   |  133386|     404.759|   0.5%/129|   0.5%/135|   0.5%/136|   0.5%/138 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 110   |     198|      61.636|   1.6%/ 43|   2.0%/ 35|   2.1%/ 33|   2.2%/ 32 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 112   |      56|      89.794|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 118   |    1928|     225.843|   1.0%/ 71|   1.0%/ 68|   1.0%/ 68|   1.0%/ 67 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 132   |    1398|     183.555|   0.6%/119|   0.6%/115|   0.6%/114|   0.6%/113 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 102   |      95|      53.200|   0.3%/236|   0.2%/326|   0.2%/353|   0.2%/383 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 112   |     814|     139.883|   0.4%/158|   0.3%/221|   0.3%/245|   0.3%/274 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  88   |      21|      35.666|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 110   |     966|      29.964|   2.8%/ 25|   2.6%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 121   |      87|      30.705|   3.8%/ 18|   3.9%/ 18|   3.9%/ 18|   3.9%/ 18 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 120   |     988|      22.985|   0.9%/ 80|   0.8%/ 87|   0.8%/ 88|   0.8%/ 90 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 103   |      23|       0.732|   5.7%/ 12|   6.0%/ 11|   6.1%/ 11|   6.1%/ 11 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 124   |    1716|      38.191|   3.1%/ 23|   3.2%/ 22|   3.2%/ 22|   3.2%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 106   |     534|     180.545|   2.2%/ 32|   1.8%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 131   |     106|       4.126|   0.2%/342|   0.2%/302|   0.2%/293|   0.2%/284 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 120   |     710|      79.749|   0.1%/720|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 119   |     286|      28.437|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 116   |     109|      70.714|   2.3%/ 30|   1.4%/ 51|   1.1%/ 62|   0.9%/ 80 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 114   |    2260|      13.417|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 101   |     448|      47.667|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 121   |    9788|     849.297|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  95   |      24|       2.026|   3.1%/ 23|   1.6%/ 44|   1.1%/ 60|   0.7%/ 98 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 103   |    1674|     145.954|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16|   4.2%/ 17 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 111   |     207|      62.668|   1.5%/ 47|   1.9%/ 37|   2.0%/ 35|   2.1%/ 34 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 101   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 115   |   69366|     328.107|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 121   |     261|      37.611|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 114   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  88   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 107   |     340|      12.819|   1.2%/ 56|   1.7%/ 40|   1.9%/ 37|   2.0%/ 34 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 123   |    8822|     232.176|   0.2%/343|   0.2%/452|   0.1%/490|   0.1%/533 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  48   |      53|       9.600|   1.1%/ 65|   1.6%/ 42|   1.8%/ 39|   1.9%/ 37 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  73   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 110   |    6897|     360.968|   2.2%/ 31|   1.6%/ 44|   1.4%/ 48|   1.3%/ 54 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 121   |    4642|       3.310|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 110   |    4882|      98.840|   4.1%/ 17|   3.9%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 113   |      24|       4.725|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 113   |     114|      27.949|   0.4%/178|   0.5%/128|   0.6%/120|   0.6%/113 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 114   |      86|       7.698|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 118   |     609|     104.579|   0.1%/883|   0.1%/869|   0.1%/862|   0.1%/853 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 115   |     840|      81.071|   1.3%/ 51|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 118   |    4942|     282.900|   0.9%/ 78|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 124   |    3789|      37.787|   2.6%/ 26|   2.1%/ 33|   2.0%/ 35|   1.9%/ 37 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 101   |     260|      40.154|   4.7%/ 14|   3.7%/ 18|   3.4%/ 20|   3.2%/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  79   |      57|      41.724|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  96   |     118|       1.191|   1.0%/ 70|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 111   |     329|      59.591|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 146   |   30002|     447.285|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 112   |      47|      21.824|   1.4%/ 51|   0.9%/ 77|   0.8%/ 87|   0.7%/100 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 109   |       3|       1.178|   4.2%/ 16|   4.6%/ 15|   4.8%/ 14|   5.1%/ 13 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  97   |      15|       4.095|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 123   |    9061|     108.968|   0.1%/780|   0.1%/940|   0.1%/990|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 111   |     136|       4.502|   2.2%/ 32|   1.2%/ 60|   0.9%/ 75|   0.7%/101 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 121   |     193|      18.027|   0.1%/704|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 116   |    1113|      67.034|   4.0%/ 17|   3.6%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  86   |      36|       2.915|   1.3%/ 53|   0.8%/ 83|   0.7%/ 98|   0.6%/120 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  75   |      26|      16.003|   1.6%/ 42|   0.2%/382|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  96   |     123|      10.610|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 106   |     730|      79.691|   3.5%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 117   |     593|      60.701|   0.2%/440|   0.1%/639|   0.1%/730|   0.1%/855 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 121   |   21904|      16.091|   2.5%/ 27|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 121   |    3407|      12.766|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 141   |   12195|     146.263|   1.4%/ 50|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 128   |    3180|      81.270|   5.2%/ 13|   4.2%/ 16|   3.9%/ 17|   3.7%/ 19 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 121   |    1747|     354.875|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 111   |     343|      37.299|   0.8%/ 86|   1.0%/ 69|   1.1%/ 66|   1.1%/ 63 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 140   |   34960|     580.354|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 113   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 148   |     989|       7.856|   0.1%/479|   0.1%/769|   0.1%/911|   0.1%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 105   |      10|       0.953|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 107   |     274|      14.660|   1.5%/ 45|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 106   |     173|       3.644|   1.9%/ 37|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 106   |      84|      46.684|   2.4%/ 29|   3.7%/ 19|   4.0%/ 17|   4.3%/ 16 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  97   |     382|      86.455|   0.9%/ 77|   0.9%/ 81|   0.9%/ 81|   0.8%/ 82 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  98   |     119|      18.274|   7.6%/  9|   8.8%/  8|   9.1%/  7|   9.4%/  7 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  98   |      30|      15.733|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 122   |      36|       5.324|   0.7%/102|   0.7%/ 94|   0.7%/ 93|   0.8%/ 92 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  97   |      41|       9.108|   1.5%/ 45|   2.2%/ 32|   2.3%/ 30|   2.5%/ 28 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  99   |      39|       5.637|   6.1%/ 11|   5.5%/ 12|   5.3%/ 13|   5.2%/ 13 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 111   |      79|      28.417|   0.2%/457|   0.1%/709|   0.1%/825|   0.1%/989 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  54   |      36|       1.378|   7.9%/  9|   4.3%/ 16|   3.1%/ 22|   1.8%/ 38 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 115   |     121|       3.694|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 103   |     121|       5.962|   0.5%/145|   0.4%/177|   0.4%/188|   0.3%/200 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 102   |     140|      34.402|   1.3%/ 54|   1.1%/ 66|   1.0%/ 69|   1.0%/ 72 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 113   |   33965|     268.336|   2.2%/ 31|   1.9%/ 37|   1.8%/ 39|   1.7%/ 41 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 114   |     624|     232.868|   1.5%/ 45|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 122   |     241|       6.721|   0.8%/ 88|   0.9%/ 73|   1.0%/ 71|   1.0%/ 68 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  46   |       9|       0.296|   4.8%/ 14|   4.7%/ 15|   4.3%/ 16|   3.8%/ 18 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  55   |      36|       1.203|   2.7%/ 25|   1.6%/ 42|   1.3%/ 53|   0.9%/ 74 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 126   |    6154|     352.527|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 103   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 105   |      91|      14.157|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 107   |      68|       3.054|   0.1%/699|   0.1%/634|   0.1%/622|   0.1%/612 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 109   |     690|       3.349|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 110   |     373|     179.356|   2.3%/ 30|   2.0%/ 35|   1.9%/ 37|   1.8%/ 38 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 118   |     252|      47.037|   0.1%/748|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 101   |     240|      51.406|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 113   |    5144|      23.452|   1.8%/ 38|   1.5%/ 47|   1.4%/ 50|   1.3%/ 54 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 121   |     828|     196.222|   3.0%/ 23|   3.3%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 111   |      22|       3.018|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 112   |   11452|     356.413|   1.9%/ 37|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 159   |    1347|      12.413|   0.6%/107|   0.5%/131|   0.5%/139|   0.5%/149 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 120   |    1565|      40.790|   0.7%/ 99|   0.6%/122|   0.5%/130|   0.5%/139 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 115   |    1636|     159.212|   0.4%/167|   0.5%/143|   0.5%/138|   0.5%/134 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 104   |     139|      50.701|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 110   |    1828|      94.212|   1.1%/ 60|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 113   |   10831|      73.809|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  41   |       3|       0.242|   8.2%/  8|   0.4%/196|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 108   |    2136|      62.410|   2.9%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 100   |     148|       9.109|   3.0%/ 23|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 112   |     328|      47.112|   2.0%/ 34|   2.7%/ 25|   2.9%/ 24|   3.1%/ 22 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  78   |      64|       8.037|   0.8%/ 91|   0.5%/138|   0.4%/155|   0.4%/176 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 111   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 104   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 118   |     111|      53.243|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  93   |      92|       5.795|   0.2%/366|   0.2%/306|   0.2%/290|   0.3%/276 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 105   |    3691|      62.801|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17|   4.0%/ 17 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 129   |   28551|     606.179|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 104   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 119   |     643|      15.149|   1.1%/ 65|   0.9%/ 80|   0.8%/ 85|   0.8%/ 89 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 121   |    5528|     534.726|   0.4%/188|   0.3%/240|   0.3%/259|   0.2%/281 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 127   |    1968|     228.746|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 103   |      14|       0.813|   3.6%/ 19|  11.9%/  6|   2.5%/ 28|   0.0%/ -- |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 101   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 131   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 105   |      15|       2.009|   0.6%/111|   0.6%/112|   0.6%/112|   0.6%/111 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 107   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 113   |      50|       4.267|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 115   |    5304|      63.783|   0.4%/190|   0.3%/201|   0.3%/204|   0.3%/207 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 132   |  133386|     404.759|   0.5%/129|   0.5%/135|   0.5%/136|   0.5%/138 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 119   |    1344|      32.101|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 112   |     328|      33.203|   0.5%/149|   0.5%/153|   0.4%/154|   0.4%/155 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 121   |   44781|     674.058|   0.2%/301|   0.2%/348|   0.2%/362|   0.2%/378 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 103   |      29|       8.359|   0.9%/ 79|   0.8%/ 91|   0.7%/ 95|   0.7%/ 99 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 105   |      40|       1.167|   6.6%/ 10|   9.1%/  7|   9.7%/  7|  10.4%/  7 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 105   |      79|       2.456|   5.0%/ 14|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  99   |      42|       2.367|   7.7%/  9|  11.9%/  6|  11.9%/  6|  11.9%/  6 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 109   |       9|       0.602|   0.0%/ --|   4.0%/ 17|   4.0%/ 17|   0.0%/ -- |

