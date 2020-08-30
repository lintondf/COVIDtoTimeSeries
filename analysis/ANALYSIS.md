# State and Country COVID-19 Analysis #
## Updated: at 2020-08-30 for data as of 2020-08-29 ##

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.1% of deaths and 57.9% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 151   |   32941|    1693.303|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 151   |   15954|    1796.186|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 151   |   13021|     329.553|   1.1%/ 65|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 151   |   13174|     454.332|   1.6%/ 44|   1.4%/ 50|   1.3%/ 51|   1.3%/ 53 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 151   |   11415|     531.459|   1.3%/ 51|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 151   |    9028|    1299.040|   0.2%/386|   0.2%/374|   0.2%/370|   0.2%/367 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 151   |    8211|     647.938|   0.2%/278|   0.3%/268|   0.3%/265|   0.3%/263 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 151   |    7660|     598.354|   0.2%/316|   0.2%/316|   0.2%/316|   0.2%/317 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 151   |    6718|     672.676|   0.2%/456|   0.2%/445|   0.2%/442|   0.2%/439 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 151   |    5565|     524.128|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 151   |  183287|     556.183|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 151   |  121109|     572.859|   0.8%/ 82|   0.8%/ 87|   0.8%/ 89|   0.8%/ 90 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 151   |   64381|     508.627|   0.9%/ 76|   0.8%/ 84|   0.8%/ 87|   0.8%/ 89 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 151   |   64352|      47.275|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 151   |   47367|     712.978|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 151   |   35511|     589.509|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 151   |   30594|     456.103|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 151   |   28999|     615.684|   0.1%/829|   0.1%/725|   0.1%/703|   0.1%/682 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 151   |   29895|     930.390|   0.7%/101|   0.6%/116|   0.6%/120|   0.6%/125 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 151   |   21639|     259.525|   0.7%/104|   0.6%/122|   0.5%/128|   0.5%/134 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 151   |    2137|     435.871|   0.8%/ 83|   0.7%/ 93|   0.7%/ 96|   0.7%/ 99 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 151   |      36|      49.073|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 151   |    5065|     695.916|   0.9%/ 80|   0.7%/ 94|   0.7%/ 98|   0.7%/103 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 151   |     764|     253.059|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 151   |   13021|     329.553|   1.1%/ 65|   1.0%/ 70|   1.0%/ 71|   1.0%/ 72 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 151   |    1941|     337.019|   0.2%/356|   0.2%/364|   0.2%/365|   0.2%/367 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 151   |    4468|    1253.130|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 151   |     605|     621.080|   0.1%/542|   0.1%/528|   0.1%/525|   0.1%/521 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 151   |   11415|     531.459|   1.3%/ 51|   1.1%/ 62|   1.1%/ 65|   1.0%/ 69 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 151   |    5565|     524.128|   1.3%/ 52|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 151   |      57|      40.521|   3.0%/ 23|   3.3%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 151   |     357|     199.716|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 151   |    8211|     647.938|   0.2%/278|   0.3%/268|   0.3%/265|   0.3%/263 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 151   |    3294|     489.306|   0.4%/188|   0.4%/190|   0.4%/191|   0.4%/192 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 151   |    1099|     348.262|   0.9%/ 74|   1.0%/ 70|   1.0%/ 69|   1.0%/ 69 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 151   |     449|     154.169|   0.8%/ 89|   0.8%/ 91|   0.8%/ 92|   0.8%/ 92 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 151   |     921|     206.146|   0.9%/ 75|   1.0%/ 70|   1.0%/ 69|   1.0%/ 68 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 151   |    4956|    1066.160|   0.7%/ 96|   0.7%/101|   0.7%/103|   0.7%/104 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 151   |     132|      98.400|   0.3%/234|   0.3%/224|   0.3%/221|   0.3%/219 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 151   |    3742|     618.922|   0.2%/330|   0.2%/349|   0.2%/354|   0.2%/358 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 151   |    9028|    1299.040|   0.2%/386|   0.2%/374|   0.2%/370|   0.2%/367 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 151   |    6718|     672.676|   0.2%/456|   0.2%/445|   0.2%/442|   0.2%/439 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 151   |    1864|     330.491|   0.5%/138|   0.5%/132|   0.5%/131|   0.5%/130 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 151   |    2448|     822.604|   1.2%/ 57|   1.1%/ 61|   1.1%/ 62|   1.1%/ 62 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 151   |    1514|     246.698|   0.6%/108|   0.6%/107|   0.6%/107|   0.6%/107 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 151   |     103|      96.063|   1.6%/ 42|   1.5%/ 46|   1.5%/ 46|   1.5%/ 47 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 151   |     394|     203.711|   0.6%/109|   0.6%/110|   0.6%/110|   0.6%/110 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 151   |    1320|     428.502|   1.5%/ 46|   1.4%/ 48|   1.4%/ 49|   1.4%/ 50 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 151   |     432|     317.812|   0.2%/462|   0.2%/452|   0.2%/449|   0.2%/447 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 151   |   15954|    1796.186|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 151   |     773|     368.544|   0.6%/118|   0.6%/123|   0.6%/124|   0.6%/126 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 151   |   32941|    1693.303|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 151   |    2692|     256.649|   1.0%/ 70|   0.9%/ 74|   0.9%/ 75|   0.9%/ 76 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 151   |     144|     188.808|   1.0%/ 69|   0.9%/ 76|   0.9%/ 78|   0.9%/ 80 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 151   |    4127|     353.079|   0.6%/115|   0.6%/115|   0.6%/114|   0.6%/114 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 151   |     792|     200.276|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 46 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 151   |     452|     107.109|   1.2%/ 59|   1.1%/ 61|   1.1%/ 61|   1.1%/ 62 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 151   |    7660|     598.354|   0.2%/316|   0.2%/316|   0.2%/316|   0.2%/317 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 151   |     441|     137.928|   2.1%/ 33|   2.0%/ 35|   1.9%/ 36|   1.9%/ 36 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 151   |    1043|     984.437|   0.2%/383|   0.2%/330|   0.2%/319|   0.2%/308 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 151   |    2726|     529.443|   1.3%/ 52|   1.2%/ 58|   1.2%/ 60|   1.1%/ 61 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 151   |     167|     188.915|   0.6%/109|   0.5%/127|   0.5%/132|   0.5%/138 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 151   |    1735|     253.893|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 41 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 151   |   13174|     454.332|   1.6%/ 44|   1.4%/ 50|   1.3%/ 51|   1.3%/ 53 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 151   |  183287|     556.183|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 151   |     412|     128.478|   0.9%/ 78|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 151   |      58|      93.197|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 151   |    2546|     298.284|   0.5%/132|   0.5%/130|   0.5%/129|   0.5%/127 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 151   |    1932|     253.672|   0.6%/125|   0.5%/143|   0.5%/148|   0.4%/154 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 151   |     204|     113.907|   2.1%/ 33|   2.2%/ 32|   2.2%/ 32|   2.2%/ 31 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 151   |    1121|     192.602|   0.6%/117|   0.6%/122|   0.6%/123|   0.6%/124 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 139   |      39|      66.859|   0.3%/208|   0.1%/482|   0.1%/729|   0.0%/ *** |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 151   |    1417|      43.986|   0.2%/291|   0.2%/399|   0.2%/442|   0.1%/496 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 151   |     278|      97.846|   1.6%/ 44|   1.4%/ 49|   1.4%/ 50|   1.3%/ 52 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 151   |    1498|      34.846|   0.7%/104|   0.6%/110|   0.6%/112|   0.6%/114 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 151   |     112|       3.600|   1.7%/ 41|   1.4%/ 51|   1.3%/ 54|   1.2%/ 58 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 151   |    8515|     189.484|   3.0%/ 23|   3.0%/ 23|   2.9%/ 23|   2.9%/ 24 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 151   |     877|     296.628|   0.5%/152|   0.4%/174|   0.4%/181|   0.4%/188 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 151   |     648|      25.224|   3.2%/ 22|   2.8%/ 25|   2.7%/ 25|   2.6%/ 26 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 151   |     735|      82.570|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 151   |     532|      52.826|   0.3%/213|   0.2%/321|   0.2%/364|   0.2%/417 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 151   |     193|     124.777|   0.8%/ 91|   0.7%/102|   0.7%/106|   0.6%/110 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 151   |    4206|      24.968|   1.1%/ 64|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 151   |     667|      70.894|   0.7%/ 97|   0.8%/ 91|   0.8%/ 90|   0.8%/ 89 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 151   |   10037|     870.891|   0.1%/969|   0.1%/962|   0.1%/964|   0.1%/967 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 146   |      40|       3.407|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 151   |    4968|     433.107|   1.5%/ 47|   1.3%/ 51|   1.3%/ 53|   1.3%/ 54 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 151   |     607|     183.959|   1.7%/ 41|   1.6%/ 42|   1.6%/ 42|   1.6%/ 43 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 151   |       3|       1.426|   1.1%/ 66|   0.4%/155|   0.3%/247|   0.1%/630 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 151   |  121109|     572.859|   0.8%/ 82|   0.8%/ 87|   0.8%/ 89|   0.8%/ 90 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 151   |     610|      87.713|   1.5%/ 47|   1.4%/ 49|   1.4%/ 49|   1.4%/ 50 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 151   |      55|       2.650|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 139   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 151   |     413|      15.563|   0.2%/376|   0.2%/402|   0.2%/411|   0.2%/421 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 151   |    9160|     241.062|   0.1%/964|   0.1%/951|   0.1%/948|   0.1%/945 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  99   |      61|      11.105|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 124   |      77|       4.727|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 151   |   11204|     586.374|   0.5%/134|   0.5%/141|   0.5%/143|   0.5%/144 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 151   |    4719|       3.366|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 151   |   19487|     394.502|   1.9%/ 37|   1.7%/ 42|   1.6%/ 43|   1.6%/ 44 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 151   |     434|      85.859|   2.7%/ 26|   2.3%/ 31|   2.2%/ 32|   2.0%/ 34 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 151   |     180|      44.100|   0.7%/ 96|   0.7%/ 95|   0.7%/ 94|   0.7%/ 93 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 151   |      91|       8.146|   0.3%/203|   0.4%/160|   0.5%/151|   0.5%/144 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 151   |     624|     107.215|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 151   |    1687|     162.835|   1.2%/ 59|   1.1%/ 64|   1.0%/ 66|   1.0%/ 67 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 151   |    6489|     371.470|   0.5%/128|   0.6%/119|   0.6%/116|   0.6%/114 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 151   |    5385|      53.699|   0.3%/211|   0.3%/232|   0.3%/238|   0.3%/243 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 151   |     723|     111.532|   1.2%/ 58|   1.0%/ 70|   0.9%/ 73|   0.9%/ 77 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 130   |      83|      61.110|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 147   |     816|       8.273|   3.0%/ 23|   2.7%/ 26|   2.6%/ 27|   2.5%/ 28 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 151   |     336|      60.714|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 151   |   30594|     456.103|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 151   |      54|      24.638|   0.1%/660|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 151   |     136|      58.110|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   1.1%/ 65 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 148   |      18|       4.932|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 151   |    9302|     111.875|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 151   |     284|       9.375|   1.1%/ 65|   0.8%/ 84|   0.8%/ 90|   0.7%/ 98 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 151   |     255|      23.743|   1.0%/ 67|   1.2%/ 59|   1.2%/ 57|   1.2%/ 56 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 151   |    2764|     166.443|   1.0%/ 67|   0.9%/ 74|   0.9%/ 76|   0.9%/ 78 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 137   |      58|       4.726|   1.1%/ 63|   1.3%/ 53|   1.4%/ 50|   1.4%/ 48 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 126   |      35|      21.766|   0.4%/188|   0.3%/228|   0.3%/238|   0.3%/248 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 147   |     205|      17.672|   0.4%/175|   0.2%/348|   0.2%/462|   0.1%/681 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 151   |    1795|     195.986|   1.2%/ 59|   1.2%/ 56|   1.3%/ 54|   1.3%/ 53 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 151   |     616|      63.004|   0.1%/794|   0.1%/906|   0.1%/942|   0.1%/981 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 151   |   64352|      47.275|   1.8%/ 39|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 151   |    7184|      26.916|   1.3%/ 55|   1.3%/ 53|   1.3%/ 53|   1.3%/ 52 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 151   |   21639|     259.525|   0.7%/104|   0.6%/122|   0.5%/128|   0.5%/134 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 151   |    6935|     177.232|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59|   1.2%/ 60 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 151   |    1779|     361.476|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 151   |     926|     100.832|   1.5%/ 45|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 151   |   35511|     589.509|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 151   |      19|       6.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 151   |    1255|       9.962|   1.0%/ 68|   1.1%/ 61|   1.2%/ 59|   1.2%/ 58 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 151   |      11|       1.032|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 151   |    1625|      86.956|   1.2%/ 56|   1.3%/ 53|   1.3%/ 52|   1.3%/ 51 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 151   |     596|      12.529|   1.3%/ 52|   1.1%/ 64|   1.0%/ 68|   1.0%/ 73 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 151   |     525|     292.228|   1.8%/ 39|   1.3%/ 52|   1.2%/ 57|   1.1%/ 63 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 148   |     531|     120.200|   0.4%/160|   0.4%/188|   0.4%/197|   0.3%/207 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 149   |    1046|     160.059|   0.1%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 149   |      34|      17.627|   0.4%/176|   0.5%/141|   0.5%/134|   0.5%/127 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 151   |     154|      22.532|   3.4%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 148   |      83|      18.593|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 150   |     237|      34.501|   3.4%/ 20|   3.3%/ 21|   3.2%/ 21|   3.2%/ 22 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 151   |      85|      30.510|   0.4%/192|   0.4%/156|   0.5%/149|   0.5%/142 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 105   |     189|       7.209|   1.0%/ 70|   0.7%/104|   0.6%/117|   0.5%/131 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 151   |     125|       3.817|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 151   |     126|       6.208|   0.1%/ ***|   0.1%/918|   0.1%/883|   0.1%/849 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 151   |     158|      38.785|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 151   |   64381|     508.627|   0.9%/ 76|   0.8%/ 84|   0.8%/ 87|   0.8%/ 89 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 151   |     990|     369.286|   0.8%/ 89|   0.8%/ 92|   0.7%/ 93|   0.7%/ 93 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 151   |    1106|      30.828|   3.9%/ 17|   4.0%/ 17|   4.0%/ 17|   4.0%/ 17 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  97   |      22|       0.721|   1.0%/ 67|   0.8%/ 83|   0.8%/ 88|   0.8%/ 92 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  51   |      69|      27.999|   6.1%/ 11|   5.2%/ 13|   4.7%/ 14|   4.3%/ 16 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 106   |     203|       6.753|   5.2%/ 13|   5.5%/ 13|   5.5%/ 12|   5.6%/ 12 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 151   |    6245|     357.737|   0.1%/ ***|   0.1%/905|   0.1%/875|   0.1%/847 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 151   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 151   |     139|      21.451|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 151   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 151   |    1025|       4.973|   0.3%/234|   0.2%/345|   0.2%/391|   0.2%/452 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 151   |     589|     283.624|   0.7%/102|   0.7%/100|   0.7%/ 99|   0.7%/ 98 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 151   |     266|      49.496|   0.1%/977|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 151   |     678|     145.289|   1.1%/ 64|   0.9%/ 77|   0.9%/ 81|   0.8%/ 86 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 151   |    6307|      28.754|   0.1%/468|   0.1%/577|   0.1%/612|   0.1%/651 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 151   |    2011|     476.674|   0.9%/ 79|   0.7%/ 95|   0.7%/100|   0.7%/105 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  34   |       4|       0.448|   3.7%/ 19|   3.2%/ 22|   5.4%/ 13|   7.9%/  9 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 151   |     304|      42.461|   6.2%/ 11|   6.4%/ 11|   6.4%/ 11|   6.5%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 151   |   29895|     930.390|   0.7%/101|   0.6%/116|   0.6%/120|   0.6%/125 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 151   |    3358|      30.948|   2.2%/ 32|   2.4%/ 29|   2.4%/ 29|   2.4%/ 28 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 151   |    2029|      52.856|   0.6%/113|   0.6%/110|   0.6%/110|   0.6%/109 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 151   |    1817|     176.784|   0.2%/395|   0.2%/390|   0.2%/389|   0.2%/387 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 151   |     198|      72.198|   0.2%/319|   0.1%/746|   0.1%/ ***|   0.0%/ *** |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 151   |    3569|     183.906|   1.4%/ 51|   1.3%/ 53|   1.3%/ 53|   1.3%/ 54 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 151   |   17013|     115.938|   0.6%/109|   0.6%/115|   0.6%/117|   0.6%/118 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  92   |      17|       1.354|   5.0%/ 14|   5.1%/ 13|   5.1%/ 14|   5.0%/ 14 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 151   |    3874|     113.212|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 151   |     286|      17.635|   0.9%/ 78|   0.8%/ 90|   0.7%/ 94|   0.7%/ 98 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 151   |     725|     104.067|   0.4%/162|   0.3%/266|   0.2%/316|   0.2%/390 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 129   |      70|       8.823|   0.1%/500|   0.1%/480|   0.1%/468|   0.2%/454 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 151   |      27|       4.734|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 151   |      34|       6.159|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 151   |     134|      63.991|   0.2%/344|   0.1%/546|   0.1%/633|   0.1%/752 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 144   |      94|       5.943|   0.2%/309|   0.3%/222|   0.3%/206|   0.4%/192 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 151   |   14485|     246.445|   1.3%/ 53|   1.0%/ 72|   0.9%/ 80|   0.8%/ 88 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 151   |   28999|     615.684|   0.1%/829|   0.1%/725|   0.1%/703|   0.1%/682 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 151   |      12|       0.550|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 151   |     831|      19.589|   0.2%/283|   0.2%/394|   0.2%/436|   0.1%/489 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 151   |    5827|     563.612|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 151   |    2005|     233.063|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 151   |     108|       6.147|   2.9%/ 24|   3.0%/ 23|   3.1%/ 23|   3.1%/ 22 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 151   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 151   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 151   |      29|       3.829|   0.2%/319|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 151   |       8|       5.865|   4.7%/ 15|   5.5%/ 13|   5.7%/ 12|   5.9%/ 12 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 151   |      75|       6.438|   1.4%/ 51|   1.6%/ 43|   1.7%/ 41|   1.7%/ 40 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 151   |    6247|      75.126|   0.4%/192|   0.4%/182|   0.4%/180|   0.4%/177 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 151   |  183287|     556.183|   0.6%/123|   0.5%/130|   0.5%/131|   0.5%/133 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  37   |      30|       0.740|   6.3%/ 11|   6.1%/ 11|   5.4%/ 13|   4.4%/ 16 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 151   |    2507|      59.873|   1.4%/ 48|   1.5%/ 46|   1.5%/ 46|   1.5%/ 45 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 151   |     380|      38.429|   0.3%/209|   0.3%/199|   0.4%/197|   0.4%/195 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 151   |   47367|     712.978|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 151   |      44|      12.450|   0.8%/ 82|   0.9%/ 77|   0.9%/ 76|   0.9%/ 75 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 151   |     316|       9.268|   2.2%/ 31|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 151   |     389|      12.073|   2.4%/ 29|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  30   |      32|       0.330|   1.9%/ 36|   3.3%/ 21|   3.0%/ 23|   2.7%/ 26 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 150   |     309|      17.278|   0.4%/189|   0.2%/283|   0.2%/324|   0.2%/379 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 151   |     200|      13.210|   3.1%/ 22|   2.6%/ 27|   2.4%/ 28|   2.3%/ 30 |

