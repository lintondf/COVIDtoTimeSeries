# State and Country COVID-19 Analysis #
## Updated: at 2020-08-19 for data as of 2020-08-18 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.7% of deaths and 40.4% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.8% of deaths and 58.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 140   |   32864|    1689.337|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 140   |   15927|    1793.139|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 140   |   11630|     294.340|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 140   |   11454|     395.013|   2.0%/ 35|   1.6%/ 43|   1.5%/ 46|   1.4%/ 48 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 140   |    9962|     463.824|   2.0%/ 34|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 140   |    8862|    1275.133|   0.2%/433|   0.2%/446|   0.2%/449|   0.2%/453 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 140   |    7992|     630.694|   0.2%/323|   0.2%/326|   0.2%/327|   0.2%/328 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 140   |    7470|     583.537|   0.2%/320|   0.2%/308|   0.2%/305|   0.2%/302 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 140   |    6602|     661.034|   0.1%/492|   0.1%/465|   0.2%/459|   0.2%/453 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 140   |    4812|     453.178|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 140   |  172724|     524.130|   0.6%/110|   0.6%/116|   0.6%/118|   0.6%/120 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 140   |  110640|     523.338|   0.9%/ 73|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 140   |   58544|     462.515|   1.1%/ 60|   1.1%/ 65|   1.0%/ 66|   1.0%/ 68 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 140   |   53352|      39.194|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 140   |   47026|     707.849|   0.1%/953|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 140   |   35345|     586.744|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 140   |   30431|     453.681|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 140   |   28641|     608.084|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 140   |   26288|     818.129|   0.9%/ 76|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 140   |   20227|     242.599|   0.9%/ 73|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 140   |    1985|     404.785|   1.0%/ 67|   0.9%/ 81|   0.8%/ 86|   0.8%/ 91 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 140   |      29|      39.844|   1.3%/ 54|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 140   |    4690|     644.404|   1.2%/ 60|   0.9%/ 78|   0.8%/ 85|   0.8%/ 92 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 140   |     634|     210.125|   1.6%/ 43|   1.5%/ 47|   1.4%/ 49|   1.4%/ 51 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 140   |   11630|     294.340|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 140   |    1904|     330.655|   0.2%/332|   0.2%/378|   0.2%/391|   0.2%/403 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 140   |    4458|    1250.436|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 140   |     598|     614.287|   0.1%/855|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 140   |    9962|     463.824|   2.0%/ 34|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 140   |    4812|     453.178|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49|   1.4%/ 49 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 140   |      41|      29.039|   1.1%/ 61|   1.3%/ 55|   1.3%/ 54|   1.3%/ 53 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 140   |     293|     164.160|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 140   |    7992|     630.694|   0.2%/323|   0.2%/326|   0.2%/327|   0.2%/328 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 140   |    3153|     468.378|   0.4%/187|   0.4%/184|   0.4%/183|   0.4%/182 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 140   |     997|     316.142|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90|   0.8%/ 90 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 140   |     417|     143.078|   0.7%/ 93|   0.7%/106|   0.6%/110|   0.6%/114 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 140   |     824|     184.537|   0.7%/102|   0.7%/103|   0.7%/104|   0.7%/104 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 140   |    4575|     984.107|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87|   0.8%/ 88 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 140   |     128|      95.100|   0.2%/322|   0.2%/412|   0.2%/442|   0.1%/478 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 140   |    3664|     606.088|   0.2%/298|   0.2%/331|   0.2%/340|   0.2%/351 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 140   |    8862|    1275.133|   0.2%/433|   0.2%/446|   0.2%/449|   0.2%/453 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 140   |    6602|     661.034|   0.1%/492|   0.1%/465|   0.2%/459|   0.2%/453 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 140   |    1758|     311.682|   0.5%/152|   0.5%/138|   0.5%/135|   0.5%/132 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 140   |    2167|     728.203|   1.4%/ 50|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 140   |    1413|     230.149|   0.7%/103|   0.7%/105|   0.7%/105|   0.7%/105 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 140   |      91|      85.159|   1.7%/ 41|   1.2%/ 59|   1.0%/ 66|   0.9%/ 76 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 140   |     368|     189.986|   0.6%/114|   0.6%/115|   0.6%/116|   0.6%/117 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 140   |    1113|     361.372|   1.7%/ 41|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 140   |     425|     312.589|   0.1%/616|   0.1%/984|   0.1%/ ***|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 140   |   15927|    1793.139|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 140   |     726|     346.420|   0.6%/107|   0.6%/118|   0.6%/121|   0.6%/125 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 140   |   32864|    1689.337|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 140   |    2427|     231.428|   1.1%/ 65|   0.9%/ 73|   0.9%/ 75|   0.9%/ 78 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 140   |     126|     165.576|   1.3%/ 54|   1.4%/ 49|   1.4%/ 48|   1.5%/ 47 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 140   |    3884|     332.277|   0.6%/120|   0.5%/132|   0.5%/136|   0.5%/139 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 140   |     681|     172.029|   1.3%/ 55|   1.2%/ 57|   1.2%/ 57|   1.2%/ 58 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 140   |     403|      95.512|   1.2%/ 60|   1.0%/ 67|   1.0%/ 70|   1.0%/ 72 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 140   |    7470|     583.537|   0.2%/320|   0.2%/308|   0.2%/305|   0.2%/302 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 140   |     345|     108.066|   2.6%/ 27|   2.7%/ 25|   2.8%/ 25|   2.8%/ 25 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 140   |    1024|     966.188|   0.1%/783|   0.1%/802|   0.1%/805|   0.1%/807 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 140   |    2408|     467.750|   1.7%/ 41|   1.4%/ 51|   1.3%/ 54|   1.2%/ 57 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 140   |     157|     177.000|   0.9%/ 79|   0.8%/ 88|   0.8%/ 91|   0.7%/ 94 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 140   |    1421|     208.027|   1.6%/ 42|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 140   |   11454|     395.013|   2.0%/ 35|   1.6%/ 43|   1.5%/ 46|   1.4%/ 48 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 140   |  172724|     524.130|   0.6%/110|   0.6%/116|   0.6%/118|   0.6%/120 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 140   |     377|     117.668|   1.0%/ 68|   0.8%/ 85|   0.8%/ 91|   0.7%/ 98 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 140   |      58|      93.629|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 140   |    2434|     285.210|   0.5%/148|   0.4%/185|   0.3%/199|   0.3%/215 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 140   |    1807|     237.331|   0.8%/ 92|   0.8%/ 91|   0.8%/ 91|   0.8%/ 91 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 140   |     166|      92.448|   2.0%/ 34|   2.1%/ 32|   2.2%/ 32|   2.2%/ 32 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 140   |    1056|     181.303|   0.6%/115|   0.5%/131|   0.5%/136|   0.5%/142 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 128   |      31|      52.712|   0.8%/ 87|   0.8%/ 90|   0.8%/ 90|   0.8%/ 92 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 140   |    1383|      42.922|   0.4%/161|   0.4%/172|   0.4%/174|   0.4%/177 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 140   |     241|      84.658|   2.1%/ 33|   1.8%/ 37|   1.8%/ 39|   1.7%/ 40 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 140   |    1397|      32.488|   0.8%/ 91|   0.7%/ 97|   0.7%/ 99|   0.7%/100 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 140   |      98|       3.149|   2.5%/ 27|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 140   |    6173|     137.360|   3.0%/ 23|   2.8%/ 25|   2.7%/ 25|   2.7%/ 26 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 140   |     839|     283.617|   0.6%/119|   0.5%/150|   0.4%/160|   0.4%/172 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 140   |     461|      17.956|   4.7%/ 15|   4.8%/ 14|   4.8%/ 14|   4.8%/ 14 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 140   |     729|      81.837|   0.1%/649|   0.1%/591|   0.1%/577|   0.1%/564 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 140   |     525|      52.144|   0.6%/118|   0.3%/238|   0.2%/317|   0.1%/473 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 140   |     176|     113.899|   0.9%/ 74|   0.9%/ 81|   0.8%/ 83|   0.8%/ 85 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 140   |    3747|      22.243|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 140   |     619|      65.791|   0.5%/128|   0.5%/149|   0.4%/155|   0.4%/161 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 140   |    9939|     862.441|   0.1%/968|   0.1%/820|   0.1%/788|   0.1%/758 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 135   |      39|       3.359|   0.3%/231|   0.2%/455|   0.1%/580|   0.1%/789 |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 140   |    4321|     376.754|   1.8%/ 39|   1.5%/ 47|   1.4%/ 49|   1.3%/ 52 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 140   |     507|     153.597|   1.7%/ 40|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 140   |       3|       1.289|   3.2%/ 21|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 140   |  110640|     523.338|   0.9%/ 73|   0.9%/ 79|   0.9%/ 81|   0.8%/ 83 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 140   |     528|      75.892|   1.6%/ 42|   1.5%/ 46|   1.5%/ 47|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 140   |      55|       2.620|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 128   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 140   |     403|      15.196|   0.2%/339|   0.2%/328|   0.2%/324|   0.2%/319 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 140   |    9089|     239.188|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  88   |      61|      11.182|   0.2%/296|   0.2%/337|   0.2%/364|   0.2%/404 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 113   |      76|       4.694|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 140   |   10638|     556.742|   0.6%/120|   0.5%/138|   0.5%/144|   0.5%/150 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 140   |    4705|       3.355|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 140   |   16190|     327.764|   2.4%/ 29|   2.1%/ 32|   2.1%/ 33|   2.0%/ 34 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 140   |     348|      68.716|   3.6%/ 19|   3.0%/ 23|   2.9%/ 24|   2.8%/ 25 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 140   |     170|      41.622|   0.7%/ 99|   0.5%/131|   0.5%/143|   0.4%/156 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 140   |      88|       7.880|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 140   |     622|     106.831|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 140   |    1494|     144.204|   1.5%/ 46|   1.5%/ 45|   1.5%/ 45|   1.5%/ 45 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 140   |    6144|     351.719|   0.4%/187|   0.3%/222|   0.3%/232|   0.3%/244 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 140   |    5238|      52.236|   0.4%/170|   0.3%/229|   0.3%/250|   0.3%/275 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 140   |     646|      99.547|   1.8%/ 39|   1.6%/ 44|   1.5%/ 46|   1.4%/ 48 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 119   |      88|      64.766|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 136   |     583|       5.914|   3.8%/ 18|   3.6%/ 19|   3.6%/ 19|   3.5%/ 19 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 140   |     334|      60.416|   0.1%/943|   0.1%/864|   0.1%/850|   0.1%/836 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 140   |   30431|     453.681|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 140   |      52|      24.064|   0.3%/266|   0.2%/296|   0.2%/303|   0.2%/309 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 140   |      63|      26.835|  12.8%/  5|  13.6%/  5|   8.0%/  8|   5.3%/ 13 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 137   |      17|       4.613|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 140   |    9246|     111.200|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 140   |     244|       8.054|   1.7%/ 41|   1.7%/ 42|   1.7%/ 42|   1.7%/ 42 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 140   |     227|      21.122|   0.7%/ 92|   0.9%/ 77|   0.9%/ 74|   1.0%/ 71 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 140   |    2482|     149.484|   1.2%/ 57|   1.0%/ 71|   0.9%/ 75|   0.9%/ 80 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 126   |      52|       4.256|   0.5%/129|   0.4%/180|   0.3%/200|   0.3%/224 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 115   |      32|      20.165|   1.5%/ 45|   2.0%/ 34|   2.1%/ 33|   2.2%/ 31 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 136   |     199|      17.217|   1.1%/ 64|   1.1%/ 63|   1.1%/ 62|   1.1%/ 62 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 140   |    1670|     182.331|   0.9%/ 74|   0.5%/153|   0.3%/206|   0.2%/314 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 140   |     609|      62.282|   0.1%/593|   0.1%/514|   0.1%/499|   0.1%/485 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 140   |   53352|      39.194|   2.0%/ 34|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 140   |    6331|      23.718|   1.1%/ 63|   1.0%/ 70|   1.0%/ 72|   0.9%/ 74 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 140   |   20227|     242.599|   0.9%/ 73|   0.8%/ 83|   0.8%/ 86|   0.8%/ 89 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 140   |    6073|     155.218|   1.3%/ 53|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 140   |    1776|     360.907|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 140   |     711|      77.354|   1.8%/ 39|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 140   |   35345|     586.744|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 140   |      15|       5.425|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 140   |    1101|       8.739|   0.7%/102|   0.8%/ 84|   0.9%/ 80|   0.9%/ 77 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 140   |      11|       1.032|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 140   |    1453|      77.737|   1.1%/ 65|   1.4%/ 50|   1.5%/ 47|   1.6%/ 44 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 140   |     514|      10.813|   1.8%/ 38|   1.4%/ 48|   1.3%/ 52|   1.2%/ 57 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 140   |     435|     242.287|   2.8%/ 24|   2.4%/ 29|   2.2%/ 31|   2.1%/ 33 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 137   |     508|     114.883|   0.6%/109|   0.6%/118|   0.6%/121|   0.6%/123 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 138   |    1522|     233.029|   0.3%/210|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 138   |      32|      16.977|   0.1%/558|   0.1%/641|   0.1%/665|   0.1%/689 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 140   |     108|      15.789|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18|   3.8%/ 18 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 137   |      84|      18.698|   0.5%/147|   0.4%/192|   0.3%/210|   0.3%/232 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 139   |     169|      24.606|   4.1%/ 17|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 140   |      81|      29.084|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  94   |     180|       6.854|   2.6%/ 27|   1.8%/ 38|   1.6%/ 43|   1.4%/ 48 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 140   |     125|       3.827|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 140   |     125|       6.191|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 140   |     157|      38.568|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 140   |   58544|     462.515|   1.1%/ 60|   1.1%/ 65|   1.0%/ 66|   1.0%/ 68 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 140   |     917|     341.818|   0.9%/ 81|   0.8%/ 86|   0.8%/ 87|   0.8%/ 89 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 140   |     696|      19.388|   3.9%/ 18|   4.2%/ 16|   4.3%/ 16|   4.4%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  86   |      20|       0.668|   2.2%/ 31|   1.2%/ 59|   0.9%/ 78|   0.6%/113 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  40   |      40|      16.072|   8.9%/  8|   7.3%/  9|   5.6%/ 12|   3.7%/ 18 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  95   |     115|       3.841|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15|   4.5%/ 15 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 140   |    6194|     354.802|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 140   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 140   |     132|      20.462|   0.6%/120|   0.5%/146|   0.4%/154|   0.4%/163 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 140   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 140   |     995|       4.827|   0.5%/134|   0.4%/167|   0.4%/178|   0.4%/191 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 140   |     556|     267.776|   0.6%/112|   0.5%/143|   0.5%/154|   0.4%/166 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 140   |     260|      48.407|   0.1%/929|   0.1%/735|   0.1%/697|   0.1%/662 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 140   |     606|     129.840|   1.7%/ 41|   1.6%/ 44|   1.6%/ 44|   1.5%/ 45 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 140   |    6221|      28.364|   0.2%/326|   0.2%/431|   0.1%/467|   0.1%/510 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 140   |    1849|     438.275|   1.2%/ 56|   1.0%/ 68|   1.0%/ 72|   0.9%/ 76 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  23   |       3|       0.336|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 140   |     119|      16.624|   6.6%/ 10|   7.5%/  9|   7.7%/  9|   7.9%/  9 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 140   |   26288|     818.129|   0.9%/ 76|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 140   |    2584|      23.811|   1.9%/ 36|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 140   |    1896|      49.392|   0.6%/121|   0.6%/117|   0.6%/116|   0.6%/115 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 140   |    1783|     173.461|   0.2%/407|   0.2%/406|   0.2%/406|   0.2%/405 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 140   |     196|      71.308|   0.6%/110|   0.6%/122|   0.6%/125|   0.5%/129 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 140   |    3074|     158.433|   1.5%/ 45|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 140   |   15949|     108.683|   0.7%/ 98|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  81   |       9|       0.752|   4.6%/ 15|   0.0%/ --|   0.0%/ --|   7.7%/  9 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 140   |    3479|     101.684|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67|   1.0%/ 67 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 140   |     261|      16.107|   1.2%/ 56|   1.1%/ 61|   1.1%/ 62|   1.1%/ 64 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 140   |     698|     100.241|   0.9%/ 80|   0.7%/105|   0.6%/114|   0.6%/125 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 118   |      69|       8.792|   0.2%/405|   0.1%/506|   0.1%/549|   0.1%/604 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 140   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 140   |      31|       5.760|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 140   |     132|      63.038|   0.3%/207|   0.3%/276|   0.2%/305|   0.2%/342 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 133   |      93|       5.852|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 140   |   12840|     218.464|   2.2%/ 31|   1.8%/ 37|   1.8%/ 39|   1.7%/ 42 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 140   |   28641|     608.084|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 140   |      11|       0.505|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 140   |     811|      19.104|   0.4%/160|   0.4%/185|   0.4%/192|   0.3%/200 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 140   |    5798|     560.795|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 140   |    1993|     231.657|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 140   |      66|       3.752|   0.6%/107|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 140   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 140   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 140   |      28|       3.765|   2.0%/ 34|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 140   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 140   |      53|       4.530|   0.7%/104|   0.9%/ 79|   0.9%/ 74|   1.0%/ 70 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 140   |    6006|      72.229|   0.3%/224|   0.3%/219|   0.3%/218|   0.3%/216 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 140   |  172724|     524.130|   0.6%/110|   0.6%/116|   0.6%/118|   0.6%/120 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  26   |      15|       0.378|   9.8%/  7|   8.4%/  8|   6.6%/ 10|   5.1%/ 13 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 140   |    2150|      51.338|   1.3%/ 54|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 140   |     364|      36.828|   0.3%/255|   0.3%/241|   0.3%/237|   0.3%/233 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 140   |   47026|     707.849|   0.1%/953|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 140   |      39|      11.072|   0.7%/104|   0.7%/ 94|   0.8%/ 92|   0.8%/ 90 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 140   |     253|       7.415|   2.9%/ 24|   2.5%/ 27|   2.4%/ 28|   2.3%/ 30 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 140   |     300|       9.315|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21|   3.3%/ 21 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  19   |      26|       0.270|  11.5%/  6|   4.6%/ 15|   4.4%/ 16|   2.7%/ 25 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 139   |     285|      15.913|   1.5%/ 45|   1.9%/ 37|   1.0%/ 67|   0.5%/136 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 140   |     165|      10.855|   5.5%/ 13|   1.0%/ 67|   1.8%/ 39|   2.7%/ 25 |

