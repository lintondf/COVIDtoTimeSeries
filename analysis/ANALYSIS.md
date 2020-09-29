# State and Country COVID-19 Analysis #
## Updated: at 2020-09-29 for data as of 2020-09-28 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.3% of deaths and 38.2% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 65.9% of deaths and 55.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 181   |   33134|    1703.236|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 181   |   16113|    1814.050|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 181   |   16044|     553.309|   0.6%/111|   0.5%/127|   0.5%/132|   0.5%/137 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 181   |   15843|     400.959|   0.6%/123|   0.5%/136|   0.5%/139|   0.5%/143 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 181   |   14230|     662.526|   0.8%/ 92|   0.7%/ 97|   0.7%/ 99|   0.7%/100 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 181   |    9411|    1354.152|   0.1%/469|   0.2%/461|   0.2%/459|   0.2%/457 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 181   |    8864|     699.472|   0.3%/269|   0.3%/268|   0.3%/267|   0.3%/267 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 181   |    8091|     632.022|   0.2%/331|   0.2%/319|   0.2%/316|   0.2%/314 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 181   |    7067|     707.648|   0.1%/513|   0.1%/528|   0.1%/532|   0.1%/536 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 181   |    7041|     663.153|   0.6%/108|   0.6%/121|   0.6%/124|   0.5%/128 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 181   |  206087|     625.370|   0.4%/187|   0.4%/195|   0.4%/197|   0.3%/200 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 181   |  143088|     676.821|   0.5%/135|   0.5%/144|   0.5%/146|   0.5%/148 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 181   |   97962|      71.966|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 181   |   77375|     611.285|   0.5%/128|   0.5%/139|   0.5%/142|   0.5%/145 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 181   |   42028|     632.608|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/977 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 181   |   35815|     594.558|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 181   |   32401|    1008.386|   0.3%/198|   0.3%/219|   0.3%/225|   0.3%/231 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 181   |   31595|     471.038|   0.2%/403|   0.2%/354|   0.2%/343|   0.2%/333 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 181   |   31282|     664.156|   0.2%/357|   0.2%/345|   0.2%/342|   0.2%/339 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 181   |   25583|     306.828|   0.7%/ 99|   0.7%/ 95|   0.7%/ 93|   0.7%/ 92 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 181   |    2547|     519.361|   0.4%/175|   0.3%/216|   0.3%/229|   0.3%/245 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 181   |      51|      69.466|   0.3%/211|   0.2%/410|   0.1%/535|   0.1%/772 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 181   |    5656|     777.112|   0.4%/192|   0.3%/209|   0.3%/213|   0.3%/217 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 181   |    1348|     446.729|   1.2%/ 59|   1.1%/ 64|   1.1%/ 65|   1.0%/ 66 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 181   |   15843|     400.959|   0.6%/123|   0.5%/136|   0.5%/139|   0.5%/143 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 181   |    2045|     355.148|   0.2%/389|   0.2%/389|   0.2%/389|   0.2%/389 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 181   |    4503|    1263.108|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 181   |     632|     649.530|   0.2%/337|   0.2%/306|   0.2%/300|   0.2%/293 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 181   |   14230|     662.526|   0.8%/ 92|   0.7%/ 97|   0.7%/ 99|   0.7%/100 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 181   |    7041|     663.153|   0.6%/108|   0.6%/121|   0.6%/124|   0.5%/128 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 181   |     142|     100.064|   1.7%/ 42|   1.3%/ 52|   1.2%/ 56|   1.2%/ 60 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 181   |     477|     266.680|   0.6%/109|   0.5%/140|   0.5%/151|   0.4%/163 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 181   |    8864|     699.472|   0.3%/269|   0.3%/268|   0.3%/267|   0.3%/267 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 181   |    3593|     533.706|   0.3%/234|   0.3%/236|   0.3%/236|   0.3%/237 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 181   |    1338|     424.124|   0.5%/134|   0.5%/149|   0.5%/153|   0.4%/157 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 181   |     655|     224.715|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61|   1.1%/ 61 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 181   |    1179|     263.796|   0.7%/106|   0.6%/115|   0.6%/118|   0.6%/121 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 181   |    5518|    1186.956|   0.3%/231|   0.3%/265|   0.3%/275|   0.2%/286 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 181   |     141|     104.923|   0.2%/366|   0.2%/390|   0.2%/398|   0.2%/406 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 181   |    3936|     651.109|   0.2%/407|   0.2%/409|   0.2%/409|   0.2%/409 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 181   |    9411|    1354.152|   0.1%/469|   0.2%/461|   0.2%/459|   0.2%/457 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 181   |    7067|     707.648|   0.1%/513|   0.1%/528|   0.1%/532|   0.1%/536 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 181   |    2073|     367.614|   0.3%/200|   0.3%/205|   0.3%/206|   0.3%/208 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 181   |    2960|     994.642|   0.5%/131|   0.5%/147|   0.5%/151|   0.4%/156 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 181   |    2013|     328.047|   1.2%/ 59|   1.3%/ 54|   1.3%/ 53|   1.3%/ 51 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 181   |     179|     167.294|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 181   |     474|     245.048|   0.6%/115|   0.6%/113|   0.6%/113|   0.6%/113 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 181   |    1615|     524.466|   0.6%/124|   0.5%/145|   0.5%/152|   0.4%/159 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 181   |     440|     323.503|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 181   |   16113|    1814.050|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 181   |     876|     417.855|   0.4%/181|   0.4%/189|   0.4%/191|   0.4%/194 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 181   |   33134|    1703.236|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 181   |    3479|     331.713|   0.8%/ 82|   0.8%/ 84|   0.8%/ 85|   0.8%/ 85 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 181   |     216|     283.793|   2.3%/ 30|   2.6%/ 27|   2.6%/ 26|   2.7%/ 25 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 181   |    4799|     410.557|   0.4%/155|   0.4%/164|   0.4%/166|   0.4%/169 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 181   |    1016|     256.757|   0.8%/ 89|   0.7%/ 93|   0.7%/ 94|   0.7%/ 95 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 181   |     556|     131.769|   0.5%/143|   0.4%/175|   0.4%/185|   0.4%/197 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 181   |    8091|     632.022|   0.2%/331|   0.2%/319|   0.2%/316|   0.2%/314 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 181   |     672|     210.379|   1.2%/ 56|   1.1%/ 62|   1.1%/ 64|   1.1%/ 66 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 181   |    1111|    1048.285|   0.2%/310|   0.2%/300|   0.2%/298|   0.2%/296 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 181   |    3397|     659.763|   0.6%/116|   0.5%/135|   0.5%/140|   0.5%/146 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 181   |     216|     243.977|   1.3%/ 55|   1.4%/ 50|   1.4%/ 49|   1.5%/ 48 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 181   |    2435|     356.320|   1.0%/ 68|   1.0%/ 72|   0.9%/ 73|   0.9%/ 74 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 181   |   16044|     553.309|   0.6%/111|   0.5%/127|   0.5%/132|   0.5%/137 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 181   |  206087|     625.370|   0.4%/187|   0.4%/195|   0.4%/197|   0.3%/200 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 181   |     454|     141.679|   0.3%/234|   0.3%/269|   0.2%/278|   0.2%/288 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 181   |      58|      92.950|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 181   |    3173|     371.760|   0.7%/ 93|   0.8%/ 88|   0.8%/ 87|   0.8%/ 86 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 181   |    2107|     276.667|   0.3%/204|   0.3%/205|   0.3%/205|   0.3%/205 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 181   |     353|     196.975|   1.4%/ 49|   1.3%/ 53|   1.3%/ 54|   1.2%/ 55 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 181   |    1292|     221.904|   0.4%/160|   0.4%/170|   0.4%/172|   0.4%/175 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 169   |      52|      89.592|   0.1%/536|   0.1%/488|   0.1%/475|   0.2%/462 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 181   |    1455|      45.160|   0.1%/511|   0.1%/498|   0.1%/495|   0.1%/493 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 181   |     390|     137.032|   0.8%/ 87|   0.7%/106|   0.6%/112|   0.6%/118 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 181   |    1738|      40.414|   0.4%/168|   0.4%/184|   0.4%/189|   0.4%/194 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 181   |     174|       5.587|   1.9%/ 37|   2.0%/ 35|   2.0%/ 35|   2.0%/ 34 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 181   |   15960|     355.156|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30|   2.3%/ 30 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 181   |     956|     323.191|   0.3%/249|   0.3%/260|   0.3%/263|   0.3%/266 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 181   |     936|      36.463|   0.4%/163|   0.1%/500|   0.1%/995|   0.0%/ *** |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 181   |     784|      88.094|   0.3%/235|   0.3%/206|   0.3%/200|   0.4%/194 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 181   |     591|      58.689|   0.3%/228|   0.3%/247|   0.3%/252|   0.3%/258 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 181   |     240|     155.557|   1.0%/ 66|   1.1%/ 61|   1.2%/ 60|   1.2%/ 59 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 181   |    5233|      31.061|   0.6%/112|   0.6%/121|   0.6%/124|   0.5%/127 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 181   |     826|      87.764|   0.6%/107|   0.6%/110|   0.6%/111|   0.6%/112 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 181   |    9975|     865.573|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 176   |      40|       3.413|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 181   |    8458|     737.443|   0.5%/150|   0.3%/216|   0.3%/242|   0.3%/275 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 181   |     836|     253.367|   1.1%/ 65|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 181   |      18|       7.909|   3.0%/ 23|   2.2%/ 32|   2.0%/ 35|   1.8%/ 39 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 181   |  143088|     676.821|   0.5%/135|   0.5%/144|   0.5%/146|   0.5%/148 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 181   |     819|     117.765|   0.7%/102|   0.6%/124|   0.5%/131|   0.5%/139 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 181   |      56|       2.701|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 169   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 181   |     418|      15.745|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 181   |    9317|     245.180|   0.1%/ ***|   0.1%/947|   0.1%/932|   0.1%/918 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 129   |      62|      11.281|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 154   |      83|       5.139|   0.4%/195|   0.4%/157|   0.5%/149|   0.5%/142 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 181   |   12693|     664.319|   0.4%/168|   0.4%/170|   0.4%/171|   0.4%/171 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 181   |    4742|       3.382|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 181   |   26147|     529.335|   0.8%/ 92|   0.6%/110|   0.6%/116|   0.6%/122 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 181   |     874|     172.841|   2.4%/ 29|   2.3%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 181   |     276|      67.751|   1.4%/ 48|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 181   |     122|      10.900|   0.9%/ 79|   0.9%/ 76|   0.9%/ 76|   0.9%/ 75 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 181   |     646|     110.888|   0.2%/359|   0.2%/310|   0.2%/300|   0.2%/290 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 181   |    2178|     210.274|   0.5%/153|   0.3%/231|   0.3%/265|   0.2%/310 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 181   |    7443|     426.085|   0.3%/264|   0.2%/318|   0.2%/335|   0.2%/355 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 181   |    5911|      58.947|   0.3%/238|   0.3%/245|   0.3%/247|   0.3%/249 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 181   |     845|     130.204|   0.3%/200|   0.2%/282|   0.2%/313|   0.2%/352 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 160   |      83|      61.107|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 177   |    1223|      12.393|   1.0%/ 69|   0.8%/ 88|   0.7%/ 94|   0.7%/101 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 181   |     343|      62.022|   0.1%/586|   0.1%/509|   0.1%/493|   0.1%/477 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 181   |   31595|     471.038|   0.2%/403|   0.2%/354|   0.2%/343|   0.2%/333 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 181   |      54|      24.769|   0.1%/629|   0.1%/512|   0.1%/488|   0.1%/467 |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 181   |     112|      47.882|   0.4%/178|   0.3%/235|   0.3%/255|   0.2%/278 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 178   |      19|       5.191|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 181   |    9447|     113.609|   0.1%/888|   0.1%/791|   0.1%/769|   0.1%/748 |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 181   |     303|      10.018|   0.2%/339|   0.1%/480|   0.1%/536|   0.1%/608 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 181   |     378|      35.227|   1.5%/ 46|   1.6%/ 43|   1.6%/ 43|   1.6%/ 42 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 181   |    3249|     195.681|   0.6%/123|   0.5%/126|   0.5%/127|   0.5%/127 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 167   |      66|       5.403|   0.3%/253|   0.2%/316|   0.2%/334|   0.2%/354 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 156   |      40|      24.864|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 177   |     229|      19.822|   0.3%/236|   0.2%/284|   0.2%/299|   0.2%/316 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 181   |    2319|     253.220|   0.6%/110|   0.6%/122|   0.6%/125|   0.5%/128 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 181   |     659|      67.434|   1.0%/ 69|   1.2%/ 58|   1.2%/ 56|   1.3%/ 54 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 181   |   97962|      71.966|   1.3%/ 53|   1.2%/ 56|   1.2%/ 57|   1.2%/ 58 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 181   |   10576|      39.624|   1.2%/ 57|   1.2%/ 58|   1.2%/ 58|   1.2%/ 58 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 181   |   25583|     306.828|   0.7%/ 99|   0.7%/ 95|   0.7%/ 93|   0.7%/ 92 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 181   |    9171|     234.391|   0.8%/ 86|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 181   |    1799|     365.558|   0.1%/922|   0.1%/791|   0.1%/764|   0.1%/739 |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 181   |    1437|     156.434|   1.9%/ 36|   2.0%/ 34|   2.1%/ 33|   2.1%/ 33 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 181   |   35815|     594.558|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 181   |      94|      34.379|   5.3%/ 13|   5.4%/ 13|   5.4%/ 13|   5.4%/ 13 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 181   |    1591|      12.633|   0.5%/142|   0.4%/179|   0.4%/191|   0.3%/205 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 181   |      40|       3.776|   5.4%/ 13|   6.0%/ 11|   6.1%/ 11|   6.3%/ 11 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 181   |    1727|      92.429|   0.2%/340|   0.1%/553|   0.1%/654|   0.1%/800 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 181   |     690|      14.498|   0.8%/ 90|   0.8%/ 85|   0.8%/ 84|   0.8%/ 83 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 181   |     490|     272.634|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 178   |     604|     136.600|   0.5%/145|   0.5%/142|   0.5%/141|   0.5%/141 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 179   |    1064|     162.800|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 179   |      36|      19.071|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 181   |     368|      53.903|   2.6%/ 27|   2.4%/ 28|   2.4%/ 29|   2.3%/ 29 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 178   |      82|      18.323|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 180   |     546|      79.528|   2.5%/ 27|   2.4%/ 29|   2.4%/ 29|   2.3%/ 29 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 181   |      89|      31.693|   0.3%/213|   0.4%/175|   0.4%/167|   0.4%/159 |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 135   |     232|       8.850|   0.5%/127|   0.5%/146|   0.5%/153|   0.4%/159 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 181   |     133|       4.047|   0.1%/585|   0.1%/480|   0.2%/459|   0.2%/439 |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 181   |     130|       6.418|   0.1%/603|   0.1%/580|   0.1%/574|   0.1%/568 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 181   |     162|      39.628|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 181   |   77375|     611.285|   0.5%/128|   0.5%/139|   0.5%/142|   0.5%/145 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 181   |    1297|     483.561|   0.9%/ 73|   1.0%/ 71|   1.0%/ 71|   1.0%/ 71 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 181   |    2169|      60.476|   1.9%/ 37|   1.7%/ 41|   1.7%/ 42|   1.6%/ 43 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 127   |      58|       1.934|   3.8%/ 18|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  81   |     123|      49.916|   1.2%/ 57|   0.9%/ 81|   0.8%/ 91|   0.7%/104 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 136   |     496|      16.538|   2.2%/ 31|   1.9%/ 36|   1.9%/ 37|   1.8%/ 39 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 181   |    6355|     364.057|   0.1%/749|   0.1%/660|   0.1%/640|   0.1%/621 |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 181   |      22|       4.418|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 181   |     151|      23.320|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 181   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 181   |    1121|       5.439|   0.2%/363|   0.1%/478|   0.1%/521|   0.1%/572 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 181   |     732|     352.372|   0.7%/ 94|   0.7%/ 92|   0.8%/ 92|   0.8%/ 92 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 181   |     269|      50.094|   0.2%/419|   0.2%/342|   0.2%/327|   0.2%/312 |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 181   |     917|     196.683|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65|   1.1%/ 65 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 181   |    6472|      29.506|   0.1%/782|   0.1%/812|   0.1%/819|   0.1%/825 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 181   |    2358|     559.011|   0.5%/131|   0.5%/138|   0.5%/140|   0.5%/142 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  64   |       7|       0.806|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 181   |     861|     120.407|   2.8%/ 24|   2.5%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 181   |   32401|    1008.386|   0.3%/198|   0.3%/219|   0.3%/225|   0.3%/231 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 181   |    5559|      51.232|   1.2%/ 56|   1.1%/ 61|   1.1%/ 63|   1.1%/ 64 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 181   |    2417|      62.979|   0.7%/ 95|   0.8%/ 89|   0.8%/ 87|   0.8%/ 86 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 181   |    1947|     189.492|   0.3%/225|   0.3%/205|   0.3%/201|   0.4%/196 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 181   |     215|      78.191|   0.3%/262|   0.3%/273|   0.3%/276|   0.2%/279 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 181   |    4793|     247.005|   0.9%/ 78|   0.8%/ 83|   0.8%/ 84|   0.8%/ 86 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 181   |   20318|     138.458|   0.6%/110|   0.6%/109|   0.6%/109|   0.6%/108 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 122   |      30|       2.422|   1.3%/ 54|   1.2%/ 60|   1.1%/ 62|   1.1%/ 64 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 181   |    4733|     138.314|   0.6%/108|   0.6%/113|   0.6%/114|   0.6%/115 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 181   |     309|      19.078|   0.2%/280|   0.2%/327|   0.2%/339|   0.2%/353 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 181   |     751|     107.842|   0.1%/539|   0.1%/659|   0.1%/697|   0.1%/739 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 159   |      72|       9.153|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 181   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 181   |      42|       7.638|   0.9%/ 76|   1.1%/ 65|   1.1%/ 62|   1.2%/ 60 |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 181   |     145|      69.419|   0.4%/180|   0.5%/151|   0.5%/144|   0.5%/138 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 174   |      99|       6.214|   0.1%/808|   0.1%/748|   0.1%/729|   0.1%/709 |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 181   |   16720|     284.481|   0.4%/167|   0.3%/209|   0.3%/222|   0.3%/237 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 181   |   31282|     664.156|   0.2%/357|   0.2%/345|   0.2%/342|   0.2%/339 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 181   |      13|       0.606|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 181   |     840|      19.782|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 181   |    5884|     569.098|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 181   |    2065|     240.025|   0.1%/670|   0.1%/613|   0.1%/600|   0.1%/588 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 181   |     202|      11.539|   1.5%/ 45|   1.3%/ 54|   1.2%/ 57|   1.2%/ 59 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 181   |      21|       0.376|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 181   |      59|       0.889|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 181   |      47|       6.269|   1.6%/ 43|   1.7%/ 41|   1.7%/ 41|   1.7%/ 40 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 181   |      87|      63.883|   2.5%/ 27|   1.6%/ 44|   1.3%/ 52|   1.1%/ 64 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 181   |     206|      17.567|   3.1%/ 22|   3.4%/ 21|   3.4%/ 20|   3.5%/ 20 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 181   |    8028|      96.537|   0.9%/ 76|   0.9%/ 73|   1.0%/ 72|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 181   |  206087|     625.370|   0.4%/187|   0.4%/195|   0.4%/197|   0.3%/200 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  67   |      75|       1.857|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 181   |    4109|      98.103|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43|   1.6%/ 43 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 181   |     413|      41.780|   0.2%/281|   0.2%/292|   0.2%/295|   0.2%/297 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 181   |   42028|     632.608|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/977 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 181   |      47|      13.392|   0.2%/309|   0.2%/335|   0.2%/340|   0.2%/346 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 181   |     477|      13.967|   1.1%/ 62|   1.0%/ 72|   0.9%/ 75|   0.9%/ 78 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 181   |     624|      19.377|   1.6%/ 43|   1.5%/ 45|   1.5%/ 46|   1.5%/ 46 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  60   |      35|       0.364|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 180   |     341|      19.082|   0.2%/319|   0.2%/441|   0.1%/491|   0.1%/554 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 181   |     237|      15.607|   0.1%/736|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

