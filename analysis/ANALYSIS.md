# State and Country COVID-19 Analysis #
## Updated: at 2020-08-05 for data as of 2020-08-04 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.4% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

![Deaths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeaths.png)

![Daily Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/4LargestDeathsPerDay.png)

Despite quite large rhetorical, political, and social differences in their approaches to the pandemic, the rates of death in these four states appear to be converging.  Deaths in Florida and California have followed nearly identical trajectories since early April 2020 with Florida somewhat higher, but both falling well below New York and above Texas.


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


# Ten US States with Highest Death Tolls #

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.6% of deaths and 55.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 126   |   32752|    1683.589|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 126   |   15876|    1787.400|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 126   |    9639|     243.958|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 126   |    8663|    1246.626|   0.2%/399|   0.2%/405|   0.2%/406|   0.2%/407 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 126   |    7746|     611.286|   0.2%/341|   0.2%/351|   0.2%/353|   0.2%/356 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 126   |    7391|     344.138|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 126   |    7467|     257.522|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 126   |    7259|     567.011|   0.2%/372|   0.2%/425|   0.2%/441|   0.2%/458 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 126   |    6472|     648.020|   0.1%/670|   0.1%/701|   0.1%/707|   0.1%/712 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 126   |    4442|    1245.959|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 126   |  156762|     475.695|   0.7%/102|   0.7%/ 98|   0.7%/ 98|   0.7%/ 97 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 126   |   96740|     457.592|   1.1%/ 60|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 126   |   49340|     389.797|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 60 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 126   |   46404|     698.487|   0.1%/546|   0.1%/605|   0.1%/622|   0.1%/640 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 126   |   40092|      29.453|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 126   |   35178|     583.982|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 126   |   30293|     451.628|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 126   |   28463|     604.302|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 126   |   20669|     643.253|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 126   |   17726|     212.603|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 126   |    1689|     344.458|   1.5%/ 45|   1.4%/ 49|   1.4%/ 51|   1.3%/ 52 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 126   |      25|      33.968|   2.4%/ 28|   3.0%/ 23|   3.2%/ 22|   3.3%/ 21 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 126   |    4017|     551.839|   2.1%/ 34|   1.7%/ 41|   1.6%/ 44|   1.5%/ 47 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 126   |     483|     160.044|   1.9%/ 36|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 126   |    9639|     243.958|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 126   |    1853|     321.763|   0.3%/215|   0.3%/210|   0.3%/209|   0.3%/208 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 126   |    4442|    1245.959|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 126   |     599|     615.231|   0.2%/451|   0.1%/472|   0.1%/478|   0.1%/485 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 126   |    7391|     344.138|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 126   |    3913|     368.499|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 126   |      27|      19.137|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 126   |     207|     116.084|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 126   |    7746|     611.286|   0.2%/341|   0.2%/351|   0.2%/353|   0.2%/356 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 126   |    2999|     445.472|   0.4%/195|   0.3%/198|   0.3%/199|   0.3%/201 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 126   |     891|     282.351|   0.7%/ 99|   0.7%/100|   0.7%/101|   0.7%/101 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 126   |     368|     126.411|   1.0%/ 68|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 126   |     755|     169.053|   0.7%/ 93|   0.7%/ 99|   0.7%/101|   0.7%/103 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 126   |    4054|     872.022|   0.8%/ 86|   0.9%/ 79|   0.9%/ 77|   0.9%/ 76 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 126   |     124|      92.291|   0.4%/183|   0.4%/195|   0.3%/198|   0.3%/201 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 126   |    3532|     584.178|   0.3%/245|   0.3%/240|   0.3%/239|   0.3%/238 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 126   |    8663|    1246.626|   0.2%/399|   0.2%/405|   0.2%/406|   0.2%/407 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 126   |    6472|     648.020|   0.1%/670|   0.1%/701|   0.1%/707|   0.1%/712 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 126   |    1661|     294.533|   0.3%/215|   0.3%/216|   0.3%/216|   0.3%/216 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 126   |    1737|     583.788|   1.6%/ 43|   1.7%/ 40|   1.7%/ 39|   1.8%/ 39 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 126   |    1297|     211.271|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 126   |      65|      61.070|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 126   |     336|     173.766|   0.5%/131|   0.4%/165|   0.4%/177|   0.4%/191 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 126   |     864|     280.648|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 126   |     420|     308.585|   0.3%/232|   0.3%/243|   0.3%/247|   0.3%/251 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 126   |   15876|    1787.400|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 126   |     664|     316.484|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80|   0.9%/ 81 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 126   |   32752|    1683.589|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 126   |    2050|     195.489|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 126   |     107|     140.492|   0.9%/ 78|   0.9%/ 81|   0.8%/ 82|   0.8%/ 83 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 126   |    3569|     305.322|   0.8%/ 91|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 126   |     564|     142.557|   1.3%/ 53|   1.4%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 126   |     336|      79.750|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 126   |    7259|     567.011|   0.2%/372|   0.2%/425|   0.2%/441|   0.2%/458 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 126   |     234|      73.121|   1.8%/ 39|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 126   |    1013|     955.926|   0.1%/686|   0.1%/989|   0.1%/ ***|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 126   |    1909|     370.837|   2.8%/ 25|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 126   |     136|     153.430|   1.0%/ 67|   1.1%/ 65|   1.1%/ 64|   1.1%/ 63 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 126   |    1127|     164.957|   1.7%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 126   |    7467|     257.522|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 126   |  156762|     475.695|   0.7%/102|   0.7%/ 98|   0.7%/ 98|   0.7%/ 97 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 126   |     324|     100.949|   1.6%/ 42|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 126   |      57|      91.129|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 126   |    2217|     259.762|   0.7%/104|   0.8%/ 89|   0.8%/ 86|   0.8%/ 83 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 126   |    1611|     211.562|   0.7%/101|   0.7%/ 95|   0.7%/ 94|   0.8%/ 92 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 126   |     118|      65.677|   1.3%/ 53|   1.6%/ 42|   1.7%/ 40|   1.8%/ 38 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 126   |     957|     164.391|   0.8%/ 87|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 114   |      27|      46.484|   0.7%/106|   0.6%/120|   0.6%/123|   0.5%/126 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 126   |    1331|      41.293|   0.6%/117|   0.2%/371|   0.1%/802|   0.0%/ -- |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 126   |     177|      62.120|   2.8%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 126   |    1254|      29.171|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78|   0.9%/ 78 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 126   |      60|       1.923|   6.3%/ 11|   2.5%/ 27|   3.7%/ 19|   3.0%/ 23 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 126   |    3992|      88.842|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 126   |     781|     263.964|   1.1%/ 62|   0.9%/ 79|   0.8%/ 84|   0.8%/ 90 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 126   |     232|       9.038|   4.7%/ 15|   5.5%/ 12|   5.7%/ 12|   6.0%/ 11 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 126   |     719|      80.707|   0.1%/936|   0.1%/832|   0.1%/808|   0.1%/785 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 126   |     485|      48.200|   1.7%/ 40|   1.5%/ 47|   1.4%/ 49|   1.3%/ 51 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 126   |     155|     100.149|   1.1%/ 64|   0.8%/ 88|   0.7%/ 97|   0.6%/108 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 126   |    3279|      19.463|   1.2%/ 55|   1.1%/ 63|   1.1%/ 66|   1.0%/ 68 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 126   |     579|      61.497|   0.9%/ 79|   0.8%/ 85|   0.8%/ 87|   0.8%/ 88 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 126   |    9853|     854.926|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 121   |      38|       3.271|   0.7%/ 98|   0.1%/481|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 126   |    3308|     288.381|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 126   |     365|     110.533|   2.3%/ 30|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 126   |       1|       0.428|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 126   |   96740|     457.592|   1.1%/ 60|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 126   |     407|      58.595|   1.9%/ 36|   2.0%/ 34|   2.0%/ 34|   2.1%/ 34 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 126   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 114   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 126   |     397|      14.949|   0.2%/284|   0.1%/596|   0.1%/846|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 126   |    9006|     237.011|   0.1%/899|   0.1%/974|   0.1%/993|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  74   |      59|      10.778|   0.3%/206|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  99   |      75|       4.617|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 126   |   10029|     524.867|   0.9%/ 81|   0.8%/ 87|   0.8%/ 89|   0.8%/ 91 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 126   |    4664|       3.326|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 126   |   11404|     230.861|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 126   |     200|      39.577|   7.1%/ 10|   6.3%/ 11|   6.1%/ 11|   5.9%/ 12 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 126   |     152|      37.374|   1.4%/ 49|   1.7%/ 42|   1.7%/ 40|   1.8%/ 39 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 126   |      87|       7.776|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 126   |     616|     105.770|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 126   |    1212|     116.978|   1.4%/ 51|   1.3%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 126   |    5823|     333.340|   0.6%/125|   0.5%/138|   0.5%/141|   0.5%/145 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 126   |    4998|      49.840|   0.8%/ 83|   0.6%/113|   0.6%/124|   0.5%/136 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 126   |     499|      76.857|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 105   |      78|      57.113|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 122   |     331|       3.353|   4.9%/ 14|   5.4%/ 13|   5.5%/ 12|   5.6%/ 12 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 126   |     329|      59.599|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 126   |   30293|     451.628|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 126   |      51|      23.348|   0.6%/123|   0.7%/104|   0.7%/100|   0.7%/ 97 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 126   |      11|       4.851|   6.8%/ 10|   7.2%/  9|   7.3%/  9|   7.4%/  9 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 123   |      17|       4.626|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 126   |    9162|     110.186|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 126   |     190|       6.288|   1.6%/ 43|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 126   |     209|      19.467|   0.4%/170|   0.5%/145|   0.5%/140|   0.5%/135 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 126   |    2085|     125.597|   2.0%/ 34|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 112   |      48|       3.926|   0.9%/ 73|   0.8%/ 86|   0.8%/ 91|   0.7%/ 96 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 101   |      27|      16.664|   0.3%/210|   0.6%/125|   0.6%/113|   0.7%/102 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 122   |     168|      14.477|   0.7%/ 95|   0.6%/112|   0.6%/117|   0.6%/122 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 126   |    1462|     159.636|   2.7%/ 25|   2.6%/ 26|   2.6%/ 27|   2.6%/ 27 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 126   |     597|      61.096|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 126   |   40092|      29.453|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 126   |    5511|      20.648|   1.5%/ 45|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 126   |   17726|     212.603|   1.3%/ 52|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 126   |    5130|     131.102|   1.7%/ 40|   1.4%/ 49|   1.3%/ 51|   1.3%/ 54 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 126   |    1767|     359.036|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 126   |     555|      60.433|   2.0%/ 34|   2.1%/ 33|   2.1%/ 32|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 126   |   35178|     583.982|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 126   |      10|       3.667|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 126   |    1016|       8.064|   0.2%/310|   0.3%/247|   0.3%/235|   0.3%/224 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 126   |      11|       1.050|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 126   |     955|      51.131|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 126   |     385|       8.088|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 126   |     258|     143.796|   4.4%/ 16|   4.5%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 123   |     464|     104.976|   0.8%/ 86|   0.8%/ 82|   0.8%/ 82|   0.9%/ 81 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 124   |    1632|     249.747|   2.1%/ 34|   1.1%/ 64|   0.8%/ 83|   0.6%/119 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 124   |      32|      16.684|   0.3%/273|   0.3%/221|   0.3%/208|   0.4%/196 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 126   |      65|       9.568|   2.9%/ 24|   3.4%/ 21|   3.5%/ 20|   3.6%/ 19 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 123   |      81|      18.049|   0.8%/ 84|   0.9%/ 75|   1.0%/ 73|   1.0%/ 70 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 125   |      90|      13.073|   8.2%/  8|   4.4%/ 16|   7.9%/  9|   6.3%/ 11 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 126   |      80|      28.709|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  80   |     126|       4.786|   4.7%/ 15|   4.1%/ 17|   3.9%/ 18|   3.7%/ 19 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 126   |     125|       3.821|   0.1%/529|   0.1%/503|   0.1%/497|   0.1%/492 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 126   |     125|       6.155|   0.1%/653|   0.1%/868|   0.1%/965|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 126   |     159|      38.892|   0.1%/515|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 126   |   49340|     389.797|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 60 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 126   |     809|     301.780|   1.0%/ 69|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 126   |     362|      10.095|   2.7%/ 26|   3.2%/ 22|   3.3%/ 21|   3.5%/ 20 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  72   |      13|       0.439|   1.8%/ 39|   4.6%/ 15|   5.4%/ 13|   6.2%/ 11 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  26   |      12|       4.941|   5.2%/ 13|   5.2%/ 13|   4.4%/ 16|   3.7%/ 18 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  81   |      59|       1.980|   2.6%/ 26|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 126   |    6169|     353.373|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 126   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 126   |     121|      18.727|   1.0%/ 72|   0.8%/ 81|   0.8%/ 84|   0.8%/ 87 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 126   |      69|       3.097|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 126   |     916|       4.444|   0.8%/ 90|   0.6%/115|   0.6%/123|   0.5%/133 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 126   |     511|     246.198|   1.1%/ 61|   1.0%/ 70|   1.0%/ 72|   0.9%/ 75 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 126   |     256|      47.642|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 126   |     457|      97.883|   1.7%/ 41|   1.1%/ 64|   0.9%/ 75|   0.8%/ 91 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 126   |    6074|      27.693|   0.4%/165|   0.3%/261|   0.2%/304|   0.2%/364 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 126   |    1558|     369.345|   2.0%/ 34|   1.8%/ 39|   1.7%/ 40|   1.6%/ 42 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 126   |      58|       8.134|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 126   |   20669|     643.253|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 126   |    2130|      19.633|   1.0%/ 67|   1.1%/ 64|   1.1%/ 63|   1.1%/ 61 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 126   |    1741|      45.370|   0.4%/156|   0.4%/156|   0.4%/156|   0.4%/156 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 126   |    1746|     169.929|   0.2%/389|   0.1%/486|   0.1%/518|   0.1%/555 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 126   |     178|      64.914|   0.8%/ 85|   0.8%/ 90|   0.8%/ 90|   0.8%/ 91 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 126   |    2451|     126.289|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 126   |   14456|      98.514|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 92 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  67   |       5|       0.404|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 126   |    3020|      88.266|   1.1%/ 63|   0.9%/ 75|   0.9%/ 79|   0.8%/ 84 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 126   |     219|      13.511|   1.5%/ 46|   1.4%/ 51|   1.3%/ 53|   1.3%/ 55 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 126   |     617|      88.636|   1.6%/ 44|   1.3%/ 53|   1.2%/ 56|   1.2%/ 59 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 104   |      67|       8.518|   0.2%/421|   0.1%/816|   0.1%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 126   |      27|       4.748|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 126   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 126   |     121|      57.713|   0.5%/136|   0.7%/106|   0.7%/100|   0.7%/ 95 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 119   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 126   |    9132|     155.371|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 126   |   28463|     604.302|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 126   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 126   |     761|      17.936|   0.6%/107|   0.6%/111|   0.6%/112|   0.6%/113 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 126   |    5773|     558.385|   0.1%/559|   0.1%/861|   0.1%/998|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 126   |    1983|     230.456|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 126   |      51|       2.887|   1.7%/ 40|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 126   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 126   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 126   |      19|       2.585|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 126   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 126   |      51|       4.317|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 126   |    5766|      69.338|   0.3%/230|   0.3%/237|   0.3%/239|   0.3%/241 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 126   |  156762|     475.695|   0.7%/102|   0.7%/ 98|   0.7%/ 98|   0.7%/ 97 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  12   |       5|       0.124|   0.0%/ --|  26.0%/  2|  18.6%/  4|   7.7%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 126   |    1786|      42.653|   1.1%/ 65|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 126   |     353|      35.656|   0.2%/305|   0.2%/342|   0.2%/352|   0.2%/364 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 126   |   46404|     698.487|   0.1%/546|   0.1%/605|   0.1%/622|   0.1%/640 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 126   |      37|      10.374|   0.7%/ 99|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 126   |     167|       4.895|   4.0%/ 17|   3.7%/ 19|   3.6%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 126   |     187|       5.799|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 125   |     185|      10.325|   3.8%/ 18|   1.2%/ 58|   0.5%/126|   0.0%/ -- |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 126   |      75|       4.976|   8.5%/  8|   9.6%/  7|   9.9%/  7|  10.2%/  7 |

