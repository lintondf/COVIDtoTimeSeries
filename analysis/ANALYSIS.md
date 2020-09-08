# State and Country COVID-19 Analysis #
## Updated: at 2020-09-08 for data as of 2020-09-07 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.2% of deaths and 39.5% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.8% of deaths and 57.2% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 160   |   33007|    1696.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 160   |   15981|    1799.250|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 160   |   14020|     354.817|   0.9%/ 81|   0.8%/ 89|   0.8%/ 92|   0.7%/ 94 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 160   |   14139|     487.630|   1.1%/ 61|   0.9%/ 73|   0.9%/ 77|   0.9%/ 81 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 160   |   12262|     570.939|   0.9%/ 75|   0.7%/ 96|   0.7%/103|   0.6%/111 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 160   |    9148|    1316.369|   0.1%/466|   0.1%/485|   0.1%/490|   0.1%/496 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 160   |    8403|     663.132|   0.3%/267|   0.3%/259|   0.3%/257|   0.3%/255 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 160   |    7782|     607.884|   0.2%/378|   0.2%/401|   0.2%/408|   0.2%/414 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 160   |    6824|     683.305|   0.2%/452|   0.2%/456|   0.2%/458|   0.2%/459 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 160   |    6162|     580.413|   1.1%/ 61|   1.1%/ 65|   1.0%/ 66|   1.0%/ 68 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 160   |  190753|     578.840|   0.5%/149|   0.4%/162|   0.4%/166|   0.4%/169 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 160   |  128618|     608.376|   0.7%/100|   0.6%/110|   0.6%/113|   0.6%/115 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 160   |   73513|      54.005|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 160   |   68684|     542.626|   0.8%/ 91|   0.7%/100|   0.7%/103|   0.7%/106 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 160   |   41155|     619.479|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 160   |   35564|     590.391|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 160   |   30749|     458.422|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 160   |   30850|     960.115|   0.6%/124|   0.5%/139|   0.5%/143|   0.5%/148 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 160   |   29378|     623.737|   0.1%/473|   0.2%/410|   0.2%/397|   0.2%/384 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 160   |   22562|     270.601|   0.5%/127|   0.5%/145|   0.5%/150|   0.4%/155 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 160   |    2306|     470.357|   0.8%/ 86|   0.8%/ 89|   0.8%/ 90|   0.8%/ 91 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 160   |      43|      58.756|   1.5%/ 45|   1.6%/ 43|   1.6%/ 42|   1.6%/ 42 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 160   |    5310|     729.592|   0.6%/112|   0.5%/134|   0.5%/141|   0.5%/149 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 160   |     912|     302.115|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36|   1.9%/ 36 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 160   |   14020|     354.817|   0.9%/ 81|   0.8%/ 89|   0.8%/ 92|   0.7%/ 94 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 160   |    1973|     342.529|   0.2%/339|   0.2%/332|   0.2%/330|   0.2%/328 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 160   |    4471|    1254.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 160   |     610|     626.259|   0.1%/656|   0.1%/687|   0.1%/696|   0.1%/706 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 160   |   12262|     570.939|   0.9%/ 75|   0.7%/ 96|   0.7%/103|   0.6%/111 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 160   |    6162|     580.413|   1.1%/ 61|   1.1%/ 65|   1.0%/ 66|   1.0%/ 68 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 160   |      87|      61.327|   3.9%/ 18|   4.1%/ 17|   4.2%/ 16|   4.3%/ 16 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 160   |     406|     227.291|   1.4%/ 51|   1.1%/ 60|   1.1%/ 63|   1.0%/ 67 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 160   |    8403|     663.132|   0.3%/267|   0.3%/259|   0.3%/257|   0.3%/255 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 160   |    3384|     502.688|   0.3%/220|   0.3%/235|   0.3%/239|   0.3%/243 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 160   |    1182|     374.709|   0.8%/ 89|   0.8%/ 91|   0.8%/ 92|   0.7%/ 93 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 160   |     483|     165.634|   0.8%/ 84|   0.8%/ 82|   0.9%/ 81|   0.9%/ 81 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 160   |    1006|     225.099|   0.9%/ 74|   0.9%/ 73|   1.0%/ 73|   1.0%/ 73 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 160   |    5168|    1111.789|   0.5%/140|   0.4%/167|   0.4%/176|   0.4%/185 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 160   |     135|     100.278|   0.2%/311|   0.2%/339|   0.2%/347|   0.2%/356 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 160   |    3809|     630.104|   0.2%/344|   0.2%/352|   0.2%/354|   0.2%/357 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 160   |    9148|    1316.369|   0.1%/466|   0.1%/485|   0.1%/490|   0.1%/496 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 160   |    6824|     683.305|   0.2%/452|   0.2%/456|   0.2%/458|   0.2%/459 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 160   |    1924|     341.216|   0.4%/187|   0.3%/206|   0.3%/211|   0.3%/217 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 160   |    2655|     891.931|   0.9%/ 80|   0.7%/ 93|   0.7%/ 97|   0.7%/101 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 160   |    1644|     267.790|   1.0%/ 67|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 160   |     118|     110.859|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 160   |     411|     212.267|   0.4%/160|   0.4%/190|   0.3%/199|   0.3%/210 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 160   |    1439|     467.243|   1.0%/ 67|   0.9%/ 79|   0.8%/ 83|   0.8%/ 87 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 160   |     435|     319.738|   0.1%/979|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 160   |   15981|    1799.250|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 160   |     810|     386.407|   0.5%/129|   0.5%/135|   0.5%/137|   0.5%/139 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 160   |   33007|    1696.720|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 160   |    2919|     278.304|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73|   0.9%/ 73 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 160   |     156|     205.117|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64|   1.1%/ 64 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 160   |    4303|     368.121|   0.5%/144|   0.5%/153|   0.4%/156|   0.4%/158 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 160   |     876|     221.323|   1.1%/ 64|   1.0%/ 69|   1.0%/ 71|   1.0%/ 72 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 160   |     492|     116.631|   0.9%/ 75|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 160   |    7782|     607.884|   0.2%/378|   0.2%/401|   0.2%/408|   0.2%/414 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 160   |     492|     154.209|   1.5%/ 46|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 160   |    1059|     999.380|   0.1%/490|   0.1%/500|   0.1%/504|   0.1%/509 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 160   |    2968|     576.375|   1.0%/ 67|   0.9%/ 77|   0.9%/ 79|   0.8%/ 82 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 160   |     174|     197.192|   0.6%/122|   0.5%/131|   0.5%/134|   0.5%/136 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 160   |    1949|     285.169|   1.2%/ 56|   1.1%/ 64|   1.0%/ 67|   1.0%/ 70 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 160   |   14139|     487.630|   1.1%/ 61|   0.9%/ 73|   0.9%/ 77|   0.9%/ 81 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 160   |  190753|     578.840|   0.5%/149|   0.4%/162|   0.4%/166|   0.4%/169 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 160   |     430|     134.124|   0.6%/119|   0.5%/144|   0.5%/153|   0.4%/162 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 160   |      58|      92.979|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 160   |    2692|     315.365|   0.6%/120|   0.6%/115|   0.6%/114|   0.6%/113 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 160   |    1987|     260.888|   0.3%/200|   0.3%/272|   0.2%/298|   0.2%/331 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 160   |     254|     141.513|   2.2%/ 32|   2.2%/ 31|   2.2%/ 31|   2.3%/ 30 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 160   |    1174|     201.658|   0.6%/124|   0.5%/126|   0.5%/127|   0.5%/127 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 148   |      43|      74.049|   0.3%/271|   0.2%/380|   0.2%/415|   0.2%/453 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 160   |    1423|      44.160|   0.1%/719|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 160   |     320|     112.570|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 160   |    1574|      36.599|   0.6%/123|   0.5%/132|   0.5%/135|   0.5%/138 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 160   |     122|       3.913|   1.4%/ 49|   1.2%/ 56|   1.2%/ 57|   1.2%/ 59 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 160   |   10487|     233.363|   2.4%/ 29|   2.2%/ 32|   2.1%/ 32|   2.1%/ 33 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 160   |     905|     306.088|   0.4%/182|   0.3%/203|   0.3%/209|   0.3%/215 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 160   |     818|      31.842|   2.5%/ 28|   2.2%/ 32|   2.1%/ 33|   2.0%/ 35 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 160   |     737|      82.825|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 160   |     549|      54.525|   0.4%/175|   0.4%/175|   0.4%/174|   0.4%/174 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 160   |     200|     129.590|   0.6%/115|   0.5%/129|   0.5%/132|   0.5%/136 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 160   |    4568|      27.113|   0.9%/ 77|   0.8%/ 82|   0.8%/ 84|   0.8%/ 85 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 160   |     715|      76.018|   0.7%/ 93|   0.8%/ 91|   0.8%/ 90|   0.8%/ 90 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 160   |    9901|     859.117|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 155   |      40|       3.440|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 160   |    5582|     486.628|   1.3%/ 52|   1.3%/ 55|   1.3%/ 55|   1.2%/ 56 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 160   |     680|     205.949|   1.4%/ 50|   1.3%/ 54|   1.2%/ 55|   1.2%/ 57 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 160   |       7|       3.104|   7.6%/  9|   9.0%/  8|   9.4%/  7|   9.8%/  7 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 160   |  128618|     608.376|   0.7%/100|   0.6%/110|   0.6%/113|   0.6%/115 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 160   |     692|      99.509|   1.3%/ 51|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 160   |      55|       2.650|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 148   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 160   |     417|      15.717|   0.1%/617|   0.1%/848|   0.1%/934|   0.1%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 160   |    9210|     242.369|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 108   |      62|      11.302|   0.1%/610|   0.1%/496|   0.1%/478|   0.1%/463 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 133   |      78|       4.778|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 160   |   11677|     611.107|   0.5%/144|   0.5%/149|   0.5%/150|   0.5%/152 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 160   |    4735|       3.377|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 160   |   22125|     447.908|   1.5%/ 47|   1.3%/ 53|   1.2%/ 55|   1.2%/ 58 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 160   |     515|     101.741|   2.1%/ 32|   1.9%/ 37|   1.8%/ 38|   1.7%/ 40 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 160   |     198|      48.559|   1.0%/ 68|   1.1%/ 62|   1.1%/ 61|   1.2%/ 59 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 160   |      96|       8.533|   0.6%/118|   0.7%/100|   0.7%/ 96|   0.7%/ 93 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 160   |     627|     107.706|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 160   |    1869|     180.406|   1.2%/ 58|   1.2%/ 60|   1.2%/ 60|   1.2%/ 60 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 160   |    6784|     388.378|   0.5%/143|   0.5%/143|   0.5%/143|   0.5%/143 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 160   |    5549|      55.336|   0.3%/207|   0.3%/210|   0.3%/211|   0.3%/212 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 160   |     776|     119.664|   0.9%/ 75|   0.8%/ 87|   0.8%/ 91|   0.7%/ 94 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 139   |      83|      61.107|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 156   |     976|       9.891|   2.3%/ 31|   1.9%/ 36|   1.8%/ 38|   1.7%/ 39 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 160   |     337|      60.877|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 160   |   30749|     458.422|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 160   |      53|      24.607|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 160   |     121|      51.579|   0.0%/ --|   0.7%/101|   0.0%/ --|   0.0%/ -- |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 157   |      19|       5.228|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 160   |    9339|     112.316|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 160   |     295|       9.728|   0.6%/123|   0.3%/218|   0.3%/269|   0.2%/352 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 160   |     287|      26.727|   1.1%/ 64|   1.1%/ 60|   1.2%/ 60|   1.2%/ 59 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 160   |    2930|     176.488|   0.7%/ 98|   0.6%/120|   0.5%/127|   0.5%/136 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 146   |      63|       5.122|   0.8%/ 86|   0.8%/ 90|   0.8%/ 91|   0.7%/ 92 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 135   |      37|      23.022|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 156   |     212|      18.305|   0.5%/130|   0.6%/125|   0.6%/123|   0.6%/121 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 160   |    2028|     221.388|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.3%/ 52 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 160   |     623|      63.702|   0.2%/455|   0.2%/406|   0.2%/394|   0.2%/383 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 160   |   73513|      54.005|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 160   |    8106|      30.368|   1.3%/ 53|   1.4%/ 51|   1.4%/ 51|   1.4%/ 50 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 160   |   22562|     270.601|   0.5%/127|   0.5%/145|   0.5%/150|   0.4%/155 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 160   |    7646|     195.404|   1.1%/ 62|   1.1%/ 65|   1.1%/ 66|   1.0%/ 67 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 160   |    1778|     361.303|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 160   |    1068|     116.253|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 160   |   35564|     590.391|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 160   |      24|       8.905|   3.6%/ 19|   4.1%/ 17|   4.2%/ 16|   4.4%/ 16 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 160   |    1387|      11.009|   1.0%/ 68|   1.0%/ 67|   1.0%/ 67|   1.0%/ 66 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 160   |      17|       1.555|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 160   |    1672|      89.476|   0.7%/105|   0.5%/147|   0.4%/164|   0.4%/186 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 160   |     623|      13.108|   0.7%/ 95|   0.5%/152|   0.4%/178|   0.3%/217 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 160   |     532|     296.466|   0.4%/184|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 157   |     547|     123.729|   0.4%/185|   0.3%/204|   0.3%/209|   0.3%/214 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 158   |     974|     149.073|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 158   |      35|      18.308|   0.4%/167|   0.5%/148|   0.5%/144|   0.5%/140 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 160   |     204|      29.849|   3.0%/ 23|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 157   |      82|      18.389|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 159   |     295|      42.935|   2.7%/ 25|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 160   |      87|      31.191|   0.2%/409|   0.1%/491|   0.1%/523|   0.1%/564 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 114   |     203|       7.734|   0.8%/ 87|   0.8%/ 92|   0.7%/ 94|   0.7%/ 95 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 160   |     128|       3.898|   0.1%/ ***|   0.1%/ ***|   0.1%/981|   0.1%/936 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 160   |     126|       6.245|   0.1%/905|   0.1%/766|   0.1%/737|   0.1%/710 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 160   |     160|      39.223|   0.1%/719|   0.1%/627|   0.1%/608|   0.1%/590 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 160   |   68684|     542.626|   0.8%/ 91|   0.7%/100|   0.7%/103|   0.7%/106 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 160   |    1067|     397.822|   0.9%/ 78|   0.9%/ 75|   0.9%/ 74|   0.9%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 160   |    1486|      41.428|   3.1%/ 22|   2.9%/ 24|   2.9%/ 24|   2.8%/ 24 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 106   |      27|       0.898|   2.0%/ 34|   2.4%/ 29|   2.5%/ 28|   2.5%/ 27 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  60   |      94|      38.161|   4.4%/ 16|   2.4%/ 28|   1.9%/ 36|   1.3%/ 52 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 115   |     313|      10.432|   4.7%/ 15|   4.4%/ 16|   4.3%/ 16|   4.2%/ 17 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 160   |    6282|     359.866|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 160   |      22|       4.418|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 160   |     143|      22.125|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 160   |      69|       3.092|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 160   |    1055|       5.117|   0.4%/174|   0.4%/170|   0.4%/168|   0.4%/166 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 160   |     624|     300.384|   0.6%/115|   0.6%/116|   0.6%/116|   0.6%/117 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 160   |     265|      49.460|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 160   |     736|     157.737|   1.0%/ 66|   1.0%/ 71|   1.0%/ 73|   0.9%/ 74 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 160   |    6366|      29.022|   0.1%/595|   0.1%/698|   0.1%/729|   0.1%/762 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 160   |    2124|     503.379|   0.7%/100|   0.6%/115|   0.6%/120|   0.6%/124 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  43   |       5|       0.560|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 160   |     488|      68.181|   5.4%/ 13|   5.1%/ 13|   5.1%/ 14|   5.0%/ 14 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 160   |   30850|     960.115|   0.6%/124|   0.5%/139|   0.5%/143|   0.5%/148 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 160   |    3985|      36.727|   1.7%/ 40|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 160   |    2134|      55.615|   0.6%/122|   0.6%/124|   0.6%/125|   0.6%/125 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 160   |    1843|     179.360|   0.2%/416|   0.2%/419|   0.2%/419|   0.2%/420 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 160   |     203|      73.728|   0.3%/214|   0.3%/209|   0.3%/207|   0.3%/204 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 160   |    3971|     204.616|   1.2%/ 57|   1.2%/ 60|   1.1%/ 61|   1.1%/ 62 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 160   |   17912|     122.064|   0.6%/118|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 101   |      20|       1.593|   0.0%/ --|   1.9%/ 36|   1.8%/ 38|   1.8%/ 38 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 160   |    4145|     121.138|   0.8%/ 87|   0.7%/ 94|   0.7%/ 96|   0.7%/ 98 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 160   |     298|      18.391|   0.5%/133|   0.4%/187|   0.3%/208|   0.3%/235 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 160   |     733|     105.331|   0.3%/276|   0.2%/457|   0.1%/543|   0.1%/666 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 138   |      71|       9.001|   0.2%/414|   0.2%/363|   0.2%/352|   0.2%/344 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 160   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 160   |      37|       6.773|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 160   |     135|      64.675|   0.2%/379|   0.2%/424|   0.2%/436|   0.2%/448 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 153   |      98|       6.165|   0.1%/549|   0.1%/588|   0.1%/608|   0.1%/636 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 160   |   15381|     261.691|   0.9%/ 77|   0.7%/102|   0.6%/110|   0.6%/120 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 160   |   29378|     623.737|   0.1%/473|   0.2%/410|   0.2%/397|   0.2%/384 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 160   |      12|       0.562|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 160   |     836|      19.698|   0.2%/442|   0.1%/594|   0.1%/647|   0.1%/707 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 160   |    5839|     564.790|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 160   |    2015|     234.178|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 160   |     143|       8.177|   2.9%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 160   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 160   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 160   |      31|       4.127|   0.7%/100|   0.9%/ 81|   0.9%/ 77|   0.9%/ 73 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 160   |      35|      25.556|   6.7%/ 10|   7.4%/  9|   7.6%/  9|   7.7%/  9 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 160   |      88|       7.494|   2.1%/ 32|   2.5%/ 28|   2.5%/ 27|   2.6%/ 26 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 160   |    6471|      77.823|   0.6%/107|   0.7%/ 94|   0.8%/ 91|   0.8%/ 88 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 160   |  190753|     578.840|   0.5%/149|   0.4%/162|   0.4%/166|   0.4%/169 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  46   |      43|       1.064|   3.0%/ 23|   5.7%/ 12|   6.7%/ 10|   7.8%/  9 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 160   |    2909|      69.453|   1.6%/ 42|   1.7%/ 40|   1.7%/ 40|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 160   |     392|      39.589|   0.3%/234|   0.3%/248|   0.3%/252|   0.3%/256 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 160   |   41155|     619.479|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 160   |      46|      13.080|   0.6%/123|   0.5%/146|   0.4%/154|   0.4%/163 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 160   |     365|      10.680|   1.7%/ 40|   1.5%/ 47|   1.4%/ 48|   1.4%/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 160   |     448|      13.910|   1.8%/ 38|   1.6%/ 44|   1.5%/ 45|   1.5%/ 47 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  39   |      35|       0.366|   2.1%/ 32|   0.6%/109|   0.3%/260|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 159   |     304|      16.982|   0.4%/174|   0.3%/249|   0.2%/279|   0.2%/315 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 160   |     230|      15.155|   1.2%/ 58|   0.5%/153|   0.3%/258|   0.1%/834 |

