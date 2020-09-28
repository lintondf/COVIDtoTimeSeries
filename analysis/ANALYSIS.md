# State and Country COVID-19 Analysis #
## Updated: at 2020-09-28 for data as of 2020-09-27 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 65.9% of deaths and 55.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 180   |   33127|    1702.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 180   |   16107|    1813.455|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 180   |   15968|     550.703|   0.6%/107|   0.6%/122|   0.5%/126|   0.5%/130 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 180   |   15773|     399.185|   0.6%/116|   0.5%/126|   0.5%/129|   0.5%/131 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 180   |   14143|     658.500|   0.8%/ 87|   0.8%/ 90|   0.8%/ 91|   0.8%/ 92 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 180   |    9397|    1352.138|   0.1%/472|   0.1%/465|   0.1%/463|   0.2%/461 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 180   |    8842|     697.757|   0.3%/263|   0.3%/260|   0.3%/259|   0.3%/258 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 180   |    8075|     630.775|   0.2%/319|   0.2%/303|   0.2%/300|   0.2%/296 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 180   |    7058|     706.770|   0.1%/503|   0.1%/516|   0.1%/519|   0.1%/523 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 180   |    7006|     659.838|   0.7%/104|   0.6%/115|   0.6%/118|   0.6%/121 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 180   |  205429|     623.373|   0.4%/179|   0.4%/185|   0.4%/187|   0.4%/188 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 180   |  142470|     673.898|   0.5%/131|   0.5%/138|   0.5%/140|   0.5%/142 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 180   |   95523|      70.174|   1.3%/ 53|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 180   |   77035|     608.602|   0.6%/122|   0.5%/132|   0.5%/134|   0.5%/137 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 180   |   41999|     632.176|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/978 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 180   |   35797|     594.248|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 180   |   32300|    1005.234|   0.4%/190|   0.3%/209|   0.3%/214|   0.3%/219 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 180   |   31509|     469.756|   0.2%/405|   0.2%/352|   0.2%/341|   0.2%/330 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 180   |   31163|     661.622|   0.2%/344|   0.2%/329|   0.2%/325|   0.2%/322 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 180   |   25390|     304.520|   0.7%/100|   0.7%/ 96|   0.7%/ 95|   0.7%/ 94 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 180   |    2540|     518.129|   0.4%/161|   0.4%/193|   0.3%/202|   0.3%/213 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 180   |      50|      68.059|   0.4%/197|   0.2%/365|   0.1%/466|   0.1%/642 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 180   |    5641|     774.970|   0.4%/185|   0.3%/200|   0.3%/204|   0.3%/208 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 180   |    1326|     439.538|   1.1%/ 61|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 180   |   15773|     399.185|   0.6%/116|   0.5%/126|   0.5%/129|   0.5%/131 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 180   |    2042|     354.545|   0.2%/386|   0.2%/386|   0.2%/385|   0.2%/385 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 180   |    4502|    1262.676|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 180   |     631|     648.054|   0.2%/335|   0.2%/302|   0.2%/295|   0.2%/288 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 180   |   14143|     658.500|   0.8%/ 87|   0.8%/ 90|   0.8%/ 91|   0.8%/ 92 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 180   |    7006|     659.838|   0.7%/104|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 180   |     140|      98.940|   1.7%/ 40|   1.4%/ 49|   1.3%/ 53|   1.2%/ 56 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 180   |     475|     265.781|   0.7%/100|   0.6%/124|   0.5%/132|   0.5%/141 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 180   |    8842|     697.757|   0.3%/263|   0.3%/260|   0.3%/259|   0.3%/258 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 180   |    3583|     532.185|   0.3%/229|   0.3%/230|   0.3%/230|   0.3%/230 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 180   |    1332|     422.317|   0.5%/128|   0.5%/140|   0.5%/143|   0.5%/147 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 180   |     647|     222.084|   1.2%/ 57|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 180   |    1172|     262.385|   0.7%/101|   0.6%/108|   0.6%/110|   0.6%/113 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 180   |    5505|    1184.106|   0.3%/223|   0.3%/255|   0.3%/264|   0.3%/274 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 180   |     141|     104.771|   0.2%/335|   0.2%/344|   0.2%/347|   0.2%/351 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 180   |    3930|     650.036|   0.2%/409|   0.2%/413|   0.2%/414|   0.2%/414 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 180   |    9397|    1352.138|   0.1%/472|   0.1%/465|   0.1%/463|   0.2%/461 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 180   |    7058|     706.770|   0.1%/503|   0.1%/516|   0.1%/519|   0.1%/523 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 180   |    2066|     366.414|   0.3%/200|   0.3%/205|   0.3%/206|   0.3%/208 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 180   |    2949|     990.895|   0.6%/125|   0.5%/139|   0.5%/143|   0.5%/146 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 180   |    1984|     323.277|   1.2%/ 59|   1.3%/ 54|   1.3%/ 52|   1.4%/ 51 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 180   |     176|     164.642|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 180   |     471|     243.576|   0.6%/110|   0.6%/107|   0.7%/106|   0.7%/105 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 180   |    1609|     522.441|   0.6%/117|   0.5%/135|   0.5%/140|   0.5%/145 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 180   |     440|     323.379|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 180   |   16107|    1813.455|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 180   |     873|     416.448|   0.4%/177|   0.4%/185|   0.4%/187|   0.4%/189 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 180   |   33127|    1702.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 180   |    3454|     329.349|   0.9%/ 78|   0.9%/ 79|   0.9%/ 79|   0.9%/ 79 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 180   |     210|     276.030|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 25 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 180   |    4780|     408.970|   0.5%/143|   0.5%/146|   0.5%/148|   0.5%/149 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 180   |    1010|     255.125|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 90 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 180   |     554|     131.316|   0.5%/135|   0.4%/163|   0.4%/172|   0.4%/182 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 180   |    8075|     630.775|   0.2%/319|   0.2%/303|   0.2%/300|   0.2%/296 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 180   |     665|     208.162|   1.3%/ 53|   1.2%/ 57|   1.2%/ 59|   1.2%/ 60 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 180   |    1108|    1045.900|   0.2%/295|   0.2%/281|   0.2%/277|   0.3%/274 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 180   |    3382|     656.931|   0.6%/111|   0.5%/128|   0.5%/133|   0.5%/138 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 180   |     213|     240.682|   1.3%/ 52|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 180   |    2414|     353.256|   1.1%/ 65|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 180   |   15968|     550.703|   0.6%/107|   0.6%/122|   0.5%/126|   0.5%/130 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 180   |  205429|     623.373|   0.4%/179|   0.4%/185|   0.4%/187|   0.4%/188 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 180   |     453|     141.327|   0.3%/238|   0.2%/281|   0.2%/294|   0.2%/308 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 180   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 180   |    3147|     368.675|   0.8%/ 89|   0.8%/ 83|   0.8%/ 82|   0.9%/ 80 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 180   |    2101|     275.855|   0.4%/190|   0.4%/187|   0.4%/186|   0.4%/185 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 180   |     349|     194.738|   1.5%/ 46|   1.4%/ 49|   1.4%/ 50|   1.4%/ 51 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 180   |    1287|     221.117|   0.5%/153|   0.4%/159|   0.4%/161|   0.4%/163 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 168   |      52|      89.108|   0.1%/486|   0.2%/433|   0.2%/419|   0.2%/406 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 180   |    1453|      45.099|   0.1%/501|   0.1%/485|   0.1%/481|   0.1%/477 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 180   |     388|     136.254|   0.8%/ 84|   0.7%/101|   0.7%/106|   0.6%/112 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 180   |    1731|      40.266|   0.4%/160|   0.4%/172|   0.4%/176|   0.4%/179 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 180   |     171|       5.480|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 180   |   15601|     347.161|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 180   |     953|     322.251|   0.3%/255|   0.3%/271|   0.3%/275|   0.2%/279 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 180   |     939|      36.570|   0.5%/153|   0.1%/485|   0.1%/ ***|   0.0%/ -- |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 180   |     777|      87.286|   0.3%/224|   0.4%/193|   0.4%/187|   0.4%/181 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 180   |     589|      58.534|   0.3%/223|   0.3%/241|   0.3%/246|   0.3%/252 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 180   |     237|     153.708|   1.0%/ 69|   1.1%/ 63|   1.1%/ 62|   1.1%/ 61 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 180   |    5205|      30.894|   0.6%/112|   0.6%/122|   0.6%/125|   0.5%/128 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 180   |     821|      87.244|   0.7%/106|   0.6%/109|   0.6%/110|   0.6%/110 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 180   |    9970|     865.149|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 175   |      40|       3.413|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 180   |    8420|     734.115|   0.5%/143|   0.3%/207|   0.3%/232|   0.3%/265 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 180   |     828|     250.951|   1.1%/ 64|   1.0%/ 67|   1.0%/ 67|   1.0%/ 68 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 180   |      18|       7.795|   3.4%/ 20|   2.7%/ 26|   2.5%/ 27|   2.3%/ 30 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 180   |  142470|     673.898|   0.5%/131|   0.5%/138|   0.5%/140|   0.5%/142 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 180   |     814|     117.141|   0.7%/101|   0.6%/124|   0.5%/132|   0.5%/141 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 180   |      56|       2.696|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 168   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 180   |     418|      15.741|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 180   |    9309|     244.988|   0.1%/ ***|   0.1%/977|   0.1%/962|   0.1%/948 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 128   |      62|      11.282|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 153   |      83|       5.114|   0.2%/278|   0.3%/226|   0.3%/216|   0.3%/206 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 180   |   12642|     661.632|   0.4%/169|   0.4%/173|   0.4%/174|   0.4%/175 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 180   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 180   |   26006|     526.473|   0.8%/ 90|   0.6%/109|   0.6%/115|   0.6%/121 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 180   |     854|     168.859|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 180   |     273|      66.855|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 180   |     121|      10.810|   0.8%/ 83|   0.9%/ 80|   0.9%/ 80|   0.9%/ 79 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 180   |     644|     110.515|   0.2%/355|   0.2%/305|   0.2%/294|   0.2%/284 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 180   |    2173|     209.830|   0.5%/139|   0.4%/196|   0.3%/220|   0.3%/249 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 180   |    7421|     424.839|   0.3%/248|   0.2%/292|   0.2%/305|   0.2%/320 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 180   |    5894|      58.784|   0.3%/235|   0.3%/242|   0.3%/244|   0.3%/246 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 180   |     843|     129.944|   0.4%/187|   0.3%/258|   0.2%/285|   0.2%/317 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 159   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 176   |    1215|      12.315|   1.1%/ 66|   0.8%/ 82|   0.8%/ 87|   0.7%/ 93 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 180   |     342|      61.910|   0.1%/649|   0.1%/569|   0.1%/551|   0.1%/534 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 180   |   31509|     469.756|   0.2%/405|   0.2%/352|   0.2%/341|   0.2%/330 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 180   |      54|      24.733|   0.1%/594|   0.1%/476|   0.2%/453|   0.2%/432 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 180   |     112|      47.710|   0.4%/183|   0.3%/259|   0.2%/288|   0.2%/323 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 177   |      19|       5.195|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 180   |    9437|     113.493|   0.1%/882|   0.1%/781|   0.1%/758|   0.1%/736 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 180   |     303|      10.008|   0.2%/306|   0.2%/412|   0.2%/451|   0.1%/499 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 180   |     371|      34.635|   1.5%/ 46|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 180   |    3233|     194.693|   0.6%/122|   0.6%/126|   0.5%/126|   0.5%/127 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 166   |      66|       5.390|   0.3%/270|   0.2%/366|   0.2%/398|   0.2%/435 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 155   |      40|      24.889|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 176   |     229|      19.787|   0.3%/210|   0.3%/239|   0.3%/247|   0.3%/256 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 180   |    2307|     251.950|   0.7%/105|   0.6%/117|   0.6%/120|   0.6%/123 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 180   |     656|      67.121|   0.9%/ 74|   1.1%/ 62|   1.2%/ 60|   1.2%/ 58 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 180   |   95523|      70.174|   1.3%/ 53|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 180   |   10457|      39.178|   1.2%/ 55|   1.2%/ 56|   1.2%/ 56|   1.2%/ 56 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 180   |   25390|     304.520|   0.7%/100|   0.7%/ 96|   0.7%/ 95|   0.7%/ 94 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 180   |    9108|     232.781|   0.8%/ 85|   0.8%/ 91|   0.7%/ 93|   0.7%/ 95 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 180   |    1798|     365.247|   0.1%/965|   0.1%/824|   0.1%/795|   0.1%/768 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 180   |    1403|     152.703|   1.8%/ 38|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 180   |   35797|     594.248|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 180   |      89|      32.751|   5.3%/ 13|   5.4%/ 13|   5.4%/ 13|   5.4%/ 13 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 180   |    1586|      12.593|   0.5%/135|   0.4%/168|   0.4%/179|   0.4%/191 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 180   |      39|       3.636|   4.9%/ 14|   5.4%/ 13|   5.6%/ 12|   5.7%/ 12 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 180   |    1726|      92.394|   0.2%/301|   0.2%/451|   0.1%/515|   0.1%/598 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 180   |     684|      14.375|   0.7%/ 93|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 180   |     490|     273.099|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 177   |     601|     135.899|   0.5%/147|   0.5%/145|   0.5%/144|   0.5%/144 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 178   |    1063|     162.659|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 178   |      36|      19.062|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 180   |     360|      52.692|   2.7%/ 26|   2.5%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 177   |      82|      18.323|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 179   |     534|      77.672|   2.5%/ 27|   2.4%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 180   |      88|      31.620|   0.2%/283|   0.3%/239|   0.3%/229|   0.3%/220 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 134   |     232|       8.819|   0.6%/117|   0.5%/129|   0.5%/133|   0.5%/136 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 180   |     132|       4.028|   0.1%/782|   0.1%/649|   0.1%/621|   0.1%/594 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 180   |     130|       6.410|   0.1%/544|   0.1%/509|   0.1%/500|   0.1%/492 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 180   |     162|      39.638|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 180   |   77035|     608.602|   0.6%/122|   0.5%/132|   0.5%/134|   0.5%/137 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 180   |    1284|     478.903|   0.9%/ 73|   1.0%/ 72|   1.0%/ 71|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 180   |    2138|      59.589|   1.9%/ 36|   1.7%/ 41|   1.7%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 126   |      56|       1.858|   3.8%/ 18|   4.1%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  80   |     122|      49.637|   1.3%/ 53|   1.0%/ 72|   0.9%/ 78|   0.8%/ 87 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 135   |     487|      16.234|   2.3%/ 30|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 180   |    6351|     363.828|   0.1%/872|   0.1%/788|   0.1%/768|   0.1%/748 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 180   |      25|       5.121|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 180   |     151|      23.298|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 180   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 180   |    1120|       5.433|   0.2%/356|   0.1%/471|   0.1%/514|   0.1%/567 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 180   |     727|     349.843|   0.8%/ 90|   0.8%/ 88|   0.8%/ 87|   0.8%/ 86 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 180   |     269|      50.025|   0.1%/538|   0.2%/444|   0.2%/425|   0.2%/407 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 180   |     907|     194.382|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 180   |    6466|      29.480|   0.1%/805|   0.1%/852|   0.1%/864|   0.1%/875 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 180   |    2347|     556.328|   0.5%/131|   0.5%/139|   0.5%/141|   0.5%/142 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  63   |       7|       0.808|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 180   |     842|     117.741|   2.9%/ 24|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 180   |   32300|    1005.234|   0.4%/190|   0.3%/209|   0.3%/214|   0.3%/219 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 180   |    5498|      50.662|   1.2%/ 56|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 180   |    2396|      62.441|   0.7%/ 96|   0.8%/ 90|   0.8%/ 89|   0.8%/ 87 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 180   |    1940|     188.818|   0.3%/231|   0.3%/211|   0.3%/207|   0.3%/202 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 180   |     214|      78.024|   0.3%/263|   0.3%/275|   0.2%/278|   0.2%/281 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 180   |    4756|     245.099|   0.9%/ 77|   0.8%/ 82|   0.8%/ 83|   0.8%/ 85 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 180   |   20196|     137.625|   0.6%/109|   0.6%/108|   0.6%/107|   0.6%/107 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 121   |      30|       2.390|   2.2%/ 32|   2.3%/ 30|   2.3%/ 29|   2.4%/ 29 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 180   |    4705|     137.492|   0.6%/108|   0.6%/113|   0.6%/114|   0.6%/115 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 180   |     309|      19.036|   0.2%/311|   0.2%/399|   0.2%/428|   0.2%/461 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 180   |     750|     107.740|   0.1%/520|   0.1%/634|   0.1%/670|   0.1%/710 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 158   |      72|       9.159|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 180   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 180   |      41|       7.586|   0.9%/ 79|   1.0%/ 67|   1.1%/ 65|   1.1%/ 62 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 180   |     144|      68.946|   0.3%/218|   0.4%/184|   0.4%/177|   0.4%/170 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 173   |      99|       6.210|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 180   |   16663|     283.511|   0.4%/169|   0.3%/219|   0.3%/235|   0.3%/255 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 180   |   31163|     661.622|   0.2%/344|   0.2%/329|   0.2%/325|   0.2%/322 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 180   |      13|       0.605|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 180   |     840|      19.787|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 180   |    5882|     568.915|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 180   |    2063|     239.733|   0.1%/632|   0.1%/567|   0.1%/553|   0.1%/539 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 180   |     200|      11.412|   1.5%/ 45|   1.3%/ 53|   1.2%/ 56|   1.2%/ 59 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 180   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 180   |      59|       0.889|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 180   |      47|       6.170|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 180   |      86|      63.297|   2.8%/ 24|   1.9%/ 36|   1.7%/ 41|   1.5%/ 48 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 180   |     148|      12.585|   5.2%/ 13|   5.8%/ 12|   6.0%/ 11|   6.1%/ 11 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 180   |    7949|      95.589|   0.9%/ 76|   1.0%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 180   |  205429|     623.373|   0.4%/179|   0.4%/185|   0.4%/187|   0.4%/188 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  66   |      73|       1.815|   2.1%/ 34|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 180   |    4047|      96.634|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 180   |     412|      41.682|   0.2%/289|   0.2%/306|   0.2%/310|   0.2%/314 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 180   |   41999|     632.176|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/978 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 180   |      47|      13.367|   0.2%/287|   0.2%/308|   0.2%/311|   0.2%/315 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 180   |     473|      13.850|   1.2%/ 60|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 180   |     615|      19.099|   1.6%/ 42|   1.6%/ 44|   1.6%/ 45|   1.5%/ 45 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  59   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 179   |     341|      19.039|   0.2%/280|   0.2%/359|   0.2%/388|   0.2%/422 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 180   |     237|      15.663|   0.1%/674|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

