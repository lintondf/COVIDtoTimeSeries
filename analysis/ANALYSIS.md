# State and Country COVID-19 Analysis #
## Updated: at 2020-09-18 for data as of 2020-09-17 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.9% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.3% of deaths and 56.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 170   |   33063|    1699.563|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 170   |   16046|    1806.502|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 170   |   15084|     520.216|   0.8%/ 87|   0.7%/104|   0.6%/110|   0.6%/116 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 170   |   14917|     377.534|   0.7%/ 98|   0.6%/107|   0.6%/110|   0.6%/113 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 170   |   13138|     611.680|   0.8%/ 83|   0.8%/ 92|   0.7%/ 94|   0.7%/ 96 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 170   |    9262|    1332.740|   0.1%/524|   0.1%/549|   0.1%/556|   0.1%/562 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 170   |    8619|     680.140|   0.3%/276|   0.3%/275|   0.3%/275|   0.3%/275 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 170   |    7901|     617.162|   0.2%/435|   0.2%/461|   0.1%/468|   0.1%/475 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 170   |    6957|     696.665|   0.2%/462|   0.1%/473|   0.1%/476|   0.1%/480 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 170   |    6622|     623.694|   0.8%/ 91|   0.6%/109|   0.6%/115|   0.6%/122 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 170   |  198011|     600.863|   0.4%/167|   0.4%/177|   0.4%/179|   0.4%/182 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 170   |  135589|     641.349|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/133 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 170   |   84397|      62.001|   1.4%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 170   |   73101|     577.521|   0.6%/108|   0.6%/119|   0.6%/122|   0.6%/125 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 170   |   41766|     628.673|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 170   |   35646|     591.753|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 170   |   31000|     462.166|   0.1%/758|   0.1%/669|   0.1%/649|   0.1%/630 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 170   |   31343|     975.463|   0.4%/160|   0.4%/181|   0.4%/188|   0.4%/194 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 170   |   29973|     636.357|   0.2%/365|   0.2%/332|   0.2%/325|   0.2%/318 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 170   |   23736|     284.685|   0.6%/124|   0.5%/127|   0.5%/127|   0.5%/127 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 170   |    2434|     496.363|   0.6%/112|   0.6%/125|   0.5%/128|   0.5%/132 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 170   |      47|      64.113|   0.7%/102|   0.5%/129|   0.5%/138|   0.5%/149 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 170   |    5466|     750.927|   0.4%/187|   0.3%/250|   0.3%/272|   0.2%/299 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 170   |    1076|     356.708|   1.5%/ 46|   1.4%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 170   |   14917|     377.534|   0.7%/ 98|   0.6%/107|   0.6%/110|   0.6%/113 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 170   |    2005|     348.188|   0.2%/396|   0.2%/401|   0.2%/402|   0.2%/403 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 170   |    4484|    1257.823|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 170   |     618|     634.375|   0.1%/475|   0.2%/440|   0.2%/431|   0.2%/422 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 170   |   13138|     611.680|   0.8%/ 83|   0.8%/ 92|   0.7%/ 94|   0.7%/ 96 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 170   |    6622|     623.694|   0.8%/ 91|   0.6%/109|   0.6%/115|   0.6%/122 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 170   |     115|      81.350|   2.4%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 170   |     445|     249.288|   1.0%/ 72|   0.8%/ 90|   0.7%/ 97|   0.7%/104 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 170   |    8619|     680.140|   0.3%/276|   0.3%/275|   0.3%/275|   0.3%/275 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 170   |    3483|     517.310|   0.3%/229|   0.3%/235|   0.3%/237|   0.3%/238 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 170   |    1264|     400.684|   0.6%/107|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 170   |     539|     185.096|   1.6%/ 44|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 170   |    1097|     245.495|   0.9%/ 81|   0.8%/ 83|   0.8%/ 84|   0.8%/ 84 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 170   |    5346|    1150.069|   0.4%/171|   0.4%/195|   0.3%/201|   0.3%/208 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 170   |     137|     102.048|   0.3%/263|   0.3%/249|   0.3%/245|   0.3%/241 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 170   |    3870|     640.122|   0.2%/431|   0.1%/468|   0.1%/479|   0.1%/490 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 170   |    9262|    1332.740|   0.1%/524|   0.1%/549|   0.1%/556|   0.1%/562 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 170   |    6957|     696.665|   0.2%/462|   0.1%/473|   0.1%/476|   0.1%/480 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 170   |    1993|     353.408|   0.4%/187|   0.4%/191|   0.4%/192|   0.4%/193 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 170   |    2809|     943.931|   0.7%/102|   0.6%/117|   0.6%/121|   0.6%/126 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 170   |    1797|     292.765|   0.7%/100|   0.7%/104|   0.7%/105|   0.6%/107 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 170   |     143|     133.979|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 170   |     442|     228.443|   0.6%/124|   0.6%/125|   0.6%/125|   0.6%/126 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 170   |    1524|     494.940|   0.8%/ 90|   0.7%/105|   0.6%/109|   0.6%/114 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 170   |     437|     321.645|   0.1%/714|   0.1%/696|   0.1%/688|   0.1%/679 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 170   |   16046|    1806.502|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 170   |     842|     401.382|   0.4%/173|   0.4%/194|   0.3%/200|   0.3%/206 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 170   |   33063|    1699.563|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 170   |    3180|     303.213|   0.9%/ 77|   0.9%/ 78|   0.9%/ 78|   0.9%/ 79 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 170   |     175|     230.021|   1.3%/ 52|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 170   |    4532|     387.709|   0.6%/116|   0.6%/111|   0.6%/110|   0.6%/108 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 170   |     942|     238.140|   0.8%/ 83|   0.7%/ 94|   0.7%/ 97|   0.7%/100 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 170   |     529|     125.316|   0.8%/ 87|   0.7%/ 94|   0.7%/ 96|   0.7%/ 98 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 170   |    7901|     617.162|   0.2%/435|   0.2%/461|   0.1%/468|   0.1%/475 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 170   |     573|     179.525|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 170   |    1080|    1019.586|   0.2%/333|   0.2%/311|   0.2%/306|   0.2%/301 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 170   |    3193|     620.141|   0.8%/ 84|   0.7%/ 94|   0.7%/ 97|   0.7%/100 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 170   |     187|     211.507|   0.9%/ 81|   0.9%/ 73|   1.0%/ 72|   1.0%/ 70 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 170   |    2183|     319.493|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 170   |   15084|     520.216|   0.8%/ 87|   0.7%/104|   0.6%/110|   0.6%/116 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 170   |  198011|     600.863|   0.4%/167|   0.4%/177|   0.4%/179|   0.4%/182 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 170   |     444|     138.576|   0.4%/189|   0.3%/253|   0.3%/276|   0.2%/303 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 170   |      58|      92.950|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 170   |    2839|     332.631|   0.4%/164|   0.4%/182|   0.4%/187|   0.4%/193 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 170   |    2033|     266.927|   0.3%/219|   0.3%/244|   0.3%/250|   0.3%/257 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 170   |     299|     166.927|   1.8%/ 38|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 170   |    1234|     212.021|   0.5%/135|   0.5%/139|   0.5%/140|   0.5%/141 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 158   |      46|      78.868|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 170   |    1433|      44.457|   0.1%/563|   0.1%/584|   0.1%/588|   0.1%/590 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 170   |     356|     125.259|   1.1%/ 63|   1.0%/ 72|   0.9%/ 75|   0.9%/ 78 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 170   |    1654|      38.460|   0.5%/129|   0.5%/133|   0.5%/134|   0.5%/135 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 170   |     143|       4.583|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 170   |   12703|     282.667|   2.0%/ 34|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 170   |     930|     314.405|   0.3%/235|   0.3%/265|   0.3%/274|   0.2%/284 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 170   |    1002|      39.016|   1.1%/ 65|   0.6%/111|   0.5%/136|   0.4%/175 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 170   |     757|      85.004|   0.1%/542|   0.1%/468|   0.2%/452|   0.2%/436 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 170   |     571|      56.732|   0.4%/174|   0.4%/173|   0.4%/173|   0.4%/173 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 170   |     216|     139.959|   0.7%/ 93|   0.8%/ 90|   0.8%/ 90|   0.8%/ 89 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 170   |    4910|      29.148|   0.7%/ 92|   0.7%/101|   0.7%/103|   0.7%/106 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 170   |     772|      82.009|   0.7%/ 93|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 170   |    9933|     861.904|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 165   |      40|       3.429|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 170   |    7721|     673.192|   0.8%/ 83|   0.7%/103|   0.6%/110|   0.6%/118 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 170   |     747|     226.352|   1.2%/ 60|   1.1%/ 64|   1.1%/ 65|   1.0%/ 66 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 170   |      13|       5.759|   5.5%/ 12|   5.3%/ 13|   5.3%/ 13|   5.2%/ 13 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 170   |  135589|     641.349|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/133 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 170   |     766|     110.186|   1.0%/ 68|   0.9%/ 77|   0.9%/ 80|   0.8%/ 83 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 170   |      56|       2.688|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 158   |       1|       0.091|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 170   |     417|      15.716|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 170   |    9249|     243.400|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 118   |      62|      11.310|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 143   |      81|       4.979|   0.2%/443|   0.2%/337|   0.2%/317|   0.2%/299 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 170   |   12171|     637.008|   0.4%/164|   0.4%/172|   0.4%/174|   0.4%/177 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 170   |    4746|       3.384|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 170   |   24390|     493.761|   1.1%/ 65|   0.9%/ 78|   0.8%/ 83|   0.8%/ 87 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 170   |     662|     130.964|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27|   2.5%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 170   |     230|      56.396|   1.5%/ 45|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 170   |     110|       9.831|   0.7%/102|   0.7%/ 97|   0.7%/ 96|   0.7%/ 95 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 170   |     633|     108.640|   0.1%/737|   0.1%/645|   0.1%/625|   0.1%/606 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 170   |    2063|     199.156|   0.9%/ 75|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 170   |    7127|     407.974|   0.4%/166|   0.4%/177|   0.4%/180|   0.4%/183 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 170   |    5723|      57.071|   0.3%/220|   0.3%/226|   0.3%/227|   0.3%/228 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 170   |     817|     125.934|   0.6%/117|   0.5%/149|   0.4%/160|   0.4%/173 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 149   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 166   |    1109|      11.239|   1.5%/ 47|   1.2%/ 60|   1.1%/ 64|   1.0%/ 68 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 170   |     338|      61.175|   0.1%/961|   0.1%/830|   0.1%/801|   0.1%/773 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 170   |   31000|     462.166|   0.1%/758|   0.1%/669|   0.1%/649|   0.1%/630 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 170   |      53|      24.440|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 170   |     106|      45.079|   0.3%/206|   1.0%/ 71|   1.3%/ 54|   1.3%/ 54 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 167   |      19|       5.205|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 170   |    9375|     112.747|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 170   |     297|       9.813|   0.4%/193|   0.3%/268|   0.2%/295|   0.2%/325 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 170   |     321|      29.900|   1.1%/ 61|   1.2%/ 59|   1.2%/ 59|   1.2%/ 58 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 170   |    3057|     184.136|   0.5%/133|   0.4%/161|   0.4%/170|   0.4%/179 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 156   |      65|       5.320|   0.3%/222|   0.1%/546|   0.1%/871|   0.0%/ *** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 145   |      40|      25.037|   0.3%/226|   0.3%/247|   0.3%/254|   0.3%/263 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 166   |     222|      19.216|   0.4%/156|   0.4%/159|   0.4%/160|   0.4%/161 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 170   |    2184|     238.452|   0.7%/101|   0.5%/128|   0.5%/138|   0.5%/150 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 170   |     637|      65.159|   0.3%/215|   0.4%/180|   0.4%/173|   0.4%/166 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 170   |   84397|      62.001|   1.4%/ 48|   1.4%/ 50|   1.4%/ 50|   1.4%/ 51 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 170   |    9220|      34.545|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 170   |   23736|     284.685|   0.6%/124|   0.5%/127|   0.5%/127|   0.5%/127 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 170   |    8395|     214.546|   1.0%/ 71|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 170   |    1785|     362.596|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 170   |    1193|     129.837|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 170   |   35646|     591.753|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 170   |      50|      18.360|   4.7%/ 15|   4.8%/ 14|   4.8%/ 14|   4.9%/ 14 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 170   |    1507|      11.968|   0.8%/ 86|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 170   |      26|       2.394|   3.6%/ 19|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 170   |    1703|      91.131|   0.5%/151|   0.4%/188|   0.3%/200|   0.3%/213 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 170   |     645|      13.564|   0.6%/123|   0.5%/151|   0.4%/160|   0.4%/169 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 170   |     506|     281.555|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 167   |     571|     129.170|   0.5%/148|   0.5%/142|   0.5%/140|   0.5%/139 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 168   |    1025|     156.867|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 168   |      36|      18.693|   0.2%/358|   0.2%/434|   0.2%/460|   0.1%/490 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 170   |     271|      39.754|   2.8%/ 24|   2.7%/ 25|   2.7%/ 26|   2.7%/ 26 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 167   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 169   |     407|      59.295|   3.1%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 170   |      87|      31.287|   0.1%/765|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 124   |     218|       8.299|   0.7%/101|   0.6%/115|   0.6%/120|   0.6%/124 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 170   |     129|       3.931|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 170   |     128|       6.334|   0.1%/747|   0.1%/717|   0.1%/712|   0.1%/709 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 170   |     162|      39.613|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 170   |   73101|     577.521|   0.6%/108|   0.6%/119|   0.6%/122|   0.6%/125 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 170   |    1167|     435.112|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78|   0.9%/ 77 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 170   |    1842|      51.335|   2.3%/ 30|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 116   |      39|       1.284|   3.3%/ 21|   3.8%/ 18|   3.9%/ 18|   4.0%/ 17 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  70   |     109|      44.341|   1.8%/ 38|   2.0%/ 34|   2.0%/ 34|   2.1%/ 33 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 125   |     402|      13.397|   3.1%/ 23|   2.5%/ 28|   2.3%/ 30|   2.2%/ 32 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 170   |    6310|     361.437|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 170   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 170   |     147|      22.822|   0.4%/188|   0.4%/188|   0.4%/188|   0.4%/187 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 170   |      69|       3.092|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 170   |    1098|       5.327|   0.4%/194|   0.4%/196|   0.4%/197|   0.4%/197 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 170   |     668|     321.762|   0.7%/ 96|   0.7%/ 93|   0.8%/ 92|   0.8%/ 91 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 170   |     265|      49.429|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 170   |     815|     174.735|   1.1%/ 64|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 170   |    6417|      29.259|   0.1%/766|   0.1%/883|   0.1%/918|   0.1%/956 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 170   |    2229|     528.439|   0.6%/125|   0.5%/141|   0.5%/145|   0.5%/150 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  53   |       6|       0.695|   1.7%/ 42|   2.6%/ 26|   2.8%/ 25|   2.9%/ 24 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 170   |     659|      92.098|   3.3%/ 21|   2.6%/ 26|   2.5%/ 28|   2.3%/ 30 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 170   |   31343|     975.463|   0.4%/160|   0.4%/181|   0.4%/188|   0.4%/194 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 170   |    4739|      43.675|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 170   |    2248|      58.561|   0.6%/124|   0.6%/124|   0.6%/124|   0.6%/123 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 170   |    1879|     182.801|   0.2%/336|   0.2%/316|   0.2%/311|   0.2%/306 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 170   |     209|      75.993|   0.3%/228|   0.3%/223|   0.3%/222|   0.3%/221 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 170   |    4380|     225.708|   1.0%/ 69|   0.9%/ 75|   0.9%/ 76|   0.9%/ 78 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 170   |   18968|     129.259|   0.6%/117|   0.6%/117|   0.6%/117|   0.6%/118 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 111   |      24|       1.912|   1.7%/ 41|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 170   |    4420|     129.171|   0.7%/ 99|   0.7%/106|   0.6%/107|   0.6%/109 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 170   |     304|      18.738|   0.3%/226|   0.2%/337|   0.2%/383|   0.2%/443 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 170   |     741|     106.479|   0.2%/406|   0.1%/557|   0.1%/612|   0.1%/677 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 148   |      73|       9.179|   0.1%/555|   0.1%/725|   0.1%/796|   0.1%/886 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 170   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 170   |      39|       7.143|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 170   |     136|      65.040|   0.1%/957|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 163   |      99|       6.211|   0.1%/896|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 170   |   16113|     274.146|   0.6%/119|   0.4%/157|   0.4%/170|   0.4%/186 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 170   |   29973|     636.357|   0.2%/365|   0.2%/332|   0.2%/325|   0.2%/318 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 170   |      13|       0.579|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 170   |     840|      19.790|   0.1%/998|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 170   |    5857|     566.560|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 170   |    2027|     235.593|   0.1%/ ***|   0.1%/994|   0.1%/977|   0.1%/959 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 170   |     175|      10.011|   2.1%/ 32|   1.9%/ 36|   1.8%/ 38|   1.8%/ 39 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 170   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 170   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 170   |      40|       5.292|   2.1%/ 32|   2.6%/ 27|   2.7%/ 26|   2.8%/ 25 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 170   |      66|      48.023|   5.9%/ 12|   5.8%/ 12|   5.7%/ 12|   5.7%/ 12 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 170   |     117|       9.957|   3.4%/ 20|   3.9%/ 18|   4.0%/ 17|   4.1%/ 17 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 170   |    7217|      86.787|   0.8%/ 84|   0.9%/ 76|   0.9%/ 75|   0.9%/ 73 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 170   |  198011|     600.863|   0.4%/167|   0.4%/177|   0.4%/179|   0.4%/182 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  56   |      62|       1.529|   4.1%/ 17|   3.3%/ 21|   3.2%/ 22|   3.0%/ 23 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 170   |    3446|      82.290|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 170   |     404|      40.819|   0.3%/247|   0.3%/262|   0.3%/266|   0.3%/271 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 170   |   41766|     628.673|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 170   |      46|      13.128|   0.1%/504|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 170   |     419|      12.275|   1.5%/ 45|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 170   |     524|      16.253|   1.8%/ 39|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  49   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 169   |     320|      17.919|   0.8%/ 90|   0.8%/ 83|   0.9%/ 81|   0.9%/ 79 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 170   |     243|      16.017|   0.4%/159|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |

