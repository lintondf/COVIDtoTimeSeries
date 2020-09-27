# State and Country COVID-19 Analysis #
## Updated: at 2020-09-27 for data as of 2020-09-26 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.4% of deaths and 38.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 65.9% of deaths and 55.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 179   |   33120|    1702.511|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 179   |   16102|    1812.841|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 179   |   15874|     547.474|   0.7%/104|   0.6%/118|   0.6%/122|   0.5%/127 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 179   |   15688|     397.050|   0.6%/113|   0.6%/122|   0.6%/124|   0.5%/127 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 179   |   14040|     653.715|   0.8%/ 84|   0.8%/ 87|   0.8%/ 88|   0.8%/ 88 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 179   |    9382|    1350.070|   0.1%/475|   0.1%/469|   0.1%/467|   0.1%/466 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 179   |    8819|     695.958|   0.3%/264|   0.3%/261|   0.3%/260|   0.3%/259 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 179   |    8058|     629.415|   0.2%/311|   0.2%/294|   0.2%/289|   0.2%/285 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 179   |    7049|     705.827|   0.1%/493|   0.1%/505|   0.1%/508|   0.1%/511 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 179   |    6961|     655.594|   0.7%/102|   0.6%/114|   0.6%/118|   0.6%/121 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 179   |  204689|     621.127|   0.4%/176|   0.4%/182|   0.4%/183|   0.4%/184 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 179   |  141758|     670.532|   0.5%/129|   0.5%/136|   0.5%/138|   0.5%/140 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 179   |   94354|      69.316|   1.3%/ 52|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 179   |   76634|     605.429|   0.6%/119|   0.5%/127|   0.5%/129|   0.5%/132 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 179   |   41971|     631.761|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 179   |   35779|     593.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 179   |   32189|    1001.783|   0.4%/185|   0.3%/203|   0.3%/207|   0.3%/212 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 179   |   31431|     468.591|   0.2%/410|   0.2%/354|   0.2%/343|   0.2%/331 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 179   |   31065|     659.546|   0.2%/305|   0.2%/284|   0.2%/279|   0.3%/275 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 179   |   25206|     302.316|   0.7%/102|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 179   |    2531|     516.279|   0.5%/143|   0.4%/163|   0.4%/169|   0.4%/175 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 179   |      49|      66.816|   0.4%/176|   0.2%/290|   0.2%/348|   0.2%/434 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 179   |    5620|     772.127|   0.4%/185|   0.3%/203|   0.3%/207|   0.3%/212 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 179   |    1305|     432.466|   1.1%/ 63|   1.0%/ 72|   0.9%/ 74|   0.9%/ 77 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 179   |   15688|     397.050|   0.6%/113|   0.6%/122|   0.6%/124|   0.5%/127 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 179   |    2038|     353.927|   0.2%/377|   0.2%/374|   0.2%/373|   0.2%/372 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 179   |    4500|    1262.309|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 179   |     630|     646.679|   0.2%/334|   0.2%/299|   0.2%/291|   0.2%/284 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 179   |   14040|     653.715|   0.8%/ 84|   0.8%/ 87|   0.8%/ 88|   0.8%/ 88 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 179   |    6961|     655.594|   0.7%/102|   0.6%/114|   0.6%/118|   0.6%/121 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 179   |     138|      97.296|   1.7%/ 40|   1.4%/ 51|   1.3%/ 55|   1.2%/ 59 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 179   |     472|     264.270|   0.7%/ 92|   0.6%/112|   0.6%/118|   0.6%/125 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 179   |    8819|     695.958|   0.3%/264|   0.3%/261|   0.3%/260|   0.3%/259 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 179   |    3573|     530.658|   0.3%/229|   0.3%/230|   0.3%/230|   0.3%/231 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 179   |    1326|     420.317|   0.6%/122|   0.5%/132|   0.5%/135|   0.5%/138 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 179   |     640|     219.743|   1.3%/ 54|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 179   |    1165|     260.804|   0.7%/ 98|   0.7%/105|   0.6%/107|   0.6%/109 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 179   |    5489|    1180.766|   0.3%/218|   0.3%/249|   0.3%/258|   0.3%/267 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 179   |     141|     104.604|   0.2%/308|   0.2%/307|   0.2%/307|   0.2%/307 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 179   |    3923|     648.837|   0.2%/421|   0.2%/431|   0.2%/433|   0.2%/435 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 179   |    9382|    1350.070|   0.1%/475|   0.1%/469|   0.1%/467|   0.1%/466 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 179   |    7049|     705.827|   0.1%/493|   0.1%/505|   0.1%/508|   0.1%/511 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 179   |    2060|     365.208|   0.3%/198|   0.3%/203|   0.3%/205|   0.3%/206 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 179   |    2934|     985.861|   0.6%/124|   0.5%/138|   0.5%/142|   0.5%/146 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 179   |    1955|     318.572|   1.1%/ 63|   1.2%/ 58|   1.2%/ 57|   1.2%/ 56 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 179   |     173|     161.885|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 179   |     468|     242.091|   0.6%/109|   0.7%/106|   0.7%/105|   0.7%/104 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 179   |    1601|     519.706|   0.6%/113|   0.5%/130|   0.5%/135|   0.5%/140 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 179   |     439|     323.225|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 179   |   16102|    1812.841|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 179   |     870|     414.922|   0.4%/178|   0.4%/187|   0.4%/190|   0.4%/192 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 179   |   33120|    1702.511|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 179   |    3426|     326.670|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 179   |     207|     271.405|   2.1%/ 32|   2.4%/ 29|   2.5%/ 28|   2.5%/ 27 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 179   |    4760|     407.259|   0.5%/134|   0.5%/135|   0.5%/135|   0.5%/135 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 179   |    1002|     253.136|   0.8%/ 86|   0.8%/ 90|   0.8%/ 91|   0.8%/ 92 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 179   |     552|     130.766|   0.5%/127|   0.5%/149|   0.4%/156|   0.4%/164 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 179   |    8058|     629.415|   0.2%/311|   0.2%/294|   0.2%/289|   0.2%/285 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 179   |     657|     205.801|   1.4%/ 51|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 179   |    1106|    1043.749|   0.2%/278|   0.3%/259|   0.3%/254|   0.3%/250 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 179   |    3364|     653.387|   0.6%/108|   0.6%/123|   0.5%/128|   0.5%/133 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 179   |     210|     237.480|   1.3%/ 53|   1.5%/ 47|   1.5%/ 46|   1.6%/ 44 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 179   |    2391|     349.879|   1.1%/ 64|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 179   |   15874|     547.474|   0.7%/104|   0.6%/118|   0.6%/122|   0.5%/127 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 179   |  204689|     621.127|   0.4%/176|   0.4%/182|   0.4%/183|   0.4%/184 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 179   |     452|     140.832|   0.3%/264|   0.2%/343|   0.2%/370|   0.2%/401 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 179   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 179   |    3120|     365.516|   0.8%/ 87|   0.9%/ 80|   0.9%/ 79|   0.9%/ 77 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 179   |    2093|     274.918|   0.4%/189|   0.4%/186|   0.4%/185|   0.4%/184 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 179   |     344|     192.124|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 179   |    1282|     220.221|   0.5%/151|   0.4%/158|   0.4%/159|   0.4%/161 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 167   |      51|      88.560|   0.2%/440|   0.2%/383|   0.2%/370|   0.2%/356 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 179   |    1451|      45.040|   0.1%/478|   0.2%/456|   0.2%/451|   0.2%/445 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 179   |     385|     135.264|   0.9%/ 80|   0.7%/ 96|   0.7%/100|   0.7%/106 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 179   |    1724|      40.102|   0.5%/152|   0.4%/161|   0.4%/164|   0.4%/166 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 179   |     167|       5.374|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 179   |   15242|     339.174|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 179   |     951|     321.388|   0.3%/249|   0.3%/264|   0.3%/268|   0.3%/272 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 179   |     937|      36.478|   0.5%/137|   0.2%/392|   0.1%/716|   0.0%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 179   |     775|      87.007|   0.3%/210|   0.4%/180|   0.4%/173|   0.4%/167 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 179   |     588|      58.372|   0.3%/219|   0.3%/235|   0.3%/240|   0.3%/245 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 179   |     235|     152.025|   0.9%/ 73|   1.0%/ 68|   1.0%/ 67|   1.0%/ 66 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 179   |    5174|      30.709|   0.6%/110|   0.6%/121|   0.6%/123|   0.5%/127 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 179   |     816|      86.695|   0.7%/105|   0.6%/109|   0.6%/109|   0.6%/110 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 179   |    9966|     864.768|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 174   |      40|       3.414|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 179   |    8393|     731.777|   0.5%/136|   0.4%/195|   0.3%/218|   0.3%/247 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 179   |     820|     248.363|   1.1%/ 63|   1.1%/ 65|   1.1%/ 65|   1.1%/ 66 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 179   |      18|       7.604|   3.9%/ 18|   3.3%/ 21|   3.1%/ 22|   3.0%/ 23 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 179   |  141758|     670.532|   0.5%/129|   0.5%/136|   0.5%/138|   0.5%/140 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 179   |     809|     116.430|   0.7%/ 96|   0.6%/117|   0.6%/123|   0.5%/130 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 179   |      56|       2.696|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 167   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 179   |     418|      15.733|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 179   |    9303|     244.811|   0.1%/ ***|   0.1%/ ***|   0.1%/991|   0.1%/978 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 127   |      62|      11.282|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 152   |      83|       5.092|   0.2%/327|   0.3%/270|   0.3%/258|   0.3%/247 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 179   |   12589|     658.885|   0.4%/171|   0.4%/176|   0.4%/177|   0.4%/178 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 179   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 179   |   25822|     522.752|   0.8%/ 88|   0.6%/108|   0.6%/114|   0.6%/120 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 179   |     836|     165.321|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 179   |     269|      65.912|   1.5%/ 46|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 179   |     120|      10.705|   0.8%/ 88|   0.8%/ 86|   0.8%/ 85|   0.8%/ 85 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 179   |     642|     110.275|   0.2%/365|   0.2%/311|   0.2%/300|   0.2%/289 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 179   |    2166|     209.143|   0.5%/128|   0.4%/175|   0.4%/193|   0.3%/215 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 179   |    7388|     422.943|   0.3%/237|   0.3%/275|   0.2%/287|   0.2%/300 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 179   |    5878|      58.618|   0.3%/233|   0.3%/239|   0.3%/241|   0.3%/243 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 179   |     840|     129.583|   0.4%/172|   0.3%/228|   0.3%/248|   0.3%/272 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 158   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 175   |    1204|      12.206|   1.1%/ 62|   0.9%/ 77|   0.9%/ 81|   0.8%/ 87 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 179   |     342|      61.832|   0.1%/596|   0.1%/512|   0.1%/494|   0.1%/477 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 179   |   31431|     468.591|   0.2%/410|   0.2%/354|   0.2%/343|   0.2%/331 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 179   |      54|      24.699|   0.1%/566|   0.2%/449|   0.2%/425|   0.2%/404 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 179   |     111|      47.491|   0.4%/188|   0.2%/296|   0.2%/342|   0.2%/402 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 176   |      19|       5.200|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 179   |    9428|     113.392|   0.1%/926|   0.1%/823|   0.1%/800|   0.1%/777 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 179   |     303|       9.992|   0.2%/280|   0.2%/363|   0.2%/391|   0.2%/424 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 179   |     365|      34.051|   1.5%/ 46|   1.6%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 179   |    3214|     193.556|   0.6%/124|   0.5%/129|   0.5%/130|   0.5%/131 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 165   |      66|       5.375|   0.2%/293|   0.1%/463|   0.1%/535|   0.1%/631 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 154   |      40|      24.963|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 175   |     228|      19.736|   0.4%/187|   0.3%/203|   0.3%/207|   0.3%/212 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 179   |    2293|     250.384|   0.7%/103|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 179   |     655|      66.999|   0.9%/ 78|   1.1%/ 66|   1.1%/ 63|   1.1%/ 61 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 179   |   94354|      69.316|   1.3%/ 52|   1.3%/ 55|   1.2%/ 55|   1.2%/ 56 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 179   |   10335|      38.719|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 179   |   25206|     302.316|   0.7%/102|   0.7%/ 98|   0.7%/ 97|   0.7%/ 96 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 179   |    9040|     231.030|   0.8%/ 83|   0.8%/ 89|   0.8%/ 91|   0.7%/ 93 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 179   |    1796|     364.950|   0.1%/ ***|   0.1%/865|   0.1%/833|   0.1%/804 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 179   |    1375|     149.639|   1.8%/ 39|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 179   |   35779|     593.959|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 179   |      85|      31.185|   5.4%/ 13|   5.5%/ 13|   5.5%/ 12|   5.5%/ 12 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 179   |    1579|      12.541|   0.6%/125|   0.5%/150|   0.4%/158|   0.4%/167 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 179   |      37|       3.510|   4.6%/ 15|   5.0%/ 14|   5.2%/ 13|   5.3%/ 13 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 179   |    1724|      92.248|   0.3%/267|   0.2%/375|   0.2%/416|   0.1%/467 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 179   |     678|      14.260|   0.7%/100|   0.7%/ 97|   0.7%/ 96|   0.7%/ 96 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 179   |     491|     273.204|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 176   |     598|     135.231|   0.5%/149|   0.5%/146|   0.5%/146|   0.5%/145 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 177   |    1061|     162.455|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 177   |      36|      19.049|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 179   |     351|      51.412|   2.8%/ 25|   2.7%/ 26|   2.7%/ 26|   2.6%/ 26 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 176   |      82|      18.323|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 178   |     521|      75.766|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 179   |      88|      31.520|   0.2%/384|   0.2%/338|   0.2%/326|   0.2%/315 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 133   |     231|       8.781|   0.6%/111|   0.6%/119|   0.6%/121|   0.6%/123 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 179   |     131|       4.009|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 179   |     130|       6.401|   0.1%/495|   0.2%/452|   0.2%/442|   0.2%/431 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 179   |     162|      39.640|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 179   |   76634|     605.429|   0.6%/119|   0.5%/127|   0.5%/129|   0.5%/132 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 179   |    1272|     474.450|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 179   |    2099|      58.521|   1.9%/ 36|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 125   |      53|       1.778|   3.7%/ 19|   4.0%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  79   |     121|      49.296|   1.4%/ 48|   1.2%/ 59|   1.1%/ 63|   1.0%/ 66 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 134   |     478|      15.937|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 179   |    6348|     363.608|   0.1%/906|   0.1%/825|   0.1%/805|   0.1%/786 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 179   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 179   |     150|      23.262|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 179   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 179   |    1118|       5.425|   0.2%/340|   0.2%/441|   0.1%/478|   0.1%/523 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 179   |     721|     347.351|   0.8%/ 89|   0.8%/ 86|   0.8%/ 85|   0.8%/ 84 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 179   |     268|      49.943|   0.1%/497|   0.2%/403|   0.2%/384|   0.2%/366 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 179   |     897|     192.239|   1.1%/ 66|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 179   |    6460|      29.453|   0.1%/826|   0.1%/890|   0.1%/907|   0.1%/924 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 179   |    2334|     553.354|   0.5%/133|   0.5%/142|   0.5%/145|   0.5%/147 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  62   |       7|       0.811|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 179   |     819|     114.507|   3.0%/ 23|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 179   |   32189|    1001.783|   0.4%/185|   0.3%/203|   0.3%/207|   0.3%/212 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 179   |    5430|      50.039|   1.2%/ 56|   1.1%/ 62|   1.1%/ 63|   1.1%/ 65 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 179   |    2377|      61.945|   0.7%/100|   0.7%/ 94|   0.7%/ 92|   0.8%/ 91 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 179   |    1934|     188.177|   0.3%/242|   0.3%/221|   0.3%/217|   0.3%/212 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 179   |     214|      77.824|   0.3%/263|   0.3%/276|   0.2%/279|   0.2%/283 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 179   |    4715|     242.986|   0.9%/ 77|   0.8%/ 82|   0.8%/ 83|   0.8%/ 85 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 179   |   20067|     136.747|   0.6%/109|   0.6%/108|   0.6%/107|   0.6%/107 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 120   |      29|       2.352|   1.2%/ 60|   0.9%/ 73|   0.9%/ 77|   0.8%/ 82 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 179   |    4675|     136.634|   0.6%/107|   0.6%/112|   0.6%/113|   0.6%/114 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 179   |     308|      18.983|   0.2%/335|   0.1%/473|   0.1%/526|   0.1%/590 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 179   |     749|     107.612|   0.1%/501|   0.1%/610|   0.1%/644|   0.1%/682 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 157   |      72|       9.165|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 179   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 179   |      41|       7.537|   0.9%/ 80|   1.0%/ 68|   1.1%/ 65|   1.1%/ 63 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 179   |     143|      68.442|   0.3%/240|   0.3%/204|   0.4%/196|   0.4%/188 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 172   |      99|       6.206|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 179   |   16605|     282.523|   0.4%/160|   0.3%/204|   0.3%/218|   0.3%/235 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 179   |   31065|     659.546|   0.2%/305|   0.2%/284|   0.2%/279|   0.3%/275 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 179   |      13|       0.604|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 179   |     840|      19.788|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 179   |    5880|     568.717|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 179   |    2060|     239.405|   0.1%/595|   0.1%/527|   0.1%/512|   0.1%/497 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 179   |     197|      11.249|   1.6%/ 44|   1.3%/ 53|   1.3%/ 55|   1.2%/ 58 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 179   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 179   |      59|       0.888|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 179   |      46|       6.081|   1.6%/ 44|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 179   |      85|      62.209|   3.1%/ 22|   2.2%/ 31|   2.0%/ 35|   1.7%/ 40 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 179   |     144|      12.297|   2.9%/ 24|   3.1%/ 22|   3.1%/ 22|   3.2%/ 22 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 179   |    7877|      94.723|   0.9%/ 77|   1.0%/ 73|   1.0%/ 72|   1.0%/ 71 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 179   |  204689|     621.127|   0.4%/176|   0.4%/182|   0.4%/183|   0.4%/184 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  65   |      72|       1.778|   2.1%/ 32|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 179   |    3983|      95.111|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 179   |     411|      41.577|   0.2%/308|   0.2%/335|   0.2%/343|   0.2%/351 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 179   |   41971|     631.761|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 179   |      47|      13.334|   0.3%/268|   0.2%/284|   0.2%/286|   0.2%/288 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 179   |     468|      13.710|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 71 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 179   |     606|      18.810|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  58   |      35|       0.364|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 178   |     339|      18.980|   0.3%/246|   0.2%/297|   0.2%/314|   0.2%/334 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 179   |     237|      15.666|   0.1%/548|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

