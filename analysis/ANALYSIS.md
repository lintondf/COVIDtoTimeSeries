# State and Country COVID-19 Analysis #
## Updated: at 2020-08-16 for data as of 2020-08-14 ##

Uses the total death counts from the daily report files from the JHU CSSE COVID-19 GITHUB repository: https://github.com/CSSEGISandData/COVID-19.git.

# US Confirmed Case Rates vs. Death Rates #

The next several plots show _per capita_ data for the four US states with the largest populations: California, Florida, Texas, and New York.  These four states comprise 33.2% of the US population and account for 37.6% of deaths and 40.3% of confirmed cases.  Per capita data is expressed per million of population.  One per million is 0.0001%.  1% is 10,000 per million.  

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

Deaths in the 10 US States with the highest death tolls expressed as deaths per 1 million population. These ten states comprise 52.0% of the US population and account for 67.9% of deaths and 58.6% of confirmed cases.

![US States with Highest Death Toll - Death Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeaths.png)

![US States with Highest Death Toll - Death Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestDeathsPerDay.png)

![US States with Highest Death Toll - Cases Toll](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20Cases.png)

![US States with Highest Death Toll - Cases Rates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/10LargestConfirmed%20CasesPerDay.png)

Daily Death Rate of Growth (DDRG) in the 10 US States with the highest death tolls.

![US States with Highest Death Toll - Daily Death Rate of Growths](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/States10WorstDDGR.png)

|State|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 136   |   32834|    1687.813|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15909|    1791.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |   11114|     281.279|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 136   |   10613|     366.001|   2.2%/ 32|   1.8%/ 39|   1.6%/ 42|   1.5%/ 45 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    9273|     431.762|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 136   |    8808|    1267.391|   0.2%/402|   0.2%/399|   0.2%/399|   0.2%/398 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 136   |    7926|     625.458|   0.2%/315|   0.2%/312|   0.2%/311|   0.2%/311 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 136   |    7401|     578.117|   0.2%/304|   0.2%/282|   0.3%/276|   0.3%/270 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 136   |    6563|     657.207|   0.1%/515|   0.1%/478|   0.1%/470|   0.1%/462 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 136   |    4541|     427.698|   1.6%/ 43|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |


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
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  168753|     512.081|   0.7%/ 97|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 136   |  106992|     506.084|   1.1%/ 65|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 136   |   56178|     443.824|   1.4%/ 51|   1.3%/ 51|   1.3%/ 51|   1.3%/ 51 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   49530|      36.386|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   46894|     705.856|   0.1%/656|   0.1%/739|   0.1%/765|   0.1%/792 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   35255|     585.261|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   30384|     452.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28580|     606.793|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 136   |   23317|     725.677|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   19597|     235.037|   1.0%/ 66|   0.9%/ 74|   0.9%/ 77|   0.9%/ 79 |


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
|[Alabama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alabama.png)| 136   |    1920|     391.504|   1.4%/ 50|   1.3%/ 52|   1.3%/ 52|   1.3%/ 53 |
|[Alaska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Alaska.png)| 136   |      28|      38.663|   1.3%/ 53|   1.4%/ 50|   1.4%/ 49|   1.4%/ 49 |
|[Arizona](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arizona.png)| 136   |    4537|     623.309|   1.5%/ 45|   1.3%/ 54|   1.2%/ 56|   1.2%/ 58 |
|[Arkansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Arkansas.png)| 136   |     599|     198.576|   2.0%/ 35|   2.0%/ 34|   2.0%/ 34|   2.0%/ 34 |
|[California](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/California.png)| 136   |   11114|     281.279|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Colorado](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Colorado.png)| 136   |    1891|     328.324|   0.2%/285|   0.2%/313|   0.2%/320|   0.2%/328 |
|[Connecticut](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Connecticut.png)| 136   |    4453|    1249.059|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Delaware](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Delaware.png)| 136   |     601|     617.380|   0.1%/564|   0.1%/628|   0.1%/646|   0.1%/665 |
|[Florida](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Florida.png)| 136   |    9273|     431.762|   2.3%/ 30|   2.2%/ 31|   2.2%/ 31|   2.2%/ 31 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Georgia.png)| 136   |    4541|     427.698|   1.6%/ 43|   1.7%/ 40|   1.8%/ 39|   1.8%/ 39 |
|[Hawaii](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Hawaii.png)| 136   |      31|      21.711|   2.9%/ 23|   3.8%/ 18|   4.1%/ 17|   4.3%/ 16 |
|[Idaho](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Idaho.png)| 136   |     276|     154.439|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Illinois](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Illinois.png)| 136   |    7926|     625.458|   0.2%/315|   0.2%/312|   0.2%/311|   0.2%/311 |
|[Indiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Indiana.png)| 136   |    3106|     461.409|   0.4%/176|   0.4%/168|   0.4%/166|   0.4%/163 |
|[Iowa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Iowa.png)| 136   |     968|     306.738|   0.8%/ 85|   0.9%/ 81|   0.9%/ 81|   0.9%/ 80 |
|[Kansas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kansas.png)| 136   |     406|     139.352|   1.0%/ 69|   1.0%/ 68|   1.0%/ 68|   1.0%/ 68 |
|[Kentucky](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Kentucky.png)| 136   |     803|     179.816|   0.7%/ 99|   0.7%/102|   0.7%/102|   0.7%/102 |
|[Louisiana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Louisiana.png)| 136   |    4436|     954.271|   0.9%/ 81|   0.9%/ 80|   0.9%/ 80|   0.9%/ 80 |
|[Maine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maine.png)| 136   |     127|      94.564|   0.3%/252|   0.2%/292|   0.2%/305|   0.2%/318 |
|[Maryland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Maryland.png)| 136   |    3634|     601.102|   0.3%/246|   0.3%/247|   0.3%/247|   0.3%/248 |
|[Massachusetts](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Massachusetts.png)| 136   |    8808|    1267.391|   0.2%/402|   0.2%/399|   0.2%/399|   0.2%/398 |
|[Michigan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Michigan.png)| 136   |    6563|     657.207|   0.1%/515|   0.1%/478|   0.1%/470|   0.1%/462 |
|[Minnesota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Minnesota.png)| 136   |    1724|     305.709|   0.4%/188|   0.4%/180|   0.4%/179|   0.4%/177 |
|[Mississippi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Mississippi.png)| 136   |    2062|     692.778|   1.6%/ 42|   1.7%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Missouri](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Missouri.png)| 136   |    1379|     224.705|   0.6%/111|   0.6%/123|   0.5%/126|   0.5%/130 |
|[Montana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Montana.png)| 136   |      86|      80.032|   2.6%/ 26|   2.4%/ 29|   2.3%/ 30|   2.3%/ 30 |
|[Nebraska](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nebraska.png)| 136   |     359|     185.468|   0.7%/ 97|   0.8%/ 91|   0.8%/ 90|   0.8%/ 88 |
|[Nevada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Nevada.png)| 136   |    1045|     339.143|   1.9%/ 36|   2.0%/ 35|   2.0%/ 35|   2.0%/ 35 |
|[New Hampshire](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Hampshire.png)| 136   |     424|     311.761|   0.1%/481|   0.1%/760|   0.1%/887|   0.1%/ *** |
|[New Jersey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Jersey.png)| 136   |   15909|    1791.137|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20Mexico.png)| 136   |     711|     339.183|   0.7%/100|   0.6%/111|   0.6%/114|   0.6%/118 |
|[New York](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/New%20York.png)| 136   |   32834|    1687.813|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[North Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Carolina.png)| 136   |    2340|     223.136|   1.3%/ 53|   1.3%/ 54|   1.3%/ 54|   1.3%/ 54 |
|[North Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/North%20Dakota.png)| 136   |     119|     156.802|   1.2%/ 58|   1.3%/ 53|   1.3%/ 51|   1.4%/ 50 |
|[Ohio](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Ohio.png)| 136   |    3809|     325.828|   0.7%/105|   0.6%/111|   0.6%/113|   0.6%/115 |
|[Oklahoma](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oklahoma.png)| 136   |     651|     164.463|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50|   1.4%/ 50 |
|[Oregon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Oregon.png)| 136   |     386|      91.606|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47|   1.5%/ 47 |
|[Pennsylvania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Pennsylvania.png)| 136   |    7401|     578.117|   0.2%/304|   0.2%/282|   0.3%/276|   0.3%/270 |
|[Puerto Rico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Puerto%20Rico.png)| 136   |     307|      96.195|   2.5%/ 28|   2.7%/ 25|   2.8%/ 25|   2.9%/ 24 |
|[Rhode Island](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Rhode%20Island.png)| 136   |    1020|     962.867|   0.1%/758|   0.1%/804|   0.1%/813|   0.1%/821 |
|[South Carolina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Carolina.png)| 136   |    2294|     445.570|   2.0%/ 34|   1.8%/ 39|   1.7%/ 41|   1.6%/ 43 |
|[South Dakota](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/South%20Dakota.png)| 136   |     152|     171.858|   1.0%/ 70|   1.0%/ 72|   0.9%/ 73|   0.9%/ 74 |
|[Tennessee](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Tennessee.png)| 136   |    1339|     196.012|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40|   1.7%/ 40 |
|[Texas](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Texas.png)| 136   |   10613|     366.001|   2.2%/ 32|   1.8%/ 39|   1.6%/ 42|   1.5%/ 45 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/US.png)| 136   |  168753|     512.081|   0.7%/ 97|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96 |
|[Utah](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Utah.png)| 136   |     366|     114.062|   1.3%/ 54|   1.1%/ 62|   1.1%/ 64|   1.0%/ 67 |
|[Vermont](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Vermont.png)| 136   |      58|      93.434|   0.0%/ --|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Virginia.png)| 136   |    2399|     281.103|   0.6%/111|   0.6%/113|   0.6%/114|   0.6%/116 |
|[Washington](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Washington.png)| 136   |    1755|     230.407|   0.8%/ 89|   0.8%/ 85|   0.8%/ 85|   0.8%/ 84 |
|[West Virginia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/West%20Virginia.png)| 136   |     151|      84.227|   2.5%/ 27|   3.0%/ 23|   3.1%/ 22|   3.3%/ 21 |
|[Wisconsin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wisconsin.png)| 136   |    1035|     177.736|   0.7%/ 95|   0.7%/ 99|   0.7%/100|   0.7%/101 |
|[Wyoming](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/states/Wyoming.png)| 124   |      29|      50.967|   1.0%/ 67|   1.2%/ 57|   1.3%/ 55|   1.3%/ 53 |


# All Countries #

Click on the link in the first column to view the deaths and DDRG chart for a specific country.
 
|Country|Days|Deaths|Deaths/1M|DDRG[6:7]|DDRG[2:3]|DDRG[1:2]|DDRG[0:1]|
|:--|--:|--:|--:|--:|--:|--:|--:|
|[Afghanistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Afghanistan.png)| 136   |    1361|      42.243|   0.5%/135|   0.5%/144|   0.5%/145|   0.5%/146 |
|[Albania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Albania.png)| 136   |     225|      78.969|   2.4%/ 29|   2.2%/ 31|   2.2%/ 32|   2.1%/ 33 |
|[Algeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Algeria.png)| 136   |    1360|      31.628|   0.8%/ 84|   0.8%/ 88|   0.8%/ 89|   0.8%/ 90 |
|[Angola](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Angola.png)| 136   |      89|       2.867|   2.9%/ 23|   2.6%/ 27|   2.5%/ 28|   2.4%/ 29 |
|[Argentina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Argentina.png)| 136   |    5530|     123.050|   3.5%/ 20|   3.5%/ 20|   3.5%/ 20|   3.5%/ 19 |
|[Armenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Armenia.png)| 136   |     825|     278.986|   0.7%/ 99|   0.6%/124|   0.5%/133|   0.5%/142 |
|[Australia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Australia.png)| 136   |     395|      15.384|   5.2%/ 13|   5.6%/ 12|   5.7%/ 12|   5.8%/ 12 |
|[Austria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Austria.png)| 136   |     725|      81.476|   0.1%/674|   0.1%/596|   0.1%/579|   0.1%/563 |
|[Azerbaijan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Azerbaijan.png)| 136   |     521|      51.707|   0.9%/ 81|   0.5%/131|   0.4%/155|   0.4%/190 |
|[Bahrain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bahrain.png)| 136   |     170|     110.354|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   0.9%/ 73 |
|[Bangladesh](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bangladesh.png)| 136   |    3612|      21.442|   1.1%/ 63|   1.0%/ 68|   1.0%/ 69|   1.0%/ 70 |
|[Belarus](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belarus.png)| 136   |     609|      64.678|   0.6%/123|   0.4%/154|   0.4%/165|   0.4%/177 |
|[Belgium](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Belgium.png)| 136   |    9902|     859.244|   0.1%/ ***|   0.1%/ ***|   0.1%/974|   0.1%/935 |
|[Benin](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Benin.png)| 131   |      39|       3.340|   0.1%/513|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Bolivia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bolivia.png)| 136   |    4094|     356.914|   2.1%/ 33|   1.9%/ 37|   1.8%/ 38|   1.8%/ 39 |
|[Bosnia and Herzegovina](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bosnia%20and%20Herzegovina.png)| 136   |     471|     142.710|   2.1%/ 32|   2.1%/ 32|   2.1%/ 32|   2.2%/ 32 |
|[Botswana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Botswana.png)| 136   |       3|       1.127|   3.5%/ 20|   2.2%/ 32|   1.9%/ 36|   1.7%/ 42 |
|[Brazil](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Brazil.png)| 136   |  106992|     506.084|   1.1%/ 65|   1.0%/ 68|   1.0%/ 68|   1.0%/ 69 |
|[Bulgaria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Bulgaria.png)| 136   |     498|      71.604|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37|   1.9%/ 37 |
|[Burkina Faso](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burkina%20Faso.png)| 136   |      54|       2.595|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ *** |
|[Burundi](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Burundi.png)| 124   |       1|       0.091|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Cameroon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cameroon.png)| 136   |     400|      15.073|   0.2%/319|   0.2%/334|   0.2%/334|   0.2%/332 |
|[Canada](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Canada.png)| 136   |    9066|     238.586|   0.1%/915|   0.1%/905|   0.1%/902|   0.1%/898 |
|[Central African Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Central%20African%20Republic.png)|  84   |      61|      11.086|   0.3%/246|   0.5%/148|   0.5%/134|   0.6%/122 |
|[Chad](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chad.png)| 109   |      76|       4.689|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Chile](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Chile.png)| 136   |   10452|     547.043|   0.7%/106|   0.6%/120|   0.6%/124|   0.5%/129 |
|[China](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/China.png)| 136   |    4695|       3.348|   0.1%/ ***|   0.1%/954|   0.1%/927|   0.1%/902 |
|[Colombia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Colombia.png)| 136   |   14925|     302.144|   2.8%/ 25|   2.6%/ 27|   2.5%/ 27|   2.5%/ 28 |
|[Costa Rica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Costa%20Rica.png)| 136   |     313|      61.820|   5.0%/ 14|   4.2%/ 16|   4.0%/ 17|   3.9%/ 18 |
|[Croatia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Croatia.png)| 136   |     166|      40.844|   0.9%/ 81|   0.7%/101|   0.6%/108|   0.6%/117 |
|[Cuba](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Cuba.png)| 136   |      88|       7.877|   0.1%/832|   0.1%/683|   0.1%/656|   0.1%/632 |
|[Denmark](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Denmark.png)| 136   |     621|     106.600|   0.1%/882|   0.1%/782|   0.1%/758|   0.1%/736 |
|[Dominican Republic](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Dominican%20Republic.png)| 136   |    1408|     135.926|   1.6%/ 44|   1.6%/ 42|   1.7%/ 42|   1.7%/ 41 |
|[Ecuador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ecuador.png)| 136   |    6074|     347.706|   0.4%/158|   0.4%/176|   0.4%/182|   0.4%/188 |
|[Egypt](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Egypt.png)| 136   |    5182|      51.680|   0.5%/138|   0.4%/183|   0.3%/199|   0.3%/217 |
|[El Salvador](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/El%20Salvador.png)| 136   |     609|      93.874|   2.1%/ 33|   1.9%/ 36|   1.9%/ 36|   1.9%/ 37 |
|[Equatorial Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Equatorial%20Guinea.png)| 115   |      92|      68.055|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Ethiopia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ethiopia.png)| 132   |     509|       5.159|   4.3%/ 16|   4.2%/ 16|   4.2%/ 16|   4.2%/ 16 |
|[Finland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Finland.png)| 136   |     333|      60.220|   0.1%/849|   0.1%/710|   0.1%/681|   0.1%/655 |
|[France](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/France.png)| 136   |   30384|     452.977|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Gabon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gabon.png)| 136   |      52|      23.870|   0.2%/399|   0.1%/ ***|   0.0%/ ***|   0.0%/ -- |
|[Gambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Gambia.png)| 136   |      54|      23.001|   5.9%/ 12|  12.8%/  5|  23.2%/  3|  19.1%/  3 |
|[Georgia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Georgia.png)| 133   |      17|       4.642|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Germany](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Germany.png)| 136   |    9226|     110.955|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Ghana](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ghana.png)| 136   |     230|       7.584|   1.8%/ 39|   1.8%/ 39|   1.8%/ 39|   1.8%/ 38 |
|[Greece](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Greece.png)| 136   |     217|      20.245|   0.4%/162|   0.5%/150|   0.5%/147|   0.5%/144 |
|[Guatemala](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guatemala.png)| 136   |    2393|     144.139|   1.5%/ 47|   1.2%/ 56|   1.2%/ 59|   1.1%/ 62 |
|[Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea.png)| 122   |      51|       4.215|   0.6%/122|   0.3%/230|   0.2%/300|   0.2%/433 |
|[Guinea-Bissau](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Guinea-Bissau.png)| 111   |      30|      18.565|   1.0%/ 70|   1.3%/ 53|   1.4%/ 50|   1.5%/ 47 |
|[Haiti](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Haiti.png)| 132   |     191|      16.479|   1.3%/ 54|   1.5%/ 48|   1.5%/ 46|   1.5%/ 45 |
|[Honduras](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Honduras.png)| 136   |    1650|     180.154|   1.4%/ 51|   0.8%/ 82|   0.7%/ 98|   0.6%/120 |
|[Hungary](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Hungary.png)| 136   |     605|      61.936|   0.1%/580|   0.2%/453|   0.2%/429|   0.2%/408 |
|[India](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/India.png)| 136   |   49530|      36.386|   2.2%/ 32|   2.1%/ 33|   2.1%/ 33|   2.1%/ 33 |
|[Indonesia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Indonesia.png)| 136   |    6114|      22.907|   1.2%/ 58|   1.1%/ 66|   1.0%/ 68|   1.0%/ 70 |
|[Iran](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iran.png)| 136   |   19597|     235.037|   1.0%/ 66|   0.9%/ 74|   0.9%/ 77|   0.9%/ 79 |
|[Iraq](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Iraq.png)| 136   |    5812|     148.541|   1.4%/ 50|   1.2%/ 55|   1.2%/ 57|   1.2%/ 59 |
|[Ireland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ireland.png)| 136   |    1774|     360.535|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Israel](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Israel.png)| 136   |     665|      72.375|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37|   1.9%/ 37 |
|[Italy](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Italy.png)| 136   |   35255|     585.261|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Jamaica](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jamaica.png)| 136   |      14|       5.254|   0.0%/ --|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Japan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Japan.png)| 136   |    1068|       8.483|   0.5%/140|   0.6%/115|   0.6%/110|   0.7%/105 |
|[Jordan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Jordan.png)| 136   |      11|       1.033|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Kazakhstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kazakhstan.png)| 136   |    1349|      72.201|   1.3%/ 51|   1.9%/ 36|   2.1%/ 34|   2.2%/ 31 |
|[Kenya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kenya.png)| 136   |     486|      10.219|   2.4%/ 28|   2.2%/ 31|   2.1%/ 32|   2.1%/ 33 |
|[Kosovo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kosovo.png)| 136   |     392|     218.228|   3.7%/ 19|   3.5%/ 20|   3.4%/ 20|   3.4%/ 20 |
|[Kuwait](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kuwait.png)| 133   |     497|     112.374|   0.7%/ 99|   0.7%/104|   0.7%/105|   0.7%/106 |
|[Kyrgyzstan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Kyrgyzstan.png)| 134   |    1514|     231.771|   0.6%/118|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Latvia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Latvia.png)| 134   |      32|      16.919|   0.1%/728|   0.1%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Lebanon](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lebanon.png)| 136   |      94|      13.743|   3.7%/ 19|   4.0%/ 17|   4.1%/ 17|   4.1%/ 17 |
|[Liberia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Liberia.png)| 133   |      83|      18.462|   0.7%/ 94|   0.8%/ 90|   0.8%/ 89|   0.8%/ 89 |
|[Libya](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Libya.png)| 135   |     147|      21.394|   3.5%/ 20|   3.6%/ 19|   3.6%/ 19|   3.6%/ 19 |
|[Lithuania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Lithuania.png)| 136   |      81|      29.045|   0.1%/ ***|   0.1%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Madagascar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Madagascar.png)|  90   |     169|       6.442|   3.3%/ 21|   2.8%/ 25|   2.6%/ 26|   2.5%/ 27 |
|[Malaysia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Malaysia.png)| 136   |     125|       3.831|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mali](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mali.png)| 136   |     125|       6.190|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Mauritania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mauritania.png)| 136   |     157|      38.622|   0.0%/ ***|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Mexico](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mexico.png)| 136   |   56178|     443.824|   1.4%/ 51|   1.3%/ 51|   1.3%/ 51|   1.3%/ 51 |
|[Moldova](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Moldova.png)| 136   |     889|     331.448|   0.9%/ 74|   0.9%/ 76|   0.9%/ 76|   0.9%/ 77 |
|[Morocco](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Morocco.png)| 136   |     577|      16.089|   3.6%/ 19|   4.0%/ 17|   4.1%/ 17|   4.2%/ 16 |
|[Mozambique](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Mozambique.png)|  82   |      19|       0.640|   3.4%/ 20|   3.6%/ 19|   3.7%/ 19|   3.7%/ 18 |
|[Namibia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Namibia.png)|  36   |      31|      12.496|   8.3%/  8|   8.1%/  8|   9.1%/  7|  10.4%/  6 |
|[Nepal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nepal.png)|  91   |      97|       3.220|   4.8%/ 14|   5.9%/ 12|   6.2%/ 11|   6.5%/ 11 |
|[Netherlands](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Netherlands.png)| 136   |    6185|     354.307|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[New Zealand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/New%20Zealand.png)| 136   |      22|       4.418|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Nicaragua](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nicaragua.png)| 136   |     130|      20.121|   0.8%/ 90|   0.7%/103|   0.7%/106|   0.6%/110 |
|[Niger](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Niger.png)| 136   |      69|       3.092|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Nigeria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Nigeria.png)| 136   |     979|       4.750|   0.7%/106|   0.6%/121|   0.6%/125|   0.5%/130 |
|[North Macedonia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/North%20Macedonia.png)| 136   |     548|     263.615|   0.7%/100|   0.5%/135|   0.5%/148|   0.4%/164 |
|[Norway](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Norway.png)| 136   |     256|      47.776|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Oman](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Oman.png)| 136   |     568|     121.705|   1.9%/ 37|   1.7%/ 40|   1.7%/ 41|   1.7%/ 41 |
|[Pakistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Pakistan.png)| 136   |    6186|      28.202|   0.3%/259|   0.2%/337|   0.2%/362|   0.2%/391 |
|[Panama](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Panama.png)| 136   |    1782|     422.433|   1.5%/ 47|   1.3%/ 55|   1.2%/ 57|   1.1%/ 60 |
|[Papua New Guinea](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Papua%20New%20Guinea.png)|  19   |       3|       0.336|  10.3%/  7|   0.0%/ --|   0.0%/ --|   0.0%/ -- |
|[Paraguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Paraguay.png)| 136   |      96|      13.365|   5.4%/ 13|   5.9%/ 12|   6.1%/ 11|   6.2%/ 11 |
|[Peru](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Peru.png)| 136   |   23317|     725.677|   1.0%/ 67|   1.0%/ 71|   1.0%/ 72|   1.0%/ 73 |
|[Philippines](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Philippines.png)| 136   |    2400|      22.114|   1.5%/ 48|   1.7%/ 42|   1.7%/ 40|   1.8%/ 39 |
|[Poland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Poland.png)| 136   |    1852|      48.249|   0.6%/118|   0.6%/110|   0.6%/108|   0.7%/106 |
|[Portugal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Portugal.png)| 136   |    1771|     172.319|   0.2%/391|   0.2%/393|   0.2%/392|   0.2%/391 |
|[Qatar](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Qatar.png)| 136   |     192|      69.795|   0.8%/ 88|   0.8%/ 87|   0.8%/ 87|   0.8%/ 86 |
|[Romania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Romania.png)| 136   |    2885|     148.690|   1.6%/ 44|   1.7%/ 41|   1.7%/ 40|   1.7%/ 40 |
|[Russia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Russia.png)| 136   |   15565|     106.066|   0.8%/ 86|   0.8%/ 92|   0.7%/ 94|   0.7%/ 95 |
|[Rwanda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Rwanda.png)|  77   |       8|       0.660|   0.0%/ ***|   0.0%/ ***|   0.0%/ --|   0.0%/ -- |
|[Saudi Arabia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Saudi%20Arabia.png)| 136   |    3344|      97.718|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63|   1.1%/ 63 |
|[Senegal](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Senegal.png)| 136   |     250|      15.413|   1.4%/ 49|   1.3%/ 51|   1.3%/ 52|   1.3%/ 53 |
|[Serbia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Serbia.png)| 136   |     681|      97.849|   1.1%/ 63|   0.9%/ 75|   0.9%/ 79|   0.8%/ 84 |
|[Sierra Leone](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sierra%20Leone.png)| 114   |      69|       8.743|   0.3%/268|   0.3%/235|   0.3%/227|   0.3%/220 |
|[Singapore](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Singapore.png)| 136   |      27|       4.734|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Slovakia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovakia.png)| 136   |      31|       5.702|   0.0%/ ***|   0.0%/ --|   0.0%/ ***|   0.0%/ *** |
|[Slovenia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Slovenia.png)| 136   |     130|      62.229|   0.6%/108|   0.7%/ 97|   0.7%/ 95|   0.7%/ 93 |
|[Somalia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Somalia.png)| 129   |      93|       5.852|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[South Africa](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/South%20Africa.png)| 136   |   11975|     203.749|   2.7%/ 25|   2.4%/ 28|   2.4%/ 29|   2.3%/ 30 |
|[Spain](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Spain.png)| 136   |   28580|     606.793|   0.0%/ ***|   0.0%/ ***|   0.1%/ ***|   0.1%/ *** |
|[Sri Lanka](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sri%20Lanka.png)| 136   |      11|       0.505|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Sudan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sudan.png)| 136   |     800|      18.844|   0.5%/139|   0.4%/154|   0.4%/158|   0.4%/163 |
|[Sweden](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Sweden.png)| 136   |    5793|     560.315|   0.1%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Switzerland](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Switzerland.png)| 136   |    1991|     231.413|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Syria](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Syria.png)| 136   |      58|       3.331|   1.3%/ 54|   0.7%/103|   0.5%/134|   0.4%/190 |
|[Tanzania](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tanzania.png)| 136   |      21|       0.376|   0.0%/ ***|   0.0%/ ***|   0.0%/ ***|   0.0%/ *** |
|[Thailand](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Thailand.png)| 136   |      58|       0.872|   0.0%/ --|   0.0%/ --|   0.0%/ ***|   0.0%/ -- |
|[Togo](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Togo.png)| 136   |      26|       3.506|   2.6%/ 26|   3.2%/ 22|   3.3%/ 21|   3.4%/ 20 |
|[Trinidad and Tobago](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Trinidad%20and%20Tobago.png)| 136   |       8|       5.865|   0.0%/ --|   0.0%/ --|   0.0%/ --|   0.0%/ *** |
|[Tunisia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Tunisia.png)| 136   |      52|       4.423|   0.3%/202|   0.5%/153|   0.5%/144|   0.5%/136 |
|[Turkey](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Turkey.png)| 136   |    5934|      71.357|   0.3%/243|   0.3%/247|   0.3%/248|   0.3%/250 |
|[US](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/US.png)| 136   |  168753|     512.081|   0.7%/ 97|   0.7%/ 96|   0.7%/ 96|   0.7%/ 96 |
|[Uganda](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uganda.png)|  22   |      13|       0.318|   7.9%/  9|   9.8%/  7|   9.3%/  7|  12.1%/  6 |
|[Ukraine](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Ukraine.png)| 136   |    2044|      48.815|   1.3%/ 52|   1.4%/ 49|   1.4%/ 49|   1.4%/ 48 |
|[United Arab Emirates](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Arab%20Emirates.png)| 136   |     361|      36.453|   0.2%/328|   0.2%/355|   0.2%/363|   0.2%/372 |
|[United Kingdom](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/United%20Kingdom.png)| 136   |   46894|     705.856|   0.1%/656|   0.1%/739|   0.1%/765|   0.1%/792 |
|[Uruguay](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uruguay.png)| 136   |      38|      10.781|   0.3%/198|   0.2%/287|   0.2%/326|   0.2%/376 |
|[Uzbekistan](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Uzbekistan.png)| 136   |     231|       6.757|   3.4%/ 20|   3.1%/ 22|   3.0%/ 23|   2.9%/ 23 |
|[Venezuela](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Venezuela.png)| 136   |     264|       8.186|   3.6%/ 19|   3.7%/ 18|   3.8%/ 18|   3.8%/ 18 |
|[Vietnam](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Vietnam.png)|  15   |      24|       0.249|   3.6%/ 19|  11.5%/  6|  11.9%/  6|  14.5%/  5 |
|[Zambia](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zambia.png)| 135   |     257|      14.387|   5.3%/ 13|   6.1%/ 11|   6.3%/ 11|   6.4%/ 11 |
|[Zimbabwe](https://github.com/lintondf/COVIDtoTimeSeries/raw/master/analysis/countries/Zimbabwe.png)| 136   |     145|       9.539|   6.6%/ 10|   6.1%/ 11|   5.9%/ 12|   5.7%/ 12 |

