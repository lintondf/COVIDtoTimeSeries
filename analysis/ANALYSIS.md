# State and Country COVID-19 Analysis #
## Updated: at 2020-08-20 for data as of 2020-08-19 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.8% of deaths and 40.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.7% of deaths and 58.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 141   |   32871|    1689.721|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 141   |   15931|    1793.616|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 141   |   11763|     297.717|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 141   |   11611|     400.440|   1.9%/ 36|   1.6%/ 44|   1.5%/ 46|   1.4%/ 49 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 141   |   10131|     471.699|   2.0%/ 35|   1.8%/ 38|   1.8%/ 39|   1.7%/ 39 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 141   |    8876|    1277.204|   0.2%/439|   0.2%/454|   0.2%/458|   0.1%/462 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 141   |    8011|     632.156|   0.2%/317|   0.2%/317|   0.2%/317|   0.2%/318 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 141   |    7490|     585.081|   0.2%/314|   0.2%/301|   0.2%/298|   0.2%/294 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 141   |    6612|     662.077|   0.1%/493|   0.1%/471|   0.1%/465|   0.2%/460 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 141   |    4877|     459.295|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 141   |  173747|     527.235|   0.6%/111|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 141   |  111611|     527.934|   0.9%/ 73|   0.9%/ 79|   0.9%/ 80|   0.8%/ 82 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 141   |   59134|     467.175|   1.1%/ 61|   1.0%/ 67|   1.0%/ 68|   1.0%/ 70 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 141   |   54359|      39.934|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 141   |   47065|     708.434|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 141   |   35368|     587.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 141   |   30441|     453.823|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 141   |   28655|     608.382|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 141   |   26663|     829.823|   0.9%/ 78|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 141   |   20373|     244.352|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 141   |    1997|     407.355|   1.0%/ 70|   0.8%/ 85|   0.8%/ 90|   0.7%/ 96 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 141   |      29|      40.169|   1.3%/ 55|   1.2%/ 58|   1.2%/ 59|   1.1%/ 60 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 141   |    4727|     649.412|   1.1%/ 62|   0.9%/ 80|   0.8%/ 87|   0.7%/ 94 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 141   |     643|     213.061|   1.6%/ 43|   1.5%/ 48|   1.4%/ 49|   1.4%/ 51 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 141   |   11763|     297.717|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 63 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 141   |    1907|     331.103|   0.2%/359|   0.2%/422|   0.2%/440|   0.2%/459 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 141   |    4459|    1250.727|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 141   |     598|     613.773|   0.1%/850|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 141   |   10131|     471.699|   2.0%/ 35|   1.8%/ 38|   1.8%/ 39|   1.7%/ 39 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 141   |    4877|     459.295|   1.4%/ 51|   1.3%/ 51|   1.3%/ 52|   1.3%/ 52 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 141   |      42|      29.741|   1.2%/ 56|   1.4%/ 50|   1.4%/ 49|   1.4%/ 48 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 141   |     298|     166.642|   2.1%/ 32|   1.9%/ 36|   1.8%/ 37|   1.8%/ 39 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 141   |    8011|     632.156|   0.2%/317|   0.2%/317|   0.2%/317|   0.2%/318 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 141   |    3167|     470.474|   0.4%/181|   0.4%/174|   0.4%/173|   0.4%/171 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 141   |    1006|     318.889|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83|   0.8%/ 83 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 141   |     419|     143.927|   0.7%/ 94|   0.7%/106|   0.6%/110|   0.6%/114 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 141   |     832|     186.136|   0.7%/ 95|   0.7%/ 92|   0.8%/ 92|   0.8%/ 91 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 141   |    4612|     992.127|   0.8%/ 86|   0.8%/ 88|   0.8%/ 89|   0.8%/ 89 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 141   |     128|      95.178|   0.2%/365|   0.1%/508|   0.1%/562|   0.1%/631 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 141   |    3671|     607.286|   0.2%/306|   0.2%/341|   0.2%/352|   0.2%/364 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 141   |    8876|    1277.204|   0.2%/439|   0.2%/454|   0.2%/458|   0.1%/462 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 141   |    6612|     662.077|   0.1%/493|   0.1%/471|   0.1%/465|   0.2%/460 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 141   |    1768|     313.510|   0.5%/144|   0.5%/131|   0.5%/127|   0.6%/124 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 141   |    2193|     736.906|   1.4%/ 51|   1.2%/ 55|   1.2%/ 57|   1.2%/ 58 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 141   |    1423|     231.892|   0.7%/ 96|   0.7%/ 93|   0.7%/ 92|   0.8%/ 91 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 141   |      92|      85.822|   1.5%/ 45|   1.0%/ 68|   0.9%/ 78|   0.7%/ 93 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 141   |     370|     191.315|   0.6%/109|   0.6%/108|   0.6%/108|   0.6%/108 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 141   |    1133|     367.804|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 141   |     426|     313.083|   0.1%/543|   0.1%/694|   0.1%/739|   0.1%/788 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 141   |   15931|    1793.616|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 141   |     731|     348.460|   0.6%/107|   0.6%/117|   0.6%/119|   0.6%/122 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 141   |   32871|    1689.721|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 141   |    2451|     233.689|   1.1%/ 65|   1.0%/ 72|   0.9%/ 75|   0.9%/ 77 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 141   |     128|     168.114|   1.3%/ 54|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 141   |    3907|     334.208|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/134 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 141   |     691|     174.592|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 141   |     408|      96.711|   1.2%/ 58|   1.1%/ 62|   1.1%/ 64|   1.1%/ 65 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 141   |    7490|     585.081|   0.2%/314|   0.2%/301|   0.2%/298|   0.2%/294 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 141   |     355|     111.043|   2.5%/ 28|   2.6%/ 27|   2.6%/ 26|   2.6%/ 26 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 141   |    1025|     967.408|   0.1%/702|   0.1%/675|   0.1%/668|   0.1%/660 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 141   |    2434|     472.825|   1.6%/ 43|   1.3%/ 53|   1.2%/ 56|   1.2%/ 59 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 141   |     158|     178.098|   0.8%/ 84|   0.7%/ 98|   0.7%/102|   0.6%/107 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 141   |    1446|     211.627|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 141   |   11611|     400.440|   1.9%/ 36|   1.6%/ 44|   1.5%/ 46|   1.4%/ 49 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 141   |  173747|     527.235|   0.6%/111|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 141   |     381|     118.689|   1.0%/ 68|   0.8%/ 83|   0.8%/ 87|   0.7%/ 92 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 141   |      58|      93.624|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 141   |    2442|     286.052|   0.4%/155|   0.3%/198|   0.3%/215|   0.3%/235 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 141   |    1821|     239.192|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 141   |     169|      94.237|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 141   |    1062|     182.384|   0.6%/115|   0.5%/130|   0.5%/134|   0.5%/139 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 129   |      31|      53.670|   0.8%/ 84|   0.8%/ 84|   0.8%/ 85|   0.8%/ 86 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 141   |    1387|      43.043|   0.4%/177|   0.4%/195|   0.3%/200|   0.3%/206 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 141   |     244|      85.899|   1.9%/ 36|   1.7%/ 42|   1.6%/ 44|   1.5%/ 46 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 141   |    1407|      32.714|   0.8%/ 92|   0.7%/ 97|   0.7%/ 98|   0.7%/100 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 141   |     100|       3.200|   2.3%/ 30|   1.8%/ 37|   1.7%/ 40|   1.6%/ 43 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 141   |    6357|     141.459|   3.0%/ 23|   2.9%/ 24|   2.8%/ 24|   2.8%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 141   |     842|     284.729|   0.6%/120|   0.5%/147|   0.4%/156|   0.4%/166 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 141   |     480|      18.686|   4.5%/ 15|   4.5%/ 15|   4.4%/ 15|   4.4%/ 15 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 141   |     729|      81.914|   0.1%/683|   0.1%/638|   0.1%/628|   0.1%/617 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 141   |     525|      52.169|   0.5%/130|   0.2%/278|   0.2%/385|   0.1%/625 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 141   |     178|     115.054|   1.0%/ 71|   0.9%/ 74|   0.9%/ 75|   0.9%/ 75 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 141   |    3784|      22.464|   1.0%/ 67|   1.0%/ 70|   1.0%/ 70|   1.0%/ 71 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 141   |     622|      66.121|   0.5%/127|   0.5%/143|   0.5%/147|   0.5%/151 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 141   |    9950|     863.346|   0.1%/916|   0.1%/775|   0.1%/745|   0.1%/717 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 136   |      39|       3.366|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 141   |    4374|     381.329|   1.7%/ 41|   1.4%/ 49|   1.3%/ 52|   1.3%/ 55 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 141   |     516|     156.369|   1.8%/ 39|   1.7%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 141   |       3|       1.316|   3.0%/ 23|   2.7%/ 26|   2.6%/ 26|   2.6%/ 27 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 141   |  111611|     527.934|   0.9%/ 73|   0.9%/ 79|   0.9%/ 80|   0.8%/ 82 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 141   |     535|      76.968|   1.6%/ 42|   1.5%/ 45|   1.5%/ 46|   1.5%/ 47 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 141   |      55|       2.627|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 129   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 141   |     404|      15.237|   0.2%/304|   0.2%/278|   0.3%/271|   0.3%/265 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 141   |    9095|     239.350|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  89   |      61|      11.186|   0.2%/319|   0.1%/480|   0.1%/590|   0.1%/789 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 114   |      76|       4.694|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 141   |   10681|     558.979|   0.6%/125|   0.5%/146|   0.5%/152|   0.4%/159 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 141   |    4714|       3.361|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 141   |   16492|     333.877|   2.3%/ 30|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 141   |     355|      70.161|   3.5%/ 20|   2.9%/ 23|   2.8%/ 25|   2.7%/ 26 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 141   |     170|      41.783|   0.7%/106|   0.5%/144|   0.4%/158|   0.4%/174 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 141   |      88|       7.879|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 141   |     622|     106.864|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 141   |    1514|     146.146|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 141   |    6164|     352.850|   0.4%/188|   0.3%/219|   0.3%/228|   0.3%/238 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 141   |    5249|      52.348|   0.4%/181|   0.3%/246|   0.3%/269|   0.2%/297 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 141   |     654|     100.817|   1.7%/ 41|   1.5%/ 47|   1.4%/ 49|   1.3%/ 51 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 120   |      88|      64.523|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 137   |     605|       6.136|   3.8%/ 18|   3.7%/ 19|   3.7%/ 19|   3.6%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 141   |     334|      60.461|   0.1%/904|   0.1%/831|   0.1%/817|   0.1%/805 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 141   |   30441|     453.823|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 141   |      52|      24.157|   0.4%/189|   0.4%/175|   0.4%/171|   0.4%/166 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 141   |      77|      32.798|  23.2%/  3|   8.0%/  8|   5.3%/ 13|   6.9%/ 10 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 138   |      17|       4.605|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 141   |    9251|     111.262|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 141   |     249|       8.231|   1.8%/ 38|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 141   |     229|      21.390|   0.8%/ 88|   0.9%/ 73|   1.0%/ 70|   1.0%/ 67 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 141   |    2505|     150.894|   1.2%/ 58|   1.0%/ 71|   0.9%/ 75|   0.9%/ 80 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 127   |      52|       4.287|   0.6%/116|   0.5%/138|   0.5%/145|   0.5%/152 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 116   |      33|      20.465|   1.3%/ 53|   1.6%/ 44|   1.6%/ 43|   1.7%/ 41 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 137   |     201|      17.346|   1.0%/ 71|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 141   |    1672|     182.522|   0.9%/ 80|   0.4%/166|   0.3%/224|   0.2%/342 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 141   |     609|      62.356|   0.1%/616|   0.1%/553|   0.1%/542|   0.1%/532 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 141   |   54359|      39.934|   2.0%/ 34|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 141   |    6389|      23.936|   1.1%/ 64|   1.0%/ 70|   1.0%/ 71|   0.9%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 141   |   20373|     244.352|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 141   |    6147|     157.093|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 141   |    1777|     360.984|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 141   |     723|      78.733|   1.8%/ 39|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 141   |   35368|     587.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 141   |      15|       5.428|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 141   |    1111|       8.818|   0.8%/ 92|   0.9%/ 75|   1.0%/ 72|   1.0%/ 69 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 141   |      11|       1.032|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 141   |    1481|      79.277|   1.5%/ 45|   2.0%/ 34|   2.1%/ 32|   2.3%/ 30 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 141   |     521|      10.952|   1.8%/ 38|   1.4%/ 48|   1.4%/ 51|   1.3%/ 55 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 141   |     444|     247.096|   2.5%/ 28|   1.9%/ 36|   1.7%/ 40|   1.6%/ 43 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 138   |     510|     115.461|   0.6%/114|   0.6%/126|   0.5%/129|   0.5%/132 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 139   |    1524|     233.215|   0.3%/245|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 139   |      32|      17.044|   0.2%/343|   0.2%/305|   0.2%/296|   0.2%/286 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 141   |     111|      16.280|   3.4%/ 20|   3.5%/ 20|   3.5%/ 19|   3.5%/ 19 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 138   |      84|      18.721|   0.4%/168|   0.3%/252|   0.2%/291|   0.2%/345 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 140   |     175|      25.487|   4.0%/ 17|   3.9%/ 17|   3.9%/ 18|   3.9%/ 18 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 141   |      81|      29.088|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  95   |     181|       6.906|   2.3%/ 30|   1.5%/ 46|   1.3%/ 53|   1.1%/ 64 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 141   |     125|       3.825|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 141   |     125|       6.190|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 141   |     157|      38.595|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 141   |   59134|     467.175|   1.1%/ 61|   1.0%/ 67|   1.0%/ 68|   1.0%/ 70 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 141   |     923|     344.185|   0.8%/ 83|   0.8%/ 89|   0.8%/ 91|   0.7%/ 92 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 141   |     730|      20.345|   3.9%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  87   |      20|       0.668|   1.9%/ 36|   0.8%/ 85|   0.5%/131|   0.2%/299 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  41   |      40|      16.281|  10.7%/  6|   6.5%/ 11|   4.2%/ 16|   1.8%/ 38 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  96   |     120|       4.017|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 141   |    6197|     354.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 141   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 141   |     133|      20.589|   0.6%/108|   0.6%/119|   0.6%/122|   0.6%/126 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 141   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 141   |     998|       4.843|   0.5%/140|   0.4%/177|   0.4%/190|   0.3%/205 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 141   |     558|     268.740|   0.6%/117|   0.5%/151|   0.4%/162|   0.4%/176 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 141   |     261|      48.554|   0.1%/828|   0.1%/656|   0.1%/622|   0.1%/591 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 141   |     615|     131.876|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 141   |    6229|      28.402|   0.2%/341|   0.2%/449|   0.1%/487|   0.1%/531 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 141   |    1865|     442.015|   1.2%/ 57|   1.0%/ 69|   1.0%/ 72|   0.9%/ 76 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  24   |       3|       0.336|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 141   |     126|      17.587|   6.6%/ 10|   7.4%/  9|   7.6%/  9|   7.8%/  9 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 141   |   26663|     829.823|   0.9%/ 78|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 141   |    2683|      24.729|   1.9%/ 37|   2.1%/ 33|   2.2%/ 32|   2.3%/ 31 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 141   |    1908|      49.709|   0.6%/120|   0.6%/116|   0.6%/115|   0.6%/114 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 141   |    1786|     173.757|   0.2%/410|   0.2%/409|   0.2%/408|   0.2%/407 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 141   |     197|      71.558|   0.6%/123|   0.5%/144|   0.5%/152|   0.4%/160 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 141   |    3120|     160.786|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 141   |   16046|     109.343|   0.7%/100|   0.6%/110|   0.6%/113|   0.6%/116 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  82   |      10|       0.795|   4.6%/ 15|   0.0%/ --|   7.7%/  9|   7.7%/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 141   |    3515|     102.724|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 141   |     263|      16.251|   1.2%/ 59|   1.1%/ 65|   1.0%/ 67|   1.0%/ 69 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 141   |     701|     100.701|   0.8%/ 85|   0.6%/114|   0.6%/125|   0.5%/139 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 119   |      69|       8.796|   0.2%/457|   0.1%/636|   0.1%/720|   0.1%/839 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 141   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 141   |      32|       5.800|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 141   |     132|      63.172|   0.3%/243|   0.2%/379|   0.2%/449|   0.1%/555 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 134   |      93|       5.852|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 141   |   13027|     221.646|   2.1%/ 32|   1.8%/ 39|   1.7%/ 42|   1.6%/ 44 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 141   |   28655|     608.382|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 141   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 141   |     813|      19.167|   0.4%/163|   0.4%/186|   0.4%/194|   0.3%/201 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 141   |    5800|     561.060|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 141   |    1994|     231.777|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 141   |      69|       3.922|   0.5%/144|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 141   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 141   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 141   |      29|       3.813|   1.8%/ 38|   1.7%/ 42|   1.6%/ 43|   1.5%/ 45 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 141   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 141   |      53|       4.554|   0.7%/ 94|   1.0%/ 72|   1.0%/ 68|   1.1%/ 64 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 141   |    6026|      72.473|   0.3%/220|   0.3%/213|   0.3%/211|   0.3%/210 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 141   |  173747|     527.235|   0.6%/111|   0.6%/118|   0.6%/120|   0.6%/122 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  27   |      16|       0.398|   9.5%/  7|   6.9%/ 10|   6.5%/ 11|   6.2%/ 11 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 141   |    2179|      52.022|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 141   |     365|      36.946|   0.3%/253|   0.3%/239|   0.3%/235|   0.3%/231 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 141   |   47065|     708.434|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 141   |      39|      11.174|   0.8%/ 88|   0.9%/ 77|   0.9%/ 74|   1.0%/ 71 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 141   |     259|       7.577|   2.8%/ 25|   2.4%/ 29|   2.3%/ 30|   2.2%/ 31 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 141   |     309|       9.599|   3.2%/ 21|   3.2%/ 21|   3.2%/ 22|   3.2%/ 22 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  20   |      25|       0.263|  11.9%/  6|   4.4%/ 16|   2.8%/ 25|   1.3%/ 52 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 140   |     290|      16.198|   4.5%/ 15|   5.2%/ 13|   5.4%/ 13|   5.5%/ 12 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 141   |     168|      11.098|   7.2%/ 10|   1.8%/ 39|   2.7%/ 25|   4.4%/ 16 |

