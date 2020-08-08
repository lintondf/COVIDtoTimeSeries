# State and Country COVID-19 Analysis #
## Updated: at 2020-08-08 for data as of 2020-08-07 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.0% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.4% of deaths and 55.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 129   |   32783|    1685.194|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 129   |   15880|    1787.882|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 129   |   10090|     255.362|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 129   |    8572|     295.616|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 129   |    8706|    1252.702|   0.2%/414|   0.2%/422|   0.2%/425|   0.2%/427 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 129   |    7967|     370.928|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 129   |    7802|     615.731|   0.2%/305|   0.2%/292|   0.2%/289|   0.2%/285 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 129   |    7297|     569.961|   0.2%/367|   0.2%/394|   0.2%/401|   0.2%/408 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 129   |    6500|     650.884|   0.1%/542|   0.1%/494|   0.1%/482|   0.1%/470 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 129   |    4445|    1246.828|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 129   |  160544|     487.169|   0.7%/ 93|   0.8%/ 87|   0.8%/ 86|   0.8%/ 85 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 129   |   99903|     472.553|   1.2%/ 60|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 129   |   51299|     405.278|   1.4%/ 50|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 129   |   46595|     701.356|   0.1%/522|   0.1%/543|   0.1%/548|   0.1%/554 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 129   |   42764|      31.416|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 129   |   35197|     584.290|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 129   |   30318|     451.999|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 129   |   28488|     604.826|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 129   |   21632|     673.243|   1.1%/ 60|   1.1%/ 64|   1.1%/ 65|   1.1%/ 66 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   18391|     220.580|   1.3%/ 55|   1.2%/ 58|   1.2%/ 59|   1.1%/ 60 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 129   |    1757|     358.311|   1.5%/ 47|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 129   |      26|      35.697|   1.2%/ 57|   1.5%/ 46|   1.6%/ 44|   1.6%/ 42 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 129   |    4184|     574.860|   1.9%/ 36|   1.6%/ 44|   1.5%/ 46|   1.4%/ 49 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 129   |     517|     171.469|   2.1%/ 33|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 129   |   10090|     255.362|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 129   |    1866|     324.037|   0.3%/256|   0.2%/279|   0.2%/287|   0.2%/296 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 129   |    4445|    1246.828|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 129   |     602|     618.699|   0.1%/515|   0.1%/580|   0.1%/601|   0.1%/623 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 129   |    7967|     370.928|   2.4%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 129   |    4081|     384.365|   1.3%/ 51|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 129   |      28|      19.571|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 129   |     231|     129.178|   3.0%/ 23|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 129   |    7802|     615.731|   0.2%/305|   0.2%/292|   0.2%/289|   0.2%/285 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 129   |    3029|     449.924|   0.3%/199|   0.3%/205|   0.3%/207|   0.3%/208 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 129   |     913|     289.320|   0.8%/ 90|   0.8%/ 86|   0.8%/ 85|   0.8%/ 85 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 129   |     381|     130.688|   1.0%/ 70|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 129   |     769|     172.127|   0.7%/101|   0.6%/110|   0.6%/113|   0.6%/117 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 129   |    4171|     897.219|   0.9%/ 79|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 129   |     125|      93.006|   0.3%/216|   0.3%/249|   0.3%/260|   0.3%/272 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 129   |    3562|     589.129|   0.3%/248|   0.3%/245|   0.3%/245|   0.3%/245 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 129   |    8706|    1252.702|   0.2%/414|   0.2%/422|   0.2%/425|   0.2%/427 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 129   |    6500|     650.884|   0.1%/542|   0.1%/494|   0.1%/482|   0.1%/470 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 129   |    1679|     297.695|   0.3%/204|   0.4%/198|   0.4%/196|   0.4%/194 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 129   |    1840|     618.244|   1.7%/ 40|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 129   |    1324|     215.661|   0.7%/ 96|   0.7%/ 98|   0.7%/ 98|   0.7%/ 99 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 129   |      71|      66.172|   2.9%/ 24|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 129   |     343|     177.189|   0.7%/105|   0.7%/106|   0.7%/106|   0.7%/106 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 129   |     915|     297.128|   1.8%/ 38|   1.9%/ 36|   1.9%/ 36|   1.9%/ 35 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 129   |     422|     310.258|   0.2%/287|   0.2%/347|   0.2%/369|   0.2%/394 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 129   |   15880|    1787.882|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 129   |     679|     323.855|   0.8%/ 84|   0.8%/ 87|   0.8%/ 88|   0.8%/ 89 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 129   |   32783|    1685.194|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 129   |    2142|     204.268|   1.4%/ 49|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 129   |     110|     144.294|   0.9%/ 75|   0.9%/ 77|   0.9%/ 77|   0.9%/ 78 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 129   |    3652|     312.449|   0.8%/ 92|   0.8%/ 89|   0.8%/ 89|   0.8%/ 89 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 129   |     595|     150.270|   1.6%/ 43|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 129   |     350|      83.074|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 129   |    7297|     569.961|   0.2%/367|   0.2%/394|   0.2%/401|   0.2%/408 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 129   |     249|      78.010|   2.2%/ 32|   2.5%/ 28|   2.6%/ 27|   2.7%/ 26 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 129   |    1015|     958.270|   0.1%/672|   0.1%/817|   0.1%/861|   0.1%/907 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 129   |    2040|     396.290|   2.6%/ 27|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 129   |     141|     159.295|   1.1%/ 61|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 129   |    1193|     174.659|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 129   |    8572|     295.616|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 129   |  160544|     487.169|   0.7%/ 93|   0.8%/ 87|   0.8%/ 86|   0.8%/ 85 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 129   |     338|     105.557|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 129   |      57|      91.955|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 129   |    2285|     267.756|   0.8%/ 86|   1.0%/ 72|   1.0%/ 69|   1.0%/ 67 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 129   |    1653|     217.134|   0.8%/ 90|   0.8%/ 82|   0.9%/ 81|   0.9%/ 79 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 129   |     125|      69.498|   1.5%/ 47|   1.7%/ 39|   1.8%/ 38|   1.9%/ 36 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 129   |     984|     168.998|   0.8%/ 82|   0.9%/ 76|   0.9%/ 75|   0.9%/ 73 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 117   |      27|      47.405|   0.7%/ 99|   0.7%/ 97|   0.7%/ 96|   0.7%/ 94 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 129   |    1331|      41.317|   0.4%/158|   0.1%/582|   0.0%/ ***|   0.0%/ -- |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 129   |     192|      67.507|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 129   |    1287|      29.926|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80|   0.9%/ 81 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 129   |      68|       2.182|   4.4%/ 16|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 129   |    4406|      98.043|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 129   |     795|     268.671|   0.9%/ 77|   0.6%/107|   0.6%/118|   0.5%/132 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 129   |     271|      10.551|   4.6%/ 15|   5.2%/ 13|   5.3%/ 13|   5.4%/ 13 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 129   |     720|      80.886|   0.1%/ ***|   0.1%/964|   0.1%/955|   0.1%/947 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 129   |     501|      49.752|   1.4%/ 49|   1.1%/ 62|   1.0%/ 67|   0.9%/ 73 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 129   |     159|     103.009|   1.1%/ 61|   1.0%/ 69|   1.0%/ 72|   0.9%/ 74 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 129   |    3378|      20.049|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 129   |     590|      62.710|   0.8%/ 89|   0.7%/102|   0.7%/106|   0.6%/110 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 129   |    9864|     855.910|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 124   |      39|       3.321|   0.5%/154|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 129   |    3569|     311.193|   2.6%/ 26|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 129   |     394|     119.420|   2.2%/ 31|   2.3%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 129   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 129   |   99903|     472.553|   1.2%/ 60|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 129   |     436|      62.763|   2.1%/ 33|   2.3%/ 31|   2.3%/ 30|   2.3%/ 29 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 129   |      54|       2.566|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 117   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 129   |     396|      14.928|   0.1%/490|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 129   |    9024|     237.475|   0.1%/960|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  77   |      59|      10.742|   0.1%/720|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 102   |      75|       4.639|   0.1%/ ***|   0.1%/545|   0.1%/483|   0.2%/431 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 129   |   10148|     531.114|   0.8%/ 87|   0.7%/ 96|   0.7%/ 98|   0.7%/101 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 129   |    4676|       3.335|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 129   |   12464|     252.331|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 129   |     233|      46.079|   6.5%/ 11|   5.7%/ 12|   5.5%/ 13|   5.3%/ 13 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 129   |     158|      38.771|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 129   |      88|       7.815|   0.1%/742|   0.1%/515|   0.1%/474|   0.2%/439 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 129   |     617|     105.952|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 129   |    1261|     121.775|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 129   |    5914|     338.571|   0.6%/125|   0.5%/132|   0.5%/133|   0.5%/135 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 129   |    5061|      50.470|   0.7%/102|   0.5%/145|   0.4%/162|   0.4%/183 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 129   |     529|      81.610|   2.3%/ 30|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 108   |      88|      64.695|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 125   |     381|       3.866|   4.6%/ 15|   4.8%/ 14|   4.9%/ 14|   4.9%/ 14 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 129   |     330|      59.776|   0.1%/ ***|   0.1%/813|   0.1%/759|   0.1%/712 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 129   |   30318|     451.999|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 129   |      51|      23.688|   0.5%/144|   0.5%/140|   0.5%/140|   0.5%/140 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 129   |      16|       6.750|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 126   |      17|       4.660|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 129   |    9182|     110.426|   0.1%/ ***|   0.1%/998|   0.1%/967|   0.1%/938 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 129   |     202|       6.679|   1.8%/ 38|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 129   |     211|      19.688|   0.4%/195|   0.4%/183|   0.4%/180|   0.4%/178 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 129   |    2190|     131.873|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 115   |      50|       4.070|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57|   1.2%/ 57 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 104   |      27|      16.866|   0.3%/248|   0.4%/187|   0.4%/176|   0.4%/167 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 125   |     173|      14.920|   0.9%/ 76|   1.0%/ 71|   1.0%/ 70|   1.0%/ 69 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 129   |    1543|     168.473|   2.3%/ 30|   2.0%/ 35|   1.9%/ 37|   1.8%/ 39 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 129   |     599|      61.272|   0.1%/ ***|   0.1%/807|   0.1%/749|   0.1%/697 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 129   |   42764|      31.416|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32|   2.2%/ 32 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 129   |    5701|      21.359|   1.4%/ 48|   1.2%/ 57|   1.2%/ 59|   1.1%/ 62 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 129   |   18391|     220.580|   1.3%/ 55|   1.2%/ 58|   1.2%/ 59|   1.1%/ 60 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 129   |    5331|     136.246|   1.6%/ 43|   1.4%/ 51|   1.3%/ 53|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 129   |    1769|     359.367|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 129   |     587|      63.910|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 129   |   35197|     584.290|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 129   |      12|       4.527|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 129   |    1029|       8.170|   0.3%/214|   0.4%/168|   0.4%/159|   0.5%/151 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 129   |      11|       1.043|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 129   |    1099|      58.810|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 129   |     419|       8.803|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 129   |     305|     170.000|   4.6%/ 15|   4.8%/ 14|   4.8%/ 14|   4.9%/ 14 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 126   |     474|     107.292|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94|   0.7%/ 94 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 127   |    1737|     265.806|   1.5%/ 48|   0.5%/133|   0.3%/240|   0.1%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 127   |      32|      16.811|   0.2%/351|   0.2%/308|   0.2%/298|   0.2%/289 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 129   |      71|      10.467|   2.9%/ 24|   3.1%/ 22|   3.1%/ 22|   3.2%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 126   |      81|      18.064|   0.7%/101|   0.7%/ 94|   0.7%/ 92|   0.8%/ 91 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 128   |     105|      15.333|   4.5%/ 15|   4.8%/ 14|   4.8%/ 14|   4.9%/ 14 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 129   |      81|      28.855|   0.1%/595|   0.1%/471|   0.2%/444|   0.2%/417 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  83   |     139|       5.280|   4.3%/ 16|   3.7%/ 19|   3.5%/ 20|   3.3%/ 21 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 129   |     125|       3.829|   0.1%/753|   0.1%/899|   0.1%/953|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 129   |     125|       6.165|   0.1%/729|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 129   |     158|      38.808|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 129   |   51299|     405.278|   1.4%/ 50|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 129   |     836|     311.557|   1.0%/ 66|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 129   |     398|      11.086|   3.1%/ 22|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  75   |      15|       0.514|   2.7%/ 26|   4.1%/ 17|   4.5%/ 15|   4.8%/ 14 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  29   |      16|       6.507|   6.2%/ 11|   5.3%/ 13|   7.3%/  9|   9.6%/  7 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  84   |      66|       2.201|   3.0%/ 23|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 129   |    6173|     353.611|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 129   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 129   |     125|      19.274|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 129   |      69|       3.094|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 129   |     938|       4.552|   0.9%/ 81|   0.8%/ 87|   0.8%/ 88|   0.8%/ 89 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 129   |     525|     252.943|   1.1%/ 65|   0.9%/ 74|   0.9%/ 76|   0.9%/ 79 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 129   |     256|      47.683|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 129   |     495|     106.204|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 129   |    6107|      27.843|   0.3%/203|   0.2%/326|   0.2%/382|   0.2%/462 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 129   |    1632|     386.886|   1.9%/ 37|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  12   |       3|       0.336|  26.0%/  2|   0.0%/ --|  14.5%/  5|  14.5%/  5 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 129   |      66|       9.297|   4.3%/ 16|   4.5%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 129   |   21632|     673.243|   1.1%/ 60|   1.1%/ 64|   1.1%/ 65|   1.1%/ 66 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 129   |    2188|      20.166|   1.0%/ 70|   1.0%/ 68|   1.0%/ 67|   1.0%/ 66 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 129   |    1772|      46.173|   0.5%/132|   0.6%/122|   0.6%/119|   0.6%/117 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 129   |    1751|     170.425|   0.1%/471|   0.1%/630|   0.1%/689|   0.1%/762 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 129   |     181|      66.018|   0.7%/103|   0.6%/117|   0.6%/121|   0.6%/126 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 129   |    2565|     132.159|   1.4%/ 49|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 129   |   14796|     100.829|   0.9%/ 78|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  70   |       5|       0.404|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 129   |    3107|      90.792|   1.1%/ 64|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 129   |     228|      14.055|   1.5%/ 46|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 129   |     638|      91.649|   1.4%/ 48|   1.2%/ 57|   1.2%/ 60|   1.1%/ 63 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 107   |      68|       8.544|   0.1%/466|   0.1%/606|   0.1%/651|   0.1%/702 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 129   |      27|       4.740|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 129   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 129   |     124|      59.250|   0.6%/112|   0.8%/ 90|   0.8%/ 86|   0.8%/ 82 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 122   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 129   |   10026|     170.579|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 129   |   28488|     604.826|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 129   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 129   |     774|      18.229|   0.6%/117|   0.6%/126|   0.5%/128|   0.5%/131 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 129   |    5784|     559.455|   0.1%/634|   0.1%/937|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 129   |    1985|     230.750|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 129   |      53|       3.010|   2.4%/ 28|   2.9%/ 23|   1.4%/ 48|   1.4%/ 48 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 129   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 129   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 129   |      21|       2.805|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 129   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 129   |      51|       4.346|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 129   |    5817|      69.948|   0.3%/231|   0.3%/236|   0.3%/238|   0.3%/239 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 129   |  160544|     487.169|   0.7%/ 93|   0.8%/ 87|   0.8%/ 86|   0.8%/ 85 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  15   |       6|       0.149|  26.0%/  2|   7.7%/  9|   0.0%/ --|   6.3%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 129   |    1854|      44.272|   1.2%/ 59|   1.2%/ 56|   1.2%/ 55|   1.3%/ 55 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 129   |     355|      35.918|   0.2%/278|   0.2%/281|   0.2%/282|   0.2%/283 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 129   |   46595|     701.356|   0.1%/522|   0.1%/543|   0.1%/548|   0.1%/554 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 129   |      37|      10.572|   0.7%/104|   0.6%/112|   0.6%/113|   0.6%/114 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 129   |     185|       5.434|   3.9%/ 18|   3.6%/ 19|   3.5%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 129   |     206|       6.403|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 128   |     196|      10.938|   4.2%/ 16|   1.2%/ 59|   5.2%/ 13|   5.0%/ 14 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 129   |      96|       6.337|   7.9%/  9|   8.5%/  8|   8.7%/  8|   8.8%/  8 |

