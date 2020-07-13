# State and Country COVID-19 Analysis #
## Updated: at 2020-07-13 for data as of 2020-07-12 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.7% of deaths and 38.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 70.9% of deaths and 52.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 121   |   32539|    1672.652|   0.1%/747|   0.1%/867|   0.1%/903|   0.1%/942 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 125   |   15898|    1789.851|   0.3%/251|   0.3%/237|   0.3%/233|   0.3%/228 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 115   |    8334|    1199.224|   0.3%/265|   0.2%/290|   0.2%/296|   0.2%/302 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 118   |    7383|     582.657|   0.5%/132|   0.6%/125|   0.6%/123|   0.6%/121 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 131   |    7027|     177.838|   1.3%/ 54|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 116   |    6916|     540.204|   0.3%/211|   0.3%/223|   0.3%/226|   0.3%/229 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 116   |    6307|     631.507|   0.2%/380|   0.2%/358|   0.2%/352|   0.2%/346 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 116   |    4359|    1222.628|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 127   |    4158|     193.578|   1.6%/ 44|   1.8%/ 39|   1.8%/ 38|   1.8%/ 37 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 121   |    3402|     731.727|   0.5%/145|   0.5%/135|   0.5%/132|   0.5%/129 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 135   |  135480|     411.112|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/132 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 118   |   72673|     343.753|   1.7%/ 42|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 124   |   45017|     677.609|   0.2%/327|   0.2%/378|   0.2%/394|   0.2%/410 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 116   |   35735|     282.317|   2.1%/ 34|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 143   |   34987|     580.801|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 149   |   30040|     447.854|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 132   |   28491|     604.903|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 124   |   23328|      17.138|   2.5%/ 28|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 144   |   12747|     152.889|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 115   |   11980|     372.859|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 110   |    1118|     228.081|   1.5%/ 47|   1.6%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 110   |      18|      24.276|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 114   |    2178|     299.201|   2.4%/ 28|   2.6%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 111   |     324|     107.464|   1.6%/ 44|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 131   |    7027|     177.838|   1.3%/ 54|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 121   |    1724|     299.292|   0.2%/325|   0.2%/329|   0.2%/329|   0.2%/327 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 116   |    4359|    1222.628|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 109   |     522|     535.636|   0.1%/492|   0.1%/489|   0.1%/487|   0.1%/484 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 127   |    4158|     193.578|   1.6%/ 44|   1.8%/ 39|   1.8%/ 38|   1.8%/ 37 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 123   |    2994|     281.975|   0.6%/119|   0.6%/122|   0.6%/123|   0.6%/123 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 104   |      19|      13.678|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 109   |     101|      56.257|   0.9%/ 81|   1.1%/ 61|   1.2%/ 57|   1.3%/ 54 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 118   |    7383|     582.657|   0.5%/132|   0.6%/125|   0.6%/123|   0.6%/121 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 119   |    2770|     411.437|   0.4%/181|   0.3%/199|   0.3%/204|   0.3%/209 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 110   |     749|     237.337|   0.5%/153|   0.5%/145|   0.5%/143|   0.5%/140 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 122   |     298|     102.409|   0.7%/102|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 119   |     627|     140.247|   0.8%/ 82|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 121   |    3402|     731.727|   0.5%/145|   0.5%/135|   0.5%/132|   0.5%/129 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 108   |     113|      83.743|   0.6%/118|   0.7%/ 98|   0.7%/ 94|   0.8%/ 91 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 116   |    3326|     550.187|   0.4%/197|   0.3%/220|   0.3%/226|   0.3%/232 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 115   |    8334|    1199.224|   0.3%/265|   0.2%/290|   0.2%/296|   0.2%/302 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 116   |    6307|     631.507|   0.2%/380|   0.2%/358|   0.2%/352|   0.2%/346 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 114   |    1548|     274.505|   0.4%/183|   0.3%/226|   0.3%/240|   0.3%/255 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 116   |    1236|     415.277|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 116   |    1096|     178.600|   0.6%/115|   0.6%/119|   0.6%/120|   0.6%/121 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 108   |      24|      22.718|   0.6%/119|   0.5%/152|   0.4%/162|   0.4%/174 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 107   |     290|     150.042|   0.4%/155|   0.1%/530|   0.1%/ ***|   0.0%/ -- |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 119   |     582|     188.799|   1.2%/ 56|   1.5%/ 46|   1.6%/ 44|   1.7%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 112   |     396|     290.896|   0.5%/130|   0.4%/185|   0.3%/206|   0.3%/232 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 125   |   15898|    1789.851|   0.3%/251|   0.3%/237|   0.3%/233|   0.3%/228 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 110   |     543|     258.926|   0.8%/ 90|   0.8%/ 82|   0.9%/ 80|   0.9%/ 78 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 121   |   32539|    1672.652|   0.1%/747|   0.1%/867|   0.1%/903|   0.1%/942 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 110   |    1517|     144.679|   0.8%/ 82|   0.8%/ 85|   0.8%/ 86|   0.8%/ 86 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 108   |      86|     112.834|   0.7%/ 94|   0.9%/ 74|   1.0%/ 70|   1.0%/ 66 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 115   |    3055|     261.356|   0.6%/115|   0.6%/114|   0.6%/114|   0.6%/113 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 116   |     419|     105.970|   0.7%/ 95|   0.8%/ 84|   0.9%/ 81|   0.9%/ 79 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 120   |     233|      55.221|   1.1%/ 64|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 116   |    6916|     540.204|   0.3%/211|   0.3%/223|   0.3%/226|   0.3%/229 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 114   |     162|      50.628|   0.6%/108|   0.8%/ 82|   0.9%/ 77|   1.0%/ 72 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 107   |     984|     929.037|   0.3%/215|   0.2%/342|   0.2%/401|   0.1%/485 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 119   |     950|     184.460|   2.1%/ 33|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 124   |     107|     121.263|   1.5%/ 45|   1.7%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 114   |     735|     107.506|   1.8%/ 39|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 118   |    3093|     106.665|   2.1%/ 32|   2.5%/ 27|   2.6%/ 26|   2.8%/ 25 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 135   |  135480|     411.112|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/132 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 113   |     211|      65.905|   1.8%/ 39|   2.1%/ 33|   2.2%/ 32|   2.3%/ 30 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 115   |      56|      89.748|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 121   |    1983|     232.344|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 135   |    1428|     187.506|   0.6%/108|   0.7%/101|   0.7%/ 99|   0.7%/ 97 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 105   |      96|      53.541|   0.3%/269|   0.2%/315|   0.2%/325|   0.2%/335 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 115   |     822|     141.241|   0.4%/163|   0.4%/195|   0.3%/203|   0.3%/212 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  91   |      21|      36.396|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 113   |    1031|      31.994|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 124   |      96|      33.568|   3.4%/ 20|   3.2%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 123   |    1012|      23.542|   0.9%/ 81|   0.8%/ 84|   0.8%/ 85|   0.8%/ 85 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 106   |      26|       0.826|   5.4%/ 13|   5.0%/ 14|   4.9%/ 14|   4.8%/ 14 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 127   |    1869|      41.600|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 109   |     567|     191.751|   2.2%/ 32|   2.0%/ 34|   2.0%/ 35|   2.0%/ 35 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 134   |     107|       4.173|   0.3%/235|   0.4%/193|   0.4%/184|   0.4%/176 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 123   |     710|      79.710|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 122   |     312|      30.991|   3.2%/ 22|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 119   |     112|      72.477|   2.1%/ 34|   1.3%/ 53|   1.1%/ 62|   0.9%/ 75 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 117   |    2392|      14.199|   2.2%/ 32|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 104   |     467|      49.623|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 124   |    9793|     849.801|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  98   |      26|       2.192|   0.0%/ --|   3.1%/ 22|   7.4%/  9|   4.2%/ 16 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 106   |    1863|     162.420|   4.0%/ 17|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 114   |     219|      66.483|   1.4%/ 48|   1.7%/ 42|   1.7%/ 40|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 104   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 118   |   72673|     343.753|   1.7%/ 42|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 124   |     272|      39.184|   1.4%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 117   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  91   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 110   |     357|      13.462|   0.8%/ 90|   1.0%/ 73|   1.0%/ 69|   1.1%/ 65 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 126   |    8857|     233.075|   0.2%/391|   0.1%/498|   0.1%/534|   0.1%/574 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  51   |      54|       9.768|   1.4%/ 49|   1.0%/ 69|   0.8%/ 87|   0.6%/120 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  76   |      74|       4.569|   0.0%/ ***|   0.1%/774|   0.1%/650|   0.1%/556 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 113   |    7167|     375.102|   1.9%/ 36|   1.4%/ 49|   1.3%/ 53|   1.2%/ 58 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 124   |    4641|       3.310|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 113   |    5465|     110.628|   4.1%/ 17|   3.9%/ 18|   3.9%/ 18|   3.8%/ 18 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 116   |      29|       5.677|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 116   |     117|      28.769|   0.7%/102|   0.9%/ 76|   1.0%/ 72|   1.0%/ 68 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 117   |      87|       7.724|   0.1%/719|   0.1%/673|   0.1%/658|   0.1%/641 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 121   |     610|     104.722|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 118   |     883|      85.243|   1.5%/ 45|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 121   |    5065|     289.980|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 127   |    3980|      39.691|   2.4%/ 29|   1.9%/ 36|   1.8%/ 38|   1.7%/ 41 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 104   |     279|      43.087|   3.9%/ 17|   2.8%/ 25|   2.5%/ 28|   2.2%/ 32 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  82   |      56|      41.251|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  99   |     126|       1.273|   2.3%/ 30|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 114   |     329|      59.597|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 149   |   30040|     447.854|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 115   |      48|      21.902|   0.9%/ 78|   0.4%/155|   0.3%/205|   0.2%/302 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 112   |       3|       1.302|   3.2%/ 21|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 100   |      15|       4.077|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 126   |    9080|     109.202|   0.1%/818|   0.1%/940|   0.1%/973|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 114   |     141|       4.664|   1.9%/ 36|   1.3%/ 51|   1.2%/ 57|   1.1%/ 64 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 124   |     193|      18.039|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 119   |    1234|      74.334|   3.9%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  89   |      37|       3.042|   1.4%/ 48|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  78   |      26|      16.257|   1.1%/ 64|   0.6%/113|   0.5%/132|   0.4%/154 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  99   |     136|      11.712|   2.5%/ 27|   3.1%/ 22|   3.2%/ 21|   3.4%/ 20 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 109   |     802|      87.568|   3.4%/ 20|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 120   |     596|      60.969|   0.2%/395|   0.2%/455|   0.1%/474|   0.1%/493 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 124   |   23328|      17.138|   2.5%/ 28|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 124   |    3605|      13.505|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 144   |   12747|     152.889|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 131   |    3465|      88.557|   4.4%/ 15|   3.4%/ 20|   3.2%/ 22|   2.9%/ 24 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 124   |    1748|     355.233|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 114   |     355|      38.619|   0.9%/ 76|   1.1%/ 63|   1.2%/ 60|   1.2%/ 58 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 143   |   34987|     580.801|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 116   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 151   |     990|       7.857|   0.1%/734|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 108   |      10|       0.958|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 110   |     293|      15.686|   0.8%/ 89|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 109   |     185|       3.888|   2.0%/ 34|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 109   |     103|      57.314|   4.2%/ 17|   5.7%/ 12|   6.1%/ 11|   6.5%/ 10 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 100   |     391|      88.383|   0.8%/ 85|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 101   |     147|      22.475|   7.2%/  9|   7.3%/  9|   7.3%/  9|   7.3%/  9 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 101   |      30|      15.733|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 125   |      37|       5.379|   0.5%/141|   0.4%/173|   0.4%/186|   0.3%/202 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 100   |      43|       9.661|   2.7%/ 25|   3.9%/ 18|   4.2%/ 16|   4.5%/ 15 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 102   |      42|       6.180|   5.0%/ 14|   3.3%/ 21|   2.8%/ 24|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 114   |      79|      28.422|   0.1%/726|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  57   |      36|       1.367|   5.9%/ 12|   1.7%/ 42|   0.6%/117|   0.0%/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 118   |     121|       3.705|   0.0%/ ***|   0.1%/858|   0.1%/775|   0.1%/705 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 106   |     122|       6.021|   0.4%/160|   0.4%/195|   0.3%/206|   0.3%/219 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 105   |     147|      36.021|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 116   |   35735|     282.317|   2.1%/ 34|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 117   |     651|     242.570|   1.5%/ 47|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 125   |     247|       6.897|   0.8%/ 89|   0.9%/ 79|   0.9%/ 78|   0.9%/ 76 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  49   |       9|       0.310|   5.3%/ 13|   2.9%/ 24|   2.1%/ 33|   1.3%/ 53 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  58   |      38|       1.254|   2.2%/ 32|   1.5%/ 45|   1.4%/ 49|   1.3%/ 53 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 129   |    6160|     352.870|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 106   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 108   |      94|      14.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 110   |      68|       3.058|   0.1%/893|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 112   |     732|       3.551|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 113   |     391|     188.138|   2.1%/ 34|   1.7%/ 40|   1.6%/ 42|   1.6%/ 44 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 121   |     253|      47.075|   0.1%/874|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 104   |     262|      56.099|   3.2%/ 21|   3.1%/ 23|   3.0%/ 23|   2.9%/ 23 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 116   |    5346|      24.373|   1.6%/ 42|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 124   |     909|     215.486|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 114   |      22|       3.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 115   |   11980|     372.859|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 162   |    1379|      12.705|   0.7%/102|   0.6%/116|   0.6%/120|   0.6%/124 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 123   |    1587|      41.358|   0.6%/109|   0.5%/133|   0.5%/140|   0.5%/148 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 118   |    1659|     161.428|   0.4%/166|   0.5%/152|   0.5%/149|   0.5%/147 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 107   |     149|      54.258|   2.2%/ 32|   2.3%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 113   |    1891|      97.428|   1.1%/ 62|   1.1%/ 61|   1.1%/ 61|   1.1%/ 60 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 116   |   11357|      77.395|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  44   |       4|       0.323|   0.0%/ --|   0.0%/ --|  10.1%/  7|  10.1%/  7 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 111   |    2282|      66.690|   2.6%/ 27|   2.3%/ 30|   2.3%/ 30|   2.2%/ 31 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 103   |     155|       9.549|   2.5%/ 28|   1.9%/ 37|   1.7%/ 40|   1.6%/ 44 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 115   |     370|      53.085|   2.7%/ 26|   3.5%/ 20|   3.7%/ 19|   3.9%/ 18 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  81   |      64|       8.058|   0.5%/141|   0.2%/327|   0.1%/489|   0.1%/989 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 114   |      26|       4.559|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 107   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 121   |     111|      53.243|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  96   |      93|       5.830|   0.2%/390|   0.2%/341|   0.2%/336|   0.2%/332 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 108   |    4116|      70.034|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 132   |   28491|     604.903|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 107   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 122   |     659|      15.522|   1.0%/ 71|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 124   |    5568|     538.599|   0.3%/209|   0.3%/267|   0.2%/286|   0.2%/309 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 130   |    1969|     228.816|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 106   |      17|       0.954|  11.9%/  6|   4.6%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 104   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 134   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 108   |      15|       2.026|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 110   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 116   |      50|       4.266|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 118   |    5361|      64.476|   0.4%/188|   0.4%/192|   0.4%/193|   0.4%/194 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 135   |  135480|     411.112|   0.5%/127|   0.5%/131|   0.5%/132|   0.5%/132 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 122   |    1406|      33.578|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 115   |     333|      33.654|   0.5%/152|   0.5%/153|   0.5%/154|   0.5%/154 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 124   |   45017|     677.609|   0.2%/327|   0.2%/378|   0.2%/394|   0.2%/410 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 106   |      30|       8.590|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78|   0.9%/ 78 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 108   |      57|       1.683|   7.7%/  9|   9.7%/  7|  10.2%/  7|  10.7%/  6 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 108   |      91|       2.823|   4.9%/ 14|   4.8%/ 14|   4.8%/ 14|   4.7%/ 14 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 102   |      46|       2.593|   5.1%/ 13|   3.7%/ 19|   3.4%/ 20|   3.0%/ 23 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 112   |      10|       0.664|   8.4%/  8|  11.7%/  6|  12.7%/  5|  13.6%/  5 |

