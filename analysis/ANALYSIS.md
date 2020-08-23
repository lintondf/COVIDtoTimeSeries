# State and Country COVID-19 Analysis #
## Updated: at 2020-08-23 for data as of 2020-08-22 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.9% of deaths and 40.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 144   |   32888|    1690.578|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 144   |   15946|    1795.288|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 144   |   12171|     308.042|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 144   |   12175|     419.904|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 144   |   10612|     494.100|   1.8%/ 39|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 144   |    8919|    1283.361|   0.2%/426|   0.2%/431|   0.2%/432|   0.2%/433 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 144   |    8071|     636.939|   0.2%/290|   0.2%/280|   0.3%/277|   0.3%/274 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 144   |    7547|     589.484|   0.2%/295|   0.2%/280|   0.3%/276|   0.3%/273 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 144   |    6644|     665.308|   0.2%/459|   0.2%/434|   0.2%/428|   0.2%/422 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 144   |    5082|     478.660|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 144   |  176854|     536.664|   0.6%/110|   0.6%/115|   0.6%/116|   0.6%/117 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 144   |  114681|     542.456|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 144   |   60898|     481.109|   1.1%/ 63|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 144   |   57430|      42.190|   2.0%/ 35|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 144   |   47180|     710.167|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 144   |   35427|     588.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 144   |   30483|     454.455|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 144   |   28770|     610.816|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 144   |   27843|     866.525|   0.8%/ 85|   0.7%/ 95|   0.7%/ 98|   0.7%/102 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 144   |   20812|     249.615|   0.8%/ 83|   0.7%/ 95|   0.7%/ 99|   0.7%/103 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 144   |    2043|     416.569|   1.0%/ 72|   0.8%/ 84|   0.8%/ 88|   0.7%/ 92 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 144   |      30|      41.512|   1.2%/ 57|   1.1%/ 60|   1.1%/ 61|   1.1%/ 62 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 144   |    4842|     665.166|   1.1%/ 65|   0.9%/ 79|   0.8%/ 84|   0.8%/ 89 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 144   |     674|     223.498|   1.7%/ 40|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 144   |   12171|     308.042|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 144   |    1917|     332.830|   0.2%/360|   0.2%/394|   0.2%/403|   0.2%/412 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 144   |    4462|    1251.622|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 144   |     599|     614.898|   0.1%/561|   0.1%/547|   0.1%/543|   0.1%/538 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 144   |   10612|     494.100|   1.8%/ 39|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 144   |    5082|     478.660|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51|   1.4%/ 51 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 144   |      46|      32.660|   2.7%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 144   |     314|     175.764|   2.2%/ 32|   2.1%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 144   |    8071|     636.939|   0.2%/290|   0.2%/280|   0.3%/277|   0.3%/274 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 144   |    3210|     476.797|   0.4%/167|   0.4%/159|   0.4%/157|   0.4%/154 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 144   |    1032|     327.097|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81|   0.9%/ 81 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 144   |     428|     147.077|   0.8%/ 85|   0.8%/ 89|   0.8%/ 89|   0.8%/ 90 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 144   |     857|     191.878|   0.9%/ 77|   1.0%/ 70|   1.0%/ 68|   1.0%/ 66 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 144   |    4719|    1015.193|   0.8%/ 87|   0.8%/ 90|   0.8%/ 90|   0.8%/ 91 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 144   |     129|      95.957|   0.3%/265|   0.3%/269|   0.3%/270|   0.3%/269 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 144   |    3693|     610.813|   0.2%/313|   0.2%/345|   0.2%/354|   0.2%/364 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 144   |    8919|    1283.361|   0.2%/426|   0.2%/431|   0.2%/432|   0.2%/433 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 144   |    6644|     665.308|   0.2%/459|   0.2%/434|   0.2%/428|   0.2%/422 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 144   |    1798|     318.731|   0.5%/136|   0.6%/124|   0.6%/121|   0.6%/119 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 144   |    2270|     762.731|   1.3%/ 52|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 144   |    1453|     236.704|   0.7%/104|   0.7%/104|   0.7%/103|   0.7%/103 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 144   |      94|      87.914|   1.7%/ 42|   1.3%/ 54|   1.2%/ 58|   1.1%/ 62 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 144   |     377|     195.091|   0.7%/106|   0.7%/106|   0.7%/105|   0.7%/105 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 144   |    1199|     389.199|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 144   |     428|     314.739|   0.2%/417|   0.2%/414|   0.2%/411|   0.2%/407 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 144   |   15946|    1795.288|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 144   |     744|     354.951|   0.7%/106|   0.6%/112|   0.6%/113|   0.6%/114 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 144   |   32888|    1690.578|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 144   |    2529|     241.123|   1.1%/ 62|   1.1%/ 65|   1.1%/ 66|   1.0%/ 67 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 144   |     133|     175.127|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 144   |    3976|     340.162|   0.6%/113|   0.6%/117|   0.6%/118|   0.6%/119 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 144   |     721|     182.327|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48|   1.5%/ 48 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 144   |     422|     100.007|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 144   |    7547|     589.484|   0.2%/295|   0.2%/280|   0.3%/276|   0.3%/273 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 144   |     383|     120.058|   2.5%/ 27|   2.6%/ 26|   2.6%/ 26|   2.7%/ 26 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 144   |    1029|     971.179|   0.1%/602|   0.1%/552|   0.1%/540|   0.1%/528 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 144   |    2530|     491.321|   1.6%/ 44|   1.4%/ 51|   1.3%/ 53|   1.3%/ 55 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 144   |     161|     182.036|   0.8%/ 83|   0.7%/ 92|   0.7%/ 95|   0.7%/ 98 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 144   |    1535|     224.600|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 144   |   12175|     419.904|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 144   |  176854|     536.664|   0.6%/110|   0.6%/115|   0.6%/116|   0.6%/117 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 144   |     390|     121.775|   1.0%/ 68|   0.9%/ 78|   0.9%/ 81|   0.8%/ 83 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 144   |      58|      93.549|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 144   |    2465|     288.834|   0.4%/158|   0.4%/195|   0.3%/207|   0.3%/221 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 144   |    1863|     244.670|   0.8%/ 91|   0.8%/ 91|   0.8%/ 91|   0.8%/ 91 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 144   |     178|      99.325|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 144   |    1081|     185.625|   0.6%/107|   0.6%/113|   0.6%/114|   0.6%/115 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 132   |      34|      57.908|   1.5%/ 46|   1.8%/ 39|   1.9%/ 37|   1.9%/ 36 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 144   |    1399|      43.424|   0.4%/197|   0.3%/223|   0.3%/231|   0.3%/241 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 144   |     254|      89.310|   1.7%/ 41|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 144   |    1435|      33.375|   0.7%/ 97|   0.7%/103|   0.7%/105|   0.6%/107 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 144   |     104|       3.334|   2.0%/ 35|   1.5%/ 47|   1.3%/ 51|   1.2%/ 57 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 144   |    6940|     154.429|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 144   |     853|     288.540|   0.5%/127|   0.5%/150|   0.4%/157|   0.4%/165 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 144   |     548|      21.354|   3.6%/ 19|   3.3%/ 21|   3.2%/ 22|   3.1%/ 22 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 144   |     731|      82.141|   0.1%/751|   0.1%/738|   0.1%/736|   0.1%/734 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 144   |     526|      52.288|   0.4%/177|   0.1%/471|   0.1%/797|   0.0%/ *** |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 144   |     183|     118.473|   1.0%/ 69|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 144   |    3903|      23.170|   1.1%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 144   |     633|      67.332|   0.6%/115|   0.6%/117|   0.6%/117|   0.6%/117 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 144   |    9979|     865.917|   0.1%/850|   0.1%/738|   0.1%/714|   0.1%/692 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 139   |      40|       3.369|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 144   |    4542|     395.989|   1.6%/ 44|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 144   |     544|     164.725|   1.8%/ 38|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 144   |       3|       1.380|   2.2%/ 31|   1.7%/ 40|   1.6%/ 43|   1.5%/ 47 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 144   |  114681|     542.456|   1.0%/ 72|   0.9%/ 75|   0.9%/ 76|   0.9%/ 77 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 144   |     556|      79.972|   1.5%/ 47|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 144   |      55|       2.641|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 132   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 144   |     408|      15.363|   0.2%/283|   0.3%/257|   0.3%/251|   0.3%/245 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 144   |    9114|     239.848|   0.1%/998|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  92   |      61|      11.172|   0.1%/466|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 117   |      76|       4.690|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 144   |   10835|     567.044|   0.5%/127|   0.5%/142|   0.5%/146|   0.5%/151 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 144   |    4712|       3.361|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 144   |   17379|     351.825|   2.1%/ 33|   1.8%/ 38|   1.7%/ 40|   1.7%/ 42 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 144   |     379|      74.954|   3.3%/ 21|   2.7%/ 26|   2.5%/ 28|   2.3%/ 29 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 144   |     172|      42.288|   0.6%/122|   0.4%/165|   0.4%/181|   0.3%/199 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 144   |      89|       7.902|   0.1%/875|   0.1%/788|   0.1%/769|   0.1%/750 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 144   |     623|     106.939|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 144   |    1570|     151.553|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 144   |    6248|     357.700|   0.4%/157|   0.4%/158|   0.4%/157|   0.4%/157 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 144   |    5286|      52.720|   0.3%/205|   0.3%/274|   0.2%/298|   0.2%/326 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 144   |     677|     104.362|   1.5%/ 46|   1.2%/ 56|   1.2%/ 59|   1.1%/ 63 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 123   |      84|      62.210|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 140   |     673|       6.823|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 144   |     335|      60.548|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 144   |   30483|     454.455|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 144   |      53|      24.389|   0.3%/273|   0.2%/285|   0.2%/286|   0.2%/286 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 144   |     101|      43.099|  13.6%/  5|   8.7%/  8|  10.1%/  7|   2.9%/ 23 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 141   |      17|       4.588|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 144   |    9270|     111.483|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 144   |     264|       8.707|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 144   |     237|      22.107|   0.8%/ 86|   0.9%/ 74|   1.0%/ 72|   1.0%/ 69 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 144   |    2588|     155.895|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.0%/ 66 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 130   |      53|       4.357|   0.6%/116|   0.5%/127|   0.5%/129|   0.5%/130 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 119   |      34|      21.148|   0.5%/137|   0.4%/191|   0.3%/215|   0.3%/248 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 140   |     204|      17.578|   0.7%/100|   0.5%/132|   0.5%/146|   0.4%/164 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 144   |    1687|     184.189|   0.7%/ 93|   0.4%/169|   0.3%/209|   0.3%/273 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 144   |     611|      62.562|   0.1%/639|   0.1%/614|   0.1%/611|   0.1%/609 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 144   |   57430|      42.190|   2.0%/ 35|   1.9%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 144   |    6589|      24.685|   1.1%/ 63|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 144   |   20812|     249.615|   0.8%/ 83|   0.7%/ 95|   0.7%/ 99|   0.7%/103 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 144   |    6380|     163.058|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 144   |    1778|     361.246|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 144   |     763|      83.011|   1.7%/ 40|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 144   |   35427|     588.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 144   |      16|       5.739|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 144   |    1153|       9.155|   0.9%/ 77|   1.1%/ 64|   1.1%/ 62|   1.2%/ 59 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 144   |      11|       1.032|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 144   |    1545|      82.690|   1.5%/ 47|   1.8%/ 38|   1.9%/ 37|   1.9%/ 35 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 144   |     547|      11.497|   1.9%/ 36|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 144   |     467|     259.834|   2.5%/ 28|   2.1%/ 34|   1.9%/ 35|   1.8%/ 38 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 141   |     517|     117.068|   0.5%/127|   0.5%/144|   0.5%/149|   0.4%/155 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 142   |    1536|     235.053|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 142   |      33|      17.212|   0.2%/295|   0.3%/255|   0.3%/244|   0.3%/234 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 144   |     122|      17.866|   3.3%/ 21|   3.3%/ 21|   3.2%/ 21|   3.2%/ 21 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 141   |      84|      18.740|   0.3%/269|   0.1%/808|   0.0%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 143   |     193|      28.064|   3.7%/ 18|   3.6%/ 19|   3.5%/ 19|   3.5%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 144   |      82|      29.343|   0.2%/329|   0.3%/254|   0.3%/239|   0.3%/226 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  98   |     185|       7.059|   1.8%/ 39|   1.0%/ 69|   0.8%/ 86|   0.6%/113 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 144   |     125|       3.822|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 144   |     125|       6.188|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 144   |     158|      38.673|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 144   |   60898|     481.109|   1.1%/ 63|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 144   |     942|     351.410|   0.8%/ 89|   0.7%/ 97|   0.7%/ 99|   0.7%/102 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 144   |     836|      23.306|   4.2%/ 16|   4.5%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  90   |      21|       0.684|   1.6%/ 42|   1.0%/ 68|   0.9%/ 81|   0.7%/100 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  44   |      45|      18.218|   9.0%/  8|   4.5%/ 15|   4.2%/ 16|   4.0%/ 17 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  99   |     141|       4.700|   5.0%/ 14|   5.3%/ 13|   5.3%/ 13|   5.4%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 144   |    6210|     355.729|   0.1%/ ***|   0.1%/ ***|   0.1%/967|   0.1%/921 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 144   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 144   |     135|      20.874|   0.6%/123|   0.5%/142|   0.5%/148|   0.5%/154 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 144   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 144   |    1009|       4.894|   0.5%/148|   0.4%/181|   0.4%/192|   0.3%/204 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 144   |     565|     272.235|   0.6%/126|   0.4%/154|   0.4%/163|   0.4%/173 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 144   |     263|      49.014|   0.2%/390|   0.2%/306|   0.2%/290|   0.3%/276 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 144   |     638|     136.865|   1.4%/ 49|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 144   |    6255|      28.518|   0.2%/374|   0.1%/475|   0.1%/508|   0.1%/547 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 144   |    1914|     453.604|   1.1%/ 63|   0.9%/ 75|   0.9%/ 79|   0.8%/ 83 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  27   |       4|       0.448|   0.0%/ --|   6.4%/ 11|   9.1%/  7|  11.5%/  6 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 144   |     188|      26.240|   6.3%/ 11|   6.8%/ 10|   6.9%/ 10|   7.0%/ 10 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 144   |   27843|     866.525|   0.8%/ 85|   0.7%/ 95|   0.7%/ 98|   0.7%/102 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 144   |    2901|      26.733|   2.1%/ 33|   2.4%/ 29|   2.5%/ 28|   2.5%/ 27 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 144   |    1945|      50.675|   0.6%/113|   0.6%/108|   0.6%/107|   0.7%/106 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 144   |    1795|     174.629|   0.2%/415|   0.2%/414|   0.2%/414|   0.2%/414 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 144   |     198|      71.996|   0.4%/178|   0.2%/277|   0.2%/326|   0.2%/397 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 144   |    3256|     167.801|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 144   |   16344|     111.374|   0.7%/102|   0.6%/110|   0.6%/112|   0.6%/115 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  85   |      11|       0.916|   4.9%/ 14|   4.7%/ 15|   4.7%/ 15|   4.7%/ 15 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 144   |    3626|     105.958|   1.1%/ 66|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 144   |     270|      16.683|   1.1%/ 65|   0.9%/ 75|   0.9%/ 78|   0.9%/ 81 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 144   |     711|     102.070|   0.7%/ 99|   0.5%/137|   0.5%/152|   0.4%/170 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 122   |      70|       8.796|   0.1%/702|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 144   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 144   |      33|       6.061|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 144   |     132|      63.158|   0.2%/284|   0.1%/499|   0.1%/625|   0.1%/840 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 137   |      93|       5.852|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 144   |   13590|     231.226|   1.9%/ 36|   1.5%/ 45|   1.5%/ 48|   1.4%/ 51 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 144   |   28770|     610.816|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 144   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 144   |     821|      19.346|   0.4%/181|   0.3%/212|   0.3%/221|   0.3%/232 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 144   |    5810|     561.986|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 144   |    1998|     232.219|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 144   |      80|       4.545|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 144   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 144   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 144   |      29|       3.905|   1.3%/ 55|   0.7%/ 95|   0.6%/117|   0.4%/156 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 144   |       8|       5.865|  11.2%/  6|   0.0%/ --|   0.0%/ --|   2.7%/ 25 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 144   |      54|       4.621|   1.0%/ 70|   1.3%/ 55|   1.3%/ 52|   1.4%/ 49 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 144   |    6089|      73.224|   0.3%/212|   0.3%/204|   0.3%/202|   0.3%/200 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 144   |  176854|     536.664|   0.6%/110|   0.6%/115|   0.6%/116|   0.6%/117 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  30   |      20|       0.506|   8.3%/  8|   7.6%/  9|   7.9%/  9|   8.2%/  8 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 144   |    2272|      54.249|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 144   |     369|      37.357|   0.3%/216|   0.4%/195|   0.4%/190|   0.4%/185 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 144   |   47180|     710.167|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 144   |      41|      11.598|   1.0%/ 70|   1.2%/ 59|   1.2%/ 56|   1.3%/ 54 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 144   |     276|       8.076|   2.6%/ 27|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 144   |     336|      10.419|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  23   |      25|       0.260|   6.1%/ 11|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 143   |     303|      16.928|   1.1%/ 60|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 144   |     178|      11.740|   3.4%/ 20|   2.0%/ 34|   1.7%/ 41|   1.4%/ 51 |

