# State and Country COVID-19 Analysis #
## Updated: at 2020-08-21 for data as of 2020-08-20 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.8% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.6% of deaths and 58.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 142   |   32877|    1690.011|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 142   |   15936|    1794.120|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 142   |   11894|     301.033|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 142   |   11775|     406.087|   1.9%/ 36|   1.6%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 142   |   10293|     479.264|   1.9%/ 36|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 142   |    8890|    1279.220|   0.2%/437|   0.2%/449|   0.2%/452|   0.2%/455 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 142   |    8031|     633.732|   0.2%/304|   0.2%/298|   0.2%/297|   0.2%/295 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 142   |    7509|     586.566|   0.2%/302|   0.2%/285|   0.2%/282|   0.2%/278 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 142   |    6623|     663.214|   0.1%/469|   0.2%/442|   0.2%/435|   0.2%/429 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 142   |    4940|     465.303|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 142   |  174769|     530.336|   0.6%/110|   0.6%/115|   0.6%/117|   0.6%/119 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 142   |  112619|     532.702|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 142   |   59723|     471.831|   1.1%/ 61|   1.0%/ 66|   1.0%/ 67|   1.0%/ 69 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 142   |   55372|      40.678|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 142   |   47102|     708.989|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 142   |   35391|     587.507|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 142   |   30449|     453.940|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 142   |   28668|     608.657|   0.1%/ ***|   0.1%/963|   0.1%/921|   0.1%/881 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 142   |   27111|     843.764|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 142   |   20515|     246.048|   0.9%/ 77|   0.8%/ 87|   0.8%/ 90|   0.7%/ 93 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 142   |    2011|     410.162|   1.0%/ 72|   0.8%/ 88|   0.7%/ 93|   0.7%/ 99 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 142   |      30|      40.434|   1.2%/ 55|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 142   |    4765|     654.630|   1.1%/ 62|   0.9%/ 78|   0.8%/ 83|   0.8%/ 89 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 142   |     652|     216.019|   1.6%/ 42|   1.5%/ 46|   1.5%/ 48|   1.4%/ 49 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 142   |   11894|     301.033|   1.2%/ 56|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 142   |    1909|     331.542|   0.2%/377|   0.2%/446|   0.1%/466|   0.1%/488 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 142   |    4460|    1251.005|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 142   |     597|     613.378|   0.1%/841|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 142   |   10293|     479.264|   1.9%/ 36|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 142   |    4940|     465.303|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 142   |      44|      30.735|   1.6%/ 42|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 142   |     303|     169.351|   2.2%/ 32|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 142   |    8031|     633.732|   0.2%/304|   0.2%/298|   0.2%/297|   0.2%/295 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 142   |    3181|     472.549|   0.4%/171|   0.4%/161|   0.4%/159|   0.4%/157 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 142   |    1014|     321.537|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81|   0.9%/ 81 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 142   |     422|     144.843|   0.8%/ 91|   0.7%/ 99|   0.7%/102|   0.7%/104 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 142   |     840|     187.912|   0.8%/ 86|   0.9%/ 81|   0.9%/ 79|   0.9%/ 78 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 142   |    4648|     999.832|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 142   |     128|      95.343|   0.2%/363|   0.1%/482|   0.1%/524|   0.1%/573 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 142   |    3679|     608.471|   0.2%/306|   0.2%/338|   0.2%/348|   0.2%/359 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 142   |    8890|    1279.220|   0.2%/437|   0.2%/449|   0.2%/452|   0.2%/455 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 142   |    6623|     663.214|   0.1%/469|   0.2%/442|   0.2%/435|   0.2%/429 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 142   |    1778|     315.314|   0.5%/138|   0.6%/124|   0.6%/121|   0.6%/118 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 142   |    2219|     745.507|   1.4%/ 51|   1.3%/ 55|   1.2%/ 56|   1.2%/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 142   |    1434|     233.614|   0.7%/ 97|   0.7%/ 94|   0.7%/ 93|   0.8%/ 92 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 142   |      92|      86.208|   1.6%/ 44|   1.1%/ 63|   1.0%/ 71|   0.8%/ 81 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 142   |     373|     192.614|   0.7%/103|   0.7%/100|   0.7%/ 99|   0.7%/ 98 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 142   |    1156|     375.267|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 142   |     426|     313.636|   0.2%/461|   0.1%/497|   0.1%/503|   0.1%/508 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 142   |   15936|    1794.120|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 142   |     735|     350.554|   0.7%/106|   0.6%/114|   0.6%/116|   0.6%/118 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 142   |   32877|    1690.011|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 142   |    2476|     236.079|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 71 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 142   |     130|     170.337|   1.3%/ 54|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 142   |    3929|     336.132|   0.6%/115|   0.6%/121|   0.6%/123|   0.6%/124 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 142   |     701|     177.215|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 142   |     413|      97.875|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 142   |    7509|     586.566|   0.2%/302|   0.2%/285|   0.2%/282|   0.2%/278 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 142   |     365|     114.163|   2.6%/ 27|   2.7%/ 26|   2.7%/ 25|   2.7%/ 25 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 142   |    1026|     968.634|   0.1%/655|   0.1%/612|   0.1%/601|   0.1%/589 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 142   |    2461|     478.075|   1.6%/ 43|   1.3%/ 52|   1.3%/ 55|   1.2%/ 58 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 142   |     159|     179.309|   0.8%/ 86|   0.7%/100|   0.7%/104|   0.6%/109 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 142   |    1473|     215.548|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 142   |   11775|     406.087|   1.9%/ 36|   1.6%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 142   |  174769|     530.336|   0.6%/110|   0.6%/115|   0.6%/117|   0.6%/119 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 142   |     384|     119.740|   1.0%/ 66|   0.9%/ 76|   0.9%/ 80|   0.8%/ 83 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 142   |      58|      93.602|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 142   |    2449|     286.961|   0.4%/155|   0.4%/197|   0.3%/212|   0.3%/230 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 142   |    1836|     241.076|   0.8%/ 90|   0.8%/ 89|   0.8%/ 88|   0.8%/ 88 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 142   |     172|      95.825|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 142   |    1068|     183.479|   0.6%/111|   0.6%/122|   0.6%/125|   0.5%/128 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 130   |      32|      55.018|   0.9%/ 76|   0.9%/ 74|   0.9%/ 74|   0.9%/ 74 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 142   |    1392|      43.191|   0.4%/183|   0.3%/203|   0.3%/209|   0.3%/215 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 142   |     248|      87.042|   1.8%/ 38|   1.5%/ 45|   1.4%/ 48|   1.4%/ 50 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 142   |    1416|      32.938|   0.8%/ 92|   0.7%/ 97|   0.7%/ 98|   0.7%/ 99 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 142   |     101|       3.244|   2.3%/ 30|   1.9%/ 37|   1.7%/ 40|   1.6%/ 42 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 142   |    6547|     145.685|   3.1%/ 22|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 142   |     845|     285.789|   0.6%/123|   0.5%/150|   0.4%/158|   0.4%/167 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 142   |     502|      19.540|   4.3%/ 16|   4.2%/ 16|   4.1%/ 17|   4.1%/ 17 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 142   |     730|      81.978|   0.1%/749|   0.1%/736|   0.1%/733|   0.1%/730 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 142   |     525|      52.169|   0.5%/146|   0.2%/349|   0.1%/530|   0.1%/ *** |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 142   |     179|     116.145|   1.0%/ 70|   1.0%/ 72|   1.0%/ 72|   0.9%/ 73 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 142   |    3823|      22.692|   1.0%/ 66|   1.0%/ 68|   1.0%/ 69|   1.0%/ 69 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 142   |     626|      66.484|   0.6%/123|   0.5%/133|   0.5%/136|   0.5%/138 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 142   |    9960|     864.249|   0.1%/866|   0.1%/732|   0.1%/704|   0.1%/678 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 137   |      40|       3.368|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 142   |    4426|     385.891|   1.6%/ 42|   1.4%/ 51|   1.3%/ 54|   1.2%/ 57 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 142   |     525|     159.092|   1.8%/ 38|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 142   |       3|       1.339|   2.6%/ 26|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 142   |  112619|     532.702|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 142   |     542|      77.988|   1.6%/ 43|   1.5%/ 47|   1.4%/ 48|   1.4%/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 142   |      55|       2.633|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 130   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 142   |     406|      15.284|   0.3%/277|   0.3%/244|   0.3%/237|   0.3%/229 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 142   |    9101|     239.494|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  90   |      61|      11.184|   0.2%/350|   0.1%/791|   0.1%/ ***|   0.0%/ *** |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 115   |      76|       4.692|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 142   |   10730|     561.543|   0.5%/128|   0.5%/148|   0.4%/154|   0.4%/161 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 142   |    4709|       3.358|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 142   |   16782|     339.749|   2.3%/ 31|   2.0%/ 35|   1.9%/ 36|   1.8%/ 38 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 142   |     362|      71.641|   3.5%/ 20|   2.9%/ 24|   2.7%/ 25|   2.6%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 142   |     171|      41.938|   0.6%/113|   0.4%/156|   0.4%/171|   0.4%/190 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 142   |      88|       7.878|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 142   |     622|     106.888|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 142   |    1532|     147.912|   1.4%/ 49|   1.4%/ 51|   1.4%/ 51|   1.3%/ 51 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 142   |    6189|     354.280|   0.4%/179|   0.3%/199|   0.3%/204|   0.3%/209 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 142   |    5260|      52.458|   0.4%/191|   0.3%/260|   0.2%/284|   0.2%/314 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 142   |     662|     102.022|   1.6%/ 42|   1.4%/ 50|   1.3%/ 52|   1.3%/ 55 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 121   |      86|      63.620|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 138   |     628|       6.361|   3.9%/ 18|   3.8%/ 18|   3.8%/ 18|   3.7%/ 18 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 142   |     334|      60.497|   0.1%/996|   0.1%/967|   0.1%/964|   0.1%/962 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 142   |   30449|     453.940|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 142   |      53|      24.241|   0.3%/213|   0.3%/204|   0.3%/200|   0.4%/196 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 142   |      81|      34.502|  16.0%/  4|   5.3%/ 13|   6.9%/ 10|   8.7%/  8 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 139   |      17|       4.597|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 142   |    9258|     111.339|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 142   |     255|       8.412|   1.9%/ 36|   2.1%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 142   |     232|      21.649|   0.8%/ 87|   0.9%/ 74|   1.0%/ 71|   1.0%/ 68 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 142   |    2531|     152.423|   1.2%/ 57|   1.0%/ 67|   1.0%/ 71|   0.9%/ 74 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 128   |      53|       4.317|   0.7%/105|   0.6%/112|   0.6%/113|   0.6%/114 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 117   |      33|      20.748|   1.0%/ 69|   1.1%/ 65|   1.1%/ 64|   1.1%/ 64 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 138   |     202|      17.448|   0.9%/ 79|   0.8%/ 88|   0.8%/ 91|   0.7%/ 95 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 142   |    1674|     182.782|   0.8%/ 85|   0.4%/170|   0.3%/224|   0.2%/325 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 142   |     610|      62.418|   0.1%/642|   0.1%/600|   0.1%/594|   0.1%/588 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 142   |   55372|      40.678|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 142   |    6450|      24.164|   1.1%/ 64|   1.0%/ 69|   1.0%/ 70|   1.0%/ 72 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 142   |   20515|     246.048|   0.9%/ 77|   0.8%/ 87|   0.8%/ 90|   0.7%/ 93 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 142   |    6223|     159.041|   1.3%/ 52|   1.3%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 142   |    1777|     361.077|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 142   |     736|      80.130|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 142   |   35391|     587.507|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 142   |      15|       5.490|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 142   |    1123|       8.916|   0.8%/ 83|   1.0%/ 68|   1.1%/ 65|   1.1%/ 62 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 142   |      11|       1.032|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 142   |    1505|      80.560|   1.8%/ 38|   2.4%/ 29|   2.5%/ 27|   2.7%/ 26 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 142   |     528|      11.102|   1.8%/ 38|   1.5%/ 46|   1.4%/ 49|   1.3%/ 52 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 142   |     451|     250.987|   2.2%/ 32|   1.5%/ 47|   1.3%/ 53|   1.1%/ 61 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 139   |     513|     116.008|   0.6%/118|   0.5%/130|   0.5%/134|   0.5%/138 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 140   |    1525|     233.413|   0.2%/287|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 140   |      33|      17.109|   0.3%/242|   0.3%/199|   0.4%/189|   0.4%/180 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 142   |     115|      16.794|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 139   |      84|      18.732|   0.4%/193|   0.2%/324|   0.2%/396|   0.1%/513 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 141   |     181|      26.311|   3.9%/ 18|   3.7%/ 18|   3.7%/ 18|   3.7%/ 19 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 142   |      81|      29.144|   0.1%/966|   0.1%/946|   0.1%/947|   0.1%/948 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  96   |     183|       6.989|   2.1%/ 32|   1.3%/ 52|   1.1%/ 62|   0.9%/ 76 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 142   |     125|       3.824|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 142   |     125|       6.189|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 142   |     157|      38.622|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 142   |   59723|     471.831|   1.1%/ 61|   1.0%/ 66|   1.0%/ 67|   1.0%/ 69 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 142   |     929|     346.535|   0.8%/ 87|   0.7%/ 96|   0.7%/ 98|   0.7%/101 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 142   |     766|      21.367|   4.0%/ 17|   4.3%/ 16|   4.4%/ 16|   4.4%/ 15 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  88   |      20|       0.677|   1.8%/ 39|   0.9%/ 79|   0.6%/109|   0.4%/179 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  42   |      41|      16.696|  11.1%/  6|   5.3%/ 13|   3.6%/ 19|   2.0%/ 35 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  97   |     126|       4.206|   4.6%/ 15|   4.7%/ 15|   4.7%/ 15|   4.7%/ 15 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 142   |    6201|     355.219|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 142   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 142   |     134|      20.697|   0.7%/ 99|   0.7%/102|   0.7%/102|   0.7%/103 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 142   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 142   |    1002|       4.860|   0.5%/142|   0.4%/176|   0.4%/188|   0.3%/201 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 142   |     560|     269.722|   0.6%/123|   0.4%/159|   0.4%/171|   0.4%/185 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 142   |     262|      48.724|   0.2%/462|   0.2%/355|   0.2%/335|   0.2%/317 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 142   |     624|     133.787|   1.6%/ 42|   1.6%/ 44|   1.5%/ 45|   1.5%/ 45 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 142   |    6237|      28.437|   0.2%/349|   0.2%/449|   0.1%/483|   0.1%/523 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 142   |    1880|     445.726|   1.2%/ 59|   1.0%/ 70|   0.9%/ 74|   0.9%/ 78 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  25   |       3|       0.336|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 142   |     157|      21.936|   6.4%/ 11|   7.1%/ 10|   7.2%/  9|   7.4%/  9 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 142   |   27111|     843.764|   0.9%/ 80|   0.8%/ 90|   0.7%/ 93|   0.7%/ 96 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 142   |    2755|      25.388|   2.0%/ 35|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 142   |    1920|      50.028|   0.6%/117|   0.6%/113|   0.6%/112|   0.6%/111 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 142   |    1789|     174.041|   0.2%/408|   0.2%/405|   0.2%/404|   0.2%/403 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 142   |     197|      71.746|   0.5%/138|   0.4%/176|   0.4%/190|   0.3%/207 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 142   |    3166|     163.170|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46|   1.5%/ 46 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 142   |   16143|     110.007|   0.7%/100|   0.6%/109|   0.6%/111|   0.6%/114 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  83   |      11|       0.855|   4.6%/ 15|   7.7%/  9|   7.7%/  9|  11.2%/  6 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 142   |    3552|     103.804|   1.1%/ 66|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 142   |     266|      16.398|   1.1%/ 62|   1.0%/ 70|   1.0%/ 73|   0.9%/ 76 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 142   |     704|     101.146|   0.8%/ 90|   0.6%/121|   0.5%/133|   0.5%/148 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 120   |      70|       8.798|   0.1%/521|   0.1%/872|   0.1%/ ***|   0.0%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 142   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 142   |      32|       5.854|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 142   |     132|      63.170|   0.2%/289|   0.1%/557|   0.1%/746|   0.1%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 135   |      93|       5.852|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 142   |   13207|     224.713|   2.1%/ 34|   1.7%/ 41|   1.6%/ 43|   1.5%/ 46 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 142   |   28668|     608.657|   0.1%/ ***|   0.1%/963|   0.1%/921|   0.1%/881 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 142   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 142   |     816|      19.232|   0.4%/166|   0.4%/191|   0.3%/198|   0.3%/206 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 142   |    5803|     561.336|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 142   |    1995|     231.918|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 142   |      72|       4.124|   1.4%/ 48|   1.1%/ 62|   1.0%/ 66|   1.0%/ 71 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 142   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 142   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 142   |      29|       3.852|   1.6%/ 42|   1.4%/ 51|   1.3%/ 54|   1.2%/ 59 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 142   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 142   |      54|       4.577|   0.8%/ 85|   1.1%/ 65|   1.1%/ 61|   1.2%/ 58 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 142   |    6047|      72.718|   0.3%/217|   0.3%/210|   0.3%/208|   0.3%/206 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 142   |  174769|     530.336|   0.6%/110|   0.6%/115|   0.6%/117|   0.6%/119 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  28   |      18|       0.452|   9.4%/  7|   6.6%/ 10|   7.1%/ 10|   7.8%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 142   |    2210|      52.767|   1.3%/ 53|   1.3%/ 51|   1.4%/ 51|   1.4%/ 51 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 142   |     367|      37.079|   0.3%/236|   0.3%/217|   0.3%/212|   0.3%/207 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 142   |   47102|     708.989|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 142   |      40|      11.302|   0.8%/ 87|   0.9%/ 75|   1.0%/ 72|   1.0%/ 70 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 142   |     264|       7.730|   2.7%/ 26|   2.3%/ 30|   2.2%/ 31|   2.1%/ 32 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 142   |     318|       9.882|   3.2%/ 22|   3.1%/ 22|   3.1%/ 22|   3.1%/ 23 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  21   |      25|       0.260|  11.2%/  6|   2.8%/ 25|   1.4%/ 51|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 141   |     295|      16.482|   6.5%/ 10|   7.3%/  9|   7.4%/  9|   7.6%/  9 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 142   |     171|      11.309|   4.1%/ 17|   2.7%/ 25|   2.4%/ 29|   2.0%/ 34 |

