# State and Country COVID-19 Analysis #
## Updated: at 2020-09-30 for data as of 2020-09-29 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 65.8% of deaths and 55.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 182   |   33141|    1703.586|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 182   |   16118|    1814.697|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 182   |   16120|     555.941|   0.6%/115|   0.5%/133|   0.5%/138|   0.5%/143 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 182   |   15919|     402.878|   0.5%/126|   0.5%/140|   0.5%/144|   0.5%/148 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 182   |   14317|     666.587|   0.7%/ 98|   0.7%/105|   0.6%/108|   0.6%/110 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 182   |    9424|    1356.082|   0.1%/476|   0.1%/470|   0.1%/469|   0.1%/467 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 182   |    8885|     701.199|   0.3%/276|   0.3%/276|   0.3%/277|   0.3%/277 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 182   |    8107|     633.249|   0.2%/348|   0.2%/341|   0.2%/339|   0.2%/338 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 182   |    7077|     708.649|   0.1%/515|   0.1%/530|   0.1%/533|   0.1%/537 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 182   |    7075|     666.389|   0.6%/113|   0.5%/127|   0.5%/131|   0.5%/135 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 182   |  206765|     627.427|   0.4%/193|   0.3%/204|   0.3%/206|   0.3%/209 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 182   |  143728|     679.849|   0.5%/139|   0.5%/149|   0.5%/152|   0.4%/154 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 182   |   99128|      72.823|   1.3%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 182   |   77734|     614.118|   0.5%/132|   0.5%/144|   0.5%/147|   0.5%/151 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 182   |   42062|     633.132|   0.1%/ ***|   0.1%/989|   0.1%/958|   0.1%/929 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 182   |   35835|     594.889|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 182   |   32496|    1011.346|   0.3%/202|   0.3%/223|   0.3%/229|   0.3%/236 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 182   |   31652|     471.886|   0.2%/379|   0.2%/332|   0.2%/322|   0.2%/312 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 182   |   31386|     666.364|   0.2%/362|   0.2%/351|   0.2%/349|   0.2%/346 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 182   |   25780|     309.201|   0.7%/ 98|   0.7%/ 93|   0.8%/ 92|   0.8%/ 91 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 182   |    2553|     520.686|   0.4%/186|   0.3%/235|   0.3%/251|   0.3%/270 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 182   |      52|      71.181|   0.3%/219|   0.2%/414|   0.1%/531|   0.1%/739 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 182   |    5671|     779.111|   0.3%/207|   0.3%/229|   0.3%/235|   0.3%/242 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 182   |    1370|     454.086|   1.2%/ 57|   1.1%/ 60|   1.1%/ 61|   1.1%/ 62 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 182   |   15919|     402.878|   0.5%/126|   0.5%/140|   0.5%/144|   0.5%/148 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 182   |    2049|     355.720|   0.2%/404|   0.2%/409|   0.2%/410|   0.2%/412 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 182   |    4505|    1263.556|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 182   |     634|     650.983|   0.2%/346|   0.2%/320|   0.2%/314|   0.2%/308 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 182   |   14317|     666.587|   0.7%/ 98|   0.7%/105|   0.6%/108|   0.6%/110 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 182   |    7075|     666.389|   0.6%/113|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 182   |     143|     101.122|   1.5%/ 45|   1.2%/ 58|   1.1%/ 63|   1.0%/ 68 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 182   |     478|     267.592|   0.6%/116|   0.5%/153|   0.4%/166|   0.4%/182 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 182   |    8885|     701.199|   0.3%/276|   0.3%/276|   0.3%/277|   0.3%/277 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 182   |    3605|     535.429|   0.3%/232|   0.3%/233|   0.3%/233|   0.3%/233 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 182   |    1345|     426.313|   0.5%/132|   0.5%/144|   0.5%/147|   0.5%/151 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 182   |     662|     227.306|   1.1%/ 63|   1.1%/ 65|   1.1%/ 65|   1.1%/ 66 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 182   |    1185|     265.204|   0.6%/110|   0.6%/121|   0.6%/124|   0.5%/128 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 182   |    5531|    1189.679|   0.3%/234|   0.3%/268|   0.2%/277|   0.2%/288 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 182   |     141|     105.142|   0.2%/359|   0.2%/379|   0.2%/386|   0.2%/393 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 182   |    3943|     652.220|   0.2%/404|   0.2%/404|   0.2%/404|   0.2%/403 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 182   |    9424|    1356.082|   0.1%/476|   0.1%/470|   0.1%/469|   0.1%/467 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 182   |    7077|     708.649|   0.1%/515|   0.1%/530|   0.1%/533|   0.1%/537 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 182   |    2080|     368.770|   0.3%/205|   0.3%/211|   0.3%/213|   0.3%/215 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 182   |    2974|     999.286|   0.5%/132|   0.5%/146|   0.5%/150|   0.4%/155 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 182   |    2039|     332.301|   1.1%/ 62|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 182   |     182|     169.945|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 182   |     477|     246.723|   0.6%/114|   0.6%/113|   0.6%/112|   0.6%/112 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 182   |    1622|     526.444|   0.5%/132|   0.4%/158|   0.4%/166|   0.4%/175 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 182   |     440|     323.607|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 182   |   16118|    1814.697|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 182   |     879|     419.198|   0.4%/189|   0.3%/201|   0.3%/204|   0.3%/207 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 182   |   33141|    1703.586|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 182   |    3507|     334.335|   0.8%/ 86|   0.8%/ 89|   0.8%/ 89|   0.8%/ 90 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 182   |     225|     294.706|   2.3%/ 31|   2.5%/ 27|   2.6%/ 27|   2.7%/ 26 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 182   |    4819|     412.240|   0.4%/161|   0.4%/173|   0.4%/176|   0.4%/180 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 182   |    1023|     258.524|   0.8%/ 92|   0.7%/ 97|   0.7%/ 99|   0.7%/100 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 182   |     558|     132.375|   0.5%/138|   0.4%/163|   0.4%/171|   0.4%/179 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 182   |    8107|     633.249|   0.2%/348|   0.2%/341|   0.2%/339|   0.2%/338 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 182   |     679|     212.486|   1.2%/ 60|   1.0%/ 68|   1.0%/ 70|   1.0%/ 72 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 182   |    1113|    1050.740|   0.2%/315|   0.2%/306|   0.2%/305|   0.2%/303 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 182   |    3412|     662.647|   0.6%/122|   0.5%/143|   0.5%/150|   0.4%/157 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 182   |     219|     247.491|   1.2%/ 57|   1.3%/ 52|   1.4%/ 51|   1.4%/ 50 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 182   |    2456|     359.475|   1.0%/ 70|   0.9%/ 75|   0.9%/ 77|   0.9%/ 78 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 182   |   16120|     555.941|   0.6%/115|   0.5%/133|   0.5%/138|   0.5%/143 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 182   |  206765|     627.427|   0.4%/193|   0.3%/204|   0.3%/206|   0.3%/209 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 182   |     456|     142.145|   0.3%/213|   0.3%/230|   0.3%/234|   0.3%/237 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 182   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 182   |    3198|     374.667|   0.7%/ 97|   0.7%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 182   |    2115|     277.781|   0.3%/201|   0.3%/200|   0.3%/200|   0.3%/200 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 182   |     357|     199.398|   1.4%/ 50|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 182   |    1298|     222.940|   0.4%/159|   0.4%/167|   0.4%/170|   0.4%/172 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 170   |      52|      89.978|   0.1%/591|   0.1%/549|   0.1%/536|   0.1%/524 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 182   |    1457|      45.226|   0.1%/514|   0.1%/503|   0.1%/501|   0.1%/498 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 182   |     392|     137.851|   0.8%/ 89|   0.6%/107|   0.6%/113|   0.6%/119 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 182   |    1744|      40.553|   0.4%/175|   0.4%/194|   0.3%/199|   0.3%/205 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 182   |     177|       5.695|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   2.0%/ 35 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 182   |   16336|     363.520|   2.3%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 182   |     958|     324.068|   0.3%/244|   0.3%/251|   0.3%/253|   0.3%/255 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 182   |     934|      36.374|   0.4%/169|   0.1%/463|   0.1%/794|   0.0%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 182   |     788|      88.501|   0.3%/222|   0.4%/195|   0.4%/189|   0.4%/184 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 182   |     592|      58.845|   0.3%/232|   0.3%/252|   0.3%/257|   0.3%/263 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 182   |     243|     157.320|   1.0%/ 66|   1.1%/ 61|   1.1%/ 60|   1.2%/ 59 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 182   |    5261|      31.226|   0.6%/113|   0.6%/122|   0.6%/125|   0.5%/128 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 182   |     831|      88.296|   0.6%/107|   0.6%/111|   0.6%/112|   0.6%/113 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 182   |    9981|     866.078|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 177   |      40|       3.412|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 182   |    8502|     741.206|   0.4%/155|   0.3%/222|   0.3%/248|   0.2%/280 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 182   |     845|     256.024|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 182   |      19|       7.990|   2.6%/ 27|   1.7%/ 40|   1.5%/ 46|   1.3%/ 54 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 182   |  143728|     679.849|   0.5%/139|   0.5%/149|   0.5%/152|   0.4%/154 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 182   |     823|     118.408|   0.7%/100|   0.6%/118|   0.6%/123|   0.5%/129 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 182   |      56|       2.703|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 170   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 182   |     418|      15.750|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 182   |    9325|     245.392|   0.1%/962|   0.1%/897|   0.1%/881|   0.1%/866 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 130   |      62|      11.281|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 155   |      84|       5.168|   0.4%/161|   0.5%/131|   0.6%/125|   0.6%/119 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 182   |   12742|     666.861|   0.4%/170|   0.4%/173|   0.4%/173|   0.4%/174 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 182   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 182   |   26290|     532.230|   0.7%/ 94|   0.6%/112|   0.6%/117|   0.6%/123 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 182   |     895|     176.854|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 182   |     280|      68.629|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 182   |     123|      10.976|   0.8%/ 83|   0.9%/ 81|   0.9%/ 81|   0.9%/ 80 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 182   |     647|     111.173|   0.2%/366|   0.2%/320|   0.2%/310|   0.2%/301 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 182   |    2180|     210.503|   0.4%/171|   0.2%/279|   0.2%/332|   0.2%/410 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 182   |    7464|     427.289|   0.2%/283|   0.2%/349|   0.2%/372|   0.2%/397 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 182   |    5927|      59.105|   0.3%/241|   0.3%/249|   0.3%/251|   0.3%/253 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 182   |     847|     130.561|   0.4%/198|   0.3%/265|   0.2%/289|   0.2%/318 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 161   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 178   |    1231|      12.474|   1.0%/ 72|   0.8%/ 92|   0.7%/ 98|   0.7%/106 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 182   |     343|      62.135|   0.1%/539|   0.1%/467|   0.2%/452|   0.2%/437 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 182   |   31652|     471.886|   0.2%/379|   0.2%/332|   0.2%/322|   0.2%/312 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 182   |      54|      24.803|   0.1%/667|   0.1%/553|   0.1%/530|   0.1%/509 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 182   |     113|      48.097|   0.4%/165|   0.3%/199|   0.3%/210|   0.3%/222 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 179   |      19|       5.187|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 182   |    9457|     113.732|   0.1%/867|   0.1%/773|   0.1%/752|   0.1%/732 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 182   |     304|      10.033|   0.2%/342|   0.1%/474|   0.1%/526|   0.1%/590 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 182   |     384|      35.801|   1.5%/ 47|   1.5%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 182   |    3264|     196.585|   0.5%/128|   0.5%/133|   0.5%/134|   0.5%/135 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 168   |      66|       5.419|   0.3%/235|   0.3%/270|   0.2%/278|   0.2%/287 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 157   |      40|      24.788|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 178   |     230|      19.849|   0.3%/268|   0.2%/344|   0.2%/369|   0.2%/399 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 182   |    2332|     254.621|   0.6%/112|   0.6%/124|   0.5%/127|   0.5%/130 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 182   |     662|      67.735|   1.0%/ 66|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 182   |   99128|      72.823|   1.3%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 182   |   10695|      40.071|   1.2%/ 58|   1.2%/ 60|   1.2%/ 60|   1.1%/ 61 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 182   |   25780|     309.201|   0.7%/ 98|   0.7%/ 93|   0.8%/ 92|   0.8%/ 91 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 182   |    9234|     236.001|   0.8%/ 88|   0.7%/ 95|   0.7%/ 97|   0.7%/100 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 182   |    1801|     365.863|   0.1%/961|   0.1%/840|   0.1%/815|   0.1%/791 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 182   |    1472|     160.184|   1.9%/ 36|   2.1%/ 34|   2.1%/ 33|   2.1%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 182   |   35835|     594.889|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 182   |      99|      36.255|   5.2%/ 13|   5.3%/ 13|   5.3%/ 13|   5.3%/ 13 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 182   |    1596|      12.672|   0.5%/146|   0.4%/184|   0.4%/197|   0.3%/212 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 182   |      42|       3.928|   5.8%/ 12|   6.5%/ 10|   6.7%/ 10|   6.9%/ 10 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 182   |    1731|      92.622|   0.2%/311|   0.2%/440|   0.1%/490|   0.1%/551 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 182   |     696|      14.630|   0.8%/ 88|   0.8%/ 83|   0.9%/ 81|   0.9%/ 80 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 182   |     489|     272.297|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 179   |     607|     137.276|   0.5%/142|   0.5%/139|   0.5%/139|   0.5%/138 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 180   |    1064|     162.824|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 180   |      37|      19.147|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 182   |     376|      55.097|   2.5%/ 28|   2.3%/ 30|   2.3%/ 30|   2.3%/ 31 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 179   |      82|      18.323|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 181   |     559|      81.367|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 182   |      89|      31.817|   0.4%/168|   0.5%/137|   0.5%/130|   0.6%/124 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 136   |     233|       8.876|   0.5%/142|   0.4%/176|   0.4%/188|   0.3%/202 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 182   |     133|       4.062|   0.1%/495|   0.2%/405|   0.2%/387|   0.2%/370 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 182   |     130|       6.431|   0.1%/540|   0.1%/506|   0.1%/498|   0.1%/490 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 182   |     162|      39.618|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 182   |   77734|     614.118|   0.5%/132|   0.5%/144|   0.5%/147|   0.5%/151 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 182   |    1309|     488.106|   0.9%/ 74|   1.0%/ 73|   1.0%/ 73|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 182   |    2203|      61.413|   1.9%/ 37|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 128   |      60|       1.997|   3.7%/ 18|   3.9%/ 18|   4.0%/ 17|   4.0%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  82   |     123|      50.088|   1.1%/ 63|   0.7%/ 99|   0.6%/116|   0.5%/142 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 137   |     504|      16.816|   2.1%/ 32|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 182   |    6359|     364.290|   0.1%/657|   0.1%/573|   0.1%/554|   0.1%/536 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 182   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 182   |     151|      23.375|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 182   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 182   |    1122|       5.444|   0.2%/385|   0.1%/519|   0.1%/570|   0.1%/632 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 182   |     738|     355.082|   0.7%/ 94|   0.7%/ 93|   0.7%/ 93|   0.7%/ 93 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 182   |     269|      50.197|   0.2%/335|   0.3%/272|   0.3%/260|   0.3%/248 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 182   |     928|     199.027|   1.1%/ 61|   1.2%/ 60|   1.2%/ 60|   1.2%/ 59 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 182   |    6477|      29.532|   0.1%/764|   0.1%/782|   0.1%/785|   0.1%/788 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 182   |    2370|     561.828|   0.5%/130|   0.5%/136|   0.5%/137|   0.5%/139 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  65   |       7|       0.800|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 182   |     881|     123.130|   2.8%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 182   |   32496|    1011.346|   0.3%/202|   0.3%/223|   0.3%/229|   0.3%/236 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 182   |    5620|      51.789|   1.2%/ 58|   1.1%/ 63|   1.1%/ 65|   1.0%/ 66 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 182   |    2437|      63.504|   0.7%/ 93|   0.8%/ 87|   0.8%/ 85|   0.8%/ 84 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 182   |    1954|     190.169|   0.3%/221|   0.3%/203|   0.3%/198|   0.4%/195 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 182   |     215|      78.332|   0.2%/290|   0.2%/314|   0.2%/320|   0.2%/327 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 182   |    4831|     248.934|   0.9%/ 80|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 182   |   20445|     139.325|   0.6%/112|   0.6%/111|   0.6%/111|   0.6%/111 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 123   |      30|       2.447|   1.3%/ 55|   1.1%/ 62|   1.1%/ 64|   1.1%/ 66 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 182   |    4761|     139.132|   0.6%/109|   0.6%/113|   0.6%/115|   0.6%/116 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 182   |     310|      19.123|   0.3%/263|   0.2%/290|   0.2%/297|   0.2%/304 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 182   |     752|     107.946|   0.1%/543|   0.1%/652|   0.1%/686|   0.1%/724 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 160   |      72|       9.152|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 182   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 182   |      42|       7.723|   0.9%/ 81|   1.0%/ 69|   1.0%/ 67|   1.1%/ 65 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 182   |     146|      69.938|   0.4%/161|   0.5%/134|   0.5%/129|   0.6%/124 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 175   |      99|       6.218|   0.1%/879|   0.1%/840|   0.1%/824|   0.1%/807 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 182   |   16779|     285.485|   0.4%/164|   0.4%/197|   0.3%/207|   0.3%/218 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 182   |   31386|     666.364|   0.2%/362|   0.2%/351|   0.2%/349|   0.2%/346 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 182   |      13|       0.607|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 182   |     839|      19.777|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 182   |    5886|     569.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 182   |    2068|     240.345|   0.1%/699|   0.1%/646|   0.1%/634|   0.1%/623 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 182   |     204|      11.669|   1.5%/ 46|   1.3%/ 54|   1.2%/ 57|   1.2%/ 59 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 182   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 182   |      59|       0.889|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 182   |      48|       6.371|   1.6%/ 44|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 182   |      88|      64.438|   2.3%/ 30|   1.4%/ 51|   1.1%/ 62|   0.9%/ 79 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 182   |     213|      18.207|   5.5%/ 12|   6.1%/ 11|   6.3%/ 11|   6.4%/ 11 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 182   |    8117|      97.608|   0.9%/ 77|   0.9%/ 74|   0.9%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 182   |  206765|     627.427|   0.4%/193|   0.3%/204|   0.3%/206|   0.3%/209 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  68   |      76|       1.885|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 182   |    4172|      99.607|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 182   |     414|      41.905|   0.3%/267|   0.3%/271|   0.3%/271|   0.3%/272 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 182   |   42062|     633.132|   0.1%/ ***|   0.1%/989|   0.1%/958|   0.1%/929 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 182   |      47|      13.448|   0.3%/258|   0.3%/257|   0.3%/256|   0.3%/254 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 182   |     481|      14.084|   1.1%/ 63|   0.9%/ 73|   0.9%/ 76|   0.9%/ 79 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 182   |     633|      19.649|   1.6%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  61   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 181   |     342|      19.119|   0.2%/365|   0.1%/557|   0.1%/645|   0.1%/770 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 182   |     236|      15.553|   0.1%/645|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

