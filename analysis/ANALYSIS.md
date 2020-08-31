# State and Country COVID-19 Analysis #
## Updated: at 2020-08-31 for data as of 2020-08-30 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.1% of deaths and 39.9% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.1% of deaths and 57.8% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 152   |   32949|    1693.742|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 152   |   15955|    1796.248|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 152   |   13139|     332.531|   1.0%/ 68|   0.9%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 152   |   13324|     459.520|   1.5%/ 46|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 152   |   11532|     536.939|   1.3%/ 55|   1.0%/ 67|   1.0%/ 71|   0.9%/ 75 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 152   |    9044|    1301.363|   0.2%/390|   0.2%/379|   0.2%/376|   0.2%/374 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 152   |    8230|     649.441|   0.2%/285|   0.2%/278|   0.3%/276|   0.3%/274 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 152   |    7674|     599.454|   0.2%/325|   0.2%/330|   0.2%/332|   0.2%/333 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 152   |    6731|     673.955|   0.2%/440|   0.2%/425|   0.2%/421|   0.2%/417 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 152   |    5635|     530.772|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 152   |  184183|     558.902|   0.5%/127|   0.5%/135|   0.5%/137|   0.5%/139 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 152   |  121998|     577.061|   0.8%/ 85|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 152   |   65391|      48.038|   1.7%/ 40|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 152   |   64902|     512.744|   0.9%/ 77|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 152   |   41101|     618.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 152   |   35518|     589.619|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 152   |   30607|     456.309|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 152   |   29021|     616.156|   0.1%/926|   0.1%/832|   0.1%/811|   0.1%/792 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 152   |   30099|     936.737|   0.7%/104|   0.6%/119|   0.6%/124|   0.5%/128 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 152   |   21755|     260.917|   0.6%/107|   0.5%/127|   0.5%/133|   0.5%/139 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 152   |    2157|     439.978|   0.9%/ 79|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 152   |      37|      50.130|   1.1%/ 65|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 152   |    5102|     700.978|   0.8%/ 82|   0.7%/ 97|   0.7%/101|   0.7%/106 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 152   |     778|     257.891|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 152   |   13139|     332.531|   1.0%/ 68|   0.9%/ 73|   0.9%/ 75|   0.9%/ 77 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 152   |    1944|     337.619|   0.2%/356|   0.2%/362|   0.2%/363|   0.2%/364 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 152   |    4468|    1253.297|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 152   |     605|     621.662|   0.1%/595|   0.1%/603|   0.1%/605|   0.1%/608 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 152   |   11532|     536.939|   1.3%/ 55|   1.0%/ 67|   1.0%/ 71|   0.9%/ 75 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 152   |    5635|     530.772|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 152   |      60|      42.222|   3.3%/ 21|   3.7%/ 19|   3.8%/ 18|   3.8%/ 18 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 152   |     364|     203.504|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 152   |    8230|     649.441|   0.2%/285|   0.2%/278|   0.3%/276|   0.3%/274 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 152   |    3304|     490.843|   0.4%/194|   0.3%/199|   0.3%/201|   0.3%/203 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 152   |    1109|     351.469|   0.9%/ 76|   1.0%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 152   |     452|     155.172|   0.7%/ 95|   0.7%/ 99|   0.7%/100|   0.7%/101 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 152   |     929|     207.965|   0.9%/ 76|   1.0%/ 72|   1.0%/ 72|   1.0%/ 71 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 152   |    4986|    1072.552|   0.7%/101|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 152   |     133|      98.618|   0.3%/255|   0.3%/252|   0.3%/252|   0.3%/252 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 152   |    3750|     620.319|   0.2%/323|   0.2%/335|   0.2%/338|   0.2%/341 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 152   |    9044|    1301.363|   0.2%/390|   0.2%/379|   0.2%/376|   0.2%/374 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 152   |    6731|     673.955|   0.2%/440|   0.2%/425|   0.2%/421|   0.2%/417 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 152   |    1872|     331.848|   0.5%/146|   0.5%/143|   0.5%/143|   0.5%/143 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 152   |    2474|     831.168|   1.1%/ 61|   1.0%/ 66|   1.0%/ 67|   1.0%/ 69 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 152   |    1525|     248.506|   0.7%/102|   0.7%/ 99|   0.7%/ 99|   0.7%/ 98 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 152   |     104|      97.671|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 152   |     396|     204.657|   0.6%/118|   0.6%/124|   0.6%/125|   0.5%/127 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 152   |    1336|     433.876|   1.4%/ 48|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 152   |     433|     318.203|   0.1%/478|   0.1%/474|   0.1%/474|   0.1%/473 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 152   |   15955|    1796.248|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 152   |     776|     370.292|   0.6%/124|   0.5%/132|   0.5%/135|   0.5%/137 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 152   |   32949|    1693.742|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 152   |    2716|     258.925|   1.0%/ 72|   0.9%/ 76|   0.9%/ 78|   0.9%/ 79 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 152   |     145|     190.270|   1.0%/ 72|   0.9%/ 81|   0.8%/ 84|   0.8%/ 87 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 152   |    4148|     354.830|   0.6%/119|   0.6%/120|   0.6%/120|   0.6%/120 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 152   |     803|     202.831|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 152   |     457|     108.394|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 152   |    7674|     599.454|   0.2%/325|   0.2%/330|   0.2%/332|   0.2%/333 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 152   |     448|     140.324|   2.0%/ 34|   1.9%/ 36|   1.9%/ 37|   1.8%/ 38 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 152   |    1045|     986.088|   0.2%/399|   0.2%/351|   0.2%/341|   0.2%/331 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 152   |    2757|     535.503|   1.3%/ 53|   1.2%/ 60|   1.1%/ 62|   1.1%/ 63 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 152   |     168|     190.063|   0.7%/105|   0.6%/116|   0.6%/119|   0.6%/122 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 152   |    1763|     257.960|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42|   1.7%/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 152   |   13324|     459.520|   1.5%/ 46|   1.3%/ 53|   1.3%/ 55|   1.2%/ 57 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 152   |  184183|     558.902|   0.5%/127|   0.5%/135|   0.5%/137|   0.5%/139 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 152   |     415|     129.323|   0.8%/ 84|   0.7%/ 94|   0.7%/ 97|   0.7%/100 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 152   |      58|      93.183|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 152   |    2560|     299.936|   0.5%/130|   0.5%/126|   0.6%/125|   0.6%/123 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 152   |    1939|     254.687|   0.5%/133|   0.4%/157|   0.4%/165|   0.4%/174 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 152   |     209|     116.742|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 152   |    1127|     193.603|   0.6%/123|   0.5%/129|   0.5%/131|   0.5%/133 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 140   |      39|      67.265|   0.3%/247|   0.1%/825|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 152   |    1419|      44.032|   0.2%/330|   0.1%/503|   0.1%/581|   0.1%/690 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 152   |     283|      99.361|   1.6%/ 44|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 152   |    1508|      35.063|   0.7%/106|   0.6%/112|   0.6%/114|   0.6%/116 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 152   |     113|       3.644|   1.5%/ 45|   1.2%/ 59|   1.1%/ 63|   1.0%/ 69 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 152   |    8743|     194.546|   2.9%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 152   |     881|     297.929|   0.5%/152|   0.4%/171|   0.4%/177|   0.4%/182 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 152   |     667|      25.953|   3.2%/ 22|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 152   |     735|      82.597|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 152   |     534|      52.999|   0.3%/209|   0.2%/286|   0.2%/313|   0.2%/343 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 152   |     194|     125.384|   0.7%/ 99|   0.6%/117|   0.6%/123|   0.5%/129 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 152   |    4251|      25.232|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 152   |     672|      71.436|   0.7%/ 96|   0.8%/ 91|   0.8%/ 89|   0.8%/ 88 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 152   |   10044|     871.559|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 147   |      40|       3.414|   0.2%/289|   0.2%/296|   0.2%/296|   0.2%/296 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 152   |    5035|     438.939|   1.4%/ 48|   1.3%/ 52|   1.3%/ 53|   1.3%/ 55 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 152   |     616|     186.690|   1.6%/ 43|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 152   |       4|       1.576|   3.3%/ 21|   3.6%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 152   |  121998|     577.061|   0.8%/ 85|   0.8%/ 91|   0.7%/ 93|   0.7%/ 94 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 152   |     618|      88.907|   1.4%/ 48|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 152   |      55|       2.651|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 140   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 152   |     414|      15.579|   0.2%/420|   0.1%/480|   0.1%/501|   0.1%/525 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 152   |    9166|     241.223|   0.1%/977|   0.1%/970|   0.1%/969|   0.1%/967 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 100   |      61|      11.104|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 125   |      77|       4.733|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 152   |   11262|     589.395|   0.5%/134|   0.5%/140|   0.5%/142|   0.5%/143 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 152   |    4722|       3.367|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 152   |   19813|     401.112|   1.8%/ 38|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 152   |     443|      87.677|   2.6%/ 27|   2.1%/ 32|   2.0%/ 34|   1.9%/ 36 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 152   |     181|      44.510|   0.8%/ 88|   0.8%/ 84|   0.8%/ 83|   0.9%/ 81 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 152   |      92|       8.182|   0.4%/177|   0.5%/139|   0.5%/132|   0.6%/125 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 152   |     624|     107.250|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 152   |    1704|     164.482|   1.1%/ 61|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 152   |    6525|     373.563|   0.5%/129|   0.6%/120|   0.6%/118|   0.6%/115 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 152   |    5403|      53.882|   0.3%/209|   0.3%/226|   0.3%/230|   0.3%/234 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 152   |     731|     112.634|   1.2%/ 60|   1.0%/ 73|   0.9%/ 77|   0.9%/ 81 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 131   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 148   |     836|       8.477|   2.9%/ 24|   2.5%/ 27|   2.4%/ 28|   2.3%/ 30 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 152   |     336|      60.727|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 152   |   30607|     456.309|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 152   |      54|      24.652|   0.1%/762|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 152   |     136|      58.041|   1.2%/ 59|   2.2%/ 32|   1.1%/ 65|   1.1%/ 65 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 149   |      19|       4.995|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 152   |    9306|     111.924|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 152   |     286|       9.449|   1.0%/ 69|   0.8%/ 91|   0.7%/ 99|   0.6%/109 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 152   |     258|      24.051|   1.0%/ 68|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 152   |    2787|     167.877|   1.0%/ 69|   0.9%/ 78|   0.9%/ 80|   0.8%/ 82 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 138   |      58|       4.783|   1.1%/ 65|   1.3%/ 55|   1.3%/ 53|   1.4%/ 51 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 127   |      35|      21.781|   0.3%/216|   0.2%/278|   0.2%/294|   0.2%/312 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 148   |     205|      17.705|   0.4%/198|   0.2%/451|   0.1%/656|   0.1%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 152   |    1820|     198.736|   1.2%/ 58|   1.3%/ 55|   1.3%/ 53|   1.3%/ 52 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 152   |     616|      63.034|   0.1%/901|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 152   |   65391|      48.038|   1.7%/ 40|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 152   |    7281|      27.278|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 51 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 152   |   21755|     260.917|   0.6%/107|   0.5%/127|   0.5%/133|   0.5%/139 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 152   |    7014|     179.263|   1.2%/ 57|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 152   |    1779|     361.483|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 152   |     942|     102.517|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 152   |   35518|     589.619|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 152   |      20|       7.162|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 152   |    1269|      10.074|   1.0%/ 67|   1.2%/ 60|   1.2%/ 59|   1.2%/ 57 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 152   |      11|       1.032|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 152   |    1635|      87.526|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63|   1.1%/ 63 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 152   |     601|      12.644|   1.2%/ 56|   1.0%/ 72|   0.9%/ 78|   0.8%/ 84 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 152   |     531|     295.470|   1.5%/ 45|   1.1%/ 66|   0.9%/ 74|   0.8%/ 85 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 149   |     533|     120.616|   0.4%/160|   0.4%/185|   0.4%/192|   0.3%/200 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 150   |    1028|     157.389|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 150   |      34|      17.706|   0.4%/189|   0.4%/155|   0.5%/148|   0.5%/142 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 152   |     159|      23.317|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 149   |      83|      18.559|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 151   |     243|      35.353|   3.4%/ 21|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 152   |      86|      30.636|   0.4%/187|   0.5%/153|   0.5%/147|   0.5%/141 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 106   |     191|       7.260|   1.0%/ 70|   0.8%/ 89|   0.7%/ 94|   0.7%/ 99 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 152   |     125|       3.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 152   |     126|       6.212|   0.1%/ ***|   0.1%/ ***|   0.1%/970|   0.1%/935 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 152   |     158|      38.828|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 152   |   64902|     512.744|   0.9%/ 77|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 152   |     997|     371.860|   0.8%/ 92|   0.7%/ 96|   0.7%/ 97|   0.7%/ 98 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 152   |    1147|      31.966|   3.8%/ 18|   3.7%/ 19|   3.7%/ 19|   3.7%/ 19 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  98   |      22|       0.735|   1.2%/ 59|   1.3%/ 55|   1.3%/ 53|   1.3%/ 52 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  52   |      72|      29.383|   6.1%/ 11|   5.2%/ 13|   4.9%/ 14|   4.6%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 107   |     215|       7.163|   5.4%/ 13|   5.7%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 152   |    6249|     357.970|   0.1%/ ***|   0.1%/936|   0.1%/909|   0.1%/883 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 152   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 152   |     139|      21.514|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 152   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 152   |    1027|       4.982|   0.3%/262|   0.2%/417|   0.1%/490|   0.1%/592 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 152   |     594|     285.893|   0.7%/ 99|   0.7%/ 95|   0.7%/ 94|   0.7%/ 92 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 152   |     266|      49.516|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 152   |     686|     146.958|   1.1%/ 63|   0.9%/ 74|   0.9%/ 77|   0.9%/ 81 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 152   |    6314|      28.785|   0.1%/498|   0.1%/625|   0.1%/667|   0.1%/715 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 152   |    2026|     480.244|   0.9%/ 81|   0.7%/ 96|   0.7%/101|   0.7%/106 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  35   |       5|       0.583|   1.9%/ 37|   4.9%/ 14|   6.9%/ 10|   8.9%/  8 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 152   |     322|      45.028|   6.1%/ 11|   6.3%/ 11|   6.3%/ 11|   6.3%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 152   |   30099|     936.737|   0.7%/104|   0.6%/119|   0.6%/124|   0.5%/128 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 152   |    3437|      31.677|   2.3%/ 30|   2.5%/ 28|   2.5%/ 27|   2.6%/ 27 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 152   |    2039|      53.141|   0.6%/116|   0.6%/116|   0.6%/116|   0.6%/116 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 152   |    1820|     177.075|   0.2%/393|   0.2%/388|   0.2%/387|   0.2%/385 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 152   |     199|      72.328|   0.2%/321|   0.1%/666|   0.1%/899|   0.1%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 152   |    3613|     186.206|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.2%/ 55 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 152   |   17114|     116.623|   0.6%/111|   0.6%/117|   0.6%/118|   0.6%/120 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  93   |      17|       1.392|   8.4%/  8|   2.2%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 152   |    3907|     114.173|   0.9%/ 74|   0.9%/ 79|   0.9%/ 80|   0.9%/ 81 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 152   |     288|      17.772|   0.9%/ 79|   0.8%/ 92|   0.7%/ 96|   0.7%/100 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 152   |     726|     104.322|   0.4%/177|   0.2%/304|   0.2%/370|   0.1%/471 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 130   |      70|       8.834|   0.1%/551|   0.1%/540|   0.1%/528|   0.1%/512 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 152   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 152   |      34|       6.168|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 152   |     134|      64.086|   0.2%/416|   0.1%/770|   0.1%/965|   0.1%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 145   |      95|       5.977|   0.3%/222|   0.4%/160|   0.5%/148|   0.5%/139 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 152   |   14622|     248.772|   1.2%/ 56|   0.9%/ 76|   0.8%/ 84|   0.7%/ 93 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 152   |   29021|     616.156|   0.1%/926|   0.1%/832|   0.1%/811|   0.1%/792 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 152   |      12|       0.552|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 152   |     832|      19.614|   0.2%/321|   0.1%/486|   0.1%/558|   0.1%/655 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 152   |    5829|     563.780|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 152   |    2006|     233.151|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 152   |     111|       6.357|   2.9%/ 24|   3.0%/ 23|   3.1%/ 22|   3.1%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 152   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 152   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 152   |      29|       3.820|   0.2%/430|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 152   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 152   |      77|       6.527|   1.3%/ 52|   1.5%/ 45|   1.6%/ 43|   1.7%/ 42 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 152   |    6272|      75.431|   0.4%/188|   0.4%/178|   0.4%/175|   0.4%/173 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 152   |  184183|     558.902|   0.5%/127|   0.5%/135|   0.5%/137|   0.5%/139 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  38   |      30|       0.754|   6.4%/ 11|   5.1%/ 13|   3.8%/ 18|   2.3%/ 30 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 152   |    2546|      60.801|   1.5%/ 47|   1.5%/ 45|   1.6%/ 45|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 152   |     381|      38.566|   0.3%/207|   0.4%/197|   0.4%/195|   0.4%/194 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 152   |   41101|     618.653|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 152   |      44|      12.549|   0.8%/ 82|   0.9%/ 78|   0.9%/ 77|   0.9%/ 76 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 152   |     323|       9.451|   2.2%/ 32|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 152   |     397|      12.315|   2.3%/ 30|   2.0%/ 34|   2.0%/ 35|   1.9%/ 37 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  31   |      32|       0.334|   2.3%/ 29|   3.0%/ 23|   2.6%/ 26|   2.2%/ 32 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 151   |     308|      17.222|   0.6%/113|   0.4%/186|   0.3%/223|   0.2%/280 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 152   |     205|      13.541|   2.9%/ 24|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |

