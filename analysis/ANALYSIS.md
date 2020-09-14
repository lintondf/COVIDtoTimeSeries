# State and Country COVID-19 Analysis #
## Updated: at 2020-09-14 for data as of 2020-09-13 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 39.1% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.6% of deaths and 56.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 166   |   33042|    1698.525|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 166   |   16018|    1803.353|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 166   |   14713|     507.416|   0.9%/ 76|   0.8%/ 91|   0.7%/ 96|   0.7%/102 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 166   |   14559|     368.471|   0.8%/ 91|   0.7%/101|   0.7%/104|   0.6%/107 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 166   |   12768|     594.468|   0.9%/ 78|   0.8%/ 88|   0.8%/ 91|   0.7%/ 93 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 166   |    9216|    1326.104|   0.1%/506|   0.1%/533|   0.1%/540|   0.1%/547 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 166   |    8533|     673.413|   0.3%/258|   0.3%/250|   0.3%/248|   0.3%/246 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 166   |    7854|     613.509|   0.2%/422|   0.2%/453|   0.1%/462|   0.1%/471 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 166   |    6908|     691.726|   0.2%/398|   0.2%/389|   0.2%/387|   0.2%/384 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 166   |    6462|     608.639|   0.9%/ 76|   0.8%/ 86|   0.8%/ 89|   0.8%/ 92 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 166   |  195078|     591.964|   0.4%/161|   0.4%/173|   0.4%/176|   0.4%/180 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 166   |  132828|     628.291|   0.6%/112|   0.6%/123|   0.6%/126|   0.5%/129 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 166   |   80083|      58.832|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 166   |   71461|     564.563|   0.7%/ 95|   0.7%/102|   0.7%/104|   0.7%/105 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 166   |   41717|     627.929|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 166   |   35609|     591.131|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 166   |   30878|     460.339|   0.1%/979|   0.1%/889|   0.1%/868|   0.1%/848 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 166   |   31056|     966.520|   0.5%/146|   0.4%/166|   0.4%/172|   0.4%/178 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 166   |   29743|     631.477|   0.2%/406|   0.2%/364|   0.2%/355|   0.2%/346 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 166   |   23223|     278.527|   0.5%/130|   0.5%/139|   0.5%/142|   0.5%/144 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 166   |    2385|     486.318|   0.7%/102|   0.6%/110|   0.6%/113|   0.6%/116 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 166   |      46|      62.784|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 166   |    5413|     743.642|   0.4%/157|   0.3%/207|   0.3%/224|   0.3%/245 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 166   |    1003|     332.257|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 166   |   14559|     368.471|   0.8%/ 91|   0.7%/101|   0.7%/104|   0.6%/107 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 166   |    1992|     345.908|   0.2%/403|   0.2%/415|   0.2%/419|   0.2%/422 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 166   |    4478|    1255.996|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 166   |     614|     630.276|   0.1%/587|   0.1%/578|   0.1%/575|   0.1%/572 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 166   |   12768|     594.468|   0.9%/ 78|   0.8%/ 88|   0.8%/ 91|   0.7%/ 93 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 166   |    6462|     608.639|   0.9%/ 76|   0.8%/ 86|   0.8%/ 89|   0.8%/ 92 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 166   |     105|      74.277|   3.0%/ 23|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 166   |     433|     242.046|   1.1%/ 63|   0.9%/ 80|   0.8%/ 86|   0.7%/ 93 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 166   |    8533|     673.413|   0.3%/258|   0.3%/250|   0.3%/248|   0.3%/246 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 166   |    3444|     511.532|   0.3%/221|   0.3%/228|   0.3%/229|   0.3%/231 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 166   |    1236|     391.653|   0.7%/ 95|   0.7%/100|   0.7%/101|   0.7%/103 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 166   |     515|     176.715|   1.2%/ 59|   1.3%/ 54|   1.3%/ 52|   1.4%/ 51 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 166   |    1061|     237.518|   1.0%/ 72|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 166   |    5274|    1134.520|   0.4%/159|   0.4%/185|   0.4%/193|   0.3%/202 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 166   |     136|     100.995|   0.2%/422|   0.1%/508|   0.1%/535|   0.1%/565 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 166   |    3848|     636.508|   0.2%/390|   0.2%/414|   0.2%/420|   0.2%/427 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 166   |    9216|    1326.104|   0.1%/506|   0.1%/533|   0.1%/540|   0.1%/547 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 166   |    6908|     691.726|   0.2%/398|   0.2%/389|   0.2%/387|   0.2%/384 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 166   |    1964|     348.162|   0.4%/177|   0.4%/181|   0.4%/182|   0.4%/183 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 166   |    2749|     923.665|   0.7%/ 95|   0.6%/112|   0.6%/117|   0.6%/122 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 166   |    1746|     284.426|   0.8%/ 91|   0.8%/ 91|   0.8%/ 91|   0.8%/ 92 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 166   |     132|     123.748|   2.0%/ 34|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 166   |     430|     222.468|   0.7%/ 93|   0.8%/ 86|   0.8%/ 84|   0.8%/ 82 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 166   |    1491|     483.982|   0.8%/ 85|   0.7%/105|   0.6%/112|   0.6%/119 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 166   |     436|     320.442|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 166   |   16018|    1803.353|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 166   |     830|     396.035|   0.4%/158|   0.4%/175|   0.4%/180|   0.4%/186 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 166   |   33042|    1698.525|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 166   |    3075|     293.217|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 166   |     166|     217.934|   1.1%/ 60|   1.2%/ 58|   1.2%/ 58|   1.2%/ 57 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 166   |    4427|     378.768|   0.5%/135|   0.5%/137|   0.5%/137|   0.5%/137 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 166   |     917|     231.641|   1.0%/ 72|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 166   |     514|     121.865|   0.8%/ 83|   0.8%/ 91|   0.7%/ 93|   0.7%/ 96 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 166   |    7854|     613.509|   0.2%/422|   0.2%/453|   0.1%/462|   0.1%/471 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 166   |     537|     168.130|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 166   |    1071|    1010.588|   0.2%/370|   0.2%/352|   0.2%/348|   0.2%/343 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 166   |    3104|     602.801|   0.9%/ 75|   0.8%/ 84|   0.8%/ 86|   0.8%/ 89 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 166   |     181|     204.039|   0.7%/102|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 166   |    2083|     304.889|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 166   |   14713|     507.416|   0.9%/ 76|   0.8%/ 91|   0.7%/ 96|   0.7%/102 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 166   |  195078|     591.964|   0.4%/161|   0.4%/173|   0.4%/176|   0.4%/180 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 166   |     439|     137.067|   0.5%/149|   0.4%/186|   0.4%/198|   0.3%/211 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 166   |      58|      92.950|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 166   |    2760|     323.360|   0.4%/164|   0.4%/181|   0.4%/187|   0.4%/193 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 166   |    2011|     264.139|   0.3%/237|   0.2%/305|   0.2%/327|   0.2%/353 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 166   |     279|     155.895|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 166   |    1211|     208.000|   0.6%/124|   0.6%/125|   0.6%/125|   0.6%/125 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 154   |      44|      75.885|   0.1%/618|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 166   |    1427|      44.266|   0.1%/892|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 166   |     344|     120.746|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.0%/ 66 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 166   |    1620|      37.684|   0.5%/131|   0.5%/139|   0.5%/142|   0.5%/144 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 166   |     133|       4.285|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 166   |   11835|     263.365|   2.2%/ 32|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 166   |     920|     311.164|   0.3%/219|   0.3%/251|   0.3%/261|   0.3%/271 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 166   |     937|      36.493|   1.5%/ 46|   1.0%/ 67|   0.9%/ 76|   0.8%/ 87 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 166   |     748|      84.047|   0.1%/650|   0.1%/557|   0.1%/536|   0.1%/515 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 166   |     562|      55.839|   0.4%/180|   0.4%/180|   0.4%/180|   0.4%/180 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 166   |     209|     135.627|   0.8%/ 88|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 166   |    4780|      28.376|   0.8%/ 84|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 166   |     749|      79.565|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 166   |    9917|     860.480|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 161   |      40|       3.437|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 166   |    6062|     528.471|   1.0%/ 67|   0.9%/ 77|   0.9%/ 80|   0.8%/ 84 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 166   |     718|     217.365|   1.1%/ 64|   0.9%/ 76|   0.9%/ 79|   0.8%/ 83 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 166   |      11|       4.695|   6.2%/ 11|   6.5%/ 10|   6.6%/ 10|   6.6%/ 10 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 166   |  132828|     628.291|   0.6%/112|   0.6%/123|   0.6%/126|   0.5%/129 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 166   |     740|     106.436|   1.2%/ 60|   1.1%/ 65|   1.0%/ 67|   1.0%/ 69 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 166   |      56|       2.678|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 154   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 166   |     418|      15.728|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 166   |    9232|     242.944|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 114   |      62|      11.326|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 139   |      80|       4.896|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 166   |   11975|     626.725|   0.5%/153|   0.4%/159|   0.4%/160|   0.4%/161 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 166   |    4741|       3.381|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 166   |   23566|     477.095|   1.2%/ 55|   1.1%/ 64|   1.0%/ 66|   1.0%/ 69 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 166   |     597|     118.124|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 166   |     214|      52.412|   1.3%/ 53|   1.4%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 166   |     107|       9.549|   0.9%/ 80|   1.0%/ 70|   1.0%/ 68|   1.1%/ 66 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 166   |     630|     108.155|   0.1%/ ***|   0.1%/910|   0.1%/887|   0.1%/865 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 166   |    1993|     192.366|   1.1%/ 65|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 166   |    6992|     400.252|   0.5%/139|   0.5%/139|   0.5%/139|   0.5%/138 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 166   |    5654|      56.381|   0.3%/216|   0.3%/221|   0.3%/222|   0.3%/223 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 166   |     803|     123.774|   0.7%/ 99|   0.6%/122|   0.5%/130|   0.5%/138 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 145   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 162   |    1063|      10.769|   1.7%/ 40|   1.4%/ 49|   1.3%/ 53|   1.2%/ 56 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 166   |     337|      60.999|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 166   |   30878|     460.339|   0.1%/979|   0.1%/889|   0.1%/868|   0.1%/848 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 166   |      53|      24.497|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 166   |     117|      49.651|   0.0%/ --|   0.3%/206|   1.0%/ 69|   1.0%/ 70 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 163   |      20|       5.241|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 166   |    9360|     112.563|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 166   |     294|       9.720|   0.3%/249|   0.1%/949|   0.0%/ ***|   0.0%/ -- |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 166   |     306|      28.567|   1.1%/ 66|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 166   |    3008|     181.183|   0.6%/122|   0.4%/155|   0.4%/165|   0.4%/178 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 152   |      65|       5.299|   0.6%/122|   0.4%/159|   0.4%/172|   0.4%/189 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 141   |      39|      24.522|   0.5%/131|   0.6%/116|   0.6%/113|   0.6%/110 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 162   |     219|      18.882|   0.5%/134|   0.6%/126|   0.6%/124|   0.6%/122 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 166   |    2139|     233.608|   0.9%/ 78|   0.8%/ 87|   0.8%/ 89|   0.7%/ 93 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 166   |     631|      64.567|   0.2%/324|   0.2%/280|   0.3%/270|   0.3%/261 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 166   |   80083|      58.832|   1.5%/ 46|   1.4%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 166   |    8766|      32.844|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 166   |   23223|     278.527|   0.5%/130|   0.5%/139|   0.5%/142|   0.5%/144 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 166   |    8100|     207.004|   1.0%/ 68|   1.0%/ 73|   0.9%/ 74|   0.9%/ 75 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 166   |    1781|     361.824|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 166   |    1142|     124.287|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 166   |   35609|     591.131|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 166   |      43|      15.776|   4.5%/ 15|   5.1%/ 13|   5.2%/ 13|   5.4%/ 13 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 166   |    1464|      11.626|   0.9%/ 76|   0.9%/ 80|   0.9%/ 80|   0.8%/ 81 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 166   |      18|       1.675|   2.0%/ 34|   3.4%/ 20|   5.0%/ 14|   6.3%/ 11 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 166   |    1691|      90.477|   0.5%/152|   0.3%/254|   0.2%/305|   0.2%/382 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 166   |     635|      13.346|   0.6%/123|   0.4%/185|   0.3%/210|   0.3%/242 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 166   |     516|     287.470|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 163   |     560|     126.726|   0.4%/172|   0.4%/175|   0.4%/175|   0.4%/175 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 164   |     997|     152.548|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 164   |      35|      18.577|   0.2%/327|   0.2%/389|   0.2%/411|   0.2%/437 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 166   |     244|      35.684|   3.2%/ 22|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 163   |      82|      18.331|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 165   |     361|      52.495|   3.2%/ 21|   3.2%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 166   |      87|      31.228|   0.1%/771|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 120   |     213|       8.103|   0.8%/ 89|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 166   |     129|       3.925|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 166   |     128|       6.308|   0.1%/536|   0.2%/454|   0.2%/437|   0.2%/421 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 166   |     161|      39.511|   0.1%/673|   0.1%/625|   0.1%/615|   0.1%/605 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 166   |   71461|     564.563|   0.7%/ 95|   0.7%/102|   0.7%/104|   0.7%/105 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 166   |    1128|     420.472|   0.9%/ 81|   0.9%/ 79|   0.9%/ 79|   0.9%/ 78 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 166   |    1785|      49.764|   2.6%/ 27|   2.3%/ 30|   2.2%/ 31|   2.1%/ 33 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 112   |      33|       1.096|   3.1%/ 22|   3.8%/ 18|   3.9%/ 18|   4.1%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  66   |     101|      40.928|   2.2%/ 32|   1.7%/ 41|   1.6%/ 43|   1.5%/ 45 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 121   |     368|      12.267|   3.4%/ 20|   2.6%/ 27|   2.4%/ 29|   2.2%/ 32 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 166   |    6299|     360.824|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 166   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 166   |     146|      22.549|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 166   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 166   |    1083|       5.252|   0.4%/180|   0.4%/175|   0.4%/174|   0.4%/173 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 166   |     649|     312.648|   0.7%/106|   0.7%/106|   0.7%/106|   0.7%/106 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 166   |     265|      49.401|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 166   |     781|     167.451|   1.0%/ 68|   1.0%/ 72|   0.9%/ 73|   0.9%/ 74 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 166   |    6398|      29.170|   0.1%/706|   0.1%/825|   0.1%/861|   0.1%/901 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 166   |    2188|     518.562|   0.6%/117|   0.5%/134|   0.5%/139|   0.5%/144 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  49   |       5|       0.560|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 166   |     605|      84.532|   4.0%/ 17|   3.4%/ 20|   3.2%/ 21|   3.0%/ 23 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 166   |   31056|     966.520|   0.5%/146|   0.4%/166|   0.4%/172|   0.4%/178 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 166   |    4358|      40.162|   1.6%/ 42|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 166   |    2199|      57.296|   0.5%/134|   0.5%/140|   0.5%/141|   0.5%/143 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 166   |    1862|     181.211|   0.2%/395|   0.2%/388|   0.2%/386|   0.2%/383 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 166   |     206|      75.060|   0.3%/264|   0.3%/267|   0.3%/268|   0.3%/270 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 166   |    4226|     217.774|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 166   |   18536|     126.317|   0.6%/117|   0.6%/118|   0.6%/119|   0.6%/119 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 107   |      23|       1.836|   1.8%/ 38|   3.2%/ 21|   1.6%/ 44|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 166   |    4308|     125.898|   0.7%/ 99|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 166   |     302|      18.605|   0.3%/198|   0.2%/319|   0.2%/376|   0.2%/458 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 166   |     738|     106.008|   0.2%/365|   0.1%/556|   0.1%/636|   0.1%/741 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 144   |      72|       9.143|   0.2%/347|   0.2%/331|   0.2%/328|   0.2%/326 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 166   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 166   |      38|       6.998|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 166   |     136|      64.965|   0.1%/730|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 159   |      99|       6.201|   0.1%/505|   0.1%/546|   0.1%/560|   0.1%/575 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 166   |   15858|     269.801|   0.7%/100|   0.5%/130|   0.5%/141|   0.5%/153 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 166   |   29743|     631.477|   0.2%/406|   0.2%/364|   0.2%/355|   0.2%/346 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 166   |      12|       0.560|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 166   |     839|      19.758|   0.1%/771|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 166   |    5849|     565.756|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 166   |    2022|     234.986|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 166   |     164|       9.358|   2.5%/ 27|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 166   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 166   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 166   |      36|       4.766|   1.9%/ 36|   2.4%/ 29|   2.5%/ 28|   2.6%/ 26 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 166   |      52|      38.215|   7.1%/ 10|   7.5%/  9|   7.6%/  9|   7.7%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 166   |     107|       9.099|   2.3%/ 30|   2.5%/ 28|   2.6%/ 27|   2.6%/ 26 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 166   |    6677|      80.301|   0.8%/ 91|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 166   |  195078|     591.964|   0.4%/161|   0.4%/173|   0.4%/176|   0.4%/180 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  52   |      55|       1.353|   5.2%/ 13|   4.0%/ 17|   3.6%/ 19|   3.2%/ 22 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 166   |    3225|      77.000|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 166   |     399|      40.387|   0.3%/206|   0.3%/206|   0.3%/206|   0.3%/206 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 166   |   41717|     627.929|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 166   |      46|      13.152|   0.2%/319|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 166   |     396|      11.605|   1.6%/ 43|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 166   |     491|      15.233|   1.8%/ 39|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  45   |      35|       0.364|   0.2%/290|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 165   |     309|      17.294|   0.4%/170|   0.3%/204|   0.3%/213|   0.3%/223 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 166   |     241|      15.903|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

