# State and Country COVID-19 Analysis #
## Updated: at 2020-09-24 for data as of 2020-09-23 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.1% of deaths and 56.1% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 176   |   33101|    1701.553|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 176   |   16083|    1810.674|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 176   |   15616|     538.564|   0.7%/105|   0.5%/127|   0.5%/134|   0.5%/142 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 176   |   15437|     390.687|   0.6%/114|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 176   |   13715|     638.573|   0.7%/ 95|   0.7%/104|   0.6%/107|   0.6%/110 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 176   |    9341|    1344.064|   0.1%/492|   0.1%/494|   0.1%/494|   0.1%/493 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 176   |    8749|     690.416|   0.2%/284|   0.2%/288|   0.2%/289|   0.2%/290 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 176   |    7999|     624.827|   0.2%/330|   0.2%/314|   0.2%/310|   0.2%/306 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 176   |    7019|     702.782|   0.1%/507|   0.1%/528|   0.1%/534|   0.1%/539 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 176   |    6844|     644.562|   0.6%/108|   0.5%/130|   0.5%/137|   0.5%/144 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 176   |  202412|     614.218|   0.4%/185|   0.4%/197|   0.3%/200|   0.3%/204 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 176   |  139677|     660.686|   0.5%/136|   0.5%/149|   0.5%/153|   0.4%/157 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 176   |   91019|      66.866|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 176   |   75438|     595.984|   0.6%/121|   0.5%/133|   0.5%/137|   0.5%/140 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 176   |   41886|     630.481|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 176   |   35726|     593.077|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 176   |   31862|     991.625|   0.3%/206|   0.3%/249|   0.3%/263|   0.2%/278 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 176   |   31265|     466.113|   0.1%/503|   0.2%/436|   0.2%/422|   0.2%/408 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 176   |   30665|     651.060|   0.2%/351|   0.2%/331|   0.2%/326|   0.2%/322 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 176   |   24669|     295.866|   0.6%/108|   0.7%/105|   0.7%/104|   0.7%/103 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 176   |    2502|     510.220|   0.5%/136|   0.4%/157|   0.4%/163|   0.4%/170 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 176   |      47|      64.857|   0.5%/152|   0.3%/235|   0.3%/272|   0.2%/324 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 176   |    5565|     764.594|   0.3%/205|   0.3%/249|   0.3%/263|   0.2%/278 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 176   |    1244|     412.200|   1.0%/ 67|   0.8%/ 83|   0.8%/ 88|   0.7%/ 94 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 176   |   15437|     390.687|   0.6%/114|   0.5%/127|   0.5%/131|   0.5%/135 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 176   |    2027|     351.955|   0.2%/380|   0.2%/377|   0.2%/376|   0.2%/375 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 176   |    4495|    1260.807|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 176   |     625|     641.924|   0.2%/338|   0.2%/297|   0.2%/288|   0.2%/280 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 176   |   13715|     638.573|   0.7%/ 95|   0.7%/104|   0.6%/107|   0.6%/110 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 176   |    6844|     644.562|   0.6%/108|   0.5%/130|   0.5%/137|   0.5%/144 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 176   |     132|      93.386|   1.8%/ 38|   1.4%/ 50|   1.3%/ 55|   1.1%/ 60 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 176   |     465|     260.072|   0.8%/ 82|   0.7%/ 98|   0.7%/102|   0.6%/108 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 176   |    8749|     690.416|   0.2%/284|   0.2%/288|   0.2%/289|   0.2%/290 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 176   |    3540|     525.901|   0.3%/254|   0.3%/267|   0.3%/271|   0.3%/274 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 176   |    1307|     414.098|   0.6%/112|   0.6%/120|   0.6%/122|   0.6%/124 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 176   |     613|     210.432|   1.4%/ 49|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 176   |    1144|     256.008|   0.7%/101|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 176   |    5447|    1171.680|   0.3%/204|   0.3%/234|   0.3%/243|   0.3%/252 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 176   |     140|     103.912|   0.3%/243|   0.3%/226|   0.3%/222|   0.3%/218 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 176   |    3904|     645.750|   0.2%/444|   0.1%/471|   0.1%/478|   0.1%/485 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 176   |    9341|    1344.064|   0.1%/492|   0.1%/494|   0.1%/494|   0.1%/493 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 176   |    7019|     702.782|   0.1%/507|   0.1%/528|   0.1%/534|   0.1%/539 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 176   |    2039|     361.520|   0.4%/189|   0.4%/191|   0.4%/191|   0.4%/191 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 176   |    2895|     972.699|   0.6%/121|   0.5%/140|   0.5%/145|   0.5%/151 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 176   |    1889|     307.742|   0.8%/ 89|   0.8%/ 88|   0.8%/ 88|   0.8%/ 88 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 176   |     163|     152.886|   2.1%/ 33|   2.2%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 176   |     459|     237.038|   0.7%/106|   0.7%/102|   0.7%/101|   0.7%/100 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 176   |    1578|     512.261|   0.6%/109|   0.5%/129|   0.5%/134|   0.5%/141 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 176   |     439|     322.850|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 176   |   16083|    1810.674|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 176   |     861|     410.464|   0.4%/178|   0.4%/192|   0.4%/195|   0.3%/199 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 176   |   33101|    1701.553|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 176   |    3337|     318.202|   0.8%/ 86|   0.8%/ 91|   0.8%/ 92|   0.7%/ 93 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 176   |     195|     255.943|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 176   |    4686|     400.885|   0.5%/140|   0.5%/143|   0.5%/143|   0.5%/144 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 176   |     980|     247.616|   0.7%/ 95|   0.6%/107|   0.6%/111|   0.6%/114 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 176   |     545|     129.169|   0.6%/116|   0.5%/136|   0.5%/143|   0.5%/150 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 176   |    7999|     624.827|   0.2%/330|   0.2%/314|   0.2%/310|   0.2%/306 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 176   |     632|     198.016|   1.5%/ 47|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 176   |    1097|    1035.122|   0.2%/279|   0.3%/255|   0.3%/250|   0.3%/245 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 176   |    3312|     643.279|   0.7%/102|   0.6%/118|   0.6%/123|   0.5%/128 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 176   |     201|     227.262|   1.0%/ 69|   1.1%/ 63|   1.1%/ 62|   1.1%/ 60 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 176   |    2321|     339.609|   1.0%/ 67|   0.9%/ 73|   0.9%/ 75|   0.9%/ 76 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 176   |   15616|     538.564|   0.7%/105|   0.5%/127|   0.5%/134|   0.5%/142 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 176   |  202412|     614.218|   0.4%/185|   0.4%/197|   0.3%/200|   0.3%/204 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 176   |     449|     140.117|   0.3%/255|   0.2%/355|   0.2%/393|   0.2%/440 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 176   |      58|      92.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 176   |    3025|     354.452|   0.8%/ 90|   0.8%/ 83|   0.9%/ 81|   0.9%/ 80 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 176   |    2070|     271.808|   0.3%/206|   0.3%/210|   0.3%/210|   0.3%/211 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 176   |     330|     184.279|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 176   |    1266|     217.391|   0.4%/162|   0.4%/175|   0.4%/179|   0.4%/183 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 164   |      50|      86.184|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 176   |    1445|      44.830|   0.1%/503|   0.1%/486|   0.1%/482|   0.1%/477 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 176   |     377|     132.513|   1.0%/ 67|   0.9%/ 76|   0.9%/ 78|   0.9%/ 81 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 176   |    1702|      39.590|   0.5%/140|   0.5%/146|   0.5%/148|   0.5%/149 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 176   |     158|       5.075|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 176   |   14224|     316.518|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35|   2.0%/ 35 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 176   |     943|     318.941|   0.3%/246|   0.3%/266|   0.3%/271|   0.3%/276 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 176   |     945|      36.786|   0.6%/108|   0.3%/264|   0.2%/410|   0.1%/913 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 176   |     769|      86.350|   0.2%/288|   0.3%/246|   0.3%/238|   0.3%/230 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 176   |     583|      57.878|   0.3%/205|   0.3%/217|   0.3%/221|   0.3%/225 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 176   |     227|     147.350|   0.8%/ 82|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 176   |    5090|      30.213|   0.7%/104|   0.6%/114|   0.6%/117|   0.6%/120 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 176   |     801|      85.116|   0.7%/106|   0.6%/111|   0.6%/112|   0.6%/113 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 176   |    9954|     863.713|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 171   |      40|       3.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 176   |    8204|     715.258|   0.6%/117|   0.4%/164|   0.4%/182|   0.3%/204 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 176   |     794|     240.607|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 176   |      16|       6.948|   3.4%/ 20|   2.5%/ 27|   2.3%/ 30|   2.0%/ 34 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 176   |  139677|     660.686|   0.5%/136|   0.5%/149|   0.5%/153|   0.4%/157 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 176   |     797|     114.647|   0.8%/ 89|   0.6%/109|   0.6%/116|   0.6%/124 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 176   |      56|       2.695|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 164   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 176   |     417|      15.714|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 176   |    9283|     244.291|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 124   |      62|      11.288|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 149   |      82|       5.043|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 176   |   12444|     651.257|   0.4%/189|   0.3%/205|   0.3%/210|   0.3%/215 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 176   |    4744|       3.383|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 176   |   25392|     514.051|   0.8%/ 83|   0.7%/104|   0.6%/110|   0.6%/118 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 176   |     775|     153.283|   2.6%/ 26|   2.7%/ 26|   2.7%/ 25|   2.7%/ 25 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 176   |     256|      62.804|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42|   1.7%/ 41 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 176   |     117|      10.452|   1.0%/ 72|   1.0%/ 66|   1.1%/ 65|   1.1%/ 64 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 176   |     638|     109.552|   0.1%/468|   0.2%/401|   0.2%/387|   0.2%/373 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 176   |    2144|     206.996|   0.7%/105|   0.5%/130|   0.5%/139|   0.5%/150 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 176   |    7314|     418.708|   0.3%/232|   0.3%/276|   0.2%/290|   0.2%/306 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 176   |    5828|      58.118|   0.3%/224|   0.3%/228|   0.3%/229|   0.3%/230 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 176   |     834|     128.596|   0.4%/157|   0.3%/212|   0.3%/232|   0.3%/256 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 155   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 172   |    1176|      11.918|   1.2%/ 55|   1.0%/ 68|   1.0%/ 72|   0.9%/ 76 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 176   |     340|      61.525|   0.1%/679|   0.1%/576|   0.1%/554|   0.1%/533 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 176   |   31265|     466.113|   0.1%/503|   0.2%/436|   0.2%/422|   0.2%/408 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 176   |      53|      24.565|   0.1%/493|   0.2%/376|   0.2%/353|   0.2%/332 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 176   |     110|      46.838|   1.3%/ 54|   0.0%/ --|   0.6%/113|   0.6%/113 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 173   |      19|       5.202|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 176   |    9404|     113.098|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 176   |     301|       9.944|   0.3%/245|   0.2%/315|   0.2%/338|   0.2%/364 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 176   |     347|      32.402|   1.4%/ 50|   1.5%/ 47|   1.5%/ 46|   1.5%/ 45 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 176   |    3163|     190.508|   0.6%/123|   0.5%/130|   0.5%/132|   0.5%/134 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 162   |      65|       5.352|   0.3%/205|   0.3%/272|   0.2%/294|   0.2%/319 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 151   |      40|      25.107|   0.1%/544|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 172   |     226|      19.544|   0.3%/209|   0.3%/243|   0.3%/254|   0.3%/267 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 176   |    2255|     246.171|   0.7%/106|   0.5%/127|   0.5%/133|   0.5%/139 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 176   |     647|      66.232|   0.7%/ 97|   0.9%/ 81|   0.9%/ 78|   0.9%/ 74 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 176   |   91019|      66.866|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 176   |    9949|      37.274|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 176   |   24669|     295.866|   0.6%/108|   0.7%/105|   0.7%/104|   0.7%/103 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 176   |    8840|     225.931|   0.9%/ 77|   0.8%/ 82|   0.8%/ 83|   0.8%/ 84 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 176   |    1792|     364.035|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 176   |    1300|     141.448|   1.5%/ 46|   1.6%/ 45|   1.6%/ 44|   1.6%/ 44 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 176   |   35726|     593.077|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 176   |      72|      26.499|   5.0%/ 14|   8.4%/  8|   7.7%/  9|   4.3%/ 16 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 176   |    1560|      12.389|   0.6%/114|   0.5%/135|   0.5%/142|   0.5%/150 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 176   |      33|       3.109|   4.1%/ 17|   4.5%/ 15|   4.5%/ 15|   4.6%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 176   |    1718|      91.952|   0.3%/224|   0.2%/300|   0.2%/328|   0.2%/361 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 176   |     664|      13.959|   0.5%/126|   0.5%/138|   0.5%/140|   0.5%/143 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 176   |     495|     275.535|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 173   |     589|     133.334|   0.5%/143|   0.5%/138|   0.5%/137|   0.5%/136 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 174   |    1056|     161.637|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 174   |      36|      18.980|   0.2%/334|   0.2%/372|   0.2%/383|   0.2%/394 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 176   |     325|      47.580|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 173   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 175   |     485|      70.525|   2.8%/ 25|   2.7%/ 26|   2.6%/ 26|   2.6%/ 26 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 176   |      87|      31.289|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 130   |     227|       8.633|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 176   |     130|       3.968|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 176   |     129|       6.368|   0.1%/653|   0.1%/621|   0.1%/615|   0.1%/608 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 176   |     162|      39.655|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 176   |   75438|     595.984|   0.6%/121|   0.5%/133|   0.5%/137|   0.5%/140 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 176   |    1236|     460.830|   0.9%/ 74|   1.0%/ 73|   1.0%/ 72|   1.0%/ 72 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 176   |    2010|      56.031|   2.0%/ 34|   1.8%/ 39|   1.7%/ 41|   1.6%/ 42 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 122   |      47|       1.578|   3.3%/ 21|   3.5%/ 20|   3.5%/ 20|   3.5%/ 19 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  76   |     117|      47.783|   1.6%/ 43|   1.3%/ 51|   1.3%/ 54|   1.2%/ 57 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 131   |     450|      15.013|   2.5%/ 28|   2.1%/ 33|   2.0%/ 35|   1.9%/ 36 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 176   |    6333|     362.802|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 176   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 176   |     149|      23.137|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 176   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 176   |    1114|       5.404|   0.3%/268|   0.2%/310|   0.2%/323|   0.2%/339 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 176   |     704|     338.894|   0.8%/ 85|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 176   |     267|      49.681|   0.1%/ ***|   0.1%/ ***|   0.1%/975|   0.1%/940 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 176   |     869|     186.363|   1.1%/ 61|   1.1%/ 60|   1.2%/ 60|   1.2%/ 60 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 176   |    6446|      29.387|   0.1%/854|   0.1%/965|   0.1%/997|   0.1%/ *** |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 176   |    2302|     545.578|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  59   |       7|       0.796|   2.7%/ 26|   2.7%/ 26|   2.7%/ 25|   2.8%/ 24 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 176   |     762|     106.535|   3.2%/ 22|   2.7%/ 25|   2.6%/ 26|   2.5%/ 27 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 176   |   31862|     991.625|   0.3%/206|   0.3%/249|   0.3%/263|   0.2%/278 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 176   |    5230|      48.193|   1.4%/ 51|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 176   |    2328|      60.664|   0.6%/120|   0.6%/119|   0.6%/118|   0.6%/118 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 176   |    1914|     186.237|   0.3%/235|   0.3%/210|   0.3%/204|   0.3%/199 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 176   |     212|      77.255|   0.3%/241|   0.3%/244|   0.3%/246|   0.3%/247 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 176   |    4604|     237.246|   0.9%/ 77|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 176   |   19682|     134.122|   0.6%/114|   0.6%/114|   0.6%/114|   0.6%/114 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 117   |      27|       2.218|   1.5%/ 46|   2.6%/ 27|   1.3%/ 55|   1.3%/ 55 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 176   |    4591|     134.181|   0.7%/105|   0.6%/110|   0.6%/111|   0.6%/113 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 176   |     307|      18.917|   0.2%/325|   0.1%/521|   0.1%/610|   0.1%/735 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 176   |     747|     107.281|   0.2%/450|   0.1%/549|   0.1%/579|   0.1%/613 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 154   |      73|       9.176|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 176   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 176   |      40|       7.391|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 176   |     140|      67.020|   0.1%/566|   0.1%/565|   0.1%/562|   0.1%/558 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 169   |      99|       6.204|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 176   |   16458|     280.010|   0.5%/150|   0.3%/198|   0.3%/215|   0.3%/235 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 176   |   30665|     651.060|   0.2%/351|   0.2%/331|   0.2%/326|   0.2%/322 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 176   |      13|       0.599|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 176   |     840|      19.798|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 176   |    5872|     567.945|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 176   |    2048|     238.031|   0.1%/705|   0.1%/624|   0.1%/606|   0.1%/588 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 176   |     190|      10.878|   1.7%/ 40|   1.5%/ 47|   1.4%/ 49|   1.3%/ 52 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 176   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 176   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 176   |      44|       5.790|   0.6%/107|   0.6%/108|   0.6%/109|   0.6%/110 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 176   |      81|      59.043|   4.0%/ 17|   3.2%/ 21|   3.0%/ 23|   2.8%/ 24 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 176   |     134|      11.429|   4.9%/ 14|   5.7%/ 12|   5.9%/ 12|   6.0%/ 11 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 176   |    7640|      91.881|   0.9%/ 79|   0.9%/ 74|   1.0%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 176   |  202412|     614.218|   0.4%/185|   0.4%/197|   0.3%/200|   0.3%/204 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  62   |      67|       1.664|   2.6%/ 26|   1.6%/ 44|   1.4%/ 51|   1.1%/ 61 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 176   |    3799|      90.710|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 176   |     409|      41.325|   0.2%/329|   0.2%/382|   0.2%/398|   0.2%/416 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 176   |   41886|     630.481|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 176   |      47|      13.234|   0.2%/363|   0.1%/506|   0.1%/555|   0.1%/611 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 176   |     454|      13.311|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 176   |     578|      17.948|   1.7%/ 41|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  55   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 175   |     335|      18.733|   0.4%/175|   0.4%/187|   0.4%/190|   0.4%/194 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 176   |     240|      15.852|   0.2%/351|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

