# State and Country COVID-19 Analysis #
## Updated: at 2020-08-27 for data as of 2020-08-26 ##

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.3% of deaths and 58.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 148   |   32917|    1692.102|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 148   |   15957|    1796.469|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 148   |   12657|     320.341|   1.1%/ 64|   1.0%/ 69|   1.0%/ 71|   1.0%/ 73 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 148   |   12814|     441.909|   1.6%/ 42|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 148   |   11119|     517.689|   1.5%/ 48|   1.2%/ 57|   1.1%/ 61|   1.1%/ 64 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 148   |    8977|    1291.713|   0.2%/415|   0.2%/412|   0.2%/411|   0.2%/410 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 148   |    8146|     642.845|   0.2%/303|   0.2%/299|   0.2%/298|   0.2%/297 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 148   |    7610|     594.458|   0.2%/327|   0.2%/329|   0.2%/331|   0.2%/332 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 148   |    6686|     669.502|   0.2%/462|   0.2%/446|   0.2%/442|   0.2%/439 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 148   |    5350|     503.900|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 148   |  180490|     547.695|   0.6%/124|   0.5%/134|   0.5%/137|   0.5%/140 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 148   |  118364|     559.873|   0.9%/ 80|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 148   |   62916|     497.052|   0.9%/ 73|   0.8%/ 83|   0.8%/ 85|   0.8%/ 89 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 148   |   61399|      45.106|   1.8%/ 38|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 148   |   40997|     617.096|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 148   |   35481|     589.014|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 148   |   30544|     455.357|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 148   |   28898|     613.530|   0.1%/913|   0.1%/780|   0.1%/753|   0.1%/728 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 148   |   29159|     907.484|   0.8%/ 91|   0.7%/102|   0.7%/105|   0.6%/109 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 148   |   21314|     255.631|   0.7%/ 94|   0.6%/109|   0.6%/114|   0.6%/119 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 148   |    2091|     426.442|   0.8%/ 90|   0.6%/114|   0.6%/123|   0.5%/133 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 148   |      32|      44.109|   1.2%/ 59|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 148   |    4966|     682.234|   0.9%/ 81|   0.7%/104|   0.6%/112|   0.6%/121 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 148   |     723|     239.557|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 148   |   12657|     320.341|   1.1%/ 64|   1.0%/ 69|   1.0%/ 71|   1.0%/ 73 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 148   |    1930|     335.125|   0.2%/372|   0.2%/396|   0.2%/403|   0.2%/409 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 148   |    4466|    1252.498|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 148   |     602|     618.609|   0.2%/433|   0.2%/389|   0.2%/378|   0.2%/367 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 148   |   11119|     517.689|   1.5%/ 48|   1.2%/ 57|   1.1%/ 61|   1.1%/ 64 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 148   |    5350|     503.900|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 148   |      51|      36.157|   2.3%/ 30|   2.5%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 148   |     336|     187.944|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 148   |    8146|     642.845|   0.2%/303|   0.2%/299|   0.2%/298|   0.2%/297 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 148   |    3259|     484.052|   0.4%/184|   0.4%/183|   0.4%/183|   0.4%/184 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 148   |    1066|     337.937|   0.8%/ 84|   0.8%/ 83|   0.8%/ 83|   0.8%/ 82 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 148   |     439|     150.821|   0.7%/ 96|   0.7%/104|   0.7%/106|   0.6%/108 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 148   |     893|     199.940|   0.9%/ 75|   1.0%/ 69|   1.0%/ 67|   1.0%/ 66 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 148   |    4859|    1045.217|   0.8%/ 91|   0.7%/ 95|   0.7%/ 96|   0.7%/ 96 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 148   |     131|      97.456|   0.3%/212|   0.4%/195|   0.4%/191|   0.4%/186 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 148   |    3720|     615.358|   0.2%/332|   0.2%/363|   0.2%/371|   0.2%/380 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 148   |    8977|    1291.713|   0.2%/415|   0.2%/412|   0.2%/411|   0.2%/410 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 148   |    6686|     669.502|   0.2%/462|   0.2%/446|   0.2%/442|   0.2%/439 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 148   |    1834|     325.251|   0.5%/147|   0.5%/141|   0.5%/140|   0.5%/139 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 148   |    2367|     795.180|   1.2%/ 58|   1.1%/ 64|   1.1%/ 65|   1.0%/ 67 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 148   |    1485|     241.931|   0.6%/121|   0.5%/127|   0.5%/128|   0.5%/130 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 148   |      98|      92.121|   1.6%/ 44|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 148   |     387|     199.908|   0.6%/110|   0.6%/111|   0.6%/111|   0.6%/111 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 148   |    1268|     411.546|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 148   |     430|     316.337|   0.1%/540|   0.1%/578|   0.1%/588|   0.1%/598 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 148   |   15957|    1796.469|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 148   |     760|     362.533|   0.6%/120|   0.5%/130|   0.5%/132|   0.5%/135 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 148   |   32917|    1692.102|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 148   |    2620|     249.827|   1.0%/ 71|   0.9%/ 78|   0.9%/ 79|   0.8%/ 81 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 148   |     140|     183.950|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 148   |    4052|     346.649|   0.5%/133|   0.5%/145|   0.5%/148|   0.5%/152 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 148   |     758|     191.598|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 148   |     437|     103.659|   1.0%/ 66|   0.9%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 148   |    7610|     594.458|   0.2%/327|   0.2%/329|   0.2%/331|   0.2%/332 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 148   |     418|     130.740|   2.1%/ 32|   2.0%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 148   |    1036|     977.811|   0.2%/443|   0.2%/381|   0.2%/368|   0.2%/355 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 148   |    2638|     512.455|   1.3%/ 53|   1.1%/ 65|   1.0%/ 68|   1.0%/ 72 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 148   |     165|     186.096|   0.7%/106|   0.5%/130|   0.5%/138|   0.5%/146 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 148   |    1649|     241.256|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 148   |   12814|     441.909|   1.6%/ 42|   1.4%/ 50|   1.3%/ 52|   1.3%/ 54 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 148   |  180490|     547.695|   0.6%/124|   0.5%/134|   0.5%/137|   0.5%/140 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 148   |     403|     125.583|   0.9%/ 74|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 148   |      58|      93.366|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 148   |    2506|     293.563|   0.5%/150|   0.4%/164|   0.4%/167|   0.4%/170 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 148   |    1907|     250.367|   0.6%/112|   0.6%/124|   0.5%/128|   0.5%/132 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 148   |     191|     106.512|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 148   |    1103|     189.441|   0.6%/122|   0.5%/132|   0.5%/135|   0.5%/137 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 136   |      37|      64.586|   0.9%/ 80|   0.8%/ 85|   0.8%/ 87|   0.8%/ 88 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 148   |    1411|      43.801|   0.3%/236|   0.2%/288|   0.2%/306|   0.2%/328 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 148   |     268|      94.077|   1.7%/ 42|   1.4%/ 48|   1.4%/ 49|   1.3%/ 51 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 148   |    1471|      34.221|   0.7%/101|   0.6%/107|   0.6%/108|   0.6%/110 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 148   |     109|       3.488|   1.5%/ 45|   1.0%/ 67|   0.9%/ 76|   0.8%/ 88 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 148   |    7809|     173.768|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 148   |     868|     293.363|   0.5%/141|   0.4%/165|   0.4%/172|   0.4%/179 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 148   |     653|      25.408|   3.4%/ 21|   3.0%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 148   |     734|      82.442|   0.1%/756|   0.1%/760|   0.1%/762|   0.1%/764 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 148   |     529|      52.559|   0.3%/205|   0.2%/392|   0.1%/501|   0.1%/688 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 148   |     189|     122.428|   0.9%/ 80|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 148   |    4071|      24.163|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 148   |     652|      69.256|   0.7%/103|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 148   |   10011|     868.664|   0.1%/921|   0.1%/861|   0.1%/850|   0.1%/840 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 143   |      40|       3.379|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 148   |    4782|     416.909|   1.5%/ 46|   1.3%/ 51|   1.3%/ 53|   1.3%/ 54 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 148   |     579|     175.519|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 148   |       3|       1.421|   1.5%/ 47|   0.9%/ 75|   0.8%/ 90|   0.6%/112 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 148   |  118364|     559.873|   0.9%/ 80|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 148   |     585|      84.158|   1.5%/ 47|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 148   |      55|       2.649|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 136   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 148   |     411|      15.487|   0.2%/341|   0.2%/341|   0.2%/342|   0.2%/344 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 148   |    9140|     240.533|   0.1%/968|   0.1%/957|   0.1%/953|   0.1%/949 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  96   |      61|      11.129|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 121   |      76|       4.704|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 148   |   11044|     578.010|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/148 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 148   |    4721|       3.366|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 148   |   18599|     376.531|   2.0%/ 34|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 148   |     410|      80.982|   2.8%/ 25|   2.3%/ 30|   2.2%/ 31|   2.1%/ 33 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 148   |     176|      43.138|   0.6%/113|   0.6%/126|   0.5%/129|   0.5%/132 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 148   |      89|       7.929|   0.3%/272|   0.3%/212|   0.3%/200|   0.4%/188 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 148   |     624|     107.087|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 148   |    1637|     158.059|   1.2%/ 59|   1.1%/ 65|   1.0%/ 67|   1.0%/ 69 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 148   |    6373|     364.812|   0.5%/148|   0.5%/144|   0.5%/142|   0.5%/141 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 148   |    5339|      53.242|   0.3%/217|   0.3%/262|   0.3%/275|   0.2%/289 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 148   |     704|     108.603|   1.3%/ 53|   1.1%/ 65|   1.0%/ 69|   1.0%/ 73 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 127   |      83|      61.216|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 144   |     759|       7.693|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 148   |     335|      60.666|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 148   |   30544|     455.357|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 148   |      53|      24.575|   0.2%/421|   0.1%/522|   0.1%/555|   0.1%/593 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 148   |     119|      50.745|   8.7%/  8|   1.2%/ 59|   2.3%/ 30|   2.2%/ 31 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 145   |      17|       4.680|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 148   |    9290|     111.721|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 148   |     277|       9.160|   1.4%/ 49|   1.3%/ 54|   1.2%/ 55|   1.2%/ 57 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 148   |     246|      22.923|   0.8%/ 86|   0.9%/ 78|   0.9%/ 77|   0.9%/ 75 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 148   |    2692|     162.108|   1.1%/ 63|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 134   |      55|       4.528|   0.9%/ 74|   1.1%/ 63|   1.1%/ 60|   1.2%/ 58 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 123   |      35|      21.541|   0.4%/185|   0.2%/329|   0.2%/414|   0.1%/560 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 144   |     204|      17.627|   0.4%/177|   0.1%/544|   0.1%/ ***|   0.0%/ -- |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 148   |    1726|     188.510|   0.8%/ 83|   0.7%/ 98|   0.7%/102|   0.7%/106 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 148   |     614|      62.869|   0.1%/604|   0.1%/596|   0.1%/595|   0.1%/594 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 148   |   61399|      45.106|   1.8%/ 38|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 148   |    6904|      25.868|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 148   |   21314|     255.631|   0.7%/ 94|   0.6%/109|   0.6%/114|   0.6%/119 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 148   |    6698|     171.194|   1.3%/ 54|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 148   |    1779|     361.462|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 148   |     876|      95.329|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 148   |   35481|     589.014|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 148   |      16|       6.046|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 148   |    1210|       9.608|   1.0%/ 71|   1.1%/ 62|   1.2%/ 60|   1.2%/ 58 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 148   |      11|       1.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 148   |    1600|      85.637|   1.4%/ 48|   1.6%/ 42|   1.7%/ 41|   1.7%/ 40 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 148   |     579|      12.173|   1.7%/ 42|   1.5%/ 47|   1.4%/ 49|   1.4%/ 51 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 148   |     506|     281.938|   2.4%/ 28|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 145   |     526|     118.940|   0.5%/145|   0.4%/168|   0.4%/175|   0.4%/183 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 146   |    1135|     173.647|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 146   |      33|      17.350|   0.2%/456|   0.2%/439|   0.2%/435|   0.2%/431 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 148   |     139|      20.327|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 145   |      84|      18.668|   0.1%/636|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 147   |     217|      31.531|   3.5%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 148   |      84|      30.011|   0.4%/188|   0.5%/146|   0.5%/138|   0.5%/131 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 102   |     186|       7.077|   1.0%/ 68|   0.3%/239|   0.1%/637|   0.0%/ -- |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 148   |     125|       3.819|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 148   |     125|       6.192|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 148   |     158|      38.747|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 148   |   62916|     497.052|   0.9%/ 73|   0.8%/ 83|   0.8%/ 85|   0.8%/ 89 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 148   |     969|     361.165|   0.8%/ 91|   0.7%/ 97|   0.7%/ 99|   0.7%/100 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 148   |     989|      27.575|   4.3%/ 16|   4.5%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  94   |      21|       0.705|   1.3%/ 52|   1.0%/ 68|   1.0%/ 72|   0.9%/ 76 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  48   |      61|      24.705|   4.7%/ 15|   6.8%/ 10|   7.2%/  9|   7.5%/  9 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 103   |     172|       5.747|   5.0%/ 14|   5.1%/ 13|   5.1%/ 13|   5.2%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 148   |    6229|     356.831|   0.1%/ ***|   0.1%/985|   0.1%/947|   0.1%/911 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 148   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 148   |     137|      21.220|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 148   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 148   |    1020|       4.950|   0.4%/180|   0.3%/230|   0.3%/248|   0.3%/268 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 148   |     577|     277.678|   0.6%/122|   0.5%/133|   0.5%/135|   0.5%/138 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 148   |     265|      49.359|   0.1%/586|   0.1%/528|   0.1%/517|   0.1%/507 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 148   |     664|     142.450|   1.4%/ 51|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 148   |    6287|      28.662|   0.2%/427|   0.1%/532|   0.1%/567|   0.1%/606 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 148   |    1972|     467.435|   0.9%/ 73|   0.8%/ 89|   0.7%/ 94|   0.7%/ 99 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  31   |       4|       0.448|   6.5%/ 11|   1.7%/ 40|   0.1%/942|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 148   |     249|      34.782|   6.1%/ 11|   6.4%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 148   |   29159|     907.484|   0.8%/ 91|   0.7%/102|   0.7%/105|   0.6%/109 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 148   |    3137|      28.911|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 148   |    1991|      51.865|   0.6%/119|   0.6%/119|   0.6%/119|   0.6%/119 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 148   |    1807|     175.833|   0.2%/400|   0.2%/394|   0.2%/393|   0.2%/392 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 148   |     198|      72.140|   0.2%/277|   0.1%/718|   0.1%/ ***|   0.0%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 148   |    3434|     176.978|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 148   |   16718|     113.926|   0.6%/110|   0.6%/120|   0.6%/123|   0.6%/125 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  89   |      15|       1.183|   5.6%/ 12|   6.9%/ 10|   7.3%/  9|   7.6%/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 148   |    3772|     110.236|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 148   |     280|      17.266|   1.0%/ 69|   0.9%/ 78|   0.9%/ 81|   0.8%/ 84 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 148   |     721|     103.493|   0.6%/124|   0.4%/178|   0.3%/200|   0.3%/227 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 126   |      69|       8.779|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 148   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 148   |      33|       6.130|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 148   |     133|      63.739|   0.3%/206|   0.3%/241|   0.3%/250|   0.3%/260 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 141   |      94|       5.883|   0.1%/654|   0.2%/444|   0.2%/409|   0.2%/378 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 148   |   14170|     241.082|   1.5%/ 47|   1.1%/ 63|   1.0%/ 69|   0.9%/ 77 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 148   |   28898|     613.530|   0.1%/913|   0.1%/780|   0.1%/753|   0.1%/728 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 148   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 148   |     828|      19.507|   0.3%/236|   0.2%/311|   0.2%/338|   0.2%/369 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 148   |    5820|     562.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 148   |    2002|     232.735|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 148   |      96|       5.459|   3.0%/ 23|   3.2%/ 22|   3.2%/ 21|   3.3%/ 21 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 148   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 148   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 148   |      29|       3.902|   0.4%/162|   0.1%/627|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 148   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 148   |      55|       4.727|   1.3%/ 54|   1.6%/ 44|   1.7%/ 42|   1.7%/ 40 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 148   |    6174|      74.252|   0.3%/207|   0.3%/200|   0.3%/199|   0.4%/197 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 148   |  180490|     547.695|   0.6%/124|   0.5%/134|   0.5%/137|   0.5%/140 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  34   |      26|       0.644|   7.6%/  9|   6.4%/ 11|   7.2%/  9|   8.4%/  8 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 148   |    2397|      57.229|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 148   |     376|      38.025|   0.4%/184|   0.4%/164|   0.4%/159|   0.4%/155 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 148   |   40997|     617.096|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 148   |      43|      12.119|   0.9%/ 75|   1.0%/ 67|   1.1%/ 65|   1.1%/ 63 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 148   |     299|       8.768|   2.4%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 148   |     367|      11.403|   2.6%/ 27|   2.3%/ 30|   2.2%/ 31|   2.2%/ 32 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  27   |      29|       0.304|   0.5%/151|   2.2%/ 31|   2.6%/ 27|   2.9%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 147   |     310|      17.308|   0.7%/ 92|   0.6%/115|   0.6%/123|   0.5%/133 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 148   |     187|      12.307|   3.8%/ 18|   0.7%/106|   2.8%/ 25|   4.9%/ 14 |

