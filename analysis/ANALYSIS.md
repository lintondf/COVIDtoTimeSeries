# State and Country COVID-19 Analysis #
## Updated: at 2020-07-20 for data as of 2020-07-19 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.0% of deaths and 39.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.2% of deaths and 57.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 128   |   32624|    1677.016|   0.1%/983|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 132   |   15851|    1784.559|   0.2%/310|   0.2%/336|   0.2%/344|   0.2%/352 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 122   |    8445|    1215.154|   0.2%/322|   0.2%/352|   0.2%/361|   0.2%/370 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 138   |    7734|     195.747|   1.3%/ 52|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 125   |    7569|     597.291|   0.4%/198|   0.3%/238|   0.3%/252|   0.3%/270 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 123   |    7040|     549.923|   0.3%/247|   0.3%/264|   0.3%/269|   0.3%/273 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 123   |    6377|     638.499|   0.2%/442|   0.2%/459|   0.1%/464|   0.1%/470 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 134   |    4846|     225.610|   2.1%/ 33|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 123   |    4394|    1232.445|   0.1%/645|   0.1%/584|   0.1%/567|   0.1%/550 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 125   |    3868|     133.386|   3.0%/ 23|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 142   |  140484|     426.299|   0.5%/127|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 125   |   80256|     379.619|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 131   |   45486|     684.661|   0.2%/393|   0.2%/445|   0.2%/460|   0.1%/475 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 123   |   39779|     314.264|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 150   |   35066|     582.113|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 156   |   30161|     449.661|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 139   |   28430|     603.606|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 131   |   27501|      20.203|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 151   |   14160|     169.830|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 122   |   13274|     413.126|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 117   |    1279|     260.819|   1.8%/ 37|   2.1%/ 33|   2.1%/ 32|   2.2%/ 31 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 117   |      18|      24.777|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 121   |    2690|     369.512|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 118   |     358|     118.787|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 138   |    7734|     195.747|   1.3%/ 52|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 128   |    1753|     304.436|   0.2%/308|   0.2%/290|   0.2%/285|   0.2%/280 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 123   |    4394|    1232.445|   0.1%/645|   0.1%/584|   0.1%/567|   0.1%/550 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 116   |     523|     537.093|   0.1%/467|   0.2%/454|   0.2%/451|   0.2%/448 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 134   |    4846|     225.610|   2.1%/ 33|   2.4%/ 29|   2.4%/ 28|   2.5%/ 27 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 130   |    3158|     297.403|   0.7%/ 96|   0.8%/ 87|   0.8%/ 85|   0.8%/ 83 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 111   |      24|      16.763|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 116   |     109|      60.803|   1.4%/ 48|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 125   |    7569|     597.291|   0.4%/198|   0.3%/238|   0.3%/252|   0.3%/270 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 126   |    2828|     420.049|   0.3%/204|   0.3%/219|   0.3%/223|   0.3%/227 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 117   |     788|     249.818|   0.6%/107|   0.8%/ 91|   0.8%/ 88|   0.8%/ 85 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 129   |     311|     106.600|   0.6%/113|   0.6%/122|   0.6%/125|   0.5%/128 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 126   |     667|     149.395|   0.9%/ 75|   1.0%/ 71|   1.0%/ 70|   1.0%/ 69 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 128   |    3530|     759.358|   0.5%/136|   0.5%/128|   0.5%/126|   0.6%/124 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 115   |     117|      87.140|   0.6%/121|   0.6%/120|   0.6%/120|   0.6%/120 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 123   |    3384|     559.705|   0.3%/243|   0.3%/273|   0.2%/281|   0.2%/290 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 122   |    8445|    1215.154|   0.2%/322|   0.2%/352|   0.2%/361|   0.2%/370 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 123   |    6377|     638.499|   0.2%/442|   0.2%/459|   0.1%/464|   0.1%/470 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 121   |    1582|     280.464|   0.4%/192|   0.3%/200|   0.3%/202|   0.3%/203 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 123   |    1359|     456.688|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 123   |    1142|     186.095|   0.6%/121|   0.5%/127|   0.5%/129|   0.5%/130 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 115   |      38|      35.374|   2.4%/ 29|   3.0%/ 23|   3.1%/ 22|   3.3%/ 21 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 114   |     299|     154.610|   0.6%/124|   0.6%/113|   0.6%/109|   0.7%/104 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 126   |     648|     210.473|   1.4%/ 51|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 119   |     400|     294.039|   0.3%/227|   0.2%/363|   0.2%/424|   0.1%/509 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 132   |   15851|    1784.559|   0.2%/310|   0.2%/336|   0.2%/344|   0.2%/352 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 117   |     573|     273.369|   0.7%/ 93|   0.8%/ 92|   0.8%/ 91|   0.8%/ 91 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 128   |   32624|    1677.016|   0.1%/983|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 117   |    1644|     156.780|   1.1%/ 65|   1.2%/ 58|   1.2%/ 56|   1.3%/ 55 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 115   |      91|     119.903|   0.8%/ 88|   0.9%/ 80|   0.9%/ 79|   0.9%/ 78 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 122   |    3160|     270.352|   0.5%/131|   0.5%/135|   0.5%/136|   0.5%/137 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 123   |     448|     113.173|   0.9%/ 76|   1.0%/ 67|   1.1%/ 65|   1.1%/ 63 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 127   |     258|      61.166|   1.3%/ 52|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 123   |    7040|     549.923|   0.3%/247|   0.3%/264|   0.3%/269|   0.3%/273 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 121   |     177|      55.286|   1.0%/ 69|   1.2%/ 56|   1.3%/ 53|   1.4%/ 51 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 114   |     995|     939.386|   0.2%/325|   0.1%/474|   0.1%/532|   0.1%/604 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 126   |    1130|     219.437|   2.5%/ 28|   2.7%/ 25|   2.8%/ 25|   2.9%/ 24 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 131   |     118|     133.260|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 121   |     842|     123.165|   1.9%/ 37|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 125   |    3868|     133.386|   3.0%/ 23|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 142   |  140484|     426.299|   0.5%/127|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 120   |     246|      76.660|   1.9%/ 36|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 122   |      56|      89.745|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 128   |    2059|     241.270|   0.6%/108|   0.5%/137|   0.5%/148|   0.4%/160 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 142   |    1455|     191.071|   0.5%/144|   0.5%/152|   0.4%/154|   0.4%/157 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 112   |     100|      55.623|   0.5%/144|   0.6%/116|   0.6%/110|   0.7%/105 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 122   |     842|     144.654|   0.4%/175|   0.4%/176|   0.4%/176|   0.4%/176 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  98   |      24|      41.454|   0.8%/ 90|   1.1%/ 61|   1.2%/ 56|   1.3%/ 52 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 120   |    1195|      37.071|   2.3%/ 29|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 131   |     115|      40.537|   3.1%/ 22|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 130   |    1076|      25.025|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 113   |      31|       0.996|   3.5%/ 20|   2.3%/ 31|   1.9%/ 36|   1.6%/ 42 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 134   |    2288|      50.914|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 116   |     645|     218.024|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 141   |     112|       4.354|   1.1%/ 62|   1.5%/ 47|   1.6%/ 44|   1.7%/ 41 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 130   |     712|      79.923|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 129   |     367|      36.415|   2.6%/ 27|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 126   |     126|      81.698|   2.0%/ 34|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 124   |    2667|      15.833|   1.8%/ 39|   1.6%/ 44|   1.5%/ 46|   1.5%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 111   |     504|      53.593|   1.2%/ 58|   1.1%/ 64|   1.1%/ 66|   1.0%/ 67 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 131   |    9804|     850.729|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 105   |      31|       2.624|   4.2%/ 16|   6.0%/ 11|   6.0%/ 11|   3.5%/ 20 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 113   |    2228|     194.277|   3.1%/ 22|   2.5%/ 27|   2.4%/ 29|   2.2%/ 31 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 121   |     249|      75.525|   1.7%/ 42|   1.8%/ 38|   1.8%/ 38|   1.9%/ 37 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 111   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 125   |   80256|     379.619|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 131   |     304|      43.720|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 124   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  98   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 117   |     381|      14.357|   0.7%/105|   0.7%/ 96|   0.7%/ 95|   0.7%/ 93 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 133   |    8921|     234.770|   0.1%/515|   0.1%/643|   0.1%/686|   0.1%/734 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  58   |      54|       9.895|   0.3%/250|   0.5%/126|   0.6%/108|   0.7%/ 92 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  83   |      75|       4.631|   0.1%/714|   0.1%/702|   0.1%/722|   0.1%/757 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 120   |    8153|     426.713|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.5%/ 48 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 131   |    4643|       3.311|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 120   |    6901|     139.712|   3.5%/ 20|   3.2%/ 21|   3.1%/ 22|   3.1%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 123   |      51|      10.157|   8.1%/  8|   9.7%/  7|  10.1%/  7|  10.5%/  6 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 123   |     122|      29.974|   0.5%/152|   0.4%/176|   0.4%/186|   0.4%/198 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 124   |      87|       7.776|   0.1%/991|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 128   |     612|     105.028|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 125   |     981|      94.719|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 128   |    5340|     305.723|   0.8%/ 86|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 134   |    4436|      44.238|   1.9%/ 37|   1.5%/ 45|   1.4%/ 48|   1.4%/ 51 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 111   |     331|      51.059|   3.3%/ 21|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  89   |      51|      37.753|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 106   |     161|       1.630|   3.1%/ 22|   3.8%/ 18|   4.0%/ 17|   4.2%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 121   |     328|      59.423|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 156   |   30161|     449.661|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 122   |      47|      21.717|   0.3%/256|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 119   |       4|       1.569|   3.5%/ 20|   3.9%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 107   |      15|       4.031|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 133   |    9108|     109.534|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 121   |     149|       4.934|   1.3%/ 53|   1.0%/ 68|   0.9%/ 73|   0.9%/ 79 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 131   |     194|      18.082|   0.1%/966|   0.1%/976|   0.1%/975|   0.1%/971 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 126   |    1542|      92.872|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  96   |      40|       3.254|   1.0%/ 68|   0.9%/ 78|   0.8%/ 81|   0.8%/ 86 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  85   |      26|      16.371|   0.3%/213|   0.1%/842|   0.0%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 106   |     153|      13.241|   1.7%/ 41|   1.4%/ 51|   1.2%/ 55|   1.1%/ 61 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 116   |     927|     101.234|   2.6%/ 27|   2.1%/ 32|   2.0%/ 34|   1.9%/ 36 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 127   |     598|      61.185|   0.1%/825|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 131   |   27501|      20.203|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 131   |    4105|      15.381|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 151   |   14160|     169.830|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 138   |    4067|     103.953|   3.2%/ 22|   2.4%/ 29|   2.2%/ 32|   2.0%/ 35 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 131   |    1753|     356.091|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 121   |     396|      43.109|   1.5%/ 47|   1.8%/ 39|   1.8%/ 37|   1.9%/ 36 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 150   |   35066|     582.113|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 123   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 158   |     990|       7.857|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 115   |      10|       0.961|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 117   |     413|      22.101|   0.1%/502|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 116   |     229|       4.807|   2.7%/ 26|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 116   |     140|      77.860|   4.6%/ 15|   5.4%/ 13|   5.6%/ 12|   5.8%/ 12 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 107   |     411|      92.920|   0.7%/ 93|   0.7%/101|   0.7%/104|   0.7%/106 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 108   |     211|      32.274|   5.5%/ 12|   4.4%/ 16|   4.1%/ 17|   3.8%/ 18 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 108   |      31|      16.279|   0.2%/284|   0.3%/214|   0.3%/201|   0.4%/191 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 132   |      39|       5.775|   0.8%/ 86|   0.9%/ 78|   0.9%/ 76|   0.9%/ 74 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 107   |      59|      13.097|   6.6%/ 10|   9.1%/  7|   9.7%/  7|  10.4%/  7 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 109   |      51|       7.375|   1.7%/ 40|   3.8%/ 18|   3.7%/ 18|   1.4%/ 48 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 121   |      80|      28.482|   0.1%/693|   0.1%/671|   0.1%/660|   0.1%/645 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  64   |      58|       2.217|   4.5%/ 15|   8.7%/  8|   9.8%/  7|  10.9%/  6 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 125   |     122|       3.733|   0.1%/918|   0.1%/691|   0.1%/652|   0.1%/618 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 113   |     122|       6.036|   0.2%/440|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 112   |     156|      38.245|   1.0%/ 72|   0.9%/ 80|   0.8%/ 83|   0.8%/ 86 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 123   |   39779|     314.264|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 124   |     696|     259.623|   1.1%/ 62|   1.0%/ 72|   0.9%/ 75|   0.9%/ 79 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 132   |     269|       7.493|   1.1%/ 66|   1.2%/ 59|   1.2%/ 58|   1.2%/ 56 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  56   |      10|       0.322|   1.1%/ 60|   1.5%/ 46|   1.7%/ 41|   1.9%/ 35 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  10   |       3|       1.220|   0.0%/ --|   0.0%/ --|   0.0%/ --|  14.5%/  5 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  65   |      41|       1.353|   1.3%/ 53|   1.1%/ 62|   1.0%/ 66|   1.0%/ 71 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 136   |    6164|     353.075|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 113   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 115   |     102|      15.721|   1.2%/ 59|   1.0%/ 72|   0.9%/ 77|   0.8%/ 82 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 117   |      69|       3.090|   0.1%/494|   0.2%/446|   0.2%/431|   0.2%/417 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 119   |     807|       3.914|   1.4%/ 49|   1.2%/ 57|   1.2%/ 60|   1.1%/ 63 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 120   |     426|     205.100|   1.6%/ 44|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 128   |     255|      47.434|   0.1%/550|   0.1%/484|   0.1%/467|   0.2%/451 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 111   |     317|      68.058|   3.1%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 123   |    5723|      26.094|   1.2%/ 57|   1.0%/ 72|   0.9%/ 77|   0.8%/ 83 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 131   |    1104|     261.776|   2.8%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 121   |      29|       4.056|   3.3%/ 21|   3.8%/ 18|   4.0%/ 17|   4.1%/ 17 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 122   |   13274|     413.126|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 169   |    1668|      15.374|   0.9%/ 80|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 130   |    1634|      42.569|   0.5%/136|   0.4%/161|   0.4%/168|   0.4%/176 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 125   |    1698|     165.270|   0.3%/207|   0.3%/234|   0.3%/243|   0.3%/252 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 114   |     162|      58.840|   1.4%/ 49|   1.0%/ 70|   0.9%/ 79|   0.8%/ 91 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 120   |    2035|     104.880|   1.1%/ 65|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 123   |   12483|      85.068|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  51   |       5|       0.385|   4.8%/ 14|   3.9%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 118   |    2546|      74.408|   2.0%/ 35|   1.6%/ 43|   1.5%/ 46|   1.4%/ 49 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 110   |     167|      10.318|   1.8%/ 39|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 122   |     476|      68.331|   2.8%/ 24|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  88   |      65|       8.223|   0.4%/178|   0.4%/174|   0.4%/170|   0.4%/165 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 121   |      27|       4.713|   0.3%/255|   0.4%/183|   0.4%/170|   0.4%/159 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 114   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 128   |     111|      53.183|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 103   |      93|       5.879|   0.1%/538|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 115   |    5149|      87.598|   3.4%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 139   |   28430|     603.606|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 114   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 129   |     689|      16.240|   0.7%/ 92|   0.6%/108|   0.6%/112|   0.6%/118 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 131   |    5642|     545.756|   0.3%/265|   0.2%/317|   0.2%/331|   0.2%/347 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 137   |    1970|     228.965|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 113   |      26|       1.502|   5.9%/ 12|   6.0%/ 11|   4.4%/ 16|   4.4%/ 16 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 111   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 141   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 115   |      15|       2.018|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 117   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 123   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 125   |    5497|      66.106|   0.4%/194|   0.4%/196|   0.4%/197|   0.4%/197 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 142   |  140484|     426.299|   0.5%/127|   0.5%/126|   0.6%/126|   0.6%/125 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 129   |    1528|      36.491|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 122   |     341|      34.436|   0.4%/194|   0.3%/223|   0.3%/232|   0.3%/243 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 131   |   45486|     684.661|   0.2%/393|   0.2%/445|   0.2%/460|   0.1%/475 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 113   |      33|       9.313|   1.1%/ 63|   1.2%/ 57|   1.2%/ 56|   1.3%/ 54 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 115   |      93|       2.722|   6.5%/ 11|   6.2%/ 11|   6.1%/ 11|   6.0%/ 11 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 115   |     118|       3.664|   4.0%/ 17|   3.5%/ 19|   3.4%/ 20|   3.3%/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 109   |      52|       2.891|  12.8%/  5|  18.7%/  4|  20.3%/  3|  22.0%/  3 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 119   |      27|       1.805|   8.4%/  8|   9.4%/  7|   9.6%/  7|   9.8%/  7 |

