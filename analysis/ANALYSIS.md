# State and Country COVID-19 Analysis #
## Updated: at 2020-09-01 for data as of 2020-08-31 ##

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
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 153   |   32957|    1694.150|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 153   |   15955|    1796.331|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 153   |   13243|     335.172|   1.0%/ 71|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 153   |   13413|     462.580|   1.4%/ 49|   1.2%/ 58|   1.1%/ 61|   1.1%/ 64 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 153   |   11622|     541.139|   1.2%/ 58|   1.0%/ 73|   0.9%/ 78|   0.8%/ 83 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 153   |    9059|    1303.615|   0.2%/398|   0.2%/390|   0.2%/388|   0.2%/386 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 153   |    8247|     650.836|   0.2%/298|   0.2%/297|   0.2%/296|   0.2%/296 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 153   |    7686|     600.405|   0.2%/347|   0.2%/363|   0.2%/368|   0.2%/373 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 153   |    6743|     675.188|   0.2%/427|   0.2%/409|   0.2%/405|   0.2%/400 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 153   |    5700|     536.820|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 153   |  184979|     561.318|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/149 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 153   |  122790|     580.810|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 153   |   66363|      48.753|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 153   |   65333|     516.151|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 95 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 153   |   41254|     620.961|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 153   |   35524|     589.723|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 153   |   30624|     456.563|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 153   |   29055|     616.883|   0.1%/872|   0.1%/785|   0.1%/766|   0.1%/749 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 153   |   30260|     941.768|   0.7%/106|   0.6%/121|   0.6%/126|   0.5%/131 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 153   |   21853|     262.099|   0.6%/111|   0.5%/131|   0.5%/138|   0.5%/145 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 153   |    2176|     443.736|   0.9%/ 76|   0.9%/ 80|   0.9%/ 80|   0.9%/ 81 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 153   |      37|      51.058|   0.6%/107|   0.4%/165|   0.4%/192|   0.3%/230 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 153   |    5128|     704.560|   0.8%/ 88|   0.7%/106|   0.6%/111|   0.6%/117 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 153   |     793|     262.690|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 153   |   13243|     335.172|   1.0%/ 71|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 153   |    1948|     338.195|   0.2%/365|   0.2%/373|   0.2%/376|   0.2%/378 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 153   |    4469|    1253.399|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 153   |     606|     622.323|   0.1%/628|   0.1%/650|   0.1%/657|   0.1%/665 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 153   |   11622|     541.139|   1.2%/ 58|   1.0%/ 73|   0.9%/ 78|   0.8%/ 83 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 153   |    5700|     536.820|   1.3%/ 53|   1.3%/ 55|   1.3%/ 55|   1.2%/ 55 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 153   |      62|      43.869|   3.7%/ 19|   4.2%/ 17|   4.3%/ 16|   4.4%/ 16 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 153   |     370|     206.767|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 153   |    8247|     650.836|   0.2%/298|   0.2%/297|   0.2%/296|   0.2%/296 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 153   |    3314|     492.262|   0.3%/204|   0.3%/214|   0.3%/217|   0.3%/221 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 153   |    1119|     354.627|   0.9%/ 80|   0.9%/ 78|   0.9%/ 78|   0.9%/ 77 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 153   |     455|     156.083|   0.7%/ 99|   0.7%/105|   0.7%/106|   0.6%/108 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 153   |     937|     209.777|   0.9%/ 79|   0.9%/ 76|   0.9%/ 76|   0.9%/ 75 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 153   |    5013|    1078.311|   0.6%/107|   0.6%/119|   0.6%/122|   0.6%/126 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 153   |     133|      98.816|   0.2%/282|   0.2%/291|   0.2%/295|   0.2%/298 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 153   |    3758|     621.520|   0.2%/319|   0.2%/326|   0.2%/328|   0.2%/329 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 153   |    9059|    1303.615|   0.2%/398|   0.2%/390|   0.2%/388|   0.2%/386 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 153   |    6743|     675.188|   0.2%/427|   0.2%/409|   0.2%/405|   0.2%/400 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 153   |    1879|     333.099|   0.4%/156|   0.4%/159|   0.4%/160|   0.4%/161 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 153   |    2498|     839.467|   1.1%/ 63|   1.0%/ 69|   1.0%/ 71|   1.0%/ 73 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 153   |    1537|     250.416|   0.7%/ 97|   0.7%/ 93|   0.8%/ 92|   0.8%/ 90 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 153   |     106|      98.891|   1.6%/ 42|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 153   |     398|     205.807|   0.6%/122|   0.5%/129|   0.5%/131|   0.5%/133 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 153   |    1351|     438.744|   1.3%/ 52|   1.2%/ 59|   1.1%/ 61|   1.1%/ 63 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 153   |     433|     318.543|   0.1%/521|   0.1%/538|   0.1%/543|   0.1%/549 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 153   |   15955|    1796.331|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 153   |     781|     372.294|   0.6%/125|   0.5%/133|   0.5%/136|   0.5%/138 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 153   |   32957|    1694.150|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 153   |    2736|     260.880|   0.9%/ 75|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 153   |     146|     191.644|   0.9%/ 74|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 153   |    4163|     356.184|   0.5%/127|   0.5%/130|   0.5%/131|   0.5%/132 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 153   |     812|     205.119|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 153   |     462|     109.496|   1.2%/ 59|   1.2%/ 60|   1.1%/ 60|   1.1%/ 60 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 153   |    7686|     600.405|   0.2%/347|   0.2%/363|   0.2%/368|   0.2%/373 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 153   |     455|     142.509|   1.9%/ 36|   1.7%/ 40|   1.7%/ 41|   1.6%/ 43 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 153   |    1047|     987.950|   0.2%/417|   0.2%/376|   0.2%/366|   0.2%/358 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 153   |    2783|     540.441|   1.2%/ 56|   1.1%/ 63|   1.1%/ 65|   1.0%/ 67 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 153   |     169|     190.902|   0.6%/109|   0.6%/122|   0.6%/125|   0.5%/129 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 153   |    1789|     261.752|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44|   1.6%/ 45 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 153   |   13413|     462.580|   1.4%/ 49|   1.2%/ 58|   1.1%/ 61|   1.1%/ 64 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 153   |  184979|     561.318|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/149 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 153   |     417|     129.951|   0.7%/ 93|   0.6%/110|   0.6%/115|   0.6%/121 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 153   |      58|      93.137|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 153   |    2573|     301.481|   0.5%/132|   0.5%/128|   0.5%/126|   0.6%/125 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 153   |    1946|     255.494|   0.5%/145|   0.4%/178|   0.4%/190|   0.3%/203 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 153   |     214|     119.242|   2.2%/ 31|   2.3%/ 30|   2.3%/ 30|   2.3%/ 29 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 153   |    1132|     194.418|   0.5%/129|   0.5%/139|   0.5%/142|   0.5%/144 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 141   |      39|      67.642|   0.2%/296|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 153   |    1419|      44.048|   0.2%/383|   0.1%/681|   0.1%/849|   0.1%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 153   |     287|     100.728|   1.6%/ 44|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 153   |    1517|      35.268|   0.6%/107|   0.6%/113|   0.6%/115|   0.6%/117 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 153   |     114|       3.670|   1.4%/ 49|   1.0%/ 67|   0.9%/ 74|   0.8%/ 82 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 153   |    8962|     199.419|   2.7%/ 25|   2.6%/ 27|   2.6%/ 27|   2.5%/ 27 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 153   |     884|     299.000|   0.4%/155|   0.4%/174|   0.4%/180|   0.4%/185 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 153   |     685|      26.654|   3.1%/ 22|   2.8%/ 24|   2.8%/ 25|   2.7%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 153   |     735|      82.615|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 153   |     535|      53.141|   0.3%/204|   0.3%/259|   0.3%/275|   0.2%/293 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 153   |     194|     125.897|   0.6%/108|   0.5%/134|   0.5%/143|   0.4%/154 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 153   |    4294|      25.490|   1.1%/ 66|   1.1%/ 66|   1.1%/ 66|   1.1%/ 66 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 153   |     677|      72.005|   0.7%/ 96|   0.8%/ 90|   0.8%/ 89|   0.8%/ 87 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 153   |   10053|     872.326|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 148   |      40|       3.421|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 153   |    5095|     444.185|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 153   |     624|     189.157|   1.6%/ 44|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 153   |       4|       1.727|   5.4%/ 13|   6.6%/ 10|   6.9%/ 10|   7.3%/  9 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 153   |  122790|     580.810|   0.8%/ 88|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 153   |     627|      90.209|   1.4%/ 48|   1.4%/ 51|   1.4%/ 51|   1.3%/ 51 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 153   |      55|       2.650|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 141   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 153   |     414|      15.591|   0.1%/474|   0.1%/591|   0.1%/634|   0.1%/686 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 153   |    9173|     241.397|   0.1%/982|   0.1%/978|   0.1%/977|   0.1%/976 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 101   |      61|      11.138|   0.1%/ ***|   0.1%/967|   0.1%/875|   0.1%/790 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 126   |      77|       4.739|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 153   |   11315|     592.179|   0.5%/135|   0.5%/141|   0.5%/143|   0.5%/144 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 153   |    4723|       3.368|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 153   |   20107|     407.051|   1.8%/ 39|   1.6%/ 43|   1.6%/ 44|   1.5%/ 46 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 153   |     452|      89.373|   2.5%/ 27|   2.1%/ 32|   2.0%/ 34|   1.9%/ 36 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 153   |     183|      44.929|   0.8%/ 84|   0.9%/ 78|   0.9%/ 76|   0.9%/ 75 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 153   |      93|       8.263|   0.4%/159|   0.6%/126|   0.6%/119|   0.6%/113 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 153   |     625|     107.273|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 153   |    1721|     166.167|   1.1%/ 61|   1.1%/ 66|   1.0%/ 67|   1.0%/ 68 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 153   |    6558|     375.449|   0.5%/133|   0.6%/126|   0.6%/124|   0.6%/122 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 153   |    5420|      54.054|   0.3%/207|   0.3%/220|   0.3%/223|   0.3%/225 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 153   |     736|     113.454|   1.1%/ 63|   0.9%/ 78|   0.8%/ 82|   0.8%/ 87 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 132   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 149   |     854|       8.655|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 153   |     336|      60.757|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 153   |   30624|     456.563|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 153   |      54|      24.656|   0.1%/880|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 153   |     144|      61.144|   2.3%/ 30|   1.1%/ 65|   1.1%/ 65|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 150   |      19|       5.048|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 153   |    9310|     111.968|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 153   |     288|       9.500|   0.9%/ 73|   0.7%/ 98|   0.6%/108|   0.6%/120 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 153   |     262|      24.390|   1.0%/ 69|   1.1%/ 63|   1.1%/ 62|   1.1%/ 61 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 153   |    2808|     169.131|   1.0%/ 72|   0.8%/ 82|   0.8%/ 84|   0.8%/ 87 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 139   |      59|       4.832|   1.0%/ 70|   1.1%/ 62|   1.1%/ 60|   1.2%/ 59 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 128   |      35|      21.816|   0.3%/252|   0.2%/330|   0.2%/352|   0.2%/375 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 149   |     205|      17.698|   0.3%/235|   0.1%/717|   0.0%/ ***|   0.0%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 153   |    1844|     201.350|   1.2%/ 59|   1.3%/ 55|   1.3%/ 54|   1.3%/ 53 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 153   |     616|      63.068|   0.1%/959|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 153   |   66363|      48.753|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 153   |    7377|      27.637|   1.3%/ 55|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 153   |   21853|     262.099|   0.6%/111|   0.5%/131|   0.5%/138|   0.5%/145 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 153   |    7092|     181.264|   1.2%/ 58|   1.1%/ 60|   1.1%/ 61|   1.1%/ 61 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 153   |    1779|     361.464|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 153   |     958|     104.308|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 153   |   35524|     589.723|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 153   |      20|       7.421|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 153   |    1285|      10.199|   1.1%/ 65|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 153   |      15|       1.440|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 153   |    1636|      87.579|   1.0%/ 69|   0.9%/ 76|   0.9%/ 78|   0.9%/ 80 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 153   |     605|      12.724|   1.2%/ 60|   0.9%/ 79|   0.8%/ 86|   0.7%/ 94 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 153   |     533|     296.801|   1.3%/ 53|   0.8%/ 89|   0.6%/108|   0.5%/136 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 150   |     535|     120.994|   0.4%/164|   0.4%/189|   0.4%/197|   0.3%/205 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 151   |    1014|     155.187|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 151   |      34|      17.777|   0.3%/207|   0.4%/176|   0.4%/169|   0.4%/163 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 153   |     165|      24.161|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 150   |      83|      18.527|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 152   |     249|      36.270|   3.3%/ 21|   3.1%/ 22|   3.1%/ 23|   3.0%/ 23 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 153   |      86|      30.759|   0.3%/200|   0.4%/169|   0.4%/163|   0.4%/157 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 107   |     192|       7.311|   1.0%/ 71|   0.8%/ 89|   0.7%/ 93|   0.7%/ 97 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 153   |     125|       3.824|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 153   |     126|       6.216|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 153   |     158|      38.869|   0.1%/ ***|   0.1%/896|   0.1%/859|   0.1%/824 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 153   |   65333|     516.151|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 95 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 153   |    1003|     374.119|   0.7%/ 96|   0.7%/101|   0.7%/102|   0.7%/103 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 153   |    1192|      33.221|   3.6%/ 19|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  99   |      23|       0.749|   1.4%/ 51|   1.6%/ 43|   1.7%/ 41|   1.8%/ 39 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  53   |      75|      30.634|   6.0%/ 11|   5.0%/ 14|   4.8%/ 14|   4.6%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 108   |     227|       7.553|   5.4%/ 13|   5.7%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 153   |    6253|     358.199|   0.1%/ ***|   0.1%/998|   0.1%/975|   0.1%/953 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 153   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 153   |     139|      21.554|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 153   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 153   |    1028|       4.985|   0.2%/293|   0.1%/509|   0.1%/624|   0.1%/804 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 153   |     598|     288.054|   0.7%/ 98|   0.7%/ 93|   0.8%/ 91|   0.8%/ 90 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 153   |     266|      49.533|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 153   |     692|     148.324|   1.1%/ 60|   1.0%/ 67|   1.0%/ 69|   1.0%/ 71 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 153   |    6319|      28.808|   0.1%/535|   0.1%/690|   0.1%/743|   0.1%/805 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 153   |    2038|     483.006|   0.8%/ 84|   0.7%/100|   0.7%/105|   0.6%/111 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  36   |       5|       0.560|   0.7%/ 98|   4.7%/ 15|   5.0%/ 14|   5.0%/ 14 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 153   |     342|      47.782|   6.0%/ 11|   6.1%/ 11|   6.1%/ 11|   6.1%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 153   |   30260|     941.768|   0.7%/106|   0.6%/121|   0.6%/126|   0.5%/131 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 153   |    3518|      32.420|   2.3%/ 30|   2.5%/ 28|   2.5%/ 28|   2.5%/ 27 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 153   |    2050|      53.410|   0.6%/121|   0.6%/123|   0.6%/123|   0.6%/124 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 153   |    1823|     177.370|   0.2%/403|   0.2%/402|   0.2%/402|   0.2%/402 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 153   |     199|      72.358|   0.2%/345|   0.1%/718|   0.1%/969|   0.0%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 153   |    3657|     188.432|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 153   |   17207|     117.257|   0.6%/113|   0.6%/119|   0.6%/121|   0.6%/122 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  94   |      18|       1.429|   2.9%/ 24|   2.3%/ 30|   2.1%/ 32|   2.0%/ 35 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 153   |    3938|     115.077|   0.9%/ 76|   0.8%/ 82|   0.8%/ 83|   0.8%/ 85 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 153   |     290|      17.873|   0.8%/ 83|   0.7%/ 97|   0.7%/102|   0.6%/107 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 153   |     727|     104.423|   0.4%/193|   0.2%/346|   0.2%/430|   0.1%/568 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 131   |      70|       8.843|   0.1%/609|   0.1%/622|   0.1%/614|   0.1%/603 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 153   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 153   |      34|       6.169|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 153   |     134|      64.116|   0.1%/489|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 146   |      96|       6.020|   0.4%/173|   0.6%/125|   0.6%/117|   0.6%/109 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 153   |   14711|     250.299|   1.2%/ 58|   0.9%/ 80|   0.8%/ 88|   0.7%/ 97 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 153   |   29055|     616.883|   0.1%/872|   0.1%/785|   0.1%/766|   0.1%/749 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 153   |      12|       0.555|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 153   |     833|      19.623|   0.2%/365|   0.1%/613|   0.1%/740|   0.1%/933 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 153   |    5828|     563.727|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 153   |    2007|     233.246|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 153   |     115|       6.584|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 153   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 153   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 153   |      29|       3.809|   0.0%/ --|   0.0%/ --|   0.0%/ --|   1.2%/ 57 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 153   |      21|      15.112|   5.4%/ 13|   5.9%/ 12|   6.1%/ 11|   6.2%/ 11 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 153   |      78|       6.619|   1.3%/ 53|   1.5%/ 46|   1.5%/ 45|   1.6%/ 43 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 153   |    6296|      75.716|   0.4%/184|   0.4%/173|   0.4%/171|   0.4%/168 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 153   |  184979|     561.318|   0.5%/132|   0.5%/143|   0.5%/146|   0.5%/149 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  39   |      32|       0.784|   6.7%/ 10|   4.6%/ 15|   3.6%/ 19|   2.7%/ 25 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 153   |    2586|      61.740|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 153   |     383|      38.724|   0.3%/200|   0.4%/190|   0.4%/188|   0.4%/186 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 153   |   41254|     620.961|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 153   |      44|      12.642|   0.8%/ 82|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 153   |     328|       9.619|   2.1%/ 32|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 153   |     403|      12.522|   2.2%/ 31|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  32   |      34|       0.349|   2.7%/ 26|   3.1%/ 23|   3.1%/ 22|   3.2%/ 22 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 152   |     309|      17.261|   0.6%/114|   0.4%/188|   0.3%/225|   0.2%/281 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 153   |     209|      13.818|   2.5%/ 28|   1.8%/ 38|   1.7%/ 41|   1.5%/ 46 |

