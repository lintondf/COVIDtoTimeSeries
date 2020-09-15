# State and Country COVID-19 Analysis #
## Updated: at 2020-09-15 for data as of 2020-09-14 ##

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.6% of deaths and 56.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 167   |   33046|    1698.736|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 167   |   16024|    1804.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 167   |   14800|     510.416|   0.9%/ 80|   0.7%/ 98|   0.7%/104|   0.6%/110 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 167   |   14641|     370.542|   0.7%/ 95|   0.6%/107|   0.6%/110|   0.6%/114 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 167   |   12846|     598.097|   0.8%/ 84|   0.7%/ 97|   0.7%/101|   0.7%/105 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 167   |    9227|    1327.741|   0.1%/507|   0.1%/532|   0.1%/538|   0.1%/545 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 167   |    8554|     675.040|   0.3%/267|   0.3%/262|   0.3%/261|   0.3%/260 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 167   |    7866|     614.417|   0.2%/437|   0.1%/475|   0.1%/485|   0.1%/496 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 167   |    6921|     693.004|   0.2%/433|   0.2%/436|   0.2%/437|   0.2%/437 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 167   |    6504|     612.579|   0.9%/ 79|   0.8%/ 91|   0.7%/ 94|   0.7%/ 98 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 167   |  195734|     593.954|   0.4%/169|   0.4%/183|   0.4%/187|   0.4%/192 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 167   |  133453|     631.245|   0.6%/116|   0.5%/129|   0.5%/132|   0.5%/136 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 167   |   81103|      59.581|   1.5%/ 48|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 167   |   71866|     567.761|   0.7%/100|   0.6%/108|   0.6%/111|   0.6%/113 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 167   |   41726|     628.072|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 167   |   35617|     591.271|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 167   |   30905|     460.740|   0.1%/983|   0.1%/901|   0.1%/882|   0.1%/863 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 167   |   31099|     967.861|   0.5%/150|   0.4%/170|   0.4%/176|   0.4%/183 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 167   |   29800|     632.694|   0.2%/422|   0.2%/385|   0.2%/376|   0.2%/369 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 167   |   23341|     279.938|   0.5%/130|   0.5%/138|   0.5%/140|   0.5%/142 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 167   |    2396|     488.582|   0.6%/108|   0.6%/120|   0.6%/123|   0.5%/127 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 167   |      46|      63.231|   1.1%/ 66|   1.0%/ 69|   1.0%/ 69|   1.0%/ 70 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 167   |    5424|     745.171|   0.4%/169|   0.3%/228|   0.3%/250|   0.3%/277 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 167   |    1017|     336.883|   1.6%/ 43|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 167   |   14641|     370.542|   0.7%/ 95|   0.6%/107|   0.6%/110|   0.6%/114 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 167   |    1995|     346.389|   0.2%/423|   0.2%/445|   0.2%/450|   0.2%/456 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 167   |    4480|    1256.470|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 167   |     615|     631.295|   0.1%/545|   0.1%/525|   0.1%/519|   0.1%/513 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 167   |   12846|     598.097|   0.8%/ 84|   0.7%/ 97|   0.7%/101|   0.7%/105 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 167   |    6504|     612.579|   0.9%/ 79|   0.8%/ 91|   0.7%/ 94|   0.7%/ 98 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 167   |     108|      76.259|   2.8%/ 24|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 167   |     435|     243.642|   1.0%/ 72|   0.7%/ 97|   0.7%/106|   0.6%/118 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 167   |    8554|     675.040|   0.3%/267|   0.3%/262|   0.3%/261|   0.3%/260 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 167   |    3452|     512.789|   0.3%/230|   0.3%/240|   0.3%/243|   0.3%/245 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 167   |    1243|     393.844|   0.7%/102|   0.6%/110|   0.6%/112|   0.6%/115 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 167   |     522|     179.066|   1.2%/ 56|   1.4%/ 51|   1.4%/ 49|   1.4%/ 48 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 167   |    1070|     239.503|   0.9%/ 75|   0.9%/ 75|   0.9%/ 75|   0.9%/ 75 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 167   |    5291|    1138.181|   0.4%/165|   0.4%/194|   0.3%/202|   0.3%/212 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 167   |     136|     101.170|   0.2%/364|   0.2%/397|   0.2%/406|   0.2%/415 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 167   |    3853|     637.364|   0.2%/409|   0.2%/441|   0.2%/450|   0.2%/460 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 167   |    9227|    1327.741|   0.1%/507|   0.1%/532|   0.1%/538|   0.1%/545 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 167   |    6921|     693.004|   0.2%/433|   0.2%/436|   0.2%/437|   0.2%/437 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 167   |    1971|     349.490|   0.4%/176|   0.4%/179|   0.4%/179|   0.4%/180 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 167   |    2762|     928.103|   0.7%/100|   0.6%/119|   0.6%/125|   0.5%/132 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 167   |    1758|     286.488|   0.7%/ 98|   0.7%/100|   0.7%/100|   0.7%/101 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 167   |     135|     126.443|   2.0%/ 35|   2.1%/ 33|   2.1%/ 33|   2.1%/ 32 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 167   |     433|     224.048|   0.7%/104|   0.7%/100|   0.7%/ 98|   0.7%/ 97 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 167   |    1498|     486.185|   0.8%/ 91|   0.6%/116|   0.6%/124|   0.5%/133 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 167   |     436|     320.629|   0.1%/953|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 167   |   16024|    1804.074|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 167   |     833|     397.260|   0.4%/167|   0.4%/190|   0.4%/197|   0.3%/204 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 167   |   33046|    1698.736|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 167   |    3098|     295.370|   0.9%/ 79|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 167   |     168|     220.566|   1.2%/ 60|   1.2%/ 58|   1.2%/ 57|   1.2%/ 57 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 167   |    4445|     380.285|   0.5%/145|   0.5%/151|   0.5%/152|   0.5%/154 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 167   |     923|     233.185|   0.9%/ 75|   0.8%/ 84|   0.8%/ 86|   0.8%/ 88 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 167   |     517|     122.637|   0.8%/ 85|   0.7%/ 94|   0.7%/ 97|   0.7%/ 99 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 167   |    7866|     614.417|   0.2%/437|   0.1%/475|   0.1%/485|   0.1%/496 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 167   |     545|     170.513|   1.6%/ 43|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 167   |    1073|    1012.640|   0.2%/380|   0.2%/366|   0.2%/362|   0.2%/359 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 167   |    3125|     606.939|   0.9%/ 79|   0.8%/ 89|   0.8%/ 92|   0.7%/ 95 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 167   |     182|     205.604|   0.7%/ 94|   0.8%/ 88|   0.8%/ 86|   0.8%/ 85 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 167   |    2108|     308.429|   1.3%/ 53|   1.3%/ 55|   1.2%/ 56|   1.2%/ 56 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 167   |   14800|     510.416|   0.9%/ 80|   0.7%/ 98|   0.7%/104|   0.6%/110 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 167   |  195734|     593.954|   0.4%/169|   0.4%/183|   0.4%/187|   0.4%/192 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 167   |     441|     137.502|   0.4%/154|   0.4%/192|   0.3%/205|   0.3%/218 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 167   |      58|      92.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 167   |    2770|     324.502|   0.4%/166|   0.4%/185|   0.4%/190|   0.4%/197 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 167   |    2016|     264.718|   0.3%/244|   0.2%/312|   0.2%/334|   0.2%/360 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 167   |     284|     158.376|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 167   |    1217|     208.935|   0.5%/129|   0.5%/130|   0.5%/131|   0.5%/131 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 155   |      44|      75.875|   0.1%/801|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 167   |    1427|      44.293|   0.1%/888|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 167   |     347|     121.930|   1.2%/ 57|   1.1%/ 63|   1.1%/ 66|   1.0%/ 68 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 167   |    1628|      37.859|   0.5%/134|   0.5%/143|   0.5%/145|   0.5%/148 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 167   |     135|       4.351|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 167   |   12049|     268.112|   2.1%/ 33|   1.9%/ 36|   1.8%/ 37|   1.8%/ 38 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 167   |     923|     312.014|   0.3%/219|   0.3%/247|   0.3%/256|   0.3%/265 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 167   |     955|      37.168|   1.4%/ 51|   0.9%/ 78|   0.8%/ 90|   0.7%/106 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 167   |     751|      84.318|   0.2%/420|   0.2%/351|   0.2%/336|   0.2%/322 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 167   |     564|      56.060|   0.4%/178|   0.4%/178|   0.4%/178|   0.4%/178 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 167   |     211|     136.734|   0.8%/ 88|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 167   |    4813|      28.567|   0.8%/ 87|   0.7%/ 94|   0.7%/ 96|   0.7%/ 98 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 167   |     754|      80.185|   0.8%/ 91|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 167   |    9921|     860.830|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 162   |      40|       3.435|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 167   |    7384|     643.760|   1.0%/ 70|   0.8%/ 82|   0.8%/ 86|   0.8%/ 90 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 167   |     723|     219.011|   1.0%/ 66|   0.9%/ 78|   0.8%/ 82|   0.8%/ 86 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 167   |      12|       4.981|   6.0%/ 11|   6.1%/ 11|   6.2%/ 11|   6.2%/ 11 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 167   |  133453|     631.245|   0.6%/116|   0.5%/129|   0.5%/132|   0.5%/136 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 167   |     747|     107.412|   1.1%/ 62|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 167   |      56|       2.681|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 155   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 167   |     417|      15.725|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 167   |    9235|     243.039|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 115   |      62|      11.322|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 140   |      80|       4.917|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 167   |   12027|     629.463|   0.5%/153|   0.4%/159|   0.4%/160|   0.4%/161 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 167   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 167   |   23779|     481.399|   1.2%/ 58|   1.0%/ 67|   1.0%/ 70|   0.9%/ 73 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 167   |     613|     121.255|   2.4%/ 29|   2.3%/ 29|   2.3%/ 29|   2.3%/ 30 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 167   |     217|      53.208|   1.4%/ 49|   1.6%/ 44|   1.6%/ 42|   1.7%/ 41 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 167   |     108|       9.635|   0.8%/ 82|   0.9%/ 73|   1.0%/ 71|   1.0%/ 69 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 167   |     630|     108.272|   0.1%/875|   0.1%/767|   0.1%/744|   0.1%/722 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 167   |    2011|     194.158|   1.0%/ 68|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 167   |    7026|     402.209|   0.5%/146|   0.5%/149|   0.5%/149|   0.5%/150 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 167   |    5671|      56.553|   0.3%/217|   0.3%/221|   0.3%/222|   0.3%/223 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 167   |     806|     124.308|   0.7%/104|   0.5%/130|   0.5%/138|   0.5%/148 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 146   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 163   |    1074|      10.885|   1.7%/ 42|   1.3%/ 52|   1.2%/ 56|   1.2%/ 60 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 167   |     337|      61.013|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 167   |   30905|     460.740|   0.1%/983|   0.1%/901|   0.1%/882|   0.1%/863 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 167   |      53|      24.478|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 167   |     114|      48.516|   0.0%/ --|   1.0%/ 69|   1.0%/ 70|   1.0%/ 70 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 164   |      20|       5.238|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 167   |    9362|     112.598|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 167   |     295|       9.744|   0.3%/217|   0.1%/469|   0.1%/649|   0.1%/ *** |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 167   |     310|      28.889|   1.1%/ 65|   1.1%/ 64|   1.1%/ 64|   1.1%/ 63 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 167   |    3019|     181.832|   0.5%/126|   0.4%/160|   0.4%/171|   0.4%/183 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 153   |      65|       5.309|   0.5%/141|   0.3%/204|   0.3%/231|   0.3%/267 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 142   |      40|      24.698|   0.5%/149|   0.5%/138|   0.5%/136|   0.5%/134 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 163   |     220|      18.976|   0.5%/134|   0.5%/127|   0.6%/126|   0.6%/124 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 167   |    2153|     235.046|   0.8%/ 82|   0.7%/ 93|   0.7%/ 97|   0.7%/101 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 167   |     633|      64.736|   0.2%/288|   0.3%/246|   0.3%/237|   0.3%/229 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 167   |   81103|      59.581|   1.5%/ 48|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 167   |    8876|      33.254|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 167   |   23341|     279.938|   0.5%/130|   0.5%/138|   0.5%/140|   0.5%/142 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 167   |    8171|     208.836|   1.0%/ 70|   0.9%/ 74|   0.9%/ 76|   0.9%/ 77 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 167   |    1781|     361.961|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 167   |    1154|     125.623|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 167   |   35617|     591.271|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 167   |      45|      16.418|   4.8%/ 14|   5.5%/ 12|   5.7%/ 12|   5.9%/ 12 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 167   |    1475|      11.713|   0.9%/ 79|   0.8%/ 83|   0.8%/ 84|   0.8%/ 86 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 167   |      18|       1.704|   3.8%/ 18|   4.3%/ 16|   4.4%/ 15|   4.6%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 167   |    1690|      90.445|   0.4%/167|   0.3%/267|   0.2%/316|   0.2%/387 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 167   |     636|      13.380|   0.5%/130|   0.4%/196|   0.3%/223|   0.3%/257 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 167   |     513|     285.610|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 164   |     563|     127.260|   0.4%/173|   0.4%/175|   0.4%/176|   0.4%/176 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 165   |    1005|     153.805|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 165   |      35|      18.596|   0.2%/374|   0.1%/488|   0.1%/533|   0.1%/589 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 167   |     250|      36.693|   3.1%/ 22|   3.1%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 164   |      82|      18.330|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 166   |     371|      54.047|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 167   |      87|      31.246|   0.1%/635|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 121   |     214|       8.157|   0.8%/ 92|   0.7%/100|   0.7%/103|   0.7%/106 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 167   |     129|       3.927|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 167   |     128|       6.316|   0.1%/578|   0.1%/503|   0.1%/487|   0.1%/473 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 167   |     161|      39.544|   0.1%/734|   0.1%/704|   0.1%/698|   0.1%/693 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 167   |   71866|     567.761|   0.7%/100|   0.6%/108|   0.6%/111|   0.6%/113 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 167   |    1136|     423.765|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84|   0.8%/ 84 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 167   |    1833|      51.109|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 113   |      34|       1.139|   3.3%/ 21|   3.9%/ 18|   4.1%/ 17|   4.3%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  67   |     103|      41.706|   2.1%/ 34|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 122   |     376|      12.518|   3.3%/ 21|   2.6%/ 26|   2.4%/ 28|   2.2%/ 31 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 167   |    6301|     360.962|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 167   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 167   |     146|      22.582|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 167   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 167   |    1087|       5.271|   0.4%/187|   0.4%/185|   0.4%/184|   0.4%/184 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 167   |     653|     314.565|   0.6%/108|   0.6%/109|   0.6%/109|   0.6%/109 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 167   |     265|      49.398|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 167   |     789|     169.225|   1.0%/ 68|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 167   |    6403|      29.192|   0.1%/725|   0.1%/848|   0.1%/886|   0.1%/927 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 167   |    2197|     520.878|   0.6%/120|   0.5%/137|   0.5%/142|   0.5%/148 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  50   |       6|       0.665|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 167   |     620|      86.615|   3.8%/ 18|   3.2%/ 22|   3.0%/ 23|   2.9%/ 24 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 167   |   31099|     967.861|   0.5%/150|   0.4%/170|   0.4%/176|   0.4%/183 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 167   |    4452|      41.023|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 167   |    2210|      57.575|   0.5%/135|   0.5%/140|   0.5%/141|   0.5%/143 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 167   |    1866|     181.589|   0.2%/374|   0.2%/361|   0.2%/358|   0.2%/355 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 167   |     207|      75.303|   0.3%/259|   0.3%/260|   0.3%/261|   0.3%/262 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 167   |    4266|     219.855|   1.0%/ 66|   1.0%/ 71|   1.0%/ 73|   0.9%/ 74 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 167   |   18636|     126.995|   0.6%/119|   0.6%/121|   0.6%/122|   0.6%/122 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 108   |      23|       1.861|   3.6%/ 19|   1.6%/ 44|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 167   |    4335|     126.681|   0.7%/ 99|   0.6%/108|   0.6%/111|   0.6%/113 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 167   |     302|      18.632|   0.3%/200|   0.2%/310|   0.2%/358|   0.2%/424 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 167   |     739|     106.093|   0.2%/387|   0.1%/595|   0.1%/684|   0.1%/803 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 145   |      72|       9.157|   0.2%/386|   0.2%/393|   0.2%/396|   0.2%/401 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 167   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 167   |      38|       7.035|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 167   |     136|      64.977|   0.1%/835|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 160   |      99|       6.205|   0.1%/587|   0.1%/686|   0.1%/719|   0.1%/756 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 167   |   15915|     270.770|   0.6%/108|   0.5%/146|   0.4%/160|   0.4%/177 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 167   |   29800|     632.694|   0.2%/422|   0.2%/385|   0.2%/376|   0.2%/369 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 167   |      12|       0.562|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 167   |     839|      19.767|   0.1%/809|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 167   |    5850|     565.864|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 167   |    2023|     235.145|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 167   |     167|       9.521|   2.4%/ 28|   2.2%/ 31|   2.2%/ 31|   2.1%/ 32 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 167   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 167   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 167   |      37|       4.904|   1.8%/ 38|   2.2%/ 31|   2.3%/ 30|   2.4%/ 28 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 167   |      56|      40.777|   6.8%/ 10|   7.1%/ 10|   7.2%/ 10|   7.2%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 167   |     109|       9.308|   2.4%/ 29|   2.7%/ 26|   2.7%/ 25|   2.8%/ 25 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 167   |    7014|      84.350|   0.8%/ 90|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 167   |  195734|     593.954|   0.4%/169|   0.4%/183|   0.4%/187|   0.4%/192 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  53   |      56|       1.397|   5.1%/ 13|   4.0%/ 17|   3.7%/ 18|   3.5%/ 19 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 167   |    3278|      78.263|   1.7%/ 42|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 167   |     400|      40.490|   0.3%/222|   0.3%/229|   0.3%/231|   0.3%/233 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 167   |   41726|     628.072|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 167   |      46|      13.136|   0.2%/381|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 167   |     402|      11.768|   1.6%/ 43|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 167   |     499|      15.474|   1.8%/ 39|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  46   |      35|       0.364|   0.1%/686|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 166   |     312|      17.433|   0.4%/172|   0.3%/200|   0.3%/207|   0.3%/214 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 167   |     242|      15.950|   0.9%/ 74|   0.3%/204|   0.2%/366|   0.0%/ *** |

