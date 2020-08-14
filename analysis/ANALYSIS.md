# State and Country COVID-19 Analysis #
## Updated: at 2020-08-14 for data as of 2020-08-13 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.3% of deaths and 40.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 135   |   32823|    1687.266|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 135   |   15902|    1790.377|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 135   |   10941|     276.904|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 135   |   10382|     358.055|   2.2%/ 32|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 135   |    9045|     421.135|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 135   |    8790|    1264.780|   0.2%/428|   0.2%/441|   0.2%/445|   0.2%/449 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 135   |    7906|     623.924|   0.2%/326|   0.2%/329|   0.2%/330|   0.2%/331 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 135   |    7378|     576.308|   0.2%/343|   0.2%/337|   0.2%/335|   0.2%/333 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 135   |    6551|     655.985|   0.1%/577|   0.1%/559|   0.1%/556|   0.1%/553 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 135   |    4462|     420.242|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 135   |  167433|     508.075|   0.7%/101|   0.7%/102|   0.7%/102|   0.7%/103 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 135   |  105798|     500.436|   1.0%/ 66|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 135   |   55366|     437.411|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 135   |   48380|      35.541|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 135   |   46859|     705.329|   0.1%/663|   0.1%/764|   0.1%/795|   0.1%/831 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 135   |   35233|     584.893|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 135   |   30370|     452.767|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 135   |   28564|     606.460|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 135   |   22944|     714.079|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 135   |   19784|     237.283|   1.1%/ 65|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 135   |    1897|     386.819|   1.5%/ 48|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 135   |      28|      38.150|   1.2%/ 55|   1.4%/ 50|   1.4%/ 49|   1.5%/ 48 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 135   |    4472|     614.398|   1.5%/ 47|   1.2%/ 59|   1.1%/ 63|   1.0%/ 67 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 135   |     587|     194.554|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 135   |   10941|     276.904|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 135   |    1885|     327.342|   0.2%/299|   0.2%/343|   0.2%/356|   0.2%/371 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 135   |    4451|    1248.562|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 135   |     601|     617.245|   0.1%/554|   0.1%/618|   0.1%/636|   0.1%/655 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 135   |    9045|     421.135|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33|   2.1%/ 33 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 135   |    4462|     420.242|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 135   |      28|      20.005|   2.1%/ 33|   2.7%/ 26|   2.8%/ 24|   3.0%/ 23 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 135   |     274|     153.567|   2.3%/ 30|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 135   |    7906|     623.924|   0.2%/326|   0.2%/329|   0.2%/330|   0.2%/331 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 135   |    3091|     459.208|   0.4%/189|   0.4%/186|   0.4%/185|   0.4%/184 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 135   |     959|     303.930|   0.8%/ 87|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 135   |     402|     137.970|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 135   |     797|     178.331|   0.7%/105|   0.6%/112|   0.6%/114|   0.6%/116 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 135   |    4399|     946.231|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 135   |     127|      94.293|   0.3%/247|   0.2%/288|   0.2%/300|   0.2%/314 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 135   |    3623|     599.342|   0.3%/247|   0.3%/248|   0.3%/248|   0.3%/249 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 135   |    8790|    1264.780|   0.2%/428|   0.2%/441|   0.2%/445|   0.2%/449 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 135   |    6551|     655.985|   0.1%/577|   0.1%/559|   0.1%/556|   0.1%/553 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 135   |    1721|     305.207|   0.4%/174|   0.4%/160|   0.4%/157|   0.4%/154 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 135   |    2025|     680.392|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 135   |    1370|     223.241|   0.6%/112|   0.5%/126|   0.5%/130|   0.5%/135 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 135   |      84|      78.246|   2.7%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 135   |     356|     184.073|   0.7%/102|   0.7%/ 97|   0.7%/ 96|   0.7%/ 95 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 135   |    1022|     331.813|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 135   |     423|     311.326|   0.1%/516|   0.1%/994|   0.1%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 135   |   15902|    1790.377|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 135   |     706|     336.653|   0.7%/100|   0.6%/114|   0.6%/118|   0.6%/123 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 135   |   32823|    1687.266|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 135   |    2309|     220.192|   1.3%/ 54|   1.2%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 135   |     118|     154.798|   1.2%/ 57|   1.4%/ 51|   1.4%/ 50|   1.4%/ 48 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 135   |    3780|     323.384|   0.6%/110|   0.6%/120|   0.6%/123|   0.5%/126 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 135   |     641|     161.878|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 56 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 135   |     381|      90.284|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 135   |    7378|     576.308|   0.2%/343|   0.2%/337|   0.2%/335|   0.2%/333 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 135   |     300|      93.838|   2.3%/ 30|   2.5%/ 27|   2.6%/ 27|   2.6%/ 26 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 135   |    1019|     961.825|   0.1%/819|   0.1%/938|   0.1%/970|   0.1%/ *** |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 135   |    2251|     437.145|   2.0%/ 34|   1.7%/ 40|   1.6%/ 43|   1.5%/ 45 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 135   |     150|     170.041|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 79 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 135   |    1315|     192.488|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 135   |   10382|     358.055|   2.2%/ 32|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 135   |  167433|     508.075|   0.7%/101|   0.7%/102|   0.7%/102|   0.7%/103 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 135   |     361|     112.650|   1.3%/ 54|   1.1%/ 62|   1.1%/ 64|   1.0%/ 67 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 135   |      58|      93.357|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 135   |    2386|     279.544|   0.6%/108|   0.6%/108|   0.6%/109|   0.6%/109 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 135   |    1739|     228.357|   0.8%/ 91|   0.8%/ 88|   0.8%/ 88|   0.8%/ 87 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 135   |     146|      81.235|   2.5%/ 28|   3.0%/ 23|   3.1%/ 22|   3.2%/ 21 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 135   |    1026|     176.288|   0.7%/ 99|   0.7%/105|   0.6%/107|   0.6%/109 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 123   |      29|      50.344|   1.0%/ 70|   1.2%/ 59|   1.2%/ 56|   1.3%/ 54 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 135   |    1353|      41.990|   0.5%/140|   0.4%/160|   0.4%/165|   0.4%/168 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 135   |     219|      76.980|   2.3%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 135   |    1348|      31.360|   0.8%/ 84|   0.8%/ 89|   0.8%/ 90|   0.8%/ 92 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 135   |      86|       2.776|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16|   4.3%/ 16 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 135   |    5334|     118.690|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 135   |     820|     277.233|   0.7%/ 96|   0.6%/122|   0.5%/131|   0.5%/141 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 135   |     376|      14.651|   5.1%/ 13|   5.5%/ 13|   5.6%/ 12|   5.7%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 135   |     724|      81.355|   0.1%/774|   0.1%/709|   0.1%/695|   0.1%/682 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 135   |     518|      51.424|   0.9%/ 77|   0.6%/124|   0.5%/146|   0.4%/178 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 135   |     169|     109.189|   1.0%/ 66|   1.0%/ 71|   1.0%/ 73|   0.9%/ 74 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 135   |    3570|      21.190|   1.1%/ 64|   1.0%/ 71|   1.0%/ 73|   0.9%/ 75 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 135   |     606|      64.369|   0.6%/121|   0.4%/154|   0.4%/166|   0.4%/179 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 135   |    9894|     858.518|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 130   |      39|       3.330|   0.2%/301|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 135   |    4018|     350.344|   2.1%/ 32|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 135   |     460|     139.272|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 135   |       2|       1.068|   2.6%/ 27|   0.1%/863|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 135   |  105798|     500.436|   1.0%/ 66|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 135   |     489|      70.324|   1.9%/ 36|   1.9%/ 35|   1.9%/ 35|   1.9%/ 35 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 135   |      54|       2.594|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 123   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 135   |     399|      15.038|   0.2%/326|   0.2%/363|   0.2%/368|   0.2%/372 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 135   |    9058|     238.385|   0.1%/980|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  83   |      61|      11.045|   0.3%/250|   0.5%/131|   0.6%/115|   0.7%/103 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 108   |      76|       4.686|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 135   |   10387|     543.596|   0.7%/105|   0.6%/121|   0.6%/126|   0.5%/131 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 135   |    4693|       3.347|   0.1%/ ***|   0.1%/936|   0.1%/908|   0.1%/881 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 135   |   14524|     294.024|   2.7%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 28 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 135   |     300|      59.280|   4.9%/ 14|   4.5%/ 15|   4.3%/ 16|   4.2%/ 16 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 135   |     165|      40.524|   0.9%/ 81|   0.7%/101|   0.6%/108|   0.6%/117 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 135   |      88|       7.875|   0.1%/759|   0.1%/593|   0.1%/564|   0.1%/538 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 135   |     620|     106.516|   0.1%/811|   0.1%/690|   0.1%/664|   0.1%/639 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 135   |    1383|     133.562|   1.5%/ 46|   1.6%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 135   |    6047|     346.144|   0.4%/163|   0.4%/189|   0.4%/198|   0.3%/207 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 135   |    5159|      51.452|   0.5%/136|   0.4%/187|   0.3%/206|   0.3%/229 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 135   |     597|      91.984|   2.1%/ 33|   1.9%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 114   |      93|      68.665|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 131   |     488|       4.941|   4.1%/ 17|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 135   |     333|      60.172|   0.1%/773|   0.1%/619|   0.1%/589|   0.1%/562 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 135   |   30370|     452.767|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 135   |      52|      23.867|   0.2%/335|   0.1%/672|   0.1%/921|   0.0%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 135   |      43|      18.316|  10.7%/  6|  19.0%/  3|  12.8%/  5|  23.2%/  3 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 132   |      17|       4.650|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 135   |    9219|     110.868|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 135   |     225|       7.445|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 135   |     216|      20.162|   0.4%/166|   0.5%/154|   0.5%/151|   0.5%/148 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 135   |    2361|     142.217|   1.4%/ 48|   1.2%/ 58|   1.1%/ 62|   1.1%/ 66 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 121   |      51|       4.212|   0.7%/105|   0.4%/169|   0.3%/200|   0.3%/246 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 110   |      29|      18.170|   0.7%/101|   0.8%/ 85|   0.9%/ 81|   0.9%/ 79 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 131   |     188|      16.216|   1.1%/ 61|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 135   |    1636|     178.678|   1.4%/ 48|   0.9%/ 75|   0.8%/ 88|   0.7%/106 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 135   |     604|      61.845|   0.1%/596|   0.2%/457|   0.2%/431|   0.2%/408 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 135   |   48380|      35.541|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 135   |    6044|      22.645|   1.2%/ 58|   1.0%/ 67|   1.0%/ 70|   0.9%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 135   |   19784|     237.283|   1.1%/ 65|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 135   |    5731|     146.469|   1.4%/ 50|   1.2%/ 56|   1.2%/ 58|   1.1%/ 60 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 135   |    1774|     360.397|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 135   |     651|      70.883|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 135   |   35233|     584.893|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 135   |      14|       5.195|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 135   |    1062|       8.430|   0.4%/156|   0.5%/130|   0.6%/125|   0.6%/120 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 135   |      11|       1.033|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 135   |    1314|      70.328|   2.0%/ 35|   2.8%/ 24|   3.0%/ 23|   3.3%/ 21 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 135   |     476|      10.009|   2.5%/ 28|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 135   |     376|     209.398|   3.6%/ 19|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 132   |     493|     111.546|   0.7%/100|   0.7%/106|   0.6%/107|   0.6%/109 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 133   |    1510|     231.100|   0.7%/104|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 133   |      32|      16.917|   0.1%/632|   0.1%/883|   0.1%/ ***|   0.1%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 135   |      90|      13.192|   3.7%/ 19|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 132   |      82|      18.375|   0.8%/ 90|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 134   |     141|      20.465|   4.0%/ 17|   5.3%/ 13|   3.5%/ 20|   2.6%/ 27 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 135   |      81|      29.030|   0.1%/968|   0.1%/907|   0.1%/893|   0.1%/881 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  89   |     165|       6.285|   3.4%/ 20|   2.8%/ 25|   2.6%/ 26|   2.5%/ 28 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 135   |     125|       3.831|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 135   |     125|       6.188|   0.1%/958|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 135   |     157|      38.627|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 135   |   55366|     437.411|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 135   |     879|     327.880|   0.9%/ 77|   0.8%/ 82|   0.8%/ 83|   0.8%/ 85 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 135   |     559|      15.590|   3.5%/ 20|   3.9%/ 18|   4.0%/ 17|   4.1%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  81   |      19|       0.624|   3.3%/ 21|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  35   |      25|      10.167|   7.8%/  9|   7.3%/  9|   7.6%/  9|   7.9%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  90   |      90|       3.016|   4.4%/ 15|   5.5%/ 13|   5.7%/ 12|   6.0%/ 11 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 135   |    6183|     354.171|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 135   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 135   |     129|      20.007|   0.9%/ 81|   0.8%/ 87|   0.8%/ 88|   0.8%/ 90 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 135   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 135   |     973|       4.720|   0.7%/104|   0.6%/120|   0.6%/124|   0.5%/129 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 135   |     544|     262.112|   0.7%/ 97|   0.5%/131|   0.5%/144|   0.4%/160 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 135   |     256|      47.761|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 135   |     557|     119.377|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 135   |    6171|      28.135|   0.3%/255|   0.2%/346|   0.2%/378|   0.2%/415 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 135   |    1760|     417.090|   1.5%/ 46|   1.3%/ 54|   1.2%/ 56|   1.2%/ 59 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  18   |       3|       0.336|  14.5%/  5|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 135   |      91|      12.761|   5.2%/ 13|   5.7%/ 12|   5.9%/ 12|   6.0%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 135   |   22944|     714.079|   1.0%/ 67|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 135   |    2370|      21.842|   1.4%/ 49|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 135   |    1839|      47.913|   0.6%/126|   0.6%/119|   0.6%/117|   0.6%/116 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 135   |    1767|     171.959|   0.2%/412|   0.2%/431|   0.2%/434|   0.2%/438 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 135   |     190|      69.243|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86|   0.8%/ 85 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 135   |    2839|     146.293|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 135   |   15432|     105.160|   0.8%/ 88|   0.7%/ 97|   0.7%/ 99|   0.7%/102 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  76   |       8|       0.648|   0.0%/ --|   5.3%/ 13|   4.6%/ 15|   4.6%/ 15 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 135   |    3303|      96.523|   1.1%/ 64|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 135   |     246|      15.179|   1.4%/ 50|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 135   |     675|      96.933|   1.1%/ 61|   0.9%/ 73|   0.9%/ 77|   0.9%/ 81 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 113   |      69|       8.721|   0.3%/248|   0.3%/204|   0.4%/195|   0.4%/186 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 135   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 135   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 135   |     130|      61.955|   0.6%/111|   0.7%/ 99|   0.7%/ 97|   0.7%/ 95 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 128   |      93|       5.852|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 135   |   11686|     198.819|   2.7%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 135   |   28564|     606.460|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 135   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 135   |     796|      18.756|   0.5%/135|   0.5%/150|   0.4%/154|   0.4%/158 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 135   |    5790|     560.043|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 135   |    1990|     231.323|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 135   |      57|       3.237|   1.7%/ 41|   1.2%/ 59|   1.0%/ 67|   0.9%/ 76 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 135   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 135   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 135   |      26|       3.407|   5.0%/ 14|   4.2%/ 16|   4.2%/ 16|   1.3%/ 53 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 135   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 135   |      52|       4.412|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 135   |    5913|      71.108|   0.3%/245|   0.3%/251|   0.3%/253|   0.3%/255 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 135   |  167433|     508.075|   0.7%/101|   0.7%/102|   0.7%/102|   0.7%/103 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  21   |      11|       0.262|   4.7%/ 15|  12.8%/  5|   9.9%/  7|   6.5%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 135   |    2015|      48.105|   1.3%/ 54|   1.3%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 135   |     360|      36.360|   0.2%/336|   0.2%/373|   0.2%/384|   0.2%/396 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 135   |   46859|     705.329|   0.1%/663|   0.1%/764|   0.1%/795|   0.1%/831 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 135   |      38|      10.724|   0.3%/224|   0.2%/415|   0.1%/535|   0.1%/755 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 135   |     224|       6.551|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 135   |     253|       7.866|   3.4%/ 20|   3.5%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  14   |      21|       0.218|   7.7%/  9|  17.0%/  4|  11.5%/  6|  11.9%/  6 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 134   |     247|      13.837|   5.4%/ 13|   6.3%/ 11|   6.5%/ 11|   6.7%/ 10 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 135   |     138|       9.098|   6.6%/ 10|   6.1%/ 11|   5.9%/ 12|   5.7%/ 12 |

