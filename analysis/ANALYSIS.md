# State and Country COVID-19 Analysis #
## Updated: at 2020-07-28 for data as of 2020-07-27 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 35.7% of deaths and 39.7% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 49.9% of the US population and account for 69.4% of deaths and 56.5% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 118   |   32655|    1678.609|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 118   |   15849|    1784.324|   0.1%/601|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 118   |    8546|    1229.793|   0.2%/396|   0.2%/440|   0.2%/452|   0.1%/464 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 118   |    8584|     217.237|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 118   |    7635|     602.515|   0.2%/334|   0.2%/434|   0.1%/465|   0.1%/500 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 118   |    7157|     559.072|   0.2%/307|   0.2%/352|   0.2%/366|   0.2%/381 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 118   |    6422|     643.094|   0.1%/691|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 118   |    5979|     278.398|   2.3%/ 30|   2.4%/ 28|   2.4%/ 28|   2.5%/ 28 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 118   |    5214|     179.818|   3.6%/ 19|   4.0%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 118   |    4426|    1241.372|   0.1%/882|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 118   |  147669|     448.102|   0.6%/113|   0.6%/107|   0.7%/105|   0.7%/104 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 118   |   88591|     419.044|   1.3%/ 52|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 118   |   45934|     691.407|   0.1%/474|   0.1%/525|   0.1%/539|   0.1%/553 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 118   |   44452|     351.183|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 118   |   35131|     583.203|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 118   |   33550|      24.647|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 118   |   30243|     450.878|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 118   |   28436|     603.738|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 118   |   14848|     462.102|   1.3%/ 55|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 118   |   15948|     191.271|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 118   |    1498|     305.517|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 118   |      20|      27.194|   1.7%/ 40|   1.8%/ 39|   1.8%/ 38|   1.8%/ 38 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 118   |    3426|     470.630|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 118   |     410|     135.788|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 118   |    8584|     217.237|   1.3%/ 54|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 118   |    1799|     312.403|   0.3%/239|   0.3%/223|   0.3%/219|   0.3%/216 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 118   |    4426|    1241.372|   0.1%/882|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 118   |     561|     576.167|   0.2%/399|   0.2%/377|   0.2%/371|   0.2%/365 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 118   |    5979|     278.398|   2.3%/ 30|   2.4%/ 28|   2.4%/ 28|   2.5%/ 28 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 118   |    3497|     329.318|   1.1%/ 61|   1.3%/ 52|   1.4%/ 50|   1.4%/ 48 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 118   |      27|      18.912|   1.6%/ 43|   2.1%/ 32|   2.3%/ 30|   2.4%/ 28 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 118   |     149|      83.599|   1.7%/ 40|   1.9%/ 36|   2.0%/ 35|   2.0%/ 34 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 118   |    7635|     602.515|   0.2%/334|   0.2%/434|   0.1%/465|   0.1%/500 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 118   |    2910|     432.242|   0.4%/194|   0.4%/190|   0.4%/188|   0.4%/187 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 118   |     839|     266.011|   0.7%/104|   0.7%/104|   0.7%/105|   0.7%/106 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 118   |     332|     114.019|   0.8%/ 87|   0.9%/ 79|   0.9%/ 77|   0.9%/ 75 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 118   |     709|     158.621|   0.8%/ 87|   0.8%/ 91|   0.8%/ 92|   0.7%/ 93 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 118   |    3758|     808.470|   0.5%/127|   0.6%/121|   0.6%/120|   0.6%/118 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 118   |     120|      89.353|   0.4%/190|   0.3%/257|   0.2%/282|   0.2%/312 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 118   |    3450|     570.656|   0.3%/262|   0.3%/273|   0.3%/276|   0.2%/279 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 118   |    8546|    1229.793|   0.2%/396|   0.2%/440|   0.2%/452|   0.1%/464 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 118   |    6422|     643.094|   0.1%/691|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 118   |    1621|     287.370|   0.3%/217|   0.3%/224|   0.3%/227|   0.3%/229 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 118   |    1510|     507.474|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 118   |    1210|     197.231|   0.7%/ 94|   0.8%/ 85|   0.8%/ 82|   0.9%/ 80 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 118   |      49|      45.439|   2.9%/ 24|   3.1%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 118   |     321|     165.695|   0.6%/110|   0.7%/106|   0.7%/105|   0.7%/106 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 118   |     746|     242.163|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 118   |     409|     301.099|   0.3%/202|   0.4%/196|   0.4%/193|   0.4%/190 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 118   |   15849|    1784.324|   0.1%/601|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 118   |     616|     293.914|   0.9%/ 79|   0.9%/ 75|   0.9%/ 74|   1.0%/ 73 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 118   |   32655|    1678.609|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 118   |    1840|     175.414|   1.3%/ 54|   1.4%/ 51|   1.4%/ 50|   1.4%/ 50 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 118   |     100|     131.181|   1.0%/ 71|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 118   |    3333|     285.096|   0.6%/112|   0.6%/107|   0.7%/106|   0.7%/105 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 118   |     497|     125.589|   1.2%/ 58|   1.3%/ 51|   1.4%/ 50|   1.4%/ 49 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 118   |     291|      68.917|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48|   1.4%/ 48 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 118   |    7157|     559.072|   0.2%/307|   0.2%/352|   0.2%/366|   0.2%/381 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 118   |     198|      62.153|   1.5%/ 47|   1.7%/ 40|   1.8%/ 38|   1.9%/ 37 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 118   |    1007|     950.110|   0.2%/423|   0.1%/527|   0.1%/562|   0.1%/602 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 118   |    1488|     288.949|   3.3%/ 21|   3.7%/ 18|   3.8%/ 18|   3.9%/ 17 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 118   |     126|     142.220|   0.9%/ 78|   0.7%/103|   0.6%/113|   0.6%/125 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 118   |     985|     144.193|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 118   |    5214|     179.818|   3.6%/ 19|   4.0%/ 17|   4.0%/ 17|   4.1%/ 17 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 118   |  147669|     448.102|   0.6%/113|   0.6%/107|   0.7%/105|   0.7%/104 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 118   |     284|      88.497|   1.8%/ 39|   1.6%/ 43|   1.6%/ 43|   1.6%/ 44 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 118   |      56|      89.745|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 118   |    2098|     245.778|   0.4%/171|   0.3%/233|   0.3%/256|   0.2%/282 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 118   |    1506|     197.826|   0.6%/122|   0.5%/134|   0.5%/137|   0.5%/140 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 118   |     104|      57.984|   0.5%/145|   0.5%/141|   0.5%/140|   0.5%/140 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 118   |     891|     153.000|   0.6%/110|   0.7%/ 94|   0.8%/ 90|   0.8%/ 87 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 106   |      26|      44.843|   0.6%/109|   0.4%/168|   0.3%/200|   0.3%/250 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 118   |    1304|      40.452|   1.5%/ 47|   1.1%/ 62|   1.0%/ 67|   0.9%/ 73 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 118   |     141|      49.400|   3.1%/ 23|   3.2%/ 22|   3.2%/ 22|   3.2%/ 21 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 118   |    1164|      27.072|   1.0%/ 73|   1.0%/ 71|   1.0%/ 70|   1.0%/ 69 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 118   |      39|       1.266|   1.1%/ 61|   5.7%/ 12|   6.6%/ 10|   5.4%/ 13 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 118   |    3036|      67.555|   3.4%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 118   |     729|     246.546|   1.6%/ 44|   1.3%/ 52|   1.3%/ 54|   1.2%/ 57 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 118   |     137|       5.323|   3.1%/ 22|   4.1%/ 17|   4.4%/ 16|   4.6%/ 15 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 118   |     713|      80.069|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 118   |     429|      42.581|   2.2%/ 31|   2.1%/ 33|   2.0%/ 34|   2.0%/ 35 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 118   |     144|      93.124|   1.7%/ 41|   1.6%/ 44|   1.5%/ 45|   1.5%/ 46 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 118   |    2980|      17.689|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 118   |     541|      57.516|   1.0%/ 69|   0.9%/ 75|   0.9%/ 77|   0.9%/ 78 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 118   |    9823|     852.325|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 113   |      37|       3.127|   2.2%/ 31|   1.6%/ 42|   1.5%/ 47|   1.3%/ 52 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 118   |    2674|     233.170|   2.7%/ 26|   2.5%/ 28|   2.4%/ 29|   2.4%/ 29 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 118   |     291|      88.285|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 118   |       1|       0.428|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 118   |   88591|     419.044|   1.3%/ 52|   1.2%/ 55|   1.2%/ 56|   1.2%/ 57 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 118   |     347|      49.963|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 42 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 118   |      53|       2.540|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 106   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 118   |     392|      14.781|   0.5%/142|   0.5%/128|   0.6%/125|   0.6%/123 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 118   |    8955|     235.657|   0.1%/835|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  66   |      60|      10.892|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70|   1.0%/ 72 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)|  91   |      75|       4.620|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 118   |    9486|     496.449|   1.0%/ 66|   0.9%/ 74|   0.9%/ 76|   0.9%/ 79 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 118   |    4646|       3.313|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 118   |    8764|     177.425|   3.3%/ 21|   3.1%/ 22|   3.1%/ 22|   3.1%/ 22 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 118   |     112|      22.221|   8.1%/  8|   9.0%/  8|   9.2%/  7|   9.4%/  7 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 118   |     129|      31.686|   1.2%/ 59|   1.5%/ 45|   1.6%/ 43|   1.7%/ 40 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 118   |      87|       7.778|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 118   |     613|     105.295|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 118   |    1082|     104.426|   1.3%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 118   |    5582|     319.554|   0.6%/110|   0.6%/126|   0.5%/130|   0.5%/136 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 118   |    4749|      47.362|   1.2%/ 56|   0.9%/ 74|   0.9%/ 80|   0.8%/ 88 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 118   |     417|      64.288|   2.9%/ 24|   2.8%/ 25|   2.8%/ 25|   2.7%/ 25 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)|  97   |      51|      37.548|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 114   |     226|       2.286|   3.9%/ 18|   4.3%/ 16|   4.4%/ 16|   4.5%/ 15 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 118   |     328|      59.413|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 118   |   30243|     450.878|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 118   |      48|      22.244|   0.5%/135|   0.7%/105|   0.7%/ 98|   0.8%/ 91 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 118   |       6|       2.671|   6.3%/ 11|   7.9%/  9|   8.4%/  8|   8.8%/  8 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 115   |      16|       4.324|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 118   |    9128|     109.781|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 118   |     166|       5.481|   1.5%/ 47|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 118   |     201|      18.767|   0.3%/236|   0.4%/179|   0.4%/168|   0.4%/159 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 118   |    1813|     109.216|   2.5%/ 27|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 104   |      44|       3.572|   1.2%/ 59|   1.2%/ 56|   1.2%/ 55|   1.3%/ 55 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)|  93   |      26|      16.224|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 114   |     162|      13.960|   1.0%/ 67|   0.6%/110|   0.5%/130|   0.4%/156 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 118   |    1143|     124.830|   2.8%/ 25|   2.9%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 118   |     597|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 118   |   33550|      24.647|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28|   2.5%/ 28 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 118   |    4885|      18.301|   2.1%/ 33|   2.1%/ 33|   2.1%/ 32|   2.1%/ 32 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 118   |   15948|     191.271|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 118   |    4563|     116.623|   2.3%/ 30|   1.9%/ 36|   1.8%/ 38|   1.7%/ 40 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 118   |    1764|     358.435|   0.1%/896|   0.1%/775|   0.1%/749|   0.1%/724 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 118   |     471|      51.260|   1.9%/ 37|   2.1%/ 33|   2.1%/ 33|   2.2%/ 32 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 118   |   35131|     583.203|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 118   |      10|       3.667|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 118   |     996|       7.907|   0.1%/607|   0.1%/485|   0.2%/459|   0.2%/436 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 118   |      11|       1.051|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 118   |     641|      34.309|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 118   |     293|       6.151|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 118   |     184|     102.536|   4.1%/ 17|   3.8%/ 18|   3.7%/ 19|   3.6%/ 19 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 115   |     434|      98.266|   0.8%/ 88|   0.8%/ 84|   0.8%/ 83|   0.8%/ 82 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 116   |     304|      46.475|   4.0%/ 17|   3.2%/ 22|   3.0%/ 23|   2.8%/ 25 |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 116   |      31|      16.384|   0.1%/697|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 118   |      45|       6.526|   2.1%/ 33|   2.7%/ 25|   2.9%/ 24|   3.1%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 115   |      78|      17.411|   0.8%/ 82|   0.2%/315|   0.1%/ ***|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 117   |      62|       9.047|   3.2%/ 22|   3.2%/ 22|   3.2%/ 22|   3.2%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 118   |      80|      28.709|   0.1%/971|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  72   |      90|       3.420|   5.6%/ 12|   5.4%/ 13|   5.3%/ 13|   5.3%/ 13 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 118   |     124|       3.776|   0.1%/590|   0.1%/508|   0.1%/491|   0.1%/476 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 118   |     123|       6.094|   0.2%/420|   0.2%/435|   0.2%/433|   0.2%/429 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 118   |     160|      39.159|   0.4%/161|   0.2%/460|   0.1%/863|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 118   |   44452|     351.183|   1.5%/ 46|   1.4%/ 50|   1.4%/ 51|   1.3%/ 52 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 118   |     748|     278.920|   1.0%/ 69|   0.9%/ 74|   0.9%/ 75|   0.9%/ 77 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 118   |     301|       8.388|   1.6%/ 42|   1.9%/ 36|   2.0%/ 35|   2.1%/ 33 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  64   |      11|       0.379|   2.1%/ 34|   0.6%/108|   0.2%/353|   0.0%/ -- |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  18   |       8|       3.253|  51.8%/  1|   0.0%/ --|   4.6%/ 15|   4.6%/ 15 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  73   |      46|       1.539|   1.5%/ 47|   2.2%/ 32|   2.4%/ 29|   2.6%/ 27 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 118   |    6160|     352.842|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 118   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 118   |     111|      17.179|   1.0%/ 72|   0.8%/ 89|   0.7%/ 95|   0.7%/102 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 118   |      69|       3.104|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 118   |     872|       4.231|   1.2%/ 59|   1.0%/ 67|   1.0%/ 70|   1.0%/ 72 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 118   |     471|     226.816|   1.4%/ 50|   1.3%/ 53|   1.3%/ 54|   1.3%/ 55 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 118   |     256|      47.665|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 118   |     396|      84.952|   2.8%/ 24|   2.8%/ 25|   2.7%/ 25|   2.7%/ 25 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 118   |    5952|      27.137|   0.7%/ 95|   0.5%/143|   0.4%/163|   0.4%/190 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 118   |    1342|     318.179|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.3%/ 30 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 118   |      43|       5.985|   3.8%/ 18|   4.4%/ 16|   4.5%/ 15|   4.6%/ 15 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 118   |   14848|     462.102|   1.3%/ 55|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 118   |    1977|      18.218|   0.9%/ 73|   1.0%/ 72|   1.0%/ 72|   1.0%/ 72 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 118   |    1680|      43.765|   0.4%/162|   0.4%/174|   0.4%/177|   0.4%/180 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 118   |    1725|     167.841|   0.3%/276|   0.2%/334|   0.2%/351|   0.2%/369 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 118   |     169|      61.532|   0.8%/ 86|   0.5%/150|   0.4%/182|   0.3%/230 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 118   |    2210|     113.904|   1.0%/ 66|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 118   |   13505|      92.027|   1.1%/ 61|   1.0%/ 70|   1.0%/ 72|   0.9%/ 75 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  59   |       5|       0.410|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 118   |    2804|      81.951|   1.5%/ 46|   1.3%/ 55|   1.2%/ 57|   1.2%/ 60 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 118   |     192|      11.873|   1.9%/ 37|   1.9%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 118   |     561|      80.524|   2.1%/ 33|   1.7%/ 40|   1.6%/ 42|   1.6%/ 45 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)|  96   |      67|       8.432|   0.3%/262|   0.2%/419|   0.1%/513|   0.1%/674 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 118   |      27|       4.778|   0.1%/585|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 118   |      28|       5.132|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 118   |     116|      55.253|   0.2%/314|   0.3%/223|   0.3%/207|   0.4%/194 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 111   |      93|       5.863|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 118   |    6967|     118.534|   3.7%/ 18|   3.9%/ 18|   4.0%/ 17|   4.0%/ 17 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 118   |   28436|     603.738|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 118   |      11|       0.505|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 118   |     727|      17.120|   0.7%/102|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 118   |    5723|     553.593|   0.2%/342|   0.2%/402|   0.2%/421|   0.2%/442 |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 118   |    1977|     229.748|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 118   |      42|       2.372|   7.4%/  9|   4.0%/ 17|   2.8%/ 25|   4.6%/ 15 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 118   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 118   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 118   |      17|       2.225|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 118   |       8|       5.865|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 118   |      50|       4.265|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 118   |    5637|      67.794|   0.3%/213|   0.3%/225|   0.3%/228|   0.3%/232 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 118   |  147669|     448.102|   0.6%/113|   0.6%/107|   0.7%/105|   0.7%/104 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 118   |    1645|      39.288|   1.1%/ 63|   1.0%/ 69|   1.0%/ 70|   1.0%/ 71 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 118   |     346|      34.987|   0.2%/282|   0.2%/372|   0.2%/404|   0.2%/441 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 118   |   45934|     691.407|   0.1%/474|   0.1%/525|   0.1%/539|   0.1%/553 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 118   |      35|       9.971|   0.8%/ 84|   0.7%/ 98|   0.7%/103|   0.6%/109 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 118   |     127|       3.720|   4.8%/ 14|   3.9%/ 18|   3.7%/ 19|   3.5%/ 20 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 118   |     149|       4.611|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 117   |     177|       9.894|   8.2%/  8|   7.4%/  9|   7.0%/ 10|   6.7%/ 10 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 118   |      36|       2.359|   5.8%/ 12|   4.3%/ 16|   3.9%/ 18|   3.5%/ 19 |

