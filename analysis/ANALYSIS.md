# State and Country COVID-19 Analysis #
## Updated: at 2020-08-17 for data as of 2020-08-16 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.6% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 138   |   32848|    1688.529|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 138   |   15917|    1792.029|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 138   |   11382|     288.051|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 138   |   10998|     379.281|   2.2%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 138   |    9610|     447.433|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 138   |    8836|    1271.445|   0.2%/401|   0.2%/398|   0.2%/397|   0.2%/396 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 138   |    7958|     628.040|   0.2%/316|   0.2%/315|   0.2%/315|   0.2%/315 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 138   |    7438|     581.007|   0.2%/290|   0.3%/266|   0.3%/260|   0.3%/254 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 138   |    6583|     659.118|   0.1%/483|   0.2%/446|   0.2%/438|   0.2%/429 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 138   |    4682|     440.972|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 138   |  170773|     518.209|   0.7%/102|   0.7%/104|   0.7%/104|   0.7%/105 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 138   |  108632|     513.843|   1.0%/ 71|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 138   |   57384|     453.349|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 138   |   51342|      37.717|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 138   |   46937|     706.506|   0.1%/830|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 138   |   35288|     585.801|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 138   |   30407|     453.327|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 138   |   28609|     607.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 138   |   24541|     763.782|   1.0%/ 69|   1.0%/ 72|   1.0%/ 73|   0.9%/ 74 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 138   |   19901|     238.684|   1.0%/ 70|   0.9%/ 78|   0.9%/ 81|   0.8%/ 84 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 138   |    1953|     398.352|   1.2%/ 59|   1.0%/ 69|   1.0%/ 71|   0.9%/ 75 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 138   |      29|      39.126|   1.3%/ 53|   1.2%/ 57|   1.2%/ 58|   1.2%/ 59 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 138   |    4614|     633.936|   1.4%/ 51|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 138   |     617|     204.490|   1.8%/ 38|   1.7%/ 41|   1.7%/ 41|   1.6%/ 42 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 138   |   11382|     288.051|   1.4%/ 51|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 138   |    1898|     329.522|   0.2%/291|   0.2%/314|   0.2%/320|   0.2%/325 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 138   |    4456|    1249.710|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 138   |     599|     615.350|   0.1%/671|   0.1%/827|   0.1%/880|   0.1%/941 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 138   |    9610|     447.433|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 138   |    4682|     440.972|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 138   |      32|      22.451|   3.3%/ 21|   4.2%/ 16|   4.5%/ 15|   4.7%/ 14 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 138   |     284|     159.053|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 32 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 138   |    7958|     628.040|   0.2%/316|   0.2%/315|   0.2%/315|   0.2%/315 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 138   |    3129|     464.801|   0.4%/182|   0.4%/177|   0.4%/175|   0.4%/173 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 138   |     981|     311.082|   0.8%/ 89|   0.8%/ 89|   0.8%/ 88|   0.8%/ 88 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 138   |     412|     141.339|   0.9%/ 79|   0.8%/ 83|   0.8%/ 83|   0.8%/ 84 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 138   |     813|     181.915|   0.7%/102|   0.7%/105|   0.7%/105|   0.7%/106 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 138   |    4506|     969.240|   0.8%/ 84|   0.8%/ 86|   0.8%/ 87|   0.8%/ 87 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 138   |     127|      94.827|   0.2%/285|   0.2%/346|   0.2%/366|   0.2%/388 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 138   |    3650|     603.782|   0.3%/265|   0.3%/276|   0.2%/280|   0.2%/283 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 138   |    8836|    1271.445|   0.2%/401|   0.2%/398|   0.2%/397|   0.2%/396 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 138   |    6583|     659.118|   0.1%/483|   0.2%/446|   0.2%/438|   0.2%/429 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 138   |    1741|     308.640|   0.4%/171|   0.4%/160|   0.4%/158|   0.4%/155 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 138   |    2116|     710.926|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 138   |    1391|     226.592|   0.6%/119|   0.5%/134|   0.5%/139|   0.5%/143 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 138   |      89|      82.921|   2.1%/ 33|   1.6%/ 42|   1.5%/ 45|   1.4%/ 49 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 138   |     363|     187.707|   0.6%/107|   0.7%/105|   0.7%/105|   0.7%/105 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 138   |    1080|     350.486|   1.8%/ 38|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 138   |     424|     312.152|   0.1%/506|   0.1%/739|   0.1%/827|   0.1%/936 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 138   |   15917|    1792.029|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 138   |     718|     342.461|   0.7%/104|   0.6%/116|   0.6%/120|   0.6%/124 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 138   |   32848|    1688.529|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 138   |    2385|     227.357|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 138   |     123|     160.947|   1.2%/ 60|   1.3%/ 55|   1.3%/ 54|   1.3%/ 53 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 138   |    3846|     328.990|   0.6%/110|   0.6%/117|   0.6%/119|   0.6%/121 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 138   |     665|     168.039|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 138   |     395|      93.647|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 138   |    7438|     581.007|   0.2%/290|   0.3%/266|   0.3%/260|   0.3%/254 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 138   |     328|     102.692|   2.7%/ 25|   3.0%/ 23|   3.1%/ 22|   3.2%/ 22 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 138   |    1022|     964.359|   0.1%/772|   0.1%/800|   0.1%/805|   0.1%/808 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 138   |    2347|     455.846|   1.8%/ 38|   1.5%/ 46|   1.4%/ 48|   1.4%/ 51 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 138   |     154|     174.581|   1.0%/ 72|   0.9%/ 75|   0.9%/ 77|   0.9%/ 78 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 138   |    1377|     201.497|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 138   |   10998|     379.281|   2.2%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 138   |  170773|     518.209|   0.7%/102|   0.7%/104|   0.7%/104|   0.7%/105 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 138   |     372|     115.913|   1.2%/ 59|   1.0%/ 69|   1.0%/ 72|   0.9%/ 75 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 138   |      58|      93.578|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 138   |    2419|     283.401|   0.5%/127|   0.5%/144|   0.5%/149|   0.4%/156 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 138   |    1781|     233.856|   0.8%/ 90|   0.8%/ 88|   0.8%/ 88|   0.8%/ 87 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 138   |     160|      89.141|   2.3%/ 30|   2.6%/ 26|   2.7%/ 26|   2.8%/ 25 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 138   |    1046|     179.619|   0.7%/100|   0.7%/106|   0.6%/108|   0.6%/110 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 126   |      30|      52.022|   1.0%/ 71|   1.1%/ 64|   1.1%/ 62|   1.1%/ 61 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 138   |    1373|      42.595|   0.5%/145|   0.5%/151|   0.5%/152|   0.5%/152 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 138   |     233|      81.760|   2.3%/ 30|   2.1%/ 33|   2.1%/ 33|   2.0%/ 34 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 138   |    1378|      32.038|   0.8%/ 89|   0.7%/ 95|   0.7%/ 97|   0.7%/ 98 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 138   |      94|       3.018|   2.9%/ 24|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 138   |    5847|     130.120|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 138   |     831|     280.974|   0.6%/111|   0.5%/143|   0.4%/154|   0.4%/167 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 138   |     426|      16.569|   5.3%/ 13|   5.6%/ 12|   5.7%/ 12|   5.7%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 138   |     727|      81.644|   0.1%/671|   0.1%/603|   0.1%/588|   0.1%/573 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 138   |     522|      51.896|   0.7%/ 96|   0.4%/165|   0.3%/202|   0.3%/258 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 138   |     173|     111.884|   0.9%/ 74|   0.8%/ 82|   0.8%/ 84|   0.8%/ 87 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 138   |    3674|      21.811|   1.0%/ 66|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 138   |     613|      65.167|   0.5%/129|   0.4%/159|   0.4%/168|   0.4%/179 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 138   |    9921|     860.841|   0.1%/ ***|   0.1%/843|   0.1%/806|   0.1%/772 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 133   |      39|       3.348|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 138   |    4204|     366.499|   1.9%/ 36|   1.6%/ 43|   1.5%/ 45|   1.5%/ 47 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 138   |     490|     148.348|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41|   1.6%/ 42 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 138   |       3|       1.215|   4.1%/ 17|   3.7%/ 18|   3.7%/ 19|   3.7%/ 19 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 138   |  108632|     513.843|   1.0%/ 71|   0.9%/ 77|   0.9%/ 78|   0.9%/ 80 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 138   |     512|      73.700|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 138   |      54|       2.604|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 126   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 138   |     401|      15.118|   0.2%/380|   0.2%/405|   0.2%/407|   0.2%/409 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 138   |    9077|     238.888|   0.1%/970|   0.1%/987|   0.1%/991|   0.1%/994 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  86   |      61|      11.155|   0.3%/258|   0.3%/210|   0.3%/203|   0.3%/199 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 111   |      76|       4.693|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 138   |   10536|     551.401|   0.6%/114|   0.5%/132|   0.5%/137|   0.5%/143 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 138   |    4700|       3.352|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 138   |   15535|     314.497|   2.6%/ 27|   2.3%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 138   |     329|      65.102|   3.9%/ 18|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 138   |     168|      41.206|   0.8%/ 86|   0.6%/107|   0.6%/115|   0.6%/123 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 138   |      88|       7.880|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 138   |     622|     106.741|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 138   |    1449|     139.922|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 138   |    6108|     349.652|   0.4%/170|   0.4%/195|   0.3%/203|   0.3%/211 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 138   |    5208|      51.938|   0.5%/154|   0.3%/205|   0.3%/223|   0.3%/245 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 138   |     627|      96.712|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.7%/ 42 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 117   |      91|      66.839|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 134   |     544|       5.511|   3.9%/ 18|   3.7%/ 19|   3.7%/ 19|   3.6%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 138   |     333|      60.307|   0.1%/ ***|   0.1%/991|   0.1%/976|   0.1%/964 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 138   |   30407|     453.327|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 138   |      52|      23.822|   0.1%/601|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 138   |      63|      26.835|   6.6%/ 10|  16.0%/  4|  17.8%/  4|  13.6%/  5 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 135   |      17|       4.624|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 138   |    9237|     111.089|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 138   |     235|       7.769|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 138   |     221|      20.622|   0.7%/104|   0.8%/ 87|   0.8%/ 83|   0.9%/ 79 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 138   |    2438|     146.819|   1.4%/ 51|   1.1%/ 61|   1.1%/ 64|   1.0%/ 68 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 124   |      52|       4.230|   0.5%/143|   0.2%/294|   0.2%/403|   0.1%/649 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 113   |      31|      19.233|   1.3%/ 53|   1.7%/ 39|   1.9%/ 37|   2.0%/ 35 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 134   |     196|      16.890|   1.2%/ 57|   1.3%/ 52|   1.4%/ 50|   1.4%/ 49 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 138   |    1658|     180.989|   1.1%/ 63|   0.6%/119|   0.5%/153|   0.3%/213 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 138   |     607|      62.125|   0.1%/581|   0.1%/478|   0.2%/458|   0.2%/441 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 138   |   51342|      37.717|   2.1%/ 33|   2.0%/ 34|   2.0%/ 34|   2.0%/ 35 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 138   |    6212|      23.274|   1.1%/ 62|   1.0%/ 70|   1.0%/ 72|   0.9%/ 75 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 138   |   19901|     238.684|   1.0%/ 70|   0.9%/ 78|   0.9%/ 81|   0.8%/ 84 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 138   |    5928|     151.493|   1.3%/ 53|   1.2%/ 59|   1.1%/ 61|   1.1%/ 63 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 138   |    1775|     360.736|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 138   |     687|      74.803|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 138   |   35288|     585.801|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 138   |      15|       5.361|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 138   |    1084|       8.605|   0.6%/122|   0.7%/101|   0.7%/ 97|   0.7%/ 93 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 138   |      11|       1.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 138   |    1397|      74.774|   0.7%/ 96|   1.0%/ 73|   1.0%/ 68|   1.1%/ 64 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 138   |     501|      10.523|   2.1%/ 33|   1.7%/ 40|   1.6%/ 43|   1.5%/ 45 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 138   |     415|     230.954|   3.5%/ 19|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 135   |     502|     113.619|   0.7%/103|   0.6%/109|   0.6%/111|   0.6%/112 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 136   |    1518|     232.354|   0.4%/158|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 136   |      32|      16.914|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 138   |     101|      14.737|   3.6%/ 19|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 135   |      83|      18.606|   0.6%/115|   0.6%/125|   0.5%/128|   0.5%/132 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 137   |     157|      22.901|   4.0%/ 17|   3.9%/ 17|   3.9%/ 18|   3.9%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 138   |      81|      29.071|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  92   |     175|       6.679|   2.9%/ 24|   2.3%/ 30|   2.1%/ 33|   1.9%/ 35 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 138   |     125|       3.828|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 138   |     125|       6.190|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 138   |     157|      38.584|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 138   |   57384|     453.349|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 138   |     902|     336.402|   0.9%/ 77|   0.9%/ 80|   0.9%/ 81|   0.8%/ 81 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 138   |     633|      17.659|   3.8%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  84   |      20|       0.661|   2.9%/ 24|   2.2%/ 32|   2.0%/ 34|   1.8%/ 37 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  38   |      38|      15.266|   7.3%/  9|  15.1%/  4|  18.3%/  4|  21.4%/  3 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  93   |     106|       3.523|   4.7%/ 15|   5.2%/ 13|   5.3%/ 13|   5.4%/ 13 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 138   |    6189|     354.557|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 138   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 138   |     131|      20.255|   0.6%/114|   0.5%/152|   0.4%/165|   0.4%/182 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 138   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 138   |     988|       4.791|   0.6%/115|   0.5%/132|   0.5%/138|   0.5%/143 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 138   |     551|     265.368|   0.6%/109|   0.5%/147|   0.4%/161|   0.4%/178 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 138   |     257|      47.818|   0.1%/503|   0.2%/361|   0.2%/336|   0.2%/313 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 138   |     585|     125.404|   1.7%/ 41|   1.5%/ 45|   1.5%/ 46|   1.5%/ 48 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 138   |    6203|      28.280|   0.2%/291|   0.2%/379|   0.2%/408|   0.2%/442 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 138   |    1814|     429.981|   1.3%/ 53|   1.1%/ 65|   1.0%/ 68|   0.9%/ 73 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  21   |       3|       0.336|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 138   |     107|      14.988|   5.9%/ 12|   6.6%/ 10|   6.8%/ 10|   6.9%/ 10 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 138   |   24541|     763.782|   1.0%/ 69|   1.0%/ 72|   1.0%/ 73|   0.9%/ 74 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 138   |    2474|      22.796|   1.7%/ 40|   2.0%/ 34|   2.1%/ 33|   2.2%/ 32 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 138   |    1874|      48.824|   0.6%/118|   0.6%/111|   0.6%/110|   0.6%/108 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 138   |    1777|     172.871|   0.2%/399|   0.2%/397|   0.2%/396|   0.2%/394 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 138   |     194|      70.606|   0.7%/ 99|   0.7%/104|   0.7%/105|   0.6%/107 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 138   |    2981|     153.643|   1.6%/ 44|   1.6%/ 42|   1.6%/ 42|   1.7%/ 41 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 138   |   15753|     107.349|   0.8%/ 91|   0.7%/ 99|   0.7%/101|   0.7%/103 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  79   |       8|       0.685|  11.9%/  6|   4.6%/ 15|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 138   |    3409|      99.622|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65|   1.1%/ 66 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 138   |     255|      15.763|   1.4%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 138   |     690|      99.038|   1.0%/ 71|   0.8%/ 90|   0.7%/ 97|   0.7%/104 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 116   |      69|       8.774|   0.2%/325|   0.2%/327|   0.2%/330|   0.2%/333 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 138   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 138   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 138   |     131|      62.715|   0.5%/134|   0.5%/135|   0.5%/136|   0.5%/138 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 131   |      93|       5.852|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 138   |   12408|     211.117|   2.5%/ 28|   2.1%/ 32|   2.0%/ 34|   2.0%/ 35 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 138   |   28609|     607.404|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 138   |      11|       0.505|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 138   |     805|      18.964|   0.5%/153|   0.4%/177|   0.4%/185|   0.4%/193 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 138   |    5794|     560.479|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 138   |    1992|     231.548|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 138   |      61|       3.479|   2.2%/ 32|   1.7%/ 40|   1.6%/ 43|   1.5%/ 46 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 138   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 138   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 138   |      27|       3.648|   4.4%/ 16|   0.0%/ --|   1.3%/ 55|   1.3%/ 55 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 138   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 138   |      53|       4.494|   0.4%/165|   0.5%/127|   0.6%/119|   0.6%/113 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 138   |    5967|      71.763|   0.3%/231|   0.3%/229|   0.3%/228|   0.3%/227 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 138   |  170773|     518.209|   0.7%/102|   0.7%/104|   0.7%/104|   0.7%/105 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  24   |      13|       0.333|  13.7%/  5|  10.0%/  7|   8.9%/  8|   7.6%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 138   |    2096|      50.038|   1.3%/ 54|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 138   |     362|      36.610|   0.2%/309|   0.2%/317|   0.2%/319|   0.2%/321 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 138   |   46937|     706.506|   0.1%/830|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 138   |      38|      10.857|   0.4%/157|   0.4%/174|   0.4%/179|   0.4%/184 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 138   |     242|       7.075|   3.1%/ 22|   2.7%/ 26|   2.6%/ 26|   2.5%/ 27 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 138   |     282|       8.741|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  17   |      24|       0.250|  14.5%/  5|  11.2%/  6|  10.1%/  7|   4.6%/ 15 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 137   |     272|      15.215|   6.4%/ 11|   2.0%/ 34|   1.9%/ 37|   1.9%/ 37 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 138   |     155|      10.256|   0.6%/107|   7.2%/ 10|   2.1%/ 32|   1.0%/ 67 |

