# State and Country COVID-19 Analysis #
## Updated: at 2020-08-24 for data as of 2020-08-23 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 145   |   32894|    1690.882|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 145   |   15951|    1795.789|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 145   |   12295|     311.171|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 145   |   12344|     425.718|   1.9%/ 37|   1.7%/ 41|   1.6%/ 43|   1.6%/ 44 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 145   |   10757|     500.829|   1.7%/ 41|   1.5%/ 47|   1.4%/ 49|   1.4%/ 51 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 145   |    8931|    1285.166|   0.2%/436|   0.2%/445|   0.2%/448|   0.2%/450 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 145   |    8089|     638.383|   0.2%/294|   0.2%/287|   0.2%/285|   0.2%/283 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 145   |    7563|     590.790|   0.2%/302|   0.2%/290|   0.2%/288|   0.2%/285 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 145   |    6655|     666.366|   0.1%/465|   0.2%/444|   0.2%/439|   0.2%/434 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 145   |    5152|     485.195|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 145   |  177790|     539.501|   0.6%/113|   0.6%/119|   0.6%/121|   0.6%/122 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 145   |  115608|     546.836|   0.9%/ 74|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 145   |   61418|     485.221|   1.1%/ 65|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 145   |   58429|      42.924|   1.9%/ 36|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 145   |   47212|     710.640|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 145   |   35443|     588.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 145   |   30498|     454.685|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 145   |   28799|     611.442|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 145   |   28209|     877.929|   0.8%/ 86|   0.7%/ 96|   0.7%/ 99|   0.7%/103 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 145   |   20940|     251.143|   0.8%/ 86|   0.7%/ 99|   0.7%/103|   0.6%/108 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 145   |    2055|     419.142|   0.9%/ 75|   0.8%/ 89|   0.7%/ 93|   0.7%/ 98 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 145   |      31|      42.208|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 145   |    4874|     669.603|   1.0%/ 69|   0.8%/ 85|   0.8%/ 90|   0.7%/ 96 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 145   |     686|     227.294|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 145   |   12295|     311.171|   1.2%/ 58|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 145   |    1920|     333.404|   0.2%/349|   0.2%/369|   0.2%/374|   0.2%/379 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 145   |    4463|    1251.832|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 145   |     599|     615.403|   0.1%/497|   0.1%/462|   0.2%/452|   0.2%/443 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 145   |   10757|     500.829|   1.7%/ 41|   1.5%/ 47|   1.4%/ 49|   1.4%/ 51 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 145   |    5152|     485.195|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 145   |      47|      33.509|   2.5%/ 28|   2.8%/ 24|   2.9%/ 24|   3.0%/ 23 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 145   |     319|     178.288|   2.1%/ 33|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 145   |    8089|     638.383|   0.2%/294|   0.2%/287|   0.2%/285|   0.2%/283 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 145   |    3222|     478.667|   0.4%/171|   0.4%/164|   0.4%/162|   0.4%/160 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 145   |    1040|     329.591|   0.8%/ 85|   0.8%/ 84|   0.8%/ 84|   0.8%/ 83 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 145   |     431|     147.906|   0.8%/ 88|   0.7%/ 93|   0.7%/ 95|   0.7%/ 96 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 145   |     866|     193.746|   0.9%/ 78|   1.0%/ 72|   1.0%/ 70|   1.0%/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 145   |    4756|    1022.957|   0.8%/ 88|   0.8%/ 90|   0.8%/ 91|   0.8%/ 91 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 145   |     130|      96.351|   0.3%/224|   0.3%/210|   0.3%/206|   0.3%/201 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 145   |    3700|     611.932|   0.2%/319|   0.2%/353|   0.2%/362|   0.2%/373 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 145   |    8931|    1285.166|   0.2%/436|   0.2%/445|   0.2%/448|   0.2%/450 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 145   |    6655|     666.366|   0.1%/465|   0.2%/444|   0.2%/439|   0.2%/434 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 145   |    1807|     320.425|   0.5%/138|   0.5%/128|   0.6%/126|   0.6%/124 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 145   |    2292|     769.971|   1.3%/ 55|   1.1%/ 61|   1.1%/ 63|   1.1%/ 65 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 145   |    1461|     238.027|   0.6%/110|   0.6%/112|   0.6%/113|   0.6%/113 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 145   |      95|      88.576|   1.5%/ 47|   1.1%/ 64|   1.0%/ 70|   0.9%/ 78 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 145   |     380|     196.220|   0.6%/110|   0.6%/111|   0.6%/111|   0.6%/111 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 145   |    1217|     395.022|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 145   |     429|     315.217|   0.2%/433|   0.2%/430|   0.2%/427|   0.2%/423 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 145   |   15951|    1795.789|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 145   |     748|     356.887|   0.6%/109|   0.6%/115|   0.6%/116|   0.6%/118 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 145   |   32894|    1690.882|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 145   |    2552|     243.360|   1.1%/ 63|   1.0%/ 67|   1.0%/ 68|   1.0%/ 69 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 145   |     135|     177.614|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 145   |    3996|     341.851|   0.6%/117|   0.6%/122|   0.6%/123|   0.6%/125 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 145   |     730|     184.548|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 145   |     425|     100.879|   1.1%/ 61|   1.0%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 145   |    7563|     590.790|   0.2%/302|   0.2%/290|   0.2%/288|   0.2%/285 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 145   |     393|     123.051|   2.5%/ 28|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 145   |    1030|     972.225|   0.1%/619|   0.1%/575|   0.1%/565|   0.1%/554 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 145   |    2558|     496.909|   1.5%/ 45|   1.4%/ 51|   1.3%/ 53|   1.3%/ 55 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 145   |     162|     183.267|   0.8%/ 84|   0.7%/ 93|   0.7%/ 96|   0.7%/ 98 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 145   |    1563|     228.718|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 145   |   12344|     425.718|   1.9%/ 37|   1.7%/ 41|   1.6%/ 43|   1.6%/ 44 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 145   |  177790|     539.501|   0.6%/113|   0.6%/119|   0.6%/121|   0.6%/122 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 145   |     393|     122.543|   0.9%/ 74|   0.8%/ 87|   0.8%/ 90|   0.7%/ 95 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 145   |      58|      93.503|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 145   |    2474|     289.884|   0.4%/159|   0.4%/192|   0.3%/202|   0.3%/213 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 145   |    1875|     246.261|   0.7%/ 95|   0.7%/ 96|   0.7%/ 97|   0.7%/ 97 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 145   |     181|     101.108|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 145   |    1086|     186.580|   0.6%/111|   0.6%/119|   0.6%/121|   0.6%/122 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 133   |      35|      60.444|   1.8%/ 39|   2.2%/ 32|   2.3%/ 30|   2.4%/ 29 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 145   |    1402|      43.515|   0.3%/214|   0.3%/254|   0.3%/268|   0.2%/284 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 145   |     257|      90.369|   1.7%/ 41|   1.4%/ 50|   1.3%/ 53|   1.2%/ 56 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 145   |    1444|      33.581|   0.7%/ 99|   0.6%/107|   0.6%/109|   0.6%/111 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 145   |     105|       3.364|   1.8%/ 38|   1.3%/ 52|   1.2%/ 57|   1.1%/ 64 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 145   |    7128|     158.610|   3.0%/ 23|   2.9%/ 24|   2.9%/ 24|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 145   |     857|     289.793|   0.5%/127|   0.5%/145|   0.5%/151|   0.4%/156 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 145   |     573|      22.305|   3.5%/ 19|   3.2%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 145   |     732|      82.222|   0.1%/716|   0.1%/693|   0.1%/688|   0.1%/683 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 145   |     527|      52.327|   0.4%/182|   0.2%/425|   0.1%/630|   0.1%/ *** |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 145   |     185|     119.571|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72|   1.0%/ 72 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 145   |    3943|      23.407|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 145   |     638|      67.778|   0.6%/111|   0.6%/110|   0.6%/110|   0.6%/109 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 145   |    9988|     866.696|   0.1%/864|   0.1%/763|   0.1%/741|   0.1%/721 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 140   |      40|       3.372|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 145   |    4597|     400.768|   1.6%/ 44|   1.3%/ 52|   1.3%/ 55|   1.2%/ 57 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 145   |     552|     167.305|   1.7%/ 40|   1.6%/ 44|   1.6%/ 45|   1.5%/ 45 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 145   |       3|       1.393|   2.0%/ 35|   1.5%/ 46|   1.4%/ 50|   1.3%/ 55 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 145   |  115608|     546.836|   0.9%/ 74|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 145   |     562|      80.818|   1.4%/ 50|   1.2%/ 58|   1.1%/ 61|   1.1%/ 63 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 145   |      55|       2.644|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 133   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 145   |     409|      15.396|   0.2%/305|   0.2%/285|   0.2%/281|   0.3%/277 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 145   |    9120|     240.007|   0.1%/983|   0.1%/980|   0.1%/979|   0.1%/977 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  93   |      61|      11.159|   0.1%/554|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 118   |      76|       4.688|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 145   |   10886|     569.757|   0.5%/128|   0.5%/141|   0.5%/144|   0.5%/148 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 145   |    4715|       3.362|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 145   |   17668|     357.688|   2.1%/ 33|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 145   |     386|      76.297|   3.1%/ 22|   2.5%/ 27|   2.4%/ 29|   2.2%/ 31 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 145   |     173|      42.442|   0.6%/124|   0.4%/162|   0.4%/175|   0.4%/189 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 145   |      89|       7.907|   0.1%/855|   0.1%/779|   0.1%/760|   0.1%/739 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 145   |     623|     106.967|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 145   |    1588|     153.305|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 145   |    6279|     359.434|   0.5%/151|   0.5%/149|   0.5%/148|   0.5%/147 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 145   |    5298|      52.835|   0.3%/210|   0.3%/273|   0.2%/294|   0.2%/319 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 145   |     684|     105.387|   1.4%/ 48|   1.2%/ 59|   1.1%/ 63|   1.0%/ 67 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 124   |      84|      62.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 141   |     695|       7.047|   3.7%/ 19|   3.6%/ 19|   3.5%/ 19|   3.5%/ 20 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 145   |     335|      60.566|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 145   |   30498|     454.685|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 145   |      53|      24.446|   0.2%/314|   0.2%/342|   0.2%/347|   0.2%/352 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 145   |      87|      37.057|   8.0%/  8|  10.1%/  7|   2.9%/ 23|   2.4%/ 29 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 142   |      17|       4.582|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 145   |    9275|     111.550|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 145   |     267|       8.823|   1.7%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 145   |     240|      22.335|   0.8%/ 83|   1.0%/ 72|   1.0%/ 70|   1.0%/ 68 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 145   |    2615|     157.484|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.1%/ 66 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 131   |      53|       4.373|   0.5%/130|   0.5%/151|   0.4%/156|   0.4%/161 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 120   |      34|      21.256|   0.4%/166|   0.2%/290|   0.2%/365|   0.1%/499 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 141   |     204|      17.611|   0.6%/114|   0.4%/175|   0.3%/205|   0.3%/250 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 145   |    1691|     184.601|   0.7%/ 96|   0.4%/163|   0.4%/195|   0.3%/240 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 145   |     612|      62.651|   0.1%/587|   0.1%/555|   0.1%/550|   0.1%/545 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 145   |   58429|      42.924|   1.9%/ 36|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 145   |    6663|      24.962|   1.1%/ 62|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 145   |   20940|     251.143|   0.8%/ 86|   0.7%/ 99|   0.7%/103|   0.6%/108 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 145   |    6457|     165.019|   1.3%/ 53|   1.2%/ 56|   1.2%/ 56|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 145   |    1778|     361.322|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 145   |     776|      84.462|   1.7%/ 41|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 145   |   35443|     588.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 145   |      16|       5.822|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 145   |    1168|       9.271|   0.9%/ 76|   1.1%/ 64|   1.1%/ 62|   1.2%/ 59 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 145   |      11|       1.032|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 145   |    1556|      83.264|   1.3%/ 53|   1.5%/ 46|   1.6%/ 44|   1.6%/ 43 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 145   |     555|      11.673|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 145   |     477|     265.451|   2.8%/ 25|   2.5%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 142   |     520|     117.542|   0.5%/132|   0.5%/151|   0.4%/157|   0.4%/163 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 143   |    1540|     235.761|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 143   |      33|      17.255|   0.2%/326|   0.2%/291|   0.2%/282|   0.3%/272 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 145   |     126|      18.402|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22|   3.1%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 142   |      84|      18.724|   0.2%/325|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 144   |     199|      28.904|   3.6%/ 19|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 145   |      82|      29.491|   0.3%/247|   0.4%/187|   0.4%/176|   0.4%/165 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  99   |     186|       7.068|   1.6%/ 44|   0.8%/ 90|   0.6%/122|   0.4%/189 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 145   |     125|       3.821|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 145   |     125|       6.187|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 145   |     158|      38.694|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 145   |   61418|     485.221|   1.1%/ 65|   1.0%/ 71|   0.9%/ 73|   0.9%/ 75 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 145   |     948|     353.646|   0.8%/ 91|   0.7%/ 99|   0.7%/102|   0.7%/104 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 145   |     874|      24.366|   4.2%/ 16|   4.5%/ 15|   4.6%/ 15|   4.7%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  91   |      21|       0.685|   1.4%/ 48|   0.8%/ 92|   0.6%/120|   0.4%/172 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  45   |      49|      19.947|   7.4%/  9|   5.4%/ 13|   5.8%/ 12|   6.4%/ 11 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 100   |     148|       4.938|   5.1%/ 13|   5.4%/ 13|   5.4%/ 13|   5.5%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 145   |    6215|     356.006|   0.1%/ ***|   0.1%/ ***|   0.1%/960|   0.1%/917 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 145   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 145   |     135|      20.931|   0.5%/139|   0.4%/171|   0.4%/182|   0.4%/194 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 145   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 145   |    1012|       4.909|   0.4%/155|   0.4%/190|   0.3%/202|   0.3%/216 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 145   |     568|     273.344|   0.5%/127|   0.5%/151|   0.4%/159|   0.4%/167 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 145   |     264|      49.130|   0.2%/436|   0.2%/352|   0.2%/335|   0.2%/320 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 145   |     643|     137.936|   1.3%/ 54|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 145   |    6264|      28.557|   0.2%/378|   0.1%/469|   0.1%/498|   0.1%/531 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 145   |    1928|     457.099|   1.1%/ 65|   0.9%/ 78|   0.8%/ 82|   0.8%/ 86 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  28   |       4|       0.448|   0.0%/ --|   8.1%/  8|   6.1%/ 11|   3.6%/ 19 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 145   |     202|      28.284|   6.3%/ 11|   6.7%/ 10|   6.8%/ 10|   6.9%/ 10 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 145   |   28209|     877.929|   0.8%/ 86|   0.7%/ 96|   0.7%/ 99|   0.7%/103 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 145   |    2968|      27.352|   2.1%/ 34|   2.3%/ 30|   2.4%/ 29|   2.4%/ 29 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 145   |    1956|      50.975|   0.6%/114|   0.6%/111|   0.6%/110|   0.6%/109 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 145   |    1797|     174.904|   0.2%/418|   0.2%/418|   0.2%/419|   0.2%/419 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 145   |     198|      72.034|   0.3%/205|   0.2%/378|   0.1%/487|   0.1%/688 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 145   |    3300|     170.077|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50|   1.4%/ 50 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 145   |   16437|     112.014|   0.7%/104|   0.6%/112|   0.6%/115|   0.6%/117 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  86   |      12|       0.960|   0.0%/ --|   3.2%/ 21|   3.2%/ 21|   2.9%/ 23 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 145   |    3662|     107.019|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 68 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 145   |     273|      16.830|   1.0%/ 66|   0.9%/ 76|   0.9%/ 78|   0.8%/ 82 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 145   |     713|     102.413|   0.7%/106|   0.5%/149|   0.4%/165|   0.4%/186 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 123   |      69|       8.792|   0.1%/831|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 145   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 145   |      33|       6.077|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 145   |     132|      63.199|   0.3%/267|   0.2%/426|   0.1%/503|   0.1%/614 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 138   |      93|       5.852|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 145   |   13744|     233.834|   1.8%/ 38|   1.4%/ 48|   1.3%/ 52|   1.2%/ 55 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 145   |   28799|     611.442|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 145   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 145   |     823|      19.388|   0.4%/196|   0.3%/240|   0.3%/254|   0.3%/270 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 145   |    5812|     562.221|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 145   |    1999|     232.364|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 145   |      84|       4.772|   2.6%/ 26|   2.7%/ 26|   2.7%/ 26|   2.7%/ 25 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 145   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 145   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 145   |      30|       3.917|   1.1%/ 64|   0.5%/134|   0.4%/191|   0.2%/335 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 145   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 145   |      54|       4.648|   1.1%/ 64|   1.4%/ 50|   1.5%/ 47|   1.5%/ 45 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 145   |    6110|      73.480|   0.3%/210|   0.3%/202|   0.3%/199|   0.4%/197 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 145   |  177790|     539.501|   0.6%/113|   0.6%/119|   0.6%/121|   0.6%/122 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  31   |      21|       0.510|   6.9%/ 10|   6.8%/ 10|   5.6%/ 12|   4.3%/ 16 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 145   |    2304|      55.011|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 145   |     371|      37.525|   0.3%/201|   0.4%/178|   0.4%/173|   0.4%/168 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 145   |   47212|     710.640|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 145   |      41|      11.736|   1.0%/ 70|   1.2%/ 59|   1.2%/ 57|   1.3%/ 55 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 145   |     281|       8.243|   2.6%/ 27|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 145   |     344|      10.673|   2.8%/ 24|   2.6%/ 26|   2.6%/ 27|   2.5%/ 27 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  24   |      27|       0.278|   4.4%/ 16|   0.0%/ --|   1.1%/ 64|   2.5%/ 27 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 144   |     306|      17.112|   1.1%/ 62|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 145   |     179|      11.839|   1.8%/ 39|   2.5%/ 27|   0.7%/105|   0.9%/ 79 |

