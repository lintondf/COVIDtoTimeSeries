# State and Country COVID-19 Analysis #
## Updated: at 2020-07-23 for data as of 2020-07-22 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.2% of deaths and 39.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.8% of deaths and 57.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 131   |   32620|    1676.811|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 135   |   15838|    1783.080|   0.2%/405|   0.1%/526|   0.1%/572|   0.1%/629 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 125   |    8484|    1220.864|   0.2%/366|   0.2%/421|   0.2%/438|   0.2%/457 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 141   |    8029|     203.207|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 128   |    7609|     600.494|   0.3%/242|   0.2%/334|   0.2%/371|   0.2%/420 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 126   |    7086|     553.498|   0.3%/276|   0.2%/307|   0.2%/316|   0.2%/326 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 126   |    6400|     640.805|   0.1%/494|   0.1%/548|   0.1%/565|   0.1%/584 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 137   |    5218|     242.943|   2.1%/ 32|   2.4%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 128   |    4295|     148.110|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 126   |    4409|    1236.691|   0.1%/666|   0.1%/612|   0.1%/601|   0.1%/590 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 145   |  142757|     433.195|   0.5%/129|   0.5%/129|   0.5%/129|   0.5%/129 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 128   |   83357|     394.286|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 134   |   45658|     687.248|   0.2%/450|   0.1%/524|   0.1%/547|   0.1%/571 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 126   |   41509|     327.932|   1.6%/ 42|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 153   |   35099|     582.666|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 159   |   30205|     450.305|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 134   |   29571|      21.724|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 142   |   28433|     603.674|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 154   |   14810|     177.626|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 125   |   13825|     430.277|   1.5%/ 46|   1.4%/ 50|   1.4%/ 50|   1.3%/ 51 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 120   |    1346|     274.547|   1.7%/ 41|   1.7%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 120   |      19|      25.325|   0.8%/ 84|   0.9%/ 79|   0.9%/ 77|   0.9%/ 76 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 124   |    2954|     405.834|   2.9%/ 24|   3.1%/ 22|   3.1%/ 22|   3.2%/ 22 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 121   |     377|     124.801|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 141   |    8029|     203.207|   1.3%/ 55|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 131   |    1767|     306.792|   0.2%/297|   0.2%/278|   0.3%/274|   0.3%/270 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 126   |    4409|    1236.691|   0.1%/666|   0.1%/612|   0.1%/601|   0.1%/590 |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 119   |     526|     539.737|   0.2%/448|   0.2%/429|   0.2%/424|   0.2%/419 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 137   |    5218|     242.943|   2.1%/ 32|   2.4%/ 29|   2.4%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 133   |    3248|     305.916|   0.8%/ 84|   0.9%/ 75|   1.0%/ 72|   1.0%/ 70 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 114   |      25|      17.530|   0.7%/101|   1.0%/ 66|   1.1%/ 60|   1.2%/ 56 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 119   |     125|      70.198|   1.5%/ 47|   1.7%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 128   |    7609|     600.494|   0.3%/242|   0.2%/334|   0.2%/371|   0.2%/420 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 129   |    2855|     424.147|   0.3%/205|   0.3%/213|   0.3%/215|   0.3%/217 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 120   |     808|     256.016|   0.7%/100|   0.8%/ 88|   0.8%/ 85|   0.8%/ 83 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 132   |     317|     108.896|   0.7%/101|   0.7%/100|   0.7%/ 99|   0.7%/ 99 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 129   |     683|     152.826|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 90 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 131   |    3561|     765.915|   0.4%/179|   0.3%/200|   0.3%/207|   0.3%/215 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 118   |     119|      88.296|   0.5%/135|   0.5%/149|   0.5%/153|   0.4%/158 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 126   |    3410|     563.975|   0.3%/248|   0.3%/268|   0.3%/273|   0.2%/279 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 125   |    8484|    1220.864|   0.2%/366|   0.2%/421|   0.2%/438|   0.2%/457 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 126   |    6400|     640.805|   0.1%/494|   0.1%/548|   0.1%/565|   0.1%/584 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 124   |    1596|     282.965|   0.3%/214|   0.3%/230|   0.3%/234|   0.3%/238 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 126   |    1412|     474.541|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 126   |    1159|     188.809|   0.5%/129|   0.5%/139|   0.5%/142|   0.5%/145 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 118   |      42|      39.047|   2.5%/ 27|   3.1%/ 22|   3.2%/ 22|   3.3%/ 21 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 117   |     308|     159.294|   0.7%/ 94|   0.9%/ 75|   1.0%/ 71|   1.0%/ 67 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 129   |     680|     220.628|   1.5%/ 48|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 122   |     402|     295.908|   0.3%/238|   0.2%/306|   0.2%/328|   0.2%/353 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 135   |   15838|    1783.080|   0.2%/405|   0.1%/526|   0.1%/572|   0.1%/629 |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 120   |     588|     280.626|   0.8%/ 85|   0.9%/ 80|   0.9%/ 79|   0.9%/ 78 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 131   |   32620|    1676.811|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 120   |    1711|     163.117|   1.2%/ 60|   1.3%/ 54|   1.3%/ 52|   1.4%/ 51 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 118   |      94|     123.905|   0.9%/ 73|   1.1%/ 65|   1.1%/ 63|   1.1%/ 61 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 125   |    3221|     275.546|   0.6%/116|   0.6%/111|   0.6%/110|   0.6%/109 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 126   |     462|     116.829|   1.0%/ 72|   1.1%/ 64|   1.1%/ 62|   1.1%/ 61 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 130   |     270|      63.931|   1.4%/ 51|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 126   |    7086|     553.498|   0.3%/276|   0.2%/307|   0.2%/316|   0.2%/326 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 124   |     183|      57.211|   1.0%/ 70|   1.1%/ 61|   1.2%/ 59|   1.2%/ 57 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 117   |    1000|     943.593|   0.2%/348|   0.2%/431|   0.2%/458|   0.1%/487 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 129   |    1230|     238.971|   2.6%/ 27|   2.8%/ 24|   2.9%/ 24|   2.9%/ 23 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 134   |     121|     137.268|   1.1%/ 64|   1.0%/ 69|   1.0%/ 71|   1.0%/ 73 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 124   |     888|     129.931|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38|   1.8%/ 38 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 128   |    4295|     148.110|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 145   |  142757|     433.195|   0.5%/129|   0.5%/129|   0.5%/129|   0.5%/129 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 123   |     259|      80.941|   1.8%/ 37|   1.8%/ 37|   1.8%/ 38|   1.8%/ 38 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 125   |      56|      89.745|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 131   |    2079|     243.555|   0.5%/130|   0.4%/179|   0.3%/198|   0.3%/222 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 145   |    1471|     193.209|   0.5%/146|   0.5%/154|   0.4%/156|   0.4%/158 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 115   |     101|      56.458|   0.4%/159|   0.5%/145|   0.5%/142|   0.5%/139 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 125   |     856|     147.001|   0.5%/147|   0.5%/134|   0.5%/130|   0.5%/127 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 101   |      25|      43.423|   1.0%/ 69|   1.1%/ 60|   1.2%/ 59|   1.2%/ 57 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 123   |    1246|      38.673|   1.9%/ 37|   1.5%/ 45|   1.5%/ 48|   1.4%/ 50 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 134   |     123|      43.329|   2.7%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 32 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 133   |    1107|      25.739|   0.9%/ 76|   0.9%/ 74|   0.9%/ 74|   0.9%/ 73 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 116   |      33|       1.057|   2.5%/ 28|   0.0%/ --|   1.1%/ 61|   4.4%/ 16 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 137   |    2521|      56.109|   3.1%/ 22|   3.2%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 119   |     680|     229.931|   1.9%/ 36|   1.8%/ 38|   1.8%/ 38|   1.8%/ 39 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 144   |     122|       4.762|   1.5%/ 46|   2.0%/ 35|   2.1%/ 33|   2.2%/ 32 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 133   |     712|      79.967|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 132   |     391|      38.804|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 129   |     132|      85.827|   1.7%/ 40|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 127   |    2782|      16.514|   1.7%/ 41|   1.5%/ 46|   1.5%/ 47|   1.4%/ 49 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 114   |     518|      55.019|   1.1%/ 64|   0.9%/ 75|   0.9%/ 78|   0.9%/ 81 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 134   |    9810|     851.223|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 108   |      33|       2.836|   2.7%/ 26|   2.8%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 116   |    2383|     207.718|   2.8%/ 24|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 124   |     265|      80.146|   1.8%/ 38|   2.0%/ 35|   2.0%/ 34|   2.1%/ 34 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 114   |       1|       0.428|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 128   |   83357|     394.286|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 134   |     318|      45.813|   1.6%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 127   |      53|       2.540|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 101   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 120   |     388|      14.603|   0.6%/110|   0.6%/110|   0.6%/110|   0.6%/110 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 136   |    8941|     235.288|   0.1%/632|   0.1%/858|   0.1%/941|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  61   |      56|      10.187|   0.4%/165|   0.8%/ 85|   0.9%/ 75|   1.0%/ 67 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  86   |      75|       4.631|   0.1%/889|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 123   |    8735|     457.132|   1.2%/ 58|   0.9%/ 73|   0.9%/ 78|   0.8%/ 84 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 134   |    4644|       3.312|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 123   |    7525|     152.336|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 126   |      69|      13.630|   8.4%/  8|   9.5%/  7|   9.8%/  7|  10.1%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 126   |     124|      30.450|   0.5%/126|   0.5%/131|   0.5%/133|   0.5%/135 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 127   |      87|       7.783|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 131   |     612|     105.086|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 128   |    1020|      98.482|   1.4%/ 50|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 131   |    5440|     311.406|   0.7%/ 96|   0.7%/106|   0.6%/109|   0.6%/112 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 137   |    4599|      45.860|   1.6%/ 43|   1.3%/ 54|   1.2%/ 57|   1.1%/ 61 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 114   |     363|      55.995|   3.2%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  92   |      51|      37.554|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 109   |     182|       1.846|   3.5%/ 20|   4.1%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 124   |     328|      59.358|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 159   |   30205|     450.305|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 125   |      47|      21.643|   0.2%/395|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 122   |       4|       1.805|   4.2%/ 16|   4.6%/ 15|   4.7%/ 14|   4.9%/ 14 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 110   |      16|       4.169|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 136   |    9115|     109.619|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 124   |     155|       5.116|   1.4%/ 51|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 134   |     195|      18.226|   0.2%/371|   0.2%/279|   0.3%/261|   0.3%/245 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 129   |    1650|      99.355|   2.9%/ 24|   2.4%/ 28|   2.3%/ 30|   2.2%/ 31 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)|  99   |      41|       3.362|   1.1%/ 62|   1.1%/ 62|   1.1%/ 63|   1.1%/ 63 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  88   |      26|      16.319|   0.2%/366|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 109   |     157|      13.564|   1.4%/ 49|   1.0%/ 71|   0.9%/ 80|   0.7%/ 94 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 119   |     997|     108.891|   2.7%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Hong Kong](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hong%20Kong.png)|  35   |       3|       0.400|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 130   |     598|      61.203|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 134   |   29571|      21.724|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28|   2.4%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 134   |    4376|      16.396|   2.1%/ 34|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 154   |   14810|     177.626|   1.5%/ 47|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 141   |    4305|     110.027|   2.8%/ 25|   2.1%/ 33|   1.9%/ 36|   1.8%/ 39 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 134   |    1755|     356.519|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 124   |     421|      45.834|   1.6%/ 42|   1.9%/ 36|   2.0%/ 35|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 153   |   35099|     582.666|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 126   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 161   |     990|       7.864|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 118   |      11|       1.028|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 120   |     573|      30.670|  13.6%/  5|  15.8%/  4|  16.3%/  4|  16.8%/  4 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 119   |     253|       5.310|   2.9%/ 24|   3.2%/ 21|   3.3%/ 21|   3.4%/ 20 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 119   |     155|      86.191|   3.7%/ 18|   4.0%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 110   |     417|      94.438|   0.7%/105|   0.6%/121|   0.6%/126|   0.5%/131 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 111   |     244|      37.318|   5.2%/ 13|   4.3%/ 16|   4.1%/ 17|   3.9%/ 17 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 111   |      31|      16.372|   0.2%/363|   0.2%/357|   0.2%/362|   0.2%/372 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 135   |      41|       6.036|   1.0%/ 69|   1.2%/ 59|   1.2%/ 57|   1.2%/ 55 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 110   |      73|      16.244|   1.5%/ 46|   0.9%/ 77|   0.7%/ 96|   0.5%/128 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 112   |      54|       7.831|   4.8%/ 14|   1.4%/ 49|   1.4%/ 50|   3.4%/ 20 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 124   |      80|      28.600|   0.1%/613|   0.1%/551|   0.1%/532|   0.1%/513 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  67   |      71|       2.697|   5.3%/ 13|   6.2%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 128   |     123|       3.750|   0.1%/628|   0.1%/492|   0.1%/467|   0.2%/444 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 116   |     122|       6.048|   0.2%/445|   0.1%/923|   0.1%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 115   |     159|      38.900|   0.8%/ 87|   0.6%/113|   0.6%/122|   0.5%/133 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 126   |   41509|     327.932|   1.6%/ 42|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 127   |     716|     267.036|   1.1%/ 62|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 135   |     280|       7.804|   1.2%/ 58|   1.3%/ 53|   1.3%/ 51|   1.4%/ 50 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  59   |      11|       0.369|   1.5%/ 47|   3.5%/ 20|   4.0%/ 17|   4.6%/ 15 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  13   |       7|       2.847|  26.0%/  2|  26.0%/  2|  51.8%/  1|  32.6%/  2 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  68   |      41|       1.376|   1.1%/ 61|   0.7%/ 96|   0.6%/112|   0.5%/133 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 139   |    6163|     353.016|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 116   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 118   |     106|      16.379|   1.3%/ 52|   1.3%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 120   |      69|       3.099|   0.1%/684|   0.1%/735|   0.1%/748|   0.1%/762 |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 122   |     830|       4.028|   1.3%/ 54|   1.0%/ 66|   1.0%/ 70|   0.9%/ 75 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 123   |     443|     213.380|   1.6%/ 44|   1.4%/ 49|   1.4%/ 51|   1.3%/ 52 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 131   |     255|      47.576|   0.1%/707|   0.1%/699|   0.1%/696|   0.1%/695 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 114   |     347|      74.362|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 126   |    5841|      26.631|   1.0%/ 69|   0.8%/ 92|   0.7%/100|   0.6%/111 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 134   |    1195|     283.282|   2.8%/ 25|   2.7%/ 26|   2.7%/ 26|   2.7%/ 26 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 124   |      34|       4.704|   4.1%/ 17|   5.0%/ 14|   5.2%/ 13|   5.5%/ 13 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 125   |   13825|     430.277|   1.5%/ 46|   1.4%/ 50|   1.4%/ 50|   1.3%/ 51 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 172   |    1826|      16.823|   0.8%/ 82|   0.9%/ 79|   0.9%/ 79|   0.9%/ 78 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 133   |    1652|      43.032|   0.5%/154|   0.4%/183|   0.4%/192|   0.3%/202 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 128   |    1710|     166.391|   0.3%/235|   0.2%/282|   0.2%/298|   0.2%/317 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 117   |     166|      60.278|   1.3%/ 55|   0.9%/ 76|   0.8%/ 84|   0.7%/ 95 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 123   |    2097|     108.063|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 126   |   12891|      87.844|   1.3%/ 54|   1.1%/ 61|   1.1%/ 64|   1.0%/ 66 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  54   |       5|       0.422|   3.7%/ 19|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 121   |    2651|      77.473|   1.8%/ 39|   1.4%/ 48|   1.4%/ 50|   1.3%/ 53 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 113   |     176|      10.844|   1.8%/ 38|   1.7%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 125   |     514|      73.782|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  91   |      66|       8.356|   0.4%/166|   0.5%/141|   0.5%/135|   0.5%/129 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 124   |      27|       4.753|   0.2%/332|   0.2%/280|   0.3%/271|   0.3%/264 |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 117   |      28|       5.132|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 131   |     112|      53.666|   0.2%/364|   0.3%/254|   0.3%/234|   0.3%/216 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 106   |      93|       5.875|   0.1%/894|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 118   |    5675|      96.546|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.0%/ 23 |
|[South Korea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Korea.png)|  19   |      53|       1.024|  23.8%/  3|  11.2%/  6|  10.0%/  7|   9.1%/  7 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 142   |   28433|     603.674|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 117   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 132   |     705|      16.605|   0.8%/ 87|   0.7%/ 93|   0.7%/ 95|   0.7%/ 96 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 134   |    5676|     549.011|   0.2%/292|   0.2%/338|   0.2%/351|   0.2%/364 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 140   |    1971|     229.124|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 116   |      32|       1.824|   5.0%/ 14|   5.1%/ 14|   7.4%/  9|   8.6%/  8 |
|[Taiwan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Taiwan.png)|  23   |       1|       0.042|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 114   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 144   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 118   |      15|       2.029|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 120   |       8|       5.865|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 126   |      50|       4.265|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 128   |    5552|      66.766|   0.3%/201|   0.3%/206|   0.3%/208|   0.3%/209 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 145   |  142757|     433.195|   0.5%/129|   0.5%/129|   0.5%/129|   0.5%/129 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 132   |    1574|      37.573|   1.2%/ 60|   1.0%/ 68|   1.0%/ 70|   1.0%/ 73 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 125   |     343|      34.711|   0.3%/210|   0.3%/245|   0.3%/256|   0.3%/268 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 134   |   45658|     687.248|   0.2%/450|   0.1%/524|   0.1%/547|   0.1%/571 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 116   |      34|       9.600|   1.0%/ 69|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 118   |     107|       3.126|   5.8%/ 12|   5.0%/ 14|   4.8%/ 14|   4.5%/ 15 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 118   |     129|       3.992|   3.7%/ 19|   3.1%/ 22|   3.0%/ 23|   2.8%/ 24 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 112   |     144|       8.051|  16.4%/  4|  18.6%/  4|  19.2%/  3|  19.7%/  3 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 122   |      32|       2.119|   6.7%/ 10|   6.0%/ 11|   5.7%/ 12|   5.4%/ 13 |

