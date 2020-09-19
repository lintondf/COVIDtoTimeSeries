# State and Country COVID-19 Analysis #
## Updated: at 2020-09-19 for data as of 2020-09-18 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 38.4% of deaths and 38.8% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 66.2% of deaths and 56.4% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 171   |   33071|    1699.986|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 171   |   16053|    1807.309|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 171   |   15176|     523.401|   0.8%/ 88|   0.7%/105|   0.6%/110|   0.6%/116 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 171   |   15007|     379.802|   0.7%/ 99|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 171   |   13245|     616.670|   0.9%/ 81|   0.8%/ 87|   0.8%/ 89|   0.8%/ 91 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 171   |    9273|    1334.399|   0.1%/517|   0.1%/537|   0.1%/542|   0.1%/546 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 171   |    8641|     681.931|   0.3%/269|   0.3%/266|   0.3%/265|   0.3%/264 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 171   |    7915|     618.248|   0.2%/415|   0.2%/429|   0.2%/433|   0.2%/437 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 171   |    6968|     697.705|   0.1%/476|   0.1%/493|   0.1%/498|   0.1%/503 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 171   |    6659|     627.150|   0.7%/ 93|   0.6%/111|   0.6%/117|   0.6%/124 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 171   |  198792|     603.233|   0.4%/166|   0.4%/174|   0.4%/176|   0.4%/178 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 171   |  136313|     644.775|   0.6%/117|   0.5%/126|   0.5%/128|   0.5%/131 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 171   |   85453|      62.777|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 171   |   73497|     580.644|   0.6%/111|   0.6%/122|   0.6%/126|   0.5%/129 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 171   |   41783|     628.923|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 171   |   35657|     591.927|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 171   |   31027|     462.564|   0.1%/692|   0.1%/605|   0.1%/586|   0.1%/568 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 171   |   31421|     977.900|   0.4%/164|   0.4%/187|   0.4%/193|   0.3%/200 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 171   |   30035|     637.689|   0.2%/356|   0.2%/325|   0.2%/318|   0.2%/312 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 171   |   23877|     286.368|   0.6%/122|   0.6%/123|   0.6%/123|   0.6%/123 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 171   |    2446|     498.873|   0.6%/115|   0.5%/128|   0.5%/132|   0.5%/136 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 171   |      47|      64.305|   0.7%/100|   0.6%/124|   0.5%/132|   0.5%/141 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 171   |    5483|     753.317|   0.4%/180|   0.3%/226|   0.3%/241|   0.3%/258 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 171   |    1118|     370.362|   1.4%/ 50|   1.2%/ 56|   1.2%/ 58|   1.1%/ 60 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 171   |   15007|     379.802|   0.7%/ 99|   0.6%/108|   0.6%/111|   0.6%/114 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 171   |    2009|     348.803|   0.2%/388|   0.2%/390|   0.2%/390|   0.2%/390 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 171   |    4487|    1258.387|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 171   |     619|     635.358|   0.1%/482|   0.2%/451|   0.2%/443|   0.2%/435 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 171   |   13245|     616.670|   0.9%/ 81|   0.8%/ 87|   0.8%/ 89|   0.8%/ 91 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 171   |    6659|     627.150|   0.7%/ 93|   0.6%/111|   0.6%/117|   0.6%/124 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 171   |     119|      84.101|   2.5%/ 28|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 171   |     449|     251.049|   1.0%/ 71|   0.8%/ 87|   0.8%/ 91|   0.7%/ 97 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 171   |    8641|     681.931|   0.3%/269|   0.3%/266|   0.3%/265|   0.3%/264 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 171   |    3493|     518.898|   0.3%/227|   0.3%/232|   0.3%/233|   0.3%/234 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 171   |    1272|     403.063|   0.7%/105|   0.6%/112|   0.6%/114|   0.6%/116 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 171   |     546|     187.291|   1.6%/ 42|   1.9%/ 37|   1.9%/ 36|   2.0%/ 35 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 171   |    1106|     247.493|   0.9%/ 81|   0.8%/ 83|   0.8%/ 84|   0.8%/ 85 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 171   |    5365|    1153.981|   0.4%/173|   0.4%/196|   0.3%/202|   0.3%/209 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 171   |     138|     102.305|   0.3%/263|   0.3%/250|   0.3%/246|   0.3%/242 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 171   |    3876|     641.050|   0.2%/431|   0.1%/465|   0.1%/475|   0.1%/485 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 171   |    9273|    1334.399|   0.1%/517|   0.1%/537|   0.1%/542|   0.1%/546 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 171   |    6968|     697.705|   0.1%/476|   0.1%/493|   0.1%/498|   0.1%/503 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 171   |    2001|     354.739|   0.4%/186|   0.4%/190|   0.4%/190|   0.4%/191 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 171   |    2824|     948.905|   0.7%/103|   0.6%/117|   0.6%/121|   0.6%/125 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 171   |    1812|     295.231|   0.7%/ 96|   0.7%/ 98|   0.7%/ 99|   0.7%/100 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 171   |     146|     136.511|   1.8%/ 38|   1.8%/ 38|   1.8%/ 37|   1.8%/ 37 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 171   |     444|     229.756|   0.5%/128|   0.5%/130|   0.5%/131|   0.5%/131 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 171   |    1534|     498.121|   0.8%/ 89|   0.7%/102|   0.7%/106|   0.6%/110 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 171   |     438|     321.903|   0.1%/778|   0.1%/779|   0.1%/775|   0.1%/770 |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 171   |   16053|    1807.309|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 171   |     845|     402.814|   0.4%/173|   0.4%/192|   0.4%/198|   0.3%/203 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 171   |   33071|    1699.986|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 171   |    3208|     305.904|   0.9%/ 76|   0.9%/ 77|   0.9%/ 77|   0.9%/ 77 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 171   |     178|     233.777|   1.4%/ 49|   1.5%/ 45|   1.6%/ 44|   1.6%/ 43 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 171   |    4563|     390.361|   0.6%/112|   0.6%/107|   0.7%/106|   0.7%/104 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 171   |     949|     239.790|   0.8%/ 82|   0.8%/ 92|   0.7%/ 94|   0.7%/ 97 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 171   |     531|     125.995|   0.7%/ 94|   0.7%/105|   0.6%/109|   0.6%/112 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 171   |    7915|     618.248|   0.2%/415|   0.2%/429|   0.2%/433|   0.2%/437 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 171   |     585|     183.052|   1.8%/ 39|   1.8%/ 38|   1.8%/ 37|   1.9%/ 37 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 171   |    1083|    1022.205|   0.2%/317|   0.2%/294|   0.2%/289|   0.2%/283 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 171   |    3215|     624.339|   0.8%/ 85|   0.7%/ 94|   0.7%/ 97|   0.7%/100 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 171   |     189|     214.031|   1.0%/ 72|   1.1%/ 64|   1.1%/ 62|   1.1%/ 60 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 171   |    2208|     323.129|   1.2%/ 57|   1.2%/ 60|   1.1%/ 61|   1.1%/ 61 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 171   |   15176|     523.401|   0.8%/ 88|   0.7%/105|   0.6%/110|   0.6%/116 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 171   |  198792|     603.233|   0.4%/166|   0.4%/174|   0.4%/176|   0.4%/178 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 171   |     445|     138.780|   0.3%/209|   0.2%/293|   0.2%/326|   0.2%/367 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 171   |      58|      92.950|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 171   |    2867|     335.914|   0.5%/134|   0.5%/135|   0.5%/135|   0.5%/136 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 171   |    2038|     267.687|   0.3%/217|   0.3%/238|   0.3%/244|   0.3%/249 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 171   |     304|     169.680|   1.8%/ 38|   1.8%/ 39|   1.8%/ 39|   1.7%/ 40 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 171   |    1240|     213.051|   0.5%/136|   0.5%/140|   0.5%/141|   0.5%/142 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 159   |      47|      80.479|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 171   |    1435|      44.515|   0.1%/515|   0.1%/515|   0.1%/513|   0.1%/510 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 171   |     360|     126.417|   1.1%/ 63|   1.0%/ 71|   0.9%/ 74|   0.9%/ 77 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 171   |    1662|      38.653|   0.5%/129|   0.5%/133|   0.5%/134|   0.5%/135 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 171   |     145|       4.665|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40|   1.7%/ 39 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 171   |   12923|     287.562|   2.0%/ 34|   1.9%/ 37|   1.8%/ 37|   1.8%/ 38 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 171   |     932|     315.078|   0.3%/243|   0.3%/277|   0.2%/286|   0.2%/297 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 171   |    1018|      39.621|   1.0%/ 68|   0.6%/120|   0.5%/148|   0.4%/192 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 171   |     759|      85.227|   0.1%/464|   0.2%/398|   0.2%/383|   0.2%/370 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 171   |     573|      56.943|   0.4%/176|   0.4%/176|   0.4%/176|   0.4%/176 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 171   |     218|     141.190|   0.8%/ 89|   0.8%/ 85|   0.8%/ 85|   0.8%/ 84 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 171   |    4940|      29.323|   0.7%/ 95|   0.7%/105|   0.6%/108|   0.6%/111 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 171   |     777|      82.559|   0.7%/ 95|   0.7%/ 95|   0.7%/ 95|   0.7%/ 95 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 171   |    9936|     862.178|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 166   |      40|       3.427|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 171   |    7790|     679.149|   0.8%/ 88|   0.6%/112|   0.6%/120|   0.5%/130 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 171   |     755|     228.766|   1.2%/ 59|   1.1%/ 63|   1.1%/ 64|   1.1%/ 65 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 171   |      14|       6.051|   5.5%/ 12|   5.3%/ 13|   5.3%/ 13|   5.2%/ 13 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 171   |  136313|     644.775|   0.6%/117|   0.5%/126|   0.5%/128|   0.5%/131 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 171   |     772|     111.017|   1.0%/ 70|   0.9%/ 81|   0.8%/ 84|   0.8%/ 87 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 171   |      56|       2.690|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 159   |       1|       0.091|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 171   |     417|      15.715|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 171   |    9254|     243.525|   0.1%/ ***|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)| 119   |      62|      11.304|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 144   |      81|       4.992|   0.1%/590|   0.1%/463|   0.2%/438|   0.2%/415 |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 171   |   12221|     639.615|   0.4%/164|   0.4%/172|   0.4%/174|   0.4%/176 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 171   |    4740|       3.380|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 171   |   24550|     497.013|   1.0%/ 70|   0.8%/ 85|   0.8%/ 90|   0.7%/ 96 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 171   |     680|     134.468|   2.5%/ 27|   2.6%/ 27|   2.6%/ 27|   2.6%/ 27 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 171   |     235|      57.585|   1.6%/ 43|   1.8%/ 39|   1.8%/ 38|   1.9%/ 37 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 171   |     111|       9.913|   0.7%/ 96|   0.8%/ 91|   0.8%/ 90|   0.8%/ 89 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 171   |     633|     108.778|   0.1%/720|   0.1%/633|   0.1%/614|   0.1%/596 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 171   |    2078|     200.659|   0.9%/ 78|   0.8%/ 86|   0.8%/ 88|   0.8%/ 91 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 171   |    7158|     409.794|   0.4%/174|   0.4%/188|   0.4%/192|   0.4%/196 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 171   |    5740|      57.244|   0.3%/221|   0.3%/226|   0.3%/227|   0.3%/229 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 171   |     820|     126.398|   0.6%/122|   0.4%/155|   0.4%/166|   0.4%/179 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 150   |      83|      61.107|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 167   |    1119|      11.341|   1.4%/ 49|   1.1%/ 62|   1.0%/ 66|   1.0%/ 71 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 171   |     338|      61.224|   0.1%/ ***|   0.1%/933|   0.1%/905|   0.1%/878 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 171   |   31027|     462.564|   0.1%/692|   0.1%/605|   0.1%/586|   0.1%/568 |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 171   |      53|      24.427|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 171   |     106|      45.320|   1.0%/ 69|   1.3%/ 54|   1.3%/ 54|   0.9%/ 73 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 168   |      19|       5.201|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 171   |    9380|     112.805|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 171   |     298|       9.829|   0.3%/210|   0.2%/304|   0.2%/339|   0.2%/381 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 171   |     325|      30.271|   1.2%/ 59|   1.2%/ 57|   1.2%/ 57|   1.2%/ 56 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 171   |    3074|     185.129|   0.6%/125|   0.5%/144|   0.5%/149|   0.4%/154 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 157   |      65|       5.316|   0.3%/266|   0.1%/994|   0.0%/ ***|   0.0%/ -- |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 146   |      40|      25.105|   0.3%/257|   0.2%/304|   0.2%/322|   0.2%/343 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 167   |     223|      19.287|   0.4%/166|   0.4%/173|   0.4%/176|   0.4%/179 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 171   |    2194|     239.611|   0.7%/100|   0.6%/124|   0.5%/132|   0.5%/142 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 171   |     639|      65.380|   0.3%/206|   0.4%/174|   0.4%/167|   0.4%/160 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 171   |   85453|      62.777|   1.4%/ 49|   1.3%/ 52|   1.3%/ 53|   1.3%/ 53 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 171   |    9339|      34.988|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 171   |   23877|     286.368|   0.6%/122|   0.6%/123|   0.6%/123|   0.6%/123 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 171   |    8469|     216.440|   1.0%/ 72|   0.9%/ 76|   0.9%/ 77|   0.9%/ 78 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 171   |    1786|     362.876|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 171   |    1207|     131.318|   1.3%/ 52|   1.3%/ 54|   1.3%/ 55|   1.3%/ 55 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 171   |   35657|     591.927|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 171   |      53|      19.381|   1.7%/ 40|   3.1%/ 22|   5.0%/ 14|   6.1%/ 11 |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 171   |    1518|      12.049|   0.8%/ 86|   0.7%/ 93|   0.7%/ 95|   0.7%/ 97 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 171   |      27|       2.514|   3.7%/ 19|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 171   |    1705|      91.235|   0.4%/169|   0.3%/221|   0.3%/240|   0.3%/261 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 171   |     648|      13.626|   0.6%/123|   0.5%/149|   0.4%/157|   0.4%/164 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 171   |     503|     279.994|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 168   |     574|     129.909|   0.5%/141|   0.5%/133|   0.5%/131|   0.5%/129 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 169   |    1033|     158.055|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 169   |      36|      18.759|   0.3%/275|   0.2%/288|   0.2%/292|   0.2%/295 |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 171   |     280|      40.972|   2.9%/ 24|   2.8%/ 24|   2.8%/ 25|   2.8%/ 25 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 168   |      82|      18.323|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 170   |     420|      61.118|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23|   3.0%/ 23 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 171   |      87|      31.286|   0.1%/881|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)| 125   |     219|       8.340|   0.7%/106|   0.6%/123|   0.5%/129|   0.5%/135 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 171   |     129|       3.935|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 171   |     128|       6.338|   0.1%/819|   0.1%/813|   0.1%/815|   0.1%/819 |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 171   |     162|      39.627|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.0%/ *** |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 171   |   73497|     580.644|   0.6%/111|   0.6%/122|   0.6%/126|   0.5%/129 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 171   |    1178|     439.395|   0.9%/ 76|   0.9%/ 74|   0.9%/ 74|   0.9%/ 73 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 171   |    1851|      51.593|   2.3%/ 31|   2.0%/ 35|   1.9%/ 37|   1.8%/ 38 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)| 117   |      40|       1.330|   3.3%/ 21|   3.6%/ 19|   3.7%/ 19|   3.8%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  71   |     110|      44.823|   1.8%/ 38|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)| 126   |     409|      13.642|   2.9%/ 24|   2.3%/ 31|   2.1%/ 33|   2.0%/ 35 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 171   |    6313|     361.647|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 171   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 171   |     148|      22.879|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 171   |      69|       3.092|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 171   |    1101|       5.343|   0.3%/203|   0.3%/208|   0.3%/210|   0.3%/212 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 171   |     674|     324.529|   0.8%/ 92|   0.8%/ 88|   0.8%/ 86|   0.8%/ 85 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 171   |     266|      49.474|   0.0%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 171   |     823|     176.440|   1.1%/ 65|   1.0%/ 66|   1.0%/ 66|   1.0%/ 67 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 171   |    6423|      29.282|   0.1%/759|   0.1%/859|   0.1%/888|   0.1%/918 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 171   |    2240|     531.056|   0.6%/125|   0.5%/139|   0.5%/143|   0.5%/147 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  54   |       6|       0.698|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 171   |     671|      93.835|   3.2%/ 21|   2.6%/ 26|   2.4%/ 28|   2.3%/ 30 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 171   |   31421|     977.900|   0.4%/164|   0.4%/187|   0.4%/193|   0.3%/200 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 171   |    4826|      44.473|   1.7%/ 41|   1.7%/ 42|   1.6%/ 42|   1.6%/ 42 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 171   |    2261|      58.912|   0.6%/122|   0.6%/121|   0.6%/121|   0.6%/121 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 171   |    1883|     183.277|   0.2%/317|   0.2%/295|   0.2%/290|   0.2%/284 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 171   |     209|      76.219|   0.3%/238|   0.3%/236|   0.3%/236|   0.3%/236 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 171   |    4417|     227.598|   1.0%/ 70|   0.9%/ 75|   0.9%/ 77|   0.9%/ 78 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 171   |   19086|     130.063|   0.6%/115|   0.6%/115|   0.6%/114|   0.6%/114 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)| 112   |      24|       1.965|   1.6%/ 42|   1.5%/ 47|   1.4%/ 48|   1.4%/ 49 |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 171   |    4448|     129.995|   0.7%/100|   0.7%/106|   0.6%/107|   0.6%/109 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 171   |     304|      18.769|   0.3%/231|   0.2%/338|   0.2%/381|   0.2%/435 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 171   |     742|     106.598|   0.2%/414|   0.1%/558|   0.1%/609|   0.1%/669 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 149   |      73|       9.182|   0.1%/643|   0.1%/976|   0.1%/ ***|   0.1%/ *** |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 171   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 171   |      39|       7.182|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 171   |     137|      65.220|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 164   |      99|       6.213|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 171   |   16169|     275.105|   0.6%/124|   0.4%/165|   0.4%/179|   0.4%/196 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 171   |   30035|     637.689|   0.2%/356|   0.2%/325|   0.2%/318|   0.2%/312 |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 171   |      13|       0.584|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 171   |     840|      19.792|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 171   |    5860|     566.821|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 171   |    2028|     235.731|   0.1%/ ***|   0.1%/930|   0.1%/911|   0.1%/893 |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 171   |     178|      10.155|   2.1%/ 33|   1.8%/ 38|   1.8%/ 39|   1.7%/ 41 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 171   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 171   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 171   |      41|       5.409|   2.0%/ 34|   2.4%/ 29|   2.5%/ 28|   2.6%/ 27 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 171   |      68|      50.119|   5.6%/ 12|   5.3%/ 13|   5.3%/ 13|   5.2%/ 13 |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 171   |     119|      10.188|   3.1%/ 22|   3.5%/ 20|   3.6%/ 19|   3.7%/ 19 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 171   |    7285|      87.608|   0.8%/ 83|   0.9%/ 75|   0.9%/ 74|   1.0%/ 72 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 171   |  198792|     603.233|   0.4%/166|   0.4%/174|   0.4%/176|   0.4%/178 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  57   |      63|       1.556|   3.8%/ 18|   2.9%/ 23|   2.7%/ 25|   2.5%/ 28 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 171   |    3508|      83.756|   1.7%/ 41|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 171   |     405|      40.915|   0.3%/259|   0.2%/278|   0.2%/284|   0.2%/290 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 171   |   41783|     628.923|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 171   |      46|      13.139|   0.2%/400|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 171   |     425|      12.441|   1.5%/ 45|   1.4%/ 49|   1.4%/ 50|   1.3%/ 51 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 171   |     532|      16.524|   1.8%/ 39|   1.7%/ 41|   1.7%/ 41|   1.7%/ 42 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  50   |      35|       0.364|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 170   |     323|      18.079|   0.7%/ 93|   0.8%/ 86|   0.8%/ 84|   0.8%/ 83 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 171   |     242|      15.985|   0.3%/223|   0.0%/ --|   0.0%/ --|   0.0%/ -- |

