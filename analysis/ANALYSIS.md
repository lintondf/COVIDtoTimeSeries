# State and Country COVID-19 Analysis #
## Updated: at 2020-09-25 for data as of 2020-09-24 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.4% of deaths and 38.6% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.0% of deaths and 56.0% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 177   |   33106|    1701.786|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 177   |   16089|    1811.403|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 177   |   15702|     541.515|   0.7%/104|   0.6%/123|   0.5%/128|   0.5%/135 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 177   |   15519|     392.759|   0.6%/113|   0.6%/124|   0.5%/127|   0.5%/131 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 177   |   13822|     643.528|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 177   |    9354|    1346.054|   0.1%/485|   0.1%/484|   0.1%/483|   0.1%/482 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 177   |    8771|     692.181|   0.2%/278|   0.2%/279|   0.2%/280|   0.2%/280 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 177   |    8019|     626.370|   0.2%/317|   0.2%/299|   0.2%/294|   0.2%/290 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 177   |    7029|     703.798|   0.1%/495|   0.1%/509|   0.1%/513|   0.1%/516 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 177   |    6881|     648.112|   0.7%/105|   0.6%/122|   0.5%/127|   0.5%/132 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 177   |  203153|     616.467|   0.4%/181|   0.4%/190|   0.4%/193|   0.4%/195 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 177   |  140360|     663.917|   0.5%/134|   0.5%/146|   0.5%/149|   0.5%/153 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 177   |   92127|      67.679|   1.3%/ 51|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 177   |   75839|     599.153|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/134 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 177   |   41913|     630.878|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 177   |   35743|     593.358|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 177   |   31971|     995.020|   0.3%/201|   0.3%/235|   0.3%/245|   0.3%/256 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 177   |   31333|     467.131|   0.1%/477|   0.2%/413|   0.2%/400|   0.2%/387 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 177   |   30799|     653.904|   0.2%/347|   0.2%/328|   0.2%/324|   0.2%/320 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 177   |   24842|     297.944|   0.7%/106|   0.7%/102|   0.7%/101|   0.7%/100 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 177   |    2514|     512.735|   0.5%/130|   0.5%/145|   0.5%/149|   0.5%/153 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 177   |      47|      64.905|   0.5%/149|   0.3%/215|   0.3%/243|   0.2%/279 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 177   |    5582|     766.888|   0.3%/200|   0.3%/235|   0.3%/245|   0.3%/256 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 177   |    1264|     418.893|   1.0%/ 66|   0.9%/ 80|   0.8%/ 85|   0.8%/ 90 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 177   |   15519|     392.759|   0.6%/113|   0.6%/124|   0.5%/127|   0.5%/131 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 177   |    2031|     352.634|   0.2%/368|   0.2%/362|   0.2%/360|   0.2%/358 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 177   |    4497|    1261.315|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 177   |     627|     643.477|   0.2%/338|   0.2%/299|   0.2%/291|   0.2%/282 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 177   |   13822|     643.528|   0.8%/ 90|   0.7%/ 96|   0.7%/ 98|   0.7%/100 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 177   |    6881|     648.112|   0.7%/105|   0.6%/122|   0.5%/127|   0.5%/132 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 177   |     134|      94.730|   1.6%/ 42|   1.2%/ 59|   1.1%/ 65|   0.9%/ 73 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 177   |     467|     261.601|   0.8%/ 83|   0.7%/ 99|   0.7%/104|   0.6%/109 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 177   |    8771|     692.181|   0.2%/278|   0.2%/279|   0.2%/280|   0.2%/280 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 177   |    3550|     527.376|   0.3%/250|   0.3%/260|   0.3%/262|   0.3%/265 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 177   |    1313|     416.189|   0.6%/115|   0.6%/123|   0.6%/125|   0.5%/128 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 177   |     622|     213.498|   1.4%/ 50|   1.5%/ 48|   1.5%/ 47|   1.5%/ 46 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 177   |    1151|     257.557|   0.7%/102|   0.6%/112|   0.6%/115|   0.6%/118 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 177   |    5461|    1174.767|   0.3%/209|   0.3%/239|   0.3%/248|   0.3%/257 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 177   |     140|     104.172|   0.3%/261|   0.3%/248|   0.3%/244|   0.3%/241 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 177   |    3910|     646.739|   0.2%/432|   0.2%/450|   0.2%/455|   0.2%/459 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 177   |    9354|    1346.054|   0.1%/485|   0.1%/484|   0.1%/483|   0.1%/482 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 177   |    7029|     703.798|   0.1%/495|   0.1%/509|   0.1%/513|   0.1%/516 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 177   |    2046|     362.739|   0.4%/191|   0.4%/193|   0.4%/194|   0.4%/194 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 177   |    2907|     976.924|   0.6%/119|   0.5%/134|   0.5%/138|   0.5%/142 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 177   |    1910|     311.270|   0.9%/ 81|   0.9%/ 79|   0.9%/ 78|   0.9%/ 78 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 177   |     166|     155.777|   2.0%/ 35|   2.0%/ 34|   2.1%/ 34|   2.1%/ 33 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 177   |     462|     238.629|   0.7%/105|   0.7%/100|   0.7%/ 99|   0.7%/ 98 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 177   |    1585|     514.723|   0.6%/109|   0.5%/126|   0.5%/131|   0.5%/137 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 177   |     439|     322.962|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 177   |   16089|    1811.403|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 177   |     863|     411.800|   0.4%/182|   0.4%/197|   0.3%/201|   0.3%/205 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 177   |   33106|    1701.786|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 177   |    3364|     320.792|   0.8%/ 84|   0.8%/ 87|   0.8%/ 88|   0.8%/ 89 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 177   |     199|     261.216|   1.8%/ 39|   1.9%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 177   |    4712|     403.124|   0.5%/135|   0.5%/136|   0.5%/137|   0.5%/137 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 177   |     986|     249.285|   0.8%/ 92|   0.7%/101|   0.7%/103|   0.7%/105 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 177   |     547|     129.728|   0.6%/118|   0.5%/137|   0.5%/143|   0.5%/149 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 177   |    8019|     626.370|   0.2%/317|   0.2%/299|   0.2%/294|   0.2%/290 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 177   |     641|     200.642|   1.4%/ 50|   1.3%/ 52|   1.3%/ 53|   1.3%/ 54 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 177   |    1100|    1038.213|   0.3%/273|   0.3%/250|   0.3%/245|   0.3%/240 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 177   |    3329|     646.652|   0.7%/103|   0.6%/118|   0.6%/123|   0.5%/127 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 177   |     204|     230.399|   1.0%/ 66|   1.1%/ 60|   1.2%/ 59|   1.2%/ 58 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 177   |    2342|     342.783|   1.0%/ 67|   1.0%/ 72|   0.9%/ 73|   0.9%/ 75 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 177   |   15702|     541.515|   0.7%/104|   0.6%/123|   0.5%/128|   0.5%/135 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 177   |  203153|     616.467|   0.4%/181|   0.4%/190|   0.4%/193|   0.4%/195 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 177   |     450|     140.292|   0.3%/265|   0.2%/367|   0.2%/405|   0.2%/452 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 177   |      58|      92.950|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 177   |    3058|     358.265|   0.8%/ 86|   0.9%/ 79|   0.9%/ 77|   0.9%/ 75 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 177   |    2077|     272.726|   0.4%/195|   0.4%/194|   0.4%/193|   0.4%/193 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 177   |     335|     186.872|   1.6%/ 44|   1.5%/ 47|   1.5%/ 47|   1.4%/ 48 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 177   |    1271|     218.265|   0.4%/159|   0.4%/169|   0.4%/173|   0.4%/176 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 165   |      50|      87.096|   0.1%/634|   0.1%/598|   0.1%/587|   0.1%/576 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 177   |    1447|      44.905|   0.1%/490|   0.1%/470|   0.1%/464|   0.2%/459 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 177   |     380|     133.483|   1.0%/ 71|   0.8%/ 82|   0.8%/ 85|   0.8%/ 88 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 177   |    1710|      39.770|   0.5%/141|   0.5%/147|   0.5%/149|   0.5%/150 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 177   |     161|       5.165|   1.7%/ 41|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 177   |   14544|     323.651|   2.2%/ 32|   2.1%/ 32|   2.1%/ 32|   2.1%/ 32 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 177   |     946|     319.791|   0.3%/244|   0.3%/261|   0.3%/265|   0.3%/269 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 177   |     941|      36.640|   0.6%/116|   0.2%/292|   0.1%/465|   0.1%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 177   |     771|      86.558|   0.3%/261|   0.3%/222|   0.3%/214|   0.3%/207 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 177   |     584|      58.043|   0.3%/210|   0.3%/224|   0.3%/228|   0.3%/233 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 177   |     229|     148.705|   0.9%/ 79|   0.9%/ 75|   0.9%/ 74|   1.0%/ 73 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 177   |    5118|      30.382|   0.7%/106|   0.6%/116|   0.6%/119|   0.6%/122 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 177   |     806|      85.639|   0.7%/106|   0.6%/110|   0.6%/111|   0.6%/112 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 177   |    9958|     864.056|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 172   |      40|       3.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 177   |    8276|     721.574|   0.6%/123|   0.4%/174|   0.4%/193|   0.3%/218 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 177   |     803|     243.180|   1.1%/ 65|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 177   |      17|       7.207|   3.6%/ 19|   2.7%/ 25|   2.5%/ 28|   2.3%/ 30 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 177   |  140360|     663.917|   0.5%/134|   0.5%/146|   0.5%/149|   0.5%/153 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 177   |     801|     115.283|   0.8%/ 90|   0.6%/110|   0.6%/116|   0.6%/123 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 177   |      56|       2.695|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 165   |       1|       0.091|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 177   |     417|      15.721|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 177   |    9289|     244.454|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 125   |      62|      11.285|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 150   |      82|       5.055|   0.1%/497|   0.2%/414|   0.2%/398|   0.2%/383 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 177   |   12491|     653.721|   0.4%/186|   0.3%/200|   0.3%/204|   0.3%/208 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 177   |    4745|       3.384|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 177   |   25535|     516.956|   0.8%/ 86|   0.6%/107|   0.6%/114|   0.6%/122 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 177   |     796|     157.291|   2.6%/ 26|   2.6%/ 26|   2.6%/ 26|   2.7%/ 26 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 177   |     260|      63.822|   1.5%/ 47|   1.6%/ 44|   1.6%/ 44|   1.6%/ 43 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 177   |     118|      10.542|   0.9%/ 76|   1.0%/ 72|   1.0%/ 71|   1.0%/ 70 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 177   |     639|     109.728|   0.2%/427|   0.2%/365|   0.2%/351|   0.2%/339 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 177   |    2153|     207.894|   0.6%/112|   0.5%/144|   0.4%/156|   0.4%/170 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 177   |    7340|     420.205|   0.3%/232|   0.3%/274|   0.2%/287|   0.2%/302 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 177   |    5844|      58.285|   0.3%/227|   0.3%/232|   0.3%/233|   0.3%/234 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 177   |     836|     128.952|   0.4%/161|   0.3%/215|   0.3%/234|   0.3%/258 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 156   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 173   |    1186|      12.019|   1.2%/ 56|   1.0%/ 68|   1.0%/ 72|   0.9%/ 76 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 177   |     341|      61.624|   0.1%/605|   0.1%/510|   0.1%/490|   0.1%/471 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 177   |   31333|     467.131|   0.1%/477|   0.2%/413|   0.2%/400|   0.2%/387 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 177   |      53|      24.612|   0.1%/510|   0.2%/393|   0.2%/370|   0.2%/349 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 177   |     111|      47.112|   0.4%/160|   0.3%/245|   0.3%/277|   0.2%/317 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 174   |      19|       5.198|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 177   |    9411|     113.183|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 177   |     302|       9.962|   0.3%/248|   0.2%/311|   0.2%/331|   0.2%/354 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 177   |     352|      32.850|   1.5%/ 47|   1.6%/ 44|   1.6%/ 43|   1.6%/ 42 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 177   |    3179|     191.487|   0.6%/124|   0.5%/131|   0.5%/133|   0.5%/134 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 163   |      65|       5.359|   0.3%/231|   0.2%/328|   0.2%/362|   0.2%/404 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 152   |      40|      25.090|   0.1%/657|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 173   |     227|      19.619|   0.4%/188|   0.3%/206|   0.3%/211|   0.3%/217 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 177   |    2267|     247.491|   0.6%/109|   0.5%/128|   0.5%/134|   0.5%/141 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 177   |     649|      66.419|   0.8%/ 90|   0.9%/ 75|   1.0%/ 72|   1.0%/ 69 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 177   |   92127|      67.679|   1.3%/ 51|   1.3%/ 54|   1.3%/ 54|   1.3%/ 55 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 177   |   10079|      37.761|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53|   1.3%/ 53 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 177   |   24842|     297.944|   0.7%/106|   0.7%/102|   0.7%/101|   0.7%/100 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 177   |    8907|     227.644|   0.9%/ 79|   0.8%/ 85|   0.8%/ 86|   0.8%/ 87 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 177   |    1793|     364.326|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 177   |    1323|     143.950|   1.6%/ 43|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 177   |   35743|     593.358|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 177   |      76|      27.994|   6.1%/ 11|   7.7%/  9|   4.3%/ 16|   3.2%/ 21 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 177   |    1567|      12.445|   0.6%/118|   0.5%/142|   0.5%/149|   0.4%/158 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 177   |      35|       3.243|   4.1%/ 17|   4.5%/ 15|   4.6%/ 15|   4.6%/ 15 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 177   |    1720|      92.072|   0.3%/214|   0.3%/269|   0.2%/287|   0.2%/306 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 177   |     668|      14.038|   0.6%/118|   0.6%/123|   0.6%/124|   0.6%/125 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 177   |     493|     274.614|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 174   |     592|     133.976|   0.5%/145|   0.5%/141|   0.5%/140|   0.5%/139 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 175   |    1059|     162.093|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 175   |      36|      19.006|   0.2%/373|   0.2%/435|   0.2%/453|   0.1%/473 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 177   |     334|      48.898|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 174   |      82|      18.323|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 176   |     496|      72.223|   2.6%/ 26|   2.5%/ 27|   2.5%/ 28|   2.5%/ 28 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 177   |      88|      31.363|   0.1%/935|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 131   |     228|       8.684|   0.7%/101|   0.7%/105|   0.7%/106|   0.6%/107 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 177   |     130|       3.976|   0.1%/ ***|   0.1%/893|   0.1%/855|   0.1%/818 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 177   |     129|       6.380|   0.1%/495|   0.2%/445|   0.2%/434|   0.2%/423 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 177   |     162|      39.652|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 177   |   75839|     599.153|   0.6%/118|   0.5%/128|   0.5%/131|   0.5%/134 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 177   |    1248|     465.277|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 70 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 177   |    2038|      56.809|   2.0%/ 35|   1.7%/ 40|   1.7%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 123   |      49|       1.645|   3.5%/ 20|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  77   |     119|      48.413|   1.6%/ 44|   1.4%/ 50|   1.4%/ 51|   1.3%/ 53 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 132   |     461|      15.362|   2.4%/ 29|   2.0%/ 34|   2.0%/ 35|   1.9%/ 37 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 177   |    6339|     363.113|   0.1%/ ***|   0.1%/946|   0.1%/929|   0.1%/911 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 177   |      22|       4.418|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 177   |     150|      23.186|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 177   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 177   |    1116|       5.412|   0.2%/294|   0.2%/355|   0.2%/377|   0.2%/401 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 177   |     710|     341.637|   0.8%/ 87|   0.8%/ 83|   0.8%/ 82|   0.9%/ 81 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 177   |     267|      49.755|   0.1%/843|   0.1%/698|   0.1%/668|   0.1%/641 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 177   |     880|     188.563|   1.1%/ 60|   1.2%/ 59|   1.2%/ 59|   1.2%/ 59 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 177   |    6450|      29.408|   0.1%/843|   0.1%/935|   0.1%/961|   0.1%/988 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 177   |    2312|     548.108|   0.5%/127|   0.5%/135|   0.5%/137|   0.5%/139 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  60   |       7|       0.805|   2.6%/ 26|   2.1%/ 33|   2.0%/ 34|   1.9%/ 36 |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 177   |     781|     109.169|   3.1%/ 22|   2.7%/ 25|   2.6%/ 26|   2.5%/ 27 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 177   |   31971|     995.020|   0.3%/201|   0.3%/235|   0.3%/245|   0.3%/256 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 177   |    5298|      48.818|   1.3%/ 54|   1.2%/ 59|   1.1%/ 61|   1.1%/ 62 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 177   |    2344|      61.080|   0.6%/114|   0.6%/110|   0.6%/109|   0.6%/108 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 177   |    1921|     186.887|   0.3%/238|   0.3%/214|   0.3%/209|   0.3%/204 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 177   |     213|      77.443|   0.3%/253|   0.3%/262|   0.3%/265|   0.3%/267 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 177   |    4640|     239.108|   0.9%/ 77|   0.8%/ 83|   0.8%/ 85|   0.8%/ 87 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 177   |   19809|     134.988|   0.6%/112|   0.6%/111|   0.6%/110|   0.6%/110 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 118   |      28|       2.249|   4.4%/ 16|   1.3%/ 55|   1.3%/ 55|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 177   |    4619|     135.001|   0.7%/105|   0.6%/110|   0.6%/111|   0.6%/113 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 177   |     307|      18.938|   0.2%/334|   0.1%/519|   0.1%/599|   0.1%/708 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 177   |     748|     107.396|   0.1%/470|   0.1%/574|   0.1%/606|   0.1%/642 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 155   |      72|       9.171|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 177   |      27|       4.734|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 177   |      41|       7.442|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 177   |     141|      67.463|   0.2%/421|   0.2%/384|   0.2%/374|   0.2%/364 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 170   |      99|       6.201|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 177   |   16510|     280.906|   0.5%/149|   0.4%/190|   0.3%/204|   0.3%/220 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 177   |   30799|     653.904|   0.2%/347|   0.2%/328|   0.2%/324|   0.2%/320 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 177   |      13|       0.601|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 177   |     840|      19.795|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 177   |    5874|     568.214|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 177   |    2052|     238.501|   0.1%/610|   0.1%/533|   0.1%/516|   0.1%/500 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 177   |     193|      11.004|   1.7%/ 41|   1.4%/ 48|   1.4%/ 51|   1.3%/ 53 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 177   |      21|       0.376|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 177   |      58|       0.872|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 177   |      44|       5.889|   0.9%/ 80|   0.9%/ 78|   0.9%/ 78|   0.9%/ 78 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 177   |      82|      60.184|   3.6%/ 19|   2.7%/ 25|   2.5%/ 27|   2.3%/ 30 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 177   |     137|      11.707|   2.8%/ 25|   3.0%/ 23|   3.0%/ 23|   3.1%/ 22 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 177   |    7720|      92.837|   0.9%/ 78|   0.9%/ 74|   1.0%/ 73|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 177   |  203153|     616.467|   0.4%/181|   0.4%/190|   0.4%/193|   0.4%/195 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  63   |      69|       1.707|   2.4%/ 29|   2.0%/ 35|   1.9%/ 36|   1.9%/ 37 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 177   |    3858|      92.119|   1.6%/ 43|   1.6%/ 44|   1.6%/ 44|   1.6%/ 44 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 177   |     409|      41.394|   0.2%/341|   0.2%/398|   0.2%/416|   0.2%/436 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 177   |   41913|     630.878|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 177   |      47|      13.270|   0.2%/291|   0.2%/334|   0.2%/343|   0.2%/353 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 177   |     459|      13.452|   1.3%/ 52|   1.2%/ 56|   1.2%/ 58|   1.2%/ 59 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 177   |     587|      18.230|   1.7%/ 41|   1.6%/ 42|   1.6%/ 43|   1.6%/ 43 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  56   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 176   |     337|      18.823|   0.4%/190|   0.3%/210|   0.3%/216|   0.3%/222 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 177   |     239|      15.792|   0.2%/406|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

