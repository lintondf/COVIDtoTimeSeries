# State and Country COVID-19 Analysis #
## Updated: at 2020-07-21 for data as of 2020-07-20 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.1% of deaths and 39.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.2% of deaths and 57.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 129   |   32621|    1676.880|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 133   |   15831|    1782.359|   0.2%/336|   0.2%/383|   0.2%/399|   0.2%/416 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 123   |    8457|    1216.960|   0.2%/338|   0.2%/378|   0.2%/390|   0.2%/403 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 139   |    7827|     198.098|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 126   |    7582|     598.344|   0.3%/213|   0.3%/274|   0.2%/298|   0.2%/327 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 124   |    7053|     550.932|   0.3%/267|   0.2%/299|   0.2%/308|   0.2%/318 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 124   |    6385|     639.294|   0.2%/461|   0.1%/492|   0.1%/501|   0.1%/511 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 135   |    4968|     231.306|   2.1%/ 33|   2.3%/ 30|   2.4%/ 29|   2.5%/ 28 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 124   |    4400|    1234.044|   0.1%/652|   0.1%/590|   0.1%/574|   0.1%/559 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 126   |    4013|     138.401|   3.0%/ 23|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 143   |  141170|     428.381|   0.5%/130|   0.5%/131|   0.5%/131|   0.5%/131 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 126   |   81229|     384.220|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 132   |   45542|     685.512|   0.2%/423|   0.1%/496|   0.1%/518|   0.1%/541 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 124   |   40330|     318.620|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 151   |   35076|     582.289|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 157   |   30179|     449.919|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 140   |   28432|     603.642|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 132   |   28153|      20.682|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 152   |   14369|     172.336|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 123   |   13431|     417.987|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 118   |    1300|     265.138|   1.8%/ 39|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 118   |      18|      24.884|   0.7%/ 93|   0.8%/ 85|   0.8%/ 83|   0.9%/ 81 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 122   |    2774|     381.097|   3.0%/ 23|   3.3%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 119   |     364|     120.523|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 139   |    7827|     198.098|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 129   |    1757|     305.154|   0.2%/317|   0.2%/303|   0.2%/300|   0.2%/297 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 124   |    4400|    1234.044|   0.1%/652|   0.1%/590|   0.1%/574|   0.1%/559 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 117   |     524|     537.724|   0.1%/473|   0.1%/467|   0.1%/465|   0.1%/463 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 135   |    4968|     231.306|   2.1%/ 33|   2.3%/ 30|   2.4%/ 29|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 131   |    3180|     299.467|   0.7%/ 98|   0.8%/ 91|   0.8%/ 89|   0.8%/ 87 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 112   |      24|      16.996|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 117   |     120|      66.873|   1.3%/ 54|   1.5%/ 45|   1.6%/ 43|   1.7%/ 41 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 126   |    7582|     598.344|   0.3%/213|   0.3%/274|   0.2%/298|   0.2%/327 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 127   |    2835|     421.107|   0.3%/210|   0.3%/227|   0.3%/232|   0.3%/237 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 118   |     794|     251.791|   0.6%/107|   0.7%/ 93|   0.8%/ 90|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 130   |     312|     107.216|   0.6%/113|   0.6%/122|   0.6%/124|   0.6%/126 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 127   |     673|     150.637|   0.9%/ 77|   0.9%/ 74|   0.9%/ 73|   1.0%/ 73 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 129   |    3539|     761.350|   0.5%/144|   0.5%/140|   0.5%/140|   0.5%/139 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 116   |     118|      87.516|   0.6%/121|   0.6%/121|   0.6%/122|   0.6%/122 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 124   |    3392|     561.036|   0.3%/250|   0.2%/280|   0.2%/289|   0.2%/298 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 123   |    8457|    1216.960|   0.2%/338|   0.2%/378|   0.2%/390|   0.2%/403 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 124   |    6385|     639.294|   0.2%/461|   0.1%/492|   0.1%/501|   0.1%/511 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 122   |    1587|     281.328|   0.4%/198|   0.3%/208|   0.3%/210|   0.3%/212 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 124   |    1374|     461.574|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 124   |    1147|     186.887|   0.6%/126|   0.5%/135|   0.5%/137|   0.5%/140 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 116   |      39|      36.476|   2.2%/ 32|   2.6%/ 26|   2.8%/ 25|   2.9%/ 24 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 115   |     303|     156.485|   0.6%/109|   0.7%/ 93|   0.8%/ 89|   0.8%/ 85 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 127   |     656|     212.970|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 120   |     401|     294.637|   0.3%/236|   0.2%/357|   0.2%/407|   0.1%/472 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 133   |   15831|    1782.359|   0.2%/336|   0.2%/383|   0.2%/399|   0.2%/416 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 118   |     578|     275.536|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 129   |   32621|    1676.880|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 118   |    1665|     158.774|   1.1%/ 64|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 116   |      92|     121.077|   0.8%/ 84|   0.9%/ 77|   0.9%/ 76|   0.9%/ 74 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 123   |    3179|     271.964|   0.6%/125|   0.6%/124|   0.6%/124|   0.6%/124 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 124   |     452|     114.129|   0.9%/ 78|   1.0%/ 70|   1.0%/ 69|   1.0%/ 67 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 128   |     261|      61.969|   1.3%/ 52|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 124   |    7053|     550.932|   0.3%/267|   0.2%/299|   0.2%/308|   0.2%/318 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 122   |     179|      55.967|   1.0%/ 70|   1.2%/ 58|   1.2%/ 56|   1.3%/ 54 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 115   |     997|     940.793|   0.2%/341|   0.1%/489|   0.1%/545|   0.1%/614 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 127   |    1159|     225.113|   2.4%/ 28|   2.6%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 132   |     119|     134.766|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57|   1.2%/ 57 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 122   |     856|     125.252|   1.8%/ 38|   1.9%/ 36|   1.9%/ 36|   2.0%/ 35 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 126   |    4013|     138.401|   3.0%/ 23|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 143   |  141170|     428.381|   0.5%/130|   0.5%/131|   0.5%/131|   0.5%/131 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 121   |     250|      78.029|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 123   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 129   |    2066|     242.017|   0.6%/116|   0.4%/155|   0.4%/169|   0.4%/187 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 143   |    1460|     191.685|   0.5%/145|   0.5%/154|   0.4%/156|   0.4%/159 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 113   |     100|      55.880|   0.4%/154|   0.5%/132|   0.5%/128|   0.6%/123 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 123   |     846|     145.215|   0.4%/170|   0.4%/168|   0.4%/167|   0.4%/166 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  99   |      24|      42.007|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 121   |    1215|      37.709|   2.2%/ 31|   2.1%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 132   |     118|      41.515|   2.9%/ 23|   2.6%/ 26|   2.5%/ 27|   2.5%/ 28 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 131   |    1086|      25.253|   0.9%/ 78|   0.9%/ 77|   0.9%/ 77|   0.9%/ 76 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 114   |      32|       1.013|   3.1%/ 23|   1.7%/ 41|   1.3%/ 52|   1.0%/ 69 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 135   |    2358|      52.478|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 117   |     656|     221.861|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37|   1.8%/ 37 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 142   |     113|       4.384|   1.3%/ 54|   1.7%/ 41|   1.8%/ 39|   1.9%/ 36 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 131   |     712|      79.943|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 130   |     374|      37.125|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 127   |     128|      83.138|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 44 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 125   |    2705|      16.059|   1.7%/ 40|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 112   |     509|      54.104|   1.2%/ 60|   1.0%/ 68|   1.0%/ 70|   0.9%/ 73 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 132   |    9807|     850.940|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 106   |      32|       2.689|   0.0%/ --|   6.0%/ 11|   3.5%/ 20|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 114   |    2276|     198.453|   3.0%/ 23|   2.5%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 122   |     254|      76.926|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 112   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 126   |   81229|     384.220|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 132   |     308|      44.375|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 125   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  99   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 118   |     383|      14.420|   0.6%/122|   0.6%/119|   0.6%/119|   0.6%/119 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 134   |    8928|     234.945|   0.1%/550|   0.1%/706|   0.1%/759|   0.1%/821 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  59   |      55|       9.974|   0.3%/214|   0.7%/ 93|   0.9%/ 80|   1.0%/ 69 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  84   |      75|       4.632|   0.1%/770|   0.1%/970|   0.1%/ ***|   0.1%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 121   |    8355|     437.266|   1.3%/ 52|   1.1%/ 63|   1.0%/ 67|   1.0%/ 71 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 132   |    4644|       3.312|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 121   |    7103|     143.797|   3.5%/ 20|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 124   |      57|      11.219|   9.1%/  7|  10.5%/  6|  10.8%/  6|  11.2%/  6 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 124   |     123|      30.102|   0.5%/152|   0.4%/178|   0.4%/189|   0.3%/201 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 125   |      87|       7.779|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 129   |     612|     105.054|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 126   |     995|      96.100|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 129   |    5372|     307.504|   0.8%/ 91|   0.7%/ 99|   0.7%/101|   0.7%/104 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 135   |    4490|      44.777|   1.8%/ 39|   1.4%/ 48|   1.4%/ 51|   1.3%/ 54 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 112   |     342|      52.783|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  90   |      51|      37.607|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 107   |     167|       1.696|   3.3%/ 21|   4.0%/ 17|   4.2%/ 16|   4.3%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 122   |     328|      59.395|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 157   |   30179|     449.919|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 123   |      47|      21.652|   0.2%/320|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 120   |       4|       1.632|   4.1%/ 17|   4.8%/ 14|   4.9%/ 14|   5.1%/ 13 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 108   |      15|       4.070|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 134   |    9110|     109.558|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 122   |     151|       5.002|   1.4%/ 51|   1.2%/ 60|   1.1%/ 62|   1.1%/ 64 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 132   |     194|      18.108|   0.1%/848|   0.1%/794|   0.1%/778|   0.1%/760 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 127   |    1578|      95.045|   3.2%/ 22|   2.8%/ 25|   2.7%/ 26|   2.6%/ 26 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  97   |      40|       3.286|   1.0%/ 69|   0.9%/ 80|   0.8%/ 84|   0.8%/ 88 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  86   |      26|      16.351|   0.3%/252|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 107   |     154|      13.306|   1.5%/ 46|   1.1%/ 65|   0.9%/ 74|   0.8%/ 87 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 117   |     946|     103.304|   2.6%/ 27|   2.2%/ 31|   2.1%/ 32|   2.0%/ 34 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 128   |     598|      61.207|   0.1%/889|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 132   |   28153|      20.682|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 132   |    4192|      15.705|   1.9%/ 35|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 152   |   14369|     172.336|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 139   |    4139|     105.792|   3.0%/ 23|   2.3%/ 31|   2.1%/ 33|   1.9%/ 37 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 132   |    1753|     356.263|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 122   |     404|      44.012|   1.5%/ 45|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 151   |   35076|     582.289|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 124   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 159   |     990|       7.858|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 116   |      11|       1.003|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 118   |     431|      23.069|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 117   |     236|       4.955|   2.7%/ 26|   3.0%/ 23|   3.0%/ 23|   3.1%/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 117   |     145|      80.751|   4.4%/ 16|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 108   |     413|      93.363|   0.7%/ 99|   0.6%/113|   0.6%/117|   0.6%/122 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 109   |     222|      33.973|   5.2%/ 13|   3.9%/ 17|   3.6%/ 19|   3.3%/ 21 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 109   |      31|      16.319|   0.2%/306|   0.3%/249|   0.3%/240|   0.3%/232 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 133   |      40|       5.860|   0.8%/ 86|   0.9%/ 79|   0.9%/ 77|   0.9%/ 75 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 108   |      67|      15.000|   2.2%/ 32|   2.0%/ 35|   1.9%/ 37|   1.8%/ 39 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 110   |      52|       7.500|   3.4%/ 20|   3.7%/ 18|   1.4%/ 48|   1.4%/ 49 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 122   |      80|      28.526|   0.1%/525|   0.2%/437|   0.2%/415|   0.2%/394 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  65   |      63|       2.385|   4.8%/ 14|   6.8%/ 10|   7.3%/  9|   7.8%/  9 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 126   |     122|       3.740|   0.1%/711|   0.1%/528|   0.1%/496|   0.1%/468 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 114   |     122|       6.029|   0.1%/536|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 113   |     157|      38.523|   1.0%/ 73|   0.9%/ 81|   0.8%/ 84|   0.8%/ 87 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 124   |   40330|     318.620|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 125   |     702|     261.920|   1.1%/ 63|   0.9%/ 74|   0.9%/ 78|   0.9%/ 81 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 133   |     272|       7.592|   1.1%/ 62|   1.2%/ 56|   1.3%/ 55|   1.3%/ 53 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  57   |      10|       0.340|   0.8%/ 82|   2.9%/ 24|   3.6%/ 19|   4.3%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  11   |       4|       1.627|  26.0%/  2|   0.0%/ --|  14.5%/  5|  26.0%/  2 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  66   |      41|       1.356|   1.3%/ 53|   0.8%/ 85|   0.7%/103|   0.5%/132 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 137   |    6163|     353.053|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 114   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 116   |     102|      15.804|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 118   |      69|       3.094|   0.1%/549|   0.1%/524|   0.1%/514|   0.1%/503 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 120   |     816|       3.958|   1.4%/ 51|   1.2%/ 60|   1.1%/ 63|   1.0%/ 66 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 121   |     432|     208.062|   1.6%/ 43|   1.4%/ 49|   1.4%/ 51|   1.3%/ 53 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 129   |     255|      47.489|   0.1%/592|   0.1%/536|   0.1%/522|   0.1%/507 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 112   |     327|      70.074|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 124   |    5771|      26.312|   1.1%/ 61|   0.9%/ 78|   0.8%/ 84|   0.8%/ 91 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 132   |    1134|     268.905|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 122   |      30|       4.251|   3.6%/ 19|   4.3%/ 16|   4.4%/ 15|   4.6%/ 15 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 123   |   13431|     417.987|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 170   |    1740|      16.034|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   1.0%/ 73 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 131   |    1639|      42.711|   0.5%/144|   0.4%/172|   0.4%/181|   0.4%/190 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 126   |    1702|     165.632|   0.3%/220|   0.3%/260|   0.3%/273|   0.2%/289 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 115   |     163|      59.292|   1.4%/ 51|   1.0%/ 71|   0.9%/ 79|   0.8%/ 90 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 121   |    2054|     105.825|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 124   |   12623|      86.023|   1.4%/ 51|   1.2%/ 56|   1.2%/ 57|   1.2%/ 59 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  52   |       5|       0.404|   4.2%/ 16|   4.9%/ 14|   5.4%/ 13|   6.0%/ 11 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 119   |    2580|      75.384|   1.9%/ 36|   1.5%/ 45|   1.5%/ 47|   1.4%/ 50 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 111   |     170|      10.469|   1.8%/ 39|   1.5%/ 47|   1.4%/ 49|   1.3%/ 52 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 123   |     490|      70.295|   2.8%/ 25|   3.0%/ 23|   3.1%/ 23|   3.1%/ 22 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  89   |      65|       8.275|   0.4%/175|   0.4%/158|   0.5%/153|   0.5%/146 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 122   |      27|       4.730|   0.3%/270|   0.3%/203|   0.4%/191|   0.4%/181 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 115   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 129   |     112|      53.297|   0.1%/ ***|   0.1%/877|   0.1%/823|   0.1%/769 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 104   |      93|       5.880|   0.1%/628|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 116   |    5297|      90.120|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 140   |   28432|     603.642|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 115   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 130   |     694|      16.359|   0.8%/ 88|   0.7%/ 96|   0.7%/ 99|   0.7%/101 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 132   |    5655|     546.970|   0.2%/283|   0.2%/343|   0.2%/361|   0.2%/380 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 138   |    1970|     229.010|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 114   |      28|       1.607|   9.5%/  7|   4.4%/ 16|   4.4%/ 16|   5.1%/ 14 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 112   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 142   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 116   |      15|       2.016|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 118   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 124   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 126   |    5515|      66.327|   0.4%/197|   0.3%/200|   0.3%/201|   0.3%/202 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 143   |  141170|     428.381|   0.5%/130|   0.5%/131|   0.5%/131|   0.5%/131 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 130   |    1543|      36.836|   1.2%/ 57|   1.1%/ 64|   1.1%/ 66|   1.0%/ 68 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 123   |     341|      34.527|   0.3%/199|   0.3%/230|   0.3%/239|   0.3%/250 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 132   |   45542|     685.512|   0.2%/423|   0.1%/496|   0.1%/518|   0.1%/541 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 114   |      33|       9.409|   1.1%/ 63|   1.2%/ 57|   1.2%/ 56|   1.3%/ 55 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 116   |      98|       2.861|   6.2%/ 11|   5.8%/ 12|   5.6%/ 12|   5.5%/ 13 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 116   |     122|       3.781|   3.9%/ 18|   3.3%/ 21|   3.2%/ 22|   3.0%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 110   |     127|       7.089|  15.2%/  4|  17.5%/  4|  18.1%/  4|  18.6%/  4 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 120   |      29|       1.905|   8.0%/  9|   8.4%/  8|   8.4%/  8|   8.4%/  8 |

