# State and Country COVID-19 Analysis #
## Updated: at 2020-07-08 for data as of 2020-07-07 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 34.6% of deaths and 37.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 42.5% of the US population and account for 71.6% of deaths and 53.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 116   |   32319|    1661.330|   0.1%/492|   0.1%/506|   0.1%/509|   0.1%/514 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 120   |   15786|    1777.222|   0.2%/305|   0.2%/353|   0.2%/366|   0.2%/380 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 110   |    8239|    1185.543|   0.3%/251|   0.2%/311|   0.2%/330|   0.2%/351 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 113   |    7144|     563.809|   0.4%/161|   0.4%/188|   0.4%/196|   0.3%/203 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 111   |    6813|     532.208|   0.3%/217|   0.3%/269|   0.2%/286|   0.2%/306 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 126   |    6558|     165.986|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 111   |    6249|     625.682|   0.1%/470|   0.1%/526|   0.1%/543|   0.1%/563 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 111   |    4354|    1221.093|   0.1%/664|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 122   |    3826|     178.134|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 116   |    3319|     713.857|   0.4%/175|   0.4%/183|   0.4%/185|   0.4%/187 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 130   |  132014|     400.597|   0.5%/135|   0.5%/147|   0.5%/151|   0.4%/155 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 113   |   67269|     318.189|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 119   |   44607|     671.436|   0.2%/297|   0.2%/356|   0.2%/375|   0.2%/397 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 138   |   34935|     579.946|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 111   |   32749|     258.724|   2.3%/ 30|   1.8%/ 38|   1.7%/ 41|   1.6%/ 44 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 144   |   29982|     446.988|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 127   |   28588|     606.954|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 119   |   21021|      15.443|   2.6%/ 27|   2.5%/ 28|   2.5%/ 28|   2.4%/ 28 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 139   |   11844|     142.052|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 110   |   11089|     345.118|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 105   |    1040|     212.110|   1.2%/ 57|   1.1%/ 65|   1.0%/ 67|   1.0%/ 70 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 105   |      16|      22.377|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 109   |    1927|     264.759|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 106   |     304|     100.598|   1.7%/ 40|   1.3%/ 53|   1.2%/ 57|   1.1%/ 62 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 126   |    6558|     165.986|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 116   |    1710|     297.002|   0.2%/448|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 111   |    4354|    1221.093|   0.1%/664|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 104   |     529|     542.852|   0.1%/478|   0.1%/839|   0.1%/998|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 122   |    3826|     178.134|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 118   |    2919|     274.916|   0.5%/136|   0.4%/195|   0.3%/218|   0.3%/248 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)|  99   |      19|      13.514|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 104   |      94|      52.569|   0.4%/197|   0.4%/179|   0.4%/176|   0.4%/172 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 113   |    7144|     563.809|   0.4%/161|   0.4%/188|   0.4%/196|   0.3%/203 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 114   |    2721|     404.218|   0.4%/169|   0.3%/199|   0.3%/208|   0.3%/218 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 105   |     731|     231.761|   0.4%/191|   0.3%/239|   0.3%/256|   0.3%/275 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 117   |     289|      99.135|   0.7%/ 94|   0.7%/ 94|   0.7%/ 93|   0.7%/ 94 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 114   |     599|     134.180|   0.8%/ 89|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 116   |    3319|     713.857|   0.4%/175|   0.4%/183|   0.4%/185|   0.4%/187 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 103   |     109|      80.753|   0.5%/133|   0.7%/ 97|   0.8%/ 90|   0.8%/ 84 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 111   |    3276|     541.863|   0.4%/183|   0.3%/226|   0.3%/241|   0.3%/257 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 110   |    8239|    1185.543|   0.3%/251|   0.2%/311|   0.2%/330|   0.2%/351 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 111   |    6249|     625.682|   0.1%/470|   0.1%/526|   0.1%/543|   0.1%/563 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 109   |    1526|     270.592|   0.5%/152|   0.3%/202|   0.3%/219|   0.3%/239 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 111   |    1147|     385.518|   1.0%/ 69|   0.9%/ 74|   0.9%/ 75|   0.9%/ 77 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 111   |    1067|     173.777|   0.6%/112|   0.5%/134|   0.5%/140|   0.5%/147 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 103   |      23|      21.809|   0.7%/ 93|   0.6%/125|   0.5%/137|   0.5%/150 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 102   |     290|     149.985|   0.8%/ 85|   0.5%/145|   0.4%/177|   0.3%/228 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 114   |     540|     175.267|   0.8%/ 90|   0.9%/ 79|   0.9%/ 76|   0.9%/ 74 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 107   |     389|     285.787|   0.7%/ 99|   0.6%/126|   0.5%/136|   0.5%/148 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 120   |   15786|    1777.222|   0.2%/305|   0.2%/353|   0.2%/366|   0.2%/380 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 105   |     521|     248.410|   0.6%/111|   0.5%/134|   0.5%/140|   0.5%/147 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 116   |   32319|    1661.330|   0.1%/492|   0.1%/506|   0.1%/509|   0.1%/514 |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 105   |    1465|     139.686|   0.8%/ 84|   0.6%/126|   0.5%/144|   0.4%/168 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 103   |      81|     106.920|   0.4%/176|   0.4%/181|   0.4%/181|   0.4%/181 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 110   |    2963|     253.447|   0.5%/126|   0.5%/142|   0.5%/147|   0.5%/152 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 111   |     404|     101.973|   0.5%/128|   0.6%/123|   0.6%/122|   0.6%/121 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 115   |     219|      51.856|   0.9%/ 80|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 111   |    6813|     532.208|   0.3%/217|   0.3%/269|   0.2%/286|   0.2%/306 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 109   |     156|      48.917|   0.3%/222|   0.3%/217|   0.3%/217|   0.3%/217 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 102   |     975|     920.153|   0.4%/162|   0.3%/237|   0.3%/271|   0.2%/317 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 114   |     841|     163.364|   1.6%/ 42|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 119   |     100|     113.307|   1.1%/ 64|   0.9%/ 74|   0.9%/ 78|   0.8%/ 82 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 109   |     665|      97.377|   1.4%/ 49|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 113   |    2720|      93.821|   1.4%/ 50|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 130   |  132014|     400.597|   0.5%/135|   0.5%/147|   0.5%/151|   0.4%/155 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 108   |     189|      58.956|   1.3%/ 52|   1.5%/ 47|   1.5%/ 46|   1.6%/ 44 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 110   |      56|      89.835|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 116   |    1887|     221.131|   0.9%/ 75|   0.9%/ 73|   0.9%/ 73|   0.9%/ 73 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 130   |    1380|     181.217|   0.5%/134|   0.5%/142|   0.5%/144|   0.5%/145 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 100   |      95|      53.043|   0.3%/206|   0.3%/256|   0.3%/273|   0.2%/290 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 110   |     810|     139.110|   0.5%/151|   0.3%/243|   0.2%/286|   0.2%/349 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  86   |      20|      34.954|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 108   |     919|      28.519|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 119   |      82|      28.652|   4.2%/ 16|   4.6%/ 15|   4.7%/ 15|   4.7%/ 14 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 118   |     972|      22.615|   0.9%/ 80|   0.8%/ 91|   0.7%/ 94|   0.7%/ 97 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 101   |      21|       0.685|   5.9%/ 12|   6.6%/ 10|   6.7%/ 10|   6.9%/ 10 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 122   |    1613|      35.884|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 104   |     515|     174.056|   2.2%/ 31|   1.7%/ 42|   1.5%/ 45|   1.4%/ 50 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 129   |     105|       4.107|   0.2%/290|   0.3%/231|   0.3%/219|   0.3%/209 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 118   |     710|      79.731|   0.1%/539|   0.1%/908|   0.1%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 117   |     269|      26.762|   3.4%/ 20|   3.2%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 114   |     107|      69.271|   2.8%/ 24|   1.9%/ 37|   1.6%/ 43|   1.4%/ 51 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 112   |    2168|      12.869|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)|  99   |     435|      46.267|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 119   |    9782|     848.823|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)|  93   |      23|       1.996|   9.5%/  7|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 101   |    1547|     134.853|   4.4%/ 15|   4.6%/ 15|   4.7%/ 15|   4.7%/ 15 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 109   |     198|      60.033|   1.1%/ 65|   1.3%/ 54|   1.3%/ 52|   1.4%/ 50 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)|  99   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 113   |   67269|     318.189|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 119   |     253|      36.446|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 112   |      53|       2.540|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  86   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 105   |     325|      12.246|   0.4%/189|   0.1%/646|   0.1%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 121   |    8799|     231.559|   0.2%/319|   0.2%/442|   0.1%/486|   0.1%/539 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  46   |      51|       9.348|   1.9%/ 36|   1.6%/ 43|   1.9%/ 36|   2.3%/ 30 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  71   |      74|       4.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 108   |    6720|     351.698|   2.5%/ 28|   1.8%/ 38|   1.7%/ 41|   1.5%/ 46 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 119   |    4641|       3.310|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 108   |    4533|      91.761|   4.3%/ 16|   4.2%/ 16|   4.2%/ 17|   4.1%/ 17 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 111   |      21|       4.107|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 111   |     112|      27.548|   0.4%/181|   0.6%/124|   0.6%/114|   0.7%/106 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 112   |      86|       7.700|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 116   |     608|     104.426|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 113   |     818|      78.937|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 116   |    4867|     278.613|   1.0%/ 73|   1.0%/ 73|   1.0%/ 73|   1.0%/ 73 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 122   |    3642|      36.323|   2.9%/ 24|   2.4%/ 29|   2.2%/ 31|   2.1%/ 33 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)|  99   |     245|      37.730|   5.3%/ 13|   4.7%/ 15|   4.5%/ 15|   4.3%/ 16 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  77   |      54|      39.991|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)|  94   |     111|       1.126|   1.5%/ 46|   0.4%/197|   0.0%/ ***|   0.0%/ -- |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 109   |     329|      59.569|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 144   |   29982|     446.988|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 110   |      47|      21.537|   1.6%/ 43|   1.1%/ 66|   0.9%/ 74|   0.8%/ 85 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 107   |       3|       1.069|   3.7%/ 19|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)|  95   |      15|       4.097|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 121   |    9048|     108.811|   0.1%/780|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 109   |     135|       4.453|   2.7%/ 26|   1.6%/ 44|   1.3%/ 52|   1.1%/ 65 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 119   |     193|      18.009|   0.1%/720|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 114   |    1037|      62.435|   4.1%/ 17|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  84   |      35|       2.870|   1.4%/ 48|   1.0%/ 67|   0.9%/ 76|   0.8%/ 89 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  73   |      26|      16.194|   2.3%/ 30|   0.8%/ 92|   0.4%/194|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)|  94   |     118|      10.189|   1.7%/ 41|   1.4%/ 48|   1.4%/ 51|   1.3%/ 54 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 104   |     686|      74.876|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 115   |     592|      60.597|   0.2%/371|   0.1%/472|   0.1%/509|   0.1%/554 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 119   |   21021|      15.443|   2.6%/ 27|   2.5%/ 28|   2.5%/ 28|   2.4%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 119   |    3277|      12.279|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 139   |   11844|     142.052|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 126   |    2950|      75.403|   5.7%/ 12|   4.7%/ 15|   4.4%/ 16|   4.2%/ 16 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 119   |    1746|     354.787|   0.1%/866|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 109   |     335|      36.457|   0.7%/106|   0.8%/ 87|   0.8%/ 83|   0.9%/ 79 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 138   |   34935|     579.946|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 111   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 146   |     988|       7.845|   0.2%/437|   0.1%/687|   0.1%/811|   0.1%/994 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 103   |      10|       0.947|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 105   |     258|      13.829|   2.2%/ 31|   0.4%/155|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 104   |     168|       3.527|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 104   |      67|      37.526|   0.2%/305|   0.4%/188|   0.4%/169|   0.5%/152 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)|  95   |     376|      85.014|   0.9%/ 75|   0.8%/ 84|   0.8%/ 86|   0.8%/ 88 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)|  96   |     100|      15.294|   7.1%/ 10|   8.5%/  8|   8.9%/  8|   9.2%/  7 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)|  96   |      30|      15.737|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 120   |      36|       5.255|   0.8%/ 88|   0.9%/ 73|   1.0%/ 70|   1.0%/ 67 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)|  95   |      39|       8.683|   1.1%/ 63|   1.5%/ 46|   1.6%/ 43|   1.7%/ 41 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)|  97   |      35|       5.146|   6.0%/ 11|   7.2%/ 10|   8.0%/  9|   9.0%/  8 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 109   |      79|      28.387|   0.2%/356|   0.2%/441|   0.1%/468|   0.1%/500 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  52   |      35|       1.342|   7.1%/ 10|   8.0%/  9|   8.0%/  9|   8.0%/  9 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 113   |     121|       3.694|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 101   |     120|       5.919|   0.5%/129|   0.5%/150|   0.4%/156|   0.4%/162 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 100   |     137|      33.531|   1.2%/ 59|   0.5%/127|   0.4%/177|   0.2%/288 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 111   |   32749|     258.724|   2.3%/ 30|   1.8%/ 38|   1.7%/ 41|   1.6%/ 44 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 112   |     607|     226.417|   1.5%/ 45|   1.4%/ 51|   1.3%/ 53|   1.3%/ 54 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 120   |     236|       6.588|   0.7%/ 94|   0.9%/ 75|   1.0%/ 71|   1.0%/ 68 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  44   |       8|       0.274|   3.8%/ 18|   6.2%/ 11|   7.0%/ 10|   7.9%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  53   |      36|       1.191|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 124   |    6148|     352.203|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 101   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 103   |      88|      13.687|   3.9%/ 18|   0.0%/ --|   0.0%/ --|   3.1%/ 22 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 105   |      68|       3.047|   0.1%/585|   0.1%/483|   0.2%/457|   0.2%/433 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 107   |     667|       3.235|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 108   |     360|     173.146|   2.5%/ 28|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 116   |     252|      47.023|   0.1%/621|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)|  99   |     224|      48.079|   3.5%/ 20|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 111   |    5005|      22.818|   2.0%/ 35|   1.5%/ 46|   1.4%/ 50|   1.3%/ 54 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 119   |     776|     183.841|   2.9%/ 23|   3.2%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 109   |      21|       2.916|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 110   |   11089|     345.118|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 157   |    1335|      12.305|   0.7%/ 94|   0.6%/109|   0.6%/113|   0.6%/119 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 118   |    1549|      40.352|   0.7%/ 93|   0.6%/115|   0.6%/122|   0.5%/130 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 113   |    1620|     157.599|   0.4%/175|   0.5%/145|   0.5%/139|   0.5%/133 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 102   |     133|      48.282|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.1%/ 32 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 108   |    1783|      91.873|   1.1%/ 62|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 111   |   10492|      71.499|   1.6%/ 42|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  39   |       3|       0.244|   8.7%/  8|   2.9%/ 24|   0.1%/679|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 106   |    2030|      59.315|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)|  98   |     141|       8.678|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 110   |     308|      44.163|   1.4%/ 49|   1.9%/ 36|   2.0%/ 34|   2.2%/ 32 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  76   |      63|       7.992|   0.9%/ 78|   0.6%/124|   0.5%/144|   0.4%/172 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 109   |      26|       4.559|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 102   |      28|       5.132|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 116   |     111|      53.190|   0.1%/854|   0.1%/811|   0.1%/815|   0.1%/825 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)|  91   |      92|       5.770|   0.2%/308|   0.3%/238|   0.3%/220|   0.3%/204 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 103   |    3417|      58.132|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 127   |   28588|     606.954|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 102   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 117   |     632|      14.893|   1.0%/ 68|   0.7%/ 99|   0.6%/111|   0.5%/126 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 119   |    5497|     531.707|   0.4%/181|   0.3%/241|   0.3%/263|   0.2%/291 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 125   |    1968|     228.751|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 101   |      11|       0.620|   0.0%/ --|  13.0%/  5|  11.9%/  6|  11.9%/  6 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)|  99   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 129   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 103   |      15|       1.986|   0.8%/ 82|   1.0%/ 68|   1.1%/ 65|   1.1%/ 63 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 105   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 111   |      50|       4.268|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 113   |    5268|      63.357|   0.4%/187|   0.3%/201|   0.3%/205|   0.3%/209 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 130   |  132014|     400.597|   0.5%/135|   0.5%/147|   0.5%/151|   0.4%/155 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 117   |    1304|      31.144|   1.6%/ 45|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 110   |     326|      32.913|   0.5%/145|   0.5%/149|   0.5%/149|   0.5%/149 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 119   |   44607|     671.436|   0.2%/297|   0.2%/356|   0.2%/375|   0.2%/397 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 101   |      29|       8.261|   0.9%/ 73|   0.9%/ 78|   0.9%/ 80|   0.8%/ 82 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 103   |      34|       0.992|   5.2%/ 13|   7.5%/  9|   8.0%/  8|   8.6%/  8 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 103   |      71|       2.215|   5.0%/ 14|   5.1%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)|  97   |      37|       2.095|  10.9%/  6|   0.0%/ --|   0.0%/ --|  11.9%/  6 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 107   |       9|       0.564|   3.8%/ 18|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |

