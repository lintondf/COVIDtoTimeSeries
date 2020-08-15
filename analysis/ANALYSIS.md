# State and Country COVID-19 Analysis #
## Updated: at 2020-08-15 for data as of 2020-08-14 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.5% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.9% of deaths and 58.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 136   |   32833|    1687.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15908|    1791.010|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |   11103|     280.995|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 136   |   10588|     365.143|   2.2%/ 31|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    9237|     430.051|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 136   |    8804|    1266.883|   0.2%/420|   0.2%/427|   0.2%/428|   0.2%/430 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 136   |    7925|     625.394|   0.2%/317|   0.2%/316|   0.2%/316|   0.2%/316 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 136   |    7399|     577.931|   0.2%/312|   0.2%/292|   0.2%/287|   0.2%/282 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 136   |    6560|     656.905|   0.1%/552|   0.1%/528|   0.1%/523|   0.1%/519 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 136   |    4533|     426.895|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  168584|     511.566|   0.7%/ 99|   0.7%/100|   0.7%/100|   0.7%/101 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 136   |  106716|     504.776|   1.0%/ 68|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 136   |   56076|     443.015|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   49379|      36.276|   2.1%/ 32|   2.1%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   46894|     705.856|   0.1%/656|   0.1%/739|   0.1%/765|   0.1%/792 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   35239|     584.992|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   30384|     452.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28580|     606.793|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 136   |   23317|     725.677|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   19595|     235.019|   1.0%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 136   |    1919|     391.413|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 136   |      28|      38.447|   1.3%/ 51|   1.2%/ 55|   1.2%/ 57|   1.2%/ 58 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 136   |    4526|     621.785|   1.5%/ 47|   1.2%/ 56|   1.2%/ 59|   1.1%/ 63 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 136   |     597|     197.893|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |   11103|     280.995|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 136   |    1889|     328.096|   0.2%/301|   0.2%/343|   0.2%/356|   0.2%/369 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 136   |    4453|    1249.059|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 136   |     601|     617.380|   0.1%/564|   0.1%/628|   0.1%/646|   0.1%/665 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    9237|     430.051|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 136   |    4533|     426.895|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 136   |      31|      21.711|   2.9%/ 23|   3.8%/ 18|   4.1%/ 17|   4.3%/ 16 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 136   |     275|     153.992|   2.3%/ 30|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 136   |    7925|     625.394|   0.2%/317|   0.2%/316|   0.2%/316|   0.2%/316 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 136   |    3104|     461.081|   0.4%/183|   0.4%/178|   0.4%/176|   0.4%/174 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 136   |     967|     306.489|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83|   0.8%/ 83 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 136   |     406|     139.232|   1.0%/ 71|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 136   |     802|     179.608|   0.7%/102|   0.6%/106|   0.6%/107|   0.6%/108 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 136   |    4436|     954.271|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 136   |     127|      94.446|   0.3%/277|   0.2%/347|   0.2%/371|   0.2%/398 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 136   |    3633|     600.968|   0.3%/250|   0.3%/253|   0.3%/254|   0.3%/255 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 136   |    8804|    1266.883|   0.2%/420|   0.2%/427|   0.2%/428|   0.2%/430 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 136   |    6560|     656.905|   0.1%/552|   0.1%/528|   0.1%/523|   0.1%/519 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 136   |    1729|     306.660|   0.4%/164|   0.5%/149|   0.5%/145|   0.5%/142 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 136   |    2056|     690.721|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 136   |    1377|     224.361|   0.6%/117|   0.5%/133|   0.5%/138|   0.5%/144 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 136   |      85|      79.957|   2.6%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 136   |     359|     185.468|   0.7%/ 97|   0.8%/ 91|   0.8%/ 90|   0.8%/ 88 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 136   |    1041|     338.021|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 136   |     424|     311.761|   0.1%/481|   0.1%/760|   0.1%/887|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15908|    1791.010|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 136   |     710|     338.553|   0.7%/105|   0.6%/121|   0.5%/127|   0.5%/132 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 136   |   32833|    1687.763|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 136   |    2335|     222.663|   1.3%/ 55|   1.2%/ 57|   1.2%/ 57|   1.2%/ 58 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 136   |     119|     156.802|   1.2%/ 58|   1.3%/ 53|   1.3%/ 51|   1.4%/ 50 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 136   |    3802|     325.251|   0.6%/111|   0.6%/120|   0.6%/123|   0.6%/126 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 136   |     648|     163.858|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 136   |     386|      91.565|   1.5%/ 47|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 136   |    7399|     577.931|   0.2%/312|   0.2%/292|   0.2%/287|   0.2%/282 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 136   |     308|      96.517|   2.5%/ 28|   2.7%/ 25|   2.8%/ 25|   2.9%/ 24 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 136   |    1020|     962.867|   0.1%/758|   0.1%/804|   0.1%/813|   0.1%/821 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 136   |    2287|     444.095|   2.0%/ 35|   1.6%/ 42|   1.6%/ 44|   1.5%/ 47 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 136   |     152|     171.480|   0.9%/ 73|   0.9%/ 77|   0.9%/ 79|   0.9%/ 81 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 136   |    1336|     195.532|   1.7%/ 41|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 136   |   10588|     365.143|   2.2%/ 31|   1.8%/ 38|   1.7%/ 40|   1.6%/ 43 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 136   |  168584|     511.566|   0.7%/ 99|   0.7%/100|   0.7%/100|   0.7%/101 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 136   |     365|     113.907|   1.2%/ 56|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 136   |      58|      93.434|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 136   |    2398|     280.911|   0.6%/114|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 136   |    1753|     230.176|   0.8%/ 91|   0.8%/ 89|   0.8%/ 89|   0.8%/ 88 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 136   |     151|      84.202|   2.5%/ 28|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 136   |    1033|     177.354|   0.7%/101|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 124   |      29|      50.967|   1.0%/ 67|   1.2%/ 57|   1.3%/ 55|   1.3%/ 53 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 136   |    1360|      42.208|   0.5%/140|   0.5%/152|   0.4%/154|   0.4%/155 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 136   |     224|      78.598|   2.3%/ 30|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 136   |    1359|      31.596|   0.8%/ 86|   0.8%/ 91|   0.8%/ 92|   0.7%/ 94 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 136   |      89|       2.867|   2.9%/ 23|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 136   |    5513|     122.688|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 136   |     825|     278.825|   0.7%/100|   0.5%/129|   0.5%/138|   0.5%/148 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 136   |     393|      15.307|   5.2%/ 13|   5.5%/ 12|   5.6%/ 12|   5.7%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 136   |     725|      81.426|   0.1%/767|   0.1%/710|   0.1%/697|   0.1%/685 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 136   |     520|      51.686|   0.8%/ 82|   0.5%/136|   0.4%/162|   0.3%/200 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 136   |     170|     110.144|   1.0%/ 69|   0.9%/ 76|   0.9%/ 77|   0.9%/ 79 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 136   |    3607|      21.409|   1.1%/ 65|   1.0%/ 70|   1.0%/ 72|   0.9%/ 73 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 136   |     609|      64.678|   0.6%/123|   0.4%/154|   0.4%/165|   0.4%/177 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 136   |    9902|     859.220|   0.1%/ ***|   0.1%/ ***|   0.1%/962|   0.1%/923 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 131   |      39|       3.325|   0.2%/431|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 136   |    4085|     356.160|   2.1%/ 34|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 136   |     471|     142.565|   2.1%/ 32|   2.1%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 136   |       3|       1.127|   3.5%/ 20|   2.2%/ 32|   1.9%/ 36|   1.7%/ 42 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 136   |  106716|     504.776|   1.0%/ 68|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 136   |     497|      71.532|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.8%/ 37 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 136   |      54|       2.595|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 124   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 136   |     400|      15.073|   0.2%/319|   0.2%/334|   0.2%/334|   0.2%/332 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 136   |    9065|     238.569|   0.1%/931|   0.1%/929|   0.1%/928|   0.1%/927 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  84   |      61|      11.086|   0.3%/246|   0.5%/148|   0.5%/134|   0.6%/122 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 109   |      76|       4.689|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 136   |   10443|     546.570|   0.6%/108|   0.6%/126|   0.5%/131|   0.5%/137 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 136   |    4695|       3.348|   0.1%/ ***|   0.1%/905|   0.1%/878|   0.1%/853 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 136   |   14877|     301.174|   2.7%/ 26|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 136   |     311|      61.574|   4.6%/ 15|   4.1%/ 17|   4.0%/ 17|   3.8%/ 18 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 136   |     166|      40.763|   0.8%/ 85|   0.6%/111|   0.6%/120|   0.5%/132 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 136   |      88|       7.877|   0.1%/832|   0.1%/683|   0.1%/656|   0.1%/632 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 136   |     621|     106.600|   0.1%/882|   0.1%/782|   0.1%/758|   0.1%/736 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 136   |    1404|     135.584|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 136   |    6068|     347.377|   0.4%/164|   0.4%/189|   0.4%/197|   0.3%/205 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 136   |    5179|      51.653|   0.5%/141|   0.4%/190|   0.3%/208|   0.3%/230 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 136   |     608|      93.676|   2.0%/ 34|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 115   |      92|      68.055|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 132   |     506|       5.130|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17|   3.9%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 136   |     333|      60.220|   0.1%/849|   0.1%/710|   0.1%/681|   0.1%/655 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   30384|     452.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 136   |      52|      23.870|   0.2%/399|   0.1%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 136   |      50|      21.297|   5.9%/ 12|  12.8%/  5|  23.2%/  3|  16.0%/  4 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 133   |      17|       4.642|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 136   |    9225|     110.945|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 136   |     228|       7.542|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 136   |     218|      20.297|   0.5%/149|   0.5%/133|   0.5%/130|   0.5%/126 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 136   |    2391|     144.002|   1.4%/ 48|   1.2%/ 57|   1.1%/ 61|   1.1%/ 64 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 122   |      51|       4.215|   0.6%/122|   0.3%/230|   0.2%/300|   0.2%/433 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 111   |      29|      18.283|   0.6%/115|   0.7%/105|   0.7%/103|   0.7%/102 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 132   |     190|      16.424|   1.2%/ 58|   1.3%/ 51|   1.4%/ 50|   1.4%/ 48 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 136   |    1650|     180.114|   1.3%/ 52|   0.8%/ 88|   0.6%/107|   0.5%/135 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 136   |     605|      61.936|   0.1%/580|   0.2%/453|   0.2%/429|   0.2%/408 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   49379|      36.276|   2.1%/ 32|   2.1%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 136   |    6107|      22.881|   1.2%/ 59|   1.0%/ 68|   1.0%/ 70|   0.9%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   19595|     235.019|   1.0%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 136   |    5800|     148.231|   1.4%/ 51|   1.2%/ 58|   1.1%/ 60|   1.1%/ 63 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 136   |    1774|     360.535|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 136   |     664|      72.226|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   35239|     584.992|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 136   |      14|       5.254|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 136   |    1068|       8.479|   0.5%/146|   0.6%/121|   0.6%/116|   0.6%/112 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 136   |      11|       1.033|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 136   |    1349|      72.201|   1.3%/ 51|   1.9%/ 36|   2.1%/ 34|   2.2%/ 31 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 136   |     485|      10.200|   2.4%/ 29|   2.1%/ 32|   2.1%/ 34|   2.0%/ 35 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 136   |     390|     217.258|   3.6%/ 19|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 133   |     496|     112.222|   0.7%/103|   0.6%/110|   0.6%/113|   0.6%/115 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 134   |    1514|     231.710|   0.6%/118|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 134   |      32|      16.919|   0.1%/728|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 136   |      93|      13.667|   3.6%/ 19|   3.9%/ 18|   3.9%/ 17|   4.0%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 133   |      83|      18.462|   0.7%/ 94|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 135   |     146|      21.247|   4.9%/ 14|   5.1%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 136   |      81|      29.045|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  90   |     169|       6.424|   3.3%/ 21|   2.7%/ 26|   2.6%/ 27|   2.4%/ 29 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 136   |     125|       3.831|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 136   |     125|       6.190|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 136   |     157|      38.622|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 136   |   56076|     443.015|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 136   |     887|     330.772|   0.9%/ 76|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 136   |     577|      16.089|   3.6%/ 19|   4.1%/ 17|   4.2%/ 17|   4.3%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  82   |      19|       0.640|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  36   |      29|      11.963|   8.3%/  8|  10.2%/  7|  12.4%/  5|  14.9%/  4 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  91   |      96|       3.202|   4.7%/ 15|   5.7%/ 12|   6.0%/ 11|   6.2%/ 11 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 136   |    6185|     354.289|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 136   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 136   |     130|      20.121|   0.8%/ 90|   0.7%/103|   0.7%/106|   0.6%/110 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 136   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 136   |     979|       4.749|   0.6%/107|   0.6%/122|   0.5%/126|   0.5%/131 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 136   |     547|     263.332|   0.7%/104|   0.5%/145|   0.4%/161|   0.4%/182 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 136   |     256|      47.776|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 136   |     567|     121.520|   1.8%/ 38|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 136   |    6184|      28.195|   0.3%/264|   0.2%/348|   0.2%/377|   0.2%/409 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 136   |    1781|     422.158|   1.5%/ 48|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  19   |       3|       0.336|  10.3%/  7|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 136   |      97|      13.517|   5.5%/ 12|   6.1%/ 11|   6.3%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 136   |   23317|     725.677|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 136   |    2408|      22.191|   1.5%/ 47|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 136   |    1850|      48.210|   0.6%/122|   0.6%/115|   0.6%/114|   0.6%/112 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 136   |    1770|     172.272|   0.2%/402|   0.2%/411|   0.2%/411|   0.2%/412 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 136   |     191|      69.676|   0.8%/ 92|   0.7%/ 93|   0.7%/ 93|   0.7%/ 93 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 136   |    2884|     148.633|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 136   |   15545|     105.934|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/101 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  77   |       8|       0.660|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 136   |    3339|      97.573|   1.1%/ 64|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 136   |     250|      15.393|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 136   |     681|      97.752|   1.1%/ 64|   0.9%/ 78|   0.8%/ 83|   0.8%/ 88 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 114   |      69|       8.743|   0.3%/268|   0.3%/235|   0.3%/227|   0.3%/220 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 136   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 136   |      31|       5.702|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 136   |     130|      62.229|   0.6%/108|   0.7%/ 97|   0.7%/ 95|   0.7%/ 93 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 129   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 136   |   11959|     203.470|   2.7%/ 26|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28580|     606.793|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 136   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 136   |     799|      18.832|   0.5%/142|   0.4%/160|   0.4%/166|   0.4%/172 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 136   |    5793|     560.315|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 136   |    1991|     231.413|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 136   |      58|       3.313|   1.3%/ 54|   0.7%/103|   0.5%/134|   0.4%/190 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 136   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 136   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 136   |      26|       3.480|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 136   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 136   |      52|       4.437|   0.3%/236|   0.4%/181|   0.4%/170|   0.4%/161 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 136   |    5931|      71.322|   0.3%/241|   0.3%/244|   0.3%/245|   0.3%/246 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  168584|     511.566|   0.7%/ 99|   0.7%/100|   0.7%/100|   0.7%/101 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  22   |       9|       0.223|   7.9%/  9|   9.8%/  7|   8.4%/  8|   9.5%/  7 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 136   |    2040|      48.710|   1.3%/ 55|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 136   |     360|      36.420|   0.2%/359|   0.2%/413|   0.2%/430|   0.2%/449 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   46894|     705.856|   0.1%/656|   0.1%/739|   0.1%/765|   0.1%/792 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 136   |      38|      10.781|   0.3%/198|   0.2%/287|   0.2%/326|   0.2%/376 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 136   |     230|       6.735|   3.3%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 136   |     263|       8.149|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.7%/ 19 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  15   |      22|       0.229|   3.6%/ 19|  11.5%/  6|  11.9%/  6|  11.2%/  6 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 135   |     257|      14.347|   5.3%/ 13|   6.1%/ 11|   6.3%/ 11|   6.4%/ 11 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 136   |     144|       9.522|   6.6%/ 10|   6.0%/ 11|   5.8%/ 12|   5.7%/ 12 |

