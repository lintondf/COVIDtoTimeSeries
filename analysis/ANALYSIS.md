# State and Country COVID-19 Analysis #
## Updated: at 2020-08-01 for data as of 2020-07-31 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 36.1% of deaths and 40.0% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 68.8% of deaths and 56.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 122   |   32710|    1681.441|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 122   |   15862|    1785.812|   0.1%/970|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 122   |    9096|     230.217|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 122   |    8603|    1237.964|   0.2%/392|   0.2%/403|   0.2%/405|   0.2%/407 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 122   |    7688|     606.673|   0.2%/323|   0.2%/336|   0.2%/338|   0.2%/340 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 122   |    7212|     563.319|   0.2%/320|   0.2%/348|   0.2%/356|   0.2%/363 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 122   |    6641|     309.199|   2.6%/ 27|   2.8%/ 25|   2.8%/ 25|   2.8%/ 24 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 122   |    6423|     221.505|   4.0%/ 17|   4.4%/ 16|   4.4%/ 15|   4.5%/ 15 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 122   |    6445|     645.397|   0.1%/652|   0.1%/732|   0.1%/752|   0.1%/771 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 122   |    4436|    1244.197|   0.1%/933|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 122   |  152242|     461.977|   0.7%/ 99|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 122   |   92752|     438.728|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 122   |   46999|     371.302|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 122   |   46183|     695.149|   0.1%/479|   0.1%/499|   0.1%/503|   0.1%/508 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 122   |   36717|      26.973|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 122   |   35156|     583.607|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 122   |   30268|     451.249|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 122   |   28444|     603.906|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 122   |   19864|     618.200|   1.2%/ 59|   1.0%/ 68|   1.0%/ 70|   0.9%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 122   |   16844|     202.023|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 122   |    1598|     325.825|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 122   |      22|      30.403|   2.3%/ 30|   3.0%/ 23|   3.2%/ 21|   3.4%/ 20 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 122   |    3744|     514.368|   2.6%/ 27|   2.4%/ 29|   2.3%/ 30|   2.3%/ 31 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 122   |     446|     147.650|   1.9%/ 36|   2.0%/ 34|   2.1%/ 33|   2.1%/ 32 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 122   |    9096|     230.217|   1.4%/ 48|   1.5%/ 46|   1.5%/ 45|   1.6%/ 44 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 122   |    1827|     317.226|   0.3%/200|   0.4%/178|   0.4%/173|   0.4%/169 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 122   |    4436|    1244.197|   0.1%/933|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 122   |     587|     602.456|   0.2%/429|   0.2%/424|   0.2%/424|   0.2%/425 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 122   |    6641|     309.199|   2.6%/ 27|   2.8%/ 25|   2.8%/ 25|   2.8%/ 24 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 122   |    3699|     348.416|   1.3%/ 55|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 122   |      27|      19.171|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 122   |     168|      94.106|   4.3%/ 16|   5.1%/ 13|   5.3%/ 13|   5.5%/ 12 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 122   |    7688|     606.673|   0.2%/323|   0.2%/336|   0.2%/338|   0.2%/340 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 122   |    2956|     439.139|   0.4%/184|   0.4%/176|   0.4%/174|   0.4%/173 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 122   |     866|     274.418|   0.8%/ 89|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 122   |     350|     120.057|   1.2%/ 59|   1.4%/ 49|   1.5%/ 47|   1.5%/ 45 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 122   |     734|     164.316|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79|   0.9%/ 79 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 122   |    3915|     842.220|   0.9%/ 77|   1.0%/ 66|   1.1%/ 64|   1.1%/ 62 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 122   |     122|      90.935|   0.4%/159|   0.4%/160|   0.4%/160|   0.4%/159 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 122   |    3491|     577.360|   0.3%/240|   0.3%/231|   0.3%/229|   0.3%/226 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 122   |    8603|    1237.964|   0.2%/392|   0.2%/403|   0.2%/405|   0.2%/407 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 122   |    6445|     645.397|   0.1%/652|   0.1%/732|   0.1%/752|   0.1%/771 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 122   |    1640|     290.778|   0.3%/219|   0.3%/224|   0.3%/225|   0.3%/227 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 122   |    1610|     540.984|   1.5%/ 45|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 122   |    1256|     204.695|   0.8%/ 86|   0.9%/ 77|   0.9%/ 75|   0.9%/ 73 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 122   |      56|      52.854|   3.9%/ 18|   4.4%/ 16|   4.5%/ 15|   4.7%/ 15 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 122   |     330|     170.633|   0.7%/ 95|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 122   |     805|     261.437|   1.8%/ 38|   2.0%/ 35|   2.0%/ 34|   2.1%/ 33 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 122   |     415|     305.032|   0.3%/208|   0.3%/199|   0.4%/197|   0.4%/195 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 122   |   15862|    1785.812|   0.1%/970|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 122   |     641|     305.473|   0.9%/ 76|   0.9%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 122   |   32710|    1681.441|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 122   |    1939|     184.883|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 122   |     104|     136.140|   1.0%/ 72|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 122   |    3450|     295.117|   0.8%/ 90|   0.9%/ 80|   0.9%/ 78|   0.9%/ 76 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 122   |     530|     134.046|   1.5%/ 47|   1.7%/ 41|   1.7%/ 40|   1.8%/ 38 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 122   |     315|      74.715|   1.8%/ 39|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 122   |    7212|     563.319|   0.2%/320|   0.2%/348|   0.2%/356|   0.2%/363 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 122   |     215|      67.376|   1.6%/ 44|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 122   |    1010|     953.762|   0.1%/515|   0.1%/672|   0.1%/727|   0.1%/792 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 122   |    1710|     332.172|   3.2%/ 22|   3.4%/ 20|   3.4%/ 20|   3.5%/ 20 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 122   |     130|     146.700|   1.0%/ 70|   0.9%/ 74|   0.9%/ 75|   0.9%/ 75 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 122   |    1060|     155.078|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 122   |    6423|     221.505|   4.0%/ 17|   4.4%/ 16|   4.4%/ 15|   4.5%/ 15 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 122   |  152242|     461.977|   0.7%/ 99|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 122   |     304|      94.784|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 122   |      56|      90.086|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 122   |    2141|     250.812|   0.5%/136|   0.5%/129|   0.5%/127|   0.6%/125 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 122   |    1556|     204.397|   0.7%/106|   0.7%/100|   0.7%/ 98|   0.7%/ 96 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 122   |     109|      60.974|   1.1%/ 63|   1.4%/ 48|   1.5%/ 45|   1.6%/ 42 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 122   |     922|     158.365|   0.7%/ 95|   0.8%/ 83|   0.9%/ 80|   0.9%/ 78 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 110   |      26|      45.778|   0.7%/ 95|   0.6%/121|   0.5%/130|   0.5%/140 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 122   |    1327|      41.194|   0.9%/ 74|   0.5%/143|   0.4%/187|   0.3%/271 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 122   |     158|      55.638|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 122   |    1210|      28.131|   1.0%/ 72|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 122   |      49|       1.587|   5.7%/ 12|   6.3%/ 11|   7.5%/  9|   3.4%/ 20 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 122   |    3516|      78.234|   3.5%/ 19|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 122   |     756|     255.459|   1.2%/ 55|   1.0%/ 73|   0.9%/ 79|   0.8%/ 86 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 122   |     184|       7.146|   4.1%/ 17|   5.1%/ 13|   5.4%/ 13|   5.6%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 122   |     716|      80.397|   0.1%/786|   0.1%/623|   0.1%/589|   0.1%/556 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 122   |     459|      45.599|   2.0%/ 35|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 122   |     150|      97.434|   1.4%/ 48|   1.2%/ 57|   1.2%/ 59|   1.1%/ 62 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 122   |    3143|      18.657|   1.5%/ 47|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 122   |     560|      59.543|   1.0%/ 73|   0.9%/ 77|   0.9%/ 79|   0.9%/ 80 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 122   |    9839|     853.730|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 117   |      38|       3.234|   1.4%/ 49|   1.0%/ 70|   0.9%/ 79|   0.8%/ 91 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 122   |    2963|     258.358|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 122   |     315|      95.549|   2.1%/ 33|   2.3%/ 30|   2.3%/ 30|   2.4%/ 29 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 122   |       1|       0.428|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 122   |   92752|     438.728|   1.3%/ 54|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 122   |     376|      54.123|   1.9%/ 36|   2.1%/ 33|   2.1%/ 33|   2.2%/ 32 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 122   |      53|       2.540|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 110   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 122   |     396|      14.914|   0.4%/168|   0.4%/189|   0.4%/196|   0.3%/205 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 122   |    8981|     236.342|   0.1%/823|   0.1%/923|   0.1%/948|   0.1%/972 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  70   |      60|      10.890|   0.8%/ 90|   0.2%/392|   0.0%/ ***|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  95   |      75|       4.617|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 122   |    9826|     514.268|   0.9%/ 76|   0.8%/ 86|   0.8%/ 89|   0.8%/ 92 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 122   |    4654|       3.319|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 122   |   10039|     203.232|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 122   |     157|      30.998|   8.6%/  8|   9.1%/  7|   9.2%/  7|   9.3%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 122   |     143|      35.059|   1.3%/ 54|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 122   |      87|       7.769|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 122   |     614|     105.528|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 122   |    1148|     110.876|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 122   |    5705|     326.609|   0.6%/113|   0.6%/122|   0.6%/124|   0.5%/126 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 122   |    4886|      48.731|   1.0%/ 67|   0.8%/ 88|   0.7%/ 96|   0.7%/104 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 122   |     459|      70.765|   2.7%/ 25|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 101   |      51|      37.548|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 118   |     269|       2.731|   4.2%/ 16|   4.5%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 122   |     329|      59.494|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 122   |   30268|     451.249|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 122   |      49|      22.701|   0.4%/191|   0.4%/167|   0.4%/163|   0.4%/160 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 122   |       9|       3.693|   6.7%/ 10|   7.8%/  9|   8.0%/  8|   8.3%/  8 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 119   |      17|       4.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 122   |    9145|     109.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 122   |     178|       5.868|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 122   |     205|      19.086|   0.3%/242|   0.3%/202|   0.4%/194|   0.4%/188 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 122   |    1947|     117.231|   2.2%/ 31|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 108   |      46|       3.801|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  97   |      26|      16.204|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 118   |     164|      14.137|   0.7%/ 94|   0.5%/151|   0.4%/177|   0.3%/211 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 122   |    1313|     143.399|   3.2%/ 22|   3.5%/ 20|   3.5%/ 19|   3.6%/ 19 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 122   |     597|      61.053|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 122   |   36717|      26.973|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 122   |    5220|      19.556|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 122   |   16844|     202.023|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 122   |    4862|     124.267|   2.0%/ 34|   1.7%/ 41|   1.6%/ 44|   1.5%/ 46 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 122   |    1767|     359.025|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 122   |     510|      55.530|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 122   |   35156|     583.607|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 122   |      10|       3.667|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 122   |    1004|       7.971|   0.2%/449|   0.2%/355|   0.2%/337|   0.2%/321 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 122   |      11|       1.056|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 122   |     829|      44.341|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 122   |     331|       6.962|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 122   |     215|     119.771|   4.1%/ 17|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 119   |     449|     101.520|   0.8%/ 91|   0.8%/ 89|   0.8%/ 89|   0.8%/ 88 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 120   |    1336|     204.423|   3.0%/ 23|   2.0%/ 34|   1.8%/ 38|   1.6%/ 44 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 120   |      31|      16.425|   0.1%/548|   0.1%/675|   0.1%/705|   0.1%/730 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 122   |      56|       8.143|   2.9%/ 24|   3.7%/ 19|   3.8%/ 18|   4.0%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 119   |      79|      17.696|   0.6%/120|   0.2%/385|   0.1%/741|   0.0%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 121   |      74|      10.700|   3.9%/ 18|   4.4%/ 16|   4.6%/ 15|   4.7%/ 15 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 122   |      80|      28.730|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  76   |     109|       4.148|   5.3%/ 13|   5.2%/ 13|   5.2%/ 13|   5.2%/ 13 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 122   |     124|       3.798|   0.1%/545|   0.1%/492|   0.1%/480|   0.1%/468 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 122   |     124|       6.136|   0.2%/439|   0.2%/430|   0.2%/427|   0.2%/425 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 122   |     159|      39.011|   0.2%/281|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 122   |   46999|     371.302|   1.5%/ 48|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 122   |     777|     289.897|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70|   1.0%/ 70 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 122   |     333|       9.272|   2.0%/ 34|   2.4%/ 29|   2.5%/ 28|   2.6%/ 27 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  68   |      11|       0.369|   1.0%/ 72|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  22   |      10|       4.067|   0.0%/ ***|   5.2%/ 13|   6.7%/ 10|   8.2%/  8 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  77   |      53|       1.759|   2.2%/ 31|   3.2%/ 22|   3.4%/ 20|   3.7%/ 19 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 122   |    6164|     353.094|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 122   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 122   |     117|      18.129|   1.2%/ 57|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 122   |      69|       3.101|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 122   |     897|       4.352|   0.9%/ 76|   0.7%/ 96|   0.7%/102|   0.6%/110 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 122   |     492|     236.776|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.0%/ 66 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 122   |     256|      47.633|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 122   |     436|      93.453|   2.6%/ 26|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 122   |    6022|      27.454|   0.6%/125|   0.4%/192|   0.3%/221|   0.3%/260 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 122   |    1455|     344.949|   2.3%/ 30|   2.1%/ 33|   2.0%/ 34|   1.9%/ 35 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 122   |      50|       7.006|   3.7%/ 19|   3.8%/ 18|   3.9%/ 18|   3.9%/ 18 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 122   |   19864|     618.200|   1.2%/ 59|   1.0%/ 68|   1.0%/ 70|   0.9%/ 73 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 122   |    2041|      18.807|   0.8%/ 90|   0.6%/108|   0.6%/114|   0.6%/121 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 122   |    1710|      44.561|   0.5%/150|   0.5%/147|   0.5%/146|   0.5%/145 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 122   |    1736|     168.957|   0.2%/324|   0.2%/387|   0.2%/406|   0.2%/427 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 122   |     173|      63.007|   0.8%/ 85|   0.7%/ 99|   0.7%/103|   0.7%/106 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 122   |    2317|     119.416|   1.2%/ 60|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 122   |   14001|      95.410|   1.1%/ 66|   1.0%/ 72|   0.9%/ 74|   0.9%/ 76 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  63   |       5|       0.404|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 122   |    2919|      85.304|   1.3%/ 55|   1.1%/ 65|   1.0%/ 69|   0.9%/ 73 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 122   |     207|      12.788|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 122   |     590|      84.659|   1.8%/ 39|   1.4%/ 49|   1.3%/ 52|   1.2%/ 56 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 100   |      67|       8.491|   0.3%/248|   0.2%/294|   0.2%/307|   0.2%/320 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 122   |      27|       4.765|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 122   |      28|       5.132|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 122   |     118|      56.281|   0.3%/245|   0.4%/187|   0.4%/177|   0.4%/168 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 115   |      93|       5.856|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 122   |    8084|     137.547|   3.5%/ 19|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 122   |   28444|     603.906|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 122   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 122   |     741|      17.470|   0.6%/116|   0.5%/132|   0.5%/136|   0.5%/142 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 122   |    5755|     556.695|   0.2%/375|   0.2%/431|   0.2%/448|   0.1%/466 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 122   |    1980|     230.177|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 122   |      47|       2.687|   4.1%/ 17|   2.9%/ 24|   2.6%/ 27|   2.2%/ 31 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 122   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 122   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 122   |      18|       2.433|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 122   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 122   |      50|       4.265|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 122   |    5700|      68.549|   0.3%/229|   0.3%/247|   0.3%/251|   0.3%/256 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 122   |  152242|     461.977|   0.7%/ 99|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 122   |    1713|      40.904|   1.1%/ 64|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 122   |     350|      35.354|   0.3%/253|   0.3%/261|   0.3%/262|   0.3%/263 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 122   |   46183|     695.149|   0.1%/479|   0.1%/499|   0.1%/503|   0.1%/508 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 122   |      36|      10.157|   0.7%/106|   0.5%/148|   0.4%/165|   0.4%/187 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 122   |     145|       4.258|   4.3%/ 16|   3.8%/ 18|   3.6%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 122   |     166|       5.165|   3.2%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 25 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 121   |     185|      10.332|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 122   |      45|       2.943|   7.3%/  9|   7.6%/  9|   7.8%/  9|   8.0%/  9 |

