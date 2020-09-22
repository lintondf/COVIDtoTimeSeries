# State and Country COVID-19 Analysis #
## Updated: at 2020-09-22 for data as of 2020-09-21 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.2% of deaths and 56.3% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 174   |   33091|    1701.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 174   |   16071|    1809.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 174   |   15444|     532.641|   0.7%/ 98|   0.6%/117|   0.6%/123|   0.5%/130 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 174   |   15268|     386.414|   0.6%/108|   0.6%/119|   0.6%/123|   0.5%/126 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 174   |   13530|     629.936|   0.8%/ 89|   0.7%/ 97|   0.7%/100|   0.7%/102 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 174   |    9314|    1340.227|   0.1%/482|   0.1%/482|   0.1%/482|   0.1%/481 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 174   |    8706|     687.071|   0.3%/275|   0.3%/276|   0.3%/276|   0.3%/276 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 174   |    7962|     621.955|   0.2%/362|   0.2%/354|   0.2%/351|   0.2%/349 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 174   |    6998|     700.679|   0.1%/528|   0.1%/563|   0.1%/573|   0.1%/583 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 174   |    6769|     637.493|   0.7%/102|   0.6%/123|   0.5%/130|   0.5%/137 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 174   |  200973|     609.850|   0.4%/178|   0.4%/189|   0.4%/192|   0.4%/195 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 174   |  138407|     654.679|   0.6%/125|   0.5%/135|   0.5%/137|   0.5%/140 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 174   |   88770|      65.213|   1.4%/ 50|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 174   |   74640|     589.678|   0.6%/118|   0.5%/131|   0.5%/135|   0.5%/139 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 174   |   41838|     629.751|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 174   |   35697|     592.587|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 174   |   31694|     986.372|   0.4%/181|   0.3%/208|   0.3%/216|   0.3%/225 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 174   |   31144|     464.309|   0.1%/577|   0.1%/502|   0.1%/485|   0.1%/470 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 174   |   30431|     646.078|   0.2%/363|   0.2%/340|   0.2%/335|   0.2%/330 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 174   |   24336|     291.878|   0.6%/113|   0.6%/111|   0.6%/110|   0.6%/109 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 174   |    2479|     505.574|   0.5%/130|   0.5%/150|   0.4%/156|   0.4%/163 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 174   |      47|      64.737|   0.6%/116|   0.5%/150|   0.4%/162|   0.4%/176 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 174   |    5533|     760.190|   0.4%/187|   0.3%/225|   0.3%/237|   0.3%/249 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 174   |    1203|     398.475|   1.1%/ 64|   0.9%/ 81|   0.8%/ 86|   0.7%/ 93 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 174   |   15268|     386.414|   0.6%/108|   0.6%/119|   0.6%/123|   0.5%/126 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 174   |    2019|     350.592|   0.2%/401|   0.2%/406|   0.2%/407|   0.2%/408 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 174   |    4492|    1259.854|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 174   |     622|     638.836|   0.2%/432|   0.2%/394|   0.2%/385|   0.2%/377 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 174   |   13530|     629.936|   0.8%/ 89|   0.7%/ 97|   0.7%/100|   0.7%/102 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 174   |    6769|     637.493|   0.7%/102|   0.6%/123|   0.5%/130|   0.5%/137 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 174   |     128|      90.121|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 174   |     458|     256.421|   0.9%/ 78|   0.7%/ 95|   0.7%/100|   0.7%/106 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 174   |    8706|     687.071|   0.3%/275|   0.3%/276|   0.3%/276|   0.3%/276 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 174   |    3523|     523.236|   0.3%/239|   0.3%/247|   0.3%/249|   0.3%/251 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 174   |    1292|     409.424|   0.6%/117|   0.5%/129|   0.5%/132|   0.5%/136 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 174   |     591|     202.784|   1.5%/ 45|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 174   |    1130|     252.900|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/ 99 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 174   |    5415|    1164.883|   0.4%/191|   0.3%/217|   0.3%/225|   0.3%/233 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 174   |     139|     103.294|   0.3%/242|   0.3%/223|   0.3%/219|   0.3%/214 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 174   |    3892|     643.754|   0.2%/449|   0.1%/486|   0.1%/496|   0.1%/506 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 174   |    9314|    1340.227|   0.1%/482|   0.1%/482|   0.1%/482|   0.1%/481 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 174   |    6998|     700.679|   0.1%/528|   0.1%/563|   0.1%/573|   0.1%/583 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 174   |    2024|     358.850|   0.4%/182|   0.4%/182|   0.4%/182|   0.4%/182 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 174   |    2865|     962.773|   0.6%/118|   0.5%/138|   0.5%/144|   0.5%/151 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 174   |    1853|     301.952|   0.7%/ 94|   0.7%/ 96|   0.7%/ 97|   0.7%/ 97 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 174   |     156|     146.365|   2.2%/ 32|   2.3%/ 30|   2.4%/ 29|   2.4%/ 29 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 174   |     451|     233.346|   0.5%/146|   0.4%/155|   0.4%/157|   0.4%/160 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 174   |    1561|     506.722|   0.7%/101|   0.6%/118|   0.6%/122|   0.5%/128 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 174   |     439|     322.544|   0.1%/990|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 174   |   16071|    1809.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 174   |     854|     407.511|   0.4%/167|   0.4%/178|   0.4%/181|   0.4%/184 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 174   |   33091|    1701.024|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 174   |    3286|     313.354|   0.8%/ 82|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 174   |     188|     246.609|   1.6%/ 42|   1.8%/ 38|   1.8%/ 38|   1.9%/ 37 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 174   |    4639|     396.885|   0.5%/131|   0.5%/130|   0.5%/130|   0.5%/130 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 174   |     967|     244.376|   0.7%/ 94|   0.6%/108|   0.6%/112|   0.6%/116 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 174   |     539|     127.909|   0.6%/112|   0.5%/133|   0.5%/139|   0.5%/147 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 174   |    7962|     621.955|   0.2%/362|   0.2%/354|   0.2%/351|   0.2%/349 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 174   |     615|     192.708|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 174   |    1091|    1029.447|   0.2%/318|   0.2%/298|   0.2%/294|   0.2%/289 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 174   |    3273|     635.731|   0.7%/ 97|   0.6%/113|   0.6%/117|   0.6%/122 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 174   |     197|     222.587|   1.1%/ 62|   1.3%/ 55|   1.3%/ 53|   1.3%/ 51 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 174   |    2277|     333.285|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 174   |   15444|     532.641|   0.7%/ 98|   0.6%/117|   0.6%/123|   0.5%/130 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 174   |  200973|     609.850|   0.4%/178|   0.4%/189|   0.4%/192|   0.4%/195 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 174   |     447|     139.563|   0.3%/239|   0.2%/337|   0.2%/376|   0.2%/424 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 174   |      58|      92.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 174   |    2961|     346.940|   0.8%/ 89|   0.9%/ 81|   0.9%/ 79|   0.9%/ 77 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 174   |    2054|     269.729|   0.3%/241|   0.3%/267|   0.3%/274|   0.2%/282 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 174   |     320|     178.828|   1.8%/ 38|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 174   |    1256|     215.683|   0.4%/154|   0.4%/165|   0.4%/168|   0.4%/172 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 162   |      49|      84.248|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 174   |    1441|      44.702|   0.1%/521|   0.1%/510|   0.1%/506|   0.1%/502 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 174   |     370|     130.137|   1.1%/ 62|   1.0%/ 69|   1.0%/ 71|   0.9%/ 73 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 174   |    1686|      39.211|   0.5%/140|   0.5%/147|   0.5%/149|   0.5%/151 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 174   |     153|       4.908|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 174   |   13623|     303.142|   2.0%/ 35|   1.8%/ 38|   1.8%/ 39|   1.7%/ 39 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 174   |     938|     317.250|   0.3%/261|   0.2%/296|   0.2%/306|   0.2%/317 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 174   |    1064|      41.414|   0.8%/ 88|   0.4%/183|   0.3%/249|   0.2%/387 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 174   |     765|      85.888|   0.2%/346|   0.2%/295|   0.2%/285|   0.3%/275 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 174   |     579|      57.521|   0.4%/194|   0.3%/201|   0.3%/203|   0.3%/206 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 174   |     223|     144.598|   0.8%/ 90|   0.8%/ 87|   0.8%/ 86|   0.8%/ 86 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 174   |    5029|      29.853|   0.7%/102|   0.6%/113|   0.6%/116|   0.6%/119 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 174   |     791|      84.085|   0.7%/106|   0.6%/110|   0.6%/112|   0.6%/113 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 174   |    9947|     863.106|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 169   |      40|       3.422|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 174   |    8012|     698.518|   0.7%/106|   0.5%/144|   0.4%/159|   0.4%/176 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 174   |     778|     235.776|   1.1%/ 65|   1.0%/ 71|   1.0%/ 72|   0.9%/ 74 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 174   |      16|       6.691|   4.4%/ 16|   3.7%/ 18|   3.6%/ 19|   3.4%/ 20 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 174   |  138407|     654.679|   0.6%/125|   0.5%/135|   0.5%/137|   0.5%/140 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 174   |     787|     113.282|   0.8%/ 82|   0.7%/100|   0.7%/105|   0.6%/112 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 174   |      56|       2.694|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 162   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 174   |     417|      15.715|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 174   |    9270|     243.952|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 122   |      62|      11.293|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 147   |      82|       5.023|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 174   |   12364|     647.109|   0.4%/169|   0.4%/176|   0.4%/179|   0.4%/181 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 174   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 174   |   25072|     507.578|   0.9%/ 76|   0.7%/ 93|   0.7%/ 98|   0.7%/104 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 174   |     735|     145.340|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 174   |     248|      60.814|   1.5%/ 45|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 174   |     115|      10.230|   1.0%/ 72|   1.0%/ 66|   1.1%/ 65|   1.1%/ 63 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 174   |     636|     109.192|   0.1%/589|   0.1%/513|   0.1%/496|   0.1%/481 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 174   |    2121|     204.741|   0.7%/ 92|   0.6%/109|   0.6%/115|   0.6%/121 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 174   |    7252|     415.177|   0.3%/207|   0.3%/238|   0.3%/248|   0.3%/258 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 174   |    5792|      57.767|   0.3%/222|   0.3%/227|   0.3%/228|   0.3%/230 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 174   |     829|     127.780|   0.5%/139|   0.4%/181|   0.4%/195|   0.3%/212 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 153   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 170   |    1152|      11.675|   1.3%/ 53|   1.0%/ 66|   1.0%/ 71|   0.9%/ 75 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 174   |     339|      61.374|   0.1%/ ***|   0.1%/895|   0.1%/869|   0.1%/845 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 174   |   31144|     464.309|   0.1%/577|   0.1%/502|   0.1%/485|   0.1%/470 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 174   |      53|      24.466|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 174   |     108|      46.188|   1.0%/ 71|   0.3%/223|   0.3%/223|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 171   |      19|       5.197|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 174   |    9392|     112.957|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 174   |     300|       9.899|   0.3%/216|   0.3%/271|   0.2%/288|   0.2%/307 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 174   |     338|      31.490|   1.3%/ 55|   1.3%/ 52|   1.4%/ 51|   1.4%/ 50 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 174   |    3129|     188.447|   0.6%/114|   0.6%/120|   0.6%/121|   0.6%/122 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 160   |      65|       5.332|   0.3%/255|   0.1%/511|   0.1%/678|   0.1%/ *** |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 149   |      40|      25.167|   0.2%/392|   0.1%/660|   0.1%/812|   0.1%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 170   |     225|      19.429|   0.3%/212|   0.3%/253|   0.3%/268|   0.2%/286 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 174   |    2231|     243.610|   0.7%/100|   0.6%/118|   0.6%/124|   0.5%/130 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 174   |     643|      65.827|   0.6%/111|   0.8%/ 91|   0.8%/ 87|   0.8%/ 84 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 174   |   88770|      65.213|   1.4%/ 50|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 174   |    9694|      36.319|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55|   1.3%/ 55 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 174   |   24336|     291.878|   0.6%/113|   0.6%/111|   0.6%/110|   0.6%/109 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 174   |    8695|     222.213|   0.9%/ 74|   0.9%/ 78|   0.9%/ 79|   0.9%/ 80 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 174   |    1790|     363.615|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/993 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 174   |    1260|     137.099|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 174   |   35697|     592.587|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 174   |      64|      23.310|   9.9%/  7|  11.1%/  6|  11.3%/  6|  11.6%/  6 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 174   |    1545|      12.266|   0.7%/101|   0.6%/115|   0.6%/119|   0.6%/124 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 174   |      31|       2.871|   4.0%/ 17|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 174   |    1710|      91.500|   0.3%/244|   0.2%/391|   0.2%/460|   0.1%/558 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 174   |     657|      13.803|   0.5%/135|   0.4%/157|   0.4%/163|   0.4%/170 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 174   |     497|     276.896|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 171   |     584|     132.014|   0.5%/139|   0.5%/132|   0.5%/131|   0.5%/129 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 172   |    1047|     160.293|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 172   |      36|      18.912|   0.3%/273|   0.2%/283|   0.2%/285|   0.2%/286 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 174   |     306|      44.768|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 171   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 173   |     460|      66.878|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 174   |      87|      31.288|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 128   |     224|       8.517|   0.7%/ 97|   0.7%/ 99|   0.7%/100|   0.7%/100 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 174   |     130|       3.957|   0.1%/ ***|   0.1%/947|   0.1%/903|   0.1%/861 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 174   |     129|       6.347|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 174   |     162|      39.652|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 174   |   74640|     589.678|   0.6%/118|   0.5%/131|   0.5%/135|   0.5%/139 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 174   |    1212|     451.912|   0.9%/ 75|   0.9%/ 73|   0.9%/ 73|   1.0%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 174   |    1943|      54.164|   2.1%/ 32|   1.9%/ 37|   1.8%/ 38|   1.7%/ 39 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 120   |      44|       1.469|   3.2%/ 22|   3.3%/ 21|   3.4%/ 21|   3.4%/ 20 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  74   |     114|      46.508|   1.7%/ 41|   1.4%/ 50|   1.3%/ 53|   1.2%/ 57 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 129   |     435|      14.497|   2.6%/ 26|   2.2%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 174   |    6324|     362.270|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 174   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 174   |     149|      23.008|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 174   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 174   |    1110|       5.383|   0.3%/238|   0.3%/262|   0.3%/269|   0.2%/277 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 174   |     692|     333.086|   0.8%/ 86|   0.9%/ 81|   0.9%/ 80|   0.9%/ 79 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 174   |     266|      49.608|   0.1%/ ***|   0.1%/831|   0.1%/793|   0.1%/758 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 174   |     849|     182.059|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 66 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 174   |    6436|      29.343|   0.1%/839|   0.1%/964|   0.1%/ ***|   0.1%/ *** |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 174   |    2277|     539.762|   0.6%/121|   0.5%/128|   0.5%/130|   0.5%/131 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  57   |       7|       0.762|   2.5%/ 27|   2.7%/ 26|   2.7%/ 25|   2.8%/ 24 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 174   |     722|     100.871|   3.2%/ 22|   2.7%/ 26|   2.5%/ 27|   2.4%/ 28 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 174   |   31694|     986.372|   0.4%/181|   0.3%/208|   0.3%/216|   0.3%/225 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 174   |    5082|      46.831|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 174   |    2300|      59.932|   0.6%/122|   0.6%/122|   0.6%/121|   0.6%/121 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 174   |    1900|     184.860|   0.3%/254|   0.3%/228|   0.3%/222|   0.3%/216 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 174   |     211|      76.845|   0.3%/243|   0.3%/247|   0.3%/248|   0.3%/250 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 174   |    4529|     233.399|   0.9%/ 74|   0.9%/ 80|   0.8%/ 82|   0.8%/ 83 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 174   |   19440|     132.473|   0.6%/114|   0.6%/113|   0.6%/113|   0.6%/113 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 115   |      26|       2.131|   0.0%/ --|   5.7%/ 12|   4.2%/ 16|   2.6%/ 27 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 174   |    4534|     132.500|   0.7%/103|   0.6%/108|   0.6%/109|   0.6%/111 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 174   |     306|      18.867|   0.3%/266|   0.2%/385|   0.2%/431|   0.1%/488 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 174   |     745|     107.014|   0.2%/427|   0.1%/530|   0.1%/562|   0.1%/597 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 152   |      73|       9.183|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 174   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 174   |      40|       7.281|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 174   |     138|      65.932|   0.1%/842|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 167   |      99|       6.208|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 174   |   16338|     277.974|   0.5%/142|   0.4%/190|   0.3%/208|   0.3%/229 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 174   |   30431|     646.078|   0.2%/363|   0.2%/340|   0.2%/335|   0.2%/330 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 174   |      13|       0.594|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 174   |     840|      19.798|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 174   |    5867|     567.452|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 174   |    2041|     237.211|   0.1%/995|   0.1%/926|   0.1%/910|   0.1%/894 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 174   |     185|      10.584|   1.8%/ 38|   1.6%/ 45|   1.5%/ 47|   1.4%/ 49 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 174   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 174   |      58|       0.872|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 174   |      43|       5.669|   1.0%/ 67|   1.1%/ 61|   1.1%/ 60|   1.2%/ 59 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 174   |      76|      55.990|   4.6%/ 15|   4.1%/ 17|   3.9%/ 18|   3.7%/ 18 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 174   |     144|      12.324|   4.2%/ 16|   4.9%/ 14|   5.0%/ 14|   5.2%/ 13 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 174   |    7495|      90.129|   0.9%/ 80|   0.9%/ 74|   0.9%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 174   |  200973|     609.850|   0.4%/178|   0.4%/189|   0.4%/192|   0.4%/195 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  60   |      65|       1.615|   3.2%/ 22|   1.8%/ 38|   1.5%/ 48|   1.1%/ 64 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 174   |    3683|      87.946|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41|   1.7%/ 41 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 174   |     407|      41.178|   0.2%/296|   0.2%/331|   0.2%/342|   0.2%/353 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 174   |   41838|     629.751|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 174   |      46|      13.177|   0.2%/414|   0.1%/795|   0.1%/ ***|   0.1%/ *** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 174   |     443|      12.976|   1.5%/ 46|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 174   |     560|      17.369|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  53   |      35|       0.364|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 173   |     331|      18.502|   0.6%/119|   0.6%/116|   0.6%/115|   0.6%/115 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 174   |     241|      15.902|   0.3%/242|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

