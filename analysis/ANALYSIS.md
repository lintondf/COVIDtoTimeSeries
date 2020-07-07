# State and Country COVID-19 Analysis #
## Updated: at 2020-07-07 for data as of 2020-07-06 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 36.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.8% of deaths and 54.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 115   |   32256|    1658.099|   0.2%/453|   0.2%/449|   0.2%/447|   0.2%/446 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 119   |   15735|    1771.480|   0.2%/298|   0.2%/354|   0.2%/369|   0.2%/386 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 109   |    8224|    1183.378|   0.3%/238|   0.2%/288|   0.2%/303|   0.2%/321 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 112   |    7093|     559.731|   0.4%/186|   0.2%/282|   0.2%/324|   0.2%/381 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 110   |    6797|     530.968|   0.3%/205|   0.3%/247|   0.3%/260|   0.3%/276 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 125   |    6488|     164.199|   1.0%/ 68|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 110   |    6238|     624.665|   0.1%/473|   0.1%/548|   0.1%/573|   0.1%/601 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 110   |    4353|    1220.939|   0.1%/589|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 121   |    3777|     175.834|   1.2%/ 58|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 115   |    3305|     710.955|   0.4%/175|   0.4%/184|   0.4%/186|   0.4%/188 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 129   |  131384|     398.683|   0.5%/133|   0.5%/144|   0.5%/147|   0.5%/151 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 112   |   66287|     313.545|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 118   |   44528|     670.245|   0.2%/281|   0.2%/330|   0.2%/345|   0.2%/362 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 137   |   34926|     579.791|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 110   |   32228|     254.607|   2.4%/ 29|   1.9%/ 36|   1.8%/ 39|   1.7%/ 42 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 143   |   29969|     446.791|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 126   |   28616|     607.563|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 118   |   20654|      15.173|   2.6%/ 26|   2.5%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 138   |   11671|     139.982|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 109   |   10914|     339.680|   2.0%/ 34|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 104   |    1029|     209.834|   1.3%/ 55|   1.2%/ 60|   1.1%/ 62|   1.1%/ 63 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 104   |      16|      21.674|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 108   |    1886|     259.126|   2.1%/ 33|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 105   |     300|      99.289|   1.8%/ 39|   1.3%/ 53|   1.2%/ 59|   1.1%/ 65 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 125   |    6488|     164.199|   1.0%/ 68|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 115   |    1710|     296.905|   0.2%/365|   0.1%/679|   0.1%/861|   0.1%/ *** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 110   |    4353|    1220.939|   0.1%/589|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 103   |     529|     543.041|   0.2%/444|   0.1%/903|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 121   |    3777|     175.834|   1.2%/ 58|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 117   |    2909|     274.023|   0.5%/132|   0.3%/198|   0.3%/226|   0.3%/263 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  98   |      19|      13.454|   1.2%/ 60|   1.7%/ 40|   1.9%/ 37|   2.0%/ 34 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 103   |      94|      52.374|   0.3%/200|   0.4%/181|   0.4%/177|   0.4%/173 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 112   |    7093|     559.731|   0.4%/186|   0.2%/282|   0.2%/324|   0.2%/381 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 113   |    2712|     402.814|   0.4%/164|   0.4%/197|   0.3%/207|   0.3%/217 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 104   |     728|     230.882|   0.4%/194|   0.3%/269|   0.2%/298|   0.2%/336 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 116   |     287|      98.349|   0.7%/ 94|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 113   |     594|     132.980|   0.8%/ 92|   0.7%/ 94|   0.7%/ 95|   0.7%/ 95 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 115   |    3305|     710.955|   0.4%/175|   0.4%/184|   0.4%/186|   0.4%/188 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 102   |     108|      80.065|   0.5%/151|   0.6%/108|   0.7%/100|   0.7%/ 94 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 110   |    3266|     540.297|   0.4%/176|   0.3%/218|   0.3%/232|   0.3%/248 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 109   |    8224|    1183.378|   0.3%/238|   0.2%/288|   0.2%/303|   0.2%/321 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 110   |    6238|     624.665|   0.1%/473|   0.1%/548|   0.1%/573|   0.1%/601 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 108   |    1522|     269.920|   0.5%/141|   0.4%/184|   0.3%/199|   0.3%/215 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 110   |    1133|     380.742|   1.0%/ 71|   0.9%/ 81|   0.8%/ 85|   0.8%/ 88 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 110   |    1061|     172.796|   0.6%/108|   0.5%/132|   0.5%/139|   0.5%/146 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 102   |      23|      21.735|   0.8%/ 82|   0.7%/ 99|   0.7%/104|   0.6%/109 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 101   |     290|     149.841|   0.9%/ 73|   0.7%/104|   0.6%/116|   0.5%/132 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 113   |     534|     173.385|   0.7%/ 95|   0.8%/ 86|   0.8%/ 83|   0.9%/ 81 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 106   |     387|     284.615|   0.7%/ 93|   0.6%/115|   0.6%/124|   0.5%/133 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 119   |   15735|    1771.480|   0.2%/298|   0.2%/354|   0.2%/369|   0.2%/386 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 104   |     518|     247.195|   0.7%/106|   0.5%/126|   0.5%/132|   0.5%/138 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 115   |   32256|    1658.099|   0.2%/453|   0.2%/449|   0.2%/447|   0.2%/446 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 104   |    1459|     139.097|   0.9%/ 79|   0.6%/114|   0.5%/129|   0.5%/148 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 102   |      81|     105.874|   0.3%/235|   0.2%/417|   0.1%/518|   0.1%/683 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 109   |    2945|     251.961|   0.5%/128|   0.5%/152|   0.4%/160|   0.4%/169 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 110   |     401|     101.325|   0.5%/128|   0.6%/120|   0.6%/119|   0.6%/118 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 114   |     217|      51.364|   0.9%/ 81|   0.8%/ 88|   0.8%/ 90|   0.8%/ 92 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 110   |    6797|     530.968|   0.3%/205|   0.3%/247|   0.3%/260|   0.3%/276 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 108   |     156|      48.707|   0.3%/231|   0.3%/230|   0.3%/231|   0.3%/232 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 101   |     972|     917.643|   0.5%/153|   0.3%/227|   0.3%/259|   0.2%/304 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 113   |     825|     160.328|   1.7%/ 41|   1.8%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 118   |      99|     112.452|   1.2%/ 59|   1.1%/ 65|   1.0%/ 67|   1.0%/ 69 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 108   |     656|      96.058|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 112   |    2673|      92.201|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 129   |  131384|     398.683|   0.5%/133|   0.5%/144|   0.5%/147|   0.5%/151 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 107   |     186|      57.908|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 109   |      56|      89.880|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 115   |    1871|     219.202|   1.0%/ 72|   1.0%/ 68|   1.0%/ 67|   1.0%/ 66 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 129   |    1372|     180.209|   0.5%/139|   0.5%/152|   0.4%/156|   0.4%/160 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)|  99   |      95|      52.886|   0.3%/204|   0.3%/250|   0.3%/267|   0.2%/286 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 109   |     808|     138.744|   0.5%/142|   0.3%/230|   0.3%/272|   0.2%/333 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  85   |      20|      34.575|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 107   |     894|      27.728|   2.8%/ 25|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 118   |      78|      27.460|   4.3%/ 16|   4.9%/ 14|   5.0%/ 14|   5.1%/ 13 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 117   |     966|      22.454|   0.9%/ 78|   0.8%/ 89|   0.7%/ 92|   0.7%/ 96 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 100   |      20|       0.655|   6.1%/ 11|   6.9%/ 10|   7.2%/  9|   7.4%/  9 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 121   |    1561|      34.743|   2.9%/ 24|   2.9%/ 24|   2.9%/ 23|   2.9%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 103   |     506|     171.149|   2.3%/ 30|   1.7%/ 40|   1.6%/ 43|   1.4%/ 48 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 128   |     105|       4.095|   0.2%/361|   0.2%/295|   0.2%/283|   0.3%/272 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 117   |     710|      79.711|   0.1%/487|   0.1%/739|   0.1%/859|   0.1%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 116   |     261|      25.971|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 113   |     106|      68.580|   3.2%/ 22|   2.2%/ 31|   2.0%/ 35|   1.7%/ 40 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 111   |    2120|      12.582|   2.4%/ 28|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  98   |     429|      45.597|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 118   |    9779|     848.549|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  92   |      23|       1.985|   4.1%/ 17|   3.0%/ 23|   2.6%/ 26|   2.3%/ 30 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 100   |    1481|     129.139|   4.5%/ 15|   4.8%/ 14|   4.9%/ 14|   5.0%/ 14 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 108   |     195|      59.111|   0.9%/ 76|   1.0%/ 66|   1.1%/ 65|   1.1%/ 63 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  98   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 112   |   66287|     313.545|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 118   |     250|      35.906|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 111   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  85   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 104   |     319|      12.015|   0.3%/258|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 120   |    8788|     231.274|   0.2%/298|   0.2%/409|   0.2%/449|   0.1%/495 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  45   |      50|       9.098|   2.6%/ 26|   1.2%/ 58|   1.2%/ 58|   1.3%/ 54 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  70   |      74|       4.555|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 107   |    6611|     345.980|   2.7%/ 26|   2.0%/ 34|   1.9%/ 37|   1.7%/ 40 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 118   |    4641|       3.310|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 107   |    4359|      88.248|   4.4%/ 16|   4.3%/ 16|   4.3%/ 16|   4.3%/ 16 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 110   |      19|       3.818|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 110   |     112|      27.358|   0.4%/163|   0.7%/104|   0.7%/ 95|   0.8%/ 87 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 111   |      86|       7.699|   0.1%/882|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 115   |     607|     104.319|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 112   |     807|      77.870|   1.3%/ 53|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 115   |    4820|     275.907|   1.0%/ 71|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 121   |    3571|      35.617|   3.0%/ 23|   2.5%/ 27|   2.4%/ 29|   2.3%/ 31 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  98   |     236|      36.377|   5.6%/ 12|   5.1%/ 13|   5.0%/ 14|   4.8%/ 14 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  76   |      52|      38.368|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  93   |     112|       1.131|   1.8%/ 39|   0.6%/108|   0.3%/206|   0.0%/ *** |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 108   |     329|      59.549|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 143   |   29969|     446.791|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 109   |      46|      21.382|   1.7%/ 41|   1.0%/ 69|   0.8%/ 82|   0.7%/ 99 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 106   |       2|       1.013|   2.7%/ 25|   1.1%/ 61|   0.8%/ 90|   0.4%/155 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  94   |      15|       4.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 120   |    9043|     108.751|   0.1%/726|   0.1%/920|   0.1%/986|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 108   |     134|       4.410|   2.7%/ 25|   1.5%/ 47|   1.1%/ 61|   0.8%/ 84 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 118   |     193|      18.002|   0.1%/715|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 113   |    1003|      60.393|   4.2%/ 16|   4.0%/ 17|   3.9%/ 17|   3.9%/ 18 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  83   |      35|       2.855|   1.6%/ 44|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  72   |      26|      16.246|   2.6%/ 27|   1.2%/ 58|   0.8%/ 84|   0.4%/156 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  93   |     116|      10.040|   1.8%/ 39|   1.5%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 103   |     663|      72.345|   3.9%/ 17|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 114   |     592|      60.542|   0.2%/331|   0.2%/385|   0.2%/403|   0.2%/423 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 118   |   20654|      15.173|   2.6%/ 26|   2.5%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 118   |    3212|      12.034|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 138   |   11671|     139.982|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 125   |    2841|      72.609|   5.9%/ 12|   4.9%/ 14|   4.7%/ 15|   4.4%/ 15 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 118   |    1745|     354.639|   0.1%/788|   0.1%/962|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 108   |     332|      36.104|   0.6%/118|   0.7%/ 98|   0.7%/ 94|   0.8%/ 91 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 137   |   34926|     579.791|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 110   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 145   |     987|       7.838|   0.2%/410|   0.1%/610|   0.1%/703|   0.1%/836 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 102   |       9|       0.844|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 104   |     243|      12.988|   2.6%/ 26|   0.9%/ 74|   0.5%/141|   0.0%/ *** |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 103   |     165|       3.465|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.7%/ 42 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 103   |      64|      35.395|   0.2%/392|   0.3%/255|   0.3%/228|   0.3%/205 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  94   |     372|      84.271|   0.9%/ 76|   0.8%/ 88|   0.8%/ 92|   0.7%/ 95 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  95   |      92|      14.035|   6.6%/ 10|   7.7%/  9|   8.0%/  9|   8.3%/  8 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  95   |      30|      15.738|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 119   |      36|       5.214|   0.7%/ 93|   0.9%/ 76|   0.9%/ 73|   1.0%/ 70 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  94   |      38|       8.489|   0.8%/ 82|   1.0%/ 66|   1.1%/ 63|   1.1%/ 61 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  96   |      34|       4.885|  10.1%/  7|   2.6%/ 27|   7.2%/ 10|   8.0%/  9 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 108   |      79|      28.358|   0.2%/321|   0.2%/361|   0.2%/373|   0.2%/385 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  51   |      34|       1.280|   6.2%/ 11|   8.8%/  8|   9.3%/  7|   9.8%/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 112   |     121|       3.695|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 100   |     119|       5.900|   0.6%/121|   0.5%/137|   0.5%/141|   0.5%/145 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)|  99   |     136|      33.277|   1.2%/ 58|   0.4%/165|   0.2%/305|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 110   |   32228|     254.607|   2.4%/ 29|   1.9%/ 36|   1.8%/ 39|   1.7%/ 42 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 111   |     599|     223.233|   1.6%/ 44|   1.4%/ 50|   1.3%/ 51|   1.3%/ 53 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 119   |     234|       6.527|   0.7%/103|   0.8%/ 82|   0.9%/ 78|   0.9%/ 74 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  43   |       8|       0.265|   3.4%/ 20|   6.4%/ 11|   7.4%/  9|   8.7%/  8 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  52   |      35|       1.169|   2.8%/ 25|   3.1%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 123   |    6145|     352.023|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 100   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 102   |      86|      13.382|   3.9%/ 18|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 104   |      68|       3.043|   0.1%/539|   0.2%/440|   0.2%/413|   0.2%/388 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 106   |     656|       3.183|   1.7%/ 40|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 107   |     352|     169.682|   2.6%/ 27|   2.3%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 115   |     252|      47.008|   0.1%/537|   0.1%/840|   0.1%/988|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  98   |     216|      46.402|   3.5%/ 20|   3.8%/ 18|   3.8%/ 18|   3.9%/ 18 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 110   |    4942|      22.532|   2.0%/ 34|   1.5%/ 47|   1.3%/ 52|   1.2%/ 58 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 118   |     749|     177.587|   2.8%/ 24|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 108   |      20|       2.848|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 109   |   10914|     339.680|   2.0%/ 34|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 156   |    1328|      12.239|   0.8%/ 90|   0.7%/101|   0.7%/104|   0.6%/108 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 117   |    1541|      40.161|   0.8%/ 86|   0.7%/102|   0.6%/107|   0.6%/112 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 112   |    1611|     156.756|   0.4%/183|   0.5%/151|   0.5%/145|   0.5%/139 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 101   |     130|      47.310|   2.1%/ 32|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 107   |    1760|      90.712|   1.1%/ 64|   1.2%/ 60|   1.2%/ 59|   1.2%/ 58 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 110   |   10332|      70.410|   1.7%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  38   |       3|       0.249|   3.2%/ 22|   5.1%/ 13|   1.7%/ 40|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 105   |    1976|      57.735|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 24 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  97   |     137|       8.458|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 109   |     302|      43.318|   1.2%/ 58|   1.6%/ 42|   1.7%/ 40|   1.9%/ 37 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  75   |      63|       7.940|   0.9%/ 73|   0.6%/112|   0.5%/131|   0.4%/155 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 108   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 101   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 115   |     111|      53.159|   0.1%/745|   0.1%/642|   0.1%/627|   0.1%/617 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  90   |      91|       5.753|   0.2%/296|   0.3%/204|   0.4%/186|   0.4%/169 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 102   |    3281|      55.815|   3.6%/ 19|   3.5%/ 19|   3.5%/ 19|   3.5%/ 19 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 126   |   28616|     607.563|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 101   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 116   |     628|      14.806|   1.1%/ 65|   0.7%/ 96|   0.6%/108|   0.6%/124 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 118   |    5485|     530.581|   0.4%/167|   0.3%/213|   0.3%/229|   0.3%/248 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 124   |    1968|     228.746|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 100   |      11|       0.602|   0.0%/ --|   3.6%/ 19|  13.0%/  5|  11.9%/  6 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  98   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 128   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 102   |      15|       1.968|   0.9%/ 76|   1.2%/ 57|   1.3%/ 54|   1.4%/ 51 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 104   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 110   |      50|       4.270|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 112   |    5251|      63.150|   0.4%/184|   0.4%/197|   0.3%/200|   0.3%/204 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 129   |  131384|     398.683|   0.5%/133|   0.5%/144|   0.5%/147|   0.5%/151 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 116   |    1286|      30.696|   1.6%/ 44|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 109   |     324|      32.757|   0.5%/146|   0.5%/152|   0.5%/153|   0.4%/155 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 118   |   44528|     670.245|   0.2%/281|   0.2%/330|   0.2%/345|   0.2%/362 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 100   |      29|       8.189|   0.9%/ 75|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 102   |      32|       0.927|   4.5%/ 15|   6.6%/ 10|   7.2%/  9|   7.7%/  9 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 102   |      68|       2.107|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13|   5.3%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  96   |      34|       1.915|   4.6%/ 15|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 106   |       8|       0.535|   3.9%/ 18|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22 |

