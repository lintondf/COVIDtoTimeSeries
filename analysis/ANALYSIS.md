# State and Country COVID-19 Analysis #
## Updated: at 2020-07-12 for data as of 2020-07-11 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.7% of deaths and 37.9% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.0% of deaths and 52.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 120   |   32511|    1671.211|   0.1%/718|   0.1%/824|   0.1%/856|   0.1%/890 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 124   |   15905|    1790.614|   0.3%/244|   0.3%/227|   0.3%/222|   0.3%/217 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 114   |    8316|    1196.610|   0.3%/259|   0.2%/284|   0.2%/290|   0.2%/296 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 117   |    7343|     579.437|   0.6%/126|   0.6%/117|   0.6%/114|   0.6%/111 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 130   |    6937|     175.574|   1.3%/ 53|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 115   |    6896|     538.647|   0.3%/206|   0.3%/218|   0.3%/221|   0.3%/223 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 115   |    6295|     630.283|   0.2%/393|   0.2%/376|   0.2%/372|   0.2%/367 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 115   |    4358|    1222.320|   0.1%/909|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 126   |    4080|     189.955|   1.5%/ 46|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 120   |    3384|     727.836|   0.5%/150|   0.5%/141|   0.5%/139|   0.5%/137 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 134   |  134817|     409.102|   0.6%/126|   0.5%/128|   0.5%/129|   0.5%/130 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 117   |   71636|     338.846|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 123   |   44938|     676.413|   0.2%/315|   0.2%/361|   0.2%/375|   0.2%/390 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 142   |   34978|     580.657|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 115   |   35136|     277.586|   2.1%/ 32|   1.9%/ 37|   1.8%/ 39|   1.7%/ 40 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 148   |   30031|     447.712|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 131   |   28496|     605.005|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 123   |   22799|      16.749|   2.5%/ 28|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 143   |   12562|     150.666|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 114   |   11803|     367.345|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 109   |    1103|     224.898|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 109   |      18|      24.062|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 113   |    2117|     290.905|   2.4%/ 29|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 110   |     320|     106.162|   1.6%/ 43|   1.4%/ 49|   1.4%/ 50|   1.3%/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 130   |    6937|     175.574|   1.3%/ 53|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 120   |    1720|     298.763|   0.2%/353|   0.2%/391|   0.2%/401|   0.2%/409 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 115   |    4358|    1222.320|   0.1%/909|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 108   |     523|     537.226|   0.2%/452|   0.2%/430|   0.2%/421|   0.2%/412 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 126   |    4080|     189.955|   1.5%/ 46|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 122   |    2977|     280.383|   0.6%/124|   0.5%/133|   0.5%/134|   0.5%/136 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 103   |      19|      13.640|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 108   |      99|      55.391|   0.9%/ 79|   1.2%/ 57|   1.3%/ 53|   1.4%/ 49 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 117   |    7343|     579.437|   0.6%/126|   0.6%/117|   0.6%/114|   0.6%/111 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 118   |    2762|     410.193|   0.4%/174|   0.4%/188|   0.4%/191|   0.4%/195 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 109   |     745|     236.112|   0.4%/155|   0.5%/148|   0.5%/146|   0.5%/144 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 121   |     297|     101.785|   0.7%/ 98|   0.7%/102|   0.7%/103|   0.7%/104 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 118   |     622|     139.140|   0.9%/ 80|   0.9%/ 77|   0.9%/ 77|   0.9%/ 76 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 120   |    3384|     727.836|   0.5%/150|   0.5%/141|   0.5%/139|   0.5%/137 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 107   |     112|      83.028|   0.5%/127|   0.7%/106|   0.7%/102|   0.7%/ 98 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 115   |    3316|     548.470|   0.4%/193|   0.3%/218|   0.3%/224|   0.3%/231 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 114   |    8316|    1196.610|   0.3%/259|   0.2%/284|   0.2%/290|   0.2%/296 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 115   |    6295|     630.283|   0.2%/393|   0.2%/376|   0.2%/372|   0.2%/367 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 113   |    1544|     273.832|   0.4%/175|   0.3%/215|   0.3%/228|   0.3%/242 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 115   |    1218|     409.234|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.5%/ 47 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 115   |    1090|     177.656|   0.6%/115|   0.6%/121|   0.6%/123|   0.6%/124 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 107   |      24|      22.532|   0.6%/112|   0.5%/145|   0.4%/156|   0.4%/168 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 106   |     291|     150.226|   0.5%/136|   0.2%/376|   0.1%/691|   0.0%/ *** |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 118   |     572|     185.590|   1.2%/ 58|   1.5%/ 46|   1.6%/ 43|   1.7%/ 41 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 111   |     394|     289.967|   0.6%/121|   0.4%/168|   0.4%/186|   0.3%/207 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 124   |   15905|    1790.614|   0.3%/244|   0.3%/227|   0.3%/222|   0.3%/217 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 109   |     538|     256.796|   0.8%/ 90|   0.8%/ 82|   0.9%/ 80|   0.9%/ 78 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 120   |   32511|    1671.211|   0.1%/718|   0.1%/824|   0.1%/856|   0.1%/890 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 109   |    1506|     143.563|   0.8%/ 82|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 107   |      85|     111.733|   0.7%/ 97|   0.9%/ 76|   1.0%/ 72|   1.0%/ 67 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 114   |    3037|     259.783|   0.6%/114|   0.6%/113|   0.6%/113|   0.6%/112 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 115   |     416|     105.134|   0.7%/100|   0.8%/ 88|   0.8%/ 86|   0.8%/ 83 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 119   |     230|      54.596|   1.1%/ 61|   1.3%/ 55|   1.3%/ 54|   1.3%/ 52 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 115   |    6896|     538.647|   0.3%/206|   0.3%/218|   0.3%/221|   0.3%/223 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 113   |     160|      50.032|   0.5%/133|   0.6%/107|   0.7%/101|   0.7%/ 96 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 106   |     983|     928.258|   0.4%/193|   0.2%/280|   0.2%/316|   0.2%/363 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 118   |     927|     180.082|   2.1%/ 33|   2.4%/ 29|   2.5%/ 28|   2.6%/ 27 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 123   |     106|     119.325|   1.4%/ 50|   1.4%/ 48|   1.4%/ 48|   1.5%/ 47 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 113   |     720|     105.433|   1.8%/ 38|   2.0%/ 34|   2.1%/ 33|   2.1%/ 32 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 117   |    2991|     103.142|   2.1%/ 33|   2.5%/ 28|   2.6%/ 26|   2.7%/ 25 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 134   |  134817|     409.102|   0.6%/126|   0.5%/128|   0.5%/129|   0.5%/130 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 112   |     207|      64.437|   1.8%/ 39|   2.1%/ 33|   2.2%/ 31|   2.3%/ 30 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 114   |      56|      89.756|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 120   |    1967|     230.480|   1.0%/ 68|   1.1%/ 65|   1.1%/ 65|   1.1%/ 64 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 134   |    1418|     186.155|   0.6%/109|   0.7%/102|   0.7%/100|   0.7%/ 98 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 104   |      96|      53.420|   0.3%/270|   0.2%/361|   0.2%/387|   0.2%/415 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 114   |     820|     140.822|   0.4%/162|   0.3%/199|   0.3%/210|   0.3%/222 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  90   |      21|      36.203|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 112   |    1010|      31.346|   2.6%/ 27|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 123   |      93|      32.574|   3.3%/ 21|   3.1%/ 22|   3.1%/ 23|   3.0%/ 23 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 122   |    1004|      23.357|   0.9%/ 80|   0.8%/ 83|   0.8%/ 83|   0.8%/ 84 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 105   |      25|       0.788|   5.3%/ 13|   5.1%/ 13|   5.0%/ 14|   4.8%/ 14 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 126   |    1820|      40.500|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 108   |     557|     188.241|   2.2%/ 31|   2.0%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 133   |     107|       4.157|   0.3%/272|   0.3%/229|   0.3%/219|   0.3%/211 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 122   |     710|      79.704|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 121   |     304|      30.161|   3.2%/ 21|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 118   |     111|      71.756|   2.2%/ 32|   1.3%/ 51|   1.1%/ 61|   0.9%/ 74 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 116   |    2350|      13.946|   2.2%/ 31|   2.0%/ 34|   2.0%/ 35|   2.0%/ 35 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 103   |     461|      48.995|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 123   |    9792|     849.652|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  97   |      25|       2.135|   0.0%/ --|   3.1%/ 22|   3.1%/ 22|   7.4%/  9 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 105   |    1802|     157.064|   4.1%/ 17|   3.9%/ 18|   3.9%/ 18|   3.8%/ 18 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 113   |     216|      65.294|   1.5%/ 47|   1.8%/ 39|   1.8%/ 37|   1.9%/ 36 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 103   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 117   |   71636|     338.846|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 123   |     269|      38.726|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 116   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  90   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 109   |     352|      13.278|   0.9%/ 74|   1.2%/ 57|   1.3%/ 54|   1.4%/ 50 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 125   |    8847|     232.817|   0.2%/372|   0.1%/477|   0.1%/511|   0.1%/551 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  50   |      54|       9.767|   1.4%/ 48|   1.2%/ 58|   1.0%/ 68|   0.8%/ 87 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  75   |      74|       4.555|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 112   |    7086|     370.829|   2.0%/ 34|   1.5%/ 47|   1.3%/ 51|   1.2%/ 57 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 123   |    4641|       3.310|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 112   |    5261|     106.516|   4.1%/ 17|   3.9%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 115   |      27|       5.355|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 115   |     116|      28.511|   0.6%/115|   0.8%/ 84|   0.9%/ 79|   0.9%/ 75 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 116   |      86|       7.711|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 120   |     610|     104.687|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 117   |     868|      83.760|   1.4%/ 48|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 120   |    5024|     287.632|   0.9%/ 81|   0.8%/ 84|   0.8%/ 86|   0.8%/ 87 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 126   |    3915|      39.048|   2.4%/ 28|   1.9%/ 35|   1.8%/ 38|   1.7%/ 41 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 103   |     273|      42.053|   4.2%/ 16|   3.1%/ 22|   2.8%/ 25|   2.5%/ 28 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  81   |      57|      41.771|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  98   |     123|       1.246|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.2%/ 32 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 113   |     329|      59.599|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 148   |   30031|     447.712|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 114   |      48|      21.896|   1.0%/ 67|   0.6%/122|   0.5%/151|   0.3%/199 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 111   |       3|       1.265|   3.5%/ 19|   3.7%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  99   |      15|       4.080|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 125   |    9075|     109.136|   0.1%/779|   0.1%/884|   0.1%/912|   0.1%/941 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 113   |     140|       4.612|   1.9%/ 36|   1.2%/ 60|   1.0%/ 71|   0.8%/ 86 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 123   |     193|      18.032|   0.1%/925|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 118   |    1193|      71.831|   3.9%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  88   |      37|       3.011|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  77   |      26|      16.209|   1.2%/ 57|   0.4%/165|   0.2%/284|   0.1%/833 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  98   |     132|      11.364|   2.3%/ 30|   2.7%/ 25|   2.9%/ 24|   3.0%/ 23 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 108   |     781|      85.231|   3.4%/ 20|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 119   |     595|      60.879|   0.2%/401|   0.1%/479|   0.1%/505|   0.1%/534 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 123   |   22799|      16.749|   2.5%/ 28|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 123   |    3538|      13.254|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 143   |   12562|     150.666|   1.4%/ 49|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 130   |    3376|      86.288|   4.7%/ 15|   3.7%/ 19|   3.4%/ 20|   3.1%/ 22 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 123   |    1748|     355.085|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 113   |     350|      38.121|   0.9%/ 81|   1.0%/ 67|   1.1%/ 64|   1.1%/ 62 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 142   |   34978|     580.657|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 115   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 150   |     990|       7.857|   0.1%/648|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 107   |      10|       0.957|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 109   |     282|      15.099|   1.1%/ 63|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 108   |     181|       3.813|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 108   |      97|      53.939|   4.1%/ 17|   5.8%/ 12|   6.2%/ 11|   6.6%/ 10 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  99   |     388|      87.687|   0.8%/ 83|   0.8%/ 90|   0.8%/ 91|   0.7%/ 93 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 100   |     136|      20.819|   7.2%/  9|   7.6%/  9|   7.6%/  9|   7.7%/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 100   |      30|      15.733|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 124   |      37|       5.365|   0.6%/125|   0.5%/136|   0.5%/140|   0.5%/146 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  99   |      43|       9.498|   2.3%/ 31|   3.2%/ 21|   3.5%/ 20|   3.7%/ 19 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 101   |      41|       6.030|   7.2%/ 10|   3.8%/ 18|   2.8%/ 25|   1.8%/ 38 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 113   |      79|      28.428|   0.1%/614|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  56   |      36|       1.369|   6.7%/ 10|   2.2%/ 32|   0.9%/ 74|   0.0%/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 117   |     121|       3.700|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 105   |     122|       6.007|   0.5%/152|   0.4%/181|   0.4%/190|   0.3%/201 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 104   |     145|      35.572|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 115   |   35136|     277.586|   2.1%/ 32|   1.9%/ 37|   1.8%/ 39|   1.7%/ 40 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 116   |     643|     239.761|   1.5%/ 45|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 124   |     245|       6.826|   0.7%/ 94|   0.8%/ 84|   0.8%/ 82|   0.9%/ 80 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  48   |       9|       0.309|   5.1%/ 13|   4.1%/ 17|   3.6%/ 19|   3.1%/ 22 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  57   |      37|       1.232|   2.5%/ 28|   1.2%/ 56|   0.9%/ 75|   0.6%/113 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 128   |    6158|     352.777|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 105   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 107   |      93|      14.436|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 109   |      68|       3.057|   0.1%/830|   0.1%/879|   0.1%/914|   0.1%/961 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 111   |     717|       3.480|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 112   |     385|     185.313|   2.1%/ 33|   1.8%/ 39|   1.7%/ 41|   1.6%/ 43 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 120   |     253|      47.073|   0.1%/757|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 103   |     254|      54.526|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 115   |    5271|      24.033|   1.7%/ 41|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 123   |     883|     209.357|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 113   |      22|       3.082|   1.5%/ 45|   1.3%/ 54|   1.2%/ 58|   1.1%/ 63 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 114   |   11803|     367.345|   1.8%/ 38|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 161   |    1369|      12.613|   0.7%/ 98|   0.6%/111|   0.6%/115|   0.6%/119 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 122   |    1581|      41.190|   0.7%/104|   0.6%/124|   0.5%/131|   0.5%/138 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 117   |    1651|     160.681|   0.4%/163|   0.5%/146|   0.5%/142|   0.5%/139 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 106   |     146|      53.221|   2.3%/ 31|   2.4%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 112   |    1870|      96.378|   1.1%/ 61|   1.2%/ 58|   1.2%/ 58|   1.2%/ 57 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 115   |   11183|      76.208|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  43   |       4|       0.323|   3.5%/ 19|   2.4%/ 29|   3.5%/ 20|   4.6%/ 15 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 110   |    2236|      65.332|   2.7%/ 26|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 102   |     153|       9.427|   2.6%/ 26|   2.1%/ 33|   2.0%/ 35|   1.8%/ 38 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 114   |     346|      49.676|   2.5%/ 28|   3.3%/ 21|   3.5%/ 19|   3.8%/ 18 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  80   |      64|       8.059|   0.6%/120|   0.3%/243|   0.2%/322|   0.1%/478 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 113   |      26|       4.559|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 106   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 120   |     112|      53.251|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  95   |      92|       5.813|   0.2%/437|   0.2%/421|   0.2%/422|   0.2%/426 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 107   |    3978|      67.682|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 131   |   28496|     605.005|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 106   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 121   |     655|      15.426|   1.0%/ 66|   0.9%/ 76|   0.9%/ 79|   0.9%/ 81 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 123   |    5556|     537.431|   0.4%/194|   0.3%/239|   0.3%/254|   0.3%/270 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 129   |    1968|     228.791|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 105   |      16|       0.917|  13.0%/  5|   0.0%/ --|   4.6%/ 15|   4.6%/ 15 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 103   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 133   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 107   |      15|       2.022|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 109   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 115   |      50|       4.266|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 117   |    5342|      64.246|   0.4%/189|   0.4%/196|   0.4%/197|   0.3%/199 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 134   |  134817|     409.102|   0.6%/126|   0.5%/128|   0.5%/129|   0.5%/130 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 121   |    1386|      33.101|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 114   |     331|      33.498|   0.5%/153|   0.4%/157|   0.4%/157|   0.4%/158 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 123   |   44938|     676.413|   0.2%/315|   0.2%/361|   0.2%/375|   0.2%/390 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 105   |      30|       8.471|   0.8%/ 87|   0.7%/104|   0.6%/110|   0.6%/117 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 107   |      53|       1.545|   7.4%/  9|   9.7%/  7|  10.2%/  7|  10.8%/  6 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 107   |      87|       2.702|   5.0%/ 14|   5.0%/ 14|   5.1%/ 14|   5.1%/ 14 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 101   |      45|       2.539|   5.8%/ 12|   4.6%/ 15|   4.4%/ 16|   4.1%/ 17 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 111   |      10|       0.642|   4.6%/ 15|   0.0%/ --|  13.0%/  5|  26.0%/  3 |

