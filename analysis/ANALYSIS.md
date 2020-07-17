# State and Country COVID-19 Analysis #
## Updated: at 2020-07-17 for data as of 2020-07-16 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.9% of deaths and 38.9% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.5% of deaths and 57.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 125   |   32607|    1676.162|   0.1%/863|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 129   |   15860|    1785.627|   0.3%/275|   0.3%/274|   0.3%/274|   0.3%/274 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 119   |    8396|    1208.183|   0.2%/314|   0.2%/358|   0.2%/371|   0.2%/386 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 135   |    7415|     187.657|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 122   |    7506|     592.371|   0.4%/167|   0.4%/179|   0.4%/183|   0.4%/188 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 120   |    6987|     545.762|   0.3%/238|   0.3%/258|   0.3%/263|   0.3%/268 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 120   |    6348|     635.682|   0.2%/424|   0.2%/430|   0.2%/432|   0.2%/434 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 131   |    4500|     209.530|   1.8%/ 38|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 120   |    4377|    1227.788|   0.1%/698|   0.1%/674|   0.1%/662|   0.1%/648 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 122   |    3484|     120.140|   2.5%/ 28|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 139   |  138176|     419.294|   0.5%/132|   0.5%/135|   0.5%/136|   0.5%/137 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 122   |   76929|     363.884|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 128   |   45287|     681.675|   0.2%/369|   0.2%/426|   0.2%/442|   0.2%/459 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 120   |   37993|     300.157|   1.8%/ 37|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 147   |   35030|     581.527|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 153   |   30105|     448.826|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28441|     603.840|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 128   |   25577|      18.789|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 148   |   13541|     162.400|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 119   |   12708|     395.510|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.5%/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 114   |    1199|     244.442|   1.7%/ 41|   1.9%/ 37|   1.9%/ 35|   2.0%/ 34 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 114   |      18|      24.467|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 118   |    2436|     334.713|   2.7%/ 26|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 115   |     341|     113.114|   1.5%/ 47|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 135   |    7415|     187.657|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 125   |    1740|     302.215|   0.2%/296|   0.3%/272|   0.3%/265|   0.3%/258 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 120   |    4377|    1227.788|   0.1%/698|   0.1%/674|   0.1%/662|   0.1%/648 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 113   |     521|     535.014|   0.1%/476|   0.2%/450|   0.2%/445|   0.2%/440 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 131   |    4500|     209.530|   1.8%/ 38|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 127   |    3081|     290.173|   0.7%/104|   0.7%/ 97|   0.7%/ 95|   0.7%/ 93 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 108   |      22|      15.668|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 113   |     105|      58.763|   1.0%/ 71|   1.2%/ 57|   1.3%/ 54|   1.3%/ 51 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 122   |    7506|     592.371|   0.4%/167|   0.4%/179|   0.4%/183|   0.4%/188 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 123   |    2802|     416.157|   0.3%/203|   0.3%/226|   0.3%/232|   0.3%/239 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 114   |     769|     243.839|   0.6%/119|   0.7%/100|   0.7%/ 96|   0.8%/ 92 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 126   |     305|     104.847|   0.7%/106|   0.6%/113|   0.6%/115|   0.6%/116 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 123   |     648|     145.033|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 125   |    3473|     746.994|   0.5%/142|   0.5%/134|   0.5%/132|   0.5%/130 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 112   |     115|      85.678|   0.5%/130|   0.5%/131|   0.5%/132|   0.5%/133 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 120   |    3360|     555.715|   0.3%/231|   0.3%/267|   0.2%/278|   0.2%/290 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 119   |    8396|    1208.183|   0.2%/314|   0.2%/358|   0.2%/371|   0.2%/386 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 120   |    6348|     635.682|   0.2%/424|   0.2%/430|   0.2%/432|   0.2%/434 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 118   |    1565|     277.550|   0.3%/198|   0.3%/226|   0.3%/234|   0.3%/242 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 120   |    1303|     437.914|   1.3%/ 55|   1.3%/ 52|   1.3%/ 52|   1.4%/ 51 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 120   |    1124|     183.166|   0.6%/111|   0.6%/110|   0.6%/110|   0.6%/109 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 112   |      34|      31.538|   3.3%/ 21|   4.4%/ 15|   4.7%/ 14|   5.0%/ 14 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 111   |     293|     151.478|   0.4%/166|   0.3%/239|   0.3%/263|   0.2%/289 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 123   |     619|     201.040|   1.3%/ 52|   1.5%/ 45|   1.6%/ 43|   1.7%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 116   |     398|     292.869|   0.4%/187|   0.2%/311|   0.2%/371|   0.2%/458 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 129   |   15860|    1785.627|   0.3%/275|   0.3%/274|   0.3%/274|   0.3%/274 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 114   |     560|     267.287|   0.8%/ 92|   0.8%/ 88|   0.8%/ 87|   0.8%/ 86 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 125   |   32607|    1676.162|   0.1%/863|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 114   |    1584|     151.062|   1.0%/ 69|   1.1%/ 60|   1.2%/ 58|   1.2%/ 56 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 112   |      89|     116.750|   0.7%/ 96|   0.8%/ 85|   0.8%/ 82|   0.9%/ 80 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 119   |    3113|     266.284|   0.5%/136|   0.5%/148|   0.5%/152|   0.4%/156 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 120   |     434|     109.576|   0.8%/ 90|   0.8%/ 82|   0.9%/ 81|   0.9%/ 79 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 124   |     246|      58.409|   1.3%/ 55|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 120   |    6987|     545.762|   0.3%/238|   0.3%/258|   0.3%/263|   0.3%/268 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 118   |     170|      53.165|   0.8%/ 86|   1.0%/ 69|   1.1%/ 65|   1.1%/ 62 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 111   |     991|     935.841|   0.3%/255|   0.2%/359|   0.2%/396|   0.2%/440 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 123   |    1037|     201.450|   2.1%/ 33|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 128   |     113|     127.811|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 118   |     792|     115.919|   1.8%/ 39|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 122   |    3484|     120.140|   2.5%/ 28|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 139   |  138176|     419.294|   0.5%/132|   0.5%/135|   0.5%/136|   0.5%/137 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 117   |     232|      72.253|   2.0%/ 34|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 119   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 125   |    2031|     237.954|   0.7%/ 93|   0.6%/111|   0.6%/117|   0.6%/124 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 139   |    1441|     189.221|   0.4%/163|   0.4%/186|   0.4%/194|   0.3%/203 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 109   |      98|      54.568|   0.4%/182|   0.5%/148|   0.5%/141|   0.5%/134 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 119   |     832|     142.940|   0.4%/188|   0.3%/214|   0.3%/221|   0.3%/228 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  95   |      22|      38.240|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 117   |    1118|      34.708|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 128   |     107|      37.496|   3.2%/ 21|   2.9%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 127   |    1048|      24.363|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 110   |      29|       0.927|   3.1%/ 22|   4.2%/ 16|   1.3%/ 55|   2.5%/ 28 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 131   |    2100|      46.723|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 113   |     609|     205.978|   2.0%/ 35|   1.8%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 138   |     110|       4.276|   0.6%/122|   0.7%/ 93|   0.8%/ 88|   0.8%/ 83 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 127   |     711|      79.817|   0.1%/995|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 126   |     344|      34.161|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 29 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 123   |     119|      77.000|   2.0%/ 34|   1.7%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 121   |    2551|      15.145|   1.9%/ 36|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 108   |     489|      51.969|   1.3%/ 54|   1.2%/ 58|   1.2%/ 59|   1.1%/ 60 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 128   |    9799|     850.262|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 102   |      28|       2.357|   2.4%/ 28|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 110   |    2082|     181.523|   3.4%/ 20|   2.8%/ 24|   2.7%/ 26|   2.5%/ 27 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 118   |     236|      71.482|   1.6%/ 44|   1.7%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 108   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 122   |   76929|     363.884|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 128   |     291|      41.814|   1.6%/ 43|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 121   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  95   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 114   |     372|      14.011|   0.6%/121|   0.6%/107|   0.7%/105|   0.7%/103 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 130   |    8894|     234.063|   0.1%/467|   0.1%/593|   0.1%/635|   0.1%/685 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  55   |      53|       9.683|   1.0%/ 68|   0.1%/778|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  80   |      75|       4.618|   0.1%/613|   0.2%/370|   0.2%/333|   0.2%/304 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 117   |    7454|     390.135|   1.5%/ 46|   1.1%/ 64|   1.0%/ 70|   0.9%/ 78 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 128   |    4641|       3.310|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 117   |    6294|     127.416|   3.8%/ 18|   3.6%/ 19|   3.5%/ 19|   3.5%/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 120   |      39|       7.748|   4.2%/ 16|   9.7%/  7|  10.1%/  7|   7.3%/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 120   |     121|      29.654|   0.6%/109|   0.7%/ 98|   0.7%/ 96|   0.7%/ 94 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 121   |      87|       7.762|   0.1%/721|   0.1%/679|   0.1%/663|   0.1%/647 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 125   |     611|     104.898|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 122   |     939|      90.688|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 125   |    5223|     298.993|   0.8%/ 83|   0.8%/ 87|   0.8%/ 88|   0.8%/ 89 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 131   |    4248|      42.366|   2.1%/ 33|   1.7%/ 40|   1.6%/ 42|   1.5%/ 45 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 108   |     304|      46.904|   3.3%/ 21|   2.5%/ 27|   2.3%/ 30|   2.1%/ 32 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  86   |      53|      38.655|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 103   |     143|       1.448|   2.8%/ 25|   3.4%/ 20|   3.5%/ 19|   3.7%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 118   |     329|      59.515|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 153   |   30105|     448.826|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 119   |      47|      21.844|   0.5%/143|   0.1%/641|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 116   |       3|       1.400|   2.3%/ 29|   2.1%/ 33|   2.0%/ 35|   1.8%/ 38 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 104   |      15|       4.046|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 130   |    9098|     109.419|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 118   |     145|       4.798|   1.3%/ 53|   0.8%/ 88|   0.7%/105|   0.5%/130 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 128   |     194|      18.043|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 123   |    1411|      85.009|   3.7%/ 19|   3.5%/ 20|   3.5%/ 20|   3.4%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  93   |      39|       3.175|   1.2%/ 57|   1.2%/ 59|   1.2%/ 59|   1.2%/ 60 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  82   |      26|      16.379|   0.5%/129|   0.3%/260|   0.2%/341|   0.1%/498 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 103   |     148|      12.781|   2.1%/ 33|   2.1%/ 33|   2.1%/ 34|   2.0%/ 34 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 113   |     876|      95.600|   2.8%/ 25|   2.3%/ 30|   2.2%/ 32|   2.0%/ 34 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 124   |     598|      61.143|   0.1%/604|   0.1%/960|   0.1%/ ***|   0.1%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 128   |   25577|      18.789|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 128   |    3875|      14.520|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 148   |   13541|     162.400|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 135   |    3819|      97.598|   3.7%/ 19|   2.8%/ 25|   2.5%/ 27|   2.3%/ 30 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 128   |    1750|     355.556|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 118   |     375|      40.847|   1.2%/ 60|   1.4%/ 50|   1.5%/ 48|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 147   |   35030|     581.527|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 120   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 155   |     990|       7.856|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 112   |      10|       0.960|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 114   |     390|      20.876|   0.2%/342|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 113   |     208|       4.377|   2.5%/ 27|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 113   |     124|      69.254|   5.4%/ 13|   6.9%/ 10|   7.2%/  9|   7.6%/  9 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 104   |     403|      91.123|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 105   |     181|      27.679|   6.2%/ 11|   5.3%/ 13|   5.1%/ 13|   4.8%/ 14 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 105   |      31|      16.108|   0.3%/240|   0.5%/147|   0.5%/133|   0.6%/121 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 129   |      38|       5.536|   0.5%/128|   0.5%/143|   0.5%/147|   0.5%/152 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 104   |      53|      11.831|   3.0%/ 23|   3.8%/ 18|   3.9%/ 17|   4.1%/ 17 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 106   |      47|       6.850|   2.8%/ 25|   3.4%/ 20|   3.3%/ 21|   4.8%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 118   |      79|      28.386|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  61   |      41|       1.568|   2.8%/ 24|   4.8%/ 14|   5.5%/ 13|   6.2%/ 11 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 122   |     122|       3.721|   0.1%/ ***|   0.1%/800|   0.1%/744|   0.1%/695 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 110   |     122|       6.043|   0.3%/267|   0.1%/590|   0.1%/862|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 109   |     152|      37.288|   1.0%/ 70|   0.9%/ 81|   0.8%/ 85|   0.8%/ 89 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 120   |   37993|     300.157|   1.8%/ 37|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 121   |     678|     252.723|   1.2%/ 57|   1.1%/ 65|   1.0%/ 68|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 129   |     259|       7.228|   1.0%/ 69|   1.1%/ 61|   1.2%/ 60|   1.2%/ 58 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  53   |       9|       0.304|   2.8%/ 25|   0.4%/161|   0.0%/ --|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  62   |      39|       1.313|   1.5%/ 46|   1.2%/ 55|   1.2%/ 57|   1.2%/ 60 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 133   |    6163|     353.054|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 110   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 112   |      99|      15.329|   1.6%/ 44|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 114   |      69|       3.074|   0.1%/530|   0.2%/456|   0.2%/440|   0.2%/424 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 116   |     781|       3.787|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 117   |     410|     197.601|   1.7%/ 41|   1.3%/ 53|   1.2%/ 57|   1.1%/ 61 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 125   |     253|      47.220|   0.1%/766|   0.1%/841|   0.1%/853|   0.1%/863 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 108   |     292|      62.529|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 120   |    5581|      25.447|   1.4%/ 50|   1.1%/ 62|   1.1%/ 65|   1.0%/ 70 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 128   |    1017|     241.031|   2.8%/ 24|   2.8%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 118   |      26|       3.601|   2.7%/ 26|   2.8%/ 25|   2.8%/ 24|   2.9%/ 24 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 119   |   12708|     395.510|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.5%/ 48 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 166   |    1418|      13.066|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89|   0.8%/ 89 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 127   |    1614|      42.046|   0.5%/126|   0.5%/153|   0.4%/161|   0.4%/171 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 122   |    1684|     163.890|   0.4%/179|   0.4%/182|   0.4%/183|   0.4%/185 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 111   |     158|      57.415|   1.7%/ 40|   1.5%/ 47|   1.4%/ 50|   1.3%/ 53 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 117   |    1974|     101.748|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 120   |   12012|      81.853|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  48   |       4|       0.341|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 115   |    2438|      71.246|   2.2%/ 32|   1.8%/ 38|   1.7%/ 41|   1.6%/ 43 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 107   |     161|       9.917|   1.8%/ 37|   1.2%/ 59|   1.0%/ 70|   0.8%/ 85 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 119   |     433|      62.161|   3.0%/ 23|   3.6%/ 19|   3.8%/ 18|   3.9%/ 18 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  85   |      64|       8.119|   0.4%/184|   0.3%/244|   0.3%/264|   0.2%/285 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 118   |      26|       4.646|   0.3%/205|   0.5%/127|   0.6%/115|   0.7%/105 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 111   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 125   |     111|      53.167|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 100   |      93|       5.873|   0.2%/373|   0.2%/413|   0.2%/429|   0.2%/448 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 112   |    4691|      79.816|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28441|     603.840|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 111   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 126   |     676|      15.939|   0.8%/ 85|   0.7%/101|   0.7%/105|   0.6%/111 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 128   |    5609|     542.500|   0.3%/259|   0.2%/339|   0.2%/366|   0.2%/398 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 134   |    1969|     228.906|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 110   |      22|       1.257|   4.6%/ 15|   9.5%/  7|  11.2%/  6|   5.0%/ 14 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 108   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 138   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 112   |      15|       2.027|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 114   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 120   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 122   |    5440|      65.415|   0.4%/190|   0.4%/191|   0.4%/191|   0.4%/191 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 139   |  138176|     419.294|   0.5%/132|   0.5%/135|   0.5%/136|   0.5%/137 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 126   |    1479|      35.319|   1.4%/ 50|   1.3%/ 54|   1.2%/ 55|   1.2%/ 57 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 119   |     338|      34.139|   0.4%/177|   0.4%/196|   0.3%/202|   0.3%/209 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 128   |   45287|     681.675|   0.2%/369|   0.2%/426|   0.2%/442|   0.2%/459 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 110   |      32|       8.969|   1.0%/ 71|   1.0%/ 69|   1.0%/ 69|   1.0%/ 68 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 112   |      78|       2.280|   7.0%/ 10|   7.4%/  9|   7.5%/  9|   7.5%/  9 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 112   |     107|       3.321|   4.5%/ 15|   4.2%/ 16|   4.1%/ 17|   4.0%/ 17 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 106   |      48|       2.671|   3.0%/ 23|   1.1%/ 61|   0.6%/109|   0.1%/525 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 116   |      23|       1.505|   8.8%/  8|  11.0%/  6|  11.5%/  6|  12.1%/  6 |

