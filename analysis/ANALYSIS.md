# State and Country COVID-19 Analysis #
## Updated: at 2020-09-11 for data as of 2020-09-10 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.7% of deaths and 57.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 163   |   33028|    1697.800|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 163   |   15998|    1801.105|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 163   |   14279|     361.382|   0.8%/ 91|   0.7%/104|   0.6%/108|   0.6%/112 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 163   |   14394|     496.411|   0.9%/ 74|   0.7%/ 93|   0.7%/100|   0.6%/108 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 163   |   12471|     580.634|   0.8%/ 84|   0.7%/105|   0.6%/113|   0.6%/121 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 163   |    9180|    1321.021|   0.1%/520|   0.1%/564|   0.1%/576|   0.1%/590 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 163   |    8463|     667.829|   0.2%/290|   0.2%/292|   0.2%/292|   0.2%/293 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 163   |    7819|     610.736|   0.2%/399|   0.2%/427|   0.2%/435|   0.2%/443 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 163   |    6864|     687.317|   0.2%/397|   0.2%/383|   0.2%/380|   0.2%/376 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 163   |    6317|     594.974|   1.0%/ 70|   0.9%/ 79|   0.9%/ 81|   0.8%/ 84 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 163   |  192813|     585.089|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/193 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 163   |  130663|     618.052|   0.6%/110|   0.6%/123|   0.5%/127|   0.5%/131 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 163   |   76740|      56.376|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 163   |   70043|     553.361|   0.7%/ 93|   0.7%/101|   0.7%/103|   0.7%/105 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 163   |   41042|     617.766|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 163   |   35585|     590.731|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 163   |   30804|     459.248|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 163   |   30904|     961.800|   0.5%/132|   0.5%/148|   0.5%/152|   0.4%/156 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 163   |   29575|     627.909|   0.2%/401|   0.2%/348|   0.2%/337|   0.2%/327 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 163   |   22881|     274.430|   0.5%/129|   0.5%/141|   0.5%/145|   0.5%/148 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 163   |    2343|     477.906|   0.6%/107|   0.6%/122|   0.5%/127|   0.5%/132 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 163   |      45|      60.953|   0.8%/ 83|   0.7%/ 94|   0.7%/ 98|   0.7%/102 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 163   |    5362|     736.736|   0.5%/140|   0.4%/184|   0.3%/199|   0.3%/217 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 163   |     959|     317.636|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 163   |   14279|     361.382|   0.8%/ 91|   0.7%/104|   0.6%/108|   0.6%/112 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 163   |    1982|     344.193|   0.2%/403|   0.2%/421|   0.2%/425|   0.2%/430 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 163   |    4474|    1254.915|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 163   |     612|     627.981|   0.1%/691|   0.1%/733|   0.1%/744|   0.1%/756 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 163   |   12471|     580.634|   0.8%/ 84|   0.7%/105|   0.6%/113|   0.6%/121 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 163   |    6317|     594.974|   1.0%/ 70|   0.9%/ 79|   0.9%/ 81|   0.8%/ 84 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 163   |      96|      68.004|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 163   |     421|     235.569|   1.3%/ 53|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 163   |    8463|     667.829|   0.2%/290|   0.2%/292|   0.2%/292|   0.2%/293 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 163   |    3413|     506.908|   0.3%/226|   0.3%/239|   0.3%/242|   0.3%/246 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 163   |    1211|     383.701|   0.8%/ 86|   0.8%/ 87|   0.8%/ 87|   0.8%/ 87 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 163   |     496|     170.355|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 163   |    1031|     230.806|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82|   0.8%/ 82 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 163   |    5218|    1122.530|   0.4%/154|   0.4%/186|   0.4%/196|   0.3%/207 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 163   |     135|     100.590|   0.2%/442|   0.1%/582|   0.1%/636|   0.1%/701 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 163   |    3829|     633.381|   0.2%/373|   0.2%/391|   0.2%/396|   0.2%/401 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 163   |    9180|    1321.021|   0.1%/520|   0.1%/564|   0.1%/576|   0.1%/590 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 163   |    6864|     687.317|   0.2%/397|   0.2%/383|   0.2%/380|   0.2%/376 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 163   |    1941|     344.117|   0.3%/208|   0.3%/235|   0.3%/243|   0.3%/251 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 163   |    2701|     907.568|   0.8%/ 92|   0.6%/111|   0.6%/117|   0.6%/123 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 163   |    1701|     277.191|   0.9%/ 77|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 163   |     124|     116.120|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 163   |     419|     216.386|   0.6%/120|   0.6%/119|   0.6%/119|   0.6%/118 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 163   |    1465|     475.736|   0.9%/ 80|   0.7%/101|   0.6%/109|   0.6%/117 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 163   |     435|     319.942|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 163   |   15998|    1801.105|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 163   |     821|     391.461|   0.5%/143|   0.4%/155|   0.4%/158|   0.4%/162 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 163   |   33028|    1697.800|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 163   |    2994|     285.505|   0.9%/ 76|   0.9%/ 79|   0.9%/ 79|   0.9%/ 80 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 163   |     160|     210.267|   0.9%/ 75|   0.9%/ 80|   0.9%/ 81|   0.8%/ 82 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 163   |    4360|     373.015|   0.5%/145|   0.5%/153|   0.4%/155|   0.4%/157 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 163   |     895|     226.304|   0.9%/ 77|   0.8%/ 90|   0.7%/ 94|   0.7%/ 99 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 163   |     503|     119.219|   0.9%/ 80|   0.8%/ 88|   0.8%/ 90|   0.7%/ 93 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 163   |    7819|     610.736|   0.2%/399|   0.2%/427|   0.2%/435|   0.2%/443 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 163   |     511|     160.050|   1.5%/ 46|   1.4%/ 51|   1.3%/ 52|   1.3%/ 54 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 163   |    1064|    1004.520|   0.2%/421|   0.2%/410|   0.2%/408|   0.2%/406 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 163   |    3030|     588.430|   0.9%/ 77|   0.8%/ 92|   0.7%/ 96|   0.7%/101 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 163   |     177|     199.595|   0.5%/143|   0.4%/161|   0.4%/166|   0.4%/171 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 163   |    2004|     293.231|   1.2%/ 58|   1.0%/ 67|   1.0%/ 69|   1.0%/ 72 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 163   |   14394|     496.411|   0.9%/ 74|   0.7%/ 93|   0.7%/100|   0.6%/108 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 163   |  192813|     585.089|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/193 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 163   |     435|     135.604|   0.5%/134|   0.4%/166|   0.4%/177|   0.4%/189 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 163   |      58|      92.953|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 163   |    2730|     319.836|   0.5%/141|   0.5%/145|   0.5%/146|   0.5%/148 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 163   |    1998|     262.408|   0.3%/220|   0.2%/291|   0.2%/316|   0.2%/346 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 163   |     267|     149.005|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.6%/ 42 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 163   |    1191|     204.618|   0.5%/133|   0.5%/138|   0.5%/139|   0.5%/140 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 151   |      44|      75.349|   0.2%/437|   0.1%/757|   0.1%/903|   0.1%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 163   |    1425|      44.214|   0.1%/678|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 163   |     333|     116.978|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 163   |    1597|      37.134|   0.5%/126|   0.5%/135|   0.5%/138|   0.5%/140 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 163   |     127|       4.088|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 48 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 163   |   11135|     247.772|   2.3%/ 29|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 163   |     913|     308.686|   0.3%/201|   0.3%/229|   0.3%/237|   0.3%/246 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 163   |     874|      34.012|   1.9%/ 37|   1.4%/ 49|   1.3%/ 53|   1.2%/ 58 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 163   |     742|      83.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 163   |     556|      55.203|   0.4%/172|   0.4%/170|   0.4%/169|   0.4%/169 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 163   |     204|     132.235|   0.7%/101|   0.7%/103|   0.7%/103|   0.7%/103 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 163   |    4675|      27.748|   0.9%/ 80|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 163   |     732|      77.763|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 91 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 163   |    9906|     859.607|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 158   |      40|       3.440|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 163   |    5817|     507.139|   1.2%/ 57|   1.1%/ 61|   1.1%/ 63|   1.1%/ 64 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 163   |     699|     211.883|   1.2%/ 56|   1.1%/ 63|   1.1%/ 65|   1.0%/ 68 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 163   |       9|       3.929|   7.1%/ 10|   8.0%/  8|   8.2%/  8|   8.5%/  8 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 163   |  130663|     618.052|   0.6%/110|   0.6%/123|   0.5%/127|   0.5%/131 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 163   |     717|     103.175|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 163   |      56|       2.666|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 151   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 163   |     417|      15.727|   0.1%/933|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 163   |    9221|     242.669|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 111   |      62|      11.325|   0.1%/795|   0.1%/902|   0.1%/961|   0.1%/ *** |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 136   |      79|       4.842|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 163   |   11820|     618.640|   0.4%/155|   0.4%/164|   0.4%/167|   0.4%/169 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 163   |    4737|       3.378|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 163   |   22846|     462.505|   1.4%/ 51|   1.2%/ 59|   1.1%/ 61|   1.1%/ 64 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 163   |     554|     109.497|   2.2%/ 31|   2.0%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 163   |     205|      50.378|   1.1%/ 64|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 163   |     104|       9.266|   0.8%/ 83|   1.0%/ 70|   1.0%/ 67|   1.1%/ 65 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 163   |     628|     107.909|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 163   |    1933|     186.637|   1.2%/ 60|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 163   |    6888|     394.338|   0.5%/142|   0.5%/142|   0.5%/142|   0.5%/143 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 163   |    5601|      55.859|   0.3%/214|   0.3%/218|   0.3%/219|   0.3%/221 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 163   |     790|     121.805|   0.8%/ 87|   0.7%/105|   0.6%/111|   0.6%/117 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 142   |      83|      61.107|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 159   |    1021|      10.353|   2.0%/ 34|   1.7%/ 41|   1.6%/ 43|   1.5%/ 45 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 163   |     337|      60.938|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 163   |   30804|     459.248|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 163   |      53|      24.547|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 163   |     119|      50.846|   1.0%/ 67|   0.0%/ --|   0.0%/ --|   0.3%/206 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 160   |      20|       5.248|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 163   |    9349|     112.442|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 163   |     294|       9.719|   0.4%/196|   0.1%/659|   0.0%/ ***|   0.0%/ -- |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 163   |     297|      27.665|   1.1%/ 65|   1.1%/ 62|   1.1%/ 62|   1.1%/ 61 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 163   |    2970|     178.887|   0.6%/108|   0.5%/135|   0.5%/144|   0.4%/154 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 149   |      64|       5.236|   0.8%/ 86|   0.8%/ 90|   0.8%/ 92|   0.7%/ 93 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 138   |      38|      23.825|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 159   |     215|      18.569|   0.5%/150|   0.5%/148|   0.5%/148|   0.5%/147 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 163   |    2092|     228.416|   1.1%/ 65|   1.1%/ 65|   1.1%/ 66|   1.0%/ 66 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 163   |     626|      64.094|   0.2%/405|   0.2%/358|   0.2%/347|   0.2%/337 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 163   |   76740|      56.376|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 163   |    8438|      31.615|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 163   |   22881|     274.430|   0.5%/129|   0.5%/141|   0.5%/145|   0.5%/148 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 163   |    7876|     201.282|   1.1%/ 65|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 163   |    1779|     361.470|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 163   |    1105|     120.249|   1.4%/ 51|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 163   |   35585|     590.731|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 163   |      38|      14.066|   5.5%/ 12|   6.3%/ 11|   6.5%/ 10|   6.7%/ 10 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 163   |    1428|      11.336|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69|   1.0%/ 69 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 163   |      17|       1.618|   2.9%/ 24|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 163   |    1684|      90.103|   0.7%/102|   0.5%/130|   0.5%/139|   0.5%/150 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 163   |     628|      13.205|   0.6%/115|   0.4%/194|   0.3%/234|   0.2%/293 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 163   |     524|     291.728|   0.2%/442|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 160   |     554|     125.238|   0.4%/169|   0.4%/173|   0.4%/174|   0.4%/175 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 161   |     980|     150.027|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 161   |      35|      18.479|   0.3%/229|   0.3%/228|   0.3%/229|   0.3%/229 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 163   |     222|      32.518|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 160   |      82|      18.356|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 162   |     327|      47.523|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.5%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 163   |      87|      31.220|   0.1%/617|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 117   |     208|       7.936|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 163   |     128|       3.915|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 163   |     127|       6.278|   0.1%/532|   0.2%/433|   0.2%/413|   0.2%/395 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 163   |     161|      39.381|   0.1%/624|   0.1%/547|   0.1%/531|   0.1%/516 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 163   |   70043|     553.361|   0.7%/ 93|   0.7%/101|   0.7%/103|   0.7%/105 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 163   |    1098|     409.622|   0.9%/ 76|   1.0%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 163   |    1632|      45.502|   2.9%/ 24|   2.6%/ 27|   2.5%/ 27|   2.4%/ 28 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 109   |      29|       0.974|   2.3%/ 30|   2.7%/ 26|   2.8%/ 25|   2.8%/ 24 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  63   |      96|      39.068|   3.2%/ 22|   1.5%/ 45|   1.1%/ 60|   0.8%/ 90 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 118   |     345|      11.514|   4.0%/ 17|   3.3%/ 21|   3.1%/ 22|   2.9%/ 24 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 163   |    6291|     360.365|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 163   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 163   |     145|      22.384|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 163   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 163   |    1070|       5.189|   0.4%/167|   0.4%/159|   0.4%/157|   0.4%/155 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 163   |     637|     306.626|   0.7%/103|   0.7%/101|   0.7%/101|   0.7%/100 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 163   |     265|      49.396|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 163   |     759|     162.740|   1.1%/ 62|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 163   |    6383|      29.100|   0.1%/631|   0.1%/725|   0.1%/753|   0.1%/783 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 163   |    2155|     510.798|   0.6%/111|   0.5%/131|   0.5%/137|   0.5%/143 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  46   |       5|       0.560|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 163   |     549|      76.698|   4.7%/ 14|   4.3%/ 16|   4.2%/ 16|   4.1%/ 17 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 163   |   30904|     961.800|   0.5%/132|   0.5%/148|   0.5%/152|   0.4%/156 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 163   |    4154|      38.279|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 163   |    2167|      56.461|   0.5%/130|   0.5%/135|   0.5%/136|   0.5%/138 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 163   |    1852|     180.230|   0.2%/423|   0.2%/427|   0.2%/428|   0.2%/429 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 163   |     205|      74.498|   0.3%/214|   0.3%/205|   0.3%/202|   0.3%/199 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 163   |    4099|     211.244|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 163   |   18215|     124.127|   0.6%/119|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 104   |      21|       1.726|   4.0%/ 17|   3.6%/ 19|   3.4%/ 20|   5.0%/ 14 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 163   |    4228|     123.560|   0.8%/ 92|   0.7%/100|   0.7%/102|   0.7%/105 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 163   |     300|      18.501|   0.4%/164|   0.3%/252|   0.2%/291|   0.2%/343 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 163   |     736|     105.638|   0.2%/318|   0.1%/508|   0.1%/593|   0.1%/711 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 141   |      72|       9.088|   0.3%/268|   0.3%/222|   0.3%/213|   0.3%/205 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 163   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 163   |      37|       6.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 163   |     136|      64.862|   0.1%/516|   0.1%/650|   0.1%/695|   0.1%/746 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 156   |      98|       6.177|   0.1%/970|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 163   |   15618|     265.720|   0.8%/ 88|   0.6%/115|   0.6%/124|   0.5%/135 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 163   |   29575|     627.909|   0.2%/401|   0.2%/348|   0.2%/337|   0.2%/327 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 163   |      12|       0.562|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 163   |     837|      19.728|   0.1%/618|   0.1%/995|   0.1%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 163   |    5844|     565.274|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 163   |    2019|     234.635|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 163   |     154|       8.788|   2.8%/ 25|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 163   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 163   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 163   |      33|       4.401|   1.1%/ 64|   1.4%/ 51|   1.4%/ 48|   1.5%/ 46 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 163   |      42|      30.602|   6.4%/ 11|   6.8%/ 10|   6.9%/ 10|   6.9%/ 10 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 163   |      99|       8.405|   1.8%/ 38|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 163   |    6628|      79.707|   0.7%/ 97|   0.8%/ 86|   0.8%/ 83|   0.9%/ 81 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 163   |  192813|     585.089|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/193 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  49   |      49|       1.227|   4.4%/ 16|   5.1%/ 13|   5.0%/ 14|   4.8%/ 14 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 163   |    3063|      73.137|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 163   |     395|      39.972|   0.3%/214|   0.3%/216|   0.3%/217|   0.3%/218 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 163   |   41042|     617.766|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 163   |      46|      13.147|   0.4%/184|   0.2%/294|   0.2%/349|   0.2%/429 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 163   |     379|      11.116|   1.6%/ 42|   1.4%/ 48|   1.4%/ 49|   1.4%/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 163   |     468|      14.527|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  42   |      35|       0.364|   1.0%/ 70|   0.1%/799|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 162   |     305|      17.029|   0.4%/166|   0.3%/227|   0.3%/249|   0.3%/274 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 163   |     236|      15.571|   1.6%/ 43|   1.2%/ 56|   1.1%/ 61|   1.0%/ 67 |

