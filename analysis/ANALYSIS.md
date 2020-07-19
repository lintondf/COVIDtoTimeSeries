# State and Country COVID-19 Analysis #
## Updated: at 2020-07-19 for data as of 2020-07-18 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.0% of deaths and 39.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.2% of deaths and 57.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 127   |   32612|    1676.381|   0.1%/940|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 131   |   15834|    1782.670|   0.2%/291|   0.2%/301|   0.2%/304|   0.2%/308 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 121   |    8430|    1212.972|   0.2%/318|   0.2%/351|   0.2%/360|   0.2%/370 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 137   |    7635|     193.238|   1.4%/ 51|   1.5%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 124   |    7551|     595.922|   0.4%/185|   0.3%/211|   0.3%/220|   0.3%/231 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 122   |    7024|     548.681|   0.3%/237|   0.3%/249|   0.3%/251|   0.3%/254 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 122   |    6368|     637.668|   0.2%/424|   0.2%/429|   0.2%/431|   0.2%/433 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 133   |    4721|     219.802|   2.0%/ 34|   2.3%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 122   |    4389|    1231.084|   0.1%/621|   0.1%/546|   0.1%/526|   0.1%/506 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 124   |    3714|     128.075|   2.9%/ 24|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 141   |  139747|     424.063|   0.5%/126|   0.6%/126|   0.6%/125|   0.6%/125 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 124   |   79210|     374.672|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 130   |   45427|     683.776|   0.2%/380|   0.2%/427|   0.2%/439|   0.2%/453 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 122   |   39216|     309.817|   1.8%/ 38|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 149   |   35055|     581.941|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 155   |   30145|     449.411|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 138   |   28431|     603.632|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 130   |   26845|      19.721|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 150   |   13951|     167.324|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 121   |   13087|     407.301|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 116   |    1254|     255.718|   1.9%/ 37|   2.1%/ 32|   2.2%/ 31|   2.3%/ 30 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 116   |      18|      24.639|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 120   |    2601|     357.395|   2.9%/ 24|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 117   |     354|     117.143|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 137   |    7635|     193.238|   1.4%/ 51|   1.5%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 127   |    1750|     303.814|   0.2%/299|   0.2%/277|   0.3%/272|   0.3%/266 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 122   |    4389|    1231.084|   0.1%/621|   0.1%/546|   0.1%/526|   0.1%/506 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 115   |     522|     536.312|   0.1%/462|   0.2%/442|   0.2%/437|   0.2%/432 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 133   |    4721|     219.802|   2.0%/ 34|   2.3%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 129   |    3133|     295.052|   0.7%/ 98|   0.8%/ 88|   0.8%/ 86|   0.8%/ 84 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 110   |      23|      16.392|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 115   |     108|      60.203|   1.6%/ 43|   2.1%/ 33|   2.2%/ 31|   2.4%/ 29 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 124   |    7551|     595.922|   0.4%/185|   0.3%/211|   0.3%/220|   0.3%/231 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 125   |    2820|     418.836|   0.3%/202|   0.3%/217|   0.3%/221|   0.3%/225 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 116   |     782|     247.843|   0.7%/106|   0.8%/ 89|   0.8%/ 85|   0.8%/ 82 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 128   |     309|     106.056|   0.6%/109|   0.6%/116|   0.6%/118|   0.6%/120 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 125   |     661|     147.964|   0.9%/ 76|   1.0%/ 72|   1.0%/ 72|   1.0%/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 127   |    3510|     755.133|   0.5%/138|   0.5%/130|   0.5%/128|   0.5%/126 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 114   |     116|      86.662|   0.5%/128|   0.5%/132|   0.5%/134|   0.5%/136 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 122   |    3376|     558.369|   0.3%/242|   0.3%/275|   0.2%/285|   0.2%/296 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 121   |    8430|    1212.972|   0.2%/318|   0.2%/351|   0.2%/360|   0.2%/370 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 122   |    6368|     637.668|   0.2%/424|   0.2%/429|   0.2%/431|   0.2%/433 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 120   |    1577|     279.572|   0.4%/189|   0.3%/198|   0.3%/200|   0.3%/202 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 122   |    1342|     450.794|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 122   |    1137|     185.208|   0.6%/118|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 114   |      37|      34.383|   2.7%/ 25|   3.5%/ 20|   3.7%/ 19|   3.9%/ 18 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 113   |     297|     153.737|   0.6%/118|   0.6%/107|   0.7%/103|   0.7%/ 99 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 125   |     639|     207.534|   1.4%/ 50|   1.6%/ 45|   1.6%/ 43|   1.6%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 118   |     399|     293.518|   0.3%/216|   0.2%/350|   0.2%/413|   0.1%/501 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 131   |   15834|    1782.670|   0.2%/291|   0.2%/301|   0.2%/304|   0.2%/308 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 116   |     569|     271.455|   0.8%/ 91|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 127   |   32612|    1676.381|   0.1%/940|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 116   |    1625|     154.939|   1.1%/ 65|   1.2%/ 57|   1.2%/ 55|   1.3%/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 114   |      90|     118.704|   0.7%/ 94|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 121   |    3141|     268.704|   0.5%/136|   0.5%/145|   0.5%/148|   0.5%/151 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 122   |     443|     112.005|   0.9%/ 78|   1.0%/ 68|   1.1%/ 65|   1.1%/ 63 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 126   |     254|      60.250|   1.3%/ 53|   1.5%/ 48|   1.5%/ 46|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 122   |    7024|     548.681|   0.3%/237|   0.3%/249|   0.3%/251|   0.3%/254 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 120   |     174|      54.613|   1.0%/ 72|   1.2%/ 57|   1.3%/ 54|   1.3%/ 52 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 113   |     994|     938.665|   0.2%/295|   0.2%/419|   0.1%/463|   0.1%/517 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 125   |    1097|     213.090|   2.5%/ 28|   2.8%/ 25|   2.8%/ 24|   2.9%/ 24 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 130   |     116|     131.453|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 120   |     825|     120.795|   1.9%/ 37|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 124   |    3714|     128.075|   2.9%/ 24|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 141   |  139747|     424.063|   0.5%/126|   0.6%/126|   0.6%/125|   0.6%/125 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 119   |     242|      75.379|   2.0%/ 35|   2.1%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 121   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 127   |    2050|     240.199|   0.7%/100|   0.6%/122|   0.5%/130|   0.5%/138 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 141   |    1451|     190.484|   0.5%/144|   0.5%/152|   0.4%/154|   0.4%/157 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 111   |      99|      55.345|   0.5%/143|   0.6%/112|   0.7%/106|   0.7%/101 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 121   |     839|     144.063|   0.4%/181|   0.4%/190|   0.4%/192|   0.4%/193 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  97   |      23|      40.295|   1.4%/ 49|   2.1%/ 33|   2.2%/ 31|   2.4%/ 28 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 119   |    1170|      36.300|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30|   2.2%/ 31 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 130   |     113|      39.572|   3.2%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 129   |    1066|      24.799|   0.9%/ 79|   0.9%/ 78|   0.9%/ 77|   0.9%/ 77 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 112   |      30|       0.976|   3.6%/ 19|   3.0%/ 23|   2.9%/ 24|   2.7%/ 25 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 133   |    2227|      49.566|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 115   |     633|     214.025|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 140   |     111|       4.327|   1.0%/ 72|   1.3%/ 54|   1.4%/ 51|   1.4%/ 48 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 129   |     711|      79.899|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 128   |     359|      35.704|   2.6%/ 26|   2.3%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 125   |     124|      80.282|   2.1%/ 32|   1.9%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 123   |    2627|      15.594|   1.8%/ 38|   1.6%/ 43|   1.5%/ 45|   1.5%/ 47 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 110   |     499|      53.083|   1.2%/ 56|   1.1%/ 61|   1.1%/ 63|   1.1%/ 64 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 130   |    9803|     850.608|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 104   |      30|       2.547|   4.2%/ 16|   2.5%/ 28|   6.0%/ 11|   6.0%/ 11 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 112   |    2183|     190.296|   3.2%/ 22|   2.6%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 120   |     245|      74.239|   1.7%/ 41|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 110   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 124   |   79210|     374.672|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 130   |     300|      43.157|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 123   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  97   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 116   |     379|      14.264|   0.7%/ 95|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 132   |    8914|     234.576|   0.1%/487|   0.1%/597|   0.1%/633|   0.1%/672 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  57   |      54|       9.795|   0.4%/162|   0.3%/235|   0.3%/237|   0.3%/231 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  82   |      75|       4.628|   0.1%/647|   0.1%/549|   0.1%/539|   0.1%/536 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 119   |    7898|     413.337|   1.4%/ 51|   1.0%/ 69|   0.9%/ 75|   0.8%/ 82 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 130   |    4641|       3.310|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 119   |    6689|     135.416|   3.6%/ 19|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 122   |      47|       9.245|   7.3%/  9|   8.4%/  8|   8.7%/  8|   9.0%/  8 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 122   |     122|      29.900|   0.5%/134|   0.5%/144|   0.5%/148|   0.5%/153 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 123   |      87|       7.772|   0.1%/889|   0.1%/923|   0.1%/929|   0.1%/936 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 127   |     611|     104.991|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 124   |     967|      93.309|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 127   |    5302|     303.519|   0.8%/ 84|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 133   |    4379|      43.671|   1.9%/ 36|   1.6%/ 44|   1.5%/ 46|   1.4%/ 49 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 110   |     321|      49.517|   3.3%/ 21|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  88   |      52|      38.042|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 105   |     154|       1.561|   2.9%/ 24|   3.6%/ 19|   3.8%/ 18|   3.9%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 120   |     329|      59.453|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 155   |   30145|     449.411|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 121   |      47|      21.777|   0.3%/207|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 118   |       4|       1.495|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 106   |      15|       4.034|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 132   |    9105|     109.505|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 120   |     148|       4.887|   1.2%/ 56|   0.8%/ 82|   0.7%/ 92|   0.7%/106 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 130   |     194|      18.070|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 125   |    1501|      90.389|   3.5%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  95   |      40|       3.235|   1.1%/ 61|   1.1%/ 64|   1.1%/ 65|   1.0%/ 66 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  84   |      26|      16.385|   0.4%/180|   0.1%/528|   0.1%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 105   |     152|      13.131|   1.9%/ 37|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 115   |     908|      99.174|   2.6%/ 26|   2.2%/ 32|   2.0%/ 34|   1.9%/ 36 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 126   |     598|      61.173|   0.1%/762|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 130   |   26845|      19.721|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 130   |    4023|      15.072|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 150   |   13951|     167.324|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 137   |    3995|     102.091|   3.3%/ 21|   2.5%/ 28|   2.3%/ 30|   2.1%/ 33 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 130   |    1752|     355.924|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 120   |     388|      42.262|   1.4%/ 51|   1.6%/ 42|   1.7%/ 40|   1.8%/ 39 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 149   |   35055|     581.941|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 122   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 157   |     990|       7.858|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 114   |      10|       0.960|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 116   |     407|      21.769|   0.2%/396|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 115   |     222|       4.663|   2.7%/ 26|   3.0%/ 23|   3.1%/ 22|   3.2%/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 115   |     134|      74.788|   4.0%/ 17|   4.8%/ 14|   5.0%/ 14|   5.2%/ 13 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 106   |     408|      92.382|   0.8%/ 90|   0.7%/ 95|   0.7%/ 96|   0.7%/ 98 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 107   |     199|      30.404|   5.8%/ 12|   4.8%/ 14|   4.5%/ 15|   4.2%/ 16 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 107   |      31|      16.240|   0.3%/266|   0.4%/187|   0.4%/173|   0.4%/162 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 131   |      39|       5.706|   1.0%/ 73|   1.1%/ 63|   1.1%/ 60|   1.2%/ 58 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 106   |      57|      12.643|   6.1%/ 11|   8.6%/  8|   9.3%/  7|   9.9%/  7 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 108   |      50|       7.241|   0.9%/ 80|   4.8%/ 14|   3.8%/ 18|   3.7%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 120   |      79|      28.434|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  63   |      54|       2.055|   3.9%/ 17|   8.1%/  8|   9.2%/  7|  10.4%/  6 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 124   |     122|       3.726|   0.1%/ ***|   0.1%/ ***|   0.1%/985|   0.1%/943 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 112   |     122|       6.041|   0.2%/367|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 111   |     154|      37.890|   1.0%/ 72|   0.8%/ 83|   0.8%/ 86|   0.8%/ 90 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 122   |   39216|     309.817|   1.8%/ 38|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 123   |     690|     257.358|   1.2%/ 60|   1.0%/ 69|   1.0%/ 72|   0.9%/ 75 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 131   |     266|       7.401|   1.0%/ 67|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  55   |       9|       0.312|   1.6%/ 44|   0.8%/ 89|   0.7%/105|   0.6%/117 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  64   |      40|       1.345|   1.3%/ 52|   1.2%/ 56|   1.2%/ 58|   1.1%/ 60 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 135   |    6164|     353.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 112   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 114   |     101|      15.623|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 64 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 116   |      69|       3.086|   0.2%/449|   0.2%/382|   0.2%/365|   0.2%/349 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 118   |     799|       3.874|   1.5%/ 47|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 119   |     420|     202.104|   1.6%/ 43|   1.3%/ 53|   1.2%/ 57|   1.1%/ 60 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 127   |     254|      47.370|   0.1%/567|   0.1%/507|   0.1%/490|   0.1%/474 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 110   |     308|      66.117|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 122   |    5680|      25.898|   1.2%/ 56|   1.0%/ 70|   0.9%/ 75|   0.9%/ 81 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 130   |    1075|     254.821|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 120   |      28|       3.885|   3.1%/ 22|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 121   |   13087|     407.301|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 168   |    1613|      14.865|   0.9%/ 81|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 129   |    1628|      42.410|   0.5%/132|   0.4%/155|   0.4%/162|   0.4%/169 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 124   |    1694|     164.846|   0.4%/196|   0.3%/213|   0.3%/218|   0.3%/224 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 113   |     160|      58.377|   1.5%/ 47|   1.1%/ 64|   1.0%/ 71|   0.9%/ 80 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 119   |    2015|     103.851|   1.1%/ 64|   1.1%/ 65|   1.1%/ 66|   1.0%/ 66 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 122   |   12337|      84.072|   1.5%/ 47|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  50   |       5|       0.404|   5.2%/ 13|   2.9%/ 23|   2.3%/ 30|   1.8%/ 39 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 117   |    2512|      73.415|   2.0%/ 34|   1.7%/ 41|   1.6%/ 44|   1.5%/ 47 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 109   |     165|      10.177|   1.8%/ 39|   1.3%/ 54|   1.2%/ 60|   1.0%/ 66 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 121   |     461|      66.259|   3.0%/ 23|   3.4%/ 20|   3.5%/ 20|   3.6%/ 19 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  87   |      65|       8.194|   0.4%/180|   0.4%/193|   0.4%/193|   0.4%/192 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 120   |      27|       4.693|   0.3%/235|   0.4%/162|   0.5%/149|   0.5%/138 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 113   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 127   |     111|      53.111|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 102   |      93|       5.879|   0.1%/467|   0.1%/763|   0.1%/919|   0.1%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 114   |    5003|      85.129|   3.5%/ 20|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 138   |   28431|     603.632|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 113   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 128   |     683|      16.100|   0.7%/ 97|   0.6%/122|   0.5%/131|   0.5%/141 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 130   |    5633|     544.879|   0.3%/251|   0.2%/294|   0.2%/306|   0.2%/319 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 136   |    1970|     228.954|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 112   |      25|       1.432|   4.6%/ 15|   5.0%/ 14|   6.0%/ 11|   4.4%/ 16 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 110   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 140   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 114   |      15|       2.021|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 116   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 122   |      50|       4.265|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 124   |    5478|      65.881|   0.4%/192|   0.4%/193|   0.4%/193|   0.4%/193 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 141   |  139747|     424.063|   0.5%/126|   0.6%/126|   0.6%/125|   0.6%/125 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 128   |    1513|      36.126|   1.3%/ 53|   1.2%/ 58|   1.2%/ 59|   1.1%/ 61 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 121   |     340|      34.342|   0.4%/193|   0.3%/225|   0.3%/236|   0.3%/248 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 130   |   45427|     683.776|   0.2%/380|   0.2%/427|   0.2%/439|   0.2%/453 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 112   |      32|       9.196|   1.1%/ 63|   1.2%/ 57|   1.2%/ 55|   1.3%/ 54 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 114   |      88|       2.578|   6.6%/ 10|   6.5%/ 11|   6.4%/ 11|   6.4%/ 11 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 114   |     115|       3.557|   4.2%/ 16|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 108   |      51|       2.833|   9.4%/  7|  13.1%/  5|  14.0%/  5|  15.1%/  4 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 118   |      26|       1.710|   8.9%/  8|  10.4%/  7|  10.8%/  6|  11.1%/  6 |

