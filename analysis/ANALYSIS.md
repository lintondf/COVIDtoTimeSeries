# State and Country COVID-19 Analysis #
## Updated: at 2020-07-22 for data as of 2020-07-21 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.1% of deaths and 39.5% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.0% of deaths and 57.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 130   |   32619|    1676.741|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 134   |   15842|    1783.591|   0.2%/361|   0.2%/433|   0.2%/458|   0.1%/488 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 124   |    8471|    1218.947|   0.2%/354|   0.2%/404|   0.2%/419|   0.2%/436 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 140   |    7921|     200.476|   1.2%/ 56|   1.2%/ 55|   1.2%/ 55|   1.2%/ 55 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 127   |    7595|     599.324|   0.3%/230|   0.2%/308|   0.2%/339|   0.2%/379 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 125   |    7069|     552.200|   0.3%/275|   0.2%/309|   0.2%/320|   0.2%/331 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 125   |    6392|     640.078|   0.1%/481|   0.1%/526|   0.1%/540|   0.1%/556 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    5086|     236.801|   2.1%/ 33|   2.3%/ 30|   2.4%/ 29|   2.4%/ 28 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 125   |    4405|    1235.473|   0.1%/659|   0.1%/599|   0.1%/585|   0.1%/572 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 127   |    4151|     143.151|   2.9%/ 24|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 144   |  141934|     430.697|   0.5%/132|   0.5%/133|   0.5%/133|   0.5%/133 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 127   |   82253|     389.066|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 133   |   45599|     686.363|   0.2%/442|   0.1%/522|   0.1%/547|   0.1%/574 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 125   |   40901|     323.131|   1.6%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 152   |   35088|     582.491|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 158   |   30192|     450.120|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 133   |   28817|      21.170|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 141   |   28432|     603.651|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 153   |   14588|     174.961|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 124   |   13633|     424.277|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 119   |    1320|     269.125|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 119   |      18|      24.960|   0.7%/103|   0.6%/108|   0.6%/109|   0.6%/110 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 123   |    2868|     394.060|   2.9%/ 24|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 120   |     370|     122.646|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 140   |    7921|     200.476|   1.2%/ 56|   1.2%/ 55|   1.2%/ 55|   1.2%/ 55 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 130   |    1762|     305.912|   0.2%/316|   0.2%/302|   0.2%/299|   0.2%/297 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 125   |    4405|    1235.473|   0.1%/659|   0.1%/599|   0.1%/585|   0.1%/572 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 118   |     524|     538.616|   0.1%/479|   0.1%/479|   0.1%/479|   0.1%/479 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    5086|     236.801|   2.1%/ 33|   2.3%/ 30|   2.4%/ 29|   2.4%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 132   |    3209|     302.278|   0.7%/ 95|   0.8%/ 87|   0.8%/ 85|   0.8%/ 83 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 113   |      24|      17.204|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 118   |     123|      68.807|   1.4%/ 50|   1.7%/ 41|   1.7%/ 40|   1.8%/ 38 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 127   |    7595|     599.324|   0.3%/230|   0.2%/308|   0.2%/339|   0.2%/379 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 128   |    2845|     422.566|   0.3%/213|   0.3%/230|   0.3%/234|   0.3%/239 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 119   |     801|     253.928|   0.7%/105|   0.8%/ 92|   0.8%/ 89|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 131   |     315|     107.961|   0.6%/110|   0.6%/114|   0.6%/115|   0.6%/116 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 128   |     678|     151.765|   0.9%/ 81|   0.9%/ 81|   0.9%/ 81|   0.9%/ 81 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 130   |    3545|     762.644|   0.4%/166|   0.4%/179|   0.4%/183|   0.4%/188 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 117   |     118|      87.952|   0.5%/128|   0.5%/135|   0.5%/137|   0.5%/139 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 125   |    3401|     562.595|   0.3%/247|   0.3%/269|   0.3%/275|   0.2%/281 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 124   |    8471|    1218.947|   0.2%/354|   0.2%/404|   0.2%/419|   0.2%/436 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 125   |    6392|     640.078|   0.1%/481|   0.1%/526|   0.1%/540|   0.1%/556 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 123   |    1591|     282.135|   0.3%/206|   0.3%/221|   0.3%/224|   0.3%/228 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 125   |    1392|     467.553|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 125   |    1152|     187.776|   0.5%/131|   0.5%/144|   0.5%/148|   0.5%/152 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 117   |      40|      37.692|   2.2%/ 31|   2.7%/ 26|   2.8%/ 25|   2.9%/ 24 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 116   |     305|     157.919|   0.7%/102|   0.8%/ 84|   0.9%/ 79|   0.9%/ 75 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 128   |     667|     216.387|   1.3%/ 52|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 121   |     401|     295.193|   0.3%/238|   0.2%/328|   0.2%/360|   0.2%/400 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 134   |   15842|    1783.591|   0.2%/361|   0.2%/433|   0.2%/458|   0.1%/488 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 119   |     583|     278.185|   0.8%/ 89|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 130   |   32619|    1676.741|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 119   |    1688|     160.947|   1.1%/ 63|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 117   |      93|     122.360|   0.9%/ 78|   1.0%/ 70|   1.0%/ 68|   1.0%/ 67 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 124   |    3200|     273.781|   0.6%/117|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 125   |     457|     115.382|   0.9%/ 79|   1.0%/ 72|   1.0%/ 71|   1.0%/ 69 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 129   |     266|      62.977|   1.4%/ 51|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 125   |    7069|     552.200|   0.3%/275|   0.2%/309|   0.2%/320|   0.2%/331 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 123   |     181|      56.532|   0.9%/ 73|   1.1%/ 63|   1.1%/ 62|   1.2%/ 60 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 116   |     998|     942.409|   0.2%/349|   0.1%/467|   0.1%/508|   0.1%/557 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 128   |    1192|     231.465|   2.4%/ 28|   2.6%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 133   |     120|     136.043|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 123   |     872|     127.604|   1.8%/ 39|   1.8%/ 38|   1.8%/ 37|   1.8%/ 37 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 127   |    4151|     143.151|   2.9%/ 24|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 144   |  141934|     430.697|   0.5%/132|   0.5%/133|   0.5%/133|   0.5%/133 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 122   |     254|      79.358|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 124   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 130   |    2073|     242.857|   0.6%/124|   0.4%/169|   0.4%/186|   0.3%/208 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 144   |    1466|     192.522|   0.5%/145|   0.5%/153|   0.4%/156|   0.4%/158 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 114   |     101|      56.197|   0.4%/156|   0.5%/138|   0.5%/135|   0.5%/131 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 124   |     851|     146.077|   0.4%/161|   0.5%/153|   0.5%/151|   0.5%/148 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 100   |      25|      42.750|   1.1%/ 63|   1.4%/ 49|   1.5%/ 47|   1.6%/ 45 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 122   |    1232|      38.238|   2.1%/ 34|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 133   |     121|      42.417|   2.8%/ 25|   2.4%/ 28|   2.3%/ 29|   2.3%/ 31 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 132   |    1096|      25.492|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75|   0.9%/ 75 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 115   |      32|       1.024|   2.8%/ 25|   1.4%/ 49|   1.1%/ 64|   0.8%/ 91 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 136   |    2437|      54.228|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 118   |     668|     225.751|   1.9%/ 36|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 143   |     118|       4.604|   1.3%/ 52|   1.7%/ 40|   1.8%/ 38|   1.9%/ 36 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 132   |     712|      79.952|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 131   |     382|      37.918|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 128   |     131|      84.598|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 126   |    2744|      16.285|   1.7%/ 40|   1.5%/ 46|   1.5%/ 47|   1.4%/ 49 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 113   |     513|      54.557|   1.1%/ 62|   1.0%/ 72|   0.9%/ 75|   0.9%/ 78 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 133   |    9808|     851.073|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 107   |      32|       2.743|   2.9%/ 24|   2.4%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 115   |    2325|     202.713|   2.9%/ 24|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 123   |     259|      78.570|   1.7%/ 40|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 113   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 127   |   82253|     389.066|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 133   |     313|      45.051|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 126   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 100   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 119   |     385|      14.521|   0.6%/126|   0.6%/115|   0.6%/113|   0.6%/111 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 135   |    8934|     235.103|   0.1%/590|   0.1%/780|   0.1%/848|   0.1%/929 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  60   |      55|      10.023|   0.4%/190|   0.6%/108|   0.7%/ 96|   0.8%/ 86 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  85   |      75|       4.632|   0.1%/839|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 122   |    8561|     448.068|   1.3%/ 54|   1.0%/ 66|   1.0%/ 70|   0.9%/ 74 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 133   |    4644|       3.312|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 122   |    7312|     148.039|   3.4%/ 20|   3.1%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 125   |      63|      12.451|  10.1%/  7|  13.9%/  5|  12.0%/  6|   8.0%/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 125   |     123|      30.245|   0.5%/143|   0.4%/163|   0.4%/170|   0.4%/178 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 126   |      87|       7.782|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 130   |     612|     105.073|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 127   |    1008|      97.352|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 130   |    5404|     309.382|   0.7%/ 95|   0.7%/105|   0.6%/107|   0.6%/111 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 136   |    4551|      45.385|   1.7%/ 41|   1.4%/ 51|   1.3%/ 54|   1.2%/ 57 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 113   |     352|      54.340|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  91   |      51|      37.555|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 108   |     174|       1.765|   3.3%/ 21|   4.0%/ 17|   4.2%/ 17|   4.3%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 123   |     328|      59.371|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 158   |   30192|     450.120|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 124   |      47|      21.629|   0.2%/424|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 121   |       4|       1.688|   3.8%/ 18|   4.1%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 109   |      15|       4.119|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 135   |    9112|     109.585|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 123   |     153|       5.061|   1.4%/ 50|   1.2%/ 56|   1.2%/ 57|   1.2%/ 59 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 133   |     195|      18.157|   0.1%/575|   0.1%/469|   0.2%/446|   0.2%/425 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 128   |    1615|      97.277|   3.0%/ 23|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  98   |      41|       3.328|   1.0%/ 66|   1.0%/ 70|   1.0%/ 71|   1.0%/ 73 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  87   |      26|      16.328|   0.2%/302|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 108   |     156|      13.435|   1.4%/ 48|   1.0%/ 72|   0.8%/ 83|   0.7%/100 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 118   |     972|     106.129|   2.6%/ 26|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 129   |     598|      61.208|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 133   |   28817|      21.170|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 133   |    4280|      16.035|   2.0%/ 35|   2.1%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 153   |   14588|     174.961|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 140   |    4235|     108.245|   2.9%/ 24|   2.2%/ 32|   2.0%/ 35|   1.8%/ 38 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 133   |    1754|     356.383|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 123   |     413|      44.969|   1.6%/ 43|   1.9%/ 36|   2.0%/ 35|   2.1%/ 34 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 152   |   35088|     582.491|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 125   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 160   |     990|       7.861|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 117   |      11|       1.018|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 119   |     450|      24.074|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 118   |     244|       5.125|   2.8%/ 25|   3.1%/ 22|   3.2%/ 22|   3.3%/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 118   |     150|      83.279|   4.6%/ 15|   5.1%/ 13|   5.2%/ 13|   5.3%/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 109   |     415|      93.845|   0.7%/104|   0.6%/123|   0.5%/129|   0.5%/136 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 110   |     233|      35.659|   5.3%/ 13|   4.5%/ 15|   4.3%/ 16|   4.1%/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 110   |      31|      16.350|   0.2%/332|   0.2%/298|   0.2%/295|   0.2%/294 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 134   |      40|       5.933|   0.8%/ 86|   0.9%/ 78|   0.9%/ 77|   0.9%/ 75 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 109   |      71|      15.826|   1.8%/ 38|   1.3%/ 51|   1.2%/ 57|   1.1%/ 65 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 111   |      52|       7.619|   3.3%/ 21|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 123   |      80|      28.565|   0.1%/567|   0.1%/497|   0.1%/477|   0.2%/457 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  66   |      67|       2.542|   5.1%/ 13|   6.4%/ 11|   6.6%/ 10|   6.9%/ 10 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 127   |     123|       3.746|   0.1%/587|   0.2%/439|   0.2%/412|   0.2%/389 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 115   |     122|       6.032|   0.1%/533|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 114   |     158|      38.741|   0.9%/ 77|   0.8%/ 91|   0.7%/ 95|   0.7%/100 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 125   |   40901|     323.131|   1.6%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 50 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 126   |     709|     264.552|   1.1%/ 63|   1.0%/ 72|   0.9%/ 75|   0.9%/ 78 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 134   |     276|       7.695|   1.1%/ 61|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  58   |      11|       0.357|   0.8%/ 82|   3.3%/ 21|   4.0%/ 17|   4.7%/ 15 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  12   |       7|       2.847|  26.0%/  2|  14.5%/  5|  26.0%/  2|  51.8%/  1 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  67   |      41|       1.355|   1.2%/ 58|   0.6%/119|   0.4%/166|   0.2%/278 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 138   |    6163|     353.024|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 115   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 117   |     104|      16.111|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 119   |      69|       3.097|   0.1%/611|   0.1%/617|   0.1%/616|   0.1%/614 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 121   |     823|       3.994|   1.3%/ 52|   1.1%/ 63|   1.0%/ 66|   1.0%/ 70 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 122   |     437|     210.515|   1.6%/ 44|   1.4%/ 50|   1.4%/ 51|   1.3%/ 53 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 130   |     255|      47.536|   0.1%/643|   0.1%/603|   0.1%/592|   0.1%/582 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 113   |     337|      72.139|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 125   |    5808|      26.480|   1.1%/ 65|   0.8%/ 85|   0.8%/ 92|   0.7%/101 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 133   |    1165|     276.227|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 123   |      32|       4.474|   3.9%/ 17|   4.7%/ 15|   4.9%/ 14|   5.2%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 124   |   13633|     424.277|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 171   |    1790|      16.497|   0.9%/ 73|   1.0%/ 69|   1.0%/ 68|   1.0%/ 67 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 132   |    1646|      42.885|   0.5%/149|   0.4%/178|   0.4%/187|   0.4%/196 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 127   |    1706|     165.991|   0.3%/227|   0.3%/269|   0.2%/283|   0.2%/299 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 116   |     164|      59.804|   1.3%/ 53|   0.9%/ 74|   0.8%/ 82|   0.7%/ 93 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 122   |    2075|     106.914|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 125   |   12756|      86.928|   1.3%/ 53|   1.2%/ 59|   1.1%/ 61|   1.1%/ 63 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  53   |       5|       0.414|   0.0%/ --|   7.7%/  9|   7.7%/  9|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 120   |    2618|      76.506|   1.8%/ 38|   1.5%/ 46|   1.4%/ 49|   1.3%/ 52 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 112   |     173|      10.666|   1.8%/ 38|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 124   |     502|      72.019|   2.7%/ 25|   2.8%/ 24|   2.8%/ 24|   2.9%/ 24 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  90   |      66|       8.319|   0.4%/172|   0.5%/146|   0.5%/139|   0.5%/133 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 123   |      27|       4.744|   0.2%/304|   0.3%/240|   0.3%/229|   0.3%/220 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 116   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 130   |     112|      53.451|   0.1%/690|   0.1%/489|   0.2%/450|   0.2%/415 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 105   |      93|       5.878|   0.1%/743|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 117   |    5450|      92.730|   3.2%/ 22|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 141   |   28432|     603.651|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 116   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 131   |     698|      16.457|   0.8%/ 86|   0.7%/ 92|   0.7%/ 94|   0.7%/ 96 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 133   |    5664|     547.906|   0.2%/295|   0.2%/357|   0.2%/376|   0.2%/396 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 139   |    1971|     229.067|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 115   |      30|       1.720|  11.2%/  6|   4.4%/ 16|   5.1%/ 14|   7.4%/  9 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 113   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 143   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 117   |      15|       2.012|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 119   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 125   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 127   |    5534|      66.546|   0.3%/199|   0.3%/204|   0.3%/205|   0.3%/207 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 144   |  141934|     430.697|   0.5%/132|   0.5%/133|   0.5%/133|   0.5%/133 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 131   |    1558|      37.190|   1.2%/ 59|   1.0%/ 66|   1.0%/ 69|   1.0%/ 71 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 124   |     342|      34.624|   0.3%/204|   0.3%/238|   0.3%/248|   0.3%/260 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 133   |   45599|     686.363|   0.2%/442|   0.1%/522|   0.1%/547|   0.1%/574 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 115   |      33|       9.487|   1.0%/ 69|   1.0%/ 67|   1.0%/ 67|   1.0%/ 66 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 117   |     102|       2.998|   6.0%/ 11|   5.4%/ 13|   5.2%/ 13|   5.0%/ 14 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 117   |     125|       3.885|   3.7%/ 18|   3.2%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 111   |     138|       7.704|  12.2%/  6|  16.0%/  4|  17.1%/  4|  18.2%/  4 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 121   |      30|       2.007|   7.4%/  9|   7.1%/ 10|   7.0%/ 10|   6.9%/ 10 |

