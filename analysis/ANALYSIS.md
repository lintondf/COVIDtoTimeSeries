# State and Country COVID-19 Analysis #
## Updated: at 2020-09-02 for data as of 2020-09-01 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.1% of deaths and 39.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.1% of deaths and 57.7% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 154   |   32965|    1694.568|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 154   |   15956|    1796.456|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 154   |   13346|     337.759|   0.9%/ 74|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 154   |   13495|     465.425|   1.3%/ 52|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 154   |   11708|     545.129|   1.1%/ 61|   0.9%/ 78|   0.8%/ 83|   0.8%/ 90 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 154   |    9073|    1305.632|   0.2%/412|   0.2%/410|   0.2%/410|   0.2%/409 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 154   |    8268|     652.456|   0.2%/299|   0.2%/298|   0.2%/297|   0.2%/297 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 154   |    7699|     601.391|   0.2%/368|   0.2%/396|   0.2%/404|   0.2%/414 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 154   |    6756|     676.463|   0.2%/401|   0.2%/377|   0.2%/371|   0.2%/366 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 154   |    5768|     543.262|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 154   |  185781|     563.753|   0.5%/138|   0.5%/151|   0.4%/154|   0.4%/158 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 154   |  123618|     584.725|   0.8%/ 90|   0.7%/ 99|   0.7%/101|   0.7%/104 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 154   |   67338|      49.469|   1.7%/ 42|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 154   |   65807|     519.892|   0.8%/ 82|   0.8%/ 92|   0.7%/ 95|   0.7%/ 98 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 154   |   41280|     621.357|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 154   |   35530|     589.819|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 154   |   30643|     456.839|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 154   |   29093|     617.680|   0.1%/774|   0.1%/686|   0.1%/667|   0.1%/650 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 154   |   30392|     945.860|   0.6%/109|   0.6%/124|   0.5%/129|   0.5%/134 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 154   |   21949|     263.250|   0.6%/115|   0.5%/136|   0.5%/143|   0.5%/150 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 154   |    2194|     447.535|   0.9%/ 78|   0.9%/ 81|   0.8%/ 81|   0.8%/ 82 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 154   |      38|      52.337|   0.6%/120|   0.3%/204|   0.3%/249|   0.2%/321 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 154   |    5152|     707.795|   0.7%/ 95|   0.6%/118|   0.6%/125|   0.5%/134 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 154   |     808|     267.731|   1.9%/ 37|   1.9%/ 37|   1.9%/ 36|   1.9%/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 154   |   13346|     337.759|   0.9%/ 74|   0.8%/ 83|   0.8%/ 85|   0.8%/ 88 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 154   |    1951|     338.709|   0.2%/387|   0.2%/406|   0.2%/411|   0.2%/417 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 154   |    4469|    1253.510|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 154   |     607|     622.881|   0.1%/659|   0.1%/698|   0.1%/711|   0.1%/725 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 154   |   11708|     545.129|   1.1%/ 61|   0.9%/ 78|   0.8%/ 83|   0.8%/ 90 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 154   |    5768|     543.262|   1.3%/ 55|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 154   |      64|      45.430|   4.0%/ 17|   4.6%/ 15|   4.7%/ 15|   4.9%/ 14 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 154   |     375|     210.045|   1.9%/ 37|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 154   |    8268|     652.456|   0.2%/299|   0.2%/298|   0.2%/297|   0.2%/297 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 154   |    3324|     493.762|   0.3%/209|   0.3%/222|   0.3%/226|   0.3%/231 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 154   |    1128|     357.586|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 79 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 154   |     458|     157.102|   0.7%/102|   0.6%/109|   0.6%/111|   0.6%/113 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 154   |     946|     211.824|   0.9%/ 78|   0.9%/ 75|   0.9%/ 75|   0.9%/ 75 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 154   |    5038|    1083.702|   0.6%/110|   0.6%/122|   0.5%/126|   0.5%/130 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 154   |     133|      98.981|   0.2%/312|   0.2%/339|   0.2%/348|   0.2%/358 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 154   |    3765|     622.690|   0.2%/330|   0.2%/342|   0.2%/345|   0.2%/347 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 154   |    9073|    1305.632|   0.2%/412|   0.2%/410|   0.2%/410|   0.2%/409 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 154   |    6756|     676.463|   0.2%/401|   0.2%/377|   0.2%/371|   0.2%/366 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 154   |    1885|     334.267|   0.4%/168|   0.4%/177|   0.4%/180|   0.4%/183 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 154   |    2522|     847.508|   1.1%/ 65|   1.0%/ 71|   1.0%/ 73|   0.9%/ 75 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 154   |    1549|     252.438|   0.7%/ 96|   0.8%/ 92|   0.8%/ 91|   0.8%/ 90 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 154   |     107|     100.079|   1.5%/ 45|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 154   |     400|     206.933|   0.6%/122|   0.5%/129|   0.5%/131|   0.5%/133 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 154   |    1365|     443.246|   1.2%/ 57|   1.0%/ 68|   1.0%/ 71|   0.9%/ 74 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 154   |     434|     318.825|   0.1%/571|   0.1%/618|   0.1%/633|   0.1%/650 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 154   |   15956|    1796.456|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 154   |     785|     374.567|   0.6%/121|   0.5%/127|   0.5%/128|   0.5%/129 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 154   |   32965|    1694.568|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 154   |    2759|     263.050|   0.9%/ 77|   0.8%/ 83|   0.8%/ 84|   0.8%/ 86 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 154   |     147|     193.112|   0.9%/ 75|   0.8%/ 85|   0.8%/ 88|   0.8%/ 91 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 154   |    4182|     357.763|   0.5%/135|   0.5%/143|   0.5%/145|   0.5%/148 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 154   |     820|     207.351|   1.2%/ 57|   1.2%/ 59|   1.2%/ 60|   1.1%/ 61 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 154   |     467|     110.612|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64|   1.1%/ 64 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 154   |    7699|     601.391|   0.2%/368|   0.2%/396|   0.2%/404|   0.2%/414 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 154   |     462|     144.701|   1.7%/ 40|   1.5%/ 46|   1.4%/ 48|   1.4%/ 50 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 154   |    1049|     989.849|   0.2%/421|   0.2%/385|   0.2%/377|   0.2%/369 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 154   |    2809|     545.536|   1.2%/ 58|   1.0%/ 67|   1.0%/ 70|   1.0%/ 72 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 154   |     170|     191.603|   0.6%/121|   0.5%/141|   0.5%/147|   0.5%/154 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 154   |    1814|     265.487|   1.6%/ 44|   1.5%/ 46|   1.5%/ 47|   1.5%/ 47 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 154   |   13495|     465.425|   1.3%/ 52|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 154   |  185781|     563.753|   0.5%/138|   0.5%/151|   0.4%/154|   0.4%/158 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 154   |     418|     130.530|   0.7%/101|   0.6%/125|   0.5%/133|   0.5%/142 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 154   |      58|      93.096|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 154   |    2590|     303.385|   0.5%/129|   0.6%/124|   0.6%/122|   0.6%/121 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 154   |    1952|     256.332|   0.5%/148|   0.4%/183|   0.4%/195|   0.3%/209 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 154   |     219|     122.189|   2.1%/ 33|   2.2%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 154   |    1137|     195.286|   0.5%/135|   0.5%/147|   0.5%/150|   0.4%/154 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 142   |      39|      67.885|   0.2%/357|   0.0%/ --|   0.0%/ --|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 154   |    1420|      44.067|   0.2%/428|   0.1%/848|   0.1%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 154   |     291|     102.212|   1.6%/ 44|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 154   |    1525|      35.471|   0.6%/108|   0.6%/115|   0.6%/116|   0.6%/118 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 154   |     115|       3.693|   1.3%/ 54|   0.9%/ 77|   0.8%/ 86|   0.7%/ 97 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 154   |    9173|     204.133|   2.7%/ 26|   2.5%/ 28|   2.5%/ 28|   2.4%/ 29 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 154   |     887|     299.998|   0.4%/159|   0.4%/179|   0.4%/185|   0.4%/191 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 154   |     705|      27.453|   3.1%/ 22|   2.8%/ 25|   2.7%/ 25|   2.6%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 154   |     736|      82.640|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 154   |     537|      53.295|   0.3%/199|   0.3%/237|   0.3%/247|   0.3%/258 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 154   |     195|     126.293|   0.6%/119|   0.4%/156|   0.4%/170|   0.4%/187 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 154   |    4337|      25.741|   1.0%/ 67|   1.0%/ 67|   1.0%/ 68|   1.0%/ 68 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 154   |     683|      72.583|   0.7%/ 95|   0.8%/ 89|   0.8%/ 88|   0.8%/ 87 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 154   |    9929|     861.588|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 149   |      40|       3.425|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 154   |    5157|     449.624|   1.4%/ 50|   1.3%/ 54|   1.3%/ 55|   1.2%/ 56 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 154   |     633|     191.645|   1.5%/ 45|   1.5%/ 48|   1.4%/ 48|   1.4%/ 49 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 154   |       4|       1.878|   7.4%/  9|   9.4%/  7|   9.9%/  7|  10.5%/  6 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 154   |  123618|     584.725|   0.8%/ 90|   0.7%/ 99|   0.7%/101|   0.7%/104 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 154   |     637|      91.620|   1.5%/ 47|   1.5%/ 48|   1.4%/ 48|   1.4%/ 48 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 154   |      55|       2.650|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 142   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 154   |     415|      15.616|   0.1%/463|   0.1%/563|   0.1%/599|   0.1%/640 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 154   |    9179|     241.568|   0.1%/987|   0.1%/986|   0.1%/986|   0.1%/986 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 102   |      61|      11.173|   0.1%/713|   0.2%/406|   0.2%/362|   0.2%/324 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 127   |      77|       4.743|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 154   |   11365|     594.806|   0.5%/138|   0.5%/144|   0.5%/146|   0.5%/147 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 154   |    4725|       3.369|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 154   |   20411|     413.211|   1.8%/ 39|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 154   |     460|      91.024|   2.4%/ 28|   2.1%/ 33|   2.0%/ 35|   1.9%/ 36 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 154   |     185|      45.345|   0.8%/ 84|   0.9%/ 78|   0.9%/ 76|   0.9%/ 75 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 154   |      93|       8.325|   0.4%/157|   0.6%/126|   0.6%/119|   0.6%/114 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 154   |     625|     107.316|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 154   |    1740|     168.006|   1.1%/ 60|   1.1%/ 65|   1.0%/ 66|   1.0%/ 67 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 154   |    6589|     377.203|   0.5%/140|   0.5%/135|   0.5%/134|   0.5%/132 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 154   |    5438|      54.232|   0.3%/204|   0.3%/212|   0.3%/213|   0.3%/215 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 154   |     741|     114.269|   1.0%/ 66|   0.8%/ 82|   0.8%/ 87|   0.7%/ 92 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 133   |      83|      61.107|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 150   |     872|       8.834|   2.7%/ 25|   2.3%/ 29|   2.3%/ 31|   2.2%/ 32 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 154   |     336|      60.783|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 154   |   30643|     456.839|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 154   |      54|      24.657|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 154   |     155|      66.213|   2.2%/ 31|   1.1%/ 65|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 151   |      19|       5.091|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 154   |    9314|     112.011|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 154   |     289|       9.540|   0.9%/ 77|   0.7%/105|   0.6%/117|   0.5%/131 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 154   |     265|      24.738|   1.1%/ 66|   1.2%/ 59|   1.2%/ 58|   1.2%/ 57 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 154   |    2828|     170.339|   0.9%/ 75|   0.8%/ 86|   0.8%/ 89|   0.7%/ 93 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 140   |      59|       4.870|   0.9%/ 76|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 129   |      35|      21.794|   0.2%/287|   0.2%/387|   0.2%/416|   0.2%/449 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 150   |     205|      17.711|   0.3%/251|   0.1%/725|   0.1%/ ***|   0.0%/ *** |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 154   |    1868|     203.938|   1.2%/ 60|   1.2%/ 56|   1.3%/ 55|   1.3%/ 54 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 154   |     617|      63.108|   0.1%/947|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 154   |   67338|      49.469|   1.7%/ 42|   1.5%/ 45|   1.5%/ 45|   1.5%/ 46 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 154   |    7473|      27.999|   1.3%/ 55|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 154   |   21949|     263.250|   0.6%/115|   0.5%/136|   0.5%/143|   0.5%/150 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 154   |    7171|     183.278|   1.2%/ 58|   1.1%/ 61|   1.1%/ 61|   1.1%/ 62 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 154   |    1779|     361.436|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 154   |     975|     106.108|   1.5%/ 45|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 154   |   35530|     589.819|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 154   |      21|       7.620|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 154   |    1300|      10.325|   1.1%/ 64|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 154   |      15|       1.453|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 154   |    1645|      88.017|   1.0%/ 68|   0.9%/ 73|   0.9%/ 74|   0.9%/ 76 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 154   |     608|      12.790|   1.1%/ 66|   0.8%/ 91|   0.7%/101|   0.6%/113 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 154   |     535|     297.693|   1.1%/ 62|   0.6%/121|   0.4%/159|   0.3%/234 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 151   |     537|     121.401|   0.4%/167|   0.4%/193|   0.3%/200|   0.3%/208 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 152   |    1004|     153.625|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 152   |      34|      17.830|   0.3%/225|   0.4%/197|   0.4%/191|   0.4%/186 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 154   |     171|      24.993|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 151   |      83|      18.496|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 153   |     255|      37.082|   2.9%/ 24|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 154   |      86|      30.862|   0.3%/217|   0.4%/189|   0.4%/183|   0.4%/178 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 108   |     194|       7.387|   0.9%/ 73|   0.8%/ 85|   0.8%/ 87|   0.8%/ 89 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 154   |     125|       3.824|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 154   |     126|       6.219|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 154   |     159|      38.907|   0.1%/874|   0.1%/707|   0.1%/674|   0.1%/644 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 154   |   65807|     519.892|   0.8%/ 82|   0.8%/ 92|   0.7%/ 95|   0.7%/ 98 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 154   |    1010|     376.718|   0.7%/ 98|   0.7%/103|   0.7%/104|   0.7%/106 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 154   |    1238|      34.500|   3.5%/ 19|   3.4%/ 20|   3.4%/ 20|   3.3%/ 21 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 100   |      23|       0.760|   1.4%/ 49|   1.7%/ 41|   1.8%/ 39|   1.9%/ 37 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  54   |      80|      32.387|   5.9%/ 12|   5.1%/ 13|   5.0%/ 14|   5.0%/ 14 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 109   |     239|       7.966|   5.4%/ 13|   5.6%/ 12|   5.7%/ 12|   5.7%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 154   |    6258|     358.462|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 154   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 154   |     140|      21.674|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 154   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 154   |    1029|       4.993|   0.2%/289|   0.2%/455|   0.1%/530|   0.1%/635 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 154   |     602|     290.043|   0.7%/100|   0.7%/ 95|   0.7%/ 94|   0.7%/ 93 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 154   |     266|      49.539|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 154   |     698|     149.597|   1.2%/ 57|   1.1%/ 62|   1.1%/ 63|   1.1%/ 64 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 154   |    6323|      28.829|   0.1%/567|   0.1%/743|   0.1%/806|   0.1%/879 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 154   |    2049|     485.789|   0.8%/ 88|   0.7%/105|   0.6%/110|   0.6%/116 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  37   |       4|       0.448|   1.4%/ 49|   3.8%/ 18|   2.6%/ 26|   1.1%/ 63 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 154   |     362|      50.669|   6.0%/ 11|   6.0%/ 11|   6.0%/ 11|   6.1%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 154   |   30392|     945.860|   0.6%/109|   0.6%/124|   0.5%/129|   0.5%/134 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 154   |    3594|      33.115|   2.2%/ 31|   2.3%/ 30|   2.4%/ 29|   2.4%/ 29 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 154   |    2061|      53.707|   0.6%/125|   0.5%/128|   0.5%/129|   0.5%/130 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 154   |    1826|     177.649|   0.2%/417|   0.2%/423|   0.2%/425|   0.2%/427 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 154   |     199|      72.426|   0.2%/340|   0.1%/607|   0.1%/744|   0.1%/951 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 154   |    3701|     190.744|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 57 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 154   |   17304|     117.916|   0.6%/115|   0.6%/121|   0.6%/123|   0.6%/125 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  95   |      18|       1.451|   7.7%/  9|   2.2%/ 32|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 154   |    3968|     115.970|   0.9%/ 78|   0.8%/ 84|   0.8%/ 86|   0.8%/ 87 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 154   |     291|      17.954|   0.8%/ 90|   0.6%/110|   0.6%/117|   0.6%/124 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 154   |     728|     104.519|   0.3%/207|   0.2%/379|   0.1%/476|   0.1%/639 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 132   |      70|       8.873|   0.1%/466|   0.2%/406|   0.2%/389|   0.2%/372 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 154   |      27|       4.734|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 154   |      34|       6.170|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 154   |     134|      64.134|   0.1%/570|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 147   |      96|       6.060|   0.4%/171|   0.5%/127|   0.6%/119|   0.6%/112 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 154   |   14795|     251.718|   1.1%/ 62|   0.8%/ 87|   0.7%/ 96|   0.6%/107 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 154   |   29093|     617.680|   0.1%/774|   0.1%/686|   0.1%/667|   0.1%/650 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 154   |      12|       0.556|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 154   |     833|      19.628|   0.2%/418|   0.1%/798|   0.1%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 154   |    5828|     563.721|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 154   |    2008|     233.408|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 154   |     119|       6.816|   2.9%/ 24|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 154   |      21|       0.376|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 154   |      58|       0.872|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 154   |      29|       3.800|   0.0%/ --|   0.0%/ --|   1.2%/ 57|   1.2%/ 57 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 154   |      22|      15.846|   6.1%/ 11|   6.9%/ 10|   7.1%/ 10|   7.3%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 154   |      79|       6.743|   1.4%/ 51|   1.6%/ 44|   1.6%/ 43|   1.7%/ 42 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 154   |    6321|      76.011|   0.4%/180|   0.4%/169|   0.4%/167|   0.4%/164 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 154   |  185781|     563.753|   0.5%/138|   0.5%/151|   0.4%/154|   0.4%/158 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  40   |      32|       0.805|   6.8%/ 10|   4.0%/ 17|   3.3%/ 21|   2.7%/ 25 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 154   |    2627|      62.727|   1.5%/ 47|   1.5%/ 45|   1.5%/ 45|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 154   |     384|      38.860|   0.4%/194|   0.4%/184|   0.4%/182|   0.4%/180 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 154   |   41280|     621.357|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 154   |      45|      12.721|   0.8%/ 90|   0.8%/ 90|   0.8%/ 91|   0.8%/ 91 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 154   |     334|       9.775|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 40 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 154   |     410|      12.718|   2.1%/ 32|   1.8%/ 38|   1.7%/ 40|   1.6%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  33   |      34|       0.357|   3.0%/ 23|   2.7%/ 25|   2.5%/ 27|   2.4%/ 28 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 153   |     308|      17.203|   0.6%/114|   0.4%/182|   0.3%/215|   0.3%/262 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 154   |     213|      14.070|   2.3%/ 30|   1.6%/ 43|   1.4%/ 48|   1.3%/ 55 |

