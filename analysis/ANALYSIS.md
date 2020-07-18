# State and Country COVID-19 Analysis #
## Updated: at 2020-07-18 for data as of 2020-07-17 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.0% of deaths and 39.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 70.4% of deaths and 57.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 126   |   32611|    1676.359|   0.1%/899|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 130   |   15844|    1783.815|   0.2%/278|   0.2%/280|   0.2%/281|   0.2%/282 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 120   |    8414|    1210.665|   0.2%/313|   0.2%/349|   0.2%/359|   0.2%/370 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |    7523|     190.388|   1.3%/ 51|   1.4%/ 48|   1.5%/ 48|   1.5%/ 47 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 123   |    7530|     594.244|   0.4%/177|   0.4%/197|   0.3%/203|   0.3%/211 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 121   |    7006|     547.279|   0.3%/235|   0.3%/248|   0.3%/251|   0.3%/254 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 121   |    6359|     636.688|   0.2%/427|   0.2%/435|   0.2%/438|   0.2%/440 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 132   |    4601|     214.225|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 121   |    4384|    1229.531|   0.1%/639|   0.1%/575|   0.1%/557|   0.1%/538 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 123   |    3599|     124.110|   2.7%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 140   |  138963|     421.684|   0.5%/129|   0.5%/130|   0.5%/130|   0.5%/130 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 123   |   78069|     369.275|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 129   |   45360|     682.773|   0.2%/372|   0.2%/420|   0.2%/434|   0.2%/448 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 121   |   38604|     304.979|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 148   |   35044|     581.748|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 154   |   30126|     449.136|   0.1%/ ***|   0.1%/ ***|   0.1%/989|   0.1%/976 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 137   |   28435|     603.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 129   |   26212|      19.256|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 149   |   13745|     164.856|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 120   |   12901|     401.517|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 115   |    1227|     250.147|   1.8%/ 38|   2.1%/ 33|   2.2%/ 32|   2.2%/ 31 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 115   |      18|      24.396|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 119   |    2515|     345.485|   2.8%/ 25|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 116   |     348|     115.196|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |    7523|     190.388|   1.3%/ 51|   1.4%/ 48|   1.5%/ 48|   1.5%/ 47 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 126   |    1745|     303.056|   0.2%/291|   0.3%/265|   0.3%/258|   0.3%/251 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 121   |    4384|    1229.531|   0.1%/639|   0.1%/575|   0.1%/557|   0.1%/538 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 114   |     521|     535.441|   0.2%/459|   0.2%/430|   0.2%/424|   0.2%/418 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 132   |    4601|     214.225|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 128   |    3105|     292.462|   0.7%/101|   0.8%/ 92|   0.8%/ 90|   0.8%/ 88 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 109   |      23|      15.980|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 114   |     106|      59.456|   1.1%/ 65|   1.3%/ 52|   1.4%/ 49|   1.5%/ 47 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 123   |    7530|     594.244|   0.4%/177|   0.4%/197|   0.3%/203|   0.3%/211 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 124   |    2810|     417.426|   0.3%/205|   0.3%/225|   0.3%/231|   0.3%/238 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 115   |     776|     245.934|   0.7%/106|   0.8%/ 87|   0.8%/ 83|   0.9%/ 80 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 127   |     307|     105.431|   0.7%/105|   0.6%/109|   0.6%/111|   0.6%/112 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 124   |     654|     146.429|   0.9%/ 78|   0.9%/ 75|   0.9%/ 75|   0.9%/ 74 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 126   |    3493|     751.391|   0.5%/138|   0.5%/128|   0.5%/126|   0.6%/124 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 113   |     116|      86.069|   0.5%/136|   0.5%/145|   0.5%/149|   0.5%/153 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 121   |    3368|     557.040|   0.3%/238|   0.3%/273|   0.2%/284|   0.2%/296 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 120   |    8414|    1210.665|   0.2%/313|   0.2%/349|   0.2%/359|   0.2%/370 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 121   |    6359|     636.688|   0.2%/427|   0.2%/435|   0.2%/438|   0.2%/440 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 119   |    1571|     278.527|   0.4%/191|   0.3%/206|   0.3%/210|   0.3%/213 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 121   |    1323|     444.426|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 121   |    1130|     184.120|   0.6%/116|   0.6%/118|   0.6%/119|   0.6%/120 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 113   |      35|      33.105|   3.1%/ 22|   4.1%/ 17|   4.3%/ 16|   4.6%/ 15 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 112   |     295|     152.754|   0.5%/132|   0.5%/133|   0.5%/132|   0.5%/130 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 124   |     629|     204.123|   1.3%/ 51|   1.5%/ 45|   1.6%/ 44|   1.6%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 117   |     399|     293.177|   0.3%/199|   0.2%/324|   0.2%/381|   0.1%/462 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 130   |   15844|    1783.815|   0.2%/278|   0.2%/280|   0.2%/281|   0.2%/282 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 115   |     565|     269.423|   0.8%/ 91|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 126   |   32611|    1676.359|   0.1%/899|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 115   |    1604|     152.968|   1.0%/ 67|   1.2%/ 60|   1.2%/ 58|   1.2%/ 56 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 113   |      90|     117.826|   0.7%/ 95|   0.8%/ 85|   0.8%/ 83|   0.8%/ 82 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 120   |    3126|     267.469|   0.5%/138|   0.5%/150|   0.4%/154|   0.4%/158 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 121   |     438|     110.736|   0.8%/ 84|   0.9%/ 75|   0.9%/ 73|   1.0%/ 71 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 125   |     250|      59.328|   1.3%/ 54|   1.4%/ 48|   1.5%/ 47|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 121   |    7006|     547.279|   0.3%/235|   0.3%/248|   0.3%/251|   0.3%/254 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 119   |     172|      53.914|   0.9%/ 77|   1.1%/ 61|   1.2%/ 58|   1.3%/ 55 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 112   |     993|     937.680|   0.3%/272|   0.2%/379|   0.2%/416|   0.2%/460 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 124   |    1065|     206.874|   2.2%/ 31|   2.4%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 129   |     115|     129.773|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 119   |     808|     118.295|   1.8%/ 38|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 123   |    3599|     124.110|   2.7%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 140   |  138963|     421.684|   0.5%/129|   0.5%/130|   0.5%/130|   0.5%/130 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 118   |     236|      73.708|   2.0%/ 34|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 120   |      56|      89.745|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 126   |    2041|     239.098|   0.7%/ 97|   0.6%/117|   0.6%/124|   0.5%/132 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 140   |    1445|     189.808|   0.5%/150|   0.4%/162|   0.4%/165|   0.4%/170 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 110   |      99|      54.980|   0.4%/154|   0.6%/119|   0.6%/112|   0.7%/106 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 120   |     835|     143.409|   0.4%/193|   0.3%/219|   0.3%/226|   0.3%/233 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)|  96   |      23|      39.312|   0.5%/142|   0.7%/ 93|   0.8%/ 85|   0.9%/ 78 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 118   |    1145|      35.523|   2.4%/ 28|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 129   |     110|      38.506|   3.2%/ 21|   2.9%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 128   |    1057|      24.575|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 111   |      29|       0.947|   3.1%/ 22|   1.3%/ 55|   2.5%/ 28|   3.7%/ 19 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 132   |    2164|      48.165|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 114   |     621|     209.987|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 139   |     111|       4.310|   0.8%/ 91|   1.0%/ 69|   1.1%/ 65|   1.1%/ 61 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 128   |     711|      79.872|   0.1%/990|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 127   |     351|      34.904|   2.7%/ 25|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 124   |     122|      78.885|   2.2%/ 32|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 122   |    2590|      15.373|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 109   |     494|      52.542|   1.3%/ 54|   1.2%/ 59|   1.1%/ 60|   1.1%/ 62 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 129   |    9801|     850.454|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 103   |      29|       2.454|   2.7%/ 25|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 111   |    2129|     185.580|   3.3%/ 21|   2.7%/ 25|   2.6%/ 27|   2.4%/ 29 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 119   |     241|      72.983|   1.7%/ 41|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 109   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 123   |   78069|     369.275|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 129   |     296|      42.514|   1.6%/ 43|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 122   |      53|       2.540|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)|  96   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 115   |     376|      14.162|   0.7%/105|   0.8%/ 90|   0.8%/ 88|   0.8%/ 86 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 131   |    8903|     234.306|   0.1%/476|   0.1%/594|   0.1%/632|   0.1%/676 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  56   |      53|       9.679|   0.7%/ 99|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  81   |      75|       4.624|   0.1%/622|   0.2%/442|   0.2%/413|   0.2%/389 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 118   |    7632|     399.405|   1.4%/ 49|   1.0%/ 68|   0.9%/ 75|   0.8%/ 84 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 129   |    4641|       3.310|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 118   |    6491|     131.399|   3.7%/ 19|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 121   |      43|       8.440|   6.8%/ 10|   7.2%/  9|   7.3%/  9|   7.4%/  9 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 121   |     121|      29.796|   0.6%/120|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 122   |      87|       7.767|   0.1%/800|   0.1%/786|   0.1%/777|   0.1%/768 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 126   |     611|     104.949|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 123   |     952|      91.868|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 126   |    5263|     301.307|   0.8%/ 84|   0.8%/ 88|   0.8%/ 89|   0.8%/ 90 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 132   |    4320|      43.081|   2.0%/ 35|   1.6%/ 42|   1.6%/ 44|   1.5%/ 47 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 109   |     312|      48.086|   3.3%/ 21|   2.6%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  87   |      52|      38.123|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 104   |     147|       1.493|   2.8%/ 25|   3.4%/ 20|   3.5%/ 19|   3.7%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 119   |     329|      59.478|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 154   |   30126|     449.136|   0.1%/ ***|   0.1%/ ***|   0.1%/989|   0.1%/976 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 120   |      47|      21.834|   0.4%/170|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 117   |       3|       1.412|   2.1%/ 32|   1.6%/ 42|   1.5%/ 47|   1.3%/ 54 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 105   |      15|       4.039|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 131   |    9102|     109.460|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 119   |     147|       4.838|   1.3%/ 55|   0.8%/ 88|   0.7%/103|   0.6%/125 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 129   |     194|      18.057|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 124   |    1461|      87.972|   3.7%/ 19|   3.5%/ 20|   3.5%/ 20|   3.4%/ 20 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  94   |      39|       3.208|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  83   |      26|      16.381|   0.5%/150|   0.2%/383|   0.1%/619|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 104   |     150|      12.973|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 114   |     891|      97.253|   2.7%/ 26|   2.2%/ 32|   2.0%/ 34|   1.9%/ 37 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 125   |     598|      61.153|   0.1%/697|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 129   |   26212|      19.256|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 129   |    3950|      14.799|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 149   |   13745|     164.856|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 136   |    3921|     100.199|   3.5%/ 20|   2.6%/ 26|   2.4%/ 29|   2.2%/ 31 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 129   |    1751|     355.735|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 119   |     381|      41.522|   1.2%/ 55|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 148   |   35044|     581.748|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 121   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 156   |     990|       7.859|   0.1%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 113   |      10|       0.959|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 115   |     399|      21.379|   0.2%/336|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 114   |     215|       4.524|   2.6%/ 26|   3.1%/ 23|   3.2%/ 22|   3.3%/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 114   |     129|      71.924|   5.8%/ 12|   7.2%/  9|   7.6%/  9|   7.9%/  9 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 105   |     406|      91.752|   0.8%/ 88|   0.8%/ 92|   0.7%/ 93|   0.7%/ 95 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 106   |     188|      28.764|   6.1%/ 11|   5.1%/ 14|   4.8%/ 14|   4.5%/ 15 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 106   |      31|      16.180|   0.3%/250|   0.4%/164|   0.5%/150|   0.5%/137 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 130   |      38|       5.622|   0.8%/ 88|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 105   |      55|      12.222|   4.9%/ 14|   6.9%/ 10|   7.4%/  9|   8.0%/  9 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 107   |      48|       7.035|   1.8%/ 38|   3.3%/ 21|   4.8%/ 14|   3.8%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 119   |      79|      28.373|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  62   |      43|       1.635|   2.9%/ 24|   7.5%/  9|   8.8%/  8|  10.2%/  7 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 123   |     122|       3.724|   0.1%/ ***|   0.1%/907|   0.1%/854|   0.1%/808 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 111   |     122|       6.040|   0.2%/311|   0.1%/880|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 110   |     153|      37.574|   1.0%/ 71|   0.9%/ 81|   0.8%/ 84|   0.8%/ 89 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 121   |   38604|     304.979|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 122   |     684|     255.118|   1.2%/ 58|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 130   |     262|       7.310|   1.0%/ 70|   1.1%/ 63|   1.1%/ 62|   1.2%/ 60 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  54   |       9|       0.302|   2.0%/ 34|   0.2%/450|   0.0%/ --|   0.0%/ -- |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  63   |      40|       1.332|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 134   |    6165|     353.157|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 111   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 113   |     100|      15.493|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 115   |      69|       3.080|   0.2%/413|   0.2%/330|   0.2%/313|   0.2%/296 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 117   |     790|       3.833|   1.6%/ 44|   1.5%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 118   |     415|     199.749|   1.6%/ 43|   1.3%/ 54|   1.2%/ 58|   1.1%/ 63 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 126   |     254|      47.298|   0.1%/649|   0.1%/615|   0.1%/603|   0.1%/589 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 109   |     300|      64.273|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 121   |    5632|      25.679|   1.3%/ 53|   1.0%/ 66|   1.0%/ 70|   0.9%/ 75 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 129   |    1045|     247.785|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 119   |      27|       3.738|   2.8%/ 24|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 120   |   12901|     401.517|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 167   |    1427|      13.148|   0.8%/ 82|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 128   |    1621|      42.245|   0.5%/129|   0.4%/154|   0.4%/162|   0.4%/170 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 123   |    1689|     164.401|   0.4%/184|   0.4%/191|   0.4%/193|   0.4%/196 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 112   |     159|      57.955|   1.6%/ 43|   1.3%/ 55|   1.2%/ 59|   1.1%/ 64 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 118   |    1995|     102.800|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 121   |   12179|      82.991|   1.5%/ 46|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  49   |       4|       0.323|   5.0%/ 14|   2.1%/ 33|   0.8%/ 88|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 116   |    2477|      72.400|   2.1%/ 33|   1.7%/ 40|   1.6%/ 42|   1.5%/ 45 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 108   |     163|      10.060|   1.8%/ 38|   1.2%/ 57|   1.1%/ 65|   0.9%/ 76 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 120   |     447|      64.138|   3.0%/ 23|   3.5%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  86   |      64|       8.160|   0.4%/183|   0.3%/214|   0.3%/220|   0.3%/224 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 119   |      27|       4.673|   0.3%/218|   0.5%/144|   0.5%/132|   0.6%/121 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 112   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 126   |     111|      53.139|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 101   |      93|       5.877|   0.2%/413|   0.1%/546|   0.1%/600|   0.1%/670 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 113   |    4847|      82.470|   3.5%/ 20|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 137   |   28435|     603.706|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 112   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 127   |     680|      16.013|   0.8%/ 90|   0.6%/109|   0.6%/115|   0.6%/122 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 129   |    5622|     543.804|   0.3%/249|   0.2%/299|   0.2%/314|   0.2%/330 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 135   |    1970|     228.928|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 111   |      24|       1.354|   4.6%/ 15|  11.2%/  6|   5.0%/ 14|   6.0%/ 11 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 109   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 139   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 113   |      15|       2.025|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 115   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 121   |      50|       4.265|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 123   |    5459|      65.650|   0.4%/191|   0.4%/192|   0.4%/192|   0.4%/193 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 140   |  138963|     421.684|   0.5%/129|   0.5%/130|   0.5%/130|   0.5%/130 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 127   |    1495|      35.705|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 120   |     339|      34.245|   0.4%/187|   0.3%/216|   0.3%/225|   0.3%/235 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 129   |   45360|     682.773|   0.2%/372|   0.2%/420|   0.2%/434|   0.2%/448 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 111   |      32|       9.065|   1.0%/ 71|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 113   |      83|       2.430|   6.8%/ 10|   6.9%/ 10|   6.9%/ 10|   6.9%/ 10 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 113   |     111|       3.442|   4.4%/ 16|   4.0%/ 17|   3.9%/ 18|   3.8%/ 18 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 107   |      49|       2.743|   6.0%/ 11|   6.9%/ 10|   7.2%/  9|   7.5%/  9 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 117   |      24|       1.609|   8.8%/  8|  10.6%/  6|  11.1%/  6|  11.5%/  6 |

