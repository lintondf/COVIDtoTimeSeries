# State and Country COVID-19 Analysis #
## Updated: at 2020-08-25 for data as of 2020-08-24 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.0% of deaths and 40.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.5% of deaths and 58.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 146   |   32899|    1691.165|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 146   |   15954|    1796.215|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 146   |   12412|     314.135|   1.2%/ 60|   1.1%/ 64|   1.1%/ 66|   1.0%/ 67 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 146   |   12500|     431.087|   1.8%/ 39|   1.6%/ 44|   1.5%/ 46|   1.4%/ 48 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 146   |   10896|     507.305|   1.6%/ 44|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 146   |    8946|    1287.291|   0.2%/432|   0.2%/437|   0.2%/439|   0.2%/440 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 146   |    8106|     639.706|   0.2%/306|   0.2%/304|   0.2%/304|   0.2%/303 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 146   |    7577|     591.897|   0.2%/318|   0.2%/315|   0.2%/315|   0.2%/314 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 146   |    6665|     667.328|   0.1%/464|   0.2%/446|   0.2%/442|   0.2%/437 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 146   |    5215|     491.147|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 146   |  178652|     542.119|   0.6%/118|   0.5%/127|   0.5%/129|   0.5%/132 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 146   |  116475|     550.940|   0.9%/ 77|   0.8%/ 83|   0.8%/ 84|   0.8%/ 85 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 146   |   61897|     489.005|   1.0%/ 68|   0.9%/ 76|   0.9%/ 78|   0.9%/ 81 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 146   |   59416|      43.649|   1.9%/ 37|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 146   |   40992|     617.016|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 146   |   35458|     588.621|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 146   |   30514|     454.919|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 146   |   28830|     612.095|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 146   |   28552|     888.592|   0.8%/ 87|   0.7%/ 97|   0.7%/100|   0.7%/104 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 146   |   21060|     252.586|   0.8%/ 88|   0.7%/102|   0.6%/107|   0.6%/111 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 146   |    2067|     421.559|   0.9%/ 80|   0.7%/ 97|   0.7%/103|   0.6%/110 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 146   |      31|      42.857|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 146   |    4901|     673.358|   1.0%/ 72|   0.8%/ 91|   0.7%/ 97|   0.7%/103 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 146   |     697|     230.998|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 146   |   12412|     314.135|   1.2%/ 60|   1.1%/ 64|   1.1%/ 66|   1.0%/ 67 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 146   |    1923|     333.918|   0.2%/355|   0.2%/375|   0.2%/380|   0.2%/385 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 146   |    4464|    1251.997|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 146   |     600|     616.567|   0.1%/466|   0.2%/424|   0.2%/413|   0.2%/402 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 146   |   10896|     507.305|   1.6%/ 44|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 146   |    5215|     491.147|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 146   |      49|      34.494|   2.3%/ 31|   2.5%/ 27|   2.6%/ 26|   2.7%/ 26 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 146   |     323|     180.786|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 146   |    8106|     639.706|   0.2%/306|   0.2%/304|   0.2%/304|   0.2%/303 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 146   |    3234|     480.373|   0.4%/179|   0.4%/175|   0.4%/174|   0.4%/174 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 146   |    1048|     332.188|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 146   |     433|     148.738|   0.7%/ 96|   0.7%/105|   0.6%/107|   0.6%/110 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 146   |     875|     195.777|   0.9%/ 78|   1.0%/ 72|   1.0%/ 70|   1.0%/ 69 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 146   |    4789|    1030.156|   0.8%/ 90|   0.7%/ 94|   0.7%/ 95|   0.7%/ 96 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 146   |     130|      96.721|   0.3%/208|   0.4%/189|   0.4%/184|   0.4%/179 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 146   |    3706|     612.929|   0.2%/328|   0.2%/364|   0.2%/374|   0.2%/385 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 146   |    8946|    1287.291|   0.2%/432|   0.2%/437|   0.2%/439|   0.2%/440 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 146   |    6665|     667.328|   0.1%/464|   0.2%/446|   0.2%/442|   0.2%/437 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 146   |    1816|     321.995|   0.5%/143|   0.5%/135|   0.5%/133|   0.5%/131 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 146   |    2311|     776.449|   1.2%/ 59|   1.0%/ 68|   1.0%/ 71|   0.9%/ 73 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 146   |    1468|     239.154|   0.6%/118|   0.6%/124|   0.5%/126|   0.5%/128 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 146   |      95|      89.205|   1.4%/ 50|   1.0%/ 71|   0.9%/ 78|   0.8%/ 88 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 146   |     382|     197.562|   0.6%/110|   0.6%/112|   0.6%/112|   0.6%/113 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 146   |    1233|     400.368|   1.6%/ 43|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 146   |     429|     315.640|   0.2%/449|   0.2%/447|   0.2%/445|   0.2%/442 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 146   |   15954|    1796.215|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 146   |     752|     358.813|   0.6%/112|   0.6%/119|   0.6%/121|   0.6%/123 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 146   |   32899|    1691.165|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 146   |    2573|     245.317|   1.0%/ 67|   1.0%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 146   |     137|     179.958|   1.3%/ 53|   1.4%/ 50|   1.4%/ 50|   1.4%/ 49 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 146   |    4014|     343.382|   0.6%/124|   0.5%/132|   0.5%/134|   0.5%/136 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 146   |     738|     186.600|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 146   |     429|     101.698|   1.0%/ 66|   0.9%/ 74|   0.9%/ 77|   0.9%/ 79 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 146   |    7577|     591.897|   0.2%/318|   0.2%/315|   0.2%/315|   0.2%/314 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 146   |     402|     125.721|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 146   |    1032|     973.844|   0.1%/588|   0.1%/540|   0.1%/528|   0.1%/517 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 146   |    2585|     501.982|   1.5%/ 47|   1.3%/ 55|   1.2%/ 57|   1.2%/ 60 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 146   |     163|     184.286|   0.8%/ 90|   0.7%/102|   0.7%/105|   0.6%/108 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 146   |    1590|     232.725|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 146   |   12500|     431.087|   1.8%/ 39|   1.6%/ 44|   1.5%/ 46|   1.4%/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 146   |  178652|     542.119|   0.6%/118|   0.5%/127|   0.5%/129|   0.5%/132 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 146   |     396|     123.380|   0.9%/ 77|   0.8%/ 92|   0.7%/ 96|   0.7%/101 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 146   |      58|      93.446|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 146   |    2482|     290.816|   0.4%/161|   0.4%/191|   0.3%/199|   0.3%/209 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 146   |    1886|     247.706|   0.7%/100|   0.7%/105|   0.7%/106|   0.6%/107 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 146   |     184|     102.639|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 146   |    1091|     187.384|   0.6%/116|   0.6%/126|   0.5%/128|   0.5%/131 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 134   |      36|      62.261|   1.5%/ 46|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 146   |    1405|      43.597|   0.3%/231|   0.2%/287|   0.2%/307|   0.2%/331 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 146   |     260|      91.473|   1.7%/ 42|   1.4%/ 49|   1.3%/ 51|   1.3%/ 54 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 146   |    1453|      33.789|   0.7%/100|   0.6%/108|   0.6%/110|   0.6%/112 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 146   |     106|       3.396|   1.7%/ 39|   1.3%/ 55|   1.1%/ 60|   1.0%/ 68 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 146   |    7348|     163.507|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 146   |     860|     290.940|   0.5%/129|   0.5%/148|   0.5%/153|   0.4%/158 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 146   |     598|      23.292|   3.4%/ 20|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 146   |     733|      82.308|   0.1%/686|   0.1%/655|   0.1%/648|   0.1%/642 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 146   |     527|      52.367|   0.4%/186|   0.2%/387|   0.1%/523|   0.1%/800 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 146   |     186|     120.605|   1.0%/ 72|   0.9%/ 74|   0.9%/ 74|   0.9%/ 75 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 146   |    3984|      23.649|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 146   |     642|      68.236|   0.6%/108|   0.7%/106|   0.7%/105|   0.7%/104 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 146   |    9996|     867.414|   0.1%/893|   0.1%/807|   0.1%/789|   0.1%/773 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 141   |      40|       3.370|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 146   |    4653|     405.653|   1.5%/ 45|   1.3%/ 52|   1.3%/ 54|   1.2%/ 56 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 146   |     561|     169.829|   1.7%/ 42|   1.5%/ 46|   1.5%/ 47|   1.5%/ 48 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 146   |       3|       1.404|   1.8%/ 38|   1.3%/ 53|   1.2%/ 59|   1.0%/ 67 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 146   |  116475|     550.940|   0.9%/ 77|   0.8%/ 83|   0.8%/ 84|   0.8%/ 85 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 146   |     569|      81.806|   1.4%/ 51|   1.2%/ 58|   1.1%/ 60|   1.1%/ 63 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 146   |      55|       2.646|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 134   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 146   |     409|      15.424|   0.2%/330|   0.2%/321|   0.2%/320|   0.2%/319 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 146   |    9127|     240.181|   0.1%/983|   0.1%/978|   0.1%/976|   0.1%/974 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  94   |      61|      11.146|   0.1%/688|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 119   |      76|       4.686|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 146   |   10940|     572.554|   0.5%/127|   0.5%/138|   0.5%/141|   0.5%/144 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 146   |    4717|       3.364|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 146   |   17967|     363.726|   2.1%/ 34|   1.8%/ 38|   1.7%/ 39|   1.7%/ 41 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 146   |     392|      77.593|   2.9%/ 23|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 146   |     174|      42.642|   0.6%/121|   0.5%/149|   0.4%/158|   0.4%/167 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 146   |      89|       7.913|   0.1%/542|   0.2%/444|   0.2%/423|   0.2%/402 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 146   |     623|     107.013|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 146   |    1605|     154.917|   1.3%/ 54|   1.2%/ 58|   1.2%/ 59|   1.1%/ 61 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 146   |    6307|     361.053|   0.5%/153|   0.5%/150|   0.5%/149|   0.5%/148 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 146   |    5310|      52.955|   0.3%/214|   0.3%/272|   0.2%/291|   0.2%/312 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 146   |     690|     106.385|   1.4%/ 50|   1.1%/ 62|   1.0%/ 66|   1.0%/ 70 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 125   |      84|      61.655|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 142   |     717|       7.263|   3.6%/ 19|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 146   |     335|      60.606|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 146   |   30514|     454.919|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 146   |      53|      24.496|   0.2%/360|   0.2%/410|   0.2%/422|   0.2%/436 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 146   |     116|      49.441|   5.3%/ 13|   2.9%/ 23|   2.4%/ 29|   1.2%/ 59 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 143   |      17|       4.610|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 146   |    9280|     111.608|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 146   |     270|       8.930|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.3%/ 52 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 146   |     242|      22.532|   0.8%/ 84|   0.9%/ 74|   1.0%/ 72|   1.0%/ 70 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 146   |    2640|     158.988|   1.2%/ 58|   1.1%/ 63|   1.1%/ 65|   1.0%/ 66 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 132   |      54|       4.415|   0.6%/116|   0.6%/120|   0.6%/121|   0.6%/121 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 121   |      34|      21.352|   0.3%/224|   0.1%/643|   0.1%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 142   |     204|      17.622|   0.5%/133|   0.3%/248|   0.2%/325|   0.1%/478 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 146   |    1698|     185.400|   0.7%/ 95|   0.5%/142|   0.4%/160|   0.4%/183 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 146   |     613|      62.727|   0.1%/593|   0.1%/572|   0.1%/568|   0.1%/565 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 146   |   59416|      43.649|   1.9%/ 37|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 146   |    6739|      25.249|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62|   1.1%/ 62 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 146   |   21060|     252.586|   0.8%/ 88|   0.7%/102|   0.6%/107|   0.6%/111 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 146   |    6536|     167.053|   1.3%/ 54|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 146   |    1779|     361.381|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 146   |     836|      90.970|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 146   |   35458|     588.621|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 146   |      16|       5.888|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 146   |    1182|       9.385|   0.9%/ 76|   1.1%/ 65|   1.1%/ 63|   1.1%/ 61 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 146   |      11|       1.032|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 146   |    1562|      83.588|   1.0%/ 66|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 146   |     563|      11.840|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 146   |     485|     270.179|   2.6%/ 27|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 143   |     522|     118.032|   0.5%/135|   0.4%/155|   0.4%/161|   0.4%/167 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 144   |    1544|     236.285|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 144   |      33|      17.291|   0.2%/373|   0.2%/340|   0.2%/331|   0.2%/322 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 146   |     129|      18.933|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 143   |      84|      18.702|   0.2%/391|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 145   |     205|      29.798|   3.6%/ 19|   3.4%/ 20|   3.3%/ 21|   3.3%/ 21 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 146   |      83|      29.651|   0.3%/201|   0.5%/152|   0.5%/142|   0.5%/134 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 100   |     186|       7.093|   1.4%/ 51|   0.5%/130|   0.3%/210|   0.1%/545 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 146   |     125|       3.820|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 146   |     125|       6.186|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 146   |     158|      38.714|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 146   |   61897|     489.005|   1.0%/ 68|   0.9%/ 76|   0.9%/ 78|   0.9%/ 81 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 146   |     954|     355.785|   0.7%/ 94|   0.7%/104|   0.7%/106|   0.6%/109 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 146   |     913|      25.437|   4.3%/ 16|   4.5%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  92   |      21|       0.695|   1.4%/ 49|   0.8%/ 83|   0.7%/100|   0.6%/123 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  46   |      54|      21.991|   5.7%/ 12|   6.7%/ 10|   7.8%/  9|   8.9%/  8 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 101   |     156|       5.193|   5.1%/ 13|   5.2%/ 13|   5.3%/ 13|   5.3%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 146   |    6219|     356.268|   0.1%/ ***|   0.1%/ ***|   0.1%/991|   0.1%/950 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 146   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 146   |     135|      20.973|   0.4%/157|   0.3%/210|   0.3%/230|   0.3%/253 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 146   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 146   |    1015|       4.923|   0.4%/163|   0.3%/206|   0.3%/220|   0.3%/236 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 146   |     570|     274.554|   0.6%/126|   0.5%/146|   0.5%/151|   0.4%/157 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 146   |     264|      49.227|   0.1%/478|   0.2%/399|   0.2%/383|   0.2%/368 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 146   |     651|     139.495|   1.3%/ 54|   1.1%/ 62|   1.1%/ 65|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 146   |    6270|      28.588|   0.2%/393|   0.1%/486|   0.1%/517|   0.1%/551 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 146   |    1943|     460.477|   1.0%/ 67|   0.9%/ 80|   0.8%/ 85|   0.8%/ 89 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  29   |       4|       0.448|   1.0%/ 68|   6.5%/ 11|   3.0%/ 23|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 146   |     218|      30.420|   6.0%/ 11|   6.3%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 146   |   28552|     888.592|   0.8%/ 87|   0.7%/ 97|   0.7%/100|   0.7%/104 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 146   |    3026|      27.888|   2.0%/ 34|   2.2%/ 31|   2.2%/ 31|   2.3%/ 30 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 146   |    1967|      51.250|   0.6%/118|   0.6%/117|   0.6%/116|   0.6%/116 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 146   |    1801|     175.212|   0.2%/416|   0.2%/417|   0.2%/417|   0.2%/418 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 146   |     198|      72.080|   0.3%/228|   0.1%/475|   0.1%/663|   0.1%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 146   |    3343|     172.297|   1.4%/ 49|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 146   |   16526|     112.619|   0.7%/106|   0.6%/116|   0.6%/118|   0.6%/121 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  87   |      13|       1.021|   7.7%/  9|   3.2%/ 21|   2.9%/ 23|   8.4%/  8 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 146   |    3699|     108.110|   1.0%/ 66|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 146   |     275|      16.980|   1.1%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 146   |     715|     102.732|   0.6%/112|   0.4%/160|   0.4%/179|   0.3%/203 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 124   |      69|       8.791|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 146   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 146   |      33|       6.101|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 146   |     133|      63.401|   0.3%/264|   0.2%/400|   0.2%/459|   0.1%/538 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 139   |      93|       5.852|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 146   |   13885|     236.235|   1.7%/ 41|   1.3%/ 54|   1.2%/ 58|   1.1%/ 63 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 146   |   28830|     612.095|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 146   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 146   |     825|      19.431|   0.3%/206|   0.3%/256|   0.3%/273|   0.2%/291 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 146   |    5815|     562.468|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 146   |    2000|     232.491|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 146   |      88|       5.005|   2.8%/ 24|   2.9%/ 24|   2.9%/ 23|   3.0%/ 23 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 146   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 146   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 146   |      30|       3.917|   0.9%/ 75|   0.3%/216|   0.2%/429|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 146   |       8|       5.865|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 146   |      55|       4.676|   1.2%/ 59|   1.5%/ 46|   1.6%/ 43|   1.7%/ 41 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 146   |    6131|      73.735|   0.3%/209|   0.3%/201|   0.3%/199|   0.4%/198 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 146   |  178652|     542.119|   0.6%/118|   0.5%/127|   0.5%/129|   0.5%/132 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  32   |      22|       0.539|   6.6%/ 10|   6.1%/ 11|   5.1%/ 14|   3.8%/ 18 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 146   |    2335|      55.750|   1.3%/ 51|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 146   |     373|      37.698|   0.4%/188|   0.4%/165|   0.4%/160|   0.4%/155 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 146   |   40992|     617.016|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 146   |      42|      11.854|   0.9%/ 75|   1.1%/ 65|   1.1%/ 62|   1.1%/ 60 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 146   |     287|       8.414|   2.5%/ 27|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 146   |     352|      10.921|   2.7%/ 25|   2.5%/ 28|   2.4%/ 28|   2.4%/ 29 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  25   |      27|       0.283|   2.9%/ 24|   1.3%/ 53|   2.6%/ 27|   2.6%/ 27 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 145   |     308|      17.218|   1.1%/ 61|   1.2%/ 57|   1.2%/ 56|   1.3%/ 55 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 146   |     180|      11.898|   2.7%/ 25|   0.7%/105|   0.9%/ 79|   0.7%/106 |

